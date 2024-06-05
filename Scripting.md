---
Learn basic scripting by solving some challenges!
---

# Scripting — Writeup

## Overview
### Scripting — Writeup
### Scripting — Writeup
![](https://miro.medium.com/max/2560/1*enCF61GFzLovMNXzAJmVNQ.png)
![](https://tryhackme-images.s3.amazonaws.com/room-icons/b404cfcdf14054b6dabf2a94a48f0ba0.png)
### [Easy] Base64
This file has been base64 encoded 50 times - write a script to retrieve the flag. Here is the general process to do this:
read input from the file
use function to decode the file
do process in a loop
Try do this in both Bash and Python!
```text
download the task 30 mb b64 encoded 50 times

with cyberchef takes a lot time ... so create a python script
```
```text
┌──(kali㉿kali)-[~/scripting]
└─$ nano b64.py
```
```text
┌──(kali㉿kali)-[~/scripting]
└─$ cat b64.py
import base64

#Open file
with open('b64.txt') as f:
        msg = f.read()

#Decode 50 times
for _ in range(50):
        msg = base64.b64decode(msg)

print(f"Th flag is: {msg.decode('utf8')}")
```
```text
┌──(kali㉿kali)-[~/scripting]
└─$ python3 b64.py
Th flag is: HackBack2019=
```
![[Pasted image 20221026121914.png]]
What is the final string?
*HackBack2019=*
### [Medium] Gotta Catch em All
You need to write a script that connects to this webserver on the correct port, do an operation on a number and then move onto the next port. Start your original number at 0.
The format is: operation, number, next port.
For example the website might display, add 900 3212 which would be: add 900 and move onto port 3212.
Then if it was minus 212 3499, you'd minus 212 (from the previous number which was 900) and move onto the next port 3499
Do this until you the page response is STOP (or you hit port 9765).
Each port is also only live for 4 seconds. After that it goes to the next port. You might have to wait until port 1337 becomes live again...
Go to: http://<machines_ip>:3010 to start...
General Approach(it's best to do this using the sockets library in Python):
Create a socket in Python using the sockets library https://docs.python.org/3/howto/sockets.html
Connect to the port
Send an operation
View response and continue
![[Pasted image 20221026123721.png]]

## Enumeration
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.174.84 --ulimit 5500 -b 65535 -- -A
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.174.84:22
Open 10.10.174.84:3010
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.93 ( https://nmap.org ) at 2022-10-26 13:35 EDT
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:35
Completed NSE at 13:35, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:35
Completed NSE at 13:35, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:35
Completed NSE at 13:35, 0.00s elapsed
Initiating Ping Scan at 13:35
Scanning 10.10.174.84 [2 ports]
Completed Ping Scan at 13:35, 0.31s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 13:35
Completed Parallel DNS resolution of 1 host. at 13:35, 0.02s elapsed
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 13:35
Scanning 10.10.174.84 [2 ports]
Discovered open port 22/tcp on 10.10.174.84
Discovered open port 3010/tcp on 10.10.174.84
Completed Connect Scan at 13:35, 0.31s elapsed (2 total ports)
Initiating Service scan at 13:35
Scanning 2 services on 10.10.174.84
Completed Service scan at 13:35, 7.58s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.174.84.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:35
Completed NSE at 13:35, 9.37s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:35
Completed NSE at 13:35, 1.41s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:35
Completed NSE at 13:35, 0.00s elapsed
Nmap scan report for 10.10.174.84
Host is up, received conn-refused (0.31s latency).
Scanned at 2022-10-26 13:35:21 EDT for 19s

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c8cc25b7cbd585c3d8b1a2b81bf99ee3 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCXsmODtOWVYR+ZZRJmgrnoJY4Gvlvbrj+g+rpi1n9J9XACL1Wp10tdAc+vtcLEBQ+Oc7IUs9CUnL/NY/q2rATFxhZ0MBy+AmZ29Exf9ywCdSHX41NyLQ3FbNOjS3P0gyyNhsrfK8YbXKBMr8xqjeZYM9Ypn0NT3WJq+QmzlF2lTnMVqatBHQTbCAGmMo5pd91wekaE5oqBppOpUKoVCPsPUatGKg4dOVW3dOrkn2hwWwCVkmFw3+RQzyVvWKMMgNaNOH66h1NDAB6INOvjYvW+brxxrGGHns2WeZpFU9cxQVhF0l1R0tWNCJnkSTvR1Qi6aYZQMrdPcHiE92C+d4KV
|   256 d83c67cd1d400835ca018091ec37515c (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBMzxLhIw6LzXpIjMMlPy6RMV72TqZgCwHgEW0xCAx5eLKJhyg9QSkJdDco4sd0hw/PYgCN50HmylNrCkT1cah3g=
|   256 8a89d6a62f3bf0628814a05cd16f5358 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFGEKu05jt0N6KtTD9SHIrBmdeNJv2wHYWGu09PqYnNH
3010/tcp open  http    syn-ack Werkzeug httpd 0.14.1 (Python 3.5.2)
|_http-server-header: Werkzeug/0.14.1 Python/3.5.2
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:35
Completed NSE at 13:35, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:35
Completed NSE at 13:35, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:35
Completed NSE at 13:35, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.30 seconds

go to ip:3010 to see currently port
```
```text
┌──(kali㉿kali)-[~/scripting]
└─$ cat webClient.py
import socket
import time
import re
import sys

def Main():
        serverIP = sys.argv[1] #Get ip from user input
        serverPort = 1337
        oldNum = 0 # Start as 0 per instructions

        while serverPort != 9765:
                try: #try until port 1337 is available
                        if serverPort == 1337:
                                print(f"Connecting to {serverIP} waiting for Port {serverPort} to become available...")

                        #Creating socket and connect to server
                        s = socket.socket()
                        s.connect((serverIP,serverPort))

                        #Send get request to server
                        gRequest = f"GET / HTTP/1.0\r\nHost: {serverIP}:{serverPort}\r\n\r\n"

                        s.send(gRequest.encode('utf8'))

                        #Retrieve data from get request
                        while True:
                                response = s.recv(1024)
                                if (len(response) < 1):
                                        break
                                data = response.decode("utf8")

                        #Format and assign the data into usable vars
                        op, newNum, nextPort = assignData(data)
                        #perform given calcs
                        oldNum = doMath(op, oldNum, newNum)
                        #Display output and move on
                        print(f"Current number is {oldNum}, moving onto port {nextPort}")
                        serverPort = nextPort

                        s.close()

                except:
                        s.close()
                        time.sleep(3) #Ports update every 4 sec
                        pass

        print(f"The final answer is {round(oldNum,2)}")

def doMath(op, oldNum, newNum):
        if op == 'add':
                return oldNum + newNum
        elif op == 'minus':
                return oldNum - newNum
        elif op == 'divide':
                return oldNum / newNum
        elif op == 'multiply':
                return oldNum * newNum
        else:
                return None

def assignData(data):
        dataArr = re.split(' |\*|\n' , data) #Split data with multi delim
        dataArr = list(filter(None, dataArr)) #Filter null strings
        #Assign the last 3 values of data
        op = dataArr[-3]
        newNum = float(dataArr[-2])
        nextPort = int(dataArr[-1])

        return op, newNum, nextPort

if __name__ == '__main__':
        Main()
```
```text
┌──(kali㉿kali)-[~/scripting]
└─$ python3 webClient.py 10.10.174.84
Connecting to 10.10.174.84 waiting for Port 1337 to become available...
Connecting to 10.10.174.84 waiting for Port 1337 to become available...
Connecting to 10.10.174.84 waiting for Port 1337 to become available...
Connecting to 10.10.174.84 waiting for Port 1337 to become available...
Connecting to 10.10.174.84 waiting for Port 1337 to become available...
Connecting to 10.10.174.84 waiting for Port 1337 to become available...
Connecting to 10.10.174.84 waiting for Port 1337 to become available...
Connecting to 10.10.174.84 waiting for Port 1337 to become available...
Connecting to 10.10.174.84 waiting for Port 1337 to become available...
Connecting to 10.10.174.84 waiting for Port 1337 to become available...
Connecting to 10.10.174.84 waiting for Port 1337 to become available...
Connecting to 10.10.174.84 waiting for Port 1337 to become available...
Connecting to 10.10.174.84 waiting for Port 1337 to become available...
Connecting to 10.10.174.84 waiting for Port 1337 to become available...
Connecting to 10.10.174.84 waiting for Port 1337 to become available...
Connecting to 10.10.174.84 waiting for Port 1337 to become available...
