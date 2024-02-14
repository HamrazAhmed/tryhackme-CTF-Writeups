---
Learn advanced techniques such as null, FIN, Xmas, and idle (zombie) scans, spoofing, in addition to FW and IDS evasion.
---

# Nmap Advanced Port Scans — Writeup

## Enumeration
![](https://assets.tryhackme.com/room-banners/netsecmodule.png)
### Introduction
This room is the third in the Nmap series (part of the Introduction to Network Security module). In the first two rooms, we learned about live host discovery and basic port scans.
Nmap Live Host Discovery
Nmap Basic Port Scans
Nmap Advanced Port Scans
Nmap Post Port Scans
In Nmap Basic Port Scans, we covered TCP flags and reviewed the TCP 3-way handshake. To initiate a connection, TCP requires the first packet to have the SYN flag set. Consequently, we can tell if a TCP port is open based on the response we receive.
Security researchers and hackers contemplated the TCP flags, shown in the figure below and explained in the previous room, and started to experiment. They wanted to know what would happen if we send a TCP packet, which is not part of any ongoing TCP connection, with one or more flags set.
For instance, an ACK flag is set when you want to acknowledge received data. An ACK scan is like trying to acknowledge data that was neither sent nor received in the first place. Consider this simple analogy, someone coming to you out of nowhere to tell you, “yes, I hear you, please continue.” when you haven’t said anything.
This room explains advanced types of scans and scan options. Some of these scan types can be useful against specific systems, while others are useful in particular network setups. We will cover the following types of port scans:
Null Scan
FIN Scan
Xmas Scan
Maimon Scan
ACK Scan
Window Scan
Custom Scan
Moreover, we will cover the following:
Spoofing IP
Spoofing MAC
Decoy Scan
Fragmented Packets
Idle/Zombie Scan
We will discuss options and techniques to evade firewalls and IDS systems. We also cover options to get more verbose details from Nmap.
Launch the AttackBox by using the Start AttackBox button and get ready to experiment with different types of Nmap scans against different virtual machines.
*No answer needed*
Let’s start with the following three types of scans:
Null Scan
FIN Scan
Xmas Scan
Null Scan
The null scan does not set any flag; all six flag bits are set to zero. You can choose this scan using the -sN option. A TCP packet with no flags set will not trigger any response when it reaches an open port, as shown in the figure below. Therefore, from Nmap’s perspective, a lack of reply in a null scan indicates that either the port is open or a firewall is blocking the packet.
However, we expect the target server to respond with an RST packet if the port is closed. Consequently, we can use the lack of RST response to figure out the ports that are not closed: open or filtered.
Below is an example of a null scan against a Linux server. The null scan we carried out has successfully identified the six open ports on the target system. Because the null scan relies on the lack of a response to infer that the port is not closed, it cannot indicate with certainty that these ports are open; there is a possibility that the ports are not responding due to a firewall rule.
Pentester Terminal
pentester@TryHackMe$ sudo nmap -sN 10.10.235.172
Starting Nmap 7.60 ( https://nmap.org ) at 2021-08-30 10:30 BST
Nmap scan report for 10.10.235.172
Host is up (0.00066s latency).
Not shown: 994 closed ports
PORT    STATE         SERVICE
22/tcp  open|filtered ssh
25/tcp  open|filtered smtp
80/tcp  open|filtered http
110/tcp open|filtered pop3
111/tcp open|filtered rpcbind
143/tcp open|filtered imap
MAC Address: 02:45:BF:8A:2D:6B (Unknown)
Nmap done: 1 IP address (1 host up) scanned in 96.50 seconds
Note that many Nmap options require root privileges. Unless you are running Nmap as root, you need to use sudo as in the example above using the -sN option.
FIN Scan
The FIN scan sends a TCP packet with the FIN flag set. You can choose this scan type using the -sF option. Similarly, no response will be sent if the TCP port is open. Again, Nmap cannot be sure if the port is open or if a firewall is blocking the traffic related to this TCP port.
However, the target system should respond with an RST if the port is closed. Consequently, we will be able to know which ports are closed and use this knowledge to infer the ports that are open or filtered. It's worth noting some firewalls will 'silently' drop the traffic without sending an RST.
Below is an example of a FIN scan against a Linux server. The result is quite similar to the result we obtained earlier using a null scan.
Pentester Terminal
pentester@TryHackMe$ sudo nmap -sF 10.10.235.172
Starting Nmap 7.60 ( https://nmap.org ) at 2021-08-30 10:32 BST
Nmap scan report for 10.10.235.172
Host is up (0.0018s latency).
Not shown: 994 closed ports
PORT    STATE         SERVICE
22/tcp  open|filtered ssh
25/tcp  open|filtered smtp
80/tcp  open|filtered http
110/tcp open|filtered pop3
111/tcp open|filtered rpcbind
143/tcp open|filtered imap
MAC Address: 02:45:BF:8A:2D:6B (Unknown)
Nmap done: 1 IP address (1 host up) scanned in 96.52 seconds
Xmas Scan
The Xmas scan gets its name after Christmas tree lights. An Xmas scan sets the FIN, PSH, and URG flags simultaneously. You can select Xmas scan with the option -sX.
Like the Null scan and FIN scan, if an RST packet is received, it means that the port is closed. Otherwise, it will be reported as open|filtered.
The following two figures show the case when the TCP port is open and the case when the TCP port is closed.
The console output below shows an example of a Xmas scan against a Linux server. The obtained results are pretty similar to that of the null scan and the FIN scan.
Pentester Terminal
pentester@TryHackMe$ sudo nmap -sX 10.10.235.172
Starting Nmap 7.60 ( https://nmap.org ) at 2021-08-30 10:34 BST
Nmap scan report for 10.10.235.172
Host is up (0.00087s latency).
Not shown: 994 closed ports
PORT    STATE         SERVICE
22/tcp  open|filtered ssh
25/tcp  open|filtered smtp
80/tcp  open|filtered http
110/tcp open|filtered pop3
111/tcp open|filtered rpcbind
143/tcp open|filtered imap
MAC Address: 02:45:BF:8A:2D:6B (Unknown)
Nmap done: 1 IP address (1 host up) scanned in 84.85 seconds
On scenario where these three scan types can be efficient is when scanning a target behind a stateless (non-stateful) firewall. A stateless firewall will check if the incoming packet has the SYN flag set to detect a connection attempt. Using a flag combination that does not match the SYN packet makes it possible to deceive the firewall and reach the system behind it. However, a stateful firewall will practically block all such crafted packets and render this kind of scan useless.
```text
┌──(kali㉿kali)-[~]
└─$ sudo nmap -sF 10.10.106.254
Starting Nmap 7.92 ( https://nmap.org ) at 2022-08-30 16:50 EDT
Nmap scan report for 10.10.106.254
Host is up (0.20s latency).
Not shown: 993 closed tcp ports (reset)
PORT    STATE         SERVICE
22/tcp  open|filtered ssh
25/tcp  open|filtered smtp
53/tcp  open|filtered domain
80/tcp  open|filtered http
110/tcp open|filtered pop3
111/tcp open|filtered rpcbind
143/tcp open|filtered imap

Nmap done: 1 IP address (1 host up) scanned in 14.80 seconds
```
```text
┌──(kali㉿kali)-[~]
└─$ sudo nmap -sN 10.10.106.254
Starting Nmap 7.92 ( https://nmap.org ) at 2022-08-30 16:52 EDT
Nmap scan report for 10.10.106.254
Host is up (0.20s latency).
Not shown: 993 closed tcp ports (reset)
PORT    STATE         SERVICE
22/tcp  open|filtered ssh
25/tcp  open|filtered smtp
53/tcp  open|filtered domain
80/tcp  open|filtered http
110/tcp open|filtered pop3
111/tcp open|filtered rpcbind
143/tcp open|filtered imap

Nmap done: 1 IP address (1 host up) scanned in 9.93 seconds
```
```text
┌──(kali㉿kali)-[~]
└─$ sudo nmap -sX 10.10.106.254
Starting Nmap 7.92 ( https://nmap.org ) at 2022-08-30 16:53 EDT
Nmap scan report for 10.10.106.254
Host is up (0.20s latency).
Not shown: 993 closed tcp ports (reset)
PORT    STATE         SERVICE
22/tcp  open|filtered ssh
25/tcp  open|filtered smtp
53/tcp  open|filtered domain
80/tcp  open|filtered http
110/tcp open|filtered pop3
111/tcp open|filtered rpcbind
143/tcp open|filtered imap

Nmap done: 1 IP address (1 host up) scanned in 12.22 seconds
```
In a null scan, how many flags are set to 1?
*0*
In a FIN scan, how many flags are set to 1? *1*
In a Xmas scan, how many flags are set to 1? *3*
Start the VM and load the AttackBox. Once both are ready, open the terminal on the AttackBox and use nmap to launch a FIN scan against the target VM. How many ports appear as open|filtered? *7*
Repeat your scan launching a null scan against the target VM. How many ports appear as open|filtered? *7*
Uriel Maimon first described this scan in 1996. In this scan, the FIN and ACK bits are set. The target should send an RST packet as a response. However, certain BSD-derived systems drop the packet if it is an open port exposing the open ports. This scan won’t work on most targets encountered in modern networks; however, we include it in this room to better understand the port scanning mechanism and the hacking mindset. To select this scan type, use the -sM option.
Most target systems respond with an RST packet regardless of whether the TCP port is open. In such a case, we won’t be able to discover the open ports. The figure below shows the expected behaviour in the cases of both open and closed TCP ports.
The console output below is an example of a TCP Maimon scan against a Linux server. As mentioned, because open ports and closed ports are behaving the same way, the Maimon scan could not discover any open ports on the target system.
Pentester Terminal
pentester@TryHackMe$ sudo nmap -sM 10.10.252.27
Starting Nmap 7.60 ( https://nmap.org ) at 2021-08-30 10:36 BST
Nmap scan report for ip-10-10-252-27.eu-west-1.compute.internal (10.10.252.27)
Host is up (0.00095s latency).
All 1000 scanned ports on ip-10-10-252-27.eu-west-1.compute.internal (10.10.252.27) are closed
MAC Address: 02:45:BF:8A:2D:6B (Unknown)
Nmap done: 1 IP address (1 host up) scanned in 1.61 seconds
This type of scan is not the first scan one would pick to discover a system; however, it is important to know about it as you don’t know when it could come in handy.
In the Maimon scan, how many flags are set?
*2*
This task will cover how to perform a TCP ACK scan, a TCP window scan, and how to create your custom flag scan.
TCP ACK Scan
Let’s start with the TCP ACK scan. As the name implies, an ACK scan will send a TCP packet with the ACK flag set. Use the -sA option to choose this scan. As we show in the figure below, the target would respond to the ACK with RST regardless of the state of the port. This behaviour happens because a TCP packet with the ACK flag set should be sent only in response to a received TCP packet to acknowledge the receipt of some data, unlike our case. Hence, this scan won’t tell us whether the target port is open in a simple setup.
In the following example, we scanned the target VM before installing a firewall on it. As expected, we couldn’t learn which ports were open.
Pentester Terminal
pentester@TryHackMe$ sudo nmap -sA 10.10.159.225
Starting Nmap 7.60 ( https://nmap.org ) at 2021-08-30 10:37 BST
Nmap scan report for 10.10.159.225
Host is up (0.0013s latency).
All 1000 scanned ports on MACHINE_IP are unfiltered
MAC Address: 02:45:BF:8A:2D:6B (Unknown)
Nmap done: 1 IP address (1 host up) scanned in 1.68 seconds
This kind of scan would be helpful if there is a firewall in front of the target. Consequently, based on which ACK packets resulted in responses, you will learn which ports were not blocked by the firewall. In other words, this type of scan is more suitable to discover firewall rule sets and configuration.
After setting up the target VM 10.10.159.225 with a firewall, we repeated the ACK scan. This time, we received some interesting results. As seen in the console output below, we have three ports that aren't being blocked by the firewall. This result indicates that the firewall is blocking all other ports except for these three ports.
Pentester Terminal
pentester@TryHackMe$ sudo nmap -sA 10.10.159.225
Starting Nmap 7.60 ( https://nmap.org ) at 2021-09-07 11:34 BST
Nmap scan report for 10.10.159.225
Host is up (0.00046s latency).
Not shown: 997 filtered ports
PORT    STATE      SERVICE
22/tcp  unfiltered ssh
25/tcp  unfiltered smtp
80/tcp  unfiltered http
MAC Address: 02:78:C0:D0:4E:E9 (Unknown)
Nmap done: 1 IP address (1 host up) scanned in 15.45 seconds
Window Scan
Another similar scan is the TCP window scan. The TCP window scan is almost the same as the ACK scan; however, it examines the TCP Window field of the RST packets returned. On specific systems, this can reveal that the port is open. You can select this scan type with the option -sW. As shown in the figure below, we expect to get an RST packet in reply to our “uninvited” ACK packets, regardless of whether the port is open or closed.
Similarly, launching a TCP window scan against a Linux system with no firewall will not provide much information. As we can see in the console output below, the results of the window scan against a Linux server with no firewall didn’t give any extra information compared to the ACK scan executed earlier.
Pentester Terminal
pentester@TryHackMe$ sudo nmap -sW 10.10.159.225
Starting Nmap 7.60 ( https://nmap.org ) at 2021-08-30 10:38 BST
Nmap scan report for 10.10.159.225
Host is up (0.0011s latency).
All 1000 scanned ports on ip-10-10-252-27.eu-west-1.compute.internal (10.10.252.27) are closed
MAC Address: 02:45:BF:8A:2D:6B (Unknown)
Nmap done: 1 IP address (1 host up) scanned in 1.60 seconds
However, as you would expect, if we repeat our TCP window scan against a server behind a firewall, we expect to get more satisfying results. In the console output shown below, the TCP window scan pointed that three ports are detected as closed. (This is in contrast with the ACK scan that labelled the same three ports as unfiltered.) Although we know that these three ports are not closed, we realize they responded differently, indicating that the firewall does not block them.
Pentester Terminal
pentester@TryHackMe$ sudo nmap -sW 10.10.159.225
Starting Nmap 7.60 ( https://nmap.org ) at 2021-09-07 11:39 BST
Nmap scan report for 10.10.159.225
Host is up (0.00040s latency).
Not shown: 997 filtered ports
PORT    STATE  SERVICE
22/tcp  closed ssh
25/tcp  closed smtp
80/tcp  closed http
MAC Address: 02:78:C0:D0:4E:E9 (Unknown)
Nmap done: 1 IP address (1 host up) scanned in 14.84 seconds
Custom Scan
If you want to experiment with a new TCP flag combination beyond the built-in TCP scan types, you can do so using --scanflags. For instance, if you want to set SYN, RST, and FIN simultaneously, you can do so using --scanflags RSTSYNFIN. As shown in the figure below, if you develop your custom scan, you need to know how the different ports will behave to interpret the results in different scenarios correctly.
Finally, it is essential to note that the ACK scan and the window scan were very efficient at helping us map out the firewall rules. However, it is vital to remember that just because a firewall is not blocking a specific port, it does not necessarily mean that a service is listening on that port. For example, there is a possibility that the firewall rules need to be updated to reflect recent service changes. Hence, ACK and window scans are exposing the firewall rules, not the services.
```text
┌──(kali㉿kali)-[~]
└─$ sudo nmap -sA 10.10.159.225
[sudo] password for kali: 
Starting Nmap 7.92 ( https://nmap.org ) at 2022-08-30 17:33 EDT
Nmap scan report for 10.10.159.225
Host is up (0.20s latency).
Not shown: 981 filtered tcp ports (no-response), 15 filtered tcp ports (host-prohibited)
PORT    STATE      SERVICE
22/tcp  unfiltered ssh
25/tcp  unfiltered smtp
80/tcp  unfiltered http
443/tcp unfiltered https

Nmap done: 1 IP address (1 host up) scanned in 10.93 seconds
```
In TCP Window scan, how many flags are set?
*1*
You decided to experiment with a custom TCP scan that has the reset flag set. What would you add after --scanflags?  *rst* (The reset flag is RST)
The VM received an update to its firewall ruleset. A new port is now allowed by the firewall. After you make sure that you have terminated the VM from Task 2, start the VM for this task. Launch the AttackBox if you haven't done that already. Once both are ready, open the terminal on the AttackBox and use Nmap to launch an ACK scan against the target VM. How many ports appear unfiltered? *4*
What is the new port number that appeared? *443*
Is there any service behind the newly discovered port number? (Y/N) *N* (http://10.10.159.225:443/)
