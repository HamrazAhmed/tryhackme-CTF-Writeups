# Introduction to Cryptography — Writeup

## Overview
### Introduction to Cryptography — Writeup
### Introduction to Cryptography — Writeup
----
Learn about encryption algorithms such as AES, Diffie-Hellman key exchange, hashing, PKI, and TLS.
---
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/2140d4d554b437c7fb2e7816c259b4fc.png)
### Introduction
The purpose of this room is to introduce users to basic cryptography concepts such as:
-   Symmetric encryption, such as AES
-   Asymmetric encryption, such as RSA
-   Diffie-Hellman Key Exchange
-   Hashing
-   PKI
Suppose you want to send a message that no one can understand except the intended recipient. How would you do that?
One of the simplest ciphers is the Caesar cipher, used more than 2000 years ago. Caesar Cipher shifts the letter by a fixed number of places to the left or to the right. Consider the case of shifting by 3 to the right to encrypt, as shown in the figure below.
The recipient needs to know that the text was shifted by 3 to the right to recover the original message.
Using the same key to encrypt “TRY HACK ME”, we get “WUB KDFN PH”.
The Caesar Cipher that we have described above can use a key between 1 and 25. With a key of 1, each letter is shifted by one position, where A becomes B, and Z becomes A. With a key of 25, each letter is shifted by 25 positions, where A becomes Z, and B becomes A. A key of 0 means no change; moreover, a key of 26 will also lead to no change as it would lead to a full rotation. Consequently, we conclude that Caesar Cipher has a keyspace of 25; there are 25 different keys that the user can choose from.
Consider the case where you have intercepted a message encrypted using Caesar Cipher: “YMNX NX FQUMF GWFAT HTSYFHYNSL YFSLT MTYJQ RNPJ”. We are asked to decrypt it without knowledge of the key. We can attempt this by using brute force, i.e., we can try all the possible keys and see which one makes the most sense. In the following figure, we noticed that key being 5 makes the most sense, “THIS IS ALPHA BRAVO CONTACTING TANGO HOTEL MIKE.”
Caesar cipher is considered a **substitution cipher** because each letter in the alphabet is substituted with another.
Another type of cipher is called **transposition cipher**, which encrypts the message by changing the order of the letters. Let’s consider a simple transposition cipher in the figure below. We start with the message, “THIS IS ALPHA BRAVO CONTACTING TANGO HOTEL MIKE”, and the key `42351`. After we write the letters of our message by filling one column after the other, we rearrange the columns based on the key and then read the rows. In other words, we write by columns and we read by rows. Also notice that we ignored all the space in the plaintext in this example.  The resulting ciphertext “NPCOTGHOTH…” is read one row after the other. In other words, a transposition cipher simply rearranges the order of the letters, unlike the substitution cipher, which substitutes the letters without changing their order.
This task introduced simple substitution and transposition ciphers and applied them to messages made of alphabetic characters. For an encryption algorithm to be considered **secure**, it should be infeasible to recover the original message, i.e., plaintext. (In mathematical terms, we need a **hard** problem, i.e., a problem that cannot be solved in polynomial time. A problem that we can solve in polynomial time is a problem that’s feasible to solve even for large input, although it might take the computer quite some time to finish.)
If the encrypted message can be broken in one week, the encryption used would be considered insecure. However, if the encrypted message can be broken in 1 million years, the encryption would be considered practically secure.
Consider the mono-alphabetic substitution cipher, where each letter is mapped to a new letter. For example, in English, you would map “a” to one of the 26 English letters, then you would map “b” to one of the remaining 25 English letters, and then map “c” to one of the remaining 24 English letters, and so on.
For example, we might choose the letters in the alphabet “abcdefghijklmnopqrstuvwxyz” to be mapped to “xpatvrzyjhecsdikbfwunqgmol” respectively. In other words, “a” becomes “x”, “b” becomes “p”, and so on. The recipient needs to know the key, “xpatvrzyjhecsdikbfwunqgmol”, to decrypt the encrypted messages successfully.
This algorithm might look very secure, especially since trying all the possible keys is not feasible. However, different techniques can be used to break a ciphertext using such an encryption algorithm. One weakness of such an algorithm is letter frequency. In English texts, the most common letters are ‘e’, ‘t’, and ‘a’, as they appear at a frequency of 13%, 9.1%, and 8.2%, respectively. Moreover, in English texts, the most common first letters are ‘t’, ‘a’, and ‘o’, as they appear at 16%, 11.7% and 7.6%, respectively. Add to this the fact that most of the message words are dictionary words, and you will be able to break an encrypted text with the alphabetic substitution cipher in no time.
We don’t really need to use the encryption key to decrypt the received ciphertext, “Uyv sxd gyi siqvw x sinduxjd pvzjdw po axffojdz xgxo wsxcc wuidvw.” As shown in the figure below, using a website such as [quipqiup](https://www.quipqiup.com/), it will take a moment to discover that the original text was “The man who moves a mountain begins by carrying away small stones.” This example clearly indicates that this algorithm is broken and should not be used for confidential communication.
Answer the questions below
You have received the following encrypted message:
_“Xjnvw lc sluxjmw jsqm wjpmcqbg jg wqcxqmnvw; xjzjmmjd lc wjpm sluxjmw jsqm bqccqm zqy.” Zlwvzjxj Zpcvcol_
You can guess that it is a quote. Who said it?
Use quipqiup
“Today is victory over yourself of yesterday; tomorrow is your victory over lesser men.” Miyamoto Musashi
*Miyamoto Musashi*
```text
1.  Symmetric encryption, such as AES, uses a single key to encrypt and decrypt data. This means that the same key is used for both encryption and decryption, and the key must be securely exchanged between the sender and recipient.
    
2.  Asymmetric encryption, such as RSA, uses two keys: a public key and a private key. The public key is used to encrypt data, while the private key is used to decrypt it. This allows for secure communication even if the public key is publicly available.
    
3.  Diffie-Hellman Key Exchange is a method for securely exchanging keys over an insecure channel. It allows two parties to establish a shared secret key that can be used for encryption and decryption.
    
4.  Hashing is a one-way function that takes an input and produces a fixed-length output, called a hash. Hashes are commonly used for verifying the integrity of data, since even a small change in the input will result in a completely different output hash.
    
5.  PKI (Public Key Infrastructure) refers to the set of rules, policies, and procedures needed to create, manage, distribute, use, store, and revoke digital certificates, which are used to authenticate parties and to secure data transmission over networks.
```
### Symmetric Encryption
Download Task Files
Let’s review some terminology:
-   **Cryptographic Algorithm** or **Cipher**: This algorithm defines the encryption and decryption processes.
-   **Key**: The cryptographic algorithm needs a key to convert the plaintext into ciphertext and vice versa.
-   **plaintext** is the original message that we want to encrypt
-   **ciphertext** is the message in its encrypted form
A symmetric encryption algorithm uses the same key for encryption and decryption. Consequently, the communicating parties need to agree on a secret key before being able to exchange any messages.
In the following figure, the sender provides the _encrypt_ process with the plaintext and the key to get the ciphertext. The ciphertext is usually sent over some communication channel.
On the other end, the recipient provides the _decrypt_ process with the same key used by the sender to recover the original plaintext from the received ciphertext. Without knowledge of the key, the recipient won’t be able to recover the plaintext.
National Institute of Standard and Technology (NIST) published the Data Encryption Standard (DES) in 1977. DES is a symmetric encryption algorithm that uses a key size of 56 bits. In 1997, a challenge to break a message encrypted using DES was solved. Consequently, it was demonstrated that it had become feasible to use a brute-force search to find the key and break a message encrypted using DES. In 1998, a DES key was broken in 56 hours. These cases indicated that DES could no longer be considered secure.
NIST published the Advanced Encryption Standard (AES) in 2001. Like DES, it is a symmetric encryption algorithm; however, it uses a key size of 128, 192, or 256 bits, and it is still considered secure and in use today. AES repeats the following four transformations multiple times:
1.  `SubBytes(state)`: This transformation looks up each byte in a given substitution table (S-box) and substitutes it with the respective value. The `state` is 16 bytes, i.e., 128 bits, saved in a 4 by 4 array.
2.  `ShiftRows(state)`: The second row is shifted by one place, the third row is shifted by two places, and the fourth row is shifted by three places. This is shown in the figure below.
3.  `MixColumns(state)`: Each column is multiplied by a fixed matrix (4 by 4 array).
4.  `AddRoundKey(state)`: A round key is added to the state using the XOR operation.
The total number of transformation rounds depends on the key size.
Don’t worry if you find this cryptic because it is! Our purpose is not to learn the details of how AES works nor to implement it as a programming library; the purpose is to appreciate the difference in complexity between ancient encryption algorithms and modern ones. If you are curious to dive into details, you can check the AES specifications, including pseudocode and examples in its published standard, [FIPS PUB 197](https://csrc.nist.gov/publications/detail/fips/197/final).
In addition to AES, many other symmetric encryption algorithms are considered secure. Here is a list of symmetric encryption algorithms supported by GPG (GnuPG) 2.37.7, for example:
Encryption Algorithm
Notes
AES, AES192, and AES256
AES with a key size of 128, 192, and 256 bits
IDEA
International Data Encryption Algorithm (IDEA)
3DES
Triple DES (Data Encryption Standard) and is based on DES. We should note that 3DES will be deprecated in 2023 and disallowed in 2024.
CAST5
Also known as CAST-128. Some sources state that CASE stands for the names of its authors: Carlisle Adams and Stafford Tavares.
BLOWFISH
Designed by Bruce Schneier
TWOFISH
Designed by Bruce Schneier and derived from Blowfish
CAMELLIA128, CAMELLIA192, and CAMELLIA256
Designed by Mitsubishi Electric and NTT in Japan. Its name is derived from the flower camellia japonica.
All the algorithms mentioned so far are block cipher symmetric encryption algorithms. A block cipher algorithm converts the input (plaintext) into blocks and encrypts each block. A block is usually 128 bits. In the figure below, we want to encrypt the plaintext “TANGO HOTEL MIKE”, a total of 16 characters. The first step is to represent it in binary. If we use ASCII, “T” is `0x54` in hexadecimal format, “A” is `0x41`, and so on. Every two hexadecimal digits constitute 8 bits and represent one byte. A block of 128 bits is practically 16 bytes and is represented in a 4 by 4 array. The 128-bit block is fed as one unit to the encryption method.
The other type of symmetric encryption algorithm is stream ciphers, which encrypt the plaintext byte by byte. Consider the case where we want to encrypt the message “TANGO HOTEL MIKE”; each character needs to be converted to its binary representation. If we use ASCII, “T” is `0x54` in hexadecimal, while “A” is `0x41`, and so on. The encryption method will process one byte at a time. This is represented in the figure below.
Symmetric encryption solves many security problems discussed in the [Security Principles](https://tryhackme.com/room/securityprinciples) room. Let’s say that Alice and Bob met and chose an encryption algorithm and agreed on a specific key. We assume that the selected encryption algorithm is secure and that the secret key is kept safe. Let’s take a look at what we can achieve:
-   **Confidentiality**: If Eve intercepted the encrypted message, she wouldn’t be able to recover the plaintext. Consequently, all messages exchanged between Alice and Bob are confidential as long as they are sent encrypted.
-   **Integrity**: When Bob receives an encrypted message and decrypts it successfully using the key he agreed upon with Alice, Bob can be sure that no one could tamper with the message across the channel. When using secure modern encryption algorithms, any minor modification to the ciphertext would prevent successful decryption or would lead to gibberish as plaintext.
-   **Authenticity**: Being able to decrypt the ciphertext using the secret key also proves the authenticity of the message because only Alice and Bob know the secret key.
We are just getting started, and we know how to maintain confidentiality, check the integrity and ensure the authenticity of the exchanged messages. More practical and efficient approaches will be presented in later tasks. The question, for now, is whether this is scalable.
With Alice and Bob, we needed one key. If we have Alice, Bob, and Charlie, we need three keys: one for Alice and Bob, another for Alice and Charlie, and a third for Bob and Charlie. However, the number of keys grows quickly; communication between 100 users requires almost 5000 different secret keys. (If you are curious about the mathematics behind it, that’s 99 + 98 + 97 + … + 1 = 4950).
Moreover, if one system gets compromised, they need to create new keys to be used with the other 99 users. Another problem would be finding a secure channel to exchange the keys with all the other users. Obviously, this quickly grows out of hand.
In the next task, we will cover asymmetric encryption. One of the problems solved with asymmetric encryption is when 100 users only need to share a total of 100 keys to communicate securely. (As explained earlier, symmetric encryption would require around 5000 keys to secure the communications for 100 users.)
There are many programs available for symmetric encryption. We will focus on two, which are widely used for asymmetric encryption as well:
-   GNU Privacy Guard
-   OpenSSL Project
### GNU Privacy Guard
The [GNU Privacy Guard](https://gnupg.org/), also known as GnuPG or GPG, implements the OpenPGP standard.
We can encrypt a file using GnuPG (GPG) using the following command:
`gpg --symmetric --cipher-algo CIPHER message.txt`, where CIPHER is the name of the encryption algorithm. You can check supported ciphers using the command `gpg --version`. The encrypted file will be saved as `message.txt.gpg`.
The default output is in the binary OpenPGP format; however, if you prefer to create an ASCII armoured output, which can be opened in any text editor, you should add the option `--armor`. For example, `gpg --armor --symmetric --cipher-algo CIPHER message.txt`.
You can decrypt using the following command:
`gpg --output original_message.txt --decrypt message.gpg`
### OpenSSL Project
The [OpenSSL Project](https://www.openssl.org/) maintains the OpenSSL software.
We can encrypt a file using OpenSSL using the following command:
`openssl aes-256-cbc -e -in message.txt -out encrypted_message`
We can decrypt the resulting file using the following command:
`openssl aes-256-cbc -d -in encrypted_message -out original_message.txt`
To make the encryption more secure and resilient against brute-force attacks, we can add `-pbkdf2` to use the Password-Based Key Derivation Function 2 (PBKDF2); moreover, we can specify the number of iterations on the password to derive the encryption key using `-iter NUMBER`. To iterate 10,000 times, the previous command would become:
`openssl aes-256-cbc -pbkdf2 -iter 10000 -e -in message.txt -out encrypted_message`
Consequently, the decryption command becomes:
`openssl aes-256-cbc -pbkdf2 -iter 10000 -d -in encrypted_message -out original_message.txt`
In the following questions, we will use `gpg` and `openssl` on the AttackBox to carry out symmetric encryption.
The necessary files for this task are located under `/root/Rooms/cryptographyintro/task02`. **The zip file attached to this task can be used to tackle the questions of tasks 2, 3, 4, 5, and 6**.
Answer the questions below
```scss
https://lasec.epfl.ch/memo/memo_des.shtml

Deep Crack Machine by Paul Kocher

The plaintext is a 16-byte (128-bit) block represented by the hexadecimal values: `01 23 45 67 89 AB CD EF FE DC BA 98 76 54 32 10`.

The round key is also a 16-byte (128-bit) block represented by the hexadecimal values: `10 20 30 40 50 60 70 80 90 A0 B0 C0 D0 E0 F0 00`.

To perform the AddRoundKey operation, we perform an XOR operation between each corresponding byte of the plaintext and the round key:

01 (plaintext)
10 (round key)
--------- (XOR)
11 (ciphertext)

23 (plaintext)
20 (round key)
--------- (XOR)
03 (ciphertext)

45 (plaintext)
30 (round key)
--------- (XOR)
75 (ciphertext)

...

BA (plaintext)
A0 (round key)
--------- (XOR)
1A (ciphertext)

76 (plaintext)
70 (round key)
--------- (XOR)
06 (ciphertext)

54 (plaintext)
60 (round key)
--------- (XOR)
34 (ciphertext)

32 (plaintext)
50 (round key)
--------- (XOR)
22 (ciphertext)

10 (plaintext)
00 (round key)
--------- (XOR)
10 (ciphertext)

So, the final ciphertext produced by the AddRoundKey operation is: `11 03 75 27 D9 CB BD 4F EE 5C 1A 06 34 22 10`.

In the example, the binary representation of the hexadecimal values is used to perform the XOR operation. The XOR operation is performed bit-by-bit, so:

54 (plaintext in binary: 0101 0100)
60 (round key in binary: 0110 0000)
--------- (XOR)
34 (ciphertext in binary: 0011 0100)

32 (plaintext in binary: 0011 0010)
50 (round key in binary: 0101 0000)
--------- (XOR)
22 (ciphertext in binary: 0001 0010)

After the XOR operation, the binary result is converted back to hexadecimal to get the final ciphertext. The binary value `0011 0100` is equivalent to the hexadecimal value `34`, and the binary value `0001 0010` is equivalent to the hexadecimal value `22`.
```
```text
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task02]
└─$ gpg --version                                                                                      
gpg (GnuPG) 2.2.40
libgcrypt 1.10.1
Copyright (C) 2022 g10 Code GmbH
License GNU GPL-3.0-or-later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Home: /home/witty/.gnupg
Supported algorithms:
Pubkey: RSA, ELG, DSA, ECDH, ECDSA, EDDSA
Cipher: IDEA, 3DES, CAST5, BLOWFISH, AES, AES192, AES256, TWOFISH,
        CAMELLIA128, CAMELLIA192, CAMELLIA256
Hash: SHA1, RIPEMD160, SHA256, SHA384, SHA512, SHA224
Compression: Uncompressed, ZIP, ZLIB, BZIP2
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task02]
└─$ ls
quote01.txt.gpg  quote02  quote03.txt.gpg
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task02]
└─$ echo 'god' > msg.txt                          
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task02]
└─$ ls
msg.txt  quote01.txt.gpg  quote02  quote03.txt.gpg

┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task02]
└─$ gpg --symmetric --cipher-algo AES256 msg.txt    
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task02]
└─$ ls
msg.txt  msg.txt.gpg  quote01.txt.gpg  quote02  quote03.txt.gpg

┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task02]
└─$ gpg --output original_message.txt --decrypt msg.txt.gpg 
gpg: AES256.CFB encrypted data
gpg: encrypted with 1 passphrase
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task02]
└─$ cat original_message.txt 
god

┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task02]
└─$ echo 'live' > msg2.txt
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task02]
└─$ ls
msg2.txt  msg.txt  msg.txt.gpg  original_message.txt  quote01.txt.gpg  quote02  quote03.txt.gpg

┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task02]
└─$ openssl aes-256-cbc -pbkdf2 -iter 10000 -e -in msg2.txt -out encrypted_message
enter AES-256-CBC encryption password:
Verifying - enter AES-256-CBC encryption password:
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task02]
└─$ openssl aes-256-cbc -pbkdf2 -iter 10000 -d -in encrypted_message -out original_message2.txt
enter AES-256-CBC decryption password:
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task02]
└─$ cat original_message2.txt 
live

┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task02]
└─$ gpg --output original_quote01.txt --decrypt quote01.txt.gpg
gpg: AES256.CFB encrypted data
gpg: encrypted with 1 passphrase
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task02]
└─$ cat original_quote01.txt 
Do not waste time idling or thinking after you have set your goals.
Miyamoto Musashi

┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task02]
└─$ openssl aes-256-cbc -d -in quote02 -out original_message_quote02.txt
enter AES-256-CBC decryption password:
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task02]
└─$ cat original_message_quote02.txt 
The true science of martial arts means practicing them in such a way that they will be useful at any time, and to teach them in such a way that they will be useful in all things.
Miyamoto Musashi

┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task02]
└─$ gpg --output original_quote03.txt --decrypt quote03.txt.gpg        
gpg: CAMELLIA256.CFB encrypted data
gpg: encrypted with 1 passphrase
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task02]
└─$ cat original_quote03.txt 
You must understand that there is more than one path to the top of the mountain.
Miyamoto Musashi
```
![[Pasted image 20230213152033.png]]
Decrypt the file `quote01` encrypted (using AES256) with the key `s!kR3T55` using `gpg`. What is the third word in the file?
*waste*
Decrypt the file `quote02` encrypted (using AES256-CBC) with the key `s!kR3T55` using `openssl`. What is the third word in the file?
*science*
Decrypt the file `quote03` encrypted (using CAMELLIA256) with the key `s!kR3T55` using `gpg`. What is the third word in the file?
*understand*
### Asymmetric Encryption
Symmetric encryption requires the users to find a secure channel to exchange keys. By secure channel, we are mainly concerned with confidentiality and integrity. In other words, we need a channel where no third party can eavesdrop and read the traffic; moreover, no one can change the sent messages and data.
Asymmetric encryption makes it possible to exchange encrypted messages without a secure channel; we just need a reliable channel. By reliable channel, we mean that we are mainly concerned with the channel’s integrity and not confidentiality.
When using an asymmetric encryption algorithm, we would generate a key pair: a public key and a private key. The public key is shared with the world, or more specifically, with the people who want to communicate with us securely. The private key must be saved securely, and we must never let anyone access it. Moreover, it is not feasible to derive the private key despite the knowledge of the public key.
How does this key pair work?
If a message is encrypted with one key, it can be decrypted with the other. In other words:
-   If Alice encrypts a message using Bob’s public key, it can be decrypted only using Bob’s private key.
-   Reversely, if Bob encrypts a message using his private key, it can only be decrypted using Bob’s public key.
### Confidentiality
We can use asymmetric encryption to achieve confidentiality by encrypting the messages using the recipient’s public key. In the following two figures, we can see that:
Alice wants to ensure confidentiality in her communication with Bob. She encrypts the message using Bob’s public key, and Bob decrypts them using his private key. Bob’s public key is expected to be published on a public database or on his website, for instance.
When Bob wants to reply to Alice, he encrypts his messages using Alice’s public key, and Alice can decrypt them using her private key.
In other words, it becomes easy to communicate with Alice and Bob while ensuring the confidentiality of the messages. The only requirement is that all parties have their public keys available for interested senders.
Note: In practice, symmetric encryption algorithms allow faster operations than asymmetric encryption; therefore, we will cover later how we can use the best of both worlds.
### Integrity, Authenticity, and Nonrepudiation
Beyond confidentiality, asymmetric encryption can solve integrity, authenticity and nonrepudiation. Let’s say that Bob wants to make a statement and wants everyone to be able to confirm that this statement indeed came from him. Bob needs to encrypt the message using his private key; the recipients can decrypt it using Bob’s public key. If the message decrypts successfully with Bob’s public key, it means that the message was encrypted using Bob’s private key. (In practice, he would encrypt a hash of the original message. We will elaborate on this later.)
Being decrypted successfully using Bob’s public key leads to a few interesting conclusions.
-   First, the message was not altered across the way (communication channel); this proves the message _integrity_.
-   Second, knowing that no one has access to Bob’s private key, we can be sure that this message did indeed come from Bob; this proves the message _authenticity_.
-   Finally, because no one other than Bob has access to Bob’s private key, Bob cannot deny sending this message; this establishes _nonrepudiation_.
We have seen how asymmetric encryption can help establish confidentiality, integrity, authenticity, and nonrepudiation. In real-life scenarios, asymmetric encryption can be relatively slow to encrypt large files and vast amounts of data. In another task, we will see how we can use asymmetric encryption in conjunction with symmetric encryption to achieve these security objectives relatively faster.
### RSA
RSA got its name from its inventors, Rivest, Shamir, and Adleman. It works as follows:
1.  Choose two random prime numbers, _p_ and _q_. Calculate _N_ = _p_ × _q_.
2.  Choose two integers _e_ and _d_ such that _e_ × _d_ = 1 mod _ϕ_(_N_), where _ϕ_(_N_) = _N_ − _p_ − _q_ + 1. This step will let us generate the public key (_N_,_e_) and the private key (_N_,_d_).
3.  The sender can encrypt a value _x_ by calculating _y_ = _x__e_ mod _N_. (Modulus)
4.  The recipient can decrypt _y_ by calculating _x_ = _y__d_ mod _N_. Note that _y__d_ = _x__e__d_ = _x__k__ϕ_(_N_) + 1 = (_x__ϕ_(_N_))_k_ × _x_ = _x_. This step explains why we put a restriction on the choice of _e_ and _d_.
Don’t worry if the above mathematical equations looked too complicated; you don’t need mathematics to be able to use RSA, as it is readily available via programs and programming libraries.
RSA security relies on factorization being a hard problem. It is easy to multiply _p_ by _q_; however, it is time-consuming to find _p_ and _q_ given _N_. Moreover, for this to be secure, _p_ and _q_ should be pretty large numbers, for example, each being 1024 bits (that’s a number with more than 300 digits). It is important to note that RSA relies on secure random number generation, as with other asymmetric encryption algorithms. If an adversary can guess _p_ and _q_, the whole system would be considered insecure.
Let’s consider the following practical example.
1.  Bob chooses two prime numbers: _p_ = 157 and _q_ = 199. He calculates _N_ = 31243.
2.  With _ϕ_(_N_) = _N_ − _p_ − _q_ + 1 = 31243 − 157 − 199 + 1 = 30888, Bob selects _e_ = 163 and _d_ = 379 where _e_ × _d_ = 163 × 379 = 61777 and 61777 mod 30888 = 1. The public key is (31243,163) and the private key is (31243,379).
3.  Let’s say that the value to encrypt is _x_ = 13, then Alice would calculate and send _y_ = _x__e_ mod _N_ = 13163 mod 31243 = 16342.
4.  Bob will decrypt the received value by calculating _x_ = _y__d_ mod _N_ = 16341379 mod 31243 = 13.
The previous example was to understand the mathematics behind it better. To see real values for _p_ and _q_, let’s create a real keypair using a tool such as `openssl`.
Terminal
```shell-session
user@TryHackMe$ openssl genrsa -out private-key.pem 2048

user@TryHackMe$ openssl rsa -in private-key.pem -pubout -out public-key.pem
writing RSA key

user@TryHackMe$ cat public-key.pem
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAymcAeYg1ohPQLHu7u9l1
UutN8bCP7r6czRX2zrQrpElYrm5mHERi1xweWEhTJ/0Q13FJcHLGtLbdQc0rGpOd
DnYJBuzrqXU2hC7E7dlqLsj63NPADqlOGYCGCWnm/HGM2WuVtDXqRitN4zeNKEWI
QmEctfucopZx5AVJ1vTn+qMv/0D6QU7Mm65MTSYg1SCRA0D0N9NLMj4rYlLOIr5q
5g3iunAE4tCROMcHf7fxWMuWdJTdtxTv7+4P5XGkWrWriO22JFHp9N22Fm96V9jH
7aASRkIZvQFmx+1dl7btZDhsm2ezU07LBabv9efj0gIwz6P3mTJVm+wxaDH6jiXB
dwIDAQAB
-----END PUBLIC KEY-----

user@TryHackMe$ openssl rsa -in private-key.pem -text -noout
Private-Key: (2048 bit, 2 primes)
modulus:
    00:ca:67:00:79:88:35:a2:13:d0:2c:7b:bb:bb:d9:
    75:52:eb:4d:f1:b0:8f:ee:be:9c:cd:15:f6:ce:b4:
    2b:a4:49:58:ae:6e:66:1c:44:62:d7:1c:1e:58:48:
    53:27:fd:10:d7:71:49:70:72:c6:b4:b6:dd:41:cd:
    2b:1a:93:9d:0e:76:09:06:ec:eb:a9:75:36:84:2e:
    c4:ed:d9:6a:2e:c8:fa:dc:d3:c0:0e:a9:4e:19:80:
    86:09:69:e6:fc:71:8c:d9:6b:95:b4:35:ea:46:2b:
    4d:e3:37:8d:28:45:88:42:61:1c:b5:fb:9c:a2:96:
    71:e4:05:49:d6:f4:e7:fa:a3:2f:ff:40:fa:41:4e:
    cc:9b:ae:4c:4d:26:20:d5:20:91:03:40:f4:37:d3:
    4b:32:3e:2b:62:52:ce:22:be:6a:e6:0d:e2:ba:70:
    04:e2:d0:91:38:c7:07:7f:b7:f1:58:cb:96:74:94:
    dd:b7:14:ef:ef:ee:0f:e5:71:a4:5a:b5:ab:88:ed:
    b6:24:51:e9:f4:dd:b6:16:6f:7a:57:d8:c7:ed:a0:
    12:46:42:19:bd:01:66:c7:ed:5d:97:b6:ed:64:38:
    6c:9b:67:b3:53:4e:cb:05:a6:ef:f5:e7:e3:d2:02:
    30:cf:a3:f7:99:32:55:9b:ec:31:68:31:fa:8e:25:
    c1:77
publicExponent: 65537 (0x10001)
privateExponent:
    10:fe:00:be:33:3f:3d:72:28:61:f3:a9:59:25:f2:
    81:99:9b:9b:94:d5:20:98:04:15:fb:a8:12:c6:71:
    7b:83:64:dc:90:0c:26:87:5f:3c:eb:f1:68:3b:fa:
    2f:3b:41:b4:b4:a0:13:be:af:0b:f0:e6:36:66:01:
    1e:64:12:25:6a:a7:6b:5b:6c:95:77:6f:b2:3d:32:
    ef:3c:f7:7b:22:08:5d:8d:b1:6c:09:ae:b2:d9:65:
    67:58:ea:b9:7a:d6:f6:51:df:e9:97:35:29:da:ec:
    d9:0c:8a:df:3c:a7:29:db:79:4b:95:ea:1a:84:42:
    df:7f:ca:29:2f:ba:62:02:37:05:c0:b0:c2:ff:42:
    6b:fb:e1:36:40:10:ae:11:0f:d8:87:2f:fe:10:2e:
    a4:60:de:ff:fe:c8:ab:0b:29:fa:6c:20:ec:87:33:
    46:c0:cd:96:36:cb:9b:ca:81:17:e5:c3:eb:34:b2:
    83:0f:52:cc:e9:68:bd:cb:d2:85:2f:fe:c4:47:76:
    df:94:69:ce:7b:8a:50:71:36:96:e6:35:fb:fb:b4:
    4a:ac:63:9b:9d:1b:bb:32:71:31:45:a2:25:33:cc:
    f7:a5:fb:9f:66:b1:4e:30:ce:9d:71:e8:fa:7d:5f:
    33:a0:c1:94:0a:b7:b7:f3:16:7e:4f:ad:89:3d:ba:
    51
prime1:
    00:e0:3d:87:b3:d3:1f:d2:c6:66:23:83:a5:95:d5:
    20:35:f8:d8:c0:94:cf:cc:d2:04:d4:e4:ef:cf:c2:
    94:00:10:cd:d1:4a:df:09:4e:7e:95:f8:70:08:b1:
    20:98:8a:e3:88:f7:cc:a8:32:62:32:68:f6:1f:c0:
    fb:c1:71:41:8c:21:a3:ff:20:e6:96:d0:6e:4b:66:
    61:08:d0:b7:26:48:27:62:a7:d3:ff:36:55:c8:e1:
    ab:91:48:90:fb:b5:b1:92:be:90:06:a8:40:1b:2a:
    2d:53:1e:87:fc:a7:8a:57:72:0b:e5:35:71:7b:dd:
    8c:e5:b5:ab:64:7c:37:c5:0d
prime2:
    00:e7:11:ac:50:f5:dc:16:cf:20:46:77:5d:ca:16:
    29:36:35:89:95:c0:f8:4b:42:ef:03:a0:f1:ce:2e:
    1b:da:55:a9:ff:5a:28:4d:78:c5:8a:e2:55:9b:94:
    b4:56:ec:ab:1b:dd:b8:07:be:dd:d5:0f:49:90:b3:
    ed:a2:d7:78:38:24:d5:9e:7d:a2:e8:8c:e0:2a:33:
    32:21:1f:0e:6b:aa:0b:b4:11:6a:bd:8f:d9:86:3f:
    ad:42:c8:bc:42:23:21:39:8d:0c:60:f2:ca:2a:00:
    0a:8e:de:fb:1a:3c:51:9d:f2:dc:0a:59:80:d6:a4:
    47:5c:02:a3:d0:30:1d:47:93
[...]
```
We executed three commands:
-   `openssl genrsa -out private-key.pem 2048`: With `openssl`, we used `genrsa` to generate an RSA private key. Using `-out`, we specified that the resulting private key is saved as `private-key.pem`. We added `2048` to specify a key size of 2048 bits.
-   `openssl rsa -in private-key.pem -pubout -out public-key.pem`: Using `openssl`, we specified that we are using the RSA algorithm with the `rsa` option. We specified that we wanted to get the public key using `-pubout`. Finally, we set the private key as input using `-in private-key.pem` and saved the output using `-out public-key.pem`.
-   `openssl rsa -in private-key.pem -text -noout`: We are curious to see real RSA variables, so we used `-text -noout`. The values of _p_, _q_, _N_, _e_, and _d_ are `prime1`, `prime2`, `modulus`, `publicExponent`, and `privateExponent`, respectively.
If we already have the recipient’s public key, we can encrypt it with the command `openssl pkeyutl -encrypt -in plaintext.txt -out ciphertext -inkey public-key.pem -pubin`
The recipient can decrypt it using the command `openssl pkeyutl -decrypt -in ciphertext -inkey private-key.pem -out decrypted.txt`
Answer the questions below
```scss
Sure! The RSA algorithm is a method for securely transmitting information. It works by creating two keys - a public key and a private key.

First, two random prime numbers, p and q, are chosen. Then, the product of those two numbers, N, is calculated.

Next, two integers, e and d, are chosen such that e * d is equal to 1 when divided by a value calculated from N. This value is called "phi(N)" and is equal to N - p - q + 1.

The public key is a pair of values (N, e) and is used to encrypt a message. The recipient of the message can then use their private key, which is a pair of values (N, d), to decrypt the message.

The reason this works is because of the mathematical property that the encryption and decryption calculations follow, specifically the one where (x^e)^d is equal to x (mod N). This means that if you encrypt a message using the public key, only someone with the matching private key can properly decrypt it.

The number of digits in an RSA key is a direct representation of its size in bits. Each digit in a decimal representation of a number represents a power of 10, and each power of 10 can be represented by 4 bits of binary data.

So, a 300-digit decimal number would be approximately 1200 bits in size, which is close to the 1024-bit key size that was commonly used in the past.

In general, the number of digits in a decimal representation of an RSA key can be calculated as:

`number of digits = (size of key in bits) / (bits per digit)`

where `bits per digit` is typically taken as 4.

┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task03/pkey_and_prkey]
└─$ openssl genrsa -out private-key.pem 2048
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task03/pkey_and_prkey]
└─$ ls
private-key.pem
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task03/pkey_and_prkey]
└─$ openssl rsa -in private-key.pem -pubout -out public-key.pem
writing RSA key
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task03/pkey_and_prkey]
└─$ ls
private-key.pem  public-key.pem

──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task03/pkey_and_prkey]
└─$ cat private-key.pem     
-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCOJksWnzy49Xdy
/MTn0LzF5fl2ZCt617XxNKXSyUbv2YCWN5kxDtgXIbzkGOBZMRS5d/VE3a96/mBi
.....

fW1muNM0HyIX1ZZhCsjNlQ==
-----END PRIVATE KEY-----
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task03/pkey_and_prkey]
└─$ cat public-key.pem 
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAjiZLFp88uPV3cvzE59C8
xeX5dmQrete18TSl0slG79mAljeZMQ7YFyG85BjgWTEUuXf1RN2vev5gYpC/u/KB
sg1aF4dvWsWBx9xDJbwsOFtx0PAjmxa6BFHbvRH4fcyU+qYq468cDY6MMA3fu08U
ZJRksX1iqULU2436cvvwv2V4s+FXRBrI4U8DB/VJi03jltxXHfrhappTwVTh01NL
VV54eqxasPAhTrVuqx5IDgd7aq7FRi40YA19uNNLrPe6H5wHYGmKz0eW5NOdRbjx
QLZyfvXhLwQpbZ6ZWp1x++IGp5hY43o5Ohhnqd1HZq0/KAqHgqPDiJgKNlH+6wLD
owIDAQAB
-----END PUBLIC KEY-----

┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task03/pkey_and_prkey]
└─$ openssl rsa -in private-key.pem -text -noout
Private-Key: (2048 bit, 2 primes)
modulus:
    00:8e:26:4b:16:9f:3c:b8:f5:77:72:fc:c4:e7:d0:
    bc:c5:e5:f9:76:64:2b:7a:d7:b5:f1:34:a5:d2:c9:
    46:ef:d9:80:96:37:99:31:0e:d8:17:21:bc:e4:18:
    e0:59:31:14:b9:77:f5:44:dd:af:7a:fe:60:62:90:
    bf:bb:f2:81:b2:0d:5a:17:87:6f:5a:c5:81:c7:dc:
    43:25:bc:2c:38:5b:71:d0:f0:23:9b:16:ba:04:51:
    db:bd:11:f8:7d:cc:94:fa:a6:2a:e3:af:1c:0d:8e:
    8c:30:0d:df:bb:4f:14:64:94:64:b1:7d:62:a9:42:
    ...
publicExponent: 65537 (0x10001)
privateExponent:
    3b:29:15:cc:32:f6:b7:35:b6:02:7d:cf:c7:78:f8:
    ef:d6:20:46:55:37:41:57:80:8a:04:32:d5:70:de:
    9c:99:25:aa:9f:36:1b:14:45:fc:0e:97:0a:49:8e:
    29:a0:c3:32:d3:89:99:21:38:54:d4:84:b1:d0:f3:
    73:59:e0:ff:85:0e:0f:47:d7:20:ec:9d:70:5c:2b:
    f8:0b:02:4e:6c:44:88:c4:40:d5:5d:96:8a:90:b5:
    06:d1:f1:5d:0d:e5:9d:11:c6:3c:df:56:aa:0f:bf:
    29:8a:c4:a8:34:a7:d4:9a:6b:f3:f0:ae:bc:aa:2b:
    ...
prime1:
    00:bb:56:8a:64:00:0e:06:9f:fc:0c:5e:b9:7e:ee:
    a1:4b:af:50:07:ff:55:da:ae:da:4a:74:e1:3a:ba:
    cf:7c:13:fe:02:25:fc:c1:23:fa:73:55:36:cd:a9:
    1c:3f:eb:d6:05:72:e2:3e:7b:de:f4:ea:ce:48:15:
    94:b7:79:9b:16:b4:84:af:ae:b3:07:63:9f:82:4c:
    ...
prime2:
    00:c2:3f:d5:10:18:a4:23:39:7a:33:e7:28:4c:61:
    45:ff:46:33:00:7f:76:be:9f:bc:42:68:d5:5f:e7:
    e7:5f:f2:42:13:b2:20:15:ec:af:af:03:49:0e:b5:
    b9:62:5b:73:2a:5d:c0:15:cd:7b:29:8f:57:d2:e0:
    8c:e3:1d:4d:b8:13:3b:42:4b:99:31:e3:a7:31:31:
    ...
exponent1:
    48:bb:5c:97:5e:7e:13:8c:61:6a:dc:0b:e0:7f:fd:
    17:49:45:25:15:b8:db:62:2f:55:e0:f2:e0:be:4e:
    77:b9:bb:50:52:37:43:35:18:b3:56:4e:24:a2:97:
    59:29:d2:b9:e2:d4:7b:b5:d3:e5:fa:93:83:e0:fd:
    10:0e:a2:6b:ba:42:19:83:15:f6:b4:72:e5:3f:69:
    ..
exponent2:
    2a:2a:55:03:a3:75:ad:b7:c2:51:15:f2:67:72:0e:
    11:b5:99:48:98:62:9c:4a:6c:41:36:24:6b:27:19:
    d0:77:f3:e3:f6:9c:84:65:d6:54:f5:2f:9c:a3:d1:
    d4:09:e9:db:de:71:dd:c9:b6:dc:74:a3:29:c1:58:
    93:cc:3e:9c:a0:80:12:89:fa:7d:1b:df:a5:0c:20:
    ...
coefficient:
    26:c8:a7:5f:ff:70:6c:15:b8:fc:86:da:ee:7b:50:
    9e:3d:26:9b:02:f4:7a:2e:4a:92:e9:f3:70:b0:fc:
    19:2d:1c:a2:52:95:e8:4b:a0:05:e6:ce:26:8e:0b:
    0a:04:c8:99:93:a7:ab:65:11:ba:3a:1e:b1:f2:34:
    bb:ea:45:3a:57:65:f6:97:48:d4:1f:8a:e7:b3:de:
    ...

┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task03/pkey_and_prkey]
└─$ echo 'go=d' > plaintext.txt

┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task03/pkey_and_prkey]
└─$ openssl pkeyutl -encrypt -in plaintext.txt -out ciphertext -inkey public-key.pem -pubin
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task03/pkey_and_prkey]
└─$ cat ciphertext 
�ȼO�5��7�š�WU����;�n>��^q�N��x9{�j��}K��s�vO�������@������F4N��1�0:�V些:!�-�̬�����ݫ��X�B�#,C	˒�"PGc�4G`;}���lM���.��U�:
����>UL4�Z�DR<��yZ���}�Zj
                         �FjIdw@���
kn�y�VRo.�`�D�D��&��ck
                      `X��������+��ՏW�T����V�  

┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task03/pkey_and_prkey]
└─$ openssl pkeyutl -decrypt -in ciphertext -inkey private-key.pem -out decrypted.txt
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task03/pkey_and_prkey]
└─$ cat decrypted.txt 
go=d

┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task03]
└─$ ls
ciphertext_message  pkey_and_prkey  private-key-bob.pem  public-key-alice.pem  public-key-bob.pem
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task03]
└─$ openssl pkeyutl -decrypt -in ciphertext_message -inkey private-key-bob.pem -out decrypted.txt
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task03]
└─$ cat decrypted.txt 
"Perception is strong and sight weak. In strategy it is important to see distant things as if they were close and to take a distanced view of close things."
Miyamoto Musashi

┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task03]
└─$ openssl rsa -in private-key-bob.pem -text -noout
Private-Key: (2048 bit, 2 primes)
modulus:
    00:e8:5e:73:7d:54:55:0a:cc:56:64:87:b3:4b:8e:
    24:df:96:b8:b9:5f:19:d4:71:a5:b9:5a:a8:d9:ab:
    b4:7b:7f:59:08:c5:9c:47:0d:73:92:97:b8:ef:67:
    b7:a6:5a:59:2c:e3:4c:ca:7f:53:1c:9e:34:32:0e:
    c6:7c:60:b2:d6:1f:30:b2:ed:da:14:e9:15:78:80:
    71:92:3c:26:32:a9:2b:3a:15:4e:48:2d:93:04:a5:
    21:c7:da:15:6c:dd:bc:89:0e:cc:54:be:84:d6:40:
    b8:47:59:d1:b2:27:c9:0d:43:55:de:33:dd:01:8f:
    bf:6c:3e:79:31:dd:e4:90:8d:c3:35:72:31:85:15:
    ae:ac:5a:96:c8:34:90:0e:32:4e:86:45:55:78:fb:
    13:ed:a4:fb:f0:64:b4:61:04:f6:7c:e3:56:aa:03:
    a3:43:1e:40:0b:98:1f:73:66:4a:5c:3a:25:69:2c:
    d9:92:f8:69:c1:5b:61:b7:f2:3a:68:28:e9:2b:75:
    08:9c:a4:63:9e:71:2b:63:aa:99:75:cf:78:00:23:
    fc:5a:df:2d:95:14:2f:e6:10:5d:a0:ff:4d:07:c8:
    d3:bb:2d:8f:0d:8a:fc:ab:43:5d:35:53:dc:72:a2:
    74:5b:c0:88:0d:ee:c3:1f:7b:1c:74:1a:5e:e1:c1:
    88:31
publicExponent: 65537 (0x10001)
privateExponent:
    02:3b:3b:4b:58:ce:a2:eb:e8:bd:ce:65:1f:b4:9d:
    bb:5d:41:d3:85:e0:ee:f3:fd:c3:69:e6:1f:db:a6:
    40:09:59:06:dc:89:98:fa:68:17:0a:f3:46:59:43:
    4a:35:a9:3a:e5:1e:8c:fd:ec:03:ba:56:85:f9:de:
    58:be:14:f9:8e:bd:c8:fa:15:13:5e:54:4b:c9:45:
    4d:ec:db:46:61:44:28:ff:f6:0b:26:0f:8e:06:87:
    ec:83:60:f1:4a:af:cf:76:74:ea:86:14:80:7a:33:
    f5:7b:71:fd:63:f9:bf:9c:30:96:e6:fd:ed:a5:e9:
    10:ab:b3:93:91:ad:ea:e0:17:99:e8:7b:3d:64:58:
    b1:74:3e:0e:81:5b:6d:fa:41:7a:23:26:4f:f1:24:
    a8:73:f3:36:24:a2:65:17:7d:5b:52:8e:1f:fc:b7:
    e6:53:bc:89:b0:e5:18:65:71:29:34:cb:f7:65:51:
    39:0c:62:33:24:b8:60:bf:89:8b:c8:f5:0d:7d:e5:
    85:cf:57:cf:c3:d8:44:10:8f:54:6c:04:99:8d:d7:
    fd:e2:74:18:7b:5c:6c:3c:e1:30:0a:8b:8b:55:70:
    88:8a:67:64:63:5c:65:8f:fa:92:cf:94:04:b9:8d:
    53:28:bb:31:d8:31:3c:4c:06:cd:b6:17:e9:51:d8:
    81
prime1:
    00:ff:ea:65:3e:e5:96:96:0b:66:55:f1:f9:d0:37:
    66:e9:35:a5:c3:43:ca:66:75:40:49:46:8d:85:a7:
    ff:f4:73:97:69:11:a1:1e:37:f9:e3:38:cb:c0:5e:
    56:e9:1a:0d:f2:9f:80:56:87:2a:99:bb:88:8e:93:
    35:5a:9a:c6:f7:99:44:90:88:09:33:a6:0d:ea:b4:
    56:98:66:20:9c:34:e7:b9:33:64:4f:08:01:08:62:
    44:68:8f:df:79:0d:84:2b:77:e7:03:8b:3c:7a:e3:
    e0:e0:ee:23:64:22:51:ed:dd:b8:1c:b3:75:c4:3f:
    4a:cf:fc:7c:57:0b:95:75:e7
prime2:
    00:e8:72:11:5c:b5:5c:14:19:85:ce:e7:d2:e9:54:
    7b:58:ae:32:e9:e6:39:a7:65:b4:90:2f:53:b5:9d:
    22:62:84:fe:52:86:f5:01:a2:9c:b0:4f:80:ee:d4:
    07:27:3b:69:02:70:33:da:7d:97:56:b9:3e:f3:a1:
    84:9e:73:6a:47:e5:99:8c:44:86:75:c1:bf:71:89:
    06:b0:ee:dd:16:45:e7:05:fa:02:bd:e6:3e:b7:f2:
    fe:e7:22:0b:ed:ca:23:a0:68:0b:fe:fb:c3:57:19:
    21:58:6e:73:1d:9d:3c:2a:8a:c1:7e:ea:73:67:5a:
    cb:3d:a8:9b:be:50:08:9e:27
