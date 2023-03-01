# Basic Static Analysis — Writeup

## Overview
### Basic Static Analysis — Writeup
### Basic Static Analysis — Writeup
----
Learn basic malware analysis techniques without running the malware.
---
### Introduction
In the previous rooms of this module, we learned about the basics of computer architecture and Assembly language. While those topics are essential building blocks to learning malware analysis, we will start analyzing malware starting from this room.
Before starting this room, it is recommended that you complete the following rooms.
-   [Intro to Malware Analysis](http://tryhackme.com/jr/intromalwareanalysis)
-   x86 Assembly Crash Course (coming soon!)
-   x86 Architecture Overview (coming soon!)
The first step in analyzing malware is generally to look at its properties without running it. This type of analysis is called static analysis because the malware is static and is not running. We will cover basic static analysis in this room. In particular, we will cover the following topics.
-   Lab setup for malware analysis
-   Searching for strings in a malware
-   Fingerprinting malware through hashes
-   Signature-based detection mechanisms
-   Extracting useful information from the PE header
So without further ado, let's move on to the next task to learn about setting up a malware analysis lab.
Answer the questions below
Complete the pre-requisite rooms.
Completed
### Lab Setup
Start Machine
### Basic precautions for malware analysis:
Before analyzing malware, one must understand that malware is often destructive. This means that when malware is being analyzed, there is a high chance of damaging the environment in which it is being analyzed. This damage can be permanent, and it might take more effort to get rid of this damage than the effort made to analyze the malware. Therefore, creating a lab setup that can withstand the destructive nature of malware is necessary.
A lab setup for malware analysis requires the ability to save the state of a machine (snapshot) and revert to that state whenever required. The machine is thus prepared with all the required tools installed, and its state is saved. After analyzing the malware in that machine, it is restored to its clean state with all the tools installed. This activity ensures that each malware is analyzed in an otherwise clean environment, and after analysis, the machine can be reverted without any sustained damage.
Virtual Machines provide an ideal medium for malware analysis. Some famous software used for creating and using Virtual Machines includes [Oracle VirtualBox](https://www.virtualbox.org/) and [VMWare Workstation](https://www.vmware.com/products/workstation-pro.html). These applications can create snapshots and revert to them whenever required, making them well-suited for our malware analysis pursuit. In short, the following steps portray the usage of Virtual Machines for malware analysis.
1.  Created a fresh Virtual Machine with a new OS install
2.  Set up the machine by installing all the required analysis tools in it
3.  Take a snapshot of the machine
4.  Copy/Download malware samples inside the VM and analyze it
5.  Revert the machine to the snapshot after the analysis completes
Following these steps ensures that your VM is not contaminated with remnants of previous malware samples when analyzing new malware. It also ensures that you don't have to install your tools again and again for each analysis. Selecting the tools to install in your malware analysis VM can also be hectic. One can use one of the freely available malware analysis VMs with pre-installed tools to ease this task. Let's review some common malware analysis VMs most popular among security researchers.
The FLARE VM is a Windows-based VM well-suited for malware analysis created by Mandiant (Previously FireEye). It contains some of the community's favorite malware analysis tools. Furthermore, it is also customizable, i.e., you can install any of your own tools to the VM. FLARE VM is compatible with Windows 7 and Windows 10. For a list of tools already installed in the VM and installation steps, you can visit the [GitHub page](https://github.com/mandiant/flare-vm) or the [Mandiant blog](https://www.mandiant.com/resources/blog/flare-vm-update) for the VM. Since it is a Windows-based VM, it can perform dynamic analysis of Windows-based malware.
An instance of FLARE VM is attached to this room for performing practical tasks. Please click the Start Machine button on the top-right corner of this task to start the machine before proceeding to the next task. The attached VM has a directory named mal on the Desktop, which contains malware samples that we would be analyzing for this room.
REMnux stands for Reverse Engineering Malware Linux. It is a Linux-based malware analysis distribution created by Lenny Zeltser in 2010. Later on, more people joined the team to improve upon the distribution. Like the FLARE VM, it includes some of the most popular reverse engineering and malware analysis tools pre-installed. It helps the analysts save time that would otherwise be spent in identifying, searching for, and installing the required tools. Details like installation and documentation can be found on [GitHub](https://github.com/REMnux) or the [website](https://remnux.org/) for distribution. Being a Linux-based distribution, it cannot be used to perform dynamic analysis of Windows-based malware. REMnux was previously used in the Intro to Malware Analysis room and will also be used in the upcoming rooms.
Please click the Start Machine button on the top-right corner of this task to start the machine before proceeding to the next task. The machine will start in a split-screen view. If the VM is not visible, use the blue Show Split View button at the top-right of the page. The attached VM has a directory named mal on the Desktop, which contains malware samples that we would be analyzing for this room. Alternatively, you might use the following information to log into the machine:
Machine IP: `MACHINE_IP`
Username: `Administrator`
Password: `letmein123!`
Answer the questions below
```scss
https://docs.remnux.org/install-distro/get-virtual-appliance

Reverse Engineering Malware Linux

I've downloaded it Remnux (just follow steps)

Username: `remnux` 
Password: `malware`

FLARE VM is a Windows-based VM (I don't have much space)
```
Start the attached VM before proceeding
Completed
### String search
In the [Intro to Malware Analysis](https://tryhackme.com/room/intromalwareanalysis) room, we identified that searching for strings is one of the first steps in malware analysis. A string search provides useful information to a malware analyst by identifying important pieces of strings present in a suspected malware sample. To learn a little more about strings, we can look at [this room](https://tryhackme.com/room/malstrings) dedicated to strings.
### How a string search works:
A string search looks at the binary data in a malware sample regardless of its file type and identifies sequences of ASCII or Unicode characters followed by a null character. Wherever it finds such a sequence, it reports that as a string. This might raise the question that not all sequences of binary data that looks like ASCII or Unicode characters will be actual strings, which is right. Many sequences of bytes can fulfill the criteria mentioned above but are not strings of useful value; rather, they might include memory addresses, assembly instructions, etc. Therefore, a string search leads to many False Positives (FPs). These FPs show up as garbage in the output of our string search and should be ignored. It is up to the analyst to identify the useful strings and ignore the rest.
### What to look for?
Since an analyst has to identify actual strings of interest and differentiate them from the garbage, it is good to know what to look for when performing a string search. Although a lot of useful information can be unearthed in a string search, the following artifacts can be used as Indicators of Compromise (IOCs) and prove more useful.
-   Windows Functions and APIs, like SetWindowsHook, CreateProcess, InternetOpen, etc. They provide information about the possible functionality of the malware
-   IP Addresses, URLs, or Domains can provide information about possible C2 communication. The Wannacry malware's killswitch domain was found using a string search
-   Miscellaneous strings such as Bitcoin addresses, text used for Message Boxes, etc. This information helps set the context for further malware analysis
### Basic String Search:
In the [Intro to Malware Analysis](https://tryhackme.com/room/intromalwareanalysis) room, we learned about the `strings` utility, which is pre-installed in Linux machines and can be used for a basic string search. Similarly, the FLARE VM comes with a Windows utility, `strings.exe`, that performs the same task. This Windows strings utility is part of the Sysinternals suite, a set of tools published by Microsoft to analyze different aspects of a Windows machine. Details about the strings utility can be found in [Microsoft Documentation](https://docs.microsoft.com/en-us/sysinternals/downloads/strings). The strings utility comes pre-installed in the FLARE VM attached to this room. The good thing about the command line strings utility is that it can dump strings to a file for further analysis. In the attached VM, executing the following command will perform a basic string search in a binary.
`C:\Users\Administrator\Desktop>strings <path to binary>`
Several other tools included in the FLARE VM can be used for string search. For example, CyberChef (Desktop>FLARE>Utilities>Cyberchef) has a recipe for basic string search as well. PEstudio (Desktop>FLARE>Utilities>pestudio) also provides a string search utility. PEstudio also provides some additional information about the strings, like, the encoding, size of the string, offset in the binary where the string was found, and a hint to guess what the string is related to. It also has a column for a blacklist, which matches the strings against some signatures.
The above screenshot from PEstudio shows strings found by PEstudio in a malware sample. This can be done by selecting strings in the left pane after loading the PE file in PEstudio. The blacklist here shows a bunch of Windows API calls, which PEstudio flags as potentially used in malicious processes. You can learn about these APIs using resources like [MalAPI](https://malapi.io/) or [MSDN](https://docs.microsoft.com/en-us/search/?scope=Desktop&terms=queryperformancecounter).
### Obfuscated strings:
Searching for strings often proves one of the most effective first steps in malware analysis. As seen in [the case of Wannacry](https://www.wired.com/2017/05/accidental-kill-switch-slowed-fridays-massive-ransomware-attack/), effective use of string search can often disrupt malware propagation and infection. The malware authors know this and don't want a simple string search to thwart their malicious activities. Therefore, they deploy techniques to obfuscate strings in their malware. Malware authors use several techniques to obfuscate the key parts of their code. These techniques often render a string search ineffective, i.e., we won't find much information when we search for strings.
Mandiant (then FireEye) launched FLOSS to solve this problem, short for **F**ireEye **L**abs **O**bfuscated **S**tring **S**olver. FLOSS uses several techniques to deobfuscate and extract strings that would not be otherwise found using a string search. The type of strings that FLOSS can extract and how it works can be found in [Mandiant's blog post](https://www.mandiant.com/resources/blog/automatically-extracting-obfuscated-strings).
To execute FLOSS, open a command prompt and navigate to the Desktop directory. From there, use the following command.
`C:\Users\Administrator\Desktop>floss -h`
This command will open the help page for FLOSS. We can use the following command to use FLOSS to search for obfuscated strings in a binary.
`C:\Users\Administrator\Desktop>floss --no-static-strings <path to binary>`
Please remember that the command might take some time to execute, and you might see what appear to be some error messages before the results are generated.
Answer the questions below
On the Desktop in the attached VM, there is a directory named 'mal' with malware samples 1 to 6. Use floss to identify obfuscated strings found in the samples named 2, 5, and 6. Which of these samples contains the string 'DbgView.exe'?
Use floss to extract obfuscated strings. Floss can be executed from cmd after navigating to the C:\Users\Administrator\Desktop
```text
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

FLARE Tue 02/14/2023 16:22:49.97
C:\Users\Administrator>cd C:\Users\Administrator\Desktop\mal

FLARE Tue 02/14/2023 16:23:00.08
C:\Users\Administrator\Desktop\mal>dir
 Volume in drive C has no label.
 Volume Serial Number is 0EBE-2DEE

 Directory of C:\Users\Administrator\Desktop\mal

09/13/2022  06:40 AM    <DIR>          .
09/13/2022  06:40 AM    <DIR>          ..
09/04/2022  05:54 AM           296,448 1
07/27/2021  07:50 PM            35,408 2
09/10/2022  10:17 PM           267,297 3
09/04/2022  05:54 AM         1,318,986 4
07/26/2021  06:43 PM           645,632 5
09/04/2022  05:55 AM           870,912 6
               6 File(s)      3,434,683 bytes
               2 Dir(s)  30,787,768,320 bytes free

FLARE Tue 02/14/2023 16:23:04.27
C:\Users\Administrator\Desktop\mal>

C:\Users\Administrator\Desktop\mal>floss --no-static-strings 2

FLOSS decoded 0 strings

FLOSS extracted 0 stackstrings

Finished execution after 0.015000 seconds

FLARE Tue 02/14/2023 16:25:31.54
C:\Users\Administrator\Desktop\mal>floss --no-static-strings 5

FLOSS decoded 0 strings

FLOSS extracted 0 stackstrings

Finished execution after 0.000000 seconds

FLARE Tue 02/14/2023 16:25:51.60
C:\Users\Administrator\Desktop\mal>floss --no-static-strings 6
WARNING:envi.codeflow:parseOpcode error at 0x1400596c8 (addCodeFlow(0x140058558)): InvalidInstruction("'c5eeffff440fb70233c041baffff0000' at 0x1400596c8L",)
WARNING:envi.codeflow:parseOpcode error at 0x14004edc2 (addCodeFlow(0x14004b0d4)): InvalidInstruction("'db75178b1509f30400488d0d2ca50300' at 0x14004edc2L",)
WARNING:envi.codeflow:parseOpcode error at 0x14004e645 (addCodeFlow(0x14004e5b0)): InvalidInstruction("'db75178b1586fa0400488d0df9ab0300' at 0x14004e645L",)

FLOSS decoded 1 strings
@@AD

FLOSS extracted 45 stackstrings
Dbgview.exe
Dbgview.exe
AVQZAWI
Dbgview.exe
Dbgview.exe
Dbgview.exe
Dbgview.exe
Dbgview.exe
Dbgview.exe
Dbgview.exe
Dbgview.exe
D$ H
Dbgview.exe
Dbgview.exe
L$ H
Dbgview.exe
Dbgview.exe
Dbgview.exe
Dbgview.exe
Dbgview.exe
Dbgview.exe
Dbgview.exe
A_A^
Dbgview.exe
Dbgview.exe
Dbgview.exe
Dbgview.exe
Dbgview.exe
Dbgview.exe
Dbgview.exe
112222I
Dbgview.exe
Dbgview.exe
Dbgview.exe
Dbgview.exe
Dbgview.exe
Dbgview.exe
Dbgview.exe
D$ H
@@AD
Dbgview.exe
Dbgview.exe
Dbgview.exe
Dbgview.exe
Dbgview.exe

Finished execution after 35.484000 seconds

FLARE Tue 02/14/2023 16:26:56.74
```
![[Pasted image 20230214193336.png]]
*6*
### Fingerprinting malware
Besides identifying files, hashes are also used to store passwords to authenticate users. In malware analysis, hash files can be used to identify unique malware, search for this malware in different malware repositories and databases, and as an Indicator of Compromise (IOC).
### Commonly used methods of calculating File hashes:
For identification of files, a hash of the complete file is taken. There are various methods to take the hash. The most commonly used methods are:
-   Md5sum
-   Sha1sum
-   Sha256sum
The first two types of hashes are now considered insecure or prone to collision attacks (when two or more inputs result in the same hash). Although a collision attack for these hash functions is not very probable, it is still possible. Therefore, sha256sum is currently considered the most secure method of calculating a file hash. In the attached VM, we can see that multiple utilities calculate file hashes for us.
### Finding Similar files using hashes:
Another scenario in which hash functions help a malware analyst is identifying similar files using hashes. We already established that even a slight change in the contents of a file would result in a different hash. However, some types of hashes can help identify the similarity among different files. Let's learn about some of these.
### Imphash:
The imphash stands for "import hash". Imports are functions that an executable file imports from other files or Dynamically Linked Libraries (DLLs). The imphash is a hash of the function calls/libraries that a malware sample imports and the order in which these libraries are present in the sample. This helps identify samples from the same threat groups or performing similar activities. More details on the Imphash can be found on Mandiant's blog [here](https://www.mandiant.com/resources/blog/tracking-malware-import-hashing).
We can use PEstudio to calculate the Imphash of a sample.
Any malware samples with the same imports in the same order will have the same imphash. This helps in identifying similar samples.
In the above screenshot from [Malware Bazaar](https://bazaar.abuse.ch/browse.php?search=imphash%3A756fdea446bc618b4804509775306c0d), all these samples have the same imphash. We can see that all of these samples are classified as the same malware family. We can see that their sha256 hash is vastly different and doesn't provide any information as to their similarity. However, the same imphash helps us identify that they might belong to the same family.
### Fuzzy hashes/SSDEEP:
Another way to identify similar malware is through fuzzy hashes. A fuzzy hash is a Context Triggered Piecewise Hash (CTPH). This hash is calculated by dividing a file into pieces and calculating the hashes of the different pieces. This method creates multiple inputs with similar sequences of bytes, even though the whole file might be different. More information on SSDEEP can be found on this [link](https://ssdeep-project.github.io/ssdeep/index.html).
Multiple utilities can be used in the attached VM to calculate ssdeep, like CyberChef. However, the ssdeep utility has been placed on the Desktop to make it easier. The following command shows the help menu of the utility.
Finding similar files using ssdeep
```shell-session
C:\Users\Administrator\Desktop>ssdeep-2.14.1\ssdeep.exe -h
ssdeep version 2.14.1 by Jesse Kornblum and the ssdeep Project
For copyright information, see man page or README.TXT.

Usage: ssdeep [-m file] [-k file] [-dpgvrsblcxa] [-t val] [-h|-V] [FILES]
-m - Match FILES against known hashes in file
-k - Match signatures in FILES against signatures in file
-d - Directory mode, compare all files in a directory
-p - Pretty matching mode. Similar to -d but includes all matches
-g - Cluster matches together
-v - Verbose mode. Displays filename as its being processed
-r - Recursive mode
-s - Silent mode; all errors are suppressed
-b - Uses only the bare name of files; all path information omitted
-l - Uses relative paths for filenames
-c - Prints output in CSV format
-x - Compare FILES as signature files
-a - Display all matches, regardless of score
-t - Only displays matches above the given threshold
-h - Display this help message
-V - Display version number and exit

FLARE Sun 09/18/2022 17:28:35.11
C:\Users\Administrator\Desktop>
```
Let's calculate the hashes of all the samples in the mal directory in the attached VM.
Calculating ssdeep
```shell-session
C:\Users\Administrator\Desktop>ssdeep-2.14.1\ssdeep.exe mal\*
ssdeep,1.1--blocksize:hash:hash,filename
3072:C3twbyJdvGwRCf/swDQheOAmN4hMRl37G:8EacOAmN6C,"C:\Users\Administrator\Desktop\mal\1"
768:fMjB/JpMfHDWqpuXDvod3UmQmv4acY2GS2C9xjwhU:UFQlpSDvoJrbvUfGS2q,"C:\Users\Administrator\Desktop\mal\2"
1536:C3tvICAqw8IKVn2wJk0c8PoYJvGwRCwAL6pILgl7vBIQtCnDkbZ3eOAmV2u4hnnM:C3twbyJdvGwRCf/swDQheOAmN4hM,"C:\Users\Administrator\Desktop\mal\3"
24576:u7DtlSDAlZvEFZhbS7buPPcedeHP5XLnkO3hGL8Siw9zVZprY8fWg5r11O:8OKVizL3cvtkO3hmVVZBYu5r1M,"C:\Users\Administrator\Desktop\mal\4"
12288:z+IIs67xrXWxgxMdplNGvIcGZwwDVHJXuDzKYzIE5P/XiS6lYSz8uahDtbNL6WTW:z+PsGlsFGgcQDJJQ,"C:\Users\Administrator\Desktop\mal\5"
24576:UCsTPcqE9S7tdODN+6ybJVCy2pvZHGOzPBjRj4AFsb:UCO7tsp+6ybJVChpRjvs,"C:\Users\Administrator\Desktop\mal\6"

FLARE Sun 09/18/2022 17:41:12.38
C:\Users\Administrator\Desktop>
```
We can try the other options shown in the help file per the requirement. When we have the ssdeep hashes, we can match these hashes together to identify similar files. This helps us identify similar files if we have a bulk of data. The documentation link provided above has very good examples of usage. The following terminal window shows one of the examples relevant to our use case to match files. For this, we can use the `-d` operator. The `-r` operator runs the ssdeep utility recursively, and the `-l` operator outputs relative paths of the files.
Finding matching files using ssdeep
```shell-session
C:\Users\Administrator\Desktop>ssdeep-2.14.1\ssdeep -l -r -d Incoming Outgoing Trash
Outgoing/Corporate Espionage/Our Budget.doc matches Incoming/Budget 2007.doc (99)
Outgoing/Personnel Mayhem/Your Buddy Makes More Than You.doc matches Incoming/Salaries.doc (45)
Trash/DO NOT DISTRIBUTE.doc matches Outgoing/Plan for Hostile Takeover.doc (88)

FLARE Sun 09/18/2022 17:41:12.38
C:\Users\Administrator\Desktop>
```
The results show files that match each other. The number in the bracket at the end is the percentage of matches among the files.
Answer the questions below
```text
mal 3
imphash,F397831B8900AFF7FBEF2FFDE97C2603

mal 1 same imphash

imphash,F397831B8900AFF7FBEF2FFDE97C2603

so same mal familiy

C:\Users\Administrator\Desktop>ssdeep-2.14.1\ssdeep.exe mal\*
ssdeep,1.1--blocksize:hash:hash,filename
3072:C3twbyJdvGwRCf/swDQheOAmN4hMRl37G:8EacOAmN6C,"C:\Users\Administrator\Desktop\mal\1"
768:fMjB/JpMfHDWqpuXDvod3UmQmv4acY2GS2C9xjwhU:UFQlpSDvoJrbvUfGS2q,"C:\Users\Administrator\Desktop\mal\2"
1536:C3tvICAqw8IKVn2wJk0c8PoYJvGwRCwAL6pILgl7vBIQtCnDkbZ3eOAmV2u4hnnM:C3twbyJdvGwRCf/swDQheOAmN4hM,"C:\Users\Administrator\Desktop\mal\3"
24576:u7DtlSDAlZvEFZhbS7buPPcedeHP5XLnkO3hGL8Siw9zVZprY8fWg5r11O:8OKVizL3cvtkO3hmVVZBYu5r1M,"C:\Users\Administrator\Desktop\mal\4"
12288:z+IIs67xrXWxgxMdplNGvIcGZwwDVHJXuDzKYzIE5P/XiS6lYSz8uahDtbNL6WTW:z+PsGlsFGgcQDJJQ,"C:\Users\Administrator\Desktop\mal\5"
24576:UCsTPcqE9S7tdODN+6ybJVCy2pvZHGOzPBjRj4AFsb:UCO7tsp+6ybJVChpRjvs,"C:\Users\Administrator\Desktop\mal\6"
3::,"C:\Users\Administrator\Desktop\mal\cd"
3::,"C:\Users\Administrator\Desktop\mal\dir"

FLARE Tue 02/14/2023 16:48:15.78

C:\Users\Administrator\Desktop>ssdeep-2.14.1\ssdeep.exe -l -r -d mal\*
mal\3 matches mal\1 (93)
mal\dir matches mal\cd (100)

FLARE Tue 02/14/2023 16:49:15.63
```
![[Pasted image 20230214194503.png]]
In the samples located at Desktop\mal\ directory in the attached VM, which of the samples has the same imphash as file 3?
*1*
Using the ssdeep utility, what is the percentage match of the above-mentioned files?
*93*
### Signature-based detection
In the previous task, we learned how hashes could identify identical files. We also found out that hashes can be changed by changing even a single byte of data in a file and how specific hashes like imphash and ssdeep help us identify file similarities. While using imphash or ssdeep provides a way to identify if some files are similar, sometimes we just need to identify if a file contains the information of interest. Hashes are not the ideal tool to perform this task.
Signatures are a way to identify if a particular file has a particular type of content. We can consider a signature as a pattern that might be found inside a file. This pattern is often a sequence of bytes in a file, with or without any context regarding where it is found. Security researchers often use signatures to identify patterns in a file, identify if a file is malicious, and identify suspected behavior and malware family.
### Yara rules:
Yara rules are a type of signature-based rule. It is famously called a pattern-matching swiss army knife for malware researchers. Yara can identify information based on binary and textual patterns, such as hexadecimal and strings contained within a file. TryHackMe has a [dedicated room](https://tryhackme.com/room/yara) for Yara rules if it interests you.
The security community publishes a [repository](https://github.com/Yara-Rules/rules) of open-source Yara rules that we can use as per our needs. When analyzing malware, we can use this repository to dig into the community's collective wisdom. However, while using these rules, please keep in mind that some might depend on context. Some others might just be used for the identification of patterns that can be non-malicious as well. Hence, just because a rule hits doesn't mean the file is malicious. For a better understanding, please read the documentation for the particular rule to identify the use case where it will be applicable in the best possible manner.

## Enumeration
Besides the open-source signatures, Antivirus companies spend lots of resources to create proprietary signatures. The advantage of these proprietary signatures is that since they have to be sold commercially, there are lesser chances of False Positives (FPs, when a signature hits a non-malicious file). However, this might lead to a few False Negatives (FNs, when a malicious file does not hit any signature).
Antivirus scanning helps identify if a file is malicious with high confidence. Antivirus software will often mention the signature that the file has hit, which might hint at the file's functionality. However, we must note that despite their best efforts, every AV product in the market has some FPs and some FNs. Therefore, when analyzing malware, it is prudent to get a verdict from multiple products. The [Virustotal](https://www.virustotal.com/gui/home/upload) website makes this task easier for us, where we can find the verdict about a file from 60+ AV vendors, apart from some very useful information. We also touched upon this topic in our Intro to Malware Analysis room. Please remember, if you are analyzing a sensitive file, it is best practice to search for its hash on Virustotal or other scanning websites instead of uploading the file itself. This is done to avoid leaking sensitive information on the internet and letting a sophisticated attacker know that you are analyzing their malware.
Since we have covered Yara rules in detail in the Yara room and Virustotal scanning in the Intro to malware analysis room, we will not cover them again here. However, the FLARE VM has another very cool tool that can be used for signature scanning.
### Capa:
Capa is another open-source tool created by Mandiant. This tool helps identify the capabilities found in a PE file. Capa reads the files and tries to identify the behavior of the file based on signatures such as imports, strings, mutexes, and other artifacts present in the file. For further detail into the background of Capa, we can visit its [Github page](https://github.com/mandiant/capa) or Mandiant's [blog post](https://www.mandiant.com/resources/blog/capa-automatically-identify-malware-capabilities) introducing Capa.
Using Capa is simple. On the command prompt, we just point capa to the file we want to run it against.
`C:\Users\Administrator\Desktop>capa mal.exe`
The `-h` operator shows detailed options.
Capa
```shell-session
C:\Users\Administrator\Desktop>capa -h
usage: capa.exe [-h] [--version] [-v] [-vv] [-d] [-q] [--color {auto,always,never}] [-f {auto,pe,sc32,sc64,freeze}] [-b {vivisect,smda}] [-r RULES] [-t TAG] [-j] sample

The FLARE team's open-source tool to identify capabilities in executable files.

positional arguments:
  sample                path to sample to analyze

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v, --verbose         enable verbose result document (no effect with --json)
  -vv, --vverbose       enable very verbose result document (no effect with --json)
