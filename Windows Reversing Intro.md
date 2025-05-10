# Windows Reversing Intro — Writeup

## Overview
### Windows Reversing Intro — Writeup
### Windows Reversing Intro — Writeup
----
Introduction to reverse engineering x64 Windows software.
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/e1566084619ac2e56f872e4f3a4faea3.png)
Start Machine
**Previous Room**
[https://tryhackme.com/room/win64assembly](https://tryhackme.com/room/win64assembly)
This room is part of a series of rooms that will introduce you to reverse engineering software on Windows. This is going to be a fairly short and easy room in which you will be introduced to how higher-level concepts look at a lower level. You will also start to get familiar with IDA. We will use the skills learned here to perform more advanced reverse engineering techniques in future rooms.
The programs provided in this room are compiled with MSVC (C++ compiler built-in with Visual Studio) set to release mode for x64. Debug binaries and symbols will not be used to teach with, however, debug symbols will be provided for those who are curious. This is done to make everything as realistic as possible. Debug symbols are a luxury when reverse engineering, and aren't common when dealing with executables.
### Get Hands-On.
**When running the samples on their own, outside of IDA, run them via the command line.**
Use the VM provided alongside this room to get hands-on with the material. This will greatly improve your experience and learning in this room. The VM has IDA Freeware installed along with the samples for the room.
VM Credentials:
- **Username:** thm
- **Password:** THMWinRE!
Quick note for the VM: When you load an executable into IDA you will be asked for debug symbols (a PDB). Say no to this. A further explanation as to why will be provided in the next task. If you attempt to download symbols IDA may crash.
### Bring your own VM!
While the VM hosting on THM is great, they do have their limitations. Things such as processing power and internet access will make some tasks more difficult and it's for those reasons why I highly recommend you make a VM on your own computer. All you will need to do is install IDA Freeware and get the programs we will be reverse engineering.
Answer the questions below
Let's get started!
Question Done
### Tool Introductions
In this room, we will be using IDA Freeware. Historically the downside to IDA has always been its pricing, however, thanks to recent developments in other tools, the free version of IDA now has many more features than it used to. Other good tools include x64dbg, Ghidra, WinDBG, Radare2, and of course GDB. My daily drivers are x64dbg and Ghidra. IDA is used for this series since it's easy for beginners and results in us only having to use one tool.
First, let's discuss static vs dynamic analysis. **Static** analysis involves looking at the program as it exists on disk; The program is never executed. **Dynamic** analysis involves analyzing the process as it runs. Dynamic analysis is usually preferred unless dealing with malware. Dynamic analysis allows you to see data in memory and how it's being used. Static on the other hand requires you to guess or do detailed reverse engineering to figure it out.
There are three main functionalities that our tools will provide, those are debugging, disassembling, and decompiling. **Disassemblers** will translate the program from its bytes on disk or in memory into its assembly code equivalent and present it in an informative way. **Decompilers** are similar to disassemblers except instead of giving us the assembly, it attempts to recreate the code in C/C++. The downside to decompilers is that they can be inaccurate, or lack information. Because of this, if you're using a decompiler it's a good idea to have the disassembled code next to the decompiled code to check for inaccuracies. **Debuggers**, alongside disassemblers and decompilers, will allow us to place breakpoints within the program while it's running and analyze registers, memory, statuses, and more. They also allow for changing data in memory while the program is running.
IDA is quite an extensive tool, I will only show you what you need to know. I **highly** encourage you to learn more about how to use IDA on your own time. It's not difficult to use, rather there's just a lot to it. For the following explanations, I will be using notepad.exe (C:\Windows\System32\notepad.exe).
To load a program into IDA you can start IDA then follow the prompts, or you can alternatively just drag and drop the executable file onto the IDA icon on your Desktop. While loading the program into IDA it will prompt you about the type of file, you can just stick with the defaults. At some point, you will be asked about debug symbols (PDB). In the real world, get any debug symbols you can. Normally you will only have the debug symbols for Windows libraries. For the sake of this room, we won't use any except for what comes with the system by default.
### Debug Symbols
Debug symbols are extremely helpful and you should use them when you can. Unfortunately, you will usually only have debug symbols for common libraries and rarely for the executable of interest. In addition to that, most reversing tools download symbols for common libraries so if you don't have an internet connection you won't get them. Note that because of this, don't attempt to download symbols in IDA when using the VM otherwise you will get errors and it may crash. In this room, we will go over the samples **without** their debug symbols to maintain as much realism as possible. However, for further learning purposes, debug symbols will be provided if you wish to manually load them.
### Code Views
The two primary views, listing and graph view, show the program in its disassembled form. You can switch between the two by pressing the space bar. I recommend you spend most of your time in graph view, as it shows the flow of the program.
As you can see in the graph view, the arrows represent the destination of jump instructions. This is incredibly useful and a massive time saver.
In the listing view, you can see slightly more information, however, it's much harder to understand the flow of the program.
You may find it helpful to enable Auto Comments by going to _Options > General > Disassembly (Selected by default) > Auto Comments
_Play around with it on/off and see if you like it. I found it useful when I started since it describes what is happening in the assembly.
**You need to have internet access to be able to decompile code with IDA Freeware, so it will NOT work in the provided VM.**
IDA also has a decompiler. Do not become reliant on decompilers as they aren't always accurate and often have issues representing every instruction in longer sections of code. With that said, they are a great place to get a general idea of what's going on. To decompile, IDA calls it pseudocode, you can click on the area of code you want to decompile and press _F5_. You can also go to _View > Open Subviews > Generate Pseudocode_.
**I will not be utilizing the decompiler feature of IDA for this series of rooms.**

## Enumeration
These tabs are pretty self-explanatory. The imports tab shows all of the functions imported by the current program from other sources. The exports tab shows all of the functions exposed by the current program. Note that the exports of an executable usually contain only the entry point (where the program starts executing from).
### Functions
On the left, you can see the Functions window which shows the identified functions for the current program. Depending on what symbols you have access to, you may have more or less functions with actual names. If there are no symbols to identify a function, it will instead be given a generic name such as sub_140001000 where 140001000 is the address of the function.
### Other Subviews
You can find other useful tabs/subviews under _View > Open Subviews_. I encourage you to play around with the different subviews as there's a significant amount of information found within them. One subview in particular which you should get familiar with is the _Strings_ subview. Here you can view all identified strings in memory. This can be helpful, as we will see later when finding a certain function or place of interest.
### Further Learning
As mentioned, IDA is packed full of stuff. I highly recommend you play around and get familiar with IDA. There are loads of guides, videos, and even books out there to assist you!
Answer the questions below
Once you feel comfortable with IDA, let's start doing some reverse engineering!
Completed
### Task 3  Explanation Function Prologue/Epilogue
Remember how functions need stack frames? Function prologues and epilogues will set up, create, and destroy stack frames according to the calling convention in use. I will introduce them here and point them out as we encounter them on our journey.
### Prologue
The prologue comes before the body of a function is executed. Not all prologues are the same, but here are three things that can happen and the order they usually happen in.
1. Volatile registers are saved. If there is shadow space available, and the appropriate compilation options are chosen, the shadow space can be used to hold volatile registers. If there is no room in shadow space then registers are pushed onto the stack.
2. Space is allocated for the stack frame by subtracting from RSP. The amount subtracted from RSP can be used to determine the number of function parameters.
3. RSP or RBP may be preserved to be restored later. Since RBP isn't used much for stack purposes in x64 when it gets preserved it's likely _not_ being preserved to keep a stack address safe, rather it's being treated the same as the other volatile registers. In the case that it _is_ being used for stack purposes, you may see something along the lines of `mov RSP, RBP` which moves RSP to where RBP was at, setting up a new stack frame right next to the previous one.
Generally speaking, it's fine to skim over the function prologue, however, note that it can hint at how many parameters are passed to the function.
### Epilogue
The epilogue is pretty straightforward, it undoes/unwinds any stack-related things, mostly caused by the prologue. The epilogue can be a nice place to double-check you didn't miss anything within the prologue, but it's generally more useless to a reverse engineer than the prologue.
You may see the following in the epilogue:
1. Addition to RSP to restore/delete the stack frame.
2. Restoring registers, usually done by popping registers off the stack which were pushed on the stack during the prologue.
3. Return.
That's all there is to most epilogues.
Quick side note, you may have heard that nothing on disk is ever actually deleted. When you delete something the OS simply marks that area on disk as not being used so the OS knows it can write to that location without overwriting anything important. This is why data removal software exists. It will go in and fill in the area with zeroes or junk data so the original data is removed. Similarly, nothing gets deleted from the stack by the prologue or epilogue. When the next stack frame is made it will be put right where the old one was and there will still be data there. This is why you should initialize variables upfront, because otherwise, your variable may contain garbage from the previous function/stack frame.
Answer the questions below
It's like a play, but there's way more bits.
Question Done
### Task 4  Analysis Function Call Sample
Download Task Files
**When running the samples on their own, outside of IDA, run them via the command line.**
Before you load the program into IDA, I want to quickly repeat a warning. When you are prompted for debug symbols **do not** do it. This is to maintain realism. If you wish to use debug symbols for further learning on your own, you can load them manually after the program is loaded into IDA. The debug symbols are provided in a folder on the Desktop along with the samples. If you attempt to download symbols IDA may crash.
### **Getting Started**
Let's take a look at a sample that calls a function. For this task use **HelloWorld.exe**. It's usually a good idea to run the program before doing any reverse engineering, so go ahead and do that. Again, when you run the program do so from a command prompt since the program closes very quickly.
We are going to start from main(), find it in the function list if IDA doesn't navigate to it automatically. The main() function should look something like this:
Notice the `sub RSP, 28h` at the top. For this function that's the entire prologue. It's setting up the function by moving the stack pointer and creating a new stack frame area.
### printf()
For now, we will focus on the first function call within main(), which is a call to printf(). IDA does not resolve that this is printf(), so instead, you can identify it as such based on the parameters passed and what it does when the program runs. IDA shows two strings loaded into the first two parameters for the function call. The first parameter (passed via RCX) is the format string "%s\n", the second parameter (RDX) is the "Hello with..." string. Immediately after the two parameters is the call. In IDA you can rename the sub_### to whatever you want by right-clicking and going to _Rename_ or by selecting the function and pressing _N_. Renaming variables and functions is very useful when dealing with bigger projects.
That's it for the call to printf(). The first parameter is the format string, the second is the "Hello..." string, and printf() makes the magic happen. Feel free to look into printf() more if you'd like.
### std::cout
Now let's look at the second function call which is to std::cout.
We can identify it's std::cout without using the string printed to the console because we can see things related to cout, basic_ostream, and char_traits. You may notice the names of the functions are quite odd as displayed in IDA. We will discuss this in the DLL section, but in short, the names are mangled for function overloading. For now, look past the name mangling. With that said, you may not be familiar with those functions so the first thing to do is look them up. Here's a brief overview of them all:
- basic_ostream - C++ template for output streams. [More info here](https://en.cppreference.com/w/cpp/io/basic_ostream).
- char_traits - Provides some abstraction from basic character and string types.
- cout - std::cout - Sends text to the console.
Now to address the elephant in the room. Where is the string that's supposed to be printed? Let's find it.
To find our string go to _View > Open Subviews > Strings_ or press _Shift + F12_. Note that this may take a bit to process. Then look for the string in the list. You can use Ctrl + F to search. Double-click the string in the list and this will bring you to the string where you can see all references to that string. IDA calls these XREFs, short for cross-references.
The string only has one reference, so double-click it. This will bring you to the location of the string which is in a very large function.
The string is very clearly not where we would've expected it to be. We can see `sputn`, which long story short means we're dealing with character streams. So what is this massive function and what is it doing? If you go to the top of the function in the listing view you can see what references it. Sure enough, main() references this function. So what's going on here?
### Inlining
One compiler/linker optimization that makes noticeable changes to the code is inlining. When a function gets inlined it's essentially pasted where the call would be instead of making a call. See the following example.
**Without** Function Inlining:
```cpp
int Add(int x, int y){
    return x+y;
}
int main(){
    int x = RandInt();
    int res = Add(x, 5)
}
```
**With** Function Inlining:
```cpp
int main(){
    int x = RandInt();
    int res = x + 5;
}
```
What's happening with our string in HelloWorld.exe is similar. Instead of the string being passed as a parameter to std::cout, it's directly referenced in std::cout. You may think that this would cause problems because what if std::cout is called to print a different string? You'd be correct, this would cause problems for further calls to std::cout. As it turns out if std::cout is called more than once you will not see this optimization used. Instead, you will see it used similar to how printf() is used.
I encourage you to write a program to play around with this to develop a deeper understanding of it. You may have noticed that there's some interesting stuff with std::cout that I skipped over. In short, it has to do with function overloading, basic_ostream, and streambuf which deals with character streams. If you're interested, simple searches of those things will bring you some useful information.
That concludes the basic function example. It's really easy to understand function calls as long as you know the calling convention used. Luckily for x64 Windows it only uses fastcall, but other systems and architectures will likely not be that nice. Be sure to know whatever calling convention you're dealing with well, it will make your work much easier.
Answer the questions below
In the HelloWorld.exe sample, which instruction sets up the first parameter for the call to printf()? Provide the full instruction as shown in IDA, with single spaces. Example: mov RAX, RBX
Think back to the x64 Windows calling convention, what register is used to pass the first parameter? Also, look at the comments provided by IDA which show what the parameters are. Which would be the first when using printf()?
*lea rcx, Format*
### Task 5  Analysis Loop Sample
Download Task Files
**When running the samples on their own, outside of IDA, run them via the command line.**
It's highly encouraged to follow along for this portion in your own VM, as it will make it must easier for you to understand. This task uses _Loop.exe_. Load it into IDA and go to the main() function. The graph view is highly recommended.
