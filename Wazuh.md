---
Wazuh is a free, open source and enterprise-ready security monitoring solution for threat detection, integrity monitoring.
---

# Wazuh — Writeup

## Overview
### Wazuh — Writeup
### Wazuh — Writeup
![](https://assets.tryhackme.com/additional/banners/wazuhbanner.png)
### Introduction
Welcome to a room showcasing the capabilities of the Wazuh EDR software solution. In this room, you can expect to learn the following things:
-   What is an EDR and why are they useful solutions
-   Where an EDR like Wazuh is used
-   Accessing Wazuh
-   Navigating Wazuh
-   Learning about Wazuh rules and alerts
-   Digesting logs to view specific events on devices including Linux and Windows
-   How you can extend Wazuh using plugins and its API
Firstly, let's understand what EDR solutions are exactly. Endpoint detection and response (EDR) are a series of tools and applications that monitor devices for an activity that could indicate a threat or security breach. These tools and applications have features that include:
-   Auditing a device for common vulnerabilities
-   Proactively monitoring a device for suspicious activity such as unauthorised logins, brute-force attacks or privilege escalations
-   Visualising complex data and events into neat and trendy graphs
-   Recording a device's normal operating behaviour to help with detecting anomalies
Created in 2015, [Wazuh](https://wazuh.com/) is an open-source, freely available and extensive EDR solution. It can be used in all scales of environments. Wazuh operates on a management and agent module. Simply, a device is dedicated to running Wazuh named a manager, where Wazuh operates on a management and agent model where the manager is responsible for managing agents installed on the devices you’d like to monitor. Let's look at this model in the diagram below:
_We can see logs from three Agents being sent to the Wazuh server._
When was Wazuh released?
*2015*
What is the term that Wazuh calls a device that is being monitored for suspicious activity and potential security threats?
*agent*
Lastly, what is the term for a device that is responsible for managing these devices?
These people manage employees within a workplace
*manager*
### Required: Deploy Wazuh Server
[Connect](https://tryhackme.com/access) to the TryHackMe network and deploy the Wazuh management server attached to this task and wait a **minimum of five minutes** before visiting the Wazuh server on [HTTPS://10.10.219.238](https://10.10.219.238/) . It is **essential** that you prefix the IP address (10.10.219.238) with HTTPS like so: [HTTPS://10.10.219.238](https://10.10.219.238/)
**If you load the Wazuh management server too early, it will say "Kibana Server is not ready yet" Please wait a few more minutes before refreshing the page and trying again.**
Once it has started, log in using the following credentials:
**Username:** wazuh (**make sure that this is lowercase!**)
**Password:** eYa0M1-hG0e7rjGi-lRB2qGYVoonsG1K
Select "**Global Tenant**" after successfully logging in. Refer to the animated gif below of the process if you are stuck.
**Note:** The questions within the tasks of this room **will expect the data stored on this Wazuh management server**, so it is vital that you are able to connect to this server before continuing.
The Wazuh management server in this room will show the agents as being _disconnected_ - this is expected.
Kibana es un software de panel de visualización de datos disponible en la fuente para Elasticsearch, cuyo sucesor gratuito y de código abierto en OpenSearch es OpenSearch
### Wazuh Agents
Devices that record the events and processes of a system are called agents. Agents monitor the processes and events that take place on the device, such as authentication and user management. Agents will offload these logs to a designated collector for processing, such as Wazuh.
In order for Wazuh to be populated, agents need to be installed onto devices to log such events. Wazuh can guide you through the agent deployment process provided you fill out some pre-requisites such as::
-   Operating System
-   The address of the Wazuh server that the agent should send logs to (this can be a DNS entry or an IP address)
-   What group the agent will be under - you can sort agents into groups within Wazuh if you wish
This wizard can be launched by navigating to the following location on the Wazuh server: **Wazuh -> Agents -> Deploy New Agent** as illustrated in this screenshot below:
Domain Name System (DNS) is the protocol responsible for resolving hostnames, such as tryhackme.com, to their respective IP addresses.
Once you navigate to this display, the intuitive wizard will be available to you. I have shared screenshots of using the wizard to install Wazhur's agent on both Windows and Debian/Ubuntu. At stage 4, you are given a command to copy and paste to your clipboard which will install & configure the agent on the device that you wish to collect logs from.
**Installing the Wazuh agent on Windows:**
Invoke-WebRequest -Uri https://packages.wazuh.com/4.x/windows/wazuh-agent-4.2.5-1.msi -OutFile wazuh-agent-4.2.5.msi; ./wazuh-agent-4.2.5.msi /q WAZUH_MANAGER='wazuh.thm' WAZUH_REGISTRATION_SERVER='wazuh.thm' WAZUH_AGENT_GROUP='default'
**Installing the Wazuh agent on Debian/Ubuntu:**
Answer the questions below
Ensure that you are logged in to the Wazuh management server on [HTTPS://10.10.219.238](https://10.10.219.238/)
Completed
Navigate to the "Agents" tab by pressing **Wazuh** -> **Agents**
Completed
How many agents does this Wazuh management server manage?
*2*
What are the status of the agents managed by this Wazuh management server?
*Disconnected*

## Enumeration
Wazuh features a reporting module that allows you to view a summarised breakdown of events that have occurred on an agent.
First, we will need to select a view to generate reports from. In this example, I want to generate a report of the security events in the last 24 hours. To do so, I will need to open the view: **1. Modules -> 2. Security Events**
Now, if there have been alerts within the last 24 hours, I can generate a report like so:
**Note:** If this button is greyed out, there is no report data, so you will either need to change your query or extend the date range.
The report **may** take between a couple of seconds to a few minutes to generate (depending on the amount of data needed to be processed). After allowing some time, we will navigate to the report overview dashboard within Wazuh.
First, press on the "Wazuh" heading at the top of the screen and select "**Management**", and then click on the "**Reporting**" text located under the "**Status and Reports**" sub-heading:
The report overview dashboard lists all generated reports. To download a report, press the save icon on the right of the report located under the "**Actions**" heading.
Answer the questions below
Use Wazuh's "Report" feature to generate a report of an agent.
Completed
Navigate to the [Wazuh "Report" dashboard](https://10.10.219.238/app/wazuh#/manager/?tab=reporting)
Completed
Analyse the report. What is the name of the agent that has generated the most alerts?
![[Pasted image 20221213132304.png]]
*agent-001*
### Loading Sample Data
The Wazuh management server comes with sample data bundled with the installation that can be loaded at your convenience. I have not enabled this by default to improve the performance of the server. However, if you wish to import much more data to showcase the extensibility of Wazuh further, follow the steps below. Navigate to the module to load the sample data:
1.  Open the "**Wazuh"** tab in the heading.
2.  Highlight over "**Settings".**
3.  Select the "**Sample Data"** heading.
4.  Press the "**Add Data**" button on the respective three cards to import the data.
-   Note that this may take up to a minute for each. Refer to this animated picture below for example. The data will have successfully imported when the button on the card says "Remove data"
Return to the Wazuh dashboard to see the newly imported data. For example, we can now see that the "Security Events" module has a tonne more data for us to explore.
**Please note** that you will need to play with the date range. The absolute minimum required to show the sample will need to be Last 7 days+ and refresh the dashboard for this to apply.
Answer the questions below
I've imported the sample data!
Completed
I have played around with the sample data.
https://10.10.219.238/reports/wazuh-overview-general-1670956832.pdf
![[Pasted image 20221213134152.png]]

## Exploitation
Wazuh’s Vulnerability Assessment module is a powerful tool that can be used to periodically scan an agent's operating system for installed applications and their version numbers.
Once this information has been gathered, it is sent back to the Wazuh server and compared against a database of CVEs to discover potential vulnerabilities. For example, the agent in the screenshot below has a version of Vim that is vulnerable to **CVE-2019-12735**.  https://www.exploit-db.com/exploits/46973
The vulnerability scanner module will perform a full scan when the Wazuh agent is first installed on a device and **must** be configured to run at a set interval then after (by default, this is set to 5 minute intervals when enabled) like so:
_Configuring the Wazuh management server to audit agents for vulnerabilities frequently (/var/ossec/etc/ossec.conf)_
Linux is a command line operating system based on unix. There are multiple operating systems that are based on Linux.
Wazuh is capable of testing an agent's configuration against certain rulesets to check for compliance. However, out of the box, it is arguably sensitive. Take, for example, this Linux host running the Wazuh agent. There have been a total of 769 events occurring that the system performs as part of its daily maintenance
These frequent actions, such as removing files, are often detected as a security event. These events and the related severities are determined by Wazuh's rulesets, which is something that we will come on to explore adjusting in another task.
We can analyze these events individually by selecting the event's dropdown. You can sort events based upon various factors such as timestamp, tactics, or description.
Answer the questions below
Ensure that you are logged in to the Wazuh management server on [HTTPS://10.10.219.238](https://10.10.219.238/)
Completed
Navigate to the Agents tab by pressing **Wazuh** -> **Agents** like so
Completed
Select the agent named "**AGENT-001**"
Completed
How many "Security Event" alerts have been generated by the agent "AGENT-001"?
**Note**: You will need to make sure that your time range includes the 11th of March 2022
![[Pasted image 20221213115900.png]]
*196*
### Wazuh Policy Auditing
Wazuh is capable of auditing and monitoring an agent's configuration whilst proactively recording event logs. When the Wazuh agent is installed, an audit is performed where a metric is given using multiple frameworks and legislations such as NIST, MITRE and GDPR.
For example, see how this agent DC-01 scores against MITRE, NIST, and SCA:
El Reglamento General de Protección de Datos es el reglamento europeo relativo a la protección de las personas físicas en lo que respecta al tratamiento de sus datos personales y a la libre circulación de estos datos.
These frameworks are outlined in the [Pentesting Fundamentals](https://tryhackme.com/room/pentestingfundamentals) room if you wish to learn more about them.
Wazuh presents a broad illustration of the logs. We can use the visualizations to break down this data and explore it further. Let's do this with the same agent. For example, see the benchmark for this domain controller running on a windows server:
Answer the questions below
Ensure that you are logged in to the Wazuh management server on [10.10.219.238](https://tryhackme.com/room/MACHINE_IP%20target=)
Completed
Navigate to the "Modules" tab by pressing **Wazuh** -> **Modules** and open the "Policy Management" module like so:
![](https://assets.tryhackme.com/additional/wazuh/navigate5.png)
Completed
### Monitoring Logons with Wazuh
Wazuh's security event monitor is capable to actively record both successful and unsuccessful authentication attempts. The rule with an id of 5710 detects attempted connections that are unsuccessful for the SSH protocol. Let's look at this animated picture below as an example.
The alert was created because someone tried to log onto the agent "**ip-10-10-73- 118**" with the user "**cmnatic**" which does not exist. I have summarized this alert into the table below:
**Field**
**Value**
**Description**
agent.ip
10.10.73.118
This is the IP address of the agent that the alert was triggered on.
agent.name
ip-10-10-73-118
This is the hostname of the agent that the alert was triggered on.
rule.description
sshd: Attempt to login using a non-existent user
This field is a brief description of what the event is alerting to.
rule.mitre.technique
Brute-Force
This field explains the MITRE technique that the alert pertains to.
rule.mitre.id
T1110
This field is the MITRE ID of the alert
rule.id
5710
This field is the ID assigned to the alert by Wazuh's ruleset
location
/var/log/auth.log
This field is the location of the file that the alert was generated from on the agent. In this example, it is the authentication log on the linux agent.
For reference, this alert is stored in a specific file on the Wazuh management server: `/var/ossec/logs/alerts/alerts.log`. We can use a command such as grep or nano to search through this file on the management server manually.
Viewing the Wazuh logon alert log for a login session (su) on the root account by the ubuntu user
```shell-session
ubuntu@wazuh-server:~$ sudo less /var/ossec/logs/alerts/alerts.log
** Alert 1634284538.566764: - pam,syslog,authentication_success,pci_dss_10.2.5,gpg13_7.8,gpg13_7.9,gdpr_IV_32.2,hipaa_164.312.b,ni>
2021 Oct 15 07:55:38 ip-10-10-218-190->/var/log/auth.log
Rule: 5501 (level 3) -> 'PAM: Login session opened.'
User: root
Oct 15 07:55:37 ip-10-10-218-190 sudo: pam_unix(sudo:session): session opened for user root by ubuntu(uid=0)
uid: 0
```
Looking at the animated gif below, we can see how Wazuh has created an alert for successful login to a Window's server running the Wazuh agent. Because this attempt was successful, the severity of the alert is considered less than that of an unsuccessful login. This can, of course, be tailored to your environment. For example, if a user infrequently used is logged on, you can configure Wazuh to list this alert with higher severity.
The animated gif below shows the number of Windows agent events/alerts triggered to show how many times a user has logged on. . In this case, it narrows down the total logon events of **285** to **79**.
Answer the questions below
Ensure that you are logged in to the Wazuh management server on [10.10.229.53](https://tryhackme.com/room/10.10.229.53%20target=)
Completed
Navigate to the "Management" tab by pressing Wazuh -> **Management** and open the "Rules" module like so:
![](https://assets.tryhackme.com/additional/wazuh/rules2.png)
Completed
### Collecting Windows Logs with Wazuh
All sorts of actions and events are captured and recorded on a Windows operating system. This includes authentication attempts, networking connections, files that were accessed, and the behaviours of applications and services. This information is stored in the Windows event log using a tool called Sysmon.
We can use the Wazuh agent to aggregate these events recorded by _Sysmon_ for processing to the Wazuh manager. Now, we will need to configure both the Wazuh agent and the Sysmon application.  Sysmon uses rules that are made in XML formatting to be triggered. For example, in the XML snippet below, we are telling Sysmon to monitor for the event of the powershell.exe process starting.
A Sysmon configuration file for monitoring the Powershell process
```shell-session
Sysmon schemaversion="3.30" 
         HashAlgorithms md5 /HashAlgorithms 
  EventFiltering 
  !--SYSMON EVENT ID 1 : PROCESS CREATION-- 
  ProcessCreate onmatch="include" 
  Image condition="contains" powershell.exe /Image 
  /ProcessCreate 
  !--SYSMON EVENT ID 2 : FILE CREATION TIME RETROACTIVELY CHANGED IN THE FILESYSTEM-- 
  FileCreateTime onmatch="include"  /FileCreateTime 
  !--SYSMON EVENT ID 3 : NETWORK CONNECTION INITIATED-- 
  NetworkConnect onmatch="include"  /NetworkConnect 
  !--SYSMON EVENT ID 4 : RESERVED FOR SYSMON STATUS MESSAGES, THIS LINE IS INCLUDED FOR DOCUMENTATION PURPOSES ONLY-- 
  !--SYSMON EVENT ID 5 : PROCESS ENDED-- 
  ProcessTerminate onmatch="include"  /ProcessTerminate 
  !--SYSMON EVENT ID 6 : DRIVER LOADED INTO KERNEL-- 
  DriverLoad onmatch="include"  /DriverLoad  
  !--SYSMON EVENT ID 7 : DLL (IMAGE) LOADED BY PROCESS-- 
  ImageLoad onmatch="include"  /ImageLoad 
  !--SYSMON EVENT ID 8 : REMOTE THREAD CREATED-- 
  CreateRemoteThread onmatch="include"  /CreateRemoteThread 
  !--SYSMON EVENT ID 9 : RAW DISK ACCESS-- 
  RawAccessRead onmatch="include"  /RawAccessRead  
  !--SYSMON EVENT ID 10 : INTER-PROCESS ACCESS-- 
  ProcessAccess onmatch="include"  /ProcessAccess 
  !--SYSMON EVENT ID 11 : FILE CREATED-- 
  FileCreate onmatch="include"  /FileCreate 
  !--SYSMON EVENT ID 12 & 13 & 14 : REGISTRY MODIFICATION-- 
  RegistryEvent onmatch="include"  /RegistryEvent 
  !--SYSMON EVENT ID 15 : ALTERNATE DATA STREAM CREATED-- 
  FileCreateStreamHash onmatch="include"  /FileCreateStreamHash  
  PipeEvent onmatch="include"  /PipeEvent 
  /EventFiltering 
 /Sysmon
```
To instruct Sysmon to do, we need to execute the Sysmon application and provide the aforementioned configuration file like so: `Sysmon64.exe -accepteula -i detect_powershell.xml`
We can verify that Sysmon has accepted our configuration file by navigating to the Event Viewer and searching for the “**Sysmon**” module like so:
Let’s launch a powershell prompt on the Windows Server and return to our Event Viewer. We can now see a record of this powershell prompt being opened, kept within the Event Viewer.
Now we will need to configure the Wazuh agent on this Window Server to instruct it to send these events to the Wazuh management server. To do so, we need to open the Wazuh agent file located at: `C:\Program Files (x86)\ossec-agent\ossec.conf`
To include the following snippet:
Configuring the Wazuh Agent's configuration
```shell-session
<localfile>
<location>Microsoft-Windows-Sysmon/Operational</location>
<log_format>eventchannel</log_format>
</localfile>
```
Looking like so:
