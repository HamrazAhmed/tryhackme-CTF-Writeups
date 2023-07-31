# Flip — Writeup

## Overview
### Flip — Writeup
### Flip — Writeup
----
Hey, do a flip!
----
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/30129d71d291d86c1976d56c3333d8f7.png)
Download Task Files
First, go ahead and review the source code before moving on to Task 2.
You can review the source code by clicking on the Download Task Files button at the top of this task to download the required file.
Answer the questions below
Download the source code.
Completed

## Flags / Answers
- Start Machine
- Log in as the admin and capture the flag!
- If you can...
- Whenever you are ready, click on the **Start Machine** button to fire up the Virtual Machine. Please allow 3-5 minutes for the VM to fully start.
- The server is listening on port 1337 via TCP. You can connect to it using Netcat or any other tool you prefer.
- Answer the questions below
- What is the flag?
```text
- import socketserver 
import socket, os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
from binascii import unhexlify

flag = open('flag','r').read().strip()

def encrypt_data(data,key,iv):
    padded = pad(data.encode(),16,style='pkcs7')
    cipher = AES.new(key, AES.MODE_CBC,iv)
    enc = cipher.encrypt(padded)
    return enc.hex()

def decrypt_data(encryptedParams,key,iv):
    cipher = AES.new(key, AES.MODE_CBC,iv)
    paddedParams = cipher.decrypt( unhexlify(encryptedParams))
    if b'admin&password=sUp3rPaSs1' in unpad(paddedParams,16,style='pkcs7'):
        return 1
    else:
        return 0

def send_message(server, message):
    enc = message.encode()
    server.send(enc)

def setup(server,username,password,key,iv):
        message = 'access_username=' + username +'&password=' + password
        send_message(server, "Leaked ciphertext: " + encrypt_data(message,key,iv)+'\n')
        send_message(server,"enter ciphertext: ")

        enc_message = server.recv(4096).decode().strip()

        try:
                check = decrypt_data(enc_message,key,iv)
        except Exception as e:
                send_message(server, str(e) + '\n')
                server.close()

        if check:
                send_message(server, 'No way! You got it!\nA nice flag for you: '+ flag)
                server.close()
        else:
                send_message(server, 'Flip off!')
                server.close()

def start(server):
        key = get_random_bytes(16)
        iv = get_random_bytes(16)
        send_message(server, 'Welcome! Please login as the admin!\n')
        send_message(server, 'username: ')
        username = server.recv(4096).decode().strip()

        send_message(server, username +"'s password: ")
        password = server.recv(4096).decode().strip()

        message = 'access_username=' + username +'&password=' + password

        if "admin&password=sUp3rPaSs1" in message:
            send_message(server, 'Not that easy :)\nGoodbye!\n')
        else:
            setup(server,username,password,key,iv)

class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        start(self.request)

if __name__ == '__main__':
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 1337), RequestHandler)
    server.serve_forever()

┌──(witty㉿kali)-[/usr/share/wordlists/seclists/Passwords]
└─$ nc 10.10.212.171 1337
Welcome! Please login as the admin!
username: admin
admin's password: sUp3rPaSs1
Not that easy :)
Goodbye!

┌──(witty㉿kali)-[/usr/share/wordlists/seclists/Passwords]
└─$ nc 10.10.212.171 1337
Welcome! Please login as the admin!
username: bdmin
bdmin's password: sUp3rPaSs1
Leaked ciphertext: 51d22bb11e1b8ea82f19c94ee689f3ef868afc48784d1603ce1e18628269cf41167926f553079ed7fa4ce546d43e4273

┌──(witty㉿kali)-[/usr/share/wordlists/seclists/Passwords]
└─$ nc 10.10.212.171 1337
Welcome! Please login as the admin!
username: bdmin
bdmin's password: sUp3rPaSs1
Leaked ciphertext: b8f8ee11c7b25dd536f2a7818c2fbac348a15eed7c0c1f929cc891590f75b7a346b8bab98797c2fe05694d1d49fd20ae
enter ciphertext: b8f8ee11c7b25dd536f2a7818c2fbac348a15eed7c0c1f929cc891590f75b7a346b8bab98797c2fe05694d1d49fd20ae
Flip off! 

CBC (Cipher Block Chaining) mode is a widely used block cipher mode of operation in cryptography. It is used to encrypt data in blocks, where each block is typically 128 bits (16 bytes) in length. CBC mode adds an additional layer of security and prevents patterns from appearing in the encrypted output.

In CBC mode, the plaintext is divided into blocks, and each block is XORed with the previous ciphertext block before encryption. This XOR operation introduces a feedback mechanism, making the encryption of each block dependent on the previous ciphertext block. It helps prevent identical plaintext blocks from producing the same ciphertext blocks, adding a level of diffusion and making it more resistant to certain types of attacks.

Here's a simple example of how CBC mode encryption works:

Suppose we have the following plaintext (16 bytes):

arduinoCopy code

`Plain text:  "Hello, CBC mode!"`

1. Initialization Vector (IV) generation: An Initialization Vector is a random value of the same block size used to start the chaining process. For the first block, there's no previous ciphertext block, so we use an IV. Let's assume the IV is:
