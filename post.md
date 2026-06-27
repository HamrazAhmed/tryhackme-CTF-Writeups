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
