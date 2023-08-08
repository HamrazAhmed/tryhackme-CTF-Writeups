# Fusion Corp — Writeup

## Overview
### Fusion Corp — Writeup
### Fusion Corp — Writeup
----
Fusion Corp said they got everything patched... did they?
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/c7c5cbaebf5b3c858e7c37f4213ab6e1.jpeg)
Start Machine
Please give the VM 5-10 minutes to fully boot.
You had an engagement a while ago for Fusion Corp. They contacted you saying they've patched everything reported and you can start retesting.
Answer the questions below

## Enumeration
```text
──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.50.4 --ulimit 5500 -b 65535 -- -A -Pn
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

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.50.4:53
Open 10.10.50.4:80
Open 10.10.50.4:88
Open 10.10.50.4:135
Open 10.10.50.4:139
Open 10.10.50.4:389
Open 10.10.50.4:445
Open 10.10.50.4:464
Open 10.10.50.4:593
Open 10.10.50.4:3269
Open 10.10.50.4:3268
Open 10.10.50.4:3389
Open 10.10.50.4:5985
Open 10.10.50.4:9389
Open 10.10.50.4:49666
Open 10.10.50.4:49677
Open 10.10.50.4:49668
Open 10.10.50.4:49669
Open 10.10.50.4:49670
Open 10.10.50.4:49689
Open 10.10.50.4:49699
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
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.50.4 [21 ports]
Discovered open port 53/tcp on 10.10.50.4
Discovered open port 445/tcp on 10.10.50.4
Discovered open port 135/tcp on 10.10.50.4
Discovered open port 3389/tcp on 10.10.50.4
Discovered open port 139/tcp on 10.10.50.4
Discovered open port 80/tcp on 10.10.50.4
Discovered open port 49699/tcp on 10.10.50.4
Discovered open port 49689/tcp on 10.10.50.4
Discovered open port 593/tcp on 10.10.50.4
Discovered open port 88/tcp on 10.10.50.4
Discovered open port 49666/tcp on 10.10.50.4
Discovered open port 3269/tcp on 10.10.50.4
Discovered open port 49670/tcp on 10.10.50.4
Discovered open port 5985/tcp on 10.10.50.4
Discovered open port 389/tcp on 10.10.50.4
Discovered open port 49677/tcp on 10.10.50.4
Discovered open port 9389/tcp on 10.10.50.4
Discovered open port 49668/tcp on 10.10.50.4
Discovered open port 49669/tcp on 10.10.50.4
Discovered open port 464/tcp on 10.10.50.4
Discovered open port 3268/tcp on 10.10.50.4
Completed Connect Scan (21 total ports)
Initiating Service scan
Scanning 21 services on 10.10.50.4
Completed Service scan (21 services on 1 host)
NSE: Script scanning 10.10.50.4.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
NSE Timing: About 99.97% done; ETC: 14:39 (0:00:00 remaining)
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.50.4
Host is up, received user-set (0.20s latency).

PORT      STATE SERVICE       REASON  VERSION
53/tcp    open  domain        syn-ack Simple DNS Plus
80/tcp    open  http          syn-ack Microsoft IIS httpd 10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-favicon: Unknown favicon MD5: FED84E16B6CCFE88EE7FFAAE5DFEFD34
|_http-server-header: Microsoft-IIS/10.0
|_http-title: eBusiness Bootstrap Template
88/tcp    open  kerberos-sec  syn-ack Microsoft Windows Kerberos (server time: :18Z)
135/tcp   open  msrpc         syn-ack Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack Microsoft Windows netbios-ssn
389/tcp   open  ldap          syn-ack Microsoft Windows Active Directory LDAP (Domain: fusion.corp0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds? syn-ack
464/tcp   open  kpasswd5?     syn-ack
593/tcp   open  ncacn_http    syn-ack Microsoft Windows RPC over HTTP 1.0
3268/tcp  open  ldap          syn-ack Microsoft Windows Active Directory LDAP (Domain: fusion.corp0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped    syn-ack
3389/tcp  open  ms-wbt-server syn-ack Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: FUSION
|   NetBIOS_Domain_Name: FUSION
|   NetBIOS_Computer_Name: FUSION-DC
|   DNS_Domain_Name: fusion.corp
|   DNS_Computer_Name: Fusion-DC.fusion.corp
|   Product_Version: 10.0.17763
|_  System_Time: 2023-07-21T18:39:10+00:00
| ssl-cert: Subject: commonName=Fusion-DC.fusion.corp
| Issuer: commonName=Fusion-DC.fusion.corp
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| MD5:   d896df4ba43ee9f0996019b5e46d6678
| SHA-1: e1b0787c13757d619c77802bafdefb5ccd339401
| -----BEGIN CERTIFICATE-----
| MIIC7jCCAdagAwIBAgIQQxCmr+BQ5qRDlkCauFFsZTANBgkqhkiG9w0BAQsFADAg
| MR4wHAYDVQQDExVGdXNpb24tREMuZnVzaW9uLmNvcnAwHhcNMjMwNzIwMTgwNjM2
| WhcNMjQwMTE5MTgwNjM2WjAgMR4wHAYDVQQDExVGdXNpb24tREMuZnVzaW9uLmNv
| cnAwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDW9rDNe6wuLClHzVZd
| 6wm1tAC0tUHPWFK043xOA+2tU4My40Y7Nnmb+3GMEA/wZdcVtkOBDOwixDDE8iKv
| vRwE9NmOhy3/4NA7itsoS6lyTjeUlbzR4xKlC4gNAvbrmAiYziIVB6USwU1WWJUC
| lfZCAChOh9uyGuBvWAAZRnVyj1n57OhuD6nQjKRpBEEMLdZoAQS1rYv2VOrWhhLt
| yV9Cpr+7mdqMDCY5Lz0zbe6OFfrUPcE2Un185vLuiavMjPFumosPvw03skdRHyN6
| FJdF2atj9H51X2jBxlZdxJxTyZ03lmEPd1dH7rKv+JxDTLfAS6CPev424SAtsMEn
| 4q29AgMBAAGjJDAiMBMGA1UdJQQMMAoGCCsGAQUFBwMBMAsGA1UdDwQEAwIEMDAN
| BgkqhkiG9w0BAQsFAAOCAQEAAzStTi1/p0tzqS5fj5tnyNwFWdkjDgrcBVprwGOw
| kvmb0WMwOOluAal1m1OKOwcZnIwWzXRrs3BSJewj4Tw2hXo7rok7sySogRVoqNG7
| 8W4348VgdaFcIlMD7m3HSj9k8GDajGgFtVjUzVYGhWIAanFkWI9YPgYDmU3NEA7m
| vPQKwTMK35dBzBIGO/I3u1QUaoyCL7uCYNi2V/ZhZtwPpaySQkZbuzWLAQ9qhi/H
| VtuvOCY1u74IlaF0nd13cqsActxzNvLGLGGPpb7BFrX+o/w2M7jF58zUjnW+J5Vm
| dObg4LdihFHdmQgmfp1RTStEfBoHVUkecOr9RD2OdEM7xw==
|_-----END CERTIFICATE-----
5985/tcp  open  http          syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        syn-ack .NET Message Framing
49666/tcp open  msrpc         syn-ack Microsoft Windows RPC
49668/tcp open  msrpc         syn-ack Microsoft Windows RPC
49669/tcp open  ncacn_http    syn-ack Microsoft Windows RPC over HTTP 1.0
49670/tcp open  msrpc         syn-ack Microsoft Windows RPC
49677/tcp open  msrpc         syn-ack Microsoft Windows RPC
49689/tcp open  msrpc         syn-ack Microsoft Windows RPC
49699/tcp open  msrpc         syn-ack Microsoft Windows RPC
Service Info: Host: FUSION-DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 29730/tcp): CLEAN (Timeout)
|   Check 2 (port 60869/tcp): CLEAN (Timeout)
|   Check 3 (port 41214/udp): CLEAN (Timeout)
|   Check 4 (port 21353/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-time: 
|   date: 2023-07-21T18:39:13
|_  start_date: N/A
|_clock-skew: mean: 0s, deviation: 0s, median: 0s
| smb2-security-mode: 
|   311: 
|_    Message signing enabled and required

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
Nmap done: 1 IP address (1 host up) scanned in 104.40 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ dirsearch -u http://10.10.50.4/ -i200,301,302,401 -w /usr/share/wordlists/dirb/common.txt

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 4613

Output File: /home/witty/.dirsearch/reports/10.10.50.4/-_23-07-21_14-42-31.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-07-21_14-42-31.log

Target: http://10.10.50.4/

[14:42:32] Starting: 
[14:42:41] 301 -  148B  - /backup  ->  http://10.10.50.4/backup/
[14:42:47] 301 -  145B  - /css  ->  http://10.10.50.4/css/
[14:42:57] 301 -  145B  - /img  ->  http://10.10.50.4/img/
[14:42:59] 200 -   53KB - /index.html
[14:43:00] 301 -  144B  - /js  ->  http://10.10.50.4/js/
[14:43:01] 301 -  145B  - /lib  ->  http://10.10.50.4/lib/

Task Completed

go to backup
open employees.ods

usernames

jmickel
aarnold
llinda
jpowel
dvroslav
tjefferson
nmaurin
mladovic
lparker
kgarland
dpertersen

┌──(witty㉿kali)-[~/Downloads]
└─$ cat username_fusion 
jmickel
aarnold
llinda
jpowel
dvroslav
tjefferson
nmaurin
mladovic
lparker
kgarland
dpertersen

┌──(witty㉿kali)-[~/Downloads]
└─$ rpcclient -U% 10.10.50.4   
rpcclient $> enumdomusers
result was NT_STATUS_ACCESS_DENIED
rpcclient $> enumdomains
result was NT_STATUS_ACCESS_DENIED
rpcclient $> enumprivs
found 35 privileges

SeCreateTokenPrivilege 		0:2 (0x0:0x2)
SeAssignPrimaryTokenPrivilege 		0:3 (0x0:0x3)
SeLockMemoryPrivilege 		0:4 (0x0:0x4)
SeIncreaseQuotaPrivilege 		0:5 (0x0:0x5)
SeMachineAccountPrivilege 		0:6 (0x0:0x6)
SeTcbPrivilege 		0:7 (0x0:0x7)
SeSecurityPrivilege 		0:8 (0x0:0x8)
SeTakeOwnershipPrivilege 		0:9 (0x0:0x9)
SeLoadDriverPrivilege 		0:10 (0x0:0xa)
SeSystemProfilePrivilege 		0:11 (0x0:0xb)
SeSystemtimePrivilege 		0:12 (0x0:0xc)
SeProfileSingleProcessPrivilege 		0:13 (0x0:0xd)
SeIncreaseBasePriorityPrivilege 		0:14 (0x0:0xe)
SeCreatePagefilePrivilege 		0:15 (0x0:0xf)
SeCreatePermanentPrivilege 		0:16 (0x0:0x10)
SeBackupPrivilege 		0:17 (0x0:0x11)
SeRestorePrivilege 		0:18 (0x0:0x12)
SeShutdownPrivilege 		0:19 (0x0:0x13)
SeDebugPrivilege 		0:20 (0x0:0x14)
SeAuditPrivilege 		0:21 (0x0:0x15)
SeSystemEnvironmentPrivilege 		0:22 (0x0:0x16)
SeChangeNotifyPrivilege 		0:23 (0x0:0x17)
SeRemoteShutdownPrivilege 		0:24 (0x0:0x18)
SeUndockPrivilege 		0:25 (0x0:0x19)
SeSyncAgentPrivilege 		0:26 (0x0:0x1a)
SeEnableDelegationPrivilege 		0:27 (0x0:0x1b)
SeManageVolumePrivilege 		0:28 (0x0:0x1c)
SeImpersonatePrivilege 		0:29 (0x0:0x1d)
SeCreateGlobalPrivilege 		0:30 (0x0:0x1e)
SeTrustedCredManAccessPrivilege 		0:31 (0x0:0x1f)
SeRelabelPrivilege 		0:32 (0x0:0x20)
SeIncreaseWorkingSetPrivilege 		0:33 (0x0:0x21)
SeTimeZonePrivilege 		0:34 (0x0:0x22)
SeCreateSymbolicLinkPrivilege 		0:35 (0x0:0x23)
SeDelegateSessionUserImpersonatePrivilege 		0:36 (0x0:0x24)

┌──(witty㉿kali)-[~/Downloads]
└─$ rdesktop -f -u "" 10.10.50.4   
Autoselecting keyboard map 'en-us' from locale

ATTENTION! The server uses and invalid security certificate which can not be trusted for
the following identified reasons(s);

 1. Certificate issuer is not trusted by this system.

     Issuer: CN=Fusion-DC.fusion.corp

Review the following certificate info before you trust it to be added as an exception.
If you do not trust the certificate the connection atempt will be aborted:

    Subject: CN=Fusion-DC.fusion.corp
     Issuer: CN=Fusion-DC.fusion.corp
 Valid From: Thu Jul 20 14:06:36 2023
         To: Fri Jan 19 13:06:36 2024

  Certificate fingerprints:

       sha1: e1b0787c13757d619c77802bafdefb5ccd339401
     sha256: b80d5c07940fa8efc1a2d784895649ea521228f453a970d11087a08f83214f16

Do you trust this certificate (yes/no)? yes
Failed to initialize NLA, do you have correct Kerberos TGT initialized ?
Failed to connect, CredSSP required by server (check if server has disabled old TLS versions, if yes use -V option).

┌──(witty㉿kali)-[~/Downloads]
└─$ crackmapexec smb 10.10.50.4 -u guest -p ""
SMB         10.10.50.4      445    FUSION-DC        [*] Windows 10.0 Build 17763 x64 (name:FUSION-DC) (domain:fusion.corp) (signing:True) (SMBv1:False)
SMB         10.10.50.4      445    FUSION-DC        [-] fusion.corp\guest: STATUS_ACCOUNT_DISABLED 
                                                                                   
┌──(witty㉿kali)-[~/Downloads]
└─$ crackmapexec smb 10.10.50.4 -u kali -p "" 
SMB         10.10.50.4      445    FUSION-DC        [*] Windows 10.0 Build 17763 x64 (name:FUSION-DC) (domain:fusion.corp) (signing:True) (SMBv1:False)
SMB         10.10.50.4      445    FUSION-DC        [-] fusion.corp\kali: STATUS_LOGON_FAILURE

┌──(witty㉿kali)-[~/Downloads]
└─$ ldapsearch -x -s base namingcontexts -H ldap://10.10.50.4
```
```text
# extended LDIF
#
```
```text
# LDAPv3
```
```text
# base <> (default) with scope baseObject
```
```text
# filter: (objectclass=*)
```
```text
# requesting: namingcontexts 
#

#
dn:
namingcontexts: DC=fusion,DC=corp
namingcontexts: CN=Configuration,DC=fusion,DC=corp
namingcontexts: CN=Schema,CN=Configuration,DC=fusion,DC=corp
namingcontexts: DC=DomainDnsZones,DC=fusion,DC=corp
namingcontexts: DC=ForestDnsZones,DC=fusion,DC=corp
```
```text
# search result
search: 2
result: 0 Success
```
```text
# numResponses: 2
```

## Exploitation
```text
# numEntries: 1

┌──(witty㉿kali)-[~/Downloads]
└─$ ./kerbrute userenum -d 'fusion.corp' --dc 10.10.50.4 username_fusion 

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
