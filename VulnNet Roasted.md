---
VulnNet Entertainment quickly deployed another management instance on their very broad network...
---

# VulnNet Roasted — Writeup

## Overview
### VulnNet Roasted — Writeup
### VulnNet Roasted — Writeup
### VulnNet: Roasted
Start Machine
VulnNet Entertainment just deployed a new instance on their network with the newly-hired system administrators. Being a security-aware company, they as always hired you to perform a penetration test, and see how system administrators are performing.
-   Difficulty: Easy
-   Operating System: Windows
This is a much simpler machine, do not overthink. You can do it by following common methodologies.
Note: It _might_ take up to 6 minutes for this machine to fully boot.
Icon made by [DinosoftLabs](https://www.flaticon.com/authors/dinosoftlabs) from [www.flaticon.com](https://www.flaticon.com/)
Answer the questions below

## Enumeration
```text
┌──(kali㉿kali)-[~]
└─$ rustscan -a 10.10.60.167 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
🌍HACK THE PLANET🌍

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.60.167:53
Open 10.10.60.167:88
Open 10.10.60.167:135
Open 10.10.60.167:139
Open 10.10.60.167:389
Open 10.10.60.167:445
Open 10.10.60.167:464
Open 10.10.60.167:593
Open 10.10.60.167:636
Open 10.10.60.167:3269
Open 10.10.60.167:3268
Open 10.10.60.167:5985
Open 10.10.60.167:9389
Open 10.10.60.167:49665
Open 10.10.60.167:49669
Open 10.10.60.167:49670
Open 10.10.60.167:49672
Open 10.10.60.167:49703
Open 10.10.60.167:49790
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-29 22:24 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 22:24
Completed NSE at 22:24, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 22:24
Completed NSE at 22:24, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 22:24
Completed NSE at 22:24, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 22:24
Completed Parallel DNS resolution of 1 host. at 22:24, 0.01s elapsed
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 22:24
Scanning 10.10.60.167 [19 ports]
Discovered open port 139/tcp on 10.10.60.167
Discovered open port 135/tcp on 10.10.60.167
Discovered open port 53/tcp on 10.10.60.167
Discovered open port 445/tcp on 10.10.60.167
Discovered open port 389/tcp on 10.10.60.167
Discovered open port 88/tcp on 10.10.60.167
Discovered open port 3269/tcp on 10.10.60.167
Discovered open port 49669/tcp on 10.10.60.167
Discovered open port 9389/tcp on 10.10.60.167
Discovered open port 49790/tcp on 10.10.60.167
Discovered open port 464/tcp on 10.10.60.167
Discovered open port 49670/tcp on 10.10.60.167
Discovered open port 636/tcp on 10.10.60.167
Discovered open port 49665/tcp on 10.10.60.167
Discovered open port 49672/tcp on 10.10.60.167
Discovered open port 49703/tcp on 10.10.60.167
Discovered open port 5985/tcp on 10.10.60.167
Discovered open port 593/tcp on 10.10.60.167
Discovered open port 3268/tcp on 10.10.60.167
Completed Connect Scan at 22:24, 0.50s elapsed (19 total ports)
Initiating Service scan at 22:24
Scanning 19 services on 10.10.60.167
Completed Service scan at 22:25, 57.96s elapsed (19 services on 1 host)
NSE: Script scanning 10.10.60.167.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 22:25
NSE Timing: About 99.96% done; ETC: 22:26 (0:00:00 remaining)
Completed NSE at 22:26, 40.09s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 22:26
Completed NSE at 22:26, 14.45s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 22:26
Completed NSE at 22:26, 0.00s elapsed
Nmap scan report for 10.10.60.167
Host is up, received user-set (0.25s latency).
Scanned at 2022-12-29 22:24:51 EST for 113s

PORT      STATE SERVICE       REASON  VERSION
53/tcp    open  domain        syn-ack Simple DNS Plus
88/tcp    open  kerberos-sec  syn-ack Microsoft Windows Kerberos (server time: 2022-12-30 03:24:59Z)
135/tcp   open  msrpc         syn-ack Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack Microsoft Windows netbios-ssn
389/tcp   open  ldap          syn-ack Microsoft Windows Active Directory LDAP (Domain: vulnnet-rst.local0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds? syn-ack
464/tcp   open  kpasswd5?     syn-ack
593/tcp   open  ncacn_http    syn-ack Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped    syn-ack
3268/tcp  open  ldap          syn-ack Microsoft Windows Active Directory LDAP (Domain: vulnnet-rst.local0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped    syn-ack
5985/tcp  open  http          syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
9389/tcp  open  mc-nmf        syn-ack .NET Message Framing
49665/tcp open  msrpc         syn-ack Microsoft Windows RPC
49669/tcp open  ncacn_http    syn-ack Microsoft Windows RPC over HTTP 1.0
49670/tcp open  msrpc         syn-ack Microsoft Windows RPC
49672/tcp open  msrpc         syn-ack Microsoft Windows RPC
49703/tcp open  msrpc         syn-ack Microsoft Windows RPC
49790/tcp open  msrpc         syn-ack Microsoft Windows RPC
Service Info: Host: WIN-2BO8M1OE1M1; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 32166/tcp): CLEAN (Timeout)
|   Check 2 (port 50927/tcp): CLEAN (Timeout)
|   Check 3 (port 22994/udp): CLEAN (Timeout)
|   Check 4 (port 9159/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
|_clock-skew: 0s
| smb2-time: 
|   date: 2022-12-30T03:25:53
|_  start_date: N/A
| smb2-security-mode: 
|   311: 
|_    Message signing enabled and required

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 22:26
Completed NSE at 22:26, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 22:26
Completed NSE at 22:26, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 22:26
Completed NSE at 22:26, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 114.17 seconds

Domain: vulnnet-rst.local

Starting with the Samba shares, we can use smbclient to list the network shares
```
```text
┌──(kali㉿kali)-[~]
└─$ smbclient -N -L 10.10.60.167

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share 
        SYSVOL          Disk      Logon server share 
        VulnNet-Business-Anonymous Disk      VulnNet Business Sharing
        VulnNet-Enterprise-Anonymous Disk      VulnNet Enterprise Sharing
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.60.167 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available

smbmap will also reveal the permissions
```
```text
┌──(kali㉿kali)-[~]
└─$ smbmap -u anonymous -H 10.10.60.167 
[+] Guest session       IP: 10.10.60.167:445    Name: 10.10.60.167                                      
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        IPC$                                                    READ ONLY       Remote IPC
        NETLOGON                                                NO ACCESS       Logon server share 
        SYSVOL                                                  NO ACCESS       Logon server share 
        VulnNet-Business-Anonymous                              READ ONLY       VulnNet Business Sharing
        VulnNet-Enterprise-Anonymous                            READ ONLY       VulnNet Enterprise Sharing

getting files
```
```text
┌──(kali㉿kali)-[~/VulnNet]
└─$ smbclient -N \\\\10.10.60.167\\VulnNet-Business-Anonymous
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Fri Mar 12 21:46:40 2021
  ..                                  D        0  Fri Mar 12 21:46:40 2021
  Business-Manager.txt                A      758  Thu Mar 11 20:24:34 2021
  Business-Sections.txt               A      654  Thu Mar 11 20:24:34 2021
  Business-Tracking.txt               A      471  Thu Mar 11 20:24:34 2021

                8771839 blocks of size 4096. 4554468 blocks available
smb: \> get Business-Manager.txt 
getting file \Business-Manager.txt of size 758 as Business-Manager.txt (0.2 KiloBytes/sec) (average 0.2 KiloBytes/sec)
smb: \> get Business-Sections.txt 
getting file \Business-Sections.txt of size 654 as Business-Sections.txt (0.3 KiloBytes/sec) (average 0.2 KiloBytes/sec)
smb: \> get Business-Tracking.txt 
getting file \Business-Tracking.txt of size 471 as Business-Tracking.txt (0.3 KiloBytes/sec) (average 0.2 KiloBytes/sec)
smb: \> quit
```
```text
┌──(kali㉿kali)-[~/VulnNet]
└─$ smbclient -N \\\\10.10.60.167\\VulnNet-Enterprise-Anonymous
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Fri Mar 12 21:46:40 2021
  ..                                  D        0  Fri Mar 12 21:46:40 2021
  Enterprise-Operations.txt           A      467  Thu Mar 11 20:24:34 2021
  Enterprise-Safety.txt               A      503  Thu Mar 11 20:24:34 2021
  Enterprise-Sync.txt                 A      496  Thu Mar 11 20:24:34 2021

                8771839 blocks of size 4096. 4554452 blocks available
smb: \> get Enterprise-Operations.txt 
getting file \Enterprise-Operations.txt of size 467 as Enterprise-Operations.txt (0.2 KiloBytes/sec) (average 0.2 KiloBytes/sec)
smb: \> get Enterprise-Safety.txt 
getting file \Enterprise-Safety.txt of size 503 as Enterprise-Safety.txt (0.3 KiloBytes/sec) (average 0.2 KiloBytes/sec)
smb: \> get Enterprise-Sync.txt 
getting file \Enterprise-Sync.txt of size 496 as Enterprise-Sync.txt (0.2 KiloBytes/sec) (average 0.2 KiloBytes/sec)
smb: \> quit
```
```text
┌──(kali㉿kali)-[~/VulnNet]
└─$ cat Business-Manager.txt 
VULNNET BUSINESS
~~~~~~~~~~~~~~~~~~~

Alexa Whitehat is our core business manager. All business-related offers, campaigns, and advertisements should be directed to her. 
We understand that when you’ve got questions, especially when you’re on a tight proposal deadline, you NEED answers. 
Our customer happiness specialists are at the ready, armed with friendly, helpful, timely support by email or online messaging.
We’re here to help, regardless of which you plan you’re on or if you’re just taking us for a test drive.
Our company looks forward to all of the business proposals, we will do our best to evaluate all of your offers properly. 
To contact our core business manager call this number: 1337 0000 7331

~VulnNet Entertainment
~TryHackMe
```
```text
┌──(kali㉿kali)-[~/VulnNet]
└─$ cat Business-Sections.txt 
VULNNET BUSINESS
~~~~~~~~~~~~~~~~~~~

Jack Goldenhand is the person you should reach to for any business unrelated proposals.
Managing proposals is a breeze with VulnNet. We save all your case studies, fees, images and team bios all in one central library.
Tag them, search them and drop them into your layout. Proposals just got... dare we say... fun?
No more emailing big PDFs, printing and shipping proposals or faxing back signatures (ugh).
Your client gets a branded, interactive proposal they can sign off electronically. No need for extra software or logins.
Oh, and we tell you as soon as your client opens it.

~VulnNet Entertainment
~TryHackMe
```
```text
┌──(kali㉿kali)-[~/VulnNet]
└─$ cat Business-Tracking.txt 
VULNNET TRACKING
~~~~~~~~~~~~~~~~~~

Keep a pulse on your sales pipeline of your agency. We let you know your close rate,
which sections of your proposals get viewed and for how long,
and all kinds of insight into what goes into your most successful proposals so you can sell smarter.
We keep track of all necessary activities and reach back to you with newly gathered data to discuss the outcome. 
You won't miss anything ever again. 

~VulnNet Entertainment
~TryHackMe
```
```text
┌──(kali㉿kali)-[~/VulnNet]
└─$ cat Enterprise-Operations.txt 
VULNNET OPERATIONS
~~~~~~~~~~~~~~~~~~~~

We bring predictability and consistency to your process. Making it repetitive doesn’t make it boring. 
Set the direction, define roles, and rely on automation to keep reps focused and make onboarding a breeze.
Don't wait for an opportunity to knock - build the door. Contact us right now.
VulnNet Entertainment is fully commited to growth, security and improvement.
Make a right decision!

~VulnNet Entertainment
~TryHackMe
```
```text
┌──(kali㉿kali)-[~/VulnNet]
└─$ cat Enterprise-Safety.txt    
VULNNET SAFETY
~~~~~~~~~~~~~~~~

Tony Skid is a core security manager and takes care of internal infrastructure.
We keep your data safe and private. When it comes to protecting your private information...
we’ve got it locked down tighter than Alcatraz. 
We partner with TryHackMe, use 128-bit SSL encryption, and create daily backups. 
And we never, EVER disclose any data to third-parties without your permission. 
Rest easy, nothing’s getting out of here alive.

~VulnNet Entertainment
~TryHackMe
```

## Exploitation
```text
┌──(kali㉿kali)-[~/VulnNet]
└─$ cat Enterprise-Sync.txt  
VULNNET SYNC
~~~~~~~~~~~~~~

Johnny Leet keeps the whole infrastructure up to date and helps you sync all of your apps.
Proposals are just one part of your agency sales process. We tie together your other software, so you can import contacts from your CRM,
auto create deals and generate invoices in your accounting software. We are regularly adding new integrations.
Say no more to desync problems.
To contact our sync manager call this number: 7331 0000 1337

~VulnNet Entertainment
~TryHackMe

just for me

──(kali㉿kali)-[~/VulnNet]
└─$ pip3 install kerbrute
Defaulting to user installation because normal site-packages is not writeable
Collecting kerbrute
  Downloading kerbrute-0.0.2-py3-none-any.whl (17 kB)
Requirement already satisfied: impacket in /usr/local/lib/python3.10/dist-packages/impacket-0.9.24.dev1+20210704.162046.29ad5792-py3.10.egg (from kerbrute) (0.9.24.dev1+20210704.162046.29ad5792)
Requirement already satisfied: chardet in /home/kali/.local/lib/python3.10/site-packages (from impacket->kerbrute) (5.0.0)
Requirement already satisfied: flask>=1.0 in /usr/lib/python3/dist-packages (from impacket->kerbrute) (2.2.2)
Requirement already satisfied: future in /usr/lib/python3/dist-packages (from impacket->kerbrute) (0.18.2)
Requirement already satisfied: ldap3!=2.5.0,!=2.5.2,!=2.6,>=2.5 in /usr/lib/python3/dist-packages (from impacket->kerbrute) (2.9.1)
Requirement already satisfied: ldapdomaindump>=0.9.0 in /usr/lib/python3/dist-packages (from impacket->kerbrute) (0.9.3)
Requirement already satisfied: pyOpenSSL>=0.16.2 in /usr/lib/python3/dist-packages (from impacket->kerbrute) (21.0.0)
Requirement already satisfied: pyasn1>=0.2.3 in /usr/local/lib/python3.10/dist-packages (from impacket->kerbrute) (0.4.8)
Requirement already satisfied: pycryptodomex in /usr/lib/python3/dist-packages (from impacket->kerbrute) (3.11.0)
Requirement already satisfied: six in /usr/local/lib/python3.10/dist-packages (from impacket->kerbrute) (1.16.0)
Installing collected packages: kerbrute
  WARNING: The script kerbrute is installed in '/home/kali/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.                                                                                                         
Successfully installed kerbrute-0.0.2
```
```text
┌──(kali㉿kali)-[~/VulnNet]
└─$ kerbrute
kerbrute: command not found
```
```text
┌──(kali㉿kali)-[~/VulnNet]
└─$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games
```
```text
┌──(kali㉿kali)-[~/VulnNet]
└─$ export PATH=/home/kali/.local/bin:$PATH

https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb/rpcclient-enumeration

rpcclient es una herramienta de línea de comandos que se utiliza para interactuar con servicios de Protocolo de Mensajería de Red (RPC, por sus siglas en inglés) en sistemas operativos basados en Unix. RPC es una tecnología que permite a los programas en diferentes sistemas operativos comunicarse entre sí a través de una red.

rpcclient se utiliza a menudo para probar y depurar servicios RPC, y también puede utilizarse para realizar tareas de administración de red y para explorar la información disponible en un servidor RPC. Para utilizar rpcclient, debe conocer el nombre del servicio RPC al que desea conectarse y el puerto en el que está escuchando el servicio.

Una vez que se ha conectado a un servidor RPC utilizando rpcclient, puede utilizar comandos para realizar diferentes acciones, como listar los servicios disponibles, ver información sobre un servicio específico o realizar llamadas a procedimientos remotos.

En resumen, rpcclient es una herramienta útil para interactuar con servicios RPC y realizar tareas de administración de red en sistemas operativos basados en Unix.

Active Directory es un servicio de directorio de Microsoft que se utiliza en redes empresariales para almacenar y gestionar información sobre usuarios, dispositivos y recursos de la red. Active Directory utiliza el Protocolo de Mensajería de Red (RPC, por sus siglas en inglés) para permitir que los programas se comuniquen con el servicio de directorio y realicen tareas de administración de la red.

Para interactuar con Active Directory, puede utilizar diferentes herramientas y utilidades, como el Administrador de Active Directory, el Módulo de PowerShell para Active Directory o la herramienta de línea de comandos rpcclient. Estas herramientas le permiten realizar tareas de administración de la red, como agregar y eliminar usuarios, crear grupos y asignar permisos, y gestionar dispositivos y recursos de la red.

En resumen, Active Directory es un servicio de directorio que se utiliza en redes empresariales para almacenar y gestionar información sobre usuarios, dispositivos y recursos de la red. Puede utilizar herramientas como el Administrador de Active Directory, PowerShell o rpcclient para interactuar con Active Directory y realizar tareas de administración de la red.
```
```text
┌──(kali㉿kali)-[~/VulnNet]
└─$ rpcclient -U "" 10.10.21.40
Password for [WORKGROUP\]:
rpcclient $> help
---------------         ----------------------
       UNIXINFO
       getpwuid         Get shell and homedir
       uidtosid         Convert uid to sid
---------------         ----------------------
         MDSSVC
fetch_properties                Fetch connection properties
fetch_attributes                Fetch attributes for a CNID
---------------         ----------------------
        CLUSAPI
clusapi_open_cluster            Open cluster
clusapi_get_cluster_name                Get cluster name
clusapi_get_cluster_version             Get cluster version
clusapi_get_quorum_resource             Get quorum resource
clusapi_create_enum             Create enum query
clusapi_create_enumex           Create enumex query
clusapi_open_resource           Open cluster resource
clusapi_online_resource         Set cluster resource online
clusapi_offline_resource                Set cluster resource offline
clusapi_get_resource_state              Get cluster resource state
clusapi_get_cluster_version2            Get cluster version2
clusapi_pause_node              Pause cluster node
clusapi_resume_node             Resume cluster node
---------------         ----------------------
        WITNESS
GetInterfaceList                List the interfaces to which witness client connections can be made
       Register         Register for resource state change notifications of a NetName and IPAddress
     UnRegister         Unregister for notifications from the server</para></listitem></varlistentry>
    AsyncNotify         Request notification of registered resource changes from the server
     RegisterEx         Register for resource state change notifications of a NetName, ShareName and multiple IPAddresses
---------------         ----------------------
          FSRVP
fss_is_path_sup         Check whether a share supports shadow-copy requests
fss_get_sup_version             Get supported FSRVP version from server
fss_create_expose               Request shadow-copy creation and exposure
     fss_delete         Request shadow-copy share deletion
fss_has_shadow_copy             Check for an associated share shadow-copy
fss_get_mapping         Get shadow-copy share mapping information
fss_recovery_complete           Flag read-write snapshot as recovery complete, allowing further shadow-copy requests
---------------         ----------------------
         WINREG
 winreg_enumkey         Enumerate Keys
querymultiplevalues             Query multiple values
querymultiplevalues2            Query multiple values
---------------         ----------------------
       EVENTLOG
eventlog_readlog                Read Eventlog
eventlog_numrecord              Get number of records
eventlog_oldestrecord           Get oldest record
eventlog_reportevent            Report event
eventlog_reporteventsource              Report event and source
eventlog_registerevsource               Register event source
eventlog_backuplog              Backup Eventlog File
eventlog_loginfo                Get Eventlog Information
---------------         ----------------------
        DRSUAPI
   dscracknames         Crack Name
    dsgetdcinfo         Get Domain Controller Info
 dsgetncchanges         Get NC Changes
dswriteaccountspn               Write Account SPN
---------------         ----------------------
         NTSVCS
ntsvcs_getversion               Query NTSVCS version
ntsvcs_validatedevinst          Query NTSVCS device instance
ntsvcs_hwprofflags              Query NTSVCS HW prof flags
ntsvcs_hwprofinfo               Query NTSVCS HW prof info
ntsvcs_getdevregprop            Query NTSVCS device registry property
ntsvcs_getdevlistsize           Query NTSVCS device list size
ntsvcs_getdevlist               Query NTSVCS device list
---------------         ----------------------
         WKSSVC
wkssvc_wkstagetinfo             Query WKSSVC Workstation Information
wkssvc_getjoininformation               Query WKSSVC Join Information
wkssvc_messagebuffersend                Send WKSSVC message
wkssvc_enumeratecomputernames           Enumerate WKSSVC computer names
wkssvc_enumerateusers           Enumerate WKSSVC users
---------------         ----------------------
       SHUTDOWN
---------------         ----------------------
       EPMAPPER
         epmmap         Map a binding
      epmlookup         Lookup bindings
---------------         ----------------------
           ECHO
     echoaddone         Add one to a number
       echodata         Echo data
       sinkdata         Sink data
     sourcedata         Source data
---------------         ----------------------
            DFS
     dfsversion         Query DFS support
         dfsadd         Add a DFS share
      dfsremove         Remove a DFS share
     dfsgetinfo         Query DFS share info
        dfsenum         Enumerate dfs shares
      dfsenumex         Enumerate dfs shares
---------------         ----------------------
         SRVSVC
        srvinfo         Server query info
   netshareenum         Enumerate shares
netshareenumall         Enumerate all shares
netsharegetinfo         Get Share Info
netsharesetinfo         Set Share Info
netsharesetdfsflags             Set DFS flags
    netfileenum         Enumerate open files
   netremotetod         Fetch remote time of day
netnamevalidate         Validate sharename
  netfilegetsec         Get File security
     netsessdel         Delete Session
    netsessenum         Enumerate Sessions
    netdiskenum         Enumerate Disks
    netconnenum         Enumerate Connections
    netshareadd         Add share
    netsharedel         Delete share
---------------         ----------------------
       NETLOGON
     logonctrl2         Logon Control 2
   getanydcname         Get trusted DC name
      getdcname         Get trusted PDC name
  dsr_getdcname         Get trusted DC name
dsr_getdcnameex         Get trusted DC name
dsr_getdcnameex2                Get trusted DC name
dsr_getsitename         Get sitename
dsr_getforesttrustinfo          Get Forest Trust Info
      logonctrl         Logon Control
       samlogon         Sam Logon
change_trust_pw         Change Trust Account Password
    gettrustrid         Get trust rid
dsr_enumtrustdom                Enumerate trusted domains
dsenumdomtrusts         Enumerate all trusted domains in an AD forest
deregisterdnsrecords            Deregister DNS records
netrenumtrusteddomains          Enumerate trusted domains
netrenumtrusteddomainsex                Enumerate trusted domains
getdcsitecoverage               Get the Site-Coverage from a DC
   capabilities         Return Capabilities
logongetdomaininfo              Return LogonGetDomainInfo
---------------         ----------------------
IRemoteWinspool
winspool_AsyncOpenPrinter               Open printer handle
winspool_AsyncCorePrinterDriverInstalled                Query Core Printer Driver Installed
---------------         ----------------------
        SPOOLSS
      adddriver         Add a print driver
     addprinter         Add a printer
      deldriver         Delete a printer driver
    deldriverex         Delete a printer driver with files
       enumdata         Enumerate printer data
     enumdataex         Enumerate printer data for a key
        enumkey         Enumerate printer keys
       enumjobs         Enumerate print jobs
         getjob         Get print job
         setjob         Set print job
      enumports         Enumerate printer ports
    enumdrivers         Enumerate installed printer drivers
   enumprinters         Enumerate printers
        getdata         Get print driver data
      getdataex         Get printer driver data with keyname
      getdriver         Get print driver information
   getdriverdir         Get print driver upload directory
getdriverpackagepath            Get print driver package download directory
     getprinter         Get printer info
    openprinter         Open printer handle
 openprinter_ex         Open printer handle
      setdriver         Set printer driver
getprintprocdir         Get print processor directory
        addform         Add form
        setform         Set form
        getform         Get form
     deleteform         Delete form
      enumforms         Enumerate forms
     setprinter         Set printer comment
 setprintername         Set printername
 setprinterdata         Set REG_SZ printer data
       rffpcnex         Rffpcnex test
     printercmp         Printer comparison test
      enumprocs         Enumerate Print Processors
enumprocdatatypes               Enumerate Print Processor Data Types
   enummonitors         Enumerate Print Monitors
createprinteric         Create Printer IC
playgdiscriptonprinteric                Create Printer IC
getcoreprinterdrivers           Get CorePrinterDriver
enumpermachineconnections               Enumerate Per Machine Connections
addpermachineconnection         Add Per Machine Connection
delpermachineconnection         Delete Per Machine Connection
---------------         ----------------------
           SAMR
      queryuser         Query user info
     querygroup         Query group info
queryusergroups         Query user groups
queryuseraliases                Query user aliases
  querygroupmem         Query group membership
  queryaliasmem         Query alias membership
 queryaliasinfo         Query alias info
    deletealias         Delete an alias
  querydispinfo         Query display info
 querydispinfo2         Query display info
 querydispinfo3         Query display info
   querydominfo         Query domain info
   enumdomusers         Enumerate domain users
  enumdomgroups         Enumerate domain groups
  enumalsgroups         Enumerate alias groups
    enumdomains         Enumerate domains
  createdomuser         Create domain user
 createdomgroup         Create domain group
 createdomalias         Create domain alias
 samlookupnames         Look up names
  samlookuprids         Look up names
 deletedomgroup         Delete domain group
  deletedomuser         Delete domain user
 samquerysecobj         Query SAMR security object
   getdompwinfo         Retrieve domain password info
getusrdompwinfo         Retrieve user domain password info
   lookupdomain         Lookup Domain Name
      chgpasswd         Change user password
     chgpasswd2         Change user password
     chgpasswd3         Change user password
     chgpasswd4         Change user password
 getdispinfoidx         Get Display Information Index
    setuserinfo         Set user info
   setuserinfo2         Set user info2
---------------         ----------------------
      LSARPC-DS
  dsroledominfo         Get Primary Domain Information
---------------         ----------------------
         LSARPC
       lsaquery         Query info policy
     lookupsids         Convert SIDs to names
    lookupsids3         Convert SIDs to names
lookupsids_level                Convert SIDs to names
    lookupnames         Convert names to SIDs
   lookupnames4         Convert names to SIDs
lookupnames_level               Convert names to SIDs
      enumtrust         Enumerate trusted domains
      enumprivs         Enumerate privileges
    getdispname         Get the privilege name
     lsaenumsid         Enumerate the LSA SIDS
lsacreateaccount                Create a new lsa account
lsaenumprivsaccount             Enumerate the privileges of an SID
lsaenumacctrights               Enumerate the rights of an SID
     lsaaddpriv         Assign a privilege to a SID
     lsadelpriv         Revoke a privilege from a SID
lsaaddacctrights                Add rights to an account
lsaremoveacctrights             Remove rights from an account
lsalookupprivvalue              Get a privilege value given its name
 lsaquerysecobj         Query LSA security object
lsaquerytrustdominfo            Query LSA trusted domains info (given a SID)
lsaquerytrustdominfobyname              Query LSA trusted domains info (given a name), only works for Windows > 2k
lsaquerytrustdominfobysid               Query LSA trusted domains info (given a SID)
lsasettrustdominfo              Set LSA trusted domain info
    getusername         Get username
   createsecret         Create Secret
   deletesecret         Delete Secret
    querysecret         Query Secret
      setsecret         Set Secret
retrieveprivatedata             Retrieve Private Data
storeprivatedata                Store Private Data
 createtrustdom         Create Trusted Domain
 deletetrustdom         Delete Trusted Domain
---------------         ----------------------
GENERAL OPTIONS
           help         Get help on commands
              ?         Get help on commands
     debuglevel         Set debug level
          debug         Set debug level
           list         List available commands on <pipe>
           exit         Exit program
           quit         Exit program
           sign         Force RPC pipe connections to be signed
           seal         Force RPC pipe connections to be sealed
         packet         Force RPC pipe connections with packet authentication level
       schannel         Force RPC pipe connections to be sealed with 'schannel'. Assumes valid machine account to this domain controller.
   schannelsign         Force RPC pipe connections to be signed (not sealed) with 'schannel'.  Assumes valid machine account to this domain controller.
        timeout         Set timeout (in milliseconds) for RPC operations
      transport         Choose ncacn transport for RPC operations
           none         Force RPC pipe connections to have no special properties
rpcclient $> enumdomains
result was NT_STATUS_ACCESS_DENIED
rpcclient $> enumdomusers
result was NT_STATUS_ACCESS_DENIED
rpcclient $> quit

https://cheatsheet.haax.fr/windows-systems/exploitation/crackmapexec/

till tomorrow :) turuturu

https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb#crackmapexec

As we have a read access to IPC$ without authentication, we are able to list the domain users as anonymous

IPC$ share[](#ipcusd-share)

From book **_Network Security Assessment 3rd edition_**

With an anonymous null session you can access the IPC$ share and interact with services exposed via named pipes. The enum4linux utility within Kali Linux is particularly useful; with it, you can obtain the following:

-   Operating system information
    

-   Details of the parent domain
    
