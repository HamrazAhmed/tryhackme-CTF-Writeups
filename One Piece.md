# One Piece — Writeup

## Overview
### One Piece — Writeup
### One Piece — Writeup
----
A CTF room based on the wonderful manga One Piece. Can you become the Pirate King?
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/ee72b0ca17cd6185e03ed809ba766698.jpeg)
Start Machine
Welcome to the One Piece room.
Your dream is to find the One Piece and hence to become the Pirate King.
Once the VM is deployed, you will be able to enter a World full of Pirates.
Please notice that pirates do not play fair. They can create rabbit holes to trap you.
This room may be a bit different to what you are used to:
- Required skills to perform the intended exploits are pretty basic.
- However, solving the (let's say) "enigmas" to know what you need to do may be trickier.
This room is some sort of game, some sort of puzzle.
> **_Please note that if you are currently reading/watching One Piece and if you did not finish Zou arc, you will get spoiled during this room._**
Answer the questions below
Deploy the machine and hoist the sails
Completed
### Task 2  Road Poneglyphs
In order to reach Laugh Tale, the island where the One Piece is located, you must collect the 4 Road Poneglyphs.
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads/mnemonic/backups/Mnemonic]
└─$ rustscan -a 10.10.220.152 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.220.152:21
Open 10.10.220.152:22
Open 10.10.220.152:80
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
Scanning 10.10.220.152 [3 ports]
Discovered open port 22/tcp on 10.10.220.152
Discovered open port 80/tcp on 10.10.220.152
Discovered open port 21/tcp on 10.10.220.152
Completed Connect Scan (3 total ports)
Initiating Service scan
Scanning 3 services on 10.10.220.152
Completed Service scan (3 services on 1 host)
NSE: Script scanning 10.10.220.152.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
NSE: [ftp-bounce 10.10.220.152:21] PORT response: 500 Illegal PORT command.
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.220.152
Host is up, received user-set (0.19s latency).

PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0             187 Jul 26  2020 welcome.txt
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
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 011818f9b78ac36c7f922d939055a129 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC45MSZ6fV/xyKjd0Vlj750dJSO5TPl1lrNfd+t+qc4LIKnaMoUsyIuxlnTOSQ0yHhGCxRYaDheybyGr1JqQrFazro9bL5cr3o0LQYLgTWbTcVAgkByqDvblrqUj1c6O4R0Z3BoppqzBgXIsUJFw96HAiYzVJCh9RN2rGnAHmqy8lIS/Z56pFlmiEOc3/W1ccnA/ABAIWkX25Kpxz+QE1eMEWEswLG57qmG8nt0qkOT6hQ9sskVW/ADnUmY3rO/dsP7TXh/IvI1slb6HALUlQXXfGUp/2CwOS7SfIthom8HJ3s7STVVOiAQM6xw6USA9QFLObcUSV0qHpXzJnyQtqtl
|   256 cc0218a9b52b49e45b77f96ec2dbc90d (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLQ8y5fOAYcijtTXLprC5JojtRJvMIvbUGGFTMN5eYol3XZucpVKnt/fyLV/5x1jWXsnQixuE2QMCJ6hNRGwHgw=
|   256 b85272e62ad57e563d167bbc518c7b2a (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIWb4BgTYBRRA6bswNkUVwbviPydKMyyWsLyspHwzc/B
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-title: New World
| http-methods: 
|_  Supported Methods: HEAD GET POST OPTIONS
|_http-favicon: Unknown favicon MD5: C31581B251EA41386CB903FC27B37692
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

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
Nmap done: 1 IP address (1 host up) scanned in 14.98 seconds

┌──(witty㉿kali)-[~/Downloads/mnemonic/backups]
└─$ ftp 10.10.220.152
Connected to 10.10.220.152.
220 (vsFTPd 3.0.3)
Name (10.10.220.152:witty): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -lah
229 Entering Extended Passive Mode (|||16301|)
150 Here comes the directory listing.
drwxr-xr-x    3 0        0            4096 Jul 26  2020 .
drwxr-xr-x    3 0        0            4096 Jul 26  2020 ..
drwxr-xr-x    2 0        0            4096 Jul 26  2020 .the_whale_tree
-rw-r--r--    1 0        0             187 Jul 26  2020 welcome.txt
226 Directory send OK.
ftp> mget *
mget welcome.txt [anpqy?]? yes
229 Entering Extended Passive Mode (|||53377|)
150 Opening BINARY mode data connection for welcome.txt (187 bytes).
100% |*********************************|   187       66.91 KiB/s    00:00 ETA
226 Transfer complete.
187 bytes received in 00:00 (0.83 KiB/s)
ftp> cd .the_whale_tree
250 Directory successfully changed.
ftp> ls -lah
229 Entering Extended Passive Mode (|||11907|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jul 26  2020 .
drwxr-xr-x    3 0        0            4096 Jul 26  2020 ..
-rw-r--r--    1 0        0            8652 Jul 26  2020 .road_poneglyph.jpeg
-rw-r--r--    1 0        0            1147 Jul 26  2020 .secret_room.txt
226 Directory send OK.
ftp> mget *
ftp> get .road_poneglyph.jpeg
local: .road_poneglyph.jpeg remote: .road_poneglyph.jpeg
229 Entering Extended Passive Mode (|||51738|)
150 Opening BINARY mode data connection for .road_poneglyph.jpeg (8652 bytes).
100% |*********************************|  8652        4.55 MiB/s    00:00 ETA
226 Transfer complete.
8652 bytes received in 00:00 (42.78 KiB/s)
ftp> get .secret_room.txt
local: .secret_room.txt remote: .secret_room.txt
229 Entering Extended Passive Mode (|||8519|)
150 Opening BINARY mode data connection for .secret_room.txt (1147 bytes).
100% |*********************************|  1147       11.88 MiB/s    00:00 ETA
226 Transfer complete.
1147 bytes received in 00:00 (5.72 KiB/s)
ftp> exit
221 Goodbye.

┌──(witty㉿kali)-[~/Downloads/mnemonic/backups]
└─$ cat welcome.txt 
Welcome to Zou. It is an island located on the back of a massive, millennium-old elephant named Zunesha that roams the New World.
Except this, there is not much to say about this island.

┌──(witty㉿kali)-[~/Downloads/mnemonic/backups]
└─$ cat .secret_room.txt
Inuarashi: You reached the center of the Whale, the majestic tree of Zou.
Nekomamushi: We have hidden this place for centuries.
Inuarashi: Indeed, it holds a secret.
Nekomamushi: Do you see this red stele ? This is a Road Poneglyph.
Luffy: A Road Poneglyph ??
Inuarashi: There are four Road Poneglyphs around the world. Each of them gives one of the key to reach Laugh Tale and to find the One Piece.
Luffy: The One Piece ?? That's my dream ! I will find it and I will become the Pirate King !!!
Nekomamushi: A lot have tried but only one succeeded over the centuries, Gol D Roger, the former Pirate King.
Inuarashi: It is commonly known that both Emperors, Big Mom and Kaido, own a Road Poneglyph but no one knows where is the last one.
Nekomamushi: The other issue is the power of Big Mom and Kaido, they are Emperor due to their strength, you won't be able to take them down easily.
Luffy: I will show them, there can be only one Pirate King and it will be me !!
Inuarashi: There is another issue regarding the Road Poneglyph.
Nekomamushi: They are written in an ancient language and a very few people around the world can actually read them. 

┌──(witty㉿kali)-[~/Downloads/mnemonic/backups]
└─$ steghide extract -sf .road_poneglyph.jpeg 
Enter passphrase: 
wrote extracted data to "road_poneglyphe1.txt".
                                                                              
┌──(witty㉿kali)-[~/Downloads/mnemonic/backups]
└─$ cat road_poneglyphe1.txt 
FUWS2LJNEAWS2LJNFUQC4LJNFUWSALRNFUWS2IBNFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWQULJNFUWS2IBNFUWS2LJAFYWS2LJNEAXC2LJNFUQC2LJNFUWSALJNFUWS2IBOFUWS2LJAFYWS2LJNBIWS2LJNFUQC2LJNFUWSALRNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2CRNFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWSALJNFUWS2IBOFUWS2LJAFUWS2LJNEAWS2LJNFUFC2LJNFUWSALJNFUWS2IBOFUWS2LJAFYWS2LJNEAXC2LJNFUQC2LJNFUWSALJNFUWS2IBNFUWS2LIKFUWS2LJNEAWS2LJNFUQC4LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWQULJNFUWS2IBNFUWS2LJAFYWS2LJNEAXC2LJNFUQC2LJNFUWSALRNFUWS2IBNFUWS2LJAFYWS2LJNBIWS2LJNFUQC2LJNFUWSALRNFUWS2IBOFUWS2LJAFUWS2LJNEAXC2LJNFUQC2LJNFUWSALJNFUWS2CRNFUWS2LJAFUWS2LJNEAXC2LJNFUQC2LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUFC2LJNFUWSALJNFUWS2IBOFUWS2LJAFYWS2LJNEAWS2LJNFUQC4LJNFUWSALJNFUWS2IBOFUWS2LIKFUWS2LJNEAWS2LJNFUQC4LJNFUWSALRNFUWS2IBOFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWQULJNFUWS2IBNFUWS2LJAFYWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNBIWS2LJNFUQC2LJNFUWSALRNFUWS2IBOFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWSALJNFUWS2CRNFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWSALRNFUWS2IBNFUWS2LJAFUWS2LJNEAXC2LJNFUFC2LJNFUWSALJNFUWS2IBOFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2IBNFUWS2LIKFUWS2LJNEAWS2LJNFUQC4LJNFUWSALRNFUWS2IBNFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWQULJNFUWS2IBNFUWS2LJAFYWS2LJNEAXC2LJNFUQC4LJNFUWSALJNFUWS2IBNFUWS2LJAFYWS2LJNBIWS2LJNFUQC2LJNFUWSALRNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2CRNFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWSALJNFUWS2IBOFUWS2LJAFYWS2LJNEAWS2LJNFUFC2LJNFUWSALJNFUWS2IBOFUWS2LJAFYWS2LJNEAXC2LJNFUQC2LJNFUWSALJNFUWS2IBOFUWS2LIKFUWS2LJNEAWS2LJNFUQC4LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWQULJNFUWS2IBNFUWS2LJAFYWS2LJNEAXC2LJNFUQC2LJNFUWSALJNFUWS2IBOFUWS2LJAFYWS2LJNBIWS2LJNFUQC2LJNFUWSALRNFUWS2IBOFUWS2LJAFUWS2LJNEAWS2LJNFUQC4LJNFUWSALJNFUWS2CRNFUWS2LJAFUWS2LJNEAXC2LJNFUQC2LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUFC2LJNFUWSALJNFUWS2IBOFUWS2LJAFYWS2LJNEAWS2LJNFUQC4LJNFUWSALJNFUWS2IBOFUWS2LIKFUWS2LJNEAWS2LJNFUQC4LJNFUWSALRNFUWS2IBNFUWS2LJAFYWS2LJNEAWS2LJNFUQC2LJNFUWQULJNFUWS2IBNFUWS2LJAFYWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNBIWS2LJNFUQC2LJNFUWSALRNFUWS2IBOFUWS2LJAFUWS2LJNEAWS2LJNFUQC4LJNFUWSALRNFUWS2CRNFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWSALJNFUWS2IBNFUWS2LJAFYWS2LJNEAWS2LJNFUFC2LJNFUWSALJNFUWS2IBOFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2IBNFUWS2LIK

view-source:http://10.10.220.152/

<!--J5VEKNCJKZEXEUSDJZEE2MC2M5KFGWJTJMYFMV2PNE2UMWLJGFBEUVKWNFGFKRJQKJLUS5SZJBBEOS2FON3U4U3TFNLVO2ZRJVJXARCUGFHEOS2YKVWUWVKON5HEOQLVKEZGI3S2GJFEOSKTPBRFAMCGKVJEIODQKJUWQ3KMIMYUCY3LNBGUWMCFO5IGYQTWKJ4VMRK2KRJEKWTMGRUVCMCKONQTGTJ5-->

https://cyberchef.io/#recipe=From_Base32('A-Z2-7%3D',false)From_Base64('A-Za-z0-9%2B/%3D',true)From_Base85('!-u')&input=SjVWRUtOQ0pLWkVYRVVTREpaRUUyTUMyTTVLRkdXSlRKTVlGTVYyUE5FMlVNV0xKR0ZCRVVWS1dORkdGS1JKUUtKTFVTNVNaSkJCRU9TMkZPTjNVNFUzVEZOTFZPMlpSSlZKWEFSQ1VHRkhFT1MyWUtWV1VXVktPTjVIRU9RTFZLRVpHSTNTMkdKRkVPU0tUUEJSRkFNQ0dLVkpFSU9EUUtKVVdRM0tNSU1ZVUNZM0xOQkdVV01DRk81SUdZUVRXS0o0Vk1SSzJLUkpFS1dUTUdSVVZDTUNLT05RVEdUSjU

so base32, base64 and base85

:18!R+D#G3F`M&7+EV:.Eb-A%Eb-A4Eb/`pF(K05+>Yi51*COSF)u&)Ch4`.CgggbF!,[?ATD?)F(f,-@rHL+A0>PoG%De4Df^"CBlks

Nami ensures there are precisely 3472 possible places where she could have lost it.

OSINT

https://github.com/1FreyR/LogPose

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://10.10.220.152/ -w /home/witty/Downloads/LogPose.txt -x txt,php,zip,bak,py,html 
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.220.152/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /home/witty/Downloads/LogPose.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              bak,py,html,txt,php,zip
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
Progress: 643 / 24311 (2.64%)[ERROR]  [!] Get 
http://10.10.220.152/dr3ssr0s4.html       (Status: 200) [Size: 3985]

You reach Dressrosa Island, an island ruled by one of the seven Warlords, Donquixote Doflamingo.<br/>
        He took over the island, you are horrified and decide to take him down.

view-source:http://10.10.220.152/images/rabbit_hole.png

let's download

┌──(witty㉿kali)-[~]
└─$ eog rabbithole.png   
^C
                                                                                       
┌──(witty㉿kali)-[~]
└─$ tesseract rabbithole.png output_1 -l eng txt && cat output_1.txt
6b 65 79 3a 69 6d 20 6f 6e 20 6f 74 69 20 Gf 74 69

m5.J`/{{#F%&!5Gl}+n<a

Lhtttavbsw ql gbbzy gfivwwvz

https://www.dcode.fr/ascii-code

|   |   |
|---|---|
|HEX /1-2|key:im on oti ti|

https://www.dcode.fr/base-91-encoding
ito ito no mi:yek

https://www.dcode.fr/vigenere-cipher

key: ITOITONOMI

Doflamingo is still standing

https://onepiece.fandom.com/es/wiki/Fruta_Ito_Ito

view-source:http://10.10.220.152/css/dressrosa_style.css

#container {
    height: 75vh;
    width: 90vw;
    margin: 1vh;
    background-image: url("../king_kong_gun.jpg");
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: flex-start;
    align-content: flex-start;
    flex-wrap: wrap;
    position: relative;
}

http://10.10.220.152/king_kong_gun.jpg

┌──(witty㉿kali)-[~]
└─$ exiftool king_kong_gun.jpg  
ExifTool Version Number         : 12.57
File Name                       : king_kong_gun.jpg
Directory                       : .
File Size                       : 43 kB
File Modification Date/Time     : 2023:07:07 17:46:22-04:00
File Access Date/Time           : 2023:07:07 17:46:22-04:00
File Inode Change Date/Time     : 2023:07:07 17:46:22-04:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Comment                         : Doflamingo is /ko.jpg
Image Width                     : 736
Image Height                    : 414
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 736x414
Megapixels                      : 0.305

http://10.10.220.152/ko.jpg

┌──(witty㉿kali)-[~]
└─$ exiftool ko.jpg            
ExifTool Version Number         : 12.57
File Name                       : ko.jpg
Directory                       : .
File Size                       : 176 kB
File Modification Date/Time     : 2023:07:07 17:46:58-04:00
File Access Date/Time           : 2023:07:07 17:46:58-04:00
File Inode Change Date/Time     : 2023:07:07 17:46:58-04:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Image Width                     : 1280
Image Height                    : 720
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 1280x720
Megapixels                      : 0.922

┌──(witty㉿kali)-[~]
└─$ strings ko.jpg | tac
Congratulations, this is the Log Pose that should lead you to the next island: /wh0l3_c4k3.php

You are on Whole Cake Island. This is the territory of Big Mom, one of the 4 Emperors, this is to say one of the 4 pirates the closest to the One Piece but also the strongest.
Big Mom chases you and want to destroy you. It is unthinkable to fight her directly.
You need to find a way to appease her. 

<!--Big Mom likes cakes-->

┌──(witty㉿kali)-[~]
└─$ sudo tcpdump -i tun0 icmp                                       
[sudo] password for witty: 
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on tun0, link-type RAW (Raw IP), snapshot length 262144 bytes

; ping 10.8.19.103  (Not RCE)

Cookies

NoCakeForYou

changing value

CakeForYou

You successfully stole a copy of the 2nd Road Poneglyph: FUWS2LJNEAWS2LJNFUQC4LJNFUWSALRNFUWS2IBNFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWQULJNFUWS2IBNFUWS2LJAFYWS2LJNEAXC2LJNFUQC2LJNFUWSALRNFUWS2IBNFUWS2LJAFYWS2LJNBIWS2LJNFUQC2LJNFUWSALRNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2CRNFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWSALJNFUWS2IBNFUWS2LJAFYWS2LJNEAXC2LJNFUFC2LJNFUWSALJNFUWS2IBOFUWS2LJAFYWS2LJNEAWS2LJNFUQC4LJNFUWSALJNFUWS2IBOFUWS2LIKFUWS2LJNEAWS2LJNFUQC4LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWQULJNFUWS2IBNFUWS2LJAFYWS2LJNEAXC2LJNFUQC2LJNFUWSALRNFUWS2IBNFUWS2LJAFUWS2LJNBIWS2LJNFUQC4LJNFUWSALRNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUQC4LJNFUWSALRNFUWS2CRNFUWS2LJAFUWS2LJNEAXC2LJNFUQC2LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUFC2LJNFUWSALJNFUWS2IBOFUWS2LJAFYWS2LJNEAWS2LJNFUQC2LJNFUWSALRNFUWS2IBOFUWS2LIKFUWS2LJNEAWS2LJNFUQC4LJNFUWSALRNFUWS2IBOFUWS2LJAFUWS2LJNEAWS2LJNFUQC4LJNFUWQULJNFUWS2IBNFUWS2LJAFYWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNBIWS2LJNFUQC2LJNFUWSALRNFUWS2IBOFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWSALRNFUWS2CRNFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWSALJNFUWS2IBNFUWS2LJAFYWS2LJNEAXC2LJNFUFC2LJNFUWSALJNFUWS2IBOFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2IBNFUWS2LIKFUWS2LJNEAWS2LJNFUQC4LJNFUWSALRNFUWS2IBNFUWS2LJAFYWS2LJNEAWS2LJNFUQC2LJNFUWQULJNFUWS2IBOFUWS2LJAFYWS2LJNEAWS2LJNFUQC2LJNFUWSALRNFUWS2IBNFUWS2LJAFUWS2LJNBIWS2LJNFUQC2LJNFUWSALRNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2CRNFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWSALJNFUWS2IBOFUWS2LJAFUWS2LJNEAWS2LJNFUFC2LJNFUWSALJNFUWS2IBOFUWS2LJAFYWS2LJNEAWS2LJNFUQC4LJNFUWSALJNFUWS2IBNFUWS2LIKFUWS2LJNEAWS2LJNFUQC4LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWQULJNFUWS2IBNFUWS2LJAFYWS2LJNEAXC2LJNFUQC2LJNFUWSALRNFUWS2IBOFUWS2LJAFYWS2LJNBIWS2LJNFUQC2LJNFUWSALRNFUWS2IBOFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2CRNFUWS2LJAFUWS2LJNEAXC2LJNFUQC2LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUFC2LJNFUWSALJNFUWS2IBOFUWS2LJAFYWS2LJNEAWS2LJNFUQC4LJNFUWSALRNFUWS2IBOFUWS2LIKFUWS2LJNEAWS2LJNFUQC4LJNFUWSALRNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWQULJNFUWS2IBNFUWS2LJAFYWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNBIWS2LJNFUQC2LJNFUWSALRNFUWS2IBOFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWSALJNFUWS2CRNFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWSALJNFUWS2IBOFUWS2LJAFYWS2LJNEAWS2LJNFUFC2LJNFUWSALJNFUWS2IBOFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2IBNFUWS2LIKFUWS2LJNEAWS2LJNFUQC4LJNFUWSALRNFUWS2IBNFUWS2LJAFYWS2LJNEAWS2LJNFUQC4LJNFUWQULJNFUWS2IBNFUWS2LJAFYWS2LJNEAXC2LJNFUQC2LJNFUWSALJNFUWS2IBOFUWS2LJAFUWS2LJNBIWS2LJNFUQC2LJNFUWSALRNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2CRNFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWSALJNFUWS2IBOFUWS2LJAFYWS2LJNEAWS2LJNFUFC2LJNFUWSALRNFUWS2IBOFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2IBOFUWS2LIKFUWS2LJNEAWS2LJNFUQC4LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWQULJNFUWS2IBNFUWS2LJAFYWS2LJNEAXC2LJNFUQC2LJNFUWSALRNFUWS2IBNFUWS2LJAFYWS2LJNBIWS2LJNFUQC2LJNFUWSALRNFUWS2IBOFUWS2LJAFUWS2LJNEAXC2LJNFUQC2LJNFUWSALRNFUWS2CRNFUWS2LJAFUWS2LJNEAXC2LJNFUQC2LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUFC2LJNFUWSALJNFUWS2IBOFUWS2LJAFYWS2LJNEAWS2LJNFUQC4LJNFUWSALRNFUWS2IBOFUWS2LIKFUWS2LJNEAXC2LJNFUQC4LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUQC4LJNFUWQULJNFUWS2IBNFUWS2LJAFYWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNBIWS2LJNFUQC2LJNFUWSALRNFUWS2IBOFUWS2LJAFUWS2LJNEAXC2LJNFUQC2LJNFUWSALRNFUWS2CRNFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWSALJNFUWS2IBOFUWS2LJAFYWS2LJNEAWS2LJNFUFC2LJNFUWSALJNFUWS2IBOFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2IBNFUWS2LIKFUWS2LJNEAWS2LJNFUQC4LJNFUWSALRNFUWS2IBNFUWS2LJAFYWS2LJNEAWS2LJNFUQC4LJNFUWQULJNFUWS2IBNFUWS2LJAFYWS2LJNEAXC2LJNFUQC2LJNFUWSALRNFUWS2IBOFUWS2LJAFUWS2LJNBIWS2LJNFUQC2LJNFUWSALRNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2CRNFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWSALJNFUWS2IBNFUWS2LJAFYWS2LJNEAXC2LJNFUFC2LJNFUWSALJNFUWS2IBOFUWS2LJAFYWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2IBOFUWS2LIKFUWS2LJNEAWS2LJNFUQC4LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWQULJNFUWS2IBNFUWS2LJAFYWS2LJNEAXC2LJNFUQC2LJNFUWSALJNFUWS2IBOFUWS2LJAFYWS2LJNBIWS2LJNFUQC2LJNFUWSALRNFUWS2IBOFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWSALRNFUWS2CRNFUWS2LJAFUWS2LJNEAXC2LJNFUQC2LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUFC2LJNFUWSALJNFUWS2IBOFUWS2LJAFYWS2LJNEAWS2LJNFUQC4LJNFUWSALJNFUWS2IBOFUWS2LIKFUWS2LJNEAWS2LJNFUQC4LJNFUWSALRNFUWS2IBNFUWS2LJAFYWS2LJNEAWS2LJNFUQC4LJNFUWQULJNFUWS2IBNFUWS2LJAFYWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNBIWS2LJNFUQC2LJNFUWSALRNFUWS2IBOFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWSALJNFUWS2CRNFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWSALJNFUWS2IBNFUWS2LJAFUWS2LJNEAXC2LJNFUFC2LJNFUWSALJNFUWS2IBOFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2IBNFUWS2LIKFUWS2LJNEAWS2LJNFUQC4LJNFUWSALRNFUWS2IBNFUWS2LJAFYWS2LJNEAXC2LJNFUQC2LJNFUWQULJNFUWS2IBNFUWS2LJAFYWS2LJNEAXC2LJNFUQC2LJNFUWSALJNFUWS2IBOFUWS2LJAFYWS2LJNBIWS2LJNFUQC2LJNFUWSALRNFUWS2IBNFUWS2LJAFUWS2LJNEAWS2LJNFUQC2LJNFUWSALJNFUWS2CRNFUWS2LJAFUWS2LJNEAXC2LJNFUQC4LJNFUWSALJNFUWS2IBNFUWS2LJA
You succeed to run away but you don't own a Log Pose to go to Kaido's Island, you are sailing without even knowing where you are heading to.
You end up reaching a strange island: /r4nd0m.html

http://10.10.220.152/r4nd0m.html

 On your way, you decide to stop by an island you can see from your boat in order to get supplies.
Surprisingly enough, you meet your friend Buggy the Clown there.
He wants to challenge you to play one of his games. He knows he can't lose, he even promise a Log Pose for Onigashima if you can beat him.
He even let you decide which game you'd like to play: 

view-source:http://10.10.220.152/buggy_games/brain_teaser.js

document.getElementById('back').textContent = "Log Pose: /0n1g4sh1m4.php"  

document.getElementById('back')
<div id="back" class="cube_face">
​
accessKey: ""
​
accessKeyLabel: ""
​
align: ""
​
assignedSlot: null
​
attributes: NamedNodeMap [ id="back", class="cube_face" ]
​
baseURI: "http://10.10.220.152/buggy_games/brain_teaser.html"
​
childElementCount: 0
​
childNodes: NodeList [ #text
 ]
​
children: HTMLCollection { length: 0 }
​
classList: DOMTokenList [ "cube_face" ]
​
className: "cube_face"
​
clientHeight: 200
​
clientLeft: 3
​
clientTop: 3
​
clientWidth: 200
​
contentEditable: "inherit"
​
dataset: DOMStringMap(0)
​
dir: ""
​
draggable: false
​
enterKeyHint: ""
​
firstChild: #text "Log Pose: /0n1g4sh1m4.php"
​
firstElementChild: null
​
hidden: false
​
id: "back"
​
innerHTML: "Log Pose: /0n1g4sh1m4.php"
​
innerText: "Log Pose: /0n1g4sh1m4.php"
​
inputMode: ""
​
isConnected: true
​
isContentEditable: false
​
lang: ""
​
lastChild: #text "Log Pose: /0n1g4sh1m4.php"
​​
assignedSlot: null
​​
baseURI: "http://10.10.220.152/buggy_games/brain_teaser.html"
​​
childNodes: NodeList []
​​
data: "Log Pose: /0n1g4sh1m4.php"
​​
firstChild: null
​​
isConnected: true
​​
lastChild: null
​​
length: 25
​​
nextElementSibling: null
​​
nextSibling: null
​​
nodeName: "#text"
​​
nodeType: 3
​​
nodeValue: "Log Pose: /0n1g4sh1m4.php"
​​
ownerDocument: HTMLDocument http://10.10.220.152/buggy_games/brain_teaser.html
​​
parentElement: <div id="back" class="cube_face">​​
parentNode: <div id="back" class="cube_face">
​​
previousElementSibling: null
​​
previousSibling: null
​​
textContent: "Log Pose: /0n1g4sh1m4.php"
​​
wholeText: "Log Pose: /0n1g4sh1m4.php"
​​
<prototype>: TextPrototype { splitText: splitText(), wholeText: Getter, assignedSlot: Getter, … }
​
lastElementChild: null
​
localName: "div"
​
namespaceURI: "http://www.w3.org/1999/xhtml"
​
nextElementSibling: <div id="right" class="cube_face">​
nextSibling: #text "\n                "
​
nodeName: "DIV"
​
nodeType: 1
​
nodeValue: null
​
nonce: ""
​
offsetHeight: 205
​
offsetLeft: -103
​
offsetParent: <div id="container__animation" style="transform: rotateX(16.42…) rotateY(-26.5711deg);">
​
offsetTop: -8
​
offsetWidth: 205
​
onabort: null
​
onanimationcancel: null
​
onanimationend: null
​
onanimationiteration: null
​
onanimationstart: null
​
onauxclick: null
​
onbeforeinput: null
​
onblur: null
​
oncanplay: null
​
oncanplaythrough: null
​
onchange: null
​
onclick: null
​
onclose: null
​
oncontextmenu: null
​
oncopy: null
​
oncuechange: null
​
oncut: null
​
ondblclick: null
​
ondrag: null
​
ondragend: null
​
ondragenter: null
​
ondragexit: null
​
ondragleave: null
​
ondragover: null
​
ondragstart: null
​
ondrop: null
​
ondurationchange: null
​
onemptied: null
​
onended: null
​
onerror: null
​
onfocus: null
​
onformdata: null
​
onfullscreenchange: null
​
onfullscreenerror: null
​
ongotpointercapture: null
​
oninput: null
​
oninvalid: null
​
onkeydown: null
​
onkeypress: null
​
onkeyup: null
​
onload: null
​
onloadeddata: null
​
onloadedmetadata: null
​
onloadend: null
​
onloadstart: null
​
onlostpointercapture: null
​
onmousedown: null
​
onmouseenter: null
​
onmouseleave: null
​
onmousemove: null
​
onmouseout: null
​
onmouseover: null
​
onmouseup: null
​
onmozfullscreenchange: null
​
onmozfullscreenerror: null
​
onpaste: null
​
onpause: null
​
onplay: null
​
onplaying: null
​
onpointercancel: null
​
onpointerdown: null
​
onpointerenter: null
​
onpointerleave: null
​
onpointermove: null
​
onpointerout: null
​
onpointerover: null
​
onpointerup: null
​
onprogress: null
​
onratechange: null
​
onreset: null
​
onresize: null
​
onscroll: null
​
onsecuritypolicyviolation: null
​
onseeked: null
​
onseeking: null
​
onselect: null
​
onselectionchange: null
​
onselectstart: null
​
onslotchange: null
​
onstalled: null
​
onsubmit: null
​
onsuspend: null
​
ontimeupdate: null
​
ontoggle: null
​
ontransitioncancel: null
​
ontransitionend: null
​
ontransitionrun: null
​
ontransitionstart: null
​
onvolumechange: null
​
onwaiting: null
​
onwebkitanimationend: null
​
onwebkitanimationiteration: null
​
onwebkitanimationstart: null
​
onwebkittransitionend: null
​
onwheel: null
​
outerHTML: "<div id=\"back\" class=\"cube_face\">Log Pose: /0n1g4sh1m4.php</div>"
​
outerText: "Log Pose: /0n1g4sh1m4.php"
​
ownerDocument: HTMLDocument http://10.10.220.152/buggy_games/brain_teaser.html
​
parentElement: <div id="container__animation" style="transform: rotateX(16.42…) rotateY(-26.5711deg);">​
parentNode: <div id="container__animation" style="transform: rotateX(16.42…) rotateY(-26.5711deg);">​
part: DOMTokenList []
​
prefix: null
​
previousElementSibling: <div id="front" class="cube_face">​
previousSibling: #text "\n                "
​
scrollHeight: 200
​
scrollLeft: 0
​
scrollLeftMax: 0
​
scrollTop: 0
​
scrollTopMax: 0
​
scrollWidth: 200
​
shadowRoot: null
​
slot: ""
​
spellcheck: false
​
style: CSS2Properties(0)
​
tabIndex: -1
​
tagName: "DIV"
​
textContent: "Log Pose: /0n1g4sh1m4.php"
​
title: ""
​
<prototype>: HTMLDivElementPrototype { align: Getter & Setter, … }

http://10.10.220.152/0n1g4sh1m4.php

You reach the island of Onigashima. This is one of the Kaido's territory, one of the four Emperors, Kaido of the Beasts is renowned as the Strongest Creature in the world.
It is said that if it is a 1 vs 1, Kaido will prevail.
Speaking about brute force, Kaido is unbeatable.

Straw Hat Luffy has 2 options: 

download kaido.jpeg

┌──(witty㉿kali)-[~]
└─$ stegcracker kaido.jpeg /usr/share/wordlists/rockyou.txt
StegCracker 2.1.0 - (https://github.com/Paradoxis/StegCracker)
Copyright (c) 2023 - Luke Paris (Paradoxis)

StegCracker has been retired following the release of StegSeek, which 
will blast through the rockyou.txt wordlist within 1.9 second as opposed 
to StegCracker which takes ~5 hours.

StegSeek can be found at: https://github.com/RickdeJager/stegseek

Counting lines in wordlist..
Attacking file 'kaido.jpeg' with wordlist '/usr/share/wordlists/rockyou.txt'..
Successfully cracked file with password: imabeast
Tried 106308 passwords
Your file has been written to: kaido.jpeg.out
