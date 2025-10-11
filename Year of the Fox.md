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