exponent1:
    1e:20:56:c8:df:b8:29:73:b0:19:60:01:fb:8b:fa:
    16:6c:15:56:76:4d:86:60:39:30:27:19:13:e9:e2:
    0c:c1:ea:ca:18:a4:31:ed:7f:02:4b:b6:58:b0:02:
    65:30:87:01:cf:db:08:d4:a2:a4:34:5a:70:06:4e:
    5a:9b:2b:df:0b:f0:f1:5e:c2:4e:8d:36:c8:31:70:
    9c:42:31:86:92:07:d1:5a:86:6d:73:50:c3:ce:e5:
    a4:b5:83:26:39:fc:1c:2d:e2:49:1d:84:02:27:7f:
    5a:9b:4e:19:44:9d:06:76:7a:6d:0e:87:47:91:f7:
    d9:a2:2c:75:06:cd:12:73
exponent2:
    28:a9:f3:e1:9d:14:9b:ab:8f:5e:0f:ee:34:c5:83:
    c2:92:ce:f3:5e:44:4d:c5:9c:1d:f1:39:9a:b6:ff:
    91:ee:a4:33:39:ca:d8:db:62:bf:f1:58:a3:ef:51:
    c5:0a:3e:a7:9f:8b:62:b8:bf:e5:fb:08:49:44:c3:
    57:98:e7:49:e6:9f:c3:0b:25:de:a9:e3:5c:f0:54:
    cc:55:2d:36:3d:4a:5a:20:4f:a4:7b:08:13:d4:1d:
    c5:bf:8e:08:ae:69:27:21:ac:9f:91:d9:ad:7e:06:
    f8:5a:72:27:07:1f:c4:6d:7b:c6:41:2b:a9:34:18:
    04:14:60:12:9e:1b:b3:d7
