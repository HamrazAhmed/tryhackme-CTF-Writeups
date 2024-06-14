---
Provide understanding to Sigma, a Generic Signature Format for SIEM Systems.
---

# Sigma — Writeup

## Overview
### Sigma — Writeup
### Sigma — Writeup
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/2cdd7c4c0da4c5f1c890b8406c30c363.png)
![](https://assets.tryhackme.com/room-banners/sigma.png)
### Introduction
Introduction
Detection engineering is an important role and task for a security analyst. It involves developing processes that will guide you as an analyst to identify threats before they cause any harm to an environment through the use of rules. This room will introduce you to Sigma, an open-source generic signature language used to write detection rules applicable across different SIEM backends.
Learning Objectives
-   Introduction to the Sigma rule language.
-   Learn about Sigma Rule writing syntax and conversion to various SIEM query languages.
-   Navigate through writing rules for various detections on Windows Event Logs.
-   Practice writing Sigma rules for an interactive case.
Prerequisites
It is advisable to check out the following rooms to understand the defensive security operations that would be useful for a security analyst during threat detection.
-   [Security Operations](https://tryhackme.com/room/securityoperations)
-   [Windows Event Logs](https://tryhackme.com/room/windowseventlogs)
-   [Sysmon](https://tryhackme.com/room/sysmon)
-   [Splunk 101](https://tryhackme.com/room/splunk101)
-   [Investigating with ELK 101](https://tryhackme.com/room/investigatingwithelk101)
### What is Sigma?
Through log monitoring and analysis, SOC analysts are tasked with collecting, analysing and extracting as much usable information from logs and using it to build detection queries and searches for their environments. However, on most occasions, it becomes challenging to standardise investigations and have the ability to share them with other analysts for detection enrichment. Sharing Indicators of compromise (IOC) and signatures may not be enough, as log events are often left unattended. Here is where Sigma seeks to bridge the gap.
[Sigma](https://github.com/SigmaHQ/sigma) is an open-source generic signature language developed by Florian Roth & Thomas Patzke to describe log events in a structured format. This allows for quick sharing of detection methods by security analysts. It is mentioned that **"Sigma is for log files as Snort is for network traffic, and Yara is for files."**
Sigma makes it easy to perform content matching based on collected logs to raise threat alerts for analysts to investigate. Log files are usually collected and stored in a database or SIEM solution for further analysis.
### Sigma Use Cases
Sigma was developed to satisfy the following uses:
-   To make detection methods and signatures shareable alongside IOCs and Yara rules.
-   To write SIEM searches that avoid vendor lock-in.
-   To share signatures with threat intelligence communities.
-   To write custom detection rules for malicious behaviour based on specific conditions.
### Sigma Development Process
As a SOC analyst, the process of using Sigma to write up your detection rules will involve understanding the elements mentioned below:
-   **Sigma Rule Format:** Generic structured log descriptions written in YAML.
-   **Sigma Converter:** A set of python scripts that will process the rules on the backend and perform custom field matching based on specified SIEM query language.
-   **Machine Query:** Resulting search query to filter out alerts during investigations. The query will be based on the specified SIEM.
The [Sigma GitHub repo](https://github.com/SigmaHQ/sigma) provides information about the project, public rules, tests and conversion tools. Please have a look at the project as we progress through the room.
### Sigma Rule Syntax
Download Task Files
As indicated in the previous task, Sigma rules are written in YAML Ain't Markup Language ([YAML](http://yaml.org/)), a data serialisation language that is human-readable and useful for managing data. It's often used as a format for configuration files, but its object serialisation abilities make it a substitute for languages like JSON.
Common factors to note about YAML files are:
-   YAML is case-sensitive.
-   Files should have the `.yml` extension.
-   Spaces are used for indentation and not tabs.
-   Comments are attributed using the `#` character.
-   Key-value pairs are denoted using the colon `:` character.
-   Array elements are denoted using the dash `-` character.
[QuickYAML Guide](https://www.tutorialspoint.com/yaml/yaml_quick_guide.htm)
### Sigma Syntax
Let us use an example of a WMI Event Subscription [rule](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/wmi_event/sysmon_wmi_event_subscription.yml) to define the different syntax elements. Download the attached task file, and open it in a text editor to go through this room's rule syntax and rule writing sections.
-   **Title:** Names the rule based on what it is supposed to detect. This should be short and clear.
-   **ID:** A globally unique identifier mainly used by the developers of Sigma to maintain the order of identification for the rules submitted to the public repository, found in UUID format.
You may also add references to related rule IDs using the _related_ attribute, making it easier to form relationships between detections. These relations would fall under the following types:
-   Derived: This will describe that the rule has sprung from another rule, which may still be active.
-   Obsolete: This will indicate that the listed rule is no longer being used.
-   Merged: This will indicate that the rule combines linked rules.
-   Renamed: This indicates the rule was previously identified under a different ID but has now been changed due to changes in naming schemes or avoiding collisions.
-   Similar: This attribute points to corresponding rules, such as indicating the same detection content applied to different log sources.
-   **Status:** Describes the stage in which the rule maturity is at while in use. There are five declared statuses that you can use:
-   _Stable_: The rule may be used in production environments and dashboards.
-   _Test_: Trials are being done to the rule and could require fine-tuning.
-   _Experimental_: The rule is very generic and is being tested. It could lead to false results, be noisy, and identify interesting events.
-   _Deprecated_: The rule has been replaced and would no longer yield accurate results. The`related` field is used to create associations between the current rule and one that has been deprecated.
-   _Unsupported_: The rule is not usable in its current state (unique correlation log, homemade fields).
-   **Description:** Provides more context about the rule and its intended purpose. With the rule, you can be as verbose as possible on the malicious activity you intend to detect.
WMI_Event_Subscription.yml
```shell-session
title: WMI Event Subscription
id: 0f06a3a5-6a09-413f-8743-e6cf35561297
status: test
description: Detects creation of WMI event subscription persistence method.
```
-   **Logsource:** Describes the log data to be used for the detection. It consists of other optional attributes:
-   _Product_: Selects all log outputs of a particular product. Examples are Windows, Apache.
-   _Category_: Selects the log files written by the selected product. Examples are firewall, web, and antivirus.
-   _Service_: Selects only a subset of the logs from the selected product. Examples are _sshd_ on Linux or _Security_ on Windows.
-   _Definition_: Describes the log source and any applied configurations.
WMI_Event_Subscription.yml
```shell-session
logsource:
   product: windows    
   category: wmi_event
```
-   **Detection:** A required field in the detection rule describes the parameters of the malicious activity we need an alert for. The parameters are divided into two main parts: the search identifiers - the fields and values that the detection should be searching for -  and condition expression - which sets the action to be taken on the detection, such as selection or filtering. More on this is below.
This rule has a detection modifier that looks for logs with one of Windows Event IDs 19, 20 or 21. The condition informs the detection engine to match and select the identified logs.
WMI_Event_Subscription.yml
```shell-session
detection:
  selection:
    EventID:  # This shows the search identifier value
      - 19    # This shows the search's list value
      - 20
      - 21
  condition: selection
```
-   **FalsePositives:** A list of known false positive outputs based on log data that may occur.
-   **Level:** Describes the severity with which the activity should be taken under the written rule. The attribute comprises five levels: Informational -> Low -> Medium -> High -> Critical
-   **Tags:** Adds information that may be used to categorise the rule. Tags may include values for CVE numbers and tactics and techniques from the MITRE ATT&CK framework. Sigma developers have defined a list of [predefined tags](https://github.com/SigmaHQ/sigma/wiki/Tags).
WMI_Event_Subscription.yml
```shell-session
falsepositives:
    - Exclude legitimate (vetted) use of WMI event subscription in your network

level: medium

tags:
  - attack.persistence # Points to the MITRE tactic.
  - attack.t1546.003   # Points to the MITRE technique.
```
### Search Identifiers and Condition Expressions
As mentioned earlier, the detection section of the rule describes what you intend to search for within the log data and how the selection and filters are to be evaluated. The definition of the search identifiers can comprise two data structures - **lists and maps** - which dictate the order in which the detection would be processed.
When the identifiers are provided using lists, they will be presented using strings linked with a logical **'OR'** operation. Mainly, they will be listed using hyphens (-). For example, below, we can look at an extract of the [Netcat Powershell Version rule](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_powercat.yml) where the detection is written to match on the `HostApplication` field containing 'powercat' or 'powercat.ps1' as its value.
Posh_PC_Powercat.yml
```shell-session
detection:
  selection:
    HostApplication|contains:
         - 'powercat'
         - 'powercat.ps1'
  condition: selection
```
On the other hand, maps comprise key/value pairs where the key matches up to a field in the log data while the value presented is a string or numeral value to be searched for within the log. Maps follow a logical **'AND'** operation.
As an example, we can look at the [Clear Linux log rule](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_clear_logs.yml) where the `selection` term forms the map, and the rule intends to match on `Image|endswith` either of the values listed, AND `CommandLine` contains either value listed. This example shows how maps and lists can be used together when developing detections. It should be noted that `endswith` and `contains` are value modifiers, and two lists are used for the search values, where one of each group has to match for the rule to initiate an alert.
Process_Creation_Lnx_Clear_Logs.yml
```shell-session
detection:
  selection:
    Image|endswith:
         - '/rm' # covers /rmdir as well
         - '/shred'
    CommandLine|contains:
         - '/var/log'
         - '/var/spool/mail'
  condition: selection
```
As we have mentioned the value modifier, it is worth noting that they are appended after the field name with a pipe character (|), and there are two types of value modifiers:
-   **Transformation modifiers:** These change the values provided into different values and can modify the logical operations between values. They include:
-   _contains:_ The value would be matched anywhere in the field.
-   _all:_ This changes the OR operation of lists into an AND operation. This means that the search conditions has to match all listed values.
-   _base64:_ This looks at values encoded with Base64.
-   _endswith:_ With this modifier, the value is expected to be at the end of the field. For example, this is representative of `*\cmd.exe`.
-   _startswith:_ This modifier will match the value at the beginning of the field. For example, `power*`.
-   **Type modifiers:** These change the type of the value or sometimes even the value itself. Currently, the only usable type modifier is `re`, which is supported by Elasticsearch queries to handle the value as a regular expression.
For conditions, this is based on the names set for your detections, such as _selection and_ _filter,_ and will determine the specification of the rule based on a selected expression. Some of the terms supported include:
-   **Logical AND/OR**
-   **1/all of search-identifier**
-   **1/all of them**
-   **not**
An example of these conditional values can be seen in the extract below from the [Remote File Copy rule](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_file_copy.yml), where the detection seeks to look for either of the tools: `scp`, `rsync` or `sftp` and with either filter values `@` or `:`.
Remote_File_Copy.yml
```shell-session
detection:
  tools:
         - 'scp'
         - 'rsync'
         - 'sftp'
  filter:
         - '@'
         - ':'
  condition: tools and filter
```
Another example to showcase a combination of the conditional expressions can be seen in the extract below from the [Run Once Persistence Registry Event rule](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_runonce_persistence.yml), where the detection seeks to look for values on the map that start and end with various registry values while filtering out Google Chrome and Microsoft Edge entries that would raise false positive alerts.
Registry_Event_RunOnce_Persistence.yml
```shell-session
detection:
  selection:
    TargetObject|startswith: 'HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components'
    TargetObject|endswith: '\StubPath'
  filter_chrome:
    Details|startswith: '"C:\Program Files\Google\Chrome\Application\'
    Details|endswith: '\Installer\chrmstp.exe" --configure-user-settings --verbose-logging --system-level'
  filter_edge:
    Details|startswith:
    - '"C:\Program Files (x86)\Microsoft\Edge\Application\'
    - '"C:\Program Files\Microsoft\Edge\Application\'
    Details|endswith: '\Installer\setup.exe" --configure-user-settings --verbose-logging --system-level --msedge 
    --channel=stable'
  condition: selection and not 1 of filter_*
```
Click the link to find more information about the [Sigma syntax specification.](https://github.com/SigmaHQ/sigma/wiki/Specification)
Answer the questions below
Which status level could lead to false results or be noisy, but could also identify interesting events?
*experimental*
The rule detection comprises two main elements: __ and condition expressions.
*search identifiers*
What two data structures are used for the search identifiers?
answer1 and answer2
*lists and maps*
### Rule Writing & Conversion
Start Machine
After going through the basic syntax of Sigma rules, it is crucial to understand how to write them based on a threat investigation. As a SOC analyst, you must go through the thought process of developing your detection and writing the rules appropriate for your environment. We shall use the scenario below to go through this process.
Start up the attached machine and give it 5 minutes to load. Login to the Kibana dashboard on [http://MACHINE_IP/](http://machine_ip/), which has been populated with logs for testing the detection rules written in this task and the practical scenario in task 6. Use the credentials **THM_Analyst: THM_Analyst1234.** Deploy the AttackBox and log in to the Kibana dashboard using Firefox.
### Scenario
You should use the SIGMA specification file downloaded from Task 3  as a basis for writing the rule. If you are using the AttackBox, the file is available in the directory `/root/Rooms/sigma/Sigma_Rule_File.yml`.
### Step 1: Intel Analysis
The shared intel shows us a lot of information and commands to download and install AnyDesk. An adversary could wrap this up in a malicious executable sent to an unsuspecting user through a phishing email. We can start picking out values that would be important for detecting any occurrence of an installation.
-   Source URL: This marks the download source for the software, highlighted by the $url variable.
-   Destination File: The adversary would seek to identify a destination directory for the download. This is marked by the $file variable.
-   Installation Command: From the intel, we can see that various instances of `CMD.exe` are being used to install and set a user password by the script. From this, we can pick out the installation attributes such as `--install`, `--start-with-win` and `--silent`.
Other essential pieces of information from the intel would include:
-   Adversary Persistence: The adversary would seek to maintain access to the victim's machine. In this instance, they would create a user account `oldadministrator` and give the user elevated privileges to run other tasks.
-   Registry Edit: We can also pick out the registry edit, where the added user is added to a `SpecialAccounts` user list.
With this information, we can evaluate the creation of a rule to aid in detecting when an installation has taken place.
### Step 2: Rule Identification
We can start building our rule by filling in the Title and Description sections, given the information that we are looking for an AnyDesk remote tool installation. Let us also set the status as `experimental` , as this rule will be tested internally.
Process_Creation_AnyDesk_Installation.yml
```shell-session
title: AnyDesk Installation
status: experimental
description: AnyDesk Remote Desktop installation can be used by attacker to gain remote access.
```
### Step 3: Log Source
As indicated from our intel, Windows devices would be our targetted device. Windows Eventlog and Sysmon provide events such as process creation and file creation. Our case focuses on the creation of an installation process, thus listing our logsource category as `process_creation.`
Process_Creation_AnyDesk_Installation.yml
```shell-session
logsource:
    category: process_creation
    product: windows
```
The detection section of our rule is the essential part. The information derived from the intel will define what we need to detect within our environment. For the AnyDesk installation, we noted the installation commands that would be used by the adversary that contains the strings: `install`, and `start-with-win`. We can therefore write our search identifiers as below with the modifiers `contains` and `all` to indicate that the rule will match all those values.
Additionally, we can include searching for the current directory where the commands will be executed from, `C:\ProgramData\AnyDesk.exe`
For our condition expression, this evaluates the selection of our detection.
Process_Creation_AnyDesk_Installation.yml
```shell-session
detection:
    selection:
        CommandLine|contains|all: 
            - '--install'
            - '--start-with-win'
        CurrentDirectory|contains:
            - 'C:\ProgramData\AnyDesk.exe'
    condition: selection
```
### Step 5: Rule Metadata
After adding the required and vital bits to our rule, we can add other helpful information under level, tags, references and false positives. We can reference the MITRE ATT&CK Command and Control tactic and its corresponding [T1219](https://attack.mitre.org/techniques/T1219/) technique for tags.
With this, we have our rule, which we can now convert to the SIEM query of our choice and test the detection.
Process_Creation_AnyDesk_Installation.yml
```shell-session
falsepositives:
    - Legitimate deployment of AnyDesk
level: high
references:
    - https://twitter.com/TheDFIRReport/status/1423361119926816776?s=20
tags:
    - attack.command_and_control
    - attack.t1219
```
### Rule Conversion
Sigma rules need to be converted to the appropriate SIEM target that is being utilised to store all the logs. Using the rule we have written above, we shall now learn how to use the sigmac and uncoder.io tools to convert them into ElasticSearch and Splunk queries.
### Sigmac
[Sigmac](https://github.com/SigmaHQ/sigma/tree/8bb3379b6807610d61d29db1d76f5af4840b8208/tools) is a Python-written tool that converts Sigma rules by matching the detection log source field values to the appropriate SIEM backend fields. As part of the Sigma repo (Advisable to clone the repo to get the tool and all the available rules published by the Sigma team), this tool allows for quick and easy conversion of Sigma rules from the command line. Below is a snippet of how to use the tool through its help command, and we shall display the basic syntax of using the tool by converting the AnyDesk rule we have written to the Splunk query.
Note: Sigmac will be deprecated by end of 2022, and attention from the owners will shift to sigma-cli. However, a copy of Sigmac is available on the AttackBox, and you can initiate the use of the tool for the rest of the room using `python3.9 root/Rooms/sigma/sigma/tools/sigmac`.
Sigmac Help Options
```shell-session
SecurityNomad@THM:~# cd /root/Rooms/sigma/sigma/tools/
SecurityNomad@THM:~/Rooms/sigma/sigma/tools# python3.9 sigmac -h

usage: sigmac [-h] [--recurse] [--filter FILTER]
              [--target {chronicle,kibana-ndjson,sumologic,sumologic-cse,es-rule-eql,athena,carbonblack,limacharlie,netwitness,csharp,hawk,opensearch-monitor,powershell,ala-rule,elastalert,sql,xpack-watcher,netwitness-epl,ala,lacework,logiq,qualys,sysmon,arcsight-esm,fireeye-helix,hedera,fortisiem,humio,kibana,mdatp,grep,streamalert,sumologic-cse-rule,uberagent,es-qs-lr,es-eql,es-dsl,es-rule,sqlite,stix,fieldlist,devo,es-qs,splunkxml,logpoint,datadog-logs,splunkdm,qradar,sentinel-rule,crowdstrike,elastalert-dsl,arcsight,ee-outliers,splunk,graylog}]
              [--lists] [--lists-files-after-date LISTS_FILES_AFTER_DATE]
              [--config CONFIG] [--output OUTPUT]
              [--output-fields OUTPUT_FIELDS] [--output-format {json,yaml}]
              [--output-extention OUTPUT_EXTENTION] [--print0]
              [--backend-option BACKEND_OPTION]
              [--backend-config BACKEND_CONFIG] [--backend-help BACKEND_HELP]
              [--defer-abort] [--ignore-backend-errors] [--verbose] [--debug]
              [inputs [inputs ...]]

Convert Sigma rules into SIEM signatures.
```
The main options to be used are:
-   -t: This sets the targeted SIEM backend you wish to get queries for (Elasticsearch, Splunk, QRadar, ElastAlert).
-   -c: This sets the configuration file used for the conversion. The file handles the field mappings between the rule and the target SIEM environment, ensuring that the necessary fields are correct for performing investigations on your environment.
-   --backend-option: This allows you to pass a backend configuration file or individual modifications that dictate alert options for the target SIEM environment. For example, in ElasticSearch, we can specify specific field properties to be our primary keyword_field to be searched against, such as fields that end in the `.keyword` or `.security` fields below:
Sigmac ElasticSearch Conversion
```shell-session
SecurityNomad@THM:~/Rooms/sigma/sigma/tools# python3.9 sigmac -t es-qs -c tools/config/winlogbeat.yml --backend-option keyword_field=".keyword" --backend-option analyzed_sub_field_name=".security" ../rules/windows/sysmon/sysmon_accessing_winapi_in_powershell_credentials_dumping.yml

(winlog.channel.security:"Microsoft\-Windows\-Sysmon\/Operational" AND winlog.event_id.security:("8" OR "10") AND winlog.event_data.SourceImage.keyword:*\\powershell.exe AND winlog.event_data.TargetImage.keyword:*\\lsass.exe)
```
You can find more information through the [Sigmac documentation](https://github.com/SigmaHQ/sigma/blob/master/tools/README.md). We can convert our AnyDesk Installation rule  to a Splunk alert as shown below:
Sigmac Splunk Conversion
```shell-session
SecurityNomad@THM:~/Rooms/sigma/sigma/tools# python3.9 sigmac -t splunk -c splunk-windows Process_Creation_AnyDesk_Installation.yml

(CommandLine="*--install*" CommandLine="*--start-with-win*" (CurrentDirectory="*C:\\ProgramData\\AnyDesk.exe*"))
```
Sigma developers are working on a python library that will be Sigmac's replacement, known as [pySigma](https://github.com/SigmaHQ/pySigma).
### Uncoder.io
[Uncoder.IO](https://uncoder.io/) is an open-source web Sigma converter for numerous SIEM and EDR platforms. It is easy to use as it allows you to copy your Sigma rule on the platform and select your preferred backend application for translation.
We can copy our rule and convert it into different queries of our choice. Below, the rule has been converted into Elastic Query, QRadar and Splunk. You can copy the translation into the SIEM platform to test for any matches.
Convert the AnyDesk Installation Sigma rule we have written throughout this task to an Elastic Query and use it to analyse log data from the launched machine on the Kibana dashboard. Use the information found to answer the following questions.
**TIP: Be aware that the converted queries may not all work verbatim as converted from the tools. This is due to the processing of regex characters (\,*), and you may be required to adjust the queries, especially around escaped blank space. For example, for this exercise, you have to remove the * characters from the result and only escape the colon (:) in the folder path and the directory slashes.**
Answer the questions below
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ nano Process_Creation_AnyDesk_Installation.yml
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ cat Process_Creation_AnyDesk_Installation.yml 
title: AnyDesk Installation
status: experimental
description: AnyDesk Remote Desktop installation can be used by attacker to gain remote access.
logsource:
    category: process_creation
    product: windows
detection:
    selection:
        CommandLine|contains|all: 
            - '--install'
            - '--start-with-win'
        CurrentDirectory|contains:
            - 'C:\ProgramData\AnyDesk.exe'
    condition: selection
falsepositives:
    - Legitimate deployment of AnyDesk
level: high
references:
    - https://twitter.com/TheDFIRReport/status/1423361119926816776?s=20
tags:
    - attack.command_and_control
    - attack.t1219

(process.command_line.text:*\-\-install* AND process.command_line.text:*\-\-start\-with\-win* AND process.working_directory.text:*C\:\\ProgramData\\AnyDesk.exe*)

login: **THM_Analyst: THM_Analyst1234**

then search : 1 year before

(process.command_line.text:--install AND process.command_line.text:--start-with-win AND process.working_directory.text:C\:\\ProgramData\\AnyDesk.exe)

and find 1 result

{
  "_index": ".ds-winlogbeat-8.2.3-2022.06.27-000001",
  "_id": "kVdlrIEB3iMYFrgzf9-i",
  "_version": 1,
  "_score": 1,
  "_source": {
    "agent": {
      "name": "THM_Aurora_Test",
      "id": "ba6b17a6-3ca3-45a9-b4b2-fc995ab1c73a",
      "type": "winlogbeat",
      "ephemeral_id": "c483a7ab-6222-40f5-af9e-467e53880dac",
      "version": "8.2.3"
    },
    "process": {
      "args": [
        "C:\\Users\\Administrator\\Desktop\\AnyDesk.exe",
        "--install",
        "C:\\Program Files (x86)\\AnyDesk",
        "--start-with-win",
        "--create-shortcuts",
        "--create-taskbar-icon",
        "--create-desktop-icon",
        "--install-driver:mirror",
        "--update-disabled",
        "--svc-conf",
        "C:\\Users\\Administrator\\AppData\\Roaming\\AnyDesk\\service.conf",
        "--sys-conf",
        "C:\\Users\\Administrator\\AppData\\Roaming\\AnyDesk\\system.conf"
      ],
      "parent": {
        "args": [
          "C:\\Users\\Administrator\\Desktop\\AnyDesk.exe",
          "/S"
        ],
        "name": "AnyDesk.exe",
        "pid": 1392,
        "args_count": 2,
        "entity_id": "{c5d2b969-7bf0-62bb-0103-000000001f01}",
        "executable": "C:\\Users\\Administrator\\Desktop\\AnyDesk.exe",
        "command_line": "\"C:\\Users\\Administrator\\Desktop\\AnyDesk.exe\" /S "
      },
      "pe": {
        "file_version": "7.0.10",
        "product": "AnyDesk",
        "description": "AnyDesk",
        "original_file_name": "-",
        "company": "AnyDesk Software GmbH"
      },
      "name": "AnyDesk.exe",
      "pid": 2612,
      "working_directory": "C:\\Users\\Administrator\\Desktop\\",
      "args_count": 13,
      "entity_id": "{c5d2b969-7e54-62bb-0603-000000001f01}",
      "hash": {
        "sha1": "9779751121508f17cbd831e9c2780b4cf0e1b96c",
        "sha256": "d7b9f1141c649c08254a4978f98211a5ab3b10591693fcf271409e36beae2933",
        "md5": "0dbe3504bc5daa73e7b3f75bbb104e42"
      },
      "executable": "C:\\Users\\Administrator\\Desktop\\AnyDesk.exe",
      "command_line": "\"C:\\Users\\Administrator\\Desktop\\AnyDesk.exe\" --install \"C:\\Program Files (x86)\\AnyDesk\"  --start-with-win --create-shortcuts --create-taskbar-icon --create-desktop-icon --install-driver:mirror --update-disabled --svc-conf \"C:\\Users\\Administrator\\AppData\\Roaming\\AnyDesk\\service.conf\"  --sys-conf \"C:\\Users\\Administrator\\AppData\\Roaming\\AnyDesk\\system.conf\" "
    },
    "winlog": {
      "computer_name": "THM_Aurora_Test",
      "process": {
        "pid": 3528,
        "thread": {
          "id": 2908
        }
      },
      "channel": "Microsoft-Windows-Sysmon/Operational",
      "event_data": {
        "Company": "AnyDesk Software GmbH",
        "LogonGuid": "{c5d2b969-7ee7-62b9-4833-170000000000}",
        "Description": "AnyDesk",
        "TerminalSessionId": "2",
        "IntegrityLevel": "High",
        "ParentUser": "THM_AURORA_TEST\\Administrator",
        "Product": "AnyDesk",
        "FileVersion": "7.0.10",
        "LogonId": "0x173348"
      },
      "opcode": "Info",
      "version": 5,
      "record_id": "9284",
      "event_id": "1",
      "task": "Process Create (rule: ProcessCreate)",
      "provider_guid": "{5770385f-c22a-43e0-bf4c-06f5698ffbd9}",
      "api": "wineventlog",
      "provider_name": "Microsoft-Windows-Sysmon",
      "user": {
        "identifier": "S-1-5-18",
        "domain": "NT AUTHORITY",
        "name": "SYSTEM",
        "type": "User"
      }
    },
    "log": {
      "level": "information"
    },
    "rule": {
      "name": "technique_id=T1036,technique_name=Masquerading"
    },
    "message": "Process Create:\nRuleName: technique_id=T1036,technique_name=Masquerading\nUtcTime: 2022-06-28 22:19:00.780\nProcessGuid: {c5d2b969-7e54-62bb-0603-000000001f01}\nProcessId: 2612\nImage: C:\\Users\\Administrator\\Desktop\\AnyDesk.exe\nFileVersion: 7.0.10\nDescription: AnyDesk\nProduct: AnyDesk\nCompany: AnyDesk Software GmbH\nOriginalFileName: -\nCommandLine: \"C:\\Users\\Administrator\\Desktop\\AnyDesk.exe\" --install \"C:\\Program Files (x86)\\AnyDesk\"  --start-with-win --create-shortcuts --create-taskbar-icon --create-desktop-icon --install-driver:mirror --update-disabled --svc-conf \"C:\\Users\\Administrator\\AppData\\Roaming\\AnyDesk\\service.conf\"  --sys-conf \"C:\\Users\\Administrator\\AppData\\Roaming\\AnyDesk\\system.conf\" \nCurrentDirectory: C:\\Users\\Administrator\\Desktop\\\nUser: THM_AURORA_TEST\\Administrator\nLogonGuid: {c5d2b969-7ee7-62b9-4833-170000000000}\nLogonId: 0x173348\nTerminalSessionId: 2\nIntegrityLevel: High\nHashes: SHA1=9779751121508F17CBD831E9C2780B4CF0E1B96C,MD5=0DBE3504BC5DAA73E7B3F75BBB104E42,SHA256=D7B9F1141C649C08254A4978F98211A5AB3B10591693FCF271409E36BEAE2933,IMPHASH=00000000000000000000000000000000\nParentProcessGuid: {c5d2b969-7bf0-62bb-0103-000000001f01}\nParentProcessId: 1392\nParentImage: C:\\Users\\Administrator\\Desktop\\AnyDesk.exe\nParentCommandLine: \"C:\\Users\\Administrator\\Desktop\\AnyDesk.exe\" /S \nParentUser: THM_AURORA_TEST\\Administrator",
    "cloud": {
      "availability_zone": "eu-west-1b",
      "image": {
        "id": "ami-0844a966e30ab3c23"
      },
      "instance": {
        "id": "i-0f365e6a14c6c7ae1"
      },
      "provider": "aws",
      "machine": {
        "type": "t2.medium"
      },
      "service": {
        "name": "EC2"
      },
      "region": "eu-west-1",
      "account": {
        "id": "739930428441"
      }
    },
    "@timestamp": "2022-06-28T22:19:00.780Z",
    "ecs": {
      "version": "1.12.0"
    },
    "related": {
      "user": [
        "Administrator"
      ],
      "hash": [
        "d7b9f1141c649c08254a4978f98211a5ab3b10591693fcf271409e36beae2933",
        "9779751121508f17cbd831e9c2780b4cf0e1b96c",
        "0dbe3504bc5daa73e7b3f75bbb104e42"
      ]
    },
    "host": {
      "hostname": "THM_Aurora_Test",
      "os": {
        "build": "17763.1821",
        "kernel": "10.0.17763.1821 (WinBuild.160101.0800)",
        "name": "Windows Server 2019 Datacenter",
        "family": "windows",
        "type": "windows",
        "version": "10.0",
        "platform": "windows"
      },
      "ip": [
        "fe80::8495:da75:43eb:5822",
        "10.10.222.40"
      ],
      "name": "THM_Aurora_Test",
      "id": "c5d2b969-b61a-4159-8f78-6391a1c805db",
      "mac": [
        "02:23:bb:82:ce:19"
      ],
      "architecture": "x86_64"
    },
    "event": {
      "ingested": "2022-06-28T22:19:01.919824857Z",
      "code": "1",
      "provider": "Microsoft-Windows-Sysmon",
      "created": "2022-06-28T22:19:00.897Z",
      "kind": "event",
      "module": "sysmon",
      "action": "Process Create (rule: ProcessCreate)",
      "type": [
        "start"
      ],
      "category": [
        "process"
      ]
    },
    "user": {
      "domain": "THM_AURORA_TEST",
      "name": "Administrator",
      "id": "S-1-5-18"
    }
  },
  "fields": {
    "process.hash.md5": [
      "0dbe3504bc5daa73e7b3f75bbb104e42"
    ],
    "event.category": [
      "process"
    ],
    "host.os.name.text": [
      "Windows Server 2019 Datacenter"
    ],
    "process.parent.command_line": [
      "\"C:\\Users\\Administrator\\Desktop\\AnyDesk.exe\" /S "
    ],
    "process.parent.name": [
      "AnyDesk.exe"
    ],
    "process.parent.pid": [
      1392
    ],
    "process.hash.sha256": [
      "d7b9f1141c649c08254a4978f98211a5ab3b10591693fcf271409e36beae2933"
    ],
    "host.hostname": [
      "THM_Aurora_Test"
    ],
    "host.mac": [
      "02:23:bb:82:ce:19"
    ],
    "winlog.process.pid": [
      3528
    ],
    "host.os.version": [
      "10.0"
    ],
    "agent.name": [
      "THM_Aurora_Test"
    ],
    "winlog.event_data.Company": [
      "AnyDesk Software GmbH"
    ],
    "user.id": [
      "S-1-5-18"
    ],
    "host.os.type": [
      "windows"
    ],
    "cloud.region": [
      "eu-west-1"
    ],
    "agent.hostname": [
      "THM_Aurora_Test"
    ],
    "process.pe.product": [
      "AnyDesk"
    ],
    "related.user": [
      "Administrator"
    ],
    "host.architecture": [
      "x86_64"
    ],
    "cloud.provider": [
      "aws"
    ],
    "event.provider": [
      "Microsoft-Windows-Sysmon"
    ],
    "cloud.machine.type": [
      "t2.medium"
    ],
    "winlog.event_data.FileVersion": [
      "7.0.10"
    ],
    "event.code": [
      "1"
    ],
    "agent.id": [
      "ba6b17a6-3ca3-45a9-b4b2-fc995ab1c73a"
    ],
    "winlog.event_data.LogonGuid": [
      "{c5d2b969-7ee7-62b9-4833-170000000000}"
    ],
    "winlog.event_data.Description": [
      "AnyDesk"
    ],
    "process.command_line.text": [
      "\"C:\\Users\\Administrator\\Desktop\\AnyDesk.exe\" --install \"C:\\Program Files (x86)\\AnyDesk\"  --start-with-win --create-shortcuts --create-taskbar-icon --create-desktop-icon --install-driver:mirror --update-disabled --svc-conf \"C:\\Users\\Administrator\\AppData\\Roaming\\AnyDesk\\service.conf\"  --sys-conf \"C:\\Users\\Administrator\\AppData\\Roaming\\AnyDesk\\system.conf\" "
    ],
    "winlog.process.thread.id": [
      2908
    ],
    "user.name": [
      "Administrator"
    ],
    "process.working_directory": [
      "C:\\Users\\Administrator\\Desktop\\"
    ],
    "process.entity_id": [
      "{c5d2b969-7e54-62bb-0603-000000001f01}"
    ],
    "host.ip": [
      "fe80::8495:da75:43eb:5822",
      "10.10.222.40"
    ],
    "cloud.instance.id": [
      "i-0f365e6a14c6c7ae1"
    ],
    "agent.type": [
      "winlogbeat"
    ],
    "process.pe.original_file_name": [
      "-"
    ],
    "process.executable.text": [
      "C:\\Users\\Administrator\\Desktop\\AnyDesk.exe"
    ],
    "winlog.api": [
      "wineventlog"
    ],
    "user.domain": [
      "THM_AURORA_TEST"
    ],
    "host.id": [
      "c5d2b969-b61a-4159-8f78-6391a1c805db"
    ],
    "process.pe.file_version": [
      "7.0.10"
    ],
    "process.working_directory.text": [
      "C:\\Users\\Administrator\\Desktop\\"
    ],
    "winlog.user.name": [
      "SYSTEM"
    ],
    "cloud.image.id": [
      "ami-0844a966e30ab3c23"
    ],
    "process.pe.company": [
      "AnyDesk Software GmbH"
    ],
    "event.action": [
      "Process Create (rule: ProcessCreate)"
    ],
    "event.ingested": [
      "2022-06-28T22:19:01.919Z"
    ],
    "@timestamp": [
      "2022-06-28T22:19:00.780Z"
    ],
    "winlog.channel": [
      "Microsoft-Windows-Sysmon/Operational"
    ],
    "cloud.account.id": [
      "739930428441"
    ],
    "host.os.platform": [
      "windows"
    ],
    "winlog.opcode": [
      "Info"
    ],
    "agent.ephemeral_id": [
      "c483a7ab-6222-40f5-af9e-467e53880dac"
    ],
    "winlog.event_data.TerminalSessionId": [
      "2"
    ],
    "process.hash.sha1": [
      "9779751121508f17cbd831e9c2780b4cf0e1b96c"
    ],
    "user.name.text": [
      "Administrator"
    ],
    "winlog.event_data.LogonId": [
      "0x173348"
    ],
    "process.name.text": [
      "AnyDesk.exe"
    ],
    "winlog.provider_name": [
      "Microsoft-Windows-Sysmon"
    ],
    "winlog.provider_guid": [
      "{5770385f-c22a-43e0-bf4c-06f5698ffbd9}"
    ],
    "related.hash": [
      "d7b9f1141c649c08254a4978f98211a5ab3b10591693fcf271409e36beae2933",
      "9779751121508f17cbd831e9c2780b4cf0e1b96c",
      "0dbe3504bc5daa73e7b3f75bbb104e42"
    ],
    "process.pid": [
      2612
    ],
    "winlog.computer_name": [
      "THM_Aurora_Test"
    ],
    "cloud.availability_zone": [
      "eu-west-1b"
    ],
    "process.parent.entity_id": [
      "{c5d2b969-7bf0-62bb-0103-000000001f01}"
    ],
    "winlog.record_id": [
      "9284"
    ],
    "host.os.name": [
      "Windows Server 2019 Datacenter"
    ],
    "log.level": [
      "information"
    ],
    "host.name": [
      "THM_Aurora_Test"
    ],
    "event.kind": [
      "event"
    ],
    "winlog.version": [
      5
    ],
    "rule.name": [
      "technique_id=T1036,technique_name=Masquerading"
    ],
    "process.parent.args_count": [
      2
    ],
    "process.name": [
      "AnyDesk.exe"
    ],
    "cloud.service.name": [
      "EC2"
    ],
    "process.parent.executable.text": [
      "C:\\Users\\Administrator\\Desktop\\AnyDesk.exe"
    ],
    "ecs.version": [
      "1.12.0"
    ],
    "event.created": [
      "2022-06-28T22:19:00.897Z"
    ],
    "process.pe.description": [
      "AnyDesk"
    ],
    "agent.version": [
      "8.2.3"
    ],
    "host.os.family": [
      "windows"
    ],
    "winlog.event_data.ParentUser": [
      "THM_AURORA_TEST\\Administrator"
    ],
    "process.parent.name.text": [
      "AnyDesk.exe"
    ],
    "winlog.user.type": [
      "User"
    ],
    "host.os.build": [
      "17763.1821"
    ],
    "event.module": [
      "sysmon"
    ],
    "host.os.kernel": [
      "10.0.17763.1821 (WinBuild.160101.0800)"
    ],
    "process.executable": [
      "C:\\Users\\Administrator\\Desktop\\AnyDesk.exe"
    ],
    "winlog.user.identifier": [
      "S-1-5-18"
    ],
    "winlog.task": [
      "Process Create (rule: ProcessCreate)"
    ],
    "winlog.user.domain": [
      "NT AUTHORITY"
    ],
    "process.parent.executable": [
      "C:\\Users\\Administrator\\Desktop\\AnyDesk.exe"
    ],
    "process.parent.command_line.text": [
      "\"C:\\Users\\Administrator\\Desktop\\AnyDesk.exe\" /S "
    ],
    "process.args_count": [
      13
    ],
    "winlog.event_data.IntegrityLevel": [
      "High"
    ],
    "process.args": [
      "C:\\Users\\Administrator\\Desktop\\AnyDesk.exe",
      "--install",
      "C:\\Program Files (x86)\\AnyDesk",
      "--start-with-win",
      "--create-shortcuts",
      "--create-taskbar-icon",
      "--create-desktop-icon",
      "--install-driver:mirror",
      "--update-disabled",
      "--svc-conf",
      "C:\\Users\\Administrator\\AppData\\Roaming\\AnyDesk\\service.conf",
      "--sys-conf",
      "C:\\Users\\Administrator\\AppData\\Roaming\\AnyDesk\\system.conf"
    ],
    "message": [
      "Process Create:\nRuleName: technique_id=T1036,technique_name=Masquerading\nUtcTime: 2022-06-28 22:19:00.780\nProcessGuid: {c5d2b969-7e54-62bb-0603-000000001f01}\nProcessId: 2612\nImage: C:\\Users\\Administrator\\Desktop\\AnyDesk.exe\nFileVersion: 7.0.10\nDescription: AnyDesk\nProduct: AnyDesk\nCompany: AnyDesk Software GmbH\nOriginalFileName: -\nCommandLine: \"C:\\Users\\Administrator\\Desktop\\AnyDesk.exe\" --install \"C:\\Program Files (x86)\\AnyDesk\"  --start-with-win --create-shortcuts --create-taskbar-icon --create-desktop-icon --install-driver:mirror --update-disabled --svc-conf \"C:\\Users\\Administrator\\AppData\\Roaming\\AnyDesk\\service.conf\"  --sys-conf \"C:\\Users\\Administrator\\AppData\\Roaming\\AnyDesk\\system.conf\" \nCurrentDirectory: C:\\Users\\Administrator\\Desktop\\\nUser: THM_AURORA_TEST\\Administrator\nLogonGuid: {c5d2b969-7ee7-62b9-4833-170000000000}\nLogonId: 0x173348\nTerminalSessionId: 2\nIntegrityLevel: High\nHashes: SHA1=9779751121508F17CBD831E9C2780B4CF0E1B96C,MD5=0DBE3504BC5DAA73E7B3F75BBB104E42,SHA256=D7B9F1141C649C08254A4978F98211A5AB3B10591693FCF271409E36BEAE2933,IMPHASH=00000000000000000000000000000000\nParentProcessGuid: {c5d2b969-7bf0-62bb-0103-000000001f01}\nParentProcessId: 1392\nParentImage: C:\\Users\\Administrator\\Desktop\\AnyDesk.exe\nParentCommandLine: \"C:\\Users\\Administrator\\Desktop\\AnyDesk.exe\" /S \nParentUser: THM_AURORA_TEST\\Administrator"
    ],
    "winlog.event_id": [
      "1"
