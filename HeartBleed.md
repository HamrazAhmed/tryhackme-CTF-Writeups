---
SSL issues are still lurking in the wild. Can you exploit this web servers OpenSSL?
---

# HeartBleed — Writeup

## Overview
### HeartBleed — Writeup
### HeartBleed — Writeup
![|222](https://tryhackme-images.s3.amazonaws.com/room-icons/82db1237966d14e10bf2c66690989283.png)
### Background Information
Introduction to Heartbleed and SSL/TLS
On the internet today, most web servers are configured to use SSL/TLS. SSL(secure socket layer) is just a predecessor to TLS(transport layer security). The most common versions are TLS 1.2 and TLS 1.3(which has recently been released). Configuring a web server to use TLS means that all communication from that particular server to a client will be encrypted; any malicious third party that has access to this traffic will not be able to understand/decrypt the traffic, and they also will not be able to modify the traffic. To learn more about how the TLS connections are established, check [1.2](https://tls.ulfheim.net/) and [1.3](https://tls13.ulfheim.net/) out.
Heartbleed is a bug due to the implementation in the OpenSSL library from versions 1.0.1 to 1.0.1f(which is very widely used). It allows a user to access memory on the server(which they usually wouldn't have access to). This in turn allows a malicious user to access different kinds of information(that they wouldn't usually have access to due to the encryption and integrity provided by TLS) including:
server private key
confidential data like usernames, passwords and other personal information
Analysing the Bug
The implementation error occurs in the heartbeat message that is used by OpenSSL to keep a connection alive even when no data is sent. A mechanism like this is important because if a connection dies/resets quite often, it would be expensive to set up the TLS aspect of the connection again; this affects the latency across the internet and it would make using services slow for users. A heartbeat message sent by one end of the connection contains random data and the length of the data, and this exact data is sent back when received by the other end of the connection. When the server retrieves this message from the client here's what it does:
The server constructs a pointer(memory location) to the heartbeat record
It then copies the length of the data sent by a user into a variable(called payload)
The length of this data is unchecked
The server then allocates memory in the form of:
1 + 2 + payload + padding(this can be maximum of 1 + 2 + 65535 + 16)
The server then creates another pointer(bp) to access this memory
The server then copies payload number of bytes from data sent by the user to the bp pointer
The server sends the data contained in the bp pointers to the user
With this, you can see that the user controls the amount and length of data they send over. If the user does not send over any data(where the length is 0), it means that the server will copy arbitrary memory into the new pointer(which is how it can access secret information on the server). When retrieving data this way, the data can be different with different responses as the memory on the server will change.
Remediation
To ensure that arbitrary data from the server isn’t copied and sent to a user, the server needs to check the length of the heartbeat message:
The server needs to check that the length of the heartbeat message sent by the user isn’t 0
The server needs to check the the length doesn’t exceed the specified length of the variable that holds the data
References:
http://heartbleed.com/
https://www.seancassidy.me/diagnosis-of-the-openssl-heartbleed-bug.html
https://stackabuse.com/heartbleed-bug-explained/
Read above and ensure you have a good understanding of how the Heartbleed vulnerability works.
### Protecting Data In Transit
In this task, you need to obtain a flag using a very well known vulnerability. Make sure you pay attention to all the information and errors displayed. Pay particular attention to how web servers are configured.
It may take between 3-4 minutes for the server to deploy and configure. Please be patient.
https://&lt;ip>
```text
https://34.244.244.152/

My friend really like this Heartbleed song - I think you all will like it too
```

## Enumeration
```text
┌──(kali㉿kali)-[~]
└─$ nmap -sV --script vuln 34.244.244.152  
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-11 17:32 EDT
Nmap scan report for ec2-34-244-244-152.eu-west-1.compute.amazonaws.com (34.244.244.152)
Host is up (0.19s latency).
Not shown: 998 filtered tcp ports (no-response)
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 7.4 (protocol 2.0)
443/tcp open  ssl/http nginx 1.15.7
|_http-server-header: nginx/1.15.7
| ssl-ccs-injection: 
|   VULNERABLE:
|   SSL/TLS MITM vulnerability (CCS Injection)
|     State: VULNERABLE
|     Risk factor: High
|       OpenSSL before 0.9.8za, 1.0.0 before 1.0.0m, and 1.0.1 before 1.0.1h
|       does not properly restrict processing of ChangeCipherSpec messages,
|       which allows man-in-the-middle attackers to trigger use of a zero
|       length master key in certain OpenSSL-to-OpenSSL communications, and
|       consequently hijack sessions or obtain sensitive information, via
|       a crafted TLS handshake, aka the "CCS Injection" vulnerability.
|           
|     References:
|       http://www.cvedetails.com/cve/2014-0224
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0224
|_      http://www.openssl.org/news/secadv_20140605.txt
| ssl-heartbleed: 
|   VULNERABLE:
|   The Heartbleed Bug is a serious vulnerability in the popular OpenSSL cryptographic software library. It allows for stealing information intended to be protected by SSL/TLS encryption.
|     State: VULNERABLE
|     Risk factor: High
|       OpenSSL versions 1.0.1 and 1.0.2-beta releases (including 1.0.1f and 1.0.2-beta1) of OpenSSL are affected by the Heartbleed bug. The bug allows for reading memory of systems protected by the vulnerable OpenSSL versions and could allow for disclosure of otherwise encrypted confidential information as well as the encryption keys themselves.
|           
|     References:
|       http://www.openssl.org/news/secadv_20140407.txt 
|       http://cvedetails.com/cve/2014-0160/
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0160
| http-vuln-cve2011-3192: 
|   VULNERABLE:
|   Apache byterange filter DoS
|     State: VULNERABLE
|     IDs:  BID:49303  CVE:CVE-2011-3192
|       The Apache web server is vulnerable to a denial of service attack when numerous
|       overlapping byte ranges are requested.
|     Disclosure date: 2011-08-19
|     References:
|       https://www.tenable.com/plugins/nessus/55976
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2011-3192
|       https://seclists.org/fulldisclosure/2011/Aug/175
|_      https://www.securityfocus.com/bid/49303
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 304.93 seconds
zsh: segmentation fault  nmap -sV --script vuln 34.244.244.152

using metasploit (heartbleed)
```
```text
┌──(kali㉿kali)-[~]
