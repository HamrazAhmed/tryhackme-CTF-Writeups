# Jacob the Boss — Writeup

## Overview
### Jacob the Boss — Writeup
### Jacob the Boss — Writeup
----
Find a way in and learn a little more.
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/065e4dc344a4c5fc9155dd4ae9eca52b.jpeg)
Start Machine
Well, the flaw that makes up this box is the reproduction found in the production environment of a customer a while ago, the verification in season consisted of two steps, the last one within the environment, we hit it head-on and more than 15 machines were vulnerable that together with the development team we were able to correct and adapt.
*First of all, add the **jacobtheboss.box** address to your hosts file.
Anyway, learn a little more, have fun!
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~]
└─$ tac /etc/hosts
10.10.59.221 jacobtheboss.box

┌──(witty㉿kali)-[~]
└─$ rustscan -a 10.10.59.221 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.10.59.221:22
Open 10.10.59.221:80
Open 10.10.59.221:111
Open 10.10.59.221:1090
Open 10.10.59.221:1098
Open 10.10.59.221:1099
Open 10.10.59.221:3306
Open 10.10.59.221:4444
Open 10.10.59.221:4445
Open 10.10.59.221:4446
Open 10.10.59.221:4712
Open 10.10.59.221:4713
Open 10.10.59.221:8083
Open 10.10.59.221:8080
Open 10.10.59.221:8009
Open 10.10.59.221:34187
Open 10.10.59.221:39279
Open 10.10.59.221:59898
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
Initiating Connect Scan
Scanning jacobtheboss.box (10.10.59.221) [18 ports]
Discovered open port 80/tcp on 10.10.59.221
Discovered open port 111/tcp on 10.10.59.221
Discovered open port 8080/tcp on 10.10.59.221
Discovered open port 3306/tcp on 10.10.59.221
Discovered open port 22/tcp on 10.10.59.221
Discovered open port 1099/tcp on 10.10.59.221
Discovered open port 59898/tcp on 10.10.59.221
Discovered open port 8083/tcp on 10.10.59.221
Discovered open port 4712/tcp on 10.10.59.221
Discovered open port 4445/tcp on 10.10.59.221
Discovered open port 1098/tcp on 10.10.59.221
Discovered open port 4444/tcp on 10.10.59.221
Discovered open port 39279/tcp on 10.10.59.221
Discovered open port 4446/tcp on 10.10.59.221
Discovered open port 34187/tcp on 10.10.59.221
Discovered open port 1090/tcp on 10.10.59.221
Discovered open port 4713/tcp on 10.10.59.221
Discovered open port 8009/tcp on 10.10.59.221
Completed Connect Scan (18 total ports)
Initiating Service scan
Scanning 18 services on jacobtheboss.box (10.10.59.221)
Completed Service scan (18 services on 1 host)
NSE: Script scanning 10.10.59.221.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
NSE Timing: About 99.88% done; ETC: 11:43 (0:00:00 remaining)
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for jacobtheboss.box (10.10.59.221)
Host is up, received user-set (0.21s latency).

