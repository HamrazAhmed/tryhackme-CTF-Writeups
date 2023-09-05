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
ponse UpdateDocumentationVersionResponse CreateDocumentationVersionResponse DeleteDocumentationVersionResponse GetDocumentationVersionResp
onse EndUpdateIntegrationResponse BeginUpdateIntegrationResponse EndDeleteIntegrationResponse BeginDeleteIntegrationResponse EndGetIntegra
tionResponse BeginGetIntegrationResponse EndPutIntegrationResponse BeginPutIntegrationResponse TestInvokeAuthorizerResponse UpdateAuthoriz
erResponse CreateAuthorizerResponse DeleteAuthorizerResponse GetAuthorizerResponse ErrorResponse UpdateRequestValidatorResponse CreateRequ
estValidatorResponse DeleteRequestValidatorResponse GetRequestValidatorResponse GetResourcesResponse GetStagesResponse GetDomainNamesRespo
nse GetSdkTypesResponse GetGatewayResponsesResponse GetClientCertificatesResponse GetTagsResponse GetBasePathMappingsResponse GetRestApisR
esponse GetVpcLinksResponse GetModelsResponse GetUsagePlansResponse GetDocumentationVersionsResponse GetAuthorizersResponse GetRequestVali
datorsResponse GetDeploymentsResponse GetDocumentationPartsResponse ImportDocumentationPartsResponse GetApiKeysResponse ImportApiKeysRespo
nse GetUsagePlanKeysResponse get_DefaultResponse set_DefaultResponse IsSetDefaultResponse _defaultResponse UpdateDeploymentResponse Create
DeploymentResponse DeleteDeploymentResponse GetDeploymentResponse UpdateAccountResponse GetAccountResponse UpdateDocumentationPartResponse
 CreateDocumentationPartResponse DeleteDocumentationPartResponse GetDocumentationPartResponse GetExportResponse EndUpdateGatewayResponse B
eginUpdateGatewayResponse EndDeleteGatewayResponse BeginDeleteGatewayResponse EndGetGatewayResponse BeginGetGatewayResponse EndPutGatewayR
esponse BeginPutGatewayResponse UpdateApiKeyResponse CreateApiKeyResponse DeleteApiKeyResponse GetApiKeyResponse CreateUsagePlanKeyRespons
e DeleteUsagePlanKeyResponse GetUsagePlanKeyResponse Dispose get_CertificateUploadDate set_CertificateUploadDate IsSetCertificateUploadDat
e _certificateUploadDate get_LastUpdatedDate set_LastUpdatedDate IsSetLastUpdatedDate _lastUpdatedDate get_CreatedDate set_CreatedDate IsS
etCreatedDate _createdDate get_EndDate set_EndDate IsSetEndDate _endDate get_ExpirationDate set_ExpirationDate IsSetExpirationDate _expira
tionDate get_StartDate set_StartDate IsSetStartDate _startDate get_PemEncodedCertificate set_PemEncodedCertificate IsSetPemEncodedCertific
ate _pemEncodedCertificate EndUpdateClientCertificate BeginUpdateClientCertificate EndGenerateClientCertificate BeginGenerateClientCertifi
cate EndDeleteClientCertificate BeginDeleteClientCertificate EndGetClientCertificate BeginGetClientCertificate EndGetModelTemplate BeginGe
tModelTemplate state Write Overwrite SuppressMessageAttribute DebuggableAttribute ComVisibleAttribute AssemblyTitleAttribute AssemblyTrade
markAttribute AssemblyFileVersionAttribute AssemblyInformationalVersionAttribute AssemblyConfigurationAttribute AssemblyDescriptionAttribu
te CompilationRelaxationsAttribute AllowPartiallyTrustedCallersAttribute AssemblyProductAttribute AssemblyCopyrightAttribute CLSCompliantA
ttribute AssemblyCompanyAttribute RuntimeCompatibilityAttribute AWSPropertyAttribute get_Value set_Value FindValue get_IncludeValue set_In
cludeValue IsSetIncludeValue _includeValue GetHeaderValue get_HasValue IsSetValue get_DefaultValue set_DefaultValue IsSetDefaultValue _def
aultValue _value Move Remove get_MinimumCompressionSize set_MinimumCompressionSize IsSetMinimumCompressionSize _minimumCompressionSize get
_CacheClusterSize set_CacheClusterSize IsSetCacheClusterSize _cacheClusterSize Amazon.Runtime.IAmazonService.get_Config IClientConfig clie
ntConfig AmazonAPIGatewayConfig config Encoding get_ContentHandling set_ContentHandling IsSetContentHandling _contentHandling get_Operatio
nNameMapping EndUpdateBasePathMapping BeginUpdateBasePathMapping EndCreateBasePathMapping BeginCreateBasePathMapping EndDeleteBasePathMapp
ing BeginDeleteBasePathMapping EndGetBasePathMapping BeginGetBasePathMapping FromString ToString BuildUserAgentString set_UseQueryString g
et_PathWithQueryString set_PathWithQueryString IsSetPathWithQueryString _pathWithQueryString disposing MethodSetting get_Log set_Log IsSet
Log _log get_Path set_Path set_ResourcePath get_BasePath set_BasePath IsSetBasePath _basePath IsSetPath _path get_Length ReadAtDepth get_C
urrentDepth Amazon.Runtime.Internal.Auth EndUpdateRestApi BeginUpdateRestApi EndCreateRestApi BeginCreateRestApi EndDeleteRestApi BeginDel
eteRestApi EndGetRestApi BeginGetRestApi EndImportRestApi BeginImportRestApi EndPutRestApi BeginPutRestApi get_Uri set_Uri get_AuthorizerU
ri set_AuthorizerUri IsSetAuthorizerUri _authorizerUri IsSetUri _uri AsyncCallback callback EndGetSdk BeginGetSdk Seek EndUpdateVpcLink Be
ginUpdateVpcLink EndCreateVpcLink BeginCreateVpcLink EndDeleteVpcLink BeginDeleteVpcLink EndGetVpcLink BeginGetVpcLink Amazon.Runtime.Inte
rnal Amazon.Util.Internal Amazon.APIGateway.Internal Amazon.APIGateway.Model EndUpdateModel BeginUpdateModel EndCreateModel BeginCreateMod
el EndDeleteModel BeginDeleteModel EndGetModel BeginGetModel get_LoggingLevel set_LoggingLevel IsSetLoggingLevel _loggingLevel Amazon.Runt
ime.Internal.Util Amazon.Util Marshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.Method,Amazon.Runtime.Inter
nal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.Resource,Amazon.R
untime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.Stage
,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Mo
del.ApiStage,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.A
PIGateway.Model.DomainName,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarsh
aller<Amazon.APIGateway.Model.SdkType,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transfo
rm.IUnmarshaller<Amazon.APIGateway.Model.MethodResponse,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtim
e.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.IntegrationResponse,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.U
nmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.GatewayResponse,Amazon.Runtime.Internal.Transform.XmlUnm
arshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.ClientCertificate,Amazon.Runtime.Inte
rnal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.BasePathMapping,
Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Mod
el.MethodSetting,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amaz
on.APIGateway.Model.RestApi,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmars
haller<Amazon.APIGateway.Model.VpcLink,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transf
orm.IUnmarshaller<Amazon.APIGateway.Model.Model,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Intern
al.Transform.IUnmarshaller<Amazon.APIGateway.Model.UsagePlan,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.R
untime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.DocumentationVersion,Amazon.Runtime.Internal.Transform.XmlUnmarshallerCont
ext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.DocumentationPartLocation,Amazon.Runtime.Internal.
Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.Integration,Amazon.Ru
ntime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.Endpoi
ntConfiguration,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazo
n.APIGateway.Model.Authorizer,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnma
rshaller<Amazon.APIGateway.Model.RequestValidator,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Inte
rnal.Transform.IUnmarshaller<Amazon.APIGateway.Model.QuotaSettings,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Am
azon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.ThrottleSettings,Amazon.Runtime.Internal.Transform.XmlUnmarshallerCo
ntext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.AccessLogSettings,Amazon.Runtime.Internal.Transf
orm.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.CanarySettings,Amazon.Runti
me.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.Deploymen
t,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.M
odel.MethodSnapshot,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<A
mazon.APIGateway.Model.DocumentationPart,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Tran
sform.IUnmarshaller<Amazon.APIGateway.Model.ApiKey,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Int
ernal.Transform.IUnmarshaller<Amazon.APIGateway.Model.UsagePlanKey,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Am
azon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.SdkConfigurationProperty,Amazon.Runtime.Internal.Transform.XmlUnmars
hallerContext>.Unmarshall AWSSDK.APIGateway.dll FromBool get_RequireAuthorizationForCacheControl set_RequireAuthorizationForCacheControl I
sSetRequireAuthorizationForCacheControl _requireAuthorizationForCacheControl get_Stream get_ContentStream set_ContentStream CopyStream Mem
oryStream get_Item set_Item IsSetItem _item System get_From set_From get_CloneFrom set_CloneFrom IsSetCloneFrom _cloneFrom IsSetFrom _from
 Amazon.Runtime.Internal.Transform EndUpdateUsagePlan BeginUpdateUsagePlan EndCreateUsagePlan BeginCreateUsagePlan EndDeleteUsagePlan Begi
nDeleteUsagePlan EndGetUsagePlan BeginGetUsagePlan awsSessionToken JsonToken get_Flatten set_Flatten IsSetFlatten _flatten get_Certificate
Chain set_CertificateChain IsSetCertificateChain _certificateChain SeekOrigin region get_Version set_Version get_ServiceVersion get_Docume
ntationVersion set_DocumentationVersion EndUpdateDocumentationVersion BeginUpdateDocumentationVersion EndCreateDocumentationVersion BeginC
reateDocumentationVersion EndDeleteDocumentationVersion BeginDeleteDocumentationVersion EndGetDocumentationVersion BeginGetDocumentationVe
rsion IsSetDocumentationVersion _documentationVersion set_MarshallerVersion IsSetVersion get_ApiKeyVersion set_ApiKeyVersion IsSetApiKeyVe
rsion _apiKeyVersion _version get_IdentityValidationExpression set_IdentityValidationExpression IsSetIdentityValidationExpression _identit
yValidationExpression TestExpression get_Location set_Location IsSetLocation DocumentationPartLocation _location PatchOperation get_Method
Integration set_MethodIntegration IsSetMethodIntegration _methodIntegration EndUpdateIntegration BeginUpdateIntegration EndDeleteIntegrati
on BeginDeleteIntegration EndGetIntegration BeginGetIntegration EndPutIntegration BeginPutIntegration get_EndpointConfiguration set_Endpoi
ntConfiguration IsSetEndpointConfiguration _endpointConfiguration System.Globalization System.Runtime.Serialization get_Authorization set_
Authorization IsSetAuthorization _authorization System.Reflection get_ParameterCollection get_Position set_Position IsSetPosition _positio
n get_ContentDisposition set_ContentDisposition IsSetContentDisposition _contentDisposition LimitExceededException NotImplementedException
 UnauthorizedException NotFoundException AmazonServiceException ServiceUnavailableException UnmarshallException innerException TooManyRequ
estsException ConflictException BadRequestException AmazonAPIGatewayException get_Description set_Description get_StageDescription set_Sta
geDescription IsSetStageDescription _stageDescription IsSetDescription _description ThirdParty.Json.LitJson Amazon get_ResourceArn set_Res
ourceArn IsSetResourceArn _resourceArn get_CloudwatchRoleArn set_CloudwatchRoleArn IsSetCloudwatchRoleArn _cloudwatchRoleArn get_Certifica
teArn set_CertificateArn get_RegionalCertificateArn set_RegionalCertificateArn IsSetRegionalCertificateArn _regionalCertificateArn IsSetCe
rtificateArn _certificateArn get_WebAclArn set_WebAclArn IsSetWebAclArn _webAclArn get_DestinationArn set_DestinationArn IsSetDestinationA
rn _destinationArn get_SelectionPattern set_SelectionPattern IsSetSelectionPattern _selectionPattern CultureInfo SerializationInfo info ge
t_Op set_Op IsSetOp _op IFormatProvider IPipelineHandler AmazonAPIGatewayPostMarshallHandler ApiStageMarshaller DocumentationPartLocationM
arshaller PatchOperationMarshaller EndpointConfigurationMarshaller QuotaSettingsMarshaller ThrottleSettingsMarshaller DeploymentCanarySett
ingsMarshaller set_RequestMarshaller TestInvokeMethodRequestMarshaller UpdateMethodRequestMarshaller DeleteMethodRequestMarshaller GetMeth
odRequestMarshaller PutMethodRequestMarshaller UpdateResourceRequestMarshaller CreateResourceRequestMarshaller DeleteResourceRequestMarsha
ller TagResourceRequestMarshaller UntagResourceRequestMarshaller GetResourceRequestMarshaller UpdateUsageRequestMarshaller GetUsageRequest
Marshaller UpdateStageRequestMarshaller CreateStageRequestMarshaller DeleteStageRequestMarshaller GetStageRequestMarshaller FlushStageCach
eRequestMarshaller FlushStageAuthorizersCacheRequestMarshaller UpdateDomainNameRequestMarshaller CreateDomainNameRequestMarshaller DeleteD
omainNameRequestMarshaller GetDomainNameRequestMarshaller GetSdkTypeRequestMarshaller UpdateMethodResponseRequestMarshaller DeleteMethodRe
sponseRequestMarshaller GetMethodResponseRequestMarshaller PutMethodResponseRequestMarshaller UpdateIntegrationResponseRequestMarshaller D
eleteIntegrationResponseRequestMarshaller GetIntegrationResponseRequestMarshaller PutIntegrationResponseRequestMarshaller UpdateGatewayRes
ponseRequestMarshaller DeleteGatewayResponseRequestMarshaller GetGatewayResponseRequestMarshaller PutGatewayResponseRequestMarshaller Upda
teClientCertificateRequestMarshaller GenerateClientCertificateRequestMarshaller DeleteClientCertificateRequestMarshaller GetClientCertific
ateRequestMarshaller GetModelTemplateRequestMarshaller UpdateBasePathMappingRequestMarshaller CreateBasePathMappingRequestMarshaller Delet
eBasePathMappingRequestMarshaller GetBasePathMappingRequestMarshaller UpdateRestApiRequestMarshaller CreateRestApiRequestMarshaller Delete
RestApiRequestMarshaller GetRestApiRequestMarshaller ImportRestApiRequestMarshaller PutRestApiRequestMarshaller GetSdkRequestMarshaller Up
dateVpcLinkRequestMarshaller CreateVpcLinkRequestMarshaller DeleteVpcLinkRequestMarshaller GetVpcLinkRequestMarshaller UpdateModelRequestM
arshaller CreateModelRequestMarshaller DeleteModelRequestMarshaller GetModelRequestMarshaller UpdateUsagePlanRequestMarshaller CreateUsage
PlanRequestMarshaller DeleteUsagePlanRequestMarshaller GetUsagePlanRequestMarshaller UpdateDocumentationVersionRequestMarshaller CreateDoc
umentationVersionRequestMarshaller DeleteDocumentationVersionRequestMarshaller GetDocumentationVersionRequestMarshaller UpdateIntegrationR
equestMarshaller DeleteIntegrationRequestMarshaller GetIntegrationRequestMarshaller PutIntegrationRequestMarshaller TestInvokeAuthorizerRe
questMarshaller UpdateAuthorizerRequestMarshaller CreateAuthorizerRequestMarshaller DeleteAuthorizerRequestMarshaller GetAuthorizerRequest
Marshaller UpdateRequestValidatorRequestMarshaller CreateRequestValidatorRequestMarshaller DeleteRequestValidatorRequestMarshaller GetRequ
estValidatorRequestMarshaller GetResourcesRequestMarshaller GetStagesRequestMarshaller GetDomainNamesRequestMarshaller GetSdkTypesRequestM
arshaller GetGatewayResponsesRequestMarshaller GetClientCertificatesRequestMarshaller GetTagsRequestMarshaller GetBasePathMappingsRequestM
arshaller GetRestApisRequestMarshaller GetVpcLinksRequestMarshaller GetModelsRequestMarshaller GetUsagePlansRequestMarshaller GetDocumenta
tionVersionsRequestMarshaller GetAuthorizersRequestMarshaller GetRequestValidatorsRequestMarshaller GetDeploymentsRequestMarshaller GetDoc
umentationPartsRequestMarshaller ImportDocumentationPartsRequestMarshaller GetApiKeysRequestMarshaller ImportApiKeysRequestMarshaller GetU
sagePlanKeysRequestMarshaller UpdateDeploymentRequestMarshaller CreateDeploymentRequestMarshaller DeleteDeploymentRequestMarshaller GetDep
loymentRequestMarshaller UpdateAccountRequestMarshaller GetAccountRequestMarshaller UpdateDocumentationPartRequestMarshaller CreateDocumen
tationPartRequestMarshaller DeleteDocumentationPartRequestMarshaller GetDocumentationPartRequestMarshaller GetExportRequestMarshaller Upda
teApiKeyRequestMarshaller CreateApiKeyRequestMarshaller DeleteApiKeyRequestMarshaller GetApiKeyRequestMarshaller CreateUsagePlanKeyRequest
Marshaller DeleteUsagePlanKeyRequestMarshaller GetUsagePlanKeyRequestMarshaller StageKeyMarshaller MethodUnmarshaller ResourceUnmarshaller
 ApiStageUnmarshaller DoubleUnmarshaller DomainNameUnmarshaller DateTimeUnmarshaller SdkTypeUnmarshaller set_ResponseUnmarshaller TestInvo
keMethodResponseUnmarshaller UpdateMethodResponseUnmarshaller DeleteMethodResponseUnmarshaller GetMethodResponseUnmarshaller PutMethodResp
onseUnmarshaller UpdateResourceResponseUnmarshaller CreateResourceResponseUnmarshaller DeleteResourceResponseUnmarshaller TagResourceRespo
nseUnmarshaller UntagResourceResponseUnmarshaller GetResourceResponseUnmarshaller UpdateUsageResponseUnmarshaller GetUsageResponseUnmarsha
ller UpdateStageResponseUnmarshaller CreateStageResponseUnmarshaller DeleteStageResponseUnmarshaller GetStageResponseUnmarshaller FlushSta
geCacheResponseUnmarshaller FlushStageAuthorizersCacheResponseUnmarshaller UpdateDomainNameResponseUnmarshaller CreateDomainNameResponseUn
marshaller DeleteDomainNameResponseUnmarshaller GetDomainNameResponseUnmarshaller GetSdkTypeResponseUnmarshaller UpdateMethodResponseRespo
nseUnmarshaller DeleteMethodResponseResponseUnmarshaller GetMethodResponseResponseUnmarshaller PutMethodResponseResponseUnmarshaller Updat
eIntegrationResponseResponseUnmarshaller DeleteIntegrationResponseResponseUnmarshaller GetIntegrationResponseResponseUnmarshaller PutInteg
rationResponseResponseUnmarshaller UpdateGatewayResponseResponseUnmarshaller DeleteGatewayResponseResponseUnmarshaller GetGatewayResponseR
esponseUnmarshaller PutGatewayResponseResponseUnmarshaller UpdateClientCertificateResponseUnmarshaller GenerateClientCertificateResponseUn
marshaller DeleteClientCertificateResponseUnmarshaller GetClientCertificateResponseUnmarshaller GetModelTemplateResponseUnmarshaller Updat
eBasePathMappingResponseUnmarshaller CreateBasePathMappingResponseUnmarshaller DeleteBasePathMappingResponseUnmarshaller GetBasePathMappin
gResponseUnmarshaller UpdateRestApiResponseUnmarshaller CreateRestApiResponseUnmarshaller DeleteRestApiResponseUnmarshaller GetRestApiResp
onseUnmarshaller ImportRestApiResponseUnmarshaller PutRestApiResponseUnmarshaller GetSdkResponseUnmarshaller UpdateVpcLinkResponseUnmarsha
ller CreateVpcLinkResponseUnmarshaller DeleteVpcLinkResponseUnmarshaller GetVpcLinkResponseUnmarshaller UpdateModelResponseUnmarshaller Cr
eateModelResponseUnmarshaller DeleteModelResponseUnmarshaller GetModelResponseUnmarshaller UpdateUsagePlanResponseUnmarshaller CreateUsage
PlanResponseUnmarshaller DeleteUsagePlanResponseUnmarshaller GetUsagePlanResponseUnmarshaller UpdateDocumentationVersionResponseUnmarshall
er CreateDocumentationVersionResponseUnmarshaller DeleteDocumentationVersionResponseUnmarshaller GetDocumentationVersionResponseUnmarshall
er UpdateIntegrationResponseUnmarshaller DeleteIntegrationResponseUnmarshaller GetIntegrationResponseUnmarshaller PutIntegrationResponseUn
marshaller JsonResponseUnmarshaller TestInvokeAuthorizerResponseUnmarshaller UpdateAuthorizerResponseUnmarshaller CreateAuthorizerResponse
Unmarshaller DeleteAuthorizerResponseUnmarshaller GetAuthorizerResponseUnmarshaller JsonErrorResponseUnmarshaller UpdateRequestValidatorRe
sponseUnmarshaller CreateRequestValidatorResponseUnmarshaller DeleteRequestValidatorResponseUnmarshaller GetRequestValidatorResponseUnmars
haller GetResourcesResponseUnmarshaller GetStagesResponseUnmarshaller GetDomainNamesResponseUnmarshaller GetSdkTypesResponseUnmarshaller G
etGatewayResponsesResponseUnmarshaller GetClientCertificatesResponseUnmarshaller GetTagsResponseUnmarshaller GetBasePathMappingsResponseUn
marshaller GetRestApisResponseUnmarshaller GetVpcLinksResponseUnmarshaller GetModelsResponseUnmarshaller GetUsagePlansResponseUnmarshaller
 GetDocumentationVersionsResponseUnmarshaller GetAuthorizersResponseUnmarshaller GetRequestValidatorsResponseUnmarshaller GetDeploymentsRe
