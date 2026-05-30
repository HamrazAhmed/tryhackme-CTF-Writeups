# harder — Writeup

## Overview
### harder — Writeup
### harder — Writeup
----
Real pentest findings combined
----
![](https://assets.tryhackme.com/img/banners/default_tryhackme.png)
![](https://tryhackme-images.s3.amazonaws.com/room-icons/4a70bd07bced343f9adf02c10e499ed5.png)
Start Machine
The machine is completely inspired by real world pentest findings. Perhaps you will consider them very challenging but without any rabbit holes. Once you have a shell it is very important to know which underlying linux distribution is used and where certain configurations are located.
Hints to the initial foodhold: Look closely at every request. Re-scan all newly found web services/folders and may use some wordlists from seclists ([https://tools.kali.org/password-attacks/seclists](https://tools.kali.org/password-attacks/seclists)). Read the source with care.
Edit: There is a second way to get root access without using any key...are you able to spot the bug?
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.5.192 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.5.192:2
Open 10.10.5.192:22
Open 10.10.5.192:80
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
Scanning 10.10.5.192 [3 ports]
Discovered open port 80/tcp on 10.10.5.192
Discovered open port 22/tcp on 10.10.5.192
Discovered open port 2/tcp on 10.10.5.192
Completed Connect Scan (3 total ports)
Initiating Service scan
Scanning 3 services on 10.10.5.192
Completed Service scan (3 services on 1 host)
NSE: Script scanning 10.10.5.192.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.5.192
Host is up, received user-set (0.21s latency).

PORT   STATE SERVICE REASON  VERSION
2/tcp  open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 f88c1e071df3de8a01f15051e4e600fe (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDEFmFCa+IH2JigaT+Z8eV8W3N0cSDkslS33rwJ1tptuG0IvY5mvhC/bYiNO9vTigCiTgkHXKiFp0Kog0kiPPzihW3PU8HSpQHuSAH27vRsKR9mHY24rj7PA2mPxjObkD6PqS4Yq2YVK6BKV3RY+dYIIe0nbqFNyB/QiK7+EXXHrQLnboMy35uXfM2vy02XJxDRlhd/lyepiMXWVdTo2LHgnjL8bl9oiRzIYEtYzXg7jQErNamPwes4fqokd4Di+ma5zmeCxYfu+75/E49gvQEwwUUWJNbjAokOe8XKUwZsJsoUcJAMqn/gk0HAVZ4rdHqziWTYIGSsNeTJHyX7vB3r
|   256 e65dea6c838620def0f03a1e5f7d47b5 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJtXi31P1Ad+O7K71zZTGscq53c+5mUQTA/KxVNEc1Xm3I/7ubkunbVoR4MWt5v4SrYZnVB7iUbjXWiwmzRnwOw=
|   256 e9efd378db9c47207e62829d8f6f456a (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKRvDffPpS8dq2oJcYvNPU2NzZtjbVppVt1wM8Y52P/i
22/tcp open  ssh     syn-ack OpenSSH 8.3 (protocol 2.0)
| ssh-hostkey: 
|   4096 cfe2d927d2d9f3f78e5dd2f99da4fb66 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCns4FcsZGpefUl1pFm7KRPBXz7nIQ590yiEd6aNm6DEKKVQOUUT4TtSEpCaUhnDU/+XHFBJfXdm73tzEwCgN7fyxmXSCWDWu1tC1zui3CA/sr/g5k+Az0u1yTvoc3eUSByeGvVyShubpuCB5Mwa2YZJxiHu/WzFrtDbGIGiVcQgLJTXdXE+aK7hbsx6T9HMJpKEnneRvLY4WT6ZNjw8kfp6oHMFvz/lnDffyWMNxn9biQ/pSkZHOsBzLcAfAYXIp6710byAWGwuZL2/d6Yq1jyLY3bic6R7HGVWEX6VDcrxAeED8uNHF8kPqh46dFkyHekOOye6TnALXMZ/uo3GSvrJd1OWx2kZ1uPJWOl2bKj1aVKKsLgAsmrrRtG1KWrZZDqpxm/iUerlJzAl3YdLxyqXnQXvcBNHR6nc4js+bJwTPleuCOUVvkS1QWkljSDzJ878AKBDBxVLcFI0vCiIyUm065lhgTiPf0+v4Et4IQ7PlAZLjQGlttKeaI54MZQPM53JPdVqASlVTChX7689Wm94//boX4/YlyWJ0EWz/a0yrwifFK/fHJWXYtQiQQI02gPzafIy7zI6bO3N7CCkWdTbBPmX+zvw9QcjCxaq1T+L/v04oi0K1StQlCUTE12M4fMeO/HfAQYCRm6tfue2BlAriIomF++Bh4yO73z3YeNuQ==
|   256 1e457b0ab5aa87e61bb1b79f5d8f8570 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIB+INGLWU0nf9OkPJkFoW9Gx2tdNEjLVXHrtZg17ALjH
80/tcp open  http    syn-ack nginx 1.18.0
|_http-title: Error
| http-methods: 
|_  Supported Methods: GET HEAD POST
|_http-server-header: nginx/1.18.0
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
Nmap done: 1 IP address (1 host up) scanned in 25.12 seconds

<span class="text-muted">This page is powered by php-fpm</span>

                                                                                  
┌──(witty㉿kali)-[~/Downloads]
└─$ nikto -host http://10.10.5.192 
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.5.192
+ Target Hostname:    10.10.5.192
+ Target Port:        80
---------------------------------------------------------------------------
+ Server: nginx/1.18.0
+ /: Retrieved x-powered-by header: PHP/7.3.19.
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ /: Cookie TestCookie created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ No CGI Directories found (use '-C all' to force check all possible dirs)

┌──(witty㉿kali)-[~/Downloads]
└─$ dirsearch -u http://10.10.5.192 -i200,301,302,401 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 220545

Output File: /home/witty/.dirsearch/reports/10.10.5.192/_23-07-17_19-09-42.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-07-17_19-09-42.log

Target: http://10.10.5.192/

[19:09:43] Starting: 
[19:10:14] 301 -  169B  - /vendor  ->  http://10.10.5.192:8080/vendor/

response 

HTTP/1.1 200 OK

Server: nginx/1.18.0

Date: Mon, 17 Jul 2023 23:08:19 GMT

Content-Type: text/html; charset=UTF-8

Connection: close

Vary: Accept-Encoding

X-Powered-By: PHP/7.3.19

Set-Cookie: TestCookie=just+a+test+cookie; expires=Tue, 18-Jul-2023 00:08:19 GMT; Max-Age=3600; path=/; domain=pwd.harder.local; secure

Content-Length: 1985

┌──(witty㉿kali)-[~/Downloads]
└─$ tac /etc/hosts
10.10.5.192  pwd.harder.local

http://pwd.harder.local/index.php

admin:admin

extra security in place. our source code will be reviewed soon ...

┌──(witty㉿kali)-[~/Downloads]
└─$ wfuzz -u pwd.harder.local -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host: FUZZ.harder.local" --hc 404 --hw 166
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://pwd.harder.local/
Total requests: 114441

=====================================================================
ID           Response   Lines    Word       Chars       Payload          
=====================================================================

000001726:   200        23 L     457 W      19912 Ch    "shell"   

┌──(witty㉿kali)-[~/Downloads]
└─$ tac /etc/hosts
10.10.5.192  pwd.harder.local shell.harder.local

http://shell.harder.local/index.php

admin:admin

Invalid login credentials!

┌──(witty㉿kali)-[~/Downloads]
└─$ dirsearch -u shell.harder.local -i200,301,302,401 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 220545

Output File: /home/witty/.dirsearch/reports/shell.harder.local_23-07-17_19-18-39.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-07-17_19-18-39.log

Target: http://shell.harder.local/

[19:18:40] Starting: 
[19:18:58] 301 -  169B  - /vendor  ->  http://shell.harder.local:8080/vendor/
CTRL+C detected: Pausing threads, please wait...

using another wordlist

/usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-files.txt

or large

┌──(witty㉿kali)-[~/Downloads]
└─$ cat /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt | grep gitignore

┌──(witty㉿kali)-[~/Downloads]
└─$ dirsearch -u pwd.harder.local -i200,301,302,401 -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-files.txt

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 17129

Output File: /home/witty/.dirsearch/reports/pwd.harder.local_23-07-17_19-25-05.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-07-17_19-25-05.log

Target: http://pwd.harder.local/

[19:25:06] Starting: 
[19:25:08] 200 -   19KB - /index.php
[19:25:10] 200 -    0B  - /auth.php
[19:25:12] 200 -   19KB - /.
[19:25:27] 301 -  169B  - /.git  ->  http://pwd.harder.local:8080/.git/

┌──(witty㉿kali)-[~/Downloads]
└─$ dirsearch -u shell.harder.local -i200,301,302,401 -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-files.txt 

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 17129

Output File: /home/witty/.dirsearch/reports/shell.harder.local_23-07-17_19-24-29.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-07-17_19-24-29.log

Target: http://shell.harder.local/

[19:24:36] Starting: 
[19:24:39] 200 -   19KB - /index.php
[19:24:41] 200 -    0B  - /auth.php
[19:24:44] 200 -   19KB - /.
[19:24:57] 200 -   73B  - /ip.php

http://shell.harder.local/ip.php

Your IP is not allowed to use this webservice. Only 10.10.10.x is allowed

X-Forwarded-For:10.10.10.1

response

HTTP/1.1 200 OK

Server: nginx/1.18.0

Date: Mon, 17 Jul 2023 23:28:45 GMT

Content-Type: text/html; charset=UTF-8

Connection: close

Vary: Accept-Encoding

X-Powered-By: PHP/7.3.19

Content-Length: 0

┌──(witty㉿kali)-[~/Downloads]
└─$ cat index.gitignore 
credentials.php
secret.php

┌──(witty㉿kali)-[~/Downloads]
└─$ cd ../bug_hunter 
                                                                              
┌──(witty㉿kali)-[~/bug_hunter]
└─$ ls     
Burp-Suite                   GG-Dorking      MyScripts         svn-extractor
CertificateTransparencyLogs  github-search   pastebin-scraper  waybackMachine
commoncrawl                  GitTools        Photon            xsser
Endpoints                    knockpy_report  s3brute           XSStrike
GCPBucketBrute               lazyrecon       SQLiDetector      xxeserv
                                                                              
┌──(witty㉿kali)-[~/bug_hunter]
└─$ cd GitTools 
                                                                              
┌──(witty㉿kali)-[~/bug_hunter/GitTools]
└─$ ls
Dumper  Extractor  Finder  LICENSE.md  README.md
                                                                              
┌──(witty㉿kali)-[~/bug_hunter/GitTools]
└─$ cd Dumper   
                                                                              
┌──(witty㉿kali)-[~/bug_hunter/GitTools/Dumper]
└─$ ls
gitdumper.sh  README.md

┌──(witty㉿kali)-[~/bug_hunter/GitTools/Dumper]
└─$ ./gitdumper.sh http://pwd.harder.local/.git/ git
###########
```
```text
# GitDumper is part of https://github.com/internetwache/GitTools
#
```
```text
# Developed and maintained by @gehaxelt from @internetwache
#
```
```text
# Use at your own risk. Usage might be illegal in certain circumstances.
```
```text
# Only for educational purposes!
###########

[*] Destination folder does not exist
[+] Creating git/.git/
[+] Downloaded: HEAD
[-] Downloaded: objects/info/packs
[+] Downloaded: description
[+] Downloaded: config
[+] Downloaded: COMMIT_EDITMSG
[+] Downloaded: index
[-] Downloaded: packed-refs
[+] Downloaded: refs/heads/master
[-] Downloaded: refs/remotes/origin/HEAD
[-] Downloaded: refs/stash
[+] Downloaded: logs/HEAD
[+] Downloaded: logs/refs/heads/master
[-] Downloaded: logs/refs/remotes/origin/HEAD
[-] Downloaded: info/refs
[+] Downloaded: info/exclude
[-] Downloaded: /refs/wip/index/refs/heads/master
[-] Downloaded: /refs/wip/wtree/refs/heads/master
[+] Downloaded: objects/93/99abe877c92db19e7fc122d2879b470d7d6a58
[-] Downloaded: objects/00/00000000000000000000000000000000000000
[+] Downloaded: objects/ad/68cc6e2a786c4e671a6a00d6f7066dc1a49fc3
[+] Downloaded: objects/04/7afea4868d8b4ce8e7d6ca9eec9c82e3fe2161
[+] Downloaded: objects/e3/361e96c0a9db20541033f254df272deeb9dba7
[+] Downloaded: objects/c6/66164d58b28325393533478750410d6bbdff53
[+] Downloaded: objects/aa/938abf60c64cdb2d37d699409f77427c1b3826
[+] Downloaded: objects/cd/a7930579f48816fac740e2404903995e0ff614
[+] Downloaded: objects/22/8694f875f20080e29788d7cc3b626272107462
[+] Downloaded: objects/66/428e37f6bfaac0b42ce66106bee0a5bdf94d4e
[+] Downloaded: objects/6e/1096eae64fede71a78e54999236553b75b3b65
[+] Downloaded: objects/be/c719ffb34ca3d424bd170df5f6f37050d8a91c

┌──(witty㉿kali)-[~/bug_hunter/GitTools/Dumper]
└─$ cd git   
                                                                              
┌──(witty㉿kali)-[~/bug_hunter/GitTools/Dumper/git]
└─$ ls
                                                                              
┌──(witty㉿kali)-[~/bug_hunter/GitTools/Dumper/git]
└─$ ls -lah
total 12K
drwxr-xr-x 3 witty witty 4.0K Jul 17 19:35 .
drwxr-xr-x 3 witty witty 4.0K Jul 17 19:35 ..
drwxr-xr-x 6 witty witty 4.0K Jul 17 19:35 .git
                                                                              
┌──(witty㉿kali)-[~/bug_hunter/GitTools/Dumper/git]
└─$ cd .git         
                                                                              
┌──(witty㉿kali)-[~/…/GitTools/Dumper/git/.git]
└─$ ls -lah
total 44K
drwxr-xr-x  6 witty witty 4.0K Jul 17 19:35 .
drwxr-xr-x  3 witty witty 4.0K Jul 17 19:35 ..
-rw-r--r--  1 witty witty   14 Jul 17 19:35 COMMIT_EDITMSG
-rw-r--r--  1 witty witty   92 Jul 17 19:35 config
-rw-r--r--  1 witty witty   73 Jul 17 19:35 description
-rw-r--r--  1 witty witty   23 Jul 17 19:35 HEAD
-rw-r--r--  1 witty witty  361 Jul 17 19:35 index
drwxr-xr-x  2 witty witty 4.0K Jul 17 19:35 info
drwxr-xr-x  3 witty witty 4.0K Jul 17 19:35 logs
drwxr-xr-x 15 witty witty 4.0K Jul 17 19:35 objects
drwxr-xr-x  5 witty witty 4.0K Jul 17 19:35 refs
                                                                              
┌──(witty㉿kali)-[~/…/GitTools/Dumper/git/.git]
└─$ git log                                       
commit 9399abe877c92db19e7fc122d2879b470d7d6a58 (HEAD -> master)
Author: evs <evs@harder.htb>
Date:   Thu Oct 3 18:12:23 2019 +0300

    add gitignore

commit 047afea4868d8b4ce8e7d6ca9eec9c82e3fe2161
Author: evs <evs@harder.htb>
Date:   Thu Oct 3 18:11:32 2019 +0300

    add extra security

commit ad68cc6e2a786c4e671a6a00d6f7066dc1a49fc3
Author: evs <evs@harder.htb>
Date:   Thu Oct 3 14:00:52 2019 +0300

    added index.php
                                                                              
                          
┌──(witty㉿kali)-[~/…/GitTools/Dumper/git/.git]
└─$ cd ..           
                                                                              
┌──(witty㉿kali)-[~/bug_hunter/GitTools/Dumper/git]
└─$ git checkout .
Updated 4 paths from the index
