---
Learn about the common forensic artifacts found in the file system of Linux Operating System
---

# Linux Forensics — Writeup

## Overview
### Linux Forensics — Writeup
### Linux Forensics — Writeup
![](https://assets.tryhackme.com/additional/linuxforensics/room-banner.png)
### Introduction
In the previous few rooms, we learned about performing forensics on Windows machines. While Windows is still the most common Desktop Operating System, especially in enterprise environments, Linux also constitutes a significant portion of the pie. Especially, Linux is very common in servers that host different services for enterprises.
In an Enterprise environment, the two most common entry points for an external attacker are either through public-facing servers or through endpoints used by individuals. Since Linux can be found in any of these two endpoints, it is useful to know how to find forensic information on a Linux machine, which is the focus of this room.
After completing this room, we will have learned:
-   An introduction to Linux and its different flavors.
-   Finding OS, account, and system information on a Linux machine
-   Finding information about running processes, executed processes, and processes that are scheduled to run
-   Finding system log files and identifying information from them
-   Common third-party applications used in Linux and their logs
### Linux Forensics
The Linux Operating System can be found in a lot of places. While it might not be as easy to use as Windows or macOS, it has its own set of advantages that make its use widespread. It is found in the Web servers you interact with, in your smartphone, and maybe, even in the entertainment unit of your car. One of the reasons for this versatility is that Linux is an open-source Operating System with many different flavors. It is also very lightweight and can run on very low resources. It can be considered modular in nature and can be customized as per requirements, meaning that only those components can be installed which are required. All of these reasons make Linux an important part of our lives.
For learning more about Linux, it is highly recommended that you go through the [Linux Fundamentals 1](https://tryhackme.com/room/linuxfundamentalspart1), [Linux Fundamentals 2](https://tryhackme.com/room/linuxfundamentalspart2), and [Linux Fundamentals 3](https://tryhackme.com/room/linuxfundamentalspart3) rooms on TryHackMe.
Linux comes in many different flavors, also called distributions. There are minor differences between these distributions. Sometimes the differences are mostly cosmetic, while sometimes the differences are a little more pronounced. Some of the common Linux distributions include:
-   Ubuntu
-   Redhat
-   ArchLinux
-   Open SUSE
-   Linux Mint
-   CentOS
-   Debian
For the purpose of this room, we will be working on the Ubuntu distribution. So let's move on to the next task to learn to perform forensics on Linux.
### OS and account information
As we did in the Windows Forensics rooms, we will start by identifying the system and finding basic information about the system. In the case of Windows, we identified that the Windows Registry contains information about the Windows machine. For a Linux system, everything is stored in a file. Therefore, to identify forensic artifacts, we will need to know the locations of these files and how to read them. Below, we will start by identifying System information on a Linux host.
### Access the attached machine
Alternatively, you can access the machine using the following credentials:
**Username**: Ubuntu
**Password**: 123456
### OS release information
To find the OS release information, we can use the `cat` utility to read the file located at `/etc/os-release`.To know more about the `cat` utility, you can read its man page.
`man cat`
The below terminal shows the OS release information.
OS release
```shell-session
user@machine$ cat /etc/os-release 
NAME="Ubuntu"
VERSION="20.04.1 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04.1 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
```
### User accounts
The `/etc/passwd` file contains information about the user accounts that exist on a Linux system. We can use the `cat` utility to read this file. The output contains 7 colon-separated fields, describing username, password information, user id (uid), group id (gid), description, home directory information, and the default shell that executes when the user logs in. It can be noticed that just like Windows, the user-created user accounts have uids 1000 or above. You can use the following command to make it more readable:
`cat /etc/passwd| column -t -s :`
User accounts
```shell-session
user@machine$cat /etc/passwd| column -t -s :
root                  x  0      0      root                                /root                    /bin/bash
daemon                x  1      1      daemon                              /usr/sbin                /usr/sbin/nologin
bin                   x  2      2      bin                                 /bin                     /usr/sbin/nologin
sys                   x  3      3      sys                                 /dev                     /usr/sbin/nologin
sync                  x  4      65534  sync                                /bin                     /bin/sync
games                 x  5      60     games                               /usr/games               /usr/sbin/nologin
.
.
.
.
.
ubuntu                x  1000   1000   Ubuntu                              /home/ubuntu             /bin/bash
pulse                 x  123    130    PulseAudio daemon,,,                /var/run/pulse           /usr/sbin/nologin
tryhackme             x  1001   1001   tryhackme,,,                        /home/tryhackme          /bin/bash
```
In the above command, we can see the information for the user ubuntu. The username is ubuntu, its password information field shows `x`, which signifies that the password information is stored in the `/etc/shadow` file. The uid of the user is 1000. The gid is also 1000. The description, which often contains the full name or contact information, mentions the name Ubuntu. The home directory is set to `/home/ubuntu`, and the default shell is set to `/bin/bash`. We can see similar information about other users from the file as well.
### Group Information
The `/etc/group` file contains information about the different user groups present on the host. It can be read using the cat utility.
Group information
```shell-session
user@machine$ cat /etc/group
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:syslog,ubuntu
tty:x:5:syslog
```
We can see that the user `ubuntu` belongs to the `adm` group, which has a password stored in the `/etc/shadow` file, signified by the `x` character. The gid is 4, and the group contains 2 users, Syslog, and ubuntu.
### Sudoers List
A Linux host allows only those users to elevate privileges to `sudo`, which are present in the Sudoers list. This list is stored in the file `/etc/sudoers` and can be read using the `cat` utility. You will need to elevate privileges to access this file.
Sudoers list
```shell-session
user@machine$ sudo cat /etc/sudoers
#
```
```shell-session
# This file MUST be edited with the 'visudo' command as root.
#
```
```shell-session
# Please consider adding local content in /etc/sudoers.d/ instead of
```
```shell-session
# directly modifying this file.
#
```
```shell-session
# See the man page for details on how to write a sudoers file.
#
Defaults	env_reset
Defaults	mail_badpass
Defaults	secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
```
```shell-session
# Host alias specification
```
```shell-session
# User alias specification
```
```shell-session
# Cmnd alias specification
```
```shell-session
# User privilege specification
root	ALL=(ALL:ALL) ALL
```
```shell-session
# Members of the admin group may gain root privileges
%admin ALL=(ALL) ALL
```
```shell-session
# Allow members of group sudo to execute any command
%sudo	ALL=(ALL:ALL) ALL
```
```shell-session
# See sudoers(5) for more information on "#include" directives:

#includedir /etc/sudoers.d
```
### Login information
In the /var/log directory, we can find log files of all kinds including `wtmp` and `btmp`. The `btmp` file saves information about failed logins, while the `wtmp` keeps historical data of logins. These files are not regular text files that can be read using `cat`, `less` or `vim`; instead, they are binary files, which have to be read using the `last` utility. You can learn more about the `last` utility by reading its man page.
`man last`
The following terminal shows the contents of `wtmp` being read using the `last` utility.
Login information
```shell-session
user@machine$ sudo last -f /var/log/wtmp
reboot   system boot  5.4.0-1029-aws   Tue Mar 29 17:28   still running
reboot   system boot  5.4.0-1029-aws   Tue Mar 29 04:46 - 15:52  (11:05)
reboot   system boot  5.4.0-1029-aws   Mon Mar 28 01:35 - 01:51 (1+00:16)

wtmp begins Mon Mar 28 01:35:10 2022
```
### Authentication logs
Every user that authenticates on a Linux host is logged in the auth log. The auth log is a file placed in the location `/var/log/auth.log`. It can be read using the `cat` utility, however, given the size of the file, we can use `tail`, `head`, `more` or `less` utilities to make it easier to read.
Auth logs
```shell-session
user@machine$ cat /var/log/auth.log |tail
Mar 29 17:28:48 tryhackme gnome-keyring-daemon[989]: The PKCS#11 component was already initialized
Mar 29 17:28:48 tryhackme gnome-keyring-daemon[989]: The SSH agent was already initialized
Mar 29 17:28:49 tryhackme polkitd(authority=local): Registered Authentication Agent for unix-session:2 (system bus name :1.73 [/usr/lib/x86_64-linux-gnu/polkit-mate/polkit-mate-authentication-agent-1], object path /org/mate/PolicyKit1/AuthenticationAgent, locale en_US.UTF-8)
Mar 29 17:28:58 tryhackme pkexec[1618]: ubuntu: Error executing command as another user: Not authorized [USER=root] [TTY=unknown] [CWD=/home/ubuntu] [COMMAND=/usr/lib/update-notifier/package-system-locked]
Mar 29 17:29:09 tryhackme dbus-daemon[548]: [system] Failed to activate service 'org.bluez': timed out (service_start_timeout=25000ms)
Mar 29 17:30:01 tryhackme CRON[1679]: pam_unix(cron:session): session opened for user root by (uid=0)
Mar 29 17:30:01 tryhackme CRON[1679]: pam_unix(cron:session): session closed for user root
Mar 29 17:49:52 tryhackme sudo:   ubuntu : TTY=pts/0 ; PWD=/home/ubuntu ; USER=root ; COMMAND=/usr/bin/cat /etc/sudoers
Mar 29 17:49:52 tryhackme sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
Mar 29 17:49:52 tryhackme sudo: pam_unix(sudo:session): session closed for user root
```
In the above log file, we can see that the user ubuntu elevated privileges on `Mar 29 17:49:52` using `sudo` to run the command `cat /etc/sudoers`. We can see the subsequent session opened and closed events for the root user, which were a result of the above-mentioned privilege escalation.
Answer the questions below
In the attached VM, there is a user account named tryhackme. What is the uid of this account?
See the /etc/passwd file
```text
ubuntu@Linux4n6:~$ tail /etc/passwd | column -t -s :
cups-pk-helper     x  121   127   user for cups-pk-helper service,,,  /home/cups-pk-helper     /usr/sbin/nologin
geoclue            x  122   128   /var/lib/geoclue                    /usr/sbin/nologin
pulse              x  123   130   PulseAudio daemon,,,                /var/run/pulse           /usr/sbin/nologin
speech-dispatcher  x  124   29    Speech Dispatcher,,,                /run/speech-dispatcher   /bin/false
saned              x  125   132   /var/lib/saned                      /usr/sbin/nologin
nm-openvpn         x  126   133   NetworkManager OpenVPN,,,           /var/lib/openvpn/chroot  /usr/sbin/nologin
colord             x  127   134   colord colour management daemon,,,  /var/lib/colord          /usr/sbin/nologin
hplip              x  128   7     HPLIP system user,,,                /run/hplip               /bin/false
gdm                x  129   135   Gnome Display Manager               /var/lib/gdm3            /bin/false
tryhackme          x  1001  1001  tryhackme,,,                        /home/tryhackme          /bin/bash
```
*1001*
Which two users are the members of the group `audio`?
See group information
```text
ubuntu@Linux4n6:~$ cat /etc/group | grep audio
audio:x:29:ubuntu,pulse
```
*ubuntu,pulse*
A session was started on this machine on Sat Apr 16 20:10. How long did this session last?
Get this info from wtmp
```text
ubuntu@Linux4n6:~$ sudo last -f /var/log/wtmp
reboot   system boot  5.4.0-1029-aws   Fri Dec 16 21:51   still running
reboot   system boot  5.4.0-1029-aws   Sun Apr 17 21:00   still running
reboot   system boot  5.4.0-1029-aws   Sun Apr 17 20:50 - 21:00  (00:10)
reboot   system boot  5.4.0-1029-aws   Sun Apr 17 09:40 - 09:43  (00:03)
reboot   system boot  5.4.0-1029-aws   Sun Apr 17 05:01 - 09:23  (04:22)
reboot   system boot  5.4.0-1029-aws   Sat Apr 16 22:51 - 23:10  (00:18)
reboot   system boot  5.4.0-1029-aws   Sat Apr 16 20:10 - 21:43  (01:32)

wtmp begins Sat Apr 16 20:10:29 2022
```
*01:32*
### System Configuration
Once we have identified the OS and account information, we can start looking into the system configuration of the host.
### Hostname
The hostname is stored in the `/etc/hostname` file on a Linux Host. It can be accessed using the `cat` utility.
Hostname
```shell-session
user@machine$ cat /etc/hostname 
tryhackme
```
### Timezone
Timezone information is a significant piece of information that gives an indicator of the general location of the device or the time window it might be used in. Timezone information can be found at the location`/etc/timezone` and it can be read using the `cat` utility.
Timezone
```shell-session
user@machine$ cat /etc/timezone
Etc/UTC
```
### Network Configuration
To find information about the network interfaces, we can `cat` the `/etc/network/interfaces` file. The output on your machine might be different from the one shown here, depending on your configuration.
Network interfaces
```shell-session
user@machine$ cat /etc/network/interfaces
```
```shell-session
# This file describes the network interfaces available on your system
```
```shell-session
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*
```
```shell-session
# The loopback network interface
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet dhcp
```
Similarly, to find information about the MAC and IP addresses of the different interfaces, we can use the `ip` utility. To learn more about the `ip` utility, we can see its `man` page.
`man ip`
The below terminal shows the usage of the `ip` utility. Note that this will only be helpful on a live system.
IP information
```shell-session
user@machine$ ip address show 
1: lo:  mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0:  mtu 9001 qdisc mq state UP group default qlen 1000
    link/ether 02:20:61:f1:3c:e9 brd ff:ff:ff:ff:ff:ff
    inet 10.10.95.252/16 brd 10.10.255.255 scope global dynamic eth0
       valid_lft 2522sec preferred_lft 2522sec
    inet6 fe80::20:61ff:fef1:3ce9/64 scope link 
       valid_lft forever preferred_lft forever
```
### Active network connections
On a live system, knowing the active network connections provides additional context to the investigation. We can use the `netstat` utility to find active network connections on a Linux host. We can learn more about the `netstat` utility by reading its `man` page.
`man netstat`
The below terminal shows the usage of the `netstat` utility.
Active network connections
```shell-session
user@machine$ netstat -natp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:5901          0.0.0.0:*               LISTEN      829/Xtigervnc       
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:60602         127.0.0.1:5901          ESTABLISHED -                   
tcp        0      0 10.10.95.252:57432      18.66.171.77:443        ESTABLISHED -                   
tcp        0      0 10.10.95.252:80         10.100.1.33:51934       ESTABLISHED -                   
tcp        0      0 127.0.0.1:5901          127.0.0.1:60602         ESTABLISHED 829/Xtigervnc       
tcp6       0      0 ::1:5901                :::*                    LISTEN      829/Xtigervnc       
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 ::1:631                 :::*                    LISTEN      -
```
### Running processes
If performing forensics on a live system, it is helpful to check the running processes. The `ps` utility shows details about the running processes. To find out about the `ps` utility, we can use the `man` page.
`man ps`
The below terminal shows the usage of the `ps` utility.
Running processes
```shell-session
user@machine$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         729  0.0  0.0   7352  2212 ttyS0    Ss+  17:28   0:00 /sbin/agetty -o -p -- \u --keep-baud 115200,38400,9600 ttyS0 vt220
root         738  0.0  0.0   5828  1844 tty1     Ss+  17:28   0:00 /sbin/agetty -o -p -- \u --noclear tty1 linux
root         755  0.0  1.5 272084 63736 tty7     Ssl+ 17:28   0:00 /usr/lib/xorg/Xorg -core :0 -seat seat0 -auth /var/run/lightdm/root/:0 -nolisten tcp vt7 -novtswitch
ubuntu      1672  0.0  0.1   5264  4588 pts/0    Ss   17:29   0:00 bash
ubuntu      1985  0.0  0.0   5892  2872 pts/0    R+   17:40   0:00 ps au
```
### DNS information
The file `/etc/hosts` contains the configuration for the DNS name assignment. We can use the `cat` utility to read the hosts file. To learn more about the hosts file, we can use the `man`page.
`man hosts`
The below terminal shows a sample output of the hosts file.
hosts file
```shell-session
user@machine$ cat /etc/hosts
127.0.0.1 localhost
```
```shell-session
# The following lines are desirable for IPv6 capable hosts
::1 ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
ff02::3 ip6-allhosts
```
The information about DNS servers that a Linux host talks to for DNS resolution is stored in the resolv.conf file. Its location is `/etc/resolv.conf`. We can use the `cat` utility to read this file.
Resolv.conf
```shell-session
user@machine$ cat /etc/resolv.conf
```
```shell-session
# This file is managed by man:systemd-resolved(8). Do not edit.
#
```
```shell-session
# This is a dynamic resolv.conf file for connecting local clients to the
```
```shell-session
# internal DNS stub resolver of systemd-resolved. This file lists all
```
```shell-session
# configured search domains.
#
```
```shell-session
# Run "resolvectl status" to see details about the uplink DNS servers
```
```shell-session
# currently in use.
#
```
```shell-session
# Third party programs must not access this file directly, but only through the
```
```shell-session
# symlink at /etc/resolv.conf. To manage man:resolv.conf(5) in a different way,
```
```shell-session
# replace this symlink by a static file or a different symlink.
#
```
```shell-session
# See man:systemd-resolved.service(8) for details about the supported modes of
```
```shell-session
# operation for /etc/resolv.conf.

nameserver 127.0.0.53
options edns0 trust-ad
search eu-west-1.compute.internal
```
Answer the questions below
What is the hostname of the attached VM?
```text
ubuntu@Linux4n6:~$ cat /etc/hostname
Linux4n6
```
*Linux4n6*
What is the timezone of the attached VM?
```text
ubuntu@Linux4n6:~$ cat /etc/timezone
Asia/Karachi
```
*Asia/Karachi*
What program is listening on the address 127.0.0.1:5901?
Use netstat to see open connections, find the mentioned address and the associated program name
```text
ubuntu@Linux4n6:~$ netstat -natp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:5901          0.0.0.0:*               LISTEN      919/Xtigervnc       
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      -                   
tcp        0      0 10.10.12.178:80         10.100.1.202:37888      ESTABLISHED -                   
tcp        0      0 127.0.0.1:5901          127.0.0.1:51586         ESTABLISHED 919/Xtigervnc       
tcp        0      0 127.0.0.1:51586         127.0.0.1:5901          ESTABLISHED -                   
tcp6       0      0 ::1:5901                :::*                    LISTEN      919/Xtigervnc       
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 ::1:631                 :::*                    LISTEN      -
```
*Xtigervnc*
What is the full path of this program?
Use ps aux command to view running processes. You can grep the required process name. Please note that process names are case-sensitive.
```text
ubuntu@Linux4n6:~$ ps aux | grep -i "Xtigervnc"
ubuntu       919  0.3  3.0 350720 123564 ?       S    21:51   0:22 /usr/bin/Xtigervnc :1 -desktop Linux4n6:1 (ubuntu) -auth /home/ubuntu/.Xauthority -geometry 1900x1200 -depth 24 -rfbwait 30000 -rfbauth /home/ubuntu/.vnc/passwd -rfbport 5901 -pn -localhost -SecurityTypes VncAuth
ubuntu      2732  0.0  0.0   3436   656 pts/0    S+   23:25   0:00 grep --color=auto -i Xtigervnc
```
*/usr/bin/Xtigervnc*
