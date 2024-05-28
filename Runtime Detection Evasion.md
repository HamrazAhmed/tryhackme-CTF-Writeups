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
Windows Script Host (wscript and cscript)
JavaScript and VBScript
Office VBA macros
As attackers, when targeting the above components, we will need to be mindful of AMSI and its implementations when executing code or abusing components.
In the next task, we will cover the technical details behind how AMSI works and is instrumented in Windows.
What response value is assigned to 32768?
*AMSI_RESULT_DETECTED*
### AMSI Instrumentation
The way AMSI is instrumented can be complex, including multiple DLLs and varying execution strategies depending on where it is instrumented. By definition, AMSI is only an interface for other anti-malware products; AMSI will use multiple provider DLLs and API calls depending on what is being executed and at what layer it is being executed.
AMSI is instrumented from System.Management.Automation.dll, a .NET assembly developed by Windows; From the Microsoft docs, "Assemblies form the fundamental units of deployment, version control, reuse, activation scoping, and security permissions for .NET-based applications." The .NET assembly will instrument other DLLs and API calls depending on the interpreter and whether it is on disk or memory. The below diagram depicts how data is dissected as it flows through the layers and what DLLs/API calls are being instrumented.
In the above graph data will begin flowing dependent on the interpreter used (PowerShell/VBScript/etc.)  Various API calls and interfaces will be instrumented as the data flows down the model at each layer. It is important to understand the complete model of AMSI, but we can break it down into core components, shown in the diagram below.
Note: AMSI is only instrumented when loaded from memory when executed from the CLR. It is assumed that if on disk MsMpEng.exe (Windows Defender) is already being instrumented.
Most of our research and known bypasses are placed in the Win32 API layer, manipulating the [AmsiScanBuffer](https://learn.microsoft.com/en-us/windows/win32/api/amsi/nf-amsi-amsiscanbuffer) API call.
You may also notice the "Other Applications" interface from AMSI. Third-parties such as AV providers can instrument AMSI from their products. Microsoft documents AMSI functions and the AMSI stream interface.
We can break down the code for AMSI PowerShell instrumentation to better understand how it is implemented and checks for suspicious content. To find where AMSI is instrumented, we can use InsecurePowerShell maintained by Cobbr. [InsecurePowerShell](https://github.com/PowerShell/PowerShell/compare/master...cobbr:master) is a GitHub fork of PowerShell with security features removed; this means we can look through the compared commits and observe any security features. AMSI is only instrumented in twelve lines of code under src/System.Management.Automation/engine/runtime/CompiledScriptBlock.cs. These twelve lines are shown below.
![[Pasted image 20220917155215.png]]
We can take our knowledge of how AMSI is instrumented and research from others to create and use bypasses that abuse and evade AMSI or its utilities.
Will AMSI be instrumented if the file is only on disk? (Y/N)
*N*
### PowerShell Downgrade
The PowerShell downgrade attack is a very low-hanging fruit that allows attackers to modify the current PowerShell version to remove security features.
Most PowerShell sessions will start with the most recent PowerShell engine, but attackers can manually change the version with a one-liner. By "downgrading" the PowerShell version to 2.0, you bypass security features since they were not implemented until version 5.0.
The attack only requires a one-liner to execute in our session. We can launch a new PowerShell process with the flags -Version to specify the version (2).
```text
PowerShell -Version 2
```
This attack can actively be seen exploited in tools such as Unicorn.
https://github.com/trustedsec/unicorn
![[Pasted image 20220917160029.png]]
Since this attack is such low-hanging fruit and simple in technique, there are a plethora of ways for the blue team to detect and mitigate this attack.
The two easiest mitigations are removing the PowerShell 2.0 engine from the device and denying access to PowerShell 2.0 via application blocklisting.
Enter the flag obtained from the desktop after executing the command in cmd.exe.
![[Pasted image 20220917160620.png]]
### PowerShell Reflection
Reflection allows a user or administrator to access and interact with .NET assemblies. From the Microsoft docs, "Assemblies form the fundamental units of deployment, version control, reuse, activation scoping, and security permissions for .NET-based applications." .NET assemblies may seem foreign; however, we can make them more familiar by knowing they take shape in familiar formats such as exe (executable) and dll (dynamic-link library).
PowerShell reflection can be abused to modify and identify information from valuable DLLs.
The AMSI utilities for PowerShell are stored in the AMSIUtils .NET assembly located in System.Management.Automation.AmsiUtils.
Matt Graeber published a one-liner to accomplish the goal of using Reflection to modify and bypass the AMSI utility. This one-line can be seen in the code block below.
![[Pasted image 20220917160734.png]]
To explain the code functionality, we will break it down into smaller sections.
First, the snippet will call the reflection function and specify it wants to use an assembly from [Ref.Assembly] it will then obtain the type of the AMSI utility using GetType.
![[Pasted image 20220917160748.png]]
The information collected from the previous section will be forwarded to the next function to obtain a specified field within the assembly using GetField.
![[Pasted image 20220917160804.png]]
The assembly and field information will then be forwarded to the next parameter to set the value from $false to $true using SetValue.
![[Pasted image 20220917160821.png]]
Once the amsiInitFailed field is set to $true, AMSI will respond with the response code: AMSI_RESULT_NOT_DETECTED = 1
Read the above and practice leveraging the one-liner on the provided machine.
To utilize the one-liner, you can run it in the same session as the desired malicious code or prepend it to the malicious code.
You must already be in a PowerShell session to execute the one-liner
Enter the flag obtained from the desktop after executing the command.
![[Pasted image 20220917160947.png]]
### Patching AMSI
AMSI is primarily instrumented and loaded from amsi.dll; this can be confirmed from the diagram we observed earlier. This dll can be abused and forced to point to a response code we want. The AmsiScanBuffer function provides us the hooks and functionality we need to access the pointer/buffer for the response code.