PORT      STATE SERVICE     REASON  VERSION
22/tcp    open  ssh         syn-ack OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 82ca136ed963c05f4a23a5a5a5103c7f (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDOLOk6ktnJtucoDmXmBrc4H4gGe5Cybdy3jh1VZg+CYg+sZbYXzGi2/JO45cRqYd2NFIq7l+oTsjFgh76qAayKMU4D3+gKaC+U2VL93nCU1SywzvZLLc8MEy7mTHflOm4kZCmycgtJO4tfUhuH64yEP+lv3ENFeH5jgyJcGABF/p44MMSwnvpaLMfOuEGuEhKMPA4c+XAiS3J+sErUbpx6ragGGJAKTpww+arDy11slMsyJgjN6GUjlR0y+P0E4/NsrNHe86GKXJ1G4bfKEdKOPeTZ+wZMNFDCVNLPHLWUBIgWNQHIgRcXiBvPAvIrrt8gV/+td9C74Bsj0VqEEJnP
|   256 a46ed25d0d362e732f1d529ce58a7b04 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNUtPCeXKNaq6WZlT3PxbZbQmka1bb5I+yBRhUb5tzmf2GEmdDOk6R7MSUlEtzGzQ4GjAWFZG3q7ZcBahg8ur8A=
|   256 6f54a65eba5badcc87eed3a8d5e0aa2a (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJI3bQUWzwhk0iJYl+gGn09NgvRLtN4vJ4DG6SrE7/Hb
80/tcp    open  http        syn-ack Apache httpd 2.4.6 ((CentOS) PHP/7.3.20)
|_http-title: My first blog
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.6 (CentOS) PHP/7.3.20
111/tcp   open  rpcbind     syn-ack 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|_  100000  3,4          111/udp6  rpcbind
1090/tcp  open  java-rmi    syn-ack Java RMI
|_rmi-dumpregistry: ERROR: Script execution failed (use -d to debug)
1098/tcp  open  java-rmi    syn-ack Java RMI
1099/tcp  open  java-object syn-ack Java Object Serialization
| fingerprint-strings: 
|   NULL: 
|     java.rmi.MarshalledObject|
|     hash[
|     locBytest
|     objBytesq
|     http://jacobtheboss.box:8083/q
|     org.jnp.server.NamingServer_Stub
|     java.rmi.server.RemoteStub
|     java.rmi.server.RemoteObject
|     xpw;
|     UnicastRef2
|_    jacobtheboss.box
3306/tcp  open  mysql       syn-ack MariaDB (unauthorized)
4444/tcp  open  java-rmi    syn-ack Java RMI
4445/tcp  open  java-object syn-ack Java Object Serialization
4446/tcp  open  java-object syn-ack Java Object Serialization
4712/tcp  open  msdtc       syn-ack Microsoft Distributed Transaction Coordinator (error)
4713/tcp  open  pulseaudio? syn-ack
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, JavaRMI, Kerberos, LANDesk-RC, LDAPBindReq, LDAPSearchReq, LPDString, NCP, NULL, NotesRPC, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie, WMSRequest, X11Probe, afp, giop, ms-sql-s, oracle-tns: 
|_    858b
8009/tcp  open  ajp13       syn-ack Apache Jserv (Protocol v1.3)
| ajp-methods: 
|   Supported methods: GET HEAD POST PUT DELETE TRACE OPTIONS
|   Potentially risky methods: PUT DELETE TRACE
|_  See https://nmap.org/nsedoc/scripts/ajp-methods.html
8080/tcp  open  http        syn-ack Apache Tomcat/Coyote JSP engine 1.1
|_http-favicon: Unknown favicon MD5: 799F70B71314A7508326D1D2F68F7519
| http-methods: 
|   Supported Methods: GET HEAD POST PUT DELETE TRACE OPTIONS
|_  Potentially risky methods: PUT DELETE TRACE
|_http-title: Welcome to JBoss&trade;
|_http-server-header: Apache-Coyote/1.1
|_http-open-proxy: Proxy might be redirecting requests
8083/tcp  open  http        syn-ack JBoss service httpd
|_http-title: Site doesn't have a title (text/html).
34187/tcp open  unknown     syn-ack
39279/tcp open  java-rmi    syn-ack Java RMI
59898/tcp open  unknown     syn-ack
4 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port1099-TCP:V=7.93%I=7%D=7/23%Time=64BD49E4%P=x86_64-pc-linux-gnu%r(NU
SF:LL,16F,"\xac\xed\0\x05sr\0\x19java\.rmi\.MarshalledObject\|\xbd\x1e\x97
SF:\xedc\xfc>\x02\0\x03I\0\x04hash\[\0\x08locBytest\0\x02\[B\[\0\x08objByt
SF:esq\0~\0\x01xp\x01\"U\xeaur\0\x02\[B\xac\xf3\x17\xf8\x06\x08T\xe0\x02\0
SF:\0xp\0\0\0\.\xac\xed\0\x05t\0\x1dhttp://jacobtheboss\.box:8083/q\0~\0\0
SF:q\0~\0\0uq\0~\0\x03\0\0\0\xc7\xac\xed\0\x05sr\0\x20org\.jnp\.server\.Na
SF:mingServer_Stub\0\0\0\0\0\0\0\x02\x02\0\0xr\0\x1ajava\.rmi\.server\.Rem
SF:oteStub\xe9\xfe\xdc\xc9\x8b\xe1e\x1a\x02\0\0xr\0\x1cjava\.rmi\.server\.
SF:RemoteObject\xd3a\xb4\x91\x0ca3\x1e\x03\0\0xpw;\0\x0bUnicastRef2\0\0\x1
SF:0jacobtheboss\.box\0\0\x04J\0\0\0\0\0\0\0\0m\xfb\x10\xeb\0\0\x01\x89\x8
SF:3fK\xf6\x80\0\0x");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port4445-TCP:V=7.93%I=7%D=7/23%Time=64BD49EA%P=x86_64-pc-linux-gnu%r(NU
SF:LL,4,"\xac\xed\0\x05");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port4446-TCP:V=7.93%I=7%D=7/23%Time=64BD49EA%P=x86_64-pc-linux-gnu%r(NU
SF:LL,4,"\xac\xed\0\x05");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port4713-TCP:V=7.93%I=7%D=7/23%Time=64BD49EA%P=x86_64-pc-linux-gnu%r(NU
SF:LL,5,"858b\n")%r(GenericLines,5,"858b\n")%r(GetRequest,5,"858b\n")%r(HT
SF:TPOptions,5,"858b\n")%r(RTSPRequest,5,"858b\n")%r(RPCCheck,5,"858b\n")%
SF:r(DNSVersionBindReqTCP,5,"858b\n")%r(DNSStatusRequestTCP,5,"858b\n")%r(
SF:Help,5,"858b\n")%r(SSLSessionReq,5,"858b\n")%r(TerminalServerCookie,5,"
SF:858b\n")%r(TLSSessionReq,5,"858b\n")%r(Kerberos,5,"858b\n")%r(SMBProgNe
SF:g,5,"858b\n")%r(X11Probe,5,"858b\n")%r(FourOhFourRequest,5,"858b\n")%r(
SF:LPDString,5,"858b\n")%r(LDAPSearchReq,5,"858b\n")%r(LDAPBindReq,5,"858b
SF:\n")%r(SIPOptions,5,"858b\n")%r(LANDesk-RC,5,"858b\n")%r(TerminalServer
SF:,5,"858b\n")%r(NCP,5,"858b\n")%r(NotesRPC,5,"858b\n")%r(JavaRMI,5,"858b
SF:\n")%r(WMSRequest,5,"858b\n")%r(oracle-tns,5,"858b\n")%r(ms-sql-s,5,"85
SF:8b\n")%r(afp,5,"858b\n")%r(giop,5,"858b\n");
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

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
Nmap done: 1 IP address (1 host up) scanned in 202.16 seconds

http://jacobtheboss.box:8080/ Jboss

http://jacobtheboss.box:8080/jbossws/

    Version: jbossws-native-3.0.4.SP1
    Build: 200811271317
    View a list of deployed services
    Access JMX console

like tony tiger

git clone https://github.com/joaomatosf/jexboss.git
cd jexboss
pip install -r requires.txt
python jexboss.py -h

┌──(witty㉿kali)-[~/Downloads/jexboss]
└─$ python jexboss.py -host http://jacobtheboss.box:8080

