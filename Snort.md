---
Learn how to use Snort to detect real-time threats, analyse recorded traffic files and identify anomalies.
---

# Snort — Writeup

## Overview
### Snort — Writeup
![](https://assets.tryhackme.com/room-banners/snort-banner-pink.png)
### Introduction
This room expects you to be familiar with basic Linux command-line functionalities like general system navigation and Network fundamentals (ports, protocols and traffic data). The room aims to encourage you to start working with Snort to analyse live and captured traffic.
Before joining this room, we suggest completing the 'Network Fundamentals' module. If you have general knowledge of network basics and Linux fundamentals, you will be ready to begin! If you feel you need assistance in the Linux command line, you can always refer to our "Linux Fundamentals" rooms (here 1 2 3);
SNORT is an open-source, rule-based Network Intrusion Detection and Prevention System (NIDS/NIPS). It was developed and still maintained by Martin Roesch, open-source contributors, and the Cisco Talos team.
The official description: "Snort is the foremost Open Source Intrusion Prevention System (IPS) in the world. Snort IPS uses a series of rules that help define malicious network activity and uses those rules to find packets that match against them and generate alerts for users." https://www.snort.org/
### Interactive Material and VM
Once the machine had fully started, you will see a folder named "Task-Exercises" on the Desktop. Each exercise has an individual folder and files; use them accordingly to the questions.
Everything you need is located under the "Task-Exercises" folder.
There are two sub-folders available;
Config-Sample - Sample configuration and rule files. These files are provided to show what the configuration files look like. Installed Snort instance doesn't use them, so feel free to practice and modify them. Snort's original base files are located under /etc/snort folder.
Exercise-Files - There are separate folders for each task. Each folder contains pcap, log and rule files ready to play with.
Traffic Generator
The machine is offline, but there is a script (traffic-generator.sh) for you to generate traffic to your snort interface. You will use this script to trigger traffic to the snort interface. Once you run the script, it will ask you to choose the exercise type and then automatically open another terminal to show you the output of the selected action.
Note that each traffic is designed for a specific exercise. Make sure you start the snort instance and wait until to end of the script execution. Don't stop the traffic flood unless you choose the wrong exercise.
Run the "traffic generator.sh" file by executing it as sudo.
```text
executing the traffic generator script

           
user@ubuntu$ sudo ./traffic-generator.sh
```
General desktop overview. Traffic generator script in action.
Once you choose an action, the menu disappears and opens a terminal instance to show you the output of the action.
Navigate to the Task-Exercises folder and run the command "./.easy.sh" and write the output
```text
wx------ 2 ubuntu ubuntu 4.0K Jan  6  2022 Config-Sample
drwx------ 7 ubuntu ubuntu 4.0K Feb  4  2022 Exercise-Files
-rwxrwxr-x 1 ubuntu ubuntu 1.7K Jan 10  2022 traffic-generator.sh
ubuntu@ip-10-10-228-159:~/Desktop/Task-Exercises$ ./.
./                         .easy.sh
../                        .traffic-generator-source/
ubuntu@ip-10-10-228-159:~/Desktop/Task-Exercises$ ./.easy.sh 
Too Easy!
```
*Too Easy!*
### Introduction to IDS/IPS
Before diving into Snort and analysing traffic, let's have a brief overview of what an Intrusion Detection System (IDS) and Intrusion Prevention System (IPS) is. It is possible to configure your network infrastructure and use both of them, but before starting to use any of them, let's learn the differences.
Intrusion Detection System (IDS)
IDS is a passive monitoring solution for detecting possible malicious activities/patterns, abnormal incidents, and policy violations. It is responsible for generating alerts for each suspicious event.
There are two main types of IDS systems;
Network Intrusion Detection System (NIDS) - NIDS monitors the traffic flow from various areas of the network. The aim is to investigate the traffic on the entire subnet. If a signature is identified, an alert is created.
Host-based Intrusion Detection System (HIDS) - HIDS monitors the traffic flow from a single endpoint device. The aim is to investigate the traffic on a particular device. If a signature is identified, an alert is created.
Intrusion Prevention System (IPS)
IPS is an active protecting solution for preventing possible malicious activities/patterns, abnormal incidents, and policy violations. It is responsible for stopping/preventing/terminating the suspicious event as soon as the detection is performed.
There are four main types of IPS systems;
Network Intrusion Prevention System (NIPS) - NIPS monitors the traffic flow from various areas of the network. The aim is to protect the traffic on the entire subnet. If a signature is identified, the connection is terminated.
Behaviour-based Intrusion Prevention System (Network Behaviour Analysis - NBA) - Behaviour-based systems monitor the traffic flow from various areas of the network. The aim is to protect the traffic on the entire subnet. If a signature is identified, the connection is terminated.
Network Behaviour Analysis System works similar to NIPS. The difference between NIPS and Behaviour-based is; behaviour based systems require a training period (also known as "baselining") to learn the normal traffic and differentiate the malicious traffic and threats. This model provides more efficient results against new threats.
The system is trained to know the "normal" to detect "abnormal". The training period is crucial to avoid any false positives. In case of any security breach during the training period, the results will be highly problematic. Another critical point is to ensure that the system is well trained to recognise benign activities.
Wireless Intrusion Prevention System (WIPS) - WIPS monitors the traffic flow from of wireless network. The aim is to protect the wireless traffic and stop possible attacks launched from there. If a signature is identified, the connection is terminated.
Host-based Intrusion Prevention System (HIPS) - HIPS actively protects the traffic flow from a single endpoint device. The aim is to investigate the traffic on a particular device. If a signature is identified, the connection is terminated.
HIPS working mechanism is similar to HIDS. The difference between them is that while HIDS creates alerts for threats, HIPS stops the threats by terminating the connection.
Detection/Prevention Techniques
There are three main detection and prevention techniques used in IDS and IPS solutions;
Technique	Approach
Signature-Based
This technique relies on rules that identify the specific patterns of the known malicious behaviour. This model helps detect known threats.
Behaviour-Based
This technique identifies new threats with new patterns that pass through signatures. The model compares the known/normal with unknown/abnormal behaviours. This model helps detect previously unknown or new threats.
Policy-Based	This technique compares detected activities with system configuration and security policies. This model helps detect policy violations.
Summary
Phew! That was a long ride and lots of information. Let's summarise the overall functions of the IDS and IPS in a nutshell.
IDS can identify threats but require user assistance to stop them.
IPS can identify and block the threats with less user assistance at the detection time.
Now let's talk about Snort. Here is the rest of the official description of the snort;
"Snort can be deployed inline to stop these packets, as well. Snort has three primary uses: As a packet sniffer like tcpdump, as a packet logger — which is useful for network traffic debugging, or it can be used as a full-blown network intrusion prevention system. Snort can be downloaded and configured for personal and business use alike."
SNORT is an open-source, rule-based Network Intrusion Detection and Prevention System (NIDS/NIPS). It was developed and still maintained by Martin Roesch, open-source contributors, and the Cisco Talos team.
Capabilities of Snort;
Live traffic analysis
Attack and probe detection
Packet logging
Protocol analysis
Real-time alerting
Modules & plugins
Pre-processors
Cross-platform support! (Linux & Windows)
Snort has three main use models;
Sniffer Mode - Read IP packets and prompt them in the console application.
Packet Logger Mode - Log all IP packets (inbound and outbound) that visit the network.
NIDS (Network Intrusion Detection System)  and NIPS (Network Intrusion Prevention System) Modes - Log/drop the packets that are deemed as malicious according to the user-defined rules.
Which snort mode can help you stop the threats on a local machine?
*HIPS*
Which snort mode can help you detect threats on a local network?
*NIDS*
Which snort mode can help you detect the threats on a local machine?
*HIDS*
Which snort mode can help you stop the threats on a local network?
*NIPS*
Which snort mode works similar to NIPS mode?
*NBA*
![[Pasted image 20221205112803.png]]
completo sistema de prevención de intrusiones en la red
According to the official description of the snort, what kind of NIPS is it?
*full-blown*
NBA training period is also known as ...
*baselining*
### First Interaction with Snort
The First Interaction with Snort
First, let's verify snort is installed. The following command will show you the instance version.
```text
version check

           
user@ubuntu$ snort -V

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build XXXXXX) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11
```
Before getting your hands dirty, we should ensure our configuration file is valid.
Here "-T" is used for testing configuration, and "-c" is identifying the configuration file (snort.conf).
Note that it is possible to use an additional configuration file by pointing it with "-c".
```text
configuration check

           
user@ubuntu$ sudo snort -c /etc/snort/snort.conf -T 

        --== Initializing Snort ==--
Initializing Output Plugins!
Initializing Preprocessors!
Initializing Plug-ins!
... [Output truncated]
        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build XXXX) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

           Rules Engine: SF_SNORT_DETECTION_ENGINE  Version 2.4  
           Preprocessor Object: SF_GTP  Version 1.1  
           Preprocessor Object: SF_SIP  Version 1.1  
           Preprocessor Object: SF_SSH  Version 1.1  
           Preprocessor Object: SF_SMTP  Version 1.1  
           Preprocessor Object: SF_POP  Version 1.0  
           Preprocessor Object: SF_DCERPC2  Version 1.0  
           Preprocessor Object: SF_IMAP  Version 1.0  
           Preprocessor Object: SF_DNP3  Version 1.1  
           Preprocessor Object: SF_SSLPP  Version 1.1  
           Preprocessor Object: SF_MODBUS  Version 1.1  
           Preprocessor Object: SF_SDF  Version 1.1  
           Preprocessor Object: SF_REPUTATION  Version 1.1  
           Preprocessor Object: SF_DNS  Version 1.1  
           Preprocessor Object: SF_FTPTELNET  Version 1.2  
... [Output truncated]
Snort successfully validated the configuration!
Snort exiting
```
Once we use a configuration file, snort got much more power! The configuration file is an all-in-one management file of the snort. Rules, plugins, detection mechanisms, default actions and output settings are identified here. It is possible to have multiple configuration files for different purposes and cases but can only use one at runtime.
Note that every time you start the Snort, it will automatically show the default banner and initial information about your setup. You can prevent this by using the "-q" parameter.
Parameter	Description
-V / --version	This parameter provides information about your instance version.
-c	Identifying the configuration file
-T	Snort's self-test parameter, you can test your setup with this parameter.
-q	Quiet mode prevents snort from displaying the default banner and initial information about your setup.
That was an easy one; let's continue exploring snort modes!
Run the Snort instance and check the build number.
```text
ubuntu@ip-10-10-228-159:~/Desktop/Task-Exercises$ snort -V

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11
```
*149*
Test the current instance with "/etc/snort/snort.conf" file and check how many rules are loaded with the current build.
```text
ubuntu@ip-10-10-228-159:~/Desktop/Task-Exercises$ sudo snort -c /etc/snort/snort.conf -T
Running in Test mode

        --== Initializing Snort ==--
Initializing Output Plugins!
Initializing Preprocessors!
Initializing Plug-ins!
Parsing Rules file "/etc/snort/snort.conf"
PortVar 'HTTP_PORTS' defined :  [ 80:81 311 383 591 593 901 1220 1414 1741 1830 2301 2381 2809 3037 3128 3702 4343 4848 5250 6988 7000:7001 7144:7145 7510 7777 7779 8000 8008 8014 8028 8080 8085 8088 8090 8118 8123 8180:8181 8243 8280 8300 8800 8888 8899 9000 9060 9080 9090:9091 9443 9999 11371 34443:34444 41080 50002 55555 ]
PortVar 'SHELLCODE_PORTS' defined :  [ 0:79 81:65535 ]
PortVar 'ORACLE_PORTS' defined :  [ 1024:65535 ]
PortVar 'SSH_PORTS' defined :  [ 22 ]
PortVar 'FTP_PORTS' defined :  [ 21 2100 3535 ]
PortVar 'SIP_PORTS' defined :  [ 5060:5061 5600 ]
PortVar 'FILE_DATA_PORTS' defined :  [ 80:81 110 143 311 383 591 593 901 1220 1414 1741 1830 2301 2381 2809 3037 3128 3702 4343 4848 5250 6988 7000:7001 7144:7145 7510 7777 7779 8000 8008 8014 8028 8080 8085 8088 8090 8118 8123 8180:8181 8243 8280 8300 8800 8888 8899 9000 9060 9080 9090:9091 9443 9999 11371 34443:34444 41080 50002 55555 ]
PortVar 'GTP_PORTS' defined :  [ 2123 2152 3386 ]
Detection:
   Search-Method = AC-Full-Q
    Split Any/Any group = enabled
    Search-Method-Optimizations = enabled
    Maximum pattern length = 20
Tagged Packet Limit: 256
Loading dynamic engine /usr/lib/snort_dynamicengine/libsf_engine.so... done
Loading all dynamic detection libs from /usr/lib/snort_dynamicrules...
WARNING: No dynamic libraries found in directory /usr/lib/snort_dynamicrules.
  Finished Loading all dynamic detection libs from /usr/lib/snort_dynamicrules
Loading all dynamic preprocessor libs from /usr/lib/snort_dynamicpreprocessor/...
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_ssl_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_sip_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_imap_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_smtp_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_reputation_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_ftptelnet_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_dce2_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_sdf_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_modbus_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_gtp_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_dns_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_dnp3_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_ssh_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_pop_preproc.so... done
  Finished Loading all dynamic preprocessor libs from /usr/lib/snort_dynamicpreprocessor/
Log directory = /var/log/snort
WARNING: ip4 normalizations disabled because not inline.
WARNING: tcp normalizations disabled because not inline.
WARNING: icmp4 normalizations disabled because not inline.
WARNING: ip6 normalizations disabled because not inline.
WARNING: icmp6 normalizations disabled because not inline.
Frag3 global config:
    Max frags: 65536
    Fragment memory cap: 4194304 bytes
Frag3 engine config:
    Bound Address: default
    Target-based policy: WINDOWS
    Fragment timeout: 180 seconds
    Fragment min_ttl:   1
    Fragment Anomalies: Alert
    Overlap Limit:     10
    Min fragment Length:     100
      Max Expected Streams: 768
Stream global config:
    Track TCP sessions: ACTIVE
    Max TCP sessions: 262144
    TCP cache pruning timeout: 30 seconds
    TCP cache nominal timeout: 3600 seconds
    Memcap (for reassembly packet storage): 8388608
    Track UDP sessions: ACTIVE
    Max UDP sessions: 131072
    UDP cache pruning timeout: 30 seconds
    UDP cache nominal timeout: 180 seconds
    Track ICMP sessions: INACTIVE
    Track IP sessions: INACTIVE
    Log info if session memory consumption exceeds 1048576
    Send up to 2 active responses
    Wait at least 5 seconds between responses
    Protocol Aware Flushing: ACTIVE
        Maximum Flush Point: 16000
Stream TCP Policy config:
    Bound Address: default
    Reassembly Policy: WINDOWS
    Timeout: 180 seconds
    Limit on TCP Overlaps: 10
    Maximum number of bytes to queue per session: 1048576
    Maximum number of segs to queue per session: 2621
    Options:
        Require 3-Way Handshake: YES
        3-Way Handshake Timeout: 180
        Detect Anomalies: YES
    Reassembly Ports:
      21 client (Footprint) 
      22 client (Footprint) 
      23 client (Footprint) 
      25 client (Footprint) 
      42 client (Footprint) 
      53 client (Footprint) 
      79 client (Footprint) 
      80 client (Footprint) server (Footprint)
      81 client (Footprint) server (Footprint)
      109 client (Footprint) 
      110 client (Footprint) 
      111 client (Footprint) 
      113 client (Footprint) 
      119 client (Footprint) 
      135 client (Footprint) 
      136 client (Footprint) 
      137 client (Footprint) 
      139 client (Footprint) 
      143 client (Footprint) 
      161 client (Footprint) 
      additional ports configured but not printed.
Stream UDP Policy config:
    Timeout: 180 seconds
HttpInspect Config:
    GLOBAL CONFIG
      Detect Proxy Usage:       NO
      IIS Unicode Map Filename: /etc/snort/unicode.map
      IIS Unicode Map Codepage: 1252
      Memcap used for logging URI and Hostname: 150994944
      Max Gzip Memory: 104857600
      Max Gzip Sessions: 201649
      Gzip Compress Depth: 65535
      Gzip Decompress Depth: 65535
    DEFAULT SERVER CONFIG:
      Server profile: All
      Ports (PAF): 80 81 311 383 591 593 901 1220 1414 1741 1830 2301 2381 2809 3037 3128 3702 4343 4848 5250 6988 7000 7001 7144 7145 7510 7777 7779 8000 8008 8014 8028 8080 8085 8088 8090 8118 8123 8180 8181 8243 8280 8300 8800 8888 8899 9000 9060 9080 9090 9091 9443 9999 11371 34443 34444 41080 50002 55555 
      Server Flow Depth: 0
      Client Flow Depth: 0
      Max Chunk Length: 500000
      Small Chunk Length Evasion: chunk size <= 10, threshold >= 5 times
      Max Header Field Length: 750
      Max Number Header Fields: 100
      Max Number of WhiteSpaces allowed with header folding: 200
      Inspect Pipeline Requests: YES
      URI Discovery Strict Mode: NO
      Allow Proxy Usage: NO
      Disable Alerting: NO
      Oversize Dir Length: 500
      Only inspect URI: NO
      Normalize HTTP Headers: NO
      Inspect HTTP Cookies: YES
      Inspect HTTP Responses: YES
      Extract Gzip from responses: YES
      Decompress response files:   
      Unlimited decompression of gzip data from responses: YES
      Normalize Javascripts in HTTP Responses: YES
      Max Number of WhiteSpaces allowed with Javascript Obfuscation in HTTP responses: 200
      Normalize HTTP Cookies: NO
      Enable XFF and True Client IP: NO
      Log HTTP URI data: NO
      Log HTTP Hostname data: NO
      Extended ASCII code support in URI: NO
      Ascii: YES alert: NO
      Double Decoding: YES alert: NO
      %U Encoding: YES alert: YES
      Bare Byte: YES alert: NO
      UTF 8: YES alert: NO
      IIS Unicode: YES alert: NO
      Multiple Slash: YES alert: NO
      IIS Backslash: YES alert: NO
      Directory Traversal: YES alert: NO
      Web Root Traversal: YES alert: NO
      Apache WhiteSpace: YES alert: NO
      IIS Delimiter: YES alert: NO
      IIS Unicode Map: GLOBAL IIS UNICODE MAP CONFIG
      Non-RFC Compliant Characters: 0x00 0x01 0x02 0x03 0x04 0x05 0x06 0x07 
      Whitespace Characters: 0x09 0x0b 0x0c 0x0d 
rpc_decode arguments:
    Ports to decode RPC on: 111 32770 32771 32772 32773 32774 32775 32776 32777 32778 32779 
    alert_fragments: INACTIVE
    alert_large_fragments: INACTIVE
    alert_incomplete: INACTIVE
    alert_multiple_requests: INACTIVE
FTPTelnet Config:
    GLOBAL CONFIG
      Inspection Type: stateful
      Check for Encrypted Traffic: YES alert: NO
      Continue to check encrypted data: YES
    TELNET CONFIG:
      Ports: 23 
      Are You There Threshold: 20
      Normalize: YES
      Detect Anomalies: YES
    FTP CONFIG:
      FTP Server: default
        Ports (PAF): 21 2100 3535 
        Check for Telnet Cmds: YES alert: YES
        Ignore Telnet Cmd Operations: YES alert: YES
        Ignore open data channels: NO
      FTP Client: default
        Check for Bounce Attacks: YES alert: YES
        Check for Telnet Cmds: YES alert: YES
        Ignore Telnet Cmd Operations: YES alert: YES
        Max Response Length: 256
SMTP Config:
    Ports: 25 465 587 691 
    Inspection Type: Stateful
    Normalize: ATRN AUTH BDAT DATA DEBUG EHLO EMAL ESAM ESND ESOM ETRN EVFY EXPN HELO HELP IDENT MAIL NOOP ONEX QUEU QUIT RCPT RSET SAML SEND STARTTLS SOML TICK TIME TURN TURNME VERB VRFY X-EXPS XADR XAUTH XCIR XEXCH50 XGEN XLICENSE X-LINK2STATE XQUE XSTA XTRN XUSR CHUNKING X-ADAT X-DRCP X-ERCP X-EXCH50 
    Ignore Data: No
    Ignore TLS Data: No
    Ignore SMTP Alerts: No
    Max Command Line Length: 512
    Max Specific Command Line Length: 
       ATRN:255 AUTH:246 BDAT:255 DATA:246 DEBUG:255 
       EHLO:500 EMAL:255 ESAM:255 ESND:255 ESOM:255 
       ETRN:246 EVFY:255 EXPN:255 HELO:500 HELP:500 
       IDENT:255 MAIL:260 NOOP:255 ONEX:246 QUEU:246 
       QUIT:246 RCPT:300 RSET:246 SAML:246 SEND:246 
       SIZE:255 STARTTLS:246 SOML:246 TICK:246 TIME:246 
       TURN:246 TURNME:246 VERB:246 VRFY:255 X-EXPS:246 
       XADR:246 XAUTH:246 XCIR:246 XEXCH50:246 XGEN:246 
       XLICENSE:246 X-LINK2STATE:246 XQUE:246 XSTA:246 XTRN:246 
       XUSR:246 
    Max Header Line Length: 1000
    Max Response Line Length: 512
    X-Link2State Alert: Yes
    Drop on X-Link2State Alert: No
    Alert on commands: None
    Alert on unknown commands: No
    SMTP Memcap: 838860
    MIME Max Mem: 838860
    Base64 Decoding: Enabled
    Base64 Decoding Depth: Unlimited
    Quoted-Printable Decoding: Enabled
    Quoted-Printable Decoding Depth: Unlimited
    Unix-to-Unix Decoding: Enabled
    Unix-to-Unix Decoding Depth: Unlimited
    Non-Encoded MIME attachment Extraction: Enabled
    Non-Encoded MIME attachment Extraction Depth: Unlimited
    Log Attachment filename: Enabled
    Log MAIL FROM Address: Enabled
    Log RCPT TO Addresses: Enabled
    Log Email Headers: Enabled
    Email Hdrs Log Depth: 1464
SSH config: 
    Autodetection: ENABLED
    Challenge-Response Overflow Alert: ENABLED
    SSH1 CRC32 Alert: ENABLED
    Server Version String Overflow Alert: ENABLED
    Protocol Mismatch Alert: ENABLED
    Bad Message Direction Alert: DISABLED
    Bad Payload Size Alert: DISABLED
    Unrecognized Version Alert: DISABLED
    Max Encrypted Packets: 20  
    Max Server Version String Length: 100  
    MaxClientBytes: 19600 (Default) 
    Ports:
	22
DCE/RPC 2 Preprocessor Configuration
  Global Configuration
    DCE/RPC Defragmentation: Enabled
    Memcap: 102400 KB
    Events: co 
    SMB Fingerprint policy: Disabled
  Server Default Configuration
    Policy: WinXP
    Detect ports (PAF)
      SMB: 139 445 
      TCP: 135 
      UDP: 135 
      RPC over HTTP server: 593 
      RPC over HTTP proxy: None
    Autodetect ports (PAF)
      SMB: None
      TCP: 1025-65535 
      UDP: 1025-65535 
      RPC over HTTP server: 1025-65535 
      RPC over HTTP proxy: None
    Invalid SMB shares: C$ D$ ADMIN$ 
    Maximum SMB command chaining: 3 commands
    SMB file inspection: Disabled
DNS config: 
    DNS Client rdata txt Overflow Alert: ACTIVE
    Obsolete DNS RR Types Alert: INACTIVE
    Experimental DNS RR Types Alert: INACTIVE
    Ports: 53
SSLPP config:
    Encrypted packets: not inspected
    Ports:
      443      465      563      636      989
      992      993      994      995     7801
     7802     7900     7901     7902     7903
     7904     7905     7906     7907     7908
     7909     7910     7911     7912     7913
     7914     7915     7916     7917     7918
     7919     7920
    Server side data is trusted
    Maximum SSL Heartbeat length: 0
Sensitive Data preprocessor config: 
    Global Alert Threshold: 25
    Masked Output: DISABLED
SIP config: 
    Max number of sessions: 40000  
    Max number of dialogs in a session: 4 (Default) 
    Status: ENABLED
    Ignore media channel: DISABLED
    Max URI length: 512  
    Max Call ID length: 80  
    Max Request name length: 20 (Default) 
    Max From length: 256 (Default) 
    Max To length: 256 (Default) 
    Max Via length: 1024 (Default) 
    Max Contact length: 512  
    Max Content length: 2048  
    Ports:
	5060	5061	5600
    Methods:
	  invite cancel ack bye register options refer subscribe update join info message notify benotify do qauth sprack publish service unsubscribe prack
IMAP Config:
    Ports: 143 
    IMAP Memcap: 838860
    MIME Max Mem: 838860
    Base64 Decoding: Enabled
    Base64 Decoding Depth: Unlimited
    Quoted-Printable Decoding: Enabled
    Quoted-Printable Decoding Depth: Unlimited
    Unix-to-Unix Decoding: Enabled
    Unix-to-Unix Decoding Depth: Unlimited
    Non-Encoded MIME attachment Extraction: Enabled
    Non-Encoded MIME attachment Extraction Depth: Unlimited
POP Config:
    Ports: 110 
    POP Memcap: 838860
    MIME Max Mem: 838860
    Base64 Decoding: Enabled
    Base64 Decoding Depth: Unlimited
    Quoted-Printable Decoding: Enabled
    Quoted-Printable Decoding Depth: Unlimited
    Unix-to-Unix Decoding: Enabled
    Unix-to-Unix Decoding Depth: Unlimited
    Non-Encoded MIME attachment Extraction: Enabled
    Non-Encoded MIME attachment Extraction Depth: Unlimited
Modbus config: 
    Ports:
	502
DNP3 config: 
    Memcap: 262144
    Check Link-Layer CRCs: ENABLED
    Ports:
	20000

+++++++++++++++++++++++++++++++++++++++++++++++++++
Initializing rule chains...
WARNING: /etc/snort/rules/chat.rules(33) threshold (in rule) is deprecated; use detection_filter instead.

WARNING: /etc/snort/rules/community-sql-injection.rules(6) GID 1 SID 100000106 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-sql-injection.rules(7) GID 1 SID 100000107 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-sql-injection.rules(8) GID 1 SID 100000108 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-sql-injection.rules(9) GID 1 SID 100000109 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-sql-injection.rules(11) GID 1 SID 100000192 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-sql-injection.rules(12) GID 1 SID 100000193 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-sql-injection.rules(13) GID 1 SID 100000194 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-sql-injection.rules(14) GID 1 SID 100000690 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-sql-injection.rules(15) GID 1 SID 100000691 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-client.rules(6) GID 1 SID 100000118 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-client.rules(7) GID 1 SID 100000119 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-client.rules(9) GID 1 SID 100000228 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-client.rules(14) GID 1 SID 100000284 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-client.rules(16) GID 1 SID 100000447 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-client.rules(18) GID 1 SID 100000692 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-client.rules(20) GID 1 SID 100000693 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-client.rules(23) GID 1 SID 100000864 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-iis.rules(7) GID 1 SID 100000138 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-iis.rules(8) GID 1 SID 100000139 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-iis.rules(9) GID 1 SID 100000173 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-iis.rules(10) GID 1 SID 100000174 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(6) GID 1 SID 100000121 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(7) GID 1 SID 100000122 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(8) GID 1 SID 100000129 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(9) GID 1 SID 100000130 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(10) GID 1 SID 100000131 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(12) GID 1 SID 100000132 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(13) GID 1 SID 100000133 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(14) GID 1 SID 100000140 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(15) GID 1 SID 100000141 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(16) GID 1 SID 100000142 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(17) GID 1 SID 100000143 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(18) GID 1 SID 100000144 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(19) GID 1 SID 100000145 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(20) GID 1 SID 100000146 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(22) GID 1 SID 100000148 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(23) GID 1 SID 100000149 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(24) GID 1 SID 100000150 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(25) GID 1 SID 100000177 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(26) GID 1 SID 100000178 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(27) GID 1 SID 100000179 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(28) GID 1 SID 100000184 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(29) GID 1 SID 100000185 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(30) GID 1 SID 100000200 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(31) GID 1 SID 100000209 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(33) GID 1 SID 100000216 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(34) GID 1 SID 100000217 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(35) GID 1 SID 100000225 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(38) GID 1 SID 100000237 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(39) GID 1 SID 100000302 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(40) GID 1 SID 100000303 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(42) GID 1 SID 100000313 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(43) GID 1 SID 100000314 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(49) GID 1 SID 100000317 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(50) GID 1 SID 100000318 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(51) GID 1 SID 100000319 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(52) GID 1 SID 100000320 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(53) GID 1 SID 100000321 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(54) GID 1 SID 100000322 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(55) GID 1 SID 100000323 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(56) GID 1 SID 100000324 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(57) GID 1 SID 100000325 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(58) GID 1 SID 100000326 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(59) GID 1 SID 100000327 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(60) GID 1 SID 100000328 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(61) GID 1 SID 100000329 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(62) GID 1 SID 100000330 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(63) GID 1 SID 100000331 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(64) GID 1 SID 100000332 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(65) GID 1 SID 100000333 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(66) GID 1 SID 100000334 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(67) GID 1 SID 100000335 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(68) GID 1 SID 100000336 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(69) GID 1 SID 100000337 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(70) GID 1 SID 100000338 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(71) GID 1 SID 100000339 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(72) GID 1 SID 100000340 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(73) GID 1 SID 100000341 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(74) GID 1 SID 100000342 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(75) GID 1 SID 100000343 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(76) GID 1 SID 100000344 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(77) GID 1 SID 100000345 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(78) GID 1 SID 100000346 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(79) GID 1 SID 100000347 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(80) GID 1 SID 100000348 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(81) GID 1 SID 100000349 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(82) GID 1 SID 100000350 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(83) GID 1 SID 100000351 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(84) GID 1 SID 100000352 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(85) GID 1 SID 100000353 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(86) GID 1 SID 100000354 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(87) GID 1 SID 100000355 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(88) GID 1 SID 100000356 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(89) GID 1 SID 100000357 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(90) GID 1 SID 100000358 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(91) GID 1 SID 100000359 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(92) GID 1 SID 100000360 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(93) GID 1 SID 100000361 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(94) GID 1 SID 100000362 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(95) GID 1 SID 100000363 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(96) GID 1 SID 100000364 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(97) GID 1 SID 100000365 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(98) GID 1 SID 100000366 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(99) GID 1 SID 100000367 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(100) GID 1 SID 100000368 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(101) GID 1 SID 100000369 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(102) GID 1 SID 100000370 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(103) GID 1 SID 100000371 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(104) GID 1 SID 100000372 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(105) GID 1 SID 100000373 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(106) GID 1 SID 100000374 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(107) GID 1 SID 100000375 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(108) GID 1 SID 100000376 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(109) GID 1 SID 100000377 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(110) GID 1 SID 100000378 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(111) GID 1 SID 100000379 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(112) GID 1 SID 100000380 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(113) GID 1 SID 100000382 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(114) GID 1 SID 100000383 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(115) GID 1 SID 100000384 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(116) GID 1 SID 100000385 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(117) GID 1 SID 100000386 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(119) GID 1 SID 100000387 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(120) GID 1 SID 100000388 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(121) GID 1 SID 100000389 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(122) GID 1 SID 100000390 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(123) GID 1 SID 100000391 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(124) GID 1 SID 100000392 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(125) GID 1 SID 100000393 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(126) GID 1 SID 100000394 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(127) GID 1 SID 100000395 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(128) GID 1 SID 100000396 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(129) GID 1 SID 100000397 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(130) GID 1 SID 100000398 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(131) GID 1 SID 100000399 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(132) GID 1 SID 100000400 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(133) GID 1 SID 100000401 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(134) GID 1 SID 100000402 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(135) GID 1 SID 100000403 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(136) GID 1 SID 100000404 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(137) GID 1 SID 100000405 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(138) GID 1 SID 100000406 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(139) GID 1 SID 100000407 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(140) GID 1 SID 100000408 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(141) GID 1 SID 100000409 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(142) GID 1 SID 100000410 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(143) GID 1 SID 100000411 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(144) GID 1 SID 100000412 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(145) GID 1 SID 100000413 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(146) GID 1 SID 100000414 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(147) GID 1 SID 100000415 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(148) GID 1 SID 100000416 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(149) GID 1 SID 100000417 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(150) GID 1 SID 100000418 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(151) GID 1 SID 100000419 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(152) GID 1 SID 100000420 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(153) GID 1 SID 100000421 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(154) GID 1 SID 100000422 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(155) GID 1 SID 100000423 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(156) GID 1 SID 100000424 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(157) GID 1 SID 100000425 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(158) GID 1 SID 100000426 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(161) GID 1 SID 100000427 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(162) GID 1 SID 100000428 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(163) GID 1 SID 100000429 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(166) GID 1 SID 100000430 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(167) GID 1 SID 100000431 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(168) GID 1 SID 100000432 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(169) GID 1 SID 100000433 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(170) GID 1 SID 100000434 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(171) GID 1 SID 100000435 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(172) GID 1 SID 100000436 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(173) GID 1 SID 100000437 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(174) GID 1 SID 100000438 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(175) GID 1 SID 100000439 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(176) GID 1 SID 100000440 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(177) GID 1 SID 100000441 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(178) GID 1 SID 100000442 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(179) GID 1 SID 100000443 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(180) GID 1 SID 100000444 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(181) GID 1 SID 100000448 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(182) GID 1 SID 100000449 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(183) GID 1 SID 100000450 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(184) GID 1 SID 100000451 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(185) GID 1 SID 100000452 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(186) GID 1 SID 100000453 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(187) GID 1 SID 100000454 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(188) GID 1 SID 100000455 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(189) GID 1 SID 100000456 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(190) GID 1 SID 100000457 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(191) GID 1 SID 100000458 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(192) GID 1 SID 100000459 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(193) GID 1 SID 100000460 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(194) GID 1 SID 100000461 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(195) GID 1 SID 100000462 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(196) GID 1 SID 100000694 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(197) GID 1 SID 100000695 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(198) GID 1 SID 100000696 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(199) GID 1 SID 100000697 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(200) GID 1 SID 100000698 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(201) GID 1 SID 100000699 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(202) GID 1 SID 100000700 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(203) GID 1 SID 100000701 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(204) GID 1 SID 100000702 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(207) GID 1 SID 100000890 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(208) GID 1 SID 100000891 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(211) GID 1 SID 100000895 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(212) GID 1 SID 100000896 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(213) GID 1 SID 100000897 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(214) GID 1 SID 100000898 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(215) GID 1 SID 100000899 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(6) GID 1 SID 100000151 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(7) GID 1 SID 100000186 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(8) GID 1 SID 100000187 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(9) GID 1 SID 100000188 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(10) GID 1 SID 100000195 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(11) GID 1 SID 100000201 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(12) GID 1 SID 100000202 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(13) GID 1 SID 100000203 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(14) GID 1 SID 100000204 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(15) GID 1 SID 100000205 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(16) GID 1 SID 100000206 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(17) GID 1 SID 100000211 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(18) GID 1 SID 100000212 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(19) GID 1 SID 100000213 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(20) GID 1 SID 100000214 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(21) GID 1 SID 100000218 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(22) GID 1 SID 100000220 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(23) GID 1 SID 100000221 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(24) GID 1 SID 100000285 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(25) GID 1 SID 100000286 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(26) GID 1 SID 100000287 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(27) GID 1 SID 100000288 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(28) GID 1 SID 100000289 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(29) GID 1 SID 100000290 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(30) GID 1 SID 100000291 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(31) GID 1 SID 100000292 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(32) GID 1 SID 100000293 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(33) GID 1 SID 100000294 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(34) GID 1 SID 100000295 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(35) GID 1 SID 100000296 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(36) GID 1 SID 100000297 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(37) GID 1 SID 100000298 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(38) GID 1 SID 100000299 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(39) GID 1 SID 100000300 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(40) GID 1 SID 100000304 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(41) GID 1 SID 100000305 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(42) GID 1 SID 100000306 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(43) GID 1 SID 100000307 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(44) GID 1 SID 100000308 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(45) GID 1 SID 100000309 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(46) GID 1 SID 100000445 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(48) GID 1 SID 100000463 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(49) GID 1 SID 100000464 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(50) GID 1 SID 100000465 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(51) GID 1 SID 100000466 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(52) GID 1 SID 100000467 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(53) GID 1 SID 100000468 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(54) GID 1 SID 100000469 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(55) GID 1 SID 100000470 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(56) GID 1 SID 100000471 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(57) GID 1 SID 100000472 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(58) GID 1 SID 100000473 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(59) GID 1 SID 100000474 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(60) GID 1 SID 100000475 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(61) GID 1 SID 100000476 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(62) GID 1 SID 100000477 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(63) GID 1 SID 100000478 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(64) GID 1 SID 100000479 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(65) GID 1 SID 100000480 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(66) GID 1 SID 100000481 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(67) GID 1 SID 100000482 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(68) GID 1 SID 100000483 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(69) GID 1 SID 100000484 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(70) GID 1 SID 100000485 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(71) GID 1 SID 100000486 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(72) GID 1 SID 100000487 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(73) GID 1 SID 100000488 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(74) GID 1 SID 100000489 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(75) GID 1 SID 100000490 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(76) GID 1 SID 100000491 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(77) GID 1 SID 100000492 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(78) GID 1 SID 100000493 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(79) GID 1 SID 100000494 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(80) GID 1 SID 100000495 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(81) GID 1 SID 100000496 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(82) GID 1 SID 100000497 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(83) GID 1 SID 100000498 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(84) GID 1 SID 100000499 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(85) GID 1 SID 100000500 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(86) GID 1 SID 100000501 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(87) GID 1 SID 100000502 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(88) GID 1 SID 100000503 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(89) GID 1 SID 100000504 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(90) GID 1 SID 100000505 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(91) GID 1 SID 100000506 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(92) GID 1 SID 100000507 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(93) GID 1 SID 100000508 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(94) GID 1 SID 100000509 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(95) GID 1 SID 100000510 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(96) GID 1 SID 100000511 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(97) GID 1 SID 100000512 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(98) GID 1 SID 100000513 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(99) GID 1 SID 100000514 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(100) GID 1 SID 100000515 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(101) GID 1 SID 100000516 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(102) GID 1 SID 100000517 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(103) GID 1 SID 100000518 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(104) GID 1 SID 100000519 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(105) GID 1 SID 100000520 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(106) GID 1 SID 100000521 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(107) GID 1 SID 100000522 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(108) GID 1 SID 100000523 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(109) GID 1 SID 100000524 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(110) GID 1 SID 100000525 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(111) GID 1 SID 100000526 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(112) GID 1 SID 100000527 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(113) GID 1 SID 100000528 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(114) GID 1 SID 100000529 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(115) GID 1 SID 100000530 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(116) GID 1 SID 100000531 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(117) GID 1 SID 100000532 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(118) GID 1 SID 100000533 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(119) GID 1 SID 100000534 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(120) GID 1 SID 100000535 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(121) GID 1 SID 100000536 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(122) GID 1 SID 100000537 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(123) GID 1 SID 100000538 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(124) GID 1 SID 100000539 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(125) GID 1 SID 100000540 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(126) GID 1 SID 100000541 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(127) GID 1 SID 100000542 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(128) GID 1 SID 100000543 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(129) GID 1 SID 100000544 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(130) GID 1 SID 100000545 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(131) GID 1 SID 100000546 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(132) GID 1 SID 100000547 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(133) GID 1 SID 100000548 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(134) GID 1 SID 100000549 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(135) GID 1 SID 100000550 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(136) GID 1 SID 100000551 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(137) GID 1 SID 100000552 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(138) GID 1 SID 100000553 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(139) GID 1 SID 100000554 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(140) GID 1 SID 100000555 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(141) GID 1 SID 100000556 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(142) GID 1 SID 100000557 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(143) GID 1 SID 100000558 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(144) GID 1 SID 100000559 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(145) GID 1 SID 100000560 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(146) GID 1 SID 100000561 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(147) GID 1 SID 100000562 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(148) GID 1 SID 100000563 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(149) GID 1 SID 100000564 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(150) GID 1 SID 100000565 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(151) GID 1 SID 100000566 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(152) GID 1 SID 100000567 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(153) GID 1 SID 100000568 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(154) GID 1 SID 100000569 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(155) GID 1 SID 100000570 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(156) GID 1 SID 100000571 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(157) GID 1 SID 100000572 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(158) GID 1 SID 100000573 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(159) GID 1 SID 100000574 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(160) GID 1 SID 100000575 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(161) GID 1 SID 100000576 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(162) GID 1 SID 100000577 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(163) GID 1 SID 100000578 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(164) GID 1 SID 100000579 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(165) GID 1 SID 100000580 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(166) GID 1 SID 100000581 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(167) GID 1 SID 100000582 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(168) GID 1 SID 100000583 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(169) GID 1 SID 100000584 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(170) GID 1 SID 100000585 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(171) GID 1 SID 100000586 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(172) GID 1 SID 100000587 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(173) GID 1 SID 100000588 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(174) GID 1 SID 100000589 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(175) GID 1 SID 100000590 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(176) GID 1 SID 100000591 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(177) GID 1 SID 100000592 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(178) GID 1 SID 100000593 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(179) GID 1 SID 100000594 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(180) GID 1 SID 100000595 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(181) GID 1 SID 100000596 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(182) GID 1 SID 100000597 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(183) GID 1 SID 100000598 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(184) GID 1 SID 100000599 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(185) GID 1 SID 100000600 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(186) GID 1 SID 100000601 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(187) GID 1 SID 100000602 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(188) GID 1 SID 100000603 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(189) GID 1 SID 100000604 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(190) GID 1 SID 100000605 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(191) GID 1 SID 100000606 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(192) GID 1 SID 100000607 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(193) GID 1 SID 100000608 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(194) GID 1 SID 100000609 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(195) GID 1 SID 100000610 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(196) GID 1 SID 100000611 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(197) GID 1 SID 100000612 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(198) GID 1 SID 100000613 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(199) GID 1 SID 100000614 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(200) GID 1 SID 100000615 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(201) GID 1 SID 100000616 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(202) GID 1 SID 100000617 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(203) GID 1 SID 100000618 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(204) GID 1 SID 100000619 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(205) GID 1 SID 100000620 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(206) GID 1 SID 100000621 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(207) GID 1 SID 100000622 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(208) GID 1 SID 100000623 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(209) GID 1 SID 100000624 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(210) GID 1 SID 100000625 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(211) GID 1 SID 100000626 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(212) GID 1 SID 100000627 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(213) GID 1 SID 100000628 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(214) GID 1 SID 100000629 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(215) GID 1 SID 100000630 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(216) GID 1 SID 100000631 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(217) GID 1 SID 100000632 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(218) GID 1 SID 100000633 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(219) GID 1 SID 100000634 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(220) GID 1 SID 100000635 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(221) GID 1 SID 100000636 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(222) GID 1 SID 100000637 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(223) GID 1 SID 100000638 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(224) GID 1 SID 100000639 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(225) GID 1 SID 100000640 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(226) GID 1 SID 100000641 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(227) GID 1 SID 100000642 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(228) GID 1 SID 100000643 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(229) GID 1 SID 100000644 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(230) GID 1 SID 100000645 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(231) GID 1 SID 100000646 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(232) GID 1 SID 100000647 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(233) GID 1 SID 100000648 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(234) GID 1 SID 100000649 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(235) GID 1 SID 100000650 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(236) GID 1 SID 100000651 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(237) GID 1 SID 100000652 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(238) GID 1 SID 100000653 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(239) GID 1 SID 100000654 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(240) GID 1 SID 100000655 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(241) GID 1 SID 100000656 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(242) GID 1 SID 100000657 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(243) GID 1 SID 100000658 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(244) GID 1 SID 100000659 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(245) GID 1 SID 100000660 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(246) GID 1 SID 100000661 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(247) GID 1 SID 100000662 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(248) GID 1 SID 100000663 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(249) GID 1 SID 100000664 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(250) GID 1 SID 100000665 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(251) GID 1 SID 100000666 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(252) GID 1 SID 100000667 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(253) GID 1 SID 100000668 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(254) GID 1 SID 100000669 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(255) GID 1 SID 100000670 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(256) GID 1 SID 100000671 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(257) GID 1 SID 100000672 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(258) GID 1 SID 100000673 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(259) GID 1 SID 100000674 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(260) GID 1 SID 100000675 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(261) GID 1 SID 100000676 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(262) GID 1 SID 100000677 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(263) GID 1 SID 100000678 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(264) GID 1 SID 100000679 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(265) GID 1 SID 100000680 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(266) GID 1 SID 100000681 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(267) GID 1 SID 100000682 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(268) GID 1 SID 100000683 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(270) GID 1 SID 100000703 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(271) GID 1 SID 100000704 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(272) GID 1 SID 100000705 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(273) GID 1 SID 100000706 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(274) GID 1 SID 100000707 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(275) GID 1 SID 100000708 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(276) GID 1 SID 100000709 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(277) GID 1 SID 100000710 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(278) GID 1 SID 100000711 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(279) GID 1 SID 100000712 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(280) GID 1 SID 100000713 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(281) GID 1 SID 100000714 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(282) GID 1 SID 100000715 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(283) GID 1 SID 100000716 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(284) GID 1 SID 100000717 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(285) GID 1 SID 100000718 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(286) GID 1 SID 100000719 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(287) GID 1 SID 100000720 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(288) GID 1 SID 100000721 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(289) GID 1 SID 100000722 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(290) GID 1 SID 100000723 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(291) GID 1 SID 100000724 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(292) GID 1 SID 100000725 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(293) GID 1 SID 100000726 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(294) GID 1 SID 100000727 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(295) GID 1 SID 100000728 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(296) GID 1 SID 100000729 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(297) GID 1 SID 100000730 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(298) GID 1 SID 100000731 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(299) GID 1 SID 100000732 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(300) GID 1 SID 100000733 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(301) GID 1 SID 100000734 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(302) GID 1 SID 100000735 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(303) GID 1 SID 100000736 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(304) GID 1 SID 100000737 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(305) GID 1 SID 100000738 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(306) GID 1 SID 100000739 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(307) GID 1 SID 100000740 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(308) GID 1 SID 100000741 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(309) GID 1 SID 100000742 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(310) GID 1 SID 100000743 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(311) GID 1 SID 100000744 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(312) GID 1 SID 100000745 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(313) GID 1 SID 100000746 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(314) GID 1 SID 100000747 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(315) GID 1 SID 100000748 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(316) GID 1 SID 100000749 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(317) GID 1 SID 100000750 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(318) GID 1 SID 100000751 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(319) GID 1 SID 100000752 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(320) GID 1 SID 100000753 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(321) GID 1 SID 100000754 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(322) GID 1 SID 100000755 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(323) GID 1 SID 100000756 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(324) GID 1 SID 100000757 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(325) GID 1 SID 100000758 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(326) GID 1 SID 100000759 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(327) GID 1 SID 100000760 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(328) GID 1 SID 100000761 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(329) GID 1 SID 100000762 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(330) GID 1 SID 100000763 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(331) GID 1 SID 100000764 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(332) GID 1 SID 100000765 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(333) GID 1 SID 100000766 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(334) GID 1 SID 100000767 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(335) GID 1 SID 100000768 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(336) GID 1 SID 100000769 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(337) GID 1 SID 100000770 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(338) GID 1 SID 100000771 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(339) GID 1 SID 100000772 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(340) GID 1 SID 100000773 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(341) GID 1 SID 100000774 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(342) GID 1 SID 100000775 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(343) GID 1 SID 100000776 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(344) GID 1 SID 100000777 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(345) GID 1 SID 100000778 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(346) GID 1 SID 100000779 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(347) GID 1 SID 100000780 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(348) GID 1 SID 100000781 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(349) GID 1 SID 100000782 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(350) GID 1 SID 100000783 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(351) GID 1 SID 100000784 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(352) GID 1 SID 100000785 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(353) GID 1 SID 100000786 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(354) GID 1 SID 100000787 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(355) GID 1 SID 100000788 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(356) GID 1 SID 100000789 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(357) GID 1 SID 100000790 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(358) GID 1 SID 100000791 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(359) GID 1 SID 100000792 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(360) GID 1 SID 100000793 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(361) GID 1 SID 100000794 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(362) GID 1 SID 100000795 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(363) GID 1 SID 100000796 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(364) GID 1 SID 100000797 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(365) GID 1 SID 100000798 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(366) GID 1 SID 100000799 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(367) GID 1 SID 100000800 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(368) GID 1 SID 100000801 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(369) GID 1 SID 100000802 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(370) GID 1 SID 100000803 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(371) GID 1 SID 100000804 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(372) GID 1 SID 100000805 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(373) GID 1 SID 100000806 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(374) GID 1 SID 100000807 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(375) GID 1 SID 100000808 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(376) GID 1 SID 100000809 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(377) GID 1 SID 100000810 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(378) GID 1 SID 100000811 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(379) GID 1 SID 100000812 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(380) GID 1 SID 100000813 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(381) GID 1 SID 100000814 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(382) GID 1 SID 100000815 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(383) GID 1 SID 100000816 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(384) GID 1 SID 100000817 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(385) GID 1 SID 100000818 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(386) GID 1 SID 100000820 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(387) GID 1 SID 100000821 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(388) GID 1 SID 100000822 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(389) GID 1 SID 100000823 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(390) GID 1 SID 100000824 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(391) GID 1 SID 100000825 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(392) GID 1 SID 100000826 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(393) GID 1 SID 100000827 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(394) GID 1 SID 100000828 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(395) GID 1 SID 100000829 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(396) GID 1 SID 100000830 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(397) GID 1 SID 100000831 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(398) GID 1 SID 100000832 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(399) GID 1 SID 100000833 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(400) GID 1 SID 100000834 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(401) GID 1 SID 100000835 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(402) GID 1 SID 100000836 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(403) GID 1 SID 100000837 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(404) GID 1 SID 100000838 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(405) GID 1 SID 100000839 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(406) GID 1 SID 100000840 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(407) GID 1 SID 100000841 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(408) GID 1 SID 100000842 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(409) GID 1 SID 100000843 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(410) GID 1 SID 100000844 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(411) GID 1 SID 100000845 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(412) GID 1 SID 100000846 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(413) GID 1 SID 100000847 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(414) GID 1 SID 100000849 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(415) GID 1 SID 100000850 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(416) GID 1 SID 100000851 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(417) GID 1 SID 100000852 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(418) GID 1 SID 100000853 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(419) GID 1 SID 100000854 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(420) GID 1 SID 100000855 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(421) GID 1 SID 100000856 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(422) GID 1 SID 100000857 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(423) GID 1 SID 100000858 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(424) GID 1 SID 100000859 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(425) GID 1 SID 100000860 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(426) GID 1 SID 100000861 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(427) GID 1 SID 100000862 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(428) GID 1 SID 100000863 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(431) GID 1 SID 100000865 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(432) GID 1 SID 100000866 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(433) GID 1 SID 100000867 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(434) GID 1 SID 100000868 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(435) GID 1 SID 100000869 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(436) GID 1 SID 100000870 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(437) GID 1 SID 100000871 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(438) GID 1 SID 100000872 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(439) GID 1 SID 100000873 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(441) GID 1 SID 100000882 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(443) GID 1 SID 100000883 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(444) GID 1 SID 100000884 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(445) GID 1 SID 100000885 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(446) GID 1 SID 100000886 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(447) GID 1 SID 100000887 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(448) GID 1 SID 100000888 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(449) GID 1 SID 100000889 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(450) GID 1 SID 100000906 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(451) GID 1 SID 100000907 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(452) GID 1 SID 100000908 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(453) GID 1 SID 100000909 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(454) GID 1 SID 100000910 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(455) GID 1 SID 100000911 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(456) GID 1 SID 100000912 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(457) GID 1 SID 100000913 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(458) GID 1 SID 100000914 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(459) GID 1 SID 100000915 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(460) GID 1 SID 100000916 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(461) GID 1 SID 100000917 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(462) GID 1 SID 100000918 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(463) GID 1 SID 100000919 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(464) GID 1 SID 100000920 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(465) GID 1 SID 100000921 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(466) GID 1 SID 100000922 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(467) GID 1 SID 100000925 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(468) GID 1 SID 100000926 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(469) GID 1 SID 100000929 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(470) GID 1 SID 100000930 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(471) GID 1 SID 100000931 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(472) GID 1 SID 100000932 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(473) GID 1 SID 100000933 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(474) GID 1 SID 100000934 in rule duplicates previous rule. Ignoring old rule.

4151 Snort rules read
    3477 detection rules
    0 decoder rules
    0 preprocessor rules
3477 Option Chains linked into 271 Chain Headers
0 Dynamic rules
+++++++++++++++++++++++++++++++++++++++++++++++++++

+-------------------[Rule Port Counts]---------------------------------------
|             tcp     udp    icmp      ip
|     src     151      18       0       0
|     dst    3306     126       0       0
|     any     383      48     146      22
|      nc      27       8      95      20
|     s+d      12       5       0       0
+----------------------------------------------------------------------------

+-----------------------[detection-filter-config]------------------------------
| memory-cap : 1048576 bytes
+-----------------------[detection-filter-rules]-------------------------------
| none
-------------------------------------------------------------------------------

+-----------------------[rate-filter-config]-----------------------------------
| memory-cap : 1048576 bytes
+-----------------------[rate-filter-rules]------------------------------------
| none
-------------------------------------------------------------------------------

+-----------------------[event-filter-config]----------------------------------
| memory-cap : 1048576 bytes
+-----------------------[event-filter-global]----------------------------------
| none
+-----------------------[event-filter-local]-----------------------------------
| gen-id=1      sig-id=2495       type=Both      tracking=dst count=20  seconds=60 
| gen-id=1      sig-id=1991       type=Limit     tracking=src count=1   seconds=60 
| gen-id=1      sig-id=2923       type=Threshold tracking=dst count=10  seconds=60 
| gen-id=1      sig-id=2924       type=Threshold tracking=dst count=10  seconds=60 
| gen-id=1      sig-id=2275       type=Threshold tracking=dst count=5   seconds=60 
| gen-id=1      sig-id=2496       type=Both      tracking=dst count=20  seconds=60 
| gen-id=1      sig-id=3152       type=Threshold tracking=src count=5   seconds=2  
| gen-id=1      sig-id=2494       type=Both      tracking=dst count=20  seconds=60 
| gen-id=1      sig-id=3273       type=Threshold tracking=src count=5   seconds=2  
| gen-id=1      sig-id=2523       type=Both      tracking=dst count=10  seconds=10 
+-----------------------[suppression]------------------------------------------
| none
-------------------------------------------------------------------------------
Rule application order: activation->dynamic->pass->drop->sdrop->reject->alert->log
Verifying Preprocessor Configurations!
WARNING: flowbits key 'smb.tree.create.llsrpc' is set but not ever checked.
WARNING: flowbits key 'ms_sql_seen_dns' is checked but not ever set.
33 out of 1024 flowbits in use.

[ Port Based Pattern Matching Memory ]
+- [ Aho-Corasick Summary ] -------------------------------------
| Storage Format    : Full-Q 
| Finite Automaton  : DFA
| Alphabet Size     : 256 Chars
| Sizeof State      : Variable (1,2,4 bytes)
| Instances         : 215
|     1 byte states : 204
|     2 byte states : 11
|     4 byte states : 0
| Characters        : 64982
| States            : 32135
| Transitions       : 872051
| State Density     : 10.6%
| Patterns          : 5055
| Match States      : 3855
| Memory (MB)       : 17.00
|   Patterns        : 0.51
|   Match Lists     : 1.02
|   DFA
|     1 byte states : 1.02
|     2 byte states : 14.05
|     4 byte states : 0.00
+----------------------------------------------------------------
[ Number of patterns truncated to 20 bytes: 1039 ]

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

           Rules Engine: SF_SNORT_DETECTION_ENGINE  Version 2.4  <Build 1>
           Preprocessor Object: SF_POP  Version 1.0  <Build 1>
           Preprocessor Object: SF_SSH  Version 1.1  <Build 3>
           Preprocessor Object: SF_DNP3  Version 1.1  <Build 1>
           Preprocessor Object: SF_DNS  Version 1.1  <Build 4>
           Preprocessor Object: SF_GTP  Version 1.1  <Build 1>
           Preprocessor Object: SF_MODBUS  Version 1.1  <Build 1>
           Preprocessor Object: SF_SDF  Version 1.1  <Build 1>
           Preprocessor Object: SF_DCERPC2  Version 1.0  <Build 3>
           Preprocessor Object: SF_FTPTELNET  Version 1.2  <Build 13>
           Preprocessor Object: SF_REPUTATION  Version 1.1  <Build 1>
           Preprocessor Object: SF_SMTP  Version 1.1  <Build 9>
           Preprocessor Object: SF_IMAP  Version 1.0  <Build 1>
           Preprocessor Object: SF_SIP  Version 1.1  <Build 1>
           Preprocessor Object: SF_SSLPP  Version 1.1  <Build 4>

Snort successfully validated the configuration!
Snort exiting
```
*4151*
Test the current instance with "/etc/snort/snortv2.conf" file and check how many rules are loaded with the current build.
```text
ubuntu@ip-10-10-228-159:~/Desktop/Task-Exercises$ sudo snort -c /etc/snort/snortv2.conf -T
Running in Test mode

        --== Initializing Snort ==--
Initializing Output Plugins!
Initializing Preprocessors!
Initializing Plug-ins!
Parsing Rules file "/etc/snort/snortv2.conf"
PortVar 'HTTP_PORTS' defined :  [ 80:81 311 383 591 593 901 1220 1414 1741 1830 2301 2381 2809 3037 3128 3702 4343 4848 5250 6988 7000:7001 7144:7145 7510 7777 7779 8000 8008 8014 8028 8080 8085 8088 8090 8118 8123 8180:8181 8243 8280 8300 8800 8888 8899 9000 9060 9080 9090:9091 9443 9999 11371 34443:34444 41080 50002 55555 ]
PortVar 'SHELLCODE_PORTS' defined :  [ 0:79 81:65535 ]
PortVar 'ORACLE_PORTS' defined :  [ 1024:65535 ]
PortVar 'SSH_PORTS' defined :  [ 22 ]
PortVar 'FTP_PORTS' defined :  [ 21 2100 3535 ]
PortVar 'SIP_PORTS' defined :  [ 5060:5061 5600 ]
PortVar 'FILE_DATA_PORTS' defined :  [ 80:81 110 143 311 383 591 593 901 1220 1414 1741 1830 2301 2381 2809 3037 3128 3702 4343 4848 5250 6988 7000:7001 7144:7145 7510 7777 7779 8000 8008 8014 8028 8080 8085 8088 8090 8118 8123 8180:8181 8243 8280 8300 8800 8888 8899 9000 9060 9080 9090:9091 9443 9999 11371 34443:34444 41080 50002 55555 ]
PortVar 'GTP_PORTS' defined :  [ 2123 2152 3386 ]
Detection:
   Search-Method = AC-Full-Q
    Split Any/Any group = enabled
    Search-Method-Optimizations = enabled
    Maximum pattern length = 20
Tagged Packet Limit: 256
Loading dynamic engine /usr/lib/snort_dynamicengine/libsf_engine.so... done
Loading all dynamic detection libs from /usr/lib/snort_dynamicrules...
WARNING: No dynamic libraries found in directory /usr/lib/snort_dynamicrules.
  Finished Loading all dynamic detection libs from /usr/lib/snort_dynamicrules
Loading all dynamic preprocessor libs from /usr/lib/snort_dynamicpreprocessor/...
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_ssl_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_sip_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_imap_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_smtp_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_reputation_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_ftptelnet_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_dce2_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_sdf_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_modbus_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_gtp_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_dns_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_dnp3_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_ssh_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_pop_preproc.so... done
  Finished Loading all dynamic preprocessor libs from /usr/lib/snort_dynamicpreprocessor/
Log directory = /var/log/snort
WARNING: ip4 normalizations disabled because not inline.
WARNING: tcp normalizations disabled because not inline.
WARNING: icmp4 normalizations disabled because not inline.
WARNING: ip6 normalizations disabled because not inline.
WARNING: icmp6 normalizations disabled because not inline.
Frag3 global config:
    Max frags: 65536
    Fragment memory cap: 4194304 bytes
Frag3 engine config:
    Bound Address: default
    Target-based policy: WINDOWS
    Fragment timeout: 180 seconds
    Fragment min_ttl:   1
    Fragment Anomalies: Alert
    Overlap Limit:     10
    Min fragment Length:     100
      Max Expected Streams: 768
Stream global config:
    Track TCP sessions: ACTIVE
    Max TCP sessions: 262144
    TCP cache pruning timeout: 30 seconds
    TCP cache nominal timeout: 3600 seconds
    Memcap (for reassembly packet storage): 8388608
    Track UDP sessions: ACTIVE
    Max UDP sessions: 131072
    UDP cache pruning timeout: 30 seconds
    UDP cache nominal timeout: 180 seconds
    Track ICMP sessions: INACTIVE
    Track IP sessions: INACTIVE
    Log info if session memory consumption exceeds 1048576
    Send up to 2 active responses
    Wait at least 5 seconds between responses
    Protocol Aware Flushing: ACTIVE
        Maximum Flush Point: 16000
Stream TCP Policy config:
    Bound Address: default
    Reassembly Policy: WINDOWS
    Timeout: 180 seconds
    Limit on TCP Overlaps: 10
    Maximum number of bytes to queue per session: 1048576
    Maximum number of segs to queue per session: 2621
    Options:
        Require 3-Way Handshake: YES
        3-Way Handshake Timeout: 180
        Detect Anomalies: YES
    Reassembly Ports:
      21 client (Footprint) 
      22 client (Footprint) 
      23 client (Footprint) 
      25 client (Footprint) 
      42 client (Footprint) 
      53 client (Footprint) 
      79 client (Footprint) 
      80 client (Footprint) server (Footprint)
      81 client (Footprint) server (Footprint)
      109 client (Footprint) 
      110 client (Footprint) 
      111 client (Footprint) 
      113 client (Footprint) 
      119 client (Footprint) 
      135 client (Footprint) 
      136 client (Footprint) 
      137 client (Footprint) 
      139 client (Footprint) 
      143 client (Footprint) 
      161 client (Footprint) 
      additional ports configured but not printed.
Stream UDP Policy config:
    Timeout: 180 seconds
HttpInspect Config:
    GLOBAL CONFIG
      Detect Proxy Usage:       NO
      IIS Unicode Map Filename: /etc/snort/unicode.map
      IIS Unicode Map Codepage: 1252
      Memcap used for logging URI and Hostname: 150994944
      Max Gzip Memory: 104857600
      Max Gzip Sessions: 201649
      Gzip Compress Depth: 65535
      Gzip Decompress Depth: 65535
    DEFAULT SERVER CONFIG:
      Server profile: All
      Ports (PAF): 80 81 311 383 591 593 901 1220 1414 1741 1830 2301 2381 2809 3037 3128 3702 4343 4848 5250 6988 7000 7001 7144 7145 7510 7777 7779 8000 8008 8014 8028 8080 8085 8088 8090 8118 8123 8180 8181 8243 8280 8300 8800 8888 8899 9000 9060 9080 9090 9091 9443 9999 11371 34443 34444 41080 50002 55555 
      Server Flow Depth: 0
      Client Flow Depth: 0
      Max Chunk Length: 500000
      Small Chunk Length Evasion: chunk size <= 10, threshold >= 5 times
      Max Header Field Length: 750
      Max Number Header Fields: 100
      Max Number of WhiteSpaces allowed with header folding: 200
      Inspect Pipeline Requests: YES
      URI Discovery Strict Mode: NO
      Allow Proxy Usage: NO
      Disable Alerting: NO
      Oversize Dir Length: 500
      Only inspect URI: NO
      Normalize HTTP Headers: NO
      Inspect HTTP Cookies: YES
      Inspect HTTP Responses: YES
      Extract Gzip from responses: YES
      Decompress response files:   
      Unlimited decompression of gzip data from responses: YES
      Normalize Javascripts in HTTP Responses: YES
      Max Number of WhiteSpaces allowed with Javascript Obfuscation in HTTP responses: 200
      Normalize HTTP Cookies: NO
      Enable XFF and True Client IP: NO
      Log HTTP URI data: NO
      Log HTTP Hostname data: NO
      Extended ASCII code support in URI: NO
      Ascii: YES alert: NO
      Double Decoding: YES alert: NO
      %U Encoding: YES alert: YES
      Bare Byte: YES alert: NO
      UTF 8: YES alert: NO
      IIS Unicode: YES alert: NO
      Multiple Slash: YES alert: NO
      IIS Backslash: YES alert: NO
      Directory Traversal: YES alert: NO
      Web Root Traversal: YES alert: NO
      Apache WhiteSpace: YES alert: NO
      IIS Delimiter: YES alert: NO
      IIS Unicode Map: GLOBAL IIS UNICODE MAP CONFIG
      Non-RFC Compliant Characters: 0x00 0x01 0x02 0x03 0x04 0x05 0x06 0x07 
      Whitespace Characters: 0x09 0x0b 0x0c 0x0d 
rpc_decode arguments:
    Ports to decode RPC on: 111 32770 32771 32772 32773 32774 32775 32776 32777 32778 32779 
    alert_fragments: INACTIVE
    alert_large_fragments: INACTIVE
    alert_incomplete: INACTIVE
    alert_multiple_requests: INACTIVE
FTPTelnet Config:
    GLOBAL CONFIG
      Inspection Type: stateful
      Check for Encrypted Traffic: YES alert: NO
      Continue to check encrypted data: YES
    TELNET CONFIG:
      Ports: 23 
      Are You There Threshold: 20
      Normalize: YES
      Detect Anomalies: YES
    FTP CONFIG:
      FTP Server: default
        Ports (PAF): 21 2100 3535 
        Check for Telnet Cmds: YES alert: YES
        Ignore Telnet Cmd Operations: YES alert: YES
        Ignore open data channels: NO
      FTP Client: default
        Check for Bounce Attacks: YES alert: YES
        Check for Telnet Cmds: YES alert: YES
        Ignore Telnet Cmd Operations: YES alert: YES
        Max Response Length: 256
SMTP Config:
    Ports: 25 465 587 691 
    Inspection Type: Stateful
    Normalize: ATRN AUTH BDAT DATA DEBUG EHLO EMAL ESAM ESND ESOM ETRN EVFY EXPN HELO HELP IDENT MAIL NOOP ONEX QUEU QUIT RCPT RSET SAML SEND STARTTLS SOML TICK TIME TURN TURNME VERB VRFY X-EXPS XADR XAUTH XCIR XEXCH50 XGEN XLICENSE X-LINK2STATE XQUE XSTA XTRN XUSR CHUNKING X-ADAT X-DRCP X-ERCP X-EXCH50 
    Ignore Data: No
    Ignore TLS Data: No
    Ignore SMTP Alerts: No
    Max Command Line Length: 512
    Max Specific Command Line Length: 
       ATRN:255 AUTH:246 BDAT:255 DATA:246 DEBUG:255 
       EHLO:500 EMAL:255 ESAM:255 ESND:255 ESOM:255 
       ETRN:246 EVFY:255 EXPN:255 HELO:500 HELP:500 
       IDENT:255 MAIL:260 NOOP:255 ONEX:246 QUEU:246 
       QUIT:246 RCPT:300 RSET:246 SAML:246 SEND:246 
       SIZE:255 STARTTLS:246 SOML:246 TICK:246 TIME:246 
       TURN:246 TURNME:246 VERB:246 VRFY:255 X-EXPS:246 
       XADR:246 XAUTH:246 XCIR:246 XEXCH50:246 XGEN:246 
       XLICENSE:246 X-LINK2STATE:246 XQUE:246 XSTA:246 XTRN:246 
       XUSR:246 
    Max Header Line Length: 1000
    Max Response Line Length: 512
    X-Link2State Alert: Yes
    Drop on X-Link2State Alert: No
    Alert on commands: None
    Alert on unknown commands: No
    SMTP Memcap: 838860
    MIME Max Mem: 838860
    Base64 Decoding: Enabled
    Base64 Decoding Depth: Unlimited
    Quoted-Printable Decoding: Enabled
    Quoted-Printable Decoding Depth: Unlimited
    Unix-to-Unix Decoding: Enabled
    Unix-to-Unix Decoding Depth: Unlimited
    Non-Encoded MIME attachment Extraction: Enabled
    Non-Encoded MIME attachment Extraction Depth: Unlimited
    Log Attachment filename: Enabled
    Log MAIL FROM Address: Enabled
    Log RCPT TO Addresses: Enabled
    Log Email Headers: Enabled
    Email Hdrs Log Depth: 1464
SSH config: 
    Autodetection: ENABLED
    Challenge-Response Overflow Alert: ENABLED
    SSH1 CRC32 Alert: ENABLED
    Server Version String Overflow Alert: ENABLED
    Protocol Mismatch Alert: ENABLED
    Bad Message Direction Alert: DISABLED
    Bad Payload Size Alert: DISABLED
    Unrecognized Version Alert: DISABLED
    Max Encrypted Packets: 20  
    Max Server Version String Length: 100  
    MaxClientBytes: 19600 (Default) 
    Ports:
	22
DCE/RPC 2 Preprocessor Configuration
  Global Configuration
    DCE/RPC Defragmentation: Enabled
    Memcap: 102400 KB
    Events: co 
    SMB Fingerprint policy: Disabled
  Server Default Configuration
    Policy: WinXP
    Detect ports (PAF)
      SMB: 139 445 
      TCP: 135 
      UDP: 135 
      RPC over HTTP server: 593 
      RPC over HTTP proxy: None
    Autodetect ports (PAF)
      SMB: None
      TCP: 1025-65535 
      UDP: 1025-65535 
      RPC over HTTP server: 1025-65535 
      RPC over HTTP proxy: None
    Invalid SMB shares: C$ D$ ADMIN$ 
    Maximum SMB command chaining: 3 commands
    SMB file inspection: Disabled
DNS config: 
    DNS Client rdata txt Overflow Alert: ACTIVE
    Obsolete DNS RR Types Alert: INACTIVE
    Experimental DNS RR Types Alert: INACTIVE
    Ports: 53
SSLPP config:
    Encrypted packets: not inspected
    Ports:
      443      465      563      636      989
      992      993      994      995     7801
     7802     7900     7901     7902     7903
     7904     7905     7906     7907     7908
     7909     7910     7911     7912     7913
     7914     7915     7916     7917     7918
     7919     7920
    Server side data is trusted
    Maximum SSL Heartbeat length: 0
Sensitive Data preprocessor config: 
    Global Alert Threshold: 25
    Masked Output: DISABLED
SIP config: 
    Max number of sessions: 40000  
    Max number of dialogs in a session: 4 (Default) 
    Status: ENABLED
    Ignore media channel: DISABLED
    Max URI length: 512  
    Max Call ID length: 80  
    Max Request name length: 20 (Default) 
    Max From length: 256 (Default) 
    Max To length: 256 (Default) 
    Max Via length: 1024 (Default) 
    Max Contact length: 512  
    Max Content length: 2048  
    Ports:
	5060	5061	5600
    Methods:
	  invite cancel ack bye register options refer subscribe update join info message notify benotify do qauth sprack publish service unsubscribe prack
IMAP Config:
    Ports: 143 
    IMAP Memcap: 838860
    MIME Max Mem: 838860
    Base64 Decoding: Enabled
    Base64 Decoding Depth: Unlimited
    Quoted-Printable Decoding: Enabled
    Quoted-Printable Decoding Depth: Unlimited
    Unix-to-Unix Decoding: Enabled
    Unix-to-Unix Decoding Depth: Unlimited
    Non-Encoded MIME attachment Extraction: Enabled
    Non-Encoded MIME attachment Extraction Depth: Unlimited
POP Config:
    Ports: 110 
    POP Memcap: 838860
    MIME Max Mem: 838860
    Base64 Decoding: Enabled
    Base64 Decoding Depth: Unlimited
    Quoted-Printable Decoding: Enabled
    Quoted-Printable Decoding Depth: Unlimited
    Unix-to-Unix Decoding: Enabled
    Unix-to-Unix Decoding Depth: Unlimited
    Non-Encoded MIME attachment Extraction: Enabled
    Non-Encoded MIME attachment Extraction Depth: Unlimited
Modbus config: 
    Ports:
	502
DNP3 config: 
    Memcap: 262144
    Check Link-Layer CRCs: ENABLED
    Ports:
	20000

+++++++++++++++++++++++++++++++++++++++++++++++++++
Initializing rule chains...
1 Snort rules read
    1 detection rules
    0 decoder rules
    0 preprocessor rules
1 Option Chains linked into 1 Chain Headers
0 Dynamic rules
+++++++++++++++++++++++++++++++++++++++++++++++++++

+-------------------[Rule Port Counts]---------------------------------------
|             tcp     udp    icmp      ip
|     src       0       0       0       0
|     dst       0       0       0       0
|     any       0       0       1       0
|      nc       0       0       1       0
|     s+d       0       0       0       0
+----------------------------------------------------------------------------

+-----------------------[detection-filter-config]------------------------------
| memory-cap : 1048576 bytes
+-----------------------[detection-filter-rules]-------------------------------
| none
-------------------------------------------------------------------------------

+-----------------------[rate-filter-config]-----------------------------------
| memory-cap : 1048576 bytes
+-----------------------[rate-filter-rules]------------------------------------
| none
-------------------------------------------------------------------------------

+-----------------------[event-filter-config]----------------------------------
| memory-cap : 1048576 bytes
+-----------------------[event-filter-global]----------------------------------
+-----------------------[event-filter-local]-----------------------------------
| none
+-----------------------[suppression]------------------------------------------
| none
-------------------------------------------------------------------------------
Rule application order: activation->dynamic->pass->drop->sdrop->reject->alert->log
Verifying Preprocessor Configurations!

[ Port Based Pattern Matching Memory ]
[ Number of patterns truncated to 20 bytes: 0 ]

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

           Rules Engine: SF_SNORT_DETECTION_ENGINE  Version 2.4  <Build 1>
           Preprocessor Object: SF_POP  Version 1.0  <Build 1>
           Preprocessor Object: SF_SSH  Version 1.1  <Build 3>
           Preprocessor Object: SF_DNP3  Version 1.1  <Build 1>
           Preprocessor Object: SF_DNS  Version 1.1  <Build 4>
           Preprocessor Object: SF_GTP  Version 1.1  <Build 1>
           Preprocessor Object: SF_MODBUS  Version 1.1  <Build 1>
           Preprocessor Object: SF_SDF  Version 1.1  <Build 1>
           Preprocessor Object: SF_DCERPC2  Version 1.0  <Build 3>
           Preprocessor Object: SF_FTPTELNET  Version 1.2  <Build 13>
           Preprocessor Object: SF_REPUTATION  Version 1.1  <Build 1>
           Preprocessor Object: SF_SMTP  Version 1.1  <Build 9>
           Preprocessor Object: SF_IMAP  Version 1.0  <Build 1>
           Preprocessor Object: SF_SIP  Version 1.1  <Build 1>
           Preprocessor Object: SF_SSLPP  Version 1.1  <Build 4>

Snort successfully validated the configuration!
Snort exiting

uhmm

seems slowly

so try to crack the pass from ubuntu machine to use ssh in my machine

https://thecyphere.com/blog/difference-hashing-encryption-salting/

some differences between encryption and hashing and also why using salt is more secure in hashing :)
```
```text
┌──(kali㉿kali)-[~/snort]
└─$ cat shadow.txt 
root:*:18747:0:99999:7:::
daemon:*:18747:0:99999:7:::
bin:*:18747:0:99999:7:::
sys:*:18747:0:99999:7:::
sync:*:18747:0:99999:7:::
games:*:18747:0:99999:7:::
man:*:18747:0:99999:7:::
lp:*:18747:0:99999:7:::
mail:*:18747:0:99999:7:::
news:*:18747:0:99999:7:::
uucp:*:18747:0:99999:7:::
proxy:*:18747:0:99999:7:::
www-data:*:18747:0:99999:7:::
backup:*:18747:0:99999:7:::
list:*:18747:0:99999:7:::
irc:*:18747:0:99999:7:::
gnats:*:18747:0:99999:7:::
nobody:*:18747:0:99999:7:::
systemd-network:*:18747:0:99999:7:::
systemd-resolve:*:18747:0:99999:7:::
systemd-timesync:*:18747:0:99999:7:::
messagebus:*:18747:0:99999:7:::
syslog:*:18747:0:99999:7:::
_apt:*:18747:0:99999:7:::
tss:*:18747:0:99999:7:::
uuidd:*:18747:0:99999:7:::
tcpdump:*:18747:0:99999:7:::
sshd:*:18747:0:99999:7:::
landscape:*:18747:0:99999:7:::
pollinate:*:18747:0:99999:7:::
ec2-instance-connect:!:18747:0:99999:7:::
systemd-coredump:!!:18820::::::
ubuntu:!$6$vmzKXtCowJO/EvOg$PcukzMtijIm6kj56vz7m33c6KExbF7Horki4oPeujuoVsOsonzlUm/w6e/Enmb.NAcOKVNBkHEC22j.5FyqHu0:19004:0:99999:7:::
lxd:!:18820::::::
lightdm:*:18820:0:99999:7:::
dnsmasq:*:18820:0:99999:7:::
usbmux:*:18820:0:99999:7:::
rtkit:*:18820:0:99999:7:::
avahi:*:18820:0:99999:7:::
cups-pk-helper:*:18820:0:99999:7:::
pulse:*:18820:0:99999:7:::
geoclue:*:18820:0:99999:7:::
saned:*:18820:0:99999:7:::
colord:*:18820:0:99999:7:::
gdm:*:18820:0:99999:7:::
snort:*:19000:0:99999:7:::
```
```text
┌──(kali㉿kali)-[~/snort]
└─$ cat passwd.txt 
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
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
sshd:x:109:65534::/run/sshd:/usr/sbin/nologin
landscape:x:110:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:111:1::/var/cache/pollinate:/bin/false
ec2-instance-connect:x:112:65534::/nonexistent:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
lightdm:x:113:121:Light Display Manager:/var/lib/lightdm:/bin/false
dnsmasq:x:114:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
usbmux:x:115:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
rtkit:x:116:123:RealtimeKit,,,:/proc:/usr/sbin/nologin
avahi:x:117:124:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin
cups-pk-helper:x:118:125:user for cups-pk-helper service,,,:/home/cups-pk-helper:/usr/sbin/nologin
pulse:x:119:126:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin
geoclue:x:120:128::/var/lib/geoclue:/usr/sbin/nologin
saned:x:121:130::/var/lib/saned:/usr/sbin/nologin
colord:x:122:131:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
gdm:x:123:132:Gnome Display Manager:/var/lib/gdm3:/bin/false
snort:x:124:133:Snort IDS:/var/log/snort:/usr/sbin/nologin
```
```text
┌──(kali㉿kali)-[~/snort]
└─$ unshadow passwd.txt shadow.txt > hash.txt
```
```text
┌──(kali㉿kali)-[~/snort]
└─$ cat hash.txt  
root:*:0:0:root:/root:/bin/bash
daemon:*:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:*:2:2:bin:/bin:/usr/sbin/nologin
sys:*:3:3:sys:/dev:/usr/sbin/nologin
sync:*:4:65534:sync:/bin:/bin/sync
games:*:5:60:games:/usr/games:/usr/sbin/nologin
man:*:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:*:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:*:8:8:mail:/var/mail:/usr/sbin/nologin
news:*:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:*:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:*:13:13:proxy:/bin:/usr/sbin/nologin
www-data:*:33:33:www-data:/var/www:/usr/sbin/nologin
backup:*:34:34:backup:/var/backups:/usr/sbin/nologin
list:*:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:*:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:*:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:*:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:*:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:*:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:*:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:*:103:106::/nonexistent:/usr/sbin/nologin
syslog:*:104:110::/home/syslog:/usr/sbin/nologin
_apt:*:105:65534::/nonexistent:/usr/sbin/nologin
tss:*:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:*:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:*:108:113::/nonexistent:/usr/sbin/nologin
sshd:*:109:65534::/run/sshd:/usr/sbin/nologin
landscape:*:110:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:*:111:1::/var/cache/pollinate:/bin/false
ec2-instance-connect:!:112:65534::/nonexistent:/usr/sbin/nologin
systemd-coredump:!!:999:999:systemd Core Dumper:/:/usr/sbin/nologin
ubuntu:!$6$vmzKXtCowJO/EvOg$PcukzMtijIm6kj56vz7m33c6KExbF7Horki4oPeujuoVsOsonzlUm/w6e/Enmb.NAcOKVNBkHEC22j.5FyqHu0:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
lxd:!:998:100::/var/snap/lxd/common/lxd:/bin/false
lightdm:*:113:121:Light Display Manager:/var/lib/lightdm:/bin/false
dnsmasq:*:114:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
usbmux:*:115:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
rtkit:*:116:123:RealtimeKit,,,:/proc:/usr/sbin/nologin
avahi:*:117:124:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin
cups-pk-helper:*:118:125:user for cups-pk-helper service,,,:/home/cups-pk-helper:/usr/sbin/nologin
pulse:*:119:126:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin
geoclue:*:120:128::/var/lib/geoclue:/usr/sbin/nologin
saned:*:121:130::/var/lib/saned:/usr/sbin/nologin
colord:*:122:131:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
gdm:*:123:132:Gnome Display Manager:/var/lib/gdm3:/bin/false
snort:*:124:133:Snort IDS:/var/log/snort:/usr/sbin/nologin

seems salted :(
ubuntu:!$6$vmzKXtCowJO/EvOg$PcukzMtijIm6kj56vz7m33c6KExbF7Horki4oPeujuoVsOsonzlUm/w6e/Enmb.NAcOKVNBkHEC22j.5FyqHu0:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
```

## Exploitation
```text
┌──(kali㉿kali)-[~/snort]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
Using default input encoding: UTF-8
No password hashes loaded (see FAQ)

I see it 

trying to use some pass
```
```text
┌──(kali㉿kali)-[~/snort]
└─$ mkpasswd -m sha-512 Password1234
$6$mcpfTegkq/MgnH/0$iggkC9r7rSqq.tgdwW9akgP14OEi6n1hD9rXDTaXj.mpZBCvpM9Glt1tFn0e.z46hVZp7RZp1/HbBsAscQZRw1

maybe the best way, is just replacing the ubuntu's pass
like this

root@ip-10-10-81-86:/home/ubuntu# cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
witty:x:0:0:witty:/root:/bin/bash
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
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
sshd:x:109:65534::/run/sshd:/usr/sbin/nologin
landscape:x:110:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:111:1::/var/cache/pollinate:/bin/false
ec2-instance-connect:x:112:65534::/nonexistent:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
lightdm:x:113:121:Light Display Manager:/var/lib/lightdm:/bin/false
dnsmasq:x:114:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
usbmux:x:115:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
rtkit:x:116:123:RealtimeKit,,,:/proc:/usr/sbin/nologin
avahi:x:117:124:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin
cups-pk-helper:x:118:125:user for cups-pk-helper service,,,:/home/cups-pk-helper:/usr/sbin/nologin
pulse:x:119:126:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin
geoclue:x:120:128::/var/lib/geoclue:/usr/sbin/nologin
saned:x:121:130::/var/lib/saned:/usr/sbin/nologin
colord:x:122:131:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
gdm:x:123:132:Gnome Display Manager:/var/lib/gdm3:/bin/false
snort:x:124:133:Snort IDS:/var/log/snort:/usr/sbin/nologin

root@ip-10-10-81-86:/home/ubuntu# cat /etc/shadow
root:*:18747:0:99999:7:::
daemon:*:18747:0:99999:7:::
bin:*:18747:0:99999:7:::
sys:*:18747:0:99999:7:::
sync:*:18747:0:99999:7:::
games:*:18747:0:99999:7:::
man:*:18747:0:99999:7:::
lp:*:18747:0:99999:7:::
mail:*:18747:0:99999:7:::
news:*:18747:0:99999:7:::
uucp:*:18747:0:99999:7:::
proxy:*:18747:0:99999:7:::
www-data:*:18747:0:99999:7:::
backup:*:18747:0:99999:7:::
list:*:18747:0:99999:7:::
irc:*:18747:0:99999:7:::
gnats:*:18747:0:99999:7:::
nobody:*:18747:0:99999:7:::
systemd-network:*:18747:0:99999:7:::
systemd-resolve:*:18747:0:99999:7:::
systemd-timesync:*:18747:0:99999:7:::
messagebus:*:18747:0:99999:7:::
syslog:*:18747:0:99999:7:::
_apt:*:18747:0:99999:7:::
tss:*:18747:0:99999:7:::
uuidd:*:18747:0:99999:7:::
tcpdump:*:18747:0:99999:7:::
sshd:*:18747:0:99999:7:::
landscape:*:18747:0:99999:7:::
pollinate:*:18747:0:99999:7:::
ec2-instance-connect:!:18747:0:99999:7:::
systemd-coredump:!!:18820::::::
ubuntu:$6$mcpfTegkq/MgnH/0$iggkC9r7rSqq.tgdwW9akgP14OEi6n1hD9rXDTaXj.mpZBCvpM9Glt1tFn0e.z46hVZp7RZp1/HbBsAscQZRw1:19004:0:99999:7:::
witty:$6$mcpfTegkq/MgnH/0$iggkC9r7rSqq.tgdwW9akgP14OEi6n1hD9rXDTaXj.mpZBCvpM9Glt1tFn0e.z46hVZp7RZp1/HbBsAscQZRw1:18747:0:99999:7:::
lxd:!:18820::::::
lightdm:*:18820:0:99999:7:::
dnsmasq:*:18820:0:99999:7:::
usbmux:*:18820:0:99999:7:::
rtkit:*:18820:0:99999:7:::
avahi:*:18820:0:99999:7:::
cups-pk-helper:*:18820:0:99999:7:::
pulse:*:18820:0:99999:7:::
geoclue:*:18820:0:99999:7:::
saned:*:18820:0:99999:7:::
colord:*:18820:0:99999:7:::
gdm:*:18820:0:99999:7:::
snort:*:19000:0:99999:7:::
```
```text
┌──(kali㉿kali)-[~/snort]
└─$ ssh ubuntu@10.10.81.86
ubuntu@10.10.81.86's password:  Password1234
Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.8.0-1038-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Mon Dec  5 18:48:43 UTC 2022

  System load:  0.16               Processes:             222
  Usage of /:   10.1% of 43.56GB   Users logged in:       0
  Memory usage: 18%                IPv4 address for eth0: 10.10.81.86
  Swap usage:   0%                 IPv4 address for eth1: 10.234.0.1

210 updates can be applied immediately.
104 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

The list of available updates is more than a week old.
To check for new updates run: sudo apt update

/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
/bin/bash: warning: shell level (1000) too high, resetting to 1
sudo su
su witty
^Cubuntu@ip-10-10-81-86:~$ whoami
ubuntu
ubuntu@ip-10-10-81-86:~$ sudo su
root@ip-10-10-81-86:/home/ubuntu# :)
```
![[Pasted image 20221205133312.png]]
![[Pasted image 20221205133327.png]]
*1*
### Operation Mode 1: Sniffer Mode
Let's run Snort in Sniffer Mode
Like tcpdump, Snort has various flags capable of viewing various data about the packet it is ingesting.
Sniffer mode parameters are explained in the table below;
Parameter	Description
-v	Verbose. Display the TCP/IP output in the console.
-d	Display the packet data (payload).
-e	Display the link-layer (TCP/IP/UDP/ICMP) headers.
-X	Display the full packet details in HEX.
-i	This parameter helps to define a specific network interface to listen/sniff. Once you have multiple interfaces, you can choose a specific interface to sniff.
Let's start using each parameter and see the difference between them. Snort needs active traffic on your interface, so we need to generate traffic to see Snort in action.
To do this, use the traffic-generator script (find this in the Task-Exercise folder)
Sniffing with parameter "-i"
Start the Snort instance in verbose mode (-v) and use the interface (-i) "eth0"; sudo snort -v-i eth0
In case you have only one interface, Snort uses it by default. The above example demonstrates to sniff on the interface named "eth0". Once you simulate the parameter -v, you will notice it will automatically use the "eth0" interface and prompt it.
Sniffing with parameter "-v"
Start the Snort instance in verbose mode (-v); sudo snort -v
Now run the traffic-generator script as sudo and start ICMP/HTTP traffic. Once the traffic is generated, snort will start showing the  packets in verbosity mode as follows;
```text
sniffing with -v

           
user@ubuntu$ sudo snort -v
                             
Running in packet dump mode

        --== Initializing Snort ==--
...
Commencing packet processing (pid=64)
12/01-20:10:13.846653 192.168.175.129:34316 -> 192.168.175.2:53
UDP TTL:64 TOS:0x0 ID:23826 IpLen:20 DgmLen:64 DF
Len: 36
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/01-20:10:13.846794 192.168.175.129:38655 -> 192.168.175.2:53
UDP TTL:64 TOS:0x0 ID:23827 IpLen:20 DgmLen:64 DF
Len: 36
===============================================================================
Snort exiting
```
As you can see in the given output, verbosity mode provides tcpdump like output information. Once we interrupt the sniffing with CTRL+C, it stops and summarises the sniffed packets.
Sniffing with parameter "-d"
Start the Snort instance in dumping packet data mode (-d); sudo snort -d
Now run the traffic-generator script as sudo and start ICMP/HTTP traffic. Once the traffic is generated, snort will start showing the  packets in verbosity mode as follows;
```text
sniffing with -d

           
user@ubuntu$ sudo snort -d
                             
Running in packet dump mode

        --== Initializing Snort ==--
...
Commencing packet processing (pid=67)

12/01-20:45:42.068675 192.168.175.129:37820 -> 192.168.175.2:53
UDP TTL:64 TOS:0x0 ID:53099 IpLen:20 DgmLen:56 DF
Len: 28
99 A5 01 00 00 01 00 00 00 00 00 00 06 67 6F 6F  .............goo
67 6C 65 03 63 6F 6D 00 00 1C 00 01              gle.com.....

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/01-20:45:42.070742 192.168.175.2:53 -> 192.168.175.129:44947
UDP TTL:128 TOS:0x0 ID:63307 IpLen:20 DgmLen:72
Len: 44
FE 64 81 80 00 01 00 01 00 00 00 00 06 67 6F 6F  .d...........goo
67 6C 65 03 63 6F 6D 00 00 01 00 01 C0 0C 00 01  gle.com.........
00 01 00 00 00 05 00 04 D8 3A CE CE              .........:..

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
```
As you can see in the given output, packet data payload mode covers the verbose mode and provides more data.
Sniffing with parameter "-de"
Start the Snort instance in dump (-d) and link-layer header grabbing (-e) mode; snort -d -e
Now run the traffic-generator script as sudo and start ICMP/HTTP traffic. Once the traffic is generated, snort will start showing the  packets in verbosity mode as follows;
```text
sniffing with -de

           
user@ubuntu$ sudo snort -de
                             
Running in packet dump mode

        --== Initializing Snort ==--
...
Commencing packet processing (pid=70)
12/01-20:55:26.958773 00:0C:29:A5:B7:A2 -> 00:50:56:E1:9B:9D type:0x800 len:0x46
192.168.175.129:47395 -> 192.168.175.2:53 UDP TTL:64 TOS:0x0 ID:64294 IpLen:20 DgmLen:56 DF
Len: 28
6D 9C 01 00 00 01 00 00 00 00 00 00 06 67 6F 6F  m............goo
67 6C 65 03 63 6F 6D 00 00 01 00 01              gle.com.....

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/01-20:55:26.965226 00:50:56:E1:9B:9D -> 00:0C:29:A5:B7:A2 type:0x800 len:0x56
192.168.175.2:53 -> 192.168.175.129:47395 UDP TTL:128 TOS:0x0 ID:63346 IpLen:20 DgmLen:72
Len: 44
6D 9C 81 80 00 01 00 01 00 00 00 00 06 67 6F 6F  m............goo
67 6C 65 03 63 6F 6D 00 00 01 00 01 C0 0C 00 01  gle.com.........
00 01 00 00 00 05 00 04 D8 3A D6 8E              .........:..
```
Sniffing with parameter "-X"
Start the Snort instance in full packet dump mode (-X); sudo snort -X
Now run the traffic-generator script as sudo and start ICMP/HTTP traffic. Once the traffic is generated, snort will start showing the  packets in verbosity mode as follows;
```text
sniffing with -X

           
user@ubuntu$ sudo snort -X
                             
Running in packet dump mode

        --== Initializing Snort ==--
...
Commencing packet processing (pid=76)
WARNING: No preprocessors configured for policy 0.
12/01-21:07:56.806121 192.168.175.1:58626 -> 239.255.255.250:1900
UDP TTL:1 TOS:0x0 ID:48861 IpLen:20 DgmLen:196
Len: 168
0x0000: 01 00 5E 7F FF FA 00 50 56 C0 00 08 08 00 45 00  ..^....PV.....E.
0x0010: 00 C4 BE DD 00 00 01 11 9A A7 C0 A8 AF 01 EF FF  ................
0x0020: FF FA E5 02 07 6C 00 B0 85 AE 4D 2D 53 45 41 52  .....l....M-SEAR
0x0030: 43 48 20 2A 20 48 54 54 50 2F 31 2E 31 0D 0A 48  CH * HTTP/1.1..H
0x0040: 4F 53 54 3A 20 32 33 39 2E 32 35 35 2E 32 35 35  OST: 239.255.255
0x0050: 2E 32 35 30 3A 31 39 30 30 0D 0A 4D 41 4E 3A 20  .250:1900..MAN: 
0x0060: 22 73 73 64 70 3A 64 69 73 63 6F 76 65 72 22 0D  "ssdp:discover".
0x0070: 0A 4D 58 3A 20 31 0D 0A 53 54 3A 20 75 72 6E 3A  .MX: 1..ST: urn:
0x0080: 64 69 61 6C 2D 6D 75 6C 74 69 73 63 72 65 65 6E  dial-multiscreen
0x0090: 2D 6F 72 67 3A 73 65 72 76 69 63 65 3A 64 69 61  -org:service:dia
0x00A0: 6C 3A 31 0D 0A 55 53 45 52 2D 41 47 45 4E 54 3A  l:1..USER-AGENT:
0x00B0: 20 43 68 72 6F 6D 69 75 6D 2F 39 35 2E 30 2E 34   Chromium/95.0.4
0x00C0: 36 33 38 2E 36 39 20 57 69 6E 64 6F 77 73 0D 0A  638.69 Windows..
0x00D0: 0D 0A                                            ..

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/01-21:07:57.624205 216.58.214.142 -> 192.168.175.129
ICMP TTL:128 TOS:0x0 ID:63394 IpLen:20 DgmLen:84
Type:0  Code:0  ID:15  Seq:1  ECHO REPLY
0x0000: 00 0C 29 A5 B7 A2 00 50 56 E1 9B 9D 08 00 45 00  ..)....PV.....E.
0x0010: 00 54 F7 A2 00 00 80 01 24 13 D8 3A D6 8E C0 A8  .T......$..:....
0x0020: AF 81 00 00 BE B6 00 0F 00 01 2D E4 A7 61 00 00  ..........-..a..
0x0030: 00 00 A4 20 09 00 00 00 00 00 10 11 12 13 14 15  ... ............
0x0040: 16 17 18 19 1A 1B 1C 1D 1E 1F 20 21 22 23 24 25  .......... !"#$%
0x0050: 26 27 28 29 2A 2B 2C 2D 2E 2F 30 31 32 33 34 35  &'()*+,-./012345
0x0060: 36 37                                            67

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
```
Note that you can use the parameters both in combined and separated form as follows;
snort -v
snort -vd
snort -de
snort -v -d -e
snort -X
Make sure you understand and practice each parameter with different types of traffic and discover your favourite combination.
You can practice the parameter combinations by using the traffic-generator script.
```text
root@ip-10-10-81-86:/home/ubuntu# ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
root@ip-10-10-81-86:/home/ubuntu# cd Desktop/
root@ip-10-10-81-86:/home/ubuntu/Desktop# ls
Task-Exercises
root@ip-10-10-81-86:/home/ubuntu/Desktop# cd Task-Exercises/
root@ip-10-10-81-86:/home/ubuntu/Desktop/Task-Exercises# ls
Config-Sample  Exercise-Files  traffic-generator.sh
root@ip-10-10-81-86:/home/ubuntu/Desktop/Task-Exercises# ls -lah
total 28K
drwx------ 5 ubuntu ubuntu 4.0K Jan 10  2022 .
drwxr-xr-x 3 ubuntu ubuntu 4.0K Jan 10  2022 ..
-rwxrwxr-x 1 ubuntu ubuntu   30 Dec 25  2021 .easy.sh
drwx------ 2 ubuntu ubuntu 4.0K Jan  6  2022 .traffic-generator-source
drwx------ 2 ubuntu ubuntu 4.0K Jan  6  2022 Config-Sample
drwx------ 7 ubuntu ubuntu 4.0K Feb  4  2022 Exercise-Files
-rwxrwxr-x 1 ubuntu ubuntu 1.7K Jan 10  2022 traffic-generator.sh
root@ip-10-10-81-86:/home/ubuntu/Desktop/Task-Exercises# sudo snort -v -i eth0
Running in packet dump mode

        --== Initializing Snort ==--
Initializing Output Plugins!
pcap DAQ configured to passive.
Acquiring network traffic from "eth0".
Decoding Ethernet

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

Commencing packet processing (pid=21540)
12/05-18:56:26.104591 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25945 IpLen:20 DgmLen:112 DF
***AP*** Seq: 0x60F6CF91  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759855475 925906178 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:56:26.104692 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25946 IpLen:20 DgmLen:136 DF
***AP*** Seq: 0x60F6CFCD  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759855476 925906178 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:56:26.104721 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25947 IpLen:20 DgmLen:284 DF
***AP*** Seq: 0x60F6D021  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759855476 925906178 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:56:26.104754 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25948 IpLen:20 DgmLen:332 DF
***AP*** Seq: 0x60F6D109  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759855476 925906178 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:56:26.104801 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25949 IpLen:20 DgmLen:288 DF
***AP*** Seq: 0x60F6D221  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759855476 925906178 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:26.195377 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32127 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6CF25  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925906356 759855369 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:26.277587 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32128 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6CF91  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925906437 759855450 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:26.300954 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32129 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6CFCD  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925906459 759855475 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:26.300954 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32132 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6D221  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925906459 759855476 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:26.300954 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32130 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6D021  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925906459 759855476 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:26.300954 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32131 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6D109  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925906459 759855476 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:26.300955 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32133 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6D30D  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925906460 759855476 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:56:27.108609 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25950 IpLen:20 DgmLen:456 DF
***AP*** Seq: 0x60F6D30D  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759856480 925906460 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:56:27.108760 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25951 IpLen:20 DgmLen:576 DF
***AP*** Seq: 0x60F6D4A1  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759856480 925906460 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:56:27.108823 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25952 IpLen:20 DgmLen:1376 DF
***AP*** Seq: 0x60F6D6AD  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759856480 925906460 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
12/05-18:56:27.317687 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32134 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6D4A1  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925907469 759856480 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:27.317687 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32135 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6D6AD  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925907470 759856480 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:27.317687 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32136 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6DBA9  Win: 0x1ED  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925907470 759856480 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:27.317688 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32137 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6DBD9  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925907470 759856480 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:27.317688 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32138 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6E0D5  Win: 0x1F4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925907470 759856480 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:27.320394 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32139 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6E38D  Win: 0x1EF  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925907470 759856480 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:56:28.132547 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25956 IpLen:20 DgmLen:320 DF
***AP*** Seq: 0x60F6E38D  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759857503 925907470 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
12/05-18:56:28.132635 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25959 IpLen:20 DgmLen:1248 DF
***AP*** Seq: 0x60F6EBCD  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759857504 925907470 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:28.337540 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32140 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6E499  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925908485 759857503 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:28.337541 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32141 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6E995  Win: 0x1F2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925908485 759857503 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:28.337541 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32142 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6EBCD  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925908485 759857503 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:28.337541 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32143 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6F079  Win: 0x1EE  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925908485 759857504 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:56:29.156504 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25960 IpLen:20 DgmLen:272 DF
***AP*** Seq: 0x60F6F079  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759858527 925908485 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:56:29.156541 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25961 IpLen:20 DgmLen:1048 DF
***AP*** Seq: 0x60F6F155  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759858527 925908485 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:56:29.156627 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25962 IpLen:20 DgmLen:1120 DF
***AP*** Seq: 0x60F6F539  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759858528 925908485 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:29.355104 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32144 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6F155  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925909499 759858527 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:29.359202 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32145 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6F539  Win: 0x1F2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925909499 759858527 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:29.359202 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32146 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6F965  Win: 0x1EA  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925909499 759858528 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:56:30.180496 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25963 IpLen:20 DgmLen:272 DF
***AP*** Seq: 0x60F6F965  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759859551 925909499 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:56:30.180535 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25964 IpLen:20 DgmLen:1128 DF
***AP*** Seq: 0x60F6FA41  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759859551 925909499 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:56:30.180571 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25965 IpLen:20 DgmLen:888 DF
***AP*** Seq: 0x60F6FE75  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759859551 925909499 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:30.376678 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32147 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6FA41  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925910517 759859551 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:30.376740 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32148 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F6FE75  Win: 0x1F2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925910517 759859551 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:30.386991 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32149 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F701B9  Win: 0x1EC  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925910517 759859551 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:56:31.204503 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25966 IpLen:20 DgmLen:200 DF
***AP*** Seq: 0x60F701B9  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759860575 925910517 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:56:31.204542 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25967 IpLen:20 DgmLen:1136 DF
***AP*** Seq: 0x60F7024D  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759860575 925910517 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:56:31.204607 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25968 IpLen:20 DgmLen:944 DF
***AP*** Seq: 0x60F70689  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759860576 925910517 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:31.402681 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32150 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F7024D  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925911534 759860575 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:31.402681 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32151 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F70689  Win: 0x1F2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925911535 759860575 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:31.402681 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32152 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F70A05  Win: 0x1EC  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925911535 759860576 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:56:32.228537 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25969 IpLen:20 DgmLen:152 DF
***AP*** Seq: 0x60F70A05  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759861599 925911535 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
12/05-18:56:32.228611 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25972 IpLen:20 DgmLen:584 DF
***AP*** Seq: 0x60F71045  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759861600 925911535 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:32.451624 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32153 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F70A69  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925912579 759861599 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:32.457123 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32154 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F70F65  Win: 0x1F2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925912580 759861599 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:32.457123 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32155 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F71045  Win: 0x1F2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925912580 759861599 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:32.457124 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32156 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F71259  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925912580 759861600 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:56:33.252536 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25973 IpLen:20 DgmLen:504 DF
***AP*** Seq: 0x60F71259  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759862623 925912580 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
12/05-18:56:33.252613 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25976 IpLen:20 DgmLen:336 DF
***AP*** Seq: 0x60F71A21  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759862624 925912580 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:33.451083 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32157 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F7141D  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925913570 759862623 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:33.451083 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32158 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F71919  Win: 0x1F2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925913570 759862623 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:33.451083 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32159 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F71A21  Win: 0x1F2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925913570 759862623 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:56:33.451112 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32160 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE44A  Ack: 0x60F71B3D  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925913570 759862624 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

^C*** Caught Int-Signal
12/05-18:56:34.276636 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:25977 IpLen:20 DgmLen:1288 DF
***AP*** Seq: 0x60F71B3D  Ack: 0xDE6CE44A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759863648 925913570 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

===============================================================================
Run time for packet processing was 9.227589 seconds
Snort processed 62 packets.
Snort ran for 0 days 0 hours 0 minutes 9 seconds
   Pkts/sec:            6
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      12906496
  Total allocated space (uordblks):      679312
  Total free space (fordblks):           107120
  Topmost releasable block (keepcost):   105344
===============================================================================
Packet I/O Totals:
   Received:           69
   Analyzed:           62 ( 89.855%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            7 ( 10.145%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:           62 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:           62 (100.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:           58 ( 93.548%)
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
   IP4 Disc:            4 (  6.452%)
   IP6 Disc:            0 (  0.000%)
   TCP Disc:            0 (  0.000%)
   UDP Disc:            0 (  0.000%)
  ICMP Disc:            0 (  0.000%)
All Discard:            4 (  6.452%)
      Other:            0 (  0.000%)
Bad Chk Sum:           24 ( 38.710%)
    Bad TTL:            0 (  0.000%)
     S5 G 1:            0 (  0.000%)
     S5 G 2:            0 (  0.000%)
      Total:           62
===============================================================================
Snort exiting

root@ip-10-10-81-86:/home/ubuntu/Desktop/Task-Exercises# sudo snort -v 
Running in packet dump mode

        --== Initializing Snort ==--
Initializing Output Plugins!
pcap DAQ configured to passive.
Acquiring network traffic from "eth0".
Decoding Ethernet

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

Commencing packet processing (pid=21553)
12/05-18:57:56.568622 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26005 IpLen:20 DgmLen:112 DF
***AP*** Seq: 0x60F735ED  Ack: 0xDE6CE6B2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759945940 925996469 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:57:56.568750 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26006 IpLen:20 DgmLen:432 DF
***AP*** Seq: 0x60F73629  Ack: 0xDE6CE6B2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759945940 925996469 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:57:56.568819 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26007 IpLen:20 DgmLen:316 DF
***AP*** Seq: 0x60F737A5  Ack: 0xDE6CE6B2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759945940 925996469 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:57:56.697605 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32202 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE6B2  Ack: 0x60F734F5  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925996671 759945874 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:57:56.731700 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32203 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE6B2  Ack: 0x60F73581  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925996703 759945886 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:57:56.733309 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32204 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE6B2  Ack: 0x60F735ED  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925996703 759945901 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:57:56.767842 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32205 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE6B2  Ack: 0x60F73629  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925996737 759945940 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:57:56.767843 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32207 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE6B2  Ack: 0x60F738AD  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925996737 759945940 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:57:56.767843 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32206 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE6B2  Ack: 0x60F737A5  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925996737 759945940 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:57:57.572685 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26008 IpLen:20 DgmLen:1248 DF
***AP*** Seq: 0x60F738AD  Ack: 0xDE6CE6B2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759946944 925996737 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
12/05-18:57:57.788824 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32208 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE6B2  Ack: 0x60F73D59  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925997730 759946944 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:57:57.788824 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32209 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE6B2  Ack: 0x60F74255  Win: 0x1EE  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925997730 759946944 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:57:57.788824 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32210 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE6B2  Ack: 0x60F74539  Win: 0x1E9  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925997730 759946944 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
12/05-18:57:58.806942 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32211 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE6B2  Ack: 0x60F74A35  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925998761 759947967 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:57:58.806942 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32212 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE6B2  Ack: 0x60F74B35  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925998762 759947967 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:57:59.620539 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26013 IpLen:20 DgmLen:912 DF
***AP*** Seq: 0x60F74B35  Ack: 0xDE6CE6B2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759948991 925998762 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:57:59.818253 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32213 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE6B2  Ack: 0x60F74E91  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 925999761 759948991 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

^C*** Caught Int-Signal
12/05-18:58:00.644522 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26014 IpLen:20 DgmLen:760 DF
***AP*** Seq: 0x60F74E91  Ack: 0xDE6CE6B2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759950015 925999761 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

===============================================================================
Run time for packet processing was 5.131625 seconds
Snort processed 20 packets.
Snort ran for 0 days 0 hours 0 minutes 5 seconds
   Pkts/sec:            4
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      12906496
  Total allocated space (uordblks):      679312
  Total free space (fordblks):           107120
  Topmost releasable block (keepcost):   104480
===============================================================================
Packet I/O Totals:
   Received:           31
   Analyzed:           20 ( 64.516%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:           11 ( 35.484%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:           20 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:           20 (100.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:           18 ( 90.000%)
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
   IP4 Disc:            2 ( 10.000%)
   IP6 Disc:            0 (  0.000%)
   TCP Disc:            0 (  0.000%)
   UDP Disc:            0 (  0.000%)
  ICMP Disc:            0 (  0.000%)
All Discard:            2 ( 10.000%)
      Other:            0 (  0.000%)
Bad Chk Sum:            6 ( 30.000%)
    Bad TTL:            0 (  0.000%)
     S5 G 1:            0 (  0.000%)
     S5 G 2:            0 (  0.000%)
      Total:           20
===============================================================================
Snort exiting

root@ip-10-10-81-86:/home/ubuntu/Desktop/Task-Exercises# sudo snort -d -q
12/05-18:58:26.578143 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32256 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE93A  Ack: 0x60F761D5  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926026347 759975752 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:27.428547 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26039 IpLen:20 DgmLen:400 DF
***AP*** Seq: 0x60F761D5  Ack: 0xDE6CE93A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759976799 926026347 
96 84 96 41 2C E5 FE 0B EC 61 28 73 0C C5 69 F3  ...A,....a(s..i.
BB 18 E6 4A 65 54 93 C7 7C 37 33 12 55 CC 1B 41  ...JeT..|73.U..A
AE 2F 10 67 7D EB 8A 23 61 7C 3C 1A EE 3B 05 8A  ./.g}..#a|<..;..
44 17 08 51 87 53 BE 5F E9 20 C0 FA CD 52 22 FF  D..Q.S._. ...R".
10 D6 5D 10 31 38 08 A5 90 47 A6 94 BA D1 F1 3B  ..].18...G.....;
5D BA F2 F4 1C D6 11 3A C2 F3 BC 00 CD 0B 92 10  ]......:........
70 0F BB B3 E2 CE DA 00 5B CF F7 A0 6B 4C 75 3E  p.......[...kLu>
17 4A 8D 83 D5 F3 85 77 1D DF EA 06 54 7E FD DC  .J.....w....T~..
B3 FD 20 6B C7 00 FF A9 17 DC 9D 62 20 C2 2E 48  .. k.......b ..H
41 31 16 0B 84 B0 00 C6 27 2E 4E 77 11 D9 98 05  A1......'.Nw....
50 CB 00 15 09 A0 37 2B 0A 60 D8 0F AA 35 10 F7  P.....7+.`...5..
6A 92 D7 42 B9 DF B0 31 C6 28 A6 DF 92 4D 69 B3  j..B...1.(...Mi.
BB B9 97 51 CF 3C 8C 0C 21 44 23 2C 42 25 6A A4  ...Q.<..!D#,B%j.
C7 D1 CF B0 7D 51 B6 05 CF B3 E0 1F 63 A1 71 9D  ....}Q......c.q.
81 D7 0E DD EC F8 60 99 22 6D 65 98 D8 C5 87 34  ......`."me....4
6E 16 2F 1E 73 C4 35 C6 CF ED 46 87 67 D8 75 F1  n./.s.5...F.g.u.
80 7A D2 C2 C6 CF 2E C4 75 BB 2C 92 AE 82 FB 81  .z......u.,.....
21 77 88 F9 5A D4 60 53 F8 AE 74 5A B7 C8 76 31  !w..Z.`S..tZ..v1
04 71 C5 1A 5C F1 45 93 36 75 BD D9 54 FB EE 11  .q..\.E.6u..T...
A0 B1 47 D2 B3 9A CE BA 10 19 A4 6A 8A 7C 76 A9  ..G........j.|v.
4F C2 20 D6 C2 8B 24 51 02 D8 93 E2 A4 5C 70 28  O. ...$Q.....\p(
49 08 B0 3E EC F5 43 2F 55 3C 02 56              I..>..C/U<.V

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:27.622006 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32257 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE93A  Ack: 0x60F76331  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926027386 759976799 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:28.452678 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26042 IpLen:20 DgmLen:480 DF
***AP*** Seq: 0x60F769FD  Ack: 0xDE6CE93A  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 759977824 926027386 
3E C4 E4 BB 4E D6 E6 A1 66 C2 F4 D7 CD 5E B5 59  >...N...f....^.Y
D2 58 35 DD F8 8F CE ED 5F BC E9 18 18 69 F2 5D  .X5....._....i.]
56 DF C6 9B 52 70 D2 1E C9 70 EC FF 67 F6 2E D0  V...Rp...p..g...
0D 2A BF FE B3 CA EF 54 2F 20 24 2A BB FF 00 21  .*.....T/ $*...!
F3 31 E1 BC 4F F2 07 AD 1F 87 EE B4 02 45 D7 92  .1..O........E..
39 1F 65 6E DB 7C 90 EA 5E 52 B5 4A 43 0B 60 A8  9.en.|..^R.JC.`.
9C 0E 48 37 08 71 59 C5 BB 00 AB 22 89 A8 83 4D  ..H7.qY...."...M
9C 23 51 03 97 12 70 5A DB E1 D6 52 5A 7F 91 E4  .#Q...pZ...RZ...
5B 5A 9B 47 47 86 0C A9 15 04 75 6A 3A 31 4C 23  [Z.GG.....uj:1L#
91 A3 C0 E5 F8 9D 86 03 78 E4 95 B0 41 2D 95 95  ........x...A-..
99 84 A5 0D DB AF 36 6A CB 3A F5 DD 68 F3 04 9F  ......6j.:..h...
93 72 5B 3F B3 05 4C 2D 6C E8 E0 1D A4 D1 D1 79  .r[?..L-l......y
40 62 E0 43 30 12 45 D0 81 15 C7 16 87 94 87 9A  @b.C0.E.........
B7 AC A1 B5 8F E5 73 28 3A 1D 8C 88 19 56 B7 61  ......s(:....V.a
27 35 69 37 AC 93 B4 C0 D8 AF B3 0E F9 F7 D7 B6  '5i7............
E6 DC 57 20 F7 C3 0C 24 DC AA BC 54 A1 5C 8F 9E  ..W ...$...T.\..
1E EC B6 71 BB 78 E7 C4 7E 97 19 F6 CC B6 42 6F  ...q.x..~.....Bo
02 9C AF 1A 09 E7 DC C4 66 E4 74 55 CD 19 1D 44  ........f.tU...D
91 A7 C9 C3 5C EE 3F 7C C0 C8 63 08 D0 7E 87 6D  ....\.?|..c..~.m
56 D8 82 5F C5 7F 2D 31 A2 E9 9D 12 CD E6 70 16  V.._..-1......p.
34 F7 76 4F 9B AF FD 5B 31 FD C3 D5 6E 05 D8 26  4.vO...[1...n..&
46 99 E2 97 2C E7 64 66 C4 0C 77 99 E8 D1 59 82  F...,.df..w...Y.
0D 7B 85 DC AE 2F 46 6E F2 D3 42 ED B6 D4 0D DE  .{.../Fn..B.....
F8 10 B2 1C D4 DB 53 28 A3 0D 26 12 79 97 01 5B  ......S(..&.y..[
E6 05 B6 A0 DA F0 01 EF 07 0B 0E 5A 15 02 55 D8  ...........Z..U.
23 52 1B 6B E5 6D 4B 44 2E 3E 6A 4C 1A 2E 9A 53  #R.k.mKD.>jL...S
37 06 13 39 B7 8D 6F 3F 22 A9 D5 6A              7..9..o?"..j

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:28.643225 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32258 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE93A  Ack: 0x60F7682D  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926028403 759977823 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:28.652060 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32259 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE93A  Ack: 0x60F769FD  Win: 0x1F2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926028403 759977823 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:28.652060 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32260 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CE93A  Ack: 0x60F76BA9  Win: 0x1EF  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926028403 759977824 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

^C*** Caught Int-Signal

root@ip-10-10-81-86:/home/ubuntu/Desktop/Task-Exercises# sudo snort -d -e -q
12/05-18:58:57.798504 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32284 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CEA62  Ack: 0x60F77BDD  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926057365 760006972 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:58.660536 02:89:23:51:E4:69 -> 02:C8:85:B5:5A:AA type:0x800 len:0x186
10.10.81.86:22 -> 10.8.19.103:48220 TCP TTL:64 TOS:0x10 ID:26059 IpLen:20 DgmLen:376 DF
***AP*** Seq: 0x60F77BDD  Ack: 0xDE6CEA62  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760008031 926057365 
60 56 E3 35 F2 70 69 1F 37 59 A2 97 C1 2C 3A 11  `V.5.pi.7Y...,:.
17 D7 39 87 45 72 B2 70 FF D0 35 E8 0C 0D 45 5F  ..9.Er.p..5...E_
23 8F 0A BA 90 92 42 EB F1 15 BC 1C 7D 91 BC 2D  #.....B.....}..-
87 C7 18 61 C1 D5 8E D1 39 BA EE 3D D5 F0 34 16  ...a....9..=..4.
FC D3 A2 06 CE 9C 2D 2D EE 9F E6 79 E3 41 60 14  ......--...y.A`.
64 33 18 9E FD 41 B8 9B 7B DE 98 80 DC CD 9A BC  d3...A..{.......
9C F0 42 54 85 B6 F1 A8 EA AD 3A AB DC F5 53 C5  ..BT......:...S.
A8 A4 0E 6D 67 B2 75 35 64 43 AE 9D B6 11 0A 6C  ...mg.u5dC.....l
0D 12 53 DC 4F 36 7A 1D 48 9D 8B 38 A7 69 99 B9  ..S.O6z.H..8.i..
66 2B C1 E2 CE 60 8E 27 C8 C4 88 DD C5 97 32 73  f+...`.'......2s
21 FC 82 EF FE 0B 23 13 F3 06 F2 73 96 D0 13 60  !.....#....s...`
FB 91 30 49 CE A9 D7 52 4A 6A DF F8 2A 48 ED 1E  ..0I...RJj..*H..
2E 90 54 AE 45 E2 F4 EB B6 AE E2 62 0D 21 C2 BB  ..T.E......b.!..
E5 EE 95 BB DD 44 90 54 1D 53 F1 2F EE D8 DB 9F  .....D.T.S./....
45 D5 AC C6 78 89 BC 6E 96 8E E0 A7 51 17 DB D3  E...x..n....Q...
05 72 CE 6A 51 46 9B 0F 5A A8 37 17 59 29 37 54  .r.jQF..Z.7.Y)7T
89 3A 12 8B 8D DD E8 79 62 2E 4D BF BE 24 17 31  .:.....yb.M..$.1
BF F4 CC A1 44 68 DB 6E B0 B0 23 E9 8A F0 E4 23  ....Dh.n..#....#
85 DF B8 84 4A 5F BC 19 48 E2 64 90 64 18 C1 A8  ....J_..H.d.d...
F9 E4 63 A1 A3 C3 DC EB 2C 80 D6 3D 80 12 D7 3C  ..c.....,..=...<
FA 87 9D 23                                      ...#

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:58.660644 02:89:23:51:E4:69 -> 02:C8:85:B5:5A:AA type:0x800 len:0x6E
10.10.81.86:22 -> 10.8.19.103:48220 TCP TTL:64 TOS:0x10 ID:26060 IpLen:20 DgmLen:96 DF
***AP*** Seq: 0x60F77D21  Ack: 0xDE6CEA62  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760008032 926057365 
7F F4 A7 FF 64 13 C3 1F 2E F6 0F 1B ED 80 02 B8  ....d...........
68 55 4C 16 10 55 13 C5 95 16 58 A6 40 A9 9A C9  hUL..U....X.@...
21 75 E6 98 73 2E 81 EE B7 25 68 80              !u..s....%h.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:58.660663 02:89:23:51:E4:69 -> 02:C8:85:B5:5A:AA type:0x800 len:0xB6
10.10.81.86:22 -> 10.8.19.103:48220 TCP TTL:64 TOS:0x10 ID:26061 IpLen:20 DgmLen:168 DF
***AP*** Seq: 0x60F77D4D  Ack: 0xDE6CEA62  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760008032 926057365 
81 2E DD DB D7 B8 1E 1E E1 45 C1 31 3F AA AF BA  .........E.1?...
34 B3 16 A2 3E BC B7 43 8C 6C E0 D0 37 09 BE CE  4...>..C.l..7...
05 D0 3E 65 B8 73 AF 91 8B E0 3D 96 5C ED 6C 43  ..>e.s....=.\.lC
8B 29 9A BA D0 4A 8C 8A C9 0C 50 D5 B3 DB 26 5C  .)...J....P...&\
7F 0A C9 6E DC CF D4 89 A2 D2 52 29 F5 3C E1 41  ...n......R).<.A
2A BB D5 26 DD C1 0F C4 81 A9 87 80 83 DA C5 68  *..&...........h
49 C3 CE 5F 6A 1B C3 F3 5B CA FF 56 26 DE E8 53  I.._j...[..V&..S
89 62 2F 17                                      .b/.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:58.861500 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32285 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CEA62  Ack: 0x60F77D21  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926058415 760008031 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:58.861500 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32286 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CEA62  Ack: 0x60F77D4D  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926058415 760008032 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:58.862703 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32287 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CEA62  Ack: 0x60F77DC1  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926058415 760008032 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:59.684573 02:89:23:51:E4:69 -> 02:C8:85:B5:5A:AA type:0x800 len:0x18E
10.10.81.86:22 -> 10.8.19.103:48220 TCP TTL:64 TOS:0x10 ID:26062 IpLen:20 DgmLen:384 DF
***AP*** Seq: 0x60F77DC1  Ack: 0xDE6CEA62  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760009055 926058415 
24 3F 28 65 88 59 1F BE DE 24 1F 27 C1 1B 56 6A  $?(e.Y...$.'..Vj
40 47 1A 18 93 65 79 01 C1 1C B9 AE A3 FF F3 46  @G...ey........F
78 FC 0E DC D9 3D 0E 20 C7 C0 F5 E2 FF E8 FA 3C  x....=. .......<
3E 33 BD 7C 57 6D 20 B5 89 1A 4E 79 94 FD 3B D2  >3.|Wm ...Ny..;.
F1 7E D7 B8 8C D8 C7 71 99 F6 23 90 9C 26 2A 6A  .~.....q..#..&*j
28 03 ED 82 79 48 26 F7 DF 98 DE 28 F2 D6 0C BB  (...yH&....(....
FA 1F AB F4 F3 3F AF A1 CF 04 12 77 13 E2 97 76  .....?.....w...v
EE 27 C2 FA F0 43 19 AB 8E A5 D2 57 DD 33 40 16  .'...C.....W.3@.
D0 F3 F2 9B 8C F1 9A 73 01 1D C0 8C C7 41 B6 A5  .......s.....A..
85 34 D8 DB BF 7D E8 00 45 BA DA 2B 7B 6D 7D F1  .4...}..E..+{m}.
D1 61 55 B4 3B FF 51 50 1B 20 46 4C 0E DB F5 1E  .aU.;.QP. FL....
0F DE C9 3A C8 A0 0A 5C 8A A6 A1 E0 4A 78 09 B0  ...:...\....Jx..
42 67 D3 1B A8 E2 BC ED 36 9B EE 07 D2 C8 79 9F  Bg......6.....y.
83 BA 36 13 C5 D8 30 B5 50 4F BF 6E CB 2E D0 1E  ..6...0.PO.n....
E5 F2 5B 4B B9 1E 52 58 24 46 59 0B 3F FB EB 02  ..[K..RX$FY.?...
03 B0 1C 0A C0 87 26 65 A7 A2 F7 43 D6 AE 19 35  ......&e...C...5
53 73 E8 E3 0F FB F1 A9 F8 DB 1F C5 D2 46 53 7F  Ss...........FS.
40 4E BC 4F 89 DF E6 04 73 EC 48 EB 54 8E D9 39  @N.O....s.H.T..9
74 26 A3 FF 90 AC EF 97 71 7E 19 11 B1 38 0A C7  t&......q~...8..
D5 17 50 4D 8A A4 94 C4 04 7F 55 46 2C 76 F8 EE  ..PM......UF,v..
4F 24 B0 73 14 0E 14 0E 9E 65 D3 33              O$.s.....e.3

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:59.684787 02:89:23:51:E4:69 -> 02:C8:85:B5:5A:AA type:0x800 len:0x12E
10.10.81.86:22 -> 10.8.19.103:48220 TCP TTL:64 TOS:0x10 ID:26067 IpLen:20 DgmLen:288 DF
***AP*** Seq: 0x60F78E5D  Ack: 0xDE6CEA62  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760009056 926058415 
32 C2 2A DA 4C B1 72 62 A5 3A C7 5F 12 97 D6 B2  2.*.L.rb.:._....
88 D4 57 03 15 EC 4C C0 C4 FC 93 5C CE E6 C8 7A  ..W...L....\...z
59 77 38 D3 07 91 82 05 7F 9B 9C B1 51 AC E8 E7  Yw8.........Q...
F7 B7 CE 4A EC 28 80 B1 0B 4B 65 D8 6F 8C 6D 88  ...J.(...Ke.o.m.
DB 81 40 4E C6 A4 50 D5 79 E7 99 3F 58 D6 DB 28  ..@N..P.y..?X..(
75 C7 96 97 29 66 38 1D 5F C1 A8 14 F3 42 F8 43  u...)f8._....B.C
2D BB FD 4F A6 B3 43 2D 6E 88 39 3A DD 6B 34 32  -..O..C-n.9:.k42
97 47 11 D7 5C 64 AF 6C A6 CC E3 3A DF 36 69 C1  .G..\d.l...:.6i.
11 9A 9D 2B FB C6 7D 33 A5 A2 4E 0A AA E0 84 96  ...+..}3..N.....
AA 60 D1 D8 0B 5D 75 46 1F BE 11 8B F0 4F 3F E6  .`...]uF.....O?.
E8 00 21 6C F4 88 69 E8 BD DF AC 2B 8E F0 B7 2C  ..!l..i....+...,
E0 45 BA 79 69 5C 7A 36 6A 44 55 B4 B6 16 29 E5  .E.yi\z6jDU...).
4D B7 9E 58 6D 50 D0 93 78 79 E1 E7 44 68 62 DB  M..XmP..xy..Dhb.
26 75 DE BD 46 4C 96 12 DF 2C C4 D0 A0 B4 78 0C  &u..FL...,....x.
2D 58 64 3F 25 26 AB 28 D3 44 9B D4              -Xd?%&.(.D..

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:59.882717 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32288 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CEA62  Ack: 0x60F77F0D  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926059433 760009055 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:59.886728 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32289 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CEA62  Ack: 0x60F78409  Win: 0x1F2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926059433 760009056 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:59.886729 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32290 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CEA62  Ack: 0x60F785A1  Win: 0x1EF  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926059433 760009056 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:59.886745 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32291 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CEA62  Ack: 0x60F78A9D  Win: 0x1E6  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926059434 760009056 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:59.886749 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32292 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CEA62  Ack: 0x60F78E5D  Win: 0x1DF  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926059434 760009056 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:58:59.888569 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32293 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CEA62  Ack: 0x60F78F49  Win: 0x1DE  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926059434 760009056 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

^C*** Caught Int-Signal

root@ip-10-10-81-86:/home/ubuntu/Desktop/Task-Exercises# sudo snort -X
Running in packet dump mode

        --== Initializing Snort ==--
Initializing Output Plugins!
pcap DAQ configured to passive.
Acquiring network traffic from "eth0".
Decoding Ethernet

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

Commencing packet processing (pid=21579)
12/05-18:59:32.872608 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26097 IpLen:20 DgmLen:112 DF
***AP*** Seq: 0x60F7A891  Ack: 0xDE6CECA2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760042244 926092118 
0x0000: 02 C8 85 B5 5A AA 02 89 23 51 E4 69 08 00 45 10  ....Z...#Q.i..E.
0x0010: 00 70 65 F1 40 00 40 06 5B B8 0A 0A 51 56 0A 08  .pe.@.@.[...QV..
0x0020: 13 67 00 16 BC 5C 60 F7 A8 91 DE 6C EC A2 80 18  .g...\`....l....
0x0030: 01 D4 79 31 00 00 01 01 08 0A 2D 4D 53 04 37 33  ..y1......-MS.73
0x0040: 0B 56 34 17 10 48 CF 08 D4 D7 3F 15 0C A0 96 E3  .V4..H....?.....
0x0050: BF 0A 6E 03 70 68 4A 60 09 F0 B4 23 1F FA E0 4F  ..n.phJ`...#...O
0x0060: CE 62 99 A7 D7 65 64 F8 21 A3 41 32 66 6E DE E5  .b...ed.!.A2fn..
0x0070: 04 41 21 3D 39 F2 74 D4 97 86 E1 52 ED 8F        .A!=9.t....R..

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:59:32.872745 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26098 IpLen:20 DgmLen:488 DF
***AP*** Seq: 0x60F7A8CD  Ack: 0xDE6CECA2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760042244 926092118 
0x0000: 02 C8 85 B5 5A AA 02 89 23 51 E4 69 08 00 45 10  ....Z...#Q.i..E.
0x0010: 01 E8 65 F2 40 00 40 06 5A 3F 0A 0A 51 56 0A 08  ..e.@.@.Z?..QV..
0x0020: 13 67 00 16 BC 5C 60 F7 A8 CD DE 6C EC A2 80 18  .g...\`....l....
0x0030: 01 D4 7A A9 00 00 01 01 08 0A 2D 4D 53 04 37 33  ..z.......-MS.73
0x0040: 0B 56 7B 35 50 4D 8E BD DD 0F AE D8 D1 EC 65 3F  .V{5PM........e?
0x0050: 78 8D CB 38 9E FF 1C 96 EB C6 86 6E 35 51 B9 BB  x..8.......n5Q..
0x0060: CD 58 55 C5 6F 24 7F 41 9F AC A2 04 BB 0F 66 98  .XU.o$.A......f.
0x0070: B3 FB B9 4B 2A 40 98 94 5A EA CF C0 E6 55 01 00  ...K*@..Z....U..
0x0080: 2B 71 85 AB 97 AB A3 9A 2B 3A 9A F9 11 07 7B 85  +q......+:....{.
0x0090: 0E 51 02 4F B4 19 CF F0 0B BE 18 49 07 B3 06 05  .Q.O.......I....
0x00A0: 6A A8 BC 4C 8E AC AA 84 A0 32 94 8A F4 AB E0 10  j..L.....2......
0x00B0: AE 79 4B A9 33 89 71 24 03 4E 9C 8E 83 BE 57 1C  .yK.3.q$.N....W.
0x00C0: 62 07 93 EF C7 80 4F 06 B5 58 27 2C AB 67 CA 3E  b.....O..X',.g.>
0x00D0: E9 31 76 FB 05 4B 4A 08 82 12 97 6F 61 5F 1A 59  .1v..KJ....oa_.Y
0x00E0: B2 2E 56 BA 76 B2 54 F6 62 1A 97 1F DC FF BB D0  ..V.v.T.b.......
0x00F0: 8A D8 69 EE BC 94 0C 00 BC 4B 80 28 1C 74 77 38  ..i......K.(.tw8
0x0100: 52 A4 DA 3E 04 0B FF 96 5F 5D 16 64 D3 75 8B 24  R..>...._].d.u.$
0x0110: 2D 45 2E 65 BC 44 28 3A 9D B4 63 D5 94 B0 C6 59  -E.e.D(:..c....Y
0x0120: FC C8 82 1E 09 FF 01 CC 5F 13 4E 4E 18 12 74 4C  ........_.NN..tL
0x0130: CC D8 CE 55 84 C8 F4 1F FE 32 8C 2E 61 D2 05 91  ...U.....2..a...
0x0140: 1F E7 03 FD CF AC 74 62 82 BD D8 60 5B 0E C7 9E  ......tb...`[...
0x0150: 3C BB CD E4 DE 32 AF A4 4D 68 0A 13 5B DF 6D 2D  <....2..Mh..[.m-
0x0160: 02 33 4D 74 C3 BA 78 26 BE C8 DA 1B C8 3B 5B B2  .3Mt..x&.....;[.
0x0170: A2 B4 57 FD AA 45 2B 15 AC 9A 90 25 79 6B AF F6  ..W..E+....%yk..
0x0180: BF B7 CB 1A 68 67 AC 68 F2 C8 10 2E A4 DA FB B4  ....hg.h........
0x0190: 27 A0 BA 9D 74 65 63 D1 9F 6A 2F FA 95 E0 00 CA  '...tec..j/.....
0x01A0: 95 8E 88 9F AA BC 78 A0 41 3A 15 1F 3B 50 5D E9  ......x.A:..;P].
0x01B0: BD 5A 2C 5C 65 74 1B 6F 5A B7 E9 EE 88 E6 93 FE  .Z,\et.oZ.......
0x01C0: 1C E0 8B F4 97 B3 DB 18 44 5A 74 36 1E 23 B2 43  ........DZt6.#.C
0x01D0: C1 7D 53 F6 5E D0 43 80 FC 7F FA 48 49 A9 B5 71  .}S.^.C....HI..q
0x01E0: B0 22 A6 B3 3F D0 2B 3E EC A4 D4 29 2A EE 3F D0  ."..?.+>...)*.?.
0x01F0: C2 E4 18 D7 39 ED                                ....9.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:59:32.872834 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26099 IpLen:20 DgmLen:224 DF
***AP*** Seq: 0x60F7AA81  Ack: 0xDE6CECA2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760042244 926092118 
0x0000: 02 C8 85 B5 5A AA 02 89 23 51 E4 69 08 00 45 10  ....Z...#Q.i..E.
0x0010: 00 E0 65 F3 40 00 40 06 5B 46 0A 0A 51 56 0A 08  ..e.@.@.[F..QV..
0x0020: 13 67 00 16 BC 5C 60 F7 AA 81 DE 6C EC A2 80 18  .g...\`....l....
0x0030: 01 D4 79 A1 00 00 01 01 08 0A 2D 4D 53 04 37 33  ..y.......-MS.73
0x0040: 0B 56 DF 46 FB 9F 9C B0 42 D3 98 A0 53 EA E5 E0  .V.F....B...S...
0x0050: F9 73 5A A9 01 1C 66 B5 24 2B 16 C9 B1 9F 60 BD  .sZ...f.$+....`.
0x0060: D9 9F B9 21 6D 2D AA DE 49 8E 49 39 86 22 01 F9  ...!m-..I.I9."..
0x0070: DA FD E5 D5 1C 9D C7 7D 39 2A 7E B5 53 19 E7 16  .......}9*~.S...
0x0080: 3C 09 20 AC 1A A6 09 A0 AA 73 CA 08 D0 69 3B B7  <. ......s...i;.
0x0090: 62 7C F3 E4 4B 46 53 E0 7B 8C 8D D3 59 F6 F6 D3  b|..KFS.{...Y...
0x00A0: 25 0A A3 84 8E 35 2B 6C 60 A3 3F D5 58 4D F8 8B  %....5+l`.?.XM..
0x00B0: 6D 2D B9 AA EA AE A1 BA E8 6B FB 7D F2 7E 23 3A  m-.......k.}.~#:
0x00C0: 4A 4C E8 85 59 85 07 6D 81 1A 0A 86 E7 F1 78 21  JL..Y..m......x!
0x00D0: D6 01 45 7E 15 66 38 EB 9F E2 40 01 AD B0 40 2E  ..E~.f8...@...@.
0x00E0: 47 58 81 97 61 90 24 75 33 02 29 8A AB D9        GX..a.$u3.)...

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:33.008250 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32331 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7A77D  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926092316 760042184 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 4B 40 00 3F 06 44 9A 0A 08 13 67 0A 0A  .4~K@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 A7 7D 80 10  QV.\...l..`..}..
0x0030: 01 F5 A8 9D 00 00 01 01 08 0A 37 33 0C 1C 2D 4D  ..........73..-M
0x0040: 52 C8                                            R.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:33.034677 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32332 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7A801  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926092327 760042195 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 4C 40 00 3F 06 44 99 0A 08 13 67 0A 0A  .4~L@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 A8 01 80 10  QV.\...l..`.....
0x0030: 01 F5 A8 03 00 00 01 01 08 0A 37 33 0C 27 2D 4D  ..........73.'-M
0x0040: 52 D3                                            R.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:33.034677 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32333 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7A825  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926092328 760042195 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 4D 40 00 3F 06 44 98 0A 08 13 67 0A 0A  .4~M@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 A8 25 80 10  QV.\...l..`..%..
0x0030: 01 F5 A7 DE 00 00 01 01 08 0A 37 33 0C 28 2D 4D  ..........73.(-M
0x0040: 52 D3                                            R.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:33.063250 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32334 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7A891  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926092362 760042210 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 4E 40 00 3F 06 44 97 0A 08 13 67 0A 0A  .4~N@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 A8 91 80 10  QV.\...l..`.....
0x0030: 01 F5 A7 41 00 00 01 01 08 0A 37 33 0C 4A 2D 4D  ...A......73.J-M
0x0040: 52 E2                                            R.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:33.074017 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32335 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7A8CD  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926092374 760042244 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 4F 40 00 3F 06 44 96 0A 08 13 67 0A 0A  .4~O@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 A8 CD 80 10  QV.\...l..`.....
0x0030: 01 F5 A6 D7 00 00 01 01 08 0A 37 33 0C 56 2D 4D  ..........73.V-M
0x0040: 53 04                                            S.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:33.074018 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32336 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7AA81  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926092374 760042244 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 50 40 00 3F 06 44 95 0A 08 13 67 0A 0A  .4~P@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 AA 81 80 10  QV.\...l..`.....
0x0030: 01 F5 A5 23 00 00 01 01 08 0A 37 33 0C 56 2D 4D  ...#......73.V-M
0x0040: 53 04                                            S.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:33.074018 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32337 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7AB2D  Win: 0x1F4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926092374 760042244 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 51 40 00 3F 06 44 94 0A 08 13 67 0A 0A  .4~Q@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 AB 2D 80 10  QV.\...l..`..-..
0x0030: 01 F4 A4 78 00 00 01 01 08 0A 37 33 0C 56 2D 4D  ...x......73.V-M
0x0040: 53 04                                            S.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:59:33.860715 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26100 IpLen:20 DgmLen:1176 DF
***AP*** Seq: 0x60F7AB2D  Ack: 0xDE6CECA2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760043232 926092374 
0x0000: 02 C8 85 B5 5A AA 02 89 23 51 E4 69 08 00 45 10  ....Z...#Q.i..E.
0x0010: 04 98 65 F4 40 00 40 06 57 8D 0A 0A 51 56 0A 08  ..e.@.@.W...QV..
0x0020: 13 67 00 16 BC 5C 60 F7 AB 2D DE 6C EC A2 80 18  .g...\`..-.l....
0x0030: 01 D4 7D 59 00 00 01 01 08 0A 2D 4D 56 E0 37 33  ..}Y......-MV.73
0x0040: 0C 56 A3 64 5E 73 CF 76 9C A4 C3 5B 0E 03 08 D5  .V.d^s.v...[....
0x0050: 7E 58 2B FD AB 19 B2 CC 7D 38 71 1D 22 02 B3 09  ~X+.....}8q."...
0x0060: EC BE B1 6E B2 B3 55 0C CF FA 32 05 3A 93 81 B8  ...n..U...2.:...
0x0070: 4A A3 77 40 01 7B 5A 04 F6 49 FD 68 45 53 3D B9  J.w@.{Z..I.hES=.
0x0080: 2C 8E F2 83 64 50 C9 0E 91 1A 54 E3 F2 B2 DE 07  ,...dP....T.....
0x0090: 0D 1C 4C C5 BB 79 9B 26 B1 C0 B8 E5 C9 BD 8B 65  ..L..y.&.......e
0x00A0: 15 70 2C A0 12 76 C7 BF DE 82 7E 2B B9 6E 61 67  .p,..v....~+.nag
0x00B0: 88 86 5E A8 D1 7E 27 C2 D6 79 78 2F E8 0E 7D 59  ..^..~'..yx/..}Y
0x00C0: F7 0D 18 1E D5 93 D6 D6 51 EB 2E CC 04 C9 D6 04  ........Q.......
0x00D0: DE EA 9D 80 3B 75 0A 93 B6 5C 97 6E 8A F8 4B 1A  ....;u...\.n..K.
0x00E0: F8 F1 55 D6 87 33 25 AE 81 77 C5 D3 78 15 7F 44  ..U..3%..w..x..D
0x00F0: F9 E8 B8 C6 EB 9A C2 FE F0 DB F2 99 1F 94 94 C5  ................
0x0100: FF 36 22 90 2A 8F 12 C1 61 2B 76 A5 FF DD E2 1C  .6".*...a+v.....
0x0110: E7 2C 3B 6E 73 D2 A0 49 16 6A 0D BC 59 54 D7 5E  .,;ns..I.j..YT.^
0x0120: C0 01 04 B6 51 CF AD C7 3E DC D8 47 B7 D0 FE 4E  ....Q...>..G...N
0x0130: D6 AA 2D 1A 46 90 DF DF 64 A5 6E E3 0C D2 68 E1  ..-.F...d.n...h.
0x0140: 4A 79 1D CA E2 65 46 E2 7A D0 39 6D 05 9C 51 62  Jy...eF.z.9m..Qb
0x0150: E2 F3 73 2D E7 73 2E D9 94 61 BD F3 EA 27 F4 AF  ..s-.s...a...'..
0x0160: 04 3B 86 A4 5E 78 C0 96 CC F7 1D 3D 56 43 1A 1A  .;..^x.....=VC..
0x0170: 58 D8 73 42 7D CF CC 29 68 E0 47 ED 1B 3F 1F 39  X.sB}..)h.G..?.9
0x0180: 7C DA 64 1C D4 68 27 F8 CA 3F FE 89 99 4E 39 E1  |.d..h'..?...N9.
0x0190: FD 21 64 59 6E 03 DF 8F 2F 3F D3 D8 7B EA 7B 04  .!dYn.../?..{.{.
0x01A0: 5E 72 7D 6E 9E EB BD B1 8F 03 B4 B5 B6 B7 F3 BD  ^r}n............
0x01B0: E8 1B E6 20 3F 80 53 54 0F 7F D6 4B 4A 71 F3 D0  ... ?.ST...KJq..
0x01C0: 9D 85 A1 DD A0 97 D0 15 56 0C 0C DE 07 D4 FD 5A  ........V......Z
0x01D0: 4B DF E0 3D 81 76 69 A6 BA BB FE 6F A5 24 44 0F  K..=.vi....o.$D.
0x01E0: 60 06 BF BF 14 EB 54 2A 74 2A 52 73 02 4C D8 C0  `.....T*t*Rs.L..
0x01F0: EE 3F E7 4A 03 5F 19 BF AD C0 7C 47 CF F4 89 A8  .?.J._....|G....
0x0200: 7C 96 07 BC C1 47 22 7A DF 16 C4 62 CD 7E 6C B3  |....G"z...b.~l.
0x0210: 22 87 1F 99 81 D6 F4 60 53 0B EB 4B 0A 3A 9D 36  "......`S..K.:.6
0x0220: F4 8B 0B 07 E9 4E 99 20 A2 28 A2 51 55 E9 2A 33  .....N. .(.QU.*3
0x0230: 00 15 AC EB 21 21 44 47 30 6C F4 13 9C 38 0F DC  ....!!DG0l...8..
0x0240: 60 EC 62 7D 6D 2C B2 A6 F1 11 C2 A3 9C 4A F1 A0  `.b}m,.......J..
0x0250: 23 66 9A 40 DE F2 7E B2 DC 46 04 33 47 DE A7 1F  #f.@..~..F.3G...
0x0260: BC CA 62 2E DE 71 8E 1D 33 40 81 1C 30 14 75 77  ..b..q..3@..0.uw
0x0270: 9A EC F6 16 D0 BB 93 EE D6 71 C3 1A FD F5 A6 81  .........q......
0x0280: 57 B6 E8 7F 20 3A BE 08 96 69 E1 F0 33 AA 88 9C  W... :...i..3...
0x0290: 56 37 B0 AC 88 90 47 26 70 84 CF 9B 51 CB 13 A7  V7....G&p...Q...
0x02A0: F2 A2 B8 50 E5 41 2C DF C8 18 D1 B2 E4 85 AA 3C  ...P.A,........<
0x02B0: B9 F8 96 1B C5 BF 69 68 A2 F5 D5 D6 9A 0B 59 AF  ......ih......Y.
0x02C0: 18 6F 8B 9D 2C A0 4E 2F E3 75 21 79 5E F7 B8 DA  .o..,.N/.u!y^...
0x02D0: 05 B3 21 68 41 D5 FE 27 A7 25 B3 A6 8F 2C 94 7F  ..!hA..'.%...,..
0x02E0: 5C 49 F1 B6 A5 BE C1 26 30 14 AA 35 F7 0E B0 5F  \I.....&0..5..._
0x02F0: 88 02 D5 E6 81 05 63 73 C2 C0 CF A4 CA 82 37 2F  ......cs......7/
0x0300: F7 48 D1 57 7E DA 17 95 C9 F0 97 05 04 6A 7C 0D  .H.W~........j|.
0x0310: 8B A2 86 BB 86 CC 02 03 0F 03 75 9E 0C B4 A7 05  ..........u.....
0x0320: 9A 27 57 60 16 1E DA 10 84 40 D2 69 9B 03 F6 EC  .'W`.....@.i....
0x0330: 6E E9 A0 8A 16 F6 5E 81 F5 49 F8 17 5F 84 27 6A  n.....^..I.._.'j
0x0340: 1B 11 39 49 57 E3 5C 65 D6 57 E6 B2 03 BD 78 FF  ..9IW.\e.W....x.
0x0350: 91 17 34 5F 07 45 7A B4 ED 63 98 A2 3B F0 6E D5  ..4_.Ez..c..;.n.
0x0360: 54 D6 CC C9 9B DF 48 59 37 B0 07 8B EA 0E 3D 2F  T.....HY7.....=/
0x0370: 66 A8 E0 F4 AF C4 76 21 8E D6 18 AC 07 32 0B 59  f.....v!.....2.Y
0x0380: 58 A6 48 83 AC 10 1A 79 93 5E A9 3E FA 9E 05 81  X.H....y.^.>....
0x0390: 7F 19 0B 66 73 C9 39 46 AE 22 46 A1 8A 12 2C 81  ...fs.9F."F...,.
0x03A0: 10 10 58 76 74 BC DF 5D DD 5D 04 E3 16 DF 7D A7  ..Xvt..].]....}.
0x03B0: F0 BF 79 00 FD DB 66 ED 66 A8 1B 36 61 A4 42 66  ..y...f.f..6a.Bf
0x03C0: 04 20 D0 DC 8D 72 49 AB 79 F2 68 B6 85 C3 EE 31  . ...rI.y.h....1
0x03D0: 3B 30 07 E2 32 90 C8 6B 22 A1 34 20 76 89 28 70  ;0..2..k".4 v.(p
0x03E0: AE BA 01 50 89 45 00 18 2B 45 C1 94 A6 9F 46 A3  ...P.E..+E....F.
0x03F0: 01 BC CF 3A 61 AF 3C 88 58 22 82 F1 AB 15 07 53  ...:a.<.X".....S
0x0400: 64 F7 8A 67 E8 72 4D CB EB AE B2 AC 8F 7A 9B 71  d..g.rM......z.q
0x0410: 45 0E 9A E9 21 08 B2 93 5D B6 F0 15 5F 5B EB 92  E...!...]..._[..
0x0420: 78 67 CC 3D 45 C5 9F 89 6D F5 C7 A5 C9 E9 CB D6  xg.=E...m.......
0x0430: A3 7A 99 E9 09 9A 73 46 F7 B2 9D 77 4A 10 79 30  .z....sF...wJ.y0
0x0440: 76 86 1F 1F BA D7 9B 65 BC 0A AB 1A 36 18 85 3B  v......e....6..;
0x0450: FA 77 90 61 B5 55 4D AA 82 1B 9E F6 90 F0 62 21  .w.a.UM.......b!
0x0460: 04 45 C6 DE 3E B3 66 14 00 47 EF 8E B9 25 BA A6  .E..>.f..G...%..
0x0470: B3 5C 98 61 A7 2D 8E D3 35 67 98 0D B0 A6 72 BF  .\.a.-..5g....r.
0x0480: 7F D6 27 48 BC B6 0C 3C 8F 5D 58 1A 1F BD C4 DD  ..'H...<.]X.....
0x0490: 1A A3 EA 83 08 B8 1A 5E BB 7B DC 9C 0A 31 64 EA  .......^.{...1d.
0x04A0: DA 74 E1 90 69 14                                .t..i.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:33.860893 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26103 IpLen:20 DgmLen:1496 DF
***AP*** Seq: 0x60F7B989  Ack: 0xDE6CECA2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760043232 926092374 
0x0000: 02 C8 85 B5 5A AA 02 89 23 51 E4 69 08 00 45 10  ....Z...#Q.i..E.
0x0010: 05 D8 65 F7 40 00 40 06 56 4A 0A 0A 51 56 0A 08  ..e.@.@.VJ..QV..
0x0020: 13 67 00 16 BC 5C 60 F7 B9 89 DE 6C EC A2 80 18  .g...\`....l....
0x0030: 01 D4 7E 99 00 00 01 01 08 0A 2D 4D 56 E0 37 33  ..~.......-MV.73
0x0040: 0C 56 9A 1A 1D 8E 1F 9F 88 EB B3 26 03 B3 E6 ED  .V.........&....
0x0050: 9F 0C 1E 6D 63 01 75 46 99 14 27 63 79 32 9C 54  ...mc.uF..'cy2.T
0x0060: AA 86 78 63 2A 8F 8A D6 95 00 14 2A D9 E3 55 F2  ..xc*......*..U.
0x0070: E0 2B 41 31 C8 10 E5 80 23 40 6D 4C F5 E0 86 2F  .+A1....#@mL.../
0x0080: D5 00 17 C4 6C 53 B9 B8 C4 50 B2 5E 2D 11 5A F1  ....lS...P.^-.Z.
0x0090: 8E EA B5 02 6D 42 D8 40 73 57 02 26 B0 67 96 4E  ....mB.@sW.&.g.N
0x00A0: 3F D7 E8 37 CA 4D AB 84 C4 48 91 8F 40 46 1C D0  ?..7.M...H..@F..
0x00B0: 0D C6 89 9A A3 FA F9 9A 58 39 F0 5B 23 A1 F8 CE  ........X9.[#...
0x00C0: 8E A0 5B 0D 6A 34 93 9B 7A 7E 8B 34 9E B8 50 F0  ..[.j4..z~.4..P.
0x00D0: 6C D8 47 77 11 B2 76 14 FE 8B 16 4D BD D6 94 61  l.Gw..v....M...a
0x00E0: D0 D9 BC 47 EF 3A E5 3D 17 CF D2 50 E5 F2 4E 05  ...G.:.=...P..N.
0x00F0: 64 E9 02 B3 B9 C3 09 63 E6 B6 7B 84 4A 4E C7 EE  d......c..{.JN..
0x0100: B9 AE 38 04 39 7F 4A 37 96 99 C0 26 D1 97 1C 12  ..8.9.J7...&....
0x0110: 30 71 55 FF 78 45 45 09 88 7C 9D E8 E4 EA 1B B8  0qU.xEE..|......
0x0120: 05 CC 96 A6 DB E7 3C A8 B2 D5 6D ED 93 26 08 9B  ......<...m..&..
0x0130: B1 79 0D 0B 10 11 5A A7 80 C9 62 4F FB 65 1B F5  .y....Z...bO.e..
0x0140: 1D 98 A8 C9 2B 45 89 EF 3F 7D 38 D3 E1 4B 5B 08  ....+E..?}8..K[.
0x0150: A0 97 3F 63 D4 5A 71 B9 07 DC DA 59 A2 E6 66 EB  ..?c.Zq....Y..f.
0x0160: 98 A6 61 54 BD D4 C0 FD AD A7 8C D0 98 36 23 42  ..aT.........6#B
0x0170: 63 56 52 39 BC C7 E1 3D D8 20 63 DA AD 49 EB BB  cVR9...=. c..I..
0x0180: 48 6C 1D 4B 9C 7E 73 01 49 3D AC 74 C4 08 F3 83  Hl.K.~s.I=.t....
0x0190: AC 0B E6 DA A0 17 4A 33 56 10 56 2E C6 F0 EC 0A  ......J3V.V.....
0x01A0: 6C B1 AB 36 24 53 A1 B0 20 6F 12 CB BC EE 23 85  l..6$S.. o....#.
0x01B0: 89 16 E8 46 6B D3 0E EF 66 76 FD A1 C3 1F FD EB  ...Fk...fv......
0x01C0: E2 F8 A1 28 C1 E2 E8 88 9F 9A 0B 1A 12 8E 5E 31  ...(..........^1
0x01D0: D8 41 65 E7 BB 21 72 AA 12 18 A7 90 B2 F7 F4 05  .Ae..!r.........
0x01E0: C2 7D 59 0B 50 FC 6F 41 01 AB 7B 61 3F 28 A6 C1  .}Y.P.oA..{a?(..
0x01F0: E7 B3 C8 33 DE 55 6C 10 D0 39 A5 84 8E BC F9 AB  ...3.Ul..9......
0x0200: FB 4C A8 12 A5 DB 86 D1 14 5B AA BF 55 29 98 8F  .L.......[..U)..
0x0210: 01 0B 26 B8 91 11 63 28 7A 32 43 BE 17 EA CA BC  ..&...c(z2C.....
0x0220: 1A 4C 04 41 84 8E F7 F1 CF 80 E7 8A A7 10 CB 3B  .L.A...........;
0x0230: D8 EF FA F5 81 3F A5 E4 B5 F2 FD D4 39 6A 6F 11  .....?......9jo.
0x0240: 5B 89 24 8E 30 B5 2C 13 AB F4 F6 CB D2 D7 FB 0E  [.$.0.,.........
0x0250: 40 F7 47 BD 44 EA E7 25 D0 0A E7 CA 82 73 6E B1  @.G.D..%.....sn.
0x0260: A1 C4 FA EC EF F8 C4 E7 25 78 D7 89 CF F3 87 68  ........%x.....h
0x0270: EE 92 B9 C7 3B 2B 8E EA C1 7F 6D 3A AD 0C 1C F6  ....;+....m:....
0x0280: 6C 9A 0C 80 1F DC 78 D9 FC D9 35 D0 AC BC F1 C8  l.....x...5.....
0x0290: AC BF FD E6 2D 8A 8C 17 7B 89 83 E6 13 A5 AC 12  ....-...{.......
0x02A0: 4E 5E 1D 73 A0 91 F8 3C 83 5D 43 E6 4C 8F E5 D5  N^.s...<.]C.L...
0x02B0: 2D 64 21 E5 1B FD 1E 9E 8E FD AD D0 0E 0A BA 16  -d!.............
0x02C0: 33 17 38 48 8C 9B 1D CC 7F D4 B4 DA F3 8B B8 9E  3.8H............
0x02D0: C6 52 B0 93 39 36 04 65 F3 8F A6 6A 43 E9 9A 83  .R..96.e...jC...
0x02E0: A8 35 D1 41 3A E4 BE 81 2B 91 EC E6 3E 3C 94 33  .5.A:...+...><.3
0x02F0: 98 78 4D E6 F2 2A 47 43 53 EA BB 83 BA 50 E4 95  .xM..*GCS....P..
0x0300: 4F F8 7C 52 27 3E B0 DF 85 94 BF 52 EC C9 F4 D9  O.|R'>.....R....
0x0310: E7 EF 11 EE 6E 1B 3E 61 02 34 7B 01 09 AD EF FB  ....n.>a.4{.....
0x0320: F6 51 C8 50 B2 0A 60 59 E1 30 BA 98 4A B0 8B 98  .Q.P..`Y.0..J...
0x0330: 7E E4 EB BB 5F 89 2C 18 0A 0D B8 BA F7 7F FE F0  ~..._.,.........
0x0340: BA 93 15 B1 6A 73 79 E4 87 D8 72 14 57 22 DB FF  ....jsy...r.W"..
0x0350: 80 75 BF A0 B7 16 50 AB B4 F4 D3 40 4D 8E 5B 44  .u....P....@M.[D
0x0360: 31 2E 2B D6 21 09 8C 07 56 CD CD 88 93 03 41 5D  1.+.!...V.....A]
0x0370: 02 D4 06 DA 82 36 9B F9 A0 2A 9C FA 82 F5 5B 94  .....6...*....[.
0x0380: 4A AB 67 21 B8 BA 79 49 B1 CA 1E C3 C2 97 66 44  J.g!..yI......fD
0x0390: A4 8C A7 9B 4A E8 FA C8 C5 BE 54 8D 79 3A 69 BB  ....J.....T.y:i.
0x03A0: 45 07 D2 E5 8E 5C 44 A7 1E 65 6F 8D 10 7F 87 94  E....\D..eo.....
0x03B0: F2 80 00 BC 38 88 EE 23 BE A2 5A AC F1 C6 79 F9  ....8..#..Z...y.
0x03C0: 87 57 64 81 62 A8 27 A8 8A FB 02 40 D0 7F AB E7  .Wd.b.'....@....
0x03D0: 86 F1 2B B4 CA DD CD 29 FE 95 B2 63 69 D7 4A 0D  ..+....)...ci.J.
0x03E0: 06 C1 EB C6 9D F5 6D 52 63 72 F6 7D 86 89 26 4E  ......mRcr.}..&N
0x03F0: AC 20 E3 89 19 CC 91 74 53 DA 6A 43 6F 5C DF DC  . .....tS.jCo\..
0x0400: 4C 02 8E 28 EA 8B 72 BF C7 03 0A A9 D8 A7 03 B9  L..(..r.........
0x0410: 52 7B 37 5A 1F AB 04 F4 22 74 1D 77 41 B4 6C F9  R{7Z...."t.wA.l.
0x0420: 1E 16 9D 6A 9A 88 6E 66 30 30 97 06 AF 62 A6 52  ...j..nf00...b.R
0x0430: 9C 35 BA 4C C8 FD 9B BD E1 2D 43 B2 CB 6A 34 3D  .5.L.....-C..j4=
0x0440: EB CE 9E CD 02 0B 46 DA F5 59 73 C5 A3 66 08 1B  ......F..Ys..f..
0x0450: 9E FD 0A C3 08 B0 AE 0F 53 12 EF 24 C9 A8 B9 5F  ........S..$..._
0x0460: 82 67 49 F2 4F E6 0D 21 D4 08 52 03 9A 78 B3 D5  .gI.O..!..R..x..
0x0470: F4 5A 3A A3 D6 9F 4E B9 53 3A 53 B0 82 57 0D 4D  .Z:...N.S:S..W.M
0x0480: 16 42 FA DC FB 36 48 99 F7 63 9E 15 25 1B AE 42  .B...6H..c..%..B
0x0490: 4F C0 50 BE 05 33 85 45 F9 13 C6 86 C1 60 F8 AC  O.P..3.E.....`..
0x04A0: 59 3E 27 C3 08 10 A6 BF 34 86 43 86 C5 AD 06 FD  Y>'.....4.C.....
0x04B0: 65 01 B1 9C 63 79 8A AA 1C BA 06 9D F6 8B 51 41  e...cy........QA
0x04C0: C1 05 D9 4A FF 8B FB 91 7E 70 04 B6 C0 FE 5A C9  ...J....~p....Z.
0x04D0: 45 87 FA 89 24 2B 60 E4 98 D2 AF E9 CD 8D CF 81  E...$+`.........
0x04E0: C2 30 0F 51 87 FE 29 A0 26 10 6A 6D 64 F8 89 E4  .0.Q..).&.jmd...
0x04F0: B0 69 7D 69 25 6F F3 02 DA 95 DA 7A 1F 3F 52 15  .i}i%o.....z.?R.
0x0500: EB DC B1 08 AC C1 87 EF A2 59 6E 25 08 63 1D 9B  .........Yn%.c..
0x0510: 65 9C C0 22 F7 6D 40 C4 2A F6 4F E9 23 CB 47 B7  e..".m@.*.O.#.G.
0x0520: 9D 21 1E C3 E9 1C 56 B3 D2 EF F6 D9 C5 62 FD 80  .!....V......b..
0x0530: C9 7E 03 97 A8 0A 20 CB 1E D2 60 DC 99 18 AC 69  .~.... ...`....i
0x0540: FD F0 5C 66 1A 94 EF 59 0C 6A 47 B7 AC 5F 40 8D  ..\f...Y.jG.._@.
0x0550: 5B E3 BB 13 06 85 A0 53 E6 4D 0B E8 A3 AD 3F DB  [......S.M....?.
0x0560: B0 94 B4 B5 B8 D3 7D 57 EA A7 5E 32 B3 61 D6 E7  ......}W..^2.a..
0x0570: E0 B8 70 FC 16 B5 3F DF A4 EB 04 92 B6 05 19 BC  ..p...?.........
0x0580: D5 5E BD 6B 7F 19 D0 3B C3 50 2C 3A 20 8D 8E E8  .^.k...;.P,: ...
0x0590: CF 57 85 2C 4D 31 7B 07 33 A4 49 AA 09 B5 7D AD  .W.,M1{.3.I...}.
0x05A0: 47 D1 91 0F 51 03 7F 31 AF B2 4D D6 8D C8 E1 BB  G...Q..1..M.....
0x05B0: 1D 1F A0 C6 7D 61 63 15 0F 2F BC 2A A0 4D 46 C0  ....}ac../.*.MF.
0x05C0: F8 FA 02 EE 1D 23 D5 B1 CD C0 9F 6A 30 9A DD 61  .....#.....j0..a
0x05D0: EA 7B 4D 49 72 0E EE 59 60 B1 C3 1F 87 B4 60 26  .{MIr..Y`.....`&
0x05E0: 26 F3 45 91 FD 75                                &.E..u

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
12/05-18:59:33.861086 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26109 IpLen:20 DgmLen:128 DF
***AP*** Seq: 0x60F7D31D  Ack: 0xDE6CECA2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760043232 926092374 
0x0000: 02 C8 85 B5 5A AA 02 89 23 51 E4 69 08 00 45 10  ....Z...#Q.i..E.
0x0010: 00 80 65 FD 40 00 40 06 5B 9C 0A 0A 51 56 0A 08  ..e.@.@.[...QV..
0x0020: 13 67 00 16 BC 5C 60 F7 D3 1D DE 6C EC A2 80 18  .g...\`....l....
0x0030: 01 D4 79 41 00 00 01 01 08 0A 2D 4D 56 E0 37 33  ..yA......-MV.73
0x0040: 0C 56 28 87 EF BE 92 4A 20 DC AD 0D 36 34 AD F2  .V(....J ...64..
0x0050: E5 1D B2 25 52 9E 3D A1 BF 34 C6 D6 30 4B 98 9F  ...%R.=..4..0K..
0x0060: 58 32 6F CF 84 4F FF D4 31 8F E6 4A F0 B8 FB B6  X2o..O..1..J....
0x0070: DB 84 B8 3F 22 16 AE B0 11 12 4A D7 F6 86 58 84  ...?".....J...X.
0x0080: 71 14 A6 D4 D6 67 D0 F7 D5 8D 74 F1 DC BD        q....g....t...

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:34.063021 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32338 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7AF91  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926093357 760043232 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 52 40 00 3F 06 44 93 0A 08 13 67 0A 0A  .4~R@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 AF 91 80 10  QV.\...l..`.....
0x0030: 01 F5 98 60 00 00 01 01 08 0A 37 33 10 2D 2D 4D  ...`......73.--M
0x0040: 56 E0                                            V.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:34.063056 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32339 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7B48D  Win: 0x1EE  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926093357 760043232 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 53 40 00 3F 06 44 92 0A 08 13 67 0A 0A  .4~S@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 B4 8D 80 10  QV.\...l..`.....
0x0030: 01 EE 93 6B 00 00 01 01 08 0A 37 33 10 2D 2D 4D  ...k......73.--M
0x0040: 56 E0                                            V.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:34.063057 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32340 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7B989  Win: 0x1E5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926093358 760043232 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 54 40 00 3F 06 44 91 0A 08 13 67 0A 0A  .4~T@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 B9 89 80 10  QV.\...l..`.....
0x0030: 01 E5 8E 77 00 00 01 01 08 0A 37 33 10 2E 2D 4D  ...w......73..-M
0x0040: 56 E0                                            V.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:34.063847 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32341 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7BE85  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926093358 760043232 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 55 40 00 3F 06 44 90 0A 08 13 67 0A 0A  .4~U@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 BE 85 80 10  QV.\...l..`.....
0x0030: 01 F5 89 6B 00 00 01 01 08 0A 37 33 10 2E 2D 4D  ...k......73..-M
0x0040: 56 E0                                            V.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:34.063847 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32342 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7BF2D  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926093358 760043232 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 56 40 00 3F 06 44 8F 0A 08 13 67 0A 0A  .4~V@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 BF 2D 80 10  QV.\...l..`..-..
0x0030: 01 F5 88 C3 00 00 01 01 08 0A 37 33 10 2E 2D 4D  ..........73..-M
0x0040: 56 E0                                            V.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:34.063847 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32343 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7C429  Win: 0x1F2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926093358 760043232 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 57 40 00 3F 06 44 8E 0A 08 13 67 0A 0A  .4~W@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 C4 29 80 10  QV.\...l..`..)..
0x0030: 01 F2 83 CA 00 00 01 01 08 0A 37 33 10 2E 2D 4D  ..........73..-M
0x0040: 56 E0                                            V.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:34.063847 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32344 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7C925  Win: 0x1E9  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926093358 760043232 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 58 40 00 3F 06 44 8D 0A 08 13 67 0A 0A  .4~X@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 C9 25 80 10  QV.\...l..`..%..
0x0030: 01 E9 7E D7 00 00 01 01 08 0A 37 33 10 2E 2D 4D  ..~.......73..-M
0x0040: 56 E0                                            V.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:34.063847 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32345 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7CE21  Win: 0x1E0  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926093358 760043232 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 59 40 00 3F 06 44 8C 0A 08 13 67 0A 0A  .4~Y@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 CE 21 80 10  QV.\...l..`..!..
0x0030: 01 E0 79 E4 00 00 01 01 08 0A 37 33 10 2E 2D 4D  ..y.......73..-M
0x0040: 56 E0                                            V.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:34.063847 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32346 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7D31D  Win: 0x1D7  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926093359 760043232 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 5A 40 00 3F 06 44 8B 0A 08 13 67 0A 0A  .4~Z@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 D3 1D 80 10  QV.\...l..`.....
0x0030: 01 D7 74 F0 00 00 01 01 08 0A 37 33 10 2F 2D 4D  ..t.......73./-M
0x0040: 56 E0                                            V.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:34.067400 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32347 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7D369  Win: 0x1D7  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926093359 760043232 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 5B 40 00 3F 06 44 8A 0A 08 13 67 0A 0A  .4~[@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 D3 69 80 10  QV.\...l..`..i..
0x0030: 01 D7 74 A4 00 00 01 01 08 0A 37 33 10 2F 2D 4D  ..t.......73./-M
0x0040: 56 E0                                            V.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:59:34.884513 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26110 IpLen:20 DgmLen:320 DF
***AP*** Seq: 0x60F7D369  Ack: 0xDE6CECA2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760044255 926093359 
0x0000: 02 C8 85 B5 5A AA 02 89 23 51 E4 69 08 00 45 10  ....Z...#Q.i..E.
0x0010: 01 40 65 FE 40 00 40 06 5A DB 0A 0A 51 56 0A 08  .@e.@.@.Z...QV..
0x0020: 13 67 00 16 BC 5C 60 F7 D3 69 DE 6C EC A2 80 18  .g...\`..i.l....
0x0030: 01 D4 7A 01 00 00 01 01 08 0A 2D 4D 5A DF 37 33  ..z.......-MZ.73
0x0040: 10 2F 69 4C EF 15 D1 70 50 A9 BD FB 87 38 84 05  ./iL...pP....8..
0x0050: 2A 3F A5 AE 0A CD A3 D9 55 C1 77 8B C6 08 F3 DC  *?......U.w.....
0x0060: F4 06 5A A6 A7 90 97 A1 B0 C9 06 6F 9C 26 B4 FE  ..Z........o.&..
0x0070: 75 F2 6B B6 0E 63 5A 33 96 B7 DA 3F FE 02 17 12  u.k..cZ3...?....
0x0080: A2 46 C7 DD 66 A6 45 B5 6C B8 70 C6 1D C4 92 26  .F..f.E.l.p....&
0x0090: C2 86 64 12 D2 A9 40 80 09 0B A8 8F 05 CC 1D 73  ..d...@........s
0x00A0: 21 E3 37 B1 F1 66 14 B6 31 97 79 E4 BC A3 26 9B  !.7..f..1.y...&.
0x00B0: 95 A0 D5 0E 9F 32 A5 3C 7D A5 64 B9 B9 99 07 86  .....2.<}.d.....
0x00C0: C7 17 56 25 81 39 8B D9 0B D7 F2 C8 02 3B E2 9D  ..V%.9.......;..
0x00D0: DD 61 EA 7D 2C F5 F6 6A 13 5A 64 21 6E 4A 8B B4  .a.},..j.Zd!nJ..
0x00E0: B7 EA CF F9 DD 54 B8 68 A4 78 B7 A9 57 0D 72 D9  .....T.h.x..W.r.
0x00F0: B7 11 57 02 1D 08 03 64 F7 74 79 ED C7 D7 C9 D2  ..W....d.ty.....
0x0100: F9 F2 B3 0C E1 70 13 D0 3F 13 7C AC 14 6A EE 89  .....p..?.|..j..
0x0110: 8E 52 2C 4C FC E6 3B 5E 73 42 4A 27 55 1C 2B AE  .R,L..;^sBJ'U.+.
0x0120: 76 BC 7C 5D BF E2 C7 E4 DF 68 71 23 2C E0 9F 5C  v.|].....hq#,..\
0x0130: 25 1D 50 07 6D 15 18 65 2B 92 C2 12 AD C7 57 AE  %.P.m..e+.....W.
0x0140: 89 C2 34 B0 50 18 E1 1B C7 2A D8 24 C7 FA        ..4.P....*.$..

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:59:34.884621 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26111 IpLen:20 DgmLen:912 DF
***AP*** Seq: 0x60F7D475  Ack: 0xDE6CECA2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760044256 926093359 
0x0000: 02 C8 85 B5 5A AA 02 89 23 51 E4 69 08 00 45 10  ....Z...#Q.i..E.
0x0010: 03 90 65 FF 40 00 40 06 58 8A 0A 0A 51 56 0A 08  ..e.@.@.X...QV..
0x0020: 13 67 00 16 BC 5C 60 F7 D4 75 DE 6C EC A2 80 18  .g...\`..u.l....
0x0030: 01 D4 7C 51 00 00 01 01 08 0A 2D 4D 5A E0 37 33  ..|Q......-MZ.73
0x0040: 10 2F 9B 14 CD 7F 12 D3 A0 33 CE E4 F9 D4 0C 74  ./.......3.....t
0x0050: A5 43 F1 2B 45 F0 25 BA 53 01 00 C4 7D 23 8E E2  .C.+E.%.S...}#..
0x0060: D0 FD 0E 07 0B F5 92 4D 32 2D 4C 08 75 46 9B A5  .......M2-L.uF..
0x0070: FF 2A BE 7A 61 89 F8 EB C8 B6 64 9E 3E 96 B6 B1  .*.za.....d.>...
0x0080: 4E 45 5F 8A 39 6B 8F 77 C9 66 DF 19 6F 88 AD 31  NE_.9k.w.f..o..1
0x0090: 98 EB 8D 7A AA 3B 9D 3D 48 96 1F 04 05 FF B4 D1  ...z.;.=H.......
0x00A0: 97 7D BC 3B 6D 17 96 DF A1 B3 04 7C EE 15 3A FE  .}.;m......|..:.
0x00B0: 1E 94 9E 90 BB 67 98 75 2D 99 01 7E FB 9E 91 EB  .....g.u-..~....
0x00C0: 05 0E 61 B8 59 14 89 54 99 94 DD E5 CE 0E 35 E6  ..a.Y..T......5.
0x00D0: 7B 94 D0 AB B8 26 6C 91 7A 79 4D D4 BD A6 3D 44  {....&l.zyM...=D
0x00E0: DE 38 C0 4C 8D C7 AD 4A 26 E1 FC 6B 9B B7 A0 04  .8.L...J&..k....
0x00F0: B2 90 F7 FF 01 B1 EF 1F 72 5A 9B 9E B8 24 DC 21  ........rZ...$.!
0x0100: B8 05 B6 90 57 7F 50 86 51 0B 56 4A 67 15 19 F3  ....W.P.Q.VJg...
0x0110: 0E C3 C0 B1 27 BE 0C 22 83 3B F5 6B D0 83 2C 03  ....'..".;.k..,.
0x0120: 62 C6 9C F1 02 B4 8B 59 1A 84 26 5F 85 9D 89 3D  b......Y..&_...=
0x0130: 9C 32 AC 4E 13 B7 90 46 EF 50 9E CD 9A 52 A5 39  .2.N...F.P...R.9
0x0140: 01 FF 7B 88 7F DA EE FA F9 70 60 ED 90 06 DD B4  ..{......p`.....
0x0150: A6 B2 B8 F1 BA 7E 07 B8 AC 41 35 62 A0 F7 70 C7  .....~...A5b..p.
0x0160: EA 25 53 28 75 5D FF 0C 2A EE C2 56 26 11 64 D1  .%S(u]..*..V&.d.
0x0170: 2F 40 5E 69 F0 FA 1D BE 0D 5E 6F F0 E1 90 E9 F3  /@^i.....^o.....
0x0180: BD 64 F0 C7 17 41 CB 99 3D 61 89 05 B4 8C C1 67  .d...A..=a.....g
0x0190: AF C6 FA 4D B4 CF 5C E8 75 75 53 78 FD 75 84 8B  ...M..\.uuSx.u..
0x01A0: E7 05 B1 B6 A4 E9 16 52 46 7C A5 BE 9A BA 35 C0  .......RF|....5.
0x01B0: FC 63 20 22 A0 BC A9 8D 6C C6 1C E6 55 9A 37 26  .c "....l...U.7&
0x01C0: 6D 6B 48 9E 32 A9 26 7A 83 5F 16 8A B9 4C 6A D0  mkH.2.&z._...Lj.
0x01D0: B6 6F 9E A8 49 D9 94 3A 4E 1F FA 89 69 87 04 97  .o..I..:N...i...
0x01E0: E8 D9 2C C5 BD CE B0 BF B0 B7 29 8A 1C E2 17 00  ..,.......).....
0x01F0: A8 4F B6 2F AE 1A 27 C0 86 16 37 77 F1 E3 4F F8  .O./..'...7w..O.
0x0200: 27 10 33 35 17 2D B6 D3 1F 2D 01 47 DB 12 0F 86  '.35.-...-.G....
0x0210: F8 18 8F A7 1E AE C5 75 E5 98 BC 85 0E 8D D3 B8  .......u........
0x0220: F4 C1 21 9C 97 18 14 63 F4 64 39 D8 64 ED B2 BB  ..!....c.d9.d...
0x0230: F0 26 58 07 86 A3 CF DE C8 B2 9C 1C F0 97 05 DF  .&X.............
0x0240: BE 8D C4 2F D2 4D 2D 7C 40 8A 20 01 BE B0 35 AD  .../.M-|@. ...5.
0x0250: 76 6E 74 59 DD 9B 7D 5A 3B FA 29 BA D6 F4 97 F4  vntY..}Z;.).....
0x0260: 9C E0 11 16 5E 50 1E 11 58 E1 A2 39 0C 0D B5 7F  ....^P..X..9....
0x0270: FC 8C 21 27 11 F2 82 6D 5C 5A 87 13 62 BF 7F A0  ..!'...m\Z..b...
0x0280: D3 6F 44 79 4F 89 6B 46 7C 9F 71 D1 B1 B3 B5 85  .oDyO.kF|.q.....
0x0290: 5E F7 55 63 94 BA 6A 70 36 6E A5 04 F4 BA D4 B1  ^.Uc..jp6n......
0x02A0: 24 1A 67 7A B0 1E 00 7E D7 13 F7 36 96 81 2D 02  $.gz...~...6..-.
0x02B0: 8D EB C5 C4 79 4F E5 C6 34 10 25 FB E6 58 05 43  ....yO..4.%..X.C
0x02C0: 41 B3 8A 0D B2 54 2C 7A 58 24 FB 06 8B C7 42 10  A....T,zX$....B.
0x02D0: 33 ED 21 AD EB E0 EC AD EE 64 A7 31 81 BC F1 C2  3.!......d.1....
0x02E0: 86 7F 09 A5 2C BA C2 DB B9 F9 AE BA 41 7F 19 4B  ....,.......A..K
0x02F0: 38 F8 82 8A 82 F9 43 5D F1 3A CA DF 34 45 54 BD  8.....C].:..4ET.
0x0300: 12 0A B6 7C B9 80 41 34 B7 F0 0C 94 94 59 D8 3A  ...|..A4.....Y.:
0x0310: C3 C2 D3 88 D6 CD E5 04 79 EF 0D BD F1 6A AE D0  ........y....j..
0x0320: 50 5F 3D F8 E2 D7 29 55 FF CC 02 20 7F D0 53 A7  P_=...)U... ..S.
0x0330: F6 1A FB 2C DF 9C 36 2A CE A9 CC 3D EE 95 E6 D6  ...,..6*...=....
0x0340: F8 86 7C D2 46 2A 70 8D 73 FB 0B F7 7C FA 8C 2D  ..|.F*p.s...|..-
0x0350: 10 EE 83 7D 0D B4 5E CA 74 08 69 B9 D7 AD F1 24  ...}..^.t.i....$
0x0360: 8A 19 E8 64 8D F9 D1 EB 84 0A 49 8C 7B F8 C2 B2  ...d......I.{...
0x0370: 3D 9E 21 78 2F 67 90 BF 53 98 09 41 87 E9 46 59  =.!x/g..S..A..FY
0x0380: C2 04 D2 83 12 58 8A EE 13 20 68 E0 7D 5A 87 67  .....X... h.}Z.g
0x0390: C0 97 9F A9 DF 83 9E 6C 74 B2 DB F7 20 E1        .......lt... .

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:59:34.884671 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26112 IpLen:20 DgmLen:1064 DF
***AP*** Seq: 0x60F7D7D1  Ack: 0xDE6CECA2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760044256 926093359 
0x0000: 02 C8 85 B5 5A AA 02 89 23 51 E4 69 08 00 45 10  ....Z...#Q.i..E.
0x0010: 04 28 66 00 40 00 40 06 57 F1 0A 0A 51 56 0A 08  .(f.@.@.W...QV..
0x0020: 13 67 00 16 BC 5C 60 F7 D7 D1 DE 6C EC A2 80 18  .g...\`....l....
0x0030: 01 D4 7C E9 00 00 01 01 08 0A 2D 4D 5A E0 37 33  ..|.......-MZ.73
0x0040: 10 2F DA 08 CE EC DD 1D 42 7D 4A A9 B6 C6 F6 8D  ./......B}J.....
0x0050: FB BE 42 EC 64 6D 66 2F 88 F4 AB AC B2 DB 6B DA  ..B.dmf/......k.
0x0060: 74 D5 5F 58 B3 4F 00 B2 B7 A6 80 EF 73 37 89 F8  t._X.O......s7..
0x0070: FF 1D 7F 79 1A 65 AD BB 2A 3E 6E DF 80 E1 EE 66  ...y.e..*>n....f
0x0080: E6 30 C3 53 E7 8E E9 E7 04 25 4B 83 1C 73 D2 ED  .0.S.....%K..s..
0x0090: A1 8E 9D 48 52 A1 A2 5F 65 46 6A 44 96 D6 1A 7E  ...HR.._eFjD...~
0x00A0: F8 A6 EE 56 56 2E CB 1D 6D D6 D9 23 D9 72 46 8A  ...VV...m..#.rF.
0x00B0: 09 92 C5 F3 C2 94 54 04 F4 37 06 B9 87 BE 50 BF  ......T..7....P.
0x00C0: 3B 21 E5 58 ED 4D 31 09 E8 56 62 E7 C1 11 30 DC  ;!.X.M1..Vb...0.
0x00D0: A5 31 BD 8E 40 EF AE 14 F1 98 45 C3 4F CB 7E 7C  .1..@.....E.O.~|
0x00E0: B4 1D 35 37 42 10 2F 90 3C AE 1B 84 4D A2 73 FD  ..57B./.<...M.s.
0x00F0: 3A 5E 1D 8F A4 5A 75 F5 90 B0 E5 EF 25 A7 3D 1A  :^...Zu.....%.=.
0x0100: 15 EF C7 87 71 2A 45 F3 32 E7 95 EB E6 97 75 BC  ....q*E.2.....u.
0x0110: F4 E1 6E FF F8 72 D8 81 0C 6F 96 41 65 26 A0 14  ..n..r...o.Ae&..
0x0120: D0 F0 F8 A1 91 96 84 69 97 6D AC 67 8C 1B D2 15  .......i.m.g....
0x0130: F4 36 C3 F5 93 70 D0 7A 52 58 3B 67 5B 2D 7E A9  .6...p.zRX;g[-~.
0x0140: 8E F0 E1 BA 4E 8C 90 FB AE 3A 71 7A 49 09 4C CE  ....N....:qzI.L.
0x0150: 6F 48 35 C0 70 D4 C2 54 B8 0D 1F 85 F6 16 75 67  oH5.p..T......ug
0x0160: 3D E1 8D F6 10 7B AB CB 7E 24 4E 8A 1D B3 9D C5  =....{..~$N.....
0x0170: 78 DA 7F 50 C4 5D 23 F2 E3 0E F6 2D FD 56 FC 49  x..P.]#....-.V.I
0x0180: E7 21 F7 2F 8E 7B 0A 15 D8 0B 09 6D B0 AA 16 A6  .!./.{.....m....
0x0190: C7 09 D6 BE 08 1B 3A C2 80 C7 88 F9 4A 4F 3C BA  ......:.....JO<.
0x01A0: 29 FF 02 0E 4A 57 74 AE A3 A1 1E 08 07 03 5F 01  )...JWt......._.
0x01B0: 76 B7 42 F1 39 EE E7 A0 E7 BC 37 96 28 5A 66 B0  v.B.9.....7.(Zf.
0x01C0: 76 07 AA 80 1F 77 0D F8 DB 74 43 4B 4D 58 5F F0  v....w...tCKMX_.
0x01D0: 0C 56 BD C3 13 80 36 12 ED A2 01 E4 56 53 29 C6  .V....6.....VS).
0x01E0: 1D C1 90 3C B1 40 B6 68 5A EA F3 EA C3 6C 1B 4E  ...<.@.hZ....l.N
0x01F0: 2A 64 16 DD 3D 0F FF 0E BA 44 AC F6 39 8C FC AE  *d..=....D..9...
0x0200: 5B 1A 24 5B 77 01 F2 C5 D8 A5 C5 40 6F D5 79 D4  [.$[w......@o.y.
0x0210: 8D FD 88 22 2F BE E2 D1 2D 3E 08 9B 1D 1E F0 04  ..."/...->......
0x0220: 39 38 71 9E 10 51 EC 0B 5A 08 B7 38 A3 19 04 CD  98q..Q..Z..8....
0x0230: 42 54 14 9D 25 AD D1 E3 10 F5 AC FD 69 D7 17 4C  BT..%.......i..L
0x0240: 5B 1B D8 AB 86 19 85 C9 45 A5 25 96 D9 3D DC FB  [.......E.%..=..
0x0250: A5 00 58 6C A1 E2 09 21 CD BE 26 05 81 3F C8 30  ..Xl...!..&..?.0
0x0260: 53 DA F1 52 E9 E8 20 53 BB 7B EF 4D CD 8A 70 BA  S..R.. S.{.M..p.
0x0270: A2 B6 CE B8 32 AE E5 8E 29 82 87 B4 82 30 F3 75  ....2...)....0.u
0x0280: 57 B7 7C 16 FB A8 C3 A9 92 95 E2 55 0C 1F D6 F2  W.|........U....
0x0290: 50 76 77 6F C5 56 13 5C D5 B5 91 E1 D5 E6 26 2E  Pvwo.V.\......&.
0x02A0: 7C DF 9D 03 21 D3 CA 92 DE 1F 43 86 2A 56 B0 32  |...!.....C.*V.2
0x02B0: E3 50 40 90 53 47 AE 4A 73 F0 E5 71 72 82 F3 2A  .P@.SG.Js..qr..*
0x02C0: 38 C8 F1 F1 4B 2A E3 E7 43 7A 3F A6 A4 EE 73 CD  8...K*..Cz?...s.
0x02D0: 43 F1 21 AA 8B 3D 31 9B 32 D7 A9 EB 7D D9 CC EE  C.!..=1.2...}...
0x02E0: 55 77 14 6B 5E D7 B2 3C 36 49 32 0A 7F 7D 92 E7  Uw.k^..<6I2..}..
0x02F0: AA F1 A5 CF FF 80 FC F9 DF 1D 70 3D 14 DD D1 43  ..........p=...C
0x0300: D0 B8 7B 5C 93 C9 55 0D 62 3D 34 44 96 E0 9C 0B  ..{\..U.b=4D....
0x0310: 27 98 CD 16 B4 D0 5C 41 BF D4 86 67 04 6A 7B 99  '.....\A...g.j{.
0x0320: 2D 47 7D 85 2D CF 71 4A C4 5E A5 9B 8C F1 41 76  -G}.-.qJ.^....Av
0x0330: 78 D8 A1 4B 28 5C 2A D0 90 F1 70 B5 AE 32 3D A1  x..K(\*...p..2=.
0x0340: 41 8B C0 28 C0 BB 84 A6 CA 4E 87 22 E8 68 7F 15  A..(.....N.".h..
0x0350: E6 DE 08 32 3E 6B 4E B4 35 E7 FD C4 36 D2 10 CF  ...2>kN.5...6...
0x0360: 6D 54 CE 64 5D 98 31 4F 5E 73 D6 22 4E 38 7E AC  mT.d].1O^s."N8~.
0x0370: 33 97 CF F1 02 8B 12 06 2D 00 BC C4 E5 F2 7C 79  3.......-.....|y
0x0380: E7 43 C4 ED 55 CE CB 66 95 54 54 5F 3A E9 36 30  .C..U..f.TT_:.60
0x0390: 49 3B 9E 4C FB 84 2B A1 06 7F C4 AE 84 4F B5 5B  I;.L..+......O.[
0x03A0: 64 97 99 90 FF 66 0D C5 D5 1C DC F0 E5 4B 09 97  d....f.......K..
0x03B0: 3A 8D 11 6E 75 59 39 32 E4 AC BB C7 2C 29 25 E4  :..nuY92....,)%.
0x03C0: DC 7D 25 CC 3F EB 46 C8 36 10 13 E4 CE A6 2D 04  .}%.?.F.6.....-.
0x03D0: 47 FA 8F ED 43 CE 56 07 8D 62 9A 06 4B D7 36 56  G...C.V..b..K.6V
0x03E0: F6 06 4F 66 6C C8 79 33 9E 64 23 5A FF 90 C9 D0  ..Ofl.y3.d#Z....
0x03F0: C6 6F 05 8D DC 40 F2 E3 BC 75 0C EA 6C 22 25 B1  .o...@...u..l"%.
0x0400: E2 14 5C 16 27 EB 99 1E B0 94 9B F6 CA B7 BB 3D  ..\.'..........=
0x0410: 2C B0 EF EC 04 8E E6 45 D3 B3 3A 01 CF 29 33 8C  ,......E..:..)3.
0x0420: E0 B6 FB 86 2E 2C F9 47 16 61 F9 BC EB 91 ED DF  .....,.G.a......
0x0430: CA C5 F8 07 02 48                                .....H

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:59:34.884718 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26113 IpLen:20 DgmLen:760 DF
***AP*** Seq: 0x60F7DBC5  Ack: 0xDE6CECA2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760044256 926093359 
0x0000: 02 C8 85 B5 5A AA 02 89 23 51 E4 69 08 00 45 10  ....Z...#Q.i..E.
0x0010: 02 F8 66 01 40 00 40 06 59 20 0A 0A 51 56 0A 08  ..f.@.@.Y ..QV..
0x0020: 13 67 00 16 BC 5C 60 F7 DB C5 DE 6C EC A2 80 18  .g...\`....l....
0x0030: 01 D4 7B B9 00 00 01 01 08 0A 2D 4D 5A E0 37 33  ..{.......-MZ.73
0x0040: 10 2F 25 10 46 4B BF D9 C5 27 45 E1 E5 BD 2F 3F  ./%.FK...'E.../?
0x0050: F1 CE 40 10 7E FF 8E 97 E2 97 EC CC EC 5A 0C 2D  ..@.~........Z.-
0x0060: 37 94 1E 6A 1A 38 24 D3 A1 38 DE 8F 0E C7 7A C9  7..j.8$..8....z.
0x0070: 63 B8 99 7D 26 8D D1 88 44 00 89 EC 35 EC 12 9B  c..}&...D...5...
0x0080: 42 C6 C6 71 45 4E 70 4A 4C 97 13 D5 53 C1 25 48  B..qENpJL...S.%H
0x0090: C4 EF 32 94 EE 61 C9 8C B5 08 4A A5 02 53 AF F4  ..2..a....J..S..
0x00A0: 32 68 B2 AF 25 CE 5C 9B 5D E6 FD AC 9D F2 C3 96  2h..%.\.].......
0x00B0: F1 84 BD CE CC E7 27 E8 33 9B 29 95 CB C8 89 6D  ......'.3.)....m
0x00C0: DC DC F5 18 5D C7 C9 35 1E 92 DE FC 88 82 CC 04  ....]..5........
0x00D0: A8 3B E2 D7 F7 50 C7 18 D2 F5 2C ED 43 7D 11 96  .;...P....,.C}..
0x00E0: C8 B9 B6 B7 88 85 5F 8B 73 78 FC DC 44 23 84 0A  ......_.sx..D#..
0x00F0: F3 65 63 C9 42 20 D4 6D EA F6 7D A7 33 75 80 4F  .ec.B .m..}.3u.O
0x0100: E3 0A 7C 09 B3 2A A8 06 F9 69 EF 60 21 40 BC D8  ..|..*...i.`!@..
0x0110: 11 45 D8 A2 AC 9E CC A4 B9 BA B5 E9 87 72 AA E0  .E...........r..
0x0120: 77 01 8E 54 CA D4 B8 30 AC A8 0F 32 C6 87 10 21  w..T...0...2...!
0x0130: A7 FB C3 B7 96 9E 21 82 A2 46 54 B2 E2 B1 DF 51  ......!..FT....Q
0x0140: BF 86 8C 4F 96 D6 DD B1 C7 B3 29 30 EB 7B A0 4E  ...O......)0.{.N
0x0150: CB 7D 14 6A 9C BE 63 EA 7C 76 C4 CD AD 38 EE 23  .}.j..c.|v...8.#
0x0160: D8 53 5E 05 40 DA 43 F1 0F B8 18 FC 58 E6 AB 21  .S^.@.C.....X..!
0x0170: 1E 08 1B 23 C0 E1 07 F8 09 7D 7F 05 3F 2D AF 3D  ...#.....}..?-.=
0x0180: 90 C8 5A AD E1 72 B0 29 E1 0D 09 2A D8 EA 38 23  ..Z..r.)...*..8#
0x0190: F2 30 8D 93 6F A3 3A 1D B8 A5 E3 C1 26 58 C0 F4  .0..o.:.....&X..
0x01A0: CD 5E 66 16 C0 80 09 BC CF B0 23 AE AC C8 94 14  .^f.......#.....
0x01B0: CE 4B 73 23 00 57 E5 79 70 7D AD 3D 6F 41 84 53  .Ks#.W.yp}.=oA.S
0x01C0: A4 76 2F 0A BA 70 C7 61 3C A3 C2 E7 31 48 7A 8E  .v/..p.a<...1Hz.
0x01D0: A0 89 03 04 7D 79 DE B5 45 6F D5 EE A6 0B D0 F4  ....}y..Eo......
0x01E0: 75 1B 41 31 94 BC CF 24 AE 4A 87 57 66 88 58 C2  u.A1...$.J.Wf.X.
0x01F0: 7C 85 32 70 69 94 E9 E7 56 54 8C 9F 23 A3 BF C4  |.2pi...VT..#...
0x0200: AF 93 1A E6 87 2A D7 68 44 AB DA 6D B7 91 DC C2  .....*.hD..m....
0x0210: BB C9 75 74 AD 9E D7 DF E9 8B AD CD D3 BB B2 AA  ..ut............
0x0220: 03 E0 31 1E BE 91 41 74 29 24 C2 22 9C C3 95 94  ..1...At)$."....
0x0230: C1 CC 34 30 6A 02 41 57 CB 4D ED 07 73 F4 80 00  ..40j.AW.M..s...
0x0240: DB A1 0A F8 00 6E C4 9A F7 E6 84 4B 29 65 96 5B  .....n.....K)e.[
0x0250: F0 4A D2 F3 0B E0 4C 0C 6C F9 81 45 9B 39 EC 24  .J....L.l..E.9.$
0x0260: DC 7B BD 14 05 22 28 27 D7 44 78 AB 37 A3 DC FF  .{..."('.Dx.7...
0x0270: 11 2E D4 92 2D 25 DD 14 F1 2A F7 8E FE 7E 10 BE  ....-%...*...~..
0x0280: F9 E5 2B D8 96 4D 1F BC 53 2B C8 17 DF B4 42 97  ..+..M..S+....B.
0x0290: 7A 04 C8 C3 38 C6 BD C4 27 8E 21 04 A5 3F 22 25  z...8...'.!..?"%
0x02A0: F6 45 8F E9 70 4F F1 27 28 9C 5B 01 A0 72 6D 4D  .E..pO.'(.[..rmM
0x02B0: 17 98 54 F8 A5 F9 59 B3 BD 7C 16 11 DF 96 8F 49  ..T...Y..|.....I
0x02C0: 56 27 A9 46 CE 14 94 0E C6 8B A7 83 91 9C 04 2F  V'.F.........../
0x02D0: 49 A6 18 FA 73 1B D7 F2 7C 1B 21 78 63 BC 74 EE  I...s...|.!xc.t.
0x02E0: 34 FD FC FC 01 71 33 A4 1E B0 53 F4 5C 09 42 59  4....q3...S.\.BY
0x02F0: 25 91 11 FE 07 21 2B D6 2D 19 6A B8 5D AB 4F 24  %....!+.-.j.].O$
0x0300: C9 45 BF 4B 57 12                                .E.KW.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:59:34.884738 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26114 IpLen:20 DgmLen:508 DF
***AP*** Seq: 0x60F7DE89  Ack: 0xDE6CECA2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760044256 926093359 
0x0000: 02 C8 85 B5 5A AA 02 89 23 51 E4 69 08 00 45 10  ....Z...#Q.i..E.
0x0010: 01 FC 66 02 40 00 40 06 5A 1B 0A 0A 51 56 0A 08  ..f.@.@.Z...QV..
0x0020: 13 67 00 16 BC 5C 60 F7 DE 89 DE 6C EC A2 80 18  .g...\`....l....
0x0030: 01 D4 7A BD 00 00 01 01 08 0A 2D 4D 5A E0 37 33  ..z.......-MZ.73
0x0040: 10 2F 82 26 E3 2B CA B6 EF 44 5F B8 62 AE F0 89  ./.&.+...D_.b...
0x0050: 9A BA E9 E5 91 CA B0 34 04 C5 FD 08 CC 0B B3 5E  .......4.......^
0x0060: 32 68 F2 EC 71 55 35 5B 52 FD 0F 12 98 E8 BB 2F  2h..qU5[R....../
0x0070: 7F A1 B6 29 C9 17 CE BE 75 BC BA 90 07 B3 0D 29  ...)....u......)
0x0080: 53 35 05 EF 8E 68 AD F1 DA CA A0 9D 42 E6 3A A3  S5...h......B.:.
0x0090: F8 77 D8 89 40 CE B0 E5 3F A2 2E 1B 5E 20 1D B3  .w..@...?...^ ..
0x00A0: CE 92 42 00 38 68 6E 8E 44 C5 4A 15 55 8A E0 83  ..B.8hn.D.J.U...
0x00B0: 80 D9 FD 0F 65 B5 35 09 A8 A7 84 A7 CF A2 3E 78  ....e.5.......>x
0x00C0: D8 3E 57 E4 7B 45 41 6D 6A 16 3C 80 60 35 FD 14  .>W.{EAmj.<.`5..
0x00D0: BD C0 89 72 42 20 D7 E5 55 50 4A 31 FD 2D E1 B7  ...rB ..UPJ1.-..
0x00E0: D9 26 6F 70 26 63 6A 49 5A 28 DC 99 29 3D A2 89  .&op&cjIZ(..)=..
0x00F0: 4E CF FA B7 61 B2 54 49 3E 90 07 45 63 D6 77 6B  N...a.TI>..Ec.wk
0x0100: 2D 72 5B 47 27 A2 0B 99 98 31 1B 75 D6 56 09 BB  -r[G'....1.u.V..
0x0110: 9C 4B 8F 4A D5 EE E9 47 C2 F8 E2 62 B4 A2 36 DC  .K.J...G...b..6.
0x0120: 83 22 6B 2E 3C 37 B2 66 13 9F 3F 43 50 67 15 1B  ."k.<7.f..?CPg..
0x0130: 81 12 8F 84 3C 26 3B 9C E1 F9 5E 06 46 9C 39 D7  ....<&;...^.F.9.
0x0140: 1C 9D 50 1B DE C6 4B 99 C9 7B F9 09 D4 5A 53 78  ..P...K..{...ZSx
0x0150: D8 42 6D E5 0D 66 DA 48 2A 48 C2 A6 B2 3B 3F F8  .Bm..f.H*H...;?.
0x0160: 5A D4 18 9F B3 62 8F 4A 93 F4 E8 D7 B8 35 49 85  Z....b.J.....5I.
0x0170: 65 81 B0 97 40 6B 65 DD 7C 37 BE 73 9C FF D2 1E  e...@ke.|7.s....
0x0180: 79 D8 06 2D 38 2B 76 A7 31 91 DB 17 52 AC 99 E8  y..-8+v.1...R...
0x0190: 9F 80 53 83 EE 07 87 21 07 46 C8 03 80 86 2E A3  ..S....!.F......
0x01A0: 67 2C 29 37 2A D2 B7 45 7C 79 80 9F DF 04 63 4F  g,)7*..E|y....cO
0x01B0: 9D A5 DB C0 FE D1 F0 43 3D D7 25 B3 64 6B 0F 99  .......C=.%.dk..
0x01C0: 8B 94 83 02 75 51 E3 D2 9B CD 37 4A C0 C4 26 8F  ....uQ....7J..&.
0x01D0: BD B0 6F FA 58 22 0D DF F0 C5 08 46 FE 67 65 FE  ..o.X".....F.ge.
0x01E0: 9B FF 3D FB B4 AC 73 C3 C7 16 94 88 3D 8C 70 3A  ..=...s.....=.p:
0x01F0: F8 CB 0B C7 F6 B1 0A 90 24 6A D5 44 B1 8F 86 16  ........$j.D....
0x0200: B6 59 03 A0 7A F6 69 06 2D 24                    .Y..z.i.-$

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:59:34.884801 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26115 IpLen:20 DgmLen:1064 DF
***AP*** Seq: 0x60F7E051  Ack: 0xDE6CECA2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760044256 926093359 
0x0000: 02 C8 85 B5 5A AA 02 89 23 51 E4 69 08 00 45 10  ....Z...#Q.i..E.
0x0010: 04 28 66 03 40 00 40 06 57 EE 0A 0A 51 56 0A 08  .(f.@.@.W...QV..
0x0020: 13 67 00 16 BC 5C 60 F7 E0 51 DE 6C EC A2 80 18  .g...\`..Q.l....
0x0030: 01 D4 7C E9 00 00 01 01 08 0A 2D 4D 5A E0 37 33  ..|.......-MZ.73
0x0040: 10 2F 2F 74 2A 3E F5 2F F6 B0 A0 E1 3E A6 0C 3E  .//t*>./....>..>
0x0050: D8 46 47 CD 94 34 DA A4 C3 AF 28 16 57 F4 D4 9F  .FG..4....(.W...
0x0060: 67 50 9F 02 E5 CC 90 E1 65 67 2A B8 59 47 EC 86  gP......eg*.YG..
0x0070: F1 60 80 E4 91 F6 61 54 9E A0 7F 8C 91 63 E8 EA  .`....aT.....c..
0x0080: 45 08 91 7D A6 5C 18 46 27 B5 2D 11 13 A2 EA D3  E..}.\.F'.-.....
0x0090: 3D 5E B7 98 05 21 16 B1 8C 7D 3E 56 68 2E BB 4B  =^...!...}>Vh..K
0x00A0: 33 C5 14 E0 51 A6 95 1D B1 20 90 34 4C 50 27 91  3...Q.... .4LP'.
0x00B0: 49 61 A3 6F E5 71 C0 AF 91 33 F4 31 C0 C9 C2 78  Ia.o.q...3.1...x
0x00C0: 7B FB 6E B3 98 44 DC 42 7B 25 EE F3 DC 44 29 16  {.n..D.B{%...D).
0x00D0: 54 F2 12 51 AE 0E 2D 87 9F 06 26 5E 8B BF D2 01  T..Q..-...&^....
0x00E0: CE D1 CA 50 B1 0C B5 41 FD AC D3 42 BA CD C5 40  ...P...A...B...@
0x00F0: E6 FA 22 64 D9 5B 9B 80 B5 CF 5B 7E 7F 8F B4 9E  .."d.[....[~....
0x0100: 8F AE 9F 60 A8 45 C1 20 9F 39 38 BD BA A2 F8 75  ...`.E. .98....u
0x0110: A9 1C D6 4C A7 C9 E6 36 B3 3D 66 19 85 F8 26 BB  ...L...6.=f...&.
0x0120: F7 65 56 49 C3 5E B6 73 7A 92 72 A4 5A 6D D7 97  .eVI.^.sz.r.Zm..
0x0130: D4 C5 3E 93 30 17 6C 3B C5 48 43 B2 43 B1 D9 3E  ..>.0.l;.HC.C..>
0x0140: 13 0F C6 72 66 A4 C5 A6 E1 88 FF 90 58 EE 80 76  ...rf.......X..v
0x0150: 01 D5 B4 C1 9F 31 3B F5 29 14 0B E6 67 37 AF 21  .....1;.)...g7.!
0x0160: EC 48 EE 29 0E 0D C1 F3 6F 64 23 30 21 29 0D 4A  .H.)....od#0!).J
0x0170: D5 1B 9E 5A 40 A8 80 7B 08 35 D2 58 F8 04 58 B8  ...Z@..{.5.X..X.
0x0180: 0B 1A 9B 6C 42 A7 F3 0D 05 2D DE 2C C7 68 46 FE  ...lB....-.,.hF.
0x0190: 4E D8 1A 0B 1A 49 2F B2 B2 32 F3 CE 3E BA 41 95  N....I/..2..>.A.
0x01A0: DF 9A 41 A2 AE C8 77 B4 3E C2 9E A4 28 95 83 3E  ..A...w.>...(..>
0x01B0: B9 5A 7F 6A 2C 77 03 76 29 07 CC 60 22 63 DB F5  .Z.j,w.v)..`"c..
0x01C0: D0 FE 12 93 BC 11 E8 9F FA 0E EE 32 24 C4 3D 3D  ...........2$.==
0x01D0: 27 46 E8 EF 7F 96 8F A7 59 93 A6 36 F8 B5 B1 1E  'F......Y..6....
0x01E0: 5D 04 5A 6B 7F BB A1 0E EE 6F 4B 04 48 F6 BE 10  ].Zk.....oK.H...
0x01F0: 0B ED EB B9 56 32 7D E8 95 D0 4A 17 8F 64 9F 2D  ....V2}...J..d.-
0x0200: DC 04 D4 44 DC F5 6E 29 64 11 A1 43 43 74 FC 50  ...D..n)d..CCt.P
0x0210: B6 51 E6 2C FD 7A F2 6C D1 6E 92 0A CE 5E 55 FC  .Q.,.z.l.n...^U.
0x0220: 15 66 F3 36 13 55 19 B8 83 BB 98 47 D5 26 0F A2  .f.6.U.....G.&..
0x0230: 70 FA 31 CA 2C F5 30 BF 43 56 49 D0 61 A5 1D 59  p.1.,.0.CVI.a..Y
0x0240: 0C F5 93 2B 40 66 D2 A5 9E 68 0D 28 3E 20 5C 40  ...+@f...h.(> \@
0x0250: 4D E0 9E 46 54 17 54 EC 98 F4 B9 A7 60 7F DC 64  M..FT.T.....`..d
0x0260: 84 2A C2 1B BC 1F B8 79 E2 2D D6 0C E5 8D 25 50  .*.....y.-....%P
0x0270: ED A1 E4 10 92 3A C0 9B A4 01 00 42 1E CA 5E AD  .....:.....B..^.
0x0280: D1 A8 52 A7 A3 F7 F6 96 FE F2 76 A5 D4 A2 AF ED  ..R.......v.....
0x0290: 85 21 A7 CE 0C 9E 96 0C 72 C9 A4 CE A5 05 8A D8  .!......r.......
0x02A0: 71 8C 81 ED 72 F2 0F 0F 1E F0 DF B5 31 8F 80 DD  q...r.......1...
0x02B0: 7F FC 45 95 99 7E D6 D7 08 93 B8 75 52 E7 92 F2  ..E..~.....uR...
0x02C0: 9D 67 1A 31 26 7A 4A 4C 7D 08 FB 50 24 2D 55 FA  .g.1&zJL}..P$-U.
0x02D0: 96 76 4C F5 68 C9 6A E1 2D FF 40 EB F1 F1 2B D2  .vL.h.j.-.@...+.
0x02E0: D8 7F C8 15 6B 08 7B 5E 80 5C 7F D7 45 A2 1C D1  ....k.{^.\..E...
0x02F0: A3 FA 6B 78 B5 C9 3C A2 6B 9F 80 47 1D C1 35 45  ..kx..<.k..G..5E
0x0300: 6D 08 82 4D 40 D5 E1 63 B4 DD 05 D7 D3 A3 9F 22  m..M@..c......."
0x0310: 92 B7 70 9A 26 4F 98 2E 79 95 50 DE E7 15 9E 1E  ..p.&O..y.P.....
0x0320: 86 C6 9F 5A 83 9F E6 47 5E B3 5F 68 21 5E 95 BD  ...Z...G^._h!^..
0x0330: 57 FE 93 48 F7 4F 8F FC FF 8E 7E A4 4C 3D 85 99  W..H.O....~.L=..
0x0340: DC 12 B1 04 71 8A 02 DD 11 A6 82 F5 89 51 9F 94  ....q........Q..
0x0350: 27 0B 45 B3 10 B7 0B 8D C8 D0 61 30 FA FF 35 D9  '.E.......a0..5.
0x0360: 1B 96 A7 9A C9 5A 04 11 65 AF 41 7D 49 90 52 FE  .....Z..e.A}I.R.
0x0370: 74 8A 3F C9 6F E5 05 FD 18 8A DE BE 1D F4 FE 69  t.?.o..........i
0x0380: BA DD EC 39 06 D6 E1 B4 D6 6C 6D B9 F1 5C 2D 18  ...9.....lm..\-.
0x0390: 96 1B 6C 9C 81 26 22 D7 9F D7 35 A0 F0 78 A4 E7  ..l..&"...5..x..
0x03A0: F7 2C 12 3B 66 03 02 2F 68 BE 21 34 02 42 A5 72  .,.;f../h.!4.B.r
0x03B0: 5F 3C C9 35 76 57 5E 80 10 C2 21 3B B3 7A 63 B5  _<.5vW^...!;.zc.
0x03C0: 30 C6 31 95 07 BC 7D 1D 87 CF 01 DF 9E 73 2C AD  0.1...}......s,.
0x03D0: 0C 8F 6F F6 B8 2B 65 79 1E 2D 06 F4 56 E8 E6 10  ..o..+ey.-..V...
0x03E0: CD 41 95 EC B1 C5 9C 92 1F 4A 30 5C 1E 41 E6 05  .A.......J0\.A..
0x03F0: 60 B4 07 F9 BC 92 89 20 BC FE 3A 8D 2C 82 42 93  `...... ..:.,.B.
0x0400: 66 50 11 9C 9C 90 18 72 AD 33 19 AD 4D 06 F0 59  fP.....r.3..M..Y
0x0410: 19 4E BF E4 69 F1 91 00 FE E9 7F 06 75 33 10 C0  .N..i.......u3..
0x0420: 77 61 55 8E 3B BB 08 AC 7D 5D C0 A2 C7 72 0F 6B  waU.;...}]...r.k
0x0430: 89 8A 29 A9 B4 70                                ..)..p

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:59:34.884857 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26116 IpLen:20 DgmLen:1252 DF
***AP*** Seq: 0x60F7E445  Ack: 0xDE6CECA2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760044256 926093359 
0x0000: 02 C8 85 B5 5A AA 02 89 23 51 E4 69 08 00 45 10  ....Z...#Q.i..E.
0x0010: 04 E4 66 04 40 00 40 06 57 31 0A 0A 51 56 0A 08  ..f.@.@.W1..QV..
0x0020: 13 67 00 16 BC 5C 60 F7 E4 45 DE 6C EC A2 80 18  .g...\`..E.l....
0x0030: 01 D4 7D A5 00 00 01 01 08 0A 2D 4D 5A E0 37 33  ..}.......-MZ.73
0x0040: 10 2F 01 56 E3 03 5B 5E 52 99 75 E4 81 B8 E9 A7  ./.V..[^R.u.....
0x0050: 57 23 32 2C E4 D1 80 AF FA 5D CA B2 39 BD 9A C8  W#2,.....]..9...
0x0060: B6 6B 3E D9 26 AD 25 0F 98 EC D3 8E CB 19 F8 25  .k>.&.%........%
0x0070: F7 00 BD 35 E9 FB 0E A3 84 D7 BC 57 4C 33 66 52  ...5.......WL3fR
0x0080: CD 2D 59 3B 24 8A B6 9E CC E9 A4 60 A1 6A 3E C3  .-Y;$......`.j>.
0x0090: 12 A1 6F 27 14 72 59 49 5F E2 2F F0 09 49 C3 C2  ..o'.rYI_./..I..
0x00A0: 5C F7 D8 80 E9 E2 F6 1D 1F 65 7D 14 C9 7F AF 37  \........e}....7
0x00B0: 46 67 FE 83 A0 1F E1 39 85 F2 12 07 B0 83 A6 06  Fg.....9........
0x00C0: 8F 04 0D 75 FA 2B 8C 3D 72 F8 1C 25 DB 7B 27 FD  ...u.+.=r..%.{'.
0x00D0: 4A 90 6D 0E 2D 86 5A 8F 3C A6 AB F0 9A B7 FB B0  J.m.-.Z.<.......
0x00E0: A6 8D E7 3B 05 1A 9E B8 C1 20 9C A7 05 2C F6 A7  ...;..... ...,..
0x00F0: A8 56 43 00 30 28 96 B6 F1 67 C9 F6 8D 5A F7 A0  .VC.0(...g...Z..
0x0100: 99 E7 B5 3A FF 89 24 D0 C1 38 61 0A 93 2E 42 56  ...:..$..8a...BV
0x0110: 56 CB E3 87 82 08 CF 75 B7 8F A7 F5 EF 1A C1 E0  V......u........
0x0120: 84 C2 E9 0F 21 E0 05 E0 77 77 1B 05 23 6A 47 6A  ....!...ww..#jGj
0x0130: BF 6D 32 72 13 ED 4D FC 6D ED 33 2B 13 66 89 41  .m2r..M.m.3+.f.A
0x0140: 34 1F 19 F3 ED CB 29 15 7A AE 67 1B 36 0A 28 B4  4.....).z.g.6.(.
0x0150: 0D 06 50 56 12 02 30 AA E9 D0 51 87 3C 76 0B 36  ..PV..0...Q.<v.6
0x0160: 8D 5B E7 EA 7E AC 6F 21 EB 13 A7 92 4F CC 9B 69  .[..~.o!....O..i
0x0170: 4F 27 66 69 22 D3 41 18 C1 0B A9 74 B7 EA 0B 26  O'fi".A....t...&
0x0180: E9 02 D2 AC 17 28 65 9E 8B 1A 89 75 8E 04 76 45  .....(e....u..vE
0x0190: BA D2 40 7C E6 5E 9C 3F 33 1A 6C 8F 63 46 D1 BE  ..@|.^.?3.l.cF..
0x01A0: D7 68 00 96 CB 1B B9 0F 79 22 23 AE BF 58 C9 75  .h......y"#..X.u
0x01B0: C3 30 AA AD D1 B9 7F DF A8 78 EC 3C D4 F1 AF 82  .0.......x.<....
0x01C0: 4A D4 0D 89 93 7F 1D 77 A8 28 EE A9 8D 82 8C CB  J......w.(......
0x01D0: D5 39 5B 0F C7 66 F1 B9 1C 99 DE 0F 0B 4E 0C FA  .9[..f.......N..
0x01E0: 1C F2 4B DD 13 16 4D 0E BC 42 A8 31 D5 79 3C 53  ..K...M..B.1.y<S
0x01F0: B9 15 C4 77 9A 83 97 91 92 EF 97 04 4F 87 DD A0  ...w........O...
0x0200: 99 CF 44 59 69 B2 02 E5 C4 3C AB 0B C2 DF 39 13  ..DYi....<....9.
0x0210: 83 80 34 B0 20 29 B2 DF 6F D7 8D 0C E1 1B EE FC  ..4. )..o.......
0x0220: 35 05 E0 DC ED 1D 37 AC 90 30 C1 CD B3 6A CC EC  5.....7..0...j..
0x0230: A2 9C D1 01 CA 89 53 29 D6 7C 15 CE A8 D7 0F FF  ......S).|......
0x0240: B7 C9 8C 21 4E 2F 5D 6C 52 29 29 43 B5 D3 E5 07  ...!N/]lR))C....
0x0250: 3D A6 FC 03 07 1E 6C F6 54 72 42 87 06 62 41 67  =.....l.TrB..bAg
0x0260: 86 5B BD 9F 87 CC 85 BA 6D 85 E7 9D 13 B0 8B BF  .[......m.......
0x0270: C4 E8 4E 84 F4 35 DF 3B 41 96 41 5B 68 8E F3 76  ..N..5.;A.A[h..v
0x0280: 60 D5 57 EA 93 53 2D 11 B6 96 B9 9E 05 A7 6D 06  `.W..S-.......m.
0x0290: C6 BF 44 41 A2 E0 FD 4C E1 E0 D3 5A F5 4F 4E F7  ..DA...L...Z.ON.
0x02A0: 2F BB 45 6D BC A6 7B 91 D9 5E B6 4C 9F F8 DA FB  /.Em..{..^.L....
0x02B0: 97 3B C6 7E 1F 27 76 35 FD 79 E0 2A 60 B1 CC D0  .;.~.'v5.y.*`...
0x02C0: AC C7 2E C9 9A 2E E3 46 8F 4B 56 35 4B 9D A6 85  .......F.KV5K...
0x02D0: 71 DA 11 C9 F0 EC 2C FD 43 8B E7 23 14 75 64 AD  q.....,.C..#.ud.
0x02E0: CC BF 5D 1A 57 88 30 4F B9 75 37 17 4D DD 64 E7  ..].W.0O.u7.M.d.
0x02F0: 5A C4 A2 2B 79 04 1F E5 B1 EB 9C 23 A3 3D DD 0A  Z..+y......#.=..
0x0300: 71 33 18 6B 2D 85 67 31 A3 1A 6E D1 6F BC 60 C0  q3.k-.g1..n.o.`.
0x0310: A5 A8 5A ED 02 93 B7 B6 0E 12 20 B3 1F 25 73 76  ..Z....... ..%sv
0x0320: 67 78 7B F0 F4 BE 5C 99 BF 4E 14 D7 C5 F0 B1 70  gx{...\..N.....p
0x0330: 01 4E 2B 3D 40 1A 04 06 D2 53 55 61 FC 0C 1A 26  .N+=@....SUa...&
0x0340: B8 C7 37 4A 77 8F 3A B2 40 32 2C F7 DD 3E D6 82  ..7Jw.:.@2,..>..
0x0350: 74 CB 3B 76 2C CB 69 C5 0C 41 06 04 7A 5C 26 3B  t.;v,.i..A..z\&;
0x0360: 37 F4 AC 0D C4 E0 E1 17 1A 22 18 4D 06 18 38 71  7........".M..8q
0x0370: A1 D3 7B 83 37 21 19 B8 8C 47 69 6D 96 24 B3 8D  ..{.7!...Gim.$..
0x0380: F0 46 4E 75 01 2D 88 9A 33 6B EC E0 3A FD EC A1  .FNu.-..3k..:...
0x0390: 0E C1 65 B7 57 DF 8F 9F 54 82 04 3F A8 2D 58 00  ..e.W...T..?.-X.
0x03A0: C2 BB E2 3E 6D ED 82 90 47 16 E5 86 F3 E3 CE F5  ...>m...G.......
0x03B0: 50 E2 5A FE 8F BE C0 F3 3C DF DF 47 6C 26 43 44  P.Z.....<..Gl&CD
0x03C0: 1C E6 76 9C 0B 8C B2 0F EA 85 14 7B 59 F3 C5 1E  ..v........{Y...
0x03D0: 2D 28 82 63 BB 65 91 DC A9 66 65 D8 AD 48 25 3F  -(.c.e...fe..H%?
0x03E0: 31 E4 09 04 44 5A 22 24 BB 20 C5 50 B8 F5 D8 21  1...DZ"$. .P...!
0x03F0: 3E D0 E3 44 54 EE 91 92 91 3D 04 30 CC 06 C3 63  >..DT....=.0...c
0x0400: AC C5 E3 20 10 12 3F 65 2B A5 86 C0 DB 6D 2A F4  ... ..?e+....m*.
0x0410: 85 E2 5C B9 62 C8 AF 85 EA 95 3C 08 CD 9F 76 57  ..\.b.....<...vW
0x0420: 08 1D 81 A7 33 F2 FA 11 38 49 17 DF B1 FD BC 14  ....3...8I......
0x0430: 5E 83 A4 13 1E 8D BB D0 97 D6 50 D0 C4 A6 B2 77  ^.........P....w
0x0440: 7C DD 81 B4 D3 BF 78 21 5B 25 8A E7 B5 9E 49 E0  |.....x![%....I.
0x0450: 63 AE B4 F9 29 06 EE ED BE D8 F5 03 9A 4F 60 E1  c...)........O`.
0x0460: 24 36 74 B8 53 7D 09 34 D0 10 52 A4 21 43 B0 CB  $6t.S}.4..R.!C..
0x0470: 27 BA 2F 1A AE 66 F7 B0 09 DC 82 15 43 AA A5 2A  './..f......C..*
0x0480: A7 59 EF 5F 39 49 F7 0C 90 CD CE 29 F5 00 41 33  .Y._9I.....)..A3
0x0490: 8B B5 2E D3 76 24 4E 00 C4 32 2C 88 A2 9D 52 82  ....v$N..2,...R.
0x04A0: BB 87 B8 AD 82 D9 4A 69 4C 7D 38 7E 49 1B B5 FA  ......JiL}8~I...
0x04B0: DD 7A 86 8F EE F6 88 C6 42 C7 D4 AA 80 48 80 B8  .z......B....H..
0x04C0: 2C 9C 12 D5 69 1C 55 48 92 A0 72 E0 A5 40 B1 CE  ,...i.UH..r..@..
0x04D0: F4 B3 4E BD 06 38 57 95 49 FA D6 2C DC 90 2B 31  ..N..8W.I..,..+1
0x04E0: 28 8B 43 5A 85 B0 CC 28 42 BF CA B6 A3 46 AE FB  (.CZ...(B....F..
0x04F0: 6D 37                                            m7

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:59:34.884918 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26117 IpLen:20 DgmLen:1108 DF
***AP*** Seq: 0x60F7E8F5  Ack: 0xDE6CECA2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760044256 926093359 
0x0000: 02 C8 85 B5 5A AA 02 89 23 51 E4 69 08 00 45 10  ....Z...#Q.i..E.
0x0010: 04 54 66 05 40 00 40 06 57 C0 0A 0A 51 56 0A 08  .Tf.@.@.W...QV..
0x0020: 13 67 00 16 BC 5C 60 F7 E8 F5 DE 6C EC A2 80 18  .g...\`....l....
0x0030: 01 D4 7D 15 00 00 01 01 08 0A 2D 4D 5A E0 37 33  ..}.......-MZ.73
0x0040: 10 2F 85 0F 21 A3 C6 E2 32 ED 6E 6D 00 78 D5 E5  ./..!...2.nm.x..
0x0050: 05 3B 7D 64 1A 68 D2 61 59 A6 15 84 C7 BF DC 25  .;}d.h.aY......%
0x0060: 54 94 3A 53 BE D5 25 01 77 59 66 18 39 D4 B3 A8  T.:S..%.wYf.9...
0x0070: 31 54 DB A1 B9 FD B9 E5 82 38 9F 06 8A 7E 55 B1  1T.......8...~U.
0x0080: CA 8A B3 76 33 AF AF DE 7D CC A4 13 8C 16 A4 9E  ...v3...}.......
0x0090: F5 3A 46 01 21 1A 3B 75 7C 8C CF D1 77 91 49 A9  .:F.!.;u|...w.I.
0x00A0: 28 BC BE 2C 07 69 60 13 2D 69 BC 2B AE 96 64 4C  (..,.i`.-i.+..dL
0x00B0: 98 83 DF 00 98 D0 E8 86 AE F9 5A DE 63 26 07 9C  ..........Z.c&..
0x00C0: 61 6B FE 6B E5 B7 D7 AD A9 45 C1 93 1D AC 44 13  ak.k.....E....D.
0x00D0: EB 53 D4 5E EC FB 60 13 EB B4 AF 3D 66 14 0F FD  .S.^..`....=f...
0x00E0: 4B 2E 8E 87 32 2A 4C 1C 8F E1 28 AC 0C 19 1F FF  K...2*L...(.....
0x00F0: 16 55 64 A9 9E 84 DD 04 F8 07 4C BB 76 87 47 99  .Ud.......L.v.G.
0x0100: E5 38 64 3F 76 14 33 8D 0C F4 7B 72 D2 63 92 7C  .8d?v.3...{r.c.|
0x0110: 19 1F 59 5C 81 F8 E9 7C 08 FB C5 42 CB C3 27 F3  ..Y\...|...B..'.
0x0120: C0 E4 96 D9 FD 05 80 6A 20 3E 5F 2B 36 30 3E 56  .......j >_+60>V
0x0130: 99 85 00 7B F4 04 DF 09 0D EB E2 AB 1C 01 6A FA  ...{..........j.
0x0140: D2 E8 58 FA 97 18 2E 47 1A 08 D6 66 8D 7E 49 75  ..X....G...f.~Iu
0x0150: 7B A2 59 32 DD BF 70 35 91 DC BF 1D 0E 7B 2F 44  {.Y2..p5.....{/D
0x0160: D2 E3 EE BD 91 C0 01 3A C1 95 3C E0 67 4E EF 87  .......:..<.gN..
0x0170: F3 1D 90 6A B0 8E 07 C9 75 FB B5 8B EC 06 5A D1  ...j....u.....Z.
0x0180: 9F FB 26 0F 97 3E 11 D9 C6 C6 39 79 D8 05 47 CA  ..&..>....9y..G.
0x0190: 4D 93 48 E9 76 AC AD 90 09 86 16 A4 7A 76 2C 7A  M.H.v.......zv,z
0x01A0: 24 7D E8 28 BF 23 7A A4 9C 80 C0 CE 92 5F E7 FE  $}.(.#z......_..
0x01B0: 16 54 DE A4 47 16 92 D7 B2 54 6D AD 23 E4 CE FF  .T..G....Tm.#...
0x01C0: 24 4C F8 59 4E B5 26 03 20 9C D6 D3 A6 09 27 93  $L.YN.&. .....'.
0x01D0: F3 6C 92 F7 61 8D 53 5C A1 C7 90 B2 B5 9F 2C 37  .l..a.S\......,7
0x01E0: E1 85 A0 7C 1F 1A B7 85 05 CD FB D8 0E 67 F1 A2  ...|.........g..
0x01F0: D4 7F 95 8B D9 DB 50 1F 9C 93 92 A5 96 26 D2 0C  ......P......&..
0x0200: 35 35 B8 3D E7 06 85 4F 01 36 68 BC F0 77 5F 4B  55.=...O.6h..w_K
0x0210: 5C F3 06 48 19 FB 83 9E 3F DF 84 A0 40 C9 6B A9  \..H....?...@.k.
0x0220: C7 B3 08 CF 60 DB 1F AC 1F 52 1B B9 A0 60 6F 5E  ....`....R...`o^
0x0230: F6 88 AC AB FD 56 76 0B 43 27 B9 CB 00 8F 0A F9  .....Vv.C'......
0x0240: F8 6D D9 AC 98 24 92 CD 47 CF 3D A3 12 A3 7F F9  .m...$..G.=.....
0x0250: 40 81 1D 51 3D 13 5B AD 65 81 9D 5C B2 1B E6 0D  @..Q=.[.e..\....
0x0260: CD 33 E7 DB B0 55 E7 D5 4D F4 03 C3 FA D7 70 59  .3...U..M.....pY
0x0270: 05 5A 56 17 9C CF F1 6A C2 66 81 69 EF CA 34 B6  .ZV....j.f.i..4.
0x0280: 36 5A 05 E0 31 64 6A 3E A8 26 F4 7C 7D A0 0E 99  6Z..1dj>.&.|}...
0x0290: 31 6D CE D5 43 24 5E 37 53 6A 21 A3 66 D8 C2 4C  1m..C$^7Sj!.f..L
0x02A0: 57 F0 54 C3 20 F8 B0 AB D6 5A 83 4B 8A B1 8F FA  W.T. ....Z.K....
0x02B0: 4C E3 5B C6 BB DA 8B 2B 88 25 0A 73 4D 48 8C 7F  L.[....+.%.sMH..
0x02C0: A1 7C 7D 30 C5 A4 B2 AF 22 2A 5D 9E 5C 8D 92 0F  .|}0...."*].\...
0x02D0: C0 7A 59 EF 9E 51 FA ED E5 D2 11 61 2F C8 22 69  .zY..Q.....a/."i
0x02E0: 24 BC 65 7A 2E 1D D8 7A 6C BF AC 66 30 43 EE 47  $.ez...zl..f0C.G
0x02F0: D9 E1 C3 17 13 F8 95 1A D4 BA 43 2F 2F B4 19 48  ..........C//..H
0x0300: CC 83 EE 03 90 F4 66 95 68 90 68 36 3D 4F D3 79  ......f.h.h6=O.y
0x0310: 0F E6 35 27 B3 4B 1A 51 3E 3F DC B3 37 DE 31 21  ..5'.K.Q>?..7.1!
0x0320: 61 CA 9D F2 09 68 CA 8C AE 75 71 CB 54 7C 49 26  a....h...uq.T|I&
0x0330: 21 81 7C 04 7A 41 16 1B 56 BA E9 46 5A D1 8A 22  !.|.zA..V..FZ.."
0x0340: 8F EA 8F 63 4B 9C 5B 89 6F 8B 8A BF 8A 69 58 E4  ...cK.[.o....iX.
0x0350: 66 6D A9 FC 02 9E 9D 5F 65 13 12 52 FE 41 28 C1  fm....._e..R.A(.
0x0360: 9F D8 4C F5 63 32 81 4D E4 CA A0 31 71 6A C3 C1  ..L.c2.M...1qj..
0x0370: 99 2C D0 22 3E F6 1D 09 85 97 1E 1E B3 6F 2D 73  .,.">........o-s
0x0380: 3B 69 EC 10 D9 8D D7 8F D6 E0 CE BB 41 0F FE 10  ;i..........A...
0x0390: 88 28 FD EF 0D 0F B2 FD 10 C7 38 44 CA 0A 3C 1B  .(........8D..<.
0x03A0: E8 AE DB 31 BF 14 99 38 A7 D8 3A 71 4A D3 F8 41  ...1...8..:qJ..A
0x03B0: 81 E7 D2 F2 7E 8E F7 71 A8 C1 D7 6D 24 4E 4A 15  ....~..q...m$NJ.
0x03C0: F9 DA 1B C4 6E 2F 4F 79 B9 7B 38 AD F8 D6 8F AE  ....n/Oy.{8.....
0x03D0: 16 06 56 FB 07 96 8D CE D5 E0 D1 98 79 A2 24 6A  ..V.........y.$j
0x03E0: 60 DD AD D7 0E 54 52 AC 80 3F 30 51 47 0F 36 FE  `....TR..?0QG.6.
0x03F0: 75 55 60 B6 87 B9 FB 14 E1 4C A8 50 D2 D6 CA DB  uU`......L.P....
0x0400: 19 75 A3 81 BD CA C6 D5 E9 A7 35 55 2A 43 C6 46  .u........5U*C.F
0x0410: A8 4C E3 3A 9B 53 A1 87 B2 90 67 EE 0A C6 F4 EA  .L.:.S....g.....
0x0420: AA 83 C0 B6 24 79 B1 25 93 76 6E 3A A6 48 1F 9C  ....$y.%.vn:.H..
0x0430: 6D 10 B7 C2 5B 6E 2C CA A1 4F 5A 9F 6E 9D FF 9B  m...[n,..OZ.n...
0x0440: 96 E9 EE EC D6 15 DC 8A 07 E7 A0 D1 EC 44 A5 42  .............D.B
0x0450: 4F CA A3 98 2B D5 92 3E 17 2B 13 50 5A E5 E2 1F  O...+..>.+.PZ...
0x0460: 43 4C                                            CL

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:59:34.884979 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26118 IpLen:20 DgmLen:580 DF
***AP*** Seq: 0x60F7ED15  Ack: 0xDE6CECA2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760044256 926093359 
0x0000: 02 C8 85 B5 5A AA 02 89 23 51 E4 69 08 00 45 10  ....Z...#Q.i..E.
0x0010: 02 44 66 06 40 00 40 06 59 CF 0A 0A 51 56 0A 08  .Df.@.@.Y...QV..
0x0020: 13 67 00 16 BC 5C 60 F7 ED 15 DE 6C EC A2 80 18  .g...\`....l....
0x0030: 01 D4 7B 05 00 00 01 01 08 0A 2D 4D 5A E0 37 33  ..{.......-MZ.73
0x0040: 10 2F 48 A9 F6 6C 7B 18 25 27 F0 91 41 14 92 11  ./H..l{.%'..A...
0x0050: 87 F6 6A A4 4C 9C D7 28 99 A7 CC D9 30 49 74 39  ..j.L..(....0It9
0x0060: B6 61 C4 F0 BA 0B 78 7C AC C6 CF 38 5F 9B EC 7C  .a....x|...8_..|
0x0070: DE 9E 4D 0C 20 3A DA C7 C5 4B 8D 84 39 BF FD B0  ..M. :...K..9...
0x0080: C9 C6 62 76 84 58 DA 6F 2F 19 CA 23 C3 9C 24 1E  ..bv.X.o/..#..$.
0x0090: B2 18 87 EA 03 97 C5 CA A2 06 4A F3 32 0A A8 6A  ..........J.2..j
0x00A0: 8C 57 EC B2 9D FE CC 24 F4 BD 42 C2 4B B0 09 37  .W.....$..B.K..7
0x00B0: 59 46 69 50 CC 7C F3 9A 7E B8 72 B9 43 CB 14 EF  YFiP.|..~.r.C...
0x00C0: 4A 8C D4 A7 9A 17 BB B1 86 3C 1D 1E BC 5A 86 A5  J........<...Z..
0x00D0: 90 9B A6 AD 0A 48 95 CF DC B9 C7 67 A4 E8 5F 28  .....H.....g.._(
0x00E0: 34 75 BE 0A 6C FC A4 A2 52 A0 8A 85 25 ED DA CE  4u..l...R...%...
0x00F0: 9D BD 07 89 D6 85 08 54 65 76 F1 32 01 15 AF 8F  .......Tev.2....
0x0100: 80 5B 4A 77 BB 87 C7 FD 93 3E 1F 1D E8 14 25 DA  .[Jw.....>....%.
0x0110: 46 7C B5 B5 E4 6F 2F 42 0E 58 04 90 13 91 11 21  F|...o/B.X.....!
0x0120: FE 6F A5 42 8B EF 8D D2 26 53 0D D5 7D 88 9B F4  .o.B....&S..}...
0x0130: 26 38 2D 15 BC F2 86 D6 9E C1 9C 36 01 F4 12 A5  &8-........6....
0x0140: 8E 74 F8 F0 9A 90 24 87 53 4E 42 18 5A 21 D6 46  .t....$.SNB.Z!.F
0x0150: F9 B5 AD 44 BB 08 2C 44 BE 3E 0F 87 8B 23 14 EF  ...D..,D.>...#..
0x0160: 68 4B F0 F5 73 F6 FD 5A 4D 34 13 61 AF 39 10 79  hK..s..ZM4.a.9.y
0x0170: E7 BA BD 2E 94 A4 52 41 FD B2 EB 0F 8B 1E 6B A3  ......RA......k.
0x0180: 76 B7 88 9B DA E2 0C 84 33 AA 68 9F 58 41 0C 62  v.......3.h.XA.b
0x0190: 9E 6D 29 92 9A B2 37 F8 E6 4E 42 55 0E D7 F4 4E  .m)...7..NBU...N
0x01A0: A6 F0 45 AB 72 F8 EC D0 47 4B 2A BB D1 4E 58 70  ..E.r...GK*..NXp
0x01B0: 6D 8A B4 1C 3B A8 6D B0 DF A5 B3 EE 74 9E 7F 92  m...;.m.....t...
0x01C0: A5 8A 74 1E DC 70 AB 20 0F 1C 6A 1C 7E DB 44 D9  ..t..p. ..j.~.D.
0x01D0: DA 0D 93 88 D7 97 BA 70 47 67 F6 32 ED 59 41 FF  .......pGg.2.YA.
0x01E0: 1C 33 79 2C 93 03 EF 6F FD CF B9 08 06 4A 67 0A  .3y,...o.....Jg.
0x01F0: 27 36 85 49 8A D6 35 F0 CA 21 3A FA 9D 50 D6 33  '6.I..5..!:..P.3
0x0200: E2 7F AC CD 16 CC 99 EA 33 AF 34 73 B9 8B 0F FA  ........3.4s....
0x0210: C6 A9 80 36 0F 96 2D 59 F8 45 93 1A 31 59 DF 2E  ...6..-Y.E..1Y..
0x0220: 3A C9 F6 E5 1F C5 C3 90 C7 76 88 CC CB 99 E0 A0  :........v......
0x0230: 95 4E 23 C5 A1 0A 69 E4 89 C7 FF 65 B6 89 50 45  .N#...i....e..PE
0x0240: 1A 9F 99 4C CA 90 E8 3F DF CC 8A 32 BC FA E0 CC  ...L...?...2....
0x0250: 59 FB                                            Y.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-18:59:34.885058 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26119 IpLen:20 DgmLen:456 DF
***AP*** Seq: 0x60F7EF25  Ack: 0xDE6CECA2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760044256 926093359 
0x0000: 02 C8 85 B5 5A AA 02 89 23 51 E4 69 08 00 45 10  ....Z...#Q.i..E.
0x0010: 01 C8 66 07 40 00 40 06 5A 4A 0A 0A 51 56 0A 08  ..f.@.@.ZJ..QV..
0x0020: 13 67 00 16 BC 5C 60 F7 EF 25 DE 6C EC A2 80 18  .g...\`..%.l....
0x0030: 01 D4 7A 89 00 00 01 01 08 0A 2D 4D 5A E0 37 33  ..z.......-MZ.73
0x0040: 10 2F 8A D9 8B 05 1E 56 83 F8 31 C2 79 55 B1 B2  ./.....V..1.yU..
0x0050: E9 4F 22 D6 8D 06 F7 B5 BB 04 5E DD 1D 20 C5 7B  .O".......^.. .{
0x0060: 7F A2 D4 BF 62 FF 8D A5 28 C3 3C B0 35 E1 D0 E3  ....b...(.<.5...
0x0070: 47 F2 EA 2D 8C CC 6F 9C 95 47 E1 E0 07 9D 7D 6E  G..-..o..G....}n
0x0080: A1 83 B3 E5 A6 8C 22 73 4D 2D 71 52 9F 59 C6 A1  ......"sM-qR.Y..
0x0090: 7A 9F 4B 6A 39 72 83 51 65 3C AA 18 7E 7B 4B 80  z.Kj9r.Qe<..~{K.
0x00A0: 69 DD FF 4A 18 5E 9F 24 A7 02 72 67 6C E7 AC E0  i..J.^.$..rgl...
0x00B0: 39 B4 01 BB 05 9E 07 A9 10 7F 21 24 10 17 1F B2  9.........!$....
0x00C0: 0D 72 5D AA 32 AA 73 D3 BE F8 5B C7 ED 33 53 37  .r].2.s...[..3S7
0x00D0: 03 E3 1F EE 7E 77 0F 4C EC 18 23 6A 6E 46 EF 4A  ....~w.L..#jnF.J
0x00E0: 89 45 88 FC CB 6C B1 DA 7A 51 FF 28 01 B8 AC A4  .E...l..zQ.(....
0x00F0: 3A D8 50 D1 12 0C 2A 34 3A EB EF FB BE F9 B9 BE  :.P...*4:.......
0x0100: 50 E4 BB 6E 65 35 0B 30 F0 C9 05 FE D4 2F 23 DD  P..ne5.0...../#.
0x0110: 29 BD CC DA E7 E3 4E F9 1F 84 01 9B 66 68 40 42  ).....N.....fh@B
0x0120: E3 8A 69 85 6E 1C FE B7 02 FB FF 18 AE A2 AC 5B  ..i.n..........[
0x0130: 60 4D E5 74 8B D5 68 29 4B 0D 0A 28 C4 31 67 FD  `M.t..h)K..(.1g.
0x0140: 6E EA 6B B2 DC 6A 2F 84 19 44 59 4A 06 D8 5A 80  n.k..j/..DYJ..Z.
0x0150: 6E A5 2F 44 19 44 0D 36 33 CC 43 59 BB 9F 3A 84  n./D.D.63.CY..:.
0x0160: 3B 0F E4 5B 48 D7 1B 01 92 BE 48 E2 3B 80 CD FF  ;..[H.....H.;...
0x0170: 54 BF D0 DA B5 30 6B 28 57 EE 7D 1F DD 86 F6 4B  T....0k(W.}....K
0x0180: D9 F7 26 1C 39 83 1C AB 1D 37 E2 06 27 E0 FB 50  ..&.9....7..'..P
0x0190: 43 55 11 35 21 AA 02 0E 6B 3D 58 EF 42 76 0C 76  CU.5!...k=X.Bv.v
0x01A0: 78 5C 43 40 5F 3E 07 78 C4 2D BB 80 18 F0 62 94  x\C@_>.x.-....b.
0x01B0: 0C AF 6A 8D 84 A9 60 5F 02 6B C0 72 2D 94 07 B6  ..j...`_.k.r-...
0x01C0: 38 B4 81 C1 62 0A 5A FE 73 A6 E6 A5 BE 77 F8 2D  8...b.Z.s....w.-
0x01D0: BB C0 79 22 57 CA                                ..y"W.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:35.089019 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32348 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7D475  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926094372 760044255 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 5C 40 00 3F 06 44 89 0A 08 13 67 0A 0A  .4~\@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 D4 75 80 10  QV.\...l..`..u..
0x0030: 01 F5 6B 86 00 00 01 01 08 0A 37 33 14 24 2D 4D  ..k.......73.$-M
0x0040: 5A DF                                            Z.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:35.089019 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32349 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7D7D1  Win: 0x1F2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926094372 760044256 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 5D 40 00 3F 06 44 88 0A 08 13 67 0A 0A  .4~]@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 D7 D1 80 10  QV.\...l..`.....
0x0030: 01 F2 68 2C 00 00 01 01 08 0A 37 33 14 24 2D 4D  ..h,......73.$-M
0x0040: 5A E0                                            Z.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:35.089019 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32350 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7DBC5  Win: 0x1EB  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926094373 760044256 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 5E 40 00 3F 06 44 87 0A 08 13 67 0A 0A  .4~^@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 DB C5 80 10  QV.\...l..`.....
0x0030: 01 EB 64 3E 00 00 01 01 08 0A 37 33 14 25 2D 4D  ..d>......73.%-M
0x0040: 5A E0                                            Z.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:35.089019 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32351 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7DE89  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926094373 760044256 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 5F 40 00 3F 06 44 86 0A 08 13 67 0A 0A  .4~_@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 DE 89 80 10  QV.\...l..`.....
0x0030: 01 F5 61 70 00 00 01 01 08 0A 37 33 14 25 2D 4D  ..ap......73.%-M
0x0040: 5A E0                                            Z.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
12/05-18:59:35.089201 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32352 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7E051  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926094373 760044256 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 60 40 00 3F 06 44 85 0A 08 13 67 0A 0A  .4~`@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 E0 51 80 10  QV.\...l..`..Q..
0x0030: 01 F5 5F A8 00 00 01 01 08 0A 37 33 14 25 2D 4D  .._.......73.%-M
0x0040: 5A E0                                            Z.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:35.089201 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32353 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7E445  Win: 0x1EE  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926094373 760044256 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 61 40 00 3F 06 44 84 0A 08 13 67 0A 0A  .4~a@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 E4 45 80 10  QV.\...l..`..E..
0x0030: 01 EE 5B BB 00 00 01 01 08 0A 37 33 14 25 2D 4D  ..[.......73.%-M
0x0040: 5A E0                                            Z.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:35.089260 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32354 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7E8F5  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926094373 760044256 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 62 40 00 3F 06 44 83 0A 08 13 67 0A 0A  .4~b@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 E8 F5 80 10  QV.\...l..`.....
0x0030: 01 F5 57 04 00 00 01 01 08 0A 37 33 14 25 2D 4D  ..W.......73.%-M
0x0040: 5A E0                                            Z.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:35.089260 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32355 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7ED15  Win: 0x1EE  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926094373 760044256 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 63 40 00 3F 06 44 82 0A 08 13 67 0A 0A  .4~c@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 ED 15 80 10  QV.\...l..`.....
0x0030: 01 EE 52 EB 00 00 01 01 08 0A 37 33 14 25 2D 4D  ..R.......73.%-M
0x0040: 5A E0                                            Z.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
12/05-18:59:35.089396 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32356 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7EF25  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926094374 760044256 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 64 40 00 3F 06 44 81 0A 08 13 67 0A 0A  .4~d@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 EF 25 80 10  QV.\...l..`..%..
0x0030: 01 F5 50 D3 00 00 01 01 08 0A 37 33 14 26 2D 4D  ..P.......73.&-M
0x0040: 5A E0                                            Z.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:35.089396 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32357 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7F0B9  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926094374 760044256 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 65 40 00 3F 06 44 80 0A 08 13 67 0A 0A  .4~e@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 F0 B9 80 10  QV.\...l..`.....
0x0030: 01 F5 4F 3F 00 00 01 01 08 0A 37 33 14 26 2D 4D  ..O?......73.&-M
0x0040: 5A E0                                            Z.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
12/05-18:59:35.089528 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26136 IpLen:20 DgmLen:124 DF
***AP*** Seq: 0x60F84079  Ack: 0xDE6CECA2  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 760044460 926094374 
0x0000: 02 C8 85 B5 5A AA 02 89 23 51 E4 69 08 00 45 10  ....Z...#Q.i..E.
0x0010: 00 7C 66 18 40 00 40 06 5B 85 0A 0A 51 56 0A 08  .|f.@.@.[...QV..
0x0020: 13 67 00 16 BC 5C 60 F8 40 79 DE 6C EC A2 80 18  .g...\`.@y.l....
0x0030: 01 D4 79 3D 00 00 01 01 08 0A 2D 4D 5B AC 37 33  ..y=......-M[.73
0x0040: 14 26 DE CF 66 F9 BD 84 30 8C 02 C0 8A 65 FD 82  .&..f...0....e..
0x0050: 8C A8 B0 42 E1 77 BE 40 A4 71 88 30 D9 B5 D4 42  ...B.w.@.q.0...B
0x0060: B3 7F 99 61 B6 25 32 59 EF 96 C2 1C F4 66 49 BD  ...a.%2Y.....fI.
0x0070: 5F 75 FB 0D CA 1B 12 43 E4 D3 83 FA 79 BF 64 16  _u.....C....y.d.
0x0080: 59 99 93 2D 0F CB 6E C9 E1 6C                    Y..-..n..l

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:35.287615 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32358 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7F5B5  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926094575 760044460 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 66 40 00 3F 06 44 7F 0A 08 13 67 0A 0A  .4~f@.?.D....g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 F5 B5 80 10  QV.\...l..`.....
0x0030: 01 F5 48 AE 00 00 01 01 08 0A 37 33 14 EF 2D 4D  ..H.......73..-M
0x0040: 5B AC                                            [.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:35.293174 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32359 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7FAB1  Win: 0x1EE  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926094575 760044460 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 67 40 00 3F 06 44 7E 0A 08 13 67 0A 0A  .4~g@.?.D~...g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 FA B1 80 10  QV.\...l..`.....
0x0030: 01 EE 43 B9 00 00 01 01 08 0A 37 33 14 EF 2D 4D  ..C.......73..-M
0x0040: 5B AC                                            [.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:35.293174 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32360 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F7FFAD  Win: 0x1E5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926094575 760044460 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 68 40 00 3F 06 44 7D 0A 08 13 67 0A 0A  .4~h@.?.D}...g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F7 FF AD 80 10  QV.\...l..`.....
0x0030: 01 E5 3E C6 00 00 01 01 08 0A 37 33 14 EF 2D 4D  ..>.......73..-M
0x0040: 5B AC                                            [.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:35.293174 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32361 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F804A9  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926094575 760044460 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 69 40 00 3F 06 44 7C 0A 08 13 67 0A 0A  .4~i@.?.D|...g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F8 04 A9 80 10  QV.\...l..`.....
0x0030: 01 F5 39 BA 00 00 01 01 08 0A 37 33 14 EF 2D 4D  ..9.......73..-M
0x0040: 5B AC                                            [.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:35.293174 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32362 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F809A5  Win: 0x1EE  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926094575 760044460 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 6A 40 00 3F 06 44 7B 0A 08 13 67 0A 0A  .4~j@.?.D{...g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F8 09 A5 80 10  QV.\...l..`.....
0x0030: 01 EE 34 C5 00 00 01 01 08 0A 37 33 14 EF 2D 4D  ..4.......73..-M
0x0040: 5B AC                                            [.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:35.293499 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32363 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F80EA1  Win: 0x1E5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926094575 760044460 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 6B 40 00 3F 06 44 7A 0A 08 13 67 0A 0A  .4~k@.?.Dz...g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F8 0E A1 80 10  QV.\...l..`.....
0x0030: 01 E5 2F D2 00 00 01 01 08 0A 37 33 14 EF 2D 4D  ../.......73..-M
0x0040: 5B AC                                            [.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:35.293509 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32364 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F81899  Win: 0x1EE  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926094576 760044460 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 6C 40 00 3F 06 44 79 0A 08 13 67 0A 0A  .4~l@.?.Dy...g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F8 18 99 80 10  QV.\...l..`.....
0x0030: 01 EE 25 D0 00 00 01 01 08 0A 37 33 14 F0 2D 4D  ..%.......73..-M
0x0040: 5B AC                                            [.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-18:59:35.293525 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32365 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CECA2  Ack: 0x60F840C1  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 926094577 760044460 
0x0000: 02 89 23 51 E4 69 02 C8 85 B5 5A AA 08 00 45 10  ..#Q.i....Z...E.
0x0010: 00 34 7E 6D 40 00 3F 06 44 78 0A 08 13 67 0A 0A  .4~m@.?.Dx...g..
0x0020: 51 56 BC 5C 00 16 DE 6C EC A2 60 F8 40 C1 80 10  QV.\...l..`.@...
0x0030: 01 F5 FD 9F 00 00 01 01 08 0A 37 33 14 F1 2D 4D  ..........73..-M
0x0040: 5B AC                                            [.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

^C*** Caught Int-Signal
WARNING: No preprocessors configured for policy 0.
===============================================================================
Run time for packet processing was 4.91611 seconds
Snort processed 64 packets.
Snort ran for 0 days 0 hours 0 minutes 4 seconds
   Pkts/sec:           16
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      13213696
  Total allocated space (uordblks):      679312
  Total free space (fordblks):           107120
  Topmost releasable block (keepcost):   104480
===============================================================================
Packet I/O Totals:
   Received:          130
   Analyzed:           64 ( 49.231%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:           66 ( 50.769%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:           64 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:           64 (100.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:           52 ( 81.250%)
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
   IP4 Disc:           12 ( 18.750%)
   IP6 Disc:            0 (  0.000%)
   TCP Disc:            0 (  0.000%)
   UDP Disc:            0 (  0.000%)
  ICMP Disc:            0 (  0.000%)
All Discard:           12 ( 18.750%)
      Other:            0 (  0.000%)
Bad Chk Sum:           17 ( 26.562%)
    Bad TTL:            0 (  0.000%)
     S5 G 1:            0 (  0.000%)
     S5 G 2:            0 (  0.000%)
      Total:           64
===============================================================================
Snort exiting
```
### Operation Mode 2: Packet Logger Mode
Let's run Snort in Logger Mode
You can use Snort as a sniffer and log the sniffed packets via logger mode. You only need to use the packet logger mode parameters, and Snort does the rest to accomplish this.
Packet logger parameters are explained in the table below;
Parameter	Description
-l
Logger mode, target log and alert output directory. Default output folder is /var/log/snort
The default action is to dump as tcpdump format in /var/log/snort
-K ASCII	Log packets in ASCII format.
-r	Reading option, read the dumped logs in Snort.
-n	Specify the number of packets that will process/read. Snort will stop after reading the specified number of packets.
Let's start using each parameter and see the difference between them. Snort needs active traffic on your interface, so we need to generate traffic to see Snort in action.
Logfile Ownership
Before generating logs and investigating them, we must remember the Linux file ownership and permissions. No need to deep dive into user types and permissions. The fundamental file ownership rule; whoever creates a file becomes the owner of the corresponding file.
Snort needs superuser (root) rights to sniff the traffic, so once you run the snort with the "sudo" command, the "root" account will own the generated log files. Therefore you will need "root" rights to investigate the log files. There are two different approaches to investigate the generated log files;
Elevation of privileges - You can elevate your privileges to examine the files. You can use the "sudo" command to execute your command as a superuser with the following command sudo command. You can also elevate the session privileges and switch to the superuser account to examine the generated log files with the following command: sudo su
Changing the ownership of files/directories - You can also change the ownership of the file/folder to read it as your user: sudo chown username file or sudo chown username -R directory The "-R" parameter helps recursively process the files and directories.
Logging with parameter "-l"
First, start the Snort instance in packet logger mode; sudo snort -dev -l .
Now start ICMP/HTTP traffic with the traffic-generator script.
Once the traffic is generated, Snort will start showing the packets and log them in the target directory. You can configure the default output directory in snort.config file. However, you can use the "-l" parameter to set a target directory. Identifying the default log directory is useful for continuous monitoring operations, and the "-l" parameter is much more useful for testing purposes.
The -l . part of the command creates the logs in the current directory. You will need to use this option to have the logs for each exercise in their fold
```text
logging with -l

           
user@ubuntu$ sudo snort -dev -l .
                             
Running in packet logging mode

        --== Initializing Snort ==--
Initializing Output Plugins!
Log directory = /var/log/snort
pcap DAQ configured to passive.
Acquiring network traffic from "ens33".
Decoding Ethernet

        --== Initialization Complete ==--
...
Commencing packet processing (pid=2679)
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
```
Now, let's check the generated log file. Note that the log file names will be different in your case.
```text
checking the log file

           
user@ubuntu$ ls .
                             
snort.log.1638459842
```
As you can see, it is a single all-in-one log file. It is a binary/tcpdump format log. This is what it looks like in the folder view.
Logging with parameter "-K ASCII"
Start the Snort instance in packet logger mode; sudo snort -dev -K ASCII
Now run the traffic-generator script as sudo and start ICMP/HTTP traffic. Once the traffic is generated, Snort will start showing the  packets in verbosity mode as follows;
```text
logging with -K ASCII

           
user@ubuntu$ sudo snort -dev -K ASCII -l .
                             
Running in packet logging mode

        --== Initializing Snort ==--
Initializing Output Plugins!
Log directory = /var/log/snort
pcap DAQ configured to passive.
Acquiring network traffic from "ens33".
Decoding Ethernet

        --== Initialization Complete ==--
...
Commencing packet processing (pid=2679)
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
```
Now, let's check the generated log file.
```text
Checking the log file

           
user@ubuntu$ ls .
                             
142.250.187.110  192.168.175.129  snort.log.1638459842
```
This is what it looks like in the folder view.
The logs created with "-K ASCII" parameter is entirely different. There are two folders with IP address names. Let's look into them.
```text
checking the log file

           
user@ubuntu$ ls ./192.168.175.129/
                             
ICMP_ECHO  UDP:36648-53  UDP:40757-53  UDP:47404-53  UDP:50624-123
```
Once we look closer at the created folders, we can see that the logs are in ASCII and categorised format, so it is possible to read them without using a Snort instance.
This is what it looks like in the folder view.
In a nutshell, ASCII mode provides multiple files in human-readable format, so it is possible to read the logs easily by using a text editor. By contrast with ASCII format, binary format is not human-readable and requires analysis using Snort or an application like tcpdump.
Let's compare the ASCII format with the binary format by opening both of them in a text editor. The difference between the binary log file and the ASCII log file is shown below. (Left side: binary format. Right side: ASCII format).
Reading generated logs with parameter "-r"
Start the Snort instance in packet reader mode; sudo snort -r
```text
reading log files with -r

           
user@ubuntu$ sudo snort -r snort.log.1638459842
                             
Running in packet dump mode

        --== Initializing Snort ==--
Initializing Output Plugins!
pcap DAQ configured to read-file.
Acquiring network traffic from "snort.log.1638459842".

        --== Initialization Complete ==--
...
Commencing packet processing (pid=3012)
WARNING: No preprocessors configured for policy 0.
12/02-07:44:03.123225 192.168.175.129 -> 142.250.187.110
ICMP TTL:64 TOS:0x0 ID:41900 IpLen:20 DgmLen:84 DF
Type:8  Code:0  ID:1   Seq:49  ECHO
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
WARNING: No preprocessors configured for policy 0.
12/02-07:44:26.169620 192.168.175.129 -> 142.250.187.110
ICMP TTL:64 TOS:0x0 ID:44765 IpLen:20 DgmLen:84 DF
Type:8  Code:0  ID:1   Seq:72  ECHO
===============================================================================
Packet I/O Totals:
   Received:           51
   Analyzed:           51 (100.000%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            0 (  0.000%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
...
      Total:           51
===============================================================================
Snort exiting
```
Note that Snort can read and handle the binary like output (tcpdump and Wireshark also can handle this log format). However, if you create logs with "-K ASCII" parameter, Snort will not read them. As you can see in the above output, Snort read and displayed the log file just like in the sniffer mode.
Opening log file with tcpdump.
```text
Opening the log file with tcpdump

           
user@ubuntu$ sudo tcpdump -r snort.log.1638459842 -ntc 10
                             
reading from file snort.log.1638459842, link-type EN10MB (Ethernet)
IP 192.168.175.129 > 142.250.187.110: ICMP echo request, id 1, seq 49, length 64
IP 142.250.187.110 > 192.168.175.129: ICMP echo reply, id 1, seq 49, length 64
IP 192.168.175.129 > 142.250.187.110: ICMP echo request, id 1, seq 50, length 64
IP 142.250.187.110 > 192.168.175.129: ICMP echo reply, id 1, seq 50, length 64
IP 192.168.175.129 > 142.250.187.110: ICMP echo request, id 1, seq 51, length 64
IP 142.250.187.110 > 192.168.175.129: ICMP echo reply, id 1, seq 51, length 64
IP 192.168.175.129 > 142.250.187.110: ICMP echo request, id 1, seq 52, length 64
IP 142.250.187.110 > 192.168.175.129: ICMP echo reply, id 1, seq 52, length 64
IP 192.168.175.1.63096 > 239.255.255.250.1900: UDP, length 173
IP 192.168.175.129 > 142.250.187.110: ICMP echo request, id 1, seq 53, length 64
```
Opening log file with Wireshark.
"-r" parameter also allows users to filter the binary log files. You can filter the processed log to see specific packets with the "-r" parameter and Berkeley Packet Filters (BPF).
sudo snort -r logname.log -X
sudo snort -r logname.log icmp
sudo snort -r logname.log tcp
sudo snort -r logname.log 'udp and port 53'
The output will be the same as the above, but only packets with the chosen protocol will be shown. Additionally, you can specify the number of processes with the parameter "-n". The following command will process only the first 10 packets:
snort -dvr logname.log -n 10
Please use the following resources to understand how the BPF works and its use.
https://en.wikipedia.org/wiki/Berkeley_Packet_Filter
https://biot.com/capstats/bpf.html
https://www.tcpdump.org/manpages/tcpdump.1.html
Now, use the attached VM and navigate to the Task-Exercises/Exercise-Files/TASK-6 folder to answer the questions!
```text
root@ip-10-10-81-86:/home/ubuntu/Desktop/Task-Exercises# sudo snort -dev -l .
Running in packet logging mode

        --== Initializing Snort ==--
Initializing Output Plugins!
Log directory = .
pcap DAQ configured to passive.
Acquiring network traffic from "eth0".
Decoding Ethernet

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

Commencing packet processing (pid=21669)
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
^C*** Caught Int-Signal
===============================================================================
Run time for packet processing was 33.803189 seconds
Snort processed 77 packets.
Snort ran for 0 days 0 hours 0 minutes 33 seconds
   Pkts/sec:            2
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      12906496
  Total allocated space (uordblks):      679712
  Total free space (fordblks):           106720
  Topmost releasable block (keepcost):   99104
===============================================================================
Packet I/O Totals:
   Received:           81
   Analyzed:           77 ( 95.062%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            4 (  4.938%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:           77 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:           77 (100.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:           77 (100.000%)
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
Bad Chk Sum:           37 ( 48.052%)
    Bad TTL:            0 (  0.000%)
     S5 G 1:            0 (  0.000%)
     S5 G 2:            0 (  0.000%)
      Total:           77
===============================================================================
Snort exiting

root@ip-10-10-81-86:/home/ubuntu/Desktop/Task-Exercises# ls .
Config-Sample  Exercise-Files  snort.log.1670270789  traffic-generator.sh

root@ip-10-10-81-86:/home/ubuntu/Desktop/Task-Exercises# sudo snort -dev -K ASCII -l .
Running in packet logging mode

        --== Initializing Snort ==--
Initializing Output Plugins!
Log directory = .
pcap DAQ configured to passive.
Acquiring network traffic from "eth0".
Decoding Ethernet

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

Commencing packet processing (pid=21679)
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
^C*** Caught Int-Signal
===============================================================================
Run time for packet processing was 9.219645 seconds
Snort processed 31 packets.
Snort ran for 0 days 0 hours 0 minutes 9 seconds
   Pkts/sec:            3
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      13180928
  Total allocated space (uordblks):      678528
  Total free space (fordblks):           107904
  Topmost releasable block (keepcost):   107040
===============================================================================
Packet I/O Totals:
   Received:           36
   Analyzed:           31 ( 86.111%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            5 ( 13.889%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:           31 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:           31 (100.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:           31 (100.000%)
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
Bad Chk Sum:           14 ( 45.161%)
    Bad TTL:            0 (  0.000%)
     S5 G 1:            0 (  0.000%)
     S5 G 2:            0 (  0.000%)
      Total:           31
===============================================================================
Snort exiting

root@ip-10-10-81-86:/home/ubuntu/Desktop/Task-Exercises# ls .
10.8.19.103  Config-Sample  Exercise-Files  snort.log.1670270789  traffic-generator.sh

root@ip-10-10-81-86:/home/ubuntu/Desktop/Task-Exercises# ls ./10.8.19.103/
TCP:48220-22

root@ip-10-10-81-86:/home/ubuntu/Desktop/Task-Exercises# cat ./10.8.19.103/TCP\:48220-22 
12/05-20:07:59.424589 02:89:23:51:E4:69 -> 02:C8:85:B5:5A:AA type:0x800 len:0x7E
10.10.81.86:22 -> 10.8.19.103:48220 TCP TTL:64 TOS:0x10 ID:26329 IpLen:20 DgmLen:112 DF
***AP*** Seq: 0x60F97D8D  Ack: 0xDE6CF60E  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764148795 929082634 
4D 20 FB 6F 02 97 CA D1 FF 83 51 B3 30 8F FC 05  M .o......Q.0...
A6 4D 25 54 44 DB 65 77 4E F5 02 38 F8 0D 5E A2  .M%TD.ewN..8..^.
E5 F5 93 7B 2E 68 00 7C 21 1D 6B A1 6F F7 B0 8C  ...{.h.|!.k.o...
BE B7 F1 72 04 71 91 59 CD 80 28 62              ...r.q.Y..(b

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:07:59.424718 02:89:23:51:E4:69 -> 02:C8:85:B5:5A:AA type:0x800 len:0x1F6
10.10.81.86:22 -> 10.8.19.103:48220 TCP TTL:64 TOS:0x10 ID:26330 IpLen:20 DgmLen:488 DF
***AP*** Seq: 0x60F97DC9  Ack: 0xDE6CF60E  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764148796 929082634 
C7 AF 95 8F 59 A4 1C 20 09 23 67 F6 D1 1C 09 0A  ....Y.. .#g.....
6B 4E 1A 17 1A A8 CC C4 47 93 80 6C D2 C5 EE 10  kN......G..l....
15 C6 63 FE 26 E8 E2 D0 19 8E 98 93 4A 9D 9C B9  ..c.&.......J...
81 1E 45 09 7C CE 2B D1 A7 47 0A 29 B3 25 86 A7  ..E.|.+..G.).%..
6F 57 17 43 65 80 6F 8C 4A 4E A0 74 DB 56 97 B4  oW.Ce.o.JN.t.V..
67 43 DD BA DE E6 E8 CD EF 6A A8 BA 04 49 66 5B  gC.......j...If[
2B 31 23 3B BC A4 81 84 39 71 A8 3A 78 37 21 8C  +1#;....9q.:x7!.
D3 C2 37 F4 80 E7 44 80 FD F6 4C 91 12 47 A7 D5  ..7...D...L..G..
47 C1 ED C0 4A 0D B9 C9 56 48 5F DE AB 48 D0 70  G...J...VH_..H.p
C1 1E F1 82 D7 2F FF 2D A2 F7 F2 A2 BF 0D 34 16  ...../.-......4.
A0 7B 21 B1 26 78 04 D4 D4 A7 15 0B 06 A0 01 92  .{!.&x..........
A8 E1 8F 1F D7 1F 5F 33 57 0D 5E A7 AE CE 70 FC  ......_3W.^...p.
F8 D1 5A AD 7D A3 69 CF 12 FD 29 E3 EB D9 77 3A  ..Z.}.i...)...w:
81 D5 E6 D8 8B 6F FA 37 51 94 2E 4C 85 FA 7D 19  .....o.7Q..L..}.
A3 9A 60 C0 C7 27 79 1B 78 EF 74 97 16 5B 17 27  ..`..'y.x.t..[.'
BC 0A A6 9C A5 5B 5F 4F 52 4C F4 8D BF 74 E7 51  .....[_ORL...t.Q
67 8A 0D 06 94 3A DB 39 E7 80 A9 3F 84 4A BF E3  g....:.9...?.J..
D2 C4 8A 11 03 EC 64 A7 B6 B3 4B 66 37 EB 54 9E  ......d...Kf7.T.
EF 01 B3 49 77 8B DA BC AD 46 ED FD A6 A1 3A E2  ...Iw....F....:.
CC 8F D7 4F 51 29 D3 C0 3C 12 AF BB B4 E4 B3 8A  ...OQ)..<.......
16 1D 4C 0D 89 C2 65 B7 82 8A 96 B4 48 5E 89 23  ..L...e.....H^.#
BC 1B 16 06 1F 92 86 C3 C9 F7 5D EA 91 0B 80 98  ..........].....
BC 8E E8 8F 96 5B DC D3 DB 99 46 94 DC 37 E3 2B  .....[....F..7.+
79 F2 47 3A F0 62 ED 52 BA 89 7D DF DD 05 78 0F  y.G:.b.R..}...x.
4B B3 63 BB DE 4A 50 30 DC 74 CD 3E FF F3 DA 87  K.c..JP0.t.>....
52 C1 F6 A6 FC CF 7F 38 2E A6 E3 37 E3 DB 90 86  R......8...7....
00 E7 57 D2 CE 7B 8A 57 32 B6 7A 14 3D 05 D7 57  ..W..{.W2.z.=..W
DE 7B E5 7E                                      .{.~

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:07:59.424789 02:89:23:51:E4:69 -> 02:C8:85:B5:5A:AA type:0x800 len:0xEE
10.10.81.86:22 -> 10.8.19.103:48220 TCP TTL:64 TOS:0x10 ID:26331 IpLen:20 DgmLen:224 DF
***AP*** Seq: 0x60F97F7D  Ack: 0xDE6CF60E  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764148796 929082634 
EC F0 17 FF 4F 36 D1 55 BE 6D 4C 71 09 83 14 7C  ....O6.U.mLq...|
8F 69 1E BB F3 F4 6E 47 D9 E5 93 16 0A D8 0E 87  .i....nG........
A2 B5 4E EE BE 1F EC 6A 04 CA 59 E1 BB EA 20 18  ..N....j..Y... .
5A 73 F4 94 85 38 C8 87 55 53 FE 1C 36 55 57 B6  Zs...8..US..6UW.
7A B7 FB 7D 37 4B 49 53 41 8A BA 03 DB B9 DA 1F  z..}7KISA.......
DD D6 75 FC 83 F2 F7 8D 78 9D 62 52 62 45 24 4D  ..u.....x.bRbE$M
70 17 46 90 A8 26 44 8B C8 32 BC 07 A9 68 B2 70  p.F..&D..2...h.p
45 AA CB 14 5D D1 9D 3D CE 90 C4 37 85 A8 AD F7  E...]..=...7....
9C 83 15 C0 C7 81 8F 79 BF 3D B0 EE CA E8 2B CD  .......y.=....+.
ED 3A A3 91 01 C1 8E 57 36 F3 24 4A 50 07 BE FF  .:.....W6.$JP...
31 54 62 54 99 52 F4 BE 90 6E 9E A5              1TbT.R...n..

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:07:59.557061 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32585 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF60E  Ack: 0x60F97C59  Win: 0x7A2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929082831 764148738 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:07:59.575854 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32586 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF60E  Ack: 0x60F97CE5  Win: 0x7A2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929082844 764148751 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:07:59.587373 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32587 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF60E  Ack: 0x60F97D21  Win: 0x7A2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929082860 764148764 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:07:59.587373 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32588 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF60E  Ack: 0x60F97D8D  Win: 0x7A2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929082860 764148766 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:07:59.626131 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32589 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF60E  Ack: 0x60F97DC9  Win: 0x7A2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929082899 764148795 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:07:59.626131 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32590 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF60E  Ack: 0x60F97F7D  Win: 0x79F  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929082899 764148796 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:07:59.627044 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32591 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF60E  Ack: 0x60F98029  Win: 0x79E  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929082899 764148796 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:00.421300 02:89:23:51:E4:69 -> 02:C8:85:B5:5A:AA type:0x800 len:0xCE
10.10.81.86:22 -> 10.8.19.103:48220 TCP TTL:64 TOS:0x10 ID:26332 IpLen:20 DgmLen:192 DF
***AP*** Seq: 0x60F98029  Ack: 0xDE6CF60E  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764149792 929082899 
84 41 D9 CD 9A EB 7F EC 0F D0 23 A6 00 8B D9 41  .A........#....A
68 C5 02 E1 93 F7 C5 D2 2C A7 17 D4 06 5A 8B 4E  h.......,....Z.N
A5 1E BE 69 45 67 FA 41 C1 13 D7 AC 2E DA EC CF  ...iEg.A........
37 6E 2A BC CF D0 A6 41 05 A9 BB 63 54 ED C5 84  7n*....A...cT...
B4 21 8D D3 23 14 4C 59 49 21 F5 43 38 3B F6 F9  .!..#.LYI!.C8;..
57 EC 80 67 82 E9 33 7D EE 82 BF AD 3C 8A 88 30  W..g..3}....<..0
95 78 11 8C B1 97 16 FB B3 77 98 AC 4F 09 BD A7  .x.......w..O...
3C 3D 71 D7 C9 9F D1 C1 F0 2F 8D F9 D4 A8 80 A5  <=q....../......
EC 31 F5 B6 99 69 0A 66 01 5F DB 11              .1...i.f._..

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:00.421343 02:89:23:51:E4:69 -> 02:C8:85:B5:5A:AA type:0x800 len:0x15A
10.10.81.86:22 -> 10.8.19.103:48220 TCP TTL:64 TOS:0x10 ID:26333 IpLen:20 DgmLen:332 DF
***AP*** Seq: 0x60F980B5  Ack: 0xDE6CF60E  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764149792 929082899 
E9 09 BD 54 1F 9D FB 66 33 DF FA 8B 9A A4 C2 53  ...T...f3......S
98 1A D0 FF CA 80 9F 76 8F DC 2B DC 64 29 64 77  .......v..+.d)dw
A1 0B 4C F5 FA A3 9B 52 F4 14 3E 35 B1 F1 BB BE  ..L....R..>5....
7F 62 2C D2 7F 14 DC EF 53 05 09 36 C8 4A 54 B6  .b,.....S..6.JT.
E9 D4 EE 5C 1B DC 50 C0 5C B7 35 B4 C6 62 C5 A1  ...\..P.\.5..b..
26 A6 28 B6 79 95 53 BC 25 AE 3B 84 08 6F 62 DD  &.(.y.S.%.;..ob.
11 6A 78 56 DA EC 80 3C DA 82 B4 33 48 97 DF F0  .jxV...<...3H...
B7 D2 57 CA 56 FA 0B E0 C6 9C 99 96 A5 A2 3D 58  ..W.V.........=X
81 FB 28 B2 98 E6 EB FC 7D 32 F3 05 DC F9 F8 AC  ..(.....}2......
50 BE A7 92 C0 06 D7 1E 69 BF 1E 75 D3 08 D6 D2  P.......i..u....
2B 10 DE 97 6B 50 C2 41 A6 1F 3E 32 FC 4D 3A 72  +...kP.A..>2.M:r
FA BE 79 6F 2C A1 EF 7F 96 E4 9E D5 59 09 CD 80  ..yo,.......Y...
1B 23 A4 EA 86 DD B5 56 30 1F 1B 24 9A 7E D7 ED  .#.....V0..$.~..
45 66 98 55 F4 BB 6B 4C 49 8F DD 1B F0 04 B5 E7  Ef.U..kLI.......
BF 60 8E E1 5E 5A 11 8B 29 26 A8 5B A7 2F 7F DA  .`..^Z..)&.[./..
76 AC 11 F4 4C 88 6B CF 4D 91 40 CB A9 48 E2 47  v...L.k.M.@..H.G
F8 6A F2 62 EB E6 BA 8D 04 93 A7 50 BB BF 51 07  .j.b.......P..Q.
E8 E8 93 4A B7 26 DA 0A                          ...J.&..

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:00.421386 02:89:23:51:E4:69 -> 02:C8:85:B5:5A:AA type:0x800 len:0x9E
10.10.81.86:22 -> 10.8.19.103:48220 TCP TTL:64 TOS:0x10 ID:26334 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F981CD  Ack: 0xDE6CF60E  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764149792 929082899 
05 16 F4 8F B1 B7 35 57 DD ED B4 C6 8A B0 A8 B3  ......5W........
F3 B8 21 D3 35 A6 F2 E0 15 7A 60 E6 30 25 B3 34  ..!.5....z`.0%.4
2A 80 91 84 8C 24 D4 74 CF 43 67 B8 E1 A0 9C 6B  *....$.t.Cg....k
2F 87 5A AD 25 E7 F5 7F 7A DF AB 0B F9 FD 8A 68  /.Z.%...z......h
7B 7D DF E5 CA 32 AB 06 11 87 19 4D 49 9D F1 F2  {}...2.....MI...
84 B6 FE 34 E2 DE 00 4B 65 77 AB 1D              ...4...Kew..

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:00.616996 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32592 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF60E  Ack: 0x60F980B5  Win: 0x7A2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929083901 764149792 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:00.617354 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32593 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF60E  Ack: 0x60F981CD  Win: 0x7A2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929083902 764149792 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:00.617354 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32594 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF60E  Ack: 0x60F98229  Win: 0x7A2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929083902 764149792 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:01.444682 02:89:23:51:E4:69 -> 02:C8:85:B5:5A:AA type:0x800 len:0xCE
10.10.81.86:22 -> 10.8.19.103:48220 TCP TTL:64 TOS:0x10 ID:26335 IpLen:20 DgmLen:192 DF
***AP*** Seq: 0x60F98229  Ack: 0xDE6CF60E  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764150816 929083902 
7D 3A B3 1A E3 C6 E2 D7 43 86 34 FC CE D3 FC 8C  }:......C.4.....
C5 2D 37 28 B7 55 78 A2 98 7F F1 A5 64 3E 82 C8  .-7(.Ux.....d>..
73 D6 CA 5A 20 37 20 5B 4D 92 4F D6 4D 73 8A C8  s..Z 7 [M.O.Ms..
98 5A 02 CC BB 8A 86 89 8B 1A 0F 26 77 A8 35 9C  .Z.........&w.5.
C2 87 21 A3 EA D9 86 67 A7 C3 F9 DD C8 43 87 23  ..!....g.....C.#
D6 A9 03 12 E4 32 70 09 9F 0D 41 F3 0F 03 B9 C8  .....2p...A.....
0C 1B AC 5D 9C 70 B1 8B 6F B6 97 24 1C A9 E1 17  ...].p..o..$....
1C BD 21 A3 D2 F3 BE D8 58 57 1B A4 76 28 5F 19  ..!.....XW..v(_.
E9 95 CA A6 61 88 F9 4F 00 0F 9A 06              ....a..O....

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:01.444773 02:89:23:51:E4:69 -> 02:C8:85:B5:5A:AA type:0x800 len:0x9E
10.10.81.86:22 -> 10.8.19.103:48220 TCP TTL:64 TOS:0x10 ID:26336 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F982B5  Ack: 0xDE6CF60E  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764150816 929083902 
A6 66 A6 DD 26 DF 94 91 A6 C7 FD 0C EF C5 6D 09  .f..&.........m.
28 AA 41 05 D0 6D BB 6B A2 B2 2A E2 B2 FC 10 02  (.A..m.k..*.....
95 89 F1 2B 40 FA 99 C1 81 25 F7 A1 81 CF 6B E2  ...+@....%....k.
C4 18 4A A4 DF C7 68 63 AA 5E 1B D9 2A 7E 7C A6  ..J...hc.^..*~|.
B2 2A 10 8F 4A 70 8C 76 3B 13 10 0B 63 3B 62 04  .*..Jp.v;...c;b.
2B EC EB 9F 3D D4 C8 B2 CC 35 B9 AD              +...=....5..

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:01.637155 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32595 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF60E  Ack: 0x60F982B5  Win: 0x7A2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929084935 764150816 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:01.637190 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32596 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF60E  Ack: 0x60F98311  Win: 0x7A2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929084935 764150816 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:02.468634 02:89:23:51:E4:69 -> 02:C8:85:B5:5A:AA type:0x800 len:0xCE
10.10.81.86:22 -> 10.8.19.103:48220 TCP TTL:64 TOS:0x10 ID:26337 IpLen:20 DgmLen:192 DF
***AP*** Seq: 0x60F98311  Ack: 0xDE6CF60E  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764151840 929084935 
76 D5 4C 57 B8 0D AC BC 1E CA 24 AA 1E FF A5 EB  v.LW......$.....
92 1E 1E 02 09 BA 09 46 24 96 9C 51 9C C8 43 49  .......F$..Q..CI
96 BD 8B 03 56 93 87 52 13 97 40 2E 36 08 58 AA  ....V..R..@.6.X.
1E EA DD 27 1A 31 0F 67 CD 17 94 B7 EB 3E 10 13  ...'.1.g.....>..
CF D3 5B FE 9B 72 9F BD AE D2 8E 85 F2 40 1A 3C  ..[..r.......@.<
F8 60 A0 28 C1 3B 15 6E F6 95 21 F0 F4 8B C1 83  .`.(.;.n..!.....
DF AE BA 0C E3 D4 9A 66 37 63 F8 A1 58 12 DF D9  .......f7c..X...
79 41 2D 64 67 6B 4E 13 4C DD 76 42 F6 52 A9 90  yA-dgkN.L.vB.R..
9B 47 AB C2 6B 75 D4 38 D8 85 33 E3              .G..ku.8..3.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:02.663346 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32597 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF60E  Ack: 0x60F9839D  Win: 0x7A2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929085969 764151840 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:03.492569 02:89:23:51:E4:69 -> 02:C8:85:B5:5A:AA type:0x800 len:0x9E
10.10.81.86:22 -> 10.8.19.103:48220 TCP TTL:64 TOS:0x10 ID:26338 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F9839D  Ack: 0xDE6CF60E  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764152863 929085969 
9B 16 62 AB 6A 2F 6D 3E 4B F8 41 0A AF 8A 6F 69  ..b.j/m>K.A...oi
81 F1 53 8B 0E 5A 64 7E D4 8B 35 4E C1 F9 2F 51  ..S..Zd~..5N../Q
49 1A 43 85 1B FF 28 B9 B9 DD 37 FF 3E 72 45 15  I.C...(...7.>rE.
36 8E 83 3F 10 49 CC 7D A9 36 32 69 3E 66 2A DD  6..?.I.}.62i>f*.
32 DA 7C B8 5D C0 AC EC 7E 1E 95 8E 11 4C 86 AC  2.|.]...~....L..
E2 14 D2 EB FC 23 5A 30 A6 0B AA D4              .....#Z0....

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:03.687244 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32598 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF60E  Ack: 0x60F983F9  Win: 0x7A2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929086999 764152863 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:04.516577 02:89:23:51:E4:69 -> 02:C8:85:B5:5A:AA type:0x800 len:0x9E
10.10.81.86:22 -> 10.8.19.103:48220 TCP TTL:64 TOS:0x10 ID:26339 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F983F9  Ack: 0xDE6CF60E  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764153887 929086999 
9A CD 92 17 F4 D8 9B E5 47 D6 72 A1 52 55 70 44  ........G.r.RUpD
4F 81 81 E0 EE D8 BB 3A 50 9C DE 65 0F FF 63 74  O......:P..e..ct
BF 53 5C 19 A8 5E 49 CE 00 B4 59 F7 E3 6C F9 F1  .S\..^I...Y..l..
76 60 CA 0C 1D 31 F5 1B 73 F1 F8 08 14 4C 11 5F  v`...1..s....L._
11 D6 D3 33 F4 30 63 19 92 E7 83 8D 5C E0 37 48  ...3.0c.....\.7H
EB EE 68 29 C5 D3 69 02 CB E7 3A 85              ..h)..i...:.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:04.711975 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32599 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF60E  Ack: 0x60F98455  Win: 0x7A2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929088031 764153887 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:05.540609 02:89:23:51:E4:69 -> 02:C8:85:B5:5A:AA type:0x800 len:0x9E
10.10.81.86:22 -> 10.8.19.103:48220 TCP TTL:64 TOS:0x10 ID:26340 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F98455  Ack: 0xDE6CF60E  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764154912 929088031 
78 60 79 2C 73 29 E1 91 C2 2E 51 A1 53 4A F1 4E  x`y,s)....Q.SJ.N
AB 4C 7B 7F E0 FD 91 CE 7F 11 96 72 37 C2 75 97  .L{........r7.u.
F1 41 B6 9D 45 FB CB B0 0B C1 F4 BC 43 04 3D A5  .A..E.......C.=.
3D F9 E2 A3 94 85 CF 4B 83 92 7A D0 65 5A BB F7  =......K..z.eZ..
A6 1C 2D 93 D2 24 00 A4 79 B2 AF 2B 98 21 88 3F  ..-..$..y..+.!.?
51 B6 56 92 B5 C0 4C 99 60 9A 80 A4              Q.V...L.`...

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:05.740395 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32600 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF60E  Ack: 0x60F984B1  Win: 0x7A2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929089056 764154912 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:06.564601 02:89:23:51:E4:69 -> 02:C8:85:B5:5A:AA type:0x800 len:0x9E
10.10.81.86:22 -> 10.8.19.103:48220 TCP TTL:64 TOS:0x10 ID:26341 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F984B1  Ack: 0xDE6CF60E  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764155935 929089056 
B4 66 29 8E 64 2F 5A 3D B5 58 08 6E 91 6B 0D AD  .f).d/Z=.X.n.k..
B9 3D 2C 75 6E 32 7B 1B A7 1E 49 34 CA 28 4E 30  .=,un2{...I4.(N0
0B 66 8F 2A B7 87 67 E1 91 A4 49 AA 2E D4 8E AE  .f.*..g...I.....
BB 8B BF E4 F7 7C F8 90 1F 20 73 91 E5 B7 DD 8B  .....|... s.....
0D 52 EE 1F B2 EA 7A 3E 5F F9 24 17 73 F4 AE FD  .R....z>_.$.s...
00 65 6B 65 BB 79 A4 85 D4 97 15 8F              .eke.y......

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:06.757554 02:C8:85:B5:5A:AA -> 02:89:23:51:E4:69 type:0x800 len:0x42
10.8.19.103:48220 -> 10.10.81.86:22 TCP TTL:63 TOS:0x10 ID:32601 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF60E  Ack: 0x60F9850D  Win: 0x7A2  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929090078 764155935 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:08:07.588560 02:89:23:51:E4:69 -> 02:C8:85:B5:5A:AA type:0x800 len:0x9E
10.10.81.86:22 -> 10.8.19.103:48220 TCP TTL:64 TOS:0x10 ID:26342 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F9850D  Ack: 0xDE6CF60E  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764156959 929090078 
CA D8 0A 8E DE 94 5C 4A 22 C6 77 BC 40 C7 FE B2  ......\J".w.@...
B5 72 39 4B 10 04 08 34 34 F3 A7 E0 F8 6A A7 B8  .r9K...44....j..
A8 C3 7A FE D0 A0 E2 BF F8 93 B4 8C 2F 9D 17 56  ..z........./..V
92 08 50 4D 4A 4D AC E1 5E 9A 34 B5 3D 29 37 B1  ..PMJM..^.4.=)7.
BA 8F 60 BE 20 C2 C9 6D C8 95 AE 08 9C 3A A9 E3  ..`. ..m.....:..
1F 93 BB 58 50 7E 98 B1 BA 30 69 7A              ...XP~...0iz

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

root@ip-10-10-81-86:/home/ubuntu/Desktop/Task-Exercises# sudo snort -r snort.log.1670270789 
Running in packet dump mode

        --== Initializing Snort ==--
Initializing Output Plugins!
pcap DAQ configured to read-file.
Acquiring network traffic from "snort.log.1670270789".

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

Commencing packet processing (pid=21697)
12/05-20:06:29.436568 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26237 IpLen:20 DgmLen:112 DF
***AP*** Seq: 0x60F95915  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764058807 928992682 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:29.437210 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26238 IpLen:20 DgmLen:624 DF
***AP*** Seq: 0x60F95951  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764058808 928992682 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:29.576532 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32458 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F957E1  Win: 0x70E  TcpLen: 32
TCP Options (3) => NOP NOP TS: 928992898 764058755 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:29.595884 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32459 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F9586D  Win: 0x722  TcpLen: 32
TCP Options (3) => NOP NOP TS: 928992910 764058767 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:29.622348 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32460 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F958A9  Win: 0x722  TcpLen: 32
TCP Options (3) => NOP NOP TS: 928992943 764058781 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:29.626073 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32461 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F95915  Win: 0x722  TcpLen: 32
TCP Options (3) => NOP NOP TS: 928992943 764058782 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:29.636213 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32462 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F95951  Win: 0x722  TcpLen: 32
TCP Options (3) => NOP NOP TS: 928992950 764058807 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:29.636213 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32463 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F95B8D  Win: 0x736  TcpLen: 32
TCP Options (3) => NOP NOP TS: 928992951 764058808 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:30.436590 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26239 IpLen:20 DgmLen:248 DF
***AP*** Seq: 0x60F95B8D  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764059807 928992951 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:30.436695 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26240 IpLen:20 DgmLen:248 DF
***AP*** Seq: 0x60F95C51  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764059808 928992951 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:30.632979 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32464 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F95C51  Win: 0x74A  TcpLen: 32
TCP Options (3) => NOP NOP TS: 928993950 764059807 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:30.632980 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32465 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F95D15  Win: 0x75E  TcpLen: 32
TCP Options (3) => NOP NOP TS: 928993951 764059808 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:31.460523 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26241 IpLen:20 DgmLen:192 DF
***AP*** Seq: 0x60F95D15  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764060831 928993951 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:31.657535 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32466 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F95DA1  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 928994978 764060831 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:32.484522 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26242 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F95DA1  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764061855 928994978 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:32.677531 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32467 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F95DFD  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 928995998 764061855 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:33.508512 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26243 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F95DFD  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764062879 928995998 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:33.702399 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32468 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F95E59  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 928997022 764062879 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:34.532588 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26244 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F95E59  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764063903 928997022 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:34.728301 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32469 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F95EB5  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 928998043 764063903 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:35.556536 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26245 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F95EB5  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764064927 928998043 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:35.752222 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32470 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F95F11  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 928999064 764064927 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:36.580523 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26246 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F95F11  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764065951 928999064 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:36.782260 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32471 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F95F6D  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929000083 764065951 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:37.604553 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26247 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F95F6D  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764066975 929000083 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:37.797621 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32472 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F95FC9  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929001101 764066975 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:38.628525 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26248 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F95FC9  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764067999 929001101 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:38.827168 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32473 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F96025  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929002121 764067999 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:39.652539 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26249 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F96025  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764069023 929002121 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:39.847642 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32474 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F96081  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929003139 764069023 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:40.676512 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26250 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F96081  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764070047 929003139 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:40.867363 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32475 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F960DD  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929004156 764070047 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:41.700523 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26251 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F960DD  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764071071 929004156 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:41.895779 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32476 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F96139  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929005175 764071071 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:42.724530 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26252 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F96139  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764072095 929005175 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:42.918037 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32477 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F96195  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929006191 764072095 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:43.748519 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26253 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F96195  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764073119 929006191 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:43.950922 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32478 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F961F1  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929007210 764073119 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:44.772511 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26254 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F961F1  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764074143 929007210 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:44.966138 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32479 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F9624D  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929008227 764074143 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:45.796512 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26255 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F9624D  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764075167 929008227 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:45.986032 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32480 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F962A9  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929009242 764075167 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:46.820506 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26256 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F962A9  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764076191 929009242 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:47.021711 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32481 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F96305  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929010260 764076191 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:47.844553 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26257 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F96305  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764077215 929010260 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:48.036859 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32482 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F96361  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929011275 764077215 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:48.868520 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26258 IpLen:20 DgmLen:136 DF
***AP*** Seq: 0x60F96361  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764078239 929011275 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:48.868620 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26259 IpLen:20 DgmLen:88 DF
***AP*** Seq: 0x60F963B5  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764078240 929011275 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:49.071228 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32483 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F963B5  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929012292 764078239 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:49.071229 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32484 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F963D9  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929012292 764078240 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:49.892494 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26260 IpLen:20 DgmLen:136 DF
***AP*** Seq: 0x60F963D9  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764079263 929012292 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:49.892582 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26261 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F9642D  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764079263 929012292 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:50.090614 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32485 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F9642D  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929013310 764079263 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:50.092953 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32486 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F96489  Win: 0x772  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929013310 764079263 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:50.916522 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26262 IpLen:20 DgmLen:192 DF
***AP*** Seq: 0x60F96489  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764080287 929013310 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:51.117344 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32487 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F96515  Win: 0x786  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929014325 764080287 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:51.940566 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26263 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F96515  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764081311 929014325 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:52.137743 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32488 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F96571  Win: 0x786  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929015342 764081311 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:52.964518 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26264 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F96571  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764082335 929015342 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:53.156854 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32489 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F965CD  Win: 0x786  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929016380 764082335 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:53.988537 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26265 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F965CD  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764083359 929016380 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:54.182036 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32490 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F96629  Win: 0x786  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929017426 764083359 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:55.012497 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26266 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F96629  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764084383 929017426 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:55.207058 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32491 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F96685  Win: 0x786  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929018470 764084383 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:56.036508 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26267 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F96685  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764085407 929018470 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:56.232209 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32492 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F966E1  Win: 0x786  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929019510 764085407 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:57.060531 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26268 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F966E1  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764086431 929019510 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:57.267152 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32493 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F9673D  Win: 0x786  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929020545 764086431 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:58.084542 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26269 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F9673D  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764087455 929020545 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:58.282084 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32494 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F96799  Win: 0x786  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929021577 764087455 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:06:59.108513 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26270 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F96799  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764088479 929021577 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:06:59.303349 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32495 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F967F5  Win: 0x786  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929022609 764088479 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:07:00.132637 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26271 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F967F5  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764089504 929022609 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:07:00.325427 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32496 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F96851  Win: 0x786  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929023636 764089504 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:07:01.156602 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26272 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F96851  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764090527 929023636 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-20:07:01.352135 10.8.19.103:48220 -> 10.10.81.86:22
TCP TTL:63 TOS:0x10 ID:32497 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xDE6CF092  Ack: 0x60F968AD  Win: 0x786  TcpLen: 32
TCP Options (3) => NOP NOP TS: 929024666 764090527 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-20:07:02.180507 10.10.81.86:22 -> 10.8.19.103:48220
TCP TTL:64 TOS:0x10 ID:26273 IpLen:20 DgmLen:144 DF
***AP*** Seq: 0x60F968AD  Ack: 0xDE6CF092  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 764091551 929024666 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

===============================================================================
Run time for packet processing was 0.2108 seconds
Snort processed 77 packets.
Snort ran for 0 days 0 hours 0 minutes 0 seconds
   Pkts/sec:           77
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      12906496
  Total allocated space (uordblks):      678144
  Total free space (fordblks):           108288
  Topmost releasable block (keepcost):   102304
===============================================================================
Packet I/O Totals:
   Received:           77
   Analyzed:           77 (100.000%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            0 (  0.000%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:           77 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:           77 (100.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:           77 (100.000%)
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
Bad Chk Sum:           37 ( 48.052%)
    Bad TTL:            0 (  0.000%)
     S5 G 1:            0 (  0.000%)
     S5 G 2:            0 (  0.000%)
      Total:           77
===============================================================================
Snort exiting

root@ip-10-10-81-86:/home/ubuntu/Desktop/Task-Exercises# sudo tcpdump -r snort.log.1670270789 -ntc 10
reading from file snort.log.1670270789, link-type EN10MB (Ethernet)
IP 10.10.81.86.22 > 10.8.19.103.48220: Flags [P.], seq 1626954005:1626954065, ack 3731681426, win 468, options [nop,nop,TS val 764058807 ecr 928992682], length 60
IP 10.10.81.86.22 > 10.8.19.103.48220: Flags [P.], seq 60:632, ack 1, win 468, options [nop,nop,TS val 764058808 ecr 928992682], length 572
IP 10.8.19.103.48220 > 10.10.81.86.22: Flags [.], ack 4294966988, win 1806, options [nop,nop,TS val 928992898 ecr 764058755], length 0
IP 10.8.19.103.48220 > 10.10.81.86.22: Flags [.], ack 4294967128, win 1826, options [nop,nop,TS val 928992910 ecr 764058767], length 0
IP 10.8.19.103.48220 > 10.10.81.86.22: Flags [.], ack 4294967188, win 1826, options [nop,nop,TS val 928992943 ecr 764058781], length 0
IP 10.8.19.103.48220 > 10.10.81.86.22: Flags [.], ack 0, win 1826, options [nop,nop,TS val 928992943 ecr 764058782], length 0
IP 10.8.19.103.48220 > 10.10.81.86.22: Flags [.], ack 60, win 1826, options [nop,nop,TS val 928992950 ecr 764058807], length 0
IP 10.8.19.103.48220 > 10.10.81.86.22: Flags [.], ack 632, win 1846, options [nop,nop,TS val 928992951 ecr 764058808], length 0
IP 10.10.81.86.22 > 10.8.19.103.48220: Flags [P.], seq 632:828, ack 1, win 468, options [nop,nop,TS val 764059807 ecr 928992951], length 196
IP 10.10.81.86.22 > 10.8.19.103.48220: Flags [P.], seq 828:1024, ack 1, win 468, options [nop,nop,TS val 764059808 ecr 928992951], length 196

root@ip-10-10-81-86:/home/ubuntu/Desktop/Task-Exercises# sudo tcpdump -r snort.log.1670270789 -ntc 5
reading from file snort.log.1670270789, link-type EN10MB (Ethernet)
IP 10.10.81.86.22 > 10.8.19.103.48220: Flags [P.], seq 1626954005:1626954065, ack 3731681426, win 468, options [nop,nop,TS val 764058807 ecr 928992682], length 60
IP 10.10.81.86.22 > 10.8.19.103.48220: Flags [P.], seq 60:632, ack 1, win 468, options [nop,nop,TS val 764058808 ecr 928992682], length 572
IP 10.8.19.103.48220 > 10.10.81.86.22: Flags [.], ack 4294966988, win 1806, options [nop,nop,TS val 928992898 ecr 764058755], length 0
IP 10.8.19.103.48220 > 10.10.81.86.22: Flags [.], ack 4294967128, win 1826, options [nop,nop,TS val 928992910 ecr 764058767], length 0
IP 10.8.19.103.48220 > 10.10.81.86.22: Flags [.], ack 4294967188, win 1826, options [nop,nop,TS val 928992943 ecr 764058781], length 0

root@ip-10-10-52-242:/home/ubuntu/Desktop/Task-Exercises# sudo snort -r snort.log.1670274953 -x
Running in packet dump mode

        --== Initializing Snort ==--
Initializing Output Plugins!
pcap DAQ configured to read-file.
Acquiring network traffic from "snort.log.1670274953".

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

Commencing packet processing (pid=6884)
12/05-21:15:53.466091 10.10.52.242:22 -> 10.8.19.103:49618
TCP TTL:64 TOS:0x10 ID:54712 IpLen:20 DgmLen:112 DF
***AP*** Seq: 0xE0703FD1  Ack: 0xBD7F8804  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 4193525944 3816246954 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-21:15:53.466231 10.10.52.242:22 -> 10.8.19.103:49618
TCP TTL:64 TOS:0x10 ID:54713 IpLen:20 DgmLen:136 DF
***AP*** Seq: 0xE070400D  Ack: 0xBD7F8804  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 4193525944 3816246954 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-21:15:53.466257 10.10.52.242:22 -> 10.8.19.103:49618
TCP TTL:64 TOS:0x10 ID:54714 IpLen:20 DgmLen:448 DF
***AP*** Seq: 0xE0704061  Ack: 0xBD7F8804  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 4193525944 3816246954 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-21:15:53.466294 10.10.52.242:22 -> 10.8.19.103:49618
TCP TTL:64 TOS:0x10 ID:54715 IpLen:20 DgmLen:216 DF
***AP*** Seq: 0xE07041ED  Ack: 0xBD7F8804  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 4193525944 3816246954 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.573987 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8575 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE0703F29  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247159 4193525863 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.623821 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8576 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE0703F65  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247206 4193525910 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.624999 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8577 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE0703FD1  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247209 4193525912 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.664128 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8578 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE070400D  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247242 4193525944 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.664129 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8579 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE0704061  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247242 4193525944 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.664129 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8580 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE07041ED  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247242 4193525944 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.664129 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8581 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE0704291  Win: 0x1F4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247242 4193525944 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-21:15:53.709713 10.10.52.242:55678 -> 91.189.91.48:443
TCP TTL:64 TOS:0x0 ID:56607 IpLen:20 DgmLen:60 DF
******S* Seq: 0x5FB4BE54  Ack: 0x0  Win: 0xF507  TcpLen: 40
TCP Options (5) => MSS: 8961 SackOK TS: 1868606612 0 NOP WS: 7 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-21:15:54.458068 10.10.52.242:22 -> 10.8.19.103:49618
TCP TTL:64 TOS:0x10 ID:54716 IpLen:20 DgmLen:248 DF
***AP*** Seq: 0xE0704291  Ack: 0xBD7F8804  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 4193526936 3816247242 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-21:15:54.458093 10.10.52.242:22 -> 10.8.19.103:49618
TCP TTL:64 TOS:0x10 ID:54717 IpLen:20 DgmLen:296 DF
***AP*** Seq: 0xE0704355  Ack: 0xBD7F8804  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 4193526936 3816247242 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:54.654231 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8582 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE0704355  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816248224 4193526936 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:54.654231 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8583 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE0704449  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816248224 4193526936 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-21:15:54.713834 10.10.52.242:55678 -> 91.189.91.48:443
TCP TTL:64 TOS:0x0 ID:56608 IpLen:20 DgmLen:60 DF
******S* Seq: 0x5FB4BE54  Ack: 0x0  Win: 0xF507  TcpLen: 40
TCP Options (5) => MSS: 8961 SackOK TS: 1868607616 0 NOP WS: 7 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-21:15:55.482091 10.10.52.242:22 -> 10.8.19.103:49618
TCP TTL:64 TOS:0x10 ID:54718 IpLen:20 DgmLen:192 DF
***AP*** Seq: 0xE0704449  Ack: 0xBD7F8804  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 4193527960 3816248224 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

===============================================================================
Run time for packet processing was 0.540 seconds
Snort processed 18 packets.
Snort ran for 0 days 0 hours 0 minutes 0 seconds
   Pkts/sec:           18
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      12906496
  Total allocated space (uordblks):      678144
  Total free space (fordblks):           108288
  Topmost releasable block (keepcost):   102304
===============================================================================
Packet I/O Totals:
   Received:           18
   Analyzed:           18 (100.000%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            0 (  0.000%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:           18 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:           18 (100.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:           18 (100.000%)
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
Bad Chk Sum:            9 ( 50.000%)
    Bad TTL:            0 (  0.000%)
     S5 G 1:            0 (  0.000%)
     S5 G 2:            0 (  0.000%)
      Total:           18
===============================================================================
Snort exiting

root@ip-10-10-52-242:/home/ubuntu/Desktop/Task-Exercises# sudo snort -r snort.log.1670274953 icmp
Running in packet dump mode

        --== Initializing Snort ==--
Initializing Output Plugins!
Snort BPF option: icmp
pcap DAQ configured to read-file.
Acquiring network traffic from "snort.log.1670274953".

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

Commencing packet processing (pid=6891)
===============================================================================
Run time for packet processing was 0.44 seconds
Snort processed 0 packets.
Snort ran for 0 days 0 hours 0 minutes 0 seconds
   Pkts/sec:            0
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      12906496
  Total allocated space (uordblks):      679296
  Total free space (fordblks):           107136
  Topmost releasable block (keepcost):   99456
===============================================================================
Packet I/O Totals:
   Received:            0
   Analyzed:            0 (  0.000%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            0 (  0.000%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:            0 (  0.000%)
       VLAN:            0 (  0.000%)
        IP4:            0 (  0.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:            0 (  0.000%)
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
      Total:            0
===============================================================================
Snort exiting

root@ip-10-10-52-242:/home/ubuntu/Desktop/Task-Exercises# sudo snort -r snort.log.1670274953 tcp
Running in packet dump mode

        --== Initializing Snort ==--
Initializing Output Plugins!
Snort BPF option: tcp
pcap DAQ configured to read-file.
Acquiring network traffic from "snort.log.1670274953".

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

Commencing packet processing (pid=6898)
12/05-21:15:53.466091 10.10.52.242:22 -> 10.8.19.103:49618
TCP TTL:64 TOS:0x10 ID:54712 IpLen:20 DgmLen:112 DF
***AP*** Seq: 0xE0703FD1  Ack: 0xBD7F8804  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 4193525944 3816246954 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-21:15:53.466231 10.10.52.242:22 -> 10.8.19.103:49618
TCP TTL:64 TOS:0x10 ID:54713 IpLen:20 DgmLen:136 DF
***AP*** Seq: 0xE070400D  Ack: 0xBD7F8804  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 4193525944 3816246954 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-21:15:53.466257 10.10.52.242:22 -> 10.8.19.103:49618
TCP TTL:64 TOS:0x10 ID:54714 IpLen:20 DgmLen:448 DF
***AP*** Seq: 0xE0704061  Ack: 0xBD7F8804  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 4193525944 3816246954 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-21:15:53.466294 10.10.52.242:22 -> 10.8.19.103:49618
TCP TTL:64 TOS:0x10 ID:54715 IpLen:20 DgmLen:216 DF
***AP*** Seq: 0xE07041ED  Ack: 0xBD7F8804  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 4193525944 3816246954 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.573987 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8575 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE0703F29  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247159 4193525863 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.623821 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8576 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE0703F65  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247206 4193525910 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.624999 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8577 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE0703FD1  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247209 4193525912 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.664128 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8578 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE070400D  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247242 4193525944 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.664129 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8579 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE0704061  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247242 4193525944 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.664129 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8580 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE07041ED  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247242 4193525944 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.664129 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8581 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE0704291  Win: 0x1F4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247242 4193525944 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-21:15:53.709713 10.10.52.242:55678 -> 91.189.91.48:443
TCP TTL:64 TOS:0x0 ID:56607 IpLen:20 DgmLen:60 DF
******S* Seq: 0x5FB4BE54  Ack: 0x0  Win: 0xF507  TcpLen: 40
TCP Options (5) => MSS: 8961 SackOK TS: 1868606612 0 NOP WS: 7 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-21:15:54.458068 10.10.52.242:22 -> 10.8.19.103:49618
TCP TTL:64 TOS:0x10 ID:54716 IpLen:20 DgmLen:248 DF
***AP*** Seq: 0xE0704291  Ack: 0xBD7F8804  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 4193526936 3816247242 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-21:15:54.458093 10.10.52.242:22 -> 10.8.19.103:49618
TCP TTL:64 TOS:0x10 ID:54717 IpLen:20 DgmLen:296 DF
***AP*** Seq: 0xE0704355  Ack: 0xBD7F8804  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 4193526936 3816247242 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:54.654231 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8582 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE0704355  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816248224 4193526936 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:54.654231 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8583 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE0704449  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816248224 4193526936 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-21:15:54.713834 10.10.52.242:55678 -> 91.189.91.48:443
TCP TTL:64 TOS:0x0 ID:56608 IpLen:20 DgmLen:60 DF
******S* Seq: 0x5FB4BE54  Ack: 0x0  Win: 0xF507  TcpLen: 40
TCP Options (5) => MSS: 8961 SackOK TS: 1868607616 0 NOP WS: 7 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-21:15:55.482091 10.10.52.242:22 -> 10.8.19.103:49618
TCP TTL:64 TOS:0x10 ID:54718 IpLen:20 DgmLen:192 DF
***AP*** Seq: 0xE0704449  Ack: 0xBD7F8804  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 4193527960 3816248224 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

===============================================================================
Run time for packet processing was 0.547 seconds
Snort processed 18 packets.
Snort ran for 0 days 0 hours 0 minutes 0 seconds
   Pkts/sec:           18
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      12906496
  Total allocated space (uordblks):      680400
  Total free space (fordblks):           106032
  Topmost releasable block (keepcost):   94272
===============================================================================
Packet I/O Totals:
   Received:           18
   Analyzed:           18 (100.000%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            0 (  0.000%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:           18 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:           18 (100.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:           18 (100.000%)
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
Bad Chk Sum:            9 ( 50.000%)
    Bad TTL:            0 (  0.000%)
     S5 G 1:            0 (  0.000%)
     S5 G 2:            0 (  0.000%)
      Total:           18
===============================================================================
Snort exiting

root@ip-10-10-52-242:/home/ubuntu/Desktop/Task-Exercises# sudo snort -r snort.log.1670274953 'udp and port 53'
Running in packet dump mode

        --== Initializing Snort ==--
Initializing Output Plugins!
Snort BPF option: udp and port 53
pcap DAQ configured to read-file.
Acquiring network traffic from "snort.log.1670274953".

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

Commencing packet processing (pid=6906)
===============================================================================
Run time for packet processing was 0.42 seconds
Snort processed 0 packets.
Snort ran for 0 days 0 hours 0 minutes 0 seconds
   Pkts/sec:            0
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      12906496
  Total allocated space (uordblks):      680416
  Total free space (fordblks):           106016
  Topmost releasable block (keepcost):   85984
===============================================================================
Packet I/O Totals:
   Received:            0
   Analyzed:            0 (  0.000%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            0 (  0.000%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:            0 (  0.000%)
       VLAN:            0 (  0.000%)
        IP4:            0 (  0.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:            0 (  0.000%)
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
      Total:            0
===============================================================================
Snort exiting

root@ip-10-10-52-242:/home/ubuntu/Desktop/Task-Exercises# sudo snort -dvr snort.log.1670274953 -n 10
Exiting after 10 packets
Running in packet dump mode

        --== Initializing Snort ==--
Initializing Output Plugins!
pcap DAQ configured to read-file.
Acquiring network traffic from "snort.log.1670274953".

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

Commencing packet processing (pid=6913)
12/05-21:15:53.466091 10.10.52.242:22 -> 10.8.19.103:49618
TCP TTL:64 TOS:0x10 ID:54712 IpLen:20 DgmLen:112 DF
***AP*** Seq: 0xE0703FD1  Ack: 0xBD7F8804  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 4193525944 3816246954 
1A A4 69 6D BE D8 5E B5 AA 80 94 D8 9C 46 02 A4  ..im..^......F..
6B 5B 80 D6 5E F3 6F F1 93 5C 61 04 E0 55 A6 45  k[..^.o..\a..U.E
66 CA B2 1C 43 30 70 AD 84 E1 52 6B D0 10 86 59  f...C0p...Rk...Y
DF 85 6B 73 E4 76 11 58 77 2D D0 20              ..ks.v.Xw-. 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-21:15:53.466231 10.10.52.242:22 -> 10.8.19.103:49618
TCP TTL:64 TOS:0x10 ID:54713 IpLen:20 DgmLen:136 DF
***AP*** Seq: 0xE070400D  Ack: 0xBD7F8804  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 4193525944 3816246954 
F9 73 C1 09 00 D0 31 75 DD 39 31 90 AB D8 F0 A3  .s....1u.91.....
EC 76 2F C8 69 E0 84 74 B9 43 0E 4C C9 9A 1B 77  .v/.i..t.C.L...w
BF C0 88 40 15 1C 1B E9 3C 82 94 CD 02 06 F5 7F  ...@....<.......
97 7D BF 66 33 9F F7 0A 28 0A 71 36 85 9A E8 FA  .}.f3...(.q6....
02 A7 C4 77 F2 4D 9B 43 1E 6B C9 B2 B1 1A 58 8E  ...w.M.C.k....X.
EE 39 E0 37                                      .9.7

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-21:15:53.466257 10.10.52.242:22 -> 10.8.19.103:49618
TCP TTL:64 TOS:0x10 ID:54714 IpLen:20 DgmLen:448 DF
***AP*** Seq: 0xE0704061  Ack: 0xBD7F8804  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 4193525944 3816246954 
6A F3 60 0F 0B 01 B6 19 58 50 0D 8F 8A 17 38 ED  j.`.....XP....8.
6F A8 3B C7 8D 0E C6 69 1C 54 14 DB 62 55 8D 47  o.;....i.T..bU.G
32 49 C2 B8 1E C1 57 0D C5 24 DD 3F 2E 1A E0 94  2I....W..$.?....
C8 82 C1 82 8E 74 1C F8 18 3B 41 5A 16 01 BE 90  .....t...;AZ....
7F 5D 5A 05 AD F7 77 91 53 81 2C 0F B0 F2 C8 2D  .]Z...w.S.,....-
AE D2 1A 51 91 C4 2E 06 5E E8 DC 1C AA 00 74 4A  ...Q....^.....tJ
7D D7 1D 1B 7F 1C 2E 18 16 50 50 79 8E 76 CE 19  }........PPy.v..
02 15 20 0E F1 0C 02 ED 01 9F 2C 08 1C 6A 78 00  .. .......,..jx.
37 48 22 EE 15 79 04 E0 71 6A 7C 16 BC 02 2D 26  7H"..y..qj|...-&
C7 00 50 97 45 2D 0E 0D FF 41 30 D6 65 7B 5E 65  ..P.E-...A0.e{^e
70 F0 41 7B 69 54 4A E2 46 D0 B6 85 C3 54 06 1C  p.A{iTJ.F....T..
91 D4 95 36 07 B3 98 06 2C AE BA 88 A8 FF 14 20  ...6....,...... 
9A FD 12 D2 6C B9 63 D3 BE 62 69 D6 9D 11 DD 2D  ....l.c..bi....-
F1 14 70 2C 06 B3 B1 EE 17 A5 EF 29 E2 70 56 5B  ..p,.......).pV[
0C 0C 41 A5 1A 49 B4 BA 6B 6B 62 56 36 EA 1C 5C  ..A..I..kkbV6..\
A6 ED D4 A5 24 00 F8 58 D5 BA CD 5A E3 FF 1B 67  ....$..X...Z...g
3D BE 79 19 00 CC 54 4D F9 66 5D 7D EC 55 FA E9  =.y...TM.f]}.U..
14 22 3F FB 6E 40 9C 6E 5E 04 21 7D 1C 8F 2C B0  ."?.n@.n^.!}..,.
61 D5 5A 78 1D 16 D3 AB FC 3E BE E8 D0 B1 1D CA  a.Zx.....>......
71 8D 84 00 BB 24 67 D6 D9 6A 88 45 99 F6 71 65  q....$g..j.E..qe
15 77 D6 64 0C 54 21 20 2D 03 9A F1 F3 78 9A 05  .w.d.T! -....x..
38 DE 98 EB EA 48 CF 24 7D A8 79 7A 05 43 DE A3  8....H.$}.yz.C..
30 1A DA 5D 47 26 9E 3A D4 DE 63 B3 02 16 49 33  0..]G&.:..c...I3
C0 AE 8E 48 A4 2B E2 AF 15 FE 2A 68 31 64 CD 04  ...H.+....*h1d..
33 E8 42 AE 5A 00 B2 90 66 A2 3B 9F              3.B.Z...f.;.

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

12/05-21:15:53.466294 10.10.52.242:22 -> 10.8.19.103:49618
TCP TTL:64 TOS:0x10 ID:54715 IpLen:20 DgmLen:216 DF
***AP*** Seq: 0xE07041ED  Ack: 0xBD7F8804  Win: 0x1D4  TcpLen: 32
TCP Options (3) => NOP NOP TS: 4193525944 3816246954 
39 A6 3A B8 0A D0 CC 1C 46 E0 34 07 16 C3 6B 58  9.:.....F.4...kX
9E 4C 32 AE 7B B4 D4 C4 BB EC CC 61 07 27 1C B7  .L2.{......a.'..
EA 4D BD 12 34 EA 40 4E B4 F0 8C 86 F2 89 3A B8  .M..4.@N......:.
98 27 0F CB 1E 9C C3 66 D5 CB 32 E0 B6 5C 89 55  .'.....f..2..\.U
60 03 39 8D B3 26 50 92 16 8E 82 E8 04 27 C4 52  `.9..&P......'.R
7A 49 85 A4 97 23 4D 16 24 47 AA 8E 3B 8F A9 D7  zI...#M.$G..;...
D0 44 68 55 B0 90 75 46 FB 23 F6 D2 AF B3 A7 2F  .DhU..uF.#...../
71 D0 28 C8 22 2D 74 E6 9B 4B F5 02 38 C3 F9 75  q.(."-t..K..8..u
23 75 F4 ED B5 71 9B C3 0F B9 D2 A0 69 E5 05 06  #u...q......i...
C7 0F EC 2F 45 13 D5 38 26 19 53 06 D9 76 14 C7  .../E..8&.S..v..
80 93 21 5A                                      ..!Z

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.573987 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8575 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE0703F29  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247159 4193525863 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.623821 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8576 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE0703F65  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247206 4193525910 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.624999 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8577 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE0703FD1  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247209 4193525912 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.664128 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8578 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE070400D  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247242 4193525944 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.664129 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8579 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE0704061  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247242 4193525944 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
12/05-21:15:53.664129 10.8.19.103:49618 -> 10.10.52.242:22
TCP TTL:63 TOS:0x10 ID:8580 IpLen:20 DgmLen:52 DF
***A**** Seq: 0xBD7F8804  Ack: 0xE07041ED  Win: 0x1F5  TcpLen: 32
TCP Options (3) => NOP NOP TS: 3816247242 4193525944 

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

===============================================================================
Run time for packet processing was 0.461 seconds
Snort processed 10 packets.
Snort ran for 0 days 0 hours 0 minutes 0 seconds
   Pkts/sec:           10
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      13180928
  Total allocated space (uordblks):      678144
  Total free space (fordblks):           108288
  Topmost releasable block (keepcost):   102304
===============================================================================
Packet I/O Totals:
   Received:           10
   Analyzed:           10 (100.000%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            0 (  0.000%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:           10 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:           10 (100.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:           10 (100.000%)
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
Bad Chk Sum:            4 ( 40.000%)
    Bad TTL:            0 (  0.000%)
     S5 G 1:            0 (  0.000%)
     S5 G 2:            0 (  0.000%)
      Total:           10
===============================================================================
Snort exiting
```
Investigate the traffic with the default configuration file with ASCII mode.
sudo snort -dev -K ASCII -l .
Execute the traffic generator script and choose "TASK-6 Exercise". Wait until the traffic ends, then stop the Snort instance. Now analyse the output summary and answer the question.
sudo ./traffic-generator.sh
Now, you should have the logs in the current directory. Navigate to folder "145.254.160.237". What is the source port used to connect port 53?
You can re-generate the traffic if the expected log is not generated. "sudo ls" can help you! Check the "Logfile Ownership" part in this task to avoid the "permission denied" error.
![[Pasted image 20221205162718.png]]
```text
ubuntu@ip-10-10-52-242:~/Desktop/Task-Exercises$ sudo snort -dev -K ASCII -l .
Running in packet logging mode

        --== Initializing Snort ==--
Initializing Output Plugins!
Log directory = .
pcap DAQ configured to passive.
Acquiring network traffic from "eth0".
Decoding Ethernet

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

Commencing packet processing (pid=7113)
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
(snort_decoder) WARNING: IP dgm len > captured len
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
WARNING: No preprocessors configured for policy 0.
^C*** Caught Int-Signal
WARNING: No preprocessors configured for policy 0.
===============================================================================
Run time for packet processing was 45.79621 seconds
Snort processed 1533 packets.
Snort ran for 0 days 0 hours 0 minutes 45 seconds
   Pkts/sec:           34
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      13180928
  Total allocated space (uordblks):      678528
  Total free space (fordblks):           107904
  Topmost releasable block (keepcost):   107040
===============================================================================
Packet I/O Totals:
   Received:         1559
   Analyzed:         1533 ( 98.332%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:           26 (  1.668%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:         1533 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:         1527 ( 99.609%)
       Frag:            0 (  0.000%)
       ICMP:           68 (  4.436%)
        UDP:            4 (  0.261%)
        TCP:         1362 ( 88.845%)
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
        ARP:            6 (  0.391%)
        IPX:            0 (  0.000%)
   Eth Loop:            0 (  0.000%)
   Eth Disc:            0 (  0.000%)
   IP4 Disc:           93 (  6.067%)
   IP6 Disc:            0 (  0.000%)
   TCP Disc:            0 (  0.000%)
   UDP Disc:            0 (  0.000%)
  ICMP Disc:            0 (  0.000%)
All Discard:           93 (  6.067%)
      Other:            0 (  0.000%)
Bad Chk Sum:          530 ( 34.573%)
    Bad TTL:            0 (  0.000%)
     S5 G 1:            0 (  0.000%)
     S5 G 2:            0 (  0.000%)
      Total:         1533
===============================================================================
Snort exiting

ubuntu@ip-10-10-52-242:~/Desktop/Task-Exercises$ sudo ./traffic-generator.sh
```
```text
# Option “-e” is deprecated and might be removed in a later version of gnome-terminal.
```
```text
# Use “-- ” to terminate the options and put the command line to execute after it.

ubuntu@ip-10-10-52-242:~/Desktop/Task-Exercises$ ls
10.10.52.242  142.250.187.110  172.67.27.10     Config-Sample   PACKET_NONIP
10.100.1.202  145.254.160.237  192.168.175.129  Exercise-Files  traffic-generator.sh
ubuntu@ip-10-10-52-242:~/Desktop/Task-Exercises$ cd 145.254.160.237/
bash: cd: 145.254.160.237/: Permission denied
ubuntu@ip-10-10-52-242:~/Desktop/Task-Exercises$ sudo ls
10.10.52.242  142.250.187.110  172.67.27.10	Config-Sample	PACKET_NONIP
10.100.1.202  145.254.160.237  192.168.175.129	Exercise-Files	traffic-generator.sh

ubuntu@ip-10-10-52-242:~/Desktop/Task-Exercises$ sudo chown ubuntu -R 145.254.160.237/
ubuntu@ip-10-10-52-242:~/Desktop/Task-Exercises$ cd 145.254.160.237/
ubuntu@ip-10-10-52-242:~/Desktop/Task-Exercises/145.254.160.237$ ls
TCP:3371-80  TCP:3372-80  UDP:3009-53
```
*3009*
Use snort.log.1640048004
Read the snort.log file with Snort; what is the IP ID of the 10th packet?
snort -r snort.log.1640048004 -n 10
-n helps to analyse the "n" number of packets. You can view the IP with sniffing mode parameters -v, -d, -e or -X.
```text
root@ip-10-10-52-242:/home/ubuntu/Desktop/Task-Exercises# cd Exercise-Files/
root@ip-10-10-52-242:/home/ubuntu/Desktop/Task-Exercises/Exercise-Files# ls
TASK-5  TASK-6  TASK-7  TASK-8  TASK-9
root@ip-10-10-52-242:/home/ubuntu/Desktop/Task-Exercises/Exercise-Files# cd TASK-6
root@ip-10-10-52-242:/home/ubuntu/Desktop/Task-Exercises/Exercise-Files/TASK-6# ls
snort.log.1640048004
root@ip-10-10-52-242:/home/ubuntu/Desktop/Task-Exercises/Exercise-Files/TASK-6# snort -r snort.log.1640048004 -n 10
Exiting after 10 packets
Running in packet dump mode

        --== Initializing Snort ==--
Initializing Output Plugins!
pcap DAQ configured to read-file.
Acquiring network traffic from "snort.log.1640048004".

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

Commencing packet processing (pid=7165)
WARNING: No preprocessors configured for policy 0.
05/13-10:17:07.311224 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3905 IpLen:20 DgmLen:48 DF
******S* Seq: 0x38AFFE13  Ack: 0x0  Win: 0x2238  TcpLen: 28
TCP Options (4) => MSS: 1460 NOP NOP SackOK 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:08.222534 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:0 IpLen:20 DgmLen:48 DF
***A**S* Seq: 0x114C618B  Ack: 0x38AFFE14  Win: 0x16D0  TcpLen: 28
TCP Options (4) => MSS: 1380 NOP NOP SackOK 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:08.222534 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3908 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFE14  Ack: 0x114C618C  Win: 0x25BC  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:08.222534 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3909 IpLen:20 DgmLen:519 DF
***AP*** Seq: 0x38AFFE14  Ack: 0x114C618C  Win: 0x25BC  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:08.783340 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49310 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x114C618C  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:08.993643 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49311 IpLen:20 DgmLen:1420 DF
***A**** Seq: 0x114C618C  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:09.123830 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3910 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFFF3  Ack: 0x114C66F0  Win: 0x25BC  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:09.123830 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49312 IpLen:20 DgmLen:1420 DF
***A**** Seq: 0x114C66F0  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:09.324118 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3911 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFFF3  Ack: 0x114C6C54  Win: 0x25BC  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:09.754737 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49313 IpLen:20 DgmLen:1420 DF
***A**** Seq: 0x114C6C54  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

===============================================================================
Run time for packet processing was 0.400 seconds
Snort processed 10 packets.
Snort ran for 0 days 0 hours 0 minutes 0 seconds
   Pkts/sec:           10
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      12906496
  Total allocated space (uordblks):      678144
  Total free space (fordblks):           108288
  Topmost releasable block (keepcost):   102304
===============================================================================
Packet I/O Totals:
   Received:           10
   Analyzed:           10 (100.000%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            0 (  0.000%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:           10 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:           10 (100.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:           10 (100.000%)
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
      Total:           10
===============================================================================
Snort exiting

WARNING: No preprocessors configured for policy 0.
05/13-10:17:09.754737 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49313 IpLen:20 DgmLen:1420 DF
***A**** Seq: 0x114C6C54  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20

ID:49313
```
*49313*
Read the "snort.log.1640048004" file with Snort; what is the referer of the 4th packet?
"-X" helps you to display the full packet details.
```text
root@ip-10-10-52-242:/home/ubuntu/Desktop/Task-Exercises/Exercise-Files/TASK-6# snort -r snort.log.1640048004 -n 4 -X
Exiting after 4 packets
Running in packet dump mode

        --== Initializing Snort ==--
Initializing Output Plugins!
pcap DAQ configured to read-file.
Acquiring network traffic from "snort.log.1640048004".

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

Commencing packet processing (pid=7174)
WARNING: No preprocessors configured for policy 0.
05/13-10:17:07.311224 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3905 IpLen:20 DgmLen:48 DF
******S* Seq: 0x38AFFE13  Ack: 0x0  Win: 0x2238  TcpLen: 28
TCP Options (4) => MSS: 1460 NOP NOP SackOK 
0x0000: FE FF 20 00 01 00 00 00 01 00 00 00 08 00 45 00  .. ...........E.
0x0010: 00 30 0F 41 40 00 80 06 91 EB 91 FE A0 ED 41 D0  .0.A@.........A.
0x0020: E4 DF 0D 2C 00 50 38 AF FE 13 00 00 00 00 70 02  ...,.P8.......p.
0x0030: 22 38 C3 0C 00 00 02 04 05 B4 01 01 04 02        "8............

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:08.222534 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:0 IpLen:20 DgmLen:48 DF
***A**S* Seq: 0x114C618B  Ack: 0x38AFFE14  Win: 0x16D0  TcpLen: 28
TCP Options (4) => MSS: 1380 NOP NOP SackOK 
0x0000: 00 00 01 00 00 00 FE FF 20 00 01 00 08 00 45 00  ........ .....E.
0x0010: 00 30 00 00 40 00 2F 06 F2 2C 41 D0 E4 DF 91 FE  .0..@./..,A.....
0x0020: A0 ED 00 50 0D 2C 11 4C 61 8B 38 AF FE 14 70 12  ...P.,.La.8...p.
0x0030: 16 D0 5B DC 00 00 02 04 05 64 01 01 04 02        ..[......d....

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:08.222534 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3908 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFE14  Ack: 0x114C618C  Win: 0x25BC  TcpLen: 20
0x0000: FE FF 20 00 01 00 00 00 01 00 00 00 08 00 45 00  .. ...........E.
0x0010: 00 28 0F 44 40 00 80 06 91 F0 91 FE A0 ED 41 D0  .(.D@.........A.
0x0020: E4 DF 0D 2C 00 50 38 AF FE 14 11 4C 61 8C 50 10  ...,.P8....La.P.
0x0030: 25 BC 79 64 00 00                                %.yd..

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:08.222534 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3909 IpLen:20 DgmLen:519 DF
***AP*** Seq: 0x38AFFE14  Ack: 0x114C618C  Win: 0x25BC  TcpLen: 20
0x0000: FE FF 20 00 01 00 00 00 01 00 00 00 08 00 45 00  .. ...........E.
0x0010: 02 07 0F 45 40 00 80 06 90 10 91 FE A0 ED 41 D0  ...E@.........A.
0x0020: E4 DF 0D 2C 00 50 38 AF FE 14 11 4C 61 8C 50 18  ...,.P8....La.P.
0x0030: 25 BC A9 58 00 00 47 45 54 20 2F 64 6F 77 6E 6C  %..X..GET /downl
0x0040: 6F 61 64 2E 68 74 6D 6C 20 48 54 54 50 2F 31 2E  oad.html HTTP/1.
0x0050: 31 0D 0A 48 6F 73 74 3A 20 77 77 77 2E 65 74 68  1..Host: www.eth
0x0060: 65 72 65 61 6C 2E 63 6F 6D 0D 0A 55 73 65 72 2D  ereal.com..User-
0x0070: 41 67 65 6E 74 3A 20 4D 6F 7A 69 6C 6C 61 2F 35  Agent: Mozilla/5
0x0080: 2E 30 20 28 57 69 6E 64 6F 77 73 3B 20 55 3B 20  .0 (Windows; U; 
0x0090: 57 69 6E 64 6F 77 73 20 4E 54 20 35 2E 31 3B 20  Windows NT 5.1; 
0x00A0: 65 6E 2D 55 53 3B 20 72 76 3A 31 2E 36 29 20 47  en-US; rv:1.6) G
0x00B0: 65 63 6B 6F 2F 32 30 30 34 30 31 31 33 0D 0A 41  ecko/20040113..A
0x00C0: 63 63 65 70 74 3A 20 74 65 78 74 2F 78 6D 6C 2C  ccept: text/xml,
0x00D0: 61 70 70 6C 69 63 61 74 69 6F 6E 2F 78 6D 6C 2C  application/xml,
0x00E0: 61 70 70 6C 69 63 61 74 69 6F 6E 2F 78 68 74 6D  application/xhtm
0x00F0: 6C 2B 78 6D 6C 2C 74 65 78 74 2F 68 74 6D 6C 3B  l+xml,text/html;
0x0100: 71 3D 30 2E 39 2C 74 65 78 74 2F 70 6C 61 69 6E  q=0.9,text/plain
0x0110: 3B 71 3D 30 2E 38 2C 69 6D 61 67 65 2F 70 6E 67  ;q=0.8,image/png
0x0120: 2C 69 6D 61 67 65 2F 6A 70 65 67 2C 69 6D 61 67  ,image/jpeg,imag
0x0130: 65 2F 67 69 66 3B 71 3D 30 2E 32 2C 2A 2F 2A 3B  e/gif;q=0.2,*/*;
0x0140: 71 3D 30 2E 31 0D 0A 41 63 63 65 70 74 2D 4C 61  q=0.1..Accept-La
0x0150: 6E 67 75 61 67 65 3A 20 65 6E 2D 75 73 2C 65 6E  nguage: en-us,en
0x0160: 3B 71 3D 30 2E 35 0D 0A 41 63 63 65 70 74 2D 45  ;q=0.5..Accept-E
0x0170: 6E 63 6F 64 69 6E 67 3A 20 67 7A 69 70 2C 64 65  ncoding: gzip,de
0x0180: 66 6C 61 74 65 0D 0A 41 63 63 65 70 74 2D 43 68  flate..Accept-Ch
0x0190: 61 72 73 65 74 3A 20 49 53 4F 2D 38 38 35 39 2D  arset: ISO-8859-
0x01A0: 31 2C 75 74 66 2D 38 3B 71 3D 30 2E 37 2C 2A 3B  1,utf-8;q=0.7,*;
0x01B0: 71 3D 30 2E 37 0D 0A 4B 65 65 70 2D 41 6C 69 76  q=0.7..Keep-Aliv
0x01C0: 65 3A 20 33 30 30 0D 0A 43 6F 6E 6E 65 63 74 69  e: 300..Connecti
0x01D0: 6F 6E 3A 20 6B 65 65 70 2D 61 6C 69 76 65 0D 0A  on: keep-alive..
0x01E0: 52 65 66 65 72 65 72 3A 20 68 74 74 70 3A 2F 2F  Referer: http://
0x01F0: 77 77 77 2E 65 74 68 65 72 65 61 6C 2E 63 6F 6D  www.ethereal.com
0x0200: 2F 64 65 76 65 6C 6F 70 6D 65 6E 74 2E 68 74 6D  /development.htm
0x0210: 6C 0D 0A 0D 0A                                   l....

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

===============================================================================
Run time for packet processing was 0.278 seconds
Snort processed 4 packets.
Snort ran for 0 days 0 hours 0 minutes 0 seconds
   Pkts/sec:            4
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      13213696
  Total allocated space (uordblks):      678144
  Total free space (fordblks):           108288
  Topmost releasable block (keepcost):   102304
===============================================================================
Packet I/O Totals:
   Received:            4
   Analyzed:            4 (100.000%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            0 (  0.000%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:            4 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:            4 (100.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:            4 (100.000%)
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
      Total:            4
===============================================================================
Snort exiting

http://www.ethereal.com/development.html
```
*http://www.ethereal.com/development.html*
Read the "snort.log.1640048004" file with Snort; what is the Ack number of the 8th packet?
```text
root@ip-10-10-52-242:/home/ubuntu/Desktop/Task-Exercises/Exercise-Files/TASK-6# snort -r snort.log.1640048004 -n 8
Exiting after 8 packets
Running in packet dump mode

        --== Initializing Snort ==--
Initializing Output Plugins!
pcap DAQ configured to read-file.
Acquiring network traffic from "snort.log.1640048004".

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

Commencing packet processing (pid=7182)
WARNING: No preprocessors configured for policy 0.
05/13-10:17:07.311224 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3905 IpLen:20 DgmLen:48 DF
******S* Seq: 0x38AFFE13  Ack: 0x0  Win: 0x2238  TcpLen: 28
TCP Options (4) => MSS: 1460 NOP NOP SackOK 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:08.222534 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:0 IpLen:20 DgmLen:48 DF
***A**S* Seq: 0x114C618B  Ack: 0x38AFFE14  Win: 0x16D0  TcpLen: 28
TCP Options (4) => MSS: 1380 NOP NOP SackOK 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:08.222534 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3908 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFE14  Ack: 0x114C618C  Win: 0x25BC  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:08.222534 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3909 IpLen:20 DgmLen:519 DF
***AP*** Seq: 0x38AFFE14  Ack: 0x114C618C  Win: 0x25BC  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:08.783340 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49310 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x114C618C  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:08.993643 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49311 IpLen:20 DgmLen:1420 DF
***A**** Seq: 0x114C618C  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:09.123830 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3910 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFFF3  Ack: 0x114C66F0  Win: 0x25BC  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:09.123830 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49312 IpLen:20 DgmLen:1420 DF
***A**** Seq: 0x114C66F0  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

===============================================================================
Run time for packet processing was 0.288 seconds
Snort processed 8 packets.
Snort ran for 0 days 0 hours 0 minutes 0 seconds
   Pkts/sec:            8
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      12906496
  Total allocated space (uordblks):      678144
  Total free space (fordblks):           108288
  Topmost releasable block (keepcost):   102304
===============================================================================
Packet I/O Totals:
   Received:            8
   Analyzed:            8 (100.000%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            0 (  0.000%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:            8 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:            8 (100.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:            8 (100.000%)
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
      Total:            8
===============================================================================
Snort exiting

WARNING: No preprocessors configured for policy 0.
05/13-10:17:09.123830 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49312 IpLen:20 DgmLen:1420 DF
***A**** Seq: 0x114C66F0  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20

 Ack: 0x38AFFFF3
```
*0x38AFFFF3*
Read the "snort.log.1640048004" file with Snort; what is the number of the "TCP port 80" packets?
BPF filters will help you to filter the log file. 'tcp and port 80'
```text
root@ip-10-10-52-242:/home/ubuntu/Desktop/Task-Exercises/Exercise-Files/TASK-6# snort -r snort.log.1640048004 'tcp and port 80'
Running in packet dump mode

        --== Initializing Snort ==--
Initializing Output Plugins!
Snort BPF option: tcp and port 80
pcap DAQ configured to read-file.
Acquiring network traffic from "snort.log.1640048004".

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

Commencing packet processing (pid=7190)
WARNING: No preprocessors configured for policy 0.
05/13-10:17:07.311224 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3905 IpLen:20 DgmLen:48 DF
******S* Seq: 0x38AFFE13  Ack: 0x0  Win: 0x2238  TcpLen: 28
TCP Options (4) => MSS: 1460 NOP NOP SackOK 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:08.222534 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:0 IpLen:20 DgmLen:48 DF
***A**S* Seq: 0x114C618B  Ack: 0x38AFFE14  Win: 0x16D0  TcpLen: 28
TCP Options (4) => MSS: 1380 NOP NOP SackOK 
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:08.222534 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3908 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFE14  Ack: 0x114C618C  Win: 0x25BC  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:08.222534 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3909 IpLen:20 DgmLen:519 DF
***AP*** Seq: 0x38AFFE14  Ack: 0x114C618C  Win: 0x25BC  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:08.783340 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49310 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x114C618C  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:08.993643 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49311 IpLen:20 DgmLen:1420 DF
***A**** Seq: 0x114C618C  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:09.123830 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3910 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFFF3  Ack: 0x114C66F0  Win: 0x25BC  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:09.123830 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49312 IpLen:20 DgmLen:1420 DF
***A**** Seq: 0x114C66F0  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:09.324118 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3911 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFFF3  Ack: 0x114C6C54  Win: 0x25BC  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:09.754737 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49313 IpLen:20 DgmLen:1420 DF
***A**** Seq: 0x114C6C54  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:09.864896 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49314 IpLen:20 DgmLen:1420 DF
***AP*** Seq: 0x114C71B8  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:09.864896 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3912 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFFF3  Ack: 0x114C771C  Win: 0x25BC  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:09.945011 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49315 IpLen:20 DgmLen:1420 DF
***A**** Seq: 0x114C771C  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:10.125270 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3914 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFFF3  Ack: 0x114C7C80  Win: 0x25BC  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:10.205385 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49316 IpLen:20 DgmLen:1420 DF
***A**** Seq: 0x114C7C80  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:10.295515 145.254.160.237:3371 -> 216.239.59.99:80
TCP TTL:128 TOS:0x0 ID:3917 IpLen:20 DgmLen:761 DF
***AP*** Seq: 0x36C21E28  Ack: 0x2E6B5384  Win: 0x2238  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:10.325558 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3918 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFFF3  Ack: 0x114C81E4  Win: 0x25BC  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:10.686076 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49317 IpLen:20 DgmLen:1420 DF
***A**** Seq: 0x114C81E4  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:10.806249 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49318 IpLen:20 DgmLen:1420 DF
***AP*** Seq: 0x114C8748  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:10.806249 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3919 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFFF3  Ack: 0x114C8CAC  Win: 0x25BC  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:10.946451 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49319 IpLen:20 DgmLen:1420 DF
***A**** Seq: 0x114C8CAC  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:10.956465 216.239.59.99:80 -> 145.254.160.237:3371
TCP TTL:55 TOS:0x10 ID:34104 IpLen:20 DgmLen:40
***A**** Seq: 0x2E6B5384  Ack: 0x36C220F9  Win: 0x7AE4  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:11.126710 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3920 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFFF3  Ack: 0x114C9210  Win: 0x25BC  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:11.226854 216.239.59.99:80 -> 145.254.160.237:3371
TCP TTL:55 TOS:0x10 ID:34254 IpLen:20 DgmLen:1470
***AP*** Seq: 0x2E6B5384  Ack: 0x36C220F9  Win: 0x7AE4  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:11.266912 216.239.59.99:80 -> 145.254.160.237:3371
TCP TTL:55 TOS:0x10 ID:34255 IpLen:20 DgmLen:200
***AP*** Seq: 0x2E6B591A  Ack: 0x36C220F9  Win: 0x7AE4  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:11.266912 145.254.160.237:3371 -> 216.239.59.99:80
TCP TTL:128 TOS:0x0 ID:3923 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x36C220F9  Ack: 0x2E6B59BA  Win: 0x2238  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:11.417128 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49320 IpLen:20 DgmLen:1420 DF
***AP*** Seq: 0x114C9210  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:11.527286 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3926 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFFF3  Ack: 0x114C9774  Win: 0x25BC  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:11.537300 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49321 IpLen:20 DgmLen:1420 DF
***A**** Seq: 0x114C9774  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:11.667488 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49322 IpLen:20 DgmLen:1420 DF
***A**** Seq: 0x114C9CD8  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:11.667488 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3927 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFFF3  Ack: 0x114CA23C  Win: 0x25BC  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:11.807689 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49323 IpLen:20 DgmLen:1420 DF
***A**** Seq: 0x114CA23C  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:11.807689 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3928 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFFF3  Ack: 0x114CA7A0  Win: 0x25BC  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:12.088092 216.239.59.99:80 -> 145.254.160.237:3371
TCP TTL:55 TOS:0x10 ID:36076 IpLen:20 DgmLen:1470
***AP*** Seq: 0x2E6B5384  Ack: 0x36C220F9  Win: 0x7AE4  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:12.088092 145.254.160.237:3371 -> 216.239.59.99:80
TCP TTL:128 TOS:0x0 ID:3929 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x36C220F9  Ack: 0x2E6B59BA  Win: 0x2238  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:12.158193 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49324 IpLen:20 DgmLen:464 DF
***AP*** Seq: 0x114CA7A0  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:12.328438 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3932 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFFF3  Ack: 0x114CA948  Win: 0x2414  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:25.216971 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:49325 IpLen:20 DgmLen:40 DF
***A***F Seq: 0x114CA948  Ack: 0x38AFFFF3  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:25.216971 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3935 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x38AFFFF3  Ack: 0x114CA949  Win: 0x2414  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:37.374452 145.254.160.237:3372 -> 65.208.228.223:80
TCP TTL:128 TOS:0x0 ID:3938 IpLen:20 DgmLen:40 DF
***A***F Seq: 0x38AFFFF3  Ack: 0x114CA949  Win: 0x2414  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

WARNING: No preprocessors configured for policy 0.
05/13-10:17:37.704928 65.208.228.223:80 -> 145.254.160.237:3372
TCP TTL:47 TOS:0x0 ID:0 IpLen:20 DgmLen:40 DF
***A**** Seq: 0x114CA949  Ack: 0x38AFFFF4  Win: 0x1920  TcpLen: 20
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

===============================================================================
Run time for packet processing was 0.1041 seconds
Snort processed 41 packets.
Snort ran for 0 days 0 hours 0 minutes 0 seconds
   Pkts/sec:           41
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       786432
  Bytes in mapped regions (hblkhd):      12906496
  Total allocated space (uordblks):      680416
  Total free space (fordblks):           106016
  Topmost releasable block (keepcost):   85984
===============================================================================
Packet I/O Totals:
   Received:           41
   Analyzed:           41 (100.000%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:            0 (  0.000%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:           41 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:           41 (100.000%)
       Frag:            0 (  0.000%)
       ICMP:            0 (  0.000%)
        UDP:            0 (  0.000%)
        TCP:           41 (100.000%)
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
      Total:           41
===============================================================================
Snort exiting

Snort processed 41 packets.
```
*41*
### Operation Mode 3: IDS/IPS
Snort in IDS/IPS Mode
Capabilities of Snort are not limited to sniffing and logging the traffic. IDS/IPS mode helps you manage the traffic according to user-defined rules.
Note that (N)IDS/IPS mode depends on the rules and configuration. TASK-10 summarises the essential paths, files and variables. Also, TASK-3 covers configuration testing. Here, we need to understand the operating logic first, and then we will be going into rules in TASK-9.
Let's run Snort in IDS/IPS Mode
NIDS mode parameters are explained in the table below;
Parameter	Description
-c
Defining the configuration file.
-T	Testing the configuration file.
-N	Disable logging.
-D	Background mode.
-A
Alert modes;
full: Full alert mode, providing all possible information about the alert. This one also is the default mode; once you use -A and don't specify any mode, snort uses this mode.
fast:  Fast mode shows the alert message, timestamp, source and destination IP, along with port numbers.
console: Provides fast style alerts on the console screen.
cmg: CMG style, basic header details with payload in hex and text format.
none: Disabling alerting.
Let's start using each parameter and see the difference between them. Snort needs active traffic on your interface, so we need to generate traffic to see Snort in action. To do this, use the traffic-generator script and sniff the traffic.
Once you start running IDS/IPS mode, you need to use rules. As we mentioned earlier, we will use a pre-defined ICMP rule as an example. The defined rule will only generate alerts in any direction of ICMP packet activity.
alert icmp any any <> any any  (msg: "ICMP Packet Found"; sid: 100001; rev:1;)
This rule is located in "/etc/snort/rules/local.rules".
Remember, in this module, we will focus only on the operating modes. The rules are covered in TASK9&10. Snort will create an "alert" file if the traffic flow triggers an alert. One last note; once you start running IPS/IDS mode, the sniffing and logging mode will be semi-passive. However, you can activate the functions using the parameters discussed in previous tasks. (-i, -v, -d, -e, -X, -l, -K ASCII) If you don't remember the purpose of these commands, please revisit TASK4.
IDS/IPS mode with parameter "-c and -T"
Start the Snort instance and test the configuration file. sudo snort -c /etc/snort/snort.conf -T  This command will check your configuration file and prompt it if there is any misconfiguratioın in your current setting. You should be familiar with this command if you covered TASK3. If you don't remember the output of this command, please revisit TASK4.
IDS/IPS mode with parameter "-N"
Start the Snort instance and disable logging by running the following command: sudo snort -c /etc/snort/snort.conf -N
Now run the traffic-generator script as sudo and start ICMP/HTTP traffic. This command will disable logging mode. The rest of the other functions will still be available (if activated).
The command-line output will provide the information requested with the parameters. So, if you activate verbosity (-v) or full packet dump (-X) you will still have the output in the console, but there will be no logs in the log folder.
IDS/IPS mode with parameter "-D"
Start the Snort instance in background mode with the following command: sudo snort -c /etc/snort/snort.conf -D
Now run the traffic-generator script as sudo and start ICMP/HTTP traffic. Once the traffic is generated, snort will start processing the packets and accomplish the given task with additional parameters.
```text
running in background mode

           
user@ubuntu$ sudo snort -c /etc/snort/snort.conf -D

Spawning daemon child...
My daemon child 2898 lives...
Daemon parent exiting (0)
```
The command-line output will provide the information requested with the parameters. So, if you activate verbosity (-v) or full packet dump (-X) with packet logger mode (-l) you will still have the logs in the logs folder, but there will be no output in the console.
Once you start the background mode and want to check the corresponding process, you can easily use the "ps" command as shown below;
```text
running in background mode

           
user@ubuntu$ ps -ef | grep snort

root        2898    1706  0 05:53 ?        00:00:00 snort -c /etc/snort/snort.conf -D
```
If you want to stop the daemon, you can easily use the "kill" command to stop the process.
```text
running in background mode

           
user@ubuntu$ sudo kill -9 2898
```
IDS/IPS mode with parameter "-A"
Remember that there are several alert modes available in snort;
console: Provides fast style alerts on the console screen.
cmg: Provides basic header details with payload in hex and text format.
full: Full alert mode, providing all possible information about the alert.
fast: Fast mode, shows the alert message, timestamp, source and destination ıp along with port numbers.
none: Disabling alerting.
In this section, only the "console" and "cmg" parameters provide alert information in the console. It is impossible to identify the difference between the rest of the alert modes via terminal. Differences can be identified by looking at generated logs.
At the end of this section, we will compare the "full", "fast" and "none" modes. Remember that these parameters don't provide console output, so we will continue to identify the differences through log formats.
IDS/IPS mode with parameter "-A console"
Console mode provides fast style alerts on the console screen. Start the Snort instance in console alert mode (-A console ) with the following command sudo snort -c /etc/snort/snort.conf -A console
Now run the traffic-generator script as sudo and start ICMP/HTTP traffic. Once the traffic is generated, snort will start generating alerts according to provided ruleset defined in the configuration file.
```text
running in console alert mode

           
user@ubuntu$ sudo snort -c /etc/snort/snort.conf -A console
Running in IDS mode

        --== Initializing Snort ==--
Initializing Output Plugins!
Initializing Preprocessors!
Initializing Plug-ins!
Parsing Rules file "/etc/snort/snort.conf"
...
Commencing packet processing (pid=3743)
12/12-02:08:27.577495  [**] [1:366:7] ICMP PING *NIX [**] [Classification: Misc activity] [Priority: 3] {ICMP} 192.168.175.129 -> 142.250.187.110
12/12-02:08:27.577495  [**] [1:10000001:0] ICMP Packet found [**] [Priority: 0] {ICMP} 192.168.175.129 -> 142.250.187.110
12/12-02:08:27.577495  [**] [1:384:5] ICMP PING [**] [Classification: Misc activity] [Priority: 3] {ICMP} 192.168.175.129 -> 142.250.187.110
12/12-02:08:27.609719  [**] [1:10000001:0] ICMP Packet found [**] [Priority: 0] {ICMP} 142.250.187.110 -> 192.168.175.129
^C*** Caught Int-Signal
12/12-02:08:29.595898  [**] [1:366:7] ICMP PING *NIX [**] [Classification: Misc activity] [Priority: 3] {ICMP} 192.168.175.129 -> 142.250.187.110
12/12-02:08:29.595898  [**] [1:10000001:0] ICMP Packet found [**] [Priority: 0] {ICMP} 192.168.175.129 -> 142.250.187.110
12/12-02:08:29.595898  [**] [1:384:5] ICMP PING [**] [Classification: Misc activity] [Priority: 3] {ICMP} 192.168.175.129 -> 142.250.187.110
===============================================================================
Run time for packet processing was 26.25844 seconds
Snort processed 88 packets.
```
IDS/IPS mode with parameter "-A cmg"
Cmg mode provides basic header details with payload in hex and text format. Start the Snort instance in cmg alert mode (-A cmg ) with the following command sudo snort -c /etc/snort/snort.conf -A cmg
Now run the traffic-generator script as sudo and start ICMP/HTTP traffic. Once the traffic is generated, snort will start generating alerts according to provided ruleset defined in the configuration file.
```text
running in cmg alert mode

           
user@ubuntu$ sudo snort -c /etc/snort/snort.conf -A cmg
Running in IDS mode

        --== Initializing Snort ==--
Initializing Output Plugins!
Initializing Preprocessors!
Initializing Plug-ins!
Parsing Rules file "/etc/snort/snort.conf"
...
Commencing packet processing (pid=3743)
12/12-02:23:56.944351  [**] [1:366:7] ICMP PING *NIX [**] [Classification: Misc activity] [Priority: 3] {ICMP} 192.168.175.129 -> 142.250.187.110
12/12-02:23:56.944351 00:0C:29:A5:B7:A2 -> 00:50:56:E1:9B:9D type:0x800 len:0x62
192.168.175.129 -> 142.250.187.110 ICMP TTL:64 TOS:0x0 ID:10393 IpLen:20 DgmLen:84 DF
Type:8  Code:0  ID:4   Seq:1  ECHO
BC CD B5 61 00 00 00 00 CE 68 0E 00 00 00 00 00  ...a.....h......
10 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E 1F  ................
20 21 22 23 24 25 26 27 28 29 2A 2B 2C 2D 2E 2F   !"#$%&'()*+,-./
30 31 32 33 34 35 36 37                          01234567

=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
```
Let's compare the console and cmg outputs before moving on to other alarm types. As you can see in the given outputs above, console mode provides basic header and rule information. Cmg mode provides full packet details along with rule information.
IDS/IPS mode with parameter "-A fast"
Fast mode provides alert messages, timestamps, and source and destination IP addresses. Remember, there is no console output in this mode. Start the Snort instance in fast alert mode (-A fast ) with the following command sudo snort -c /etc/snort/snort.conf -A fast
Now run the traffic-generator script as sudo and start ICMP/HTTP traffic. Once the traffic is generated, snort will start generating alerts according to provided ruleset defined in the configuration file.
```text
running in fast alert mode

           
user@ubuntu$ sudo snort -c /etc/snort/snort.conf -A fast
Running in IDS mode

        --== Initializing Snort ==--
Initializing Output Plugins!
Initializing Preprocessors!
Initializing Plug-ins!
Parsing Rules file "/etc/snort/snort.conf"
...
Commencing packet processing (pid=3743)
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
```
Let's check the alarm file;
As you can see in the given picture above, fast style alerts contain summary information on the action like direction and alert header.
IDS/IPS mode with parameter "-A full"
Full alert mode provides all possible information about the alert. Remember, there is no console output in this mode. Start the Snort instance in full alert mode (-A full ) with the following command sudo snort -c /etc/snort/snort.conf -A full
Now run the traffic-generator script as sudo and start ICMP/HTTP traffic. Once the traffic is generated, snort will start generating alerts according to provided ruleset defined in the configuration file.
```text
running in full alert mode

           
user@ubuntu$ sudo snort -c /etc/snort/snort.conf -A full
Running in IDS mode

        --== Initializing Snort ==--
Initializing Output Plugins!
Initializing Preprocessors!
Initializing Plug-ins!
Parsing Rules file "/etc/snort/snort.conf"
...
Commencing packet processing (pid=3744)
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
```
Let's check the alarm file;
As you can see in the given picture above, full style alerts contain all possible information on the action.
IDS/IPS mode with parameter "-A none"
Disable alerting. This mode doesn't create the alert file. However, it still logs the traffic and creates a log file in binary dump format. Remember, there is no console output in this mode. Start the Snort instance in none alert mode (-A none) with the following command sudo snort -c /etc/snort/snort.conf -A none
Now run the traffic-generator script as sudo and start ICMP/HTTP traffic. Once the traffic is generated, snort will start generating alerts according to provided ruleset defined in the configuration file.
```text
running in none alert mode

           
user@ubuntu$ sudo snort -c /etc/snort/snort.conf -A none
Running in IDS mode

        --== Initializing Snort ==--
Initializing Output Plugins!
Initializing Preprocessors!
Initializing Plug-ins!
Parsing Rules file "/etc/snort/snort.conf"
...
Commencing packet processing (pid=3745)
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
```
As you can see in the picture below, there is no alert file. Snort only generated the log file.
IDS/IPS mode: "Using rule file without configuration file"
It is possible to run the Snort only with rules without a configuration file. Running the Snort in this mode will help you test the user-created rules. However, this mode will provide less performance.
```text
user@ubuntu$ sudo snort -c /etc/snort/rules/local.rules -A console
Running in IDS mode

12/12-12:13:29.167955  [**] [1:10000001:0] ICMP Packet found [**] [Priority: 0] {ICMP} 192.168.175.129 -> 142.250.187.110
12/12-12:13:29.200543  [**] [1:10000001:0] ICMP Packet found [**] [Priority: 0] {ICMP} 142.250.187.110 -> 192.168.175.129
12/12-12:13:30.169785  [**] [1:10000001:0] ICMP Packet found [**] [Priority: 0] {ICMP} 192.168.175.129 -> 142.250.187.110
12/12-12:13:30.201470  [**] [1:10000001:0] ICMP Packet found [**] [Priority: 0] {ICMP} 142.250.187.110 -> 192.168.175.129
12/12-12:13:31.172101  [**] [1:10000001:0] ICMP Packet found [**] [Priority: 0] {ICMP} 192.168.175.129 -> 142.250.187.110
^C*** Caught Int-Signal
```
IPS mode and dropping packets
Snort IPS mode activated with -Q --daq afpacket parameters. You can also activate this mode by editing snort.conf file. However, you don't need to edit snort.conf file in the scope of this room. Review the bonus task or snort manual for further information on daq and advanced configuration settings: -Q --daq afpacket
Activate the Data Acquisition (DAQ) modules and use the afpacket module to use snort as an IPS: -i eth0:eth1
Identifying interfaces note that Snort IPS require at least two interfaces to work. Now run the traffic-generator script as sudo and start ICMP/HTTP traffic.
```text
running IPS mode

           
user@ubuntu$ sudo snort -c /etc/snort/snort.conf -q -Q --daq afpacket -i eth0:eth1 -A console
Running in IPS mode

12/18-07:40:01.527100  [Drop] [**] [1:1000001:0] ICMP Packet found [**] [Priority: 0] {ICMP} 192.168.175.131 -> 192.168.175.2
12/18-07:40:01.552811  [Drop] [**] [1:1000001:0] ICMP Packet found [**] [Priority: 0] {ICMP} 172.217.169.142 -> 192.168.1.18
12/18-07:40:01.566232  [Drop] [**] [1:1000001:0] ICMP Packet found [**] [Priority: 0] {ICMP} 192.168.175.131 -> 192.168.175.2
12/18-07:40:02.517903  [Drop] [**] [1:1000001:0] ICMP Packet found [**] [Priority: 0] {ICMP} 192.168.1.18 -> 172.217.169.142
12/18-07:40:02.550844  [Drop] [**] [1:1000001:0] ICMP Packet found [**] [Priority: 0] {ICMP} 172.217.169.142 -> 192.168.1.18
^C*** Caught Int-Signal
```
As you can see in the picture above, Snort blocked the packets this time. We used the same rule with a different action (drop/reject). Remember, for the scope of this task; our point is the operating mode, not the rule.
Investigate the traffic with the default configuration file.
sudo snort -c /etc/snort/snort.conf -A full -l .
Execute the traffic generator script and choose "TASK-7 Exercise". Wait until the traffic stops, then stop the Snort instance. Now analyse the output summary and answer the question.
sudo ./traffic-generator.sh
What is the number of the detected HTTP GET methods?
Timing is important, you should start the sniffing before the attack and terminate right after the attack. You can read the provided output statistics summary on the console.
```text
ubuntu@ip-10-10-52-242:~/Desktop/Task-Exercises$ sudo snort -c /etc/snort/snort.conf -A full -l .
Running in IDS mode

        --== Initializing Snort ==--
Initializing Output Plugins!
Initializing Preprocessors!
Initializing Plug-ins!
Parsing Rules file "/etc/snort/snort.conf"
PortVar 'HTTP_PORTS' defined :  [ 80:81 311 383 591 593 901 1220 1414 1741 1830 2301 2381 2809 3037 3128 3702 4343 4848 5250 6988 7000:7001 7144:7145 7510 7777 7779 8000 8008 8014 8028 8080 8085 8088 8090 8118 8123 8180:8181 8243 8280 8300 8800 8888 8899 9000 9060 9080 9090:9091 9443 9999 11371 34443:34444 41080 50002 55555 ]
PortVar 'SHELLCODE_PORTS' defined :  [ 0:79 81:65535 ]
PortVar 'ORACLE_PORTS' defined :  [ 1024:65535 ]
PortVar 'SSH_PORTS' defined :  [ 22 ]
PortVar 'FTP_PORTS' defined :  [ 21 2100 3535 ]
PortVar 'SIP_PORTS' defined :  [ 5060:5061 5600 ]
PortVar 'FILE_DATA_PORTS' defined :  [ 80:81 110 143 311 383 591 593 901 1220 1414 1741 1830 2301 2381 2809 3037 3128 3702 4343 4848 5250 6988 7000:7001 7144:7145 7510 7777 7779 8000 8008 8014 8028 8080 8085 8088 8090 8118 8123 8180:8181 8243 8280 8300 8800 8888 8899 9000 9060 9080 9090:9091 9443 9999 11371 34443:34444 41080 50002 55555 ]
PortVar 'GTP_PORTS' defined :  [ 2123 2152 3386 ]
Detection:
   Search-Method = AC-Full-Q
    Split Any/Any group = enabled
    Search-Method-Optimizations = enabled
    Maximum pattern length = 20
Tagged Packet Limit: 256
Loading dynamic engine /usr/lib/snort_dynamicengine/libsf_engine.so... done
Loading all dynamic detection libs from /usr/lib/snort_dynamicrules...
WARNING: No dynamic libraries found in directory /usr/lib/snort_dynamicrules.
  Finished Loading all dynamic detection libs from /usr/lib/snort_dynamicrules
Loading all dynamic preprocessor libs from /usr/lib/snort_dynamicpreprocessor/...
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_ssl_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_sip_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_imap_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_smtp_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_reputation_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_ftptelnet_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_dce2_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_sdf_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_modbus_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_gtp_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_dns_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_dnp3_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_ssh_preproc.so... done
  Loading dynamic preprocessor library /usr/lib/snort_dynamicpreprocessor//libsf_pop_preproc.so... done
  Finished Loading all dynamic preprocessor libs from /usr/lib/snort_dynamicpreprocessor/
Log directory = .
WARNING: ip4 normalizations disabled because not inline.
WARNING: tcp normalizations disabled because not inline.
WARNING: icmp4 normalizations disabled because not inline.
WARNING: ip6 normalizations disabled because not inline.
WARNING: icmp6 normalizations disabled because not inline.
Frag3 global config:
    Max frags: 65536
    Fragment memory cap: 4194304 bytes
Frag3 engine config:
    Bound Address: default
    Target-based policy: WINDOWS
    Fragment timeout: 180 seconds
    Fragment min_ttl:   1
    Fragment Anomalies: Alert
    Overlap Limit:     10
    Min fragment Length:     100
      Max Expected Streams: 768
Stream global config:
    Track TCP sessions: ACTIVE
    Max TCP sessions: 262144
    TCP cache pruning timeout: 30 seconds
    TCP cache nominal timeout: 3600 seconds
    Memcap (for reassembly packet storage): 8388608
    Track UDP sessions: ACTIVE
    Max UDP sessions: 131072
    UDP cache pruning timeout: 30 seconds
    UDP cache nominal timeout: 180 seconds
    Track ICMP sessions: INACTIVE
    Track IP sessions: INACTIVE
    Log info if session memory consumption exceeds 1048576
    Send up to 2 active responses
    Wait at least 5 seconds between responses
    Protocol Aware Flushing: ACTIVE
        Maximum Flush Point: 16000
Stream TCP Policy config:
    Bound Address: default
    Reassembly Policy: WINDOWS
    Timeout: 180 seconds
    Limit on TCP Overlaps: 10
    Maximum number of bytes to queue per session: 1048576
    Maximum number of segs to queue per session: 2621
    Options:
        Require 3-Way Handshake: YES
        3-Way Handshake Timeout: 180
        Detect Anomalies: YES
    Reassembly Ports:
      21 client (Footprint) 
      22 client (Footprint) 
      23 client (Footprint) 
      25 client (Footprint) 
      42 client (Footprint) 
      53 client (Footprint) 
      79 client (Footprint) 
      80 client (Footprint) server (Footprint)
      81 client (Footprint) server (Footprint)
      109 client (Footprint) 
      110 client (Footprint) 
      111 client (Footprint) 
      113 client (Footprint) 
      119 client (Footprint) 
      135 client (Footprint) 
      136 client (Footprint) 
      137 client (Footprint) 
      139 client (Footprint) 
      143 client (Footprint) 
      161 client (Footprint) 
      additional ports configured but not printed.
Stream UDP Policy config:
    Timeout: 180 seconds
HttpInspect Config:
    GLOBAL CONFIG
      Detect Proxy Usage:       NO
      IIS Unicode Map Filename: /etc/snort/unicode.map
      IIS Unicode Map Codepage: 1252
      Memcap used for logging URI and Hostname: 150994944
      Max Gzip Memory: 104857600
      Max Gzip Sessions: 201649
      Gzip Compress Depth: 65535
      Gzip Decompress Depth: 65535
    DEFAULT SERVER CONFIG:
      Server profile: All
      Ports (PAF): 80 81 311 383 591 593 901 1220 1414 1741 1830 2301 2381 2809 3037 3128 3702 4343 4848 5250 6988 7000 7001 7144 7145 7510 7777 7779 8000 8008 8014 8028 8080 8085 8088 8090 8118 8123 8180 8181 8243 8280 8300 8800 8888 8899 9000 9060 9080 9090 9091 9443 9999 11371 34443 34444 41080 50002 55555 
      Server Flow Depth: 0
      Client Flow Depth: 0
      Max Chunk Length: 500000
      Small Chunk Length Evasion: chunk size <= 10, threshold >= 5 times
      Max Header Field Length: 750
      Max Number Header Fields: 100
      Max Number of WhiteSpaces allowed with header folding: 200
      Inspect Pipeline Requests: YES
      URI Discovery Strict Mode: NO
      Allow Proxy Usage: NO
      Disable Alerting: NO
      Oversize Dir Length: 500
      Only inspect URI: NO
      Normalize HTTP Headers: NO
      Inspect HTTP Cookies: YES
      Inspect HTTP Responses: YES
      Extract Gzip from responses: YES
      Decompress response files:   
      Unlimited decompression of gzip data from responses: YES
      Normalize Javascripts in HTTP Responses: YES
      Max Number of WhiteSpaces allowed with Javascript Obfuscation in HTTP responses: 200
      Normalize HTTP Cookies: NO
      Enable XFF and True Client IP: NO
      Log HTTP URI data: NO
      Log HTTP Hostname data: NO
      Extended ASCII code support in URI: NO
      Ascii: YES alert: NO
      Double Decoding: YES alert: NO
      %U Encoding: YES alert: YES
      Bare Byte: YES alert: NO
      UTF 8: YES alert: NO
      IIS Unicode: YES alert: NO
      Multiple Slash: YES alert: NO
      IIS Backslash: YES alert: NO
      Directory Traversal: YES alert: NO
      Web Root Traversal: YES alert: NO
      Apache WhiteSpace: YES alert: NO
      IIS Delimiter: YES alert: NO
      IIS Unicode Map: GLOBAL IIS UNICODE MAP CONFIG
      Non-RFC Compliant Characters: 0x00 0x01 0x02 0x03 0x04 0x05 0x06 0x07 
      Whitespace Characters: 0x09 0x0b 0x0c 0x0d 
rpc_decode arguments:
    Ports to decode RPC on: 111 32770 32771 32772 32773 32774 32775 32776 32777 32778 32779 
    alert_fragments: INACTIVE
    alert_large_fragments: INACTIVE
    alert_incomplete: INACTIVE
    alert_multiple_requests: INACTIVE
FTPTelnet Config:
    GLOBAL CONFIG
      Inspection Type: stateful
      Check for Encrypted Traffic: YES alert: NO
      Continue to check encrypted data: YES
    TELNET CONFIG:
      Ports: 23 
      Are You There Threshold: 20
      Normalize: YES
      Detect Anomalies: YES
    FTP CONFIG:
      FTP Server: default
        Ports (PAF): 21 2100 3535 
        Check for Telnet Cmds: YES alert: YES
        Ignore Telnet Cmd Operations: YES alert: YES
        Ignore open data channels: NO
      FTP Client: default
        Check for Bounce Attacks: YES alert: YES
        Check for Telnet Cmds: YES alert: YES
        Ignore Telnet Cmd Operations: YES alert: YES
        Max Response Length: 256
SMTP Config:
    Ports: 25 465 587 691 
    Inspection Type: Stateful
    Normalize: ATRN AUTH BDAT DATA DEBUG EHLO EMAL ESAM ESND ESOM ETRN EVFY EXPN HELO HELP IDENT MAIL NOOP ONEX QUEU QUIT RCPT RSET SAML SEND STARTTLS SOML TICK TIME TURN TURNME VERB VRFY X-EXPS XADR XAUTH XCIR XEXCH50 XGEN XLICENSE X-LINK2STATE XQUE XSTA XTRN XUSR CHUNKING X-ADAT X-DRCP X-ERCP X-EXCH50 
    Ignore Data: No
    Ignore TLS Data: No
    Ignore SMTP Alerts: No
    Max Command Line Length: 512
    Max Specific Command Line Length: 
       ATRN:255 AUTH:246 BDAT:255 DATA:246 DEBUG:255 
       EHLO:500 EMAL:255 ESAM:255 ESND:255 ESOM:255 
       ETRN:246 EVFY:255 EXPN:255 HELO:500 HELP:500 
       IDENT:255 MAIL:260 NOOP:255 ONEX:246 QUEU:246 
       QUIT:246 RCPT:300 RSET:246 SAML:246 SEND:246 
       SIZE:255 STARTTLS:246 SOML:246 TICK:246 TIME:246 
       TURN:246 TURNME:246 VERB:246 VRFY:255 X-EXPS:246 
       XADR:246 XAUTH:246 XCIR:246 XEXCH50:246 XGEN:246 
       XLICENSE:246 X-LINK2STATE:246 XQUE:246 XSTA:246 XTRN:246 
       XUSR:246 
    Max Header Line Length: 1000
    Max Response Line Length: 512
    X-Link2State Alert: Yes
    Drop on X-Link2State Alert: No
    Alert on commands: None
    Alert on unknown commands: No
    SMTP Memcap: 838860
    MIME Max Mem: 838860
    Base64 Decoding: Enabled
    Base64 Decoding Depth: Unlimited
    Quoted-Printable Decoding: Enabled
    Quoted-Printable Decoding Depth: Unlimited
    Unix-to-Unix Decoding: Enabled
    Unix-to-Unix Decoding Depth: Unlimited
    Non-Encoded MIME attachment Extraction: Enabled
    Non-Encoded MIME attachment Extraction Depth: Unlimited
    Log Attachment filename: Enabled
    Log MAIL FROM Address: Enabled
    Log RCPT TO Addresses: Enabled
    Log Email Headers: Enabled
    Email Hdrs Log Depth: 1464
SSH config: 
    Autodetection: ENABLED
    Challenge-Response Overflow Alert: ENABLED
    SSH1 CRC32 Alert: ENABLED
    Server Version String Overflow Alert: ENABLED
    Protocol Mismatch Alert: ENABLED
    Bad Message Direction Alert: DISABLED
    Bad Payload Size Alert: DISABLED
    Unrecognized Version Alert: DISABLED
    Max Encrypted Packets: 20  
    Max Server Version String Length: 100  
    MaxClientBytes: 19600 (Default) 
    Ports:
	22
DCE/RPC 2 Preprocessor Configuration
  Global Configuration
    DCE/RPC Defragmentation: Enabled
    Memcap: 102400 KB
    Events: co 
    SMB Fingerprint policy: Disabled
  Server Default Configuration
    Policy: WinXP
    Detect ports (PAF)
      SMB: 139 445 
      TCP: 135 
      UDP: 135 
      RPC over HTTP server: 593 
      RPC over HTTP proxy: None
    Autodetect ports (PAF)
      SMB: None
      TCP: 1025-65535 
      UDP: 1025-65535 
      RPC over HTTP server: 1025-65535 
      RPC over HTTP proxy: None
    Invalid SMB shares: C$ D$ ADMIN$ 
    Maximum SMB command chaining: 3 commands
    SMB file inspection: Disabled
DNS config: 
    DNS Client rdata txt Overflow Alert: ACTIVE
    Obsolete DNS RR Types Alert: INACTIVE
    Experimental DNS RR Types Alert: INACTIVE
    Ports: 53
SSLPP config:
    Encrypted packets: not inspected
    Ports:
      443      465      563      636      989
      992      993      994      995     7801
     7802     7900     7901     7902     7903
     7904     7905     7906     7907     7908
     7909     7910     7911     7912     7913
     7914     7915     7916     7917     7918
     7919     7920
    Server side data is trusted
    Maximum SSL Heartbeat length: 0
Sensitive Data preprocessor config: 
    Global Alert Threshold: 25
    Masked Output: DISABLED
SIP config: 
    Max number of sessions: 40000  
    Max number of dialogs in a session: 4 (Default) 
    Status: ENABLED
    Ignore media channel: DISABLED
    Max URI length: 512  
    Max Call ID length: 80  
    Max Request name length: 20 (Default) 
    Max From length: 256 (Default) 
    Max To length: 256 (Default) 
    Max Via length: 1024 (Default) 
    Max Contact length: 512  
    Max Content length: 2048  
    Ports:
	5060	5061	5600
    Methods:
	  invite cancel ack bye register options refer subscribe update join info message notify benotify do qauth sprack publish service unsubscribe prack
IMAP Config:
    Ports: 143 
    IMAP Memcap: 838860
    MIME Max Mem: 838860
    Base64 Decoding: Enabled
    Base64 Decoding Depth: Unlimited
    Quoted-Printable Decoding: Enabled
    Quoted-Printable Decoding Depth: Unlimited
    Unix-to-Unix Decoding: Enabled
    Unix-to-Unix Decoding Depth: Unlimited
    Non-Encoded MIME attachment Extraction: Enabled
    Non-Encoded MIME attachment Extraction Depth: Unlimited
POP Config:
    Ports: 110 
    POP Memcap: 838860
    MIME Max Mem: 838860
    Base64 Decoding: Enabled
    Base64 Decoding Depth: Unlimited
    Quoted-Printable Decoding: Enabled
    Quoted-Printable Decoding Depth: Unlimited
    Unix-to-Unix Decoding: Enabled
    Unix-to-Unix Decoding Depth: Unlimited
    Non-Encoded MIME attachment Extraction: Enabled
    Non-Encoded MIME attachment Extraction Depth: Unlimited
Modbus config: 
    Ports:
	502
DNP3 config: 
    Memcap: 262144
    Check Link-Layer CRCs: ENABLED
    Ports:
	20000

+++++++++++++++++++++++++++++++++++++++++++++++++++
Initializing rule chains...
WARNING: /etc/snort/rules/chat.rules(33) threshold (in rule) is deprecated; use detection_filter instead.

WARNING: /etc/snort/rules/community-sql-injection.rules(6) GID 1 SID 100000106 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-sql-injection.rules(7) GID 1 SID 100000107 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-sql-injection.rules(8) GID 1 SID 100000108 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-sql-injection.rules(9) GID 1 SID 100000109 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-sql-injection.rules(11) GID 1 SID 100000192 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-sql-injection.rules(12) GID 1 SID 100000193 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-sql-injection.rules(13) GID 1 SID 100000194 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-sql-injection.rules(14) GID 1 SID 100000690 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-sql-injection.rules(15) GID 1 SID 100000691 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-client.rules(6) GID 1 SID 100000118 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-client.rules(7) GID 1 SID 100000119 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-client.rules(9) GID 1 SID 100000228 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-client.rules(14) GID 1 SID 100000284 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-client.rules(16) GID 1 SID 100000447 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-client.rules(18) GID 1 SID 100000692 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-client.rules(20) GID 1 SID 100000693 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-client.rules(23) GID 1 SID 100000864 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-iis.rules(7) GID 1 SID 100000138 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-iis.rules(8) GID 1 SID 100000139 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-iis.rules(9) GID 1 SID 100000173 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-iis.rules(10) GID 1 SID 100000174 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(6) GID 1 SID 100000121 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(7) GID 1 SID 100000122 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(8) GID 1 SID 100000129 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(9) GID 1 SID 100000130 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(10) GID 1 SID 100000131 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(12) GID 1 SID 100000132 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(13) GID 1 SID 100000133 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(14) GID 1 SID 100000140 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(15) GID 1 SID 100000141 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(16) GID 1 SID 100000142 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(17) GID 1 SID 100000143 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(18) GID 1 SID 100000144 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(19) GID 1 SID 100000145 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(20) GID 1 SID 100000146 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(22) GID 1 SID 100000148 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(23) GID 1 SID 100000149 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(24) GID 1 SID 100000150 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(25) GID 1 SID 100000177 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(26) GID 1 SID 100000178 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(27) GID 1 SID 100000179 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(28) GID 1 SID 100000184 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(29) GID 1 SID 100000185 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(30) GID 1 SID 100000200 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(31) GID 1 SID 100000209 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(33) GID 1 SID 100000216 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(34) GID 1 SID 100000217 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(35) GID 1 SID 100000225 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(38) GID 1 SID 100000237 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(39) GID 1 SID 100000302 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(40) GID 1 SID 100000303 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(42) GID 1 SID 100000313 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(43) GID 1 SID 100000314 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(49) GID 1 SID 100000317 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(50) GID 1 SID 100000318 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(51) GID 1 SID 100000319 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(52) GID 1 SID 100000320 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(53) GID 1 SID 100000321 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(54) GID 1 SID 100000322 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(55) GID 1 SID 100000323 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(56) GID 1 SID 100000324 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(57) GID 1 SID 100000325 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(58) GID 1 SID 100000326 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(59) GID 1 SID 100000327 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(60) GID 1 SID 100000328 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(61) GID 1 SID 100000329 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(62) GID 1 SID 100000330 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(63) GID 1 SID 100000331 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(64) GID 1 SID 100000332 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(65) GID 1 SID 100000333 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(66) GID 1 SID 100000334 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(67) GID 1 SID 100000335 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(68) GID 1 SID 100000336 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(69) GID 1 SID 100000337 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(70) GID 1 SID 100000338 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(71) GID 1 SID 100000339 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(72) GID 1 SID 100000340 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(73) GID 1 SID 100000341 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(74) GID 1 SID 100000342 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(75) GID 1 SID 100000343 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(76) GID 1 SID 100000344 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(77) GID 1 SID 100000345 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(78) GID 1 SID 100000346 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(79) GID 1 SID 100000347 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(80) GID 1 SID 100000348 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(81) GID 1 SID 100000349 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(82) GID 1 SID 100000350 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(83) GID 1 SID 100000351 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(84) GID 1 SID 100000352 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(85) GID 1 SID 100000353 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(86) GID 1 SID 100000354 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(87) GID 1 SID 100000355 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(88) GID 1 SID 100000356 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(89) GID 1 SID 100000357 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(90) GID 1 SID 100000358 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(91) GID 1 SID 100000359 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(92) GID 1 SID 100000360 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(93) GID 1 SID 100000361 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(94) GID 1 SID 100000362 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(95) GID 1 SID 100000363 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(96) GID 1 SID 100000364 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(97) GID 1 SID 100000365 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(98) GID 1 SID 100000366 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(99) GID 1 SID 100000367 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(100) GID 1 SID 100000368 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(101) GID 1 SID 100000369 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(102) GID 1 SID 100000370 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(103) GID 1 SID 100000371 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(104) GID 1 SID 100000372 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(105) GID 1 SID 100000373 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(106) GID 1 SID 100000374 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(107) GID 1 SID 100000375 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(108) GID 1 SID 100000376 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(109) GID 1 SID 100000377 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(110) GID 1 SID 100000378 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(111) GID 1 SID 100000379 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(112) GID 1 SID 100000380 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(113) GID 1 SID 100000382 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(114) GID 1 SID 100000383 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(115) GID 1 SID 100000384 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(116) GID 1 SID 100000385 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(117) GID 1 SID 100000386 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(119) GID 1 SID 100000387 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(120) GID 1 SID 100000388 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(121) GID 1 SID 100000389 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(122) GID 1 SID 100000390 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(123) GID 1 SID 100000391 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(124) GID 1 SID 100000392 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(125) GID 1 SID 100000393 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(126) GID 1 SID 100000394 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(127) GID 1 SID 100000395 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(128) GID 1 SID 100000396 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(129) GID 1 SID 100000397 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(130) GID 1 SID 100000398 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(131) GID 1 SID 100000399 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(132) GID 1 SID 100000400 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(133) GID 1 SID 100000401 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(134) GID 1 SID 100000402 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(135) GID 1 SID 100000403 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(136) GID 1 SID 100000404 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(137) GID 1 SID 100000405 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(138) GID 1 SID 100000406 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(139) GID 1 SID 100000407 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(140) GID 1 SID 100000408 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(141) GID 1 SID 100000409 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(142) GID 1 SID 100000410 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(143) GID 1 SID 100000411 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(144) GID 1 SID 100000412 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(145) GID 1 SID 100000413 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(146) GID 1 SID 100000414 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(147) GID 1 SID 100000415 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(148) GID 1 SID 100000416 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(149) GID 1 SID 100000417 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(150) GID 1 SID 100000418 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(151) GID 1 SID 100000419 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(152) GID 1 SID 100000420 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(153) GID 1 SID 100000421 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(154) GID 1 SID 100000422 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(155) GID 1 SID 100000423 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(156) GID 1 SID 100000424 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(157) GID 1 SID 100000425 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(158) GID 1 SID 100000426 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(161) GID 1 SID 100000427 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(162) GID 1 SID 100000428 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(163) GID 1 SID 100000429 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(166) GID 1 SID 100000430 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(167) GID 1 SID 100000431 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(168) GID 1 SID 100000432 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(169) GID 1 SID 100000433 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(170) GID 1 SID 100000434 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(171) GID 1 SID 100000435 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(172) GID 1 SID 100000436 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(173) GID 1 SID 100000437 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(174) GID 1 SID 100000438 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(175) GID 1 SID 100000439 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(176) GID 1 SID 100000440 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(177) GID 1 SID 100000441 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(178) GID 1 SID 100000442 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(179) GID 1 SID 100000443 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(180) GID 1 SID 100000444 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(181) GID 1 SID 100000448 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(182) GID 1 SID 100000449 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(183) GID 1 SID 100000450 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(184) GID 1 SID 100000451 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(185) GID 1 SID 100000452 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(186) GID 1 SID 100000453 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(187) GID 1 SID 100000454 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(188) GID 1 SID 100000455 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(189) GID 1 SID 100000456 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(190) GID 1 SID 100000457 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(191) GID 1 SID 100000458 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(192) GID 1 SID 100000459 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(193) GID 1 SID 100000460 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(194) GID 1 SID 100000461 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(195) GID 1 SID 100000462 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(196) GID 1 SID 100000694 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(197) GID 1 SID 100000695 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(198) GID 1 SID 100000696 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(199) GID 1 SID 100000697 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(200) GID 1 SID 100000698 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(201) GID 1 SID 100000699 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(202) GID 1 SID 100000700 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(203) GID 1 SID 100000701 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(204) GID 1 SID 100000702 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(207) GID 1 SID 100000890 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(208) GID 1 SID 100000891 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(211) GID 1 SID 100000895 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(212) GID 1 SID 100000896 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(213) GID 1 SID 100000897 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(214) GID 1 SID 100000898 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-misc.rules(215) GID 1 SID 100000899 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(6) GID 1 SID 100000151 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(7) GID 1 SID 100000186 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(8) GID 1 SID 100000187 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(9) GID 1 SID 100000188 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(10) GID 1 SID 100000195 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(11) GID 1 SID 100000201 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(12) GID 1 SID 100000202 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(13) GID 1 SID 100000203 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(14) GID 1 SID 100000204 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(15) GID 1 SID 100000205 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(16) GID 1 SID 100000206 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(17) GID 1 SID 100000211 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(18) GID 1 SID 100000212 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(19) GID 1 SID 100000213 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(20) GID 1 SID 100000214 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(21) GID 1 SID 100000218 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(22) GID 1 SID 100000220 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(23) GID 1 SID 100000221 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(24) GID 1 SID 100000285 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(25) GID 1 SID 100000286 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(26) GID 1 SID 100000287 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(27) GID 1 SID 100000288 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(28) GID 1 SID 100000289 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(29) GID 1 SID 100000290 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(30) GID 1 SID 100000291 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(31) GID 1 SID 100000292 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(32) GID 1 SID 100000293 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(33) GID 1 SID 100000294 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(34) GID 1 SID 100000295 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(35) GID 1 SID 100000296 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(36) GID 1 SID 100000297 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(37) GID 1 SID 100000298 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(38) GID 1 SID 100000299 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(39) GID 1 SID 100000300 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(40) GID 1 SID 100000304 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(41) GID 1 SID 100000305 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(42) GID 1 SID 100000306 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(43) GID 1 SID 100000307 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(44) GID 1 SID 100000308 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(45) GID 1 SID 100000309 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(46) GID 1 SID 100000445 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(48) GID 1 SID 100000463 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(49) GID 1 SID 100000464 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(50) GID 1 SID 100000465 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(51) GID 1 SID 100000466 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(52) GID 1 SID 100000467 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(53) GID 1 SID 100000468 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(54) GID 1 SID 100000469 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(55) GID 1 SID 100000470 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(56) GID 1 SID 100000471 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(57) GID 1 SID 100000472 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(58) GID 1 SID 100000473 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(59) GID 1 SID 100000474 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(60) GID 1 SID 100000475 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(61) GID 1 SID 100000476 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(62) GID 1 SID 100000477 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(63) GID 1 SID 100000478 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(64) GID 1 SID 100000479 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(65) GID 1 SID 100000480 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(66) GID 1 SID 100000481 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(67) GID 1 SID 100000482 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(68) GID 1 SID 100000483 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(69) GID 1 SID 100000484 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(70) GID 1 SID 100000485 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(71) GID 1 SID 100000486 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(72) GID 1 SID 100000487 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(73) GID 1 SID 100000488 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(74) GID 1 SID 100000489 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(75) GID 1 SID 100000490 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(76) GID 1 SID 100000491 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(77) GID 1 SID 100000492 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(78) GID 1 SID 100000493 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(79) GID 1 SID 100000494 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(80) GID 1 SID 100000495 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(81) GID 1 SID 100000496 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(82) GID 1 SID 100000497 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(83) GID 1 SID 100000498 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(84) GID 1 SID 100000499 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(85) GID 1 SID 100000500 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(86) GID 1 SID 100000501 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(87) GID 1 SID 100000502 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(88) GID 1 SID 100000503 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(89) GID 1 SID 100000504 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(90) GID 1 SID 100000505 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(91) GID 1 SID 100000506 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(92) GID 1 SID 100000507 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(93) GID 1 SID 100000508 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(94) GID 1 SID 100000509 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(95) GID 1 SID 100000510 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(96) GID 1 SID 100000511 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(97) GID 1 SID 100000512 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(98) GID 1 SID 100000513 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(99) GID 1 SID 100000514 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(100) GID 1 SID 100000515 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(101) GID 1 SID 100000516 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(102) GID 1 SID 100000517 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(103) GID 1 SID 100000518 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(104) GID 1 SID 100000519 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(105) GID 1 SID 100000520 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(106) GID 1 SID 100000521 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(107) GID 1 SID 100000522 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(108) GID 1 SID 100000523 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(109) GID 1 SID 100000524 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(110) GID 1 SID 100000525 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(111) GID 1 SID 100000526 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(112) GID 1 SID 100000527 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(113) GID 1 SID 100000528 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(114) GID 1 SID 100000529 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(115) GID 1 SID 100000530 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(116) GID 1 SID 100000531 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(117) GID 1 SID 100000532 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(118) GID 1 SID 100000533 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(119) GID 1 SID 100000534 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(120) GID 1 SID 100000535 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(121) GID 1 SID 100000536 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(122) GID 1 SID 100000537 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(123) GID 1 SID 100000538 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(124) GID 1 SID 100000539 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(125) GID 1 SID 100000540 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(126) GID 1 SID 100000541 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(127) GID 1 SID 100000542 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(128) GID 1 SID 100000543 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(129) GID 1 SID 100000544 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(130) GID 1 SID 100000545 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(131) GID 1 SID 100000546 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(132) GID 1 SID 100000547 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(133) GID 1 SID 100000548 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(134) GID 1 SID 100000549 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(135) GID 1 SID 100000550 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(136) GID 1 SID 100000551 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(137) GID 1 SID 100000552 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(138) GID 1 SID 100000553 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(139) GID 1 SID 100000554 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(140) GID 1 SID 100000555 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(141) GID 1 SID 100000556 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(142) GID 1 SID 100000557 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(143) GID 1 SID 100000558 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(144) GID 1 SID 100000559 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(145) GID 1 SID 100000560 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(146) GID 1 SID 100000561 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(147) GID 1 SID 100000562 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(148) GID 1 SID 100000563 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(149) GID 1 SID 100000564 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(150) GID 1 SID 100000565 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(151) GID 1 SID 100000566 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(152) GID 1 SID 100000567 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(153) GID 1 SID 100000568 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(154) GID 1 SID 100000569 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(155) GID 1 SID 100000570 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(156) GID 1 SID 100000571 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(157) GID 1 SID 100000572 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(158) GID 1 SID 100000573 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(159) GID 1 SID 100000574 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(160) GID 1 SID 100000575 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(161) GID 1 SID 100000576 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(162) GID 1 SID 100000577 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(163) GID 1 SID 100000578 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(164) GID 1 SID 100000579 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(165) GID 1 SID 100000580 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(166) GID 1 SID 100000581 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(167) GID 1 SID 100000582 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(168) GID 1 SID 100000583 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(169) GID 1 SID 100000584 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(170) GID 1 SID 100000585 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(171) GID 1 SID 100000586 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(172) GID 1 SID 100000587 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(173) GID 1 SID 100000588 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(174) GID 1 SID 100000589 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(175) GID 1 SID 100000590 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(176) GID 1 SID 100000591 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(177) GID 1 SID 100000592 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(178) GID 1 SID 100000593 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(179) GID 1 SID 100000594 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(180) GID 1 SID 100000595 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(181) GID 1 SID 100000596 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(182) GID 1 SID 100000597 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(183) GID 1 SID 100000598 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(184) GID 1 SID 100000599 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(185) GID 1 SID 100000600 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(186) GID 1 SID 100000601 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(187) GID 1 SID 100000602 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(188) GID 1 SID 100000603 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(189) GID 1 SID 100000604 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(190) GID 1 SID 100000605 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(191) GID 1 SID 100000606 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(192) GID 1 SID 100000607 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(193) GID 1 SID 100000608 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(194) GID 1 SID 100000609 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(195) GID 1 SID 100000610 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(196) GID 1 SID 100000611 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(197) GID 1 SID 100000612 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(198) GID 1 SID 100000613 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(199) GID 1 SID 100000614 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(200) GID 1 SID 100000615 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(201) GID 1 SID 100000616 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(202) GID 1 SID 100000617 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(203) GID 1 SID 100000618 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(204) GID 1 SID 100000619 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(205) GID 1 SID 100000620 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(206) GID 1 SID 100000621 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(207) GID 1 SID 100000622 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(208) GID 1 SID 100000623 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(209) GID 1 SID 100000624 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(210) GID 1 SID 100000625 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(211) GID 1 SID 100000626 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(212) GID 1 SID 100000627 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(213) GID 1 SID 100000628 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(214) GID 1 SID 100000629 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(215) GID 1 SID 100000630 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(216) GID 1 SID 100000631 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(217) GID 1 SID 100000632 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(218) GID 1 SID 100000633 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(219) GID 1 SID 100000634 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(220) GID 1 SID 100000635 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(221) GID 1 SID 100000636 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(222) GID 1 SID 100000637 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(223) GID 1 SID 100000638 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(224) GID 1 SID 100000639 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(225) GID 1 SID 100000640 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(226) GID 1 SID 100000641 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(227) GID 1 SID 100000642 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(228) GID 1 SID 100000643 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(229) GID 1 SID 100000644 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(230) GID 1 SID 100000645 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(231) GID 1 SID 100000646 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(232) GID 1 SID 100000647 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(233) GID 1 SID 100000648 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(234) GID 1 SID 100000649 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(235) GID 1 SID 100000650 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(236) GID 1 SID 100000651 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(237) GID 1 SID 100000652 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(238) GID 1 SID 100000653 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(239) GID 1 SID 100000654 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(240) GID 1 SID 100000655 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(241) GID 1 SID 100000656 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(242) GID 1 SID 100000657 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(243) GID 1 SID 100000658 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(244) GID 1 SID 100000659 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(245) GID 1 SID 100000660 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(246) GID 1 SID 100000661 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(247) GID 1 SID 100000662 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(248) GID 1 SID 100000663 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(249) GID 1 SID 100000664 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(250) GID 1 SID 100000665 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(251) GID 1 SID 100000666 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(252) GID 1 SID 100000667 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(253) GID 1 SID 100000668 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(254) GID 1 SID 100000669 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(255) GID 1 SID 100000670 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(256) GID 1 SID 100000671 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(257) GID 1 SID 100000672 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(258) GID 1 SID 100000673 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(259) GID 1 SID 100000674 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(260) GID 1 SID 100000675 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(261) GID 1 SID 100000676 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(262) GID 1 SID 100000677 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(263) GID 1 SID 100000678 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(264) GID 1 SID 100000679 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(265) GID 1 SID 100000680 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(266) GID 1 SID 100000681 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(267) GID 1 SID 100000682 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(268) GID 1 SID 100000683 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(270) GID 1 SID 100000703 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(271) GID 1 SID 100000704 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(272) GID 1 SID 100000705 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(273) GID 1 SID 100000706 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(274) GID 1 SID 100000707 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(275) GID 1 SID 100000708 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(276) GID 1 SID 100000709 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(277) GID 1 SID 100000710 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(278) GID 1 SID 100000711 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(279) GID 1 SID 100000712 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(280) GID 1 SID 100000713 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(281) GID 1 SID 100000714 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(282) GID 1 SID 100000715 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(283) GID 1 SID 100000716 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(284) GID 1 SID 100000717 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(285) GID 1 SID 100000718 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(286) GID 1 SID 100000719 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(287) GID 1 SID 100000720 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(288) GID 1 SID 100000721 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(289) GID 1 SID 100000722 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(290) GID 1 SID 100000723 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(291) GID 1 SID 100000724 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(292) GID 1 SID 100000725 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(293) GID 1 SID 100000726 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(294) GID 1 SID 100000727 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(295) GID 1 SID 100000728 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(296) GID 1 SID 100000729 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(297) GID 1 SID 100000730 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(298) GID 1 SID 100000731 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(299) GID 1 SID 100000732 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(300) GID 1 SID 100000733 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(301) GID 1 SID 100000734 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(302) GID 1 SID 100000735 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(303) GID 1 SID 100000736 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(304) GID 1 SID 100000737 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(305) GID 1 SID 100000738 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(306) GID 1 SID 100000739 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(307) GID 1 SID 100000740 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(308) GID 1 SID 100000741 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(309) GID 1 SID 100000742 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(310) GID 1 SID 100000743 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(311) GID 1 SID 100000744 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(312) GID 1 SID 100000745 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(313) GID 1 SID 100000746 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(314) GID 1 SID 100000747 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(315) GID 1 SID 100000748 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(316) GID 1 SID 100000749 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(317) GID 1 SID 100000750 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(318) GID 1 SID 100000751 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(319) GID 1 SID 100000752 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(320) GID 1 SID 100000753 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(321) GID 1 SID 100000754 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(322) GID 1 SID 100000755 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(323) GID 1 SID 100000756 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(324) GID 1 SID 100000757 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(325) GID 1 SID 100000758 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(326) GID 1 SID 100000759 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(327) GID 1 SID 100000760 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(328) GID 1 SID 100000761 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(329) GID 1 SID 100000762 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(330) GID 1 SID 100000763 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(331) GID 1 SID 100000764 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(332) GID 1 SID 100000765 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(333) GID 1 SID 100000766 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(334) GID 1 SID 100000767 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(335) GID 1 SID 100000768 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(336) GID 1 SID 100000769 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(337) GID 1 SID 100000770 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(338) GID 1 SID 100000771 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(339) GID 1 SID 100000772 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(340) GID 1 SID 100000773 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(341) GID 1 SID 100000774 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(342) GID 1 SID 100000775 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(343) GID 1 SID 100000776 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(344) GID 1 SID 100000777 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(345) GID 1 SID 100000778 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(346) GID 1 SID 100000779 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(347) GID 1 SID 100000780 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(348) GID 1 SID 100000781 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(349) GID 1 SID 100000782 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(350) GID 1 SID 100000783 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(351) GID 1 SID 100000784 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(352) GID 1 SID 100000785 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(353) GID 1 SID 100000786 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(354) GID 1 SID 100000787 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(355) GID 1 SID 100000788 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(356) GID 1 SID 100000789 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(357) GID 1 SID 100000790 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(358) GID 1 SID 100000791 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(359) GID 1 SID 100000792 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(360) GID 1 SID 100000793 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(361) GID 1 SID 100000794 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(362) GID 1 SID 100000795 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(363) GID 1 SID 100000796 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(364) GID 1 SID 100000797 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(365) GID 1 SID 100000798 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(366) GID 1 SID 100000799 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(367) GID 1 SID 100000800 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(368) GID 1 SID 100000801 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(369) GID 1 SID 100000802 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(370) GID 1 SID 100000803 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(371) GID 1 SID 100000804 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(372) GID 1 SID 100000805 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(373) GID 1 SID 100000806 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(374) GID 1 SID 100000807 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(375) GID 1 SID 100000808 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(376) GID 1 SID 100000809 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(377) GID 1 SID 100000810 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(378) GID 1 SID 100000811 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(379) GID 1 SID 100000812 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(380) GID 1 SID 100000813 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(381) GID 1 SID 100000814 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(382) GID 1 SID 100000815 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(383) GID 1 SID 100000816 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(384) GID 1 SID 100000817 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(385) GID 1 SID 100000818 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(386) GID 1 SID 100000820 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(387) GID 1 SID 100000821 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(388) GID 1 SID 100000822 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(389) GID 1 SID 100000823 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(390) GID 1 SID 100000824 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(391) GID 1 SID 100000825 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(392) GID 1 SID 100000826 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(393) GID 1 SID 100000827 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(394) GID 1 SID 100000828 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(395) GID 1 SID 100000829 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(396) GID 1 SID 100000830 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(397) GID 1 SID 100000831 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(398) GID 1 SID 100000832 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(399) GID 1 SID 100000833 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(400) GID 1 SID 100000834 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(401) GID 1 SID 100000835 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(402) GID 1 SID 100000836 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(403) GID 1 SID 100000837 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(404) GID 1 SID 100000838 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(405) GID 1 SID 100000839 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(406) GID 1 SID 100000840 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(407) GID 1 SID 100000841 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(408) GID 1 SID 100000842 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(409) GID 1 SID 100000843 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(410) GID 1 SID 100000844 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(411) GID 1 SID 100000845 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(412) GID 1 SID 100000846 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(413) GID 1 SID 100000847 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(414) GID 1 SID 100000849 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(415) GID 1 SID 100000850 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(416) GID 1 SID 100000851 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(417) GID 1 SID 100000852 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(418) GID 1 SID 100000853 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(419) GID 1 SID 100000854 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(420) GID 1 SID 100000855 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(421) GID 1 SID 100000856 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(422) GID 1 SID 100000857 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(423) GID 1 SID 100000858 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(424) GID 1 SID 100000859 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(425) GID 1 SID 100000860 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(426) GID 1 SID 100000861 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(427) GID 1 SID 100000862 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(428) GID 1 SID 100000863 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(431) GID 1 SID 100000865 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(432) GID 1 SID 100000866 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(433) GID 1 SID 100000867 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(434) GID 1 SID 100000868 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(435) GID 1 SID 100000869 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(436) GID 1 SID 100000870 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(437) GID 1 SID 100000871 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(438) GID 1 SID 100000872 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(439) GID 1 SID 100000873 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(441) GID 1 SID 100000882 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(443) GID 1 SID 100000883 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(444) GID 1 SID 100000884 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(445) GID 1 SID 100000885 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(446) GID 1 SID 100000886 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(447) GID 1 SID 100000887 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(448) GID 1 SID 100000888 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(449) GID 1 SID 100000889 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(450) GID 1 SID 100000906 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(451) GID 1 SID 100000907 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(452) GID 1 SID 100000908 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(453) GID 1 SID 100000909 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(454) GID 1 SID 100000910 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(455) GID 1 SID 100000911 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(456) GID 1 SID 100000912 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(457) GID 1 SID 100000913 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(458) GID 1 SID 100000914 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(459) GID 1 SID 100000915 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(460) GID 1 SID 100000916 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(461) GID 1 SID 100000917 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(462) GID 1 SID 100000918 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(463) GID 1 SID 100000919 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(464) GID 1 SID 100000920 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(465) GID 1 SID 100000921 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(466) GID 1 SID 100000922 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(467) GID 1 SID 100000925 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(468) GID 1 SID 100000926 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(469) GID 1 SID 100000929 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(470) GID 1 SID 100000930 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(471) GID 1 SID 100000931 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(472) GID 1 SID 100000932 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(473) GID 1 SID 100000933 in rule duplicates previous rule. Ignoring old rule.

WARNING: /etc/snort/rules/community-web-php.rules(474) GID 1 SID 100000934 in rule duplicates previous rule. Ignoring old rule.

4151 Snort rules read
    3477 detection rules
    0 decoder rules
    0 preprocessor rules
3477 Option Chains linked into 271 Chain Headers
0 Dynamic rules
+++++++++++++++++++++++++++++++++++++++++++++++++++

+-------------------[Rule Port Counts]---------------------------------------
|             tcp     udp    icmp      ip
|     src     151      18       0       0
|     dst    3306     126       0       0
|     any     383      48     146      22
|      nc      27       8      95      20
|     s+d      12       5       0       0
+----------------------------------------------------------------------------

+-----------------------[detection-filter-config]------------------------------
| memory-cap : 1048576 bytes
+-----------------------[detection-filter-rules]-------------------------------
| none
-------------------------------------------------------------------------------

+-----------------------[rate-filter-config]-----------------------------------
| memory-cap : 1048576 bytes
+-----------------------[rate-filter-rules]------------------------------------
| none
-------------------------------------------------------------------------------

+-----------------------[event-filter-config]----------------------------------
| memory-cap : 1048576 bytes
+-----------------------[event-filter-global]----------------------------------
| none
+-----------------------[event-filter-local]-----------------------------------
| gen-id=1      sig-id=2275       type=Threshold tracking=dst count=5   seconds=60 
| gen-id=1      sig-id=2924       type=Threshold tracking=dst count=10  seconds=60 
| gen-id=1      sig-id=3152       type=Threshold tracking=src count=5   seconds=2  
| gen-id=1      sig-id=2496       type=Both      tracking=dst count=20  seconds=60 
| gen-id=1      sig-id=2523       type=Both      tracking=dst count=10  seconds=10 
| gen-id=1      sig-id=1991       type=Limit     tracking=src count=1   seconds=60 
| gen-id=1      sig-id=3273       type=Threshold tracking=src count=5   seconds=2  
| gen-id=1      sig-id=2494       type=Both      tracking=dst count=20  seconds=60 
| gen-id=1      sig-id=2495       type=Both      tracking=dst count=20  seconds=60 
| gen-id=1      sig-id=2923       type=Threshold tracking=dst count=10  seconds=60 
+-----------------------[suppression]------------------------------------------
| none
-------------------------------------------------------------------------------
Rule application order: activation->dynamic->pass->drop->sdrop->reject->alert->log
Verifying Preprocessor Configurations!
WARNING: flowbits key 'ms_sql_seen_dns' is checked but not ever set.
WARNING: flowbits key 'smb.tree.create.llsrpc' is set but not ever checked.
33 out of 1024 flowbits in use.

[ Port Based Pattern Matching Memory ]
+- [ Aho-Corasick Summary ] -------------------------------------
| Storage Format    : Full-Q 
| Finite Automaton  : DFA
| Alphabet Size     : 256 Chars
| Sizeof State      : Variable (1,2,4 bytes)
| Instances         : 215
|     1 byte states : 204
|     2 byte states : 11
|     4 byte states : 0
| Characters        : 64982
| States            : 32135
| Transitions       : 872051
| State Density     : 10.6%
| Patterns          : 5055
| Match States      : 3855
| Memory (MB)       : 17.00
|   Patterns        : 0.51
|   Match Lists     : 1.02
|   DFA
|     1 byte states : 1.02
|     2 byte states : 14.05
|     4 byte states : 0.00
+----------------------------------------------------------------
[ Number of patterns truncated to 20 bytes: 1039 ]
pcap DAQ configured to passive.
Acquiring network traffic from "eth0".
Reload thread starting...
Reload thread started, thread 0x7f92e1ca4700 (7243)
Decoding Ethernet

        --== Initialization Complete ==--

   ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.7.0 GRE (Build 149) 
   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
           Copyright (C) 2014 Cisco and/or its affiliates. All rights reserved.
           Copyright (C) 1998-2013 Sourcefire, Inc., et al.
           Using libpcap version 1.9.1 (with TPACKET_V3)
           Using PCRE version: 8.39 2016-06-14
           Using ZLIB version: 1.2.11

           Rules Engine: SF_SNORT_DETECTION_ENGINE  Version 2.4  <Build 1>
           Preprocessor Object: SF_POP  Version 1.0  <Build 1>
           Preprocessor Object: SF_SSH  Version 1.1  <Build 3>
           Preprocessor Object: SF_DNP3  Version 1.1  <Build 1>
           Preprocessor Object: SF_DNS  Version 1.1  <Build 4>
           Preprocessor Object: SF_GTP  Version 1.1  <Build 1>
           Preprocessor Object: SF_MODBUS  Version 1.1  <Build 1>
           Preprocessor Object: SF_SDF  Version 1.1  <Build 1>
           Preprocessor Object: SF_DCERPC2  Version 1.0  <Build 3>
           Preprocessor Object: SF_FTPTELNET  Version 1.2  <Build 13>
           Preprocessor Object: SF_REPUTATION  Version 1.1  <Build 1>
           Preprocessor Object: SF_SMTP  Version 1.1  <Build 9>
           Preprocessor Object: SF_IMAP  Version 1.0  <Build 1>
           Preprocessor Object: SF_SIP  Version 1.1  <Build 1>
           Preprocessor Object: SF_SSLPP  Version 1.1  <Build 4>
Commencing packet processing (pid=7235)
^C*** Caught Int-Signal
===============================================================================
Run time for packet processing was 56.8457 seconds
Snort processed 1575 packets.
Snort ran for 0 days 0 hours 0 minutes 56 seconds
   Pkts/sec:           28
===============================================================================
Memory usage summary:
  Total non-mmapped bytes (arena):       44691456
  Bytes in mapped regions (hblkhd):      13574144
  Total allocated space (uordblks):      40376656
  Total free space (fordblks):           4314800
  Topmost releasable block (keepcost):   78912
===============================================================================
Packet I/O Totals:
   Received:         1627
   Analyzed:         1575 ( 96.804%)
    Dropped:            0 (  0.000%)
   Filtered:            0 (  0.000%)
Outstanding:           52 (  3.196%)
   Injected:            0
===============================================================================
Breakdown by protocol (includes rebuilt packets):
        Eth:         1580 (100.000%)
       VLAN:            0 (  0.000%)
        IP4:         1574 ( 99.620%)
       Frag:            0 (  0.000%)
       ICMP:           68 (  4.304%)
        UDP:            4 (  0.253%)
        TCP:         1359 ( 86.013%)
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
        ARP:            6 (  0.380%)
        IPX:            0 (  0.000%)
   Eth Loop:            0 (  0.000%)
   Eth Disc:            0 (  0.000%)
   IP4 Disc:          143 (  9.051%)
   IP6 Disc:            0 (  0.000%)
   TCP Disc:            0 (  0.000%)
   UDP Disc:            0 (  0.000%)
  ICMP Disc:            0 (  0.000%)
All Discard:          143 (  9.051%)
      Other:            0 (  0.000%)
Bad Chk Sum:          487 ( 30.823%)
    Bad TTL:            0 (  0.000%)
     S5 G 1:            4 (  0.253%)
     S5 G 2:            1 (  0.063%)
      Total:         1580
===============================================================================
Action Stats:
     Alerts:          170 ( 10.759%)
     Logged:          170 ( 10.759%)
     Passed:            0 (  0.000%)
Limits:
      Match:            0
      Queue:            0
        Log:            0
      Event:            0
      Alert:            0
Verdicts:
      Allow:         1575 ( 96.804%)
      Block:            0 (  0.000%)
    Replace:            0 (  0.000%)
  Whitelist:            0 (  0.000%)
  Blacklist:            0 (  0.000%)
     Ignore:            0 (  0.000%)
      Retry:            0 (  0.000%)
===============================================================================
Frag3 statistics:
        Total Fragments: 0
      Frags Reassembled: 0
               Discards: 0
          Memory Faults: 0
               Timeouts: 0
               Overlaps: 0
              Anomalies: 0
                 Alerts: 0
                  Drops: 0
     FragTrackers Added: 0
    FragTrackers Dumped: 0
FragTrackers Auto Freed: 0
    Frag Nodes Inserted: 0
     Frag Nodes Deleted: 0
===============================================================================
===============================================================================
Stream statistics:
            Total sessions: 9
              TCP sessions: 7
              UDP sessions: 2
             ICMP sessions: 0
               IP sessions: 0
                TCP Prunes: 0
                UDP Prunes: 0
               ICMP Prunes: 0
                 IP Prunes: 0
TCP StreamTrackers Created: 7
TCP StreamTrackers Deleted: 7
              TCP Timeouts: 0
              TCP Overlaps: 0
       TCP Segments Queued: 414
     TCP Segments Released: 414
       TCP Rebuilt Packets: 5
         TCP Segments Used: 18
              TCP Discards: 1
                  TCP Gaps: 0
      UDP Sessions Created: 2
      UDP Sessions Deleted: 2
              UDP Timeouts: 0
              UDP Discards: 0
                    Events: 96
           Internal Events: 0
           TCP Port Filter
                  Filtered: 0
                 Inspected: 0
                   Tracked: 868
           UDP Port Filter
                  Filtered: 0
                 Inspected: 0
                   Tracked: 2
===============================================================================
HTTP Inspect - encodings (Note: stream-reassembled packets included):
    POST methods:                         0         
    GET methods:                          2         
    HTTP Request Headers extracted:       2         
    HTTP Request Cookies extracted:       0         
    Post parameters extracted:            0         
    HTTP response Headers extracted:      3         
    HTTP Response Cookies extracted:      0         
    Unicode:                              0         
    Double unicode:                       0         
    Non-ASCII representable:              0         
    Directory traversals:                 0         
    Extra slashes ("//"):                 1         
    Self-referencing paths ("./"):        0         
    HTTP Response Gzip packets extracted: 1         
    Gzip Compressed Data Processed:       1272.00   
    Gzip Decompressed Data Processed:     3608.00   
    Total packets processed:              420       
===============================================================================
SMTP Preprocessor Statistics
  Total sessions                                    : 0
  Max concurrent sessions                           : 0
===============================================================================
dcerpc2 Preprocessor Statistics
  Total sessions: 0
===============================================================================
===============================================================================
SIP Preprocessor Statistics
  Total sessions: 0
===============================================================================
Snort exiting

ubuntu@ip-10-10-52-242:~/Desktop/Task-Exercises$ ls
10.10.52.242  142.250.187.110  172.67.27.10     Config-Sample   PACKET_NONIP
10.100.1.202  145.254.160.237  192.168.175.129  Exercise-Files  traffic-generator.sh
ubuntu@ip-10-10-52-242:~/Desktop/Task-Exercises$ sudo ./traffic-generator.sh
```
```text
# Option “-e” is deprecated and might be removed in a later version of gnome-terminal.
```
```text
# Use “-- ” to terminate the options and put the command line to execute after it.

first execute sniff then the traffic generator task 7

  GET methods:                          2
```
*2*
You can practice the rest of the parameters by using the traffic-generator script.
```text
practicing

root@ip-10-10-52-242:/home/ubuntu/Desktop/Task-Exercises# cd /etc/snort
root@ip-10-10-52-242:/etc/snort# ls
classification.config  gen-msg.map       rules       snort.debian.conf  threshold.conf
community-sid-msg.map  reference.config  snort.conf  snortv2.conf       unicode.map
root@ip-10-10-52-242:/etc/snort# cat snort.conf
#--------------------------------------------------
```
```text
#   VRT Rule Packages Snort.conf
#
```
```text
#   For more information visit us at:
```
```text
#     http://www.snort.org                   Snort Website
```
```text
#     http://vrt-blog.snort.org/    Sourcefire VRT Blog
#
```
```text
#     Mailing list Contact:      snort-sigs@lists.sourceforge.net
```
```text
#     False Positive reports:    fp@sourcefire.com
```
```text
#     Snort bugs:                bugs@snort.org
#
```
```text
#     Compatible with Snort Versions:
```
```text
#     VERSIONS : 2.9.7.0
#
```
```text
#     Snort build options:
```
```text
#     OPTIONS : --enable-gre --enable-mpls --enable-targetbased --enable-ppm --enable-perfprofiling --enable-zlib --enable-active-response --enable-normalizer --enable-reload --enable-react --enable-flexresp3
#
```
```text
#     Additional information:
```
```text
#     This configuration file enables active response, to run snort in
```
```text
#     test mode -T you are required to supply an interface -i <interface>
```
```text
#     or test mode will fail to fully validate the configuration and
```
```text
#     exit with a FATAL error
#--------------------------------------------------

###################################################
```
```text
# This file contains a sample snort configuration.
```
```text
# You should take the following steps to create your own custom configuration:
#
```
```text
#  1) Set the network variables.
```
```text
#  2) Configure the decoder
```
```text
#  3) Configure the base detection engine
```
```text
#  4) Configure dynamic loaded libraries
```
```text
#  5) Configure preprocessors
```
```text
#  6) Configure output plugins
```
```text
#  7) Customize your rule set
```
```text
#  8) Customize preprocessor and decoder rule set
```
```text
#  9) Customize shared object rule set
###################################################

###################################################
```
```text
# Step #1: Set the network variables.  For more information, see README.variables
###################################################
```
```text
# Setup the network addresses you are protecting
#
```
```text
# Note to Debian users: this value is overriden when starting
```
```text
# up the Snort daemon through the init.d script by the
```
```text
# value of DEBIAN_SNORT_HOME_NET s defined in the
```
```text
# /etc/snort/snort.debian.conf configuration file
#
ipvar HOME_NET any
```
```text
# Set up the external network addresses. Leave as "any" in most situations
ipvar EXTERNAL_NET any
```
```text
# If HOME_NET is defined as something other than "any", alternative, you can
```
```text
# use this definition if you do not want to detect attacks from your internal
```
```text
# IP addresses:
#ipvar EXTERNAL_NET !$HOME_NET
```
```text
# List of DNS servers on your network 
ipvar DNS_SERVERS $HOME_NET
```
```text
# List of SMTP servers on your network
ipvar SMTP_SERVERS $HOME_NET
```
```text
# List of web servers on your network
ipvar HTTP_SERVERS $HOME_NET
```
```text
# List of sql servers on your network 
ipvar SQL_SERVERS $HOME_NET
```
```text
# List of telnet servers on your network
ipvar TELNET_SERVERS $HOME_NET
```
```text
# List of ssh servers on your network
ipvar SSH_SERVERS $HOME_NET
```
```text
# List of ftp servers on your network
ipvar FTP_SERVERS $HOME_NET
```
```text
# List of sip servers on your network
ipvar SIP_SERVERS $HOME_NET
```
```text
# List of ports you run web servers on
portvar HTTP_PORTS [80,81,311,383,591,593,901,1220,1414,1741,1830,2301,2381,2809,3037,3128,3702,4343,4848,5250,6988,7000,7001,7144,7145,7510,7777,7779,8000,8008,8014,8028,8080,8085,8088,8090,8118,8123,8180,8181,8243,8280,8300,8800,8888,8899,9000,9060,9080,9090,9091,9443,9999,11371,34443,34444,41080,50002,55555]
```
```text
# List of ports you want to look for SHELLCODE on.
portvar SHELLCODE_PORTS !80
```
```text
# List of ports you might see oracle attacks on
portvar ORACLE_PORTS 1024:
```
```text
# List of ports you want to look for SSH connections on:
portvar SSH_PORTS 22
```
```text
# List of ports you run ftp servers on
portvar FTP_PORTS [21,2100,3535]
```
```text
# List of ports you run SIP servers on
portvar SIP_PORTS [5060,5061,5600]
```
```text
# List of file data ports for file inspection
portvar FILE_DATA_PORTS [$HTTP_PORTS,110,143]
```
```text
# List of GTP ports for GTP preprocessor
portvar GTP_PORTS [2123,2152,3386]
```
```text
# other variables, these should not be modified
ipvar AIM_SERVERS [64.12.24.0/23,64.12.28.0/23,64.12.161.0/24,64.12.163.0/24,64.12.200.0/24,205.188.3.0/24,205.188.5.0/24,205.188.7.0/24,205.188.9.0/24,205.188.153.0/24,205.188.179.0/24,205.188.248.0/24]
```
```text
# Path to your rules files (this can be a relative path)
```
```text
# Note for Windows users:  You are advised to make this an absolute path,
```
```text
# such as:  c:\snort\rules
var RULE_PATH /etc/snort/rules
var SO_RULE_PATH /etc/snort/so_rules
var PREPROC_RULE_PATH /etc/snort/preproc_rules
```
```text
# If you are using reputation preprocessor set these
```
```text
# Currently there is a bug with relative paths, they are relative to where snort is
```
```text
# not relative to snort.conf like the above variables
```
```text
# This is completely inconsistent with how other vars work, BUG 89986
```
```text
# Set the absolute path appropriately
var WHITE_LIST_PATH /etc/snort/rules
var BLACK_LIST_PATH /etc/snort/rules

###################################################
```
```text
# Step #2: Configure the decoder.  For more information, see README.decode
###################################################
```
```text
# Stop generic decode events:
config disable_decode_alerts
```
```text
# Stop Alerts on experimental TCP options
config disable_tcpopt_experimental_alerts
```
```text
# Stop Alerts on obsolete TCP options
config disable_tcpopt_obsolete_alerts
```
```text
# Stop Alerts on T/TCP alerts
config disable_tcpopt_ttcp_alerts
```
```text
# Stop Alerts on all other TCPOption type events:
config disable_tcpopt_alerts
```
```text
# Stop Alerts on invalid ip options
config disable_ipopt_alerts
```
```text
# Alert if value in length field (IP, TCP, UDP) is greater th elength of the packet
```
```text
# config enable_decode_oversized_alerts
```
```text
# Same as above, but drop packet if in Inline mode (requires enable_decode_oversized_alerts)
```
```text
# config enable_decode_oversized_drops
```
```text
# Configure IP / TCP checksum mode
config checksum_mode: all
```
```text
# Configure maximum number of flowbit references.  For more information, see README.flowbits
```
```text
# config flowbits_size: 64
```
```text
# Configure ports to ignore
```
```text
# config ignore_ports: tcp 21 6667:6671 1356
```
```text
# config ignore_ports: udp 1:17 53
```
```text
# Configure active response for non inline operation. For more information, see REAMDE.active
```
```text
# config response: eth0 attempts 2
```
```text
# Configure DAQ related options for inline operation. For more information, see README.daq
#
```
```text
# config daq: <type>
```
```text
# config daq_dir: <dir>
```
```text
# config daq_mode: <mode>
```
```text
# config daq_var: <var>
#
```
```text
# <type> ::= pcap | afpacket | dump | nfq | ipq | ipfw
```
```text
# <mode> ::= read-file | passive | inline
```
```text
# <var> ::= arbitrary <name>=<value passed to DAQ
```
```text
# <dir> ::= path as to where to look for DAQ module so's
```
```text
# Configure specific UID and GID to run snort as after dropping privs. For more information see snort -h command line options
#
```
```text
# config set_gid:
```
```text
# config set_uid:
```
```text
# Configure default snaplen. Snort defaults to MTU of in use interface. For more information see README
#
```
```text
# config snaplen:
#
```
```text
# Configure default bpf_file to use for filtering what traffic reaches snort. For more information see snort -h command line options (-F)
#
```
```text
# config bpf_file:
#
```
```text
# Configure default log directory for snort to log to.  For more information see snort -h command line options (-l)
#
```
```text
# config logdir:

###################################################
```
```text
# Step #3: Configure the base detection engine.  For more information, see  README.decode
###################################################
```
```text
# Configure PCRE match limitations
config pcre_match_limit: 3500
config pcre_match_limit_recursion: 1500
```
```text
# Configure the detection engine  See the Snort Manual, Configuring Snort - Includes - Config
config detection: search-method ac-split search-optimize max-pattern-len 20
```
```text
# Configure the event queue.  For more information, see README.event_queue
config event_queue: max_queue 8 log 5 order_events content_length

###################################################
## Configure GTP if it is to be used.
## For more information, see README.GTP
####################################################
```
```text
# config enable_gtp

###################################################
```
```text
# Per packet and rule latency enforcement
```
```text
# For more information see README.ppm
###################################################
```
```text
# Per Packet latency configuration
#config ppm: max-pkt-time 250, \
```
```text
#   fastpath-expensive-packets, \
```
```text
#   pkt-log
```
```text
# Per Rule latency configuration
#config ppm: max-rule-time 200, \
```
```text
#   threshold 3, \
```
```text
#   suspend-expensive-rules, \
```
```text
#   suspend-timeout 20, \
```
```text
#   rule-log alert

###################################################
```
```text
# Configure Perf Profiling for debugging
```
```text
# For more information see README.PerfProfiling
###################################################

#config profile_rules: print all, sort avg_ticks
#config profile_preprocs: print all, sort avg_ticks

###################################################
```
```text
# Configure protocol aware flushing
```
```text
# For more information see README.stream5
###################################################
config paf_max: 16000

###################################################
```
```text
# Step #4: Configure dynamic loaded libraries.
```
```text
# For more information, see Snort Manual, Configuring Snort - Dynamic Modules
###################################################
```
```text
# path to dynamic preprocessor libraries
dynamicpreprocessor directory /usr/lib/snort_dynamicpreprocessor/
```
```text
# path to base preprocessor engine
dynamicengine /usr/lib/snort_dynamicengine/libsf_engine.so
```
```text
# path to dynamic rules libraries
dynamicdetection directory /usr/lib/snort_dynamicrules

###################################################
```
```text
# Step #5: Configure preprocessors
```
```text
# For more information, see the Snort Manual, Configuring Snort - Preprocessors
###################################################
```
```text
# GTP Control Channle Preprocessor. For more information, see README.GTP
```
```text
# preprocessor gtp: ports { 2123 3386 2152 }
```
```text
# Inline packet normalization. For more information, see README.normalize
```
```text
# Does nothing in IDS mode
preprocessor normalize_ip4
preprocessor normalize_tcp: ips ecn stream
preprocessor normalize_icmp4
preprocessor normalize_ip6
preprocessor normalize_icmp6
```
```text
# Target-based IP defragmentation.  For more inforation, see README.frag3
preprocessor frag3_global: max_frags 65536
preprocessor frag3_engine: policy windows detect_anomalies overlap_limit 10 min_fragment_length 100 timeout 180
```
```text
# Target-Based stateful inspection/stream reassembly.  For more inforation, see README.stream5
preprocessor stream5_global: track_tcp yes, \
   track_udp yes, \
   track_icmp no, \ 
   max_tcp 262144, \
   max_udp 131072, \
   max_active_responses 2, \
   min_response_seconds 5
preprocessor stream5_tcp: policy windows, detect_anomalies, require_3whs 180, \
   overlap_limit 10, small_segments 3 bytes 150, timeout 180, \
    ports client 21 22 23 25 42 53 79 109 110 111 113 119 135 136 137 139 143 \
        161 445 513 514 587 593 691 1433 1521 1741 2100 3306 6070 6665 6666 6667 6668 6669 \
        7000 8181 32770 32771 32772 32773 32774 32775 32776 32777 32778 32779, \
    ports both 80 81 311 383 443 465 563 591 593 636 901 989 992 993 994 995 1220 1414 1830 2301 2381 2809 3037 3128 3702 4343 4848 5250 6988 7907 7000 7001 7144 7145 7510 7802 7777 7779 \
        7801 7900 7901 7902 7903 7904 7905 7906 7908 7909 7910 7911 7912 7913 7914 7915 7916 \
        7917 7918 7919 7920 8000 8008 8014 8028 8080 8085 8088 8090 8118 8123 8180 8243 8280 8300 8800 8888 8899 9000 9060 9080 9090 9091 9443 9999 11371 34443 34444 41080 50002 55555
preprocessor stream5_udp: timeout 180
```
```text
# performance statistics.  For more information, see the Snort Manual, Configuring Snort - Preprocessors - Performance Monitor
```
```text
# preprocessor perfmonitor: time 300 file /var/snort/snort.stats pktcnt 10000
```
```text
# HTTP normalization and anomaly detection.  For more information, see README.http_inspect
preprocessor http_inspect: global iis_unicode_map unicode.map 1252 compress_depth 65535 decompress_depth 65535 max_gzip_mem 104857600
preprocessor http_inspect_server: server default \
    http_methods { GET POST PUT SEARCH MKCOL COPY MOVE LOCK UNLOCK NOTIFY POLL BCOPY BDELETE BMOVE LINK UNLINK OPTIONS HEAD DELETE TRACE TRACK CONNECT SOURCE SUBSCRIBE UNSUBSCRIBE PROPFIND PROPPATCH BPROPFIND BPROPPATCH RPC_CONNECT PROXY_SUCCESS BITS_POST CCM_POST SMS_POST RPC_IN_DATA RPC_OUT_DATA RPC_ECHO_DATA } \
    chunk_length 500000 \
    server_flow_depth 0 \
    client_flow_depth 0 \
    post_depth 65495 \
    oversize_dir_length 500 \
    max_header_length 750 \
    max_headers 100 \
    max_spaces 200 \
    small_chunk_length { 10 5 } \
    ports { 80 81 311 383 591 593 901 1220 1414 1741 1830 2301 2381 2809 3037 3128 3702 4343 4848 5250 6988 7000 7001 7144 7145 7510 7777 7779 8000 8008 8014 8028 8080 8085 8088 8090 8118 8123 8180 8181 8243 8280 8300 8800 8888 8899 9000 9060 9080 9090 9091 9443 9999 11371 34443 34444 41080 50002 55555 } \
    non_rfc_char { 0x00 0x01 0x02 0x03 0x04 0x05 0x06 0x07 } \
    enable_cookie \
    extended_response_inspection \
    inspect_gzip \
    normalize_utf \
    unlimited_decompress \
    normalize_javascript \
    apache_whitespace no \
    ascii no \
    bare_byte no \
    directory no \
    double_decode no \
    iis_backslash no \
    iis_delimiter no \
    iis_unicode no \
    multi_slash no \
    utf_8 no \
    u_encode yes \
    webroot no
```
```text
# ONC-RPC normalization and anomaly detection.  For more information, see the Snort Manual, Configuring Snort - Preprocessors - RPC Decode
preprocessor rpc_decode: 111 32770 32771 32772 32773 32774 32775 32776 32777 32778 32779 no_alert_multiple_requests no_alert_large_fragments no_alert_incomplete
```
```text
# Back Orifice detection.
preprocessor bo
```
```text
# FTP / Telnet normalization and anomaly detection.  For more information, see README.ftptelnet
preprocessor ftp_telnet: global inspection_type stateful encrypted_traffic no check_encrypted
preprocessor ftp_telnet_protocol: telnet \
    ayt_attack_thresh 20 \
    normalize ports { 23 } \
    detect_anomalies
preprocessor ftp_telnet_protocol: ftp server default \
    def_max_param_len 100 \
    ports { 21 2100 3535 } \
    telnet_cmds yes \
    ignore_telnet_erase_cmds yes \
    ftp_cmds { ABOR ACCT ADAT ALLO APPE AUTH CCC CDUP } \
    ftp_cmds { CEL CLNT CMD CONF CWD DELE ENC EPRT } \
    ftp_cmds { EPSV ESTA ESTP FEAT HELP LANG LIST LPRT } \
    ftp_cmds { LPSV MACB MAIL MDTM MIC MKD MLSD MLST } \
    ftp_cmds { MODE NLST NOOP OPTS PASS PASV PBSZ PORT } \
    ftp_cmds { PROT PWD QUIT REIN REST RETR RMD RNFR } \
    ftp_cmds { RNTO SDUP SITE SIZE SMNT STAT STOR STOU } \
    ftp_cmds { STRU SYST TEST TYPE USER XCUP XCRC XCWD } \
    ftp_cmds { XMAS XMD5 XMKD XPWD XRCP XRMD XRSQ XSEM } \
    ftp_cmds { XSEN XSHA1 XSHA256 } \
    alt_max_param_len 0 { ABOR CCC CDUP ESTA FEAT LPSV NOOP PASV PWD QUIT REIN STOU SYST XCUP XPWD } \
    alt_max_param_len 200 { ALLO APPE CMD HELP NLST RETR RNFR STOR STOU XMKD } \
    alt_max_param_len 256 { CWD RNTO } \
    alt_max_param_len 400 { PORT } \
    alt_max_param_len 512 { SIZE } \
    chk_str_fmt { ACCT ADAT ALLO APPE AUTH CEL CLNT CMD } \
    chk_str_fmt { CONF CWD DELE ENC EPRT EPSV ESTP HELP } \
    chk_str_fmt { LANG LIST LPRT MACB MAIL MDTM MIC MKD } \
    chk_str_fmt { MLSD MLST MODE NLST OPTS PASS PBSZ PORT } \
    chk_str_fmt { PROT REST RETR RMD RNFR RNTO SDUP SITE } \
    chk_str_fmt { SIZE SMNT STAT STOR STRU TEST TYPE USER } \
    chk_str_fmt { XCRC XCWD XMAS XMD5 XMKD XRCP XRMD XRSQ } \ 
    chk_str_fmt { XSEM XSEN XSHA1 XSHA256 } \
    cmd_validity ALLO < int [ char R int ] > \    
    cmd_validity EPSV < [ { char 12 | char A char L char L } ] > \
    cmd_validity MACB < string > \
    cmd_validity MDTM < [ date nnnnnnnnnnnnnn[.n[n[n]]] ] string > \
    cmd_validity MODE < char ASBCZ > \
    cmd_validity PORT < host_port > \
    cmd_validity PROT < char CSEP > \
    cmd_validity STRU < char FRPO [ string ] > \    
    cmd_validity TYPE < { char AE [ char NTC ] | char I | char L [ number ] } >
preprocessor ftp_telnet_protocol: ftp client default \
    max_resp_len 256 \
    bounce yes \
    ignore_telnet_erase_cmds yes \
    telnet_cmds yes
```
```text
# SMTP normalization and anomaly detection.  For more information, see README.SMTP
preprocessor smtp: ports { 25 465 587 691 } \
    inspection_type stateful \
    b64_decode_depth 0 \
    qp_decode_depth 0 \
    bitenc_decode_depth 0 \
    uu_decode_depth 0 \
    log_mailfrom \
    log_rcptto \
    log_filename \
    log_email_hdrs \
    normalize cmds \
    normalize_cmds { ATRN AUTH BDAT CHUNKING DATA DEBUG EHLO EMAL ESAM ESND ESOM ETRN EVFY } \
    normalize_cmds { EXPN HELO HELP IDENT MAIL NOOP ONEX QUEU QUIT RCPT RSET SAML SEND SOML } \
    normalize_cmds { STARTTLS TICK TIME TURN TURNME VERB VRFY X-ADAT X-DRCP X-ERCP X-EXCH50 } \
    normalize_cmds { X-EXPS X-LINK2STATE XADR XAUTH XCIR XEXCH50 XGEN XLICENSE XQUE XSTA XTRN XUSR } \
    max_command_line_len 512 \
    max_header_line_len 1000 \
    max_response_line_len 512 \
    alt_max_command_line_len 260 { MAIL } \
    alt_max_command_line_len 300 { RCPT } \
    alt_max_command_line_len 500 { HELP HELO ETRN EHLO } \
    alt_max_command_line_len 255 { EXPN VRFY ATRN SIZE BDAT DEBUG EMAL ESAM ESND ESOM EVFY IDENT NOOP RSET } \
    alt_max_command_line_len 246 { SEND SAML SOML AUTH TURN ETRN DATA RSET QUIT ONEX QUEU STARTTLS TICK TIME TURNME VERB X-EXPS X-LINK2STATE XADR XAUTH XCIR XEXCH50 XGEN XLICENSE XQUE XSTA XTRN XUSR } \
    valid_cmds { ATRN AUTH BDAT CHUNKING DATA DEBUG EHLO EMAL ESAM ESND ESOM ETRN EVFY } \ 
    valid_cmds { EXPN HELO HELP IDENT MAIL NOOP ONEX QUEU QUIT RCPT RSET SAML SEND SOML } \
    valid_cmds { STARTTLS TICK TIME TURN TURNME VERB VRFY X-ADAT X-DRCP X-ERCP X-EXCH50 } \
    valid_cmds { X-EXPS X-LINK2STATE XADR XAUTH XCIR XEXCH50 XGEN XLICENSE XQUE XSTA XTRN XUSR } \
    xlink2state { enabled }
```
```text
# Portscan detection.  For more information, see README.sfportscan
```
```text
# preprocessor sfportscan: proto  { all } memcap { 10000000 } sense_level { low }
```
```text
# ARP spoof detection.  For more information, see the Snort Manual - Configuring Snort - Preprocessors - ARP Spoof Preprocessor
```
```text
# preprocessor arpspoof
```
```text
# preprocessor arpspoof_detect_host: 192.168.40.1 f0:0f:00:f0:0f:00
```
```text
# SSH anomaly detection.  For more information, see README.ssh
preprocessor ssh: server_ports { 22 } \
                  autodetect \
                  max_client_bytes 19600 \
                  max_encrypted_packets 20 \
                  max_server_version_len 100 \
                  enable_respoverflow enable_ssh1crc32 \
                  enable_srvoverflow enable_protomismatch
```
```text
# SMB / DCE-RPC normalization and anomaly detection.  For more information, see README.dcerpc2
preprocessor dcerpc2: memcap 102400, events [co ]
preprocessor dcerpc2_server: default, policy WinXP, \
    detect [smb [139,445], tcp 135, udp 135, rpc-over-http-server 593], \
    autodetect [tcp 1025:, udp 1025:, rpc-over-http-server 1025:], \
    smb_max_chain 3, smb_invalid_shares ["C$", "D$", "ADMIN$"]
```
```text
# DNS anomaly detection.  For more information, see README.dns
preprocessor dns: ports { 53 } enable_rdata_overflow
```
```text
# SSL anomaly detection and traffic bypass.  For more information, see README.ssl
preprocessor ssl: ports { 443 465 563 636 989 992 993 994 995 7801 7802 7900 7901 7902 7903 7904 7905 7906 7907 7908 7909 7910 7911 7912 7913 7914 7915 7916 7917 7918 7919 7920 }, trustservers, noinspect_encrypted
```
```text
# SDF sensitive data preprocessor.  For more information see README.sensitive_data
preprocessor sensitive_data: alert_threshold 25
```
```text
# SIP Session Initiation Protocol preprocessor.  For more information see README.sip
preprocessor sip: max_sessions 40000, \
   ports { 5060 5061 5600 }, \
   methods { invite \
             cancel \
             ack \
             bye \
             register \
             options \
             refer \
             subscribe \
             update \
             join \
             info \
             message \
             notify \
             benotify \
             do \
             qauth \
             sprack \
             publish \
             service \
             unsubscribe \
             prack }, \
   max_uri_len 512, \
   max_call_id_len 80, \
   max_requestName_len 20, \
   max_from_len 256, \
   max_to_len 256, \
   max_via_len 1024, \
   max_contact_len 512, \
   max_content_len 2048
```
```text
# IMAP preprocessor.  For more information see README.imap
preprocessor imap: \
   ports { 143 } \
   b64_decode_depth 0 \
   qp_decode_depth 0 \
   bitenc_decode_depth 0 \
   uu_decode_depth 0
```
```text
# POP preprocessor. For more information see README.pop
preprocessor pop: \
   ports { 110 } \
   b64_decode_depth 0 \
   qp_decode_depth 0 \
   bitenc_decode_depth 0 \
   uu_decode_depth 0
```
```text
# Modbus preprocessor. For more information see README.modbus
preprocessor modbus: ports { 502 }
```
```text
# DNP3 preprocessor. For more information see README.dnp3
preprocessor dnp3: ports { 20000 } \
   memcap 262144 \
   check_crc

#
```
```text
# Note to Debian users: this is disabled since it is an experimental
```
```text
# preprocessor. If you want to use it you have to create the rules files
```
```text
# referenced below in the /etc/snort/rules directory
#
```
```text
# Reputation preprocessor. For more information see README.reputation
#preprocessor reputation: \
```
```text
#   memcap 500, \
```
```text
#   priority whitelist, \
```
```text
#   nested_ip inner, \
```
```text
#   whitelist $WHITE_LIST_PATH/white_list.rules, \
```
```text
#   blacklist $BLACK_LIST_PATH/black_list.rules

###################################################
```
```text
# Step #6: Configure output plugins
```
```text
# For more information, see Snort Manual, Configuring Snort - Output Modules
###################################################
```
```text
# unified2
```
```text
# Recommended for most installs
```
```text
# output unified2: filename merged.log, limit 128, nostamp, mpls_event_types, vlan_event_types
output unified2: filename snort.log, limit 128, nostamp, mpls_event_types, vlan_event_types
```
```text
# Additional configuration for specific types of installs
```
```text
# output alert_unified2: filename snort.alert, limit 128, nostamp
```
```text
# output log_unified2: filename snort.log, limit 128, nostamp
```
```text
# syslog
```
```text
# output alert_syslog: LOG_AUTH LOG_ALERT
```
```text
# pcap
```
```text
# output log_tcpdump: tcpdump.log
```
```text
# metadata reference data.  do not modify these lines
include classification.config
include reference.config

###################################################
```
```text
# Step #7: Customize your rule set
```
```text
# For more information, see Snort Manual, Writing Snort Rules
#
```
```text
# NOTE: All categories are enabled in this conf file
###################################################
```
```text
# Note to Debian users: The rules preinstalled in the system
```
```text
# can be *very* out of date. For more information please read
```
```text
# the /usr/share/doc/snort-rules-default/README.Debian file

#
```
```text
# If you install the official VRT Sourcefire rules please review this
```
```text
# configuration file and re-enable (remove the comment in the first line) those
```
```text
# rules files that are available in your system (in the /etc/snort/rules
```
```text
# directory)
```
```text
# site specific rules
include $RULE_PATH/local.rules
```
```text
# The include files commented below have been disabled
```
```text
# because they are not available in the stock Debian
```
```text
# rules. If you install the Sourcefire VRT please make
```
```text
# sure you re-enable them again:

#include $RULE_PATH/app-detect.rules
include $RULE_PATH/attack-responses.rules
include $RULE_PATH/backdoor.rules
include $RULE_PATH/bad-traffic.rules
#include $RULE_PATH/blacklist.rules
#include $RULE_PATH/botnet-cnc.rules
#include $RULE_PATH/browser-chrome.rules
#include $RULE_PATH/browser-firefox.rules
#include $RULE_PATH/browser-ie.rules
#include $RULE_PATH/browser-other.rules
#include $RULE_PATH/browser-plugins.rules
#include $RULE_PATH/browser-webkit.rules
include $RULE_PATH/chat.rules
#include $RULE_PATH/content-replace.rules
include $RULE_PATH/ddos.rules
include $RULE_PATH/dns.rules
include $RULE_PATH/dos.rules
include $RULE_PATH/experimental.rules
#include $RULE_PATH/exploit-kit.rules
include $RULE_PATH/exploit.rules
#include $RULE_PATH/file-executable.rules
#include $RULE_PATH/file-flash.rules
#include $RULE_PATH/file-identify.rules
#include $RULE_PATH/file-image.rules
#include $RULE_PATH/file-multimedia.rules
#include $RULE_PATH/file-office.rules
#include $RULE_PATH/file-other.rules
#include $RULE_PATH/file-pdf.rules
include $RULE_PATH/finger.rules
include $RULE_PATH/ftp.rules
include $RULE_PATH/icmp-info.rules
include $RULE_PATH/icmp.rules
include $RULE_PATH/imap.rules
#include $RULE_PATH/indicator-compromise.rules
#include $RULE_PATH/indicator-obfuscation.rules
#include $RULE_PATH/indicator-shellcode.rules
include $RULE_PATH/info.rules
#include $RULE_PATH/malware-backdoor.rules
#include $RULE_PATH/malware-cnc.rules
#include $RULE_PATH/malware-other.rules
#include $RULE_PATH/malware-tools.rules
include $RULE_PATH/misc.rules
include $RULE_PATH/multimedia.rules
include $RULE_PATH/mysql.rules
include $RULE_PATH/netbios.rules
