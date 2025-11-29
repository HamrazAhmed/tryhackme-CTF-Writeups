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

[*] Network IP:

  Id                    IP Address            Netmask               Broadcast           
  7                     10.10.220.228         255.255.0.0           1                   
  1                     127.0.0.1             255.0.0.0             1                   

[*] Routing information:

  Destination           Next hop              Mask                  Metric              
  0.0.0.0               10.10.0.1             0.0.0.0               25                  
  10.10.0.0             10.10.220.228         255.255.0.0           281                 
  10.10.220.228         10.10.220.228         255.255.255.255       281                 
  10.10.255.255         10.10.220.228         255.255.255.255       281                 
  127.0.0.0             127.0.0.1             255.0.0.0             331                 
  127.0.0.1             127.0.0.1             255.255.255.255       331                 
  127.255.255.255       127.0.0.1             255.255.255.255       331                 
  169.254.169.123       10.10.0.1             255.255.255.255       50                  
  169.254.169.249       10.10.0.1             255.255.255.255       50                  
  169.254.169.250       10.10.0.1             255.255.255.255       50                  
  169.254.169.251       10.10.0.1             255.255.255.255       50                  
  169.254.169.253       10.10.0.1             255.255.255.255       50                  
  169.254.169.254       10.10.0.1             255.255.255.255       50                  
  224.0.0.0             127.0.0.1             240.0.0.0             331                 
  255.255.255.255       127.0.0.1             255.255.255.255       331                 

[*] TCP connections and listening ports:

  Local address         Local port            Remote address        Remote port           State               
  0.0.0.0               80                    0.0.0.0               0                     listen              
  0.0.0.0               135                   0.0.0.0               0                     listen              
  0.0.0.0               443                   0.0.0.0               0                     listen              
  0.0.0.0               445                   0.0.0.0               0                     listen              
  0.0.0.0               3306                  0.0.0.0               0                     listen              
  0.0.0.0               3389                  0.0.0.0               0                     listen              
  0.0.0.0               5985                  0.0.0.0               0                     listen              
  0.0.0.0               47001                 0.0.0.0               0                     listen              
  0.0.0.0               49664                 0.0.0.0               0                     listen              
  0.0.0.0               49665                 0.0.0.0               0                     listen              
  0.0.0.0               49666                 0.0.0.0               0                     listen              
  0.0.0.0               49667                 0.0.0.0               0                     listen              
  0.0.0.0               49668                 0.0.0.0               0                     listen              
  0.0.0.0               49673                 0.0.0.0               0                     listen              
  10.10.220.228         139                   0.0.0.0               0                     listen              
  10.10.220.228         49716                 52.165.165.26         443                   synSent             

[*] Listening UDP ports:

  Local address         Local port          
  0.0.0.0               123                 
  0.0.0.0               161                 
  0.0.0.0               3389                
  0.0.0.0               5353                
  0.0.0.0               5355                
  10.10.220.228         137                 
  10.10.220.228         138                 
  127.0.0.1             57116               

[*] Network services:

  Index                 Name                
  0                     Power               
  1                     mysql               
  2                     Server              
  3                     Themes              
  4                     SysMain             
  5                     Apache2.4           
  6                     IP Helper           
  7                     DNS Client          
  8                     DHCP Client         
  9                     Time Broker         
  10                    Workstation         
  11                    SNMP Service        
  12                    User Manager        
  13                    Windows Time        
  14                    CoreMessaging       
  15                    Plug and Play       
  16                    Print Spooler       
  17                    Task Scheduler      
  18                    Windows Update      
  19                    Remote Registry     
  20                    Amazon SSM Agent    
  21                    CNG Key Isolation   
  22                    COM+ Event System   
  23                    Windows Event Log   
  24                    IPsec Policy Agent  
  25                    Group Policy Client 
  26                    RPC Endpoint Mapper 
  27                    Web Account Manager 
  28                    AWS Lite Guest Agent
  29                    Device Setup Manager
  30                    Network List Service
  31                    System Events Broker
  32                    User Profile Service
  33                    Base Filtering Engine
  34                    Local Session Manager
  35                    TCP/IP NetBIOS Helper
  36                    Cryptographic Services
  37                    Certificate Propagation
  38                    Remote Desktop Services
  39                    Shell Hardware Detection
  40                    State Repository Service
  41                    Diagnostic Policy Service
  42                    Network Connection Broker
  43                    Security Accounts Manager
  44                    Windows Defender Firewall
  45                    Network Location Awareness
  46                    Windows Connection Manager
  47                    Windows Font Cache Service
  48                    Remote Procedure Call (RPC)
  49                    Update Orchestrator Service
  50                    User Access Logging Service
  51                    DCOM Server Process Launcher
  52                    Remote Desktop Configuration
  53                    Network Store Interface Service
  54                    Client License Service (ClipSVC)
  55                    Distributed Link Tracking Client
  56                    Capability Access Manager Service
  57                    System Event Notification Service
  58                    Connected Devices Platform Service
  59                    Windows Defender Antivirus Service
  60                    Windows Management Instrumentation
  61                    Distributed Transaction Coordinator
  62                    Microsoft Account Sign-in Assistant
  63                    Background Tasks Infrastructure Service
  64                    Connected User Experiences and Telemetry
  65                    WinHTTP Web Proxy Auto-Discovery Service
  66                    Windows Push Notifications System Service
  67                    Windows Remote Management (WS-Management)
  68                    Remote Desktop Services UserMode Port Redirector
  69                    Windows Defender Antivirus Network Inspection Service

