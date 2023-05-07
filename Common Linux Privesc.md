---
A room explaining common Linux privilege escalation
---

# Common Linux Privesc — Writeup

## Enumeration
What is LinEnum?
LinEnum is a simple bash script that performs common commands related to privilege escalation, saving time and allowing more effort to be put toward getting root. It is important to understand what commands LinEnum executes, so that you are able to manually enumerate privesc vulnerabilities in a situation where you're unable to use LinEnum or other like scripts. In this room, we will explain what LinEnum is showing, and what commands can be used to replicate it.
Where to get LinEnum
You can download a local copy of LinEnum from:
https://github.com/rebootuser/LinEnum/blob/master/LinEnum.sh
It's worth keeping this somewhere you'll remember, because LinEnum is an invaluable tool.
How do I get LinEnum on the target machine?
There are two ways to get LinEnum on the target machine. The first way, is to go to the directory that you have your local copy of LinEnum stored in, and start a Python web server using "python3 -m http.server 8000" [1]. Then using "wget" on the target machine, and your local IP, you can grab the file from your local machine [2]. Then make the file executable using the command "chmod +x FILENAME.sh".
![](https://raw.githubusercontent.com/polo-sec/writing/master/Security%20Challenge%20Walkthroughs/Common%20Linux%20Privesc/Resources/1.png)
![](https://raw.githubusercontent.com/polo-sec/writing/master/Security%20Challenge%20Walkthroughs/Common%20Linux%20Privesc/Resources/2.png)
Other Methods
In case you're unable to transport the file, you can also, if you have sufficient permissions, copy the raw LinEnum code from your local machine [1] and paste it into a new file on the target, using Vi or Nano [2]. Once you've done this, you can save the file with the ".sh" extension. Then make the file executable using the command "chmod +x FILENAME.sh". You now have now made your own executable copy of the LinEnum script on the target machine!
![](https://raw.githubusercontent.com/polo-sec/writing/master/Security%20Challenge%20Walkthroughs/Common%20Linux%20Privesc/Resources/3.png)
![](https://raw.githubusercontent.com/polo-sec/writing/master/Security%20Challenge%20Walkthroughs/Common%20Linux%20Privesc/Resources/4.png)
Running LinEnum
LinEnum can be run the same way you run any bash script, go to the directory where LinEnum is and run the command "./LinEnum.sh".
Understanding LinEnum Output
The LinEnum output is broken down into different sections, these are the main sections that we will focus on:
Kernel Kernel information is shown here. There is most likely a kernel exploit available for this machine.
Can we read/write sensitive files: The world-writable files are shown below. These are the files that any authenticated user can read and write to. By looking at the permissions of these sensitive files, we can see where there is misconfiguration that allows users who shouldn't usually be able to, to be able to write to sensitive files.
SUID Files: The output for SUID files is shown here. There are a few interesting items that we will definitely look into as a way to escalate privileges. SUID (Set owner User ID up on execution) is a special type of file permissions given to a file. It allows the file to run with permissions of whoever the owner is. If this is root, it runs with root permissions. It can allow us to escalate privileges.
Crontab Contents: The scheduled cron jobs are shown below. Cron is used to schedule commands at a specific time. These scheduled commands or tasks are known as “cron jobs”. Related to this is the crontab command which creates a crontab file containing commands and instructions for the cron daemon to execute. There is certainly enough information to warrant attempting to exploit Cronjobs here.
There's also a lot of other useful information contained in this scan. Lets have a read!
First, lets SSH into the target machine, using the credentials user3:password. This is to simulate getting a foothold on the system as a normal privilege user. *No answer needed*
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.122.19 - - [25/Aug/2022 00:33:33] "GET /LinEnum.sh HTTP/1.1" 200 -
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ ssh user3@10.10.122.19    
The authenticity of host '10.10.122.19 (10.10.122.19)' can't be established.
ED25519 key fingerprint is SHA256:jLEFDbU9QfFrO7qiwZE+2jefy4BgIndRJj79zvdIZoE.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.122.19' (ED25519) to the list of known hosts.
user3@10.10.122.19's password: 
Welcome to Linux Lite 4.4 (GNU/Linux 4.15.0-45-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

413 packages can be updated.
195 updates are security updates.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

Welcome to Linux Lite 4.4 user3
 
Thursday 25 August 2022, 00:32:48
Memory Usage: 341/1991MB (17.13%)
Disk Usage: 6/217GB (3%)
Support - https://www.linuxliteos.com/forums/ (Right click, Open Link)
 
user3@polobox:~$ wget http://10.11.81.220:8000/LinEnum.sh
--2022-08-25 00:33:32--  http://10.11.81.220:8000/LinEnum.sh
Connecting to 10.11.81.220:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 46631 (46K) [text/x-sh]
Saving to: ‘LinEnum.sh’

LinEnum.sh             100%[===========================>]  45.54K   108KB/s    in 0.4s    

2022-08-25 00:33:33 (108 KB/s) - ‘LinEnum.sh’ saved [46631/46631]

user3@polobox:~$ ls
Desktop    Downloads   Music     Public  Templates
Documents  LinEnum.sh  Pictures  shell   Videos
user3@polobox:~$ chmod +x LinEnum.sh
```
```text
user3@polobox:~$ ls
Desktop    Downloads   Music     Public  Templates
Documents  LinEnum.sh  Pictures  shell   Videos
user3@polobox:~$ chmod +x LinEnum.sh 
user3@polobox:~$ ./LinEnum.sh 

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
Thu Aug 25 00:34:32 EDT 2022                                                               
                                                                                           

### SYSTEM ##############################################
[-] Kernel information:
Linux polobox 4.15.0-45-generic #48-Ubuntu SMP Tue Jan 29 16:28:13 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux

[-] Kernel information (continued):
Linux version 4.15.0-45-generic (buildd@lgw01-amd64-031) (gcc version 7.3.0 (Ubuntu 7.3.0-16ubuntu3)) #48-Ubuntu SMP Tue Jan 29 16:28:13 UTC 2019

[-] Specific release information:
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=18.04
DISTRIB_CODENAME=bionic
DISTRIB_DESCRIPTION="Linux Lite 4.4"
NAME="Ubuntu"
VERSION="18.04.2 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.2 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic

[-] Hostname:
polobox

### USER/GROUP ##########################################
[-] Current user/group info:
uid=1002(user3) gid=1002(user3) groups=1002(user3)

[-] Users that have previously logged onto the system:
Username         Port     From             Latest
user3            pts/0    10.11.81.220     Thu Aug 25 00:32:48 -0400 2022
user8            pts/0    192.168.43.232   Mon Mar  2 10:33:59 -0500 2020

[-] Who else is logged on:
 00:34:32 up 4 min,  1 user,  load average: 0.12, 0.37, 0.19
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
user3    pts/0    10.11.81.220     00:32    6.00s  0.04s  0.00s /bin/bash ./LinEnum.sh

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
uid=100(systemd-timesync) gid=102(systemd-timesync) groups=102(systemd-timesync)
uid=101(systemd-network) gid=103(systemd-network) groups=103(systemd-network)
uid=102(systemd-resolve) gid=104(systemd-resolve) groups=104(systemd-resolve)
uid=104(syslog) gid=108(syslog) groups=108(syslog),4(adm)
uid=105(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=106(messagebus) gid=110(messagebus) groups=110(messagebus)
uid=107(uuidd) gid=111(uuidd) groups=111(uuidd)
uid=108(lightdm) gid=117(lightdm) groups=117(lightdm)
uid=109(ntp) gid=119(ntp) groups=119(ntp)
uid=110(avahi) gid=120(avahi) groups=120(avahi)
uid=111(colord) gid=123(colord) groups=123(colord)
uid=112(dnsmasq) gid=65534(nogroup) groups=65534(nogroup)
uid=113(hplip) gid=7(lp) groups=7(lp)
uid=114(nm-openconnect) gid=124(nm-openconnect) groups=124(nm-openconnect)
uid=115(nm-openvpn) gid=125(nm-openvpn) groups=125(nm-openvpn)
uid=116(pulse) gid=126(pulse) groups=126(pulse),29(audio)
uid=117(rtkit) gid=128(rtkit) groups=128(rtkit)
uid=118(saned) gid=129(saned) groups=129(saned),122(scanner)
uid=119(usbmux) gid=46(plugdev) groups=46(plugdev)
uid=103(geoclue) gid=105(geoclue) groups=105(geoclue)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=999(vboxadd) gid=1(daemon) groups=1(daemon)
uid=1000(user1) gid=1000(user1) groups=1000(user1)
uid=1001(user2) gid=1001(user2) groups=1001(user2)
uid=1002(user3) gid=1002(user3) groups=1002(user3)
uid=1003(user4) gid=1003(user4) groups=1003(user4),0(root)
uid=120(statd) gid=65534(nogroup) groups=65534(nogroup)
uid=1004(user5) gid=1004(user5) groups=1004(user5)
uid=1005(user6) gid=1005(user6) groups=1005(user6)
uid=121(mysql) gid=131(mysql) groups=131(mysql)
uid=1006(user7) gid=0(root) groups=0(root)
uid=1007(user8) gid=1007(user8) groups=1007(user8)
uid=122(sshd) gid=65534(nogroup) groups=65534(nogroup)

[-] It looks like we have some admin users:
uid=104(syslog) gid=108(syslog) groups=108(syslog),4(adm)

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
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
syslog:x:104:108::/home/syslog:/bin/false
_apt:x:105:65534::/nonexistent:/bin/false
messagebus:x:106:110::/var/run/dbus:/bin/false
uuidd:x:107:111::/run/uuidd:/bin/false
lightdm:x:108:117:Light Display Manager:/var/lib/lightdm:/bin/false
ntp:x:109:119::/home/ntp:/bin/false
avahi:x:110:120:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
colord:x:111:123:colord colour management daemon,,,:/var/lib/colord:/bin/false
dnsmasq:x:112:65534:dnsmasq,,,:/var/lib/misc:/bin/false
hplip:x:113:7:HPLIP system user,,,:/var/run/hplip:/bin/false
nm-openconnect:x:114:124:NetworkManager OpenConnect plugin,,,:/var/lib/NetworkManager:/bin/false
nm-openvpn:x:115:125:NetworkManager OpenVPN,,,:/var/lib/openvpn/chroot:/bin/false
pulse:x:116:126:PulseAudio daemon,,,:/var/run/pulse:/bin/false
rtkit:x:117:128:RealtimeKit,,,:/proc:/bin/false
saned:x:118:129::/var/lib/saned:/bin/false
usbmux:x:119:46:usbmux daemon,,,:/var/lib/usbmux:/bin/false
geoclue:x:103:105::/var/lib/geoclue:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
vboxadd:x:999:1::/var/run/vboxadd:/bin/false
user1:x:1000:1000:user1,,,:/home/user1:/bin/bash
user2:x:1001:1001:user2,,,:/home/user2:/bin/bash
user3:x:1002:1002:user3,,,:/home/user3:/bin/bash
user4:x:1003:1003:user4,,,:/home/user4:/bin/bash
statd:x:120:65534::/var/lib/nfs:/usr/sbin/nologin
user5:x:1004:1004:user5,,,:/home/user5:/bin/bash
user6:x:1005:1005:user6,,,:/home/user6:/bin/bash
mysql:x:121:131:MySQL Server,,,:/var/mysql:/bin/bash
user7:x:1006:0:user7,,,:/home/user7:/bin/bash
user8:x:1007:1007:user8,,,:/home/user8:/bin/bash
sshd:x:122:65534::/run/sshd:/usr/sbin/nologin

[-] Super user account(s):
root

[-] Accounts that have recently used sudo:
/home/user5/.sudo_as_admin_successful
/home/user7/.sudo_as_admin_successful
/home/user6/.sudo_as_admin_successful
/home/user1/.sudo_as_admin_successful
/home/user8/.sudo_as_admin_successful
/home/user4/.sudo_as_admin_successful
/home/user3/.sudo_as_admin_successful
/home/user2/.sudo_as_admin_successful

[-] Are permissions on /home directories lax:
total 40K
drwxr-xr-x 10 root  root  4.0K Jun  5  2019 .
drwxr-xr-x 23 root  root  4.0K Apr  9  2019 ..
drwxr-xr-x 22 user1 user1 4.0K Mar  2  2020 user1
drwxr-xr-x 22 user2 user2 4.0K Mar  2  2020 user2
drwxr-xr-x 22 user3 user3 4.0K Aug 25 00:33 user3
drwxr-xr-x 22 user4 user4 4.0K Mar  2  2020 user4
drwxr-xr-x 22 user5 user5 4.0K Mar  4  2020 user5
drwxr-xr-x 22 user6 user6 4.0K Mar  2  2020 user6
drwxr-xr-x 22 user7 root  4.0K Mar  2  2020 user7
drwxr-xr-x 22 user8 user8 4.0K Mar  2  2020 user8

### ENVIRONMENTAL #######################################
[-] Environment information:
SSH_CONNECTION=10.11.81.220 49178 10.10.122.19 22
LANG=en_US.UTF-8
XDG_SESSION_ID=2
USER=user3
QT_QPA_PLATFORMTHEME=qt5ct
PWD=/home/user3
HOME=/home/user3
SSH_CLIENT=10.11.81.220 49178 22
SSH_TTY=/dev/pts/0
GTK_MODULES=:canberra-gtk-module
MAIL=/var/mail/user3
SHELL=/bin/bash
TERM=xterm-256color
SHLVL=2
LOGNAME=user3
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1002/bus
XDG_RUNTIME_DIR=/run/user/1002
QT_AUTO_SCREEN_SCALE_FACTOR=0 
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
XDG_SESSION_COOKIE=467cfa02c550474bb86de9fac8d7106a-1661401966.611269-1763732986
_=/usr/bin/env

[-] Path information:
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
drwxr-xr-x 2 root root  4096 Feb 17  2019 /bin
drwxr-xr-x 2 root root 12288 Jun  4  2019 /sbin
drwxr-xr-x 2 root root 69632 Mar  2  2020 /usr/bin
drwxr-xr-x 2 root root  4096 Mar 20  2018 /usr/games
drwxr-xr-x 2 root root  4096 Mar 23  2018 /usr/local/bin
drwxr-xr-x 2 root root  4096 Apr 30  2016 /usr/local/games
drwxr-xr-x 2 root root  4096 Feb 17  2019 /usr/local/sbin
drwxr-xr-x 2 root root 12288 Mar  2  2020 /usr/sbin

[-] Available shells:
```
```text
# /etc/shells: valid login shells
/bin/sh
/bin/dash
/bin/bash
/bin/rbash

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
-rw-r--r-- 1 root root  780 Jun  4  2019 /etc/crontab

/etc/cron.d:
total 24
drwxr-xr-x   2 root root  4096 Jun  4  2019 .
drwxr-xr-x 162 root root 12288 Mar  6  2020 ..
-rw-r--r--   1 root root   712 Jan 17  2018 php
-rw-r--r--   1 root root   102 Apr  5  2016 .placeholder

/etc/cron.daily:
total 84
drwxr-xr-x   2 root root  4096 Jun  4  2019 .
drwxr-xr-x 162 root root 12288 Mar  6  2020 ..
-rwxr-xr-x   1 root root   539 Oct 10  2018 apache2
-rwxr-xr-x   1 root root   376 Nov 20  2017 apport
-rwxr-xr-x   1 root root  1478 Feb 26  2018 apt-compat
-rwxr-xr-x   1 root root   314 Nov 26  2015 aptitude
-rwxr-xr-x   1 root root   355 May 22  2012 bsdmainutils
-rwxr-xr-x   1 root root   384 Oct  5  2014 cracklib-runtime
-rwxr-xr-x   1 root root  1176 Nov  2  2017 dpkg
-rwxr-xr-x   1 root root  2211 Apr 13  2014 locate
-rwxr-xr-x   1 root root   372 May  6  2015 logrotate
-rwxr-xr-x   1 root root  1065 Feb 28  2018 man-db
-rwxr-xr-x   1 root root   538 Mar  1  2018 mlocate
-rwxr-xr-x   1 root root  1387 Dec 13  2017 ntp
-rwxr-xr-x   1 root root   249 Nov 12  2015 passwd
-rw-r--r--   1 root root   102 Apr  5  2016 .placeholder
-rwxr-xr-x   1 root root   383 Mar  7  2016 samba
-rwxr-xr-x   1 root root   246 Feb  6  2018 ubuntu-advantage-tools
-rwxr-xr-x   1 root root   214 Apr 12  2016 update-notifier-common

/etc/cron.hourly:
total 20
drwxr-xr-x   2 root root  4096 Mar 20  2018 .
drwxr-xr-x 162 root root 12288 Mar  6  2020 ..
-rw-r--r--   1 root root   102 Apr  5  2016 .placeholder

/etc/cron.monthly:
total 20
drwxr-xr-x   2 root root  4096 Mar 20  2018 .
drwxr-xr-x 162 root root 12288 Mar  6  2020 ..
-rw-r--r--   1 root root   102 Apr  5  2016 .placeholder

/etc/cron.weekly:
total 32
drwxr-xr-x   2 root root  4096 Feb 17  2019 .
drwxr-xr-x 162 root root 12288 Mar  6  2020 ..
-rwxr-xr-x   1 root root   730 Apr 13  2016 apt-xapian-index
-rwxr-xr-x   1 root root   723 Feb 28  2018 man-db
-rw-r--r--   1 root root   102 Apr  5  2016 .placeholder
-rwxr-xr-x   1 root root   211 Apr 12  2016 update-notifier-common

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
*/5  *    * * * root    /home/user4/Desktop/autoscript.sh
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#

[-] Systemd timers:
NEXT                         LEFT          LAST                         PASSED               UNIT                         ACTIVATES
Thu 2022-08-25 00:39:00 EDT  4min 19s left Thu 2022-08-25 00:30:12 EDT  4min 27s ago         phpsessionclean.timer        phpsessionclean.service
Thu 2022-08-25 00:43:39 EDT  8min left     Mon 2020-03-02 09:13:23 EST  2 years 5 months ago motd-news.timer              motd-news.service
Thu 2022-08-25 00:44:46 EDT  10min left    n/a                          n/a                  systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
Mon 2022-08-29 00:00:00 EDT  3 days left   Thu 2022-08-25 00:30:12 EDT  4min 27s ago         fstrim.timer                 fstrim.service

4 timers listed.
Enable thorough tests to see inactive timers

### NETWORKING  ##########################################
[-] Network and IP info:
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 9001
        inet 10.10.122.19  netmask 255.255.0.0  broadcast 10.10.255.255
        inet6 fe80::bf:dfff:fe44:3d71  prefixlen 64  scopeid 0x20<link>
        ether 02:bf:df:44:3d:71  txqueuelen 1000  (Ethernet)
        RX packets 344  bytes 77311 (77.3 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 496  bytes 72759 (72.7 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 203  bytes 16977 (16.9 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 203  bytes 16977 (16.9 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

[-] ARP history:
ip-10-10-0-1.eu-west-1.compute.internal (10.10.0.1) at 02:c8:85:b5:5a:aa [ether] on eth0

[-] Nameserver(s):
```
```text
# run "systemd-resolve --status" to see details about the actual nameservers.
nameserver 127.0.0.53

[-] Nameserver(s):
Global
         DNS Servers: 10.0.0.2
          DNS Domain: eu-west-1.compute.internal
          DNSSEC NTA: 10.in-addr.arpa
                      16.172.in-addr.arpa
                      168.192.in-addr.arpa
                      17.172.in-addr.arpa
                      18.172.in-addr.arpa
                      19.172.in-addr.arpa
                      20.172.in-addr.arpa
                      21.172.in-addr.arpa
                      22.172.in-addr.arpa
                      23.172.in-addr.arpa
                      24.172.in-addr.arpa
                      25.172.in-addr.arpa
                      26.172.in-addr.arpa
                      27.172.in-addr.arpa
                      28.172.in-addr.arpa
                      29.172.in-addr.arpa
                      30.172.in-addr.arpa
                      31.172.in-addr.arpa
                      corp
                      d.f.ip6.arpa
                      home
                      internal
                      intranet
                      lan
                      local
                      private
                      test

Link 2 (eth0)
      Current Scopes: DNS
       LLMNR setting: yes
MulticastDNS setting: no
      DNSSEC setting: no
    DNSSEC supported: no
         DNS Servers: 10.0.0.2
          DNS Domain: eu-west-1.compute.internal

[-] Default route:
default         ip-10-10-0-1.eu 0.0.0.0         UG    0      0        0 eth0

[-] Listening TCP:
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:139             0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:50673           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:44179           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:38867           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:53271           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:445             0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:2049            0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::139                  :::*                    LISTEN      -                   
tcp6       0      0 :::111                  :::*                    LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   
tcp6       0      0 :::38481                :::*                    LISTEN      -                   
tcp6       0      0 :::53939                :::*                    LISTEN      -                   
tcp6       0      0 :::39989                :::*                    LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 ::1:631                 :::*                    LISTEN      -                   
tcp6       0      0 :::445                  :::*                    LISTEN      -                   
tcp6       0      0 :::2049                 :::*                    LISTEN      -                   
tcp6       0      0 :::51937                :::*                    LISTEN      -                   

[-] Listening UDP:
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
udp        0      0 0.0.0.0:2049            0.0.0.0:*                           -                   
udp        0      0 127.0.0.53:53           0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:68              0.0.0.0:*                           -                   
udp        0      0 10.10.122.19:68         0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:111             0.0.0.0:*                           -                   
udp        0      0 10.10.255.255:137       0.0.0.0:*                           -                   
udp        0      0 10.10.122.19:137        0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:137             0.0.0.0:*                           -                   
udp        0      0 10.10.255.255:138       0.0.0.0:*                           -                   
udp        0      0 10.10.122.19:138        0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:138             0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:44184           0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:46298           0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:5353            0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:38199           0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:37266           0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:55914           0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:631             0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:39557           0.0.0.0:*                           -                   
udp        0      0 0.0.0.0:714             0.0.0.0:*                           -                   
udp6       0      0 :::2049                 :::*                                -                   
udp6       0      0 :::111                  :::*                                -                   
udp6       0      0 :::5353                 :::*                                -                   
udp6       0      0 :::46383                :::*                                -                   
udp6       0      0 :::36354                :::*                                -                   
udp6       0      0 :::47751                :::*                                -                   
udp6       0      0 :::714                  :::*                                -                   
udp6       0      0 :::49870                :::*                                -                   
udp6       0      0 :::60120                :::*                                -                   

### SERVICES #############################################
[-] Running processes:
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.5  0.4 159728  9024 ?        Ss   00:29   0:01 /sbin/init splash
root         2  0.0  0.0      0     0 ?        S    00:29   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        I    00:29   0:00 [kworker/0:0]
root         4  0.0  0.0      0     0 ?        I<   00:29   0:00 [kworker/0:0H]
root         5  0.0  0.0      0     0 ?        I    00:29   0:00 [kworker/u30:0]
root         6  0.0  0.0      0     0 ?        I<   00:29   0:00 [mm_percpu_wq]
root         7  0.0  0.0      0     0 ?        S    00:29   0:00 [ksoftirqd/0]
root         8  0.0  0.0      0     0 ?        I    00:29   0:00 [rcu_sched]
root         9  0.0  0.0      0     0 ?        I    00:29   0:00 [rcu_bh]
root        10  0.0  0.0      0     0 ?        S    00:29   0:00 [migration/0]
root        11  0.0  0.0      0     0 ?        S    00:29   0:00 [watchdog/0]
root        12  0.0  0.0      0     0 ?        S    00:29   0:00 [cpuhp/0]
root        13  0.0  0.0      0     0 ?        S    00:29   0:00 [kdevtmpfs]
root        14  0.0  0.0      0     0 ?        I<   00:29   0:00 [netns]
root        15  0.0  0.0      0     0 ?        S    00:29   0:00 [rcu_tasks_kthre]
root        16  0.0  0.0      0     0 ?        S    00:29   0:00 [kauditd]
root        17  0.0  0.0      0     0 ?        S    00:29   0:00 [xenbus]
root        18  0.0  0.0      0     0 ?        S    00:29   0:00 [xenwatch]
root        19  0.0  0.0      0     0 ?        I    00:29   0:00 [kworker/0:1]
root        20  0.0  0.0      0     0 ?        S    00:29   0:00 [khungtaskd]
root        21  0.0  0.0      0     0 ?        S    00:29   0:00 [oom_reaper]
root        22  0.0  0.0      0     0 ?        I<   00:29   0:00 [writeback]
root        23  0.0  0.0      0     0 ?        S    00:29   0:00 [kcompactd0]
root        24  0.0  0.0      0     0 ?        SN   00:29   0:00 [ksmd]
root        25  0.0  0.0      0     0 ?        SN   00:29   0:00 [khugepaged]
root        26  0.0  0.0      0     0 ?        I<   00:29   0:00 [crypto]
root        27  0.0  0.0      0     0 ?        I<   00:29   0:00 [kintegrityd]
root        28  0.0  0.0      0     0 ?        I<   00:29   0:00 [kblockd]
root        29  0.0  0.0      0     0 ?        I<   00:29   0:00 [ata_sff]
root        30  0.0  0.0      0     0 ?        I<   00:29   0:00 [md]
root        31  0.0  0.0      0     0 ?        I<   00:29   0:00 [edac-poller]
root        32  0.0  0.0      0     0 ?        I<   00:29   0:00 [devfreq_wq]
root        33  0.0  0.0      0     0 ?        I<   00:29   0:00 [watchdogd]
root        34  0.0  0.0      0     0 ?        I    00:29   0:00 [kworker/u30:1]
root        36  0.0  0.0      0     0 ?        S    00:29   0:00 [kswapd0]
root        37  0.0  0.0      0     0 ?        S    00:29   0:00 [ecryptfs-kthrea]
root        79  0.0  0.0      0     0 ?        I<   00:29   0:00 [kthrotld]
root        80  0.0  0.0      0     0 ?        I<   00:29   0:00 [acpi_thermal_pm]
root        81  0.0  0.0      0     0 ?        S    00:29   0:00 [scsi_eh_0]
root        82  0.0  0.0      0     0 ?        I<   00:29   0:00 [scsi_tmf_0]
root        83  0.0  0.0      0     0 ?        S    00:29   0:00 [scsi_eh_1]
root        84  0.0  0.0      0     0 ?        I<   00:29   0:00 [scsi_tmf_1]
root        85  0.0  0.0      0     0 ?        I    00:29   0:00 [kworker/u30:2]
root        86  0.0  0.0      0     0 ?        I    00:29   0:00 [kworker/u30:3]
root        90  0.0  0.0      0     0 ?        I<   00:29   0:00 [ipv6_addrconf]
root        99  0.0  0.0      0     0 ?        I<   00:29   0:00 [kstrp]
root       116  0.0  0.0      0     0 ?        I<   00:29   0:00 [kworker/0:1H]
root       117  0.0  0.0      0     0 ?        I<   00:29   0:00 [charger_manager]
root       169  0.0  0.0      0     0 ?        I    00:29   0:00 [kworker/0:2]
root       173  0.0  0.0      0     0 ?        I<   00:29   0:00 [ttm_swap]
root       274  0.0  0.0      0     0 ?        S    00:29   0:00 [jbd2/xvda1-8]
root       275  0.0  0.0      0     0 ?        I<   00:29   0:00 [ext4-rsv-conver]
root       325  0.0  0.6  94796 13792 ?        S<s  00:29   0:00 /lib/systemd/systemd-journald
root       332  0.0  0.0      0     0 ?        I    00:29   0:00 [kworker/u30:4]
root       340  0.0  0.0      0     0 ?        I<   00:29   0:00 [rpciod]
root       341  0.0  0.0      0     0 ?        I<   00:29   0:00 [xprtiod]
root       343  0.0  0.0  23920   180 ?        Ss   00:29   0:00 /usr/sbin/blkmapd
root       344  0.0  0.0  97708  1728 ?        Ss   00:29   0:00 /sbin/lvmetad -f
root       346  0.3  0.2  47364  5584 ?        Ss   00:29   0:00 /lib/systemd/systemd-udevd
root       469  0.0  0.0      0     0 ?        S    00:30   0:00 [jbd2/xvda4-8]
root       470  0.0  0.0      0     0 ?        I<   00:30   0:00 [ext4-rsv-conver]
root       473  0.0  0.0      0     0 ?        S    00:30   0:00 [jbd2/xvda2-8]
root       474  0.0  0.0      0     0 ?        I<   00:30   0:00 [ext4-rsv-conver]
systemd+   531  0.0  0.2  80028  5208 ?        Ss   00:30   0:00 /lib/systemd/systemd-networkd
systemd+   537  0.0  0.1 143976  3292 ?        Ssl  00:30   0:00 /lib/systemd/systemd-timesyncd
root       538  0.0  0.1  47600  3560 ?        Ss   00:30   0:00 /sbin/rpcbind -f -w
root       540  0.0  0.0  30040   228 ?        Ss   00:30   0:00 /usr/sbin/rpc.idmapd
root       616  0.0  0.2  70596  6084 ?        Ss   00:30   0:00 /lib/systemd/systemd-logind
root       623  0.0  0.5 517304 12100 ?        Ssl  00:30   0:00 /usr/lib/udisks2/udisksd
root       632  0.0  0.4 301456  8800 ?        Ssl  00:30   0:00 /usr/lib/accountsservice/accounts-daemon
root       635  0.0  0.4 427256  9080 ?        Ssl  00:30   0:00 /usr/sbin/ModemManager
syslog     643  0.0  0.2 267032  4372 ?        Ssl  00:30   0:00 /usr/sbin/rsyslogd -n
root       645  0.0  0.1  31320  3300 ?        Ss   00:30   0:00 /usr/sbin/cron -f
avahi      647  0.0  0.1  44908  3260 ?        Ss   00:30   0:00 avahi-daemon: registering [polobox.local]
root       650  0.0  0.0   4552   748 ?        Ss   00:30   0:00 /usr/sbin/acpid
root       657  0.0  0.8 170468 17188 ?        Ssl  00:30   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
message+   660  0.0  0.2  48428  5040 ?        Ss   00:30   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
avahi      686  0.0  0.0  44776   324 ?        S    00:30   0:00 avahi-daemon: chroot helper
root       720  0.0  0.8 421416 17460 ?        Ssl  00:30   0:00 /usr/sbin/NetworkManager --no-daemon
root       726  0.0  0.2  44752  5340 ?        Ss   00:30   0:00 /sbin/wpa_supplicant -u -s -O /run/wpa_supplicant
root       727  0.0  0.3 100564  7988 ?        Ss   00:30   0:00 /usr/sbin/cupsd -l
root       740  0.0  0.5 303652 10920 ?        Ssl  00:30   0:00 /usr/sbin/cups-browsed
root       807  0.0  0.5 308832 10616 ?        Ssl  00:30   0:00 /usr/lib/policykit-1/polkitd --no-debug
systemd+   827  0.0  0.3  70740  6296 ?        Ss   00:30   0:00 /lib/systemd/systemd-resolved
root       841  0.0  0.0  25660  1232 ?        Ss   00:30   0:00 /sbin/dhclient -1 -4 -v -pf /run/dhclient.eth0.pid -lf /var/lib/dhcp/dhclient.eth0.leases -I -df /var/lib/dhcp/dhclient6.eth0.leases eth0
root       971  0.0  0.0  38068   752 ?        Ss   00:30   0:00 /usr/sbin/rpc.mountd --manage-gids
root       987  0.0  0.0      0     0 ?        S    00:30   0:00 [lockd]
root      1003  0.0  0.0      0     0 ?        S    00:30   0:00 [nfsd]
root      1004  0.0  0.0      0     0 ?        S    00:30   0:00 [nfsd]
root      1005  0.0  0.0      0     0 ?        S    00:30   0:00 [nfsd]
root      1006  0.0  0.0      0     0 ?        S    00:30   0:00 [nfsd]
root      1007  0.0  0.0      0     0 ?        S    00:30   0:00 [nfsd]
root      1008  0.0  0.0      0     0 ?        S    00:30   0:00 [nfsd]
root      1009  0.0  0.0      0     0 ?        S    00:30   0:00 [nfsd]
root      1010  0.0  0.0      0     0 ?        S    00:30   0:00 [nfsd]
root      1057  0.0  0.2  72296  5804 ?        Ss   00:30   0:00 /usr/sbin/sshd -D
root      1068  0.0  0.5 265344 11884 ?        Ss   00:30   0:00 /usr/sbin/nmbd --foreground --no-process-group
root      1174  0.0  0.7 330772 16268 ?        Ss   00:30   0:00 /usr/sbin/apache2 -k start
user6     1175  0.0  0.3 330796  6220 ?        S    00:30   0:00 /usr/sbin/apache2 -k start
user6     1176  0.0  0.3 330796  6220 ?        S    00:30   0:00 /usr/sbin/apache2 -k start
user6     1177  0.0  0.3 330796  6220 ?        S    00:30   0:00 /usr/sbin/apache2 -k start
user6     1178  0.0  0.3 330796  6220 ?        S    00:30   0:00 /usr/sbin/apache2 -k start
user6     1179  0.0  0.3 330796  6220 ?        S    00:30   0:00 /usr/sbin/apache2 -k start
root      1183  0.0  0.9 353492 20376 ?        Ss   00:30   0:00 /usr/sbin/smbd --foreground --no-process-group
mysql     1188  0.1  8.5 1154572 174480 ?      Sl   00:30   0:00 /usr/sbin/mysqld --daemonize --pid-file=/run/mysqld/mysqld.pid
root      1274  0.0  0.2 344936  5956 ?        S    00:30   0:00 /usr/sbin/smbd --foreground --no-process-group
root      1275  0.0  0.2 344928  4780 ?        S    00:30   0:00 /usr/sbin/smbd --foreground --no-process-group
root      1315  0.0  0.3 354016  7316 ?        S    00:30   0:00 /usr/sbin/smbd --foreground --no-process-group
root      5978  0.0  0.4 382480  9064 ?        Ssl  00:31   0:00 /usr/sbin/lightdm
root      5991  0.0  0.1  15956  2464 ttyS0    Ss+  00:31   0:00 /sbin/agetty -o -p -- \u --keep-baud 115200,38400,9600 ttyS0 vt220
root      5993  0.2  2.5 340612 52168 tty7     Ssl+ 00:31   0:00 /usr/lib/xorg/Xorg -core :0 -seat seat0 -auth /var/run/lightdm/root/:0 -nolisten tcp vt7 -novtswitch
root      6004  0.0  0.3 271724  7940 ?        Sl   00:31   0:00 lightdm --session-child 16 19
lightdm   6010  0.0  0.3  76764  8080 ?        Ss   00:31   0:00 /lib/systemd/systemd --user
lightdm   6011  0.0  0.1 218816  2652 ?        S    00:31   0:00 (sd-pam)
lightdm   6027  0.0  0.0   4628   772 ?        Ss   00:31   0:00 /bin/sh /usr/lib/lightdm/lightdm-greeter-session /usr/sbin/lightdm-gtk-greeter
lightdm   6028  0.7  3.5 633212 72444 ?        Sl   00:31   0:01 /usr/sbin/lightdm-gtk-greeter
lightdm   6030  0.0  0.1  47628  3756 ?        Ss   00:31   0:00 /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
lightdm   6031  0.0  0.4 367932  8872 ?        Ssl  00:31   0:00 /usr/lib/at-spi2-core/at-spi-bus-launcher
lightdm   6034  0.0  0.3 284848  6860 ?        Ssl  00:31   0:00 /usr/lib/gvfs/gvfsd
lightdm   6039  0.0  0.3 366484  7992 ?        Sl   00:31   0:00 /usr/lib/gvfs/gvfsd-fuse /run/user/108/gvfs -f -o big_writes
lightdm   6042  0.0  0.1  47496  3636 ?        S    00:31   0:00 /usr/bin/dbus-daemon --config-file=/usr/share/defaults/at-spi2/accessibility.conf --nofork --print-address 3
lightdm   6050  0.0  0.2 220640  5348 ?        Sl   00:31   0:00 /usr/lib/at-spi2-core/at-spi2-registryd --use-gnome-session
root      6065  0.0  0.3 128252  6368 ?        S    00:31   0:00 lightdm --session-child 12 19
root      6066  0.0  0.3 126664  7948 ?        Ss   00:32   0:00 sshd: user3 [priv]
user3     6068  0.0  0.3  76776  7752 ?        Ss   00:32   0:00 /lib/systemd/systemd --user
user3     6069  0.0  0.1 218816  2652 ?        S    00:32   0:00 (sd-pam)
root      6080  0.0  0.3 604504  6980 ?        Ssl  00:32   0:00 /usr/sbin/console-kit-daemon --no-daemon
user3     6273  0.0  0.1 126664  3608 ?        S    00:32   0:00 sshd: user3@pts/0
user3     6275  0.0  0.2  22780  5404 pts/0    Ss   00:32   0:00 -bash
user3     6295  0.0  0.1  13676  4004 pts/0    S+   00:34   0:00 /bin/bash ./LinEnum.sh
user3     6296  0.0  0.1  13808  3028 pts/0    S+   00:34   0:00 /bin/bash ./LinEnum.sh
user3     6297  0.0  0.0   7476   820 pts/0    S+   00:34   0:00 tee -a
user3     6525  0.0  0.1  13808  2840 pts/0    S+   00:34   0:00 /bin/bash ./LinEnum.sh
user3     6526  0.0  0.1  37364  3376 pts/0    R+   00:34   0:00 ps aux

[-] Process binaries and associated permissions (from above list):
1.1M -rwxr-xr-x 1 root root 1.1M Apr  4  2018 /bin/bash
   0 lrwxrwxrwx 1 root root    4 Apr  9  2019 /bin/sh -> dash
1.6M -rwxr-xr-x 1 root root 1.6M Jan 29  2019 /lib/systemd/systemd
128K -rwxr-xr-x 1 root root 127K Jan 29  2019 /lib/systemd/systemd-journald
216K -rwxr-xr-x 1 root root 215K Jan 29  2019 /lib/systemd/systemd-logind
1.6M -rwxr-xr-x 1 root root 1.6M Jan 29  2019 /lib/systemd/systemd-networkd
