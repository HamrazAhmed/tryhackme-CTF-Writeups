---
Put your Zeek skills into practice and analyse network traffic.
---

# Zeek Exercises — Writeup

## Overview
### Zeek Exercises — Writeup
### Zeek Exercises — Writeup
### Anomalous DNS
An alert triggered: "Anomalous DNS Activity".
The case was assigned to you. Inspect the PCAP and retrieve the artefacts to confirm this alert is a true positive.
Investigate the dns-tunneling.pcap file. Investigate the dns.log file. What is the number of DNS records linked to the IPv6 address?
DNS "AAAA" records store IPV6 addresses.
```text
root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/anomalous-dns# ls
clear-logs.sh  dns-tunneling.pcap
root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/anomalous-dns# zeekctl start
Warning: new zeek version detected (run the zeekctl "deploy" command)
starting zeek ...
root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/anomalous-dns# zeekctl status
Warning: new zeek version detected (run the zeekctl "deploy" command)
Name         Type       Host          Status    Pid    Started
zeek         standalone localhost     running   2535   10 Dec 17:18:24

root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/anomalous-dns# zeek -Cr dns-tunneling.pcap 
root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/anomalous-dns# ls
clear-logs.sh  dns-tunneling.pcap  http.log  packet_filter.log
conn.log       dns.log             ntp.log

root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/anomalous-dns# head dns.log 
#separator \x09
#set_separator	,
#empty_field	(empty)
#unset_field	-
#path	dns
#open	2022-12-10-17-46-29
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	proto	trans_id	rtt	query	qclass	qclass_name	qtype	qtype_name	rcode	rcode_name	AATC	RD	RA	Z	answers	TTLs	rejected

root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/anomalous-dns# cat dns.log | zeek-cut qtype_name | grep -i 'AAAA' | wc -l
320
```
*320*
Investigate the conn.log file. What is the longest connection duration?
The "duration" value represents the connection time between two hosts.
```text
root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/anomalous-dns# head conn.log 
#separator \x09
#set_separator	,
#empty_field	(empty)
#unset_field	-
#path	conn
#open	2022-12-10-17-46-29
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	proto	service	duration	orig_bytes	resp_bytes	conn_state	local_orig	local_resp	missed_bytes	history	orig_pkts	orig_ip_bytes	resp_pkts	resp_ip_bytes	tunnel_parents

root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/anomalous-dns# cat conn.log | zeek-cut duration | sort -nr | sed -n "1p"
9.420791
```
*9.420791*
Investigate the dns.log file. Filter all unique DNS queries. What is the number of unique domain queries?
You need to use the DNS query values for summarising and counting the number of unique domains. There are lots of "***.cisco-update.com" DNS queries, you need to filter the main address and find out the rest of the queries that don't contain the "***.cisco-update.com" pattern. You can filter the main "***.cisco-update.com" DNS pattern as "cisco-update.com" with the following command; "cat dns.log | zeek-cut query |rev | cut -d '.' -f 1-2 | rev | head"
```text
root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/anomalous-dns# head dns.log
#separator \x09
#set_separator	,
#empty_field	(empty)
#unset_field	-
#path	dns
#open	2022-12-10-17-46-29
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	proto	trans_id	rtt	query	qclass	qclass_name	qtype	qtype_name	rcode	rcode_name	AATC	RD	RA	Z	answers	TTLs	rejected

root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/anomalous-dns# cat dns.log | zeek-cut query | rev | cut -d '.' -f 1-2 | rev | sort | uniq
_tcp.local
cisco-update.com
in-addr.arpa
ip6.arpa
rhodes.edu
ubuntu.com
root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/anomalous-dns# cat dns.log | zeek-cut query | rev | cut -d '.' -f 1-2 | rev | sort | uniq |wc -l
6
```
*6*
There are a massive amount of DNS queries sent to the same domain. This is abnormal. Let's find out which hosts are involved in this activity. Investigate the conn.log file. What is the IP address of the source host?
```text
root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/anomalous-dns# head conn.log 
#separator \x09
#set_separator	,
#empty_field	(empty)
#unset_field	-
#path	conn
#open	2022-12-10-17-46-29
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	proto	service	duration	orig_bytes	resp_bytes	conn_state	local_orig	local_resp	missed_bytes	history	orig_pkts	orig_ip_bytes	resp_pkts	resp_ip_bytes	tunnel_parents

root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/anomalous-dns# cat conn.log | zeek-cut id.orig_h | sed -n "1p"
10.20.57.3
```
*10.20.57.3*
### Phishing
An alert triggered: "Phishing Attempt".
The case was assigned to you. Inspect the PCAP and retrieve the artefacts to confirm this alert is a true positive.
Investigate the logs. What is the suspicious source address? Enter your answer in defanged format.
Cyberchef can defang.
```text
root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/phishing# zeek -Cr phishing.pcap 
root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/phishing# ls
clear-logs.sh  file-extract-demo.zeek  packet_filter.log
conn.log       files.log               pe.log
dhcp.log       hash-demo.zeek          phishing.pcap
dns.log        http.log

root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/phishing# head conn.log 
#separator \x09
#set_separator	,
#empty_field	(empty)
#unset_field	-
#path	conn
#open	2022-12-10-18-25-03
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	proto	service	duration	orig_bytes	resp_bytes	conn_state	local_orig	local_resp	missed_bytes	history	orig_pkts	orig_ip_bytes	resp_pkts	resp_ip_bytes	tunnel_parents

root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/phishing# cat conn.log | zeek-cut id.orig_h | sed -n "1p"
10.6.27.102

defanging ip with cyberchef

10[.]6[.]27[.]102
```
*10[.]6[.]27[.]102*
Investigate the http.log file. Which domain address were the malicious files downloaded from? Enter your answer in defanged format.
Cyberchef can defang.
```text
root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/phishing# head http.log 
#separator \x09
#set_separator	,
#empty_field	(empty)
#unset_field	-
#path	http
#open	2022-12-10-18-25-03
#fields	ts	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	trans_depth	method	host	uri	referrer	version	user_agent	origin	request_body_len	response_body_len	status_code	status_msg	info_code	info_msg	tags	username	password	proxied	orig_fuids	orig_filenames	orig_mime_types	resp_fuids	resp_filenames	resp_mime_types

root@ip-10-10-49-209:/home/ubuntu/Desktop/Exercise-Files/phishing# cat http.log | zeek-cut uri host
/ncsi.txt	www.msftncsi.com
/Documents/Invoice&MSO-Request.doc	smart-fax.com
/knr.exe	smart-fax.com

defanging url with cyberchef
```
*smart-fax[.]com*
Investigate the malicious document in VirusTotal. What kind of file is associated with the malicious document?
Search MD5 value in Virustotal. VT>Relations
```text
search smart-fax.com on virustotal

https://www.virustotal.com/gui/domain/smart-fax.com

then go to relations and follow link of .doc
 	Invoice&MSO-Request.doc 

then again go to relations
