# OWASP Broken Access Control — Writeup

## Overview
### OWASP Broken Access Control — Writeup
### OWASP Broken Access Control — Writeup
----
Exploit Broken Access Control: Number 1 of the Top 10 web security risks.
----
Broken access controls are a type of security vulnerability that arises when an application or system fails to properly restrict access to sensitive data or functionality. This vulnerability allows attackers to gain unauthorized access to resources that should be restricted, such as user accounts, files, databases, or administrative functions. Broken access controls can occur due to a variety of factors, including poor design, configuration errors, or coding mistakes.
1. Understand what Broken Access Control is and its impact.
2. Identify Broken Access Control vulnerabilities in web applications.
3. Exploit these vulnerabilities in a controlled environment.
4. Understand and apply measures to mitigate and prevent these vulnerabilities.
### Pre-requisites:
1. Basic understanding of JSON, web applications, and HTTP protocols.
2. Familiarity with scripting languages such as PHP and JavaScript.
3. Knowledge of web application security standards and frameworks such as [OWASP Top 10](https://tryhackme.com/room/owasptop102021).
4. Basic understanding and usage of a proxy tool like [Burp Suite](https://tryhackme.com/room/burpsuiterepeater).
Answer the questions below
Click me to proceed onto the next task.
Completed
### Task 2  Broken Access Control Introduction
### What is Access Control?
Access control is a security mechanism used to control which users or systems are allowed to access a particular resource or system. Access control is implemented in computer systems to ensure that only authorized users have access to resources, such as files, directories, databases, and web pages. The primary goal of access control is to protect sensitive data and ensure that it is only accessible to those who are authorized to access it.
Access control can be implemented in different ways, depending on the type of resource being protected and the security requirements of the system. Some common access control mechanisms include:
1. **Discretionary Access Control (DAC)**: In this type of access control, the resource owner or administrator determines who is allowed to access a resource and what actions they are allowed to perform. DAC is commonly used in operating systems and file systems. In layman’s terms, imagine a castle where the king can give keys to his advisors, allowing them to open any doors they like, whenever they want. That’s DAC for you. It’s the liberty to control access to your own resources. The one in charge, like the king of the castle, can hand out permissions to whomever they please, dictating who can come in and out.
2. **Mandatory Access Control (MAC)**: In this type of access control, access to resources is determined by a set of predefined rules or policies that are enforced by the system. MAC is commonly used in highly secure environments, such as government and military systems. In layman’s terms, picture a fort with an iron-clad security protocol. Only specific individuals with particular security clearances can access certain areas, and this is non-negotiable. The high commander sets the rules, and they are rigorously followed. That’s how MAC works. It’s like the stern security officer who allows no exceptions to the rule.
3. **Role-Based Access Control (RBAC)**: In this type of access control, users are assigned roles that define their level of access to resources. RBAC is commonly used in enterprise systems, where users have different levels of authority based on their job responsibilities. In layman’s terms, imagine a modern corporation. You have your managers, your executives, your sales staff, etc. They each have different access to the building. Some can enter the boardroom, others can access the sales floor, and so on. That’s the essence of RBAC - assigning access based on a person’s role within an organization.
4. **Attribute-Based Access Control (ABAC)**: In this type of access control, access to resources is determined by a set of attributes, such as user role, time of day, location, and device. ABAC is commonly used in cloud environments and web applications. In layman’s terms, think of a highly advanced sci-fi security system that scans individuals for certain attributes. Maybe it checks whether they’re from a particular planet, whether they’re carrying a specific device, or if they’re trying to access a resource at a specific time. That’s ABAC. It’s like the smart, flexible security of the future.
Implementing access control can help prevent security breaches and unauthorized access to sensitive data. However, access control is not foolproof and can be vulnerable to various types of attacks, such as privilege escalation and broken access control vulnerabilities. Therefore, it is important to regularly review and test access control mechanisms to ensure that they are working as intended.
### Broken Access Control:
Broken access control vulnerabilities refer to situations where access control mechanisms fail to enforce proper restrictions on user access to resources or data. Here are some common exploits for broken access control and examples:
1. **Horizontal privilege escalation** occurs when an attacker can access resources or data belonging to other users with the same level of access. For example, a user might be able to access another user’s account by changing the user ID in the URL.
2. **Vertical privilege escalation** occurs when an attacker can access resources or data belonging to users with higher access levels. For example, a regular user can access administrative functions by manipulating a hidden form field or URL parameter.
3. **Insufficient access control checks** occur when access control checks are not performed correctly or consistently, allowing an attacker to bypass them. For example, an application might allow users to view sensitive data without verifying their proper permissions.
4. **Insecure direct object references** occur when an attacker can access a resource or data by exploiting a weakness in the application’s access control mechanisms. For example, an application might use predictable or easily guessable identifiers for sensitive data, making it easier for an attacker to access. You may refer to this [room](https://tryhackme.com/room/owasptop102021) in **Task #4** to learn more about this.
These exploits can be prevented by implementing strong access control mechanisms and regularly reviewing and testing them to ensure they are functioning as intended.
Answer the questions below
What is IDOR?
*Insecure direct object references*
What occurs when an attacker can access resources or data belonging to other users with the same level of access?
*Horizontal privilege escalation*
What occurs when an attacker can access resources or data from users with higher access levels?
*Vertical privilege escalation*
What is ABAC?
*Attribute-Based Access Control*
What is RBAC?
*Role-Based Access Control*
### Task 3  Deploy the Machine
Start Machine
To focus on learning about the Broken Access Controls, please click on the `Start Machine` button located in the upper-right-hand corner of this task to deploy the virtual machine for this room.
After obtaining the machine’s generated IP address, you can either use our AttackBox or use your own VM connected to TryHackMe’s VPN to begin the attack. If you prefer to use the AttackBox, you can simply click on the `Start AttackBox` button located above the room name.
After starting the AttackBox or connecting your attack VM to TryHackMe’s VPN, you can now start accessing the target website application by entering **http://MACHINE_IP/** into the browser.
_Keep in mind that the machine may take up to **5 minutes** to spawn._
Answer the questions below
I have deployed the machine attached to the task.
Completed
### Task 4  Assessing the Web Application
In this task, our objective is to gain a comprehensive understanding of the web application’s functionalities. This will allow us to make the most of the application’s capabilities and achieve our desired outcomes.
### Assessing the Application:
When you browse a web application as a penetration tester, imagine what the underlying code looks like and what vulnerabilities come to mind for each functionality, request, and response.
The web application for this room features a Dashboard, Login, and Registration form that enables users to access the dashboard of the website. From a web app pentester standpoint, the pentester will usually register an account. After the registration, the pentester will then try to check the login function for any access control vulnerabilities.
Below are the screenshots of each webpage:
**Registration:**
**Login:**
**Dashboard:**
In order for us to capture the HTTP requests being sent to the server, we can use [OWASP ZAP](https://www.zaproxy.org/) or Burp Suite Community Edition.
To learn more about the detailed usage of Burp Suite and its functionalities, you may refer to the [Burp Suite Module](https://tryhackme.com/module/learn-burp-suite).
### Capturing the HTTP traffic
In order for us to further analyze the requests and responses being sent and received from the server, we will use the **“Proxy”** module of Burp Suite to capture the HTTP traffic that is being sent to the server. The captured HTTP traffic can be used with the other modules of Burp Suite.
These can then be manipulated or sent to other tools, such as **“Repeater”**, for further processing before being allowed to continue to their destination.
Below is the captured HTTP traffic that is being sent to `functions.php` after login.
Based on the screenshot displayed above, we can observe that upon completing the login process, the web application will give us a JSON response that contains the status, message, first_name, last_name, is_admin, and redirect_link which the server uses to redirect the user to the `dashboard.php` with the parameter “isadmin” in the URL.
### Understanding the content of the HTTP request and response:
- The target web application does not have any implemented security headers, which indicates that there are no preventative measures (like a first line of defense) in place to protect the web application against certain types of attacks.
- The target web application is running on a Linux operating system (`Debian`) and is using Apache web server (`Apache/2.4.38`). This information can be useful in identifying potential security vulnerabilities that may exist in the target web application.
- The target web application utilizes `PHP/8.0.19` as its backend programming language. This information is important for understanding the technology stack of the application and identifying potential security vulnerabilities or compatibility issues that may arise with other software components.
- The target web application redirects the user to the dashboard with a parameter that we can possibly test for privilege escalation vulnerabilities.
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.43.212 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
🌍HACK THE PLANET🌍

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.43.212:22
Open 10.10.43.212:80
Open 10.10.43.212:443
Open 10.10.43.212:3306
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org )
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Initiating Parallel DNS resolution of 1 host.
Completed Parallel DNS resolution of 1 host.
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.43.212 [4 ports]
Discovered open port 3306/tcp on 10.10.43.212
Discovered open port 22/tcp on 10.10.43.212
Discovered open port 80/tcp on 10.10.43.212
Discovered open port 443/tcp on 10.10.43.212
Completed Connect Scan (4 total ports)
Initiating Service scan
Scanning 4 services on 10.10.43.212
Completed Service scan (4 services on 1 host)
NSE: Script scanning 10.10.43.212.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.43.212
Host is up, received user-set (0.18s latency).

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 aeed1f4af4179eced83e0fcb203af9f4 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDMqEnYcxtOMr3o7KFvkC/gs1N+rmqDi2zRY96uux++t50kHep+eCVz2g9ottj0mDqbJfal9E5/I6QFgv4YpImR9uI5iD6g9CnrG+fTyj6ishJmIz91r+i/TdE0I93sEoj8O4/JhTb0lqDAMig0Ujc0OowXUwGDHk1crjutWsFGM04z1fvKz8cqGpbPL9a+8qwTI9BHHG8RDxAm4bt0WxBdn3a0jKGBpO/varyoEwYBs4FIiyDnIWdXYBjgzGSkemWFIyfjA6poTn5X8ahsUyB9u966OS21miCPg3lO9XqTrODq+lTEKDputXeXr2+xiPai1Im7wz5TDwN8Ugzrf8F3IKO/6YqlN+E5Rs7XvlvKtt1+dzNIupFSpaksIgWBrvH2MVs4kIptOHuQCsLEUJgbtnxcs30Paa3U+4bAfCmzK0h2Qh9YJIeixojtt0PG1pdTx3YCTkX4vh40obuS8uI0jFsBFlFTYMRA++Z+3njpHDfQdEPuVb0Te77gaJgydmU=
|   256 5dbdc35d880b6efb10570427af799130 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBMFBmL6L1aO0LsYpGr7d7TwRUXuDzZ6vXzBTHbGKmOb0nD2O7n3SNUYWVl/VJpDaLWVIeCRr3098U8RaRBbgFFU=
|   256 a4041e6b1c0bf7b8ecf226ef22820591 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJv4fOpcujX7nG9BQqmygYK5oHJa4G7qQQ32XsbEuzIO
80/tcp   open  http    syn-ack Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Welcome to VulnerableApp
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
443/tcp  open  http    syn-ack Apache httpd 2.4.38
|_http-server-header: Apache/2.4.38 (Debian)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: Welcome to VulnerableApp
3306/tcp open  mysql   syn-ack MySQL 8.0.32
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=MySQL_Server_8.0.32_Auto_Generated_Server_Certificate
| Issuer: commonName=MySQL_Server_8.0.32_Auto_Generated_CA_Certificate
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| MD5:   08c7c59f2eb6f8116697738a91656971
| SHA-1: ad22fc9dcb5a2b64b42e6ca4d2c12b552e739895
| -----BEGIN CERTIFICATE-----
| MIIDBzCCAe+gAwIBAgIBAjANBgkqhkiG9w0BAQsFADA8MTowOAYDVQQDDDFNeVNR
| TF9TZXJ2ZXJfOC4wLjMyX0F1dG9fR2VuZXJhdGVkX0NBX0NlcnRpZmljYXRlMB4X
| DTIzMDQxMTAyNTk0M1oXDTMzMDQwODAyNTk0M1owQDE+MDwGA1UEAww1TXlTUUxf
| U2VydmVyXzguMC4zMl9BdXRvX0dlbmVyYXRlZF9TZXJ2ZXJfQ2VydGlmaWNhdGUw
| ggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDGcSvk6LihXJHB/vEoHREi