sponseUnmarshaller GetDocumentationPartsResponseUnmarshaller ImportDocumentationPartsResponseUnmarshaller GetApiKeysResponseUnmarshaller I
mportApiKeysResponseUnmarshaller GetUsagePlanKeysResponseUnmarshaller UpdateDeploymentResponseUnmarshaller CreateDeploymentResponseUnmarsh
aller DeleteDeploymentResponseUnmarshaller GetDeploymentResponseUnmarshaller UpdateAccountResponseUnmarshaller GetAccountResponseUnmarshal
ler UpdateDocumentationPartResponseUnmarshaller CreateDocumentationPartResponseUnmarshaller DeleteDocumentationPartResponseUnmarshaller Ge
tDocumentationPartResponseUnmarshaller GetExportResponseUnmarshaller GatewayResponseUnmarshaller UpdateApiKeyResponseUnmarshaller CreateAp
iKeyResponseUnmarshaller DeleteApiKeyResponseUnmarshaller GetApiKeyResponseUnmarshaller CreateUsagePlanKeyResponseUnmarshaller DeleteUsage
PlanKeyResponseUnmarshaller GetUsagePlanKeyResponseUnmarshaller ClientCertificateUnmarshaller BasePathMappingUnmarshaller StringUnmarshall
er MethodSettingUnmarshaller LongUnmarshaller RestApiUnmarshaller VpcLinkUnmarshaller ModelUnmarshaller BoolUnmarshaller UsagePlanUnmarsha
ller DocumentationVersionUnmarshaller DocumentationPartLocationUnmarshaller IntegrationUnmarshaller EndpointConfigurationUnmarshaller Auth
orizerUnmarshaller RequestValidatorUnmarshaller QuotaSettingsUnmarshaller ThrottleSettingsUnmarshaller AccessLogSettingsUnmarshaller Canar
ySettingsUnmarshaller IntUnmarshaller DeploymentUnmarshaller MethodSnapshotUnmarshaller DocumentationPartUnmarshaller ApiKeyUnmarshaller U
sagePlanKeyUnmarshaller SdkConfigurationPropertyUnmarshaller AWS4Signer AbstractAWSSigner CreateSigner AddHandlerAfter get_Writer StringWr
iter JsonWriter TextWriter EndTestInvokeAuthorizer BeginTestInvokeAuthorizer EndUpdateAuthorizer BeginUpdateAuthorizer EndCreateAuthorizer
 BeginCreateAuthorizer EndDeleteAuthorizer BeginDeleteAuthorizer EndGetAuthorizer BeginGetAuthorizer get_PassthroughBehavior set_Passthrou
ghBehavior IsSetPassthroughBehavior _passthroughBehavior EndUpdateRequestValidator BeginUpdateRequestValidator EndCreateRequestValidator B
eginCreateRequestValidator EndDeleteRequestValidator BeginDeleteRequestValidator EndGetRequestValidator BeginGetRequestValidator GetEnumer
ator .ctor .cctor get_ProviderARNs set_ProviderARNs IsSetProviderARNs _providerarNs System.Diagnostics get_Ids set_Ids IsSetIds _ids get_C
acheTtlInSeconds set_CacheTtlInSeconds IsSetCacheTtlInSeconds _cacheTtlInSeconds get_AuthorizerResultTtlInSeconds set_AuthorizerResultTtlI
nSeconds IsSetAuthorizerResultTtlInSeconds _authorizerResultTtlInSeconds get_ResourceMethods set_ResourceMethods IsSetResourceMethods _res
ourceMethods System.Runtime.InteropServices System.Runtime.CompilerServices EndGetResources BeginGetResources get_StageVariableOverrides s
et_StageVariableOverrides IsSetStageVariableOverrides _stageVariableOverrides DebuggingModes get_ApiStages set_ApiStages IsSetApiStages _a
piStages EndGetStages BeginGetStages get_Properties set_Properties get_ConfigurationProperties set_ConfigurationProperties IsSetConfigurat
ionProperties _configurationProperties IsSetProperties _properties get_Variables set_Variables get_StageVariables set_StageVariables IsSet
StageVariables _stageVariables IsSetVariables _variables EndGetDomainNames BeginGetDomainNames get_AuthorizationScopes set_AuthorizationSc
opes IsSetAuthorizationScopes _authorizationScopes get_Types set_Types get_BinaryMediaTypes set_BinaryMediaTypes IsSetBinaryMediaTypes _bi
naryMediaTypes EndGetSdkTypes BeginGetSdkTypes IsSetTypes _types get_Features set_Features IsSetFeatures _features get_MethodResponses set
_MethodResponses IsSetMethodResponses _methodResponses get_IntegrationResponses set_IntegrationResponses IsSetIntegrationResponses _integr
ationResponses EndGetGatewayResponses BeginGetGatewayResponses EndGetClientCertificates BeginGetClientCertificates get_ResponseTemplates s
et_ResponseTemplates IsSetResponseTemplates _responseTemplates get_RequestTemplates set_RequestTemplates IsSetRequestTemplates _requestTem
plates GetBytes get_IncludeValues set_IncludeValues IsSetIncludeValues _includeValues get_Tags set_Tags EndGetTags BeginGetTags IsSetTags
_tags get_Warnings set_Warnings get_FailOnWarnings set_FailOnWarnings IsSetFailOnWarnings _failOnWarnings IsSetWarnings _warnings EndGetBa
sePathMappings BeginGetBasePathMappings QuotaSettings get_MethodSettings set_MethodSettings IsSetMethodSettings _methodSettings get_Thrott
leSettings set_ThrottleSettings IsSetThrottleSettings _throttleSettings get_AccessLogSettings set_AccessLogSettings IsSetAccessLogSettings
 _accessLogSettings get_CanarySettings set_CanarySettings IsSetCanarySettings DeploymentCanarySettings _canarySettings get_TimeoutInMillis
 set_TimeoutInMillis IsSetTimeoutInMillis _timeoutInMillis EndGetRestApis BeginGetRestApis System.Diagnostics.CodeAnalysis EndGetVpcLinks
BeginGetVpcLinks AWSCredentials get_Credentials set_Credentials get_AuthorizerCredentials set_AuthorizerCredentials IsSetAuthorizerCredent
ials _authorizerCredentials GetCredentials IsSetCredentials _credentials Equals get_ResponseModels set_ResponseModels IsSetResponseModels
_responseModels EndGetModels BeginGetModels get_RequestModels set_RequestModels IsSetRequestModels _requestModels AWSSDKUtils InternalSDKU
tils StringUtils get_Items set_Items IsSetItems _items get_Claims set_Claims IsSetClaims _claims EndGetUsagePlans BeginGetUsagePlans EndGe
tDocumentationVersions BeginGetDocumentationVersions Amazon.APIGateway.Model.Internal.MarshallTransformations get_PatchOperations set_Patc
hOperations IsSetPatchOperations _patchOperations InvokeOptions get_TargetArns set_TargetArns IsSetTargetArns _targetArns get_Headers set_
Headers get_MultiValueHeaders set_MultiValueHeaders IsSetMultiValueHeaders _multiValueHeaders IsSetHeaders _headers get_Parameters set_Par
ameters get_ResponseParameters set_ResponseParameters IsSetResponseParameters _responseParameters IsSetParameters get_RequestParameters se
t_RequestParameters get_ValidateRequestParameters set_ValidateRequestParameters IsSetValidateRequestParameters _validateRequestParameters
IsSetRequestParameters _requestParameters get_CacheKeyParameters set_CacheKeyParameters IsSetCacheKeyParameters _cacheKeyParameters _param
eters EndGetAuthorizers BeginGetAuthorizers EndGetRequestValidators BeginGetRequestValidators ConstantClass EndGetDeployments BeginGetDepl
oyments get_Accepts set_Accepts IsSetAccepts _accepts EndGetDocumentationParts BeginGetDocumentationParts EndImportDocumentationParts Begi
nImportDocumentationParts get_Status set_Status get_DomainNameStatus set_DomainNameStatus IsSetDomainNameStatus _domainNameStatus VpcLinkS
tatus get_LocationStatus set_LocationStatus IsSetLocationStatus _locationStatus get_CacheClusterStatus set_CacheClusterStatus IsSetCacheCl
usterStatus _cacheClusterStatus IsSetStatus get_ClientStatus set_ClientStatus IsSetClientStatus _clientStatus _status get_StageKeys set_St
ageKeys IsSetStageKeys _stageKeys get_TagKeys set_TagKeys IsSetTagKeys _tagKeys EndGetApiKeys BeginGetApiKeys EndImportApiKeys BeginImport
ApiKeys EndGetUsagePlanKeys BeginGetUsagePlanKeys get_Format set_Format ApiKeysFormat IsSetFormat _format requestObject System.Net get_Off
set set_Offset IsSetOffset _offset op_Implicit get_Limit set_Limit get_RateLimit set_RateLimit get_ThrottlingRateLimit set_ThrottlingRateL
imit IsSetThrottlingRateLimit _throttlingRateLimit IsSetRateLimit _rateLimit IsSetLimit get_BurstLimit set_BurstLimit get_ThrottlingBurstL
imit set_ThrottlingBurstLimit IsSetThrottlingBurstLimit _throttlingBurstLimit IsSetBurstLimit _burstLimit _limit GetValueOrDefault IAsyncR
esult asyncResult FromInt get_UserAgent _userAgent AmazonServiceClient AmazonAPIGatewayClient EndUpdateDeployment BeginUpdateDeployment En
dCreateDeployment BeginCreateDeployment EndDeleteDeployment BeginDeleteDeployment EndGetDeployment BeginGetDeployment get_Current IsHeader
Present set_Content set_RegionEndpoint get_Count EndUpdateAccount BeginUpdateAccount EndGetAccount BeginGetAccount MethodSnapshot get_Path
Part set_PathPart IsSetPathPart _pathPart EndUpdateDocumentationPart BeginUpdateDocumentationPart EndCreateDocumentationPart BeginCreateDo
cumentationPart EndDeleteDocumentationPart BeginDeleteDocumentationPart EndGetDocumentationPart BeginGetDocumentationPart WriteObjectStart
 WriteArrayStart EndGetExport BeginGetExport Test IRequest get_Request publicRequest TestInvokeMethodRequest UpdateMethodRequest DeleteMet
