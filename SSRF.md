---
Learn how to exploit Server-Side Request Forgery (SSRF) vulnerabilities, allowing you to access internal server resources.
---

# SSRF — Writeup

## Overview
### SSRF — Writeup
### SSRF — Writeup
### What is an SSRF?
Room Brief
In this room, you'll learn what an SSRF is, what kind of impact they can have, you'll view some example SSRF attacks, how you can discover SSRF vulnerabilities, how to circumvent input rules and then we have a practice for you against with to try your newfound skills.
What is an SSRF?
SSRF stands for Server-Side Request Forgery. It's a vulnerability that allows a malicious user to cause the webserver to make an additional or edited HTTP request to the resource of the attacker's choosing.
Types of SSRF
There are two types of SSRF vulnerability; the first is a regular SSRF where data is returned to the attacker's screen. The second is a Blind SSRF vulnerability where an SSRF occurs, but no information is returned to the attacker's screen.
What's the impact?
A successful SSRF attack can result in any of the following:
Access to unauthorised areas.
Access to customer/organisational data.
Ability to Scale to internal networks.
Reveal authentication tokens/credentials.
What does SSRF stand for?
*Server-Side Request Forgery.*
As opposed to a regular SSRF, what is the other type? *Blind*
### SSRF Examples
Click the View Site button, which will take you through some common SSRF examples, how to exploit them and even a simulation to see if you can take advantage of an SSRF vulnerability using what you've learnt.
Instructions
The below example shows how the attacker can have complete control over the page requested by the webserver.
The Expected Request is what the website.thm server is expecting to receive, with the section in red being the URL that the website will fetch for the information.
The attacker can modify the area in red to an URL of their choice.
![](https://static-labs.tryhackme.cloud/sites/ssrf-examples/images/ssrf_1.png)
The below example shows how an attacker can still reach the /api/user page with only having control over the path by utilising directory traversal. When website.thm receives ../ this is a message to move up a directory which removes the /stock portion of the request and turns the final request into /api/user
![](https://static-labs.tryhackme.cloud/sites/ssrf-examples/images/ssrf_2.png)
In this example, the attacker can control the server's subdomain to which the request is made. Take note of the payload ending in &x= being used to stop the remaining path from being appended to the end of the attacker's URL and instead turns it into a parameter (?x=) on the query string.
![](https://static-labs.tryhackme.cloud/sites/ssrf-examples/images/ssrf_3.png)
Going back to the original request, the attacker can instead force the webserver to request a server of the attacker's choice. By doing so, we can capture request headers that are sent to the attacker's specified domain. These headers could contain authentication credentials or API keys sent by website.thm (that would normally authenticate to api.website.thm).
![](https://static-labs.tryhackme.cloud/sites/ssrf-examples/images/ssrf_4.png)
Using what you've learnt, try changing the address in the browser below to force the webserver to return data from https://server.website.thm/flag?id=9. To make things easier the Server Requesting bar at the bottom of the mock browser will show the URL that website.thm is requesting.
Question Hint
Append &x= at the end to ignore the rest of the URL.
```404
https://website.thm/item/2?server=server.website.thm/flag?id=9

404 Not Found
nginx 1.18
Server Requesting: https://server.website.thm/flag?id=9.website.thm/api/item?id=2
```
By including the “&x=” payload at the end of the URL, you can bypass it.
It works because it prevents the attacker’s remaining default “URL Path” from being attached to the end of the attacker’s URL.
```flag
https://website.thm/item/2?server=server.website.thm/flag?id=9&x

Flag ID: 9 Found!
