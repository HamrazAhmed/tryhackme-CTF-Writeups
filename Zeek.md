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
