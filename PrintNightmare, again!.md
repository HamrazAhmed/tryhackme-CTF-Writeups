---
Search the artifacts on the endpoint to determine if the employee used any of the Windows Printer Spooler vulnerabilities to elevate their privileges. 
---

# PrintNightmare, again! — Writeup

## Overview
### PrintNightmare, again! — Writeup
### PrintNightmare, again! — Writeup
### Detection
![|333](https://i.ibb.co/ryX9w7H/businessmen-in-the-work-office-meeting-on-global-planning-and-marketing-research-vector-illustration.jpg)
Scenario: In the weekly internal security meeting it was reported that an employee overheard two co-workers discussing the PrintNightmare exploit and how they can use it to elevate their privileges on their local computers.
Task: Inspect the artifacts on the endpoint to detect the exploit they used.
Note: Use the FullEventLogView tool. Go to Options > Advanced Options and set Show events from all times.
If you need a refresher on PrintNightmare, see our previous PrintNightmare room!
```text
using fulleventlogview 
Go to Options > Advanced Options and set Show events from all times
and filter with event id like 316,808,811,31017,7031,3,11

use find and search for zip

File created:
RuleName: Downloads
UtcTime: 2021-08-27 09:52:07.311
ProcessGuid: {a19e3d6a-b595-6128-0901-000000000d00}
ProcessId: 2124
Image: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
TargetFilename: C:\Users\bmurphy\Downloads\levelup.zip
CreationUtcTime: 2021-08-27 09:52:07.311

File created:
RuleName: Downloads
UtcTime: 2021-08-27 09:52:27.520
ProcessGuid: {a19e3d6a-b595-6128-0901-000000000d00}
ProcessId: 2124
Image: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
TargetFilename: C:\Users\bmurphy\Downloads\CVE-2021-1675-main\CVE-2021-1675.ps1
CreationUtcTime: 2021-08-27 09:52:27.520

File created:
RuleName: DLL
UtcTime: 2021-08-27 09:53:38.066
ProcessGuid: {a19e3d6a-b595-6128-0901-000000000d00}
ProcessId: 2124
Image: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
TargetFilename: C:\Users\bmurphy\AppData\Local\Temp\3\nightmare.dll
CreationUtcTime: 2021-08-27 09:53:38.066

File created:
RuleName: DLL
UtcTime: 2021-08-27 09:53:38.566
ProcessGuid: {a19e3d6a-aea6-6128-3600-000000000d00}
ProcessId: 2600
Image: C:\Windows\System32\spoolsv.exe
TargetFilename: C:\Windows\System32\spool\drivers\x64\3\New\nightmare.dll
CreationUtcTime: 2021-08-27 09:53:38.566

Process '\Device\HarddiskVolume2\Windows\System32\spoolsv.exe' (PID 2600) would have been blocked from loading the non-Microsoft-signed binary '\Windows\System32\spool\drivers\x64\3\nightmare.dll'.

show all event views to see primary registry path .. find HKLM

event id 13
quick filter HKLM
or THMPrinter
