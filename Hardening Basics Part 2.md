---
Continue learning about hardening
---

# Hardening Basics Part 2 — Writeup

## Overview
### Hardening Basics Part 2 — Writeup
### Hardening Basics Part 2 — Writeup
![](https://tryhackme-images.s3.amazonaws.com/room-icons/81525b4555b637e5ca3b742357fc4b5b.jpeg)
### Introduction
Introduction
Welcome to Part 2 of Hardening Basics! While this room can be enjoyed on its own, it is meant to be done in conjunction with Part 1. If you have not done Part 1 yet, I highly recommend you do so.
In this room, we will cover the following:
SSH and Encryption (Chapter 3)
Mandatory Access Control (Chapter 4)
This was mentioned in Part 1 but in case you did not do that room:
There are no questions related to performing tasks on a virtual machine. However, I have provided a semi-configured Ubuntu 18.04 environment for you to play around with while you go through the different tasks. Things that have been configured at a basic level will be:
Users
PAM
Permissions
Passwords
And that's it! I'll leave you to play around as you wish. You may access the machine with the following credentials (if you're coming from Part 1, you do not need to deploy the VM):
spooky:tryhackme
These will be global credentials that should give you access to do everything you need to.  I will provide other credentials for tasks where I feel it's possible to lock yourself out from a mistake. You can find some optional challenges in Task 15.
The hope is that by the end of this room, you'll be able to clearly explain and understand the above topics and apply them to your daily life, or life at work. Whether you're a senior systems administrator or just starting out as a junior, these topics will help you understand what it takes to harden a Linux system.
Topics have been chosen from this book. I looked through the table of contents and picked out the ones that would be the most important and allow the room to have the best content while still keeping it within the proper limits. I think the above 4 topics are the best and will give you the most knowledge on how to harden a system. If you have a subscription to O'Reilly through work or school, I suggest checking the book out.
Disclaimer
All tasks for this room were completed using Ubuntu 18.04 LTS. That being said, pretty much everything that applies to 18.04 can apply to 20.04 as well. If you take what you learn out of this room and try to apply it in the real world for practice and fun and something does not work, be sure to check the documentation for what you are trying to do.
### ~~~~~ Chapter 3 Quiz ~~~~~
Summary
I hope you're continuing to learn something new with each chapter. Even if some of this is re-hashing old concepts, maybe there has been some things you've forgotten. We've gone through GPG and encryption, creating SSH keys, and some methods to harden SSH further.
Now it's time to complete a little skills check and see how well you understand the material.
Which SSH Protocol version is the most secure?
*2*
This is a random, arbitrary number, used as the session key, that is used to encrypt GPG.
*nonce*
Yey/Ney - GPG is based off of the OpenGPG standard
*Yey*
What is the command to generate your GPG keys?
*gpg --gen-key*
```text
┌──(kali㉿kali)-[~]
└─$ gpg --gen-key                                     
gpg (GnuPG) 2.2.39; Copyright (C) 2022 g10 Code GmbH
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Note: Use "gpg --full-generate-key" for a full featured key generation dialog.

GnuPG needs to construct a user ID to identify your key.

Real name:
```
What is the command to symmetrically encrypt a file with GPG?
*gpg -c*
```text
┌──(kali㉿kali)-[~]
└─$ gpg -h                                                      
gpg (GnuPG) 2.2.39
libgcrypt 1.10.1
Copyright (C) 2022 g10 Code GmbH
License GNU GPL-3.0-or-later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Home: /home/kali/.gnupg
Supported algorithms:
Pubkey: RSA, ELG, DSA, ECDH, ECDSA, EDDSA
Cipher: IDEA, 3DES, CAST5, BLOWFISH, AES, AES192, AES256, TWOFISH,
        CAMELLIA128, CAMELLIA192, CAMELLIA256
Hash: SHA1, RIPEMD160, SHA256, SHA384, SHA512, SHA224
Compression: Uncompressed, ZIP, ZLIB, BZIP2

Syntax: gpg [options] [files]
Sign, check, encrypt or decrypt
Default operation depends on the input data

Commands:
 
 -s, --sign                         make a signature
     --clear-sign                   make a clear text signature
 -b, --detach-sign                  make a detached signature
 -e, --encrypt                      encrypt data
 -c, --symmetric                    encryption only with symmetric cipher
 -d, --decrypt                      decrypt data (default)
     --verify                       verify a signature
 -k, --list-keys                    list keys
     --list-signatures              list keys and signatures
     --check-signatures             list and check key signatures
     --fingerprint                  list keys and fingerprints
 -K, --list-secret-keys             list secret keys
     --generate-key                 generate a new key pair
     --quick-generate-key           quickly generate a new key pair
     --quick-add-uid                quickly add a new user-id
     --quick-revoke-uid             quickly revoke a user-id
     --quick-set-expire             quickly set a new expiration date
     --full-generate-key            full featured key pair generation
     --generate-revocation          generate a revocation certificate
     --delete-keys                  remove keys from the public keyring
     --delete-secret-keys           remove keys from the secret keyring
     --quick-sign-key               quickly sign a key
     --quick-lsign-key              quickly sign a key locally
     --quick-revoke-sig             quickly revoke a key signature
     --sign-key                     sign a key
     --lsign-key                    sign a key locally
     --edit-key                     sign or edit a key
     --change-passphrase            change a passphrase
     --export                       export keys
     --send-keys                    export keys to a keyserver
     --receive-keys                 import keys from a keyserver
     --search-keys                  search for keys on a keyserver
     --refresh-keys                 update all keys from a keyserver
     --import                       import/merge keys
     --card-status                  print the card status
     --edit-card                    change data on a card
     --change-pin                   change a card's PIN
     --update-trustdb               update the trust database
     --print-md                     print message digests
     --server                       run in server mode
     --tofu-policy VALUE            set the TOFU policy for a key

Options controlling the diagnostic output:
 -v, --verbose                      verbose
 -q, --quiet                        be somewhat more quiet
     --options FILE                 read options from FILE
     --log-file FILE                write server mode logs to FILE

Options controlling the configuration:
     --default-key NAME             use NAME as default secret key
     --encrypt-to NAME              encrypt to user ID NAME as well
     --group SPEC                   set up email aliases
     --openpgp                      use strict OpenPGP behavior
 -n, --dry-run                      do not make any changes
 -i, --interactive                  prompt before overwriting

Options controlling the output:
 -a, --armor                        create ascii armored output
 -o, --output FILE                  write output to FILE
     --textmode                     use canonical text mode
 -z N                               set compress level to N (0 disables)

Options controlling key import and export:
     --auto-key-locate MECHANISMS   use MECHANISMS to locate keys by mail address
     --auto-key-import              import missing key from a signature
     --include-key-block            include the public key in signatures
     --disable-dirmngr              disable all access to the dirmngr

Options to specify keys:
 -r, --recipient USER-ID            encrypt for USER-ID
 -u, --local-user USER-ID           use USER-ID to sign or decrypt

(See the man page for a complete listing of all commands and options)

Examples:

 -se -r Bob [file]          sign and encrypt for user Bob
 --clear-sign [file]        make a clear text signature
 --detach-sign [file]       make a detached signature
 --list-keys [names]        show keys
 --fingerprint [names]      show fingerprints

Please report bugs to <https://bugs.gnupg.org>.
```
What is the command to asymmetrically encrypt a file with GPG?
*gpg -e*
```text
┌──(kali㉿kali)-[~]
└─$ ssh-keygen -t rsa       
Generating public/private rsa key pair.
Enter file in which to save the key (/home/kali/.ssh/id_rsa)
```
What is the command to create SSH keys?
*ssh-keygen*
Where are ssh keys stored in a user's home directory?
The directory name
*.ssh*
What option needs to be set to select the type of key to generate for SSH?
*-t*
The SSH configuration options presented in this chapter were found in what file (full path)?
*/etc/ssh/sshd_config*
### GNU Privacy Guard
GNU Privacy Guard
![](https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Gnupg_logo.svg/636px-Gnupg_logo.svg.png)
To understand what GNU Privacy Guard (GPG) is and does, we need to start with the original encryption system it's based off of; Pretty Good Privacy.
Overview of Pretty Good Privacy
Pretty Good Privacy (PGP) is used widely to encrypt and decrypt email by using asymmetrical and symmetrical systems. When you first send your email, it is encrypted with your own public key, as well as a session key, which is a one-time use random number called a nonce. The session key is then encrypted into the public key and sent with the cipher text. To decrypt your email, the receiving end must use their private key in order to discover the session key. The session key combined with the private key are then used to decrypt the cipher text back into the original document.
This is where GPG comes in. GPG is actually directly based off of the OpenPGP standard. GPG comes pre-installed on Ubuntu and comes with several advantages:
Easy encryption for email and files
Even the NSA can't crack PGP https://twitter.com/Snowden/status/878686842631139334?s=20
Asymmetric encryption removes the need to provide a password for decrypting or unlocking files thus improving security overall
Using GPG
﻿Creating GPG Keys
When you first want to use GPG, it requires you to create your own keys. To do that we use gpg --gen-key.
This process is extremely simple. Once you press Enter after inputting the above command, it will create some files and directories as well as ask for some information:
![](https://i.imgur.com/4dw6YWA.png)
I've just entered fake information for this user (the key generation process will still work).
Following that, the program will proceed to generate random bytes for the key. It informs the user that
![](https://i.imgur.com/4eClzUl.png)
So go ahead and move your mouse, type some stuff out or engage the disks. I just moved the mouse around...a lot. After quite some time, the process will complete and create another directory in your home directory called .gnugpg.
![](https://i.imgur.com/R0o9dGF.png)
You can verify the keys were created with gpg --list-keys.
```text

```
```text
┌──(kali㉿kali)-[~]
└─$ gpg --gen-key
gpg (GnuPG) 2.2.39; Copyright (C) 2022 g10 Code GmbH
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Note: Use "gpg --full-generate-key" for a full featured key generation dialog.

GnuPG needs to construct a user ID to identify your key.

Real name: witty
Email address: witty@email.com
You selected this USER-ID:
    "witty <witty@email.com>"

Change (N)ame, (E)mail, or (O)kay/(Q)uit? O
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: directory '/home/kali/.gnupg/openpgp-revocs.d' created
gpg: revocation certificate stored as '/home/kali/.gnupg/openpgp-revocs.d/CD881F54294C394D1DACAF9515EA3A624E2D604E.rev'
public and secret key created and signed.

pub   rsa3072 2022-10-23 [SC] [expires: 2024-10-22]
      [REDACTED]
uid                      witty <witty@email.com>
sub   rsa3072 2022-10-23 [E] [expires: 2024-10-22]
```
```text
┌──(kali㉿kali)-[~]
└─$ gpg --list-keys
gpg: checking the trustdb
gpg: marginals needed: 3  completes needed: 1  trust model: pgp
gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
gpg: next trustdb check due at 2024-10-22
/home/kali/.gnupg/pubring.kbx
-----------------------------
pub   dsa3072 2020-03-11 [SCA]
      [REDACTED]
uid           [ unknown] tryhackme <stuxnet@tryhackme.com>
sub   elg1024 2020-03-11 [E]

pub   rsa2048 2020-11-08 [SC] [expires: 2022-11-08]
      [REDACTED]
uid           [ unknown] Paradox <paradox@overpass.thm>
sub   rsa2048 2020-11-08 [E] [expires: 2022-11-08]

pub   dsa2048 2019-08-12 [SCA]
      [REDACTED]
uid           [ unknown] anonforce <melodias@anonforce.nsa>
sub   elg512 2019-08-12 [E]

pub   rsa3072 2022-10-23 [SC] [expires: 2024-10-22]
      [REDACTED]
uid           [ultimate] witty <witty@email.com>
sub   rsa3072 2022-10-23 [E] [expires: 2024-10-22]
```
### Encrypting Your Files
Encrypting Your Files with GPG
Symmetric
Symmetric encryption works by using only one key to encrypt and decrypt. In our case here, you'll see that we encrypt a text file with a passphrase and then anyone that wants to decrypt and read that file must know the passphrase.
What if we have a secret file that we don't want anyone with prying eyes to just be able to read? We can encrypt it! We do so with gpg -c <our_file> .
![](https://i.imgur.com/AKlotyu.png)
![[Pasted image 20221022195701.png]]
This will prompt the user to enter a passphrase to protect the file.
*Note* This is not the passphrase you used to create your keys
Oddly enough, symmetrically encrypting your file leaves a backup copy that's unencrypted. You can remove it with shred or rm. Then let's decrypt our file and see what's inside!
![](https://i.imgur.com/YYCKsH5.png)
```text
┌──(kali㉿kali)-[~]
└─$ gpg -d top.txt.gpg
gpg: AES256.CFB encrypted data
gpg: encrypted with 1 passphrase
gpg top :)
```
As you can see, we can decrypt our file with the -d option while targeting our gpg file that was encrypted. This will print out the contents of the file after prompting for the secret passphrase.  Let's move on to encrypting using asymmetric encryption.
Asymmetric
Asymmetric encryption works by using two keys - one to encrypt, and one to decrypt. The public key is used to encrypt the data while the private key is used to decrypt the data. So using the typical Bob and Alice example, let's say Bob wants to send Alice an encrypted file.
He would first encrypt the file using Alice's public key and then send the file away. Once Alice receives the file, she can decrypt it with her private key. The big takeaway here is that public keys can be shared, private keys should be kept private and held onto for dear life. NEVER SHARE YOUR PRIVATE KEY!
We'll need two users here. For this example, we'll use Nick and Spooky. Nick has a really super, secret file he wants to share but he doesn't want to have to share a passphrase. In order to do this, both parties need to have generated keys using the method from the previous task.
Since the public key is used to encrypt the data, both Nick and Spooky need to extract their public keys and send them to each other. We do that by navigating to the .gnupg folder and then gpg --export -a -o <filename>.  This will export the user's public key as ASCII armored output as the filename specified. In order to import the file, you need to be in that user's .gnupg directory or know the path.
![](https://i.imgur.com/faW6bw6.png)
```text
┌──(kali㉿kali)-[~/.gnupg]
└─$ gpg --export -a -o witty_public_key.txt
```
```text
┌──(kali㉿kali)-[~/.gnupg]
└─$ ls
openpgp-revocs.d   pubring.kbx   random_seed  witty_public_key.txt
private-keys-v1.d  pubring.kbx~  trustdb.gpg
```
```text
┌──(kali㉿kali)-[~/.gnupg]
└─$ gpg --import witty_public_key.txt                        
gpg: key[REDACTED]: "tryhackme <stuxnet@tryhackme.com>" not changed
gpg: key [REDACTED]: "Paradox <paradox@overpass.thm>" not changed
gpg: key [REDACTED]: "anonforce <melodias@anonforce.nsa>" not changed
gpg: key [REDACTED]: "witty <witty@email.com>" not changed
gpg: Total number processed: 4
gpg:              unchanged: 4
```
As easy as that, we can import Spooky's key and he can import Nick's public key using the same command but changing the file name.
Now, let's say Nick wants to send Spooky an encrypted file. He has some really important document he needs to send. He will encrypt his document asymmetrically with gpg -e <document>.
![](https://i.imgur.com/cI5eSD3.png)
Now, normally, Nick would send this file to Spooky through Email, IRC, Discord, or some other secure method (carrier pigeon lol).  In this case we'll just place it in /tmp. When Spooky goes to decrypt it, he will be prompted for his passphrase for his private key. After entering that he is greeted with the text from the file!
![](https://i.imgur.com/GRc6iAl.png)
So, not really anything super important here...but it could be!
```text
┌──(kali㉿kali)-[~]
└─$ gpg -e anonymous.txt 
You did not specify a user ID. (you may use "-r")

Current recipients:

Enter the user ID.  End with an empty line: witty

Current recipients:
rsa3072/466E734D80B976F9 2022-10-23 "witty <witty@email.com>"

Enter the user ID.  End with an empty line: stuxnet
gpg: 61E104A66184FBCC: There is no assurance this key belongs to the named user

sub  elg1024/61E104A66184FBCC 2020-03-11 tryhackme <stuxnet@tryhackme.com>
 Primary key fingerprint: 14B3 794D 5554 349A 715C  DBA0 8F3D A3DE C670 7170
      Subkey fingerprint: 8801 18AB 8F71 8E51 95BC  AD41 61E1 04A6 6184 FBCC

It is NOT certain that the key belongs to the person named
in the user ID.  If you *really* know what you are doing,
you may answer the next question with yes.

Use this key anyway? (y/N) y

Current recipients:
elg1024/61E104A66184FBCC 2020-03-11 "tryhackme <stuxnet@tryhackme.com>"
rsa3072/466E734D80B976F9 2022-10-23 "witty <witty@email.com>"

Enter the user ID.  End with an empty line:
```
```text
┌──(kali㉿kali)-[~]
└─$ ls -la 
total 67108
drwxr-xr-x 55 kali kali     4096 Oct 22 21:20 .
drwxr-xr-x  3 root root     4096 May 12 11:52 ..
-rw-r--r--  1 kali kali       34 Oct 21 00:46 1_hash
-rw-r--r--  1 kali kali       33 Oct 21 16:36 2_hash
-rw-r--r--  1 kali kali     1458 Sep 25 15:49 47799.txt
-rw-r--r--  1 kali kali       65 Sep 27 19:01 agent.hash
drwxr-xr-x  2 kali kali     4096 Sep 27 12:09 alfred
-rw-r--r--  1 kali kali        6 Oct 22 21:18 anonymous.txt
-rw-r--r--  1 kali kali      738 Oct 22 21:20 anonymous.txt.gpg
```
```text
┌──(kali㉿kali)-[~]
└─$ gpg -d anonymous.txt.gpg 
wgpg: encrypted with 1024-bit ELG key, ID 61E104A66184FBCC, created 2020-03-11
      "tryhackme <stuxnet@tryhackme.com>"
gpg: public key decryption failed: Timeout
gpg: encrypted with 3072-bit RSA key, ID 466E734D80B976F9, created 2022-10-23
      "witty <witty@email.com>"
u r 9
```
![[Pasted image 20221022202335.png]]
```text
┌──(kali㉿kali)-[~]
└─$ gpg --gen-key                    
gpg (GnuPG) 2.2.39; Copyright (C) 2022 g10 Code GmbH
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Note: Use "gpg --full-generate-key" for a full featured key generation dialog.

GnuPG needs to construct a user ID to identify your key.

Real name: jesus
Email address: wittyale@mailfence.com
You selected this USER-ID:
    "jesus <wittyale@mailfence.com>"

Change (N)ame, (E)mail, or (O)kay/(Q)uit? E
Email address: wittyale@mailfence.com
You selected this USER-ID:
    "jesus <wittyale@mailfence.com>"

Change (N)ame, (E)mail, or (O)kay/(Q)uit? O
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: revocation certificate stored as '/home/kali/.gnupg/openpgp-revocs.d/C3E184FC5B3A439C70EC6C294603CAD422451D2E.rev'
public and secret key created and signed.

pub   rsa3072 2022-10-23 [SC] [expires: 2024-10-22]
      [REDACTED]
uid                      jesus <wittyale@mailfence.com>
sub   rsa3072 2022-10-23 [E] [expires: 2024-10-22]
```
```text
┌──(kali㉿kali)-[~]
└─$ gpg --list-keys
gpg: checking the trustdb
gpg: marginals needed: 3  completes needed: 1  trust model: pgp
gpg: depth: 0  valid:   2  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 2u
gpg: next trustdb check due at 2024-10-22
/home/kali/.gnupg/pubring.kbx
-----------------------------
pub   dsa3072 2020-03-11 [SCA]
       [REDACTED]
uid           [ unknown] tryhackme <stuxnet@tryhackme.com>
sub   elg1024 2020-03-11 [E]

pub   rsa2048 2020-11-08 [SC] [expires: 2022-11-08]
      [REDACTED]
uid           [ unknown] Paradox <paradox@overpass.thm>
sub   rsa2048 2020-11-08 [E] [expires: 2022-11-08]

