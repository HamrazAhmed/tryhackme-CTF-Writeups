---
Penetration Testing Challenge
---

# Internal — Writeup

## Overview
### Internal — Writeup
### Internal — Writeup
![](https://tryhackme-images.s3.amazonaws.com/room-icons/222b3e855f88a482c1267748f76f90e0.jpeg)
### Pre-engagement Briefing
You have been assigned to a client that wants a penetration test conducted on an environment due to be released to production in three weeks.
Scope of Work
The client requests that an engineer conducts an external, web app, and internal assessment of the provided virtual environment. The client has asked that minimal information be provided about the assessment, wanting the engagement conducted from the eyes of a malicious actor (black box penetration test).  The client has asked that you secure two flags (no location provided) as proof of exploitation:
User.txt
Root.txt
Additionally, the client has provided the following scope allowances:
Ensure that you modify your hosts file to reflect internal.thm
Any tools or techniques are permitted in this engagement
Locate and note all vulnerabilities found
Submit the flags discovered to the dashboard
Only the IP address assigned to your machine is in scope
(Roleplay off)
I encourage you to approach this challenge as an actual penetration test. Consider writing a report, to include an executive summary, vulnerability and exploitation assessment, and remediation suggestions, as this will benefit you in preparation for the eLearnsecurity eCPPT or career as a penetration tester in the field.
Note - this room can be completed without Metasploit
**Writeups will not be accepted for this room.**
### Deploy and Engage the Client Environment
Having accepted the project, you are provided with the client assessment environment.  Secure the User and Root flags and submit them to the dashboard as proof of exploitation.
```text
┌──(kali㉿kali)-[~]
└─$ ping 10.10.97.105                      
PING 10.10.97.105 (10.10.97.105) 56(84) bytes of data.
64 bytes from 10.10.97.105: icmp_seq=1 ttl=63 time=202 ms
64 bytes from 10.10.97.105: icmp_seq=2 ttl=63 time=202 ms
^C
--- 10.10.97.105 ping statistics ---
3 packets transmitted, 2 received, 33.3333% packet loss, time 2006ms
rtt min/avg/max/mdev = 201.531/201.670/201.809/0.139 ms

ttl=63 so linux
```
```text
┌──(kali㉿kali)-[~]
└─$ sudo nano /etc/hosts                             
[sudo] password for kali:
```
```text
┌──(kali㉿kali)-[~]
└─$ cat /etc/hosts         
127.0.0.1       localhost
127.0.1.1       kali
10.10.113.254   magician
10.10.121.237   git.git-and-crumpets.thm
10.10.149.10    hipflasks.thm hipper.hipflasks.thm
10.10.91.93     raz0rblack raz0rblack.thm
10.10.234.77    lab.enterprise.thm
10.10.96.58     source
10.10.59.104    CONTROLLER.local
10.10.54.75     acmeitsupport.thm
10.10.102.33    overwrite.uploadvulns.thm shell.uploadvulns.thm java.uploadvulns.thm annex.uploadvulns.thm magic.uploadvulns.thm jewel.uploadvulns.thm demo.uploadvulns.thm
10.10.179.221   development.smag.thm
10.10.87.241    mafialive.thm
10.10.97.105    internal.thm
```
```text
# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```
```text
┌──(kali㉿kali)-[~]
└─$ ping internal.thm
PING internal.thm (10.10.97.105) 56(84) bytes of data.
64 bytes from internal.thm (10.10.97.105): icmp_seq=1 ttl=63 time=199 ms
64 bytes from internal.thm (10.10.97.105): icmp_seq=2 ttl=63 time=197 ms
64 bytes from internal.thm (10.10.97.105): icmp_seq=3 ttl=63 time=210 ms
^C
--- internal.thm ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2004ms
rtt min/avg/max/mdev = 196.600/201.695/209.705/5.733 ms
```

## Enumeration
```text
┌──(kali㉿kali)-[~]
└─$ sudo nmap -sC -sV -T4 -A -Pn -sS -n -O internal.thm
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-28 11:52 EDT
Nmap scan report for internal.thm (10.10.97.105)
Host is up (0.18s latency).
Not shown: 997 closed tcp ports (reset)
PORT     STATE    SERVICE VERSION
22/tcp   open     ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 6e:fa:ef:be:f6:5f:98:b9:59:7b:f7:8e:b9:c5:62:1e (RSA)
|   256 ed:64:ed:33:e5:c9:30:58:ba:23:04:0d:14:eb:30:e9 (ECDSA)
|_  256 b0:7f:7f:7b:52:62:62:2a:60:d4:3d:36:fa:89:ee:ff (ED25519)
80/tcp   open     http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.29 (Ubuntu)
9220/tcp filtered unknown
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=9/28%OT=22%CT=1%CU=33593%PV=Y%DS=2%DC=T%G=Y%TM=63346DF
OS:4%P=x86_64-pc-linux-gnu)SEQ(SP=FD%GCD=1%ISR=10C%TI=Z%CI=Z%II=I%TS=A)SEQ(
OS:SP=FD%GCD=1%ISR=10B%TI=Z%CI=Z%TS=A)OPS(O1=M505ST11NW7%O2=M505ST11NW7%O3=
OS:M505NNT11NW7%O4=M505ST11NW7%O5=M505ST11NW7%O6=M505ST11)WIN(W1=F4B3%W2=F4
OS:B3%W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3)ECN(R=Y%DF=Y%T=40%W=F507%O=M505NNSNW7
OS:%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=
OS:Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%
OS:RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0
OS:%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIP
OS:CK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 587/tcp)
HOP RTT       ADDRESS
1   195.37 ms 10.11.0.1
2   195.56 ms 10.10.97.105

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 32.92 seconds
zsh: segmentation fault  sudo nmap -sC -sV -T4 -A -Pn -sS -n -O internal.thm
```
```text
┌──(kali㉿kali)-[~]
└─$ feroxbuster --url http://internal.thm -w /usr/share/wordlists/dirb/common.txt -t 60 -C 404,403

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.7.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://internal.thm
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
200      GET      375l      964w    10918c http://internal.thm/
301      GET        9l       28w      311c http://internal.thm/blog => http://internal.thm/blog/
200      GET      375l      964w    10918c http://internal.thm/index.html
301      GET        9l       28w      317c http://internal.thm/javascript => http://internal.thm/javascript/
301      GET        9l       28w      317c http://internal.thm/phpmyadmin => http://internal.thm/phpmyadmin/
301      GET        9l       28w      316c http://internal.thm/wordpress => http://internal.thm/wordpress/
301      GET        9l       28w      324c http://internal.thm/javascript/jquery => http://internal.thm/javascript/jquery/
301      GET        0l        0w        0c http://internal.thm/blog/index.php => http://internal.thm/blog/
301      GET        9l       28w      321c http://internal.thm/phpmyadmin/doc => http://internal.thm/phpmyadmin/doc/
200      GET       98l      278w    22486c http://internal.thm/phpmyadmin/favicon.ico
200      GET       26l      359w        0c http://internal.thm/phpmyadmin/index.php
301      GET        9l       28w      320c http://internal.thm/phpmyadmin/js => http://internal.thm/phpmyadmin/js/
[###########>--------] - 37s    20491/36912   30s     found:11      errors:437    
[#########>----------] - 37s    20511/41526   38s     found:12      errors:437    
[#########>----------] - 37s    20543/41526   38s     found:12      errors:437    
[#########>----------] - 37s    20643/41526   38s     found:12      errors:437    
[#########>----------] - 37s    20656/41526   38s     found:12      errors:437    
[#########>----------] - 37s    20705/41526   38s     found:12      errors:439    
[##########>---------] - 37s    20790/41526   38s     found:12      errors:444    
[##########>---------] - 37s    20820/41526   38s     found:12      errors:444    
[##########>---------] - 37s    20874/41526   37s     found:12      errors:445    
[##########>---------] - 37s    20935/41526   37s     found:12      errors:445    
[##########>---------] - 37s    20970/41526   37s     found:12      errors:445    
[##########>---------] - 37s    21040/41526   37s     found:12      errors:454    
[##########>---------] - 37s    21088/41526   37s     found:12      errors:455    
301      GET        9l       28w      324c http://internal.thm/phpmyadmin/locale => http://internal.thm/phpmyadmin/locale/

wordpress enumeration

Browsing /blog confirms our assumption, this is a Wordpress blog. Let’s enumerate the users with wpscan:
```
```text
┌──(kali㉿kali)-[~]
└─$ wpscan --url http://internal.thm/blog -e u                             
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.22
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[i] It seems like you have not updated the database for some time.
[?] Do you want to update now? [Y]es [N]o, default: [N]
[+] URL: http://internal.thm/blog/ [10.10.97.105]
[+] Started: Wed Sep 28 12:08:23 2022

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.29 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://internal.thm/blog/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://internal.thm/blog/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://internal.thm/blog/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.4.2 identified (Insecure, released on 2020-06-10).
 | Found By: Rss Generator (Passive Detection)
 |  - http://internal.thm/blog/index.php/feed/, <generator>https://wordpress.org/?v=5.4.2</generator>
 |  - http://internal.thm/blog/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.4.2</generator>

[+] WordPress theme in use: twentyseventeen
 | Location: http://internal.thm/blog/wp-content/themes/twentyseventeen/
 | Last Updated: 2022-05-24T00:00:00.000Z
 | Readme: http://internal.thm/blog/wp-content/themes/twentyseventeen/readme.txt
 | [!] The version is out of date, the latest version is 3.0
 | Style URL: http://internal.thm/blog/wp-content/themes/twentyseventeen/style.css?ver=20190507
 | Style Name: Twenty Seventeen