hodRequest GetMethodRequest PutMethodRequest AmazonWebServiceRequest UpdateResourceRequest CreateResourceRequest DeleteResourceRequest Tag
ResourceRequest UntagResourceRequest GetResourceRequest UpdateUsageRequest GetUsageRequest UpdateStageRequest CreateStageRequest DeleteSta
geRequest GetStageRequest FlushStageCacheRequest FlushStageAuthorizersCacheRequest UpdateDomainNameRequest CreateDomainNameRequest DeleteD
omainNameRequest GetDomainNameRequest GetSdkTypeRequest UpdateMethodResponseRequest DeleteMethodResponseRequest GetMethodResponseRequest P
utMethodResponseRequest UpdateIntegrationResponseRequest DeleteIntegrationResponseRequest GetIntegrationResponseRequest PutIntegrationResp
onseRequest UpdateGatewayResponseRequest DeleteGatewayResponseRequest GetGatewayResponseRequest PutGatewayResponseRequest UpdateClientCert
ificateRequest GenerateClientCertificateRequest DeleteClientCertificateRequest GetClientCertificateRequest GetModelTemplateRequest UpdateB
asePathMappingRequest CreateBasePathMappingRequest DeleteBasePathMappingRequest GetBasePathMappingRequest UpdateRestApiRequest CreateRestA
piRequest DeleteRestApiRequest GetRestApiRequest ImportRestApiRequest PutRestApiRequest GetSdkRequest UpdateVpcLinkRequest CreateVpcLinkRe
quest DeleteVpcLinkRequest GetVpcLinkRequest UpdateModelRequest CreateModelRequest DeleteModelRequest GetModelRequest UpdateUsagePlanReque
st CreateUsagePlanRequest DeleteUsagePlanRequest GetUsagePlanRequest UpdateDocumentationVersionRequest CreateDocumentationVersionRequest D
eleteDocumentationVersionRequest GetDocumentationVersionRequest UpdateIntegrationRequest DeleteIntegrationRequest GetIntegrationRequest Pu
tIntegrationRequest TestInvokeAuthorizerRequest UpdateAuthorizerRequest CreateAuthorizerRequest DeleteAuthorizerRequest GetAuthorizerReque
st UpdateRequestValidatorRequest CreateRequestValidatorRequest DeleteRequestValidatorRequest GetRequestValidatorRequest GetResourcesReques
t GetStagesRequest GetDomainNamesRequest GetSdkTypesRequest GetGatewayResponsesRequest GetClientCertificatesRequest GetTagsRequest GetBase
PathMappingsRequest GetRestApisRequest GetVpcLinksRequest GetModelsRequest GetUsagePlansRequest GetDocumentationVersionsRequest GetAuthori
zersRequest GetRequestValidatorsRequest GetDeploymentsRequest GetDocumentationPartsRequest ImportDocumentationPartsRequest GetApiKeysReque
st ImportApiKeysRequest GetUsagePlanKeysRequest DefaultRequest UpdateDeploymentRequest CreateDeploymentRequest DeleteDeploymentRequest Get
DeploymentRequest UpdateAccountRequest GetAccountRequest UpdateDocumentationPartRequest CreateDocumentationPartRequest DeleteDocumentation
PartRequest GetDocumentationPartRequest GetExportRequest AmazonAPIGatewayRequest UpdateApiKeyRequest CreateApiKeyRequest DeleteApiKeyReque
st GetApiKeyRequest CreateUsagePlanKeyRequest DeleteUsagePlanKeyRequest GetUsagePlanKeyRequest request input MoveNext System.Text CreateFr
omAsyncContext StreamingContext get_AdditionalContext set_AdditionalContext IsSetAdditionalContext _additionalContext IExecutionContext IA
syncExecutionContext executionContext JsonMarshallerContext XmlUnmarshallerContext JsonUnmarshallerContext IRequestContext get_RequestCont
ext context Csv AWSSDK.APIGateway Amazon.APIGateway IAmazonAPIGateway get_Policy set_Policy IsSetPolicy get_SecurityPolicy set_SecurityPol
icy IsSetSecurityPolicy _securityPolicy _policy get_Latency set_Latency IsSetLatency _latency get_Body set_Body get_CertificateBody set_Ce
rtificateBody IsSetCertificateBody _certificateBody IsSetBody get_ValidateRequestBody set_ValidateRequestBody IsSetValidateRequestBody _va
lidateRequestBody _body get_Key StageKey get_CertificatePrivateKey set_CertificatePrivateKey IsSetCertificatePrivateKey _certificatePrivat
eKey get_ApiKey set_ApiKey EndUpdateApiKey BeginUpdateApiKey EndCreateApiKey BeginCreateApiKey EndDeleteApiKey BeginDeleteApiKey EndGetApi
Key BeginGetApiKey IsSetApiKey _apiKey EndCreateUsagePlanKey BeginCreateUsagePlanKey EndDeleteUsagePlanKey BeginDeleteUsagePlanKey EndGetU
sagePlanKey BeginGetUsagePlanKey awsSecretAccessKey ContentHandlingStrategy get_UnauthorizedCacheControlHeaderStrategy set_UnauthorizedCac
heControlHeaderStrategy IsSetUnauthorizedCacheControlHeaderStrategy _unauthorizedCacheControlHeaderStrategy Copy get_ApiSummary set_ApiSum
mary IsSetApiSummary _apiSummary get_NameQuery set_NameQuery IsSetNameQuery _nameQuery FallbackCredentialsFactory op_Inequality System.Sec
urity SdkConfigurationProperty     a p i g a t e w a y  2 0 1 5 - 0 7 - 0 9 3 . 3 . 1 0 2 . 3 1  c s v  A U T H O R I Z E R
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.xml:2566:            The type of a usage plan key. Currently, the
valid key type is <code>API_KEY</code>.
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.xml:3053:            AUTHORIZER_CONFIGURATION_ERROR</li><li>BAD_REQUES
T_PARAMETERS</li><li>BAD_REQUEST_BODY</li><li>DEFAULT_4XX</li><li>DEFAULT_5XX</li><li>EXPIRED_TOKEN</li><li>INVALID_SIGNATURE</li><li>INTE
GRATION_FAILURE</li><li>INTEGRATION_TIMEOUT</li><li>INVALID_API_KEY</li><li>MISSING_AUTHENTICATION_TOKEN</li><li>
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.xml:3988:            AUTHORIZER_CONFIGURATION_ERROR</li><li>BAD_REQUES
T_PARAMETERS</li><li>BAD_REQUEST_BODY</li><li>DEFAULT_4XX</li><li>DEFAULT_5XX</li><li>EXPIRED_TOKEN</li><li>INVALID_SIGNATURE</li><li>INTE
GRATION_FAILURE</li><li>INTEGRATION_TIMEOUT</li><li>INVALID_API_KEY</li><li>MISSING_AUTHENTICATION_TOKEN</li><li>
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.xml:5547:            AUTHORIZER_CONFIGURATION_ERROR</li><li>BAD_REQUES
T_PARAMETERS</li><li>BAD_REQUEST_BODY</li><li>DEFAULT_4XX</li><li>DEFAULT_5XX</li><li>EXPIRED_TOKEN</li><li>INVALID_SIGNATURE</li><li>INTE
GRATION_FAILURE</li><li>INTEGRATION_TIMEOUT</li><li>INVALID_API_KEY</li><li>MISSING_AUTHENTICATION_TOKEN</li><li>
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.xml:5644:            AUTHORIZER_CONFIGURATION_ERROR</li><li>BAD_REQUES
T_PARAMETERS</li><li>BAD_REQUEST_BODY</li><li>DEFAULT_4XX</li><li>DEFAULT_5XX</li><li>EXPIRED_TOKEN</li><li>INVALID_SIGNATURE</li><li>INTE
GRATION_FAILURE</li><li>INTEGRATION_TIMEOUT</li><li>INVALID_API_KEY</li><li>MISSING_AUTHENTICATION_TOKEN</li><li>
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.xml:5733:            }, { "href":
"/restapis/o81lxisefl/gatewayresponses/ACCESS_DENIED" }, { "href": "/restapis/o81lxisefl/gatewayresponses/INVALID_API_KEY"
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.xml:5799:            "403" }, { "_links": { "self": { "href":
"/restapis/o81lxisefl/gatewayresponses/INVALID_API_KEY"
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.xml:5801:            "templated": true }, "gatewayresponse:update": {
"href": "/restapis/o81lxisefl/gatewayresponses/INVALID_API_KEY"
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.xml:5803:            "{\"message\":$context.error.messageString}" },
"responseType": "INVALID_API_KEY",
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.xml:7793:            The type of a usage plan key. Currently, the
valid key type is <code>API_KEY</code>.
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.xml:8091:            : { "{api_key}" : [ [0, 100], [10, 90], [100,
10]]}</code>, where <code>{api_key}</code>
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.xml:16524:            AUTHORIZER_CONFIGURATION_ERROR</li><li>BAD_REQUE
ST_PARAMETERS</li><li>BAD_REQUEST_BODY</li><li>DEFAULT_4XX</li><li>DEFAULT_5XX</li><li>EXPIRED_TOKEN</li><li>INVALID_SIGNATURE</li><li>INT
EGRATION_FAILURE</li><li>INTEGRATION_TIMEOUT</li><li>INVALID_API_KEY</li><li>MISSING_AUTHENTICATION_TOKEN</li><li>
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.xml:16626:            AUTHORIZER_CONFIGURATION_ERROR</li><li>BAD_REQUE
ST_PARAMETERS</li><li>BAD_REQUEST_BODY</li><li>DEFAULT_4XX</li><li>DEFAULT_5XX</li><li>EXPIRED_TOKEN</li><li>INVALID_SIGNATURE</li><li>INT
EGRATION_FAILURE</li><li>INTEGRATION_TIMEOUT</li><li>INVALID_API_KEY</li><li>MISSING_AUTHENTICATION_TOKEN</li><li>
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.xml:19969:            AUTHORIZER_CONFIGURATION_ERROR</li><li>BAD_REQUE
ST_PARAMETERS</li><li>BAD_REQUEST_BODY</li><li>DEFAULT_4XX</li><li>DEFAULT_5XX</li><li>EXPIRED_TOKEN</li><li>INVALID_SIGNATURE</li><li>INT
EGRATION_FAILURE</li><li>INTEGRATION_TIMEOUT</li><li>INVALID_API_KEY</li><li>MISSING_AUTHENTICATION_TOKEN</li><li>
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.xml:20066:            AUTHORIZER_CONFIGURATION_ERROR</li><li>BAD_REQUE
ST_PARAMETERS</li><li>BAD_REQUEST_BODY</li><li>DEFAULT_4XX</li><li>DEFAULT_5XX</li><li>EXPIRED_TOKEN</li><li>INVALID_SIGNATURE</li><li>INT
EGRATION_FAILURE</li><li>INTEGRATION_TIMEOUT</li><li>INVALID_API_KEY</li><li>MISSING_AUTHENTICATION_TOKEN</li><li>
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.xml:21664:            : { "{api_key}" : [ [0, 100], [10, 90], [100,
10]]}</code>, where <code>{api_key}</code>
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.xml:21909:            The type of a usage plan key. Currently, the
valid key type is <code>API_KEY</code>.
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.xml:22563:        <member
name="F:Amazon.APIGateway.GatewayResponseType.INVALID_API_KEY">
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.APIGateway.xml:22565:            Constant INVALID_API_KEY for GatewayResponseType
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.AppSync.dll:4241:               ��$    e �e �e �e �e �e �e �e �e �e �
{  { 2 2{ 7 7{ = ={ C C{ I I{ O O{ U U{ [ [{ a a{ g g{ m m{ s s{ y y{  { � �{ � �{
� �{ � �{ � �{ � �{ � �{ � �{ � �{ � �{ � �{ � �{ � �{ � �{ � �{ � �{ � �{ � �{ � �{ �
 �{ � �   Nullable`1 List`1 IMarshaller`2 IRequestMarshaller`2 IUnmarshaller`2 ListUnmarshaller`2 KeyValuePair`2 IDictionary`2 Dictio
naryUnmarshaller`4 get_UTF8 <Module> AWS_LAMBDA AMAZON_DYNAMODB FAILED NOT_APPLICABLE PIPELINE NONE RELATIONAL_DATABASE ACTIVE PROCESSING
DELETING AMAZON_ELASTICSEARCH SDL ALL get_AuthTTL set_AuthTTL IsSetAuthTTL get_IatTTL set_IatTTL IsSetIatTTL AWS_IAM JSON System.IO HTTP E
RROR AMAZON_COGNITO_USER_POOLS SUCCESS OPENID_CONNECT UNIT RDS_HTTP_ENDPOINT ALLOW API_KEY DENY get_Schema set_Schema EndGetIntrospectionS
chema BeginGetIntrospectionSchema IsSetSchema _schema AmazonAppSyncMetadata IServiceMetadata get_ServiceMetadata serviceMetadata mscorlib
System.Collections.Generic AWSSDK.AppSync Amazon.AppSync IAmazonAppSync get_Id set_Id get_ServiceId get_ApiId set_ApiId IsSetApiId _apiId
get_UserPoolId set_UserPoolId IsSetUserPoolId _userPoolId get_FunctionId set_FunctionId IsSetFunctionId _functionId IsSetId get_ClientId s
et_ClientId IsSetClientId _clientId get_RequestId requestId awsAccessKeyId Read Add _id WriteObjectEnd WriteArrayEnd get_Kind set_Kind Res
olverKind IsSetKind _kind set_HttpMethod IAmazonService get_Instance GetInstance _instance get_DataSource set_DataSource EndUpdateDataSour
ce BeginUpdateDataSource EndCreateDataSource BeginCreateDataSource EndDeleteDataSource BeginDeleteDataSource EndGetDataSource BeginGetData
Source IsSetDataSource _dataSource EndTagResource BeginTagResource EndUntagResource BeginUntagResource AddPathResource EndListTagsForResou
rce BeginListTagsForResource get_Code errorCode HttpStatusCode statusCode get_Message message EndInvoke BeginInvoke IDisposable get_Name s
et_Name get_FieldName set_FieldName IsSetFieldName _fieldName get_SigningServiceName set_SigningServiceName IsSetSigningServiceName _signi
ngServiceName set_AuthenticationServiceName get_RegionEndpointServiceName get_DataSourceName set_DataSourceName IsSetDataSourceName _dataS
ourceName get_TableName set_TableName IsSetTableName _tableName get_TypeName set_TypeName IsSetTypeName _typeName get_DatabaseName set_Dat
abaseName IsSetDatabaseName _databaseName IsSetName WritePropertyName _name Amazon.Runtime get_Type set_Type DataSourceType get_Relational
DatabaseSourceType set_RelationalDatabaseSourceType IsSetRelationalDatabaseSourceType _relationalDatabaseSourceType EndUpdateType BeginUpd
ateType EndCreateType BeginCreateType EndDeleteType BeginDeleteType get_CurrentTokenType get_AuthenticationType set_AuthenticationType IsS
etAuthenticationType _authenticationType get_AuthorizationType set_AuthorizationType IsSetAuthorizationType _authorizationType ErrorType e
rrorType EndGetType BeginGetType IsSetType OutputType _type AWSSDK.Core get_InvariantCulture InvokeOptionsBase GetIntrospectionSchemaRespo
nse AmazonWebServiceResponse UpdateDataSourceResponse CreateDataSourceResponse DeleteDataSourceResponse GetDataSourceResponse TagResourceR
esponse UntagResourceResponse ListTagsForResourceResponse UpdateTypeResponse CreateTypeResponse DeleteTypeResponse GetTypeResponse UpdateG
raphqlApiResponse CreateGraphqlApiResponse DeleteGraphqlApiResponse GetGraphqlApiResponse StartSchemaCreationResponse UpdateFunctionRespon
se CreateFunctionResponse DeleteFunctionResponse GetFunctionResponse ListResolversByFunctionResponse UpdateResolverResponse CreateResolver
Response DeleteResolverResponse GetResolverResponse ErrorResponse ListDataSourcesResponse ListTypesResponse ListGraphqlApisResponse ListFu
nctionsResponse ListResolversResponse GetSchemaCreationStatusResponse ListApiKeysResponse UpdateApiKeyResponse CreateApiKeyResponse Delete
ApiKeyResponse Dispose get_ResponseMappingTemplate set_ResponseMappingTemplate IsSetResponseMappingTemplate _responseMappingTemplate get_R
equestMappingTemplate set_RequestMappingTemplate IsSetRequestMappingTemplate _requestMappingTemplate state Write SuppressMessageAttribute
DebuggableAttribute ComVisibleAttribute AssemblyTitleAttribute AssemblyTrademarkAttribute AssemblyFileVersionAttribute AssemblyInformation
alVersionAttribute AssemblyConfigurationAttribute AssemblyDescriptionAttribute CompilationRelaxationsAttribute AllowPartiallyTrustedCaller
sAttribute AssemblyProductAttribute AssemblyCopyrightAttribute CLSCompliantAttribute AssemblyCompanyAttribute RuntimeCompatibilityAttribut
e AWSPropertyAttribute get_Value FindValue get_HasValue value Amazon.Runtime.IAmazonService.get_Config get_LambdaConfig set_LambdaConfig I
sSetLambdaConfig _lambdaConfig get_DynamodbConfig set_DynamodbConfig IsSetDynamodbConfig _dynamodbConfig AmazonAppSyncConfig LambdaDataSou
rceConfig DynamodbDataSourceConfig RelationalDatabaseDataSourceConfig ElasticsearchDataSourceConfig HttpDataSourceConfig get_PipelineConfi
g set_PipelineConfig IsSetPipelineConfig _pipelineConfig get_RelationalDatabaseConfig set_RelationalDatabaseConfig IsSetRelationalDatabase
Config _relationalDatabaseConfig get_LogConfig set_LogConfig IsSetLogConfig _logConfig get_ElasticsearchConfig set_ElasticsearchConfig IsS
etElasticsearchConfig _elasticsearchConfig get_UserPoolConfig set_UserPoolConfig CognitoUserPoolConfig IsSetUserPoolConfig _userPoolConfig
 get_AwsIamConfig set_AwsIamConfig IsSetAwsIamConfig _awsIamConfig get_AuthorizationConfig set_AuthorizationConfig IsSetAuthorizationConfi
g _authorizationConfig get_HttpConfig set_HttpConfig IsSetHttpConfig _httpConfig get_OpenIDConnectConfig set_OpenIDConnectConfig IsSetOpen
IDConnectConfig _openidConnectConfig IClientConfig clientConfig get_RdsHttpEndpointConfig set_RdsHttpEndpointConfig IsSetRdsHttpEndpointCo
nfig _rdsHttpEndpointConfig config Encoding get_OperationNameMapping FromString ToString BuildUserAgentString set_UseQueryString disposing
 set_ResourcePath ReadAtDepth get_CurrentDepth Amazon.Runtime.Internal.Auth get_GraphqlApi set_GraphqlApi EndUpdateGraphqlApi BeginUpdateG
raphqlApi EndCreateGraphqlApi BeginCreateGraphqlApi EndDeleteGraphqlApi BeginDeleteGraphqlApi EndGetGraphqlApi BeginGetGraphqlApi IsSetGra
phqlApi _graphqlApi AsyncCallback callback Seek Amazon.AppSync.Internal Amazon.Runtime.Internal Amazon.Util.Internal Amazon.AppSync.Model
get_FieldLogLevel set_FieldLogLevel IsSetFieldLogLevel _fieldLogLevel Amazon.Runtime.Internal.Util Amazon.Util Marshall Amazon.Runtime.Int
ernal.Transform.IUnmarshaller<Amazon.AppSync.Model.DataSource,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.
Runtime.Internal.Transform.IUnmarshaller<Amazon.AppSync.Model.Type,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Am
azon.Runtime.Internal.Transform.IUnmarshaller<Amazon.AppSync.Model.LambdaDataSourceConfig,Amazon.Runtime.Internal.Transform.XmlUnmarshalle
rContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.AppSync.Model.DynamodbDataSourceConfig,Amazon.Runtime.Internal
.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.AppSync.Model.RelationalDatabaseDataS
ourceConfig,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.Ap
pSync.Model.ElasticsearchDataSourceConfig,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Tra
nsform.IUnmarshaller<Amazon.AppSync.Model.HttpDataSourceConfig,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon
.Runtime.Internal.Transform.IUnmarshaller<Amazon.AppSync.Model.PipelineConfig,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Un
marshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.AppSync.Model.LogConfig,Amazon.Runtime.Internal.Transform.XmlUnmarshallerC
ontext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.AppSync.Model.UserPoolConfig,Amazon.Runtime.Internal.Transform.X
mlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.AppSync.Model.CognitoUserPoolConfig,Amazon.Runtim
e.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.AppSync.Model.AwsIamConfig,
Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.AppSync.Model.
AuthorizationConfig,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<A
mazon.AppSync.Model.OpenIDConnectConfig,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Trans
form.IUnmarshaller<Amazon.AppSync.Model.RdsHttpEndpointConfig,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.
Runtime.Internal.Transform.IUnmarshaller<Amazon.AppSync.Model.GraphqlApi,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarsh
all Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.AppSync.Model.FunctionConfiguration,Amazon.Runtime.Internal.Transform.XmlUnmars
hallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.AppSync.Model.AdditionalAuthenticationProvider,Amazon.Run
time.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.AppSync.Model.Resolver,A
mazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.AppSync.Model.A
piKey,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall AWSSDK.AppSync.dll FromBool _authttl _iatttl get_Stream CopyStr
eam FromMemoryStream set_Item System Amazon.Runtime.Internal.Transform awsSessionToken JsonToken get_NextToken set_NextToken IsSetNextToke
n _nextToken SeekOrigin get_SigningRegion set_SigningRegion IsSetSigningRegion _signingRegion get_AwsRegion set_AwsRegion IsSetAwsRegion _
awsRegion region get_ServiceVersion get_FunctionVersion set_FunctionVersion IsSetFunctionVersion _functionVersion set_MarshallerVersion Te
stExpression EndStartSchemaCreation BeginStartSchemaCreation get_FunctionConfiguration set_FunctionConfiguration IsSetFunctionConfiguratio
n _functionConfiguration System.Globalization System.Runtime.Serialization get_DefaultAction set_DefaultAction IsSetDefaultAction _default
Action System.Reflection get_ParameterCollection EndUpdateFunction BeginUpdateFunction EndCreateFunction BeginCreateFunction EndDeleteFunc
tion BeginDeleteFunction EndGetFunction BeginGetFunction EndListResolversByFunction BeginListResolversByFunction get_Definition set_Defini
tion IsSetDefinition _definition GraphQLSchemaException AmazonAppSyncException ApiLimitExceededException ApiKeyLimitExceededException Acce
ssDeniedException NotImplementedException UnauthorizedException NotFoundException AmazonServiceException InternalFailureException Unmarsha
llException ConcurrentModificationException innerException ApiKeyValidityOutOfBoundsException BadRequestException get_Description set_Desc
ription IsSetDescription _description ThirdParty.Json.LitJson Amazon get_Arn set_Arn get_DataSourceArn set_DataSourceArn IsSetDataSourceAr
n _dataSourceArn get_ResourceArn set_ResourceArn IsSetResourceArn _resourceArn get_ServiceRoleArn set_ServiceRoleArn IsSetServiceRoleArn _
serviceRoleArn get_CloudWatchLogsRoleArn set_CloudWatchLogsRoleArn IsSetCloudWatchLogsRoleArn _cloudWatchLogsRoleArn get_AwsSecretStoreArn
 set_AwsSecretStoreArn IsSetAwsSecretStoreArn _awsSecretStoreArn get_FunctionArn set_FunctionArn get_LambdaFunctionArn set_LambdaFunctionA
rn IsSetLambdaFunctionArn _lambdaFunctionArn IsSetFunctionArn _functionArn get_ResolverArn set_ResolverArn IsSetResolverArn _resolverArn I
sSetArn _arn CultureInfo SerializationInfo info AdditionalAuthenticationProvider IFormatProvider get_DbClusterIdentifier set_DbClusterIden
tifier IsSetDbClusterIdentifier _dbClusterIdentifier LambdaDataSourceConfigMarshaller DynamodbDataSourceConfigMarshaller RelationalDatabas
eDataSourceConfigMarshaller ElasticsearchDataSourceConfigMarshaller HttpDataSourceConfigMarshaller PipelineConfigMarshaller LogConfigMarsh
aller CognitoUserPoolConfigMarshaller AwsIamConfigMarshaller AuthorizationConfigMarshaller OpenIDConnectConfigMarshaller RdsHttpEndpointCo
nfigMarshaller AdditionalAuthenticationProviderMarshaller set_RequestMarshaller GetIntrospectionSchemaRequestMarshaller UpdateDataSourceRe
questMarshaller CreateDataSourceRequestMarshaller DeleteDataSourceRequestMarshaller GetDataSourceRequestMarshaller TagResourceRequestMarsh
aller UntagResourceRequestMarshaller ListTagsForResourceRequestMarshaller UpdateTypeRequestMarshaller CreateTypeRequestMarshaller DeleteTy
peRequestMarshaller GetTypeRequestMarshaller UpdateGraphqlApiRequestMarshaller CreateGraphqlApiRequestMarshaller DeleteGraphqlApiRequestMa
rshaller GetGraphqlApiRequestMarshaller StartSchemaCreationRequestMarshaller UpdateFunctionRequestMarshaller CreateFunctionRequestMarshall
er DeleteFunctionRequestMarshaller GetFunctionRequestMarshaller ListResolversByFunctionRequestMarshaller UpdateResolverRequestMarshaller C
reateResolverRequestMarshaller DeleteResolverRequestMarshaller GetResolverRequestMarshaller ListDataSourcesRequestMarshaller ListTypesRequ
estMarshaller ListGraphqlApisRequestMarshaller ListFunctionsRequestMarshaller ListResolversRequestMarshaller GetSchemaCreationStatusReques
tMarshaller ListApiKeysRequestMarshaller UpdateApiKeyRequestMarshaller CreateApiKeyRequestMarshaller DeleteApiKeyRequestMarshaller DataSou
rceUnmarshaller TypeUnmarshaller set_ResponseUnmarshaller GetIntrospectionSchemaResponseUnmarshaller UpdateDataSourceResponseUnmarshaller
CreateDataSourceResponseUnmarshaller DeleteDataSourceResponseUnmarshaller GetDataSourceResponseUnmarshaller TagResourceResponseUnmarshalle
r UntagResourceResponseUnmarshaller ListTagsForResourceResponseUnmarshaller UpdateTypeResponseUnmarshaller CreateTypeResponseUnmarshaller
DeleteTypeResponseUnmarshaller GetTypeResponseUnmarshaller UpdateGraphqlApiResponseUnmarshaller CreateGraphqlApiResponseUnmarshaller Delet
eGraphqlApiResponseUnmarshaller GetGraphqlApiResponseUnmarshaller StartSchemaCreationResponseUnmarshaller UpdateFunctionResponseUnmarshall
er CreateFunctionResponseUnmarshaller DeleteFunctionResponseUnmarshaller GetFunctionResponseUnmarshaller ListResolversByFunctionResponseUn
marshaller JsonResponseUnmarshaller UpdateResolverResponseUnmarshaller CreateResolverResponseUnmarshaller DeleteResolverResponseUnmarshall
er GetResolverResponseUnmarshaller JsonErrorResponseUnmarshaller ListDataSourcesResponseUnmarshaller ListTypesResponseUnmarshaller ListGra
phqlApisResponseUnmarshaller ListFunctionsResponseUnmarshaller ListResolversResponseUnmarshaller GetSchemaCreationStatusResponseUnmarshall
er ListApiKeysResponseUnmarshaller UpdateApiKeyResponseUnmarshaller CreateApiKeyResponseUnmarshaller DeleteApiKeyResponseUnmarshaller Lamb
daDataSourceConfigUnmarshaller DynamodbDataSourceConfigUnmarshaller RelationalDatabaseDataSourceConfigUnmarshaller ElasticsearchDataSource
ConfigUnmarshaller HttpDataSourceConfigUnmarshaller PipelineConfigUnmarshaller LogConfigUnmarshaller CognitoUserPoolConfigUnmarshaller Aws
IamConfigUnmarshaller AuthorizationConfigUnmarshaller OpenIDConnectConfigUnmarshaller RdsHttpEndpointConfigUnmarshaller StringUnmarshaller
 LongUnmarshaller GraphqlApiUnmarshaller BoolUnmarshaller FunctionConfigurationUnmarshaller AdditionalAuthenticationProviderUnmarshaller R
esolverUnmarshaller ApiKeyUnmarshaller AWS4Signer AbstractAWSSigner CreateSigner get_Writer StringWriter JsonWriter TextWriter get_Issuer
set_Issuer IsSetIssuer _issuer get_Resolver set_Resolver EndUpdateResolver BeginUpdateResolver EndCreateResolver BeginCreateResolver EndDe
leteResolver BeginDeleteResolver EndGetResolver BeginGetResolver IsSetResolver _resolver GetEnumerator .ctor .cctor System.Diagnostics Sys
tem.Runtime.InteropServices System.Runtime.CompilerServices get_DataSources set_DataSources IsSetDataSources EndListDataSources BeginListD
ataSources _dataSources DebuggingModes get_Types set_Types IsSetTypes EndListTypes BeginListTypes _types get_Expires set_Expires IsSetExpi
res _expires GetBytes get_IncludeDirectives set_IncludeDirectives IsSetIncludeDirectives _includeDirectives get_Tags set_Tags IsSetTags _t
ags get_GraphqlApis set_GraphqlApis IsSetGraphqlApis EndListGraphqlApis BeginListGraphqlApis _graphqlApis get_Uris set_Uris IsSetUris _uri
s System.Diagnostics.CodeAnalysis AWSCredentials get_UseCallerCredentials set_UseCallerCredentials IsSetUseCallerCredentials _useCallerCre
dentials GetCredentials credentials Equals get_Details set_Details IsSetDetails _details AWSSDKUtils InternalSDKUtils StringUtils Amazon.A
ppSync.Model.Internal.MarshallTransformations get_Functions set_Functions IsSetFunctions EndListFunctions BeginListFunctions _functions In
vokeOptions get_Headers get_AdditionalAuthenticationProviders set_AdditionalAuthenticationProviders IsSetAdditionalAuthenticationProviders
 _additionalAuthenticationProviders get_Parameters get_Resolvers set_Resolvers IsSetResolvers EndListResolvers BeginListResolvers _resolve
rs ConstantClass get_MaxResults set_MaxResults IsSetMaxResults _maxResults get_Status set_Status SchemaStatus EndGetSchemaCreationStatus B
eginGetSchemaCreationStatus IsSetStatus _status get_TagKeys set_TagKeys IsSetTagKeys _tagKeys get_ApiKeys set_ApiKeys IsSetApiKeys EndList
ApiKeys BeginListApiKeys _apiKeys get_Format set_Format TypeDefinitionFormat IsSetFormat _format requestObject System.Net op_Implicit GetV
alueOrDefault IAsyncResult asyncResult FromInt get_UserAgent _userAgent AmazonAppSyncClient AmazonServiceClient get_Current set_Content ge
t_ExcludeVerboseContent set_ExcludeVerboseContent IsSetExcludeVerboseContent _excludeVerboseContent get_Endpoint set_Endpoint set_RegionEn
dpoint IsSetEndpoint _endpoint get_Count WriteObjectStart WriteArrayStart IRequest GetIntrospectionSchemaRequest publicRequest AmazonAppSy
ncRequest AmazonWebServiceRequest UpdateDataSourceRequest CreateDataSourceRequest DeleteDataSourceRequest GetDataSourceRequest TagResource
Request UntagResourceRequest ListTagsForResourceRequest UpdateTypeRequest CreateTypeRequest DeleteTypeRequest GetTypeRequest UpdateGraphql
ApiRequest CreateGraphqlApiRequest DeleteGraphqlApiRequest GetGraphqlApiRequest StartSchemaCreationRequest UpdateFunctionRequest CreateFun
ctionRequest DeleteFunctionRequest GetFunctionRequest ListResolversByFunctionRequest UpdateResolverRequest CreateResolverRequest DeleteRes
olverRequest GetResolverRequest ListDataSourcesRequest ListTypesRequest ListGraphqlApisRequest ListFunctionsRequest ListResolversRequest G
etSchemaCreationStatusRequest ListApiKeysRequest DefaultRequest UpdateApiKeyRequest CreateApiKeyRequest DeleteApiKeyRequest request input
MoveNext System.Text StreamingContext JsonMarshallerContext XmlUnmarshallerContext JsonUnmarshallerContext context get_AppIdClientRegex se
t_AppIdClientRegex IsSetAppIdClientRegex _appIdClientRegex get_Key get_ApiKey set_ApiKey EndUpdateApiKey BeginUpdateApiKey EndCreateApiKey
 BeginCreateApiKey EndDeleteApiKey BeginDeleteApiKey IsSetApiKey _apiKey awsSecretAccessKey FallbackCredentialsFactory op_Inequality Syste
m.Security   a p p s y n c  2 0 1 7 - 0 7 - 2 5 3 . 3 . 1 0 2 . 6  3A M A Z O N _ C O G N I T O _ U S E R _ P O O L S  A P I _ K E Y
 A W S _ I A M  O P E N I D _ C O N N E C T  A M A Z O N _ D Y N A M O D B  )A M A Z O N _ E L A S T I C S E A R C H  A W S _ L A M B
D A     H T T P         N O N E  'R E L A T I O N A L _ D A T A B A S E  A L L O W     D E N Y  A L L  E R R O R
J S O N  S D L  #R D S _ H T T P _ E N D P O I N T  P I P E L I N E    U N I T
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.AppSync.xml:6047:        <member
name="F:Amazon.AppSync.AuthenticationType.API_KEY">
C:\Program Files (x86)\AWS SDK for .NET\bin\Net35\AWSSDK.AppSync.xml:6049:            Constant API_KEY for AuthenticationType
C:\Program Files (x86)\AWS SDK for .NET\bin\Net45\AWSSDK.APIGateway.dll:17465:��' �      TLS_1_0 GB_6_1 Nullable`1 Task`1 List`1 TLS_1_2
 GB_58_2 IMarshaller`2 IRequestMarshaller`2 IUnmarshaller`2 ListUnmarshaller`2 KeyValuePair`2 IDictionary`2 FAIL_WITH_403 Int64 GB_28_4 Di
ctionaryUnmarshaller`4 GB_0_5 GB_13_5 GB_1_6 GB_237 GB_118 get_UTF8 <Module> QUOTA_EXCEEDED ACCESS_DENIED FAILED THROTTLED UNDOCUMENTED UN
AUTHORIZED RESOURCE_NOT_FOUND METHOD RESOURCE EDGE REQUEST_TOO_LARGE NOT_AVAILABLE UNSUPPORTED_MEDIA_TYPE INTEGRATION_FAILURE AUTHORIZER_F
AILURE INVALID_SIGNATURE RESPONSE PRIVATE PENDING UPDATING DELETING MONTH API MOCK WEEK VPC_LINK REGIONAL MODEL EXPIRED_TOKEN MISSING_AUTH
ENTICATION_TOKEN System.IO HTTP SUCCEED_WITH_RESPONSE_HEADER SUCCEED_WITHOUT_RESPONSE_HEADER REQUEST_HEADER PATH_PARAMETER QUERY_PARAMETER
 AUTHORIZER API_CONFIGURATION_ERROR AUTHORIZER_CONFIGURATION_ERROR COGNITO_USER_POOLS BAD_REQUEST_PARAMETERS CREATE_IN_PROGRESS DELETE_IN_
PROGRESS FLUSH_IN_PROGRESS AWS INTERNET REQUEST INTEGRATION_TIMEOUT CONVERT_TO_TEXT DEFAULT_4XX DEFAULT_5XX DAY RESPONSE_BODY BAD_REQUEST_
BODY INVALID_API_KEY CONVERT_TO_BINARY HTTP_PROXY AWS_PROXY get_Schema set_Schema IsSetSchema _schema get_ResponseData IWebResponseData IS
erviceMetadata get_ServiceMetadata serviceMetadata AmazonAPIGatewayMetadata get_Quota set_Quota IsSetQuota _quota mscorlib get_PercentTraf
fic set_PercentTraffic IsSetPercentTraffic _percentTraffic System.Collections.Generic InvokeSync TestInvokeMethodAsync UpdateMethodAsync D
eleteMethodAsync GetMethodAsync PutMethodAsync UpdateResourceAsync CreateResourceAsync DeleteResourceAsync TagResourceAsync UntagResourceA
sync GetResourceAsync UpdateUsageAsync GetUsageAsync UpdateStageAsync CreateStageAsync DeleteStageAsync GetStageAsync FlushStageCacheAsync
 FlushStageAuthorizersCacheAsync InvokeAsync UpdateDomainNameAsync CreateDomainNameAsync DeleteDomainNameAsync GetDomainNameAsync GetSdkTy
peAsync UpdateMethodResponseAsync DeleteMethodResponseAsync GetMethodResponseAsync PutMethodResponseAsync UpdateIntegrationResponseAsync D
eleteIntegrationResponseAsync GetIntegrationResponseAsync PutIntegrationResponseAsync UpdateGatewayResponseAsync DeleteGatewayResponseAsyn
c GetGatewayResponseAsync PutGatewayResponseAsync UpdateClientCertificateAsync GenerateClientCertificateAsync DeleteClientCertificateAsync
 GetClientCertificateAsync GetModelTemplateAsync UpdateBasePathMappingAsync CreateBasePathMappingAsync DeleteBasePathMappingAsync GetBaseP
athMappingAsync UpdateRestApiAsync CreateRestApiAsync DeleteRestApiAsync GetRestApiAsync ImportRestApiAsync PutRestApiAsync GetSdkAsync Up
dateVpcLinkAsync CreateVpcLinkAsync DeleteVpcLinkAsync GetVpcLinkAsync UpdateModelAsync CreateModelAsync DeleteModelAsync GetModelAsync Up
dateUsagePlanAsync CreateUsagePlanAsync DeleteUsagePlanAsync GetUsagePlanAsync UpdateDocumentationVersionAsync CreateDocumentationVersionA
sync DeleteDocumentationVersionAsync GetDocumentationVersionAsync UpdateIntegrationAsync DeleteIntegrationAsync GetIntegrationAsync PutInt
egrationAsync TestInvokeAuthorizerAsync UpdateAuthorizerAsync CreateAuthorizerAsync DeleteAuthorizerAsync GetAuthorizerAsync UpdateRequest
ValidatorAsync CreateRequestValidatorAsync DeleteRequestValidatorAsync GetRequestValidatorAsync GetResourcesAsync GetStagesAsync GetDomain
NamesAsync GetSdkTypesAsync GetGatewayResponsesAsync GetClientCertificatesAsync GetTagsAsync GetBasePathMappingsAsync GetRestApisAsync Get
VpcLinksAsync GetModelsAsync GetUsagePlansAsync GetDocumentationVersionsAsync GetAuthorizersAsync GetRequestValidatorsAsync GetDeployments
Async GetDocumentationPartsAsync ImportDocumentationPartsAsync GetApiKeysAsync ImportApiKeysAsync GetUsagePlanKeysAsync UpdateDeploymentAs
ync CreateDeploymentAsync DeleteDeploymentAsync GetDeploymentAsync UpdateAccountAsync GetAccountAsync UpdateDocumentationPartAsync CreateD
ocumentationPartAsync DeleteDocumentationPartAsync GetDocumentationPartAsync GetExportAsync UpdateApiKeyAsync CreateApiKeyAsync DeleteApiK
eyAsync GetApiKeyAsync CreateUsagePlanKeyAsync DeleteUsagePlanKeyAsync GetUsagePlanKeyAsync get_Id set_Id get_ServiceId get_ResourceId set
_ResourceId IsSetResourceId _resourceId get_RegionalHostedZoneId set_RegionalHostedZoneId IsSetRegionalHostedZoneId _regionalHostedZoneId
get_DistributionHostedZoneId set_DistributionHostedZoneId IsSetDistributionHostedZoneId _distributionHostedZoneId get_ClientCertificateId
set_ClientCertificateId IsSetClientCertificateId _clientCertificateId get_ApiId set_ApiId IsSetApiId get_RestApiId set_RestApiId IsSetRest
ApiId _restApiId _apiId get_VpcLinkId set_VpcLinkId IsSetVpcLinkId _vpcLinkId get_PrincipalId set_PrincipalId IsSetPrincipalId _principalI
d get_UsagePlanId set_UsagePlanId IsSetUsagePlanId _usagePlanId get_ConnectionId set_ConnectionId IsSetConnectionId _connectionId get_Cust
omerId set_CustomerId IsSetCustomerId _customerId get_AuthorizerId set_AuthorizerId IsSetAuthorizerId _authorizerId get_RequestValidatorId
 set_RequestValidatorId IsSetRequestValidatorId _requestValidatorId get_GenerateDistinctId set_GenerateDistinctId IsSetGenerateDistinctId
_generateDistinctId IsSetId get_DeploymentId set_DeploymentId IsSetDeploymentId _deploymentId get_ParentId set_ParentId IsSetParentId _par
entId get_DocumentationPartId set_DocumentationPartId IsSetDocumentationPartId _documentationPartId get_RequestId requestId get_KeyId set_
KeyId awsAccessKeyId IsSetKeyId _keyId Read Add get_Embed set_Embed IsSetEmbed _embed get_Enabled set_Enabled get_DataTraceEnabled set_Dat
aTraceEnabled IsSetDataTraceEnabled _dataTraceEnabled get_TracingEnabled set_TracingEnabled IsSetTracingEnabled _tracingEnabled get_Cachin
gEnabled set_CachingEnabled IsSetCachingEnabled _cachingEnabled get_CacheClusterEnabled set_CacheClusterEnabled IsSetCacheClusterEnabled _
cacheClusterEnabled get_MetricsEnabled set_MetricsEnabled IsSetMetricsEnabled _metricsEnabled IsSetEnabled _enabled get_Required set_Requi
red IsSetRequired get_ApiKeyRequired set_ApiKeyRequired IsSetApiKeyRequired _apiKeyRequired _required get_CacheDataEncrypted set_CacheData
Encrypted IsSetCacheDataEncrypted _cacheDataEncrypted _id WriteObjectEnd WriteArrayEnd get_Method set_Method TestInvokeMethod UpdateMethod
 DeleteMethod get_HttpMethod set_HttpMethod get_IntegrationHttpMethod set_IntegrationHttpMethod IsSetIntegrationHttpMethod _integrationHtt
pMethod IsSetHttpMethod _httpMethod GetMethod IsSetMethod PutMethod _method get_Period set_Period IsSetPeriod _period Replace get_CacheNam
espace set_CacheNamespace IsSetCacheNamespace _cacheNamespace IAmazonService get_Instance GetInstance _instance get_ApiKeySource set_ApiKe
ySource IsSetApiKeySource _apiKeySource get_IdentitySource set_IdentitySource IsSetIdentitySource _identitySource AddSubResource UpdateRes
ource CreateResource DeleteResource TagResource UntagResource AddPathResource GetResource get_Code errorCode get_StatusCode set_StatusCode
 HttpStatusCode IsSetStatusCode _statusCode get_ProductCode set_ProductCode IsSetProductCode _productCode get_Mode set_Mode IsSetMode PutM
ode _mode UpdateUsage GetUsage get_Message get_StatusMessage set_StatusMessage get_DomainNameStatusMessage set_DomainNameStatusMessage IsS
etDomainNameStatusMessage _domainNameStatusMessage IsSetStatusMessage _statusMessage message get_Stage set_Stage UpdateStage CreateStage D
eleteStage ApiStage GetStage IsSetStage _stage Merge get_UseStageCache set_UseStageCache IsSetUseStageCache _useStageCache FlushStageCache
 FlushStageAuthorizersCache PreInvoke IDisposable get_Throttle set_Throttle IsSetThrottle _throttle get_Name set_Name set_AuthenticationSe
rviceName get_RegionEndpointServiceName get_StageName set_StageName IsSetStageName _stageName get_CertificateName set_CertificateName get_
RegionalCertificateName set_RegionalCertificateName IsSetRegionalCertificateName _regionalCertificateName IsSetCertificateName _certificat
eName get_ModelName set_ModelName IsSetModelName _modelName get_DomainName set_DomainName UpdateDomainName CreateDomainName DeleteDomainNa
me get_RegionalDomainName set_RegionalDomainName IsSetRegionalDomainName _regionalDomainName get_DistributionDomainName set_DistributionDo
mainName IsSetDistributionDomainName _distributionDomainName GetDomainName IsSetDomainName _domainName get_OperationName set_OperationName
 IsSetOperationName _operationName IsSetName get_FriendlyName set_FriendlyName IsSetFriendlyName _friendlyName WritePropertyName _name Dat
eTime Amazon.Runtime CustomizeRuntimePipeline pipeline get_Type set_Type QuotaPeriodType ApiKeySourceType get_ResponseType set_ResponseTyp
e IsSetResponseType GatewayResponseType _responseType get_AuthType set_AuthType IsSetAuthType _authType get_SdkType set_SdkType GetSdkType
 IsSetSdkType _sdkType get_CurrentTokenType IntegrationType get_AuthorizationType set_AuthorizationType IsSetAuthorizationType _authorizat
ionType get_ConnectionType set_ConnectionType IsSetConnectionType _connectionType AuthorizerType ErrorType errorType LocationStatusType Is
SetType get_ContentType set_ContentType IsSetContentType _contentType EndpointType DocumentationPartType get_ExportType set_ExportType IsS
etExportType _exportType get_KeyType set_KeyType IsSetKeyType _keyType _type AWSSDK.Core get_InvariantCulture InvokeOptionsBase TestInvoke
MethodResponse UpdateMethodResponse DeleteMethodResponse GetMethodResponse PutMethodResponse AmazonWebServiceResponse UpdateResourceRespon
se CreateResourceResponse DeleteResourceResponse TagResourceResponse UntagResourceResponse GetResourceResponse UpdateUsageResponse GetUsag
eResponse UpdateStageResponse CreateStageResponse DeleteStageResponse GetStageResponse FlushStageCacheResponse FlushStageAuthorizersCacheR
esponse UpdateDomainNameResponse CreateDomainNameResponse DeleteDomainNameResponse GetDomainNameResponse GetSdkTypeResponse UpdateMethodRe
sponseResponse DeleteMethodResponseResponse GetMethodResponseResponse PutMethodResponseResponse UpdateIntegrationResponseResponse DeleteIn
tegrationResponseResponse GetIntegrationResponseResponse PutIntegrationResponseResponse UpdateGatewayResponseResponse DeleteGatewayRespons
eResponse GetGatewayResponseResponse PutGatewayResponseResponse UpdateClientCertificateResponse GenerateClientCertificateResponse DeleteCl
ientCertificateResponse GetClientCertificateResponse GetModelTemplateResponse UpdateBasePathMappingResponse CreateBasePathMappingResponse
DeleteBasePathMappingResponse GetBasePathMappingResponse UpdateRestApiResponse CreateRestApiResponse DeleteRestApiResponse GetRestApiRespo
nse ImportRestApiResponse PutRestApiResponse GetSdkResponse UpdateVpcLinkResponse CreateVpcLinkResponse DeleteVpcLinkResponse GetVpcLinkRe
sponse UpdateModelResponse CreateModelResponse DeleteModelResponse GetModelResponse UpdateUsagePlanResponse CreateUsagePlanResponse Delete
UsagePlanResponse GetUsagePlanResponse UpdateDocumentationVersionResponse CreateDocumentationVersionResponse DeleteDocumentationVersionRes
ponse GetDocumentationVersionResponse UpdateIntegrationResponse DeleteIntegrationResponse GetIntegrationResponse PutIntegrationResponse Te
stInvokeAuthorizerResponse UpdateAuthorizerResponse CreateAuthorizerResponse DeleteAuthorizerResponse GetAuthorizerResponse ErrorResponse
UpdateRequestValidatorResponse CreateRequestValidatorResponse DeleteRequestValidatorResponse GetRequestValidatorResponse GetResourcesRespo
nse GetStagesResponse GetDomainNamesResponse GetSdkTypesResponse GetGatewayResponsesResponse GetClientCertificatesResponse GetTagsResponse
 GetBasePathMappingsResponse GetRestApisResponse GetVpcLinksResponse GetModelsResponse GetUsagePlansResponse GetDocumentationVersionsRespo
nse GetAuthorizersResponse GetRequestValidatorsResponse GetDeploymentsResponse GetDocumentationPartsResponse ImportDocumentationPartsRespo
nse GetApiKeysResponse ImportApiKeysResponse GetUsagePlanKeysResponse get_DefaultResponse set_DefaultResponse IsSetDefaultResponse _defaul
tResponse UpdateDeploymentResponse CreateDeploymentResponse DeleteDeploymentResponse GetDeploymentResponse UpdateAccountResponse GetAccoun
tResponse UpdateDocumentationPartResponse CreateDocumentationPartResponse DeleteDocumentationPartResponse GetDocumentationPartResponse Get
ExportResponse UpdateGatewayResponse DeleteGatewayResponse GetGatewayResponse PutGatewayResponse UpdateApiKeyResponse CreateApiKeyResponse
 DeleteApiKeyResponse GetApiKeyResponse CreateUsagePlanKeyResponse DeleteUsagePlanKeyResponse GetUsagePlanKeyResponse Dispose get_Certific
ateUploadDate set_CertificateUploadDate IsSetCertificateUploadDate _certificateUploadDate get_LastUpdatedDate set_LastUpdatedDate IsSetLas
tUpdatedDate _lastUpdatedDate get_CreatedDate set_CreatedDate IsSetCreatedDate _createdDate get_EndDate set_EndDate IsSetEndDate _endDate
get_ExpirationDate set_ExpirationDate IsSetExpirationDate _expirationDate get_StartDate set_StartDate IsSetStartDate _startDate get_PemEnc
odedCertificate set_PemEncodedCertificate IsSetPemEncodedCertificate _pemEncodedCertificate UpdateClientCertificate GenerateClientCertific
ate DeleteClientCertificate GetClientCertificate GetModelTemplate Write Overwrite SuppressMessageAttribute DebuggableAttribute ComVisibleA
ttribute AssemblyTitleAttribute AssemblyTrademarkAttribute TargetFrameworkAttribute AssemblyFileVersionAttribute AssemblyInformationalVers
ionAttribute AssemblyConfigurationAttribute AssemblyDescriptionAttribute CompilationRelaxationsAttribute AllowPartiallyTrustedCallersAttri
bute AssemblyProductAttribute AssemblyCopyrightAttribute CLSCompliantAttribute AssemblyCompanyAttribute RuntimeCompatibilityAttribute AWSP
ropertyAttribute get_Value set_Value FindValue get_IncludeValue set_IncludeValue IsSetIncludeValue _includeValue GetHeaderValue get_HasVal
ue IsSetValue get_DefaultValue set_DefaultValue IsSetDefaultValue _defaultValue _value Move Remove get_MinimumCompressionSize set_MinimumC
ompressionSize IsSetMinimumCompressionSize _minimumCompressionSize get_CacheClusterSize set_CacheClusterSize IsSetCacheClusterSize _cacheC
lusterSize Amazon.Runtime.IAmazonService.get_Config IClientConfig clientConfig AmazonAPIGatewayConfig config System.Threading Encoding get
_ContentHandling set_ContentHandling IsSetContentHandling _contentHandling System.Runtime.Versioning get_OperationNameMapping UpdateBasePa
thMapping CreateBasePathMapping DeleteBasePathMapping GetBasePathMapping FromString ToString BuildUserAgentString set_UseQueryString get_P
athWithQueryString set_PathWithQueryString IsSetPathWithQueryString _pathWithQueryString disposing MethodSetting get_Log set_Log IsSetLog
_log get_Path set_Path set_ResourcePath get_BasePath set_BasePath IsSetBasePath _basePath IsSetPath _path get_Length ReadAtDepth get_Curre
ntDepth Amazon.Runtime.Internal.Auth UpdateRestApi CreateRestApi DeleteRestApi GetRestApi ImportRestApi PutRestApi get_Uri set_Uri get_Aut
horizerUri set_AuthorizerUri IsSetAuthorizerUri _authorizerUri IsSetUri _uri GetSdk Seek UpdateVpcLink CreateVpcLink DeleteVpcLink GetVpcL
ink Amazon.Runtime.Internal Amazon.Util.Internal Amazon.APIGateway.Internal Amazon.APIGateway.Model UpdateModel CreateModel DeleteModel Ge
tModel get_LoggingLevel set_LoggingLevel IsSetLoggingLevel _loggingLevel Amazon.Runtime.Internal.Util Amazon.Util Marshall Amazon.Runtime.
Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.Method,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazo
n.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.Resource,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unma
rshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.Stage,Amazon.Runtime.Internal.Transform.XmlUnmarshallerCont
ext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.ApiStage,Amazon.Runtime.Internal.Transform.XmlUnma
rshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.DomainName,Amazon.Runtime.Internal.Tra
nsform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.SdkType,Amazon.Runtime.I
nternal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.MethodRespons
e,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.M
odel.IntegrationResponse,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshal
ler<Amazon.APIGateway.Model.GatewayResponse,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.T
ransform.IUnmarshaller<Amazon.APIGateway.Model.ClientCertificate,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amaz
on.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.BasePathMapping,Amazon.Runtime.Internal.Transform.XmlUnmarshallerConte
xt>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.MethodSetting,Amazon.Runtime.Internal.Transform.Xml
UnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.RestApi,Amazon.Runtime.Internal.Tr
ansform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.VpcLink,Amazon.Runtime.
Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.Model,Amazon
.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGateway.Model.Usa
gePlan,Amazon.Runtime.Internal.Transform.XmlUnmarshallerContext>.Unmarshall Amazon.Runtime.Internal.Transform.IUnmarshaller<Amazon.APIGate
