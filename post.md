# TryHackMe & HackTheBox Master Room Rankings: Difficulty, Length & Release Timeline

> **Comprehensive Index & Deep-Dive Analysis of 427 Security Rooms & Walkthroughs**

This document provides a complete ranking and catalog of all **427 rooms** contained in this repository. Each room is evaluated and indexed according to its **Difficulty Tier**, **Estimated Completion Time / Length**, and **Release Timeline / Era**, along with its technical focus area and direct link to the writeup.

## Executive Overview & Statistics

### Breakdown by Difficulty Tier

| Difficulty Tier | Room Count | Description & Recommended Audience |
| :--- | :---: | :--- |
| **Insane / Capstone** | 2 | Multi-network, pivoting, multi-host enterprise compromise environments (Wreath, Holo) |
| **Hard** | 42 | Complex binary exploitation, advanced AD evasion, and chained exploit chains |
| **Medium** | 194 | Real-world CTF scenarios, intermediate web/privesc, and forensic investigations |
| **Easy** | 156 | Foundational root machines, tool-specific training, and guided CVE labs |
| **Info / Walkthrough** | 32 | Conceptual security, theory modules, protocol primers, and career paths |
| **Special Events / Multi-Day** | 1 | Large-scale multi-challenge events (e.g., Advent of Cyber 2022) |
| **Total Catalog** | **427** | **Complete repository coverage** |

### Breakdown by Release Timeline

| Year / Release Era | Room Count | Typical Threat Landscape & Focus |
| :---: | :---: | :--- |
| **2019** | 18 | Classic boot2roots, initial THM founding labs, basic CMS exploits (Fuel CMS, Webmin) |
| **2020** | 126 | Linux privilege escalation paths, basic Buffer Overflows (OSCP prep), early AD rooms |
| **2021** | 167 | Surge in Active Directory, complex pivoting labs (Wreath, Holo), PrintNightmare, Log4j |
| **2022** | 110 | Modern defense evasion (AMSI, ETW), Certifried, Follina, SOC/DFIR Splunk & Zeek |
| **2023** | 6 | LocalPotato, Outlook NTLM leaks, advanced endpoint persistence & modern cloud/container DFIR |

---

## 1. Tier 1: Insane & Capstone Labs (Mastery Level)

These rooms represent long-form offensive engagements, enterprise-grade multi-machine networks, pivoting through subnets, or deep architectural exploitation.

| Room Name | Platform / Type | Est. Time / Length | Release | Writeup File |
| :--- | :--- | :---: | :---: | :--- |
| **Advent of Cyber 2022** | Event / Multi-topic | `10+ hrs (24 Days)` | 2022 | [Advent of Cyber 2022.md](./Advent%20of%20Cyber%202022.md) |
| **Holo** | Network Lab / Multi-node | `6 - 10 hrs` | 2021 | [Holo.md](./Holo.md) |
| **Wreath** | Enterprise Network Pivoting Lab | `6 - 10 hrs` | 2021 | [Wreath.md](./Wreath.md) |


## 2. Tier 2: Hard Difficulty Rooms (Advanced Exploitation)

Challenging rooms requiring chained vulnerabilities, custom exploit development, binary reversing, AV/EDR evasion, or advanced Active Directory attacks.

| Room Name | Platform / Type | Est. Time / Length | Release | Writeup File |
| :--- | :--- | :---: | :---: | :--- |
| **AV Evasion Shellcode** | Red Teaming / Malware | `2 - 3 hrs` | 2022 | [AV Evasion Shellcode.md](./AV%20Evasion%20Shellcode.md) |
| **Abusing Windows Internals** | Windows Internals | `2.5 - 3.5 hrs` | 2022 | [Abusing Windows Internals.md](./Abusing%20Windows%20Internals.md) |
| **Anonymous Playground** | Reverse Engineering / CTF | `2 - 3 hrs` | 2020 | [Anonymous Playground.md](./Anonymous%20Playground.md) |
| **BioHazard** | Multi-stage CTF | `3 - 4 hrs` | 2020 | [BioHazard.md](./BioHazard.md) |
| **Brainpan 1** | Buffer Overflow / CTF | `2.5 - 3.5 hrs` | 2020 | [Brainpan 1.md](./Brainpan%201.md) |
| **Carpe Diem 1** | Linux / Privilege Escalation | `2.5 - 3.5 hrs` | 2021 | [Carpe Diem 1.md](./Carpe%20Diem%201.md) |
| **Corp** | Active Directory | `3 - 4 hrs` | 2021 | [Corp.md](./Corp.md) |
| **Daily Bugle** | Joomla / SQLi / Linux | `2 - 3 hrs` | 2019 | [Daily Bugle.md](./Daily%20Bugle.md) |
| **Enterprise** | Buffer Overflow / Linux | `3 - 4 hrs` | 2020 | [Enterprise.md](./Enterprise.md) |
| **Evading Logging and Monitoring** | Evasion / Defense | `2.5 - 3.5 hrs` | 2022 | [Evading Logging and Monitoring.md](./Evading%20Logging%20and%20Monitoring.md) |
| **Ghizer** | Multi-stage Linux CTF | `3 - 4 hrs` | 2021 | [Ghizer.md](./Ghizer.md) |
| **HA Joker CTF** | Multi-level CTF | `3 - 4 hrs` | 2020 | [HA Joker CTF.md](./HA%20Joker%20CTF.md) |
| **HipFlask** | Binary / Web CTF | `3 - 4 hrs` | 2021 | [HipFlask.md](./HipFlask.md) |
| **Insekube** | Kubernetes Pentest | `3 - 4 hrs` | 2021 | [Insekube.md](./Insekube.md) |
| **Internal** | AD / WordPress / Jenkins | `2.5 - 3.5 hrs` | 2020 | [Internal.md](./Internal.md) |
| **LinuxFunctionHooking** | Linux Internals / Hooking | `2.5 hrs` | 2022 | [LinuxFunctionHooking.md](./LinuxFunctionHooking.md) |
| **Lookback** | Active Directory / Exchange | `3 - 4 hrs` | 2022 | [Lookback.md](./Lookback.md) |
| **Obfuscation Principles** | Malware / Evasion | `2 hrs` | 2022 | [Obfuscation Principles.md](./Obfuscation%20Principles.md) |
| **Olympus** | Web / Linux CTF | `2.5 - 3.5 hrs` | 2021 | [Olympus.md](./Olympus.md) |
| **Osiris** | Active Directory / CTF | `3 - 4 hrs` | 2021 | [Osiris.md](./Osiris.md) |
| **Ra 2** | Active Directory / PKI | `3 - 4 hrs` | 2022 | [Ra 2.md](./Ra%202.md) |
| **Ra** | Active Directory / Windmill | `3 - 4 hrs` | 2021 | [Ra.md](./Ra.md) |
| **RazorBlack** | Active Directory Lab | `3 - 4 hrs` | 2021 | [RazorBlack.md](./RazorBlack.md) |
| **Red** | Multi-stage Linux CTF | `3 - 4 hrs` | 2021 | [Red.md](./Red.md) |
| **Retro** | Windows / CVE-2019-1388 | `2 hrs` | 2019 | [Retro.md](./Retro.md) |
| **Runtime Detection Evasion** | AMSI / ETW Evasion | `2 - 3 hrs` | 2022 | [Runtime Detection Evasion.md](./Runtime%20Detection%20Evasion.md) |
| **Sandbox Evasion** | Malware Evasion | `2 hrs` | 2022 | [Sandbox Evasion.md](./Sandbox%20Evasion.md) |
| **Sea Surfer** | SSRF / Gitea / Linux | `2.5 - 3.5 hrs` | 2021 | [Sea Surfer.md](./Sea%20Surfer.md) |
| **Set** | Social Engineering Toolkit | `2 hrs` | 2020 | [Set.md](./Set.md) |
| **Signature Evasion** | Defender Evasion | `2.5 hrs` | 2022 | [Signature Evasion.md](./Signature%20Evasion.md) |
| **Snort Challenge - Live Attacks** | IDS / Snort Live | `2.5 - 3.5 hrs` | 2022 | [Snort Challenge - Live Attacks.md](./Snort%20Challenge%20-%20Live%20Attacks.md) |
| **Tempest** | Active Directory / CTF | `3 hrs` | 2022 | [Tempest.md](./Tempest.md) |
| **Tempus Fugit Durius** | Linux / Advanced CTF | `3 hrs` | 2021 | [Tempus Fugit Durius.md](./Tempus%20Fugit%20Durius.md) |
| **The Server From Hell** | Tarpit / Port Scanning | `2.5 hrs` | 2020 | [The Server From Hell.md](./The%20Server%20From%20Hell.md) |
| **Theseus** | Linux / Advanced CTF | `3 hrs` | 2021 | [Theseus.md](./Theseus.md) |
| **VulnNet Endgame** | Active Directory / Enterprise | `3.5 - 5 hrs` | 2021 | [VulnNet Endgame.md](./VulnNet%20Endgame.md) |
| **Year of the Dog** | 2FA Bypass / Linux CTF | `2.5 - 3.5 hrs` | 2020 | [Year of the Dog.md](./Year%20of%20the%20Dog.md) |
| **Year of the Fox** | Samba / SQLi CTF | `2.5 - 3.5 hrs` | 2020 | [Year of the Fox.md](./Year%20of%20the%20Fox.md) |
| **Year of the Jellyfish** | Hardened Linux CTF | `3 - 4 hrs` | 2020 | [Year of the Jellyfish.md](./Year%20of%20the%20Jellyfish.md) |
| **Year of the Owl** | Windows PrivEsc CTF | `2.5 - 3.5 hrs` | 2020 | [Year of the Owl.md](./Year%20of%20the%20Owl.md) |
| **Year of the Pig** | Web / Linux CTF | `2.5 - 3.5 hrs` | 2020 | [Year of the Pig.md](./Year%20of%20the%20Pig.md) |
| **ret2libc** | Binary Exploitation / ROP | `2.5 - 3.5 hrs` | 2020 | [ret2libc.md](./ret2libc.md) |

---

## 3. Tier 3: Medium Difficulty Rooms (Intermediate Hands-on)

Standard competitive CTFs and realistic penetration testing environments covering privilege escalation, custom web application flaws, pivoting, and forensic triage.

| Room Name | Platform / Type | Est. Time / Length | Release | Writeup File |
| :--- | :--- | :---: | :---: | :--- |
| **0day** | Linux CTF | `1 - 2 hrs` | 2020 | [0day.md](./0day.md) |
| **AD Certificate Templates** | Active Directory | `1.5 - 2 hrs` | 2022 | [AD Certificate Templates.md](./AD%20Certificate%20Templates.md) |
| **AllSignsPoint2Pwnage** | Active Directory | `1.5 - 2.5 hrs` | 2022 | [AllSignsPoint2Pwnage.md](./AllSignsPoint2Pwnage.md) |
| **Android Malware Analysis** | Mobile DFIR | `1.5 - 2 hrs` | 2022 | [Android Malware Analysis.md](./Android%20Malware%20Analysis.md) |
| **Annie** | Linux CTF | `1 - 2 hrs` | 2021 | [Annie.md](./Annie.md) |
| **Anonymous** | Linux CTF | `1 - 1.5 hrs` | 2020 | [Anonymous.md](./Anonymous.md) |
| **Aratus** | Linux CTF | `1.5 - 2 hrs` | 2022 | [Aratus.md](./Aratus.md) |
| **Atlas** | Network Pentest | `1.5 - 2 hrs` | 2022 | [Atlas.md](./Atlas.md) |
| **Attacking Kerberos** | Active Directory | `2 - 3 hrs` | 2021 | [Attacking Kerberos.md](./Attacking%20Kerberos.md) |
| **Basic Static Analysis** | Malware Analysis | `1.5 - 2 hrs` | 2022 | [Basic Static Analysis.md](./Basic%20Static%20Analysis.md) |
| **Bebop** | Linux CTF | `1 - 1.5 hrs` | 2021 | [Bebop.md](./Bebop.md) |
| **Biblioteca** | Linux / SQLi | `1.5 - 2 hrs` | 2022 | [Biblioteca.md](./Biblioteca.md) |
| **BinaryHeaven** | Binary Exploitation | `2 - 3 hrs` | 2020 | [BinaryHeaven.md](./BinaryHeaven.md) |
| **Binex** | Binary Exploitation | `2 - 3 hrs` | 2020 | [Binex.md](./Binex.md) |
| **Blog** | Linux / WordPress | `1.5 - 2 hrs` | 2020 | [Blog.md](./Blog.md) |
| **Boiler CTF** | Linux CTF | `1.5 - 2 hrs` | 2019 | [Boiler CTF.md](./Boiler%20CTF.md) |
| **Boogeyman 1** | DFIR / Threat Hunting | `2 - 3 hrs` | 2023 | [Boogeyman 1.md](./Boogeyman%201.md) |
| **Brainstorm** | Buffer Overflow / Windows | `1.5 - 2.5 hrs` | 2019 | [Brainstorm.md](./Brainstorm.md) |
| **Brute** | Linux / Brute | `1 - 1.5 hrs` | 2020 | [Brute.md](./Brute.md) |
| **Buffer Overflow Prep** | OSCP Prep / BoF | `3 - 5 hrs` | 2020 | [Buffer Overflow Prep.md](./Buffer%20Overflow%20Prep.md) |
| **Buffer Overflows** | Binary / BoF | `2 - 3 hrs` | 2020 | [Buffer Overflows.md](./Buffer%20Overflows.md) |
| **CCT2019** | CTF Challenge | `1.5 - 2 hrs` | 2019 | [CCT2019.md](./CCT2019.md) |
| **CMSpit** | CMS Exploitation | `1 - 1.5 hrs` | 2021 | [CMSpit.md](./CMSpit.md) |
| **CMesS** | Linux CTF | `1 - 1.5 hrs` | 2020 | [CMesS.md](./CMesS.md) |
| **CVE-2022-26923** | Active Directory Certifried | `1.5 - 2 hrs` | 2022 | [CVE-2022-26923.md](./CVE-2022-26923.md) |
| **CVE-2023-38408** | OpenSSH PKCS#11 | `1 hr` | 2023 | [CVE-2023-38408.md](./CVE-2023-38408.md) |
| **Cat Pictures 2** | Steganography / Linux | `1.5 - 2 hrs` | 2021 | [Cat Pictures 2.md](./Cat%20Pictures%202.md) |
| **Cat Pictures** | Steganography / Linux | `1.5 - 2 hrs` | 2021 | [Cat Pictures.md](./Cat%20Pictures.md) |
| **Content Security Policy** | Web Security | `1 hr` | 2022 | [Content Security Policy.md](./Content%20Security%20Policy.md) |
| **Conti** | Ransomware Analysis | `1 - 1.5 hrs` | 2022 | [Conti.md](./Conti.md) |
| **ConvertMyVideo** | Web / Command Injection | `1 hr` | 2020 | [ConvertMyVideo.md](./ConvertMyVideo.md) |
| **Cooctus Stories** | Web CTF | `1.5 - 2 hrs` | 2020 | [Cooctus Stories.md](./Cooctus%20Stories.md) |
| **Credentials Harvesting** | Credential Dumping | `1.5 - 2 hrs` | 2022 | [Credentials Harvesting.md](./Credentials%20Harvesting.md) |
| **Crocc Crew** | Web CTF | `1.5 - 2 hrs` | 2020 | [Crocc Crew.md](./Crocc%20Crew.md) |
| **Crylo** | Crypto / Linux | `1.5 - 2 hrs` | 2021 | [Crylo.md](./Crylo.md) |
| **CyberCrafted** | Minecraft / Linux CTF | `2 - 3 hrs` | 2021 | [CyberCrafted.md](./CyberCrafted.md) |
| **DX1 Liberty Island** | Linux CTF | `1.5 - 2 hrs` | 2022 | [DX1 Liberty Island.md](./DX1%20Liberty%20Island.md) |
| **Data Exfiltration** | Network / Red Team | `2 hrs` | 2022 | [Data Exfiltration.md](./Data%20Exfiltration.md) |
| **Debug** | PHP Deserialization | `1.5 - 2 hrs` | 2021 | [Debug.md](./Debug.md) |
| **Deja Vu** | Linux CTF | `1.5 - 2 hrs` | 2021 | [Deja Vu.md](./Deja%20Vu.md) |
| **Dependency Management** | DevSecOps | `1.5 hrs` | 2022 | [Dependency Management.md](./Dependency%20Management.md) |
| **Different CTF** | CTF Challenge | `1.5 hrs` | 2020 | [Different CTF.md](./Different%20CTF.md) |
| **Digital Forensics Case B4DM755** | DFIR Case | `1.5 - 2 hrs` | 2021 | [Digital Forensics Case B4DM755.md](./Digital%20Forensics%20Case%20B4DM755.md) |
| **Dissecting PE Headers** | Reverse Engineering | `1.5 hrs` | 2022 | [Dissecting PE Headers.md](./Dissecting%20PE%20Headers.md) |
| **Eavesdropper** | Linux Network Sniffing | `1.5 hrs` | 2022 | [Eavesdropper.md](./Eavesdropper.md) |
| **Empire** | PowerShell Empire C2 | `2 hrs` | 2021 | [Empire.md](./Empire.md) |
| **Empline** | Linux / Asterisk CTF | `1.5 - 2 hrs` | 2021 | [Empline.md](./Empline.md) |
| **Erit Securus I** | Linux CTF | `1.5 - 2 hrs` | 2021 | [Erit Securus I.md](./Erit%20Securus%20I.md) |
| **Flatline** | FreePBX / Linux | `1.5 hrs` | 2021 | [Flatline.md](./Flatline.md) |
| **Flip** | Crypto / CBC Bit-flipping | `1.5 - 2 hrs` | 2021 | [Flip.md](./Flip.md) |
| **Forgotten Implant** | C2 / Incident Response | `1.5 - 2 hrs` | 2022 | [Forgotten Implant.md](./Forgotten%20Implant.md) |
| **Fusion Corp** | Active Directory | `2 - 3 hrs` | 2021 | [Fusion Corp.md](./Fusion%20Corp.md) |
| **Gatekeeper** | Buffer Overflow / Windows | `2 - 3 hrs` | 2020 | [Gatekeeper.md](./Gatekeeper.md) |
| **Generic University** | Web / Linux CTF | `1.5 hrs` | 2021 | [Generic University.md](./Generic%20University.md) |
| **Git_crumpets** | Git / Web Exploitation | `1.5 hrs` | 2021 | [Git_crumpets.md](./Git_crumpets.md) |
| **GoldenEye** | Linux / Pop3 / CTF | `2 - 3 hrs` | 2019 | [GoldenEye.md](./GoldenEye.md) |
| **Grep** | Linux PrivEsc | `1.5 hrs` | 2021 | [Grep.md](./Grep.md) |
| **HackPark** | Windows / Hydra / WinPE | `1.5 - 2.5 hrs` | 2019 | [HackPark.md](./HackPark.md) |
| **Hacking with PowerShell** | PowerShell Red Team | `2 - 3 hrs` | 2020 | [Hacking with PowerShell.md](./Hacking%20with%20PowerShell.md) |
| **Hamlet** | Linux CTF | `1.5 hrs` | 2021 | [Hamlet.md](./Hamlet.md) |
| **HaskHell** | Haskell / Linux CTF | `1.5 hrs` | 2020 | [HaskHell.md](./HaskHell.md) |
| **Incident handling with Splunk** | SOC / Splunk | `2 hrs` | 2021 | [Incident handling with Splunk.md](./Incident%20handling%20with%20Splunk.md) |
| **Inferno** | Linux CTF / Codiad | `1.5 hrs` | 2020 | [Inferno.md](./Inferno.md) |
| **Intro To Pwntools** | Exploit Dev / Python | `2 hrs` | 2021 | [Intro To Pwntools.md](./Intro%20To%20Pwntools.md) |
| **Intro to Detection Engineering** | Detection / Blue Team | `1.5 hrs` | 2022 | [Intro to Detection Engineering.md](./Intro%20to%20Detection%20Engineering.md) |
| **Intro to Malware Analysis** | Malware Analysis | `1.5 - 2 hrs` | 2021 | [Intro to Malware Analysis.md](./Intro%20to%20Malware%20Analysis.md) |
| **Intro to Threat Emulation** | Adversary Emulation | `1.5 hrs` | 2022 | [Intro to Threat Emulation.md](./Intro%20to%20Threat%20Emulation.md) |
| **Introduction to Cryptography** | Applied Crypto | `2 hrs` | 2020 | [Introduction to Cryptography.md](./Introduction%20to%20Cryptography.md) |
| **Intrusion Detection** | Snort / Suricata IDS | `2 - 3 hrs` | 2021 | [Intrusion Detection.md](./Intrusion%20Detection.md) |
| **Iron Corp** | Windows CTF | `1.5 - 2 hrs` | 2020 | [Iron Corp.md](./Iron%20Corp.md) |
| **Jack** | WordPress / FastCGI CTF | `2 hrs` | 2020 | [Jack.md](./Jack.md) |
| **Jacob the Boss** | JBoss Exploitation | `1 - 1.5 hrs` | 2020 | [Jacob the Boss.md](./Jacob%20the%20Boss.md) |
| **Jeff** | WordPress / Linux CTF | `1.5 - 2 hrs` | 2020 | [Jeff.md](./Jeff.md) |
| **Jurassic Park** | SQLi / Linux CTF | `1.5 hrs` | 2020 | [Jurassic Park.md](./Jurassic%20Park.md) |
| **KAPE** | Triage Forensics | `2 hrs` | 2022 | [KAPE.md](./KAPE.md) |
| **Keldagrim** | Linux CTF | `1.5 hrs` | 2020 | [Keldagrim.md](./Keldagrim.md) |
| **KoTH Food CTF** | King of the Hill | `1.5 hrs` | 2020 | [KoTH Food CTF.md](./KoTH%20Food%20CTF.md) |
| **KoTH Hackers** | King of the Hill | `1.5 hrs` | 2020 | [KoTH Hackers.md](./KoTH%20Hackers.md) |
| **Kubernetes for Everyone** | Kubernetes Security | `2 hrs` | 2021 | [Kubernetes for Everyone.md](./Kubernetes%20for%20Everyone.md) |
| **L2 MAC Flooding & ARP Spoofing** | Network Attacks | `1.5 hrs` | 2022 | [L2 MAC Flooding & ARP Spoofing.md](./L2%20MAC%20Flooding%20%26%20ARP%20Spoofing.md) |
| **Linux Forensics** | DFIR / Linux | `1.5 - 2 hrs` | 2022 | [Linux Forensics.md](./Linux%20Forensics.md) |
| **Living Off the Land** | LOLBAS / LOLBins | `1.5 hrs` | 2022 | [Living Off the Land.md](./Living%20Off%20the%20Land.md) |
| **LocalPotato** | Windows PrivEsc / CVE-2023-21746 | `1 hr` | 2023 | [LocalPotato.md](./LocalPotato.md) |
| **Lockdown** | Linux CTF | `1.5 hrs` | 2021 | [Lockdown.md](./Lockdown.md) |
| **Lumberjack Turtle** | Log4j / CVE-2021-44228 | `1.5 hrs` | 2021 | [Lumberjack Turtle.md](./Lumberjack%20Turtle.md) |
| **Lunizz CTF** | Linux CTF | `1.5 hrs` | 2021 | [Lunizz CTF.md](./Lunizz%20CTF.md) |
| **MAL REMnux The Redux** | Malware Analysis | `1.5 hrs` | 2021 | [MAL REMnux The Redux.md](./MAL%20REMnux%20The%20Redux.md) |
| **MISP** | Threat Sharing | `1.5 hrs` | 2022 | [MISP.md](./MISP.md) |
| **Madeye's Castle** | Linux CTF | `1.5 - 2 hrs` | 2021 | [Madeye's Castle.md](./Madeye%27s%20Castle.md) |
| **Metamorphosis** | Active Directory | `2 hrs` | 2022 | [Metamorphosis.md](./Metamorphosis.md) |
| **Microsoft Windows Hardening** | Defensive Hardening | `1.5 hrs` | 2022 | [Microsoft Windows Hardening.md](./Microsoft%20Windows%20Hardening.md) |
| **Mindgames** | Brainfuck / Python PrivEsc | `1.5 hrs` | 2021 | [Mindgames.md](./Mindgames.md) |
| **Minotaur's Labyrinth** | Web / SQLi CTF | `1.5 hrs` | 2021 | [Minotaur's Labyrinth.md](./Minotaur%27s%20Labyrinth.md) |
| **Mnemonic** | Active Directory / Forensics | `2 hrs` | 2022 | [Mnemonic.md](./Mnemonic.md) |
| **NIS - Linux Part I** | Network Services | `1.5 hrs` | 2021 | [NIS - Linux Part I.md](./NIS%20-%20Linux%20Part%20I.md) |
| **NahamStore** | Web Pentesting Lab | `2.5 - 3.5 hrs` | 2022 | [NahamStore.md](./NahamStore.md) |
| **Napping** | Web Tabnabbing | `1 hr` | 2022 | [Napping.md](./Napping.md) |
| **Net Sec Challenge** | Network Challenge | `1.5 hrs` | 2021 | [Net Sec Challenge.md](./Net%20Sec%20Challenge.md) |
| **Network Security Solutions** | IDS / IPS / Firewalls | `1.5 hrs` | 2022 | [Network Security Solutions.md](./Network%20Security%20Solutions.md) |
| **Nmap Advanced Port Scans** | Recon / Nmap | `1 hr` | 2021 | [Nmap Advanced Port Scans.md](./Nmap%20Advanced%20Port%20Scans.md) |
| **Nmap Post Port Scans** | Recon / Nmap | `1 hr` | 2021 | [Nmap Post Port Scans.md](./Nmap%20Post%20Port%20Scans.md) |
| **NoNameCTF** | Linux CTF | `1.5 hrs` | 2021 | [NoNameCTF.md](./NoNameCTF.md) |
| **NoSQL injection Basics** | Web / NoSQLi | `1 hr` | 2021 | [NoSQL injection Basics.md](./NoSQL%20injection%20Basics.md) |
| **OWASP API Security Top 10 - 1** | API Security | `1.5 hrs` | 2022 | [OWASP API Security Top 10 - 1.md](./OWASP%20API%20Security%20Top%2010%20-%201.md) |
| **OWASP API Security Top 10 - 2** | API Security | `1.5 hrs` | 2022 | [OWASP API Security Top 10 - 2.md](./OWASP%20API%20Security%20Top%2010%20-%202.md) |
| **OWASP Broken Access Control** | Web Security | `1 hr` | 2022 | [OWASP Broken Access Control.md](./OWASP%20Broken%20Access%20Control.md) |
| **Oh My WebServer** | CVE-2021-42013 / Docker | `1 hr` | 2021 | [Oh My WebServer.md](./Oh%20My%20WebServer.md) |
| **Ollie** | Linux CTF / phpIPAM | `1.5 hrs` | 2022 | [Ollie.md](./Ollie.md) |
| **One Piece** | Anime CTF / Linux | `1.5 hrs` | 2020 | [One Piece.md](./One%20Piece.md) |
| **OpenCTI** | Threat Intelligence | `1.5 hrs` | 2022 | [OpenCTI.md](./OpenCTI.md) |
| **Outlook NTLM Leak** | CVE-2023-23397 | `1 hr` | 2023 | [Outlook NTLM Leak.md](./Outlook%20NTLM%20Leak.md) |
| **Overpass3** | Web / GPG / Linux CTF | `1.5 hrs` | 2020 | [Overpass3.md](./Overpass3.md) |
| **PS Eclipse** | PowerShell Script Analysis | `1 hr` | 2022 | [PS Eclipse.md](./PS%20Eclipse.md) |
| **ParrotPost Phishing Analysis** | Phishing Analysis | `1.5 hrs` | 2022 | [ParrotPost Phishing Analysis.md](./ParrotPost%20Phishing%20Analysis.md) |
| **Password Attacks** | Cracking / Hydra / Hashcat | `2 hrs` | 2022 | [Password Attacks.md](./Password%20Attacks.md) |
| **Phishing Emails 3** | Email Header Analysis | `1 hr` | 2022 | [Phishing Emails 3.md](./Phishing%20Emails%203.md) |
| **Phishing Emails 4** | Email Header Analysis | `1 hr` | 2022 | [Phishing Emails 4.md](./Phishing%20Emails%204.md) |
| **Phishing Emails 5** | Email Header Analysis | `1 hr` | 2022 | [Phishing Emails 5.md](./Phishing%20Emails%205.md) |
| **Plotted-TMS** | Traffic Management CMS | `1.5 - 2 hrs` | 2021 | [Plotted-TMS.md](./Plotted-TMS.md) |
| **PowerShell for Pentesters** | PowerShell Scripting | `2 hrs` | 2020 | [PowerShell for Pentesters.md](./PowerShell%20for%20Pentesters.md) |
| **PrintNightmare, again!** | CVE-2021-34527 | `45 mins` | 2021 | [PrintNightmare, again!.md](./PrintNightmare%2C%20again%21.md) |
| **PrintNightmare, thrice!** | CVE-2021-36958 | `45 mins` | 2021 | [PrintNightmare, thrice!.md](./PrintNightmare%2C%20thrice%21.md) |
| **PrintNightmare** | CVE-2021-1675 / 34527 | `1 hr` | 2021 | [PrintNightmare.md](./PrintNightmare.md) |
| **Racetrack Bank** | Race Conditions / Web | `1 hr` | 2022 | [Racetrack Bank.md](./Racetrack%20Bank.md) |
| **Recovery** | Windows / Web CTF | `2 hrs` | 2021 | [Recovery.md](./Recovery.md) |
| **Red Team OPSEC** | Red Team Operations | `1.5 hrs` | 2022 | [Red Team OPSEC.md](./Red%20Team%20OPSEC.md) |
| **Red Team Threat Intel** | Red Team Intelligence | `1.5 hrs` | 2022 | [Red Team Threat Intel.md](./Red%20Team%20Threat%20Intel.md) |
| **Redline** | Memory & Endpoint DFIR | `1.5 hrs` | 2021 | [Redline.md](./Redline.md) |
| **Relevant** | Windows / PrintSpoofer CTF | `1.5 - 2 hrs` | 2020 | [Relevant.md](./Relevant.md) |
| **Revenge** | SQLi / Linux CTF | `1.5 hrs` | 2020 | [Revenge.md](./Revenge.md) |
| **Revil_Corp** | Ransomware Analysis | `1.5 hrs` | 2021 | [Revil_Corp.md](./Revil_Corp.md) |
| **Road** | Web / MongoDB / Docker | `1.5 hrs` | 2021 | [Road.md](./Road.md) |
| **SQHell** | Advanced SQLi | `2 hrs` | 2020 | [SQHell.md](./SQHell.md) |
| **SSRF** | Server-Side Request Forgery | `1 hr` | 2021 | [SSRF.md](./SSRF.md) |
| **Scripting** | Python / Network Sockets | `1.5 hrs` | 2020 | [Scripting.md](./Scripting.md) |
| **Secret Recipe** | Memory Forensics | `1.5 hrs` | 2021 | [Secret Recipe.md](./Secret%20Recipe.md) |
| **Sigma** | Detection Engineering | `1.5 hrs` | 2022 | [Sigma.md](./Sigma.md) |
| **Snapped Phishing Line** | Phishing DFIR | `1.5 hrs` | 2022 | [Snapped Phishing Line.md](./Snapped%20Phishing%20Line.md) |
| **Snort Challenge - The Basics** | IDS / Snort Rules | `2 hrs` | 2022 | [Snort Challenge - The Basics.md](./Snort%20Challenge%20-%20The%20Basics.md) |
| **Splunk 2** | SIEM Querying | `1.5 hrs` | 2021 | [Splunk 2.md](./Splunk%202.md) |
| **Super-Spam** | Email / Web CTF | `1.5 hrs` | 2020 | [Super-Spam.md](./Super-Spam.md) |
| **Sustah** | Linux / Rate Limiting | `1.5 hrs` | 2020 | [Sustah.md](./Sustah.md) |
| **Sweettooth Inc.** | Docker / Linux CTF | `1.5 hrs` | 2021 | [Sweettooth Inc..md](./Sweettooth%20Inc..md) |
| **Sysmon** | Windows Logging | `1.5 hrs` | 2021 | [Sysmon.md](./Sysmon.md) |
| **Tactical Detection** | Blue Team Detection | `1.5 hrs` | 2022 | [Tactical Detection.md](./Tactical%20Detection.md) |
| **Takedown** | Active Directory / CTF | `2 hrs` | 2021 | [Takedown.md](./Takedown.md) |
| **Tardigrade** | Linux Persistence DFIR | `1.5 hrs` | 2023 | [Tardigrade.md](./Tardigrade.md) |
| **Temple** | Flask SSTI / Linux CTF | `1.5 hrs` | 2021 | [Temple.md](./Temple.md) |
| **That's The Ticket** | Kerberos / Web | `1.5 hrs` | 2021 | [That's The Ticket.md](./That%27s%20The%20Ticket.md) |
| **The Blob Blog** | Web / Node.js CTF | `1.5 hrs` | 2021 | [The Blob Blog.md](./The%20Blob%20Blog.md) |
| **The Cod Caper** | Buffer Overflow / Linux | `2 hrs` | 2020 | [The Cod Caper.md](./The%20Cod%20Caper.md) |
| **The Docker Rodeo** | Docker Escape CTF | `1.5 hrs` | 2021 | [The Docker Rodeo.md](./The%20Docker%20Rodeo.md) |
| **The Great Escape** | Docker Escape CTF | `1.5 hrs` | 2021 | [The Great Escape.md](./The%20Great%20Escape.md) |
| **The Impossible Challenge** | Reverse Engineering | `1.5 hrs` | 2020 | [The Impossible Challenge.md](./The%20Impossible%20Challenge.md) |
| **Threat Intel & Containment** | Threat Intelligence | `1.5 hrs` | 2022 | [Threat Intel & Containment.md](./Threat%20Intel%20%26%20Containment.md) |
| **Tokyo Ghoul** | Python Jail / Linux CTF | `1.5 hrs` | 2021 | [Tokyo Ghoul.md](./Tokyo%20Ghoul.md) |
| **Tony the Tiger** | JBoss / Linux CTF | `1.5 hrs` | 2020 | [Tony the Tiger.md](./Tony%20the%20Tiger.md) |
| **Unattended** | Linux CTF | `1.5 hrs` | 2020 | [Unattended.md](./Unattended.md) |
| **Undiscovered** | Linux CTF | `1.5 hrs` | 2021 | [Undiscovered.md](./Undiscovered.md) |
| **Uranium CTF** | Linux CTF | `1.5 hrs` | 2021 | [Uranium CTF.md](./Uranium%20CTF.md) |
| **Valley** | Linux CTF | `1.5 hrs` | 2023 | [Valley.md](./Valley.md) |
| **Velociraptor** | Endpoint Forensics | `1.5 hrs` | 2021 | [Velociraptor.md](./Velociraptor.md) |
| **Volatility** | Memory Forensics | `2 hrs` | 2020 | [Volatility.md](./Volatility.md) |
| **VulnNet Internal** | Internal Network Pentest | `2 - 3 hrs` | 2021 | [VulnNet Internal.md](./VulnNet%20Internal.md) |
| **VulnNet Node** | Node.js Deserialization | `1.5 hrs` | 2021 | [VulnNet Node.md](./VulnNet%20Node.md) |
| **VulnNet Roasted** | Active Directory Roast | `2 hrs` | 2021 | [VulnNet Roasted.md](./VulnNet%20Roasted.md) |
| **Warzone 2** | Network PCAP Analysis | `1 hr` | 2022 | [Warzone 2.md](./Warzone%202.md) |
| **Watcher** | Boot2Root / Linux CTF | `1.5 - 2 hrs` | 2020 | [Watcher.md](./Watcher.md) |
| **Wazuh** | SIEM & XDR | `2 hrs` | 2022 | [Wazuh.md](./Wazuh.md) |
| **Weaponization** | Red Team Weaponization | `1.5 hrs` | 2022 | [Weaponization.md](./Weaponization.md) |
| **Weasel** | WSL / Windows CTF | `1.5 hrs` | 2022 | [Weasel.md](./Weasel.md) |
| **Wekor** | SQLi / WordPress / CyberChef | `2 hrs` | 2021 | [Wekor.md](./Wekor.md) |
| **Windows Event Logs** | Windows DFIR | `2 hrs` | 2021 | [Windows Event Logs.md](./Windows%20Event%20Logs.md) |
| **Windows Forensics 1** | Windows Forensics | `1.5 hrs` | 2021 | [Windows Forensics 1.md](./Windows%20Forensics%201.md) |
| **Windows Forensics 2** | Windows Forensics | `1.5 hrs` | 2021 | [Windows Forensics 2.md](./Windows%20Forensics%202.md) |
| **Windows Internals** | Operating System Internals | `1.5 hrs` | 2021 | [Windows Internals.md](./Windows%20Internals.md) |
| **Windows Local Persistence** | Red Team Persistence | `2 hrs` | 2022 | [Windows Local Persistence.md](./Windows%20Local%20Persistence.md) |
| **Windows Privilege Escalation** | PrivEsc Fundamentals | `2 hrs` | 2020 | [Windows Privilege Escalation.md](./Windows%20Privilege%20Escalation.md) |
| **Windows Reversing Intro** | Reverse Engineering | `1.5 hrs` | 2022 | [Windows Reversing Intro.md](./Windows%20Reversing%20Intro.md) |
| **Wireshark Traffic Analysis** | Packet Analysis | `1.5 hrs` | 2021 | [Wireshark Traffic Analysis.md](./Wireshark%20Traffic%20Analysis.md) |
| **Wonderland** | Linux / Python Hijack | `1.5 hrs` | 2020 | [Wonderland.md](./Wonderland.md) |
| **Year of the rabbit** | Burp / Linux CTF | `1.5 hrs` | 2020 | [Year of the rabbit.md](./Year%20of%20the%20rabbit.md) |
| **You're in a cave** | Text Adventure CTF | `1.5 hrs` | 2020 | [You're in a cave.md](./You%27re%20in%20a%20cave.md) |
| **Zeek Exercises** | Zeek / Network DFIR | `1.5 hrs` | 2022 | [Zeek Exercises.md](./Zeek%20Exercises.md) |
| **Zeno** | Linux CTF / Restaurant CMS | `1.5 hrs` | 2021 | [Zeno.md](./Zeno.md) |
| **ZeroLogon** | CVE-2020-1472 | `45 mins` | 2020 | [ZeroLogon.md](./ZeroLogon.md) |
| **b3dr0ck** | Linux / TLS Socket CTF | `1.5 hrs` | 2021 | [b3dr0ck.md](./b3dr0ck.md) |
| **battery** | Web / PHP / Linux CTF | `1.5 hrs` | 2020 | [battery.md](./battery.md) |
| **biteme** | Linux / PHP CTF | `1.5 hrs` | 2021 | [biteme.md](./biteme.md) |
| **hackerNote** | Web / SSTI / Linux | `1.5 hrs` | 2021 | [hackerNote.md](./hackerNote.md) |
| **harder** | Git / PHP / Linux CTF | `1.5 hrs` | 2020 | [harder.md](./harder.md) |
| **iOS Forensics** | Mobile DFIR | `1.5 hrs` | 2022 | [iOS Forensics.md](./iOS%20Forensics.md) |
| **pyLon** | Python / Linux CTF | `1.5 hrs` | 2021 | [pyLon.md](./pyLon.md) |
| **toc2** | Race Condition (TOCTOU) | `1.5 hrs` | 2021 | [toc2.md](./toc2.md) |

