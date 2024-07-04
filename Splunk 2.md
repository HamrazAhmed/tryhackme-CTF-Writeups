---
Part of the Blue Primer series. This room is based on version 2 of the Boss of the SOC (BOTS) competition by Splunk.
---

# Splunk 2 — Writeup

## Overview
### Splunk 2 — Writeup
### Splunk 2 — Writeup
![](https://assets.tryhackme.com/additional/splunk-overview/splunk2-room-banner.png)
### Deploy!
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-botsv2-2017.png)
BOTSv2 Dataset:
The data included in this app was generated in August of 2017 by members of Splunk's Security Specialist team - Dave Herrald, Ryan Kovar, Steve Brant, Jim Apger, John Stoner, Ken Westin, David Veuve and James Brodsky. They stood up a few lab environments connected to the Internet. Within the environment they had a few Windows endpoints instrumented with the Splunk Universal Forwarder and Splunk Stream. The forwarders were configured with best practices for Windows endpoint monitoring, including a full Microsoft Sysmon deployment and best practices for Windows Event logging. The environment included a Palo Alto Networks next-generation firewall to capture traffic and provide web proxy services, and Suricata to provide network-based IDS.
Note: This information is from the Advanced Hunting APTs with Splunk app.
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-botsv2-app.png)
BOTSv2 Github: https://github.com/splunk/botsv2
It is recommended that you complete the Splunk 101 room before attempting this room.
Room Machine
Before moving forward, deploy the Splunk virtual machine.
From the AttackBox, open Firefox Web Browser and navigate to the Splunk instance (http://10.10.176.25:8000).
You may need to refresh the page until Splunk loads. This can take up to five minutes to launch.
Deployed the virtual machine and connected to the website found at 10.10.176.25:8000
*No answer needed*
### Dive into the data
![](https://assets.tryhackme.com/additional/splunk-overview/splunk-botsv2-frothly.png)
In this exercise, you assume the persona of Alice Bluebird, the analyst who successfully assisted Wayne Enterprises and was recommended to Grace Hoppy at Frothly (a beer company) to assist them with their recent issues.
What Kinds of Events Do We Have?
The SPL (Splunk Search Processing Language) command metadata can be used to search for the same kind of information that is found in the Data Summary, with the bonus of being able to search within a specific index, if desired. All time-values are returned in EPOCH time, so to make the output user readable, the eval command should be used to provide more human-friendly formatting.
In this example, we will search the botsv2 index and return a listing of all the source types that can be found as well as a count of events and the first time and last time seen.
Resources:
http://docs.splunk.com/Documentation/Splunk/latest/SearchReference/Metadata
https://www.splunk.com/blog/2017/07/31/metadata-metalore.html
Metadata command:
```text
| metadata type=sourcetypes index=botsv2 | eval firstTime=strftime(firstTime,"%Y-%m-%d %H:%M:%S") | eval lastTime=strftime(lastTime,"%Y-%m-%d %H:%M:%S") | eval recentTime=strftime(recentTime,"%Y-%m-%d %H:%M:%S") | sort - totalCount
```
Note: This information is from the Advanced Hunting APTs with Splunk app.
I'm ready to get hunting with Splunk.
*No answer needed*
### 100 series questions
The questions below are from the BOTSv2 dataset, questions 100-104. Some additional questions were added.
In this task, we'll attempt to help guide you to each question's answer.
Note: The approach outlined in this task is not the only approach to tackle each question.
Reading the questions below, the focus is on Amber Turing and her communication with a competitor.
Question 1
The first objective is to find out what competitor website she visited. What is a good starting point?
When it comes to HTTP traffic, the source and destination IP addresses should be recorded in logs. You need Amber's IP address.
You can start with the following command, index="botsv2" amber, and see what events are returned. Look at the events on the first page.
Amber's IP address is visible in the events related to PAN traffic, but it's not straightforward.
To get her IP address, we can hone in on the PAN traffic source type specifically.
Command: index="botsv2" sourcetype="pan:traffic"
From here, you should have Amber's IP address. You can build a new search query using this information.
It would be best if you used the HTTP stream source type in your new search query.
Using Amber's IP address, construct the following search query.
Command: index="botsv2" IPADDR sourcetype="stream:HTTP"
You must substitute IPADDR with Amber's IP address.
After this query executes, there are many events to sift through for the answer. How else can you narrow this down?
Look at the additional fields.
Another field you can add to the search query to further shrink the returned events list is the site field.
Think about it; you're investigating what competitor website Amber visited.
Expand the search query only to return the site field. Additionally, you can remove duplicate entries and display the results nicely in a table.
Command: index="botsv2" IPADDR sourcetype="stream:HTTP" | KEYWORD site | KEYWORD site
You must substitute KEYWORD with the Splunk commands to remove the duplicate entries and display the output in a table format.
Note: The first KEYWORD is to remove the duplicate entries, and the second is to display the output in a table format.
The results returned to show the URIs that Amber visited, but which website is the one that you're looking for?
To help answer these questions: Who does Amber work for, and what industry are they in?
The competitor is in the same industry. The competitor website now should clearly be visible in the table output.
Extra: You can also use the industry as a search phrase to narrow down the results to a handful of events (1 result to be exact).
Command: index="botsv2" IPADDR sourcetype="stream:HTTP" *INDUSTRY* | KEYWORD site | KEYWORD site
Note: Use asterisks to surround the search term.
Questions 2-7
Amber found the executive contact information and sent him an email. Based on question 2, you know it's an image.
Since you now know the competitor website, you can construct a more specific search query isolating the results to focus on Amber's HTTP traffic to the competitor website.
Command: index="botsv2" IPADDR sourcetype="stream:HTTP" COMPETITOR_WEBSITE
Replace COMPETITOR_WEBSITE with the actual URI of the competitor website.
You can expand on the search query to output the specific field you want in a table format for an easy-to-read format, as we did for the previous objective.
Based on the image, you have the CEO's last name but not his first name. Maybe you can get the name in the email communication.
You can now draw your attention to email traffic, SMTP, but you need Amber's email address. You should be able to get this on your own. :)
Once you have Amber's email address, you can build a search query to focus on her email address and the competitor's website to find events that show email communication between Amber and the competitor.
Command: index="botsv2" sourcetype="stream:smtp" AMBERS_EMAIL COMPETITOR_WEBSITE
Replace AMBERS_EMAIL with her actual email address.
With the returned results from the above search query, you can answer your own remaining questions. :)
```text
search for all time 
index="botsv2" sourcetype="pan:traffic" amber
then open more client_ip
	10.0.2.101

index="botsv2" 10.0.2.101 sourcetype="stream:HTTP" NOT(site=*.microsoft.com OR site=*.windowsupdate.com OR site=*.bing.com OR site=*.digicert.com OR site=*.akamaized.net OR site=*msn.com OR site=*.adnxs.com OR *office.net OR *symcd.com OR site=*gvt1*)
| dedup site 
| table site

em.vindale.com
www.vindale.com
uranus.frothly.local:8014
www.berkbeer.com (correct)

index="botsv2" 10.0.2.101 sourcetype="stream:HTTP" www.berkbeer.com *ceo*
 
 uri_path: /images/ceoberk.png 

index="botsv2" sourcetype="stream:smtp" amber

 sender: Amber Turing <aturing@froth.ly>
   sender_alias: Amber Turing
   sender_email: aturing@froth.ly 

index="botsv2" sourcetype="stream:smtp" aturing@froth.ly berkbeer*
 sender_email: mberk@berkbeer.com 

index="botsv2" sourcetype="stream:smtp" aturing@froth.ly berk*
Give me a call this afternoon if you=
 are free.=C2=A0=0A=0AMartin Berk=0ACEO=0A777.222.8765=0Amberk@berkbeer.=
com=0A=0A----- Original Message -----=0AFrom: "Amber Turing" 

[+] press content

index="botsv2" sourcetype="stream:smtp" aturing@froth.ly hbernhard@berkbeer.com
[+] attach_filename
Saccharomyces_cerevisiae_patent.docx 

index=botsv2 sourcetype="stream:smtp" "aturing@froth.ly" "hbernhard@berkbeer.com"
[+]Content Body

VGhhbmtzIGZvciB0YWtpbmcgdGhlIHRpbWUgdG9kYXksIEFzIGRpc2N1c3NlZCBoZXJlIGlzIHRo
ZSBkb2N1bWVudCBJIHdhcyByZWZlcnJpbmcgdG8uICBQcm9iYWJseSBiZXR0ZXIgdG8gdGFrZSB0
aGlzIG9mZmxpbmUuIEVtYWlsIG1lIGZyb20gbm93IG9uIGF0IGFtYmVyc3RoZWJlc3RAeWVhc3Rp
ZWJlYXN0aWUuY29tPG1haWx0bzphbWJlcnN0aGViZXN0QHllYXN0aWViZWFzdGllLmNvbT4NCg0K
RnJvbTogaGJlcm5oYXJkQGJlcmtiZWVyLmNvbTxtYWlsdG86aGJlcm5oYXJkQGJlcmtiZWVyLmNv
bT4gW21haWx0bzpoYmVybmhhcmRAYmVya2JlZXIuY29tXQ0KU2VudDogRnJpZGF5LCBBdWd1c3Qg
MTEsIDIwMTcgOTowOCBBTQ0KVG86IEFtYmVyIFR1cmluZyA8YXR1cmluZ0Bmcm90aC5seTxtYWls
dG86YXR1cmluZ0Bmcm90aC5seT4+DQpTdWJqZWN0OiBIZWlueiBCZXJuaGFyZCBDb250YWN0IElu
Zm9ybWF0aW9uDQoNCkhlbGxvIEFtYmVyLA0KDQpHcmVhdCB0YWxraW5nIHdpdGggeW91IHRvZGF5
LCBoZXJlIGlzIG15IGNvbnRhY3QgaW5mb3JtYXRpb24uIERvIHlvdSBoYXZlIGEgcGVyc29uYWwg
ZW1haWwgSSBjYW4gcmVhY2ggeW91IGF0IGFzIHdlbGw/DQoNClRoYW5rIFlvdQ0KDQpIZWlueiBC
ZXJuaGFyZA0KaGVybmhhcmRAYmVya2JlZXIuY29tPG1haWx0bzpoZXJuaGFyZEBiZXJrYmVlci5j
b20+DQo4NjUuODg4Ljc1NjMNCg0K 

(decoding cyberchef)

Thanks for taking the time today, As discussed here is the document I was referring to.  Probably better to take this offline. Email me from now on at ambersthebest@yeastiebeastie.com<mailto:ambersthebest@yeastiebeastie.com>

From: hbernhard@berkbeer.com<mailto:hbernhard@berkbeer.com> [mailto:hbernhard@berkbeer.com]
Sent: Friday, August 11, 2017 9:08 AM
To: Amber Turing <aturing@froth.ly<mailto:aturing@froth.ly>>
Subject: Heinz Bernhard Contact Information

Hello Amber,

Great talking with you today, here is my contact information. Do you have a personal email I can reach you at as well?

Thank You

Heinz Bernhard
hernhard@berkbeer.com<mailto:hernhard@berkbeer.com>
865.888.7563
```
Amber Turing was hoping for Frothly to be acquired by a potential competitor which fell through, but visited their website to find contact information for their executive team. What is the website domain that she visited?
*www.berkbeer.com*
Amber found the executive contact information and sent him an email. What image file displayed the executive's contact information? Answer example: /path/image.ext
*/images/ceoberk.png *
What is the CEO's name? Provide the first and last name.
*Martin Berk*
What is the CEO's email address?
*mberk@berkbeer.com*
After the initial contact with the CEO, Amber contacted another employee at this competitor. What is that employee's email address?
*hbernhard@berkbeer.com*
What is the name of the file attachment that Amber sent to a contact at the competitor?
*Saccharomyces_cerevisiae_patent.docx *
What is Amber's personal email address?
*ambersthebest@yeastiebeastie.com*
### 200 series questions
In this task, we'll attempt to tackle the 200 series questions from the BOTSv2 dataset.
Note: As noted in the previous task, this guide is not the only way to query Splunk for the answers to the questions below.
Question 1
Our first task is to identify the version of Tor that Amber installed. You can use a keyword search to get you started.
What are some good keywords? Definitely Amber. Another would be Tor. Give that a go.
Command: index="botsv2" amber tor
Over 300 results are returned. You can reverse the order of results (hoping the 1st event is the TOR installation) and see if you can get the answer.
You should add another keyword to this search query. I'll leave that task to you.
Command: index="botsv2" amber tor KEYWORD
Replace the KEYWORD with another search term to help narrow down the events to the answer.
Questions 2 & 3
You need to determine the public IP address for brewertalk.com and the IP address performing a web vulnerability scan against it.
You should be able to tackle this one on your own. Use the previous search queries as your guide.
Questions 4 & 5
Now that you have the attacker IP address, build your new search query with the attacker IP as the source IP.
Command: index="botsv2" src_ip="ATTACKER_IP"
Tip: Change the Sampling to 1:100 or your query will auto-cancel and throw errors.
Yikes! The number of events returned is over 18,000 .. but that is fine.
Use the Interesting Fields to help you identify what the URI path that is being attacked is.
Once the URI path has been identified, you can use it to expand the search query further to determine what SQL function is being abused.
Command: index="botsv2" src_ip="ATTACKER_IP" uri_path="URI_PATH"
You should have over 600 events to sift through but fret not; the answer is there.
Questions 6 & 7
Awesome, thus far, you have identified Amber downloaded Tor Browser (you even know the exact version). You identified what URI path and the SQL function attacked on brewertalk.com.
Your task now is to identify the cookie value that was transmitted as part of an XSS attack. The user has been identified as Kevin.
Before diving right in, get some details on Kevin. This is the first time you hear of him.
Command: index="botsv2" kevin
Ok, now you have Kevin's first and last name. Time to figure out the cookie value from the XSS attack.
As before, you can start with a simple keyword search.
You know that you're looking for events related to Kevin's HTTP traffic with an XSS payload, and you're focused on the cookie value.
Honestly, you should be able to tackle this one on your own as well. Use the previous search queries as your guide.
After you executed the search query that yields the events with the answer, you can identify the username used for the spear phishing attack.
Based on the question hint, you can perform a keyword search query here as well.
Command: index="botsv2" KEYWORD
As times before, replace KEYWORD with the actual keyword search term.
Great! You should have been able to find all the answers to the questions using basic keyword searches.
```text
index="botsv2" amber tor.exe

process torbrowser-install-7.0.4_en-US.exe

index="botsv2" www.brewertalk.com
dest_ip  52.42.208.228 	473 	4.399%
src_ip    45.77.65.211 	8,965

index="botsv2" www.brewertalk.com 52.42.208.228
uri_path   /member.php 	3 	0.775%

index="botsv2" brewertalk.com src_ip="45.77.65.211" uri_path="/member.php" 
| dedup form_data 
| table form_data

regcheck1=&regcheck2=true&username=makman&password=mukarram&password2=mukarram&email=mak@live.com&email2=mak@live.com&referrername=&imagestring=F7yR4&imagehash=1c1d0e6eae9c113f4ff65339e4b3079c&answer=4&allownotices=1&receivepms=1&pmnotice=1&subscriptionmethod=0&timezoneoffset=0&dstcorrection=2&regtime=1416039333&step=registration&action=do_register&regsubmit=Submit Registration!&question_id=makman' and updatexml(NULL,concat (0x3a,(SUBSTRING((SELECT password FROM mybb_users ORDER BY UID LIMIT 5,1), 32, 31))),NULL) and '1 

updatexml

index="botsv2" kevin sourcetype="stream:http" tag="error"
| table cookie

cookie
mybb[lastvisit]=1502408189; mybb[lastactive]=1502408191; sid=4a06e3f4a6eb6ba1501c4eb7f9b25228; adminsid=9267f9cec584473a8d151c25ddb691f1; acploginattempts=0

1502408189

index="botsv2" 1bc3eab741900ab25c98eee86bf20feb 
| table form_data

statistics
my_post_key=1bc3eab741900ab25c98eee86bf20feb&username=kIagerfield&password=beer_lulz&confirm_password=beer_lulz&email=kIagerfield@froth.ly&usergroup=4&additionalgroups[]=4&displaygroup=4

kIagerfield
```
What version of TOR Browser did Amber install to obfuscate her web browsing? Answer guidance: Numeric with one or more delimiter.
*7.0.4*
