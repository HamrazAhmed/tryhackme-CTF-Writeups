# Boogeyman 1 — Writeup

## Overview
### Boogeyman 1 — Writeup
### Boogeyman 1 — Writeup
----
A new threat actor emerges from the wild using the name Boogeyman. Are you afraid of the Boogeyman?
----
### [Introduction] New threat in town.
Start Machine
﻿_Uncover the secrets of the new emerging threat, the Boogeyman._
In this room, you will be tasked to analyse the Tactics, Techniques, and Procedures (TTPs) executed by a threat group, from obtaining initial access until achieving its objective.
Prerequisites
This room may require the combined knowledge gained from the SOC L1 Pathway. We recommend going through the following rooms before attempting this challenge.
-   [Phishing Analysis Fundamentals](https://tryhackme.com/room/phishingemails1tryoe)
-   [Phishing Analysis Tools](https://tryhackme.com/room/phishingemails3tryoe)
-   [Windows Event Logs](https://tryhackme.com/room/windowseventlogs)
-   [Wireshark: Traffic Analysis](https://tryhackme.com/room/wiresharktrafficanalysis)
-   Tshark (coming soon!)
Investigation Platform
Before we proceed, deploy the attached machine by clicking the **Start Machine button** in the upper-right-hand corner of the task. It may take up to 3-5 minutes to initialise the services.
The machine will start in a split-screen view. In case the VM is not visible, use the blue Show Split View button at the top-right of the page.
Artefacts
For the investigation proper, you will be provided with the following artefacts:
-   Copy of the phishing email (dump.eml)
-   Powershell Logs from Julianne's workstation (powershell.json)
-   Packet capture from the same workstation (capture.pcapng)
Note: The powershell.json file contains JSON-formatted PowerShell logs extracted from its original evtx file via the [evtx2json](https://github.com/Silv3rHorn/evtx2json) tool.
You may find these files in the /home/ubuntu/Desktop/artefacts directory.
Tools
﻿The provided VM contains the following tools at your disposal:
-   Thunderbird - a free and open-source cross-platform email client.
-   [LNKParse3](https://github.com/Matmaus/LnkParse3) - a python package for forensics of a binary file with LNK extension.
-   Wireshark - GUI-based packet analyser.
-   Tshark - CLI-based Wireshark.
-   jq - a lightweight and flexible command-line JSON processor.
To effectively parse and analyse the provided artefacts, you may also utilise built-in command-line tools such as:
-   grep
-   sed
-   awk
-   base64
Now, let's start hunting the Boogeyman!
Answer the questions below
Let's hunt that boogeyman!
Completed
### [Email Analysis] Look at that headers!
The Boogeyman is here!
Julianne, a finance employee working for Quick Logistics LLC, received a follow-up email regarding an unpaid invoice from their business partner, B Packaging Inc. Unbeknownst to her, the attached document was malicious and compromised her workstation.
The security team was able to flag the suspicious execution of the attachment, in addition to the phishing reports received from the other finance department employees, making it seem to be a targeted attack on the finance team. Upon checking the latest trends, the initial TTP used for the malicious attachment is attributed to the new threat group named Boogeyman, known for targeting the logistics sector.
You are tasked to analyse and assess the impact of the compromise.
Investigation Guide
Given the initial information, we know that the compromise started with a phishing email. Let's start with analysing the **dump.eml** file located in the artefacts directory. There are two ways to analyse the headers and rebuild the attachment:
-   The manual way uses command-line tools such as **cat**, **grep**, **base64**, and **sed.** Analyse the contents manually and build the attachment by decoding the string located at the bottom of the file.
ubuntu@tryhackme:~
```shell-session
ubuntu@tryhackme$ echo # sample command to rebuild the payload, presuming the encoded payload is written in another file, without all line terminators
ubuntu@tryhackme$ cat *PAYLOAD FILE* | base64 -d > Invoice.zip
```
-   An alternative and easier way to do this is to double-click the EML file to open it via Thunderbird. The attachment can be saved and extracted accordingly.
Once the payload from the encrypted archive is extracted, use **lnkparse** to extract the information inside the payload.
ubuntu@tryhackme:~
```shell-session
ubuntu@tryhackme$ lnkparse *LNK FILE*
```
Answer the questions below
```text
doing in 2 ways
ubuntu@tryhackme:~/Desktop/artefacts$ echo "UEsDBBQAAQAIAGiGLVZRFQDJ3gIAACgJAAAUAAAASW52b2ljZV8yMDIzMDEwMy5sbmvuhS6/jU+4
> ClhWAZwY+LBcOUvw6oMIq5WNiZwjlKXvAj+pMMBFROiABqlJBxngGOoWUKX0yBXsXOhYPq3Z+Zls
> vZX0xZqtZ/KWnX/QpZXzW44KZz1eqH+hnLgKXPTBsyTSqpqK9QUvYEsltPMSYnL0IqSNwX2TuL9l
> oB0QB3owNKK2cltANxR5Nt3pdYwKJ4BqqI4x7D/ze4bWBT1jlR4HW8VEByEyLoc2fw3I0r0bc/8J
> v9g1SZPBvshBg0pxI0/89GR2agMP+Lv6smkO/huUEOSRpidp/ft+prkt5v9sHFyS/Q0CTb9njCi2
> terQ9NTeFAOkNAhGxWUPqPwPzB0cS+GBC2JY3LMqlA0K5aTejRodyVPcLlq2KVbyF7XljH2NZA4T
> bFsDNJMFk2fQB1hfvmseP9FA20VAfwYvYW8GnBDdqhJtAwJ5xNvJgFFK/MTY2fChwTNN2zszqhzn
> v1Sx+71+duA41HGR9K/jh4nEeRgPslOVlGtLwKBikbIpx/5ZaLpiZYwKS177jDoh3Qx+FRxsM6Ue
> hjPSNgKmWHFZjReDWx8KD7qGLL9acO0hvZUuH83b70sAREDJbw+4sC2jcYO+hrHys6E4Dml030WQ
> WhkKpvYv4DUw9nDmkGg4YgnyAv/iMbtImSUZQ/Wc6dEJM213hYefp8DTQZ321fZU5iCk86bAdxX2
> 3Ov40S9eX78X7CSp9b0QKNeC+N3JgMJ/gQrCWC73UfmHjT4mkBoP8A4YktR2LFNeistVP/zeMQPS
> qUs8KaI7q+VTu/9buNeWkEW2maDm+bC0Q4AnJL+AocgZDPJ0RzfLWEpff3nbaYb6aPqhLTBfFURi
> dszLIMEKmDLmiVqkWZJly9qV26NFttz5y4Q+fAATd6tMYRDlu/BFCo4+rdxjiKl0Gnn7UBHCq0gy
> eEv/L8bppKI09XqNV3MJxMLBE3RN7E080hVp07qDpNpQTYEFa08gGy6yYFBLAQI/ABQAAQAIAGiG
> LVZRFQDJ3gIAACgJAAAUACQAAAAAAAAAIAAAAAAAAABJbnZvaWNlXzIwMjMwMTAzLmxuawoAIAAA
> AAAAAQAYAGiPRUBvJ9kBAAAAAAAAAAAAAAAAAAAAAFBLBQYAAAAAAQABAGYAAAAQAwAAAAA=" | base64 -d > Invoice2.zip
ubuntu@tryhackme:~/Desktop/artefacts$ ls
Invoice.zip   capture.pcapng  evtx2json        powershell.json
Invoice2.zip  dump.eml        powershell.evtx
ubuntu@tryhackme:~/Desktop/artefacts$ file Invoice2.zip 
Invoice2.zip: Zip archive data, at least v2.0 to extract
ubuntu@tryhackme:~/Desktop/artefacts$ file Invoice.zip 
Invoice.zip: Zip archive data, at least v2.0 to extract

source email

From: Arthur Griffin <agriffin@bpakcaging.xyz>
Date: Fri, 13 Jan 2023 09:25:26 +0000
Subject: Collection for Quick Logistics LLC - Jan 2023
Message-Id: <4uiwqc5wd1qx.HPk2p-JE_jYbkWIRB-SmuA2@tracking.bpakcaging.xyz>
Reply-To: Arthur Griffin <agriffin@bpakcaging.xyz>
Sender: agriffin@bpakcaging.xyz
To: Julianne Westcott <julianne.westcott@hotmail.com>

DKIM-Signature: v=1; a=rsa-sha256; d=elasticemail.com; s=api;
	c=relaxed/simple; t=1673601926;
	h=from:date:subject:reply-to:to:list-unsubscribe;
	bh=DORzQK4K9VXO5g47mYpyX7cPagIyvAX1RLfbY0szvCc=;
	b=jcC3z+U5lVQUJEYRyQ76Z+xaJMrXN2YdjyM8pUl7hgXesQaY7rqSORNRWynpDQ3/CBSllw31eDq
	WmoqpFqj2uVy5RXK73lkBEHs5ju1eH/4svHpZLS9+wU/tO5dfZVUImvY32iinpJCtoiMLjdpKYMA/
	d5BBGqluALtqy9fZQzM=
List-Unsubscribe:
 =?us-ascii?q?=3Cmailto=3Aunsubscribe+HPk2p-JE=5FjYbkWIRB-SmuA2=40bounces=2Eelasticem?=
 =?us-ascii?q?ail=2Enet=3Fsubject=3Dunsubscribe=3E=2C?=
 =?us-ascii?q?_=3Chttp=3A=2F=2Ftracking=2Ebpakcaging=2Exyz=2Ftracking=2Funsubscribe=3Fmsgid=3DHP?=
 =?us-ascii?q?k2p-JE=5FjYbkWIRB-SmuA2&c=3D0=3E?=

Hi Julianne,

I hope you are well.

I just wanted to drop you a quick note to remind you in respect of doc=
ument #39586972 is due for payment on January 20, 2023.

I would be grateful if you could confirm everything is on track for pa=
yment.

For additional information, kindly see the attached document.

You may use this code to view the encrypted file: Invoice2023!

Best regards,
Arthur Griffin
Collections Officer
B Packaging Inc.

ubuntu@tryhackme:~/Desktop/artefacts$ unzip Invoice.zip 
Archive:  Invoice.zip
[Invoice.zip] Invoice_20230103.lnk password: 
  inflating: Invoice_20230103.lnk 

ubuntu@tryhackme:~/Desktop/artefacts$ lnkparse Invoice_20230103.lnk 
Windows Shortcut Information:
   Link CLSID: 00021401-0000-0000-C000-000000000046
   Link Flags: HasTargetIDList | HasName | HasRelativePath | HasWorkingDir | HasArguments | HasIconLocation | IsUnicode | HasExpIcon - (16637)
   File Flags:  - (0)

   Creation Timestamp: None
   Modified Timestamp: None
   Accessed Timestamp: None

   Icon Index: 0 
   Window Style: SW_SHOWMINNOACTIVE 
   HotKey: CONTROL - C {0x4302} 

   TARGETS:
      Index: 78
      ITEMS:
         Root Folder
            Sort index: My Computer
            Guid: 20D04FE0-3AEA-1069-A2D8-08002B30309D
         Volume Item
            Flags: 0xf
            Data: None
         File entry
            Flags: Is directory
            Modification time: None
            File attribute flags: 16
            Primary name: Windows
         File entry
            Flags: Is directory
            Modification time: None
            File attribute flags: 16
            Primary name: System32
         File entry
            Flags: Is directory
            Modification time: None
            File attribute flags: 16
            Primary name: WindowsPowerShell
         File entry
            Flags: Is directory
            Modification time: None
            File attribute flags: 16
            Primary name: v1.0
         File entry
            Flags: Is file
            Modification time: None
            File attribute flags: 0
            Primary name: powershell.exe

   DATA
      Description: Invoice Jan 2023
      Relative path: ..\..\..\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
