---
Learn and practice log investigation, pcap analysis and threat hunting with Brim.
---

# Brim — Writeup

## Overview
### Brim — Writeup
### Brim — Writeup
### Introduction
BRIM is an open-source desktop application that processes pcap files and logs files. Its primary focus is providing search and analytics. In this room, you will learn how to use Brim, process pcap files and investigate log files to find the needle in the haystack! This room expects you to be familiar with basic security concepts and processing Zeek log files. We suggest completing the "Network Fundamentals" path and the "Zeek room" before starting working in this room.
https://www.brimdata.io/
A VM is attached to this room. You don't need SSH or RDP; the room provides a "Split View" feature. Exercise files are located in the folder on the desktop.
NOTE: DO NOT directly interact with any domains and IP addresses in this room.
### What is Brim?
What is Brim?
Brim is an open-source desktop application that processes pcap files and logs files, with a primary focus on providing search and analytics. It uses the Zeek log processing format. It also supports Zeek signatures and Suricata Rules for detection.
It can handle two types of data as an input;
Packet Capture Files: Pcap files created with tcpdump, tshark and Wireshark like applications.
Log Files: Structured log files like Zeek logs.
Brim is built on open-source platforms:
Zeek: Log generating engine.
Zed Language: Log querying language that allows performing keywoırd searches with filters and pipelines.
ZNG Data Format: Data storage format that supports saving data streams.
Electron and React: Cross-platform UI.
Why Brim?
Ever had to investigate a big pcap file? Pcap files bigger than one gigabyte are cumbersome for Wireshark. Processing big pcaps with tcpdump and Zeek is efficient but requires time and effort. Brim reduces the time and effort spent processing pcap files and investigating the log files by providing a simple and powerful GUI application.
Brim vs Wireshark vs Zeek
While each of them is powerful and useful, it is good to know the strengths and weaknesses of each tool and which one to use for the best outcome. As a traffic capture analyser, some overlapping functionalities exist, but each one has a unique value for different situations.
The common best practice is handling medium-sized pcaps with Wireshark, creating logs and correlating events with Zeek, and processing multiple logs in Brim.
Brim	Wireshark	Zeek
Purpose	Pcap processing; event/stream and log investigation.	Traffic sniffing. Pcap processing; packet and stream investigation.	Pcap processing; event/stream and log investigation.
GUI	✔
✔
✖
Sniffing	✖
✔
✔
Pcap processing	✔
✔
✔
Log processing	✔
✖
✔
Packet decoding	✖
✔
✔
Filtering	✔
✔
✔
Scripting
✖
✖
✔
Signature Support	✔
✖
✔
Statistics	✔
✔
✔
File Extraction	✖
✔
✔
Handling  pcaps over 1GB	Medium performance
Low performance
Good performance
Ease of Management	4/5	4/5	3/5
### The Basics
Landing Page
Once you open the application, the landing page loads up. The landing page has three sections and a file importing window. It also provides quick info on supported file formats.
Pools: Data resources, investigated pcap and log files.
Queries: List of available queries.
History: List of launched queries.
Pools and Log Details
Pools represent the imported files. Once you load a pcap, Brim processes the file and creates Zeek logs, correlates them, and displays all available findings in a timeline, as shown in the image below.
The timeline provides information about capture start and end dates. Brim also provides information fields. You can hover over fields to have more details on the field. The above image shows a user hovering over the Zeek's conn.log file and uid value. This information will help you in creating custom queries. The rest of the log details are shown in the right pane and provides details of the log file fields. Note that you can always export the results by using the export function located near the timeline.
You can correlate each log entry by reviewing the correlation section at the log details pane (shown on the left image). This section provides information on the source and destination addresses, duration and associated log files. This quick information helps you answer the "Where to look next?" question and find the event of interest and linked evidence.
You can also right-click on each field to filter and accomplish a list of tasks.
Filtering values
Counting fields
Sorting (A-Z and Z-A)
Viewing details
Performing whois lookup on IP address
Viewing the associated packets in Wireshark
The image below demonstrates how to perform whois lookup and Wireshark packet inspection.
Queries and History
Queries help us to correlate finding and find the event of the interest. History stores executed queries.
The image on the left demonstrates how to browse the queries and load a specific query from the library.
Queries can have names, tags and descriptions. Query library lists the query names, and once you double-click, it passes the actual query to the search bar.
You can double-click on the query and execute it with ease. Once you double-click on the query, the actual query appears on the search bar and is listed under the history tab.
The results are shown under the search bar. In this case, we listed all available log sources created by Brim. In this example, we only insert a pcap file, and it automatically creates nine types of Zeek log files.
Brim has 12 premade queries listed under the "Brim" folder. These queries help us discover the Brim query structure and accomplish quick searches from templates.  You can add new queries by clicking on the "+" button near the "Queries" menu.
Process the "sample.pcap" file and look at the details of the first DNS log that appear on the dashboard. What is the "qclass_name"?
You can review the details of the log files by "right-click --> "Open details".
![[Pasted image 20221211104118.png]]
*C_INTERNET*
Look at the details of the first NTP log that appear on the dashboard. What is the "duration" value?
The correlation section provides the duration value.
![[Pasted image 20221211104332.png]]
*0.005*
Look at the details of the STATS packet log that is visible on the dashboard. What is the "reassem_tcp_size"?
![[Pasted image 20221211104457.png]]
*540*
### Default Queries
Default Queries
We mentioned that Brim had 12 premade queries in the previous task. Let's see them in action! Now, open Brim, import the sample pcap and go through the walkthrough.
Reviewing Overall Activity
This query provides general information on the pcap file. The provided information is valuable for accomplishing further investigation and creating custom queries. It is impossible to create advanced or case-specific queries without knowing the available log files.
The image on the left shows that there are 20 logs generated for the provided pcap file.
Windows Specific Networking Activity
This query focuses on Windows networking activity and details the source and destination addresses and named pipe, endpoint and operation detection. The provided information helps investigate and understand specific Windows events like SMB enumeration, logins and service exploiting.
Brim - windows networking activity
Unique Network Connections and Transferred Data
These two queries provide information on unique connections and connection-data correlation. The provided info helps analysts detect weird and malicious connections and suspicious and beaconing activities. The uniq list provides a clear list of unique connections that help identify anomalies. The data list summarises the data transfer rate that supports the anomaly investigation hypothesis.
DNS and HTTP Methods
These queries provide the list of the DNS queries and HTTP methods. The provided information helps analysts to detect anomalous DNS and HTTP traffic. You can also narrow the search by viewing the "HTTP POST" requests with the available query and modifying it to view the "HTTP GET" methods.
File Activity
This query provides the list of the available files. It helps analysts to detect possible data leakage attempts and suspicious file activity. The query provides info on the detected file MIME and file name and hash values (MD5, SHA1).
IP Subnet Statistics
This query provides the list of the available IP subnets. It helps analysts detect possible communications outside the scope and identify out of ordinary IP addresses.
Suricata Alerts
These queries provide information based on Suricata rule results. Three different queries are available to view the available logs in different formats (category-based, source and destination-based, and subnet based).
Note: Suricata is an open-source threat detection engine that can act as a rule-based Intrusion Detection and Prevention System. It is developed by the Open Information Security Foundation (OISF). Suricata works and detects anomalies in a similar way to Snort and can use the same signatures.
Investigate the files. What is the name of the detected GIF file?
Use task4 pcap file.
![[Pasted image 20221211111745.png]]
![[Pasted image 20221211112014.png]]
*cat01_with_hidden_text.gif*
Investigate the conn logfile. What is the number of the identified city names?
You can filter the conn logfile and then view the available sections by scrolling the horizontal bar. _path=="conn" | cut geo.resp.country_code, geo.resp.region, geo.resp.city
_path=="conn" | cut geo.resp.country_code, geo.resp.region, geo.resp.city | sort geo.resp.city
![[Pasted image 20221211112359.png]]
*2*
Investigate the Suricata alerts. What is the Signature id of the alert category "Potential Corporate Privacy Violation"?
![[Pasted image 20221211112807.png]]
![[Pasted image 20221211112712.png]]
*2,012,887*
### Use Cases
Custom Queries and Use Cases
There are a variety of use case examples in traffic analysis. For a security analyst, it is vital to know the common patterns and indicators of anomaly or malicious traffic. In this task, we will cover some of them. Let's review the basics of the Brim queries before focusing on the custom and advanced ones.
Brim Query Reference
```text
Purpose	Syntax	Example Query
Basic search 	You can search any string and numeric value. 	

Find logs containing an IP address or any value.
10.0.0.1

Logical operators 	Or, And, Not. 	

Find logs contain three digits of an IP AND NTP keyword.
192 and NTP

Filter values	"field name" == "value"	

Filter source IP.
id.orig_h==192.168.121.40

List specific log file contents
	_path=="log name"
	

List the contents of the conn log file.
_path=="conn"

Count field values 	count () by "field"	

Count the number of the available log files.
count () by _path

Sort findings	sort	

Count the number of the available log files and sort recursively.
count () by _path | sort -r

Cut specific field from a log file	_path=="conn" | cut "field name"	

Cut the source IP, destination port and destination IP addresses from the conn log file.
_path=="conn" | cut id.orig_h, id.resp_p, id.resp_h

List unique values	uniq	

Show the unique network connections. 

_path=="conn" | cut id.orig_h, id.resp_p, id.resp_h | sort | uniq

Note: It is highly suggested to use field names and filtering options and not rely on the blind/irregular search function. Brim provides great indexing of log sources, but it is not performing well in irregular search queries. The best practice is always to use the field filters to search for the event of interest.
Communicated Hosts
	

Identifying the list of communicated hosts is the first step of the investigation. Security analysts need to know which hosts are actively communicating on the network to detect any suspicious and abnormal activity in the first place. This approach will help analysts to detect possible access violations, exploitation attempts and malware infections.

Query: _path=="conn" | cut id.orig_h, id.resp_h | sort | uniq
Frequently Communicated Hosts
	

After having the list of communicated hosts, it is important to identify which hosts communicate with each other most frequently. This will help security analysts to detect possible data exfiltration, exploitation and backdooring activities.

Query: _path=="conn" | cut id.orig_h, id.resp_h | sort | uniq -c | sort -r
Most Active Ports
	

Suspicious activities are not always detectable in the first place. Attackers use multiple ways of hiding and bypassing methods to avoid detection. However, since the data is evidence, it is impossible to hide the packet traces. Investigating the most active ports will help analysts to detect silent and well-hidden anomalies by focusing on the data bus and used services. 

Query: _path=="conn" | cut id.resp_p, service | sort | uniq -c | sort -r count

Query:  _path=="conn" | cut id.orig_h, id.resp_h, id.resp_p, service | sort id.resp_p | uniq -c | sort -r 
Long Connections
	

For security analysts, the long connections could be the first anomaly indicator. If the client is not designed to serve a continuous service, investigating the connection duration between two IP addresses can reveal possible anomalies like backdoors.

Query: _path=="conn" | cut id.orig_h, id.resp_p, id.resp_h, duration | sort -r duration
Transferred Data 
	

Another essential point is calculating the transferred data size. If the client is not designed to serve and receive files and act as a file server, it is important to investigate the total bytes for each connection. Thus, analysts can distinguish possible data exfiltration or suspicious file actions like malware downloading and spreading.

