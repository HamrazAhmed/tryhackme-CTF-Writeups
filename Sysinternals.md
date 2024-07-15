---
Learn to use the Sysinternals tools to analyze Window systems or applications.
---

# Sysinternals — Writeup

## Overview
### Sysinternals — Writeup
### Sysinternals — Writeup
![|222](https://tryhackme-images.s3.amazonaws.com/room-icons/c27aa60ea78798c327dbacc9688b62c3.png)
### Introduction
What are the tools known as Sysinternals?
The Sysinternals tools is a compilation of over 70+ Windows-based tools. Each of the tools falls into one of the following categories:
File and Disk Utilities
Networking Utilities
Process Utilities
Security Utilities
System Information
Miscellaneous
The Sysinternals tools and its website (sysinternals.com) were created by Mark Russinovich back in the late '90s, along with an individual named Bryce Cogswell under the company Wininternals Software.
In 2006, Microsoft acquired Wininternals Software, and Mark Russinovich joined Microsoft. Today he is the CTO of Microsoft Azure.
Mark Russinovich made headlines when he reported that Sony embedded rootkits into their music CDs back in 2005. This discovery was made known thanks to one of the Sysinternals tools he was testing. You can read more about that [here](https://www.virusbulletin.com/virusbulletin/2005/12/inside-sony-s-rootkit).
He also discovered in 2006 that Symantec was using rootkit-like technology. You can read more about that [here](https://www.zdnet.com/article/symantec-confesses-to-using-rootkit-technology/).
The Sysinternals tools are extremely popular among IT professionals who manage Windows systems. These tools are so popular that even red teamers and adversaries alike use them. Throughout this room, I'll note which tools MITRE has identified to have been used by adversaries.
The goal of this room is to introduce you to a handful of Sysinternals tools with the hopes that you will expand on this knowledge with your own research and curiosity.
Hopefully, you can add Sysinternals to your toolkit, as many already have.
Machine IP: MACHINE_IP
User: administrator
Password: letmein123!
When did Microsoft acquire the Sysinternals tools?
*2006*
### Install the Sysinternals Suite
Time to get our hands dirty with Sysinternals.
The Sysinternals tool(s) can be downloaded and run from the local system, or the tool(s) can be run from the web.
Regarding local install/run, you can download the entire suite or just the tool(s) you need.
If you wish to download a tool or two but not the entire suite, you can navigate to the Sysinternals Utilities Index page, https://docs.microsoft.com/en-us/sysinternals/downloads/, and download the tool(s). If you know which tool you want to download, then this is fine. The tools are listed in alphabetical order are not separated by categories.
![](https://assets.tryhackme.com/additional/sysinternals/sysint-util-index.png)
Alternatively, you can use the category links to find and download the tool(s). This route is better since there are so many tools you can focus on all the tools of interest instead of the entire index.
For example, let's say you need tools to inspect Windows processes; then, you can navigate to the Process Utilities page, https://docs.microsoft.com/en-us/sysinternals/downloads/process-utilities/, for all the tools that fall under this category.
![](https://assets.tryhackme.com/additional/sysinternals/sysint-proc-util.png)
Notice that you are conveniently supplied with a brief explanation for each tool.
Lastly, you can do the same from the Sysinternals Live URL, https://live.sysinternals.com/. This is the same URL to use if you wish to run the tool from the web. We will look at how to accomplish this in the next section.
If you chose to download from this page, it is similar to the Sysinternals Utilities Index page. The tools are listed in alphabetical order and are not separated by categories.
![](https://assets.tryhackme.com/additional/sysinternals/sysint-live-index.png)
If you wish to download the Sysinternals Suite, you can download the zip file from here.
The suite has a select number of Sysinternal tools. See below for a rundown of the tools included in the suite.
![](https://assets.tryhackme.com/additional/sysinternals/sysint-suite.png)
After you download the zip file, you need to extract the files. After the files are extracted, the extra step, which is by choice, is to add the folder path to the environment variables. By doing so, you can launch the tools via the command line without navigating to the directory the tools reside in.
Environment Variables can be edited from System Properties.
The System Properties can be launched via the command line by running sysdm.cpl. Click on the Advanced tab.
![](https://assets.tryhackme.com/additional/sysinternals/env-variables.png)
Select Path under System Variables and select Edit... then OK.
![](https://assets.tryhackme.com/additional/sysinternals/env-variables2.png)
In the next screen select New and enter the folder path where the Sysinternals Suite was extracted to. Press OK to confirm the changes.
![](https://assets.tryhackme.com/additional/sysinternals/env-variables3.png)
Open a new command prompt (elevated) to confirm that the Sysinternals Suite can be executed from any location.
![](https://assets.tryhackme.com/additional/sysinternals/env-variables4.png)
A local copy of the Sysinternals Suite is located in `C:\Tools\Sysint`.
Alternatively, a PowerShell module can download and install all of the Sysinternals tools.
PowerShell command: Download-SysInternalsTools C:\Tools\Sysint
Now let's look at how to run the Sysinternals tools from the web.
What is the last tool listed within the Sysinternals Suite?
*ZoomIt*
### Using Sysinternals Live
Per the Sysinternals website, "Sysinternals Live is a service that enables you to execute Sysinternals tools directly from the Web without hunting for and manually downloading them. Simply enter a tool's Sysinternals Live path into Windows Explorer or a command prompt as `live.sysinternals.com/<toolname> or  \\live.sysinternals.com\tools\<toolname>`."
Let's take a look at how we can do this.
Based on the instructions, to launch Process Monitor from the web the syntax is `\\live.sysinternals.com\tools\procmon.exe`.
And it fails.
![](https://assets.tryhackme.com/additional/sysinternals/sysint-live-fail.png)
To resolve this issue the WebDAV client must be installed and running on the machine. The WebDAV protocol is what allows a local machine to access a remote machine running a WebDAV share and perform actions in it.
On a Windows 10 client, the WebDAV client is installed but the client is most likely not running. If you try to run a Sysinternals tool it will fail with a message "The network path was not found."
![](https://assets.tryhackme.com/additional/sysinternals/win10-webclient1b.png)
The service needs to be started before attempting to call any Sysinternals tool in this fashion.
![](https://assets.tryhackme.com/additional/sysinternals/win10-webclient2.png)
Verify it's running before proceeding.
![](https://assets.tryhackme.com/additional/sysinternals/win10-webclient3.png)
Also, Network Discovery needs to be enabled as well. This setting can be enabled in the Network and Sharing Center.
There are a few ways to open the Network and Sharing Center. Here is a neat command line to launch it.
![](https://assets.tryhackme.com/additional/sysinternals/network-and-sharing.png)
Click on Change advanced sharing settings and select Turn on network discovery for your current network profile.
The attached VM is a Windows Server 2019 edition. The WebDAV client is not installed by default.
The feature to install on Windows Server is WebDAV Redirector. This feature can be installed via Server Manager or using PowerShell.
To install with PowerShell, `Install-WindowsFeature WebDAV-Redirector –Restart`. The server needs to reboot for the installation to complete.
After reboot, the installation can be verified with the following PowerShell command, `Get-WindowsFeature WebDAV-Redirector | Format-Table –Autosize`.
![](https://assets.tryhackme.com/additional/sysinternals/win2019-webclient1.png)
The same process as with a Windows 10 client applies from this point:
Make sure the WebClient service is running
Make sure Network Discovery is enabled
Now with all the necessary components installed and enabled the local machine is ready to run Sysinternals tools from the web.
There are 2 ways the tools can be run:
Run the tool from the command line (as shown above from the Windows 10 machine)
Create a network drive and run the tool from the mapped drive
Method 1 - Run tool from command line
![](https://assets.tryhackme.com/additional/sysinternals/win2019-method1.png)
Method 2 - Run tool from a mapped drive
![](https://assets.tryhackme.com/additional/sysinternals/win2019-method2a.png)
Note: The asterick will auto-assign a drive letter. The asterick can be replaced with an actual drive letter instead.
![](https://assets.tryhackme.com/additional/sysinternals/win2019-method2b.png)
The website is now browsable within the local machine.
![](https://assets.tryhackme.com/additional/sysinternals/win2019-method2c.png)
![](https://assets.tryhackme.com/additional/sysinternals/win2019-method2d.png)
Now that we got that out of the way time to start exploring some of these tools.
What service needs to be enabled on the local host to interact with live.sysinternals.com?
*webclient*
### File and Disk Utilities
Each task within this room will focus on 1 or 2 tools per section (maybe more).
Again, the goal is to introduce you to the Sysinternals tools, but there are far too many tools to go into each tool in depth.
Sigcheck
"Sigcheck is a command-line utility that shows file version number, timestamp information, and digital signature details, including certificate chains. It also includes an option to check a file’s status on VirusTotal, a site that performs automated file scanning against over 40 antivirus engines, and an option to upload a file for scanning." (official definition)
![](https://assets.tryhackme.com/additional/sysinternals/sigcheck1.png)
(https://docs.microsoft.com/en-us/sysinternals/downloads/sigcheck)
From the official Sigcheck page, a use case is identified towards the bottom of the page.
If you completed the Core Windows Processes room you should be aware that the location of all the executables is `C:\Windows\System32, except for Explorer.exe (which is C:\Windows)`.
Use Case: Check for unsigned files in `C:\Windows\System32`.
Command: `sigcheck -u -e C:\Windows\System32`
![](https://assets.tryhackme.com/additional/sysinternals/sigcheck2.png)
Parameter usage:
-u "If VirusTotal check is enabled, show files that are unknown by VirusTotal or have non-zero detection, otherwise show only unsigned files."
-e "Scan executable images only (regardless of their extension)"
Note: If the results were different it would warrant an investigation into any listed executables.
Streams
"The NTFS file system provides applications the ability to create alternate data streams of information. By default, all data is stored in a file's main unnamed data stream, but by using the syntax 'file:stream', you are able to read and write to alternates." (official definition)
Alternate Data Streams (ADS) is a file attribute specific to Windows NTFS (New Technology File System). Every file has at least one data stream ($DATA) and ADS allows files to contain more than one stream of data. Natively Window Explorer doesn't display ADS to the user. There are 3rd party executables that can be used to view this data, but Powershell gives you the ability to view ADS for files.
Malware writers have used ADS to hide data in an endpoint, but not all its uses are malicious. When you download a file from the Internet unto an endpoint, there are identifiers written to ADS to identify that it was downloaded from the Internet.
![](https://assets.tryhackme.com/additional/sysinternals/streams1.png)
Example: A file downloaded from the Internet.
![](https://assets.tryhackme.com/additional/sysinternals/streams2.png)
Since the file has this identifier, additional security measures are added to its properties.
You can read more on streams [here].
SDelete
"SDelete is a command line utility that takes a number of options. In any given use, it allows you to delete one or more files and/or directories, or to cleanse the free space on a logical disk."
As per the official documentation page, SDelete (Secure Delete) implemented the DOD 5220.22-M (Department of Defense clearing and sanitizing protocol).
![](https://assets.tryhackme.com/additional/sysinternals/sdelete.png)
Source: https://www.lifewire.com/dod-5220-22-m-2625856
SDelete has been used by adversaries and is associated with MITRE techniques [T1485](https://attack.mitre.org/techniques/T1485/) (Data Destruction) and [T1070.004](https://attack.mitre.org/techniques/T1070/004/) (Indicator Removal on Host: File Deletion). It's MITRE ID [S0195](https://attack.mitre.org/software/S0195/).
You can review this tool more in-depth by visiting its Sysinternals SDelete [page](https://docs.microsoft.com/en-us/sysinternals/downloads/sdelete).
Other tools fall under the File and Disk Utilities category. I encourage you to explore these tools at your own leisure.
Link: https://docs.microsoft.com/en-us/sysinternals/downloads/file-and-disk-utilities
There is a txt file on the desktop named file.txt. Using one of the three discussed tools in this task, what is the text within the ADS?
(Use the streams command to find the stream file name. Use "`notepad .\file.txt:example.txt`" to open the stream file.)
```text
C:\Users\Administrator>cd Desktop

C:\Users\Administrator\Desktop>streams file.txt

streams v1.60 - Reveal NTFS alternate streams.
Copyright (C) 2005-2016 Mark Russinovich
Sysinternals - www.sysinternals.com

C:\Users\Administrator\Desktop\file.txt:
         :ads.txt:$DATA 26

C:\Users\Administrator\Desktop>notepad file.txt:ads.txt

in notepad I am hiding in the stream.
```
![[Pasted image 20220902193253.png]]
*I am hiding in the stream.*
### Networking Utilities
TCPView
"TCPView is a Windows program that will show you detailed listings of all TCP and UDP endpoints on your system, including the local and remote addresses and state of TCP connections. On Windows Server 2008, Vista, and XP, TCPView also reports the name of the process that owns the endpoint. TCPView provides a more informative and conveniently presented subset of the Netstat program that ships with Windows. The TCPView download includes Tcpvcon, a command-line version with the same functionality." (official definition)
This is a good time to mention that Windows has a built-in utility that provides the same functionality. This tool is called Resource Monitor. There are many ways to open this tool. From the command line use `resmon`.
![](https://assets.tryhackme.com/additional/sysinternals/resource-monitor0.png)
Expand TCP Connections to view the Remote Address for each Process with an outbound connection.
![](https://assets.tryhackme.com/additional/sysinternals/resource-monitor.png)
This tool can also be called from the Performance tab within Task Manager. Look at the bottom left for the link to open Resource Monitor.
![](https://assets.tryhackme.com/additional/sysinternals/resource-monitor2.png)
Now back to TCPView.
![](https://assets.tryhackme.com/additional/sysinternals/tcpview.png)
The below image shows the default view for TCPView.
