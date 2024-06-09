---
Perform Registry Forensics to Investigate a case.
---

# Secret Recipe — Writeup

## Overview
### Secret Recipe — Writeup
### Secret Recipe — Writeup
![](https://tryhackme-images.s3.amazonaws.com/room-icons/08870f82d4ce4374cdc6fe1ad922d0e3.png)
### Introduction
Start Machine
Storyline
His machine has been confiscated and examined, but no traces could be found. The security department has pulled some important **registry artifacts** from his device and has tasked you to examine these artifacts and determine the presence of secret files on his machine.
Room Machine
Before moving forward, let's deploy the machine. The machine will start in a split-screen view. In case the VM is not visible, use the blue Show Split View button at the top-right of the page. You may also access it via the AttackBox or RDP using the credentials below. It will take up to 3-5 minutes to start.
On the Desktop, there is a folder named `Artifacts`, which contains the registry Hives to examine and another folder named `EZ tools`, which includes all the required tools to analyze the artifacts.
**Credentials**
**Username**: `Administrator`
**Password:** `thm_4n6`
**Note:** If you are using Registry Explorer to parse the hives, expect some delay in loading as it takes time to parse the hives.
Answer the questions below
Connect with the Lab
Completed
How many Files are available in the Artifacts folder on the Desktop?
![[Pasted image 20230121145600.png]]
*6*
### Windows Registry Forensics
Download Task Files
Registry Recap
Following Registry Hives have been pulled from the suspect Host and placed in the `C:\Users\Administrator\Desktop\Artifacts` folder. All required tools are also placed on the path. `C:\Users\Administrator\Desktop\EZ Tools`.
Your challenge is to examine the registry hives using the tools provided, observe the user's activities and answer the questions.
Registry Hives
-   SYSTEM
-   SECURITY
-   SOFTWARE
-   SAM
-   NTUSER.DAT
-   UsrClass.dat
**Note:** The `Download Task Files` button has a cheat sheet, which can be used as a reference to answer the questions.
Answer the questions below
```text
Los archivos mencionados (SYSTEM, SECURITY, SOFTWARE, SAM, NTUSER.DAT, UsrClass.dat) son todos archivos de sistema de Windows conocidos como "tableros" o "colmenas" del Registro. Cada uno de estos archivos contiene una serie de claves y valores que se utilizan para almacenar la configuración del sistema y los programas instalados.

-   SYSTEM: Contiene información sobre los controladores de dispositivos y el hardware del sistema.
-   SECURITY: Contiene información sobre la seguridad del sistema, incluyendo cuentas de usuario y grupos, políticas de seguridad y registros de auditoría.
-   SOFTWARE: Contiene información sobre los programas instalados en el sistema, incluyendo configuraciones de programas y claves de registro de aplicaciones.
-   SAM: Contiene información sobre las cuentas de usuario del sistema, incluyendo nombres de usuario y contraseñas cifradas.
-   NTUSER.DAT: Contiene información sobre la configuración de usuario individual, incluyendo preferencias de escritorio, configuraciones de programas y historial de navegación.
-   UsrClass.dat: Contiene información sobre la configuración de clases de usuario, que se utiliza para personalizar la experiencia de usuario en el sistema.

Un "tablero" o "colmena" del Registro es un archivo que almacena un conjunto de claves y valores que se utilizan para almacenar la configuración del sistema y los programas instalados en el sistema operativo Windows. El registro es una base de datos jerárquica que contiene información sobre hardware, software, configuraciones de usuario y aplicaciones. Los tableros son los archivos donde se guarda esa información.

Shellbags is a term used to describe information that is stored in the Windows Registry related to the configuration of folders and the way they are displayed in Windows Explorer. This information includes the size and position of the window, the sort order of the files, and the folder's expanded or collapsed state.

For example, if a user opens a folder and resizes the window, this new size is stored in the Shellbags key of the Windows Registry. Next time the user opens that folder, the folder will automatically open with the same size and position that the user last used.

Another example is if a user opens a folder and sorts the files by the date modified, this new sort order is also stored in the Shellbags key of the Windows Registry. Next time the user opens that folder, the files will automatically be sorted by the date modified, this way the user doesn't have to sort the files again.

In summary, Shellbags is a feature of Windows that automatically saves and restores the settings of the folders and files, like the position, size, sorting, expanded and collapsed state, etc.

-   Current Control Set: This is a key in the Windows Registry that contains settings and configuration information for the current version of Windows. This key is used to store system-wide settings, including device driver settings, services and device settings, and other system-wide configurations.
    
-   MRUs (Most Recently Used): These are keys in the Windows Registry that store a list of the most recently used files, folders, and other resources by the user. For example, the MRU key for the Run dialog box stores a list of the most recent commands typed in the Run dialog box.
    
-   UserAssist: This is a key in the Windows Registry that stores information about the programs and files that a user has used on the system. It keeps track of the number of times the user has opened a program or file, the last time it was opened, and other related information.
    
-   ShimCache: This is a cache of shims, which are small programs that are used to fix compatibility issues with older programs. ShimCache stores information about the shims that have been used on the system, including the name of the shim, the date and time it was used, and other related information.
    
-   Amcache: This is a key in the Windows Registry that stores information about applications that have been installed on the system. It keeps track of the name, publisher, version, and other information about the application, and the date and time it was installed.
    
-   BAM/DAM (Boot Execution and Application Execution): These are keys in the Windows Registry that store information about the programs and files that have been run on the system during the boot process and after the system has started up. This information includes the name of the program or file, the date and time it was run, and other related information.
    

For example, when a user runs a program, ShimCache will store information about the program and when it was run. This information can be useful for forensic analysis, as it can provide insight into what programs were run on a system and when. Another example is when an user install an application, Amcache will store information about the application name, publisher, version, and the date and time it was installed. This information can be used to identify what programs were installed on a system and when.

Regenerate response

Using Registry explorer v1.6.0.0

1)
Load Hive/SYSTEM/

SYSTEM\ControlSet001\Control\ComputerName\ComputerName ---> JAMES

2) Load Hive/SAM/

SAM\Domains\Account\Users\Name\Administrator ---> 2021-03-17 14:58:48 (copy last write time)

3)

RegUnknown (0x1F4, 500 decimal)

The RID (Relative Identifier) associated with the Administrator account is typically 500. RID is a unique number that is assigned to each account in Windows and is used to differentiate between different accounts on the system. The RID is part of the security identifier (SID) of an account, which is used to identify the account and its permissions on the system. The SID is composed of a domain SID, which is unique to the domain or system, and a RID, which is unique to the account within the domain or system.

In Windows, the RID for the built-in Administrator account is 500. This is a well-known RID and is used by the system to identify the Administrator account, regardless of the name that is assigned to it. Other built-in accounts such as Guest, also have well-known RIDs.

It is important to note that RID can be changed, but it is not recommend as it can cause issues on the system.

Un ejemplo de cómo se ve un SID con un RID es: S-1-5-21-34233434-123456789-12345678-500, en donde el último número, 500 es el RID que identifica a la cuenta Administrador.

Otro ejemplo es, un usuario llamado "Juan" tiene una cuenta en el sistema operativo Windows, el sistema le asigna un RID, por ejemplo 1000, este RID es único para esa cuenta y no se repite en otras cuentas.

4)

7 users: Administrator, art-test, bdoor, DefaultAccount, Guest, J. Andreson and WDAGUtilityAccount.

5)

bdoor  -> RegUnknown (0x3F5, 1013 decimal)

6)

Load Hive/Software

Software/Microsoft/Windows NT/CurrentVersion/NetworkList ---> ProtonVPN

7)

First Connect LOCAL

2022-10-12 19:52:36

8)

Load Hive/SYSTEM

search shares

SYSTEM/ControlSet001/Services/LanmanServer/Shares -- Path=C:\RESTRICTED FILES (Value Name RESTRICTED)

8)

DHCP (Dynamic Host Configuration Protocol) is a network protocol that is used to automatically assign IP addresses, subnet masks, default gateways, and other network configuration settings to devices on a network. This eliminates the need for manual configuration of these settings on each device.

For example, when a device such as a laptop or smartphone is connected to a network, it sends a broadcast message requesting an IP address. The DHCP server on the network receives this request and assigns an available IP address to the device along with the necessary network configuration settings. The device can then communicate on the network using the assigned IP address.

Another example, in a company, when a new employee joins the company, he/she is given a laptop. The employee connects the laptop to the company's network via a wired or wireless connection. The laptop sends a request for an IP address to the DHCP server. The DHCP server assigns an available IP address to the laptop, and also assigns the necessary network configurations such as the subnet mask and the default gateway. This way, the new employee can start working on his/her laptop and access the company's network resources.

In short, DHCP is a protocol that helps automate the process of assigning IP addresses and other network configurations to devices on a network, making it easier for network administrators to manage and maintain the network.

Load Hive/SYSTEM

SYSTEM\ControlSet001\Services\Tcpip \Parameters\Interfaces (DHCPIP Address 172.31.2.197)

9)

Load Hive/NTUSER.DAT

NTUSER.DAT\Software\Microsoft\Windows \CurrentVersion\Explorer\RecentDocs\pdf (secret-recipe.pdf)

10)

RunMRU (Run Most Recently Used) is a key in the Windows Registry that stores a list of the most recently used commands that were typed into the Run dialog box. The Run dialog box is a feature in Windows that allows users to quickly open programs, files, and folders by typing the name or path of the item into the Run box and pressing Enter.

