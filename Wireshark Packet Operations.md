---
Learn the fundamentals of packet analysis with Wireshark and how to find the needle in the haystack!
---

# Wireshark Packet Operations — Writeup

## Overview
### Wireshark Packet Operations — Writeup
### Wireshark Packet Operations — Writeup
### Introduction
In this room, we will cover the fundamentals of packet analysis with Wireshark and investigate the event of interest at the packet-level. Note that this is the second room of the Wireshark room trio, and it is suggested to visit the first room (Wireshark: The Basics) to practice and refresh your Wireshark skills before starting this one.
In the first room, we covered the basics of the Wireshark by focusing on how it operates and how to use it to investigate traffic captures. In this room, we will cover advanced features of the Wireshark by focusing on packet-level details with Wireshark statistics, filters, operators and functions.
Note: A VM is attached to this room. You don't need SSH or RDP; the room provides a "Split View" feature. Access to the machine will be provided in-browser and will deploy in Split View mode in your browser. If you don't see it, use the blue Show Split View button at the top right of this room page to show it. DO NOT directly interact with any domains and IP addresses in this room. The domains and IP addresses are included for reference reasons only.

## Enumeration
```text
┌──(kali㉿kali)-[~]
└─$ nc -nvlp 4444 > Exercise.pcapng
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: Listening on :::4444
Ncat: Listening on 0.0.0.0:4444
Ncat: Connection from 10.10.196.189.
Ncat: Connection from 10.10.196.189:39626.
^C
```
```text
┌──(kali㉿kali)-[~]
└─$ ls -lah Exercise.pcapng
-rw-r--r-- 1 kali kali 118M Oct  9 15:58 Exercise.pcapng

nc 10.11.81.220 4444 < Exercise.pcapng
```
### Statistics | Summary
Statistics
This menu provides multiple statistics options ready to investigate to help users see the big picture in terms of the scope of the traffic, available protocols, endpoints and conversations, and some protocol-specific details like DHCP, DNS and HTTP/2. For a security analyst, it is crucial to know how to utilise the statical information. This section provides a quick summary of the processed pcap, which will help analysts create a hypothesis for an investigation. You can use the "Statistics" menu to view all available options. Now start the given VM, open the Wireshark, load the "Exercise.pcapng" file and go through the walkthrough.
Resolved Addresses
This option helps analysts identify IP addresses and DNS names available in the capture file by providing the list of the resolved addresses and their hostnames. Note that the hostname information is taken from DNS answers in the capture file. Analysts can quickly identify the accessed resources by using this menu. Thus they can spot accessed resources and evaluate them according to the event of interest. You can use the "Statistics --> Resolved Addresses" menu to view all resolved addresses by Wireshark.
Protocol Hierarchy
This option breaks down all available protocols from the capture file and helps analysts view the protocols in a tree view based on packet counters and percentages. Thus analysts can view the overall usage of the ports and services and focus on the event of interest. The golden rule mentioned in the previous room is valid in this section; you can right-click and filter the event of interest. You can use the "Statistics --> Protocol Hierarchy" menu to view this info.
Conversations
Conversation represents traffic between two specific endpoints. This option provides the list of the conversations in five base formats; ethernet, IPv4, IPv6, TCP and UDP. Thus analysts can identify all conversations and contact endpoints for the event of interest. You can use the "Statistic --> Conversations" menu to view this info.
Endpoints
The endpoints option is similar to the conversations option. The only difference is that this option provides unique information for a single information field (Ethernet, IPv4, IPv6, TCP and UDP ). Thus analysts can identify the unique endpoints in the capture file and use it for the event of interest. You can use the "Statistics --> Endpoints" menu to view this info.
Wireshark also supports resolving MAC addresses to human-readable format using the manufacturer name assigned by IEEE. Note that this conversion is done through the first three bytes of the MAC address and only works for the known manufacturers. When you review the ethernet endpoints, you can activate this option with the "Name resolution" button in the lower-left corner of the endpoints window.
Name resolution is not limited only to MAC addresses. Wireshark provides IP and port name resolution options as well. However, these options are not enabled by default. If you want to use these functionalities, you need to activate them through the "Edit --> Preferences --> Name Resolution" menu. Once you enable IP and port name resolution, you will see the resolved IP address and port names in the packet list pane and also will be able to view resolved names in the "Conversations" and "Endpoints" menus as well.
Endpoint menu view with name resolution:
Besides name resolution, Wireshark also provides an IP geolocation mapping that helps analysts identify the map's source and destination addresses. But this feature is not activated by default and needs supplementary data like the GeoIP database. Currently, Wireshark supports MaxMind databases, and the latest versions of the Wireshark come configured MaxMind DB resolver. However, you still need MaxMind DB files and provide the database path to Wireshark by using the "Edit --> Preferences --> Name Resolution --> MaxMind database directories" menu. Once you download and indicate the path, Wireshark will automatically provide GeoIP information under the IP protocol details for the matched IP addresses.
Endpoints and GeoIP view.
Note: You need an active internet connection to view the GeoIP map. The lab machine doesn't have an active internet connection!
```text
create an account in MaxMind then download country,city and asm(gzip) to use
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ mv GeoLite2-Country_20221007.tar.gz ../wireshark_op
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ cd ../wireshark_op
```
```text
┌──(kali㉿kali)-[~/wireshark_op]
└─$ ls
Exercise.pcapng        GeoLite2-ASN_20221007.tar.gz   GeoLite2-Country_20221007.tar.gz
GeoLite2-ASN_20221007  GeoLite2-City_20221007.tar.gz
```
```text
┌──(kali㉿kali)-[~/wireshark_op]
└─$ tar -xf GeoLite2-City_20221007.tar.gz
```
```text
┌──(kali㉿kali)-[~/wireshark_op]
└─$ tar -xf GeoLite2-Country_20221007.tar.gz
```
```text
┌──(kali㉿kali)-[~/wireshark_op]
└─$ ls
Exercise.pcapng               GeoLite2-City_20221007         GeoLite2-Country_20221007.tar.gz
GeoLite2-ASN_20221007         GeoLite2-City_20221007.tar.gz
GeoLite2-ASN_20221007.tar.gz  GeoLite2-Country_20221007
```
```text
┌──(kali㉿kali)-[~/wireshark_op]
└─$ cd GeoLite2-City_20221007
```
```text
┌──(kali㉿kali)-[~/wireshark_op/GeoLite2-City_20221007]
└─$ ls
COPYRIGHT.txt  GeoLite2-City.mmdb  LICENSE.txt  README.txt
```
```text
┌──(kali㉿kali)-[~/wireshark_op/GeoLite2-City_20221007]
└─$ cd ..
```
```text
┌──(kali㉿kali)-[~/wireshark_op]
└─$ ls
Exercise.pcapng               GeoLite2-City_20221007         GeoLite2-Country_20221007.tar.gz
GeoLite2-ASN_20221007         GeoLite2-City_20221007.tar.gz
GeoLite2-ASN_20221007.tar.gz  GeoLite2-Country_20221007
```
```text
┌──(kali㉿kali)-[~/wireshark_op]
└─$ cd GeoLite2-Country_20221007
```
```text
┌──(kali㉿kali)-[~/wireshark_op/GeoLite2-Country_20221007]
└─$ ls
COPYRIGHT.txt  GeoLite2-Country.mmdb  LICENSE.txt

doesn't appear nothing 😔
```
![[Pasted image 20221009191510.png]]
Investigate the resolved addresses. What is the IP address of the hostname starts with "bbc"?
"Resolved Addresses" can help.
*199.232.24.81*
![[Pasted image 20221009203248.png]]
What is the number of IPv4 conversations?
"Conversations" can help.
*435*
![[Pasted image 20221009203420.png]]
How many bytes (k) were transferred from the "Micro-St" MAC address?
"Endpoints" and "Name Resolution" can help.
*7474*
![[Pasted image 20221009203546.png]]
What is the number of IP addresses linked with "Kansas City"?
"Endpoints" can help.
*4*
![[Pasted image 20221009203710.png]]
Which IP address is linked with "Blicnet" AS Organisation?
"Endpoints" can help.
*188.246.82.7*
![[Pasted image 20221009203925.png]]
![[Pasted image 20221009203943.png]]
### Statistics | Protocol Details
IPv4 and IPv6
Up to here, almost all options provided information that contained both versions of the IP addresses. The statistics menu has two options for narrowing the statistics on packets containing a specific IP version. Thus, analysts can identify and list all events linked to specific IP versions in a single window and use it for the event of interest. You can use the "Statistics --> IPvX Statistics" menu to view this info.
DNS
This option breaks down all DNS packets from the capture file and helps analysts view the findings in a tree view based on packet counters and percentages of the DNS protocol. Thus analysts can view the DNS service's overall usage, including rcode, opcode, class, query type, service and query stats and use it for the event of interest. You can use the "Statistics --> DNS" menu to view this info.
HTTP
This option breaks down all HTTP packets from the capture file and helps analysts view the findings in a tree view based on packet counters and percentages of the HTTP protocol. Thus analysts can view the HTTP service's overall usage, including request and response codes and the original requests. You can use the "Statistics --> HTTP" menu to view this info.
What is the most used IPv4 destination address?
"IPv4 Statistics" can help.
*10.100.1.33*
![[Pasted image 20221009222354.png]]
What is the max service request-response time of the DNS packets?
"DNS Statistics" can help.
*0.467897*
![[Pasted image 20221009222858.png]]
What is the number of HTTP Requests accomplished by "rad[.]msn[.]com?
"HTTP Statistics" can help.
24+15
*39*
![[Pasted image 20221009223326.png]]
### Packet Filtering | Principles
Packet Filtering
In the previous room (Wireshark | The Basics), we covered packet filtering and how to filter packets without using queries. In this room, we will use queries to filter packets. As mentioned earlier, there are two types of filters in Wireshark. While both use similar syntax, they are used for different purposes. Let's remember the difference between these two categories.
Capture Filters
This type of filter is used to save only a specific part of the traffic. It is set before capturing traffic and not changeable during the capture.
Display Filters
This type of filter is used to investigate packets by reducing the number of visible packets, and it is changeable during the capture.
Note: You cannot use the display filter expressions for capturing traffic and vice versa.
The typical use case is capturing everything and filtering the packets according to the event of interest. Only experienced professionals use capture filters and sniff traffic. This is why Wireshark supports more protocol types in display filters. Please ensure you thoroughly learn how to use capture filters before using them in a live environment. Remember, you cannot capture the event of interest if your capture filter is not matching the specific traffic pattern you are looking for.
Capture Filter Syntax
These filters use byte offsets hex values and masks with boolean operators, and it is not easy to understand/predict the filter's purpose at first glance. The base syntax is explained below:
Scope: host, net, port and portrange.
Direction: src, dst, src or dst, src and dst,
Protocol: ether, wlan, ip, ip6, arp, rarp, tcp and udp.
Sample filter to capture port 80 traffic: tcp port 80
You can read more on capture filter syntax from [here](https://www.wireshark.org/docs/man-pages/pcap-filter.html) and [here](https://gitlab.com/wireshark/wireshark/-/wikis/CaptureFilters#useful-filters). A quick reference is available under the "Capture --> Capture Filters" menu.
Display Filter Syntax
This is Wireshark's most powerful feature. It supports 3000 protocols and allows conducting packet-level searches under the protocol breakdown. The official "[Display Filter Reference](https://www.wireshark.org/docs/dfref/)" provides all supported protocols breakdown for filtering.
Sample filter to capture port 80 traffic: tcp.port == 80
Wireshark has a built-in option (Display Filter Expression) that stores all supported protocol structures to help analysts create display filters. We will cover the "Display Filter Expression" menu later. Now let's understand the fundamentals of the display filter operations. A quick reference is available under the "Analyse --> Display Filters" menu.
Comparison Operators
You can create display filters by using different comparison operators to find the event of interest. The primary operators are shown in the table below.
English	C-Like	Description	Example
eq	==	Equal
ip.src == 10.10.10.100
ne	!=	Not equal
ip.src != 10.10.10.100
gt	>	Greater than
ip.ttl > 250
lt	<	Less Than
ip.ttl < 10
ge	>=	Greater than or equal to
ip.ttl >= 0xFA
le	<=	Less than or equal to
ip.ttl <= 0xA
Note: Wireshark supports decimal and hexadecimal values in filtering. You can use any format you want according to the search you will conduct.
Logical Expressions
Wireshark supports boolean syntax. You can create display filters by using logical operators as well.
English  	C-Like	Description  	Example
and	&&	Logical AND
(ip.src == 10.10.10.100) AND (ip.src == 10.10.10.111)
or	||	Logical OR
(ip.src == 10.10.10.100) OR (ip.src == 10.10.10.111)
not	!	Logical NOT
!(ip.src == 10.10.10.222)
Note: Usage of !=value is deprecated; using it could provide inconsistent results. Using the !(value) style is suggested for more consistent results.
Packet Filter Toolbar
The filter toolbar is where you create and apply your display filters. It is a smart toolbar that helps you create valid display filters with ease. Before starting to filter packets, here are a few tips:
Packet filters are defined in lowercase.
Packet filters have an autocomplete feature to break down protocol details, and each detail is represented by a "dot".
Packet filters have a three-colour representation explained below.
Green	Valid filter
Red	Invalid filter
