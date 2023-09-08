---
Learn how to harden an Ubuntu Server! Covers a wide range of topics (Part 1)
---

# Hardening Basics Part 1 — Writeup

## Overview
### Hardening Basics Part 1 — Writeup
### Hardening Basics Part 1 — Writeup
![|333](https://tryhackme-images.s3.amazonaws.com/room-icons/7c26efd9aef602a7bc03b2feb0e06067.jpeg)
### Hardening Basics
![|333](https://cdn.pixabay.com/photo/2014/02/13/07/28/security-265130_960_720.jpg)
Welcome to the walkthrough for Harden. In this room, we will explore the different ways to protect an Ubuntu 18.04 Server. Tasks will cover a wide range of hardening topics with challenges along the way to prove your mettle and test your knowledge. You can look forward to the following topics:
User Accounts
Firewall Security
SSH and Encryption
Mandatory Access Control
There are no questions related to performing tasks on a virtual machine. However, I have provided a semi-configured Ubuntu 18.04 environment for you to play around with while you go through the different tasks. Things that have been configured at a basic level will be:
Users
PAM
Permissions
Passwords
And that's it! I'll leave you to play around as you wish. You may access the machine with the following credentials:
spooky:tryhackme
These will be global credentials that should give you access to do everything you need to.  I will provide other credentials for tasks where I feel it's possible to lock yourself out from a mistake. You can find some optional challenges in Part 2 of this room series.
The hope is that by the end of this room, you'll be able to clearly explain and understand the above topics and apply them to your daily life, or life at work. Whether you're a senior systems administrator or just starting out as a junior, these topics will help you understand what it takes to harden a Linux system.
Topics have been chosen from [this](https://www.oreilly.com/library/view/mastering-linux-security/9781788620307/) book. I looked through the table of contents and picked out the ones that would be the most important and allow the room to have the best content while still keeping it within the proper limits. I think the above 4 topics are the best and will give you the most knowledge on how to harden a system. If you have a subscription to O'Reilly through work or school, I suggest checking the book out.
Disclaimer
All tasks for this room were completed using Ubuntu 18.04 LTS. That being said, pretty much everything that applies to 18.04 can apply to 20.04 as well. If you take what you learn out of this room and try to apply it in the real world for practice and fun and something does not work, be sure to check the documentation for what you are trying to do.
### ~~~~~ Chapter 1: Securing User Accounts ~~~~~
Chapter 1: Securing User Accounts
Managing the users of any system is no small task. The principle of least privilege states that each user should only have enough access to perform their daily tasks. This means that an HR Admin should not have access to the system log files. However, this may mean that an IT Administrator does have access to the HR drive but not necessarily employee information. This chapter will focus on securing your user accounts through the smart configuration of sudo, using complex passwords, disabling root access and locking down home directories.

## Privilege Escalation
﻿The Dangers of Root
The root user is the highest user in a Linux system. They are able to do anything, including modifying system and boot files.  Knowing that, you can see why logging in as root is probably not ideal in most situations.
Being on a site like this, you probably use root to utilize the features of your Kali, Parrot, or other hacking Operating System.  In an environment like this, it's completely fine. But in the real world, using root can be and should be viewed as a danger to your system and company.
There is a tool in Linux that allows users to use their standard user accounts but still access programs and binaries as if they were root with their standard user passwords. That tool is sudo.
### Sudo (Part 1)
![](https://imgs.xkcd.com/comics/sandwich.png)
https://xkcd.com/149/
What is sudo?
sudo stands for "super-user do". Sudo allows any non-root user to run applications as root. It's as simple as that.
Why is sudo Important?
sudo is important to system administrators because it means they can allow certain users to perform actions with sudo while still having that user keep his/her privileges.
Let's say Nick is a Junior System Administrator and he's asked by his senior to perform some tasks. He's asked to:
Install a package that the team will need (apt install)
Reload the Apache web server after the senior made some configuration changes (systemctl reload apache2)
Each of these tasks will require Nick to use sudo before being able to perform them. Doing so will grant him root user privileges for the duration of that program and then returns back to Nick's default privileges.
Advantages of sudo
It was touched on above but when sudo is configured correctly, it greatly increases the security of your Linux environment. There are a few advantages it has such as:
Slowing hackers down. Since the root login will most likely be disabled and your users are properly granted sudo, any attacker will not know which account to go after, thus slowing them down. If they are slowed down enough, they may stop the attack and give up
Allow non-privileged users to perform privileged tasks by entering their own passwords
Keeps in line with the principle of least privilege by allowing administrators to assign certain users full privileges, while assigning other users only the privileges they need to complete their daily tasks
﻿Adding Users to a Predefined Admin Group
Method 1
This is the first way to add users to the sudo group. Generally, this is considered the easiest method to allow users to use the sudo command. On Ubuntu 18.04, unless otherwise specified upon account creation, the user is automatically added to the sudo group. Let's take a look at nick's groups with the groups command.
![](https://i.imgur.com/gQ9BJHK.png)
We can see that Nick is a part of the sudo group (as well as a few others). If Nick was not part of the sudo group already, we could easily add him with one simple command: usermod -aG sudo nick. The -aG options here will add Nick to the group sudo. Using the -a option helps Nick retain any previously existing groups. You can also directly add a user to the sudo group upon creation with the command, useradd -G sudo james .
But what does adding a user to the sudo group in Ubuntu mean? By default, Ubuntu allows sudo users to execute any program as root with their password. There are a few ways we can check this information. The first way is as Nick with sudo -l .
![](https://i.imgur.com/5tTDatO.png)
The important information are in the last lines. This is saying that Nick (as part of the sudo group) may run all commands as any user on any machine.
There's another way to view this information and that's with visudo. This opens the sudo policy file. The sudo policy file is stored in /etc/sudoers. We can do it here as Nick, but we would need to use sudo if we want to edit it since it can only be edited by the root user (using just visudo as Nick actually gives a permission denied).
![](https://i.imgur.com/urlodE6.png)
This gives the same information as sudo -l but it has one difference; the "%sudo" indicates that it's for the group, sudo. There are other groups in this file such as "admin". This is where administrators can set what programs a user in a certain group can perform and whether or not they need a password. You may have seen sometimes %sudo ALL=(ALL:ALL) ALL NOPASSWD: ALL. That NOPASSWD part says that the user that is part of the sudo group does not need to enter their local password to use sudo privileges. Generally, this is not recommended - even for home use.
Method 2
This next method utilizes the sudo policy file mentioned in Method 1. It's nice to be able to modify what an entire group can do, but that's just for Ubuntu.  If you're managing users in a network across multiple flavors of Linux (CentOS, Red Hat, etc.), where the sudo group may be called something different, this method may be more preferable.
What you can do is add a User Alias to the policy file and add users to that alias (below), or add lines for individual users.  The first image below creates the ADMIN User Alias and assigns 3 users to it and then says that this Alias has full sudo powers.
```text
# User alias specification
User_Alias     ADMINS = spooky, james
               ADMINS ALL=(ALL) ALL
```
![](https://i.imgur.com/duOu7Xk.png)
![](https://i.imgur.com/f9Ma1M3.png)
I would not recommend the second option (individual user aliases) in a large network since this can become unwieldy very quickly.﻿ The first option is going to be your best bet as you'll see in the next Task that we can simply add users to this alias and control which commands they have access to with sudo very easily.
### Sudo (Part 2)
Setting Up sudo for Only Certain Delegated Privileges﻿
Assigning Command Aliases
﻿In the previous task, we saw how we can add users to the sudo group, and set up a User Alias in the sudo policy file, visudo.
I know I've hammered this point a lot in these two tasks, but the next method that we'll talk about here will ensure that users are assigned to the groups they belong to and only are allowed access to the programs they need to complete their daily tasks. This is how sudo aligns with the principle of least privilege.
It does this by allowing the root user to set what are called Command Aliases in the sudo policy file. Just as we set a User Alias in this file in the last task, we'll set a Command Alias now in the same file. Since we've already gone over it, I'm going to create another User Alias with the name of SYSTEMADMINS and assign some users to it. So again, using sudo visudo, we'll edit the line under the comment # Cmnd alias specification
We'll just add a few commands to the list. These don't mean anything in the actual context of what a System Admin would need. In reality, a System Admin would probably have sudo access to most things, but for brevity, let's only include a few.
```text
# Cmnd alias specification
Cmnd_ALias SYSTEM = /usr/bin/systemctl restart , /usr/bin/systemctl restart ssh, /bin/chmod
```
![](https://i.imgur.com/xR4UEGY.png)
![](https://i.imgur.com/KzIXxeE.png)
The SYSTEM Command Alias allows the user to run systemctl restart, systemctl restart ssh and chmod . What do you think will happen if someone in the SYSTEMADMINS User Alias tried to run systemctl restart apache2? It would fail because that specific service has not been specified in the Alias. However, they are able to restart the ssh service because this is specified. And lastly, they can use chmod with all options.
If we wanted to allow the SYSTEMADMINS User Alias to be able to restart all services, we can use a wildcard character at the end so the new Alias would look like /usr/bin/systemctl restart *.
Different Ways to Assign Commands
We can also assign Command Aliases to individual users, specific commands to individual users, and Command Aliases to groups:
![](https://i.imgur.com/cRtduDI.png)
So dark is assigned specifically to the WEBDEV Command Alias, the user paradox is assigned only the cd command (poor Paradox) and the HR User Alias can only perform tasks in the HR Command Alias. See how useful the sudo policy can be in allowing you to separate privileges?
A Mention of Host Aliases
Host Aliases exist. They are a way to trickle down a sudo policy across the network and different servers. For example, you may have a MAILSERVERS Host Alias which contains servers mail1 and mail2. This Host Alias has certain users or groups assigned to it like we've demonstrated in these last two tasks and that Host Alias has a Command Alias assigned to it stating which commands those users are able to run.
When those users run a command on mail1 or mail2, the server will check the sudo policy file to see if they can do what they're trying to do.
I don't want to go into too much detail about it here because in a home environment and small-medium business environments, it probably is just easier to copy the sudo policy file to each server in the network.  This will really only come into play with large enterprise networks and even then they will probably be using one centralized Ansible or other automation in effect.
http://www.silcom.com.pe/servicios_automatizacion_ansible.html
Disabling Root Access
Restrict Root Shell Access
Generally it's a good idea to restrict root access. You can do this through several methods:
Disabling the root login shell
Disabling root SSH login
Disabling root using PAM (Password Authentication Module)
Disable Root Login Shell
Disabling the root login shell is a very simple task. You need to edit the /etc/passwd file to be the following:
![](https://i.imgur.com/stm8Mb4.png)
```text
root:x:0:0:root:/root:/usr/sbin/nologin
```
Normally, this is set to /bin/bash but setting it to /usr/sbin/nologin will politely reject the root login. Doing this will prevent users from doing sudo -s
Disable Root SSH Login
Disabling the root SSH login is another simple task that's fixed with one simple configuration change in /etc/ssh/sshd_config.conf
![](https://i.imgur.com/sb7m6tR.png)
```text
spooky@harden:/etc/ssh$ cat sshd_config
```
```text
#       $OpenBSD: sshd_config,v 1.101 2017/03/14 07:19:07 djm Exp $
```
```text
# This is the sshd server system-wide configuration file.  See
```
```text
# sshd_config(5) for more information.
```
```text
# This sshd was compiled with PATH=/usr/bin:/bin:/usr/sbin:/sbin
```
```text
# The strategy used for options in the default sshd_config shipped with
```
```text
# OpenSSH is to specify options with their default value where
```
```text
# possible, but leave them commented.  Uncommented options override the
```
```text
# default value.

#Port 22
#AddressFamily any
#ListenAddress 0.0.0.0
#ListenAddress ::

#HostKey /etc/ssh/ssh_host_rsa_key
#HostKey /etc/ssh/ssh_host_ecdsa_key
#HostKey /etc/ssh/ssh_host_ed25519_key
```
```text
# Ciphers and keying
#RekeyLimit default none
```
```text
# Logging
#SyslogFacility AUTH
#LogLevel INFO
```
```text
# Authentication:

#LoginGraceTime 2m
PermitRootLogin yes

in this case just change yes to no
PermitRootLogin no
```
We change the #PermitRootLogin to no. Easy.
Disable Root Using PAM
This is one that I didn't even know about so bare with me here. For those that don't know, the PAM is "a powerful suite of shared libraries used to dynamically authenticate a user to applications (or services) in a Linux system" (Tecmint). The PAM settings are controlled by the conf file in /etc/pam.d or /etc/pam.conf. The pam.conf file warns us
https://www.tecmint.com/configure-pam-in-centos-ubuntu-linux/
![](https://i.imgur.com/0uiXAo8.png)
!!! WARNING !!! Editing the /etc/pam.d/* or /etc/pam.conf files can lock you out of your system.
I'll go through one example because there's a lot to it. Let's look at the example of disabling root SSHD login because that seems to be a common theme among articles online. We can configure our /etc/pam.d/sshd like the following
![](https://i.imgur.com/brp6EOW.png)
And lastly in /etc/ssh, we make a file called deniedusers and use vim to add root to the top and then save and close.
For the above configuration, the below explains what each setting does (Tecmint)
auth: the module type
required: a flag that states if the above module is used, it must pass, otherwise fail.
pam_listfile.so: a module that provides a way to deny or allow services based on an arbitrary file
onerr=succeed: module argument
item=user: module argument that specifies what is listed in the file and should be checked for
sense=deny: module argument which specifies the action to take if the name is found in the file. If not found, then the opposite action is requested
file=/etc/ssh/deniedusers: module argument; specifies file containing one line per argument (in this case, our users that are denied access)
```text
# Custom PAM Configurations
auth    required        pam_listfile.so \
        onerr=succeed   item=user       sense=deny      file=/etc/ssh/deniedusers

root@harden:/etc/ssh# cat deniedusers 
root
```
Disabling Shell Escapes
If you've ever visited GTFOBins, then you know that there exist ways for non-privileged users to escalate their privileges to root using shell escapes in text editors. Looking at the simple example of vim from GTFOBins, we see the following escapes:
![](https://i.imgur.com/mX6QdU2.png)
Escape (a) has you adding the -c option which will execute the following command, which in this case is /bin/sh.
Escape (b) has you setting the variable "shell" to /bin/sh and then calling it.
If, in either of these examples, you are able to run vim with sudo, either of these will escape you into a root shell
![](https://i.imgur.com/rOWyPQg.png)
In order to get around this issue, use sudoedit in the sudo policy file instead of any editor as sudoedit does not have any shell escapes. You can do this with the following:
![](https://i.imgur.com/XDBIAL6.png)
```text
spooky@harden:/etc/pam.d$ sudoedit hi
spooky@harden:/etc/pam.d$ ls
atd              common-session-noninteractive  runuser
chfn             cron                           runuser-l
chpasswd         hi                             sshd
chsh             login                          su
common-account   newusers                       sudo
common-auth      other                          systemd-user
common-password  passwd                         vmtoolsd
common-session   polkit-1
spooky@harden:/etc/pam.d$ cat hi
hi

spooky@harden:/etc/pam.d$ nano hi (with nano, vim, vi cannot modified, just only with sudoedit)
spooky@harden:/etc/pam.d$ sudoedit hi
spooky@harden:/etc/pam.d$ cat hi
hi :)
```
### Locking Home Directories
Quick Note on Locking a User's Home Directory in Ubuntu
Ubuntu by default sets a new user's home directory permissions to 755 (UMASK of 022). This means that any other user and group can read and write in that user's directory. This is generally not good practice and it's up to the system admin to change this. The UMASK is set in /etc/login.defs so let's take a look at that file real quick.
![](https://i.imgur.com/wVhHmsC.png)
Specifically, we're looking at the boxed UMASK in this screenshot, but pay attention to the long note that Ubuntu gives. They even state that 077 would be more secure. So changing that here will automatically make any new user's home directory more secure.  Awesome stuff.
Note: The resulting permissions that get set are just 777 - UMASK so in this case:
777
022
-------
755
Since 777 is the numerical equivalent of rwxrwxrwx in Linux, subtracting that from the UMASK, you get the resulting permissions that will be set on a user's home directory and files.
so with 077 will be 777 - 077 = 700
### Configuring Password Complexity
Pwquality
﻿Pwquality is a PAM module that allows you to configure password complexity requirements for your users. It's fairly easy to install on Ubuntu. You'll do sudo apt-get install libpam-pwquality. Once installed, it automatically adds an entry into the /etc/pam.d/common-password file. The pam.d directory is just another location where PAM adds files for basic services like ssh, basic login, etc.
```text
spooky@harden:/etc/pam.d$ cat common-password | grep pwquality
password        requisite                       pam_pwquality.so retry=3,minlen=8,difok=3,lcredit=-1,ucredit=-1,dcredit=-1,ocredit=-1
```
![](https://i.imgur.com/EbcQ5un.png)
Remember from before how to read this?  There's a few differences but let's take a look:
password: module
requisite: module; states that if the the module fails, the operation is immediately terminated with a failure without invoking other modules
pam_pwquality.so: checks the pwquality.conf file for the requirements
retry=3: allows the user to retry their password 3 times before returning with an error
If we look at a few lines from the pwquality.conf file found in /etc/security, we can see that there are many options the administrator can set for the password quality.  The lines just need to be uncommented and modified.
```text
spooky@harden:/etc/security$ cat pwquality.conf
```
```text
# Configuration for systemwide password quality limits
```
```text
# Defaults:
#
```
```text
# Number of characters in the new password that must not be present in the
```
```text
# old password.
```
```text
# difok = 1
#
```
```text
# Minimum acceptable size for the new password (plus one if
```
```text
# credits are not disabled which is the default). (See pam_cracklib manual.)
```
```text
# Cannot be set to lower value than 6.
```
```text
# minlen = 8
#
```
```text
# The maximum credit for having digits in the new password. If less than 0
```
```text
# it is the minimum number of digits in the new password.
```
```text
# dcredit = 0
#
```
```text
# The maximum credit for having uppercase characters in the new password.
```
```text
# If less than 0 it is the minimum number of uppercase characters in the new
```
```text
# password.
```
```text
# ucredit = 0
#
```
```text
# The maximum credit for having lowercase characters in the new password.
```
```text
# If less than 0 it is the minimum number of lowercase characters in the new
```
```text
# password.
```
```text
# lcredit = 0
#
```
```text
# The maximum credit for having other characters in the new password.
```
```text
# If less than 0 it is the minimum number of other characters in the new
```
```text
# password.
```
```text
# ocredit = 0
#
```
```text
# The minimum number of required classes of characters for the new
```
```text
# password (digits, uppercase, lowercase, others).
```
```text
# minclass = 0
#
```
```text
# The maximum number of allowed consecutive same characters in the new password.
```
```text
# The check is disabled if the value is 0.
```
```text
# maxrepeat = 0
#
```
```text
# The maximum number of allowed consecutive characters of the same class in the
```
```text
# new password.
```
```text
# The check is disabled if the value is 0.
```
```text
# maxclassrepeat = 0
#
```
```text
# Whether to check for the words from the passwd entry GECOS string of the user.
```
```text
# The check is enabled if the value is not 0.
```
```text
# gecoscheck = 0
#
```
```text
# Whether to check for the words from the cracklib dictionary.
```
```text
# The check is enabled if the value is not 0.
```
```text
# dictcheck = 1
#
```
```text
# Whether to check if it contains the user name in some form.
```
```text
# The check is enabled if the value is not 0.
```
```text
# usercheck = 1
#
```
```text
# Whether the check is enforced by the PAM module and possibly other
```
```text
# applications.
```
```text
# The new password is rejected if it fails the check and the value is not 0.
```
```text
# enforcing = 1
#
```
```text
# Path to the cracklib dictionaries. Default is to use the cracklib default.
```
```text
# dictpath =
```
![](https://i.imgur.com/hfRwinA.png)
### Configuring Other Password Requirements
Configuring Other Password Requirements
﻿In the Security world, when we talk about passwords, there's 4 important concepts that relate to passwords. They are:
Password complexity
Password length
Password expiration
Password history
We already covered the first 2 in previous tasks by configuring pwquality for our server. Now let's cover the last 2.
Password Expiration
When we open /etc/login.defs, and scroll down to the "Password aging controls" section, we can set password expiration here.  There are a few options:
![](https://i.imgur.com/t1i0JBx.png)
```text
spooky@harden:/etc$ cat login.defs | grep PASS_
```
```text
#       PASS_MAX_DAYS   Maximum number of days a password may be used.
```
```text
#       PASS_MIN_DAYS   Minimum number of days allowed between password changes.
```
```text
#       PASS_WARN_AGE   Number of days warning given before a password expires.
PASS_MAX_DAYS   99999
PASS_MIN_DAYS   0
PASS_WARN_AGE   7
```
PASS_MAX_DAYS: Default 99999; Sets the maximum number of days a password may be used
PASS_MIN_DAYS: Default 0; Sets the minimum number of days a user must keep their password before changing it
PASS_WARN_AGE: Default 7; Sets the number of days out from expiration that the system will warn the user
It is generally considered good practice to have a user's password expire after 90 days with a minimum age of at least 1. We'll get into why when we get to Password History next.
Password History
When configuring the password history of any system, it is generally considered best practice to remember the previous 10 passwords. This will ensure that the user's passwords stay different and are not reused. As we talked about above, setting a minimum age of 1 and a password history of 10 means that somebody would need to wait at least 11 days before they're able to get back to their original password. Usually this is enough to dissuade anyone from trying.
To configure password history in Ubuntu, we're once again going to look at /etc/pam.d/common-password. Take a look at the screenshot below for a sample configuration
![](https://i.imgur.com/FXYRR7b.png)
The pwquality line from before has been removed for simplicity. Let's focus on the top line. Again, I'll go through the PAM settings.
Disclaimer: The PAM is not easy to understand. I did a lot of research and reading for any of these tasks where PAM was used.  Some of these explanations are from the documentation of pam.d found [here](https://linux.die.net/man/5/pam.d).
password: module type we are referencing
required: module where failure returns a failure to the PAM-API
pam_pwhistory.so: module that configures the password history requirements
remember=2: option for the pam_pwhistory.so module to remember the last n passwords (n = 2). These passwords are saved in /etc/security/opasswd
retry=3: option for the pam_pwhistory.so module to prompt the user 3 times before returning a failure
You may notice a change to the pam_unix.so line below the top one. We make use of use_authtok here and we tell the module to use shadow which will create shadow passwords when updating a user's password.
```text
spooky@harden:/etc/security$ sudo -s
root@harden:/etc/security# sudoedit opasswd
```
```text
# here are the per-ackage modules (the "Primary" block)
password        required        pam_pwhistory.so remember=2 retry=3
password        (success=1 default=ignore)      pam_unix.so use_authtok obscure sha512 shadow
```
### Dangers of the lxd Group
The lxd Group in Ubuntu
I figure this wouldn't be a room about hardening if I ignore the fact that for whatever reason, Ubuntu places users (unless otherwise specified) into the lxd group. This group is known to be a point of privilege escalation and should be removed from any user that is a part of it.
It's so prevalent that Linux-Smart-Enumeration even checks for it. So, just remove it from any user that has it assigned. Using adduser does not add the user to any predefined groups and should probably be used when adding new users.
