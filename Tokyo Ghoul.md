---
Help kaneki escape jason room
---

# Tokyo Ghoul — Writeup

## Overview
### Tokyo Ghoul — Writeup
### Tokyo Ghoul — Writeup
![](https://i.pinimg.com/originals/fd/65/ff/fd65ffab480607b6ec1eb33239e690f9.png)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/796659bf2a5ae9a15bb6c948291fef4a.jpeg)
### About the room
Start Machine
![](https://i.imgur.com/tuzTqo4.gif)
This room took a lot of inspiration from [psychobreak](https://tryhackme.com/room/psychobreak) , and it is based on Tokyo Ghoul anime.
Alert: This room can contain some spoilers 'only s1 and s2 ' so if you are interested to watch the anime, wait till you finish the anime and come back to do the room
The machine will take some time, just go grab some water or make a coffee.
**This room contains some non-pg13 elements in the form of narrative descriptions. Please proceed only at your own comfort level.**
Answer the questions below
_Read the above_
Completed
Deploy the machine
Completed
### Where am i ?
![](https://thumbs.gfycat.com/DecisiveLeadingDuck-small.gif)
Let's do some scanning .
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads/Rooms/gau]
└─$ rustscan -a 10.10.136.184 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.136.184:21
Open 10.10.136.184:22
Open 10.10.136.184:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-23 12:43 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:43
Completed NSE at 12:43, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:43
Completed NSE at 12:43, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:43
Completed NSE at 12:43, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 12:43
Completed Parallel DNS resolution of 1 host. at 12:43, 13.01s elapsed
DNS resolution of 1 IPs took 13.02s. Mode: Async [#: 1, OK: 0, NX: 0, DR: 1, SF: 0, TR: 3, CN: 0]
Initiating Connect Scan at 12:43
Scanning 10.10.136.184 [3 ports]
Discovered open port 80/tcp on 10.10.136.184
Discovered open port 22/tcp on 10.10.136.184
Discovered open port 21/tcp on 10.10.136.184
Completed Connect Scan at 12:43, 0.20s elapsed (3 total ports)
Initiating Service scan at 12:43
Scanning 3 services on 10.10.136.184
Completed Service scan at 12:43, 11.61s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.136.184.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:43
NSE: [ftp-bounce 10.10.136.184:21] PORT response: 500 Illegal PORT command.
NSE Timing: About 99.05% done; ETC: 12:44 (0:00:00 remaining)
Completed NSE at 12:44, 55.31s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:44
Completed NSE at 12:44, 7.93s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:44
Completed NSE at 12:44, 0.00s elapsed
Nmap scan report for 10.10.136.184
Host is up, received user-set (0.19s latency).
Scanned at 2023-02-23 12:43:33 EST for 76s

PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    3 ftp      ftp          4096 Jan 23  2021 need_Help?
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
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 fa9e38d395df55ea14c949d80a61db5e (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCeIXT46ZiVmp8Es0cKk8YkMs3kwCdmC2Ve/0A0F7aKUIOlbyLc9FkbTEGSrE69obV3u6VywjxZX6VWQoJRHLooPmZCHkYGjW+y5kfEoyeu7pqZr7oA8xgSRf+gsEETWqPnSwjTznFaZ0T1X0KfIgCidrr9pWC0c2AxC1zxNPz9p13NJH5n4RUSYCMOm2xSIwUr6ySL3v/jijwEKIMnwJHbEOmxhGrzaAXgAJeGkXUA0fU1mTVLlSwOClKOBTTo+FGcJdrFf65XenUVLaqaQGytKxR2qiCkr7bbTaWV0F8jPtVD4zOXLy2rGoozMU7jAukQu6uaDxpE7BiybhV3Ac1x
|   256 adb7a75e36cb32a090908e0b98308a97 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBC5o77nOh7/3HUQAxhtNqHX7LGDtYoVZ0au6UJzFVsAEJ644PyU2/pALbapZwFEQI3AUZ5JxjylwKzf1m+G5OJM=
|   256 a2a2c81496c5206885e541d0aa538bbd (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOJwYjN/qiwrS4es9m/LgWitFMA0f6AJMTi8aHkYj7vE
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:44
Completed NSE at 12:44, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:44
Completed NSE at 12:44, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:44
Completed NSE at 12:44, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 90.30 seconds

┌──(witty㉿kali)-[~/Downloads/wappylyzer]
└─$ ftp 10.10.136.184
Connected to 10.10.136.184.
220 (vsFTPd 3.0.3)
Name (10.10.136.184:witty): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||41898|)
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Jan 23  2021 need_Help?
226 Directory send OK.
ftp> ls -la
229 Entering Extended Passive Mode (|||40583|)
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Jan 23  2021 .
drwxr-xr-x    3 ftp      ftp          4096 Jan 23  2021 ..
drwxr-xr-x    3 ftp      ftp          4096 Jan 23  2021 need_Help?
226 Directory send OK.
ftp> more need_Help?
Failed to open file.
ftp> cd need_Help?
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||45568|)
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Jan 23  2021 .
drwxr-xr-x    3 ftp      ftp          4096 Jan 23  2021 ..
-rw-r--r--    1 ftp      ftp           480 Jan 23  2021 Aogiri_tree.txt
drwxr-xr-x    2 ftp      ftp          4096 Jan 23  2021 Talk_with_me
226 Directory send OK.
ftp> more Aogiri_tree.txtt
Why are you so late?? i've been waiting for too long .
So i heard you need help to defeat Jason , so i'll help you to do it and i know 
you are wondering how i will. 
I knew Rize San more than anyone and she is a part of you, right?
That mean you got her kagune , so you should activate her Kagune and to do that 
you should get all control to your body , i'll help you to know Rise san more an
d get her kagune , and don't forget you are now a part of the Aogiri tree .
Bye Kaneki.

ftp> mget *
mget need_to_talk [anpqy?]? 
229 Entering Extended Passive Mode (|||41588|)
150 Opening BINARY mode data connection for need_to_talk (17488 bytes).
  0% |                                   |     0        0.00 KiB/s    --:-- ETA

uhmm
```
Use nmap to scan all ports
Completed
How many ports are open ?
*3*
What is the OS used ?
*Ubuntu*
### Planning to escape
![](https://pm1.narvii.com/5731/bc5df8c79950e46f820fad03bcb98e056b03adc8_hq.jpg)
Try to look around any thing would be useful .
Answer the questions below
```text
view-source:http://10.10.136.184/jasonroom.html

<!-- look don't tell jason but we will help you escape we will give you the key to open those chains and here is some clothes to look like us and a mask to look anonymous and go to the ftp room right there -->

I see the problem I was using Cloudflare Warp 🤣

ftp> mget *
mget need_to_talk [anpqy?]? y
229 Entering Extended Passive Mode (|||45528|)
150 Opening BINARY mode data connection for need_to_talk (17488 bytes).
100% |***********************************| 17488       89.67 KiB/s    00:00 ETA
226 Transfer complete.
17488 bytes received in 00:00 (45.22 KiB/s)
mget rize_and_kaneki.jpg [anpqy?]? y
229 Entering Extended Passive Mode (|||46330|)
150 Opening BINARY mode data connection for rize_and_kaneki.jpg (46674 bytes).
100% |***********************************| 46674      120.55 KiB/s    00:00 ETA
226 Transfer complete.
46674 bytes received in 00:00 (79.52 KiB/s)

┌──(witty㉿kali)-[~/Downloads/wappylyzer]
└─$ file need_to_talk    
need_to_talk: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=adba55165982c79dd348a1b03c32d55e15e95cf6, for GNU/Linux 3.2.0, not stripped
                                                                                
┌──(witty㉿kali)-[~/Downloads/wappylyzer]
└─$ chmod +x need_to_talk 
                                                                                
┌──(witty㉿kali)-[~/Downloads/wappylyzer]
└─$ ./need_to_talk 
Hey Kaneki finnaly you want to talk 
Unfortunately before I can give you the kagune you need to give me the paraphrase
Do you have what I'm looking for?

┌──(witty㉿kali)-[~/Downloads/wappylyzer]
└─$ file rize_and_kaneki.jpg 
rize_and_kaneki.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 1024x576, components 3

┌──(witty㉿kali)-[~/Downloads/wappylyzer]
└─$ steghide extract -sf rize_and_kaneki.jpg                                  
Enter passphrase: 
steghide: could not extract any data with that passphrase!

┌──(witty㉿kali)-[~/Downloads/wappylyzer]
└─$ strings need_to_talk                    
/lib64/ld-linux-x86-64.so.2
mgUa
puts
putchar
stdin
printf
fgets
strlen
stdout
malloc
usleep
__cxa_finalize
setbuf
strcmp
__libc_start_main
free
libc.so.6
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u/UH
You_founH
d_1t
[]A\A]A^A_
kamishiro
Hey Kaneki finnaly you want to talk 
Unfortunately before I can give you the kagune you need to give me the paraphrase
Do you have what I'm looking for?
Good job. I believe this is what you came for:
Hmm. I don't think this is what I was looking for.
Take a look inside of me. rabin2 -z
;*3$"
GCC: (Debian 9.3.0-15) 9.3.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.7452
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
need_to_talk.c
__FRAME_END__
__init_array_end
_DYNAMIC
__init_array_start
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
free@@GLIBC_2.2.5
putchar@@GLIBC_2.2.5
print_intro
_ITM_deregisterTMCloneTable
stdout@@GLIBC_2.2.5
sleep_delay
puts@@GLIBC_2.2.5
stdin@@GLIBC_2.2.5
_edata
strlen@@GLIBC_2.2.5
setbuf@@GLIBC_2.2.5
printf@@GLIBC_2.2.5
slow_type
__libc_start_main@@GLIBC_2.2.5
fgets@@GLIBC_2.2.5
__data_start
strcmp@@GLIBC_2.2.5
__gmon_start__
__dso_handle
_IO_stdin_used
__libc_csu_init
malloc@@GLIBC_2.2.5
__bss_start
main
dialogs
check_password
