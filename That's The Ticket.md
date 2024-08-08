# That's The Ticket — Writeup

## Overview
### That's The Ticket — Writeup
### That's The Ticket — Writeup
----
IT Support are going to have a bad day, can you get into the admin account?
----
![](https://assets.tryhackme.com/additional/thatstheticket/banner.png)
Start Machine
IT Support is going to have a really bad day today, but don't think they're stupid! They have really strict firewalls!
Using the IT support portal try and make your way into the admin account.
**Hint:** Our HTTP & DNS Logging tool on [http://10.10.10.100](http://10.10.10.100/) may come in useful!
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.84.149 --ulimit 5500 -b 65535 -- -A -Pn
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

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.84.149:22
Open 10.10.84.149:80
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
DNS resolution of 1 IPs took 0.01s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.84.149 [2 ports]
Discovered open port 22/tcp on 10.10.84.149
Discovered open port 80/tcp on 10.10.84.149
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.84.149
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.84.149.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.84.149
Host is up, received user-set (0.18s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 bfc39c992cc4e2d92033d13cdc0148d2 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC8dfacBZcXm48CzKZh1Vd6tO6p86sR7PyBbxJj9q9Zifzlq+GmD+r1eXLaH+waOWnD/fmPr8CtScSVP0iu0opnIZ21A4Zy/SOjNKVuDWGWP36cj/XxiTlLL3qfOk0OXy/xVEYycYWhiJm1VLhOSg5Tk3xGGJRBY9V1MfBF/Oq2DdEcODzUnh/JLikJctZ15DwGTaY+6ehl6Kh1PwRQ6XZmhLP42P9NtPCY8AkXCO2EJrE/tzckhUzi4vr17Z0M4zZd8AZX1SfX3t5hULhKMDbQ7zRQNTIeaLYdPBa4Yu3Ze2annUvOlKhnTKm+omW7vbXKWurIWRqyG59F12sNHl3P
|   256 0820c273c7c5d7a7ef020911fc85a8e2 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBO1cxZc0WJgiYCd7m7sxzMYbgVLjqIc40ZZi4Y+M+YHJeISCq1bhTMLSpIWHxwpnQg+qVD3wrgYWI9Hr6FGGMrg=
|   256 1f51682b5e99574cb740150574d00d9b (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFCYrvmQ5DCiI8ZbvzVWWIkj1apQr36j4vJ8K8MfUCKz
80/tcp open  http    syn-ack nginx 1.14.0 (Ubuntu)
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: Ticket Manager > Home
| http-methods: 
|_  Supported Methods: GET HEAD POST
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
Nmap done: 1 IP address (1 host up) scanned in 20.52 seconds

┌──(root㉿kali)-[/home/witty/Downloads]
└─# dirsearch -u http://10.10.84.149/ -i200,301,302,401

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 10927

Output File: /root/.dirsearch/reports/10.10.84.149/-_23-07-28_14-13-44.txt

Error Log: /root/.dirsearch/logs/errors-23-07-28_14-13-44.log

Target: http://10.10.84.149/

[14:13:45] Starting: 
[14:15:40] 200 -    2KB - /login
[14:15:41] 200 -    2KB - /login/
[14:15:42] 302 -    0B  - /logout  ->  /
[14:15:42] 302 -    0B  - /logout/  ->  /
[14:16:11] 200 -    2KB - /register

after registering
XSS
<div><textarea name="message" class="form-control" style="height: 200px;"></textarea></div>
