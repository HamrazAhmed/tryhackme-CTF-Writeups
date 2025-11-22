# Year of the Owl — Writeup

## Overview
### Year of the Owl — Writeup
### Year of the Owl — Writeup
----
The foolish owl sits on his throne...
----
![](https://assets.tryhackme.com/img/yoto.png)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/37401a7f48999c57c03e7d947541b099.png)
Start Machine
When the labyrinth is before you and you lose your way, sometimes thinking outside the walls is the way forward.
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ nmap 10.10.220.228 -p- -vv -Pn
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Starting Nmap 7.93 ( https://nmap.org )
Initiating Parallel DNS resolution of 1 host.
Completed Parallel DNS resolution of 1 host.
Initiating Connect Scan
Scanning 10.10.220.228 [65535 ports]
Discovered open port 3306/tcp on 10.10.220.228
Discovered open port 445/tcp on 10.10.220.228
Discovered open port 139/tcp on 10.10.220.228
Discovered open port 80/tcp on 10.10.220.228
Discovered open port 443/tcp on 10.10.220.228
Discovered open port 3389/tcp on 10.10.220.228
Connect Scan Timing: About 2.88% done; ETC: 21:24 (0:17:24 remaining)
Connect Scan Timing: About 12.85% done; ETC: 21:14 (0:06:54 remaining)
Connect Scan Timing: About 21.80% done; ETC: 21:13 (0:05:26 remaining)
Connect Scan Timing: About 28.76% done; ETC: 21:13 (0:05:00 remaining)
Connect Scan Timing: About 35.27% done; ETC: 21:13 (0:04:37 remaining)
Connect Scan Timing: About 41.86% done; ETC: 21:13 (0:04:11 remaining)
Connect Scan Timing: About 50.85% done; ETC: 21:13 (0:03:24 remaining)
Discovered open port 47001/tcp on 10.10.220.228
Connect Scan Timing: About 59.95% done; ETC: 21:13 (0:02:41 remaining)
Discovered open port 5985/tcp on 10.10.220.228
Connect Scan Timing: About 68.25% done; ETC: 21:12 (0:02:06 remaining)
Connect Scan Timing: About 75.85% done; ETC: 21:12 (0:01:36 remaining)
Connect Scan Timing: About 84.34% done; ETC: 21:14 (0:01:13 remaining)
Connect Scan Timing: About 91.32% done; ETC: 21:14 (0:00:40 remaining)
Completed Connect Scan (65535 total ports)
Nmap scan report for 10.10.220.228
Host is up, received user-set (0.20s latency).
Not shown: 65527 filtered tcp ports (no-response)
PORT      STATE SERVICE       REASON
80/tcp    open  http          syn-ack
139/tcp   open  netbios-ssn   syn-ack
443/tcp   open  https         syn-ack
445/tcp   open  microsoft-ds  syn-ack
3306/tcp  open  mysql         syn-ack
3389/tcp  open  ms-wbt-server syn-ack
5985/tcp  open  wsman         syn-ack
47001/tcp open  winrm         syn-ack

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 456.65 seconds

https://hacking-etico.com//descubriendo-comunidad-snmp-con-onesixtyone/

┌──(witty㉿kali)-[~/Downloads]
└─$ onesixtyone 10.10.220.228 -c /usr/share/seclists/Discovery/SNMP/snmp-onesixtyone.txt
Scanning 1 hosts, 3218 communities
10.10.220.228 [openview] Hardware: Intel64 Family 6 Model 63 Stepping 2 AT/AT COMPATIBLE - Software: Windows Version 6.3 (Build 17763 Multiprocessor Free)

┌──(witty㉿kali)-[~/Downloads]
└─$ snmp-check 10.10.220.228 -c openview
snmp-check v1.9 - SNMP enumerator
Copyright (c) 2005-2015 by Matteo Cantoni (www.nothink.org)

[+] Try to connect to 10.10.220.228:161 using SNMPv1 and community 'openview'

[*] System information:

  Host IP address               : 10.10.220.228
  Hostname                      : year-of-the-owl
  Description                   : Hardware: Intel64 Family 6 Model 63 Stepping 2 AT/AT COMPATIBLE - Software: Windows Version 6.3 (Build 17763 Multiprocessor Free)
  Contact                       : -
  Location                      : -
  Uptime snmp                   : 00:07:44.76
  Uptime system                 : 00:06:41.07
  System date                   : 2023-6-30 02:12:21.3
  Domain                        : WORKGROUP

[*] User accounts:

  Guest               
  Jareth              
  Administrator       
  DefaultAccount      
  WDAGUtilityAccount  

[*] Network information:

  IP forwarding enabled         : no
  Default TTL                   : 128
  TCP segments received         : 102244
  TCP segments sent             : 444
  TCP segments retrans          : 52
  Input datagrams               : 173230
  Delivered datagrams           : 173352
  Output datagrams              : 583

[*] Network interfaces:

  Interface                     : [ up ] Software Loopback Interface 1
  Id                            : 1
  Mac Address                   : :::::
  Type                          : softwareLoopback
  Speed                         : 1073 Mbps
  MTU                           : 1500
  In octets                     : 0
  Out octets                    : 0

  Interface                     : [ down ] Microsoft 6to4 Adapter
  Id                            : 2
  Mac Address                   : :::::
  Type                          : unknown
  Speed                         : 0 Mbps
  MTU                           : 0
  In octets                     : 0
  Out octets                    : 0

  Interface                     : [ down ] Microsoft IP-HTTPS Platform Adapter
  Id                            : 3
  Mac Address                   : :::::
  Type                          : unknown
  Speed                         : 0 Mbps
  MTU                           : 0
  In octets                     : 0
  Out octets                    : 0

  Interface                     : [ down ] Microsoft Kernel Debug Network Adapter
  Id                            : 4
  Mac Address                   : :::::
  Type                          : ethernet-csmacd
  Speed                         : 0 Mbps
  MTU                           : 0
  In octets                     : 0
  Out octets                    : 0

  Interface                     : [ down ] Intel(R) 82574L Gigabit Network Connection
  Id                            : 5
  Mac Address                   : 00:0c:29:02:45:89
  Type                          : ethernet-csmacd
  Speed                         : 0 Mbps
  MTU                           : 0
  In octets                     : 0
  Out octets                    : 0

  Interface                     : [ down ] Microsoft Teredo Tunneling Adapter
  Id                            : 6
  Mac Address                   : :::::
  Type                          : unknown
  Speed                         : 0 Mbps
  MTU                           : 0
  In octets                     : 0
  Out octets                    : 0

  Interface                     : [ up ] AWS PV Network Device #0
  Id                            : 7
  Mac Address                   : 02:35:ad:14:52:51
  Type                          : ethernet-csmacd
  Speed                         : 1000 Mbps
  MTU                           : 9001
  In octets                     : 12870444
  Out octets                    : 55973

  Interface                     : [ up ] AWS PV Network Device #0-WFP Native MAC Layer LightWeight Filter-0000
  Id                            : 8
  Mac Address                   : 02:35:ad:14:52:51
  Type                          : ethernet-csmacd
  Speed                         : 1000 Mbps
  MTU                           : 9001
  In octets                     : 12870444
  Out octets                    : 55973

  Interface                     : [ up ] AWS PV Network Device #0-QoS Packet Scheduler-0000
  Id                            : 9
  Mac Address                   : 02:35:ad:14:52:51
  Type                          : ethernet-csmacd
  Speed                         : 1000 Mbps
  MTU                           : 9001
  In octets                     : 12870444
  Out octets                    : 55973

  Interface                     : [ up ] AWS PV Network Device #0-WFP 802.3 MAC Layer LightWeight Filter-0000
  Id                            : 10
  Mac Address                   : 02:35:ad:14:52:51
  Type                          : ethernet-csmacd
  Speed                         : 1000 Mbps
  MTU                           : 9001
  In octets                     : 12870444
  Out octets                    : 55973

