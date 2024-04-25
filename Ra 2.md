---
Just when they thought their hashes were safe... Ra 2 - The sequel!
---

# Ra 2 — Writeup

## Overview
### Ra 2 — Writeup
### Ra 2 — Writeup
**Story**
WindCorp recently had a security-breach. Since then they have hardened their infrastructure, learning from their mistakes. But maybe not enough? You have managed to enter their local network...
Happy Hacking!
Created by @4nqr34z and @theart42
_(Give it at least 5 minutes to boot)_
```text
┌──(kali㉿kali)-[~/threader3000]
└─$ git clone https://github.com/dievus/threader3000.git
```

## Enumeration
```text
┌──(kali㉿kali)-[~/threader3000]
└─$ python3 threader3000.py               
------------------------------------------------------------
        Threader 3000 - Multi-threaded Port Scanner          
                       Version 1.0.7                    
                   A project by The Mayor               
------------------------------------------------------------
Enter your target IP address or URL here: 10.10.219.166
------------------------------------------------------------
Scanning target 10.10.219.166
Time started: 2022-12-22 13:38:53.039666
------------------------------------------------------------
Port 53 is open
Port 88 is open
Port 139 is open
Port 135 is open
Port 80 is open
Port 389 is open
Port 445 is open
Port 443 is open
Port 464 is open
Port 593 is open
Port 636 is open
Port 2179 is open
Port 3268 is open
Port 3269 is open
Port 3389 is open
Port 5229 is open
Port 5223 is open
Port 5222 is open
Port 5262 is open
Port 5263 is open
Port 5270 is open
Port 5269 is open
Port 5275 is open
Port 5276 is open
Port 7070 is open
Port 7443 is open
Port 7777 is open
Port 9091 is open
Port 9090 is open
Port 9389 is open
Port 49667 is open
Port 49668 is open
Port 49669 is open
Port 49670 is open
Port 49672 is open
Port 49689 is open
Port 49703 is open
Port scan completed in 0:01:47.086578
------------------------------------------------------------
Threader3000 recommends the following Nmap scan:
************************************************************
nmap -p53,88,139,135,80,389,445,443,464,593,636,2179,3268,3269,3389,5229,5223,5222,5262,5263,5270,5269,5275,5276,7070,7443,7777,9091,9090,9389,49667,49668,49669,49670,49672,49689,49703 -sV -sC -T4 -Pn -oA 10.10.219.166 10.10.219.166
************************************************************
Would you like to run Nmap or quit to terminal?
------------------------------------------------------------
1 = Run suggested Nmap scan
2 = Run another Threader3000 scan
3 = Exit to terminal
```
```text
┌──(kali㉿kali)-[~/threader3000]
└─$ rustscan -a 10.10.219.166 --ulimit 5500 -b 65535 -- -A
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.219.166:53
Open 10.10.219.166:80
Open 10.10.219.166:88
Open 10.10.219.166:135
Open 10.10.219.166:139
Open 10.10.219.166:389
Open 10.10.219.166:445
Open 10.10.219.166:464
Open 10.10.219.166:443
Open 10.10.219.166:593
Open 10.10.219.166:636
Open 10.10.219.166:2179
Open 10.10.219.166:3268
Open 10.10.219.166:3269
Open 10.10.219.166:3389
Open 10.10.219.166:5222
Open 10.10.219.166:5223
Open 10.10.219.166:5229
Open 10.10.219.166:5262
Open 10.10.219.166:5263
Open 10.10.219.166:5269
Open 10.10.219.166:5270
Open 10.10.219.166:5276
Open 10.10.219.166:5275
Open 10.10.219.166:7070
Open 10.10.219.166:7443
Open 10.10.219.166:7777
Open 10.10.219.166:9090
Open 10.10.219.166:9091
Open 10.10.219.166:9389
Open 10.10.219.166:49667
Open 10.10.219.166:49668
Open 10.10.219.166:49669
Open 10.10.219.166:49670
Open 10.10.219.166:49672
Open 10.10.219.166:49689
Open 10.10.219.166:49703
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-22 14:29 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:29
Completed NSE at 14:29, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:29
Completed NSE at 14:29, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:29
Completed NSE at 14:29, 0.00s elapsed
Initiating Ping Scan at 14:29
Scanning 10.10.219.166 [2 ports]
Completed Ping Scan at 14:29, 0.21s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 14:29
Completed Parallel DNS resolution of 1 host. at 14:29, 0.02s elapsed
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 14:29
Scanning 10.10.219.166 [37 ports]
Discovered open port 53/tcp on 10.10.219.166
Discovered open port 139/tcp on 10.10.219.166
Discovered open port 445/tcp on 10.10.219.166
Discovered open port 135/tcp on 10.10.219.166
Discovered open port 80/tcp on 10.10.219.166
Discovered open port 3389/tcp on 10.10.219.166
Discovered open port 443/tcp on 10.10.219.166
Discovered open port 5269/tcp on 10.10.219.166
Discovered open port 49667/tcp on 10.10.219.166
Discovered open port 5276/tcp on 10.10.219.166
Discovered open port 7777/tcp on 10.10.219.166
Discovered open port 593/tcp on 10.10.219.166
Discovered open port 9091/tcp on 10.10.219.166
Discovered open port 5270/tcp on 10.10.219.166
Discovered open port 5263/tcp on 10.10.219.166
Discovered open port 88/tcp on 10.10.219.166
Discovered open port 9389/tcp on 10.10.219.166
Discovered open port 7443/tcp on 10.10.219.166
Discovered open port 389/tcp on 10.10.219.166
Discovered open port 3269/tcp on 10.10.219.166
Discovered open port 49703/tcp on 10.10.219.166
Discovered open port 5275/tcp on 10.10.219.166
Discovered open port 49670/tcp on 10.10.219.166
Discovered open port 9090/tcp on 10.10.219.166
Discovered open port 5222/tcp on 10.10.219.166
Discovered open port 464/tcp on 10.10.219.166
Discovered open port 49669/tcp on 10.10.219.166
Discovered open port 49672/tcp on 10.10.219.166
Discovered open port 3268/tcp on 10.10.219.166
Discovered open port 49668/tcp on 10.10.219.166
Discovered open port 7070/tcp on 10.10.219.166
Discovered open port 5223/tcp on 10.10.219.166
Discovered open port 636/tcp on 10.10.219.166
Discovered open port 5262/tcp on 10.10.219.166
Discovered open port 2179/tcp on 10.10.219.166
Discovered open port 49689/tcp on 10.10.219.166
Discovered open port 5229/tcp on 10.10.219.166
Completed Connect Scan at 14:29, 0.64s elapsed (37 total ports)
Initiating Service scan at 14:29
Scanning 37 services on 10.10.219.166
Completed Service scan at 14:31, 80.58s elapsed (37 services on 1 host)
NSE: Script scanning 10.10.219.166.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:31
NSE Timing: About 99.98% done; ETC: 14:31 (0:00:00 remaining)
Completed NSE at 14:31, 40.17s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:31
Completed NSE at 14:32, 11.64s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:32
Completed NSE at 14:32, 0.01s elapsed
Nmap scan report for 10.10.219.166
Host is up, received syn-ack (0.21s latency).
Scanned at 2022-12-22 14:29:54 EST for 134s

PORT      STATE SERVICE             REASON  VERSION
53/tcp    open  domain              syn-ack Simple DNS Plus
80/tcp    open  http                syn-ack Microsoft IIS httpd 10.0
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Did not follow redirect to https://fire.windcorp.thm/
88/tcp    open  kerberos-sec        syn-ack Microsoft Windows Kerberos (server time: 2022-12-22 19:30:01Z)
135/tcp   open  msrpc               syn-ack Microsoft Windows RPC
139/tcp   open  netbios-ssn         syn-ack Microsoft Windows netbios-ssn
389/tcp   open  ldap                syn-ack Microsoft Windows Active Directory LDAP (Domain: windcorp.thm0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=fire.windcorp.thm
| Subject Alternative Name: DNS:fire.windcorp.thm, DNS:selfservice.windcorp.thm, DNS:selfservice.dev.windcorp.thm
| Issuer: commonName=fire.windcorp.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-05-29T03:31:08
| Not valid after:  2028-05-29T03:41:03
| MD5:   804bdc395ce5dd7b19a5851c01d123ad
| SHA-1: 37f4e667cef75cc447c9d20125cf2b7d20b2c1f4
| -----BEGIN CERTIFICATE-----
| MIIDajCCAlKgAwIBAgIQUI2QvXTCj7RCVdv6XlGMvjANBgkqhkiG9w0BAQsFADAc
| MRowGAYDVQQDDBFmaXJlLndpbmRjb3JwLnRobTAeFw0yMDA1MjkwMzMxMDhaFw0y
| ODA1MjkwMzQxMDNaMBwxGjAYBgNVBAMMEWZpcmUud2luZGNvcnAudGhtMIIBIjAN
| BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv900af0f6n80F0J6U9jMgcwQrozr
| kXmi02esW1XAsHpWnuuMQDIN6AtiYmDcoFEXz/NteLI7T6PusqQ6SXqLBurTnR8V
| InPD3Qea6lxOXNjuNeqqZKHhUaXiwSaqtAB+GzPkNtevw3jeEj99ST/G1qwY9Xce
| sfeqR2J4kQ+8U5yKLJDPBxOSx3+SHjKErrLTk66lrlEi4atr+P/ccXA5TBkZFkYh
| i3YdKTDnYeP2fMrqvOqpw82eniHAGJ2N8JJbNep86ps8giIRieBUUclF/WCp4c33
| p4i1ioVxJIYJj6f0tjGhy9GxB7l69OtUutcIG0/FhxL2dQ86MmnHH0dE7QIDAQAB
| o4GnMIGkMA4GA1UdDwEB/wQEAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAgYIKwYB
| BQUHAwEwVAYDVR0RBE0wS4IRZmlyZS53aW5kY29ycC50aG2CGHNlbGZzZXJ2aWNl
| LndpbmRjb3JwLnRobYIcc2VsZnNlcnZpY2UuZGV2LndpbmRjb3JwLnRobTAdBgNV
| HQ4EFgQUIZvYlCIhAOFLRutycf6U2H6LhqIwDQYJKoZIhvcNAQELBQADggEBAKVC
| ZS6HOuSODERi/glj3rPJaHCStxHPEg69txOIDaM9fX4WBfmSjn+EzlrHLdeRS22h
| nTPirvuT+5nn6xbUrq9J6RCTZJD+uFc9wZl7Viw3hJcWbsO8DTQAshuZ5YJ574pG
| HjyoVDOfYhy8/8ThvYf1H8/OaIpG4UIo0vY9qeBQBOPZdbdVjWNerkFmXVq+MMVf
| pAt+FffQE/48kTCppuSKeM5ZMgHP1/zhZqyJ3npljVDlgppjvh1loSYB+reMkhwK
| 2gpGJNwxLyFDhTMLaj0pzFL9okqs5ovEWEj8p96hEE6Xxl4ZApv6mxTs9j2oY6+P
| MTUqFyYKchFUeYlgf7k=
|_-----END CERTIFICATE-----
|_ssl-date: 2022-12-22T19:31:57+00:00; -1s from scanner time.
443/tcp   open  ssl/http            syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
| ssl-cert: Subject: commonName=fire.windcorp.thm
| Subject Alternative Name: DNS:fire.windcorp.thm, DNS:selfservice.windcorp.thm, DNS:selfservice.dev.windcorp.thm
| Issuer: commonName=fire.windcorp.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-05-29T03:31:08
| Not valid after:  2028-05-29T03:41:03
| MD5:   804bdc395ce5dd7b19a5851c01d123ad
| SHA-1: 37f4e667cef75cc447c9d20125cf2b7d20b2c1f4
| -----BEGIN CERTIFICATE-----
| MIIDajCCAlKgAwIBAgIQUI2QvXTCj7RCVdv6XlGMvjANBgkqhkiG9w0BAQsFADAc
| MRowGAYDVQQDDBFmaXJlLndpbmRjb3JwLnRobTAeFw0yMDA1MjkwMzMxMDhaFw0y
| ODA1MjkwMzQxMDNaMBwxGjAYBgNVBAMMEWZpcmUud2luZGNvcnAudGhtMIIBIjAN
| BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv900af0f6n80F0J6U9jMgcwQrozr
| kXmi02esW1XAsHpWnuuMQDIN6AtiYmDcoFEXz/NteLI7T6PusqQ6SXqLBurTnR8V
| InPD3Qea6lxOXNjuNeqqZKHhUaXiwSaqtAB+GzPkNtevw3jeEj99ST/G1qwY9Xce
| sfeqR2J4kQ+8U5yKLJDPBxOSx3+SHjKErrLTk66lrlEi4atr+P/ccXA5TBkZFkYh
| i3YdKTDnYeP2fMrqvOqpw82eniHAGJ2N8JJbNep86ps8giIRieBUUclF/WCp4c33
| p4i1ioVxJIYJj6f0tjGhy9GxB7l69OtUutcIG0/FhxL2dQ86MmnHH0dE7QIDAQAB
| o4GnMIGkMA4GA1UdDwEB/wQEAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAgYIKwYB
| BQUHAwEwVAYDVR0RBE0wS4IRZmlyZS53aW5kY29ycC50aG2CGHNlbGZzZXJ2aWNl
| LndpbmRjb3JwLnRobYIcc2VsZnNlcnZpY2UuZGV2LndpbmRjb3JwLnRobTAdBgNV
| HQ4EFgQUIZvYlCIhAOFLRutycf6U2H6LhqIwDQYJKoZIhvcNAQELBQADggEBAKVC
| ZS6HOuSODERi/glj3rPJaHCStxHPEg69txOIDaM9fX4WBfmSjn+EzlrHLdeRS22h
| nTPirvuT+5nn6xbUrq9J6RCTZJD+uFc9wZl7Viw3hJcWbsO8DTQAshuZ5YJ574pG
| HjyoVDOfYhy8/8ThvYf1H8/OaIpG4UIo0vY9qeBQBOPZdbdVjWNerkFmXVq+MMVf
| pAt+FffQE/48kTCppuSKeM5ZMgHP1/zhZqyJ3npljVDlgppjvh1loSYB+reMkhwK
| 2gpGJNwxLyFDhTMLaj0pzFL9okqs5ovEWEj8p96hEE6Xxl4ZApv6mxTs9j2oY6+P
| MTUqFyYKchFUeYlgf7k=
|_-----END CERTIFICATE-----
|_ssl-date: 2022-12-22T19:31:56+00:00; -1s from scanner time.
| tls-alpn: 
|_  http/1.1
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
445/tcp   open  microsoft-ds?       syn-ack
464/tcp   open  kpasswd5?           syn-ack
593/tcp   open  ncacn_http          syn-ack Microsoft Windows RPC over HTTP 1.0
636/tcp   open  ssl/ldap            syn-ack
| ssl-cert: Subject: commonName=fire.windcorp.thm
| Subject Alternative Name: DNS:fire.windcorp.thm, DNS:selfservice.windcorp.thm, DNS:selfservice.dev.windcorp.thm
| Issuer: commonName=fire.windcorp.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-05-29T03:31:08
| Not valid after:  2028-05-29T03:41:03
| MD5:   804bdc395ce5dd7b19a5851c01d123ad
| SHA-1: 37f4e667cef75cc447c9d20125cf2b7d20b2c1f4
| -----BEGIN CERTIFICATE-----
| MIIDajCCAlKgAwIBAgIQUI2QvXTCj7RCVdv6XlGMvjANBgkqhkiG9w0BAQsFADAc
| MRowGAYDVQQDDBFmaXJlLndpbmRjb3JwLnRobTAeFw0yMDA1MjkwMzMxMDhaFw0y
| ODA1MjkwMzQxMDNaMBwxGjAYBgNVBAMMEWZpcmUud2luZGNvcnAudGhtMIIBIjAN
| BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv900af0f6n80F0J6U9jMgcwQrozr
| kXmi02esW1XAsHpWnuuMQDIN6AtiYmDcoFEXz/NteLI7T6PusqQ6SXqLBurTnR8V
| InPD3Qea6lxOXNjuNeqqZKHhUaXiwSaqtAB+GzPkNtevw3jeEj99ST/G1qwY9Xce
| sfeqR2J4kQ+8U5yKLJDPBxOSx3+SHjKErrLTk66lrlEi4atr+P/ccXA5TBkZFkYh
| i3YdKTDnYeP2fMrqvOqpw82eniHAGJ2N8JJbNep86ps8giIRieBUUclF/WCp4c33
| p4i1ioVxJIYJj6f0tjGhy9GxB7l69OtUutcIG0/FhxL2dQ86MmnHH0dE7QIDAQAB
| o4GnMIGkMA4GA1UdDwEB/wQEAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAgYIKwYB
| BQUHAwEwVAYDVR0RBE0wS4IRZmlyZS53aW5kY29ycC50aG2CGHNlbGZzZXJ2aWNl
| LndpbmRjb3JwLnRobYIcc2VsZnNlcnZpY2UuZGV2LndpbmRjb3JwLnRobTAdBgNV
| HQ4EFgQUIZvYlCIhAOFLRutycf6U2H6LhqIwDQYJKoZIhvcNAQELBQADggEBAKVC
| ZS6HOuSODERi/glj3rPJaHCStxHPEg69txOIDaM9fX4WBfmSjn+EzlrHLdeRS22h
| nTPirvuT+5nn6xbUrq9J6RCTZJD+uFc9wZl7Viw3hJcWbsO8DTQAshuZ5YJ574pG
| HjyoVDOfYhy8/8ThvYf1H8/OaIpG4UIo0vY9qeBQBOPZdbdVjWNerkFmXVq+MMVf
| pAt+FffQE/48kTCppuSKeM5ZMgHP1/zhZqyJ3npljVDlgppjvh1loSYB+reMkhwK
| 2gpGJNwxLyFDhTMLaj0pzFL9okqs5ovEWEj8p96hEE6Xxl4ZApv6mxTs9j2oY6+P
| MTUqFyYKchFUeYlgf7k=
|_-----END CERTIFICATE-----
|_ssl-date: 2022-12-22T19:31:55+00:00; -2s from scanner time.
2179/tcp  open  vmrdp?              syn-ack
3268/tcp  open  ldap                syn-ack Microsoft Windows Active Directory LDAP (Domain: windcorp.thm0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=fire.windcorp.thm
| Subject Alternative Name: DNS:fire.windcorp.thm, DNS:selfservice.windcorp.thm, DNS:selfservice.dev.windcorp.thm
| Issuer: commonName=fire.windcorp.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-05-29T03:31:08
| Not valid after:  2028-05-29T03:41:03
| MD5:   804bdc395ce5dd7b19a5851c01d123ad
| SHA-1: 37f4e667cef75cc447c9d20125cf2b7d20b2c1f4
| -----BEGIN CERTIFICATE-----
| MIIDajCCAlKgAwIBAgIQUI2QvXTCj7RCVdv6XlGMvjANBgkqhkiG9w0BAQsFADAc
| MRowGAYDVQQDDBFmaXJlLndpbmRjb3JwLnRobTAeFw0yMDA1MjkwMzMxMDhaFw0y
| ODA1MjkwMzQxMDNaMBwxGjAYBgNVBAMMEWZpcmUud2luZGNvcnAudGhtMIIBIjAN
| BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv900af0f6n80F0J6U9jMgcwQrozr
| kXmi02esW1XAsHpWnuuMQDIN6AtiYmDcoFEXz/NteLI7T6PusqQ6SXqLBurTnR8V
| InPD3Qea6lxOXNjuNeqqZKHhUaXiwSaqtAB+GzPkNtevw3jeEj99ST/G1qwY9Xce
| sfeqR2J4kQ+8U5yKLJDPBxOSx3+SHjKErrLTk66lrlEi4atr+P/ccXA5TBkZFkYh
| i3YdKTDnYeP2fMrqvOqpw82eniHAGJ2N8JJbNep86ps8giIRieBUUclF/WCp4c33
| p4i1ioVxJIYJj6f0tjGhy9GxB7l69OtUutcIG0/FhxL2dQ86MmnHH0dE7QIDAQAB
| o4GnMIGkMA4GA1UdDwEB/wQEAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAgYIKwYB
| BQUHAwEwVAYDVR0RBE0wS4IRZmlyZS53aW5kY29ycC50aG2CGHNlbGZzZXJ2aWNl
| LndpbmRjb3JwLnRobYIcc2VsZnNlcnZpY2UuZGV2LndpbmRjb3JwLnRobTAdBgNV
| HQ4EFgQUIZvYlCIhAOFLRutycf6U2H6LhqIwDQYJKoZIhvcNAQELBQADggEBAKVC
| ZS6HOuSODERi/glj3rPJaHCStxHPEg69txOIDaM9fX4WBfmSjn+EzlrHLdeRS22h
| nTPirvuT+5nn6xbUrq9J6RCTZJD+uFc9wZl7Viw3hJcWbsO8DTQAshuZ5YJ574pG
| HjyoVDOfYhy8/8ThvYf1H8/OaIpG4UIo0vY9qeBQBOPZdbdVjWNerkFmXVq+MMVf
| pAt+FffQE/48kTCppuSKeM5ZMgHP1/zhZqyJ3npljVDlgppjvh1loSYB+reMkhwK
| 2gpGJNwxLyFDhTMLaj0pzFL9okqs5ovEWEj8p96hEE6Xxl4ZApv6mxTs9j2oY6+P
| MTUqFyYKchFUeYlgf7k=
|_-----END CERTIFICATE-----
|_ssl-date: 2022-12-22T19:31:58+00:00; -1s from scanner time.
3269/tcp  open  ssl/ldap            syn-ack Microsoft Windows Active Directory LDAP (Domain: windcorp.thm0., Site: Default-First-Site-Name)
|_ssl-date: 2022-12-22T19:31:56+00:00; -1s from scanner time.
| ssl-cert: Subject: commonName=fire.windcorp.thm
| Subject Alternative Name: DNS:fire.windcorp.thm, DNS:selfservice.windcorp.thm, DNS:selfservice.dev.windcorp.thm
| Issuer: commonName=fire.windcorp.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-05-29T03:31:08
| Not valid after:  2028-05-29T03:41:03
| MD5:   804bdc395ce5dd7b19a5851c01d123ad
| SHA-1: 37f4e667cef75cc447c9d20125cf2b7d20b2c1f4
| -----BEGIN CERTIFICATE-----
| MIIDajCCAlKgAwIBAgIQUI2QvXTCj7RCVdv6XlGMvjANBgkqhkiG9w0BAQsFADAc
| MRowGAYDVQQDDBFmaXJlLndpbmRjb3JwLnRobTAeFw0yMDA1MjkwMzMxMDhaFw0y
| ODA1MjkwMzQxMDNaMBwxGjAYBgNVBAMMEWZpcmUud2luZGNvcnAudGhtMIIBIjAN
| BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv900af0f6n80F0J6U9jMgcwQrozr
| kXmi02esW1XAsHpWnuuMQDIN6AtiYmDcoFEXz/NteLI7T6PusqQ6SXqLBurTnR8V
| InPD3Qea6lxOXNjuNeqqZKHhUaXiwSaqtAB+GzPkNtevw3jeEj99ST/G1qwY9Xce
| sfeqR2J4kQ+8U5yKLJDPBxOSx3+SHjKErrLTk66lrlEi4atr+P/ccXA5TBkZFkYh
| i3YdKTDnYeP2fMrqvOqpw82eniHAGJ2N8JJbNep86ps8giIRieBUUclF/WCp4c33
| p4i1ioVxJIYJj6f0tjGhy9GxB7l69OtUutcIG0/FhxL2dQ86MmnHH0dE7QIDAQAB
| o4GnMIGkMA4GA1UdDwEB/wQEAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAgYIKwYB
| BQUHAwEwVAYDVR0RBE0wS4IRZmlyZS53aW5kY29ycC50aG2CGHNlbGZzZXJ2aWNl
| LndpbmRjb3JwLnRobYIcc2VsZnNlcnZpY2UuZGV2LndpbmRjb3JwLnRobTAdBgNV
| HQ4EFgQUIZvYlCIhAOFLRutycf6U2H6LhqIwDQYJKoZIhvcNAQELBQADggEBAKVC
| ZS6HOuSODERi/glj3rPJaHCStxHPEg69txOIDaM9fX4WBfmSjn+EzlrHLdeRS22h
| nTPirvuT+5nn6xbUrq9J6RCTZJD+uFc9wZl7Viw3hJcWbsO8DTQAshuZ5YJ574pG
| HjyoVDOfYhy8/8ThvYf1H8/OaIpG4UIo0vY9qeBQBOPZdbdVjWNerkFmXVq+MMVf
| pAt+FffQE/48kTCppuSKeM5ZMgHP1/zhZqyJ3npljVDlgppjvh1loSYB+reMkhwK
| 2gpGJNwxLyFDhTMLaj0pzFL9okqs5ovEWEj8p96hEE6Xxl4ZApv6mxTs9j2oY6+P
| MTUqFyYKchFUeYlgf7k=
|_-----END CERTIFICATE-----
3389/tcp  open  ms-wbt-server       syn-ack Microsoft Terminal Services
|_ssl-date: 2022-12-22T19:31:56+00:00; -1s from scanner time.
| ssl-cert: Subject: commonName=Fire.windcorp.thm
| Issuer: commonName=Fire.windcorp.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2022-12-21T18:29:48
| Not valid after:  2023-06-22T18:29:48
| MD5:   aa8d74009e3e023b81a1ee3572528f4e
| SHA-1: 1d8d42b74d461e3edf7101fdf5807bef6d1f71b9
| -----BEGIN CERTIFICATE-----
| MIIC5jCCAc6gAwIBAgIQUolJNkPosrpDW+fy+RcynzANBgkqhkiG9w0BAQsFADAc
| MRowGAYDVQQDExFGaXJlLndpbmRjb3JwLnRobTAeFw0yMjEyMjExODI5NDhaFw0y
| MzA2MjIxODI5NDhaMBwxGjAYBgNVBAMTEUZpcmUud2luZGNvcnAudGhtMIIBIjAN
| BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvSUKk9BuwKO4ZvgK+6Os8Wfaox7m
| 4rQzHZGyJW66E9UP1q1VzudT3Q51PrNRrXbiV/+3Z29sb6tjGulfDNZN7mssESIw
| d1GnoDvDY7ZHtWMQaiMRV3eAavbSIOlIsD42Yzq7OoSoJEytPZS3BMLSjhLSjN6u
| 3UfNW1bu7BV8VKz5lAnOPaEWCxCZAHiYH1uXFPmFPyebMGFarFgpOx3oeJ6wwhVQ
| UG1qbtoFpEZkZ7LG715f6bDt3oBReFCMhLj9Zqe8TDytgZoCeFygXHXUGaiU+cXO
| TqiOoSglrUwWoaNm5+M0fvNZuew6p3LBdeY9WGixtiO/vQfqWYyTXUnSlQIDAQAB
| oyQwIjATBgNVHSUEDDAKBggrBgEFBQcDATALBgNVHQ8EBAMCBDAwDQYJKoZIhvcN
| AQELBQADggEBAGGxjTHOBn91GeDXijQqsQSwH2xFm+2maFwt9yIRAhgjub+I/lFo
| 6FgaZ2wB/a0C3v9Wjilvtl4DT1msu5lD8z2Uf0xeXFrRxCBi4wTsQSHEPS4rEb6g
| 6w/Vs+qFDUcwWrefRuXSCOZHRtCM/7T7591kUZPrqvMFr071m6wMMBeGq6Wp+e3K
| wW6fakF6qOvAO+o8W2delI0HUj9y/HMTup9GJDzw3Hz37uOYoc9fHnvHayVjIiHK
| tR4PD12UvbR+84/gHVWEi98fR1J2kJvZOUxvQNCmpxtzFtkVIA1TxlyGAe3I4jtC
| lo+l8TDNBRuIWozrIMUYGoC2HWGDMTIjZx8=
|_-----END CERTIFICATE-----
5222/tcp  open  jabber              syn-ack
| xmpp-info: 
|   STARTTLS Failed
|   info: 
|     capabilities: 
|     errors: 
|       invalid-namespace
|       (timeout)
|     unknown: 
|     auth_mechanisms: 
|     compression_methods: 
|     features: 
|     stream_id: 4h64nvl9gw
|     xmpp: 
|_      version: 1.0
| ssl-cert: Subject: commonName=fire.windcorp.thm
| Subject Alternative Name: DNS:fire.windcorp.thm, DNS:*.fire.windcorp.thm
| Issuer: commonName=fire.windcorp.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-05-01T08:39:00
| Not valid after:  2025-04-30T08:39:00
| MD5:   b715542583f3a20f75c8ca2d3353cbb7
| SHA-1: 97f70772a26be3247ed5bbcb5f357d74798266ae
| -----BEGIN CERTIFICATE-----
| MIIDLzCCAhegAwIBAgIIXUFELG7QgAIwDQYJKoZIhvcNAQELBQAwHDEaMBgGA1UE
| AwwRZmlyZS53aW5kY29ycC50aG0wHhcNMjAwNTAxMDgzOTAwWhcNMjUwNDMwMDgz
| OTAwWjAcMRowGAYDVQQDDBFmaXJlLndpbmRjb3JwLnRobTCCASIwDQYJKoZIhvcN
| AQEBBQADggEPADCCAQoCggEBAKLH0/j17RVdD8eXC+0IFovAoql2REjOSf2NpJLK
| /6fgtx3CA4ftLsj7yOpmj8Oe1gqfWd2EM/zKk+ZmZwQFxLQL93t1OD/za1gyclxr
| IVbPVWqFoM2BUU9O3yU0VVRGP7xKDHm4bcoNmq9UNurEtFlCNeCC1fcwzfYvKD89
| X04Rv/6kn1GlQq/iM8PGCLDUf1p1WJcwGT5FUiBa9boTU9llBcGqbodZaBKzPPP8
| DmvSYF71IKBT8NsVzqiAiO3t/oHgApvUd9BqdbZeN46XORrOhBQV0xUpNVy9L5OE
| UAD1so3ePTNjpPE5SfTKymT1a8Fiw5kroKODN0nzy50yP3UCAwEAAaN1MHMwMQYD
| VR0RBCowKIIRZmlyZS53aW5kY29ycC50aG2CEyouZmlyZS53aW5kY29ycC50aG0w
| HQYDVR0OBBYEFOtMzqgfsY11qewZNfPjiLxnGykGMB8GA1UdIwQYMBaAFOtMzqgf
| sY11qewZNfPjiLxnGykGMA0GCSqGSIb3DQEBCwUAA4IBAQAHofv0VP+hE+5sg0KR
| 2x0Xeg4cIXEia0c5cIJ7K7bhfoLOcT7WcMKCLIN3A416PREdkB6Q610uDs8RpezJ
| II/wBoIp2G0Y87X3Xo5FmNJjl9lGX5fvayen98khPXvZkurHdWdtA4m8pHOdYOrk
| n8Jth6L/y4L5WlgEGL0x0HK4yvd3iz0VNrc810HugpyfVWeasChhZjgAYXUVlA8k
| +QxLxyNr/PBfRumQGzw2n3msXxwfHVzaHphy56ph85PcRS35iNqgrtK0fe3Qhpq7
| v5vQYKlOGq5FI6Mf9ni7S1pXSqF4U9wuqZy4q4tXWAVootmJv1DIgfSMLvXplN9T
| LucP
|_-----END CERTIFICATE-----
|_ssl-date: 2022-12-22T19:31:58+00:00; -2s from scanner time.
| fingerprint-strings: 
|   RPCCheck: 
|_    <stream:error xmlns:stream="http://etherx.jabber.org/streams"><not-well-formed xmlns="urn:ietf:params:xml:ns:xmpp-streams"/></stream:error></stream:stream>
5223/tcp  open  ssl/jabber          syn-ack Ignite Realtime Openfire Jabber server 3.10.0 or later
| ssl-cert: Subject: commonName=fire.windcorp.thm
| Subject Alternative Name: DNS:fire.windcorp.thm, DNS:*.fire.windcorp.thm
| Issuer: commonName=fire.windcorp.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-05-01T08:39:00
| Not valid after:  2025-04-30T08:39:00
| MD5:   b715542583f3a20f75c8ca2d3353cbb7
| SHA-1: 97f70772a26be3247ed5bbcb5f357d74798266ae
| -----BEGIN CERTIFICATE-----
| MIIDLzCCAhegAwIBAgIIXUFELG7QgAIwDQYJKoZIhvcNAQELBQAwHDEaMBgGA1UE
| AwwRZmlyZS53aW5kY29ycC50aG0wHhcNMjAwNTAxMDgzOTAwWhcNMjUwNDMwMDgz
| OTAwWjAcMRowGAYDVQQDDBFmaXJlLndpbmRjb3JwLnRobTCCASIwDQYJKoZIhvcN
| AQEBBQADggEPADCCAQoCggEBAKLH0/j17RVdD8eXC+0IFovAoql2REjOSf2NpJLK
| /6fgtx3CA4ftLsj7yOpmj8Oe1gqfWd2EM/zKk+ZmZwQFxLQL93t1OD/za1gyclxr
| IVbPVWqFoM2BUU9O3yU0VVRGP7xKDHm4bcoNmq9UNurEtFlCNeCC1fcwzfYvKD89
| X04Rv/6kn1GlQq/iM8PGCLDUf1p1WJcwGT5FUiBa9boTU9llBcGqbodZaBKzPPP8
| DmvSYF71IKBT8NsVzqiAiO3t/oHgApvUd9BqdbZeN46XORrOhBQV0xUpNVy9L5OE
| UAD1so3ePTNjpPE5SfTKymT1a8Fiw5kroKODN0nzy50yP3UCAwEAAaN1MHMwMQYD
| VR0RBCowKIIRZmlyZS53aW5kY29ycC50aG2CEyouZmlyZS53aW5kY29ycC50aG0w
| HQYDVR0OBBYEFOtMzqgfsY11qewZNfPjiLxnGykGMB8GA1UdIwQYMBaAFOtMzqgf
| sY11qewZNfPjiLxnGykGMA0GCSqGSIb3DQEBCwUAA4IBAQAHofv0VP+hE+5sg0KR
| 2x0Xeg4cIXEia0c5cIJ7K7bhfoLOcT7WcMKCLIN3A416PREdkB6Q610uDs8RpezJ
| II/wBoIp2G0Y87X3Xo5FmNJjl9lGX5fvayen98khPXvZkurHdWdtA4m8pHOdYOrk
| n8Jth6L/y4L5WlgEGL0x0HK4yvd3iz0VNrc810HugpyfVWeasChhZjgAYXUVlA8k
| +QxLxyNr/PBfRumQGzw2n3msXxwfHVzaHphy56ph85PcRS35iNqgrtK0fe3Qhpq7
| v5vQYKlOGq5FI6Mf9ni7S1pXSqF4U9wuqZy4q4tXWAVootmJv1DIgfSMLvXplN9T
| LucP
|_-----END CERTIFICATE-----
|_ssl-date: 2022-12-22T19:31:56+00:00; -1s from scanner time.
| xmpp-info: 
|   STARTTLS Failed
|   info: 
|     capabilities: 
|     unknown: 
|     errors: 
|       (timeout)
|     compression_methods: 
|     auth_mechanisms: 
|     xmpp: 
|_    features: 
5229/tcp  open  jaxflow?            syn-ack
5262/tcp  open  jabber              syn-ack
| xmpp-info: 
|   STARTTLS Failed
|   info: 
|     capabilities: 
|     errors: 
|       invalid-namespace
|       (timeout)
|     unknown: 
|     auth_mechanisms: 
|     compression_methods: 
|     features: 
|     stream_id: 3tdo9mabru
|     xmpp: 
|_      version: 1.0
| fingerprint-strings: 
|   RPCCheck: 
|_    <stream:error xmlns:stream="http://etherx.jabber.org/streams"><not-well-formed xmlns="urn:ietf:params:xml:ns:xmpp-streams"/></stream:error></stream:stream>
5263/tcp  open  ssl/jabber          syn-ack
| ssl-cert: Subject: commonName=fire.windcorp.thm
| Subject Alternative Name: DNS:fire.windcorp.thm, DNS:*.fire.windcorp.thm
| Issuer: commonName=fire.windcorp.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-05-01T08:39:00
| Not valid after:  2025-04-30T08:39:00
| MD5:   b715542583f3a20f75c8ca2d3353cbb7
| SHA-1: 97f70772a26be3247ed5bbcb5f357d74798266ae
| -----BEGIN CERTIFICATE-----
| MIIDLzCCAhegAwIBAgIIXUFELG7QgAIwDQYJKoZIhvcNAQELBQAwHDEaMBgGA1UE
| AwwRZmlyZS53aW5kY29ycC50aG0wHhcNMjAwNTAxMDgzOTAwWhcNMjUwNDMwMDgz
| OTAwWjAcMRowGAYDVQQDDBFmaXJlLndpbmRjb3JwLnRobTCCASIwDQYJKoZIhvcN
| AQEBBQADggEPADCCAQoCggEBAKLH0/j17RVdD8eXC+0IFovAoql2REjOSf2NpJLK
| /6fgtx3CA4ftLsj7yOpmj8Oe1gqfWd2EM/zKk+ZmZwQFxLQL93t1OD/za1gyclxr
| IVbPVWqFoM2BUU9O3yU0VVRGP7xKDHm4bcoNmq9UNurEtFlCNeCC1fcwzfYvKD89
| X04Rv/6kn1GlQq/iM8PGCLDUf1p1WJcwGT5FUiBa9boTU9llBcGqbodZaBKzPPP8
| DmvSYF71IKBT8NsVzqiAiO3t/oHgApvUd9BqdbZeN46XORrOhBQV0xUpNVy9L5OE
| UAD1so3ePTNjpPE5SfTKymT1a8Fiw5kroKODN0nzy50yP3UCAwEAAaN1MHMwMQYD
| VR0RBCowKIIRZmlyZS53aW5kY29ycC50aG2CEyouZmlyZS53aW5kY29ycC50aG0w
| HQYDVR0OBBYEFOtMzqgfsY11qewZNfPjiLxnGykGMB8GA1UdIwQYMBaAFOtMzqgf
| sY11qewZNfPjiLxnGykGMA0GCSqGSIb3DQEBCwUAA4IBAQAHofv0VP+hE+5sg0KR
| 2x0Xeg4cIXEia0c5cIJ7K7bhfoLOcT7WcMKCLIN3A416PREdkB6Q610uDs8RpezJ
| II/wBoIp2G0Y87X3Xo5FmNJjl9lGX5fvayen98khPXvZkurHdWdtA4m8pHOdYOrk
| n8Jth6L/y4L5WlgEGL0x0HK4yvd3iz0VNrc810HugpyfVWeasChhZjgAYXUVlA8k
| +QxLxyNr/PBfRumQGzw2n3msXxwfHVzaHphy56ph85PcRS35iNqgrtK0fe3Qhpq7
| v5vQYKlOGq5FI6Mf9ni7S1pXSqF4U9wuqZy4q4tXWAVootmJv1DIgfSMLvXplN9T
| LucP
|_-----END CERTIFICATE-----
| xmpp-info: 
|   STARTTLS Failed
|   info: 
|     capabilities: 
|     unknown: 
|     errors: 
|       (timeout)
|     compression_methods: 
|     auth_mechanisms: 
|     xmpp: 
|_    features: 
|_ssl-date: 2022-12-22T19:31:57+00:00; -1s from scanner time.
| fingerprint-strings: 
|   RPCCheck: 
|_    <stream:error xmlns:stream="http://etherx.jabber.org/streams"><not-well-formed xmlns="urn:ietf:params:xml:ns:xmpp-streams"/></stream:error></stream:stream>
5269/tcp  open  xmpp                syn-ack Wildfire XMPP Client
| xmpp-info: 
|   STARTTLS Failed
|   info: 
|     capabilities: 
|     unknown: 
|     errors: 
|       (timeout)
|     compression_methods: 
|     auth_mechanisms: 
|     xmpp: 
|_    features: 
5270/tcp  open  ssl/xmpp            syn-ack Wildfire XMPP Client
|_ssl-date: 2022-12-22T19:31:55+00:00; -2s from scanner time.
| ssl-cert: Subject: commonName=fire.windcorp.thm
| Subject Alternative Name: DNS:fire.windcorp.thm, DNS:*.fire.windcorp.thm
| Issuer: commonName=fire.windcorp.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-05-01T08:39:00
| Not valid after:  2025-04-30T08:39:00
| MD5:   b715542583f3a20f75c8ca2d3353cbb7
| SHA-1: 97f70772a26be3247ed5bbcb5f357d74798266ae
| -----BEGIN CERTIFICATE-----
| MIIDLzCCAhegAwIBAgIIXUFELG7QgAIwDQYJKoZIhvcNAQELBQAwHDEaMBgGA1UE
| AwwRZmlyZS53aW5kY29ycC50aG0wHhcNMjAwNTAxMDgzOTAwWhcNMjUwNDMwMDgz
| OTAwWjAcMRowGAYDVQQDDBFmaXJlLndpbmRjb3JwLnRobTCCASIwDQYJKoZIhvcN
| AQEBBQADggEPADCCAQoCggEBAKLH0/j17RVdD8eXC+0IFovAoql2REjOSf2NpJLK
| /6fgtx3CA4ftLsj7yOpmj8Oe1gqfWd2EM/zKk+ZmZwQFxLQL93t1OD/za1gyclxr
| IVbPVWqFoM2BUU9O3yU0VVRGP7xKDHm4bcoNmq9UNurEtFlCNeCC1fcwzfYvKD89
| X04Rv/6kn1GlQq/iM8PGCLDUf1p1WJcwGT5FUiBa9boTU9llBcGqbodZaBKzPPP8
| DmvSYF71IKBT8NsVzqiAiO3t/oHgApvUd9BqdbZeN46XORrOhBQV0xUpNVy9L5OE
| UAD1so3ePTNjpPE5SfTKymT1a8Fiw5kroKODN0nzy50yP3UCAwEAAaN1MHMwMQYD
| VR0RBCowKIIRZmlyZS53aW5kY29ycC50aG2CEyouZmlyZS53aW5kY29ycC50aG0w
| HQYDVR0OBBYEFOtMzqgfsY11qewZNfPjiLxnGykGMB8GA1UdIwQYMBaAFOtMzqgf
| sY11qewZNfPjiLxnGykGMA0GCSqGSIb3DQEBCwUAA4IBAQAHofv0VP+hE+5sg0KR
| 2x0Xeg4cIXEia0c5cIJ7K7bhfoLOcT7WcMKCLIN3A416PREdkB6Q610uDs8RpezJ
| II/wBoIp2G0Y87X3Xo5FmNJjl9lGX5fvayen98khPXvZkurHdWdtA4m8pHOdYOrk
| n8Jth6L/y4L5WlgEGL0x0HK4yvd3iz0VNrc810HugpyfVWeasChhZjgAYXUVlA8k
| +QxLxyNr/PBfRumQGzw2n3msXxwfHVzaHphy56ph85PcRS35iNqgrtK0fe3Qhpq7
| v5vQYKlOGq5FI6Mf9ni7S1pXSqF4U9wuqZy4q4tXWAVootmJv1DIgfSMLvXplN9T
| LucP
|_-----END CERTIFICATE-----
5275/tcp  open  jabber              syn-ack
| xmpp-info: 
|   STARTTLS Failed
|   info: 
|     capabilities: 
|     errors: 
|       invalid-namespace
|       (timeout)
|     unknown: 
|     auth_mechanisms: 
|     compression_methods: 
|     features: 
|     stream_id: 7n7jqz5kvm
|     xmpp: 
|_      version: 1.0
| fingerprint-strings: 
|   RPCCheck: 
|_    <stream:error xmlns:stream="http://etherx.jabber.org/streams"><not-well-formed xmlns="urn:ietf:params:xml:ns:xmpp-streams"/></stream:error></stream:stream>
