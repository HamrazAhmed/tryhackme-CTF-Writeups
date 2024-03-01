---
Leverage tool-agnostic software obfuscation practices to hide malicious functions and create unique code.
---

# Obfuscation Principles — Writeup

## Overview
### Obfuscation Principles — Writeup
### Obfuscation Principles — Writeup
![|333](https://tryhackme-images.s3.amazonaws.com/room-icons/7ec073c23670722c04caa1056194f8aa.png)
### Introduction
Obfuscation is an essential component of detection evasion methodology and preventing analysis of malicious software. Obfuscation originated to protect software and intellectual property from being stolen or reproduced. While it is still widely used for its original purpose, adversaries have adapted its use for malicious intent.
In this room, we will observe obfuscation from multiple perspectives and break down obfuscation methods.
Learning Objectives
Learn how to evade modern detection engineering using tool-agnostic obfuscation
Understand the principles of obfuscation and its origins from intellectual property protection
Implement obfuscation methods to hide malicious functions
Before beginning this room, familiarize yourself with basic programming logic and syntax. Knowledge of C and PowerShell is recommended but not required.
We have provided several machines with the required files and web servers to complete this room. Using the credentials below, you can access the machine and web server in-browser or through RDP.
Machine IP: MACHINE_IP             Username: Student             Password: TryHackMe!
This is going to be a lot of information. Please put on your evil helmets and locate your nearest fire extinguisher.
### Origins of Obfuscation
Obfuscation is widely used in many software-related fields to protect IP (Intellectual Property) and other proprietary information an application may contain.
For example, the popular game: Minecraft uses the obfuscator [ProGuard](https://github.com/Guardsquare/proguard) to obfuscate and minimize its Java classes. Minecraft also releases obfuscation maps with limited information as a translator between the old un-obfuscated classes and the new obfuscated classes to support the modding community.
This is only one example of the wide range of ways obfuscation is publicly used. To document and organize the variety of obfuscation methods, we can reference the Layered obfuscation: a taxonomy of software obfuscation techniques for layered security paper. This research paper organizes obfuscation methods by layers, similar to the OSI model but for application data flow. Below is the figure used as the complete overview of each taxonomy layer.
https://cybersecurity.springeropen.com/track/pdf/10.1186/s42400-020-00049-3.pdf
Each sub-layer is then broken down into specific methods that can achieve the overall objective of the sub-layer.
In this room, we will primarily focus on the code-element layer of the taxonomy, as seen in the figure below.
To use the taxonomy, we can determine an objective and then pick a method that fits our requirements. For example, suppose we want to obfuscate the layout of our code but cannot modify the existing code. In that case, we can inject junk code, summarized by the taxonomy:
Code Element Layer > Obfuscating Layout > Junk Codes.
But how could this be used maliciously? Adversaries and malware developers can leverage obfuscation to break signatures or prevent program analysis. In the upcoming tasks, we will discuss both perspectives of malware obfuscation, including the purpose and underlying techniques of each.
How many core layers make up the Layered Obfuscation Taxonomy?
*4*
What sub-layer of the Layered Obfuscation Taxonomy encompasses meaningless identifiers?
*Obfuscating Layout*
### Obfuscation's Function for Static Evasion
Two of the more considerable security boundaries in the way of an adversary are anti-virus engines and EDR (Endpoint Detection & Response) solutions. As covered in the Introduction to Anti-virus room, both platforms will leverage an extensive database of known signatures referred to as static signatures as well as heuristic signatures that consider application behavior.
To evade signatures, adversaries can leverage an extensive range of logic and syntax rules to implement obfuscation. This is commonly achieved by abusing data obfuscation practices that hide important identifiable information in legitimate applications.
The aforementioned white paper: Layered Obfuscation Taxonomy, summarizes these practices well under the code-element layer. Below is a table of methods covered by the taxonomy in the obfuscating data sub-layer.
Diagram showing the objectives of the Obfuscating Data Sub-Layer: Array Transformation, Data Encoding, Data Procedurization, and Data Splitting/Merging
Obfuscation Method	Purpose
Array Transformation
Transforms an array by splitting, merging, folding, and flattening
Data Encoding
Encodes data with mathematical functions or ciphers
Data Procedurization
Substitutes static data with procedure calls
Data Splitting/Merging
Distributes information of one variable into several new variables
In the upcoming tasks, we will primarily focus on data splitting/merging; because static signatures are weaker, we generally only need to focus on that one aspect in initial obfuscation.
Check out the Encoding/Packing/Binder/Crypters room for more information about data encoding, and the Signature Evasion room for more information about data procedurization and transformation.
What obfuscation method will break or split an object?
*Data Splitting*
What obfuscation method is used to rewrite static data with a procedure call?
*Data Procedurization*
### Object Concatenation
Concatenation is a common programming concept that combines two separate objects into one object, such as a string.
A pre-defined operator defines where the concatenation will occur to combine two independent objects. Below is a generic example of string concatenation in Python.
```text
┌──(kali㉿kali)-[~]
└─$ python
Python 3.10.5 (main, Jun  8 2022, 09:26:22) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = "hi "
>>> b = "dog"
>>> c = a + b
>>> print(c)
hi dog
```
```text
>>> A = "Hello "
>>> B = "THM"
>>> C = A + B
>>> print(C)
Hello THM
>>>
```
Depending on the language used in a program, there may be different or multiple pre-defined operators than can be used for concatenation. Below is a small table of common languages and their corresponding pre-defined operators.
Language
Concatenation Operator
Python
“+”
PowerShell
“+”, ”,”, ”$”, or no operator at all
C#
“+”, “String.Join”, “String.Concat”
C
“strcat”
C++
“+”, “append”
The aforementioned white paper: Layered Obfuscation Taxonomy, summarizes these practices well under the code-element layer’s data splitting/merging sub-layer.
What does this mean for attackers? Concatenation can open the doors to several vectors to modify signatures or manipulate other aspects of an application. The most common example of concatenation being used in malware is breaking targeted static signatures, as covered in the Signature Evasion room. Attackers can also use it preemptively to break up all objects of a program and attempt to remove all signatures at once without hunting them down, commonly seen in obfuscators as covered in task 9.
Below we will observe a static Yara rule and attempt to use concatenation to evade the static signature.
```text
rule ExampleRule
{
    strings:
        $text_string = "AmsiScanBuffer"
        $hex_string = { B8 57 00 07 80 C3 }

    condition:
        $my_text_string or $my_hex_string
}
```
When a compiled binary is scanned with Yara, it will create a positive alert/detection if the defined string is present. Using concatenation, the string can be functionally the same but will appear as two independent strings when scanned, resulting in no alerts.
IntPtr ASBPtr = GetProcAddress(TargetDLL, "AmsiScanBuffer");
IntPtr ASBPtr = GetProcAddress(TargetDLL, "Amsi" + "Scan" + "Buffer");
If the second code block were to be scanned with the Yara rule, there would be no alerts!
Extending from concatenation, attackers can also use non-interpreted characters to disrupt or confuse a static signature. These can be used independently or with concatenation, depending on the strength/implementation of the signature. Below is a table of some common non-interpreted characters that we can leverage.
Character
Purpose
Example
Breaks
Break a single string into multiple sub strings and combine them
```text
('co'+'ffe'+'e')
Reorders
	Reorder a string’s components
	

('{1}{0}'-f'ffee','co')
Whitespace
	Include white space that is not interpreted
	

.( 'Ne' +'w-Ob' + 'ject')
Ticks
	Include ticks that are not interpreted
	

d`own`LoAd`Stri`ng
Random Case
	Tokens are generally not case sensitive and can be any arbitrary case
	

dOwnLoAdsTRing
```
Using the knowledge you have accrued throughout this task, obfuscate the following PowerShell snippet until it evades Defender’s detections.
![[Pasted image 20220916165550.png]]
To get you started, we recommend breaking up each section of the code and observe how it interacts or is detected. You can then break the signature present in the independent section and add another section to it until you have a clean snippet.
Once you think your snippet is sufficiently obfuscated, submit it to the webserver at http://10.10.25.43 ; if successful a flag will appear in a pop-up.
If you are still stuck we have provided a walkthrough of the solution below.
What flag is found after uploading a properly obfuscated snippet?
![[Pasted image 20220916193019.png]]
![[Pasted image 20220916193004.png]]
### Obfuscation's Function for Analysis Deception
After obfuscating basic functions of malicious code, it may be able to pass software detections but is still susceptible to human analysis. While not a security boundary without further policies, analysts and reverse engineers can gain deep insight into the functionality of our malicious application and halt operations.
Adversaries can leverage advanced logic and mathematics to create more complex and harder-to-understand code to combat analysis and reverse engineering.
For more information about reverse engineering, check out the Malware Analysis module.
The aforementioned white paper: Layered Obfuscation Taxonomy, summarizes these practices well under other sub-layers of the code-element layer. Below is a table of methods covered by the taxonomy in the obfuscating layout and obfuscating controls sub-layers.
Obfuscation Method
Purpose
Junk Code
Add junk instructions that are non-functional, also known as a code stubs
Separation of Related Code
Separate related codes or instructions to increase difficulty in reading the program
Stripping Redundant Symbols
Strips symbolic information such as debug information or other symbol tables
Meaningless Identifiers
Transform a meaningful identifier to something meaningless
Implicit Controls
Converts explicit controls instructions to implicit instructions
Dispatcher-based Controls
Determines the next block to be executed during the runtime
Probabilistic Control Flows
Introduces replications of control flows with the same semantics but different syntax
Bogus Control Flows
Control flows deliberately added to a program but will never be executed
In the upcoming tasks, we will demonstrate several of the above methods in an agnostic format.
Check out the Sandbox Evasion room for more information about anti-analysis and anti-reversing
What are junk instructions referred to as in junk code?
*Code stubs*
What obfuscation layer aims to confuse an analyst by manipulating the code flow and abstract syntax trees?
*Obfuscating Controls*
### Code Flow and Logic
Control flow is a critical component of a program’s execution that will define how a program will logically proceed. Logic is one of the most significant determining factors to an application’s control flow and encompasses various uses such as if/else statements or for loops. A program will traditionally execute from the top-down; when a logic statement is encountered, it will continue execution by following the statement.
Below is a table of some logic statements you may encounter when dealing with control flows or program logic.
Logic Statement
Purpose
if/else
Executes only if a condition is met, else it will execute a different code block
try/catch
Will try to execute a code block and catch it if it fails to handle errors.
switch case
A switch will follow similar conditional logic to an if statement but checks several different possible conditions with cases before resolving to a break or default
for/while loop
A for loop will execute for a set amount of a condition. A while loop will execute until a condition is no longer met.
To make this concept concrete, we can observe an example function and its corresponding CFG (Control Flow Graph) to depict it’s possible control flow paths.
```text
x = 10 
if(x > 7):
	print("This executes")
else:
	print("This is ignored")
```
What does this mean for attackers? An analyst can attempt to understand a program’s function through its control flow; while problematic, logic and control flow is almost effortless to manipulate and make arbitrarily confusing. When dealing with control flow, an attacker aims to introduce enough obscure and arbitrary logic to confuse an analyst but not too much to raise further suspicion or potentially be detected by a platform as malicious.
In the upcoming task, we will discuss different control flow patterns an attacker can use to confuse an analyst.
Can logic change and impact the control flow of a program? (T/F)
*T*
### Arbitrary Control Flow Patterns