coefficient:
    6e:69:83:47:fb:63:da:cc:a5:bb:98:e6:ff:a5:18:
    06:d2:7d:17:19:26:d7:bc:7a:72:13:5a:e3:7e:bc:
    e4:6b:ba:5c:ad:fd:b5:df:73:a0:2f:53:c4:70:f0:
    21:5b:86:13:46:96:ab:2e:4c:e1:c9:63:d0:13:73:
    9f:90:d8:20:59:3a:23:86:cf:1a:03:3b:4a:21:da:
    e8:77:28:3e:41:70:df:07:6e:7f:c0:25:6d:84:26:
    18:18:bc:78:07:2c:05:1f:b6:b8:73:38:c6:2b:ce:
    56:e7:e2:ff:12:bd:06:c4:0a:a6:f4:36:d1:cf:93:
    a6:d5:75:d3:22:b7:3b:3a

┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task03]
└─$ cat public-key-alice.pem 
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyaqi9VqzjTMeEVs8Oz+8
ZuAJRqckyP+Mxny4aS0s0u1SrCG5qpUAbhxZY8+iBbM0ZaHaVKmP6LdWkBfWHM2k
pZZqzSp56rPl9GRAp27x1kiFjdMGG9M7wdGXpOpAvy25QEmbcqRg7AAaf2WMWTVB
3TygmgOqaJo7xnodpBxlvfuoFvfnITVA+nuBe36aX7ledN6FjEW0Zz56UELLIIsV
SnQQMncLiMDrPldOuYUX/H+HS+jTudpcagxMpSmXRRJhzg3T0U/GUGOOAyigxqMs
tQyraSjiOeBegwvg/ibkbEha4tqloDpenjw40IlPNxcr2I/TdGlz8b1MBJ6K6+Eb
dQIDAQAB
-----END PUBLIC KEY-----
                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task03]
