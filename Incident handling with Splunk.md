---
Learn to use Splunk for incident handling through interactive scenarios.
---

# Incident handling with Splunk — Writeup

## Overview
### Incident handling with Splunk — Writeup
### Introduction: Incident Handling
This room covers an incident Handling scenario using Splunk. An incident from a security perspective is "Any event or action, that has a negative consequence on the security of a user/computer or an organization is considered a security incident." Below are a few of the events that would negatively affect the environment when they occurred:
-   Crashing the system
-   Execution of an unwanted program
-   Access to sensitive information from an unauthorized user
-   A Website being defaced by the attacker
-   The use of USB devices when there is a restriction in usage is against the company's policy
**Learning Objective**
-   Learn how to leverage OSINT sites during an investigation
-   How to map Attacker's activities to Cyber Kill Chain Phases
-   How to utilize effective Splunk searches to investigate logs
-   Understand the importance of host-centric and network-centric log sources
**Room Prerequisites**
Before going through this room, it is expected that the participants will have a basic understanding of Splunk. If not, consider going through this room, Splunk 101 ([https://tryhackme.com/jr/splunk101](https://tryhackme.com/jr/splunk101)).
It is good to understand the following before completing this lesson:
-   Splunk overview and basic navigation
-   Important Splunk Queries
-   Know how to use different functions/values to craft a search query
-   How to look for interesting fields
Website defacements are the **unauthorized modification of web pages, including the addition, removal, or alteration of existing content**. These attacks are commonly carried out by hacktivists, who compromise a website or web server and replace or alter the hosted website information with their own messages.
### Incident Handling - Life Cycle
**Incident Handling Life Cycle**
As an Incident Handler / SOC Analyst, we would aim to know the attackers' tactics, techniques, and procedures. Then we can stop/defend/prevent against the attack in a better way. The Incident Handling process is divided into four different phases. Let's briefly go through each phase before jumping into the incident, which we will be going through in this exercise.
**1. Preparation**
The preparation phase covers the readiness of an organization against an attack. That means documenting the requirements, defining the policies, incorporating the security controls to monitor like EDR / SIEM / IDS / IPS, etc. It also includes hiring/training the staff.
**2. Detection and Analysis**
The detection phase covers everything related to detecting an incident and the analysis process of the incident. This phase covers getting alerts from the security controls like SIEM/EDR investigating the alert to find the root cause. This phase also covers hunting for the unknown threat within the organization.
**3. Containment, Eradication, and Recovery**
This phase covers the actions needed to prevent the incident from spreading and securing the network. It involves steps taken to avoid an attack from spreading into the network, isolating the infected host, clearing the network from the infection traces, and gaining control back from the attack.
**4. Post-Incident Activity / Lessons Learnt**
This phase includes identifying the loopholes in the organization's security posture, which led to an intrusion, and improving so that the attack does not happen next time. The steps involve identifying weaknesses that led to the attack, adding detection rules so that similar breach does not happen again, and most importantly, training the staff if required.
### Incident Handling: Scenario
In this exercise, we will investigate a cyber attack in which the attacker defaced an organization's website. This organization has Splunk as a SIEM solution setup. Our task as a Security Analysis would be to investigate this cyber attack and map the attacker's activities into all 7 of the Cyber Kill Chain Phases. It is important to note that we don't need to follow the sequence of the cyber kill chain during the Investigation. One finding in one phase will lead to another finding that may have mapped into some other phase.
### Incident handling with Splunk — Writeup
We will follow the Cyber kill Chain Model and map the attacker's activity in each phase during this Investigation. When required, we will also utilize Open Source Intelligence (OSINT) and other findings to fill the gaps in the kill chain. It is not necessary to follow this sequence of the phases while investigating.
-   Reconnaissance
-   Weaponization
-   Delivery
-   Exploitation
-   Installation
-   Command & Control
-   Actions on Objectives
**Scenario**
A Big corporate organization **Wayne Enterprises** has recently faced a cyber-attack where the attackers broke into their network, found their way to their web server, and have successfully defaced their website **http://www.imreallynotbatman.com**. Their website is now showing the trademark of the attackers with the message **YOUR SITE HAS BEEN DEFACED** as shown below.
They have requested "**US**" to join them as a **Security Analyst** and help them investigate this cyber attack and find the root cause and all the attackers' activities within their network.
The good thing is, that they have Splunk already in place, so we have got all the event logs related to the attacker's activities captured. We need to explore the records and find how the attack got into their network and what actions they performed.
This Investigation comes under the `Detection and Analysis phase.`
**Splunk**
During our investigation, we will be using `Splunk` as our SIEM solution. Logs are being ingested from webserver/firewall/Suricata/Sysmon etc. In the data summary tab, we can explore the log sources showing visibility into both network-centric and host-centric activities. To get the complete picture of the hosts and log sources being monitored in Wayne Enterprise, please click on the **Data summary** and navigate the available tabs to get the information.
**Interesting log Sources**
Some of the interesting log sources that will help us in our Investigation are:
**Log Sources**
**Details**
**wineventlog**
It contains Windows Event logs
**winRegistry**
It contains the logs related to registry creation / modification / deletion etc.
**XmlWinEventLog**
It contains the sysmon event logs. It is a very important log source from an investigation point of view.
**fortigate_utm
**
It contains Fortinet Firewall logs
**iis
**
It contains IIS web server logs
**Nessus:scan
**
It contains the results from the Nessus vulnerability scanner.
**Suricata
**
It contains the details of the alerts from the Suricata IDS.   This log source shows which alert was triggered and what caused the alert to get triggered— a very important log source for the Investigation.
**stream:http
**
It contains the network flow related to http traffic.
**stream: DNS
**
It contains the network flow related to DNS traffic.
**stream:icmp
**
It contains the network flow related to icmp traffic.
**Note:** All the event logs that we are going to investigate are present in `index=botsv1`
Now that we know what hosts we have to investigate, what sources and the source types are, **let's connect to the lab and start Investigating**.
Room Machine
Before moving forward, deploy the machine. When you deploy the machine, it will be assigned an IP **Machine IP**: `MACHINE_IP`. The machine will take up to 3-5 minutes to start.
**Action on Objective**
As the website was defaced due to a successful attack by the adversary, it would be helpful to understand better what ended up on the website that caused defacement.
As an analyst, our first quest could be to figure out the traffic flow that could lead us to the answer to this question. There can be a different approach to finding the answer to this question. We will start our investigation by examining the **Suricata** log source and the IP addresses communicating with the webserver 192.168.250.70.
**Search Query**:`index=botsv1 dest=192.168.250.70 sourcetype=suricata`
The logs do not show any external IP communicating with the server. Let us change the flow direction to see if any communication originates from the server.
**Search Query:** `index=botsv1 src=192.168.250.70 sourcetype=suricata`
What is interesting about the output? Usually, the web servers do not originate the traffic. The browser or the client would be the source, and the server would be the destination. Here we see three external IPs towards which our web server initiates the outbound traffic. There is a large chunk of traffic going to these external IP addresses, which could be worth checking.
Pivot into the destination IPs one by one to see what kind of traffic/communication is being carried out.
**Search Query:** `index=botsv1 src=192.168.250.70 sourcetype=suricata dest_ip=23.22.63.114`
The URL field shows 2 PHP files and one jpeg file. This jpeg file looks interesting. Let us change the search query and see where this jpeg file came from.
**Search Query:** `index=botsv1 url="/poisonivy-is-coming-for-you-batman.jpeg" dest_ip="192.168.250.70" | table _time src dest_ip http.hostname url`
The end result clearly shows a suspicious jpeg `poisonivy-is-coming-for-you-batman.jpeg` was downloaded from the attacker's host `prankglassinebracket.jumpingcrab.com` that defaced the site.
Answer the questions below
What is the name of the file that defaced the imreallynotbatman.com website ?
*poisonivy-is-coming-for-you-batman.jpeg*
Fortigate Firewall 'fortigate_utm' detected SQL attempt from the attacker's IP 40.80.148.42. What is the name of the rule that was triggered during the SQL Injection attempt?
attack field
index=botsv1 src=40.80.148.42 sourcetype=fortigate_utm
![[Pasted image 20221214221614.png]]
*HTTP.URI.SQL.Injection*
### Command and Control Phase
The attacker uploaded the file to the server before defacing it. While doing so, the attacker used a Dynamic DNS to resolve a malicious IP. Our objective would be to find the IP that the attacker decided the DNS.
To investigate the communication to and from the adversary's IP addresses, we will be examining the network-centric log sources mentioned above. We will first pick fortigate_utm to review the firewall logs and then move on to the other log sources.
**Search Query:** `index=botsv1 sourcetype=fortigate_utm"poisonivy-is-coming-for-you-batman.jpeg"   `
Looking into the Fortinet firewall logs, we can see the src IP, destination IP, and URL. Look at the fields on the left panel and the field `url` contains the FQDN (Fully Qualified Domain Name).
Though we have found the answer, we can verify other log sources.
Let us verify the answer by looking at another log source.`stream:http`.
**Search Query:** `index=botsv1 sourcetype=stream:http dest_ip=23.22.63.114 "poisonivy-is-coming-for-you-batman.jpeg" src_ip=192.168.250.70`
We have identified the suspicious domain as a Command and Control Server, which the attacker contacted after gaining control of the server.
**Note:** We can also confirm the domain by looking at the last log source `stream:dns` to see what DNS queries were sent from the webserver during the infection period.
Answer the questions below
This attack used dynamic DNS to resolve to the malicious IP. What fully qualified domain name (FQDN) is associated with this attack?
*prankglassinebracket.jumpingcrab.com*
### Weaponization Phase
In the weaponization phase, the adversaries would:
-   Create Malware / Malicious document to gain initial access / evade detection etc.
-   Establish domains similar to the target domain to trick users.
-   Create a Command and Control Server for the post-exploitation communication/activity etc.
We have found some domains / IP addresses associated with the attacker during the investigations. This task will mainly look into OSINT sites to see what more information we can get about the adversary.
So far, we have found a domain `prankglassinebracket.jumpingcrab.com` associated with this attack. Our first task would be to find the IP address tied to the domains that may potentially be pre-staged to attack Wayne Enterprise.
In the following exercise, we will be searching the online Threat Intel sites for any information like IP addresses/domains / Email addresses associated with this domain which could help us know more about this adversary.
**Robtex:**
[Robtex](https://www.robtex.com/) is a Threat Intel site that provides information about IP addresses, domain names, etc.
Please search for the domain on the robtex site and see what we get. We will get the IP addresses associated with this domain.
Some domains/subdomains associated with this domain:
Reference**:** [https://www.robtex.com/dns-lookup/prankglassinebracket.jumpingcrab.com](https://www.robtex.com/dns-lookup/prankglassinebracket.jumpingcrab.com)
Next, search for the IP address `23.22.63.114`  on this Threat Intel site.
What did we find? this IP is associated with some domains that look pretty similar to **the WAYNE Enterprise** site.
Reference: [https://www.robtex.com/ip-lookup/23.22.63.114](https://www.robtex.com/ip-lookup/23.22.63.114)
**ThreatCrowd**:
[ThreatCrowd](https://www.threatcrowd.org/) is a Search Engine for Threats that provides intel based on the IP, domain, email address, etc.
We will use ThreatCrowd to find the relationship between IP addresses and domains. Let's look at the threatcrowd site to see if we can find some information regarding this IP.
Reference**:** [https://threatcrowd.org/ip.php?ip=23.22.63.114](https://threatcrowd.org/ip.php?ip=23.22.63.114)
See, we found multiple IPs domains associated with this particular IP, along with the email address `lillian.rose@po1s0nvy.com` that could potentially be associated with the adversary.
**Virustotal**
[Virustotal](https://www.virustotal.com/) is an OSINT site used to analyze suspicious files, domains, IP, etc. Let's now search for the IP address on the virustotal site. If we go to the **RELATIONS** tab, we can see all the domains associated with this IP which look similar to the Wayn Enterprise company.
In the domain list, we saw the domain that is associated with the attacker`www.po1s0n1vy.com` . Let us search for this domain on the virustotal.
We can also look for the whois information on this site -> [whois.domaintools.com](https://whois.domaintools.com/) to see if we can find something valuable.
Answer the questions below
What IP address has P01s0n1vy tied to domains that are pre-staged to attack Wayne Enterprises?
*23.22.63.114*
Based on the data gathered from this attack and common open-source intelligence sources for domain names, what is the email address that is most likely associated with the P01s0n1vy APT group?
*lillian.rose@po1s0nvy.com*
### Delivery Phase
Attackers create malware and infect devices to gain initial access or evade defenses and find ways to deliver it through different means. We have identified various IP addresses, domains and Email addresses associated with this adversary. Our task for this lesson would be to use the information we have about the adversary and use various Threat Hunting platforms and OSINT sites to find any malware linked with the adversary.
Threat Intel report suggested that this adversary group Poison lvy appears to have a secondary attack vector in case the `initial compromise` fails. Our objective would be to understand more about the attacker and their methodology and correlate the information found in the logs with various threat Intel sources.
**OSINT sites**
-   Virustotal
-   ThreatMiner
-   Hybrid-Analysis
**ThreatMiner**
Let's start our investigation by looking for the IP `23.22.63.114` on the Threat Intel site [ThreatMiner.](https://www.threatminer.org/host.php?q=23.22.63.114#gsc.tab=0&gsc.q=23.22.63.114&gsc.page=1)
We found three files associated with this IP, from which one file with the hash value  `c99131e0169171935c5ac32615ed6261` seems to be malicious and something of interest.
Now, click on this MD5 hash value to see the metadata and other important information about this particular file.
Reference: [https://www.threatminer.org/host.php?q=23.22.63.114#gsc.tab=0&gsc.q=23.22.63.114&gsc.page=1](https://www.threatminer.org/host.php?q=23.22.63.114#gsc.tab=0&gsc.q=23.22.63.114&gsc.page=1)[](https://www.threatminer.org/host.php?q=23.22.63.114#gsc.tab=0&gsc.q=23.22.63.114&gsc.page=1)
**Virustotal**
Open [virustotal.com](http://virustotal.com/) and search for the hash on the virustotal now. Here, we can get information about the metadata about this Malware in the Details tab.
Reference: [https://www.virustotal.com/gui/file/9709473ab351387aab9e816eff3910b9f28a7a70202e250ed46dba8f820f34a8/community](https://www.virustotal.com/gui/file/9709473ab351387aab9e816eff3910b9f28a7a70202e250ed46dba8f820f34a8/community)
**Hybrid-Analysis**
Hybrid Analysis is a beneficial site that shows the behavior Analysis of any malware. Here you can look at all the activities performed by this Malware after being executed. Some of the information that Hybrid-Analysis provides are:
-   Network Communication.
-   DNS Requests
-   Contacted Hosts with Country Mapping
-   Strings
-   MITRE ATT&CK Mapping
-   Malicious Indicators.
-   DLLs Imports / Exports
-   Mutex Information if created
-   File Metadata
-   Screenshots
Scroll down, and you will get a lot of information about this Malware.
Reference**:** [https://www.hybrid-analysis.com/sample/9709473ab351387aab9e816eff3910b9f28a7a70202e250ed46dba8f820f34a8?environmentId=100](https://www.hybrid-analysis.com/sample/9709473ab351387aab9e816eff3910b9f28a7a70202e250ed46dba8f820f34a8?environmentId=100)[](https://www.hybrid-analysis.com/sample/9709473ab351387aab9e816eff3910b9f28a7a70202e250ed46dba8f820f34a8?environmentId=100)
Answer the questions below
What is the HASH of the Malware associated with the APT group?
*c99131e0169171935c5ac32615ed6261*
What is the name of the Malware associated with the Poison Ivy Infrastructure?
*MirandaTateScreensaver.scr.exe*
53 74 65 76 65 20 42 72 61 6e 74 27 73 20 42 65 61 72 64 20 69 73 20 61 20 70 6f 77 65 72 66 75 6c 20 74 68 69 6e 67 2e 20 46 69 6e 64 20 74 68 69 73 20 6d 65 73 73 61 67 65 20 61 6e 64 20 61 73 6b 20 68 69 6d 20 74 6f 20 62 75 79 20 79 6f 75 20 61 20 62 65 65 72 21 21 21
Steve Brant's Beard is a powerful thing. Find this message and ask him to buy you a beer!!!
### Conclusion
**Conclusion:**
In this fun exercise, as a SOC Analyst, we have investigated a cyber-attack where the attacker had defaced a website 'imreallynotbatman.com' of the Wayne Enterprise. We mapped the attacker's activities into the 7 phases of the Cyber Kill Chain. Let us recap everything we have found so far:
**Reconnaissance Phase:**
We first looked at any reconnaissance activity from the attacker to identify the IP address and other details about the adversary.
**Findings:**
-   IP Address `40.80.148.42` was found to be scanning our webserver.
-   The attacker was using Acunetix as a web scanner.
**Exploitation Phase:**
We then looked into the traces of exploitation attempts and found brute-force attacks against our server, which were successful.
**Findings:**
-   Brute force attack originated from IP `23.22.63.114.`
-   The IP address used to gain access: `40.80.148.42`
-   142 unique brute force attempts were made against the server, out of which one attempt was successful
**Installation Phase:**
Next, we looked at the installation phase to see any executable from the attacker's IP Address uploaded to our server.
**Findings:**
-   A malicious executable file `3791.exe` was observed to be uploaded by the attacker.
-   We looked at the sysmon logs and found the MD5 hash of the file.
**Action on Objective:**
After compromising the web server, the attacker defaced the website.
**Findings:**
-   We examined the logs and found the file name used to deface the webserver.
**Weaponization Phase:**
We used various threat Intel platforms to find the attacker's infrastructure based on the following information we saw in the above activities.
Information we had:
Domain: `prankglassinebracket.jumpingcrab.com`
IP Address: `23.22.63.114`
**Findings:**
-   Multiple masquerading domains were found associated with the attacker's IPs.
