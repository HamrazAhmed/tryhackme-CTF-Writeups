---
Establish a baseline knowledge of tactical detection, leveraging efficient techniques to bolster your security posture.
---

# Tactical Detection — Writeup

## Overview
### Tactical Detection — Writeup
### Tactical Detection — Writeup
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/54b461182108211552af2f88808bb719.png)
### Introduction
_You’re hired as a security engineer, and you want to make a good impression. You noticed that there’s a default ruleset available, and it has already been enabled. The SOC team seems to function, albeit not as efficiently as you might expect - then it dawns on you; the default rules just won’t cut it._
This scenario is not uncommon - in fact, a common pitfall of modern SOCs today is leaning too much on default rules and settings of the products they deploy, leaving them with security alerts that don't really add value to their security posture.
Learning Objectives:
In this room, we will strive to understand the mindset behind choosing a tactical approach in alerting and detecting threats, IOAs, IOCs, etc. In the process, we will gain practical experience in setting up a basic tactical detection capability leveraging techniques used in real-life environments.
Room Prerequisites and Expectation Setting:
There are no hard prerequisites in order to gain value from this room; however, it would be very helpful to have a basic understanding of navigating cmd and executing basic commands, as well as navigating FullEventLogView as it would be our main tool in reviewing Event Logs.
This room will touch upon some of the most efficient ways to bolster an organization's security posture by leveraging detection mechanisms and walking the user through setting them up tactically. This should serve as a baseline where the user will be able to learn the basics, implement them in their functions, and make them truly their own.
### Unique Threat Intel
_You stumbled upon documentation of a previous incident containing a couple of unique Indicators of Compromise (IOCs)_
Unique IOCs of previous intrusions are good examples of Threat Intel as they’re traces of the specific adversary that your environment has already faced. The inclusion of these IOCs in your detection mechanism will help spot re-intrusion of that specific adversary immediately, among others.
The screenshots above are excerpts from a spreadsheet that contains IOCs that can be integrated with the organization’s current detection mechanism. It’s more or less the same format that Incident Responders use as they go through their investigation. Logging in IOCs in a file like this allows for better collaboration among multiple incident responders. It also makes scoping of the incident more effective - more often than not, IOCs lead to more IOCs.
In the spreadsheet excerpt above, based on the description, the direct indicator found by the authors of the documentation is actually just the **bad3xe69connection[.]io**; however, upon further inspection of the malicious domain, they were able to conclude that two other malicious domains should be recorded as IOCs due to their association with the original malicious domain.
To maximize our efficiency, we will transform these IOCs into detection rules in a vendor-agnostic format using **Sigma**.
Sigma is an open-source generic signature language developed to describe log events in a structured format. This allows for quick sharing of detection methods by security analysts.
A basic example of how it can be written into a functional Sigma rule is as follows.
baddomains.yml
```shell-session
title: Executable Download from Suspicious Domains
status: test
description: Detects download of executable types from hosts found in the IOC spreadsheet
author: Mokmokmok
modified: 2022/08/23
logsource:
  category: proxy
detection:
  selection:
    c-uri-extension:
      - 'exe'
    r-dns:
      - 'bad3xe69connection.io'
      - 'kind4bad.com'
      - 'nic3connection.io'
  condition: selection
fields:
  - c-uri
falsepositives:
  - Unkown
level: medium
```
The Sigma rule that we came up with from the IOCs presented above is very simple and straightforward, yet the additional layer of detection that it gives the organization is invaluable. In the grander scheme of things, these layers work together to give your analysts the visibility that they need to spot bad actors before it's too late.
Remember that the bad guys need to circumvent all our defenses in order to get to their objectives, but we only need them to fail one layer of detection to have an idea that they're there.
Answer the questions below
What did we use to transform IOCs as detection rules in a vendor-agnostic format?
*Sigma*
What is the original indicator found by the authors of the documentation? Write it as written in the spreadsheet.
*bad3xe69connection.io*
What is the full file path of the malicious file downloaded from the internet?
*C:\Downloads\bad3xe69.exe*
In the Sigma Rule baddomains.yml, what is the logsource category used by the author?
*proxy*
### Publicly Generated IOCs
_You’re feeling proud of yourself for being able to implement detection rules that have an immediate impact on the organization when suddenly, news broke out of a new 0-day vulnerability. Upon taking a closer look at it, you realize that your organization is directly susceptible to this vulnerability._
You don’t have to be able to experience everything in order to learn from something - you can learn from other people’s experiences or research or learnings. Analogous to that is the array of research being done by the community, and almost always, they release public IOCs. These public IOCs are then transformed into usable mechanisms to detect bad things in the environment.
Going back to our previous task, we've leveraged Sigma to transform unique IOCs into a product-agnostic form that we can use regardless of our SIEM choice. As this technique shows great promise to the community, there are a number of nice repositories that contain user-submitted Sigma rules that anyone can use. You can plug one directly into your SIEM for immediate value, or further edit it to fit your environment and add even more value to your security posture.
The following is a nice exercise: Write a detection rule for these two / transform these publicly generated IOCs into usable alerts for use in the Elastic Stack and Splunk. We will do the first one together, while you can do the rest on your own. For our purposes, we will be using [Uncoder](https://uncoder.io/) to help with the transformation of these sigma rules. Uncoder is a nice tool that helps convert sigma rules to queries that can be immediately used within a SIEM of your choice.
A fairly recent 0-day vulnerability, Follina-MSDT, has a publicly available sigma rule developed by huntress's Matthew Brennan:
Follina-MSDT Sigma Rule
```shell-session
title: Suspicious msdt.exe execution - Office Exploit
id: 97a80ed7-1f3f-4d05-9ef4-65760e634f6b
status: experimental
description: This rule will monitor suspicious arguments passed to the msdt.exe process. These arguments are an indicator of recent Office/Msdt exploitation. 
references:
    - https://doublepulsar.com/follina-a-microsoft-office-code-execution-vulnerability-1a47fce5629e
    - https://twitter.com/MalwareJake/status/1531019243411623939
author: 'Matthew Brennan'
tags:
    - attack.execution
logsource:
    category: process_creation
    product: windows
detection:

    selection1:
      Image|endswith:
        - 'msdt.exe'
    selection2:
      CommandLine|contains:
        - 'PCWDiagnostic'
    selection3:
      CommandLine|contains:
        - 'ms-msdt:-id'
        - 'ms-msdt:/id'

    selection4:
      CommandLine|contains:
        - 'invoke'
    condition: selection1 and (selection4 or (selection2 and selection3))
falsepositives:
  - Unknown
level: high
```
Another 0-day vulnerability that made waves this past year, log4j, has multiple publicly available sigma rules. One such rule can detect [suspicious shells](https://github.com/SigmaHQ/sigma/blob/d46d89e403c7ebe9f70a100859c7c8cac1841a33/rules/windows/process_creation/proc_creation_win_susp_shell_spawn_by_java.yml) spawned from a Java host process, written by Andreas Hunkeler and Florian Roth:
Log4j Suspicious Shells Sigma Rule
```shell-session
title: Suspicious Shells Spawned by Java
id: 0d34ed8b-1c12-4ff2-828c-16fc860b766d
description: Detects suspicious shell spawned from Java host process (e.g. log4j exploitation)
status: experimental
author: Andreas Hunkeler (@Karneades), Florian Roth
modified: 2022/08/02
tags:
    - attack.initial_access
    - attack.persistence
    - attack.privilege_escalation
logsource:
    category: process_creation
    product: windows
detection:
    selection:
        ParentImage|endswith: '\java.exe'
        Image|endswith:
            - '\sh.exe'
            - '\bash.exe'
            - '\powershell.exe'
            - '\pwsh.exe'
            - '\schtasks.exe'
            - '\certutil.exe'
            - '\whoami.exe'
            - '\bitsadmin.exe'
            - '\wscript.exe'
            - '\cscript.exe'
            - '\scrcons.exe'
            - '\regsvr32.exe'
            - '\hh.exe'
            - '\wmic.exe'        # https://app.any.run/tasks/c903e9c8-0350-440c-8688-3881b556b8e0/
            - '\mshta.exe'
            - '\rundll32.exe'
            - '\forfiles.exe'
            - '\scriptrunner.exe'
            - '\mftrace.exe'
            - '\AppVLP.exe'
            - '\curl.exe'
    condition: selection
falsepositives:
    - Legitimate calls to system binaries
    - Company specific internal usage
level: high
```
Upon navigating to [Uncoder](https://uncoder.io/), you will immediately see two text boxes, as shown below:
Make sure that on the left side, the Sigma tab is selected as shown above. Copy the Follina-MSDT Sigma Rule contents and then paste it in the left text box. Since we're creating a detection rule for Elastic Stack, we will be using ElastAlert - you can find its documentation [here](https://elastalert.readthedocs.io/en/latest/). Click on the downward arrow and select ElastAlert. Upon doing so, the bottom messages should show _Translating from: Sigma_ and _Translating to: ElastAlert,_ respectively. Click on the _Translate_ button when you're ready.
Upon clicking Translate, it shouldn't take long before the results come out of the right text box.
It is important to note that there's no guarantee that the transformed Sigma rules will work perfectly straight out of Uncoder. In order to be production ready, you need to do a lot of testing and fine-tuning. What Uncoder essentially offers is a generic blueprint - it is up to the user to further improve upon it.
Answer the questions below
```text
Translating From Sigma to ElastAlert (uncoder.io)
alert:
- debug
description: This rule will monitor suspicious arguments passed to the msdt.exe process.
  These arguments are an indicator of recent Office/Msdt exploitation. (Rule 97a80ed7-1f3f-4d05-9ef4-65760e634f6b).
filter:
- query_string:
    query: (process.executable.text:*msdt.exe AND ((process.command_line.text:*invoke*)
      OR ((process.command_line.text:*PCWDiagnostic* AND process.command_line.text:(*ms\-msdt\:\-id*
      OR *ms\-msdt\:\/id*)))))
index: winlogbeat-*
name: suspicious_msdt_exe_execution___office_exploit
priority: 2
realert:
  minutes: 0
type: any
```
Upon translating the Follina Sigma Rule, what is the index name that the rule will be using, as shown in the output?
*winlogbeat-**
What is the Alerter subclass, as shown in the output?
This is described by the line right after "alert:"
*debug*
Change the Uncoder output to _Elastic Query._
Which part of the ElastAlert output looks exactly like the Elastic Query?
"part" refers to either of the following: alert, filter, index, name, priority, realert, and type
```text
(process.executable.text:*msdt.exe AND ((process.command_line.text:*invoke*) OR ((process.command_line.text:*PCWDiagnostic* AND process.command_line.text:(*ms\-msdt\:\-id* OR *ms\-msdt\:\/id*)))))
```
*filter*
Translate the Log4j Sigma Rule into a _Splunk Alert_.
What is the alert severity, as shown in the output?
```text
Translating from sigma to splunk alert

[Suspicious Shells Spawned by Java]
alert.severity = 3
description = Detects suspicious shell spawned from Java host process (e.g. log4j exploitation) (Rule ID: 0d34ed8b-1c12-4ff2-828c-16fc860b766d) Reference: https://tdm.socprime.com/tdm/info/0
cron_schedule = 0 * * * *
disabled = 1
is_scheduled = 1
is_visible = 1
dispatch.earliest_time = -60m@m
