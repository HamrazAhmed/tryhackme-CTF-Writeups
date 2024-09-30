# Warzone 2 — Writeup

## Overview
### Warzone 2 — Writeup
### Warzone 2 — Writeup
----
You received another IDS/IPS alert. Time to triage the alert to determine if its a true positive.
----
![](https://assets.tryhackme.com/additional/warzone/warzone-banner.png)
### Another day, another alert.
Start Machine
![SOC Team](https://assets.tryhackme.com/additional/jrsecanalyst/task2.png)
You work as a Tier 1 Security Analyst L1 for a Managed Security Service Provider (MSSP). Again, you're tasked with monitoring network alerts.
An alert triggered: **Misc activity**, **A Network Trojan Was Detected**, and **Potential Corporate Privacy Violation**.
The case was assigned to you. Inspect the PCAP and retrieve the artifacts to confirm this alert is a true positive.
Your tools:
-   [Brim](https://tryhackme.com/room/brim)
-   [Network Miner](https://tryhackme.com/room/networkminer)
-   [Wireshark](https://tryhackme.com/room/wireshark)
---
Deploy the machine attached to this task; it will be visible in the split-screen view once it is ready.
If you don't see a virtual machine load then click the Show Split View button.
![Show Split Screen if needed](https://assets.tryhackme.com/additional/challs/warzone2-split-view.png)
Answer the questions below
```text
using brim import pcap
then filter: event_type=="alert" alert.category=="A Network Trojan was detected" 

alert.signature
ET MALWARE Likely Evil EXE download from MSXMLHTTP non-exe extension M2

filter: event_type=="alert" alert.category=="Potential Corporate Privacy Violation"

alert.signature
ET POLICY PE EXE or DLL Windows file download HTTP

src_ip 185.118.164.8

defanging ip 185[.]118[.]164[.]8

filter 185.118.164.8

file_desc http://awh93dhkylps5ulnq-be.com/czwih/fxla.php?l=gap1.cab

full uri defanged so without http://

awh93dhkylps5ulnq-be[.]com/czwih/fxla[.]php?l=gap1[.]cab

go to query file activity 

filename
gap1.cab
md5
78e05075e686397097de69fb0402263e
sha1
f3e9e7f321deb1a3408053168a6a67c6cd70e114

let's search on virus total

https://www.virustotal.com/gui/file/3769a84dbe7ba74ad7b0b355a864483d3562888a67806082ff094a56ce73bf7e

draw.dll

filter 185.118.164.8 then go to 6 result

user_agent Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/8.0; .NET4.0C; .NET4.0E)

from  virustotal 

a-zcorner.com
d0d0abee1d18255e.com
d0d0f3d189430.com
knockoutlights.com
msnbot-207-46-194-33.search.msn.com
organicgreensfl.com

then comparing with brim 
defanging domains
a-zcorner[.]com,knockoutlights[.]com

filter 10.0.0.0/8 id.resp_h!=176.119.156.128
then defanged ips

64[.]225[.]65[.]166,142[.]93[.]211[.]176

https://www.virustotal.com/gui/ip-address/64.225.65.166/relations

nl-1.nodes.skey.network
fridomcoin.com
dagynalch.pw
antivarevare.top
ulcertification.xyz
tocsicambar.xyz
safebanktest.top
ns2.parcellsafebox.com
ns1.parcellsafebox.com
cadinstitute.com
www.cadinstitute.com

filter id.resp_h==64.225.65.166
defanged domains
safebanktest[.]top,tocsicambar[.]xyz,ulcertification[.]xyz

https://www.virustotal.com/gui/ip-address/142.93.211.176/relations

dev.carsinindia.in
admin.carsinindia.in
meeting230.krititech.com
www.woondly.com
woondly.com
crmtest.ibrook.in
biggfix.serveeazy.com
www.biggfix.serveeazy.com
myphone.serveeazy.com
bright.serveeazy.com
amtiaz.serveeazy.com
www.admin.serveeazy.com
www.myphone.serveeazy.com
admin.serveeazy.com
mobitronold.serveeazy.com
alrehan.serveeazy.com
www.bright.serveeazy.com
www.mobitronold.serveeazy.com
www.amtiaz.serveeazy.com
www.alrehan.serveeazy.com
ariesmobilecareold.serveeazy.com
www.ariesmobilecareold.serveeazy.com
www.image.serveeazy.com
image.serveeazy.com
webmail.serveeazy.com
alreef.serveeazy.com
www.alreef.serveeazy.com
cpanel.serveeazy.com
www.serveeazy.com
serveeazy.com
cpcontacts.serveeazy.com
mail.serveeazy.com
webdisk.serveeazy.com
cpcalendars.serveeazy.com
www.cellzone.serveeazy.com
crackfix.serveeazy.com
www.mobilecareold.serveeazy.com
techmobiles.serveeazy.com
smdsolutions.serveeazy.com
smartphonecare.serveeazy.com
www.mastersold.serveeazy.com
www.crackfix.serveeazy.com
www.smartphonecare.serveeazy.com
mastersold.serveeazy.com
www.techmobiles.serveeazy.com
www.smdsolutions.serveeazy.com
www.old.serveeazy.com
bst.serveeazy.com
www.bst.serveeazy.com
old.serveeazy.com
www.impt.serveeazy.com
cellzone.serveeazy.com
www.bserveold.serveeazy.com
www.techgarage.serveeazy.com
www.utsold.serveeazy.com
techgarage.serveeazy.com
impt.serveeazy.com
www.mksolutions.serveeazy.com
nextlevel.serveeazy.com
