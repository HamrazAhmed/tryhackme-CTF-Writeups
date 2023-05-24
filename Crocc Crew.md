# Crocc Crew — Writeup

## Overview
### Crocc Crew — Writeup
### Crocc Crew — Writeup
----
Crocc Crew has created a backdoor on a Cooctus Corp Domain Controller. We're calling in the experts to find the real back door!
----
![](https://i.imgur.com/XXcnchz.png)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/d387f5c6b5c2bfd07451dd27c187e185.png)
### Task 2  Hack Back!
﻿**The Crocc Crew Strikes!**
You just gained initial access into a segmented part of the network and you've found only one device -- A domain controller. It appears that it's already been hacked... Can you find out who did it?
![](https://i.imgur.com/qbQ85Im.png)
_Check out the Crocc Crew merch on Varg's [Redbubble](https://www.redbubble.com/people/Vargles/explore?page=1&sortOrder=recent)._
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ ping 10.10.175.192                                                  
PING 10.10.175.192 (10.10.175.192) 56(84) bytes of data.
64 bytes from 10.10.175.192: icmp_seq=1 ttl=127 time=286 ms
64 bytes from 10.10.175.192: icmp_seq=2 ttl=127 time=300 ms
^C
--- 10.10.175.192 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1003ms
rtt min/avg/max/mdev = 285.729/292.706/299.683/6.977 ms

┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.175.192 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Real hackers hack time ⌛

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.175.192:53
Open 10.10.175.192:80
Open 10.10.175.192:88
Open 10.10.175.192:135
Open 10.10.175.192:139
Open 10.10.175.192:389
Open 10.10.175.192:445
Open 10.10.175.192:464
Open 10.10.175.192:593
Open 10.10.175.192:3268
Open 10.10.175.192:3389
Open 10.10.175.192:9389
Open 10.10.175.192:49671
Open 10.10.175.192:49667
Open 10.10.175.192:49668
Open 10.10.175.192:49669
Open 10.10.175.192:49670
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
DNS resolution of 1 IPs took 0.04s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.175.192 [17 ports]
Discovered open port 3389/tcp on 10.10.175.192
Discovered open port 139/tcp on 10.10.175.192
Discovered open port 53/tcp on 10.10.175.192
Discovered open port 445/tcp on 10.10.175.192
Discovered open port 135/tcp on 10.10.175.192
Discovered open port 80/tcp on 10.10.175.192
Discovered open port 593/tcp on 10.10.175.192
Discovered open port 49668/tcp on 10.10.175.192
Discovered open port 389/tcp on 10.10.175.192
Discovered open port 464/tcp on 10.10.175.192
Discovered open port 3268/tcp on 10.10.175.192
Discovered open port 9389/tcp on 10.10.175.192
Discovered open port 49670/tcp on 10.10.175.192
Discovered open port 49669/tcp on 10.10.175.192
Discovered open port 88/tcp on 10.10.175.192
Discovered open port 49671/tcp on 10.10.175.192
Discovered open port 49667/tcp on 10.10.175.192
Completed Connect Scan (17 total ports)
Initiating Service scan
Scanning 17 services on 10.10.175.192
Completed Service scan (17 services on 1 host)
NSE: Script scanning 10.10.175.192.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
NSE Timing: About 99.79% done; ETC: 22:44 (0:00:00 remaining)
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.175.192
Host is up, received user-set (0.20s latency).

PORT      STATE SERVICE       REASON  VERSION
53/tcp    open  domain        syn-ack Simple DNS Plus
80/tcp    open  http          syn-ack Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
88/tcp    open  kerberos-sec  syn-ack Microsoft Windows Kerberos (server time: :12Z)
135/tcp   open  msrpc         syn-ack Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack Microsoft Windows netbios-ssn
389/tcp   open  ldap          syn-ack Microsoft Windows Active Directory LDAP (Domain: COOCTUS.CORP0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds? syn-ack
464/tcp   open  kpasswd5?     syn-ack
593/tcp   open  ncacn_http    syn-ack Microsoft Windows RPC over HTTP 1.0
3268/tcp  open  ldap          syn-ack Microsoft Windows Active Directory LDAP (Domain: COOCTUS.CORP0., Site: Default-First-Site-Name)
3389/tcp  open  ms-wbt-server syn-ack Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: COOCTUS
|   NetBIOS_Domain_Name: COOCTUS
|   NetBIOS_Computer_Name: DC
|   DNS_Domain_Name: COOCTUS.CORP
|   DNS_Computer_Name: DC.COOCTUS.CORP
|   Product_Version: 10.0.17763
|_  System_Time: 2023-06-30T02:44:03+00:00
| ssl-cert: Subject: commonName=DC.COOCTUS.CORP
| Issuer: commonName=DC.COOCTUS.CORP
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| MD5:   5630c25111fd1fb81aa47fc421f16038
| SHA-1: 62765024f4d1b03511a8cf97e7012e50b85e2ff2
| -----BEGIN CERTIFICATE-----
| MIIC4jCCAcqgAwIBAgIQLvfcEI/E47tC6Oju696q3DANBgkqhkiG9w0BAQsFADAa
| MRgwFgYDVQQDEw9EQy5DT09DVFVTLkNPUlAwHhcNMjMwNjI5MDIzODE3WhcNMjMx
| MjI5MDIzODE3WjAaMRgwFgYDVQQDEw9EQy5DT09DVFVTLkNPUlAwggEiMA0GCSqG
| SIb3DQEBAQUAA4IBDwAwggEKAoIBAQC6e4hDni6oS5bSCboHYrLLbVChEVvKnYaM
| rmNu6wDnFlhWoIfI8FzFdjhwKymDl6plizQ6LBkwQyMUfkvFleTUTl9c1ugTFpgm
| wNd425dSBSZMPMIGb3W4LEHDc7h0cAe6oTegYz6LJ50+mwQ6ea8/U1TZr7R4AnU5
| K5NPyH5sXqibOjyaixF2EZzkWuYRyfNMvIUB1NnU/5aiZ9lsdVK/lgskMf1URZkt
| ZnhBUpB+nWLTx3Q/7DTB8on6+Q+ZarA0CD21Fa8cYN3QwkDBitJlBVa891SWbR0J
| tuhQdG8S3jvVmzkQ0XPZa1eF3aTxMD30uW3VFBpwDg6wcWagjV8dAgMBAAGjJDAi
| MBMGA1UdJQQMMAoGCCsGAQUFBwMBMAsGA1UdDwQEAwIEMDANBgkqhkiG9w0BAQsF
| AAOCAQEAiBprThi/yJ2IpQ48w0tzcO6oU/RiwoUpWIojYQOFbfPlTc4AC6tPZlTu
| lHNM3kQ3e164+tUL97S338nlb3nK2FgqsyCeK6d2wfBHrZLoyANPXutGzFBXTegR
| sOP+c3Z9zQ3D+RulKjtxEDEX3NVmB/eqkvWxdV1kUrSt9V+iIMvuHTse2NgXN0hD
| usFE4XYL01LpWIRvgQsmP9+LdAElTPRfZaKW32VJznpSRD6t8/LdtOCrmcvk2hc9
| baDwwkkqIdx2R4e9sxKJt7BFzAlqIOKCl4CHzvbZsRPI1TITDEyp6Pd+OKOmdqz9
| X50w9t4A6soiCfD3gsMy6OESv9OpUA==
|_-----END CERTIFICATE-----
9389/tcp  open  mc-nmf        syn-ack .NET Message Framing
49667/tcp open  msrpc         syn-ack Microsoft Windows RPC
49668/tcp open  ncacn_http    syn-ack Microsoft Windows RPC over HTTP 1.0
49669/tcp open  msrpc         syn-ack Microsoft Windows RPC
49670/tcp open  msrpc         syn-ack Microsoft Windows RPC
49671/tcp open  msrpc         syn-ack Microsoft Windows RPC
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 20816/tcp): CLEAN (Timeout)
|   Check 2 (port 52689/tcp): CLEAN (Timeout)
|   Check 3 (port 62928/udp): CLEAN (Timeout)
|   Check 4 (port 65279/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   311: 
|_    Message signing enabled and required
|_clock-skew: mean: 0s, deviation: 0s, median: 0s
| smb2-time: 
|   date: 2023-06-30T02:44:04
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
Nmap done: 1 IP address (1 host up) scanned in 105.43 seconds

http://10.10.175.192/robots.txt

User-Agent: *
Disallow:
/robots.txt
/db-config.bak
/backdoor.php

<script>
$('body').terminal({
    hello: function(what) {
        this.echo('Hello, ' + what +
                  '. Wellcome to this terminal.');
    }
}, {
    greetings: 'CroccCrew >:)'
});
</script>

http://10.10.175.192/db-config.bak

<?php

$servername = "db.cooctus.corp";
$username = "C00ctusAdm1n";
$password = "B4dt0th3b0n3";

// Create connection $conn = new mysqli($servername, $username, $password);

// Check connection if ($conn->connect_error) {
die ("Connection Failed: " .$conn->connect_error);
}

echo "Connected Successfully";

?>

┌──(witty㉿kali)-[~/Downloads]
└─$ rpcclient -U "" 10.10.175.192
Password for [WORKGROUP\]:
Cannot connect to server.  Error was NT_STATUS_LOGON_FAILURE
┌──(witty㉿kali)-[~/Downloads]
└─$ rpcclient -U% 10.10.175.192
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
└─$ rdesktop -f -u "" 10.10.175.192
Autoselecting keyboard map 'en-us' from locale

ATTENTION! The server uses and invalid security certificate which can not be trusted for
the following identified reasons(s);

 1. Certificate issuer is not trusted by this system.

     Issuer: CN=DC.COOCTUS.CORP

Review the following certificate info before you trust it to be added as an exception.
If you do not trust the certificate the connection atempt will be aborted:

    Subject: CN=DC.COOCTUS.CORP
     Issuer: CN=DC.COOCTUS.CORP
 Valid From: Wed Jun 28 22:38:17 2023
         To: Thu Dec 28 21:38:17 2023

  Certificate fingerprints:

       sha1: 62765024f4d1b03511a8cf97e7012e50b85e2ff2
     sha256: 8e647bd4f67a2e100231111462848115a32758694a82d7761db3ac1240ca4b36

Do you trust this certificate (yes/no)? yes
Failed to initialize NLA, do you have correct Kerberos TGT initialized ?
Core(warning): Certificate received from server is NOT trusted by this system, an exception has been added by the user to trust this specific certificate.
Connection established using SSL.
disconnect: Disconnect initiated by user.

┌──(witty㉿kali)-[~/Downloads]
└─$ crackmapexec smb 10.10.175.192 -u Visitor -p GuestLogin!
SMB         10.10.175.192   445    DC               [*] Windows 10.0 Build 17763 x64 (name:DC) (domain:COOCTUS.CORP) (signing:True) (SMBv1:False)
SMB         10.10.175.192   445    DC               [+] COOCTUS.CORP\Visitor:GuestLogin!

┌──(witty㉿kali)-[~/Downloads]
└─$ smbclient -L //10.10.175.192 -U "Visitor"           
Password for [WORKGROUP\Visitor]:

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	Home            Disk      
	IPC$            IPC       Remote IPC
	NETLOGON        Disk      Logon server share 
	SYSVOL          Disk      Logon server share 
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.175.192 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available

┌──(witty㉿kali)-[~/Downloads]
└─$ smbclient //10.10.175.192/Home -U "Visitor"          
Password for [WORKGROUP\Visitor]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Jun  8 15:42:53 2021
  ..                                  D        0  Tue Jun  8 15:42:53 2021
  user.txt                            A       17  Mon Jun  7 23:14:25 2021

		15587583 blocks of size 4096. 11430746 blocks available
smb: \> more user.txt 
getting file \user.txt of size 17 as /tmp/smbmore.zPNYd5 (0.0 KiloBytes/sec) (average 0.0 KiloBytes/sec)

THM{Gu3st_Pl3as3}

┌──(witty㉿kali)-[~/Downloads]
└─$ smbclient //10.10.175.192/SYSVOL -U "Visitor"
Password for [WORKGROUP\Visitor]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Mon Jun  7 20:34:33 2021
  ..                                  D        0  Mon Jun  7 20:34:33 2021
  COOCTUS.CORP                       Dr        0  Mon Jun  7 20:34:33 2021

		15587583 blocks of size 4096. 11430697 blocks available
smb: \> cd COOCTUS.CORP\
smb: \COOCTUS.CORP\> ls
  .                                   D        0  Mon Jun  7 20:40:32 2021
  ..                                  D        0  Mon Jun  7 20:40:32 2021
  DfsrPrivate                      DHSr        0  Mon Jun  7 20:40:32 2021
  Policies                            D        0  Mon Jun  7 20:34:38 2021
  scripts                             D        0  Mon Jun  7 20:34:33 2021

		15587583 blocks of size 4096. 11430440 blocks available
smb: \COOCTUS.CORP\> cd DfsrPrivate\
cd \COOCTUS.CORP\DfsrPrivate\: NT_STATUS_ACCESS_DENIED
smb: \COOCTUS.CORP\> ls
  .                                   D        0  Mon Jun  7 20:40:32 2021
  ..                                  D        0  Mon Jun  7 20:40:32 2021
  DfsrPrivate                      DHSr        0  Mon Jun  7 20:40:32 2021
  Policies                            D        0  Mon Jun  7 20:34:38 2021
  scripts                             D        0  Mon Jun  7 20:34:33 2021

		15587583 blocks of size 4096. 11430440 blocks available
smb: \COOCTUS.CORP\> cd Policies\
smb: \COOCTUS.CORP\Policies\> l
  .                                   D        0  Mon Jun  7 20:34:38 2021
  ..                                  D        0  Mon Jun  7 20:34:38 2021
  {31B2F340-016D-11D2-945F-00C04FB984F9}      D        0  Mon Jun  7 20:34:38 2021
  {6AC1786C-016F-11D2-945F-00C04fB984F9}      D        0  Mon Jun  7 20:34:38 2021

		15587583 blocks of size 4096. 11430440 blocks available
smb: \COOCTUS.CORP\Policies\> cd ..\scripts\
smb: \COOCTUS.CORP\scripts\> ls
  .                                   D        0  Mon Jun  7 20:34:33 2021
  ..                                  D        0  Mon Jun  7 20:34:33 2021

		15587583 blocks of size 4096. 11430440 blocks available

**A suffix (also known as a naming context) is a DN that identifies the top entry in a locally held directory hierarchy**.

┌──(witty㉿kali)-[~/Downloads]
└─$ ldapsearch -h
ldapsearch: option requires an argument -- 'h'
ldapsearch: unrecognized option -h
usage: ldapsearch [options] [filter [attributes...]]
where:
  filter	RFC 4515 compliant LDAP search filter
  attributes	whitespace-separated list of attribute descriptions
    which may include:
      1.1   no attributes
      *     all user attributes
      +     all operational attributes
Search options:
  -a deref   one of never (default), always, search, or find
  -A         retrieve attribute names only (no values)
  -b basedn  base dn for search
  -c         continuous operation mode (do not stop on errors)
  -E [!]<ext>[=<extparam>] search extensions (! indicates criticality)
             [!]accountUsability         (NetScape Account usability)
             [!]domainScope              (domain scope)
             !dontUseCopy                (Don't Use Copy)
             [!]mv=<filter>              (RFC 3876 matched values filter)
             [!]pr=<size>[/prompt|noprompt] (RFC 2696 paged results/prompt)
             [!]ps=<changetypes>/<changesonly>/<echg> (draft persistent search)
             [!]sss=[-]<attr[:OID]>[/[-]<attr[:OID]>...]
                                         (RFC 2891 server side sorting)
             [!]subentries[=true|false]  (RFC 3672 subentries)
             [!]sync=ro[/<cookie>]       (RFC 4533 LDAP Sync refreshOnly)
                     rp[/<cookie>][/<slimit>] (refreshAndPersist)
             [!]vlv=<before>/<after>(/<offset>/<count>|:<value>)
                                         (ldapv3-vlv-09 virtual list views)
             [!]deref=derefAttr:attr[,...][;derefAttr:attr[,...][;...]]
             !dirSync=<flags>/<maxAttrCount>[/<cookie>]
                                         (MS AD DirSync)
             [!]extendedDn=<flag>        (MS AD Extended DN
             [!]showDeleted              (MS AD Show Deleted)
             [!]serverNotif              (MS AD Server Notification)
             [!]<oid>[=:<value>|::<b64value>] (generic control; no response handling)
  -f file    read operations from `file'
  -F prefix  URL prefix for files (default: file:///tmp/)
  -l limit   time limit (in seconds, or "none" or "max") for search
  -L         print responses in LDIFv1 format
  -LL        print responses in LDIF format without comments
  -LLL       print responses in LDIF format without comments