---

## 4. Tier 4: Easy Difficulty Rooms (Foundational & Tool Mastery)

Beginner-friendly root machines, CVE reproduction labs, tool walk-throughs (Nmap, Burp Suite, Metasploit, Wireshark), and fundamental privesc.

| Room Name | Platform / Type | Est. Time / Length | Release | Writeup File |
| :--- | :--- | :---: | :---: | :--- |
| **Active Directory Basics(1)** | Walkthrough / AD | `45 - 60 mins` | 2021 | [Active Directory Basics(1).md](./Active%20Directory%20Basics%281%29.md) |
| **Active Directory Basics** | Walkthrough / AD | `45 - 60 mins` | 2021 | [Active Directory Basics.md](./Active%20Directory%20Basics.md) |
| **Agent T** | Web / CTF | `20 - 30 mins` | 2021 | [Agent T.md](./Agent%20T.md) |
| **Alfred** | Windows CTF | `1 - 1.5 hrs` | 2019 | [Alfred.md](./Alfred.md) |
| **All in One** | Linux CTF | `1 - 1.5 hrs` | 2020 | [All in One.md](./All%20in%20One.md) |
| **Anonforce** | Linux CTF | `30 - 45 mins` | 2020 | [Anonforce.md](./Anonforce.md) |
| **Archangel** | Linux CTF | `1 - 1.5 hrs` | 2020 | [Archangel.md](./Archangel.md) |
| **Atlassian, CVE-2022-26134** | CVE / Web | `30 - 45 mins` | 2022 | [Atlassian, CVE-2022-26134.md](./Atlassian%2C%20CVE-2022-26134.md) |
| **AttackerKB** | Walkthrough | `30 mins` | 2020 | [AttackerKB.md](./AttackerKB.md) |
| **Authentication Bypass** | Web Fundamentals | `45 mins` | 2021 | [Authentication Bypass.md](./Authentication%20Bypass.md) |
| **Autopsy** | DFIR | `1 - 1.5 hrs` | 2021 | [Autopsy.md](./Autopsy.md) |
| **Avengers Blog** | Web CTF | `30 - 45 mins` | 2019 | [Avengers Blog.md](./Avengers%20Blog.md) |
| **Badbyte** | Linux CTF | `1 - 1.5 hrs` | 2020 | [Badbyte.md](./Badbyte.md) |
| **Benign** | DFIR / Splunk | `45 mins` | 2022 | [Benign.md](./Benign.md) |
| **Blaster** | Windows CTF | `1 hr` | 2020 | [Blaster.md](./Blaster.md) |
| **BlockChain** | Walkthrough | `45 mins` | 2021 | [BlockChain.md](./BlockChain.md) |
| **BlueTeam** | Defensive | `45 mins` | 2020 | [BlueTeam.md](./BlueTeam.md) |
| **Bolt** | Web / CMS | `30 - 45 mins` | 2020 | [Bolt.md](./Bolt.md) |
| **Bookstore** | Linux / API CTF | `1 - 1.5 hrs` | 2020 | [Bookstore.md](./Bookstore.md) |
| **BountyHacker** | Linux CTF | `30 - 45 mins` | 2019 | [BountyHacker.md](./BountyHacker.md) |
| **Break Out The Cage** | Linux CTF | `1 hr` | 2020 | [Break Out The Cage.md](./Break%20Out%20The%20Cage.md) |
| **Brim** | DFIR / Network | `1 hr` | 2021 | [Brim.md](./Brim.md) |
| **Brooklyn Nine Nine** | Linux CTF | `45 mins` | 2020 | [Brooklyn Nine Nine.md](./Brooklyn%20Nine%20Nine.md) |
| **Brute Force Heroes** | Authentication | `45 mins` | 2022 | [Brute Force Heroes.md](./Brute%20Force%20Heroes.md) |
| **Bugged** | IoT / MQTT | `45 mins` | 2022 | [Bugged.md](./Bugged.md) |
| **Burp Suite Extender** | Web Tools | `30 - 45 mins` | 2021 | [Burp Suite Extender.md](./Burp%20Suite%20Extender.md) |
| **Burp Suite Intruder** | Web Tools | `45 mins` | 2021 | [Burp Suite Intruder.md](./Burp%20Suite%20Intruder.md) |
| **Burp Suite Other Modules** | Web Tools | `45 mins` | 2021 | [Burp Suite Other Modules.md](./Burp%20Suite%20Other%20Modules.md) |
| **CTF collection Vol.2** | Misc / Crypto CTF | `1 hr` | 2020 | [CTF collection Vol.2.md](./CTF%20collection%20Vol.2.md) |
| **CVE-2019-18634** | Linux PrivEsc | `30 mins` | 2020 | [CVE-2019-18634.md](./CVE-2019-18634.md) |
| **CVE-2021-41773** | Apache Path Traversal | `30 - 45 mins` | 2021 | [CVE-2021-41773.md](./CVE-2021-41773.md) |
| **Capture!** | Web / Captcha Bypass | `45 mins` | 2021 | [Capture!.md](./Capture%21.md) |
| **Chill Hack** | Linux CTF | `1 hr` | 2020 | [Chill Hack.md](./Chill%20Hack.md) |
| **Chocolate Factory** | Linux CTF | `1 hr` | 2020 | [Chocolate Factory.md](./Chocolate%20Factory.md) |
| **ColddBox Easy** | WordPress / Linux | `45 - 60 mins` | 2020 | [ColddBox Easy.md](./ColddBox%20Easy.md) |
| **Command Injection** | Web Pentest | `45 mins` | 2021 | [Command Injection.md](./Command%20Injection.md) |
| **Committed** | Git Forensics | `20 - 30 mins` | 2022 | [Committed.md](./Committed.md) |
| **Common Linux Privesc** | Privilege Escalation | `1.5 - 2 hrs` | 2020 | [Common Linux Privesc.md](./Common%20Linux%20Privesc.md) |
| **Confidential** | DFIR / PDF Forensics | `30 mins` | 2022 | [Confidential.md](./Confidential.md) |
| **Core Windows Processes** | Windows Forensics | `1 hr` | 2021 | [Core Windows Processes.md](./Core%20Windows%20Processes.md) |
| **Corridor** | Web / IDOR | `20 - 30 mins` | 2022 | [Corridor.md](./Corridor.md) |
| **Couch** | CouchDB Misconfig | `30 mins` | 2021 | [Couch.md](./Couch.md) |
| **Cross-site Scripting-1** | Web Fundamentals | `1 hr` | 2021 | [Cross-site Scripting-1.md](./Cross-site%20Scripting-1.md) |
| **Cross-site Scripting** | Web Fundamentals | `1 hr` | 2020 | [Cross-site Scripting.md](./Cross-site%20Scripting.md) |
| **Cyber Scotland 2021** | Event CTF | `1.5 hrs` | 2021 | [Cyber Scotland 2021.md](./Cyber%20Scotland%202021.md) |
| **CyberHeroes** | Web Authentication | `20 mins` | 2022 | [CyberHeroes.md](./CyberHeroes.md) |
| **Cyborg** | Linux / Borg Backup | `45 mins` | 2020 | [Cyborg.md](./Cyborg.md) |
| **Dav** | WebDAV Exploit | `30 mins` | 2020 | [Dav.md](./Dav.md) |
| **Develpy** | Linux / Python Esc | `45 mins` | 2020 | [Develpy.md](./Develpy.md) |
| **Dig Dug** | DNS Recon | `20 mins` | 2022 | [Dig Dug.md](./Dig%20Dug.md) |
| **Dirty Pipe** | CVE-2022-0847 Exploit | `30 - 45 mins` | 2022 | [Dirty Pipe.md](./Dirty%20Pipe.md) |
| **Easy Peasy** | Linux CTF | `45 mins` | 2020 | [Easy Peasy.md](./Easy%20Peasy.md) |
| **En-pass** | Linux CTF | `1 hr` | 2021 | [En-pass.md](./En-pass.md) |
| **Enumeration** | Reconnaissance | `1.5 hrs` | 2020 | [Enumeration.md](./Enumeration.md) |
| **Epoch** | Command Injection | `20 - 30 mins` | 2022 | [Epoch.md](./Epoch.md) |
| **Exploit Vulnerabilities** | Pentesting Basics | `45 mins` | 2021 | [Exploit Vulnerabilities.md](./Exploit%20Vulnerabilities.md) |
| **File Inclusion** | LFI / RFI Fundamentals | `1 hr` | 2021 | [File Inclusion.md](./File%20Inclusion.md) |
| **Firewalls** | Network Security | `1 hr` | 2021 | [Firewalls.md](./Firewalls.md) |
| **Follina MSDT** | CVE-2022-30190 | `30 - 45 mins` | 2022 | [Follina MSDT.md](./Follina%20MSDT.md) |
| **Fowsniff CTF** | Linux CTF | `1 hr` | 2019 | [Fowsniff CTF.md](./Fowsniff%20CTF.md) |
| **GLITCH** | Node.js / Linux CTF | `1 hr` | 2020 | [GLITCH.md](./GLITCH.md) |
| **Gallery** | Linux / Web CMS | `1 hr` | 2021 | [Gallery.md](./Gallery.md) |
| **Game Zone** | SQLi / SSH Tunneling | `1 - 1.5 hrs` | 2019 | [Game Zone.md](./Game%20Zone.md) |
| **GamingServer** | Linux CTF / PrivEsc | `1 hr` | 2020 | [GamingServer.md](./GamingServer.md) |
| **Gotta Catch'em All!** | Pokemon CTF | `30 mins` | 2020 | [Gotta Catch'em All!.md](./Gotta%20Catch%27em%20All%21.md) |
| **Hack_printer** | Printer Hacking | `20 mins` | 2020 | [Hack_printer.md](./Hack_printer.md) |
| **Hacked** | PCAP Analysis | `30 mins` | 2020 | [Hacked.md](./Hacked.md) |
| **Hacker vs. Hacker** | Web Shell Hunting | `45 mins` | 2022 | [Hacker vs. Hacker.md](./Hacker%20vs.%20Hacker.md) |
| **Hardening Basics Part 1** | Defensive Hardening | `1.5 hrs` | 2022 | [Hardening Basics Part 1.md](./Hardening%20Basics%20Part%201.md) |
| **Hardening Basics Part 2** | Defensive Hardening | `1.5 hrs` | 2022 | [Hardening Basics Part 2.md](./Hardening%20Basics%20Part%202.md) |
| **Hashing - Crypto 101** | Cryptography Basics | `45 mins` | 2020 | [Hashing - Crypto 101.md](./Hashing%20-%20Crypto%20101.md) |
| **HeartBleed** | OpenSSL Vulnerability | `45 mins` | 2020 | [HeartBleed.md](./HeartBleed.md) |
| **IDE** | Web / Linux PrivEsc | `45 mins` | 2021 | [IDE.md](./IDE.md) |
| **IDOR** | Web Security | `30 mins` | 2021 | [IDOR.md](./IDOR.md) |
| **Ignite** | Fuel CMS Exploit | `45 mins` | 2019 | [Ignite.md](./Ignite.md) |
| **Intermediate Nmap** | Recon / Nmap | `45 mins` | 2020 | [Intermediate Nmap.md](./Intermediate%20Nmap.md) |
| **Intro to C2** | C2 Frameworks | `1 hr` | 2022 | [Intro to C2.md](./Intro%20to%20C2.md) |
| **Intro to Docker** | Containers / Docker | `1 hr` | 2021 | [Intro to Docker.md](./Intro%20to%20Docker.md) |
| **Intro to Pipeline Automation** | CI/CD Security | `1 hr` | 2022 | [Intro to Pipeline Automation.md](./Intro%20to%20Pipeline%20Automation.md) |
| **Introduction To Honeypots** | Blue Team Defense | `1 hr` | 2021 | [Introduction To Honeypots.md](./Introduction%20To%20Honeypots.md) |
| **Introduction to Flask** | Web Development | `1 hr` | 2021 | [Introduction to Flask.md](./Introduction%20to%20Flask.md) |
| **Investigating with ELK 101** | ELK Stack / DFIR | `1 hr` | 2021 | [Investigating with ELK 101.md](./Investigating%20with%20ELK%20101.md) |
| **ItsyBitsy** | Log Analysis | `30 mins` | 2022 | [ItsyBitsy.md](./ItsyBitsy.md) |
| **JPGChat** | Linux / Python Injection | `30 mins` | 2021 | [JPGChat.md](./JPGChat.md) |
| **Jack-of-All-Trades** | Multi-skill CTF | `45 mins` | 2020 | [Jack-of-All-Trades.md](./Jack-of-All-Trades.md) |
| **Jason** | Node.js Deserialization | `45 mins` | 2021 | [Jason.md](./Jason.md) |
| **John The Ripper** | Password Cracking | `1 hr` | 2020 | [John The Ripper.md](./John%20The%20Ripper.md) |
| **LazyAdmin** | SweetRice CMS | `30 mins` | 2019 | [LazyAdmin.md](./LazyAdmin.md) |
| **Lesson Learned** | Incident Response | `30 mins` | 2022 | [Lesson Learned.md](./Lesson%20Learned.md) |
| **Library** | Linux CTF / Python | `45 mins` | 2020 | [Library.md](./Library.md) |
| **Linux Local Enumeration** | PrivEsc Fundamentals | `1 hr` | 2020 | [Linux Local Enumeration.md](./Linux%20Local%20Enumeration.md) |
| **Looking_Glass** | SSH / Stego CTF | `45 mins` | 2020 | [Looking_Glass.md](./Looking_Glass.md) |
| **MAL Strings** | Static Analysis | `30 mins` | 2021 | [MAL Strings.md](./MAL%20Strings.md) |
| **MD2PDF** | SSRF / XSS | `30 mins` | 2022 | [MD2PDF.md](./MD2PDF.md) |
| **Magician** | ImageMagick / Linux CTF | `1 hr` | 2021 | [Magician.md](./Magician.md) |
| **Masterminds** | Zeek / Network Traffic | `1 hr` | 2022 | [Masterminds.md](./Masterminds.md) |
| **Metasploit  Meterpreter** | Tool Walkthrough | `1 hr` | 2020 | [Metasploit  Meterpreter.md](./Metasploit%20%20Meterpreter.md) |
| **Metasploit Exploitation** | Tool Walkthrough | `1.5 hrs` | 2020 | [Metasploit Exploitation.md](./Metasploit%20Exploitation.md) |
| **Metasploit** | Tool Walkthrough | `1.5 hrs` | 2020 | [Metasploit.md](./Metasploit.md) |
| **Mr. Phisher** | Phishing Analysis | `30 mins` | 2022 | [Mr. Phisher.md](./Mr.%20Phisher.md) |
| **Mustacchio** | Linux / Web CTF | `45 mins` | 2021 | [Mustacchio.md](./Mustacchio.md) |
| **Neighbour** | IDOR Vulnerability | `20 mins` | 2022 | [Neighbour.md](./Neighbour.md) |
| **NerdHerd** | Linux CTF / Samba | `1 hr` | 2020 | [NerdHerd.md](./NerdHerd.md) |
| **Network Services 2** | NFS / SMTP / MySQL | `1.5 hrs` | 2020 | [Network Services 2.md](./Network%20Services%202.md) |
| **Network Services** | SMB / Telnet / FTP | `1.5 hrs` | 2020 | [Network Services.md](./Network%20Services.md) |
| **NetworkMiner** | PCAP Forensics | `45 mins` | 2021 | [NetworkMiner.md](./NetworkMiner.md) |
| **New Hire Old Artifacts** | DFIR / Splunk | `45 mins` | 2022 | [New Hire Old Artifacts.md](./New%20Hire%20Old%20Artifacts.md) |
| **Ninja Skills** | Linux Command Line | `45 mins` | 2020 | [Ninja Skills.md](./Ninja%20Skills.md) |
| **Nmap Basic Port Scans** | Recon / Nmap | `45 mins` | 2021 | [Nmap Basic Port Scans.md](./Nmap%20Basic%20Port%20Scans.md) |
| **OWASP Top 10 - 2021** | Web Security | `2 hrs` | 2021 | [OWASP Top 10 - 2021.md](./OWASP%20Top%2010%20-%202021.md) |
| **Opacity** | PHP Upload / KeePass | `1 hr` | 2022 | [Opacity.md](./Opacity.md) |
| **Osquery The Basics** | Endpoint Visibility | `1 hr` | 2021 | [Osquery The Basics.md](./Osquery%20The%20Basics.md) |
| **Osquery** | Endpoint Visibility | `1 hr` | 2021 | [Osquery.md](./Osquery.md) |
| **OverlayFS** | CVE-2021-3493 Exploit | `30 mins` | 2021 | [OverlayFS.md](./OverlayFS.md) |
| **Overpass** | Broken Auth / Linux CTF | `45 mins` | 2020 | [Overpass.md](./Overpass.md) |
| **Phishing1** | Email Analysis Basics | `30 mins` | 2021 | [Phishing1.md](./Phishing1.md) |
| **Polkit_CVE** | CVE-2021-3560 / CVE-2021-4034 | `30 mins` | 2021 | [Polkit_CVE.md](./Polkit_CVE.md) |
| **Poster** | PostgreSQL Exploitation | `45 mins` | 2020 | [Poster.md](./Poster.md) |
| **Putting it all together** | Network Summary | `30 mins` | 2021 | [Putting it all together.md](./Putting%20it%20all%20together.md) |
| **Pwnkit** | CVE-2021-4034 Exploit | `20 mins` | 2022 | [Pwnkit.md](./Pwnkit.md) |
| **Python for Pentesters** | Python Scripting | `1 hr` | 2021 | [Python for Pentesters.md](./Python%20for%20Pentesters.md) |
| **REmux The Tmux** | Terminal Multiplexer | `30 mins` | 2021 | [REmux The Tmux.md](./REmux%20The%20Tmux.md) |
| **Res** | Redis Exploitation | `30 mins` | 2020 | [Res.md](./Res.md) |
| **SQLMAP** | SQLi Automation | `1 hr` | 2020 | [SQLMAP.md](./SQLMAP.md) |
| **Skynet** | Linux / Samba / RFI | `1 hr` | 2019 | [Skynet.md](./Skynet.md) |
| **Smag Grotto** | PCAP / Linux CTF | `45 mins` | 2020 | [Smag Grotto.md](./Smag%20Grotto.md) |
| **Snort** | IDS Fundamentals | `1.5 hrs` | 2022 | [Snort.md](./Snort.md) |
| **Source** | Webmin CVE-2019-15107 | `30 mins` | 2020 | [Source.md](./Source.md) |
| **Splunk 101** | SIEM Fundamentals | `1.5 hrs` | 2021 | [Splunk 101.md](./Splunk%20101.md) |
| **Splunk Basics** | SIEM Intro | `45 mins` | 2021 | [Splunk Basics.md](./Splunk%20Basics.md) |
| **Startup** | Linux / Wireshark CTF | `1 hr` | 2020 | [Startup.md](./Startup.md) |
| **Steel Mountain** | Windows / Reaver | `1 hr` | 2019 | [Steel Mountain.md](./Steel%20Mountain.md) |
| **Subdomain Enumeration** | Reconnaissance | `45 mins` | 2021 | [Subdomain Enumeration.md](./Subdomain%20Enumeration.md) |
| **Surfer** | SSRF Challenge | `30 mins` | 2022 | [Surfer.md](./Surfer.md) |
| **Sysinternals** | Windows Tools | `1 hr` | 2021 | [Sysinternals.md](./Sysinternals.md) |
| **TakeOver** | Subdomain Takeover | `30 mins` | 2022 | [TakeOver.md](./TakeOver.md) |
| **Team** | Linux CTF / LFI | `1 hr` | 2020 | [Team.md](./Team.md) |
| **Tech_Supp0rt 1** | Linux / Subversion CTF | `45 mins` | 2021 | [Tech_Supp0rt 1.md](./Tech_Supp0rt%201.md) |
| **Templates** | SSTI Fundamentals | `45 mins` | 2021 | [Templates.md](./Templates.md) |
| **The Lay of the land** | Reconnaissance | `45 mins` | 2020 | [The Lay of the land.md](./The%20Lay%20of%20the%20land.md) |
| **TheHive Project** | Incident Response SOAR | `1 hr` | 2021 | [TheHive Project.md](./TheHive%20Project.md) |
| **Thompson** | Tomcat Exploitation | `30 mins` | 2020 | [Thompson.md](./Thompson.md) |
| **ToolsRus** | Basic Pentest Tools | `30 mins` | 2019 | [ToolsRus.md](./ToolsRus.md) |
| **Traffic Analysis Essentials** | Network Traffic Analysis | `1 hr` | 2022 | [Traffic Analysis Essentials.md](./Traffic%20Analysis%20Essentials.md) |
| **Training for New Analyst** | SOC Training | `1 hr` | 2022 | [Training for New Analyst.md](./Training%20for%20New%20Analyst.md) |
| **Upload Vulnerabilities** | File Upload Bypass | `1 hr` | 2020 | [Upload Vulnerabilities.md](./Upload%20Vulnerabilities.md) |
| **Vulnerability Capstone** | Capstone Lab | `45 mins` | 2021 | [Vulnerability Capstone.md](./Vulnerability%20Capstone.md) |
| **Warzone 1** | Network PCAP Analysis | `45 mins` | 2022 | [Warzone 1.md](./Warzone%201.md) |
| **Web Enumeration** | Web Reconnaissance | `1 hr` | 2021 | [Web Enumeration.md](./Web%20Enumeration.md) |
| **Wgel CTF** | Linux PrivEsc CTF | `30 mins` | 2019 | [Wgel CTF.md](./Wgel%20CTF.md) |
| **Willow** | Linux CTF | `45 mins` | 2020 | [Willow.md](./Willow.md) |
| **Wireshark 101** | Packet Analysis | `1 hr` | 2020 | [Wireshark 101.md](./Wireshark%20101.md) |
| **Wireshark Packet Operations** | Packet Analysis | `1 hr` | 2021 | [Wireshark Packet Operations.md](./Wireshark%20Packet%20Operations.md) |
| **WordPress-Cve2021** | WordPress CVE Lab | `45 mins` | 2021 | [WordPress-Cve2021.md](./WordPress-Cve2021.md) |
| **Yara** | Malware Detection Rules | `1 hr` | 2020 | [Yara.md](./Yara.md) |
| **Zeek** | Network Monitoring | `1.5 hrs` | 2022 | [Zeek.md](./Zeek.md) |

