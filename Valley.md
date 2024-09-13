# Valley — Writeup

## Overview
### Valley — Writeup
### Valley — Writeup
----
Can you find your way into the Valley?
----
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/2700326f6bf2127c414a0fa4582496cd.png)
Start Machine
Boot the box and find a way in to escalate all the way to root!
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.97.111 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.97.111:22
Open 10.10.97.111:80
Open 10.10.97.111:37370
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
Scanning 10.10.97.111 [3 ports]
Discovered open port 80/tcp on 10.10.97.111
Discovered open port 22/tcp on 10.10.97.111
Discovered open port 37370/tcp on 10.10.97.111
Completed Connect Scan (3 total ports)
Initiating Service scan
Scanning 3 services on 10.10.97.111
Completed Service scan (3 services on 1 host)
NSE: Script scanning 10.10.97.111.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.97.111
Host is up, received user-set (0.18s latency).

PORT      STATE SERVICE REASON  VERSION
22/tcp    open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 c2842ac1225a10f16616dda0f6046295 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCf7Zvn7fOyAWUwEI2aH/k8AyPehxzzuNC1v4AAlhDa4Off4085gRIH/EXpjOoZSBvo8magsCH32JaKMMc59FSK4canP2I0VrXwkEX0F8PjA1TV4qgqXJI0zNVwFrfBORDdlCPNYiqRNFp1vaxTqLOFuHt5r34134yRwczxTsD4Uf9Z6c7Yzr0GV6NL3baGHDeSZ/msTiFKFzLTTKbFkbU4SQYc7jIWjl0ylQ6qtWivBiavEWTwkHHKWGg9WEdFpU2zjeYTrDNnaEfouD67dXznI+FiiTiFf4KC9/1C+msppC0o77nxTGI0352wtBV9KjTU/Aja+zSTMDxoGVvo/BabczvRCTwhXxzVpWNe3YTGeoNESyUGLKA6kUBfFNICrJD2JR7pXYKuZVwpJUUCpy5n6MetnonUo0SoMg/fzqMWw2nCZOpKzVo9OdD8R/ZTnX/iQKGNNvgD7RkbxxFK5OA9TlvfvuRUQQaQP7+UctsaqG2F9gUfWorSdizFwfdKvRU=
|   256 429e2ff63e5adb51996271c48c223ebb (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNIiJc4hdfcu/HtdZN1fyz/hU1SgSas1Lk/ncNc9UkfSDG2SQziJ/5SEj1AQhK0T4NdVeaMSDEunQnrmD1tJ9hg=
|   256 2ea0a56cd983e0016cb98a609b638672 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEZhkboYdSkdR3n1G4sQtN4uO3hy89JxYkizKi6Sd/Ky
80/tcp    open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Site doesn't have a title (text/html).
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET POST
|_http-server-header: Apache/2.4.41 (Ubuntu)
37370/tcp open  ftp     syn-ack vsftpd 3.0.3
Service Info: OSs: Linux, Unix; CPE: cpe:/o:linux:linux_kernel

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
Nmap done: 1 IP address (1 host up) scanned in 14.36 seconds

http://10.10.97.111/static/1

http://10.10.97.111/static/00

dev notes from valleyDev:
-add wedding photo examples
-redo the editing on #4
-remove /dev1243224123123
-check for SIEM alerts

http://10.10.97.111/dev1243224123123/

view-source:http://10.10.97.111/dev1243224123123/dev.js

if (username === "siemDev" && password === "california") {
        window.location.href = "/dev1243224123123/devNotes37370.txt";

http://10.10.97.111/dev1243224123123/devNotes37370.txt

dev notes for ftp server:
-stop reusing credentials
-check for any vulnerabilies
-stay up to date on patching
-change ftp port to normal port

┌──(witty㉿kali)-[~/Downloads]
└─$ ftp 10.10.97.111 37370
Connected to 10.10.97.111.
220 (vsFTPd 3.0.3)
Name (10.10.97.111:witty): siemDev
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||57075|)
150 Here comes the directory listing.
-rw-rw-r--    1 1000     1000         7272 Mar 06 13:55 siemFTP.pcapng
-rw-rw-r--    1 1000     1000      1978716 Mar 06 13:55 siemHTTP1.pcapng
-rw-rw-r--    1 1000     1000      1972448 Mar 06 14:06 siemHTTP2.pcapng
226 Directory send OK.
ftp> mget *
mget siemFTP.pcapng [anpqy?]? y
229 Entering Extended Passive Mode (|||46138|)
150 Opening BINARY mode data connection for siemFTP.pcapng (7272 bytes).
100% |*****************************************************************************|  7272       69.92 KiB/s    00:00 ETA
226 Transfer complete.
7272 bytes received in 00:00 (24.70 KiB/s)
mget siemHTTP1.pcapng [anpqy?]? y
229 Entering Extended Passive Mode (|||13176|)
150 Opening BINARY mode data connection for siemHTTP1.pcapng (1978716 bytes).
100% |*****************************************************************************|  1932 KiB  493.07 KiB/s    00:00 ETA
226 Transfer complete.
1978716 bytes received in 00:04 (469.60 KiB/s)
mget siemHTTP2.pcapng [anpqy?]? y
229 Entering Extended Passive Mode (|||61333|)
150 Opening BINARY mode data connection for siemHTTP2.pcapng (1972448 bytes).
100% |*****************************************************************************|  1926 KiB  499.73 KiB/s    00:00 ETA
226 Transfer complete.
1972448 bytes received in 00:04 (474.83 KiB/s)
ftp> exit
221 Goodbye.

┌──(witty㉿kali)-[~/Downloads]
└─$ wireshark siemFTP.pcapng 

┌──(witty㉿kali)-[~/Downloads]
└─$ wireshark siemHTTP2.pcapng 

follow http stream

POST /index.html HTTP/1.1
Host: 192.168.111.136
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 42
Origin: http://192.168.111.136
Connection: keep-alive
Referer: http://192.168.111.136/index.html
Upgrade-Insecure-Requests: 1

uname=valleyDev&psw=ph0t0s1234&remember=onHTTP/1.1 200 OK

valleyDev:ph0t0s1234

┌──(witty㉿kali)-[~/Downloads]
└─$ ssh valleyDev@10.10.97.111                                                                    
The authenticity of host '10.10.97.111 (10.10.97.111)' can't be established.
ED25519 key fingerprint is SHA256:cssZyBk7QBpWU8cMEAJTKWPfN5T2yIZbqgKbnrNEols.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.97.111' (ED25519) to the list of known hosts.
valleyDev@10.10.97.111's password: 
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.4.0-139-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

 * Introducing Expanded Security Maintenance for Applications.
   Receive updates to over 25,000 software packages with your
   Ubuntu Pro subscription. Free for personal use.

     https://ubuntu.com/pro
valleyDev@valley:~$ whoami
