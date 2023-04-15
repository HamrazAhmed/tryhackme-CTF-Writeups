# CMesS — Writeup

## Overview
### CMesS — Writeup
### CMesS — Writeup
----
Can you root this Gila CMS box?
---
![](https://i.imgur.com/qnV5dJQ.png)

## Privilege Escalation
```bash
# symbolic names for networks, see networks(5) for more information
link-local 169.254.0.0
eth0      Link encap:Ethernet  HWaddr 02:09:c7:bb:bf:13  
          inet addr:10.10.105.35  Bcast:10.10.255.255  Mask:255.255.0.0
          inet6 addr: fe80::9:c7ff:febb:bf13/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:9001  Metric:1
          RX packets:64628 errors:0 dropped:0 overruns:0 frame:0
          TX packets:63262 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:4858546 (4.8 MB)  TX bytes:9400313 (9.4 MB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:1619 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1619 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1 
          RX bytes:156180 (156.1 KB)  TX bytes:156180 (156.1 KB)

╔══════════╣ Active Ports
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#open-ports
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -               
tcp6       0      0 :::80                   :::*                    LISTEN      -               
tcp6       0      0 :::22                   :::*                    LISTEN      -               

╔══════════╣ Can I sniff with tcpdump?
No

                               ╔═══════════════════╗
═══════════════════════════════╣ Users Information ╠═══════════════════════════════
                               ╚═══════════════════╝
╔══════════╣ My user
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#users
uid=33(www-data) gid=33(www-data) groups=33(www-data)

╔══════════╣ Do I have PGP keys?
/usr/bin/gpg
netpgpkeys Not Found
netpgp Not Found

╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid

╔══════════╣ Checking sudo tokens
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#reusing-sudo-tokens
ptrace protection is enabled (1)
gdb wasn't found in PATH, this might still be vulnerable but linpeas won't be able to check it

╔══════════╣ Checking Pkexec policy
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation/interesting-groups-linux-pe#pe-method-2

╔══════════╣ Superusers
root:x:0:0:root:/root:/bin/bash

╔══════════╣ Users with console
andre:x:1000:1000:andre,,,:/home/andre:/bin/bash
root:x:0:0:root:/root:/bin/bash

╔══════════╣ All users & groups
uid=0(root) gid=0(root) groups=0(root)
uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=100(systemd-timesync) gid=102(systemd-timesync) groups=102(systemd-timesync)
uid=1000(mandre) gid=1000(mandre) groups=1000(mandre)
uid=101(systemd-network) gid=103(systemd-network) groups=103(systemd-network)
uid=102(systemd-resolve) gid=104(systemd-resolve) groups=104(systemd-resolve)
uid=103(systemd-bus-proxy) gid=105(systemd-bus-proxy) groups=105(systemd-bus-proxy)
uid=104(syslog) gid=108(syslog) groups=108(syslog),4(adm)
uid=105(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=106(messagebus) gid=110(messagebus) groups=110(messagebus)
uid=107(uuidd) gid=111(uuidd) groups=111(uuidd)
uid=108(mysql) gid=117(mysql) groups=117(mysql)
uid=109(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=5(games) gid=60(games) groups=60(games)
uid=6(man) gid=12(man) groups=12(man)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=9(news) gid=9(news) groups=9(news)

╔══════════╣ Login now
 10:03:14 up 40 min,  0 users,  load average: 3.04, 2.51, 1.81
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

╔══════════╣ Last logons
mandre    tty1         Sun Feb  9 11:02:51 2020 - down                      (00:01)     0.0.0.0
reboot   system boot  Sun Feb  9 11:02:38 2020 - Sun Feb  9 11:04:02 2020  (00:01)     0.0.0.0
mandre    tty1         Sun Feb  9 10:58:15 2020 - down                      (00:04)     0.0.0.0
reboot   system boot  Sun Feb  9 10:57:50 2020 - Sun Feb  9 11:02:24 2020  (00:04)     0.0.0.0
mandre    tty1         Thu Feb  6 18:18:33 2020 - crash                    (2+16:39)    0.0.0.0
reboot   system boot  Thu Feb  6 18:18:21 2020 - Sun Feb  9 11:02:24 2020 (2+16:44)    0.0.0.0
mandre    tty1         Thu Feb  6 18:01:42 2020 - crash                     (00:16)     0.0.0.0
reboot   system boot  Thu Feb  6 18:00:21 2020 - Sun Feb  9 11:02:24 2020 (2+17:02)    0.0.0.0

wtmp begins Thu Feb  6 18:00:21 2020

╔══════════╣ Last time logon each user
Username         Port     From             Latest
mandre            pts/0    10.0.0.20        Thu Feb 13 15:02:43 -0800 2020

╔══════════╣ Do not forget to test 'su' as any other user with shell: without password and with their names as password (I can't do it...)

╔══════════╣ Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!

                             ╔══════════════════════╗
═════════════════════════════╣ Software Information ╠═════════════════════════════
                             ╚══════════════════════╝
╔══════════╣ Useful software
/usr/bin/base64
/bin/nc
/bin/netcat
/usr/bin/perl
/usr/bin/php
/bin/ping
/usr/bin/python3
/usr/bin/sudo
/usr/bin/wget

╔══════════╣ Installed Compilers
/usr/share/gcc-5

╔══════════╣ MySQL version
mysql  Ver 14.14 Distrib 5.7.29, for Linux (x86_64) using  EditLine wrapper

═╣ MySQL connection using default root/root ........... No
═╣ MySQL connection using root/toor ................... No
═╣ MySQL connection using root/NOPASS ................. No

╔══════════╣ Searching mysql credentials and exec
From '/etc/mysql/mysql.conf.d/mysqld.cnf' Mysql user: user		= mysql
Found readable /etc/mysql/my.cnf
!includedir /etc/mysql/conf.d/
!includedir /etc/mysql/mysql.conf.d/

╔══════════╣ Analyzing MariaDB Files (limit 70)

-rw------- 1 root root 317 Feb  6  2020 /etc/mysql/debian.cnf

╔══════════╣ Analyzing Apache-Nginx Files (limit 70)
Apache version: Server version: Apache/2.4.18 (Ubuntu)
Server built:   2019-10-08T13:31:25
httpd Not Found

Nginx version: nginx Not Found

/etc/apache2/mods-enabled/php7.0.conf-<FilesMatch ".+\.ph(p[3457]?|t|tml)$">
/etc/apache2/mods-enabled/php7.0.conf:    SetHandler application/x-httpd-php
--
/etc/apache2/mods-enabled/php7.0.conf-<FilesMatch ".+\.phps$">
/etc/apache2/mods-enabled/php7.0.conf:    SetHandler application/x-httpd-php-source
--
/etc/apache2/mods-available/php7.0.conf-<FilesMatch ".+\.ph(p[3457]?|t|tml)$">
/etc/apache2/mods-available/php7.0.conf:    SetHandler application/x-httpd-php
--
/etc/apache2/mods-available/php7.0.conf-<FilesMatch ".+\.phps$">
/etc/apache2/mods-available/php7.0.conf:    SetHandler application/x-httpd-php-source
══╣ PHP exec extensions
drwxr-xr-x 2 root root 4096 Feb  6  2020 /etc/apache2/sites-enabled
drwxr-xr-x 2 root root 4096 Feb  6  2020 /etc/apache2/sites-enabled
lrwxrwxrwx 1 root root 35 Feb  6  2020 /etc/apache2/sites-enabled/000-default.conf -> ../sites-available/000-default.conf
<VirtualHost *:80>
	ServerAdmin webmaster@localhost
	DocumentRoot /var/www/html
<Directory "/var/www/html">
	AllowOverride All
</Directory>
	
	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
<VirtualHost *:80>
	ServerAdmin webmaster@localhost
	ServerName dev.cmess.thm
	DocumentRoot /var/www/dev
	
</VirtualHost>

-rw-r--r-- 1 root root 1516 Feb  6  2020 /etc/apache2/sites-available/000-default.conf
<VirtualHost *:80>
	ServerAdmin webmaster@localhost
	DocumentRoot /var/www/html
<Directory "/var/www/html">
	AllowOverride All
</Directory>
	
	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
<VirtualHost *:80>
	ServerAdmin webmaster@localhost
	ServerName dev.cmess.thm
	DocumentRoot /var/www/dev
	
</VirtualHost>
lrwxrwxrwx 1 root root 35 Feb  6  2020 /etc/apache2/sites-enabled/000-default.conf -> ../sites-available/000-default.conf
<VirtualHost *:80>
	ServerAdmin webmaster@localhost
	DocumentRoot /var/www/html
<Directory "/var/www/html">
	AllowOverride All
</Directory>
	
	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
<VirtualHost *:80>
	ServerAdmin webmaster@localhost
	ServerName dev.cmess.thm
	DocumentRoot /var/www/dev
	
</VirtualHost>

-rw-r--r-- 1 root root 70999 Jan 14  2020 /etc/php/7.0/apache2/php.ini
allow_url_fopen = On
allow_url_include = Off
odbc.allow_persistent = On
ibase.allow_persistent = 1
mysqli.allow_persistent = On
pgsql.allow_persistent = On
-rw-r--r-- 1 root root 70656 Jan 14  2020 /etc/php/7.0/cli/php.ini
allow_url_fopen = On
allow_url_include = Off
odbc.allow_persistent = On
ibase.allow_persistent = 1
mysqli.allow_persistent = On
pgsql.allow_persistent = On
-rw-r--r-- 1 root root 70999 Jan 14  2020 /etc/php/7.0/fpm/php.ini
allow_url_fopen = On
allow_url_include = Off
odbc.allow_persistent = On
ibase.allow_persistent = 1
mysqli.allow_persistent = On
pgsql.allow_persistent = On

╔══════════╣ Analyzing Rsync Files (limit 70)
-rw-r--r-- 1 root root 1044 Sep 30  2013 /usr/share/doc/rsync/examples/rsyncd.conf
[ftp]
	comment = public archive
	path = /var/www/pub
	use chroot = yes
	lock file = /var/lock/rsyncd
	read only = yes
	list = yes
	uid = nobody
	gid = nogroup
	strict modes = yes
	ignore errors = no
	ignore nonreadable = yes
	transfer logging = no
	timeout = 600
	refuse options = checksum dry-run
	dont compress = *.gz *.tgz *.zip *.z *.rpm *.deb *.iso *.bz2 *.tbz

╔══════════╣ Analyzing Ldap Files (limit 70)
The password hash is from the {SSHA} to 'structural'
drwxr-xr-x 2 root root 4096 Feb  6  2020 /etc/ldap

╔══════════╣ Searching ssl/ssh files
Port 22
PermitRootLogin prohibit-password
PubkeyAuthentication yes
PermitEmptyPasswords no
ChallengeResponseAuthentication no
UsePAM yes
══╣ Some home ssh config file was found
/usr/share/doc/openssh-client/examples/sshd_config
AuthorizedKeysFile	.ssh/authorized_keys
Subsystem	sftp	/usr/lib/openssh/sftp-server

══╣ /etc/hosts.allow file found, trying to read the rules:
/etc/hosts.allow

Searching inside /etc/ssh/ssh_config for interesting info
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials no

╔══════════╣ Analyzing PAM Auth Files (limit 70)
drwxr-xr-x 2 root root 4096 Feb  6  2020 /etc/pam.d
-rw-r--r-- 1 root root 2133 Mar  4  2019 /etc/pam.d/sshd

╔══════════╣ Analyzing Keyring Files (limit 70)
drwxr-xr-x 2 root root 4096 Feb  6  2020 /usr/share/keyrings
drwxr-xr-x 2 root root 4096 Feb  6  2020 /var/lib/apt/keyrings

╔══════════╣ Searching uncommon passwd files (splunk)
passwd file: /etc/pam.d/passwd
passwd file: /etc/passwd
passwd file: /usr/share/bash-completion/completions/passwd
passwd file: /usr/share/lintian/overrides/passwd

╔══════════╣ Analyzing PGP-GPG Files (limit 70)
/usr/bin/gpg
gpg Not Found
netpgpkeys Not Found
netpgp Not Found

-rw-r--r-- 1 root root 12255 Feb 26  2019 /etc/apt/trusted.gpg
-rw-r--r-- 1 root root 12335 May 18  2012 /usr/share/keyrings/ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 0 May 18  2012 /usr/share/keyrings/ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root 2253 Nov  5  2017 /usr/share/keyrings/ubuntu-esm-keyring.gpg
-rw-r--r-- 1 root root 1139 Nov  5  2017 /usr/share/keyrings/ubuntu-fips-keyring.gpg
-rw-r--r-- 1 root root 1227 May 18  2012 /usr/share/keyrings/ubuntu-master-keyring.gpg
-rw-r--r-- 1 root root 2256 Feb 26  2016 /usr/share/popularity-contest/debian-popcon.gpg
-rw-r--r-- 1 root root 12335 Feb 26  2019 /var/lib/apt/keyrings/ubuntu-archive-keyring.gpg

╔══════════╣ Searching docker files (limit 70)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation/docker-breakout/docker-breakout-privilege-escalation
-rwxrwxrwx 1 root root 639 Jul 10  2019 /var/www/html/Dockerfile

╔══════════╣ Analyzing Postfix Files (limit 70)
-rw-r--r-- 1 root root 694 May 18  2016 /usr/share/bash-completion/completions/postfix

╔══════════╣ Analyzing FTP Files (limit 70)

-rw-r--r-- 1 root root 69 Jan 14  2020 /etc/php/7.0/mods-available/ftp.ini
-rw-r--r-- 1 root root 69 Jan 14  2020 /usr/share/php7.0-common/common/ftp.ini

╔══════════╣ Analyzing Interesting logs Files (limit 70)

-rw-r--r-- 1 www-data www-data 948 Mar 14 09:41 /var/www/html/log/error.log

╔══════════╣ Analyzing Windows Files (limit 70)

lrwxrwxrwx 1 root root 20 Feb  6  2020 /etc/alternatives/my.cnf -> /etc/mysql/mysql.cnf
lrwxrwxrwx 1 root root 24 Feb  6  2020 /etc/mysql/my.cnf -> /etc/alternatives/my.cnf
-rw-r--r-- 1 root root 81 Feb  6  2020 /var/lib/dpkg/alternatives/my.cnf

╔══════════╣ Analyzing Other Interesting Files (limit 70)
-rw-r--r-- 1 root root 3771 Aug 31  2015 /etc/skel/.bashrc

-rw-r--r-- 1 root root 655 May 16  2017 /etc/skel/.profile

                               ╔═══════════════════╗
═══════════════════════════════╣ Interesting Files ╠═══════════════════════════════
                               ╚═══════════════════╝
╔══════════╣ SUID - Check easy privesc, exploits and write perms
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid
strings Not Found
-rwsr-xr-x 1 root root 11K May  8  2018 /usr/bin/vmware-user-suid-wrapper
-rwsr-xr-x 1 root root 40K May 16  2017 /usr/bin/chsh
-rwsr-xr-x 1 root root 74K May 16  2017 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 39K May 16  2017 /usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root root 53K May 16  2017 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
-rwsr-xr-x 1 root root 49K May 16  2017 /usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root root 134K Jul  4  2017 /usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerable
-rwsr-xr-x 1 root root 10K Mar 27  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 419K Mar  4  2019 /usr/lib/openssh/ssh-keysign
-rwsr-xr-- 1 root messagebus 42K Jan 12  2017 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 139K Jan 28  2017 /bin/ntfs-3g  --->  Debian9/8/7/Ubuntu/Gentoo/others/Ubuntu_Server_16.10_and_others(02-2017)
-rwsr-xr-x 1 root root 31K Jul 12  2016 /bin/fusermount
-rwsr-xr-x 1 root root 40K May 16  2018 /bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
-rwsr-xr-x 1 root root 44K May  7  2014 /bin/ping6
-rwsr-xr-x 1 root root 40K May 16  2017 /bin/su
-rwsr-xr-x 1 root root 44K May  7  2014 /bin/ping
-rwsr-xr-x 1 root root 27K May 16  2018 /bin/umount  --->  BSD/Linux(08-1996)

╔══════════╣ SGID
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid
-rwxr-sr-x 1 root shadow 23K May 16  2017 /usr/bin/expiry
-rwxr-sr-x 1 root shadow 61K May 16  2017 /usr/bin/chage
-rwxr-sr-x 1 root ssh 351K Mar  4  2019 /usr/bin/ssh-agent
-rwxr-sr-x 1 root tty 27K May 16  2018 /usr/bin/wall
-rwxr-sr-x 1 root crontab 36K Apr  5  2016 /usr/bin/crontab
-rwxr-sr-x 1 root tty 15K Mar  1  2016 /usr/bin/bsd-write
-rwxr-sr-x 1 root mlocate 39K Nov 17  2014 /usr/bin/mlocate
-rwxr-sr-x 1 root shadow 35K Apr  9  2018 /sbin/unix_chkpwd
-rwxr-sr-x 1 root shadow 35K Apr  9  2018 /sbin/pam_extrausers_chkpwd

╔══════════╣ Checking misconfigurations of ld.so
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#ld-so
/etc/ld.so.conf
include /etc/ld.so.conf.d/*.conf

/etc/ld.so.conf.d
  /etc/ld.so.conf.d/libc.conf
/usr/local/lib
  /etc/ld.so.conf.d/x86_64-linux-gnu.conf
/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu
  /etc/ld.so.conf.d/x86_64-linux-gnu_EGL.conf
/usr/lib/x86_64-linux-gnu/mesa-egl

╔══════════╣ Capabilities
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#capabilities
Current env capabilities:
Current: =
Current proc capabilities:
CapInh:	0000000000000000
CapPrm:	0000000000000000
CapEff:	0000000000000000
CapBnd:	0000003fffffffff
CapAmb:	0000000000000000

Parent Shell capabilities:
0x0000000000000000=

Files with capabilities (limited to 50):
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/systemd-detect-virt = cap_dac_override,cap_sys_ptrace+ep
/usr/bin/mtr = cap_net_raw+ep

╔══════════╣ AppArmor binary profiles
-rw-r--r-- 1 root root 3310 Apr 12  2016 sbin.dhclient
-rw-r--r-- 1 root root 1793 Jan 21  2020 usr.sbin.mysqld
-rw-r--r-- 1 root root 1527 Jan  5  2016 usr.sbin.rsyslogd
-rw-r--r-- 1 root root 1469 Sep  8  2017 usr.sbin.tcpdump

╔══════════╣ Files with ACLs (limited to 50)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#acls
files with acls in searched folders Not Found

╔══════════╣ .sh files in path
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#script-binaries-in-path
/usr/bin/gettext.sh

╔══════════╣ Executable files potentially added by user (limit 70)
+18:54:07.1196134090 /opt/.password.bak
+18:28:50.0044226230 /var/www/html/assets/.htaccess

╔══════════╣ Unexpected in root
/initrd.img
/vmlinuz

╔══════════╣ Files (scripts) in /etc/profile.d/
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#profiles-files
total 16
drwxr-xr-x  2 root root 4096 Feb  6  2020 .
drwxr-xr-x 89 root root 4096 Feb 13  2020 ..
-rw-r--r--  1 root root  663 May 18  2016 bash_completion.sh
-rw-r--r--  1 root root 1003 Dec 29  2015 cedilla-portuguese.sh

╔══════════╣ Permissions in init, init.d, systemd, and rc.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#init-init-d-systemd-and-rc-d

═╣ Hashes inside passwd file? ........... No
═╣ Writable passwd file? ................ No
═╣ Credentials in fstab/mtab? ........... No
═╣ Can I read shadow files? ............. No
═╣ Can I read shadow plists? ............ No
═╣ Can I write shadow plists? ........... No
═╣ Can I read opasswd file? ............. No
═╣ Can I write in network-scripts? ...... No
═╣ Can I read root folder? .............. No

╔══════════╣ Searching root files in home dirs (limit 30)
/home/
/root/
/var/www
/var/www/dev
/var/www/dev/index.html
/var/www/html
/var/www/html/composer.json
/var/www/html/index.php
/var/www/html/assets
/var/www/html/assets/.htaccess
/var/www/html/assets/gila-logo.png
/var/www/html/tmp
/var/www/html/tmp/.htaccess
/var/www/html/.htaccess
/var/www/html/sites
/var/www/html/sites/README.md
/var/www/html/app.yaml
/var/www/html/LICENSE
/var/www/html/log
/var/www/html/Dockerfile
/var/www/html/lib
/var/www/html/lib/prism
/var/www/html/lib/prism/prism.css
/var/www/html/lib/prism/prism.js
/var/www/html/lib/vue
/var/www/html/lib/vue/vue-editor.css
/var/www/html/lib/vue/vue.min.js
/var/www/html/lib/vue/vue-draggable.min.js
/var/www/html/lib/vue/vue-editor.js
/var/www/html/lib/CodeMirror

╔══════════╣ Searching folders owned by me containing others files on it (limit 100)
/run/php

╔══════════╣ Readable files belonging to root and readable by me but not world readable

╔══════════╣ Modified interesting files in the last 5mins (limit 100)
/tmp/andre_backup.tar.gz
/var/log/syslog
/var/log/auth.log

logrotate 3.8.7

╔══════════╣ Files inside /home/www-data (limit 20)

╔══════════╣ Files inside others home (limit 20)
/var/www/dev/index.html
/var/www/html/composer.json
/var/www/html/index.php
/var/www/html/assets/.htaccess
/var/www/html/assets/payload_ivan.php
/var/www/html/assets/gila-logo.png
/var/www/html/tmp/.htaccess
/var/www/html/.htaccess
/var/www/html/sites/README.md
/var/www/html/app.yaml
/var/www/html/LICENSE
/var/www/html/log/error.log
/var/www/html/log/load.php
/var/www/html/log/sessions.log
/var/www/html/log/packages2update.json
/var/www/html/log/login.failed.log
/var/www/html/Dockerfile
/var/www/html/lib/prism/prism.css
/var/www/html/lib/prism/prism.js
/var/www/html/lib/vue/vue-editor.css
grep: write error: Broken pipe

╔══════════╣ Searching installed mail applications

╔══════════╣ Mails (limit 50)

╔══════════╣ Backup files (limited 100)
-rw-r--r-- 1 root root 161 Mar 14 10:08 /tmp/andre_backup.tar.gz
-rw-r--r-- 1 root root 7867 May  6  2015 /usr/share/doc/telnet/README.telnet.old.gz
-rw-r--r-- 1 root root 298768 Dec 29  2015 /usr/share/doc/manpages/Changes.old.gz
-rw-r--r-- 1 root root 10464 Feb  6  2020 /usr/share/info/dir.old
-rw-r--r-- 1 root root 755 Apr  7  2016 /usr/share/help-langpack/en_AU/deja-dup/backup-first.page
-rw-r--r-- 1 root root 974 Apr  7  2016 /usr/share/help-langpack/en_AU/deja-dup/backup-auto.page
-rw-r--r-- 1 root root 2018 Jun 21  2016 /usr/share/help-langpack/en_AU/ubuntu-help/backup-frequency.page
-rw-r--r-- 1 root root 1291 Jun 21  2016 /usr/share/help-langpack/en_AU/ubuntu-help/backup-why.page
-rw-r--r-- 1 root root 2392 Jun 21  2016 /usr/share/help-langpack/en_AU/ubuntu-help/backup-how.page
-rw-r--r-- 1 root root 2500 Jun 21  2016 /usr/share/help-langpack/en_AU/ubuntu-help/backup-what.page
-rw-r--r-- 1 root root 2295 Jun 21  2016 /usr/share/help-langpack/en_AU/ubuntu-help/backup-where.page
-rw-r--r-- 1 root root 1720 Jun 21  2016 /usr/share/help-langpack/en_AU/ubuntu-help/backup-check.page
-rw-r--r-- 1 root root 1422 Jun 21  2016 /usr/share/help-langpack/en_AU/ubuntu-help/backup-restore.page
-rw-r--r-- 1 root root 3073 Jun 21  2016 /usr/share/help-langpack/en_AU/ubuntu-help/backup-thinkabout.page
-rw-r--r-- 1 root root 2543 Jun 24  2016 /usr/share/help-langpack/en_GB/evolution/backup-restore.page
-rw-r--r-- 1 root root 755 Apr  7  2016 /usr/share/help-langpack/en_GB/deja-dup/backup-first.page
-rw-r--r-- 1 root root 974 Apr  7  2016 /usr/share/help-langpack/en_GB/deja-dup/backup-auto.page
-rw-r--r-- 1 root root 2020 Jun 21  2016 /usr/share/help-langpack/en_GB/ubuntu-help/backup-frequency.page
-rw-r--r-- 1 root root 1291 Jun 21  2016 /usr/share/help-langpack/en_GB/ubuntu-help/backup-why.page
-rw-r--r-- 1 root root 2371 Jun 21  2016 /usr/share/help-langpack/en_GB/ubuntu-help/backup-how.page
-rw-r--r-- 1 root root 2503 Jun 21  2016 /usr/share/help-langpack/en_GB/ubuntu-help/backup-what.page
-rw-r--r-- 1 root root 2289 Jun 21  2016 /usr/share/help-langpack/en_GB/ubuntu-help/backup-where.page
-rw-r--r-- 1 root root 1720 Jun 21  2016 /usr/share/help-langpack/en_GB/ubuntu-help/backup-check.page
-rw-r--r-- 1 root root 1420 Jun 21  2016 /usr/share/help-langpack/en_GB/ubuntu-help/backup-restore.page
-rw-r--r-- 1 root root 3067 Jun 21  2016 /usr/share/help-langpack/en_GB/ubuntu-help/backup-thinkabout.page
-rw-r--r-- 1 root root 2034 Jun 21  2016 /usr/share/help-langpack/en_CA/ubuntu-help/backup-frequency.page
-rw-r--r-- 1 root root 1298 Jun 21  2016 /usr/share/help-langpack/en_CA/ubuntu-help/backup-why.page
-rw-r--r-- 1 root root 2418 Jun 21  2016 /usr/share/help-langpack/en_CA/ubuntu-help/backup-how.page
-rw-r--r-- 1 root root 2530 Jun 21  2016 /usr/share/help-langpack/en_CA/ubuntu-help/backup-what.page
-rw-r--r-- 1 root root 2308 Jun 21  2016 /usr/share/help-langpack/en_CA/ubuntu-help/backup-where.page
-rw-r--r-- 1 root root 1732 Jun 21  2016 /usr/share/help-langpack/en_CA/ubuntu-help/backup-check.page
-rw-r--r-- 1 root root 1427 Jun 21  2016 /usr/share/help-langpack/en_CA/ubuntu-help/backup-restore.page
-rw-r--r-- 1 root root 3094 Jun 21  2016 /usr/share/help-langpack/en_CA/ubuntu-help/backup-thinkabout.page
-rw-r--r-- 1 root root 35792 May  8  2018 /usr/lib/open-vm-tools/plugins/vmsvc/libvmbackup.so
-rw-r--r-- 1 root root 190591 Jan 16  2019 /usr/src/linux-headers-4.4.0-142-generic/.config.old
-rw-r--r-- 1 root root 0 Jan 16  2019 /usr/src/linux-headers-4.4.0-142-generic/include/config/wm831x/backup.h
-rw-r--r-- 1 root root 0 Jan 16  2019 /usr/src/linux-headers-4.4.0-142-generic/include/config/net/team/mode/activebackup.h
-rw-r--r-- 1 root root 3020 Feb  6  2020 /etc/apt/sources.bak
-rw-r--r-- 1 root root 610 Feb  6  2020 /etc/xml/catalog.old
-rw-r--r-- 1 root root 673 Feb  6  2020 /etc/xml/xml-core.xml.old
-rwxrwxrwx 1 root root 36 Feb  6  2020 /opt/.password.bak
-rwxrwxrwx 1 root root 866 Jul 10  2019 /var/www/html/src/core/views/admin/db_backup.php
-rwxrwxrwx 1 root root 3773 Jul 10  2019 /var/www/html/src/core/classes/db_backup.php
-rw-r--r-- 1 root root 128 Feb  6  2020 /var/lib/sgml-base/supercatalog.old
-rw-r--r-- 1 root root 9038 Jan 16  2019 /lib/modules/4.4.0-142-generic/kernel/drivers/power/wm831x_backup.ko
-rw-r--r-- 1 root root 9070 Jan 16  2019 /lib/modules/4.4.0-142-generic/kernel/drivers/net/team/team_mode_activebackup.ko

╔══════════╣ Searching tables inside readable .db/.sql/.sqlite files (limit 100)
Found /var/lib/mlocate/mlocate.db: regular file, no read permission

╔══════════╣ Web files?(output limit)
/var/www/:
total 16K
drwxr-xr-x  4 root root 4.0K Feb  6  2020 .
drwxr-xr-x 12 root root 4.0K Feb  6  2020 ..
drwxr-xr-x  2 root root 4.0K Feb  6  2020 dev
drwxrwxrwx  9 root root 4.0K Feb 13  2020 html

/var/www/dev:
total 12K
drwxr-xr-x 2 root root 4.0K Feb  6  2020 .

╔══════════╣ All hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)
-rw-r--r-- 1 root root 220 Aug 31  2015 /etc/skel/.bash_logout
-rw-r--r-- 1 root root 1391 Feb  6  2020 /etc/apparmor.d/cache/.features
-rw------- 1 root root 0 Feb 26  2019 /etc/.pwd.lock
-rwxrwxrwx 1 root root 36 Feb  6  2020 /opt/.password.bak
-rw-r--r-- 1 root root 0 Mar 14 09:22 /run/network/.ifstate.lock
-rwxrwxrwx 1 root root 1 Feb  6  2020 /var/www/html/assets/.htaccess
-rwxrwxrwx 1 root root 37 Jul 10  2019 /var/www/html/tmp/.htaccess
-rwxrwxrwx 1 root root 1065 Jul 10  2019 /var/www/html/.htaccess
-rwxrwxrwx 1 root root 37 Jul 10  2019 /var/www/html/lib/.htaccess
-rwxrwxrwx 1 root root 37 Jul 10  2019 /var/www/html/src/.htaccess
-rwxrwxrwx 1 root root 1 Jul 10  2019 /var/www/html/src/core/widgets/.htaccess
-rwxrwxrwx 1 root root 37 Jul 10  2019 /var/www/html/themes/.htaccess

╔══════════╣ Readable files inside /tmp, /var/tmp, /private/tmp, /private/var/at/tmp, /private/var/tmp, and backup folders (limit 70)
-rw-r--r-- 1 root root 161 Mar 14 10:08 /tmp/andre_backup.tar.gz
-rwxrwxrwx 1 www-data www-data 828098 Feb 10 12:38 /tmp/linpeas.sh
-rw-r--r-- 1 root root 16930 Feb  6  2020 /var/backups/apt.extended_states.0

╔══════════╣ Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-files
/dev/mqueue
/dev/shm
/opt/.password.bak
/run/lock
/run/lock/apache2
/run/php
/tmp
/tmp/.ICE-unix
/tmp/.Test-unix
/tmp/.X11-unix
/tmp/.XIM-unix
/tmp/.font-unix
#)You_can_write_even_more_files_inside_last_directory

/var/cache/apache2/mod_cache_disk
/var/lib/php/sessions
/var/tmp
/var/www/html
/var/www/html/.htaccess
/var/www/html/Dockerfile
/var/www/html/LICENSE
/var/www/html/app.yaml
/var/www/html/assets
/var/www/html/assets/.htaccess
/var/www/html/assets/payload_ivan.php
/var/www/html/composer.json
/var/www/html/config.default.php
/var/www/html/config.php
/var/www/html/index.php
/var/www/html/lib
/var/www/html/lib/.htaccess
/var/www/html/lib/CodeMirror
/var/www/html/lib/CodeMirror/codemirror.css
/var/www/html/lib/CodeMirror/codemirror.js
/var/www/html/lib/CodeMirror/css.js
/var/www/html/lib/CodeMirror/htmlmixed.js
/var/www/html/lib/CodeMirror/javascript.js
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/lib/bootstrap
/var/www/html/lib/bootstrap/bootstrap.min.css
/var/www/html/lib/bootstrap/bootstrap.min.js
/var/www/html/lib/font-awesome
/var/www/html/lib/font-awesome/css
/var/www/html/lib/font-awesome/css/font-awesome.min.css
/var/www/html/lib/font-awesome/fonts
/var/www/html/lib/font-awesome/fonts/fontawesome-webfont.woff
/var/www/html/lib/font-awesome/fonts/fontawesome-webfont.woff2
/var/www/html/lib/gila.min.css
/var/www/html/lib/gila.min.js
/var/www/html/lib/jquery
/var/www/html/lib/jquery/jquery-3.3.1.min.js
/var/www/html/lib/jquery/jquery-sortable.js
/var/www/html/lib/prism
/var/www/html/lib/prism/prism.css
/var/www/html/lib/prism/prism.js
/var/www/html/lib/select2
/var/www/html/lib/select2/select2.min.css
/var/www/html/lib/select2/select2.min.js
/var/www/html/lib/slick
/var/www/html/lib/slick/fonts
/var/www/html/lib/slick/fonts/slick.eot
/var/www/html/lib/slick/fonts/slick.ttf
/var/www/html/lib/slick/fonts/slick.woff
/var/www/html/lib/slick/slick-theme.css
/var/www/html/lib/slick/slick.css
/var/www/html/lib/slick/slick.min.js
/var/www/html/lib/tinymce
/var/www/html/lib/tinymce/jquery.tinymce.min.js
/var/www/html/lib/tinymce/langs
/var/www/html/lib/tinymce/langs/readme.md
/var/www/html/lib/tinymce/license.txt
/var/www/html/lib/tinymce/plugins
/var/www/html/lib/tinymce/plugins/advlist
/var/www/html/lib/tinymce/plugins/advlist/plugin.min.js
/var/www/html/lib/tinymce/plugins/anchor
/var/www/html/lib/tinymce/plugins/anchor/plugin.min.js
/var/www/html/lib/tinymce/plugins/autolink
/var/www/html/lib/tinymce/plugins/autolink/plugin.min.js
/var/www/html/lib/tinymce/plugins/autoresize
/var/www/html/lib/tinymce/plugins/autoresize/plugin.min.js
/var/www/html/lib/tinymce/plugins/autosave
/var/www/html/lib/tinymce/plugins/autosave/plugin.min.js
/var/www/html/lib/tinymce/plugins/bbcode
/var/www/html/lib/tinymce/plugins/bbcode/plugin.min.js
/var/www/html/lib/tinymce/plugins/charmap
/var/www/html/lib/tinymce/plugins/charmap/plugin.min.js
/var/www/html/lib/tinymce/plugins/code
/var/www/html/lib/tinymce/plugins/code/plugin.min.js
/var/www/html/lib/tinymce/plugins/codesample
/var/www/html/lib/tinymce/plugins/codesample/css
/var/www/html/lib/tinymce/plugins/codesample/css/prism.css
/var/www/html/lib/tinymce/plugins/codesample/plugin.min.js
/var/www/html/lib/tinymce/plugins/colorpicker
/var/www/html/lib/tinymce/plugins/colorpicker/plugin.min.js
/var/www/html/lib/tinymce/plugins/contextmenu
/var/www/html/lib/tinymce/plugins/contextmenu/plugin.min.js
/var/www/html/lib/tinymce/plugins/directionality
/var/www/html/lib/tinymce/plugins/directionality/plugin.min.js
/var/www/html/lib/tinymce/plugins/emoticons
/var/www/html/lib/tinymce/plugins/emoticons/img
/var/www/html/lib/tinymce/plugins/emoticons/plugin.min.js
/var/www/html/lib/tinymce/plugins/fullpage
/var/www/html/lib/tinymce/plugins/fullpage/plugin.min.js
/var/www/html/lib/tinymce/plugins/fullscreen
/var/www/html/lib/tinymce/plugins/fullscreen/plugin.min.js
/var/www/html/lib/tinymce/plugins/help
/var/www/html/lib/tinymce/plugins/help/img
/var/www/html/lib/tinymce/plugins/help/plugin.min.js
/var/www/html/lib/tinymce/plugins/hr
/var/www/html/lib/tinymce/plugins/hr/plugin.min.js
/var/www/html/lib/tinymce/plugins/image
/var/www/html/lib/tinymce/plugins/image/plugin.min.js
/var/www/html/lib/tinymce/plugins/imagetools
/var/www/html/lib/tinymce/plugins/imagetools/plugin.min.js
/var/www/html/lib/tinymce/plugins/importcss
/var/www/html/lib/tinymce/plugins/importcss/plugin.min.js
/var/www/html/lib/tinymce/plugins/insertdatetime
/var/www/html/lib/tinymce/plugins/insertdatetime/plugin.min.js
/var/www/html/lib/tinymce/plugins/legacyoutput
/var/www/html/lib/tinymce/plugins/legacyoutput/plugin.min.js
/var/www/html/lib/tinymce/plugins/link
/var/www/html/lib/tinymce/plugins/link/plugin.min.js
/var/www/html/lib/tinymce/plugins/lists
/var/www/html/lib/tinymce/plugins/lists/plugin.min.js
/var/www/html/lib/tinymce/plugins/media
/var/www/html/lib/tinymce/plugins/media/plugin.min.js
/var/www/html/lib/tinymce/plugins/nonbreaking
/var/www/html/lib/tinymce/plugins/nonbreaking/plugin.min.js
/var/www/html/lib/tinymce/plugins/noneditable
/var/www/html/lib/tinymce/plugins/noneditable/plugin.min.js
/var/www/html/lib/tinymce/plugins/pagebreak
/var/www/html/lib/tinymce/plugins/pagebreak/plugin.min.js
/var/www/html/lib/tinymce/plugins/paste
/var/www/html/lib/tinymce/plugins/paste/plugin.min.js
/var/www/html/lib/tinymce/plugins/preview
/var/www/html/lib/tinymce/plugins/preview/plugin.min.js
/var/www/html/lib/tinymce/plugins/print
/var/www/html/lib/tinymce/plugins/print/plugin.min.js
/var/www/html/lib/tinymce/plugins/save
/var/www/html/lib/tinymce/plugins/save/plugin.min.js
/var/www/html/lib/tinymce/plugins/searchreplace
/var/www/html/lib/tinymce/plugins/searchreplace/plugin.min.js
/var/www/html/lib/tinymce/plugins/spellchecker
/var/www/html/lib/tinymce/plugins/spellchecker/plugin.min.js
/var/www/html/lib/tinymce/plugins/tabfocus
/var/www/html/lib/tinymce/plugins/tabfocus/plugin.min.js
