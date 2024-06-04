---
Learn about active defense mechanisms Blue Teamers can deploy to identify adversaries in their environment.
---

# Sandbox Evasion — Writeup

## Overview
### Sandbox Evasion — Writeup
### Sandbox Evasion — Writeup
![|333](https://tryhackme-images.s3.amazonaws.com/room-icons/152639915686cc66d088790d04a5f1b3.png)
### Introduction
Welcome to Sandbox Evasion
Lots of companies deploy a “Defense in Depth” strategy, which refers to implementing security in layers, so if one layer fails, there should be another one that an adversary must evade. In this room, we will be focusing on one unique type of active defense; Sandboxes. Sandboxes provide a safe way to analyze a potentially malicious file and observe the effects on the system and return if the executable is malicious or not.
Learning Objectives
In this room, we will learn about Sandboxes in-depth; by the time you finish this room, you will gain a better understanding of the following topics:
Learn how Malware Sandboxes work
Learn about Static and Dynamic Malware Analysis
Common Sandbox Evasion Methods
Developing and Testing Sandbox Evasion Methods with Any.Run
Room Pre-requisites
For this room, we recommend the prior experience in the following areas:
Windows APIs
C++ Programming
Active Directory
### An Adversary walks into a Sandbox
What is Malware Analysis
Malware Analysis is the process of analyzing a suspicious file to determine what it does on both a micro level (by looking at Assembly), and a macro level (by looking at what it does on the system). This process lets Blue Teamers gain a better understanding of malicious programs, which can aid them in developing detections.
Static vs. Dynamic Analysis
There are two ways that a Blue Teamer can analyze a suspicious file; one way is by looking at the code on a micro-level (as previously stated) by using Disassemblers such as IDA or Ghidra. This process is more well known as “Static Analysis”.
On the flip side of the coin, we can observe what happens when the suspicious file is executed on the system through a process called “Dynamic Analysis”. On the system, there are often many analysis tools installed, such as EDR Software, Sysmon, ProcMon, Process Hacker, and Debuggers (For example, OllyDebug, WinDbg, x64Dbg), and much more.
Introduction to Sandboxes
One of the most creative and effective ways that Blue Teamers have come up with to analyze suspicious-looking files is in the category of Dynamic Analysis. This method involves running the file in a containerized (or virtualized) environment; This environment is referred to as a Sandbox. Depending on the sandbox of choice, you may be able to customize what version of Windows is running, the software installed on the machine, and much more.
Sandboxes provide a safe and effective way to monitor what a suspicious-looking file does before running it on a production system (or allowing it to be sent to a production system). There are many commercial Sandboxes that may be in place in various parts of a network.
In the diagram above, there are three different sandboxes in place. It is not uncommon for there to be one, two, or even three Sandboxes in a corporate environment. Often you may find them in the following places:
Firewalls
Mail Servers
Workstations
Each sandbox may work differently; for example, a Firewall may execute the attachment in the email and see what kind of network communications occur, whereas a Mail sandbox may open the email and see if an embedded file within the email triggers a download over a protocol like SMB in an attempt to steal a NetNTLM hash, where a host-based Anti-Virus Sandbox may execute the file and monitor for malicious programmatic behavior or changes to the system.
There are various vendors that make various Sandbox products that Blue Teamers may be able to deploy in a corporate network. Here are some popular examples:
Palo Alto Wildfire (Firewall) https://www.paloaltonetworks.co.uk/products/secure-the-network/wildfire
Proofpoint TAP (Email Sandbox)https://www.proofpoint.com/uk/products/advanced-threat-protection/targeted-attack-protection
Falcon Sandbox (EDR/Workstation)https://www.crowdstrike.co.uk/products/threat-intelligence/falcon-sandbox-malware-analysis/
MimeCast (Email Sandbox)/https://www.mimecast.com/
VirusTotal (Sample Submission Site)https://www.virustotal.com
Any.Run (Sample Submission Site)https://any.run/
Antiscan.me (Sample Submission Site)https://antiscan.me/
Joe Sandbox (Sample Submission Site)https://www.joesandbox.com/
In the next section, we will learn about various techniques commonly deployed by Malware authors to gain an understanding of some evasion techniques that exist.
We have provided a Windows development VM where you can develop your own Sandbox evasion techniques. You can access the virtual machine with the following credentials:
Username: Administrator
Password: TryHackMe123!
Sandboxes are a form of ______ Analysis
*Dynamic*
What type of Sandboxes analyze attachments attached to emails?
*Mail sandbox*
### Common Sandbox Evasion Techniques
An Introduction to Sandbox Evasion
Now that you have a general idea of what Malware Sandboxes are, we can move on to learning some evasion techniques at a high level. We will be breaking this down into four different categories; in the next task, we will implement four different evasion techniques (one from each category), so you can leave this room with some practical knowledge to help out in your Red Team operations.
We will be covering the following four broad categories:
Sleeping through Sandboxes
Geolocation and Geoblocking
Checking System Information
Querying Network Information
These are ordered from the most basic techniques to the most advanced. Let's get started.
Sleeping through Sandboxes
Malware Sandboxes are often limited to a time constraint to prevent the overallocation of resources, which may increase the Sandboxes queue drastically. This is a crucial aspect that we can abuse; if we know that a Sandbox will only run for five minutes at any given time, we can implement a sleep timer that sleeps for five minutes before our shellcode is executed. This could be done in any number of ways; one common way is to query the current system time and, in a parallel thread, check and see how much time has elapsed. After the five minutes have passed, our program can begin normal execution.
Another popular method is to do complex, compute-heavy math, which may take a certain amount of time — for example, calculating the Fibonacci sequence up to a given number. Remember that it may take more or less time to do so based on the system's hardware. Masking your application is generally a good idea to avoid Anti-Virus detections in general, so this should already be something in your toolkit.
Beware that some sandboxes may alter built-in sleep functions; various Anti-Virus vendors have put out blog posts about bypassing built-in sleep functions. So it is highly recommended you develop your own sleep function. Here are a couple of blog posts about bypassing Sleep functions:
https://evasions.checkpoint.com/techniques/timing.html
https://www.joesecurity.org/blog/660946897093663167
Geolocation
One defining factor of Sandboxes is that they are often located off-premise and are hosted by Anti-Virus providers. If you know you are attacking TryHackMe, a European company, and your binary is executed in California, you can make an educated guess that the binary has ended up in a Sandbox. You may choose to implement a geolocation filter on your program that checks if the IP Address block is owned by the company you are targeting or if it is from a residential address space. There are several services that you can use to check this information:
ifconfig.me
https://rdap.arin.net/registry/ip/1.1.1.1
IfConfig.me can be used to retrieve your current IP Address, with additional information being optional. Combining this with ARIN's RDAP allows you to determine the ISP returned in an easy to parse format (JSON).
It is important to note that this method will only work if the host has internet access. Some organizations may build a block list of specific domains, so you should be 100% sure that this method will work for the organization you are attempting to leverage this against.
Checking System Information
Another incredibly popular method is to observe system information. Most Sandboxes typically have reduced resources. A popular Malware Sandbox service, Any.Run, only allocates 1 CPU core and 4GB of RAM per virtual machine:
a Screenshot of the SystemInfo command from Any.Run
Most workstations in a network typically have 2-8 CPU cores, 8-32GB of RAM, and 256GB-1TB+ of drive space. This is incredibly dependent on the organization that you are targeting, but generally, you can expect more than 2 CPU cores per system and more than 4GB of RAM. Knowing this, we can tailor our code to query for basic system info (CPU core count, RAM amount, Disk size, etc).
By no means is this an exhaustive list, but here are some additional examples of things you may be able to filter on:
Storage Medium Serial Number
PC Hostname
BIOS/UEFI Version/Serial Number
Windows Product Key/OS Version
Network Adapter Information
Virtualization Checks
Current Signed in User
and much more!
Querying Network Information
The last method is the most open-ended method that we will be covering. Because of its open-endedness it is considered one of the more advanced methods as it involves querying information about the Active Directory domain.
Almost no Malware Sandboxes are joined in a domain, so it's relatively safe to assume if the machine is not joined to a domain, it is not the right target! However, you cannot always be too sure, so you should collect some information about the domain to be safe. There are many objects that you can query; here are some to consider:
Computers
User accounts
Last User Login(s)
Groups
Domain Admins
Enterprise Admins
Domain Controllers
Service Accounts
DNS Servers
These techniques can vary in difficulty; therefore, you should consider how much time and effort you want to spend building out these evasion methods. A simple method, such as checking the systems environment variables (this can be done with echo %VARIABLE% or to display all variables, use the set command) for an item like the LogonServer, LogonUserSid, or LogonDomain may be much easier than implementing a Windows API.
Setting the Stage
Now that you have a better understanding of what Sandbox Bypass method types exist, we will take it to the next step and implement some of the Sandbox Bypasses in the next task.
Before we move on to the next task, we're going to be starting with a basic dropper that retrieves shellcode from a Web Server (specifically from /index.raw) and injects it into memory, and executes the shellcode. It's important to note that all shellcode must be generated with MSFVenom in a raw format, and must be 64-bit, not 32-bit. It can be generated with the following command.
```text

```
The shellcode should then be hosted on the AttackBox via any HTTP Server. Python3's http.server module is highly portable and flexible and will serve as a good base for this task. In the real world, you may host your shellcode on your C2 server. For the purposes of the lab, we will be utilizing the Attackbox with no C2 server.
The code attached to this task has been tested and compiled using Visual Studio 2019 (or above). Download the dropper.cpp, and open it. It's important to note that there are several placeholder values on lines 16, 22, 24, 27, and 33 that you must update to make the code function properly. Once you have altered the values, compile the code for a 64-bit release.
Read the above task to learn about Sandbox Evasion Techniques.
*No answer needed*
Download the task files and modify the .cpp file to retrieve the MSFVenom generated shellcode.
*No answer needed*
Which Sandbox Evasion method would you use to abuse a Sandbox that runs for a short period of time?
Note: most Sandboxes are only allowed to run for a short period of time
*Sleeping*
Which Sandbox Evasion method would you use to check the Sandboxes system information for virtualised devices?
Note: Sandboxes usually run with limited resources and virtualised devices
*Checking System Information*
### Implementing Various Evasion Techniques
Diving into Sandbox Evasion
With this base code acquired, we will take our first step into the world of Sandbox Evasion. We're going to start with our sleep because it is the simplest.
Taking a Nap
We can take our template code from the previous task and add a Sleep statement for 120,000MS  to it. This translates to roughly 120 seconds or 2 minutes. Generally, you would want a time closer to 5 minutes to be sure; however, 2 minutes will suffice for testing purposes. We'll now add our Sleep statement in the main function:
```text
