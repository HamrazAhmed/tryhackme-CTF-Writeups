# ret2libc — Writeup

## Overview
### ret2libc — Writeup
### ret2libc — Writeup
----
This room teaches basic return-oriented programming (ROP), exploitation of binaries and an ASLR bypass.
----
**Before we start.**
This room is a bit more advanced. If you are new to binary exploitation, reverse engineering, basics of c programming and scripting with Python, I strongly recommend you do the rooms linked below first to get some essential knowledge.
- [Windows x64 Assembly](https://tryhackme.com/room/win64assembly)
- [Python Basics](https://tryhackme.com/room/pythonbasics)
- [Intro To Pwntools](https://tryhackme.com/room/introtopwntools)
- [Windows Reversing Intro](https://tryhackme.com/room/windowsreversingintro)
Answer the questions below
I know the essentials of binary exploitation and want to continue!
Correct Answer
### Task 2  Introduction
Start Machine
So welcome to the room ret2libc! 😎
Before we start, deploy the machine attached to the task by pressing the green "**Start Machine**" button, as well as the AttackBox if you don't want to bother installing additional tools (using the "**Start AttackBox**" button at the top of the page) or you can use your own machine and connect through OpenVPN.
Keep in mind the booting can take up to **3 minutes**.
And while you wait, let me tell you what return-oriented programming (ROP) is and how the ret2libc attack works.
### **Return oriented programming (ROP)**
- The basis of return-oriented programming is chaining together small chunks of code already present within the binary itself in such a way as to do what we wish. For example, reading flag.txt file, or even better, getting a shell.
### ****ret2libc attack****
- The ret2libc is ROP with a small difference. The difference is that these small chunks of code which we'll be using are in the dynamically linked c library called libc.
- Why do we use libc? Well, it's already linked to our binary, and libc has some of the functions which are interesting to us. One of the functions which are useful to us is called "system" which lets us execute anything passed to it.
- Now, what if I tell you that in libc, there is also a string value that looks like this: "/bin/sh". I think you now know where this is going.
- All we have to do is create an ROP chain (small chunks of code chained together) that passes the "/bin/sh" string as the argument to the system function and then call this function.
And that's it. You now know how the ret2libc attack works.
**If you are done reading, and your machine is ready, use these **ssh credentials** to connect:**
- Username: **andy**
- Password: ****ret2libc!****
Answer the questions below
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ ssh andy@10.10.111.177                          
The authenticity of host '10.10.111.177 (10.10.111.177)' can't be established.
ED25519 key fingerprint is SHA256:5OLk24aNLKtWYiNZ+C1A9J71a2CoNOeBX5YyyGq+KlQ.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.111.177' (ED25519) to the list of known hosts.
andy@10.10.111.177's password: 
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 4.15.0-156-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

 System information disabled due to load higher than 1.0

0 updates can be applied immediately.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

Last login: Sun Sep 12 19:18:45 2021 from 192.168.33.1
andy@ubuntu:~$ ls
exploit_me
andy@ubuntu:~$ file exploit_me
exploit_me: setuid ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=2c771960dddc76d1e69e8f741185d232c7ee6098, not stripped
```
Start the machine!
Completed
What is the name of the function which is essential for ret2libc attack?
*system*
### Task 3  Tools used
Throughout the room, I'll be using listed tools that make the process of binary exploitation and reverse engineering much easier. I'll provide you links to the official documentation of every tool so you can install them on your machine if they aren't already.
**Pwntools and gdb with gef are already preinstalled in the attached VM.**
### **Pwntools**
The first thing on this list is a python library called pwntools, which we'll use for creating our exploit script. Pwntools should already be installed on Kali Linux.
Link (pwntools): [https://docs.pwntools.com/en/stable/install.html](https://docs.pwntools.com/en/stable/install.html)
### **gdb + gef**
The second thing on the list is the debugger, I use gdb with a plugin called gef, but if you are using any other plugin like pwndbg or peda, you should be fine as well. Gdb should be available as a package on your Linux distribution.
Link (gdb): [https://www.sourceware.org/gdb/](https://www.sourceware.org/gdb/)
Link (gef): [https://gef.readthedocs.io/en/master/#setup](https://gef.readthedocs.io/en/master/#setup)
### **Ghidra**
And the last thing on this list is a reverse engineering tool called Ghidra. Ghidra is already installed in the THM Attack box, so if you don't want to bother with downloading it, you can use it there.
Link (ghidra): [https://ghidra-sre.org/](https://ghidra-sre.org/)
Answer the questions below
I understand which tools are used throughout the room, and I am ready to continue!
Correct Answer
### Task 4  Review of the binary
After connecting to the box, go to the andy's home directory. There you should find a binary called exploit_me.
You can see is that the binary is glowing red... hmm. What does that mean? I guess you already know that, but in case you don't, let's check the binary permissions.
`ls -la exploit_me`
You can see there's a setuid bit in place which means we could maybe escalate privileges? (If the binary has a setuid bit set, it means you can run the binary as the owner of this binary). Let's keep this in mind for later and move on.
### Architecture
The next thing we should check is the architecture of the binary, especially if it's a 32-bit or 64-bit executable. We can do that with the file command.
Architecture
```shell-session
andy@ubuntu:~$ file exploit_me
exploit_me: setuid ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=2c771960dddc76d1e69e8f741185d232c7ee6098, not stripped
```
As you can see we're working with a 64-bit binary.
You might ask, why does that matter to us? There are many things we can take from that information, but the crucial section to us is which calling conventions are being used.
In short, calling conventions are a set of rules used, for example, when the program is calling functions or passing parameters.
Later, when we craft our ROP chain, we have to apply these rules so the program can understand our instructions and our exploit script can work without any problems.
Now that we know what the calling conventions are and which architecture is our binary. We just have to find the exact calling convention for our binary. I made it easy for you and already found it on the Wikipedia page [here](https://en.wikipedia.org/wiki/X86_calling_conventions), almost at the bottom.
|   |   |   |   |
|---|---|---|---|
|Architecture|Name|Operating system, compiler|Register order for parameters (arguments)|
|x86-64|System V AMD64|[Solaris](https://en.wikipedia.org/wiki/Solaris_(operating_system)), [Linux](https://en.wikipedia.org/wiki/Linux), [BSD](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution), [macOS](https://en.wikipedia.org/wiki/MacOS), [OpenVMS](https://en.wikipedia.org/wiki/OpenVMS) ([GCC](https://en.wikipedia.org/wiki/GNU_Compiler_Collection), [Intel C++ Compiler](https://en.wikipedia.org/wiki/Intel_C%2B%2B_Compiler), [Clang](https://en.wikipedia.org/wiki/Clang), [Delphi](https://en.wikipedia.org/wiki/Delphi_(IDE)))|RDI, RSI, RDX, RCX, R8, R9, [XYZ]MM0–7|
The table above tells us which architecture this calling convention is, its name, which operating system, and on the right-hand side is the important stuff.
Let's use as an example any c-function that has one argument. Let's say puts, for example. Now let's go over what the last thing in this table tells us. It says that if we want to give some data as the argument to our puts, we first need to move the data into the $RDI register.
If we would have some other function with more arguments, let's say three. For the first argument, we'd use register $RDI, for the second $RSI, and the last one $RDX.
This way, our binary will understand what we want to pass as an argument to the function.
### **Running the binary**
When we run a binary, it prompts us to type our name. When we do that, it prints out our name on the screen.
Running the binary
```shell-session
andy@ubuntu:~$ ./exploit_me
Type your name:
andy
Your name is: andy
```
The first thing that should hit our head when seeing the binary like this in the CTF is if the binary is vulnerable to buffer overflow.
Let's try that by simply writing 30 A's instead of our name.
Buffer overflow
```shell-session
andy@ubuntu:~$ ./exploit_me
Type your name:
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Your name is: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Segmentation fault (core dumped)
```
And as we can see, we got a segmentation fault which means that our binary is vulnerable to a buffer overflow attack.
### **Finding the offset**
The next thing we need to figure out is the offset of this overflow. By offset, I mean the minimum number of A's (bytes) required for the segmentation fault to happen. We can find this in gdb and use a command called pattern, which comes with gef. Open the binary in the gdb with `gdb exploit_me`
Once we have our binary open, we need to generate the pattern that we'll be giving to our binary as an input instead of the  A's that we used earlier. Generate the pattern in gdb with the command `pattern create`
Once you have created the pattern, copy the output (= long text with lots of a's) and then run the binary inside of the gdb simply by typing: `r`
You'll get prompted for the name, so paste our created pattern here and hit enter. You should see values for the registers, the stack etc., from when the segmentation fault occurred, but that's not the important thing here. All we need to do is read the data from the $RSP register and use it in the pattern search command. We can do that easily with `pattern search $rsp`
If you followed me step by step, you should see the offset in the gdb by yourself and keep it in mind because we'll need it for crafting our exploit.
**Note:** If we were working with a 32-bit binary, we'd look for the data for our pattern search in the $RIP register.
### 
### **Protections**
Another important part of reviewing the binary is looking for binary protections. For that, we can use command checksec, which comes preinstalled with **pwntools**.
Binary protections
```shell-session
andy@ubuntu:~$ checksec exploit_me
[*] '/home/andy/exploit_me'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```
I'd like to talk about every protection in-depth but this would make this room even longer than it is, but if you followed my advice and completed room [Intro To Pwntools](https://tryhackme.com/room/introtopwntools), you should have a basic idea of what every protection is doing.
The main things we should take from this:
- The binary has **Partial RELRO,** which means that the **global offset table** is read and writable.
- **Stack canary** isn't found, which means that if there is any buffer overflow, we can simply abuse it.
- **NX** is enabled, which means that we cannot execute custom shellcode from the stack, and it's also the main reason we're using the ret2libc attack.
- **PIE** is disabled, which means that our binary will always start at the address 0x400000 and won't be affected by **ASLR**.
On the next task, we'll discuss the global offset table (GOT), **ASLR** and how it affects our exploitation.
Answer the questions below
```text
andy@ubuntu:~$ ls -lah
total 416K
drwxr-xr-x 5 andy andy 4.0K Sep 12  2021 .
drwxr-xr-x 3 root root 4.0K Sep 12  2021 ..
-rw------- 1 andy andy    1 Sep 12  2021 .bash_history
-rw-rw-r-- 1 andy andy   44 Sep 12  2021 .bash_profile
-rw-rw-r-- 1 andy andy 3.8K Sep 12  2021 .bashrc
drwx------ 3 andy andy 4.0K Sep 12  2021 .cache
-rw-rw-r-- 1 andy andy   34 Sep 12  2021 .gdbinit
-rw-rw-r-- 1 andy andy 368K Sep 12  2021 .gdbinit-gef.py
drwx------ 3 andy andy 4.0K Sep 12  2021 .gnupg
drwx------ 5 andy andy 4.0K Sep 12  2021 .local
-rw-r--r-- 1 andy andy    0 Sep 12  2021 .sudo_as_admin_successful
-rwsrwxr-x 1 root root 8.2K Sep 12  2021 exploit_me

andy@ubuntu:~$ ./exploit_me
Type your name: 
andy
Your name is: andy
andy@ubuntu:~$ ./exploit_me
Type your name: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Your name is: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Segmentation fault (core dumped)

In x86 and x86-64 architectures, the "$RSP" register stands for "Stack Pointer." It is a special-purpose register that holds the memory address of the top of the stack. The stack is a region of memory used for temporary data storage during function calls and for managing local variables within functions.

For example, in x86-64 assembly language, the "$RSP" register is used to perform stack-related operations. Some common instructions involving the stack pointer include:

- `push`: Pushes a value onto the stack, decrementing the stack pointer.
- `pop`: Pops a value from the stack, incrementing the stack pointer.
- `call`: Calls a function and pushes the return address onto the stack.
- `ret`: Returns from a function by popping the return address from the stack.

andy@ubuntu:~$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.8.19.103 - - [03/Aug/2023 00:23:57] "GET /exploit_me HTTP/1.1" 200 -

┌──(witty㉿kali)-[~/Downloads]
└─$ wget 10.10.32.161:8000/exploit_me
--  http://10.10.32.161:8000/exploit_me
Connecting to 10.10.32.161:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 8392 (8.2K) [application/octet-stream]
Saving to: ‘exploit_me’

exploit_me           100%[=====================>]   8.20K  --.-KB/s    in 0.08s   

(96.9 KB/s) - ‘exploit_me’ saved [8392/8392]

                                                                                   
┌──(witty㉿kali)-[~/Downloads]
└─$ chmod +x exploit_me 
                                                                                   
┌──(witty㉿kali)-[~/Downloads]
└─$ ./exploit_me 
Type your name: 
hi
Your name is: hi

┌──(witty㉿kali)-[~/Downloads]
└─$ gdb exploit_me 
GNU gdb (Debian 13.1-2) 13.1
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
pwndbg: loaded 136 pwndbg commands and 43 shell commands. Type pwndbg [--shell | --all] [filter] for a list.
pwndbg: created $rebase, $ida GDB functions (can be used with print/break)
Reading symbols from exploit_me...
(No debugging symbols found in exploit_me)
------- tip of the day (disable with set show-tips off) -------
Use GDB's dprintf command to print all calls to given function. E.g. dprintf malloc, "malloc(%p)\n", (void*)$rdi will print all malloc calls
gdb-peda$ pattern create
Error: missing argument
Generate, search, or write a cyclic pattern to memory
Set "pattern" option for basic/extended pattern type
