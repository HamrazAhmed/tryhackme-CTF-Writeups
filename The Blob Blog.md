# The Blob Blog — Writeup

## Overview
### The Blob Blog — Writeup
### The Blob Blog — Writeup
----
Successfully hack into bobloblaw's computer
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/8c7c2c9a239e2badd7a5a62df9eff1d5.png)
Start Machine
Can you root the box?
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.209.198 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.209.198:22
Open 10.10.209.198:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.94 ( https://nmap.org )
Happy 26th Birthday to Nmap, may it live to be 126!
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
DNS resolution of 1 IPs took 0.01s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.209.198 [2 ports]
Discovered open port 22/tcp on 10.10.209.198
Discovered open port 80/tcp on 10.10.209.198
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.209.198
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.209.198.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.209.198
Host is up, received user-set (0.21s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 e7:28:a6:33:66:4e:99:9e:8e:ad:2f:1b:49:ec:3e:e8 (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBALXivx0EdFUjWn8Hg9zVrEE0+FIVsz0Dgt27TYzwHsc2NBir/vuOaG2wuM28Yu1yY5yX8QyIT7QvvtGwpZMS9wGy0x+mjSzMVgkkUpMDp2Yholkm9NH/CDhaA8zg3HxGd8/EdnHMLWszgF58xPCjUAtL3tZK09B4w/pdM0FFAF5BAAAAFQDzhIOaKK76v9eKeZNe0ZgkHVdyWQAAAIEAirSNjm02GVhgTbV6I60sZmY9nWORouyVp+Y+K0MQF+Jvxr0QQEWFeIVNbYNW0eg06VJ0JLexGNttrT/N6LPU4KBR7zIGOshLhXV847rwkUjODCt0ZeLjUv0X8o6T4ExZi92VLBylxQmk2OMgUIyeVPVbAsDAK2N0LFWHfpLTbl0AAACARqXryFKMWJQTJ1Ta5dX4bCZ20ulsATRbFuMLH1OZoA7gM2A2rijxPvK6Vp/VJt7701LhgI0dUZClMLC8q0OXaTEO3Ao6zdJb8W5snDue2TrPm12UnELgUD/NwWVqyjgYq1UgZ+71l+3fy6Q8opDILH+RYmAypIXb29dXvICjC5U=
|   2048 86:fc:ed:ce:46:63:4d:fd:ca:74:b6:50:46:ac:33:0f (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDgOLGhQs3olTn9V7fF/VB8GkElTVbM33EOlppILeLZmIdeg0NkxZdScAjalP4AB/yiU/01Whysy6NhOeuyVfwRhCkvpoWkN1X20YI6fPdTE5TLOeR+m78IXXZlyBSj2GOqvM7tPr0BqvfpsoxkS4zXVYG4OhxZDR4/rmXA9GaSOTzGEOWj839sbW6cdos5nanQSdEhDM441+GeUfXfPh+nqasy422AEhDqFh6cDRcQw5MXR2pt+VicabIfcVjRNRCmNgpx3nbJ/u1TeNC8C40krEiH735AbPd/Bu/Hbg2hY0AR7I/2dwsZMMcQ6weRLY0bOdW8wWPTIgdWN65DVAlf
|   256 e0:cc:05:0a:1b:8f:5e:a8:83:7d:c3:d2:b3:cf:91:ca (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOdOqWQM/+hxmRNa9Np94ZyfIfPGqNPOMKRMQkwCUXxrEfrC6RxnuNQolldjaSZtTx4nd/qWQqcNvrFbifP942o=
|   256 80:e3:45:b2:55:e2:11:31:ef:b1:fe:39:a8:90:65:c5 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJCjSR4Gytw2HNoqL4fDTKnxm0d8U/16kopRnicLqWMM
80/tcp open  http    syn-ack Apache httpd 2.4.7 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.7 (Ubuntu)
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
Nmap done: 1 IP address (1 host up) scanned in 15.16 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ dirsearch -u http://10.10.209.198 -H "User-Agent: HackerOne VDP wittyale" -i200,301,302,401

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 10927

Output File: /home/witty/.dirsearch/reports/10.10.209.198/_23-09-01_11-17-59.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-09-01_11-17-59.log

Target: http://10.10.209.198/

[11:18:00] Starting: 
[11:19:26] 200 -   13KB - /index.html

Task Completed

┌──(witty㉿kali)-[~/Downloads]
└─$ nikto -host http://10.10.209.198 -useragent "User-Agent: HackerOne VDP wittyale"
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.209.198
+ Target Hostname:    10.10.209.198
+ Target Port:        80
---------------------------------------------------------------------------
+ Server: Apache/2.4.7 (Ubuntu)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /: Server may leak inodes via ETags, header found with file /, inode: 3400, size: 5ab85cfdde1d0, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ Apache/2.4.7 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ OPTIONS: Allowed HTTP Methods: GET, HEAD, POST, OPTIONS .

Engagement Tools

Using Comments search with burp

K1stLS0+Kys8XT4rLisrK1stPisrKys8XT4uLS0tLisrKysrKysrKy4tWy0+KysrKys8XT4tLisrKytbLT4rKzxdPisuLVstPisrKys8XT4uLS1bLT4rKysrPF0+LS4tWy0+KysrPF0+LS4tLVstLS0+KzxdPi0tLitbLS0tLT4rPF0+KysrLlstPisrKzxdPisuLVstPisrKzxdPi4tWy0tLT4rKzxdPisuLS0uLS0tLS0uWy0+KysrPF0+Li0tLS0tLS0tLS0tLS4rWy0tLS0tPis8XT4uLS1bLS0tPis8XT4uLVstLS0tPis8XT4rKy4rK1stPisrKzxdPi4rKysrKysrKysrKysuLS0tLS0tLS0tLi0tLS0uKysrKysrKysrLi0tLS0tLS0tLS0uLS1bLS0tPis8XT4tLS0uK1stLS0tPis8XT4rKysuWy0+KysrPF0+Ky4rKysrKysrKysrKysrLi0tLS0tLS0tLS0uLVstLS0+KzxdPi0uKysrK1stPisrPF0+Ky4tWy0+KysrKzxdPi4tLVstPisrKys8XT4tLi0tLS0tLS0tLisrKysrKy4tLS0tLS0tLS0uLS0tLS0tLS0uLVstLS0+KzxdPi0uWy0+KysrPF0+Ky4rKysrKysrKysrKy4rKysrKysrKysrKy4tWy0+KysrPF0+LS4rWy0tLT4rPF0+KysrLi0tLS0tLS4rWy0tLS0+KzxdPisrKy4tWy0tLT4rKzxdPisuKysrLisuLS0tLS0tLS0tLS0tLisrKysrKysrLi1bKys+LS0tPF0+Ky4rKysrK1stPisrKzxdPi4tLi1bLT4rKysrKzxdPi0uKytbLS0+KysrPF0+LlstLS0+Kys8XT4tLS4rKysrK1stPisrKzxdPi4tLS0tLS0tLS0uWy0tLT4rPF0+LS0uKysrKytbLT4rKys8XT4uKysrKysrLi0tLS5bLS0+KysrKys8XT4rKysuK1stLS0tLT4rPF0+Ky4tLS0tLS0tLS0uKysrKy4tLS4rLi0tLS0tLS4rKysrKysrKysrKysrLisrKy4rLitbLS0tLT4rPF0+KysrLitbLT4rKys8XT4rLisrKysrKysrKysrLi4rKysuKy4rWysrPi0tLTxdPi4rK1stLS0+Kys8XT4uLlstPisrPF0+Ky5bLS0tPis8XT4rLisrKysrKysrKysrLi1bLT4rKys8XT4tLitbLS0tPis8XT4rKysuLS0tLS0tLitbLS0tLT4rPF0+KysrLi1bLS0tPisrPF0+LS0uKysrKysrKy4rKysrKysuLS0uKysrK1stPisrKzxdPi5bLS0tPis8XT4tLS0tLitbLS0tLT4rPF0+KysrLlstLT4rKys8XT4rLi0tLS0tLi0tLS0tLS0tLS0tLS4tLS1bLT4rKysrPF0+Li0tLS0tLS0tLS0tLS4tLS0uKysrKysrKysrLi1bLT4rKysrKzxdPi0uKytbLS0+KysrPF0+Li0tLS0tLS0uLS0tLS0tLS0tLS0tLi0tLVstPisrKys8XT4uLS0tLS0tLS0tLS0tLi0tLS4rKysrKysrKysuLVstPisrKysrPF0+LS4tLS0tLVstPisrPF0+LS4tLVstLS0+Kys8XT4tLg==

from base64 then brainfck
When I was a kid, my friends and I would always knock on 3 of our neighbors doors. Always houses 1, then 3, then 5!

Dang it Bob, why do you always forget your password?
I'll encode for you here so nobody else can figure out what it is: 
HcfP8J54AK4

https://www.dcode.fr/cipher-identifier

from base58

cUpC4k3s

┌──(witty㉿kali)-[~/Downloads]
└─$ ssh bob@10.10.209.198     
The authenticity of host '10.10.209.198 (10.10.209.198)' can't be established.
ED25519 key fingerprint is SHA256:0XkBHUMyhHjf9e2PYYI/NKQLKJ7jY7Yjr5jt672T5i0.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.209.198' (ED25519) to the list of known hosts.
bob@10.10.209.198's password: 
Permission denied, please try again.

┌──(witty㉿kali)-[~/Downloads]
└─$ knock 10.10.209.198 1 3 5                                 
                                                                                  
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.209.198 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.209.198:21
Open 10.10.209.198:22
Open 10.10.209.198:80
Open 10.10.209.198:445
Open 10.10.209.198:8080
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.94 ( https://nmap.org )
Happy 26th Birthday to Nmap, may it live to be 126!
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
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.209.198 [5 ports]
Discovered open port 22/tcp on 10.10.209.198
Discovered open port 80/tcp on 10.10.209.198
Discovered open port 445/tcp on 10.10.209.198
Discovered open port 21/tcp on 10.10.209.198
Discovered open port 8080/tcp on 10.10.209.198
Completed Connect Scan (5 total ports)
Initiating Service scan
Scanning 5 services on 10.10.209.198
Completed Service scan (5 services on 1 host)
NSE: Script scanning 10.10.209.198.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
NSE Timing: About 98.43% done; ETC: 11:41 (0:00:00 remaining)
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.209.198
Host is up, received user-set (0.18s latency).

PORT     STATE SERVICE REASON  VERSION
21/tcp   open  ftp     syn-ack vsftpd 3.0.2
22/tcp   open  ssh     syn-ack OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 e7:28:a6:33:66:4e:99:9e:8e:ad:2f:1b:49:ec:3e:e8 (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBALXivx0EdFUjWn8Hg9zVrEE0+FIVsz0Dgt27TYzwHsc2NBir/vuOaG2wuM28Yu1yY5yX8QyIT7QvvtGwpZMS9wGy0x+mjSzMVgkkUpMDp2Yholkm9NH/CDhaA8zg3HxGd8/EdnHMLWszgF58xPCjUAtL3tZK09B4w/pdM0FFAF5BAAAAFQDzhIOaKK76v9eKeZNe0ZgkHVdyWQAAAIEAirSNjm02GVhgTbV6I60sZmY9nWORouyVp+Y+K0MQF+Jvxr0QQEWFeIVNbYNW0eg06VJ0JLexGNttrT/N6LPU4KBR7zIGOshLhXV847rwkUjODCt0ZeLjUv0X8o6T4ExZi92VLBylxQmk2OMgUIyeVPVbAsDAK2N0LFWHfpLTbl0AAACARqXryFKMWJQTJ1Ta5dX4bCZ20ulsATRbFuMLH1OZoA7gM2A2rijxPvK6Vp/VJt7701LhgI0dUZClMLC8q0OXaTEO3Ao6zdJb8W5snDue2TrPm12UnELgUD/NwWVqyjgYq1UgZ+71l+3fy6Q8opDILH+RYmAypIXb29dXvICjC5U=
|   2048 86:fc:ed:ce:46:63:4d:fd:ca:74:b6:50:46:ac:33:0f (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDgOLGhQs3olTn9V7fF/VB8GkElTVbM33EOlppILeLZmIdeg0NkxZdScAjalP4AB/yiU/01Whysy6NhOeuyVfwRhCkvpoWkN1X20YI6fPdTE5TLOeR+m78IXXZlyBSj2GOqvM7tPr0BqvfpsoxkS4zXVYG4OhxZDR4/rmXA9GaSOTzGEOWj839sbW6cdos5nanQSdEhDM441+GeUfXfPh+nqasy422AEhDqFh6cDRcQw5MXR2pt+VicabIfcVjRNRCmNgpx3nbJ/u1TeNC8C40krEiH735AbPd/Bu/Hbg2hY0AR7I/2dwsZMMcQ6weRLY0bOdW8wWPTIgdWN65DVAlf
|   256 e0:cc:05:0a:1b:8f:5e:a8:83:7d:c3:d2:b3:cf:91:ca (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOdOqWQM/+hxmRNa9Np94ZyfIfPGqNPOMKRMQkwCUXxrEfrC6RxnuNQolldjaSZtTx4nd/qWQqcNvrFbifP942o=
|   256 80:e3:45:b2:55:e2:11:31:ef:b1:fe:39:a8:90:65:c5 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJCjSR4Gytw2HNoqL4fDTKnxm0d8U/16kopRnicLqWMM
80/tcp   open  http    syn-ack Apache httpd 2.4.7 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
445/tcp  open  http    syn-ack Apache httpd 2.4.7 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
8080/tcp open  http    syn-ack Werkzeug httpd 1.0.1 (Python 3.5.3)
|_http-server-header: Werkzeug/1.0.1 Python/3.5.3
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_smb2-time: Protocol negotiation failed (SMB2)
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 48961/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 37860/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 46570/udp): CLEAN (Timeout)
|   Check 4 (port 35156/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
|_smb2-security-mode: Couldn't establish a SMBv2 connection.

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
Nmap done: 1 IP address (1 host up) scanned in 59.05 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ ftp 10.10.209.198                                        
Connected to 10.10.209.198.
220 (vsFTPd 3.0.2)
Name (10.10.209.198:witty): anonymous
530 Permission denied.
ftp: Login failed
ftp> exit
221 Goodbye.
                                                                                   
┌──(witty㉿kali)-[~/Downloads]
└─$ ftp 10.10.209.198
Connected to 10.10.209.198.
220 (vsFTPd 3.0.2)
Name (10.10.209.198:witty): bob
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lah
229 Entering Extended Passive Mode (|||33995|).
150 Here comes the directory listing.
dr-xr-xr-x    3 1001     1001         4096 Jul 25  2020 .
dr-xr-xr-x    3 1001     1001         4096 Jul 25  2020 ..
-rw-r--r--    1 1001     1001          220 Jul 25  2020 .bash_logout
-rw-r--r--    1 1001     1001         3771 Jul 25  2020 .bashrc
-rw-r--r--    1 1001     1001          675 Jul 25  2020 .profile
-rw-r--r--    1 1001     1001         8980 Jul 25  2020 examples.desktop
dr-xr-xr-x    3 65534    65534        4096 Jul 25  2020 ftp
226 Directory send OK.
ftp> more .bash_logout
```
```text
# ~/.bash_logout: executed by bash(1) when login shell exits.
```
```text
# when leaving the console clear the screen to increase privacy

if [ "$SHLVL" = 1 ]; then
    [ -x /usr/bin/clear_console ] && /usr/bin/clear_console -q
fi

ftp> more .bashrc
```
```text
# ~/.bashrc: executed by bash(1) for non-login shells.
```
```text
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
```
```text
# for examples
```
```text
# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac
```
```text
# don't put duplicate lines or lines starting with space in the history.
```
```text
# See bash(1) for more options
HISTCONTROL=ignoreboth
```
```text
# append to the history file, don't overwrite it
shopt -s histappend
```
```text
# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000
```
```text
# check the window size after each command and, if necessary,
```
```text
# update the values of LINES and COLUMNS.
shopt -s checkwinsize
```
```text
# If set, the pattern "**" used in a pathname expansion context will
```
```text
# match all files and zero or more directories and subdirectories.
#shopt -s globstar
```
```text
# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"
```
```text
# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi
```
```text
# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac
```
```text
# uncomment for a colored prompt, if the terminal has the capability; turned
```
```text
# off by default to not distract the user: the focus in a terminal window
```
```text
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
```
```text
# We have color support; assume it's compliant with Ecma-48
```
```text
# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
```
```text
# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[
01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt
```
```text
# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac
```
```text
# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolor
s -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi
```
```text
# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote
=01'
```
```text
# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
```
```text
# Add an "alert" alias for long running commands.  Use like so:
```
```text
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo er
ror)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
```
```text
# Alias definitions.
```
```text
# You may want to put all your additions into a separate file like
```
```text
# ~/.bash_aliases, instead of adding them here directly.
```
```text
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```
```text
# enable programmable completion features (you don't need to enable
```
```text
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
```
```text
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

ftp> more .profile
```
```text
# ~/.profile: executed by the command interpreter for login shells.
```
```text
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
```
```text
# exists.
```
```text
# see /usr/share/doc/bash/examples/startup-files for examples.
```
```text
# the files are located in the bash-doc package.
```
```text
# the default umask is set in /etc/profile; for setting the umask
```
```text
# for ssh logins, install and configure the libpam-umask package.
#umask 022
```
```text
# if running bash
if [ -n "$BASH_VERSION" ]; then
```
```text
# include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
	. "$HOME/.bashrc"
    fi
fi
```
```text
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

ftp> more examples.desktop
[Desktop Entry]
Version=1.0
Type=Link
Name=Examples
Name[aa]=Ceelallo
Name[ace]=Contoh
Name[af]=Voorbeelde
Name[am]=ምሳሌዎች
Name[an]=Exemplos
Name[ar]=أمثلة
Name[ast]=Exemplos
Name[az]=Nümunələr
Name[be]=Прыклады
Name[bg]=Примери
Name[bn]=উদাহরণ
Name[br]=Skouerioù
Name[bs]=Primjeri
Name[ca]=Exemples
Name[ca@valencia]=Exemples
Name[ckb]=نمونه‌كان
Name[cs]=Ukázky
Name[csb]=Przëmiôrë
Name[cy]=Enghreifftiau
Name[da]=Eksempler
Name[de]=Beispiele
Name[dv]=މިސާލުތަށް
Name[el]=Παραδείγματα
Name[en_AU]=Examples
Name[en_CA]=Examples
Name[en_GB]=Examples
Name[eo]=Ekzemploj
Name[es]=Ejemplos
Name[et]=Näidised
Name[eu]=Adibideak
Name[fa]=نمونه‌ها
Name[fi]=Esimerkkejä
Name[fil]=Mga halimbawa
Name[fo]=Dømir
Name[fr]=Exemples
Name[fur]=Esemplis
Name[fy]=Foarbylden
Name[ga]=Samplaí
Name[gd]=Buill-eisimpleir
Name[gl]=Exemplos
Name[gu]=દૃષ્ટાન્તો
Name[gv]=Sampleyryn
Name[he]=דוגמאות
Name[hi]=उदाहरण
Name[hr]=Primjeri
Name[ht]=Egzanp
Name[hu]=Minták
Name[hy]=Օրինակներ
Name[id]=Contoh
Name[is]=Sýnishorn
Name[it]=Esempi
Name[ja]=サンプル
Name[ka]=ნიმუშები
Name[kk]=Мысалдар
Name[kl]=Assersuutit
Name[km]=ឧទាហរណ៍
Name[kn]=ಉದಾಹರಣೆಗಳು
Name[ko]=예시
Name[ku]=Mînak
Name[kw]=Ensamplow
Name[ky]=Мисалдар
Name[lb]=Beispiller
Name[lt]=Pavyzdžių failai
Name[lv]=Paraugi
Name[mg]=Ohatra
Name[mhr]=Пример-влак
Name[mi]=Tauira
Name[mk]=Примери
Name[ml]=ഉദാഹരണങ്ങള്‍
Name[mr]=उदाहरणे
Name[ms]=Contoh-contoh
Name[my]=ဥပမာများ
Name[nb]=Eksempler
Name[nds]=Bispelen
Name[ne]=उदाहरणहरू
Name[nl]=Voorbeeld-bestanden
Name[nn]=Døme
Name[nso]=Mehlala
Name[oc]=Exemples
Name[pa]=ਉਦਾਹਰਨਾਂ
Name[pl]=Przykłady
Name[pt]=Exemplos
Name[pt_BR]=Exemplos
Name[ro]=Exemple
Name[ru]=Примеры
Name[sc]=Esempiusu
Name[sco]=Examples
Name[sd]=مثالون
Name[se]=Ovdamearkkat
Name[shn]=တူဝ်ယၢင်ႇ
Name[si]=නිදසුන්
Name[sk]=Príklady
Name[sl]=Zgledi
Name[sml]=Saga Saupama
Name[sn]=Miyenzaniso
Name[sq]=Shembujt
Name[sr]=Примери
Name[sv]=Exempel
Name[sw]=Mifano
Name[szl]=Bajszpile
Name[ta]=உதாரணங்கள்
Name[ta_LK]=உதாரணங்கள்
Name[te]=ఉదాహరణలు
Name[tg]=Намунаҳо
Name[th]=ตัวอย่าง
Name[tr]=Örnekler
Name[tt]=Мисаллар
Name[ug]=مىساللار
Name[uk]=Приклади
Name[ur]=مثالیں
Name[uz]=Намуналар
Name[vec]=Esempi
Name[vi]=Mẫu ví dụ
Name[wae]=Bischbil
Name[zh_CN]=示例
Name[zh_HK]=範例
Name[zh_TW]=範例
Comment=Example content for Ubuntu