└─$ cat public-key-bob.pem 
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA6F5zfVRVCsxWZIezS44k
35a4uV8Z1HGluVqo2au0e39ZCMWcRw1zkpe472e3plpZLONMyn9THJ40Mg7GfGCy
1h8wsu3aFOkVeIBxkjwmMqkrOhVOSC2TBKUhx9oVbN28iQ7MVL6E1kC4R1nRsifJ
DUNV3jPdAY+/bD55Md3kkI3DNXIxhRWurFqWyDSQDjJOhkVVePsT7aT78GS0YQT2
fONWqgOjQx5AC5gfc2ZKXDolaSzZkvhpwVtht/I6aCjpK3UInKRjnnErY6qZdc94
ACP8Wt8tlRQv5hBdoP9NB8jTuy2PDYr8q0NdNVPccqJ0W8CIDe7DH3scdBpe4cGI
MQIDAQAB
-----END PUBLIC KEY-----
```
On the AttackBox, you can find the directory for this task located at `/root/Rooms/cryptographyintro/task03`; alternatively, you can use the task file from Task 2 to work on your own machine.
Bob has received the file `ciphertext_message` sent to him from Alice. You can find the key you need in the same folder. What is the first word of the original plaintext?
Decrypt with Bob’s private key.
*Perception*
Take a look at Bob’s private RSA key. What is the last byte of _p_?
p is prime1. The answer should be two hexadecimal digits.
*e7*
Take a look at Bob’s private RSA key. What is the last byte of _q_?
q is prime2. The answer should be two hexadecimal digits.
*27*
### Diffie-Hellman Key Exchange
Alice and Bob can communicate over an insecure channel. By insecure, we mean that there are eavesdroppers who can read the messages exchanged on this channel. How can Alice and Bob agree on a secret key in such a setting? One way would be to use the Diffie-Hellman key exchange.
Diffie-Hellman is an asymmetric encryption algorithm. It allows the exchange of a secret over a public channel. We will skip the modular arithmetic background and provide a simple numeric example. We will need two mathematical operations: power and modulus. _x__p_, i.e., _x_ raised to the power _p_, is _x_ multiplied by itself _p_ times. Furthermore, _x_ mod _m_, i.e., _x_ modulus _m_, is the remainder of the division of _x_ by _m_.
1.  Alice and Bob agree on _q_ and _g_. For this to work, _q_ should be a prime number, and _g_ is a number smaller than _q_ that satisfies certain conditions. (In modular arithmetic, _g_ is a generator.) In this example, we take _q_ = 29 and _g_ = 3.
2.  Alice chooses a random number _a_ smaller than _q_. She calculates _A_ = (_g__a_) mod _q_. The number _a_ must be kept a secret; however, _A_ is sent to Bob. Let’s say that Alice picks the number _a_ = 13 and calculates _A_ = 313%29 = 19 and sends it to Bob.
3.  Bob picks a random number _b_ smaller than _q_. He calculates _B_ = (_g__b_) mod _q_. Bob must keep _b_ a secret; however, he sends _B_ to Alice. Let’s consider the case where Bob chooses the number _b_ = 15 and calculates _B_ = 315%29 = 26. He proceeds to send it to Alice.
4.  Alice receives _B_ and calculates _k__e__y_ = _B__a_ mod _q_. Numeric example _k__e__y_ = 2613 mod 29 = 10.
5.  Bob receives _A_ and calculates _k__e__y_ = _A__b_ mod _q_. Numeric example _k__e__y_ = 1915 mod 29 = 10.
We can see that Alice and Bob reached the same key.
Although an eavesdropper has learned the values of _q_, _g_, _A_, and _B_, they won’t be able to calculate the secret _k__e__y_ that Alice and Bob have exchanged. The above steps are summarized in the figure below.
Although the numbers we have chosen make it easy to find _a_ and _b_, even without using a computer, real-world examples would select a _q_ of 256 bits in length. In decimal numbers, that’s 115 with 75 zeroes to its right (I don’t know how to read that either, but I was told it is read as 115 quattuorvigintillion). Such a large _q_ will make it infeasible to find _a_ or _b_ despite knowledge of _q_, _g_, _A_, and _B_.
Let’s take a look at actual Diffie-Hellman parameters. We can use `openssl` to generate them; we need to specify the option `dhparam` to indicate that we want to generate Diffie-Hellman parameters along with the specified size in bits, such as `2048` or `4096`.
In the console output below, we can view the prime number `P` and the generator `G` using the command `openssl dhparam -in dhparams.pem -text -noout`. (This is similar to what we did with the RSA private key.)
Terminal
```shell-session
user@TryHackMe$ openssl dhparam -out dhparams.pem 2048
Generating DH parameters, 2048 bit long safe prime
[...]
```
```shell-session
$ openssl dhparam -in dhparams.pem -text -noout
    DH Parameters: (2048 bit)
    P:   
        00:82:3b:9d:b5:29:31:f8:12:fe:21:e1:90:30:37:
        ac:d2:48:41:f7:d7:55:e5:d2:5d:dd:87:67:9e:bd:
        b3:97:df:05:a9:d2:d9:56:4f:66:b5:d9:d8:65:06:
        58:c3:8f:b3:0e:30:d2:9a:0b:c3:0a:56:8d:fc:0f:
        f2:e2:9e:4f:16:16:93:4e:b9:a4:c3:9c:09:2d:48:
        a2:ec:b6:97:92:63:a3:b4:75:36:3f:51:77:ca:ac:
        44:6d:99:eb:4d:4a:97:d5:4b:52:c8:07:f8:16:30:
        37:d3:b2:47:30:e6:4e:bc:6a:53:d1:9b:6a:4d:91:
        7a:4b:4f:af:3b:f0:ce:b9:ed:91:4d:8b:52:5a:3f:
        bb:6b:06:ae:32:95:7d:53:da:9b:ce:b0:ec:7d:81:
        25:05:d8:ce:ca:76:e7:d1:5a:31:13:d2:9f:62:b4:
        d5:ad:7d:cd:c9:ab:3d:28:e3:92:27:9f:f3:66:a0:
        be:61:49:cc:47:21:d8:e0:2c:e8:c6:35:4b:2f:ba:
        35:36:8f:bb:41:c6:89:b2:60:3c:62:bb:fe:bf:59:
        d3:7f:05:69:55:dc:61:1b:b4:bb:68:fa:65:1e:2e:
        46:2f:2d:21:62:d1:9f:a0:2b:aa:81:df:3a:f9:7d:
        0b:9d:0e:47:68:01:4f:6e:81:cc:4c:2a:91:fc:8c:
        f4:6f
    G:    2 (0x2)
```
Diffie-Hellman key exchange algorithm allows two parties to agree on a secret over an insecure channel. However, the discussed key exchange is prone to a Man-in-the-Middle (MitM) attack; an attacker might reply to Alice pretending to be Bob and reply to Bob pretending to be Alice. We discuss a solution to this problem in Task 6.
Answer the questions below
```cs
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task04]
└─$ openssl dhparam -out dhparams2.pem 2048
Generating DH parameters, 2048 bit long safe prime
..............+......................................................+.................................................................................................................................................................................................................................+.........................................+............................................................................+...........+.................................................................................................+.....................................................................................................................................................................................................................................................................+....................................................................+.................................................................+.......................................................................................+......................+.+..+....................................................................................................................................................................................................................................................................................................................................................................................................................................................................+........................+...............................................................................................+.....................................................+............................................................................................................................................................+.......................................................+...................................................................................................................+.+...............+.................................................................................+......................................+................................................................................................................................................................................................................................................................................................................................................................................+...............................................................................+....................................................................................................................................................................................................................................................................................................+..........................................+...............................................+.............................................................................................................+........................................................................+......................................................................................................+........................................................................................+.................+....................................................+..................................................................................................................................................+.....................................................................................................................................................................................................+...............................................................................................................................................................................................................................................................................................................................................................+......................................................................................................................................................................................................................+.............................................................................................................................................................+.............................................+.............................................+..............................................................................+..................................+................................................................................................................................................+...............................................................................................................................................................................................................................+................................................................................+...........................................................................................+...................................................................................................................................................................................................................................+...............+..............+....................................................................................................................+...............................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................+...+...........................................................+.....................................................................+...............................................................................................................................................................................+............................................................................+......................................................+................................................................+.....................+......+.......................+...............+......+.......................................................................................................................................................................................................................................................................+..................................................................................................+.........................................+........+.......................................................................................................................................................................................................................................+...........................................+......................+...................................................................................................................................+.......................................................................................+.................................................................................................................+.................................................................................................+...................................+...............................................................................................................................................................+...............................................................................................+....................+........................................................................................+.....................+.....................................................................................................................+..............................................................................................................................................................................................................................................................................+...............................................................................................................................................................................................................................................................................................................................+...........................................................................................................................................................................................................................................................................................................+........................................................+......................+..............................................................................................................+.................+.........+..............................................................................................................................................................................................+...................................+..........................+...................................................................+................................................................+..................................................................................................................................................................................................................................................................................................................................................................................+...+....................................................................................................+..................................................................................................+.....+.........................................................................................................................................................+..+...................................................................................................................+.....+.........................................................................................................................+..........+...................................................................................................................................................................................................................................+................................................................................................................................................................................................................++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*

┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task04]
└─$ openssl dhparam -in dhparams2.pem -text -noout
    DH Parameters: (2048 bit)
    P:   
        00:c5:72:44:6e:2d:62:d0:cb:a3:fd:ee:f3:e1:c0:
        ec:e6:1d:85:1d:a8:94:de:e7:2f:36:00:51:e4:3d:
        1e:23:d7:6c:90:8c:d0:22:ee:a5:99:db:1d:94:4a:
        c4:16:80:90:8a:da:63:88:c8:d2:22:94:4a:a7:a2:
        63:6b:dd:6d:5d:06:3c:fa:cb:d2:88:e6:fa:eb:0f:
        4c:1f:a9:75:c6:52:ce:2a:31:24:52:36:9f:3e:9d:
        92:32:72:9d:c2:d2:2b:68:d1:ea:21:0a:17:26:b6:
        7f:c7:f8:73:36:f0:51:b5:36:f4:e5:77:f4:59:75:
        9e:32:59:2a:bf:75:7f:a0:ff:d5:ad:a9:ea:58:b4:
        1f:c2:13:29:43:b1:1c:e7:37:09:14:ab:c1:d4:c9:
        21:8d:f7:90:5b:a8:31:3f:8e:62:80:45:c1:b5:64:
        73:5b:0b:e7:8d:e4:39:e2:a1:50:98:23:cf:dc:de:
        a3:d5:6c:61:bf:86:f1:0c:a3:df:7d:bc:26:f6:35:
        1a:72:81:c6:61:63:5d:b8:cb:4d:32:a1:5b:b6:84:
        fa:c3:6d:e5:19:0f:d7:a3:8d:1c:81:36:00:f7:47:
        9f:1f:41:7e:2d:44:50:bf:4d:a6:9f:c8:2e:74:c1:
        94:35:22:01:0f:ea:af:51:c1:05:4e:af:57:4f:0f:
        08:3f
    G:    2 (0x2)

                                                                                                                                                                       
