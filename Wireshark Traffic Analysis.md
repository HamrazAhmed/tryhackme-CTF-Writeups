---
Learn the basics of traffic analysis with Wireshark and how to find anomalies on your network!
---

# Wireshark Traffic Analysis — Writeup

## Overview
### Wireshark Traffic Analysis — Writeup
### Wireshark Traffic Analysis — Writeup
### Introduction
In this room, we will cover the techniques and key points of traffic analysis with Wireshark and detect suspicious activities. Note that this is the third and last room of the Wireshark room trio, and it is suggested to visit the first two rooms stated below to practice and refresh your Wireshark skills before starting this one.
Wireshark: The Basics
Wireshark: Packet Operations
In the first two rooms, we have covered how to use Wireshark and do packet-level searches. Now, it is time to investigate and correlate the packet-level information to see the big picture in the network traffic, like detecting anomalies and malicious activities. For a security analyst, it is vital to stop and understand pieces of information spread in packets by applying the analyst's knowledge and tool functionality. This room will cover investigating packet-level details by synthesising the analyst knowledge and  Wireshark functionality for detecting anomalies and odd situations for a given case.
Note: A VM is attached to this room. You don't need SSH or RDP; the room provides a "Split View" feature. DO NOT directly interact with any domains and IP addresses in this room. The domains and IP addresses are included only for reference reasons.

