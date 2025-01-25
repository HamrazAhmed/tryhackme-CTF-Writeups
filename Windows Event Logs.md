---
Introduction to Windows Event Logs and the tools to query them.
---

# Windows Event Logs — Writeup

## Overview
### Windows Event Logs — Writeup
### Windows Event Logs — Writeup
![|222](https://tryhackme-images.s3.amazonaws.com/room-icons/09ca5c3caddabd224011e2269153745e.png)
### What are event logs?
Per Wikipedia, "Event logs record events taking place in the execution of a system to provide an audit trail that can be used to understand the activity of the system and to diagnose problems. They are essential to understand the activities of complex systems, particularly in applications with little user interaction (such as server applications)."
This definition would apply to system administrators, IT technicians, desktop engineers, etc. If the endpoint is experiencing an issue, the event logs can be queried to see any clues about what led to the issue. The operating system, by default, writes messages to these logs.
As defenders (blue teamers), there is another use case for event logs. "It can also be useful to combine log file entries from multiple sources. This approach, in combination with statistical analysis, may yield correlations between seemingly unrelated events on different servers."
This is where SIEMs (Security information and event management) such as Splunk and Elastic come into play.
If you don't know exactly what a SEIM is used for, below is a visual overview of its capabilities. (Image credit: Varonis)
![](https://assets.tryhackme.com/additional/win-event-logs/siem.png)
Even though it's possible to access a remote machine's event logs, this will not be feasible with a large enterprise environment. Instead, one can view the logs from all the endpoints, appliances, etc., in a SIEM. This will allow you to query the logs from multiple devices instead of manually connecting to a single device to view its logs.
Windows is not the only operating system that uses a logging system. Linux and macOS do as well. For example, on Linux systems, the logging system is known as Syslog. Within this room, though, we're only focusing on the Windows logging system called Windows Event Logs.
Room Machine
Before moving forward, please deploy the machine.
You can use the AttackBox and Remmina to connect to the remote machine. Make sure the remote machine is deployed before proceeding.
Click on the plus icon, as shown below.
![](https://assets.tryhackme.com/additional/sam-aoc2020/remmina5.png)
For Server provide (MACHINE_IP) as the IP address provided to you for the remote machine. The credentials for the user account is:
User name: administrator
User password: blueT3aming!
![](https://assets.tryhackme.com/additional/win-event-logs/remmina.png)
Accept the Certificate when prompted, and you should be logged into the remote system now.
Note: The virtual machine may take up to 3 minutes to load.
Let's begin...
*No answer needed*
### Event Viewer
The Windows Event Logs are not text files that can be viewed using a text editor. However, the raw data can be translated into XML using the Windows API. The events stored in these log files are stored in a proprietary binary format with a .evt or .evtx extension. The log files with the .evtx file extension typically reside in `C:\Windows\System32\winevt\Logs`.
There are 3 main ways of accessing these event logs within a Windows system:
Event Viewer (GUI-based application)
Wevtutil.exe (command-line tool)
Get-WinEvent (PowerShell cmdlet)
Each method of accessing the event logs has its pros and cons. In this section, we'll look at the Event Viewer first.
In any Windows system, the Event Viewer (an MMC [Microsoft Management Console] snap-in) can be launched by simply right-clicking the Windows icon in the taskbar and selecting Event Viewer.
![](https://assets.tryhackme.com/additional/win-event-logs/start-event-viewer.png)
For the savvy sysadmins that use the CLI much of their day, Event Viewer can be launched by typing eventvwr.msc.
Event Viewer has 3 panes.
The pane on the left provides a hierarchical tree listing of the event log providers.
The pane in the middle will either display a general overview and summary or the events specific to a selected provider.
The pane on the right is the actions pane.
There are 5 types of events that can be logged. Below is a table from docs.microsoft.com providing a brief description for each.
![](https://assets.tryhackme.com/additional/win-event-logs/five-event-types.png)
On the left pane, the standard logs are visible under Windows Logs. Below is a table from docs.microsoft.com providing a brief description for each.
![](https://assets.tryhackme.com/additional/win-event-logs/standard-event-logs.png)
The next section is the Applications and Services Logs. Expand this section and drill down on Microsoft > Windows > PowerShell > Operational.
PowerShell will log operations from the engine, providers, and cmdlets to the Windows event log.
Right-click on Operational then Properties.
![](https://assets.tryhackme.com/additional/win-event-logs/operational-properties.png)
Within Properties, you see the log location, log size, and when it was created, modified, and last accessed. Within the Properties window, you can also see the maximum set log size and what action to take once the criteria are met. This concept is known as log rotation. These are discussions held with corporations of various sizes. How long to keep logs and when it's permissible to overwrite the logs with new data.
Lastly, notice the Clear Log button at the bottom right. There are legitimate reasons to use this button, but adversaries will likely attempt to clear the logs to go undetected.  Note: This is not the only method to clear the event logs for any given event provider.
Focus your attention on the middle pane. Remember from earlier that this pane will display the events specific to a selected provider. In this case, PowerShell/Operational.
![](https://assets.tryhackme.com/additional/win-event-logs/posh-operational-1b.png)
From the above image, notice the event provider's name and the number of events logged. In this case, there are 44 events logged. You might see a different number. No worries, though.
A brief explanation for each column:
The first column is Level, which is the event type. Recall from earlier there are 5 different event types. This first entry is labeled as Information.
Next is Date and Time, which is when the event was logged.
The third column Source is the name of the software that logs the event. From the above image, the source is PowerShell.
Events are identified by IDs (Event ID), which is the fourth column. Note that Event IDs are not unique. Meaning that Event ID 4103 in the above image is related to Executing Pipeline but will have an entirely different meaning in another event log.
Lastly is Task Category, which is an Event Category. This entry will help you organize events so Event Viewer can filter them. The event source defines this column.
The middle pane has a split view. For any event, you click on the event, and more information is displayed in the bottom half of the middle pane.
This section has 2 tabs: General and Details.
General is the default view, and the rendered data is displayed.
The Details view has 2 options: Friendly view and XML view.
Below is a snippet of the General view.
![](https://assets.tryhackme.com/additional/win-event-logs/posh-operational-3.png)
Lastly, take a look at the Actions pane. There are several options available, but we'll only focus on a few. Please examine all the actions that can be performed at your own leisure if you're not familiar with MMC snap-ins.
As you should have noticed, within the Actions pane, you can open a saved log. This is useful if the remote machine can't be accessed. The logs can be provided to the analyst.  You will perform this action a little later.
The Create Custom View and Filter Current Log are nearly identical. The only difference between the 2 is that the By log and By source radio buttons are grayed out in Filter Current Log. Reason for that? The filter you can make with this specific action only relates to the current log. Hence no reason for 'by log' or 'by source' to be enabled.
Why are these actions useful? Say, for instance, you don't want all the events associated with PowerShell/Operational cluttering all the real estate in the pane. Maybe you're only interested in 4104 events. That is possible with these 2 actions.
To view event logs from another computer, right-click Event Viewer (Local) > Connect to Another Computer...
![](https://assets.tryhackme.com/additional/win-event-logs/remote-computer.png)
That will conclude the general overview of the Event Viewer—time to become familiar with the tool.
Note: Don't forget to deploy the machine for this room before proceeding. Give the room about 3 minutes to fully load.
For the questions below, use Event Viewer to analyze Microsoft-Windows-PowerShell/Operational log.
*No answer needed*
What is the Event ID for the first event?
*40961*
Filter on Event ID 4104. What was the 2nd command executed in the PowerShell session?
*whoami*
What is the Task Category for Event ID 4104?
*Execute a Remote Command*
For the questions below, use Event Viewer to analyze the Windows PowerShell log.
*No answer needed*
What is the Task Category for Event ID 800?*Pipeline Execution Details*
### wevtutil.exe
Ok, you played around with Event Viewer. Imagine you have to sit there and manually sift through hundreds or even thousands of events (even after filtering the log). Not fun. It would be nice if you could write scripts to do this work for you. We will explore some tools that will allow you to query event logs via the command line and/or PowerShell.
Let's look at wevtutil.exe first. Per Microsoft, the wevtutil.exe tool "enables you to retrieve information about event logs and publishers. You can also use this command to install and uninstall event manifests, to run queries, and to export, archive, and clear logs."
As with any tool, access its help files to find out how to run the tool. An example of a command to do this is wevtutil.exe /?.
![](https://assets.tryhackme.com/additional/win-event-logs/wevtutil2.png)
From the above screenshot, under Usage, you are provided a brief example of how to use the tool.
In this example, ep (enum-publishers) is used. This is a command for wevtutil.exe.
The other commands are...
![](https://assets.tryhackme.com/additional/win-event-logs/wevtutil-commands.png)
Lastly, within the help information for wevtutil.exe are Common options.
![](https://assets.tryhackme.com/additional/win-event-logs/wevtutil-options.png)
Notice at the bottom of the above snapshot, wevtutil COMMAND /?. This will provide additional information specific to a command.
Let's get more information on the command qe (query-events).
![](https://assets.tryhackme.com/additional/win-event-logs/wevtutil-query-events.png)
Look over the information within the help menu to fully understand how to use this command.
Ok, great! You have enough information to use this tool—time to answer some questions. It is always recommended to look into the tool and its related information at your own leisure.
Note: You can get more information about using this tool further but visiting the online help documentation docs.microsoft.com.
```text
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\Administrator> wevtutil.exe el | Measure-Object

Count    : 1071
Average  :
Sum      :
Maximum  :
Minimum  :
Property :
```
How many log names are in the machine?
*1071*
What is the definition for the query-events command?
*Reads events from an event log, from a log file, or using a structured query.*
What option would you use to provide a path to a log file?
*/lf:true*
What is the VALUE for /q?
*XPATH query*
The questions below are based on this command: wevtutil qe Application /c:3 /rd:true /f:text *No answer needed*
```text
PS C:\Users\Administrator> wevtutil qe Application /c:3 /rd:true /f:text
Event[0]:
  Log Name: Application
  Source: Microsoft-Windows-Security-SPP
  Event ID: 16384
  Task: N/A
  Level: Information
  Opcode: N/A
  Keyword: Classic
  User: N/A
  User Name: N/A
  Computer: WIN-1O0UJBNP9G7
  Description:
Successfully scheduled Software Protection service for re-start at 2022-09-12T00:51:13Z. Reason: RulesEngine.

Event[1]:
  Log Name: Application
  Source: Microsoft-Windows-Security-SPP
  Event ID: 16394
  Task: N/A
  Level: Information
  Opcode: N/A
  Keyword: Classic
  User: N/A
  User Name: N/A
  Computer: WIN-1O0UJBNP9G7
  Description:
Offline downlevel migration succeeded.

Event[2]:
  Log Name: Application
  Source: Desktop Window Manager
  Event ID: 9027
  Task: N/A
  Level: Information
  Opcode: N/A
  Keyword: Classic
  User: N/A
  User Name: N/A
  Computer: WIN-1O0UJBNP9G7
  Description:
The Desktop Window Manager has registered the session port.
```
What is the log name? *Application*
What is the /rd option for? *Event read direction*
What is the /c option for? *Maximum number of events to read*
### Get-WinEvent
On to the next tool. Now we'll examine a PowerShell cmdlet called Get-WinEvent. Per Microsoft, the Get-WinEvent cmdlet "gets events from event logs and event tracing log files on local and remote computers."
A more detailed explanation:
![](https://assets.tryhackme.com/additional/win-event-logs/get-winevent-desc.png)
Note: The Get-WinEvent cmdlet replaces the Get-EventLog cmdlet.
As with any new tool, in this case that tool is a PowerShell cmdlet; it's good practice to read the Get-Help documentation to become acquainted with its capabilities. Please refer to the Get-Help information online [docs.microsoft.com](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent?view=powershell-5.1).
Look over the examples provided in the Get-Help documentation. Some tasks might require some PowerShell-fu, while others don't. Even if your PowerShell-fu is not up to par, fret not; each example has a detailed explanation of the commands/cmdlets used.
Let's talk a bit about filtering.
Generally speaking, you can filter event logs as such `Get-WinEvent -LogName Application | Where-Object { $_.ProviderName -Match 'WLMS' }`.
![](https://assets.tryhackme.com/additional/win-event-logs/wlms.png)
Tip: If you are ever working on a Windows evaluation virtual machine that is cut off from the Internet eventually, it will shut down every hour. ;^)
When working with large event logs, per Microsoft, it's inefficient to send objects down the pipeline to a Where-Object command. The use of the Get-WinEvent cmdlet's FilterHashtable parameter is recommended to filter event logs.
The image below is of the same command a few lines above but instead of using the Where-Object cmdlet the FilterHashtable is used instead.
![](https://assets.tryhackme.com/additional/win-event-logs/wlms-2.png)
In case you're wondering, the results will between the 2 commands above are the same.
The syntax of a hash table is as follows: ![](https://assets.tryhackme.com/additional/win-event-logs/hash-table-2.png)
Guidelines for defining a hash table is as follows:
![](https://assets.tryhackme.com/additional/win-event-logs/hash-table.png)
Note: You don't need to use a semicolon if you separate each key/value with a new line as in the screenshot above for the -FilterHashtable for `ProviderName='WLMS'`.
Below is a table that displays the accepted key/value pairs for the Get-WinEvent FilterHashtable parameter.
![](https://assets.tryhackme.com/additional/win-event-logs/filter-hashtable.png)
When building a query with a hash table, Microsoft recommends building the hash table one key-value pair at a time.
Event Viewer can provide quick information on what you need to build your hash table.
![](https://assets.tryhackme.com/additional/win-event-logs/build-hash-table.png)
Based on this information, the hash table will look as follows:
![](https://assets.tryhackme.com/additional/win-event-logs/msi-installer.png)
For more information on creating Get-WinEvent queries with FilterHashtable, check the official Microsoft documentation docs.microsoft.com.
Since we're on the topic of Get-WinEvent and FilterHashtable, here is a command that you might find useful (shared by @mubix):
```text
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-PowerShell/Operational'; ID=4104} | Select-Object -Property Message | Select-String -Pattern 'SecureString'
```
You can read more about creating hash tables in general [docs.microsoft.com](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_hash_tables?view=powershell-7.2&viewFallbackFrom=powershell-7.1).
Answer the following questions using the [online](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/Get-WinEvent?view=powershell-7.2&viewFallbackFrom=powershell-7.1) help documentation for Get-WinEvent *No answer needed*
```text
Microsoft-Windows-Containers-Wcifs/Operational
Circular             1052672           0 Microsoft-Windows-Containers-Wcnfs/Operational
Circular             1052672           0 Microsoft-Windows-CoreApplication/Operational
Circular             1052672           0 Microsoft-Windows-CorruptedFileRecovery-Client/Operational
Circular             1052672           0 Microsoft-Windows-CorruptedFileRecovery-Server/Operational
Circular             1052672           0 Microsoft-Windows-Crypto-DPAPI/BackUpKeySvc
Circular             1052672             Microsoft-Windows-Crypto-DPAPI/Debug
Circular             1052672          48 Microsoft-Windows-Crypto-DPAPI/Operational
Circular             1052672             Microsoft-Windows-Crypto-NCrypt/Operational
Circular             1052672           0 Microsoft-Windows-DAL-Provider/Operational
Circular             1052672           6 Microsoft-Windows-DataIntegrityScan/Admin
Circular             1052672           0 Microsoft-Windows-DataIntegrityScan/CrashRecovery
Circular             1052672           0 Microsoft-Windows-DateTimeControlPanel/Operational
Circular             1052672           0 Microsoft-Windows-DeviceGuard/Operational
Circular             1052672           1 Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider/Admin
Circular             1052672           0 Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider/Operational
Circular             1052672           0 Microsoft-Windows-Devices-Background/Operational
Circular             1052672        1228 Microsoft-Windows-DeviceSetupManager/Admin
Circular             1052672          68 Microsoft-Windows-DeviceSetupManager/Operational
Circular             1052672           0 Microsoft-Windows-DeviceSync/Operational
Circular             1052672           0 Microsoft-Windows-DeviceUpdateAgent/Operational
Circular             1052672           4 Microsoft-Windows-Dhcp-Client/Admin
Circular             1052672             Microsoft-Windows-Dhcp-Client/Operational
Circular             1052672           0 Microsoft-Windows-Dhcpv6-Client/Admin
Circular             1052672             Microsoft-Windows-Dhcpv6-Client/Operational
Circular             1052672          19 Microsoft-Windows-Diagnosis-DPS/Operational
Circular             1052672           0 Microsoft-Windows-Diagnosis-PCW/Operational
Circular             1052672           0 Microsoft-Windows-Diagnosis-PLA/Operational
Circular             1052672          21 Microsoft-Windows-Diagnosis-Scheduled/Operational
Circular             1052672           3 Microsoft-Windows-Diagnosis-Scripted/Admin
Circular             1052672          12 Microsoft-Windows-Diagnosis-Scripted/Operational
Circular             1052672           0 Microsoft-Windows-Diagnosis-ScriptedDiagnosticsProvider/Operational
Circular             1052672           0 Microsoft-Windows-Diagnostics-Networking/Operational
Circular             1052672           0 Microsoft-Windows-DirectoryServices-Deployment/Operational
Circular             1052672           0 Microsoft-Windows-DiskDiagnostic/Operational
Circular             1052672           0 Microsoft-Windows-DiskDiagnosticDataCollector/Operational
Circular             1052672           0 Microsoft-Windows-DiskDiagnosticResolver/Operational
Circular             1052672             Microsoft-Windows-DisplayColorCalibration/Operational
Circular             1052672             Microsoft-Windows-DNS-Client/Operational
Circular             1052672             Microsoft-Windows-DriverFrameworks-UserMode/Operational
Circular             1052672           0 Microsoft-Windows-DSC/Admin
Circular             1052672           0 Microsoft-Windows-DSC/Operational
Circular             1052672           0 Microsoft-Windows-EapHost/Operational
Circular             1052672           0 Microsoft-Windows-EapMethods-RasChap/Operational
Circular             1052672           0 Microsoft-Windows-EapMethods-RasTls/Operational
Circular             1052672           0 Microsoft-Windows-EapMethods-Sim/Operational
Circular             1052672           0 Microsoft-Windows-EapMethods-Ttls/Operational
Circular             1052672           0 Microsoft-Windows-EDP-Application-Learning/Admin
Circular             1052672           0 Microsoft-Windows-EDP-Audit-Regular/Admin
Circular             1052672           0 Microsoft-Windows-EDP-Audit-TCB/Admin
Circular             1052672           0 Microsoft-Windows-EnrollmentPolicyWebService/Admin
Circular             1052672           0 Microsoft-Windows-EnrollmentWebService/Admin
Circular             1052672             Microsoft-Windows-ESE/Operational
Circular             1052672           0 Microsoft-Windows-EventCollector/Operational
Circular             1052672           0 Microsoft-Windows-Fault-Tolerant-Heap/Operational
Circular             1052672           0 Microsoft-Windows-FeatureConfiguration/Operational
Circular             1052672           0 Microsoft-Windows-FederationServices-Deployment/Operational
Circular             1052672           0 Microsoft-Windows-FileServices-ServerManager-EventProvider/Admin
Circular             1052672           0 Microsoft-Windows-FileServices-ServerManager-EventProvider/Operational
Circular             1052672           0 Microsoft-Windows-FileShareShadowCopyProvider/Operational
Circular             1052672           0 Microsoft-Windows-FMS/Operational
Circular             4194304           0 Microsoft-Windows-Folder Redirection/Operational
Circular             1052672          19 Microsoft-Windows-Forwarding/Operational
Circular             1052672           0 Microsoft-Windows-GenericRoaming/Admin
Circular             1052672             Microsoft-Windows-glcnd/Admin
Circular             4194304        1031 Microsoft-Windows-GroupPolicy/Operational
Circular             1052672         223 Microsoft-Windows-HelloForBusiness/Operational
Circular             1052672           0 Microsoft-Windows-Help/Operational
Circular             1052672           0 Microsoft-Windows-HomeGroup Control Panel/Operational
Circular             1052672             Microsoft-Windows-HttpService/Log
Circular             1052672             Microsoft-Windows-HttpService/Trace
Circular             1052672           0 Microsoft-Windows-Hyper-V-Guest-Drivers/Admin
Circular             1052672             Microsoft-Windows-Hyper-V-Guest-Drivers/Operational
Circular             1052672           0 Microsoft-Windows-Hyper-V-Hypervisor-Admin
Circular             1052672           0 Microsoft-Windows-Hyper-V-Hypervisor-Operational
Circular             1052672           0 Microsoft-Windows-IdCtrls/Operational
Circular             1052672           0 Microsoft-Windows-IKE/Operational
Circular             1052672           0 Microsoft-Windows-International-RegionalOptionsControlPanel/Operational
Circular             1052672           1 Microsoft-Windows-International/Operational
Circular             1052672           0 Microsoft-Windows-Iphlpsvc/Operational
Circular             1052672           0 Microsoft-Windows-KdsSvc/Operational
Circular             1052672             Microsoft-Windows-Kerberos-KdcProxy/Operational
Circular             1052672             Microsoft-Windows-Kerberos/Operational
Circular             1052672           0 Microsoft-Windows-Kernel-ApphelpCache/Operational
Circular             1052672         208 Microsoft-Windows-Kernel-Boot/Operational
Circular             1052672           1 Microsoft-Windows-Kernel-EventTracing/Admin
Circular             1052672        2614 Microsoft-Windows-Kernel-IO/Operational
Circular             1052672         478 Microsoft-Windows-Kernel-PnP/Configuration
Circular             1052672           0 Microsoft-Windows-Kernel-Power/Thermal-Operational
Circular             1052672          29 Microsoft-Windows-Kernel-ShimEngine/Operational
Circular             1052672           0 Microsoft-Windows-Kernel-StoreMgr/Operational
Circular             1052672           0 Microsoft-Windows-Kernel-WDI/Operational
Circular             1052672           0 Microsoft-Windows-Kernel-WHEA/Errors
Circular             1052672          32 Microsoft-Windows-Kernel-WHEA/Operational
Circular             1052672         123 Microsoft-Windows-Known Folders API Service
Circular             1052672          14 Microsoft-Windows-LanguagePackSetup/Operational
Circular             1052672             Microsoft-Windows-LinkLayerDiscoveryProtocol/Operational
Circular             1052672         801 Microsoft-Windows-LiveId/Operational
Circular             1052672             Microsoft-Windows-LSA/Operational
Circular             1052672           0 Microsoft-Windows-ManagementTools-RegistryProvider/Operational
Circular             1052672           0 Microsoft-Windows-ManagementTools-TaskManagerProvider/Operational
Circular             1052672             Microsoft-Windows-MediaFoundation-Performance/SARStreamResource
Circular             1052672           0 Microsoft-Windows-MemoryDiagnostics-Results/Debug
Circular             1052672           0 Microsoft-Windows-MiStreamProvider/Operational
Circular             1052672           0 Microsoft-Windows-Mobile-Broadband-Experience-Parser-Task/Operational
Circular             1052672           0 Microsoft-Windows-Mobile-Broadband-Experience-SmsRouter/Admin
Circular             1052672           0 Microsoft-Windows-Mprddm/Operational
Circular             1052672           0 Microsoft-Windows-MsLbfoProvider/Operational
Circular             1052672             Microsoft-Windows-MSPaint/Admin
Circular             1052672           0 Microsoft-Windows-MUI/Admin
Circular             1052672          12 Microsoft-Windows-MUI/Operational
Circular             1052672             Microsoft-Windows-Ncasvc/Operational
Circular             1052672          12 Microsoft-Windows-NCSI/Operational
Circular             1052672             Microsoft-Windows-NDIS/Operational
Circular             1052672           0 Microsoft-Windows-NdisImPlatform/Operational
Circular             1052672           0 Microsoft-Windows-NetworkLocationWizard/Operational
Circular             1052672         122 Microsoft-Windows-NetworkProfile/Operational
Circular             1052672           0 Microsoft-Windows-NetworkProvider/Operational
Circular             1052672           0 Microsoft-Windows-NlaSvc/Operational
Circular             1052672          82 Microsoft-Windows-Ntfs/Operational
Circular             1052672          16 Microsoft-Windows-Ntfs/WHC
Circular             1052672           0 Microsoft-Windows-NTLM/Operational
Circular             1052672           0 Microsoft-Windows-OfflineFiles/Operational
Circular             1052672             Microsoft-Windows-OneX/Operational
Circular             1052672           0 Microsoft-Windows-OOBE-Machine-DUI/Operational
Circular             1052672             Microsoft-Windows-OtpCredentialProvider/Operational
Circular             1052672           0 Microsoft-Windows-PackageStateRoaming/Operational
Circular            16777216          17 Microsoft-Windows-Partition/Diagnostic
Circular             1052672           0 Microsoft-Windows-PerceptionRuntime/Operational
Circular             1052672           0 Microsoft-Windows-PerceptionSensorDataService/Operational
Circular             1052672           0 Microsoft-Windows-PersistentMemory-Nvdimm/Operational
Circular             1052672           0 Microsoft-Windows-PersistentMemory-PmemDisk/Operational
Circular             1052672           0 Microsoft-Windows-PersistentMemory-ScmBus/Certification
Circular             1052672             Microsoft-Windows-PersistentMemory-ScmBus/Operational
Circular             1052672           0 Microsoft-Windows-Policy/Operational
Circular             1052672           0 Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager/...
Retain            1048985600           0 Microsoft-Windows-PowerShell/Admin
Circular            15728640         730 Microsoft-Windows-PowerShell/Operational
Circular             1052672           0 Microsoft-Windows-PrintBRM/Admin
Circular             1052672           1 Microsoft-Windows-PrintService/Admin
Circular             1052672             Microsoft-Windows-PrintService/Operational
Circular             1052672           0 Microsoft-Windows-PriResources-Deployment/Operational
Circular             1052672             Microsoft-Windows-Program-Compatibility-Assistant/Analytic
Circular             1052672           0 Microsoft-Windows-Program-Compatibility-Assistant/CompatAfterUpgrade
Circular             1052672             Microsoft-Windows-Proximity-Common/Diagnostic
Circular             1052672           0 Microsoft-Windows-PushNotification-Platform/Admin
Circular             1052672        1674 Microsoft-Windows-PushNotification-Platform/Operational
Circular             1052672             Microsoft-Windows-RasAgileVpn/Operational
Circular             1052672           0 Microsoft-Windows-ReadyBoost/Operational
Circular             1052672           0 Microsoft-Windows-ReFS/Operational
Circular             1052672           0 Microsoft-Windows-Regsvr32/Operational
Circular             1052672           0 Microsoft-Windows-RemoteApp and Desktop Connections/Admin
Circular             1052672           0 Microsoft-Windows-RemoteApp and Desktop Connections/Operational
Circular             1052672           0 Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Admin
Circular             1052672        1186 Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Operational
Circular             1052672           0 Microsoft-Windows-RemoteDesktopServices-RemoteFX-Synth3dvsc/Admin
Circular             1052672           0 Microsoft-Windows-RemoteDesktopServices-SessionServices/Operational
Circular             1052672             Microsoft-Windows-Remotefs-Rdbss/Operational
Circular             1052672          21 Microsoft-Windows-Resource-Exhaustion-Detector/Operational
Circular             1052672           3 Microsoft-Windows-Resource-Exhaustion-Resolver/Operational
Circular             1052672           0 Microsoft-Windows-RestartManager/Operational
Circular             1052672             Microsoft-Windows-RRAS/Operational
Circular             1052672           0 Microsoft-Windows-SearchUI/Operational
Circular             1052672           0 Microsoft-Windows-Security-Adminless/Operational
Circular             1052672           0 Microsoft-Windows-Security-Audit-Configuration-Client/Operational
Circular             1052672           0 Microsoft-Windows-Security-EnterpriseData-FileRevocationManager/Operational
Circular             1052672             Microsoft-Windows-Security-ExchangeActiveSyncProvisioning/Operational
Circular             1052672             Microsoft-Windows-Security-IdentityListener/Operational
Circular             1052672           0 Microsoft-Windows-Security-LessPrivilegedAppContainer/Operational
Circular             1052672         121 Microsoft-Windows-Security-Mitigations/KernelMode
Circular             1052672           0 Microsoft-Windows-Security-Mitigations/UserMode
Circular             1052672           0 Microsoft-Windows-Security-Netlogon/Operational
Circular             1052672           0 Microsoft-Windows-Security-SPP-UX-GenuineCenter-Logging/Operational
Circular             1052672          27 Microsoft-Windows-Security-SPP-UX-Notifications/ActionCenter
Circular             1052672           0 Microsoft-Windows-Security-UserConsentVerifier/Audit
Circular             1052672             Microsoft-Windows-SecurityMitigationsBroker/Admin
Circular             1052672           0 Microsoft-Windows-SecurityMitigationsBroker/Operational
Circular             1052672           0 Microsoft-Windows-SENSE/Operational
Circular             1052672           0 Microsoft-Windows-SenseIR/Operational
Circular             1052672           0 Microsoft-Windows-ServerManager-ConfigureSMRemoting/Operational
Circular             1052672         101 Microsoft-Windows-ServerManager-DeploymentProvider/Operational
Circular             1052672         114 Microsoft-Windows-ServerManager-MgmtProvider/Operational
Circular             1052672           0 Microsoft-Windows-ServerManager-MultiMachine/Admin
Circular             1052672         402 Microsoft-Windows-ServerManager-MultiMachine/Operational
Circular             1052672             Microsoft-Windows-ServiceReportingApi/Debug
Circular             1052672           0 Microsoft-Windows-SettingSync-Azure/Debug
Circular             1052672           0 Microsoft-Windows-SettingSync-Azure/Operational
Circular             1052672           0 Microsoft-Windows-SettingSync-OneDrive/Debug
Circular             1052672           0 Microsoft-Windows-SettingSync-OneDrive/Operational
Circular             1052672          60 Microsoft-Windows-SettingSync/Debug
Circular             1052672           2 Microsoft-Windows-SettingSync/Operational
Circular             1052672           0 Microsoft-Windows-Shell-ConnectedAccountState/ActionCenter
Circular             1052672           0 Microsoft-Windows-Shell-Core/ActionCenter
Circular             1052672         683 Microsoft-Windows-Shell-Core/AppDefaults
Circular             1052672           0 Microsoft-Windows-Shell-Core/LogonTasksChannel
Circular             1052672        1507 Microsoft-Windows-Shell-Core/Operational
Circular             1052672         164 Microsoft-Windows-ShellCommon-StartLayoutPopulation/Operational
Circular             1052672           0 Microsoft-Windows-SilProvider/Operational
Circular             1052672           0 Microsoft-Windows-SmartCard-Audit/Authentication
Circular             1052672           6 Microsoft-Windows-SmartCard-DeviceEnum/Operational
Circular             1052672           0 Microsoft-Windows-SmartCard-TPM-VCard-Module/Admin
Circular             1052672           0 Microsoft-Windows-SmartCard-TPM-VCard-Module/Operational
Circular             1052672             Microsoft-Windows-SmartScreen/Debug
Circular             8388608           0 Microsoft-Windows-SmbClient/Audit
Circular             8388608          78 Microsoft-Windows-SmbClient/Connectivity
Circular             8388608           0 Microsoft-Windows-SMBClient/Operational
Circular             8388608           0 Microsoft-Windows-SmbClient/Security
Circular             1052672           0 Microsoft-Windows-SMBDirect/Admin
Circular             8388608           0 Microsoft-Windows-SMBServer/Audit
Circular             8388608           0 Microsoft-Windows-SMBServer/Connectivity
Circular             8388608          70 Microsoft-Windows-SMBServer/Operational
Circular             8388608           0 Microsoft-Windows-SMBServer/Security
Circular             1052672           1 Microsoft-Windows-SMBWitnessClient/Admin
Circular             1052672           0 Microsoft-Windows-SMBWitnessClient/Informational
Circular             5242880         212 Microsoft-Windows-StateRepository/Operational
Circular             1052672           0 Microsoft-Windows-StateRepository/Restricted
Circular             1052672             Microsoft-Windows-Storage-ATAPort/Admin
Circular             1052672             Microsoft-Windows-Storage-ATAPort/Operational
Circular             1052672             Microsoft-Windows-Storage-ClassPnP/Admin
Circular             6291456         640 Microsoft-Windows-Storage-ClassPnP/Operational
Circular             1052672             Microsoft-Windows-Storage-Disk/Admin
Circular             1052672             Microsoft-Windows-Storage-Disk/Operational
Circular             1052672             Microsoft-Windows-Storage-Storport/Admin
Circular             6291456         206 Microsoft-Windows-Storage-Storport/Health
Circular             6291456         262 Microsoft-Windows-Storage-Storport/Operational
Circular             1052672           0 Microsoft-Windows-Storage-Tiering/Admin
Circular             1052672           0 Microsoft-Windows-StorageManagement/Operational
Circular            16777216           0 Microsoft-Windows-StorageSpaces-Driver/Diagnostic
Circular             1052672           0 Microsoft-Windows-StorageSpaces-Driver/Operational
Circular             1052672           0 Microsoft-Windows-StorageSpaces-ManagementAgent/WHC
Circular            16777216           0 Microsoft-Windows-StorageSpaces-SpaceManager/Diagnostic
Circular             1052672           0 Microsoft-Windows-StorageSpaces-SpaceManager/Operational
Circular            20000000        2413 Microsoft-Windows-Store/Operational
Circular           314572800        8261 Microsoft-Windows-SystemDataArchiver/Diagnostic
Circular             1052672           0 Microsoft-Windows-SystemSettingsThreshold/Operational
Circular             1052672         109 Microsoft-Windows-TaskScheduler/Maintenance
Circular            10485760             Microsoft-Windows-TaskScheduler/Operational
Circular             1052672           0 Microsoft-Windows-TCPIP/Operational
Circular             1052672           0 Microsoft-Windows-TerminalServices-ClientUSBDevices/Admin
Circular             1052672           0 Microsoft-Windows-TerminalServices-ClientUSBDevices/Operational
Circular             1052672           0 Microsoft-Windows-TerminalServices-LocalSessionManager/Admin
Circular             1052672         143 Microsoft-Windows-TerminalServices-LocalSessionManager/Operational
Circular             1052672           0 Microsoft-Windows-TerminalServices-PnPDevices/Admin
Circular             1052672           0 Microsoft-Windows-TerminalServices-PnPDevices/Operational
Circular             1052672           6 Microsoft-Windows-TerminalServices-Printers/Admin
Circular             1052672           0 Microsoft-Windows-TerminalServices-Printers/Operational
Circular             1052672           0 Microsoft-Windows-TerminalServices-RDPClient/Operational
Circular             1052672           6 Microsoft-Windows-TerminalServices-RemoteConnectionManager/Admin
Circular             1052672          77 Microsoft-Windows-TerminalServices-RemoteConnectionManager/Operational
Circular             1052672           0 Microsoft-Windows-TerminalServices-ServerUSBDevices/Admin
Circular             1052672           0 Microsoft-Windows-TerminalServices-ServerUSBDevices/Operational
Circular             1052672           0 Microsoft-Windows-TerminalServices-SessionBroker-Client/Admin
Circular             1052672           0 Microsoft-Windows-TerminalServices-SessionBroker-Client/Operational
Circular             1052672           0 Microsoft-Windows-Time-Service-PTP-Provider/PTP-Operational
Circular             1052672         654 Microsoft-Windows-Time-Service/Operational
Circular             1052672           4 Microsoft-Windows-TWinUI/Operational
Circular             1052672           8 Microsoft-Windows-TZSync/Operational
Circular             1052672           0 Microsoft-Windows-TZUtil/Operational
Circular             1052672           0 Microsoft-Windows-UAC-FileVirtualization/Operational
Circular             1052672           0 Microsoft-Windows-UAC/Operational
Circular             1052672         315 Microsoft-Windows-UniversalTelemetryClient/Operational
Circular             1052672           0 Microsoft-Windows-User Control Panel/Operational
Circular             1052672          53 Microsoft-Windows-User Device Registration/Admin
Circular             4194304         116 Microsoft-Windows-User Profile Service/Operational
Circular             1052672           0 Microsoft-Windows-User-Loader/Operational
Circular             1052672           0 Microsoft-Windows-UserPnp/ActionCenter
Circular             1052672          22 Microsoft-Windows-UserPnp/DeviceInstall
Circular             1052672           0 Microsoft-Windows-VDRVROOT/Operational
Circular             1052672           0 Microsoft-Windows-VerifyHardwareSecurity/Admin
Circular             1052672             Microsoft-Windows-VerifyHardwareSecurity/Operational
Circular             1052672           0 Microsoft-Windows-VHDMP-Operational
Circular             1052672           0 Microsoft-Windows-Volume/Diagnostic
Circular             1052672          64 Microsoft-Windows-VolumeSnapshot-Driver/Operational
Circular             1052672           0 Microsoft-Windows-VPN-Client/Operational
Circular             1052672           0 Microsoft-Windows-VPN/Operational
Circular             1052672         152 Microsoft-Windows-Wcmsvc/Operational
Circular             1052672             Microsoft-Windows-WebAuth/Operational
Circular             5242880          27 Microsoft-Windows-WebAuthN/Operational
Circular             1052672             Microsoft-Windows-WebIO-NDF/Diagnostic
Circular             1052672             Microsoft-Windows-WEPHOSTSVC/Operational
Circular             1052672           0 Microsoft-Windows-WER-PayloadHealth/Operational
Circular             1052672           0 Microsoft-Windows-WFP/Operational
Circular             1052672          80 Microsoft-Windows-Win32k/Operational
Circular             1052672         446 Microsoft-Windows-Windows Defender/Operational
Circular             1052672           0 Microsoft-Windows-Windows Defender/WHC
Circular             1052672           0 Microsoft-Windows-Windows Firewall With Advanced Security/ConnectionSecurity
Circular             1052672             Microsoft-Windows-Windows Firewall With Advanced Security/ConnectionSecurit...
Circular             1052672         356 Microsoft-Windows-Windows Firewall With Advanced Security/Firewall
Circular             1052672          16 Microsoft-Windows-Windows Firewall With Advanced Security/FirewallDiagnostics
Circular             1052672             Microsoft-Windows-Windows Firewall With Advanced Security/FirewallVerbose
Circular             1052672             Microsoft-Windows-WindowsColorSystem/Operational
Circular             1052672          83 Microsoft-Windows-WindowsSystemAssessmentTool/Operational
Circular             1052672             Microsoft-Windows-WindowsUIImmersive/Operational
Circular             1052672          71 Microsoft-Windows-WindowsUpdateClient/Operational
Circular             1052672             Microsoft-Windows-WinHTTP-NDF/Diagnostic
Circular             1052672             Microsoft-Windows-WinINet-Capture/Analytic
Circular             1052672           0 Microsoft-Windows-WinINet-Config/ProxyConfigChanged
Circular             1052672         638 Microsoft-Windows-Winlogon/Operational
Circular             1052672             Microsoft-Windows-WinNat/Oper
Circular             1052672         128 Microsoft-Windows-WinRM/Operational
Circular             1052672             Microsoft-Windows-Winsock-AFD/Operational
Circular             1052672             Microsoft-Windows-Winsock-NameResolution/Operational
Circular             1052672           0 Microsoft-Windows-Winsock-WS2HELP/Operational
Circular             1052672           0 Microsoft-Windows-Wired-AutoConfig/Operational
Circular             1052672        1276 Microsoft-Windows-WMI-Activity/Operational
Circular             1052672           0 Microsoft-Windows-WMPNSS-Service/Operational
Circular             1052672             Microsoft-Windows-Wordpad/Admin
Circular             1052672           0 Microsoft-Windows-Workplace Join/Admin
Circular             1052672           0 Microsoft-Windows-WPD-ClassInstaller/Operational
Circular             1052672           0 Microsoft-Windows-WPD-CompositeClassDriver/Operational
Circular             1052672           0 Microsoft-Windows-WPD-MTPClassDriver/Operational
Circular             1052672             Network Isolation Operational
Circular             1052672           0 OpenSSH/Admin
Circular             1052672           0 OpenSSH/Operational
Circular             1052672          10 Setup
Circular             1052672           0 SMSApi
Circular             1052672             Windows Networking Vpn Plugin Platform/Operational
Circular             1052672             Windows Networking Vpn Plugin Platform/OperationalVerbose
```
Execute the command from Example 1 (as is). What are the names of the logs related to OpenSSH? *OpenSSH/Admin,OpenSSH/Operational*
```text
PS C:\Users\Administrator> Get-WinEvent -ListProvider *Powershell*

Name     : PowerShell
LogLinks : {Windows PowerShell}
Opcodes  : {}
Tasks    : {Engine Health
           , Command Health
           , Provider Health
           , Engine Lifecycle
           ...}

Name     : Microsoft-Windows-PowerShell
LogLinks : {Microsoft-Windows-PowerShell/Operational, Microsoft-Windows-PowerShell/Analytic,
           Microsoft-Windows-PowerShell/Debug, Microsoft-Windows-PowerShell/Admin}
Opcodes  : {win:Start, win:Stop, Open, Close...}
Tasks    : {CreateRunspace, ExecuteCommand, Serialization, Powershell-Console-Startup...}

Name     : Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager
LogLinks : {Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager/Operational,
           Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager/Analytic,
           Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager/Debug}
Opcodes  : {}
Tasks    : {FileDownloadManagerDownload, FileDownloadManagerValidate}
```
Execute the command from Example 8. Instead of the string *Policy* search for *PowerShell*. What is the name of the 3rd log provider?
*Microsoft-Windows-PowerShell-DesiredStateConfiguration-FileDownloadManager*
```text
PS C:\Users\Administrator> (Get-WinEvent -ListProvider Microsoft-Windows-PowerShell).Events | Format-Table Id, Description

   Id Description
   -- -----------
 4097 Computer Name $null or . resolve to LocalHost
 4098 Resolving to default scheme http
 4099 Remote shell name resolved to default Microsoft.PowerShell
 4100 %3...
 4101 %3...
 4102 %3...
 4103 %3...
 4104 Creating Scriptblock text (%1 of %2):...
 4105 Started invocation of ScriptBlock ID: %1...
 4106 Completed invocation of ScriptBlock ID: %1...
