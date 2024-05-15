---
Penetration Testing Challenge
---

# Relevant — Writeup

## Overview
### Relevant — Writeup
### Relevant — Writeup
![|333](https://tryhackme-images.s3.amazonaws.com/room-icons/10524728b2b462e8d164efe4e67ed087.jpeg)
### Pre-Engagement Briefing
You have been assigned to a client that wants a penetration test conducted on an environment due to be released to production in seven days.
Scope of Work
The client requests that an engineer conducts an assessment of the provided virtual environment. The client has asked that minimal information be provided about the assessment, wanting the engagement conducted from the eyes of a malicious actor (black box penetration test).  The client has asked that you secure two flags (no location provided) as proof of exploitation:
User.txt
Root.txt
Additionally, the client has provided the following scope allowances:
Any tools or techniques are permitted in this engagement, however we ask that you attempt manual exploitation first
Locate and note all vulnerabilities found
Submit the flags discovered to the dashboard
Only the IP address assigned to your machine is in scope
Find and report ALL vulnerabilities (yes, there is more than one path to root)
(Roleplay off)
I encourage you to approach this challenge as an actual penetration test. Consider writing a report, to include an executive summary, vulnerability and exploitation assessment, and remediation suggestions, as this will benefit you in preparation for the eLearnSecurity Certified Professional Penetration Tester or career as a penetration tester in the field.
Note - Nothing in this room requires Metasploit
Machine may take up to 5 minutes for all services to start.
**Writeups will not be accepted for this room.**

## Enumeration
```text
┌──(kali㉿kali)-[~/skynet/daily_bugle]
└─$ sudo nmap -sC -sV -T4 -A -Pn -sS -n -O 10.10.3.92   
[sudo] password for kali: 
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-27 22:35 EDT
Nmap scan report for 10.10.3.92
Host is up (0.20s latency).
Not shown: 995 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-title: IIS Windows Server
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds  Windows Server 2016 Standard Evaluation 14393 microsoft-ds
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: RELEVANT
|   NetBIOS_Domain_Name: RELEVANT
|   NetBIOS_Computer_Name: RELEVANT
|   DNS_Domain_Name: Relevant
|   DNS_Computer_Name: Relevant
|   Product_Version: 10.0.14393
|_  System_Time: 2022-09-28T02:36:21+00:00
| ssl-cert: Subject: commonName=Relevant
| Not valid before: 2022-09-27T02:35:08
|_Not valid after:  2023-03-29T02:35:08
|_ssl-date: 2022-09-28T02:37:00+00:00; 0s from scanner time.
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2016|2012 (90%)
OS CPE: cpe:/o:microsoft:windows_server_2016 cpe:/o:microsoft:windows_server_2012
Aggressive OS guesses: Microsoft Windows Server 2016 (90%), Microsoft Windows Server 2012 (85%), Microsoft Windows Server 2012 or Windows Server 2012 R2 (85%), Microsoft Windows Server 2012 R2 (85%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-09-28T02:36:24
|_  start_date: 2022-09-28T02:35:09
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard Evaluation 14393 (Windows Server 2016 Standard Evaluation 6.3)
|   Computer name: Relevant
|   NetBIOS computer name: RELEVANT\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2022-09-27T19:36:21-07:00
|_clock-skew: mean: 1h24m00s, deviation: 3h07m50s, median: 0s

TRACEROUTE (using port 3389/tcp)
HOP RTT       ADDRESS
1   199.13 ms 10.11.0.1
2   199.85 ms 10.10.3.92

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 70.82 seconds
zsh: segmentation fault  sudo nmap -sC -sV -T4 -A -Pn -sS -n -O 10.10.3.92
```
```text
┌──(kali㉿kali)-[~/skynet/daily_bugle]
└─$ smbclient -L 10.10.3.92                           
Password for [WORKGROUP\kali]:

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        nt4wrksv        Disk      
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.3.92 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```
```text
┌──(kali㉿kali)-[~/skynet/daily_bugle]
└─$ smbclient //10.10.3.92/nt4wrksv    
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sat Jul 25 17:46:04 2020
  ..                                  D        0  Sat Jul 25 17:46:04 2020
  passwords.txt                       A       98  Sat Jul 25 11:15:33 2020

                7735807 blocks of size 4096. 4950803 blocks available
smb: \> get passwords.txt
getting file \passwords.txt of size 98 as passwords.txt (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec)
smb: \> exit
```
```text
┌──(kali㉿kali)-[~/skynet/daily_bugle]
└─$ ls
jonah.hash  joomblah.py  passwords.txt
```
```text
┌──(kali㉿kali)-[~/skynet/daily_bugle]
└─$ cat passwords.txt 
[User Passwords - Encoded]
Qm9iIC0gIVBAJCRXMHJEITEyMw==
QmlsbCAtIEp1dzRubmFNNG40MjA2OTY5NjkhJCQk 

Bob - !P@$$W0rD!123
Bill - Juw4nnaM4n420696969!$$$

rustscan

Open 10.10.3.92:49663
Open 10.10.3.92:49667
Open 10.10.3.92:49669

49663/tcp open  http          Microsoft IIS httpd 10.0
49667/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC

Web

Scanning the hidden web directories on both ports 80/tcp and 49663/tcp takes a while but is worth it (with directory-list-2.3-medium.txt). Nothing interesting stands out on port 80/tcp, but we find that the nt4wrksv share found previously is also available as a hidden location on port 49663/tcp. 

http://10.10.3.92:49663/nt4wrksv/passwords.txt
[User Passwords - Encoded]
Qm9iIC0gIVBAJCRXMHJEITEyMw==
QmlsbCAtIEp1dzRubmFNNG40MjA2OTY5NjkhJCQk

Exploiting SMB

The handy AutoBlue-MS17-010 script can be used to exploit the MS17-010 Eternal Blue vulnerability:

According to the instructions on the GitHub repository, all that is required is to specify the target IP address, SMB port and valid credentials to authenticate if required, and a SYSTEM shell will be returned.

Cloning the Git Repository locally:

here is a keylogger found 0.10 so don't enter ur github account!! it is not the repository!!
──(kali㉿kali)-[~/skynet/daily_bugle]
└─$ git clone https://github.com/3ndG4me/AutoBlue-MS17-0.10.git         
Cloning into 'AutoBlue-MS17-0.10'...
Username for 'https://github.com': exit
Password for 'https://exit@github.com':
```
```text
┌──(kali㉿kali)-[~/skynet/daily_bugle]
└─$ ls
jonah.hash  joomblah.py  passwords.txt  shell.aspx
                                                                                                                  

the correct one
```
```text
┌──(kali㉿kali)-[~/skynet/daily_bugle]
└─$ git clone https://github.com/3ndG4me/AutoBlue-MS17-010.git 
Cloning into 'AutoBlue-MS17-010'...
