---
Learn how to bypass common logging and system monitoring, such as ETW, using modern tool-agnostic approaches.
---

# Evading Logging and Monitoring — Writeup

## Overview
### Evading Logging and Monitoring — Writeup
### Evading Logging and Monitoring — Writeup
![[Pasted image 20220917163748.png]]
![](https://tryhackme-images.s3.amazonaws.com/room-icons/c77e1c5ff6a6ab412828ef7cfa8cbb50.png)
### Introduction
One of the largest obstacles in an attacker’s path is logging and monitoring. Unlike anti-virus and EDR (Endpoint Detection and Response) solutions, logging creates a physical record of activity that can be analyzed for malicious activity.
How a device is monitored will depend on the environment and preferences of the corporation. Teams may decide not to monitor some devices at all. Generally, a monitoring solution will begin at the host device, collecting application or event logs. Once logs are created, they can be kept on the device or sent to an event collector/forwarder. Once they are off the device, the defense team decides how to aggregate them; this is generally accomplished using an indexer and a SIEM (Security Information and Event Manager).
An attacker may not have much control once logs are taken off a device, but can control what is on the device and how it is ingested. The primary target for an attacker is the event logs, managed and controlled by ETW (Event Tracing for Windows).
This room will address event tracing and its weaknesses to allow an attacker to evade or disable ETW-based solutions.
Learning Objectives
Understand the technology and implementation of event tracing.
Understand how techniques are created to evade ETW.
Learn how to apply theoretical evasion concepts to code.
Before beginning this room, familiarize yourself with basic Windows usage and functionality; we recommend completing the Windows Internals room. Basic programming knowledge in C and PowerShell is also recommended but not required.
We have provided a base Windows machine with the files needed to complete this room. You can access the machine in-browser or through RDP using the credentials below.
Machine IP: MACHINE_IP             Username: Administrator             Password: Tryhackme!
This is going to be a lot of information. Please buckle your seatbelts and locate your nearest fire extinguisher.
### Event Tracing
As previously mentioned, almost all event logging capability within Windows is handled from ETW at both the application and kernel level. While there are other services in place like Event Logging and Trace Logging, these are either extensions of ETW or less prevalent to attackers.
Component	Purpose
Controllers	Build and configure sessions
Providers	Generate events
Consumers	Interpret events
We will cover each component and how it is instrumented in more depth in the next task.
While less important to an attacker than components, event IDs are a core feature of Windows logging. Events are sent and transferred in XML(Extensible Markup Language) format which is the standard for how events are defined and implemented by providers. Below is an example of event ID 4624: An account was successfully logged on.

## Exploitation
```text
Event ID:4624
Source:Security
Category:Logon/Logoff
Message:An account was successfully logged on.

Subject:
Security ID: NT AUTHORITY\\SYSTEM
Account Name: WORKSTATION123$
...
[ snip ]
...
Logon Type: 7

New Logon:
Security ID: CORPDOMAIN\\john.doe
Account Name: john.doe
...
[ snip ]
...
Process Information:
Process ID: 0x314
```
For more information about event logging, check out the Windows Event Logs room.
At this point, we understand why logging can disrupt an attacker, but how exactly is ETW relevant to an attacker? ETW has visibility over a majority of the operating system, whereas logging generally has limited visibility or detail.
Due to the visibility of ETW, an attacker should always be mindful of the events that could be generated when carrying out their operation. The best approach to taking down ETW is to limit its insight as much as possible into specifically what you are doing while maintaining environment integrity.
In the upcoming tasks, we will cover ETW instrumentation, ETW evasion, and other ETW-based solutions.
What ETW component will build and configure sessions?
Found in table x.
*Controllers*
What event ID logs when a user account was deleted?
This question will require basic research outside of this room.
*4726*  Event ID 4726 - A user account was deleted
### Approaches to Log Evasion
Before diving deep into the more modern and technical evasion techniques, let’s look at the various approaches available and their impacts on attackers and defenders.
When first thinking about and assessing log evasion, you may think that simply destroying or tampering with the logs may be viable.
Following security best practices, it is typical for a modern environment to employ log forwarding. Log forwarding means that the SOC will move or “forward” logs from the host machine to a central server or indexer. Even if an attacker can delete logs from the host machine, they could already be off of the device and secured.
Assuming an attacker did destroy all of the logs before they were forwarded, or if they were not forwarded, how would this raise an alert? An attacker must first consider environment integrity; if no logs originate from a device, that can present serious suspicion and lead to an investigation. Even if an attacker did control what logs were removed and forwarded, defenders could still track the tampering.
Event ID	Purpose
1102
Logs when the Windows Security audit log was cleared
104
Logs when the log file was cleared
1100
Logs when the Windows Event Log service was shut down
The above event IDs can monitor the process of destroying logs or “log smashing.” This poses a clear risk to attackers attempting to tamper with or destroy logs. Although it is possible to bypass these mitigations further or tamper with the logs, an attacker must assess the risk. When approaching an environment, you are generally unaware of security practices and take an OPSEC (Operational Security) risk by attempting this approach.
If the previous approach is too aggressive, how can we strategically approach the problem?
An attacker must focus on what logs a malicious technique may result in to keep an environment's integrity intact. Knowing what may be instrumented against them, they can utilize or modify published methods.
Most published techniques will target ETW components since that will allow an attacker the most control over the tracing process.
This room will break down some of the most common published techniques and a more modern technique that allows for a wide range of control.
How many total events can be used to track event tampering?
*3*
What event ID logs when the log file was cleared?
*104*
### Tracing Instrumentation
ETW is broken up into three separate components, working together to manage and correlate data. Event logs in Windows are no different from generic XML data, making it easy to process and interpret.
Event Controllers are used to build and configure sessions. To expand on this definition, we can think of the controller as the application that determines how and where data will flow. From the Microsoft docs, “Controllers are applications that define the size and location of the log file, start and stop event tracing sessions, enable providers so they can log events to the session, manage the size of the buffer pool, and obtain execution statistics for sessions.”
Event Providers are used to generate events. To expand on this definition, the controller will tell the provider how to operate, then collect logs from its designated source. From the Microsoft docs, “Providers are applications that contain event tracing instrumentation. After a provider registers itself, a controller can then enable or disable event tracing in the provider. The provider defines its interpretation of being enabled or disabled. Generally, an enabled provider generates events, while a disabled provider does not.”
There are also four different types of providers with support for various functions and legacy systems.
Provider	Purpose
MOF (Managed Object Format)
Defines events from MOF classes. Enabled by one trace session at a time.
WPP (Windows Software Trace Preprocessor)
Associated with TMF(Trace Message Format) files to decode information. Enabled by one trace session at a time.
Manifest-Based
Defines events from a manifest. Enabled by up to eight trace sessions at a time.
TraceLogging
Self-describing events containing all required information. Enabled by up to eight trace sessions at a time.
Event Consumers are used to interpret events. To expand on this definition, the consumer will select sessions and parse events from that session or multiple at the same time. This is most commonly seen in the “Event Viewer”. From the Microsoft docs, “Consumers are applications that select one or more event tracing sessions as a source of events. A consumer can request events from multiple event tracing sessions simultaneously; the system delivers the events in chronological order. Consumers can receive events stored in log files, or from sessions that deliver events in real time.”
Each of these components can be brought together to fully understand and depict the data/session flow within ETW.
From start to finish, events originate from the providers. Controllers will determine where the data is sent and how it is processed through sessions. Consumers will save or deliver logs to be interpreted or analyzed.
Now that we understand how ETW is instrumented, how does this apply to attackers? We previously mentioned the goal of limiting visibility while maintaining integrity. We can limit a specific aspect of insight by targeting components while maintaining most of the data flow. Below is a brief list of specific techniques that target each ETW component.
Component
Techniques
Provider
PSEtwLogProvider Modification, Group Policy Takeover, Log Pipeline Abuse, Type Creation
Controller
Patching EtwEventWrite, Runtime Tracing Tampering,
Consumers
Log Smashing, Log Tampering
We will cover each of these techniques in-depth in the upcoming tasks to provide a large toolbox of possibilities.
### Reflection for Fun and Silence
Within PowerShell, ETW providers are loaded into the session from a .NET assembly: PSEtwLogProvider. From the Microsoft docs, "Assemblies form the fundamental units of deployment, version control, reuse, activation scoping, and security permissions for .NET-based applications." .NET assemblies may seem foreign; however, we can make them more familiar by knowing they take shape in familiar formats such as an exe (executable) or a dll (dynamic-link library).
In a PowerShell session, most .NET assemblies are loaded in the same security context as the user at startup. Since the session has the same privilege level as the loaded assemblies, we can modify the assembly fields and values through PowerShell reflection. From [O'Reilly](https://www.oreilly.com/library/view/professional-windows-powershell/9780471946939/9780471946939_using_.net_reflection.html) , "Reflection allows you to look inside an assembly and find out its characteristics. Inside a .NET assembly, information is stored that describes what the assembly contains. This is called metadata. A .NET assembly is, in a sense, self-describing, at least if interrogated correctly."
In the context of ETW (Event Tracing for Windows), an attacker can reflect the ETW event provider assembly and set the field m_enabled to $null.
At a high level, PowerShell reflection can be broken up into four steps:
Obtain .NET assembly for PSEtwLogProvider.
Store a null value for etwProvider field.
Set the field for m_enabled to previously stored value.
At step one, we need to obtain the type for the PSEtwLogProvider assembly. The assembly is stored in order to access its internal fields in the next step.
![[Pasted image 20220917164803.png]]
At step two, we are storing a value ($null) from the previous assembly to be used.
![[Pasted image 20220917164816.png]]
At step three, we compile our steps together to overwrite the m_enabled field with the value stored in the previous line.
