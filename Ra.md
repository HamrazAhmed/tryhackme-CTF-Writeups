# Ra — Writeup

## Overview
### Ra — Writeup
### Ra — Writeup
You have found WindCorp's internal network and their Domain Controller. Can you pwn their network?
![](https://i.imgur.com/eyf66N3.png)
![|333](https://tryhackme-images.s3.amazonaws.com/room-icons/f8cc5f48d1b4cf162c24c6964dfe0718.jpeg)
Story
You have gained access to the internal network of WindCorp, the multibillion dollar company, running an extensive social media campaign claiming to be unhackable (ha! so much for that claim!).
Next step would be to take their crown jewels and get full access to their internal network. You have spotted a new windows machine that may lead you to your end goal. Can you conquer this end boss and own their internal network?
Happy Hacking!
@4nqr34z and @theart42
(Give it at least 5 minutes to boot)
```text

```

## Enumeration
```text
┌──(kali㉿kali)-[~]
└─$ rustscan -a 10.10.181.243 --ulimit 5500 -b 65535 -- -A
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

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.181.243:53
Open 10.10.181.243:80
Open 10.10.181.243:88
Open 10.10.181.243:135
Open 10.10.181.243:139
Open 10.10.181.243:389
Open 10.10.181.243:445
Open 10.10.181.243:464
Open 10.10.181.243:593
Open 10.10.181.243:636
Open 10.10.181.243:2179
Open 10.10.181.243:3269
Open 10.10.181.243:3268
Open 10.10.181.243:5222
Open 10.10.181.243:5223
Open 10.10.181.243:5229
Open 10.10.181.243:5263
Open 10.10.181.243:5262
Open 10.10.181.243:5269
Open 10.10.181.243:5270
Open 10.10.181.243:5275
Open 10.10.181.243:5276
Open 10.10.181.243:3389
Open 10.10.181.243:7070
Open 10.10.181.243:7443
Open 10.10.181.243:7777
Open 10.10.181.243:9090
Open 10.10.181.243:9091
Open 10.10.181.243:9389
Open 10.10.181.243:49670
Open 10.10.181.243:49674
Open 10.10.181.243:49675
Open 10.10.181.243:49676
Open 10.10.181.243:49744
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

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
Initiating Ping Scan
Scanning 10.10.181.243 [2 ports]
Completed Ping Scan (1 total hosts)
Initiating Parallel DNS resolution of 1 host.
Completed Parallel DNS resolution of 1 host.
DNS resolution of 1 IPs took 0.01s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.181.243 [34 ports]
Discovered open port 3389/tcp on 10.10.181.243
Discovered open port 135/tcp on 10.10.181.243
Discovered open port 7443/tcp on 10.10.181.243
Discovered open port 139/tcp on 10.10.181.243
Discovered open port 53/tcp on 10.10.181.243
Discovered open port 80/tcp on 10.10.181.243
Discovered open port 445/tcp on 10.10.181.243
Discovered open port 88/tcp on 10.10.181.243
Discovered open port 5222/tcp on 10.10.181.243
Discovered open port 636/tcp on 10.10.181.243
Discovered open port 389/tcp on 10.10.181.243
Discovered open port 49676/tcp on 10.10.181.243
Discovered open port 3269/tcp on 10.10.181.243
Discovered open port 49675/tcp on 10.10.181.243
Discovered open port 49670/tcp on 10.10.181.243
Discovered open port 7070/tcp on 10.10.181.243
Discovered open port 7777/tcp on 10.10.181.243
Discovered open port 5270/tcp on 10.10.181.243
Discovered open port 9090/tcp on 10.10.181.243
Discovered open port 3268/tcp on 10.10.181.243
Discovered open port 9091/tcp on 10.10.181.243
Discovered open port 49744/tcp on 10.10.181.243
Discovered open port 2179/tcp on 10.10.181.243
Discovered open port 5275/tcp on 10.10.181.243
Discovered open port 5276/tcp on 10.10.181.243
Discovered open port 5269/tcp on 10.10.181.243
Discovered open port 5263/tcp on 10.10.181.243
Discovered open port 49674/tcp on 10.10.181.243
Discovered open port 5229/tcp on 10.10.181.243
Discovered open port 5223/tcp on 10.10.181.243
Discovered open port 9389/tcp on 10.10.181.243
Discovered open port 5262/tcp on 10.10.181.243
Discovered open port 593/tcp on 10.10.181.243
Discovered open port 464/tcp on 10.10.181.243
Completed Connect Scan (34 total ports)
Initiating Service scan
Scanning 34 services on 10.10.181.243
Completed Service scan (34 services on 1 host)
NSE: Script scanning 10.10.181.243.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
NSE Timing: About 99.98% done; ETC: 23:59 (0:00:00 remaining)
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.181.243
Host is up, received syn-ack (0.19s latency).

PORT      STATE SERVICE             REASON  VERSION
53/tcp    open  domain              syn-ack Simple DNS Plus
80/tcp    open  http                syn-ack Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Windcorp.
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
88/tcp    open  kerberos-sec        syn-ack Microsoft Windows Kerberos (server time: :07Z)
135/tcp   open  msrpc               syn-ack Microsoft Windows RPC
139/tcp   open  netbios-ssn         syn-ack Microsoft Windows netbios-ssn
389/tcp   open  ldap                syn-ack Microsoft Windows Active Directory LDAP (Domain: windcorp.thm0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?       syn-ack
464/tcp   open  kpasswd5?           syn-ack
593/tcp   open  ncacn_http          syn-ack Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped          syn-ack
2179/tcp  open  vmrdp?              syn-ack
3268/tcp  open  ldap                syn-ack Microsoft Windows Active Directory LDAP (Domain: windcorp.thm0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped          syn-ack
3389/tcp  open  ms-wbt-server       syn-ack Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: WINDCORP
|   NetBIOS_Domain_Name: WINDCORP
|   NetBIOS_Computer_Name: FIRE
|   DNS_Domain_Name: windcorp.thm
|   DNS_Computer_Name: Fire.windcorp.thm
|   DNS_Tree_Name: windcorp.thm
|   Product_Version: 10.0.17763
|_  System_Time: 2022-11-11T04:59:22+00:00
| ssl-cert: Subject: commonName=Fire.windcorp.thm
| Issuer: commonName=Fire.windcorp.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| MD5:   d02273d5759254452f97ba86e8e8b9d5
| SHA-1: 5c8e941c1ba3a58b23de34a7e4150358bfb899de
| -----BEGIN CERTIFICATE-----
| MIIC5jCCAc6gAwIBAgIQJ8yi/yqmtZpB8xFyQ1xT5DANBgkqhkiG9w0BAQsFADAc
| MRowGAYDVQQDExFGaXJlLndpbmRjb3JwLnRobTAeFw0yMjExMTAwNDU3MjZaFw0y
| MzA1MTIwNDU3MjZaMBwxGjAYBgNVBAMTEUZpcmUud2luZGNvcnAudGhtMIIBIjAN
| BgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyd9RGA4CF7NFWAgDc4CmOifl5msy
| EToX1hdkb+I1syZS0vivCGaqMzSx3t9ahbEaWWS+cYdgnLooOLex9KYvVCPLLzD2
| 0uE9IgZIYDO+nqm48Japa4PqBbs83lmgLME3GjEmI8jHofaEDTkQ69vewBR7iT5w
| QD7PD+v4s5Gl8G7fwcOmgedSgA4xr2FUW7AsdYmVjvIBwDQjpAIhi0IfLVEisi3Z
| UnDXa+A4R8CtskQKogaREE1Vnlfl8JPUSMd4vR4GbM31RvjwK+/d74k7b75A0Tl/
| 3aDeUfZJu+cOtaW3YFjsyfnL2XXCyW8PnOm21nR7LN4kjDsQFtfCnF1xaQIDAQAB
| oyQwIjATBgNVHSUEDDAKBggrBgEFBQcDATALBgNVHQ8EBAMCBDAwDQYJKoZIhvcN
| AQELBQADggEBAE5HJhCKWreAOPEXulK+BY0nrGrU+jlr4kWNyBJCg+D0C1fjOq6w
| QTVn6SXd9f26RMsjs7cJ1QqXZyCECJzOVCt0I0TUjsfFACYzMKK3DI2Af70tqjb7
| l8LY1yeY8WAHwVMXNJps1YYm7cWmiN/HhfSHDngfLM5dGG2JxPluZjUieccUgFrL
| HRkYbcVRj1MzP2DDyp8tKJU76HH57rjqUKnb9CVtaYcwq6UVq/bCio1SN6iyfb+I
| feO0IlZIhUKbNtL8pNuOdditYC+MnYSCfX4+MFI4tJdKfTCQGaRBtJxotvTsY6iK
| +W3SbhXgvpEkt9lA5L8jspZRZoNNBkJtpT8=
|_-----END CERTIFICATE-----
5222/tcp  open  jabber              syn-ack
| xmpp-info: 
|   STARTTLS Failed
|   info: 
|     unknown: 
|     errors: 
|       invalid-namespace
|       (timeout)
|     auth_mechanisms: 
|     capabilities: 
|     xmpp: 
|       version: 1.0
|     stream_id: 32p2034xhh
|     features: 
|_    compression_methods: 
| fingerprint-strings: 
|   RPCCheck: 
|_    <stream:error xmlns:stream="http://etherx.jabber.org/streams"><not-well-formed xmlns="urn:ietf:params:xml:ns:xmpp-streams"/></stream:error></stream:stream>
| ssl-cert: Subject: commonName=fire.windcorp.thm
| Subject Alternative Name: DNS:fire.windcorp.thm, DNS:*.fire.windcorp.thm
| Issuer: commonName=fire.windcorp.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
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
5223/tcp  open  ssl/jabber          syn-ack
| ssl-cert: Subject: commonName=fire.windcorp.thm
| Subject Alternative Name: DNS:fire.windcorp.thm, DNS:*.fire.windcorp.thm
| Issuer: commonName=fire.windcorp.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
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
| fingerprint-strings: 
|   RPCCheck: 
|_    <stream:error xmlns:stream="http://etherx.jabber.org/streams"><not-well-formed xmlns="urn:ietf:params:xml:ns:xmpp-streams"/></stream:error></stream:stream>
| xmpp-info: 
|   STARTTLS Failed
|   info: 
|     unknown: 
|     errors: 
|       (timeout)
|     auth_mechanisms: 
|     capabilities: 
|     xmpp: 
|     features: 
|_    compression_methods: 
5229/tcp  open  jaxflow?            syn-ack
5262/tcp  open  jabber              syn-ack
| xmpp-info: 
|   STARTTLS Failed
|   info: 
|     unknown: 
|     errors: 
|       invalid-namespace
|       (timeout)
|     auth_mechanisms: 
|     capabilities: 
|     xmpp: 
|       version: 1.0
|     stream_id: a2i6vozifr
|     features: 
|_    compression_methods: 
| fingerprint-strings: 
|   RPCCheck: 
|_    <stream:error xmlns:stream="http://etherx.jabber.org/streams"><not-well-formed xmlns="urn:ietf:params:xml:ns:xmpp-streams"/></stream:error></stream:stream>
5263/tcp  open  ssl/jabber          syn-ack
| xmpp-info: 
|   STARTTLS Failed
|   info: 
|     unknown: 
|     errors: 
|       (timeout)
|     auth_mechanisms: 
|     capabilities: 
|     xmpp: 
|     features: 
|_    compression_methods: 
| fingerprint-strings: 
|   RPCCheck: 
|_    <stream:error xmlns:stream="http://etherx.jabber.org/streams"><not-well-formed xmlns="urn:ietf:params:xml:ns:xmpp-streams"/></stream:error></stream:stream>
| ssl-cert: Subject: commonName=fire.windcorp.thm
| Subject Alternative Name: DNS:fire.windcorp.thm, DNS:*.fire.windcorp.thm
| Issuer: commonName=fire.windcorp.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
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
5269/tcp  open  xmpp                syn-ack Wildfire XMPP Client
| xmpp-info: 
|   STARTTLS Failed
|   info: 
|     unknown: 
|     errors: 
|       (timeout)
|     auth_mechanisms: 
|     capabilities: 
|     xmpp: 
|     features: 
|_    compression_methods: 
5270/tcp  open  ssl/xmpp            syn-ack Wildfire XMPP Client
| ssl-cert: Subject: commonName=fire.windcorp.thm
| Subject Alternative Name: DNS:fire.windcorp.thm, DNS:*.fire.windcorp.thm
| Issuer: commonName=fire.windcorp.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
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
|     unknown: 
|     errors: 
|       invalid-namespace
|       (timeout)
|     auth_mechanisms: 
|     capabilities: 
|     xmpp: 
|       version: 1.0
|     stream_id: 5ncnsa3rv1
|     features: 
|_    compression_methods: 
| fingerprint-strings: 
|   RPCCheck: 
|_    <stream:error xmlns:stream="http://etherx.jabber.org/streams"><not-well-formed xmlns="urn:ietf:params:xml:ns:xmpp-streams"/></stream:error></stream:stream>
5276/tcp  open  ssl/jabber          syn-ack
| ssl-cert: Subject: commonName=fire.windcorp.thm
| Subject Alternative Name: DNS:fire.windcorp.thm, DNS:*.fire.windcorp.thm
| Issuer: commonName=fire.windcorp.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
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
|     unknown: 
|     errors: 
|       (timeout)
|     auth_mechanisms: 
|     capabilities: 
|     xmpp: 
|     features: 
|_    compression_methods: 
| fingerprint-strings: 
|   RPCCheck: 
|_    <stream:error xmlns:stream="http://etherx.jabber.org/streams"><not-well-formed xmlns="urn:ietf:params:xml:ns:xmpp-streams"/></stream:error></stream:stream>
7070/tcp  open  http                syn-ack Jetty 9.4.18.v20190429
|_http-title: Openfire HTTP Binding Service
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Jetty(9.4.18.v20190429)
7443/tcp  open  ssl/http            syn-ack Jetty 9.4.18.v20190429
|_http-server-header: Jetty(9.4.18.v20190429)
| ssl-cert: Subject: commonName=fire.windcorp.thm
| Subject Alternative Name: DNS:fire.windcorp.thm, DNS:*.fire.windcorp.thm
| Issuer: commonName=fire.windcorp.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
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
| http-methods: 
|_  Supported Methods: GET
7777/tcp  open  socks5              syn-ack (No authentication; connection not allowed by ruleset)
| socks-auth-info: 
|_  No authentication
9090/tcp  open  zeus-admin?         syn-ack
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Date: Fri, 11 Nov 2022 04:58:13 GMT
|     Last-Modified: Fri, 31 Jan 2020 17:54:10 GMT
|     Content-Type: text/html
|     Accept-Ranges: bytes
|     Content-Length: 115
|     <html>
|     <head><title></title>
|     <meta http-equiv="refresh" content="0;URL=index.jsp">
|     </head>
|     <body>
|     </body>
|     </html>
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Date: Fri, 11 Nov 2022 04:58:21 GMT
|     Allow: GET,HEAD,POST,OPTIONS
|   JavaRMI, drda, ibm-db2-das, informix: 
|     HTTP/1.1 400 Illegal character CNTL=0x0
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 69
|     Connection: close
|     <h1>Bad Message 400</h1><pre>reason: Illegal character CNTL=0x0</pre>
|   SqueezeCenter_CLI: 
|     HTTP/1.1 400 No URI
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 49
|     Connection: close
|     <h1>Bad Message 400</h1><pre>reason: No URI</pre>
|   WMSRequest: 
|     HTTP/1.1 400 Illegal character CNTL=0x1
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 69
|     Connection: close
|_    <h1>Bad Message 400</h1><pre>reason: Illegal character CNTL=0x1</pre>
9091/tcp  open  ssl/xmltec-xmlmail? syn-ack
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP: 
|     HTTP/1.1 400 Illegal character CNTL=0x0
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 69
|     Connection: close
|     <h1>Bad Message 400</h1><pre>reason: Illegal character CNTL=0x0</pre>
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Date: Fri, 11 Nov 2022 04:58:35 GMT
|     Last-Modified: Fri, 31 Jan 2020 17:54:10 GMT
|     Content-Type: text/html
|     Accept-Ranges: bytes
|     Content-Length: 115
|     <html>
|     <head><title></title>
|     <meta http-equiv="refresh" content="0;URL=index.jsp">
|     </head>
|     <body>
|     </body>
|     </html>
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Date: Fri, 11 Nov 2022 04:58:36 GMT
|     Allow: GET,HEAD,POST,OPTIONS
|   Help: 
|     HTTP/1.1 400 No URI
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 49
|     Connection: close
|     <h1>Bad Message 400</h1><pre>reason: No URI</pre>
|   RPCCheck: 
|     HTTP/1.1 400 Illegal character OTEXT=0x80
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 71
|     Connection: close
|     <h1>Bad Message 400</h1><pre>reason: Illegal character OTEXT=0x80</pre>
|   RTSPRequest: 
|     HTTP/1.1 400 Unknown Version
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 58
|     Connection: close
|     <h1>Bad Message 400</h1><pre>reason: Unknown Version</pre>
|   SSLSessionReq: 
|     HTTP/1.1 400 Illegal character CNTL=0x16
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 70
|     Connection: close
|_    <h1>Bad Message 400</h1><pre>reason: Illegal character CNTL=0x16</pre>
| ssl-cert: Subject: commonName=fire.windcorp.thm
| Subject Alternative Name: DNS:fire.windcorp.thm, DNS:*.fire.windcorp.thm
| Issuer: commonName=fire.windcorp.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
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
9389/tcp  open  mc-nmf              syn-ack .NET Message Framing
49670/tcp open  msrpc               syn-ack Microsoft Windows RPC
49674/tcp open  ncacn_http          syn-ack Microsoft Windows RPC over HTTP 1.0
49675/tcp open  msrpc               syn-ack Microsoft Windows RPC
49676/tcp open  msrpc               syn-ack Microsoft Windows RPC
49744/tcp open  msrpc               syn-ack Microsoft Windows RPC
8 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port5222-TCP:V=7.93%I=7%D=11/10%Time=636DD675%P=x86_64-pc-linux-gnu%r(R
SF:PCCheck,9B,"<stream:error\x20xmlns:stream=\"http://etherx\.jabber\.org/
SF:streams\"><not-well-formed\x20xmlns=\"urn:ietf:params:xml:ns:xmpp-strea
