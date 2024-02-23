---
Learn the basic concepts for secure API development (Part 1).
---

# OWASP API Security Top 10 - 1 — Writeup

## Overview
### OWASP API Security Top 10 - 1 — Writeup
### OWASP API Security Top 10 - 1 — Writeup
![](https://i.imgur.com/sP6d0iZ.png)
![100](https://tryhackme-images.s3.amazonaws.com/room-icons/74be0ffb2200053145ccadac85dd24c5.png)
### Introduction
Start Machine
OWASP - Open Web Application Security Project (OWASP) is a non-profit and collaborative online community that aims to improve application security via a set of security principles, articles, documentation etc. Back in 2019, OWASP released a list of the top 10 API vulnerabilities, which will be discussed in detail, along with its potential impact and a few effective mitigation measures.
We have split this room into two parts. In **Part 1**, you will study the top 5 principles, and in Part 2 (coming soon), you will learn the remaining principles.
**Learning Objectives**
-   Best practices for API authorisation & authentication.
-   Identification of authorisation level issues.
-   Handling excessive data exposure.
-   Lack of resources and rate-limiting issues.
**Learning Pre-requisites**
An understanding of the following topics is recommended before starting the room:
-   [How websites work](https://tryhackme.com/room/howwebsiteswork).
-   [HTTP protocols & methods](https://tryhackme.com/room/protocolsandservers).
-   [Principles of security](https://tryhackme.com/room/principlesofsecurity).
-   [OWASP top 10 web vulnerabilities](https://tryhackme.com/room/owasptop10).
**Connecting to the Machine**
We will be using Windows as a development/test machine along with Talend API Tester - free edition throughout the room with the following credentials:
-   Machine IP:  `MACHINE_IP`
-   Username:   `Administrator`
-   Password:    `Owasp@123`
You can start the virtual machine by clicking `Start Machine`. The machine will start in a split-screen view. In case the VM is not visible, use the blue Show Split View button at the top-right of the page. Alternatively, you can connect with the VM through Remote Desktop using the above credentials. Please wait 1-2 minutes after the system boots completely to let the auto scripts run successfully that will execute Talend API Tester and Laravel-based web application automatically.
Let's begin!
### Understanding APIs - A refresher
**What is an API & Why is it important?**
API stands for Application Programming Interface. It is a middleware that facilitates the communication of two software components utilising a set of protocols and definitions. In the API context, the term '**application**' refers to any software having specific functionality, and '**interface**' refers to the service contract between two apps that make communication possible via requests and responses. The API documentation contains all the information on how developers have structured those responses and requests. The significance of APIs to app development is in just a single sentence, i.e., **API is a building block for developing complex and enterprise-level applications**.
**Recent Data Breaches through APIs**
-   LinkedIn data breach: In June 2021, the data of over 700 million LinkedIn users were offered for sale on one of the dark web forums, which was scraped by exploiting the LinkedIn API. The hacker published a sample of 1 million records to confirm the legitimacy of the LinkedIn breach, containing full names of the users, email addresses, phone numbers, geolocation records, LinkedIn profile links, work experience information, and other social media account details.
-   Twitter data breach: In June 2022, data of more than 5.4 Million [Twitter](https://privacy.twitter.com/en/blog/2022/an-issue-affecting-some-anonymous-accounts) users was released for sale on the dark web. Hackers conducted the breach by exploiting a zero-day in the Twitter API that showed Twitter's handle against a mobile number or email.
-   PIXLR data breach: In January 2021, PIXLR, an online photo editor app, suffered a data breach that impacted around 1.9 million users. All the data by the hackers was dumped on a dark web forum, which included usernames, email addresses, countries, and hashed passwords.
Now that we understand the threat and the damage caused due to non-adherence to mitigation measures - let's discuss developing a secure API through **OWASP API Security Top 10 principles**.
Answer the questions below
```text
An API, or Application Programming Interface, is a set of rules and protocols that allows different software programs to communicate with each other. It allows different systems to share data and functionality, and enables different software programs to interact with one another in a predefined way.

A simple example of an API is the one used to check the weather forecast. A weather forecasting website, for example, has a database of weather information that it makes available to other websites and applications through an API. This allows other websites and apps to access the weather information from the forecasting website and display it on their own platforms.

Another example, a developer could use an API from a social media platform such as Facebook to add a "Share on Facebook" button to their website. The API allows the developer to access the social media platform's functionality and integrate it into their website, so users can share the website's content on their Facebook page with a single click.

Another example, a developer could use an API from a payment processor like PayPal to add payment functionality to their website. The API allows the developer to access the payment processor's functionality and integrate it into their website, so users can make payments directly on the site.

In summary, an API is a set of rules and protocols that allows different software programs to communicate with each other, to share data and functionality and to interact with one another in a predefined way. It enables developers to access the functionality of other systems and integrate it into their own software.
```
In the LinkedIn breach (Jun 2021), how many million records (sample) were posted by a hacker on the dark web?
*1*
Is the API documentation a trivial item and not used after API development (yea/nay)?
*nay*
I understand the APIs and am ready to learn OWASP Top 10 Principles.

## Exploitation
**How does it Happen?**
Generally, API endpoints are utilised for a common practice of retrieving and manipulating data through object identifiers. BOLA refers to Insecure Direct Object Reference (IDOR) - which creates a scenario where the user uses the **input functionality and gets access to the resources they are not authorised to access**. In an API, such controls are usually implemented through programming in Models (Model-View-Controller Architecture) at the code level.
Likely Impact
The absence of controls to prevent **unauthorised object access can lead to data leakage** and, in some cases, complete account takeover. User's or subscribers' data in the database plays a critical role in an organisation's brand reputation; if such data is leaked over the internet, that may result in substantial financial loss.
**Practical Example**
-   Open the VM. You will find that the Chrome browser and Talend API Tester application are running automatically, which we will be using for debugging the API endpoints.
-   Bob is working as an API developer in `Company MHT` and developed an endpoint `/apirule1/users/{ID}` that will allow other applications or developers to request information by sending an employee ID. In the VM, you can request results by sending `GET` requests to `http://localhost:80/MHT/apirule1_v/user/1.`
-   What is the issue with the above API call? The problem is that the endpoint is not validating any incoming API call to confirm whether the request is valid. It is not checking for any authorisation whether the person requesting the API call can ask for it or not.
-   The solution for this problem is pretty simple; Bob will implement an authorisation mechanism through which he can identify who can make API calls to access employee ID information.
-   The purpose is achieved through **access tokens or authorisation tokens** in the header. In the above example, Bob will add an authorisation token so that only headers with valid authorisation tokens can make a call to this endpoint.
-   In the VM, if you add a valid `Authorization-Token` and call `http://localhost:80/MHT/apirule1_s/user/1`, only then will you be able to get the correct results. Moreover, all API calls with an invalid token will show `403 Forbidden` an error message (as shown below).
**Mitigation Measures**
-   An authorisation mechanism that relies on user policies and hierarchies should be adequately implemented.
-   Strict access controls methods to check if the logged-in user is authorised to perform specific actions.
-   Promote using completely random values (strong encryption and decryption mechanism) for nearly impossible-to-predict tokens.
Answer the questions below
```json
Model-View-Controller (MVC) is a design pattern that is commonly used in software development. It is a way of separating the code for an application into three distinct components: the model, the view, and the controller.

-   The Model represents the data and the business logic of the application. It is responsible for storing and manipulating the data.
    
-   The View is responsible for displaying the data to the user. It is the user interface of the application, such as the layout of the website or the layout of the mobile app.
    
-   The Controller is responsible for handling the communication between the Model and the View. It receives input from the user, updates the Model, and updates the View.
    

A simple example of how the MVC pattern can be applied is in a web-based application that allows users to view and edit a list of items. The Model would store the data for the items, the View would display the items to the user, and the Controller would handle the communication between the Model and the View, such as updating the data when an item is edited.

In summary, the Model-View-Controller (MVC) is a design pattern that separates the code for an application into three distinct components: the Model, the View, and the Controller. The Model represents the data and the business logic, the View is responsible for displaying the data to the user, and the Controller is responsible for handling the communication between the Model and the View. It makes the code more organized and easier to maintain.

using Talend API Tester

Method GET
http://127.0.0.1/MHT/apirule1_v/user/2

{
"id": 2,
"username": "Alice",
"name": "King",
"flag": "THM{838123}"
}

http://127.0.0.1/MHT/apirule1_v/user/3

{
"id": 3,
"username": "Bob",
"name": "Tester",
"flag": "THM{112312}"
}

http://127.0.0.1/MHT/apirule1_v/user/4

No Content

There are 3 users
```
Suppose the employee ID is an integer with incrementing value. Can you check through the vulnerable API endpoint the total number of employees in the company?
*3*
What is the flag associated with employee ID 2?
What is the username of employee ID 3?
*Bob*
**How does it happen?**
User authentication is the core aspect of developing any application containing sensitive data. Broken User Authentication (BUA) reflects a scenario where an API endpoint allows an attacker to access a database or acquire a higher privilege than the existing one. The primary reason behind BUA is either **invalid implementation of authentication** like using incorrect email/password queries etc., or the absence of security mechanisms like authorisation headers, tokens etc.
Consider a scenario in which an attacker acquires the capability to abuse an authentication API; it will eventually result in data leaks, deletion, modification, or even the complete account takeover by the attacker. Usually, hackers have created special scripts to profile, enumerate users on a system and identify authentication endpoints. A poorly implemented authentication system can lead any user to take on another user's identity.
**Likely Impact**
In broken user authentication, attackers can compromise the authenticated session or the authentication mechanism and easily access sensitive data. Malicious actors can pretend to be someone authorised and can conduct an undesired activity, including a complete account takeover.
Practical Example
-   Continue to use the Chrome browser and Talend API Tester for debugging in the VM.
-   Bob understands that authentication is critical and has been tasked to develop an API endpoint `apirule2/user/login_v` that will authenticate based on provided email and password.
-   The endpoint will return a token, which will be passed as an `Authorisation-Token` header (GET request) to `apirule2/user/details` to show details of the specific employee. Bob successfully developed the login endpoint; however, he only used email to validate the user from the `user table` and ignored the password field in the SQL query. An attacker only requires the victim's email address to get a valid token or account takeover.
-    In the VM, you can test this by sending a `POST` request to `http://localhost:80/MHT/apirule2/user/login_v` with email and password in the form parameters.
-   As we can see, the vulnerable endpoint received a token which can be forwarded to `/apirule2/user/details` to get detail of a user.
-   To fix this, we will update the login query logic and use both email and password for validation. The endpoint `/apirule2/user/login_s` is a valid endpoint, as shown below, that authorises the user based on password and email both.
**Mitigation Measures**
-   Ensure complex passwords with higher entropy for end users.
-   Do not expose sensitive credentials in **GET** or **POST** requests.
-   Enable strong JSON Web Tokens (JWT), authorisation headers etc.
-   Ensure the implementation of multifactor authentication (where possible), account lockout, or a captcha system to mitigate brute force against particular users.
-   Ensure that passwords are not saved in plain text in the database to avoid further account takeover by the attacker.
Answer the questions below
```json
JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. It is a text format that is completely language independent but uses conventions that are familiar to programmers of the C family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. JSON is often used to transmit data between a server and a web application, as well as between different parts of a web application. JSON data is represented as key-value pairs, similar to a dictionary or hash table in other programming languages.

JSON Web Tokens (JWT) is a standard for creating and representing claims securely between two parties. JWT is a JSON object that is encoded as a string and it can be digitally signed, so the authenticity of the token can be verified. JWT is commonly used to authenticate users in web applications and APIs.

A JWT typically contains three parts: a header, a payload and a signature. The header contains information about the type of token and the algorithm used to generate the signature. The payload contains the claims, which are statements about an entity (typically, the user) and additional data. The signature is used to verify that the sender of the JWT is who it says it is and to ensure that the message wasn't changed along the way.

For example, when a user logs into a web application, the server will create a JWT that contains information about the user, such as their user ID and email address. The JWT is then sent to the client, typically as a part of the response. The client will then include this JWT in the header of subsequent requests to the server, to prove that the user is authenticated. The server will then use the JWT to identify the user and authorize their requests.

In short, JSON Web Tokens (JWT) is a standard for creating and representing claims securely between two parties, it's commonly used to authenticate users in web applications and APIs. It's a JSON object that is encoded as a string, it can be digitally signed, so the authenticity of the token can be verified and it contains three parts: a header, a payload, and a signature.

A JSON object is a collection of key-value pairs that are used to represent data in a structured way. It is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate. JSON is a text format that is completely language-independent but uses conventions that are familiar to programmers of the C family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others.

The keys in a JSON object are strings and the values can be strings, numbers, booleans, arrays, or other JSON objects. JSON objects are delimited with curly braces {} and the key-value pairs are separated by a colon :.

A simple example of a JSON object is as follows:

{
    "name": "John Smith",
    "age": 35,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    },
    "phoneNumbers": [
        {
            "type": "home",
            "number": "555-555-1234"
        },
        {
            "type": "work",
            "number": "555-555-5678"
        }
    ]
}

This JSON object represents information about a person named John Smith, including his name, age, address and phone numbers. The address and phone numbers are represented as nested JSON objects. JSON objects are widely used in web development, in RESTful API, and in other services that require the exchange of data between different systems.

In summary, JSON object is a collection of key-value pairs that are used to represent data in a structured way, it's lightweight, easy for humans to read and write and easy for machines to parse and generate. JSON is widely used in web development, in RESTful API and in other services that require the exchange of data between different systems.

RESTful API (Representational State Transfer) is a type of web architecture and a set of constraints that are usually applied to web services. It is based on the principles of REST, which stands for Representational State Transfer, and it is an architectural style that defines a set of guidelines for building web services. RESTful APIs use HTTP requests to POST (create), PUT (update), GET (read), and DELETE (delete) data.

A RESTful API allows for communication between a web-based client and server and it is typically comprised of a base URL, an endpoint, and a set of HTTP methods. The base URL is the address of the server, the endpoint is the specific location on the server where the requested information is located, and the HTTP methods are used to retrieve or manipulate the information.

A simple example of a RESTful API is a weather forecasting service that allows a client to retrieve current weather information for a given location. The base URL for the service might be "[http://api.weather.com](http://api.weather.com/)", the endpoint might be "forecast" and the client could retrieve the current weather information by sending a GET request to "[http://api.weather.com/forecast?location=NewYork](http://api.weather.com/forecast?location=NewYork)"

In summary, RESTful API (Representational State Transfer) is a type of web architecture and a set of constraints that are usually applied to web services, it's based on the principles of REST, it uses HTTP requests to POST, PUT, GET and DELETE data and it's typically comprised of a base URL, an endpoint, and a set of HTTP methods. It allows for communication between a web-based client and server and it's widely used in web development.

Method POST

http://127.0.0.1/MHT/apirule2/user/login_v

add form parameters  

email Text admin@mht.com
password Text anything

Request Body

{
"success": "true",
"token": "0g*[v;~5lyx5L15J25sm$nm:cAWZv}"
}

Getting detail user with token

Method GET

http://127.0.0.1/MHT/apirule2/user/details

Header:

Authorization-Token : 0g*[v;~5lyx5L15J25sm$nm:cAWZv}

{
"id": 1,
"email": "admin@mht.com",
"name": "Bob",
"token": "0g*[v;~5lyx5L15J25sm$nm:cAWZv}",
"address": "H1 Turkey",
"city": "Mesport",
"country": "Turkey"
}

Method POST

http://127.0.0.1/MHT/apirule2/user/login_v

add form parameters  

email Text hr@mht.com
password Text witty

Request body

{
"success": "true",
"token": "cOC%Aonyis%H)mZ&uJkuI?_W#4&m>Y"
}

Method GET

http://127.0.0.1/MHT/apirule2/user/details

Header:

Authorization-Token : cOC%Aonyis%H)mZ&uJkuI?_W#4&m>Y

Request Body

{
"id": 2,
"email": "hr@mht.com",
"name": "Tara",
"token": "cOC%Aonyis%H)mZ&uJkuI?_W#4&m>Y",
"address": "H1 USA",
"city": "New York",
"country": "USA"
}

Method POST

http://127.0.0.1/MHT/apirule2/user/login_v

add form parameters  

email Text sales@mht.com
password Text witty

Request Body

{
"success": "true",
"token": "~jSkQD:u<Zdo!JDvX_9V[GrD%:JTtU"
}

Method GET

http://127.0.0.1/MHT/apirule2/user/details

Header:

Authorization-Token : ~jSkQD:u<Zdo!JDvX_9V[GrD%:JTtU

Request Body

{
"id": 3,
"email": "sales@mht.com",
"name": "Joyce",
"token": "~jSkQD:u<Zdo!JDvX_9V[GrD%:JTtU",
"address": "H1 China",
"city": "California",
"country": "China"
}
```
Can you find the token of hr@mht.com?
