---
A CTF room based on the old-time survival horror game, Resident Evil. Can you survive until the end?
---

# BioHazard — Writeup

## Overview
### BioHazard — Writeup
### BioHazard — Writeup
![|333](https://tryhackme-images.s3.amazonaws.com/room-icons/72aca9d285c3156a05b34b7f6cc67ae6.png)

## Enumeration
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.128.211 --ulimit 5000 -b 65535 -- -A 
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
[~] Automatically increasing ulimit value to 5000.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.128.211:22
Open 10.10.128.211:21
Open 10.10.128.211:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-17 21:16 EDT
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 21:16
Completed NSE at 21:16, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 21:16
Completed NSE at 21:16, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 21:16
Completed NSE at 21:16, 0.00s elapsed
Initiating Ping Scan at 21:16
Scanning 10.10.128.211 [2 ports]
Completed Ping Scan at 21:16, 0.42s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 21:16
Completed Parallel DNS resolution of 1 host. at 21:16, 0.02s elapsed
DNS resolution of 1 IPs took 0.04s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 21:16
Scanning 10.10.128.211 [3 ports]
Discovered open port 22/tcp on 10.10.128.211
Discovered open port 80/tcp on 10.10.128.211
Discovered open port 21/tcp on 10.10.128.211
Completed Connect Scan at 21:16, 0.27s elapsed (3 total ports)
Initiating Service scan at 21:16
Scanning 3 services on 10.10.128.211
Completed Service scan at 21:16, 6.51s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.128.211.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 21:16
Completed NSE at 21:16, 8.87s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 21:16
Completed NSE at 21:16, 2.15s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 21:16
Completed NSE at 21:16, 0.00s elapsed
Nmap scan report for 10.10.128.211
Host is up, received conn-refused (0.37s latency).
Scanned at 2022-09-17 21:16:34 EDT for 18s

PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c9:03:aa:aa:ea:a9:f1:f4:09:79:c0:47:41:16:f1:9b (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDM1/tmq8Lrur25evbyyI7/+nxDlhbVbMMiRfz5a0eI7Sq9yODJGCVNMPJGKOwtgA/BlPi7V3TKyYJVeH1QOzP8mPLVgfYom6ovelJiLiR6VrO4dqxx+G3ir+tj/OOSc4MpmdnqCvQKtAeJ4e5bbWakFihXyy14yi++oOzqp2VDlqMNN+d2k0uSAx1rDbngwP3UvRfE1E1TaSYhljnb9kvWRxBABhpdkUjbcRLwxBAQFBm9Vm+yQYPurC9YJ1BUlJzOFesYnbS27bG1vVCcuPQN3YjcljVCXBdd0qIvZdYlez4+mVUcJJh1iWl83sfgo+wZRmfHsedjdL1eWNrkt+ed
|   256 2e:1d:83:11:65:03:b4:78:e9:6d:94:d1:3b:db:f4:d6 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNy83txF27peDYxMhrPqfipXwZtBNY9H4fww7f2FRCkt09tEcp5f5BKhOE4cNo033XYpmaowy1r4qgFpIqKjf64=
|   256 91:3d:e4:4f:ab:aa:e2:9e:44:af:d3:57:86:70:bc:39 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMhTmk6F06eyLfM0j07nUcnqMqGdgOfFqsp3eLdbwwn0
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-methods: 
|_  Supported Methods: POST OPTIONS HEAD GET
|_http-title: Beginning of the end
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 21:16
Completed NSE at 21:16, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 21:16
Completed NSE at 21:16, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 21:16
Completed NSE at 21:16, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.57 seconds
```
How many open ports?
*3*
What is the team name in operation
*STARS alpha team* (found in home page footer)
### The Mansion
Collect all necessary items and advanced to the next level. The format of the Item flag:
Item_name{32 character}
Some of the doors are locked. Use the item flag to unlock the door.
Tips: It is better to record down all the information inside a notepad
What is the emblem flag
*emblem{fec832623ea498e20bf4fe1821d58727}*
What is the lock pick flag
*lock_pick{037b35e2ff90916a9abf99129c8e1837}*
What is the music sheet flag
*music_sheet{362d72deaf65f5bdc63daece6a1f676e}* (base32)
What is the gold emblem flag
*gold_emblem{58a8c41a9d08b8a4e38d02a4d7ff4843}*
![[Pasted image 20220917211219.png]]
![[Pasted image 20220917211731.png]]
What is the shield key flag
*shield_key{48a7a9227cd7eb89f0a062590798cbac}*
![[Pasted image 20220917204929.png]]
What is the blue gem flag
*blue_jewel{e1d457e96cac640f863ec7bc475d48aa}*
crest 1 + crest2 + crest3 +crest4
S0pXRkVVS0pKQkxIVVdTWUpFM0VTUlk9 + GVFWK5KHK5WTGTCILE4DKY3DNN4GQQRTM5AVCTKE + MDAxMTAxMTAgMDAxMTAwMTEgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAwMTEgMDAxMDAwMDAgMDAxMTAxMDAgMDExMDAxMDAgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAxMTAgMDAxMDAwMDAgMDAxMTAxMDAgMDAxMTEwMDEgMDAxMDAwMDAgMDAxMTAxMDAgMDAxMTEwMDAgMDAxMDAwMDAgMDAxMTAxMTAgMDExMDAwMTEgMDAxMDAwMDAgMDAxMTAxMTEgMDAxMTAxMTAgMDAxMDAwMDAgMDAxMTAxMTAgMDAxMTAxMDAgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTAxMTAgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTEwMDEgMDAxMDAwMDAgMDAxMTAxMTAgMDExMDAwMDEgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTEwMDEgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTAxMTEgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAxMDEgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAwMDAgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTEwMDAgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAwMTAgMDAxMDAwMDAgMDAxMTAxMTAgMDAxMTEwMDA= + gSUERauVpvKzRpyPpuYz66JDmRTbJubaoArM6CAQsnVwte6zF9J4GGYyun3k5qM9ma4s
crest 1:S0pXRkVVS0pKQkxIVVdTWUpFM0VTUlk9 (E: 2x, 14 letters)
crest 2:GVFWK5KHK5WTGTCILE4DKY3DNN4GQQRTM5AVCTKE (E: 2x, 18 letters)
crest 3:
MDAxMTAxMTAgMDAxMTAwMTEgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAwMTEgMDAxMDAwMDAgMDAxMTAxMDAgMDExMDAxMDAgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAxMTAgMDAxMDAwMDAgMDAxMTAxMDAgMDAxMTEwMDEgMDAxMDAwMDAgMDAxMTAxMDAgMDAxMTEwMDAgMDAxMDAwMDAgMDAxMTAxMTAgMDExMDAwMTEgMDAxMDAwMDAgMDAxMTAxMTEgMDAxMTAxMTAgMDAxMDAwMDAgMDAxMTAxMTAgMDAxMTAxMDAgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTAxMTAgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTEwMDEgMDAxMDAwMDAgMDAxMTAxMTAgMDExMDAwMDEgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTEwMDEgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTAxMTEgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAxMDEgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAwMDAgMDAxMDAwMDAgMDAxMTAxMDEgMDAxMTEwMDAgMDAxMDAwMDAgMDAxMTAwMTEgMDAxMTAwMTAgMDAxMDAwMDAgMDAxMTAxMTAgMDAxMTEwMDA= (E: 3x, 19 letters)
crest 4: gSUERauVpvKzRpyPpuYz66JDmRTbJubaoArM6CAQsnVwte6zF9J4GGYyun3k5qM9ma4s (E: 2x, 17 letters)
![[Pasted image 20220917212918.png]]
RlRQIHVzZXI6IG
![[Pasted image 20220917213030.png]]
h1bnRlciwgRlRQIHBh
![[Pasted image 20220917213233.png]]
c3M6IHlvdV9jYW50X2h
![[Pasted image 20220917213333.png]]
pZGVfZm9yZXZlcg==
now:
RlRQIHVzZXI6IGh1bnRlciwgRlRQIHBhc3M6IHlvdV9jYW50X2hpZGVfZm9yZXZlcg==
![[Pasted image 20220917213449.png]]
FTP user: hunter, FTP pass: you_cant_hide_forever
What is the FTP username
*hunter*
What is the FTP password
*you_cant_hide_forever*
### The guard house
After gaining access to the FTP server, you need to solve another puzzle.
```text
┌──(kali㉿kali)-[~/Downloads/biohazard]
└─$ ftp 10.10.128.211
Connected to 10.10.128.211.
220 (vsFTPd 3.0.3)
Name (10.10.128.211:kali): hunter
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||46709|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0            7994 Sep 19  2019 001-key.jpg
-rw-r--r--    1 0        0            2210 Sep 19  2019 002-key.jpg
-rw-r--r--    1 0        0            2146 Sep 19  2019 003-key.jpg
-rw-r--r--    1 0        0             121 Sep 19  2019 helmet_key.txt.gpg
-rw-r--r--    1 0        0             170 Sep 20  2019 important.txt
226 Directory send OK.
ftp> get *
local: * remote: *
229 Entering Extended Passive Mode (|||8828|)
550 Failed to open file.
ftp> get all*
local: all* remote: all*
229 Entering Extended Passive Mode (|||51104|)
550 Failed to open file.
ftp> help
Commands may be abbreviated.  Commands are:

!               epsv6           mget            preserve        sendport
```
```text
$               exit            mkdir           progress        set
account         features        mls             prompt          site
append          fget            mlsd            proxy           size
ascii           form            mlst            put             sndbuf
bell            ftp             mode            pwd             status
binary          gate            modtime         quit            struct
bye             get             more            quote           sunique
case            glob            mput            rate            system
cd              hash            mreget          rcvbuf          tenex
cdup            help            msend           recv            throttle
chmod           idle            newer           reget           trace
close           image           nlist           remopts         type
cr              lcd             nmap            rename          umask
debug           less            ntrans          reset           unset
delete          lpage           open            restart         usage
dir             lpwd            page            rhelp           user
disconnect      ls              passive         rmdir           verbose
edit            macdef          pdir            rstatus         xferbuf
epsv            mdelete         pls             runique         ?
epsv4           mdir            pmlsd           send
ftp> mget *
mget 001-key.jpg [anpqy?]? 
229 Entering Extended Passive Mode (|||16705|)
150 Opening BINARY mode data connection for 001-key.jpg (7994 bytes).
100% |**************************************|  7994        1.13 MiB/s    00:00 ETA
226 Transfer complete.
7994 bytes received in 00:00 (37.63 KiB/s)
mget 002-key.jpg [anpqy?]? 
229 Entering Extended Passive Mode (|||58378|)
150 Opening BINARY mode data connection for 002-key.jpg (2210 bytes).
100% |**************************************|  2210        2.31 MiB/s    00:00 ETA
226 Transfer complete.
2210 bytes received in 00:00 (10.62 KiB/s)
mget 003-key.jpg [anpqy?]? 
229 Entering Extended Passive Mode (|||22864|)
150 Opening BINARY mode data connection for 003-key.jpg (2146 bytes).
100% |**************************************|  2146       12.10 MiB/s    00:00 ETA
226 Transfer complete.
2146 bytes received in 00:00 (10.50 KiB/s)
mget helmet_key.txt.gpg [anpqy?]? 
229 Entering Extended Passive Mode (|||19082|)
150 Opening BINARY mode data connection for helmet_key.txt.gpg (121 bytes).
100% |**************************************|   121        1.78 KiB/s    00:00 ETA
226 Transfer complete.
121 bytes received in 00:00 (0.44 KiB/s)
mget important.txt [anpqy?]? 
229 Entering Extended Passive Mode (|||50083|)
150 Opening BINARY mode data connection for important.txt (170 bytes).
100% |**************************************|   170      779.41 KiB/s    00:00 ETA
226 Transfer complete.
170 bytes received in 00:00 (0.82 KiB/s)
ftp> ls
229 Entering Extended Passive Mode (|||38894|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0            7994 Sep 19  2019 001-key.jpg
-rw-r--r--    1 0        0            2210 Sep 19  2019 002-key.jpg
-rw-r--r--    1 0        0            2146 Sep 19  2019 003-key.jpg
-rw-r--r--    1 0        0             121 Sep 19  2019 helmet_key.txt.gpg
-rw-r--r--    1 0        0             170 Sep 20  2019 important.txt
226 Directory send OK.
ftp> exit
221 Goodbye.
```
Where is the hidden directory mentioned by Barry
```text
┌──(kali㉿kali)-[~/Downloads/biohazard]
└─$ ls
001-key.jpg  002-key.jpg  003-key.jpg  helmet_key.txt.gpg  important.txt
```
```text
┌──(kali㉿kali)-[~/Downloads/biohazard]
└─$ cat important.txt 
Jill,

I think the helmet key is inside the text file, but I have no clue on decrypting stuff. Also, I come across a /hidden_closet/ door but it was locked.

From,
Barry
```
*/hidden_closet/*
Password for the encrypted file
Three picture, three hints: hide, comment and walk away
```text
┌──(kali㉿kali)-[~/Downloads/biohazard]
└─$ binwalk 001-key.jpg 002-key.jpg 003-key.jpg 

Scan Time:     2022-09-17 22:40:52
Target File:   /home/kali/Downloads/biohazard/001-key.jpg
MD5 Checksum:  076b6a86ba92c75d366f0a18b505dcf8
Signatures:    411

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01

Scan Time:     2022-09-17 22:40:52
Target File:   /home/kali/Downloads/biohazard/002-key.jpg
MD5 Checksum:  060af11c5617fbc4fba1760f0dd52a0d
Signatures:    411

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01

Scan Time:     2022-09-17 22:40:52
Target File:   /home/kali/Downloads/biohazard/003-key.jpg
MD5 Checksum:  5c407556b6956ba74cda5ce98f8acf08
Signatures:    411

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
1930          0x78A           Zip archive data, at least v2.0 to extract, uncompressed size: 14, name: key-003.txt
2124          0x84C           End of Zip archive, footer length: 22
```
```text
┌──(kali㉿kali)-[~/Downloads/biohazard]
└─$ unzip 003-key.jpg 
Archive:  003-key.jpg
warning [003-key.jpg]:  1930 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: key-003.txt
```
```text
┌──(kali㉿kali)-[~/Downloads/biohazard]
└─$ cat key-003.txt  
3aXRoX3Zqb2x0  key3
```
```text
┌──(kali㉿kali)-[~/Downloads/biohazard]
└─$ strings 001-key.jpg 002-key.jpg 
JFIF

"*%%*424DD\

"*%%*424DD\
$3br
%&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
        #3R
&'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz
*Pr+6
)XG0
QPOu
^j2]
~Rpx
f$n[
3s3uc]D`A
*H=E%ij
J8t8"
Ro9
Bri(
rqZ`
e=FM
77*{)
70_SL
vg[[fb@8
1c1DD
Pj*@
RsZ:
`:Wk@
FUu*
.!GF
%FO=jJ
G#kvaX7VsZ
nBx"
 xfN
SUu-
|<V{P
08*r
QM9b#P
&?QVRB:V,d
">?x
Zz? >}
o}m$2
Vm.^
OSLf
dnG?
mZ[@
i\lc
iyua:\
Vp>`}Z
<',kgp^
RWIu
z+DG+M
k)V*
*I&#
,v`/l
.\c~>n
APQE
w)yau$
'>Y?2
5KSMl
?gI6
Eq5f
0Q\D
Mm#E<M
X.,u8
:v      x
>vgvw9f$
4=.]N
B^/C
E,S(h
AaS,
b]7&N
)qcs
b[yVD# 
[yqsv
<),Q
zM<@
!d?l
_Di>"
!|zU
O+fI
JFIF
5fYmVfZGVzdHJveV9

"*%%*424DD\

"*%%*424DD\
5Zs5
az8C
C%(KH\
ftkI
B}-*J
'ttT
uJ@2
!1Aaq
"2Q 0#Bbr
l)YWH]E
}VR7
p*qJ
v4NM
U!.#
! "AQ
#2Raq
?1>o
I^(h
+M_M
Z6"=
,hfb
Yx$k3
12Ra

5fYmVfZGVzdHJveV9 key 2

https://futureboy.us/stegano/decode.pl upload key01.png

cGxhbnQ0Ml9jYW key 1

key 1 + key 2 + key 3 = cGxhbnQ0Ml9jYW5fYmVfZGVzdHJveV93aXRoX3Zqb2x0

plant42_can_be_destroy_with_vjolt
```
*plant42_can_be_destroy_with_vjolt*
What is the helmet key flag
key 1 + key 2 + key 3 is not enough. You need to do something
![[Pasted image 20220917214959.png]]
```text
┌──(kali㉿kali)-[~/Downloads/biohazard]
└─$ gpg -d helmet_key.txt.gpg                
gpg: AES256.CFB encrypted data
gpg: encrypted with 1 passphrase
helmet_key{458493193501d2b94bbab2e727f8db4b}
```
*helmet_key{458493193501d2b94bbab2e727f8db4b}*
### The Revisit
Done with the puzzle? There are places you have explored before but yet to access.
![[Pasted image 20220917215239.png]]
What is the SSH login username
You missed a room yep study room :)
enter helmet flag then download
```text
┌──(kali㉿kali)-[~/Downloads/biohazard]
└─$ ls
001-key.jpg  003-key.jpg  helmet_key.txt.gpg  key-003.txt
002-key.jpg  doom.tar.gz  important.txt
