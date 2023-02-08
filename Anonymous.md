---
Not the hacking group
---

# Anonymous — Writeup

## Overview
### Anonymous — Writeup
### Anonymous — Writeup
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/876a5185c429c9703e625cb48c39637b.png)
![](https://i.imgur.com/KHhJB15.png)
### Pwn
Start Machine
![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Anonymous_emblem.svg/1024px-Anonymous_emblem.svg.png)
Try to get the two flags!  Root the machine and prove your understanding of the fundamentals! This is a virtual machine meant for beginners. Acquiring both flags will require some basic knowledge of Linux and privilege escalation methods.
--------------------------------------------------------------------
_For more information on Linux, check out_ [Learn Linux](https://tryhackme.com/room/zthlinux)
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~]
└─$ rustscan -a 10.10.207.25 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.207.25:139
Open 10.10.207.25:445
Open 10.10.207.25:21
Open 10.10.207.25:22
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-25 13:40 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:40
Completed NSE at 13:40, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:40
Completed NSE at 13:40, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:40
Completed NSE at 13:40, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 13:40
Completed Parallel DNS resolution of 1 host. at 13:40, 0.04s elapsed
DNS resolution of 1 IPs took 0.04s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 13:40
Scanning 10.10.207.25 [4 ports]
Discovered open port 445/tcp on 10.10.207.25
Discovered open port 22/tcp on 10.10.207.25
Discovered open port 21/tcp on 10.10.207.25
Discovered open port 139/tcp on 10.10.207.25
Completed Connect Scan at 13:40, 0.20s elapsed (4 total ports)
Initiating Service scan at 13:40
Scanning 4 services on 10.10.207.25
Completed Service scan at 13:40, 12.08s elapsed (4 services on 1 host)
NSE: Script scanning 10.10.207.25.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:40
NSE: [ftp-bounce 10.10.207.25:21] PORT response: 500 Illegal PORT command.
Completed NSE at 13:40, 8.45s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:40
Completed NSE at 13:40, 1.43s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:40
Completed NSE at 13:40, 0.00s elapsed
Nmap scan report for 10.10.207.25
Host is up, received user-set (0.20s latency).
Scanned at 2023-02-25 13:40:04 EST for 23s

PORT    STATE SERVICE     REASON  VERSION
21/tcp  open  ftp         syn-ack vsftpd 2.0.8 or later
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
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxrwxrwx    2 111      113          4096 Jun 04  2020 scripts [NSE: writeable]
22/tcp  open  ssh         syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 8bca21621c2b23fa6bc61fa813fe1c68 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDCi47ePYjDctfwgAphABwT1jpPkKajXoLvf3bb/zvpvDvXwWKnm6nZuzL2HA1veSQa90ydSSpg8S+B8SLpkFycv7iSy2/Jmf7qY+8oQxWThH1fwBMIO5g/TTtRRta6IPoKaMCle8hnp5pSP5D4saCpSW3E5rKd8qj3oAj6S8TWgE9cBNJbMRtVu1+sKjUy/7ymikcPGAjRSSaFDroF9fmGDQtd61oU5waKqurhZpre70UfOkZGWt6954rwbXthTeEjf+4J5+gIPDLcKzVO7BxkuJgTqk4lE9ZU/5INBXGpgI5r4mZknbEPJKS47XaOvkqm9QWveoOSQgkqdhIPjnhD
|   256 9589a412e2e6ab905d4519ff415f74ce (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPjHnAlR7sBuoSM2X5sATLllsFrcUNpTS87qXzhMD99aGGzyOlnWmjHGNmm34cWSzOohxhoK2fv9NWwcIQ5A/ng=
|   256 e12a96a4ea8f688fcc74b8f0287270cd (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDHIuFL9AdcmaAIY7u+aJil1covB44FA632BSQ7sUqap
139/tcp open  netbios-ssn syn-ack Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn syn-ack Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
Service Info: Host: ANONYMOUS; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb2-time: 
|   date: 2023-02-25T18:40:18
|_  start_date: N/A
| nbstat: NetBIOS name: ANONYMOUS, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
| Names:
|   ANONYMOUS<00>        Flags: <unique><active>
|   ANONYMOUS<03>        Flags: <unique><active>
|   ANONYMOUS<20>        Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|   WORKGROUP<1e>        Flags: <group><active>
| Statistics:
|   0000000000000000000000000000000000
|   0000000000000000000000000000000000
|_  0000000000000000000000000000
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 3606/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 48304/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 32668/udp): CLEAN (Failed to receive data)
|   Check 4 (port 62060/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: anonymous
|   NetBIOS computer name: ANONYMOUS\x00
|   Domain name: \x00
|   FQDN: anonymous
|_  System time: 2023-02-25T18:40:18+00:00
|_clock-skew: mean: 0s, deviation: 1s, median: 0s

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:40
Completed NSE at 13:40, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:40
Completed NSE at 13:40, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:40
Completed NSE at 13:40, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.80 seconds

┌──(witty㉿kali)-[~]
└─$ ftp 10.10.207.25        
Connected to 10.10.207.25.
220 NamelessOne's FTP Server!
Name (10.10.207.25:witty): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -la
229 Entering Extended Passive Mode (|||31255|)
150 Here comes the directory listing.
drwxr-xr-x    3 65534    65534        4096 May 13  2020 .
drwxr-xr-x    3 65534    65534        4096 May 13  2020 ..
drwxrwxrwx    2 111      113          4096 Jun 04  2020 scripts
226 Directory send OK.
ftp> cd scripts
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||40045|)
150 Here comes the directory listing.
drwxrwxrwx    2 111      113          4096 Jun 04  2020 .
drwxr-xr-x    3 65534    65534        4096 May 13  2020 ..
-rwxr-xrwx    1 1000     1000          314 Jun 04  2020 clean.sh
-rw-rw-r--    1 1000     1000         1161 Feb 25 18:43 removed_files.log
-rw-r--r--    1 1000     1000           68 May 12  2020 to_do.txt
226 Directory send OK.
ftp> more to_do.txt
I really need to disable the anonymous login...it's really not safe
ftp> more removed_files.log
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
Running cleanup script:  nothing to delete
ftp> more clean.sh
#!/bin/bash

tmp_files=0
echo $tmp_files
if [ $tmp_files=0 ]
then
        echo "Running cleanup script:  nothing to delete" >> /var/ftp/scripts/remo
ved_files.log
else
    for LINE in $tmp_files; do
        rm -rf /tmp/$LINE && echo "$(date) | Removed file /tmp/$LINE" >> /var/ftp/
scripts/removed_files.log;done
fi

┌──(witty㉿kali)-[~]
└─$ smbclient -N -L 10.10.207.25                                    

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	pics            Disk      My SMB Share Directory for Pics
	IPC$            IPC       IPC Service (anonymous server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------
	WORKGROUP            ANONYMOUS

┌──(witty㉿kali)-[~]
└─$ smbclient -N \\\\10.10.207.25\\pics
Try "help" to get a list of possible commands.
smb: \> ls -la
NT_STATUS_NO_SUCH_FILE listing \-la
smb: \> ls
  .                                   D        0  Sun May 17 07:11:34 2020
  ..                                  D        0  Wed May 13 21:59:10 2020
  corgo2.jpg                          N    42663  Mon May 11 20:43:42 2020
  puppos.jpeg                         N   265188  Mon May 11 20:43:42 2020

		20508240 blocks of size 1024. 13306804 blocks available
smb: \> mget *
Get file corgo2.jpg? yes
getting file \corgo2.jpg of size 42663 as corgo2.jpg (33.2 KiloBytes/sec) (average 33.2 KiloBytes/sec)
Get file puppos.jpeg? yes
getting file \puppos.jpeg of size 265188 as puppos.jpeg (157.2 KiloBytes/sec) (average 103.6 KiloBytes/sec)
smb: \> exit

                                                                                  
┌──(witty㉿kali)-[~]
└─$ file corgo2.jpg         
corgo2.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 800x533, components 3
                                                                                  
┌──(witty㉿kali)-[~]
└─$ file puppos.jpeg 
puppos.jpeg: JPEG image data, Exif standard: [TIFF image data, little-endian, direntries=19, height=3744, bps=242, PhotometricInterpretation=RGB, description=Three Pembroke Welsh Corgis side by side outdoors. Approved by Denise Flaim September 2018 and Susan Sprung., manufacturer=Canon, model=Canon EOS 5D Mark II, orientation=upper-left, width=5616], progressive, precision 8, 600x400, components 3

┌──(witty㉿kali)-[~]
└─$ ftp 10.10.207.25
Connected to 10.10.207.25.
220 NamelessOne's FTP Server!
Name (10.10.207.25:witty): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||21690|)
150 Here comes the directory listing.
drwxrwxrwx    2 111      113          4096 Jun 04  2020 scripts
226 Directory send OK.
ftp> cd scripts
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||54536|)
150 Here comes the directory listing.
-rwxr-xrwx    1 1000     1000          314 Jun 04  2020 clean.sh
-rw-rw-r--    1 1000     1000         3913 Feb 25 19:47 removed_files.log
-rw-r--r--    1 1000     1000           68 May 12  2020 to_do.txt
226 Directory send OK.
ftp> get clean.sh
local: clean.sh remote: clean.sh
229 Entering Extended Passive Mode (|||52682|)
