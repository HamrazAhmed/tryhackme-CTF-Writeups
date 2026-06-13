---
Learn about the data acquisition techniques and tools used in iOS device digital forensics!
---

# iOS Forensics — Writeup

## Overview
### iOS Forensics — Writeup
### iOS Forensics — Writeup
![](https://assets.tryhackme.com/room-banners/iosforensics.png)
![|222](https://tryhackme-images.s3.amazonaws.com/room-icons/065b3e2e59dc5598190ececd1a1c2339.png)
### 1. Introduction
![|222](https://i.imgur.com/zFqPlnI.png)
Howdy! Welcome to one of my favourite subsets of the best thing that is Digital Forensics and Incidence Response.
Not only are you going to be learning the fundamentals of iOS forensics, but you're also going to apply all knowledge found within this room in analysing an actual iPhone in "Operation JustEncase"
If this type of content is well received, I'll pursue into continuing with making some more forensics-focused content.
With that being said, let's get started. Buckle up! ~CMNatic
### 2. What is Digital Forensics and how is it Used Today?
Digital forensics is the mere digitisation of the traditional use and applications of forensic investigation, for example, within police departments after a crime has been committed.
Artefacts such as blood, fingerprints or hair fibres are used in criminal investigations to paint a picture of the events that took place and who was involved. Digital forensics is the same collection of artefacts, however, these artefacts being events on a digital device.
Removing evidence or covering your tracks is a fallacy to some extent - especially with digital devices. Someone may be able to hide exactly what they were doing, however, the act of hiding this will, in turn, leave the trace of something behind hidden.
Take the screenshot below as an example. This picture is an abstract view of what is known as an image of a hard drive.
Images are bit-for-bit replications of devices, aptly titled "images" giving a nod to photography. These images can derive from anything such as a SatNavs for a car, a smart TV, to a router and a full-on server.
This picture shows the raw data obtained from an imaged hard drive. As we can see, it's all full of zeros - blank!
![](https://i.imgur.com/cCm0s4U.png)
If this hard drive was just taken from a laptop for example, then we would expect to see a lot of contents here, not just a whole bunch of zeros, such as we see in the screenshot below.
![](https://i.imgur.com/8XyCAE4.png)
You don't have to be a forensic investigator to understand that we will find nothing meaningful on a hard drive full of zeros. However, it's what isn't there anymore that is indicative. Obviously, some efforts have been made to hide data - awfully suspicious huh?
As you'll come to discover, digital devices hold plethoras of information, and in turn, evidence about our activities. In this room we'll be analysing an iOS device, however, as the Internet of Things (IoT) expands, there's a possibility your toaster can be used as evidence against you. Because of how personal IoT devices are, they serve as goldmines for analysts.
For example. You may consider the privacy of your browsing and social media, but then you have a smart meter in the house! As (S. Kim et al, 2020) were able to create a day-to-day schedule of a participant's actions simply by using the timestamps of when doors open and close - all from the data stored within a Samsung SmartThings.
It is the same method in how a famous vigilante hacker was caught; law enforcement was able to match the timestamps of them logging into a website with the exact time they used their internet service provider. As things become more integrated within our lives, albeit with the aims of benefiting us, day-by-day they become more likely to be used against us.
Real-World Uses:
Digital forensics isn't only used in investigations by the authorities but has an extremely heavy and necessary footprint in every sector of the world. All too often we often hear about companies being hacked (fourth wall break?). Companies need to understand the chain of events on how they were breached and what data was taken, this is known as incidence response.
Not only this but, digital forensics serves a large role in civil and workplace matters. A few examples that come to mind is determining whether or not an employee is selling trade secrets to a competitor. Who is selling them, what secrets are being sold? And more importantly - who to?
One of the only times that digital forensics is in your favour is the recovery of lost data, but the details of that are for a future room or two.
What would look more suspicious? an empty hard drive or a full hard drive?
*an empty hard drive*
What is the definition for an abstract view of a hard drive?
*image*
### 3. Problems Facing Digital Forensic Analysts
Time Consumption & Resources
Digital forensics is, without doing it justice, an incredibly time-consuming process. Despite the toolkits and suites available, you find yourself having to analyse data bit-by-bit to find that one smoking gun. Now extend that to a 1TB drive - not so fun huh.
With the very nature of forensic images being exact bit-for-bit copies of an acquired device or system, you need to have the facilities to be able to store this data before it can be processed. Take a file server full of data with 10 terabytes of data. You need 10 terabytes to store that on as well, slapping on another 10 terabytes required for the backups of the image that you make; suddenly you have at least 20 terabytes sitting around.
Understanding the Person
As a forensic analyst, you have to piece various parts of information together, into a formal and well-documented timeline of events for presentation. For example, if you were to try to find a bit of text in a document on your computer, you'd know where to go. Now take away the desktop/GUI and terminal then ask your friend to try and find it through the means similar to the screenshot in Task 2. Pretty hard huh?
Encryption
As it stands, an effective and secure implementation of encryption poses as one of the biggest hurdles to forensic analysts. The problem mostly? People and/or devices themselves leave the decryption keys within the same platform. Such as in the case of the iPhone you are going to analyse. After all, it's that catch-22 of a complex password is a strong password until you need to write it down.
Steganography
We all know (and love) steganography here; Hiding data within data. And in some cases, is more secure then cryptography; seeing as cryptography makes the contents unreadable, steganography masquerades the entire existence of this data altogether. (Din et al., 2018)
Cost of Entry
Sure, you can pick up FTK Imager lite or Autopsy for free, but these tool suites - whilst being lifesavers, are only the tip of the iceberg in digital forensics.
For example, you're not going to be creating any file system images of iPhones in FTK Imager lite, and if so, you're going through it bit-for-bit if it is at all unencrypted.
Enter infamous companies such as Cellebrite. This company are arguably the forefront of data acquisition. Costing approximately $15,000 for the equipment and adapters, specialist kits such these aren't available to hobbyists - only to law enforcement, government agencies and specific Universities. Cellebrite was used to dump this iPhone.
Let alone the cost of purchasing sophisticated tools, there is a heavy expectation of certifications and even degrees; that's what filled most of my 3 years at University!
### 4. iOS File Systems
Apple, in their notorious way of doing things, have created their own sets of file system formattings: AFS and HFS+
Starting with the oldest, HFS+ or Mac OS Extended is the legacy file system used by Apple all the way in 1998 and is still supported today. The issue being that HFS was not future proof - given the fact it cannot support file timestamps past February 6th, 2040 ([Vigo., 2018](https://www.techrepublic.com/article/apfs-vs-hfs-which-apple-filesystem-is-better/)).
Whilst HFS+ didn't support encryption at its entirety (a win in our books as forensic analysts) any device such as iMac or iPhone past iOS 10.3 will have had their file system converted from HFS+ to AFS automatically.
AFS or Apple File System (creative right...!) boasts many features, including full disk encryption, worrisome for analysts considering all devices past iOS 10.3 will have this system structure. But from a design point of view, AFS introduces smarter data management such as in the screenshot below, where a file requiring 3 blocks worth of space when copied, would require another 3 blocks again.
![](https://i.imgur.com/PSSKfkg.png)
Instead of writing and storing the entire data again (taking up six blocks in our example), AFS simply creates another reference to the file (only taking up a total of four blocks in our example), similar to inodes in Linux.
### 5. Modern iOS Security
Throughout the years of design, Apple's operating system for its iOS devices has ten-folded in measure of protecting their user's data. So much so, companies have made their reputation purely by being the ones who can unlock iPhones. The ability to do so for law enforcement / governmental authorities is a sprint race behind very, very closed doors.
For example, Elcomsoft recently announced being able to acquisition file system data from iPhones running iOS 13 and 13.3 without any jailbreaking. That in of itself is groundbreaking in mobile device forensics. And that's only what we've been told about!
But We're Average Joes Here
We can't be paying thousands for bits of kit and licensing. Nor do we have the space to carry every phone adapter from Nokia's to A or Micro-B cables - take the Cellebrite UFED for example:
![](https://i.imgur.com/j9I6ZJ0.png)
Absolutely fantastic bits of kit.
You might be thinking, but surely with all of the security measures iPhones have these days such as Touch-ID and Face ID on top of the passcode, your data is safe, right?
Well, toolkits such as this UFED can use all of the acquisition methods that we discussed in task 8. However, what's worth noting is that the UFED is capable of forcing the iDevice to boot using UFED's custom boot loader, bypassing the entire iOS operating system - similar to rooting an android; resulting in an entire dump of the entire device.
The issue with this? It contradicts the golden rule of digital forensics: Never turn it off.
People often install "panic switches" into devices, where a shutdown event could trigger an entire wiping of the device. Or in the case of iPhones, if the iPhone isn't properly isolated, it can be remotely wiped via the iCloud - a very true story.
iOS' "Restricted Mode"
Since 2018, Apple enforced a "Restricted Mode" on all iDevices running that version and above. This feature disables the input/output of data functionality from the lightning (charge) cable until the iPhone is unlocked with a passcode. Devices must be trusted before any data can be written - or so as by design.
Ever seen a warning like this?
![](https://i.imgur.com/crzaqYP.png)
That'll be Apple's "Restricted Mode" at play. In this stage, the iPhone will charge, but any data cannot be written or read in its current state.
### 6. Data Acquisition & Trust Certificates
This room is going to situate ourselves as digital forensic experts for a police department, and as such, we'll discuss the techniques that - we - as experts would use and the issues surrounding them.
In modern-day digital forensics, there are four primary methods and procedures followed when trying to retrieve data from devices such as iPhones. How an analyst approaches a device is arguably the most important decision they'll make. If the wrong call was made, data that could have been retrieved may end up deleted, or just as worse, inadmissible as evidence due to incorrect technique or failure to follow policy.
In a court of law, any evidence submitted must be admissible. This complex process involves the "chain of custody". No matter how indicting a piece of evidence is, it can be dismissed if there is insufficient documentation and/or negligence in handling - all the way from the crime scene to the courtroom.
Entire policing frameworks are built solely to ensure the integrity of digital evidence such as the "[ACPO Good Practice Guide](https://www.digital-detective.net/digital-forensics-documents/ACPO_Good_Practice_Guide_for_Digital_Evidence_v5.pdf)" for police forces in the UK. I really encourage a read through!
The Four Primary Methods:
```text
Method	Use Case
Direct acquisition
	Interacting with the device itself if, for example, it was found unlocked. No need to bypass anything!
Logical/backup acquisition
	

Utilising the iTunes backup of a phone for file system entry, or the use of forensics software to analyse data found within these backups i.e. .plists 
Advanced logical acquisition
	Using the escalated privileges to an iPhones file system found when pairing an iOS device to a Computer using either iTunes or Xcode.
Physical acquisition
	The most direct approach, physical acquisition is the use of forensic imaging kits such as Cellebrite to take entire bit-for-bit copies of both the data and system partitions. Unsophisticated tools (such as those that don't launch the iPhone into a custom boot loader) will leave the data encrypted.
```
Direct Acquisition:
Perhaps one of the only times where it could be argued that Cellebrite's "Physical Analyzer" has more bells and whistles then what's needed for the job. Non-forensically focused, and most importantly free, applications such as the iFunbox perform the same job in this scenario.
Direct acquisition covers three scenarios:
1. There is no password on the phone
2. There is a password but it is known to the analyst
3. The analyst has a "Lockdown Certificate" which is what we'll come onto in just a bit.
Whilst this sounds appealing, applications such as the iFunbox are capable of writing to the device being analysed. Because of this, the image made will now be inadmissible as evidence due to the fact that there's a possibility data was (over)written to the device that wasn't from the suspect - a defence attorney can argue the data could have been left by the forensic analyst.
Logical or Backup Acquisition:
Also applicable to the three scenarios above, the backup acquisition is the cheapest way of acquiring data from a device such as an iPhone. By using iTunes' backup facility, analysts can simply use a computer that has been paired with the iPhone before. However, Logical acquisition is where the big money starts to roll in. You're going to be hearing of Cellebrite a lot, they're quite the giant in a very specialist field because of their incredible kit, making the actual stage of accumulating data ten-fold.
After all, if you can't analyse a phone - just analyse the unlocked PC that has an entire backup upon it, right?
iTunes Backups & Trust Certificates
The analysis of iPhone backups made with iTunes is an interesting topic, to say the very least. When backing up an iPhone, iTunes accesses the iPhone in a privileged state - similar to using the sudo command on Linux to run a command with root privileges.
iPhones will only backup to trusted computers. When plugging into a new device, the iPhone will ask the user whether or not they wish to trust the computer - as seen in the screenshot below:
![|333](https://i.imgur.com/x0biqfV.png)
"Trusting" a computer involves generating a pair certificate on both the iPhone and computer. If the certificate matches up on both devices, the iPhone can be backed up. This process is a fantastic security measure by Apple, namely to prevent attacks such as "Juice Jacking".
A lockdown certificate stored within /private/var/db/lockdown on later iOS devices or /private/var/Lockdown on older iOS devices, looking like the screenshot below:
![|888](https://i.imgur.com/Q1cqd09.png)
On the computer, in my case Windows, this certificate is stored in C:\ProgramData\Apple\Lockdown
![](https://i.imgur.com/BDXjSyv.png)
Where the contents look like so, albeit the screenshot is only a snippet. The certificate within the computer contains the private keys used to encrypt and decrypt against the iPhones public key:
![](https://i.imgur.com/NtiIjLM.png)
