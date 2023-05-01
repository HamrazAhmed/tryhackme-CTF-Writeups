# Cat Pictures 2 — Writeup

## Overview
### Cat Pictures 2 — Writeup
### Cat Pictures 2 — Writeup
----
Now with more Cat Pictures!
----
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/4c424fa649d64938ae8282b14e4299ac.png)

## Flags / Answers
- Give me the flags!
- Answer the questions below
```text
- ┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.183.200 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.183.200:22
Open 10.10.183.200:80
Open 10.10.183.200:3000
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
DNS resolution of 1 IPs took 0.01s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.183.200 [3 ports]
Discovered open port 22/tcp on 10.10.183.200
Discovered open port 80/tcp on 10.10.183.200
Discovered open port 3000/tcp on 10.10.183.200
Completed Connect Scan (3 total ports)
Initiating Service scan
Scanning 3 services on 10.10.183.200
Completed Service scan (3 services on 1 host)
NSE: Script scanning 10.10.183.200.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.183.200
Host is up, received user-set (0.19s latency).

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 33f0033626368c2f88952cacc3bc6465 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDWn7oP+xezi54hhxJR3FAOcCt9gU+ZfOXquxFX/NC6USigzwXcxw2B4P3Yz6Huhaox1WRRgOSAYPJp9uo1gnA+ttkVdRaIqmcizbsznuU6sXntwiunD/QDNegq5UwJI3PjQu05HhnTNwGlBuiv+V/HW2OZGo0LLMY8ixqphCtAbw5uQZsV28rB2Yy1C7FYjkRzfhGePOfyq8Ga4FSpRnWz1vHYyEzFiF9tyLXNcDEdIWalKA6hrr7msEneSITE/RrGt5tynn6Rq5/3Os0mdbV0ztvqavwcWRR6B1UAJ+zPR/GKJ6s4Zr8ImoAXIZc7lFQ7Oh8DVWYp4cearg90RZUx
|   256 4ff3b3f26e0391b27cc053d5d4038846 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBFhoBFkSKYS/dRjYASX26cs3gtgKxnLhhnXBas1fJ5i32J7h9+X8XA3GHT2SzP8/CBbs759W5q68jDA9nsTYnzo=
|   256 137c478b6ff8f46b429af2d53d341352 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMiQc+7IBNNbs8nZJ4L+ntHTLbWn0Xn5b+QnWuboKE6r
80/tcp   open  http    syn-ack nginx 1.4.6 (Ubuntu)
|_http-favicon: Unknown favicon MD5: 60D8216C0FDE4723DCA5FBD03AD44CB7
| http-methods: 
|_  Supported Methods: GET HEAD
|_http-server-header: nginx/1.4.6 (Ubuntu)
| http-git: 
|   10.10.183.200:80/.git/
|     Git repository found!
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|     Remotes:
|       https://github.com/electerious/Lychee.git
|_    Project type: PHP application (guessed from .gitignore)
|_http-title: Lychee
| http-robots.txt: 7 disallowed entries 
|_/data/ /dist/ /docs/ /php/ /plugins/ /src/ /uploads/
3000/tcp open  ppp?    syn-ack
| fingerprint-strings: 
|   GenericLines, Help, RTSPRequest: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Cache-Control: no-store, no-transform
|     Content-Type: text/html; charset=UTF-8
|     Set-Cookie: i_like_gitea=1ff0b17770725638; Path=/; HttpOnly; SameSite=Lax
|     Set-Cookie: _csrf=SPiXj75-c6sXHpC3TK1O-uEF2aQ6MTY4ODQyNjQ3Njk0MTMzNzIxMA; Path=/; Expires=Tue, 04 Jul 2023 23:21:16 GMT; HttpOnly; SameSite=Lax
|     Set-Cookie: macaron_flash=; Path=/; Max-Age=0; HttpOnly; SameSite=Lax
|     X-Frame-Options: SAMEORIGIN
|     Date: Mon, 03 Jul 2023 23:21:16 GMT
|     <!DOCTYPE html>
|     <html lang="en-US" class="theme-">
|     <head>
|     <meta charset="utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1">
|     <title> Gitea: Git with a cup of tea</title>
|     <link rel="manifest" href="data:application/json;base64,eyJuYW1lIjoiR2l0ZWE6IEdpdCB3aXRoIGEgY3VwIG9mIHRlYSIsInNob3J0X25hbWUiOiJHaXRlYTogR2l0IHdpdGggYSBjdXAgb2YgdGVhIiwic3RhcnRfdXJsIjoiaHR0cDovL2xvY2FsaG9zdDozMDAwLyIsImljb25zIjpbeyJzcmMiOiJodHRwOi
|   HTTPOptions: 
|     HTTP/1.0 405 Method Not Allowed
|     Cache-Control: no-store, no-transform
|     Set-Cookie: i_like_gitea=49c924b2fa7c9667; Path=/; HttpOnly; SameSite=Lax
|     Set-Cookie: _csrf=yb5QvFTWvT08fivFTIxqy36Ox6Q6MTY4ODQyNjQ4Mjk4NzY5ODQ3MA; Path=/; Expires=Tue, 04 Jul 2023 23:21:22 GMT; HttpOnly; SameSite=Lax
|     Set-Cookie: macaron_flash=; Path=/; Max-Age=0; HttpOnly; SameSite=Lax
|     X-Frame-Options: SAMEORIGIN
|     Date: Mon, 03 Jul 2023 23:21:22 GMT
|_    Content-Length: 0
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port3000-TCP:V=7.93%I=7%D=7/3%Time=64A357E7%P=x86_64-pc-linux-gnu%r(Gen
SF:ericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20te
SF:xt/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x2
SF:0Request")%r(GetRequest,2DE8,"HTTP/1\.0\x20200\x20OK\r\nCache-Control:\
SF:x20no-store,\x20no-transform\r\nContent-Type:\x20text/html;\x20charset=
SF:UTF-8\r\nSet-Cookie:\x20i_like_gitea=1ff0b17770725638;\x20Path=/;\x20Ht
SF:tpOnly;\x20SameSite=Lax\r\nSet-Cookie:\x20_csrf=SPiXj75-c6sXHpC3TK1O-uE
SF:F2aQ6MTY4ODQyNjQ3Njk0MTMzNzIxMA;\x20Path=/;\x20Expires=Tue,\x2004\x20Ju
SF:l\x202023\x2023:21:16\x20GMT;\x20HttpOnly;\x20SameSite=Lax\r\nSet-Cooki
SF:e:\x20macaron_flash=;\x20Path=/;\x20Max-Age=0;\x20HttpOnly;\x20SameSite
SF:=Lax\r\nX-Frame-Options:\x20SAMEORIGIN\r\nDate:\x20Mon,\x2003\x20Jul\x2
SF:02023\x2023:21:16\x20GMT\r\n\r\n<!DOCTYPE\x20html>\n<html\x20lang=\"en-
SF:US\"\x20class=\"theme-\">\n<head>\n\t<meta\x20charset=\"utf-8\">\n\t<me
SF:ta\x20name=\"viewport\"\x20content=\"width=device-width,\x20initial-sca
SF:le=1\">\n\t<title>\x20Gitea:\x20Git\x20with\x20a\x20cup\x20of\x20tea</t
SF:itle>\n\t<link\x20rel=\"manifest\"\x20href=\"data:application/json;base
SF:64,eyJuYW1lIjoiR2l0ZWE6IEdpdCB3aXRoIGEgY3VwIG9mIHRlYSIsInNob3J0X25hbWUi
SF:OiJHaXRlYTogR2l0IHdpdGggYSBjdXAgb2YgdGVhIiwic3RhcnRfdXJsIjoiaHR0cDovL2x
SF:vY2FsaG9zdDozMDAwLyIsImljb25zIjpbeyJzcmMiOiJodHRwOi")%r(Help,67,"HTTP/1
SF:\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset
SF:=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(HTTPOpt
SF:ions,1C2,"HTTP/1\.0\x20405\x20Method\x20Not\x20Allowed\r\nCache-Control
SF::\x20no-store,\x20no-transform\r\nSet-Cookie:\x20i_like_gitea=49c924b2f
SF:a7c9667;\x20Path=/;\x20HttpOnly;\x20SameSite=Lax\r\nSet-Cookie:\x20_csr
SF:f=yb5QvFTWvT08fivFTIxqy36Ox6Q6MTY4ODQyNjQ4Mjk4NzY5ODQ3MA;\x20Path=/;\x2
SF:0Expires=Tue,\x2004\x20Jul\x202023\x2023:21:22\x20GMT;\x20HttpOnly;\x20
SF:SameSite=Lax\r\nSet-Cookie:\x20macaron_flash=;\x20Path=/;\x20Max-Age=0;
SF:\x20HttpOnly;\x20SameSite=Lax\r\nX-Frame-Options:\x20SAMEORIGIN\r\nDate
SF::\x20Mon,\x2003\x20Jul\x202023\x2023:21:22\x20GMT\r\nContent-Length:\x2
SF:00\r\n\r\n")%r(RTSPRequest,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nCo
SF:ntent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n
SF:\r\n400\x20Bad\x20Request");
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
Nmap done: 1 IP address (1 host up) scanned in 104.90 seconds

http://10.10.183.200/robots.txt

User-agent: *
Disallow: /data/
Disallow: /dist/
Disallow: /docs/
Disallow: /php/
Disallow: /plugins/
Disallow: /src/
Disallow: /uploads/

http://10.10.183.200/#16678460194615/16678466730867

┌──(witty㉿kali)-[~]
└─$ exiftool f5054e97620f168c7b5088c85ab1d6e4.jpg 
ExifTool Version Number         : 12.57
File Name                       : f5054e97620f168c7b5088c85ab1d6e4.jpg
Directory                       : .
File Size                       : 73 kB
File Modification Date/Time     : 2023:07:03 19:26:12-04:00
File Access Date/Time           : 2023:07:03 19:26:12-04:00
File Inode Change Date/Time     : 2023:07:03 19:26:13-04:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Little CMS
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2012:01:25 03:41:57
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : 
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Little CMS
Profile ID                      : 0
Profile Description             : c2
Profile Copyright               : IX
Media White Point               : 0.9642 1 0.82491
Media Black Point               : 0.01205 0.0125 0.01031
