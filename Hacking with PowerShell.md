---
Learn the basics of PowerShell and PowerShell Scripting
---

# Hacking with PowerShell — Writeup

## Overview
### Hacking with PowerShell — Writeup
### Hacking with PowerShell — Writeup
![](https://i.imgur.com/xFIv4Ve.png)
![|222](https://i.imgur.com/hiUDlNA.png)
In this room, we'll be exploring the following concepts:
What is Powershell and how it works
Basic Powershell commands
Windows enumeration with Powershell
Powershell scripting
You can control the machine in your browser or RDP into the instance with the following credentials:
Username: Administrator
Password: BHN2UVw0Q
Please note that this machine does not respond to ping (ICMP) and may take a few minutes to boot up.
### What is Powershell?
Powershell is the Windows Scripting Language and shell environment that is built using the .NET framework.
This also allows Powershell to execute .NET functions directly from its shell. Most Powershell commands, called cmdlets, are written in .NET. Unlike other scripting languages and shell environments, the output of these cmdlets are objects - making Powershell somewhat object oriented. This also means that running cmdlets allows you to perform actions on the output object(which makes it convenient to pass output from one cmdlet to another). The normal format of a cmdlet is represented using Verb-Noun; for example the cmdlet to list commands is called Get-Command.
Common verbs to use include:
Get
Start
Stop
Read
Write
New
Out
To get the full list of approved verbs, visit thisn [link](https://learn.microsoft.com/en-us/powershell/scripting/developer/cmdlet/approved-verbs-for-windows-powershell-commands?view=powershell-7).
```text
┌──(kali㉿kali)-[~]
└─$ xfreerdp /u:'Administrator' /p:'BHN2UVw0Q' /v:10.10.191.198 /size:85%

Windows PowerShell
Copyright (C) 2016 Microsoft Corporation. All rights reserved.

PS C:\Users\Administrator> get-help

TOPIC
    Windows PowerShell Help System

SHORT DESCRIPTION
    Displays help about Windows PowerShell cmdlets and concepts.

LONG DESCRIPTION
    Windows PowerShell Help describes Windows PowerShell cmdlets,
    functions, scripts, and modules, and explains concepts, including
    the elements of the Windows PowerShell language.

    Windows PowerShell does not include help files, but you can read the
    help topics online, or use the Update-Help cmdlet to download help files
    to your computer and then use the Get-Help cmdlet to display the help
    topics at the command line.

    You can also use the Update-Help cmdlet to download updated help files
    as they are released so that your local help content is never obsolete.

    Without help files, Get-Help displays auto-generated help for cmdlets,
    functions, and scripts.
```
What is the command to get help about a particular cmdlet(without any parameters)?
*GET-HELP*
### Basic Powershell Commands
Now that we've understood how cmdlets works - let's explore how to use them! The main thing to remember here is that Get-Command and Get-Help are your best friends!
Using Get-Help
Get-Help displays information about a cmdlet. To get help about a particular command, run the following:
Get-Help Command-Name
You can also understand how exactly to use the command by passing in the -examples flag. This would return output like the following:
![](https://i.imgur.com/U5Mlirh.png)
Using Get-Command
Get-Command gets all the cmdlets installed on the current Computer. The great thing about this cmdlet is that it allows for pattern matching like the following
Get-Command Verb-* or Get-Command *-Noun
Running Get-Command New-* to view all the cmdlets for the verb new displays the following:
![](https://i.imgur.com/KEzbPUI.png)
Object Manipulation
In the previous task, we saw how the output of every cmdlet is an object. If we want to actually manipulate the output, we need to figure out a few things:
passing output to other cmdlets
using specific object cmdlets to extract information
The Pipeline(|) is used to pass output from one cmdlet to another. A major difference compared to other shells is that instead of passing text or string to the command after the pipe, powershell passes an object to the next cmdlet. Like every object in object oriented frameworks, an object will contain methods and properties. You can think of methods as functions that can be applied to output from the cmdlet and you can think of properties as variables in the output from a cmdlet. To view these details, pass the output of a cmdlet to the Get-Member cmdlet
Verb-Noun | Get-Member
An example of running this to view the members for Get-Command is:
Get-Command | Get-Member -MemberType Method
![](https://i.imgur.com/OlwXSbS.png)
From the above flag in the command, you can see that you can also select between methods and properties.
Creating Objects From Previous cmdlets
One way of manipulating objects is pulling out the properties from the output of a cmdlet and creating a new object. This is done using the Select-Object cmdlet.
Here's an example of listing the directories and just selecting the mode and the name:
![](https://i.imgur.com/Zdxicjj.png)
You can also use the following flags to select particular information:
first - gets the first x object
last - gets the last x object
unique - shows the unique objects
skip - skips x objects
Filtering Objects
When retrieving output objects, you may want to select objects that match a very specific value. You can do this using the Where-Object to filter based on the value of properties.
The general format of the using this cmdlet is
Verb-Noun | Where-Object -Property PropertyName -operator Value
Verb-Noun | Where-Object {$_.PropertyName -operator Value}
The second version uses the $_ operator to iterate through every object passed to the Where-Object cmdlet.
Powershell is quite sensitive so make sure you don't put quotes around the command!
Where -operator is a list of the following operators:
-Contains: if any item in the property value is an exact match for the specified value
-EQ: if the property value is the same as the specified value
-GT: if the property value is greater than the specified value
For a full list of operators, use this link.
Here's an example of checking the stopped processes:
![](https://i.imgur.com/obTvbWW.png)
Sort Object
When a cmdlet outputs a lot of information, you may need to sort it to extract the information more efficiently. You do this by pipe lining the output of a cmdlet to the Sort-Object cmdlet.
The format of the command would be
Verb-Noun | Sort-Object
Here's an example of sort the list of directories:
![](https://i.imgur.com/xob5cqe.png)
Now that you've understood the basics of how Powershell works, let try some commands to apply this knowledge!
```text
PS C:\Users\Administrator> Get-ChildItem -Path C:\ -Include *interesting-file.txt* -File -Recurse -ErrorAction SilentlyContinue

    Directory: C:\Program Files

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        10/3/2019  11:38 PM             23 interesting-file.txt.txt

SyntaxError: Invalid or unexpected token in /usr/src/tryhackme/views/dashboard.ejs while compiling ejs

If the above error is not helpful, you may want to try EJS-Lint:
https://github.com/RyanZim/EJS-Lint
    at new Function (<anonymous>)
    at Template.compile (/usr/src/tryhackme/node_modules/ejs/lib/ejs.js:592:12)
    at Object.compile (/usr/src/tryhackme/node_modules/ejs/lib/ejs.js:388:16)
    at handleCache (/usr/src/tryhackme/node_modules/ejs/lib/ejs.js:212:18)
    at tryHandleCache (/usr/src/tryhackme/node_modules/ejs/lib/ejs.js:251:16)
    at View.exports.renderFile [as engine] (/usr/src/tryhackme/node_modules/ejs/lib/ejs.js:480:10)
    at View.render (/usr/src/tryhackme/node_modules/express/lib/view.js:135:8)
    at tryRender (/usr/src/tryhackme/node_modules/express/lib/application.js:640:10)
    at Function.render (/usr/src/tryhackme/node_modules/express/lib/application.js:592:3)
    at ServerResponse.render (/usr/src/tryhackme/node_modules/express/lib/response.js:1017:7)
    at /usr/src/tryhackme/app/routes/pages.js:231:7
    at runMicrotasks (<anonymous>)
    at processTicksAndRejections (internal/process/task_queues.js:95:5)

now is fine :)

PS C:\Users\Administrator> Get-Content "C:\Program Files\interesting-file.txt.txt"
notsointerestingcontent
```
What is the location of the file "interesting-file.txt"
*C:\Program Files*
Specify the contents of this file
*notsointerestingcontent*
```text
PS C:\Users\Administrator> Get-Command | Where-Object -Property CommandType -eq Cmdlet | measure

Count    : 6638
Average  :
Sum      :
Maximum  :
Minimum  :
Property :
```
How many cmdlets are installed on the system(only cmdlets, not functions and aliases)?
*6638*
```text
PS C:\Users\Administrator> Get-FileHash -Path "C:\Program Files\interesting-file.txt.txt" -Algorithm MD5

Algorithm       Hash                                                                   Path
---------       ----                                                                   ----
MD5             49A586A2A9456226F8A1B4CEC6FAB329                                       C:\Program Files\interesting-...
```
Get the MD5 hash of interesting-file.txt
*49A586A2A9456226F8A1B4CEC6FAB329*
```text
PS C:\Users\Administrator> Get-Location

Path
----
C:\Users\Administrator
```
What is the command to get the current working directory?
*Get-Location*
```text
PS C:\Users\Administrator> Get-Location -Path "C:\Users\Administrator\Documents\Passwords"
Get-Location : A parameter cannot be found that matches parameter name 'Path'.
At line:1 char:14
+ Get-Location -Path "C:\Users\Administrator\Documents\Passwords"
+              ~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Get-Location], ParameterBindingException
    + FullyQualifiedErrorId : NamedParameterNotFound,Microsoft.PowerShell.Commands.GetLocationCommand
```
Does the path "C:\Users\Administrator\Documents\Passwords" Exist(Y/N)?
*N*
```text
PS C:\Users\Administrator> Invoke-WebRequest

cmdlet Invoke-WebRequest at command pipeline position 1
Supply values for the following parameters:
Uri:
```
What command would you use to make a request to a web server?
*Invoke-WebRequest*
```text
PS C:\Users\Administrator> Get-ChildItem -Path C:/ -Include b64.txt -Recurse -File

    Directory: C:\Users\Administrator\Desktop

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        10/3/2019  11:56 PM            432 b64.txt
Get-ChildItem : Access to the path 'C:\Windows\System32\LogFiles\WMI\RtBackup' is denied.
At line:1 char:1
+ Get-ChildItem -Path C:/ -Include b64.txt -Recurse -File
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\Windows\Syst...es\WMI\RtBackup:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand

PS C:\Users\Administrator> certutil -decode "C:\Users\Administrator\Desktop\b64.txt" decode.txt
Input Length = 432
Output Length = 323
CertUtil: -decode command completed successfully.

PS C:\Users\Administrator> Get-Content .\decode.txt
this is the flag - ihopeyoudidthisonwindows
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
```
Base64 decode the file b64.txt on Windows.
*ihopeyoudidthisonwindows*

## Enumeration
The first step when you have gained initial access to any machine would be to enumerate. We'll be enumerating the following:
users
basic networking information
file permissions
registry permissions
scheduled and running tasks
insecure files
Your task will be to answer the following questions to enumerate the machine using Powershell commands!
```text
PS C:\Users\Administrator> Get-LocalUser

Name           Enabled Description
----           ------- -----------
Administrator  True    Built-in account for administering the computer/domain
DefaultAccount False   A user account managed by the system.
duck           True
duck2          True
Guest          False   Built-in account for guest access to the computer/domain
```
How many users are there on the machine?
*5*
```text
PS C:\Users\Administrator> Get-LocalUser -SID "S-1-5-21-1394777289-3961777894-1791813945-501"

Name  Enabled Description
----  ------- -----------
Guest False   Built-in account for guest access to the computer/domain
```
Which local user does this SID(S-1-5-21-1394777289-3961777894-1791813945-501) belong to?
*Guest*
```text
PS C:\Users\Administrator> Get-LocalUser | Where-Object -Property PasswordRequired -Match false

Name           Enabled Description
----           ------- -----------
DefaultAccount False   A user account managed by the system.
duck           True
duck2          True
Guest          False   Built-in account for guest access to the computer/domain
```
How many users have their password required values set to False?
*4*
```text
PS C:\Users\Administrator> Get-LocalGroup | measure

Count    : 24
Average  :
Sum      :
Maximum  :
Minimum  :
Property :
```
How many local groups exist?
*24*
```text
PS C:\Users\Administrator> Get-NetIPAddress

IPAddress         : fe80::4ac:13a8:f5f5:bba8%7
InterfaceIndex    : 7
InterfaceAlias    : Local Area Connection* 3
AddressFamily     : IPv6
Type              : Unicast
PrefixLength      : 64
PrefixOrigin      : WellKnown
SuffixOrigin      : Link
AddressState      : Preferred
ValidLifetime     : Infinite ([TimeSpan]::MaxValue)
PreferredLifetime : Infinite ([TimeSpan]::MaxValue)
SkipAsSource      : False
PolicyStore       : ActiveStore

IPAddress         : 2001:0:2851:782c:4ac:13a8:f5f5:bba8
InterfaceIndex    : 7
InterfaceAlias    : Local Area Connection* 3
AddressFamily     : IPv6
Type              : Unicast
PrefixLength      : 64
PrefixOrigin      : RouterAdvertisement
SuffixOrigin      : Link
AddressState      : Preferred
ValidLifetime     : Infinite ([TimeSpan]::MaxValue)
PreferredLifetime : Infinite ([TimeSpan]::MaxValue)
SkipAsSource      : False
PolicyStore       : ActiveStore

IPAddress         : fe80::5526:99f8:23c7:8905%5
InterfaceIndex    : 5
InterfaceAlias    : Ethernet
AddressFamily     : IPv6
Type              : Unicast
PrefixLength      : 64
PrefixOrigin      : WellKnown
SuffixOrigin      : Link
AddressState      : Preferred
ValidLifetime     : Infinite ([TimeSpan]::MaxValue)
PreferredLifetime : Infinite ([TimeSpan]::MaxValue)
SkipAsSource      : False
PolicyStore       : ActiveStore

IPAddress         : fe80::5efe:10.10.68.87%6
InterfaceIndex    : 6
InterfaceAlias    : Reusable ISATAP Interface {90ABCE23-305A-4BDE-AA39-4FFDA7413134}
AddressFamily     : IPv6
Type              : Unicast
PrefixLength      : 128
PrefixOrigin      : WellKnown
SuffixOrigin      : Link
AddressState      : Deprecated
ValidLifetime     : Infinite ([TimeSpan]::MaxValue)
PreferredLifetime : Infinite ([TimeSpan]::MaxValue)
SkipAsSource      : False
PolicyStore       : ActiveStore

IPAddress         : ::1
InterfaceIndex    : 1
InterfaceAlias    : Loopback Pseudo-Interface 1
AddressFamily     : IPv6
Type              : Unicast
PrefixLength      : 128
PrefixOrigin      : WellKnown
SuffixOrigin      : WellKnown
AddressState      : Preferred
ValidLifetime     : Infinite ([TimeSpan]::MaxValue)
PreferredLifetime : Infinite ([TimeSpan]::MaxValue)
SkipAsSource      : False
PolicyStore       : ActiveStore

IPAddress         : 10.10.68.87
InterfaceIndex    : 5
InterfaceAlias    : Ethernet
AddressFamily     : IPv4
Type              : Unicast
PrefixLength      : 16
PrefixOrigin      : Dhcp
SuffixOrigin      : Dhcp
AddressState      : Preferred
ValidLifetime     : 00:44:59
PreferredLifetime : 00:44:59
SkipAsSource      : False
PolicyStore       : ActiveStore

IPAddress         : 127.0.0.1
InterfaceIndex    : 1
InterfaceAlias    : Loopback Pseudo-Interface 1
AddressFamily     : IPv4
Type              : Unicast
PrefixLength      : 8
PrefixOrigin      : WellKnown
SuffixOrigin      : WellKnown
AddressState      : Preferred
ValidLifetime     : Infinite ([TimeSpan]::MaxValue)
PreferredLifetime : Infinite ([TimeSpan]::MaxValue)
SkipAsSource      : False
PolicyStore       : ActiveStore
```
What command did you use to get the IP address info?
*Get-NetIPAddress*
```text
PS C:\Users\Administrator> GEt-NetTCPConnection | Where-Object -Property State -Match Listen | measure

Count    : 20
Average  :
Sum      :
Maximum  :
Minimum  :
Property :
```
How many ports are listed as listening?
*20*
```text
PS C:\Users\Administrator> GEt-NetTCPConnection | Where-Object -Property State -Match Listen

LocalAddress                        LocalPort RemoteAddress                       RemotePort State       AppliedSetting OwningProcess
------------                        --------- -------------                       ---------- -----       -------------- -------------
::                                  49676     ::                                  0          Listen                     728
::                                  49673     ::                                  0          Listen                     716
::                                  49667     ::                                  0          Listen                     1680
::                                  49666     ::                                  0          Listen                     988
::                                  49665     ::                                  0          Listen                     496
::                                  49664     ::                                  0          Listen                     616
::                                  47001     ::                                  0          Listen                     4
::                                  5985      ::                                  0          Listen                     4
::                                  3389      ::                                  0          Listen                     996
::                                  445       ::                                  0          Listen                     4
::                                  135       ::                                  0          Listen                     852
0.0.0.0                             49676     0.0.0.0                             0          Listen                     728
0.0.0.0                             49673     0.0.0.0                             0          Listen                     716
0.0.0.0                             49667     0.0.0.0                             0          Listen                     1680
0.0.0.0                             49666     0.0.0.0                             0          Listen                     988
0.0.0.0                             49665     0.0.0.0                             0          Listen                     496
0.0.0.0                             49664     0.0.0.0                             0          Listen                     616
0.0.0.0                             3389      0.0.0.0                             0          Listen                     996
10.10.68.87                         139       0.0.0.0                             0          Listen                     4
0.0.0.0                             135       0.0.0.0                             0          Listen                     852
```
What is the remote address of the local port listening on port 445?
*::*
```text
PS C:\Users\Administrator> Get-Hotfix | measure

Count    : 20
Average  :
Sum      :
Maximum  :
Minimum  :
Property :

PS C:\Users\Administrator> Get-Hotfix

Source        Description      HotFixID      InstalledBy          InstalledOn
------        -----------      --------      -----------          -----------
EC2AMAZ-5M... Update           KB3176936                          10/18/2016 12:00:00 AM
EC2AMAZ-5M... Update           KB3186568     NT AUTHORITY\SYSTEM  6/15/2017 12:00:00 AM
EC2AMAZ-5M... Update           KB3192137     NT AUTHORITY\SYSTEM  9/12/2016 12:00:00 AM
EC2AMAZ-5M... Update           KB3199209     NT AUTHORITY\SYSTEM  10/18/2016 12:00:00 AM
EC2AMAZ-5M... Update           KB3199986     EC2AMAZ-5M13VM2\A... 11/15/2016 12:00:00 AM
EC2AMAZ-5M... Update           KB4013418     EC2AMAZ-5M13VM2\A... 3/16/2017 12:00:00 AM
EC2AMAZ-5M... Update           KB4023834     EC2AMAZ-5M13VM2\A... 6/15/2017 12:00:00 AM
EC2AMAZ-5M... Update           KB4035631     NT AUTHORITY\SYSTEM  8/9/2017 12:00:00 AM
EC2AMAZ-5M... Update           KB4049065     NT AUTHORITY\SYSTEM  11/17/2017 12:00:00 AM
EC2AMAZ-5M... Update           KB4089510     NT AUTHORITY\SYSTEM  3/24/2018 12:00:00 AM
EC2AMAZ-5M... Update           KB4091664     NT AUTHORITY\SYSTEM  1/10/2019 12:00:00 AM
EC2AMAZ-5M... Update           KB4093137     NT AUTHORITY\SYSTEM  4/11/2018 12:00:00 AM
EC2AMAZ-5M... Update           KB4132216     NT AUTHORITY\SYSTEM  6/13/2018 12:00:00 AM
EC2AMAZ-5M... Security Update  KB4465659     NT AUTHORITY\SYSTEM  11/19/2018 12:00:00 AM
EC2AMAZ-5M... Security Update  KB4485447     NT AUTHORITY\SYSTEM  2/13/2019 12:00:00 AM
EC2AMAZ-5M... Security Update  KB4498947     NT AUTHORITY\SYSTEM  5/15/2019 12:00:00 AM
EC2AMAZ-5M... Security Update  KB4503537     NT AUTHORITY\SYSTEM  6/12/2019 12:00:00 AM
EC2AMAZ-5M... Security Update  KB4509091     NT AUTHORITY\SYSTEM  9/6/2019 12:00:00 AM
EC2AMAZ-5M... Security Update  KB4512574     NT AUTHORITY\SYSTEM  9/11/2019 12:00:00 AM
EC2AMAZ-5M... Security Update  KB4516044     NT AUTHORITY\SYSTEM  9/11/2019 12:00:00 AM
```
How many patches have been applied?
*20*
```text
PS C:\Users\Administrator> Get-Hotfix -Id KB4023834

Source        Description      HotFixID      InstalledBy          InstalledOn
------        -----------      --------      -----------          -----------
EC2AMAZ-5M... Update           KB4023834     EC2AMAZ-5M13VM2\A... 6/15/2017 12:00:00 AM
```
When was the patch with ID KB4023834 installed?
*6/15/2017 12:00:00 AM*
```text
PS C:\Users\Administrator> Get-ChildItem -Path C:\ -Include *.bak* -File -Recurse -ErrorAction SilentlyContinue

    Directory: C:\Program Files (x86)\Internet Explorer

Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        10/4/2019  12:42 AM             12 passwords.bak.txt

PS C:\Users\Administrator> Get-Content "C:\Program Files (x86)\Internet Explorer\passwords.bak.txt"
backpassflag
```
Find the contents of a backup file.
*backpassflag*
```text
PS C:\Users\Administrator> Get-ChildItem C:\* -Recurse | Select-String -pattern API_KEY

C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.dll:17824:     TLS_1_0 GB_6_1 Nullable`1 List`1 TLS_1_2 GB_58_2 IMarsh
aller`2 IRequestMarshaller`2 IUnmarshaller`2 ListUnmarshaller`2 KeyValuePair`2 IDictionary`2 FAIL_WITH_403 Int64 GB_28_4 DictionaryUnmarsh
aller`4 GB_0_5 GB_13_5 GB_1_6 GB_237 GB_118 get_UTF8 <Module> QUOTA_EXCEEDED ACCESS_DENIED FAILED THROTTLED UNDOCUMENTED UNAUTHORIZED RESO
URCE_NOT_FOUND METHOD RESOURCE EDGE REQUEST_TOO_LARGE NOT_AVAILABLE UNSUPPORTED_MEDIA_TYPE INTEGRATION_FAILURE AUTHORIZER_FAILURE INVALID_
SIGNATURE RESPONSE PRIVATE PENDING UPDATING DELETING MONTH API MOCK WEEK VPC_LINK REGIONAL MODEL EXPIRED_TOKEN MISSING_AUTHENTICATION_TOKE
N System.IO HTTP SUCCEED_WITH_RESPONSE_HEADER SUCCEED_WITHOUT_RESPONSE_HEADER REQUEST_HEADER PATH_PARAMETER QUERY_PARAMETER AUTHORIZER API
_CONFIGURATION_ERROR AUTHORIZER_CONFIGURATION_ERROR COGNITO_USER_POOLS BAD_REQUEST_PARAMETERS CREATE_IN_PROGRESS DELETE_IN_PROGRESS FLUSH_
IN_PROGRESS AWS INTERNET REQUEST INTEGRATION_TIMEOUT CONVERT_TO_TEXT DEFAULT_4XX DEFAULT_5XX DAY RESPONSE_BODY BAD_REQUEST_BODY INVALID_AP
I_KEY CONVERT_TO_BINARY HTTP_PROXY AWS_PROXY get_Schema set_Schema IsSetSchema _schema get_ResponseData IWebResponseData IServiceMetadata
get_ServiceMetadata serviceMetadata AmazonAPIGatewayMetadata get_Quota set_Quota IsSetQuota _quota mscorlib get_PercentTraffic set_Percent
Traffic IsSetPercentTraffic _percentTraffic System.Collections.Generic InvokeSync InvokeAsync get_Id set_Id get_ServiceId get_ResourceId s
et_ResourceId IsSetResourceId _resourceId get_RegionalHostedZoneId set_RegionalHostedZoneId IsSetRegionalHostedZoneId _regionalHostedZoneI
d get_DistributionHostedZoneId set_DistributionHostedZoneId IsSetDistributionHostedZoneId _distributionHostedZoneId get_ClientCertificateI
d set_ClientCertificateId IsSetClientCertificateId _clientCertificateId get_ApiId set_ApiId IsSetApiId get_RestApiId set_RestApiId IsSetRe
stApiId _restApiId _apiId get_VpcLinkId set_VpcLinkId IsSetVpcLinkId _vpcLinkId get_PrincipalId set_PrincipalId IsSetPrincipalId _principa
lId get_UsagePlanId set_UsagePlanId IsSetUsagePlanId _usagePlanId get_ConnectionId set_ConnectionId IsSetConnectionId _connectionId get_Cu
stomerId set_CustomerId IsSetCustomerId _customerId get_AuthorizerId set_AuthorizerId IsSetAuthorizerId _authorizerId get_RequestValidator
Id set_RequestValidatorId IsSetRequestValidatorId _requestValidatorId get_GenerateDistinctId set_GenerateDistinctId IsSetGenerateDistinctI
d _generateDistinctId IsSetId get_DeploymentId set_DeploymentId IsSetDeploymentId _deploymentId get_ParentId set_ParentId IsSetParentId _p
arentId get_DocumentationPartId set_DocumentationPartId IsSetDocumentationPartId _documentationPartId get_RequestId requestId get_KeyId se
t_KeyId awsAccessKeyId IsSetKeyId _keyId Read Add get_Embed set_Embed IsSetEmbed _embed get_Enabled set_Enabled get_DataTraceEnabled set_D
ataTraceEnabled IsSetDataTraceEnabled _dataTraceEnabled get_TracingEnabled set_TracingEnabled IsSetTracingEnabled _tracingEnabled get_Cach
ingEnabled set_CachingEnabled IsSetCachingEnabled _cachingEnabled get_CacheClusterEnabled set_CacheClusterEnabled IsSetCacheClusterEnabled
 _cacheClusterEnabled get_MetricsEnabled set_MetricsEnabled IsSetMetricsEnabled _metricsEnabled IsSetEnabled _enabled get_Required set_Req
uired IsSetRequired get_ApiKeyRequired set_ApiKeyRequired IsSetApiKeyRequired _apiKeyRequired _required get_CacheDataEncrypted set_CacheDa
taEncrypted IsSetCacheDataEncrypted _cacheDataEncrypted _id WriteObjectEnd WriteArrayEnd get_Method set_Method EndTestInvokeMethod BeginTe
stInvokeMethod EndUpdateMethod BeginUpdateMethod EndDeleteMethod BeginDeleteMethod get_HttpMethod set_HttpMethod get_IntegrationHttpMethod
 set_IntegrationHttpMethod IsSetIntegrationHttpMethod _integrationHttpMethod IsSetHttpMethod _httpMethod EndGetMethod BeginGetMethod IsSet
Method EndPutMethod BeginPutMethod _method get_Period set_Period IsSetPeriod _period Replace get_CacheNamespace set_CacheNamespace IsSetCa
cheNamespace _cacheNamespace IAmazonService get_Instance GetInstance _instance get_ApiKeySource set_ApiKeySource IsSetApiKeySource _apiKey
Source get_IdentitySource set_IdentitySource IsSetIdentitySource _identitySource AddSubResource EndUpdateResource BeginUpdateResource EndC
reateResource BeginCreateResource EndDeleteResource BeginDeleteResource EndTagResource BeginTagResource EndUntagResource BeginUntagResourc
e AddPathResource EndGetResource BeginGetResource get_Code errorCode get_StatusCode set_StatusCode HttpStatusCode IsSetStatusCode _statusC
ode get_ProductCode set_ProductCode IsSetProductCode _productCode get_Mode set_Mode IsSetMode PutMode _mode EndUpdateUsage BeginUpdateUsag
e EndGetUsage BeginGetUsage get_Message get_StatusMessage set_StatusMessage get_DomainNameStatusMessage set_DomainNameStatusMessage IsSetD
omainNameStatusMessage _domainNameStatusMessage IsSetStatusMessage _statusMessage message get_Stage set_Stage EndUpdateStage BeginUpdateSt
age EndCreateStage BeginCreateStage EndDeleteStage BeginDeleteStage ApiStage EndGetStage BeginGetStage IsSetStage _stage Merge get_UseStag
eCache set_UseStageCache IsSetUseStageCache _useStageCache EndFlushStageCache BeginFlushStageCache EndFlushStageAuthorizersCache BeginFlus
hStageAuthorizersCache EndInvoke PreInvoke BeginInvoke IDisposable get_Throttle set_Throttle IsSetThrottle _throttle get_Name set_Name set
_AuthenticationServiceName get_RegionEndpointServiceName get_StageName set_StageName IsSetStageName _stageName get_CertificateName set_Cer
tificateName get_RegionalCertificateName set_RegionalCertificateName IsSetRegionalCertificateName _regionalCertificateName IsSetCertificat
eName _certificateName get_ModelName set_ModelName IsSetModelName _modelName get_DomainName set_DomainName EndUpdateDomainName BeginUpdate
DomainName EndCreateDomainName BeginCreateDomainName EndDeleteDomainName BeginDeleteDomainName get_RegionalDomainName set_RegionalDomainNa
me IsSetRegionalDomainName _regionalDomainName get_DistributionDomainName set_DistributionDomainName IsSetDistributionDomainName _distribu
tionDomainName EndGetDomainName BeginGetDomainName IsSetDomainName _domainName get_OperationName set_OperationName IsSetOperationName _ope
rationName IsSetName get_FriendlyName set_FriendlyName IsSetFriendlyName _friendlyName WritePropertyName _name DateTime Amazon.Runtime Cus
tomizeRuntimePipeline pipeline get_Type set_Type QuotaPeriodType ApiKeySourceType get_ResponseType set_ResponseType IsSetResponseType Gate
wayResponseType _responseType get_AuthType set_AuthType IsSetAuthType _authType get_SdkType set_SdkType EndGetSdkType BeginGetSdkType IsSe
tSdkType _sdkType get_CurrentTokenType IntegrationType get_AuthorizationType set_AuthorizationType IsSetAuthorizationType _authorizationTy
pe get_ConnectionType set_ConnectionType IsSetConnectionType _connectionType AuthorizerType ErrorType errorType LocationStatusType IsSetTy
pe get_ContentType set_ContentType IsSetContentType _contentType EndpointType DocumentationPartType get_ExportType set_ExportType IsSetExp
ortType _exportType get_KeyType set_KeyType IsSetKeyType _keyType _type AWSSDK.Core get_InvariantCulture InvokeOptionsBase TestInvokeMetho
dResponse EndUpdateMethodResponse BeginUpdateMethodResponse EndDeleteMethodResponse BeginDeleteMethodResponse EndGetMethodResponse BeginGe
tMethodResponse EndPutMethodResponse BeginPutMethodResponse AmazonWebServiceResponse UpdateResourceResponse CreateResourceResponse DeleteR
esourceResponse TagResourceResponse UntagResourceResponse GetResourceResponse UpdateUsageResponse GetUsageResponse UpdateStageResponse Cre
ateStageResponse DeleteStageResponse GetStageResponse FlushStageCacheResponse FlushStageAuthorizersCacheResponse UpdateDomainNameResponse
CreateDomainNameResponse DeleteDomainNameResponse GetDomainNameResponse GetSdkTypeResponse UpdateMethodResponseResponse DeleteMethodRespon
seResponse GetMethodResponseResponse PutMethodResponseResponse UpdateIntegrationResponseResponse DeleteIntegrationResponseResponse GetInte
grationResponseResponse PutIntegrationResponseResponse UpdateGatewayResponseResponse DeleteGatewayResponseResponse GetGatewayResponseRespo
nse PutGatewayResponseResponse UpdateClientCertificateResponse GenerateClientCertificateResponse DeleteClientCertificateResponse GetClient
CertificateResponse GetModelTemplateResponse UpdateBasePathMappingResponse CreateBasePathMappingResponse DeleteBasePathMappingResponse Get
BasePathMappingResponse UpdateRestApiResponse CreateRestApiResponse DeleteRestApiResponse GetRestApiResponse ImportRestApiResponse PutRest
ApiResponse GetSdkResponse UpdateVpcLinkResponse CreateVpcLinkResponse DeleteVpcLinkResponse GetVpcLinkResponse UpdateModelResponse Create
ModelResponse DeleteModelResponse GetModelResponse UpdateUsagePlanResponse CreateUsagePlanResponse DeleteUsagePlanResponse GetUsagePlanRes
