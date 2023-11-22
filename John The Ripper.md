---
Learn how to use John the Ripper - An extremely powerful and adaptable hash cracking tool 
---

# John The Ripper — Writeup

## Overview
### John The Ripper — Writeup
### John The Ripper — Writeup
![](https://tryhackme-images.s3.amazonaws.com/room-icons/00b6a8786d69f4bd3f4aa2683411421e.jpeg)
### John who?
Welcome
John the Ripper is one of the most well known, well-loved and versatile hash cracking tools out there. It combines a fast cracking speed, with an extraordinary range of compatible hash types. This room will assume no previous knowledge, so we must first cover some basic terms and concepts before we move into practical hash cracking.
What are Hashes?
A hash is a way of taking a piece of data of any length and  representing it in another form that is a fixed length. This masks the original value of the data. This is done by running the original data through a hashing algorithm. There are many popular hashing algorithms, such as MD4,MD5, SHA1 and NTLM. Lets try and show this with an example:
If we take "polo", a string of 4 characters- and run it through an MD5 hashing algorithm, we end up with an output of: b53759f3ce692de7aff1b5779d3964da a standard 32 character MD5 hash.
Likewise, if we take "polomints", a string of 9 characters- and run it through the same MD5 hashing algorithm, we end up with an output of: 584b6e4f4586e136bc280f27f9c64f3b another standard 32 character MD5 hash.
What makes Hashes secure?
Hashing algorithms are designed so that they only operate one way. This means that a calculated hash cannot be reversed using just the output given. This ties back to a fundamental mathematical problem known as the [P vs NP relationship](https://en.wikipedia.org/wiki/P_versus_NP_problem) .
While this is an extremely interesting mathematical concept that proves fundamental to computing and cryptography I am in no way qualified to try and explain it in detail here; but abstractly it means that the algorithm to hash the value will be "NP" and can therefore be calculated reasonably. However an un-hashing algorithm would be "P" and intractable to solve- meaning that it cannot be computed in a reasonable time using standard computers.
Where John Comes in...
Even though the algorithm itself is not feasibly reversible. That doesn't mean that cracking the hashes is impossible. If you have the hashed version of a password, for example- and you know the hashing algorithm- you can use that hashing algorithm to hash a large number of words, called a dictionary. You can then compare these hashes to the one you're trying to crack, to see if any of them match. If they do, you now know what word corresponds to that hash- you've cracked it!
This process is called a dictionary attack and John the Ripper, or John as it's commonly shortened to, is a tool to allow you to conduct fast brute force attacks on a large array of different hash types.
Learning More
For some more in-depth material on specific hashing and Encryption methods I'd recommend checking out NinjaJc01's amazing room covering these topics: encryptioncrypto101
Read and understand the basic concepts of hashing and hash cracking  *No answer needed*
### Setting up John the Ripper
Setting Up John The Ripper
John the Ripper is supported on many different Operating Systems, not just Linux Distributions. As a note before we go through this, there are multiple versions of John, the standard "core" distribution, as well as multiple community editions- which extend the feature set of the original John distribution. The most popular of these distributions is the "Jumbo John"- which we will be using specific features of later.
Parrot, Kali and AttackBox
If you're using Parrot OS, Kali Linux or TryHackMe's own AttackBox- you should already have Jumbo John installed. You can double check this by typing john into the terminal. You should be met with a usage guide for john, with the first line reading: "John the Ripper 1.9.0-jumbo-1" or similar with a different version number. If not, you can use sudo apt install john to install it.
Blackarch
If you're using Blackarch, or the Blackarch repositories you may or may not have Jumbo John installed, to check if you do, use the command pacman -Qe | grep "john" You should be met with an output similar to "john 1.9.0.jumbo1-5" or similar with a different version number. If you do not have it installed, you can simply use pacman -S john to install it.
Building from Source for Linux
If you wish to build the package from source to meet your system requirements, you can do this in five fairly straightforward steps. Further advice on the installation process and how to configure your build from source can be found here.
Use git clone https://github.com/openwall/john -b bleeding-jumbo john to clone the jumbo john repository to your current working
Then cd john/src/ to change your current directory to where the source code is.
Once you're in this directory, use ./configure to check the required dependencies and options that have been configured.
If you're happy with this output, and have installed any required dependencies that are needed, use make -s clean && make -sj4 to build a binary of john. This binary will be in the above run directory, which you can change to with cd ../run
You can test this binary using ./john --test
Installing on Windows
To install Jumbo John the Ripper on Windows, you just need to download and install the zipped binary for either 64 bit systems here or for 32 bit systems here.
What is the most popular extended version of John the Ripper? *jumbo john*
### Wordlists
Wordlists
As we explained in the first task, in order to dictionary attack hashes, you need a list of words that you can hash and compare, unsurprisingly this is called a wordlist. There are many different wordlists out there, a good collection to use can be found in the SecLists repository. There are a few places you can look for wordlists on your attacking system of choice, we will quickly run through where you can find them.
Parrot, Kali and AttackBox
On Parrot, Kali and TryHackMe's AttackBox- you can find a series of amazing wordlists in the /usr/share/wordlists directory.
RockYou
For all of the tasks in this room, we will be using the infamous rockyou.txt wordlist- which is a very large common password wordlist, obtained from a data breach on a website called rockyou.com in 2009. If you are not using any of the above distributions, you can get the rockyou.txt wordlist from the SecLists repository under the /Passwords/Leaked-Databases subsection. You may need to extract it from .tar.gz format, using tar xvzf rockyou.txt.tar.gz.
Now that we have our hash cracker and wordlists all set up, lets move onto some hash cracking!
What website was the rockyou.txt wordlist created from a breach on?  *rockyou.com*
### Cracking Basic Hashes
Cracking Basic Hashes
There are multiple ways to use John the Ripper to crack simple hashes, we're going to walk through a few, before moving on to cracking some ourselves.
John Basic Syntax
The basic syntax of John the Ripper commands is as follows. We will cover the specific options and modifiers used as we use them.
john [options] [path to file]
john - Invokes the John the Ripper program
[path to file] - The file containing the hash you're trying to crack, if it's in the same directory you won't need to name a path, just the file.
Automatic Cracking
John has built-in features to detect what type of hash it's being given, and to select appropriate rules and formats to crack it for you, this isn't always the best idea as it can be unreliable- but if you can't identify what hash type you're working with and just want to try cracking it, it can be a good option! To do this we use the following syntax:
john --wordlist=[path to wordlist] [path to file]
--wordlist= - Specifies using wordlist mode, reading from the file that you supply in the following path...
[path to wordlist] - The path to the wordlist you're using, as described in the previous task.
Example Usage:
john --wordlist=/usr/share/wordlists/rockyou.txt hash_to_crack.txt
Identifying Hashes
Sometimes John won't play nicely with automatically recognising and loading hashes, that's okay! We're able to use other tools to identify the hash, and then set john to use a specific format. There are multiple ways to do this, such as using an online hash identifier like this one. I like to use a tool called hash-identifier, a Python tool that is super easy to use and will tell you what different types of hashes the one you enter is likely to be, giving you more options if the first one fails.
To use hash-identifier, you can just pull the python file from gitlab using: wget https://gitlab.com/kalilinux/packages/hash-identifier/-/raw/kali/master/hash-id.py.
Then simply launch it with python3 hash-id.py and then enter the hash you're trying to identify- and it will give you possible formats!
Format-Specific Cracking
Once you have identified the hash that you're dealing with, you can tell john to use it while cracking the provided hash using the following syntax:
john --format=[format] --wordlist=[path to wordlist] [path to file]
--format= - This is the flag to tell John that you're giving it a hash of a specific format, and to use the following format to crack it
[format] - The format that the hash is in
Example Usage:
john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash_to_crack.txt
A Note on Formats:
When you are telling john to use formats, if you're dealing with a standard hash type, e.g. md5 as in the example above, you have to prefix it with raw- to tell john you're just dealing with a standard hash type, though this doesn't always apply. To check if you need to add the prefix or not, you can list all of John's formats using john --list=formats and either check manually, or grep for your hash type using something like john --list=formats | grep -iF "md5".
Practical
Now you know the syntax, modifiers and methods to crack basic hashes, try it yourself! Download the attached .txt files that
```text
──(kali㉿kali)-[~/Downloads/learning_crypto/jhon/first_task_hashes]
└─$ cat hash1.txt       
2e728dd31fb5949bc39cac5a9f066498
```
```text
┌──(kali㉿kali)-[~/Downloads/learning_crypto/jhon/first_task_hashes]
└─$ hash-identifier 2e728dd31fb5949bc39cac5a9f066498

   #########################################################################
```
```text
#     __  __                     __           ______    _____           #
```
```text
#    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
```
```text
#    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
```
```text
#     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
```
```text
#      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
```
```text
#       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
```
```text
#        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
```
```text
#                                                             By Zion3R #
```
```text
#                                                    www.Blackploit.com #
```
```text
#                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------

Possible Hashs:
[+] MD5
[+] Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))
```
What type of hash is hash1.txt? *md5*

## Exploitation
```text
┌──(kali㉿kali)-[~/Downloads/learning_crypto/jhon/first_task_hashes]
└─$ john --list=formats | grep -iF "md5"                                      
descrypt, bsdicrypt, md5crypt, md5crypt-long, bcrypt, scrypt, LM, AFS, 
416 formats (149 dynamic formats shown as just "dynamic_n" here)
aix-ssha512, andOTP, ansible, argon2, as400-des, as400-ssha1, asa-md5, 
django-scrypt, dmd5, dmg, dominosec, dominosec8, DPAPImk, dragonfly3-32, 
mscash2, MSCHAPv2, mschapv2-naive, krb5pa-md5, mssql, mssql05, mssql12, 
net-md5, netntlmv2, netntlm, netntlm-naive, net-sha1, nk, notes, md5ns, 
Padlock, Palshop, Panama, PBKDF2-HMAC-MD4, PBKDF2-HMAC-MD5, PBKDF2-HMAC-SHA1, 
pgpwde, phpass, PHPS, PHPS2, pix-md5, PKZIP, po, postgres, PST, PuTTY, 
Raw-Blake2, Raw-Keccak, Raw-Keccak-256, Raw-MD4, Raw-MD5, Raw-MD5u, Raw-SHA1, 
solarwinds, SSH, sspr, Stribog-256, Stribog-512, STRIP, SunMD5, SybaseASE, 
Sybase-PROP, tacacs-plus, tcp-md5, telegram, tezos, Tiger, tc_aes_xts, 
HMAC-MD5, HMAC-SHA1, HMAC-SHA224, HMAC-SHA256, HMAC-SHA384, HMAC-SHA512,
```
```text
┌──(kali㉿kali)-[~/Downloads/learning_crypto/jhon/first_task_hashes]
└─$ john --list=formats                 
descrypt, bsdicrypt, md5crypt, md5crypt-long, bcrypt, scrypt, LM, AFS, 
tripcode, AndroidBackup, adxcrypt, agilekeychain, aix-ssha1, aix-ssha256, 
aix-ssha512, andOTP, ansible, argon2, as400-des, as400-ssha1, asa-md5, 
AxCrypt, AzureAD, BestCrypt, BestCryptVE4, bfegg, Bitcoin, BitLocker, 
bitshares, Bitwarden, BKS, Blackberry-ES10, WoWSRP, Blockchain, chap, 
Clipperz, cloudkeychain, dynamic_n, cq, CRC32, cryptoSafe, sha1crypt, 
sha256crypt, sha512crypt, Citrix_NS10, dahua, dashlane, diskcryptor, Django, 
django-scrypt, dmd5, dmg, dominosec, dominosec8, DPAPImk, dragonfly3-32, 
dragonfly3-64, dragonfly4-32, dragonfly4-64, Drupal7, eCryptfs, eigrp, 
electrum, EncFS, enpass, EPI, EPiServer, ethereum, fde, Fortigate256, 
Fortigate, FormSpring, FVDE, geli, gost, gpg, HAVAL-128-4, HAVAL-256-3, hdaa, 
hMailServer, hsrp, IKE, ipb2, itunes-backup, iwork, KeePass, keychain, 
keyring, keystore, known_hosts, krb4, krb5, krb5asrep, krb5pa-sha1, krb5tgs, 
krb5-17, krb5-18, krb5-3, kwallet, lp, lpcli, leet, lotus5, lotus85, LUKS, 
MD2, mdc2, MediaWiki, monero, money, MongoDB, scram, Mozilla, mscash, 
mscash2, MSCHAPv2, mschapv2-naive, krb5pa-md5, mssql, mssql05, mssql12, 
multibit, mysqlna, mysql-sha1, mysql, net-ah, nethalflm, netlm, netlmv2, 
net-md5, netntlmv2, netntlm, netntlm-naive, net-sha1, nk, notes, md5ns, 
nsec3, NT, o10glogon, o3logon, o5logon, ODF, Office, oldoffice, 
OpenBSD-SoftRAID, openssl-enc, oracle, oracle11, Oracle12C, osc, ospf, 
Padlock, Palshop, Panama, PBKDF2-HMAC-MD4, PBKDF2-HMAC-MD5, PBKDF2-HMAC-SHA1, 
PBKDF2-HMAC-SHA256, PBKDF2-HMAC-SHA512, PDF, PEM, pfx, pgpdisk, pgpsda, 
pgpwde, phpass, PHPS, PHPS2, pix-md5, PKZIP, po, postgres, PST, PuTTY, 
pwsafe, qnx, RACF, RACF-KDFAES, radius, RAdmin, RAKP, rar, RAR5, Raw-SHA512, 
Raw-Blake2, Raw-Keccak, Raw-Keccak-256, Raw-MD4, Raw-MD5, Raw-MD5u, Raw-SHA1, 
Raw-SHA1-AxCrypt, Raw-SHA1-Linkedin, Raw-SHA224, Raw-SHA256, Raw-SHA3, 
Raw-SHA384, restic, ripemd-128, ripemd-160, rsvp, RVARY, Siemens-S7, 
Salted-SHA1, SSHA512, sapb, sapg, saph, sappse, securezip, 7z, Signal, SIP, 
skein-256, skein-512, skey, SL3, Snefru-128, Snefru-256, LastPass, SNMP, 
solarwinds, SSH, sspr, Stribog-256, Stribog-512, STRIP, SunMD5, SybaseASE, 
Sybase-PROP, tacacs-plus, tcp-md5, telegram, tezos, Tiger, tc_aes_xts, 
tc_ripemd160, tc_ripemd160boot, tc_sha512, tc_whirlpool, vdi, OpenVMS, vmx, 
VNC, vtp, wbb3, whirlpool, whirlpool0, whirlpool1, wpapsk, wpapsk-pmk, 
xmpp-scram, xsha, xsha512, zed, ZIP, ZipMonster, plaintext, has-160, 
HMAC-MD5, HMAC-SHA1, HMAC-SHA224, HMAC-SHA256, HMAC-SHA384, HMAC-SHA512, 
dummy, crypt
416 formats (149 dynamic formats shown as just "dynamic_n" here)
```
```text
┌──(kali㉿kali)-[~/Downloads/learning_crypto/jhon/first_task_hashes]
└─$ john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash1.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 128/128 AVX 4x3])
Warning: no OpenMP support for this hash type, consider --fork=4
Press 'q' or Ctrl-C to abort, almost any other key for status
biscuit          (?)     
1g 0:00:00:00 DONE (2022-08-23 18:31) 50.00g/s 134400p/s 134400c/s 134400C/s shamrock..nugget
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed.
```
What is the cracked value of hash1.txt?  *biscuit*
```text
┌──(kali㉿kali)-[~/Downloads/learning_crypto/jhon/first_task_hashes]
└─$ hash-identifier 1A732667F3917C0F4AA98BB13011B9090C6F8065
   #########################################################################
```
```text
#     __  __                     __           ______    _____           #
```
```text
#    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
```
```text
#    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
```
```text
#     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
```
```text
#      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
```
```text
#       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
```
```text
#        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
```
```text
#                                                             By Zion3R #
```
```text
#                                                    www.Blackploit.com #
```
```text
#                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------

Possible Hashs:
[+] SHA-1
[+] MySQL5 - SHA-1(SHA-1($pass))
```
What type of hash is hash2.txt? *SHA1*
```text
┌──(kali㉿kali)-[~/Downloads/learning_crypto/jhon/first_task_hashes]
└─$ john --format=raw-SHA1 --wordlist=/usr/share/wordlists/rockyou.txt hash2.txt
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-SHA1 [SHA1 128/128 AVX 4x])
Warning: no OpenMP support for this hash type, consider --fork=4
Press 'q' or Ctrl-C to abort, almost any other key for status
kangeroo         (?)     
1g 0:00:00:00 DONE (2022-08-23 18:34) 33.33g/s 3904Kp/s 3904Kc/s 3904KC/s kanon..kalvin1
Use the "--show --format=Raw-SHA1" options to display all of the cracked passwords reliably
Session completed.
```
What is the cracked value of hash2.txt *kangeroo *
```text
┌──(kali㉿kali)-[~/Downloads/learning_crypto/jhon/first_task_hashes]
└─$ hash-identifier D7F4D3CCEE7ACD3DD7FAD3AC2BE2AAE9C44F4E9B7FB802D73136D4C53920140A
   #########################################################################
```
```text
#     __  __                     __           ______    _____           #
```
```text
#    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
```
```text
#    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
```
```text
#     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
```
```text
#      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
```
```text
#       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
```
```text
#        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
```
```text
#                                                             By Zion3R #
```
```text
#                                                    www.Blackploit.com #
```
```text
#                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------

Possible Hashs:
[+] SHA-256
```
What type of hash is hash3.txt? *SHA256*
```text
┌──(kali㉿kali)-[~/Downloads/learning_crypto/jhon/first_task_hashes]
└─$ john --list=formats | grep -iF "sha256"                                     
416 formats (149 dynamic formats shown as just "dynamic_n" here)
tripcode, AndroidBackup, adxcrypt, agilekeychain, aix-ssha1, aix-ssha256, 
sha256crypt, sha512crypt, Citrix_NS10, dahua, dashlane, diskcryptor, Django, 
PBKDF2-HMAC-SHA256, PBKDF2-HMAC-SHA512, PDF, PEM, pfx, pgpdisk, pgpsda, 
Raw-SHA1-AxCrypt, Raw-SHA1-Linkedin, Raw-SHA224, Raw-SHA256, Raw-SHA3, 
HMAC-MD5, HMAC-SHA1, HMAC-SHA224, HMAC-SHA256, HMAC-SHA384, HMAC-SHA512,
```
```text
┌──(kali㉿kali)-[~/Downloads/learning_crypto/jhon/first_task_hashes]
└─$ john --format=raw-SHA256 --wordlist=/usr/share/wordlists/rockyou.txt hash3.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-SHA256 [SHA256 128/128 AVX 4x])
Warning: poor OpenMP scalability for this hash type, consider --fork=4
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
microphone       (?)     
1g 0:00:00:00 DONE (2022-08-23 18:36) 33.33g/s 3276Kp/s 3276Kc/s 3276KC/s ryanscott..Donovan
Use the "--show --format=Raw-SHA256" options to display all of the cracked passwords reliably
Session completed.
```
What is the cracked value of hash3.txt *microphone *
```text
┌──(kali㉿kali)-[~/Downloads/learning_crypto/jhon/first_task_hashes]
└─$ hash-identifier c5a60cc6bbba781c601c5402755ae1044bbf45b78d1183cbf2ca1c865b6c792cf3c6b87791344986c8a832a0f9ca8d0b4afd3d9421a149d57075e1b4e93f90bf
   #########################################################################
```
```text
#     __  __                     __           ______    _____           #
```
```text
#    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
```
```text
#    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
```
```text
#     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
```
```text
#      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
```
```text
#       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
```
```text
#        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
```
```text
#                                                             By Zion3R #
```
```text
#                                                    www.Blackploit.com #
```
```text
#                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------

Possible Hashs:
[+] SHA-512
[+] Whirlpool
```
What type of hash is hash4.txt? *Whirlpool*
```text
┌──(kali㉿kali)-[~/Downloads/learning_crypto/jhon/first_task_hashes]
└─$ john --format=whirlpool --wordlist=/usr/share/wordlists/rockyou.txt hash4.txt
Using default input encoding: UTF-8
Loaded 1 password hash (whirlpool [WHIRLPOOL 32/64])
Warning: poor OpenMP scalability for this hash type, consider --fork=4
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
colossal         (?)     
1g 0:00:00:00 DONE (2022-08-23 18:39) 2.325g/s 1581Kp/s 1581Kc/s 1581KC/s davita1..chata74
Use the "--show" option to display all of the cracked passwords reliably
