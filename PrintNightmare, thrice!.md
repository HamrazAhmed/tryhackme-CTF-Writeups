---
The nightmare continues.. Search the artifacts on the endpoint, again, to determine if the employee used any of the Windows Printer Spooler vulnerabilities to elevate their privileges. 
---

# PrintNightmare, thrice! — Writeup

## Overview
### PrintNightmare, thrice! — Writeup
### PrintNightmare, thrice! — Writeup
![](https://assets.tryhackme.com/additional/printnightmare/pm-room-banner2.png)
![](https://tryhackme-images.s3.amazonaws.com/room-icons/855a6f35a14df6fb9a5e8b576c14e51d.png)
### Detection
![|333](https://i.ibb.co/5KBWxY9/Computer-forensic-science-Digital-evidence-analysis-cybercrime-investigation-data-recovering-Cyberse.jpg)
Scenario: After discovering the PrintNightmare attack the security team pushed an emergency patch to all the endpoints. The PrintNightmare exploit used previously no longer works. All is well. Unfortunately, the same 2 employees discovered yet another exploit that can possibly work on a fully patched endpoint to elevate their privileges.
Task: Inspect the artifacts on the endpoint to detect the PrintNightmare exploit used.
```text
using wireshark, filtering smb2

Source Address: 10.10.158.154
Destination Address: 20.188.56.147

Session Id: 0x000024f2f4000a85 Acct:rjones Domain:THM-PRINTNIGHT0 Host:THM-PRINTNIGHT0
THM-PRINTNIGHT0\r-jones

Session Id: 0x0000247514000041 Acct:gentilguest Domain:THM-PRINTNIGHT0 Host:THM-PRINTNIGHT0
THM-PRINTNIGHT0/gentilguest

Tree: \\printnightmare.gentilkiwi.com\IPC$

using brim

queries: windows network activity, and filter by date from A to Z
_path=~smb* OR _path=dce_rpc | sort ts

\\printnightmare.gentilkiwi.com\IPC$
\PIPE\srvsvc
\pipe\spoolss

\\printnightmare.gentilkiwi.com\IPC$,\srvsvc,\spoolss

querie: file activity
filename!=null cut _path, tx_hosts, rx_hosts, conn_uids, mime_type, filename, md5, sha1

x64\3\mimispool.dll
W32X86\3\mimispool.dll

_path=~smb* | sort ts

\\printnightmare.gentilkiwi.com\print$

\\printnightmare.gentilkiwi.com\print$,x64\3\mimispool.dll,W32X86\3\mimispool.dll

using fulleventlogview (advanced options, show all events) after 

find mimispool.dll

TargetFileName: C:\Windows\System32\spool\drivers\x64\3
TargetFileName: C:\Windows\System32\spool\drivers\W32X86\3

C:\Windows\System32\spool\drivers\W32X86\3C,:\Windows\System32\spool\drivers\x64\3