---

## 5. Tier 5: Info & Foundational Theory (Walkthrough / Concepts)

Non-root or purely educational modules detailing cybersecurity concepts, network layers, threat intelligence frameworks, and defensive models.

| Room Name | Platform / Type | Est. Time / Length | Release | Writeup File |
| :--- | :--- | :---: | :---: | :--- |
| **Careers in Cyber** | General Walkthrough | `20 mins` | 2021 | [Careers in Cyber.md](./Careers%20in%20Cyber.md) |
| **Cyber Kill Chain** | Defensive Concepts | `30 mins` | 2021 | [Cyber Kill Chain.md](./Cyber%20Kill%20Chain.md) |
| **DDOS** | Networking Basics | `20 mins` | 2020 | [DDOS.md](./DDOS.md) |
| **DFIR An Introduction** | DFIR Basics | `30 mins` | 2021 | [DFIR An Introduction.md](./DFIR%20An%20Introduction.md) |
| **DNS** | Networking Basics | `30 mins` | 2020 | [DNS.md](./DNS.md) |
| **Diamond Model** | Threat Intel | `30 mins` | 2021 | [Diamond Model.md](./Diamond%20Model.md) |
| **Extending Your Network** | Networking Basics | `30 mins` | 2021 | [Extending Your Network.md](./Extending%20Your%20Network.md) |
| **How websites work** | Web Fundamentals | `30 mins` | 2020 | [How websites work.md](./How%20websites%20work.md) |
| **Intro to Cloud Security** | Cloud Concepts | `45 mins` | 2022 | [Intro to Cloud Security.md](./Intro%20to%20Cloud%20Security.md) |
| **Intro to Containerisation** | DevOps Security | `30 mins` | 2022 | [Intro to Containerisation.md](./Intro%20to%20Containerisation.md) |
| **Intro to Cyber Threat Intel** | Threat Intelligence | `30 mins` | 2022 | [Intro to Cyber Threat Intel.md](./Intro%20to%20Cyber%20Threat%20Intel.md) |
| **Intro to Defensive Security** | Blue Team Basics | `30 mins` | 2021 | [Intro to Defensive Security.md](./Intro%20to%20Defensive%20Security.md) |
| **Intro to Endpoint Security** | Endpoint Defense | `30 mins` | 2022 | [Intro to Endpoint Security.md](./Intro%20to%20Endpoint%20Security.md) |
| **Intro to ISAC** | Information Sharing | `30 mins` | 2022 | [Intro to ISAC.md](./Intro%20to%20ISAC.md) |
| **Intro to Offensive Security** | Red Team Basics | `20 mins` | 2021 | [Intro to Offensive Security.md](./Intro%20to%20Offensive%20Security.md) |
| **Introduction to SIEM** | SOC Monitoring | `30 mins` | 2021 | [Introduction to SIEM.md](./Introduction%20to%20SIEM.md) |
| **Junior Security Analyst Intro** | SOC Analyst Path | `30 mins` | 2022 | [Junior Security Analyst Intro.md](./Junior%20Security%20Analyst%20Intro.md) |
| **Network Security** | Networking Basics | `30 mins` | 2020 | [Network Security.md](./Network%20Security.md) |
| **OSI Model** | Networking Basics | `30 mins` | 2020 | [OSI Model.md](./OSI%20Model.md) |
| **Operating System Security** | Security Basics | `30 mins` | 2021 | [Operating System Security.md](./Operating%20System%20Security.md) |
| **Packets & Frames** | Networking Basics | `30 mins` | 2021 | [Packets & Frames.md](./Packets%20%26%20Frames.md) |
| **Phishing** | Social Engineering | `30 mins` | 2021 | [Phishing.md](./Phishing.md) |
| **Protocols and Servers 2** | Networking Basics | `30 mins` | 2021 | [Protocols and Servers 2.md](./Protocols%20and%20Servers%202.md) |
| **Protocols and Servers** | Networking Basics | `30 mins` | 2021 | [Protocols and Servers.md](./Protocols%20and%20Servers.md) |
| **Pyramid Of Pain** | Threat Intel Concept | `30 mins` | 2021 | [Pyramid Of Pain.md](./Pyramid%20Of%20Pain.md) |
| **Security Engineer Intro** | Engineering Career | `30 mins` | 2022 | [Security Engineer Intro.md](./Security%20Engineer%20Intro.md) |
| **Security Operations** | SOC Overview | `30 mins` | 2021 | [Security Operations.md](./Security%20Operations.md) |
| **Security Principles** | Security Basics | `30 mins` | 2021 | [Security Principles.md](./Security%20Principles.md) |
| **TOR** | Anonymity / TOR | `20 mins` | 2020 | [TOR.md](./TOR.md) |
| **Tmux** | Linux Utilities | `20 mins` | 2020 | [Tmux.md](./Tmux.md) |
| **Unified Kill Chain** | Threat Modeling | `30 mins` | 2021 | [Unified Kill Chain.md](./Unified%20Kill%20Chain.md) |
| **x86 Architecture Overview** | Reverse Engineering | `45 mins` | 2021 | [x86 Architecture Overview.md](./x86%20Architecture%20Overview.md) |

---

## 6. Chronological Release Timeline (2019 — 2023+)

Track rooms chronologically to understand when techniques, CVEs, and defensive architectures were added to TryHackMe & HackTheBox platforms.

### 2019 Releases (18 Rooms)
| Room Name | Difficulty | Est. Time | Focus Area | Writeup Link |
| :--- | :---: | :---: | :--- | :--- |
| **Daily Bugle** | `Hard` | `2 - 3 hrs` | Joomla / SQLi / Linux | [Daily Bugle.md](./Daily%20Bugle.md) |
| **Retro** | `Hard` | `2 hrs` | Windows / CVE-2019-1388 | [Retro.md](./Retro.md) |
| **Boiler CTF** | `Medium` | `1.5 - 2 hrs` | Linux CTF | [Boiler CTF.md](./Boiler%20CTF.md) |
| **Brainstorm** | `Medium` | `1.5 - 2.5 hrs` | Buffer Overflow / Windows | [Brainstorm.md](./Brainstorm.md) |
| **CCT2019** | `Medium` | `1.5 - 2 hrs` | CTF Challenge | [CCT2019.md](./CCT2019.md) |
| **GoldenEye** | `Medium` | `2 - 3 hrs` | Linux / Pop3 / CTF | [GoldenEye.md](./GoldenEye.md) |
| **HackPark** | `Medium` | `1.5 - 2.5 hrs` | Windows / Hydra / WinPE | [HackPark.md](./HackPark.md) |
| **Alfred** | `Easy` | `1 - 1.5 hrs` | Windows CTF | [Alfred.md](./Alfred.md) |
| **Avengers Blog** | `Easy` | `30 - 45 mins` | Web CTF | [Avengers Blog.md](./Avengers%20Blog.md) |
| **BountyHacker** | `Easy` | `30 - 45 mins` | Linux CTF | [BountyHacker.md](./BountyHacker.md) |
| **Fowsniff CTF** | `Easy` | `1 hr` | Linux CTF | [Fowsniff CTF.md](./Fowsniff%20CTF.md) |
| **Game Zone** | `Easy` | `1 - 1.5 hrs` | SQLi / SSH Tunneling | [Game Zone.md](./Game%20Zone.md) |
| **Ignite** | `Easy` | `45 mins` | Fuel CMS Exploit | [Ignite.md](./Ignite.md) |
| **LazyAdmin** | `Easy` | `30 mins` | SweetRice CMS | [LazyAdmin.md](./LazyAdmin.md) |
| **Skynet** | `Easy` | `1 hr` | Linux / Samba / RFI | [Skynet.md](./Skynet.md) |
| **Steel Mountain** | `Easy` | `1 hr` | Windows / Reaver | [Steel Mountain.md](./Steel%20Mountain.md) |
| **ToolsRus** | `Easy` | `30 mins` | Basic Pentest Tools | [ToolsRus.md](./ToolsRus.md) |
| **Wgel CTF** | `Easy` | `30 mins` | Linux PrivEsc CTF | [Wgel CTF.md](./Wgel%20CTF.md) |


### 2020 Releases (126 Rooms)
| Room Name | Difficulty | Est. Time | Focus Area | Writeup Link |
| :--- | :---: | :---: | :--- | :--- |
| **Anonymous Playground** | `Hard` | `2 - 3 hrs` | Reverse Engineering / CTF | [Anonymous Playground.md](./Anonymous%20Playground.md) |
| **BioHazard** | `Hard` | `3 - 4 hrs` | Multi-stage CTF | [BioHazard.md](./BioHazard.md) |
| **Brainpan 1** | `Hard` | `2.5 - 3.5 hrs` | Buffer Overflow / CTF | [Brainpan 1.md](./Brainpan%201.md) |
| **Enterprise** | `Hard` | `3 - 4 hrs` | Buffer Overflow / Linux | [Enterprise.md](./Enterprise.md) |
| **HA Joker CTF** | `Hard` | `3 - 4 hrs` | Multi-level CTF | [HA Joker CTF.md](./HA%20Joker%20CTF.md) |
| **Internal** | `Hard` | `2.5 - 3.5 hrs` | AD / WordPress / Jenkins | [Internal.md](./Internal.md) |
| **Set** | `Hard` | `2 hrs` | Social Engineering Toolkit | [Set.md](./Set.md) |
| **The Server From Hell** | `Hard` | `2.5 hrs` | Tarpit / Port Scanning | [The Server From Hell.md](./The%20Server%20From%20Hell.md) |
| **Year of the Dog** | `Hard` | `2.5 - 3.5 hrs` | 2FA Bypass / Linux CTF | [Year of the Dog.md](./Year%20of%20the%20Dog.md) |
| **Year of the Fox** | `Hard` | `2.5 - 3.5 hrs` | Samba / SQLi CTF | [Year of the Fox.md](./Year%20of%20the%20Fox.md) |
| **Year of the Jellyfish** | `Hard` | `3 - 4 hrs` | Hardened Linux CTF | [Year of the Jellyfish.md](./Year%20of%20the%20Jellyfish.md) |
| **Year of the Owl** | `Hard` | `2.5 - 3.5 hrs` | Windows PrivEsc CTF | [Year of the Owl.md](./Year%20of%20the%20Owl.md) |
| **Year of the Pig** | `Hard` | `2.5 - 3.5 hrs` | Web / Linux CTF | [Year of the Pig.md](./Year%20of%20the%20Pig.md) |
| **ret2libc** | `Hard` | `2.5 - 3.5 hrs` | Binary Exploitation / ROP | [ret2libc.md](./ret2libc.md) |
| **0day** | `Medium` | `1 - 2 hrs` | Linux CTF | [0day.md](./0day.md) |
| **Anonymous** | `Medium` | `1 - 1.5 hrs` | Linux CTF | [Anonymous.md](./Anonymous.md) |
| **BinaryHeaven** | `Medium` | `2 - 3 hrs` | Binary Exploitation | [BinaryHeaven.md](./BinaryHeaven.md) |
| **Binex** | `Medium` | `2 - 3 hrs` | Binary Exploitation | [Binex.md](./Binex.md) |
| **Blog** | `Medium` | `1.5 - 2 hrs` | Linux / WordPress | [Blog.md](./Blog.md) |
| **Brute** | `Medium` | `1 - 1.5 hrs` | Linux / Brute | [Brute.md](./Brute.md) |
| **Buffer Overflow Prep** | `Medium` | `3 - 5 hrs` | OSCP Prep / BoF | [Buffer Overflow Prep.md](./Buffer%20Overflow%20Prep.md) |
| **Buffer Overflows** | `Medium` | `2 - 3 hrs` | Binary / BoF | [Buffer Overflows.md](./Buffer%20Overflows.md) |
| **CMesS** | `Medium` | `1 - 1.5 hrs` | Linux CTF | [CMesS.md](./CMesS.md) |
| **ConvertMyVideo** | `Medium` | `1 hr` | Web / Command Injection | [ConvertMyVideo.md](./ConvertMyVideo.md) |
| **Cooctus Stories** | `Medium` | `1.5 - 2 hrs` | Web CTF | [Cooctus Stories.md](./Cooctus%20Stories.md) |
| **Crocc Crew** | `Medium` | `1.5 - 2 hrs` | Web CTF | [Crocc Crew.md](./Crocc%20Crew.md) |
| **Different CTF** | `Medium` | `1.5 hrs` | CTF Challenge | [Different CTF.md](./Different%20CTF.md) |
| **Gatekeeper** | `Medium` | `2 - 3 hrs` | Buffer Overflow / Windows | [Gatekeeper.md](./Gatekeeper.md) |
| **Hacking with PowerShell** | `Medium` | `2 - 3 hrs` | PowerShell Red Team | [Hacking with PowerShell.md](./Hacking%20with%20PowerShell.md) |
| **HaskHell** | `Medium` | `1.5 hrs` | Haskell / Linux CTF | [HaskHell.md](./HaskHell.md) |
| **Inferno** | `Medium` | `1.5 hrs` | Linux CTF / Codiad | [Inferno.md](./Inferno.md) |
| **Introduction to Cryptography** | `Medium` | `2 hrs` | Applied Crypto | [Introduction to Cryptography.md](./Introduction%20to%20Cryptography.md) |
| **Iron Corp** | `Medium` | `1.5 - 2 hrs` | Windows CTF | [Iron Corp.md](./Iron%20Corp.md) |
| **Jack** | `Medium` | `2 hrs` | WordPress / FastCGI CTF | [Jack.md](./Jack.md) |
| **Jacob the Boss** | `Medium` | `1 - 1.5 hrs` | JBoss Exploitation | [Jacob the Boss.md](./Jacob%20the%20Boss.md) |
| **Jeff** | `Medium` | `1.5 - 2 hrs` | WordPress / Linux CTF | [Jeff.md](./Jeff.md) |
| **Jurassic Park** | `Medium` | `1.5 hrs` | SQLi / Linux CTF | [Jurassic Park.md](./Jurassic%20Park.md) |
| **Keldagrim** | `Medium` | `1.5 hrs` | Linux CTF | [Keldagrim.md](./Keldagrim.md) |
| **KoTH Food CTF** | `Medium` | `1.5 hrs` | King of the Hill | [KoTH Food CTF.md](./KoTH%20Food%20CTF.md) |
| **KoTH Hackers** | `Medium` | `1.5 hrs` | King of the Hill | [KoTH Hackers.md](./KoTH%20Hackers.md) |
| **One Piece** | `Medium` | `1.5 hrs` | Anime CTF / Linux | [One Piece.md](./One%20Piece.md) |
| **Overpass3** | `Medium` | `1.5 hrs` | Web / GPG / Linux CTF | [Overpass3.md](./Overpass3.md) |
| **PowerShell for Pentesters** | `Medium` | `2 hrs` | PowerShell Scripting | [PowerShell for Pentesters.md](./PowerShell%20for%20Pentesters.md) |
| **Relevant** | `Medium` | `1.5 - 2 hrs` | Windows / PrintSpoofer CTF | [Relevant.md](./Relevant.md) |
| **Revenge** | `Medium` | `1.5 hrs` | SQLi / Linux CTF | [Revenge.md](./Revenge.md) |
| **SQHell** | `Medium` | `2 hrs` | Advanced SQLi | [SQHell.md](./SQHell.md) |
| **Scripting** | `Medium` | `1.5 hrs` | Python / Network Sockets | [Scripting.md](./Scripting.md) |
| **Super-Spam** | `Medium` | `1.5 hrs` | Email / Web CTF | [Super-Spam.md](./Super-Spam.md) |
| **Sustah** | `Medium` | `1.5 hrs` | Linux / Rate Limiting | [Sustah.md](./Sustah.md) |
| **The Cod Caper** | `Medium` | `2 hrs` | Buffer Overflow / Linux | [The Cod Caper.md](./The%20Cod%20Caper.md) |
| **The Impossible Challenge** | `Medium` | `1.5 hrs` | Reverse Engineering | [The Impossible Challenge.md](./The%20Impossible%20Challenge.md) |
| **Tony the Tiger** | `Medium` | `1.5 hrs` | JBoss / Linux CTF | [Tony the Tiger.md](./Tony%20the%20Tiger.md) |
| **Unattended** | `Medium` | `1.5 hrs` | Linux CTF | [Unattended.md](./Unattended.md) |
| **Volatility** | `Medium` | `2 hrs` | Memory Forensics | [Volatility.md](./Volatility.md) |
| **Watcher** | `Medium` | `1.5 - 2 hrs` | Boot2Root / Linux CTF | [Watcher.md](./Watcher.md) |
| **Windows Privilege Escalation** | `Medium` | `2 hrs` | PrivEsc Fundamentals | [Windows Privilege Escalation.md](./Windows%20Privilege%20Escalation.md) |
| **Wonderland** | `Medium` | `1.5 hrs` | Linux / Python Hijack | [Wonderland.md](./Wonderland.md) |
| **Year of the rabbit** | `Medium` | `1.5 hrs` | Burp / Linux CTF | [Year of the rabbit.md](./Year%20of%20the%20rabbit.md) |
| **You're in a cave** | `Medium` | `1.5 hrs` | Text Adventure CTF | [You're in a cave.md](./You%27re%20in%20a%20cave.md) |
| **ZeroLogon** | `Medium` | `45 mins` | CVE-2020-1472 | [ZeroLogon.md](./ZeroLogon.md) |
| **battery** | `Medium` | `1.5 hrs` | Web / PHP / Linux CTF | [battery.md](./battery.md) |
| **harder** | `Medium` | `1.5 hrs` | Git / PHP / Linux CTF | [harder.md](./harder.md) |
| **All in One** | `Easy` | `1 - 1.5 hrs` | Linux CTF | [All in One.md](./All%20in%20One.md) |
| **Anonforce** | `Easy` | `30 - 45 mins` | Linux CTF | [Anonforce.md](./Anonforce.md) |
| **Archangel** | `Easy` | `1 - 1.5 hrs` | Linux CTF | [Archangel.md](./Archangel.md) |
| **AttackerKB** | `Easy` | `30 mins` | Walkthrough | [AttackerKB.md](./AttackerKB.md) |
| **Badbyte** | `Easy` | `1 - 1.5 hrs` | Linux CTF | [Badbyte.md](./Badbyte.md) |
| **Blaster** | `Easy` | `1 hr` | Windows CTF | [Blaster.md](./Blaster.md) |
| **BlueTeam** | `Easy` | `45 mins` | Defensive | [BlueTeam.md](./BlueTeam.md) |
| **Bolt** | `Easy` | `30 - 45 mins` | Web / CMS | [Bolt.md](./Bolt.md) |
| **Bookstore** | `Easy` | `1 - 1.5 hrs` | Linux / API CTF | [Bookstore.md](./Bookstore.md) |
| **Break Out The Cage** | `Easy` | `1 hr` | Linux CTF | [Break Out The Cage.md](./Break%20Out%20The%20Cage.md) |
| **Brooklyn Nine Nine** | `Easy` | `45 mins` | Linux CTF | [Brooklyn Nine Nine.md](./Brooklyn%20Nine%20Nine.md) |
| **CTF collection Vol.2** | `Easy` | `1 hr` | Misc / Crypto CTF | [CTF collection Vol.2.md](./CTF%20collection%20Vol.2.md) |
| **CVE-2019-18634** | `Easy` | `30 mins` | Linux PrivEsc | [CVE-2019-18634.md](./CVE-2019-18634.md) |
| **Chill Hack** | `Easy` | `1 hr` | Linux CTF | [Chill Hack.md](./Chill%20Hack.md) |
| **Chocolate Factory** | `Easy` | `1 hr` | Linux CTF | [Chocolate Factory.md](./Chocolate%20Factory.md) |
| **ColddBox Easy** | `Easy` | `45 - 60 mins` | WordPress / Linux | [ColddBox Easy.md](./ColddBox%20Easy.md) |
| **Common Linux Privesc** | `Easy` | `1.5 - 2 hrs` | Privilege Escalation | [Common Linux Privesc.md](./Common%20Linux%20Privesc.md) |
| **Cross-site Scripting** | `Easy` | `1 hr` | Web Fundamentals | [Cross-site Scripting.md](./Cross-site%20Scripting.md) |
| **Cyborg** | `Easy` | `45 mins` | Linux / Borg Backup | [Cyborg.md](./Cyborg.md) |
| **Dav** | `Easy` | `30 mins` | WebDAV Exploit | [Dav.md](./Dav.md) |
| **Develpy** | `Easy` | `45 mins` | Linux / Python Esc | [Develpy.md](./Develpy.md) |
| **Easy Peasy** | `Easy` | `45 mins` | Linux CTF | [Easy Peasy.md](./Easy%20Peasy.md) |
| **Enumeration** | `Easy` | `1.5 hrs` | Reconnaissance | [Enumeration.md](./Enumeration.md) |
| **GLITCH** | `Easy` | `1 hr` | Node.js / Linux CTF | [GLITCH.md](./GLITCH.md) |
| **GamingServer** | `Easy` | `1 hr` | Linux CTF / PrivEsc | [GamingServer.md](./GamingServer.md) |
| **Gotta Catch'em All!** | `Easy` | `30 mins` | Pokemon CTF | [Gotta Catch'em All!.md](./Gotta%20Catch%27em%20All%21.md) |
| **Hack_printer** | `Easy` | `20 mins` | Printer Hacking | [Hack_printer.md](./Hack_printer.md) |
| **Hacked** | `Easy` | `30 mins` | PCAP Analysis | [Hacked.md](./Hacked.md) |
| **Hashing - Crypto 101** | `Easy` | `45 mins` | Cryptography Basics | [Hashing - Crypto 101.md](./Hashing%20-%20Crypto%20101.md) |
| **HeartBleed** | `Easy` | `45 mins` | OpenSSL Vulnerability | [HeartBleed.md](./HeartBleed.md) |
| **Intermediate Nmap** | `Easy` | `45 mins` | Recon / Nmap | [Intermediate Nmap.md](./Intermediate%20Nmap.md) |
| **Jack-of-All-Trades** | `Easy` | `45 mins` | Multi-skill CTF | [Jack-of-All-Trades.md](./Jack-of-All-Trades.md) |
| **John The Ripper** | `Easy` | `1 hr` | Password Cracking | [John The Ripper.md](./John%20The%20Ripper.md) |
| **Library** | `Easy` | `45 mins` | Linux CTF / Python | [Library.md](./Library.md) |
| **Linux Local Enumeration** | `Easy` | `1 hr` | PrivEsc Fundamentals | [Linux Local Enumeration.md](./Linux%20Local%20Enumeration.md) |
| **Looking_Glass** | `Easy` | `45 mins` | SSH / Stego CTF | [Looking_Glass.md](./Looking_Glass.md) |
| **Metasploit** | `Easy` | `1.5 hrs` | Tool Walkthrough | [Metasploit.md](./Metasploit.md) |
| **Metasploit  Meterpreter** | `Easy` | `1 hr` | Tool Walkthrough | [Metasploit  Meterpreter.md](./Metasploit%20%20Meterpreter.md) |
| **Metasploit Exploitation** | `Easy` | `1.5 hrs` | Tool Walkthrough | [Metasploit Exploitation.md](./Metasploit%20Exploitation.md) |
| **NerdHerd** | `Easy` | `1 hr` | Linux CTF / Samba | [NerdHerd.md](./NerdHerd.md) |
| **Network Services** | `Easy` | `1.5 hrs` | SMB / Telnet / FTP | [Network Services.md](./Network%20Services.md) |
| **Network Services 2** | `Easy` | `1.5 hrs` | NFS / SMTP / MySQL | [Network Services 2.md](./Network%20Services%202.md) |
| **Ninja Skills** | `Easy` | `45 mins` | Linux Command Line | [Ninja Skills.md](./Ninja%20Skills.md) |
| **Overpass** | `Easy` | `45 mins` | Broken Auth / Linux CTF | [Overpass.md](./Overpass.md) |
| **Poster** | `Easy` | `45 mins` | PostgreSQL Exploitation | [Poster.md](./Poster.md) |
| **Res** | `Easy` | `30 mins` | Redis Exploitation | [Res.md](./Res.md) |
| **SQLMAP** | `Easy` | `1 hr` | SQLi Automation | [SQLMAP.md](./SQLMAP.md) |
| **Smag Grotto** | `Easy` | `45 mins` | PCAP / Linux CTF | [Smag Grotto.md](./Smag%20Grotto.md) |
| **Source** | `Easy` | `30 mins` | Webmin CVE-2019-15107 | [Source.md](./Source.md) |
| **Startup** | `Easy` | `1 hr` | Linux / Wireshark CTF | [Startup.md](./Startup.md) |
| **Team** | `Easy` | `1 hr` | Linux CTF / LFI | [Team.md](./Team.md) |
| **The Lay of the land** | `Easy` | `45 mins` | Reconnaissance | [The Lay of the land.md](./The%20Lay%20of%20the%20land.md) |
| **Thompson** | `Easy` | `30 mins` | Tomcat Exploitation | [Thompson.md](./Thompson.md) |
| **Upload Vulnerabilities** | `Easy` | `1 hr` | File Upload Bypass | [Upload Vulnerabilities.md](./Upload%20Vulnerabilities.md) |
| **Willow** | `Easy` | `45 mins` | Linux CTF | [Willow.md](./Willow.md) |
| **Wireshark 101** | `Easy` | `1 hr` | Packet Analysis | [Wireshark 101.md](./Wireshark%20101.md) |
| **Yara** | `Easy` | `1 hr` | Malware Detection Rules | [Yara.md](./Yara.md) |
| **DDOS** | `Info` | `20 mins` | Networking Basics | [DDOS.md](./DDOS.md) |
| **DNS** | `Info` | `30 mins` | Networking Basics | [DNS.md](./DNS.md) |
| **How websites work** | `Info` | `30 mins` | Web Fundamentals | [How websites work.md](./How%20websites%20work.md) |
| **Network Security** | `Info` | `30 mins` | Networking Basics | [Network Security.md](./Network%20Security.md) |
| **OSI Model** | `Info` | `30 mins` | Networking Basics | [OSI Model.md](./OSI%20Model.md) |
| **TOR** | `Info` | `20 mins` | Anonymity / TOR | [TOR.md](./TOR.md) |
| **Tmux** | `Info` | `20 mins` | Linux Utilities | [Tmux.md](./Tmux.md) |


