# Hamlet — Writeup

## Overview
### Hamlet — Writeup
### Hamlet — Writeup
----
A Shakespeare/Hamlet-inspired room in which you will explore an uncommon web application used in linguistic/NLP research.
----
![](https://i.imgur.com/aoogIkf.jpeg)
![](https://tryhackme-images.s3.amazonaws.com/room-icons/7c3ed8c81855bd05c6e7c8815ac26f37.png)
Start Machine
Welcome to **Hamlet**!
This is a fairly straightforward CTF-like room in which you will play with an uncommon web application used in linguistic research. You will also learn a little bit about Docker. While there are CTF elements, there are quite a few "real" problems in here. Feel free to explore!
In the [associated GitHub repository](https://github.com/IngoKl/THM-Hamlet), you will find detailed information about this room as well as the learning objectives. That said, I would recommend trying this room as a challenge first.
Please note that the machine **takes a while to boot fully**, and some services will only become available after a few minutes.
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.44.208 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.44.208:21
Open 10.10.44.208:22
Open 10.10.44.208:80
Open 10.10.44.208:501
Open 10.10.44.208:8000
Open 10.10.44.208:8080
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
Scanning 10.10.44.208 [6 ports]
Discovered open port 80/tcp on 10.10.44.208
Discovered open port 8080/tcp on 10.10.44.208
Discovered open port 22/tcp on 10.10.44.208
Discovered open port 21/tcp on 10.10.44.208
Discovered open port 8000/tcp on 10.10.44.208
Discovered open port 501/tcp on 10.10.44.208
Completed Connect Scan (6 total ports)
Initiating Service scan
Scanning 6 services on 10.10.44.208
Completed Service scan (6 services on 1 host)
NSE: Script scanning 10.10.44.208.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
NSE: [ftp-bounce 10.10.44.208:21] PORT response: 500 Illegal PORT command.
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.44.208
Host is up, received user-set (0.17s latency).

PORT     STATE SERVICE    REASON  VERSION
21/tcp   open  ftp        syn-ack vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.8.19.103
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rwxr-xr-x    1 0        0             113 Sep 15  2021 password-policy.md
|_-rw-r--r--    1 0        0            1425 Sep 15  2021 ufw.status
22/tcp   open  ssh        syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 a0ef4c3228a64c7f60d6a66332acab27 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC5/i3O28uWolhittypXr6mAEk+XOV998o/e/3wIWpGq9J1GhtGc3J4uwYpBt7SiS3mZivq9D5jgFhqhHb6zlBsQmGUnXUnQNYyqrBmGnyl4urp5IuV1sRCdNXQdt/lf6Z9A807OPuCkzkAexFUV28eXqdXpRsXXkqgkl5DCm2WEtV7yxPIbGlcmX+arDT9A5kGTZe9rNDdqzSafz0aVKRWoTHGHuqVmq0oPD3Cc3oYfoLu7GTJV+Cy6Hxs3s6oUVcruoi1JYvbxC9whexOr+NSZT9mGxDSDLS6jEMim2DQ+hNhiT49JXcMXhQ2nOYqBXLZF0OYyNKaGdgG35CIT40z
|   256 5a6d1a399700bec7106e365c7fcadcb2 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHtt/3Q8agNKO48Zw3srosCs+bfCx47O+i4tBUX7VGMSpzTJQS3s4DBhGvrvO+d/u9B4e9ZBgWSqo+aDqGsTZxQ=
|   256 0b7740b2cc308d8e4551fa127ce295c7 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIN4jv01JeDGsDfhWIJMF8HBv26FI18VLpBeNoiSGbKVp
80/tcp   open  http       syn-ack lighttpd 1.4.45
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-title: Hamlet Annotation Project
|_http-server-header: lighttpd/1.4.45
501/tcp  open  tcpwrapped syn-ack
8000/tcp open  http       syn-ack Apache httpd 2.4.48 ((Debian))
|_http-server-header: Apache/2.4.48 (Debian)
|_http-title: Site doesn't have a title (text/html).
| http-methods: 
|_  Supported Methods: POST OPTIONS HEAD GET
|_http-open-proxy: Proxy might be redirecting requests
8080/tcp open  http-proxy syn-ack
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 500 
|     Content-Type: application/json;charset=UTF-8
|     Date: Sat, 05 Aug 2023 00:33:37 GMT
|     Connection: close
|     {"timestamp":1691195617688,"status":500,"error":"Internal Server Error","exception":"org.springframework.security.web.firewall.RequestRejectedException","message":"The request was rejected because the URL contained a potentially malicious String "%2e"","path":"/nice%20ports%2C/Tri%6Eity.txt%2ebak"}
|   GetRequest: 
|     HTTP/1.1 302 
|     Set-Cookie: JSESSIONID=4BD4816EA50C9F4C33DD67D9949B1FD8; Path=/; HttpOnly
|     X-Content-Type-Options: nosniff
|     X-XSS-Protection: 1; mode=block
|     Cache-Control: no-cache, no-store, max-age=0, must-revalidate
|     Pragma: no-cache
|     Expires: 0
|     X-Frame-Options: SAMEORIGIN
|     Location: http://localhost:8080/login.html
|     Content-Length: 0
|     Date: Sat, 05 Aug 2023 00:33:36 GMT
|     Connection: close
|   HTTPOptions: 
|     HTTP/1.1 302 
|     Set-Cookie: JSESSIONID=F7C29486E8AF3C986D9C9F9F6B34288A; Path=/; HttpOnly
|     X-Content-Type-Options: nosniff
|     X-XSS-Protection: 1; mode=block
|     Cache-Control: no-cache, no-store, max-age=0, must-revalidate
|     Pragma: no-cache
|     Expires: 0
|     X-Frame-Options: SAMEORIGIN
|     Location: http://localhost:8080/login.html
|     Content-Length: 0
|     Date: Sat, 05 Aug 2023 00:33:36 GMT
|     Connection: close
|   RTSPRequest: 
|     HTTP/1.1 400 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 435
|     Date: Sat, 05 Aug 2023 00:33:37 GMT
|     Connection: close
|     <!doctype html><html lang="en"><head><title>HTTP Status 400 
|     Request</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 400 
|_    Request</h1></body></html>
|_http-favicon: Spring Java Framework
|_http-trane-info: Problem with XML parsing of /evox/about
|_http-open-proxy: Proxy might be redirecting requests
| http-title: WebAnno - Log in 
|_Requested resource was http://10.10.44.208:8080/login.html
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8080-TCP:V=7.93%I=7%D=8/4%Time=64CD98DF%P=x86_64-pc-linux-gnu%r(Get
SF:Request,18F,"HTTP/1\.1\x20302\x20\r\nSet-Cookie:\x20JSESSIONID=4BD4816E
SF:A50C9F4C33DD67D9949B1FD8;\x20Path=/;\x20HttpOnly\r\nX-Content-Type-Opti
SF:ons:\x20nosniff\r\nX-XSS-Protection:\x201;\x20mode=block\r\nCache-Contr
SF:ol:\x20no-cache,\x20no-store,\x20max-age=0,\x20must-revalidate\r\nPragm
SF:a:\x20no-cache\r\nExpires:\x200\r\nX-Frame-Options:\x20SAMEORIGIN\r\nLo
SF:cation:\x20http://localhost:8080/login\.html\r\nContent-Length:\x200\r\
SF:nDate:\x20Sat,\x2005\x20Aug\x202023\x2000:33:36\x20GMT\r\nConnection:\x
SF:20close\r\n\r\n")%r(HTTPOptions,18F,"HTTP/1\.1\x20302\x20\r\nSet-Cookie
SF::\x20JSESSIONID=F7C29486E8AF3C986D9C9F9F6B34288A;\x20Path=/;\x20HttpOnl
SF:y\r\nX-Content-Type-Options:\x20nosniff\r\nX-XSS-Protection:\x201;\x20m
SF:ode=block\r\nCache-Control:\x20no-cache,\x20no-store,\x20max-age=0,\x20
SF:must-revalidate\r\nPragma:\x20no-cache\r\nExpires:\x200\r\nX-Frame-Opti
SF:ons:\x20SAMEORIGIN\r\nLocation:\x20http://localhost:8080/login\.html\r\
SF:nContent-Length:\x200\r\nDate:\x20Sat,\x2005\x20Aug\x202023\x2000:33:36
SF:\x20GMT\r\nConnection:\x20close\r\n\r\n")%r(RTSPRequest,24E,"HTTP/1\.1\
SF:x20400\x20\r\nContent-Type:\x20text/html;charset=utf-8\r\nContent-Langu
SF:age:\x20en\r\nContent-Length:\x20435\r\nDate:\x20Sat,\x2005\x20Aug\x202
SF:023\x2000:33:37\x20GMT\r\nConnection:\x20close\r\n\r\n<!doctype\x20html
SF:><html\x20lang=\"en\"><head><title>HTTP\x20Status\x20400\x20\xe2\x80\x9
SF:3\x20Bad\x20Request</title><style\x20type=\"text/css\">body\x20{font-fa
SF:mily:Tahoma,Arial,sans-serif;}\x20h1,\x20h2,\x20h3,\x20b\x20{color:whit
SF:e;background-color:#525D76;}\x20h1\x20{font-size:22px;}\x20h2\x20{font-
SF:size:16px;}\x20h3\x20{font-size:14px;}\x20p\x20{font-size:12px;}\x20a\x
SF:20{color:black;}\x20\.line\x20{height:1px;background-color:#525D76;bord
SF:er:none;}</style></head><body><h1>HTTP\x20Status\x20400\x20\xe2\x80\x93
SF:\x20Bad\x20Request</h1></body></html>")%r(FourOhFourRequest,1A4,"HTTP/1
SF:\.1\x20500\x20\r\nContent-Type:\x20application/json;charset=UTF-8\r\nDa
SF:te:\x20Sat,\x2005\x20Aug\x202023\x2000:33:37\x20GMT\r\nConnection:\x20c
SF:lose\r\n\r\n{\"timestamp\":1691195617688,\"status\":500,\"error\":\"Int
SF:ernal\x20Server\x20Error\",\"exception\":\"org\.springframework\.securi
SF:ty\.web\.firewall\.RequestRejectedException\",\"message\":\"The\x20requ
SF:est\x20was\x20rejected\x20because\x20the\x20URL\x20contained\x20a\x20po
SF:tentially\x20malicious\x20String\x20\\\"%2e\\\"\",\"path\":\"/nice%20po
SF:rts%2C/Tri%6Eity\.txt%2ebak\"}");
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

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
Nmap done: 1 IP address (1 host up) scanned in 43.16 seconds

┌──(witty㉿kali)-[~]
└─$ ftp 10.10.44.208
Connected to 10.10.44.208.
220 (vsFTPd 3.0.3)
Name (10.10.44.208:witty): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -la
229 Entering Extended Passive Mode (|||50574|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        114          4096 Sep 15  2021 .
drwxr-xr-x    2 0        114          4096 Sep 15  2021 ..
-rwxr-xr-x    1 0        0             113 Sep 15  2021 password-policy.md
-rw-r--r--    1 0        0            1425 Sep 15  2021 ufw.status
226 Directory send OK.
ftp> more password-policy.md
```
```text
# Password Policy

## WebAnno

New passwords should be:

- lowercase
- between 12 and 14 characters long

ftp> more ufw.status
Status: active

To                         Action      From
--                         ------      ----
20/tcp                     ALLOW       Anywhere                  
21/tcp                     ALLOW       Anywhere                  
22/tcp                     ALLOW       Anywhere                  
80/tcp                     ALLOW       Anywhere                  
501/tcp                    ALLOW       Anywhere                  
8080/tcp                   ALLOW       Anywhere                  
8000/tcp                   ALLOW       Anywhere                  
1603/tcp                   ALLOW       Anywhere                  
1564/tcp                   ALLOW       Anywhere                  
50000:50999/tcp            ALLOW       Anywhere                  
20/tcp (v6)                ALLOW       Anywhere (v6)             
21/tcp (v6)                ALLOW       Anywhere (v6)             
22/tcp (v6)                ALLOW       Anywhere (v6)             
80/tcp (v6)                ALLOW       Anywhere (v6)             
501/tcp (v6)               ALLOW       Anywhere (v6)             
8080/tcp (v6)              ALLOW       Anywhere (v6)             
8000/tcp (v6)              ALLOW       Anywhere (v6)             
1603/tcp (v6)              ALLOW       Anywhere (v6)             
1564/tcp (v6)              ALLOW       Anywhere (v6)             
50000:50999/tcp (v6)       ALLOW       Anywhere (v6)  

Using active mode, at least using the standard FTP client, won't work very well.

┌──(witty㉿kali)-[~]
└─$ ftp 10.10.44.208
Connected to 10.10.44.208.
220 (vsFTPd 3.0.3)
Name (10.10.44.208:witty): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> passive
Passive mode: off; fallback to active mode: off.
ftp> passive
Passive mode: on; fallback to active mode: on.
ftp> dir
229 Entering Extended Passive Mode (|||50688|)
150 Here comes the directory listing.
-rwxr-xr-x    1 0        0             113 Sep 15  2021 password-policy.md
-rw-r--r--    1 0        0            1425 Sep 15  2021 ufw.status
226 Directory send OK.

Welcome to the Hamlet Annotation Project

We are a small group of researchers annotating Shakespeare's Hamlet using WebAnno. This is the version of the play we are currently using.

If you want to help out, send an email to Michael 'ghost' Canterbury (ghost@webanno.hamlet.thm). He's obsessed with Hamlet and the vocabulary used by Shakespeare.

http://10.10.44.208/hamlet.txt

http://10.10.44.208:8000/

http://10.10.44.208:8080/login.html 

https://webanno.github.io/webanno/
https://github.com/webanno/webanno

http://10.10.44.208:501/

GRAVEDIGGER
What do you call a person who builds stronger things than a stonemason, a shipbuilder, or a carpenter does?
PENTESTER
ou com'st
PENTESTER

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://10.10.44.208 -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.44.208
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://10.10.44.208/index.html           (Status: 200) [Size: 1011]
http://10.10.44.208/robots.txt           (Status: 200) [Size: 64]
Progress: 4611 / 4615 (99.91%)
===============================================================
 Finished
===============================================================

User-agent: *
Allow: /

THM{1_most_mechanical_and_dirty_hand}

Clo. What is he that builds stronger then either the
Mason, the Shipwright, or the Carpenter?
  Other. The Gallowes maker; for that Frame outliues a
thousand Tenants

┌──(witty㉿kali)-[~]
└─$ nc 10.10.44.208 501 -nv
(UNKNOWN) [10.10.44.208] 501 (?) open
GRAVEDIGGER
What do you call a person who builds stronger things than a stonemason, a shipbuilder, or a carpenter does?
PENTESTER
?
ne: Thy Mothers poyson'd:
I can
PENTESTER
Gallowes
signing his name with several different spel
PENTESTER
Gallows
Bugges and Go
PENTESTER
gallows
