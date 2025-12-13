# Year of the Pig — Writeup

## Overview
### Year of the Pig — Writeup
### Year of the Pig — Writeup
----
Some pigs do fly...
----
![](https://i.imgur.com/JiwG6Si.png)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/dda3408fbc3312849968eadbfe72df74.jpeg)
Start Machine
Some pigs fly, and some have stories to tell. Get going!
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.168.36 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.168.36:22
Open 10.10.168.36:80
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
DNS resolution of 1 IPs took 0.15s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.168.36 [2 ports]
Discovered open port 80/tcp on 10.10.168.36
Discovered open port 22/tcp on 10.10.168.36
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.168.36
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.168.36.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.168.36
Host is up, received user-set (0.19s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Marco's Blog
|_http-favicon: Unknown favicon MD5: 9899F13BCC614EE8275B88FFDC0D04DB
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET POST
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

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
Nmap done: 1 IP address (1 host up) scanned in 16.51 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://10.10.168.36/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x txt,php 
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.168.36/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              txt,php
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://10.10.168.36/login.php            (Status: 200) [Size: 2790]
http://10.10.168.36/.php                 (Status: 403) [Size: 277]
http://10.10.168.36/admin                (Status: 301) [Size: 312] [--> http://10.10.168.36/admin/]
http://10.10.168.36/assets               (Status: 301) [Size: 313] [--> http://10.10.168.36/assets/]
http://10.10.168.36/css                  (Status: 301) [Size: 310] [--> http://10.10.168.36/css/]
http://10.10.168.36/js                   (Status: 301) [Size: 309] [--> http://10.10.168.36/js/]
http://10.10.168.36/api                  (Status: 301) [Size: 310] [--> http://10.10.168.36/api/]

marco:marco

http://10.10.168.36/login.php

Remember that passwords should be a memorable word, followed by two numbers and a special character

┌──(witty㉿kali)-[~/Downloads]
└─$ cat generateList.py 
memorableWords = ['Italy', 'italy', 'Milan', 'milan', 'Savoia', 'savoia',
                  'Curtiss', 'curtiss', 'Curtis', 'curtis', 'planes', 'Planes',
                  'Plane', 'plane']
specialChars = ['!','@','#','$']
count = 0

for word in memorableWords:
    for specialChar in specialChars:
        while (count <= 99):
            if (count <= 9):
                count = '0' + str(count)
            else:
                count = str(count)
            print(word + count + specialChar)
            count = int(count)
            count += 1
        count = 0

┌──(witty㉿kali)-[~/Downloads]
└─$ python generateList.py > passwords_generated.lst
                                                                                                         
┌──(witty㉿kali)-[~/Downloads]