┌──(witty㉿kali)-[~/Downloads/intro-to-cryptography/task04]
└─$ openssl dhparam -in dhparams.pem -text -noout 
    DH Parameters: (4096 bit)
    P:   
        00:c0:10:65:c6:ad:ed:88:04:88:1e:e7:50:1b:30:
        0f:05:2c:2d:d4:ea:60:44:9e:2a:f7:90:02:89:a4:
        7e:05:99:32:38:dc:75:50:0a:c7:f6:6b:f7:b4:9a:
        df:ef:ca:e0:ce:55:5d:31:48:3e:9c:35:5a:ad:03:
        9c:87:d7:1c:48:e4:2e:29:dc:a3:90:81:23:7f:fa:
        30:5c:fb:d8:62:7b:96:35:ef:9a:0f:84:49:c4:48:
        97:b5:63:38:91:01:49:f1:42:15:fd:da:84:a6:90:
        4d:2d:05:10:41:cf:06:53:52:80:eb:1b:11:ad:5d:
        63:ed:fe:b1:f7:a7:60:1c:79:b8:88:54:a3:e4:64:
        4d:d3:04:a7:d5:76:17:00:d4:44:19:d6:12:a9:1f:
        aa:2b:ac:73:d6:52:50:92:17:a9:cd:f6:b0:ee:55:
        57:a4:db:82:6e:4f:00:20:6f:6f:f5:b1:72:97:b0:
        c5:3a:88:47:86:c6:e5:dd:fc:91:2f:82:08:05:0c:
        5c:c2:f8:62:92:67:9e:f1:53:24:c0:76:f1:3d:0c:
        50:31:5b:56:26:0a:3b:05:a3:b7:be:f9:ee:a4:82:
        f8:9d:46:ab:a9:dd:b9:04:25:61:58:aa:2a:bb:7c:
        2c:c8:e1:ef:ac:f9:50:e3:64:2e:30:9c:fd:48:26:
        25:7e:75:c0:56:58:10:8d:d7:61:b4:df:f7:ce:bd:
        9c:ef:6f:8b:47:8c:0e:cf:29:ab:eb:33:56:17:99:
        19:ee:30:5f:d9:9d:80:6e:3c:91:05:e6:cd:55:ca:
        25:f2:e3:d9:c8:68:74:1d:9e:4a:e7:53:25:1f:17:
        27:3f:4e:29:c2:19:83:da:4d:8f:b5:6b:5c:de:67:
        4f:01:10:48:84:99:32:c0:e5:e0:8b:9f:eb:4e:18:
        f7:ff:c6:47:b1:47:b8:b2:7f:3c:9c:bd:93:c2:71:
        b3:b4:37:fc:ad:2e:d9:af:2d:2c:f9:de:7f:42:8b:
        39:21:d7:47:8f:18:c4:de:ad:70:0b:11:79:c4:df:
        ef:0f:3a:9a:af:85:4e:95:05:ca:35:9e:6d:93:9b:
        e4:66:23:78:2b:d9:f4:47:e4:fe:29:1e:aa:cb:95:
        66:a2:f2:2a:c3:5a:fa:c0:a0:7d:53:bd:74:37:1d:
        b1:c7:66:67:b7:7b:5f:32:bc:2f:fa:82:0a:12:15:
        2f:41:10:cd:12:70:cc:ee:29:e7:1c:b7:07:d4:28:
        1f:73:3c:15:c0:a2:1d:2b:db:07:57:f7:10:28:c7:
        ed:e4:3a:69:c4:d9:4f:0f:c2:b4:4a:97:2a:2c:b3:
        75:77:5e:1a:21:94:8c:85:fb:0d:5e:95:0f:c8:72:
        59:6c:4f
    G:    2 (0x2)
```
On the AttackBox, you can find the directory for this task located at `/root/Rooms/cryptographyintro/task04`; alternatively, you can use the task file from Task 2 to work on your own machine.
A set of Diffie-Hellman parameters can be found in the file `dhparam.pem`. What is the size of the prime number in bits?
*4096*
What is the prime number’s last byte (least significant byte)?
The answer is two hexadecimal digits.
*4f*
### Hashing
A cryptographic hash function is an algorithm that takes data of arbitrary size as its input and returns a fixed size value, called _message digest_ or _checksum_, as its output. For example, `sha256sum` calculates the SHA256 (Secure Hash Algorithm 256) message digest. SHA256, as the name indicates, returns a checksum of size 256 bits (32 bytes). This checksum is usually written using hexadecimal digits. Knowing that a hexadecimal digit represents 4 bits, the 256 bits checksum can be represented as 64 hexadecimal digits.
In the terminal output below, we calculate the SHA256 hash values for three files of varying sizes: 4 bytes, 275 MB, and 5.2 GB. Using `sha256sum` to calculate the message digest for each of the three files, we get three completely different values that appear random. It is worth stressing that the length of the resulting message digest or checksum is the same, no matter how small or big the file is. In particular, the four-byte file `abc.txt` and the 5.2 GB file resulted in message digests of equal length independent of the file size.
Terminal
```shell-session
user@TryHackMe$ ls -lh
total 5.5G
-rw-r--r--. 1 strategos strategos    4  7月 21 12:46 abc.txt
-rw-r--r--. 1 strategos strategos 275M  2月 12 19:08 debian-hurd.img.tar.xz
-rw-r--r--. 1 strategos strategos 5.2G  4月 26 16:55 Win11_English_x64v1.iso
```
```shell-session
$ sha256sum *
c38bb113c89d8fec6475a9936411007c45563ecb7ce8acd5db7fb58c0872bda0  abc.txt
0317ff0150e0d64b70284b28c97bb788310585ea7ac46cc8139d5a3c850dea55  debian-hurd.img.tar.xz
4bc6c7e7c61af4b5d1b086c5d279947357cff45c2f82021bb58628c2503eb64e  Win11_English_x64v1.iso
```
But why would we need such a function? There are many uses, in particular:
-   Storing passwords: Instead of storing passwords in plaintext, a hash of the password is stored instead. Consequently, if a data breach occurs, the attacker will get a list of password hashes instead of the original passwords. (In practice, passwords are also “salted”, as discussed in a later task.)
-   Detecting modifications: Any minor modification to the original file would lead to a drastic change in hash value, i.e. checksum.
In the following terminal output, we have two files, `text1.txt` and `text2.txt`, which are almost identical except for (literally) one bit being different; the letters `T` and `t` are different in one bit in their ASCII representation. Even though we have flipped only a single bit, it is evident that the SHA256 checksums are entirely different. Consequently, if we use a secure hash function algorithm, we can easily confirm whether any modifications have taken place. This can help protect against both intentional tampering and file transfer errors.
Terminal
```shell-session
user@TryHackMe$ hexdump text1.txt -C
00000000  54 72 79 48 61 63 6b 4d  65 0a                    |TryHackMe.|
0000000a
```
```shell-session
$ hexdump text2.txt -C
00000000  74 72 79 48 61 63 6b 4d  65 0a                    |tryHackMe.|
0000000a
```
```shell-session
$ sha256sum text1.txt
f4616fd825a10ded9af58fbaee09f3e31751d15591f9323ea68b03a0e8ac3783  text1.txt
```
```shell-session
$ sha256sum text2.txt
9ffa3533ee33998aeb1df76026f8031c8af6ccabd8393eca002d5b7471a0b536  text2.txt
```
Some of the hashing algorithms in use and still considered secure are:
-   SHA224, SHA256, SHA384, SHA512
-   RIPEMD160
Some older hash functions, such as MD5 (Message Digest 5) and SHA-1, are cryptographically broken. By broken, we mean that it is possible to generate a different file with the same checksum as a given file. This means that we can create a hash collision. In other words, an attacker can create a new message with a given checksum, and detecting file or message tampering won’t be possible.
### HMAC
Hash-based message authentication code (HMAC) is a message authentication code (MAC) that uses a cryptographic key in addition to a hash function.
According to [RFC2104](https://www.rfc-editor.org/rfc/rfc2104), HMAC needs:
-   secret key
-   inner pad (ipad) a constant string. (RFC2104 uses the byte `0x36` repeated B times. The value of B depends on the chosen hash function.)
-   outer pad (opad) a constant string. (RFC2104 uses the byte `0x5C` repeated B times.)
Calculating the HMAC follows the following steps as shown in the figure:
1.  Append zeroes to the key to make it of length B, i.e., to make its length match that of the ipad.
2.  Using bitwise exclusive-OR (XOR), represented by ⊕, calculate _k__e__y_ ⊕ _i__p__a__d_.
3.  Append the message to the XOR output from step 2.
4.  Apply the hash function to the resulting stream of bytes (in step 3).
5.  Using XOR, calculate _k__e__y_ ⊕ _o__p__a__d_.
6.  Append the hash function output from step 4 to the XOR output from step 5.
7.  Apply the hash function to the resulting stream of bytes (in step 6) to get the HMAC.
The figure above represents the steps expressed in the following formula: _H_(_K_⊕_o__p__a__d_,_H_(_K_⊕_i__p__a__d_,_t__e__x__t_)).
To calculate the HMAC on a Linux system, you can use any of the available tools such as `hmac256` (or `sha224hmac`, `sha256hmac`, `sha384hmac`, and `sha512hmac`, where the secret key is added after the option `--key`). Below we show an example of calculating the HMAC using `hmac256` and `sha256hmac` with two different keys.
Terminal
```shell-session
user@TryHackMe$ hmac256 s!Kr37 message.txt
3ec65b7e80c5bf2e623e52e0528f1c6a74f605b10616621ba1c22a89fb244e65  message.txt

user@TryHackMe$ hmac256 1234 message.txt
4b6a2783631180fca6128592e3d17fb5bff6b0e563ad8f1c6afc1050869e440f  message.txt
