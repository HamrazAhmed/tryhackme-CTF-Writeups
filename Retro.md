---
New high score!
---

# Retro — Writeup

## Overview
### Retro — Writeup
### Retro — Writeup
![](https://i.imgur.com/RDzWHJI.png)
![|333](https://tryhackme-images.s3.amazonaws.com/room-icons/a222ca9fb08b8bdc9e10a0f6ba41ea99.jpeg)
### Pwn
![|333](https://i.imgur.com/kUwtBc8.png)
Can you time travel? If not, you might want to think about the next best thing.
Please note that this machine does not respond to ping (ICMP) and may take a few minutes to boot up.
-------------------------------------
There are two distinct paths that can be taken on Retro. One requires significantly less trial and error, however, both will work. Please check writeups if you are curious regarding the two paths. An alternative version of this room is available in it's remixed version Blaster.

## Enumeration
```text
┌──(kali㉿kali)-[~]
└─$ sudo nmap -sC -sV -T4 -A -Pn -sS -n -O 10.10.106.113
[sudo] password for kali: 
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-28 13:16 EDT
Nmap scan report for 10.10.106.113
Host is up (0.21s latency).
Not shown: 998 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-title: IIS Windows Server
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: RETROWEB
|   NetBIOS_Domain_Name: RETROWEB
|   NetBIOS_Computer_Name: RETROWEB
|   DNS_Domain_Name: RetroWeb
|   DNS_Computer_Name: RetroWeb
|   Product_Version: 10.0.14393
|_  System_Time: 2022-09-28T17:16:43+00:00
| ssl-cert: Subject: commonName=RetroWeb
| Not valid before: 2022-09-27T17:15:11
|_Not valid after:  2023-03-29T17:15:11
|_ssl-date: 2022-09-28T17:16:47+00:00; 0s from scanner time.
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2016 (89%), FreeBSD 6.X (85%)
OS CPE: cpe:/o:microsoft:windows_server_2016 cpe:/o:freebsd:freebsd:6.2
Aggressive OS guesses: Microsoft Windows Server 2016 (89%), FreeBSD 6.2-RELEASE (85%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

TRACEROUTE (using port 80/tcp)
HOP RTT       ADDRESS
1   205.34 ms 10.11.0.1
2   206.26 ms 10.10.106.113

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 44.40 seconds
zsh: segmentation fault  sudo nmap -sC -sV -T4 -A -Pn -sS -n -O 10.10.106.113
```
```text
┌──(kali㉿kali)-[~]
└─$ feroxbuster --url http://10.10.106.113 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 60 -C 404,403 

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.7.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.106.113
 🚀  Threads               │ 60
 📖  Wordlist              │ /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
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
200      GET       32l       55w      703c http://10.10.106.113/
301      GET        2l       10w      150c http://10.10.106.113/retro => http://10.10.106.113/retro/
301      GET        2l       10w      161c http://10.10.106.113/retro/wp-content => http://10.10.106.113/retro/wp-content/
301      GET        2l       10w      168c http://10.10.106.113/retro/wp-content/themes => http://10.10.106.113/retro/wp-content/themes/
301      GET        2l       10w      169c http://10.10.106.113/retro/wp-content/uploads => http://10.10.106.113/retro/wp-content/uploads/
301      GET        2l       10w      169c http://10.10.106.113/retro/wp-content/plugins => http://10.10.106.113/retro/wp-content/plugins/
301      GET        2l       10w      162c http://10.10.106.113/retro/wp-includes => http://10.10.106.113/retro/wp-includes/
301      GET        2l       10w      169c http://10.10.106.113/retro/wp-includes/images => http://10.10.106.113/retro/wp-includes/images/
301      GET        2l       10w      169c http://10.10.106.113/retro/wp-content/upgrade => http://10.10.106.113/retro/wp-content/upgrade/
301      GET        2l       10w      175c http://10.10.106.113/retro/wp-includes/images/media => http://10.10.106.113/retro/wp-includes/images/media/
301      GET        2l       10w      169c http://10.10.106.113/retro/wp-includes/Images => http://10.10.106.113/retro/wp-includes/Images/
301      GET        2l       10w      167c http://10.10.106.113/retro/wp-includes/text => http://10.10.106.113/retro/wp-includes/text/

add ip to /etc/hosts because when enter ip/retro/wp-admin gives an error which is the localhost of mine so add it!
```
```text
┌──(kali㉿kali)-[~]
└─$ sudo nano /etc/hosts
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
10.10.106.113   retro.thm
```
```text
# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

http://retro.thm/retro/wp-login.php

using wpscan

Now, we will use wpscan to enumerate plugins, themes, and users.
```
```text
┌──(kali㉿kali)-[~]
└─$ wpscan --url http://retro.thm/retro -e u
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
[+] URL: http://retro.thm/retro/ [10.10.106.113]
[+] Started: Wed Sep 28 13:31:31 2022

Interesting Finding(s):

[+] Headers
 | Interesting Entries:
 |  - Server: Microsoft-IIS/10.0
 |  - X-Powered-By: PHP/7.1.29
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://retro.thm/retro/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://retro.thm/retro/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://retro.thm/retro/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.2.1 identified (Insecure, released on 2019-05-21).
 | Found By: Rss Generator (Passive Detection)
 |  - http://retro.thm/retro/index.php/feed/, <generator>https://wordpress.org/?v=5.2.1</generator>
 |  - http://retro.thm/retro/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.2.1</generator>

[+] WordPress theme in use: 90s-retro
 | Location: http://retro.thm/retro/wp-content/themes/90s-retro/
 | Latest Version: 1.4.10 (up to date)
 | Last Updated: 2019-04-15T00:00:00.000Z
 | Readme: http://retro.thm/retro/wp-content/themes/90s-retro/readme.txt
 | Style URL: http://retro.thm/retro/wp-content/themes/90s-retro/style.css?ver=5.2.1
 | Style Name: 90s Retro
 | Style URI: https://organicthemes.com/retro-theme/
 | Description: Have you ever wished your WordPress blog looked like an old Geocities site from the 90s!? Probably n...
 | Author: Organic Themes
 | Author URI: https://organicthemes.com
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.4.10 (80% confidence)
 | Found By: Style (Passive Detection)
