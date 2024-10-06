---
Learn the methodology of enumerating websites by using tools such as Gobuster, Nikto and WPScan
---

# Web Enumeration — Writeup

## Enumeration
![](https://assets.tryhackme.com/additional/banners/webenumeration-banner.png)
### Introduction
Welcome to Web Enumeration! In this room, we'll be showcasing some of the most fundamental tools used in the enumeration stage of a web target. Good enumeration skills are vital in penetration testing -- how else are you supposed to know what you're targeting?! It is, however, rather easy to fall into rabbit holes.
The tools we'll showcase will hopefully make this process easier. You'll be able to apply the knowledge gained for each tool on an Instance dedicated to each tool.
Prerequisities for this lab
You will need to be connected to the TryHackMe network if you are not using the TryHackMe AttackBox or Kali instance. Other than that, all you need is a good posture and some willpower!
Note: This room has been written as if you were using the TryHackMe AttackBox.
﻿We don't need to start unrolling the fancy toolkit from the get-go. More often than not, the results of using our own initiative over automated scans bare more results. For example, we may be able to find the "golden ticket" without making all of the noise. Let's outline some fundamentals skills involving you and your browser.
Your browser is as extensive as you are (and some!) and keeps records of the data it receives and who from. We can use this for a range of activities: finding that exact photo or more usefully -- the location of certain files or assets being loaded. This could include things from scripts to page URLs.
Using our Browsers Developer Console
Modern-day browsers including Chrome and Firefox have a suite of tools located in the "Developer Tools/Console". We're going to be discussing Firefox's, however, Chrome has a very similar suite. This suite includes a range of tools including:
Viewing page source code
Finding assets
Debugging & executing code such as javascript on the client-side (our Browser)
Using "F12" on our keyboard, this is a shortcut to launch this suite of tools.
Inspecting Tool.
![](https://assets.tryhackme.com/additional/web-enumeration-redux/manual-enumeration/dev-inspectelement.png)
At first, we can see the web page with the heading "Hi Friend" and a section of the screen filled with the "Inspector" tool. This allows us to view the HTML source code of the webpage we have loaded in our browser. This often contains things such as developer comments, and the name to certain aspects of web page features including forms and the likes.
Developers often leave behind comments in the form of the <!-- --> tags...for example: <!-- This is a comment --> which are not rendered in the browser as we can see here:
![](https://assets.tryhackme.com/additional/web-enumeration-redux/manual-enumeration/comments.png)
![](https://assets.tryhackme.com/additional/web-enumeration-redux/manual-enumeration/comments2.png)
I gotcha!
### 1. Introduction to Gobuster
Introduction to Gobuster
Welcome to the Gobuster portion of this room! This part of the room is aimed at complete beginners to enumeration and penetration testing. By completing this portion, you will have learned:
How to install Gobuster on Kali Linux
How to use the "dir" mode to enumerate directories and several of its most useful options
How to use the "dns" mode to enumerate domains/subdomains and several of its most useful option
Where to go for help
At the end of this section, you will have the opportunity to practice what you have learned by using Gobuster on another room, [Blog](https://tryhackme.com/room/blog). This room utilizes what's called a Content Management System (CMS) in order to make things easier for the user. These typically have large and varied directory structures...perfect for directory enumeration with Gobuster!
With the introduction out of the way, let's get started!
What is Gobuster?
As the name implies, Gobuster is written in [Go](https://golang.org/). Go is an open-source, low-level language (much like C or Rust) developed by a team at Google and other contributors. If you'd like to learn more about Go, visit the website linked above.
Installing Gobuster on Kali Linux
Luckily, installing Gobuster on Kali Linux does not require any installation of Go and does not carry with it a complicated install process. This means no building from source or running any other complicated commands. Ready?
sudo apt install gobuster
Done.
Useful Global Flags
There are some useful Global flags that can be used as well. I've included them in the table below. You can review these in the main documentation as well - [here](https://github.com/OJ/gobuster).
Flag	Long Flag	Description
-t	--threads	Number of concurrent threads (default 10)
-v	--verbose	Verbose output
-z	--no-progress	Don't display progress
-q	--quiet	Don't print the banner and other noise
-o	--output	Output file to write results to
I will typically change the number of threads to 64 to increase the speed of my scans. If you don't change the number of threads, Gobuster can be a little slow.
### 1.1. Gobuster Modes
"dir" Mode
Dirbuster has a "dir" mode that allows the user to enumerate website directories. This is useful when you are performing a penetration test and would like to see what the directory structure of a website is. Often, directory structures of websites and web-apps follow a certain convention, making them susceptible to brute-forcing using wordlists. At the end of this room, you'll run Gobuster on Blog which uses WordPress, a very common Content Management System (CMS). WordPress uses a very specific directory structure for its websites.
Gobuster is powerful because it not only allows you to scan the website, but it will return the status codes as well. This will immediately let you know if you as an outside user can request that directory or not. Additional functionality of Gobuster is that it lets you search for files as well with the addition of a simple flag!
Using "dir" Mode
To use "dir" mode, you start by typing gobuster dir. This isn't the full command, but just the start. This tells Gobuster that you want to perform a directory search, instead of one of its other methods (which we'll get to). It has to be written like this or else Gobuster will complain. After that, you will need to add the URL and wordlist using the -u and -w options, respectively. Like so:
gobuster dir -u http://10.10.10.10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
Note: The URL is going to be the base path where Gobuster starts looking from. So the URL above is using the root web directory. For example, in a typical Apache installation on Linux, this is /var/www/html. So if you have a "products" directory and you want to enumerate that directory, you'd set the URL as http://10.10.10.10/products. You can also think of this like http://example.com/path/to/folder. Also notice that I specified the protocol of HTTP. This is important and required.
This is a very common, simple, and straightforward command for Gobuster. This is typically what I will run when doing capture the flag style rooms on TryHackMe. However, there are some other helpful flags that can be useful in certain scenarios
Other Useful Flags
These flags are useful in certain scenarios.  Note that these are not all of the flag options, but some of the more common ones that you'll use in penetration tests and in capture the flag events. If you'd like the full list, you can see that here.
Flag	Long Flag	Description
-c	--cookies	Cookies to use for requests
-x	--extensions	File extension(s) to search for
-H	--headers	Specify HTTP headers, -H 'Header1: val1' -H 'Header2: val2'
-k	--no-tls-validation	Skip TLS certificate verification
-n	--no-status	Don't print status codes
-P	--password	Password for Basic Auth
-s	--status-codes	Positive status codes
-b	--status-codes-blacklist	Negative status codes
-U	--username	Username for Basic Auth
A very common use of Gobuster's "dir" mode is the ability to use it's -x or --extensions flag to search for the contents of directories that you have already enumerated by providing a list of file extensions. File extensions are generally representative of the data they may contain. For example, .conf or .config files usually contain configurations for the application - including sensitive info such as database credentials.
A few other files that you may wish to search for are .txt files or other web application pages such as .html or .php . Let's assemble a command that would allow us to search the "myfolder" directory on a webserver for the following three files:
1. html
2. js
3. css
gobuster dir -u http://10.10.252.123/myfolder -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x.html,.css,.js
The -k Flag
The -k flag is special because it has an important use during penetration tests and captures the flag events. In a capture the flag room on TryHackMe for example, if HTTPS is enabled, you will most likely encounter an invalid cert error like the one below
![](https://comodosslstore.com/resources/wp-content/uploads/2018/08/NET-ERR_CERT_DATE_INVALID.png)
In instances like this, if you try to run Gobuster against this without the -k flag, it won't return anything and will most likely error out with something gross and will leave you sad. Don't worry though, easy fix! Just add the -k flag to your scan and it will bypass this invalid certification and continue scanning and deliver the goods!
Note: This flag can be used with "dir" mode and "vhost" modes
"dns" Mode
The next mode we'll focus on is the "dns" mode. This allows Gobuster to brute-force subdomains. During a penetration test (or capture the flag), it's important to check sub-domains of your target's top domain. Just because something is patched in the regular domain, does not mean it is patched in the sub-domain. There may be a vulnerability for you to exploit in one of these sub-domains. For example, if State Farm owns statefarm.com and mobile.statefarm.com, there may be a hole in mobile.statefarm.com that is not present in statefarm.com. This is why it is important to search for subdomains too!
Using "dns" Mode
To use "dns" mode, you start by typing gobuster dns. Just like "dir" mode, this isn't the full command, but just the start. This tells Gobuster that you want to perform a sub-domain brute-force, instead of one of one of the other methods as previously mentioned. It has to be written like this or else Gobuster will complain. After that, you will need to add the domain and wordlist using the -d and -w options, respectively. Like so:
gobuster dns -d mydomain.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
This tells Gobuster to do a sub-domain scan on the domain "mydomain.thm". If there are any sub-domains available, Gobuster will find them and report them to you in the terminal.
Other Useful Flags
-d and -w are the main flags that you'll need for most of your scans. But there are a few others that are worth mentioning that we can go over. They are in the table below.
Flag	Long Flag	Description
-c	--show-cname	Show CNAME Records (cannot be used with '-i' option)
-i	--show-ips	Show IP Addresses
-r	--resolver	Use custom DNS server (format server.com or server.com:port)
There aren't many additional flags to be used with this mode, but these are the main useful ones that you may use from time to time. If you'd like to see the full list of flags that can be used with this mode, check out the documentation
"vhost" Mode
The last and final mode we'll focus on is the "vhost" mode. This allows Gobuster to brute-force virtual hosts. Virtual hosts are different websites on the same machine. In some instances, they can appear to look like sub-domains, but don't be deceived! Virtual Hosts are IP based and are running on the same server. This is not usually apparent to the end-user. On an engagement, it may be worthwhile to just run Gobuster in this mode to see if it comes up with anything. You never know, it might just find something! While participating in rooms on TryHackMe, virtual hosts would be a good way to hide a completely different website if nothing turned up on your main port 80/443 scan.
Using "vhost" Mode
To use "vhost" mode, you start by typing gobuster vhost. Just like the other modes, this isn't the full command, but just the start. This tells Gobuster that you want to perform a virtual host brute-force, instead of one of the other methods as previously mentioned. It has to be written like this or else Gobuster will complain. After that, you will need to add the domain and wordlist using the -u and -w options, respectively. Like so:
gobuster vhost -u http://example.com -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
This will tell Gobuster to do a virtual host scan http://example.com using the selected wordlist.
Other Useful Flags
A lot of the same flags that are useful for "dir" mode actually still apply to virtual host mode. Please check out the "dir" mode section for these and take a look at the official documentation for the full list. There's really too many that are similar to put them back here.
I get the hang of it!
### 1.2. Useful Wordlists
Useful Wordlists
﻿There are many useful wordlists to use for each mode. These may or may not come in handy later on during the VM portion of the room! I'll go over some of the ones that are on Kali by default as well as a short section on SecLists.
Kali Linux Default Lists
Below you will find a useful list of wordlists that are installed on Kali Linux by default. This is as of the latest version at the time of writing which is 2020.3. Anything with a wildcard (*) character indicates there's more than one list that matches. Keep in mind, a lot of these can be interchanged between modes. For example, "dir" mode wordlists (such as ones from the dirbuster directory) will contain words like "admin", "index", "about", "events", etc. A lot of these could be subdomains as well. Give them a try with the different modes!
/usr/share/wordlists/dirbuster/directory-list-2.3-*.txt
/usr/share/wordlists/dirbuster/directory-list-1.0.txt
/usr/share/wordlists/dirb/big.txt
/usr/share/wordlists/dirb/common.txt
/usr/share/wordlists/dirb/small.txt
/usr/share/wordlists/dirb/extensions_common.txt - Useful for when fuzzing for files!
Non-Standard Lists
In addition to the above, Daniel Miessler has created an amazing GitHub repo called SecLists. It compiles many different lists used for many different things. The best part is, it's in apt! You can sudo apt install seclists and get the entire repo! We won't dive into any other lists as there are many. However, between what's installed by default on Kali and the SecLists repo, I doubt you'll need anything else.
### 1.3. Practical: Gobuster (Deploy #1)
Gobuster Challenges
Now's your chance to check what you've learned. Deploy the VM, allow five minutes for it to fully deploy and answer the following questions! Good luck!
You will also need to add "webenum.thm" to your /etc/hosts file to start off with like so:
echo "10.10.148.19 webenum.thm" >> /etc/hosts
You will also need to add any virtual hosts that you discover through the same way, before you can visit them in your browser i.e.:
echo "10.10.148.19 mysubdomain.webenum.thm" >> /etc/hosts
Any answer that has a list of items will have its answer formatted in the following way: ans1,ans2. Be sure to format your answers like that to get credit.
```text
┌──(root㉿kali)-[/home/kali]
└─# echo "10.10.148.19 webenum.thm" >> /etc/hosts
                                                                          
┌──(root㉿kali)-[/home/kali]
└─# echo "10.10.148.19 mysubdomain.webenum.thm" >> /etc/hosts
                                                                          
┌──(root㉿kali)-[/home/kali]
└─# cat /etc/hosts         
127.0.0.1       localhost
127.0.1.1       kali
10.10.113.254   magician
10.10.121.237   git.git-and-crumpets.thm
10.10.149.10    hipflasks.thm hipper.hipflasks.thm
10.10.91.93     raz0rblack raz0rblack.thm
10.10.234.77    lab.enterprise.thm
10.10.96.58     source
10.10.59.104    CONTROLLER.local
10.10.54.75     acmeitsupport.thm
10.10.102.33    overwrite.uploadvulns.thm shell.uploadvulns.thm java.uploadvulns.thm annex.uploadvulns.thm magic.uploadvulns.thm jewel.uploadvulns.thm demo.uploadvulns.thm
10.10.179.221   development.smag.thm
10.10.87.241    mafialive.thm
10.10.97.105    internal.thm
10.10.106.113   retro.thm
```
```text
# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

10.10.148.19 webenum.thm
10.10.148.19 mysubdomain.webenum.thm
```
Run a directory scan on the host. Other than the standard css, images and js directories, what other directories are available?
```text
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://webenum.thm -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 64 
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://webenum.thm
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/10/03 17:13:21 Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 301) [Size: 311] [--> http://webenum.thm/images/]
Progress: 169 / 220561 (0.08%)                                            /public               (Status: 301) [Size: 311] [--> http://webenum.thm/public/]
Progress: 281 / 220561 (0.13%)                                            Progress: 393 / 220561 (0.18%)                                            Progress: 479 / 220561 (0.22%)                                            Progress: 575 / 220561 (0.26%)                                            /css                  (Status: 301) [Size: 308] [--> http://webenum.thm/css/]   
Progress: 723 / 220561 (0.33%)                                            Progress: 855 / 220561 (0.39%)                                            Progress: 991 / 220561 (0.45%)                                            /js                   (Status: 301) [Size: 307] [--> http://webenum.thm/js/]    
Progress: 1163 / 220561 (0.53%)                                           Progress: 1283 / 220561 (0.58%)                                           Progress: 1411 / 220561 (0.64%)                                           Progress: 1480 / 220561 (0.67%)                                           Progress: 1620 / 220561 (0.73%)                                           Progress: 1799 / 220561 (0.82%)                                           Progress: 1934 / 220561 (0.88%)                                           Progress: 2071 / 220561 (0.94%)                                           Progress: 2254 / 220561 (1.02%)                                           Progress: 2442 / 220561 (1.11%)                                           Progress: 2574 / 220561 (1.17%)                                           Progress: 2723 / 220561 (1.23%)                                           Progress: 2891 / 220561 (1.31%)                                           Progress: 3023 / 220561 (1.37%)                                           Progress: 3211 / 220561 (1.46%)                                           Progress: 3345 / 220561 (1.52%)                                           Progress: 3532 / 220561 (1.60%)                                           Progress: 3665 / 220561 (1.66%)                                           Progress: 3827 / 220561 (1.74%)                                           Progress: 4014 / 220561 (1.82%)                                           Progress: 4151 / 220561 (1.88%)                                           Progress: 4338 / 220561 (1.97%)                                           Progress: 4482 / 220561 (2.03%)                                           Progress: 4663 / 220561 (2.11%)                                           Progress: 4829 / 220561 (2.19%)                                           Progress: 4986 / 220561 (2.26%)                                           Progress: 5175 / 220561 (2.35%)                                           Progress: 5367 / 220561 (2.43%)                                           Progress: 5498 / 220561 (2.49%)                                           Progress: 5687 / 220561 (2.58%)                                           Progress: 5836 / 220561 (2.65%)                                           Progress: 6008 / 220561 (2.72%)                                           Progress: 6198 / 220561 (2.81%)                                           Progress: 6335 / 220561 (2.87%)                                           Progress: 6518 / 220561 (2.96%)                                           Progress: 6660 / 220561 (3.02%)                                           Progress: 6842 / 220561 (3.10%)                                           Progress: 7024 / 220561 (3.18%)                                           Progress: 7164 / 220561 (3.25%)                                           Progress: 7354 / 220561 (3.33%)                                           Progress: 7489 / 220561 (3.40%)                                           Progress: 7665 / 220561 (3.48%)                                           Progress: 7798 / 220561 (3.54%)                                           Progress: 7960 / 220561 (3.61%)                                           Progress: 8116 / 220561 (3.68%)                                           Progress: 8281 / 220561 (3.75%)                                           Progress: 8472 / 220561 (3.84%)                                           Progress: 8644 / 220561 (3.92%)                                           Progress: 8793 / 220561 (3.99%)                                           Progress: 8979 / 220561 (4.07%)                                           Progress: 9132 / 220561 (4.14%)                                           Progress: 9305 / 220561 (4.22%)                                           Progress: 9496 / 220561 (4.31%)                                           Progress: 9636 / 220561 (4.37%)                                           Progress: 9817 / 220561 (4.45%)                                           Progress: 10001 / 220561 (4.53%)                                          Progress: 10137 / 220561 (4.60%)                                          Progress: 10329 / 220561 (4.68%)                                          Progress: 10467 / 220561 (4.75%)                                          Progress: 10650 / 220561 (4.83%)                                          Progress: 10841 / 220561 (4.92%)                                          Progress: 10985 / 220561 (4.98%)                                          Progress: 11164 / 220561 (5.06%)                                          Progress: 11306 / 220561 (5.13%)                                          Progress: 11484 / 220561 (5.21%)                                          Progress: 11636 / 220561 (5.28%)                                          Progress: 11817 / 220561 (5.36%)                                          Progress: 11965 / 220561 (5.42%)                                          Progress: 12148 / 220561 (5.51%)                                          Progress: 12330 / 220561 (5.59%)                                          Progress: 12473 / 220561 (5.66%)                                          Progress: 12660 / 220561 (5.74%)                                          /Changes              (Status: 301) [Size: 312] [--> http://webenum.thm/Changes/]
Progress: 12811 / 220561 (5.81%)                                          Progress: 12956 / 220561 (5.87%)                                          Progress: 13089 / 220561 (5.93%)                                          Progress: 13264 / 220561 (6.01%)                                          Progress: 13441 / 220561 (6.09%)                                          Progress: 13601 / 220561 (6.17%)                                          Progress: 13765 / 220561 (6.24%)                                          Progress: 13920 / 220561 (6.31%)                                          Progress: 14102 / 220561 (6.39%)                                          Progress: 14280 / 220561 (6.47%)                                          Progress: 14436 / 220561 (6.55%)                                          Progress: 14542 / 220561 (6.59%)                                          Progress: 14662 / 220561 (6.65%)                                          Progress: 14791 / 220561 (6.71%)                                          Progress: 14928 / 220561 (6.77%)                                          Progress: 15112 / 220561 (6.85%)                                          Progress: 15249 / 220561 (6.91%)                                          Progress: 15439 / 220561 (7.00%)                                          Progress: 15624 / 220561 (7.08%)                                          Progress: 15762 / 220561 (7.15%)                                          Progress: 15952 / 220561 (7.23%)                                          Progress: 16123 / 220561 (7.31%)                                          Progress: 16276 / 220561 (7.38%)                                          Progress: 16464 / 220561 (7.46%)                                          Progress: 16646 / 220561 (7.55%)                                          Progress: 16791 / 220561 (7.61%)                                          Progress: 16977 / 220561 (7.70%)                                          Progress: 17159 / 220561 (7.78%)                                          Progress: 17316 / 220561 (7.85%)                                          Progress: 17486 / 220561 (7.93%)                                          Progress: 17637 / 220561 (8.00%)                                          Progress: 17829 / 220561 (8.08%)                                          Progress: 17996 / 220561 (8.16%)                                          Progress: 18158 / 220561 (8.23%)                                          Progress: 18341 / 220561 (8.32%)                                          Progress: 18508 / 220561 (8.39%)                                          Progress: 18670 / 220561 (8.46%)                                          Progress: 18853 / 220561 (8.55%)                                          Progress: 19030 / 220561 (8.63%)                                          Progress: 19177 / 220561 (8.69%)                                          Progress: 19357 / 220561 (8.78%)                                          Progress: 19532 / 220561 (8.86%)                                          Progress: 19667 / 220561 (8.92%)                                          Progress: 19854 / 220561 (9.00%)                                          Progress: 20046 / 220561 (9.09%)                                          Progress: 20178 / 220561 (9.15%)                                          Progress: 20366 / 220561 (9.23%)                                          Progress: 20558 / 220561 (9.32%)                                          Progress: 20690 / 220561 (9.38%)                                          Progress: 20878 / 220561 (9.47%)                                          Progress: 21070 / 220561 (9.55%)                                          Progress: 21202 / 220561 (9.61%)                                          Progress: 21332 / 220561 (9.67%)                                          Progress: 21490 / 220561 (9.74%)                                          Progress: 21672 / 220561 (9.83%)                                          Progress: 21844 / 220561 (9.90%)                                          Progress: 22005 / 220561 (9.98%)                                          Progress: 22188 / 220561 (10.06%)                                         Progress: 22356 / 220561 (10.14%)                                         Progress: 22519 / 220561 (10.21%)                                         Progress: 22696 / 220561 (10.29%)                                         Progress: 22857 / 220561 (10.36%)                                         Progress: 22984 / 220561 (10.42%)                                         Progress: 23090 / 220561 (10.47%)                                         Progress: 23282 / 220561 (10.56%)                                         Progress: 23443 / 220561 (10.63%)                                         Progress: 23602 / 220561 (10.70%)                                         Progress: 23794 / 220561 (10.79%)                                         Progress: 23951 / 220561 (10.86%)                                         Progress: 24114 / 220561 (10.93%)                                         Progress: 24306 / 220561 (11.02%)                                         Progress: 24434 / 220561 (11.08%)                                         Progress: 24495 / 220561 (11.11%)                                         Progress: 24545 / 220561 (11.13%)                                         Progress: 24574 / 220561 (11.14%)                                         Progress: 24628 / 220561 (11.17%)                                         Progress: 24703 / 220561 (11.20%)                                         Progress: 24771 / 220561 (11.23%)                                         Progress: 24873 / 220561 (11.28%)                                         Progress: 24977 / 220561 (11.32%)                                         Progress: 25039 / 220561 (11.35%)                                         Progress: 25123 / 220561 (11.39%)                                         Progress: 25213 / 220561 (11.43%)                                         Progress: 25342 / 220561 (11.49%)                                         Progress: 25519 / 220561 (11.57%)                                         Progress: 25664 / 220561 (11.64%)                                         Progress: 25772 / 220561 (11.68%)                                         Progress: 25920 / 220561 (11.75%)                                         Progress: 26087 / 220561 (11.83%)                                         Progress: 26168 / 220561 (11.86%)                                         Progress: 26299 / 220561 (11.92%)                                         Progress: 26488 / 220561 (12.01%)                                         Progress: 26555 / 220561 (12.04%)                                         Progress: 26673 / 220561 (12.09%)                                         Progress: 26752 / 220561 (12.13%)                                         Progress: 26848 / 220561 (12.17%)                                         Progress: 27009 / 220561 (12.25%)                                         Progress: 27169 / 220561 (12.32%)                                         Progress: 27219 / 220561 (12.34%)                                         Progress: 27309 / 220561 (12.38%)                                         Progress: 27359 / 220561 (12.40%)                                         Progress: 27442 / 220561 (12.44%)                                         Progress: 27526 / 220561 (12.48%)                                         Progress: 27644 / 220561 (12.53%)                                         Progress: 27753 / 220561 (12.58%)                                         Progress: 27816 / 220561 (12.61%)                                         Progress: 27944 / 220561 (12.67%)                                         Progress: 28048 / 220561 (12.72%)                                         Progress: 28113 / 220561 (12.75%)                                         Progress: 28212 / 220561 (12.79%)                                         Progress: 28281 / 220561 (12.82%)                                         Progress: 28454 / 220561 (12.90%)                                         Progress: 28539 / 220561 (12.94%)                                         Progress: 28570 / 220561 (12.95%)                                         Progress: 28674 / 220561 (13.00%)                                         Progress: 28791 / 220561 (13.05%)                                         Progress: 28927 / 220561 (13.12%)                                         Progress: 29111 / 220561 (13.20%)                                         Progress: 29239 / 220561 (13.26%)                                         Progress: 29431 / 220561 (13.34%)                                         Progress: 29569 / 220561 (13.41%)                                         Progress: 29752 / 220561 (13.49%)                                         Progress: 29905 / 220561 (13.56%)                                         Progress: 30073 / 220561 (13.63%)                                         Progress: 30252 / 220561 (13.72%)                                         Progress: 30416 / 220561 (13.79%)                                         Progress: 30585 / 220561 (13.87%)                                         Progress: 30756 / 220561 (13.94%)                                         Progress: 30918 / 220561 (14.02%)                                         Progress: 31097 / 220561 (14.10%)                                         Progress: 31286 / 220561 (14.18%)                                         Progress: 31450 / 220561 (14.26%)                                         Progress: 31612 / 220561 (14.33%)                                         Progress: 31801 / 220561 (14.42%)                                         Progress: 31971 / 220561 (14.50%)                                         Progress: 32131 / 220561 (14.57%)                                         Progress: 32305 / 220561 (14.65%)                                         Progress: 32456 / 220561 (14.72%)                                         Progress: 32634 / 220561 (14.80%)                                         Progress: 32817 / 220561 (14.88%)                                         Progress: 32952 / 220561 (14.94%)                                         Progress: 33123 / 220561 (15.02%)                                         Progress: 33315 / 220561 (15.10%)                                         Progress: 33474 / 220561 (15.18%)                                         Progress: 33644 / 220561 (15.25%)                                         Progress: 33827 / 220561 (15.34%)                                         Progress: 34019 / 220561 (15.42%)                                         Progress: 34168 / 220561 (15.49%)                                         Progress: 34339 / 220561 (15.57%)                                         Progress: 34531 / 220561 (15.66%)                                         Progress: 34673 / 220561 (15.72%)                                         Progress: 34851 / 220561 (15.80%)                                         Progress: 35043 / 220561 (15.89%)                                         Progress: 35190 / 220561 (15.95%)                                         Progress: 35363 / 220561 (16.03%)                                         Progress: 35555 / 220561 (16.12%)                                         Progress: 35708 / 220561 (16.19%)                                         Progress: 35875 / 220561 (16.27%)                                         Progress: 36067 / 220561 (16.35%)                                         Progress: 36234 / 220561 (16.43%)                                         Progress: 36390 / 220561 (16.50%)                                         Progress: 36579 / 220561 (16.58%)                                         Progress: 36771 / 220561 (16.67%)                                         Progress: 36903 / 220561 (16.73%)                                         Progress: 37091 / 220561 (16.82%)                                         Progress: 37283 / 220561 (16.90%)                                         Progress: 37415 / 220561 (16.96%)                                         Progress: 37603 / 220561 (17.05%)                                         Progress: 37795 / 220561 (17.14%)                                         Progress: 37936 / 220561 (17.20%)                                         Progress: 38118 / 220561 (17.28%)                                         Progress: 38231 / 220561 (17.33%)                                         /VIDEO                (Status: 301) [Size: 310] [--> http://webenum.thm/VIDEO/]  
Progress: 38365 / 220561 (17.39%)                                         Progress: 38557 / 220561 (17.48%)                                         Progress: 38717 / 220561 (17.55%)                                         Progress: 38875 / 220561 (17.63%)                                         Progress: 39066 / 220561 (17.71%)                                         Progress: 39207 / 220561 (17.78%)                                         Progress: 39389 / 220561 (17.86%)                                         Progress: 39578 / 220561 (17.94%)
```
*public,Changes,VIDEO*
Run a directory scan on the host. In the "C******" directory, what file extensions exist?
You'll need to run a scan with the -x flag to look for some of the potentially interesting file types. Don't forget your wordlist!
```text
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://webenum.thm/Changes/ -w /usr/share/wordlists/dirb/common.txt -t 64 -x.php,.html,.conf,.txt,.js,.css,.py
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://webenum.thm/Changes/
[+] Method:                  GET
[+] Threads:                 64
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              conf,txt,js,css,py,php,html
[+] Timeout:                 10s
===============================================================
2022/10/03 17:27:34 Starting gobuster in directory enumeration mode
===============================================================
/.htaccess.html       (Status: 403) [Size: 276]
/.hta.txt             (Status: 403) [Size: 276]
/.htaccess.conf       (Status: 403) [Size: 276]
/.hta.js              (Status: 403) [Size: 276]
/.htaccess            (Status: 403) [Size: 276]
/.hta.css             (Status: 403) [Size: 276]
/.htaccess.txt        (Status: 403) [Size: 276]
/.hta.py              (Status: 403) [Size: 276]
/.htaccess.js         (Status: 403) [Size: 276]
/.hta                 (Status: 403) [Size: 276]
/.htaccess.css        (Status: 403) [Size: 276]
/.htpasswd.html       (Status: 403) [Size: 276]
/.hta.php             (Status: 403) [Size: 276]
/.htaccess.py         (Status: 403) [Size: 276]
/.htpasswd.conf       (Status: 403) [Size: 276]
/.hta.html            (Status: 403) [Size: 276]
/.htaccess.php        (Status: 403) [Size: 276]
/.htpasswd            (Status: 403) [Size: 276]
/.hta.conf            (Status: 403) [Size: 276]
/.htpasswd.txt        (Status: 403) [Size: 276]
/.htpasswd.js         (Status: 403) [Size: 276]
/.htpasswd.css        (Status: 403) [Size: 276]
/.htpasswd.py         (Status: 403) [Size: 276]
/.htpasswd.php        (Status: 403) [Size: 276]
/changes.conf         (Status: 200) [Size: 24] 
                                               
===============================================================
2022/10/03 17:29:29 Finished
```
*conf,js*
![](https://raw.githubusercontent.com/wpscanteam/wpscan/gh-pages/images/wpscan_logo.png)
Introduction to WPScan
First released in June 2011, WPScan has survived the tests of time and stood out as a tool that every pentester should have in their toolkits.
The WPScan framework is capable of enumerating & researching a few security vulnerability categories present in WordPress sites - including - but not limited to:
Sensitive Information Disclosure (Plugin & Theme installation versions for disclosed vulnerabilities or CVE's)
Path Discovery (Looking for misconfigured file permissions i.e. wp-config.php)
Weak Password Policies (Password bruteforcing)
Presence of Default Installation (Looking for default files)
Testing Web Application Firewalls (Common WAF plugins)
Installing WPScan
Thankfully for us, WPScan comes pre-installed on the latest versions of penetration testing systems such as Kali Linux and Parrot. If you are using an older version of Kali Linux (such as 2019) for example, WPScan is in the apt repository, so can be installed by a simple sudo apt update && sudo apt install wpscan
![](https://assets.tryhackme.com/additional/web-enumeration-redux/install-wpscan.png)
﻿Installing WPScan on other operating systems such as Ubuntu or Debian involves extra steps. Whilst the TryHackMe AttackBox comes pre-installed with WPScan, you can follow the [developer's installation guide](https://github.com/jesusgavancho/wpscan) for your local environment.
A Primer on WPScan's Database
WPScan uses information within a local database as a primary reference point when enumerating for themes and plugins. As we'll come to detail later, a technique that WPScan uses when enumerating is looking for common themes and plugins. Before using WPScan, it is highly recommended that you update this database before performing any scans.
Thankfully, this is an easy process to do. Simply run wpscan --update
![](https://assets.tryhackme.com/additional/web-enumeration-redux/update-wpscan.png)
In the next task, we will explore some of the more useful features of WPScan!
We briefly discussed the various things that ﻿WPScan is capable of discovering on a system running WordPress in Task 7. However, let's dive into this a bit further, demonstrate a few examples of the various scans used to retrieve this information and highlighting how these scans work exactly.
Enumerating for Installed Themes
WPScan has a few methods of determining the active theme on a running WordPress installation. At a premise, it boils down to a technique that we can manually do ourselves. Simply, we can look at the assets our web browser loads and then looks for the location of these on the webserver. Using the "Network" tab in your web browsers developer tools, you can see what files are loaded when you visit a webpage.
Take the screenshot below, we can see many assets are loaded, some of these will be scripts & the stylings of the theme that determines how the browser renders the website. Highlighted in the screenshot below is the URL: http://redacted/wp-content/themes/twentytwentyone/assets/
![](https://assets.tryhackme.com/additional/web-enumeration-redux/manual-discover-theme-2.png)
We can take a pretty good guess that the name of the current theme is "twentytwentyone". After inspecting the source code of the website, we can note additional references to "twentytwentyone"
![](https://assets.tryhackme.com/additional/web-enumeration-redux/manual-discover-theme.png)
However, let's use WPScan to speed this process up by using the --enumerate flag with the t argument like so:
wpscan --url http://cmnatics.playground/ --enumerate t
After a couple of minutes, we can begin to see some results:
![](https://assets.tryhackme.com/additional/web-enumeration-redux/enum-themes.png)
The great thing about WPScan is that the tool lets you know how it determined the results it has got. In this case, we're told that the "twentytwenty" theme was confirmed by scanning "Known Locations". The "twentytwenty" theme is the default WordPress theme for WordPress versions in 2020.
Enumerating for Installed Plugins
A very common feature of webservers is "Directory Listing" and is often enabled by default. Simply, "Directory Listing" is the listing of files in the directory that we are navigating to (just as if we were to use Windows Explorer or Linux's ls command. URL's in this context are very similar to file paths. The URL http://cmnatics.playground/a/directory is actually the configured root of the webserver/a/directory:
![](https://assets.tryhackme.com/additional/web-enumeration-redux/webserver-fs.png)
"Directory Listing" occurs when there is no file present that the webserver has been told to process. A very common file is "index.html" and "index.php". As these files aren't present in /a/directory, the contents are instead displayed:
![](https://assets.tryhackme.com/additional/web-enumeration-redux/index2.png)
WPScan can leverage this feature as one technique to look for plugins installed. Since they will all be located in /wp-content/plugins/pluginname, WPScan can enumerate for common/known plugins.
In the screenshot below, "easy-table-of-contents" has been discovered. Great! This could be vulnerable. To determine that, we need to know the version number. Luckily, this handed to us on a plate by WordPress.
![](https://assets.tryhackme.com/additional/web-enumeration-redux/enum-plugins2.png)
Reading through WordPress' developer documentation, we can learn about "[Plugin Readme's](https://developer.wordpress.org/plugins/wordpress-org/how-your-readme-txt-works/#how-the-readme-is-parsed)" to figure out how WPScan determined the version number. Simply, plugins must have a "README.txt" file. This file contains meta-information such as the plugin name, the versions of WordPress it is compatible with and a description.
![](https://assets.tryhackme.com/additional/web-enumeration-redux/example-readme.png)
https://developer.wordpress.org/plugins/wordpress-org/how-your-readme-txt-works/#example-readme
WPScan uses additional methods to discover plugins (such as looking for references or embeds on pages for plugin assets). We can use the --enumerate flag with the p argument like so:
wpscan --url http://cmnatics.playground/ --enumerate p
Enumerating for Users
We've highlighted that WPScan is capable of performing brute-forcing attacks. Whilst we must provide a password list such as rockyou.txt, the way how WPScan enumerates for users is interestingly simple. WordPress sites use authors for posts. Authors are in fact a type of user.
![](https://assets.tryhackme.com/additional/web-enumeration-redux/wordpress-post.png)
And sure enough, this author is picked up by our WPScan:
![](https://assets.tryhackme.com/additional/web-enumeration-redux/enum-users.png)
This scan was performed by using the --enumerate flag with the u argument like so:
wpscan --url http://cmnatics.playground/ --enumerate u
The "Vulnerable" Flag
In the commands so far, we have only enumerated WordPress to discover what themes, plugins and users are present. At the moment, we'd have to look at the output and use sites such as MITRE, NVD and CVEDetails to look up the names of these plugins and the version numbers to determine any vulnerabilities.
WPScan has the v argument for the --enumerate flag. We provide this argument alongside another (such as p for plugins). For example, our syntax would like so: wpscan --url http://cmnatics.playground/ --enumerate vp
Note, that this requires setting up WPScan to use the WPVulnDB API which is out-of-scope for this room.
![](https://assets.tryhackme.com/additional/web-enumeration-redux/vulndb.png)
Performing a Password Attack
After determining a list of possible usernames on the WordPress install, we can use WPScan to perform a bruteforcing technique against the username we specify and a password list that we provide. Simply, we use the output of our username enumeration to build a command like so: wpscan –-url http://cmnatics.playground –-passwords rockyou.txt –-usernames cmnatic
![](https://assets.tryhackme.com/additional/web-enumeration-redux/password-attack.png)
Adjusting WPScan's Aggressiveness (WAF)
Unless specified, WPScan will try to be as least "noisy" as possible. Lots of requests to a web server can trigger things such as firewalls and ultimately result in you being blocked by the server.
This means that some plugins and themes may be missed by our WPScan. Luckily, we can use arguments such as --plugins-detection and an aggressiveness profile (passive/aggressive) to specify this. For example: --plugins-detection aggressive
Summary - Cheatsheet
Flag	Description	Full Example
p	Enumerate Plugins	--enumerate p
t	Enumerate Themes	--enumerate t
u	Enumerate Usernames	--enumerate -u
v	Use WPVulnDB to cross-reference for vulnerabilities. Example command looks for vulnerable plugins (p)	--enumerate vp
aggressive	This is an aggressiveness profile for WPScan to use.	--plugins-detection aggressive
What would be the full URL for the theme "twentynineteen" installed on the WordPress site: "http://cmnatics.playground"
We detail the default location for themes & plugins throughout this task!
*http://cmnatics.playground/wp-content/themes/twentynineteen*
What argument would we provide to enumerate a WordPress site?
We're looking for the keyword here
*enumerate*
What is the name of the other aggressiveness profile that we can use in our WPScan command?
This is more likely to bypass a Web Application Firewall (WAF)
*passive*
Deploy the Instance attached to this task. You will need to add the 10.10.67.130 and domain wpscan.thm to your /etc/hosts file like below:
Replacing "DEPLOYED_INSTANCE_IP_HERE" with 10.10.67.130 and waiting 5 minutes for the Instance to setup before scanning.
![](https://assets.tryhackme.com/additional/web-enumeration-redux/hosts-file2.png)
```text
┌──(root㉿kali)-[/home/kali]
└─# echo '10.10.67.130 wpscan.thm' >> /etc/hosts
```
```text
┌──(kali㉿kali)-[~]
└─$ wpscan --url http://wpscan.thm --enumerate t              
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

[+] URL: http://wpscan.thm/ [10.10.67.130]
[+] Started: Mon Oct  3 18:58:16 2022

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.29 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://wpscan.thm/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://wpscan.thm/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://wpscan.thm/wp-cron.php
