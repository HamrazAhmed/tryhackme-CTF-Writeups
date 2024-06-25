---
Put your snort skills into practice and write snort rules to analyse live capture network traffic.
---

# Snort Challenge - The Basics — Writeup

## Overview
### Snort Challenge - The Basics — Writeup
### Snort Challenge - The Basics — Writeup
### Introduction
The room invites you a challenge to investigate a series of traffic data and stop malicious activity under two different scenarios. Let's start working with Snort to analyse live and captured traffic.
We recommend completing the Snort room first, which will teach you how to use the tool in depth.
Exercise files for each task are located on the desktop as follows;
### Writing IDS Rules (HTTP)
Let's create IDS Rules for HTTP traffic!
Navigate to the task folder.
Use the given pcap file.
Write rules to detect "all TCP port 80 traffic" packets in the given pcap file.
What is the number of detected packets?
Note: You must answer this question correctly before answering the rest of the questions in this task.
You need to investigate inbound and outbound traffic on port 80. Writing two simple rules will help you.
```text
┌──(kali㉿kali)-[~]
└─$ mkpasswd -m sha-512 Password1234
$6$337LYJ6n9X7PMx.h$wIKtRS.RoAzgfLcxSy0o7RN6.2degI2bvcfUKtLANJKuzjsx6vsExWBjaB65Dv988VkqL9TD4a69yiTV16jMq/
```
```text
┌──(kali㉿kali)-[~]
└─$ ssh ubuntu@10.10.135.44 
The authenticity of host '10.10.135.44 (10.10.135.44)' can't be established.
ED25519 key fingerprint is SHA256:9VinV6lSzIVHKOLNhG4WlbqlDOlI1KC2yfBl5TJqVsI.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.135.44' (ED25519) to the list of known hosts.
ubuntu@10.10.135.44's password: 
Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.8.0-1038-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Dec  6 23:08:28 UTC 2022

  System load:  0.05               Processes:             214
  Usage of /:   10.2% of 43.56GB   Users logged in:       0
  Memory usage: 18%                IPv4 address for eth0: 10.10.135.44
  Swap usage:   0%                 IPv4 address for eth1: 10.234.0.1

 * Ubuntu Pro delivers the most comprehensive open source security and
   compliance features.

   https://ubuntu.com/aws/pro

210 updates can be applied immediately.
104 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

The list of available updates is more than a week old.
To check for new updates run: sudo apt update

/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1

/bin/bash: warning: shell level (1000) too high, resetting to 1
^Cubuntu@ip-10-10-135-44:~$ sudo su
root@ip-10-10-135-44:/home/ubuntu# ┌──(kali㉿kali)-[~]
└─$ mkpasswd -m sha-512 Password1234
$6$337LYJ6n9X7PMx.h$wIKtRS.RoAzgfLcxSy0o7RN6.2degI2bvcfUKtLANJKuzjsx6vsExWBjaB65Dv988VkqL9TD4a69yiTV16jMq/

Replacing this hash !$6$vmzKXtCowJO/EvOg$PcukzMtijIm6kj56vz7m33c6KExbF7Horki4oPeujuoVsOsonzlUm/w6e/Enmb.NAcOKVNBkHEC22j.5FyqHu0 by mine created before.

root@ip-10-10-135-44:/home/ubuntu# nano /etc/shadow
```
```text
┌──(kali㉿kali)-[~]
└─$ ssh ubuntu@10.10.135.44 
The authenticity of host '10.10.135.44 (10.10.135.44)' can't be established.
ED25519 key fingerprint is SHA256:9VinV6lSzIVHKOLNhG4WlbqlDOlI1KC2yfBl5TJqVsI.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.135.44' (ED25519) to the list of known hosts.
ubuntu@10.10.135.44's password: 
Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.8.0-1038-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue Dec  6 23:08:28 UTC 2022

  System load:  0.05               Processes:             214
  Usage of /:   10.2% of 43.56GB   Users logged in:       0
  Memory usage: 18%                IPv4 address for eth0: 10.10.135.44
  Swap usage:   0%                 IPv4 address for eth1: 10.234.0.1

 * Ubuntu Pro delivers the most comprehensive open source security and
   compliance features.

   https://ubuntu.com/aws/pro

210 updates can be applied immediately.
104 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

The list of available updates is more than a week old.
To check for new updates run: sudo apt update

/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1

/bin/bash: warning: shell level (1000) too high, resetting to 1
^Cubuntu@ip-10-10-135-44:~$ sudo su
root@ip-10-10-135-44:/home/ubuntu# 

root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files# ls
 Config-Samples  'TASK-3 (FTP)'  'TASK-5 (TorrentMetafile)'  'TASK-7 (MS17-10)'
'TASK-2 (HTTP)'  'TASK-4 (PNG)'  'TASK-6 (Troubleshooting)'  'TASK-8 (Log4j)'
root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files# cd 'TASK-2 (HTTP)'/
root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-2 (HTTP)# ls
local.rules  mx-3.pcap
root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-2 (HTTP)# cat local.rules
```
```text
# ----------------
```
```text
# LOCAL RULES
```
```text
# ----------------
```
```text
# This file intentionally does not come with signatures.  Put your local
```
```text
# additions here.

root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-2 (HTTP)# cat local.rules
```
```text
# ----------------
```
```text
# LOCAL RULES
```
```text
# ----------------
```
```text
# This file intentionally does not come with signatures.  Put your local
```
```text
# additions here.
alert tcp any any <> any 80 (msg:"Port 80 traffic";sid:100001;rev:1;)
alert tcp any 80 <> any any (msg:"Port 80 traffic";sid:100002;rev:1;)

root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-2 (HTTP)# sudo snort -c local.rules -A console -l . -dev -r mx-3.pcap

the above command contain the following parameters

    -A output should be in console mode
    -r read the following file (pcap in our case)
    - dev show packets in development mode (very useful in this room)
    -l log the file in the following directory (default in /var/log/snort/)
    -c read the rules from the following file (local.rules)

===============================================================================
Action Stats:
     Alerts:          328 ( 71.304%)
     Logged:          328 ( 71.304%)
     Passed:            0 (  0.000%)
Limits:
      Match:            0
      Queue:            0
        Log:            0
      Event:            0
      Alert:            0
Verdicts:
      Allow:          460 (100.000%)
      Block:            0 (  0.000%)
    Replace:            0 (  0.000%)
  Whitelist:            0 (  0.000%)
  Blacklist:            0 (  0.000%)
     Ignore:            0 (  0.000%)
      Retry:            0 (  0.000%)
===============================================================================
Snort exiting
```
*328*
Investigate the log file.
What is the destination address of packet 63?
"-n" parameter helps analyze the "n" number of packets.
```text
root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-2 (HTTP)# ls
local.rules  mx-3.pcap  snort.log.1670370100

root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-2 (HTTP)# sudo snort -dev -r snort.log.1670370100 -n 63

WARNING: No preprocessors configured for policy 0.
05/13-10:17:09.123830 FE:FF:20:00:01:00 -> 00:00:01:00:00:00 type:0x800 len:0x59A
65.208.228.223:80 -> 145.254.160.237:3372 TCP TTL:47 TOS:0x0 ID:49312 IpLen:20 DgmLen:1420 DF
***A**** Seq: 0x114C66F0  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
20 20 20 20 20 20 20 20 20 20 3C 61 20 68 72 65            <a hre
66 3D 22 73 65 61 72 63 68 2E 68 74 6D 6C 22 3E  f="search.html">
53 65 61 72 63 68 3A 3C 2F 61 3E 0A 09 09 20 20  Search:</a>...  
3C 2F 64 69 76 3E 0A 09 20 20 20 20 20 20 20 20  </div>..        
3C 2F 74 64 3E 0A 09 20 20 20 20 20 20 20 20 3C  </td>..        <
74 64 3E 0A 09 20 20 20 20 20 20 20 20 20 20 3C  td>..          <
64 69 76 20 63 6C 61 73 73 3D 22 74 6F 70 66 6F  div class="topfo
72 6D 74 65 78 74 22 3E 0A 20 20 20 20 20 20 20  rmtext">.       
20 20 20 20 20 20 20 20 20 20 20 3C 69 6E 70 75             <inpu
74 20 74 79 70 65 3D 22 74 65 78 74 22 20 73 69  t type="text" si
7A 65 3D 22 31 32 22 20 6E 61 6D 65 3D 22 77 6F  ze="12" name="wo
72 64 73 22 3E 0A 09 09 20 20 3C 69 6E 70 75 74  rds">...  <input
20 74 79 70 65 3D 22 68 69 64 64 65 6E 22 20 6E   type="hidden" n
61 6D 65 3D 22 63 6F 6E 66 69 67 22 20 76 61 6C  ame="config" val
75 65 3D 22 65 74 68 65 72 65 61 6C 22 3E 0A 09  ue="ethereal">..
09 20 20 3C 2F 64 69 76 3E 0A 09 20 20 20 20 20  .  </div>..     
20 20 20 3C 2F 74 64 3E 0A 09 09 3C 74 64 20 76     </td>...<td v
61 6C 69 67 6E 3D 22 62 6F 74 74 6F 6D 22 3E 0A  align="bottom">.
09 09 20 20 3C 69 6E 70 75 74 20 74 79 70 65 3D  ..  <input type=
22 69 6D 61 67 65 22 20 63 6C 61 73 73 3D 22 67  "image" class="g
6F 62 75 74 74 6F 6E 22 20 73 72 63 3D 22 6D 6D  obutton" src="mm
2F 69 6D 61 67 65 2F 67 6F 2D 62 75 74 74 6F 6E  /image/go-button
2E 67 69 66 22 3E 0A 09 09 3C 2F 74 64 3E 0A 20  .gif">...</td>. 
20 20 20 20 20 20 20 20 20 20 20 20 20 3C 2F 74               </t
72 3E 0A 20 20 20 20 20 20 20 20 20 20 20 20 20  r>.             
20 3C 2F 66 6F 72 6D 3E 0A 3C 2F 74 61 62 6C 65   </form>.</table
3E 0A 09 20 20 3C 2F 64 69 76 3E 0A 20 20 20 20  >..  </div>.    
20 20 20 20 3C 2F 74 64 3E 0A 20 20 20 20 20 20      </td>.      
3C 2F 74 72 3E 0A 20 20 20 20 3C 2F 74 61 62 6C  </tr>.    </tabl
65 3E 0A 20 20 20 20 3C 2F 64 69 76 3E 0A 3C 64  e>.    </div>.<d
69 76 20 63 6C 61 73 73 3D 22 73 69 74 65 62 61  iv class="siteba
72 22 3E 0A 3C 70 3E 0A 20 20 3C 61 20 68 72 65  r">.<p>.  <a hre
66 3D 22 2F 22 3E 48 6F 6D 65 3C 2F 61 3E 0A 20  f="/">Home</a>. 
20 3C 73 70 61 6E 20 63 6C 61 73 73 3D 22 73 69   <span class="si
74 65 62 61 72 73 65 70 22 3E 7C 3C 2F 73 70 61  tebarsep">|</spa
6E 3E 0A 20 20 3C 61 20 68 72 65 66 3D 22 69 6E  n>.  <a href="in
74 72 6F 64 75 63 74 69 6F 6E 2E 68 74 6D 6C 22  troduction.html"
3E 49 6E 74 72 6F 64 75 63 74 69 6F 6E 3C 2F 61  >Introduction</a
3E 0A 20 20 3C 73 70 61 6E 20 63 6C 61 73 73 3D  >.  <span class=
22 73 69 74 65 62 61 72 73 65 70 22 3E 7C 3C 2F  "sitebarsep">|</
73 70 61 6E 3E 0A 20 20 44 6F 77 6E 6C 6F 61 64  span>.  Download
0A 20 20 3C 73 70 61 6E 20 63 6C 61 73 73 3D 22  .  <span class="
73 69 74 65 62 61 72 73 65 70 22 3E 7C 3C 2F 73  sitebarsep">|</s
70 61 6E 3E 0A 20 20 3C 61 20 68 72 65 66 3D 22  pan>.  <a href="
64 6F 63 73 2F 22 3E 44 6F 63 75 6D 65 6E 74 61  docs/">Documenta
74 69 6F 6E 3C 2F 61 3E 0A 20 20 3C 73 70 61 6E  tion</a>.  <span
20 63 6C 61 73 73 3D 22 73 69 74 65 62 61 72 73   class="sitebars
65 70 22 3E 7C 3C 2F 73 70 61 6E 3E 0A 20 20 3C  ep">|</span>.  <
61 20 68 72 65 66 3D 22 6C 69 73 74 73 2F 22 3E  a href="lists/">
4C 69 73 74 73 3C 2F 61 3E 0A 20 20 3C 73 70 61  Lists</a>.  <spa
6E 20 63 6C 61 73 73 3D 22 73 69 74 65 62 61 72  n class="sitebar
73 65 70 22 3E 7C 3C 2F 73 70 61 6E 3E 0A 20 20  sep">|</span>.  
3C 61 20 68 72 65 66 3D 22 66 61 71 2E 68 74 6D  <a href="faq.htm
6C 22 3E 46 41 51 3C 2F 61 3E 0A 20 20 3C 73 70  l">FAQ</a>.  <sp
61 6E 20 63 6C 61 73 73 3D 22 73 69 74 65 62 61  an class="siteba
72 73 65 70 22 3E 7C 3C 2F 73 70 61 6E 3E 0A 20  rsep">|</span>. 
20 3C 61 20 68 72 65 66 3D 22 64 65 76 65 6C 6F   <a href="develo
70 6D 65 6E 74 2E 68 74 6D 6C 22 3E 44 65 76 65  pment.html">Deve
6C 6F 70 6D 65 6E 74 3C 2F 61 3E 0A 3C 2F 70 3E  lopment</a>.</p>
0A 3C 2F 64 69 76 3E 0A 3C 64 69 76 20 63 6C 61  .</div>.<div cla
73 73 3D 22 6E 61 76 62 61 72 22 3E 0A 3C 70 3E  ss="navbar">.<p>
0A 20 20 3C 61 20 68 72 65 66 3D 22 23 72 65 6C  .  <a href="#rel
65 61 73 65 73 22 3E 4F 66 66 69 63 69 61 6C 20  eases">Official 
52 65 6C 65 61 73 65 73 3C 2F 61 3E 0A 20 20 3C  Releases</a>.  <
73 70 61 6E 20 63 6C 61 73 73 3D 22 6E 61 76 62  span class="navb
61 72 73 65 70 22 3E 7C 3C 2F 73 70 61 6E 3E 0A  arsep">|</span>.
20 20 3C 61 20 68 72 65 66 3D 22 23 6F 74 68 65    <a href="#othe
72 70 6C 61 74 22 3E 4F 74 68 65 72 20 50 6C 61  rplat">Other Pla
74 66 6F 72 6D 73 3C 2F 61 3E 0A 20 20 3C 73 70  tforms</a>.  <sp
61 6E 20 63 6C 61 73 73 3D 22 6E 61 76 62 61 72  an class="navbar
73 65 70 22 3E 7C 3C 2F 73 70 61 6E 3E 0A 20 20  sep">|</span>.  
3C 61 20 68 72 65 66 3D 22 23 6F 74 68 65 72 64  <a href="#otherd
6F 77 6E 22 3E 4F 74 68 65 72 20 44 6F 77 6E 6C  own">Other Downl
6F 61 64 73 3C 2F 61 3E 0A 20 20 3C 73 70 61 6E  oads</a>.  <span
20 63 6C 61 73 73 3D 22 6E 61 76 62 61 72 73 65   class="navbarse
70 22 3E 7C 3C 2F 73 70 61 6E 3E 0A 20 20 3C 61  p">|</span>.  <a
20 68 72 65 66 3D 22 23 6C 65 67 61 6C 22 3E 4C   href="#legal">L
65 67 61 6C 20 4E 6F 74 69 63 65 73 3C 2F 61 3E  egal Notices</a>
0A 3C 2F 70 3E 0A 3C 2F 64 69 76 3E 0A 3C 21 2D  .</p>.</div>.<!-
2D 20 42 65 67 69 6E 20 41 64 20 34 36 38 78 36  - Begin Ad 468x6
30 20 2D 2D 3E 0A 3C 64 69 76 20 63 6C 61 73 73  0 -->.<div class
3D 22 61 64 62 6C 6F 63 6B 22 3E 0A 3C 73 63 72  ="adblock">.<scr
69 70 74 20 74 79 70 65 3D 22 74 65 78 74 2F 6A  ipt type="text/j
61 76 61 73 63 72 69 70 74 22 3E 3C 21 2D 2D 0A  avascript"><!--.
67 6F 6F 67 6C 65 5F 61 64 5F 63 6C 69 65 6E 74  google_ad_client
20 3D 20 22 70 75 62 2D 32 33 30 39 31 39 31 39   = "pub-23091919
34 38 36 37                                      4867

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

===============================================================================
Run time for packet processing was 0.7245 seconds
Snort processed 63 packets.
Snort ran for 0 days 0 hours 0 minutes 0 seconds
   Pkts/sec:           63
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      13180928
  Total allocated space (uordblks):      678144
  Total free space (fordblks):           108288
  Topmost releasable block (keepcost):   102304
===============================================================================
Packet I/O Totals:
   Received:           63
   Analyzed:           63 (100.000%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            0 (  0.000%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:           63 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:           63 (100.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:           63 (100.000%)
        IP6:            0 (  0.000%)
    IP6 Ext:            0 (  0.000%)
   IP6 Opts:            0 (  0.000%)
      Frag6:            0 (  0.000%)
      ICMP6:            0 (  0.000%)
       UDP6:            0 (  0.000%)
       TCP6:            0 (  0.000%)
     Teredo:            0 (  0.000%)
    ICMP-IP:            0 (  0.000%)
    IP4/IP4:            0 (  0.000%)
    IP4/IP6:            0 (  0.000%)
    IP6/IP4:            0 (  0.000%)
    IP6/IP6:            0 (  0.000%)
        GRE:            0 (  0.000%)
    GRE Eth:            0 (  0.000%)
   GRE VLAN:            0 (  0.000%)
    GRE IP4:            0 (  0.000%)
    GRE IP6:            0 (  0.000%)
GRE IP6 Ext:            0 (  0.000%)
   GRE PPTP:            0 (  0.000%)
    GRE ARP:            0 (  0.000%)
    GRE IPX:            0 (  0.000%)
   GRE Loop:            0 (  0.000%)
       MPLS:            0 (  0.000%)
        ARP:            0 (  0.000%)
        IPX:            0 (  0.000%)
   Eth Loop:            0 (  0.000%)
   Eth Disc:            0 (  0.000%)
   IP4 Disc:            0 (  0.000%)
   IP6 Disc:            0 (  0.000%)
   TCP Disc:            0 (  0.000%)
   UDP Disc:            0 (  0.000%)
  ICMP Disc:            0 (  0.000%)
All Discard:            0 (  0.000%)
      Other:            0 (  0.000%)
Bad Chk Sum:            0 (  0.000%)
    Bad TTL:            0 (  0.000%)
     S5 G 1:            0 (  0.000%)
     S5 G 2:            0 (  0.000%)
      Total:           63
===============================================================================
Snort exiting

145.254.160.237:3372
```
*145.254.160.237*
Investigate the log file.
What is the ACK number of packet 64?
```text
root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-2 (HTTP)# sudo snort -dev -r snort.log.1670370100 -n 64

WARNING: No preprocessors configured for policy 0.
05/13-10:17:09.123830 FE:FF:20:00:01:00 -> 00:00:01:00:00:00 type:0x800 len:0x59A
65.208.228.223:80 -> 145.254.160.237:3372 TCP TTL:47 TOS:0x0 ID:49312 IpLen:20 DgmLen:1420 DF
***A**** Seq: 0x114C66F0  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
20 20 20 20 20 20 20 20 20 20 3C 61 20 68 72 65            <a hre
66 3D 22 73 65 61 72 63 68 2E 68 74 6D 6C 22 3E  f="search.html">
53 65 61 72 63 68 3A 3C 2F 61 3E 0A 09 09 20 20  Search:</a>...  
3C 2F 64 69 76 3E 0A 09 20 20 20 20 20 20 20 20  </div>..        
3C 2F 74 64 3E 0A 09 20 20 20 20 20 20 20 20 3C  </td>..        <
74 64 3E 0A 09 20 20 20 20 20 20 20 20 20 20 3C  td>..          <
64 69 76 20 63 6C 61 73 73 3D 22 74 6F 70 66 6F  div class="topfo
72 6D 74 65 78 74 22 3E 0A 20 20 20 20 20 20 20  rmtext">.       
20 20 20 20 20 20 20 20 20 20 20 3C 69 6E 70 75             <inpu
74 20 74 79 70 65 3D 22 74 65 78 74 22 20 73 69  t type="text" si
7A 65 3D 22 31 32 22 20 6E 61 6D 65 3D 22 77 6F  ze="12" name="wo
72 64 73 22 3E 0A 09 09 20 20 3C 69 6E 70 75 74  rds">...  <input
20 74 79 70 65 3D 22 68 69 64 64 65 6E 22 20 6E   type="hidden" n
61 6D 65 3D 22 63 6F 6E 66 69 67 22 20 76 61 6C  ame="config" val
75 65 3D 22 65 74 68 65 72 65 61 6C 22 3E 0A 09  ue="ethereal">..
09 20 20 3C 2F 64 69 76 3E 0A 09 20 20 20 20 20  .  </div>..     
20 20 20 3C 2F 74 64 3E 0A 09 09 3C 74 64 20 76     </td>...<td v
61 6C 69 67 6E 3D 22 62 6F 74 74 6F 6D 22 3E 0A  align="bottom">.
09 09 20 20 3C 69 6E 70 75 74 20 74 79 70 65 3D  ..  <input type=
22 69 6D 61 67 65 22 20 63 6C 61 73 73 3D 22 67  "image" class="g
6F 62 75 74 74 6F 6E 22 20 73 72 63 3D 22 6D 6D  obutton" src="mm
2F 69 6D 61 67 65 2F 67 6F 2D 62 75 74 74 6F 6E  /image/go-button
2E 67 69 66 22 3E 0A 09 09 3C 2F 74 64 3E 0A 20  .gif">...</td>. 
20 20 20 20 20 20 20 20 20 20 20 20 20 3C 2F 74               </t
72 3E 0A 20 20 20 20 20 20 20 20 20 20 20 20 20  r>.             
20 3C 2F 66 6F 72 6D 3E 0A 3C 2F 74 61 62 6C 65   </form>.</table
3E 0A 09 20 20 3C 2F 64 69 76 3E 0A 20 20 20 20  >..  </div>.    
20 20 20 20 3C 2F 74 64 3E 0A 20 20 20 20 20 20      </td>.      
3C 2F 74 72 3E 0A 20 20 20 20 3C 2F 74 61 62 6C  </tr>.    </tabl
65 3E 0A 20 20 20 20 3C 2F 64 69 76 3E 0A 3C 64  e>.    </div>.<d
69 76 20 63 6C 61 73 73 3D 22 73 69 74 65 62 61  iv class="siteba
72 22 3E 0A 3C 70 3E 0A 20 20 3C 61 20 68 72 65  r">.<p>.  <a hre
66 3D 22 2F 22 3E 48 6F 6D 65 3C 2F 61 3E 0A 20  f="/">Home</a>. 
20 3C 73 70 61 6E 20 63 6C 61 73 73 3D 22 73 69   <span class="si
74 65 62 61 72 73 65 70 22 3E 7C 3C 2F 73 70 61  tebarsep">|</spa
6E 3E 0A 20 20 3C 61 20 68 72 65 66 3D 22 69 6E  n>.  <a href="in
74 72 6F 64 75 63 74 69 6F 6E 2E 68 74 6D 6C 22  troduction.html"
3E 49 6E 74 72 6F 64 75 63 74 69 6F 6E 3C 2F 61  >Introduction</a
3E 0A 20 20 3C 73 70 61 6E 20 63 6C 61 73 73 3D  >.  <span class=
22 73 69 74 65 62 61 72 73 65 70 22 3E 7C 3C 2F  "sitebarsep">|</
73 70 61 6E 3E 0A 20 20 44 6F 77 6E 6C 6F 61 64  span>.  Download
0A 20 20 3C 73 70 61 6E 20 63 6C 61 73 73 3D 22  .  <span class="
73 69 74 65 62 61 72 73 65 70 22 3E 7C 3C 2F 73  sitebarsep">|</s
70 61 6E 3E 0A 20 20 3C 61 20 68 72 65 66 3D 22  pan>.  <a href="
64 6F 63 73 2F 22 3E 44 6F 63 75 6D 65 6E 74 61  docs/">Documenta
74 69 6F 6E 3C 2F 61 3E 0A 20 20 3C 73 70 61 6E  tion</a>.  <span
20 63 6C 61 73 73 3D 22 73 69 74 65 62 61 72 73   class="sitebars
65 70 22 3E 7C 3C 2F 73 70 61 6E 3E 0A 20 20 3C  ep">|</span>.  <
61 20 68 72 65 66 3D 22 6C 69 73 74 73 2F 22 3E  a href="lists/">
4C 69 73 74 73 3C 2F 61 3E 0A 20 20 3C 73 70 61  Lists</a>.  <spa
6E 20 63 6C 61 73 73 3D 22 73 69 74 65 62 61 72  n class="sitebar
73 65 70 22 3E 7C 3C 2F 73 70 61 6E 3E 0A 20 20  sep">|</span>.  
3C 61 20 68 72 65 66 3D 22 66 61 71 2E 68 74 6D  <a href="faq.htm
6C 22 3E 46 41 51 3C 2F 61 3E 0A 20 20 3C 73 70  l">FAQ</a>.  <sp
61 6E 20 63 6C 61 73 73 3D 22 73 69 74 65 62 61  an class="siteba
72 73 65 70 22 3E 7C 3C 2F 73 70 61 6E 3E 0A 20  rsep">|</span>. 
20 3C 61 20 68 72 65 66 3D 22 64 65 76 65 6C 6F   <a href="develo
70 6D 65 6E 74 2E 68 74 6D 6C 22 3E 44 65 76 65  pment.html">Deve
6C 6F 70 6D 65 6E 74 3C 2F 61 3E 0A 3C 2F 70 3E  lopment</a>.</p>
0A 3C 2F 64 69 76 3E 0A 3C 64 69 76 20 63 6C 61  .</div>.<div cla
73 73 3D 22 6E 61 76 62 61 72 22 3E 0A 3C 70 3E  ss="navbar">.<p>
0A 20 20 3C 61 20 68 72 65 66 3D 22 23 72 65 6C  .  <a href="#rel
65 61 73 65 73 22 3E 4F 66 66 69 63 69 61 6C 20  eases">Official 
52 65 6C 65 61 73 65 73 3C 2F 61 3E 0A 20 20 3C  Releases</a>.  <
73 70 61 6E 20 63 6C 61 73 73 3D 22 6E 61 76 62  span class="navb
61 72 73 65 70 22 3E 7C 3C 2F 73 70 61 6E 3E 0A  arsep">|</span>.
20 20 3C 61 20 68 72 65 66 3D 22 23 6F 74 68 65    <a href="#othe
72 70 6C 61 74 22 3E 4F 74 68 65 72 20 50 6C 61  rplat">Other Pla
74 66 6F 72 6D 73 3C 2F 61 3E 0A 20 20 3C 73 70  tforms</a>.  <sp
61 6E 20 63 6C 61 73 73 3D 22 6E 61 76 62 61 72  an class="navbar
73 65 70 22 3E 7C 3C 2F 73 70 61 6E 3E 0A 20 20  sep">|</span>.  
3C 61 20 68 72 65 66 3D 22 23 6F 74 68 65 72 64  <a href="#otherd
6F 77 6E 22 3E 4F 74 68 65 72 20 44 6F 77 6E 6C  own">Other Downl
6F 61 64 73 3C 2F 61 3E 0A 20 20 3C 73 70 61 6E  oads</a>.  <span
20 63 6C 61 73 73 3D 22 6E 61 76 62 61 72 73 65   class="navbarse
70 22 3E 7C 3C 2F 73 70 61 6E 3E 0A 20 20 3C 61  p">|</span>.  <a
20 68 72 65 66 3D 22 23 6C 65 67 61 6C 22 3E 4C   href="#legal">L
65 67 61 6C 20 4E 6F 74 69 63 65 73 3C 2F 61 3E  egal Notices</a>
0A 3C 2F 70 3E 0A 3C 2F 64 69 76 3E 0A 3C 21 2D  .</p>.</div>.<!-
2D 20 42 65 67 69 6E 20 41 64 20 34 36 38 78 36  - Begin Ad 468x6
30 20 2D 2D 3E 0A 3C 64 69 76 20 63 6C 61 73 73  0 -->.<div class
3D 22 61 64 62 6C 6F 63 6B 22 3E 0A 3C 73 63 72  ="adblock">.<scr
69 70 74 20 74 79 70 65 3D 22 74 65 78 74 2F 6A  ipt type="text/j
61 76 61 73 63 72 69 70 74 22 3E 3C 21 2D 2D 0A  avascript"><!--.
67 6F 6F 67 6C 65 5F 61 64 5F 63 6C 69 65 6E 74  google_ad_client
20 3D 20 22 70 75 62 2D 32 33 30 39 31 39 31 39   = "pub-23091919
34 38 36 37                                      4867

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

===============================================================================
Run time for packet processing was 0.7736 seconds
Snort processed 64 packets.
Snort ran for 0 days 0 hours 0 minutes 0 seconds
   Pkts/sec:           64
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      13180928
  Total allocated space (uordblks):      678144
  Total free space (fordblks):           108288
  Topmost releasable block (keepcost):   102304
===============================================================================
Packet I/O Totals:
   Received:           64
   Analyzed:           64 (100.000%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            0 (  0.000%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:           64 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:           64 (100.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:           64 (100.000%)
        IP6:            0 (  0.000%)
    IP6 Ext:            0 (  0.000%)
   IP6 Opts:            0 (  0.000%)
      Frag6:            0 (  0.000%)
      ICMP6:            0 (  0.000%)
       UDP6:            0 (  0.000%)
       TCP6:            0 (  0.000%)
     Teredo:            0 (  0.000%)
    ICMP-IP:            0 (  0.000%)
    IP4/IP4:            0 (  0.000%)
    IP4/IP6:            0 (  0.000%)
    IP6/IP4:            0 (  0.000%)
    IP6/IP6:            0 (  0.000%)
        GRE:            0 (  0.000%)
    GRE Eth:            0 (  0.000%)
   GRE VLAN:            0 (  0.000%)
    GRE IP4:            0 (  0.000%)
    GRE IP6:            0 (  0.000%)
GRE IP6 Ext:            0 (  0.000%)
   GRE PPTP:            0 (  0.000%)
    GRE ARP:            0 (  0.000%)
    GRE IPX:            0 (  0.000%)
   GRE Loop:            0 (  0.000%)
       MPLS:            0 (  0.000%)
        ARP:            0 (  0.000%)
        IPX:            0 (  0.000%)
   Eth Loop:            0 (  0.000%)
   Eth Disc:            0 (  0.000%)
   IP4 Disc:            0 (  0.000%)
   IP6 Disc:            0 (  0.000%)
   TCP Disc:            0 (  0.000%)
   UDP Disc:            0 (  0.000%)
  ICMP Disc:            0 (  0.000%)
All Discard:            0 (  0.000%)
      Other:            0 (  0.000%)
Bad Chk Sum:            0 (  0.000%)
    Bad TTL:            0 (  0.000%)
     S5 G 1:            0 (  0.000%)
     S5 G 2:            0 (  0.000%)
      Total:           64
===============================================================================
Snort exiting
```
*0x38AFFFF3*
Investigate the log file.
What is the SEQ number of packet 62?
```text
root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-2 (HTTP)# sudo snort -dev -r snort.log.1670370100 -n 62

WARNING: No preprocessors configured for policy 0.
05/13-10:17:09.123830 00:00:01:00:00:00 -> FE:FF:20:00:01:00 type:0x800 len:0x36
145.254.160.237:3372 -> 65.208.228.223:80 TCP TTL:128 TOS:0x0 ID:3910 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFFF3  Ack: 0x114C66F0  Win: 0x25BC  TcpLen: 20

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

===============================================================================
Run time for packet processing was 0.7603 seconds
Snort processed 62 packets.
Snort ran for 0 days 0 hours 0 minutes 0 seconds
   Pkts/sec:           62
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      13180928
  Total allocated space (uordblks):      678144
  Total free space (fordblks):           108288
  Topmost releasable block (keepcost):   102304
===============================================================================
Packet I/O Totals:
   Received:           62
   Analyzed:           62 (100.000%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            0 (  0.000%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:           62 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:           62 (100.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:           62 (100.000%)
        IP6:            0 (  0.000%)
    IP6 Ext:            0 (  0.000%)
   IP6 Opts:            0 (  0.000%)
      Frag6:            0 (  0.000%)
      ICMP6:            0 (  0.000%)
       UDP6:            0 (  0.000%)
       TCP6:            0 (  0.000%)
     Teredo:            0 (  0.000%)
    ICMP-IP:            0 (  0.000%)
    IP4/IP4:            0 (  0.000%)
    IP4/IP6:            0 (  0.000%)
    IP6/IP4:            0 (  0.000%)
    IP6/IP6:            0 (  0.000%)
        GRE:            0 (  0.000%)
    GRE Eth:            0 (  0.000%)
   GRE VLAN:            0 (  0.000%)
    GRE IP4:            0 (  0.000%)
    GRE IP6:            0 (  0.000%)
GRE IP6 Ext:            0 (  0.000%)
   GRE PPTP:            0 (  0.000%)
    GRE ARP:            0 (  0.000%)
    GRE IPX:            0 (  0.000%)
   GRE Loop:            0 (  0.000%)
       MPLS:            0 (  0.000%)
        ARP:            0 (  0.000%)
        IPX:            0 (  0.000%)
   Eth Loop:            0 (  0.000%)
   Eth Disc:            0 (  0.000%)
   IP4 Disc:            0 (  0.000%)
   IP6 Disc:            0 (  0.000%)
   TCP Disc:            0 (  0.000%)
   UDP Disc:            0 (  0.000%)
  ICMP Disc:            0 (  0.000%)
All Discard:            0 (  0.000%)
      Other:            0 (  0.000%)
Bad Chk Sum:            0 (  0.000%)
    Bad TTL:            0 (  0.000%)
     S5 G 1:            0 (  0.000%)
     S5 G 2:            0 (  0.000%)
      Total:           62
===============================================================================
Snort exiting
```
*0x38AFFFF3*
Investigate the log file.
What is the TTL of packet 65?
```text
root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-2 (HTTP)# sudo snort -dev -r snort.log.1670370100 -n 65

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:09.324118 00:00:01:00:00:00 -> FE:FF:20:00:01:00 type:0x800 len:0x36
145.254.160.237:3372 -> 65.208.228.223:80 TCP TTL:128 TOS:0x0 ID:3911 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFFF3  Ack: 0x114C6C54  Win: 0x25BC  TcpLen: 20

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

===============================================================================
Run time for packet processing was 0.7837 seconds
Snort processed 65 packets.
Snort ran for 0 days 0 hours 0 minutes 0 seconds
   Pkts/sec:           65
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      13180928
  Total allocated space (uordblks):      678144
  Total free space (fordblks):           108288
  Topmost releasable block (keepcost):   102304
===============================================================================
Packet I/O Totals:
   Received:           65
   Analyzed:           65 (100.000%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            0 (  0.000%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:           65 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:           65 (100.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:           65 (100.000%)
        IP6:            0 (  0.000%)
    IP6 Ext:            0 (  0.000%)
   IP6 Opts:            0 (  0.000%)
      Frag6:            0 (  0.000%)
      ICMP6:            0 (  0.000%)
       UDP6:            0 (  0.000%)
       TCP6:            0 (  0.000%)
     Teredo:            0 (  0.000%)
    ICMP-IP:            0 (  0.000%)
    IP4/IP4:            0 (  0.000%)
    IP4/IP6:            0 (  0.000%)
    IP6/IP4:            0 (  0.000%)
    IP6/IP6:            0 (  0.000%)
        GRE:            0 (  0.000%)
    GRE Eth:            0 (  0.000%)
   GRE VLAN:            0 (  0.000%)
    GRE IP4:            0 (  0.000%)
    GRE IP6:            0 (  0.000%)
GRE IP6 Ext:            0 (  0.000%)
   GRE PPTP:            0 (  0.000%)
    GRE ARP:            0 (  0.000%)
    GRE IPX:            0 (  0.000%)
   GRE Loop:            0 (  0.000%)
       MPLS:            0 (  0.000%)
        ARP:            0 (  0.000%)
        IPX:            0 (  0.000%)
   Eth Loop:            0 (  0.000%)
   Eth Disc:            0 (  0.000%)
   IP4 Disc:            0 (  0.000%)
   IP6 Disc:            0 (  0.000%)
   TCP Disc:            0 (  0.000%)
   UDP Disc:            0 (  0.000%)
  ICMP Disc:            0 (  0.000%)
All Discard:            0 (  0.000%)
      Other:            0 (  0.000%)
Bad Chk Sum:            0 (  0.000%)
    Bad TTL:            0 (  0.000%)
     S5 G 1:            0 (  0.000%)
     S5 G 2:            0 (  0.000%)
      Total:           65
===============================================================================
Snort exiting
```
*128*
Investigate the log file.
What is the source IP of packet 65?
*145.254.160.237*
Investigate the log file.
What is the source port of packet 65?
*3372*
### Writing IDS Rules (FTP)
Let's create IDS Rules for FTP traffic!
Navigate to the task folder.
Use the given pcap file.
Write rules to detect "all TCP port 21"  traffic in the given pcap.
What is the number of detected packets?
You need to investigate inbound and outbound traffic on port 21. Writing two simple rules will help you.
```text
root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-2 (HTTP)# cd ..
root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files# ls
 Config-Samples  'TASK-3 (FTP)'  'TASK-5 (TorrentMetafile)'  'TASK-7 (MS17-10)'
'TASK-2 (HTTP)'  'TASK-4 (PNG)'  'TASK-6 (Troubleshooting)'  'TASK-8 (Log4j)'
root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files# cd 'TASK-3 (FTP)'/
root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-3 (FTP)# ls
ftp-png-gif.pcap  local.rules
root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-3 (FTP)# nano local.rules 
root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-3 (FTP)# cat local.rules
```
```text
# ----------------
```
```text
# LOCAL RULES
```
```text
# ----------------
```
```text
# This file intentionally does not come with signatures.  Put your local
```
```text
# additions here.
alert tcp any any <> any 21 (msg:"FTP traffic";sid:100001;rev:1;)
alert tcp any 21 <> any any (msg:"FTP traffic";sid:100002;rev:1;)

root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-3 (FTP)# sudo snort -c local.rules -A console -dev -l . -r ftp-png-gif.pcap 

Action Stats:
     Alerts:          614 (145.843%)
     Logged:          614 (145.843%)
     Passed:            0 (  0.000%)
Limits:
      Match:            0
      Queue:            0
        Log:            0
      Event:            0
      Alert:            0
Verdicts:
      Allow:          421 (100.000%)
      Block:            0 (  0.000%)
    Replace:            0 (  0.000%)
  Whitelist:            0 (  0.000%)
  Blacklist:            0 (  0.000%)
     Ignore:            0 (  0.000%)
      Retry:            0 (  0.000%)
===============================================================================
Snort exiting
```
*614*
Investigate the log file.
What is the FTP service name?
```text
root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-3 (FTP)# sudo snort -r snort.log.1670372300 -dev -n 7

root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-3 (FTP)# sudo snort -r snort.log.1670372300 -dev -n 7
Exiting after 7 packets
Running in packet dump mode

        --== Initializing Snort ==--
Initializing Output Plugins!
pcap DAQ configured to read-file.
Acquiring network traffic from "snort.log.1670372300".

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

Commencing packet processing (pid=5676)
WARNING: No preprocessors configured for policy 0.
01/04-10:19:34.002181 00:50:56:C0:00:08 -> 00:0C:29:0F:71:A3 type:0x800 len:0x4A
192.168.75.1:18157 -> 192.168.75.132:21 TCP TTL:128 TOS:0x0 ID:2432 IpLen:20 DgmLen:60 DF
******S* Seq: 0xE9CEC218  Ack: 0x0  Win: 0x2000  TcpLen: 40
TCP Options (5) => MSS: 1460 NOP WS: 2 SackOK TS: 7457661 0 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
01/04-10:19:34.002181 00:50:56:C0:00:08 -> 00:0C:29:0F:71:A3 type:0x800 len:0x4A
192.168.75.1:18157 -> 192.168.75.132:21 TCP TTL:128 TOS:0x0 ID:2432 IpLen:20 DgmLen:60 DF
******S* Seq: 0xE9CEC218  Ack: 0x0  Win: 0x2000  TcpLen: 40
TCP Options (5) => MSS: 1460 NOP WS: 2 SackOK TS: 7457661 0 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
01/04-10:19:34.003768 00:0C:29:0F:71:A3 -> 00:50:56:C0:00:08 type:0x800 len:0x4E
192.168.75.132:21 -> 192.168.75.1:18157 TCP TTL:128 TOS:0x0 ID:1695 IpLen:20 DgmLen:64
***A**S* Seq: 0x93FDAA42  Ack: 0xE9CEC219  Win: 0xFAF0  TcpLen: 44
TCP Options (9) => MSS: 1460 NOP WS: 0 NOP NOP TS: 0 0 NOP NOP SackOK 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
01/04-10:19:34.003768 00:0C:29:0F:71:A3 -> 00:50:56:C0:00:08 type:0x800 len:0x4E
192.168.75.132:21 -> 192.168.75.1:18157 TCP TTL:128 TOS:0x0 ID:1695 IpLen:20 DgmLen:64
***A**S* Seq: 0x93FDAA42  Ack: 0xE9CEC219  Win: 0xFAF0  TcpLen: 44
TCP Options (9) => MSS: 1460 NOP WS: 0 NOP NOP TS: 0 0 NOP NOP SackOK 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
01/04-10:19:34.003930 00:50:56:C0:00:08 -> 00:0C:29:0F:71:A3 type:0x800 len:0x42
192.168.75.1:18157 -> 192.168.75.132:21 TCP TTL:128 TOS:0x0 ID:2433 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xE9CEC219  Ack: 0x93FDAA43  Win: 0x410C  TcpLen: 32
TCP Options (3) => NOP NOP TS: 7457661 0 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
01/04-10:19:34.003930 00:50:56:C0:00:08 -> 00:0C:29:0F:71:A3 type:0x800 len:0x42
192.168.75.1:18157 -> 192.168.75.132:21 TCP TTL:128 TOS:0x0 ID:2433 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xE9CEC219  Ack: 0x93FDAA43  Win: 0x410C  TcpLen: 32
TCP Options (3) => NOP NOP TS: 7457661 0 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
01/04-10:19:34.008856 00:0C:29:0F:71:A3 -> 00:50:56:C0:00:08 type:0x800 len:0x5D
192.168.75.132:21 -> 192.168.75.1:18157 TCP TTL:128 TOS:0x0 ID:1696 IpLen:20 DgmLen:79 DF
***AP*** Seq: 0x93FDAA43  Ack: 0xE9CEC219  Win: 0xFAF0  TcpLen: 32
TCP Options (3) => NOP NOP TS: 13955 7457661 
32 32 30 20 4D 69 63 72 6F 73 6F 66 74 20 46 54  220 Microsoft FT
50 20 53 65 72 76 69 63 65 0D 0A                 P Service..

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

===============================================================================
Run time for packet processing was 0.421 seconds
Snort processed 7 packets.
Snort ran for 0 days 0 hours 0 minutes 0 seconds
   Pkts/sec:            7
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      13180928
  Total allocated space (uordblks):      678144
  Total free space (fordblks):           108288
  Topmost releasable block (keepcost):   102304
===============================================================================
Packet I/O Totals:
   Received:            7
   Analyzed:            7 (100.000%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            0 (  0.000%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:            7 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:            7 (100.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:            7 (100.000%)
        IP6:            0 (  0.000%)
    IP6 Ext:            0 (  0.000%)
   IP6 Opts:            0 (  0.000%)
      Frag6:            0 (  0.000%)
      ICMP6:            0 (  0.000%)
       UDP6:            0 (  0.000%)
       TCP6:            0 (  0.000%)
     Teredo:            0 (  0.000%)
    ICMP-IP:            0 (  0.000%)
    IP4/IP4:            0 (  0.000%)
    IP4/IP6:            0 (  0.000%)
    IP6/IP4:            0 (  0.000%)
    IP6/IP6:            0 (  0.000%)
        GRE:            0 (  0.000%)
    GRE Eth:            0 (  0.000%)
   GRE VLAN:            0 (  0.000%)
    GRE IP4:            0 (  0.000%)
    GRE IP6:            0 (  0.000%)
GRE IP6 Ext:            0 (  0.000%)
   GRE PPTP:            0 (  0.000%)
    GRE ARP:            0 (  0.000%)
    GRE IPX:            0 (  0.000%)
   GRE Loop:            0 (  0.000%)
       MPLS:            0 (  0.000%)
        ARP:            0 (  0.000%)
        IPX:            0 (  0.000%)
   Eth Loop:            0 (  0.000%)
   Eth Disc:            0 (  0.000%)
   IP4 Disc:            0 (  0.000%)
   IP6 Disc:            0 (  0.000%)
   TCP Disc:            0 (  0.000%)
   UDP Disc:            0 (  0.000%)
  ICMP Disc:            0 (  0.000%)
All Discard:            0 (  0.000%)
      Other:            0 (  0.000%)
Bad Chk Sum:            0 (  0.000%)
    Bad TTL:            0 (  0.000%)
     S5 G 1:            0 (  0.000%)
     S5 G 2:            0 (  0.000%)
      Total:            7
===============================================================================
Snort exiting

 Microsoft FTP Service
```
*Microsoft FTP Service*
Clear the previous log and alarm files.
Deactivate/comment on the old rules.
Write a rule to detect failed FTP login attempts in the given pcap.
What is the number of detected packets?
Each failed FTP login attempt prompts a default message with the pattern; "530 User". Try to filter the given pattern in the inbound FTP traffic.
```text
root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-3 (FTP)# ls
ftp-png-gif.pcap  local.rules  snort.log.1670372300
root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-3 (FTP)# rm -r snort.log.1670372300 
root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-3 (FTP)# nano local.rules 
root@ip-10-10-135-44:/home/ubuntu/Desktop/Exercise-Files/TASK-3 (FTP)# cat local.rules
```
```text
# ----------------
```
```text
# LOCAL RULES
```
```text
# ----------------
```
```text
# This file intentionally does not come with signatures.  Put your local
```
```text
# additions here.
#alert tcp any any <> any 21 (msg:"FTP traffic";sid:100001;rev:1;)
