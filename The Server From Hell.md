# The Server From Hell — Writeup

## Overview
### The Server From Hell — Writeup
### The Server From Hell — Writeup
----
Face a server that feels as if it was configured and deployed by Satan himself. Can you escalate to root?
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/15aae7a0b9c12597a7a7cd9f7db85c48.jpeg)
Start Machine
Start at port 1337 and enumerate your way.
Good luck.
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~]
└─$ rustscan -a 10.10.173.229 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.173.229:111
Open 10.10.173.229:2049
Open 10.10.173.229:33613
Open 10.10.173.229:41851
Open 10.10.173.229:57621
Open 10.10.173.229:60329

┌──(witty㉿kali)-[~]
└─$ nc 10.10.173.229 1337
Welcome traveller, to the beginning of your journey
To begin, find the trollface
Legend says he's hiding in the first 100 ports
Try printing the banners from the ports  

┌──(witty㉿kali)-[~]
└─$ nc 10.10.173.229 1-100 -v           
10.10.173.229: inverse host lookup failed: Unknown host
(UNKNOWN) [10.10.173.229] 100 (?) open
220 NZl-OlG ESMTP
250-vAFRKNmc
250-AUTH LOGIN CRAM-MD5 PLAIN
250-AUTH=LOGIN CRAM-MD5 PLAIN
250-PIPELINING
250 8BITMIME

(UNKNOWN) [10.10.173.229] 99 (?) open
This is MoneyWorks; Server is on Windows

(UNKNOWN) [10.10.173.229] 98 (?) open
������!����

EXFO BVV

WARNING: This system is for use by authorized users only!

Password: 
(UNKNOWN) [10.10.173.229] 97 (?) open
HTTP/1.7 200 OK
Date: k
MIME-version: 1.7
Server: ZOT-PS-46Y

(UNKNOWN) [10.10.173.229] 96 (?) open
HTTP/1.1 069 i
Server: Mongrel 63620564

(UNKNOWN) [10.10.173.229] 95 (?) open
HTTP/1.0 200 Ok
Server: Embeded_httpd
Date: q
Content-Type: text/html
Connection: close

<html>

<head>
<META NAME="GENERATOR" Content="Multi-Functional Broadband NAT Router (R233801)">
(UNKNOWN) [10.10.173.229] 94 (?) open
uaversionbindjPowerDNS Recursor 9
(UNKNOWN) [10.10.173.229] 93 (?) open
220 Xerox Phaser pr
421 Service not available, closing control connection

(UNKNOWN) [10.10.173.229] 92 (?) open
220 Indy FTP-Server bereit.

(UNKNOWN) [10.10.173.229] 91 (?) open
220 -rVt FTP server ready.
500 '': command not understood.
500 '': command not understood.

(UNKNOWN) [10.10.173.229] 90 (?) open
cvs [server aborted]: bad auth protocol start: HELP

(UNKNOWN) [10.10.173.229] 89 (?) open
HTTP/1.1 400 Bad request
s<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>400 Header 'Host' is missing.</title>
(UNKNOWN) [10.10.173.229] 88 (kerberos) open
TrueWeather

>
(UNKNOWN) [10.10.173.229] 87 (?) open
����Welcome to the Agilent PNA Network Analyzer at pcZXo

SCPI> 
(UNKNOWN) [10.10.173.229] 86 (?) open
HTTP/1.1 785 x
Server: gSOAP/435

(UNKNOWN) [10.10.173.229] 85 (?) open
HTTP/1.1 302 Object Moved
Location: /vpn/index.html
Connection: close

(UNKNOWN) [10.10.173.229] 84 (?) open
HTTP/1.1 404 Unknown host.
Server: Varnish

(UNKNOWN) [10.10.173.229] 83 (?) open
$
 jlek��00000000�00000000000000
(UNKNOWN) [10.10.173.229] 82 (?) open
220  ESMTP Service (Lotus Domino Build VcshZSNYX Beta q) ready at 
(UNKNOWN) [10.10.173.229] 81 (?) open
HTTP/1.1 401 Unauthorized
Server: RabbIT proxy version GO
Content-type: text/html; charset=utf-8
Cache-Control: no-cache
Pragma: no-cache
Date: a
WWW-Authenticate: Basic realm="V:1"

