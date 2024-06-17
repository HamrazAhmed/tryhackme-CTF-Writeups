---
Learn how to break signatures and evade common AV, using modern tool-agnostic approaches.
---

# Signature Evasion — Writeup

## Overview
### Signature Evasion — Writeup
### Signature Evasion — Writeup
![](https://tryhackme-images.s3.amazonaws.com/room-icons/a4e6685f4861d637e699b729d04f5b66.png)
### Introduction
An adversary may struggle to overcome specific detections when facing an advanced anti-virus engine or EDR (Endpoint Detection & Response) solution. Even after employing some of the most common obfuscation or evasion techniques discussed in Obfuscation Principles, signatures in a malicious file may still be present.
Decorative image of a toolbox
To combat persistent signatures, adversaries can observe each individually and address them as needed.
In this room, we will understand what signatures are and how to find them, then attempt to break them following an agnostic thought process. To dive deeper and combat heuristic signatures, we will also discuss more advanced code concepts and “malware best practices.”
Learning Objectives
Understand the origins of signatures and how to observe/detect them in malicious code
Implement documented obfuscation methodology to break signatures
Leverage non-obfuscation-based techniques to break non-function oriented signatures.
This room is a successor to Obfuscation Principles; we highly recommend completing it before this room if you have not already.
Before beginning this room, familiarize yourself with basic programming logic and syntax. Knowledge of C and PowerShell is recommended but not required.
We have provided a base Windows machine with the files needed to complete this room. You can access the machine in-browser or through RDP using the credentials below.
Machine IP: MACHINE_IP             Username: Student             Password: TryHackMe!
This is going to be a lot of information. Please locate your nearest hammer and fire extinguisher.
### Signature Identification
Before jumping into breaking signatures, we need to understand and identify what we are looking for. As covered in Introduction to Anti-Virus, signatures are used by anti-virus engines to track and identify possible suspicious and/or malicious programs. In this task, we will observe how we can manually identify an exact byte where a signature starts.
When identifying signatures, whether manually or automated, we must employ an iterative process to determine what byte a signature starts at. By recursively splitting a compiled binary in half and testing it, we can get a rough estimate of a byte-range to investigate further.
We can use the native utilities head, dd, or split to split a compiled binary. In the below command prompt, we will walk through using head to find the first signature present in a msfvenom binary.
Once split, move the binary from your development environment to a machine with the anti-virus engine you would like to test on. If an alert appears, move to the lower half of the split binary and split it again. If an alert does not appear, move to the upper half of the split binary and split it again. Continue this pattern until you cannot determine where to go; this will typically occur around the kilobyte range.
Once you have reached the point at which you no longer accurately split the binary, you can use a hex editor to view the end of the binary where the signature is present.
0000C2E0  43 68 6E E9 0A 00 00 00 0C 4D 1A 8E 04 3A E9 89  Chné.....M.Ž.:é‰
0000C2F0  67 6F BE 46 01 00 00 6A 40 90 68 00 10 00 00 E9  go¾F...j@.h....é
0000C300  0A 00 00 00 53 DF A1 7F 64 ED 40 73 4A 64 56 90  ....Sß¡.dí@sJdV.
0000C310  6A 00 68 58 A4 53 E5 E9 08 00 00 00 15 0D 69 B6  j.hX¤Såé......i¶
0000C320  F4 AB 1B 73 FF D5 E9 0A 00 00 00 7D 43 00 40 DB  ô«.sÿÕé....}C.@Û
0000C330  43 8B AC 55 82 89 C3 90 E9 08 00 00 00 E4 95 8E  C‹¬U‚‰Ã.é....ä•Ž
0000C340  2C 06 AC 29 A3 89 C7 90 E9 0B 00 00 00 0B 32 AC  ,.¬)£‰Ç.é.....2¬
We have the location of a signature; how human-readable it is will be determined by the tool itself and the compilation method.
Now… no one wants to spend hours going back and forth trying to track down bad bytes; let’s automate it! In the next task, we will look at a few FOSS (Free and Open-Source Software) solutions to aid us in identifying signatures in compiled code.
Using the knowledge gained throughout this task, split the binary found in C:\Users\Student\Desktop\Binaries\shell.exe using a native utility discussed in this task. Recursively determine if the split binary is detected until you have obtained the nearest kilobyte of the first signature.
Move the binary to a different folder without an exclusion to test against Defender
*No answer needed*
To the nearest kibibyte, what is the first detected byte?
Un kibibyte (KiB) es una unidad de almacenaje de data que equivale a 2 a la 10 potencia, o 1024 bytes. Un kilobyte se puede estimar que es 10^3 o 1000 bytes
*51000* (rounding 5048 found in next session)
### Automating Signature Identification
The process shown in the previous task can be quite arduous. To speed it up, we can automate it using scripts to split bytes over an interval for us. [Find-AVSignature](https://github.com/PowerShellMafia/PowerSploit/blob/master/AntivirusBypass/Find-AVSignature.ps1) will split a provided range of bytes through a given interval.
```text
Find-AVSignature
```
```text
PS C:\> . .\FInd-AVSignature.ps1
```
```text
PS C:\> Find-AVSignature

cmdlet Find-AVSignature at command pipeline position 1
Supply values for the following parameters:
StartByte: 0
EndByte: max
Interval: 1000

Do you want to continue?
This script will result in 1 binaries being written to "C:\Users\TryHackMe"!
[Y] Yes  [N] No  [S] Suspend  [?] Help (default is "Y"): y
```
This script relieves a lot of the manual work, but still has several limitations. Although it requires less interaction than the previous task, it still requires an appropriate interval to be set to function properly. This script will also only observe strings of the binary when dropped to disk rather than scanning using the full functionality of the anti-virus engine.
To solve this problem we can use other FOSS (Free and Open-Source Software) tools that leverage the engines themselves to scan the file, including [DefenderCheck](https://github.com/matterpreter/DefenderCheck), [ThreatCheck](https://github.com/rasta-mouse/ThreatCheck), and [AMSITrigger](https://github.com/RythmStick/AMSITrigger). In this task, we will primarily focus on ThreatCheck and briefly mention the uses of AMSITrigger at the end.
ThreatCheck
ThreatCheck is a fork of DefenderCheck and is arguably the most widely used/reliable of the three. To identify possible signatures, ThreatCheck leverages several anti-virus engines against split compiled binaries and reports where it believes bad bytes are present.
ThreatCheck does not provide a pre-compiled release to the public. For ease of use we have already compiled the tool for you; it can be found in C:\Users\Administrator\Desktop\Toolsof the attached machine.
Below is the basic syntax usage of ThreatCheck.
```text
hreatCheck Help Menu
```
```text
C:\>ThreatCheck.exe --help
  -e, --engine    (Default: Defender) Scanning engine. Options: Defender, AMSI
  -f, --file      Analyze a file on disk
  -u, --url       Analyze a file from a URL
  --help          Display this help screen.
  --version       Display version information.
```
For our uses we only need to supply a file and optionally an engine; however, we will primarily want to use AMSITrigger when dealing with AMSI (Anti-Malware Scan Interface), as we will discuss later in this task.
```text
ThreatCheck
```
```text
C:\>ThreatCheck.exe -f Downloads\Grunt.bin -e AMSI
	[+] Target file size: 31744 bytes
	[+] Analyzing...
	[!] Identified end of bad bytes at offset 0x6D7A
	00000000   65 00 22 00 3A 00 22 00  7B 00 32 00 7D 00 22 00   e·"·:·"·{·2·}·"·
	00000010   2C 00 22 00 74 00 6F 00  6B 00 65 00 6E 00 22 00   ,·"·t·o·k·e·n·"·
	00000020   3A 00 7B 00 33 00 7D 00  7D 00 7D 00 00 43 7B 00   :·{·3·}·}·}··C{·
	00000030   7B 00 22 00 73 00 74 00  61 00 74 00 75 00 73 00   {·"·s·t·a·t·u·s·
	00000040   22 00 3A 00 22 00 7B 00  30 00 7D 00 22 00 2C 00   "·:·"·{·0·}·"·,·
	00000050   22 00 6F 00 75 00 74 00  70 00 75 00 74 00 22 00   "·o·u·t·p·u·t·"·
	00000060   3A 00 22 00 7B 00 31 00  7D 00 22 00 7D 00 7D 00   :·"·{·1·}·"·}·}·
	00000070   00 80 B3 7B 00 7B 00 22  00 47 00 55 00 49 00 44   ·?³{·{·"·G·U·I·D
	00000080   00 22 00 3A 00 22 00 7B  00 30 00 7D 00 22 00 2C   ·"·:·"·{·0·}·"·,
	00000090   00 22 00 54 00 79 00 70  00 65 00 22 00 3A 00 7B   ·"·T·y·p·e·"·:·{
	000000A0   00 31 00 7D 00 2C 00 22  00 4D 00 65 00 74 00 61   ·1·}·,·"·M·e·t·a
	000000B0   00 22 00 3A 00 22 00 7B  00 32 00 7D 00 22 00 2C   ·"·:·"·{·2·}·"·,
	000000C0   00 22 00 49 00 56 00 22  00 3A 00 22 00 7B 00 33   ·"·I·V·"·:·"·{·3
	000000D0   00 7D 00 22 00 2C 00 22  00 45 00 6E 00 63 00 72   ·}·"·,·"·E·n·c·r
	000000E0   00 79 00 70 00 74 00 65  00 64 00 4D 00 65 00 73   ·y·p·t·e·d·M·e·s
	000000F0   00 73 00 61 00 67 00 65  00 22 00 3A 00 22 00 7B   ·s·a·g·e·"·:·"·{
```
It’s that simple! No other configuration or syntax is required and we can get straight to modifying our tooling. To efficiently use this tool we can identify any bad bytes that are first discovered then recursively break them and run the tool again until no signatures are identified.
Note: There may be instances of false positives, in which the tool will report no bad bytes. This will require your own intuition to observe and solve; however, we will discuss this further in task 4.
AMSITrigger
As covered in Runtime Detection Evasion,AMSI leverages the runtime, making signatures harder to identify and resolve. ThreatCheck also does not support certain file types such as PowerShell that AMSITrigger does.
AMSITrigger will leverage the AMSI engine and scan functions against a provided PowerShell script and report any specific sections of code it believes need to be alerted on.
AMSITrigger does provide a pre-compiled release on their GitHub and can also be found on the Desktop of the attached machine.
Below is the syntax usage of AMSITrigger
```text
AMSITrigger Help Menu
```
```text
C:\>amsitrigger.exe --help
	-i, --inputfile=VALUE       Powershell filename
	-u, --url=VALUE             URL eg. <https://10.1.1.1/Invoke-NinjaCopy.ps1>
	-f, --format=VALUE          Output Format:
	                              1 - Only show Triggers
	                              2 - Show Triggers with Line numbers
	                              3 - Show Triggers inline with code
	                              4 - Show AMSI calls (xmas tree mode)
	-d, --debug                 Show Debug Info
	-m, --maxsiglength=VALUE    Maximum signature Length to cater for,
	                              default=2048
	-c, --chunksize=VALUE       Chunk size to send to AMSIScanBuffer,
	                              default=4096
	-h, -?, --help              Show Help
```
For our uses we only need to supply a file and the preferred format to report signatures.
![[Pasted image 20220917120127.png]]
In the next task we will discuss how you can use the information gathered from these tools to break signatures.
Using the knowledge gained throughout this task, identify bad bytes found in C:\Users\Student\Desktop\Binaries\shell.exe using ThreatCheck and the Defender engine. ThreatCheck may take up to 15 minutes to find the offset, in this case you can leave it running in the background, continue with the next task, and come back when it finishes.
```text
C:\Users\Student\Desktop\Tools>.\ThreatCheck.exe -f C:\Users\Student\Desktop\Binaries\shell.exe -e Defender
[*] C:\Temp doesn't exist. Creating it...
[+] Target file size: 73802 bytes
[+] Analyzing...
[*] Testing 36901 bytes
[*] No threat found, increasing size
[*] Testing 55351 bytes
[*] Threat found, splitting
[*] Testing 46126 bytes
[*] No threat found, increasing size
[*] Testing 59964 bytes
[*] Threat found, splitting
[*] Testing 53045 bytes

Unhandled Exception: System.IO.IOException: The process cannot access the file 'C:\Temp\file.exe' because it is being used by another process.
   at System.IO.__Error.WinIOError(Int32 errorCode, String maybeFullPath)
   at System.IO.FileStream.Init(String path, FileMode mode, FileAccess access, Int32 rights, Boolean useRights, FileShare share, Int32 bufferSize, FileOptions options, SECURITY_ATTRIBUTES secAttrs, String msgPath, Boolean bFromProxy, Boolean useLongPath, Boolean checkHost)
   at System.IO.FileStream..ctor(String path, FileMode mode, FileAccess access, FileShare share, Int32 bufferSize, FileOptions options, String msgPath, Boolean bFromProxy, Boolean useLongPath, Boolean checkHost)
   at System.IO.File.InternalWriteAllBytes(String path, Byte[] bytes, Boolean checkHost)
   at ThreatCheck.Defender.AnalyzeFile() in C:\Users\Dominic Cunningham\Downloads\ThreatCheck-master\ThreatCheck-master\ThreatCheck\ThreatCheck\Defender\Defender.cs:line 55
   at ThreatCheck.Program.ScanWithDefender(Byte[] file) in C:\Users\Dominic Cunningham\Downloads\ThreatCheck-master\ThreatCheck-master\ThreatCheck\ThreatCheck\Program.cs:line 114
   at ThreatCheck.Program.RunOptions(Options opts) in C:\Users\Dominic Cunningham\Downloads\ThreatCheck-master\ThreatCheck-master\ThreatCheck\ThreatCheck\Program.cs:line 85
   at CommandLine.ParserResultExtensions.WithParsed[T](ParserResult`1 result, Action`1 action)
   at ThreatCheck.Program.Main(String[] args) in C:\Users\Dominic Cunningham\Downloads\ThreatCheck-master\ThreatCheck-master\ThreatCheck\ThreatCheck\Program.cs:line 35

C:\Users\Student\Desktop\Tools>.\ThreatCheck.exe -f C:\Users\Student\Desktop\Binaries\shell.exe -e AMSI
[+] Target file size: 73802 bytes
[+] Analyzing...
[*] Testing 36901 bytes
[*] No threat found, increasing size
[*] Testing 55351 bytes
[*] Threat found, splitting
[*] Testing 46126 bytes
[*] No threat found, increasing size
[*] Testing 59964 bytes
[*] Threat found, splitting
[*] Testing 53045 bytes
[*] Threat found, splitting
[*] Testing 49585 bytes
[*] No threat found, increasing size
[*] Testing 61693 bytes
[*] Threat found, splitting
[*] Testing 55639 bytes
[*] Threat found, splitting
[*] Testing 52612 bytes
[*] Threat found, splitting
[*] Testing 51098 bytes
[*] Threat found, splitting
[*] Testing 50341 bytes
[*] No threat found, increasing size
[*] Testing 62071 bytes
[*] Threat found, splitting
[*] Testing 56206 bytes
[*] Threat found, splitting
[*] Testing 53273 bytes
[*] Threat found, splitting
[*] Testing 51807 bytes
[*] Threat found, splitting
[*] Testing 51074 bytes
[*] Threat found, splitting
[*] Testing 50707 bytes
[*] Threat found, splitting
[*] Testing 50524 bytes
[*] Threat found, splitting
[*] Testing 50432 bytes
[*] No threat found, increasing size
[*] Testing 62117 bytes
[*] Threat found, splitting
[*] Testing 56274 bytes
[*] Threat found, splitting
[*] Testing 53353 bytes
[*] Threat found, splitting
[*] Testing 51892 bytes
[*] Threat found, splitting
[*] Testing 51162 bytes
[*] Threat found, splitting
[*] Testing 50797 bytes
[*] Threat found, splitting
[*] Testing 50614 bytes
[*] Threat found, splitting
[*] Testing 50523 bytes
[*] Threat found, splitting
[*] Testing 50477 bytes
[*] No threat found, increasing size
[*] Testing 62139 bytes
[*] Threat found, splitting
[*] Testing 56308 bytes
[*] Threat found, splitting
[*] Testing 53392 bytes
[*] Threat found, splitting
[*] Testing 51934 bytes
[*] Threat found, splitting
[*] Testing 51205 bytes
[*] Threat found, splitting
[*] Testing 50841 bytes
[*] Threat found, splitting
[*] Testing 50659 bytes
[*] Threat found, splitting
[*] Testing 50568 bytes
[*] Threat found, splitting
[*] Testing 50522 bytes
[*] Threat found, splitting
[*] Testing 50499 bytes
[*] Threat found, splitting
[*] Testing 50488 bytes
[*] No threat found, increasing size
[*] Testing 62145 bytes
[*] Threat found, splitting
[*] Testing 56316 bytes
[*] Threat found, splitting
[*] Testing 53402 bytes
[*] Threat found, splitting
[*] Testing 51945 bytes
