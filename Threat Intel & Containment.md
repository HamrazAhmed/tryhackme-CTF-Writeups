# Threat Intel & Containment — Writeup

## Overview
### Threat Intel & Containment — Writeup
### Threat Intel & Containment — Writeup
----
Learn what threat intelligence looks like, and some containment strategies used in the IR process.
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/ce3b9f1e249893691db11a600b99289d.png)
This room is going to introduce you to what containment involves, as well as some containment strategies. Additionally, this room is going to introduce what threat intelligence is and how it can be used to understand our adversary.
You will use some of the Indicators Of Attack (IOA) & Indicators Of Compromise (IOC) from the module in the practical element of this room to analyse some threat intelligence.
Containment is a crucial phase in incidence response because the core aim is to minimise the damage caused by an incident and prevent further damage. For example, we can prevent our adversary from accessing other devices by containing infected devices. - containment is a fantastic way to preserve and record evidence that can be used in forensic analysis.
Effective containment is essential in restoring normal operations. Once a threat has been successfully contained, normal day-to-day operations can continue.
Threat intelligence, briefly, is the knowledge gained from collecting and analyzing intelligence about a threat actor. Intelligence such as IP addresses can be used to identify a specific threat actor or, for example, analyse their tactics, techniques, and procedures (TTPs). More on this later.
Learning Objectives:
By the end of the room, you should be able to:
- Recognise potential threat intelligence.
- Analyse threat intelligence to understand how an adversary operates.
- Understand what containment involves and some of the approaches that can be taken with their pros and cons.
Room Pre-requisites
This room expects you to have:
- At least an understanding that the [ATT&CK framework](https://tryhackme.com/room/mitre) exists.
- Familiarity with IP addresses. I.e., knowing what an IP address (private and public) looks like.
- At least an awareness of adversary techniques, i.e. persistence, lateral movement, etc.
- Be capable of identifying what a hash looks like - I highly recommend checking out the Preparation room (coming soon!) that is a part of this module.
Answer the questions below
I've read the introductory task!
Completed
### Task 2  Pre-Containment
This stage of the process focuses on the steps necessary to prevent an incident from having further impact.
You will be looking to gather as much information as possible about the incident and the adversary.  For example, collecting evidence from infrastructure such as Intrusion Detection Systems (IDS) and [Security and Information Management Systems](https://tryhackme.com/room/introtosiem) (SIEMS).  This evidence will form Indicators of Compromise (IOCs).
We can begin looking at our perimeter defence systems for this information. For example, looking at our setup of ELK with [packetbeat](https://www.elastic.co/beats/packetbeat), we can see that a workstation has downloaded an executable. Perhaps a user has clicked on a malicious PDF?
With this information, we can identify the workstation that has potentially been compromised.  We can then further analyse this system to gather further evidence for containment. To illustrate, we can gather the hash of this downloaded file.
Getting the hash of the downloaded executable (Windows)
```powershell
PS C:\Users\MichaelAscot\Downloads> Get-FileHash dropper.exe

Algorithm       Hash                                                                   Path
---------       ----                                                                   ----
SHA256          84BDE632C5BFD2A7FF84E579E6F7561543CA0AAD6D8E7275DAE5926BA4F561C1       C:\Users\MichaelAscot\Downlo...
```
Getting the hash of the downloaded executable (Linux)
```shell-session
ubuntu@tryhackme:~$ sha256sum dropper.exe
84BDE632C5BFD2A7FF84E579E6F7561543CA0AAD6D8E7275DAE5926BA4F561C1  dropper.exe

https://www.virustotal.com/gui/file/84bde632c5bfd2a7ff84e579e6f7561543ca0aad6d8e7275dae5926ba4f561c1/community
```
With this evidence, we now know that any host with this file is presumed to be infected. We can start creating detection alerts for this file's presence or the attacker's IP address. For example, using a SIEM such as [Wazuh](https://tryhackme.com/room/wazuhct) to check for the presence of this file on any device.
Assembling threat intelligence like this is paramount to the pre-containment stage because it allows us to link activity to any previous campaigns or attribute new behaviours to a threat actor.
Answer the questions below
What does the acronym IDS mean?
*Intrusion Detection Systems*
### Task 3  Containment Strategies
There are a few containment strategies to consider when actioning the containment phase of the incidence response. It is important to consider what strategy is suitable as they all have their pros and cons.
Containment can be considered as the bridge between the identification, scoping and eradication, and recovery phases of the incidence response process.
Isolation
**Entire isolation** is considered to be a pretty aggressive - but effective - strategy. This strategy involves the incidence response team completely isolating the infected device(s). This can be through network segmentation or physical.
As previously stated, this is pretty aggressive and is noticeable from the adversary. For example, they might realise they can no longer access the infected device(s) and have been discovered. Once an adversary notices this, they may rush to complete their action on objectives. Alternatively, they may change their focus to a compromised system that hasn’t been noticed yet.
For the sake of this room, action on objectives is the adversary achieving what they initially set out to do. This could be stealing data, or causing maximum damage to the organisation (i.e. start deleting files or damaging systems), to name a few.
When choosing this strategy, you should consider the following:
- How aggressive do you want the isolation to be?
- Is the adversary likely to rush their action on objectives? Threat intelligence can be used to help determine this.
- Do we understand the adversary enough yet? Perhaps controlled isolation would be more useful here if we do not.
**Controlled isolation** is a less aggressive strategy in containment. Although, it isn’t entirely risk-free.
This strategy involves the incidence response team closely monitoring the adversary’s actions. Rather than strictly isolating the infected system(s), the team would keep the system accessible to not tip off the adversary.
An incident response team can gather vital information and intelligence about the adversary by allowing the adversary to continue.
However, the adversary isn’t given free-roam. For example, the incident response team can prevent access if the adversary is about to perform something destructive such as wiping or exfilling data. A good “cover story” can be made to convince the adversary why they’ve suddenly lost access. For example, an announcement could be made that routine maintenance is occurring.
The ultimate aim is to understand our adversaries here without tipping them off to the fact that they are being monitored. Ultimately, it’s a “cat and mouse” game between the incidence response team and the adversary.
When choosing this strategy, you should consider the following:
- What is the risk of allowing the adversary to continue?
- Do we know enough about the adversary already?
- If so, perhaps full-on isolation would be best.
- Do we have the appropriate means to stop an adversary before they do something destructive? Can we allocate the resources and human power to closely and constantly monitor the adversary?
Linking Together
The threat intelligence and containment strategies bridge the gap between the incident response process's identification, scoping, eradication, and recovery phases. Furthermore, with good threat intelligence,  we have good identification. Threat intelligence is an ever-going process, as you will come to discover in later tasks.
Answer the questions below
What is the name of the containment strategy used when the responders closely monitor the adversary?
*Controlled Isolation*
What containment strategy is considered to be the most aggressive?
*Entire isolation*
### Task 4  Creating Threat Intelligence
It is important to understand what threat intelligence looks like. Threat intelligence is anything that can be attributed to a malicious actor. Some common forms of threat intelligence include:
- IP Addresses
- File Hashes
- Domains
- File Names (I.e. toolkits)
- Patterns, activity or techniques of known threat campaigns (TTPs)
Tactics Techniques Procedures (TTPs)
These three ingredients are used to describe the aims, techniques and methods of a threat actor. These are extremely important in understanding how the threat actor operates. For example, what toolkits do they use? What are the threat actor's objectives? Are they trying to steal data or trying to cause damage to the organisation? Is there a criminal or political reason behind their attack?
I've broken down the three ingredients below:
**Tactics:** This ingredient is the high-level objectives that the threat actor aims to achieve. For example, are they trying to steal data or corporate secrets? Perhaps they're trying to blackmail the organisation or are attacking for bragging rights.
**Techniques:** This ingredient is the specific tools or methods the threat actor employs to achieve their tactics. For example, how did the adversary gain entry? Phishing? Are they targeting any specific software or service? What methods are the adversary using to privilege escalate or laterally move across the network?
**Procedures:** This ingredient looks at the attack chain used by the adversary. For example, what is the entire process from initial access to action on objectives? To illustrate, a procedure could be phishing -> credential stealing -> accessing a privileged user account -> laterally moving -> stealing sensitive information.
By understanding the TTPs of a threat actor, we can tailor our response to the cyber threat. We can also build a picture of how the threat actor behaves.
Threat Intelligence Platforms
Multiple threat intelligence platforms are available that aid in distributing threat intelligence. For example, OpenCTI is a framework that allows the collaborative sharing of threat intelligence. In this scenario, we can see the generated report for the _tal0nix_ adversary in the OpenCTI framework.
