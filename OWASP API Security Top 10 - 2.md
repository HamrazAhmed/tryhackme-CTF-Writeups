---
Learn the basic concepts for secure API development (Part 2).
---

# OWASP API Security Top 10 - 2 — Writeup

## Overview
### OWASP API Security Top 10 - 2 — Writeup
### OWASP API Security Top 10 - 2 — Writeup
![](https://i.imgur.com/sP6d0iZ.png)
![222](https://tryhackme-images.s3.amazonaws.com/room-icons/7a45f6ff36f59b4874143d01faa98e41.png)
### Quick Recap
Start Machine
In the [previous room](https://tryhackme.com/jr/owaspapisecuritytop105w), we studied the first five principles of OWASP API Security. Now in this room, we will briefly discuss the remaining principles and their potential impact and mitigation measures.
**Learning Objectives**
-   Identification of security misconfigurations.
-   Preventing Denial of Service (DoS) against the API.
-   Ensuring appropriate logging and monitoring.
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
You can start the virtual machine by clicking the `Start Machine button`. The machine will start in a split-screen view. In case the VM is not visible, use the blue Show Split View button at the top-right of the page. Alternatively, you can connect with the VM through Remote Desktop using the above credentials. Please wait 1-2 minutes after the system boots completely to let the auto scripts run successfully that will execute Talend API Tester and Laravel-based web application automatically.
Let's begin!
Answer the questions below
I can connect and log in to the machine.

## Exploitation
﻿**How does it happen?**
Mass assignment reflects a scenario where **client-side data is automatically bound with server-side objects or class variables**. However, hackers exploit the feature by first understanding the **application's business logic** and sending specially crafted data to the server, acquiring administrative access or inserting tampered data. This functionality is widely exploited in the latest frameworks like Laravel, Code Ignitor etc.
Consider a user's profiles dashboard where users can update their profile like associated email, name, address etc. The username of the user is a read-only attribute and cannot be changed; however, a malicious actor can edit the username and submit the form. If necessary filtration is not enabled on the server side (model), it will simply insert/update the data in the database.
**Likely Impact**
The attack may result in **data tampering and privilege escalation** from a regular user to an administrator.
Practical Example
-   Open the VM. You will find that the Chrome browser and Talend API Tester application are running automatically, which we will be using for debugging the API endpoints.
-   Bob has been assigned to develop a signup API endpoint `/apirule6/user` that will take a name, username and password as input parameters (POST). The user's table has a `credit column` with a default value of `50`. Users will upgrade their membership to have a larger credit value.
-   Bob has successfully designed the form and used the mass assignment feature in Laravel to store all the incoming data from the client side to the database (as shown below).
-   What is the problem here? Bob is not doing any filtering on the server side. Since using the **mass assignment feature**, he is also inserting credit values in the database (malicious actors can update that value).
-   The solution to the problem is pretty simple. Bob must ensure necessary filtering on the server side (`apirule6/user_s`) and ensure that the default value of credit should be inserted as `50`, even if more than 50 is received from the client side (as shown below).
**Mitigation Measures**
-   Before using any framework, one must study how the backend insertions and updates are carried out. In the Laravel framework, [fillable and guarded](https://laravel.com/docs/9.x/eloquent#inserts) arrays mitigate the above-mentioned scenarios.
-   Avoid using functions that bind an input from a client to code variables automatically.
-   Allowlist those properties only that need to get updated from the client side.
Answer the questions below
```ruby
Mass assignment is a feature in some programming languages and frameworks that allows for the initialization of an object's properties with a single assignment statement. This is often used to set multiple properties of an object at once, and is particularly useful when working with forms in web development. In languages like Ruby on Rails, mass assignment can be used to set multiple attributes of a database model at once, using a hash or array of attribute values. This can be useful for reducing the amount of code required, but it also requires careful consideration of security, as it can open up the possibility of malicious users injecting unwanted values into an object's properties.

Sure, here is a simple example of mass assignment in Ruby on Rails:

class Person < ApplicationRecord
  attr_accessible :name, :age, :gender
end

#creating a new person
person = Person.new(name: "John", age: 30, gender: "male")
person.save

In this example, we have a `Person` model with `name`, `age`, and `gender` attributes. The `attr_accessible` line specifies which attributes can be mass-assigned. In the last line, we use the new method to create a new person, passing in a hash of attribute values, which sets the `name`, `age`, and `gender` attributes all at once.

This is a very simple example, but in real-world application, you may want to be more careful and make sure the data passed in is sanitized and in the right format.

Method POST

http://127.0.0.1/MHT/apirule6/user

Add form parameter

name:Bob
username:bob_mht
password:anything
credit:100 (more than 50)

Request Body

{
"name": "Bob",
"username": "bob_mht",
"credit": "110",
"id": 6
}

http://127.0.0.1/MHT/apirule6/user_s

{
"name": "Bob",
"username": "bob_mht",
"credit": 50,
"id": 7
}
```
![[Pasted image 20230125115731.png]]
Is it a good practice to blindly insert/update user-provided data in the database (yea/nay)?
*nay*
Using /apirule6/user_s, insert a record in the database using the credit value as 1000.
No answer needed
What would be the returned credit value after performing Question#2?
*50*
﻿**How does it happen?**
Security misconfiguration depicts an implementation of **incorrect and poorly configured security controls** that put the security of the whole API at stake. Several factors can result in security misconfiguration, including improper/incomplete default configuration, publically accessible cloud storage, [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS), and error messages displayed with sensitive data. Intruders can take advantage of these misconfigurations to perform detailed reconnaissance and get unauthorised access to the system.
Security misconfigurations are usually detected by vulnerability scanners or auditing tools and thus can be curtailed at the initial level. API documentation, a list of endpoints, error logs etc., **must not be publically accessible** to ensure safety against security misconfigurations. Typically, companies deploy security controls like web application firewalls, which are not configured to block undesired requests and attacks.
**Likely Impact**
Security misconfiguration can give intruders complete knowledge of API components. Firstly, it allows intruders to bypass security mechanisms. **Stack trace or other detailed errors** can provide the malicious actor access to confidential data and essential system details, further aiding the intruder in profiling the system and gaining entry.
Practical Example
-   Continue to use the Chrome browser and Talend API Tester for debugging in the VM.
-   The company MHT is facing serious server availability issues. Therefore, they assigned Bob to develop an API endpoint `/apirule7/ping_v` (GET) that will share details regarding server health and status.
-   Bob successfully designed the endpoint; however, he forgot to implement any error handling to avoid any information leakage.
-   What is the issue here? In case of an unsuccessful call, the server sends a complete stack trace in response, containing function names, controller and route information, file path etc. An attacker can use the information for profiling and preparing specific attacks on the environment.
-   The solution to the issue is pretty simple. Bob will create an API endpoint `/apirule7/ping_s` that will carry out error handling and only share desired information with the user (as shown below).
**Mitigation Measures**
-   Limit access to the administrative interfaces for authorised users and disable them for other users.
-   Disable default usernames and passwords for public-facing devices (routers, Web Application Firewall etc.).
-   Disable directory listing and set proper permissions for every file and folder.
-   Remove unnecessary pieces of code snippets, error logs etc. and turn off debugging while the code is in production.
Answer the questions below
```json
"Cross-origin" refers to the relationship between two different web sites, or origins. An origin is defined as a combination of a scheme (such as "http" or "https"), a hostname, and a port number.

So, when a request is made from one origin to a resource on another origin, it is considered a "cross-origin" request. For example, if a web page served from "[http://example.com](http://example.com/)" makes an HTTP request to "[http://other-site.com](http://other-site.com/)", that is a cross-origin request.

The same-origin policy is a security feature implemented by web browsers that limits the ability of web pages to access resources on different origins. This policy is in place to prevent malicious web pages from making unauthorized requests to other sites and potentially stealing sensitive information. CORS (Cross-Origin Resource Sharing) is a way for web servers to relax the same-origin policy and allow certain cross-origin requests.

CORS (Cross-Origin Resource Sharing) is a security feature implemented by web browsers to prevent a web page from making requests to a different domain than the one that served the web page.

An example of this would be if a web page served from "[http://example.com](http://example.com/)" tried to make an HTTP request to "[http://other-site.com](http://other-site.com/)". Without CORS, the browser would block the request as a security measure.

However, if "[http://other-site.com](http://other-site.com/)" has enabled CORS, it can specify which origins are allowed to access its resources. This is done by setting appropriate headers in the server's response, such as `Access-Control-Allow-Origin`.

Here's an example of how CORS can be enabled in a Node.js Express server:

const express = require("express");
const app = express();

app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "http://example.com");
  res.header("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE");
  res.header("Access-Control-Allow-Headers", "Content-Type");
  next();
});

app.get("/data", (req, res) => {
  res.json({ message: "Hello from the server!" });
});

app.listen(3000, () => {
  console.log("Server listening on port 3000");
});

In this example, the server is allowing the origin "[http://example.com](http://example.com/)" to access its resources, and responding to the `GET` method, allowing the headers "Content-Type" as well. You will need to check the documentation of the framework you are using to know how to set CORS headers.

CORS is a simple concept to understand but the implementation can be a bit more complex depending on the specific use case.

An endpoint refers to a specific URL or URI (Uniform Resource Identifier) that represents a resource or service that can be accessed via the web or a network. An endpoint is the point of entry for a client to access a server and its resources.

In the context of web development, an endpoint typically refers to the address of a specific server-side script or resource that a client can make requests to. For example, a server might have an endpoint for creating new users, updating existing users, or fetching a list of all users. These endpoints are usually defined by a combination of the HTTP method (such as GET, POST, PUT, DELETE) and the URL path.

In RESTful web services, an endpoint typically refers to a specific resource, such as a user, that can be accessed via the web using a specific URL. For example, a RESTful API might have an endpoint like "[https://example.com/api/users/123](https://example.com/api/users/123)" to retrieve a specific user with ID 123.

Endpoints can also be used in other contexts, such as WebSockets, where it is the address or URL of the server to which the client connects to establish a real-time connection.

In summary, an endpoint is the point where a client can access a specific resource or service that is exposed by the server.

Code snippets are small pieces of code that can be reused in different parts of a program. They are often used to automate repetitive tasks and to quickly add commonly-used functionality to a program. Code snippets can be written in any programming language and can range from a single line of code to a complete block of functionality.

Code snippets can be stored in a variety of ways, such as in a code library, an integrated development environment (IDE), or in a code snippet manager. Some common features of code snippet managers include the ability to organize and categorize snippets, search for specific snippets, and share snippets with others.

Here's an example of a code snippet written in Python that calculates the factorial of a number:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) # Output: 120

And an example of a code snippet written in JavaScript that logs the current date and time:

console.log(new Date().toString());

These are just examples, but code snippets can be any piece of code that you can reuse, adapt and save for future use.

Method GET

Endpoint:

http://127.0.0.1/MHT/apirule7/ping_v

Request Body

string(6269) "#0 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\Controller.php(54): App\Http\Controllers\API7UsersController->auth_v(Object(Illuminate\Http\Request))
#1 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\ControllerDispatcher.php(45): Illuminate\Routing\Controller->callAction('auth_v', Array)
#2 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\Route.php(261): Illuminate\Routing\ControllerDispatcher->dispatch(Object(Illuminate\Routing\Route), Object(App\Http\Controllers\API7UsersController), 'auth_v')
#3 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\Route.php(204): Illuminate\Routing\Route->runController()
#4 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\Router.php(695): Illuminate\Routing\Route->run()
#5 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Pipeline\Pipeline.php(128): Illuminate\Routing\Router->Illuminate\Routing\{closure}(Object(Illuminate\Http\Request))
#6 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\Middleware\SubstituteBindings.php(50): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
#7 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Pipeline\Pipeline.php(167): Illuminate\Routing\Middleware\SubstituteBindings->handle(Object(Illuminate\Http\Request), Object(Closure))
#8 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Pipeline\Pipeline.php(103): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
#9 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\Router.php(697): Illuminate\Pipeline\Pipeline->then(Object(Closure))
#10 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\Router.php(672): Illuminate\Routing\Router->runRouteWithinStack(Object(Illuminate\Routing\Route), Object(Illuminate\Http\Request))
#11 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\Router.php(636): Illuminate\Routing\Router->runRoute(Object(Illuminate\Http\Request), Object(Illuminate\Routing\Route))
#12 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\Router.php(625): Illuminate\Routing\Router->dispatchToRoute(Object(Illuminate\Http\Request))
#13 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Foundation\Http\Kernel.php(166): Illuminate\Routing\Router->dispatch(Object(Illuminate\Http\Request))
#14 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Pipeline\Pipeline.php(128): Illuminate\Foundation\Http\Kernel->Illuminate\Foundation\Http\{closure}(Object(Illuminate\Http\Request))
#15 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Foundation\Http\Middleware\TransformsRequest.php(21): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
#16 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Foundation\Http\Middleware\ConvertEmptyStringsToNull.php(31): Illuminate\Foundation\Http\Middleware\TransformsRequest->handle(Object(Illuminate\Http\Request), Object(Closure))
#17 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Pipeline\Pipeline.php(167): Illuminate\Foundation\Http\Middleware\ConvertEmptyStringsToNull->handle(Object(Illuminate\Http\Request), Object(Closure))
#18 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Foundation\Http\Middleware\TransformsRequest.php(21): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
#19 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Foundation\Http\Middleware\TrimStrings.php(40): Illuminate\Foundation\Http\Middleware\TransformsRequest->handle(Object(Illuminate\Http\Request), Object(Closure))
#20 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Pipeline\Pipeline.php(167): Illuminate\Foundation\Http\Middleware\TrimStrings->handle(Object(Illuminate\Http\Request), Object(Closure))
#21 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Foundation\Http\Middleware\ValidatePostSize.php(27): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
#22 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Pipeline\Pipeline.php(167): Illuminate\Foundation\Http\Middleware\ValidatePostSize->handle(Object(Illuminate\Http\Request), Object(Closure))
