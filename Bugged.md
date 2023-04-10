# Bugged — Writeup

## Overview
### Bugged — Writeup
### Bugged — Writeup
----
John likes to live in a very Internet connected world. Maybe too connected...
---
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/adcc4fe6db75bd8f327a51ea55a770aa.png)
### Analyze the network
Start Machine
John was working on his smart home appliances when he noticed weird traffic going across the network. Can you help him figure out what these weird network communications are?
_Note: the machine may take 3-5 minutes to fully boot._
Answer the questions below

## Enumeration
```text
┌──(witty㉿kali)-[~/Downloads]
└─$ rustscan -a 10.10.240.105 --ulimit 5500 -b 65535 -- -A -Pn
.----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
| {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
| .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
`-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
The Modern Day Port Scanner.
________________________________________
: https://discord.gg/GFrQsGy           :
: https://github.com/RustScan/RustScan :
 --------------------------------------
Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan

[~] The config file is expected to be at "/home/witty/.rustscan.toml"
[~] Automatically increasing ulimit value to 5500.
[!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
Open 10.10.240.105:1883
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
Scanning 10.10.240.105 [1 port]
Discovered open port 1883/tcp on 10.10.240.105
Completed Connect Scan (1 total ports)
Initiating Service scan
Scanning 1 service on 10.10.240.105
Completed Service scan (1 service on 1 host)
NSE: Script scanning 10.10.240.105.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE
Completed NSE
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE
Completed NSE
Nmap scan report for 10.10.240.105
Host is up, received user-set (0.20s latency).

PORT     STATE SERVICE                  REASON  VERSION
1883/tcp open  mosquitto version 2.0.14 syn-ack
| mqtt-subscribe: 
|   Topics and their most recent payloads: 
|     frontdeck/camera: {"id":16866657077475732531,"yaxis":78.33908,"xaxis":28.465668,"zoom":4.663113,"movement":true}
|     $SYS/broker/uptime: 352 seconds
|     $SYS/broker/load/messages/received/15min: 29.40
|     $SYS/broker/messages/sent: 534
|     $SYS/broker/store/messages/bytes: 305
|     $SYS/broker/load/sockets/15min: 0.24
|     $SYS/broker/load/bytes/received/5min: 2936.59
|     $SYS/broker/bytes/sent: 2137
|     $SYS/broker/clients/inactive: -1
|     $SYS/broker/load/sockets/1min: 2.59
|     $SYS/broker/load/messages/sent/5min: 62.53
|     $SYS/broker/load/messages/sent/15min: 29.40
|     storage/thermostat: {"id":17070290351156969688,"temperature":23.033842}
|     $SYS/broker/clients/disconnected: -1
|     $SYS/broker/load/bytes/sent/5min: 250.20
|     $SYS/broker/store/messages/count: 52
|     $SYS/broker/clients/connected: 2
|     patio/lights: {"id":6597963764048772861,"color":"ORANGE","status":"OFF"}
|     $SYS/broker/publish/bytes/received: 17921
|     $SYS/broker/load/messages/sent/1min: 90.20
|     livingroom/speaker: {"id":16598049595873910445,"gain":68}
|     $SYS/broker/load/bytes/sent/15min: 117.65
|     $SYS/broker/messages/received: 534
|     $SYS/broker/load/bytes/received/15min: 1384.31
|     $SYS/broker/bytes/received: 25170
|     $SYS/broker/version: mosquitto version 2.0.14
|     $SYS/broker/clients/active: 2
|     $SYS/broker/load/bytes/received/1min: 4150.03
|     $SYS/broker/messages/stored: 52
|     $SYS/broker/load/messages/received/1min: 90.20
|     $SYS/broker/load/sockets/5min: 0.65
|     $SYS/broker/load/bytes/sent/1min: 360.79
|_    $SYS/broker/load/messages/received/5min: 62.53

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
Nmap done: 1 IP address (1 host up) scanned in 14.68 seconds

https://securitycafe.ro//iot-pentesting-101-how-to-hack-mqtt-the-standard-for-iot-messaging/

┌──(witty㉿kali)-[~/Downloads]
└─$ mosquitto_sub --help                                      
mosquitto_sub is a simple mqtt client that will subscribe to a set of topics and print all messages it receives.
mosquitto_sub version 2.0.11 running on libmosquitto 2.0.11.

Usage: mosquitto_sub {[-h host] [--unix path] [-p port] [-u username] [-P password] -t topic | -L URL [-t topic]}
                     [-c] [-k keepalive] [-q qos] [-x session-expiry-interval]
                     [-C msg_count] [-E] [-R] [--retained-only] [--remove-retained] [-T filter_out] [-U topic ...]
                     [-F format]
                     [-W timeout_secs]
                     [-A bind_address] [--nodelay]
                     [-i id] [-I id_prefix]
                     [-d] [-N] [--quiet] [-v]
                     [--will-topic [--will-payload payload] [--will-qos qos] [--will-retain]]
                     [{--cafile file | --capath dir} [--cert file] [--key file]
                       [--ciphers ciphers] [--insecure]
                       [--tls-alpn protocol]
                       [--tls-engine engine] [--keyform keyform] [--tls-engine-kpass-sha1]]
                       [--tls-use-os-certs]
                     [--psk hex-key --psk-identity identity [--ciphers ciphers]]
                     [--proxy socks-url]
                     [-D command identifier value]
       mosquitto_sub --help

 -A : bind the outgoing socket to this host/ip address. Use to control which interface
      the client communicates over.
 -c : disable clean session/enable persistent client mode
      When this argument is used, the broker will be instructed not to clean existing sessions
      for the same client id when the client connects, and sessions will never expire when the
      client disconnects. MQTT v5 clients can change their session expiry interval with the -x
      argument.
 -C : disconnect and exit after receiving the 'msg_count' messages.
 -d : enable debug messages.
 -D : Define MQTT v5 properties. See the documentation for more details.
 -E : Exit once all subscriptions have been acknowledged by the broker.
 -F : output format.
 -h : mqtt host to connect to. Defaults to localhost.
 -i : id to use for this client. Defaults to mosquitto_sub_ appended with the process id.
 -I : define the client id as id_prefix appended with the process id. Useful for when the
      broker is using the clientid_prefixes option.
 -k : keep alive in seconds for this client. Defaults to 60.
 -L : specify user, password, hostname, port and topic as a URL in the form:
      mqtt(s)://[username[:password]@]host[:port]/topic
 -N : do not add an end of line character when printing the payload.
 -p : network port to connect to. Defaults to 1883 for plain MQTT and 8883 for MQTT over TLS.
 -P : provide a password
 -q : quality of service level to use for the subscription. Defaults to 0.
 -R : do not print stale messages (those with retain set).
 -t : mqtt topic to subscribe to. May be repeated multiple times.
 -T : topic string to filter out of results. May be repeated.
 -u : provide a username
 -U : unsubscribe from a topic. May be repeated.
