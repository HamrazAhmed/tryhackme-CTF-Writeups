---
Put your snort skills into practice and defend against a live attack
---

# Snort Challenge - Live Attacks — Writeup

## Overview
### Snort Challenge - Live Attacks — Writeup
### Snort Challenge - Live Attacks — Writeup
### Scenario 1 | Brute-Force
Use the attached VM to finish this task.
[+] THE NARRATOR
J&Y Enterprise is one of the top coffee retails in the world. They are known as tech-coffee shops and serve millions of coffee lover tech geeks and IT specialists every day.
They are famous for specific coffee recipes for the IT community and unique names for these products. Their top five recipe names are;
WannaWhite, ZeroSleep, MacDown, BerryKeep and CryptoY.
J&Y's latest recipe, "Shot4J", attracted great attention at the global coffee festival. J&Y officials promised that the product will hit the stores in the coming months.
The super-secret of this recipe is hidden in a digital safe. Attackers are after this recipe, and J&Y enterprises are having difficulties protecting their digital assets.
Last week, they received multiple attacks and decided to work with you to help them improve their security level and protect their recipe secrets.
This is your assistant J.A.V.A. (Just Another Virtual Assistant). She is an AI-driven virtual assistant and will help you notice possible anomalies. Hey, wait, something is happening...
[+] J.A.V.A.
Welcome, sir. I am sorry for the interruption. It is an emergency. Somebody is knocking on the door!
[+] YOU
Knocking on the door? What do you mean by "knocking on the door"?
[+] J.A.V.A.
We have a brute-force attack, sir.
[+] THE NARRATOR
This is not a comic book! Would you mind going and checking what's going on! Please...
[+] J.A.V.A.
Sir, you need to observe the traffic with Snort and identify the anomaly first. Then you can create a rule to stop the brute-force attack. GOOD LUCK!
Answer the questions below
First of all, start Snort in sniffer mode and try to figure out the attack source, service and port.
Then, write an IPS rule and run Snort in IPS mode to stop the brute-force attack. Once you stop the attack properly, you will have the flag on the desktop!
Here are a few points to remember:
Create the rule and test it with "-A console" mode.
Use "-A full" mode and the default log path to stop the attack.
Write the correct rule and run the Snort in IPS "-A full" mode.
Block the traffic at least for a minute and then the flag file will appear on your desktop.
Stop the attack and get the flag (which will appear on your Desktop)
"IPS mode and Dropping Packets" is covered in the main Snort room TASK-7. https://tryhackme.com/room/snort
```text
ubuntu@ip-10-10-72-206:~$ sudo su
root@ip-10-10-72-206:/home/ubuntu# ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
root@ip-10-10-72-206:/home/ubuntu# cd Desktop/
root@ip-10-10-72-206:/home/ubuntu/Desktop# ls
root@ip-10-10-72-206:/home/ubuntu/Desktop# ls -lah
total 8.0K
drwxr-xr-x  2 ubuntu ubuntu 4.0K Feb  2  2022 .
drwxr-xr-x 22 ubuntu ubuntu 4.0K Dec  7 16:23 ..
root@ip-10-10-72-206:/home/ubuntu/Desktop# cd ..
root@ip-10-10-72-206:/home/ubuntu# ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
root@ip-10-10-72-206:/home/ubuntu# cd /etc/snort/rules/
root@ip-10-10-72-206:/etc/snort/rules# ls
attack-responses.rules         community-web-dos.rules   policy.rules
backdoor.rules                 community-web-iis.rules   pop2.rules
bad-traffic.rules              community-web-misc.rules  pop3.rules
chat.rules                     community-web-php.rules   porn.rules
community-bot.rules            ddos.rules                rpc.rules
community-deleted.rules        deleted.rules             rservices.rules
community-dos.rules            dns.rules                 scan.rules
community-exploit.rules        dos.rules                 shellcode.rules
community-ftp.rules            experimental.rules        smtp.rules
community-game.rules           exploit.rules             snmp.rules
community-icmp.rules           finger.rules              sql.rules
community-imap.rules           ftp.rules                 telnet.rules
community-inappropriate.rules  icmp-info.rules           tftp.rules
community-mail-client.rules    icmp.rules                virus.rules
community-misc.rules           imap.rules                web-attacks.rules
community-nntp.rules           info.rules                web-cgi.rules
community-oracle.rules         local.rules               web-client.rules
community-policy.rules         misc.rules                web-coldfusion.rules
community-sip.rules            multimedia.rules          web-frontpage.rules
community-smtp.rules           mysql.rules               web-iis.rules
community-sql-injection.rules  netbios.rules             web-misc.rules
community-virus.rules          nntp.rules                web-php.rules
community-web-attacks.rules    oracle.rules              x11.rules
community-web-cgi.rules        other-ids.rules
community-web-client.rules     p2p.rules
root@ip-10-10-72-206:/etc/snort/rules# cat local.rules
```
```text
# $Id: local.rules,v 1.11 2004/07/23 20:15:44 bmc Exp $
```
```text
# ----------------
```
```text
# LOCAL RULES
```
```text
# ----------------
```
```text
# This file intentionally does not come with signatures.  Put your local
```
```text
# additions here.

root@ip-10-10-72-206:/etc/snort/rules# nano local.rules 
root@ip-10-10-72-206:/etc/snort/rules# cat local.rules
```
```text
# $Id: local.rules,v 1.11 2004/07/23 20:15:44 bmc Exp $
```
```text
# ----------------
```
```text
# LOCAL RULES
```
```text
