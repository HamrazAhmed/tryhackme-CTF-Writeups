# Conti — Writeup

## Overview
### Conti — Writeup
### Conti — Writeup
----
An Exchange server was compromised with ransomware. Use Splunk to investigate how the attackers compromised the server.
----
![](https://assets.tryhackme.com/additional/conti/conti-room-banner.png)
![](https://tryhackme-images.s3.amazonaws.com/room-icons/efe12f2572d7ed0e3d94c37c00560bdc.png)
### SITREP
Some employees from your company reported that they can’t log into Outlook. The Exchange system admin also reported that he can’t log in to the Exchange Admin Center. After initial triage, they discovered some weird readme files settled on the Exchange server.
Below is a copy of the ransomware note.
**Warning**: Do **NOT** attempt to visit and/or interact with any URLs displayed in the ransom note.
Read the latest on the Conti ransomware [here](https://www.bleepingcomputer.com/news/security/fbi-cisa-and-nsa-warn-of-escalating-conti-ransomware-attacks/).
---
Connect to OpenVPN or use the AttackBox to access the attached Splunk instance.
Splunk Interface Credentials:
**Username**: `bellybear`
**Password**: `password!!!`
**Splunk URL**: `http://10.10.77.154:8000`
Special thanks to [Bohan Zhang](https://www.linkedin.com/in/bohansec?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAACFkYBwB9L43-CozJsTYeFoIV29KBlKU9qc&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3BWgzBOFb8RQWd%2B24UFVSw%2Fw%3D%3D) for this challenge.
Answer the questions below
Start the attached virtual machine.
Question Done
### Exchange Server Compromised
Start Machine
Below are the error messages that the Exchange admin and employees see when they try to access anything related to Exchange or Outlook.
**Exchange Control Panel**:
**Outlook Web Access**:
**Task**: You are assigned to investigate this situation. Use Splunk to answer the questions below regarding the Conti ransomware.
Answer the questions below
```text
select all time

filter: index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational"

https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon

Event ID 11: FileCreate

File create operations are logged when a file is created or overwritten. This event is useful for monitoring autostart locations, like the Startup folder, as well as temporary and download directories, which are common places malware drops during initial infection.

index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=11

c:\Users\Administrator\Documents\cmd.exe

more fields choose Hashes then filter

index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" Image="c:\\Users\\Administrator\\Documents\\cmd.exe"

MD5=290C7DFB01E50CEA9E19DA81A781AF2C,SHA256=53B1C1B2F41A7FC300E97D036E57539453FF82001DD3F6ABF07F4896B1F9CA22,IMPHASH=23F815785DB238377F4513BE54DBA574

or just 

index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" Image="c:\\Users\\Administrator\\Documents\\cmd.exe" md5

index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=11 | stats count by TargetFilename

stats (statistics)

C:\Users\.NET v4.5 Classic\Downloads\readme.txt

index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" CommandLine="*/add*" 
| stats count by CommandLine

net user /add securityninja hardToHack123$

Event ID 8: CreateRemoteThread

The `CreateRemoteThread` event detects when a process creates a thread in another process. This technique is used by malware to inject code and hide in other processes. The event indicates the source and target process. It gives information on the code that will be run in the new thread: `StartAddress`, `StartModule` and `StartFunction`. Note that `StartModule` and `StartFunction` fields are inferred, they might be empty if the starting address is outside loaded modules or known exported functions.

index=main sourcetype="WinEventLog:Microsoft-Windows-Sysmon/Operational" EventCode=8 | table SourceImage, TargetImage