## Enumeration
Nmap Scans
Nmap is an industry-standard tool for mapping networks, identifying live hosts and discovering the services. As it is one of the most used network scanner tools, a security analyst should identify the network patterns created with it. This section will cover identifying the most common Nmap scan types.
Transmission Control Protocol (TCP) is a connection-oriented protocol requiring a TCP three-way-handshake to establish a connection. TCP provides reliable data transfer, flow control and congestion control. Higher-level protocols such as HTTP, POP3, IMAP and SMTP use TCP
User Datagram Protocol (UDP) is a connectionless protocol; UDP does not require a connection to be established. UDP is suitable for protocols that rely on fast queries, such as DNS, and for protocols that prioritise real-time communications, such as audio/video conferencing and broadcast.
-   TCP connect scans
-   SYN scans
-   UDP scans
It is essential to know how Nmap scans work to spot scan activity on the network. However, it is impossible to understand the scan details without using the correct filters. Below are the base filters to probe Nmap scan behaviour on the network.
**TCP flags in a nutshell.**
**Notes**
**Wireshark Filters**
Global search.
-   `tcp`
-   `udp`
-   Only SYN flag.
-   SYN flag is set. The rest of the bits are not important.
-   `tcp.flags == 2`
-   `tcp.flags.syn == 1`
-   Only ACK flag.
-   ACK flag is set. The rest of the bits are not important.
-   `tcp.flags == 16`
-   `tcp.flags.ack == 1`
-   Only SYN, ACK flags.
-   SYN and ACK are set. The rest of the bits are not important.
-   `tcp.flags == 18`
-   `(tcp.flags.syn == 1) and (tcp.flags.ack == 1)`
-   Only RST flag.
-   RST flag is set. The rest of the bits are not important.
-   `tcp.flags == 4`
-   `tcp.flags.reset == 1`
-   Only RST, ACK flags.
-   RST and ACK are set. The rest of the bits are not important.
-   `tcp.flags == 20`
-   `(tcp.flags.reset == 1) and (tcp.flags.ack == 1)`
-   Only FIN flag
-   FIN flag is set. The rest of the bits are not important.
-   `tcp.flags == 1`
-   `tcp.flags.fin == 1`
TCP Connect Scans
**TCP Connect Scan in a nutshell:**
-   Relies on the three-way handshake (needs to finish the handshake process).
-   Usually conducted with `nmap -sT` command.
-   Used by non-privileged users (only option for a non-root user).
-   Usually has a windows size larger than 1024 bytes as the request expects some data due to the nature of the protocol.
**Open TCP Port**
**Open TCP Port
**
**Closed TCP Port**
-   SYN -->
-   <-- SYN, ACK
-   ACK -->
-   SYN -->
-   <-- SYN, ACK
-   ACK -->
-   RST, ACK -->
-   SYN -->
-   <-- RST, ACK
The images below show the three-way handshake process of the open and close TCP ports. Images and pcap samples are split to make the investigation easier and understand each case's details.
**Open TCP port (Connect):**
**Closed TCP port (Connect):**
The above images provide the patterns in isolated traffic. However, it is not always easy to spot the given patterns in big capture files. Therefore analysts need to use a generic filter to view the initial anomaly patterns, and then it will be easier to focus on a specific traffic point. The given filter shows the TCP Connect scan patterns in a capture file.
`tcp.flags.syn==1 and tcp.flags.ack==0 and tcp.window_size > 1024`
**SYN Scans**
TCP SYN Scan in a nutshell:
-   Doesn't rely on the three-way handshake (no need to finish the handshake process).
-   Usually conducted with `nmap -sS` command.
-   Used by privileged users.
-   Usually have a size less than or equal to 1024 bytes as the request is not finished and it doesn't expect to receive data.
**Open TCP Port**
**Close TCP Port**
-   SYN -->
-   <-- SYN,ACK
-   RST-->
-   SYN -->
-   <-- RST,ACK
**Open TCP port (SYN):**
**Closed TCP port (SYN):**
The given filter shows the TCP SYN scan patterns in a capture file.
`tcp.flags.syn==1 and tcp.flags.ack==0 and tcp.window_size <= 1024`
UDP Scans
UDP Scan in a nutshell:
-   Doesn't require a handshake process
-   No prompt for open ports
-   ICMP error message for close ports
-   Usually conducted with `nmap -sU` command.
Open UDP Port
Closed UDP Port
-   UDP packet -->
-   UDP packet -->
-   ICMP Type 3, Code 3 message. (Destination unreachable, port unreachable)
**Closed (port no 69) and open (port no 68) UDP ports:**
The above image shows that the closed port returns an ICMP error packet. No further information is provided about the error at first glance, so how can an analyst decide where this error message belongs? The ICMP error message uses the original request as encapsulated data to show the source/reason of the packet. Once you expand the ICMP section in the packet details pane, you will see the encapsulated data and the original request, as shown in the below image.
The given filter shows the UDP scan patterns in a capture file.
`icmp.type==3 and icmp.code==3`
Detecting suspicious activities in chunked files is easy and a great way to learn how to focus on the details. Now use the exercise files to put your skills into practice against a single capture file and answer the questions below!
Use the "Desktop/exercise-pcaps/nmap/Exercise.pcapng" file.What is the total number of the "TCP Connect" scans?
![[Pasted image 20221211182759.png]]
*1000*
Which scan type is used to scan the TCP port 80?
*TCP Connect*
How many "UDP close port" messages are there?
![[Pasted image 20221211183823.png]]
*1083*
Which UDP port in the 55-70 port range is open?
Remember, half of the traffic analysis is done by hand when using Wireshark. Filter the traffic as shown in the task, then filter the destination port (UDP) with the "filter a column" option. Finally, scroll the bar in the packet list section and investigate the findings manually. --Because doesn't apper like destination unreacheable, finding manually
udp.dstport==68
![[Pasted image 20221211184338.png]]
*68*
### ARP Poisoning & Man In The Middle!
Address Resolution Protocol (ARP) is responsible for finding the MAC (hardware) address related to a specific IP address. It works by broadcasting an ARP query, "Who has this IP address? Tell me." And the response is of the form, "The IP address is at this MAC address."
ARP Poisoning/Spoofing (A.K.A. Man In The Middle Attack)
**ARP** protocol, or **A**ddress **R**esolution **P**rotocol (**ARP**), is the technology responsible for allowing devices to identify themselves on a network. Address Resolution Protocol Poisoning (also known as ARP Spoofing or Man In The Middle (MITM) attack) is a type of attack that involves network jamming/manipulating by sending malicious ARP packets to the default gateway. The ultimate aim is to manipulate the **"IP to MAC address table"** and sniff the traffic of the target host.
There are a variety of tools available to conduct ARP attacks. However, the mindset of the attack is static, so it is easy to detect such an attack by knowing the ARP protocol workflow and Wireshark skills.
**ARP analysis in a nutshell:**
-   Works on the local network
-   Enables the communication between MAC addresses
-   Not a secure protocol
-   Not a routable protocol
-   It doesn't have an authentication function
-   Common patterns are request & response, announcement and gratuitous packets.
Before investigating the traffic, let's review some legitimate and suspicious ARP packets. The legitimate requests are similar to the shown picture: a broadcast request that asks if any of the available hosts use an IP address and a reply from the host that uses the particular IP address.
**Notes**
**Wireshark filter**
Global search
-   `arp`
"ARP" options for grabbing the low-hanging fruits:
-   Opcode 1: ARP requests.
-   Opcode 2: ARP responses.
-   **Hunt:** Arp scanning
-   **Hunt:** Possible ARP poisoning detection
-   **Hunt:** Possible ARP flooding from detection:
-   `arp.opcode == 1`
-   `arp.opcode == 2`
-   `arp.dst.hw_mac==00:00:00:00:00:00`
-   `arp.duplicate-address-detected or arp.duplicate-address-frame`
-   `((arp) && (arp.opcode == 1)) && (arp.src.hw_mac == target-mac-address)`
A suspicious situation means having two different ARP responses (conflict) for a particular IP address. In that case, Wireshark's expert info tab warns the analyst. However, it only shows the second occurrence of the duplicate value to highlight the conflict. Therefore, identifying the malicious packet from the legitimate one is the analyst's challenge. A possible IP spoofing case is shown in the picture below.
Here, knowing the network architecture and inspecting the traffic for a specific time frame can help detect the anomaly. As an analyst, you should take notes of your findings before going further. This will help you be organised and make it easier to correlate the further findings. Look at the given picture; there is a conflict; the MAC address that ends with "b4" crafted an ARP request with the "192.168.1.25" IP address, then claimed to have the "192.168.1.1" IP address.
**Notes**
Detection Notes
**Findings**
Possible IP address match.
1 IP address announced from a MAC address.
-   MAC: 00:0c:29:e2:18:b4
-   IP: 192.168.1.25
Possible ARP spoofing attempt.
2 MAC addresses claimed the same IP address (192.168.1.1).
The " 192.168.1.1" IP address is a possible gateway address.
-   MAC1: 50:78:b3:f3:cd:f4
-   MAC 2: 00:0c:29:e2:18:b4
Possible ARP flooding attempt.
The MAC address that ends with "b4" claims to have a different/new IP address.
-   MAC: 00:0c:29:e2:18:b4
-   IP: 192.168.1.1
Let's keep inspecting the traffic to spot any other anomalies. Note that the case is split into multiple capture files to make the investigation easier.
At this point, it is evident that there is an anomaly. A security analyst cannot ignore a flood of ARP requests. This could be malicious activity, scan or network problems. There is a new anomaly; the MAC address that ends with "b4" crafted multiple ARP requests with the "192.168.1.25" IP address. Let's focus on the source of this anomaly and extend the taken notes.
Notes
Detection Notes
Findings
Possible IP address match.
1 IP address announced from a MAC address.
-   MAC: 00:0c:29:e2:18:b4
-   IP: 192.168.1.25
Possible ARP spoofing attempt.
2 MAC addresses claimed the same IP address (192.168.1.1).
The " 192.168.1.1" IP address is a possible gateway address.
-   MAC1: 50:78:b3:f3:cd:f4
-   MAC 2: 00:0c:29:e2:18:b4
Possible ARP spoofing attempt.
The MAC address that ends with "b4" claims to have a different/new IP address.
-   MAC: 00:0c:29:e2:18:b4
-   IP: 192.168.1.1
Possible ARP flooding attempt.
The MAC address that ends with "b4" crafted multiple ARP requests against a range of IP addresses.
-   MAC: 00:0c:29:e2:18:b4
-   IP: 192.168.1.xxx
Up to this point, it is evident that the MAC address that ends with "b4" owns the "192.168.1.25" IP address and crafted suspicious ARP requests against a range of IP addresses. It also claimed to have the possible gateway address as well. Let's focus on other protocols and spot the reflection of this anomaly in the following sections of the time frame.
There is HTTP traffic, and everything looks normal at the IP level, so there is no linked information with our previous findings. Let's add the MAC addresses as columns in the packet list pane to reveal the communication behind the IP addresses.
One more anomaly! The MAC address that ends with "b4" is the destination of all HTTP packets! It is evident that there is a MITM attack, and the attacker is the host with the MAC address that ends with "b4". All traffic linked to "192.168.1.12" IP addresses is forwarded to the malicious host. Let's summarise the findings before concluding the investigation.
Detection Notes
Findings
IP to MAC matches.
3  IP to MAC address matches.
-   MAC: 00:0c:29:e2:18:b4 = IP: 192.168.1.25
-   MAC: 50:78:b3:f3:cd:f4 = IP: 192.1681.1
-   MAC: 00:0c:29:98:c7:a8 = IP: 192.168.1.12
Attacker
The attacker created noise with ARP packets.
-   MAC: 00:0c:29:e2:18:b4 = IP: 192.168.1.25
Router/gateway
Gateway address.
-   MAC: 50:78:b3:f3:cd:f4 = IP: 192.1681.1
Victim
The attacker sniffed all traffic of the victim.
-   MAC: 50:78:b3:f3:cd:f4 = IP: 192.1681.12
Detecting these bits and pieces of information in a big capture file is challenging. However, in real-life cases, you will not have "tailored data" ready for investigation. Therefore you need to have the analyst mindset, knowledge and tool skills to filter and detect the anomalies.
**Note:** In traffic analysis, there are always alternative solutions available. The solution type and the approach depend on the analyst's knowledge and skill level and the available data sources.
Detecting suspicious activities in chunked files is easy and a great way to learn how to focus on the details. Now use the exercise files to put your skills into practice against a single capture file and answer the questions below!
Use the "Desktop/exercise-pcaps/arp/Exercise.pcapng" file.
What is the number of ARP requests crafted by the attacker?
![[Pasted image 20221211200214.png]]
eth.src == 00:0c:29:e2:18:b4 and arp.opcode == 1
![[Pasted image 20221211200245.png]]
*284*
What is the number of HTTP packets received by the attacker?
eth.dst == 00:0c:29:e2:18:b4 and http
![[Pasted image 20221211200434.png]]
*90*
What is the number of sniffed username&password entries?
Filter the site visited by the victim, then filter the post requests. Focusing on URI sections of the packet details after filtering could help.
http.request.full_uri == "http://testphp.vulnweb.com/userinfo.php"
not uname and pass (2) so 8 -2 = 6
![[Pasted image 20221211200945.png]]
![[Pasted image 20221211201037.png]]
*6*
What is the password of the "Client986"?
Special characters are displayed in HEX format. Make sure that you convert them to ASCII.
*clientnothere!*
What is the comment provided by the "Client354"?
Special characters are displayed in HEX format. Make sure that you convert them to ASCII.
apply as filter:
http.host == "testphp.vulnweb.com"
![[Pasted image 20221211201324.png]]
*Nice work!*
### Identifying Hosts: DHCP, NetBIOS and Kerberos
Identifying Hosts
When investigating a compromise or malware infection activity, a security analyst should know how to identify the hosts on the network apart from IP to MAC address match. One of the best methods is identifying the hosts and users on the network to decide the investigation's starting point and list the hosts and users associated with the malicious traffic/activity.
Usually, enterprise networks use a predefined pattern to name users and hosts. While this makes knowing and following the inventory easier, it has good and bad sides. The good side is that it will be easy to identify a user or host by looking at the name. The bad side is that it will be easy to clone that pattern and live in the enterprise network for adversaries. There are multiple solutions to avoid these kinds of activities, but for a security analyst, it is still essential to have host and user identification skills.
Protocols that can be used in Host and User identification:
-   Dynamic Host Configuration Protocol (DHCP) traffic
-   NetBIOS (NBNS) traffic
-   Kerberos traffic
**DHCP Analysis**
**DHCP** protocol, or **D**ynamic **H**ost **C**onfiguration **P**rotocol **(DHCP)****,** is the technology responsible for managing automatic IP address and required communication parameters assignment.
**DHCP investigation in a nutshell:**
**Notes**
**Wireshark Filter**
Global search.
-   `dhcp` or `bootp`
Filtering the proper DHCP packet options is vital to finding an event of interest.
-   **"DHCP Request"** packets contain the hostname information
-   **"DHCP ACK"** packets represent the accepted requests
-   **"DHCP NAK"** packets represent denied requests
Due to the nature of the protocol, only "Option 53" ( request type) has predefined static values. You should filter the packet type first, and then you can filter the rest of the options by "applying as column" or use the advanced filters like "contains" and "matches".
-   Request: `dhcp.option.dhcp == 3`
-   ACK: `dhcp.option.dhcp == 5`
-   NAK: `dhcp.option.dhcp == 6`
**"DHCP Request"** options for grabbing the low-hanging fruits:
-   **Option 12:** Hostname.
-   **Option 50:** Requested IP address.
-   **Option 51:** Requested IP lease time.
-   **Option 61:** Client's MAC address.
-   `dhcp.option.hostname contains "keyword"`
**"DHCP ACK"** options for grabbing the low-hanging fruits:
-   **Option 15:** Domain name.
-   **Option 51:** Assigned IP lease time.
-   `dhcp.option.domain_name contains "keyword"`
**"DHCP NAK"** options for grabbing the low-hanging fruits:
-   **Option 56:** Message (rejection details/reason).
As the message could be unique according to the case/situation, It is suggested to read the message instead of filtering it. Thus, the analyst could create a more reliable hypothesis/result by understanding the event circumstances.
NetBIOS (NBNS) Analysis
BIOS (**basic input/output system**) is the program a computer's microprocessor uses to start the computer system after it is powered on. It also manages data flow between the computer's operating system (OS) and attached devices, such as the hard disk, video adapter, keyboard, mouse and printer.
**NetBIOS** or **Net**work **B**asic **I**nput/**O**utput **S**ystem is the technology responsible for allowing applications on different hosts to communicate with each other.
**NBNS investigation in a nutshell:**
**Notes**
**Wireshark Filter**
Global search.
-   `nbns`
"NBNS" options for grabbing the low-hanging fruits:
-   **Queries:** Query details.
-   Query details could contain **"name, Time to live (TTL) and IP address details"**
-   `nbns.name contains "keyword"`
Kerberos Analysis
**Kerberos** is the default authentication service for Microsoft Windows domains. It is responsible for authenticating service requests between two or more computers over the untrusted network. The ultimate aim is to prove identity securely.
**Kerberos investigation in a nutshell:**
**Notes**
**Wireshark Filter**
Global search.
-   `kerberos`
User account search:
-   **CNameString:** The username.
**Note:** Some packets could provide hostname information in this field. To avoid this confusion, filter the **"$"** value. The values end with **"$"** are hostnames, and the ones without it are user names.
-   `kerberos.CNameString contains "keyword"`
-   `kerberos.CNameString and !(kerberos.CNameString contains "$" )`
"Kerberos" options for grabbing the low-hanging fruits:
-   **pvno:** Protocol version.
-   **realm:** Domain name for the generated ticket.
-   **sname:** Service and domain name for the generated ticket.
-   **addresses:** Client IP address and NetBIOS name.
**Note:** the "addresses" information is only available in request packets.
-   `kerberos.pvno == 5`
-   `kerberos.realm contains ".org"`
-   `kerberos.SNameString == "krbtg"`
Detecting suspicious activities in chunked files is easy and a great way to learn how to focus on the details. Now use the exercise files to put your skills into practice against a single capture file and answer the questions below!
Use the "Desktop/exercise-pcaps/dhcp-netbios-kerberos/dhcp-netbios.pcap" file.
What is the MAC address of the host "Galaxy A30"?
Filtering a pattern rather than actual value can help.
dhcp.option.hostname contains "Galaxy"
![[Pasted image 20221211214119.png]]
*9a:81:41:cb:96:6c*
How many NetBIOS registration requests does the "LIVALJM" workstation have?
"nbns.flags.opcode == 5" filter can help.
nbns.name contains "LIVALJM" and nbns.flags.opcode==5
![[Pasted image 20221211214402.png]]
*16*
Which host requested the IP address "172.16.13.85"?
dhcp.option.requested_ip_address == 172.16.13.85
![[Pasted image 20221211215441.png]]
*Galaxy-A12*
Use the "Desktop/exercise-pcaps/dhcp-netbios-kerberos/**kerberos.pcap" file.**
What is the IP address of the user "u5"? (Enter the address in defanged format.)
kerberos.CNameString contains "u5"
found ip 10.1.12.2 so defanging 10[.]1[.]12[.]2
![[Pasted image 20221211215703.png]]
*10[.]1[.]12[.]2*
What is the hostname of the available host in the Kerberos packets?
kerberos.CNameString
![[Pasted image 20221211220203.png]]
*xp1$*
### Tunneling Traffic: DNS and ICMP
Tunnelling Traffic: ICMP and DNS
Traffic tunnelling is (also known as **"port forwarding"**) transferring the data/resources in a secure method to network segments and zones. It can be used for "internet to private networks" and "private networks to internet" flow/direction. There is an encapsulation process to hide the data, so the transferred data appear natural for the case, but it contains private data packets and transfers them to the final destination securely.
Tunnelling provides anonymity and traffic security. Therefore it is highly used by enterprise networks. However, as it gives a significant level of data encryption, attackers use tunnelling to bypass security perimeters using the standard and trusted protocols used in everyday traffic like ICMP and DNS. Therefore, for a security analyst, it is crucial to have the ability to spot ICMP and DNS anomalies.
ICMP Analysis
Internet Control Message Protocol (ICMP) is designed for diagnosing and reporting network communication issues. It is highly used in error reporting and testing. As it is a trusted network layer protocol, sometimes it is used for denial of service (DoS) attacks; also, adversaries use it in data exfiltration and C2 tunnelling activities.
ICMP analysis in a nutshell:
Usually, ICMP tunnelling attacks are anomalies appearing/starting after a malware execution or vulnerability exploitation. As the ICMP packets can transfer an additional data payload, adversaries use this section to exfiltrate data and establish a C2 connection. It could be a TCP, HTTP or SSH data. As the ICMP protocols provide a great opportunity to carry extra data, it also has disadvantages. Most enterprise networks block custom packets or require administrator privileges to create custom ICMP packets.
A large volume of ICMP traffic or anomalous packet sizes are indicators of ICMP tunnelling. Still, the adversaries could create custom packets that match the regular ICMP packet size (64 bytes), so it is still cumbersome to detect these tunnelling activities. However, a security analyst should know the normal and the abnormal to spot the possible anomaly and escalate it for further analysis.
**Notes**
**Wireshark filters**
Global search
-   `icmp`
"ICMP" options for grabbing the low-hanging fruits:
-   Packet length.
-   ICMP destination addresses.
-   Encapsulated protocol signs in ICMP payload.
-   `data.len > 64 and icmp`
DNS Analysis
Domain Name System (DNS) is designed to translate/convert IP domain addresses to IP addresses. It is also known as a phonebook of the internet. As it is the essential part of web services, it is commonly used and trusted, and therefore often ignored. Due to that, adversaries use it in data exfiltration and C2 activities.
**DNS analysis in a nutshell:
**
Similar to ICMP tunnels, DNS attacks are anomalies appearing/starting after a malware execution or vulnerability exploitation. Adversary creates (or already has) a domain address and configures it as a C2 channel. The malware or the commands executed after exploitation sends DNS queries to the C2 server. However, these queries are longer than default DNS queries and crafted for subdomain addresses. Unfortunately, these subdomain addresses are not actual addresses; they are encoded commands as shown below:
**"encoded-commands.maliciousdomain.com"**
When this query is routed to the C2 server, the server sends the actual malicious commands to the host. As the DNS queries are a natural part of the networking activity, these packets have the chance of not being detected by network perimeters. A security analyst should know how to investigate the DNS packet lengths and target addresses to spot these anomalies.
**Notes**
**Wireshark Filter**
Global search
-   `dns`
"DNS" options for grabbing the low-hanging fruits:
-   Query length.
-   Anomalous and non-regular names in DNS addresses.
-   Long DNS addresses with encoded subdomain addresses.
-   Known patterns like dnscat and dns2tcp.
-   Statistical analysis like the anomalous volume of DNS requests for a particular target.
**!mdns:** Disable local link device queries.
Detecting suspicious activities in chunked files is easy and a great way to learn how to focus on the details. Now use the exercise files to put your skills into practice against a single capture file and answer the questions below!
Use the "Desktop/exercise-pcaps/dns-icmp/icmp-tunnel.pcap" file.
Investigate the anomalous packets. Which protocol is used in ICMP tunnelling?
1) Remember, Wireshark is not an IDS/IPS tool. A security analyst should know how to filter the packets and investigate the results manually. 2) Filtering anomalous packets and investigating the packet details (including payload data) could help.
data.len > 64 and icmp
look data and see ssh .. i.e length 878
![[Pasted image 20221211225232.png]]
*ssh*
Use the "Desktop/exercise-pcaps/dns-icmp/dns.pcap" file.
Investigate the anomalous packets. What is the suspicious main domain address that receives anomalous DNS queries? (Enter the address in defanged format.)
After filtering the packets, focus on the payload data in the packet bytes section. You might need to use the tool in full-screen mode/full-screen the VM.
dns.qry.name.len > 15 and !mdns
![[Pasted image 20221211225910.png]]
*dataexfil[.]com*
### Cleartext Protocol Analysis: FTP
Cleartext Protocol Analysis
Investigating cleartext protocol traces sounds easy, but when the time comes to investigate a big network trace for incident analysis and response, the game changes. Proper analysis is more than following the stream and reading the cleartext data. For a security analyst, it is important to create statistics and key results from the investigation process. As mentioned earlier at the beginning of the Wireshark room series, the analyst should have the required network knowledge and tool skills to accomplish this. Let's simulate a cleartext protocol investigation with Wireshark!
FTP Analysis
File Transfer Protocol (FTP) is designed to transfer files with ease, so it focuses on simplicity rather than security. As a result of this, using this protocol in unsecured environments could create security issues like:
-   MITM attacks
-   Credential stealing and unauthorised access
-   Phishing
-   Malware planting
-   Data exfiltration
**FTP analysis in a nutshell:**
**Notes**
**Wireshark Filter**
Global search
-   `ftp`
**"FTP"** options for grabbing the low-hanging fruits:
-   **x1x series:** Information request responses.
-   **x2x series:** Connection messages.
-   **x3x series:** Authentication messages.
**Note:** "200" means command successful.
**---**
"x1x" series options for grabbing the low-hanging fruits:
