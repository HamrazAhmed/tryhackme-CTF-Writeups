---
Learn the basics of Wireshark and how to analyze various protocols and PCAPs
---

# Wireshark 101 — Writeup

## Overview
### Wireshark 101 — Writeup
### Wireshark 101 — Writeup
### Introduction
Wireshark, a tool used for creating and analyzing PCAPs (network packet capture files), is commonly used as one of the best packet analysis tools. In this room, we will look at the basics of installing Wireshark and using it to perform basic packet analysis and take a deep look at each common networking protocol.
![](https://assets.tryhackme.com/additional/wireshark101/1.png)
PCAPs used in this room have been sourced from the Wireshark Sample Captures Page as well as captures from various members of the TryHackMe community. All credit goes to the respective owners.
_Before completing this room we recommend completing the '[Introductory Networking](https://tryhackme.com/module/network-fundamentals)'. If you have a general knowledge of networking basics then you will be ready to begin._
### Installation
The installation for Wireshark is very easy and typically comes with a packaged GUI wizard. Luckily if you're using Kali Linux (or the TryHackMe AttackBox) then it is already installed on your machine. Wireshark can run on Windows, macOS, and Linux. To begin installing Wireshark on a Windows or macOS device you will need to first grab an installer from the [Wireshark website](https://www.wireshark.org/download.html). Once you have downloaded an installer, simply run it and follow the GUI wizard.
If you are using Linux you can install Wireshark with _apt install wireshark_ or a similar package manager.
![](https://assets.tryhackme.com/additional/wireshark101/2.png)
_Note: Wireshark can come with other packages and tools; you can decide whether or not you want to install them along with Wireshark._
For more information about Wireshark check out the [Wireshark Documentation](https://www.wireshark.org/docs/).
The first screen that we are greeted by when opening Wireshark is the main page that will allow us to specify our interface(s) as well as apply filters to narrow down traffic that we are capturing.
![](https://assets.tryhackme.com/additional/wireshark101/3.png)
Here you can see that I have multiple interfaces to filter from you may have more or fewer interfaces than I have. From here we can choose whether we want to perform a live capture on our interface(s) or load a PCAP for analysis.
It is useful to note that the graphs next to the interface names show the activity on the interface, if an interface has a flat bar it may be useless to attempt to capture on it (_as no data on that interface is being picked up by the Wireshark client)_.
Live Packet Captures
If we begin by navigating to the green ribbon in Wireshark and select Manage Capture Filters we can view a list of available filters.
![](https://assets.tryhackme.com/additional/wireshark101/4.png)
You do not have to select a filter, it will only help to bring down the number of packets being brought in and organize the capture. This is only a brief introduction to filters for more information about filters go to Task 12 or go to the [Wireshark Website](https://wiki.wireshark.org/CaptureFilters).
Once you have any capture filters you want selected, you can begin a capture on an interface by double-clicking the interface or by right-clicking and navigating to Start Capture.
Depending on the network activity you may see no packets coming in or you may see packets streaming in very quickly.
Once you're done gathering the packets you need or want, you can click the red square to stop capturing, and then you can begin your analysis.
![](https://assets.tryhackme.com/additional/wireshark101/5.png)
Looking at the screenshot above we see a sample capture. This screen is where you will do most of your analysis and dissection of packets. To open a packet capture go to File > Open > and select what PCAP you want to analyze.
From this screen, Wireshark gives us some important info about each packet including:
-   Packet Number
-   Time
-   Source
-   Destination
-   Protocol
-   Length
-   Packet Info
Along with quick packet information, Wireshark also color codes packets in order of danger level as well as protocol to be able to quickly spot anomalies and protocols in captures.
![](https://assets.tryhackme.com/additional/wireshark101/6.png)
This quick glance at packet information can be useful to track down exactly what you're looking for during analysis.
Play around with the menus and various features of Wireshark to get a feel for it, some of the features we will be going into further detail within later tasks.
### Collection Methods
﻿Before going into detail about how to analyze each protocol in a PCAP we need to understand the ways to gather a PCAP file. The basic steps to gather a PCAP in Wireshark itself can be simple however bringing into traffic can both the hard part as well as the fun part, this can include: taps, port mirroring, MAC floods, ARP Poisoning. This room will not cover how to set up these various strategies of live packet capturing and will only cover the basic theory of each.
Collection Methods Overview
Some things to think about before going headfirst into attempting to collect and monitor live packet captures.
-   Begin by starting with a sample capture to ensure that everything is correctly set up and you are successfully capturing traffic.
-   Ensure that you have enough compute power to handle the number of packets based on the size of the network, this will obviously vary network by network.
-   Ensure enough disk space to store all of the packet captures.
Once you meet all these criteria and have a collection method picked out you can begin to actively monitor and collect packets on a network.
Network Taps
Network taps are a physical implant in which you physically tap between a cable, these techniques are commonly used by Threat Hunting/DFIR teams and red teams in an engagement to sniff and capture packets.
There are two primary means of tapping a wire. The first is by using hardware to tap the wire and intercept the traffic as it comes across, an example of this would be a vampire tap as pictured below.
![](https://assets.tryhackme.com/additional/wireshark101/7.gif)
Another option for planting a network tap would be an inline network tap, which you would plant between or 'inline' two network devices. The tap will replicate packets as they pass the tap. An example of this tap would be the very common Throwing Star LAN Tap
![](https://assets.tryhackme.com/additional/wireshark101/8.jpg)
MAC Floods
MAC Floods are a tactic commonly used by red teams as a way of actively sniffing packets. MAC Flooding is intended to stress the switch and fill the CAM table. Once the CAM table is filled the switch will no longer accept new MAC addresses and so in order to keep the network alive, the switch will send out packets to all ports of the switch.
_Note: This technique should be used with extreme caution and with explicit prior consent._
ARP Poisoning
ARP Poisoning is another technique used by red teams to actively sniff packets. By ARP Poisoning you can redirect the traffic from the host(s) to the machine you're monitoring from. This technique will not stress network equipment like MAC Flooding however should still be used with caution and only if other techniques like network taps are unavailable.
Combining these methods with your previous knowledge of capturing traffic from the previous task will allow you to proactively monitor and collect live packet captures from scratch.
### Filtering Captures
Packet Filtering is a very important part of packet analysis especially when you have a very large number of packet sometimes even 100,000 plus. In task 3 capture filters were briefly covered however there is a second type of filter that is often thought of as more powerful and easier to use. This second method is known as display filters, you can apply display filters in two ways: through the analyze tab and at the filter bar at the top of the packet capture.
Filtering Operators
Wireshark's filter syntax can be simple to understand making it easy to get a hold of quickly. To get the most out of these filters you need to have a basic understanding of boolean and logic operators.
Wireshark only has a few that you will need to be familiar with:
-   and - operator: and / &&
-   or - operator: or / ||
-   equals - operator: eq / ==
-   not equal - operator: ne / !=
-   greater than - operator: gt /  >
-   less than - operator: lt / <
Wireshark also has a few other operators that go beyond the power of normal logical operators. These operators are the contains, matches, and bitwise_and operators. These operators can be very useful when you have a large capture and need to pinpoint a single packet. They are out of scope for this room however I recommend doing your own research, the [Wireshark Filtering Documentation](https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html) can be a great starting point.
Basic Filtering
Filtering gives us a very large scope of what we can do with the packets, because of this there can be a lot of different filtering syntax options. We will only be covering the very basics in this room such as filtering by IP, protocol, etc. for more information on filtering check out the [Wireshark filtering documentation](https://wiki.wireshark.org/DisplayFilters).
There is a general syntax to the filter commands however they can be a little silly at times. The basic syntax of Wireshark filters is some kind of service or protocol like ip or tcp, followed by a dot then whatever is being filtered for example an address, MAC, SRC, protocol, etc.
Filtering by IP: The first filter we will look at is ip.addr, this filter will allow you to comb through the traffic and only see packets with a specific IP address contained in those packets, whether it be from the source or destination.
Syntax: `ip.addr == <IP Address>`
![](https://assets.tryhackme.com/additional/wireshark101/9.png)
This filter can be handy in practical applications, say when you are threat hunting, and have identified a potentially suspicious host with other tools, you can use Wireshark to further analyze the packets coming from that device.
Filtering by SRC and DST: The second filter will look at is two in one as well as a filter operator: ip.src and ip.dst. These filters allow us to filter the traffic by the source and destination from which the traffic is coming from.
Syntax: `ip.src == <SRC IP Address> and ip.dst == <DST IP Address>`
![](https://assets.tryhackme.com/additional/wireshark101/10.png)
Similar to the first filter we can see that Wireshark is combing through the packets and filtering based on the source and destination we set.
Filtering by TCP Protocols: The last filter that we will be covering is the protocol filter, this allows you to set a port or protocol to filter by and can be handy when trying to keep track of an unusual protocol or port being used.
It is worthwhile to mention that Wireshark can filter by both port numbers as well as protocol names.
Syntax: `tcp.port eq <Port #> or <Protocol Name>`
![](https://assets.tryhackme.com/additional/wireshark101/11.png)
Filtering by UDP Protocols: You can also filter by UDP ports by changing the prefix from tcp to udp
Syntax: `udp.port eq <Port #> or <Protocol Name>`
That is the end of filtering for this task however I recommend you play around with other filters and operators on your own. Once you're ready move on to Task 5.
### Packet Dissection
This section covers how Wireshark uses OSI layers to break down packets and how to use these layers for analysis. It is expected that you already have background knowledge of what the OSI model is and how it works.
![](https://assets.tryhackme.com/additional/wireshark101/12.png)
Raza, M., 2018. 7 Layers Of The OSI Model
Packet Details
You can double click on a packet in capture to open its details. Packets consist of 5 to 7 layers based on the OSI model. We will go over all of them in an HTTP packet from a sample capture.
![](https://assets.tryhackme.com/additional/wireshark101/13.png)
Looking above we can see 7 distinct layers to the packet: frame/packet, source [MAC], source [IP], protocol, protocol errors, application protocol, and application data. Below we will go over the layers in more detail.
-   Frame (Layer 1) -- This will show you what frame / packet you are looking at as well as details specific to the Physical layer of the OSI model.
![](https://assets.tryhackme.com/additional/wireshark101/14.png)
-   Source [MAC] (Layer 2) -- This will show you the source and destination MAC Addresses; from the Data Link layer of the OSI model.
![](https://assets.tryhackme.com/additional/wireshark101/15.png)
-   Source [IP] (Layer 3) -- This will show you the source and destination IPv4 Addresses; from the Network layer of the OSI model.
![](https://assets.tryhackme.com/additional/wireshark101/16.png)
-   Protocol (Layer 4) -- This will show you details of the protocol used (UDP/TCP) along with source and destination ports; from the Transport layer of the OSI model.
![](https://assets.tryhackme.com/additional/wireshark101/17.png)
-   Protocol Errors -- This is a continuation of the 4th layer showing specific segments from TCP that needed to be reassembled.
![](https://assets.tryhackme.com/additional/wireshark101/18.png)
-   Application Protocol (Layer 5) -- This will show details specific to the protocol being used such HTTP, FTP, SMB, etc. From the Application layer of the OSI model.
![](https://assets.tryhackme.com/additional/wireshark101/19.png)
-   Application Data -- This is an extension of layer 5 that can show the application-specific data.
![](https://assets.tryhackme.com/additional/wireshark101/20.png)
Now that we understand what a general packet is composed of, move on to looking at various application protocols and their specific details.
### ARP Traffic
ARP Overview
ARP or Address Resolution Protocol is a Layer 2 protocol that is used to connect IP Addresses with MAC Addresses. They will contain REQUEST messages and RESPONSE messages. To identify packets the message header will contain one of two operation codes:
-   Request (1)
-   Reply (2)
Below you can see a packet capture of multiple ARP requests and replies.
![](https://assets.tryhackme.com/additional/wireshark101/21.png)
It is useful to note that most devices will identify themselves or Wireshark will identify it such as Intel_78, an example of suspicious traffic would be many requests from an unrecognized source. You need to enable a setting within Wireshark however to resolve physical addresses. To enable this feature, navigate to View > Name Resolution > Ensure that Resolve Physical Addresses is checked.
Looking at the below screenshot we can see that a Cisco device is sending ARP Requests, meaning that we should be able to trust this device, however you should always stay on the side of caution when analyzing packets.
![](https://assets.tryhackme.com/additional/wireshark101/22.png)
ARP Traffic Overview
ARP Request Packets:
We can begin analyzing packets by looking at the first ARP Request packet and looking at the packet details.
![](https://assets.tryhackme.com/additional/wireshark101/23.png)
Looking at the packet details above, the most important details of the packet are outlined in red. The Opcode is short for operation code and will you tell you whether it is an ARP Request or Reply. The second outlined detail is to where the packet is requesting to, in this case, it is broadcasting the request to all.
ARP Reply Packets:
![](https://assets.tryhackme.com/additional/wireshark101/24.png)
Looking at the above packet details we can see from the Opcode that it is an ARP Reply packet. We can also get other useful information like the MAC and IP Address that was sent along with the reply since this is a reply packet we know that this was the information sent along with the message.
ARP is one of the simpler protocols to analyze, all you need to remember is to identify whether it is a request or reply packet and who it is being sent by.
Practical ARP Packet Analysis
Now that you know what ARP packets and normal traffic look, let's dive into an exercise. Start the AttackBox, and go to the folder /root/Rooms/Wireshark101 and double click the task7.pcap file to open it in Wireshark; you can also download the provided PCAP on the task.
This capture has multiple protocols so you may need to use your knowledge of filtering from previous tasks; once you're ready, begin analysis of the capture.
What is the Opcode for Packet 6?
*Request (1)*
What is the source MAC Address of Packet 19?
*80:fb:06:f0:45:d7*
What 4 packets are Reply packets?
*76,400,459,520*
What IP Address is at 80:fb:06:f0:45:d7?
*10.251.23.1*
### ICMP Traffic
ICMP Overview
ICMP or Internet Control Message Protocol is used to analyze various nodes on a network. This is most commonly used with utilities like ping and traceroute. You should already be familiar with how ICMP works; however, if you need a refresher, read the [IETF documentation](https://tools.ietf.org/html/rfc792).
Below you can see a sample of what a ping would look like, we can see a request to the server from ICMP, then a reply from the server.
![](https://assets.tryhackme.com/additional/wireshark101/icmp/1.png)
ICMP Traffic Overview
ICMP request:
Below we see packet details for a ping request packet. There are a few important things within the packet details that we can take note of first being the type and code of the packet. A type that equals 8 means that it is a request packet, if it is equal to 0 it is a reply packet. When these codes are altered or do not seem correct that is typically a sign of suspicious activity.
There are two other details within the packet that are useful to analyze: timestamp and data. The timestamp can be useful for identifying the time the ping was requested it can also be useful to identify suspicious activity in some cases. We can also look at the data string which will typically just be a random data string.
![](https://assets.tryhackme.com/additional/wireshark101/icmp/2.png)
ICMP Reply:
Below you can see that the reply packet is very similar to the request packet. One of the main difference that distinguishes a reply packet is the code, in this case, you can see it is 0, confirming that it is a reply packet.
The same analysis techniques for Request packets apply here as well, again the main difference will be the packet type.
![](https://assets.tryhackme.com/additional/wireshark101/icmp/3.png)
Practical ICMP Packet Analysis
Now that you understand how an ICMP packet is formed and what it contains, we can begin hands-on practical analysis of ICMP packets. Go to the folder /root/Rooms/Wireshark101 on the AttackBox and double click the task8.pcap file to open it in Wireshark; you can also download the pcap on this task.
This network capture only has two protocols so it is up to you whether or not you decide to filter the ICMP protocol or not.
