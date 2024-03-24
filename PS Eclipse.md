# PS Eclipse — Writeup

## Overview
### PS Eclipse — Writeup
### PS Eclipse — Writeup
----
Use Splunk to investigate the ransomware activity.
----
![](https://assets.tryhackme.com/additional/pseclipse/pseclipse-banner.png)
### Ransomware or not
Start Machine
![](https://assets.tryhackme.com/additional/jrsecanalyst/task2.png)
Scenario: You are a SOC Analyst for an MSSP (Managed Security Service Provider) company called **TryNotHackMe**.
A customer sent an email asking for an analyst to investigate the events that occurred on Keegan's machine on **Monday, May 16th, 2022**. The client noted that **the machine** is operational, but some files have a weird file extension. The client is worried that there was a ransomware attempt on Keegan's device.
Your manager has tasked you to check the events in Splunk to determine what occurred in Keegan's device.
Happy Hunting!
---
Virtual Machine
You can use the Attack Box or OpenVPN to access the Splunk instance. The IP for the Splunk instance is **MACHINE_IP**.
**Note**: Wait for the virtual machine to fully load. If you see errors after 2 minutes, refresh the URL until it loads.
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/bug_hunter/Endpoints/screenshots]
└─$ rustscan -a 10.10.11.55 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
😵 https://admin.tryhackme.com

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.11.55:22
Open 10.10.11.55:80
Open 10.10.11.55:8000
Open 10.10.11.55:8089
Open 10.10.11.55:8191
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
Scanning 10.10.11.55 [5 ports]
Discovered open port 80/tcp on 10.10.11.55
Discovered open port 22/tcp on 10.10.11.55
Discovered open port 8000/tcp on 10.10.11.55
Discovered open port 8191/tcp on 10.10.11.55
Discovered open port 8089/tcp on 10.10.11.55
Completed Connect Scan (5 total ports)
Initiating Service scan
Scanning 5 services on 10.10.11.55
Completed Service scan (5 services on 1 host)
NSE: Script scanning 10.10.11.55.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.11.55
Host is up, received user-set (0.19s latency).

PORT     STATE SERVICE         REASON  VERSION
22/tcp   open  ssh             syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 0f4a03b59f57ffd9cd3997635365db37 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNC6+970n3M250AiR0FqkTC3w6k5zC7iwHQVHcHATn6+DyY1BBWJnQBlntAhhY5YpnKJ3peXeqdouGEeU+NE20+OMrDllyoJolUm60go+bM5bcJA/rMVD4JA2J4l6Xluwexqc9d+vDqK4SO27ycdxVJufTPyEMJ4/37ZIdcsNPdFxQyL9/+0A0pFRz5tq81Zm7PB8A6T2NRe0Cq50lMv853cvGNcMx1Yv3hOZAwy4DyKy4QS2fWoVW/nq+Oc6UZRhTqbeCY7kgj79fuxIbExWSld3En23gSSVYZ5ANV2A4EcE9yqiCAHugbMizdaeRJ5ivnE0un0vPASKMxNlQDPF/
|   256 cbdaa6449a97349fd86d329569cc93dd (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEbXOczH4xup4ZMfTGVRI3DYdldRpXazlf7X7JDGOQH4ImKMh3FxJO5R4GT44loPZGjxqgw04cpRnCFK0DJ+/m8=
|   256 1d768bbeaed28b891d32eacb0ceb7a53 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIM/VWGh77+ZLgP0ziqeos/YQ6k/CJzxVUrRH5kA7e+Jj
80/tcp   open  http            syn-ack nginx 1.14.0 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-favicon: ERROR: Script execution failed (use -d to debug)
|_http-server-header: nginx/1.14.0 (Ubuntu)
| http-robots.txt: 1 disallowed entry 
|_/
| http-title: Site doesn't have a title (text/html; charset=UTF-8).
|_Requested resource was http://10.10.11.55/en-US/account/login?return_to=%2Fen-US%2F
8000/tcp open  http            syn-ack Splunkd httpd
|_http-server-header: Splunkd
| http-title: Site doesn't have a title (text/html; charset=UTF-8).
|_Requested resource was http://10.10.11.55:8000/en-US/account/login?return_to=%2Fen-US%2F
| http-robots.txt: 1 disallowed entry 
|_/
|_http-favicon: Unknown favicon MD5: E60C968E8FF3CC2F4FB869588E83AFC6
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
8089/tcp open  ssl/http        syn-ack Splunkd httpd (free license; remote login disabled)
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Server returned status 401 but no WWW-Authenticate header.
|_http-title: Site doesn't have a title (text/xml; charset=UTF-8).
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Splunkd
| ssl-cert: Subject: commonName=SplunkServerDefaultCert/organizationName=SplunkUser
| Issuer: commonName=SplunkCommonCA/organizationName=Splunk/stateOrProvinceName=CA/countryName=US/emailAddress=support@splunk.com/localityName=San Francisco
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| MD5:   2b3bc2a1bbc0fe827050fa0f1a6f3445
| SHA-1: 6d3308dc5df283707f23813b7bb5dd315bb1505c
| -----BEGIN CERTIFICATE-----
| MIIDMjCCAhoCCQDKwxvgbZblRTANBgkqhkiG9w0BAQsFADB/MQswCQYDVQQGEwJV
| UzELMAkGA1UECAwCQ0ExFjAUBgNVBAcMDVNhbiBGcmFuY2lzY28xDzANBgNVBAoM
| BlNwbHVuazEXMBUGA1UEAwwOU3BsdW5rQ29tbW9uQ0ExITAfBgkqhkiG9w0BCQEW
| EnN1cHBvcnRAc3BsdW5rLmNvbTAeFw0yMTEyMjcwNTAxMDdaFw0yNDEyMjYwNTAx
| MDdaMDcxIDAeBgNVBAMMF1NwbHVua1NlcnZlckRlZmF1bHRDZXJ0MRMwEQYDVQQK
| DApTcGx1bmtVc2VyMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA06sj
| P1jt4gQKBf5Snzrjd52aFR/ciERPxRoZCIWNRC8AXnTH9x+eZR05mU5f3Yw+MVj7
| gq/KKIwOifISTqg3JdtIIlbBrkCwR+4MqZ1XKmncR4Bf7ROQuTq7Po4qvRbXFtx2
| umj/oE1opLyH5iwkgx4zohxmM9LjZEdk1Q+XEgNrzT9rQW3W0IIqnVRw6ycBqLaM
| odGFFvmO/aGqgULIhd7cSED4fRq3em1CHIYRF6ANkywmioBIDnIA2nCezwjK6qZJ
| 1jG50MCsUX6whf5UbQAsLo1VCsNcgyxfoPZmToLs1IXUdMYhZNR4ikEf8dM4Islb
| bdmNeGujU9UsjdmFnQIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQBx2H7BOVrBoqzg
| Nb7BFI6qWnHf/EuaIgoUXQAKoh0zqVVHOfbIUNy8png1/KWhYDZ3h0o3clih2COr
| llkBsqPQGlV7XWhaGDS2gJdwxcgj8fhKYQuIYbUf9Q1C5BcPxBFVW/sVoClbhDn1
| sMfvStkUJk6s6uc1HnfjB0+8OltYlkmCk2eM5MKzP4DHe9d/Jr3cojtT5d3/XqOj
| i83AvyB4MAJKXnU2PFbVGx01ktk8CnlW8lw2Q/V1VRDMc1GdA0YxYDvmWAh2fASo
| sA/Oi//zVqYWKKZ3HcwHaztf0IDZu1OFTH6m7d1XVchAzS8mOOTKSZDOiLIM3RjW
| rgeK2V3r
|_-----END CERTIFICATE-----
8191/tcp open  limnerpressure? syn-ack
| fingerprint-strings: 
|   FourOhFourRequest, GetRequest: 
|     HTTP/1.0 200 OK
|     Connection: close
|     Content-Type: text/plain
|     Content-Length: 85
|_    looks like you are trying to access MongoDB over HTTP on the native driver port.
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
