---
Introduction to hands-on network monitoring and threat detection with Zeek (formerly Bro).
---

# Zeek — Writeup

## Overview
### Zeek — Writeup
### Zeek — Writeup
### Introduction
Zeek (formerly Bro) is an open-source and commercial network monitoring tool (traffic analyser).
https://docs.zeek.org/en/master/about.html
The official description; "Zeek (formerly Bro) is the world's leading platform for network security monitoring. Flexible, open-source, and powered by defenders." "Zeek is a passive, open-source network traffic analyser. Many operators use Zeek as a network security monitor (NSM) to support suspicious or malicious activity investigations. Zeek also supports a wide range of traffic analysis tasks beyond the security domain, including performance measurement and troubleshooting."
The room aims to provide a general network monitoring overview and work with Zeek to investigate captured traffic. This room will expect you to have basic Linux familiarity and Network fundamentals (ports, protocols and traffic data). We suggest completing the "Network Fundamentals" path before starting working in this room.
A VM is attached to this room. You don't need SSH or RDP; the room provides a "Split View" feature. Exercise files are located in the folder on the desktop. Log cleaner script "clear-logs.sh" is available in each exercise folder.
### Network Security Monitoring and Zeek
Introduction to Network Monitoring Approaches
Network monitoring is a set of management actions to watch/continuously overview and optionally save the network traffic for further investigation. This action aims to detect and reduce network problems, improve performance, and in some cases, increase overall productivity. It is a main part of the daily IT/SOC operations and differs from Network Security Monitoring (NSM) in its purpose.
Network Monitoring
Network monitoring is highly focused on IT assets like uptime (availability), device health and connection quality (performance), and network traffic balance and management (configuration). Monitoring and visualising the network traffic, troubleshooting, and root cause analysis are also part of the Network Monitoring process. This model is helpful for network administrators and usually doesn't cover identifying non-asset in-depth vulnerabilities and significant security concerns like internal threats and zero-day vulnerabilities. Usually, Network Monitoring is not within the SOC scope. It is linked to the enterprise IT/Network management team.
Network Security Monitoring
Network Security Monitoring is focused on network anomalies like rogue hosts, encrypted traffic, suspicious service and port usage, and malicious/suspicious traffic patterns in an intrusion/anomaly detection and response approach. Monitoring and visualising the network traffic and investigating suspicious events is a core part of Network Security Monitoring. This model is helpful for security analysts/incident responders, security engineers and threat hunters and covers identifying threats, vulnerabilities and security issues with a set of rules, signatures and patterns. Network Security Monitoring is part of the SOC, and the actions are separated between tier 1-2-3 analyst levels.
What is ZEEK?
Zeek (formerly Bro) is an open-source and commercial passive Network Monitoring tool (traffic analysis framework) developed by Lawrence Berkeley Labs. Today, Zeek is supported by several developers, and Corelight provides an Enterprise-ready fork of Zeek. Therefore this tool is called both open source and commercial. The differences between the open-source version and the commercial version are detailed here. https://corelight.com/products/compare-to-open-source-zeek?hsLang=en
Zeek differs from known monitoring and IDS/IPS tools by providing a wide range of detailed logs ready to investigate both for forensics and data analysis actions. Currently, Zeek provides 50+ logs in 7 categories.
Zeek vs Snort
While both are called IDS/NIDS, it is good to know the cons and pros of each tool and use them in a specific manner. While there are some overlapping functionalities, they have different purposes for usage.
Tool	Zeek	Snort
Capabilities	NSM and IDS framework. It is heavily focused on network analysis. It is more focused on specific threats to trigger alerts. The detection mechanism is focused on events.	An IDS/IPS system. It is heavily focused on signatures to detect vulnerabilities. The detection mechanism is focused on signature patterns and packets.
Cons
Hard to use.
The analysis is done out of the Zeek, manually or by automation.
Hard to detect complex threats.
Pros
It provides in-depth traffic visibility.
Useful for threat hunting.
Ability to detect complex threats.
It has a scripting language and supports event correlation.
Easy to read logs.
Easy to write rules.
Cisco supported rules.
Community support.
Common Use Case	Network monitoring.
In-depth traffic investigation.
Intrusion detecting in chained events. 	Intrusion detection and prevention.
Stop known attacks/threats.
Zeek Architecture
Zeek has two primary layers; "Event Engine" and "Policy Script Interpreter". The Event Engine layer is where the packets are processed; it is called the event core and is responsible for describing the event without focusing on event details. It is where the packages are divided into parts such as source and destination addresses, protocol identification, session analysis and file extraction. The Policy Script Interpreter layer is where the semantic analysis is conducted. It is responsible for describing the event correlations by using Zeek scripts.
Zeek Frameworks
Zeek has several frameworks to provide extended functionality in the scripting layer. These frameworks enhance Zeek's flexibility and compatibility with other network components. Each framework focuses on the specific use case and easily runs with Zeek installation. For instance, we will be using the "Logging Framework" for all cases. Having ide on each framework's functionality can help users quickly identify an event of interest.
Available Frameworks
Logging	Notice	Input	Configuration	Intelligence
Cluster	Broker Communication	Supervisor	GeoLocation	File Analysis
Signature	Summary	NetControl	Packet Analysis	TLS Decryption
You can read more on frameworks here.  https://docs.zeek.org/en/master/frameworks/index.html
Zeek Outputs
As mentioned before, Zeek provides 50+ log files under seven different categories, which are helpful in various areas such as traffic monitoring, intrusion detection, threat hunting and web analytics. This section is not intended to discuss the logs in-depth. The logs are covered in TASK 3.
Once you run Zeek, it will automatically start investigating the traffic or the given pcap file and generate logs automatically. Once you process a pcap with Zeek, it will create the logs in the working directory. If you run the Zeek as a service, your logs will be located in the default log path. The default log path is: /opt/zeek/logs/
Working with Zeek
There are two operation options for Zeek. The first one is running it as a service, and the second option is running the Zeek against a pcap. Before starting working with Zeek, let's check the version of the Zeek instance with the following command: zeek -v
Now we are sure that we have Zeek installed. Let's start the Zeek as a service! To do this, we need to use the "ZeekControl" module, as shown below. The "ZeekControl" module requires superuser permissions to use. You can elevate the session privileges and switch to the superuser account to examine the generated log files with the following command: sudo su
Here we can manage the Zeek service and view the status of the service. Primary management of the Zeek service is done with three commands; "status", "start", and "stop".
```text
ZeekControl Module

           
root@ubuntu$ zeekctl
Welcome to ZeekControl 2.X.0
[ZeekControl] > status
Name         Type       Host          Status    Pid    Started
zeek         standalone localhost     stopped
[ZeekControl] > start
starting zeek ...
[ZeekControl] > status
Name         Type       Host          Status    Pid    Started
zeek         standalone localhost     running   2541   13 Mar 18:25:08
[ZeekControl] > stop
stopping zeek ...
[ZeekControl] > status
Name         Type       Host          Status    Pid    Started
zeek         standalone localhost     stopped
```
You can also use the "ZeekControl" mode with the following commands as well;
zeekctl status
zeekctl start
zeekctl stop
The only way to listen to the live network traffic is using Zeek as a service. Apart from using the Zeek as a network monitoring tool, we can also use it as a packet investigator. To do so, we need to process the pcap files with Zeek, as shown below. Once you process a pcap file, Zeek automatically creates log files according to the traffic.
In pcap processing mode, logs are saved in the working directory. You can view the generated logs using the ls -l command.
```text
ZeekControl Module

           
root@ubuntu$ zeek -C -r sample.pcap 

root@ubuntu$ ls -l
-rw-r--r-- 1 ubuntu ubuntu  11366 Mar 13 20:45 conn.log
-rw-r--r-- 1 ubuntu ubuntu    763 Mar 13 20:45 dhcp.log
-rw-r--r-- 1 ubuntu ubuntu   2918 Mar 13 20:45 dns.log
-rw-r--r-- 1 ubuntu ubuntu    254 Mar 13 20:45 packet_filter.log
```
Main Zeek command line parameters are explained below;
Parameter	Description
-r	 Reading option, read/process a pcap file.
-C	 Ignoring checksum errors.
-v	 Version information.
zeekctl	ZeekControl module.
Investigating the generated logs will require command-line tools (cat, cut, grep sort, and uniq) and additional tools (zeek-cut). We will cover them in the following tasks.
Each exercise has a folder. Ensure you are in the right directory to find the pcap file and accompanying files. Desktop/Exercise-Files/TASK-2
```text
┌──(kali㉿kali)-[~]
└─$ mkpasswd -m sha-512 Password1234
$6$7aBBZsevrBf.kiTO$0T07Csq8zn0jvUNe5eT4LmHR2jwMR1ObSraOtop4ZQ3O/bf1bCLLR0EQLmqd8rSnoncfXM4CTOybHNRrGI7ZB/

ubuntu@ip-10-10-201-211:~$ sudo su
root@ip-10-10-201-211:/home/ubuntu# nano /etc/shadow
root@ip-10-10-201-211:/home/ubuntu# cat /etc/shadow

ubuntu:$6$7aBBZsevrBf.kiTO$0T07Csq8zn0jvUNe5eT4LmHR2jwMR1ObSraOtop4ZQ3O/bf1bCLLR0EQLmqd8rSnoncfXM4CTOybHNRrGI7ZB/:19050:0:99999:7:::

cannot 

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files# cd TASK-2
root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-2# ls
clear-logs.sh  sample.pcap
root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-2# zeekctl
Warning: new zeek version detected (run the zeekctl "deploy" command)

Welcome to ZeekControl 2.4.0

Type "help" for help.

[ZeekControl] > help

ZeekControl Version 2.4.0

  capstats [<nodes>] [<secs>]      - Report interface statistics with capstats
  check [<nodes>]                  - Check configuration before installing it
  cleanup [--all] [<nodes>]        - Delete working dirs (flush state) on nodes
  config                           - Print zeekctl configuration
  cron [--no-watch]                - Perform jobs intended to run from cron
  cron enable|disable|?            - Enable/disable "cron" jobs
  deploy                           - Check, install, and restart
  df [<nodes>]                     - Print nodes' current disk usage
  diag [<nodes>]                   - Output diagnostics for nodes
  exec <shell cmd>                 - Execute shell command on all hosts
  exit                             - Exit shell
  install                          - Update zeekctl installation/configuration
  netstats [<nodes>]               - Print nodes' current packet counters
  nodes                            - Print node configuration
  peerstatus [<nodes>]             - Print status of nodes' remote connections
  print <id> [<nodes>]             - Print values of script variable at nodes
  process <trace> [<op>] [-- <sc>] - Run Zeek with options and scripts on trace
  quit                             - Exit shell
  restart [--clean] [<nodes>]      - Stop and then restart processing
  scripts [-c] [<nodes>]           - List the Zeek scripts the nodes will load
  start [<nodes>]                  - Start processing
  status [<nodes>]                 - Summarize node status
  stop [<nodes>]                   - Stop processing
  top [<nodes>]                    - Show Zeek processes ala top
  
Commands provided by plugins:

  ps.zeek [<nodes>]                - Show Zeek processes on nodes' systems

[ZeekControl] > status
Name         Type       Host          Status    Pid    Started
zeek         standalone localhost     stopped
[ZeekControl] > start
starting zeek ...
[ZeekControl] > status
Name         Type       Host          Status    Pid    Started
zeek         standalone localhost     running   8280   08 Dec 18:28:51

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-2# zeek -v
zeek version 4.2.1

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-2# zeekctl status
Warning: new zeek version detected (run the zeekctl "deploy" command)
Name         Type       Host          Status    Pid    Started
zeek         standalone localhost     running   8280   08 Dec 18:28:51

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-2# cat clear-logs.sh 
#!/bin/bash
rm -rf *.log
rm -rf extract_files

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-2# zeek -C -r sample.pcap 
root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-2# ls -l
total 444
-rwxr-xr-x 1 ubuntu ubuntu     46 Apr  3  2022 clear-logs.sh
-rw-r--r-- 1 root   root    11375 Dec  8 18:33 conn.log
-rw-r--r-- 1 root   root      761 Dec  8 18:33 dhcp.log
-rw-r--r-- 1 root   root     2911 Dec  8 18:33 dns.log
-rw-r--r-- 1 root   root     2528 Dec  8 18:33 ntp.log
-rw-r--r-- 1 root   root      254 Dec  8 18:33 packet_filter.log
-rw-r--r-- 1 ubuntu ubuntu 407510 Mar  3  2017 sample.pcap
-rw-r--r-- 1 root   root      530 Dec  8 18:33 snmp.log
-rw-r--r-- 1 root   root      703 Dec  8 18:33 ssh.log
-rw-r--r-- 1 root   root     1561 Dec  8 18:33 syslog.log

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-2# cat conn.log
#separator \x09
#set_separator	,
#empty_field	(empty)
#unset_field	-
#path	conn
#open	2022-12-08-18-33-25
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	proto	service	duration	orig_bytes	resp_bytes	conn_state	local_orig	local_resp	missed_bytes	history	orig_pkts	orig_ip_bytes	resp_pkts	resp_ip_bytes	tunnel_parents
#types	time	string	addr	port	addr	port	enum	string	intervalcount	count	string	bool	bool	count	string	count	count	count	count	set[string]
1488571051.943250	CWjxT74xjObkfaakHi	192.168.121.2	51153	192.168.120.22	53	udp	dns	0.001263	36	106	SF	-	-0	Dd	1	64	1	134	-

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-2# cat dhcp.log
#separator \x09
#set_separator	,
#empty_field	(empty)
#unset_field	-
#path	dhcp
#open	2022-12-08-18-33-25
#fields	ts	uids	client_addr	server_addr	mac	host_name	client_fqdn	domain	requested_addr	assigned_addr	lease_time	client_message	server_message	msg_types	duration
#types	time	set[string]	addr	addr	string	string	string	string	addr	addr	interval	string	string	vector[string]	interval
1488571152.666896	CB9fDUQgJ00UMF0Nc,CFrsWd4jVETjvRPkm9	-	-	00:21:70:e9:bb:47	Microknoppix	-	-	192.168.20.11	-	--	-	REQUEST,NAK	0.009251
1488571152.699148	CWkNtQRxRlsllb1w4,CFrsWd4jVETjvRPkm9	192.168.30.11	192.168.30.1	00:21:70:e9:bb:47	Microknoppix	-	webernetz.net	192.168.30.11	192.168.30.11	86400.000000	-	-	DISCOVER,OFFER,REQUEST,ACK	0.022753
#close	2022-12-08-18-33-25

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-2# cat dns.log
#separator \x09
#set_separator	,
#empty_field	(empty)
#unset_field	-
#path	dns
#open	2022-12-08-18-33-25
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	proto	trans_id	rtt	query	qclass	qclass_name	qtype	qtype_name	rcode	rcode_name	AA	TC	RD	RA	Z	answers	TTLs	rejected
#types	time	string	addr	port	addr	port	enum	count	intervalstring	count	string	count	string	count	string	bool	bool	bool	bool	count	vector[string]	vector[interval]	bool
1488571051.943250	CWjxT74xjObkfaakHi	192.168.121.2	51153	192.168.120.22	53	udp	46282	0.001263	blog.webernetz.net	1	C_INTERNET	1	A	0	NOERROR	F	F	T	T	05.35.226.136	18180.000000	F
1488571111.943319	CqIqMWROm4Qn71gh	192.168.121.2	55916	192.168.120.22	53	udp	12856	-	blog.webernetz.net	1	C_INTERNET	1	A	-	-	F	F	T	F	0	--	F
1488571114.941785	CqIqMWROm4Qn71gh	192.168.121.2	55916	192.168.120.22	53	udp	12856	-	blog.webernetz.net	1	C_INTERNET	1	A	-	-	F	F	T	F	0	--	F
1488571117.941752	CqIqMWROm4Qn71gh	192.168.121.2	55916	192.168.120.22	53	udp	12856	-	blog.webernetz.net	1	C_INTERNET	1	A	-	-	F	F	T	F	0	--	F
1488571120.941715	CqIqMWROm4Qn71gh	192.168.121.2	55916	192.168.120.22	53	udp	12856	-	blog.webernetz.net	1	C_INTERNET	1	A	-	-	F	F	T	F	0	--	F
1488571171.944137	C5KAYIrIy6wl6Msg8	192.168.121.2	64768	192.168.120.22	53	udp	49578	-	blog.webernetz.net	1	C_INTERNET	1	A	-	-	F	F	T	F	0	--	F
1488571174.942481	C5KAYIrIy6wl6Msg8	192.168.121.2	64768	192.168.120.22	53	udp	49578	-	blog.webernetz.net	1	C_INTERNET	1	A	-	-	F	F	T	F	0	--	F
1488571177.942580	C5KAYIrIy6wl6Msg8	192.168.121.2	64768	192.168.120.22	53	udp	49578	-	blog.webernetz.net	1	C_INTERNET	1	A	-	-	F	F	T	F	0	--	F
1488571180.942543	C5KAYIrIy6wl6Msg8	192.168.121.2	64768	192.168.120.22	53	udp	49578	-	blog.webernetz.net	1	C_INTERNET	1	A	-	-	F	F	T	F	0	--	F
1488571231.945206	Cd0MrZ3ngXi2MPcdj5	192.168.121.2	58304	192.168.120.22	53	udp	25350	-	blog.webernetz.net	1	C_INTERNET	1	A	-	-	F	F	T	F	0	--	F
1488571234.943173	Cd0MrZ3ngXi2MPcdj5	192.168.121.2	58304	192.168.120.22	53	udp	25350	-	blog.webernetz.net	1	C_INTERNET	1	A	-	-	F	F	T	F	0	--	F
1488571237.943159	Cd0MrZ3ngXi2MPcdj5	192.168.121.2	58304	192.168.120.22	53	udp	25350	-	blog.webernetz.net	1	C_INTERNET	1	A	-	-	F	F	T	F	0	--	F
1488571240.944104	Cd0MrZ3ngXi2MPcdj5	192.168.121.2	58304	192.168.120.22	53	udp	25350	-	blog.webernetz.net	1	C_INTERNET	1	A	-	-	F	F	T	F	0	--	F
1488571291.946026	CRjbAG4teJkWpcRnWh	192.168.121.2	56469	192.168.120.22	53	udp	10917	0.001252	blog.webernetz.net	1	C_INTERNET	1	A	0	NOERROR	F	F	T	T	05.35.226.136	17940.000000	F
1488571351.947847	C1hBsX3s5LvIMUVpK2	192.168.121.2	62383	192.168.120.22	53	udp	58775	0.001001	blog.webernetz.net	1	C_INTERNET	1	A	0	NOERROR	F	F	T	T	05.35.226.136	17880.000000	F
1488571353.387074	Cy3hN025qGcHM8oVm7	2003:51:6012:121::2	64387	2003:51:6012:120::a08:53	53	udp	28238	0.001122	ip.webernetz.net1	C_INTERNET	28	AAAA	0	NOERROR	F	F	T	T0	2003:51:6012:110::19	62409.000000	F
#close	2022-12-08-18-33-25

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-2# cat ntp.log
#separator \x09
#set_separator	,
#empty_field	(empty)
#unset_field	-
#path	ntp
#open	2022-12-08-18-33-25
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	version	mode	stratum	poll	precision	root_delay	root_disp	ref_id	ref_time	org_time	rec_time	xmt_time	num_exts
#types	time	string	addr	port	addr	port	count	count	count	interval	interval	interval	interval	string	time	time	time	time	count
1488571044.700378	CAgBkIsEviJh4JnT8	192.168.121.40	123	212.224.120.164	123	3	3	3	1024.000000	0.000004	0.0070800.005463	212.224.120.164	1488570020.701048	1488570020.696918	1488570020.701048	1488571044.702008	0
1488571044.702385	CAgBkIsEviJh4JnT8	192.168.121.40	123	212.224.120.164	123	3	4	2	1024.000000	0.000001	0.0043030.001572	131.188.3.220	1488570556.751928	1488571044.702008	1488571044.700752	1488571044.700816	0
1488571046.696935	C7pdOj203ijQ3pbx4a	192.168.121.40	123	78.46.107.140	123	3	3	3	1024.000000	0.000004	0.0081330.005890	212.224.120.164	1488571044.705910	1488570022.691850	1488570022.699347	1488571046.698614	0
1488571046.703936	C7pdOj203ijQ3pbx4a	192.168.121.40	123	78.46.107.140	123	3	4	2	1024.000000	0.000002	0.0115660.036118	192.53.103.108	1488570102.937028	1488571046.698614	1488571046.699470	1488571046.699542	0
1488571067.702200	C5624Q1QQ95u2Uozog	192.168.121.40	123	148.251.154.36	123	3	3	3	512.000000	0.000004	0.0081330.005890	212.224.120.164	1488571044.705910	1488570043.695927	1488570043.703567	1488571067.703860	0
1488571067.708955	C5624Q1QQ95u2Uozog	192.168.121.40	123	148.251.154.36	123	3	4	3	512.000000	0.000000	0.0117490.065445	98.189.166.96	1488570036.057400	1488571067.703860	1488571067.703979	1488571067.703995	0
1488571317.261458	C98TWF4OLMycbz2It6	2003:51:6012:121::10	123	2003:51:6012:110::dcf7:123	123	4	3	2	1024.000000	0.000008	0.003052	0.057007	106.20.14.218	1488569268.242463	1488570294.243916	1488570294.246714	1488571317.259985	0
1488571317.262960	C98TWF4OLMycbz2It6	2003:51:6012:121::10	123	2003:51:6012:110::dcf7:123	123	4	4	1	1024.000000	0.000002	0.000000	0.004700	DCFa	1488571186.880789	1488571317.259985	1488571317.259725	1488571317.260059	0
1488571365.706238	CM88QM8EiCbiParvb	192.168.121.40	123	212.227.54.68	123	3	3	3	512.000000	0.000004	0.0081330.005890	212.224.120.164	1488571044.705910	1488570341.696499	1488570341.703687	1488571365.707974	0
1488571365.711985	CM88QM8EiCbiParvb	192.168.121.40	123	212.227.54.68	123	3	4	2	512.000000	0.000000	0.0069890.030792	131.188.3.223	1488570046.289139	1488571365.707974	1488571365.708844	1488571365.708869	0
#close	2022-12-08-18-33-25

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-2# cat packet_filter.log 
#separator \x09
#set_separator	,
#empty_field	(empty)
#unset_field	-
#path	packet_filter
#open	2022-12-08-18-33-25
#fields	ts	node	filter	init	success
#types	time	string	string	bool	bool
1670524405.059987	zeek	ip or not ip	T	T
#close	2022-12-08-18-33-25

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-2# cat snmp.log 
#separator \x09
#set_separator	,
#empty_field	(empty)
#unset_field	-
#path	snmp
#open	2022-12-08-18-33-25
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	duration	version	community	get_requests	get_bulk_requests	get_responses	set_requests	display_string	up_since
#types	time	string	addr	port	addr	port	interval	string	string	count	count	count	count	string	time
1488571221.774628	CYSlce1x6fXGF2Ca8d	2003:51:6012:120::13	58684	2003:51:6012:121::2	161	0.026505	2c	n5rAD1ig314IqfioYBWw	20	0	20	0	-	-
#close	2022-12-08-18-33-25

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-2# cat ssh.log
#separator \x09
#set_separator	,
#empty_field	(empty)
#unset_field	-
#path	ssh
#open	2022-12-08-18-33-25
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	version	auth_success	auth_attempts	direction	client	server	cipher_alg	mac_alg	compression_alg	kex_alg	host_key_alg	host_key
#types	time	string	addr	port	addr	port	count	bool	count	enum	string	string	string	string	string	string	string	string
1488571329.467978	CI8O6l2fkrwwTpBI1f	2003:51:6012:110::b15:22	60892	2003:51:6012:121::2	22	2	T	2	-	SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.1	SSH-2.0-Cisco-1.25	aes128-cbc	hmac-sha1	none	diffie-hellman-group-exchange-sha1	ssh-rsa	cf:5f:e7:e2:32:12:88:6e:33:c9:ad:5b:da:b6:b1:43
#close	2022-12-08-18-33-25

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-2# cat syslog.log 
#separator \x09
#set_separator	,
#empty_field	(empty)
#unset_field	-
#path	syslog
#open	2022-12-08-18-33-25
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	proto	facility	severity	message
#types	time	string	addr	port	addr	port	enum	string	string	string
1488571038.380901	CsPXxu10fSq30yRyj	192.168.121.10	50080	192.168.120.10	514	udp	LOCAL7	NOTICE	72: Mar  3 19:57:17.371: %LINK-5-CHANGED: Interface GigabitEthernet0/2, changed state to administratively down
1488571038.381406	CsPXxu10fSq30yRyj	192.168.121.10	50080	192.168.120.10	514	udp	LOCAL7	NOTICE	73: Mar  3 19:57:18.377: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/2, changed state to down
1488571187.162253	C8pRXW1zxob24icwEi	192.168.121.10	50080	192.168.120.10	514	udp	LOCAL7	ERR	74: Mar  3 19:59:46.152: %LINK-3-UPDOWN: Interface GigabitEthernet0/2, changed state to up
1488571189.276080	C8pRXW1zxob24icwEi	192.168.121.10	50080	192.168.120.10	514	udp	LOCAL7	NOTICE	75: Mar  3 19:59:48.266: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/2, changed state to up
1488571330.521769	C4pCCU2FVNOfPYPW5b	192.168.121.2	50352	192.168.120.10	514	udp	LOCAL7	INFO	63: Mar  3 20:02:09.464: %IPV6_ACL-6-ACCESSLOGP: list vty-access/10 permitted tcp 2003:51:6012:110::B15:22(60892) -> ::(22), 1 packet
1488571330.522327	C4pCCU2FVNOfPYPW5b	192.168.121.2	50352	192.168.120.10	514	udp	LOCAL7	INFO	64: Mar  3 20:02:09.468: %IPV6_ACL-6-ACCESSLOGP: list vty-access/10 permitted tcp 2003:51:6012:110::B15:22(60892) -> 2003:51:6012:121::2(22), 1 packet
#close	2022-12-08-18-33-25

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-2# cat sample.pcap

seems like packetracer commands

ip address 192.168.10.1 255.255.255.0
 ip verify unicast source reachable-via rx
 ipv6 address 2003:51:6012:122::1/64
 ipv6 rip CCNPv6 enable

interface FastEthernet0/1.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0
 ip verify unicast source reachable-via rx

interface FastEthernet0/1.30
 encapsulation dot1Q 30
 ip address 192.168.30.1 255.255.255.0
 ip verify unicast source reachable-via rx

interface FastEthernet0/1.121
 encapsulation dot1Q 121
 ip address 192.168.121.2 255.255.255.0
 ip verify unicast source reachable-via rx allow-default
 ipv6 address 2003:51:6012:121::2/64
 ipv6 rip CCNPv6 enable

interface Serial0/0/0
 no ip address
 shutdown
 no fair-queue
 clock rate 2000000

interface Serial0/0/1
 no ip address
 shutdown
 clock rate 2000000

router rip
 version 2
 network 192.168.10.0
 network 192.168.20.0
 network 192.168.30.0
 network 192.168.121.0

ip forward-protocol nd
no ip http server
ip http secure-server

ip sla 260720081
 icmp-echo 2A01:488:42:1000:50ED:8588:8A:C570
ip sla schedule 260720081 life forever start-time now
ip sla 260720082
 dns blog.webernetz.net name-server 192.168.120.22
ip sla schedule 260720082 life forever start-time now
ip sla 260720083
 icmp-jitter 192.168.120.1
ip sla schedule 260720083 life forever start-time now
ip sla 260720084
 udp-jitter 192.168.121.254 65535
ip sla schedule 260720084 life forever start-time now
ip sla 260720085
 udp-jitter 192.168.121.253 65534
ip sla schedule 260720085 life forever start-time now
logging 192.168.120.10
access-list 1 permit 192.168.0.0 0.0.255.255 log
access-list 1 deny   any log
ipv6 router rip CCNPv6
 timers 10 30 10 20

snmp-server community n5rAD1ig314IqfioYBWw RO
snmp-server ifindex persist
snmp-server contact Johannes Weber

radius server blubb
 address ipv6 2001:DB8::1812 auth-port 1812 acct-port 1813

ipv6 access-list vty-access
 permit ipv6 2003:51:6012::/48 any log
 deny ipv6 any any log

control-plane

mgcp profile default
line con 0
 exec-timeout 0 0
 privilege level 15
 logging synchronous
line aux 0
line vty 0 4
 access-class 1 in
 exec-timeout 0 0
 privilege level 15
 ipv6 access-class vty-access in
 transport input ssh
line vty 5 15
 access-class 1 in
 ipv6 access-class vty-access in
 transport input all

scheduler allocate 20000 1000
ntp update-calendar
ntp server ipv6 2.de.pool.ntp.org
ntp server ipv6 2.pool.ntp.org
ntp server ntp1.webernetz.net prefer
ntp server ntp2.webernetz.net prefer
end
CCNP-LAB-S1.webernetz.net
Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 15.0(2)SE9, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2015 by Cisco Systems, Inc.
Compiled Tue 01-Dec-15 07:07 by prod_rel_teaGigabitEthernet0/1
!3RFOC0630Z3KZ	Gi0/2
FOC1213Z3S4Gi0/1CCNP-LAB-S2.webernetz.net
!4QFOC1213Z3S4	Gi0/1 
FOC0630Z3KZGi0/2CCNP-LAB-S1.webernetz.net

yeah!!
https://chat.openai.com/chat

This appears to be a configuration file for a Cisco router. The configuration file contains various commands for configuring the router's interfaces, routing protocols, and other features. Some of the notable commands in this configuration file include:

-   `ip address`: This command is used to configure an IP address on an interface.
-   `interface`: This command is used to enter interface configuration mode, where you can configure settings for a specific interface on the router.
-   `router rip`: This command is used to enable the RIP routing protocol on the router and specify the networks that should be included in the RIP routing table.
-   `ip forward-protocol`: This command is used to enable forwarding of a specific protocol on the router.
-   `ip http server`: This command is used to enable the HTTP server on the router, allowing users to access the router's configuration using a web browser.
-   `snmp-server community`: This command is used to configure a Simple Network Management Protocol (SNMP) community on the router.
-   `radius server`: This command is used to configure a RADIUS server on the router.
-   `ipv6 access-list`: This command is used to create an IPv6 access list on the router, which can be used to filter traffic based on specified criteria.
-   `control-plane`: This command is used to enter control-plane configuration mode, where you can configure settings for the router's control plane.
-   `mgcp profile`: This command is used to configure a Media Gateway Control Protocol (MGCP) profile on the router.
-   `line con 0`: This command is used to enter line configuration mode for the console line on the router, allowing you to configure settings for the console connection.
-   `scheduler allocate`: This command is used to allocate memory for the router's scheduler.
-   `ntp update-calendar`: This command is used to update the calendar on the router using Network Time Protocol (NTP).
-   `ntp server`: This command is used to configure an NTP server on the router.
-   `end`: This command is used to exit configuration mode and return to privileged EXEC mode.

https://weberblog.net/about/

nice webpage to learn networking
```
What is the installed Zeek instance version number?
*4.2.1*
What is the version of the ZeekControl module?
*2.4.0*
Investigate the "sample.pcap" file. What is the number of generated alert files?
*8*
### Zeek Logs
Zeek Logs
Zeek generates log files according to the traffic data. You will have logs for every connection in the wire, including the application level protocols and fields. Zeek is capable of identifying 50+ logs and categorising them into seven categories. Zeek logs are well structured and tab-separated ASCII files, so reading and processing them is easy but requires effort. You should be familiar with networking and protocols to correlate the logs in an investigation, know where to focus, and find a specific piece of evidence.
Each log output consists of multiple fields, and each field holds a different part of the traffic data. Correlation is done through a unique value called "UID". The "UID" represents the unique identifier assigned to each session.
Zeek logs in a nutshell;
Category
Description
Log Files
Network
Network protocol logs.
conn.log, dce_rpc.log, dhcp.log, dnp3.log, dns.log, ftp.log, http.log, irc.log, kerberos.log, modbus.log, modbus_register_change.log, mysql.log, ntlm.log, ntp.log, radius.log, rdp.log, rfb.log, sip.log, smb_cmd.log, smb_files.log, smb_mapping.log, smtp.log, snmp.log, socks.log, ssh.log, ssl.log, syslog.log, tunnel.log.
Files
File analysis result logs.
files.log, ocsp.log, pe.log, x509.log.
NetControl
Network control and flow logs.
netcontrol.log, netcontrol_drop.log, netcontrol_shunt.log, netcontrol_catch_release.log, openflow.log.
Detection
Detection and possible indicator logs.
intel.log, notice.log, notice_alarm.log, signatures.log, traceroute.log.
Network Observations
Network flow logs.
known_certs.log, known_hosts.log, known_modbus.log, known_services.log, software.log.
Miscellaneous
Additional logs cover external alerts, inputs and failures.
barnyard2.log, dpd.log, unified2.log, unknown_protocols.log, weird.log, weird_stats.log.
Zeek Diagnostic
Zeek diagnostic logs cover system messages, actions and some statistics.
broker.log, capture_loss.log, cluster.log, config.log, loaded_scripts.log, packet_filter.log, print.log, prof.log, reporter.log, stats.log, stderr.log, stdout.log.
Please refer to Zeek's official documentation and Corelight log cheat sheet for more information. Although there are multiple log files, some log files are updated daily, and some are updated in each session. Some of the most commonly used logs are explained in the given table. https://docs.zeek.org/en/current/script-reference/log-files.html
https://corelight.com/about-zeek/zeek-data
Update Frequency	Log Name
Description
Daily	known_hosts.log	 List of hosts that completed TCP handshakes.
Daily	known_services.log	 List of services used by hosts.
Daily	known_certs.log	 List of SSL certificates.
Daily	software.log	 List of software used on the network.
Per Session	notice.log	 Anomalies detected by Zeek.
Per Session
intel.log	 Traffic contains malicious patterns/indicators.
Per Session
signatures.log	 List of triggered signatures.
This is too much protocol and log information! Yes, it is true; a difficulty of working with Zeek is having the required network knowledge and investigation mindset. Don't worry; you can have both of these and even more knowledge by working through TryHackMe paths. Just keep the streak!
Brief log usage primer table;
Overall Info	Protocol Based	Detection	Observation
conn.log	http.log	notice.log	known_host.log
files.log	dns.log	signatures.log	known_services.log
intel.log	ftp.log	pe.log	software.log
loaded_scripts.log	ssh.log	traceroute.log	weird.log
You can categorise the logs before starting an investigation. Thus, finding the evidence/anomaly you are looking for will be easier. The given table is a brief example of using multiple log files. You can create your working model or customise the given one. Make sure you read each log description and understand the purpose to know what to expect from the corresponding log file. Note that these are not the only ones to focus on. Investigated logs are highly associated with the investigation case type and hypothesis, so do not just rely only on the logs given in the example table!
The table shows us how to use multiple logs to identify anomalies and run an investigation by correlating across the available logs.
Overall Info: The aim is to review the overall connections, shared files, loaded scripts and indicators at once. This is the first step of the investigation.
Protocol Based: Once you review the overall traffic and find suspicious indicators or want to conduct a more in-depth investigation, you focus on a specific protocol.
Detection: Use the prebuild or custom scripts and signature outcomes to support your findings by having additional indicators or linked actions.
Observation: The summary of the hosts, services, software, and unexpected activity statistics will help you discover possible missing points and conclude the investigation.
Remember, we mention the pros and cons of the Zeek logs at the beginning of this task. Now let's demonstrate the log viewing and identify the differences between them.
Recall 1: Zeek logs are well structured and tab-separated ASCII files, so reading and processing them is easy but requires effort.
Recall 2: Investigating the generated logs will require command-line tools (cat, cut, grep sort, and uniq) and additional tools (zeek-cut).
Opening a Zeek log with a text editor and built-in commands;
The above image shows that reading the logs with tools is not enough to spot an anomaly quickly. Logs provide a vast amount of data to investigate and correlate. You will need to have technical knowledge and event correlation ability to carry out an investigation. It is possible to use external visualisation and correlation tools such as ELK and Splunk. We will focus on using and processing the logs with a hands-on approach in this room.
In addition to Linux command-line tools, one auxiliary program called zeek-cut reduces the effort of extracting specific columns from log files. Each log file provides "field names" in the beginning. This information will help you while using zeek-cut. Make sure that you use the "fields" and not the "types".
Tool/Auxilary Name	Purpose
Zeek-cut	Cut specific columns from zeek logs.
Let's see the "zeek-cut" in action. Let's extract the uid, protocol, source and destination hosts, and source and destination ports from the conn.log. We will first read the logs with the cat command and then extract the event of interest fields with zeek-cut auxiliary to compare the difference.
```text
zeek-cut usage example

           
root@ubuntu$ cat conn.log 
...
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	proto	service	duration	orig_bytes	resp_bytes	conn_state	local_orig	local_resp	missed_bytes	history	orig_pkts	orig_ip_bytes	resp_pkts	resp_ip_bytes	tunnel_parents
#types	time	string	addr	port	addr	port	enum	string	interval	count	count	string	bool	bool	count	string	count	count	count	count	set[string]
1488571051.943250	CTMFXm1AcIsSnq2Ric	192.168.121.2	51153	192.168.120.22	53	udp	dns	0.001263	36	106	SF	-	-0	Dd	1	64	1	134	-
1488571038.380901	CLsSsA3HLB2N6uJwW	192.168.121.10	50080	192.168.120.10	514	udp	-	0.000505	234	0	S0	-	-0	D	2	290	0	0	-

root@ubuntu$ cat conn.log | zeek-cut uid proto id.orig_h id.orig_p id.resp_h id.resp_p 
CTMFXm1AcIsSnq2Ric	udp	192.168.121.2	51153	192.168.120.22	53
CLsSsA3HLB2N6uJwW	udp	192.168.121.10	50080	192.168.120.10	514
```
As shown in the above output, the "zeek-cut" auxiliary provides massive help to extract specific fields with minimal effort. Now take time to read log formats, practice the log reading/extracting operations and answer the questions.
Each exercise has a folder. Ensure you are in the right directory to find the pcap file and accompanying files. Desktop/Exercise-Files/TASK-3
```text
root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-2# cd ../TASK-3/
root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-3# ls
clear-logs.sh  sample.pcap

You have new mail in /var/mail/root

let's see the email

root@ip-10-10-201-211:/var/mail# cat root
From root@tryhackme.eu-west-1.compute.internal  Thu Dec  8 19:00:06 2022
Return-Path: <root@tryhackme.eu-west-1.compute.internal>
X-Original-To: root@localhost
Delivered-To: root@localhost
Received: by tryhackme.eu-west-1.compute.internal (Postfix, from userid 0)
	id 66341138811; Thu,  8 Dec 2022 19:00:06 +0000 (UTC)
From: Zeek <zeek@ip-10-10-201-211>
Subject: [Zeek] Connection summary from 18:30:43-19:00:00
To: root@localhost
User-Agent: ZeekControl 2.4.0
Message-Id: <20221208190006.66341138811@tryhackme.eu-west-1.compute.internal>

>== Total === 2022-12-08-18-28-53 - 2022-12-08-18-43-53
   - Connections  23.0 - Payload 251.4k - 
     Ports        | Sources                           | Destinations              | Services           | Protocols | States        |
     80     43.5% | 10.10.201.211#1             82.6% | 169.254.169.254#2   34.8% | -            82.6% | 17  52.2% | OTH     56.5% | 
     123    21.7% | fe80::20:d5ff:fe9a:f0eb#3    8.7% | 10.10.201.211#4      8.7% | dns          13.0% | 6   43.5% | SHR     30.4% | 
     5353    8.7% | 10.100.1.202#5               8.7% | 10.10.0.1#6          8.7% | dhcp          4.3% | 1    4.3% | S0       8.7% | 
     53      8.7% |                                   | 10.0.0.2#7           8.7% |                    |           | SH       4.3% | 
     5351    4.3% |                                   | ff02::fb#8           4.3% |                    |           |               | 
     1900    4.3% |                                   | ff02::2#9            4.3% |                    |           |               | 
     134     4.3% |                                   | 239.255.255.250#10   4.3% |                    |           |               | 
     67      4.3% |                                   | 224.0.0.251#11       4.3% |                    |           |               | 
                  |                                   | 185.125.190.58#12    4.3% |                    |           |               | 
                  |                                   | 185.125.190.57#13    4.3% |                    |           |               | 

        #1=ip-10-10-201-211.eu-west-1.compute.internal  #2=<???>  #3=ip-10-10-201-211  
        #4=ip-10-10-201-211.eu-west-1.compute.internal  #5=ip-10-100-1-202.eu-west-1.compute.internal  #6=ip-10-10-0-1.eu-west-1.compute.internal  
        #7=ip-10-0-0-2.eu-west-1.compute.internal  #8=<???>  #9=ip6-allrouters  
        #10=<???>  #11=<???>  #12=prod-ntp-5.ntp4.ps5.canonical.com  
        #13=prod-ntp-4.ntp4.ps5.canonical.com  

>== Top 10 local networks by number of connections

     1  19.0  10.10.57.178/16  TryHackMe 
     2   2.0  10.0.0.0/8       Private IP space 
     3     0  172.16.0.0/12    Private IP space 
     4     0  192.168.0.0/16   Private IP space 

>== 2 connections did not have any local address. Here are the first 10:

    fe80::20:d5ff:fe9a:f0eb <-> ff02::2
    fe80::20:d5ff:fe9a:f0eb <-> ff02::fb

>== Incoming === N/A - N/A
   - Connections 0 - Payload 0 - 
     Ports        | Sources                   | Destinations              | Services           | Protocols | States        |
                  |                           |                           |                    |           |               | 
      

>== Outgoing === 2022-12-08-18-28-53 - 2022-12-08-18-43-53
   - Connections  21.0 - Payload 251.4k - 
     Ports        | Sources                   | Destinations              | Services           | Protocols | States        |
     80     47.6% | 10.10.201.211#1     90.5% | 169.254.169.254#2   38.1% | -            85.7% | 17  52.4% | OTH     57.1% | 
     123    23.8% | 10.100.1.202#3       9.5% | 10.10.201.211#4      9.5% | dns           9.5% | 6   47.6% | SHR     33.3% | 
     53      9.5% |                           | 10.10.0.1#5          9.5% | dhcp          4.8% |           | SH       4.8% | 
     5353    4.8% |                           | 10.0.0.2#6           9.5% |                    |           | S0       4.8% | 
     5351    4.8% |                           | 239.255.255.250#7    4.8% |                    |           |               | 
     1900    4.8% |                           | 224.0.0.251#8        4.8% |                    |           |               | 
     67      4.8% |                           | 185.125.190.58#9     4.8% |                    |           |               | 
                  |                           | 185.125.190.57#10    4.8% |                    |           |               | 
                  |                           | 185.125.190.56#11    4.8% |                    |           |               | 
                  |                           | 91.189.94.4#12       4.8% |                    |           |               | 

        #1=ip-10-10-201-211.eu-west-1.compute.internal  #2=<???>  #3=ip-10-100-1-202.eu-west-1.compute.internal  
        #4=ip-10-10-201-211.eu-west-1.compute.internal  #5=ip-10-10-0-1.eu-west-1.compute.internal  #6=ip-10-0-0-2.eu-west-1.compute.internal  
        #7=<???>  #8=<???>  #9=prod-ntp-5.ntp4.ps5.canonical.com  
        #10=prod-ntp-4.ntp4.ps5.canonical.com  #11=prod-ntp-3.ntp4.ps5.canonical.com  #12=pugot.canonical.com  
        

>== 10.10.57.178/16 TryHackMe === 2022-12-08-18-30-43 - 2022-12-08-18-43-00
   - Connections  19.0 - Payload 2.4k - 
     Ports        | Sources                   | Destinations              | Services           | Protocols | States        |
     80     42.1% | 10.10.201.211#1    100.0% | 169.254.169.254#2   42.1% | -            84.2% | 17  57.9% | OTH     63.2% | 
     123    26.3% |                           | 10.10.0.1#3         10.5% | dns          10.5% | 6   42.1% | SHR     36.8% | 
     53     10.5% |                           | 10.0.0.2#4          10.5% | dhcp          5.3% |           |               | 
     5353    5.3% |                           | 239.255.255.250#5    5.3% |                    |           |               | 
     5351    5.3% |                           | 224.0.0.251#6        5.3% |                    |           |               | 
     1900    5.3% |                           | 185.125.190.58#7     5.3% |                    |           |               | 
     67      5.3% |                           | 185.125.190.57#8     5.3% |                    |           |               | 
                  |                           | 185.125.190.56#9     5.3% |                    |           |               | 
                  |                           | 91.189.94.4#10       5.3% |                    |           |               | 
                  |                           | 91.189.91.157#11     5.3% |                    |           |               | 

        #1=ip-10-10-201-211.eu-west-1.compute.internal  #2=<???>  #3=ip-10-10-0-1.eu-west-1.compute.internal  
        #4=ip-10-0-0-2.eu-west-1.compute.internal  #5=<???>  #6=<???>  
        #7=prod-ntp-5.ntp4.ps5.canonical.com  #8=prod-ntp-4.ntp4.ps5.canonical.com  #9=prod-ntp-3.ntp4.ps5.canonical.com  
        #10=pugot.canonical.com  #11=alphyn.canonical.com  

>== 10.0.0.0/8 Private IP space === 2022-12-08-18-28-53 - 2022-12-08-18-43-53
   - Connections  2.0 - Payload 249.0k - 
     Ports        | Sources                   | Destinations              | Services           | Protocols | States        |
     80    100.0% | 10.100.1.202#1     100.0% | 10.10.201.211#2    100.0% | -           100.0% | 6  100.0% | SH      50.0% | 
                  |                           |                           |                    |           | S0      50.0% | 
                  |                           |                           |                    |           |               
        #1=ip-10-100-1-202.eu-west-1.compute.internal  #2=ip-10-10-201-211.eu-west-1.compute.internal  

First: 2022-12-08-18-28-53 (1670524133.901989) Last: 2022-12-08-18-43-53 1670525033.634755
0:05.64 real, 0.09 user, 0.05 sys, 0K total memory

-- 
[Automatically generated.]

From root@tryhackme.eu-west-1.compute.internal  Thu Dec  8 20:00:06 2022
Return-Path: <root@tryhackme.eu-west-1.compute.internal>
X-Original-To: root@localhost
Delivered-To: root@localhost
Received: by tryhackme.eu-west-1.compute.internal (Postfix, from userid 0)
	id 09B8713881B; Thu,  8 Dec 2022 20:00:06 +0000 (UTC)
From: Zeek <zeek@ip-10-10-201-211>
Subject: [Zeek] Connection summary from 19:00:00-20:00:00
To: root@localhost
User-Agent: ZeekControl 2.4.0
Message-Id: <20221208200006.09B8713881B@tryhackme.eu-west-1.compute.internal>

>== Total === 2022-12-08-19-00-00 - 2022-12-08-19-58-36
   - Connections  46.0 - Payload 5.9k - 
     Ports        | Sources                           | Destinations              | Services           | Protocols | States        |
     53     34.8% | 10.10.201.211#1             91.3% | 10.0.0.2#2          34.8% | -            56.5% | 17  69.6% | SHR     52.2% | 
     80     26.1% | fe80::20:d5ff:fe9a:f0eb#3    8.7% | 169.254.169.254#4   26.1% | dns          39.1% | 6   26.1% | OTH     43.5% | 
     123    21.7% |                                   | ff02::fb#5           4.3% | dhcp          4.3% | 1    4.3% | S0       4.3% | 
     5353    8.7% |                                   | ff02::2#6            4.3% |                    |           |               | 
     134     4.3% |                                   | 224.0.0.251#7        4.3% |                    |           |               | 
     67      4.3% |                                   | 185.125.190.58#8     4.3% |                    |           |               | 
                  |                                   | 185.125.190.57#9     4.3% |                    |           |               | 
                  |                                   | 185.125.190.56#10    4.3% |                    |           |               | 
                  |                                   | 91.189.94.4#11       4.3% |                    |           |               | 
                  |                                   | 91.189.91.157#12     4.3% |                    |           |               | 

        #1=ip-10-10-201-211.eu-west-1.compute.internal  #2=ip-10-0-0-2.eu-west-1.compute.internal  #3=ip-10-10-201-211  
        #4=<???>  #5=<???>  #6=ip6-allrouters  
        #7=<???>  #8=prod-ntp-5.ntp1.ps5.canonical.com  #9=prod-ntp-4.ntp1.ps5.canonical.com  
        #10=prod-ntp-3.ntp1.ps5.canonical.com  #11=pugot.canonical.com  #12=alphyn.canonical.com  
        

>== Top 10 local networks by number of connections

     1  42.0  10.10.57.178/16  TryHackMe 
     2     0  10.0.0.0/8       Private IP space 
     3     0  172.16.0.0/12    Private IP space 
     4     0  192.168.0.0/16   Private IP space 

>== 4 connections did not have any local address. Here are the first 10:

    fe80::20:d5ff:fe9a:f0eb <-> ff02::2
    fe80::20:d5ff:fe9a:f0eb <-> ff02::fb

>== Incoming === N/A - N/A
   - Connections 0 - Payload 0 - 
     Ports        | Sources                   | Destinations              | Services           | Protocols | States        |
                  |                           |                           |                    |           |               | 
          

>== Outgoing === 2022-12-08-19-00-00 - 2022-12-08-19-40-43
   - Connections  42.0 - Payload 5.8k - 
     Ports        | Sources                   | Destinations              | Services           | Protocols | States        |
     53     38.1% | 10.10.201.211#1    100.0% | 10.0.0.2#2          38.1% | -            57.1% | 17  71.4% | SHR     57.1% | 
     80     28.6% |                           | 169.254.169.254#3   28.6% | dns          38.1% | 6   28.6% | OTH     42.9% | 
     123    23.8% |                           | 224.0.0.251#4        4.8% | dhcp          4.8% |           |               | 
     5353    4.8% |                           | 185.125.190.58#5     4.8% |                    |           |               | 
     67      4.8% |                           | 185.125.190.57#6     4.8% |                    |           |               | 
                  |                           | 185.125.190.56#7     4.8% |                    |           |               | 
                  |                           | 91.189.94.4#8        4.8% |                    |           |               | 
                  |                           | 91.189.91.157#9      4.8% |                    |           |               | 
                  |                           | 10.10.0.1#10         4.8% |                    |           |               | 
                  |                           |                           |                    |           |               | 

        #1=ip-10-10-201-211.eu-west-1.compute.internal  #2=ip-10-0-0-2.eu-west-1.compute.internal  #3=<???>  
        #4=<???>  #5=prod-ntp-5.ntp1.ps5.canonical.com  #6=prod-ntp-4.ntp1.ps5.canonical.com  
        #7=prod-ntp-3.ntp1.ps5.canonical.com  #8=pugot.canonical.com  #9=alphyn.canonical.com  
        #10=ip-10-10-0-1.eu-west-1.compute.internal  

>== 10.10.57.178/16 TryHackMe === 2022-12-08-19-00-00 - 2022-12-08-19-40-43
   - Connections  42.0 - Payload 5.8k - 
     Ports        | Sources                   | Destinations              | Services           | Protocols | States        |
     53     38.1% | 10.10.201.211#1    100.0% | 10.0.0.2#2          38.1% | -            57.1% | 17  71.4% | SHR     57.1% | 
     80     28.6% |                           | 169.254.169.254#3   28.6% | dns          38.1% | 6   28.6% | OTH     42.9% | 
     123    23.8% |                           | 224.0.0.251#4        4.8% | dhcp          4.8% |           |               | 
     5353    4.8% |                           | 185.125.190.58#5     4.8% |                    |           |               | 
     67      4.8% |                           | 185.125.190.57#6     4.8% |                    |           |               | 
                  |                           | 185.125.190.56#7     4.8% |                    |           |               | 
                  |                           | 91.189.94.4#8        4.8% |                    |           |               | 
                  |                           | 91.189.91.157#9      4.8% |                    |           |               | 
                  |                           | 10.10.0.1#10         4.8% |                    |           |               | 
                  |                           |                           |                    |           |               | 

        #1=ip-10-10-201-211.eu-west-1.compute.internal  #2=ip-10-0-0-2.eu-west-1.compute.internal  #3=<???>  
        #4=<???>  #5=prod-ntp-5.ntp1.ps5.canonical.com  #6=prod-ntp-4.ntp1.ps5.canonical.com  
        #7=prod-ntp-3.ntp1.ps5.canonical.com  #8=pugot.canonical.com  #9=alphyn.canonical.com  
        #10=ip-10-10-0-1.eu-west-1.compute.internal  

First: 2022-12-08-19-00-00 (1670526000.924854) Last: 2022-12-08-19-58-36 1670529516.660470
0:05.55 real, 0.11 user, 0.04 sys, 0K total memory

-- 
[Automatically generated.]

let's continue ...

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-3# zeekctl status
Warning: new zeek version detected (run the zeekctl "deploy" command)
Name         Type       Host          Status    Pid    Started
zeek         standalone localhost     running   8280   08 Dec 18:28:51
root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-3# ls
clear-logs.sh  sample.pcap
root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-3# zeek -C -r sample.pcap 

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-3# ls
clear-logs.sh  dhcp.log  ntp.log            sample.pcap  ssh.log
conn.log       dns.log   packet_filter.log  snmp.log     syslog.log

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-3# cat dhcp.log 
#separator \x09
#set_separator	,
#empty_field	(empty)
#unset_field	-
#path	dhcp
#open	2022-12-08-20-18-21
#fields	ts	uids	client_addr	server_addr	mac	host_name	client_fqdn	domain	requested_addr	assigned_addr	lease_time	client_message	server_message	msg_types	duration
#types	time	set[string]	addr	addr	string	string	string	stringaddr	addr	interval	string	string	vector[string]	interval
1488571152.666896	CBfp2q4pJMu8eBjq2b,CxqL5739TyybHBO7eb	-	-	00:21:70:e9:bb:47	Microknoppix	-	-	192.168.20.11	-	-	--	REQUEST,NAK	0.009251
1488571152.699148	CBfp2q4pJMu8eBjq2b,CsskKT1dYYdLVx1G3l	192.168.30.11	192.168.30.1	00:21:70:e9:bb:47	Microknoppix	-	webernetz.net	192.168.30.11	192.168.30.11	86400.000000	-	-	DISCOVER,OFFER,REQUEST,ACK	0.022753
#close	2022-12-08-20-18-21

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-3# cat dhcp.log | zeek-cut host_name
Microknoppix
Microknoppix

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-3# cat dns.log |zeek-cut uid
C5VvgirtmbSkLFZp3
C9QtH84h0Ru9var3tk
C9QtH84h0Ru9var3tk
C9QtH84h0Ru9var3tk
C9QtH84h0Ru9var3tk
C1J4wh1lVBHOUrutxb
C1J4wh1lVBHOUrutxb
C1J4wh1lVBHOUrutxb
C1J4wh1lVBHOUrutxb
CWqDVu3Y15ylyuWqxe
CWqDVu3Y15ylyuWqxe
CWqDVu3Y15ylyuWqxe
CWqDVu3Y15ylyuWqxe
C82I5f3PV5Fb7C49C8
C0OwDY35cqVpr33OPb
Cvwr882C7NpodZpA76

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-3# cat dns.log |zeek-cut uid | wc -l
16

jaja

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-3# cat dns.log | zeek-cut query
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
ip.webernetz.net

2 :)

thanks openai
```
```text
┌──(kali㉿kali)-[~] └─$ cat zeek_test blog.webernetz.net blog.webernetz.net blog.webernetz.net blog.webernetz.net blog.webernetz.net blog.webernetz.net blog.webernetz.net blog.webernetz.net blog.webernetz.net blog.webernetz.net blog.webernetz.net blog.webernetz.net blog.webernetz.net blog.webernetz.net blog.webernetz.net ip.webernetz.net Como harias para contar solo los que no se repitan con un comando?

Para contar los elementos de una lista que no se repiten, puedes usar el comando `uniq`. Este comando elimina las entradas duplicadas de una lista y muestra solo las entradas únicas.

Para contar las entradas únicas en el archivo `zeek_test`, puedes usar el comando `uniq -u zeek_test | wc -l`. Esto eliminará las entradas duplicadas del archivo `zeek_test` y luego contará cuántas entradas únicas quedan.

Si deseas contar las entradas duplicadas en lugar de las únicas, puedes usar el comando `uniq -d zeek_test | wc -l`. Esto eliminará las entradas únicas del archivo `zeek_test` y luego contará cuántas entradas duplicadas quedan.
```
```text
┌──(kali㉿kali)-[~]
└─$ cat zeek_test                
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
ip.webernetz.net
```
```text
┌──(kali㉿kali)-[~]
└─$ uniq -u zeek_test | wc -l
1
```
```text
┌──(kali㉿kali)-[~]
└─$ uniq -d zeek_test | wc -l
1

Si deseas contar solo una de las entradas que se repiten y luego contar la otra entrada única, puedes usar el comando `sort zeek_test | uniq | wc -l`. Esto ordenará las entradas del archivo `zeek_test`, eliminará las entradas duplicadas y luego contará cuántas entradas quedan en total.

Es importante tener en cuenta que el comando `uniq` solo funciona correctamente si las entradas están ordenadas de forma consecutiva. Por lo tanto, es necesario usar el comando `sort` antes de usar `uniq`.
```
```text
┌──(kali㉿kali)-[~]
└─$ sort zeek_test | uniq | wc -l
2

so

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-3# cat dns.log | zeek-cut query | uniq | wc -l
2

:)

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-3# cat conn.log | zeek-cut duration
0.001263
0.000505
0.002007
0.007001
0.002503
0.002487
0.182281
0.183525
26.848411
31.470888
33.422941
0.006755
38.919292
8.998396
-
0.002746
0.182530
9.999806
8.998406
57.384652
-
-
0.017002
0.048754
7.785955
0.002747
0.180026
9.998803
2.113827
8.998898
0.026505
0.004370
168.998982
0.002623
0.003750
0.180025
-
0.001252
9.998804
10.192086
-
-
-
-
-
-
-
0.002512
0.002749
0.183527
0.184153
37.608581
0.001001
0.001122
0.027877
-
0.016002
0.182027
0.182652
0.002498
0.002626
0.005747
0.000558
31.242600
0.008248
0.003744
62.871527
0.002289
63.399855
36.978736
43.843556
53.644578
319.846921
0.001502
329.899861
309.515828
300.183120
0.012496
307.422751
331.791038
304.539681
305.791751
300.012100
332.319364
59.206449
325.924370
76.127078

just looking 

or

root@ip-10-10-201-211:/home/ubuntu/Desktop/Exercise-Files/TASK-3# cat conn.log | zeek-cut duration | sort -nr
332.319364
331.791038
329.899861
325.924370
319.846921
```
Investigate the sample.pcap file. Investigate the dhcp.log file. What is the available hostname?
*Microknoppix*
Investigate the dns.log file. What is the number of unique DNS queries?
*2*
Investigate the conn.log file. What is the longest connection duration?
*332.319364*
### CLI Kung-Fu Recall: Processing Zeek Logs
CLI Kung-Fu Recall: Processing Zeek Logs
Graphical User Interfaces (GUI) are handy and good for accomplishing tasks and processing information quickly. There are multiple advantages of GUIs, especially when processing the information visually. However, when processing massive amounts of data, GUIs are not stable and as effective as the CLI (Command Line Interface) tools.
The critical point is: What if there is no "function/button/feature" for what you want to find/view/extract?
Having the power to manipulate the data at the command line is a crucial skill for analysts. Not only in this room but each time you deal with packets, you will need to use command-line tools, Berkeley Packet Filters (BPF) and regular expressions to find/view/extract the data you are looking for. This task provides quick cheat-sheet like information to help you write CLI queries for your event of interest.
The Berkeley Packet Filter (BPF) is a technology used in certain computer operating systems for programs that need to, among other things, analyze network traffic. BPF supports filtering packets, allowing a userspace process to supply a filter program that specifies which packets it wants to receive.
```text
Category
	Command Purpose and Usage 
	Category
	Command Purpose and Usage 
Basics
	

View the command history:
ubuntu@ubuntu$ history

Execute the 10th command in history:
ubuntu@ubuntu$ !10

Execute the previous command:
ubuntu@ubuntu$ !!
	Read File	

Read sample.txt file:
ubuntu@ubuntu$ cat sample.txt

Read the first 10 lines of the file:
ubuntu@ubuntu$ head sample.txt

Read the last 10 lines of the file:
ubuntu@ubuntu$ tail sample.txt

Find
&
Filter
	

Cut the 1st field:
ubuntu@ubuntu$ cat test.txt | cut -f 1

Cut the 1st column:
ubuntu@ubuntu$ cat test.txt | cut -c1

Filter specific keywords:
ubuntu@ubuntu$ cat test.txt | grep 'keywords'

Sort outputs alphabetically:
ubuntu@ubuntu$ cat test.txt | sort

Sort outputs numerically:
ubuntu@ubuntu$ cat test.txt | sort -n

Eliminate duplicate lines:
ubuntu@ubuntu$ cat test.txt | uniq

Count line numbers:
ubuntu@ubuntu$ cat test.txt | wc -l

Show line numbers
ubuntu@ubuntu$ cat test.txt | nl
	Advanced
	

Print line 11:
ubuntu@ubuntu$ cat test.txt | sed -n '11p'

Print lines between 10-15:
ubuntu@ubuntu$ cat test.txt | sed -n '10,15p'

Print lines below 11:
ubuntu@ubuntu$ cat test.txt | awk 'NR < 11 {print $0}'

Print line 11:
ubuntu@ubuntu$ cat test.txt | awk 'NR == 11 {print $0}'
Special	
Filter specific fields of Zeek logs:
ubuntu@ubuntu$ cat signatures.log | zeek-cut uid src_addr dst_addr
Use Case	Description

sort | uniq
	Remove duplicate values.

sort | uniq -c 
	Remove duplicates and count the number of occurrences for each value.

sort -nr
	Sort values numerically and recursively.

rev
	Reverse string characters.

cut -f 1
	Cut field 1.

cut -d '.' -f 1-2
	Split the string on every dot and print keep the first two fields.

grep -v 'test'
	Display lines that  don't match the "test" string.

grep -v -e 'test1' -e 'test2'
	Display lines that don't match one or both "test1" and "test2" strings.

file 
	View file information.

grep -rin Testvalue1 * | column -t | less -S
	Search the "Testvalue1" string everywhere, organise column spaces and view the output with less.
```
```text
practicing
```
```text
┌──(kali㉿kali)-[~]
└─$ history  

 2018  sort zeek_test | uniq -u | wc -l
 2019  sort zeek_test | uniq | wc -l
```
```text
┌──(kali㉿kali)-[~]
└─$ !2019
```
```text
┌──(kali㉿kali)-[~]
└─$ sort zeek_test | uniq | wc -l
2
```
```text
┌──(kali㉿kali)-[~]
└─$ !!
```
```text
┌──(kali㉿kali)-[~]
└─$ sort zeek_test | uniq | wc -l
2
```
```text
┌──(kali㉿kali)-[~]
└─$ head zeek_test 
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
```
```text
┌──(kali㉿kali)-[~]
└─$ tail zeek_test             
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
ip.webernetz.net
```
```text
┌──(kali㉿kali)-[~]
└─$ cat zeek_test | cut -d "." -f 1
blog
blog
blog
blog
blog
blog
blog
blog
blog
blog
blog
blog
blog
blog
blog
ip
```
```text
┌──(kali㉿kali)-[~]
└─$ cat zeek_test | cut -c1-11
blog.webern
blog.webern
blog.webern
blog.webern
blog.webern
blog.webern
blog.webern
blog.webern
blog.webern
blog.webern
blog.webern
blog.webern
blog.webern
blog.webern
blog.webern
ip.webernet
```
```text
┌──(kali㉿kali)-[~]
└─$ cat zeek_test | grep 'ip' 
ip.webernetz.net
```
```text
┌──(kali㉿kali)-[~]
└─$ cat zeek_test | sort     
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
ip.webernetz.net
```
```text
┌──(kali㉿kali)-[~]
└─$ cat zeek_test | sort -n
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
ip.webernetz.net
2
111
1998
2022
```
```text
┌──(kali㉿kali)-[~]
└─$ cat zeek_test | uniq   
blog.webernetz.net
ip.webernetz.net
111
1998
2022
2
```
```text
┌──(kali㉿kali)-[~]
└─$ cat zeek_test | wc -l          
9
```
```text
┌──(kali㉿kali)-[~]
└─$ cat zeek_test | uniq | wc -l
6
```
```text
┌──(kali㉿kali)-[~]
└─$ cat zeek_test | nl          
     1  blog.webernetz.net
     2  blog.webernetz.net
     3  blog.webernetz.net
     4  blog.webernetz.net
     5  ip.webernetz.net
     6  111
     7  1998
     8  2022
     9  2
```
```text
┌──(kali㉿kali)-[~]
└─$ cat zeek_test | sed -n "8p"
2022
```
```text
┌──(kali㉿kali)-[~]
└─$ cat zeek_test | sed -n "4,8p"
blog.webernetz.net
ip.webernetz.net
111
1998
2022

El comando `awk` se utiliza para realizar operaciones de procesamiento de texto en un archivo. En este caso, el comando imprime las primeras diez líneas del archivo `test.txt`

`awk` es el nombre del comando y no tiene una abreviatura conocida. El nombre `awk` proviene de las iniciales de los apellidos de sus creadores: Alfred V. Aho, Peter J. Weinberger y Brian W. Kernighan. Es una herramienta muy útil para el procesamiento de texto y se utiliza ampliamente en sistemas operativos como Linux y Unix.

Donde `NR` es una variable predefinida en `awk` que almacena el número de líneas procesadas hasta el momento, y `$0` se refiere a toda la línea de texto actual. El comando imprime cada línea del archivo `test.txt` mientras se cumpla la condición `NR < 11`, es decir, mientras el número de líneas procesadas sea menor que 11.
```
```text
┌──(kali㉿kali)-[~]
└─$ cat zeek_test | awk 'NR < 11 {print $0}'
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
ip.webernetz.net
111
1998
2022
2
```
```text
┌──(kali㉿kali)-[~]
└─$ cat zeek_test | awk 'NR == 5 {print $0}'
ip.webernetz.net
```
```text
┌──(kali㉿kali)-[~]
└─$ sort zeek_test | uniq -c        
      1 111
      1 1998
      1 2
      1 2022
      4 blog.webernetz.net
      1 ip.webernetz.net
```
```text
┌──(kali㉿kali)-[~]
└─$ sort zeek_test -nr      
2022
1998
111
2
ip.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
```
```text
┌──(kali㉿kali)-[~]
└─$ rev zeek_test    
ten.ztenrebew.golb
ten.ztenrebew.golb
ten.ztenrebew.golb
ten.ztenrebew.golb
ten.ztenrebew.pi
111
8991
2202
2
```
```text
┌──(kali㉿kali)-[~]
└─$ cat zeek_test | cut -d '.' -f 1-3
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
blog.webernetz.net
ip.webernetz.net
111
1998
2022
2
```
```text
┌──(kali㉿kali)-[~]
└─$ cat zeek_test | cut -d '.' -f 1-2
blog.webernetz
blog.webernetz
blog.webernetz
blog.webernetz
ip.webernetz
111
1998
2022
2
```
```text
┌──(kali㉿kali)-[~]
└─$ cat zeek_test | grep -v 'webernetz'
111
1998
2022
2
```
```text
┌──(kali㉿kali)-[~]
└─$ cat zeek_test | grep -v -e 'webernetz' -e '2' 
111
1998
```
```text
┌──(kali㉿kali)-[~]
└─$ file zeek_test      
zeek_test: ASCII text
```
```text
┌──(kali㉿kali)-[~]
└─$ grep -riE "VER LA ip|MAC" /home/kali/Desktop
/home/kali/Desktop/comandos_mininet:Volcar información sobre todos los nodos:
/home/kali/Desktop/comandos_mininet:ver la ip del host1 virtual
/home/kali/Desktop/comandos_mininet:ver la MAC del host1 virtual
/home/kali/Desktop/comandos_mininet:py h1.MAC()

grep -rin Testvalue1 * | column -t | less -S que es lo que hace?

El comando `grep` se utiliza para buscar un patrón de texto en un archivo o conjunto de archivos. En este caso, el comando busca la cadena de texto "Testvalue1" en todos los archivos del directorio actual y sus subdirectorios.

La sintaxis del comando es la siguiente:

Copy code

`grep -rin Testvalue1 * | column -t | less -S`

El comando incluye varias opciones:

-   `-r`: indica a `grep` que busque recursivamente en todos los subdirectorios del directorio actual.
-   `-i`: hace que la búsqueda sea insensible a mayúsculas y minúsculas.
-   `-n`: imprime el número de línea junto a cada resultado.

La salida del comando `grep` se pasa a `column`, que formatea la salida en columnas, lo que la hace más fácil de leer. La salida de `column` se pasa a `less`, que permite navegar por la salida de forma paginada. La opción `-S` de `less` evita que las líneas se envuelvan al llegar al final de la pantalla.

En resumen, el comando busca recursivamente la cadena "Testvalue1" en todos los archivos del directorio actual y sus subdirectorios, imprime el número de línea junto a cada resultado y formatea la salida en columnas para facilitar su lectura. La salida se puede navegar de forma paginada usando `less`.
```
```text
┌──(kali㉿kali)-[~]
└─$ grep -rin ip.webernetz.net * | column -t | less -S

grep: Downloads/id_rsa: Permission denied
grep: hackthebox/Responder/certs/responder.key: Permission denied
zeek_test:5:ip.webernetz.net
```
### Zeek Signatures
Zeek Signatures
Zeek supports signatures to have rules and event correlations to find noteworthy activities on the network. Zeek signatures use low-level pattern matching and cover conditions similar to Snort rules. Unlike Snort rules, Zeek rules are not the primary event detection point. Zeek has a scripting language and can chain multiple events to find an event of interest. We focus on the signatures in this task, and then we will focus on Zeek scripting in the following tasks.
Zeek signatures are composed of three logical paths; signature id, conditions and action. The signature breakdown is shown in the table below;
Signature id	 Unique signature name.
Conditions
Header: Filtering the packet headers for specific source and destination addresses, protocol and port numbers.
Content: Filtering the packet payload for specific value/pattern.
Action
Default action: Create the "signatures.log" file in case of a signature match.
Additional action: Trigger a Zeek script.
Now let's dig more into the Zeek signatures. The below table provides the most common conditions and filters for the Zeek signatures.
Condition Field	Available Filters
Header
src-ip: Source IP.
dst-ip: Destination IP.
src-port: Source port.
dst-port: Destination port.
ip-proto: Target protocol. Supported protocols; TCP, UDP, ICMP, ICMP6, IP, IP6
Content	payload: Packet payload.
http-request: Decoded HTTP requests.
http-request-header: Client-side HTTP headers.
http-request-body: Client-side HTTP request bodys.
http-reply-header: Server-side HTTP headers.
http-reply-body: Server-side HTTP request bodys.
ftp: Command line input of FTP sessions.
Context	same-ip: Filtering the source and destination addresses for duplication.
Action	event: Signature match message.
Comparison
Operators	==, !=, <, <=, >, >=
NOTE!	 Filters accept string, numeric and regex values.
```text
Run Zeek with signature file

           
ubuntu@ubuntu$ zeek -C -r sample.pcap -s sample.sig
```
Zeek signatures use the ".sig" extension.
-C: Ignore checksum errors.
-r: Read pcap file.
-s: Use signature file.
Example | Cleartext Submission of Password
Let's create a simple signature to detect HTTP cleartext passwords.
View Signature
```text
Sample Signature

           
signature http-password {
     ip-proto == tcp
     dst_port == 80
     payload /.*password.*/
     event "Cleartext Password Found!"
}
```
```text
# signature: Signature name.
```
```text
# ip-proto: Filtering TCP connection.
```
```text
# dst-port: Filtering destination port 80.
```
```text
# payload: Filtering the "password" phrase.
```
```text
# event: Signature match message.
```
Remember, Zeek signatures support regex. Regex ".*" matches any character zero or more times. The rule will match when a "password" phrase is detected in the packet payload. Once the match occurs, Zeek will generate an alert and create additional log files (signatures.log and notice.log).
```text
Signature Usage and Log Analysis

           
ubuntu@ubuntu$ zeek -C -r http.pcap -s http-password.sig 
ubuntu@ubuntu$ ls
clear-logs.sh  conn.log  files.log  http-password.sig  http.log  http.pcap  notice.log  packet_filter.log  signatures.log

ubuntu@ubuntu$ cat notice.log  | zeek-cut id.orig_h id.resp_h msg 
10.10.57.178	44.228.249.3	10.10.57.178: Cleartext Password Found!
10.10.57.178	44.228.249.3	10.10.57.178: Cleartext Password Found!

ubuntu@ubuntu$ cat signatures.log | zeek-cut src_addr dest_addr sig_id event_msg 
10.10.57.178		http-password	10.10.57.178: Cleartext Password Found!
10.10.57.178		http-password	10.10.57.178: Cleartext Password Found!
```
As shown in the above terminal output, the signatures.log and notice.log provide basic details and the signature message. Both of the logs also have the application banner field. So it is possible to know where the signature match occurs. Let's look at the application banner!
```text
Log Analysis

           
ubuntu@ubuntu$ cat signatures.log | zeek-cut sub_msg
POST /userinfo.php HTTP/1.1\x0d\x0aHost: testphp.vulnweb.com\x0d\x0aUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/...

ubuntu@ubuntu$ cat notice.log  | zeek-cut sub
POST /userinfo.php HTTP/1.1\x0d\x0aHost: testphp.vulnweb.com\x0d\x0aUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/...
```
We will demonstrate only one log file output to avoid duplication after this point. You can practice discovering the event of interest by analysing notice.log and signatures.log.
Example | FTP Brute-force
Let's create another rule to filter FTP traffic. This time, we will use the FTP content filter to investigate command-line inputs of the FTP traffic. The aim is to detect FTP "admin" login attempts. This basic signature will help us identify the admin login attempts and have an idea of possible admin account abuse or compromise events.
```text
Sample Signature

           
signature ftp-admin {
     ip-proto == tcp
     ftp /.*USER.*dmin.*/
     event "FTP Admin Login Attempt!"
}
```
Let's run the Zeek with the signature and investigate the signatures.log and notice.log.
```text
FTP Signature

           
ubuntu@ubuntu$ zeek -C -r ftp.pcap -s ftp-admin.sig
ubuntu@ubuntu$ cat signatures.log | zeek-cut src_addr dst_addr event_msg sub_msg | sort -r| uniq
10.234.125.254	10.121.70.151	10.234.125.254: FTP Admin Login Attempt!	USER administrator
10.234.125.254	10.121.70.151	10.234.125.254: FTP Admin Login Attempt!	USER admin
```
Our rule shows us that there are multiple logging attempts with account names containing the "admin" phrase. The output gives us great information to notice if there is a brute-force attempt for an admin account.
This signature can be considered a case signature. While it is accurate and works fine, we need global signatures to detect the "known threats/anomalies". We will need those case-based signatures for significant and sophistical anomalies like zero-days and insider attacks in the real-life environment. Having individual rules for each case will create dozens of logs and alerts and cause missing the real anomaly. The critical point is logging logically, not logging everything.
We can improve our signature by not limiting the focus only to an admin account. In that case, we need to know how the FTP protocol works and the default response codes. If you don't know these details, please refer to RFC documentation.
https://datatracker.ietf.org/doc/html/rfc765
Let's optimise our rule and make it detect all possible FTP brute-force attempts.
This signature will create logs for each event containing "FTP 530 response", which allows us to track the login failure events regardless of username.
```text
Sample Signature

           
signature ftp-brute {
     ip-proto == tcp
     payload /.*530.*Login.*incorrect.*/
     event "FTP Brute-force Attempt"
}
```
Zeek signature files can consist of multiple signatures. Therefore we can have one file for each protocol/situation/threat type. Let's demonstrate this feature in our global rule.
```text
Sample Signature

           
signature ftp-username {
    ip-proto == tcp
    ftp /.*USER.*/
    event "FTP Username Input Found!"
}

signature ftp-brute {
    ip-proto == tcp
     payload /.*530.*Login.*incorrect.*/
    event "FTP Brute-force Attempt!"
}
```
Let's merge both of the signatures in a single file. We will have two different signatures, and they will generate alerts according to match status. The result will show us how we benefit from this action. Again, we will need the "CLI Kung-Fu" skills to extract the event of interest.
This rule should show us two types of alerts and help us to correlate the events by having "FTP Username Input" and "FTP Brute-force Attempt" event messages. Let's investigate the logs. We're grepping the logs in range 1001-1004 to demonstrate that the first rule matches two different accounts (admin and administrator).
```text
FTP Signature

           
ubuntu@ubuntu$ zeek -C -r ftp.pcap -s ftp-admin.sig
ubuntu@ubuntu$ cat notice.log | zeek-cut uid id.orig_h id.resp_h msg sub | sort -r| nl | uniq | sed -n '1001,1004p'
  1001	CeMYiaHA6AkfhSnd	10.234.125.254	10.121.70.151	10.234.125.254: FTP Username Input Found!	USER admin
  1002	CeMYiaHA6AkfhSnd	10.234.125.254	10.121.70.151	10.121.70.151: FTP Brute-force Attempt!	530 Login incorrect.
  1003	CeDTDZ2erDNF5w7dyf	10.234.125.254	10.121.70.151	10.234.125.254: FTP Username Input Found!	USER administrator
  1004	CeDTDZ2erDNF5w7dyf	10.234.125.254	10.121.70.151	10.121.70.151: FTP Brute-force Attempt!	530 Login incorrect.
```
Snort Rules in Zeek?
While Zeek was known as Bro, it supported Snort rules with a script called snort2bro, which converted Snort rules to Bro signatures. However, after the rebranding, workflows between the two platforms have changed. The official Zeek document mentions that the script is no longer supported and is not a part of the Zeek distribution.
Each exercise has a folder. Ensure you are in the right directory to find the pcap file and accompanying files. Desktop/Exercise-Files/TASK-5
Investigate the http.pcap file. Create the  HTTP signature shown in the task and investigate the pcap. What is the source IP of the first event?
You can use signatures.log or notice.log.
```text
ubuntu@ip-10-10-51-220:~/Desktop/Exercise-Files/TASK-5/http$ cat http-password.sig 
signature http-password {
    ip-proto == tcp
    dst-port == 80
    payload /.*password.*/
    event "Cleartext Password Found!"
}

ubuntu@ip-10-10-51-220:~/Desktop/Exercise-Files/TASK-5/http$ sudo su
root@ip-10-10-51-220:/home/ubuntu/Desktop/Exercise-Files/TASK-5/http# zeekctl start
Warning: new zeek version detected (run the zeekctl "deploy" command)
starting zeek ...
root@ip-10-10-51-220:/home/ubuntu/Desktop/Exercise-Files/TASK-5/http# zeekctl status
Warning: new zeek version detected (run the zeekctl "deploy" command)
Name         Type       Host          Status    Pid    Started
zeek         standalone localhost     running   2564   09 Dec 18:01:29

root@ip-10-10-51-220:/home/ubuntu/Desktop/Exercise-Files/TASK-5/http# zeek -C -r http.pcap -s http-password.sig 
root@ip-10-10-51-220:/home/ubuntu/Desktop/Exercise-Files/TASK-5/http# ls
clear-logs.sh  files.log          http.log   notice.log         signatures.log
conn.log       http-password.sig  http.pcap  packet_filter.log

root@ip-10-10-51-220:/home/ubuntu/Desktop/Exercise-Files/TASK-5/http# cat notice.log | zeek-cut id.orig_h id.resp_h msg
10.10.57.178	44.228.249.3	10.10.57.178: Cleartext Password Found!
10.10.57.178	44.228.249.3	10.10.57.178: Cleartext Password Found!

root@ip-10-10-51-220:/home/ubuntu/Desktop/Exercise-Files/TASK-5/http# cat signatures.log | zeek-cut src_addr dest_addr sig_id event_msg
10.10.57.178		http-password	10.10.57.178: Cleartext Password Found!
10.10.57.178		http-password	10.10.57.178: Cleartext Password Found!
root@ip-10-10-51-220:/home/ubuntu/Desktop/Exercise-Files/TASK-5/http# cat signatures.log | zeek-cut sig_id
http-password
http-password
```
*10.10.57.178*
What is the source port of the second event?
You can use signatures.log or notice.log.
```text
root@ip-10-10-51-220:/home/ubuntu/Desktop/Exercise-Files/TASK-5/http# cat signatures.log | zeek-cut src_port dest_port sig_id event_msg
38706		http-password	10.10.57.178: Cleartext Password Found!
38712		http-password	10.10.57.178: Cleartext Password Found!
```
*38712*
Investigate the conn.log.
What is the total number of the sent and received packets from source port 38706?
Sent packets (orig_pkts), received packets (resp_pkts) source port (id.orig_p).
```text
root@ip-10-10-51-220:/home/ubuntu/Desktop/Exercise-Files/TASK-5/http# cat conn.log  | zeek-cut orig_pkts resp_pkts id.orig_p | grep "38706"
11	9	38706
```
*20*
Create the global rule shown in the task and investigate the ftp.pcap file.
Investigate the notice.log. What is the number of unique events?
uid, sort and uniq will help
```text
root@ip-10-10-51-220:/home/ubuntu/Desktop/Exercise-Files/TASK-5/ftp# cat ftp-bruteforce.sig 
signature ftp-username {
    ip-proto == tcp
    ftp /.*USER.*/
    event "FTP Username Input Found!"
}

signature ftp-brute {
    ip-proto == tcp
    payload /.*530.*Login.*incorrect.*/
    event "FTP Brute-force Attempt!"
}

root@ip-10-10-51-220:/home/ubuntu/Desktop/Exercise-Files/TASK-5/ftp# zeek -C -r ftp.pcap -s ftp-bruteforce.sig 
root@ip-10-10-51-220:/home/ubuntu/Desktop/Exercise-Files/TASK-5/ftp# ls
clear-logs.sh  ftp-bruteforce.sig  notice.log         signatures.log
conn.log       ftp.pcap            packet_filter.log  weird.log

root@ip-10-10-51-220:/home/ubuntu/Desktop/Exercise-Files/TASK-5/ftp# cat notice.log | zeek-cut uid | sort | uniq | wc -l
1413
```
*1413*
What is the number of ftp-brute signature matches?
```text
root@ip-10-10-51-220:/home/ubuntu/Desktop/Exercise-Files/TASK-5/ftp# head notice.log 
#separator \x09
#set_separator	,
#empty_field	(empty)
#unset_field	-
#path	notice
#open	2022-12-09-18-19-15
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	fuid	file_mime_type	file_desc	proto	note	msg	sub	src	dst	p	n	peer_descr	actions	email_dest	suppress_for	remote_location.country_code	remote_location.region	remote_location.city	remote_location.latitude	remote_location.longitude

root@ip-10-10-51-220:/home/ubuntu/Desktop/Exercise-Files/TASK-5/ftp# tail ftp-bruteforce.sig 
    event "FTP Username Input Found!"
}

signature ftp-brute {
    ip-proto == tcp
    payload /.*530.*Login.*incorrect.*/
    event "FTP Brute-force Attempt!"
}

root@ip-10-10-51-220:/home/ubuntu/Desktop/Exercise-Files/TASK-5/ftp# cat notice.log  | zeek-cut msg | grep -i 'brute' | wc -l
1410
```
*1410*
### Zeek Scripts | Fundamentals
Zeek Scripts
Zeek has its own event-driven scripting language, which is as powerful as high-level languages and allows us to investigate and correlate the detected events. Since it is as capable as high-level programming languages, you will need to spend time on Zeek scripting language in order to become proficient. In this room, we will cover the basics of Zeek scripting to help you understand, modify and create basic scripts. Note that scripts can be used to apply a policy and in this case, they are called policy scripts.
Zeek has base scripts installed by default, and these are not intended to be modified.
These scripts are located in
"/opt/zeek/share/zeek/base".
User-generated or modified scripts should be located in a specific path.
These scripts are located in
"/opt/zeek/share/zeek/site".
Policy scripts are located in a specific path.
These scripts are located in
"/opt/zeek/share/zeek/policy".
Like Snort, to automatically load/use a script in live sniffing mode, you must identify the script in the Zeek configuration file. You can also use a script for a single run, just like the signatures.
