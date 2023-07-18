---
This room is an introduction to enumeration when approaching an unknown corporate environment.
---

# Enumeration — Writeup

## Enumeration
![](https://tryhackme-images.s3.amazonaws.com/room-icons/bdfcbc439aa00e2c7ba4bb8d81334490.png)
### Introduction
This room focuses on post-exploitation enumeration. In other words, we assume that we have successfully gained some form of access to a system. Moreover, we may have carried out privilege escalation; in other words, we might have administrator or root privileges on the target system. Some of the techniques and tools discussed in this room would still provide helpful output even with an unprivileged account, i.e., not root or administrator.
If you are interested in privilege escalation, you can check the Windows Privilege Escalation room and the Linux PrivEsc room. Moreover, there are two handy scripts, WinPEAS and LinPEAS for MS Windows and Linux privilege escalation respectively.
Our purpose is to collect more information that will aid us in gaining more access to the target network. For example, we might find the login credentials to grant access to another system. We focus on tools commonly available on standard systems to collect more information about the target. Being part of the system, such tools look innocuous and cause the least amount of "noise".
We assume you have access to a command-line interface on the target, such as bash on a Linux system or cmd.exe on an MS Windows system. Starting with one type of shell on a Linux system, it is usually easy to switch to another one. Similarly, starting from cmd.exe, you can switch to PowerShell if available. We just issued the command powershell.exe to start the PowerShell interactive command line in the terminal below.
```text
Terminal

           
user@TryHackMe$ Microsoft Windows [Version 10.0.17763.2928]
(c) 2018 Microsoft Corporation. All rights reserved.

strategos@RED-WIN-ENUM C:\Users\strategos>powershell.exe
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\strategos>
```
This room is organized as follows:
Purpose of enumeration
Linux enumeration with commonly-installed tools: System, users, networking, and running services
MS Windows enumeration with built-in tools: System, users, networking, and running services
Examples of additional tools: Seatbelt
Although it is not strictly necessary, we advise completing The Lay of the Land room before going through this one.
What command would you use to start the PowerShell interactive command line?
*powershell.exe*
### Purpose
When you gain a “shell” on the target system, you usually have very basic knowledge of the system. If it is a server, you already know which service you have exploited; however, you don’t necessarily know other details, such as usernames or network shares. Consequently, the shell will look like a “dark room” where you have an incomplete and vague knowledge of what’s around you. In this sense, enumeration helps you build a more complete and accurate picture.
The purpose behind post-exploitation enumeration is to gather as much information about the system and its network. The exploited system might be a company desktop/laptop or a server. We aim to collect the information that would allow us to pivot to other systems on the network or to loot the current system. Some of the information we are interested in gathering include:
Users and groups
Hostnames
Routing tables
Network shares
Network services
Applications and banners
Firewall configurations
Service settings and audit configurations
SNMP and DNS details
Hunting for credentials (saved on web browsers or client applications)
There is no way to list everything we might stumble upon. For instance, we might find SSH keys that might grant us access to other systems. In SSH key-based authentication, we generate an SSH key pair (public and private keys); the public key is installed on a server. Consequently, the server would trust any system that can prove knowledge of the related private key.
Furthermore, we might stumble upon sensitive data saved among the user’s documents or desktop directories. Think that someone might keep a passwords.txt or passwords.xlsx instead of a proper password manager. Source code might also contain keys and passwords left lurking around, especially if the source code is not intended to be made public.
In SSH key-based authentication, which key does the client need?
*private key*
This task focuses on enumerating a Linux machine after accessing a shell, such as bash. Although some commands provide information on more than one area, we tried to group the commands into four categories depending on the information we expect to acquire.
System
Users
Networking
Running Services
We recommend that you click "Start AttackBox" and "Start Machine" so that you can experiment and answer the questions at the end of this task.
System
On a Linux system, we can get more information about the Linux distribution and release version by searching for files or links that end with -release in /etc/. Running ls /etc/*-release helps us find such files. Let’s see what things look like on a CentOS Linux.
```text
Terminal

           
user@TryHackMe$ ls /etc/*-release
/etc/centos-release  /etc/os-release  /etc/redhat-release  /etc/system-release
```
```text
$ cat /etc/os-release 
NAME="CentOS Linux"
VERSION="7 (Core)"
[...]
```
Let’s try on a Fedora system.
```text
Terminal

           
user@TryHackMe$ ls /etc/*-release
/etc/fedora-release@  /etc/os-release@  /etc/redhat-release@  /etc/system-release@
```
```text
$ cat /etc/os-release
NAME="Fedora Linux"
VERSION="36 (Workstation Edition)"
[...]
```
We can find the system’s name using the command hostname.
```text
Terminal

           
user@TryHackMe$ hostname
rpm-red-enum.thm
```
Various files on a system can provide plenty of useful information. In particular, consider the following /etc/passwd, /etc/group, and /etc/shadow. Any user can read the files passwd and group. However, the shadow password file requires root privileges as it contains the hashed passwords. If you manage to break the hashes, you will know the user’s original password.
```text
Terminal

           
user@TryHackMe$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
[...]
michael:x:1001:1001::/home/michael:/bin/bash
peter:x:1002:1002::/home/peter:/bin/bash
jane:x:1003:1003::/home/jane:/bin/bash
randa:x:1004:1004::/home/randa:/bin/bash
```
```text
$ cat /etc/group
root:x:0:
[...]
michael:x:1001:
peter:x:1002:
jane:x:1003:
randa:x:1004:
```
```text
$ sudo cat /etc/shadow
root:$6$pZlRFi09$qqgNBS.00qtcUF9x0yHetjJbXsw0PAwQabpCilmAB47ye3OzmmJVfV6DxBYyUoWBHtTXPU0kQEVUQfPtZPO3C.:19131:0:99999:7:::
[...]
michael:$6$GADCGz6m$g.ROJGcSX/910DEipiPjU6clo6Z6/uBZ9Fvg3IaqsVnMA.UZtebTgGHpRU4NZFXTffjKPvOAgPKbtb2nQrVU70:19130:0:99999:7:::
peter:$6$RN4fdNxf$wvgzdlrIVYBJjKe3s2eqlIQhvMrtwAWBsjuxL5xMVaIw4nL9pCshJlrMu2iyj/NAryBmItFbhYAVznqRcFWIz1:19130:0:99999:7:::
jane:$6$Ees6f7QM$TL8D8yFXVXtIOY9sKjMqJ7BoHK1EHEeqM5dojTaqO52V6CPiGq2W6XjljOGx/08rSo4QXsBtLUC3PmewpeZ/Q0:19130:0:99999:7:::
randa:$6$dYsVoPyy$WR43vaETwoWooZvR03AZGPPKxjrGQ4jTb0uAHDy2GqGEOZyXvrQNH10tGlLIHac7EZGV8hSIfuXP0SnwVmnZn0:19130:0:99999:7:::
```
Similarly, various directories can reveal information about users and might contain sensitive files; one is the mail directories found at /var/mail/.
```text
user@TryHackMe$ ls -lh /var/mail/
total 4.0K
-rw-rw----. 1 jane      mail   0 May 18 14:15 jane
-rw-rw----. 1 michael   mail   0 May 18 14:13 michael
-rw-rw----. 1 peter     mail   0 May 18 14:14 peter
-rw-rw----. 1 randa     mail   0 May 18 14:15 randa
-rw-------. 1 root      mail 639 May 19 07:37 root
```
To find the installed applications you can consider listing the files in /usr/bin/ and /sbin/:
ls -lh /usr/bin/
ls -lh /sbin/
On an RPM-based Linux system, you can get a list of all installed packages using rpm -qa. The -qa indicates that we want to query all packages.
On a Debian-based Linux system, you can get the list of installed packages using dpkg -l. The output below is obtained from an Ubuntu server.
```text
Terminal

           
user@TryHackMe$ dpkg -l
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                                  Version                            Architecture Description
+++-=====================================-==================================-============-===============================================================================
ii  accountsservice                       0.6.55-0ubuntu12~20.04.5           amd64        query and manipulate user account information
ii  adduser                               3.118ubuntu2                       all          add and remove users and groups
ii  alsa-topology-conf                    1.2.2-1                            all          ALSA topology configuration files
ii  alsa-ucm-conf                         1.2.2-1ubuntu0.13                  all          ALSA Use Case Manager configuration files
ii  amd64-microcode                       3.20191218.1ubuntu1                amd64        Processor microcode firmware for AMD CPUs
[...   ]
ii  zlib1g-dev:amd64                      1:1.2.11.dfsg-2ubuntu1.3           amd64        compression library - development
```
Users
Files such as /etc/passwd reveal the usernames; however, various commands can provide more information and insights about other users on the system and their whereabouts.
You can show who is logged in using who.
```text
user@TryHackMe$ who
root     tty1         2022-05-18 13:24
jane     pts/0        2022-05-19 07:17 (10.20.30.105)
peter    pts/1        2022-05-19 07:13 (10.20.30.113)
```
We can see that the user root is logged in to the system directly, while the users jane and peter are connected over the network, and we can see their IP addresses.
Note that who should not be confused with whoami which prints your effective user id.
```text
Terminal

           
user@TryHackMe$ whoami
jane
```
To take things to the next level, you can use w, which shows who is logged in and what they are doing. Based on the terminal output below, peter is editing notes.txt and jane is the one running w in this example.
```text
Terminal

           
user@TryHackMe$ w
 07:18:43 up 18:05,  3 users,  load average: 0.00, 0.01, 0.05
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
root     tty1                      Wed13   17:52m  0.00s  0.00s less -s
jane     pts/0    10.20.30.105     07:17    3.00s  0.01s  0.00s w
peter    pts/1    10.20.30.113     07:13    5:23   0.00s  0.00s vi notes.txt
```
To print the real and effective user and group IDS, you can issue the command id (for ID).
```text
Terminal

           
user@TryHackMe$ id
uid=1003(jane) gid=1003(jane) groups=1003(jane) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
```
Do you want to know who has been using the system recently? last displays a listing of the last logged-in users; moreover, we can see who logged out and how much they stayed connected. In the output below, the user randa remained logged in for almost 17 hours, while the user michael logged out after four minutes.
```text
Terminal

           
user@TryHackMe$ last
jane     pts/0        10.20.30.105     Thu May 19 07:17   still logged in   
peter    pts/1        10.20.30.113     Thu May 19 07:13   still logged in   
michael  pts/0        10.20.30.1       Thu May 19 05:12 - 05:17  (00:04)    
randa    pts/1        10.20.30.107     Wed May 18 14:18 - 07:08  (16:49)    
root     tty1                          Wed May 18 13:24   still logged in
```
Finally, it is worth mentioning that sudo -l lists the allowed command for the invoking user on the current system.
Networking
The IP addresses can be shown using ip address show (which can be shortened to ip a s) or with the older command ifconfig -a (its package is no longer maintained.) The terminal output below shows the network interface ens33 with the IP address 10.20.30.129 and subnet mask 255.255.255.0 as it is 24.
```text
Terminal

           
user@TryHackMe$ ip a s
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:a2:0e:7e brd ff:ff:ff:ff:ff:ff
    inet 10.20.30.129/24 brd 10.20.30.255 scope global noprefixroute dynamic ens33
       valid_lft 1580sec preferred_lft 1580sec
    inet6 fe80::761a:b360:78:26cd/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```
The DNS servers can be found in the /etc/resolv.conf. Consider the following terminal output for a system that uses DHCP for its network configurations. The DNS, i.e. nameserver, is set to 10.20.30.2.
```text
Terminal

           
user@TryHackMe$ cat /etc/resolv.conf
```
```text
# Generated by NetworkManager
search localdomain thm
nameserver 10.20.30.2
```
netstat is a useful command for learning about network connections, routing tables, and interface statistics. We explain some of its many options in the table below.
Option 	Description
-a 	show both listening and non-listening sockets
-l 	show only listening sockets
-n 	show numeric output instead of resolving the IP address and port number
-t 	TCP
-u 	UDP
-x 	UNIX
-p 	Show the PID and name of the program to which the socket belongs
You can use any combination that suits your needs. For instance, netstat -plt will return Programs Listening on TCP sockets. As we can see in the terminal output below, sshd is listening on the SSH port, while master is listening on the SMTP port on both IPv4 and IPv6 addresses. Note that to get all PID (process ID) and program names, you need to run netstat as root or use sudo netstat.
```text
Terminal

           
user@TryHackMe$ sudo netstat -plt
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN      978/sshd            
tcp        0      0 localhost:smtp          0.0.0.0:*               LISTEN      1141/master         
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN      978/sshd            
tcp6       0      0 localhost:smtp          [::]:*                  LISTEN      1141/master
```
netstat -atupn will show All TCP and UDP listening and established connections and the program names with addresses and ports in numeric format.
```text
Terminal

           
user@TryHackMe$ sudo netstat -atupn
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      978/sshd            
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      1141/master         
tcp        0      0 10.20.30.129:22         10.20.30.113:38822        ESTABLISHED 5665/sshd: peter [p 
tcp        0      0 10.20.30.129:22         10.20.30.105:38826        ESTABLISHED 5723/sshd: jane [pr 
tcp6       0      0 :::22                   :::*                    LISTEN      978/sshd            
tcp6       0      0 ::1:25                  :::*                    LISTEN      1141/master         
udp        0      0 127.0.0.1:323           0.0.0.0:*                           640/chronyd         
udp        0      0 0.0.0.0:68              0.0.0.0:*                           5638/dhclient       
udp6       0      0 ::1:323                 :::*                                640/chronyd
```
One might think that using nmap before gaining access to the target machine would have provided a comparable result. However, this is not entirely true. Nmap needs to generate a relatively large number of packets to check for open ports, which can trigger intrusion detection and prevention systems. Furthermore, firewalls across the route can drop certain packets and hinder the scan, resulting in incomplete Nmap results.
lsof stands for List Open Files. If we want to display only Internet and network connections, we can use lsof -i. The terminal output below shows IPv4 and IPv6 listening services and ongoing connections. The user peter is connected to the server rpm-red-enum.thm on the ssh port. Note that to get the complete list of matching programs, you need to run lsof as root or use sudo lsof.
```text
Terminal

           
user@TryHackMe$ sudo lsof -i
COMMAND   PID      USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
chronyd   640    chrony    5u  IPv4  16945      0t0  UDP localhost:323 
chronyd   640    chrony    6u  IPv6  16946      0t0  UDP localhost:323 
sshd      978      root    3u  IPv4  20035      0t0  TCP *:ssh (LISTEN)
sshd      978      root    4u  IPv6  20058      0t0  TCP *:ssh (LISTEN)
master   1141      root   13u  IPv4  20665      0t0  TCP localhost:smtp (LISTEN)
master   1141      root   14u  IPv6  20666      0t0  TCP localhost:smtp (LISTEN)
dhclient 5638      root    6u  IPv4  47458      0t0  UDP *:bootpc 
sshd     5693     peter    3u  IPv4  47594      0t0  TCP rpm-red-enum.thm:ssh->10.20.30.113:38822 (ESTABLISHED)
[...]
```
Because the list can get quite lengthy, you can further filter the output by specifying the ports you are interested in, such as SMTP port 25. By running lsof -i :25, we limit the output to those related to port 25, as shown in the terminal output below. The server is listening on port 25 on both IPv4 and IPv6 addresses.
```text
Terminal

           
user@TryHackMe$ sudo lsof -i :25
COMMAND  PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
master  1141 root   13u  IPv4  20665      0t0  TCP localhost:smtp (LISTEN)
master  1141 root   14u  IPv6  20666      0t0  TCP localhost:smtp (LISTEN)
```
Running Services
Getting a snapshot of the running processes can provide many insights. ps lets you discover the running processes and plenty of information about them.
You can list every process on the system using ps -e, where -e selects all processes. For more information about the process, you can add -f for full-format and-l for long format. Experiment with ps -e, ps -ef, and ps -el.
You can get comparable output and see all the processes using BSD syntax: ps ax or ps aux. Note that a and x are necessary when using BSD syntax as they lift the “only yourself” and “must have a tty” restrictions; in other words, it becomes possible to display all processes. The u is for details about the user that has the process.
Option 	Description
-e 	all processes
-f 	full-format listing
-j 	jobs format
-l 	long format
-u 	user-oriented format
For more “visual” output, you can issue ps axjf to print a process tree. The f stands for “forest”, and it creates an ASCII art process hierarchy as shown in the terminal output below.
```text
Terminal

           
user@TryHackMe$ ps axf
   PID TTY      STAT   TIME COMMAND
     2 ?        S      0:00 [kthreadd]
     4 ?        S<     0:00  \_ [kworker/0:0H]
     5 ?        S      0:01  \_ [kworker/u256:0]
[...]
   978 ?        Ss     0:00 /usr/sbin/sshd -D
  5665 ?        Ss     0:00  \_ sshd: peter [priv]
  5693 ?        S      0:00  |   \_ sshd: peter@pts/1
  5694 pts/1    Ss     0:00  |       \_ -bash
  5713 pts/1    S+     0:00  |           \_ vi notes.txt
  5723 ?        Ss     0:00  \_ sshd: jane [priv]
  5727 ?        S      0:00      \_ sshd: jane@pts/0
  5728 pts/0    Ss     0:00          \_ -bash
  7080 pts/0    R+     0:00              \_ ps axf
   979 ?        Ssl    0:12 /usr/bin/python2 -Es /usr/sbin/tuned -l -P
   981 ?        Ssl    0:07 /usr/sbin/rsyslogd -n
  1141 ?        Ss     0:00 /usr/libexec/postfix/master -w
  1147 ?        S      0:00  \_ qmgr -l -t unix -u
  6991 ?        S      0:00  \_ pickup -l -t unix -u
  1371 ?        Ss     0:00 login -- root
  1376 tty1     Ss     0:00  \_ -bash
  1411 tty1     S+     0:00      \_ man man
  1420 tty1     S+     0:00          \_ less -s
[...]
```
To summarize, remember to use ps -ef or ps aux to get a list of all the running processes. Consider piping the output via grep to display output lines with certain words. The terminal output below shows the lines with peter in them.
```text
Terminal

           
user@TryHackMe$ ps -ef | grep peter
root       5665    978  0 07:11 ?        00:00:00 sshd: peter [priv]
peter      5693   5665  0 07:13 ?        00:00:00 sshd: peter@pts/1
peter      5694   5693  0 07:13 pts/1    00:00:00 -bash
peter      5713   5694  0 07:13 pts/1    00:00:00 vi notes.txt
```
Start the attached Linux machine if you have not done so already, as you need it to answer the questions below. You can log in to it using SSH: ssh user@10.10.100.30, where the login credentials are:
Username: user
Password: THM6877
```text
┌──(kali㉿kali)-[~]
└─$ ssh user@10.10.100.30    
The authenticity of host '10.10.100.30 (10.10.100.30)' can't be established.
ED25519 key fingerprint is SHA256:3KDSRP0Cf5CjpFMJzGe8IKdXPpKKukw59QM3EbFz7XY.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.100.30' (ED25519) to the list of known hosts.
user@10.10.100.30's password: 
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-120-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun 11 Sep 00:26:54 UTC 2022

  System load:  0.0               Processes:             121
  Usage of /:   62.2% of 6.53GB   Users logged in:       0
  Memory usage: 26%               IPv4 address for eth0: 10.10.100.30
  Swap usage:   0%

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

0 updates can be applied immediately.

The list of available updates is more than a week old.
To check for new updates run: sudo apt update

user@red-linux-enumeration:~$ hostname
red-linux-enumeration
user@red-linux-enumeration:~$ id
uid=1005(user) gid=1005(user) groups=1005(user),27(sudo)
user@red-linux-enumeration:~$ ls /etc/*-release
/etc/lsb-release  /etc/os-release
user@red-linux-enumeration:~$ cat /etc/os-release
NAME="Ubuntu"
VERSION="20.04.4 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.4 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
user@red-linux-enumeration:~$
```
```text
user@red-linux-enumeration:~$ last
user     pts/0        10.11.81.220     Sun Sep 11 00:26   still logged in
reboot   system boot  5.4.0-120-generi Sun Sep 11 00:14   still running
reboot   system boot  5.4.0-120-generi Mon Jun 20 13:10 - 13:13  (00:02)
randa    pts/0        10.20.30.1       Mon Jun 20 11:00 - 11:01  (00:00)
reboot   system boot  5.4.0-120-generi Mon Jun 20 09:58 - 11:01  (01:03)

wtmp begins Mon Jun 20 09:58:27 2022
```
```text
user@red-linux-enumeration:~$ ps axf
    PID TTY      STAT   TIME COMMAND
      2 ?        S      0:00 [kthreadd]
      3 ?        I<     0:00  \_ [rcu_gp]
      4 ?        I<     0:00  \_ [rcu_par_gp]
      6 ?        I<     0:00  \_ [kworker/0:0H-kblockd]
      8 ?        I      0:00  \_ [kworker/u30:0-events_unbound]
      9 ?        I<     0:00  \_ [mm_percpu_wq]
     10 ?        S      0:00  \_ [ksoftirqd/0]
     11 ?        I      0:00  \_ [rcu_sched]
     12 ?        S      0:00  \_ [migration/0]
     13 ?        S      0:00  \_ [idle_inject/0]
     14 ?        S      0:00  \_ [cpuhp/0]
     15 ?        S      0:00  \_ [kdevtmpfs]
     16 ?        I<     0:00  \_ [netns]
     17 ?        S      0:00  \_ [rcu_tasks_kthre]
     18 ?        S      0:00  \_ [kauditd]
     19 ?        S      0:00  \_ [khungtaskd]
     20 ?        S      0:00  \_ [oom_reaper]
     21 ?        I<     0:00  \_ [writeback]
     22 ?        S      0:00  \_ [kcompactd0]
     23 ?        SN     0:00  \_ [ksmd]
     24 ?        SN     0:00  \_ [khugepaged]
     70 ?        I<     0:00  \_ [kintegrityd]
     71 ?        I<     0:00  \_ [kblockd]
     72 ?        I<     0:00  \_ [blkcg_punt_bio]
     73 ?        S      0:00  \_ [xen-balloon]
     74 ?        I<     0:00  \_ [tpm_dev_wq]
     75 ?        I<     0:00  \_ [ata_sff]
     76 ?        I<     0:00  \_ [md]
     77 ?        I<     0:00  \_ [edac-poller]
     78 ?        I<     0:00  \_ [devfreq_wq]
     79 ?        S      0:00  \_ [watchdogd]
     84 ?        S      0:00  \_ [kswapd0]
     85 ?        S      0:00  \_ [ecryptfs-kthrea]
     87 ?        I<     0:00  \_ [kthrotld]
     88 ?        I<     0:00  \_ [acpi_thermal_pm]
     89 ?        S      0:00  \_ [xenbus]
     90 ?        S      0:00  \_ [xenwatch]
     91 ?        S      0:00  \_ [scsi_eh_0]
     92 ?        I<     0:00  \_ [scsi_tmf_0]
     93 ?        S      0:00  \_ [scsi_eh_1]
     94 ?        I<     0:00  \_ [scsi_tmf_1]
     96 ?        I<     0:00  \_ [vfio-irqfd-clea]
     97 ?        I<     0:00  \_ [ipv6_addrconf]
    106 ?        I<     0:00  \_ [kworker/0:1H-kblockd]
    107 ?        I<     0:00  \_ [kstrp]
    110 ?        I<     0:00  \_ [kworker/u31:0]
    123 ?        I<     0:00  \_ [charger_manager]
    157 ?        I<     0:00  \_ [cryptd]
    190 ?        I<     0:00  \_ [kdmflush]
    226 ?        I<     0:00  \_ [raid5wq]
    273 ?        S      0:00  \_ [jbd2/dm-0-8]
    274 ?        I<     0:00  \_ [ext4-rsv-conver]
    363 ?        I<     0:00  \_ [ipmi-msghandler]
    483 ?        I<     0:00  \_ [kaluad]
    484 ?        I<     0:00  \_ [kmpath_rdacd]
    485 ?        I<     0:00  \_ [kmpathd]
    486 ?        I<     0:00  \_ [kmpath_handlerd]
    495 ?        S<     0:00  \_ [loop0]
    497 ?        S<     0:00  \_ [loop1]
    500 ?        S<     0:00  \_ [loop2]
    502 ?        S<     0:00  \_ [loop3]
    504 ?        S<     0:00  \_ [loop4]
    506 ?        S<     0:00  \_ [loop5]
    508 ?        S<     0:00  \_ [loop6]
    510 ?        S<     0:00  \_ [loop7]
    519 ?        S      0:00  \_ [jbd2/xvda2-8]
    520 ?        I<     0:00  \_ [ext4-rsv-conver]
    995 ?        I      0:00  \_ [kworker/0:2-cgroup_destroy]
   1031 ?        I      0:00  \_ [kworker/0:1-events]
   1189 ?        I      0:00  \_ [kworker/u30:2-events_power_efficient]
   1237 ?        I      0:00  \_ [kworker/u30:1-events_power_efficient]
      1 ?        Ss     0:05 /sbin/init auto automatic-ubiquity noprompt
    344 ?        S<s    0:00 /lib/systemd/systemd-journald
    374 ?        Ss     0:00 /lib/systemd/systemd-udevd
    487 ?        SLsl   0:00 /sbin/multipathd -d -s
    537 ?        Ssl    0:00 /lib/systemd/systemd-timesyncd
    580 ?        Ss     0:00 /lib/systemd/systemd-networkd
    583 ?        Ss     0:00 /lib/systemd/systemd-resolved
    594 ?        Ssl    0:00 /usr/lib/accountsservice/accounts-daemon
    595 ?        Ssl    0:00 /usr/bin/amazon-ssm-agent
    734 ?        Sl     0:00  \_ /usr/bin/ssm-agent-worker
    600 ?        Ss     0:00 /usr/sbin/cron -f
    604 ?        S      0:00  \_ /usr/sbin/CRON -f
    649 ?        Ss     0:00      \_ /bin/sh -c /home/randa/THM-24765.sh
    652 ?        S      0:00          \_ /bin/bash /home/randa/THM-24765.s
    655 ?        S      0:00              \_ sleep 10000
    603 ?        Ss     0:00 /usr/bin/dbus-daemon --system --address=syste
    616 ?        Ssl    0:00 /usr/sbin/named -f -u bind
    618 ?        Ss     0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher
    619 ?        Ssl    0:00 /usr/lib/policykit-1/polkitd --no-debug
    621 ?        Ssl    0:00 /usr/sbin/rsyslogd -n -iNONE
    629 ?        Ssl    0:01 /usr/lib/snapd/snapd
    633 ?        Ss     0:00 /lib/systemd/systemd-logind
    638 ?        Ssl    0:00 /usr/lib/udisks2/udisksd
    644 ?        Ss     0:00 /usr/sbin/atd -f
    647 ?        Ss     0:00 /usr/sbin/snmpd -LOw -u Debian-snmp -g Debian
    648 ?        Ss     0:00 /usr/sbin/vsftpd /etc/vsftpd.conf
    664 ttyS0    Ss+    0:00 /sbin/agetty -o -p -- \u --keep-baud 115200,3
    671 ?        Ss     0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-10
   1006 ?        Ss     0:00  \_ sshd: user [priv]
   1154 ?        S      0:00      \_ sshd: user@pts/0
   1160 pts/0    Ss     0:00          \_ -bash
   1244 pts/0    R+     0:00              \_ ps axf
    678 tty1     Ss+    0:00 /sbin/agetty -o -p -- \u --noclear tty1 linux
    713 ?        Ssl    0:00 /usr/sbin/ModemManager
    724 ?        Ssl    0:00 /usr/sbin/slapd -h ldap:/// ldapi:/// -g open
    754 ?        Ss     0:00 /usr/sbin/inspircd --config=/etc/inspircd/ins
    767 ?        Ssl    0:00 /usr/bin/python3 /usr/share/unattended-upgrad
   1027 ?        Ss     0:00 /lib/systemd/systemd --user
   1028 ?        S      0:00  \_ (sd-pam)
```
```text
user@red-linux-enumeration:~$ sudo netstat -lnp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:389             0.0.0.0:*               LISTEN      724/slapd           
tcp        0      0 127.0.0.1:6667          0.0.0.0:*               LISTEN      754/inspircd        
tcp        0      0 10.10.100.30:53         0.0.0.0:*               LISTEN      616/named           
tcp        0      0 127.0.0.1:53            0.0.0.0:*               LISTEN      616/named           
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      583/systemd-resolve 
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      671/sshd: /usr/sbin 
tcp        0      0 127.0.0.1:953           0.0.0.0:*               LISTEN      616/named           
tcp6       0      0 :::389                  :::*                    LISTEN      724/slapd           
tcp6       0      0 fe80::8d:99ff:fee9:a:53 :::*                    LISTEN      616/named           
tcp6       0      0 ::1:53                  :::*                    LISTEN      616/named           
tcp6       0      0 :::21                   :::*                    LISTEN      648/vsftpd          
tcp6       0      0 :::22                   :::*                    LISTEN      671/sshd: /usr/sbin 
tcp6       0      0 ::1:953                 :::*                    LISTEN      616/named           
udp        0      0 0.0.0.0:37913           0.0.0.0:*                           754/inspircd        
udp        0      0 10.10.100.30:53         0.0.0.0:*                           616/named           
udp        0      0 127.0.0.1:53            0.0.0.0:*                           616/named           
udp        0      0 127.0.0.53:53           0.0.0.0:*                           583/systemd-resolve 
udp        0      0 10.10.100.30:68         0.0.0.0:*                           580/systemd-network 
udp        0      0 0.0.0.0:161             0.0.0.0:*                           647/snmpd           
udp6       0      0 ::1:53                  :::*                                616/named           
udp6       0      0 fe80::8d:99ff:fee9:a:53 :::*                                616/named           
udp6       0      0 ::1:161                 :::*                                647/snmpd           
raw6       0      0 :::58                   :::*                    7           580/systemd-network 
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name     Path
unix  2      [ ACC ]     STREAM     LISTENING     27743    647/snmpd            /var/agentx/master
unix  2      [ ACC ]     SEQPACKET  LISTENING     17323    1/init               /run/udev/control
unix  2      [ ACC ]     STREAM     LISTENING     34667    1027/systemd         /run/user/1005/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     34674    1027/systemd         /run/user/1005/bus
unix  2      [ ACC ]     STREAM     LISTENING     34675    1027/systemd         /run/user/1005/gnupg/S.dirmngr
unix  2      [ ACC ]     STREAM     LISTENING     34676    1027/systemd         /run/user/1005/gnupg/S.gpg-agent.browser
unix  2      [ ACC ]     STREAM     LISTENING     22841    1/init               /var/snap/lxd/common/lxd/unix.socket
unix  2      [ ACC ]     STREAM     LISTENING     34677    1027/systemd         /run/user/1005/gnupg/S.gpg-agent.extra
unix  2      [ ACC ]     STREAM     LISTENING     17305    1/init               @/org/kernel/linux/storage/multipathd
unix  2      [ ACC ]     STREAM     LISTENING     34678    1027/systemd         /run/user/1005/gnupg/S.gpg-agent.ssh