### 2021 Releases (167 Rooms)
| Room Name | Difficulty | Est. Time | Focus Area | Writeup Link |
| :--- | :---: | :---: | :--- | :--- |
| **Holo** | `Insane` | `6 - 10 hrs` | Network Lab / Multi-node | [Holo.md](./Holo.md) |
| **Wreath** | `Insane` | `6 - 10 hrs` | Enterprise Network Pivoting Lab | [Wreath.md](./Wreath.md) |
| **Carpe Diem 1** | `Hard` | `2.5 - 3.5 hrs` | Linux / Privilege Escalation | [Carpe Diem 1.md](./Carpe%20Diem%201.md) |
| **Corp** | `Hard` | `3 - 4 hrs` | Active Directory | [Corp.md](./Corp.md) |
| **Ghizer** | `Hard` | `3 - 4 hrs` | Multi-stage Linux CTF | [Ghizer.md](./Ghizer.md) |
| **HipFlask** | `Hard` | `3 - 4 hrs` | Binary / Web CTF | [HipFlask.md](./HipFlask.md) |
| **Insekube** | `Hard` | `3 - 4 hrs` | Kubernetes Pentest | [Insekube.md](./Insekube.md) |
| **Olympus** | `Hard` | `2.5 - 3.5 hrs` | Web / Linux CTF | [Olympus.md](./Olympus.md) |
| **Osiris** | `Hard` | `3 - 4 hrs` | Active Directory / CTF | [Osiris.md](./Osiris.md) |
| **Ra** | `Hard` | `3 - 4 hrs` | Active Directory / Windmill | [Ra.md](./Ra.md) |
| **RazorBlack** | `Hard` | `3 - 4 hrs` | Active Directory Lab | [RazorBlack.md](./RazorBlack.md) |
| **Red** | `Hard` | `3 - 4 hrs` | Multi-stage Linux CTF | [Red.md](./Red.md) |
| **Sea Surfer** | `Hard` | `2.5 - 3.5 hrs` | SSRF / Gitea / Linux | [Sea Surfer.md](./Sea%20Surfer.md) |
| **Tempus Fugit Durius** | `Hard` | `3 hrs` | Linux / Advanced CTF | [Tempus Fugit Durius.md](./Tempus%20Fugit%20Durius.md) |
| **Theseus** | `Hard` | `3 hrs` | Linux / Advanced CTF | [Theseus.md](./Theseus.md) |
| **VulnNet Endgame** | `Hard` | `3.5 - 5 hrs` | Active Directory / Enterprise | [VulnNet Endgame.md](./VulnNet%20Endgame.md) |
| **Annie** | `Medium` | `1 - 2 hrs` | Linux CTF | [Annie.md](./Annie.md) |
| **Attacking Kerberos** | `Medium` | `2 - 3 hrs` | Active Directory | [Attacking Kerberos.md](./Attacking%20Kerberos.md) |
| **Bebop** | `Medium` | `1 - 1.5 hrs` | Linux CTF | [Bebop.md](./Bebop.md) |
| **CMSpit** | `Medium` | `1 - 1.5 hrs` | CMS Exploitation | [CMSpit.md](./CMSpit.md) |
| **Cat Pictures** | `Medium` | `1.5 - 2 hrs` | Steganography / Linux | [Cat Pictures.md](./Cat%20Pictures.md) |
| **Cat Pictures 2** | `Medium` | `1.5 - 2 hrs` | Steganography / Linux | [Cat Pictures 2.md](./Cat%20Pictures%202.md) |
| **Crylo** | `Medium` | `1.5 - 2 hrs` | Crypto / Linux | [Crylo.md](./Crylo.md) |
| **CyberCrafted** | `Medium` | `2 - 3 hrs` | Minecraft / Linux CTF | [CyberCrafted.md](./CyberCrafted.md) |
| **Debug** | `Medium` | `1.5 - 2 hrs` | PHP Deserialization | [Debug.md](./Debug.md) |
| **Deja Vu** | `Medium` | `1.5 - 2 hrs` | Linux CTF | [Deja Vu.md](./Deja%20Vu.md) |
| **Digital Forensics Case B4DM755** | `Medium` | `1.5 - 2 hrs` | DFIR Case | [Digital Forensics Case B4DM755.md](./Digital%20Forensics%20Case%20B4DM755.md) |
| **Empire** | `Medium` | `2 hrs` | PowerShell Empire C2 | [Empire.md](./Empire.md) |
| **Empline** | `Medium` | `1.5 - 2 hrs` | Linux / Asterisk CTF | [Empline.md](./Empline.md) |
| **Erit Securus I** | `Medium` | `1.5 - 2 hrs` | Linux CTF | [Erit Securus I.md](./Erit%20Securus%20I.md) |
| **Flatline** | `Medium` | `1.5 hrs` | FreePBX / Linux | [Flatline.md](./Flatline.md) |
| **Flip** | `Medium` | `1.5 - 2 hrs` | Crypto / CBC Bit-flipping | [Flip.md](./Flip.md) |
| **Fusion Corp** | `Medium` | `2 - 3 hrs` | Active Directory | [Fusion Corp.md](./Fusion%20Corp.md) |
| **Generic University** | `Medium` | `1.5 hrs` | Web / Linux CTF | [Generic University.md](./Generic%20University.md) |
| **Git_crumpets** | `Medium` | `1.5 hrs` | Git / Web Exploitation | [Git_crumpets.md](./Git_crumpets.md) |
| **Grep** | `Medium` | `1.5 hrs` | Linux PrivEsc | [Grep.md](./Grep.md) |
| **Hamlet** | `Medium` | `1.5 hrs` | Linux CTF | [Hamlet.md](./Hamlet.md) |
| **Incident handling with Splunk** | `Medium` | `2 hrs` | SOC / Splunk | [Incident handling with Splunk.md](./Incident%20handling%20with%20Splunk.md) |
| **Intro To Pwntools** | `Medium` | `2 hrs` | Exploit Dev / Python | [Intro To Pwntools.md](./Intro%20To%20Pwntools.md) |
| **Intro to Malware Analysis** | `Medium` | `1.5 - 2 hrs` | Malware Analysis | [Intro to Malware Analysis.md](./Intro%20to%20Malware%20Analysis.md) |
| **Intrusion Detection** | `Medium` | `2 - 3 hrs` | Snort / Suricata IDS | [Intrusion Detection.md](./Intrusion%20Detection.md) |
| **Kubernetes for Everyone** | `Medium` | `2 hrs` | Kubernetes Security | [Kubernetes for Everyone.md](./Kubernetes%20for%20Everyone.md) |
| **Lockdown** | `Medium` | `1.5 hrs` | Linux CTF | [Lockdown.md](./Lockdown.md) |
| **Lumberjack Turtle** | `Medium` | `1.5 hrs` | Log4j / CVE-2021-44228 | [Lumberjack Turtle.md](./Lumberjack%20Turtle.md) |
| **Lunizz CTF** | `Medium` | `1.5 hrs` | Linux CTF | [Lunizz CTF.md](./Lunizz%20CTF.md) |
| **MAL REMnux The Redux** | `Medium` | `1.5 hrs` | Malware Analysis | [MAL REMnux The Redux.md](./MAL%20REMnux%20The%20Redux.md) |
| **Madeye's Castle** | `Medium` | `1.5 - 2 hrs` | Linux CTF | [Madeye's Castle.md](./Madeye%27s%20Castle.md) |
| **Mindgames** | `Medium` | `1.5 hrs` | Brainfuck / Python PrivEsc | [Mindgames.md](./Mindgames.md) |
| **Minotaur's Labyrinth** | `Medium` | `1.5 hrs` | Web / SQLi CTF | [Minotaur's Labyrinth.md](./Minotaur%27s%20Labyrinth.md) |
| **NIS - Linux Part I** | `Medium` | `1.5 hrs` | Network Services | [NIS - Linux Part I.md](./NIS%20-%20Linux%20Part%20I.md) |
| **Net Sec Challenge** | `Medium` | `1.5 hrs` | Network Challenge | [Net Sec Challenge.md](./Net%20Sec%20Challenge.md) |
| **Nmap Advanced Port Scans** | `Medium` | `1 hr` | Recon / Nmap | [Nmap Advanced Port Scans.md](./Nmap%20Advanced%20Port%20Scans.md) |
| **Nmap Post Port Scans** | `Medium` | `1 hr` | Recon / Nmap | [Nmap Post Port Scans.md](./Nmap%20Post%20Port%20Scans.md) |
| **NoNameCTF** | `Medium` | `1.5 hrs` | Linux CTF | [NoNameCTF.md](./NoNameCTF.md) |
| **NoSQL injection Basics** | `Medium` | `1 hr` | Web / NoSQLi | [NoSQL injection Basics.md](./NoSQL%20injection%20Basics.md) |
| **Oh My WebServer** | `Medium` | `1 hr` | CVE-2021-42013 / Docker | [Oh My WebServer.md](./Oh%20My%20WebServer.md) |
| **Plotted-TMS** | `Medium` | `1.5 - 2 hrs` | Traffic Management CMS | [Plotted-TMS.md](./Plotted-TMS.md) |
| **PrintNightmare** | `Medium` | `1 hr` | CVE-2021-1675 / 34527 | [PrintNightmare.md](./PrintNightmare.md) |
| **PrintNightmare, again!** | `Medium` | `45 mins` | CVE-2021-34527 | [PrintNightmare, again!.md](./PrintNightmare%2C%20again%21.md) |
| **PrintNightmare, thrice!** | `Medium` | `45 mins` | CVE-2021-36958 | [PrintNightmare, thrice!.md](./PrintNightmare%2C%20thrice%21.md) |
| **Recovery** | `Medium` | `2 hrs` | Windows / Web CTF | [Recovery.md](./Recovery.md) |
| **Redline** | `Medium` | `1.5 hrs` | Memory & Endpoint DFIR | [Redline.md](./Redline.md) |
| **Revil_Corp** | `Medium` | `1.5 hrs` | Ransomware Analysis | [Revil_Corp.md](./Revil_Corp.md) |
| **Road** | `Medium` | `1.5 hrs` | Web / MongoDB / Docker | [Road.md](./Road.md) |
| **SSRF** | `Medium` | `1 hr` | Server-Side Request Forgery | [SSRF.md](./SSRF.md) |
| **Secret Recipe** | `Medium` | `1.5 hrs` | Memory Forensics | [Secret Recipe.md](./Secret%20Recipe.md) |
| **Splunk 2** | `Medium` | `1.5 hrs` | SIEM Querying | [Splunk 2.md](./Splunk%202.md) |
| **Sweettooth Inc.** | `Medium` | `1.5 hrs` | Docker / Linux CTF | [Sweettooth Inc..md](./Sweettooth%20Inc..md) |
| **Sysmon** | `Medium` | `1.5 hrs` | Windows Logging | [Sysmon.md](./Sysmon.md) |
| **Takedown** | `Medium` | `2 hrs` | Active Directory / CTF | [Takedown.md](./Takedown.md) |
| **Temple** | `Medium` | `1.5 hrs` | Flask SSTI / Linux CTF | [Temple.md](./Temple.md) |
| **That's The Ticket** | `Medium` | `1.5 hrs` | Kerberos / Web | [That's The Ticket.md](./That%27s%20The%20Ticket.md) |
| **The Blob Blog** | `Medium` | `1.5 hrs` | Web / Node.js CTF | [The Blob Blog.md](./The%20Blob%20Blog.md) |
| **The Docker Rodeo** | `Medium` | `1.5 hrs` | Docker Escape CTF | [The Docker Rodeo.md](./The%20Docker%20Rodeo.md) |
| **The Great Escape** | `Medium` | `1.5 hrs` | Docker Escape CTF | [The Great Escape.md](./The%20Great%20Escape.md) |
| **Tokyo Ghoul** | `Medium` | `1.5 hrs` | Python Jail / Linux CTF | [Tokyo Ghoul.md](./Tokyo%20Ghoul.md) |
| **Undiscovered** | `Medium` | `1.5 hrs` | Linux CTF | [Undiscovered.md](./Undiscovered.md) |
| **Uranium CTF** | `Medium` | `1.5 hrs` | Linux CTF | [Uranium CTF.md](./Uranium%20CTF.md) |
| **Velociraptor** | `Medium` | `1.5 hrs` | Endpoint Forensics | [Velociraptor.md](./Velociraptor.md) |
| **VulnNet Internal** | `Medium` | `2 - 3 hrs` | Internal Network Pentest | [VulnNet Internal.md](./VulnNet%20Internal.md) |
| **VulnNet Node** | `Medium` | `1.5 hrs` | Node.js Deserialization | [VulnNet Node.md](./VulnNet%20Node.md) |
| **VulnNet Roasted** | `Medium` | `2 hrs` | Active Directory Roast | [VulnNet Roasted.md](./VulnNet%20Roasted.md) |
| **Wekor** | `Medium` | `2 hrs` | SQLi / WordPress / CyberChef | [Wekor.md](./Wekor.md) |
| **Windows Event Logs** | `Medium` | `2 hrs` | Windows DFIR | [Windows Event Logs.md](./Windows%20Event%20Logs.md) |
| **Windows Forensics 1** | `Medium` | `1.5 hrs` | Windows Forensics | [Windows Forensics 1.md](./Windows%20Forensics%201.md) |
| **Windows Forensics 2** | `Medium` | `1.5 hrs` | Windows Forensics | [Windows Forensics 2.md](./Windows%20Forensics%202.md) |
| **Windows Internals** | `Medium` | `1.5 hrs` | Operating System Internals | [Windows Internals.md](./Windows%20Internals.md) |
| **Wireshark Traffic Analysis** | `Medium` | `1.5 hrs` | Packet Analysis | [Wireshark Traffic Analysis.md](./Wireshark%20Traffic%20Analysis.md) |
| **Zeno** | `Medium` | `1.5 hrs` | Linux CTF / Restaurant CMS | [Zeno.md](./Zeno.md) |
| **b3dr0ck** | `Medium` | `1.5 hrs` | Linux / TLS Socket CTF | [b3dr0ck.md](./b3dr0ck.md) |
| **biteme** | `Medium` | `1.5 hrs` | Linux / PHP CTF | [biteme.md](./biteme.md) |
| **hackerNote** | `Medium` | `1.5 hrs` | Web / SSTI / Linux | [hackerNote.md](./hackerNote.md) |
| **pyLon** | `Medium` | `1.5 hrs` | Python / Linux CTF | [pyLon.md](./pyLon.md) |
| **toc2** | `Medium` | `1.5 hrs` | Race Condition (TOCTOU) | [toc2.md](./toc2.md) |
| **Active Directory Basics** | `Easy` | `45 - 60 mins` | Walkthrough / AD | [Active Directory Basics.md](./Active%20Directory%20Basics.md) |
| **Active Directory Basics(1)** | `Easy` | `45 - 60 mins` | Walkthrough / AD | [Active Directory Basics(1).md](./Active%20Directory%20Basics%281%29.md) |
| **Agent T** | `Easy` | `20 - 30 mins` | Web / CTF | [Agent T.md](./Agent%20T.md) |
| **Authentication Bypass** | `Easy` | `45 mins` | Web Fundamentals | [Authentication Bypass.md](./Authentication%20Bypass.md) |
| **Autopsy** | `Easy` | `1 - 1.5 hrs` | DFIR | [Autopsy.md](./Autopsy.md) |
| **BlockChain** | `Easy` | `45 mins` | Walkthrough | [BlockChain.md](./BlockChain.md) |
| **Brim** | `Easy` | `1 hr` | DFIR / Network | [Brim.md](./Brim.md) |
| **Burp Suite Extender** | `Easy` | `30 - 45 mins` | Web Tools | [Burp Suite Extender.md](./Burp%20Suite%20Extender.md) |
| **Burp Suite Intruder** | `Easy` | `45 mins` | Web Tools | [Burp Suite Intruder.md](./Burp%20Suite%20Intruder.md) |
| **Burp Suite Other Modules** | `Easy` | `45 mins` | Web Tools | [Burp Suite Other Modules.md](./Burp%20Suite%20Other%20Modules.md) |
| **CVE-2021-41773** | `Easy` | `30 - 45 mins` | Apache Path Traversal | [CVE-2021-41773.md](./CVE-2021-41773.md) |
| **Capture!** | `Easy` | `45 mins` | Web / Captcha Bypass | [Capture!.md](./Capture%21.md) |
| **Command Injection** | `Easy` | `45 mins` | Web Pentest | [Command Injection.md](./Command%20Injection.md) |
| **Core Windows Processes** | `Easy` | `1 hr` | Windows Forensics | [Core Windows Processes.md](./Core%20Windows%20Processes.md) |
| **Couch** | `Easy` | `30 mins` | CouchDB Misconfig | [Couch.md](./Couch.md) |
| **Cross-site Scripting-1** | `Easy` | `1 hr` | Web Fundamentals | [Cross-site Scripting-1.md](./Cross-site%20Scripting-1.md) |
| **Cyber Scotland 2021** | `Easy` | `1.5 hrs` | Event CTF | [Cyber Scotland 2021.md](./Cyber%20Scotland%202021.md) |
| **En-pass** | `Easy` | `1 hr` | Linux CTF | [En-pass.md](./En-pass.md) |
| **Exploit Vulnerabilities** | `Easy` | `45 mins` | Pentesting Basics | [Exploit Vulnerabilities.md](./Exploit%20Vulnerabilities.md) |
| **File Inclusion** | `Easy` | `1 hr` | LFI / RFI Fundamentals | [File Inclusion.md](./File%20Inclusion.md) |
| **Firewalls** | `Easy` | `1 hr` | Network Security | [Firewalls.md](./Firewalls.md) |
| **Gallery** | `Easy` | `1 hr` | Linux / Web CMS | [Gallery.md](./Gallery.md) |
| **IDE** | `Easy` | `45 mins` | Web / Linux PrivEsc | [IDE.md](./IDE.md) |
| **IDOR** | `Easy` | `30 mins` | Web Security | [IDOR.md](./IDOR.md) |
| **Intro to Docker** | `Easy` | `1 hr` | Containers / Docker | [Intro to Docker.md](./Intro%20to%20Docker.md) |
| **Introduction To Honeypots** | `Easy` | `1 hr` | Blue Team Defense | [Introduction To Honeypots.md](./Introduction%20To%20Honeypots.md) |
| **Introduction to Flask** | `Easy` | `1 hr` | Web Development | [Introduction to Flask.md](./Introduction%20to%20Flask.md) |
| **Investigating with ELK 101** | `Easy` | `1 hr` | ELK Stack / DFIR | [Investigating with ELK 101.md](./Investigating%20with%20ELK%20101.md) |
| **JPGChat** | `Easy` | `30 mins` | Linux / Python Injection | [JPGChat.md](./JPGChat.md) |
| **Jason** | `Easy` | `45 mins` | Node.js Deserialization | [Jason.md](./Jason.md) |
| **MAL Strings** | `Easy` | `30 mins` | Static Analysis | [MAL Strings.md](./MAL%20Strings.md) |
| **Magician** | `Easy` | `1 hr` | ImageMagick / Linux CTF | [Magician.md](./Magician.md) |
| **Mustacchio** | `Easy` | `45 mins` | Linux / Web CTF | [Mustacchio.md](./Mustacchio.md) |
| **NetworkMiner** | `Easy` | `45 mins` | PCAP Forensics | [NetworkMiner.md](./NetworkMiner.md) |
| **Nmap Basic Port Scans** | `Easy` | `45 mins` | Recon / Nmap | [Nmap Basic Port Scans.md](./Nmap%20Basic%20Port%20Scans.md) |
| **OWASP Top 10 - 2021** | `Easy` | `2 hrs` | Web Security | [OWASP Top 10 - 2021.md](./OWASP%20Top%2010%20-%202021.md) |
| **Osquery** | `Easy` | `1 hr` | Endpoint Visibility | [Osquery.md](./Osquery.md) |
| **Osquery The Basics** | `Easy` | `1 hr` | Endpoint Visibility | [Osquery The Basics.md](./Osquery%20The%20Basics.md) |
| **OverlayFS** | `Easy` | `30 mins` | CVE-2021-3493 Exploit | [OverlayFS.md](./OverlayFS.md) |
| **Phishing1** | `Easy` | `30 mins` | Email Analysis Basics | [Phishing1.md](./Phishing1.md) |
| **Polkit_CVE** | `Easy` | `30 mins` | CVE-2021-3560 / CVE-2021-4034 | [Polkit_CVE.md](./Polkit_CVE.md) |
| **Putting it all together** | `Easy` | `30 mins` | Network Summary | [Putting it all together.md](./Putting%20it%20all%20together.md) |
| **Python for Pentesters** | `Easy` | `1 hr` | Python Scripting | [Python for Pentesters.md](./Python%20for%20Pentesters.md) |
| **REmux The Tmux** | `Easy` | `30 mins` | Terminal Multiplexer | [REmux The Tmux.md](./REmux%20The%20Tmux.md) |
| **Splunk 101** | `Easy` | `1.5 hrs` | SIEM Fundamentals | [Splunk 101.md](./Splunk%20101.md) |
| **Splunk Basics** | `Easy` | `45 mins` | SIEM Intro | [Splunk Basics.md](./Splunk%20Basics.md) |
| **Subdomain Enumeration** | `Easy` | `45 mins` | Reconnaissance | [Subdomain Enumeration.md](./Subdomain%20Enumeration.md) |
| **Sysinternals** | `Easy` | `1 hr` | Windows Tools | [Sysinternals.md](./Sysinternals.md) |
| **Tech_Supp0rt 1** | `Easy` | `45 mins` | Linux / Subversion CTF | [Tech_Supp0rt 1.md](./Tech_Supp0rt%201.md) |
| **Templates** | `Easy` | `45 mins` | SSTI Fundamentals | [Templates.md](./Templates.md) |
| **TheHive Project** | `Easy` | `1 hr` | Incident Response SOAR | [TheHive Project.md](./TheHive%20Project.md) |
| **Vulnerability Capstone** | `Easy` | `45 mins` | Capstone Lab | [Vulnerability Capstone.md](./Vulnerability%20Capstone.md) |
| **Web Enumeration** | `Easy` | `1 hr` | Web Reconnaissance | [Web Enumeration.md](./Web%20Enumeration.md) |
| **Wireshark Packet Operations** | `Easy` | `1 hr` | Packet Analysis | [Wireshark Packet Operations.md](./Wireshark%20Packet%20Operations.md) |
| **WordPress-Cve2021** | `Easy` | `45 mins` | WordPress CVE Lab | [WordPress-Cve2021.md](./WordPress-Cve2021.md) |
| **Careers in Cyber** | `Info` | `20 mins` | General Walkthrough | [Careers in Cyber.md](./Careers%20in%20Cyber.md) |
| **Cyber Kill Chain** | `Info` | `30 mins` | Defensive Concepts | [Cyber Kill Chain.md](./Cyber%20Kill%20Chain.md) |
| **DFIR An Introduction** | `Info` | `30 mins` | DFIR Basics | [DFIR An Introduction.md](./DFIR%20An%20Introduction.md) |
| **Diamond Model** | `Info` | `30 mins` | Threat Intel | [Diamond Model.md](./Diamond%20Model.md) |
| **Extending Your Network** | `Info` | `30 mins` | Networking Basics | [Extending Your Network.md](./Extending%20Your%20Network.md) |
| **Intro to Defensive Security** | `Info` | `30 mins` | Blue Team Basics | [Intro to Defensive Security.md](./Intro%20to%20Defensive%20Security.md) |
| **Intro to Offensive Security** | `Info` | `20 mins` | Red Team Basics | [Intro to Offensive Security.md](./Intro%20to%20Offensive%20Security.md) |
| **Introduction to SIEM** | `Info` | `30 mins` | SOC Monitoring | [Introduction to SIEM.md](./Introduction%20to%20SIEM.md) |
| **Operating System Security** | `Info` | `30 mins` | Security Basics | [Operating System Security.md](./Operating%20System%20Security.md) |
| **Packets & Frames** | `Info` | `30 mins` | Networking Basics | [Packets & Frames.md](./Packets%20%26%20Frames.md) |
| **Phishing** | `Info` | `30 mins` | Social Engineering | [Phishing.md](./Phishing.md) |
| **Protocols and Servers** | `Info` | `30 mins` | Networking Basics | [Protocols and Servers.md](./Protocols%20and%20Servers.md) |
| **Protocols and Servers 2** | `Info` | `30 mins` | Networking Basics | [Protocols and Servers 2.md](./Protocols%20and%20Servers%202.md) |
| **Pyramid Of Pain** | `Info` | `30 mins` | Threat Intel Concept | [Pyramid Of Pain.md](./Pyramid%20Of%20Pain.md) |
| **Security Operations** | `Info` | `30 mins` | SOC Overview | [Security Operations.md](./Security%20Operations.md) |
| **Security Principles** | `Info` | `30 mins` | Security Basics | [Security Principles.md](./Security%20Principles.md) |
| **Unified Kill Chain** | `Info` | `30 mins` | Threat Modeling | [Unified Kill Chain.md](./Unified%20Kill%20Chain.md) |
| **x86 Architecture Overview** | `Info` | `45 mins` | Reverse Engineering | [x86 Architecture Overview.md](./x86%20Architecture%20Overview.md) |


