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
