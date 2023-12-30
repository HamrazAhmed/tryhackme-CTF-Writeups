---
A revitalised, hands-on showcase involving analysing malicious macro's, PDF's and Memory forensics of a victim of Jigsaw Ransomware; all done using the Linux-based REMnux toolset apart of my Malware Analysis series
---

# MAL REMnux The Redux — Writeup

## Overview
### MAL REMnux The Redux — Writeup
### MAL REMnux The Redux — Writeup
### 1. Introduction
![](https://remnux.org/img/remnux-logo.png)
Welcome to the redux of REMnux.
Since the release of the previous REMnux room, REMnux has had substantial changes, rendering the previous room outdated and impossible to complete.
I have taken the opportunity to recreate the room covering REMnux from scratch, taking a very different approach to ensure you get to use all the facilities that make REMnux unique.
How Have I Designed This Room Differently?
I've now re-designed the content for this room to get you as hands-on with REMnux and its tools as possible...gone are the days of reading cheatsheets for tasks; it's time for you to get stuck in and see what REMnux is really about. This room isn't designed with point-farming in mind, instead, I hope to give you enough guidance throughout the room that results in you developing a curiosity in exploring the topics & resources I introduce you to in your own time.
You will be doing the following:
Identifying and analysing malicious payloads of various formats embedded in PDF's, EXE's and Microsoft Office Macros (the most common method that malware developers use to spread malware today)
Learning how to identify obfuscated code and packed files - and in turn - analyse these.
Analysing the memory dump of a PC that became infected with the Jigsaw ransomware in the real-world using Volatility.
I have attached some useful material about some of the topics covered in the room, alongside some cheatsheets and related articles that you can browse at your leisure at the end of the room.
As always, feedback of any sort is always appreciated. I hope that recreating the room in a completely different direction is well received and proves to be worth the wait. ~CMNatic
I'm all buckled up and ready to get started.
*No answer needed*
### 2. Deploy
If you're using the machine in-browser, you can skip this task. If you want to manually SSH into the machine, read the following:
﻿Ensuring you are connected to the TryHackMe Network via OpenVPN, deploy the instance using the "Deploy" button and log in to your instance via SSH (on the standard port of 22). The necessary information to do is displayed below:
IP Address: MACHINE_IP
Username: remnux
Password: malware
I've deployed my instance
*No answer needed*
### 3. Analysing Malicious PDF's
﻿A Blast From the Past
We're back at this old chestnut, analysing malicious PDF files. In the previous room, you were analysing a PDF file for potential javascript code. PDF's are capable of containing many more types of code that can be executed without the user's knowledge. This includes:
Javascript
Python
Executables
Powershell Shellcode
Not only will this task be covering Javascript embeds (like we did previously), but also analysing embedded executables.
Looking for Embedded Javascript
We previously discussed how easily javascript can be embedded into a PDF file, whereupon opening is executed unbeknownst to the user. Javascript, much like other languages that we come on to discover in Task 4, provide a great way of creating a foothold, where additional malware can be downloaded and executed.
![](https://i.imgur.com/16r4ZtR.png)
Looks like the Cooctus Clan just wanted to say hey - it's a good thing that they're nice people!
Practical
We'll be using peepdf to begin a precursory analysis of a PDF file to determine the presence of Javascript. If there is, we will extract this Javascript code (without executing it) for our inspection.
We can simply do `peepdf demo_notsuspicious.pdf`:
![](https://i.imgur.com/yBhDeYi.png)
Note the output confirming that there's Javascript present, but also how it is executed? OpenAction will execute the code when the PDF is launched.
To extract this Javascript, we can use peepdf's "extract" module. This requires a few steps to set up but is fairly trivial.
The following command will create a script file for peepdf to use:
`echo 'extract js > javascript-from-demo_notsuspicious.pdf' > extracted_javascript.txt`
![](https://i.imgur.com/hYUwXuu.png)
The script will extract all javascript via extract js and pipe > the contents into "javascript-from-demo_notsuspicious.pdf"
We now need to tell peepdf the name of the script (extracted_javascript.txt) and the PDF file that we want to extract from (demo_notsuspicious.pdf):
2. peepdf -s extracted_javascript.txt demo_notsuspicious.pdf
Remembering that the Javascript will output into a file called "javascript-from-demo_nonsuspicious.pdf" because of our script.
To recap: "extracted_javascript.txt" (highlighted in red) is our script, where "demo_notsuspicious.pdf" (highlighted in green) is the original PDF file that we think is malicious.
![](https://i.imgur.com/0q0dt9I.png)
You will see an output, in this case, a file named "javascript-from-demo_notsuspicious" (highlighted in yellow). This file now contains our extracted Javascript, we can simply cat this to see the contents.
![](https://i.imgur.com/zSLNeKV.png)
As it turns out, the PDF file we have analysed contains the javascript code of app.alert("All your Cooctus are belong to us!")
Practical
We have used peepdf to:
1. Look for the presence of Javascript
2. Extract any contained Javascript for us to read without it being executed.
![](https://i.imgur.com/gI35CYV.png)
The commands to do so have been used above, you may have to implement them differently, proceed to answer questions 1 - 4 before moving onto the next section.
Executables
Of course not only can Javascript be embedded, by executables can be very much too.
The "advert.pdf" actually has an embedded executable. Looking at the extracted Javascript, we can see the following Javascript snippet:
![](https://i.imgur.com/HkaEbdF.png)
This tells us that when the PDF is opened, the user will be asked to save an attachment:
![](https://i.imgur.com/2ABomDi.png)
Although PDF attachments can be ZIP files or images, in this case, it is another PDF...Or is it? Well, let's save the file and see what happens. Uh oh...At least that we get a warning that something is trying to execute, but hey, Karen from HR wouldn't send you a dodgy email, right? It's probably a false alarm.
![](https://i.imgur.com/daoeGoL.png)
Ah...Well, turns out it was. We just got a reverse shell from the Windows PC to my attack machine.
![](https://i.imgur.com/o9mP0CA.png)
It's now obvious (albeit too late for them) that the "pdf" that gets saved isn't a PDF. Let's open it up in a hex editor.
![](https://i.imgur.com/CSypGSC.png)
Well well well, looks like we have an executable. Let's investigate further by looking at the strings.
![](https://i.imgur.com/lVmoupA.png)
It looks like we have our attacker's IP and port!
![](https://i.imgur.com/wthxQE3.png)
```text
remnux@thm-remnux:~/Tasks/3$ peepdf notsuspicious.pdf 
Warning: PyV8 is not installed!!

File: notsuspicious.pdf
MD5: 2992490eb3c13d8006e8e17315a9190e
SHA1: 75884015d6d984a4fcde046159f4c8f9857500ee
SHA256: 83fefd2512591b8d06cda47d56650f9cbb75f2e8dbe0ab4186bf4c0483ef468a
Size: 28891 bytes
Version: 1.7
Binary: True
Linearized: False
Encrypted: False
Updates: 0
Objects: 18
Streams: 3
URIs: 0
Comments: 0
Errors: 0

Version 0:
        Catalog: 1
        Info: 7
        Objects (18): [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        Streams (3): [4, 15, 18]
                Encoded (2): [15, 18]
        Objects with JS code (1): [6]
        Suspicious elements:
                /OpenAction (1): [1]
                /JS (1): [6]
                /JavaScript (1): [6]

remnux@thm-remnux:~/Tasks/3$ peepdf advert.pdf 
Warning: PyV8 is not installed!!

File: advert.pdf
MD5: 1b79db939b1a77a2f14030f9fd165645
SHA1: e760b618943fe8399ac1af032621b6e7b327a772
SHA256: 09bb03e57d14961e522446e1e81184ca0b4e4278f080979d80ef20dacbbe50b7
Size: 74870 bytes
Version: 1.7
Binary: True
Linearized: False
Encrypted: False
Updates: 2
Objects: 29
Streams: 6
URIs: 0
Comments: 0
Errors: 1

Version 0:
        Catalog: 1
        Info: 9
        Objects (22): [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
        Compressed objects (7): [10, 11, 12, 13, 14, 15, 16]
        Streams (5): [4, 17, 19, 20, 22]
                Xref streams (1): [22]
                Object streams (1): [17]
                Encoded (4): [4, 17, 19, 22]
        Suspicious elements:
                /Names (1): [13]

Version 1:
        Catalog: 1
        Info: 9
        Objects (0): []
        Streams (0): []

Version 2:
        Catalog: 1
        Info: 9
        Objects (7): [1, 3, 24, 25, 26, 27, 28]
        Streams (1): [26]
                Encoded (1): [26]
        Objects with JS code (1): [27]
        Suspicious elements:
                /OpenAction (1): [1]
                /Names (2): [24, 1]
                /AA (1): [3]
                /JS (1): [27]
                /Launch (1): [28]
                /JavaScript (1): [27]

remnux@thm-remnux:~/Tasks/3$ ls
advert.pdf  notsuspicious.pdf
remnux@thm-remnux:~/Tasks/3$ echo 'extract js > javascript-from-notsuspicious.pdf' > extracted_javascript.txt
remnux@thm-remnux:~/Tasks/3$ cat extracted_javascript.txt 
extract js > javascript-from-notsuspicious.pdf
remnux@thm-remnux:~/Tasks/3$ peepdf -s extracted_javascript.txt notsuspicious.pdf
remnux@thm-remnux:~/Tasks/3$ ls
advert.pdf                javascript-from-notsuspicious.pdf
extracted_javascript.txt  notsuspicious.pdf
remnux@thm-remnux:~/Tasks/3$ cat javascript-from-notsuspicious.pdf 
// peepdf comment: Javascript code located in object 6 (version 0)

app.alert("THM{Luckily_This_Isn't_Harmful}");remnux@thm-remnux:~/Tasks/3$ 

remnux@thm-remnux:~/Tasks/3$ ls
advert.pdf                javascript-from-notsuspicious.pdf
extracted_javascript.txt  notsuspicious.pdf
remnux@thm-remnux:~/Tasks/3$ echo 'extract js > javascript-from-advert.pdf' > extracted_javascript2.txt
remnux@thm-remnux:~/Tasks/3$ ls
advert.pdf                 javascript-from-notsuspicious.pdf
extracted_javascript2.txt  notsuspicious.pdf
extracted_javascript.txt
remnux@thm-remnux:~/Tasks/3$ cat extracted_javascript2.txt 
extract js > javascript-from-advert.pdf
remnux@thm-remnux:~/Tasks/3$ peepdf -s extracted_javascript2.txt advert.pdf
remnux@thm-remnux:~/Tasks/3$ ls
advert.pdf                 javascript-from-advert.pdf
extracted_javascript2.txt  javascript-from-notsuspicious.pdf
extracted_javascript.txt   notsuspicious.pdf
remnux@thm-remnux:~/Tasks/3$ cat javascript-from-advert.pdf 
// peepdf comment: Javascript code located in object 27 (version 2)

this.exportDataObject({
    cName: "notsuspicious",
    nLaunch: 0
});remnux@thm-remnux:~/Tasks/3$
```
How many types of categories of "Suspicious elements" are there in "notsuspicious.pdf"
*3*
Use peepdf to extract the javascript from "notsuspicious.pdf". What is the flag?
How many types of categories of "Suspicious elements" are there in "advert.pdf"
*6*
Now use peepdf to extract the javascript from "advert.pdf". What is the value of "cName"?
*notsuspicious*
### 4. Analysing Malicious Microsoft Office Macros
The Change in Focus from APT's
Malware infection via malicious macros (or scripts within Microsoft Office products such as Word and Excel) are some of the most successful attacks to date.
For example, current APT campaigns such as Emotet, QuickBot infect users by sending seemingly legitimate documents attached to emails i.e. an invoice for business. However, once opened, execute malicious code without the user knowing. This malicious code is often used in what's known as a "dropper attack", where additional malicious programs are downloaded onto the host.
Take the document file below as an example:
![](https://i.imgur.com/ciosaCD.png)
Looks perfectly okay, right? Well in actual fact, this word document has just downloaded a ransomware file from a malicious IP address in the background, with not much more than this snippet of code:
![](https://i.imgur.com/DQxSeHt.png)
I have programmed the script to show a pop-up for demonstration purposes. However, in real life, this would be done without any popup.
![](https://i.imgur.com/SVT0kOZ.png)
Luckily for me, this EXE is safe. Unfortunately in the real-world, this EXE could start encrypting my files.
Thankfully Anti-Viruses these days are pretty reliable on picking up that sort of activity when it is left in plaintext. The following example uses two-stages to execute an obfuscated payload code.
The macro starts once edit permissions ("Enable Edit" or "Enable Content")have enabled edit mode on the Word document
The macro executes the payload stored in the text within the document.
The downside to this? You need a large amount of text to be contained within the page, users will be suspicious and not proceed with editing the document.
![](https://i.imgur.com/5Td2ywE.png)
Although, just put on your steganography hat...Authors can just remove the borders from the text box and make the text white. The macro doesn't need the text to be visible to the user, it just needs to exist on the page.
![](https://i.imgur.com/DMhsuTd.png)
See? Not so suspicious now.
Practical
First, we will analyse a suspicious Microsoft Office Word document together. We can simply use REMnux's vmonkey which is a parser engine that is capable of analysing visual basic macros without executing (opening the document).
By using vmonkey DefinitelyALegitInvoice.doc. vmonkey has detected potentially malicious visual basic code within a macro.
![](https://i.imgur.com/jooSji9.png)
Now it's your turn, analyse the two Microsoft Office document's (.doc) files located within "/home/remnux/Tasks/4" to answer the questions attached to this task.
```text
remnux@thm-remnux:~/Tasks$ cd 4
remnux@thm-remnux:~/Tasks/4$ ls
DefinitelyALegitInvoice.doc  Taxes2020.doc
remnux@thm-remnux:~/Tasks/4$ vmonkey DefinitelyALegitInvoice.doc 
 _    ___                 __  ___            __             
| |  / (_)___  ___  _____/  |/  /___  ____  / /_____  __  __
| | / / / __ \/ _ \/ ___/ /|_/ / __ \/ __ \/ //_/ _ \/ / / /
| |/ / / /_/ /  __/ /  / /  / / /_/ / / / / ,< /  __/ /_/ / 
|___/_/ .___/\___/_/  /_/  /_/\____/_/ /_/_/|_|\___/\__, /  
     /_/                                           /____/   
vmonkey 0.08 - https://github.com/decalage2/ViperMonkey
THIS IS WORK IN PROGRESS - Check updates regularly!
Please report any issue at https://github.com/decalage2/ViperMonkey/issues

===============================================================================
FILE: DefinitelyALegitInvoice.doc
INFO     Starting emulation...
INFO     Emulating an Office (VBA) file.
INFO     Reading document metadata...
Traceback (most recent call last):
  File "/opt/vipermonkey/src/vipermonkey/vipermonkey/export_all_excel_sheets.py", line 15, in <module>
    from unotools import Socket, connect
ModuleNotFoundError: No module named 'unotools'
ERROR    Running export_all_excel_sheets.py failed. Command '['python3', '/opt/vipermonkey/src/vipermonkey/vipermonkey/export_all_excel_sheets.py', '/tmp/tmp_excel_file_4517180779']' returned non-zero exit status 1        
ERROR    Reading in file as Excel with xlrd failed. Can't find workbook in OLE2 compound document                                                   
INFO     Saving dropped analysis artifacts in .//DefinitelyALegitInvoice.doc_artifacts/                                                             
INFO     Parsing VB...
-------------------------------------------------------------------------------
VBA MACRO ThisDocument.cls 
in file:  - OLE stream: u'Macros/VBA/ThisDocument'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
-------------------------------------------------------------------------------
VBA CODE (with long lines collapsed):
Private Sub DefoLegit()
