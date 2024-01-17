---
To learn key attack vectors used by hackers and how to protect yourself using different hardening techniques.
---

# Microsoft Windows Hardening — Writeup

## Overview
### Microsoft Windows Hardening — Writeup
### Microsoft Windows Hardening — Writeup
![](https://tryhackme-images.s3.amazonaws.com/room-icons/efef926dddd6aa1e30d6558cfa5968e6.png)
### Introduction
The room aims to teach basic concepts required to harden a workstation coupled with knowledge of services/software/applications that may result in hacking a computer or data breach.
Learning Objectives
Identity & access management.
Network management.
Application management.
Storage & Compute.
Importance of updating Windows.
Cheat sheet for hardening Windows.
Connecting to the Machine
We will be using Windows 10 as a development/test machine throughout the room with the following credentials:
Machine IP: 10.10.118.42
Username: Harden
Password: harden
You can start the virtual machine in split screen view by clicking Start Machine. Alternatively, you can connect with the VM using the above credentials through Remote Desktop.
Image for RDP
Prerequisites
Before starting this room, go through the following already developed rooms for understanding the Windows fundamentals:
Windows Fundamentals 1 (Windows desktop, the NTFS file system, UAC, the Control Panel)
Windows Fundamentals 2 (System Configuration, UAC Settings, Resource Monitoring, the Windows Registry)
Windows Fundamentals 3 (Microsoft tools that help keep the device secure, such as Windows Updates, Windows Security, BitLocker)
Follow along with the steps described in upcoming tasks. Let's begin.
### Understanding General Concepts
Services
Windows Services create and manage critical functions such as network connectivity, storage, memory, sound, user credentials, and data backup and runs automatically in the background. These services are managed by the Service Control Manager panel and divided into three categories, i.e. Local, Network & System. Many applications like browsers and anti-virus software can also run their services for a seamless user experience.
Type services.msc in the Run window to access Windows services.
Windows Registry
The Windows registry is a unified container database that stores configurational settings, essential keys and shared preferences for Windows and third-party applications. Usually, on the installation of most applications, it uses a registry editor for storing various states of the application. For example, suppose an application (malicious or normal) wants to execute itself during the computer boot-up process; In that case, it will store its entry in the Run & Run Once key.
Usually, a malicious program makes undesired changes in the registry editor and tries to abuse its program or service as part of system routine activities. It is always recommended to protect the registry editor by limiting its access to unauthorised users.
Type regedit in the Run dialogue or taskbar search to access the registry editor.
Image for Accessing Registry
Event Viewer
Event Viewer is an app that shows log details about all events occurring on your computer, including driver updates, hardware failures, changes in the operating system, invalid authentication attempts and application crash logs. Event Viewer receives notifications from different services and applications running on the computer and stores them in a centralised database.
Hackers and malicious actors access Event Viewer to increase their attack surface and enhance the target system's profiling. Event categories are as below:
Application: Records events of system components.
System: Records events of already installed programs.
Security: Logs events related to security and authentication etc.
We can access Event Viewer by typing eventvwr in the Run window. The default location for storing events is C:\WINDOWS\system32\config\folder in the attached VM (10.10.118.42).
Telemetry
Telemetry is a data collection system used by Microsoft to enhance the user experience by preemptively identifying security and functional issues in software. An application seamlessly shares data (crash logs, application-specific) with Microsoft to improve the user experience for future releases.
Telemetry functionality is achieved by Universal Telemetry Client (UTC) services available in Windows and runs through diagtrack.dll. Contents acquired through telemetry service are stored encrypted in a local folder %ProgramData%\Microsoft\Diagnosis and sent to Microsoft after 15 minutes or so.
We can access The DiagTrack through the Services console in Windows 10.
In subsequent tasks, we will harden Windows 10 through various techniques at the User, Network, Application & Storage levels.
![[Pasted image 20221018205230.png]]
What is the startup type of App Readiness service in the services panel?
*Manual*
![[Pasted image 20221018205413.png]]
Open Registry Editor and find the key “tryhackme”. What is the default value of the key?
You can use the Find Option in Registry Editor
*{THM_REG_FLAG}*
![[Pasted image 20221018210443.png]]
![[Pasted image 20221018210509.png]]
![[Pasted image 20221018210530.png]]
Open the Diagnosis folder and go through the various log files. Can you find the flag?
*{THM_1000710}*
![[Pasted image 20221018210701.png]]
Open the Event Viewer and play with various event viewer filters like Information, Error, Warning etc. Which error type has the maximum number of logs?
### Identity & Access Management
Standard vs Admin Account
Identity and access management involves employing best practices to ensure that only authenticated and authorised users can access the system. There are two types of accounts in Windows, i.e. Admin and Standard Account. Per best practice, the Admin account should only be used to carry out tasks like software installation and accessing the registry editor, service panel, etc. Routine functions like access to regular applications, including Microsoft Office, browser, etc., can be allowed to standard accounts. Go to Control Panel > User Accounts to create standard or administrator accounts.
In either case, a user can authenticate themselves on the system through a password; however, Windows 10 has introduced a new feature called Windows Hello, which allows authenticating someone based on “something you have, something you know or something you are”.
To access accounts and select the sign-in option, go to Settings > Accounts > Sign-in Options.
User Account Control (UAC)
User Account Control (UAC) is a feature that enforces enhanced access control and ensures that all services and applications execute in non-administrator accounts. It helps mitigate malware's impact and minimises privilege escalation by [bypassing UAC](https://tryhackme.com/room/bypassinguac). Actions requiring elevated privileges will automatically prompt for administrative user account credentials if the logged-in user does not already possess these.
For example, installing device drivers or allowing inbound connections through Windows Firewall requires more permissions than already available privileges for a standard user. We have covered the topic in detail in Windows Fundamental 1.
As a principle, always follow the Principle of Least Privilege, which states that (Per [CISA](https://www.cisa.gov/uscert/bsi/articles/knowledge/principles/least-privilege#:~:text=The%20Principle%20of%20Least%20Privilege%20states%20cthat%20a%20subject%20should,should%20not%20have%20that%20right)) “a subject should be given only those privileges needed for it to complete its task. If a subject does not need an access right, the subject should not have that right”.
To access UAC, go to Control Panel -> User Accounts and click on Change User Account Control Setting.
Keep the notification level "Always Notify" in the User Account Control Settings.
Local Policy and Group Policies Editor
Group Policy Editor is a built-in interactive tool by Microsoft that allows to configure and implement local and group policies. We mainly use this feature when part of a network; however, we can also use it for a workstation to limit the execution of vulnerable extensions, set password policies, and other administrative settings.
Note: The feature is not available in Windows Home but only in the Pro and Enterprise versions.
Password Policies
One primary use of a local policy editor is to ensure complex and strong passwords for user accounts. For example, we can design password policies to maximise our security:
Passwords must contain both uppercase and lowercase characters.
Check passwords against leaked or already hacked databases or a dictionary of compromised passwords.
In case of 6 failed login attempts within 15 minutes, the account will remain locked for at least 1 hour.
We can access Password policies through the Local group policy editor.
Go to Security settings > Account Policies > Password policy
Setting A Lockout Policy
To protect your system password from being guessed by an attacker, we can set out a lockout policy so the account will automatically lock after certain invalid attempts. To set a lockout policy, go to Local Security Policy > Windows Settings > Account Policies > Account Lockout Policy and configure values to lock out hackers after three invalid attempts.
Find the name of the Administrator Account of the attached VM.
*Harden*
Go to the User Account Control Setting Panel (Control Panel > All Control Panel Items > User Accounts). What is the default level of Notification?
*Always Notify*
How many standard accounts are created in the VM?
*0*
### Network Management
Windows Defender Firewall
Windows Defender Firewall is a built-in application that protects computers from malicious attacks and blocks unauthorised traffic through inbound and outbound rules or filters. As an analogy, this is equivalent to “who is coming in and going out of your home”.
Malicious actors abuse Windows Firewall by bypassing existing rules. For example, if we have configured the firewall to allow incoming connections, hackers will try to manipulate the functionality by creating a remote connection to the victim's computer.
You can see more details about Windows Firewall Configuration [here](https://tryhackme.com/room/redteamfirewalls).
We can access Windows Defender Firewall by accessing WF.msc in the Run dialogue.
As mentioned in the Windows Fundamentals room, it has three main profiles Domain, Public and Private.  The Private profile must be activated with "Blocked Incoming Connections" while using the computer at home.
View detailed settings for each profile by clicking on Windows Defender Firewall Properties.
Whenever possible, enable the Windows Defender Firewall default settings. For blocking all the incoming traffic, always configure the firewall with a 'default deny' rule before making an exception rule that allows more specific traffic.
Disable unused Networking Devices
Network devices like routers, ethernet cards, WiFI adapters etc., enable data sharing between computers. If the device is improperly configured or not being used by the owner, it is recommended to disable the interface so that threat actors cannot access them and use them for data retrieval from the victim's computer.
To disable the unused Networking Devices, go to the Control panel > System and Security Setting > System > Device Manager and disable all the unused Networking devices.
Disable SMB protocol
SMB is a file-sharing protocol exploited by hackers in the wild. The protocol is primarily used for file sharing in a network; therefore, you must disable the protocol if your computer is not part of a network by issuing the [following](https://docs.microsoft.com/en-us/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3) command in PowerShell.
```text
Administrator - Windows PowerShell

           
user@machine$ Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol
Path          :
Online        : True
RestartNeeded : False
```
Protecting Local Domain Name System (DNS)
The domain name system (DNS) is a naming system that translates Fully Qualified Domain Names (FQDN) into IP addresses. If the attacker places himself in the middle, he may intercept and manipulate DNS requests and point them to attacker-controlled systems since DNS replies are neither authenticated nor encrypted.
The hosts file located in Windows acts like local DNS and is responsible for resolving hostnames to IP addresses. Malicious actors try to edit the file's content to reroute traffic to their command and control server.
The hosts file is located at C:\Windows\System32\Drivers\etc\hosts.
Mitigating Address Resolution Protocol Attack
The address resolution protocol resolves MAC addresses from given IP addresses saved in the workstations ARP cache. The ARP offers no authentication and accepts responses from any user in the network. An attacker can flood target systems with crafted ARP responses, which point to an attacker-controlled machine and put him in the middle of communication between the targeted hosts.
You can check ARP entries using the command arp -a in the command prompt.
```text
Command Prompt

           
user@machine$ arp -a
Interface: 192.168.231.2 --- 0x5
  Internet Address      Physical Address      Type
  192.168.231.255       ff-ff-ff-ff-ff-ff     static
  224.0.0.2             01-00-5e-00-00-02     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