(UNKNOWN) [10.10.173.229] 80 (http) open
<boinc_gui_rpc_reply>
<client_version>9/client_version>
<unauthorized/>
</boinc_gui_rpc_reply>

(UNKNOWN) [10.10.173.229] 79 (finger) open
HTTP/1.1 302 Moved Temporarily
rServer: iTP WebServer with NSJSP/uwqNgWIPr (HTTP/1.1 Connector)
Location: http://EsmJoP:3index.html

(UNKNOWN) [10.10.173.229] 78 (?) open
HTTP/1.1 404 Not Found
Content-Length: 0
Cache-Control: no-cache,no-store,no-cache
Content-Type: application/json
Pragma: no-cache,no-cache

HTTP/1.1 404 Not Found
Content-Length: 0
Cache-Control: no-cache,no-store,no-cache
Content-Type: application/json
Pragma: no-cache,no-cache

(UNKNOWN) [10.10.173.229] 77 (?) open
������

Lantronix MSS1 Version STI3.5/5(981103)

Type HELP at the 'Local_2> ' prompt for assistance.

Login password> 
(UNKNOWN) [10.10.173.229] 76 (?) open
0r00000eTNSLSNR for 2,24}: Version 0 - Production
(UNKNOWN) [10.10.173.229] 75 (?) open
220 PkC ESMTP Citadel server ready.

(UNKNOWN) [10.10.173.229] 74 (?) open
000�<MsgHeader_PI>
<type>RODS_VERSION</type>
<msgLen>6/msgLen>
<errorLen>0</errorLen>
<bsLen>0</bsLen>
<intInfo>0</intInfo>
</MsgHeader_PI>
<Version_PI>
<status>-1/status>
<relVersion>rodstYxGlqDw</relVersion>
<apiVersion>d</apiVersion>
<reconnPort>0</reconnPort>
<reconnAddr></reconnAddr>
<cookie>0</cookie>
</Version_PI>

(UNKNOWN) [10.10.173.229] 73 (?) open
+OK POP3 Cm [cppop 6] at [
(UNKNOWN) [10.10.173.229] 72 (?) open
HTTP/1.1 404 Not Found
Date: s GMT
Server: Unknown
Connection: close
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<HTML><HEAD>
<TITLE>404 Not Found</TITLE>
</HEAD><BODY>
<H1>Not Found</H1>
The requested URL / was not found on this server.<P>
</BODY></HTML>

(UNKNOWN) [10.10.173.229] 71 (?) open
$
 ylbghB000000000�00000000000000
(UNKNOWN) [10.10.173.229] 70 (gopher) open
�0�0�00�az�0000Jlprvpgxacsmcnij000<,dnwabct0swl000000000000000000000000000000000000000000000000000000000000000000000000����0x0�
(UNKNOWN) [10.10.173.229] 69 (?) open
HTTP/1.0 200 OK
t<title>Remote Buddy by IOSPIRIT</title>
(UNKNOWN) [10.10.173.229] 68 (?) open
����version00000U000�~000000000nsgitati00000000000000000��iaochv00000000000000000��smxsthodkumfsp.urfik
(UNKNOWN) [10.10.173.229] 67 (?) open
HTTP/1.1 217 n
WWW-Authenticate: Basic realm="Netopia-w"
Content-Type: text/html
Server: Allegro-Software-RomPager/257168892

(UNKNOWN) [10.10.173.229] 66 (?) open
������Welcome to VCSCDCS2
TANDBERG Codec Release L00

(UNKNOWN) [10.10.173.229] 65 (?) open
����

Login: 

You must supply a username

Login: 

You must supply a username

Login: 
(UNKNOWN) [10.10.173.229] 64 (?) open
HTTP/1.0 404 no application for: /
Server: HttpServer

(UNKNOWN) [10.10.173.229] 63 (?) open
�00$000brkl0000000000000000000000000
(UNKNOWN) [10.10.173.229] 62 (?) open
HTTP/1.0 200 OK
