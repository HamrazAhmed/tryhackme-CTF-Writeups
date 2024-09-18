---
Learn how to perform memory forensics with Volatility!
---

# Volatility — Writeup

## Overview
### Volatility — Writeup
### Volatility — Writeup
![](https://assets.tryhackme.com/room-banners/volatility.png)
### Introduction
Volatility is a free memory forensics tool developed and maintained by Volatility Foundation, commonly used by malware and SOC analysts within a blue team or as part of their detection and monitoring solutions. Volatility is written in Python and is made up of python plugins and modules designed as a plug-and-play way of analyzing memory dumps.
Volatility is available for Windows, Linux, and Mac OS and is written purely in Python.
Security Operations Center (SOC) is a team of IT security professionals tasked with monitoring, preventing , detecting , investigating, and responding to threats within a company’s network and systems.
![333](https://i.imgur.com/5uximLP.png)
This room uses memory dumps from THM rooms and memory samples from Volatility Foundation.
Before completing this room, we recommend completing the Core Windows Processes room.
If you plan on using your own machine or the AttackBox to run Volatility, download the files attached to this task. If you plan to use the provided machine, you can deploy it in Task 3.
From the Volatility Foundation Wiki, "Volatility is the world's most widely used framework for extracting digital artifacts from volatile memory (RAM) samples. The extraction techniques are performed completely independent of the system being investigated but offer visibility into the runtime state of the system. The framework is intended to introduce people to the techniques and complexities associated with extracting digital artifacts from volatile memory samples and provide a platform for further work into this exciting area of research."
Volatility is built off of multiple plugins working together to obtain information from the memory dump. To begin analyzing a dump, you will first need to identify the image type; there are multiple ways of identifying this information that we will cover further in later tasks. Once you have your image type and other plugins sorted, you can then begin analyzing the dump by using various volatility plugins against it that will be covered in depth later in this room.
Since Volatility is entirely independent of the system under investigation, this allows complete segmentation but full insight into the runtime state of the system.
At the time of writing, there are two main repositories for Volatility; one built off of python 2 and another built off python 3. For this room, we recommend using the Volatility3 version build off of python 3. https://github.com/volatilityfoundation/volatility3
Note: When reading blog posts and articles about Volatility, you may see volatility2 syntax mentioned or used, all syntax changed in volatility3, and within this room, we will be using the most recent version of the plugin syntax for Volatility.
### Installing Volatility
```text
┌──(kali㉿kali)-[~]
└─$ mkdir volatility
```
```text
┌──(kali㉿kali)-[~]
└─$ cd volatility
```
```text
┌──(kali㉿kali)-[~/volatility]
└─$ ls
```
```text
┌──(kali㉿kali)-[~/volatility]
└─$ git clone https://github.com/volatilityfoundation/volatility3.git
Cloning into 'volatility3'...
remote: Enumerating objects: 28935, done.
remote: Counting objects: 100% (193/193), done.
remote: Compressing objects: 100% (110/110), done.
remote: Total 28935 (delta 98), reused 154 (delta 81), pack-reused 28742
Receiving objects: 100% (28935/28935), 5.58 MiB | 5.90 MiB/s, done.
Resolving deltas: 100% (21930/21930), done.
```
```text
┌──(kali㉿kali)-[~/volatility]
└─$ ls
volatility3
```
```text
┌──(kali㉿kali)-[~/volatility]
└─$ cd volatility3
```
```text
┌──(kali㉿kali)-[~/volatility/volatility3]
└─$ ls
API_CHANGES.md  mypy.ini                  setup.py     volshell.spec
development     README.md                 test         vol.spec
doc             requirements-dev.txt      volatility3
LICENSE.txt     requirements-minimal.txt  vol.py
MANIFEST.in     requirements.txt          volshell.py
```
```text
┌──(kali㉿kali)-[~/volatility/volatility3]
└─$ pip install -r requirements.txt
```
```text
┌──(kali㉿kali)-[~/volatility/volatility3]
└─$ python3 vol.py -h
Volatility 3 Framework 2.4.1
usage: volatility [-h] [-c CONFIG] [--parallelism [{processes,threads,off}]]
                  [-e EXTEND] [-p PLUGIN_DIRS] [-s SYMBOL_DIRS] [-v] [-l LOG]
                  [-o OUTPUT_DIR] [-q] [-r RENDERER] [-f FILE] [--write-config]
                  [--save-config SAVE_CONFIG] [--clear-cache]
                  [--cache-path CACHE_PATH] [--offline]
                  [--single-location SINGLE_LOCATION] [--stackers [STACKERS ...]]
                  [--single-swap-locations [SINGLE_SWAP_LOCATIONS ...]]
                  plugin ...

An open-source memory forensics framework

options:
  -h, --help            Show this help message and exit, for specific plugin options
                        use 'volatility <pluginname> --help'
  -c CONFIG, --config CONFIG
                        Load the configuration from a json file
  --parallelism [{processes,threads,off}]
                        Enables parallelism (defaults to off if no argument given)
  -e EXTEND, --extend EXTEND
                        Extend the configuration with a new (or changed) setting
  -p PLUGIN_DIRS, --plugin-dirs PLUGIN_DIRS
                        Semi-colon separated list of paths to find plugins
  -s SYMBOL_DIRS, --symbol-dirs SYMBOL_DIRS
                        Semi-colon separated list of paths to find symbols
  -v, --verbosity       Increase output verbosity
  -l LOG, --log LOG     Log output to a file as well as the console
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Directory in which to output any generated files
  -q, --quiet           Remove progress feedback
  -r RENDERER, --renderer RENDERER
                        Determines how to render the output (quick, none, csv,
                        pretty, json, jsonl)
  -f FILE, --file FILE  Shorthand for --single-location=file:// if single-location is
                        not defined
  --write-config        Write configuration JSON file out to config.json
  --save-config SAVE_CONFIG
                        Save configuration JSON file to a file
  --clear-cache         Clears out all short-term cached items
  --cache-path CACHE_PATH
                        Change the default path (/home/kali/.cache/volatility3) used
                        to store the cache
  --offline             Do not search online for additional JSON files
  --single-location SINGLE_LOCATION
                        Specifies a base location on which to stack
  --stackers [STACKERS ...]
                        List of stackers
  --single-swap-locations [SINGLE_SWAP_LOCATIONS ...]
                        Specifies a list of swap layer URIs for use with single-
                        location

Plugins:
  For plugin specific options, run 'volatility <plugin> --help'

  plugin
    banners.Banners     Attempts to identify potential linux banners in an image
    configwriter.ConfigWriter
                        Runs the automagics and both prints and outputs configuration
                        in the output directory.
    frameworkinfo.FrameworkInfo
                        Plugin to list the various modular components of Volatility
    isfinfo.IsfInfo     Determines information about the currently available ISF
                        files, or a specific one
    layerwriter.LayerWriter
                        Runs the automagics and writes out the primary layer produced
                        by the stacker.
    linux.bash.Bash     Recovers bash command history from memory.
    linux.check_afinfo.Check_afinfo
                        Verifies the operation function pointers of network
                        protocols.
    linux.check_creds.Check_creds
                        Checks if any processes are sharing credential structures
    linux.check_idt.Check_idt
                        Checks if the IDT has been altered
    linux.check_modules.Check_modules
                        Compares module list to sysfs info, if available
    linux.check_syscall.Check_syscall
                        Check system call table for hooks.
    linux.elfs.Elfs     Lists all memory mapped ELF files for all processes.
    linux.keyboard_notifiers.Keyboard_notifiers
                        Parses the keyboard notifier call chain
    linux.kmsg.Kmsg     Kernel log buffer reader
    linux.lsmod.Lsmod   Lists loaded kernel modules.
    linux.lsof.Lsof     Lists all memory maps for all processes.
    linux.malfind.Malfind
                        Lists process memory ranges that potentially contain injected
                        code.
    linux.mountinfo.MountInfo
                        Lists mount points on processes mount namespaces
    linux.proc.Maps     Lists all memory maps for all processes.
    linux.psaux.PsAux   Lists processes with their command line arguments
    linux.pslist.PsList
                        Lists the processes present in a particular linux memory
                        image.
    linux.pstree.PsTree
                        Plugin for listing processes in a tree based on their parent
                        process ID.
    linux.tty_check.tty_check
                        Checks tty devices for hooks
    mac.bash.Bash       Recovers bash command history from memory.
    mac.check_syscall.Check_syscall
                        Check system call table for hooks.
    mac.check_sysctl.Check_sysctl
                        Check sysctl handlers for hooks.
    mac.check_trap_table.Check_trap_table
                        Check mach trap table for hooks.
    mac.ifconfig.Ifconfig
                        Lists network interface information for all devices
    mac.kauth_listeners.Kauth_listeners
                        Lists kauth listeners and their status
    mac.kauth_scopes.Kauth_scopes
                        Lists kauth scopes and their status
    mac.kevents.Kevents
                        Lists event handlers registered by processes
    mac.list_files.List_Files
                        Lists all open file descriptors for all processes.
    mac.lsmod.Lsmod     Lists loaded kernel modules.
    mac.lsof.Lsof       Lists all open file descriptors for all processes.
    mac.malfind.Malfind
                        Lists process memory ranges that potentially contain injected
                        code.
    mac.mount.Mount     A module containing a collection of plugins that produce data
                        typically found in Mac's mount command
    mac.netstat.Netstat
                        Lists all network connections for all processes.
    mac.proc_maps.Maps  Lists process memory ranges that potentially contain injected
                        code.
    mac.psaux.Psaux     Recovers program command line arguments.
    mac.pslist.PsList   Lists the processes present in a particular mac memory image.
    mac.pstree.PsTree   Plugin for listing processes in a tree based on their parent
                        process ID.
    mac.socket_filters.Socket_filters
                        Enumerates kernel socket filters.
    mac.timers.Timers   Check for malicious kernel timers.
    mac.trustedbsd.Trustedbsd
                        Checks for malicious trustedbsd modules
    mac.vfsevents.VFSevents
                        Lists processes that are filtering file system events
    timeliner.Timeliner
                        Runs all relevant plugins that provide time related
                        information and orders the results by time.
    windows.bigpools.BigPools
                        List big page pools.
    windows.cachedump.Cachedump
                        Dumps lsa secrets from memory
    windows.callbacks.Callbacks
                        Lists kernel callbacks and notification routines.
    windows.cmdline.CmdLine
                        Lists process command line arguments.
    windows.crashinfo.Crashinfo
    windows.devicetree.DeviceTree
                        Listing tree based on drivers and attached devices in a
                        particular windows memory image.
    windows.dlllist.DllList
                        Lists the loaded modules in a particular windows memory
                        image.
    windows.driverirp.DriverIrp
                        List IRPs for drivers in a particular windows memory image.
    windows.driverscan.DriverScan
                        Scans for drivers present in a particular windows memory
                        image.
    windows.dumpfiles.DumpFiles
                        Dumps cached file contents from Windows memory samples.
    windows.envars.Envars
                        Display process environment variables
    windows.filescan.FileScan
                        Scans for file objects present in a particular windows memory
                        image.
    windows.getservicesids.GetServiceSIDs
                        Lists process token sids.
    windows.getsids.GetSIDs
                        Print the SIDs owning each process
    windows.handles.Handles
                        Lists process open handles.
    windows.hashdump.Hashdump
                        Dumps user hashes from memory
    windows.info.Info   Show OS & kernel details of the memory sample being analyzed.
    windows.joblinks.JobLinks
                        Print process job link information
    windows.ldrmodules.LdrModules
    windows.lsadump.Lsadump
                        Dumps lsa secrets from memory
    windows.malfind.Malfind
                        Lists process memory ranges that potentially contain injected
                        code.
    windows.mbrscan.MBRScan
                        Scans for and parses potential Master Boot Records (MBRs)
    windows.memmap.Memmap
                        Prints the memory map
    windows.mftscan.MFTScan
                        Scans for MFT FILE objects present in a particular windows
                        memory image.
    windows.modscan.ModScan
                        Scans for modules present in a particular windows memory
                        image.
    windows.modules.Modules
                        Lists the loaded kernel modules.
    windows.mutantscan.MutantScan
                        Scans for mutexes present in a particular windows memory
                        image.
    windows.netscan.NetScan
                        Scans for network objects present in a particular windows
                        memory image.
    windows.netstat.NetStat
                        Traverses network tracking structures present in a particular
                        windows memory image.
    windows.poolscanner.PoolScanner
                        A generic pool scanner plugin.
    windows.privileges.Privs
                        Lists process token privileges
    windows.pslist.PsList
                        Lists the processes present in a particular windows memory
                        image.
    windows.psscan.PsScan
                        Scans for processes present in a particular windows memory
                        image.
    windows.pstree.PsTree
                        Plugin for listing processes in a tree based on their parent
                        process ID.
    windows.registry.certificates.Certificates
                        Lists the certificates in the registry's Certificate Store.
    windows.registry.hivelist.HiveList
                        Lists the registry hives present in a particular memory
                        image.
    windows.registry.hivescan.HiveScan
                        Scans for registry hives present in a particular windows
                        memory image.
    windows.registry.printkey.PrintKey
                        Lists the registry keys under a hive or specific key value.
    windows.registry.userassist.UserAssist
                        Print userassist registry keys and information.
    windows.sessions.Sessions
                        lists Processes with Session information extracted from
                        Environmental Variables
    windows.skeleton_key_check.Skeleton_Key_Check
                        Looks for signs of Skeleton Key malware
    windows.ssdt.SSDT   Lists the system call table.
    windows.statistics.Statistics
    windows.strings.Strings
                        Reads output from the strings command and indicates which
                        process(es) each string belongs to.
    windows.svcscan.SvcScan
                        Scans for windows services.
    windows.symlinkscan.SymlinkScan
                        Scans for links present in a particular windows memory image.
    windows.vadinfo.VadInfo
                        Lists process memory ranges.
    windows.vadyarascan.VadYaraScan
                        Scans all the Virtual Address Descriptor memory maps using
                        yara.
    windows.verinfo.VerInfo
                        Lists version information from PE files.
    windows.virtmap.VirtMap
                        Lists virtual mapped sections.
    yarascan.YaraScan   Scans kernel memory using yara rules (string or file).

We have an Ubuntu machine with Volatility and Volatility 3 already present in the /opt directory, along with all the memory files you need throughout this room. The machine will start in a split-screen view. In case the VM is not visible, use the blue Show Split View button at the top-right of the page.

IP Address: 10.10.73.242

Username: thmanalyst

Password: infected
```
### Memory Extraction
Extracting a memory dump can be performed in numerous ways, varying based on the requirements of your investigation. Listed below are a few of the techniques and tools that can be used to extract a memory from a bare-metal machine.
FTK Imager
Redline
DumpIt.exe
win32dd.exe / win64dd.exe
Memoryze
FastDump
When using an extraction tool on a bare-metal host, it can usually take a considerable amount of time; take this into consideration during your investigation if time is a constraint.
Most of the tools mentioned above for memory extraction will output a .raw file with some exceptions like Redline that can use its own agent and session structure.
![](https://i.imgur.com/AbgGsci.png)
For virtual machines, gathering a memory file can easily be done by collecting the virtual memory file from the host machine’s drive. This file can change depending on the hypervisor used; listed below are a few of the hypervisor virtual memory files you may encounter.
VMWare - .vmem
Hyper-V - .bin
Parallels - .mem
VirtualBox - .sav file *this is only a partial memory file
Exercise caution whenever attempting to extract or move memory from both bare-metal and virtual machines.
```text
┌──(kali㉿kali)-[~/volatility/volatility3]
└─$ unzip 'Practical Investigation Memory Files.zip' 
Archive:  Practical Investigation Memory Files.zip
  inflating: Investigation-1.vmem    

  inflating: Investigation-2.raw
```
```text
┌──(kali㉿kali)-[~/volatility/volatility3]
└─$
```
```text
┌──(kali㉿kali)-[~/volatility/volatility3]
└─$ ls
 API_CHANGES.md         mypy.ini                                    test
 development           'Practical Investigation Memory Files.zip'   volatility3
 doc                    README.md                                   vol.py
 Investigation-1.vmem   requirements-dev.txt                        volshell.py
 Investigation-2.raw    requirements-minimal.txt                    volshell.spec
 LICENSE.txt            requirements.txt                            vol.spec
 MANIFEST.in            setup.py
```
```text
┌──(kali㉿kali)-[~/volatility/volatility3]
└─$ ls -lah
total 1.1G
drwxr-xr-x 8 kali kali 4.0K Nov 27 19:19  .
drwxr-xr-x 3 kali kali 4.0K Nov 27 19:12  ..
-rw-r--r-- 1 kali kali 1.4K Nov 27 19:12  API_CHANGES.md
drwxr-xr-x 3 kali kali 4.0K Nov 27 19:12  development
drwxr-xr-x 3 kali kali 4.0K Nov 27 19:12  doc
drwxr-xr-x 8 kali kali 4.0K Nov 27 19:12  .git
drwxr-xr-x 4 kali kali 4.0K Nov 27 19:12  .github
-rw-r--r-- 1 kali kali  514 Nov 27 19:12  .gitignore
-rw-r--r-- 1 kali kali 512M Mar 12  2021  Investigation-1.vmem
-rw-r--r-- 1 kali kali 512M May 13  2017  Investigation-2.raw
```
Operating System (OS) is a layer between the hardware and the applications. From the application's perspective, the OS provides an interface to access the different hardware components, such as CPU, RAM, and disk storage. Examples of OS are Android, FreeBSD, Linux, macOS, and Windows.
Since converting to Python 3, the plugin structure for Volatility has changed quite drastically. In previous Volatility versions, you would need to identify a specific OS profile exact to the operating system and build version of the host, which could be hard to find or used with a plugin that could provide false positives. With Volatility3, profiles have been scrapped, and Volatility will automatically identify the host and build of the memory file.
The naming structure of plugins has also changed. In previous versions of Volatility, the naming convention has been simply the name of the plugin and was universal for all operating systems and profiles. Now with Volatility3, you need to specify the operating system prior to specifying the plugin to be used, for example, windows.info vs linux.info. This is because there are no longer profiles to distinguish between various operating systems for plugins as each operating system has drastically different memory structures and operations. Look below for options of operating system plugin syntax.
.windows
.linux
.mac
There are several plugins available with Volatility as well as third-party plugins; we will only be covering a small portion of the plugins that Volatility has to offer.
To get familiar with the plugins available, utilize the help menu. As Volatility3 is currently in active development, there is still a short list of plugins compared to its python 2 counterpart; however, the current list still allows you to do all of your analysis as needed.
### Identifying Image Info and Profiles
By default, Volatility comes with all existing Windows profiles from Windows XP to Windows 10.
Image profiles can be hard to determine if you don't know exactly what version and build the machine you extracted a memory dump from was. In some cases, you may be given a memory file with no other context, and it is up to you to figure out where to go from there. In that case, Volatility has your back and comes with the imageinfo plugin. This plugin will take the provided memory dump and assign it a list of the best possible OS profiles. OS profiles have since been deprecated with Volatility3, so we will only need to worry about identifying the profile if using Volatility2; this makes life much easier for analyzing memory dumps.
Note: imageinfo is not always correct and can have varied results depending on the provided dump; use with caution and test multiple profiles from the provided list.
If we are still looking to get information about what the host is running from the memory dump, we can use the following three plugins windows.info linux.info mac.info. This plugin will provide information about the host from the memory dump.
Syntax: python3 vol.py -f <file> windows.info
```text
──(kali㉿kali)-[~/volatility/volatility3]
└─$ python3 vol.py -f Investigation-1.vmem windows.info 
Volatility 3 Framework 2.4.1

Progress:   99.99               Reading Symbol layer                                   Progress:  100.00               PDB scanning finished                                                                                              
Variable        Value

Kernel Base     0x804d7000
DTB     0x2fe000
Symbols file:///home/kali/volatility/volatility3/volatility3/symbols/windows/ntkrnlpa.pdb/30B5FB31AE7E4ACAABA750AA241FF331-1.json.xz
Is64Bit False
IsPAE   True
layer_name      0 WindowsIntelPAE
memory_layer    1 FileLayer
KdDebuggerDataBlock     0x80545ae0
NTBuildLab      2600.xpsp.080413-2111
CSDVersion      3
KdVersionBlock  0x80545ab8
Major/Minor     15.2600
MachineType     332
KeNumberProcessors      1
SystemTime      2012-07-22 02:45:08
NtSystemRoot    C:\WINDOWS
NtProductType   NtProductWinNt
NtMajorVersion  5
NtMinorVersion  1
PE MajorOperatingSystemVersion  5
PE MinorOperatingSystemVersion  1
PE Machine      332
PE TimeDateStamp        Sun Apr 13 18:31:06 2008

thmanalyst@ubuntu:/opt/volatility3$ python3 vol.py -f dump.vmem windows.info
Volatility 3 Framework 1.0.1
Progress:  100.00               PDB scanning finished                     
Variable        Value

Kernel Base     0x804d7000
DTB     0x2fe000
Symbols file:///opt/volatility3/volatility3/symbols/windows/ntkrnlpa.pdb/30B5FB31AE7E4ACAABA750AA241FF331-1.json.xz
Is64Bit False
IsPAE   True
primary 0 WindowsIntelPAE
memory_layer    1 FileLayer
KdDebuggerDataBlock     0x80545ae0
NTBuildLab      2600.xpsp.080413-2111
CSDVersion      3
KdVersionBlock  0x80545ab8
Major/Minor     15.2600
MachineType     332
KeNumberProcessors      1
SystemTime      2012-07-22 02:45:08
NtSystemRoot    C:\WINDOWS
NtProductType   NtProductWinNt
NtMajorVersion  5
NtMinorVersion  1
PE MajorOperatingSystemVersion  5
PE MinorOperatingSystemVersion  1
PE Machine      332
PE TimeDateStamp        Sun Apr 13 18:31:06 2008
```
### Listing Processes and Connections
Five different plugins within Volatility allow you to dump processes and network connections, each with varying techniques used. In this task, we will be discussing each and its pros and cons when it comes to evasion techniques used by adversaries.
The most basic way of listing processes is using pslist; this plugin will get the list of processes from the doubly-linked list that keeps track of processes in memory, equivalent to the process list in task manager. The output from this plugin will include all current processes and terminated processes with their exit times.
Syntax: python3 vol.py -f <file> windows.pslist
Some malware, typically rootkits, will, in an attempt to hide their processes, unlink itself from the list. By unlinking themselves from the list you will no longer see their processes when using pslist. To combat this evasion technique, we can use psscan;this technique of listing processes will locate processes by finding data structures that match _EPROCESS. While this technique can help with evasion countermeasures, it can also cause false positives.
Syntax: python3 vol.py -f <file> windows.psscan
The third process plugin, pstree, does not offer any other kind of special techniques to help identify evasion like the last two plugins; however, this plugin will list all processes based on their parent process ID, using the same methods as pslist. This can be useful for an analyst to get a full story of the processes and what may have been occurring at the time of extraction.
Syntax: python3 vol.py -f <file> windows.pstree
Now that we know how to identify processes, we also need to have a way to identify the network connections present at the time of extraction on the host machine. netstat will attempt to identify all memory structures with a network connection.
Syntax: python3 vol.py -f <file> windows.netstat
Packet capture (PCAP) is a networking practice involving the interception of data packets travelling over a network. Once the packets are captured, they can be stored by IT teams for further analysis. The inspection of these packets allows IT teams to identify issues and solve network problems affecting daily operations.
This command in the current state of volatility3 can be very unstable, particularly around old Windows builds. To combat this, you can utilize other tools like bulk_extractor to extract a PCAP file from the memory file. In some cases, this is preferred in network connections that you cannot identify from Volatility alone. https://tools.kali.org/forensics/bulk-extractor
The last plugin we will cover is dlllist. This plugin will list all DLLs associated with processes at the time of extraction. This can be especially useful once you have done further analysis and can filter output to a specific DLL that might be an indicator for a specific type of malware you believe to be present on the system.
Syntax: python3 vol.py -f <file> windows.dlllist
```text
thmanalyst@ubuntu:/opt/volatility3$ python3 vol.py -f dump.vmem windows.pslist
Volatility 3 Framework 1.0.1
Progress:  100.00               PDB scanning finished                     
PID     PPID    ImageFileName   Offset(V)       Threads Handles SessionId       Wow64 CreateTime       ExitTime        File output

4       0       System  0x823c89c8      53      240     N/A     False   N/A     N/A   Disabled
368     4       smss.exe        0x822f1020      3       19      N/A     False   2012-07-22 02:42:31.000000     N/A     Disabled
584     368     csrss.exe       0x822a0598      9       326     0       False   2012-07-22 02:42:32.000000     N/A     Disabled
608     368     winlogon.exe    0x82298700      23      519     0       False   2012-07-22 02:42:32.000000     N/A     Disabled
652     608     services.exe    0x81e2ab28      16      243     0       False   2012-07-22 02:42:32.000000     N/A     Disabled
664     608     lsass.exe       0x81e2a3b8      24      330     0       False   2012-07-22 02:42:32.000000     N/A     Disabled
824     652     svchost.exe     0x82311360      20      194     0       False   2012-07-22 02:42:33.000000     N/A     Disabled
908     652     svchost.exe     0x81e29ab8      9       226     0       False   2012-07-22 02:42:33.000000     N/A     Disabled
1004    652     svchost.exe     0x823001d0      64      1118    0       False   2012-07-22 02:42:33.000000     N/A     Disabled
1056    652     svchost.exe     0x821dfda0      5       60      0       False   2012-07-22 02:42:33.000000     N/A     Disabled
1220    652     svchost.exe     0x82295650      15      197     0       False   2012-07-22 02:42:35.000000     N/A     Disabled
1484    1464    explorer.exe    0x821dea70      17      415     0       False   2012-07-22 02:42:36.000000     N/A     Disabled
1512    652     spoolsv.exe     0x81eb17b8      14      113     0       False   2012-07-22 02:42:36.000000     N/A     Disabled
1640    1484    reader_sl.exe   0x81e7bda0      5       39      0       False   2012-07-22 02:42:36.000000     N/A     Disabled
788     652     alg.exe 0x820e8da0      7       104     0       False   2012-07-22 02:43:01.000000     N/A     Disabled
1136    1004    wuauclt.exe     0x821fcda0      8       173     0       False   2012-07-22 02:43:46.000000     N/A     Disabled
1588    1004    wuauclt.exe     0x8205bda0      5       132     0       False   2012-07-22 02:44:01.000000     N/A     Disabled

thmanalyst@ubuntu:/opt/volatility3$ python3 vol.py -f dump.vmem windows.psscan
Volatility 3 Framework 1.0.1
Progress:  100.00               PDB scanning finished                     
PID     PPID    ImageFileName   Offset  Threads Handles SessionId       Wow64   CreateTime     ExitTime        File output

908     652     svchost.exe     0x2029ab8       9       226     0       False   2012-07-22 02:42:33.000000     N/A     Disabled
664     608     lsass.exe       0x202a3b8       24      330     0       False   2012-07-22 02:42:32.000000     N/A     Disabled
652     608     services.exe    0x202ab28       16      243     0       False   2012-07-22 02:42:32.000000     N/A     Disabled
1640    1484    reader_sl.exe   0x207bda0       5       39      0       False   2012-07-22 02:42:36.000000     N/A     Disabled
1512    652     spoolsv.exe     0x20b17b8       14      113     0       False   2012-07-22 02:42:36.000000     N/A     Disabled
1588    1004    wuauclt.exe     0x225bda0       5       132     0       False   2012-07-22 02:44:01.000000     N/A     Disabled
788     652     alg.exe 0x22e8da0       7       104     0       False   2012-07-22 02:43:01.000000     N/A     Disabled
1484    1464    explorer.exe    0x23dea70       17      415     0       False   2012-07-22 02:42:36.000000     N/A     Disabled
1056    652     svchost.exe     0x23dfda0       5       60      0       False   2012-07-22 02:42:33.000000     N/A     Disabled
1136    1004    wuauclt.exe     0x23fcda0       8       173     0       False   2012-07-22 02:43:46.000000     N/A     Disabled
1220    652     svchost.exe     0x2495650       15      197     0       False   2012-07-22 02:42:35.000000     N/A     Disabled
608     368     winlogon.exe    0x2498700       23      519     0       False   2012-07-22 02:42:32.000000     N/A     Disabled
584     368     csrss.exe       0x24a0598       9       326     0       False   2012-07-22 02:42:32.000000     N/A     Disabled
368     4       smss.exe        0x24f1020       3       19      N/A     False   2012-07-22 02:42:31.000000     N/A     Disabled
1004    652     svchost.exe     0x25001d0       64      1118    0       False   2012-07-22 02:42:33.000000     N/A     Disabled
824     652     svchost.exe     0x2511360       20      194     0       False   2012-07-22 02:42:33.000000     N/A     Disabled
4       0       System  0x25c89c8       53      240     N/A     False   N/A     N/A   Disabled

thmanalyst@ubuntu:/opt/volatility3$ python3 vol.py -f dump.vmem windows.pstree
Volatility 3 Framework 1.0.1
Progress:  100.00               PDB scanning finished                     
PID     PPID    ImageFileName   Offset(V)       Threads Handles SessionId       Wow64 CreateTime       ExitTime

4       0       System  0x8205bda0      53      240     N/A     False   N/A     N/A
* 368   4       smss.exe        0x8205bda0      3       19      N/A     False   2012-07-22 02:42:31.000000     N/A
** 584  368     csrss.exe       0x8205bda0      9       326     0       False   2012-07-22 02:42:32.000000     N/A
** 608  368     winlogon.exe    0x8205bda0      23      519     0       False   2012-07-22 02:42:32.000000     N/A
*** 664 608     lsass.exe       0x8205bda0      24      330     0       False   2012-07-22 02:42:32.000000     N/A
*** 652 608     services.exe    0x8205bda0      16      243     0       False   2012-07-22 02:42:32.000000     N/A
**** 1056       652     svchost.exe     0x8205bda0      5       60      0       False 2012-07-22 02:42:33.000000       N/A
**** 1220       652     svchost.exe     0x8205bda0      15      197     0       False 2012-07-22 02:42:35.000000       N/A
**** 1512       652     spoolsv.exe     0x8205bda0      14      113     0       False 2012-07-22 02:42:36.000000       N/A
**** 908        652     svchost.exe     0x8205bda0      9       226     0       False 2012-07-22 02:42:33.000000       N/A
**** 1004       652     svchost.exe     0x8205bda0      64      1118    0       False 2012-07-22 02:42:33.000000       N/A
***** 1136      1004    wuauclt.exe     0x8205bda0      8       173     0       False 2012-07-22 02:43:46.000000       N/A
***** 1588      1004    wuauclt.exe     0x8205bda0      5       132     0       False 2012-07-22 02:44:01.000000       N/A
**** 788        652     alg.exe 0x8205bda0      7       104     0       False   2012-07-22 02:43:01.000000     N/A
**** 824        652     svchost.exe     0x8205bda0      20      194     0       False 2012-07-22 02:42:33.000000       N/A
1484    1464    explorer.exe    0x8205bda0      17      415     0       False   2012-07-22 02:42:36.000000     N/A
* 1640  1484    reader_sl.exe   0x8205bda0      5       39      0       False   2012-07-22 02:42:36.000000     N/A

thmanalyst@ubuntu:/opt/volatility3$ python3 vol.py -f dump.vmem windows.dlllist
Volatility 3 Framework 1.0.1
Progress:  100.00               PDB scanning finished                     
PID     Process Base    Size    Name    Path    LoadTime        File output

368     smss.exe        0x48580000      0xf000  smss.exe        \SystemRoot\System32\smss.exe  N/A     Disabled
368     smss.exe        0x7c900000      0xaf000 ntdll.dll       C:\WINDOWS\system32\ntdll.dll  N/A     Disabled
584     csrss.exe       0x4a680000      0x5000  csrss.exe       \??\C:\WINDOWS\system32\csrss.exe      N/A     Disabled
584     csrss.exe       0x7c900000      0xaf000 ntdll.dll       C:\WINDOWS\system32\ntdll.dll  N/A     Disabled
584     csrss.exe       0x75b40000      0xb000  CSRSRV.dll      C:\WINDOWS\system32\CSRSRV.dll N/A     Disabled
584     csrss.exe       0x75b50000      0x10000 basesrv.dll     C:\WINDOWS\system32\basesrv.dll        N/A     Disabled
584     csrss.exe       0x75b60000      0x4b000 winsrv.dll      C:\WINDOWS\system32\winsrv.dll N/A     Disabled
584     csrss.exe       0x77f10000      0x49000 GDI32.dll       C:\WINDOWS\system32\GDI32.dll  N/A     Disabled
584     csrss.exe       0x7c800000      0xf6000 KERNEL32.dll    C:\WINDOWS\system32\KERNEL32.dll       N/A     Disabled
584     csrss.exe       0x7e410000      0x91000 USER32.dll      C:\WINDOWS\system32\USER32.dll N/A     Disabled
584     csrss.exe       0x7e720000      0xb0000 sxs.dll C:\WINDOWS\system32\sxs.dll   N/A      Disabled
584     csrss.exe       0x77dd0000      0x9b000 ADVAPI32.dll    C:\WINDOWS\system32\ADVAPI32.dll       N/A     Disabled
584     csrss.exe       0x77e70000      0x92000 RPCRT4.dll      C:\WINDOWS\system32\RPCRT4.dll N/A     Disabled
584     csrss.exe       0x77fe0000      0x11000 Secur32.dll     C:\WINDOWS\system32\Secur32.dll        N/A     Disabled
608     winlogon.exe    0x1000000       0x81000 winlogon.exe    \??\C:\WINDOWS\system32\winlogon.exe   N/A     Disabled
608     winlogon.exe    0x7c900000      0xaf000 ntdll.dll       C:\WINDOWS\system32\ntdll.dll  N/A     Disabled
608     winlogon.exe    0x7c800000      0xf6000 kernel32.dll    C:\WINDOWS\system32\kernel32.dll       N/A     Disabled
608     winlogon.exe    0x77dd0000      0x9b000 ADVAPI32.dll    C:\WINDOWS\system32\ADVAPI32.dll       N/A     Disabled
608     winlogon.exe    0x77e70000      0x92000 RPCRT4.dll      C:\WINDOWS\system32\RPCRT4.dll N/A     Disabled
608     winlogon.exe    0x77fe0000      0x11000 Secur32.dll     C:\WINDOWS\system32\Secur32.dll        N/A     Disabled
608     winlogon.exe    0x776c0000      0x12000 AUTHZ.dll       C:\WINDOWS\system32\AUTHZ.dll  N/A     Disabled
608     winlogon.exe    0x77c10000      0x58000 msvcrt.dll      C:\WINDOWS\system32\msvcrt.dll N/A     Disabled
608     winlogon.exe    0x77a80000      0x95000 CRYPT32.dll     C:\WINDOWS\system32\CRYPT32.dll        N/A     Disabled
608     winlogon.exe    0x77b20000      0x12000 MSASN1.dll      C:\WINDOWS\system32\MSASN1.dll N/A     Disabled
608     winlogon.exe    0x7e410000      0x91000 USER32.dll      C:\WINDOWS\system32\USER32.dll N/A     Disabled
608     winlogon.exe    0x77f10000      0x49000 GDI32.dll       C:\WINDOWS\system32\GDI32.dll  N/A     Disabled
608     winlogon.exe    0x75940000      0x8000  NDdeApi.dll     C:\WINDOWS\system32\NDdeApi.dll        N/A     Disabled
608     winlogon.exe    0x75930000      0xa000  PROFMAP.dll     C:\WINDOWS\system32\PROFMAP.dll        N/A     Disabled
608     winlogon.exe    0x5b860000      0x55000 NETAPI32.dll    C:\WINDOWS\system32\NETAPI32.dll       N/A     Disabled
608     winlogon.exe    0x769c0000      0xb4000 USERENV.dll     C:\WINDOWS\system32\USERENV.dll        N/A     Disabled
608     winlogon.exe    0x76bf0000      0xb000  PSAPI.DLL       C:\WINDOWS\system32\PSAPI.DLL  N/A     Disabled
608     winlogon.exe    0x76bc0000      0xf000  REGAPI.dll      C:\WINDOWS\system32\REGAPI.dll N/A     Disabled
608     winlogon.exe    0x77920000      0xf3000 SETUPAPI.dll    C:\WINDOWS\system32\SETUPAPI.dll       N/A     Disabled
608     winlogon.exe    0x77c00000      0x8000  VERSION.dll     C:\WINDOWS\system32\VERSION.dll        N/A     Disabled
608     winlogon.exe    0x76360000      0x10000 WINSTA.dll      C:\WINDOWS\system32\WINSTA.dll N/A     Disabled
608     winlogon.exe    0x76c30000      0x2e000 WINTRUST.dll    C:\WINDOWS\system32\WINTRUST.dll       N/A     Disabled
608     winlogon.exe    0x76c90000      0x28000 IMAGEHLP.dll    C:\WINDOWS\system32\IMAGEHLP.dll       N/A     Disabled
608     winlogon.exe    0x71ab0000      0x17000 WS2_32.dll      C:\WINDOWS\system32\WS2_32.dll N/A     Disabled
608     winlogon.exe    0x71aa0000      0x8000  WS2HELP.dll     C:\WINDOWS\system32\WS2HELP.dll        N/A     Disabled
608     winlogon.exe    0x75970000      0xf8000 MSGINA.dll      C:\WINDOWS\system32\MSGINA.dll N/A     Disabled
608     winlogon.exe    0x5d090000      0x9a000 COMCTL32.dll    C:\WINDOWS\system32\COMCTL32.dll       N/A     Disabled
608     winlogon.exe    0x74320000      0x3d000 ODBC32.dll      C:\WINDOWS\system32\ODBC32.dll N/A     Disabled
608     winlogon.exe    0x763b0000      0x49000 comdlg32.dll    C:\WINDOWS\system32\comdlg32.dll       N/A     Disabled
608     winlogon.exe    0x7c9c0000      0x817000        SHELL32.dll     C:\WINDOWS\system32\SHELL32.dll        N/A     Disabled
608     winlogon.exe    0x77f60000      0x76000 SHLWAPI.dll     C:\WINDOWS\system32\SHLWAPI.dll        N/A     Disabled
608     winlogon.exe    0x773d0000      0x103000        comctl32.dll    C:\WINDOWS\WinSxS\x86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.5512_x-ww_35d4ce83\comctl32.dll     N/A     Disabled
608     winlogon.exe    0x930000        0x17000 odbcint.dll     C:\WINDOWS\system32\odbcint.dll        N/A     Disabled
608     winlogon.exe    0x776e0000      0x23000 SHSVCS.dll      C:\WINDOWS\system32\SHSVCS.dll N/A     Disabled
608     winlogon.exe    0x76bb0000      0x5000  sfc.dll C:\WINDOWS\system32\sfc.dll   N/A      Disabled
608     winlogon.exe    0x76c60000      0x2a000 sfc_os.dll      C:\WINDOWS\system32\sfc_os.dll N/A     Disabled
608     winlogon.exe    0x774e0000      0x13d000        ole32.dll       C:\WINDOWS\system32\ole32.dll  N/A     Disabled
608     winlogon.exe    0x77b40000      0x22000 Apphelp.dll     C:\WINDOWS\system32\Apphelp.dll        N/A     Disabled
608     winlogon.exe    0x723d0000      0x1c000 WINSCARD.DLL    C:\WINDOWS\system32\WINSCARD.DLL       N/A     Disabled
608     winlogon.exe    0x76f50000      0x8000  WTSAPI32.dll    C:\WINDOWS\system32\WTSAPI32.dll       N/A     Disabled
608     winlogon.exe    0x7e720000      0xb0000 sxs.dll C:\WINDOWS\system32\sxs.dll   N/A      Disabled
608     winlogon.exe    0x5ad70000      0x38000 uxtheme.dll     C:\WINDOWS\system32\uxtheme.dll        N/A     Disabled
608     winlogon.exe    0x76b40000      0x2d000 WINMM.dll       C:\WINDOWS\system32\WINMM.dll  N/A     Disabled
608     winlogon.exe    0x76600000      0x1d000 cscdll.dll      C:\WINDOWS\system32\cscdll.dll N/A     Disabled
608     winlogon.exe    0x47020000      0x8000  dimsntfy.dll    C:\WINDOWS\System32\dimsntfy.dll       N/A     Disabled
608     winlogon.exe    0x75950000      0x1a000 WlNotify.dll    C:\WINDOWS\system32\WlNotify.dll       N/A     Disabled
608     winlogon.exe    0x71b20000      0x12000 MPR.dll C:\WINDOWS\system32\MPR.dll   N/A      Disabled
608     winlogon.exe    0x73000000      0x26000 WINSPOOL.DRV    C:\WINDOWS\system32\WINSPOOL.DRV       N/A     Disabled
608     winlogon.exe    0x68000000      0x36000 rsaenh.dll      C:\WINDOWS\system32\rsaenh.dll N/A     Disabled
608     winlogon.exe    0x71bf0000      0x13000 SAMLIB.dll      C:\WINDOWS\system32\SAMLIB.dll N/A     Disabled
608     winlogon.exe    0x77a20000      0x54000 cscui.dll       C:\WINDOWS\system32\cscui.dll  N/A     Disabled
608     winlogon.exe    0x77c70000      0x24000 msv1_0.dll      C:\WINDOWS\system32\msv1_0.dll N/A     Disabled
608     winlogon.exe    0x76d60000      0x19000 iphlpapi.dll    C:\WINDOWS\system32\iphlpapi.dll       N/A     Disabled
608     winlogon.exe    0x76d40000      0x18000 MPRAPI.dll      C:\WINDOWS\system32\MPRAPI.dll N/A     Disabled
608     winlogon.exe    0x77cc0000      0x32000 ACTIVEDS.dll    C:\WINDOWS\system32\ACTIVEDS.dll       N/A     Disabled
608     winlogon.exe    0x76e10000      0x25000 adsldpc.dll     C:\WINDOWS\system32\adsldpc.dll        N/A     Disabled
608     winlogon.exe    0x76f60000      0x2c000 WLDAP32.dll     C:\WINDOWS\system32\WLDAP32.dll        N/A     Disabled
608     winlogon.exe    0x76b20000      0x11000 ATL.DLL C:\WINDOWS\system32\ATL.DLL   N/A      Disabled
608     winlogon.exe    0x77120000      0x8b000 OLEAUT32.dll    C:\WINDOWS\system32\OLEAUT32.dll       N/A     Disabled
608     winlogon.exe    0x76e80000      0xe000  rtutils.dll     C:\WINDOWS\system32\rtutils.dll        N/A     Disabled
608     winlogon.exe    0x1630000       0x2c5000        xpsp2res.dll    C:\WINDOWS\system32\xpsp2res.dll       N/A     Disabled
608     winlogon.exe    0x77690000      0x21000 NTMARTA.DLL     C:\WINDOWS\system32\NTMARTA.DLL        N/A     Disabled
608     winlogon.exe    0x72d20000      0x9000  wdmaud.drv      C:\WINDOWS\system32\wdmaud.drv N/A     Disabled
608     winlogon.exe    0x72d10000      0x8000  msacm32.drv     C:\WINDOWS\system32\msacm32.drv        N/A     Disabled
608     winlogon.exe    0x77be0000      0x15000 MSACM32.dll     C:\WINDOWS\system32\MSACM32.dll        N/A     Disabled
608     winlogon.exe    0x77bd0000      0x7000  midimap.dll     C:\WINDOWS\system32\midimap.dll        N/A     Disabled
608     winlogon.exe    0x77050000      0xc5000 COMRes.dll      C:\WINDOWS\system32\COMRes.dll N/A     Disabled
608     winlogon.exe    0x76fd0000      0x7f000 CLBCATQ.DLL     C:\WINDOWS\system32\CLBCATQ.DLL        N/A     Disabled
652     services.exe    0x1000000       0x1c000 services.exe    C:\WINDOWS\system32\services.exe       N/A     Disabled
652     services.exe    0x7c900000      0xaf000 ntdll.dll       C:\WINDOWS\system32\ntdll.dll  N/A     Disabled
652     services.exe    0x7c800000      0xf6000 kernel32.dll    C:\WINDOWS\system32\kernel32.dll       N/A     Disabled
652     services.exe    0x77dd0000      0x9b000 ADVAPI32.dll    C:\WINDOWS\system32\ADVAPI32.dll       N/A     Disabled
652     services.exe    0x77e70000      0x92000 RPCRT4.dll      C:\WINDOWS\system32\RPCRT4.dll N/A     Disabled
652     services.exe    0x77fe0000      0x11000 Secur32.dll     C:\WINDOWS\system32\Secur32.dll        N/A     Disabled
652     services.exe    0x77c10000      0x58000 msvcrt.dll      C:\WINDOWS\system32\msvcrt.dll N/A     Disabled
652     services.exe    0x5f770000      0xc000  NCObjAPI.DLL    C:\WINDOWS\system32\NCObjAPI.DLL       N/A     Disabled
652     services.exe    0x76080000      0x65000 MSVCP60.dll     C:\WINDOWS\system32\MSVCP60.dll        N/A     Disabled
652     services.exe    0x7dbd0000      0x51000 SCESRV.dll      C:\WINDOWS\system32\SCESRV.dll N/A     Disabled
652     services.exe    0x776c0000      0x12000 AUTHZ.dll       C:\WINDOWS\system32\AUTHZ.dll  N/A     Disabled
652     services.exe    0x7e410000      0x91000 USER32.dll      C:\WINDOWS\system32\USER32.dll N/A     Disabled
652     services.exe    0x77f10000      0x49000 GDI32.dll       C:\WINDOWS\system32\GDI32.dll  N/A     Disabled
652     services.exe    0x769c0000      0xb4000 USERENV.dll     C:\WINDOWS\system32\USERENV.dll        N/A     Disabled
652     services.exe    0x7dba0000      0x21000 umpnpmgr.dll    C:\WINDOWS\system32\umpnpmgr.dll       N/A     Disabled
652     services.exe    0x76360000      0x10000 WINSTA.dll      C:\WINDOWS\system32\WINSTA.dll N/A     Disabled
652     services.exe    0x5b860000      0x55000 NETAPI32.dll    C:\WINDOWS\system32\NETAPI32.dll       N/A     Disabled
652     services.exe    0x5cb70000      0x26000 ShimEng.dll     C:\WINDOWS\system32\ShimEng.dll        N/A     Disabled
652     services.exe    0x47260000      0xf000  AcAdProc.dll    C:\WINDOWS\AppPatch\AcAdProc.dll       N/A     Disabled
652     services.exe    0x77b40000      0x22000 Apphelp.dll     C:\WINDOWS\system32\Apphelp.dll        N/A     Disabled
652     services.exe    0x77c00000      0x8000  VERSION.dll     C:\WINDOWS\system32\VERSION.dll        N/A     Disabled
652     services.exe    0x77b70000      0x11000 eventlog.dll    C:\WINDOWS\system32\eventlog.dll       N/A     Disabled
652     services.exe    0x76bf0000      0xb000  PSAPI.DLL       C:\WINDOWS\system32\PSAPI.DLL  N/A     Disabled
652     services.exe    0x71ab0000      0x17000 WS2_32.dll      C:\WINDOWS\system32\WS2_32.dll N/A     Disabled
652     services.exe    0x71aa0000      0x8000  WS2HELP.dll     C:\WINDOWS\system32\WS2HELP.dll        N/A     Disabled
652     services.exe    0x76f50000      0x8000  wtsapi32.dll    C:\WINDOWS\system32\wtsapi32.dll       N/A     Disabled
664     lsass.exe       0x1000000       0x6000  lsass.exe       C:\WINDOWS\system32\lsass.exe  N/A     Disabled
664     lsass.exe       0x7c900000      0xaf000 ntdll.dll       C:\WINDOWS\system32\ntdll.dll  N/A     Disabled
664     lsass.exe       0x7c800000      0xf6000 kernel32.dll    C:\WINDOWS\system32\kernel32.dll       N/A     Disabled
664     lsass.exe       0x77dd0000      0x9b000 ADVAPI32.dll    C:\WINDOWS\system32\ADVAPI32.dll       N/A     Disabled
664     lsass.exe       0x77e70000      0x92000 RPCRT4.dll      C:\WINDOWS\system32\RPCRT4.dll N/A     Disabled
664     lsass.exe       0x77fe0000      0x11000 Secur32.dll     C:\WINDOWS\system32\Secur32.dll        N/A     Disabled
664     lsass.exe       0x75730000      0xb5000 LSASRV.dll      C:\WINDOWS\system32\LSASRV.dll N/A     Disabled
664     lsass.exe       0x71b20000      0x12000 MPR.dll C:\WINDOWS\system32\MPR.dll   N/A      Disabled
664     lsass.exe       0x7e410000      0x91000 USER32.dll      C:\WINDOWS\system32\USER32.dll N/A     Disabled
664     lsass.exe       0x77f10000      0x49000 GDI32.dll       C:\WINDOWS\system32\GDI32.dll  N/A     Disabled
664     lsass.exe       0x77b20000      0x12000 MSASN1.dll      C:\WINDOWS\system32\MSASN1.dll N/A     Disabled
664     lsass.exe       0x77c10000      0x58000 msvcrt.dll      C:\WINDOWS\system32\msvcrt.dll N/A     Disabled
664     lsass.exe       0x5b860000      0x55000 NETAPI32.dll    C:\WINDOWS\system32\NETAPI32.dll       N/A     Disabled
664     lsass.exe       0x767a0000      0x13000 NTDSAPI.dll     C:\WINDOWS\system32\NTDSAPI.dll        N/A     Disabled
664     lsass.exe       0x76f20000      0x27000 DNSAPI.dll      C:\WINDOWS\system32\DNSAPI.dll N/A     Disabled
664     lsass.exe       0x71ab0000      0x17000 WS2_32.dll      C:\WINDOWS\system32\WS2_32.dll N/A     Disabled
664     lsass.exe       0x71aa0000      0x8000  WS2HELP.dll     C:\WINDOWS\system32\WS2HELP.dll        N/A     Disabled
664     lsass.exe       0x76f60000      0x2c000 WLDAP32.dll     C:\WINDOWS\system32\WLDAP32.dll        N/A     Disabled
664     lsass.exe       0x71bf0000      0x13000 SAMLIB.dll      C:\WINDOWS\system32\SAMLIB.dll N/A     Disabled
664     lsass.exe       0x74440000      0x6a000 SAMSRV.dll      C:\WINDOWS\system32\SAMSRV.dll N/A     Disabled
664     lsass.exe       0x76790000      0xc000  cryptdll.dll    C:\WINDOWS\system32\cryptdll.dll       N/A     Disabled
664     lsass.exe       0x5cb70000      0x26000 ShimEng.dll     C:\WINDOWS\system32\ShimEng.dll        N/A     Disabled
664     lsass.exe       0x6f880000      0x1ca000        AcGenral.DLL    C:\WINDOWS\AppPatch\AcGenral.DLL       N/A     Disabled
664     lsass.exe       0x76b40000      0x2d000 WINMM.dll       C:\WINDOWS\system32\WINMM.dll  N/A     Disabled
664     lsass.exe       0x774e0000      0x13d000        ole32.dll       C:\WINDOWS\system32\ole32.dll  N/A     Disabled
664     lsass.exe       0x77120000      0x8b000 OLEAUT32.dll    C:\WINDOWS\system32\OLEAUT32.dll       N/A     Disabled
664     lsass.exe       0x77be0000      0x15000 MSACM32.dll     C:\WINDOWS\system32\MSACM32.dll        N/A     Disabled
664     lsass.exe       0x77c00000      0x8000  VERSION.dll     C:\WINDOWS\system32\VERSION.dll        N/A     Disabled
664     lsass.exe       0x7c9c0000      0x817000        SHELL32.dll     C:\WINDOWS\system32\SHELL32.dll        N/A     Disabled
664     lsass.exe       0x77f60000      0x76000 SHLWAPI.dll     C:\WINDOWS\system32\SHLWAPI.dll        N/A     Disabled
664     lsass.exe       0x769c0000      0xb4000 USERENV.dll     C:\WINDOWS\system32\USERENV.dll        N/A     Disabled
664     lsass.exe       0x5ad70000      0x38000 UxTheme.dll     C:\WINDOWS\system32\UxTheme.dll        N/A     Disabled
664     lsass.exe       0x773d0000      0x103000        comctl32.dll    C:\WINDOWS\WinSxS\x86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.5512_x-ww_35d4ce83\comctl32.dll     N/A     Disabled
664     lsass.exe       0x5d090000      0x9a000 comctl32.dll    C:\WINDOWS\system32\comctl32.dll       N/A     Disabled
664     lsass.exe       0x4d200000      0xe000  msprivs.dll     C:\WINDOWS\system32\msprivs.dll        N/A     Disabled
664     lsass.exe       0x71cf0000      0x4c000 kerberos.dll    C:\WINDOWS\system32\kerberos.dll       N/A     Disabled
664     lsass.exe       0x77c70000      0x24000 msv1_0.dll      C:\WINDOWS\system32\msv1_0.dll N/A     Disabled
664     lsass.exe       0x76d60000      0x19000 iphlpapi.dll    C:\WINDOWS\system32\iphlpapi.dll       N/A     Disabled
664     lsass.exe       0x744b0000      0x65000 netlogon.dll    C:\WINDOWS\system32\netlogon.dll       N/A     Disabled
664     lsass.exe       0x767c0000      0x2c000 w32time.dll     C:\WINDOWS\system32\w32time.dll        N/A     Disabled
664     lsass.exe       0x76080000      0x65000 MSVCP60.dll     C:\WINDOWS\system32\MSVCP60.dll        N/A     Disabled
664     lsass.exe       0x767f0000      0x27000 schannel.dll    C:\WINDOWS\system32\schannel.dll       N/A     Disabled
664     lsass.exe       0x77a80000      0x95000 CRYPT32.dll     C:\WINDOWS\system32\CRYPT32.dll        N/A     Disabled
664     lsass.exe       0x74380000      0xf000  wdigest.dll     C:\WINDOWS\system32\wdigest.dll        N/A     Disabled
664     lsass.exe       0x68000000      0x36000 rsaenh.dll      C:\WINDOWS\system32\rsaenh.dll N/A     Disabled
664     lsass.exe       0x77920000      0xf3000 setupapi.dll    C:\WINDOWS\system32\setupapi.dll       N/A     Disabled
664     lsass.exe       0x74410000      0x2f000 scecli.dll      C:\WINDOWS\system32\scecli.dll N/A     Disabled
664     lsass.exe       0x743e0000      0x2f000 ipsecsvc.dll    C:\WINDOWS\system32\ipsecsvc.dll       N/A     Disabled
664     lsass.exe       0x776c0000      0x12000 AUTHZ.dll       C:\WINDOWS\system32\AUTHZ.dll  N/A     Disabled
664     lsass.exe       0x75d90000      0xd0000 oakley.DLL      C:\WINDOWS\system32\oakley.DLL N/A     Disabled
664     lsass.exe       0x74370000      0xb000  WINIPSEC.DLL    C:\WINDOWS\system32\WINIPSEC.DLL       N/A     Disabled
664     lsass.exe       0x71a50000      0x3f000 mswsock.dll     C:\WINDOWS\system32\mswsock.dll        N/A     Disabled
664     lsass.exe       0x662b0000      0x58000 hnetcfg.dll     C:\WINDOWS\system32\hnetcfg.dll        N/A     Disabled
664     lsass.exe       0x71a90000      0x8000  wshtcpip.dll    C:\WINDOWS\System32\wshtcpip.dll       N/A     Disabled
664     lsass.exe       0x743a0000      0xb000  pstorsvc.dll    C:\WINDOWS\system32\pstorsvc.dll       N/A     Disabled
664     lsass.exe       0x743c0000      0x1b000 psbase.dll      C:\WINDOWS\system32\psbase.dll N/A     Disabled
664     lsass.exe       0x68100000      0x26000 dssenh.dll      C:\WINDOWS\system32\dssenh.dll N/A     Disabled
824     svchost.exe     0x1000000       0x6000  svchost.exe     C:\WINDOWS\system32\svchost.exe        N/A     Disabled
824     svchost.exe     0x7c900000      0xaf000 ntdll.dll       C:\WINDOWS\system32\ntdll.dll  N/A     Disabled
824     svchost.exe     0x7c800000      0xf6000 kernel32.dll    C:\WINDOWS\system32\kernel32.dll       N/A     Disabled
824     svchost.exe     0x77dd0000      0x9b000 ADVAPI32.dll    C:\WINDOWS\system32\ADVAPI32.dll       N/A     Disabled
824     svchost.exe     0x77e70000      0x92000 RPCRT4.dll      C:\WINDOWS\system32\RPCRT4.dll N/A     Disabled
824     svchost.exe     0x77fe0000      0x11000 Secur32.dll     C:\WINDOWS\system32\Secur32.dll        N/A     Disabled
824     svchost.exe     0x5cb70000      0x26000 ShimEng.dll     C:\WINDOWS\system32\ShimEng.dll        N/A     Disabled
824     svchost.exe     0x6f880000      0x1ca000        AcGenral.DLL    C:\WINDOWS\AppPatch\AcGenral.DLL       N/A     Disabled
824     svchost.exe     0x7e410000      0x91000 USER32.dll      C:\WINDOWS\system32\USER32.dll N/A     Disabled
824     svchost.exe     0x77f10000      0x49000 GDI32.dll       C:\WINDOWS\system32\GDI32.dll  N/A     Disabled
824     svchost.exe     0x76b40000      0x2d000 WINMM.dll       C:\WINDOWS\system32\WINMM.dll  N/A     Disabled
824     svchost.exe     0x774e0000      0x13d000        ole32.dll       C:\WINDOWS\system32\ole32.dll  N/A     Disabled
824     svchost.exe     0x77c10000      0x58000 msvcrt.dll      C:\WINDOWS\system32\msvcrt.dll N/A     Disabled
824     svchost.exe     0x77120000      0x8b000 OLEAUT32.dll    C:\WINDOWS\system32\OLEAUT32.dll       N/A     Disabled
824     svchost.exe     0x77be0000      0x15000 MSACM32.dll     C:\WINDOWS\system32\MSACM32.dll        N/A     Disabled
824     svchost.exe     0x77c00000      0x8000  VERSION.dll     C:\WINDOWS\system32\VERSION.dll        N/A     Disabled
824     svchost.exe     0x7c9c0000      0x817000        SHELL32.dll     C:\WINDOWS\system32\SHELL32.dll        N/A     Disabled
824     svchost.exe     0x77f60000      0x76000 SHLWAPI.dll     C:\WINDOWS\system32\SHLWAPI.dll        N/A     Disabled
824     svchost.exe     0x769c0000      0xb4000 USERENV.dll     C:\WINDOWS\system32\USERENV.dll        N/A     Disabled
824     svchost.exe     0x5ad70000      0x38000 UxTheme.dll     C:\WINDOWS\system32\UxTheme.dll        N/A     Disabled
824     svchost.exe     0x773d0000      0x103000        comctl32.dll    C:\WINDOWS\WinSxS\x86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.5512_x-ww_35d4ce83\comctl32.dll     N/A     Disabled
824     svchost.exe     0x5d090000      0x9a000 comctl32.dll    C:\WINDOWS\system32\comctl32.dll       N/A     Disabled
824     svchost.exe     0x77690000      0x21000 NTMARTA.DLL     C:\WINDOWS\system32\NTMARTA.DLL        N/A     Disabled
824     svchost.exe     0x71bf0000      0x13000 SAMLIB.dll      C:\WINDOWS\system32\SAMLIB.dll N/A     Disabled
824     svchost.exe     0x76f60000      0x2c000 WLDAP32.dll     C:\WINDOWS\system32\WLDAP32.dll        N/A     Disabled
824     svchost.exe     0x76a80000      0x64000 rpcss.dll       c:\windows\system32\rpcss.dll  N/A     Disabled
824     svchost.exe     0x71ab0000      0x17000 WS2_32.dll      c:\windows\system32\WS2_32.dll N/A     Disabled
824     svchost.exe     0x71aa0000      0x8000  WS2HELP.dll     c:\windows\system32\WS2HELP.dll        N/A     Disabled
824     svchost.exe     0x670000        0x2c5000        xpsp2res.dll    C:\WINDOWS\system32\xpsp2res.dll       N/A     Disabled
824     svchost.exe     0x76fd0000      0x7f000 CLBCATQ.DLL     C:\WINDOWS\system32\CLBCATQ.DLL        N/A     Disabled
824     svchost.exe     0x77050000      0xc5000 COMRes.dll      C:\WINDOWS\system32\COMRes.dll N/A     Disabled
824     svchost.exe     0x760f0000      0x53000 termsrv.dll     c:\windows\system32\termsrv.dll        N/A     Disabled
824     svchost.exe     0x74f70000      0x6000  ICAAPI.dll      c:\windows\system32\ICAAPI.dll N/A     Disabled
824     svchost.exe     0x77920000      0xf3000 SETUPAPI.dll    c:\windows\system32\SETUPAPI.dll       N/A     Disabled
824     svchost.exe     0x76c30000      0x2e000 WINTRUST.dll    C:\WINDOWS\system32\WINTRUST.dll       N/A     Disabled
824     svchost.exe     0x77a80000      0x95000 CRYPT32.dll     C:\WINDOWS\system32\CRYPT32.dll        N/A     Disabled
824     svchost.exe     0x77b20000      0x12000 MSASN1.dll      C:\WINDOWS\system32\MSASN1.dll N/A     Disabled
824     svchost.exe     0x76c90000      0x28000 IMAGEHLP.dll    C:\WINDOWS\system32\IMAGEHLP.dll       N/A     Disabled
824     svchost.exe     0x776c0000      0x12000 AUTHZ.dll       c:\windows\system32\AUTHZ.dll  N/A     Disabled
824     svchost.exe     0x75110000      0x1f000 mstlsapi.dll    c:\windows\system32\mstlsapi.dll       N/A     Disabled
824     svchost.exe     0x77cc0000      0x32000 ACTIVEDS.dll    c:\windows\system32\ACTIVEDS.dll       N/A     Disabled
824     svchost.exe     0x76e10000      0x25000 adsldpc.dll     c:\windows\system32\adsldpc.dll        N/A     Disabled
824     svchost.exe     0x5b860000      0x55000 NETAPI32.dll    C:\WINDOWS\system32\NETAPI32.dll       N/A     Disabled
824     svchost.exe     0x76b20000      0x11000 ATL.DLL c:\windows\system32\ATL.DLL   N/A      Disabled
824     svchost.exe     0x76bc0000      0xf000  REGAPI.dll      C:\WINDOWS\system32\REGAPI.dll N/A     Disabled
824     svchost.exe     0x68000000      0x36000 rsaenh.dll      C:\WINDOWS\system32\rsaenh.dll N/A     Disabled
908     svchost.exe     0x1000000       0x6000  svchost.exe     C:\WINDOWS\system32\svchost.exe        N/A     Disabled
908     svchost.exe     0x7c900000      0xaf000 ntdll.dll       C:\WINDOWS\system32\ntdll.dll  N/A     Disabled
908     svchost.exe     0x7c800000      0xf6000 kernel32.dll    C:\WINDOWS\system32\kernel32.dll       N/A     Disabled
908     svchost.exe     0x77dd0000      0x9b000 ADVAPI32.dll    C:\WINDOWS\system32\ADVAPI32.dll       N/A     Disabled
908     svchost.exe     0x77e70000      0x92000 RPCRT4.dll      C:\WINDOWS\system32\RPCRT4.dll N/A     Disabled
908     svchost.exe     0x77fe0000      0x11000 Secur32.dll     C:\WINDOWS\system32\Secur32.dll        N/A     Disabled
908     svchost.exe     0x5cb70000      0x26000 ShimEng.dll     C:\WINDOWS\system32\ShimEng.dll        N/A     Disabled
908     svchost.exe     0x6f880000      0x1ca000        AcGenral.DLL    C:\WINDOWS\AppPatch\AcGenral.DLL       N/A     Disabled
908     svchost.exe     0x7e410000      0x91000 USER32.dll      C:\WINDOWS\system32\USER32.dll N/A     Disabled
908     svchost.exe     0x77f10000      0x49000 GDI32.dll       C:\WINDOWS\system32\GDI32.dll  N/A     Disabled
908     svchost.exe     0x76b40000      0x2d000 WINMM.dll       C:\WINDOWS\system32\WINMM.dll  N/A     Disabled
908     svchost.exe     0x774e0000      0x13d000        ole32.dll       C:\WINDOWS\system32\ole32.dll  N/A     Disabled
908     svchost.exe     0x77c10000      0x58000 msvcrt.dll      C:\WINDOWS\system32\msvcrt.dll N/A     Disabled
908     svchost.exe     0x77120000      0x8b000 OLEAUT32.dll    C:\WINDOWS\system32\OLEAUT32.dll       N/A     Disabled
908     svchost.exe     0x77be0000      0x15000 MSACM32.dll     C:\WINDOWS\system32\MSACM32.dll        N/A     Disabled
908     svchost.exe     0x77c00000      0x8000  VERSION.dll     C:\WINDOWS\system32\VERSION.dll        N/A     Disabled
908     svchost.exe     0x7c9c0000      0x817000        SHELL32.dll     C:\WINDOWS\system32\SHELL32.dll        N/A     Disabled
908     svchost.exe     0x77f60000      0x76000 SHLWAPI.dll     C:\WINDOWS\system32\SHLWAPI.dll        N/A     Disabled
908     svchost.exe     0x769c0000      0xb4000 USERENV.dll     C:\WINDOWS\system32\USERENV.dll        N/A     Disabled
908     svchost.exe     0x5ad70000      0x38000 UxTheme.dll     C:\WINDOWS\system32\UxTheme.dll        N/A     Disabled
908     svchost.exe     0x773d0000      0x103000        comctl32.dll    C:\WINDOWS\WinSxS\x86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.5512_x-ww_35d4ce83\comctl32.dll     N/A     Disabled
908     svchost.exe     0x5d090000      0x9a000 comctl32.dll    C:\WINDOWS\system32\comctl32.dll       N/A     Disabled
908     svchost.exe     0x76a80000      0x64000 rpcss.dll       c:\windows\system32\rpcss.dll  N/A     Disabled
908     svchost.exe     0x71ab0000      0x17000 WS2_32.dll      c:\windows\system32\WS2_32.dll N/A     Disabled
908     svchost.exe     0x71aa0000      0x8000  WS2HELP.dll     c:\windows\system32\WS2HELP.dll        N/A     Disabled
908     svchost.exe     0x670000        0x2c5000        xpsp2res.dll    C:\WINDOWS\system32\xpsp2res.dll       N/A     Disabled
908     svchost.exe     0x68000000      0x36000 rsaenh.dll      C:\WINDOWS\system32\rsaenh.dll N/A     Disabled
908     svchost.exe     0x71a50000      0x3f000 mswsock.dll     C:\WINDOWS\system32\mswsock.dll        N/A     Disabled
908     svchost.exe     0x662b0000      0x58000 hnetcfg.dll     C:\WINDOWS\system32\hnetcfg.dll        N/A     Disabled
908     svchost.exe     0x71a90000      0x8000  wshtcpip.dll    C:\WINDOWS\System32\wshtcpip.dll       N/A     Disabled
908     svchost.exe     0x76f20000      0x27000 DNSAPI.dll      C:\WINDOWS\system32\DNSAPI.dll N/A     Disabled
908     svchost.exe     0x76d60000      0x19000 iphlpapi.dll    C:\WINDOWS\system32\iphlpapi.dll       N/A     Disabled
908     svchost.exe     0x76fb0000      0x8000  winrnr.dll      C:\WINDOWS\System32\winrnr.dll N/A     Disabled
908     svchost.exe     0x76f60000      0x2c000 WLDAP32.dll     C:\WINDOWS\system32\WLDAP32.dll        N/A     Disabled
908     svchost.exe     0x76fc0000      0x6000  rasadhlp.dll    C:\WINDOWS\system32\rasadhlp.dll       N/A     Disabled
908     svchost.exe     0x76fd0000      0x7f000 CLBCATQ.DLL     C:\WINDOWS\system32\CLBCATQ.DLL        N/A     Disabled
908     svchost.exe     0x77050000      0xc5000 COMRes.dll      C:\WINDOWS\system32\COMRes.dll N/A     Disabled
1004    svchost.exe     0x1000000       0x6000  svchost.exe     C:\WINDOWS\System32\svchost.exe        N/A     Disabled
1004    svchost.exe     0x7c900000      0xaf000 ntdll.dll       C:\WINDOWS\system32\ntdll.dll  N/A     Disabled
1004    svchost.exe     0x7c800000      0xf6000 kernel32.dll    C:\WINDOWS\system32\kernel32.dll       N/A     Disabled
1004    svchost.exe     0x77dd0000      0x9b000 ADVAPI32.dll    C:\WINDOWS\system32\ADVAPI32.dll       N/A     Disabled
1004    svchost.exe     0x77e70000      0x92000 RPCRT4.dll      C:\WINDOWS\system32\RPCRT4.dll N/A     Disabled
1004    svchost.exe     0x77fe0000      0x11000 Secur32.dll     C:\WINDOWS\system32\Secur32.dll        N/A     Disabled
1004    svchost.exe     0x5cb70000      0x26000 ShimEng.dll     C:\WINDOWS\System32\ShimEng.dll        N/A     Disabled
1004    svchost.exe     0x6f880000      0x1ca000        AcGenral.DLL    C:\WINDOWS\AppPatch\AcGenral.DLL       N/A     Disabled
1004    svchost.exe     0x7e410000      0x91000 USER32.dll      C:\WINDOWS\system32\USER32.dll N/A     Disabled
1004    svchost.exe     0x77f10000      0x49000 GDI32.dll       C:\WINDOWS\system32\GDI32.dll  N/A     Disabled
1004    svchost.exe     0x76b40000      0x2d000 WINMM.dll       C:\WINDOWS\System32\WINMM.dll  N/A     Disabled
1004    svchost.exe     0x774e0000      0x13d000        ole32.dll       C:\WINDOWS\system32\ole32.dll  N/A     Disabled
1004    svchost.exe     0x77c10000      0x58000 msvcrt.dll      C:\WINDOWS\system32\msvcrt.dll N/A     Disabled
1004    svchost.exe     0x77120000      0x8b000 OLEAUT32.dll    C:\WINDOWS\system32\OLEAUT32.dll       N/A     Disabled
1004    svchost.exe     0x77be0000      0x15000 MSACM32.dll     C:\WINDOWS\System32\MSACM32.dll        N/A     Disabled
1004    svchost.exe     0x77c00000      0x8000  VERSION.dll     C:\WINDOWS\system32\VERSION.dll        N/A     Disabled
1004    svchost.exe     0x7c9c0000      0x817000        SHELL32.dll     C:\WINDOWS\system32\SHELL32.dll        N/A     Disabled
1004    svchost.exe     0x77f60000      0x76000 SHLWAPI.dll     C:\WINDOWS\system32\SHLWAPI.dll        N/A     Disabled
1004    svchost.exe     0x769c0000      0xb4000 USERENV.dll     C:\WINDOWS\system32\USERENV.dll        N/A     Disabled
1004    svchost.exe     0x5ad70000      0x38000 UxTheme.dll     C:\WINDOWS\System32\UxTheme.dll        N/A     Disabled
1004    svchost.exe     0x773d0000      0x103000        comctl32.dll    C:\WINDOWS\WinSxS\x86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.5512_x-ww_35d4ce83\comctl32.dll     N/A     Disabled
1004    svchost.exe     0x5d090000      0x9a000 comctl32.dll    C:\WINDOWS\system32\comctl32.dll       N/A     Disabled
1004    svchost.exe     0x77690000      0x21000 NTMARTA.DLL     C:\WINDOWS\System32\NTMARTA.DLL        N/A     Disabled
1004    svchost.exe     0x71bf0000      0x13000 SAMLIB.dll      C:\WINDOWS\System32\SAMLIB.dll N/A     Disabled
1004    svchost.exe     0x76f60000      0x2c000 WLDAP32.dll     C:\WINDOWS\system32\WLDAP32.dll        N/A     Disabled
1004    svchost.exe     0x630000        0x2c5000        xpsp2res.dll    C:\WINDOWS\System32\xpsp2res.dll       N/A     Disabled
1004    svchost.exe     0x776e0000      0x23000 shsvcs.dll      c:\windows\system32\shsvcs.dll N/A     Disabled
1004    svchost.exe     0x76360000      0x10000 WINSTA.dll      C:\WINDOWS\System32\WINSTA.dll N/A     Disabled
1004    svchost.exe     0x5b860000      0x55000 NETAPI32.dll    C:\WINDOWS\system32\NETAPI32.dll       N/A     Disabled
1004    svchost.exe     0x7d4b0000      0x22000 dhcpcsvc.dll    c:\windows\system32\dhcpcsvc.dll       N/A     Disabled
1004    svchost.exe     0x76f20000      0x27000 DNSAPI.dll      c:\windows\system32\DNSAPI.dll N/A     Disabled
1004    svchost.exe     0x71ab0000      0x17000 WS2_32.dll      c:\windows\system32\WS2_32.dll N/A     Disabled
1004    svchost.exe     0x71aa0000      0x8000  WS2HELP.dll     c:\windows\system32\WS2HELP.dll        N/A     Disabled
1004    svchost.exe     0x76d60000      0x19000 iphlpapi.dll    c:\windows\system32\iphlpapi.dll       N/A     Disabled
1004    svchost.exe     0x68000000      0x36000 rsaenh.dll      C:\WINDOWS\System32\rsaenh.dll N/A     Disabled
1004    svchost.exe     0x71a50000      0x3f000 mswsock.dll     C:\WINDOWS\system32\mswsock.dll        N/A     Disabled
1004    svchost.exe     0x662b0000      0x58000 hnetcfg.dll     C:\WINDOWS\System32\hnetcfg.dll        N/A     Disabled
1004    svchost.exe     0x71a90000      0x8000  wshtcpip.dll    C:\WINDOWS\System32\wshtcpip.dll       N/A     Disabled
1004    svchost.exe     0x7db10000      0x8c000 wzcsvc.dll      c:\windows\system32\wzcsvc.dll N/A     Disabled
1004    svchost.exe     0x76e80000      0xe000  rtutils.dll     c:\windows\system32\rtutils.dll        N/A     Disabled
1004    svchost.exe     0x76d30000      0x4000  WMI.dll c:\windows\system32\WMI.dll   N/A      Disabled
1004    svchost.exe     0x77a80000      0x95000 CRYPT32.dll     C:\WINDOWS\system32\CRYPT32.dll        N/A     Disabled
1004    svchost.exe     0x77b20000      0x12000 MSASN1.dll      C:\WINDOWS\system32\MSASN1.dll N/A     Disabled
1004    svchost.exe     0x72810000      0xb000  EapolQec.dll    c:\windows\system32\EapolQec.dll       N/A     Disabled
1004    svchost.exe     0x76b20000      0x11000 ATL.DLL c:\windows\system32\ATL.DLL   N/A      Disabled
1004    svchost.exe     0x726c0000      0x16000 QUtil.dll       c:\windows\system32\QUtil.dll  N/A     Disabled
1004    svchost.exe     0x76080000      0x65000 MSVCP60.dll     c:\windows\system32\MSVCP60.dll        N/A     Disabled
1004    svchost.exe     0x478c0000      0xa000  dot3api.dll     c:\windows\system32\dot3api.dll        N/A     Disabled
1004    svchost.exe     0x76f50000      0x8000  WTSAPI32.dll    c:\windows\system32\WTSAPI32.dll       N/A     Disabled
1004    svchost.exe     0x606b0000      0x10d000        ESENT.dll       c:\windows\system32\ESENT.dll  N/A     Disabled
1004    svchost.exe     0x76fd0000      0x7f000 CLBCATQ.DLL     C:\WINDOWS\System32\CLBCATQ.DLL        N/A     Disabled
1004    svchost.exe     0x77050000      0xc5000 COMRes.dll      C:\WINDOWS\System32\COMRes.dll N/A     Disabled
1004    svchost.exe     0x76b70000      0x27000 rastls.dll      C:\WINDOWS\System32\rastls.dll N/A     Disabled
1004    svchost.exe     0x754d0000      0x80000 CRYPTUI.dll     C:\WINDOWS\system32\CRYPTUI.dll        N/A     Disabled
1004    svchost.exe     0x771b0000      0xaa000 WININET.dll     C:\WINDOWS\system32\WININET.dll        N/A     Disabled
1004    svchost.exe     0x76c30000      0x2e000 WINTRUST.dll    C:\WINDOWS\system32\WINTRUST.dll       N/A     Disabled
1004    svchost.exe     0x76c90000      0x28000 IMAGEHLP.dll    C:\WINDOWS\system32\IMAGEHLP.dll       N/A     Disabled
1004    svchost.exe     0x76d40000      0x18000 MPRAPI.dll      C:\WINDOWS\System32\MPRAPI.dll N/A     Disabled
1004    svchost.exe     0x77cc0000      0x32000 ACTIVEDS.dll    C:\WINDOWS\System32\ACTIVEDS.dll       N/A     Disabled
1004    svchost.exe     0x76e10000      0x25000 adsldpc.dll     C:\WINDOWS\System32\adsldpc.dll        N/A     Disabled
1004    svchost.exe     0x77920000      0xf3000 SETUPAPI.dll    C:\WINDOWS\System32\SETUPAPI.dll       N/A     Disabled
1004    svchost.exe     0x76ee0000      0x3c000 RASAPI32.dll    C:\WINDOWS\System32\RASAPI32.dll       N/A     Disabled
1004    svchost.exe     0x76e90000      0x12000 rasman.dll      C:\WINDOWS\System32\rasman.dll N/A     Disabled
1004    svchost.exe     0x76eb0000      0x2f000 TAPI32.dll      C:\WINDOWS\System32\TAPI32.dll N/A     Disabled
1004    svchost.exe     0x767f0000      0x27000 SCHANNEL.dll    C:\WINDOWS\System32\SCHANNEL.dll       N/A     Disabled
1004    svchost.exe     0x723d0000      0x1c000 WinSCard.dll    C:\WINDOWS\System32\WinSCard.dll       N/A     Disabled
1004    svchost.exe     0x76bf0000      0xb000  PSAPI.DLL       C:\WINDOWS\System32\PSAPI.DLL  N/A     Disabled
1004    svchost.exe     0x76bd0000      0x16000 raschap.dll     C:\WINDOWS\System32\raschap.dll        N/A     Disabled
1004    svchost.exe     0x77c70000      0x24000 msv1_0.dll      C:\WINDOWS\system32\msv1_0.dll N/A     Disabled
1004    svchost.exe     0x77300000      0x33000 schedsvc.dll    c:\windows\system32\schedsvc.dll       N/A     Disabled
1004    svchost.exe     0x767a0000      0x13000 NTDSAPI.dll     c:\windows\system32\NTDSAPI.dll        N/A     Disabled
1004    svchost.exe     0x74f50000      0x5000  MSIDLE.DLL      C:\WINDOWS\System32\MSIDLE.DLL N/A     Disabled
1004    svchost.exe     0x708b0000      0xd000  audiosrv.dll    c:\windows\system32\audiosrv.dll       N/A     Disabled
1004    svchost.exe     0x76e40000      0x23000 wkssvc.dll      c:\windows\system32\wkssvc.dll N/A     Disabled
1004    svchost.exe     0x76ce0000      0x12000 cryptsvc.dll    c:\windows\system32\cryptsvc.dll       N/A     Disabled
1004    svchost.exe     0x77b90000      0x32000 certcli.dll     c:\windows\system32\certcli.dll        N/A     Disabled
1004    svchost.exe     0x74f90000      0x9000  dmserver.dll    c:\windows\system32\dmserver.dll       N/A     Disabled
1004    svchost.exe     0x74f80000      0x9000  ersvc.dll       c:\windows\system32\ersvc.dll  N/A     Disabled
1004    svchost.exe     0x77710000      0x42000 es.dll  c:\windows\system32\es.dll    N/A      Disabled
1004    svchost.exe     0x74f40000      0xc000  pchsvc.dll      c:\windows\pchealth\helpctr\binaries\pchsvc.dll        N/A     Disabled
1004    svchost.exe     0x75090000      0x1a000 srvsvc.dll      c:\windows\system32\srvsvc.dll N/A     Disabled
1004    svchost.exe     0x77d00000      0x33000 netman.dll      c:\windows\system32\netman.dll N/A     Disabled
1004    svchost.exe     0x76400000      0x1a5000        netshell.dll    c:\windows\system32\netshell.dll       N/A     Disabled
1004    svchost.exe     0x76c00000      0x2e000 credui.dll      c:\windows\system32\credui.dll N/A     Disabled
1004    svchost.exe     0x736d0000      0x6000  dot3dlg.dll     c:\windows\system32\dot3dlg.dll        N/A     Disabled
1004    svchost.exe     0x5dca0000      0x28000 OneX.DLL        c:\windows\system32\OneX.DLL   N/A     Disabled
1004    svchost.exe     0x745b0000      0x22000 eappcfg.dll     c:\windows\system32\eappcfg.dll        N/A     Disabled
1004    svchost.exe     0x5dcd0000      0xe000  eappprxy.dll    c:\windows\system32\eappprxy.dll       N/A     Disabled
1004    svchost.exe     0x73030000      0x10000 WZCSAPI.DLL     c:\windows\system32\WZCSAPI.DLL        N/A     Disabled
1004    svchost.exe     0x73d20000      0x8000  seclogon.dll    c:\windows\system32\seclogon.dll       N/A     Disabled
1004    svchost.exe     0x722d0000      0xd000  sens.dll        c:\windows\system32\sens.dll   N/A     Disabled
1004    svchost.exe     0x751a0000      0x2e000 srsvc.dll       c:\windows\system32\srsvc.dll  N/A     Disabled
1004    svchost.exe     0x74ad0000      0x8000  POWRPROF.dll    c:\windows\system32\POWRPROF.dll       N/A     Disabled
1004    svchost.exe     0x75070000      0x19000 trkwks.dll      c:\windows\system32\trkwks.dll N/A     Disabled
1004    svchost.exe     0x767c0000      0x2c000 w32time.dll     c:\windows\system32\w32time.dll        N/A     Disabled
1004    svchost.exe     0x59490000      0x28000 wmisvc.dll      c:\windows\system32\wbem\wmisvc.dll    N/A     Disabled
1004    svchost.exe     0x753e0000      0x6d000 VSSAPI.DLL      C:\WINDOWS\system32\VSSAPI.DLL N/A     Disabled
1004    svchost.exe     0x50000000      0x5000  wuauserv.dll    c:\windows\system32\wuauserv.dll       N/A     Disabled
1004    svchost.exe     0x50040000      0x119000        wuaueng.dll     C:\WINDOWS\system32\wuaueng.dll        N/A     Disabled
1004    svchost.exe     0x75260000      0x29000 ADVPACK.dll     C:\WINDOWS\System32\ADVPACK.dll        N/A     Disabled
1004    svchost.exe     0x75150000      0x13000 Cabinet.dll     C:\WINDOWS\System32\Cabinet.dll        N/A     Disabled
1004    svchost.exe     0x600a0000      0xb000  mspatcha.dll    C:\WINDOWS\System32\mspatcha.dll       N/A     Disabled
1004    svchost.exe     0x76bb0000      0x5000  sfc.dll C:\WINDOWS\System32\sfc.dll   N/A      Disabled
1004    svchost.exe     0x76c60000      0x2a000 sfc_os.dll      C:\WINDOWS\System32\sfc_os.dll N/A     Disabled
1004    svchost.exe     0x76780000      0x9000  SHFOLDER.dll    C:\WINDOWS\System32\SHFOLDER.dll       N/A     Disabled
1004    svchost.exe     0x4d4f0000      0x59000 WINHTTP.dll     C:\WINDOWS\System32\WINHTTP.dll        N/A     Disabled
1004    svchost.exe     0x73000000      0x26000 WINSPOOL.DRV    C:\WINDOWS\System32\WINSPOOL.DRV       N/A     Disabled
1004    svchost.exe     0x4c0a0000      0x17000 wscsvc.dll      c:\windows\system32\wscsvc.dll N/A     Disabled
1004    svchost.exe     0x7d1e0000      0x2bc000        msi.dll c:\windows\system32\msi.dll    N/A     Disabled
1004    svchost.exe     0x7e720000      0xb0000 SXS.DLL C:\WINDOWS\System32\SXS.DLL   N/A      Disabled
1004    svchost.exe     0x76da0000      0x16000 browser.dll     c:\windows\system32\browser.dll        N/A     Disabled
1004    svchost.exe     0x75290000      0x37000 wbemcomn.dll    C:\WINDOWS\system32\wbem\wbemcomn.dll  N/A     Disabled
1004    svchost.exe     0x762c0000      0x85000 wbemcore.dll    C:\WINDOWS\System32\Wbem\wbemcore.dll  N/A     Disabled
1004    svchost.exe     0x75310000      0x3f000 esscli.dll      C:\WINDOWS\System32\Wbem\esscli.dll    N/A     Disabled
1004    svchost.exe     0x75690000      0x76000 FastProx.dll    C:\WINDOWS\System32\Wbem\FastProx.dll  N/A     Disabled
1004    svchost.exe     0x75020000      0x1b000 wmiutils.dll    C:\WINDOWS\system32\wbem\wmiutils.dll  N/A     Disabled
1004    svchost.exe     0x75200000      0x2f000 repdrvfs.dll    C:\WINDOWS\system32\wbem\repdrvfs.dll  N/A     Disabled
1004    svchost.exe     0x76620000      0x13c000        comsvcs.dll     C:\WINDOWS\system32\comsvcs.dll        N/A     Disabled
1004    svchost.exe     0x75130000      0x14000 colbact.DLL     C:\WINDOWS\system32\colbact.DLL        N/A     Disabled
1004    svchost.exe     0x750f0000      0x13000 MTXCLU.DLL      C:\WINDOWS\system32\MTXCLU.DLL N/A     Disabled
1004    svchost.exe     0x71ad0000      0x9000  WSOCK32.dll     C:\WINDOWS\system32\WSOCK32.dll        N/A     Disabled
1004    svchost.exe     0x76d10000      0x12000 CLUSAPI.DLL     C:\WINDOWS\System32\CLUSAPI.DLL        N/A     Disabled
1004    svchost.exe     0x750b0000      0x12000 RESUTILS.DLL    C:\WINDOWS\System32\RESUTILS.DLL       N/A     Disabled
1004    svchost.exe     0x597f0000      0x6d000 wmiprvsd.dll    C:\WINDOWS\system32\wbem\wmiprvsd.dll  N/A     Disabled
1004    svchost.exe     0x5f770000      0xc000  NCObjAPI.DLL    C:\WINDOWS\system32\NCObjAPI.DLL       N/A     Disabled
1004    svchost.exe     0x75390000      0x46000 wbemess.dll     C:\WINDOWS\system32\wbem\wbemess.dll   N/A     Disabled
1004    svchost.exe     0x5f740000      0xe000  ncprov.dll      C:\WINDOWS\system32\wbem\ncprov.dll    N/A     Disabled
1004    svchost.exe     0x66460000      0x55000 ipnathlp.dll    c:\windows\system32\ipnathlp.dll       N/A     Disabled
1004    svchost.exe     0x776c0000      0x12000 AUTHZ.dll       c:\windows\system32\AUTHZ.dll  N/A     Disabled
1004    svchost.exe     0x76de0000      0x24000 upnp.dll        C:\WINDOWS\system32\upnp.dll   N/A     Disabled
1004    svchost.exe     0x74f00000      0xc000  SSDPAPI.dll     C:\WINDOWS\system32\SSDPAPI.dll        N/A     Disabled
1004    svchost.exe     0x76fc0000      0x6000  rasadhlp.dll    C:\WINDOWS\System32\rasadhlp.dll       N/A     Disabled
1004    svchost.exe     0x768d0000      0xa4000 RASDLG.dll      C:\WINDOWS\System32\RASDLG.dll N/A     Disabled
1004    svchost.exe     0x77b40000      0x22000 Apphelp.dll     C:\WINDOWS\system32\Apphelp.dll        N/A     Disabled
1004    svchost.exe     0x50640000      0xc000  wups.dll        C:\WINDOWS\system32\wups.dll   N/A     Disabled
1056    svchost.exe     0x1000000       0x6000  svchost.exe     C:\WINDOWS\system32\svchost.exe        N/A     Disabled
1056    svchost.exe     0x7c900000      0xaf000 ntdll.dll       C:\WINDOWS\system32\ntdll.dll  N/A     Disabled
1056    svchost.exe     0x7c800000      0xf6000 kernel32.dll    C:\WINDOWS\system32\kernel32.dll       N/A     Disabled
1056    svchost.exe     0x77dd0000      0x9b000 ADVAPI32.dll    C:\WINDOWS\system32\ADVAPI32.dll       N/A     Disabled
1056    svchost.exe     0x77e70000      0x92000 RPCRT4.dll      C:\WINDOWS\system32\RPCRT4.dll N/A     Disabled
1056    svchost.exe     0x77fe0000      0x11000 Secur32.dll     C:\WINDOWS\system32\Secur32.dll        N/A     Disabled
1056    svchost.exe     0x5cb70000      0x26000 ShimEng.dll     C:\WINDOWS\system32\ShimEng.dll        N/A     Disabled
1056    svchost.exe     0x6f880000      0x1ca000        AcGenral.DLL    C:\WINDOWS\AppPatch\AcGenral.DLL       N/A     Disabled
1056    svchost.exe     0x7e410000      0x91000 USER32.dll      C:\WINDOWS\system32\USER32.dll N/A     Disabled
1056    svchost.exe     0x77f10000      0x49000 GDI32.dll       C:\WINDOWS\system32\GDI32.dll  N/A     Disabled
1056    svchost.exe     0x76b40000      0x2d000 WINMM.dll       C:\WINDOWS\system32\WINMM.dll  N/A     Disabled
1056    svchost.exe     0x774e0000      0x13d000        ole32.dll       C:\WINDOWS\system32\ole32.dll  N/A     Disabled
1056    svchost.exe     0x77c10000      0x58000 msvcrt.dll      C:\WINDOWS\system32\msvcrt.dll N/A     Disabled
1056    svchost.exe     0x77120000      0x8b000 OLEAUT32.dll    C:\WINDOWS\system32\OLEAUT32.dll       N/A     Disabled
1056    svchost.exe     0x77be0000      0x15000 MSACM32.dll     C:\WINDOWS\system32\MSACM32.dll        N/A     Disabled
1056    svchost.exe     0x77c00000      0x8000  VERSION.dll     C:\WINDOWS\system32\VERSION.dll        N/A     Disabled
1056    svchost.exe     0x7c9c0000      0x817000        SHELL32.dll     C:\WINDOWS\system32\SHELL32.dll        N/A     Disabled
1056    svchost.exe     0x77f60000      0x76000 SHLWAPI.dll     C:\WINDOWS\system32\SHLWAPI.dll        N/A     Disabled
1056    svchost.exe     0x769c0000      0xb4000 USERENV.dll     C:\WINDOWS\system32\USERENV.dll        N/A     Disabled
1056    svchost.exe     0x5ad70000      0x38000 UxTheme.dll     C:\WINDOWS\system32\UxTheme.dll        N/A     Disabled
1056    svchost.exe     0x773d0000      0x103000        comctl32.dll    C:\WINDOWS\WinSxS\x86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.5512_x-ww_35d4ce83\comctl32.dll     N/A     Disabled
1056    svchost.exe     0x5d090000      0x9a000 comctl32.dll    C:\WINDOWS\system32\comctl32.dll       N/A     Disabled
1056    svchost.exe     0x76770000      0xd000  dnsrslvr.dll    c:\windows\system32\dnsrslvr.dll       N/A     Disabled
1056    svchost.exe     0x76f20000      0x27000 DNSAPI.dll      c:\windows\system32\DNSAPI.dll N/A     Disabled
1056    svchost.exe     0x71ab0000      0x17000 WS2_32.dll      c:\windows\system32\WS2_32.dll N/A     Disabled
1056    svchost.exe     0x71aa0000      0x8000  WS2HELP.dll     c:\windows\system32\WS2HELP.dll        N/A     Disabled
1056    svchost.exe     0x76d60000      0x19000 iphlpapi.dll    c:\windows\system32\iphlpapi.dll       N/A     Disabled
1220    svchost.exe     0x1000000       0x6000  svchost.exe     C:\WINDOWS\system32\svchost.exe        N/A     Disabled
1220    svchost.exe     0x7c900000      0xaf000 ntdll.dll       C:\WINDOWS\system32\ntdll.dll  N/A     Disabled
1220    svchost.exe     0x7c800000      0xf6000 kernel32.dll    C:\WINDOWS\system32\kernel32.dll       N/A     Disabled
1220    svchost.exe     0x77dd0000      0x9b000 ADVAPI32.dll    C:\WINDOWS\system32\ADVAPI32.dll       N/A     Disabled
1220    svchost.exe     0x77e70000      0x92000 RPCRT4.dll      C:\WINDOWS\system32\RPCRT4.dll N/A     Disabled
1220    svchost.exe     0x77fe0000      0x11000 Secur32.dll     C:\WINDOWS\system32\Secur32.dll        N/A     Disabled
1220    svchost.exe     0x5cb70000      0x26000 ShimEng.dll     C:\WINDOWS\system32\ShimEng.dll        N/A     Disabled
1220    svchost.exe     0x6f880000      0x1ca000        AcGenral.DLL    C:\WINDOWS\AppPatch\AcGenral.DLL       N/A     Disabled
1220    svchost.exe     0x7e410000      0x91000 USER32.dll      C:\WINDOWS\system32\USER32.dll N/A     Disabled
1220    svchost.exe     0x77f10000      0x49000 GDI32.dll       C:\WINDOWS\system32\GDI32.dll  N/A     Disabled
1220    svchost.exe     0x76b40000      0x2d000 WINMM.dll       C:\WINDOWS\system32\WINMM.dll  N/A     Disabled
1220    svchost.exe     0x774e0000      0x13d000        ole32.dll       C:\WINDOWS\system32\ole32.dll  N/A     Disabled
1220    svchost.exe     0x77c10000      0x58000 msvcrt.dll      C:\WINDOWS\system32\msvcrt.dll N/A     Disabled
1220    svchost.exe     0x77120000      0x8b000 OLEAUT32.dll    C:\WINDOWS\system32\OLEAUT32.dll       N/A     Disabled
1220    svchost.exe     0x77be0000      0x15000 MSACM32.dll     C:\WINDOWS\system32\MSACM32.dll        N/A     Disabled
1220    svchost.exe     0x77c00000      0x8000  VERSION.dll     C:\WINDOWS\system32\VERSION.dll        N/A     Disabled
1220    svchost.exe     0x7c9c0000      0x817000        SHELL32.dll     C:\WINDOWS\system32\SHELL32.dll        N/A     Disabled
1220    svchost.exe     0x77f60000      0x76000 SHLWAPI.dll     C:\WINDOWS\system32\SHLWAPI.dll        N/A     Disabled
1220    svchost.exe     0x769c0000      0xb4000 USERENV.dll     C:\WINDOWS\system32\USERENV.dll        N/A     Disabled
1220    svchost.exe     0x5ad70000      0x38000 UxTheme.dll     C:\WINDOWS\system32\UxTheme.dll        N/A     Disabled
1220    svchost.exe     0x773d0000      0x103000        comctl32.dll    C:\WINDOWS\WinSxS\x86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.5512_x-ww_35d4ce83\comctl32.dll     N/A     Disabled
1220    svchost.exe     0x5d090000      0x9a000 comctl32.dll    C:\WINDOWS\system32\comctl32.dll       N/A     Disabled
1220    svchost.exe     0x77690000      0x21000 NTMARTA.DLL     C:\WINDOWS\system32\NTMARTA.DLL        N/A     Disabled
1220    svchost.exe     0x71bf0000      0x13000 SAMLIB.dll      C:\WINDOWS\system32\SAMLIB.dll N/A     Disabled
1220    svchost.exe     0x76f60000      0x2c000 WLDAP32.dll     C:\WINDOWS\system32\WLDAP32.dll        N/A     Disabled
1220    svchost.exe     0x630000        0x2c5000        xpsp2res.dll    C:\WINDOWS\system32\xpsp2res.dll       N/A     Disabled
1220    svchost.exe     0x74c40000      0x6000  lmhsvc.dll      c:\windows\system32\lmhsvc.dll N/A     Disabled
1220    svchost.exe     0x76d60000      0x19000 iphlpapi.dll    c:\windows\system32\iphlpapi.dll       N/A     Disabled
1220    svchost.exe     0x71ab0000      0x17000 WS2_32.dll      c:\windows\system32\WS2_32.dll N/A     Disabled
1220    svchost.exe     0x71aa0000      0x8000  WS2HELP.dll     c:\windows\system32\WS2HELP.dll        N/A     Disabled
1220    svchost.exe     0x5a6e0000      0x15000 webclnt.dll     c:\windows\system32\webclnt.dll        N/A     Disabled
1220    svchost.exe     0x771b0000      0xaa000 WININET.dll     C:\WINDOWS\system32\WININET.dll        N/A     Disabled
1220    svchost.exe     0x77a80000      0x95000 CRYPT32.dll     C:\WINDOWS\system32\CRYPT32.dll        N/A     Disabled
1220    svchost.exe     0x77b20000      0x12000 MSASN1.dll      C:\WINDOWS\system32\MSASN1.dll N/A     Disabled
1220    svchost.exe     0x71ad0000      0x9000  wsock32.dll     C:\WINDOWS\system32\wsock32.dll        N/A     Disabled
1220    svchost.exe     0x76af0000      0x12000 regsvc.dll      c:\windows\system32\regsvc.dll N/A     Disabled
1220    svchost.exe     0x765e0000      0x14000 ssdpsrv.dll     c:\windows\system32\ssdpsrv.dll        N/A     Disabled
1220    svchost.exe     0x662b0000      0x58000 hnetcfg.dll     C:\WINDOWS\system32\hnetcfg.dll        N/A     Disabled
1220    svchost.exe     0x76fd0000      0x7f000 CLBCATQ.DLL     C:\WINDOWS\system32\CLBCATQ.DLL        N/A     Disabled
1220    svchost.exe     0x77050000      0xc5000 COMRes.dll      C:\WINDOWS\system32\COMRes.dll N/A     Disabled
1220    svchost.exe     0x71a50000      0x3f000 mswsock.dll     C:\WINDOWS\system32\mswsock.dll        N/A     Disabled
1220    svchost.exe     0x71a90000      0x8000  wshtcpip.dll    C:\WINDOWS\System32\wshtcpip.dll       N/A     Disabled
1484    explorer.exe    0x1000000       0xff000 Explorer.EXE    C:\WINDOWS\Explorer.EXEN/A     Disabled
1484    explorer.exe    0x7c900000      0xaf000 ntdll.dll       C:\WINDOWS\system32\ntdll.dll  N/A     Disabled
1484    explorer.exe    0x7c800000      0xf6000 kernel32.dll    C:\WINDOWS\system32\kernel32.dll       N/A     Disabled
1484    explorer.exe    0x77dd0000      0x9b000 ADVAPI32.dll    C:\WINDOWS\system32\ADVAPI32.dll       N/A     Disabled
1484    explorer.exe    0x77e70000      0x92000 RPCRT4.dll      C:\WINDOWS\system32\RPCRT4.dll N/A     Disabled
1484    explorer.exe    0x77fe0000      0x11000 Secur32.dll     C:\WINDOWS\system32\Secur32.dll        N/A     Disabled
1484    explorer.exe    0x75f80000      0xfd000 BROWSEUI.dll    C:\WINDOWS\system32\BROWSEUI.dll       N/A     Disabled
1484    explorer.exe    0x77f10000      0x49000 GDI32.dll       C:\WINDOWS\system32\GDI32.dll  N/A     Disabled
1484    explorer.exe    0x7e410000      0x91000 USER32.dll      C:\WINDOWS\system32\USER32.dll N/A     Disabled
1484    explorer.exe    0x77c10000      0x58000 msvcrt.dll      C:\WINDOWS\system32\msvcrt.dll N/A     Disabled
1484    explorer.exe    0x774e0000      0x13d000        ole32.dll       C:\WINDOWS\system32\ole32.dll  N/A     Disabled
1484    explorer.exe    0x77f60000      0x76000 SHLWAPI.dll     C:\WINDOWS\system32\SHLWAPI.dll        N/A     Disabled
1484    explorer.exe    0x77120000      0x8b000 OLEAUT32.dll    C:\WINDOWS\system32\OLEAUT32.dll       N/A     Disabled
1484    explorer.exe    0x7e290000      0x171000        SHDOCVW.dll     C:\WINDOWS\system32\SHDOCVW.dll        N/A     Disabled
1484    explorer.exe    0x77a80000      0x95000 CRYPT32.dll     C:\WINDOWS\system32\CRYPT32.dll        N/A     Disabled
1484    explorer.exe    0x77b20000      0x12000 MSASN1.dll      C:\WINDOWS\system32\MSASN1.dll N/A     Disabled
1484    explorer.exe    0x754d0000      0x80000 CRYPTUI.dll     C:\WINDOWS\system32\CRYPTUI.dll        N/A     Disabled
1484    explorer.exe    0x5b860000      0x55000 NETAPI32.dll    C:\WINDOWS\system32\NETAPI32.dll       N/A     Disabled
1484    explorer.exe    0x77c00000      0x8000  VERSION.dll     C:\WINDOWS\system32\VERSION.dll        N/A     Disabled
1484    explorer.exe    0x771b0000      0xaa000 WININET.dll     C:\WINDOWS\system32\WININET.dll        N/A     Disabled
1484    explorer.exe    0x76c30000      0x2e000 WINTRUST.dll    C:\WINDOWS\system32\WINTRUST.dll       N/A     Disabled
1484    explorer.exe    0x76c90000      0x28000 IMAGEHLP.dll    C:\WINDOWS\system32\IMAGEHLP.dll       N/A     Disabled
1484    explorer.exe    0x76f60000      0x2c000 WLDAP32.dll     C:\WINDOWS\system32\WLDAP32.dll        N/A     Disabled
1484    explorer.exe    0x7c9c0000      0x817000        SHELL32.dll     C:\WINDOWS\system32\SHELL32.dll        N/A     Disabled
1484    explorer.exe    0x5ad70000      0x38000 UxTheme.dll     C:\WINDOWS\system32\UxTheme.dll        N/A     Disabled
1484    explorer.exe    0x5cb70000      0x26000 ShimEng.dll     C:\WINDOWS\system32\ShimEng.dll        N/A     Disabled
1484    explorer.exe    0x6f880000      0x1ca000        AcGenral.DLL    C:\WINDOWS\AppPatch\AcGenral.DLL       N/A     Disabled
1484    explorer.exe    0x76b40000      0x2d000 WINMM.dll       C:\WINDOWS\system32\WINMM.dll  N/A     Disabled
1484    explorer.exe    0x77be0000      0x15000 MSACM32.dll     C:\WINDOWS\system32\MSACM32.dll        N/A     Disabled
1484    explorer.exe    0x769c0000      0xb4000 USERENV.dll     C:\WINDOWS\system32\USERENV.dll        N/A     Disabled
1484    explorer.exe    0x773d0000      0x103000        comctl32.dll    C:\WINDOWS\WinSxS\x86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.5512_x-ww_35d4ce83\comctl32.dll     N/A     Disabled
1484    explorer.exe    0x5d090000      0x9a000 comctl32.dll    C:\WINDOWS\system32\comctl32.dll       N/A     Disabled
1484    explorer.exe    0x77b40000      0x22000 appHelp.dll     C:\WINDOWS\system32\appHelp.dll        N/A     Disabled
1484    explorer.exe    0x76fd0000      0x7f000 CLBCATQ.DLL     C:\WINDOWS\system32\CLBCATQ.DLL        N/A     Disabled
1484    explorer.exe    0x77050000      0xc5000 COMRes.dll      C:\WINDOWS\system32\COMRes.dll N/A     Disabled
1484    explorer.exe    0x77a20000      0x54000 cscui.dll       C:\WINDOWS\System32\cscui.dll  N/A     Disabled
1484    explorer.exe    0x76600000      0x1d000 CSCDLL.dll      C:\WINDOWS\System32\CSCDLL.dll N/A     Disabled
1484    explorer.exe    0x5ba60000      0x71000 themeui.dll     C:\WINDOWS\system32\themeui.dll        N/A     Disabled
1484    explorer.exe    0x76380000      0x5000  MSIMG32.dll     C:\WINDOWS\system32\MSIMG32.dll        N/A     Disabled
1484    explorer.exe    0x1100000       0x2c5000        xpsp2res.dll    C:\WINDOWS\system32\xpsp2res.dll       N/A     Disabled
1484    explorer.exe    0x71d40000      0x1b000 actxprxy.dll    C:\WINDOWS\system32\actxprxy.dll       N/A     Disabled
1484    explorer.exe    0x7d1e0000      0x2bc000        msi.dll C:\WINDOWS\system32\msi.dll    N/A     Disabled
1484    explorer.exe    0x77920000      0xf3000 SETUPAPI.dll    C:\WINDOWS\system32\SETUPAPI.dll       N/A     Disabled
1484    explorer.exe    0x76980000      0x8000  LINKINFO.dll    C:\WINDOWS\system32\LINKINFO.dll       N/A     Disabled
1484    explorer.exe    0x76990000      0x25000 ntshrui.dll     C:\WINDOWS\system32\ntshrui.dll        N/A     Disabled
1484    explorer.exe    0x76b20000      0x11000 ATL.DLL C:\WINDOWS\system32\ATL.DLL   N/A      Disabled
1484    explorer.exe    0x7e1e0000      0xa2000 urlmon.dll      C:\WINDOWS\system32\urlmon.dll N/A     Disabled
1484    explorer.exe    0x68000000      0x36000 rsaenh.dll      C:\WINDOWS\system32\rsaenh.dll N/A     Disabled
1484    explorer.exe    0x76400000      0x1a5000        NETSHELL.dll    C:\WINDOWS\system32\NETSHELL.dll       N/A     Disabled
1484    explorer.exe    0x76c00000      0x2e000 credui.dll      C:\WINDOWS\system32\credui.dll N/A     Disabled
1484    explorer.exe    0x478c0000      0xa000  dot3api.dll     C:\WINDOWS\system32\dot3api.dll        N/A     Disabled
1484    explorer.exe    0x76e80000      0xe000  rtutils.dll     C:\WINDOWS\system32\rtutils.dll        N/A     Disabled
1484    explorer.exe    0x736d0000      0x6000  dot3dlg.dll     C:\WINDOWS\system32\dot3dlg.dll        N/A     Disabled
1484    explorer.exe    0x5dca0000      0x28000 OneX.DLL        C:\WINDOWS\system32\OneX.DLL   N/A     Disabled
1484    explorer.exe    0x76f50000      0x8000  WTSAPI32.dll    C:\WINDOWS\system32\WTSAPI32.dll       N/A     Disabled
1484    explorer.exe    0x76360000      0x10000 WINSTA.dll      C:\WINDOWS\system32\WINSTA.dll N/A     Disabled
1484    explorer.exe    0x745b0000      0x22000 eappcfg.dll     C:\WINDOWS\system32\eappcfg.dll        N/A     Disabled
1484    explorer.exe    0x76080000      0x65000 MSVCP60.dll     C:\WINDOWS\system32\MSVCP60.dll        N/A     Disabled
1484    explorer.exe    0x5dcd0000      0xe000  eappprxy.dll    C:\WINDOWS\system32\eappprxy.dll       N/A     Disabled
1484    explorer.exe    0x76d60000      0x19000 iphlpapi.dll    C:\WINDOWS\system32\iphlpapi.dll       N/A     Disabled
1484    explorer.exe    0x71ab0000      0x17000 WS2_32.dll      C:\WINDOWS\system32\WS2_32.dll N/A     Disabled
1484    explorer.exe    0x71aa0000      0x8000  WS2HELP.dll     C:\WINDOWS\system32\WS2HELP.dll        N/A     Disabled
1484    explorer.exe    0x75e60000      0x13000 cryptnet.dll    C:\WINDOWS\system32\cryptnet.dll       N/A     Disabled
1484    explorer.exe    0x76bf0000      0xb000  PSAPI.DLL       C:\WINDOWS\system32\PSAPI.DLL  N/A     Disabled
1484    explorer.exe    0x722b0000      0x5000  SensApi.dll     C:\WINDOWS\system32\SensApi.dll        N/A     Disabled
1484    explorer.exe    0x4d4f0000      0x59000 WINHTTP.dll     C:\WINDOWS\system32\WINHTTP.dll        N/A     Disabled
1484    explorer.exe    0x75150000      0x13000 Cabinet.dll     C:\WINDOWS\system32\Cabinet.dll        N/A     Disabled
1484    explorer.exe    0x74b30000      0x46000 webcheck.dll    C:\WINDOWS\system32\webcheck.dll       N/A     Disabled
1484    explorer.exe    0x71ad0000      0x9000  WSOCK32.dll     C:\WINDOWS\system32\WSOCK32.dll        N/A     Disabled
1484    explorer.exe    0x76280000      0x21000 stobject.dll    C:\WINDOWS\system32\stobject.dll       N/A     Disabled
1484    explorer.exe    0x74af0000      0xa000  BatMeter.dll    C:\WINDOWS\system32\BatMeter.dll       N/A     Disabled
1484    explorer.exe    0x74ad0000      0x8000  POWRPROF.dll    C:\WINDOWS\system32\POWRPROF.dll       N/A     Disabled
1484    explorer.exe    0x72d20000      0x9000  wdmaud.drv      C:\WINDOWS\system32\wdmaud.drv N/A     Disabled
1484    explorer.exe    0x72d10000      0x8000  msacm32.drv     C:\WINDOWS\system32\msacm32.drv        N/A     Disabled
1484    explorer.exe    0x77bd0000      0x7000  midimap.dll     C:\WINDOWS\system32\midimap.dll        N/A     Disabled
1484    explorer.exe    0x71b20000      0x12000 MPR.dll C:\WINDOWS\system32\MPR.dll   N/A      Disabled
1484    explorer.exe    0x75f60000      0x7000  drprov.dll      C:\WINDOWS\System32\drprov.dll N/A     Disabled
1484    explorer.exe    0x71c10000      0xe000  ntlanman.dll    C:\WINDOWS\System32\ntlanman.dll       N/A     Disabled
1484    explorer.exe    0x71cd0000      0x17000 NETUI0.dll      C:\WINDOWS\System32\NETUI0.dll N/A     Disabled
1484    explorer.exe    0x71c90000      0x40000 NETUI1.dll      C:\WINDOWS\System32\NETUI1.dll N/A     Disabled
1484    explorer.exe    0x71c80000      0x7000  NETRAP.dll      C:\WINDOWS\System32\NETRAP.dll N/A     Disabled
1484    explorer.exe    0x71bf0000      0x13000 SAMLIB.dll      C:\WINDOWS\System32\SAMLIB.dll N/A     Disabled
1484    explorer.exe    0x75f70000      0xa000  davclnt.dll     C:\WINDOWS\System32\davclnt.dll        N/A     Disabled
1484    explorer.exe    0x76ee0000      0x3c000 RASAPI32.DLL    C:\WINDOWS\system32\RASAPI32.DLL       N/A     Disabled
1484    explorer.exe    0x76e90000      0x12000 rasman.dll      C:\WINDOWS\system32\rasman.dll N/A     Disabled
1484    explorer.exe    0x76eb0000      0x2f000 TAPI32.dll      C:\WINDOWS\system32\TAPI32.dll N/A     Disabled
1484    explorer.exe    0x71a50000      0x3f000 mswsock.dll     C:\WINDOWS\System32\mswsock.dll        N/A     Disabled
1484    explorer.exe    0x76f20000      0x27000 DNSAPI.dll      C:\WINDOWS\system32\DNSAPI.dll N/A     Disabled
1484    explorer.exe    0x76fb0000      0x8000  winrnr.dll      C:\WINDOWS\System32\winrnr.dll N/A     Disabled
1484    explorer.exe    0x662b0000      0x58000 hnetcfg.dll     C:\WINDOWS\system32\hnetcfg.dll        N/A     Disabled
1484    explorer.exe    0x71a90000      0x8000  wshtcpip.dll    C:\WINDOWS\System32\wshtcpip.dll       N/A     Disabled
1512    spoolsv.exe     0x1000000       0x10000 spoolsv.exe     C:\WINDOWS\system32\spoolsv.exe        N/A     Disabled
1512    spoolsv.exe     0x7c900000      0xaf000 ntdll.dll       C:\WINDOWS\system32\ntdll.dll  N/A     Disabled
1512    spoolsv.exe     0x7c800000      0xf6000 kernel32.dll    C:\WINDOWS\system32\kernel32.dll       N/A     Disabled
1512    spoolsv.exe     0x77dd0000      0x9b000 ADVAPI32.dll    C:\WINDOWS\system32\ADVAPI32.dll       N/A     Disabled
1512    spoolsv.exe     0x77e70000      0x92000 RPCRT4.dll      C:\WINDOWS\system32\RPCRT4.dll N/A     Disabled
1512    spoolsv.exe     0x77fe0000      0x11000 Secur32.dll     C:\WINDOWS\system32\Secur32.dll        N/A     Disabled
1512    spoolsv.exe     0x77f10000      0x49000 GDI32.dll       C:\WINDOWS\system32\GDI32.dll  N/A     Disabled
1512    spoolsv.exe     0x7e410000      0x91000 USER32.dll      C:\WINDOWS\system32\USER32.dll N/A     Disabled
1512    spoolsv.exe     0x77c10000      0x58000 msvcrt.dll      C:\WINDOWS\system32\msvcrt.dll N/A     Disabled
1512    spoolsv.exe     0x5cb70000      0x26000 ShimEng.dll     C:\WINDOWS\system32\ShimEng.dll        N/A     Disabled
1512    spoolsv.exe     0x6f880000      0x1ca000        AcGenral.DLL    C:\WINDOWS\AppPatch\AcGenral.DLL       N/A     Disabled
1512    spoolsv.exe     0x76b40000      0x2d000 WINMM.dll       C:\WINDOWS\system32\WINMM.dll  N/A     Disabled
1512    spoolsv.exe     0x774e0000      0x13d000        ole32.dll       C:\WINDOWS\system32\ole32.dll  N/A     Disabled
1512    spoolsv.exe     0x77120000      0x8b000 OLEAUT32.dll    C:\WINDOWS\system32\OLEAUT32.dll       N/A     Disabled
1512    spoolsv.exe     0x77be0000      0x15000 MSACM32.dll     C:\WINDOWS\system32\MSACM32.dll        N/A     Disabled
1512    spoolsv.exe     0x77c00000      0x8000  VERSION.dll     C:\WINDOWS\system32\VERSION.dll        N/A     Disabled
1512    spoolsv.exe     0x7c9c0000      0x817000        SHELL32.dll     C:\WINDOWS\system32\SHELL32.dll        N/A     Disabled
1512    spoolsv.exe     0x77f60000      0x76000 SHLWAPI.dll     C:\WINDOWS\system32\SHLWAPI.dll        N/A     Disabled
1512    spoolsv.exe     0x769c0000      0xb4000 USERENV.dll     C:\WINDOWS\system32\USERENV.dll        N/A     Disabled
1512    spoolsv.exe     0x5ad70000      0x38000 UxTheme.dll     C:\WINDOWS\system32\UxTheme.dll        N/A     Disabled
1512    spoolsv.exe     0x773d0000      0x103000        comctl32.dll    C:\WINDOWS\WinSxS\x86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.5512_x-ww_35d4ce83\comctl32.dll     N/A     Disabled
1512    spoolsv.exe     0x5d090000      0x9a000 comctl32.dll    C:\WINDOWS\system32\comctl32.dll       N/A     Disabled
1512    spoolsv.exe     0x742e0000      0x15000 SPOOLSS.DLL     C:\WINDOWS\system32\SPOOLSS.DLL        N/A     Disabled
1512    spoolsv.exe     0x71ab0000      0x17000 WS2_32.dll      C:\WINDOWS\system32\WS2_32.dll N/A     Disabled
1512    spoolsv.exe     0x71aa0000      0x8000  WS2HELP.dll     C:\WINDOWS\system32\WS2HELP.dll        N/A     Disabled
1512    spoolsv.exe     0x76f20000      0x27000 DNSAPI.dll      C:\WINDOWS\system32\DNSAPI.dll N/A     Disabled
1512    spoolsv.exe     0x76fc0000      0x6000  rasadhlp.dll    C:\WINDOWS\system32\rasadhlp.dll       N/A     Disabled
1512    spoolsv.exe     0x75bb0000      0x56000 localspl.dll    C:\WINDOWS\system32\localspl.dll       N/A     Disabled
1512    spoolsv.exe     0x76c60000      0x2a000 sfc_os.dll      C:\WINDOWS\system32\sfc_os.dll N/A     Disabled
1512    spoolsv.exe     0x76c30000      0x2e000 WINTRUST.dll    C:\WINDOWS\system32\WINTRUST.dll       N/A     Disabled
1512    spoolsv.exe     0x77a80000      0x95000 CRYPT32.dll     C:\WINDOWS\system32\CRYPT32.dll        N/A     Disabled
1512    spoolsv.exe     0x77b20000      0x12000 MSASN1.dll      C:\WINDOWS\system32\MSASN1.dll N/A     Disabled
1512    spoolsv.exe     0x76c90000      0x28000 IMAGEHLP.dll    C:\WINDOWS\system32\IMAGEHLP.dll       N/A     Disabled
1512    spoolsv.exe     0x73000000      0x26000 winspool.drv    C:\WINDOWS\system32\winspool.drv       N/A     Disabled
1512    spoolsv.exe     0x5b860000      0x55000 netapi32.dll    C:\WINDOWS\system32\netapi32.dll       N/A     Disabled
1512    spoolsv.exe     0x742a0000      0xe000  cnbjmon.dll     C:\WINDOWS\system32\cnbjmon.dll        N/A     Disabled
1512    spoolsv.exe     0x74280000      0x7000  pjlmon.dll      C:\WINDOWS\system32\pjlmon.dll N/A     Disabled
1512    spoolsv.exe     0x72400000      0xe000  tcpmon.dll      C:\WINDOWS\system32\tcpmon.dll N/A     Disabled
1512    spoolsv.exe     0x723f0000      0x7000  usbmon.dll      C:\WINDOWS\system32\usbmon.dll N/A     Disabled
1512    spoolsv.exe     0x71a50000      0x3f000 mswsock.dll     C:\WINDOWS\System32\mswsock.dll        N/A     Disabled
1512    spoolsv.exe     0x76fb0000      0x8000  winrnr.dll      C:\WINDOWS\System32\winrnr.dll N/A     Disabled
1512    spoolsv.exe     0x76f60000      0x2c000 WLDAP32.dll     C:\WINDOWS\system32\WLDAP32.dll        N/A     Disabled
1512    spoolsv.exe     0x75c10000      0x24000 win32spl.dll    C:\WINDOWS\system32\win32spl.dll       N/A     Disabled
1512    spoolsv.exe     0x71c80000      0x7000  NETRAP.dll      C:\WINDOWS\system32\NETRAP.dll N/A     Disabled
1512    spoolsv.exe     0x767a0000      0x13000 NTDSAPI.dll     C:\WINDOWS\system32\NTDSAPI.dll        N/A     Disabled
1512    spoolsv.exe     0x76fd0000      0x7f000 CLBCATQ.DLL     C:\WINDOWS\system32\CLBCATQ.DLL        N/A     Disabled
1512    spoolsv.exe     0x77050000      0xc5000 COMRes.dll      C:\WINDOWS\system32\COMRes.dll N/A     Disabled
1512    spoolsv.exe     0x74300000      0x15000 inetpp.dll      C:\WINDOWS\system32\inetpp.dll N/A     Disabled
1512    spoolsv.exe     0x1010000       0x2c5000        xpsp2res.dll    C:\WINDOWS\system32\xpsp2res.dll       N/A     Disabled
1640    reader_sl.exe   0x400000        0xa000  Reader_sl.exe   C:\Program Files\Adobe\Reader 9.0\Reader\Reader_sl.exe N/A     Disabled
1640    reader_sl.exe   0x7c900000      0xaf000 ntdll.dll       C:\WINDOWS\system32\ntdll.dll  N/A     Disabled
1640    reader_sl.exe   0x7c800000      0xf6000 kernel32.dll    C:\WINDOWS\system32\kernel32.dll       N/A     Disabled
1640    reader_sl.exe   0x7e410000      0x91000 USER32.dll      C:\WINDOWS\system32\USER32.dll N/A     Disabled
1640    reader_sl.exe   0x77f10000      0x49000 GDI32.dll       C:\WINDOWS\system32\GDI32.dll  N/A     Disabled
1640    reader_sl.exe   0x77dd0000      0x9b000 ADVAPI32.dll    C:\WINDOWS\system32\ADVAPI32.dll       N/A     Disabled
1640    reader_sl.exe   0x77e70000      0x92000 RPCRT4.dll      C:\WINDOWS\system32\RPCRT4.dll N/A     Disabled
1640    reader_sl.exe   0x77fe0000      0x11000 Secur32.dll     C:\WINDOWS\system32\Secur32.dll        N/A     Disabled
1640    reader_sl.exe   0x7c9c0000      0x817000        SHELL32.dll     C:\WINDOWS\system32\SHELL32.dll        N/A     Disabled
1640    reader_sl.exe   0x77c10000      0x58000 msvcrt.dll      C:\WINDOWS\system32\msvcrt.dll N/A     Disabled
1640    reader_sl.exe   0x77f60000      0x76000 SHLWAPI.dll     C:\WINDOWS\system32\SHLWAPI.dll        N/A     Disabled
1640    reader_sl.exe   0x7c420000      0x87000 MSVCP80.dll     C:\WINDOWS\WinSxS\x86_Microsoft.VC80.CRT_1fc8b3b9a1e18e3b_8.0.50727.762_x-ww_6b128700\MSVCP80.dll      N/A   Disabled
1640    reader_sl.exe   0x78130000      0x9b000 MSVCR80.dll     C:\WINDOWS\WinSxS\x86_Microsoft.VC80.CRT_1fc8b3b9a1e18e3b_8.0.50727.762_x-ww_6b128700\MSVCR80.dll      N/A   Disabled
1640    reader_sl.exe   0x773d0000      0x103000        comctl32.dll    C:\WINDOWS\WinSxS\x86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.5512_x-ww_35d4ce83\comctl32.dll     N/A     Disabled
1640    reader_sl.exe   0x5d090000      0x9a000 comctl32.dll    C:\WINDOWS\system32\comctl32.dll       N/A     Disabled
1640    reader_sl.exe   0x5ad70000      0x38000 uxtheme.dll     C:\WINDOWS\system32\uxtheme.dll        N/A     Disabled
1640    reader_sl.exe   0x71ab0000      0x17000 WS2_32.dll      C:\WINDOWS\system32\WS2_32.dll N/A     Disabled
1640    reader_sl.exe   0x71aa0000      0x8000  WS2HELP.dll     C:\WINDOWS\system32\WS2HELP.dll        N/A     Disabled
788     alg.exe 0x1000000       0xd000  alg.exe C:\WINDOWS\System32\alg.exe     N/A   Disabled
788     alg.exe 0x7c900000      0xaf000 ntdll.dll       C:\WINDOWS\system32\ntdll.dll N/A      Disabled
788     alg.exe 0x7c800000      0xf6000 kernel32.dll    C:\WINDOWS\system32\kernel32.dll       N/A     Disabled
788     alg.exe 0x77c10000      0x58000 msvcrt.dll      C:\WINDOWS\system32\msvcrt.dllN/A      Disabled
788     alg.exe 0x76b20000      0x11000 ATL.DLL C:\WINDOWS\System32\ATL.DLL     N/A   Disabled
788     alg.exe 0x7e410000      0x91000 USER32.dll      C:\WINDOWS\system32\USER32.dllN/A      Disabled
788     alg.exe 0x77f10000      0x49000 GDI32.dll       C:\WINDOWS\system32\GDI32.dll N/A      Disabled
788     alg.exe 0x77dd0000      0x9b000 ADVAPI32.dll    C:\WINDOWS\system32\ADVAPI32.dll       N/A     Disabled
788     alg.exe 0x77e70000      0x92000 RPCRT4.dll      C:\WINDOWS\system32\RPCRT4.dllN/A      Disabled
788     alg.exe 0x77fe0000      0x11000 Secur32.dll     C:\WINDOWS\system32\Secur32.dllN/A     Disabled
788     alg.exe 0x774e0000      0x13d000        ole32.dll       C:\WINDOWS\system32\ole32.dll  N/A     Disabled
788     alg.exe 0x77120000      0x8b000 OLEAUT32.dll    C:\WINDOWS\system32\OLEAUT32.dll       N/A     Disabled
788     alg.exe 0x71ad0000      0x9000  WSOCK32.dll     C:\WINDOWS\System32\WSOCK32.dllN/A     Disabled
788     alg.exe 0x71ab0000      0x17000 WS2_32.dll      C:\WINDOWS\System32\WS2_32.dllN/A      Disabled
788     alg.exe 0x71aa0000      0x8000  WS2HELP.dll     C:\WINDOWS\System32\WS2HELP.dllN/A     Disabled
788     alg.exe 0x71a50000      0x3f000 MSWSOCK.DLL     C:\WINDOWS\System32\MSWSOCK.DLLN/A     Disabled
788     alg.exe 0x5cb70000      0x26000 ShimEng.dll     C:\WINDOWS\System32\ShimEng.dllN/A     Disabled
788     alg.exe 0x6f880000      0x1ca000        AcGenral.DLL    C:\WINDOWS\AppPatch\AcGenral.DLL       N/A     Disabled
788     alg.exe 0x76b40000      0x2d000 WINMM.dll       C:\WINDOWS\System32\WINMM.dll N/A      Disabled
788     alg.exe 0x77be0000      0x15000 MSACM32.dll     C:\WINDOWS\System32\MSACM32.dllN/A     Disabled
788     alg.exe 0x77c00000      0x8000  VERSION.dll     C:\WINDOWS\system32\VERSION.dllN/A     Disabled
788     alg.exe 0x7c9c0000      0x817000        SHELL32.dll     C:\WINDOWS\system32\SHELL32.dll        N/A     Disabled
788     alg.exe 0x77f60000      0x76000 SHLWAPI.dll     C:\WINDOWS\system32\SHLWAPI.dllN/A     Disabled
788     alg.exe 0x769c0000      0xb4000 USERENV.dll     C:\WINDOWS\system32\USERENV.dllN/A     Disabled
788     alg.exe 0x5ad70000      0x38000 UxTheme.dll     C:\WINDOWS\System32\UxTheme.dllN/A     Disabled
788     alg.exe 0x773d0000      0x103000        comctl32.dll    C:\WINDOWS\WinSxS\x86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.5512_x-ww_35d4ce83\comctl32.dll     N/A     Disabled
788     alg.exe 0x5d090000      0x9a000 comctl32.dll    C:\WINDOWS\system32\comctl32.dll       N/A     Disabled
788     alg.exe 0x76fd0000      0x7f000 CLBCATQ.DLL     C:\WINDOWS\System32\CLBCATQ.DLLN/A     Disabled
788     alg.exe 0x77050000      0xc5000 COMRes.dll      C:\WINDOWS\System32\COMRes.dllN/A      Disabled
788     alg.exe 0x680000        0x2c5000        xpsp2res.dll    C:\WINDOWS\System32\xpsp2res.dll       N/A     Disabled
788     alg.exe 0x662b0000      0x58000 hnetcfg.dll     C:\WINDOWS\system32\hnetcfg.dllN/A     Disabled
788     alg.exe 0x71a90000      0x8000  wshtcpip.dll    C:\WINDOWS\System32\wshtcpip.dll       N/A     Disabled
1136    wuauclt.exe     0x400000        0x1e000 wuauclt.exe     C:\WINDOWS\system32\wuauclt.exe        N/A     Disabled
1136    wuauclt.exe     0x7c900000      0xaf000 ntdll.dll       C:\WINDOWS\system32\ntdll.dll  N/A     Disabled
1136    wuauclt.exe     0x7c800000      0xf6000 kernel32.dll    C:\WINDOWS\system32\kernel32.dll       N/A     Disabled
1136    wuauclt.exe     0x77c10000      0x58000 msvcrt.dll      C:\WINDOWS\system32\msvcrt.dll N/A     Disabled
1136    wuauclt.exe     0x76b20000      0x11000 ATL.DLL C:\WINDOWS\system32\ATL.DLL   N/A      Disabled
1136    wuauclt.exe     0x7e410000      0x91000 USER32.dll      C:\WINDOWS\system32\USER32.dll N/A     Disabled
1136    wuauclt.exe     0x77f10000      0x49000 GDI32.dll       C:\WINDOWS\system32\GDI32.dll  N/A     Disabled
1136    wuauclt.exe     0x77dd0000      0x9b000 ADVAPI32.dll    C:\WINDOWS\system32\ADVAPI32.dll       N/A     Disabled
1136    wuauclt.exe     0x77e70000      0x92000 RPCRT4.dll      C:\WINDOWS\system32\RPCRT4.dll N/A     Disabled
1136    wuauclt.exe     0x77fe0000      0x11000 Secur32.dll     C:\WINDOWS\system32\Secur32.dll        N/A     Disabled
1136    wuauclt.exe     0x773d0000      0x103000        COMCTL32.dll    C:\WINDOWS\WinSxS\x86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.5512_x-ww_35d4ce83\COMCTL32.dll     N/A     Disabled
1136    wuauclt.exe     0x77f60000      0x76000 SHLWAPI.dll     C:\WINDOWS\system32\SHLWAPI.dll        N/A     Disabled
1136    wuauclt.exe     0x774e0000      0x13d000        ole32.dll       C:\WINDOWS\system32\ole32.dll  N/A     Disabled
1136    wuauclt.exe     0x77120000      0x8b000 OLEAUT32.dll    C:\WINDOWS\system32\OLEAUT32.dll       N/A     Disabled
1136    wuauclt.exe     0x50940000      0x2a000 wuaucpl.cpl     C:\WINDOWS\system32\wuaucpl.cpl        N/A     Disabled
1136    wuauclt.exe     0x76780000      0x9000  SHFOLDER.dll    C:\WINDOWS\system32\SHFOLDER.dll       N/A     Disabled
1136    wuauclt.exe     0x50040000      0x119000        wuaueng.dll     C:\WINDOWS\system32\wuaueng.dll        N/A     Disabled
1136    wuauclt.exe     0x75260000      0x29000 ADVPACK.dll     C:\WINDOWS\system32\ADVPACK.dll        N/A     Disabled
1136    wuauclt.exe     0x77c00000      0x8000  VERSION.dll     C:\WINDOWS\system32\VERSION.dll        N/A     Disabled
1136    wuauclt.exe     0x75150000      0x13000 Cabinet.dll     C:\WINDOWS\system32\Cabinet.dll        N/A     Disabled
1136    wuauclt.exe     0x77a80000      0x95000 CRYPT32.dll     C:\WINDOWS\system32\CRYPT32.dll        N/A     Disabled
1136    wuauclt.exe     0x77b20000      0x12000 MSASN1.dll      C:\WINDOWS\system32\MSASN1.dll N/A     Disabled
1136    wuauclt.exe     0x606b0000      0x10d000        ESENT.dll       C:\WINDOWS\system32\ESENT.dll  N/A     Disabled
1136    wuauclt.exe     0x600a0000      0xb000  mspatcha.dll    C:\WINDOWS\system32\mspatcha.dll       N/A     Disabled
1136    wuauclt.exe     0x77920000      0xf3000 SETUPAPI.dll    C:\WINDOWS\system32\SETUPAPI.dll       N/A     Disabled
1136    wuauclt.exe     0x76bb0000      0x5000  sfc.dll C:\WINDOWS\system32\sfc.dll   N/A      Disabled
1136    wuauclt.exe     0x76c60000      0x2a000 sfc_os.dll      C:\WINDOWS\system32\sfc_os.dll N/A     Disabled
1136    wuauclt.exe     0x76c30000      0x2e000 WINTRUST.dll    C:\WINDOWS\system32\WINTRUST.dll       N/A     Disabled
1136    wuauclt.exe     0x76c90000      0x28000 IMAGEHLP.dll    C:\WINDOWS\system32\IMAGEHLP.dll       N/A     Disabled
1136    wuauclt.exe     0x769c0000      0xb4000 USERENV.dll     C:\WINDOWS\system32\USERENV.dll        N/A     Disabled
1136    wuauclt.exe     0x4d4f0000      0x59000 WINHTTP.dll     C:\WINDOWS\system32\WINHTTP.dll        N/A     Disabled
1136    wuauclt.exe     0x73000000      0x26000 WINSPOOL.DRV    C:\WINDOWS\system32\WINSPOOL.DRV       N/A     Disabled
1136    wuauclt.exe     0x76360000      0x10000 WINSTA.dll      C:\WINDOWS\system32\WINSTA.dll N/A     Disabled
1136    wuauclt.exe     0x5b860000      0x55000 NETAPI32.dll    C:\WINDOWS\system32\NETAPI32.dll       N/A     Disabled
1136    wuauclt.exe     0x71ab0000      0x17000 WS2_32.dll      C:\WINDOWS\system32\WS2_32.dll N/A     Disabled
1136    wuauclt.exe     0x71aa0000      0x8000  WS2HELP.dll     C:\WINDOWS\system32\WS2HELP.dll        N/A     Disabled
1136    wuauclt.exe     0x76f50000      0x8000  WTSAPI32.dll    C:\WINDOWS\system32\WTSAPI32.dll       N/A     Disabled
1136    wuauclt.exe     0x76380000      0x5000  MSIMG32.dll     C:\WINDOWS\system32\MSIMG32.dll        N/A     Disabled
1136    wuauclt.exe     0x7c9c0000      0x817000        SHELL32.dll     C:\WINDOWS\system32\SHELL32.dll        N/A     Disabled
1136    wuauclt.exe     0x5cb70000      0x26000 ShimEng.dll     C:\WINDOWS\system32\ShimEng.dll        N/A     Disabled
1136    wuauclt.exe     0x6f880000      0x1ca000        AcGenral.DLL    C:\WINDOWS\AppPatch\AcGenral.DLL       N/A     Disabled
1136    wuauclt.exe     0x76b40000      0x2d000 WINMM.dll       C:\WINDOWS\system32\WINMM.dll  N/A     Disabled
1136    wuauclt.exe     0x77be0000      0x15000 MSACM32.dll     C:\WINDOWS\system32\MSACM32.dll        N/A     Disabled
1136    wuauclt.exe     0x5ad70000      0x38000 UxTheme.dll     C:\WINDOWS\system32\UxTheme.dll        N/A     Disabled
1136    wuauclt.exe     0xfb0000        0x2c5000        xpsp2res.dll    C:\WINDOWS\system32\xpsp2res.dll       N/A     Disabled
1136    wuauclt.exe     0x76fd0000      0x7f000 CLBCATQ.DLL     C:\WINDOWS\system32\CLBCATQ.DLL        N/A     Disabled
1136    wuauclt.exe     0x77050000      0xc5000 COMRes.dll      C:\WINDOWS\system32\COMRes.dll N/A     Disabled
1136    wuauclt.exe     0x50640000      0xc000  wups.dll        C:\WINDOWS\system32\wups.dll   N/A     Disabled
1588    wuauclt.exe     0x400000        0x1e000 wuauclt.exe     C:\WINDOWS\system32\wuauclt.exe        N/A     Disabled
1588    wuauclt.exe     0x7c900000      0xaf000 ntdll.dll       C:\WINDOWS\system32\ntdll.dll  N/A     Disabled
1588    wuauclt.exe     0x7c800000      0xf6000 kernel32.dll    C:\WINDOWS\system32\kernel32.dll       N/A     Disabled
1588    wuauclt.exe     0x77c10000      0x58000 msvcrt.dll      C:\WINDOWS\system32\msvcrt.dll N/A     Disabled
1588    wuauclt.exe     0x76b20000      0x11000 ATL.DLL C:\WINDOWS\system32\ATL.DLL   N/A      Disabled
1588    wuauclt.exe     0x7e410000      0x91000 USER32.dll      C:\WINDOWS\system32\USER32.dll N/A     Disabled
1588    wuauclt.exe     0x77f10000      0x49000 GDI32.dll       C:\WINDOWS\system32\GDI32.dll  N/A     Disabled
1588    wuauclt.exe     0x77dd0000      0x9b000 ADVAPI32.dll    C:\WINDOWS\system32\ADVAPI32.dll       N/A     Disabled
1588    wuauclt.exe     0x77e70000      0x92000 RPCRT4.dll      C:\WINDOWS\system32\RPCRT4.dll N/A     Disabled
1588    wuauclt.exe     0x77fe0000      0x11000 Secur32.dll     C:\WINDOWS\system32\Secur32.dll        N/A     Disabled
1588    wuauclt.exe     0x773d0000      0x103000        COMCTL32.dll    C:\WINDOWS\WinSxS\x86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.5512_x-ww_35d4ce83\COMCTL32.dll     N/A     Disabled
1588    wuauclt.exe     0x77f60000      0x76000 SHLWAPI.dll     C:\WINDOWS\system32\SHLWAPI.dll        N/A     Disabled
1588    wuauclt.exe     0x774e0000      0x13d000        ole32.dll       C:\WINDOWS\system32\ole32.dll  N/A     Disabled
1588    wuauclt.exe     0x77120000      0x8b000 OLEAUT32.dll    C:\WINDOWS\system32\OLEAUT32.dll       N/A     Disabled
1588    wuauclt.exe     0x50940000      0x2a000 wuaucpl.cpl     C:\WINDOWS\system32\wuaucpl.cpl        N/A     Disabled
1588    wuauclt.exe     0x76780000      0x9000  SHFOLDER.dll    C:\WINDOWS\system32\SHFOLDER.dll       N/A     Disabled
1588    wuauclt.exe     0x50040000      0x119000        wuaueng.dll     C:\WINDOWS\system32\wuaueng.dll        N/A     Disabled
1588    wuauclt.exe     0x75260000      0x29000 ADVPACK.dll     C:\WINDOWS\system32\ADVPACK.dll        N/A     Disabled
1588    wuauclt.exe     0x77c00000      0x8000  VERSION.dll     C:\WINDOWS\system32\VERSION.dll        N/A     Disabled
1588    wuauclt.exe     0x75150000      0x13000 Cabinet.dll     C:\WINDOWS\system32\Cabinet.dll        N/A     Disabled
1588    wuauclt.exe     0x77a80000      0x95000 CRYPT32.dll     C:\WINDOWS\system32\CRYPT32.dll        N/A     Disabled
1588    wuauclt.exe     0x77b20000      0x12000 MSASN1.dll      C:\WINDOWS\system32\MSASN1.dll N/A     Disabled
1588    wuauclt.exe     0x606b0000      0x10d000        ESENT.dll       C:\WINDOWS\system32\ESENT.dll  N/A     Disabled
1588    wuauclt.exe     0x600a0000      0xb000  mspatcha.dll    C:\WINDOWS\system32\mspatcha.dll       N/A     Disabled
1588    wuauclt.exe     0x77920000      0xf3000 SETUPAPI.dll    C:\WINDOWS\system32\SETUPAPI.dll       N/A     Disabled
1588    wuauclt.exe     0x76bb0000      0x5000  sfc.dll C:\WINDOWS\system32\sfc.dll   N/A      Disabled
1588    wuauclt.exe     0x76c60000      0x2a000 sfc_os.dll      C:\WINDOWS\system32\sfc_os.dll N/A     Disabled
1588    wuauclt.exe     0x76c30000      0x2e000 WINTRUST.dll    C:\WINDOWS\system32\WINTRUST.dll       N/A     Disabled
1588    wuauclt.exe     0x76c90000      0x28000 IMAGEHLP.dll    C:\WINDOWS\system32\IMAGEHLP.dll       N/A     Disabled
1588    wuauclt.exe     0x769c0000      0xb4000 USERENV.dll     C:\WINDOWS\system32\USERENV.dll        N/A     Disabled
1588    wuauclt.exe     0x4d4f0000      0x59000 WINHTTP.dll     C:\WINDOWS\system32\WINHTTP.dll        N/A     Disabled
1588    wuauclt.exe     0x73000000      0x26000 WINSPOOL.DRV    C:\WINDOWS\system32\WINSPOOL.DRV       N/A     Disabled
1588    wuauclt.exe     0x76360000      0x10000 WINSTA.dll      C:\WINDOWS\system32\WINSTA.dll N/A     Disabled
1588    wuauclt.exe     0x5b860000      0x55000 NETAPI32.dll    C:\WINDOWS\system32\NETAPI32.dll       N/A     Disabled
1588    wuauclt.exe     0x71ab0000      0x17000 WS2_32.dll      C:\WINDOWS\system32\WS2_32.dll N/A     Disabled
1588    wuauclt.exe     0x71aa0000      0x8000  WS2HELP.dll     C:\WINDOWS\system32\WS2HELP.dll        N/A     Disabled
1588    wuauclt.exe     0x76f50000      0x8000  WTSAPI32.dll    C:\WINDOWS\system32\WTSAPI32.dll       N/A     Disabled
1588    wuauclt.exe     0x76380000      0x5000  MSIMG32.dll     C:\WINDOWS\system32\MSIMG32.dll        N/A     Disabled
1588    wuauclt.exe     0x7c9c0000      0x817000        SHELL32.dll     C:\WINDOWS\system32\SHELL32.dll        N/A     Disabled
1588    wuauclt.exe     0x5cb70000      0x26000 ShimEng.dll     C:\WINDOWS\system32\ShimEng.dll        N/A     Disabled
1588    wuauclt.exe     0x6f880000      0x1ca000        AcGenral.DLL    C:\WINDOWS\AppPatch\AcGenral.DLL       N/A     Disabled
1588    wuauclt.exe     0x76b40000      0x2d000 WINMM.dll       C:\WINDOWS\system32\WINMM.dll  N/A     Disabled
1588    wuauclt.exe     0x77be0000      0x15000 MSACM32.dll     C:\WINDOWS\system32\MSACM32.dll        N/A     Disabled
1588    wuauclt.exe     0x5ad70000      0x38000 UxTheme.dll     C:\WINDOWS\system32\UxTheme.dll        N/A     Disabled
1588    wuauclt.exe     0x76fd0000      0x7f000 CLBCATQ.DLL     C:\WINDOWS\system32\CLBCATQ.DLL        N/A     Disabled
1588    wuauclt.exe     0x77050000      0xc5000 COMRes.dll      C:\WINDOWS\system32\COMRes.dll N/A     Disabled
1588    wuauclt.exe     0x1290000       0x2c5000        xpsp2res.dll    C:\WINDOWS\system32\xpsp2res.dll       N/A     Disabled
1588    wuauclt.exe     0x50640000      0xc000  wups.dll        C:\WINDOWS\system32\wups.dll   N/A     Disabled
```
### Volatility Hunting and Detection Capabilities
Volatility offers a plethora of plugins that can be used to aid in your hunting and detection capabilities when hunting for malware or other anomalies within a system's memory.
It is recommended that you have a basic understanding of how evasion techniques and various malware techniques are employed by adversaries, as well as how to hunt and detect them before going through this section.
The first plugin we will be talking about that is one of the most useful when hunting for code injection is malfind. This plugin will attempt to identify injected processes and their PIDs along with the offset address and a Hex, Ascii, and Disassembly view of the infected area. The plugin works by scanning the heap and identifying processes that have the executable bit set RWE or RX and/or no memory-mapped file on disk (file-less malware).
Based on what malfind identifies, the injected area will change. An MZ header is an indicator of a Windows executable file. The injected area could also be directed towards shellcode which requires further analysis.
Syntax: python3 vol.py -f <file> windows.malfind
```text
thmanalyst@ubuntu:/opt/volatility3$ python3 vol.py -f dump.vmem windows.malfind
Volatility 3 Framework 1.0.1
Progress:  100.00               PDB scanning finished                     
PID     Process Start VPN       End VPN Tag     Protection      CommitCharge    PrivateMemory  File output     Hexdump Disasm

584     csrss.exe       0x7f6f0000      0x7f7effff      Vad     PAGE_EXECUTE_READWRITE00       Disabled
c8 00 00 00 91 01 00 00 ........
ff ee ff ee 08 70 00 00 .....p..
08 00 00 00 00 fe 00 00 ........
00 00 10 00 00 20 00 00 ........
00 02 00 00 00 20 00 00 ........
8d 01 00 00 ff ef fd 7f ........
03 00 08 06 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........        c8 00 00 00 91 01 00 00 ff ee ff ee 08 70 00 00 08 00 00 00 00 fe 00 00 00 00 10 00 00 20 00 00 00 02 00 00 00 20 00 00 8d 01 00 00 ff ef fd 7f 03 00 08 06 00 00 00 00 00 00 00 00 00 00 00 00
608     winlogon.exe    0x13410000      0x13413fff      VadS    PAGE_EXECUTE_READWRITE41       Disabled
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 25 00 25 00 ....%.%.
01 00 00 00 00 00 00 00 ........        00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 25 00 25 00 01 00 00 00 00 00 00 00
608     winlogon.exe    0xf9e0000       0xf9e3fff       VadS    PAGE_EXECUTE_READWRITE41       Disabled
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 25 00 25 00 ....%.%.
01 00 00 00 00 00 00 00 ........        00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 25 00 25 00 01 00 00 00 00 00 00 00
608     winlogon.exe    0x4ee0000       0x4ee3fff       VadS    PAGE_EXECUTE_READWRITE41       Disabled
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 25 00 25 00 ....%.%.
01 00 00 00 00 00 00 00 ........        00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 25 00 25 00 01 00 00 00 00 00 00 00
608     winlogon.exe    0x554c0000      0x554c3fff      VadS    PAGE_EXECUTE_READWRITE41       Disabled
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 28 00 28 00 ....(.(.
01 00 00 00 00 00 00 00 ........        00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 28 00 28 00 01 00 00 00 00 00 00 00
608     winlogon.exe    0x4dc40000      0x4dc43fff      VadS    PAGE_EXECUTE_READWRITE41       Disabled
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 23 00 23 00 ....#.#.
01 00 00 00 00 00 00 00 ........        00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 23 00 23 00 01 00 00 00 00 00 00 00
608     winlogon.exe    0x4c540000      0x4c543fff      VadS    PAGE_EXECUTE_READWRITE41       Disabled
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 22 00 22 00 ....".".
01 00 00 00 00 00 00 00 ........        00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 22 00 22 00 01 00 00 00 00 00 00 00
608     winlogon.exe    0x5de10000      0x5de13fff      VadS    PAGE_EXECUTE_READWRITE41       Disabled
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 22 00 22 00 ....".".
01 00 00 00 00 00 00 00 ........        00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 22 00 22 00 01 00 00 00 00 00 00 00
608     winlogon.exe    0x6a230000      0x6a233fff      VadS    PAGE_EXECUTE_READWRITE41       Disabled
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 2b 00 2b 00 ....+.+.
01 00 00 00 00 00 00 00 ........        00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2b 00 2b 00 01 00 00 00 00 00 00 00
608     winlogon.exe    0x73f40000      0x73f43fff      VadS    PAGE_EXECUTE_READWRITE41       Disabled
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 2a 00 2a 00 ....*.*.
01 00 00 00 00 00 00 00 ........        00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2a 00 2a 00 01 00 00 00 00 00 00 00
1484    explorer.exe    0x1460000       0x1480fff       VadS    PAGE_EXECUTE_READWRITE33       1       Disabled
4d 5a 90 00 03 00 00 00 MZ......
04 00 00 00 ff ff 00 00 ........
b8 00 00 00 00 00 00 00 ........
40 00 00 00 00 00 00 00 @.......
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 e0 00 00 00 ........        4d 5a 90 00 03 00 00 00 04 00 00 00 ff ff 00 00 b8 00 00 00 00 00 00 00 40 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 e0 00 00 00
1640    reader_sl.exe   0x3d0000        0x3f0fff        VadS    PAGE_EXECUTE_READWRITE33       1       Disabled
4d 5a 90 00 03 00 00 00 MZ......
04 00 00 00 ff ff 00 00 ........
b8 00 00 00 00 00 00 00 ........
40 00 00 00 00 00 00 00 @.......
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 00 00 00 00 ........
00 00 00 00 e0 00 00 00 ........        4d 5a 90 00 03 00 00 00 04 00 00 00 ff ff 00 00 b8 00 00 00 00 00 00 00 40 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 e0 00 00 00
```
Volatility also offers the capability to compare the memory file against YARA rules. yarascan will search for strings, patterns, and compound rules against a rule set. You can either use a YARA file as an argument or list rules within the command line.
Syntax: python3 vol.py -f <file> windows.yarascan
There are other plugins that can be considered part of Volatility's hunting and detection capabilities; however, we will be covering them in the next task.
### Advanced Memory Forensics
Advanced Memory Forensics can become confusing when you begin talking about system objects and how malware interacts directly with the system, especially if you do not have prior experience hunting some of the techniques used such as hooking and driver manipulation. When dealing with an advanced adversary, you may encounter malware, most of the time rootkits that will employ very nasty evasion measures that will require you as an analyst to dive into the drivers, mutexes, and hooked functions. A number of modules can help us in this journey to further uncover malware hiding within memory.
The first evasion technique we will be hunting is hooking; there are five methods of hooking employed by adversaries, outlined below:
SSDT Hooks
IRP Hooks
IAT Hooks
EAT Hooks
Inline Hooks
We will only be focusing on hunting SSDT hooking as this one of the most common techniques when dealing with malware evasion and the easiest plugin to use with the base volatility plugins.
The ssdt plugin will search for hooking and output its results. Hooking can be used by legitimate applications, so it is up to you as the analyst to identify what is evil. As a brief overview of what SSDT hooking is: SSDT stands for System Service Descriptor Table; the Windows kernel uses this table to look up system functions. An adversary can hook into this table and modify pointers to point to a location the rootkit controls.
There can be hundreds of table entries that ssdt will dump; you will then have to analyze the output further or compare against a baseline. A suggestion is to use this plugin after investigating the initial compromise and working off it as part of your lead investigation.
Syntax: python3 vol.py -f <file> windows.ssdt
Adversaries will also use malicious driver files as part of their evasion. Volatility offers two plugins to list drivers.
The modules plugin will dump a list of loaded kernel modules; this can be useful in identifying active malware. However, if a malicious file is idly waiting or hidden, this plugin may miss it.
This plugin is best used once you have further investigated and found potential indicators to use as input for searching and filtering.
Syntax: python3 vol.py -f <file> windows.modules
The driverscan plugin will scan for drivers present on the system at the time of extraction. This plugin can help to identify driver files in the kernel that the modules plugin might have missed or were hidden.
As with the last plugin, it is again recommended to have a prior investigation before moving on to this plugin. It is also recommended to look through the modules plugin before driverscan.
Syntax: python3 vol.py -f <file> windows.driverscan
In most cases, driverscan will come up with no output; however, if you do not find anything with the modules plugin, it can be useful to attempt using this plugin.
There are also other plugins listed below that can be helpful when attempting to hunt for advanced malware in memory.
modscan
driverirp
callbacks
idt
apihooks
moddump
handles
Note: Some of these are only present on Volatility2 or are part of third-party plugins. To get the most out of Volatility, you may need to move to some third-party or custom plugins.

## Enumeration
```text
thmanalyst@ubuntu:/opt/volatility3$ python3 vol.py -f dump.vmem windows.ssdt
Volatility 3 Framework 1.0.1
Progress:  100.00               PDB scanning finished                     
Index   Address Module  Symbol

0       0x80599948      ntoskrnl        NtAcceptConnectPort
1       0x805e6db6      ntoskrnl        NtAccessCheck
2       0x805ea5fc      ntoskrnl        NtAccessCheckAndAuditAlarm
3       0x805e6de8      ntoskrnl        NtAccessCheckByType
4       0x805ea636      ntoskrnl        NtAccessCheckByTypeAndAuditAlarm
5       0x805e6e1e      ntoskrnl        NtAccessCheckByTypeResultList
6       0x805ea67a      ntoskrnl        NtAccessCheckByTypeResultListAndAuditAlarm
7       0x805ea6be      ntoskrnl        NtAccessCheckByTypeResultListAndAuditAlarmByHandle
8       0x8060bdfe      ntoskrnl        NtAddAtom
9       0x8060cb50      ntoskrnl        NtAddBootEntry
9       0x8060cb50      ntoskrnl        NtEnumerateBootEntries
9       0x8060cb50      ntoskrnl        NtQueryBootEntryOrder
9       0x8060cb50      ntoskrnl        NtQueryBootOptions
9       0x8060cb50      ntoskrnl        NtSetBootEntryOrder
9       0x8060cb50      ntoskrnl        NtSetBootOptions
10      0x805e21b4      ntoskrnl        NtAdjustGroupsToken
11      0x805e1e0c      ntoskrnl        NtAdjustPrivilegesToken
12      0x805cade6      ntoskrnl        NtAlertResumeThread
13      0x805cad96      ntoskrnl        NtAlertThread
14      0x8060c424      ntoskrnl        NtAllocateLocallyUniqueId
15      0x805ab5ae      ntoskrnl        NtAllocateUserPhysicalPages
16      0x8060ba3c      ntoskrnl        NtAllocateUuids
17      0x8059ddbe      ntoskrnl        NtAllocateVirtualMemory
18      0x805a5a00      ntoskrnl        NtAreMappedFilesTheSame
19      0x805cc8c4      ntoskrnl        NtAssignProcessToJobObject
20      0x804ff828      ntoskrnl        NtCallbackReturn
21      0x8060cb42      ntoskrnl        NtCancelDeviceWakeupRequest
21      0x8060cb42      ntoskrnl        NtDeleteBootEntry
21      0x8060cb42      ntoskrnl        NtModifyBootEntry
22      0x8056bcd6      ntoskrnl        NtCancelIoFile
23      0x8053500e      ntoskrnl        NtCancelTimer
24      0x806050d4      ntoskrnl        NtClearEvent
25      0x805b1c3a      ntoskrnl        NtClose
26      0x805eab36      ntoskrnl        NtCloseObjectAuditAlarm
27      0x80619e56      ntoskrnl        NtCompactKeys
28      0x805ef028      ntoskrnl        NtCompareTokens
29      0x8059a036      ntoskrnl        NtCompleteConnectPort
30      0x8061a0aa      ntoskrnl        NtCompressKey
31      0x805998e8      ntoskrnl        NtConnectPort
32      0x80540e00      ntoskrnl        NtContinue
33      0x806389aa      ntoskrnl        NtCreateDebugObject
34      0x805b3c6e      ntoskrnl        NtCreateDirectoryObject
35      0x80605124      ntoskrnl        NtCreateEvent
36      0x8060d3c6      ntoskrnl        NtCreateEventPair
37      0x8056e27c      ntoskrnl        NtCreateFile
38      0x8056dc5a      ntoskrnl        NtCreateIoCompletion
39      0x805cb888      ntoskrnl        NtCreateJobObject
40      0x805cb5c0      ntoskrnl        NtCreateJobSet
41      0x8061a286      ntoskrnl        NtCreateKey
42      0x8056e38a      ntoskrnl        NtCreateMailslotFile
43      0x8060d7be      ntoskrnl        NtCreateMutant
44      0x8056e2b6      ntoskrnl        NtCreateNamedPipeFile
45      0x805a0da8      ntoskrnl        NtCreatePagingFile
46      0x8059a404      ntoskrnl        NtCreatePort
47      0x805c7420      ntoskrnl        NtCreateProcess
48      0x805c736a      ntoskrnl        NtCreateProcessEx
49      0x8060dbde      ntoskrnl        NtCreateProfile
50      0x805a06ec      ntoskrnl        NtCreateSection
51      0x8060b15a      ntoskrnl        NtCreateSemaphore
52      0x805b9594      ntoskrnl        NtCreateSymbolicLinkObject
53      0x805c7208      ntoskrnl        NtCreateThread
54      0x8060d08e      ntoskrnl        NtCreateTimer
55      0x805ef3d0      ntoskrnl        NtCreateToken
56      0x8059a428      ntoskrnl        NtCreateWaitablePort
57      0x80639a86      ntoskrnl        NtDebugActiveProcess
58      0x80639bd6      ntoskrnl        NtDebugContinue
59      0x8060ca92      ntoskrnl        NtDelayExecution
60      0x8060c2b4      ntoskrnl        NtDeleteAtom
61      0x8060cb42      ntoskrnl        NtCancelDeviceWakeupRequest
61      0x8060cb42      ntoskrnl        NtDeleteBootEntry
61      0x8060cb42      ntoskrnl        NtModifyBootEntry
62      0x8056be1c      ntoskrnl        NtDeleteFile
63      0x8061a716      ntoskrnl        NtDeleteKey
64      0x805eac42      ntoskrnl        NtDeleteObjectAuditAlarm
65      0x8061a8e6      ntoskrnl        NtDeleteValueKey
66      0x8056e442      ntoskrnl        NtDeviceIoControlFile
67      0x806090ce      ntoskrnl        NtDisplayString
68      0x805b384e      ntoskrnl        NtDuplicateObject
69      0x805e3062      ntoskrnl        NtDuplicateToken
70      0x8060cb50      ntoskrnl        NtAddBootEntry
70      0x8060cb50      ntoskrnl        NtEnumerateBootEntries
70      0x8060cb50      ntoskrnl        NtQueryBootEntryOrder
70      0x8060cb50      ntoskrnl        NtQueryBootOptions
70      0x8060cb50      ntoskrnl        NtSetBootEntryOrder
70      0x8060cb50      ntoskrnl        NtSetBootOptions
71      0x8061aac6      ntoskrnl        NtEnumerateKey
72      0x8060cb34      ntoskrnl        NtEnumerateSystemEnvironmentValuesEx
73      0x8061ad30      ntoskrnl        NtEnumerateValueKey
74      0x805a9126      ntoskrnl        NtExtendSection
75      0x805e320e      ntoskrnl        NtFilterToken
76      0x8060c068      ntoskrnl        NtFindAtom
77      0x8056bee8      ntoskrnl        NtFlushBuffersFile
78      0x805abe38      ntoskrnl        NtFlushInstructionCache
79      0x8061af9a      ntoskrnl        NtFlushKey
80      0x805a1ab8      ntoskrnl        NtFlushVirtualMemory
81      0x805abdda      ntoskrnl        NtFlushWriteBuffer
82      0x805ab94a      ntoskrnl        NtFreeUserPhysicalPages
83      0x805a8400      ntoskrnl        NtFreeVirtualMemory
84      0x8056e476      ntoskrnl        NtFsControlFile
85      0x805c771a      ntoskrnl        NtGetContextThread
86      0x805be4d8      ntoskrnl        NtGetDevicePowerState
87      0x8058e588      ntoskrnl        NtGetPlugPlayEvent
88      0x8051d9a2      ntoskrnl        NtGetWriteWatch
89      0x805eed1c      ntoskrnl        NtImpersonateAnonymousToken
90      0x8059a492      ntoskrnl        NtImpersonateClientOfPort
91      0x805cda5c      ntoskrnl        NtImpersonateThread
92      0x806183dc      ntoskrnl        NtInitializeRegistry
93      0x805be2be      ntoskrnl        NtInitiatePowerAction
94      0x805cb484      ntoskrnl        NtIsProcessInJob
95      0x805be4c4      ntoskrnl        NtIsSystemResumeAutomatic
96      0x8059a69e      ntoskrnl        NtListenPort
97      0x80579588      ntoskrnl        NtLoadDriver
98      0x8061c482      ntoskrnl        NtLoadKey
99      0x8061c08e      ntoskrnl        NtLoadKey2
100     0x8056e4aa      ntoskrnl        NtLockFile
101     0x80609630      ntoskrnl        NtLockProductActivationKeys
102     0x8061a156      ntoskrnl        NtLockRegistryKey
103     0x805abf40      ntoskrnl        NtLockVirtualMemory
104     0x805b50ee      ntoskrnl        NtMakePermanentObject
105     0x805b1cde      ntoskrnl        NtMakeTemporaryObject
106     0x805aa8a2      ntoskrnl        NtMapUserPhysicalPages
107     0x805aae7a      ntoskrnl        NtMapUserPhysicalPagesScatter
108     0x805a7480      ntoskrnl        NtMapViewOfSection
109     0x8060cb42      ntoskrnl        NtCancelDeviceWakeupRequest
109     0x8060cb42      ntoskrnl        NtDeleteBootEntry
109     0x8060cb42      ntoskrnl        NtModifyBootEntry
110     0x8056f0da      ntoskrnl        NtNotifyChangeDirectoryFile
111     0x8061c44c      ntoskrnl        NtNotifyChangeKey
112     0x8061b09c      ntoskrnl        NtNotifyChangeMultipleKeys
113     0x805b3d40      ntoskrnl        NtOpenDirectoryObject
114     0x80605224      ntoskrnl        NtOpenEvent
115     0x8060d49e      ntoskrnl        NtOpenEventPair
116     0x8056f39a      ntoskrnl        NtOpenFile
117     0x8056dd32      ntoskrnl        NtOpenIoCompletion
118     0x805cba0e      ntoskrnl        NtOpenJobObject
119     0x8061b658      ntoskrnl        NtOpenKey
120     0x8060d896      ntoskrnl        NtOpenMutant
121     0x805ea704      ntoskrnl        NtOpenObjectAuditAlarm
122     0x805c1296      ntoskrnl        NtOpenProcess
123     0x805e39fc      ntoskrnl        NtOpenProcessToken
124     0x805e3660      ntoskrnl        NtOpenProcessTokenEx
125     0x8059f722      ntoskrnl        NtOpenSection
126     0x8060b254      ntoskrnl        NtOpenSemaphore
127     0x805b977a      ntoskrnl        NtOpenSymbolicLinkObject
128     0x805c1522      ntoskrnl        NtOpenThread
129     0x805e3a1a      ntoskrnl        NtOpenThreadToken
130     0x805e37d0      ntoskrnl        NtOpenThreadTokenEx
131     0x8060d1b0      ntoskrnl        NtOpenTimer
132     0x8063bc78      ntoskrnl        NtPlugPlayControl
133     0x805bf346      ntoskrnl        NtPowerInformation
134     0x805eddce      ntoskrnl        NtPrivilegeCheck
135     0x805e9a16      ntoskrnl        NtPrivilegeObjectAuditAlarm
136     0x805e9c02      ntoskrnl        NtPrivilegedServiceAuditAlarm
137     0x805ada08      ntoskrnl        NtProtectVirtualMemory
138     0x806052dc      ntoskrnl        NtPulseEvent
139     0x8056c0ce      ntoskrnl        NtQueryAttributesFile
140     0x8060cb50      ntoskrnl        NtAddBootEntry
140     0x8060cb50      ntoskrnl        NtEnumerateBootEntries
140     0x8060cb50      ntoskrnl        NtQueryBootEntryOrder
140     0x8060cb50      ntoskrnl        NtQueryBootOptions
140     0x8060cb50      ntoskrnl        NtSetBootEntryOrder
140     0x8060cb50      ntoskrnl        NtSetBootOptions
141     0x8060cb50      ntoskrnl        NtAddBootEntry
141     0x8060cb50      ntoskrnl        NtEnumerateBootEntries
141     0x8060cb50      ntoskrnl        NtQueryBootEntryOrder
141     0x8060cb50      ntoskrnl        NtQueryBootOptions
141     0x8060cb50      ntoskrnl        NtSetBootEntryOrder
141     0x8060cb50      ntoskrnl        NtSetBootOptions
142     0x8053c02e      ntoskrnl        NtQueryDebugFilterState
143     0x80606e68      ntoskrnl        NtQueryDefaultLocale
144     0x80607ac8      ntoskrnl        NtQueryDefaultUILanguage
145     0x8056f074      ntoskrnl        NtQueryDirectoryFile
146     0x805b3de0      ntoskrnl        NtQueryDirectoryObject
147     0x8056f3ca      ntoskrnl        NtQueryEaFile
148     0x806053a4      ntoskrnl        NtQueryEvent
149     0x8056c222      ntoskrnl        NtQueryFullAttributesFile
150     0x8060c2dc      ntoskrnl        NtQueryInformationAtom
151     0x8056fc46      ntoskrnl        NtQueryInformationFile
152     0x805cbee0      ntoskrnl        NtQueryInformationJobObject
153     0x8059a6fc      ntoskrnl        NtQueryInformationPort
154     0x805c2bfc      ntoskrnl        NtQueryInformationProcess
155     0x805c17c8      ntoskrnl        NtQueryInformationThread
156     0x805e3afa      ntoskrnl        NtQueryInformationToken
157     0x80607266      ntoskrnl        NtQueryInstallUILanguage
158     0x8060e060      ntoskrnl        NtQueryIntervalProfile
159     0x8056ddda      ntoskrnl        NtQueryIoCompletion
160     0x8061b97e      ntoskrnl        NtQueryKey
161     0x806193d4      ntoskrnl        NtQueryMultipleValueKey
162     0x8060d93e      ntoskrnl        NtQueryMutant
163     0x805bb04c      ntoskrnl        NtQueryObject
164     0x80619a80      ntoskrnl        NtQueryOpenSubKeys
165     0x8060e0ee      ntoskrnl        NtQueryPerformanceCounter
166     0x80570af2      ntoskrnl        NtQueryQuotaInformationFile
167     0x805adbca      ntoskrnl        NtQuerySection
168     0x805b5a16      ntoskrnl        NtQuerySecurityObject
169     0x8060b30c      ntoskrnl        NtQuerySemaphore
170     0x805b981a      ntoskrnl        NtQuerySymbolicLinkObject
171     0x8060cb6c      ntoskrnl        NtQuerySystemEnvironmentValue
172     0x8060cb26      ntoskrnl        NtQuerySystemEnvironmentValueEx
172     0x8060cb26      ntoskrnl        NtSetSystemEnvironmentValueEx
173     0x80607b48      ntoskrnl        NtQuerySystemInformation
174     0x806099e4      ntoskrnl        NtQuerySystemTime
175     0x8060d268      ntoskrnl        NtQueryTimer
176     0x8060929c      ntoskrnl        NtQueryTimerResolution
177     0x806184be      ntoskrnl        NtQueryValueKey
178     0x805ae250      ntoskrnl        NtQueryVirtualMemory
179     0x80570fe2      ntoskrnl        NtQueryVolumeInformationFile
180     0x805c7466      ntoskrnl        NtQueueApcThread
181     0x80540e48      ntoskrnl        NtRaiseException
182     0x8060af7e      ntoskrnl        NtRaiseHardError
183     0x805717aa      ntoskrnl        NtReadFile
184     0x80571d38      ntoskrnl        NtReadFileScatter
185     0x8059b184      ntoskrnl        NtReadRequestData
186     0x805a9712      ntoskrnl        NtReadVirtualMemory
187     0x805c89e0      ntoskrnl        NtRegisterThreadTerminatePort
188     0x8060da76      ntoskrnl        NtReleaseMutant
189     0x8060b43c      ntoskrnl        NtReleaseSemaphore
190     0x8056e0d2      ntoskrnl        NtRemoveIoCompletion
191     0x80639b56      ntoskrnl        NtRemoveProcessDebug
192     0x80619ca8      ntoskrnl        NtRenameKey
193     0x8061c332      ntoskrnl        NtReplaceKey
194     0x8059a804      ntoskrnl        NtReplyPort
195     0x8059b7cc      ntoskrnl        NtReplyWaitReceivePort
196     0x8059b1d4      ntoskrnl        NtReplyWaitReceivePortEx
197     0x8059aaee      ntoskrnl        NtReplyWaitReplyPort
198     0x805be456      ntoskrnl        NtRequestDeviceWakeup
199     0x80597d62      ntoskrnl        NtRequestPort
200     0x8059808e      ntoskrnl        NtRequestWaitReplyPort
201     0x805be264      ntoskrnl        NtRequestWakeupLatency
202     0x806054b6      ntoskrnl        NtResetEvent
203     0x8051de82      ntoskrnl        NtResetWriteWatch
204     0x8061bc3e      ntoskrnl        NtRestoreKey
205     0x805cad40      ntoskrnl        NtResumeProcess
206     0x805cac22      ntoskrnl        NtResumeThread
207     0x8061bd3a      ntoskrnl        NtSaveKey
208     0x8061be20      ntoskrnl        NtSaveKeyEx
209     0x8061bf48      ntoskrnl        NtSaveMergedKeys
210     0x8059907c      ntoskrnl        NtSecureConnectPort
211     0x8060cb50      ntoskrnl        NtAddBootEntry
211     0x8060cb50      ntoskrnl        NtEnumerateBootEntries
211     0x8060cb50      ntoskrnl        NtQueryBootEntryOrder
211     0x8060cb50      ntoskrnl        NtQueryBootOptions
211     0x8060cb50      ntoskrnl        NtSetBootEntryOrder
211     0x8060cb50      ntoskrnl        NtSetBootOptions
212     0x8060cb50      ntoskrnl        NtAddBootEntry
212     0x8060cb50      ntoskrnl        NtEnumerateBootEntries
212     0x8060cb50      ntoskrnl        NtQueryBootEntryOrder
212     0x8060cb50      ntoskrnl        NtQueryBootOptions
212     0x8060cb50      ntoskrnl        NtSetBootEntryOrder
212     0x8060cb50      ntoskrnl        NtSetBootOptions
213     0x805c792a      ntoskrnl        NtSetContextThread
214     0x8063c80e      ntoskrnl        NtSetDebugFilterState
215     0x8060ae28      ntoskrnl        NtSetDefaultHardErrorPort
216     0x80606fb8      ntoskrnl        NtSetDefaultLocale
217     0x8060782a      ntoskrnl        NtSetDefaultUILanguage
218     0x8056f8e6      ntoskrnl        NtSetEaFile
219     0x80605576      ntoskrnl        NtSetEvent
220     0x80605640      ntoskrnl        NtSetEventBoostPriority
221     0x8060d75a      ntoskrnl        NtSetHighEventPair
222     0x8060d68a      ntoskrnl        NtSetHighWaitLowEventPair
223     0x80639520      ntoskrnl        NtSetInformationDebugObject
224     0x80570284      ntoskrnl        NtSetInformationFile
225     0x805ccbf0      ntoskrnl        NtSetInformationJobObject
226     0x80618fa0      ntoskrnl        NtSetInformationKey
227     0x805ba490      ntoskrnl        NtSetInformationObject
228     0x805c3d54      ntoskrnl        NtSetInformationProcess
229     0x805c1d14      ntoskrnl        NtSetInformationThread
230     0x805f014a      ntoskrnl        NtSetInformationToken
231     0x8060dbc2      ntoskrnl        NtSetIntervalProfile
232     0x8056e070      ntoskrnl        NtSetIoCompletion
233     0x805c9b6c      ntoskrnl        NtSetLdtEntries
234     0x8060d6f6      ntoskrnl        NtSetLowEventPair
235     0x8060d61e      ntoskrnl        NtSetLowWaitHighEventPair
236     0x80570ad0      ntoskrnl        NtSetQuotaInformationFile
237     0x805b5fc0      ntoskrnl        NtSetSecurityObject
238     0x8060cdf0      ntoskrnl        NtSetSystemEnvironmentValue
239     0x8060cb26      ntoskrnl        NtQuerySystemEnvironmentValueEx
239     0x8060cb26      ntoskrnl        NtSetSystemEnvironmentValueEx
240     0x80605e76      ntoskrnl        NtSetSystemInformation
241     0x80648dd6      ntoskrnl        NtSetSystemPowerState
242     0x8060a5a4      ntoskrnl        NtSetSystemTime
243     0x805be178      ntoskrnl        NtSetThreadExecutionState
244     0x8053514a      ntoskrnl        NtSetTimer
245     0x80609a76      ntoskrnl        NtSetTimerResolution
246     0x8060b8f2      ntoskrnl        NtSetUuidSeed
247     0x8061880c      ntoskrnl        NtSetValueKey
248     0x80571406      ntoskrnl        NtSetVolumeInformationFile
249     0x80609092      ntoskrnl        NtShutdownSystem
250     0x80522c50      ntoskrnl        NtSignalAndWaitForSingleObject
251     0x8060de0c      ntoskrnl        NtStartProfile
252     0x8060dfb6      ntoskrnl        NtStopProfile
253     0x805cacea      ntoskrnl        NtSuspendProcess
254     0x805cab5c      ntoskrnl        NtSuspendThread
255     0x8060e1da      ntoskrnl        NtSystemDebugControl
256     0x805cd75a      ntoskrnl        NtTerminateJobObject
257     0x805c8c2a      ntoskrnl        NtTerminateProcess
258     0x805c8e24      ntoskrnl        NtTerminateThread
259     0x805caeaa      ntoskrnl        NtTestAlert
260     0x80531828      ntoskrnl        NtTraceEvent
261     0x8060cb5e      ntoskrnl        NtTranslateFilePath
262     0x8057971c      ntoskrnl        NtUnloadDriver
263     0x80618b36      ntoskrnl        NtUnloadKey
264     0x80618d50      ntoskrnl        NtUnloadKeyEx
265     0x8056e856      ntoskrnl        NtUnlockFile
266     0x805ac4ce      ntoskrnl        NtUnlockVirtualMemory
267     0x805a8296      ntoskrnl        NtUnmapViewOfSection
268     0x805f1502      ntoskrnl        NtVdmControl
269     0x80639288      ntoskrnl        NtWaitForDebugEvent
270     0x805b6176      ntoskrnl        NtWaitForMultipleObjects
271     0x805b608c      ntoskrnl        NtWaitForSingleObject
272     0x8060d5ba      ntoskrnl        NtWaitHighEventPair
273     0x8060d556      ntoskrnl        NtWaitLowEventPair
274     0x80572248      ntoskrnl        NtWriteFile
275     0x80572858      ntoskrnl        NtWriteFileGather
276     0x8059b1ac      ntoskrnl        NtWriteRequestData
277     0x805a981c      ntoskrnl        NtWriteVirtualMemory
278     0x8050222c      ntoskrnl        NtYieldExecution
279     0x8060e632      ntoskrnl        NtCreateKeyedEvent
280     0x8060e71c      ntoskrnl        NtOpenKeyedEvent
281     0x8060e7ce      ntoskrnl        NtReleaseKeyedEvent
282     0x8060ea5a      ntoskrnl        NtWaitForKeyedEvent
283     0x805c1798      ntoskrnl        NtQueryPortInformationProcess

thmanalyst@ubuntu:/opt/volatility3$ python3 vol.py -f dump.vmem windows.modules
Volatility 3 Framework 1.0.1
Progress:  100.00               PDB scanning finished                     
Offset  Base    Size    Name    Path    File output

0x823fc3b0      0x804d7000      0x1f8580        ntoskrnl.exe    \WINDOWS\system32\ntkrnlpa.exe Disabled
0x823fc348      0x806d0000      0x20300 hal.dll \WINDOWS\system32\hal.dll       Disabled
0x823fc2e0      0xf8b9a000      0x2000  kdcom.dll       \WINDOWS\system32\KDCOM.DLL   Disabled
0x823fc270      0xf8aaa000      0x3000  BOOTVID.dll     \WINDOWS\system32\BOOTVID.dll Disabled
0x823fc208      0xf856b000      0x2e000 ACPI.sys        ACPI.sys        Disabled
0x823fc198      0xf8b9c000      0x2000  WMILIB.SYS      \WINDOWS\system32\DRIVERS\WMILIB.SYS   Disabled
0x823fc130      0xf855a000      0x11000 pci.sys pci.sys Disabled
0x823fc0c0      0xf869a000      0xa000  isapnp.sys      isapnp.sys      Disabled
0x823fc050      0xf8aae000      0x3000  compbatt.sys    compbatt.sys    Disabled
0x823ed008      0xf8ab2000      0x4000  BATTC.SYS       \WINDOWS\system32\DRIVERS\BATTC.SYS    Disabled
0x823edf98      0xf8b9e000      0x2000  intelide.sys    intelide.sys    Disabled
0x823edf28      0xf891a000      0x7000  PCIIDEX.SYS     \WINDOWS\system32\DRIVERS\PCIIDEX.SYS  Disabled
0x823edeb8      0xf86aa000      0xb000  MountMgr.sys    MountMgr.sys    Disabled
0x823ede48      0xf853b000      0x1f000 ftdisk.sys      ftdisk.sys      Disabled
0x823eddd8      0xf8ba0000      0x2000  dmload.sys      dmload.sys      Disabled
0x823edd70      0xf8515000      0x26000 dmio.sys        dmio.sys        Disabled
0x823edd00      0xf8922000      0x5000  PartMgr.sys     PartMgr.sys     Disabled
0x823edc90      0xf86ba000      0xd000  VolSnap.sys     VolSnap.sys     Disabled
0x823edc28      0xf84fd000      0x18000 atapi.sys       atapi.sys       Disabled
0x823edbc0      0xf86ca000      0x9000  disk.sys        disk.sys        Disabled
0x823edb50      0xf86da000      0xd000  CLASSPNP.SYS    \WINDOWS\system32\DRIVERS\CLASSPNP.SYS Disabled
0x823edae0      0xf84dd000      0x20000 fltMgr.sys      fltMgr.sys      Disabled
0x823eda78      0xf84cb000      0x12000 sr.sys  sr.sys  Disabled
0x823eda08      0xf84b4000      0x17000 KSecDD.sys      KSecDD.sys      Disabled
0x823ed9a0      0xf8427000      0x8d000 Ntfs.sys        Ntfs.sys        Disabled
0x823ed938      0xf83fa000      0x2d000 NDIS.sys        NDIS.sys        Disabled
0x823ed8d0      0xf83e0000      0x1a000 Mup.sys Mup.sys Disabled
0x823ed860      0xf86ea000      0xb000  agp440.sys      agp440.sys      Disabled
0x82147bf8      0xf874a000      0xd000  i8042prt.sys    \SystemRoot\system32\DRIVERS\i8042prt.sys      Disabled
0x81ea11d8      0xf8942000      0x6000  kbdclass.sys    \SystemRoot\system32\DRIVERS\kbdclass.sys      Disabled
0x82234b48      0xf894a000      0x6000  mouclass.sys    \SystemRoot\system32\DRIVERS\mouclass.sys      Disabled
0x820c1b20      0xf8373000      0x14000 parport.sys     \SystemRoot\system32\DRIVERS\parport.sys       Disabled
0x81e85b10      0xf875a000      0x10000 serial.sys      \SystemRoot\system32\DRIVERS\serial.sys        Disabled
0x82217790      0xf8b3a000      0x4000  serenum.sys     \SystemRoot\system32\DRIVERS\serenum.sys       Disabled
0x82234f00      0xf8952000      0x7000  fdc.sys \SystemRoot\system32\DRIVERS\fdc.sys  Disabled
0x82262988      0xf876a000      0x10000 cdrom.sys       \SystemRoot\system32\DRIVERS\cdrom.sys Disabled
0x81e858d8      0xf877a000      0xf000  redbook.sys     \SystemRoot\system32\DRIVERS\redbook.sys       Disabled
0x82262720      0xf8350000      0x23000 ks.sys  \SystemRoot\system32\DRIVERS\ks.sys   Disabled
0x821455d8      0xf895a000      0x6000  usbuhci.sys     \SystemRoot\system32\DRIVERS\usbuhci.sys       Disabled
0x82236778      0xf832c000      0x24000 USBPORT.SYS     \SystemRoot\system32\DRIVERS\USBPORT.SYS       Disabled
0x822363a8      0xf878a000      0x9000  pcntpci5.sys    \SystemRoot\system32\DRIVERS\pcntpci5.sys      Disabled
0x822362c8      0xf879a000      0xa000  es1371mp.sys    \SystemRoot\system32\drivers\es1371mp.sys      Disabled
0x82235d00      0xf8308000      0x24000 portcls.sys     \SystemRoot\system32\drivers\portcls.sys       Disabled
0x82216ce8      0xf87aa000      0xf000  drmk.sys        \SystemRoot\system32\drivers\drmk.sys  Disabled
0x82234f98      0xf8962000      0x8000  usbehci.sys     \SystemRoot\system32\DRIVERS\usbehci.sys       Disabled
0x82234cf0      0xf8b42000      0x4000  CmBatt.sys      \SystemRoot\system32\DRIVERS\CmBatt.sys        Disabled
0x82234ad8      0xf87ba000      0x9000  intelppm.sys    \SystemRoot\system32\DRIVERS\intelppm.sys      Disabled
0x822349c0      0xf8cd2000      0x1000  audstub.sys     \SystemRoot\system32\DRIVERS\audstub.sys       Disabled
0x82233170      0xf87ca000      0xd000  rasl2tp.sys     \SystemRoot\system32\DRIVERS\rasl2tp.sys       Disabled
0x81e2fe80      0xf8b46000      0x3000  ndistapi.sys    \SystemRoot\system32\DRIVERS\ndistapi.sys      Disabled
0x822fe8c8      0xf82f1000      0x17000 ndiswan.sys     \SystemRoot\system32\DRIVERS\ndiswan.sys       Disabled
0x822fecf0      0xf87da000      0xb000  raspppoe.sys    \SystemRoot\system32\DRIVERS\raspppoe.sys      Disabled
0x82138420      0xf87ea000      0xc000  raspptp.sys     \SystemRoot\system32\DRIVERS\raspptp.sys       Disabled
0x82308cd0      0xf896a000      0x5000  TDI.SYS \SystemRoot\system32\DRIVERS\TDI.SYS  Disabled
0x82339c60      0xf82e0000      0x11000 psched.sys      \SystemRoot\system32\DRIVERS\psched.sys        Disabled
0x82261578      0xf87fa000      0x9000  msgpc.sys       \SystemRoot\system32\DRIVERS\msgpc.sys Disabled
0x82259258      0xf8972000      0x5000  ptilink.sys     \SystemRoot\system32\DRIVERS\ptilink.sys       Disabled
0x81ea6520      0xf897a000      0x5000  raspti.sys      \SystemRoot\system32\DRIVERS\raspti.sys        Disabled
0x821c1320      0xf8288000      0x30000 rdpdr.sys       \SystemRoot\system32\DRIVERS\rdpdr.sys Disabled
0x8207c0a8      0xf880a000      0xa000  termdd.sys      \SystemRoot\system32\DRIVERS\termdd.sys        Disabled
0x81ea6d78      0xf8ba2000      0x2000  swenum.sys      \SystemRoot\system32\DRIVERS\swenum.sys        Disabled
0x822030e8      0xf818a000      0x5e000 update.sys      \SystemRoot\system32\DRIVERS\update.sys        Disabled
0x8213dce8      0xf8b5e000      0x4000  mssmbios.sys    \SystemRoot\system32\DRIVERS\mssmbios.sys      Disabled
0x82260190      0xf881a000      0xa000  NDProxy.SYS     \SystemRoot\System32\Drivers\NDProxy.SYS       Disabled
0x81e78108      0xf8982000      0x5000  flpydisk.sys    \SystemRoot\system32\DRIVERS\flpydisk.sys      Disabled
0x822ee108      0xf883a000      0xf000  usbhub.sys      \SystemRoot\system32\DRIVERS\usbhub.sys        Disabled
0x821b9440      0xf8ba4000      0x2000  USBD.SYS        \SystemRoot\system32\DRIVERS\USBD.SYS  Disabled
0x821ea108      0xf8b86000      0x3000  gameenum.sys    \SystemRoot\system32\DRIVERS\gameenum.sys      Disabled
0x821b5e20      0xf8ba6000      0x2000  Fs_Rec.SYS      \SystemRoot\System32\Drivers\Fs_Rec.SYS        Disabled
0x82271b20      0xf8d05000      0x1000  Null.SYS        \SystemRoot\System32\Drivers\Null.SYS  Disabled
0x82271528      0xf8ba8000      0x2000  Beep.SYS        \SystemRoot\System32\Drivers\Beep.SYS  Disabled
0x82271308      0xf8992000      0x6000  vga.sys \SystemRoot\System32\drivers\vga.sys  Disabled
0x821f2e78      0xf814e000      0x14000 VIDEOPRT.SYS    \SystemRoot\System32\drivers\VIDEOPRT.SYS      Disabled
0x82271078      0xf8baa000      0x2000  mnmdd.SYS       \SystemRoot\System32\Drivers\mnmdd.SYS Disabled
0x82258e58      0xf8bac000      0x2000  RDPCDD.sys      \SystemRoot\System32\DRIVERS\RDPCDD.sys        Disabled
0x82314cc8      0xf899a000      0x5000  Msfs.SYS        \SystemRoot\System32\Drivers\Msfs.SYS  Disabled
0x82314880      0xf89a2000      0x8000  Npfs.SYS        \SystemRoot\System32\Drivers\Npfs.SYS  Disabled
0x821498c0      0xf8b96000      0x3000  rasacd.sys      \SystemRoot\system32\DRIVERS\rasacd.sys        Disabled
0x82314678      0xf811b000      0x13000 ipsec.sys       \SystemRoot\system32\DRIVERS\ipsec.sys Disabled
0x823142d8      0xf80c2000      0x59000 tcpip.sys       \SystemRoot\system32\DRIVERS\tcpip.sys Disabled
0x82314108      0xf809a000      0x28000 netbt.sys       \SystemRoot\system32\DRIVERS\netbt.sys Disabled
0x821d4be8      0xf8078000      0x22000 afd.sys \SystemRoot\System32\drivers\afd.sys  Disabled
0x823cb1d8      0xf884a000      0x9000  netbios.sys     \SystemRoot\system32\DRIVERS\netbios.sys       Disabled
0x821d4668      0xf804d000      0x2b000 rdbss.sys       \SystemRoot\system32\DRIVERS\rdbss.sys Disabled
0x82225d50      0xf7fdd000      0x70000 mrxsmb.sys      \SystemRoot\system32\DRIVERS\mrxsmb.sys        Disabled
0x821d4498      0xf886a000      0xb000  Fips.SYS        \SystemRoot\System32\Drivers\Fips.SYS  Disabled
0x823088f0      0xf7f8f000      0x26000 ipnat.sys       \SystemRoot\system32\DRIVERS\ipnat.sys Disabled
0x8205f2f8      0xf888a000      0x9000  wanarp.sys      \SystemRoot\system32\DRIVERS\wanarp.sys        Disabled
0x822095b8      0xf889a000      0x10000 Cdfs.SYS        \SystemRoot\System32\Drivers\Cdfs.SYS  Disabled
0x82291110      0xf89aa000      0x8000  usbccgp.sys     \SystemRoot\system32\DRIVERS\usbccgp.sys       Disabled
0x82250cc8      0xf82d4000      0x3000  hidusb.sys      \SystemRoot\system32\DRIVERS\hidusb.sys        Disabled
0x81e86090      0xf88aa000      0x9000  HIDCLASS.SYS    \SystemRoot\system32\DRIVERS\HIDCLASS.SYS      Disabled
0x81e350c8      0xf89b2000      0x7000  HIDPARSE.SYS    \SystemRoot\system32\DRIVERS\HIDPARSE.SYS      Disabled
0x82303488      0xf82d0000      0x3000  mouhid.sys      \SystemRoot\system32\DRIVERS\mouhid.sys        Disabled
0x8224e700      0xf7f77000      0x18000 dump_atapi.sys  \SystemRoot\System32\Drivers\dump_atapi.sys    Disabled
0x821488a8      0xf8bae000      0x2000  dump_WMILIB.SYS \SystemRoot\System32\Drivers\dump_WMILIB.SYS   Disabled
0x8224d280      0xbf800000      0x1c3000        win32k.sys      \SystemRoot\System32\win32k.sys        Disabled
0x820c21f8      0xf82c0000      0x3000  Dxapi.sys       \SystemRoot\System32\drivers\Dxapi.sys Disabled
0x82219e78      0xf89ba000      0x5000  watchdog.sys    \SystemRoot\System32\watchdog.sys      Disabled
0x822f31d8      0xbf9c3000      0x12000 dxg.sys \SystemRoot\System32\drivers\dxg.sys  Disabled
0x82066e80      0xf8d43000      0x1000  dxgthk.sys      \SystemRoot\System32\drivers\dxgthk.sys        Disabled
0x81e85008      0xbff50000      0x3000  framebuf.dll    \SystemRoot\System32\framebuf.dll      Disabled
0x81e296b8      0xf7c6f000      0x4000  ndisuio.sys     \SystemRoot\system32\DRIVERS\ndisuio.sys       Disabled
0x8227aa38      0xf792a000      0x15000 wdmaud.sys      \SystemRoot\system32\drivers\wdmaud.sys        Disabled
0x822d64a8      0xf7bdf000      0xf000  sysaudio.sys    \SystemRoot\system32\drivers\sysaudio.sys      Disabled
0x822937c0      0xf7887000      0x2d000 mrxdav.sys      \SystemRoot\system32\DRIVERS\mrxdav.sys        Disabled
0x82198138      0xf8be0000      0x2000  ParVdm.SYS      \SystemRoot\System32\Drivers\ParVdm.SYS        Disabled
0x82259430      0xf780d000      0x52000 srv.sys \SystemRoot\system32\DRIVERS\srv.sys  Disabled
0x821c5120      0xf75c4000      0x41000 HTTP.sys        \SystemRoot\System32\Drivers\HTTP.sys  Disabled

thmanalyst@ubuntu:/opt/volatility3$ python3 vol.py -f dump.vmem windows.driverscan
Volatility 3 Framework 1.0.1
Progress:  100.00               PDB scanning finished                     
Offset  Start   Size    Service Key     Driver Name     Name

thmanalyst@ubuntu:/opt/volatility3$ python3 vol.py -f dump.vmem windows.modscan
Volatility 3 Framework 1.0.1
Progress:  100.00               PDB scanning finished                     
Offset  Base    Size    Name    Path    File output

0x59ca40        0x89607b8d      0x89662c46                      Disabled
0x5a3890        0x6600000c      0x8d50a045                      Disabled
0x5a3e06        0x400   0x66000010                      Disabled
0x20296b8       0xf7c6f000      0x4000  ndisuio.sys     \SystemRoot\system32\DRIVERS\ndisuio.sys       Disabled
0x202fe80       0xf8b46000      0x3000  ndistapi.sys    \SystemRoot\system32\DRIVERS\ndistapi.sys      Disabled
0x20350c8       0xf89b2000      0x7000  HIDPARSE.SYS    \SystemRoot\system32\DRIVERS\HIDPARSE.SYS      Disabled
0x2078108       0xf8982000      0x5000  flpydisk.sys    \SystemRoot\system32\DRIVERS\flpydisk.sys      Disabled
0x2085008       0xbff50000      0x3000  framebuf.dll    \SystemRoot\System32\framebuf.dll      Disabled
0x20858d8       0xf877a000      0xf000  redbook.sys     \SystemRoot\system32\DRIVERS\redbook.sys       Disabled
0x2085b10       0xf875a000      0x10000 serial.sys      \SystemRoot\system32\DRIVERS\serial.sys        Disabled
0x2086090       0xf88aa000      0x9000  HIDCLASS.SYS    \SystemRoot\system32\DRIVERS\HIDCLASS.SYS      Disabled
0x20a11d8       0xf8942000      0x6000  kbdclass.sys    \SystemRoot\system32\DRIVERS\kbdclass.sys      Disabled
0x20a6520       0xf897a000      0x5000  raspti.sys      \SystemRoot\system32\DRIVERS\raspti.sys        Disabled
0x20a6d78       0xf8ba2000      0x2000  swenum.sys      \SystemRoot\system32\DRIVERS\swenum.sys        Disabled
0x225f2f8       0xf888a000      0x9000  wanarp.sys      \SystemRoot\system32\DRIVERS\wanarp.sys        Disabled
0x2266e80       0xf8d43000      0x1000  dxgthk.sys      \SystemRoot\System32\drivers\dxgthk.sys        Disabled
0x227c0a8       0xf880a000      0xa000  termdd.sys      \SystemRoot\system32\DRIVERS\termdd.sys        Disabled
0x22c1b20       0xf8373000      0x14000 parport.sys     \SystemRoot\system32\DRIVERS\parport.sys       Disabled
0x22c21f8       0xf82c0000      0x3000  Dxapi.sys       \SystemRoot\System32\drivers\Dxapi.sys Disabled
0x2338420       0xf87ea000      0xc000  raspptp.sys     \SystemRoot\system32\DRIVERS\raspptp.sys       Disabled
0x233dce8       0xf8b5e000      0x4000  mssmbios.sys    \SystemRoot\system32\DRIVERS\mssmbios.sys      Disabled
0x23455d8       0xf895a000      0x6000  usbuhci.sys     \SystemRoot\system32\DRIVERS\usbuhci.sys       Disabled
0x2347bf8       0xf874a000      0xd000  i8042prt.sys    \SystemRoot\system32\DRIVERS\i8042prt.sys      Disabled
0x23488a8       0xf8bae000      0x2000  dump_WMILIB.SYS \SystemRoot\System32\Drivers\dump_WMILIB.SYS   Disabled
0x23498c0       0xf8b96000      0x3000  rasacd.sys      \SystemRoot\system32\DRIVERS\rasacd.sys        Disabled
0x2398138       0xf8be0000      0x2000  ParVdm.SYS      \SystemRoot\System32\Drivers\ParVdm.SYS        Disabled
0x23b5e20       0xf8ba6000      0x2000  Fs_Rec.SYS      \SystemRoot\System32\Drivers\Fs_Rec.SYS        Disabled
0x23b9440       0xf8ba4000      0x2000  USBD.SYS        \SystemRoot\system32\DRIVERS\USBD.SYS  Disabled
0x23c1320       0xf8288000      0x30000 rdpdr.sys       \SystemRoot\system32\DRIVERS\rdpdr.sys Disabled
0x23c5120       0xf75c4000      0x41000 HTTP.sys        \SystemRoot\System32\Drivers\HTTP.sys  Disabled
0x23d4498       0xf886a000      0xb000  Fips.SYS        \SystemRoot\System32\Drivers\Fips.SYS  Disabled
0x23d4668       0xf804d000      0x2b000 rdbss.sys       \SystemRoot\system32\DRIVERS\rdbss.sys Disabled
0x23d4be8       0xf8078000      0x22000 afd.sys \SystemRoot\System32\drivers\afd.sys  Disabled
0x23ea108       0xf8b86000      0x3000  gameenum.sys    \SystemRoot\system32\DRIVERS\gameenum.sys      Disabled
0x23f2e78       0xf814e000      0x14000 VIDEOPRT.SYS    \SystemRoot\System32\drivers\VIDEOPRT.SYS      Disabled
0x24030e8       0xf818a000      0x5e000 update.sys      \SystemRoot\system32\DRIVERS\update.sys        Disabled
0x24095b8       0xf889a000      0x10000 Cdfs.SYS        \SystemRoot\System32\Drivers\Cdfs.SYS  Disabled
0x2416ce8       0xf87aa000      0xf000  drmk.sys        \SystemRoot\system32\drivers\drmk.sys  Disabled
0x2417790       0xf8b3a000      0x4000  serenum.sys     \SystemRoot\system32\DRIVERS\serenum.sys       Disabled
0x2419e78       0xf89ba000      0x5000  watchdog.sys    \SystemRoot\System32\watchdog.sys      Disabled
0x2425d50       0xf7fdd000      0x70000 mrxsmb.sys      \SystemRoot\system32\DRIVERS\mrxsmb.sys        Disabled
0x2433170       0xf87ca000      0xd000  rasl2tp.sys     \SystemRoot\system32\DRIVERS\rasl2tp.sys       Disabled
0x24349c0       0xf8cd2000      0x1000  audstub.sys     \SystemRoot\system32\DRIVERS\audstub.sys       Disabled
0x2434ad8       0xf87ba000      0x9000  intelppm.sys    \SystemRoot\system32\DRIVERS\intelppm.sys      Disabled
0x2434b48       0xf894a000      0x6000  mouclass.sys    \SystemRoot\system32\DRIVERS\mouclass.sys      Disabled
0x2434cf0       0xf8b42000      0x4000  CmBatt.sys      \SystemRoot\system32\DRIVERS\CmBatt.sys        Disabled
0x2434f00       0xf8952000      0x7000  fdc.sys \SystemRoot\system32\DRIVERS\fdc.sys  Disabled
0x2434f98       0xf8962000      0x8000  usbehci.sys     \SystemRoot\system32\DRIVERS\usbehci.sys       Disabled
0x2435d00       0xf8308000      0x24000 portcls.sys     \SystemRoot\system32\drivers\portcls.sys       Disabled
0x24362c8       0xf879a000      0xa000  es1371mp.sys    \SystemRoot\system32\drivers\es1371mp.sys      Disabled
0x24363a8       0xf878a000      0x9000  pcntpci5.sys    \SystemRoot\system32\DRIVERS\pcntpci5.sys      Disabled
0x2436778       0xf832c000      0x24000 USBPORT.SYS     \SystemRoot\system32\DRIVERS\USBPORT.SYS       Disabled
0x244d280       0xbf800000      0x1c3000        win32k.sys      \SystemRoot\System32\win32k.sys        Disabled
0x244e700       0xf7f77000      0x18000 dump_atapi.sys  \SystemRoot\System32\Drivers\dump_atapi.sys    Disabled
0x2450cc8       0xf82d4000      0x3000  hidusb.sys      \SystemRoot\system32\DRIVERS\hidusb.sys        Disabled
0x2458e58       0xf8bac000      0x2000  RDPCDD.sys      \SystemRoot\System32\DRIVERS\RDPCDD.sys        Disabled
0x2459258       0xf8972000      0x5000  ptilink.sys     \SystemRoot\system32\DRIVERS\ptilink.sys       Disabled
0x2459430       0xf780d000      0x52000 srv.sys \SystemRoot\system32\DRIVERS\srv.sys  Disabled
0x2460190       0xf881a000      0xa000  NDProxy.SYS     \SystemRoot\System32\Drivers\NDProxy.SYS       Disabled
0x2461578       0xf87fa000      0x9000  msgpc.sys       \SystemRoot\system32\DRIVERS\msgpc.sys Disabled
0x2462720       0xf8350000      0x23000 ks.sys  \SystemRoot\system32\DRIVERS\ks.sys   Disabled
0x2462988       0xf876a000      0x10000 cdrom.sys       \SystemRoot\system32\DRIVERS\cdrom.sys Disabled
0x2471078       0xf8baa000      0x2000  mnmdd.SYS       \SystemRoot\System32\Drivers\mnmdd.SYS Disabled
0x2471308       0xf8992000      0x6000  vga.sys \SystemRoot\System32\drivers\vga.sys  Disabled
0x2471528       0xf8ba8000      0x2000  Beep.SYS        \SystemRoot\System32\Drivers\Beep.SYS  Disabled
0x2471b20       0xf8d05000      0x1000  Null.SYS        \SystemRoot\System32\Drivers\Null.SYS  Disabled
0x247aa38       0xf792a000      0x15000 wdmaud.sys      \SystemRoot\system32\drivers\wdmaud.sys        Disabled
