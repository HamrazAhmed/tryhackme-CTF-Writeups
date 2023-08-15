---
An Easy Boot2Root box for beginners
---

# GamingServer — Writeup

## Overview
### GamingServer — Writeup
### GamingServer — Writeup
![](https://tryhackme-images.s3.amazonaws.com/room-icons/80d16a6756c805903806f7ecbdd80f6d.jpeg)

## Privilege Escalation
Can you gain access to this gaming server built by amateurs with no experience of web development and take advantage of the deployment system.
```text

```
```text
┌──(kali㉿kali)-[~/confidential]
└─$ rustscan -a 10.10.252.17 --ulimit 5000 -b 65535 -- -A 
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
[~] Automatically increasing ulimit value to 5000.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.252.17:22
Open 10.10.252.17:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-19 13:40 EDT
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:40
Completed NSE at 13:40, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:40
Completed NSE at 13:40, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:40
Completed NSE at 13:40, 0.00s elapsed
Initiating Ping Scan at 13:40
Scanning 10.10.252.17 [2 ports]
Completed Ping Scan at 13:40, 0.26s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 13:40
Completed Parallel DNS resolution of 1 host. at 13:40, 0.02s elapsed
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 13:40
Scanning 10.10.252.17 [2 ports]
Discovered open port 22/tcp on 10.10.252.17
Discovered open port 80/tcp on 10.10.252.17
Completed Connect Scan at 13:40, 0.21s elapsed (2 total ports)
Initiating Service scan at 13:40
Scanning 2 services on 10.10.252.17
Completed Service scan at 13:40, 6.96s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.252.17.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:40
Completed NSE at 13:40, 9.72s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:40
Completed NSE at 13:40, 1.68s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:40
Completed NSE at 13:40, 0.00s elapsed
Nmap scan report for 10.10.252.17
Host is up, received syn-ack (0.25s latency).
Scanned at 2022-09-19 13:40:35 EDT for 19s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 34:0e:fe:06:12:67:3e:a4:eb:ab:7a:c4:81:6d:fe:a9 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCrmafoLXloHrZgpBrYym3Lpsxyn7RI2PmwRwBsj1OqlqiGiD4wE11NQy3KE3Pllc/C0WgLBCAAe+qHh3VqfR7d8uv1MbWx1mvmVxK8l29UH1rNT4mFPI3Xa0xqTZn4Iu5RwXXuM4H9OzDglZas6RIm6Gv+sbD2zPdtvo9zDNj0BJClxxB/SugJFMJ+nYfYHXjQFq+p1xayfo3YIW8tUIXpcEQ2kp74buDmYcsxZBarAXDHNhsEHqVry9I854UWXXCdbHveoJqLV02BVOqN3VOw5e1OMTqRQuUvM5V4iKQIUptFCObpthUqv9HeC/l2EZzJENh+PmaRu14izwhK0mxL
|   256 49:61:1e:f4:52:6e:7b:29:98:db:30:2d:16:ed:f4:8b (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEaXrFDvKLfEOlKLu6Y8XLGdBuZ2h/sbRwrHtzsyudARPC9et/zwmVaAR9F/QATWM4oIDxpaLhA7yyh8S8m0UOg=
|   256 b8:60:c4:5b:b7:b2:d0:23:a0:c7:56:59:5c:63:1e:c4 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOLrnjg+MVLy+IxVoSmOkAtdmtSWG0JzsWVDV2XvNwrY
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-title: House of danak
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:40
Completed NSE at 13:40, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:40
Completed NSE at 13:40, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:40
Completed NSE at 13:40, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.50 seconds

some manifesto in ip/uploads/manifesto.txt

			 The Hacker Manifesto

			          by
			    +++The Mentor+++
			Written January 8, 1986

Another one got caught today, it's all over the papers. "Teenager Arrested in Computer Crime 
Scandal", "Hacker Arrested after Bank Tampering"...

Damn kids. They're all alike.

But did you, in your three-piece psychology and 1950's technobrain, ever take a look behind 
the eyes of the hacker? Did you ever wonder what made him tick, what forces shaped him, 
what may have molded him?

I am a hacker, enter my world...

Mine is a world that begins with school... I'm smarter than most of the other kids, this crap 
they teach us bores me...

Damn underachiever. They're all alike.

I'm in junior high or high school. I've listened to teachers explain for the fifteenth time 
how to reduce a fraction. I understand it. "No, Ms. Smith, I didn't show my work. I did it 
in my head..."

Damn kid. Probably copied it. They're all alike.

I made a discovery today. I found a computer. Wait a second, this is cool. It does what I 
want it to. If it makes a mistake, it's because I screwed it up. Not because it doesn't like 
me... Or feels threatened by me.. Or thinks I'm a smart ass.. Or doesn't like teaching and 
shouldn't be here...

Damn kid. All he does is play games. They're all alike.

And then it happened... a door opened to a world... rushing through the phone line like heroin
through an addict's veins, an electronic pulse is sent out, a refuge from the day-to-day 
incompetencies is sought... a board is found. "This is it... this is where I belong..." I know
everyone here... even if I've never met them, never talked to them, may never hear from them 
again... I know you all...

Damn kid. Tying up the phone line again. They're all alike...

You bet your ass we're all alike... we've been spoon-fed baby food at school when we hungered 
for steak... the bits of meat that you did let slip through were pre-chewed and tasteless. 
We've been dominated by sadists, or ignored by the apathetic. The few that had something to 
teach found us willing pupils, but those few are like drops of water in the desert.

This is our world now... the world of the electron and the switch, the beauty of the baud. We 
make use of a service already existing without paying for what could be dirt-cheap if it 
wasn't run by profiteering gluttons, and you call us criminals. We explore... and you call us 
criminals. We seek after knowledge... and you call us criminals. We exist without skin color, 
without nationality, without religious bias... and you call us criminals. You build atomic 
bombs, you wage wars, you murder, cheat, and lie to us and try to make us believe it's for 
our own good, yet we're the criminals.

Yes, I am a criminal. My crime is that of curiosity. My crime is that of judging people by 
what they say and think, not what they look like. My crime is that of outsmarting you, 
something that you will never forgive me for.

I am a hacker, and this is my manifesto. You may stop this individual, but you can't stop us 
all... after all, we're all alike.

or just check /robots.txt tehn find a dict.list and manifesto

with feroxbuster found /secret then ssh key
```
```text
┌──(kali㉿kali)-[~/confidential/gamingserver]
└─$ feroxbuster --url http://10.10.252.17 -w /usr/share/wordlists/dirb/common.txt -t 60 -C 404,403

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.7.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.252.17
 🚀  Threads               │ 60
 📖  Wordlist              │ /usr/share/wordlists/dirb/common.txt
 💢  Status Code Filters   │ [404, 403]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.7.0
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
200      GET       77l      316w     2762c http://10.10.252.17/
200      GET       77l      316w     2762c http://10.10.252.17/index.html
200      GET        3l        5w       33c http://10.10.252.17/robots.txt
301      GET        9l       28w      313c http://10.10.252.17/secret => http://10.10.252.17/secret/

-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,82823EE792E75948EE2DE731AF1A0547

T7+F+3ilm5FcFZx24mnrugMY455vI461ziMb4NYk9YJV5uwcrx4QflP2Q2Vk8phx
H4P+PLb79nCc0SrBOPBlB0V3pjLJbf2hKbZazFLtq4FjZq66aLLIr2dRw74MzHSM
FznFI7jsxYFwPUqZtkz5sTcX1afch+IU5/Id4zTTsCO8qqs6qv5QkMXVGs77F2kS
Lafx0mJdcuu/5aR3NjNVtluKZyiXInskXiC01+Ynhkqjl4Iy7fEzn2qZnKKPVPv8
9zlECjERSysbUKYccnFknB1DwuJExD/erGRiLBYOGuMatc+EoagKkGpSZm4FtcIO
IrwxeyChI32vJs9W93PUqHMgCJGXEpY7/INMUQahDf3wnlVhBC10UWH9piIOupNN
SkjSbrIxOgWJhIcpE9BLVUE4ndAMi3t05MY1U0ko7/vvhzndeZcWhVJ3SdcIAx4g
/5D/YqcLtt/tKbLyuyggk23NzuspnbUwZWoo5fvg+jEgRud90s4dDWMEURGdB2Wt
w7uYJFhjijw8tw8WwaPHHQeYtHgrtwhmC/gLj1gxAq532QAgmXGoazXd3IeFRtGB
6+HLDl8VRDz1/4iZhafDC2gihKeWOjmLh83QqKwa4s1XIB6BKPZS/OgyM4RMnN3u
Zmv1rDPL+0yzt6A5BHENXfkNfFWRWQxvKtiGlSLmywPP5OHnv0mzb16QG0Es1FPl
xhVyHt/WKlaVZfTdrJneTn8Uu3vZ82MFf+evbdMPZMx9Xc3Ix7/hFeIxCdoMN4i6
8BoZFQBcoJaOufnLkTC0hHxN7T/t/QvcaIsWSFWdgwwnYFaJncHeEj7d1hnmsAii
b79Dfy384/lnjZMtX1NXIEghzQj5ga8TFnHe8umDNx5Cq5GpYN1BUtfWFYqtkGcn
vzLSJM07RAgqA+SPAY8lCnXe8gN+Nv/9+/+/uiefeFtOmrpDU2kRfr9JhZYx9TkL
wTqOP0XWjqufWNEIXXIpwXFctpZaEQcC40LpbBGTDiVWTQyx8AuI6YOfIt+k64fG
rtfjWPVv3yGOJmiqQOa8/pDGgtNPgnJmFFrBy2d37KzSoNpTlXmeT/drkeTaP6YW
RTz8Ieg+fmVtsgQelZQ44mhy0vE48o92Kxj3uAB6jZp8jxgACpcNBt3isg7H/dq6
oYiTtCJrL3IctTrEuBW8gE37UbSRqTuj9Foy+ynGmNPx5HQeC5aO/GoeSH0FelTk
cQKiDDxHq7mLMJZJO0oqdJfs6Jt/JO4gzdBh3Jt0gBoKnXMVY7P5u8da/4sV+kJE
99x7Dh8YXnj1As2gY+MMQHVuvCpnwRR7XLmK8Fj3TZU+WHK5P6W5fLK7u3MVt1eq
Ezf26lghbnEUn17KKu+VQ6EdIPL150HSks5V+2fC8JTQ1fl3rI9vowPPuC8aNj+Q
Qu5m65A5Urmr8Y01/Wjqn2wC7upxzt6hNBIMbcNrndZkg80feKZ8RD7wE7Exll2h
v3SBMMCT5ZrBFq54ia0ohThQ8hklPqYhdSebkQtU5HPYh+EL/vU1L9PfGv0zipst
gbLFOSPp+GmklnRpihaXaGYXsoKfXvAxGCVIhbaWLAp5AybIiXHyBWsbhbSRMK+P
-----END RSA PRIVATE KEY-----

in source code <!-- john, please add some actual content to the site! lorem ipsum is horrible to look at. -->

so ssh john username
```
```text
┌──(kali㉿kali)-[~/confidential/gamingserver]
└─$ ls
dict.lst
```
```text
┌──(kali㉿kali)-[~/confidential/gamingserver]
└─$ nano secretKey
```
```text
┌──(kali㉿kali)-[~/confidential/gamingserver]
└─$ ls
dict.lst  secretKey
```
```text
┌──(kali㉿kali)-[~/confidential/gamingserver]
└─$ chmod 400 secretKey      

need a secretkey
```
```text
┌──(kali㉿kali)-[~/confidential/gamingserver]
└─$ ssh -i secretKey john@10.10.252.17  
The authenticity of host '10.10.252.17 (10.10.252.17)' can't be established.
ED25519 key fingerprint is SHA256:3Kz4ZAujxMQpTzzS0yLL9dLKLGmA1HJDOLAQWfmcabo.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
