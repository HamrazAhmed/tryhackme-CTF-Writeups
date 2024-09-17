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
