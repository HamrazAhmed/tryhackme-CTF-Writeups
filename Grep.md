# Grep — Writeup

## Overview
### Grep — Writeup
### Grep — Writeup
----
A challenge that tests your reconnaissance and OSINT skills.
----
Start Machine
Welcome to the OSINT challenge, part of TryHackMe’s Red Teaming Path. In this task, you will be an ethical hacker aiming to exploit a newly developed web application.
SuperSecure Corp, a fast-paced startup, is currently creating a blogging platform inviting security professionals to assess its security. The challenge involves using OSINT techniques to gather information from publicly accessible sources and exploit potential vulnerabilities in the web application.
Start by deploying the machine; Click on the `Start Machine` button in the upper-right-hand corner of this task to deploy the virtual machine for this room.
Your goal is to identify and exploit vulnerabilities in the application using a combination of recon and OSINT skills. As you progress, you’ll look for weak points in the app, find sensitive data, and attempt to gain unauthorized access. You will leverage the skills and knowledge acquired through the Red Team Pathway to devise and execute your attack strategies.
**Note:** Please allow the machine 3 - 5 minutes to fully boot. Also, no local privilege escalation is necessary to answer the questions.
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.78.9 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.78.9:22
Open 10.10.78.9:80
Open 10.10.78.9:443
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.94 ( https://nmap.org )
NSE: Loaded 156 scripts for scanning.
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
Scanning 10.10.78.9 [3 ports]
Discovered open port 443/tcp on 10.10.78.9
Discovered open port 22/tcp on 10.10.78.9
Discovered open port 80/tcp on 10.10.78.9
Completed Connect Scan (3 total ports)
Initiating Service scan
Scanning 3 services on 10.10.78.9
Completed Service scan (3 services on 1 host)
NSE: Script scanning 10.10.78.9.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.78.9
Host is up, received user-set (0.22s latency).

PORT    STATE SERVICE  REASON  VERSION
22/tcp  open  ssh      syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 7b:7d:b9:79:3a:5a:27:35:a8:8a:96:fe:a6:45:77:de (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCzyp8voMZUJfpIZMKR8fULuwu9/R/krbDTotgQsjVxzsmDX6HVoqUejoCiGDH2QgQqNa9rjEH+z2qnBLZz72KNCvd5O4aNUm/sQgh6HtaAR90iMHP0bm/VydbRqytqSZ9zxj1/Nqqd9GhVKhPM0xT0X3Hyl9/F+JhBHLdH6vahdK1DAnz6gZiyrZo+cxtS7WUyUlIO2yg9kAowYsaT5NPiWeHVY0+oCFAp4U9m78JylgteWAVFxQhBECWdjpJz/mzQmA0LgWMrFNDLDBJj3b+wAD9a0aZNlslZYaXFUi8UnFWcfQ5/RoX8zlmKvK167y5+1pbzNJEpOkepGKdcpTM3wE6bTF5fMETJior9BewEG13ubeuavuessMqW56cT71fTrljDLjaSmc+77CeTdsReNSr45bFDLyGD4LLJyKSOsvTmFApLcEqkVg/ZXZlE0BjxKYuSgcrTJtmNzxDmnokwfkslfXw32rz6Nte9+dJDbTsD1NLZ8zJ4Ow9C3hWTME0=
|   256 ce:e0:22:b2:5e:9e:d9:d6:89:8f:1e:57:05:9c:1e:8a (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDB3efwkSzkUT4rmJbvIRhmgZXfo+aT7s0HQpVqSALyDIOYff1DKbjZe6jTAoYi8AVM1UpCLLXhezGV2MTGbk/0=
|   256 49:ec:11:94:eb:c9:9c:51:08:6c:b1:3f:b3:21:b7:f8 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHFft6V62ZnvwTNCW5o3aVcHvVBbsWY/CM82QMPfHzFt
80/tcp  open  http     syn-ack Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
443/tcp open  ssl/http syn-ack Apache httpd 2.4.41
| tls-alpn: 
|_  http/1.1
|_ssl-date: TLS randomness does not represent time
|_http-server-header: Apache/2.4.41 (Ubuntu)
| ssl-cert: Subject: commonName=grep.thm/organizationName=SearchME/stateOrProvinceName=Some-State/countryName=US
| Issuer: commonName=grep.thm/organizationName=SearchME/stateOrProvinceName=Some-State/countryName=US
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| MD5:   7295:8ef0:7c16:221c:3b0a:40ee:913c:766c
| SHA-1: 38c2:3ba3:34b1:851a:f1d4:ee0a:37bd:701a:830c:7dd8
| -----BEGIN CERTIFICATE-----
| MIIDFzCCAf8CFGTWwbbVKaNSN8fhUdtf0QT84zCSMA0GCSqGSIb3DQEBCwUAMEgx
| CzAJBgNVBAYTAlVTMRMwEQYDVQQIDApTb21lLVN0YXRlMREwDwYDVQQKDAhTZWFy
| Y2hNRTERMA8GA1UEAwwIZ3JlcC50aG0wHhcNMjMwNjE0MTMwMzA5WhcNMjQwNjEz
| MTMwMzA5WjBIMQswCQYDVQQGEwJVUzETMBEGA1UECAwKU29tZS1TdGF0ZTERMA8G
| A1UECgwIU2VhcmNoTUUxETAPBgNVBAMMCGdyZXAudGhtMIIBIjANBgkqhkiG9w0B
| AQEFAAOCAQ8AMIIBCgKCAQEAtiDNwwY9IR2HADMy6CRAwiPH0s8dIOFGPrbYCbLz
| fDKIWURlczzOlmgpscN/YHHpt6P5ywUPLGnMK3ukYag7xTUYl+vmledTnD9oebnJ
| 6qDweFFwdZ8hysITyvCyGgqcY52JE2nBtVNj6/L16iZ60KKko8opNsTE5IYj/sUt
| PsOxeNiV3oqpOUeKtZJbn7Kssd4KBwnRqTSUlXlPXzeRipAiW5SZZXo6K4YeLVht
| XlLPtPWsMC0fj16DDDtxLlZmvu3J5o9egp/eRpWmvKWIaKQ57Y0MKB8/gso8FxxX
| NiRY9Nru0C3DCUbc/xXywQ9pIGt/Xir++aXhyxCiIGh22QIDAQABMA0GCSqGSIb3
| DQEBCwUAA4IBAQCzhJu52dIY7V/qQleDMEQ1oBLrQoFhHD6+UbvH0ELMAtL5Dc8A
| LGDdyFkgsx04TaZtJ20dyrjYD+tcAgu9Yb7eEYbfqqD5w4XSzvdEuTW2aVL86aT6
| IBbN8SMkX2zfILjHTOR1F7WAoHaIssH0yZltg+lQEEnAeb+XoIZm9cIW2bTNKoO2
| MeHgvSKkQkjROO29XQQ3mTbxFG86UsTwyGHdddnkfiWilXqgfh+wGxbY/wCdhU0C
| TnuXn4IEVdCBn16rCg51kEZZC1EWPcJpv0/InUNfcgumcVY033EXF/HgW4eNDD6H
| XmLEGKfScUWcO0//STDZGZXwf9gt30DqoMSf
|_-----END CERTIFICATE-----
|_http-title: 403 Forbidden
Service Info: Host: ip-10-10-78-9.eu-west-1.compute.internal; OS: Linux; CPE: cpe:/o:linux:linux_kernel

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
Nmap done: 1 IP address (1 host up) scanned in 27.56 seconds

POST / HTTP/1.1

Host: 10.10.78.9

HTTP/1.1 403 Forbidden

Date: Sun, 20 Aug 2023 17:22:30 GMT

just through port 80

┌──(witty㉿kali)-[~/Downloads]
└─$ dirsearch -u http://10.10.78.9/ -i200,301,302,401 

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 10927

Output File: /home/witty/.dirsearch/reports/10.10.78.9/-_23-08-20_13-24-03.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-08-20_13-24-03.log

Target: http://10.10.78.9/

[13:24:03] Starting: 
[13:25:14] 200 -   11KB - /index.php
[13:25:15] 200 -   11KB - /index.php/login/
[13:25:17] 301 -  313B  - /javascript  ->  http://10.10.78.9/javascript/

Task Completed

maybe we can bypass 403

view certificate

Organization : SearchME
Common Name : grep.thm

┌──(witty㉿kali)-[~/Downloads]
└─$ tac /etc/hosts       
10.10.78.9 grep.thm

oops I forgot the port 51337

┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.78.9 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Nmap? More like slowmap.🐢

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.78.9:22
Open 10.10.78.9:80
Open 10.10.78.9:443
Open 10.10.78.9:51337
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.94 ( https://nmap.org )
NSE: Loaded 156 scripts for scanning.
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
Initiating Connect Scan
Scanning grep.thm (10.10.78.9) [4 ports]
Discovered open port 22/tcp on 10.10.78.9
Discovered open port 51337/tcp on 10.10.78.9
Discovered open port 80/tcp on 10.10.78.9
Discovered open port 443/tcp on 10.10.78.9
Completed Connect Scan (4 total ports)
Initiating Service scan
Scanning 4 services on grep.thm (10.10.78.9)
Completed Service scan (4 services on 1 host)
NSE: Script scanning 10.10.78.9.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for grep.thm (10.10.78.9)
Host is up, received user-set (0.23s latency).

PORT      STATE SERVICE  REASON  VERSION
22/tcp    open  ssh      syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 7b:7d:b9:79:3a:5a:27:35:a8:8a:96:fe:a6:45:77:de (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCzyp8voMZUJfpIZMKR8fULuwu9/R/krbDTotgQsjVxzsmDX6HVoqUejoCiGDH2QgQqNa9rjEH+z2qnBLZz72KNCvd5O4aNUm/sQgh6HtaAR90iMHP0bm/VydbRqytqSZ9zxj1/Nqqd9GhVKhPM0xT0X3Hyl9/F+JhBHLdH6vahdK1DAnz6gZiyrZo+cxtS7WUyUlIO2yg9kAowYsaT5NPiWeHVY0+oCFAp4U9m78JylgteWAVFxQhBECWdjpJz/mzQmA0LgWMrFNDLDBJj3b+wAD9a0aZNlslZYaXFUi8UnFWcfQ5/RoX8zlmKvK167y5+1pbzNJEpOkepGKdcpTM3wE6bTF5fMETJior9BewEG13ubeuavuessMqW56cT71fTrljDLjaSmc+77CeTdsReNSr45bFDLyGD4LLJyKSOsvTmFApLcEqkVg/ZXZlE0BjxKYuSgcrTJtmNzxDmnokwfkslfXw32rz6Nte9+dJDbTsD1NLZ8zJ4Ow9C3hWTME0=
|   256 ce:e0:22:b2:5e:9e:d9:d6:89:8f:1e:57:05:9c:1e:8a (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDB3efwkSzkUT4rmJbvIRhmgZXfo+aT7s0HQpVqSALyDIOYff1DKbjZe6jTAoYi8AVM1UpCLLXhezGV2MTGbk/0=
|   256 49:ec:11:94:eb:c9:9c:51:08:6c:b1:3f:b3:21:b7:f8 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHFft6V62ZnvwTNCW5o3aVcHvVBbsWY/CM82QMPfHzFt
80/tcp    open  http     syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.41 (Ubuntu)
443/tcp   open  ssl/http syn-ack Apache httpd 2.4.41
|_ssl-date: TLS randomness does not represent time
| http-title: Welcome
|_Requested resource was /public/html/
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| tls-alpn: 
|_  http/1.1
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
| ssl-cert: Subject: commonName=grep.thm/organizationName=SearchME/stateOrProvinceName=Some-State/countryName=US
| Issuer: commonName=grep.thm/organizationName=SearchME/stateOrProvinceName=Some-State/countryName=US
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| MD5:   7295:8ef0:7c16:221c:3b0a:40ee:913c:766c
| SHA-1: 38c2:3ba3:34b1:851a:f1d4:ee0a:37bd:701a:830c:7dd8
| -----BEGIN CERTIFICATE-----
| MIIDFzCCAf8CFGTWwbbVKaNSN8fhUdtf0QT84zCSMA0GCSqGSIb3DQEBCwUAMEgx
| CzAJBgNVBAYTAlVTMRMwEQYDVQQIDApTb21lLVN0YXRlMREwDwYDVQQKDAhTZWFy
| Y2hNRTERMA8GA1UEAwwIZ3JlcC50aG0wHhcNMjMwNjE0MTMwMzA5WhcNMjQwNjEz
| MTMwMzA5WjBIMQswCQYDVQQGEwJVUzETMBEGA1UECAwKU29tZS1TdGF0ZTERMA8G
| A1UECgwIU2VhcmNoTUUxETAPBgNVBAMMCGdyZXAudGhtMIIBIjANBgkqhkiG9w0B
| AQEFAAOCAQ8AMIIBCgKCAQEAtiDNwwY9IR2HADMy6CRAwiPH0s8dIOFGPrbYCbLz
| fDKIWURlczzOlmgpscN/YHHpt6P5ywUPLGnMK3ukYag7xTUYl+vmledTnD9oebnJ
| 6qDweFFwdZ8hysITyvCyGgqcY52JE2nBtVNj6/L16iZ60KKko8opNsTE5IYj/sUt
| PsOxeNiV3oqpOUeKtZJbn7Kssd4KBwnRqTSUlXlPXzeRipAiW5SZZXo6K4YeLVht
| XlLPtPWsMC0fj16DDDtxLlZmvu3J5o9egp/eRpWmvKWIaKQ57Y0MKB8/gso8FxxX
| NiRY9Nru0C3DCUbc/xXywQ9pIGt/Xir++aXhyxCiIGh22QIDAQABMA0GCSqGSIb3
| DQEBCwUAA4IBAQCzhJu52dIY7V/qQleDMEQ1oBLrQoFhHD6+UbvH0ELMAtL5Dc8A
| LGDdyFkgsx04TaZtJ20dyrjYD+tcAgu9Yb7eEYbfqqD5w4XSzvdEuTW2aVL86aT6
| IBbN8SMkX2zfILjHTOR1F7WAoHaIssH0yZltg+lQEEnAeb+XoIZm9cIW2bTNKoO2
| MeHgvSKkQkjROO29XQQ3mTbxFG86UsTwyGHdddnkfiWilXqgfh+wGxbY/wCdhU0C
| TnuXn4IEVdCBn16rCg51kEZZC1EWPcJpv0/InUNfcgumcVY033EXF/HgW4eNDD6H
| XmLEGKfScUWcO0//STDZGZXwf9gt30DqoMSf
|_-----END CERTIFICATE-----
51337/tcp open  http     syn-ack Apache httpd 2.4.41
|_http-title: 400 Bad Request
| http-methods: 
|_  Supported Methods: GET HEAD POST
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: Host: ip-10-10-78-9.eu-west-1.compute.internal; OS: Linux; CPE: cpe:/o:linux:linux_kernel

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
Nmap done: 1 IP address (1 host up) scanned in 28.14 seconds

https://10.10.78.9:51337/

Common Name : leakchecker.grep.thm

┌──(witty㉿kali)-[~/Downloads]
└─$ tac /etc/hosts
10.10.78.9 grep.thm leakchecker.grep.thm

https://grep.thm/public/html/

register

Invalid or Expired API key

OSINT

https://github.com/search?q=SearchMEcms&type=code

https://github.com/supersecuredeveloper/searchmecms

register.php

<?php
require_once 'config.php';
header('Content-Type: application/json');

$headers = apache_request_headers();

if (isset($headers['X-THM-API-Key']) && $headers['X-THM-API-Key'] === 'TBA') {
    $input = json_decode(file_get_contents('php://input'), true);

    $stmt = $mysqli->prepare("INSERT INTO users (username, password, email, name) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("ssss", $input['username'], password_hash($input['password'], PASSWORD_DEFAULT), $input['email'], $input['name']);

    if ($stmt->execute()) {
        echo json_encode(['message' => 'Registration successful.']);