### 2022 Releases (110 Rooms)
| Room Name | Difficulty | Est. Time | Focus Area | Writeup Link |
| :--- | :---: | :---: | :--- | :--- |
| **AV Evasion Shellcode** | `Hard` | `2 - 3 hrs` | Red Teaming / Malware | [AV Evasion Shellcode.md](./AV%20Evasion%20Shellcode.md) |
| **Abusing Windows Internals** | `Hard` | `2.5 - 3.5 hrs` | Windows Internals | [Abusing Windows Internals.md](./Abusing%20Windows%20Internals.md) |
| **Evading Logging and Monitoring** | `Hard` | `2.5 - 3.5 hrs` | Evasion / Defense | [Evading Logging and Monitoring.md](./Evading%20Logging%20and%20Monitoring.md) |
| **LinuxFunctionHooking** | `Hard` | `2.5 hrs` | Linux Internals / Hooking | [LinuxFunctionHooking.md](./LinuxFunctionHooking.md) |
| **Lookback** | `Hard` | `3 - 4 hrs` | Active Directory / Exchange | [Lookback.md](./Lookback.md) |
| **Obfuscation Principles** | `Hard` | `2 hrs` | Malware / Evasion | [Obfuscation Principles.md](./Obfuscation%20Principles.md) |
| **Ra 2** | `Hard` | `3 - 4 hrs` | Active Directory / PKI | [Ra 2.md](./Ra%202.md) |
| **Runtime Detection Evasion** | `Hard` | `2 - 3 hrs` | AMSI / ETW Evasion | [Runtime Detection Evasion.md](./Runtime%20Detection%20Evasion.md) |
| **Sandbox Evasion** | `Hard` | `2 hrs` | Malware Evasion | [Sandbox Evasion.md](./Sandbox%20Evasion.md) |
| **Signature Evasion** | `Hard` | `2.5 hrs` | Defender Evasion | [Signature Evasion.md](./Signature%20Evasion.md) |
| **Snort Challenge - Live Attacks** | `Hard` | `2.5 - 3.5 hrs` | IDS / Snort Live | [Snort Challenge - Live Attacks.md](./Snort%20Challenge%20-%20Live%20Attacks.md) |
| **Tempest** | `Hard` | `3 hrs` | Active Directory / CTF | [Tempest.md](./Tempest.md) |
| **AD Certificate Templates** | `Medium` | `1.5 - 2 hrs` | Active Directory | [AD Certificate Templates.md](./AD%20Certificate%20Templates.md) |
| **AllSignsPoint2Pwnage** | `Medium` | `1.5 - 2.5 hrs` | Active Directory | [AllSignsPoint2Pwnage.md](./AllSignsPoint2Pwnage.md) |
| **Android Malware Analysis** | `Medium` | `1.5 - 2 hrs` | Mobile DFIR | [Android Malware Analysis.md](./Android%20Malware%20Analysis.md) |
| **Aratus** | `Medium` | `1.5 - 2 hrs` | Linux CTF | [Aratus.md](./Aratus.md) |
| **Atlas** | `Medium` | `1.5 - 2 hrs` | Network Pentest | [Atlas.md](./Atlas.md) |
| **Basic Static Analysis** | `Medium` | `1.5 - 2 hrs` | Malware Analysis | [Basic Static Analysis.md](./Basic%20Static%20Analysis.md) |
| **Biblioteca** | `Medium` | `1.5 - 2 hrs` | Linux / SQLi | [Biblioteca.md](./Biblioteca.md) |
| **CVE-2022-26923** | `Medium` | `1.5 - 2 hrs` | Active Directory Certifried | [CVE-2022-26923.md](./CVE-2022-26923.md) |
| **Content Security Policy** | `Medium` | `1 hr` | Web Security | [Content Security Policy.md](./Content%20Security%20Policy.md) |
| **Conti** | `Medium` | `1 - 1.5 hrs` | Ransomware Analysis | [Conti.md](./Conti.md) |
| **Credentials Harvesting** | `Medium` | `1.5 - 2 hrs` | Credential Dumping | [Credentials Harvesting.md](./Credentials%20Harvesting.md) |
| **DX1 Liberty Island** | `Medium` | `1.5 - 2 hrs` | Linux CTF | [DX1 Liberty Island.md](./DX1%20Liberty%20Island.md) |
| **Data Exfiltration** | `Medium` | `2 hrs` | Network / Red Team | [Data Exfiltration.md](./Data%20Exfiltration.md) |
| **Dependency Management** | `Medium` | `1.5 hrs` | DevSecOps | [Dependency Management.md](./Dependency%20Management.md) |
| **Dissecting PE Headers** | `Medium` | `1.5 hrs` | Reverse Engineering | [Dissecting PE Headers.md](./Dissecting%20PE%20Headers.md) |
| **Eavesdropper** | `Medium` | `1.5 hrs` | Linux Network Sniffing | [Eavesdropper.md](./Eavesdropper.md) |
| **Forgotten Implant** | `Medium` | `1.5 - 2 hrs` | C2 / Incident Response | [Forgotten Implant.md](./Forgotten%20Implant.md) |
| **Intro to Detection Engineering** | `Medium` | `1.5 hrs` | Detection / Blue Team | [Intro to Detection Engineering.md](./Intro%20to%20Detection%20Engineering.md) |
| **Intro to Threat Emulation** | `Medium` | `1.5 hrs` | Adversary Emulation | [Intro to Threat Emulation.md](./Intro%20to%20Threat%20Emulation.md) |
| **KAPE** | `Medium` | `2 hrs` | Triage Forensics | [KAPE.md](./KAPE.md) |
| **L2 MAC Flooding & ARP Spoofing** | `Medium` | `1.5 hrs` | Network Attacks | [L2 MAC Flooding & ARP Spoofing.md](./L2%20MAC%20Flooding%20%26%20ARP%20Spoofing.md) |
| **Linux Forensics** | `Medium` | `1.5 - 2 hrs` | DFIR / Linux | [Linux Forensics.md](./Linux%20Forensics.md) |
| **Living Off the Land** | `Medium` | `1.5 hrs` | LOLBAS / LOLBins | [Living Off the Land.md](./Living%20Off%20the%20Land.md) |
| **MISP** | `Medium` | `1.5 hrs` | Threat Sharing | [MISP.md](./MISP.md) |
| **Metamorphosis** | `Medium` | `2 hrs` | Active Directory | [Metamorphosis.md](./Metamorphosis.md) |
| **Microsoft Windows Hardening** | `Medium` | `1.5 hrs` | Defensive Hardening | [Microsoft Windows Hardening.md](./Microsoft%20Windows%20Hardening.md) |
| **Mnemonic** | `Medium` | `2 hrs` | Active Directory / Forensics | [Mnemonic.md](./Mnemonic.md) |
| **NahamStore** | `Medium` | `2.5 - 3.5 hrs` | Web Pentesting Lab | [NahamStore.md](./NahamStore.md) |
| **Napping** | `Medium` | `1 hr` | Web Tabnabbing | [Napping.md](./Napping.md) |
| **Network Security Solutions** | `Medium` | `1.5 hrs` | IDS / IPS / Firewalls | [Network Security Solutions.md](./Network%20Security%20Solutions.md) |
| **OWASP API Security Top 10 - 1** | `Medium` | `1.5 hrs` | API Security | [OWASP API Security Top 10 - 1.md](./OWASP%20API%20Security%20Top%2010%20-%201.md) |
| **OWASP API Security Top 10 - 2** | `Medium` | `1.5 hrs` | API Security | [OWASP API Security Top 10 - 2.md](./OWASP%20API%20Security%20Top%2010%20-%202.md) |
| **OWASP Broken Access Control** | `Medium` | `1 hr` | Web Security | [OWASP Broken Access Control.md](./OWASP%20Broken%20Access%20Control.md) |
| **Ollie** | `Medium` | `1.5 hrs` | Linux CTF / phpIPAM | [Ollie.md](./Ollie.md) |
| **OpenCTI** | `Medium` | `1.5 hrs` | Threat Intelligence | [OpenCTI.md](./OpenCTI.md) |
| **PS Eclipse** | `Medium` | `1 hr` | PowerShell Script Analysis | [PS Eclipse.md](./PS%20Eclipse.md) |
| **ParrotPost Phishing Analysis** | `Medium` | `1.5 hrs` | Phishing Analysis | [ParrotPost Phishing Analysis.md](./ParrotPost%20Phishing%20Analysis.md) |
| **Password Attacks** | `Medium` | `2 hrs` | Cracking / Hydra / Hashcat | [Password Attacks.md](./Password%20Attacks.md) |
| **Phishing Emails 3** | `Medium` | `1 hr` | Email Header Analysis | [Phishing Emails 3.md](./Phishing%20Emails%203.md) |
| **Phishing Emails 4** | `Medium` | `1 hr` | Email Header Analysis | [Phishing Emails 4.md](./Phishing%20Emails%204.md) |
| **Phishing Emails 5** | `Medium` | `1 hr` | Email Header Analysis | [Phishing Emails 5.md](./Phishing%20Emails%205.md) |
| **Racetrack Bank** | `Medium` | `1 hr` | Race Conditions / Web | [Racetrack Bank.md](./Racetrack%20Bank.md) |
| **Red Team OPSEC** | `Medium` | `1.5 hrs` | Red Team Operations | [Red Team OPSEC.md](./Red%20Team%20OPSEC.md) |
| **Red Team Threat Intel** | `Medium` | `1.5 hrs` | Red Team Intelligence | [Red Team Threat Intel.md](./Red%20Team%20Threat%20Intel.md) |
| **Sigma** | `Medium` | `1.5 hrs` | Detection Engineering | [Sigma.md](./Sigma.md) |
| **Snapped Phishing Line** | `Medium` | `1.5 hrs` | Phishing DFIR | [Snapped Phishing Line.md](./Snapped%20Phishing%20Line.md) |
| **Snort Challenge - The Basics** | `Medium` | `2 hrs` | IDS / Snort Rules | [Snort Challenge - The Basics.md](./Snort%20Challenge%20-%20The%20Basics.md) |
| **Tactical Detection** | `Medium` | `1.5 hrs` | Blue Team Detection | [Tactical Detection.md](./Tactical%20Detection.md) |
| **Threat Intel & Containment** | `Medium` | `1.5 hrs` | Threat Intelligence | [Threat Intel & Containment.md](./Threat%20Intel%20%26%20Containment.md) |
| **Warzone 2** | `Medium` | `1 hr` | Network PCAP Analysis | [Warzone 2.md](./Warzone%202.md) |
| **Wazuh** | `Medium` | `2 hrs` | SIEM & XDR | [Wazuh.md](./Wazuh.md) |
| **Weaponization** | `Medium` | `1.5 hrs` | Red Team Weaponization | [Weaponization.md](./Weaponization.md) |
| **Weasel** | `Medium` | `1.5 hrs` | WSL / Windows CTF | [Weasel.md](./Weasel.md) |
| **Windows Local Persistence** | `Medium` | `2 hrs` | Red Team Persistence | [Windows Local Persistence.md](./Windows%20Local%20Persistence.md) |
| **Windows Reversing Intro** | `Medium` | `1.5 hrs` | Reverse Engineering | [Windows Reversing Intro.md](./Windows%20Reversing%20Intro.md) |
| **Zeek Exercises** | `Medium` | `1.5 hrs` | Zeek / Network DFIR | [Zeek Exercises.md](./Zeek%20Exercises.md) |
| **iOS Forensics** | `Medium` | `1.5 hrs` | Mobile DFIR | [iOS Forensics.md](./iOS%20Forensics.md) |
| **Atlassian, CVE-2022-26134** | `Easy` | `30 - 45 mins` | CVE / Web | [Atlassian, CVE-2022-26134.md](./Atlassian%2C%20CVE-2022-26134.md) |
| **Benign** | `Easy` | `45 mins` | DFIR / Splunk | [Benign.md](./Benign.md) |
| **Brute Force Heroes** | `Easy` | `45 mins` | Authentication | [Brute Force Heroes.md](./Brute%20Force%20Heroes.md) |
| **Bugged** | `Easy` | `45 mins` | IoT / MQTT | [Bugged.md](./Bugged.md) |
| **Committed** | `Easy` | `20 - 30 mins` | Git Forensics | [Committed.md](./Committed.md) |
| **Confidential** | `Easy` | `30 mins` | DFIR / PDF Forensics | [Confidential.md](./Confidential.md) |
| **Corridor** | `Easy` | `20 - 30 mins` | Web / IDOR | [Corridor.md](./Corridor.md) |
| **CyberHeroes** | `Easy` | `20 mins` | Web Authentication | [CyberHeroes.md](./CyberHeroes.md) |
| **Dig Dug** | `Easy` | `20 mins` | DNS Recon | [Dig Dug.md](./Dig%20Dug.md) |
| **Dirty Pipe** | `Easy` | `30 - 45 mins` | CVE-2022-0847 Exploit | [Dirty Pipe.md](./Dirty%20Pipe.md) |
| **Epoch** | `Easy` | `20 - 30 mins` | Command Injection | [Epoch.md](./Epoch.md) |
| **Follina MSDT** | `Easy` | `30 - 45 mins` | CVE-2022-30190 | [Follina MSDT.md](./Follina%20MSDT.md) |
| **Hacker vs. Hacker** | `Easy` | `45 mins` | Web Shell Hunting | [Hacker vs. Hacker.md](./Hacker%20vs.%20Hacker.md) |
| **Hardening Basics Part 1** | `Easy` | `1.5 hrs` | Defensive Hardening | [Hardening Basics Part 1.md](./Hardening%20Basics%20Part%201.md) |
| **Hardening Basics Part 2** | `Easy` | `1.5 hrs` | Defensive Hardening | [Hardening Basics Part 2.md](./Hardening%20Basics%20Part%202.md) |
| **Intro to C2** | `Easy` | `1 hr` | C2 Frameworks | [Intro to C2.md](./Intro%20to%20C2.md) |
| **Intro to Pipeline Automation** | `Easy` | `1 hr` | CI/CD Security | [Intro to Pipeline Automation.md](./Intro%20to%20Pipeline%20Automation.md) |
| **ItsyBitsy** | `Easy` | `30 mins` | Log Analysis | [ItsyBitsy.md](./ItsyBitsy.md) |
| **Lesson Learned** | `Easy` | `30 mins` | Incident Response | [Lesson Learned.md](./Lesson%20Learned.md) |
| **MD2PDF** | `Easy` | `30 mins` | SSRF / XSS | [MD2PDF.md](./MD2PDF.md) |
| **Masterminds** | `Easy` | `1 hr` | Zeek / Network Traffic | [Masterminds.md](./Masterminds.md) |
| **Mr. Phisher** | `Easy` | `30 mins` | Phishing Analysis | [Mr. Phisher.md](./Mr.%20Phisher.md) |
| **Neighbour** | `Easy` | `20 mins` | IDOR Vulnerability | [Neighbour.md](./Neighbour.md) |
| **New Hire Old Artifacts** | `Easy` | `45 mins` | DFIR / Splunk | [New Hire Old Artifacts.md](./New%20Hire%20Old%20Artifacts.md) |
| **Opacity** | `Easy` | `1 hr` | PHP Upload / KeePass | [Opacity.md](./Opacity.md) |
| **Pwnkit** | `Easy` | `20 mins` | CVE-2021-4034 Exploit | [Pwnkit.md](./Pwnkit.md) |
| **Snort** | `Easy` | `1.5 hrs` | IDS Fundamentals | [Snort.md](./Snort.md) |
| **Surfer** | `Easy` | `30 mins` | SSRF Challenge | [Surfer.md](./Surfer.md) |
| **TakeOver** | `Easy` | `30 mins` | Subdomain Takeover | [TakeOver.md](./TakeOver.md) |
| **Traffic Analysis Essentials** | `Easy` | `1 hr` | Network Traffic Analysis | [Traffic Analysis Essentials.md](./Traffic%20Analysis%20Essentials.md) |
| **Training for New Analyst** | `Easy` | `1 hr` | SOC Training | [Training for New Analyst.md](./Training%20for%20New%20Analyst.md) |
| **Warzone 1** | `Easy` | `45 mins` | Network PCAP Analysis | [Warzone 1.md](./Warzone%201.md) |
| **Zeek** | `Easy` | `1.5 hrs` | Network Monitoring | [Zeek.md](./Zeek.md) |
| **Intro to Cloud Security** | `Info` | `45 mins` | Cloud Concepts | [Intro to Cloud Security.md](./Intro%20to%20Cloud%20Security.md) |
| **Intro to Containerisation** | `Info` | `30 mins` | DevOps Security | [Intro to Containerisation.md](./Intro%20to%20Containerisation.md) |
| **Intro to Cyber Threat Intel** | `Info` | `30 mins` | Threat Intelligence | [Intro to Cyber Threat Intel.md](./Intro%20to%20Cyber%20Threat%20Intel.md) |
| **Intro to Endpoint Security** | `Info` | `30 mins` | Endpoint Defense | [Intro to Endpoint Security.md](./Intro%20to%20Endpoint%20Security.md) |
| **Intro to ISAC** | `Info` | `30 mins` | Information Sharing | [Intro to ISAC.md](./Intro%20to%20ISAC.md) |
| **Junior Security Analyst Intro** | `Info` | `30 mins` | SOC Analyst Path | [Junior Security Analyst Intro.md](./Junior%20Security%20Analyst%20Intro.md) |
| **Security Engineer Intro** | `Info` | `30 mins` | Engineering Career | [Security Engineer Intro.md](./Security%20Engineer%20Intro.md) |
| **Advent of Cyber 2022** | `Easy - Medium` | `10+ hrs (24 Days)` | Event / Multi-topic | [Advent of Cyber 2022.md](./Advent%20of%20Cyber%202022.md) |


### 2023 Releases (6 Rooms)
| Room Name | Difficulty | Est. Time | Focus Area | Writeup Link |
| :--- | :---: | :---: | :--- | :--- |
| **Boogeyman 1** | `Medium` | `2 - 3 hrs` | DFIR / Threat Hunting | [Boogeyman 1.md](./Boogeyman%201.md) |
| **CVE-2023-38408** | `Medium` | `1 hr` | OpenSSH PKCS#11 | [CVE-2023-38408.md](./CVE-2023-38408.md) |
| **LocalPotato** | `Medium` | `1 hr` | Windows PrivEsc / CVE-2023-21746 | [LocalPotato.md](./LocalPotato.md) |
| **Outlook NTLM Leak** | `Medium` | `1 hr` | CVE-2023-23397 | [Outlook NTLM Leak.md](./Outlook%20NTLM%20Leak.md) |
| **Tardigrade** | `Medium` | `1.5 hrs` | Linux Persistence DFIR | [Tardigrade.md](./Tardigrade.md) |
| **Valley** | `Medium` | `1.5 hrs` | Linux CTF | [Valley.md](./Valley.md) |


---

## 7. Complete Master Index (All 427 Rooms Ranked & Filterable)

Alphabetical master directory of every room writeup in the repository.

