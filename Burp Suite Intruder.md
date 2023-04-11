---
Learn how to use Intruder to automate requests in Burp Suite
---

# Burp Suite Intruder — Writeup

## Overview
### Burp Suite Intruder — Writeup
### Burp Suite Intruder — Writeup
### Room Outline
In previous rooms of this module, we have covered Burp Suite's Proxy and Repeater functionality. If you have not completed these rooms and are not familiar with these aspects of the framework, then you are advised to complete at least the Burp Basics room before proceeding.
This room will cover the third of Burp Suite's primary modules: Intruder.
Intruder allows us to automate requests, which is very useful when fuzzing or bruteforcing. We will be looking at how to use Intruder to perform both of these functions in conjunction with the other tools we have already covered.
Let's begin!
### What is Intruder?
Intruder is Burp Suite's in-built fuzzing tool. It allows us to take a request (usually captured in the Proxy before being passed into Intruder) and use it as a template to send many more requests with slightly altered values automatically. For example, by capturing a request containing a login attempt, we could then configure Intruder to swap out the username and password fields for values from a wordlist, effectively allowing us to bruteforce the login form. Similarly, we could pass in a fuzzing[1] wordlist and use Intruder to fuzz for subdirectories, endpoints, or virtual hosts. This functionality is very similar to that provided by command-line tools such as Wfuzz or Ffuf.
In short, as a method for automating requests, Intruder is extremely powerful -- there is just one problem: to access the full speed of Intruder, we need Burp Professional. We can still use Intruder with Burp Community, but it is heavily rate-limited. This speed restriction means that many hackers choose to use other tools for fuzzing and bruteforcing.
Limitations aside, Intruder is still very useful, so it is well worth learning to use it properly.
The first view we get is a relatively sparse interface that allows us to choose our target. Assuming that we sent a request in from the Proxy (by using Ctrl + I or right-clicking and selecting "Send to Intruder"), this should already be populated for us.
There are four other Intruder sub-tabs:
Positions allows us to select an Attack Type (we will cover these in an upcoming task), as well as configure where in the request template we wish to insert our payloads.
Payloads allows us to select values to insert into each of the positions we defined in the previous sub-tab. For example, we may choose to load items in from a wordlist to serve as payloads. How these get inserted into the template depends on the attack type we chose in the Positions tab. There are many payload types to choose from (anything from a simple wordlist to regexes based on responses from the server). The Payloads sub-tab also allows us to alter Intruder's behaviour with regards to payloads; for example, we can define pre-processing rules to apply to each payload (e.g. add a prefix or suffix, match and replace, or skip if the payload matches a defined regex).
Resource Pool is not particularly useful to us in Burp Community. It allows us to divide our resources between tasks. Burp Pro would allow us to run various types of automated tasks in the background, which is where we may wish to manually allocate our available memory and processing power between these automated tasks and Intruder. Without access to these automated tasks, there is little point in using this, so we won't devote much time to it.
As with most of the other Burp tools, Intruder allows us to configure attack behaviour in the Options sub-tab. The settings here apply primarily to how Burp handles results and how Burp handles the attack itself. For example, we can choose to flag requests that contain specified pieces of text or define how Burp responds to redirect (3xx) responses.
We will take a closer look at some of these sub-tabs in the upcoming tasks. For now, just get to know where things are in the interface.
1. Fuzzing is when we take a set of data and apply it to a parameter to test functionality or to see if something exists. For example, we may choose to "fuzz for endpoints" in a web application; this would involve taking each word in a wordlist and adding it to the end of a request to see how the web server responds (e.g. http://MACHINE_IP/WORD_GOES_HERE).
Which section of the Options sub-tab allows you to control what information will be captured in the Intruder results?
*attack results*
In which Intruder sub-tab can we define the "Attack type" for our planned attack?
*Positions*
### Positions
When we are looking to perform an attack with Intruder, the first thing we need to do is look at positions. Positions tell Intruder where to insert payloads (which we will look at in upcoming tasks).
Let's switch over to the Positions sub-tab:
Notice that Burp will attempt to determine the most likely places we may wish to insert a payload automatically -- these are highlighted in green and surrounded by silcrows (§).
On the right-hand side of the interface, we have the buttons labelled "Add §", "Clear §", and "Auto §":
Add lets us define new positions by highlighting them in the editor and clicking the button.
Clear removes all defined positions, leaving us with a blank canvas to define our own.
Auto attempts to select the most likely positions automatically; this is useful if we cleared the default positions and want them back.
Here is a GIF demonstrating the process of adding, clearing, and automatically reselecting positions:
GIF showing how to select positions
Have a play around with the positions selector. Make sure that you are comfortable with the processes of adding, clearing, and automatically selecting positions.
*No answer needed*
Clear all selected positions. *No answer needed*
Select the value of the "Host" header and add it as a position.
Your editor should look something like this:
![](https://assets.muirlandoracle.co.uk/thm/modules/burp/fed2938c4055.png)
Clear this position, then click the "Auto" button again to reselect the default positions.
Your editor should be back looking like it did in the first screenshot of this task.
*No answer needed*
### Introduction
Let's switch to the "Positions" sub-tab and look in the "Attack types" drop-down menu.
There are four attack types available:
Sniper
Battering ram
Pitchfork
Cluster bomb
We will look at each of these in turn.
### Sniper
Sniper is the first and most common attack type.
When conducting a sniper attack, we provide one set of payloads. For example, this could be a single file containing a wordlist or a range of numbers. From here on out, we will refer to a list of items to be slotted into requests using the Burp Suite terminology of a "Payload Set". Intruder will take each payload in a payload set and put it into each defined position in turn.
Take a look at our example template from before:
Example Positions
POST /support/login/ HTTP/1.1
Host: MACHINE_IP
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 37
Origin: http://MACHINE_IP
Connection: close
Referer: http://MACHINE_IP/support/login/
Upgrade-Insecure-Requests: 1
username=§pentester§&password=§Expl01ted§
There are two positions defined here, targeting the username and password body parameters.
In a sniper attack, Intruder will take each position and substitute each payload into it in turn.
For example, let's assume we have a wordlist with three words in it: burp, suite, and intruder.
With the two positions that we have above, Intruder would use these words to make six requests:
Request Number
Request Body
1
username=burp&password=Expl01ted
2
username=suite&password=Expl01ted
3
username=intruder&password=Expl01ted
4
username=pentester&password=burp
5
username=pentester&password=suite
6
username=pentester&password=intruder
Notice how Intruder starts with the first position (username) and tries each of our payloads, then moves to the second position and tries the same payloads again. We can calculate the number of requests that Intruder Sniper will make as requests = numberOfWords * numberOfPositions.
This quality makes Sniper very good for single-position attacks (e.g. a password bruteforce if we know the username or fuzzing for API endpoints).
If you were using Sniper to fuzz three parameters in a request, with a wordlist containing 100 words, how many requests would Burp Suite need to send to complete the attack? *300*
How many sets of payloads will Sniper accept for conducting an attack? *1*
Sniper is good for attacks where we are only attacking a single parameter, aye or nay?*aye*
### Battering Ram
Next, let's take a look at the Battering Ram Attack type.
Like Sniper, Battering ram takes one set of payloads (e.g. one wordlist). Unlike Sniper, the Battering ram puts the same payload in every position rather than in each position in turn.
Let's use the same wordlist and example request as we did in the last task to illustrate this.
Example Positions
POST /support/login/ HTTP/1.1
Host: MACHINE_IP
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 37
Origin: http://MACHINE_IP
Connection: close
Referer: http://MACHINE_IP/support/login/
Upgrade-Insecure-Requests: 1
username=§pentester§&password=§Expl01ted§
If we use Battering ram to attack this, Intruder will take each payload and substitute it into every position at once.
With the two positions that we have above, Intruder would use the three words from before (burp, suite, and intruder) to make three requests:
Request Number
Request Body
1
username=burp&password=burp
2
username=suite&password=suite
3
username=intruder&password=intruder
As can be seen in the table, each item in our list of payloads gets put into every position for each request. True to the name, Battering ram just throws payloads at the target to see what sticks.
As a hypothetical question: you need to perform a Battering Ram Intruder attack on the example request above.
If you have a wordlist with two words in it (admin and Guest) and the positions in the request template look like this:
username=§pentester§&password=§Expl01ted§
What would the body parameters of the first request that Burp Suite sends be?
*username=admin&password=admin*
### Pitchfork
Two down, two more to go!
After Sniper, Pitchfork is the attack type you are most likely to use. It may help to think of Pitchfork as being like having numerous Snipers running simultaneously. Where Sniper uses one payload set (which it uses on every position simultaneously), Pitchfork uses one payload set per position (up to a maximum of 20) and iterates through them all at once.
This type of attack can take a little time to get your head around, so let's use our bruteforce example from before, but this time we need two wordlists:
Our first wordlist will be usernames. It contains three entries: joel, harriet, alex.
Let's say that Joel, Harriet, and Alex have had their passwords leaked: we know that Joel's password is J03l, Harriet's password is Emma1815, and Alex's password is Sk1ll.
We can use these two lists to perform a pitchfork attack on the login form from before. The process for carrying out this attack will not be covered in this task, but you will get plenty of opportunities to perform attacks like this later!
When using Intruder in pitchfork mode, the requests made would look something like this:
Request Number
Request Body
1
username=joel&password=J03l
2
username=harriet&password=Emma1815
3
username=alex&password=Sk1ll
See how Pitchfork takes the first item from each list and puts them into the request, one per position? It then repeats this for the next request: taking the second item from each list and substituting it into the template. Intruder will keep doing this until one (or all) of the lists run out. Ideally, our payload sets should be identical lengths when working in Pitchfork, as Intruder will stop testing as soon as one of the lists is complete. For example, if we have two lists, one with 100 lines and one with 90 lines, Intruder will only make 90 requests, and the final ten items in the first list will not get tested.
This attack type is exceptionally useful when forming things like credential stuffing attacks (we have just encountered a small-scale version of this). We will be looking more into these later in the room.
What is the maximum number of payload sets we can load into Intruder in Pitchfork mode? *20*
### Cluster Bomb
Finally, we come to the last of Intruder's attack types: the Cluster Bomb.
Like Pitchfork, Cluster bomb allows us to choose multiple payload sets: one per position, up to a maximum of 20; however, whilst Pitchfork iterates through each payload set simultaneously, Cluster bomb iterates through each payload set individually, making sure that every possible combination of payloads is tested.
Again, the best way to visualise this is with an example.
Let's use the same wordlists as before:
Usernames: joel, harriet, alex.
Passwords: J03l, Emma1815, Sk1ll.
But, this time, let's assume that we don't know which password belongs to which user. We have three users and three passwords, but we don't know how to match them up. In this case, we would use a cluster bomb attack; this will try every combination of values. The request table for our username and password positions looks something like this:
Request Number
Request Body
1
username=joel&password=J03l
2
username=harriet&password=J03l
3
username=alex&password=J03l
4
username=joel&password=Emma1815
5
username=harriet&password=Emma1815
6
username=alex&password=Emma1815
7
username=joel&password=Sk1ll
8
username=harriet&password=Sk1ll
9
username=alex&password=Sk1ll
Cluster Bomb will iterate through every combination of the provided payload sets to ensure that every possibility has been tested. This attack-type can create a huge amount of traffic (equal to the number of lines in each payload set multiplied together), so be careful! Equally, when using Burp Community and its Intruder rate-limiting, be aware that a Cluster Bomb attack with any moderately sized payload set will take an incredibly long time.
That said, this is another extremely useful attack type for any kind of credential bruteforcing where a username isn't known.
We have three payload sets. The first set contains 100 lines; the second contains 2 lines; and the third contains 30 lines.
How many requests will Intruder make using these payload sets in a Cluster Bomb attack? *6000* (Multiply the number of lines in each payload set together. See how very small numbers can add up fast...?)
### Payloads
That was a lot of theory, so kudos for reading through it! There will be plenty of practicals in the upcoming tasks, but first, it is imperative that we understand how to create, assign, and use payloads.
Switch over to the "Payloads" sub-tab; this is split into four sections:
The Payload Sets section allows us to choose which position we want to configure a set for as well as what type of payload we would like to use.
When we use an attack type that only allows for a single payload set (i.e. Sniper or Battering Ram), the dropdown menu for "Payload Set" will only have one option, regardless of how many positions we have defined.
If we are using one of the attack types that use multiple payload sets (i.e. Pitchfork or Cluster Bomb), then there will be one item in the dropdown for each position.
Note: Multiple positions should be read from top to bottom, then left to right when being assigned numbers in the "Payload set" dropdown. For example, with two positions (username=§pentester§&password=§Expl01ted§), the first item in the payload set dropdown would refer to the username field, and the second would refer to the password field.
The second dropdown in this section allows us to select a "payload type". By default, this is a "Simple list" -- which, as the name suggests, lets us load in a wordlist to use. There are many other payload types available -- some common ones include: Recursive Grep, Numbers, and Username generator. It is well worth perusing this list to get a feel for the wide range of options available.
Payload Options differ depending on the payload type we select for the current payload set. For example, a "Simple List" payload type will give us a box to add and remove payloads to and from the set:
