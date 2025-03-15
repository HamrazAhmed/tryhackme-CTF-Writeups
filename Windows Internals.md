---
Learn and understand the fundamentals of how Windows operates at its core.
---

# Windows Internals — Writeup

## Overview
### Windows Internals — Writeup
### Windows Internals — Writeup
![|333](https://tryhackme-images.s3.amazonaws.com/room-icons/63e02272331034b6606214960298c271.png)
### Introduction
Operating systems have a lot more technology and architecture behind them than we may see at first. In this room, we will be observing the Windows operating systems and common internal components.
Learning Objectives
Understand and interact with Windows processes and their underlying technologies.
Learn about core file formats and how they are used.
Interact with Windows internals and understand how the Windows kernel operates.
With Windows machines making up a majority of corporate infrastructure, red teams need to understand Windows internals and how they can be (ab)used. The red team can (ab)use Windows to aid in evasion and exploitation when crafting offensive tools or exploits.
Before beginning this room, familiarize yourself with basic Windows usage and functionality. Basic programming knowledge in C++ and PowerShell is also recommended but not required.
We have provided a base Windows machine with the files needed to complete this room. You can access the machine in-browser or through RDP using the credentials below.
Machine IP: MACHINE_IP             Username: THM-Attacker             Password: Tryhackme!
This is going to be a lot of information. Please buckle your seatbelts and locate your nearest fire extinguisher.
### Processes
A process maintains and represents the execution of a program; an application can contain one or more processes. A process has many components that it gets broken down into to be stored and interacted with. The Microsoft docs break down these other components, "Each process provides the resources needed to execute a program. A process has a virtual address space, executable code, open handles to system objects, a security context, a unique process identifier, environment variables, a priority class, minimum and maximum working set sizes, and at least one thread of execution." This information may seem intimidating, but this room aims to make this concept a little less complex.
As previously mentioned, processes are created from the execution of an application. Processes are core to how Windows functions, most functionality of Windows can be encompassed as an application and has a corresponding process. Below are a few examples of default applications that start processes.
MsMpEng (Microsoft Defender)
wininit (keyboard and mouse)
lsass (credential storage)
Attackers can target processes to evade detections and hide malware as legitimate processes. Below is a small list of potential attack vectors attackers could employ against processes,
Process Injection (TI055) https://attack.mitre.org/techniques/T1055/
Process Hollowing (TI055.012) https://attack.mitre.org/techniques/T1055/012/
Process Masquerading (TI055.013) https://attack.mitre.org/techniques/T1055/013/
Processes have many components; they can be split into key characteristics that we can use to describe processes at a high level. The table below describes each critical component of processes and their purpose.
Process Component
Purpose
Private Virtual Address Space
Virtual memory addresses that the process is allocated.
Executable Program
Defines code and data stored in the virtual address space.
Open Handles
Defines handles to system resources accessible to the process.
Security Context
The access token defines the user, security groups, privileges, and other security information.
Process ID
Unique numerical identifier of the process.
Threads
Section of a process scheduled for execution.
We can also explain a process at a lower level as it resides in the virtual address space. The table and diagram below depict what a process looks like in memory.
Component
Purpose
Code
Code to be executed by the process.
Global Variables
Stored variables.
Process Heap
Defines the heap where data is stored.
Process Resources
Defines further resources of the process.
Environment Block
Data structure to define process information.
This information is excellent to have when we get deeper into exploiting and abusing the underlying technologies, but they are still very abstract. We can make the process tangible by observing them in the Windows Task Manager. The task manager can report on many components and information about a process. Below is a table with a brief list of essential process details.
Value/Component
Purpose
Example
Name
Define the name of the process, typically inherited from the application
conhost.exe
PID
Unique numerical value to identify the process
7408
Status
Determines how the process is running (running, suspended, etc.)
Running
User name
User that initiated the process. Can denote privilege of the process
SYSTEM
These are what you would interact with the most as an end-user or manipulate as an attacker.
There are multiple utilities available that make observing processes easier; including Process Hacker 2, Process Explorer, and Procmon.
Processes are at the core of most internal Windows components. The following tasks will extend the information about processes and how they're used in Windows.
Open the provided file: "Logfile.PML" in Procmon and answer the questions below.
*No answer needed*
![[Pasted image 20220910235717.png]]
What is the process ID of "notepad.exe"? You can filter by the process name in Procmon.
*5984*
![[Pasted image 20220910235817.png]]
What is the parent process ID of the previous process? Found in the event properties of the process.
*3412*
What is the integrity level of the process? Found in the Process tab of the event properties.
*High*
### Threads
﻿A thread is an executable unit employed by a process and scheduled based on device factors.
Device factors can vary based on CPU and memory specifications, priority and logical factors, and others.
We can simplify the definition of a thread: "controlling the execution of a process."
Since threads control execution, this is a commonly targeted component. Thread abuse can be used on its own to aid in code execution, or it is more widely used to chain with other API calls as part of other techniques.
Threads share the same details and resources as their parent process, such as code, global variables, etc. Threads also have their unique values and data, outlined in the table below.
Component	Purpose
Stack
All data relevant and specific to the thread (exceptions, procedure calls, etc.)
Thread Local Storage
Pointers for allocating storage to a unique data environment
Stack Argument
Unique value assigned to each thread
Context Structure
Holds machine register values maintained by the kernel
Threads may seem like bare-bones and simple components, but their function is critical to processes.
Open the provided file: "Logfile.PML" in Procmon and answer the questions below.
![[Pasted image 20220910235926.png]]
What is the thread ID of the first thread created by notepad.exe?
Listed as the operation Thread Create.
*5908*
![[Pasted image 20220911000217.png]]
What is the stack argument of the previous thread?
Listed as Thread in the event properties.
*6584*
### Virtual Memory
Virtual memory is a critical component of how Windows internals work and interact with each other. Virtual memory allows other internal components to interact with memory as if it was physical memory without the risk of collisions between applications. The concept of modes and collisions is explained further in task 8.
Virtual memory provides each process with a [private virtual address space](https://docs.microsoft.com/en-us/windows/win32/memory/virtual-address-space). A memory manager is used to translate virtual addresses to physical addresses. By having a private virtual address space and not directly writing to physical memory, processes have less risk of causing damage.
The memory manager will also use pages or transfers to handle memory. Applications may use more virtual memory than physical memory allocated; the memory manager will transfer or page virtual memory to the disk to solve this problem. You can visualize this concept in the diagram below.
The theoretical maximum virtual address space is 4 GB on a 32-bit x86 system.
This address space is split in half, the lower half (0x00000000 - 0x7FFFFFFF) is allocated to processes as mentioned above. The upper half (0x80000000 - 0xFFFFFFFF) is allocated to OS memory utilization. Administrators can alter this allocation layout for applications that require a larger address space through settings (increaseUserVA) or the [AWE](https://docs.microsoft.com/en-us/windows/win32/memory/address-windowing-extensions) (Address Windowing Extensions).
The theoretical maximum virtual address space is 256 TB on a 64-bit modern system.
The exact address layout ratio from the 32-bit system is allocated to the 64-bit system.
Most issues that require settings or AWE are resolved with the increased theoretical maximum.
You can visualize both of the address space allocation layouts to the right.
Although this concept does not directly translate to Windows internals or concepts, it is crucial to understand. If understood correctly, it can be leveraged to aid in abusing Windows internals.
Read the above and answer the questions below.
*No answer needed*
What is the total theoretical maximum virtual address space of a 32-bit x86 system?
*4 gb*
![[Pasted image 20220911000439.png]]
What default setting flag can be used to reallocate user process address space?
*increaseuserva*
Open the provided file: "Logfile.PML" in Procmon and answer the questions below.
*No answer needed*
![[Pasted image 20220911000650.png]]
What is the base address of "notepad.exe"?
Listed as the operation Load Image.
*0x7ff652ec0000*
### Dynamic Link Libraries
The [Microsoft docs](https://docs.microsoft.com/en-us/troubleshoot/windows-client/deployment/dynamic-link-library#:~:text=A%20DLL%20is%20a%20library,common%20dialog%20box%20related%20functions.) describe a DLL as "a library that contains code and data that can be used by more than one program at the same time."
DLLs are used as one of the core functionalities behind application execution in Windows. From the [Windows documentation](https://docs.microsoft.com/en-us/troubleshoot/windows-client/deployment/dynamic-link-library#:~:text=A%20DLL%20is%20a%20library,common%20dialog%20box%20related%20functions.), "The use of DLLs helps promote modularization of code, code reuse, efficient memory usage, and reduced disk space. So, the operating system and the programs load faster, run faster, and take less disk space on the computer."
When a DLL is loaded as a function in a program, the DLL is assigned as a dependency. Since a program is dependent on a DLL, attackers can target the DLLs rather than the applications to control some aspect of execution or functionality.
DLL Hijacking (T1574.001) https://attack.mitre.org/techniques/T1574/001/
DLL Side-Loading (T1574.002) https://attack.mitre.org/techniques/T1574/002/
DLL Injection (T1055.001) https://attack.mitre.org/techniques/T1055/001/
DLLs are created no different than any other project/application; they only require slight syntax modification to work. Below is an example of a DLL from the Visual C++ Win32 Dynamic-Link Library project.
DLLs are created no different than any other project/application; they only require slight syntax modification to work. Below is an example of a DLL from the Visual C++ Win32 Dynamic-Link Library project.
```text
#include "stdafx.h"
#define EXPORTING_DLL
#include "sampleDLL.h"
BOOL APIENTRY DllMain( HANDLE hModule, DWORD ul_reason_for_call, LPVOID lpReserved
)
{
    return TRUE;
}

void HelloWorld()
{
    MessageBox( NULL, TEXT("Hello World"), TEXT("In a DLL"), MB_OK);
}
```
Below is the header file for the DLL; it will define what functions are imported and exported. We will discuss the header file's importance (or lack of) in the next section of this task.
```text
#ifndef INDLL_H
    #define INDLL_H
    #ifdef EXPORTING_DLL
        extern __declspec(dllexport) void HelloWorld();
    #else
        extern __declspec(dllimport) void HelloWorld();
    #endif

#endif
```
The DLL has been created, but that still leaves the question of how are they used in an application?
DLLs can be loaded in a program using load-time dynamic linking or run-time dynamic linking.
When loaded using load-time dynamic linking, explicit calls to the DLL functions are made from the application. You can only achieve this type of linking by providing a header (.h) and import library (.lib) file. Below is an example of calling an exported DLL function from an application.
```text
#include "stdafx.h"
#include "sampleDLL.h"
int APIENTRY WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
    HelloWorld();
    return 0;
}
```
When loaded using run-time dynamic linking, a separate function (LoadLibrary or LoadLibraryEx) is used to load the DLL at run time. Once loaded, you need to use GetProcAddress to identify the exported DLL function to call. Below is an example of loading and importing a DLL function in an application.
```text
...
typedef VOID (*DLLPROC) (LPTSTR);
...
HINSTANCE hinstDLL;
DLLPROC HelloWorld;
BOOL fFreeDLL;

hinstDLL = LoadLibrary("sampleDLL.dll");
if (hinstDLL != NULL)
{
    HelloWorld = (DLLPROC) GetProcAddress(hinstDLL, "HelloWorld");
