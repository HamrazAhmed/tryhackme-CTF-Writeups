---
Learn how to bypass common runtime detection measures, such as AMSI, using modern tool-agnostic approaches.
---

# Runtime Detection Evasion — Writeup

## Overview
### Runtime Detection Evasion — Writeup
### Runtime Detection Evasion — Writeup
![|333](https://tryhackme-images.s3.amazonaws.com/room-icons/f47704dcbd8d48f0f68e236c021d35c3.png)
### Introduction
With the release of PowerShell <3 the Blue Team, Microsoft released AMSI (Anti-Malware Scan Interface), a runtime monitoring solution designed to stop and monitor ongoing threats.
Learning Objectives
Understand the purpose of runtime detections and how they are instrumented.
Learn and apply techniques to bypass AMSI.
Understand common mitigations and potential alternatives to techniques.
Runtime detection measures can cause many headaches and roadblocks when executing malicious code. Luckily for us as attackers, there are several techniques and methods we can abuse and leverage to bypass common runtime detection solutions.
This room will use research from several authors and researchers; all credit goes to the respective owners.
Before beginning this room, familiarize yourself with operating system architecture as a whole. Basic programming knowledge in C# and PowerShell is also recommended but not required.
We have provided a base Windows machine with the files needed to complete this room. You can access the machine in-browser or through RDP using the credentials below.
Machine IP: MACHINE_IP             Username: THM-Attacker             Password: Tryhackme!
This is going to be a lot of information. Please buckle your seatbelts and locate your nearest fire extinguisher.
### Runtime Detections
When executing code or applications, it will almost always flow through a runtime, no matter the interpreter. This is most commonly seen when using Windows API calls and interacting with .NET. The [CLR](https://docs.microsoft.com/en-us/dotnet/standard/clr) (Common Language Runtime) and [DLR](https://docs.microsoft.com/en-us/dotnet/framework/reflection-and-codedom/dynamic-language-runtime-overview) (Dynamic Language Runtime) are the runtimes for .NET and are the most common you will encounter when working with Windows systems. In this task, we will not discuss the specifics of runtimes; instead, we will discuss how they are monitored and malicious code is detected.
A runtime detection measure will scan code before execution in the runtime and determine if it is malicious or not. Depending on the detection measure and technology behind it, this detection could be based on string signatures, heuristics, or behaviors. If code is suspected of being malicious, it will be assigned a value, and if within a specified range, it will stop execution and possibly quarantine or delete the file/code.
Runtime detection measures are different from a standard anti-virus because they will scan directly from memory and the runtime. At the same time, anti-virus products can also employ these runtime detections to give more insight into the calls and hooks originating from code. In some cases, anti-virus products may use a runtime detection stream/feed as part of their heuristics.
We will primarily focus on [AMSI](https://docs.microsoft.com/en-us/windows/win32/amsi/antimalware-scan-interface-portal)(Anti-Malware Scan Interface) in this room. AMSI is a runtime detection measure shipped natively with Windows and is an interface for other products and solutions.
What runtime detection measure is shipped natively with Windows?
*AMSI*
AMSI (Anti-Malware Scan Interface) is a PowerShell security feature that will allow any applications or services to integrate directly into anti-malware products. Defender instruments AMSI to scan payloads and scripts before execution inside the .NET runtime. From Microsoft: "The Windows Antimalware Scan Interface (AMSI) is a versatile interface standard that allows your applications and services to integrate with any anti-malware product that's present on a machine. AMSI provides enhanced malware protection for your end-users and their data, applications, and workloads."
For more information about AMSI, check out the Windows docs.
AMSI will determine its actions from a response code as a result of monitoring and scanning. Below is a list of possible response codes,
AMSI_RESULT_CLEAN = 0
AMSI_RESULT_NOT_DETECTED = 1
AMSI_RESULT_BLOCKED_BY_ADMIN_START = 16384
AMSI_RESULT_BLOCKED_BY_ADMIN_END = 20479
AMSI_RESULT_DETECTED = 32768
These response codes will only be reported on the backend of AMSI or through third-party implementation. If AMSI detects a malicious result, it will halt execution and send the below error message.
```text
AMSI Error Response

           
PS C:Users\Tryhackme> 'Invoke-Hacks'
At line:1 char:1
+ "Invoke-Hacks"
+ ~~~~~~~~~~~~~~
This script contains malicious content and has been blocked by your antivirus software.
		+ CategoryInfo          : ParserError: (:) []. ParentContainsErrorRecordException
		+ FullyQualifiedErrorId : ScriptContainedMaliciousContent
```
AMSI is fully integrated into the following Windows components,
User Account Control, or UAC
PowerShell
