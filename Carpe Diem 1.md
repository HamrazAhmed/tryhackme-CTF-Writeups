# Carpe Diem 1 — Writeup

## Overview
### Carpe Diem 1 — Writeup
### Carpe Diem 1 — Writeup
----
Recover your clients encrypted files before the ransomware timer runs out!
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/7d855efe4d13839e74e0491b784dc952.jpeg)
Start Machine
One of your clients has been hacked by the Carpe Diem cyber gang and all their important files have been encrypted. They have hired you to help them recover an important file that they need to restore their backups. They have contacted the carpe diem cybergang and paid a ransom but have not heard anything back.
The countdown timer is ticking since they visited and they are now running out of time to recover their data before the keys are deleted on the server. Can you retrieve the keys and help your client restore their data before time runs out?
The file is available to download on the machine: `/downloads/Database.carp   `
(The downloads-section is not a part of the challenge)
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads/sudo_inject]
└─$ rustscan -a 10.10.77.135 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.77.135:80
Open 10.10.77.135:111
Open 10.10.77.135:40346
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
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.77.135 [3 ports]
Discovered open port 111/tcp on 10.10.77.135
Discovered open port 40346/tcp on 10.10.77.135
Discovered open port 80/tcp on 10.10.77.135
Completed Connect Scan (3 total ports)
Initiating Service scan
Scanning 3 services on 10.10.77.135
Completed Service scan (3 services on 1 host)
NSE: Script scanning 10.10.77.135.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.77.135
Host is up, received user-set (0.18s latency).

PORT      STATE SERVICE REASON  VERSION
80/tcp    open  http    syn-ack nginx 1.6.2
|_http-server-header: nginx/1.6.2
|_http-title: Home
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
111/tcp   open  rpcbind syn-ack 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          36716/tcp6  status
|   100024  1          40346/tcp   status
|   100024  1          59030/udp   status
|_  100024  1          60395/udp6  status
40346/tcp open  status  syn-ack 1 (RPC #100024)

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
Nmap done: 1 IP address (1 host up) scanned in 23.06 seconds

Carpe Diem
All your data are belong to us!

   uu$:$:$:$:$:$uu
    uu$$$$$$$$$$$$$$$$$uu
   u$$$$$$$$$$$$$$$$$$$$$u
   u$$$$$$$$$$$$$$$$$$$$$$$u
   u$$$$$$$$$$$$$$$$$$$$$$$$$u
  u$$$$$$$$$$$$$$$$$$$$$$$$$u
  u$$$$$$*   *$$$*   *$$$$$$u
  $$$$*      u$u       $$$$*
  $$$u       u$u       u$$$
  $$$u      u$$$u      u$$$
  *$$$$uu$$$   $$$uu$$$$*
  *$$$$$$$*   *$$$$$$$*
   u$$$$$$$u$$$$$$$u
   u$*$*$*$*$*$*$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$u$u$u$u$u$$       u$$$$
  $$$$$uu      *$$$$$$$$$*     uu$$$$$$
u$$$$$$$$$$$      *****    uuuu$$$$$$$$$
$$$$***$$$$$$$$$$uuu   uu$$$$$$$$$***$$$*
 ***      **$$$$$$$$$$$uu **$***
          uuuu **$$$$$$$$$$uuu
 u$$$uuu$$$$$$$$$uu **$$$$$$$$$$$uuu$$$
 $$$$$$$$$$****           **$$$$$$$$$$$*
   *$$$$$*                      **$$$$** 

Your key will be deleted:
Wed Jul 12 2023 01:01:30 GMT+0000
0d 11h 58m 32s
BTC:	bc1q989cy4zp8x9xpxgwpznsxx44u0cxhyjjyp78hj

Proof:	bc1q989cy4zp8x9xpxgwpznsxx44u0cxhyjjyp78hj	

Hey! 

stupid is as stupid does...

OPTIONS /proof/ HTTP/1.1

Host: c4rp3d13m.net

┌──(witty㉿kali)-[~/Downloads/seasurfer]
└─$ tac /etc/hosts                                                  
10.10.77.135 c4rp3d13m.net

http://c4rp3d13m.net/downloads/

┌──(witty㉿kali)-[~/Downloads]
└─$ file decrypt_linux_amd64 
decrypt_linux_amd64: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, Go BuildID=Q-qwIhmYLL9O7nxtkSFl/ALutoQld-L8sj0x8TtDr/APPpThdSM2NmXJG6XglT/CwEqr2HOjAvrporc6crE, not stripped

</pre><h4></h4><h2>Your key will be deleted:</h2><h3>Wed Jul 12 2023 01:01:30 GMT+0000</h3><div id="counter"></div><script>function aaa(wallet) {
  var wallet = wallet;
  if (wallet.trim() === 'bc1q989cy4zp8x9xpxgwpznsxx44u0cxhyjjyp78hj'){
    alert('Hey! \n\nstupid is as stupid does...');
    return;
  }

var re = new RegExp("^([a-z0-9]{42,42})$");
if (re.test(wallet.trim())) {
  var http = new XMLHttpRequest();
  var url = 'http://c4rp3d13m.net/proof/';
  http.open('POST', url, true);
  http.setRequestHeader('Content-type', 'application/json');
  var d = '{"size":42,"proof":"'+wallet+'"}';
  http.onreadystatechange = function() {
  if(http.readyState == 4 && http.status == 200) {
    //alert(http.responseText);
    }
    }
      http.send(d);
    } else {
    alert('Invalid wallet!');
    }
    }
</script><script>function clippy() {
var copyText = document.getElementById("pay");
copyText.select();
copyText.setSelectionRange(0, 99999)
document.execCommand("copy");
alert("Copied: " + copyText.value);
}</script><script>// Set the date we're counting down to
var countdown = document.cookie
var countdown = countdown.replace(/%3A/g, ":");
var countdown = countdown.replace("countdown=", "");

var countDownDate = new Date(countdown);
countDownDate.setHours(countDownDate.getHours() + 8);
countDownDate = new Date(countDownDate).getTime();

// Update the count down every 1 second
var x = setInterval(function() {

 // Get today's date and time
var now = new Date().getTime();

// Find the distance between now and the count down date
var distance = countDownDate - now;

// Time calculations for days, hours, minutes and seconds
var days = Math.floor(distance / (1000 * 60 * 60 * 24));
var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
var seconds = Math.floor((distance % (1000 * 60)) / 1000);

// Output the result in an element with id="demo"
document.getElementById("counter").innerHTML = days + "d " + hours + "h "+ minutes + "m " + seconds + "s ";

// If the count down is over, write some text
if (distance < 0) {
clearInterval(x);
document.getElementById("counter").innerHTML = "KEY DELETED. YOU SHOULD HAVE PAYED!";
}
}, 1000);
</script>

POST /proof/ HTTP/1.1

Host: c4rp3d13m.net

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Connection: close

Cookie: session=MTAuOC4xOS4xMDM%3D; countdown=2023-07-11T17%3A01%3A30.809939

Upgrade-Insecure-Requests: 1

Content-Type: application/json

Content-Length: 64

{"size":42,"proof":"bc1q989cy4zp8x9xpxgwpznsxx44u0cxhyjjyp78hj"}

HTTP/1.1 200 OK

Server: nginx/1.6.2

Date: Tue, 11 Jul 2023 17:15:49 GMT

Content-Type: text/html; charset=utf-8

Content-Length: 10
