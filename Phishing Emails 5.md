---
Use the knowledge attained to analyze a malicious email. 
---

# Phishing Emails 5 — Writeup

## Overview
### Phishing Emails 5 — Writeup
### Phishing Emails 5 — Writeup
![](https://assets.tryhackme.com/additional/phishing1/phish-room-banner-final.png)
### Just another day as a SOC Analyst..
![](https://assets.tryhackme.com/additional/phishing5/main.png)
A Sales Executive at Greenholt PLC received an email that he didn't expect to receive from a customer. He claims that the customer never uses generic greetings such as "Good day" and didn't expect any amount of money to be transferred to his account. The email also contains an attachment that he never requested. He forwarded the email to the SOC (Security Operations Center) department for further investigation.
Investigate the email sample to determine if it is legitimate.
Tip: Open the EML file with Thunderbird.
Deploy the machine attached to this task; it will be visible in the split-screen view once it is ready.
If you don't see a virtual machine load then click the Show Split View button.
```text
go to show split view / open challenge.eml with Thunderbird email
```
![[Pasted image 20220926205543.png]]
![](https://www.cyb3rm3.com/web/image/832-e6b981a8/2022-01-01%2016_48_39-TryHackMe%20_%20Phishing%20Emails%205.png)
What is the email's timestamp? (answer format: mm/dd/yyyy hh:mm
*06/10/2020 05:58*
Who is the email from?
*Mr. James Jackson*
What is his email address?
*info@mutawamarine.com*
What email address will receive a reply to this email?
*info.mutawamarine@mail.com*
```text
with thunderbird more view source

X-Originating-IP: [x.x.x.x]
Received: from 10.197.41.148  (EHLO sub.redacted.com) (x.x.x.x)
  by mta4212.mail.bf1.yahoo.com with SMTP; Wed, 10 Jun 2020 05:58:54 +0000
Received: from hwsrv-737338.hostwindsdns.com ([192.119.71.157]:51810 helo=mutawamarine.com)
	by sub.redacted.com with esmtp (Exim 4.80)
	(envelope-from <info@mutawamarine.com>)
```
What is the Originating IP?
The answer is NOT in X-Originating-Ip
*192.119.71.157*
```text
use https://db-ip.com/