[*] Processes:

  Id                    Status                Name                  Path                  Parameters          
  1                     running               System Idle Process                                             
  4                     running               System                                                          
  68                    running               Registry                                                        
  408                   running               smss.exe                                                        
  488                   running               dwm.exe                                                         
  524                   running               svchost.exe           C:\Windows\system32\  -k netsvcs -p       
  568                   running               csrss.exe                                                       
  636                   running               csrss.exe                                                       
  688                   running               wininit.exe                                                     
  700                   running               winlogon.exe                                                    
  768                   running               services.exe                                                    
  788                   running               lsass.exe             C:\Windows\system32\                      
  856                   running               svchost.exe           C:\Windows\System32\  -k termsvcs         
  888                   running               svchost.exe           C:\Windows\system32\  -k DcomLaunch -p    
  900                   running               svchost.exe           C:\Windows\System32\  -k LocalSystemNetworkRestricted -p
  916                   running               fontdrvhost.exe                                                 
  924                   running               fontdrvhost.exe                                                 
  984                   running               svchost.exe           C:\Windows\system32\  -k RPCSS -p         
  1036                  running               svchost.exe           C:\Windows\System32\  -k LocalServiceNetworkRestricted -p
  1148                  running               MsMpEng.exe                                                     
  1188                  running               svchost.exe           C:\Windows\system32\  -k LocalService -p  
  1276                  running               svchost.exe           C:\Windows\System32\  -k NetworkService -p
  1320                  running               svchost.exe           C:\Windows\system32\  -k LocalServiceNoNetwork -p
  1368                  running               svchost.exe           C:\Windows\system32\  -k LocalServiceNetworkRestricted -p
  1392                  running               WmiPrvSE.exe          C:\Windows\system32\wbem\                      
  1428                  running               LiteAgent.exe         C:\Program Files\Amazon\XenTools\                      
  1524                  running               svchost.exe           C:\Windows\system32\  -k LocalServiceNoNetworkFirewall -p
  1668                  running               svchost.exe           C:\Windows\system32\  -k netsvcs          
  1896                  running               spoolsv.exe           C:\Windows\System32\                      
  1924                  running               svchost.exe           C:\Windows\System32\  -k utcsvc -p        
  1972                  running               amazon-ssm-agent.exe  C:\Program Files\Amazon\SSM\                      
  1976                  running               snmp.exe              C:\Windows\System32\                      
  2016                  running               svchost.exe           C:\Windows\system32\  -k LocalService     
  2076                  running               httpd.exe             C:\xampp\apache\bin\  -k runservice       
  2108                  running               mysqld.exe            C:\xampp\mysql\bin\   --defaults-file=c:\xampp\mysql\bin\my.ini mysql
  2136                  running               svchost.exe           C:\Windows\System32\  -k smbsvcs          
  2256                  running               svchost.exe           C:\Windows\system32\  -k NetworkServiceNetworkRestricted -p
  2460                  running               httpd.exe             C:\xampp\apache\bin\  -d C:/xampp/apache  
  2836                  running               LogonUI.exe                                 /flags:0x2 /state0:0xa3a50855 /state1:0x41c64e6d
  2928                  running               CompatTelRunner.exe   C:\Windows\system32\                      
  3528                  running               svchost.exe           C:\Windows\system32\  -k appmodel -p      
  3752                  running               svchost.exe                                                     
  3996                  running               NisSrv.exe                                                      
  4264                  running               WmiPrvSE.exe          C:\Windows\system32\wbem\                      
  4332                  running               msdtc.exe             C:\Windows\System32\                      
  4572                  running               SIHClient.exe                                                   
  4752                  running               conhost.exe           \??\C:\Windows\system32\  0x4                 

[*] Storage information:

  Description                   : ["C:\\ Label:  Serial Number 7c0c3814"]
  Device id                     : [#<SNMP::Integer:0x00007f89e3a94268 @value=1>]
  Filesystem type               : ["unknown"]
  Device unit                   : [#<SNMP::Integer:0x00007f89e3a9a3e8 @value=4096>]
  Memory size                   : 19.46 GB
  Memory used                   : 15.49 GB

  Description                   : ["Virtual Memory"]
  Device id                     : [#<SNMP::Integer:0x00007f89e3a9d160 @value=2>]
  Filesystem type               : ["unknown"]
  Device unit                   : [#<SNMP::Integer:0x00007f89e3dd79c0 @value=65536>]
  Memory size                   : 3.12 GB
  Memory used                   : 862.88 MB

  Description                   : ["Physical Memory"]
