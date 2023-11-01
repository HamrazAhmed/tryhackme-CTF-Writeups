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
                                                                                                                                                                       