| # | Room Name | Difficulty | Length / Est. Time | Release Year | Category / Focus | File Size | Link |
| :---: | :--- | :---: | :---: | :---: | :--- | :---: | :--- |
| 1 | **0day** | `Medium` | `1 - 2 hrs` | 2020 | Linux CTF | 113.4 KB | [0day.md](./0day.md) |
| 2 | **AD Certificate Templates** | `Medium` | `1.5 - 2 hrs` | 2022 | Active Directory | 67.9 KB | [AD Certificate Templates.md](./AD%20Certificate%20Templates.md) |
| 3 | **AV Evasion Shellcode** | `Hard` | `2 - 3 hrs` | 2022 | Red Teaming / Malware | 84.7 KB | [AV Evasion Shellcode.md](./AV%20Evasion%20Shellcode.md) |
| 4 | **Abusing Windows Internals** | `Hard` | `2.5 - 3.5 hrs` | 2022 | Windows Internals | 36.5 KB | [Abusing Windows Internals.md](./Abusing%20Windows%20Internals.md) |
| 5 | **Active Directory Basics(1)** | `Easy` | `45 - 60 mins` | 2021 | Walkthrough / AD | 44.0 KB | [Active Directory Basics(1).md](./Active%20Directory%20Basics%281%29.md) |
| 6 | **Active Directory Basics** | `Easy` | `45 - 60 mins` | 2021 | Walkthrough / AD | 29.2 KB | [Active Directory Basics.md](./Active%20Directory%20Basics.md) |
| 7 | **Advent of Cyber 2022** | `Easy - Medium` | `10+ hrs (24 Days)` | 2022 | Event / Multi-topic | 540.1 KB | [Advent of Cyber 2022.md](./Advent%20of%20Cyber%202022.md) |
| 8 | **Agent T** | `Easy` | `20 - 30 mins` | 2021 | Web / CTF | 11.0 KB | [Agent T.md](./Agent%20T.md) |
| 9 | **Alfred** | `Easy` | `1 - 1.5 hrs` | 2019 | Windows CTF | 31.2 KB | [Alfred.md](./Alfred.md) |
| 10 | **All in One** | `Easy` | `1 - 1.5 hrs` | 2020 | Linux CTF | 49.7 KB | [All in One.md](./All%20in%20One.md) |
| 11 | **AllSignsPoint2Pwnage** | `Medium` | `1.5 - 2.5 hrs` | 2022 | Active Directory | 36.3 KB | [AllSignsPoint2Pwnage.md](./AllSignsPoint2Pwnage.md) |
| 12 | **Android Malware Analysis** | `Medium` | `1.5 - 2 hrs` | 2022 | Mobile DFIR | 16.9 KB | [Android Malware Analysis.md](./Android%20Malware%20Analysis.md) |
| 13 | **Annie** | `Medium` | `1 - 2 hrs` | 2021 | Linux CTF | 16.2 KB | [Annie.md](./Annie.md) |
| 14 | **Anonforce** | `Easy` | `30 - 45 mins` | 2020 | Linux CTF | 17.8 KB | [Anonforce.md](./Anonforce.md) |
| 15 | **Anonymous Playground** | `Hard` | `2 - 3 hrs` | 2020 | Reverse Engineering / CTF | 32.1 KB | [Anonymous Playground.md](./Anonymous%20Playground.md) |
| 16 | **Anonymous** | `Medium` | `1 - 1.5 hrs` | 2020 | Linux CTF | 24.6 KB | [Anonymous.md](./Anonymous.md) |
| 17 | **Aratus** | `Medium` | `1.5 - 2 hrs` | 2022 | Linux CTF | 37.2 KB | [Aratus.md](./Aratus.md) |
| 18 | **Archangel** | `Easy` | `1 - 1.5 hrs` | 2020 | Linux CTF | 29.7 KB | [Archangel.md](./Archangel.md) |
| 19 | **Atlas** | `Medium` | `1.5 - 2 hrs` | 2022 | Network Pentest | 48.0 KB | [Atlas.md](./Atlas.md) |
| 20 | **Atlassian, CVE-2022-26134** | `Easy` | `30 - 45 mins` | 2022 | CVE / Web | 30.6 KB | [Atlassian, CVE-2022-26134.md](./Atlassian%2C%20CVE-2022-26134.md) |
| 21 | **AttackerKB** | `Easy` | `30 mins` | 2020 | Walkthrough | 4.1 KB | [AttackerKB.md](./AttackerKB.md) |
| 22 | **Attacking Kerberos** | `Medium` | `2 - 3 hrs` | 2021 | Active Directory | 71.9 KB | [Attacking Kerberos.md](./Attacking%20Kerberos.md) |
| 23 | **Authentication Bypass** | `Easy` | `45 mins` | 2021 | Web Fundamentals | 59.4 KB | [Authentication Bypass.md](./Authentication%20Bypass.md) |
| 24 | **Autopsy** | `Easy` | `1 - 1.5 hrs` | 2021 | DFIR | 22.5 KB | [Autopsy.md](./Autopsy.md) |
| 25 | **Avengers Blog** | `Easy` | `30 - 45 mins` | 2019 | Web CTF | 16.9 KB | [Avengers Blog.md](./Avengers%20Blog.md) |
| 26 | **Badbyte** | `Easy` | `1 - 1.5 hrs` | 2020 | Linux CTF | 195.0 KB | [Badbyte.md](./Badbyte.md) |
| 27 | **Basic Static Analysis** | `Medium` | `1.5 - 2 hrs` | 2022 | Malware Analysis | 61.9 KB | [Basic Static Analysis.md](./Basic%20Static%20Analysis.md) |
| 28 | **Bebop** | `Medium` | `1 - 1.5 hrs` | 2021 | Linux CTF | 5.3 KB | [Bebop.md](./Bebop.md) |
| 29 | **Benign** | `Easy` | `45 mins` | 2022 | DFIR / Splunk | 2.8 KB | [Benign.md](./Benign.md) |
| 30 | **Biblioteca** | `Medium` | `1.5 - 2 hrs` | 2022 | Linux / SQLi | 31.7 KB | [Biblioteca.md](./Biblioteca.md) |
| 31 | **BinaryHeaven** | `Medium` | `2 - 3 hrs` | 2020 | Binary Exploitation | 52.6 KB | [BinaryHeaven.md](./BinaryHeaven.md) |
| 32 | **Binex** | `Medium` | `2 - 3 hrs` | 2020 | Binary Exploitation | 75.2 KB | [Binex.md](./Binex.md) |
| 33 | **BioHazard** | `Hard` | `3 - 4 hrs` | 2020 | Multi-stage CTF | 25.9 KB | [BioHazard.md](./BioHazard.md) |
| 34 | **Blaster** | `Easy` | `1 hr` | 2020 | Windows CTF | 6.7 KB | [Blaster.md](./Blaster.md) |
| 35 | **BlockChain** | `Easy` | `45 mins` | 2021 | Walkthrough | 7.2 KB | [BlockChain.md](./BlockChain.md) |
| 36 | **Blog** | `Medium` | `1.5 - 2 hrs` | 2020 | Linux / WordPress | 26.2 KB | [Blog.md](./Blog.md) |
| 37 | **BlueTeam** | `Easy` | `45 mins` | 2020 | Defensive | 12.2 KB | [BlueTeam.md](./BlueTeam.md) |
| 38 | **Boiler CTF** | `Medium` | `1.5 - 2 hrs` | 2019 | Linux CTF | 22.4 KB | [Boiler CTF.md](./Boiler%20CTF.md) |
| 39 | **Bolt** | `Easy` | `30 - 45 mins` | 2020 | Web / CMS | 2.3 KB | [Bolt.md](./Bolt.md) |
| 40 | **Boogeyman 1** | `Medium` | `2 - 3 hrs` | 2023 | DFIR / Threat Hunting | 112.5 KB | [Boogeyman 1.md](./Boogeyman%201.md) |
| 41 | **Bookstore** | `Easy` | `1 - 1.5 hrs` | 2020 | Linux / API CTF | 17.9 KB | [Bookstore.md](./Bookstore.md) |
| 42 | **BountyHacker** | `Easy` | `30 - 45 mins` | 2019 | Linux CTF | 7.8 KB | [BountyHacker.md](./BountyHacker.md) |
| 43 | **Brainpan 1** | `Hard` | `2.5 - 3.5 hrs` | 2020 | Buffer Overflow / CTF | 0.9 KB | [Brainpan 1.md](./Brainpan%201.md) |
| 44 | **Brainstorm** | `Medium` | `1.5 - 2.5 hrs` | 2019 | Buffer Overflow / Windows | 39.1 KB | [Brainstorm.md](./Brainstorm.md) |
| 45 | **Break Out The Cage** | `Easy` | `1 hr` | 2020 | Linux CTF | 3.0 KB | [Break Out The Cage.md](./Break%20Out%20The%20Cage.md) |
| 46 | **Brim** | `Easy` | `1 hr` | 2021 | DFIR / Network | 30.3 KB | [Brim.md](./Brim.md) |
| 47 | **Brooklyn Nine Nine** | `Easy` | `45 mins` | 2020 | Linux CTF | 29.5 KB | [Brooklyn Nine Nine.md](./Brooklyn%20Nine%20Nine.md) |
| 48 | **Brute Force Heroes** | `Easy` | `45 mins` | 2022 | Authentication | 67.1 KB | [Brute Force Heroes.md](./Brute%20Force%20Heroes.md) |
| 49 | **Brute** | `Medium` | `1 - 1.5 hrs` | 2020 | Linux / Brute | 64.9 KB | [Brute.md](./Brute.md) |
| 50 | **Buffer Overflow Prep** | `Medium` | `3 - 5 hrs` | 2020 | OSCP Prep / BoF | 42.0 KB | [Buffer Overflow Prep.md](./Buffer%20Overflow%20Prep.md) |
| 51 | **Buffer Overflows** | `Medium` | `2 - 3 hrs` | 2020 | Binary / BoF | 52.6 KB | [Buffer Overflows.md](./Buffer%20Overflows.md) |
| 52 | **Bugged** | `Easy` | `45 mins` | 2022 | IoT / MQTT | 24.8 KB | [Bugged.md](./Bugged.md) |
| 53 | **Burp Suite Extender** | `Easy` | `30 - 45 mins` | 2021 | Web Tools | 8.2 KB | [Burp Suite Extender.md](./Burp%20Suite%20Extender.md) |
| 54 | **Burp Suite Intruder** | `Easy` | `45 mins` | 2021 | Web Tools | 35.2 KB | [Burp Suite Intruder.md](./Burp%20Suite%20Intruder.md) |
| 55 | **Burp Suite Other Modules** | `Easy` | `45 mins` | 2021 | Web Tools | 23.9 KB | [Burp Suite Other Modules.md](./Burp%20Suite%20Other%20Modules.md) |
| 56 | **CCT2019** | `Medium` | `1.5 - 2 hrs` | 2019 | CTF Challenge | 100.0 KB | [CCT2019.md](./CCT2019.md) |
| 57 | **CMSpit** | `Medium` | `1 - 1.5 hrs` | 2021 | CMS Exploitation | 22.3 KB | [CMSpit.md](./CMSpit.md) |
| 58 | **CMesS** | `Medium` | `1 - 1.5 hrs` | 2020 | Linux CTF | 107.6 KB | [CMesS.md](./CMesS.md) |
| 59 | **CTF collection Vol.2** | `Easy` | `1 hr` | 2020 | Misc / Crypto CTF | 5.4 KB | [CTF collection Vol.2.md](./CTF%20collection%20Vol.2.md) |
| 60 | **CVE-2019-18634** | `Easy` | `30 mins` | 2020 | Linux PrivEsc | 9.3 KB | [CVE-2019-18634.md](./CVE-2019-18634.md) |
| 61 | **CVE-2021-41773** | `Easy` | `30 - 45 mins` | 2021 | Apache Path Traversal | 27.4 KB | [CVE-2021-41773.md](./CVE-2021-41773.md) |
| 62 | **CVE-2022-26923** | `Medium` | `1.5 - 2 hrs` | 2022 | Active Directory Certifried | 77.8 KB | [CVE-2022-26923.md](./CVE-2022-26923.md) |
| 63 | **CVE-2023-38408** | `Medium` | `1 hr` | 2023 | OpenSSH PKCS#11 | 23.4 KB | [CVE-2023-38408.md](./CVE-2023-38408.md) |
| 64 | **Capture!** | `Easy` | `45 mins` | 2021 | Web / Captcha Bypass | 3.3 KB | [Capture!.md](./Capture%21.md) |
| 65 | **Careers in Cyber** | `Info` | `20 mins` | 2021 | General Walkthrough | 10.3 KB | [Careers in Cyber.md](./Careers%20in%20Cyber.md) |
| 66 | **Carpe Diem 1** | `Hard` | `2.5 - 3.5 hrs` | 2021 | Linux / Privilege Escalation | 159.8 KB | [Carpe Diem 1.md](./Carpe%20Diem%201.md) |
| 67 | **Cat Pictures 2** | `Medium` | `1.5 - 2 hrs` | 2021 | Steganography / Linux | 17.6 KB | [Cat Pictures 2.md](./Cat%20Pictures%202.md) |
| 68 | **Cat Pictures** | `Medium` | `1.5 - 2 hrs` | 2021 | Steganography / Linux | 18.0 KB | [Cat Pictures.md](./Cat%20Pictures.md) |
| 69 | **Chill Hack** | `Easy` | `1 hr` | 2020 | Linux CTF | 22.7 KB | [Chill Hack.md](./Chill%20Hack.md) |
| 70 | **Chocolate Factory** | `Easy` | `1 hr` | 2020 | Linux CTF | 4.8 KB | [Chocolate Factory.md](./Chocolate%20Factory.md) |
| 71 | **ColddBox Easy** | `Easy` | `45 - 60 mins` | 2020 | WordPress / Linux | 30.9 KB | [ColddBox Easy.md](./ColddBox%20Easy.md) |
| 72 | **Command Injection** | `Easy` | `45 mins` | 2021 | Web Pentest | 14.7 KB | [Command Injection.md](./Command%20Injection.md) |
| 73 | **Committed** | `Easy` | `20 - 30 mins` | 2022 | Git Forensics | 6.5 KB | [Committed.md](./Committed.md) |
| 74 | **Common Linux Privesc** | `Easy` | `1.5 - 2 hrs` | 2020 | Privilege Escalation | 120.7 KB | [Common Linux Privesc.md](./Common%20Linux%20Privesc.md) |
| 75 | **Confidential** | `Easy` | `30 mins` | 2022 | DFIR / PDF Forensics | 6.0 KB | [Confidential.md](./Confidential.md) |
| 76 | **Content Security Policy** | `Medium` | `1 hr` | 2022 | Web Security | 42.7 KB | [Content Security Policy.md](./Content%20Security%20Policy.md) |
| 77 | **Conti** | `Medium` | `1 - 1.5 hrs` | 2022 | Ransomware Analysis | 9.0 KB | [Conti.md](./Conti.md) |
| 78 | **ConvertMyVideo** | `Medium` | `1 hr` | 2020 | Web / Command Injection | 11.2 KB | [ConvertMyVideo.md](./ConvertMyVideo.md) |
| 79 | **Cooctus Stories** | `Medium` | `1.5 - 2 hrs` | 2020 | Web CTF | 37.8 KB | [Cooctus Stories.md](./Cooctus%20Stories.md) |
| 80 | **Core Windows Processes** | `Easy` | `1 hr` | 2021 | Windows Forensics | 27.8 KB | [Core Windows Processes.md](./Core%20Windows%20Processes.md) |
| 81 | **Corp** | `Hard` | `3 - 4 hrs` | 2021 | Active Directory | 24.4 KB | [Corp.md](./Corp.md) |
| 82 | **Corridor** | `Easy` | `20 - 30 mins` | 2022 | Web / IDOR | 1.8 KB | [Corridor.md](./Corridor.md) |
| 83 | **Couch** | `Easy` | `30 mins` | 2021 | CouchDB Misconfig | 2.0 KB | [Couch.md](./Couch.md) |
| 84 | **Credentials Harvesting** | `Medium` | `1.5 - 2 hrs` | 2022 | Credential Dumping | 117.9 KB | [Credentials Harvesting.md](./Credentials%20Harvesting.md) |
| 85 | **Crocc Crew** | `Medium` | `1.5 - 2 hrs` | 2020 | Web CTF | 41.8 KB | [Crocc Crew.md](./Crocc%20Crew.md) |
| 86 | **Cross-site Scripting-1** | `Easy` | `1 hr` | 2021 | Web Fundamentals | 25.3 KB | [Cross-site Scripting-1.md](./Cross-site%20Scripting-1.md) |
| 87 | **Cross-site Scripting** | `Easy` | `1 hr` | 2020 | Web Fundamentals | 24.6 KB | [Cross-site Scripting.md](./Cross-site%20Scripting.md) |
| 88 | **Crylo** | `Medium` | `1.5 - 2 hrs` | 2021 | Crypto / Linux | 77.5 KB | [Crylo.md](./Crylo.md) |
| 89 | **Cyber Kill Chain** | `Info` | `30 mins` | 2021 | Defensive Concepts | 22.6 KB | [Cyber Kill Chain.md](./Cyber%20Kill%20Chain.md) |
| 90 | **Cyber Scotland 2021** | `Easy` | `1.5 hrs` | 2021 | Event CTF | 46.7 KB | [Cyber Scotland 2021.md](./Cyber%20Scotland%202021.md) |
| 91 | **CyberCrafted** | `Medium` | `2 - 3 hrs` | 2021 | Minecraft / Linux CTF | 151.8 KB | [CyberCrafted.md](./CyberCrafted.md) |
| 92 | **CyberHeroes** | `Easy` | `20 mins` | 2022 | Web Authentication | 3.6 KB | [CyberHeroes.md](./CyberHeroes.md) |
| 93 | **Cyborg** | `Easy` | `45 mins` | 2020 | Linux / Borg Backup | 2.0 KB | [Cyborg.md](./Cyborg.md) |
| 94 | **DDOS** | `Info` | `20 mins` | 2020 | Networking Basics | 1.3 KB | [DDOS.md](./DDOS.md) |
| 95 | **DFIR An Introduction** | `Info` | `30 mins` | 2021 | DFIR Basics | 16.7 KB | [DFIR An Introduction.md](./DFIR%20An%20Introduction.md) |
| 96 | **DNS** | `Info` | `30 mins` | 2020 | Networking Basics | 7.3 KB | [DNS.md](./DNS.md) |
| 97 | **DX1 Liberty Island** | `Medium` | `1.5 - 2 hrs` | 2022 | Linux CTF | 28.6 KB | [DX1 Liberty Island.md](./DX1%20Liberty%20Island.md) |
| 98 | **Daily Bugle** | `Hard` | `2 - 3 hrs` | 2019 | Joomla / SQLi / Linux | 38.5 KB | [Daily Bugle.md](./Daily%20Bugle.md) |
| 99 | **Data Exfiltration** | `Medium` | `2 hrs` | 2022 | Network / Red Team | 95.5 KB | [Data Exfiltration.md](./Data%20Exfiltration.md) |
| 100 | **Dav** | `Easy` | `30 mins` | 2020 | WebDAV Exploit | 7.1 KB | [Dav.md](./Dav.md) |
| 101 | **Debug** | `Medium` | `1.5 - 2 hrs` | 2021 | PHP Deserialization | 20.3 KB | [Debug.md](./Debug.md) |
| 102 | **Deja Vu** | `Medium` | `1.5 - 2 hrs` | 2021 | Linux CTF | 48.1 KB | [Deja Vu.md](./Deja%20Vu.md) |
| 103 | **Dependency Management** | `Medium` | `1.5 hrs` | 2022 | DevSecOps | 59.1 KB | [Dependency Management.md](./Dependency%20Management.md) |
| 104 | **Develpy** | `Easy` | `45 mins` | 2020 | Linux / Python Esc | 20.1 KB | [Develpy.md](./Develpy.md) |
| 105 | **Diamond Model** | `Info` | `30 mins` | 2021 | Threat Intel | 13.9 KB | [Diamond Model.md](./Diamond%20Model.md) |
| 106 | **Different CTF** | `Medium` | `1.5 hrs` | 2020 | CTF Challenge | 17.7 KB | [Different CTF.md](./Different%20CTF.md) |
| 107 | **Dig Dug** | `Easy` | `20 mins` | 2022 | DNS Recon | 1.3 KB | [Dig Dug.md](./Dig%20Dug.md) |
| 108 | **Digital Forensics Case B4DM755** | `Medium` | `1.5 - 2 hrs` | 2021 | DFIR Case | 35.5 KB | [Digital Forensics Case B4DM755.md](./Digital%20Forensics%20Case%20B4DM755.md) |
| 109 | **Dirty Pipe** | `Easy` | `30 - 45 mins` | 2022 | CVE-2022-0847 Exploit | 10.4 KB | [Dirty Pipe.md](./Dirty%20Pipe.md) |
| 110 | **Dissecting PE Headers** | `Medium` | `1.5 hrs` | 2022 | Reverse Engineering | 32.4 KB | [Dissecting PE Headers.md](./Dissecting%20PE%20Headers.md) |
| 111 | **Easy Peasy** | `Easy` | `45 mins` | 2020 | Linux CTF | 3.3 KB | [Easy Peasy.md](./Easy%20Peasy.md) |
| 112 | **Eavesdropper** | `Medium` | `1.5 hrs` | 2022 | Linux Network Sniffing | 25.7 KB | [Eavesdropper.md](./Eavesdropper.md) |
| 113 | **Empire** | `Medium` | `2 hrs` | 2021 | PowerShell Empire C2 | 35.8 KB | [Empire.md](./Empire.md) |
| 114 | **Empline** | `Medium` | `1.5 - 2 hrs` | 2021 | Linux / Asterisk CTF | 45.2 KB | [Empline.md](./Empline.md) |
| 115 | **En-pass** | `Easy` | `1 hr` | 2021 | Linux CTF | 61.1 KB | [En-pass.md](./En-pass.md) |
| 116 | **Enterprise** | `Hard` | `3 - 4 hrs` | 2020 | Buffer Overflow / Linux | 33.4 KB | [Enterprise.md](./Enterprise.md) |
| 117 | **Enumeration** | `Easy` | `1.5 hrs` | 2020 | Reconnaissance | 64.9 KB | [Enumeration.md](./Enumeration.md) |
| 118 | **Epoch** | `Easy` | `20 - 30 mins` | 2022 | Command Injection | 17.2 KB | [Epoch.md](./Epoch.md) |
| 119 | **Erit Securus I** | `Medium` | `1.5 - 2 hrs` | 2021 | Linux CTF | 30.5 KB | [Erit Securus I.md](./Erit%20Securus%20I.md) |
| 120 | **Evading Logging and Monitoring** | `Hard` | `2.5 - 3.5 hrs` | 2022 | Evasion / Defense | 31.1 KB | [Evading Logging and Monitoring.md](./Evading%20Logging%20and%20Monitoring.md) |
| 121 | **Exploit Vulnerabilities** | `Easy` | `45 mins` | 2021 | Pentesting Basics | 12.4 KB | [Exploit Vulnerabilities.md](./Exploit%20Vulnerabilities.md) |
| 122 | **Extending Your Network** | `Info` | `30 mins` | 2021 | Networking Basics | 12.9 KB | [Extending Your Network.md](./Extending%20Your%20Network.md) |
| 123 | **File Inclusion** | `Easy` | `1 hr` | 2021 | LFI / RFI Fundamentals | 28.5 KB | [File Inclusion.md](./File%20Inclusion.md) |
| 124 | **Firewalls** | `Easy` | `1 hr` | 2021 | Network Security | 35.8 KB | [Firewalls.md](./Firewalls.md) |
| 125 | **Flatline** | `Medium` | `1.5 hrs` | 2021 | FreePBX / Linux | 19.1 KB | [Flatline.md](./Flatline.md) |
| 126 | **Flip** | `Medium` | `1.5 - 2 hrs` | 2021 | Crypto / CBC Bit-flipping | 10.3 KB | [Flip.md](./Flip.md) |
| 127 | **Follina MSDT** | `Easy` | `30 - 45 mins` | 2022 | CVE-2022-30190 | 42.1 KB | [Follina MSDT.md](./Follina%20MSDT.md) |
| 128 | **Forgotten Implant** | `Medium` | `1.5 - 2 hrs` | 2022 | C2 / Incident Response | 26.4 KB | [Forgotten Implant.md](./Forgotten%20Implant.md) |
| 129 | **Fowsniff CTF** | `Easy` | `1 hr` | 2019 | Linux CTF | 37.0 KB | [Fowsniff CTF.md](./Fowsniff%20CTF.md) |
| 130 | **Fusion Corp** | `Medium` | `2 - 3 hrs` | 2021 | Active Directory | 32.3 KB | [Fusion Corp.md](./Fusion%20Corp.md) |
| 131 | **GLITCH** | `Easy` | `1 hr` | 2020 | Node.js / Linux CTF | 20.5 KB | [GLITCH.md](./GLITCH.md) |
| 132 | **Gallery** | `Easy` | `1 hr` | 2021 | Linux / Web CMS | 39.8 KB | [Gallery.md](./Gallery.md) |
| 133 | **Game Zone** | `Easy` | `1 - 1.5 hrs` | 2019 | SQLi / SSH Tunneling | 30.6 KB | [Game Zone.md](./Game%20Zone.md) |
| 134 | **GamingServer** | `Easy` | `1 hr` | 2020 | Linux CTF / PrivEsc | 24.8 KB | [GamingServer.md](./GamingServer.md) |
| 135 | **Gatekeeper** | `Medium` | `2 - 3 hrs` | 2020 | Buffer Overflow / Windows | 47.7 KB | [Gatekeeper.md](./Gatekeeper.md) |
| 136 | **Generic University** | `Medium` | `1.5 hrs` | 2021 | Web / Linux CTF | 21.0 KB | [Generic University.md](./Generic%20University.md) |
| 137 | **Ghizer** | `Hard` | `3 - 4 hrs` | 2021 | Multi-stage Linux CTF | 405.3 KB | [Ghizer.md](./Ghizer.md) |
| 138 | **Git_crumpets** | `Medium` | `1.5 hrs` | 2021 | Git / Web Exploitation | 26.6 KB | [Git_crumpets.md](./Git_crumpets.md) |
| 139 | **GoldenEye** | `Medium` | `2 - 3 hrs` | 2019 | Linux / Pop3 / CTF | 181.6 KB | [GoldenEye.md](./GoldenEye.md) |
| 140 | **Gotta Catch'em All!** | `Easy` | `30 mins` | 2020 | Pokemon CTF | 1.3 KB | [Gotta Catch'em All!.md](./Gotta%20Catch%27em%20All%21.md) |
| 141 | **Grep** | `Medium` | `1.5 hrs` | 2021 | Linux PrivEsc | 25.2 KB | [Grep.md](./Grep.md) |
| 142 | **HA Joker CTF** | `Hard` | `3 - 4 hrs` | 2020 | Multi-level CTF | 63.0 KB | [HA Joker CTF.md](./HA%20Joker%20CTF.md) |
| 143 | **HackPark** | `Medium` | `1.5 - 2.5 hrs` | 2019 | Windows / Hydra / WinPE | 485.0 KB | [HackPark.md](./HackPark.md) |
| 144 | **Hack_printer** | `Easy` | `20 mins` | 2020 | Printer Hacking | 1.2 KB | [Hack_printer.md](./Hack_printer.md) |
| 145 | **Hacked** | `Easy` | `30 mins` | 2020 | PCAP Analysis | 5.9 KB | [Hacked.md](./Hacked.md) |
| 146 | **Hacker vs. Hacker** | `Easy` | `45 mins` | 2022 | Web Shell Hunting | 12.1 KB | [Hacker vs. Hacker.md](./Hacker%20vs.%20Hacker.md) |
| 147 | **Hacking with PowerShell** | `Medium` | `2 - 3 hrs` | 2020 | PowerShell Red Team | 235.0 KB | [Hacking with PowerShell.md](./Hacking%20with%20PowerShell.md) |
| 148 | **Hamlet** | `Medium` | `1.5 hrs` | 2021 | Linux CTF | 30.1 KB | [Hamlet.md](./Hamlet.md) |
| 149 | **Hardening Basics Part 1** | `Easy` | `1.5 hrs` | 2022 | Defensive Hardening | 80.0 KB | [Hardening Basics Part 1.md](./Hardening%20Basics%20Part%201.md) |
| 150 | **Hardening Basics Part 2** | `Easy` | `1.5 hrs` | 2022 | Defensive Hardening | 50.4 KB | [Hardening Basics Part 2.md](./Hardening%20Basics%20Part%202.md) |
| 151 | **Hashing - Crypto 101** | `Easy` | `45 mins` | 2020 | Cryptography Basics | 18.5 KB | [Hashing - Crypto 101.md](./Hashing%20-%20Crypto%20101.md) |
| 152 | **HaskHell** | `Medium` | `1.5 hrs` | 2020 | Haskell / Linux CTF | 11.0 KB | [HaskHell.md](./HaskHell.md) |
| 153 | **HeartBleed** | `Easy` | `45 mins` | 2020 | OpenSSL Vulnerability | 46.5 KB | [HeartBleed.md](./HeartBleed.md) |
| 154 | **HipFlask** | `Hard` | `3 - 4 hrs` | 2021 | Binary / Web CTF | 138.2 KB | [HipFlask.md](./HipFlask.md) |
| 155 | **Holo** | `Insane` | `6 - 10 hrs` | 2021 | Network Lab / Multi-node | 491.2 KB | [Holo.md](./Holo.md) |
| 156 | **How websites work** | `Info` | `30 mins` | 2020 | Web Fundamentals | 17.9 KB | [How websites work.md](./How%20websites%20work.md) |
| 157 | **IDE** | `Easy` | `45 mins` | 2021 | Web / Linux PrivEsc | 30.9 KB | [IDE.md](./IDE.md) |
| 158 | **IDOR** | `Easy` | `30 mins` | 2021 | Web Security | 6.2 KB | [IDOR.md](./IDOR.md) |
| 159 | **Ignite** | `Easy` | `45 mins` | 2019 | Fuel CMS Exploit | 10.0 KB | [Ignite.md](./Ignite.md) |
| 160 | **Incident handling with Splunk** | `Medium` | `2 hrs` | 2021 | SOC / Splunk | 44.6 KB | [Incident handling with Splunk.md](./Incident%20handling%20with%20Splunk.md) |
| 161 | **Inferno** | `Medium` | `1.5 hrs` | 2020 | Linux CTF / Codiad | 13.8 KB | [Inferno.md](./Inferno.md) |
| 162 | **Insekube** | `Hard` | `3 - 4 hrs` | 2021 | Kubernetes Pentest | 90.0 KB | [Insekube.md](./Insekube.md) |
| 163 | **Intermediate Nmap** | `Easy` | `45 mins` | 2020 | Recon / Nmap | 10.4 KB | [Intermediate Nmap.md](./Intermediate%20Nmap.md) |
| 164 | **Internal** | `Hard` | `2.5 - 3.5 hrs` | 2020 | AD / WordPress / Jenkins | 31.5 KB | [Internal.md](./Internal.md) |
| 165 | **Intro To Pwntools** | `Medium` | `2 hrs` | 2021 | Exploit Dev / Python | 84.3 KB | [Intro To Pwntools.md](./Intro%20To%20Pwntools.md) |
| 166 | **Intro to C2** | `Easy` | `1 hr` | 2022 | C2 Frameworks | 60.6 KB | [Intro to C2.md](./Intro%20to%20C2.md) |
| 167 | **Intro to Cloud Security** | `Info` | `45 mins` | 2022 | Cloud Concepts | 38.7 KB | [Intro to Cloud Security.md](./Intro%20to%20Cloud%20Security.md) |
| 168 | **Intro to Containerisation** | `Info` | `30 mins` | 2022 | DevOps Security | 14.4 KB | [Intro to Containerisation.md](./Intro%20to%20Containerisation.md) |
| 169 | **Intro to Cyber Threat Intel** | `Info` | `30 mins` | 2022 | Threat Intelligence | 13.3 KB | [Intro to Cyber Threat Intel.md](./Intro%20to%20Cyber%20Threat%20Intel.md) |
| 170 | **Intro to Defensive Security** | `Info` | `30 mins` | 2021 | Blue Team Basics | 16.2 KB | [Intro to Defensive Security.md](./Intro%20to%20Defensive%20Security.md) |
| 171 | **Intro to Detection Engineering** | `Medium` | `1.5 hrs` | 2022 | Detection / Blue Team | 26.9 KB | [Intro to Detection Engineering.md](./Intro%20to%20Detection%20Engineering.md) |
| 172 | **Intro to Docker** | `Easy` | `1 hr` | 2021 | Containers / Docker | 47.0 KB | [Intro to Docker.md](./Intro%20to%20Docker.md) |
| 173 | **Intro to Endpoint Security** | `Info` | `30 mins` | 2022 | Endpoint Defense | 15.7 KB | [Intro to Endpoint Security.md](./Intro%20to%20Endpoint%20Security.md) |
| 174 | **Intro to ISAC** | `Info` | `30 mins` | 2022 | Information Sharing | 22.1 KB | [Intro to ISAC.md](./Intro%20to%20ISAC.md) |
| 175 | **Intro to Malware Analysis** | `Medium` | `1.5 - 2 hrs` | 2021 | Malware Analysis | 43.1 KB | [Intro to Malware Analysis.md](./Intro%20to%20Malware%20Analysis.md) |
| 176 | **Intro to Offensive Security** | `Info` | `20 mins` | 2021 | Red Team Basics | 8.2 KB | [Intro to Offensive Security.md](./Intro%20to%20Offensive%20Security.md) |
| 177 | **Intro to Pipeline Automation** | `Easy` | `1 hr` | 2022 | CI/CD Security | 33.3 KB | [Intro to Pipeline Automation.md](./Intro%20to%20Pipeline%20Automation.md) |
| 178 | **Intro to Threat Emulation** | `Medium` | `1.5 hrs` | 2022 | Adversary Emulation | 33.3 KB | [Intro to Threat Emulation.md](./Intro%20to%20Threat%20Emulation.md) |
| 179 | **Introduction To Honeypots** | `Easy` | `1 hr` | 2021 | Blue Team Defense | 59.4 KB | [Introduction To Honeypots.md](./Introduction%20To%20Honeypots.md) |
| 180 | **Introduction to Cryptography** | `Medium` | `2 hrs` | 2020 | Applied Crypto | 109.9 KB | [Introduction to Cryptography.md](./Introduction%20to%20Cryptography.md) |
| 181 | **Introduction to Flask** | `Easy` | `1 hr` | 2021 | Web Development | 20.7 KB | [Introduction to Flask.md](./Introduction%20to%20Flask.md) |
| 182 | **Introduction to SIEM** | `Info` | `30 mins` | 2021 | SOC Monitoring | 15.8 KB | [Introduction to SIEM.md](./Introduction%20to%20SIEM.md) |
| 183 | **Intrusion Detection** | `Medium` | `2 - 3 hrs` | 2021 | Snort / Suricata IDS | 258.3 KB | [Intrusion Detection.md](./Intrusion%20Detection.md) |
| 184 | **Investigating with ELK 101** | `Easy` | `1 hr` | 2021 | ELK Stack / DFIR | 22.0 KB | [Investigating with ELK 101.md](./Investigating%20with%20ELK%20101.md) |
| 185 | **Iron Corp** | `Medium` | `1.5 - 2 hrs` | 2020 | Windows CTF | 40.0 KB | [Iron Corp.md](./Iron%20Corp.md) |
| 186 | **ItsyBitsy** | `Easy` | `30 mins` | 2022 | Log Analysis | 3.1 KB | [ItsyBitsy.md](./ItsyBitsy.md) |
| 187 | **JPGChat** | `Easy` | `30 mins` | 2021 | Linux / Python Injection | 8.4 KB | [JPGChat.md](./JPGChat.md) |
| 188 | **Jack-of-All-Trades** | `Easy` | `45 mins` | 2020 | Multi-skill CTF | 13.8 KB | [Jack-of-All-Trades.md](./Jack-of-All-Trades.md) |
| 189 | **Jack** | `Medium` | `2 hrs` | 2020 | WordPress / FastCGI CTF | 159.9 KB | [Jack.md](./Jack.md) |
| 190 | **Jacob the Boss** | `Medium` | `1 - 1.5 hrs` | 2020 | JBoss Exploitation | 19.4 KB | [Jacob the Boss.md](./Jacob%20the%20Boss.md) |
| 191 | **Jason** | `Easy` | `45 mins` | 2021 | Node.js Deserialization | 24.3 KB | [Jason.md](./Jason.md) |
| 192 | **Jeff** | `Medium` | `1.5 - 2 hrs` | 2020 | WordPress / Linux CTF | 45.6 KB | [Jeff.md](./Jeff.md) |
| 193 | **John The Ripper** | `Easy` | `1 hr` | 2020 | Password Cracking | 47.0 KB | [John The Ripper.md](./John%20The%20Ripper.md) |
| 194 | **Junior Security Analyst Intro** | `Info` | `30 mins` | 2022 | SOC Analyst Path | 8.3 KB | [Junior Security Analyst Intro.md](./Junior%20Security%20Analyst%20Intro.md) |
| 195 | **Jurassic Park** | `Medium` | `1.5 hrs` | 2020 | SQLi / Linux CTF | 29.0 KB | [Jurassic Park.md](./Jurassic%20Park.md) |
| 196 | **KAPE** | `Medium` | `2 hrs` | 2022 | Triage Forensics | 169.5 KB | [KAPE.md](./KAPE.md) |
| 197 | **Keldagrim** | `Medium` | `1.5 hrs` | 2020 | Linux CTF | 52.3 KB | [Keldagrim.md](./Keldagrim.md) |
| 198 | **KoTH Food CTF** | `Medium` | `1.5 hrs` | 2020 | King of the Hill | 134.2 KB | [KoTH Food CTF.md](./KoTH%20Food%20CTF.md) |
| 199 | **KoTH Hackers** | `Medium` | `1.5 hrs` | 2020 | King of the Hill | 38.3 KB | [KoTH Hackers.md](./KoTH%20Hackers.md) |
| 200 | **Kubernetes for Everyone** | `Medium` | `2 hrs` | 2021 | Kubernetes Security | 111.8 KB | [Kubernetes for Everyone.md](./Kubernetes%20for%20Everyone.md) |
| 201 | **L2 MAC Flooding & ARP Spoofing** | `Medium` | `1.5 hrs` | 2022 | Network Attacks | 149.9 KB | [L2 MAC Flooding & ARP Spoofing.md](./L2%20MAC%20Flooding%20%26%20ARP%20Spoofing.md) |
| 202 | **LazyAdmin** | `Easy` | `30 mins` | 2019 | SweetRice CMS | 139.1 KB | [LazyAdmin.md](./LazyAdmin.md) |
| 203 | **Lesson Learned** | `Easy` | `30 mins` | 2022 | Incident Response | 4.3 KB | [Lesson Learned.md](./Lesson%20Learned.md) |
| 204 | **Library** | `Easy` | `45 mins` | 2020 | Linux CTF / Python | 36.5 KB | [Library.md](./Library.md) |
| 205 | **Linux Forensics** | `Medium` | `1.5 - 2 hrs` | 2022 | DFIR / Linux | 43.0 KB | [Linux Forensics.md](./Linux%20Forensics.md) |
| 206 | **Linux Local Enumeration** | `Easy` | `1 hr` | 2020 | PrivEsc Fundamentals | 33.3 KB | [Linux Local Enumeration.md](./Linux%20Local%20Enumeration.md) |
| 207 | **LinuxFunctionHooking** | `Hard` | `2.5 hrs` | 2022 | Linux Internals / Hooking | 35.6 KB | [LinuxFunctionHooking.md](./LinuxFunctionHooking.md) |
| 208 | **Living Off the Land** | `Medium` | `1.5 hrs` | 2022 | LOLBAS / LOLBins | 36.8 KB | [Living Off the Land.md](./Living%20Off%20the%20Land.md) |
| 209 | **LocalPotato** | `Medium` | `1 hr` | 2023 | Windows PrivEsc / CVE-2023-21746 | 37.3 KB | [LocalPotato.md](./LocalPotato.md) |
| 210 | **Lockdown** | `Medium` | `1.5 hrs` | 2021 | Linux CTF | 31.3 KB | [Lockdown.md](./Lockdown.md) |
| 211 | **Lookback** | `Hard` | `3 - 4 hrs` | 2022 | Active Directory / Exchange | 74.3 KB | [Lookback.md](./Lookback.md) |
| 212 | **Looking_Glass** | `Easy` | `45 mins` | 2020 | SSH / Stego CTF | 14.5 KB | [Looking_Glass.md](./Looking_Glass.md) |
| 213 | **Lumberjack Turtle** | `Medium` | `1.5 hrs` | 2021 | Log4j / CVE-2021-44228 | 83.0 KB | [Lumberjack Turtle.md](./Lumberjack%20Turtle.md) |
| 214 | **Lunizz CTF** | `Medium` | `1.5 hrs` | 2021 | Linux CTF | 25.3 KB | [Lunizz CTF.md](./Lunizz%20CTF.md) |
| 215 | **MAL REMnux The Redux** | `Medium` | `1.5 hrs` | 2021 | Malware Analysis | 37.3 KB | [MAL REMnux The Redux.md](./MAL%20REMnux%20The%20Redux.md) |
| 216 | **MAL Strings** | `Easy` | `30 mins` | 2021 | Static Analysis | 10.5 KB | [MAL Strings.md](./MAL%20Strings.md) |
| 217 | **MD2PDF** | `Easy` | `30 mins` | 2022 | SSRF / XSS | 16.6 KB | [MD2PDF.md](./MD2PDF.md) |
| 218 | **MISP** | `Medium` | `1.5 hrs` | 2022 | Threat Sharing | 16.9 KB | [MISP.md](./MISP.md) |
| 219 | **Madeye's Castle** | `Medium` | `1.5 - 2 hrs` | 2021 | Linux CTF | 30.3 KB | [Madeye's Castle.md](./Madeye%27s%20Castle.md) |
| 220 | **Magician** | `Easy` | `1 hr` | 2021 | ImageMagick / Linux CTF | 14.1 KB | [Magician.md](./Magician.md) |
| 221 | **Masterminds** | `Easy` | `1 hr` | 2022 | Zeek / Network Traffic | 7.9 KB | [Masterminds.md](./Masterminds.md) |
| 222 | **Metamorphosis** | `Medium` | `2 hrs` | 2022 | Active Directory | 44.0 KB | [Metamorphosis.md](./Metamorphosis.md) |
| 223 | **Metasploit  Meterpreter** | `Easy` | `1 hr` | 2020 | Tool Walkthrough | 46.5 KB | [Metasploit  Meterpreter.md](./Metasploit%20%20Meterpreter.md) |
| 224 | **Metasploit Exploitation** | `Easy` | `1.5 hrs` | 2020 | Tool Walkthrough | 127.7 KB | [Metasploit Exploitation.md](./Metasploit%20Exploitation.md) |
| 225 | **Metasploit** | `Easy` | `1.5 hrs` | 2020 | Tool Walkthrough | 110.5 KB | [Metasploit.md](./Metasploit.md) |
| 226 | **Microsoft Windows Hardening** | `Medium` | `1.5 hrs` | 2022 | Defensive Hardening | 29.1 KB | [Microsoft Windows Hardening.md](./Microsoft%20Windows%20Hardening.md) |
| 227 | **Mindgames** | `Medium` | `1.5 hrs` | 2021 | Brainfuck / Python PrivEsc | 22.0 KB | [Mindgames.md](./Mindgames.md) |
| 228 | **Minotaur's Labyrinth** | `Medium` | `1.5 hrs` | 2021 | Web / SQLi CTF | 15.8 KB | [Minotaur's Labyrinth.md](./Minotaur%27s%20Labyrinth.md) |
| 229 | **Mnemonic** | `Medium` | `2 hrs` | 2022 | Active Directory / Forensics | 44.3 KB | [Mnemonic.md](./Mnemonic.md) |
| 230 | **Mr. Phisher** | `Easy` | `30 mins` | 2022 | Phishing Analysis | 11.1 KB | [Mr. Phisher.md](./Mr.%20Phisher.md) |
| 231 | **Mustacchio** | `Easy` | `45 mins` | 2021 | Linux / Web CTF | 14.0 KB | [Mustacchio.md](./Mustacchio.md) |
| 232 | **NIS - Linux Part I** | `Medium` | `1.5 hrs` | 2021 | Network Services | 98.5 KB | [NIS - Linux Part I.md](./NIS%20-%20Linux%20Part%20I.md) |
| 233 | **NahamStore** | `Medium` | `2.5 - 3.5 hrs` | 2022 | Web Pentesting Lab | 208.1 KB | [NahamStore.md](./NahamStore.md) |
| 234 | **Napping** | `Medium` | `1 hr` | 2022 | Web Tabnabbing | 62.1 KB | [Napping.md](./Napping.md) |
| 235 | **Neighbour** | `Easy` | `20 mins` | 2022 | IDOR Vulnerability | 6.2 KB | [Neighbour.md](./Neighbour.md) |
| 236 | **NerdHerd** | `Easy` | `1 hr` | 2020 | Linux CTF / Samba | 27.1 KB | [NerdHerd.md](./NerdHerd.md) |
| 237 | **Net Sec Challenge** | `Medium` | `1.5 hrs` | 2021 | Network Challenge | 21.2 KB | [Net Sec Challenge.md](./Net%20Sec%20Challenge.md) |
| 238 | **Network Security Solutions** | `Medium` | `1.5 hrs` | 2022 | IDS / IPS / Firewalls | 42.3 KB | [Network Security Solutions.md](./Network%20Security%20Solutions.md) |
| 239 | **Network Security** | `Info` | `30 mins` | 2020 | Networking Basics | 15.1 KB | [Network Security.md](./Network%20Security.md) |
| 240 | **Network Services 2** | `Easy` | `1.5 hrs` | 2020 | NFS / SMTP / MySQL | 48.0 KB | [Network Services 2.md](./Network%20Services%202.md) |
| 241 | **Network Services** | `Easy` | `1.5 hrs` | 2020 | SMB / Telnet / FTP | 26.6 KB | [Network Services.md](./Network%20Services.md) |
| 242 | **NetworkMiner** | `Easy` | `45 mins` | 2021 | PCAP Forensics | 29.4 KB | [NetworkMiner.md](./NetworkMiner.md) |
| 243 | **New Hire Old Artifacts** | `Easy` | `45 mins` | 2022 | DFIR / Splunk | 10.3 KB | [New Hire Old Artifacts.md](./New%20Hire%20Old%20Artifacts.md) |
| 244 | **Ninja Skills** | `Easy` | `45 mins` | 2020 | Linux Command Line | 9.3 KB | [Ninja Skills.md](./Ninja%20Skills.md) |
| 245 | **Nmap Advanced Port Scans** | `Medium` | `1 hr` | 2021 | Recon / Nmap | 37.7 KB | [Nmap Advanced Port Scans.md](./Nmap%20Advanced%20Port%20Scans.md) |
| 246 | **Nmap Basic Port Scans** | `Easy` | `45 mins` | 2021 | Recon / Nmap | 20.4 KB | [Nmap Basic Port Scans.md](./Nmap%20Basic%20Port%20Scans.md) |
| 247 | **Nmap Post Port Scans** | `Medium` | `1 hr` | 2021 | Recon / Nmap | 39.5 KB | [Nmap Post Port Scans.md](./Nmap%20Post%20Port%20Scans.md) |
| 248 | **NoNameCTF** | `Medium` | `1.5 hrs` | 2021 | Linux CTF | 47.8 KB | [NoNameCTF.md](./NoNameCTF.md) |
| 249 | **NoSQL injection Basics** | `Medium` | `1 hr` | 2021 | Web / NoSQLi | 19.7 KB | [NoSQL injection Basics.md](./NoSQL%20injection%20Basics.md) |
| 250 | **OSI Model** | `Info` | `30 mins` | 2020 | Networking Basics | 12.2 KB | [OSI Model.md](./OSI%20Model.md) |
| 251 | **OWASP API Security Top 10 - 1** | `Medium` | `1.5 hrs` | 2022 | API Security | 42.7 KB | [OWASP API Security Top 10 - 1.md](./OWASP%20API%20Security%20Top%2010%20-%201.md) |
| 252 | **OWASP API Security Top 10 - 2** | `Medium` | `1.5 hrs` | 2022 | API Security | 33.2 KB | [OWASP API Security Top 10 - 2.md](./OWASP%20API%20Security%20Top%2010%20-%202.md) |
| 253 | **OWASP Broken Access Control** | `Medium` | `1 hr` | 2022 | Web Security | 29.0 KB | [OWASP Broken Access Control.md](./OWASP%20Broken%20Access%20Control.md) |
| 254 | **OWASP Top 10 - 2021** | `Easy` | `2 hrs` | 2021 | Web Security | 72.4 KB | [OWASP Top 10 - 2021.md](./OWASP%20Top%2010%20-%202021.md) |
| 255 | **Obfuscation Principles** | `Hard` | `2 hrs` | 2022 | Malware / Evasion | 36.9 KB | [Obfuscation Principles.md](./Obfuscation%20Principles.md) |
| 256 | **Oh My WebServer** | `Medium` | `1 hr` | 2021 | CVE-2021-42013 / Docker | 16.6 KB | [Oh My WebServer.md](./Oh%20My%20WebServer.md) |
| 257 | **Ollie** | `Medium` | `1.5 hrs` | 2022 | Linux CTF / phpIPAM | 31.0 KB | [Ollie.md](./Ollie.md) |
| 258 | **Olympus** | `Hard` | `2.5 - 3.5 hrs` | 2021 | Web / Linux CTF | 51.8 KB | [Olympus.md](./Olympus.md) |
| 259 | **One Piece** | `Medium` | `1.5 hrs` | 2020 | Anime CTF / Linux | 88.1 KB | [One Piece.md](./One%20Piece.md) |
| 260 | **Opacity** | `Easy` | `1 hr` | 2022 | PHP Upload / KeePass | 38.5 KB | [Opacity.md](./Opacity.md) |
| 261 | **OpenCTI** | `Medium` | `1.5 hrs` | 2022 | Threat Intelligence | 15.3 KB | [OpenCTI.md](./OpenCTI.md) |
| 262 | **Operating System Security** | `Info` | `30 mins` | 2021 | Security Basics | 15.5 KB | [Operating System Security.md](./Operating%20System%20Security.md) |
| 263 | **Osiris** | `Hard` | `3 - 4 hrs` | 2021 | Active Directory / CTF | 102.3 KB | [Osiris.md](./Osiris.md) |
| 264 | **Osquery The Basics** | `Easy` | `1 hr` | 2021 | Endpoint Visibility | 140.7 KB | [Osquery The Basics.md](./Osquery%20The%20Basics.md) |
| 265 | **Osquery** | `Easy` | `1 hr` | 2021 | Endpoint Visibility | 69.2 KB | [Osquery.md](./Osquery.md) |
| 266 | **Outlook NTLM Leak** | `Medium` | `1 hr` | 2023 | CVE-2023-23397 | 36.8 KB | [Outlook NTLM Leak.md](./Outlook%20NTLM%20Leak.md) |
| 267 | **OverlayFS** | `Easy` | `30 mins` | 2021 | CVE-2021-3493 Exploit | 1.2 KB | [OverlayFS.md](./OverlayFS.md) |
| 268 | **Overpass** | `Easy` | `45 mins` | 2020 | Broken Auth / Linux CTF | 6.8 KB | [Overpass.md](./Overpass.md) |
| 269 | **Overpass3** | `Medium` | `1.5 hrs` | 2020 | Web / GPG / Linux CTF | 30.0 KB | [Overpass3.md](./Overpass3.md) |
| 270 | **PS Eclipse** | `Medium` | `1 hr` | 2022 | PowerShell Script Analysis | 16.0 KB | [PS Eclipse.md](./PS%20Eclipse.md) |
| 271 | **Packets & Frames** | `Info` | `30 mins` | 2021 | Networking Basics | 19.2 KB | [Packets & Frames.md](./Packets%20%26%20Frames.md) |
| 272 | **ParrotPost Phishing Analysis** | `Medium` | `1.5 hrs` | 2022 | Phishing Analysis | 51.0 KB | [ParrotPost Phishing Analysis.md](./ParrotPost%20Phishing%20Analysis.md) |
| 273 | **Password Attacks** | `Medium` | `2 hrs` | 2022 | Cracking / Hydra / Hashcat | 84.2 KB | [Password Attacks.md](./Password%20Attacks.md) |
| 274 | **Phishing Emails 3** | `Medium` | `1 hr` | 2022 | Email Header Analysis | 22.2 KB | [Phishing Emails 3.md](./Phishing%20Emails%203.md) |
| 275 | **Phishing Emails 4** | `Medium` | `1 hr` | 2022 | Email Header Analysis | 15.2 KB | [Phishing Emails 4.md](./Phishing%20Emails%204.md) |
| 276 | **Phishing Emails 5** | `Medium` | `1 hr` | 2022 | Email Header Analysis | 3.5 KB | [Phishing Emails 5.md](./Phishing%20Emails%205.md) |
| 277 | **Phishing** | `Info` | `30 mins` | 2021 | Social Engineering | 22.4 KB | [Phishing.md](./Phishing.md) |
| 278 | **Phishing1** | `Easy` | `30 mins` | 2021 | Email Analysis Basics | 8.5 KB | [Phishing1.md](./Phishing1.md) |
| 279 | **Plotted-TMS** | `Medium` | `1.5 - 2 hrs` | 2021 | Traffic Management CMS | 118.0 KB | [Plotted-TMS.md](./Plotted-TMS.md) |
| 280 | **Polkit_CVE** | `Easy` | `30 mins` | 2021 | CVE-2021-3560 / CVE-2021-4034 | 14.7 KB | [Polkit_CVE.md](./Polkit_CVE.md) |
| 281 | **Poster** | `Easy` | `45 mins` | 2020 | PostgreSQL Exploitation | 40.0 KB | [Poster.md](./Poster.md) |
| 282 | **PowerShell for Pentesters** | `Medium` | `2 hrs` | 2020 | PowerShell Scripting | 149.7 KB | [PowerShell for Pentesters.md](./PowerShell%20for%20Pentesters.md) |
| 283 | **PrintNightmare, again!** | `Medium` | `45 mins` | 2021 | CVE-2021-34527 | 5.9 KB | [PrintNightmare, again!.md](./PrintNightmare%2C%20again%21.md) |
| 284 | **PrintNightmare, thrice!** | `Medium` | `45 mins` | 2021 | CVE-2021-36958 | 4.8 KB | [PrintNightmare, thrice!.md](./PrintNightmare%2C%20thrice%21.md) |
| 285 | **PrintNightmare** | `Medium` | `1 hr` | 2021 | CVE-2021-1675 / 34527 | 77.4 KB | [PrintNightmare.md](./PrintNightmare.md) |
| 286 | **Protocols and Servers 2** | `Info` | `30 mins` | 2021 | Networking Basics | 39.5 KB | [Protocols and Servers 2.md](./Protocols%20and%20Servers%202.md) |
| 287 | **Protocols and Servers** | `Info` | `30 mins` | 2021 | Networking Basics | 28.1 KB | [Protocols and Servers.md](./Protocols%20and%20Servers.md) |
| 288 | **Putting it all together** | `Easy` | `30 mins` | 2021 | Network Summary | 8.3 KB | [Putting it all together.md](./Putting%20it%20all%20together.md) |
| 289 | **Pwnkit** | `Easy` | `20 mins` | 2022 | CVE-2021-4034 Exploit | 10.1 KB | [Pwnkit.md](./Pwnkit.md) |
| 290 | **Pyramid Of Pain** | `Info` | `30 mins` | 2021 | Threat Intel Concept | 29.8 KB | [Pyramid Of Pain.md](./Pyramid%20Of%20Pain.md) |
| 291 | **Python for Pentesters** | `Easy` | `1 hr` | 2021 | Python Scripting | 33.5 KB | [Python for Pentesters.md](./Python%20for%20Pentesters.md) |
| 292 | **REmux The Tmux** | `Easy` | `30 mins` | 2021 | Terminal Multiplexer | 9.7 KB | [REmux The Tmux.md](./REmux%20The%20Tmux.md) |
| 293 | **Ra 2** | `Hard` | `3 - 4 hrs` | 2022 | Active Directory / PKI | 88.8 KB | [Ra 2.md](./Ra%202.md) |
| 294 | **Ra** | `Hard` | `3 - 4 hrs` | 2021 | Active Directory / Windmill | 90.2 KB | [Ra.md](./Ra.md) |
| 295 | **Racetrack Bank** | `Medium` | `1 hr` | 2022 | Race Conditions / Web | 22.8 KB | [Racetrack Bank.md](./Racetrack%20Bank.md) |
| 296 | **RazorBlack** | `Hard` | `3 - 4 hrs` | 2021 | Active Directory Lab | 58.1 KB | [RazorBlack.md](./RazorBlack.md) |
| 297 | **Recovery** | `Medium` | `2 hrs` | 2021 | Windows / Web CTF | 127.8 KB | [Recovery.md](./Recovery.md) |
| 298 | **Red Team OPSEC** | `Medium` | `1.5 hrs` | 2022 | Red Team Operations | 21.7 KB | [Red Team OPSEC.md](./Red%20Team%20OPSEC.md) |
| 299 | **Red Team Threat Intel** | `Medium` | `1.5 hrs` | 2022 | Red Team Intelligence | 13.4 KB | [Red Team Threat Intel.md](./Red%20Team%20Threat%20Intel.md) |
| 300 | **Red** | `Hard` | `3 - 4 hrs` | 2021 | Multi-stage Linux CTF | 45.8 KB | [Red.md](./Red.md) |
| 301 | **Redline** | `Medium` | `1.5 hrs` | 2021 | Memory & Endpoint DFIR | 26.1 KB | [Redline.md](./Redline.md) |
| 302 | **Relevant** | `Medium` | `1.5 - 2 hrs` | 2020 | Windows / PrintSpoofer CTF | 15.7 KB | [Relevant.md](./Relevant.md) |
| 303 | **Res** | `Easy` | `30 mins` | 2020 | Redis Exploitation | 14.5 KB | [Res.md](./Res.md) |
| 304 | **Retro** | `Hard` | `2 hrs` | 2019 | Windows / CVE-2019-1388 | 29.2 KB | [Retro.md](./Retro.md) |
| 305 | **Revenge** | `Medium` | `1.5 hrs` | 2020 | SQLi / Linux CTF | 46.8 KB | [Revenge.md](./Revenge.md) |
| 306 | **Revil_Corp** | `Medium` | `1.5 hrs` | 2021 | Ransomware Analysis | 5.1 KB | [Revil_Corp.md](./Revil_Corp.md) |
| 307 | **Road** | `Medium` | `1.5 hrs` | 2021 | Web / MongoDB / Docker | 19.3 KB | [Road.md](./Road.md) |
| 308 | **Runtime Detection Evasion** | `Hard` | `2 - 3 hrs` | 2022 | AMSI / ETW Evasion | 17.8 KB | [Runtime Detection Evasion.md](./Runtime%20Detection%20Evasion.md) |
| 309 | **SQHell** | `Medium` | `2 hrs` | 2020 | Advanced SQLi | 30.2 KB | [SQHell.md](./SQHell.md) |
| 310 | **SQLMAP** | `Easy` | `1 hr` | 2020 | SQLi Automation | 48.5 KB | [SQLMAP.md](./SQLMAP.md) |
| 311 | **SSRF** | `Medium` | `1 hr` | 2021 | Server-Side Request Forgery | 11.9 KB | [SSRF.md](./SSRF.md) |
| 312 | **Sandbox Evasion** | `Hard` | `2 hrs` | 2022 | Malware Evasion | 32.4 KB | [Sandbox Evasion.md](./Sandbox%20Evasion.md) |
| 313 | **Scripting** | `Medium` | `1.5 hrs` | 2020 | Python / Network Sockets | 21.7 KB | [Scripting.md](./Scripting.md) |
| 314 | **Sea Surfer** | `Hard` | `2.5 - 3.5 hrs` | 2021 | SSRF / Gitea / Linux | 51.4 KB | [Sea Surfer.md](./Sea%20Surfer.md) |
| 315 | **Secret Recipe** | `Medium` | `1.5 hrs` | 2021 | Memory Forensics | 23.3 KB | [Secret Recipe.md](./Secret%20Recipe.md) |
| 316 | **Security Engineer Intro** | `Info` | `30 mins` | 2022 | Engineering Career | 26.4 KB | [Security Engineer Intro.md](./Security%20Engineer%20Intro.md) |
| 317 | **Security Operations** | `Info` | `30 mins` | 2021 | SOC Overview | 10.6 KB | [Security Operations.md](./Security%20Operations.md) |
| 318 | **Security Principles** | `Info` | `30 mins` | 2021 | Security Basics | 26.2 KB | [Security Principles.md](./Security%20Principles.md) |
| 319 | **Set** | `Hard` | `2 hrs` | 2020 | Social Engineering Toolkit | 375.1 KB | [Set.md](./Set.md) |
| 320 | **Sigma** | `Medium` | `1.5 hrs` | 2022 | Detection Engineering | 95.8 KB | [Sigma.md](./Sigma.md) |
| 321 | **Signature Evasion** | `Hard` | `2.5 hrs` | 2022 | Defender Evasion | 46.2 KB | [Signature Evasion.md](./Signature%20Evasion.md) |
| 322 | **Skynet** | `Easy` | `1 hr` | 2019 | Linux / Samba / RFI | 29.0 KB | [Skynet.md](./Skynet.md) |
| 323 | **Smag Grotto** | `Easy` | `45 mins` | 2020 | PCAP / Linux CTF | 12.0 KB | [Smag Grotto.md](./Smag%20Grotto.md) |
| 324 | **Snapped Phishing Line** | `Medium` | `1.5 hrs` | 2022 | Phishing DFIR | 22.5 KB | [Snapped Phishing Line.md](./Snapped%20Phishing%20Line.md) |
| 325 | **Snort Challenge - Live Attacks** | `Hard` | `2.5 - 3.5 hrs` | 2022 | IDS / Snort Live | 16.8 KB | [Snort Challenge - Live Attacks.md](./Snort%20Challenge%20-%20Live%20Attacks.md) |
| 326 | **Snort Challenge - The Basics** | `Medium` | `2 hrs` | 2022 | IDS / Snort Rules | 124.5 KB | [Snort Challenge - The Basics.md](./Snort%20Challenge%20-%20The%20Basics.md) |
| 327 | **Snort** | `Easy` | `1.5 hrs` | 2022 | IDS Fundamentals | 1375.9 KB | [Snort.md](./Snort.md) |
| 328 | **Source** | `Easy` | `30 mins` | 2020 | Webmin CVE-2019-15107 | 1.7 KB | [Source.md](./Source.md) |
| 329 | **Splunk 101** | `Easy` | `1.5 hrs` | 2021 | SIEM Fundamentals | 28.8 KB | [Splunk 101.md](./Splunk%20101.md) |
| 330 | **Splunk 2** | `Medium` | `1.5 hrs` | 2021 | SIEM Querying | 36.0 KB | [Splunk 2.md](./Splunk%202.md) |
| 331 | **Splunk Basics** | `Easy` | `45 mins` | 2021 | SIEM Intro | 8.7 KB | [Splunk Basics.md](./Splunk%20Basics.md) |
| 332 | **Startup** | `Easy` | `1 hr` | 2020 | Linux / Wireshark CTF | 20.0 KB | [Startup.md](./Startup.md) |
| 333 | **Steel Mountain** | `Easy` | `1 hr` | 2019 | Windows / Reaver | 34.7 KB | [Steel Mountain.md](./Steel%20Mountain.md) |
| 334 | **Subdomain Enumeration** | `Easy` | `45 mins` | 2021 | Reconnaissance | 178.0 KB | [Subdomain Enumeration.md](./Subdomain%20Enumeration.md) |
| 335 | **Super-Spam** | `Medium` | `1.5 hrs` | 2020 | Email / Web CTF | 49.0 KB | [Super-Spam.md](./Super-Spam.md) |
| 336 | **Surfer** | `Easy` | `30 mins` | 2022 | SSRF Challenge | 6.2 KB | [Surfer.md](./Surfer.md) |
| 337 | **Sustah** | `Medium` | `1.5 hrs` | 2020 | Linux / Rate Limiting | 14.2 KB | [Sustah.md](./Sustah.md) |
| 338 | **Sweettooth Inc.** | `Medium` | `1.5 hrs` | 2021 | Docker / Linux CTF | 51.0 KB | [Sweettooth Inc..md](./Sweettooth%20Inc..md) |
| 339 | **Sysinternals** | `Easy` | `1 hr` | 2021 | Windows Tools | 32.2 KB | [Sysinternals.md](./Sysinternals.md) |
| 340 | **Sysmon** | `Medium` | `1.5 hrs` | 2021 | Windows Logging | 103.4 KB | [Sysmon.md](./Sysmon.md) |
| 341 | **TOR** | `Info` | `20 mins` | 2020 | Anonymity / TOR | 1.1 KB | [TOR.md](./TOR.md) |
| 342 | **Tactical Detection** | `Medium` | `1.5 hrs` | 2022 | Blue Team Detection | 27.5 KB | [Tactical Detection.md](./Tactical%20Detection.md) |
| 343 | **TakeOver** | `Easy` | `30 mins` | 2022 | Subdomain Takeover | 8.3 KB | [TakeOver.md](./TakeOver.md) |
| 344 | **Takedown** | `Medium` | `2 hrs` | 2021 | Active Directory / CTF | 48.4 KB | [Takedown.md](./Takedown.md) |
| 345 | **Tardigrade** | `Medium` | `1.5 hrs` | 2023 | Linux Persistence DFIR | 16.6 KB | [Tardigrade.md](./Tardigrade.md) |
| 346 | **Team** | `Easy` | `1 hr` | 2020 | Linux CTF / LFI | 32.1 KB | [Team.md](./Team.md) |
| 347 | **Tech_Supp0rt 1** | `Easy` | `45 mins` | 2021 | Linux / Subversion CTF | 16.9 KB | [Tech_Supp0rt 1.md](./Tech_Supp0rt%201.md) |
| 348 | **Tempest** | `Hard` | `3 hrs` | 2022 | Active Directory / CTF | 68.0 KB | [Tempest.md](./Tempest.md) |
| 349 | **Templates** | `Easy` | `45 mins` | 2021 | SSTI Fundamentals | 7.5 KB | [Templates.md](./Templates.md) |
| 350 | **Temple** | `Medium` | `1.5 hrs` | 2021 | Flask SSTI / Linux CTF | 165.1 KB | [Temple.md](./Temple.md) |
| 351 | **Tempus Fugit Durius** | `Hard` | `3 hrs` | 2021 | Linux / Advanced CTF | 154.2 KB | [Tempus Fugit Durius.md](./Tempus%20Fugit%20Durius.md) |
| 352 | **That's The Ticket** | `Medium` | `1.5 hrs` | 2021 | Kerberos / Web | 9.9 KB | [That's The Ticket.md](./That%27s%20The%20Ticket.md) |
| 353 | **The Blob Blog** | `Medium` | `1.5 hrs` | 2021 | Web / Node.js CTF | 49.5 KB | [The Blob Blog.md](./The%20Blob%20Blog.md) |
| 354 | **The Cod Caper** | `Medium` | `2 hrs` | 2020 | Buffer Overflow / Linux | 128.1 KB | [The Cod Caper.md](./The%20Cod%20Caper.md) |
| 355 | **The Docker Rodeo** | `Medium` | `1.5 hrs` | 2021 | Docker Escape CTF | 151.3 KB | [The Docker Rodeo.md](./The%20Docker%20Rodeo.md) |
| 356 | **The Great Escape** | `Medium` | `1.5 hrs` | 2021 | Docker Escape CTF | 34.2 KB | [The Great Escape.md](./The%20Great%20Escape.md) |
| 357 | **The Impossible Challenge** | `Medium` | `1.5 hrs` | 2020 | Reverse Engineering | 2.4 KB | [The Impossible Challenge.md](./The%20Impossible%20Challenge.md) |
| 358 | **The Lay of the land** | `Easy` | `45 mins` | 2020 | Reconnaissance | 56.5 KB | [The Lay of the land.md](./The%20Lay%20of%20the%20land.md) |
| 359 | **The Server From Hell** | `Hard` | `2.5 hrs` | 2020 | Tarpit / Port Scanning | 33.3 KB | [The Server From Hell.md](./The%20Server%20From%20Hell.md) |
| 360 | **TheHive Project** | `Easy` | `1 hr` | 2021 | Incident Response SOAR | 14.5 KB | [TheHive Project.md](./TheHive%20Project.md) |
| 361 | **Theseus** | `Hard` | `3 hrs` | 2021 | Linux / Advanced CTF | 123.1 KB | [Theseus.md](./Theseus.md) |
| 362 | **Thompson** | `Easy` | `30 mins` | 2020 | Tomcat Exploitation | 24.2 KB | [Thompson.md](./Thompson.md) |
| 363 | **Threat Intel & Containment** | `Medium` | `1.5 hrs` | 2022 | Threat Intelligence | 20.8 KB | [Threat Intel & Containment.md](./Threat%20Intel%20%26%20Containment.md) |
| 364 | **Tmux** | `Info` | `20 mins` | 2020 | Linux Utilities | 3.0 KB | [Tmux.md](./Tmux.md) |
| 365 | **Tokyo Ghoul** | `Medium` | `1.5 hrs` | 2021 | Python Jail / Linux CTF | 24.2 KB | [Tokyo Ghoul.md](./Tokyo%20Ghoul.md) |
| 366 | **Tony the Tiger** | `Medium` | `1.5 hrs` | 2020 | JBoss / Linux CTF | 41.5 KB | [Tony the Tiger.md](./Tony%20the%20Tiger.md) |
| 367 | **ToolsRus** | `Easy` | `30 mins` | 2019 | Basic Pentest Tools | 17.8 KB | [ToolsRus.md](./ToolsRus.md) |
| 368 | **Traffic Analysis Essentials** | `Easy` | `1 hr` | 2022 | Network Traffic Analysis | 11.3 KB | [Traffic Analysis Essentials.md](./Traffic%20Analysis%20Essentials.md) |
| 369 | **Training for New Analyst** | `Easy` | `1 hr` | 2022 | SOC Training | 72.3 KB | [Training for New Analyst.md](./Training%20for%20New%20Analyst.md) |
| 370 | **Unattended** | `Medium` | `1.5 hrs` | 2020 | Linux CTF | 22.8 KB | [Unattended.md](./Unattended.md) |
| 371 | **Undiscovered** | `Medium` | `1.5 hrs` | 2021 | Linux CTF | 22.8 KB | [Undiscovered.md](./Undiscovered.md) |
| 372 | **Unified Kill Chain** | `Info` | `30 mins` | 2021 | Threat Modeling | 19.8 KB | [Unified Kill Chain.md](./Unified%20Kill%20Chain.md) |
| 373 | **Upload Vulnerabilities** | `Easy` | `1 hr` | 2020 | File Upload Bypass | 48.9 KB | [Upload Vulnerabilities.md](./Upload%20Vulnerabilities.md) |
| 374 | **Uranium CTF** | `Medium` | `1.5 hrs` | 2021 | Linux CTF | 28.0 KB | [Uranium CTF.md](./Uranium%20CTF.md) |
| 375 | **Valley** | `Medium` | `1.5 hrs` | 2023 | Linux CTF | 14.4 KB | [Valley.md](./Valley.md) |
| 376 | **Velociraptor** | `Medium` | `1.5 hrs` | 2021 | Endpoint Forensics | 32.4 KB | [Velociraptor.md](./Velociraptor.md) |
| 377 | **Volatility** | `Medium` | `2 hrs` | 2020 | Memory Forensics | 309.4 KB | [Volatility.md](./Volatility.md) |
| 378 | **VulnNet Endgame** | `Hard` | `3.5 - 5 hrs` | 2021 | Active Directory / Enterprise | 58.3 KB | [VulnNet Endgame.md](./VulnNet%20Endgame.md) |
| 379 | **VulnNet Internal** | `Medium` | `2 - 3 hrs` | 2021 | Internal Network Pentest | 50.3 KB | [VulnNet Internal.md](./VulnNet%20Internal.md) |
| 380 | **VulnNet Node** | `Medium` | `1.5 hrs` | 2021 | Node.js Deserialization | 27.6 KB | [VulnNet Node.md](./VulnNet%20Node.md) |
| 381 | **VulnNet Roasted** | `Medium` | `2 hrs` | 2021 | Active Directory Roast | 69.3 KB | [VulnNet Roasted.md](./VulnNet%20Roasted.md) |
| 382 | **Vulnerability Capstone** | `Easy` | `45 mins` | 2021 | Capstone Lab | 4.1 KB | [Vulnerability Capstone.md](./Vulnerability%20Capstone.md) |
| 383 | **Warzone 1** | `Easy` | `45 mins` | 2022 | Network PCAP Analysis | 9.6 KB | [Warzone 1.md](./Warzone%201.md) |
| 384 | **Warzone 2** | `Medium` | `1 hr` | 2022 | Network PCAP Analysis | 10.1 KB | [Warzone 2.md](./Warzone%202.md) |
| 385 | **Watcher** | `Medium` | `1.5 - 2 hrs` | 2020 | Boot2Root / Linux CTF | 110.2 KB | [Watcher.md](./Watcher.md) |
| 386 | **Wazuh** | `Medium` | `2 hrs` | 2022 | SIEM & XDR | 34.3 KB | [Wazuh.md](./Wazuh.md) |
| 387 | **Weaponization** | `Medium` | `1.5 hrs` | 2022 | Red Team Weaponization | 40.6 KB | [Weaponization.md](./Weaponization.md) |
| 388 | **Weasel** | `Medium` | `1.5 hrs` | 2022 | WSL / Windows CTF | 34.7 KB | [Weasel.md](./Weasel.md) |
| 389 | **Web Enumeration** | `Easy` | `1 hr` | 2021 | Web Reconnaissance | 138.4 KB | [Web Enumeration.md](./Web%20Enumeration.md) |
| 390 | **Wekor** | `Medium` | `2 hrs` | 2021 | SQLi / WordPress / CyberChef | 101.8 KB | [Wekor.md](./Wekor.md) |
| 391 | **Wgel CTF** | `Easy` | `30 mins` | 2019 | Linux PrivEsc CTF | 9.0 KB | [Wgel CTF.md](./Wgel%20CTF.md) |
| 392 | **Willow** | `Easy` | `45 mins` | 2020 | Linux CTF | 18.6 KB | [Willow.md](./Willow.md) |
| 393 | **Windows Event Logs** | `Medium` | `2 hrs` | 2021 | Windows DFIR | 143.5 KB | [Windows Event Logs.md](./Windows%20Event%20Logs.md) |
| 394 | **Windows Forensics 1** | `Medium` | `1.5 hrs` | 2021 | Windows Forensics | 42.6 KB | [Windows Forensics 1.md](./Windows%20Forensics%201.md) |
| 395 | **Windows Forensics 2** | `Medium` | `1.5 hrs` | 2021 | Windows Forensics | 67.5 KB | [Windows Forensics 2.md](./Windows%20Forensics%202.md) |
| 396 | **Windows Internals** | `Medium` | `1.5 hrs` | 2021 | Operating System Internals | 26.5 KB | [Windows Internals.md](./Windows%20Internals.md) |
| 397 | **Windows Local Persistence** | `Medium` | `2 hrs` | 2022 | Red Team Persistence | 79.8 KB | [Windows Local Persistence.md](./Windows%20Local%20Persistence.md) |
| 398 | **Windows Privilege Escalation** | `Medium` | `2 hrs` | 2020 | PrivEsc Fundamentals | 134.2 KB | [Windows Privilege Escalation.md](./Windows%20Privilege%20Escalation.md) |
| 399 | **Windows Reversing Intro** | `Medium` | `1.5 hrs` | 2022 | Reverse Engineering | 40.5 KB | [Windows Reversing Intro.md](./Windows%20Reversing%20Intro.md) |
| 400 | **Wireshark 101** | `Easy` | `1 hr` | 2020 | Packet Analysis | 36.9 KB | [Wireshark 101.md](./Wireshark%20101.md) |
| 401 | **Wireshark Packet Operations** | `Easy` | `1 hr` | 2021 | Packet Analysis | 29.0 KB | [Wireshark Packet Operations.md](./Wireshark%20Packet%20Operations.md) |
| 402 | **Wireshark Traffic Analysis** | `Medium` | `1.5 hrs` | 2021 | Packet Analysis | 59.2 KB | [Wireshark Traffic Analysis.md](./Wireshark%20Traffic%20Analysis.md) |
| 403 | **Wonderland** | `Medium` | `1.5 hrs` | 2020 | Linux / Python Hijack | 9.0 KB | [Wonderland.md](./Wonderland.md) |
| 404 | **WordPress-Cve2021** | `Easy` | `45 mins` | 2021 | WordPress CVE Lab | 31.0 KB | [WordPress-Cve2021.md](./WordPress-Cve2021.md) |
| 405 | **Wreath** | `Insane` | `6 - 10 hrs` | 2021 | Enterprise Network Pivoting Lab | 329.7 KB | [Wreath.md](./Wreath.md) |
| 406 | **Yara** | `Easy` | `1 hr` | 2020 | Malware Detection Rules | 188.6 KB | [Yara.md](./Yara.md) |
| 407 | **Year of the Dog** | `Hard` | `2.5 - 3.5 hrs` | 2020 | 2FA Bypass / Linux CTF | 21.4 KB | [Year of the Dog.md](./Year%20of%20the%20Dog.md) |
| 408 | **Year of the Fox** | `Hard` | `2.5 - 3.5 hrs` | 2020 | Samba / SQLi CTF | 36.5 KB | [Year of the Fox.md](./Year%20of%20the%20Fox.md) |
| 409 | **Year of the Jellyfish** | `Hard` | `3 - 4 hrs` | 2020 | Hardened Linux CTF | 21.3 KB | [Year of the Jellyfish.md](./Year%20of%20the%20Jellyfish.md) |
| 410 | **Year of the Owl** | `Hard` | `2.5 - 3.5 hrs` | 2020 | Windows PrivEsc CTF | 32.5 KB | [Year of the Owl.md](./Year%20of%20the%20Owl.md) |
| 411 | **Year of the Pig** | `Hard` | `2.5 - 3.5 hrs` | 2020 | Web / Linux CTF | 16.1 KB | [Year of the Pig.md](./Year%20of%20the%20Pig.md) |
| 412 | **Year of the rabbit** | `Medium` | `1.5 hrs` | 2020 | Burp / Linux CTF | 4.0 KB | [Year of the rabbit.md](./Year%20of%20the%20rabbit.md) |
| 413 | **You're in a cave** | `Medium` | `1.5 hrs` | 2020 | Text Adventure CTF | 48.0 KB | [You're in a cave.md](./You%27re%20in%20a%20cave.md) |
| 414 | **Zeek Exercises** | `Medium` | `1.5 hrs` | 2022 | Zeek / Network DFIR | 13.9 KB | [Zeek Exercises.md](./Zeek%20Exercises.md) |
| 415 | **Zeek** | `Easy` | `1.5 hrs` | 2022 | Network Monitoring | 130.9 KB | [Zeek.md](./Zeek.md) |
| 416 | **Zeno** | `Medium` | `1.5 hrs` | 2021 | Linux CTF / Restaurant CMS | 16.8 KB | [Zeno.md](./Zeno.md) |
| 417 | **ZeroLogon** | `Medium` | `45 mins` | 2020 | CVE-2020-1472 | 39.6 KB | [ZeroLogon.md](./ZeroLogon.md) |
| 418 | **b3dr0ck** | `Medium` | `1.5 hrs` | 2021 | Linux / TLS Socket CTF | 26.1 KB | [b3dr0ck.md](./b3dr0ck.md) |
| 419 | **battery** | `Medium` | `1.5 hrs` | 2020 | Web / PHP / Linux CTF | 32.1 KB | [battery.md](./battery.md) |
| 420 | **biteme** | `Medium` | `1.5 hrs` | 2021 | Linux / PHP CTF | 23.1 KB | [biteme.md](./biteme.md) |
| 421 | **hackerNote** | `Medium` | `1.5 hrs` | 2021 | Web / SSTI / Linux | 31.3 KB | [hackerNote.md](./hackerNote.md) |
| 422 | **harder** | `Medium` | `1.5 hrs` | 2020 | Git / PHP / Linux CTF | 31.9 KB | [harder.md](./harder.md) |
| 423 | **iOS Forensics** | `Medium` | `1.5 hrs` | 2022 | Mobile DFIR | 26.1 KB | [iOS Forensics.md](./iOS%20Forensics.md) |
| 424 | **pyLon** | `Medium` | `1.5 hrs` | 2021 | Python / Linux CTF | 27.1 KB | [pyLon.md](./pyLon.md) |
| 425 | **ret2libc** | `Hard` | `2.5 - 3.5 hrs` | 2020 | Binary Exploitation / ROP | 45.7 KB | [ret2libc.md](./ret2libc.md) |
| 426 | **toc2** | `Medium` | `1.5 hrs` | 2021 | Race Condition (TOCTOU) | 15.2 KB | [toc2.md](./toc2.md) |
| 427 | **x86 Architecture Overview** | `Info` | `45 mins` | 2021 | Reverse Engineering | 18.4 KB | [x86 Architecture Overview.md](./x86%20Architecture%20Overview.md) |

---

### Notes & Methodology

- **Difficulty Criteria**: Reflects official TryHackMe / HackTheBox badges, required technical prerequisite knowledge, and degree of exploit chaining.

- **Length / Completion Time**: Estimated realistic completion duration for dedicated hands-on engagement (excluding machine queue times).

- **Release Timelines**: Based on room launch date on TryHackMe/HTB, target CVE disclosure dates, and terminal artifact timestamps.
