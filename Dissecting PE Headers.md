# Dissecting PE Headers — Writeup

## Overview
### Dissecting PE Headers — Writeup
### Dissecting PE Headers — Writeup
----
Learn about Portable Executable files and how their headers work.
----
![](https://assets.tryhackme.com/additional/peheaders/dissecting_pe_headers.png)
![](https://tryhackme-images.s3.amazonaws.com/room-icons/d337b40079925cc50a870a6ba872c242.png)
In the Windows Operating System, you might have often seen files with extension `.exe`. The `.exe` extension here stands for executable. As the name suggests, an executable file contains code that can be executed. Therefore, anything that needs to be run on a Windows Operating System is executed using an executable file, also called a Portable Executable file (PE file), as it can be run on any Windows system. A PE file is a Common Object File Format (COFF) data structure. The COFF consists of Windows PE files, DLLs, shared objects in Linux, and ELF files. For this room, we will only be covering the Windows PE files.
Given this background knowledge, it becomes essential to understand the PE file to learn malware analysis. This room will introduce us to the following concepts:
- Understanding the different headers in a PE file
- Learning how to read PE headers
- Identify packed executables
- Use the information from PE headers to analyze malware
Before going through this room, it is recommended that you complete the [Intro to Malware Analysis](https://tryhackme.com/room/intromalwareanalysis) room.
Answer the questions below
Go through the Intro to Malware Analysis room.
Question Done
On disk, a PE executable looks the same as any other form of digital data, i.e., a combination of bits. If we open a PE file in a Hex editor, we will see a random bunch of Hex characters. This bunch of Hex characters are the instructions a Windows OS needs to execute this binary file.
In the upcoming tasks, we will try to make sense of the Hex numbers we see in the above screenshot and describe them as Windows understands them. We will also explore how to leverage this information for malware analysis. We will use the `wxHexEditor` utility, present in the next task's attached VM to perform this task.
As we view the file in a Hex editor, we observe that manually interpreting all this data might become too tedious. Therefore, we will use a tool `pe-tree` in the attached VM to help us analyze the PE header. This is what we see when we open a PE file using `pe-tree`.
- IMAGE_DOS_HEADER
- IMAGE_NT_HEADERS
- FILE_HEADER
- OPTIONAL_HEADER
- IMAGE_SECTION_HEADER
- IMAGE_IMPORT_DESCRIPTOR
All of these headers are of the data type [STRUCT](https://docs.microsoft.com/en-us/cpp/cpp/struct-cpp?view=msvc-170). A struct is a user-defined data type that combines several different types of data elements in a single variable. Since it is user-defined, we need to see the documentation to understand the type for each STRUCT variable. The documentation for each header can be found on [MSDN](https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-image_nt_headers32), where you can find the data types of the different fields inside these headers.
Please remember that while we use the tools mentioned earlier, various other tools perform similar tasks. However, the goal is not to learn about the tools but instead the PE format so that we can perform the same analysis using any other tools we come across, providing the same functionality.
Now, let's move to the following tasks and learn about each of these parts of a PE file.
Answer the questions below
What data type are the PE headers?
*STRUCT*
### Task 3  IMAGE_DOS_HEADER and DOS_STUB
Start Machine
For this task, we will need to use the attached VM. For this purpose, press the 'Start Machine' button on the top-right corner of this task to start the attached machine. The machine will start in a split-screen view. In case the machine is not visible, use the blue Show Split View button at the top-right of the page. Alternatively, you can log in to the machine using the following credentials:
Username: ubuntu
Password: 123456
Once the machine starts, we can find that there is a directory on the Desktop of the machine named `Samples`. In this directory, we will find a few PE files. Let's open the file named `redline` in a Hex editor to see what it looks like. We can use the `wxHexEditor` utility in the attached VM to open the required file. To open the `wxHexEditor`, press the menu on the top left corner of the VM and search for `wxHexEditor`, as shown in the following screenshot.
This is what the redline PE will look like in the Hex Editor.
Since it seems a little too complex to comprehend, let's use the help of the `pe-tree` utility to see what the PE header looks like. If we run the following command in the terminal in the attached VM, it will open the redline PE file in the `pe-tree` utility.
`pe-tree Desktop/Samples/redline`
Please note that the pe-tree utility will take roughly 8 minutes to open. In the meanwhile, you can continue reading the text and come back once it has opened. This is what the `pe-tree` output will look like when we open the redline utility.
The above screenshot shows some basic information about the PE file in the right-hand pane. We see the size, hashes, Entropy, architecture, and compiled date of the PE file. This information is not extracted directly from the header; instead, it is calculated or extracted from different parts of the header, as we will see later. The header starts below this information, with the heading IMAGE_DOS_HEADER. Let's dive into that and learn what information that contains.
### The IMAGE_DOS_HEADER:
The IMAGE_DOS_HEADER consists of the first 64 bytes of the PE file. We will analyze some of the valuable information found in the IMAGE_DOS_HEADER below. The below screenshot has the IMAGE_DOS_HEADER highlighted in the Hex Editor.
In the screenshot above from the Hex Editor, notice the first two bytes that say `4D 5A`. They translate to the `MZ` characters in ASCII, as shown in the right pane of the Hex Editor. So what do these characters mean?
The MZ characters denote the initials of [Mark Zbikowski](https://en.wikipedia.org/wiki/Mark_Zbikowski), one of the Microsoft architects who created the MS-DOS file format. The MZ characters are an identifier of the Portable Executable format. When these two bytes are present at the start of a file, the Windows OS considers it a Portable Executable format file.
This is what it will look like when we expand the IMAGE_DOS_HEADER dropdown menu:
Notice the first entry in the IMAGE_DOS_HEADER dropdown menu. It says `e_magic` and has a value of `0x5a4d MZ`. This is the same as what we saw in the Hex Editor above, but the byte order is reversed due to [endianness](https://en.wikipedia.org/wiki/Endianness). The Intel x86 architecture uses a little-endian format, while ARM uses a big-endian format.
The last value in the IMAGE_DOS_HEADER is called `e_lfanew`. In the above screenshot, it has a value of `0x000000d8`. This denotes the address from where the IMAGE_NT_HEADERS start. Therefore, in this PE file, the IMAGE_NT_HEADERS start from the address `0x000000d8`. We can see this value highlighted in the Hex editor below.
We have to remember that the byte order is switched when we compare those reported by the pe-tree utility and those we see in the Hex editor due to [endianness](https://en.wikipedia.org/wiki/Endianness).
The IMAGE_DOS_HEADER is generally not of much use apart from these fields, especially during malware reverse engineering. The only reason it's there is backward compatibility between MS-DOS and Windows.
### The DOS_STUB:
In the pe-tree utility, we see that the following dropdown menu after IMAGE_DOS_HEADER is the DOS STUB. Let's expand that and see what we find in there.
The DOS STUB contains the message that we also see in the Hex Editor `!This program cannot be run in DOS mode`, as seen in the screenshot below. Please note that the size, hashes, and Entropy shown here by pe-tree are not related to the PE file; instead, it is for the particular section we are analyzing. These values are calculated based on the data in a specific header and are not included.
The size value denotes the size of the section in bytes. Then we see different hashes for the section. We learned about hashes in the [Intro to Malware Analysis](https://tryhackme.com/room/intromalwareanalysis) room. Entropy is the amount of randomness found in data. The higher the value of Entropy, the more random the data is. We will learn about the utility of Entropy as we learn more about malware analysis.
The DOS STUB is a small piece of code that only runs if the PE file is incompatible with the system it is being run on. It displays the message mentioned above. For example, since this PE file we are examining is a Windows executable, if it is run in MS-DOS, the PE file will exit after showing the message in the DOS STUB.
Answer the questions below
```text
ubuntu@ip-10-10-131-54:~$ pe-tree Desktop/Samples/zmsuz3pinwl

e_lfanew: 0x000000f8
```
How many bytes are present in the IMAGE_DOS_HEADER?
*64*
What does MZ stand for?
*Mark Zbikowski*
In what variable of the IMAGE_DOS_HEADER is the address of IMAGE_NT_HEADERS saved?
*e_lfanew*
In the attached VM, open the PE file Desktop/Samples/zmsuz3pinwl in pe-tree. What is the address of IMAGE_NT_HEADERS for this PE file?
Check the e_lfanew value in the IMAGE_DOS_HEADER
**
### Task 4  IMAGE_NT_HEADERS
The rest of the room will focus on the different parts of IMAGE_NT_HEADERS. We can find details of IMAGE_NT_HEADERS in [Microsoft Documentation](https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-image_nt_headers32). This header contains most of the vital information related to the PE file. In pe-tree, this is how the IMAGE_NT_HEADERS look like:
### NT_HEADERS:
Before diving into the details of NT_HEADERS, let's get an overview of the NT_HEADERS. The NT_HEADERS consist of the following:
- Signature
- FILE_HEADER
- OPTIONAL_HEADER
We will cover the Signature and FILE_HEADER in this task but the OPTIONAL_HEADER in the next task.
The starting address of IMAGE_NT_HEADERS is found in `e_lfanew` from the IMAGE_DOS_HEADER. In the redline binary, we saw that this address was `0x000000D8`. So let's start by going to this offset and see what we find there. We can do that by pressing `Ctrl+G` in the Hex Editor Window or going to Edit>Go to offset from the GUI.
We have to make sure that we select `From beginning` in `Type of branch` option at the bottom and the data type is set to `Hex` for correct results.
### Signature:
The first 4 bytes of the NT_HEADERS consist of the Signature. We can see this as the bytes `50 45 00 00` in Hex, or the characters `PE` in ASCII as shown in the Hex editor.
The Signature denotes the start of the NT_HEADER. Apart from the Signature, the NT_HEADER contains the FILE_HEADER and the IMAGE_OPTIONAL_HEADER.
### FILE_HEADER:
The FILE_HEADER contains some vital information. The following screenshot shows the FILE_HEADER as shown in the pe-tree utility.
As we can see in the above screenshot, the FILE_HEADER has the following fields:
- _Machine:_ This field mentions the type of architecture for which the PE file is written. In the above example, we can see that the architecture is i386 which means that this PE file is compatible with 32-bit Intel architecture.
- _NumberOfSections:_ A PE file contains different sections where code, variables, and other resources are stored. This field of the IMAGE_FILE_HEADER mentions the number of sections the PE file has. In our case, the PE file has five sections. We will learn about sections later in the room.
- _TimeDateStamp:_ This field contains the time and date of the binary compilation.
- _PointerToSymbolTable and NumberOfSymbols:_ These fields are not generally related to PE files. Instead, they are here due to the COFF file headers.
- _SizeOfOptionalHeader:_ This field contains the size of the optional header, which we will learn about in the next task. In our case, the size is 224 bytes.
- _Characteristics:_ This is another critical field. This field mentions the different characteristics of a PE file. In our case, this field tells us that the PE file has stripped relocation information, line numbers, and local symbol information. It is an executable image and compatible with a 32-bit machine.
While we looked at the FILE_HEADER using the pe-tree utility, we can see that the hex values for each field are also shown in the pe-tree utility. Can you look at the Hex editor and find where each value is located?
We are starting to learn to read Hex now, aren't we? To learn more about the FILE_HEADER, you can check out [Microsoft Documentation](https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-image_file_header) for it.
Answer the questions below
![[Pasted image 20230815195906.png]]
In the attached VM, there is a file Desktop\Samples\zmsuz3pinwl. Open this file in pe-tree. Is this PE file compiled for a 32-bit machine or a 64-bit machine?
Check the characteristics in FILE_HEADER
*32-bit machine*
What is the TimeDateStamp of this file?
Right-click and copy the complete value, including the Hex value and its translated value
*0x62289d45 Wed Mar  9 12:27:49 2022 UTC*
### Task 5  OPTIONAL_HEADER
The OPTIONAL_HEADER is also a part of the NT_HEADERS. It contains some of the most important information present in the PE headers. Let's see what it looks like in the pe-tree utility.
In the Hex editor, the OPTIONAL_HEADER starts right after the end of the FILE_HEADER. Below you can see the start of the OPTIONAL_HEADER of the redline binary in the Hex Editor.
Let's learn about some of the critical fields in the OPTIONAL_HEADER.
- _Magic:_ The Magic number tells whether the PE file is a 32-bit or 64-bit application. If the value is 0x010B, it denotes a 32-bit application; if the value is 0x020B, it represents a 64-bit application. The above screenshot of the Hex Editor shows the highlighted bytes, which show the magic of the loaded PE file. Since the value is 0x010B, it shows that it is a 32-bit application.
- _AddressOfEntryPoint:_ This field is significant from a malware analysis/reverse-engineering point of view. This is the address from where Windows will begin execution. In other words, the first instruction to be executed is present at this address. This is a Relative Virtual Address (RVA), meaning it is at an offset relative to the base address of the image (ImageBase) once loaded into memory.
- BaseOfCode and BaseOfData: These are the addresses of the code and data sections, respectively, relative to ImageBase.
- _ImageBase:_ The ImageBase is the preferred loading address of the PE file in memory. Generally, the ImageBase for .exe files is 0x00400000, which is also the case for our PE file. Since Windows can't load all PE files at this preferred address, some relocations are in order when the file is loaded in memory. These relocations are then performed relative to the ImageBase.
- _Subsystem:_ This represents the Subsystem required to run the image. The Subsystem can be Windows Native, GUI (Graphical User Interface), CUI (Commandline User Interface), or some other Subsystem. The screenshot above from the pe-tree utility shows that the Subsystem is 0x0002, representing Windows GUI Subsystem. We can find the complete list in [Microsoft Documentation](https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-image_optional_header32).
- _DataDirectory:_ The DataDirectory is a structure that contains import and export information of the PE file (called Import Address Table and Export Address Table). This information is handy as it gives a glimpse of what the PE file might be trying to do. We will expand on the import information later in this room.
Though there is more information in the OPTIONAL_HEADER, we will not go into those in this room. If you want to learn more about the OPTIONAL_HEADER, you can check out [Microsoft Documentation](https://docs.microsoft.com/en-us/windows/win32/api/winnt/ns-winnt-image_optional_header32) about this header.
Answer the questions below
```text
Subsystem: 0x0003 WINDOWS_CUI
```
Which variable from the OPTIONAL_HEADER indicates whether the file is a 32-bit or a 64-bit application?
*Magic*
What Magic value indicates that the file is a 64-bit application?
*0x020B*
What is the subsystem of the file Desktop\Samples\zmsuz3pinwl?
Copy the complete value from pe-tree, including the hex value and translated value
*0x0003 WINDOWS_CUI*
### Task 6  IMAGE_SECTION_HEADER
The data that a PE file needs to perform its functions, like code, icons, images, User Interface elements, etc., are stored in different Sections. We can find information about these Sections in the IMAGE_SECTION_HEADER. In the pe-tree utility, the IMAGE_SECTION_HEADER is shown for each separate section, as can be seen in the below screenshot.
As we can see, the IMAGE_SECTION_HEADER has different sections, namely `.text`, `.rdata`, `.data`, `.ndata` and `.rsrc`. Before moving to the information present in the header of each section, let's learn about the commonly found sections in a PE file.
- _.text:_ The .text section is generally the section that contains executable code for the application. We can see above that the Characteristics for this section include CODE, EXECUTE and READ, meaning that this section contains executable code, which can be read but can't be written to.
- _.data:_ This section contains initialized data of the application. It has READ/WRITE permissions but doesn't have EXECUTE permissions.
- ._rdata/.idata:_ These sections often contain the import information of the PE file. Import information helps a PE file import functions from other files or Windows API.
- .ndata: The .ndata section contains uninitialized data.
